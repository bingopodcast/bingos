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
from bingo_emulator.graphics.spelling_bee import *

class MulticardBingo(procgame.game.Mode):
    def __init__(self, game):
        super(MulticardBingo, self).__init__(game=game, priority=5)
        self.holes = []
        self.startup()
        self.game.sound.register_music('motor', "audio/woodrail_motor.wav")
        self.game.sound.register_music('search1', "audio/automatic_search_one_ball.wav")
        self.game.sound.register_music('search2', "audio/automatic_search_two_ball.wav")
        self.game.sound.register_music('search3', "audio/automatic_search_three_ball.wav")
        self.game.sound.register_music('search4', "audio/automatic_search_four_ball.wav")
        self.game.sound.register_music('search5', "audio/automatic_search_five_ball.wav")
        self.game.sound.register_music('search6', "audio/automatic_search_six_ball.wav")
        self.game.sound.register_music('search7', "audio/automatic_search_seven_ball.wav")
        self.game.sound.register_music('search8', "audio/automatic_search_eight_ball.wav")
        self.game.sound.register_sound('add', "audio/woodrail_coin.wav")
        self.game.sound.register_sound('tilt', "audio/tilt.wav")
        self.game.sound.register_sound('step', "audio/step.wav")

    def sw_coin_active(self, sw):
        self.game.tilt.disengage()
        self.regular_play()
        self.delay(name="display", delay=0.1, handler=graphics.spelling_bee.display, param=self)

    def sw_startButton_active(self, sw):
        if self.game.replays > 0 or self.game.switches.freeplay.is_active():
            self.game.tilt.disengage()
            self.regular_play()

    def sw_trough4_active_for_1s(self, sw):
        if self.game.ball_count.position >= 4:
            self.timeout_actions()
    
    def timeout_actions(self):
        if (self.game.timer.position < 39):
            self.game.timer.step()
            self.delay(name="timeout", delay=5.0, handler=self.timeout_actions)
        else:
            self.game.timer.step()
            self.tilt_actions()

    def sw_trough8_closed(self, sw):
        if self.game.start.status == False:
            self.game.ball_count.position -= 1
            self.game.returned = True
            self.check_lifter_status()
        else:
            self.check_lifter_status()

    def sw_enter_active(self, sw):
        if self.game.switches.left.is_active() and self.game.switches.right.is_active():
            self.game.end_run_loop()
            os.system("/home/nbaldridge/proc/bingo_emulator/start_game.sh spelling_bee")


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
        self.cancel_delayed(name="card4_replay_step_up")
        self.cancel_delayed(name="timeout")
        self.game.search_index.disengage()
        self.game.coils.counter.pulse()
        self.game.returned = False
        self.game.sound.stop('add')
        self.game.sound.play('add')
        if self.game.start.status == True:
            if self.game.selector.position <= 3:
                self.game.selector.step()
            if self.game.switches.shutter.is_inactive():
                self.game.coils.shutter.enable()
            self.replay_step_down()
            self.check_lifter_status()
        else:
            self.game.start.engage(self.game)
            self.game.card1_replay_counter.reset()
            self.game.card2_replay_counter.reset()
            self.game.card3_replay_counter.reset()
            self.game.card4_replay_counter.reset()
            self.game.average.disengage()
            self.game.good.disengage()
            self.game.expert.disengage()
            self.game.average.engage(self.game)
            self.game.selector.reset()
            self.game.ball_count.reset()
            self.game.timer.reset()
            self.game.sound.play_music('motor', -1)
            self.regular_play()
        self.delay(name="display", delay=0.1, handler=graphics.spelling_bee.display, param=self)
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
        if self.game.ball_count.position >= 4:
            if self.game.search_index.status == False:
                self.search()
        if self.game.ball_count.position <= 4:
            self.check_lifter_status()

    # This is really nasty, but it is how we render graphics for each individual hole.
    # numbers are added (or removed from) a list.  In this way, I can re-use the same
    # routine even for games where there are ball return functions like Surf Club.

    def sw_hole1_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(1)
            if self.game.good.status == True:
                self.game.average.disengage()
                self.game.good.disengage()
                self.game.expert.engage(self.game)
            else:
                self.game.average.disengage()
                self.game.good.engage(self.game)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.spelling_bee.display, param=self)

    def sw_hole2_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(2)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.spelling_bee.display, param=self)

    def sw_hole3_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(3)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.spelling_bee.display, param=self)

    def sw_hole4_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(4)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.spelling_bee.display, param=self)

    def sw_hole5_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(5)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.spelling_bee.display, param=self)

    def sw_hole6_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(6)
            if self.game.good.status == True:
                self.game.average.disengage()
                self.game.good.disengage()
                self.game.expert.engage(self.game)
            else:
                self.game.average.disengage()
                self.game.good.engage(self.game)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.spelling_bee.display, param=self)

    def sw_hole7_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(7)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.spelling_bee.display, param=self)

    def sw_hole8_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(8)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.spelling_bee.display, param=self)

    def sw_hole9_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(9)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.spelling_bee.display, param=self)

    def sw_hole10_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(10)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.spelling_bee.display, param=self)

    def sw_hole11_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(11)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.spelling_bee.display, param=self)

    def sw_hole12_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(12)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.spelling_bee.display, param=self)

    def sw_hole13_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(13)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.spelling_bee.display, param=self)

    def sw_hole14_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(14)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.spelling_bee.display, param=self)

    def sw_hole15_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(15)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.spelling_bee.display, param=self)

    def sw_hole16_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(16)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.spelling_bee.display, param=self)

    def sw_hole17_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(17)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.spelling_bee.display, param=self)

    def sw_hole18_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(18)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.spelling_bee.display, param=self)

    def sw_replayReset_active(self, sw):
        self.game.anti_cheat.disengage()
        self.holes = []
        graphics.spelling_bee.display(self)
        self.tilt_actions()
        self.replay_step_down(self.game.replays)

    def tilt_actions(self):
        self.game.start.disengage()
        self.cancel_delayed(name="replay_reset")
        self.cancel_delayed(name="card1_replay_step_up")
        self.cancel_delayed(name="card2_replay_step_up")
        self.cancel_delayed(name="card3_replay_step_up")
        self.cancel_delayed(name="card4_replay_step_up")
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
        self.game.average.disengage()
        self.game.good.disengage()
        self.game.expert.disengage()
        self.game.sound.stop_music()
        self.game.sound.play('tilt')
        # displays "Tilt" on the backglass, you have to recoin.
        self.delay(name="display", delay=0.1, handler=graphics.spelling_bee.display, param=self)

    def search_sounds(self):
        self.game.sound.stop_music()
        if self.game.ball_count.position == 1:
            self.game.sound.play_music('search1', -1)
        if self.game.ball_count.position == 2:
            self.game.sound.play_music('search2', -1)
        if self.game.ball_count.position == 3:
            self.game.sound.play_music('search3', -1)
        if self.game.ball_count.position == 4:
            self.game.sound.play_music('search4', -1)
        if self.game.ball_count.position == 5:
            self.game.sound.play_music('search5', -1)
        if self.game.ball_count.position == 6:
            self.game.sound.play_music('search6', -1)
        if self.game.ball_count.position == 7:
            self.game.sound.play_music('search7', -1)
        if self.game.ball_count.position == 8:
            self.game.sound.play_music('search8', -1)

    def sw_tilt_active(self, sw):
        if self.game.tilt.status == False:
            self.tilt_actions()

    def replay_step_down(self, number=0):
        if number > 0:
            if number > 1:
                self.game.replays -= 1
                graphics.replay_step_down(self.game.replays, graphics.spelling_bee.reel1, graphics.spelling_bee.reel10, graphics.spelling_bee.reel100)
                self.game.coils.registerDown.pulse()
                number -= 1
                graphics.spelling_bee.display(self)
                self.delay(name="replay_reset", delay=0.13, handler=self.replay_step_down, param=number)
            elif number == 1:
                self.game.replays -= 1
                graphics.replay_step_down(self.game.replays, graphics.spelling_bee.reel1, graphics.spelling_bee.reel10, graphics.spelling_bee.reel100)
                self.game.coils.registerDown.pulse()
                number -= 1
                graphics.spelling_bee.display(self)
                self.cancel_delayed(name="replay_reset")
        else: 
            if self.game.replays > 0:
                self.game.replays -= 1
                graphics.replay_step_down(self.game.replays, graphics.spelling_bee.reel1, graphics.spelling_bee.reel10, graphics.spelling_bee.reel100)
                self.delay(name="display", delay=0.1, handler=graphics.spelling_bee.display, param=self)
            self.game.coils.registerDown.pulse()

    def replay_step_up(self):
        if self.game.replays < 99:
            self.game.replays += 1
            graphics.replay_step_up(self.game.replays, graphics.spelling_bee.reel1, graphics.spelling_bee.reel10, graphics.spelling_bee.reel100)
        self.game.coils.registerUp.pulse()
        graphics.spelling_bee.display(self)
 
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

        for i in range(0, 100):
            if i <= 50:
                self.r = self.closed_search_relays(self.game.searchdisc.position)
                self.game.searchdisc.spin()
            if i >= 51:
                self.r = self.closed_search_relays(self.game.searchdisc2.position + 50)
                self.game.searchdisc2.spin()
            self.wipers = self.r[0]
            self.card = self.r[1]
            self.four = self.r[2]

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
                            if s >= 3:
                                self.find_winner(s, self.card, self.four)
                                break
        

    def find_winner(self, relays, card, four):
        if self.game.search_index.status == False and self.game.replays < 99:
            if card == 1:
                if relays == 3 and not four:
                    amount = 2
                    if self.game.good.status == True:
                        amount = 3
                    if self.game.expert.status == True:
                        amount = 16
                    if self.game.card1_replay_counter.position < amount:
                        self.game.search_index.engage(self.game)
                        self.card1_replay_step_up(amount - self.game.card1_replay_counter.position)
                if relays == 4:
                    amount = 8
                    if self.game.good.status == True:
                        amount = 12
                    if self.game.card1_replay_counter.position < amount:
                        self.game.search_index.engage(self.game)
                        self.card1_replay_step_up(amount - self.game.card1_replay_counter.position)
            if card == 2:
                if relays == 3 and not four:
                    amount = 2
                    if self.game.good.status == True:
                        amount = 3
                    if self.game.expert.status == True:
                        amount = 16
                    if self.game.card2_replay_counter.position < amount:
                        self.game.search_index.engage(self.game)
                        self.card2_replay_step_up(amount - self.game.card2_replay_counter.position)
                if relays == 4:
                    amount = 8
                    if self.game.good.status == True:
                        amount = 12
                    if self.game.card2_replay_counter.position < amount:
                        self.game.search_index.engage(self.game)
                        self.card2_replay_step_up(amount - self.game.card2_replay_counter.position)
            if card == 3:
                if relays == 3 and not four:
                    amount = 2
                    if self.game.good.status == True:
                        amount = 3
                    if self.game.expert.status == True:
                        amount = 16
                    if self.game.card3_replay_counter.position < amount:
                        self.game.search_index.engage(self.game)
                        self.card3_replay_step_up(amount - self.game.card3_replay_counter.position)
                if relays == 4:
                    amount = 8
                    if self.game.good.status == True:
                        amount = 12
                    if self.game.card3_replay_counter.position < amount:
                        self.game.search_index.engage(self.game)
                        self.card3_replay_step_up(amount - self.game.card3_replay_counter.position)
            if card == 4:
                if relays == 3 and not four:
                    amount = 2
                    if self.game.good.status == True:
                        amount = 3
                    if self.game.expert.status == True:
                        amount = 16
                    if self.game.card4_replay_counter.position < amount:
                        self.game.search_index.engage(self.game)
                        self.card4_replay_step_up(amount - self.game.card4_replay_counter.position)
                if relays == 4:
                    amount = 8
                    if self.game.good.status == True:
                        amount = 12
                    if self.game.card4_replay_counter.position < amount:
                        self.game.search_index.engage(self.game)
                        self.card4_replay_step_up(amount - self.game.card4_replay_counter.position)

    def card1_replay_step_up(self, number):
        self.game.sound.stop_music()
        if number >= 1:
            self.game.card1_replay_counter.step()
            number -= 1
            self.replay_step_up()
            if self.game.replays == 99:
                number = 0
            self.delay(name="card1_replay_step_up", delay=0.1, handler=self.card1_replay_step_up, param=number)
        else:
            self.game.search_index.disengage()
            self.cancel_delayed(name="card1_replay_step_up")
            self.search_sounds()
            self.search()

    def card2_replay_step_up(self, number):
        self.game.sound.stop_music()
        if number >= 1:
            self.game.card2_replay_counter.step()
            number -= 1
            self.replay_step_up()
            if self.game.replays == 99:
                number = 0
            self.delay(name="card2_replay_step_up", delay=0.1, handler=self.card2_replay_step_up, param=number)
        else:
            self.game.search_index.disengage()
            self.cancel_delayed(name="card2_replay_step_up")
            self.search_sounds()
            self.search()

    def card3_replay_step_up(self, number):
        self.game.sound.stop_music()
        if number >= 1:
            self.game.card3_replay_counter.step()
            number -= 1
            self.replay_step_up()
            if self.game.replays == 99:
                number = 0
            self.delay(name="card3_replay_step_up", delay=0.1, handler=self.card3_replay_step_up, param=number)
        else:
            self.game.search_index.disengage()
            self.cancel_delayed(name="card3_replay_step_up")
            self.search_sounds()
            self.search()

    def card4_replay_step_up(self, number):
        self.game.sound.stop_music()
        if number >= 1:
            self.game.card4_replay_counter.step()
            number -= 1
            self.replay_step_up()
            if self.game.replays == 99:
                number = 0
            self.delay(name="card4_replay_step_up", delay=0.1, handler=self.card4_replay_step_up, param=number)
        else:
            self.game.search_index.disengage()
            self.cancel_delayed(name="card4_replay_step_up")
            self.search_sounds()
            self.search()

    def closed_search_relays(self, rivets):
        # This function is critical, as it will determine which card is returned, etc.  I need to check both the position of the
        # replay counter for the card, as well as the selector unit to ensure that the card is selected. We will get a row back
        # that has the numbers on the position which will return the search relay connected.  When three out of the five relays
        # are connected, we get a winner!
        
        self.pos = {}
        # Card 1
        self.pos[0] = {}
        self.pos[1] = {2:1, 3:2, 7:3}
        self.pos[2] = {18:1, 2:2, 15:3}
        self.pos[3] = {2:1, 10:2, 5:3}
        self.pos[4] = {17:1, 2:2, 3:3}
        self.pos[5] = {8:1, 2:2, 15:3, 11:4}
        self.pos[6] = {9:1, 2:2, 16:3, 14:4}
        self.pos[7] = {3:1, 13:2, 2:3, 15:4}
        self.pos[8] = {17:1, 2:2, 14:3, 7:4}
        self.pos[9] = {8:1, 2:2, 17:3, 7:4}
        self.pos[10] = {16:1, 13:2, 18:3, 12:4}
        self.pos[11] = {4:1, 13:2, 14:3, 7:4}
        self.pos[12] = {3:1, 2:2, 17:3, 7:4}
        self.pos[13] = {}
        self.pos[14] = {}
        self.pos[15] = {}
        self.pos[16] = {}
        self.pos[17] = {}

        # There are five blank positions in between cards.  Early games have less to search!
        # Card 2
        self.pos[18] = {3:1, 10:2, 12:3}
        self.pos[19] = {13:1, 15:2, 7:3}
        self.pos[20] = {16:1, 2:2, 18:3}
        self.pos[21] = {8:1, 10:2, 15:3}
        self.pos[22] = {17:1, 9:2, 7:3, 12:4}
        self.pos[23] = {15:1, 13:2, 5:3, 7:4}
        self.pos[24] = {16:1, 10:2, 15:3, 7:4}
        self.pos[25] = {11:1, 2:2, 5:3, 7:4}
        self.pos[26] = {4:1, 2:2, 15:3, 17:4}
        self.pos[27] = {9:1, 10:2, 5:3, 7:4}
        self.pos[28] = {15:1, 10:2, 5:3, 7:4}
        self.pos[29] = {14:1, 2:2, 12:3, 17:4}
        self.pos[30] = {}
        self.pos[31] = {}
        self.pos[32] = {}
        self.pos[33] = {}
        self.pos[34] = {}

        # Another five blank positions.  Can you believe it?
        # Card 3
        self.pos[35] = {9:1, 10:2, 5:3}
        self.pos[36] = {14:1, 2:2, 12:3}
        self.pos[37] = {4:1, 2:2, 3:3}
        self.pos[38] = {3:1, 2:2, 5:3}
        self.pos[39] = {17:1, 13:2, 18:3, 12:4}
        self.pos[40] = {16:1, 14:2, 2:3, 15:4}
        self.pos[41] = {9:1, 2:2, 17:3, 7:4}
        self.pos[42] = {3:1, 13:2, 2:3, 17:4}
        self.pos[43] = {17:1, 9:2, 7:3, 11:4}
        self.pos[44] = {18:1, 2:2, 16:3, 9:4}
        self.pos[45] = {8:1, 2:2, 15:3, 7:4}
        self.pos[46] = {11:1, 2:2, 17:3, 7:4}
        self.pos[47] = {}
        self.pos[48] = {}
        self.pos[49] = {}
        self.pos[50] = {}

        # Start of the second search disc modeled as part
        # of the same array for simplicity. Parent function
        # calls this subset.
        # Card #4
        self.pos[51] = {9:1, 10:2, 11:3}
        self.pos[52] = {7:1, 2:2, 15:3}
        self.pos[53] = {16:1, 10:2, 15:3}
        self.pos[54] = {8:1, 13:2, 15:3}
        self.pos[55] = {3:1, 2:2, 15:3, 7:4}
        self.pos[56] = {5:1, 13:2, 12:3, 7:4}
        self.pos[57] = {3:1, 2:2, 5:3, 7:4}
        self.pos[58] = {17:1, 7:2, 12:3, 5:4}
        self.pos[59] = {15:1, 2:2, 12:3, 17:4}
        self.pos[60] = {4:1, 13:2, 5:3, 7:4}
        self.pos[61] = {14:1, 2:2, 15:3, 17:4}
        self.pos[62] = {17:1, 18:2, 10:3, 12:4}
        self.pos[63] = {}
        self.pos[64] = {}
        self.pos[65] = {}
        self.pos[66] = {}
        self.pos[67] = {}

        # Card #5
        self.pos[68] = {}
        self.pos[69] = {}
        self.pos[70] = {}
        self.pos[71] = {}
        self.pos[72] = {}
        self.pos[73] = {}
        self.pos[74] = {}
        self.pos[75] = {}
        self.pos[76] = {}
        self.pos[77] = {}
        self.pos[78] = {}
        self.pos[79] = {}
        self.pos[80] = {}
        self.pos[81] = {}
        self.pos[82] = {}
        self.pos[83] = {}
        self.pos[84] = {}

        # Card #6
        self.pos[85] = {}
        self.pos[86] = {}
        self.pos[87] = {}
        self.pos[88] = {}
        self.pos[89] = {}
        self.pos[90] = {}
        self.pos[91] = {}
        self.pos[92] = {}
        self.pos[93] = {}
        self.pos[94] = {}
        self.pos[95] = {}
        self.pos[96] = {}
        self.pos[97] = {}
        self.pos[98] = {}
        self.pos[99] = {}
        self.pos[100] = {}

        four = 0

        if rivets in range(0,18):
            card = 1
        if rivets in range(5,13):
            four = 0
        if rivets in range(18,35):
            card = 2
        if rivets in range(22,30):
            four = 0
        if rivets in range(35,50):
            card = 3
        if rivets in range(39,47):
            four = 0
        if rivets in range(50,100):
            card = 4
        if rivets in range(55,62):
            four = 0

        return (self.pos[rivets], card, four)
            
    # Define reset as the knock-off, anti-cheat relay disabled, and replay reset enabled.  Motors turn while credits are knocked off.
    # When meter reaches zero and the zero limit switch is hit, turn off motor sound and leave backglass gi on, but with tilt displayed.

    def startup(self):        
        # Every bingo requires the meter to register '0' 
        # before allowing coin entry --
        # also needs to show a plain 'off' backglass.
        self.eb = False
        self.tilt_actions()

class SpellingBee(procgame.game.BasicGame):
    """ Spelling Bee was a re-run of Crosswords """
    def __init__(self, machine_type):
        super(SpellingBee, self).__init__(machine_type)
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

        #Hole in One uses a specialized scoring system, tracking your shots.
        self.average = units.Relay("average")
        self.good = units.Relay("good")
        self.expert = units.Relay("expert")

        #Initialize stepper units used to keep track of features or timing.
        self.selector = units.Stepper("selector", 4)
        self.timer = units.Stepper("timer", 40)
        self.ball_count = units.Stepper("ball_count", 5)

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
        super(SpellingBee, self).reset()
        self.logger = logging.getLogger('game')
        self.load_config('bingo.yaml')
        
        main_mode = MulticardBingo(self)
        self.modes.add(main_mode)
        
game = SpellingBee(machine_type='pdb')
game.reset()
game.run_loop()
