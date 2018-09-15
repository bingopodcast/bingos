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
from bingo_emulator.graphics.caravan import *

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
        self.game.sound.register_sound('square', "audio/magic_square.wav")
        self.game.sound.register_sound('tilt', "audio/tilt.wav")
        self.game.sound.register_sound('step', "audio/step.wav")
        self.game.sound.register_sound('eb_search', "audio/EB_Search.wav")

    def sw_coin_active(self, sw):
        if self.game.eb_play.status == True and self.game.tilt.status == False:
            self.game.sound.stop('add')
            self.game.sound.play('add')
            begin = self.game.spotting.position
            self.game.spotting.spin()
            self.game.mixer1.spin()
            self.game.mixer2.spin()
            self.game.mixer3.spin()
            self.game.mixer4.spin()
            self.game.coils.counter.pulse()
            self.replay_step_down()
            graphics.caravan.display(self)
            self.animate_eb_scan([begin,self.game.spotting.movement_amount,self.game.spotting.movement_amount])
            self.game.eb_play.disengage()
        else:
            self.game.tilt.disengage()
            self.regular_play()
        self.delay(name="display", delay=0.1, handler=graphics.caravan.display, param=self)

    def sw_startButton_active(self, sw):
        if self.game.replays > 0 or self.game.switches.freeplay.is_active():
            self.game.tilt.disengage()
            self.regular_play()
            self.delay(name="display", delay=0.1, handler=graphics.caravan.display, param=self)

    def sw_trough4_active_for_1s(self, sw):
        if self.game.ball_count.position >= 5:
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
            if self.game.ball_count.position >= 5:
                self.game.returned = True
            self.game.ball_count.position -= 1
            self.check_lifter_status()
        else:
            self.check_lifter_status()

    def sw_enter_active(self, sw):
        if self.game.switches.left.is_active() and self.game.switches.right.is_active():
            self.game.end_run_loop()
            os.system("/home/nbaldridge/proc/bingo_emulator/start_game.sh caravan")
        else:
            max_ball = 4
            if self.game.before_fifth.status == True:
                max_ball = 5

            if self.game.roto_feature.status == True:
                if self.game.ball_count.position < max_ball:
                    self.game.sound.play('square')
                    self.game.roto.step()
                    self.cancel_delayed("roto_animation")
                    self.animate_roto([self.game,1,1])
            self.delay(name="display", delay=0.1, handler=graphics.caravan.display, param=self)

    def sw_enter_active_for_600ms(self,sw):
        max_ball = 4
        if self.game.before_fifth.status == True:
            max_ball = 5

        if self.game.roto_feature.status == True:
            if self.game.ball_count.position < max_ball:
                self.game.sound.play('square')
                self.game.roto.step()
                self.cancel_delayed("roto_animation")
                self.animate_roto([self.game,1,1])
        self.delay(name="display", delay=0.1, handler=graphics.caravan.display, param=self)
        self.delay(name="enter", delay=0.6, handler=self.sw_enter_active_for_600ms, param=sw)


    def check_spot(self):
        if self.game.selection_feature.position >= 5:
            if self.game.spotted.position == 0:
                if 19 not in self.holes:
                    self.holes.append(19)
            if self.game.spotted.position == 1:
                if 21 not in self.holes:
                    self.holes.append(21)
        if self.game.selection_feature.position >= 6:
            if self.game.spotted.position == 2:
                if 25 not in self.holes:
                    self.holes.append(25)
        if self.game.selection_feature.position >= 7:
            print "IN HERE"
            if self.game.spotted.position == 3:
                print "IN SPOTTED"
                if 10 not in self.holes:
                    self.holes.append(10)
        if self.game.selection_feature.position >= 8:
            if self.game.spotted.position == 4:
                if 16 not in self.holes:
                    self.holes.append(16)
        self.delay(name="display", delay=0.1, handler=graphics.caravan.display, param=self)

    def sw_left_active(self, sw):
        max_ball = 4
        if self.game.before_fifth.status == True:
            max_ball = 5

        if self.game.select_spots.status == True:
            if self.game.ball_count.position < max_ball:
                self.game.spotted.stepdown()
                if self.game.selection_feature.position == 5:
                    if self.game.spotted.position == 0:
                        if 21 in self.holes:
                            if self.game.switches.hole21.is_inactive():
                                self.holes.remove(21)
                        if 16 in self.holes:
                            if self.game.switches.hole16.is_inactive():
                                self.holes.remove(16)
                        if 25 in self.holes:
                            if self.game.switches.hole25.is_inactive():
                                self.holes.remove(25)
                        if 10 in self.holes:
                            if self.game.switches.hole10.is_inactive():
                                self.holes.remove(10)
                        if 19 not in self.holes:
                            self.holes.append(19)
                    elif self.game.spotted.position == 1:
                        if 19 in self.holes:
                            if self.game.switches.hole19.is_inactive():
                                self.holes.remove(19)
                        if 21 not in self.holes:
                            self.holes.append(21)
                        if 16 in self.holes:
                            if self.game.switches.hole16.is_inactive():
                                self.holes.remove(16)
                        if 25 in self.holes:
                            if self.game.switches.hole25.is_inactive():
                                self.holes.remove(25)
                        if 10 in self.holes:
                            if self.game.switches.hole10.is_inactive():
                                self.holes.remove(10)
                    else:
                        if 19 in self.holes:
                            if self.game.switches.hole19.is_inactive():
                                self.holes.remove(19)
                        if 16 in self.holes:
                            if self.game.switches.hole16.is_inactive():
                                self.holes.remove(16)
                        if 25 in self.holes:
                            if self.game.switches.hole25.is_inactive():
                                self.holes.remove(25)
                        if 10 in self.holes:
                            if self.game.switches.hole10.is_inactive():
                                self.holes.remove(10)
                        if 21 in self.holes:
                            if self.game.switches.hole21.is_inactive():
                                self.holes.remove(21)
                elif self.game.selection_feature.position == 6:
                    if self.game.spotted.position == 0:
                        if 21 in self.holes:
                            if self.game.switches.hole21.is_inactive():
                                self.holes.remove(21)
                        if 16 in self.holes:
                            if self.game.switches.hole16.is_inactive():
                                self.holes.remove(16)
                        if 25 in self.holes:
                            if self.game.switches.hole25.is_inactive():
                                self.holes.remove(25)
                        if 10 in self.holes:
                            if self.game.switches.hole10.is_inactive():
                                self.holes.remove(10)
                        if 19 not in self.holes:
                            self.holes.append(19)
                    elif self.game.spotted.position == 1:
                        if 19 in self.holes:
                            if self.game.switches.hole19.is_inactive():
                                self.holes.remove(19)
                        if 21 not in self.holes:
                            self.holes.append(21)
                        if 16 in self.holes:
                            if self.game.switches.hole16.is_inactive():
                                self.holes.remove(16)
                        if 25 in self.holes:
                            if self.game.switches.hole25.is_inactive():
                                self.holes.remove(25)
                        if 10 in self.holes:
                            if self.game.switches.hole10.is_inactive():
                                self.holes.remove(10)
                    elif self.game.spotted.position == 2:
                        if 19 in self.holes:
                            if self.game.switches.hole19.is_inactive():
                                self.holes.remove(19)
                        if 16 in self.holes:
                            if self.game.switches.hole16.is_inactive():
                                self.holes.remove(16)
                        if 21 in self.holes:
                            if self.game.switches.hole21.is_inactive():
                                self.holes.remove(21)
                        if 10 in self.holes:
                            if self.game.switches.hole10.is_inactive():
                                self.holes.remove(10)
                        if 25 not in self.holes:
                            self.holes.append(25)
                    else:
                        if 19 in self.holes:
                            if self.game.switches.hole19.is_inactive():
                                self.holes.remove(19)
                        if 16 in self.holes:
                            if self.game.switches.hole16.is_inactive():
                                self.holes.remove(16)
                        if 25 in self.holes:
                            if self.game.switches.hole25.is_inactive():
                                self.holes.remove(25)
                        if 10 in self.holes:
                            if self.game.switches.hole10.is_inactive():
                                self.holes.remove(10)
                        if 21 in self.holes:
                            if self.game.switches.hole21.is_inactive():
                                self.holes.remove(21)
                elif self.game.selection_feature.position == 7: 
                    if self.game.spotted.position == 0:
                        if 21 in self.holes:
                            if self.game.switches.hole21.is_inactive():
                                self.holes.remove(21)
                        if 16 in self.holes:
                            if self.game.switches.hole16.is_inactive():
                                self.holes.remove(16)
                        if 25 in self.holes:
                            if self.game.switches.hole25.is_inactive():
                                self.holes.remove(25)
                        if 10 in self.holes:
                            if self.game.switches.hole10.is_inactive():
                                self.holes.remove(10)
                        if 19 not in self.holes:
                            self.holes.append(19)
                    elif self.game.spotted.position == 1:
                        if 19 in self.holes:
                            if self.game.switches.hole19.is_inactive():
                                self.holes.remove(19)
                        if 21 not in self.holes:
                            self.holes.append(21)
                        if 16 in self.holes:
                            if self.game.switches.hole16.is_inactive():
                                self.holes.remove(16)
                        if 25 in self.holes:
                            if self.game.switches.hole25.is_inactive():
                                self.holes.remove(25)
                        if 10 in self.holes:
                            if self.game.switches.hole10.is_inactive():
                                self.holes.remove(10)
                    elif self.game.spotted.position == 2:
                        if 19 in self.holes:
                            if self.game.switches.hole19.is_inactive():
                                self.holes.remove(19)
                        if 16 in self.holes:
                            if self.game.switches.hole16.is_inactive():
                                self.holes.remove(16)
                        if 21 in self.holes:
                            if self.game.switches.hole21.is_inactive():
                                self.holes.remove(21)
                        if 10 in self.holes:
                            if self.game.switches.hole10.is_inactive():
                                self.holes.remove(10)
                        if 25 not in self.holes:
                            self.holes.append(25)
                    elif self.game.spotted.position == 3:
                        if 19 in self.holes:
                            if self.game.switches.hole19.is_inactive():
                                self.holes.remove(19)
                        if 21 in self.holes:
                            if self.game.switches.hole21.is_inactive():
                                self.holes.remove(21)
                        if 16 in self.holes:
                            if self.game.switches.hole16.is_inactive():
                                self.holes.remove(16)
                        if 25 in self.holes:
                            if self.game.switches.hole25.is_inactive():
                                self.holes.remove(25)
                        if 10 not in self.holes:
                            self.holes.append(10)
                    else:
                        if 19 in self.holes:
                            if self.game.switches.hole19.is_inactive():
                                self.holes.remove(19)
                        if 16 in self.holes:
                            if self.game.switches.hole16.is_inactive():
                                self.holes.remove(16)
                        if 25 in self.holes:
                            if self.game.switches.hole25.is_inactive():
                                self.holes.remove(25)
                        if 10 in self.holes:
                            if self.game.switches.hole10.is_inactive():
                                self.holes.remove(10)
                        if 21 in self.holes:
                            if self.game.switches.hole21.is_inactive():
                                self.holes.remove(21)
                elif self.game.selection_feature.position == 8:
                    if self.game.spotted.position == 0:
                        if 21 in self.holes:
                            if self.game.switches.hole21.is_inactive():
                                self.holes.remove(21)
                        if 16 in self.holes:
                            if self.game.switches.hole16.is_inactive():
                                self.holes.remove(16)
                        if 25 in self.holes:
                            if self.game.switches.hole25.is_inactive():
                                self.holes.remove(25)
                        if 10 in self.holes:
                            if self.game.switches.hole10.is_inactive():
                                self.holes.remove(10)
                        if 19 not in self.holes:
                            self.holes.append(19)
                    elif self.game.spotted.position == 1:
                        if 19 in self.holes:
                            if self.game.switches.hole19.is_inactive():
                                self.holes.remove(19)
                        if 21 not in self.holes:
                            self.holes.append(21)
                        if 16 in self.holes:
                            if self.game.switches.hole16.is_inactive():
                                self.holes.remove(16)
                        if 25 in self.holes:
                            if self.game.switches.hole25.is_inactive():
                                self.holes.remove(25)
                        if 10 in self.holes:
                            if self.game.switches.hole10.is_inactive():
                                self.holes.remove(10)
                    elif self.game.spotted.position == 2:
                        if 19 in self.holes:
                            if self.game.switches.hole19.is_inactive():
                                self.holes.remove(19)
                        if 16 in self.holes:
                            if self.game.switches.hole16.is_inactive():
                                self.holes.remove(16)
                        if 25 not in self.holes:
                            self.holes.append(25)
                        if 10 in self.holes:
                            if self.game.switches.hole10.is_inactive():
                                self.holes.remove(10)
                        if 21 in self.holes:
                            if self.game.switches.hole21.is_inactive():
                                self.holes.remove(21)
                    elif self.game.spotted.position == 3:
                        if 19 in self.holes:
                            if self.game.switches.hole19.is_inactive():
                                self.holes.remove(19)
                        if 21 in self.holes:
                            if self.game.switches.hole21.is_inactive():
                                self.holes.remove(21)
                        if 16 in self.holes:
                            if self.game.switches.hole16.is_inactive():
                                self.holes.remove(16)
                        if 25 in self.holes:
                            if self.game.switches.hole25.is_inactive():
                                self.holes.remove(25)
                        if 10 not in self.holes:
                            self.holes.append(10)
                    elif self.game.spotted.position == 4:
                        if 19 in self.holes:
                            if self.game.switches.hole19.is_inactive():
                                self.holes.remove(19)
                        if 21 in self.holes:
                            if self.game.switches.hole21.is_inactive():
                                self.holes.remove(21)
                        if 25 in self.holes:
                            if self.game.switches.hole25.is_inactive():
                                self.holes.remove(25)
                        if 10 in self.holes:
                            if self.game.switches.hole10.is_inactive():
                                self.holes.remove(10)
                        if 16 not in self.holes:
                            self.holes.append(16)
                    else:
                        if 19 in self.holes:
                            if self.game.switches.hole19.is_inactive():
                                self.holes.remove(19)
                        if 16 in self.holes:
                            if self.game.switches.hole16.is_inactive():
                                self.holes.remove(16)
                        if 25 in self.holes:
                            if self.game.switches.hole25.is_inactive():
                                self.holes.remove(25)
                        if 10 in self.holes:
                            if self.game.switches.hole10.is_inactive():
                                self.holes.remove(10)
                        if 21 in self.holes:
                            if self.game.switches.hole21.is_inactive():
                                self.holes.remove(21)

        self.delay(name="display", delay=0.1, handler=graphics.caravan.display, param=self)

    def sw_right_active(self, sw):
        max_ball = 4
        if self.game.before_fifth.status == True:
            max_ball = 5

        if self.game.select_spots.status == True:
            if self.game.ball_count.position < max_ball:
                self.game.spotted.step()
                if self.game.selection_feature.position == 5:
                    if self.game.spotted.position == 0:
                        if 21 in self.holes:
                            if self.game.switches.hole21.is_inactive():
                                self.holes.remove(21)
                        if 16 in self.holes:
                            if self.game.switches.hole16.is_inactive():
                                self.holes.remove(16)
                        if 25 in self.holes:
                            if self.game.switches.hole25.is_inactive():
                                self.holes.remove(25)
                        if 10 in self.holes:
                            if self.game.switches.hole10.is_inactive():
                                self.holes.remove(10)
                        if 19 not in self.holes:
                            self.holes.append(19)
                    elif self.game.spotted.position == 1:
                        if 19 in self.holes:
                            if self.game.switches.hole19.is_inactive():
                                self.holes.remove(19)
                        if 21 not in self.holes:
                            self.holes.append(21)
                        if 16 in self.holes:
                            if self.game.switches.hole16.is_inactive():
                                self.holes.remove(16)
                        if 25 in self.holes:
                            if self.game.switches.hole25.is_inactive():
                                self.holes.remove(25)
                        if 10 in self.holes:
                            if self.game.switches.hole10.is_inactive():
                                self.holes.remove(10)
                    else:
                        if 19 in self.holes:
                            if self.game.switches.hole19.is_inactive():
                                self.holes.remove(19)
                        if 16 in self.holes:
                            if self.game.switches.hole16.is_inactive():
                                self.holes.remove(16)
                        if 25 in self.holes:
                            if self.game.switches.hole25.is_inactive():
                                self.holes.remove(25)
                        if 10 in self.holes:
                            if self.game.switches.hole10.is_inactive():
                                self.holes.remove(10)
                        if 21 in self.holes:
                            if self.game.switches.hole21.is_inactive():
                                self.holes.remove(21)
                elif self.game.selection_feature.position == 6:
                    if self.game.spotted.position == 0:
                        if 21 in self.holes:
                            if self.game.switches.hole21.is_inactive():
                                self.holes.remove(21)
                        if 16 in self.holes:
                            if self.game.switches.hole16.is_inactive():
                                self.holes.remove(16)
                        if 25 in self.holes:
                            if self.game.switches.hole25.is_inactive():
                                self.holes.remove(25)
                        if 10 in self.holes:
                            if self.game.switches.hole10.is_inactive():
                                self.holes.remove(10)
                        if 19 not in self.holes:
                            self.holes.append(19)
                    elif self.game.spotted.position == 1:
                        if 19 in self.holes:
                            if self.game.switches.hole19.is_inactive():
                                self.holes.remove(19)
                        if 21 not in self.holes:
                            self.holes.append(21)
                        if 16 in self.holes:
                            if self.game.switches.hole16.is_inactive():
                                self.holes.remove(16)
                        if 25 in self.holes:
                            if self.game.switches.hole25.is_inactive():
                                self.holes.remove(25)
                        if 10 in self.holes:
                            if self.game.switches.hole10.is_inactive():
                                self.holes.remove(10)
                    elif self.game.spotted.position == 2:
                        if 19 in self.holes:
                            if self.game.switches.hole19.is_inactive():
                                self.holes.remove(19)
                        if 16 in self.holes:
                            if self.game.switches.hole16.is_inactive():
                                self.holes.remove(16)
                        if 21 in self.holes:
                            if self.game.switches.hole21.is_inactive():
                                self.holes.remove(21)
                        if 10 in self.holes:
                            if self.game.switches.hole10.is_inactive():
                                self.holes.remove(10)
                        if 25 not in self.holes:
                            self.holes.append(25)
                    else:
                        if 19 in self.holes:
                            if self.game.switches.hole19.is_inactive():
                                self.holes.remove(19)
                        if 16 in self.holes:
                            if self.game.switches.hole16.is_inactive():
                                self.holes.remove(16)
                        if 25 in self.holes:
                            if self.game.switches.hole25.is_inactive():
                                self.holes.remove(25)
                        if 10 in self.holes:
                            if self.game.switches.hole10.is_inactive():
                                self.holes.remove(10)
                        if 21 in self.holes:
                            if self.game.switches.hole21.is_inactive():
                                self.holes.remove(21)
                elif self.game.selection_feature.position == 7: 
                    if self.game.spotted.position == 0:
                        if 21 in self.holes:
                            if self.game.switches.hole21.is_inactive():
                                self.holes.remove(21)
                        if 16 in self.holes:
                            if self.game.switches.hole16.is_inactive():
                                self.holes.remove(16)
                        if 25 in self.holes:
                            if self.game.switches.hole25.is_inactive():
                                self.holes.remove(25)
                        if 10 in self.holes:
                            if self.game.switches.hole10.is_inactive():
                                self.holes.remove(10)
                        if 19 not in self.holes:
                            self.holes.append(19)
                    elif self.game.spotted.position == 1:
                        if 19 in self.holes:
                            if self.game.switches.hole19.is_inactive():
                                self.holes.remove(19)
                        if 21 not in self.holes:
                            self.holes.append(21)
                        if 16 in self.holes:
                            if self.game.switches.hole16.is_inactive():
                                self.holes.remove(16)
                        if 25 in self.holes:
                            if self.game.switches.hole25.is_inactive():
                                self.holes.remove(25)
                        if 10 in self.holes:
                            if self.game.switches.hole10.is_inactive():
                                self.holes.remove(10)
                    elif self.game.spotted.position == 2:
                        if 19 in self.holes:
                            if self.game.switches.hole19.is_inactive():
                                self.holes.remove(19)
                        if 16 in self.holes:
                            if self.game.switches.hole16.is_inactive():
                                self.holes.remove(16)
                        if 21 in self.holes:
                            if self.game.switches.hole21.is_inactive():
                                self.holes.remove(21)
                        if 10 in self.holes:
                            if self.game.switches.hole10.is_inactive():
                                self.holes.remove(10)
                        if 25 not in self.holes:
                            self.holes.append(25)
                    elif self.game.spotted.position == 3:
                        if 19 in self.holes:
                            if self.game.switches.hole19.is_inactive():
                                self.holes.remove(19)
                        if 21 in self.holes:
                            if self.game.switches.hole21.is_inactive():
                                self.holes.remove(21)
                        if 16 in self.holes:
                            if self.game.switches.hole16.is_inactive():
                                self.holes.remove(16)
                        if 25 in self.holes:
                            if self.game.switches.hole25.is_inactive():
                                self.holes.remove(25)
                        if 10 not in self.holes:
                            self.holes.append(10)
                    else:
                        if 19 in self.holes:
                            if self.game.switches.hole19.is_inactive():
                                self.holes.remove(19)
                        if 16 in self.holes:
                            if self.game.switches.hole16.is_inactive():
                                self.holes.remove(16)
                        if 25 in self.holes:
                            if self.game.switches.hole25.is_inactive():
                                self.holes.remove(25)
                        if 10 in self.holes:
                            if self.game.switches.hole10.is_inactive():
                                self.holes.remove(10)
                        if 21 in self.holes:
                            if self.game.switches.hole21.is_inactive():
                                self.holes.remove(21)
                elif self.game.selection_feature.position == 8:
                    if self.game.spotted.position == 0:
                        if 21 in self.holes:
                            if self.game.switches.hole21.is_inactive():
                                self.holes.remove(21)
                        if 16 in self.holes:
                            if self.game.switches.hole16.is_inactive():
                                self.holes.remove(16)
                        if 25 in self.holes:
                            if self.game.switches.hole25.is_inactive():
                                self.holes.remove(25)
                        if 10 in self.holes:
                            if self.game.switches.hole10.is_inactive():
                                self.holes.remove(10)
                        if 19 not in self.holes:
                            self.holes.append(19)
                    elif self.game.spotted.position == 1:
                        if 19 in self.holes:
                            if self.game.switches.hole19.is_inactive():
                                self.holes.remove(19)
                        if 21 not in self.holes:
                            self.holes.append(21)
                        if 16 in self.holes:
                            if self.game.switches.hole16.is_inactive():
                                self.holes.remove(16)
                        if 25 in self.holes:
                            if self.game.switches.hole25.is_inactive():
                                self.holes.remove(25)
                        if 10 in self.holes:
                            if self.game.switches.hole10.is_inactive():
                                self.holes.remove(10)
                    elif self.game.spotted.position == 2:
                        if 19 in self.holes:
                            if self.game.switches.hole19.is_inactive():
                                self.holes.remove(19)
                        if 16 in self.holes:
                            if self.game.switches.hole16.is_inactive():
                                self.holes.remove(16)
                        if 25 not in self.holes:
                            self.holes.append(25)
                        if 10 in self.holes:
                            if self.game.switches.hole10.is_inactive():
                                self.holes.remove(10)
                        if 21 in self.holes:
                            if self.game.switches.hole21.is_inactive():
                                self.holes.remove(21)
                    elif self.game.spotted.position == 3:
                        if 19 in self.holes:
                            if self.game.switches.hole19.is_inactive():
                                self.holes.remove(19)
                        if 21 in self.holes:
                            if self.game.switches.hole21.is_inactive():
                                self.holes.remove(21)
                        if 16 in self.holes:
                            if self.game.switches.hole16.is_inactive():
                                self.holes.remove(16)
                        if 25 in self.holes:
                            if self.game.switches.hole25.is_inactive():
                                self.holes.remove(25)
                        if 10 not in self.holes:
                            self.holes.append(10)
                    elif self.game.spotted.position == 4:
                        if 19 in self.holes:
                            if self.game.switches.hole19.is_inactive():
                                self.holes.remove(19)
                        if 21 in self.holes:
                            if self.game.switches.hole21.is_inactive():
                                self.holes.remove(21)
                        if 25 in self.holes:
                            if self.game.switches.hole25.is_inactive():
                                self.holes.remove(25)
                        if 10 in self.holes:
                            if self.game.switches.hole10.is_inactive():
                                self.holes.remove(10)
                        if 16 not in self.holes:
                            self.holes.append(16)
                    else:
                        if 19 in self.holes:
                            if self.game.switches.hole19.is_inactive():
                                self.holes.remove(19)
                        if 16 in self.holes:
                            if self.game.switches.hole16.is_inactive():
                                self.holes.remove(16)
                        if 25 in self.holes:
                            if self.game.switches.hole25.is_inactive():
                                self.holes.remove(25)
                        if 10 in self.holes:
                            if self.game.switches.hole10.is_inactive():
                                self.holes.remove(10)
                        if 21 in self.holes:
                            if self.game.switches.hole21.is_inactive():
                                self.holes.remove(21)



        self.delay(name="display", delay=0.1, handler=graphics.caravan.display, param=self)

    def sw_redstar_active(self, sw):
        if self.game.red_star.status == True:
            if self.game.all_spot.status == False:
                self.game.all_spot.engage(self.game)
                self.game.sound.play('tilt')
            if 5 not in self.holes:
                self.holes.append(5)
            if 8 not in self.holes:
                self.holes.append(8)
            if self.game.ball_count.position >= 5:
                self.search()
        if self.game.lite_a_name.status == True:
            self.game.name.step()
            self.search()
        self.delay(name="display", delay=0.1, handler=graphics.caravan.display, param=self)

    def sw_yellowstar_active(self, sw):
        if self.game.yellow_star.status == True:
            if self.game.all_spot.status == False:
                self.game.all_spot.engage(self.game)
                self.game.sound.play('tilt')
            if 2 not in self.holes:
                self.holes.append(2)
            if 15 not in self.holes:
                self.holes.append(15)
            if self.game.ball_count.position >= 5:
                self.search()

        if self.game.lite_a_name.status == True:
            self.game.name.step()
            self.search()
        self.delay(name="display", delay=0.1, handler=graphics.caravan.display, param=self)
        

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
        self.cancel_delayed(name="both_animation")
        self.cancel_delayed(name="search")
        self.cancel_delayed(name="card1_replay_step_up")
        self.cancel_delayed(name="timeout")
        self.cancel_delayed(name="blink")
        self.cancel_delayed(name="blink_roto")
        self.game.search_index.disengage()
        self.game.coils.counter.pulse()
        self.game.returned = False
        self.game.sound.stop('add')
        self.game.sound.play('add')
        if self.game.start.status == True:
            if self.game.selector.position < 1:
                self.game.selector.step()
            if self.game.switches.shutter.is_inactive():
                self.game.coils.shutter.enable()
        
            self.game.cu = not self.game.cu
            if self.game.odds.position == 2:
                self.game.roto_feature.engage(self.game)
            self.game.reflex.decrease()
            begin = self.game.spotting.position
            self.game.spotting.spin()
            self.game.mixer1.spin()
            self.game.mixer2.spin()
            self.game.mixer3.spin()
            self.game.mixer4.spin()
            self.replay_step_down()
            graphics.caravan.display(self)
            if self.game.eb_play.status == False:
                self.animate_both([begin,self.game.spotting.movement_amount,1])
            self.check_lifter_status()
        else:
            self.holes = []
            self.game.start.engage(self.game)
            self.game.card1_replay_counter.reset()
            self.game.diagonal_replay_counter.reset()
            self.game.corners.disengage()
            if self.game.name.position == 6:
                self.game.name.reset()
            self.game.lite_a_name.disengage()
            self.game.diagonal_separate.reset()
            self.game.diagonal.disengage()
            self.game.super_diagonal.disengage()
            self.game.special_pocket.disengage()
            self.game.before_fourth.disengage()
            self.game.before_fifth.disengage()
            self.game.four_as_five.disengage()
            self.game.red_star.disengage()
            self.game.yellow_star.disengage()
            self.game.coils.redROLamp.disable()
            self.game.coils.yellowROLamp.disable()
            self.game.selection_feature_relay.disengage()
            self.game.odds.reset()
            self.game.roto_feature.disengage()
            self.cancel_delayed("roto_animation")
            self.reset_roto(2)
            self.game.selection_feature.reset()
            self.game.select_spots.disengage()
            self.game.start.engage(self.game)
            self.game.selector.reset()
            self.game.timer.reset()
            self.game.ball_count.reset()
            self.game.extra_ball.reset()
            if self.game.pocket.position == 6:
                self.step_eb(15 - self.game.extra_ball.position)
                self.game.pocket.reset()
            self.game.sound.play_music('motor', -1)
            self.game.before_fourth.engage(self.game)
            self.regular_play()

        self.delay(name="display", delay=0.1, handler=graphics.caravan.display, param=self)
        self.game.tilt.disengage()

    def reset_roto(self, number):
        if number != 0:
            self.game.sound.play('square')
            self.game.roto.step()
            self.delay(name="display", delay=0, handler=graphics.caravan.display, param=self)
            self.cancel_delayed("roto_animation")
            self.animate_roto([self.game,1,1])
            number -= 1
            self.delay(name="reset_roto", delay=0.58, handler=self.reset_roto, param=number)


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
                            if self.game.extra_ball.position >= 5 and self.game.ball_count.position <= 5:
                                if self.game.switches.shooter.is_open() and self.game.switches.trough3.is_closed():
                                    self.game.coils.lifter.enable()
                        if self.game.switches.trough3.is_open():
                            if self.game.extra_ball.position >= 10 and self.game.ball_count.position <= 6:
                                if self.game.switches.shooter.is_open() and self.game.switches.trough2.is_closed():
                                    self.game.coils.lifter.enable()
                        if self.game.switches.trough2.is_inactive() and self.game.ball_count.position <= 7:
                            if self.game.ball_count.position <= 7:
                                if self.game.extra_ball.position >= 15:
                                    if self.game.switches.shooter.is_open():
                                        self.game.coils.lifter.enable()
                    if self.game.returned == True and self.game.ball_count.position in [4,5,6,7]:
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

    def sw_shooter_active(self, sw):
        if self.game.ball_count.position == 7:
            self.game.coils.lifter.disable()
            self.cancel_delayed("lifter_status")

    def sw_ballLift_active_for_500ms(self, sw):
        if self.game.tilt.status == False:
            if self.game.switches.shooter.is_open():
                if self.game.ball_count.position < 5:
                    self.game.coils.lifter.enable()
                if self.game.ball_count.position == 5 and self.game.extra_ball.position >= 5:
                    self.game.coils.lifter.enable()
                if self.game.ball_count.position == 6 and self.game.extra_ball.position >= 10:
                    self.game.coils.lifter.enable()
                if self.game.ball_count.position == 7 and self.game.extra_ball.position >= 15:
                    self.game.coils.lifter.enable()

    def sw_gate_inactive_for_1ms(self, sw):
        self.game.start.disengage()
        self.game.ball_count.step()
        if self.game.switches.shutter.is_active():
            self.game.coils.shutter.enable()
        if self.game.ball_count.position == 5:
            self.game.sound.play('tilt')
            self.game.sound.play('tilt')
        if self.game.ball_count.position >= 5:
            if self.game.search_index.status == False:
                self.search()
        if self.game.ball_count.position <= 7:
            self.check_lifter_status()
        self.delay(name="display", delay=0.1, handler=graphics.caravan.display, param=self)

    # This is really nasty, but it is how we render graphics for each individual hole.
    # numbers are added (or removed from) a list.  In this way, I can re-use the same
    # routine even for games where there are ball return functions like Surf Club.

    def sw_hole1_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(1)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.caravan.display, param=self)

    def sw_hole2_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(2)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.caravan.display, param=self)

    def sw_hole3_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(3)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.caravan.display, param=self)

    def sw_hole4_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(4)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.caravan.display, param=self)

    def sw_hole5_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(5)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.caravan.display, param=self)

    def sw_hole6_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(6)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.caravan.display, param=self)

    def sw_hole7_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(7)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.caravan.display, param=self)

    def sw_hole8_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(8)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.caravan.display, param=self)

    def sw_hole9_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(9)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.caravan.display, param=self)

    def sw_hole10_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(10)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.caravan.display, param=self)

    def sw_hole11_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(11)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.caravan.display, param=self)

    def sw_hole12_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(12)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.caravan.display, param=self)

    def sw_hole13_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(13)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.caravan.display, param=self)

    def sw_hole14_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(14)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.caravan.display, param=self)

    def sw_hole15_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(15)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.caravan.display, param=self)

    def sw_hole16_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(16)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.caravan.display, param=self)

    def sw_hole17_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(17)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.caravan.display, param=self)

    def sw_hole18_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(18)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.caravan.display, param=self)

    def sw_hole19_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(19)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.caravan.display, param=self)

    def sw_hole20_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(20)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.caravan.display, param=self)

    def sw_hole21_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(21)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.caravan.display, param=self)

    def sw_hole22_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(22)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.caravan.display, param=self)

    def sw_hole23_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(23)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.caravan.display, param=self)

    def sw_hole24_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(24)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            if self.game.special_pocket.status == True:
                self.game.pocket.step()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.caravan.display, param=self)

    def sw_hole25_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(25)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.caravan.display, param=self)
    
    def sw_replayReset_active(self, sw):
        self.game.anti_cheat.disengage()
        self.holes = []
        graphics.caravan.display(self)
        self.tilt_actions()
        self.replay_step_down(self.game.replays)

    def tilt_actions(self):
        self.game.start.disengage()
        self.cancel_delayed(name="replay_reset")
        self.cancel_delayed(name="card1_replay_step_up")
        self.cancel_delayed(name="blink")
        self.cancel_delayed(name="blink_roto")
        self.cancel_delayed(name="timeout")
        self.game.search_index.disengage()
        if self.game.switches.shutter.is_active() and self.game.ball_count.position == 0:
            self.game.coils.shutter.enable()
        self.holes = []
        self.game.selector.reset()
        self.game.eb_play.disengage()
        self.game.extra_ball.reset()
        self.game.corners.disengage()
        if self.game.name.position == 6:
            self.game.name.reset()
        self.game.each_card.reset()
        self.game.lite_a_name.disengage()
        self.game.diagonal_separate.reset()
        self.game.super_diagonal.disengage()
        self.game.diagonal.disengage()
        self.game.special_pocket.disengage()
        self.game.before_fourth.disengage()
        self.game.before_fifth.disengage()
        self.game.red_star.disengage()
        self.game.yellow_star.disengage()
        self.game.roto_feature.disengage()
        self.game.coils.redROLamp.disable()
        self.game.coils.yellowROLamp.disable()
        self.game.four_as_five.disengage()
        self.game.selection_feature_relay.disengage()
        self.game.odds.reset()
        self.game.selection_feature.reset()
        self.game.select_spots.disengage()
        self.game.ball_count.reset()
        self.game.anti_cheat.engage(game)
        self.game.tilt.engage(self.game)
        self.game.sound.stop_music()
        self.game.sound.play('tilt')
        # displays "Tilt" on the backglass, you have to recoin.
        self.delay(name="display", delay=0.1, handler=graphics.caravan.display, param=self)

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
                graphics.replay_step_down(self.game.replays, graphics.caravan.reel1, graphics.caravan.reel10, graphics.caravan.reel100)
                self.game.coils.registerDown.pulse()
                number -= 1
                graphics.caravan.display(self)
                self.delay(name="replay_reset", delay=0.13, handler=self.replay_step_down, param=number)
            elif number == 1:
                self.game.replays -= 1
                graphics.replay_step_down(self.game.replays, graphics.caravan.reel1, graphics.caravan.reel10, graphics.caravan.reel100)
                self.game.coils.registerDown.pulse()
                number -= 1
                graphics.caravan.display(self)
                self.cancel_delayed(name="replay_reset")
        else: 
            if self.game.replays > 0:
                self.game.replays -= 1
                graphics.replay_step_down(self.game.replays, graphics.caravan.reel1, graphics.caravan.reel10, graphics.caravan.reel100)
                self.delay(name="display", delay=0.1, handler=graphics.caravan.display, param=self)
            self.game.coils.registerDown.pulse()

    def replay_step_up(self):
        if self.game.replays < 899:
            self.game.replays += 1
            graphics.replay_step_up(self.game.replays, graphics.caravan.reel1, graphics.caravan.reel10, graphics.caravan.reel100)
        self.game.coils.registerUp.pulse()
        self.game.reflex.increase()
        graphics.caravan.display(self)

    def sw_yellow_active(self, sw):
        if self.game.ball_count.position >= 4:
            if self.game.eb_play.status == True and (self.game.replays > 0 or self.game.switches.freeplay.is_active()):
                self.cancel_delayed("eb_animation")
                self.game.sound.stop('add')
                self.game.sound.play('add')
                self.game.cu = not self.game.cu
                begin = self.game.spotting.position
                self.game.spotting.spin()
                self.game.mixer1.spin()
                self.game.mixer2.spin()
                self.game.mixer3.spin()
                self.game.mixer4.spin()
                self.replay_step_down()
                self.game.reflex.decrease()
                self.game.coils.counter.pulse()
                graphics.caravan.display(self)
                self.animate_eb_scan([begin,self.game.spotting.movement_amount,self.game.spotting.movement_amount])

                self.delay(name="display", delay=0.1, handler=graphics.caravan.display, param=self)
                self.game.eb_play.disengage()
                self.delay(name="display", delay=0.1, handler=graphics.caravan.display, param=self)
                return
            if self.game.eb_play.status == False:
                self.game.eb_play.engage(self.game)
                self.delay(name="display", delay=0.1, handler=graphics.caravan.display, param=self)
                self.delay(name="yellow", delay=0.1, handler=self.sw_yellow_active, param=sw)
 

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
        
        for i in range(0, 50):
            self.r = self.closed_search_relays(self.game.searchdisc.position)
            self.game.searchdisc.spin()
            self.wipers = self.r[0]
            self.card = self.r[1]
            self.corners = self.r[2]
            self.diagonal = self.r[3]

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
                        s = functions.count_seq(relays)
                        if self.game.selector.position >= self.card:
                            if s >= 2:
                                self.find_winner(s, self.card, self.corners, self.diagonal)
                                break
        if self.game.name.position == 6:
            self.find_winner(0, 1, 0, 0, 1)

    def find_winner(self, relays, card, corners, diagonal, name=0):
        if self.game.search_index.status == False and self.game.replays < 899:
            if self.game.odds.position == 1:
                threeodds = 4
                fourodds = 16
                fiveodds = 50
            elif self.game.odds.position == 2:
                threeodds = 4
                fourodds = 20
                fiveodds = 75
            elif self.game.odds.position == 3:
                threeodds = 8
                fourodds = 24
                fiveodds = 100
            elif self.game.odds.position == 4:
                threeodds = 12
                fourodds = 32
                fiveodds = 100
            elif self.game.odds.position == 5:
                threeodds = 18
                fourodds = 48
                fiveodds = 150
            elif self.game.odds.position == 6:
                threeodds = 36
                fourodds = 72
                fiveodds = 150
            elif self.game.odds.position == 7:
                threeodds = 48
                fourodds = 96
                fiveodds = 200
            elif self.game.odds.position == 8:
                threeodds = 64
                fourodds = 200
                fiveodds = 300


            if name == 1:
                if self.game.card1_replay_counter.position < fiveodds:
                    self.game.search_index.engage(self.game)
                    self.card1_replay_step_up(fiveodds - self.game.card1_replay_counter.position)
            if relays == 3:
                if not corners:
                    if diagonal:
                        if self.game.diagonal.status == True:
                            if self.game.super_diagonal.status == True:
                                if self.game.diagonal_separate.position >= 5:
                                    if self.game.diagonal_replay_counter.position < fourodds:
                                        self.game.search_index.engage(self.game)
                                        self.diagonal_replay_step_up(fourodds - self.game.diagonal_replay_counter.position)
                                else:
                                     if self.game.card1_replay_counter.position < fourodds:
                                        self.game.search_index.engage(self.game)
                                        self.card1_replay_step_up(fourodds - self.game.card1_replay_counter.position)
                            else:
                                if self.game.diagonal_separate.position >= 5:
                                    if self.game.diagonal_replay_counter.position < threeodds:
                                        self.game.search_index.engage(self.game)
                                        self.diagonal_replay_step_up(threeodds - self.game.diagonal_replay_counter.position)
                                else:
                                    if self.game.card1_replay_counter.position < threeodds:
                                        self.game.search_index.engage(self.game)
                                        self.card1_replay_step_up(threeodds - self.game.card1_replay_counter.position)
                    else:
                         if self.game.card1_replay_counter.position < threeodds:
                            self.game.search_index.engage(self.game)
                            self.card1_replay_step_up(threeodds - self.game.card1_replay_counter.position)
            if relays == 4:
                if corners:
                    if self.game.selector.position >= 1:
                        if self.game.corners.status == True:
                            if self.game.card1_replay_counter.position < fiveodds:
                                self.game.search_index.engage(self.game)
                                self.card1_replay_step_up(fiveodds - self.game.card1_replay_counter.position)
                else:
                    if not corners:
                        if diagonal:
                            if self.game.diagonal.status == True:
                                if self.game.super_diagonal.status == True:
                                    if self.game.diagonal_separate.position >= 5:
                                        if self.game.diagonal_replay_counter.position < fiveodds:
                                            self.game.search_index.engage(self.game)
                                            self.diagonal_replay_step_up(fiveodds - self.game.diagonal_replay_counter.position)
                                    else:
                                         if self.game.card1_replay_counter.position < fourodds:
                                            self.game.search_index.engage(self.game)
                                            self.card1_replay_step_up(fourodds - self.game.card1_replay_counter.position)
                                else:
                                    if self.game.diagonal_separate.position >= 5:
                                        if self.game.diagonal_replay_counter.position < fiveodds:
                                            self.game.search_index.engage(self.game)
                                            self.diagonal_replay_step_up(fiveodds - self.game.diagonal_replay_counter.position)
                                    else:
                                        if self.game.card1_replay_counter.position < fourodds:
                                            self.game.search_index.engage(self.game)
                                            self.card1_replay_step_up(fourodds - self.game.card1_replay_counter.position)
                        else:
                             if self.game.card1_replay_counter.position < fourodds:
                                self.game.search_index.engage(self.game)
                                self.card1_replay_step_up(fourodds - self.game.card1_replay_counter.position)
            if relays == 5:
                if self.game.selector.position >= 1:
                    if self.game.card1_replay_counter.position < fiveodds:
                        self.game.search_index.engage(self.game)
                        self.card1_replay_step_up(fiveodds - self.game.card1_replay_counter.position)
                
    def card1_replay_step_up(self, number):
        self.game.sound.stop_music()
        if number >= 1:
            self.game.card1_replay_counter.step()
            number -= 1
            self.replay_step_up()
            if self.game.replays == 899:
                number = 0
            self.delay(name="card1_replay_step_up", delay=0.25, handler=self.card1_replay_step_up, param=number)
        else:
            self.game.search_index.disengage()
            self.cancel_delayed(name="card1_replay_step_up")
            self.search_sounds()
            self.search()
 
    def diagonal_replay_step_up(self, number):
        self.game.sound.stop_music()
        if number >= 1:
            self.game.diagonal_replay_counter.step()
            number -= 1
            self.replay_step_up()
            if self.game.replays == 899:
                number = 0
            self.delay(name="diagonal_replay_step_up", delay=0.25, handler=self.diagonal_replay_step_up, param=number)
        else:
            self.game.search_index.disengage()
            self.cancel_delayed(name="diagonal_replay_step_up")
            self.search_sounds()
            self.search()

    def closed_search_relays(self, rivets):
        # This function is critical, as it will determine which card is returned, etc.  I need to check the position of the
        # replay counter for the card. We will get a row back
        # that has the numbers on the position which will return the search relay connected.  When three out of the five relays
        # are connected, we get a winner!

        if self.game.roto.position == 0:
            self.q2 = 21
            self.q3 = 13
            self.q4 = 22
            self.r2 = 12
            self.r4 = 18
            self.s2 = 20
            self.s3 = 14
            self.s4 = 19
        elif self.game.roto.position == 1:
            self.q2 = 12
            self.q3 = 21
            self.q4 = 13
            self.r2 = 20
            self.r4 = 22
            self.s2 = 14
            self.s3 = 19
            self.s4 = 18
        elif self.game.roto.position == 2:
            self.q2 = 20
            self.q3 = 12
            self.q4 = 21
            self.r2 = 14
            self.r4 = 13
            self.s2 = 19
            self.s3 = 18
            self.s4 = 22
        elif self.game.roto.position == 3:
            self.q2 = 14
            self.q3 = 20
            self.q4 = 12
            self.r2 = 19
            self.r4 = 21
            self.s2 = 18
            self.s3 = 22
            self.s4 = 13
        elif self.game.roto.position == 4:
            self.q2 = 19
            self.q3 = 14
            self.q4 = 20
            self.r2 = 18
            self.r4 = 12
            self.s2 = 22
            self.s3 = 13
            self.s4 = 21
        elif self.game.roto.position == 5:
            self.q2 = 18
            self.q3 = 19
            self.q4 = 14
            self.r2 = 22
            self.r4 = 20
            self.s2 = 13
            self.s3 = 21
            self.s4 = 12
        elif self.game.roto.position == 6:
            self.q2 = 22
            self.q3 = 18
            self.q4 = 19
            self.r2 = 13
            self.r4 = 14
            self.s2 = 21
            self.s3 = 12
            self.s4 = 20
        elif self.game.roto.position == 7:
            self.q2 = 13
            self.q3 = 22
            self.q4 = 18
            self.r2 = 21
            self.r4 = 19
            self.s2 = 12
            self.s3 = 20
            self.s4 = 14

        self.pos = {}
        self.pos[0] = {}
        self.pos[1] = {15:1, self.q2:2, 2:3}
        self.pos[2] = {24:1, self.q3:2, self.r2:3, 1:4}
        self.pos[3] = {8:1, self.r4:2, self.s3:3, 7:4}
        self.pos[4] = {25:1, self.s4:2, 5:3}
        self.pos[5] = {2:1, self.s2:2, 5:3}
        self.pos[6] = {10:1, self.r2:2, self.s3:3, 23:4}
        self.pos[7] = {4:1, self.q3:2, self.r4:3, 17:4}
        self.pos[8] = {15:1, self.q4:2, 25:3}
        self.pos[9] = {}
        self.pos[10] = {}
        self.pos[11] = {}
        self.pos[12] = {}
        self.pos[13] = {}
        self.pos[14] = {}
        self.pos[15] = {9:1, 4:2, 15:3, 24:4, 6:5}
        self.pos[16] = {10:1, self.q2:2, self.q3:3, self.q4:4, 8:5}
        self.pos[17] = {2:1, self.r2:2, 16:3, self.r4:4, 25:5}
        self.pos[18] = {1:1, self.s2:2, self.s3:3, self.s4:4, 17:5}
        self.pos[19] = {11:1, 7:2, 5:3, 23:4, 3:5}
        self.pos[20] = {9:1, 10:2, 2:3, 1:4, 11:5}
        self.pos[21] = {4:1, self.q2:2, self.r2:3, self.s2:4, 7:5}
        self.pos[22] = {15:1, self.q3:2, 16:3, self.s3:4, 5:5}
        self.pos[23] = {24:1, self.q4:2, self.r4:3, self.s4:4, 23:5}
        self.pos[24] = {6:1, 8:2, 25:3, 17:4, 3:5}
        self.pos[25] = {9:1, self.q2:2, 16:3, self.s4:4, 3:5}
        self.pos[26] = {6:1, self.q4:2, 16:3, self.s2:4, 11:5}
        self.pos[27] = {}
        self.pos[28] = {9:1, 6:2, 3:3, 11:4}
        self.pos[29] = {}
        self.pos[30] = {}
        self.pos[31] = {}
        self.pos[32] = {}
        self.pos[33] = {}
        self.pos[34] = {}
        self.pos[35] = {}
        self.pos[36] = {}
        self.pos[37] = {}
        self.pos[38] = {}
        self.pos[39] = {}
        self.pos[40] = {}
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

        corners = False
        card = 1
        diagonal = False

        if rivets in range(1, 9):
            diagonal = True
        if rivets == 28:
            corners = True

        return (self.pos[rivets], card, corners, diagonal)

    def animate_both(self, args):
        start = args[0]
        diff = args[1]
        num = args[2]
        if start + num >= 50:
            start = 0
        if diff >= 0:
            num = num + 1
            graphics.caravan.both_animation([self, start + num])
            self.cancel_delayed(name="display")
            diff = diff - 1
            args = [start,diff,num]
            self.delay(name="both_animation", delay=0.08, handler=self.animate_both, param=args)
        else:
            self.cancel_delayed(name="both_animation")
            self.delay(name="display", delay=0.1, handler=graphics.caravan.display, param=self)
            self.scan_all()

    def animate_roto(self, args):
        self.game = args[0]
        num = args[1]
        square = args[2]
        if num < 65:
            graphics.caravan.roto_animation([self, num * -1, square])
            self.cancel_delayed(name="display")
            num = num + 1
            args = [self.game,num,square]
            self.delay(name="roto_animation", delay=0.007, handler=self.animate_roto, param=args)
        else:
            self.cancel_delayed(name="roto_animation")
            self.delay(name="display", delay=0.1, handler=graphics.caravan.display, param=self)


    def animate_eb_scan(self, args):
        start = args[0]
        diff = args[1]
        num = args[2]
        if start + num >= 50:
            start = 0
        if diff >= 0:
            num = num + 1
            graphics.caravan.eb_animation([self, start + num])
            self.cancel_delayed(name="display")
            diff = diff - 1
            args = [start,diff,num]
            self.delay(name="eb_animation", delay=0.08, handler=self.animate_eb_scan, param=args)
        else:
            self.cancel_delayed(name="eb_animation")
            self.delay(name="display", delay=0.1, handler=graphics.caravan.display, param=self)
            self.scan_eb()


    def scan_all(self):
        #Animate scanning of everything - this happens through the flash disc
        if self.game.odds.position < 1:
            self.game.odds.step()
            self.delay(name="display", delay=0, handler=graphics.caravan.display, param=self)
        else:
            if self.game.odds.position < 2:
                if self.game.odds.position == 1:
                    self.game.diagonal.engage(self.game)
                self.game.odds.step()
            self.all_probability()
            self.delay(name="display", delay=0, handler=graphics.caravan.display, param=self)

    def all_probability(self):
        mix1 = self.game.mixer1.position
        if self.game.reflex.connected_rivet() == 0:
            #Worst position for reflex - requires mixer1 to be in the three liberal positions for the connection of the wires bypassing the reflex.
            if (mix1 in [1,3]):
                self.scan_odds()
        if self.game.reflex.connected_rivet() == 1 and (mix1 in [1,3,21]):
            self.scan_odds()
        elif self.game.reflex.connected_rivet() == 2 and (mix1 in [1,3,21,6]):
            self.scan_odds()
        elif self.game.reflex.connected_rivet() == 3 and (mix1 in [1,3,21,6,20]):
            self.scan_odds()
        elif self.game.reflex.connected_rivet() == 4 and (mix1 in [1,3,21,6,20,5]):
            self.scan_odds()
        elif self.game.reflex.connected_rivet() == 5:
            self.scan_odds()

    def check_extra_step(self):
        i = random.randint(0,32)
        if i == 16:
            return 1
        else:
            return 0

    def scan_odds(self):
        m2 = self.game.mixer2.position
        if self.game.odds.position < 3:
            o = self.odds_probability()
            if o == 1:
                es = self.check_extra_step()
                if es == 1:
                    i = random.randint(1,3)
                    self.step_odds(i)
                else:
                    self.game.odds.step()
            self.features_probability()
        elif m2 == 17:
            o = self.odds_probability()
            if o == 1:
                es = self.check_extra_step()
                if es == 1:
                    i = random.randint(1,3)
                    self.step_odds(i)
                else:
                    self.game.odds.step()
            self.features_probability()
        elif self.game.odds.position ==  3:
            if m2 == 5 or m2 == 15:
                o = self.odds_probability()
                if o == 1:
                    es = self.check_extra_step()
                    if es == 1:
                        i = random.randint(1,3)
                        self.step_odds(i)
                    else:
                        self.game.odds.step()
                self.features_probability()
            elif self.game.cu:
                if m2 == 9:
                    o = self.odds_probability()
                    if o == 1:
                        es = self.check_extra_step()
                        if es == 1:
                            i = random.randint(1,3)
                            self.step_odds(i)
                        else:
                            self.game.odds.step()
                    self.features_probability()

    def features_probability(self):
        sd = self.game.spotting.position
        if sd == 40:
            if self.game.lite_a_name.status == False:
                self.game.lite_a_name.engage(self.game)
                self.game.sound.play('tilt')
        if sd == 45:
            if self.game.red_star.status == False:
                self.game.red_star.engage(self.game)
                self.game.yellow_star.engage(self.game)
                self.game.coils.redROLamp.enable()
                self.game.coils.yellowROLamp.enable()
                self.game.sound.play('tilt')
        if sd == 35:
            if self.game.corners.status == False:
                self.game.corners.engage(self.game)
                self.game.sound.play('tilt')
        if sd == 2 and self.game.diagonal_separate.position == 4:
            self.game.diagonal_separate.step()
        if sd in [0,25]:
            self.game.selection_feature_relay.engage(self.game)
            self.game.selection_feature.step()
            self.check_spot()
            if self.game.selection_feature.position == 4:
                self.game.selection_feature.step()
                self.check_spot()
        if self.game.mixer1.position == 1:
            self.step_selection(5 - self.game.selection_feature.step())
            self.check_spot()
        if sd == 41:
            if self.game.before_fifth.status == False:
                self.game.before_fourth.disengage()
                self.game.before_fifth.engage(self.game)
                self.game.sound.play('tilt')
        if sd == 49:
            self.step_selection(7 - self.game.selection_feature.position)
            self.check_spot()
        if sd == 47:
            self.step_selection(8 - self.game.selection_feature.position)
            self.check_spot()
        if self.game.diagonal_separate.position <= 4:
            self.game.diagonal_separate.step()
        if sd == 20:
            if self.game.super_diagonal.status == False:
                self.game.super_diagonal.engage(self.game)
                self.game.sound.play('tilt')
        if sd == 14:
            if self.game.special_pocket.status == False:
                self.game.special_pocket.engage(self.game)
                self.game.sound.play('tilt')
        
    def odds_probability(self):
        m3 = self.game.mixer3.position
        if m3 in [2,1]:
            return 1
        elif self.game.selection_feature_relay.status == False:
            if m3 in [8,15,5]:
                return 1
        elif self.game.each_card.position < 3:
            if m3 == 11:
                return 1
        elif self.game.each_card.position < 5:
            if m3 == 4:
                return 1
        
    def eb_probability(self):
        mix1 = self.game.mixer1.connected_rivet()
        if self.game.reflex.connected_rivet() == 0:
            #Worst position for reflex - requires mixer1 to be in the three liberal positions for the connection of the wires bypassing the reflex.
            if (mix1 in [1,3]):
                if self.game.mixer4.position in [1,3,4]:
                    self.game.extra_ball.step()
                    self.check_lifter_status()
                if self.game.spotting.position == 25 and self.game.mixer1.position == 4:
                    self.step_eb(15 - self.game.extra_ball.position)
                if self.game.spotting.position == 8:
                    self.step_eb(10 - self.game.extra_ball.position)
                if self.game.spotting.position == 0:
                    self.step_eb(5 - self.game.extra_ball.position)
        elif self.game.reflex.connected_rivet() == 1 and (mix1 in [1,3,21]):
            if self.game.mixer4.position in [1,3,4]:
                self.game.extra_ball.step()
                self.check_lifter_status()
            if self.game.spotting.position == 25 and self.game.mixer1.position == 4:
                self.step_eb(15 - self.game.extra_ball.position)
            if self.game.spotting.position == 8:
                self.step_eb(10 - self.game.extra_ball.position)
            if self.game.spotting.position == 0:
                self.step_eb(5 - self.game.extra_ball.position)
        elif self.game.reflex.connected_rivet() == 2 and (mix1 in [1,3,21,6]):
            if self.game.mixer4.position in [1,3,4]:
                self.game.extra_ball.step()
                self.check_lifter_status()
            if self.game.spotting.position == 25 and self.game.mixer1.position == 4:
                self.step_eb(15 - self.game.extra_ball.position)
            if self.game.spotting.position == 8:
                self.step_eb(10 - self.game.extra_ball.position)
            if self.game.spotting.position == 0:
                self.step_eb(5 - self.game.extra_ball.position)
        elif self.game.reflex.connected_rivet() == 3 and (mix1 in [1,3,21,6,20]):
            if self.game.mixer4.position in [1,3,4]:
                self.game.extra_ball.step()
                self.check_lifter_status()
            if self.game.spotting.position == 25 and self.game.mixer1.position == 4:
                self.step_eb(15 - self.game.extra_ball.position)
            if self.game.spotting.position == 8:
                self.step_eb(10 - self.game.extra_ball.position)
            if self.game.spotting.position == 0:
                self.step_eb(5 - self.game.extra_ball.position)
        elif self.game.reflex.connected_rivet() == 4 and (mix1 in [1,3,21,6,20,5]):
            if self.game.mixer4.position in [1,3,4]:
                self.game.extra_ball.step()
                self.check_lifter_status()
            if self.game.spotting.position == 25 and self.game.mixer1.position == 4:
                self.step_eb(15 - self.game.extra_ball.position)
            if self.game.spotting.position == 8:
                self.step_eb(10 - self.game.extra_ball.position)
            if self.game.spotting.position == 0:
                self.step_eb(5 - self.game.extra_ball.position)
        elif self.game.reflex.connected_rivet() == 5:
            if self.game.mixer4.position in [1,3,4]:
                self.game.extra_ball.step()
                self.check_lifter_status()
            if self.game.spotting.position == 25 and self.game.mixer1.position == 4:
                self.step_eb(15 - self.game.extra_ball.position)
            if self.game.spotting.position == 8:
                self.step_eb(10 - self.game.extra_ball.position)
            if self.game.spotting.position == 0:
                self.step_eb(5 - self.game.extra_ball.position)
        
        self.check_lifter_status()
        self.delay(name="display", delay=0, handler=graphics.caravan.display, param=self)
            
    def step_eb(self, number):
        if number > 0:
            number -= 1
            self.game.extra_ball.step()
            self.delay(name="display", delay=0, handler=graphics.caravan.display, param=self)
            self.check_lifter_status()
            self.delay(name="step_eb", delay=0.1, handler=self.step_eb, param=number)
            if self.game.extra_ball.position >= 9:
                self.check_lifter_status()

    def step_odds(self, number):
        if number > 0:
            number -= 1
            self.game.odds.step()
            self.delay(name="display", delay=0, handler=graphics.caravan.display, param=self)
            self.check_lifter_status()
            self.delay(name="step_odds", delay=0.1, handler=self.step_odds, param=number)
        else:
            self.search()

    def step_selection(self, number):
        if number > 0:
            number -= 1
            self.game.selection_feature.step()
            if self.game.selection_feature.position >= 4:
                self.game.select_spots.engage(self.game)
                self.check_spot()
            self.delay(name="display", delay=0, handler=graphics.caravan.display, param=self)
            self.delay(name="step_selection", delay=0.1, handler=self.step_selection, param=number)

    def scan_eb(self):
        if self.game.eb_play.status == True:
            self.eb_probability()
            # Timer resets to 0 position on ball count increasing.  We are fudging this since we will have
            # no good way to measure balls as they return back to the trough.  The ball count unit cannot be
            # relied upon as we do not have a switch in the outhole, and the trough logic is too complex for
            # the task at hand.
            # TODO: implement thunk noises into the units.py to automatically play the noises.
            self.game.timer.reset()
        else:
            # TODO: play thunk noise of EB search bearing no fruit.
            pass
        self.delay(name="display", delay=0.1, handler=graphics.caravan.display, param=self)


    # Define reset as the knock-off, anti-cheat relay disabled, and replay reset enabled.  Motors turn while credits are knocked off.
    # When meter reaches zero and the zero limit switch is hit, turn off motor sound and leave backglass gi on, but with tilt displayed.

    def startup(self):        
        # Every bingo requires the meter to register '0' 
        # before allowing coin entry --
        # also needs to show a plain 'off' backglass.
        self.eb = False
        self.tilt_actions()

class Caravan(procgame.game.BasicGame):
    def __init__(self, machine_type):
        super(Caravan, self).__init__(machine_type)
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
        self.mixer2 = units.Mixer("mixer2", 23)
        self.mixer3 = units.Mixer("mixer3", 23)
        self.mixer4 = units.Mixer("mixer4", 23)

        self.searchdisc = units.Search("searchdisc", 49)

        #Search relays
        self.s1 = units.Relay("s1")
        self.s2 = units.Relay("s2")
        self.s3 = units.Relay("s3")
        self.s4 = units.Relay("s4")
        self.s5 = units.Relay("s5")
        self.search_index = units.Relay("search_index")

        self.roto_feature = units.Relay("roto_feature")
        self.roto = units.Stepper("roto", 7, 'caravan', "continuous")

        #Odds stepper
        self.odds = units.Stepper("odds", 8, 'caravan')
        
        #Replay Counter
        self.card1_replay_counter = units.Stepper("card1_replay_counter", 300)
        self.diagonal_replay_counter = units.Stepper("diagonal_replay_counter", 300)
 
        #Initialize stepper units used to keep track of features or timing.
        self.timer = units.Stepper("timer", 40)
        self.ball_count = units.Stepper("ball_count", 8)

        # Initialize reflex(es) and mixers unique to this game
        self.reflex = units.Reflex("primary", 100)

        #In United games, they call this spotting motor the 'flash' motor, 
        #similar to the ball bowlers.
        self.spotting = units.Spotting("spotting", 49)

        #Check for status of the replay register zero switch.  If positive
        #and machine is just powered on, this will zero out the replays.
        self.replay_reset = units.Relay("replay_reset")
        
        #Extra ball unit contains 15 positions.  Max of 3 EBs.
        self.extra_ball = units.Stepper("extra_ball", 15)

        self.four_as_five = units.Relay("four_as_five")

        self.each_card = units.Stepper("each_card", 6)

        #When engage()d, light 6v circuit, and enable game features, scoring,
        #etc. Disengage()d means that the machine is 'soft' tilted. In United
        #games, they call this the lock relay, similar to many other pin
        #manufacturers.
        self.lock = units.Relay("lock")

        self.eb_play = units.Relay("eb_play")
        
        #Relay for corners lighting
        self.corners = units.Relay("corners")

        #Selector keeps track of cards in play - in United games, they call
        #this the card step-up, but I'll call it selector for consistency with other
        self.selector = units.Stepper("selector", 1)

        #When engage()d, spin.
        self.start = units.Relay("start")

        #Tilt is separate from anti-cheat in that the trip will move the shutter
        #when the game is tilted with 1st ball in the lane.  Also prevents you
        #from picking back up by killing the anti-cheat.  Can be engaged by 
        #tilt bob, slam tilt switches, or timer at 39th step.
        #Immediately kills motors.
        self.tilt = units.Relay("tilt")

        #Need to define relays for playing ebs
        self.eb = units.Relay("eb")

        # Select-a-spot setup
        self.selection_feature = units.Stepper("selection_feature", 8)
        self.select_spots = units.Relay("select_spots")
        self.spotted = units.Stepper("spotted", 4, "caravan", "continuous")

        #Some special trip relays for spotted numbers and rollovers
        self.red_star = units.Relay("red_star")
        self.yellow_star = units.Relay("yellow_star")

        self.all_spot = units.Relay("all_spot")

        self.before_fourth = units.Relay("before_fourth")
        self.before_fifth = units.Relay("before_fifth")
       
        self.name = units.Stepper("name", 6)

        self.selection_feature_relay = units.Relay("selection_feature_relay")

        self.lite_a_name = units.Relay("lite_a_name")
        self.special_pocket = units.Relay("special_pocket")
        self.pocket = units.Stepper("pocket", 6)

        self.diagonal_separate = units.Stepper("diagonal_separate", 5)
        self.super_diagonal = units.Relay("super_diagonal")
        self.diagonal = units.Relay("diagonal")

        self.anti_cheat = units.Relay("anti_cheat")

        self.replays = 0
        self.returned = False

    def reset(self):
        super(Caravan, self).reset()
        self.logger = logging.getLogger('game')
        self.load_config('bingo.yaml')
        self.lock.engage(game)
        
        main_mode = MulticardBingo(self)
        self.modes.add(main_mode)
        

game = Caravan(machine_type='pdb')
game.reset()
game.run_loop()
