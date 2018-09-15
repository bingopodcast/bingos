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
from bingo_emulator.graphics.palm_springs import *

class SinglecardBingo(procgame.game.Mode):
    def __init__(self, game):
        super(SinglecardBingo, self).__init__(game=game, priority=5)
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
        self.game.sound.register_sound('eb_search', "audio/EB_Search.wav")

    def sw_coin_active(self, sw):
        if self.game.eb_play.status == False:
            self.game.tilt.disengage()
            self.regular_play()
        else:
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
            self.game.reflex.decrease()
            self.game.coils.counter.pulse()
            graphics.palm_springs.display(self)
            self.animate_eb_scan([begin,self.game.spotting.movement_amount,self.game.spotting.movement_amount])

        self.delay(name="display", delay=0.1, handler=graphics.palm_springs.display, param=self)

    def sw_startButton_active(self, sw):
        self.game.eb_play.disengage()
        if self.game.replays > 0 or self.game.switches.freeplay.is_active():
            self.game.sound.stop('add')
            self.game.sound.play('add')
            self.game.tilt.disengage()
            self.regular_play()
            self.delay(name="display", delay=0.1, handler=graphics.palm_springs.display, param=self)

    def sw_enter_active(self, sw):
        if self.game.switches.left.is_active() and self.game.switches.right.is_active():
            self.game.end_run_loop()
            os.system("/home/nbaldridge/proc/bingo_emulator/start_game.sh palm_springs")

    def sw_all_active_for_2s(self, sw):
        if self.game.switches.drawer.is_active():
            if self.game.hold_feature.position == 8 and self.game.ball_count.position <= 4:
                self.check_shutter()
                self.game.hold_feature.reset()
                self.game.coils.holdLeft.disable()
                self.game.coils.holdRight.disable()
                if 1 in self.holes:
                    if self.game.switches.hole1.is_inactive():
                        self.holes.remove(1)
                    if self.game.spotted_numbers.position >= 7:
                        if self.game.spotted.position == 0:
                            self.holes.append(1)
                if 3 in self.holes:
                    if self.game.switches.hole3.is_inactive():
                        self.holes.remove(3)
                if 5 in self.holes:
                    if self.game.switches.hole5.is_inactive():
                        self.holes.remove(5)
                    if self.game.spotted_numbers.position >= 9:
                        if self.game.spotted.position == 2:
                            self.holes.append(5)
                if 7 in self.holes:
                    if self.game.switches.hole7.is_inactive():
                        self.holes.remove(7)
                if 9 in self.holes:
                    if self.game.switches.hole9.is_inactive():
                        self.holes.remove(9)
                    if self.game.spotted_numbers.position >= 13:
                        if self.game.spotted.position == 6:
                            self.holes.append(9)
                if 11 in self.holes:
                    if self.game.switches.hole11.is_inactive():
                        self.holes.remove(11)
                if 13 in self.holes:
                    if self.game.switches.hole13.is_inactive():
                        self.holes.remove(13)
                if 15 in self.holes:
                    if self.game.switches.hole15.is_inactive():
                        self.holes.remove(15)
                if 17 in self.holes:
                    if self.game.switches.hole17.is_inactive():
                        self.holes.remove(17)
                if 19 in self.holes:
                    if self.game.switches.hole19.is_inactive():
                        self.holes.remove(19)
                if 21 in self.holes:
                    if self.game.switches.hole21.is_inactive():
                        self.holes.remove(21)
                if 23 in self.holes:
                    if self.game.switches.hole23.is_inactive():
                        self.holes.remove(23)
                if 25 in self.holes:
                    if self.game.switches.hole25.is_inactive():
                        self.holes.remove(25)
                if 2 in self.holes:
                    if self.game.switches.hole2.is_inactive():
                        self.holes.remove(2)
                    if self.game.spotted_numbers.position >= 8:
                        if self.game.spotted.position == 1:
                            self.holes.append(2)
                if 4 in self.holes:
                    if self.game.switches.hole4.is_inactive():
                        self.holes.remove(4)
                if 6 in self.holes:
                    if self.game.switches.hole6.is_inactive():
                        self.holes.remove(6)
                if 8 in self.holes:
                    if self.game.switches.hole8.is_inactive():
                        self.holes.remove(8)
                    if self.game.spotted_numbers.position >= 10:
                        if self.game.spotted.position == 3:
                            self.holes.append(8)
                if 10 in self.holes:
                    if self.game.switches.hole10.is_inactive():
                        self.holes.remove(10)
                if 12 in self.holes:
                    if self.game.switches.hole12.is_inactive():
                        self.holes.remove(12)
                if 14 in self.holes:
                    if self.game.switches.hole14.is_inactive():
                        self.holes.remove(14)
                    if self.game.spotted_numbers.position >= 12:
                        if self.game.spotted.position == 5:
                            self.holes.append(14)
                if 16 in self.holes:
                    if self.game.switches.hole16.is_inactive():
                        self.holes.remove(16)
                    if self.game.spotted_numbers.position >= 11:
                        if self.game.spotted.position == 4:
                            self.holes.append(16)
                if 18 in self.holes:
                    if self.game.switches.hole18.is_inactive():
                        self.holes.remove(18)
                if 20 in self.holes:
                    if self.game.switches.hole20.is_inactive():
                        self.holes.remove(20)
                if 22 in self.holes:
                    if self.game.switches.hole22.is_inactive():
                        self.holes.remove(22)
                if 24 in self.holes:
                    if self.game.switches.hole24.is_inactive():
                        self.holes.remove(24)
            graphics.palm_springs.display(self)


    def sw_enter_active_for_2s(self, sw):
        if self.game.switches.drawer.is_inactive():
            if self.game.hold_feature.position == 8 and self.game.ball_count.position <= 4:
                self.check_shutter()
                self.game.hold_feature.reset()
                self.game.coils.holdLeft.disable()
                self.game.coils.holdRight.disable()
                if 1 in self.holes:
                    if self.game.switches.hole1.is_inactive():
                        self.holes.remove(1)
                    if self.game.spotted_numbers.position >= 7:
                        if self.game.spotted.position == 0:
                            self.holes.append(1)
                if 3 in self.holes:
                    if self.game.switches.hole3.is_inactive():
                        self.holes.remove(3)
                if 5 in self.holes:
                    if self.game.switches.hole5.is_inactive():
                        self.holes.remove(5)
                    if self.game.spotted_numbers.position >= 9:
                        if self.game.spotted.position == 2:
                            self.holes.append(5)
                if 7 in self.holes:
                    if self.game.switches.hole7.is_inactive():
                        self.holes.remove(7)
                if 9 in self.holes:
                    if self.game.switches.hole9.is_inactive():
                        self.holes.remove(9)
                    if self.game.spotted_numbers.position >= 13:
                        if self.game.spotted.position == 6:
                            self.holes.append(9)
                if 11 in self.holes:
                    if self.game.switches.hole11.is_inactive():
                        self.holes.remove(11)
                if 13 in self.holes:
                    if self.game.switches.hole13.is_inactive():
                        self.holes.remove(13)
                if 15 in self.holes:
                    if self.game.switches.hole15.is_inactive():
                        self.holes.remove(15)
                if 17 in self.holes:
                    if self.game.switches.hole17.is_inactive():
                        self.holes.remove(17)
                if 19 in self.holes:
                    if self.game.switches.hole19.is_inactive():
                        self.holes.remove(19)
                if 21 in self.holes:
                    if self.game.switches.hole21.is_inactive():
                        self.holes.remove(21)
                if 23 in self.holes:
                    if self.game.switches.hole23.is_inactive():
                        self.holes.remove(23)
                if 25 in self.holes:
                    if self.game.switches.hole25.is_inactive():
                        self.holes.remove(25)
                if 2 in self.holes:
                    if self.game.switches.hole2.is_inactive():
                        self.holes.remove(2)
                    if self.game.spotted_numbers.position >= 8:
                        if self.game.spotted.position == 1:
                            self.holes.append(2)
                if 4 in self.holes:
                    if self.game.switches.hole4.is_inactive():
                        self.holes.remove(4)
                if 6 in self.holes:
                    if self.game.switches.hole6.is_inactive():
                        self.holes.remove(6)
                if 8 in self.holes:
                    if self.game.switches.hole8.is_inactive():
                        self.holes.remove(8)
                    if self.game.spotted_numbers.position >= 10:
                        if self.game.spotted.position == 3:
                            self.holes.append(8)
                if 10 in self.holes:
                    if self.game.switches.hole10.is_inactive():
                        self.holes.remove(10)
                if 12 in self.holes:
                    if self.game.switches.hole12.is_inactive():
                        self.holes.remove(12)
                if 14 in self.holes:
                    if self.game.switches.hole14.is_inactive():
                        self.holes.remove(14)
                    if self.game.spotted_numbers.position >= 12:
                        if self.game.spotted.position == 5:
                            self.holes.append(14)
                if 16 in self.holes:
                    if self.game.switches.hole16.is_inactive():
                        self.holes.remove(16)
                    if self.game.spotted_numbers.position >= 11:
                        if self.game.spotted.position == 4:
                            self.holes.append(16)
                if 18 in self.holes:
                    if self.game.switches.hole18.is_inactive():
                        self.holes.remove(18)
                if 20 in self.holes:
                    if self.game.switches.hole20.is_inactive():
                        self.holes.remove(20)
                if 22 in self.holes:
                    if self.game.switches.hole22.is_inactive():
                        self.holes.remove(22)
                if 24 in self.holes:
                    if self.game.switches.hole24.is_inactive():
                        self.holes.remove(24)
            graphics.palm_springs.display(self)

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
        if self.game.spotted_numbers.position >= 7:
            if self.game.spotted.position == 0:
                if 1 not in self.holes:
                    self.holes.append(1)
        if self.game.spotted_numbers.position >= 8:
            if self.game.spotted.position == 1:
                if 2 not in self.holes:
                    self.holes.append(2)
        if self.game.spotted_numbers.position >= 9:
            if self.game.spotted.position == 2:
                if 5 not in self.holes:
                    self.holes.append(5)
        if self.game.spotted_numbers.position >= 10:
            if self.game.spotted.position == 3:
                if 8 not in self.holes:
                    self.holes.append(8)
        if self.game.spotted_numbers.position >= 11:
            if self.game.spotted.position == 4:
                if 16 not in self.holes:
                    self.holes.append(16)
        if self.game.spotted_numbers.position >= 12:
            if self.game.spotted.position == 5:
                if 14 not in self.holes:
                    self.holes.append(14)
        if self.game.spotted_numbers.position >= 13:
            if self.game.spotted.position == 6:
                if 9 not in self.holes:
                    self.holes.append(9)
        graphics.palm_springs.display(self)

    def sw_left_active(self, sw):
        max_ball = 4

        if self.game.spotted_numbers.position > 6:
            if self.game.ball_count.position < max_ball:
                self.game.spotted.stepdown()
                #Initial spotted selection - 2 numbers
                if self.game.spotted_numbers.position == 8:
                    if self.game.spotted.position == 0:
                        if 9 in self.holes:
                            if self.game.switches.hole9.is_inactive():
                                self.holes.remove(9)
                        if 14 in self.holes:
                            if self.game.switches.hole14.is_inactive():
                                self.holes.remove(14)
                        if 16 in self.holes:
                            if self.game.switches.hole16.is_inactive():
                                self.holes.remove(16)
                        if 8 in self.holes:
                            if self.game.switches.hole8.is_inactive():
                                self.holes.remove(8)
                        if 5 in self.holes:
                            if self.game.switches.hole5.is_inactive():
                                self.holes.remove(5)
                        if 2 in self.holes:
                            if self.game.switches.hole2.is_inactive():
                                self.holes.remove(2)
                        if 1 not in self.holes:
                            self.holes.append(1)
                    elif self.game.spotted.position == 1:
                        if 9 in self.holes:
                            if self.game.switches.hole9.is_inactive():
                                self.holes.remove(9)
                        if 14 in self.holes:
                            if self.game.switches.hole14.is_inactive():
                                self.holes.remove(14)
                        if 16 in self.holes:
                            if self.game.switches.hole16.is_inactive():
                                self.holes.remove(16)
                        if 8 in self.holes:
                            if self.game.switches.hole8.is_inactive():
                                self.holes.remove(8)
                        if 5 in self.holes:
                            if self.game.switches.hole5.is_inactive():
                                self.holes.remove(5)
                        if 1 in self.holes:
                            if self.game.switches.hole1.is_inactive():
                                self.holes.remove(1)
                        if 2 not in self.holes:
                            self.holes.append(2)
                    else:
                        if 9 in self.holes:
                            if self.game.switches.hole9.is_inactive():
                                self.holes.remove(9)
                        if 14 in self.holes:
                            if self.game.switches.hole14.is_inactive():
                                self.holes.remove(14)
                        if 16 in self.holes:
                            if self.game.switches.hole16.is_inactive():
                                self.holes.remove(16)
                        if 8 in self.holes:
                            if self.game.switches.hole8.is_inactive():
                                self.holes.remove(8)
                        if 5 in self.holes:
                            if self.game.switches.hole5.is_inactive():
                                self.holes.remove(5)
                        if 1 in self.holes:
                            if self.game.switches.hole1.is_inactive():
                                self.holes.remove(1)
                        if 2 in self.holes:
                            if self.game.switches.hole2.is_inactive():
                                self.holes.remove(2)
                #three numbers available
                elif self.game.spotted_numbers.position == 9:
                    if self.game.spotted.position == 0:
                        if 9 in self.holes:
                            if self.game.switches.hole9.is_inactive():
                                self.holes.remove(9)
                        if 14 in self.holes:
                            if self.game.switches.hole14.is_inactive():
                                self.holes.remove(14)
                        if 16 in self.holes:
                            if self.game.switches.hole16.is_inactive():
                                self.holes.remove(16)
                        if 8 in self.holes:
                            if self.game.switches.hole8.is_inactive():
                                self.holes.remove(8)
                        if 5 in self.holes:
                            if self.game.switches.hole5.is_inactive():
                                self.holes.remove(5)
                        if 2 in self.holes:
                            if self.game.switches.hole2.is_inactive():
                                self.holes.remove(2)
                        if 1 not in self.holes:
                            self.holes.append(1)
                    elif self.game.spotted.position == 1:
                        if 9 in self.holes:
                            if self.game.switches.hole9.is_inactive():
                                self.holes.remove(9)
                        if 14 in self.holes:
                            if self.game.switches.hole14.is_inactive():
                                self.holes.remove(14)
                        if 16 in self.holes:
                            if self.game.switches.hole16.is_inactive():
                                self.holes.remove(16)
                        if 8 in self.holes:
                            if self.game.switches.hole8.is_inactive():
                                self.holes.remove(8)
                        if 5 in self.holes:
                            if self.game.switches.hole5.is_inactive():
                                self.holes.remove(5)
                        if 1 in self.holes:
                            if self.game.switches.hole1.is_inactive():
                                self.holes.remove(1)
                        if 2 not in self.holes:
                            self.holes.append(2)
                    elif self.game.spotted.position == 2:
                        if 9 in self.holes:
                            if self.game.switches.hole9.is_inactive():
                                self.holes.remove(9)
                        if 14 in self.holes:
                            if self.game.switches.hole14.is_inactive():
                                self.holes.remove(14)
                        if 16 in self.holes:
                            if self.game.switches.hole16.is_inactive():
                                self.holes.remove(16)
                        if 8 in self.holes:
                            if self.game.switches.hole8.is_inactive():
                                self.holes.remove(8)
                        if 2 in self.holes:
                            if self.game.switches.hole2.is_inactive():
                                self.holes.remove(2)
                        if 1 in self.holes:
                            if self.game.switches.hole1.is_inactive():
                                self.holes.remove(1)
                        if 5 not in self.holes:
                            self.holes.append(5)
                    else:
                        if 9 in self.holes:
                            if self.game.switches.hole9.is_inactive():
                                self.holes.remove(9)
                        if 14 in self.holes:
                            if self.game.switches.hole14.is_inactive():
                                self.holes.remove(14)
                        if 16 in self.holes:
                            if self.game.switches.hole16.is_inactive():
                                self.holes.remove(16)
                        if 8 in self.holes:
                            if self.game.switches.hole8.is_inactive():
                                self.holes.remove(8)
                        if 5 in self.holes:
                            if self.game.switches.hole5.is_inactive():
                                self.holes.remove(5)
                        if 1 in self.holes:
                            if self.game.switches.hole1.is_inactive():
                                self.holes.remove(1)
                        if 2 in self.holes:
                            if self.game.switches.hole2.is_inactive():
                                self.holes.remove(2)
                #four positions
                elif self.game.spotted_numbers.position == 10:
                    if self.game.spotted.position == 0:
                        if 9 in self.holes:
                            if self.game.switches.hole9.is_inactive():
                                self.holes.remove(9)
                        if 14 in self.holes:
                            if self.game.switches.hole14.is_inactive():
                                self.holes.remove(14)
                        if 16 in self.holes:
                            if self.game.switches.hole16.is_inactive():
                                self.holes.remove(16)
                        if 8 in self.holes:
                            if self.game.switches.hole8.is_inactive():
                                self.holes.remove(8)
                        if 5 in self.holes:
                            if self.game.switches.hole5.is_inactive():
                                self.holes.remove(5)
                        if 2 in self.holes:
                            if self.game.switches.hole2.is_inactive():
                                self.holes.remove(2)
                        if 1 not in self.holes:
                            self.holes.append(1)
                    elif self.game.spotted.position == 1:
                        if 9 in self.holes:
                            if self.game.switches.hole9.is_inactive():
                                self.holes.remove(9)
                        if 14 in self.holes:
                            if self.game.switches.hole14.is_inactive():
                                self.holes.remove(14)
                        if 16 in self.holes:
                            if self.game.switches.hole16.is_inactive():
                                self.holes.remove(16)
                        if 8 in self.holes:
                            if self.game.switches.hole8.is_inactive():
                                self.holes.remove(8)
                        if 5 in self.holes:
                            if self.game.switches.hole5.is_inactive():
                                self.holes.remove(5)
                        if 1 in self.holes:
                            if self.game.switches.hole1.is_inactive():
                                self.holes.remove(1)
                        if 2 not in self.holes:
                            self.holes.append(2)
                    elif self.game.spotted.position == 2:
                        if 9 in self.holes:
                            if self.game.switches.hole9.is_inactive():
                                self.holes.remove(9)
                        if 14 in self.holes:
                            if self.game.switches.hole14.is_inactive():
                                self.holes.remove(14)
                        if 16 in self.holes:
                            if self.game.switches.hole16.is_inactive():
                                self.holes.remove(16)
                        if 8 in self.holes:
                            if self.game.switches.hole8.is_inactive():
                                self.holes.remove(8)
                        if 2 in self.holes:
                            if self.game.switches.hole2.is_inactive():
                                self.holes.remove(2)
                        if 1 in self.holes:
                            if self.game.switches.hole1.is_inactive():
                                self.holes.remove(1)
                        if 5 not in self.holes:
                            self.holes.append(5)
                    elif self.game.spotted.position == 3:
                        if 9 in self.holes:
                            if self.game.switches.hole9.is_inactive():
                                self.holes.remove(9)
                        if 14 in self.holes:
                            if self.game.switches.hole14.is_inactive():
                                self.holes.remove(14)
                        if 16 in self.holes:
                            if self.game.switches.hole16.is_inactive():
                                self.holes.remove(16)
                        if 5 in self.holes:
                            if self.game.switches.hole5.is_inactive():
                                self.holes.remove(5)
                        if 2 in self.holes:
                            if self.game.switches.hole2.is_inactive():
                                self.holes.remove(2)
                        if 1 in self.holes:
                            if self.game.switches.hole1.is_inactive():
                                self.holes.remove(1)
                        if 8 not in self.holes:
                            self.holes.append(8)
                    else:
                        if 9 in self.holes:
                            if self.game.switches.hole9.is_inactive():
                                self.holes.remove(9)
                        if 14 in self.holes:
                            if self.game.switches.hole14.is_inactive():
                                self.holes.remove(14)
                        if 16 in self.holes:
                            if self.game.switches.hole16.is_inactive():
                                self.holes.remove(16)
                        if 8 in self.holes:
                            if self.game.switches.hole8.is_inactive():
                                self.holes.remove(8)
                        if 5 in self.holes:
                            if self.game.switches.hole5.is_inactive():
                                self.holes.remove(5)
                        if 1 in self.holes:
                            if self.game.switches.hole1.is_inactive():
                                self.holes.remove(1)
                        if 2 in self.holes:
                            if self.game.switches.hole2.is_inactive():
                                self.holes.remove(2)
                # And five numbers
                elif self.game.spotted_numbers.position == 11: 
                    if self.game.spotted.position == 0:
                        if 9 in self.holes:
                            if self.game.switches.hole9.is_inactive():
                                self.holes.remove(9)
                        if 14 in self.holes:
                            if self.game.switches.hole14.is_inactive():
                                self.holes.remove(14)
                        if 16 in self.holes:
                            if self.game.switches.hole16.is_inactive():
                                self.holes.remove(16)
                        if 8 in self.holes:
                            if self.game.switches.hole8.is_inactive():
                                self.holes.remove(8)
                        if 5 in self.holes:
                            if self.game.switches.hole5.is_inactive():
                                self.holes.remove(5)
                        if 2 in self.holes:
                            if self.game.switches.hole2.is_inactive():
                                self.holes.remove(2)
                        if 1 not in self.holes:
                            self.holes.append(1)
                    elif self.game.spotted.position == 1:
                        if 9 in self.holes:
                            if self.game.switches.hole9.is_inactive():
                                self.holes.remove(9)
                        if 14 in self.holes:
                            if self.game.switches.hole14.is_inactive():
                                self.holes.remove(14)
                        if 16 in self.holes:
                            if self.game.switches.hole16.is_inactive():
                                self.holes.remove(16)
                        if 8 in self.holes:
                            if self.game.switches.hole8.is_inactive():
                                self.holes.remove(8)
                        if 5 in self.holes:
                            if self.game.switches.hole5.is_inactive():
                                self.holes.remove(5)
                        if 1 in self.holes:
                            if self.game.switches.hole1.is_inactive():
                                self.holes.remove(1)
                        if 2 not in self.holes:
                            self.holes.append(2)
                    elif self.game.spotted.position == 2:
                        if 9 in self.holes:
                            if self.game.switches.hole9.is_inactive():
                                self.holes.remove(9)
                        if 14 in self.holes:
                            if self.game.switches.hole14.is_inactive():
                                self.holes.remove(14)
                        if 16 in self.holes:
                            if self.game.switches.hole16.is_inactive():
                                self.holes.remove(16)
                        if 8 in self.holes:
                            if self.game.switches.hole8.is_inactive():
                                self.holes.remove(8)
                        if 2 in self.holes:
                            if self.game.switches.hole2.is_inactive():
                                self.holes.remove(2)
                        if 1 in self.holes:
                            if self.game.switches.hole1.is_inactive():
                                self.holes.remove(1)
                        if 5 not in self.holes:
                            self.holes.append(5)
                    elif self.game.spotted.position == 3:
                        if 9 in self.holes:
                            if self.game.switches.hole9.is_inactive():
                                self.holes.remove(9)
                        if 14 in self.holes:
                            if self.game.switches.hole14.is_inactive():
                                self.holes.remove(14)
                        if 16 in self.holes:
                            if self.game.switches.hole16.is_inactive():
                                self.holes.remove(16)
                        if 5 in self.holes:
                            if self.game.switches.hole5.is_inactive():
                                self.holes.remove(5)
                        if 2 in self.holes:
                            if self.game.switches.hole2.is_inactive():
                                self.holes.remove(2)
                        if 1 in self.holes:
                            if self.game.switches.hole1.is_inactive():
                                self.holes.remove(1)
                        if 8 not in self.holes:
                            self.holes.append(8)
                    elif self.game.spotted.position == 4:
                        if 9 in self.holes:
                            if self.game.switches.hole9.is_inactive():
                                self.holes.remove(9)
                        if 14 in self.holes:
                            if self.game.switches.hole14.is_inactive():
                                self.holes.remove(14)
                        if 8 in self.holes:
                            if self.game.switches.hole8.is_inactive():
                                self.holes.remove(8)
                        if 5 in self.holes:
                            if self.game.switches.hole5.is_inactive():
                                self.holes.remove(5)
                        if 2 in self.holes:
                            if self.game.switches.hole2.is_inactive():
                                self.holes.remove(2)
                        if 1 in self.holes:
                            if self.game.switches.hole1.is_inactive():
                                self.holes.remove(1)
                        if 16 not in self.holes:
                            self.holes.append(16)
                    else:
                        if 9 in self.holes:
                            if self.game.switches.hole9.is_inactive():
                                self.holes.remove(9)
                        if 14 in self.holes:
                            if self.game.switches.hole14.is_inactive():
                                self.holes.remove(14)
                        if 16 in self.holes:
                            if self.game.switches.hole16.is_inactive():
                                self.holes.remove(16)
                        if 8 in self.holes:
                            if self.game.switches.hole8.is_inactive():
                                self.holes.remove(8)
                        if 5 in self.holes:
                            if self.game.switches.hole5.is_inactive():
                                self.holes.remove(5)
                        if 1 in self.holes:
                            if self.game.switches.hole1.is_inactive():
                                self.holes.remove(1)
                        if 2 in self.holes:
                            if self.game.switches.hole2.is_inactive():
                                self.holes.remove(2)
                # And six numbers
                elif self.game.spotted_numbers.position == 12:
                    if self.game.spotted.position == 0:
                        if 9 in self.holes:
                            if self.game.switches.hole9.is_inactive():
                                self.holes.remove(9)
                        if 14 in self.holes:
                            if self.game.switches.hole14.is_inactive():
                                self.holes.remove(14)
                        if 16 in self.holes:
                            if self.game.switches.hole16.is_inactive():
                                self.holes.remove(16)
                        if 8 in self.holes:
                            if self.game.switches.hole8.is_inactive():
                                self.holes.remove(8)
                        if 5 in self.holes:
                            if self.game.switches.hole5.is_inactive():
                                self.holes.remove(5)
                        if 2 in self.holes:
                            if self.game.switches.hole2.is_inactive():
                                self.holes.remove(2)
                        if 1 not in self.holes:
                            self.holes.append(1)
                    elif self.game.spotted.position == 1:
                        if 9 in self.holes:
                            if self.game.switches.hole9.is_inactive():
                                self.holes.remove(9)
                        if 14 in self.holes:
                            if self.game.switches.hole14.is_inactive():
                                self.holes.remove(14)
                        if 16 in self.holes:
                            if self.game.switches.hole16.is_inactive():
                                self.holes.remove(16)
                        if 8 in self.holes:
                            if self.game.switches.hole8.is_inactive():
                                self.holes.remove(8)
                        if 5 in self.holes:
                            if self.game.switches.hole5.is_inactive():
                                self.holes.remove(5)
                        if 1 in self.holes:
                            if self.game.switches.hole1.is_inactive():
                                self.holes.remove(1)
                        if 2 not in self.holes:
                            self.holes.append(2)
                    elif self.game.spotted.position == 2:
                        if 9 in self.holes:
                            if self.game.switches.hole9.is_inactive():
                                self.holes.remove(9)
                        if 14 in self.holes:
                            if self.game.switches.hole14.is_inactive():
                                self.holes.remove(14)
                        if 16 in self.holes:
                            if self.game.switches.hole16.is_inactive():
                                self.holes.remove(16)
                        if 8 in self.holes:
                            if self.game.switches.hole8.is_inactive():
                                self.holes.remove(8)
                        if 2 in self.holes:
                            if self.game.switches.hole2.is_inactive():
                                self.holes.remove(2)
                        if 1 in self.holes:
                            if self.game.switches.hole1.is_inactive():
                                self.holes.remove(1)
                        if 5 not in self.holes:
                            self.holes.append(5)
                    elif self.game.spotted.position == 3:
                        if 9 in self.holes:
                            if self.game.switches.hole9.is_inactive():
                                self.holes.remove(9)
                        if 14 in self.holes:
                            if self.game.switches.hole14.is_inactive():
                                self.holes.remove(14)
                        if 16 in self.holes:
                            if self.game.switches.hole16.is_inactive():
                                self.holes.remove(16)
                        if 5 in self.holes:
                            if self.game.switches.hole5.is_inactive():
                                self.holes.remove(5)
                        if 2 in self.holes:
                            if self.game.switches.hole2.is_inactive():
                                self.holes.remove(2)
                        if 1 in self.holes:
                            if self.game.switches.hole1.is_inactive():
                                self.holes.remove(1)
                        if 8 not in self.holes:
                            self.holes.append(8)
                    elif self.game.spotted.position == 4:
                        if 9 in self.holes:
                            if self.game.switches.hole9.is_inactive():
                                self.holes.remove(9)
                        if 14 in self.holes:
                            if self.game.switches.hole14.is_inactive():
                                self.holes.remove(14)
                        if 8 in self.holes:
                            if self.game.switches.hole8.is_inactive():
                                self.holes.remove(8)
                        if 5 in self.holes:
                            if self.game.switches.hole5.is_inactive():
                                self.holes.remove(5)
                        if 2 in self.holes:
                            if self.game.switches.hole2.is_inactive():
                                self.holes.remove(2)
                        if 1 in self.holes:
                            if self.game.switches.hole1.is_inactive():
                                self.holes.remove(1)
                        if 16 not in self.holes:
                            self.holes.append(16)
                    elif self.game.spotted.position == 5:
                        if 9 in self.holes:
                            if self.game.switches.hole9.is_inactive():
                                self.holes.remove(9)
                        if 16 in self.holes:
                            if self.game.switches.hole16.is_inactive():
                                self.holes.remove(16)
                        if 8 in self.holes:
                            if self.game.switches.hole8.is_inactive():
                                self.holes.remove(8)
                        if 5 in self.holes:
                            if self.game.switches.hole5.is_inactive():
                                self.holes.remove(5)
                        if 2 in self.holes:
                            if self.game.switches.hole2.is_inactive():
                                self.holes.remove(2)
                        if 1 in self.holes:
                            if self.game.switches.hole1.is_inactive():
                                self.holes.remove(1)
                        if 14 not in self.holes:
                            self.holes.append(14)
                    else:
                        if 9 in self.holes:
                            if self.game.switches.hole9.is_inactive():
                                self.holes.remove(9)
                        if 14 in self.holes:
                            if self.game.switches.hole14.is_inactive():
                                self.holes.remove(14)
                        if 16 in self.holes:
                            if self.game.switches.hole16.is_inactive():
                                self.holes.remove(16)
                        if 8 in self.holes:
                            if self.game.switches.hole8.is_inactive():
                                self.holes.remove(8)
                        if 5 in self.holes:
                            if self.game.switches.hole5.is_inactive():
                                self.holes.remove(5)
                        if 1 in self.holes:
                            if self.game.switches.hole1.is_inactive():
                                self.holes.remove(1)
                        if 2 in self.holes:
                            if self.game.switches.hole2.is_inactive():
                                self.holes.remove(2)
                # All seven numbers
                elif self.game.spotted_numbers.position == 13:
                    if self.game.spotted.position == 0:
                        if 9 in self.holes:
                            if self.game.switches.hole9.is_inactive():
                                self.holes.remove(9)
                        if 14 in self.holes:
                            if self.game.switches.hole14.is_inactive():
                                self.holes.remove(14)
                        if 16 in self.holes:
                            if self.game.switches.hole16.is_inactive():
                                self.holes.remove(16)
                        if 8 in self.holes:
                            if self.game.switches.hole8.is_inactive():
                                self.holes.remove(8)
                        if 5 in self.holes:
                            if self.game.switches.hole5.is_inactive():
                                self.holes.remove(5)
                        if 2 in self.holes:
                            if self.game.switches.hole2.is_inactive():
                                self.holes.remove(2)
                        if 1 not in self.holes:
                            self.holes.append(1)
                    elif self.game.spotted.position == 1:
                        if 9 in self.holes:
                            if self.game.switches.hole9.is_inactive():
                                self.holes.remove(9)
                        if 14 in self.holes:
                            if self.game.switches.hole14.is_inactive():
                                self.holes.remove(14)
                        if 16 in self.holes:
                            if self.game.switches.hole16.is_inactive():
                                self.holes.remove(16)
                        if 8 in self.holes:
                            if self.game.switches.hole8.is_inactive():
                                self.holes.remove(8)
                        if 5 in self.holes:
                            if self.game.switches.hole5.is_inactive():
                                self.holes.remove(5)
                        if 1 in self.holes:
                            if self.game.switches.hole1.is_inactive():
                                self.holes.remove(1)
                        if 2 not in self.holes:
                            self.holes.append(2)
                    elif self.game.spotted.position == 2:
                        if 9 in self.holes:
                            if self.game.switches.hole9.is_inactive():
                                self.holes.remove(9)
                        if 14 in self.holes:
                            if self.game.switches.hole14.is_inactive():
                                self.holes.remove(14)
                        if 16 in self.holes:
                            if self.game.switches.hole16.is_inactive():
                                self.holes.remove(16)
                        if 8 in self.holes:
                            if self.game.switches.hole8.is_inactive():
                                self.holes.remove(8)
                        if 2 in self.holes:
                            if self.game.switches.hole2.is_inactive():
                                self.holes.remove(2)
                        if 1 in self.holes:
                            if self.game.switches.hole1.is_inactive():
                                self.holes.remove(1)
                        if 5 not in self.holes:
                            self.holes.append(5)
                    elif self.game.spotted.position == 3:
                        if 9 in self.holes:
                            if self.game.switches.hole9.is_inactive():
                                self.holes.remove(9)
                        if 14 in self.holes:
                            if self.game.switches.hole14.is_inactive():
                                self.holes.remove(14)
                        if 16 in self.holes:
                            if self.game.switches.hole16.is_inactive():
                                self.holes.remove(16)
                        if 5 in self.holes:
                            if self.game.switches.hole5.is_inactive():
                                self.holes.remove(5)
                        if 2 in self.holes:
                            if self.game.switches.hole2.is_inactive():
                                self.holes.remove(2)
                        if 1 in self.holes:
                            if self.game.switches.hole1.is_inactive():
                                self.holes.remove(1)
                        if 8 not in self.holes:
                            self.holes.append(8)
                    elif self.game.spotted.position == 4:
                        if 9 in self.holes:
                            if self.game.switches.hole9.is_inactive():
                                self.holes.remove(9)
                        if 14 in self.holes:
                            if self.game.switches.hole14.is_inactive():
                                self.holes.remove(14)
                        if 8 in self.holes:
                            if self.game.switches.hole8.is_inactive():
                                self.holes.remove(8)
                        if 5 in self.holes:
                            if self.game.switches.hole5.is_inactive():
                                self.holes.remove(5)
                        if 2 in self.holes:
                            if self.game.switches.hole2.is_inactive():
                                self.holes.remove(2)
                        if 1 in self.holes:
                            if self.game.switches.hole1.is_inactive():
                                self.holes.remove(1)
                        if 16 not in self.holes:
                            self.holes.append(16)
                    elif self.game.spotted.position == 5:
                        if 9 in self.holes:
                            if self.game.switches.hole9.is_inactive():
                                self.holes.remove(9)
                        if 16 in self.holes:
                            if self.game.switches.hole16.is_inactive():
                                self.holes.remove(16)
                        if 8 in self.holes:
                            if self.game.switches.hole8.is_inactive():
                                self.holes.remove(8)
                        if 5 in self.holes:
                            if self.game.switches.hole5.is_inactive():
                                self.holes.remove(5)
                        if 2 in self.holes:
                            if self.game.switches.hole2.is_inactive():
                                self.holes.remove(2)
                        if 1 in self.holes:
                            if self.game.switches.hole1.is_inactive():
                                self.holes.remove(1)
                        if 14 not in self.holes:
                            self.holes.append(14)
                    elif self.game.spotted.position == 6:
                        if 14 in self.holes:
                            if self.game.switches.hole14.is_inactive():
                                self.holes.remove(14)
                        if 16 in self.holes:
                            if self.game.switches.hole16.is_inactive():
                                self.holes.remove(16)
                        if 8 in self.holes:
                            if self.game.switches.hole8.is_inactive():
                                self.holes.remove(8)
                        if 5 in self.holes:
                            if self.game.switches.hole5.is_inactive():
                                self.holes.remove(5)
                        if 2 in self.holes:
                            if self.game.switches.hole2.is_inactive():
                                self.holes.remove(2)
                        if 1 in self.holes:
                            if self.game.switches.hole1.is_inactive():
                                self.holes.remove(1)
                        if 9 not in self.holes:
                            self.holes.append(9)
                    else:
                        if 9 in self.holes:
                            if self.game.switches.hole9.is_inactive():
                                self.holes.remove(9)
                        if 14 in self.holes:
                            if self.game.switches.hole14.is_inactive():
                                self.holes.remove(14)
                        if 16 in self.holes:
                            if self.game.switches.hole16.is_inactive():
                                self.holes.remove(16)
                        if 8 in self.holes:
                            if self.game.switches.hole8.is_inactive():
                                self.holes.remove(8)
                        if 5 in self.holes:
                            if self.game.switches.hole5.is_inactive():
                                self.holes.remove(5)
                        if 1 in self.holes:
                            if self.game.switches.hole1.is_inactive():
                                self.holes.remove(1)
                        if 2 in self.holes:
                            if self.game.switches.hole2.is_inactive():
                                self.holes.remove(2)

        self.delay(name="display", delay=0.1, handler=graphics.palm_springs.display, param=self)

    def sw_right_active(self, sw):
        max_ball = 4

        if self.game.spotted_numbers.position > 6:
            if self.game.ball_count.position < max_ball:
                self.game.spotted.step()
                #Initial spotted selection - 2 numbers
                if self.game.spotted_numbers.position == 8:
                    if self.game.spotted.position == 0:
                        if 9 in self.holes:
                            if self.game.switches.hole9.is_inactive():
                                self.holes.remove(9)
                        if 14 in self.holes:
                            if self.game.switches.hole14.is_inactive():
                                self.holes.remove(14)
                        if 16 in self.holes:
                            if self.game.switches.hole16.is_inactive():
                                self.holes.remove(16)
                        if 8 in self.holes:
                            if self.game.switches.hole8.is_inactive():
                                self.holes.remove(8)
                        if 5 in self.holes:
                            if self.game.switches.hole5.is_inactive():
                                self.holes.remove(5)
                        if 2 in self.holes:
                            if self.game.switches.hole2.is_inactive():
                                self.holes.remove(2)
                        if 1 not in self.holes:
                            self.holes.append(1)
                    elif self.game.spotted.position == 1:
                        if 9 in self.holes:
                            if self.game.switches.hole9.is_inactive():
                                self.holes.remove(9)
                        if 14 in self.holes:
                            if self.game.switches.hole14.is_inactive():
                                self.holes.remove(14)
                        if 16 in self.holes:
                            if self.game.switches.hole16.is_inactive():
                                self.holes.remove(16)
                        if 8 in self.holes:
                            if self.game.switches.hole8.is_inactive():
                                self.holes.remove(8)
                        if 5 in self.holes:
                            if self.game.switches.hole5.is_inactive():
                                self.holes.remove(5)
                        if 1 in self.holes:
                            if self.game.switches.hole1.is_inactive():
                                self.holes.remove(1)
                        if 2 not in self.holes:
                            self.holes.append(2)
                    else:
                        if 9 in self.holes:
                            if self.game.switches.hole9.is_inactive():
                                self.holes.remove(9)
                        if 14 in self.holes:
                            if self.game.switches.hole14.is_inactive():
                                self.holes.remove(14)
                        if 16 in self.holes:
                            if self.game.switches.hole16.is_inactive():
                                self.holes.remove(16)
                        if 8 in self.holes:
                            if self.game.switches.hole8.is_inactive():
                                self.holes.remove(8)
                        if 5 in self.holes:
                            if self.game.switches.hole5.is_inactive():
                                self.holes.remove(5)
                        if 1 in self.holes:
                            if self.game.switches.hole1.is_inactive():
                                self.holes.remove(1)
                        if 2 in self.holes:
                            if self.game.switches.hole2.is_inactive():
                                self.holes.remove(2)
                #three numbers available
                elif self.game.spotted_numbers.position == 9:
                    if self.game.spotted.position == 0:
                        if 9 in self.holes:
                            if self.game.switches.hole9.is_inactive():
                                self.holes.remove(9)
                        if 14 in self.holes:
                            if self.game.switches.hole14.is_inactive():
                                self.holes.remove(14)
                        if 16 in self.holes:
                            if self.game.switches.hole16.is_inactive():
                                self.holes.remove(16)
                        if 8 in self.holes:
                            if self.game.switches.hole8.is_inactive():
                                self.holes.remove(8)
                        if 5 in self.holes:
                            if self.game.switches.hole5.is_inactive():
                                self.holes.remove(5)
                        if 2 in self.holes:
                            if self.game.switches.hole2.is_inactive():
                                self.holes.remove(2)
                        if 1 not in self.holes:
                            self.holes.append(1)
                    elif self.game.spotted.position == 1:
                        if 9 in self.holes:
                            if self.game.switches.hole9.is_inactive():
                                self.holes.remove(9)
                        if 14 in self.holes:
                            if self.game.switches.hole14.is_inactive():
                                self.holes.remove(14)
                        if 16 in self.holes:
                            if self.game.switches.hole16.is_inactive():
                                self.holes.remove(16)
                        if 8 in self.holes:
                            if self.game.switches.hole8.is_inactive():
                                self.holes.remove(8)
                        if 5 in self.holes:
                            if self.game.switches.hole5.is_inactive():
                                self.holes.remove(5)
                        if 1 in self.holes:
                            if self.game.switches.hole1.is_inactive():
                                self.holes.remove(1)
                        if 2 not in self.holes:
                            self.holes.append(2)
                    elif self.game.spotted.position == 2:
                        if 9 in self.holes:
                            if self.game.switches.hole9.is_inactive():
                                self.holes.remove(9)
                        if 14 in self.holes:
                            if self.game.switches.hole14.is_inactive():
                                self.holes.remove(14)
                        if 16 in self.holes:
                            if self.game.switches.hole16.is_inactive():
                                self.holes.remove(16)
                        if 8 in self.holes:
                            if self.game.switches.hole8.is_inactive():
                                self.holes.remove(8)
                        if 2 in self.holes:
                            if self.game.switches.hole2.is_inactive():
                                self.holes.remove(2)
                        if 1 in self.holes:
                            if self.game.switches.hole1.is_inactive():
                                self.holes.remove(1)
                        if 5 not in self.holes:
                            self.holes.append(5)
                    else:
                        if 9 in self.holes:
                            if self.game.switches.hole9.is_inactive():
                                self.holes.remove(9)
                        if 14 in self.holes:
                            if self.game.switches.hole14.is_inactive():
                                self.holes.remove(14)
                        if 16 in self.holes:
                            if self.game.switches.hole16.is_inactive():
                                self.holes.remove(16)
                        if 8 in self.holes:
                            if self.game.switches.hole8.is_inactive():
                                self.holes.remove(8)
                        if 5 in self.holes:
                            if self.game.switches.hole5.is_inactive():
                                self.holes.remove(5)
                        if 1 in self.holes:
                            if self.game.switches.hole1.is_inactive():
                                self.holes.remove(1)
                        if 2 in self.holes:
                            if self.game.switches.hole2.is_inactive():
                                self.holes.remove(2)
                #four positions
                elif self.game.spotted_numbers.position == 10:
                    if self.game.spotted.position == 0:
                        if 9 in self.holes:
                            if self.game.switches.hole9.is_inactive():
                                self.holes.remove(9)
                        if 14 in self.holes:
                            if self.game.switches.hole14.is_inactive():
                                self.holes.remove(14)
                        if 16 in self.holes:
                            if self.game.switches.hole16.is_inactive():
                                self.holes.remove(16)
                        if 8 in self.holes:
                            if self.game.switches.hole8.is_inactive():
                                self.holes.remove(8)
                        if 5 in self.holes:
                            if self.game.switches.hole5.is_inactive():
                                self.holes.remove(5)
                        if 2 in self.holes:
                            if self.game.switches.hole2.is_inactive():
                                self.holes.remove(2)
                        if 1 not in self.holes:
                            self.holes.append(1)
                    elif self.game.spotted.position == 1:
                        if 9 in self.holes:
                            if self.game.switches.hole9.is_inactive():
                                self.holes.remove(9)
                        if 14 in self.holes:
                            if self.game.switches.hole14.is_inactive():
                                self.holes.remove(14)
                        if 16 in self.holes:
                            if self.game.switches.hole16.is_inactive():
                                self.holes.remove(16)
                        if 8 in self.holes:
                            if self.game.switches.hole8.is_inactive():
                                self.holes.remove(8)
                        if 5 in self.holes:
                            if self.game.switches.hole5.is_inactive():
                                self.holes.remove(5)
                        if 1 in self.holes:
                            if self.game.switches.hole1.is_inactive():
                                self.holes.remove(1)
                        if 2 not in self.holes:
                            self.holes.append(2)
                    elif self.game.spotted.position == 2:
                        if 9 in self.holes:
                            if self.game.switches.hole9.is_inactive():
                                self.holes.remove(9)
                        if 14 in self.holes:
                            if self.game.switches.hole14.is_inactive():
                                self.holes.remove(14)
                        if 16 in self.holes:
                            if self.game.switches.hole16.is_inactive():
                                self.holes.remove(16)
                        if 8 in self.holes:
                            if self.game.switches.hole8.is_inactive():
                                self.holes.remove(8)
                        if 2 in self.holes:
                            if self.game.switches.hole2.is_inactive():
                                self.holes.remove(2)
                        if 1 in self.holes:
                            if self.game.switches.hole1.is_inactive():
                                self.holes.remove(1)
                        if 5 not in self.holes:
                            self.holes.append(5)
                    elif self.game.spotted.position == 3:
                        if 9 in self.holes:
                            if self.game.switches.hole9.is_inactive():
                                self.holes.remove(9)
                        if 14 in self.holes:
                            if self.game.switches.hole14.is_inactive():
                                self.holes.remove(14)
                        if 16 in self.holes:
                            if self.game.switches.hole16.is_inactive():
                                self.holes.remove(16)
                        if 5 in self.holes:
                            if self.game.switches.hole5.is_inactive():
                                self.holes.remove(5)
                        if 2 in self.holes:
                            if self.game.switches.hole2.is_inactive():
                                self.holes.remove(2)
                        if 1 in self.holes:
                            if self.game.switches.hole1.is_inactive():
                                self.holes.remove(1)
                        if 8 not in self.holes:
                            self.holes.append(8)
                    else:
                        if 9 in self.holes:
                            if self.game.switches.hole9.is_inactive():
                                self.holes.remove(9)
                        if 14 in self.holes:
                            if self.game.switches.hole14.is_inactive():
                                self.holes.remove(14)
                        if 16 in self.holes:
                            if self.game.switches.hole16.is_inactive():
                                self.holes.remove(16)
                        if 8 in self.holes:
                            if self.game.switches.hole8.is_inactive():
                                self.holes.remove(8)
                        if 5 in self.holes:
                            if self.game.switches.hole5.is_inactive():
                                self.holes.remove(5)
                        if 1 in self.holes:
                            if self.game.switches.hole1.is_inactive():
                                self.holes.remove(1)
                        if 2 in self.holes:
                            if self.game.switches.hole2.is_inactive():
                                self.holes.remove(2)
                # And five numbers
                elif self.game.spotted_numbers.position == 11: 
                    if self.game.spotted.position == 0:
                        if 9 in self.holes:
                            if self.game.switches.hole9.is_inactive():
                                self.holes.remove(9)
                        if 14 in self.holes:
                            if self.game.switches.hole14.is_inactive():
                                self.holes.remove(14)
                        if 16 in self.holes:
                            if self.game.switches.hole16.is_inactive():
                                self.holes.remove(16)
                        if 8 in self.holes:
                            if self.game.switches.hole8.is_inactive():
                                self.holes.remove(8)
                        if 5 in self.holes:
                            if self.game.switches.hole5.is_inactive():
                                self.holes.remove(5)
                        if 2 in self.holes:
                            if self.game.switches.hole2.is_inactive():
                                self.holes.remove(2)
                        if 1 not in self.holes:
                            self.holes.append(1)
                    elif self.game.spotted.position == 1:
                        if 9 in self.holes:
                            if self.game.switches.hole9.is_inactive():
                                self.holes.remove(9)
                        if 14 in self.holes:
                            if self.game.switches.hole14.is_inactive():
                                self.holes.remove(14)
                        if 16 in self.holes:
                            if self.game.switches.hole16.is_inactive():
                                self.holes.remove(16)
                        if 8 in self.holes:
                            if self.game.switches.hole8.is_inactive():
                                self.holes.remove(8)
                        if 5 in self.holes:
                            if self.game.switches.hole5.is_inactive():
                                self.holes.remove(5)
                        if 1 in self.holes:
                            if self.game.switches.hole1.is_inactive():
                                self.holes.remove(1)
                        if 2 not in self.holes:
                            self.holes.append(2)
                    elif self.game.spotted.position == 2:
                        if 9 in self.holes:
                            if self.game.switches.hole9.is_inactive():
                                self.holes.remove(9)
                        if 14 in self.holes:
                            if self.game.switches.hole14.is_inactive():
                                self.holes.remove(14)
                        if 16 in self.holes:
                            if self.game.switches.hole16.is_inactive():
                                self.holes.remove(16)
                        if 8 in self.holes:
                            if self.game.switches.hole8.is_inactive():
                                self.holes.remove(8)
                        if 2 in self.holes:
                            if self.game.switches.hole2.is_inactive():
                                self.holes.remove(2)
                        if 1 in self.holes:
                            if self.game.switches.hole1.is_inactive():
                                self.holes.remove(1)
                        if 5 not in self.holes:
                            self.holes.append(5)
                    elif self.game.spotted.position == 3:
                        if 9 in self.holes:
                            if self.game.switches.hole9.is_inactive():
                                self.holes.remove(9)
                        if 14 in self.holes:
                            if self.game.switches.hole14.is_inactive():
                                self.holes.remove(14)
                        if 16 in self.holes:
                            if self.game.switches.hole16.is_inactive():
                                self.holes.remove(16)
                        if 5 in self.holes:
                            if self.game.switches.hole5.is_inactive():
                                self.holes.remove(5)
                        if 2 in self.holes:
                            if self.game.switches.hole2.is_inactive():
                                self.holes.remove(2)
                        if 1 in self.holes:
                            if self.game.switches.hole1.is_inactive():
                                self.holes.remove(1)
                        if 8 not in self.holes:
                            self.holes.append(8)
                    elif self.game.spotted.position == 4:
                        if 9 in self.holes:
                            if self.game.switches.hole9.is_inactive():
                                self.holes.remove(9)
                        if 14 in self.holes:
                            if self.game.switches.hole14.is_inactive():
                                self.holes.remove(14)
                        if 8 in self.holes:
                            if self.game.switches.hole8.is_inactive():
                                self.holes.remove(8)
                        if 5 in self.holes:
                            if self.game.switches.hole5.is_inactive():
                                self.holes.remove(5)
                        if 2 in self.holes:
                            if self.game.switches.hole2.is_inactive():
                                self.holes.remove(2)
                        if 1 in self.holes:
                            if self.game.switches.hole1.is_inactive():
                                self.holes.remove(1)
                        if 16 not in self.holes:
                            self.holes.append(16)
                    else:
                        if 9 in self.holes:
                            if self.game.switches.hole9.is_inactive():
                                self.holes.remove(9)
                        if 14 in self.holes:
                            if self.game.switches.hole14.is_inactive():
                                self.holes.remove(14)
                        if 16 in self.holes:
                            if self.game.switches.hole16.is_inactive():
                                self.holes.remove(16)
                        if 8 in self.holes:
                            if self.game.switches.hole8.is_inactive():
                                self.holes.remove(8)
                        if 5 in self.holes:
                            if self.game.switches.hole5.is_inactive():
                                self.holes.remove(5)
                        if 1 in self.holes:
                            if self.game.switches.hole1.is_inactive():
                                self.holes.remove(1)
                        if 2 in self.holes:
                            if self.game.switches.hole2.is_inactive():
                                self.holes.remove(2)
                # And six numbers
                elif self.game.spotted_numbers.position == 12:
                    if self.game.spotted.position == 0:
                        if 9 in self.holes:
                            if self.game.switches.hole9.is_inactive():
                                self.holes.remove(9)
                        if 14 in self.holes:
                            if self.game.switches.hole14.is_inactive():
                                self.holes.remove(14)
                        if 16 in self.holes:
                            if self.game.switches.hole16.is_inactive():
                                self.holes.remove(16)
                        if 8 in self.holes:
                            if self.game.switches.hole8.is_inactive():
                                self.holes.remove(8)
                        if 5 in self.holes:
                            if self.game.switches.hole5.is_inactive():
                                self.holes.remove(5)
                        if 2 in self.holes:
                            if self.game.switches.hole2.is_inactive():
                                self.holes.remove(2)
                        if 1 not in self.holes:
                            self.holes.append(1)
                    elif self.game.spotted.position == 1:
                        if 9 in self.holes:
                            if self.game.switches.hole9.is_inactive():
                                self.holes.remove(9)
                        if 14 in self.holes:
                            if self.game.switches.hole14.is_inactive():
                                self.holes.remove(14)
                        if 16 in self.holes:
                            if self.game.switches.hole16.is_inactive():
                                self.holes.remove(16)
                        if 8 in self.holes:
                            if self.game.switches.hole8.is_inactive():
                                self.holes.remove(8)
                        if 5 in self.holes:
                            if self.game.switches.hole5.is_inactive():
                                self.holes.remove(5)
                        if 1 in self.holes:
                            if self.game.switches.hole1.is_inactive():
                                self.holes.remove(1)
                        if 2 not in self.holes:
                            self.holes.append(2)
                    elif self.game.spotted.position == 2:
                        if 9 in self.holes:
                            if self.game.switches.hole9.is_inactive():
                                self.holes.remove(9)
                        if 14 in self.holes:
                            if self.game.switches.hole14.is_inactive():
                                self.holes.remove(14)
                        if 16 in self.holes:
                            if self.game.switches.hole16.is_inactive():
                                self.holes.remove(16)
                        if 8 in self.holes:
                            if self.game.switches.hole8.is_inactive():
                                self.holes.remove(8)
                        if 2 in self.holes:
                            if self.game.switches.hole2.is_inactive():
                                self.holes.remove(2)
                        if 1 in self.holes:
                            if self.game.switches.hole1.is_inactive():
                                self.holes.remove(1)
                        if 5 not in self.holes:
                            self.holes.append(5)
                    elif self.game.spotted.position == 3:
                        if 9 in self.holes:
                            if self.game.switches.hole9.is_inactive():
                                self.holes.remove(9)
                        if 14 in self.holes:
                            if self.game.switches.hole14.is_inactive():
                                self.holes.remove(14)
                        if 16 in self.holes:
                            if self.game.switches.hole16.is_inactive():
                                self.holes.remove(16)
                        if 5 in self.holes:
                            if self.game.switches.hole5.is_inactive():
                                self.holes.remove(5)
                        if 2 in self.holes:
                            if self.game.switches.hole2.is_inactive():
                                self.holes.remove(2)
                        if 1 in self.holes:
                            if self.game.switches.hole1.is_inactive():
                                self.holes.remove(1)
                        if 8 not in self.holes:
                            self.holes.append(8)
                    elif self.game.spotted.position == 4:
                        if 9 in self.holes:
                            if self.game.switches.hole9.is_inactive():
                                self.holes.remove(9)
                        if 14 in self.holes:
                            if self.game.switches.hole14.is_inactive():
                                self.holes.remove(14)
                        if 8 in self.holes:
                            if self.game.switches.hole8.is_inactive():
                                self.holes.remove(8)
                        if 5 in self.holes:
                            if self.game.switches.hole5.is_inactive():
                                self.holes.remove(5)
                        if 2 in self.holes:
                            if self.game.switches.hole2.is_inactive():
                                self.holes.remove(2)
                        if 1 in self.holes:
                            if self.game.switches.hole1.is_inactive():
                                self.holes.remove(1)
                        if 16 not in self.holes:
                            self.holes.append(16)
                    elif self.game.spotted.position == 5:
                        if 9 in self.holes:
                            if self.game.switches.hole9.is_inactive():
                                self.holes.remove(9)
                        if 16 in self.holes:
                            if self.game.switches.hole16.is_inactive():
                                self.holes.remove(16)
                        if 8 in self.holes:
                            if self.game.switches.hole8.is_inactive():
                                self.holes.remove(8)
                        if 5 in self.holes:
                            if self.game.switches.hole5.is_inactive():
                                self.holes.remove(5)
                        if 2 in self.holes:
                            if self.game.switches.hole2.is_inactive():
                                self.holes.remove(2)
                        if 1 in self.holes:
                            if self.game.switches.hole1.is_inactive():
                                self.holes.remove(1)
                        if 14 not in self.holes:
                            self.holes.append(14)
                    else:
                        if 9 in self.holes:
                            if self.game.switches.hole9.is_inactive():
                                self.holes.remove(9)
                        if 14 in self.holes:
                            if self.game.switches.hole14.is_inactive():
                                self.holes.remove(14)
                        if 16 in self.holes:
                            if self.game.switches.hole16.is_inactive():
                                self.holes.remove(16)
                        if 8 in self.holes:
                            if self.game.switches.hole8.is_inactive():
                                self.holes.remove(8)
                        if 5 in self.holes:
                            if self.game.switches.hole5.is_inactive():
                                self.holes.remove(5)
                        if 1 in self.holes:
                            if self.game.switches.hole1.is_inactive():
                                self.holes.remove(1)
                        if 2 in self.holes:
                            if self.game.switches.hole2.is_inactive():
                                self.holes.remove(2)
                # All seven numbers
                elif self.game.spotted_numbers.position == 13:
                    if self.game.spotted.position == 0:
                        if 9 in self.holes:
                            if self.game.switches.hole9.is_inactive():
                                self.holes.remove(9)
                        if 14 in self.holes:
                            if self.game.switches.hole14.is_inactive():
                                self.holes.remove(14)
                        if 16 in self.holes:
                            if self.game.switches.hole16.is_inactive():
                                self.holes.remove(16)
                        if 8 in self.holes:
                            if self.game.switches.hole8.is_inactive():
                                self.holes.remove(8)
                        if 5 in self.holes:
                            if self.game.switches.hole5.is_inactive():
                                self.holes.remove(5)
                        if 2 in self.holes:
                            if self.game.switches.hole2.is_inactive():
                                self.holes.remove(2)
                        if 1 not in self.holes:
                            self.holes.append(1)
                    elif self.game.spotted.position == 1:
                        if 9 in self.holes:
                            if self.game.switches.hole9.is_inactive():
                                self.holes.remove(9)
                        if 14 in self.holes:
                            if self.game.switches.hole14.is_inactive():
                                self.holes.remove(14)
                        if 16 in self.holes:
                            if self.game.switches.hole16.is_inactive():
                                self.holes.remove(16)
                        if 8 in self.holes:
                            if self.game.switches.hole8.is_inactive():
                                self.holes.remove(8)
                        if 5 in self.holes:
                            if self.game.switches.hole5.is_inactive():
                                self.holes.remove(5)
                        if 1 in self.holes:
                            if self.game.switches.hole1.is_inactive():
                                self.holes.remove(1)
                        if 2 not in self.holes:
                            self.holes.append(2)
                    elif self.game.spotted.position == 2:
                        if 9 in self.holes:
                            if self.game.switches.hole9.is_inactive():
                                self.holes.remove(9)
                        if 14 in self.holes:
                            if self.game.switches.hole14.is_inactive():
                                self.holes.remove(14)
                        if 16 in self.holes:
                            if self.game.switches.hole16.is_inactive():
                                self.holes.remove(16)
                        if 8 in self.holes:
                            if self.game.switches.hole8.is_inactive():
                                self.holes.remove(8)
                        if 2 in self.holes:
                            if self.game.switches.hole2.is_inactive():
                                self.holes.remove(2)
                        if 1 in self.holes:
                            if self.game.switches.hole1.is_inactive():
                                self.holes.remove(1)
                        if 5 not in self.holes:
                            self.holes.append(5)
                    elif self.game.spotted.position == 3:
                        if 9 in self.holes:
                            if self.game.switches.hole9.is_inactive():
                                self.holes.remove(9)
                        if 14 in self.holes:
                            if self.game.switches.hole14.is_inactive():
                                self.holes.remove(14)
                        if 16 in self.holes:
                            if self.game.switches.hole16.is_inactive():
                                self.holes.remove(16)
                        if 5 in self.holes:
                            if self.game.switches.hole5.is_inactive():
                                self.holes.remove(5)
                        if 2 in self.holes:
                            if self.game.switches.hole2.is_inactive():
                                self.holes.remove(2)
                        if 1 in self.holes:
                            if self.game.switches.hole1.is_inactive():
                                self.holes.remove(1)
                        if 8 not in self.holes:
                            self.holes.append(8)
                    elif self.game.spotted.position == 4:
                        if 9 in self.holes:
                            if self.game.switches.hole9.is_inactive():
                                self.holes.remove(9)
                        if 14 in self.holes:
                            if self.game.switches.hole14.is_inactive():
                                self.holes.remove(14)
                        if 8 in self.holes:
                            if self.game.switches.hole8.is_inactive():
                                self.holes.remove(8)
                        if 5 in self.holes:
                            if self.game.switches.hole5.is_inactive():
                                self.holes.remove(5)
                        if 2 in self.holes:
                            if self.game.switches.hole2.is_inactive():
                                self.holes.remove(2)
                        if 1 in self.holes:
                            if self.game.switches.hole1.is_inactive():
                                self.holes.remove(1)
                        if 16 not in self.holes:
                            self.holes.append(16)
                    elif self.game.spotted.position == 5:
                        if 9 in self.holes:
                            if self.game.switches.hole9.is_inactive():
                                self.holes.remove(9)
                        if 16 in self.holes:
                            if self.game.switches.hole16.is_inactive():
                                self.holes.remove(16)
                        if 8 in self.holes:
                            if self.game.switches.hole8.is_inactive():
                                self.holes.remove(8)
                        if 5 in self.holes:
                            if self.game.switches.hole5.is_inactive():
                                self.holes.remove(5)
                        if 2 in self.holes:
                            if self.game.switches.hole2.is_inactive():
                                self.holes.remove(2)
                        if 1 in self.holes:
                            if self.game.switches.hole1.is_inactive():
                                self.holes.remove(1)
                        if 14 not in self.holes:
                            self.holes.append(14)
                    elif self.game.spotted.position == 6:
                        if 14 in self.holes:
                            if self.game.switches.hole14.is_inactive():
                                self.holes.remove(14)
                        if 16 in self.holes:
                            if self.game.switches.hole16.is_inactive():
                                self.holes.remove(16)
                        if 8 in self.holes:
                            if self.game.switches.hole8.is_inactive():
                                self.holes.remove(8)
                        if 5 in self.holes:
                            if self.game.switches.hole5.is_inactive():
                                self.holes.remove(5)
                        if 2 in self.holes:
                            if self.game.switches.hole2.is_inactive():
                                self.holes.remove(2)
                        if 1 in self.holes:
                            if self.game.switches.hole1.is_inactive():
                                self.holes.remove(1)
                        if 9 not in self.holes:
                            self.holes.append(9)
                    else:
                        if 9 in self.holes:
                            if self.game.switches.hole9.is_inactive():
                                self.holes.remove(9)
                        if 14 in self.holes:
                            if self.game.switches.hole14.is_inactive():
                                self.holes.remove(14)
                        if 16 in self.holes:
                            if self.game.switches.hole16.is_inactive():
                                self.holes.remove(16)
                        if 8 in self.holes:
                            if self.game.switches.hole8.is_inactive():
                                self.holes.remove(8)
                        if 5 in self.holes:
                            if self.game.switches.hole5.is_inactive():
                                self.holes.remove(5)
                        if 1 in self.holes:
                            if self.game.switches.hole1.is_inactive():
                                self.holes.remove(1)
                        if 2 in self.holes:
                            if self.game.switches.hole2.is_inactive():
                                self.holes.remove(2)

        self.delay(name="display", delay=0.1, handler=graphics.palm_springs.display, param=self)

    def check_shutter(self, start=0):
        if start == 1 or self.game.hold_feature.position == 8:
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
        self.cancel_delayed(name="both_animation")
        self.cancel_delayed(name="blink_return")
        self.cancel_delayed(name="blink")
        self.cancel_delayed(name="timeout")
        self.game.sound.play('add')
        self.game.search_index.disengage()
        self.game.coils.counter.pulse()
        
        self.game.cu = not self.game.cu
        begin = self.game.spotting.position
        self.game.spotting.spin()
        self.game.mixer1.spin()
        self.game.mixer2.spin()
        self.game.mixer3.spin()
        self.game.mixer4.spin()
        self.game.reflex.decrease()
        if self.game.eb_play.status == False:
            self.animate_both([begin,self.game.spotting.movement_amount,1])
        
        self.game.returned = False
        if self.game.start.status == True:
            if self.game.selector.position < 2:
                self.game.selector.step()
            if self.game.switches.shutter.is_inactive():
                self.game.coils.shutter.enable()
            self.replay_step_down()
            graphics.palm_springs.display(self)
            self.check_lifter_status()
        else:
            self.holes = []
            self.game.start.engage(self.game)
            self.game.coils.redROLamp.disable()
            self.game.coils.yellowROLamp.disable()
            self.game.card1_replay_counter.reset()
            self.game.card2_replay_counter.reset()
            self.game.regular_corners.disengage()
            self.game.super_card1.disengage()
            self.game.super_card2.disengage()
            self.game.spotted_numbers.reset()
            self.game.hold_feature.reset()
            self.game.corners.disengage()
            self.game.corners_replay_counter.reset()
            self.game.start.engage(self.game)
            self.game.selector.reset()
            self.game.ball_count.reset()
            self.game.extra_ball.reset()
            self.game.odds.reset()
            self.game.timer.reset()
            self.game.sound.play_music('motor', -1)
            self.regular_play()
        self.delay(name="display", delay=0.1, handler=graphics.palm_springs.display, param=self)
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
        if self.game.ball_count.position == 5:
            self.game.sound.play('tilt')
        if self.game.ball_count.position >= 5:
            if self.game.search_index.status == False:
                self.search()
        if self.game.ball_count.position <= 7:
            self.check_lifter_status()
        self.delay(name="display", delay=0.1, handler=graphics.palm_springs.display, param=self)


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
            self.delay(name="display", delay=0.1, handler=graphics.palm_springs.display, param=self)

    def sw_hole2_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(2)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.palm_springs.display, param=self)

    def sw_hole3_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(3)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.palm_springs.display, param=self)

    def sw_hole4_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(4)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.palm_springs.display, param=self)

    def sw_hole5_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(5)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.palm_springs.display, param=self)

    def sw_hole6_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(6)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.palm_springs.display, param=self)

    def sw_hole7_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(7)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.palm_springs.display, param=self)

    def sw_hole8_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(8)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.palm_springs.display, param=self)

    def sw_hole9_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(9)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.palm_springs.display, param=self)

    def sw_hole10_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(10)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.palm_springs.display, param=self)

    def sw_hole11_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(11)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.palm_springs.display, param=self)

    def sw_hole12_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(12)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.palm_springs.display, param=self)

    def sw_hole13_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(13)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.palm_springs.display, param=self)

    def sw_hole14_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(14)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.palm_springs.display, param=self)

    def sw_hole15_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(15)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.palm_springs.display, param=self)

    def sw_hole16_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(16)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.palm_springs.display, param=self)

    def sw_hole17_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(17)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.palm_springs.display, param=self)

    def sw_hole18_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(18)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.palm_springs.display, param=self)

    def sw_hole19_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(19)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.palm_springs.display, param=self)

    def sw_hole20_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(20)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.palm_springs.display, param=self)

    def sw_hole21_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(21)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.palm_springs.display, param=self)

    def sw_hole22_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(22)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.palm_springs.display, param=self)

    def sw_hole23_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(23)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.palm_springs.display, param=self)

    def sw_hole24_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(24)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.palm_springs.display, param=self)

    def sw_hole25_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(25)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.palm_springs.display, param=self)

    def sw_replayReset_active(self, sw):
        self.game.anti_cheat.disengage()
        self.holes = []
        graphics.palm_springs.display(self)
        self.tilt_actions()
        self.replay_step_down(self.game.replays)

    def tilt_actions(self):
        self.game.start.disengage()
        self.cancel_delayed(name="replay_reset")
        self.cancel_delayed(name="card1_replay_step_up")
        self.cancel_delayed(name="corners_replay_step_up")
        self.cancel_delayed(name="blink_return")
        self.cancel_delayed(name="blink")
        self.cancel_delayed(name="timeout")
        self.game.coils.redROLamp.disable()
        self.game.coils.yellowROLamp.disable()
        self.game.search_index.disengage()
        if self.game.ball_count.position == 0:
            if self.game.switches.shutter.is_active():
                self.game.coils.shutter.enable()
        self.holes = []
        self.game.selector.reset()
        self.game.card1_replay_counter.reset()
        self.game.card2_replay_counter.reset()
        self.game.corners.disengage()
        self.game.corners_replay_counter.reset()
        self.game.regular_corners.disengage()
        self.game.super_card1.disengage()
        self.game.super_card2.disengage()
        self.game.ball_count.reset()
        self.game.spotted_numbers.reset()
        self.game.hold_feature.reset()
        self.game.odds.reset()
        self.game.eb_play.disengage()
        self.game.extra_ball.reset()
        self.game.anti_cheat.engage(game)
        self.game.tilt.engage(self.game)
        self.game.sound.stop_music()
        self.game.sound.play('tilt')
        # displays "Tilt" on the backglass, you have to recoin.
        self.delay(name="display", delay=0.1, handler=graphics.palm_springs.display, param=self)

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
                graphics.replay_step_down(self.game.replays, graphics.palm_springs.reel1, graphics.palm_springs.reel10, graphics.palm_springs.reel100)
                self.game.coils.registerDown.pulse()
                number -= 1
                graphics.palm_springs.display(self)
                self.delay(name="replay_reset", delay=0.13, handler=self.replay_step_down, param=number)
            elif number == 1:
                self.game.replays -= 1
                graphics.replay_step_down(self.game.replays, graphics.palm_springs.reel1, graphics.palm_springs.reel10, graphics.palm_springs.reel100)
                self.game.coils.registerDown.pulse()
                number -= 1
                graphics.palm_springs.display(self)
                self.cancel_delayed(name="replay_reset")
        else: 
            if self.game.replays > 0:
                self.game.replays -= 1
                graphics.replay_step_down(self.game.replays, graphics.palm_springs.reel1, graphics.palm_springs.reel10, graphics.palm_springs.reel100)
                self.delay(name="display", delay=0.1, handler=graphics.palm_springs.display, param=self)
            self.game.coils.registerDown.pulse()

    def replay_step_up(self):
        if self.game.replays < 899:
            self.game.replays += 1
            graphics.replay_step_up(self.game.replays, graphics.palm_springs.reel1, graphics.palm_springs.reel10, graphics.palm_springs.reel100)
        self.game.coils.registerUp.pulse()
        self.game.coils.sounder.pulse()
        self.game.reflex.increase()
        graphics.palm_springs.display(self)

    def sw_odd_active(self, sw):
        if self.game.switches.drawer.is_active():
            if self.game.hold_feature.position == 8 and self.game.ball_count.position <= 4:
                if 2 in self.holes:
                    if self.game.switches.hole2.is_inactive():
                        self.holes.remove(2)
                    if self.game.spotted_numbers.position >= 8:
                        if self.game.spotted.position == 1:
                            self.holes.append(2)
                if 4 in self.holes:
                    if self.game.switches.hole4.is_inactive():
                        self.holes.remove(4)
                if 6 in self.holes:
                    if self.game.switches.hole6.is_inactive():
                        self.holes.remove(6)
                if 8 in self.holes:
                    if self.game.switches.hole8.is_inactive():
                        self.holes.remove(8)
                    if self.game.spotted_numbers.position >= 10:
                        if self.game.spotted.position == 3:
                            self.holes.append(8)
                if 10 in self.holes:
                    if self.game.switches.hole10.is_inactive():
                        self.holes.remove(10)
                if 12 in self.holes:
                    if self.game.switches.hole12.is_inactive():
                        self.holes.remove(12)
                if 14 in self.holes:
                    if self.game.switches.hole14.is_inactive():
                        self.holes.remove(14)
                    if self.game.spotted_numbers.position >= 12:
                        if self.game.spotted.position == 5:
                            self.holes.append(14)
                if 16 in self.holes:
                    if self.game.switches.hole16.is_inactive():
                        self.holes.remove(16)
                    if self.game.spotted_numbers.position >= 11:
                        if self.game.spotted.position == 4:
                            self.holes.append(16)
                if 18 in self.holes:
                    if self.game.switches.hole18.is_inactive():
                        self.holes.remove(18)
                if 20 in self.holes:
                    if self.game.switches.hole20.is_inactive():
                        self.holes.remove(20)
                if 22 in self.holes:
                    if self.game.switches.hole22.is_inactive():
                        self.holes.remove(22)
                if 24 in self.holes:
                    if self.game.switches.hole24.is_inactive():
                        self.holes.remove(24)
            graphics.palm_springs.display(self)

    def sw_odd_inactive(self, sw):
        if self.game.switches.drawer.is_active():
            if self.game.hold_feature.position == 8 and self.game.ball_count.position <= 4:
                if self.game.switches.hole2.is_active():
                    self.holes.append(2)
                if self.game.spotted_numbers.position >= 8:
                    if self.game.spotted.position == 1:
                        self.holes.append(2)
                if self.game.switches.hole4.is_active():
                    self.holes.append(4)
                if self.game.switches.hole6.is_active():
                    self.holes.append(6)
                if self.game.switches.hole8.is_active():
                    self.holes.append(8)
                if self.game.spotted_numbers.position >= 10:
                    if self.game.spotted.position == 3:
                        self.holes.append(8)
                if self.game.switches.hole10.is_active():
                    self.holes.append(10)
                if self.game.switches.hole12.is_active():
                    self.holes.append(12)
                if self.game.switches.hole14.is_active():
                    self.holes.append(14)
                if self.game.spotted_numbers.position >= 12:
                    if self.game.spotted.position == 5:
                        self.holes.append(14)
                if self.game.switches.hole16.is_active():
                    self.holes.append(16)
                if self.game.spotted_numbers.position >= 11:
                    if self.game.spotted.position == 4:
                        self.holes.append(16)
                if self.game.switches.hole18.is_active():
                    self.holes.append(18)
                if self.game.switches.hole20.is_active():
                    self.holes.append(20)
                if self.game.switches.hole22.is_active():
                    self.holes.append(22)
                if self.game.switches.hole24.is_active():
                    self.holes.append(24)
            graphics.palm_springs.display(self)

    def sw_odd_active_for_2s(self, sw):
        if self.game.switches.drawer.is_active():
            if self.game.hold_feature.position == 8 and self.game.ball_count.position <= 4:
                self.game.coils.holdLeft.enable()
                self.check_shutter()
                self.game.hold_feature.reset()
                self.game.coils.holdLeft.disable()
                if 2 in self.holes:
                    if self.game.switches.hole2.is_inactive():
                        self.holes.remove(2)
                    if self.game.spotted_numbers.position >= 8:
                        if self.game.spotted.position == 1:
                            self.holes.append(2)
                if 4 in self.holes:
                    if self.game.switches.hole4.is_inactive():
                        self.holes.remove(4)
                if 6 in self.holes:
                    if self.game.switches.hole6.is_inactive():
                        self.holes.remove(6)
                if 8 in self.holes:
                    if self.game.switches.hole8.is_inactive():
                        self.holes.remove(8)
                    if self.game.spotted_numbers.position >= 10:
                        if self.game.spotted.position == 3:
                            self.holes.append(8)
                if 10 in self.holes:
                    if self.game.switches.hole10.is_inactive():
                        self.holes.remove(10)
                if 12 in self.holes:
                    if self.game.switches.hole12.is_inactive():
                        self.holes.remove(12)
                if 14 in self.holes:
                    if self.game.switches.hole14.is_inactive():
                        self.holes.remove(14)
                    if self.game.spotted_numbers.position >= 12:
                        if self.game.spotted.position == 5:
                            self.holes.append(14)
                if 16 in self.holes:
                    if self.game.switches.hole16.is_inactive():
                        self.holes.remove(16)
                    if self.game.spotted_numbers.position >= 11:
                        if self.game.spotted.position == 4:
                            self.holes.append(16)
                if 18 in self.holes:
                    if self.game.switches.hole18.is_inactive():
                        self.holes.remove(18)
                if 20 in self.holes:
                    if self.game.switches.hole20.is_inactive():
                        self.holes.remove(20)
                if 22 in self.holes:
                    if self.game.switches.hole22.is_inactive():
                        self.holes.remove(22)
                if 24 in self.holes:
                    if self.game.switches.hole24.is_inactive():
                        self.holes.remove(24)
            graphics.palm_springs.display(self)


    def sw_blue_active(self, sw):
        if self.game.switches.drawer.is_inactive():
            if self.game.hold_feature.position == 8 and self.game.ball_count.position <= 4:
                if 2 in self.holes:
                    if self.game.switches.hole2.is_inactive():
                        self.holes.remove(2)
                    if self.game.spotted_numbers.position >= 8:
                        if self.game.spotted.position == 1:
                            self.holes.append(2)
                if 4 in self.holes:
                    if self.game.switches.hole4.is_inactive():
                        self.holes.remove(4)
                if 6 in self.holes:
                    if self.game.switches.hole6.is_inactive():
                        self.holes.remove(6)
                if 8 in self.holes:
                    if self.game.switches.hole8.is_inactive():
                        self.holes.remove(8)
                    if self.game.spotted_numbers.position >= 10:
                        if self.game.spotted.position == 3:
                            self.holes.append(8)
                if 10 in self.holes:
                    if self.game.switches.hole10.is_inactive():
                        self.holes.remove(10)
                if 12 in self.holes:
                    if self.game.switches.hole12.is_inactive():
                        self.holes.remove(12)
                if 14 in self.holes:
                    if self.game.switches.hole14.is_inactive():
                        self.holes.remove(14)
                    if self.game.spotted_numbers.position >= 12:
                        if self.game.spotted.position == 5:
                            self.holes.append(14)
                if 16 in self.holes:
                    if self.game.switches.hole16.is_inactive():
                        self.holes.remove(16)
                    if self.game.spotted_numbers.position >= 11:
                        if self.game.spotted.position == 4:
                            self.holes.append(16)
                if 18 in self.holes:
                    if self.game.switches.hole18.is_inactive():
                        self.holes.remove(18)
                if 20 in self.holes:
                    if self.game.switches.hole20.is_inactive():
                        self.holes.remove(20)
                if 22 in self.holes:
                    if self.game.switches.hole22.is_inactive():
                        self.holes.remove(22)
                if 24 in self.holes:
                    if self.game.switches.hole24.is_inactive():
                        self.holes.remove(24)
            graphics.palm_springs.display(self)


    def sw_blue_inactive(self, sw):
        if self.game.switches.drawer.is_inactive():
            if self.game.hold_feature.position == 8 and self.game.ball_count.position <= 4:
                if self.game.switches.hole2.is_active():
                    self.holes.append(2)
                if self.game.spotted_numbers.position >= 8:
                    if self.game.spotted.position == 1:
                        self.holes.append(2)
                if self.game.switches.hole4.is_active():
                    self.holes.append(4)
                if self.game.switches.hole6.is_active():
                    self.holes.append(6)
                if self.game.switches.hole8.is_active():
                    self.holes.append(8)
                if self.game.spotted_numbers.position >= 10:
                    if self.game.spotted.position == 3:
                        self.holes.append(8)
                if self.game.switches.hole10.is_active():
                    self.holes.append(10)
                if self.game.switches.hole12.is_active():
                    self.holes.append(12)
                if self.game.switches.hole14.is_active():
                    self.holes.append(14)
                if self.game.spotted_numbers.position >= 12:
                    if self.game.spotted.position == 5:
                        self.holes.append(14)
                if self.game.switches.hole16.is_active():
                    self.holes.append(16)
                if self.game.spotted_numbers.position >= 11:
                    if self.game.spotted.position == 4:
                        self.holes.append(16)
                if self.game.switches.hole18.is_active():
                    self.holes.append(18)
                if self.game.switches.hole20.is_active():
                    self.holes.append(20)
                if self.game.switches.hole22.is_active():
                    self.holes.append(22)
                if self.game.switches.hole24.is_active():
                    self.holes.append(24)
            graphics.palm_springs.display(self)

    def sw_blue_active_for_2s(self, sw):
        if self.game.switches.drawer.is_inactive():
            if self.game.hold_feature.position == 8 and self.game.ball_count.position <= 4:
                self.game.coils.holdLeft.enable()
                self.check_shutter()
                self.game.hold_feature.reset()
                self.game.coils.holdLeft.disable()
                if 2 in self.holes:
                    if self.game.switches.hole2.is_inactive():
                        self.holes.remove(2)
                    if self.game.spotted_numbers.position >= 8:
                        if self.game.spotted.position == 1:
                            self.holes.append(2)
                if 4 in self.holes:
                    if self.game.switches.hole4.is_inactive():
                        self.holes.remove(4)
                if 6 in self.holes:
                    if self.game.switches.hole6.is_inactive():
                        self.holes.remove(6)
                if 8 in self.holes:
                    if self.game.switches.hole8.is_inactive():
                        self.holes.remove(8)
                    if self.game.spotted_numbers.position >= 10:
                        if self.game.spotted.position == 3:
                            self.holes.append(8)
                if 10 in self.holes:
                    if self.game.switches.hole10.is_inactive():
                        self.holes.remove(10)
                if 12 in self.holes:
                    if self.game.switches.hole12.is_inactive():
                        self.holes.remove(12)
                if 14 in self.holes:
                    if self.game.switches.hole14.is_inactive():
                        self.holes.remove(14)
                    if self.game.spotted_numbers.position >= 12:
                        if self.game.spotted.position == 5:
                            self.holes.append(14)
                if 16 in self.holes:
                    if self.game.switches.hole16.is_inactive():
                        self.holes.remove(16)
                    if self.game.spotted_numbers.position >= 11:
                        if self.game.spotted.position == 4:
                            self.holes.append(16)
                if 18 in self.holes:
                    if self.game.switches.hole18.is_inactive():
                        self.holes.remove(18)
                if 20 in self.holes:
                    if self.game.switches.hole20.is_inactive():
                        self.holes.remove(20)
                if 22 in self.holes:
                    if self.game.switches.hole22.is_inactive():
                        self.holes.remove(22)
                if 24 in self.holes:
                    if self.game.switches.hole24.is_inactive():
                        self.holes.remove(24)
            graphics.palm_springs.display(self)

    def sw_even_active(self, sw):
        if self.game.switches.drawer.is_active():
            if self.game.hold_feature.position == 8 and self.game.ball_count.position <= 4:
                if 1 in self.holes:
                    if self.game.switches.hole1.is_inactive():
                        self.holes.remove(1)
                    if self.game.spotted_numbers.position >= 7:
                        if self.game.spotted.position == 0:
                            self.holes.append(1)
                if 3 in self.holes:
                    if self.game.switches.hole3.is_inactive():
                        self.holes.remove(3)
                if 5 in self.holes:
                    if self.game.switches.hole5.is_inactive():
                        self.holes.remove(5)
                    if self.game.spotted_numbers.position >= 9:
                        if self.game.spotted.position == 2:
                            self.holes.append(5)
                if 7 in self.holes:
                    if self.game.switches.hole7.is_inactive():
                        self.holes.remove(7)
                if 9 in self.holes:
                    if self.game.switches.hole9.is_inactive():
                        self.holes.remove(9)
                    if self.game.spotted_numbers.position >= 13:
                        if self.game.spotted.position == 6:
                            self.holes.append(9)
                if 11 in self.holes:
                    if self.game.switches.hole11.is_inactive():
                        self.holes.remove(11)
                if 13 in self.holes:
                    if self.game.switches.hole13.is_inactive():
                        self.holes.remove(13)
                if 15 in self.holes:
                    if self.game.switches.hole15.is_inactive():
                        self.holes.remove(15)
                if 17 in self.holes:
                    if self.game.switches.hole17.is_inactive():
                        self.holes.remove(17)
                if 19 in self.holes:
                    if self.game.switches.hole19.is_inactive():
                        self.holes.remove(19)
                if 21 in self.holes:
                    if self.game.switches.hole21.is_inactive():
                        self.holes.remove(21)
                if 23 in self.holes:
                    if self.game.switches.hole23.is_inactive():
                        self.holes.remove(23)
                if 25 in self.holes:
                    if self.game.switches.hole25.is_inactive():
                        self.holes.remove(25)
            graphics.palm_springs.display(self)

    def sw_even_inactive(self, sw):
        if self.game.switches.drawer.is_active():
            if self.game.hold_feature.position == 8 and self.game.ball_count.position <= 4:
                if self.game.switches.hole1.is_active():
                    self.holes.append(1)
                if self.game.spotted_numbers.position >= 7:
                    if self.game.spotted.position == 0:
                        self.holes.append(1)
                if self.game.switches.hole3.is_active():
                    self.holes.append(3)
                if self.game.switches.hole5.is_active():
                    self.holes.append(5)
                if self.game.spotted_numbers.position >= 9:
                    if self.game.spotted.position == 2:
                        self.holes.append(5)
                if self.game.switches.hole7.is_active():
                    self.holes.append(7)
                if self.game.switches.hole9.is_active():
                    self.holes.append(9)
                if self.game.spotted_numbers.position >= 13:
                    if self.game.spotted.position == 6:
                        self.holes.append(9)
                if self.game.switches.hole11.is_active():
                    self.holes.append(11)
                if self.game.switches.hole13.is_active():
                    self.holes.append(13)
                if self.game.switches.hole15.is_active():
                    self.holes.append(15)
                if self.game.switches.hole17.is_active():
                    self.holes.append(17)
                if self.game.switches.hole19.is_active():
                    self.holes.append(19)
                if self.game.switches.hole21.is_active():
                    self.holes.append(21)
                if self.game.switches.hole23.is_active():
                    self.holes.append(23)
                if self.game.switches.hole25.is_active():
                    self.holes.append(25)
            graphics.palm_springs.display(self)

    def sw_even_active_for_2s(self, sw):
        if self.game.switches.drawer.is_active():
            if self.game.hold_feature.position == 8 and self.game.ball_count.position <= 4:
                self.game.coils.holdRight.enable()
                self.check_shutter()
                self.game.hold_feature.reset()
                self.game.coils.holdRight.disable()
                if 1 in self.holes:
                    if self.game.switches.hole1.is_inactive():
                        self.holes.remove(1)
                    if self.game.spotted_numbers.position >= 7:
                        if self.game.spotted.position == 0:
                            self.holes.append(1)
                if 3 in self.holes:
                    if self.game.switches.hole3.is_inactive():
                        self.holes.remove(3)
                if 5 in self.holes:
                    if self.game.switches.hole5.is_inactive():
                        self.holes.remove(5)
                    if self.game.spotted_numbers.position >= 9:
                        if self.game.spotted.position == 2:
                            self.holes.append(5)
                if 7 in self.holes:
                    if self.game.switches.hole7.is_inactive():
                        self.holes.remove(7)
                if 9 in self.holes:
                    if self.game.switches.hole9.is_inactive():
                        self.holes.remove(9)
                    if self.game.spotted_numbers.position >= 13:
                        if self.game.spotted.position == 6:
                            self.holes.append(9)
                if 11 in self.holes:
                    if self.game.switches.hole11.is_inactive():
                        self.holes.remove(11)
                if 13 in self.holes:
                    if self.game.switches.hole13.is_inactive():
                        self.holes.remove(13)
                if 15 in self.holes:
                    if self.game.switches.hole15.is_inactive():
                        self.holes.remove(15)
                if 17 in self.holes:
                    if self.game.switches.hole17.is_inactive():
                        self.holes.remove(17)
                if 19 in self.holes:
                    if self.game.switches.hole19.is_inactive():
                        self.holes.remove(19)
                if 21 in self.holes:
                    if self.game.switches.hole21.is_inactive():
                        self.holes.remove(21)
                if 23 in self.holes:
                    if self.game.switches.hole23.is_inactive():
                        self.holes.remove(23)
                if 25 in self.holes:
                    if self.game.switches.hole25.is_inactive():
                        self.holes.remove(25)
            graphics.palm_springs.display(self)

    def sw_green_active(self, sw):
        if self.game.switches.drawer.is_inactive():
            if self.game.hold_feature.position == 8 and self.game.ball_count.position <= 4:
                if 1 in self.holes:
                    if self.game.switches.hole1.is_inactive():
                        self.holes.remove(1)
                    if self.game.spotted_numbers.position >= 7:
                        if self.game.spotted.position == 0:
                            self.holes.append(1)
                if 3 in self.holes:
                    if self.game.switches.hole3.is_inactive():
                        self.holes.remove(3)
                if 5 in self.holes:
                    if self.game.switches.hole5.is_inactive():
                        self.holes.remove(5)
                    if self.game.spotted_numbers.position >= 9:
                        if self.game.spotted.position == 2:
                            self.holes.append(5)
                if 7 in self.holes:
                    if self.game.switches.hole7.is_inactive():
                        self.holes.remove(7)
                if 9 in self.holes:
                    if self.game.switches.hole9.is_inactive():
                        self.holes.remove(9)
                    if self.game.spotted_numbers.position >= 13:
                        if self.game.spotted.position == 6:
                            self.holes.append(9)
                if 11 in self.holes:
                    if self.game.switches.hole11.is_inactive():
                        self.holes.remove(11)
                if 13 in self.holes:
                    if self.game.switches.hole13.is_inactive():
                        self.holes.remove(13)
                if 15 in self.holes:
                    if self.game.switches.hole15.is_inactive():
                        self.holes.remove(15)
                if 17 in self.holes:
                    if self.game.switches.hole17.is_inactive():
                        self.holes.remove(17)
                if 19 in self.holes:
                    if self.game.switches.hole19.is_inactive():
                        self.holes.remove(19)
                if 21 in self.holes:
                    if self.game.switches.hole21.is_inactive():
                        self.holes.remove(21)
                if 23 in self.holes:
                    if self.game.switches.hole23.is_inactive():
                        self.holes.remove(23)
                if 25 in self.holes:
                    if self.game.switches.hole25.is_inactive():
                        self.holes.remove(25)
            graphics.palm_springs.display(self)

    def sw_green_inactive(self, sw):
        if self.game.switches.drawer.is_inactive():
            if self.game.hold_feature.position == 8 and self.game.ball_count.position <= 4:
                if self.game.switches.hole1.is_active():
                    self.holes.append(1)
                if self.game.spotted_numbers.position >= 7:
                    if self.game.spotted.position == 0:
                        self.holes.append(1)
                if self.game.switches.hole3.is_active():
                    self.holes.append(3)
                if self.game.switches.hole5.is_active():
                    self.holes.append(5)
                if self.game.spotted_numbers.position >= 9:
                    if self.game.spotted.position == 2:
                        self.holes.append(5)
                if self.game.switches.hole7.is_active():
                    self.holes.append(7)
                if self.game.switches.hole9.is_active():
                    self.holes.append(9)
                if self.game.spotted_numbers.position >= 13:
                    if self.game.spotted.position == 6:
                        self.holes.append(9)
                if self.game.switches.hole11.is_active():
                    self.holes.append(11)
                if self.game.switches.hole13.is_active():
                    self.holes.append(13)
                if self.game.switches.hole15.is_active():
                    self.holes.append(15)
                if self.game.switches.hole17.is_active():
                    self.holes.append(17)
                if self.game.switches.hole19.is_active():
                    self.holes.append(19)
                if self.game.switches.hole21.is_active():
                    self.holes.append(21)
                if self.game.switches.hole23.is_active():
                    self.holes.append(23)
                if self.game.switches.hole25.is_active():
                    self.holes.append(25)
            graphics.palm_springs.display(self)


    def sw_green_active_for_2s(self, sw):
        if self.game.switches.drawer.is_inactive():
            if self.game.hold_feature.position == 8 and self.game.ball_count.position <= 4:
                self.game.coils.holdRight.enable()
                self.check_shutter()
                self.game.hold_feature.reset()
                self.game.coils.holdRight.disable()
                if 1 in self.holes:
                    if self.game.switches.hole1.is_inactive():
                        self.holes.remove(1)
                    if self.game.spotted_numbers.position >= 7:
                        if self.game.spotted.position == 0:
                            self.holes.append(1)
                if 3 in self.holes:
                    if self.game.switches.hole3.is_inactive():
                        self.holes.remove(3)
                if 5 in self.holes:
                    if self.game.switches.hole5.is_inactive():
                        self.holes.remove(5)
                    if self.game.spotted_numbers.position >= 9:
                        if self.game.spotted.position == 2:
                            self.holes.append(5)
                if 7 in self.holes:
                    if self.game.switches.hole7.is_inactive():
                        self.holes.remove(7)
                if 9 in self.holes:
                    if self.game.switches.hole9.is_inactive():
                        self.holes.remove(9)
                    if self.game.spotted_numbers.position >= 13:
                        if self.game.spotted.position == 6:
                            self.holes.append(9)
                if 11 in self.holes:
                    if self.game.switches.hole11.is_inactive():
                        self.holes.remove(11)
                if 13 in self.holes:
                    if self.game.switches.hole13.is_inactive():
                        self.holes.remove(13)
                if 15 in self.holes:
                    if self.game.switches.hole15.is_inactive():
                        self.holes.remove(15)
                if 17 in self.holes:
                    if self.game.switches.hole17.is_inactive():
                        self.holes.remove(17)
                if 19 in self.holes:
                    if self.game.switches.hole19.is_inactive():
                        self.holes.remove(19)
                if 21 in self.holes:
                    if self.game.switches.hole21.is_inactive():
                        self.holes.remove(21)
                if 23 in self.holes:
                    if self.game.switches.hole23.is_inactive():
                        self.holes.remove(23)
                if 25 in self.holes:
                    if self.game.switches.hole25.is_inactive():
                        self.holes.remove(25)
            graphics.palm_springs.display(self)

    def sw_yellow_active(self, sw):
        if self.game.ball_count.position >= 5:
            if self.game.eb_play.status == True and (self.game.replays > 0 or self.game.switches.freeplay.is_active()):
                self.cancel_delayed("eb_animation")
                self.game.sound.stop('add')
                self.game.sound.play('add')
                self.game.cu = not self.game.cu
                begin = self.game.spotting.position
                self.game.spotting.spin()
                self.animate_eb_scan([begin,self.game.spotting.movement_amount,self.game.spotting.movement_amount])
                self.game.mixer1.spin()
                self.game.mixer2.spin()
                self.game.mixer3.spin()
                self.game.mixer4.spin()
                self.replay_step_down()
                self.game.reflex.decrease()
                self.game.coils.counter.pulse()
                graphics.palm_springs.display(self)
                self.game.eb_play.disengage()
                graphics.palm_springs.display(self)
                return
            if self.game.eb_play.status == False:
                self.game.eb_play.engage(self.game)
                graphics.palm_springs.display(self)
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
                        if self.game.super_card1.status == True:
                            if self.game.card1_replay_counter.position < fourodds:
                                self.game.search_index.engage(self.game)
                                self.card1_replay_step_up(fourodds - self.game.card1_replay_counter.position)
                    elif supercard == 2:
                        if self.game.super_card2.status == True:
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
                        if supercard == 1 or supercard == 2:
                            pass
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

    def corners_replay_step_up(self, number):
        self.game.sound.stop_music()
        if number >= 1:
            self.game.corners_replay_counter.step()
            number -= 1
            self.replay_step_up()
            if self.game.replays == 899:
                number = 0
            self.delay(name="corners_replay_step_up", delay=0.25, handler=self.corners_replay_step_up, param=number)
        else:
            self.game.search_index.disengage()
            self.cancel_delayed(name="corners_replay_step_up")
            self.search_sounds()
            self.search()

    def sc_replay_step_up(self, number):
        self.game.sound.stop_music()
        if number >= 1:
            self.game.sc_replay_counter.step()
            number -= 1
            self.replay_step_up()
            if self.game.replays == 899:
                number = 0
            self.delay(name="sc_replay_step_up", delay=0.25, handler=self.sc_replay_step_up, param=number)
        else:
            self.game.search_index.disengage()
            self.cancel_delayed(name="sc_replay_step_up")
            self.search_sounds()
            self.search()

    def closed_search_relays(self, rivets, c):
        # This function is critical, as it will determine which card is returned, etc.  I need to check the position of the
        # replay counter for the card. We will get a row back
        # that has the numbers on the position which will return the search relay connected.  When three out of the five relays
        # are connected, we get a winner!
        
        self.pos = {}
        # Card 1
        self.pos[0] = {}
        self.pos[1] = {18:1, 4:2, 8:3, 16:4, 6:5}
        self.pos[2] = {10:1, 24:2, 12:3, 20:4, 19:5}
        self.pos[3] = {2:1, 14:2, 15:3, 9:4, 1:5}
        self.pos[4] = {13:1, 22:2, 25:3, 21:4, 17:5}
        self.pos[5] = {11:1, 7:2, 5:3, 23:4, 3:5}
        self.pos[6] = {18:1, 10:2, 2:3, 13:4, 11:5}
        self.pos[7] = {4:1, 24:2, 14:3, 22:4, 7:5}
        self.pos[8] = {8:1, 12:2, 15:3, 25:4, 5:5}
        self.pos[9] = {16:1, 20:2, 9:3, 21:4, 23:5}
        self.pos[10] = {6:1, 19:2, 1:3, 17:4, 3:5}
        self.pos[11] = {18:1, 24:2, 15:3, 21:4, 3:5}
        self.pos[12] = {6:1, 20:2, 15:3, 22:4, 11:5}
        self.pos[13] = {}
        self.pos[14] = {20:1, 4:2, 22:3}
        self.pos[15] = {10:1, 14:2, 6:3}
        self.pos[16] = {12:1, 24:2, 18:3}
        self.pos[17] = {20:1, 10:2, 12:3}
        self.pos[18] = {4:1, 14:2, 24:3}
        self.pos[19] = {22:1, 6:2, 18:3}
        self.pos[20] = {20:1, 14:2, 18:3}
        self.pos[21] = {22:1, 14:2, 12:3}
        self.pos[22] = {}
        self.pos[23] = {15:1, 7:2, 23:3}
        self.pos[24] = {3:1, 9:2, 13:3}
        self.pos[25] = {17:1, 11:2, 19:3}
        self.pos[26] = {15:1, 3:2, 17:3}
        self.pos[27] = {7:1, 9:2, 11:3}
        self.pos[28] = {23:1, 13:2, 19:3}
        self.pos[29] = {15:1, 9:2, 19:3}
        self.pos[30] = {23:1, 9:2, 17:3}
        self.pos[31] = {}
        self.pos[32] = {18:1, 6:2, 11:3, 3:4}
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
        sc = 0
        card = 1

        if rivets == 32:
            corners = True
        if rivets in range(14,22):
            sc = 1
        if rivets in range(23,31):
            sc = 2

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

    def scan_odds(self):
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
            self.delay(name="display", delay=0, handler=graphics.palm_springs.display, param=self)
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
            if self.game.odds.position == 4:
                if sd in [8,15,42,49]:
                    return 1
            elif self.game.odds.position == 5:
                if sd in [2,12]:
                    return 1
            elif self.game.odds.position == 6:
                if sd in [4,32,44]:
                    return 1
            elif self.game.odds.position == 7:
                if sd in [7,35,48]:
                    return 1
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
        if self.game.super_card1.status == False and self.game.super_card2.status == False:
            if mix3 in [10,21,24,23]:
                return 1
        if self.game.super_card1.status == False or self.game.super_card2.status == False:
            if mix3 in [6,12,13]:
                return 1
        if mix3 in [1,2,3,4]:
            return 1
        if self.game.hold_feature.position <= 7:
            if mix3 in [5,10,11]:
                return 1
        if mix3 == 6:
            if self.game.spotted.position not in [5,6]:
                return 1
        return 0

    def scan_features(self):
        p = self.features_probability()

    def features_probability(self):
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

    def features_spotting(self):
        sd = self.game.spotting.position
        if sd == 15:
            if self.game.corners.status == False:
                self.game.corners.engage(self.game)
                self.game.sound.play('tilt')
        if sd in [14,22,36,44]:
            if sd == 22:
                if self.game.reflex.connected_rivet() <= 4:
                    if self.game.cu:
                        if self.game.super_card2.status == False:
                            self.game.super_card2.engage(self.game)
                            self.game.sound.play('tilt')
                    else:
                        if self.game.super_card1.status == False:
                            self.game.super_card1.engage(self.game)
                            self.game.sound.play('tilt')
            else:
                if self.game.cu:
                    if self.game.super_card2.status == False:
                        self.game.super_card2.engage(self.game)
                        self.game.sound.play('tilt')
                else:
                    if self.game.super_card1.status == False:
                        self.game.super_card1.engage(self.game)
                        self.game.sound.play('tilt')
        # CHECK SPOTTED NUMBERS
        if sd == 6:
            if self.game.spotted_numbers.position < 10:
                self.step_spotted_numbers(10 - self.game.spotted_numbers.position)
                self.check_spot()
        if self.game.reflex.connected_rivet() <= 4:
            if sd == 11:
                self.step_spotted_numbers(13)
                self.check_spot()
        if sd == 25:
            if self.game.spotted_numbers.position < 13:
                self.step_spotted_numbers(13 - self.game.spotted_numbers.position)
                self.check_spot()
        if self.game.spotted_numbers.position < 10:
            if self.game.cu:
                self.step_spotted_numbers(1)
                self.check_spot()
            else:
                self.step_hold_feature(1)
        if sd == 7:
            if self.game.spotted_numbers.position == 10:
                self.step_spotted_numbers(13)
                self.check_spot()
        if sd == 5:
            self.step_hold_feature(8)
        if sd == 33:
            self.step_hold_feature(6 - self.game.hold_feature.position)
        if sd == 3:
            self.step_hold_feature(4 - self.game.hold_feature.position)
        if self.game.spotting.position == 10:
            if self.game.spotted_numbers.position > 10:
                self.game.spotted_numbers.step()
                self.check_spot()
        
    def step_spotted_numbers(self, number):
            if number >= 1:
                self.game.spotted_numbers.step()
                self.check_spot()
                number -= 1
                if self.game.spotted_numbers.position == 6:
                    number = 2
                self.delay(name="display", delay=0.1, handler=graphics.palm_springs.display, param=self)
                self.delay(name="step_spotted_numbers", delay=0.1, handler=self.step_spotted_numbers, param=number)

    def step_hold_feature(self, number):
            if number >= 1:
                self.game.hold_feature.step()
                number -= 1
                self.delay(name="display", delay=0.1, handler=graphics.palm_springs.display, param=self)
                self.delay(name="step_hold_feature", delay=0.1, handler=self.step_hold_feature, param=number)

    def scan_eb(self):
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
        self.delay(name="display", delay=0.1, handler=graphics.palm_springs.display, param=self)

    def animate_both(self, args):
        start = args[0]
        diff = args[1]
        num = args[2]
        if start + num >= 50:
            start = 0
        if diff >= 0:
            num = num + 1
            graphics.palm_springs.both_animation([self, start + num])
            self.cancel_delayed(name="display")
            diff = diff - 1
            args = [start,diff,num]
            self.delay(name="both_animation", delay=0.08, handler=self.animate_both, param=args)
        else:
            self.cancel_delayed(name="both_animation")
            self.delay(name="display", delay=0.1, handler=graphics.palm_springs.display, param=self)
            self.scan_all()

    def animate_eb_scan(self, args):
        start = args[0]
        diff = args[1]
        num = args[2]
        if start + num >= 50:
            start = 0
        if diff >= 0:
            num = num + 1
            graphics.palm_springs.eb_animation([self, start + num])
            self.cancel_delayed(name="display")
            diff = diff - 1
            args = [start,diff,num]
            self.delay(name="eb_animation", delay=0.08, handler=self.animate_eb_scan, param=args)
        else:
            self.cancel_delayed(name="eb_animation")
            self.game.eb_play.disengage()
            self.delay(name="display", delay=0.1, handler=graphics.palm_springs.display, param=self)
            self.scan_eb()


    def check_eb_spotting(self):
        sd = self.game.spotting.position
        if sd == 50:
            self.step_eb(9 - self.game.extra_ball.position)
        elif sd == 1:
            self.step_eb(3 - self.game.extra_ball.position)
        elif sd == 6:
            if self.game.extra_ball.position < 6:
                self.step_eb(6 - self.game.extra_ball.position)
            else:
                self.step_eb(9 - self.game.extra_ball.position)
        else:
            if self.game.mixer4.position in [2,8]:
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
            self.delay(name="display", delay=0.1, handler=graphics.palm_springs.display, param=self)
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

class PalmSprings(procgame.game.BasicGame):
    """ Palm Springs was the first game with the ball return feature """
    def __init__(self, machine_type):
        super(PalmSprings, self).__init__(machine_type)
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
        self.odds = units.Stepper("odds", 8, 'palm_springs')

        #Replay Counter
        self.card1_replay_counter = units.Stepper("card1_replay_counter", 500)
        self.card2_replay_counter = units.Stepper("card1_replay_counter", 500)
        #Corners Replay Counter
        self.corners_replay_counter = units.Stepper("corners_replay_counter", 400)
        self.sc_replay_counter = units.Stepper("sc_replay_counter", 400)

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
        self.spotted_numbers = units.Stepper("spotted_numbers", 13)
        self.hold_feature = units.Stepper("hold_feature", 8)
        self.super_card1 = units.Relay("super_card1")
        self.super_card2 = units.Relay("super_card2")
        self.spotted = units.Stepper("spotted", 6, "palm_springs", "continuous")
        self.regular_corners = units.Relay("regular_corners")

        self.replays = 0
        self.returned = False

    def reset(self):
        super(PalmSprings, self).reset()
        self.logger = logging.getLogger('game')
        self.load_config('bingo.yaml')
        
        main_mode = SinglecardBingo(self)
        self.modes.add(main_mode)
        
game = PalmSprings(machine_type='pdb')
game.reset()
game.run_loop()
