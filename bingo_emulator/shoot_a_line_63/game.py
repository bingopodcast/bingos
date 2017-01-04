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
from bingo_emulator.graphics.shoot_a_line_63 import *

class MulticardBingo(procgame.game.Mode):
    def __init__(self, game):
        super(MulticardBingo, self).__init__(game=game, priority=5)
        self.holes = []
        self.game.anti_cheat.engage(self.game)
        self.startup()
        self.game.sound.register_music('motor', "audio/six_card_motor.wav")
        self.game.sound.register_music('search', "audio/six_card_search_old.wav")
        self.game.sound.register_sound('add', "audio/six_card_add_card.wav")
        self.game.sound.register_sound('tilt', "audio/tilt.wav")
        self.game.sound.register_sound('step', "audio/step.wav")
        self.game.sound.register_sound('eb_search', "audio/EB_Search.wav")

    def sw_coin_active(self, sw):
        self.game.tilt.disengage()
        self.regular_play()
        self.game.sound.stop('add')
        self.game.sound.play('add')
        self.delay(name="display", delay=0.1, handler=graphics.shoot_a_line_63.display, param=self)

    def sw_startButton_active(self, sw):
        if self.game.replays > 0 or self.game.switches.freeplay.is_active():
            self.game.tilt.disengage()
            self.sw_coin_active(sw)
            self.delay(name="display", delay=0.1, handler=graphics.shoot_a_line_63.display, param=self)

    def sw_trough4_active_for_1s(self, sw):
        if self.game.ball_count.position >= 4:
            self.timeout_actions()
    
    def timeout_actions(self):
        if (self.game.timer.position < 40):
            self.game.timer.step()
            print self.game.timer.position
            self.delay(delay=5.0, handler=self.timeout_actions)
        else:
            self.tilt_actions()

    def sw_trough8_inactive_for_1ms(self, sw):
        if self.game.start.status == False:
            self.game.ball_count.position -= 1
            self.game.returned = True
            self.check_lifter_status()

    def sw_enter_active(self, sw):
        if self.game.switches.left.is_active() and self.game.switches.right.is_active():
            self.game.end_run_loop()
            os.system("/home/nbaldridge/proc/bingo_emulator/start_game.sh shoot_a_line_63")

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
        self.game.cu = not self.game.cu
        self.cancel_delayed(name="search")
        self.cancel_delayed(name="lifter_status")
        self.cancel_delayed(name="card1_replay_step_up")
        self.cancel_delayed(name="card2_replay_step_up")
        self.cancel_delayed(name="card3_replay_step_up")
        self.cancel_delayed(name="card4_replay_step_up")
        self.cancel_delayed(name="card5_replay_step_up")
        self.cancel_delayed(name="card6_replay_step_up")
        self.game.search_index.disengage()
        self.game.coils.counter.pulse()
        self.game.returned = False
        if self.game.start.status == True:
            if self.game.selector.position < 6:
                self.game.selector.step()
                self.replay_step_down()
                if self.game.switches.shutter.is_inactive():
                    self.game.coils.shutter.enable()
                self.check_lifter_status()
        else:
            self.game.start.engage(self.game)
            self.game.card1_replay_counter.reset()
            self.game.card2_replay_counter.reset()
            self.game.card3_replay_counter.reset()
            self.game.card4_replay_counter.reset()
            self.game.card5_replay_counter.reset()
            self.game.card6_replay_counter.reset()
            self.game.start.engage(self.game)
            self.game.selector.reset()
            self.game.ball_count.reset()
            self.game.timer.reset()
            self.game.sound.play_music('motor', -1)
            self.regular_play()
        self.delay(name="display", delay=0.1, handler=graphics.shoot_a_line_63.display, param=self)
        self.game.tilt.disengage()

    def check_lifter_status(self):
        if self.game.tilt.status == False:
            if self.game.switches.trough8.is_inactive() and self.game.switches.trough5.is_active() and self.game.switches.trough4.is_active() and self.game.switches.trough3.is_active() and self.game.switches.trough2.is_active():
                if self.game.switches.shooter.is_inactive():
                    self.game.coils.lifter.enable()
            else:
                if self.game.switches.trough4.is_active():
                    if self.game.switches.shooter.is_inactive():
                        if self.game.switches.gate.is_active():
                            self.game.coils.lifter.enable()
            if self.game.returned == True and self.game.ball_count.position == 4:
                if self.game.switches.shooter.is_inactive():
                    self.game.coils.lifter.enable()
                    self.game.returned = False
        self.delay(name="lifter_status", delay=0, handler=self.check_lifter_status)

    def sw_smRunout_active_for_1ms(self, sw):
        if self.game.start.status == True:
            self.check_shutter(1)
        else:
            self.check_shutter()

    def sw_trough1_active(self, sw):
        if self.game.switches.shooter.is_active():
            self.game.coils.lifter.disable()

    def sw_ballLift_active_for_500ms(self, sw):
        if self.game.tilt.status == False:
            if self.game.switches.shooter.is_inactive():
                if self.game.ball_count.position < 5:
                    self.game.coils.lifter.enable()

    def sw_gate_inactive_for_1ms(self, sw):
        self.game.start.disengage()
        if self.game.switches.shutter.is_active():
            self.game.coils.shutter.enable()
        self.game.ball_count.step()
        if self.game.ball_count.position >= 4:
            if self.game.search_index.status == False:
                self.search()

    # This is really nasty, but it is how we render graphics for each individual hole.
    # numbers are added (or removed from) a list.  In this way, I can re-use the same
    # routine even for games where there are ball return functions like Surf Club.

    def sw_hole1_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(1)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.shoot_a_line_63.display, param=self)

    def sw_hole2_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(2)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.shoot_a_line_63.display, param=self)

    def sw_hole3_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(3)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.shoot_a_line_63.display, param=self)

    def sw_hole4_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(4)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.shoot_a_line_63.display, param=self)

    def sw_hole5_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(5)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.shoot_a_line_63.display, param=self)

    def sw_hole6_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(6)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.shoot_a_line_63.display, param=self)

    def sw_hole7_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(7)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.shoot_a_line_63.display, param=self)

    def sw_hole8_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(8)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.shoot_a_line_63.display, param=self)

    def sw_hole9_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(9)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.shoot_a_line_63.display, param=self)

    def sw_hole10_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(10)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.shoot_a_line_63.display, param=self)

    def sw_hole11_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(11)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.shoot_a_line_63.display, param=self)

    def sw_hole12_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(12)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.shoot_a_line_63.display, param=self)

    def sw_hole13_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(13)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.shoot_a_line_63.display, param=self)

    def sw_hole14_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(14)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.shoot_a_line_63.display, param=self)

    def sw_hole15_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(15)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.shoot_a_line_63.display, param=self)

    def sw_hole16_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(16)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.shoot_a_line_63.display, param=self)

    def sw_hole17_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(17)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.shoot_a_line_63.display, param=self)

    def sw_hole18_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(18)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.shoot_a_line_63.display, param=self)

    def sw_hole19_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(19)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.shoot_a_line_63.display, param=self)


    def sw_hole20_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(20)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.shoot_a_line_63.display, param=self)

    def sw_hole21_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(21)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.shoot_a_line_63.display, param=self)

    def sw_hole22_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(22)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.shoot_a_line_63.display, param=self)

    def sw_hole23_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(23)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.shoot_a_line_63.display, param=self)

    def sw_hole24_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(24)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.shoot_a_line_63.display, param=self)

    def sw_hole25_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(25)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.shoot_a_line_63.display, param=self)

    def sw_hole26_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(26)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.shoot_a_line_63.display, param=self)

    def sw_hole27_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(27)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.shoot_a_line_63.display, param=self)

    def sw_hole28_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(28)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.shoot_a_line_63.display, param=self)

    def sw_replayReset_active(self, sw):
        self.game.anti_cheat.disengage()
        self.holes = []
#        self.cancel_delayed(name="blink_title")
        graphics.shoot_a_line_63.display(self, 0)
        self.tilt_actions()
#        self.delay(name="blink_title", delay=1, handler=self.blink_title)
        self.replay_step_down(self.game.replays)

    def tilt_actions(self):
        self.game.start.disengage()
        self.cancel_delayed(name="replay_reset")
        self.cancel_delayed(name="card1_replay_step_up")
        self.cancel_delayed(name="card2_replay_step_up")
        self.cancel_delayed(name="card3_replay_step_up")
        self.cancel_delayed(name="card4_replay_step_up")
        self.cancel_delayed(name="card5_replay_step_up")
        self.cancel_delayed(name="card6_replay_step_up")
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
        self.delay(name="display", delay=0.1, handler=graphics.shoot_a_line_63.display, param=self)

    def sw_tilt_active(self, sw):
        if self.game.tilt.status == False:
            self.tilt_actions()

    def replay_step_up(self):
        if self.game.replays < 8999:
            self.game.replays += 1
            graphics.replay_step_up(self.game.replays, graphics.shoot_a_line_63.reel1, graphics.shoot_a_line_63.reel10, graphics.shoot_a_line_63.reel100, graphics.shoot_a_line_63.reel1000)
        self.game.coils.registerUp.pulse()
        graphics.shoot_a_line_63.display(self)

    def replay_step_down(self, number=0):
        if number > 0:
            if number > 1:
                self.game.replays -= 1
                self.game.coils.registerDown.pulse()
                number -= 1
                graphics.shoot_a_line_63.display(self)
                self.delay(name="replay_reset", delay=0.0, handler=self.replay_step_down, param=number)
            elif number == 1:
                self.game.replays -= 1
                self.game.coils.registerDown.pulse()
                number -= 1
                graphics.shoot_a_line_63.display(self)
                self.cancel_delayed(name="replay_reset")
        else: 
            if self.game.replays > 0:
                self.game.replays -= 1
                self.delay(name="display", delay=0.1, handler=graphics.shoot_a_line_63.display, param=self)
            self.game.coils.registerDown.pulse()

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
#        self.cancel_delayed(name="blink_title")
        self.game.sound.stop_music()
        self.game.sound.play_music('search', -1)

        if self.game.search_index.status == False and self.game.replays < 200:
            for i in range(0, 100):
                if i <= 50:
                    self.r = self.closed_search_relays(self.game.searchdisc.position)
                    self.game.searchdisc.spin()
                if i >= 51:
                    self.r = self.closed_search_relays(self.game.searchdisc2.position + 50)
                    self.game.searchdisc2.spin()
                self.wipers = self.r[0]
                self.card = self.r[1]
                self.super_line = self.r[2]

                # From here, I need to determine based on the value of r, whether to latch the search index and score. For Coney Island,
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
                                if s >= 3:
                                    self.find_winner(s, self.card, self.super_line)
                                    break
#        self.delay(name="blink_title", delay=3, handler=self.blink_title)

    def find_winner(self, relays, card, super_line):
        if self.game.search_index.status == False and self.game.replays < 200:
            if card == 1:
                if relays == 3:
                    if self.super_line == 1:
                        if self.game.card1_replay_counter.position < 12:
                            self.game.search_index.engage(self.game)
                            self.card1_replay_step_up(12 - self.game.card1_replay_counter.position)
                    else:
                        if self.game.card1_replay_counter.position < 4:
                            self.game.search_index.engage(self.game)
                            self.card1_replay_step_up(4 - self.game.card1_replay_counter.position)
                if relays == 4:
                    if self.super_line == 1:
                        if self.game.card1_replay_counter.position < 48:
                            self.game.search_index.engage(self.game)
                            self.card1_replay_step_up(48 - self.game.card1_replay_counter.position)
                    else:
                        if self.game.card1_replay_counter.position < 20:
                            self.game.search_index.engage(self.game)
                            self.card1_replay_step_up(20 - self.game.card1_replay_counter.position)
                if relays == 5:
                    if self.super_line == 1:
                        if self.game.card1_replay_counter.position < 192:
                            self.game.search_index.engage(self.game)
                            self.card1_replay_step_up(192 - self.game.card1_replay_counter.position)
                    else:
                        if self.game.card1_replay_counter.position < 48:
                            self.game.search_index.engage(self.game)
                            self.card1_replay_step_up(48 - self.game.card1_replay_counter.position)
            if card == 2:
                if relays == 3:
                    if self.super_line == 1:
                        if self.game.card2_replay_counter.position < 12:
                            self.game.search_index.engage(self.game)
                            self.card2_replay_step_up(12 - self.game.card2_replay_counter.position)
                    else:
                        if self.game.card2_replay_counter.position < 4:
                            self.game.search_index.engage(self.game)
                            self.card2_replay_step_up(4 - self.game.card2_replay_counter.position)
                if relays == 4:
                    if self.super_line == 1:
                        if self.game.card2_replay_counter.position < 72:
                            self.game.search_index.engage(self.game)
                            self.card2_replay_step_up(72 - self.game.card2_replay_counter.position)
                    else:
                        if self.game.card2_replay_counter.position < 32:
                            self.game.search_index.engage(self.game)
                            self.card2_replay_step_up(32 - self.game.card2_replay_counter.position)
                if relays == 5:
                    if self.super_line == 1:
                        if self.game.card2_replay_counter.position < 360:
                            self.game.search_index.engage(self.game)
                            self.card2_replay_step_up(360 - self.game.card2_replay_counter.position)
                    else:
                        if self.game.card2_replay_counter.position < 72:
                            self.game.search_index.engage(self.game)
                            self.card2_replay_step_up(72 - self.game.card2_replay_counter.position)
            if card == 3:
                if relays == 3:
                    if self.super_line == 1:
                        if self.game.card3_replay_counter.position < 12:
                            self.game.search_index.engage(self.game)
                            self.card3_replay_step_up(12 - self.game.card3_replay_counter.position)
                    else:
                        if self.game.card3_replay_counter.position < 4:
                            self.game.search_index.engage(self.game)
                            self.card3_replay_step_up(4 - self.game.card3_replay_counter.position)
                if relays == 4:
                    if self.super_line == 1:
                        if self.game.card3_replay_counter.position < 152:
                            self.game.search_index.engage(self.game)
                            self.card3_replay_step_up(152 - self.game.card3_replay_counter.position)
                    else:
                        if self.game.card3_replay_counter.position < 40:
                            self.game.search_index.engage(self.game)
                            self.card3_replay_step_up(40 - self.game.card3_replay_counter.position)
                if relays == 5:
                    if self.super_line == 1:
                        if self.game.card3_replay_counter.position < 472:
                            self.game.search_index.engage(self.game)
                            self.card3_replay_step_up(472 - self.game.card3_replay_counter.position)
                    else:
                        if self.game.card3_replay_counter.position < 152:
                            self.game.search_index.engage(self.game)
                            self.card3_replay_step_up(152 - self.game.card3_replay_counter.position)
            if card == 4:
                if relays == 3:
                    if self.super_line == 1:
                        if self.game.card4_replay_counter.position < 16:
                            self.game.search_index.engage(self.game)
                            self.card4_replay_step_up(16 - self.game.card4_replay_counter.position)
                    else:
                        if self.game.card4_replay_counter.position < 4:
                            self.game.search_index.engage(self.game)
                            self.card4_replay_step_up(4 - self.game.card4_replay_counter.position)
                if relays == 4:
                    if self.super_line == 1:
                        if self.game.card4_replay_counter.position < 238:
                            self.game.search_index.engage(self.game)
                            self.card4_replay_step_up(238 - self.game.card4_replay_counter.position)
                    else:
                        if self.game.card4_replay_counter.position < 62:
                            self.game.search_index.engage(self.game)
                            self.card4_replay_step_up(62 - self.game.card4_replay_counter.position)
                if relays == 5:
                    if self.super_line == 1:
                        if self.game.card4_replay_counter.position < 718:
                            self.game.search_index.engage(self.game)
                            self.card4_replay_step_up(718 - self.game.card4_replay_counter.position)
                    else:
                        if self.game.card4_replay_counter.position < 238:
                            self.game.search_index.engage(self.game)
                            self.card4_replay_step_up(238 - self.game.card4_replay_counter.position)
            if card == 5:
                if relays == 3:
                    if self.super_line == 1:
                        if self.game.card5_replay_counter.position < 22:
                            self.game.search_index.engage(self.game)
                            self.card5_replay_step_up(22 - self.game.card5_replay_counter.position)
                    else:
                        if self.game.card5_replay_counter.position < 6:
                            self.game.search_index.engage(self.game)
                            self.card5_replay_step_up(6 - self.game.card5_replay_counter.position)
                if relays == 4:
                    if self.super_line == 1:
                        if self.game.card5_replay_counter.position < 318:
                            self.game.search_index.engage(self.game)
                            self.card5_replay_step_up(318 - self.game.card5_replay_counter.position)
                    else:
                        if self.game.card5_replay_counter.position < 78:
                            self.game.search_index.engage(self.game)
                            self.card5_replay_step_up(78 - self.game.card5_replay_counter.position)
                if relays == 5:
                    if self.super_line == 1:
                        if self.game.card5_replay_counter.position < 958:
                            self.game.search_index.engage(self.game)
                            self.card5_replay_step_up(958 - self.game.card5_replay_counter.position)
                    else:
                        if self.game.card5_replay_counter.position < 318:
                            self.game.search_index.engage(self.game)
                            self.card5_replay_step_up(318 - self.game.card5_replay_counter.position)
            if card == 6:
                if relays == 3:
                    if self.super_line == 1:
                        if self.game.card6_replay_counter.position < 28:
                            self.game.search_index.engage(self.game)
                            self.card6_replay_step_up(28 - self.game.card6_replay_counter.position)
                    else:
                        if self.game.card6_replay_counter.position < 8:
                            self.game.search_index.engage(self.game)
                            self.card6_replay_step_up(8 - self.game.card6_replay_counter.position)
                if relays == 4:
                    if self.super_line == 1:
                        if self.game.card6_replay_counter.position < 510:
                            self.game.search_index.engage(self.game)
                            self.card6_replay_step_up(510 - self.game.card6_replay_counter.position)
                    else:
                        if self.game.card6_replay_counter.position < 94:
                            self.game.search_index.engage(self.game)
                            self.card6_replay_step_up(94 - self.game.card6_replay_counter.position)
                if relays == 5:
                    if self.super_line == 1:
                        if self.game.card6_replay_counter.position < 1198:
                            self.game.search_index.engage(self.game)
                            self.card6_replay_step_up(1198 - self.game.card6_replay_counter.position)
                    else:
                        if self.game.card6_replay_counter.position < 510:
                            self.game.search_index.engage(self.game)
                            self.card6_replay_step_up(510 - self.game.card6_replay_counter.position)

    def card1_replay_step_up(self, number):
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

    def card4_replay_step_up(self, number):
        if number >= 1:
            self.game.card4_replay_counter.step()
            number -= 1
            self.replay_step_up()
            if self.game.replays == 8999:
                number = 0
            self.delay(name="card4_replay_step_up", delay=0.1, handler=self.card4_replay_step_up, param=number)
        else:
            self.game.search_index.disengage()
            self.cancel_delayed(name="card4_replay_step_up")
            self.search()

    def card5_replay_step_up(self, number):
        if number >= 1:
            self.game.card5_replay_counter.step()
            number -= 1
            self.replay_step_up()
            if self.game.replays == 8999:
                number = 0
            self.delay(name="card5_replay_step_up", delay=0.1, handler=self.card5_replay_step_up, param=number)
        else:
            self.game.search_index.disengage()
            self.cancel_delayed(name="card5_replay_step_up")
            self.search()

    def card6_replay_step_up(self, number):
        if number >= 1:
            self.game.card6_replay_counter.step()
            number -= 1
            self.replay_step_up()
            self.delay(name="card6_replay_step_up", delay=0.1, handler=self.card6_replay_step_up, param=number)
        else:
            self.game.search_index.disengage()
            self.cancel_delayed(name="card6_replay_step_up")
            self.search()

    def closed_search_relays(self, rivets):
        # This function is critical, as it will determine which card is returned, etc.  I need to check both the position of the
        # replay counter for the card, as well as the selector unit to ensure that the card is selected. We will get a row back
        # that has the numbers on the position which will return the search relay connected.  When three out of the five relays
        # are connected, we get a winner!
        
        self.pos = {}
        # Card 1
        self.pos[0] = {}
        self.pos[1] = {10:1, 19:2, 1:3, 16:4, 12:5}
        self.pos[2] = {14:1, 7:2, 23:3, 4:4, 20:5}
        self.pos[3] = {2:1, 22:2, 9:3, 25:4, 3:5}
        self.pos[4] = {21:1, 8:2, 24:3, 5:4, 15:5}
        self.pos[5] = {13:1, 17:2, 6:3, 18:4, 11:5}
        self.pos[6] = {10:1, 14:2, 2:3, 21:4, 13:5}
        self.pos[7] = {19:1, 7:2, 22:3, 8:4, 17:5}
        self.pos[8] = {1:1, 23:2, 9:3, 24:4, 6:5}
        self.pos[9] = {16:1, 4:2, 25:3, 5:4, 18:5}
        self.pos[10] = {12:1, 20:2, 3:3, 15:4, 11:5}
        self.pos[11] = {10:1, 7:2, 9:3, 5:4, 11:5}
        self.pos[12] = {12:1, 4:2, 9:3, 8:4, 13:5}
        self.pos[13] = {}
        self.pos[14] = {}
        self.pos[15] = {}
        self.pos[16] = {}
        self.pos[17] = {}

        # There are five blank positions in between cards.  Early games have less to search!
        # Card 2
        self.pos[18] = {14:1, 15:2, 2:3, 25:4, 11:5}
        self.pos[19] = {3:1, 24:2, 16:3, 1:4, 20:5}
        self.pos[20] = {6:1, 21:2, 13:3, 4:4, 9:5}
        self.pos[21] = {22:1, 8:2, 23:3, 19:4, 18:5}
        self.pos[22] = {10:1, 5:2, 12:3, 17:4, 7:5}
        self.pos[23] = {14:1, 3:2, 6:3, 22:4, 10:5}
        self.pos[24] = {15:1, 24:2, 21:3, 8:4, 5:5}
        self.pos[25] = {2:1, 16:2, 13:3, 23:4, 12:5}
        self.pos[26] = {25:1, 1:2, 4:3, 19:4, 17:5}
        self.pos[27] = {11:1, 20:2, 9:3, 18:4, 7:5}
        self.pos[28] = {14:1, 24:2, 13:3, 19:4, 7:5}
        self.pos[29] = {11:1, 1:2, 13:3, 8:4, 10:5}
        self.pos[30] = {}
        self.pos[31] = {}
        self.pos[32] = {}
        self.pos[33] = {}
        self.pos[34] = {}

        # Another five blank positions.  Can you believe it?
        # Card 3
        self.pos[35] = {5:1, 20:2, 9:3, 18:4, 4:5}
        self.pos[36] = {21:1, 1:2, 12:3, 7:4, 25:5}
        self.pos[37] = {11:1, 16:2, 23:3, 3:4, 13:5}
        self.pos[38] = {24:1, 8:2, 19:3, 14:4, 22:5}
        self.pos[39] = {6:1, 17:2, 2:3, 15:4, 10:5}
        self.pos[40] = {5:1, 21:2, 11:3, 24:4, 6:5}
        self.pos[41] = {20:1, 1:2, 16:3, 8:4, 17:5}
        self.pos[42] = {9:1, 12:2, 23:3, 19:4, 2:5}
        self.pos[43] = {18:1, 7:2, 3:3, 14:4, 15:5}
        self.pos[44] = {4:1, 25:2, 13:3, 22:4, 10:5}
        self.pos[45] = {5:1, 1:2, 23:3, 14:4, 10:5}
        self.pos[46] = {4:1, 7:2, 23:3, 8:4, 6:5}
        self.pos[47] = {}
        self.pos[48] = {}
        self.pos[49] = {}
        self.pos[50] = {}

        # Start of the second search disc modeled as part
        # of the same array for simplicity. Parent function
        # calls this subset.
        # Card #4
        self.pos[51] = {18:1, 7:2, 20:3, 9:4, 1:5}
        self.pos[52] = {5:1, 23:2, 13:3, 27:4, 15:5}
        self.pos[53] = {24:1, 3:2, 17:3, 6:4, 22:5}
        self.pos[54] = {10:1, 25:2, 14:3, 19:4, 16:5}
        self.pos[55] = {2:1, 12:2, 21:3, 11:4, 8:5}
        self.pos[56] = {18:1, 5:2, 24:3, 10:4, 2:5}
        self.pos[57] = {7:1, 23:2, 3:3, 25:4, 12:5}
        self.pos[58] = {20:1, 13:2, 17:3, 14:4, 21:5}
        self.pos[59] = {9:1, 27:2, 6:3, 19:4, 11:5}
        self.pos[60] = {1:1, 15:2, 22:3, 16:4, 8:5}
        self.pos[61] = {18:1, 23:2, 17:3, 19:4, 8:5}
        self.pos[62] = {1:1, 27:2, 17:3, 25:4, 2:5}
        self.pos[63] = {}
        self.pos[64] = {}
        self.pos[65] = {}
        self.pos[66] = {}
        self.pos[67] = {}

        # Card #5
        self.pos[68] = {15:1, 7:2, 23:3, 1:4, 10:5}
        self.pos[69] = {9:1, 22:2, 11:3, 16:4, 12:5}
        self.pos[70] = {25:1, 8:2, 26:3, 5:4, 21:5}
        self.pos[71] = {13:1, 24:2, 14:3, 20:4, 17:5}
        self.pos[72] = {4:1, 18:2, 19:3, 6:4, 3:5}
        self.pos[73] = {15:1, 9:2, 25:3, 13:4, 4:5}
        self.pos[74] = {7:1, 22:2, 8:3, 24:4, 18:5}
        self.pos[75] = {23:1, 11:2, 26:3, 14:4, 19:5}
        self.pos[76] = {1:1, 16:2, 5:3, 20:4, 6:5}
        self.pos[77] = {10:1, 12:2, 21:3, 17:4, 3:5}
        self.pos[78] = {15:1, 22:2, 26:3, 20:4, 3:5}
        self.pos[79] = {10:1, 16:2, 26:3, 24:4, 4:5}
        self.pos[80] = {}
        self.pos[81] = {}
        self.pos[82] = {}
        self.pos[83] = {}
        self.pos[84] = {}

        # Card #6
        self.pos[85] = {9:1, 8:2, 25:3, 15:4, 14:5}
        self.pos[86] = {10:1, 21:2, 7:3, 20:4, 11:5}
        self.pos[87] = {27:1, 1:2, 24:3, 4:4, 28:5}
        self.pos[88] = {16:1, 22:2, 18:3, 23:4, 19:5}
        self.pos[89] = {12:1, 6:2, 17:3, 2:4, 13:5}
        self.pos[90] = {9:1, 10:2, 27:3, 16:4, 12:5}
        self.pos[91] = {8:1, 21:2, 1:3, 22:4, 6:5}
        self.pos[92] = {25:1, 7:2, 24:3, 18:4, 17:5}
        self.pos[93] = {15:1, 20:2, 4:3, 23:4, 2:5}
        self.pos[94] = {14:1, 11:2, 28:3, 19:4, 13:5}
        self.pos[95] = {9:1, 21:2, 24:3, 23:4, 13:5}
        self.pos[96] = {14:1, 20:2, 24:3, 22:4, 12:5}
        self.pos[97] = {}
        self.pos[98] = {}
        self.pos[99] = {}
        self.pos[100] = {}

        super_line = 0

        if rivets in range(0,18):
            card = 1
        if rivets in range(18,35):
            card = 2
        if rivets in range(35,50):
            card = 3
        if rivets in range(50,68):
            card = 4
        if rivets in range(68,85):
            card = 5
        if rivets in range(85,100):
            card = 6


        if rivets == 4:
            super_line = 1
        elif rivets == 21:
            super_line = 1
        elif rivets == 38:
            super_line = 1
        elif rivets == 54:
            super_line = 1
        elif rivets == 71:
            super_line = 1
        elif rivets == 88:
            super_line = 1

        return (self.pos[rivets], card, super_line)

    def blink_title(self):
        title1 = random.randint(0,1)
        title2 = random.randint(0,1)
        if title1 == 1:
            pos = [307,237]
            image = pygame.image.load('shoot_a_line_63/assets/title1_on.png').convert_alpha()
            screen.blit(image, pos)
        if title2 == 1:
            pos = [423,237]
            image = pygame.image.load('shoot_a_line_63/assets/title2_on.png').convert_alpha()
            screen.blit(image, pos)

        pygame.display.update()
        self.delay(name="display", delay=0.1, handler=graphics.shoot_a_line_63.display, param=self)
#        self.delay(name="blink_title", delay=3, handler=self.blink_title)


    # Define reset as the knock-off, anti-cheat relay disabled, and replay reset enabled.  Motors turn while credits are knocked off.
    # When meter reaches zero and the zero limit switch is hit, turn off motor sound and leave backglass gi on, but with tilt displayed.

    def startup(self):        
        self.tilt_actions()
#        self.delay(name="blink_title", delay=1, handler=self.blink_title)


class ShootALine(procgame.game.BasicGame):
    """ Fun Spot was the first Ohio Dime Game to automatically play off replays """
    def __init__(self, machine_type):
        super(ShootALine, self).__init__(machine_type)
        pygame.mixer.pre_init(44100,-16,2,512)
        self.sound = procgame.sound.SoundController(self)
        self.sound.set_volume(1.0)
        # NOTE: trough_count only counts the number of switches present in the  trough.  It does _not_ count
        #       the number of balls present.   In this game, there  should  be  8  balls.
        self.trough_count = 6

        # Subclass my units unique to this game -  modifications must be made to set up mixers and steppers unique to the game
        # NOTE: 'top' positions are indexed using a 0 index, so the top on a 24 position unit is actually 23.

        self.searchdisc = units.Search("searchdisc", 49)
        self.searchdisc2 = units.Search("searchdisc2", 49)

        #Seach relays
        self.s1 = units.Relay("s1")
        self.s2 = units.Relay("s2")
        self.s3 = units.Relay("s3")
        self.s4 = units.Relay("s4")
        self.s5 = units.Relay("s5")
        self.search_index = units.Relay("search_index")

        #Replay Counter
        self.card1_replay_counter = units.Stepper("card1_replay_counter", 100)
        self.card2_replay_counter = units.Stepper("card2_replay_counter", 100)
        self.card3_replay_counter = units.Stepper("card3_replay_counter", 100)
        self.card4_replay_counter = units.Stepper("card4_replay_counter", 100)
        self.card5_replay_counter = units.Stepper("card5_replay_counter", 100)
        self.card6_replay_counter = units.Stepper("card6_replay_counter", 100)

        #Initialize stepper units used to keep track of features or timing.
        self.selector = units.Stepper("selector", 6)
        self.timer = units.Stepper("timer", 40)
        self.ball_count = units.Stepper("ball_count", 7)

        #Check for status of the replay register zero switch.  If positive
        #and machine is just powered on, this will zero out the replays.
        self.replay_reset = units.Relay("replay_reset")
        
        # Now, the control unit can be in one of two positions, essentially.
        # This alternates by coin, and is used to portion the Spotted Numbers.
        self.cu = 1

        #When engage()d, light 6v circuit, and enable game features, scoring,
        #etc. Disengage()d means that the machine is 'soft' tilted. 
        self.anti_cheat = units.Relay("anti_cheat")

        #When engage()d, spin.
        self.start = units.Relay("start")

        #Tilt is separate from anti-cheat in that the trip will move the shutter
        #when the game is tilted with 1st ball in the lane.  Also prevents you
        #from picking back up by killing the anti-cheat.  Can be engaged by 
        #tilt bob, slam tilt switches, or timer at 39th step.
        #Immediately kills motors.
        self.tilt = units.Relay("tilt")

        self.replays = 0
        self.returned = False

    def reset(self):
        super(ShootALine, self).reset()
        self.logger = logging.getLogger('game')
        self.load_config('bingo.yaml')
        
        main_mode = MulticardBingo(self)
        self.modes.add(main_mode)

game = ShootALine(machine_type='pdb')
game.reset()
game.run_loop()
