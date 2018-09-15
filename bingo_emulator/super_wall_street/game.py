#!/usr/bin/python

import logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
import procgame.game, sys, os
import procgame.config
import random
import procgame.sound

sys.path.insert(0,os.path.pardir)
import bingo_emulator.common.units as units
import bingo_emulator.common.functions as functions
from bingo_emulator.graphics import methods as graphics
from bingo_emulator.graphics.super_wall_street import *

class MulticardBingo(procgame.game.Mode):
    def __init__(self, game):
        super(MulticardBingo, self).__init__(game=game, priority=5)
        self.holes = []
        self.startup()
        self.game.sound.register_music('motor', "audio/six_card_motor.wav")
        self.game.sound.register_sound('search', "audio/mystic_line_search.wav")
        self.game.sound.register_sound('add', "audio/six_card_add_card.wav")
        self.game.sound.register_sound('tilt', "audio/tilt.wav")
        self.game.sound.register_sound('step', "audio/step.wav")

    def sw_coin_active(self, sw):
        self.game.tilt.disengage()
        self.regular_play()
        self.delay(name="display", delay=0.1, handler=graphics.super_wall_street.display, param=self)

    def sw_startButton_active(self, sw):
        if self.game.replays > 0 or self.game.switches.freeplay.is_active():
            self.game.tilt.disengage()
            self.regular_play()
            self.delay(name="display", delay=0.1, handler=graphics.super_wall_street.display, param=self)

    def sw_trough4_active_for_1s(self, sw):
        if self.game.ball_count.position >= 4:
            self.game.probability.spin()
            self.timeout_actions()
    
    def timeout_actions(self):
        if (self.game.timer.position < 7):
            self.game.sound.play_music('motor', -1)
            self.game.timer.step()
            self.delay(name="timeout", delay=5.0, handler=self.timeout_actions)
        else:
            self.game.timer.step()
            self.game.sound.stop_music()

    def sw_trough8_closed(self, sw):
        if self.game.start.status == False:
            if self.game.ball_count.position >= 5:
                self.game.returned = True
            self.game.ball_count.position -= 1
            self.check_lifter_status()
        else:
            self.check_lifter_status()

    def sw_enter_active(self, sw):
        if self.game.switches.left.is_active() and self.game.switches.right.is_active():
            self.game.end_run_loop()
            os.system("/home/nbaldridge/proc/bingo_emulator/start_game.sh super_wall_street")
        else:
            if self.game.ball_count.position >= 4:
                self.game.sound.stop_music()
                if self.game.search_index.status == False:
                    self.game.sound.play('search')
                    self.search()
                    self.game.timer.reset()
                    self.timeout_actions()

    def check_shutter(self, start=0):
        if start == 1:
            if self.game.switches.smRunout.is_active():
                if self.game.switches.shutter.is_active():
                    self.game.coils.shutter.disable()
        else:
            if self.game.switches.shutter.is_inactive():
                if self.game.switches.smRunout.is_active():
                    self.game.coils.shutter.disable()

    def regular_play(self):
        self.holes = []
        self.cancel_delayed(name="search")
        self.cancel_delayed(name="card1_replay_step_up")
        self.cancel_delayed(name="card2_replay_step_up")
        self.cancel_delayed(name="card3_replay_step_up")
        self.cancel_delayed(name="blink_double")
        self.cancel_delayed(name="timeout")
        self.game.search_index.disengage()
        self.game.coils.counter.pulse()
        self.game.returned = False
        self.game.sound.stop('add')
        self.game.sound.play('add')
        self.game.reflex.decrease()
        if self.game.reflex.position < 40:
            self.game.cu = 1
        else:
            self.game.cu = 0
        self.game.probability.spin()
        if self.game.start.status == True:
            if self.game.selector.position < 7:
                self.game.selector.step()
                if self.check_corners() == True:
                    if self.game.selector.position == 1:
                        self.game.corners1.engage(self.game)
                        self.game.sound.play('tilt')
                    elif self.game.selector.position == 2:
                        self.game.corners2.engage(self.game)
                        self.game.sound.play('tilt')
                    elif self.game.selector.position == 3:
                        self.game.corners3.engage(self.game)
                        self.game.sound.play('tilt')
                if self.game.selector.position == 4:
                    self.game.super1.engage(self.game)
                    self.game.sound.play('tilt')
                if self.game.selector.position == 5:
                    self.game.super2.engage(self.game)
                    self.game.sound.play('tilt')
                if self.game.selector.position == 6:
                    self.game.super3.engage(self.game)
                    self.game.sound.play('tilt')
                if self.game.switches.shutter.is_inactive():
                    self.game.coils.shutter.enable()
                self.replay_step_down()
                self.check_lifter_status()
        else:
            self.game.card1_replay_counter.reset()
            self.game.card2_replay_counter.reset()
            self.game.card3_replay_counter.reset()
            self.game.super1.disengage()
            self.game.super2.disengage()
            self.game.super3.disengage()
            self.game.card1_double.disengage()
            self.game.card1_regular.disengage()
            self.game.card1_missed.disengage()
            self.game.card2_double.disengage()
            self.game.card2_regular.disengage()
            self.game.card2_missed.disengage()
            self.game.card3_double.disengage()
            self.game.card3_regular.disengage()
            self.game.card3_missed.disengage()
            self.game.corners1.disengage()
            self.game.corners2.disengage()
            self.game.corners3.disengage()
            self.game.start.engage(self.game)
            self.game.selector.reset()
            self.game.ball_count.reset()
            self.game.sound.play_music('motor', -1)
            self.regular_play()
        self.delay(name="display", delay=0.1, handler=graphics.super_wall_street.display, param=self)
        self.game.tilt.disengage()

    def check_lifter_status(self):
        if self.game.tilt.status == False:
            if self.game.switches.trough8.is_closed() and self.game.switches.trough5.is_open() and self.game.switches.trough4.is_open() and self.game.switches.trough3.is_closed() and self.game.switches.trough2.is_closed():
                if self.game.switches.shooter.is_open():
                    self.game.coils.lifter.enable()
                    self.game.returned = False
            else:
                if self.game.start.status == False:
                    if self.game.switches.trough4.is_open():
                        if self.game.switches.shooter.is_open():
                            if self.game.switches.gate.is_closed():
                                self.game.coils.lifter.enable()
                    else:
                        if self.game.switches.trough4.is_closed():
                            if self.game.selector.position >= 7:
                                if self.game.switches.shooter.is_open() and self.game.switches.trough3.is_closed():
                                    self.game.coils.lifter.enable()
                    if self.game.returned == True and self.game.ball_count.position == 5 and self.game.selector.position >= 7:
                        if self.game.switches.shooter.is_open():
                            self.game.coils.lifter.enable()
                            self.game.returned = False
                    if self.game.returned == True and self.game.ball_count.position == 4:
                        if self.game.switches.shooter.is_open():
                            self.game.coils.lifter.enable()
                            self.game.returned = False

    def sw_smRunout_active_for_1ms(self, sw):
        if self.game.start.status == True:
            self.check_shutter(1)
        else:
            self.check_shutter()

    def sw_trough1_closed(self, sw):
        if self.game.switches.shooter.is_closed():
            self.game.coils.lifter.disable()

    def sw_ballLift_active_for_500ms(self, sw):
        if self.game.tilt.status == False:
            if self.game.switches.shooter.is_open():
                if self.game.ball_count.position < 5:
                    self.game.coils.lifter.enable()

    def sw_gate_inactive_for_1ms(self, sw):
        self.game.start.disengage()
        if self.game.switches.shutter.is_active():
            self.game.coils.shutter.enable()
        self.game.ball_count.step()
        if self.game.ball_count.position == 4:
            self.game.sound.stop_music()
            self.game.sound.play('tilt')
            self.game.sound.play('tilt')
        self.game.probability.spin()
        if self.game.ball_count.position <= 5:
            self.check_lifter_status()

    # This is really nasty, but it is how we render graphics for each individual hole.
    # numbers are added (or removed from) a list.  In this way, I can re-use the same
    # routine even for games where there are ball return functions like Surf Club.

    def sw_hole1_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(1)
            self.delay(name="display", delay=0.1, handler=graphics.super_wall_street.display, param=self)

    def sw_hole2_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(2)
            self.delay(name="display", delay=0.1, handler=graphics.super_wall_street.display, param=self)

    def sw_hole3_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(3)
            self.delay(name="display", delay=0.1, handler=graphics.super_wall_street.display, param=self)

    def sw_hole4_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(4)
            self.delay(name="display", delay=0.1, handler=graphics.super_wall_street.display, param=self)

    def sw_hole5_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(5)
            self.delay(name="display", delay=0.1, handler=graphics.super_wall_street.display, param=self)

    def sw_hole6_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(6)
            self.delay(name="display", delay=0.1, handler=graphics.super_wall_street.display, param=self)

    def sw_hole7_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(7)
            self.delay(name="display", delay=0.1, handler=graphics.super_wall_street.display, param=self)

    def sw_hole8_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(8)
            self.delay(name="display", delay=0.1, handler=graphics.super_wall_street.display, param=self)

    def sw_hole9_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(9)
            self.delay(name="display", delay=0.1, handler=graphics.super_wall_street.display, param=self)

    def sw_hole10_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(10)
            self.delay(name="display", delay=0.1, handler=graphics.super_wall_street.display, param=self)

    def sw_hole11_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(11)
            self.delay(name="display", delay=0.1, handler=graphics.super_wall_street.display, param=self)

    def sw_hole12_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(12)
            self.delay(name="display", delay=0.1, handler=graphics.super_wall_street.display, param=self)

    def sw_hole13_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(13)
            self.delay(name="display", delay=0.1, handler=graphics.super_wall_street.display, param=self)

    def sw_hole14_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(14)
            self.delay(name="display", delay=0.1, handler=graphics.super_wall_street.display, param=self)

    def sw_hole15_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(15)
            self.delay(name="display", delay=0.1, handler=graphics.super_wall_street.display, param=self)

    def sw_hole16_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(16)
            self.delay(name="display", delay=0.1, handler=graphics.super_wall_street.display, param=self)

    def sw_hole17_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(17)
            self.delay(name="display", delay=0.1, handler=graphics.super_wall_street.display, param=self)

    def sw_hole18_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(18)
            self.delay(name="display", delay=0.1, handler=graphics.super_wall_street.display, param=self)

    def sw_hole19_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(19)
            self.delay(name="display", delay=0.1, handler=graphics.super_wall_street.display, param=self)

    def sw_hole20_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(20)
            self.delay(name="display", delay=0.1, handler=graphics.super_wall_street.display, param=self)

    def sw_hole21_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(21)
            self.delay(name="display", delay=0.1, handler=graphics.super_wall_street.display, param=self)

    def sw_hole22_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(22)
            self.delay(name="display", delay=0.1, handler=graphics.super_wall_street.display, param=self)

    def sw_hole23_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(23)
            self.delay(name="display", delay=0.1, handler=graphics.super_wall_street.display, param=self)

    def sw_hole24_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(24)
            self.delay(name="display", delay=0.1, handler=graphics.super_wall_street.display, param=self)

    def sw_hole25_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(25)
            self.delay(name="display", delay=0.1, handler=graphics.super_wall_street.display, param=self)

    def sw_replayReset_active(self, sw):
        self.game.anti_cheat.disengage()
        self.holes = []
        graphics.super_wall_street.display(self, 0)
        self.tilt_actions()
        self.replay_step_down(self.game.replays)

    def tilt_actions(self):
        self.game.start.disengage()
        self.cancel_delayed(name="replay_reset")
        self.cancel_delayed(name="card1_replay_step_up")
        self.cancel_delayed(name="card2_replay_step_up")
        self.cancel_delayed(name="card3_replay_step_up")
        self.cancel_delayed(name="blink_double")
        self.cancel_delayed(name="timeout")
        self.game.search_index.disengage()
        if self.game.ball_count.position == 0:
            if self.game.switches.shutter.is_active():
                self.game.coils.shutter.enable()
        self.holes = []
        self.game.selector.reset()
        self.game.ball_count.reset()
        self.game.anti_cheat.engage(game)
        self.game.tilt.engage(self.game)
        self.game.sound.stop_music()
        self.game.sound.play('tilt')
        # displays "Tilt" on the backglass, you have to recoin.
        self.delay(name="display", delay=0.1, handler=graphics.super_wall_street.display, param=self)

    def sw_tilt_active(self, sw):
        if self.game.tilt.status == False:
            self.tilt_actions()

    def replay_step_down(self, number=0):
        if number > 0:
            if number > 1:
                self.game.replays -= 1
                graphics.replay_step_down(self.game.replays, graphics.super_wall_street.reel1, graphics.super_wall_street.reel10, graphics.super_wall_street.reel100, graphics.super_wall_street.reel1000)
                self.game.coils.registerDown.pulse()
                number -= 1
                graphics.super_wall_street.display(self)
                self.delay(name="replay_reset", delay=0.13, handler=self.replay_step_down, param=number)
            elif number == 1:
                self.game.replays -= 1
                graphics.replay_step_down(self.game.replays, graphics.super_wall_street.reel1, graphics.super_wall_street.reel10, graphics.super_wall_street.reel100, graphics.super_wall_street.reel1000)
                self.game.coils.registerDown.pulse()
                number -= 1
                graphics.super_wall_street.display(self)
                self.cancel_delayed(name="replay_reset")
        else: 
            if self.game.replays > 0:
                self.game.replays -= 1
                graphics.replay_step_down(self.game.replays, graphics.super_wall_street.reel1, graphics.super_wall_street.reel10, graphics.super_wall_street.reel100, graphics.super_wall_street.reel1000)
                self.delay(name="display", delay=0.1, handler=graphics.super_wall_street.display, param=self)
            self.game.coils.registerDown.pulse()

    def replay_step_up(self):
        if self.game.replays < 8999:
            self.game.replays += 1
            graphics.replay_step_up(self.game.replays, graphics.super_wall_street.reel1, graphics.super_wall_street.reel10, graphics.super_wall_street.reel100, graphics.super_wall_street.reel1000)
        self.game.reflex.increase()
        self.game.coils.registerUp.pulse()
        graphics.super_wall_street.display(self)
 
    def search(self):
        # The search workflow/logic will determine if you actually have a winner, but it is a bit tricky.
        # if the ball is in a particular hole, the search relays need to click and/or clack, and 
        # when you have at least three going at once, it should latch on the search index and score.
        # This scoring is tempered by the selector disc.  You have to have the card enabled that you're
        # winning on.  This whole process will have to happen on a rotational basis.  The search should really
        # begin immediately upon the first ball landing in the hole.
        # I suspect that the best, fastest way to complete the search is actually to reimplement the mechanical
        # search activity.  For each revolution of the search disc (which happens about every 5-7 seconds), the
        # game will activate() each search relay for each 'hot' rivet on the search disc.  This can be on a different
        # wiper finger for each set of rivets on the search disc.
        # Replay counters also need to be implemented to prevent the supplemental searches from scoring.

        self.cancel_delayed(name="research")
        for i in range(0, 50):
            self.r = self.closed_search_relays(self.game.searchdisc.position, self.game.corners1.status, self.game.corners2.status, self.game.corners3.status)
            self.game.searchdisc.spin()
            self.wipers = self.r[0]
            self.card = self.r[1]
            self.corners = self.r[2]

            # From here, I need to determine based on the value of r, whether to latch the search index and score. For Bright Lights,
            # I need to determine the best winner on each card.  To do this, I must compare the position of the replay counter before
            # determining the winner. Reminder that my replay counters are a 1:1 representation.

            self.match = []
            for key in self.wipers:
                for number in self.holes:
                    if number == key:
                        self.match.append(self.wipers[key])
                        relays = sorted(set(self.match))
                        #TODO Play sound for each relay closure.
                        s = functions.count_seq(relays)
                        if self.game.selector.position >= self.card:
                            if self.card == 1:
                                g = self.game.card1_missed.status
                            elif self.card == 2:
                                g = self.game.card2_missed.status
                            elif self.card == 3:
                                g = self.game.card3_missed.status
                            if g == False:
                                if s >= 3:
                                    self.find_winner(s, self.card, self.corners)

    def find_winner(self, relays, card, corners):
        if self.game.search_index.status == False and self.game.replays < 8999:
            if self.game.card1_missed.status == False:
                if card == 1:
                    if relays == 3:
                        if corners == True:
                            pass
                        else:
                            if self.game.card1_replay_counter.position < 4:
                                self.game.search_index.engage(self.game)
                                self.game.sound.stop('search')
                                self.wait_for_input((1, 4))
                    if relays == 4:
                        if corners == True:
                            if self.game.corners1.status == True:
                                if self.game.super1.status == True:
                                    if self.game.card1_replay_counter.position < 200:
                                        self.game.search_index.engage(self.game)
                                        self.game.sound.stop('search')
                                        self.wait_for_input((1, 200))
                                else:
                                    if self.game.card1_replay_counter.position < 100:
                                        self.game.search_index.engage(self.game)
                                        self.game.sound.stop('search')
                                        self.wait_for_input((1, 100))
                        else:
                            if self.game.super1.status == True:
                                if self.game.card1_replay_counter.position < 24:
                                    self.game.search_index.engage(self.game)
                                    self.game.sound.stop('search')
                                    self.wait_for_input((1, 24))
                            else:
                                if self.game.card1_replay_counter.position < 12:
                                    self.game.search_index.engage(self.game)
                                    self.game.sound.stop('search')
                                    self.wait_for_input((1, 12))
                    if relays == 5:
                        if self.game.super1.status == True:
                            if self.game.card1_replay_counter.position < 200:
                                self.game.search_index.engage(self.game)
                                self.game.sound.stop('search')
                                self.wait_for_input((1, 200))
                        else:
                            if self.game.card1_replay_counter.position < 100:
                                self.game.search_index.engage(self.game)
                                self.game.sound.stop('search')
                                self.wait_for_input((1, 100))
            if self.game.card2_missed.status == False:
                if card == 2:
                    if relays == 3:
                        if corners == True:
                            pass
                        else:
                            if self.game.card2_replay_counter.position < 4:
                                self.game.search_index.engage(self.game)
                                self.game.sound.stop('search')
                                self.wait_for_input((2, 4))
                    if relays == 4:
                        if corners == True:
                            if self.game.corners2.status == True:
                                if self.game.super2.status == True:
                                    if self.game.card2_replay_counter.position < 200:
                                        self.game.search_index.engage(self.game)
                                        self.game.sound.stop('search')
                                        self.wait_for_input((2, 200))
                                else:
                                    if self.game.card2_replay_counter.position < 100:
                                        self.game.search_index.engage(self.game)
                                        self.game.sound.stop('search')
                                        self.wait_for_input((2, 100))
                        else:
                            if self.game.super2.status == True:
                                if self.game.card2_replay_counter.position < 24:
                                    self.game.search_index.engage(self.game)
                                    self.game.sound.stop('search')
                                    self.wait_for_input((2, 24))
                            else:
                                if self.game.card2_replay_counter.position < 12:
                                    self.game.search_index.engage(self.game)
                                    self.game.sound.stop('search')
                                    self.wait_for_input((2, 12))
                    if relays == 5:
                        if self.game.super2.status == True:
                            if self.game.card2_replay_counter.position < 200:
                                self.game.search_index.engage(self.game)
                                self.game.sound.stop('search')
                                self.wait_for_input((2, 200))
                        else:
                            if self.game.card2_replay_counter.position < 100:
                                self.game.search_index.engage(self.game)
                                self.game.sound.stop('search')
                                self.wait_for_input((2, 100))
            if self.game.card3_missed.status == False:
                if card == 3:
                    if relays == 3:
                        if corners == True:
                            pass
                        else:
                            if self.game.card3_replay_counter.position < 4:
                                self.game.search_index.engage(self.game)
                                self.game.sound.stop('search')
                                self.wait_for_input((3, 4))
                    if relays == 4:
                        if corners == True:
                            if self.game.corners3.status == True:
                                if self.game.super3.status == True:
                                    if self.game.card3_replay_counter.position < 200:
                                        self.game.search_index.engage(self.game)
                                        self.game.sound.stop('search')
                                        self.wait_for_input((3, 200))
                                else:
                                    if self.game.card3_replay_counter.position < 100:
                                        self.game.search_index.engage(self.game)
                                        self.game.sound.stop('search')
                                        self.wait_for_input((3, 100))
                        else:
                            if self.game.super3.status == True:
                                if self.game.card3_replay_counter.position < 24:
                                    self.game.search_index.engage(self.game)
                                    self.game.sound.stop('search')
                                    self.wait_for_input((3, 24))
                            else:
                                if self.game.card3_replay_counter.position < 12:
                                    self.game.search_index.engage(self.game)
                                    self.game.sound.stop('search')
                                    self.wait_for_input((3, 12))
                    if relays == 5:
                        if self.game.super3.status == True:
                            if self.game.card3_replay_counter.position < 200:
                                self.game.search_index.engage(self.game)
                                self.game.sound.stop('search')
                                self.wait_for_input((3, 200))
                        else:
                            if self.game.card3_replay_counter.position < 100:
                                self.game.search_index.engage(self.game)
                                self.game.sound.stop('search')
                                self.wait_for_input((3, 100))

    def wait_for_input(self, i):
        if self.game.switches.drawer.is_inactive():
            if self.game.switches.left.is_inactive() and self.game.switches.right.is_inactive():
                if i[0] == 1 and self.game.card1_replay_counter.position > 0:
                    if self.game.card1_double.status == True:
                        self.cancel_delayed(name="blink_double")
                        self.delay(name="display", delay=0.1, handler=graphics.super_wall_street.display, param=self)
                        self.game.blink = 0
                        self.card1_replay_step_up((i[1] * 2) - self.game.card1_replay_counter.position)
                    else:
                        self.cancel_delayed(name="blink_double")
                        self.delay(name="display", delay=0.1, handler=graphics.super_wall_street.display, param=self)
                        self.game.blink = 0
                        self.card1_replay_step_up(i[1] - self.game.card1_replay_counter.position)
                elif i[0] == 2 and self.game.card2_replay_counter.position > 0:
                    if self.game.card2_double.status == True:
                        self.cancel_delayed(name="blink_double")
                        self.delay(name="display", delay=0.1, handler=graphics.super_wall_street.display, param=self)
                        self.game.blink = 0
                        self.card2_replay_step_up((i[1] * 2) - self.game.card2_replay_counter.position)
                    else:
                        self.cancel_delayed(name="blink_double")
                        self.delay(name="display", delay=0.1, handler=graphics.super_wall_street.display, param=self)
                        self.game.blink = 0
                        self.card2_replay_step_up(i[1] - self.game.card2_replay_counter.position)
                elif i[0] == 3 and self.game.card3_replay_counter.position > 0:
                    if self.game.card3_double.status == True:
                        self.cancel_delayed(name="blink_double")
                        self.delay(name="display", delay=0.1, handler=graphics.super_wall_street.display, param=self)
                        self.game.blink = 0
                        self.card3_replay_step_up((i[1] * 2) - self.game.card3_replay_counter.position)
                    else:
                        self.cancel_delayed(name="blink_double")
                        self.delay(name="display", delay=0.1, handler=graphics.super_wall_street.display, param=self)
                        self.game.blink = 0
                        self.card3_replay_step_up(i[1] - self.game.card3_replay_counter.position)
                else:
                    if i[0] == 1 and self.game.card1_missed.status == True:
                        self.delay(name="display", delay=0.1, handler=graphics.super_wall_street.display, param=self)
                    elif i[0] == 2 and self.game.card2_missed.status == True:
                        self.delay(name="display", delay=0.1, handler=graphics.super_wall_street.display, param=self)
                    elif i[0] == 3 and self.game.card3_missed.status == True:
                        self.delay(name="display", delay=0.1, handler=graphics.super_wall_street.display, param=self)
                    else:
                        graphics.super_wall_street.blink_double(self)
                        self.delay(name="blink_double", delay=0.2, handler=self.wait_for_input, param=i)
            if self.game.switches.left.is_active():
                self.cancel_delayed(name="blink_double")
                self.delay(name="display", delay=0.1, handler=graphics.super_wall_street.display, param=self)
                self.game.blink = 0
                if i[0] == 1:
                    self.card1_replay_step_up(i[1] - self.game.card1_replay_counter.position)
                    self.game.card1_regular.engage(self.game)
                elif i[0] == 2:
                    self.card2_replay_step_up(i[1] - self.game.card2_replay_counter.position)
                    self.game.card2_regular.engage(self.game)
                elif i[0] == 3:
                    self.card3_replay_step_up(i[1] - self.game.card3_replay_counter.position)
                    self.game.card3_regular.engage(self.game)
                self.delay(name="display", delay=0.1, handler=graphics.super_wall_street.display, param=self)
            if self.game.switches.right.is_active():
                self.cancel_delayed(name="blink_double")
                dp = self.check_double_probability()
                if dp == True:
                    if i[0] == 1:
                        self.game.card1_double.engage(self.game)
                        self.game.sound.play('tilt')
                        self.card1_replay_step_up((i[1] * 2) - self.game.card1_replay_counter.position)
                    elif i[0] == 2:
                        self.game.card2_double.engage(self.game)
                        self.game.sound.play('tilt')
                        self.card2_replay_step_up((i[1] * 2) - self.game.card2_replay_counter.position)
                    elif i[0] == 3:
                        self.game.card3_double.engage(self.game)
                        self.game.sound.play('tilt')
                        self.card3_replay_step_up((i[1] * 2) - self.game.card3_replay_counter.position)
                    self.delay(name="display", delay=0.1, handler=graphics.super_wall_street.display, param=self)
                else:
                    if i[0] == 1:
                        self.game.card1_missed.engage(self.game)
                        self.game.sound.play('tilt')
                        self.game.search_index.disengage()
                        self.cancel_delayed(name="blink_double")
                        self.delay(name="display", delay=0.1, handler=graphics.super_wall_street.display, param=self)
                        self.delay(name="research", delay=1, handler=self.search)
                    elif i[0] == 2:
                        self.game.card2_missed.engage(self.game)
                        self.game.sound.play('tilt')
                        self.game.search_index.disengage()
                        self.cancel_delayed(name="blink_double")
                        self.delay(name="display", delay=0.1, handler=graphics.super_wall_street.display, param=self)
                        self.delay(name="research", delay=1, handler=self.search)
                    elif i[0] == 3:
                        self.game.card3_missed.engage(self.game)
                        self.game.sound.play('tilt')
                        self.game.search_index.disengage()
                        self.cancel_delayed(name="blink_double")
                        self.delay(name="display", delay=0.1, handler=graphics.super_wall_street.display, param=self)
                        self.delay(name="research", delay=1, handler=self.search)
        else:
            if self.game.switches.regular.is_inactive() and self.game.switches.double.is_inactive():
                if i[0] == 1 and self.game.card1_replay_counter.position > 0:
                    if self.game.card1_double.status == True:
                        self.cancel_delayed(name="blink_double")
                        self.delay(name="display", delay=0.1, handler=graphics.super_wall_street.display, param=self)
                        self.game.blink = 0
                        self.card1_replay_step_up((i[1] * 2) - self.game.card1_replay_counter.position)
                    else:
                        self.cancel_delayed(name="blink_double")
                        self.delay(name="display", delay=0.1, handler=graphics.super_wall_street.display, param=self)
                        self.game.blink = 0
                        self.card1_replay_step_up(i[1] - self.game.card1_replay_counter.position)
                elif i[0] == 2 and self.game.card2_replay_counter.position > 0:
                    if self.game.card2_double.status == True:
                        self.cancel_delayed(name="blink_double")
                        self.delay(name="display", delay=0.1, handler=graphics.super_wall_street.display, param=self)
                        self.game.blink = 0
                        self.card2_replay_step_up((i[1] * 2) - self.game.card2_replay_counter.position)
                    else:
                        self.cancel_delayed(name="blink_double")
                        self.delay(name="display", delay=0.1, handler=graphics.super_wall_street.display, param=self)
                        self.game.blink = 0
                        self.card2_replay_step_up(i[1] - self.game.card2_replay_counter.position)
                elif i[0] == 3 and self.game.card3_replay_counter.position > 0:
                    if self.game.card3_double.status == True:
                        self.cancel_delayed(name="blink_double")
                        self.delay(name="display", delay=0.1, handler=graphics.super_wall_street.display, param=self)
                        self.game.blink = 0
                        self.card3_replay_step_up((i[1] * 2) - self.game.card3_replay_counter.position)
                    else:
                        self.cancel_delayed(name="blink_double")
                        self.delay(name="display", delay=0.1, handler=graphics.super_wall_street.display, param=self)
                        self.game.blink = 0
                        self.card3_replay_step_up(i[1] - self.game.card3_replay_counter.position)
                else:
                    if i[0] == 1 and self.game.card1_missed.status == True:
                        self.delay(name="display", delay=0.1, handler=graphics.super_wall_street.display, param=self)
                    elif i[0] == 2 and self.game.card2_missed.status == True:
                        self.delay(name="display", delay=0.1, handler=graphics.super_wall_street.display, param=self)
                    elif i[0] == 3 and self.game.card3_missed.status == True:
                        self.delay(name="display", delay=0.1, handler=graphics.super_wall_street.display, param=self)
                    else:
                        graphics.super_wall_street.blink_double(self)
                        self.delay(name="blink_double", delay=0.2, handler=self.wait_for_input, param=i)
            if self.game.switches.regular.is_active():
                self.cancel_delayed(name="blink_double")
                self.delay(name="display", delay=0.1, handler=graphics.super_wall_street.display, param=self)
                self.game.blink = 0
                if i[0] == 1:
                    self.card1_replay_step_up(i[1] - self.game.card1_replay_counter.position)
                    self.game.card1_regular.engage(self.game)
                elif i[0] == 2:
                    self.card2_replay_step_up(i[1] - self.game.card2_replay_counter.position)
                    self.game.card2_regular.engage(self.game)
                elif i[0] == 3:
                    self.card3_replay_step_up(i[1] - self.game.card3_replay_counter.position)
                    self.game.card3_regular.engage(self.game)
                self.delay(name="display", delay=0.1, handler=graphics.super_wall_street.display, param=self)
            if self.game.switches.double.is_active():
                self.cancel_delayed(name="blink_double")
                dp = self.check_double_probability()
                if dp == True:
                    if i[0] == 1:
                        self.game.card1_double.engage(self.game)
                        self.game.sound.play('tilt')
                        self.card1_replay_step_up((i[1] * 2) - self.game.card1_replay_counter.position)
                    elif i[0] == 2:
                        self.game.card2_double.engage(self.game)
                        self.game.sound.play('tilt')
                        self.card2_replay_step_up((i[1] * 2) - self.game.card2_replay_counter.position)
                    elif i[0] == 3:
                        self.game.card3_double.engage(self.game)
                        self.game.sound.play('tilt')
                        self.card3_replay_step_up((i[1] * 2) - self.game.card3_replay_counter.position)
                    self.delay(name="display", delay=0.1, handler=graphics.super_wall_street.display, param=self)
                else:
                    if i[0] == 1:
                        self.game.card1_missed.engage(self.game)
                        self.game.sound.play('tilt')
                        self.game.search_index.disengage()
                        self.cancel_delayed(name="blink_double")
                        self.delay(name="display", delay=0.1, handler=graphics.super_wall_street.display, param=self)
                        self.delay(name="research", delay=1, handler=self.search)
                    elif i[0] == 2:
                        self.game.card2_missed.engage(self.game)
                        self.game.sound.play('tilt')
                        self.game.search_index.disengage()
                        self.cancel_delayed(name="blink_double")
                        self.delay(name="display", delay=0.1, handler=graphics.super_wall_street.display, param=self)
                        self.delay(name="research", delay=1, handler=self.search)
                    elif i[0] == 3:
                        self.game.card3_missed.engage(self.game)
                        self.game.sound.play('tilt')
                        self.game.search_index.disengage()
                        self.cancel_delayed(name="blink_double")
                        self.delay(name="display", delay=0.1, handler=graphics.super_wall_street.display, param=self)
                        self.delay(name="research", delay=1, handler=self.search)


    def check_double_probability(self):
        pos = self.game.probability.spin()
        if pos in [1,4,5,6,8,10,11,15,16,17,19,21,22,24,25,27,29,30,33,34,39,40,44,46,48]:
            return 1
        elif self.game.probability.position in [3,10]:
            if self.game.cu:
                return 1
        else:
            return 0

    def check_corners(self):
        pos = self.game.probability.position
        if self.game.cu:
            if self.game.selector.position <= 4:
                if pos in [0,5,10,11,30,6,14,29,36,42]:
                    return 1
            else:
                if pos in [6,14,29,36,42]:
                    return 1
            return 0
        else:
            if self.game.selector.position <= 4:
                if pos in [0,1,3,5,7,8,10,11,12,13,17,19,23,28,30,32,35,37,40,43,45,48]:
                    return 1
            else:
                if pos in [6,14,29,36,42]:
                    return 1
            return 0
            
    def card1_replay_step_up(self, number):
        self.game.sound.stop_music()
        if number >= 1:
            self.game.card1_replay_counter.step()
            number -= 1
            self.replay_step_up()
            if self.game.replays == 8999:
                number = 0
            self.delay(name="card1_replay_step_up", delay=0.1, handler=self.card1_replay_step_up, param=number)
        else:
            self.game.search_index.disengage()
            self.cancel_delayed(name="card1_replay_step_up")
            self.search()

    def card2_replay_step_up(self, number):
        self.game.sound.stop_music()
        if number >= 1:
            self.game.card2_replay_counter.step()
            number -= 1
            self.replay_step_up()
            if self.game.replays == 8999:
                number = 0
            self.delay(name="card2_replay_step_up", delay=0.1, handler=self.card2_replay_step_up, param=number)
        else:
            self.game.search_index.disengage()
            self.cancel_delayed(name="card2_replay_step_up")
            self.search()

    def card3_replay_step_up(self, number):
        self.game.sound.stop_music()
        if number >= 1:
            self.game.card3_replay_counter.step()
            number -= 1
            self.replay_step_up()
            if self.game.replays == 8999:
                number = 0
            self.delay(name="card3_replay_step_up", delay=0.1, handler=self.card3_replay_step_up, param=number)
        else:
            self.game.search_index.disengage()
            self.cancel_delayed(name="card3_replay_step_up")
            self.search()

    def closed_search_relays(self, rivets, c1, c2, c3):
        # This function is critical, as it will determine which card is returned, etc.  I need to check both the position of the
        # replay counter for the card, as well as the selector unit to ensure that the card is selected. We will get a row back
        # that has the numbers on the position which will return the search relay connected.  When three out of the five relays
        # are connected, we get a winner!
        
        # The orientation of the rivets shows that cards are scanned in reverse order on the search discs.  This is FUUUNNNKY.
        # I am taking the liberty of rearranging these to make logical sense.  Starting at position 8, the game in reality scans
        # for corners on card #3.

        # I am also changing the way corners are scored.  Since search relay #3 is not used, I cannot emulate 100%.  My search
        # function _requires_ that the relays are sequential.  I'm not rewriting a well-working search function just to emulate
        # the relays correctly.  You know, since they don't exist in this game. :-)

        self.pos = {}
        # Card 1
        self.pos[0] = {}
        self.pos[1] = {5:1, 6:2, 9:3, 3:4}
        self.pos[2] = {3:1, 21:2, 17:3, 19:4, 5:5}
        self.pos[3] = {6:1, 20:2, 17:3, 22:4, 9:5}
        self.pos[4] = {3:1, 7:2, 10:3, 4:4, 9:5}
        self.pos[5] = {24:1, 21:2, 18:3, 22:4, 8:5}
        self.pos[6] = {15:1, 14:2, 17:3, 11:4, 2:5}
        self.pos[7] = {13:1, 20:2, 12:3, 19:4, 23:5}
        self.pos[8] = {6:1, 25:2, 16:3, 1:4, 5:5}
        self.pos[9] = {3:1, 24:2, 15:3, 13:4, 6:5}
        self.pos[10] = {7:1, 21:2, 14:3, 20:4, 25:5}
        self.pos[11] = {10:1, 18:2, 17:3, 12:4, 16:5}
        self.pos[12] = {4:1, 22:2, 11:3, 19:4, 1:5}
        self.pos[13] = {9:1, 8:2, 2:3, 23:4, 5:5}
        self.pos[14] = {}
        self.pos[15] = {}

        # Card 2
        self.pos[16] = {4:1, 5:2, 7:3, 11:4}
        self.pos[17] = {4:1, 15:2, 21:3, 14:4, 11:5}
        self.pos[18] = {7:1, 18:2, 21:3, 17:4, 5:5}
        self.pos[19] = {4:1, 6:2, 1:3, 23:4, 5:5}
        self.pos[20] = {25:1, 15:2, 3:3, 17:4, 13:5}
        self.pos[21] = {9:1, 19:2, 21:3, 12:4, 20:5}
        self.pos[22] = {10:1, 18:2, 16:3, 14:4, 8:5}
        self.pos[23] = {7:1, 24:2, 22:3, 2:4, 11:5}
        self.pos[24] = {4:1, 25:2, 9:3, 10:4, 7:5}
        self.pos[25] = {6:1, 15:2, 19:3, 18:4, 24:5}
        self.pos[26] = {1:1, 3:2, 21:3, 16:4, 22:5}
        self.pos[27] = {23:1, 17:2, 12:3, 14:4, 2:5}
        self.pos[28] = {5:1, 13:2, 20:3, 8:4, 11:5}
        self.pos[29] = {}

        # Card 3
        self.pos[30] = {}
        self.pos[31] = {}
        self.pos[32] = {}
        self.pos[33] = {}
        self.pos[34] = {}
        self.pos[35] = {}
        self.pos[36] = {}
        self.pos[37] = {}
        self.pos[38] = {8:1, 6:2, 4:3, 1:4}
        self.pos[39] = {1:1, 15:2, 22:3, 14:4, 4:5}
        self.pos[40] = {8:1, 17:2, 22:3, 18:4, 6:5}
        self.pos[41] = {8:1, 23:2, 10:3, 13:4, 4:5}
        self.pos[42] = {2:1, 17:2, 16:3, 14:4, 24:5}
        self.pos[43] = {20:1, 12:2, 22:3, 19:4, 5:5}
        self.pos[44] = {25:1, 15:2, 9:3, 18:4, 11:5}
        self.pos[45] = {1:1, 7:2, 21:3, 3:4, 6:5}
        self.pos[46] = {8:1, 2:2, 20:3, 25:4, 1:5}
        self.pos[47] = {23:1, 17:2, 12:3, 15:4, 7:5}
        self.pos[48] = {10:1, 16:2, 22:3, 9:4, 21:5}
        self.pos[49] = {13:1, 14:2, 19:3, 18:4, 3:5}
        self.pos[50] = {4:1, 24:2, 5:3, 11:4, 6:5}

        corners = False
        card = 0

        if rivets in range(0,16):
            card = 1
            if rivets == 1:
                corners = True

        if rivets in range(16,30):
            card = 2
            if rivets == 16:
                corners = True

        if rivets in range(30,51):
            card = 3
            if rivets == 38:
                corners = True

        return (self.pos[rivets], card, corners)
         
    # Define reset as the knock-off, anti-cheat relay disabled, and replay reset enabled.  Motors turn while credits are knocked off.
    # When meter reaches zero and the zero limit switch is hit, turn off motor sound and leave backglass gi on, but with tilt displayed.

    def startup(self):        
        # Every bingo requires the meter to register '0' 
        # before allowing coin entry --
        # also needs to show a plain 'off' backglass.
        self.eb = False
        self.tilt_actions()

class SuperWallStreet(procgame.game.BasicGame):
    """ Super Wall Street is a reskin of Bali """
    def __init__(self, machine_type):
        super(SuperWallStreet, self).__init__(machine_type)
        pygame.mixer.pre_init(44100,-16,2,512)
        self.sound = procgame.sound.SoundController(self)
        self.sound.set_volume(1.0)
        # NOTE: trough_count only counts the number of switches present in the  trough.  It does _not_ count
        #       the number of balls present.   In this game, there  should  be  8  balls.
        self.trough_count = 6

        # Subclass my units unique to this game -  modifications must be made to set up mixers and steppers unique to the game
        # NOTE: 'top' positions are indexed using a 0 index, so the top on a 24 position unit is actually 23.

        self.searchdisc = units.Search("searchdisc", 49)

        #Seach relays
        self.s1 = units.Relay("s1")
        self.s2 = units.Relay("s2")
        self.s3 = units.Relay("s3")
        self.s4 = units.Relay("s4")
        self.s5 = units.Relay("s5")
        self.search_index = units.Relay("search_index")

        #Replay Counter
        self.card1_replay_counter = units.Stepper("card1_replay_counter", 600)
        self.card2_replay_counter = units.Stepper("card2_replay_counter", 600)
        self.card3_replay_counter = units.Stepper("card3_replay_counter", 600)

        #Initialize stepper units used to keep track of features or timing.
        self.selector = units.Stepper("selector", 7)
        self.timer = units.Stepper("timer", 8)
        self.ball_count = units.Stepper("ball_count", 5)

        #Have to keep track of which cards have corners scoring enabled.
        self.corners1 = units.Relay("corners1")
        self.corners2 = units.Relay("corners2")
        self.corners3 = units.Relay("corners3")

        #Check for status of the replay register zero switch.  If positive
        #and machine is just powered on, this will zero out the replays.
        self.replay_reset = units.Relay("replay_reset")
        
        #When engage()d, light 6v circuit, and enable game features, scoring,
        #etc. Disengage()d means that the machine is 'soft' tilted. 
        self.anti_cheat = units.Relay("anti_cheat")

        #Reflex controls extra connections to the double winners and corners trips
        self.reflex = units.Reflex("primary", 200)

        #When engage()d, spin.
        self.start = units.Relay("start")

        # Now, the control unit can be in one of two positions, essentially.
        # This alternates by coin, and is used to help portion the corners trips.
        self.cu = 1

        #The probability disc handles the dispersion of corners for each card
        #upon coin or button press.  It also handles the probability for
        #the double or nothing routine.
        self.probability = units.Spotting("probability", 50)

        #Tilt is separate from anti-cheat in that the trip will move the shutter
        #when the game is tilted with 1st ball in the lane.  Also prevents you
        #from picking back up by killing the anti-cheat.  Can be engaged by 
        #tilt bob, slam tilt switches, or timer at 39th step.
        #Immediately kills motors.
        self.tilt = units.Relay("tilt")

        self.replays = 0

        #Just a little variable to help track the status of blinking elements to make them blink in sync.
        self.blink = 0

        #Regular Winner Relays
        self.card1_regular = units.Relay("card1_regular")
        self.card2_regular = units.Relay("card2_regular")
        self.card3_regular = units.Relay("card3_regular")

        #Double Relays
        self.card1_double = units.Relay("card1_double")
        self.card2_double = units.Relay("card2_double")
        self.card3_double = units.Relay("card3_double")

        #Super Score Relays
        self.super1 = units.Relay("super1")
        self.super2 = units.Relay("super2")
        self.super3 = units.Relay("super3")

        #Missed Relays
        self.card1_missed = units.Relay("card1_missed")
        self.card2_missed = units.Relay("card2_missed")
        self.card3_missed = units.Relay("card3_missed")

        self.returned = False

    def reset(self):
        super(SuperWallStreet, self).reset()
        self.logger = logging.getLogger('game')
        self.load_config('bingo.yaml')
        
        main_mode = MulticardBingo(self)
        self.modes.add(main_mode)
        
game = SuperWallStreet(machine_type='pdb')
game.reset()
game.run_loop()
