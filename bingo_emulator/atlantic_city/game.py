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
from bingo_emulator.graphics.atlantic_city import *

from modes.timeout import Timeout

class MulticardBingo(procgame.game.Mode):
    def __init__(self, game):
        super(MulticardBingo, self).__init__(game=game, priority=5)
        self.holes = []
        self.startup()
        self.game.sound.register_music('motor', "audio/six_card_motor.wav")
        self.game.sound.register_music('search', "audio/six_card_search_old.wav")
        self.game.sound.register_sound('add', "audio/six_card_add_card.wav")
        self.game.sound.register_sound('tilt', "audio/tilt.wav")
        self.game.sound.register_sound('step', "audio/step.wav")
        self.game.sound.register_sound('eb_search', "audio/EB_Search.wav")

    def sw_coin_active(self, sw):
        self.game.cu = not self.game.cu
        self.game.spotting.spin()
        self.game.mixer1.spin()
        self.game.mixer2.spin()
        self.game.mixer3.spin()

        if self.game.eb_play.status == True and self.game.tilt.status == False:
            self.game.sound.stop('add')
            self.game.sound.play('add')
            self.scan_eb()
            self.replay_step_down()
            self.game.reflex.decrease()
            self.game.eb_play.disengage()
        else:
            self.game.tilt.disengage()
            self.regular_play()
            self.scan_all()
        self.delay(name="display", delay=0.1, handler=graphics.atlantic_city.display, param=self)

    def sw_startButton_active(self, sw):
        if self.game.replays > 0 or self.game.switches.freeplay.is_active():
            self.game.cu = not self.game.cu
            self.game.spotting.spin()
            self.game.mixer1.spin()
            self.game.mixer2.spin()
            self.game.mixer3.spin()

            self.game.tilt.disengage()
            self.game.extra_ball.reset()
            self.regular_play()
            self.scan_all()
            self.delay(name="display", delay=0.1, handler=graphics.atlantic_city.display, param=self)

    def sw_trough4_active_for_1s(self, sw):
        if self.game.ball_count.position >= 4:
            self.game.modes.add(Timeout(self.game, 7))

    def sw_trough8_inactive_for_1ms(self, sw):
        if self.game.start.status == False:
            self.game.ball_count.position -= 1
            self.game.returned = True
            self.check_lifter_status()

    def sw_enter_active(self, sw):
        if self.game.switches.left.is_active() and self.game.switches.right.is_active():
            self.game.end_run_loop()
            os.system("/home/nbaldridge/proc/bingo_emulator/start_game.sh atlantic_city")
            

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
        self.cancel_delayed(name="search")
        self.cancel_delayed(name="lifter_status")
        self.cancel_delayed(name="card1_replay_step_up")
        self.cancel_delayed(name="card2_replay_step_up")
        self.cancel_delayed(name="card3_replay_step_up")
        self.cancel_delayed(name="corners_replay_step_up")
        self.game.search_index.disengage()
        self.game.coils.counter.pulse()
        self.game.returned = False
        self.game.sound.stop('add')
        self.game.sound.play('add')
        if self.game.start.status == True:
            if self.game.selector.position < 3:
                self.game.selector.step()
            if self.game.switches.shutter.is_inactive():
                self.game.coils.shutter.enable()
            self.replay_step_down()
            self.game.reflex.decrease()
            self.check_lifter_status()
        else:
            self.holes = []
            self.game.start.engage(self.game)
            self.game.corners_replay_counter.reset()
            self.game.c1_double.disengage()
            self.game.c2_double.disengage()
            self.game.c3_double.disengage()
            self.game.card1_replay_counter.reset()
            self.game.card2_replay_counter.reset()
            self.game.card3_replay_counter.reset()
            self.game.start.engage(self.game)
            self.game.selector.reset()
            self.game.corners.disengage()
            self.game.ball_count.reset()
            self.game.timer.reset()
            self.game.sound.play_music('motor', -1)
            self.regular_play()
        self.delay(name="display", delay=0.1, handler=graphics.atlantic_city.display, param=self)
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
                else:
                    if self.game.switches.trough4.is_inactive():
                        if self.game.extra_ball.position >= 4 and self.game.ball_count.position == 5:
                            if self.game.switches.shooter.is_inactive() and self.game.switches.trough3.is_active():
                                self.game.coils.lifter.enable()
                    if self.game.switches.trough3.is_inactive():
                        if self.game.extra_ball.position >= 8 and self.game.ball_count.position == 6:
                            if self.game.switches.shooter.is_inactive() and self.game.switches.trough2.is_active():
                                self.game.coils.lifter.enable()
                    if self.game.switches.trough2.is_inactive() and self.game.ball_count.position <= 7:
                        if self.game.extra_ball.position >= 12 and self.game.ball_count.position == 7:
                            if self.game.switches.shooter.is_inactive():
                                self.game.coils.lifter.enable()
                    if self.game.ball_count.position >= 8:
                        self.game.coils.lifter.disable()
                if self.game.returned == True and self.game.ball_count.position == 4:
                    if self.game.switches.shooter.is_inactive():
                        self.game.coils.lifter.enable()
                        self.game.returned = False
                if self.game.returned == True and self.game.ball_count.position == 8:
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

    def sw_shooter_active(self, sw):
        if self.game.ball_count.position == 7:
            self.game.coils.lifter.disable()
            self.cancel_delayed("lifter_status")

    def sw_ballLift_active_for_500ms(self, sw):
        if self.game.tilt.status == False:
            if self.game.switches.shooter.is_inactive():
                if self.game.ball_count.position < 5:
                    self.game.coils.lifter.enable()
                if self.game.ball_count.position == 5 and self.game.extra_ball.position >= 4:
                    self.game.coils.lifter.enable()
                if self.game.ball_count.position == 6 and self.game.extra_ball.position >= 8:
                    self.game.coils.lifter.enable()
                if self.game.ball_count.position == 7 and self.game.extra_ball.position >= 12:
                    self.game.coils.lifter.enable()

    def sw_gate_inactive_for_1ms(self, sw):
        self.game.start.disengage()
        self.game.ball_count.step()
        if self.game.switches.shutter.is_active():
            self.game.coils.shutter.enable()
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
            self.delay(name="display", delay=0.1, handler=graphics.atlantic_city.display, param=self)

    def sw_hole2_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(2)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.atlantic_city.display, param=self)

    def sw_hole3_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(3)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.atlantic_city.display, param=self)

    def sw_hole4_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(4)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.atlantic_city.display, param=self)

    def sw_hole5_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(5)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.atlantic_city.display, param=self)

    def sw_hole6_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(6)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.atlantic_city.display, param=self)

    def sw_hole7_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(7)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.atlantic_city.display, param=self)

    def sw_hole8_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(8)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.atlantic_city.display, param=self)

    def sw_hole9_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(9)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.atlantic_city.display, param=self)

    def sw_hole10_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(10)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.atlantic_city.display, param=self)

    def sw_hole11_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(11)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.atlantic_city.display, param=self)

    def sw_hole12_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(12)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.atlantic_city.display, param=self)

    def sw_hole13_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(13)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.atlantic_city.display, param=self)

    def sw_hole14_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(14)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.atlantic_city.display, param=self)

    def sw_hole15_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(15)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.atlantic_city.display, param=self)

    def sw_hole16_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(16)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.atlantic_city.display, param=self)

    def sw_hole17_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(17)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.atlantic_city.display, param=self)

    def sw_hole18_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(18)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.atlantic_city.display, param=self)

    def sw_hole19_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(19)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.atlantic_city.display, param=self)

    def sw_hole20_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(20)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.atlantic_city.display, param=self)

    def sw_hole21_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(21)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.atlantic_city.display, param=self)

    def sw_hole22_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(22)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.atlantic_city.display, param=self)

    def sw_hole23_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(23)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.atlantic_city.display, param=self)

    def sw_hole24_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(24)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.atlantic_city.display, param=self)

    def sw_hole25_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(25)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.atlantic_city.display, param=self)
    
    def sw_replayReset_active(self, sw):
        self.game.anti_cheat.disengage()
        self.holes = []
#        self.cancel_delayed(name="blink_title")
        self.delay(name="display", delay=0.1, handler=graphics.atlantic_city.display, param=self)
        self.tilt_actions()
#        self.delay(name="blink_title", delay=1, handler=self.blink_title)
        self.replay_step_down(self.game.replays)

    def tilt_actions(self):
        self.game.start.disengage()
        self.cancel_delayed(name="replay_reset")
        self.cancel_delayed(name="card1_replay_step_up")
        self.cancel_delayed(name="card2_replay_step_up")
        self.cancel_delayed(name="card3_replay_step_up")
        self.cancel_delayed(name="corners_replay_step_up")
        self.game.search_index.disengage()
        if self.game.ball_count.position == 0:
            if self.game.switches.shutter.is_active():
                self.game.coils.shutter.enable()
        self.holes = []
        self.game.selector.reset()
        self.game.extra_ball.reset()
        self.game.corners.disengage()
        self.game.c1_double.disengage()
        self.game.c2_double.disengage()
        self.game.c3_double.disengage()
        self.game.corners_replay_counter.reset()
        self.game.ball_count.reset()
        self.game.anti_cheat.engage(game)
        self.game.tilt.engage(self.game)
        self.game.sound.stop_music()
        self.game.sound.play('tilt')
        # displays "Tilt" on the backglass, you have to recoin.
        self.delay(name="display", delay=0.1, handler=graphics.atlantic_city.display, param=self)
        self.game.modes.remove(Timeout)

    def sw_tilt_active(self, sw):
        if self.game.tilt.status == False:
            self.tilt_actions()

    def replay_step_down(self, number=0):
        if number > 0:
            if number > 1:
                self.game.replays -= 1
                graphics.replay_step_down(self.game.replays, graphics.atlantic_city.reel1, graphics.atlantic_city.reel10, graphics.atlantic_city.reel100)
                self.game.coils.registerDown.pulse()
                number -= 1
                graphics.atlantic_city.display(self)
                self.delay(name="replay_reset", delay=0.0, handler=self.replay_step_down, param=number)
            elif number == 1:
                self.game.replays -= 1
                graphics.replay_step_down(self.game.replays, graphics.atlantic_city.reel1, graphics.atlantic_city.reel10, graphics.atlantic_city.reel100)
                self.game.coils.registerDown.pulse()
                number -= 1
                graphics.atlantic_city.display(self)
                self.cancel_delayed(name="replay_reset")
        else: 
            if self.game.replays > 0:
                self.game.replays -= 1
                graphics.replay_step_down(self.game.replays, graphics.atlantic_city.reel1, graphics.atlantic_city.reel10, graphics.atlantic_city.reel100)
                self.delay(name="display", delay=0.1, handler=graphics.atlantic_city.display, param=self)
            self.game.coils.registerDown.pulse()

    def replay_step_up(self):
        if self.game.replays < 899:
            self.game.replays += 1
            graphics.replay_step_up(self.game.replays, graphics.atlantic_city.reel1, graphics.atlantic_city.reel10, graphics.atlantic_city.reel100)
        self.game.coils.registerUp.pulse()
        self.game.coils.sounder.pulse()
        self.game.reflex.increase()
        graphics.atlantic_city.display(self)

    def sw_yellow_active(self, sw):
        if self.game.ball_count.position >= 4:
            if self.game.eb_play.status == False:
                self.game.eb_play.engage(self.game)
                self.delay(name="display", delay=0.1, handler=graphics.atlantic_city.display, param=self)
                self.sw_yellow_active(sw)
            if self.game.eb_play.status == True and (self.game.replays > 0 or self.game.switches.freeplay.is_active()):
                self.game.sound.stop('add')
                self.game.sound.play('add')
                self.game.cu = not self.game.cu
                self.game.spotting.spin()
                self.game.mixer1.spin()
                self.game.mixer2.spin()
                self.game.mixer3.spin()
                self.scan_eb()
                self.replay_step_down()
                self.game.reflex.decrease()
                self.game.eb_play.disengage()
                self.delay(name="display", delay=0.1, handler=graphics.atlantic_city.display, param=self)
  
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

        for i in range(0, 50):
            self.r = self.closed_search_relays(self.game.searchdisc.position, self.game.corners.status)
            self.game.searchdisc.spin()
            self.wipers = self.r[0]
            self.card = self.r[1]
            self.corners = self.r[2]

            # From here, I need to determine based on the value of r, whether to latch the search index and score. 
            # I need to determine the best winner on each card.  To do this, I must compare the position of the replay counter before
            # determining the winner. Reminder that my replay counters are a 1:1 representation.

            self.match = []
            for key in self.wipers:
                for number in self.holes:
                    if number == key:
                        self.match.append(self.wipers[key])
                        relays = sorted(set(self.match))
                        #TODO Play sound for each relay closure.
                        for i in relays:
                            pass
                        s = functions.count_seq(relays)
                        if self.game.selector.position >= self.card:
                            if s >= 3:
                                self.find_winner(s, self.game.selector.position, self.card, self.corners)
                                break
#        self.delay(name="blink_title", delay=3, handler=self.blink_title)

    def find_winner(self, relays, selector, card, corners):
        if self.game.search_index.status == False and self.game.replays < 899:
            if selector >= 1:
                if card == 1:
                    if relays == 3:
                        if corners:
                            pass
                        elif self.game.c1_double.status == True:
                            if self.game.card1_replay_counter.position < 8:
                                self.game.search_index.engage(self.game)
                                self.card1_replay_step_up(8 - self.game.card1_replay_counter.position)
                        elif self.game.card1_replay_counter.position < 4:
                            self.game.search_index.engage(self.game)
                            self.card1_replay_step_up(4 - self.game.card1_replay_counter.position)
                    if relays == 4:
                        if corners and self.game.corners.status == True:
                            if self.game.corners_replay_counter.position < 200:
                                self.game.search_index.engage(self.game)
                                self.corners_replay_step_up(200 - self.game.corners_replay_counter.position)
                        else:
                            if self.game.c1_double.status == True:
                                if self.game.card1_replay_counter.position < 40:
                                    self.game.search_index.engage(self.game)
                                    self.card1_replay_step_up(40 - self.game.card1_replay_counter.position)
                            elif self.game.card1_replay_counter.position < 20:
                                self.game.search_index.engage(self.game)
                                self.card1_replay_step_up(20 - self.game.card1_replay_counter.position)
                    if relays == 5:
                        if self.game.c1_double.status == True:
                            if self.game.card1_replay_counter.position < 200:
                                self.game.search_index.engage(self.game)
                                self.card1_replay_step_up(200 - self.game.card1_replay_counter.position)
                        elif self.game.card1_replay_counter.position < 100:
                            self.game.search_index.engage(self.game)
                            self.card1_replay_step_up(100 - self.game.card1_replay_counter.position)
            if selector >= 2:
                if card == 2:
                    if relays == 3:
                        if corners:
                            pass
                        if self.game.c2_double.status == True:
                            if self.game.card2_replay_counter.position < 8:
                                self.game.search_index.engage(self.game)
                                self.card2_replay_step_up(8 - self.game.card2_replay_counter.position)
                        elif self.game.card2_replay_counter.position < 4:
                            self.game.search_index.engage(self.game)
                            self.card2_replay_step_up(4 - self.game.card2_replay_counter.position)
                    if relays == 4:
                        if corners and self.game.corners.status == True:
                            if self.game.corners_replay_counter.position < 200:
                                self.game.search_index.engage(self.game)
                                self.corners_replay_step_up(200 - self.game.corners_replay_counter.position)
                        else:
                            if self.game.c1_double.status == True:
                                if self.game.card2_replay_counter.position < 40:
                                    self.game.search_index.engage(self.game)
                                    self.card2_replay_step_up(40 - self.game.card2_replay_counter.position)
                            elif self.game.card2_replay_counter.position < 20:
                                self.game.search_index.engage(self.game)
                                self.card2_replay_step_up(20 - self.game.card2_replay_counter.position)
                    if relays == 5:
                        if self.game.c1_double.status == True:
                            if self.game.card2_replay_counter.position < 200:
                                self.game.search_index.engage(self.game)
                                self.card2_replay_step_up(200 - self.game.card2_replay_counter.position)
                        elif self.game.card2_replay_counter.position < 100:
                            self.game.search_index.engage(self.game)
                            self.card2_replay_step_up(100 - self.game.card2_replay_counter.position)
            if selector >= 3:
                if card == 3:
                    if relays == 3:
                        if corners:
                            pass
                        if self.game.c3_double.status == True:
                            if self.game.card3_replay_counter.position < 8:
                                self.game.search_index.engage(self.game)
                                self.card3_replay_step_up(8 - self.game.card3_replay_counter.position)
                        elif self.game.card3_replay_counter.position < 4:
                            self.game.search_index.engage(self.game)
                            self.card3_replay_step_up(4 - self.game.card3_replay_counter.position)
                    if relays == 4:
                        if corners and self.game.corners.status == True:
                            if self.game.corners_replay_counter.position < 200:
                                self.game.search_index.engage(self.game)
                                self.corners_replay_step_up(200 - self.game.corners_replay_counter.position)
                        else:
                            if self.game.c1_double.status == True:
                                if self.game.card3_replay_counter.position < 40:
                                    self.game.search_index.engage(self.game)
                                    self.card3_replay_step_up(40 - self.game.card3_replay_counter.position)
                            elif self.game.card3_replay_counter.position < 20:
                                self.game.search_index.engage(self.game)
                                self.card3_replay_step_up(20 - self.game.card3_replay_counter.position)
                    if relays == 5:
                        if self.game.c1_double.status == True:
                            if self.game.card3_replay_counter.position < 200:
                                self.game.search_index.engage(self.game)
                                self.card3_replay_step_up(200 - self.game.card3_replay_counter.position)
                        elif self.game.card3_replay_counter.position < 100:
                            self.game.search_index.engage(self.game)
                            self.card3_replay_step_up(100 - self.game.card3_replay_counter.position)

    def card1_replay_step_up(self, number):
        if number >= 1:
            self.game.card1_replay_counter.step()
            number -= 1
            self.replay_step_up()
            if self.game.replays == 899:
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
            if self.game.replays == 899:
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
            if self.game.replays == 899:
                number = 0
            self.delay(name="card3_replay_step_up", delay=0.1, handler=self.card3_replay_step_up, param=number)
        else:
            self.game.search_index.disengage()
            self.cancel_delayed(name="card3_replay_step_up")
            self.search()

    def corners_replay_step_up(self, number):
        if number >= 1:
            self.game.corners_replay_counter.step()
            number -= 1
            self.replay_step_up()
            if self.game.replays == 899:
                number = 0
            self.delay(name="corners_replay_step_up", delay=0.1, handler=self.corners_replay_step_up, param=number)
        else:
            self.game.search_index.disengage()
            self.cancel_delayed(name="corners_replay_step_up")
            self.search()

    def closed_search_relays(self, rivets, c):
        # This function is critical, as it will determine which card is returned, etc.  I need to check the position of the
        # replay counter for the card. We will get a row back
        # that has the numbers on the position which will return the search relay connected.  When three out of the five relays
        # are connected, we get a winner!
        
        self.pos = {}
        # Card 1
        # Search disc also not documented.
        self.pos[0] = {}
        self.pos[1] = {5:1, 1:2, 9:3, 25:4, 3:5}
        self.pos[2] = {8:1, 22:2, 10:3, 19:4, 17:5}
        self.pos[3] = {6:1, 18:2, 16:3, 11:4, 7:5}
        self.pos[4] = {24:1, 21:2, 14:3, 20:4, 13:5}
        self.pos[5] = {12:1, 23:2, 2:3, 15:4, 4:5}
        self.pos[6] = {5:1, 8:2, 6:3, 24:4, 12:5}
        self.pos[7] = {1:1, 22:2, 18:3, 21:4, 23:5}
        self.pos[8] = {9:1, 10:2, 16:3, 14:4, 2:5}
        self.pos[9] = {25:1, 19:2, 11:3, 20:4, 15:5}
        self.pos[10] = {3:1, 17:2, 7:3, 13:4, 4:5}
        self.pos[11] = {5:1, 22:2, 16:3, 20:4, 4:5}
        self.pos[12] = {3:1, 19:2, 16:3, 21:4, 12:5}
        self.pos[13] = {5:1, 3:2, 12:3, 4:4}
        self.pos[14] = {}
        self.pos[15] = {9:1, 24:2, 4:3, 16:4, 6:5}
        self.pos[16] = {13:1, 19:2, 14:3, 20:4, 25:5}
        self.pos[17] = {2:1, 18:2, 15:3, 12:4, 8:5}
        self.pos[18] = {1:1, 22:2, 11:3, 21:4, 17:5}
        self.pos[19] = {10:1, 7:2, 5:3, 23:4, 3:5}
        self.pos[20] = {9:1, 13:2, 2:3, 1:4, 10:5}
        self.pos[21] = {24:1, 19:2, 18:3, 22:4, 7:5}
        self.pos[22] = {4:1, 14:2, 15:3, 11:4, 5:5}
        self.pos[23] = {16:1, 20:2, 12:3, 21:4, 23:5}
        self.pos[24] = {6:1, 25:2, 8:3, 17:4, 3:5}
        self.pos[25] = {9:1, 19:2, 15:3, 21:4, 3:5}
        self.pos[26] = {6:1, 20:2, 15:3, 22:4, 10:5}
        self.pos[27] = {9:1, 6:2, 10:3, 3:4}
        self.pos[28] = {}
        self.pos[29] = {21:1, 7:2, 10:3, 4:4, 9:5}
        self.pos[30] = {15:1, 3:2, 18:3, 22:4, 8:5}
        self.pos[31] = {24:1, 14:2, 17:3, 11:4, 2:5}
        self.pos[32] = {13:1, 6:2, 12:3, 19:4, 23:5}
        self.pos[33] = {20:1, 25:2, 1:3, 16:4, 5:5}
        self.pos[34] = {21:1, 15:2, 24:3, 13:4, 20:5}
        self.pos[35] = {7:1, 3:2, 14:3, 6:4, 25:5}
        self.pos[36] = {10:1, 18:2, 17:3, 12:4, 1:5}
        self.pos[37] = {4:1, 22:2, 11:3, 19:4, 16:5}
        self.pos[38] = {9:1, 8:2, 2:3, 23:4, 5:5}
        self.pos[39] = {21:1, 3:2, 17:3, 19:4, 5:5}
        self.pos[40] = {9:1, 22:2, 17:3, 6:4, 20:5}
        self.pos[41] = {21:1, 9:2, 20:3, 5:4}
        self.pos[42] = {}
        self.pos[43] = {}
        self.pos[44] = {}
        self.pos[45] = {}
        self.pos[46] = {}
        self.pos[47] = {}
        self.pos[48] = {}
        self.pos[49] = {}
        self.pos[50] = {}

        corners = False
        card = 0

        if c:
            if rivets == 13 or rivets == 27 or rivets == 41:
                corners = True
        if rivets in range(0,14):
            card = 1
        elif rivets in range(15,28):
            card = 2
        elif rivets in range(29, 42):
            card = 3

        return (self.pos[rivets], card, corners)
    
    def blink_title(self):
        title1 = random.randint(0,1)
        title2 = random.randint(0,1)
        title3 = random.randint(0,1)
        title4 = random.randint(0,1)
        if title1 == 1:
            pos = [139,201]
            image = pygame.image.load('atlantic_city/assets/title1_on.png').convert_alpha()
            screen.blit(image, pos)
        if title2 == 1:
            pos = [303,211]
            image = pygame.image.load('atlantic_city/assets/title2_on.png').convert_alpha()
            screen.blit(image, pos)
        if title3 == 1:
            pos = [397,210]
            image = pygame.image.load('atlantic_city/assets/title3_on.png').convert_alpha()
            screen.blit(image, pos)
        if title4 == 1:
            pos = [514,238]
            image = pygame.image.load('atlantic_city/assets/title4_on.png').convert_alpha()
            screen.blit(image, pos)

        pygame.display.update()
        self.delay(name="display", delay=0.1, handler=graphics.atlantic_city.display, param=self)
#        self.delay(name="blink_title", delay=3, handler=self.blink_title)

    def scan_all(self):
        #Animate scanning of everything - this happens through the spotting disc
        self.all_probability()

    def all_probability(self):
       
        mix1 = self.game.mixer1.connected_rivet()
        if self.game.reflex.connected_rivet() == 1:
            self.scan_features()
            self.scan_double()
        elif self.game.reflex.connected_rivet() == 2 and (mix1 != 23 and mix1 != 19 and mix1 != 15 and mix1 != 12 and mix1 != 9 and mix1 != 5):
            self.scan_features()
            self.scan_double()
        elif self.game.reflex.connected_rivet() == 3 and (mix1 != 1 and mix1 != 5 and mix1 != 6 and mix1 != 7 and mix1 != 9 and mix1 != 12 and mix1 != 13 and mix1 != 15 and mix1 != 18 and mix1 != 19 and mix1 != 23):
            self.scan_features()
            self.scan_double()
        elif self.game.reflex.connected_rivet() == 4 and (mix1 == 2 or mix1 == 3 or mix1 == 4 or mix1 == 8 or mix1 == 10 or mix1 == 11 or mix1 == 14 or mix1 == 16 or mix1 == 17 or mix1 == 22):
            self.scan_features()
            self.scan_double()
        elif self.game.reflex.connected_rivet() == 5 and (mix1 == 2 or mix1 == 4 or mix1 == 8 or mix1 == 10 or mix1 == 11 or mix1 == 14 or mix1 == 16 or mix1 == 22):
            self.scan_features()
            self.scan_double()
        else:
            s = random.randint(1,4)
            self.animate_feature_scan(s)
            return []

    def scan_double(self):
        d = self.double_probability()

    def double_probability(self):
        sd = self.game.spotting.connected_rivet()
        mix3 = self.game.mixer3.connected_rivet()
        if self.game.card1_replay_counter.position == 0 or self.game.card2_replay_counter.position == 0 or self.game.card3_replay_counter.position == 0:
            #Check position of mixer3
            t = self.check_mixer_3()
            if t == 1:
                m = self.check_mixer_2()
                if m == 1:
                    if sd == 5 or sd == 8 or sd == 28 or sd == 37 or sd == 21 or sd == 17:
                        self.game.c1_double.engage(self.game)
                    elif sd == 20 or sd == 32 or sd == 34 or sd == 46 or sd == 27 or sd == 44:
                        self.game.c2_double.engage(self.game)
                    elif sd == 50 or sd == 11 or sd == 14 or sd == 36 or sd == 39 or sd == 48:
                        self.game.c3_double.engage(self.game)


    def check_mixer_3(self):
        mix3 = self.game.mixer3.connected_rivet()
        if (mix3 == 2 or mix3 == 5 or mix3 == 6 or mix3 == 8 or mix3 == 11 or mix3 == 12 or mix3 == 14 or mix3 == 16 or mix3 == 17 or mix3 == 20 or mix3 == 22 or mix3 == 24):
            return 1
        elif (self.game.c1_double.status and (mix3 == 1 or mix3 == 13 or mix3 == 18 or mix3 == 19)):
            return 1
        elif (self.game.c2_double.status and (mix3 == 9 or mix3 == 10 or mix3 == 13 or mix3 == 21)):
            return 1
        elif (self.game.c3_double.status and (mix3 == 3 or mix3 == 4 or mix3 == 7 or mix3 == 23)):
            return 1
        else:
            return 0

    def scan_features(self):
        p = self.features_probability()

    def features_probability(self):
        s = random.randint(1,4)
        self.animate_feature_scan(s)
        mix3 = self.game.mixer3.connected_rivet()
        if mix3 == 2 or mix3 == 3 or mix3 == 6 or mix3 == 8 or mix3 == 10 or mix3 == 11 or mix3 == 12 or mix3 == 14 or mix3 == 16 or mix3 == 17 or mix3 == 18 or mix3 == 20 or mix3 == 22 or mix3 == 24:
            self.check_trips()

    def check_trips(self):
        if self.game.selector.position == 3:
            if self.game.spotting.position == 2 or self.game.spotting.position == 9 or self.game.spotting.position == 18 or self.game.spotting.position == 38 or self.game.spotting.position == 13 or self.game.spotting.position == 22:
                if self.game.selector.position == 3:
                    if 14 not in self.holes:
                        self.holes.append(14)
                        self.game.fourteen.engage(self.game)
            elif self.game.spotting.position == 1 or self.game.spotting.position == 24 or self.game.spotting.position == 42 or self.game.spotting.position == 47 or self.game.spotting.position == 4 or self.game.spotting.position == 31:
                if self.game.selector.position == 3:
                    if 19 not in self.holes:
                        self.holes.append(19)
                        self.game.nineteen.engage(self.game)
            elif self.game.spotting.position == 6 or self.game.spotting.position == 13 or self.game.spotting.position == 30 or self.game.spotting.position == 40 or self.game.spotting.position == 12 or self.game.spotting.position == 25:
                if self.game.selector.position == 3:
                    if 22 not in self.holes:
                        self.holes.append(22)
                        self.game.twentytwo.engage(self.game)
        if self.game.spotting.position == 10 or self.game.spotting.position == 3 or self.game.spotting.position == 29 or self.game.spotting.position == 19 or self.game.spotting.position == 26 or self.game.spotting.position == 45:
            self.game.corners.engage(self.game)
        elif self.game.spotting.position == 33:
            if 15 not in self.holes:
                self.holes.append(15)
                self.game.fifteen.engage(self.game)
        elif self.game.spotting.position == 49:
            if 16 not in self.holes:
                self.holes.append(16)
                self.game.sixteen.engage(self.game)
        elif self.game.spotting.position == 7:
            if 17 not in self.holes:
                self.holes.append(17)
                self.game.seventeen.engage(self.game)
                

    def scan_eb(self):
        if self.game.eb_play.status == True:
            s = random.randint(1,12)
            self.animate_eb_scan(s)
            p = self.eb_probability()
            if p == 1:
                if self.game.extra_ball.position < 24:
                    self.game.extra_ball.step()
                    self.check_lifter_status()
                    # Timer resets to 0 position on ball count increasing.  We are fudging this since we will have
                    # no good way to measure balls as they return back to the trough.  The ball count unit cannot be
                    # relied upon as we do not have a switch in the outhole, and the trough logic is too complex for
                    # the task at hand.
                    # TODO: implement thunk noises into the units.py to automatically play the noises.
                    self.game.timer.reset()
            else:
                # TODO: play thunk noise of EB search bearing no fruit.
                pass
        self.delay(name="display", delay=0.1, handler=graphics.atlantic_city.display, param=self)

    def animate_feature_scan(self, s):
        if s > 1:
            self.delay(name="feature_animation", delay=0.1, handler=graphics.atlantic_city.feature_animation, param=s)
            self.delay(name="display", delay=0.1, handler=graphics.atlantic_city.display, param=self)
            s -= 1
            #self.delay(name="animate_feature", delay=0.1, handler=self.animate_feature_scan, param=s)
        else:
            self.delay(name="display", delay=0.1, handler=graphics.atlantic_city.display, param=self)


    def animate_eb_scan(self, s):
        if s > 1:
            self.delay(name="eb_animation", delay=0.1, handler=graphics.atlantic_city.eb_animation, param=s)
            self.delay(name="display", delay=0.1, handler=graphics.atlantic_city.display, param=self)
            s -= 1
            #self.delay(name="animate_eb", delay=0.1, handler=self.animate_eb_scan, param=s)
        else:
            self.delay(name="display", delay=0.1, handler=graphics.atlantic_city.display, param=self)

    def eb_probability(self):
        sd = self.game.spotting.connected_rivet()
        mix2 = self.game.mixer2.connected_rivet()
        mix3 = self.game.mixer3.connected_rivet()
        eb = self.game.extra_ball.position
        if self.game.card1_replay_counter.position == 0 or self.game.card2_replay_counter.position == 0 or self.game.card3_replay_counter.position == 0:
        #Check position of mixer3
            if mix3 == 2 or mix3 == 5 or mix3 == 6 or mix3 == 8 or mix3 == 11 or mix3 == 12 or mix3 == 14 or mix3 == 16 or mix3 == 17 or mix3 == 20 or mix3 == 22 or mix3 == 24:
                m = self.check_mixer_2()
                if not m:
                    s = self.check_spotted_numbers()
                    if s: 
                        e = self.check_eb()
                        if e:
                            self.game.extra_ball.step()
                            self.check_lifter_status()
                    else:
                        e = self.check_eb()
                        if e:
                            self.game.extra_ball.step()
                            self.check_lifter_status()
                else:
                    e = self.check_eb()
                    if e:
                        self.game.extra_ball.step()
                        self.check_lifter_status()
                    else:
                        if mix2 == 24:
                            if self.game.extra_ball.position < 11:
                                self.game.extra_ball.step()
                                self.check_lifter_status()
            else:
                m = self.check_mixer_2()
                if not m:
                    s = self.check_spotted_numbers()
                    if s: 
                        e = self.check_eb()
                        if e:
                            self.game.extra_ball.step()
                            self.check_lifter_status()
                    else:
                        e = self.check_eb()
                        if e:
                            self.game.extra_ball.step()
                            self.check_lifter_status()

    def check_mixer_2(self):
        mix2 = self.game.mixer2.connected_rivet()
        if ((mix2 == 5 or mix2 == 7 or mix2 == 9 or mix2 == 10 or mix2 == 11 or mix2 == 12 or mix2 == 17 or mix2 == 18 or mix2 == 20 or mix2 == 21 or mix2 == 22 or mix2 == 24)):
            if self.game.extra_ball.position == 11:
                if mix2 == 24:
                    return 0
            return 1
        else:
            return 0

    def check_spotted_numbers(self):
        mix2 = self.game.mixer2.connected_rivet()
        if (self.game.fourteen.status and self.game.fifteen.status and (mix2 == 1 or mix2 == 2 or mix2 == 6 or mix2 == 15)):
            return 1
        elif (self.game.nineteen.status and self.game.sixteen.status and (mix2 == 3 or mix2 == 8 or mix2 == 14 or mix2 == 16)):
            return 1
        elif (self.game.twentytwo.status and self.game.seventeen.status and (mix2 == 4 or mix2 == 13 or mix2 == 19 or mix2 == 23)):
            return 1
        else:
            return 0
                    
    def check_eb(self):
        # Doggone schematic for Atlantic City shows the rivets for 
        # each disc for each circuit, except for the spotting disc
        # in this circuit.  The interesting thing about these older
        # games, is that the spotting disc is attached beside the search
        # disc.   I am horribly fudging this.  Based on the schematic, there
        # are three separate positions that will allow stepup to EB 1,2
        # or 3.  I am going to just do a modulus 1 on the spotting unit.  
        # Should be sufficiently random.
        if self.game.spotting.position % 3 == 0:
            return 1
        else:
            return 0

    # Define reset as the knock-off, anti-cheat relay disabled, and replay reset enabled.  Motors turn while credits are knocked off.
    # When meter reaches zero and the zero limit switch is hit, turn off motor sound and leave backglass gi on, but with tilt displayed.

    def startup(self):        
        # Every bingo requires the meter to register '0' 
        # before allowing coin entry --
        # also needs to show a plain 'off' backglass.
        self.eb = False
        self.tilt_actions()
 #       self.delay(name="blink_title", delay=1, handler=self.blink_title)


class AtlanticCity(procgame.game.BasicGame):
    """ Atlantic City was the follow-on to Spot-Lite and is drastically simpler.
        It has more spotted numbers, but no pic-a-play."""
    def __init__(self, machine_type):
        super(AtlanticCity, self).__init__(machine_type)
        pygame.mixer.pre_init(44100,-16,2,512)
        self.sound = procgame.sound.SoundController(self)
        self.sound.set_volume(1.0)
        # NOTE: trough_count only counts the number of switches present in the  trough.  It does _not_ count
        #       the number of balls present.   In this game, there  should  be  8  balls.
        self.trough_count = 6

        # Now, the control unit can be in one of two positions, essentially.
        # This alternates by coin, and is used to portion the Spotted Numbers.
        self.cu = 1

        # Subclass my units unique to this game -  modifications must be made to set up mixers and steppers unique to the game
        # NOTE: 'top' positions are indexed using a 0 index, so the top on a 24 position unit is actually 23.

        self.mixer1 = units.Mixer("mixer1", 23)
        self.mixer2 = units.Mixer("mixer2", 23)
        self.mixer3 = units.Mixer("mixer3", 23)
        self.mixer4 = units.Mixer("mixer4", 23)
        self.mixer5 = units.Mixer("mixer5", 23)

        self.searchdisc = units.Search("searchdisc", 49)

        #Search relays
        self.s1 = units.Relay("s1")
        self.s2 = units.Relay("s2")
        self.s3 = units.Relay("s3")
        self.s4 = units.Relay("s4")
        self.s5 = units.Relay("s5")
        self.search_index = units.Relay("search_index")

        #Replay Counter
        self.card1_replay_counter = units.Stepper("card1_replay_counter", 200)
        self.card2_replay_counter = units.Stepper("card2_replay_counter", 200)
        self.card3_replay_counter = units.Stepper("card3_replay_counter", 200)
 
        #Corners Replay Counter
        self.corners_replay_counter = units.Stepper("corners_replay_counter", 200)

        #Initialize stepper units used to keep track of features or timing.
        self.timer = units.Stepper("timer", 40)
        self.ball_count = units.Stepper("ball_count", 8)

        # Initialize reflex(es) and mixers unique to this game
        # NOTE: reflex unit drawing was not available for this game, so until I convince
        #       another Spot-Lite owner to take their game apart, I'll note that there
        #       are five lugs, four of which provide another path to the mixer, and one which is always connected
        #       and bypasses the mixer entirely.  There are no games from 1951 or 52 that have the reflex documented.
        self.reflex = units.Reflex("primary", 200)

        #Atlantic City has a combined EB/spotting disc, which I am calling
        #the spotting disc for convenience.
        self.spotting = units.Spotting("spotting", 50)

        #Extra ball unit contains 12 positions in Atlantic City.  Max of 3 EBs.
        self.extra_ball = units.Stepper("extra_ball", 12)

        #When engage()d, light 6v circuit, and enable game features, scoring,
        #etc. Disengage()d means that the machine is 'soft' tilted. 
        self.anti_cheat = units.Relay("anti_cheat")

        #Card score doubling trip relays
        self.c1_double = units.Relay("c1_double")
        self.c2_double = units.Relay("c2_double")
        self.c3_double = units.Relay("c3_double")

        #Selector keeps track of cards in play
        self.selector = units.Stepper("selector", 3)

        #When engage()d, spin.
        self.start = units.Relay("start")

        #Tilt is separate from anti-cheat in that the trip will move the shutter
        #when the game is tilted with 1st ball in the lane.  Also prevents you
        #from picking back up by killing the anti-cheat.  Can be engaged by 
        #tilt bob, slam tilt switches, or timer at 39th step.
        #Immediately kills motors.
        self.tilt = units.Relay("tilt")

        #Need to define relays for playing ebs
        self.eb_play = units.Relay("eb_play")

        #Relay for corners lighting
        self.corners = units.Relay("corners")

        #Relays for spotted numbers
        self.sixteen = units.Relay("sixteen")
        self.fifteen = units.Relay("fifteen")
        self.fourteen = units.Relay("fourteen")
        self.nineteen = units.Relay("nineteen")
        self.seventeen = units.Relay("seventeen")
        self.twentytwo = units.Relay("twentytwo")

        self.replays = 0
        self.returned = False

    def reset(self):
        super(AtlanticCity, self).reset()
        self.logger = logging.getLogger('game')
        self.load_config('bingo.yaml')
        self.anti_cheat.engage(game)
        
        main_mode = MulticardBingo(self)
        self.modes.add(main_mode)
        
game = AtlanticCity(machine_type='pdb')
game.reset()
game.run_loop()
