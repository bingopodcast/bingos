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
from bingo_emulator.graphics.stars import *

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
        if self.game.eb.status == True and self.game.tilt.status == False:
            self.game.sound.stop('add')
            self.game.sound.play('add')
            self.scan_eb()
            self.game.eb.disengage()
        else:
            self.game.tilt.disengage()
            self.regular_play()
            self.scan_all()
        self.delay(name="display", delay=0.1, handler=graphics.stars.display, param=self)

    def sw_startButton_active(self, sw):
        if self.game.replays > 0 or self.game.switches.freeplay.is_active():
            self.game.tilt.disengage()
            self.regular_play()
            self.scan_all()
            self.delay(name="display", delay=0.1, handler=graphics.stars.display, param=self)

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
            os.system("/home/nbaldridge/proc/bingo_emulator/start_game.sh stars")

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
            self.game.cu = not self.game.cu
            self.game.reflex1.step()
            self.game.reflex2.step()
            
            current = self.game.flash.connected_rivet()
            self.game.flash.spin()
            new = self.game.flash.connected_rivet()
            f = [1,3,12,14,17,21,24]
            g = [2,6,10,11,20,23]
            h = [5,9,13,15,19,22]
            i = [0,4,7,8,16,18]
            if new > current:
                difference = new - current
                for j in range(current,difference):
                    if j in f:
                        self.game.mixer1.step()
                    if j in g:
                        self.game.mixer2.step()
                    if j in h:
                        self.game.mixer3.step()
                    if j in i:
                        self.game.mixer4.step()
            else:
                difference = current - new
                for j in range(0,difference):
                    if j in f:
                        self.game.mixer1.step()
                    if j in g:
                        self.game.mixer2.step()
                    if j in h:
                        self.game.mixer3.step()
                    if j in i:
                        self.game.mixer4.step()

            self.replay_step_down()
            self.check_lifter_status()
        else:
            self.holes = []
            self.game.start.engage(self.game)
            self.game.corners_replay_counter.reset()
            self.game.card1_replay_counter.reset()
            self.game.card2_replay_counter.reset()
            self.game.card3_replay_counter.reset()
            self.game.c1_double.disengage()
            self.game.c2_double.disengage()
            self.game.c3_double.disengage()
            self.game.all_double.disengage()
            self.game.sixteen.disengage()
            self.game.fifteen.disengage()
            self.game.fourteen.disengage()
            self.game.nineteen.disengage()
            self.game.seventeen.disengage()
            self.game.twentytwo.disengage()
            self.game.start.engage(self.game)
            self.game.selector.reset()
            self.game.ball_count.reset()
            self.game.extra_ball.reset()
            self.game.timer.reset()
            self.game.sound.play_music('motor', -1)
            self.regular_play()
        self.delay(name="display", delay=0.1, handler=graphics.stars.display, param=self)
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
                        if self.game.extra_ball.position >= 4 and self.game.ball_count.position <= 5:
                            if self.game.switches.shooter.is_inactive() and self.game.switches.trough3.is_active():
                                self.game.coils.lifter.enable()
                    if self.game.switches.trough3.is_inactive():
                        if self.game.extra_ball.position >= 8 and self.game.ball_count.position <= 6:
                            if self.game.switches.shooter.is_inactive() and self.game.switches.trough2.is_active():
                                self.game.coils.lifter.enable()
                    if self.game.switches.trough2.is_inactive() and self.game.ball_count.position <= 7:
                        if self.game.extra_ball.position >= 12:
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
            self.delay(name="display", delay=0.1, handler=graphics.stars.display, param=self)

    def sw_hole2_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(2)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.stars.display, param=self)

    def sw_hole3_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(3)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.stars.display, param=self)

    def sw_hole4_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(4)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.stars.display, param=self)

    def sw_hole5_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(5)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.stars.display, param=self)

    def sw_hole6_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(6)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.stars.display, param=self)

    def sw_hole7_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(7)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.stars.display, param=self)

    def sw_hole8_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(8)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.stars.display, param=self)

    def sw_hole9_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(9)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.stars.display, param=self)

    def sw_hole10_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(10)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.stars.display, param=self)

    def sw_hole11_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(11)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.stars.display, param=self)

    def sw_hole12_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(12)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.stars.display, param=self)

    def sw_hole13_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(13)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.stars.display, param=self)

    def sw_hole14_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(14)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.stars.display, param=self)

    def sw_hole15_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(15)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.stars.display, param=self)

    def sw_hole16_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(16)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.stars.display, param=self)

    def sw_hole17_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(17)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.stars.display, param=self)

    def sw_hole18_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(18)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.stars.display, param=self)

    def sw_hole19_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(19)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.stars.display, param=self)

    def sw_hole20_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(20)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.stars.display, param=self)

    def sw_hole21_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(21)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.stars.display, param=self)

    def sw_hole22_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(22)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.stars.display, param=self)

    def sw_hole23_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(23)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.stars.display, param=self)

    def sw_hole24_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(24)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.stars.display, param=self)

    def sw_hole25_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(25)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.stars.display, param=self)

    def sw_replayReset_active(self, sw):
        self.game.anti_cheat.disengage()
        self.holes = []
#        self.cancel_delayed(name="blink_title")
        graphics.stars.display(self)
        self.tilt_actions()
#        self.delay(name="blink_title", delay=1, handler=self.blink_title)
        self.replay_step_down(self.game.replays)

    def tilt_actions(self):
        self.game.start.disengage()
        self.cancel_delayed(name="replay_reset")
        self.cancel_delayed(name="card1_replay_step_up")
        self.cancel_delayed(name="card2_replay_step_up")
        self.cancel_delayed(name="card3_replay_step_up")
        self.game.search_index.disengage()
        if self.game.switches.shutter.is_active() and self.game.ball_count.position == 0:
            self.game.coils.shutter.enable()
        self.holes = []
        self.game.selector.reset()
        self.game.extra_ball.reset()
        self.game.all_double.disengage()
        self.game.c1_double.disengage()
        self.game.c2_double.disengage()
        self.game.c3_double.disengage()
        self.game.sixteen.disengage()
        self.game.fifteen.disengage()
        self.game.fourteen.disengage()
        self.game.nineteen.disengage()
        self.game.seventeen.disengage()
        self.game.twentytwo.disengage()
        self.game.ball_count.reset()
        self.game.anti_cheat.engage(game)
        self.game.tilt.engage(self.game)
        self.game.sound.stop_music()
        self.game.sound.play('tilt')
        # displays "Tilt" on the backglass, you have to recoin.
        self.delay(name="display", delay=0.1, handler=graphics.stars.display, param=self)

    def sw_tilt_active(self, sw):
        if self.game.tilt.status == False:
            self.tilt_actions()

    def replay_step_down(self, number=0):
        if number > 0:
            if number > 1:
                self.game.replays -= 1
                graphics.replay_step_down(self.game.replays, graphics.stars.reel1, graphics.stars.reel10, graphics.stars.reel100)
                self.game.coils.registerDown.pulse()
                number -= 1
                graphics.stars.display(self)
                self.delay(name="replay_reset", delay=0.0, handler=self.replay_step_down, param=number)
            elif number == 1:
                self.game.replays -= 1
                graphics.replay_step_down(self.game.replays, graphics.stars.reel1, graphics.stars.reel10, graphics.stars.reel100)
                self.game.coils.registerDown.pulse()
                number -= 1
                graphics.stars.display(self)
                self.cancel_delayed(name="replay_reset")
        else: 
            if self.game.replays > 0:
                self.game.replays -= 1
                graphics.replay_step_down(self.game.replays, graphics.stars.reel1, graphics.stars.reel10, graphics.stars.reel100)
                self.delay(name="display", delay=0.1, handler=graphics.stars.display, param=self)
            self.game.coils.registerDown.pulse()

    def replay_step_up(self):
        if self.game.replays < 899:
            self.game.replays += 1
            graphics.replay_step_up(self.game.replays, graphics.stars.reel1, graphics.stars.reel10, graphics.stars.reel100)
        self.game.coils.registerUp.pulse()
        self.game.coils.bell.pulse()
        self.game.reflex1.stepdown()
        graphics.stars.display(self)

    def sw_yellow_active(self, sw):
        if self.game.ball_count.position >= 4:
            if self.game.eb.status == False:
                self.game.eb.engage(self.game)
                self.delay(name="display", delay=0.1, handler=graphics.stars.display, param=self)
            if self.game.eb.status == True and (self.game.replays > 0 or self.game.switches.freeplay.is_active()):
                self.game.sound.stop('add')
                self.game.sound.play('add')
                self.game.cu = not self.game.cu
                self.game.reflex1.step()
                self.game.reflex2.step()
                self.replay_step_down()
                
                current = self.game.flash.connected_rivet()
                self.game.flash.spin()
                new = self.game.flash.connected_rivet()
                f = [1,3,12,14,17,21,24]
                g = [2,6,10,11,20,23]
                h = [5,9,13,15,19,22]
                i = [0,4,7,8,16,18]
                if new > current:
                    difference = new - current
                    for j in range(current,difference):
                        if j in f:
                            self.game.mixer1.step()
                        if j in g:
                            self.game.mixer2.step()
                        if j in h:
                            self.game.mixer3.step()
                        if j in i:
                            self.game.mixer4.step()
                else:
                    difference = current - new
                    for j in range(0,difference):
                        if j in f:
                            self.game.mixer1.step()
                        if j in g:
                            self.game.mixer2.step()
                        if j in h:
                            self.game.mixer3.step()
                        if j in i:
                            self.game.mixer4.step()
                
                self.scan_eb()
                self.delay(name="display", delay=0.1, handler=graphics.stars.display, param=self)
                self.game.eb.disengage()
                self.delay(name="display", delay=0.1, handler=graphics.stars.display, param=self)

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
#        self.cancel_delayed(name="blink_title")
        self.game.sound.stop_music()
        self.game.sound.play_music('search', -1)

        for i in range(0, 50):
            self.r = self.closed_search_relays(self.game.searchdisc.position)
            self.game.searchdisc.spin()
            self.wipers = self.r[0]
            self.card = self.r[1]

            # From here, I need to determine based on the value of r, whether to latch the search index and scores.  
            #I need to determine the best winner on each card.  To do this, I must compare the position of the replay counter before
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
                                self.find_winner(s, self.game.selector.position, self.card)
                                break
#        self.delay(name="blink_title", delay=3, handler=self.blink_title)

    def find_winner(self, relays, selector, card):
        if self.game.search_index.status == False and self.game.replays < 899:
            if selector >= 1:
                if card == 1:
                    if relays == 3:
                        if self.game.c1_double.status == True:
                            if self.game.card1_replay_counter.position < 8:
                                self.game.search_index.engage(self.game)
                                self.card1_replay_step_up(8 - self.game.card1_replay_counter.position)
                        else:
                            if self.game.card1_replay_counter.position < 4:
                                self.game.search_index.engage(self.game)
                                self.card1_replay_step_up(4 - self.game.card1_replay_counter.position)
                    if relays == 4:
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
                        if self.game.c2_double.status == True:
                            if self.game.card2_replay_counter.position < 8:
                                self.game.search_index.engage(self.game)
                                self.card2_replay_step_up(8 - self.game.card2_replay_counter.position)
                        else:
                            if self.game.card2_replay_counter.position < 4:
                                self.game.search_index.engage(self.game)
                                self.card2_replay_step_up(4 - self.game.card2_replay_counter.position)
                    if relays == 4:
                        if self.game.c2_double.status == True:
                            if self.game.card2_replay_counter.position < 40:
                                self.game.search_index.engage(self.game)
                                self.card2_replay_step_up(40 - self.game.card2_replay_counter.position)
                        elif self.game.card2_replay_counter.position < 20:
                            self.game.search_index.engage(self.game)
                            self.card2_replay_step_up(20 - self.game.card2_replay_counter.position)
                    if relays == 5:
                        if self.game.c2_double.status == True:
                            if self.game.card2_replay_counter.position < 200:
                                self.game.search_index.engage(self.game)
                                self.card2_replay_step_up(200 - self.game.card2_replay_counter.position)
                        elif self.game.card2_replay_counter.position < 100:
                            self.game.search_index.engage(self.game)
                            self.card2_replay_step_up(100 - self.game.card2_replay_counter.position)
            if selector >= 3:
                if card == 3:
                    if relays == 3:
                        if self.game.c3_double.status == True:
                            if self.game.card3_replay_counter.position < 8:
                                self.game.search_index.engage(self.game)
                                self.card3_replay_step_up(8 - self.game.card3_replay_counter.position)
                        else:
                            if self.game.card3_replay_counter.position < 4:
                                self.game.search_index.engage(self.game)
                                self.card3_replay_step_up(4 - self.game.card3_replay_counter.position)
                    if relays == 4:
                        if self.game.c3_double.status == True:
                            if self.game.card3_replay_counter.position < 40:
                                self.game.search_index.engage(self.game)
                                self.card3_replay_step_up(40 - self.game.card3_replay_counter.position)
                        elif self.game.card3_replay_counter.position < 20:
                            self.game.search_index.engage(self.game)
                            self.card3_replay_step_up(20 - self.game.card3_replay_counter.position)
                    if relays == 5:
                        if self.game.c3_double.status == True:
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


    def closed_search_relays(self, rivets):
        # This function is critical, as it will determine which card is returned, etc.  I need to check the position of the
        # replay counter for the card. We will get a row back
        # that has the numbers on the position which will return the search relay connected.  When three out of the five relays
        # are connected, we get a winner!
        
        self.pos = {}
        # Card 1
        # Note in United Games, that vertical columns are scanned first
        # Horizontal rows scanned after vertical columns, diagonal last
        # Now, the image shown is horizontal, then vertical, so I'm totally
        # confused.  As such, since my search is almost instantaneous, I have
        # to keep this the same as Bally, which scans horizontal, then vertical
        # then diagonal.  I can change this later if needed, but I think
        # this is correct?
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
        self.pos[13] = {}
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
        self.pos[27] = {}
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
        self.pos[41] = {}
        self.pos[42] = {}
        self.pos[43] = {}
        self.pos[44] = {}
        self.pos[45] = {}
        self.pos[46] = {}
        self.pos[47] = {}
        self.pos[48] = {}
        self.pos[49] = {}
        self.pos[50] = {}

        card = 0

        if rivets in range(0,14):
            card = 1
        elif rivets in range(15,28):
            card = 2
        elif rivets in range(29, 42):
            card = 3

        return (self.pos[rivets], card)
    
    def blink_title(self):
        title1 = random.randint(0,1)
        title2 = random.randint(0,1)
        title3 = random.randint(0,1)
        if title1 == 1:
            pos = [289,231]
            image = pygame.image.load('stars/assets/title1_on.png').convert_alpha()
            screen.blit(image, pos)
        if title2 == 1:
            pos = [232,259]
            image = pygame.image.load('stars/assets/title2_on.png').convert_alpha()
            screen.blit(image, pos)
        if title3 == 1:
            pos = [381,256]
            image = pygame.image.load('stars/assets/title3_on.png').convert_alpha()
            screen.blit(image, pos)

        pygame.display.update()
        self.delay(name="display", delay=0.1, handler=graphics.stars.display, param=self)
#        self.delay(name="blink_title", delay=3, handler=self.blink_title)

    def scan_all(self):
        #Animate scanning of everything - this happens through the flash disc
        self.all_probability()
        s = random.randint(1,4)
        self.animate_feature_scan(s)
        self.game.eb.engage(self.game)
        s = random.randint(1,9)
        self.animate_eb_scan(s)
        self.check_outer_mixer3()
        self.game.eb.disengage()

    def check_reflex2(self):
        r2 = self.game.reflex2.position
        mix1 = self.game.mixer1.connected_rivet()
        if r2 == 15 or r2 == 17 or r2 == 19:
            if mix1 == 3 or mix1 == 5:
                return 1
            else:
                return 0
        elif r2 in range(19,22):
            if mix1 == 3 or mix1 == 9 or mix1 == 14 or mix1 == 21:
                return 1
            else:
                return 0
        elif r2 == 5 or r2 == 11 or r2 == 16 or r2 in range (23,28):
            if mix1 == 2 or mix1 == 6 or mix1 == 11 or mix1 == 17 or mix1 == 21:
                return 1
            else:
                return 0
        elif r2 in range(29,32):
            if mix1 == 0 or mix1 == 5 or mix1 == 8 or mix1 == 12 or mix1 == 17 or mix1 == 20 or mix1 == 23:
                return 1
            else:
                return 0
        elif r2 in range(33,40):
            if mix1 == 0 or mix1 == 2 or mix1 == 6 or mix1 == 8 or mix1 == 11 or mix1 == 14 or mix1 == 15 or mix1 == 18 or mix1 == 20 or mix1 == 23:
                return 1
            else:
                return 0
        elif r2 in range(41,48):
            return 1
        else:
            return 1

    def check_mixer2(self):
        mix2 = self.game.mixer2.connected_rivet()
        if self.game.card1_replay_counter.position == 0 and self.game.card2_replay_counter.position == 0 and self.game.card3_replay_counter.position == 0:
            if mix2 == 10 or mix2 == 12 or mix2 == 14 or mix2 == 16 or mix2 == 18 or mix2 == 20 or mix2 == 22 or mix2 == 24:
                self.game.mixer2.spin()
                mix2 = self.game.mixer2.connected_rivet()
            else:
                if mix2 in range(0,9) or mix2 == 11 or mix2 == 13 or mix2 == 15 or mix2 == 17 or mix2 == 19 or mix2 == 21 or mix2 == 23 or mix2 == 25:
                    return 1
                else:
                    return 0
        
        # Check mix2 position.  Inner and outer row of rivets are not emulated
        # properly.  I have no idea the position of the various fingers.
        if mix2 in range(0,9) or mix2 == 11 or mix2 == 13 or mix2 == 15 or mix2 == 17 or mix2 == 19 or mix2 == 21 or mix2 == 23 or mix2 == 25:
            self.game.mixer2.spin()
            mix2 = self.game.mixer2.connected_rivet()
            if mix2 == 0 or mix2 == 4 or mix2 == 6 or mix2 == 8 or mix2 == 12 or mix2 == 14 or mix2 == 18 or mix2 == 19 or mix2 == 20 or mix2 == 22 or mix2 == 23:
                    return 1
            if self.game.c1_double.status == False:
                if mix2 == 1 or mix2 == 7 or mix2 == 10 or mix2 == 13:
                    return 1
            elif self.game.c2_double.status == False:
                if mix2 == 3 or mix2 == 9 or mix2 == 15 or mix2 == 16:
                    return 1
            elif self.game.c3_double.status == False:
                if mix2 == 5 or mix2 == 11 or mix2 == 17 or mix2 == 24:
                    return 1
            else:
                return 0
                
    def check_inner_mixer3(self):
        mix3 = self.game.mixer3.connected_rivet()
        if mix3 == 0 or mix3 == 19 or mix3 == 22 or mix3 == 40:
            self.game.fourteen.engage(self.game)
            if 14 not in self.holes:
                self.holes.append(14)
            self.delay(name="display", delay=0.1, handler=graphics.stars.display, param=self)
        elif mix3 == 7 or mix3 == 25 or mix3 == 28 or mix3 == 46:
            self.game.nineteen.engage(self.game)
            if 19 not in self.holes:
                self.holes.append(19)
            self.delay(name="display", delay=0.1, handler=graphics.stars.display, param=self)
        elif mix3 == 2 or mix3 == 16 or mix3 == 32 or mix3 == 49:
            self.game.twentytwo.engage(self.game)
            if 22 not in self.holes:
                self.holes.append(22)
            self.delay(name="display", delay=0.1, handler=graphics.stars.display, param=self)
        elif mix3 == 3:
            if self.game.selector.position == 3:
                self.game.fifteen.engage(self.game)
                if 15 not in self.holes:
                    self.holes.append(15)
                self.delay(name="display", delay=0.1, handler=graphics.stars.display, param=self)
        elif mix3 == 15:
            if self.game.selector.position == 3:
                self.game.sixteen.engage(self.game)
                if 16 not in self.holes:
                    self.holes.append(16)
                self.delay(name="display", delay=0.1, handler=graphics.stars.display, param=self)
        elif mix3 == 26:
            if self.game.selector.position == 3:
                self.game.seventeen.engage(self.game)
                if 17 not in self.holes:
                    self.holes.append(17)
                self.delay(name="display", delay=0.1, handler=graphics.stars.display, param=self)

    def all_probability(self):
        r2 = self.check_reflex2()
        if r2 == 1:
            m2 = self.check_mixer2()
            if m2 == 1:
                # Mixer 3 actually handles the main portioning for this game.
                m3 = self.check_inner_mixer3()
                m4 = self.check_mixer4()
                if m4 == 1:
                    m3 = self.check_outer_mixer3()

    def check_outer_mixer3(self):
        mix3 = self.game.mixer3.connected_rivet()
        if self.game.eb.status == False:
            if mix3 == 1:
                self.game.all_double.engage(self.game)
                self.game.c1_double.engage(self.game)
                self.game.c2_double.engage(self.game)
                self.game.c3_double.engage(self.game)
            elif mix3 == 11 or mix3 == 21 or mix3 == 33:
                self.game.c1_double.engage(self.game)
            elif mix3 == 4 or mix3 == 14 or mix3 == 24 or mix3 == 31:
                self.game.c2_double.engage(self.game)
            elif mix3 == 17 or mix3 == 27 or mix3 == 37 or mix3 == 43:
                self.game.c3_double.engage(self.game)
        elif mix3 == 0 or mix3 == 3 or mix3 == 5 or mix3 == 7 or mix3 == 10 or mix3 == 13 or mix3 == 19 or mix3 == 20 or mix3 == 22 or mix3 == 26 or mix3 == 29 or mix3 == 30 or mix3 == 32 or mix3 == 34 or mix3 == 36 or mix3 == 39 or mix3 == 42 or mix3 == 44 or mix3 == 47:
            self.check_extra_ball(3)
        elif mix3 == 6 or mix3 == 9 or mix3 == 16 or mix3 == 23 or mix3 == 40 or mix3 == 45 or mix3 == 48:
            self.check_extra_ball(7)
        elif mix3 == 2 or mix3 == 7 or mix3 == 12 or mix3 == 15 or mix3 == 18 or mix3 == 25 or mix3 == 28 or mix3 == 35 or mix3 == 38 or mix3 == 41 or mix3 == 46 or mix3 == 49:
            self.check_extra_ball(1)

    def check_extra_ball(self, maximum):
        r1 = self.game.reflex1.position
        if r1 == 3 or r1 == 8 or r1 == 12 or r1 == 15 or r1 == 15 or r1 == 20 or r1 == 26 or r1 == 33 or r1 == 40 or r1 == 47:
            if self.game.extra_ball.position < 12:
                if maximum == 1:
                    self.game.extra_ball.step()
                    self.check_lifter_status()
                    self.delay(name="display", delay=0.1, handler=graphics.stars.display, param=self)
                elif maximum == 3:
                        self.game.extra_ball.step()
                        self.check_lifter_status()
                        self.delay(name="display", delay=0.1, handler=graphics.stars.display, param=self)
                        self.game.extra_ball.step()
                        self.check_lifter_status()
                        self.delay(name="display", delay=0.1, handler=graphics.stars.display, param=self)
                        self.game.extra_ball.step()
                        self.check_lifter_status()
                elif maximum == 7:
                    if game.extra_ball.position < 7:
                        self.game.extra_ball.step()
                        self.check_lifter_status()
                        self.delay(name="display", delay=0.1, handler=graphics.stars.display, param=self)
                    if game.extra_ball.position < 7:
                        self.game.extra_ball.step()
                        self.check_lifter_status()
                        self.delay(name="display", delay=0.1, handler=graphics.stars.display, param=self)
                    if game.extra_ball.position < 7:
                        self.game.extra_ball.step()
                        self.check_lifter_status()
                        self.delay(name="display", delay=0.1, handler=graphics.stars.display, param=self)
                    if game.extra_ball.position < 7:
                        self.game.extra_ball.step()
                        self.check_lifter_status()
                        self.delay(name="display", delay=0.1, handler=graphics.stars.display, param=self)
                    if game.extra_ball.position < 7:
                        self.game.extra_ball.step()
                        self.check_lifter_status()
                        self.delay(name="display", delay=0.1, handler=graphics.stars.display, param=self)
                    if game.extra_ball.position < 7:
                        self.game.extra_ball.step()
                        self.check_lifter_status()
                        self.delay(name="display", delay=0.1, handler=graphics.stars.display, param=self)
                    if game.extra_ball.position < 7:
                        self.game.extra_ball.step()
                        self.check_lifter_status()
                        self.delay(name="display", delay=0.1, handler=graphics.stars.display, param=self)

    def check_mixer4(self):
        mix4 = self.game.mixer4.connected_rivet()
        if self.game.fifteen.status == False and self.game.sixteen.status == False and self.game.seventeen.status == False and self.game.fourteen.status == False and self.game.nineteen.status == False and self.game.twentytwo.status == False:
            return 1
        elif self.game.fifteen.status == True:
            if mix4 == 1 or mix4 == 6 or mix4 == 8 or mix4 == 14 or mix4 == 17 or mix4 == 22:
                return 0
        elif self.game.sixteen.status == True:
            if mix4 == 5 or mix4 == 7 or mix4 == 12 or mix4 == 15 or mix4 == 21 or mix4 == 23:
                return 0
        elif self.game.seventeen.status == True:
            if mix4 == 0 or mix4 == 2 or mix4 == 9 or mix4 == 10 or mix4 == 16 or mix4 == 19:
                return 0
        elif self.game.fourteen.status == True:
            if mix4 == 1 or mix4 == 5 or mix4 == 9 or mix4 == 13:
                return 0
        elif self.game.nineteen.status == True:
            if mix4 == 0 or mix4 == 4 or mix4 == 17 or mix4 == 21:
                return 0
        elif self.game.twentytwo.status == True:
            if mix4 == 8 or mix4 == 12 or mix4 == 16 or mix4 == 20:
                return 0
        else:
            if mix4 == 2 or mix4 == 3 or mix4 == 4 or mix4 == 6 or mix4 == 7 or mix4 == 10 or mix4 == 11 or mix4 == 13 or mix4 == 14 or mix4 == 15 or mix4 == 18 or mix4 == 19 or mix4 == 20 or mix4 == 22 or mix4 == 23 or mix4 == 24:
                return 1
            else:
                return 0

    def scan_eb(self):
        if self.game.eb.status == True:
            s = random.randint(1,9)
            self.animate_eb_scan(s)
            self.check_outer_mixer3()
            # Timer resets to 0 position on ball count increasing.  We are fudging this since we will have
            # no good way to measure balls as they return back to the trough.  The ball count unit cannot be
            # relied upon as we do not have a switch in the outhole, and the trough logic is too complex for
            # the task at hand.
            # TODO: implement thunk noises into the units.py to automatically play the noises.
            self.game.timer.reset()
        else:
            # TODO: play thunk noise of EB search bearing no fruit.
            pass
        self.delay(name="display", delay=0.1, handler=graphics.stars.display, param=self)

    def animate_feature_scan(self, s):
        if s > 1:
            self.delay(name="feature_animation", delay=0.1, handler=graphics.stars.feature_animation, param=s)
            self.delay(name="display", delay=0.1, handler=graphics.stars.display, param=self)
            s -= 1
            #self.delay(name="animate_feature", delay=0.1, handler=self.animate_feature_scan, param=s)
        else:
            self.delay(name="display", delay=0.1, handler=graphics.stars.display, param=self)

    def animate_eb_scan(self, s):
        if s > 1:
            self.delay(name="eb_animation", delay=0.1, handler=graphics.stars.eb_animation, param=s)
            self.delay(name="display", delay=0.1, handler=graphics.stars.display, param=self)
            s -= 1
            #self.delay(name="animate_eb", delay=0.1, handler=self.animate_eb_scan, param=s)
        else:
            self.delay(name="display", delay=0.1, handler=graphics.stars.display, param=self)

    # Define reset as the knock-off, anti-cheat relay disabled, and replay reset enabled.  Motors turn while credits are knocked off.
    # When meter reaches zero and the zero limit switch is hit, turn off motor sound and leave backglass gi on, but with tilt displayed.

    def startup(self):        
        # Every bingo requires the meter to register '0' 
        # before allowing coin entry --
        # also needs to show a plain 'off' backglass.
        self.eb = False
        self.tilt_actions()
#        self.delay(name="blink_title", delay=1, handler=self.blink_title)


class Stars(procgame.game.BasicGame):
    """ Stars is the first United game with a standard Bally 25 hole playfield.  It's not _exactly_ the same, but close enough. """
    def __init__(self, machine_type):
        super(Stars, self).__init__(machine_type)
        pygame.mixer.pre_init(44100,-16,2,512)
        self.sound = procgame.sound.SoundController(self)
        self.sound.set_volume(1.0)
        # NOTE: trough_count only counts the number of switches present in the  trough.  It does _not_ count
        #       the number of balls present.   In this game, there  should  be  8  balls.
        self.trough_count = 6

        # Now, the control unit can be in one of two positions, essentially.
        self.cu = 1

        # Subclass my units unique to this game -  modifications must be made to set up mixers and steppers unique to the game
        # NOTE: 'top' positions are indexed using a 0 index, so the top on a 24 position unit is actually 23.

        self.mixer1 = units.Mixer("mixer1", 23)
        self.mixer1.position = random.randint(0,23)
        self.mixer2 = units.Mixer("mixer2", 23)
        self.mixer2.spin()
        self.mixer3 = units.Mixer("mixer3", 23)
        self.mixer3.spin()
        self.mixer4 = units.Mixer("mixer4", 23)
        self.mixer4.spin()

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
 
        #Initialize stepper units used to keep track of features or timing.
        self.timer = units.Stepper("timer", 40)
        self.ball_count = units.Stepper("ball_count", 8)

        # Initialize reflex(es) and mixers unique to this game
        # NOTE:  Reflexes in United games are actually comprised of two
        # separate steppers.  These act as normal continuous steppers, so I
        # need to subclass as steppers.
        self.reflex1 = units.Stepper("reflex1", 50, "Stars", "continuous")
        self.reflex2 = units.Stepper("reflex2", 50, "Stars")

        #In United games, they call this spotting motor the 'flash' motor, 
        #similar to the ball bowlers.
        self.flash = units.Spotting("flash", 24)

        #Check for status of the replay register zero switch.  If positive
        #and machine is just powered on, this will zero out the replays.
        self.replay_reset = units.Relay("replay_reset")
        
        #Extra ball unit contains 12 positions in Atlantic City.  Max of 3 EBs.
        self.extra_ball = units.Stepper("extra_ball", 12)

        #When engage()d, light 6v circuit, and enable game features, scoring,
        #etc. Disengage()d means that the machine is 'soft' tilted. In United
        #games, they call this the lock relay, similar to many other pin
        #manufacturers.
        self.lock = units.Relay("lock")

        #Card score doubling trip relays
        self.c1_double = units.Relay("c1_double")
        self.c2_double = units.Relay("c2_double")
        self.c3_double = units.Relay("c3_double")

        #Selector keeps track of cards in play - in United games, they call
        #this the card step-up, but I'll call it selector for consistency with other
        #multi-card Bally games.
        self.selector = units.Stepper("selector", 3)

        #When engage()d, spin.
        self.start = units.Relay("start")

        #Tilt is separate from anti-cheat in that the trip will move the shutter
        #when the game is tilted with 1st ball in the lane.  Also prevents you
        #from picking back up by killing the anti-cheat.  Can be engaged by 
        #tilt bob, slam tilt switches, or timer at 39th step.
        #Immediately kills motors.
        self.tilt = units.Relay("tilt")

        self.anti_cheat = units.Relay("anti_cheat")

        #Need to define relays for playing ebs
        self.eb = units.Relay("eb")

        #Relay for lighting all doubles
        self.all_double = units.Relay("all_double")

        #Relays for spotted numbers
        self.sixteen = units.Relay("sixteen")
        self.fifteen = units.Relay("fifteen")
        self.fourteen = units.Relay("fourteen")
        self.nineteen = units.Relay("nineteen")
        self.seventeen = units.Relay("seventeen")
        self.twentytwo = units.Relay("twentytwo")

        self.replays = 0

        self.corners_replay_counter = units.Stepper("corners_replay_counter", 400)
        self.returned = False

    def reset(self):
        super(Stars, self).reset()
        self.logger = logging.getLogger('game')
        self.load_config('bingo.yaml')
        self.lock.engage(game)
        
        main_mode = MulticardBingo(self)
        self.modes.add(main_mode)
        

game = Stars(machine_type='pdb')
game.reset()
game.run_loop()
