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
from bingo_emulator.graphics.miami_beach import *

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

        self.delay(name="display", delay=0.1, handler=graphics.miami_beach.display, param=self)

    def sw_startButton_active(self, sw):
        self.game.eb_play.disengage()
        if self.game.replays > 0 or self.game.switches.freeplay.is_active():
            self.game.sound.stop('add')
            self.game.sound.play('add')
            self.game.tilt.disengage()
            self.regular_play()
            self.scan_all()
            self.delay(name="display", delay=0.1, handler=graphics.miami_beach.display, param=self)

    def sw_enter_active(self, sw):
        if self.game.switches.left.is_active() and self.game.switches.right.is_active():
            self.game.end_run_loop()
            os.system("/home/nbaldridge/proc/bingo_emulator/start_game.sh miami_beach")

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
        if self.game.spotted_numbers.position >= 6:
            if self.game.spotted.position == 0:
                if 19 not in self.holes:
                    self.holes.append(19)
            if self.game.spotted.position == 1:
                if 20 not in self.holes:
                    self.holes.append(20)
            if self.game.spotted.position == 2:
                if 21 not in self.holes:
                    self.holes.append(21)
            if self.game.spotted.position == 3:
                if 22 not in self.holes:
                    self.holes.append(22)
        self.delay(name="display", delay=0.1, handler=graphics.miami_beach.display, param=self)


    def sw_left_active(self, sw):
        max_ball = 4

        if self.game.spotted_numbers.position >= 6:
            if self.game.ball_count.position < max_ball:
                self.game.spotted.stepdown()
                #Initial spotted selection - 2 numbers
                if self.game.spotted_numbers.position == 6:
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
                        if 21 not in self.holes:
                            self.holes.append(21)
                    elif self.game.spotted.position == 3:
                        if 20 in self.holes:
                            if self.game.switches.hole20.is_inactive():
                                self.holes.remove(20)
                        if 21 in self.holes:
                            if self.game.switches.hole21.is_inactive():
                                self.holes.remove(21)
                        if 19 in self.holes:
                            if self.game.switches.hole19.is_inactive():
                                self.holes.remove(19)
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
                        if 21 in self.holes:
                            if self.game.switches.hole21.is_inactive():
                                self.holes.remove(21)

        self.delay(name="display", delay=0.1, handler=graphics.miami_beach.display, param=self)

    def sw_right_active(self, sw):
        max_ball = 4

        if self.game.spotted_numbers.position >= 6:
            if self.game.ball_count.position < max_ball:
                self.game.spotted.stepdown()
                #Initial spotted selection - 2 numbers
                if self.game.spotted_numbers.position == 6:
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
                        if 21 not in self.holes:
                            self.holes.append(21)
                    elif self.game.spotted.position == 3:
                        if 20 in self.holes:
                            if self.game.switches.hole20.is_inactive():
                                self.holes.remove(20)
                        if 21 in self.holes:
                            if self.game.switches.hole21.is_inactive():
                                self.holes.remove(21)
                        if 19 in self.holes:
                            if self.game.switches.hole19.is_inactive():
                                self.holes.remove(19)
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
                        if 21 in self.holes:
                            if self.game.switches.hole21.is_inactive():
                                self.holes.remove(21)

        self.delay(name="display", delay=0.1, handler=graphics.miami_beach.display, param=self)



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
            if self.game.selector.position < 1:
                self.game.selector.step()
                self.game.lines.step()
            if self.game.switches.shutter.is_inactive():
                self.game.coils.shutter.enable()
            self.replay_step_down()
            self.check_lifter_status()
            if self.game.spotted_numbers.position >= 6:
                if self.game.spotted.position == 0:
                    if 19 not in self.holes:
                        self.holes.append(19)
                elif self.game.spotted.position == 1:
                    if 20 not in self.holes:
                        self.holes.append(20)
                elif self.game.spotted.position == 2:
                    if 21 not in self.holes:
                        self.holes.append(21)
                elif self.game.spotted.position == 3:
                    if 22 not in self.holes:
                        self.holes.append(22)
        else:
            self.holes = []
            self.game.start.engage(self.game)
            self.game.card1_replay_counter.reset()
            self.game.super_corners.disengage()
            self.game.spotted_numbers.reset()
            self.game.corners.disengage()
            self.game.corners_replay_counter.reset()
            self.game.start.engage(self.game)
            self.game.lines.reset()
            self.game.curtains.reset()
            self.game.green_three_as_five.disengage()
            self.game.red_three_as_four.disengage()
            self.game.yellow_three_as_four.disengage()
            self.game.selector.reset()
            self.game.ball_count.reset()
            self.game.extra_ball.reset()
            self.game.odds.reset()
            self.game.timer.reset()
            self.game.sound.play_music('motor', -1)
            self.regular_play()
        self.delay(name="display", delay=0.1, handler=graphics.miami_beach.display, param=self)
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
        if self.game.ball_count.position >= 4:
            if self.game.search_index.status == False:
                self.search()
        if self.game.ball_count.position <= 7:
            self.check_lifter_status()
        self.delay(name="display", delay=0.1, handler=graphics.miami_beach.display, param=self)


    # This is really nasty, but it is how we render graphics for each individual hole.
    # numbers are added (or removed from) a list.  In this way, I can re-use the same
    # routine even for games where there are ball return functions like Surf Club.

    def sw_hole1_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(1)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.miami_beach.display, param=self)

    def sw_hole2_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(2)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.miami_beach.display, param=self)

    def sw_hole3_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(3)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.miami_beach.display, param=self)

    def sw_hole4_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(4)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.miami_beach.display, param=self)

    def sw_hole5_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(5)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.miami_beach.display, param=self)

    def sw_hole6_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(6)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.miami_beach.display, param=self)

    def sw_hole7_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(7)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.miami_beach.display, param=self)

    def sw_hole8_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(8)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.miami_beach.display, param=self)

    def sw_hole9_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(9)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.miami_beach.display, param=self)

    def sw_hole10_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(10)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.miami_beach.display, param=self)

    def sw_hole11_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(11)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.miami_beach.display, param=self)

    def sw_hole12_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(12)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.miami_beach.display, param=self)

    def sw_hole13_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(13)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.miami_beach.display, param=self)

    def sw_hole14_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(14)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.miami_beach.display, param=self)

    def sw_hole15_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(15)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.miami_beach.display, param=self)

    def sw_hole16_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(16)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.miami_beach.display, param=self)

    def sw_hole17_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(17)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.miami_beach.display, param=self)

    def sw_hole18_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(18)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.miami_beach.display, param=self)

    def sw_hole19_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(19)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.miami_beach.display, param=self)

    def sw_hole20_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(20)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.miami_beach.display, param=self)

    def sw_hole21_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(21)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.miami_beach.display, param=self)

    def sw_hole22_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(22)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.miami_beach.display, param=self)

    def sw_hole23_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(23)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.miami_beach.display, param=self)

    def sw_hole24_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(24)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.miami_beach.display, param=self)

    def sw_hole25_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(25)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.miami_beach.display, param=self)

    def sw_replayReset_active(self, sw):
        self.game.anti_cheat.disengage()
        self.holes = []
        graphics.miami_beach.display(self)
        self.tilt_actions()
        self.replay_step_down(self.game.replays)

    def tilt_actions(self):
        self.game.start.disengage()
        self.cancel_delayed(name="replay_reset")
        self.cancel_delayed(name="card1_replay_step_up")
        self.cancel_delayed(name="corners_replay_step_up")
        self.cancel_delayed(name="blink")
        self.cancel_delayed(name="timeout")
        self.game.card1_replay_counter.reset()
        self.game.super_corners.disengage()
        self.game.spotted_numbers.reset()
        self.game.lines.reset()
        self.game.curtains.reset()
        self.game.corners.disengage()
        self.game.corners_replay_counter.reset()
        self.game.start.engage(self.game)
        self.game.green_three_as_five.disengage()
        self.game.red_three_as_four.disengage()
        self.game.yellow_three_as_four.disengage()
        self.game.selector.reset()
        self.game.ball_count.reset()
        self.game.extra_ball.reset()
        self.game.odds.reset()
        self.game.eb_play.disengage()
        self.game.search_index.disengage()
        if self.game.ball_count.position == 0:
            if self.game.switches.shutter.is_active():
                self.game.coils.shutter.enable()
        self.holes = []
        self.game.anti_cheat.engage(game)
        self.game.tilt.engage(self.game)
        self.game.sound.stop_music()
        self.game.sound.play('tilt')
        # displays "Tilt" on the backglass, you have to recoin.
        self.delay(name="display", delay=0.1, handler=graphics.miami_beach.display, param=self)

    def sw_tilt_active(self, sw):
        if self.game.tilt.status == False:
            self.tilt_actions()

    def replay_step_down(self, number=0):
        if number > 0:
            if number > 1:
                self.game.replays -= 1
                graphics.replay_step_down(self.game.replays, graphics.miami_beach.reel1, graphics.miami_beach.reel10, graphics.miami_beach.reel100)
                self.game.coils.registerDown.pulse()
                number -= 1
                graphics.miami_beach.display(self)
                self.delay(name="replay_reset", delay=0.13, handler=self.replay_step_down, param=number)
            elif number == 1:
                self.game.replays -= 1
                graphics.replay_step_down(self.game.replays, graphics.miami_beach.reel1, graphics.miami_beach.reel10, graphics.miami_beach.reel100)
                self.game.coils.registerDown.pulse()
                number -= 1
                graphics.miami_beach.display(self)
                self.cancel_delayed(name="replay_reset")
        else: 
            if self.game.replays > 0:
                self.game.replays -= 1
                graphics.replay_step_down(self.game.replays, graphics.miami_beach.reel1, graphics.miami_beach.reel10, graphics.miami_beach.reel100)
                self.delay(name="display", delay=0.1, handler=graphics.miami_beach.display, param=self)
            self.game.coils.registerDown.pulse()

    def replay_step_up(self):
        if self.game.replays < 899:
            self.game.replays += 1
            graphics.replay_step_up(self.game.replays, graphics.miami_beach.reel1, graphics.miami_beach.reel10, graphics.miami_beach.reel100)
        self.game.coils.registerUp.pulse()
        self.game.coils.sounder.pulse()
        self.game.reflex.increase()
        graphics.miami_beach.display(self)

    def sw_yellow_active(self, sw):
        if self.game.ball_count.position >= 5:
            if self.game.eb_play.status == False:
                self.game.spotting.spin()
                self.game.mixer1.spin()
                self.game.mixer2.spin()
                self.game.mixer3.spin()
                self.game.mixer4.spin()
                self.game.eb_play.engage(self.game)
                self.delay(name="display", delay=0.1, handler=graphics.miami_beach.display, param=self)
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
                self.delay(name="display", delay=0.1, handler=graphics.miami_beach.display, param=self)
            
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
            self.color = self.r[3]

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
                        if self.game.curtains.position >= self.card:
                            if s >= 3:
                                self.find_winner(s, self.card, self.corners, self.color)
                                break

    def find_winner(self, relays, card, corners, color):
        if self.game.search_index.status == False and self.game.replays < 899:
            if self.game.odds.position == 1:
                threeodds = 4
                fourodds = 16
                fiveodds = 60
            elif self.game.odds.position == 2:
                threeodds = 6
                fourodds = 20
                fiveodds = 60
            elif self.game.odds.position == 3:
                threeodds = 8
                fourodds = 24
                fiveodds = 60
            elif self.game.odds.position == 4:
                threeodds = 12
                fourodds = 36
                fiveodds = 72
            elif self.game.odds.position == 5:
                threeodds = 18
                fourodds = 48
                fiveodds = 90
            elif self.game.odds.position == 6:
                threeodds = 24
                fourodds = 64
                fiveodds = 120
            elif self.game.odds.position == 7:
                threeodds = 36
                fourodds = 72
                fiveodds = 150
            elif self.game.odds.position == 8:
                threeodds = 48
                fourodds = 100
                fiveodds = 192
            elif self.game.odds.position == 9:
                threeodds = 64
                fourodds = 200
                fiveodds = 300

            if card <= self.game.curtains.position:
                if relays == 3:
                    if not corners:
                        if color == "green" and self.game.green_three_as_five.status == True:
                            if self.game.card1_replay_counter.position < fiveodds:
                                self.game.search_index.engage(self.game)
                                self.card1_replay_step_up(fiveodds - self.game.card1_replay_counter.position)
                        elif color == "yellow" and self.game.yellow_three_as_four.status == True:
                            if self.game.card1_replay_counter.position < fourodds:
                                self.game.search_index.engage(self.game)
                                self.card1_replay_step_up(fourodds - self.game.card1_replay_counter.position)
                        elif color == "red" and self.game.red_three_as_four.status == True:
                            if self.game.card1_replay_counter.position < fourodds:
                                self.game.search_index.engage(self.game)
                                self.card1_replay_step_up(fourodds - self.game.card1_replay_counter.position)
                        else:
                            if self.game.card1_replay_counter.position < threeodds:
                                self.game.search_index.engage(self.game)
                                self.card1_replay_step_up(threeodds - self.game.card1_replay_counter.position)
                if relays == 4:
                    if corners and self.game.corners.status == True:
                        if self.game.super_corners.status == True:
                            if self.game.corners_replay_counter.position < 300:
                                self.game.search_index.engage(self.game)
                                self.corners_replay_step_up(300 - self.game.corners_replay_counter.position)
                        else:
                            if self.game.corners_replay_counter.position < 100:
                                self.game.search_index.engage(self.game)
                                self.corners_replay_step_up(100 - self.game.corners_replay_counter.position)
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
        # 5 Line Card Horizontal
        self.pos[0] = {}
        self.pos[1] = {9:1, 4:2, 24:3, 15:4, 6:5}
        self.pos[2] = {10:1, 19:2, 14:3, 20:4, 8:5}
        self.pos[3] = {2:1, 18:2, 16:3, 12:4, 1:5}
        self.pos[4] = {13:1, 22:2, 25:3, 21:4, 17:5}
        self.pos[5] = {11:1, 7:2, 5:3, 23:4, 3:5}
        # 5 Line Card Vertical
        self.pos[6] = {9:1, 10:2, 2:3, 13:4, 11:5}
        self.pos[7] = {4:1, 19:2, 18:3, 22:4, 7:5}
        self.pos[8] = {24:1, 14:2, 16:3, 25:4, 5:5}
        self.pos[9] = {15:1, 20:2, 12:3, 21:4, 23:5}
        self.pos[10] = {6:1, 8:2, 1:3, 17:4, 3:5}
        # 5 Line Card Diagonal
        self.pos[11] = {24:1, 20:2, 1:3}
        self.pos[12] = {5:1, 21:2, 1:3}
        self.pos[13] = {}
        #6 Line Card Horizontal
        self.pos[14] = {4:1, 24:2, 15:3, 6:4, 5:5}
        self.pos[15] = {19:1, 14:2, 20:3, 8:4, 19:5}
        self.pos[16] = {18:1, 16:2, 12:3, 1:4, 23:5}
        self.pos[17] = {22:1, 25:2, 21:3, 17:4, 22:5}
        self.pos[18] = {7:1, 5:2, 23:3, 3:4, 2:5}
        #6th Vertical Line
        self.pos[19] = {5:1, 19:2, 23:3, 22:4, 2:5}
        self.pos[20] = {}
        self.pos[21] = {}
        self.pos[22] = {}
        #7th Line Card Horiz.
        self.pos[23] = {24:1, 15:2, 6:3, 5:4, 13:5}
        self.pos[24] = {14:1, 20:2, 8:3, 19:4, 9:5}
        self.pos[25] = {16:1, 12:2, 1:3, 23:4, 10:5}
        self.pos[26] = {25:1, 21:2, 17:3, 22:4, 14:5}
        self.pos[27] = {5:1, 23:2, 3:3, 2:4, 12:5}
        #7th Vertical Line
        self.pos[28] = {13:1, 9:2, 10:3, 14:4, 12:5}
        #7th card Diagonals
        self.pos[29] = {24:1, 20:2, 1:3, 22:4, 12:5}
        self.pos[30] = {5:1, 21:2, 1:3, 19:4, 13:5}
        self.pos[31] = {}
        #Corners
        self.pos[32] = {5:1, 12:2, 13:3, 24:4}
        self.pos[33] = {}
        #8th Card Horiz.
        self.pos[34] = {15:1, 6:2, 5:3, 13:4, 4:5}
        self.pos[35] = {20:1, 8:2, 19:3, 9:4, 20:5}
        self.pos[36] = {12:1, 1:2, 23:3, 10:4, 15:5}
        self.pos[37] = {21:1, 17:2, 22:3, 14:4, 21:5}
        self.pos[38] = {23:1, 3:2, 2:3, 12:4, 6:5}
        #8th Card Vert.
        self.pos[39] = {4:1, 20:2, 15:3, 21:4, 6:5}
        self.pos[40] = {}
        #9th Card Horiz.
        self.pos[41] = {6:1, 5:2, 13:3, 4:4, 1:5}
        self.pos[42] = {8:1, 19:2, 9:3, 20:4, 3:5}
        self.pos[43] = {1:1, 23:2, 10:3, 15:4, 8:5}
        self.pos[44] = {17:1, 22:2, 14:3, 21:4, 11:5}
        self.pos[45] = {3:1, 2:2, 12:3, 6:4, 7:5}
        #9th Card Vert.
        self.pos[46] = {1:1, 3:2, 8:3, 11:4, 7:5}
        self.pos[47] = {}
        self.pos[48] = {}
        self.pos[49] = {}
        self.pos[50] = {}

        corners = False
        card = 0
        color = None

        if rivets in range(0, 13):
            card = 1
        if rivets in range(14,20):
            card = 2
        if rivets in range(23,33):
            card = 3
        if rivets in range(34,40):
            card = 4
        if rivets in range(41,50):
            card = 5
        if rivets == 32:
            corners = True
        if rivets in [1,4,14,17,23,26,34,37,41,44,19]:
            color = 'red'
        if rivets in [11,12,29,30]:
            color = 'green'
        if rivets in [2,5,15,19,24,27,35,38,42,45,7,9,39]:
            color = 'yellow'

        return (self.pos[rivets], card, corners, color)
    
    def scan_all(self):
        #Animate scanning of everything - this happens through the spotting disc
        self.all_probability()

    def all_probability(self):
        if self.game.curtains.position == 0:
            self.game.curtains.step()
        if self.game.odds.position < 3:
            self.game.odds.step()
        mix1 = self.game.mixer1.connected_rivet()
        if self.game.reflex.connected_rivet() == 0 and (mix1 in [1,9,15]):
            self.scan_odds()
            self.scan_features()
        elif self.game.reflex.connected_rivet() == 1 and (mix1 in [0,2,14]):
            self.scan_odds()
            self.scan_features()
        elif self.game.reflex.connected_rivet() == 2 and (mix1 in [6,13,22]):
            self.scan_odds()
            self.scan_features()
        elif self.game.reflex.connected_rivet() == 3:
            self.scan_odds()
            self.scan_features()
        elif self.game.reflex.connected_rivet() == 4:
            self.scan_odds()
            self.scan_features()
        else:
            if mix1 in [3,4,7,8,10,11,16,17,18,19,21,23]:
                self.scan_odds()
                self.scan_features()
            else:
                s = random.randint(1,5)
                self.animate_odds_scan(s)
                s = random.randint(1,6)
                self.animate_feature_scan(s)

    def scan_odds(self):
        if self.game.odds.position < 3:
            return
        s = random.randint(1,5)
        self.animate_odds_scan(s)
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
            self.game.coils.counter.pulse()
            self.delay(name="display", delay=0, handler=graphics.miami_beach.display, param=self)
            number -= 1
            self.delay(name="extra_step", delay=0.1, handler=self.extra_step, param=number)

    def check_extra_step(self):
        i = random.randint(0,32)
        if i == 16:
            return 1
        else:
            return 0

    def odds_probability(self):
        # Check position of Mixer 2, extra scoring relays and current 
        # position of the odds, along with trip relays.
        # For first check, guaranteed single stepup.  Probability doesn't 
        # factor, so I will return as part of the initial check above.
        if self.game.odds.position == 1:
            return 1
        else:
            sd = self.game.spotting.position
            if self.game.odds.position == 2:
                if sd == 1:
                    return 1
                else:
                    return 0
            elif self.game.odds.position == 3:
                if sd == 3:
                    return 1
                else:
                    return 0
            elif self.game.odds.position == 4:
                if sd == 9:
                    return 1
                else:
                    return 0
            elif self.game.odds.position == 5:
                if sd == 10:
                    return 1
                else:
                    return 0
            elif self.game.odds.position >= 6:
                if sd == 18:
                    return 1
                else:
                    return 0
            else:
                return 0

    def scan_features(self):
        p = self.features_probability()

    def features_probability(self):
        s = random.randint(1,6)
        self.animate_feature_scan(s)
        mix2 = self.game.mixer2.position

        if self.game.lines.position < self.game.lines.top or self.game.odds.position > 2:
            if self.game.cu == True:
                if mix2 in [13,8,10]:
                    self.game.red_three_as_four.engage(self.game)
                if mix2 in [17,20,5]:
                    self.game.yellow_three_as_four.engage(self.game)
                if mix2 in [1,23]:
                    self.game.green_three_as_five.engage(self.game)
        m3 = self.check_mixer3()
        if m3 == True:
            m2 = self.check_mixer2()
            if m2 == True:
                m4 = self.check_mixer4()
                if m4 == True:
                    self.features_spotting()

    def check_mixer4(self):
        mix4 = self.game.mixer4.position
        r = self.game.red_three_as_four.status
        g = self.game.green_three_as_five.status
        y = self.game.yellow_three_as_four.status
        l = self.game.lines.top

        if r == 1 and g == 1 and y == 1:
            if mix4 in [0,1,6,7,9,12,18,21,22]:
                return 1
            else:
                return 0
        if r == 1 and g == 0 and y == 0:
            if self.game.lines.position < l:
                if mix4 in [8,10,11,14,17,19,20]:
                    return 1
            else:
                if mix4 in [1,5,17,20,23]:
                    return 1
                else:
                    return 0
        if r == 1 and g == 1 and y == 0:
            if mix4 not in [3,8,10,13,17,20,22]:
                return 1
            else:
                return 0
        if r == 0 and g == 1 and y == 1:
            if mix4 not in [0,1,6,7,9,12,18,21,22]:
                return 1
            else:
                return 0
        if r == 1 and g == 0 and y == 1:
            if mix4 not in [2,3,4,5,13,15,16,23]:
                return 1
            else:
                return 0

    def check_mixer2(self):
        mix2 = self.game.mixer2.position
        odds = self.game.odds.position
        if odds == 1:
            if mix2 not in [8,23]:
                return 1
            else:
                return 0
        if odds in [2,3]:
            return 1
        elif odds == 4:
            if mix2 not in [0,2,5,7,9,11,16,18,20,22,12,14,17,19,21,23]:
                return 1
            else:
                return 0
        elif odds == 5:
            if mix2 not in [4,10,12,14,17,21,16,22]:
                return 1
            else:
                return 0
        elif odds == 6:
            if mix2 not in [1,9,12,21,2,5,14,18]:
                return 1
            else:
                return 0
        elif odds in [7,8]:
            if mix2 not in [3,11,17,4,10,20]:
                return 1
            else:
                return 0

    def check_mixer3(self):
        mix3 = self.game.mixer3.position
        lines = self.game.lines.position
        if lines < 4:
            if mix3 in [1,3,5,8,10,13,14,17,20,22,23]:
                return 1
            else:
                return 0
        if lines in range(5,10):
            if mix3 in [0,2,4,6,7,9,12,15,16,18,19,21]:
                return 1
            else:
                return 0
        if lines >= 10:
            if mix3 == 23:
                return 1
            else:
                return 0

    def features_spotting(self):
        sd = self.game.spotting.position
        if self.game.super_corners.status == False:
            self.game.corners.engage(self.game)
        if self.game.cu == 1:
            if self.game.lines.position < 3:
                self.game.lines.step()
        else:
            self.game.spotted_numbers.step()
            self.check_spot()
        if sd in [5,10,15,19,30,32,42,46] and self.game.lines.position >= 5:
            self.step_lines(10 - self.game.lines.position)
        if sd in [8,18,25,28,33,40,43] and self.game.lines.position >= 10:
            self.step_lines(15 - self.game.lines.position)
        if sd in [0,4,11,20,36,44]:
            self.step_lines(5 - self.game.lines.position)
        if sd in [7,27]:
            self.step_lines(10 - self.game.lines.position)
        if sd in [16,22,41]:
            self.step_lines(15 - self.game.lines.position)
        if sd in [2,6,14,21,26,31,34,38,48]:
            self.step_spotted_numbers(6 - self.game.spotted_numbers.position)
            self.check_spot()
        if sd in [1,9,17,23,35,45]:
            self.step_spotted_numbers(4 - self.game.spotted_numbers.position)
            self.check_spot()
        if sd in [3,12,29,37,47]:
            self.step_spotted_numbers(5 - self.game.spotted_numbers.position)
            self.check_spot()
        if sd == 13:
            self.game.super_corners.engage(self.game)
            self.game.corners.disengage()
        if self.game.lines.position >= 5 and self.game.curtains.position < 3:
            self.step_curtains(3 - self.game.curtains.position)
        if self.game.lines.position >= 10 and self.game.curtains.position < 4:
            self.step_curtains(4 - self.game.curtains.position)
        if self.game.lines.position >= 15 and self.game.curtains.position < 5:
            self.step_curtains(5 - self.game.curtains.position)

    def step_curtains(self, number):
        if number >= 1:
            self.game.curtains.step()
            number -= 1
            self.delay(name="display", delay=0.1, handler=graphics.miami_beach.display, param=self)
            self.delay(name="step_curtains", delay=0.1, handler=self.step_curtains, param=number)

    def step_lines(self, number):
        if number >= 1:
            self.game.lines.step()
            if self.game.lines.position >= 5 and self.game.curtains.position < 3:
                self.step_curtains(3 - self.game.curtains.position)
            if self.game.lines.position >= 10 and self.game.curtains.position < 4:
                self.step_curtains(4 - self.game.curtains.position)
            if self.game.lines.position >= 15 and self.game.curtains.position < 5:
                self.step_curtains(5 - self.game.curtains.position)

            number -= 1
            self.delay(name="display", delay=0.1, handler=graphics.miami_beach.display, param=self)
            self.delay(name="step_lines", delay=0.1, handler=self.step_lines, param=number)


    def step_spotted_numbers(self, number):
        if number >= 1:
            self.game.spotted_numbers.step()
            self.check_spot()
            number -= 1
            self.delay(name="display", delay=0.1, handler=graphics.miami_beach.display, param=self)
            self.delay(name="step_spotted_numbers", delay=0.1, handler=self.step_spotted_numbers, param=number)


    def scan_eb(self):
        s = random.randint(1,9)
        self.animate_eb_scan(s)
        if self.game.extra_ball.position == 0:
            self.game.extra_ball.step()
            self.check_lifter_status()
        p = self.eb_probability()

        # Timer resets to 0 position on ball count increasing.  We are fudging this since we will have
        # no good way to measure balls as they return back to the trough.  The ball count unit cannot be
        # relied upon as we do not have a switch in the outhole, and the trough logic is too complex for
        # the task at hand.
        # TODO: implement thunk noises into the units.py to automatically play the noises.
        self.game.timer.reset()
        self.delay(name="display", delay=0.1, handler=graphics.miami_beach.display, param=self)

    def animate_odds_scan(self, s):
        if s > 1:
            self.delay(name="odds_animation", delay=0, handler=graphics.miami_beach.odds_animation, param=s)
            self.delay(name="display", delay=0.1, handler=graphics.miami_beach.display, param=self)
            s -= 1
            #self.delay(name="animate_odds", delay=0.1, handler=self.animate_odds_scan, param=s)
        else:
            self.delay(name="display", delay=0.1, handler=graphics.miami_beach.display, param=self)

    def animate_feature_scan(self, s):
        if s > 1:
            self.delay(name="feature_animation", delay=0.1, handler=graphics.miami_beach.feature_animation, param=s)
            self.delay(name="display", delay=0.1, handler=graphics.miami_beach.display, param=self)
            s -= 1
            #self.delay(name="animate_feature", delay=0.1, handler=self.animate_feature_scan, param=s)
        else:
            self.delay(name="display", delay=0.1, handler=graphics.miami_beach.display, param=self)

    def animate_eb_scan(self, s):
        if s > 1:
            self.delay(name="eb_animation", delay=0.1, handler=graphics.miami_beach.eb_animation, param=s)
            self.delay(name="display", delay=0.1, handler=graphics.miami_beach.display, param=self)
            s -= 1
            #self.delay(name="animate_eb", delay=0.1, handler=self.animate_eb_scan, param=s)
        else:
            self.delay(name="display", delay=0.1, handler=graphics.miami_beach.display, param=self)

    def check_eb_spotting(self):
        sd = self.game.spotting.position
        if sd == 0:
            if self.game.mixer3.position == 23:
                self.step_eb(9 - self.game.extra_ball.position)
        elif sd in [1,2,3,4,8,9,13,14,18,19,20,23,25,28,29,35,39,42,46,47]:
            self.step_eb(3 - self.game.extra_ball.position)
        elif sd in [6,7,11,15,16,21,24,26,27,37,40,41,44]:
            if self.game.extra_ball.position < 6:
                self.step_eb(6 - self.game.extra_ball.position)
        else:
            self.game.extra_ball.step()
            self.check_lifter_status()

    def eb_probability(self):
        mix1 = self.game.mixer1.connected_rivet()
        if self.game.reflex.connected_rivet() == 0 and (mix1 in [1,9,15]):
            m3 = self.check_mixer3()
            if m3 == 1:
                self.check_eb_spotting()
        elif self.game.reflex.connected_rivet() == 1 and (mix1 in [0,2,14]):
            m3 = self.check_mixer3()
            if m3 == 1:
                self.check_eb_spotting()
        elif self.game.reflex.connected_rivet() == 2 and (mix1 in [6,13,22]):
            m3 = self.check_mixer3()
            if m3 == 1:
                self.check_eb_spotting()
        else:
            if mix1 in [3,4,7,8,10,11,16,17,18,19,21,23]:
                m3 = self.check_mixer3()
                if m3 == 1:
                    self.check_eb_spotting()

    def step_eb(self, number):
        if number >= 1:
            self.game.extra_ball.step()
            self.check_lifter_status()
            number -= 1
            self.delay(name="display", delay=0.1, handler=graphics.miami_beach.display, param=self)
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

class MiamiBeach(procgame.game.BasicGame):
    """ Miami Beach is the only game with Magic Curtains """
    def __init__(self, machine_type):
        super(MiamiBeach, self).__init__(machine_type)
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
        self.odds = units.Stepper("odds", 9, 'miami_beach')

        #Replay Counter
        self.card1_replay_counter = units.Stepper("card1_replay_counter", 500)
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
        self.super_corners = units.Relay("super_corners")

        self.selector = units.Stepper("selector", 1)

        # Select-a-spot setup
        self.spotted_numbers = units.Stepper("spotted_numbers", 6)
        self.spotted = units.Stepper("spotted", 4, "miami_beach", "continuous")

        self.green_three_as_five = units.Relay("green_three_as_five")
        self.yellow_three_as_four = units.Relay("yellow_three_as_four")
        self.red_three_as_four = units.Relay("red_three_as_four")

        self.lines = units.Stepper("lines", 15)
        self.curtains = units.Stepper("curtains", 5)

        self.replays = 0
        self.returned = False

    def reset(self):
        super(MiamiBeach, self).reset()
        self.logger = logging.getLogger('game')
        self.load_config('bingo.yaml')
        
        main_mode = SinglecardBingo(self)
        self.modes.add(main_mode)
        
game = MiamiBeach(machine_type='pdb')
game.reset()
game.run_loop()
