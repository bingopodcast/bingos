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
from bingo_emulator.graphics.hi_fi import *

class SinglecardBingo(procgame.game.Mode):
    def __init__(self, game):
        super(SinglecardBingo, self).__init__(game=game, priority=5)
        self.holes = []
        self.startup()
        self.game.sound.register_music('motor', "audio/other_motor.wav")
        self.game.sound.register_music('search', "audio/six_card_search_old.wav")
        self.game.sound.register_sound('add', "audio/six_card_add_card.wav")
        self.game.sound.register_sound('tilt', "audio/tilt.wav")
        self.game.sound.register_sound('step', "audio/step.wav")
        self.game.sound.register_sound('eb_search', "audio/EB_Search.wav")

    def sw_coin_active(self, sw):
        if self.game.eb_play.status == False:
            self.game.tilt.disengage()
            self.regular_play()
            self.scan_all()
        else:
            self.game.sound.stop('add')
            self.game.sound.play('add')
            self.game.cu = not self.game.cu
            self.game.spotting.spin()
            self.game.mixer1.spin()
            self.game.mixer2.spin()
            self.game.mixer3.spin()
            self.game.mixer4.spin()
            self.scan_eb()
            self.replay_step_down()
            self.game.reflex.decrease()

        self.delay(name="display", delay=0.1, handler=graphics.hi_fi.display, param=self)

    def sw_startButton_active(self, sw):
        self.game.eb_play.disengage()
        if self.game.replays > 0 or self.game.switches.freeplay.is_active():
            self.game.sound.stop('add')
            self.game.sound.play('add')
            self.game.tilt.disengage()
            self.regular_play()
            self.scan_all()
            self.delay(name="display", delay=0.1, handler=graphics.hi_fi.display, param=self)

    def sw_enter_active(self, sw):
        if self.game.switches.left.is_active() and self.game.switches.right.is_active():
            self.game.end_run_loop()
            os.system("/home/nbaldridge/proc/bingo_emulator/start_game.sh hi_fi")        
        else:
            if self.game.bump_feature.position >= 5:
                if self.game.delay.status == False:
                    self.game.coils.bump.pulse()
                    self.game.bump_feature.stepdown()
                    graphics.hi_fi.display(self)
                    self.game.delay.engage(self.game)
                    self.delay(name="delay", delay=2, handler=self.bump_delay)

    def bump_delay(self):
        self.game.delay.disengage()

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
            if self.game.ball_count.position >= 5:
                self.game.returned = True
            self.game.ball_count.position -= 1
            self.check_lifter_status()
        else:
            self.check_lifter_status()

    def check_spot(self):
        if self.game.spotted_numbers.position >= 5:
            if self.game.spotted.position == 0:
                if 19 not in self.holes:
                    self.holes.append(19)
        if self.game.spotted_numbers.position >= 6:
            if self.game.spotted.position == 1:
                if 20 not in self.holes:
                    self.holes.append(20)
        if self.game.spotted_numbers.position >= 7:
            if self.game.spotted.position == 2:
                if 21 not in self.holes:
                    self.holes.append(21)
        if self.game.spotted_numbers.position >= 8:
            if self.game.spotted.position == 3:
                if 22 not in self.holes:
                    self.holes.append(22)
        if self.game.spotted_numbers.position >= 9:
            if self.game.spotted.position == 4:
                if 16 not in self.holes:
                    self.holes.append(16)
        if self.game.spotted_numbers.position >= 10:
            if self.game.spotted.position == 5:
                if 25 not in self.holes:
                    self.holes.append(25)
        if self.game.spotted_numbers.position >= 11:
            if self.game.spotted.position == 6:
                if 10 not in self.holes:
                    self.holes.append(10)
        self.delay(name="display", delay=0.1, handler=graphics.hi_fi.display, param=self)


    def sw_left_active(self, sw):
        max_ball = 4
        if self.game.before_fifth.status == True:
            max_ball = 5

        if self.game.spotted_numbers.position > 4:
            if self.game.ball_count.position < max_ball:
                self.game.spotted.stepdown()
                #Initial spotted selection - 2 numbers
                if self.game.spotted_numbers.position == 8:
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
                #five numbers available
                elif self.game.spotted_numbers.position == 9:
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
                        if 16 not in self.holes:
                            self.holes.append(16)
                    else:
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
                        if 10 in self.holes:
                            if self.game.switches.hole10.is_inactive():
                                self.holes.remove(10)
                #six positions
                elif self.game.spotted_numbers.position == 10:
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
                        if 16 not in self.holes:
                            self.holes.append(16)
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
                # And seven numbers
                elif self.game.spotted_numbers.position == 11: 
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
                        if 16 not in self.holes:
                            self.holes.append(16)
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
                        if 10 in self.holes:
                            if self.game.switches.hole10.is_inactive():
                                self.holes.remove(10)
                        if 25 not in self.holes:
                            self.holes.append(25)
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

        self.delay(name="display", delay=0.1, handler=graphics.hi_fi.display, param=self)

    def sw_right_active(self, sw):
        max_ball = 4
        if self.game.before_fifth.status == True:
            max_ball = 5

        if self.game.spotted_numbers.position > 4:
            if self.game.ball_count.position < max_ball:
                self.game.spotted.step()
                #Initial spotted selection - 2 numbers
                if self.game.spotted_numbers.position == 8:
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
                #five numbers available
                elif self.game.spotted_numbers.position == 9:
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
                        if 16 not in self.holes:
                            self.holes.append(16)
                    else:
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
                        if 10 in self.holes:
                            if self.game.switches.hole10.is_inactive():
                                self.holes.remove(10)
                #six positions
                elif self.game.spotted_numbers.position == 10:
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
                        if 16 not in self.holes:
                            self.holes.append(16)
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
                # And seven numbers
                elif self.game.spotted_numbers.position == 11: 
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
                        if 16 not in self.holes:
                            self.holes.append(16)
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
                        if 10 in self.holes:
                            if self.game.switches.hole10.is_inactive():
                                self.holes.remove(10)
                        if 25 not in self.holes:
                            self.holes.append(25)
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

        self.delay(name="display", delay=0.1, handler=graphics.hi_fi.display, param=self)

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
        self.cancel_delayed(name="card1_replay_step_up")
        self.cancel_delayed(name="corners_replay_step_up")
        self.cancel_delayed(name="blink")
        self.cancel_delayed(name="timeout")
        self.game.search_index.disengage()
        self.game.coils.counter.pulse()
        self.game.cu = not self.game.cu
        self.game.spotting.spin()
        self.game.mixer1.spin()
        self.game.mixer2.spin()
        self.game.mixer3.spin()
        self.game.mixer4.spin()
        self.game.reflex.decrease()
        self.game.sound.play_music('motor', -1)

        self.game.returned = False
        if self.game.start.status == True:
            if self.game.selector.position < 2:
                self.game.selector.step()
            if self.game.switches.shutter.is_inactive():
                self.game.coils.shutter.enable()
            self.replay_step_down()
            self.check_lifter_status()
        else:
            self.holes = []
            self.game.start.engage(self.game)
            self.game.coils.redROLamp.disable()
            self.game.coils.yellowROLamp.disable()
            self.game.card1_replay_counter.reset()
            self.game.super_card.reset()
            self.game.spotted_numbers.reset()
            self.game.bump_feature.reset()
            self.game.corners.disengage()
            self.game.corners_replay_counter.reset()
            self.game.start.engage(self.game)
            self.game.selector.reset()
            self.game.ball_count.reset()
            self.game.extra_ball.reset()
            self.game.red_rollover.disengage()
            self.game.yellow_rollover.disengage()
            self.game.odds.reset()
            self.game.timer.reset()
            self.game.before_fourth.disengage()
            self.game.before_fifth.disengage()
            self.game.before_fourth.engage(self.game)
            self.game.sound.play_music('motor', -1)
            self.regular_play()
        self.delay(name="display", delay=0.1, handler=graphics.hi_fi.display, param=self)
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
                            if self.game.extra_ball.position >= 3 and self.game.ball_count.position <= 5:
                                if self.game.switches.shooter.is_open() and self.game.switches.trough3.is_closed():
                                    self.game.coils.lifter.enable()
                        if self.game.switches.trough3.is_open():
                            if self.game.extra_ball.position >= 6 and self.game.ball_count.position <= 6:
                                if self.game.switches.shooter.is_open() and self.game.switches.trough2.is_closed():
                                    self.game.coils.lifter.enable()
                        if self.game.switches.trough2.is_inactive() and self.game.ball_count.position <= 7:
                            if self.game.ball_count.position <= 7:
                                if self.game.extra_ball.position >= 9:
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
                if self.game.ball_count.position == 5 and self.game.extra_ball.position >= 3:
                    self.game.coils.lifter.enable()
                if self.game.ball_count.position == 6 and self.game.extra_ball.position >= 6:
                    self.game.coils.lifter.enable()
                if self.game.ball_count.position == 7 and self.game.extra_ball.position >= 9:
                    self.game.coils.lifter.enable()

    def sw_gate_inactive_for_1ms(self, sw):
        self.game.start.disengage()
        self.game.ball_count.step()
        if self.game.switches.shutter.is_active():
            self.game.coils.shutter.enable()
        if self.game.ball_count.position >= 5:
            if self.game.search_index.status == False:
                self.search()
        if self.game.ball_count.position > 5:
            self.game.coils.yellowROLamp.disable()
            self.game.coils.redROLamp.disable()
        if self.game.ball_count.position <= 7:
            self.check_lifter_status()
        self.delay(name="display", delay=0.1, handler=graphics.hi_fi.display, param=self)


    # This is really nasty, but it is how we render graphics for each individual hole.
    # numbers are added (or removed from) a list.  In this way, I can re-use the same
    # routine even for games where there are ball return functions like Surf Club.

    def sw_hole1_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(1)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.hi_fi.display, param=self)

    def sw_hole2_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(2)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.hi_fi.display, param=self)

    def sw_hole3_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(3)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.hi_fi.display, param=self)

    def sw_hole4_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(4)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.hi_fi.display, param=self)

    def sw_hole5_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(5)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.hi_fi.display, param=self)

    def sw_hole6_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(6)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.hi_fi.display, param=self)

    def sw_hole7_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(7)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.hi_fi.display, param=self)

    def sw_hole8_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(8)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.hi_fi.display, param=self)

    def sw_hole9_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(9)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.hi_fi.display, param=self)

    def sw_hole10_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(10)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.hi_fi.display, param=self)

    def sw_hole11_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(11)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.hi_fi.display, param=self)

    def sw_hole12_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(12)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.hi_fi.display, param=self)

    def sw_hole13_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(13)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.hi_fi.display, param=self)

    def sw_hole14_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(14)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.hi_fi.display, param=self)

    def sw_hole15_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(15)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.hi_fi.display, param=self)

    def sw_hole16_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(16)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.hi_fi.display, param=self)

    def sw_hole17_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(17)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.hi_fi.display, param=self)

    def sw_hole18_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(18)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.hi_fi.display, param=self)

    def sw_hole19_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(19)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.hi_fi.display, param=self)

    def sw_hole20_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(20)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.hi_fi.display, param=self)

    def sw_hole21_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(21)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.hi_fi.display, param=self)

    def sw_hole22_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(22)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.hi_fi.display, param=self)

    def sw_hole23_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(23)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.hi_fi.display, param=self)

    def sw_hole24_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(24)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.hi_fi.display, param=self)

    def sw_hole25_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(25)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.hi_fi.display, param=self)

    def sw_replayReset_active(self, sw):
        self.game.anti_cheat.disengage()
        self.holes = []
        graphics.hi_fi.display(self)
        self.tilt_actions()
        self.replay_step_down(self.game.replays)

    def tilt_actions(self):
        self.game.start.disengage()
        self.cancel_delayed(name="replay_reset")
        self.cancel_delayed(name="card1_replay_step_up")
        self.cancel_delayed(name="corners_replay_step_up")
        self.cancel_delayed(name="blink")
        self.cancel_delayed(name="timeout")
        self.game.coils.redROLamp.disable()
        self.game.coils.yellowROLamp.disable()
        self.game.search_index.disengage()
        if self.game.ball_count.position == 0:
            if self.game.switches.shutter.is_active():
                self.game.coils.shutter.enable()
        self.game.card1_replay_counter.reset()
        self.game.super_card.reset()
        self.game.spotted_numbers.reset()
        self.game.bump_feature.reset()
        self.game.red_rollover.disengage()
        self.game.yellow_rollover.disengage()
        self.game.corners.disengage()
        self.game.corners_replay_counter.reset()
        self.game.start.engage(self.game)
        self.game.selector.reset()
        self.game.ball_count.reset()
        self.game.extra_ball.reset()
        self.game.odds.reset()
        self.game.timer.reset()
        self.game.before_fourth.disengage()
        self.game.before_fifth.disengage()
        self.holes = []
        self.game.ball_count.reset()
        self.game.odds.reset()
        self.game.eb_play.disengage()
        self.game.extra_ball.reset()
        self.game.anti_cheat.engage(game)
        self.game.tilt.engage(self.game)
        self.game.before_fourth.engage(self.game)
        self.game.sound.stop_music()
        self.game.sound.play('tilt')
        # displays "Tilt" on the backglass, you have to recoin.
        self.delay(name="display", delay=0.1, handler=graphics.hi_fi.display, param=self)

    def sw_tilt_active(self, sw):
        if self.game.tilt.status == False:
            if self.game.delay.status == False:
                self.tilt_actions()

    def replay_step_down(self, number=0):
        if number > 0:
            if number > 1:
                self.game.replays -= 1
                graphics.replay_step_down(self.game.replays, graphics.hi_fi.reel1, graphics.hi_fi.reel10, graphics.hi_fi.reel100)
                self.game.coils.registerDown.pulse()
                number -= 1
                graphics.hi_fi.display(self)
                self.delay(name="replay_reset", delay=0.13, handler=self.replay_step_down, param=number)
            elif number == 1:
                self.game.replays -= 1
                graphics.replay_step_down(self.game.replays, graphics.hi_fi.reel1, graphics.hi_fi.reel10, graphics.hi_fi.reel100)
                self.game.coils.registerDown.pulse()
                number -= 1
                graphics.hi_fi.display(self)
                self.cancel_delayed(name="replay_reset")
        else: 
            if self.game.replays > 0:
                self.game.replays -= 1
                graphics.replay_step_down(self.game.replays, graphics.hi_fi.reel1, graphics.hi_fi.reel10, graphics.hi_fi.reel100)
                self.delay(name="display", delay=0.1, handler=graphics.hi_fi.display, param=self)
            self.game.coils.registerDown.pulse()

    def replay_step_up(self):
        if self.game.replays < 899:
            self.game.replays += 1
            graphics.replay_step_up(self.game.replays, graphics.hi_fi.reel1, graphics.hi_fi.reel10, graphics.hi_fi.reel100)
        self.game.coils.registerUp.pulse()
        self.game.coils.sounder.pulse()
        self.game.reflex.increase()
        graphics.hi_fi.display(self)

    def sw_redstar_active(self, sw):
        if self.game.red_rollover.status == True:
            if 2 not in self.holes:
                self.holes.append(2)
            if 5 not in self.holes:
                self.holes.append(5)
            if 8 not in self.holes:
                self.holes.append(8)
            self.game.coils.yellowROLamp.disable()
            self.game.coils.redROLamp.disable()
            self.game.red_rollover.disengage()
            self.game.yellow_rollover.disengage()
        self.delay(name="display", delay=0.1, handler=graphics.hi_fi.display, param=self)

    def sw_yellowstar_active(self, sw):
        if self.game.yellow_rollover.status == True:
            if 2 not in self.holes:
                self.holes.append(2)
            if 5 not in self.holes:
                self.holes.append(5)
            if 8 not in self.holes:
                self.holes.append(8)
            self.game.coils.yellowROLamp.disable()
            self.game.coils.redROLamp.disable()
            self.game.red_rollover.disengage()
            self.game.yellow_rollover.disengage()
        self.delay(name="display", delay=0.1, handler=graphics.hi_fi.display, param=self)

    def sw_yellow_active(self, sw):
        if self.game.ball_count.position >= 5:
            if self.game.eb_play.status == False:
                self.game.spotting.spin()
                self.game.mixer1.spin()
                self.game.mixer2.spin()
                self.game.mixer3.spin()
                self.game.mixer4.spin()
                self.game.eb_play.engage(self.game)
                self.delay(name="display", delay=0.1, handler=graphics.hi_fi.display, param=self)
                self.sw_yellow_active(sw)
            if self.game.eb_play.status == True and (self.game.replays > 0 or self.game.switches.freeplay.is_active()):
                self.game.sound.stop('add')
                self.game.sound.play('add')
                self.game.cu = not self.game.cu
                self.game.spotting.spin()
                self.game.mixer1.spin()
                self.game.mixer2.spin()
                self.game.mixer3.spin()
                self.game.mixer4.spin()
                self.scan_eb()
                self.replay_step_down()
                self.game.reflex.decrease()
                self.delay(name="display", delay=0.1, handler=graphics.hi_fi.display, param=self)
                self.game.eb_play.disengage()
                self.delay(name="display", delay=0.1, handler=graphics.hi_fi.display, param=self)

            
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
        self.game.sound.stop_music()
        self.game.sound.play_music('search', -1)
        
        for i in range(0, 50):
            self.r = self.closed_search_relays(self.game.searchdisc.position, self.game.corners.status)
            self.game.searchdisc.spin()
            self.wipers = self.r[0]
            self.card = self.r[1]
            self.corners = self.r[2]
            self.supercard = self.r[3]

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
                            if s >= 3:
                                self.find_winner(s, self.card, self.corners, self.supercard)
                                break

    def find_winner(self, relays, card, corners, supercard):
        if self.game.search_index.status == False and self.game.replays < 899:
            if self.game.odds.position == 1:
                threeodds = 4
                fourodds = 16
                fiveodds = 96
            elif self.game.odds.position == 2:
                threeodds = 6
                fourodds = 20
                fiveodds = 96
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
                fourodds = 100
                fiveodds = 192
            elif self.game.odds.position == 8:
                threeodds = 64
                fourodds = 200
                fiveodds = 300

            if card == 1:
                if relays == 3:
                    if supercard == 1:
                        if self.game.super_card.position >= 4:
                            if self.game.card1_replay_counter.position < fourodds:
                                self.game.search_index.engage(self.game)
                                self.card1_replay_step_up(fourodds - self.game.card1_replay_counter.position)
                    elif supercard == 2:
                        if self.game.super_card.position >= 8:
                            if self.game.card1_replay_counter.position < fourodds:
                                self.game.search_index.engage(self.game)
                                self.card1_replay_step_up(fourodds - self.game.card1_replay_counter.position)
                    else:
                        if not corners:
                            if self.game.card1_replay_counter.position < threeodds:
                                self.game.search_index.engage(self.game)
                                self.card1_replay_step_up(threeodds - self.game.card1_replay_counter.position)
                if relays == 4:
                    if corners and self.game.corners.status == True:
                        if supercard == 1:
                            if self.game.super_card.position >= 4:
                                if self.game.corners_replay_counter.position < 200:
                                    self.game.search_index.engage(self.game)
                                    self.corners_replay_step_up(200 - self.game.corners_replay_counter.position)
                        elif supercard == 2:
                            if self.game.super_card.position >= 8:
                                if self.game.corners_replay_counter.position < 200:
                                    self.game.search_index.engage(self.game)
                                    self.corners_replay_step_up(200 - self.game.corners_replay_counter.position)
                        else:
                            if self.game.corners_replay_counter.position < 200:
                                self.game.search_index.engage(self.game)
                                self.corners_replay_step_up(200 - self.game.corners_replay_counter.position)
                                self.game.regular_corners.engage(self.game)
                    else:
                        if not corners:
                            if self.game.card1_replay_counter.position < fourodds:
                                self.game.search_index.engage(self.game)
                                self.card1_replay_step_up(fourodds - self.game.card1_replay_counter.position)
                if relays == 5:
                    if self.game.card1_replay_counter.position < fiveodds:
                        self.game.search_index.engage(self.game)
                        self.card1_replay_step_up(fiveodds - self.game.card1_replay_counter.position)


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
        self.pos[0] = {}
        self.pos[1] = {9:1, 4:2, 15:3, 24:4, 6:5}
        self.pos[2] = {10:1, 19:2, 14:3, 20:4, 8:5}
        self.pos[3] = {2:1, 18:2, 16:3, 12:4, 25:5}
        self.pos[4] = {1:1, 22:2, 13:3, 21:4, 17:5}
        self.pos[5] = {11:1, 7:2, 5:3, 23:4, 3:5}
        self.pos[6] = {9:1, 10:2, 2:3, 1:4, 11:5}
        self.pos[7] = {4:1, 19:2, 18:3, 22:4, 7:5}
        self.pos[8] = {15:1, 14:2, 16:3, 13:4, 5:5}
        self.pos[9] = {24:1, 20:2, 12:3, 21:4, 23:5}
        self.pos[10] = {6:1, 8:2, 25:3, 17:4, 3:5}
        self.pos[11] = {9:1, 19:2, 16:3, 21:4, 3:5}
        self.pos[12] = {6:1, 20:2, 16:3, 22:4, 11:5}
        self.pos[13] = {}
        self.pos[14] = {23:1, 3:2, 18:3}
        self.pos[15] = {9:1, 25:2, 11:3}
        self.pos[16] = {12:1, 24:2, 14:3}
        self.pos[17] = {23:1, 9:2, 12:3}
        self.pos[18] = {3:1, 25:2, 24:3}
        self.pos[19] = {18:1, 11:2, 14:3}
        self.pos[20] = {23:1, 25:2, 14:3}
        self.pos[21] = {18:1, 25:2, 12:3}
        self.pos[22] = {}
        self.pos[23] = {15:1, 7:2, 11:3}
        self.pos[24] = {1:1, 10:2, 13:3}
        self.pos[25] = {17:1, 4:2, 18:3}
        self.pos[26] = {15:1, 1:2, 17:3}
        self.pos[27] = {7:1, 10:2, 4:3}
        self.pos[28] = {11:1, 13:2, 18:3}
        self.pos[29] = {15:1, 10:2, 18:3}
        self.pos[30] = {11:1, 10:2, 17:3}
        self.pos[31] = {}
        self.pos[32] = {9:1, 6:2, 11:3, 3:4}
        self.pos[33] = {}
        self.pos[34] = {}
        self.pos[35] = {23:1, 18:2, 12:3, 14:4}
        self.pos[36] = {}
        self.pos[37] = {15:1, 11:2, 17:3, 18:4}
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
        sc = 0
        card = 1

        if rivets == 32:
            corners = True
        if rivets in range(14,22):
            sc = 1
        if rivets in range(23,31):
            sc = 2

        if rivets == 35:
            sc = 1
            corners = True
        if rivets == 37:
            sc = 2
            corners = True

        return (self.pos[rivets], card, corners, sc)
    
    def scan_all(self):
        #Animate scanning of everything - this happens through the spotting disc
        self.all_probability()

    def all_probability(self):
        mix1 = self.game.mixer1.connected_rivet()
        if self.game.reflex.connected_rivet() == 0 and (mix1 in [1,6,8,11,13,16,18,22,24]):
            self.scan_odds()
            self.scan_features()
        elif self.game.reflex.connected_rivet() == 1 and (mix1 not in [2,5,7,9,12,14,15,19,23]):
            self.scan_odds()
            self.scan_features()
        elif self.game.reflex.connected_rivet() == 2 and (mix1 not in [5,9,12,15,19,23]):
            self.scan_odds()
            self.scan_features()
        elif self.game.reflex.connected_rivet() == 3 and (mix1 not in [5,9,15,23]):
            self.scan_odds()
            self.scan_features()
        elif self.game.reflex.connected_rivet() == 4:
            self.scan_odds()
            self.scan_features()
        else:
            #s = random.randint(1,5)
            #self.animate_odds_scan(s)
            s = random.randint(1,6)
            self.animate_feature_scan(s)

    def scan_odds(self):
        #s = random.randint(1,5)
        #self.animate_odds_scan(s)
        p = self.odds_probability()
        if p == 1:
            es = self.check_extra_step()
            if es == 1:
                i = random.randint(1,3)
                self.extra_step(i)
            else:
                self.game.odds.step()

    def extra_step(self, number):
        if number > 0:
            self.game.odds.step()
            self.delay(name="display", delay=0, handler=graphics.hi_fi.display, param=self)
            number -= 1
            self.delay(name="extra_step", delay=0.1, handler=self.extra_step, param=number)

    def check_extra_step(self):
        i = random.randint(0,32)
        if i == 16:
            if self.game.cu:
                return 1
        else:
            return 0

    def odds_probability(self):
        # Check position of Mixer 5, Mixer 4, and Mixer 3 and current 
        # position of the odds, along with trip relays.
        # For first check, guaranteed single stepup.  Probability doesn't 
        # factor, so I will return as part of the initial check above.
        sd = self.game.spotting.position
        if self.game.odds.position <= 3:
            return 1
        else:
            m4 = self.check_mixer4()
            m3 = self.check_mixer3()
            if m4:
                if m3:
                    if self.game.odds.position == 4:
                        if sd in [1,6,9,11,19,24,28,40,44,48]:
                            return 1
                    elif self.game.odds.position == 5:
                        if sd in [0,5,14,16,17,20,26,27,31,32,33,34,37,38,39,41,43,46,47]:
                            return 1
                    elif self.game.odds.position == 6:
                        if sd in [10,15,25,36]:
                            return 1
                    elif self.game.odds.position == 7:
                        if sd in [2,8,13,23,35,49]:
                            return 1
                else:
                    return 0
            else:
                return 0

    def check_mixer4(self):
        i = random.randint(0,32)
        if i % 8 == 0:
            return 1
        else:
            return 0


    def check_mixer3(self):
        mix3 = self.game.mixer3.connected_rivet()
        if self.game.super_card.position < 8 and self.game.spotted_numbers.position < 4:
            if mix3 == 10 or mix3 == 21 or mix3 == 24 or mix3 == 23:
                return 1
        if self.game.super_card.position < 1 and self.game.spotted_numbers.position < 4:
            if mix3 in [6,12,13]:
                return 1
        if mix3 in [1,2,3,4]:
            return 1
        if self.game.bump_feature.position <= 7:
            if mix3 in [5,10,11]:
                return 1
        if mix3 == 6:
            if self.game.spotted_numbers.position < 11:
                return 1
        if mix3 == 15:
            if self.game.spotted_numbers.position < 13:
                return 1
        if mix3 == 18:
            if self.game.spotted_numbers.position < 12:
                return 1
        return 0

    def scan_features(self):
        p = self.features_probability()

    def features_probability(self):
        s = random.randint(1,6)
        self.animate_feature_scan(s)
        mix2 = self.game.mixer2.connected_rivet()
        mix3 = self.game.mixer3.connected_rivet()
        if self.game.odds.position <= 3:
            self.features_spotting()
        elif (self.game.odds.position == 4 or self.game.odds.position == 5) and mix2 == 23:
            self.features_spotting()
        elif (self.game.odds.position == 6 or self.game.odds.position == 7) and mix2 == 22:
            self.features_spotting()
        elif (self.game.odds.position == 8 or self.game.odds.position == 9) and mix2 == 12:
            self.features_spotting()

    def step_super(self, number):
        if number >= 1:
            self.game.super_card.step()
            number -= 1
            self.delay(name="display", delay=0.1, handler=graphics.hi_fi.display, param=self)
            self.delay(name="step_super_card", delay=0.1, handler=self.step_super, param=number)

    def step_bump(self, number):
        if number >= 1:
            self.game.bump_feature.step()
            number -= 1
            if self.game.bump_feature.position == 4:
                number = 4
            self.delay(name="display", delay=0.1, handler=graphics.hi_fi.display, param=self)
            self.delay(name="step_bump_card", delay=0.1, handler=self.step_bump, param=number)


    def features_spotting(self):
        sd = self.game.spotting.position
        if self.game.cu and self.game.super_card.position < 7:
            self.step_super(1)
        if self.game.cu:
            if self.game.bump_feature.position < 3:
                self.step_bump(1)
        if self.game.bump_feature.position >= 3:
            if sd in [6,17]:
                self.step_bump(10)
            else:
                if self.game.bump_feature.position < 7:
                    if sd in [3,5,8,9,11,14,18,22,23,24,27,31,34,37,43]:
                        self.step_bump(1)
        if self.game.bump_feature.position >= 7:
            if sd in [7,12,15,29,42,45]:
                self.step_bump(1)
        if self.game.super_card.position == 7:
            if sd in [3,13,35,49]:
                self.step_super(1)
        if sd in [2,44] and self.game.super_card.position < 4:
            self.step_super(4 - self.game.super_card.position)
        if sd in [9,24,28,40,48]:
            self.step_super(8)
        if sd in [29,46]:
            self.game.corners.engage(self.game)
        if sd in [6,12,16]:
            self.game.yellow_rollover.engage(self.game)
            self.game.coils.redROLamp.enable()
        if self.game.red_rollover.status == False:
            if sd in [18,19,34,39,43]:
                self.game.yellow_rollover.engage(self.game)
                self.game.coils.redROLamp.enable()
        if sd in [3,14,36]:
            self.game.red_rollover.engage(self.game)
            self.game.coils.yellowROLamp.enable()
        if self.game.yellow_rollover.status == False:
            if sd in [11,28,42,45,48,49]:
                self.game.red_rollover.engage(self.game)
                self.game.coils.yellowROLamp.enable()
        if sd in [0,1,5,9,24,26,30,33,40,46]:
            self.game.before_fourth.disengage()
            self.game.before_fifth.engage(self.game)
        # CHECK SPOTTED NUMBERS
        if self.game.reflex.connected_rivet() <= 4:
            if sd in [17,43]:
                self.step_spotted_numbers(3 - self.game.spotted_numbers.position)
                self.check_spot()
        if sd in [5,14,20,26,37,39]:
            self.step_spotted_numbers(3 - self.game.spotted_numbers.position)
            self.check_spot()
        m4 = self.check_mixer4()
        if m4 == 1:
            if self.game.spotted_numbers.position >= 4:
                self.step_spotted_numbers(9 - self.game.spotted_numbers.position)
                self.check_spot()
        if sd in [0,32,33,38,41,46]:
            if self.game.spotted_numbers.position >= 9:
                self.step_spotted_numbers(1)
                self.check_spot()
        if not self.game.cu:
            if self.game.spotted_numbers.position < 3:
                self.game.spotted_numbers.step()
                self.check_spot()
        
    def step_spotted_numbers(self, number):
            if number >= 1:
                self.game.spotted_numbers.step()
                self.check_spot()
                number -= 1
                if self.game.spotted_numbers.position == 4:
                    number = 4
                self.delay(name="display", delay=0.1, handler=graphics.hi_fi.display, param=self)
                self.delay(name="step_spotted_numbers", delay=0.1, handler=self.step_spotted_numbers, param=number)

    def scan_eb(self):
        s = random.randint(1,9)
        self.animate_eb_scan(s)
        if self.game.extra_ball.position == 0:
            self.game.extra_ball.step()
            self.check_lifter_status()
        p = self.eb_probability()
        if p == 1:
            es = self.check_extra_step()
            if es == 1:
                i = random.randint(1,6)
                self.step_eb(i)
            else:
                self.game.extra_ball.step()
                self.check_lifter_status()

        # Timer resets to 0 position on ball count increasing.  We are fudging this since we will have
        # no good way to measure balls as they return back to the trough.  The ball count unit cannot be
        # relied upon as we do not have a switch in the outhole, and the trough logic is too complex for
        # the task at hand.
        # TODO: implement thunk noises into the units.py to automatically play the noises.
        self.game.timer.reset()
        self.delay(name="display", delay=0.1, handler=graphics.hi_fi.display, param=self)

    def animate_odds_scan(self, s):
        if s > 1:
            self.delay(name="odds_animation", delay=0, handler=graphics.hi_fi.odds_animation, param=s)
            self.delay(name="display", delay=0.1, handler=graphics.hi_fi.display, param=self)
            s -= 1
            #self.delay(name="animate_odds", delay=0.1, handler=self.animate_odds_scan, param=s)
        else:
            self.delay(name="display", delay=0.1, handler=graphics.hi_fi.display, param=self)

    def animate_feature_scan(self, s):
        if s > 1:
            self.delay(name="feature_animation", delay=0.1, handler=graphics.hi_fi.feature_animation, param=s)
            self.delay(name="display", delay=0.1, handler=graphics.hi_fi.display, param=self)
            s -= 1
            #self.delay(name="animate_feature", delay=0.1, handler=self.animate_feature_scan, param=s)
        else:
            self.delay(name="display", delay=0.1, handler=graphics.hi_fi.display, param=self)

    def animate_eb_scan(self, s):
        if s > 1:
            self.delay(name="eb_animation", delay=0.1, handler=graphics.hi_fi.eb_animation, param=s)
            self.delay(name="display", delay=0.1, handler=graphics.hi_fi.display, param=self)
            s -= 1
            #self.delay(name="animate_eb", delay=0.1, handler=self.animate_eb_scan, param=s)
        else:
            self.delay(name="display", delay=0.1, handler=graphics.hi_fi.display, param=self)

    def check_eb_spotting(self):
        sd = self.game.spotting.position
        m4 = self.check_mixer4()
        if m4 == 1:
            if sd == 0:
                self.step_eb(9 - self.game.extra_ball.position)
        elif sd in [1,2,3,8,9,13,14,18,19,20,23,25,28,39,42,46,47]:
            self.step_eb(3 - self.game.extra_ball.position)
        elif sd in [6,7,15,21,24,26,37,40,41,44]:
            if self.game.extra_ball.position >= 3 and self.game.extra_ball.position < 6:
                self.step_eb(6 - self.game.extra_ball.position)
        else:
            if self.game.mixer4.position in [2,8,12,15]:
                self.game.extra_ball.step()
                self.check_lifter_status()

    def eb_probability(self):
        mix1 = self.game.mixer1.connected_rivet()
        if self.game.reflex.connected_rivet() == 0 and (mix1 in [1,6,8,11,13,16,18,22,24]):
            m3 = self.check_mixer3()
            if m3 == 1:
                i = self.check_eb_spotting()
                if i == 1:
                    return 1
                else:
                    return 0
        elif self.game.reflex.connected_rivet() == 1 and (mix1 not in [2,5,7,9,12,14,15,19,23]):
            m3 = self.check_mixer3()
            if m3 == 1:
                i = self.check_eb_spotting()
                if i == 1:
                    return 1
                else:
                    return 0
        elif self.game.reflex.connected_rivet() == 2 and (mix1 not in [5,9,12,15,19,23]):
            m3 = self.check_mixer3()
            if m3 == 1:
                i = self.check_eb_spotting()
                if i == 1:
                    return 1
                else:
                    return 0
        elif self.game.reflex.connected_rivet() == 3 and (mix1 not in [5,9,15,23]):
            m3 = self.check_mixer3()
            if m3 == 1:
                i = self.check_eb_spotting()
                if i == 1:
                    return 1
                else:
                    return 0
        elif self.game.reflex.connected_rivet() == 4:
            m3 = self.check_mixer3()
            if m3 == 1:
                i = self.check_eb_spotting()
                if i == 1:
                    return 1
                else:
                    return 0
        else:
            return 0

    def step_eb(self, number):
        if number >= 1:
            self.game.extra_ball.step()
            self.check_lifter_status()
            number -= 1
            self.delay(name="display", delay=0.1, handler=graphics.hi_fi.display, param=self)
            self.delay(name="step_eb", delay=0.1, handler=self.step_eb, param=number)

    # Define reset as the knock-off, anti-cheat relay disabled, and replay reset enabled.  Motors turn while credits are knocked off.
    # When meter reaches zero and the zero limit switch is hit, turn off motor sound and leave backglass gi on, but with tilt displayed.

    def startup(self):        
        # Every bingo requires the meter to register '0' 
        # before allowing coin entry --
        # also needs to show a plain 'off' backglass.
        self.eb = False
        self.game.anti_cheat.engage(self.game)
        self.tilt_actions()

class HiFi(procgame.game.BasicGame):
    """ Hi-Fi was the only game with the bump feature """
    def __init__(self, machine_type):
        super(HiFi, self).__init__(machine_type)
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

        self.searchdisc = units.Search("searchdisc", 49)

        #Search relays
        self.s1 = units.Relay("s1")
        self.s2 = units.Relay("s2")
        self.s3 = units.Relay("s3")
        self.s4 = units.Relay("s4")
        self.s5 = units.Relay("s5")
        self.search_index = units.Relay("search_index")

        #Odds stepper
        self.odds = units.Stepper("odds", 8, 'hi_fi')

        #Replay Counter
        self.card1_replay_counter = units.Stepper("card1_replay_counter", 500)
        #Corners Replay Counter
        self.corners_replay_counter = units.Stepper("corners_replay_counter", 400)
        #Initialize stepper units used to keep track of features or timing.
        self.timer = units.Stepper("timer", 40)
        self.ball_count = units.Stepper("ball_count", 8)

        # Initialize reflex(es) and mixers unique to this game
        self.reflex = units.Reflex("primary", 200)

        #This is a disc which has 50 positions
        #and will randomly complete paths through the various mixers to allow for odds or feature step.
        self.spotting = units.Spotting("spotting", 50)

        #Check for status of the replay register zero switch.  If positive
        #and machine is just powered on, this will zero out the replays.
        self.replay_reset = units.Relay("replay_reset")
        
        #Extra ball unit contains 24 positions.
        self.extra_ball = units.Stepper("extra_ball", 9)

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

        #Need to define relays for playing for ebs
        self.eb_play = units.Relay("eb_play")

        #Relay for corners lighting
        self.corners = units.Relay("corners")

        self.selector = units.Stepper("selector", 1)

        # Select-a-spot setup
        self.spotted_numbers = units.Stepper("spotted_numbers", 11)
        self.bump_feature = units.Stepper("bump_feature", 14)
        self.super_card = units.Stepper("super_card", 8)
        self.spotted = units.Stepper("spotted", 6, "hi_fi", "continuous")
        self.red_rollover = units.Relay("red_rollover")
        self.before_fourth = units.Relay("before_fourth")
        self.before_fifth = units.Relay("before_fifth")
        self.yellow_rollover = units.Relay("yellow_rollover")
        self.delay = units.Relay("delay")

        self.replays = 0
        self.returned = False

    def reset(self):
        super(HiFi, self).reset()
        self.logger = logging.getLogger('game')
        self.load_config('bingo.yaml')
        
        main_mode = SinglecardBingo(self)
        self.modes.add(main_mode)
        
game = HiFi(machine_type='pdb')
game.reset()
game.run_loop()
