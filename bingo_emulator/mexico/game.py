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
from bingo_emulator.graphics.mexico import *

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
        if self.game.eb_play.status == True and self.game.tilt.status == False:
            self.game.sound.stop('add')
            self.game.sound.play('add')
            self.scan_eb()
            self.game.eb_play.disengage()
        else:
            self.game.tilt.disengage()
            self.regular_play()
            self.scan_all()
        self.delay(name="display", delay=0.1, handler=graphics.mexico.display, param=self)

    def sw_startButton_active(self, sw):
        if self.game.replays > 0 or self.game.switches.freeplay.is_active():
            self.game.tilt.disengage()
            self.regular_play()
            self.scan_all()
            self.delay(name="display", delay=0.1, handler=graphics.mexico.display, param=self)

    def sw_trough4_active_for_1s(self, sw):
        if self.game.ball_count.position >= 5:
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
        if self.game.letter_xi.status == False:
            self.game.letter_xi.engage(self.game)
            self.search()

    def sw_enter_active(self, sw):
        if self.game.switches.left.is_active() and self.game.switches.right.is_active():
            self.game.end_run_loop()
            os.system("/home/nbaldridge/proc/bingo_emulator/start_game.sh mexico")
        else:
            if self.game.ball_return.position == 7 and self.game.card1_replay_counter.position == 0:
                self.regular_play(True)

    def sw_left_active(self, sw):
        max_ball = 4
        if self.game.before_fifth.status == True:
            max_ball = 5

        if self.game.selection_feature_relay.status == True and self.game.select_spots.status == False:
            if self.game.ball_count.position < max_ball:
                self.game.spotted.stepdown()

        if self.game.select_spots.status == True:
            if self.game.ball_count.position < max_ball:
                self.game.spotted.stepdown()
                if self.game.selection_feature.position == 6:
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
                elif self.game.selection_feature.position == 11: 
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


        self.delay(name="display", delay=0.1, handler=graphics.mexico.display, param=self)
        print self.holes

    def sw_right_active(self, sw):
        max_ball = 4
        if self.game.before_fifth.status == True:
            max_ball = 5

        if self.game.selection_feature_relay.status == True and self.game.select_spots.status == False:
            if self.game.ball_count.position < max_ball:
                self.game.spotted.step()

        if self.game.select_spots.status == True:
            if self.game.ball_count.position < max_ball:
                self.game.spotted.step()
                if self.game.selection_feature.position == 6:
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
                elif self.game.selection_feature.position == 11:
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

        self.delay(name="display", delay=0.1, handler=graphics.mexico.display, param=self)

    def sw_redstar_active(self, sw):
        if self.game.red_star.status == True:
            if self.game.all_spot.status == False:
                self.game.all_spot.engage(self.game)
                if 2 not in self.holes:
                    self.holes.append(2)
                if 5 not in self.holes:
                    self.holes.append(5)
                if 8 not in self.holes:
                    self.holes.append(8)
            if self.game.ball_count.position >= 5:
                self.search()
        if self.game.letter_co.status == False:
            self.game.letter_co.engage(self.game)
            self.search()
        self.delay(name="display", delay=0.1, handler=graphics.mexico.display, param=self)

    def sw_yellowstar_active(self, sw):
        if self.game.yellow_star.status == True:
            if self.game.all_spot.status == False:
                self.game.all_spot.engage(self.game)
                if 2 not in self.holes:
                    self.holes.append(2)
                if 5 not in self.holes:
                    self.holes.append(5)
                if 8 not in self.holes:
                    self.holes.append(8)
            if self.game.ball_count.position >= 5:
                self.search()

        if self.game.letter_me.status == False:
            self.game.letter_me.engage(self.game)
            self.search()
        self.delay(name="display", delay=0.1, handler=graphics.mexico.display, param=self)
        

    def check_shutter(self, start=0):
        if start == 1:
            if self.game.switches.smRunout.is_active():
                if self.game.switches.shutter.is_active():
                    self.game.coils.shutter.disable()
        else:
            if self.game.switches.shutter.is_inactive():
                if self.game.switches.smRunout.is_active():
                    self.game.coils.shutter.disable()

    def regular_play(self, ball_return=False):
        self.cancel_delayed(name="search")
        self.cancel_delayed(name="lifter_status")
        self.cancel_delayed(name="card1_replay_step_up")
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
            self.game.reflex1.step()
            self.game.reflex2.step()
            
            current = self.game.flash.connected_rivet()
            self.game.flash.spin()
            new = self.game.flash.connected_rivet()
            #NO docs for this - just fudging based on an earlier game
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
        elif ball_return == True:
            self.holes = []
            self.game.start.engage(self.game)
            self.game.card1_replay_counter.reset()
            self.game.start.engage(self.game)
            self.game.selector.reset()
            self.game.timer.reset()
            self.game.ball_count.reset()
            self.game.extra_ball.reset()
            self.game.ball_return.reset()
            self.game.sound.play_music('motor', -1)
            self.regular_play()
        else:
            self.holes = []
            self.game.start.engage(self.game)
            self.game.card1_replay_counter.reset()
            self.game.corners.disengage()
            self.game.letter_me.disengage()
            self.game.letter_xi.disengage()
            self.game.letter_co.disengage()
            self.game.left_special_card.disengage()
            self.game.right_special_card.disengage()
            self.game.before_fourth.disengage()
            self.game.before_fifth.disengage()
            self.game.three_as_four.disengage()
            self.game.coils.redROLamp.disable()
            self.game.coils.yellowROLamp.disable()
            self.game.super_card.reset()
            self.game.selection_feature_relay.disengage()
            self.game.odds.reset()
            self.game.selection_feature.reset()
            self.game.select_spots.disengage()
            self.game.start.engage(self.game)
            self.game.selector.reset()
            self.game.timer.reset()
            self.game.ball_return.reset()
            self.game.ball_count.reset()
            self.game.extra_ball.reset()
            self.game.sound.play_music('motor', -1)
            self.game.before_fourth.engage(self.game)
            self.regular_play()

        self.delay(name="display", delay=0.1, handler=graphics.mexico.display, param=self)
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
                        if self.game.extra_ball.position >= 5 and self.game.ball_count.position <= 5:
                            if self.game.switches.shooter.is_inactive() and self.game.switches.trough3.is_active():
                                self.game.coils.lifter.enable()
                    if self.game.switches.trough3.is_inactive():
                        if self.game.extra_ball.position >= 10 and self.game.ball_count.position <= 6:
                            if self.game.switches.shooter.is_inactive() and self.game.switches.trough2.is_active():
                                self.game.coils.lifter.enable()
                    if self.game.switches.trough2.is_inactive() and self.game.ball_count.position <= 7:
                        if self.game.extra_ball.position >= 15:
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
        if self.game.ball_count.position >= 4:
            if self.game.before_fourth.status == True:
                self.game.before_fourth.disengage()
        if self.game.ball_count.position >= 5:
            if self.game.before_fifth.status == True:
                self.game.before_fifth.disengage()
            if self.game.search_index.status == False:
                self.search()
        if self.game.selection_feature_relay.status == True:
            if self.game.before_fourth.status == False and self.game.before_fifth.status == False:
                if self.game.spotted.position == 7:
                    self.step_eb(15 - self.game.extra_ball.position)
                if self.game.spotted.position == 8:
                    self.game.three_as_four.engage(self.game)
                if self.game.spotted.position == 9:
                    self.step_sc(8 - self.game.super_card.position)
                if self.game.spotted.position == 10:
                    self.game.left_special_card.engage(self.game)
                    self.game.right_special_card.engage(self.game)
        self.delay(name="display", delay=0.1, handler=graphics.mexico.display, param=self)

    # This is really nasty, but it is how we render graphics for each individual hole.
    # numbers are added (or removed from) a list.  In this way, I can re-use the same
    # routine even for games where there are ball return functions like Surf Club.

    def sw_hole1_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(1)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.mexico.display, param=self)

    def sw_hole2_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(2)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.mexico.display, param=self)

    def sw_hole3_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(3)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.mexico.display, param=self)

    def sw_hole4_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(4)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.mexico.display, param=self)

    def sw_hole5_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(5)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.mexico.display, param=self)

    def sw_hole6_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(6)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.mexico.display, param=self)

    def sw_hole7_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(7)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.mexico.display, param=self)

    def sw_hole8_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(8)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.mexico.display, param=self)

    def sw_hole9_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(9)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.mexico.display, param=self)

    def sw_hole10_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(10)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.mexico.display, param=self)

    def sw_hole11_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(11)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.mexico.display, param=self)

    def sw_hole12_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(12)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.mexico.display, param=self)

    def sw_hole13_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(13)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.mexico.display, param=self)

    def sw_hole14_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(14)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.mexico.display, param=self)

    def sw_hole15_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(15)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.mexico.display, param=self)

    def sw_hole16_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(16)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.mexico.display, param=self)

    def sw_hole17_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(17)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.mexico.display, param=self)

    def sw_hole18_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(18)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.mexico.display, param=self)

    def sw_hole19_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(19)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.mexico.display, param=self)

    def sw_hole20_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(20)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.mexico.display, param=self)

    def sw_hole21_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(21)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.mexico.display, param=self)

    def sw_hole22_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(22)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.mexico.display, param=self)

    def sw_hole23_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(23)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.mexico.display, param=self)

    def sw_hole24_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(24)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.mexico.display, param=self)

    def sw_hole25_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(25)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.mexico.display, param=self)
    
    def sw_replayReset_active(self, sw):
        self.game.anti_cheat.disengage()
        self.holes = []
#        self.cancel_delayed(name="blink_title")
        graphics.mexico.display(self)
        self.tilt_actions()
#        self.delay(name="blink_title", delay=1, handler=self.blink_title)
        self.replay_step_down(self.game.replays)

    def tilt_actions(self):
        self.game.start.disengage()
        self.cancel_delayed(name="replay_reset")
        self.cancel_delayed(name="card1_replay_step_up")
        self.game.search_index.disengage()
        if self.game.switches.shutter.is_active() and self.game.ball_count.position == 0:
            self.game.coils.shutter.enable()
        self.holes = []
        self.game.selector.reset()
        self.game.extra_ball.reset()
        self.game.corners.disengage()
        self.game.letter_me.disengage()
        self.game.letter_xi.disengage()
        self.game.letter_co.disengage()
        self.game.before_fourth.disengage()
        self.game.before_fifth.disengage()
        self.game.coils.redROLamp.disable()
        self.game.coils.yellowROLamp.disable()
        self.game.super_card.reset()
        self.game.ball_return.reset()
        self.game.three_as_four.disengage()
        self.game.left_special_card.disengage()
        self.game.right_special_card.disengage()
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
        self.delay(name="display", delay=0.1, handler=graphics.mexico.display, param=self)

    def sw_tilt_active(self, sw):
        if self.game.tilt.status == False:
            self.tilt_actions()

    def replay_step_down(self, number=0):
        if number > 0:
            if number > 1:
                self.game.replays -= 1
                graphics.replay_step_down(self.game.replays, graphics.mexico.reel1, graphics.mexico.reel10, graphics.mexico.reel100)
                self.game.coils.registerDown.pulse()
                number -= 1
                graphics.mexico.display(self)
                self.delay(name="replay_reset", delay=0.0, handler=self.replay_step_down, param=number)
            elif number == 1:
                self.game.replays -= 1
                graphics.replay_step_down(self.game.replays, graphics.mexico.reel1, graphics.mexico.reel10, graphics.mexico.reel100)
                self.game.coils.registerDown.pulse()
                number -= 1
                graphics.mexico.display(self)
                self.cancel_delayed(name="replay_reset")
        else: 
            if self.game.replays > 0:
                self.game.replays -= 1
                graphics.replay_step_down(self.game.replays, graphics.mexico.reel1, graphics.mexico.reel10, graphics.mexico.reel100)
                self.delay(name="display", delay=0.1, handler=graphics.mexico.display, param=self)
            self.game.coils.registerDown.pulse()

    def replay_step_up(self):
        if self.game.replays < 899:
            self.game.replays += 1
            graphics.replay_step_up(self.game.replays, graphics.mexico.reel1, graphics.mexico.reel10, graphics.mexico.reel100)
        self.game.coils.registerUp.pulse()
        self.game.coils.bell.pulse()
        self.game.reflex1.stepdown()
        graphics.mexico.display(self)

    def sw_yellow_active(self, sw):
        if self.game.ball_count.position >= 4:
            if self.game.eb_play.status == False:
                self.game.eb_play.engage(self.game)
                self.delay(name="display", delay=0.1, handler=graphics.mexico.display, param=self)
            if self.game.eb_play.status == True and (self.game.replays > 0 or self.game.switches.freeplay.is_active()):
                self.replay_step_down()
                self.game.sound.stop('add')
                self.game.sound.play('add')
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
                
                self.scan_eb()
                self.delay(name="display", delay=0.1, handler=graphics.mexico.display, param=self)
                self.game.eb_play.disengage()
                self.delay(name="display", delay=0.1, handler=graphics.mexico.display, param=self)
  

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
            self.r = self.closed_search_relays(self.game.searchdisc.position, self.game.corners.status)
            self.game.searchdisc.spin()
            self.wipers = self.r[0]
            self.card = self.r[1]
            self.corners = self.r[2]
            self.supercard = self.r[3]
            self.left_specialcard = self.r[4]
            self.right_specialcard = self.r[5]

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
                                self.find_winner(s, self.card, self.corners, self.supercard, self.left_specialcard, self.right_specialcard)
                                break
        if self.game.letter_me.status == True and self.game.letter_xi.status == True:
            self.find_winner(0, 1, 0, 0, 0, 0, 2)
        if self.game.letter_me.status == True and self.game.letter_xi.status == True and self.game.letter_co.status == True:
            self.find_winner(0, 1, 0, 0, 0, 0, 3)
#        self.delay(name="blink_title", delay=3, handler=self.blink_title)

    def find_winner(self, relays, card, corners, supercard, left_specialcard, right_specialcard, name=0):
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


            if name == 2:
                if self.game.card1_replay_counter.position < threeodds:
                    self.game.search_index.engage(self.game)
                    self.card1_replay_step_up(threeodds - self.game.card1_replay_counter.position)
            if name == 3:
                if self.game.card1_replay_counter.position < fourodds:
                            self.game.search_index.engage(self.game)
                            self.card1_replay_step_up(fourodds - self.game.card1_replay_counter.position)
            if relays == 2:
                if left_specialcard == 1:
                    if self.game.left_special_card.status == True:
                        if self.game.card1_replay_counter.position < threeodds:
                            self.game.search_index.engage(self.game)
                            self.card1_replay_step_up(threeodds - self.game.card1_replay_counter.position)
                elif right_specialcard == 1:
                    if self.game.right_special_card.status == True:
                        if self.game.card1_replay_counter.position < threeodds:
                            self.game.search_index.engage(self.game)
                            self.card1_replay_step_up(threeodds - self.game.card1_replay_counter.position)
            if relays == 3:
                if left_specialcard == 1:
                    if self.game.left_special_card.status == True:
                        if self.game.card1_replay_counter.position < fourodds:
                            self.game.search_index.engage(self.game)
                            self.card1_replay_step_up(fourodds - self.game.card1_replay_counter.position)
                elif right_specialcard == 1:
                    if self.game.right_special_card.status == True:
                        if self.game.card1_replay_counter.position < fourodds:
                            self.game.search_index.engage(self.game)
                            self.card1_replay_step_up(fourodds - self.game.card1_replay_counter.position)
                if supercard == 1:
                    if self.game.super_card.position >= 4:
                        if self.game.card1_replay_counter.position < fourodds:
                            self.game.search_index.engage(self.game)
                            self.card1_replay_step_up(fourodds - self.game.card1_replay_counter.position)
                elif supercard == 2:
                    if self.game.super_card.position == 8:
                        if self.game.card1_replay_counter.position < fourodds:
                            self.game.search_index.engage(self.game)
                            self.card1_replay_step_up(fourodds - self.game.card1_replay_counter.position)
                else:
                    if not corners:
                        if self.game.three_as_four.status == True:
                            if self.game.card1_replay_counter.position < fourodds:
                                self.game.search_index.engage(self.game)
                                self.card1_replay_step_up(fourodds - self.game.card1_replay_counter.position)
                        else:
                            if self.game.card1_replay_counter.position < threeodds:
                                self.game.search_index.engage(self.game)
                                self.card1_replay_step_up(threeodds - self.game.card1_replay_counter.position)
            if relays == 4:
                if corners:
                    if supercard == 1 or supercard == 2:
                        print "HERE"
                        if self.game.card1_replay_counter.position < fiveodds:
                            self.game.search_index.engage(self.game)
                            self.card1_replay_step_up(fiveodds - self.game.card1_replay_counter.position)
                if corners and self.game.corners.status == True:
                    if self.game.card1_replay_counter.position < fiveodds:
                        self.game.search_index.engage(self.game)
                        self.card1_replay_step_up(fiveodds - self.game.card1_replay_counter.position)
                else:
                    if not corners:
                        if self.game.card1_replay_counter.position < fourodds:
                            self.game.search_index.engage(self.game)
                            self.card1_replay_step_up(fourodds - self.game.card1_replay_counter.position)
                    if left_specialcard == 1:
                        if self.game.left_special_card.status == True:
                            if self.game.card1_replay_counter.position < fiveodds:
                                self.game.search_index.engage(self.game)
                                self.card1_replay_step_up(fiveodds - self.game.card1_replay_counter.position)
                    elif right_specialcard == 1:
                        if self.game.right_special_card.status == True:
                            if self.game.card1_replay_counter.position < fiveodds:
                                self.game.search_index.engage(self.game)
                                self.card1_replay_step_up(fiveodds - self.game.card1_replay_counter.position)
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
        self.pos[11] = {6:1, 20:2, 16:3, 22:4, 11:5}
        self.pos[12] = {9:1, 19:2, 16:3, 21:4, 3:5}
        self.pos[13] = {}
        self.pos[14] = {9:1, 6:2, 3:3, 11:4}
        self.pos[15] = {}
        self.pos[16] = {}
        self.pos[17] = {15:1, 7:2, 11:3}
        self.pos[18] = {1:1, 10:2, 13:3}
        self.pos[19] = {17:1, 4:2, 18:3}
        self.pos[20] = {15:1, 1:2, 17:3}
        self.pos[21] = {7:1, 10:2, 4:3}
        self.pos[22] = {11:1, 13:2, 18:3}
        self.pos[23] = {11:1, 10:2, 17:3}
        self.pos[24] = {15:1, 10:2, 18:3}
        self.pos[25] = {}
        self.pos[26] = {15:1, 11:2, 18:3, 17:4}
        self.pos[27] = {}
        self.pos[28] = {}
        self.pos[29] = {23:1, 3:2, 18:3}
        self.pos[30] = {9:1, 25:2, 11:3}
        self.pos[31] = {12:1, 24:2, 14:3}
        self.pos[32] = {23:1, 9:2, 12:3}
        self.pos[33] = {3:1, 25:2, 24:3}
        self.pos[34] = {18:1, 11:2, 14:3}
        self.pos[35] = {18:1, 25:2, 12:3}
        self.pos[36] = {23:1, 25:2, 14:3}
        self.pos[37] = {}
        self.pos[38] = {23:1, 18:2, 14:3, 12:4}
        self.pos[39] = {}
        self.pos[40] = {1:1, 12:2, 4:3, 24:4}
        self.pos[41] = {12:1, 4:2, 24:3, 1:4}
        self.pos[42] = {4:1, 24:2, 1:3, 12:4}
        self.pos[43] = {24:1, 1:2, 12:3, 4:4}
        self.pos[44] = {}
        self.pos[45] = {23:1, 9:2, 6:3, 17:4}
        self.pos[46] = {9:1, 6:2, 17:3, 23:4}
        self.pos[47] = {6:1, 17:2, 23:3, 9:4}
        self.pos[48] = {17:1, 23:2, 9:3, 6:4}
        self.pos[49] = {23:1, 9:2, 6:3, 17:4}
        self.pos[50] = {}

        corners = False
        sc = 0
        card = 0
        left_specialcard = False
        right_specialcard = False

        if rivets in range(0, 15):
            card = 1
        if rivets == 14:
            corners = True
        if rivets in range(16, 27):
            sc = 2
        if rivets == 26:
            corners = True
        if rivets in range(28, 39):
            sc = 1
        if rivets == 38:
            corners = True

        if rivets in range(40, 44):
            left_specialcard = True
        if rivets in range(45, 50):
            right_specialcard = True

        return (self.pos[rivets], card, corners, sc, left_specialcard, right_specialcard)
       
    
    def blink_title(self):
        title1 = random.randint(0,1)
        title2 = random.randint(0,1)
        title3 = random.randint(0,1)
        if title1 == 1:
            pos = [284,249]
            image = pygame.image.load('mexico/assets/title1_on.png').convert_alpha()
            screen.blit(image, pos)
        if title2 == 1:
            pos = [229,275]
            image = pygame.image.load('mexico/assets/title2_on.png').convert_alpha()
            screen.blit(image, pos)
        if title3 == 1:
            pos = [347,272]
            image = pygame.image.load('mexico/assets/title3_on.png').convert_alpha()
            screen.blit(image, pos)
        
        pygame.display.update()
        self.delay(name="display", delay=0.1, handler=graphics.mexico.display, param=self)
#        self.delay(name="blink_title", delay=3, handler=self.blink_title)

    
    def scan_all(self):
        #Animate scanning of everything - this happens through the flash disc
        if self.game.odds.position < 1:
            self.game.odds.step()
            self.delay(name="display", delay=0, handler=graphics.mexico.display, param=self)
        else:
            if self.game.odds.position < 2:
                self.game.odds.step()
            self.all_probability()
            s = random.randint(1,10)
            self.animate_feature_scan(s)
            self.delay(name="display", delay=0, handler=graphics.mexico.display, param=self)

    def check_reflex2(self):
        r2 = self.game.reflex2.position
        mix1 = self.game.mixer1.connected_rivet()
        if r2 == 15 or r2 == 16 or r2 == 17 or r2 == 19:
            if mix1 == 14:
                return 1
            else:
                return 0
        elif r2 in range(19,22):
            if mix1 == 3 or mix1 == 14:
                return 1
            else:
                return 0
        elif r2 == 5 or r2 in range (23,29):
            if mix1 == 2 or mix1 == 6 or mix1 == 10 or mix1 == 17:
                return 1
            else:
                return 0
        elif r2 in range(30,35):
            if mix1 == 1 or mix1 == 5 or mix1 == 6 or mix1 == 8 or mix1 == 12 or mix1 == 23:
                return 1
            else:
                return 0
        elif r2 in range(36,43):
            if mix1 == 1 or mix1 == 5 or mix1 == 8 or mix1 == 10 or mix1 == 15 or mix1 == 17 or mix1 == 21 or mix1 == 23:
                return 1
            else:
                return 0
        elif r2 in range(44,48):
            return 1
        else:
            return 1

    def check_mixer2(self):
        mix2 = self.game.mixer2.connected_rivet()
        if self.game.odds.position <= 2:
            if mix2 == 0 or mix2 == 1 or mix2 == 3 or mix2 == 4 or mix2 == 8 or mix2 == 9 or mix2 == 11 or mix2 == 12 or mix2 == 13 or mix2 == 14 or mix2 == 16 or mix2 == 20 or mix2 == 21 or mix2 == 22 or mix2 == 24:
                return 1
            else:
                return 0
        elif self.game.odds.position == 3 or self.game.odds.position == 4:
            if mix2 == 1 or mix2 == 5 or mix2 == 6 or mix2 == 8 or mix2 == 12 or mix2 == 15 or mix2 == 16 or mix2 == 19 or mix2 == 21 or mix2 == 23:
                return 1
            else:
                return 0
        elif self.game.odds.position == 5 or self.game.odds.position == 6:
            if mix2 == 17 or mix2 == 24:
                return 1
            else:
                return 0
        else:
            if mix2 == 0 or mix2 == 2 or mix2 == 7 or mix2 == 10 or mix2 == 14 or mix2 == 18:
                return 1
            else:
                return 0

    def all_probability(self):
        r2 = self.check_reflex2()
        if r2 == 1:
            m2 = self.check_mixer2()
            if m2 == 1:
               sc = self.game.super_card.position
               sf = self.game.selection_feature.position
               m3 = self.game.mixer3.position
               self.check_mixer4()
               if sf <= 4:
                   if m3 == 1 or m3 == 15 or m3 == 23 or m3 == 5 or m3 == 17:
                        if self.game.odds.position >= 2:
                            self.game.odds.step()
                            if self.game.cu:
                                self.game.super_card.step()
                            else:
                                self.game.ball_return.step()
                            return
               elif sf == 5:
                   if m3 == 1 or m3 == 15 or m3 == 23:
                       if self.game.odds.position >= 2:
                           self.game.odds.step()
                           if self.game.cu:
                               self.game.super_card.step()
                           else:
                               self.game.ball_return.step()
                           return
               elif sf >= 6:
                   if m3 == 1:
                       if self.game.odds.position >= 2:
                           self.game.odds.step()
                           if self.game.cu:
                               self.game.super_card.step()
                           else:
                               self.game.ball_return.step()
                           return
               elif sc <= 2:
                   if m3 == 2 or m3 == 4 or m3 == 6 or m3 == 10 or m3 == 12 or m3 == 20 or m3 == 24:
                       if self.game.odds.position >= 2:
                           self.game.odds.step()
                           if self.game.cu:
                               self.game.super_card.step()
                           else:
                               self.game.ball_return.step()
                           return
               elif sc >= 3:
                   if m3 == 11 or m3 == 16 or m3 == 21:
                       if self.game.odds.position >= 2:
                           self.game.odds.step()
                           if self.game.cu:
                               self.game.super_card.step()
                           else:
                               self.game.ball_return.step()
                           return
               elif m3 == 0 or m3 == 3 or m3 == 7 or m3 == 9 or m3 == 14 or m3 == 18 or m3 == 22: 
                   if self.game.odds.position >= 2:
                       self.game.odds.step()
                       if self.game.cu:
                           self.game.super_card.step()
                       else:
                           self.game.ball_return.step()
                       return
               else:
                   if self.game.odds.position < 2:
                       self.game.odds.step()
                       return

    def check_mixer4(self):
        m4 = self.game.mixer4.position
        if self.game.selection_feature.position < 9:
            if m4 == 5 or m4 == 9 or m4 == 13 or m4 == 18 or m4 == 28 or m4 == 39 or m4 == 40 or m4 == 48 or m4 == 50:
                if self.game.selection_feature.position < 6:
                    if self.game.mixer1.position == 4 or self.game.mixer1.position == 11 or self.game.mixer1.position == 13 or self.game.mixer1.position == 16 or self.game.mixer1.position == 18 or self.game.mixer1.position == 22:
                        self.step_selection(6 - self.game.selection_feature.position)
                        self.game.select_spots.engage(self.game)
                else:
                    self.game.selection_feature.step()
                self.delay(name="display", delay=0, handler=graphics.mexico.display, param=self)
                if self.game.selection_feature.position == 4:
                    self.game.selection_feature.step()
                    self.delay(name="display", delay=0, handler=graphics.mexico.display, param=self)
                    self.game.selection_feature.step()
                    self.game.select_spots.engage(self.game)
                    self.delay(name="display", delay=0, handler=graphics.mexico.display, param=self)
        elif self.game.selection_feature.position == 9:
            if m4 == 4 or m4 == 6 or m4 == 11 or m4 == 15 or m4 == 16 or m4 == 22 or m4 == 24 or m4 == 30 or m4 == 37 or m4 == 43 or m4 == 44:
                self.game.selection_feature.step()
                self.game.select_spots.engage(self.game)
                self.delay(name="display", delay=0, handler=graphics.mexico.display, param=self)
        elif self.game.selection_feature.position == 10:
            if m4 == 3 or m4 == 8 or m4 == 12 or m4 == 20 or m4 == 29 or m4 == 32:
                self.game.selection_feature.step()
                self.game.select_spots.engage(self.game)
                self.delay(name="display", delay=0, handler=graphics.mexico.display, param=self)
        #I've fudged the selection feature step-up.  It requires multiple checks of Mixer #4. I've approximated the mixer #1 check through the single step instead.
        
        if m4 == 34 or m4 == 49:
            self.game.super_card.step()
            self.delay(name="display", delay=0, handler=graphics.mexico.display, param=self)
        if m4 == 2 or m4 == 7 or m4 == 10 or m4 == 14 or m4 == 21 or m4 == 46:
            if self.game.super_card.position < 4:
                self.step_sc(4 - self.game.super_card.position)
        if m4 == 1 or m4 == 27 or m4 == 38:
            if self.game.super_card.position >= 5:
                self.step_sc(8 - self.game.super_card.position)
        if m4 == 5 or m4 == 7 or m4 == 9 or m4 == 12 or m4 == 14 or m4 == 23 or m4 == 32 or m4 == 39 or m4 == 43 or m4 == 48:
            self.game.before_fourth.disengage()
            self.game.before_fifth.engage(self.game)
        if m4 == 4 or m4 == 6 or m4 == 22 or m4 == 28:
            self.game.corners.engage(self.game)
        if m4 == 13 or m4 == 16 or m4 == 18 or m4 == 30 or m4 == 44:
            self.game.yellow_star.engage(self.game)
            self.game.coils.redROLamp.enable()
        if self.game.red_star.status == True:
            if m4 == 2 or m4 == 8 or m4 == 21 or m4 == 24 or m4 == 37:
                self.game.yellow_star.engage(self.game)
                self.game.coils.redROLamp.enable()
        if m4 == 10 or m4 == 17 or m4 == 26 or m4 == 27 or m4 == 35:
            self.game.red_star.engage(self.game)
            self.game.coils.yellowROLamp.enable()
        if self.game.yellow_star.status == True:
            if m4 == 31 or m4 == 40 or m4 == 41 or m4 == 47 or m4 == 49:
                self.game.red_star.engage(self.game)
                self.game.yellowROLamp.enable()
        if m4 == 3 or m4 == 15 or m4 == 20 or m4 == 25 or m4 == 29 or m4 == 36 or m4 == 45:
            
            self.game.selection_feature_relay.engage(self.game)
        if self.game.reflex2.position == 50:
            if m4 == 11 or m4 == 19 or m4 == 33:
                self.game.selection_feature_relay.engage(self.game)
        self.delay(name="display", delay=0, handler=graphics.mexico.display, param=self)
        if m4 == 2 or m4 == 26 or m4 == 37 or m4 == 41 or m4 == 35 or m4 == 24 or m4 == 34 or m4 == 40 or m4 == 46 or m4 == 49:
            if self.game.left_special_card.status == False:
                self.game.left_special_card.engage(self.game)
            else:
                self.game.right_special_card.engage(self.game)
        
    def eb_probability(self):
        r2 = self.check_reflex2()
        if r2 == 1:
            m4 = self.game.mixer4.position
            o = self.game.odds.position
            if o < 2:
                if m4 == 7 or m4 == 14 or m4 == 19 or m4 == 22 or m4 == 27 or m4 == 34 or m4 == 37 or m4 == 42:
                    self.game.extra_ball.step()
            elif o == 2:
                if m4 == 0 or m4 == 5 or m4 == 9 or m4 == 17 or m4 == 20 or m4 == 22 or m4 == 37 or m4 == 39 or m4 == 44:
                    self.game.extra_ball.step()
            elif o == 3 or o == 4:
                if m4 == 0 or m4 == 5 or m4 == 10 or m4 == 16 or m4 == 17 or m4 == 25 or m4 == 30 or m4 == 32 or m4 == 35:
                    self.game.extra_ball.step()
            elif o == 5 or o == 6:
                if m4 == 0 or m4 == 15 or m4 == 45:
                    self.game.extra_ball.step()
            elif self.game.extra_ball.position < 10:
                if m4 == 1 or m4 == 3 or m4 == 4 or m4 == 6 or m4 == 11 or m4 == 15 or m4 == 19 or m4 == 21 or m4 == 26 or m4 == 31 or m4 == 33 or m4 == 35 or m4 == 41 or m4 == 46 or m4 == 49:
                    self.game.extra_ball.step()
            elif self.game.extra_ball.position >= 10 and self.game.extra_ball.position < 19:
                if m4 == 8 or m4 == 13 or m4 == 24 or m4 == 28 or m4 == 29 or m4 == 44:
                    self.game.extra_ball.step()
            elif self.game.extra_ball.position >= 19:
                if m4 == 25 or m4 == 30 or m4 == 45:
                    self.game.extra_ball.step()
            elif self.game.mixer1.position == 0:
                self.step_eb(24)
            
            self.check_lifter_status()
            self.delay(name="display", delay=0, handler=graphics.mexico.display, param=self)
            
    def step_eb(self, number):
        if number > 0:
            number -= 1
            self.game.extra_ball.step()
            self.delay(name="display", delay=0, handler=graphics.mexico.display, param=self)
            self.check_lifter_status()
            self.delay(name="step_eb", delay=0.1, handler=self.step_eb, param=number)
            if self.game.extra_ball.position >= 9:
                self.check_lifter_status()

    def step_odds(self, number):
        if number > 0:
            number -= 1
            self.game.odds.step()
            self.delay(name="display", delay=0, handler=graphics.mexico.display, param=self)
            self.check_lifter_status()
            self.delay(name="step_odds", delay=0.1, handler=self.step_odds, param=number)
        else:
            self.search()

    def step_sc(self, number):
        if number > 0:
            number -= 1
            self.game.super_card.step()
            self.delay(name="display", delay=0, handler=graphics.mexico.display, param=self)
            self.delay(name="step_sc", delay=0.1, handler=self.step_sc, param=number)
        else:
            if self.game.selection_feature_relay.status == True:
                self.search()

    def step_selection(self, number):
        if number > 0:
            number -= 1
            self.game.selection_feature.step()
            if self.game.selection_feature.position >= 4:
                self.game.select_spots.engage(self.game)
            self.delay(name="display", delay=0, handler=graphics.mexico.display, param=self)
            self.delay(name="step_selection", delay=0.1, handler=self.step_selection, param=number)

    def scan_eb(self):
        if self.game.eb_play.status == True:
            s = random.randint(1,9)
            self.animate_eb_scan(s)
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
        self.delay(name="display", delay=0.1, handler=graphics.mexico.display, param=self)

    def animate_feature_scan(self, s):
        if s > 1:
            self.delay(name="feature_animation", delay=0.1, handler=graphics.mexico.feature_animation, param=s)
            self.delay(name="display", delay=0.1, handler=graphics.mexico.display, param=self)
            s -= 1
            #self.delay(name="animate_feature", delay=0.1, handler=self.animate_feature_scan, param=s)
        else:
            self.cancel_delayed(name="feature_animation")
            self.cancel_delayed(name="display")

    def animate_eb_scan(self, s):
        if s > 1:
            self.delay(name="eb_animation", delay=0.1, handler=graphics.mexico.eb_animation, param=s)
            self.delay(name="display", delay=0.1, handler=graphics.mexico.display, param=self)
            s -= 1
            #self.delay(name="animate_eb", delay=0.1, handler=self.animate_eb_scan, param=s)
        else:
            self.cancel_delayed(name="eb_animation")
            self.cancel_delayed(name="display")


    # Define reset as the knock-off, anti-cheat relay disabled, and replay reset enabled.  Motors turn while credits are knocked off.
    # When meter reaches zero and the zero limit switch is hit, turn off motor sound and leave backglass gi on, but with tilt displayed.

    def startup(self):        
        # Every bingo requires the meter to register '0' 
        # before allowing coin entry --
        # also needs to show a plain 'off' backglass.
        self.eb = False
        self.tilt_actions()
#        self.delay(name="blink_title", delay=1, handler=self.blink_title)


class Mexico(procgame.game.BasicGame):
    """ Mexico is the second United game with a standard Bally 25 hole playfield.  It's not _exactly_ the same, but close enough. """
    def __init__(self, machine_type):
        super(Mexico, self).__init__(machine_type)
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

        #Odds stepper
        self.odds = units.Stepper("odds", 8, 'beach_club')
        
        #Replay Counter
        self.card1_replay_counter = units.Stepper("card1_replay_counter", 300)
 
        #Initialize stepper units used to keep track of features or timing.
        self.timer = units.Stepper("timer", 40)
        self.ball_count = units.Stepper("ball_count", 8)

        # Initialize reflex(es) and mixers unique to this game
        # NOTE:  Reflexes in United games are actually comprised of two
        # separate steppers.  These act as normal continuous steppers, so I
        # need to subclass as steppers.
        self.reflex1 = units.Stepper("reflex1", 50, "Mexico", "continuous")
        self.reflex2 = units.Stepper("reflex2", 50, "Mexico")

        #In United games, they call this spotting motor the 'flash' motor, 
        #similar to the ball bowlers.
        self.flash = units.Spotting("flash", 24)

        #Check for status of the replay register zero switch.  If positive
        #and machine is just powered on, this will zero out the replays.
        self.replay_reset = units.Relay("replay_reset")
        
        #Extra ball unit contains 15 positions.  Max of 3 EBs.
        self.extra_ball = units.Stepper("extra_ball", 15)

        self.left_special_card = units.Relay("left_special_card")
        self.right_special_card = units.Relay("right_special_card")

        self.three_as_four = units.Relay("three_as_four")

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
        self.selection_feature = units.Stepper("selection_feature", 11)
        self.select_spots = units.Relay("select_spots")
        self.spotted = units.Stepper("spotted", 10, "mexico", "continuous")

        self.super_card = units.Stepper("super_card", 8)
        self.ball_return = units.Stepper("ball_return", 7)

        #Some special trip relays for spotted numbers and rollovers
        self.red_star = units.Relay("red_star")
        self.yellow_star = units.Relay("yellow_star")

        self.all_spot = units.Relay("all_spot")

        self.before_fourth = units.Relay("before_fourth")
        self.before_fifth = units.Relay("before_fifth")
        
        self.letter_me = units.Relay("letter_me")
        self.letter_xi = units.Relay("letter_xi")
        self.letter_co = units.Relay("letter_co")

        self.selection_feature_relay = units.Relay("selection_feature_relay")


        self.anti_cheat = units.Relay("anti_cheat")

        self.replays = 0
        self.returned = False

    def reset(self):
        super(Mexico, self).reset()
        self.logger = logging.getLogger('game')
        self.load_config('bingo.yaml')
        self.lock.engage(game)
        
        main_mode = MulticardBingo(self)
        self.modes.add(main_mode)
        

game = Mexico(machine_type='pdb')
game.reset()
game.run_loop()
