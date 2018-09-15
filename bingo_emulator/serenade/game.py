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
from bingo_emulator.graphics.serenade import *

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
            graphics.serenade.display(self)
            self.animate_eb_scan([begin,self.game.spotting.movement_amount,self.game.spotting.movement_amount])
            self.game.eb_play.disengage()
        else:
            self.game.tilt.disengage()
            self.regular_play()
        self.delay(name="display", delay=0.1, handler=graphics.serenade.display, param=self)

    def sw_startButton_active(self, sw):
        if self.game.replays > 0 or self.game.switches.freeplay.is_active():
            self.game.tilt.disengage()
            self.regular_play()
            self.delay(name="display", delay=0.1, handler=graphics.serenade.display, param=self)

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
            os.system("/home/nbaldridge/proc/bingo_emulator/start_game.sh serenade")

    def check_spot(self):
        if self.game.selection_feature.position >= 5:
            if self.game.spotted.position == 0:
                if 19 not in self.holes:
                    self.holes.append(19)
            if self.game.spotted.position == 1:
                if 20 not in self.holes:
                    self.holes.append(20)
        if self.game.selection_feature.position >= 6:
            if self.game.spotted.position == 2:
                if 21 not in self.holes:
                    self.holes.append(21)
        if self.game.selection_feature.position >= 7:
            if self.game.spotted.position == 3:
                if 22 not in self.holes:
                    self.holes.append(22)
        if self.game.selection_feature.position >= 8:
            if self.game.spotted.position == 4:
                if 25 not in self.holes:
                    self.holes.append(25)
        if self.game.selection_feature.position >= 9:
            if self.game.spotted.position == 5:
                if 10 not in self.holes:
                    self.holes.append(10)
        if self.game.selection_feature.position >= 10:
            if self.game.spotted.position == 6:
                if 16 not in self.holes:
                    self.holes.append(16)
        self.delay(name="display", delay=0.1, handler=graphics.serenade.display, param=self)

    def sw_left_active(self, sw):
        max_ball = 4
        if self.game.before_fifth.status == True:
            max_ball = 5

        if self.game.select_spots.status == True:
            if self.game.ball_count.position < max_ball:
                self.game.spotted.stepdown()
                if self.game.selection_feature.position == 5:
                    if self.game.spotted.position == 0:
                        if 20 in self.holes:
                            if self.game.switches.hole20.is_inactive():
                                self.holes.remove(20)
                        if 21 in self.holes:
                            if self.game.switches.hole21.is_inactive():
                                self.holes.remove(21)
                        if 22 in self.holes:
                            if self.game.switches.hole22.is_inactive():
                                self.holes.remove(22)
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
                        if 21 in self.holes:
                            if self.game.switches.hole21.is_inactive():
                                self.holes.remove(21)
                        if 22 in self.holes:
                            if self.game.switches.hole22.is_inactive():
                                self.holes.remove(22)
                        if 16 in self.holes:
                            if self.game.switches.hole16.is_inactive():
                                self.holes.remove(16)
                        if 25 in self.holes:
                            if self.game.switches.hole25.is_inactive():
                                self.holes.remove(25)
                        if 10 in self.holes:
                            if self.game.switches.hole10.is_inactive():
                                self.holes.remove(10)
                        if 20 not in self.holes:
                            self.holes.append(20)
                    else:
                        if 19 in self.holes:
                            if self.game.switches.hole19.is_inactive():
                                self.holes.remove(19)
                        if 20 in self.holes:
                            if self.game.switches.hole20.is_inactive():
                                self.holes.remove(20)
                        if 22 in self.holes:
                            if self.game.switches.hole22.is_inactive():
                                self.holes.remove(22)
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
                        if 20 in self.holes:
                            if self.game.switches.hole20.is_inactive():
                                self.holes.remove(20)
                        if 21 in self.holes:
                            if self.game.switches.hole21.is_inactive():
                                self.holes.remove(21)
                        if 22 in self.holes:
                            if self.game.switches.hole22.is_inactive():
                                self.holes.remove(22)
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
                        if 21 in self.holes:
                            if self.game.switches.hole21.is_inactive():
                                self.holes.remove(21)
                        if 22 in self.holes:
                            if self.game.switches.hole22.is_inactive():
                                self.holes.remove(22)
                        if 16 in self.holes:
                            if self.game.switches.hole16.is_inactive():
                                self.holes.remove(16)
                        if 25 in self.holes:
                            if self.game.switches.hole25.is_inactive():
                                self.holes.remove(25)
                        if 10 in self.holes:
                            if self.game.switches.hole10.is_inactive():
                                self.holes.remove(10)
                        if 20 not in self.holes:
                            self.holes.append(20)
                    elif self.game.spotted.position == 2:
                        if 19 in self.holes:
                            if self.game.switches.hole19.is_inactive():
                                self.holes.remove(19)
                        if 20 in self.holes:
                            if self.game.switches.hole20.is_inactive():
                                self.holes.remove(20)
                        if 22 in self.holes:
                            if self.game.switches.hole22.is_inactive():
                                self.holes.remove(22)
                        if 16 in self.holes:
                            if self.game.switches.hole16.is_inactive():
                                self.holes.remove(16)
                        if 25 in self.holes:
                            if self.game.switches.hole25.is_inactive():
                                self.holes.remove(25)
                        if 10 in self.holes:
                            if self.game.switches.hole10.is_inactive():
                                self.holes.remove(10)
                        if 21 not in self.holes:
                            self.holes.append(21)
                    else:
                        if 19 in self.holes:
                            if self.game.switches.hole19.is_inactive():
                                self.holes.remove(19)
                        if 20 in self.holes:
                            if self.game.switches.hole20.is_inactive():
                                self.holes.remove(20)
                        if 22 in self.holes:
                            if self.game.switches.hole22.is_inactive():
                                self.holes.remove(22)
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
                        if 20 in self.holes:
                            if self.game.switches.hole20.is_inactive():
                                self.holes.remove(20)
                        if 21 in self.holes:
                            if self.game.switches.hole21.is_inactive():
                                self.holes.remove(21)
                        if 22 in self.holes:
                            if self.game.switches.hole22.is_inactive():
                                self.holes.remove(22)
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
                        if 21 in self.holes:
                            if self.game.switches.hole21.is_inactive():
                                self.holes.remove(21)
                        if 22 in self.holes:
                            if self.game.switches.hole22.is_inactive():
                                self.holes.remove(22)
                        if 16 in self.holes:
                            if self.game.switches.hole16.is_inactive():
                                self.holes.remove(16)
                        if 25 in self.holes:
                            if self.game.switches.hole25.is_inactive():
                                self.holes.remove(25)
                        if 10 in self.holes:
                            if self.game.switches.hole10.is_inactive():
                                self.holes.remove(10)
                        if 20 not in self.holes:
                            self.holes.append(20)
                    elif self.game.spotted.position == 2:
                        if 19 in self.holes:
                            if self.game.switches.hole19.is_inactive():
                                self.holes.remove(19)
                        if 20 in self.holes:
                            if self.game.switches.hole20.is_inactive():
                                self.holes.remove(20)
                        if 22 in self.holes:
                            if self.game.switches.hole22.is_inactive():
                                self.holes.remove(22)
                        if 16 in self.holes:
                            if self.game.switches.hole16.is_inactive():
                                self.holes.remove(16)
                        if 25 in self.holes:
                            if self.game.switches.hole25.is_inactive():
                                self.holes.remove(25)
                        if 10 in self.holes:
                            if self.game.switches.hole10.is_inactive():
                                self.holes.remove(10)
                        if 21 not in self.holes:
                            self.holes.append(21)
                    elif self.game.spotted.position == 3:
                        if 19 in self.holes:
                            if self.game.switches.hole19.is_inactive():
                                self.holes.remove(19)
                        if 20 in self.holes:
                            if self.game.switches.hole20.is_inactive():
                                self.holes.remove(20)
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
                        if 22 not in self.holes:
                            self.holes.append(22)
                    else:
                        if 19 in self.holes:
                            if self.game.switches.hole19.is_inactive():
                                self.holes.remove(19)
                        if 20 in self.holes:
                            if self.game.switches.hole20.is_inactive():
                                self.holes.remove(20)
                        if 22 in self.holes:
                            if self.game.switches.hole22.is_inactive():
                                self.holes.remove(22)
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
                        if 20 in self.holes:
                            if self.game.switches.hole20.is_inactive():
                                self.holes.remove(20)
                        if 21 in self.holes:
                            if self.game.switches.hole21.is_inactive():
                                self.holes.remove(21)
                        if 22 in self.holes:
                            if self.game.switches.hole22.is_inactive():
                                self.holes.remove(22)
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
                        if 21 in self.holes:
                            if self.game.switches.hole21.is_inactive():
                                self.holes.remove(21)
                        if 22 in self.holes:
                            if self.game.switches.hole22.is_inactive():
                                self.holes.remove(22)
                        if 16 in self.holes:
                            if self.game.switches.hole16.is_inactive():
                                self.holes.remove(16)
                        if 25 in self.holes:
                            if self.game.switches.hole25.is_inactive():
                                self.holes.remove(25)
                        if 10 in self.holes:
                            if self.game.switches.hole10.is_inactive():
                                self.holes.remove(10)
                        if 20 not in self.holes:
                            self.holes.append(20)
                    elif self.game.spotted.position == 2:
                        if 19 in self.holes:
                            if self.game.switches.hole19.is_inactive():
                                self.holes.remove(19)
                        if 20 in self.holes:
                            if self.game.switches.hole20.is_inactive():
                                self.holes.remove(20)
                        if 22 in self.holes:
                            if self.game.switches.hole22.is_inactive():
                                self.holes.remove(22)
                        if 16 in self.holes:
                            if self.game.switches.hole16.is_inactive():
                                self.holes.remove(16)
                        if 25 in self.holes:
                            if self.game.switches.hole25.is_inactive():
                                self.holes.remove(25)
                        if 10 in self.holes:
                            if self.game.switches.hole10.is_inactive():
                                self.holes.remove(10)
                        if 21 not in self.holes:
                            self.holes.append(21)
                    elif self.game.spotted.position == 3:
                        if 19 in self.holes:
                            if self.game.switches.hole19.is_inactive():
                                self.holes.remove(19)
                        if 20 in self.holes:
                            if self.game.switches.hole20.is_inactive():
                                self.holes.remove(20)
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
                        if 22 not in self.holes:
                            self.holes.append(22)
                    elif self.game.spotted.position == 4:
                        if 19 in self.holes:
                            if self.game.switches.hole19.is_inactive():
                                self.holes.remove(19)
                        if 20 in self.holes:
                            if self.game.switches.hole20.is_inactive():
                                self.holes.remove(20)
                        if 21 in self.holes:
                            if self.game.switches.hole21.is_inactive():
                                self.holes.remove(21)
                        if 22 in self.holes:
                            if self.game.switches.hole22.is_inactive():
                                self.holes.remove(22)
                        if 25 in self.holes:
                            if self.game.switches.hole25.is_inactive():
                                self.holes.remove(25)
                        if 10 in self.holes:
                            if self.game.switches.hole10.is_inactive():
                                self.holes.remove(10)
                        if 25 not in self.holes:
                            self.holes.append(25)
                    else:
                        if 19 in self.holes:
                            if self.game.switches.hole19.is_inactive():
                                self.holes.remove(19)
                        if 20 in self.holes:
                            if self.game.switches.hole20.is_inactive():
                                self.holes.remove(20)
                        if 22 in self.holes:
                            if self.game.switches.hole22.is_inactive():
                                self.holes.remove(22)
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
                elif self.game.selection_feature.position == 9: 
                    if self.game.spotted.position == 0:
                        if 20 in self.holes:
                            if self.game.switches.hole20.is_inactive():
                                self.holes.remove(20)
                        if 21 in self.holes:
                            if self.game.switches.hole21.is_inactive():
                                self.holes.remove(21)
                        if 22 in self.holes:
                            if self.game.switches.hole22.is_inactive():
                                self.holes.remove(22)
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
                        if 21 in self.holes:
                            if self.game.switches.hole21.is_inactive():
                                self.holes.remove(21)
                        if 22 in self.holes:
                            if self.game.switches.hole22.is_inactive():
                                self.holes.remove(22)
                        if 16 in self.holes:
                            if self.game.switches.hole16.is_inactive():
                                self.holes.remove(16)
                        if 25 in self.holes:
                            if self.game.switches.hole25.is_inactive():
                                self.holes.remove(25)
                        if 10 in self.holes:
                            if self.game.switches.hole10.is_inactive():
                                self.holes.remove(10)
                        if 20 not in self.holes:
                            self.holes.append(20)
                    elif self.game.spotted.position == 2:
                        if 19 in self.holes:
                            if self.game.switches.hole19.is_inactive():
                                self.holes.remove(19)
                        if 20 in self.holes:
                            if self.game.switches.hole20.is_inactive():
                                self.holes.remove(20)
                        if 22 in self.holes:
                            if self.game.switches.hole22.is_inactive():
                                self.holes.remove(22)
                        if 16 in self.holes:
                            if self.game.switches.hole16.is_inactive():
                                self.holes.remove(16)
                        if 25 in self.holes:
                            if self.game.switches.hole25.is_inactive():
                                self.holes.remove(25)
                        if 10 in self.holes:
                            if self.game.switches.hole10.is_inactive():
                                self.holes.remove(10)
                        if 21 not in self.holes:
                            self.holes.append(21)
                    elif self.game.spotted.position == 3:
                        if 19 in self.holes:
                            if self.game.switches.hole19.is_inactive():
                                self.holes.remove(19)
                        if 20 in self.holes:
                            if self.game.switches.hole20.is_inactive():
                                self.holes.remove(20)
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
                        if 22 not in self.holes:
                            self.holes.append(22)
                    elif self.game.spotted.position == 4:
                        if 19 in self.holes:
                            if self.game.switches.hole19.is_inactive():
                                self.holes.remove(19)
                        if 20 in self.holes:
                            if self.game.switches.hole20.is_inactive():
                                self.holes.remove(20)
                        if 21 in self.holes:
                            if self.game.switches.hole21.is_inactive():
                                self.holes.remove(21)
                        if 22 in self.holes:
                            if self.game.switches.hole22.is_inactive():
                                self.holes.remove(22)
                        if 16 in self.holes:
                            if self.game.switches.hole16.is_inactive():
                                self.holes.remove(16)
                        if 10 in self.holes:
                            if self.game.switches.hole10.is_inactive():
                                self.holes.remove(10)
                        if 25 not in self.holes:
                            self.holes.append(25)
                    elif self.game.spotted.position == 5:
                        if 19 in self.holes:
                            if self.game.switches.hole19.is_inactive():
                                self.holes.remove(19)
                        if 20 in self.holes:
                            if self.game.switches.hole20.is_inactive():
                                self.holes.remove(20)
                        if 21 in self.holes:
                            if self.game.switches.hole21.is_inactive():
                                self.holes.remove(21)
                        if 22 in self.holes:
                            if self.game.switches.hole22.is_inactive():
                                self.holes.remove(22)
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
                        if 20 in self.holes:
                            if self.game.switches.hole20.is_inactive():
                                self.holes.remove(20)
                        if 22 in self.holes:
                            if self.game.switches.hole22.is_inactive():
                                self.holes.remove(22)
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
                elif self.game.selection_feature.position == 10: 
                    if self.game.spotted.position == 0:
                        if 20 in self.holes:
                            if self.game.switches.hole20.is_inactive():
                                self.holes.remove(20)
                        if 21 in self.holes:
                            if self.game.switches.hole21.is_inactive():
                                self.holes.remove(21)
                        if 22 in self.holes:
                            if self.game.switches.hole22.is_inactive():
                                self.holes.remove(22)
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
                        if 21 in self.holes:
                            if self.game.switches.hole21.is_inactive():
                                self.holes.remove(21)
                        if 22 in self.holes:
                            if self.game.switches.hole22.is_inactive():
                                self.holes.remove(22)
                        if 16 in self.holes:
                            if self.game.switches.hole16.is_inactive():
                                self.holes.remove(16)
                        if 25 in self.holes:
                            if self.game.switches.hole25.is_inactive():
                                self.holes.remove(25)
                        if 10 in self.holes:
                            if self.game.switches.hole10.is_inactive():
                                self.holes.remove(10)
                        if 20 not in self.holes:
                            self.holes.append(20)
                    elif self.game.spotted.position == 2:
                        if 19 in self.holes:
                            if self.game.switches.hole19.is_inactive():
                                self.holes.remove(19)
                        if 20 in self.holes:
                            if self.game.switches.hole20.is_inactive():
                                self.holes.remove(20)
                        if 22 in self.holes:
                            if self.game.switches.hole22.is_inactive():
                                self.holes.remove(22)
                        if 16 in self.holes:
                            if self.game.switches.hole16.is_inactive():
                                self.holes.remove(16)
                        if 25 in self.holes:
                            if self.game.switches.hole25.is_inactive():
                                self.holes.remove(25)
                        if 10 in self.holes:
                            if self.game.switches.hole10.is_inactive():
                                self.holes.remove(10)
                        if 21 not in self.holes:
                            self.holes.append(21)
                    elif self.game.spotted.position == 3:
                        if 19 in self.holes:
                            if self.game.switches.hole19.is_inactive():
                                self.holes.remove(19)
                        if 20 in self.holes:
                            if self.game.switches.hole20.is_inactive():
                                self.holes.remove(20)
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
                        if 22 not in self.holes:
                            self.holes.append(22)
                    elif self.game.spotted.position == 4:
                        if 19 in self.holes:
                            if self.game.switches.hole19.is_inactive():
                                self.holes.remove(19)
                        if 20 in self.holes:
                            if self.game.switches.hole20.is_inactive():
                                self.holes.remove(20)
                        if 21 in self.holes:
                            if self.game.switches.hole21.is_inactive():
                                self.holes.remove(21)
                        if 22 in self.holes:
                            if self.game.switches.hole22.is_inactive():
                                self.holes.remove(22)
                        if 16 in self.holes:
                            if self.game.switches.hole16.is_inactive():
                                self.holes.remove(16)
                        if 10 in self.holes:
                            if self.game.switches.hole10.is_inactive():
                                self.holes.remove(10)
                        if 25 not in self.holes:
                            self.holes.append(25)
                    elif self.game.spotted.position == 5:
                        if 19 in self.holes:
                            if self.game.switches.hole19.is_inactive():
                                self.holes.remove(19)
                        if 20 in self.holes:
                            if self.game.switches.hole20.is_inactive():
                                self.holes.remove(20)
                        if 21 in self.holes:
                            if self.game.switches.hole21.is_inactive():
                                self.holes.remove(21)
                        if 22 in self.holes:
                            if self.game.switches.hole22.is_inactive():
                                self.holes.remove(22)
                        if 16 in self.holes:
                            if self.game.switches.hole16.is_inactive():
                                self.holes.remove(16)
                        if 25 in self.holes:
                            if self.game.switches.hole25.is_inactive():
                                self.holes.remove(25)
                        if 10 not in self.holes:
                            self.holes.append(10)
                    elif self.game.spotted.position == 6:
                        if 19 in self.holes:
                            if self.game.switches.hole19.is_inactive():
                                self.holes.remove(19)
                        if 20 in self.holes:
                            if self.game.switches.hole20.is_inactive():
                                self.holes.remove(20)
                        if 21 in self.holes:
                            if self.game.switches.hole21.is_inactive():
                                self.holes.remove(21)
                        if 22 in self.holes:
                            if self.game.switches.hole22.is_inactive():
                                self.holes.remove(22)
                        if 10 in self.holes:
                            if self.game.switches.hole10.is_inactive():
                                self.holes.remove(10)
                        if 25 in self.holes:
                            if self.game.switches.hole25.is_inactive():
                                self.holes.remove(25)
                        if 16 not in self.holes:
                            self.holes.append(16)
                    else:
                        if 19 in self.holes:
                            if self.game.switches.hole19.is_inactive():
                                self.holes.remove(19)
                        if 20 in self.holes:
                            if self.game.switches.hole20.is_inactive():
                                self.holes.remove(20)
                        if 22 in self.holes:
                            if self.game.switches.hole22.is_inactive():
                                self.holes.remove(22)
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


        self.delay(name="display", delay=0.1, handler=graphics.serenade.display, param=self)

    def sw_right_active(self, sw):
        max_ball = 4
        if self.game.before_fifth.status == True:
            max_ball = 5

        if self.game.select_spots.status == True:
            if self.game.ball_count.position < max_ball:
                self.game.spotted.step()
                if self.game.selection_feature.position == 5:
                    if self.game.spotted.position == 0:
                        if 20 in self.holes:
                            if self.game.switches.hole20.is_inactive():
                                self.holes.remove(20)
                        if 21 in self.holes:
                            if self.game.switches.hole21.is_inactive():
                                self.holes.remove(21)
                        if 22 in self.holes:
                            if self.game.switches.hole22.is_inactive():
                                self.holes.remove(22)
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
                        if 21 in self.holes:
                            if self.game.switches.hole21.is_inactive():
                                self.holes.remove(21)
                        if 22 in self.holes:
                            if self.game.switches.hole22.is_inactive():
                                self.holes.remove(22)
                        if 16 in self.holes:
                            if self.game.switches.hole16.is_inactive():
                                self.holes.remove(16)
                        if 25 in self.holes:
                            if self.game.switches.hole25.is_inactive():
                                self.holes.remove(25)
                        if 10 in self.holes:
                            if self.game.switches.hole10.is_inactive():
                                self.holes.remove(10)
                        if 20 not in self.holes:
                            self.holes.append(20)
                    else:
                        if 19 in self.holes:
                            if self.game.switches.hole19.is_inactive():
                                self.holes.remove(19)
                        if 20 in self.holes:
                            if self.game.switches.hole20.is_inactive():
                                self.holes.remove(20)
                        if 22 in self.holes:
                            if self.game.switches.hole22.is_inactive():
                                self.holes.remove(22)
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
                        if 20 in self.holes:
                            if self.game.switches.hole20.is_inactive():
                                self.holes.remove(20)
                        if 21 in self.holes:
                            if self.game.switches.hole21.is_inactive():
                                self.holes.remove(21)
                        if 22 in self.holes:
                            if self.game.switches.hole22.is_inactive():
                                self.holes.remove(22)
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
                        if 21 in self.holes:
                            if self.game.switches.hole21.is_inactive():
                                self.holes.remove(21)
                        if 22 in self.holes:
                            if self.game.switches.hole22.is_inactive():
                                self.holes.remove(22)
                        if 16 in self.holes:
                            if self.game.switches.hole16.is_inactive():
                                self.holes.remove(16)
                        if 25 in self.holes:
                            if self.game.switches.hole25.is_inactive():
                                self.holes.remove(25)
                        if 10 in self.holes:
                            if self.game.switches.hole10.is_inactive():
                                self.holes.remove(10)
                        if 20 not in self.holes:
                            self.holes.append(20)
                    elif self.game.spotted.position == 2:
                        if 19 in self.holes:
                            if self.game.switches.hole19.is_inactive():
                                self.holes.remove(19)
                        if 20 in self.holes:
                            if self.game.switches.hole20.is_inactive():
                                self.holes.remove(20)
                        if 22 in self.holes:
                            if self.game.switches.hole22.is_inactive():
                                self.holes.remove(22)
                        if 16 in self.holes:
                            if self.game.switches.hole16.is_inactive():
                                self.holes.remove(16)
                        if 25 in self.holes:
                            if self.game.switches.hole25.is_inactive():
                                self.holes.remove(25)
                        if 10 in self.holes:
                            if self.game.switches.hole10.is_inactive():
                                self.holes.remove(10)
                        if 21 not in self.holes:
                            self.holes.append(21)
                    else:
                        if 19 in self.holes:
                            if self.game.switches.hole19.is_inactive():
                                self.holes.remove(19)
                        if 20 in self.holes:
                            if self.game.switches.hole20.is_inactive():
                                self.holes.remove(20)
                        if 22 in self.holes:
                            if self.game.switches.hole22.is_inactive():
                                self.holes.remove(22)
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
                        if 20 in self.holes:
                            if self.game.switches.hole20.is_inactive():
                                self.holes.remove(20)
                        if 21 in self.holes:
                            if self.game.switches.hole21.is_inactive():
                                self.holes.remove(21)
                        if 22 in self.holes:
                            if self.game.switches.hole22.is_inactive():
                                self.holes.remove(22)
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
                        if 21 in self.holes:
                            if self.game.switches.hole21.is_inactive():
                                self.holes.remove(21)
                        if 22 in self.holes:
                            if self.game.switches.hole22.is_inactive():
                                self.holes.remove(22)
                        if 16 in self.holes:
                            if self.game.switches.hole16.is_inactive():
                                self.holes.remove(16)
                        if 25 in self.holes:
                            if self.game.switches.hole25.is_inactive():
                                self.holes.remove(25)
                        if 10 in self.holes:
                            if self.game.switches.hole10.is_inactive():
                                self.holes.remove(10)
                        if 20 not in self.holes:
                            self.holes.append(20)
                    elif self.game.spotted.position == 2:
                        if 19 in self.holes:
                            if self.game.switches.hole19.is_inactive():
                                self.holes.remove(19)
                        if 20 in self.holes:
                            if self.game.switches.hole20.is_inactive():
                                self.holes.remove(20)
                        if 22 in self.holes:
                            if self.game.switches.hole22.is_inactive():
                                self.holes.remove(22)
                        if 16 in self.holes:
                            if self.game.switches.hole16.is_inactive():
                                self.holes.remove(16)
                        if 25 in self.holes:
                            if self.game.switches.hole25.is_inactive():
                                self.holes.remove(25)
                        if 10 in self.holes:
                            if self.game.switches.hole10.is_inactive():
                                self.holes.remove(10)
                        if 21 not in self.holes:
                            self.holes.append(21)
                    elif self.game.spotted.position == 3:
                        if 19 in self.holes:
                            if self.game.switches.hole19.is_inactive():
                                self.holes.remove(19)
                        if 20 in self.holes:
                            if self.game.switches.hole20.is_inactive():
                                self.holes.remove(20)
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
                        if 22 not in self.holes:
                            self.holes.append(22)
                    else:
                        if 19 in self.holes:
                            if self.game.switches.hole19.is_inactive():
                                self.holes.remove(19)
                        if 20 in self.holes:
                            if self.game.switches.hole20.is_inactive():
                                self.holes.remove(20)
                        if 22 in self.holes:
                            if self.game.switches.hole22.is_inactive():
                                self.holes.remove(22)
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
                        if 20 in self.holes:
                            if self.game.switches.hole20.is_inactive():
                                self.holes.remove(20)
                        if 21 in self.holes:
                            if self.game.switches.hole21.is_inactive():
                                self.holes.remove(21)
                        if 22 in self.holes:
                            if self.game.switches.hole22.is_inactive():
                                self.holes.remove(22)
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
                        if 21 in self.holes:
                            if self.game.switches.hole21.is_inactive():
                                self.holes.remove(21)
                        if 22 in self.holes:
                            if self.game.switches.hole22.is_inactive():
                                self.holes.remove(22)
                        if 16 in self.holes:
                            if self.game.switches.hole16.is_inactive():
                                self.holes.remove(16)
                        if 25 in self.holes:
                            if self.game.switches.hole25.is_inactive():
                                self.holes.remove(25)
                        if 10 in self.holes:
                            if self.game.switches.hole10.is_inactive():
                                self.holes.remove(10)
                        if 20 not in self.holes:
                            self.holes.append(20)
                    elif self.game.spotted.position == 2:
                        if 19 in self.holes:
                            if self.game.switches.hole19.is_inactive():
                                self.holes.remove(19)
                        if 20 in self.holes:
                            if self.game.switches.hole20.is_inactive():
                                self.holes.remove(20)
                        if 22 in self.holes:
                            if self.game.switches.hole22.is_inactive():
                                self.holes.remove(22)
                        if 16 in self.holes:
                            if self.game.switches.hole16.is_inactive():
                                self.holes.remove(16)
                        if 25 in self.holes:
                            if self.game.switches.hole25.is_inactive():
                                self.holes.remove(25)
                        if 10 in self.holes:
                            if self.game.switches.hole10.is_inactive():
                                self.holes.remove(10)
                        if 21 not in self.holes:
                            self.holes.append(21)
                    elif self.game.spotted.position == 3:
                        if 19 in self.holes:
                            if self.game.switches.hole19.is_inactive():
                                self.holes.remove(19)
                        if 20 in self.holes:
                            if self.game.switches.hole20.is_inactive():
                                self.holes.remove(20)
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
                        if 22 not in self.holes:
                            self.holes.append(22)
                    elif self.game.spotted.position == 4:
                        if 19 in self.holes:
                            if self.game.switches.hole19.is_inactive():
                                self.holes.remove(19)
                        if 20 in self.holes:
                            if self.game.switches.hole20.is_inactive():
                                self.holes.remove(20)
                        if 21 in self.holes:
                            if self.game.switches.hole21.is_inactive():
                                self.holes.remove(21)
                        if 22 in self.holes:
                            if self.game.switches.hole22.is_inactive():
                                self.holes.remove(22)
                        if 25 in self.holes:
                            if self.game.switches.hole25.is_inactive():
                                self.holes.remove(25)
                        if 10 in self.holes:
                            if self.game.switches.hole10.is_inactive():
                                self.holes.remove(10)
                        if 25 not in self.holes:
                            self.holes.append(25)
                    else:
                        if 19 in self.holes:
                            if self.game.switches.hole19.is_inactive():
                                self.holes.remove(19)
                        if 20 in self.holes:
                            if self.game.switches.hole20.is_inactive():
                                self.holes.remove(20)
                        if 22 in self.holes:
                            if self.game.switches.hole22.is_inactive():
                                self.holes.remove(22)
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
                elif self.game.selection_feature.position == 9: 
                    if self.game.spotted.position == 0:
                        if 20 in self.holes:
                            if self.game.switches.hole20.is_inactive():
                                self.holes.remove(20)
                        if 21 in self.holes:
                            if self.game.switches.hole21.is_inactive():
                                self.holes.remove(21)
                        if 22 in self.holes:
                            if self.game.switches.hole22.is_inactive():
                                self.holes.remove(22)
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
                        if 21 in self.holes:
                            if self.game.switches.hole21.is_inactive():
                                self.holes.remove(21)
                        if 22 in self.holes:
                            if self.game.switches.hole22.is_inactive():
                                self.holes.remove(22)
                        if 16 in self.holes:
                            if self.game.switches.hole16.is_inactive():
                                self.holes.remove(16)
                        if 25 in self.holes:
                            if self.game.switches.hole25.is_inactive():
                                self.holes.remove(25)
                        if 10 in self.holes:
                            if self.game.switches.hole10.is_inactive():
                                self.holes.remove(10)
                        if 20 not in self.holes:
                            self.holes.append(20)
                    elif self.game.spotted.position == 2:
                        if 19 in self.holes:
                            if self.game.switches.hole19.is_inactive():
                                self.holes.remove(19)
                        if 20 in self.holes:
                            if self.game.switches.hole20.is_inactive():
                                self.holes.remove(20)
                        if 22 in self.holes:
                            if self.game.switches.hole22.is_inactive():
                                self.holes.remove(22)
                        if 16 in self.holes:
                            if self.game.switches.hole16.is_inactive():
                                self.holes.remove(16)
                        if 25 in self.holes:
                            if self.game.switches.hole25.is_inactive():
                                self.holes.remove(25)
                        if 10 in self.holes:
                            if self.game.switches.hole10.is_inactive():
                                self.holes.remove(10)
                        if 21 not in self.holes:
                            self.holes.append(21)
                    elif self.game.spotted.position == 3:
                        if 19 in self.holes:
                            if self.game.switches.hole19.is_inactive():
                                self.holes.remove(19)
                        if 20 in self.holes:
                            if self.game.switches.hole20.is_inactive():
                                self.holes.remove(20)
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
                        if 22 not in self.holes:
                            self.holes.append(22)
                    elif self.game.spotted.position == 4:
                        if 19 in self.holes:
                            if self.game.switches.hole19.is_inactive():
                                self.holes.remove(19)
                        if 20 in self.holes:
                            if self.game.switches.hole20.is_inactive():
                                self.holes.remove(20)
                        if 21 in self.holes:
                            if self.game.switches.hole21.is_inactive():
                                self.holes.remove(21)
                        if 22 in self.holes:
                            if self.game.switches.hole22.is_inactive():
                                self.holes.remove(22)
                        if 16 in self.holes:
                            if self.game.switches.hole16.is_inactive():
                                self.holes.remove(16)
                        if 10 in self.holes:
                            if self.game.switches.hole10.is_inactive():
                                self.holes.remove(10)
                        if 25 not in self.holes:
                            self.holes.append(25)
                    elif self.game.spotted.position == 5:
                        if 19 in self.holes:
                            if self.game.switches.hole19.is_inactive():
                                self.holes.remove(19)
                        if 20 in self.holes:
                            if self.game.switches.hole20.is_inactive():
                                self.holes.remove(20)
                        if 21 in self.holes:
                            if self.game.switches.hole21.is_inactive():
                                self.holes.remove(21)
                        if 22 in self.holes:
                            if self.game.switches.hole22.is_inactive():
                                self.holes.remove(22)
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
                        if 20 in self.holes:
                            if self.game.switches.hole20.is_inactive():
                                self.holes.remove(20)
                        if 22 in self.holes:
                            if self.game.switches.hole22.is_inactive():
                                self.holes.remove(22)
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
                elif self.game.selection_feature.position == 10: 
                    if self.game.spotted.position == 0:
                        if 20 in self.holes:
                            if self.game.switches.hole20.is_inactive():
                                self.holes.remove(20)
                        if 21 in self.holes:
                            if self.game.switches.hole21.is_inactive():
                                self.holes.remove(21)
                        if 22 in self.holes:
                            if self.game.switches.hole22.is_inactive():
                                self.holes.remove(22)
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
                        if 21 in self.holes:
                            if self.game.switches.hole21.is_inactive():
                                self.holes.remove(21)
                        if 22 in self.holes:
                            if self.game.switches.hole22.is_inactive():
                                self.holes.remove(22)
                        if 16 in self.holes:
                            if self.game.switches.hole16.is_inactive():
                                self.holes.remove(16)
                        if 25 in self.holes:
                            if self.game.switches.hole25.is_inactive():
                                self.holes.remove(25)
                        if 10 in self.holes:
                            if self.game.switches.hole10.is_inactive():
                                self.holes.remove(10)
                        if 20 not in self.holes:
                            self.holes.append(20)
                    elif self.game.spotted.position == 2:
                        if 19 in self.holes:
                            if self.game.switches.hole19.is_inactive():
                                self.holes.remove(19)
                        if 20 in self.holes:
                            if self.game.switches.hole20.is_inactive():
                                self.holes.remove(20)
                        if 22 in self.holes:
                            if self.game.switches.hole22.is_inactive():
                                self.holes.remove(22)
                        if 16 in self.holes:
                            if self.game.switches.hole16.is_inactive():
                                self.holes.remove(16)
                        if 25 in self.holes:
                            if self.game.switches.hole25.is_inactive():
                                self.holes.remove(25)
                        if 10 in self.holes:
                            if self.game.switches.hole10.is_inactive():
                                self.holes.remove(10)
                        if 21 not in self.holes:
                            self.holes.append(21)
                    elif self.game.spotted.position == 3:
                        if 19 in self.holes:
                            if self.game.switches.hole19.is_inactive():
                                self.holes.remove(19)
                        if 20 in self.holes:
                            if self.game.switches.hole20.is_inactive():
                                self.holes.remove(20)
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
                        if 22 not in self.holes:
                            self.holes.append(22)
                    elif self.game.spotted.position == 4:
                        if 19 in self.holes:
                            if self.game.switches.hole19.is_inactive():
                                self.holes.remove(19)
                        if 20 in self.holes:
                            if self.game.switches.hole20.is_inactive():
                                self.holes.remove(20)
                        if 21 in self.holes:
                            if self.game.switches.hole21.is_inactive():
                                self.holes.remove(21)
                        if 22 in self.holes:
                            if self.game.switches.hole22.is_inactive():
                                self.holes.remove(22)
                        if 16 in self.holes:
                            if self.game.switches.hole16.is_inactive():
                                self.holes.remove(16)
                        if 10 in self.holes:
                            if self.game.switches.hole10.is_inactive():
                                self.holes.remove(10)
                        if 25 not in self.holes:
                            self.holes.append(25)
                    elif self.game.spotted.position == 5:
                        if 19 in self.holes:
                            if self.game.switches.hole19.is_inactive():
                                self.holes.remove(19)
                        if 20 in self.holes:
                            if self.game.switches.hole20.is_inactive():
                                self.holes.remove(20)
                        if 21 in self.holes:
                            if self.game.switches.hole21.is_inactive():
                                self.holes.remove(21)
                        if 22 in self.holes:
                            if self.game.switches.hole22.is_inactive():
                                self.holes.remove(22)
                        if 16 in self.holes:
                            if self.game.switches.hole16.is_inactive():
                                self.holes.remove(16)
                        if 25 in self.holes:
                            if self.game.switches.hole25.is_inactive():
                                self.holes.remove(25)
                        if 10 not in self.holes:
                            self.holes.append(10)
                    elif self.game.spotted.position == 6:
                        if 19 in self.holes:
                            if self.game.switches.hole19.is_inactive():
                                self.holes.remove(19)
                        if 20 in self.holes:
                            if self.game.switches.hole20.is_inactive():
                                self.holes.remove(20)
                        if 21 in self.holes:
                            if self.game.switches.hole21.is_inactive():
                                self.holes.remove(21)
                        if 22 in self.holes:
                            if self.game.switches.hole22.is_inactive():
                                self.holes.remove(22)
                        if 10 in self.holes:
                            if self.game.switches.hole10.is_inactive():
                                self.holes.remove(10)
                        if 25 in self.holes:
                            if self.game.switches.hole25.is_inactive():
                                self.holes.remove(25)
                        if 16 not in self.holes:
                            self.holes.append(16)
                    else:
                        if 19 in self.holes:
                            if self.game.switches.hole19.is_inactive():
                                self.holes.remove(19)
                        if 20 in self.holes:
                            if self.game.switches.hole20.is_inactive():
                                self.holes.remove(20)
                        if 22 in self.holes:
                            if self.game.switches.hole22.is_inactive():
                                self.holes.remove(22)
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

        self.delay(name="display", delay=0.1, handler=graphics.serenade.display, param=self)

    def sw_redstar_active(self, sw):
        if self.game.red_star.status == True:
            if self.game.extra_ball.position < 5:
                self.step_eb(5 - self.game.extra_ball.position)
        if self.game.lite_a_name.status == True:
            self.game.name.step()
            self.search()
        self.delay(name="display", delay=0.1, handler=graphics.serenade.display, param=self)

    def sw_yellowstar_active(self, sw):
        if self.game.yellow_star.status == True:
            if self.game.extra_ball.position < 5:
                self.step_eb(5 - self.game.extra_ball.position)
        if self.game.lite_a_name.status == True:
            self.game.name.step()
            self.search()
        self.delay(name="display", delay=0.1, handler=graphics.serenade.display, param=self)

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
        self.cancel_delayed(name="blink")
        self.cancel_delayed(name="timeout")
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
            self.game.reflex.decrease()
            begin = self.game.spotting.position
            self.game.spotting.spin()
            self.game.mixer1.spin()
            self.game.mixer2.spin()
            self.game.mixer3.spin()
            self.game.mixer4.spin()
            
            self.replay_step_down()
            graphics.serenade.display(self)
            if self.game.eb_play.status == False:
                self.animate_both([begin,self.game.spotting.movement_amount,1])
            self.check_lifter_status()
        else:
            self.holes = []
            self.game.start.engage(self.game)
            self.game.card1_replay_counter.reset()
            self.game.card2_replay_counter.reset()
            self.game.corners1.disengage()
            self.game.corners2.disengage()
            self.game.lite_a_name.disengage()
            self.game.e_card.disengage()
            self.game.before_fourth.disengage()
            self.game.before_fifth.disengage()
            self.game.red_star.disengage()
            self.game.yellow_star.disengage()
            self.game.coils.redROLamp.disable()
            self.game.coils.yellowROLamp.disable()
            self.game.selection_feature_relay.disengage()
            self.game.odds.reset()
            self.game.selection_feature.reset()
            self.game.select_spots.disengage()
            self.game.start.engage(self.game)
            self.game.selector.reset()
            self.game.timer.reset()
            self.game.ball_count.reset()
            self.game.extra_ball.reset()
            self.game.sound.play_music('motor', -1)
            self.game.before_fourth.engage(self.game)
            if self.game.name.position == 7:
                self.step_odds(8)
                self.step_selection(7)
                self.game.name.reset()
                self.game.name.posotion = 1
            self.regular_play()

        self.delay(name="display", delay=0.1, handler=graphics.serenade.display, param=self)
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
        self.delay(name="display", delay=0.1, handler=graphics.serenade.display, param=self)

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
            self.delay(name="display", delay=0.1, handler=graphics.serenade.display, param=self)

    def sw_hole2_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(2)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.serenade.display, param=self)

    def sw_hole3_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(3)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.serenade.display, param=self)

    def sw_hole4_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(4)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.serenade.display, param=self)

    def sw_hole5_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(5)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.serenade.display, param=self)

    def sw_hole6_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(6)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.serenade.display, param=self)

    def sw_hole7_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(7)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.serenade.display, param=self)

    def sw_hole8_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(8)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.serenade.display, param=self)

    def sw_hole9_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(9)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.serenade.display, param=self)

    def sw_hole10_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(10)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.serenade.display, param=self)

    def sw_hole11_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(11)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.serenade.display, param=self)

    def sw_hole12_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(12)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.serenade.display, param=self)
            self.search_sounds()

    def sw_hole13_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(13)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.serenade.display, param=self)

    def sw_hole14_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(14)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.serenade.display, param=self)

    def sw_hole15_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(15)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.serenade.display, param=self)

    def sw_hole16_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(16)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.serenade.display, param=self)

    def sw_hole17_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(17)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.serenade.display, param=self)

    def sw_hole18_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(18)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.serenade.display, param=self)

    def sw_hole19_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(19)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.serenade.display, param=self)

    def sw_hole20_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(20)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.serenade.display, param=self)

    def sw_hole21_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(21)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.serenade.display, param=self)

    def sw_hole22_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(22)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.serenade.display, param=self)
            self.search_sounds()

    def sw_hole23_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(23)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.serenade.display, param=self)

    def sw_hole24_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(24)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            if self.game.lite_a_name.status == True:
                self.game.name.step()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.serenade.display, param=self)

    def sw_hole25_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(25)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.serenade.display, param=self)
    
    def sw_replayReset_active(self, sw):
        self.game.anti_cheat.disengage()
        self.holes = []
        graphics.serenade.display(self)
        self.tilt_actions()
        self.replay_step_down(self.game.replays)

    def tilt_actions(self):
        self.game.start.disengage()
        self.cancel_delayed(name="replay_reset")
        self.cancel_delayed(name="card1_replay_step_up")
        self.cancel_delayed(name="blink")
        self.cancel_delayed(name="timeout")
        self.game.search_index.disengage()
        if self.game.switches.shutter.is_active() and self.game.ball_count.position == 0:
            self.game.coils.shutter.enable()
        self.holes = []
        self.game.selector.reset()
        self.game.extra_ball.reset()
        self.game.corners1.disengage()
        self.game.corners2.disengage()
        if self.game.name.position == 7:
            self.game.name.reset()
            self.game.name.position = 1
        self.game.e_card.disengage()
        self.game.lite_a_name.disengage()
        self.game.before_fourth.disengage()
        self.game.before_fifth.disengage()
        self.game.red_star.disengage()
        self.game.yellow_star.disengage()
        self.game.coils.redROLamp.disable()
        self.game.coils.yellowROLamp.disable()
        self.game.selection_feature_relay.disengage()
        self.game.odds.reset()
        self.game.selection_feature.reset()
        self.game.select_spots.disengage()
        self.game.ball_count.reset()
        self.game.anti_cheat.engage(game)
        self.game.eb_play.disengage()
        self.game.tilt.engage(self.game)
        self.game.sound.stop_music()
        self.game.sound.play('tilt')
        # displays "Tilt" on the backglass, you have to recoin.
        self.delay(name="display", delay=0.1, handler=graphics.serenade.display, param=self)

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
                graphics.replay_step_down(self.game.replays, graphics.serenade.reel1, graphics.serenade.reel10, graphics.serenade.reel100)
                self.game.coils.registerDown.pulse()
                number -= 1
                graphics.serenade.display(self)
                self.delay(name="replay_reset", delay=0.13, handler=self.replay_step_down, param=number)
            elif number == 1:
                self.game.replays -= 1
                graphics.replay_step_down(self.game.replays, graphics.serenade.reel1, graphics.serenade.reel10, graphics.serenade.reel100)
                self.game.coils.registerDown.pulse()
                number -= 1
                graphics.serenade.display(self)
                self.cancel_delayed(name="replay_reset")
        else: 
            if self.game.replays > 0:
                self.game.replays -= 1
                graphics.replay_step_down(self.game.replays, graphics.serenade.reel1, graphics.serenade.reel10, graphics.serenade.reel100)
                self.delay(name="display", delay=0.1, handler=graphics.serenade.display, param=self)
            self.game.coils.registerDown.pulse()

    def replay_step_up(self):
        if self.game.replays < 899:
            self.game.replays += 1
            graphics.replay_step_up(self.game.replays, graphics.serenade.reel1, graphics.serenade.reel10, graphics.serenade.reel100)
        self.game.coils.registerUp.pulse()
        self.game.reflex.increase()
        graphics.serenade.display(self)

    def sw_green_active(self, sw):
        if self.game.switches.drawer.is_inactive():
            if self.game.before_fourth.status == True:
                if self.game.ball_count.position == 3:
                    if self.game.e_card.status == True:
                        self.game.selector.position = 2
            if self.game.before_fifth.status == True:
                if self.game.ball_count.position == 4:
                    if self.game.e_card.status == True:
                        self.game.selector.position = 2
            graphics.serenade.display(self)

    def sw_letterb_active(self, sw):
        if self.game.switches.drawer.is_active():
            if self.game.before_fourth.status == True:
                if self.game.ball_count.position == 3:
                    if self.game.e_card.status == True:
                        self.game.selector.position = 2
            if self.game.before_fifth.status == True:
                if self.game.ball_count.position == 4:
                    if self.game.e_card.status == True:
                        self.game.selector.position = 2
            graphics.serenade.display(self)


    def sw_blue_active(self, sw):
        if self.game.switches.drawer.is_inactive():
            if self.game.before_fourth.status == True:
                if self.game.ball_count.position == 3:
                    if self.game.e_card.status == True:
                        self.game.selector.position = 1
            if self.game.before_fifth.status == True:
                if self.game.ball_count.position == 4:
                    if self.game.e_card.status == True:
                        self.game.selector.position = 1
            graphics.serenade.display(self)

    def sw_lettera_active(self, sw):
        if self.game.switches.drawer.is_active():
            if self.game.before_fourth.status == True:
                if self.game.ball_count.position == 3:
                    if self.game.e_card.status == True:
                        self.game.selector.position = 1
            if self.game.before_fifth.status == True:
                if self.game.ball_count.position == 4:
                    if self.game.e_card.status == True:
                        self.game.selector.position = 1
            graphics.serenade.display(self)

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
                graphics.serenade.display(self)
                self.animate_eb_scan([begin,self.game.spotting.movement_amount,self.game.spotting.movement_amount])

                self.delay(name="display", delay=0.1, handler=graphics.serenade.display, param=self)
                self.game.eb_play.disengage()
                self.delay(name="display", delay=0.1, handler=graphics.serenade.display, param=self)
                return
            if self.game.eb_play.status == False:
                self.game.eb_play.engage(self.game)
                self.delay(name="display", delay=0.1, handler=graphics.serenade.display, param=self)
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
                        if self.game.selector.position == self.card:
                            if s >= 2:
                                self.find_winner(s, self.card, self.corners)
                                break

    def find_winner(self, relays, card, corners, name=0):
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
                    if card == 1:
                        if self.game.selector.position == 1:
                            if self.game.card1_replay_counter.position < threeodds:
                                self.game.search_index.engage(self.game)
                                self.card1_replay_step_up(threeodds - self.game.card1_replay_counter.position)
                    elif card == 2:
                        if self.game.selector.position == 2:
                            if self.game.card2_replay_counter.position < threeodds:
                                self.game.search_index.engage(self.game)
                                self.card2_replay_step_up(threeodds - self.game.card2_replay_counter.position)
            if relays == 4:
                if corners:
                    if card == 1:
                        if self.game.selector.position == 1:
                            if self.game.corners1.status == True:
                                if self.game.card1_replay_counter.position < fiveodds:
                                    self.game.search_index.engage(self.game)
                                    self.card1_replay_step_up(fiveodds - self.game.card1_replay_counter.position)
                    elif card == 2:
                        if self.game.selector.position == 2:
                            if self.game.corners2.status == True:
                                if self.game.card2_replay_counter.position < fiveodds:
                                    self.game.search_index.engage(self.game)
                                    self.card2_replay_step_up(fiveodds - self.game.card2_replay_counter.position)
                else:
                    if not corners:
                        if card == 1:
                            if self.game.selector.position == 1:
                                if self.game.card1_replay_counter.position < fourodds:
                                    self.game.search_index.engage(self.game)
                                    self.card1_replay_step_up(fourodds - self.game.card1_replay_counter.position)
                        elif card == 2:
                            if self.game.selector.position == 2:
                                if self.game.card2_replay_counter.position < fourodds:
                                    self.game.search_index.engage(self.game)
                                    self.card2_replay_step_up(fourodds - self.game.card2_replay_counter.position)
            if relays == 5:
                if card == 1:
                    if self.game.selector.position == 1:
                        if self.game.card1_replay_counter.position < fiveodds:
                            self.game.search_index.engage(self.game)
                            self.card1_replay_step_up(fiveodds - self.game.card1_replay_counter.position)
                elif card == 2:
                    if self.game.selector.position == 2:
                        if self.game.card2_replay_counter.position < fiveodds:
                            self.game.search_index.engage(self.game)
                            self.card2_replay_step_up(fiveodds - self.game.card2_replay_counter.position)

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
 
    def card2_replay_step_up(self, number):
        self.game.sound.stop_music()
        if number >= 1:
            self.game.card2_replay_counter.step()
            number -= 1
            self.replay_step_up()
            if self.game.replays == 899:
                number = 0
            self.delay(name="card2_replay_step_up", delay=0.25, handler=self.card2_replay_step_up, param=number)
        else:
            self.game.search_index.disengage()
            self.cancel_delayed(name="card2_replay_step_up")
            self.search_sounds()
            self.search()
      
    def closed_search_relays(self, rivets):
        # This function is critical, as it will determine which card is returned, etc.  I need to check the position of the
        # replay counter for the card. We will get a row back
        # that has the numbers on the position which will return the search relay connected.  When three out of the five relays
        # are connected, we get a winner!

        self.pos = {}
        self.pos[0] = {}
        self.pos[1] = {17:1, 22:2, 11:3, 2:4, 20:5}
        self.pos[2] = {16:1, 7:2, 12:3, 6:4, 18:5}
        self.pos[3] = {24:1, 8:2, 10:3, 14:4, 1:5}
        self.pos[4] = {25:1, 4:2, 13:3, 5:4, 9:5}
        self.pos[5] = {15:1, 19:2, 21:3, 3:4, 23:5}
        self.pos[6] = {17:1, 16:2, 24:3, 25:4, 15:5}
        self.pos[7] = {22:1, 7:2, 8:3, 4:4, 19:5}
        self.pos[8] = {11:1, 12:2, 10:3, 13:4, 21:5}
        self.pos[9] = {2:1, 6:2, 14:3, 5:4, 3:5}
        self.pos[10] = {20:1, 18:2, 1:3, 9:4, 23:5}
        self.pos[11] = {17:1, 7:2, 10:3, 5:4, 23:5}
        self.pos[12] = {20:1, 6:2, 10:3, 4:4, 15:5}
        self.pos[13] = {17:1, 20:2, 23:3, 15:4}
        self.pos[14] = {}
        self.pos[15] = {9:1, 4:2, 15:3, 24:4, 6:5}
        self.pos[16] = {10:1, 19:2, 14:3, 20:4, 8:5}
        self.pos[17] = {2:1, 18:2, 16:3, 12:4, 25:5}
        self.pos[18] = {1:1, 22:2, 13:3, 21:4, 17:5}
        self.pos[19] = {11:1, 7:2, 5:3, 23:4, 3:5}
        self.pos[20] = {9:1, 10:2, 2:3, 1:4, 11:5}
        self.pos[21] = {4:1, 19:2, 18:3, 22:4, 7:5}
        self.pos[22] = {15:1, 14:2, 16:3, 13:4, 5:5}
        self.pos[23] = {24:1, 20:2, 12:3, 21:4, 23:5}
        self.pos[24] = {6:1, 8:2, 25:3, 17:4, 3:5}
        self.pos[25] = {9:1, 19:2, 16:3, 21:4, 3:5}
        self.pos[26] = {6:1, 20:2, 16:3, 22:4, 11:5}
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
        card = 0

        if rivets in range(0, 14):
            card = 2
        if rivets == 13:
            corners = True
        if rivets in range(15,50):
            card = 1
        if rivets == 28:
            corners = True

        return (self.pos[rivets], card, corners)
       
    def scan_all(self):
        #Animate scanning of everything - this happens through the flash disc
        if self.game.odds.position < 1:
            self.game.odds.step()
            self.delay(name="display", delay=0, handler=graphics.serenade.display, param=self)
        else:
            if self.game.odds.position < 2:
                self.game.odds.step()
            self.all_probability()
            self.delay(name="display", delay=0, handler=graphics.serenade.display, param=self)

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
            if m2 in [5,15]:
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
            if self.game.corners1.status == False:
                self.game.corners1.engage(self.game)
                self.game.sound.play('tilt')
            if self.game.corners2.status == False:
                self.game.corners2.engage(self.game)
                self.game.sound.play('tilt')
        if sd == 30:
            if self.game.corners1.status == False:
                self.game.corners1.engage(self.game)
                self.game.sound.play('tilt')
            if self.game.corners2.status == False:
                self.game.corners2.engage(self.game)
                self.game.sound.play('tilt')
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
            self.step_selection(9 - self.game.selection_feature.position)
            self.check_spot()
        if sd == 47:
            self.step_selection(10 - self.game.selection_feature.position)
            self.check_spot()
        if self.game.e_card.status == False:
            if self.game.cu:
                if self.game.e_card.status == False:
                    self.game.e_card.engage(self.game)
                    self.game.sound.play('tilt')
        
    def odds_probability(self):
        m3 = self.game.mixer3.position
        if m3 in [2,1]:
            return 1
        elif self.game.selection_feature_relay.status == False:
            if m3 in [8,15,5]:
                return 1
        elif self.game.e_card.status == False:
            if m3 == 11:
                return 1
        elif self.game.e_card.status == True:
            if m3 == 4:
                return 1
        
    def eb_probability(self):
        mix1 = self.game.mixer1.connected_rivet()
        if self.game.reflex.connected_rivet() == 0:
            #Worst position for reflex - requires mixer1 to be in the three liberal positions for the connection of the wires bypassing the reflex.
            if (mix1 in [1,3]):
                if self.game.mixer4.position in [1,3,4]:
                    self.game.extra_ball.step()
                if self.game.spotting.position == 25 and self.game.mixer1.position == 4:
                    self.step_eb(15 - self.game.extra_ball.position)
                if self.game.spotting.position == 8:
                    self.step_eb(10 - self.game.extra_ball.position)
                if self.game.spotting.position == 0:
                    self.step_eb(5 - self.game.extra_ball.position)
        elif self.game.reflex.connected_rivet() == 1 and (mix1 in [1,3,21]):
            if self.game.mixer4.position in [1,3,4]:
                self.game.extra_ball.step()
            if self.game.spotting.position == 25 and self.game.mixer1.position == 4:
                self.step_eb(15 - self.game.extra_ball.position)
            if self.game.spotting.position == 8:
                self.step_eb(10 - self.game.extra_ball.position)
            if self.game.spotting.position == 0:
                self.step_eb(5 - self.game.extra_ball.position)
        elif self.game.reflex.connected_rivet() == 2 and (mix1 in [1,3,21,6]):
            if self.game.mixer4.position in [1,3,4]:
                self.game.extra_ball.step()
            if self.game.spotting.position == 25 and self.game.mixer1.position == 4:
                self.step_eb(15 - self.game.extra_ball.position)
            if self.game.spotting.position == 8:
                self.step_eb(10 - self.game.extra_ball.position)
            if self.game.spotting.position == 0:
                self.step_eb(5 - self.game.extra_ball.position)
        elif self.game.reflex.connected_rivet() == 3 and (mix1 in [1,3,21,6,20]):
            if self.game.mixer4.position in [1,3,4]:
                self.game.extra_ball.step()
            if self.game.spotting.position == 25 and self.game.mixer1.position == 4:
                self.step_eb(15 - self.game.extra_ball.position)
            if self.game.spotting.position == 8:
                self.step_eb(10 - self.game.extra_ball.position)
            if self.game.spotting.position == 0:
                self.step_eb(5 - self.game.extra_ball.position)
        elif self.game.reflex.connected_rivet() == 4 and (mix1 in [1,3,21,6,20,5]):
            if self.game.mixer4.position in [1,3,4]:
                self.game.extra_ball.step()
            if self.game.spotting.position == 25 and self.game.mixer1.position == 4:
                self.step_eb(15 - self.game.extra_ball.position)
            if self.game.spotting.position == 8:
                self.step_eb(10 - self.game.extra_ball.position)
            if self.game.spotting.position == 0:
                self.step_eb(5 - self.game.extra_ball.position)
        elif self.game.reflex.connected_rivet() == 5:
            if self.game.mixer4.position in [1,3,4]:
                self.game.extra_ball.step()
            if self.game.spotting.position == 25 and self.game.mixer1.position == 4:
                self.step_eb(15 - self.game.extra_ball.position)
            if self.game.spotting.position == 8:
                self.step_eb(10 - self.game.extra_ball.position)
            if self.game.spotting.position == 0:
                self.step_eb(5 - self.game.extra_ball.position)
        
            
        self.check_lifter_status()
        self.delay(name="display", delay=0, handler=graphics.serenade.display, param=self)
            
    def step_eb(self, number):
        if number > 0:
            number -= 1
            self.game.extra_ball.step()
            self.delay(name="display", delay=0, handler=graphics.serenade.display, param=self)
            self.check_lifter_status()
            self.delay(name="step_eb", delay=0.1, handler=self.step_eb, param=number)
            if self.game.extra_ball.position >= 9:
                self.check_lifter_status()

    def step_odds(self, number):
        if number > 0:
            number -= 1
            self.game.odds.step()
            self.delay(name="display", delay=0, handler=graphics.serenade.display, param=self)
            self.check_lifter_status()
            self.delay(name="step_odds", delay=0.1, handler=self.step_odds, param=number)
        else:
            self.search()

    def step_selection(self, number):
        if number > 0:
            number -= 1
            self.game.selection_feature.step()
            self.check_spot()
            if self.game.selection_feature.position >= 4:
                self.game.select_spots.engage(self.game)
            self.delay(name="display", delay=0, handler=graphics.serenade.display, param=self)
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
        self.delay(name="display", delay=0.1, handler=graphics.serenade.display, param=self)

    def animate_both(self, args):
        start = args[0]
        diff = args[1]
        num = args[2]
        if start + num >= 50:
            start = 0
        if diff >= 0:
            num = num + 1
            graphics.serenade.both_animation([self, start + num])
            self.cancel_delayed(name="display")
            diff = diff - 1
            args = [start,diff,num]
            self.delay(name="both_animation", delay=0.08, handler=self.animate_both, param=args)
        else:
            self.cancel_delayed(name="both_animation")
            self.delay(name="display", delay=0.1, handler=graphics.serenade.display, param=self)
            self.scan_all()

    def animate_eb_scan(self, args):
        start = args[0]
        diff = args[1]
        num = args[2]
        if start + num >= 50:
            start = 0
        if diff >= 0:
            num = num + 1
            graphics.serenade.eb_animation([self, start + num])
            self.cancel_delayed(name="display")
            diff = diff - 1
            args = [start,diff,num]
            self.delay(name="eb_animation", delay=0.08, handler=self.animate_eb_scan, param=args)
        else:
            self.cancel_delayed(name="eb_animation")
            self.delay(name="display", delay=0.1, handler=graphics.serenade.display, param=self)
            self.scan_eb()


    # Define reset as the knock-off, anti-cheat relay disabled, and replay reset enabled.  Motors turn while credits are knocked off.
    # When meter reaches zero and the zero limit switch is hit, turn off motor sound and leave backglass gi on, but with tilt displayed.

    def startup(self):        
        # Every bingo requires the meter to register '0' 
        # before allowing coin entry --
        # also needs to show a plain 'off' backglass.
        self.eb = False
        self.tilt_actions()

class Serenade(procgame.game.BasicGame):
    def __init__(self, machine_type):
        super(Serenade, self).__init__(machine_type)
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

        #Odds stepper
        self.odds = units.Stepper("odds", 8, 'serenade')
        
        #Replay Counter
        self.card1_replay_counter = units.Stepper("card1_replay_counter", 300)
        self.card2_replay_counter = units.Stepper("card1_replay_counter", 300)
 
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

        self.e_card = units.Relay("e_card")

        #When engage()d, light 6v circuit, and enable game features, scoring,
        #etc. Disengage()d means that the machine is 'soft' tilted. In United
        #games, they call this the lock relay, similar to many other pin
        #manufacturers.
        self.lock = units.Relay("lock")

        self.eb_play = units.Relay("eb_play")
        
        #Relay for corners lighting
        self.corners1 = units.Relay("corners1")
        self.corners2 = units.Relay("corners2")

        self.selector = units.Stepper("selector", 2)

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
        self.selection_feature = units.Stepper("selection_feature", 10)
        self.select_spots = units.Relay("select_spots")
        self.spotted = units.Stepper("spotted", 10, "serenade", "continuous")

        #Some special trip relays for spotted numbers and rollovers
        self.red_star = units.Relay("red_star")
        self.yellow_star = units.Relay("yellow_star")

        self.before_fourth = units.Relay("before_fourth")
        self.before_fifth = units.Relay("before_fifth")
       
        self.name = units.Stepper("name", 10)
        self.name.position = 1

        self.selection_feature_relay = units.Relay("selection_feature_relay")

        self.lite_a_name = units.Relay("lite_a_name")

        self.anti_cheat = units.Relay("anti_cheat")

        self.replays = 0
        self.returned = False

    def reset(self):
        super(Serenade, self).reset()
        self.logger = logging.getLogger('game')
        self.load_config('bingo.yaml')
        self.lock.engage(game)
        
        main_mode = MulticardBingo(self)
        self.modes.add(main_mode)
        

game = Serenade(machine_type='pdb')
game.reset()
game.run_loop()
