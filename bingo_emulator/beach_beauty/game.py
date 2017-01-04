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
from bingo_emulator.graphics.beach_beauty import *

class SinglecardBingo(procgame.game.Mode):
    def __init__(self, game):
        super(SinglecardBingo, self).__init__(game=game, priority=5)
        self.holes = []
        self.startup()
        self.game.sound.register_music('motor', "audio/six_card_motor.wav")
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

        self.delay(name="display", delay=0.1, handler=graphics.beach_beauty.display, param=self)

    def sw_startButton_active(self, sw):
        self.game.eb_play.disengage()
        if self.game.replays > 0 or self.game.switches.freeplay.is_active():
            self.game.sound.stop('add')
            self.game.sound.play('add')
            self.game.tilt.disengage()
            self.regular_play()
            self.scan_all()
            self.delay(name="display", delay=0.1, handler=graphics.beach_beauty.display, param=self)

    def sw_enter_active(self, sw):
        if self.game.switches.left.is_active() and self.game.switches.right.is_active():
            self.game.end_run_loop()
            os.system("/home/nbaldridge/proc/bingo_emulator/start_game.sh beach_beauty")

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

    def sw_left_active(self, sw):
        if self.game.wild_pockets.position >= 12:
            if self.game.pocket.status == True:
                self.game.spotted.stepdown()
                if self.game.pocket_number in self.holes:
                    self.holes.remove(self.game.pocket_number)
                if self.game.one_two_three.status == True:
                    if self.game.spotted.position == 11:
                        if 9 in self.holes:
                            if self.game.switches.hole9.is_inactive():
                                self.holes.remove(9)
                        self.holes.append(18)
                    if self.game.spotted.position == 10:
                        if 18 in self.holes:
                            if self.game.switches.hole18.is_inactive():
                                self.holes.remove(18)
                        self.holes.append(2)
                    elif self.game.spotted.position == 9:
                        if 2 in self.holes:
                            if self.game.switches.hole2.is_inactive():
                                self.holes.remove(2)
                        self.holes.append(1)
                    elif self.game.spotted.position == 8:
                        if 1 in self.holes:
                            if self.game.switches.hole1.is_inactive():
                                self.holes.remove(1)
                        self.holes.append(20)
                    elif self.game.spotted.position == 7:
                        if 20 in self.holes:
                            if self.game.switches.hole20.is_inactive():
                                self.holes.remove(20)
                        self.holes.append(14)
                    elif self.game.spotted.position == 6:
                        if 14 in self.holes:
                            if self.game.switches.hole14.is_inactive():
                                self.holes.remove(14)
                        self.holes.append(19)
                    elif self.game.spotted.position == 5:
                        if 19 in self.holes:
                            if self.game.switches.hole19.is_inactive():
                                self.holes.remove(19)
                        self.holes.append(10)
                    elif self.game.spotted.position == 4:
                        if 10 in self.holes:
                            if self.game.switches.hole10.is_inactive():
                                self.holes.remove(10)
                        self.holes.append(3)
                    elif self.game.spotted.position == 3:
                        if 3 in self.holes:
                            if self.game.switches.hole3.is_inactive():
                                self.holes.remove(3)
                        self.holes.append(24)
                    elif self.game.spotted.position == 2:
                        if 24 in self.holes:
                            if self.game.switches.hole24.is_inactive():
                                self.holes.remove(24)
                        self.holes.append(15)
                    elif self.game.spotted.position == 1:
                        if 15 in self.holes:
                            if self.game.switches.hole15.is_inactive():
                                self.holes.remove(15)
                        self.holes.append(13)
                    elif self.game.spotted.position == 0:
                        if 13 in self.holes:
                            if self.game.switches.hole13.is_inactive():
                                self.holes.remove(13)
                        self.holes.append(9)
                if self.game.four_five_six_seven.status == True:
                    if self.game.spotted.position == 12:
                        if 16 in self.holes:
                            if self.game.switches.hole16.is_inactive():
                                self.holes.remove(16)
                        self.holes.append(6)
                    if self.game.spotted.position == 11:
                        if 6 in self.holes:
                            if self.game.switches.hole6.is_inactive():
                                self.holes.remove(6)
                        self.holes.append(23)
                    elif self.game.spotted.position == 10:
                        if 23 in self.holes:
                            if self.game.switches.hole23.is_inactive():
                                self.holes.remove(23)
                        self.holes.append(5)
                    elif self.game.spotted.position == 9:
                        if 5 in self.holes:
                            if self.game.switches.hole5.is_inactive():
                                self.holes.remove(5)
                        self.holes.append(7)
                    elif self.game.spotted.position == 8:
                        if 7 in self.holes:
                            if self.game.switches.hole7.is_inactive():
                                self.holes.remove(7)
                        self.holes.append(11)
                    elif self.game.spotted.position == 7:
                        if 11 in self.holes:
                            if self.game.switches.hole11.is_inactive():
                                self.holes.remove(11)
                        self.holes.append(17)
                    elif self.game.spotted.position == 6:
                        if 17 in self.holes:
                            if self.game.switches.hole17.is_inactive():
                                self.holes.remove(17)
                        self.holes.append(21)
                    elif self.game.spotted.position == 5:
                        if 21 in self.holes:
                            if self.game.switches.hole21.is_inactive():
                                self.holes.remove(21)
                        self.holes.append(4)
                    elif self.game.spotted.position == 4:
                        if 4 in self.holes:
                            if self.game.switches.hole4.is_inactive():
                                self.holes.remove(4)
                        self.holes.append(22)
                    elif self.game.spotted.position == 3:
                        if 22 in self.holes:
                            if self.game.switches.hole22.is_inactive():
                                self.holes.remove(22)
                        self.holes.append(8)
                    elif self.game.spotted.position == 2:
                        if 8 in self.holes:
                            if self.game.switches.hole8.is_inactive():
                                self.holes.remove(8)
                        self.holes.append(25)
                    elif self.game.spotted.position == 1:
                        if 25 in self.holes:
                            if self.game.switches.hole25.is_inactive():
                                self.holes.remove(25)
                        self.holes.append(12)
                    elif self.game.spotted.position == 0:
                        if 12 in self.holes:
                            if self.game.switches.hole12.is_inactive():
                                self.holes.remove(12)
                        self.holes.append(16)

        self.delay(name="display", delay=0.1, handler=graphics.beach_beauty.display, param=self)

    def sw_right_active(self, sw):
        if self.game.wild_pockets.position >= 12:
            if self.game.pocket.status == True:
                self.game.spotted.step()
                if self.game.pocket_number in self.holes:
                    self.holes.remove(self.game.pocket_number)
                if self.game.one_two_three.status == True:
                    if self.game.spotted.position == 11:
                        if 2 in self.holes:
                            if self.game.switches.hole2.is_inactive():
                                self.holes.remove(2)
                        self.holes.append(18)
                    if self.game.spotted.position == 10:
                        if 1 in self.holes:
                            if self.game.switches.hole1.is_inactive():
                                self.holes.remove(1)
                        self.holes.append(2)
                    elif self.game.spotted.position == 9:
                        if 20 in self.holes:
                            if self.game.switches.hole20.is_inactive():
                                self.holes.remove(20)
                        self.holes.append(1)
                    elif self.game.spotted.position == 8:
                        if 14 in self.holes:
                            if self.game.switches.hole14.is_inactive():
                                self.holes.remove(14)
                        self.holes.append(20)
                    elif self.game.spotted.position == 7:
                        if 19 in self.holes:
                            if self.game.switches.hole19.is_inactive():
                                self.holes.remove(19)
                        self.holes.append(14)
                    elif self.game.spotted.position == 6:
                        if 10 in self.holes:
                            if self.game.switches.hole10.is_inactive():
                                self.holes.remove(10)
                        self.holes.append(19)
                    elif self.game.spotted.position == 5:
                        if 3 in self.holes:
                            if self.game.switches.hole3.is_inactive():
                                self.holes.remove(3)
                        self.holes.append(10)
                    elif self.game.spotted.position == 4:
                        if 24 in self.holes:
                            if self.game.switches.hole24.is_inactive():
                                self.holes.remove(24)
                        self.holes.append(3)
                    elif self.game.spotted.position == 3:
                        if 15 in self.holes:
                            if self.game.switches.hole15.is_inactive():
                                self.holes.remove(15)
                        self.holes.append(24)
                    elif self.game.spotted.position == 2:
                        if 13 in self.holes:
                            if self.game.switches.hole13.is_inactive():
                                self.holes.remove(13)
                        self.holes.append(15)
                    elif self.game.spotted.position == 1:
                        if 9 in self.holes:
                            if self.game.switches.hole9.is_inactive():
                                self.holes.remove(9)
                        self.holes.append(13)
                    elif self.game.spotted.position == 0:
                        if 18 in self.holes:
                            if self.game.switches.hole19.is_inactive():
                                self.holes.remove(18)
                        self.holes.append(9)
                if self.game.four_five_six_seven.status == True:
                    if self.game.spotted.position == 12:
                        if 23 in self.holes:
                            if self.game.switches.hole23.is_inactive():
                                self.holes.remove(23)
                        self.holes.append(6)
                    if self.game.spotted.position == 11:
                        if 5 in self.holes:
                            if self.game.switches.hole5.is_inactive():
                                self.holes.remove(5)
                        self.holes.append(23)
                    elif self.game.spotted.position == 10:
                        if 7 in self.holes:
                            if self.game.switches.hole7.is_inactive():
                                self.holes.remove(7)
                        self.holes.append(5)
                    elif self.game.spotted.position == 9:
                        if 11 in self.holes:
                            if self.game.switches.hole11.is_inactive():
                                self.holes.remove(11)
                        self.holes.append(7)
                    elif self.game.spotted.position == 8:
                        if 17 in self.holes:
                            if self.game.switches.hole17.is_inactive():
                                self.holes.remove(17)
                        self.holes.append(11)
                    elif self.game.spotted.position == 7:
                        if 21 in self.holes:
                            if self.game.switches.hole21.is_inactive():
                                self.holes.remove(21)
                        self.holes.append(17)
                    elif self.game.spotted.position == 6:
                        if 4 in self.holes:
                            if self.game.switches.hole4.is_inactive():
                                self.holes.remove(4)
                        self.holes.append(21)
                    elif self.game.spotted.position == 5:
                        if 22 in self.holes:
                            if self.game.switches.hole22.is_inactive():
                                self.holes.remove(22)
                        self.holes.append(4)
                    elif self.game.spotted.position == 4:
                        if 8 in self.holes:
                            if self.game.switches.hole8.is_inactive():
                                self.holes.remove(8)
                        self.holes.append(22)
                    elif self.game.spotted.position == 3:
                        if 25 in self.holes:
                            if self.game.switches.hole25.is_inactive():
                                self.holes.remove(25)
                        self.holes.append(8)
                    elif self.game.spotted.position == 2:
                        if 12 in self.holes:
                            if self.game.switches.hole12.is_inactive():
                                self.holes.remove(12)
                        self.holes.append(25)
                    elif self.game.spotted.position == 1:
                        if 16 in self.holes:
                            if self.game.switches.hole16.is_inactive():
                                self.holes.remove(16)
                        self.holes.append(12)
                    elif self.game.spotted.position == 0:
                        if 6 in self.holes:
                            if self.game.switches.hole6.is_inactive():
                                self.holes.remove(6)
                        self.holes.append(16)

        self.delay(name="display", delay=0.1, handler=graphics.beach_beauty.display, param=self)



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
        self.cancel_delayed(name="corners_replay_step_up")
        self.game.search_index.disengage()
        self.game.coils.counter.pulse()
        self.game.cu = not self.game.cu
        self.game.spotting.spin()
        self.game.mixer1.spin()
        self.game.mixer2.spin()
        self.game.mixer3.spin()
        self.game.mixer4.spin()
        self.game.reflex.decrease()

        self.game.returned = False
        if self.game.start.status == True:
            if self.game.selector.position < 1:
                self.game.selector.step()
            if self.game.switches.shutter.is_inactive():
                self.game.coils.shutter.enable()
            self.replay_step_down()
            self.check_lifter_status()
        else:
            self.holes = []
            self.game.start.engage(self.game)
            self.game.card1_replay_counter.reset()
            self.game.corners.disengage()
            self.game.corners_replay_counter.reset()
            self.game.start.engage(self.game)
            self.game.selector.reset()
            self.game.super_card.reset()
            self.game.pocket.disengage()
            self.game.pocket_won.disengage()
            self.game.wild_pockets.reset()
            self.game.ball_count.reset()
            self.game.extra_ball.reset()
            self.game.odds.reset()
            self.game.timer.reset()
            self.game.sound.play_music('motor', -1)
            self.regular_play()
        self.delay(name="display", delay=0.1, handler=graphics.beach_beauty.display, param=self)
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
                        if self.game.extra_ball.position >= 3 and self.game.ball_count.position <= 5:
                            if self.game.switches.shooter.is_inactive() and self.game.switches.trough3.is_active():
                                self.game.coils.lifter.enable()
                    if self.game.switches.trough3.is_inactive():
                        if self.game.extra_ball.position >= 6 and self.game.ball_count.position <= 6:
                            if self.game.switches.shooter.is_inactive() and self.game.switches.trough2.is_active():
                                self.game.coils.lifter.enable()
                    if self.game.switches.trough2.is_inactive() and self.game.ball_count.position <= 7:
                        if self.game.extra_ball.position >= 9:
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

        if self.game.pocket.status == True:
            if self.game.ball_count.position >= 4:
                self.game.pocket.disengage()
        self.delay(name="display", delay=0.1, handler=graphics.beach_beauty.display, param=self)


    # This is really nasty, but it is how we render graphics for each individual hole.
    # numbers are added (or removed from) a list.  In this way, I can re-use the same
    # routine even for games where there are ball return functions like Surf Club.

    def sw_hole1_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(1)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            if self.game.one_two_three.status == True:
                if self.game.pocket_won.status == False:
                    self.game.pocket.engage(self.game)
                    self.game.pocket_won.engage(self.game)
                    self.game.pocket_number = 1
            self.delay(name="display", delay=0.1, handler=graphics.beach_beauty.display, param=self)

    def sw_hole2_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(2)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            if self.game.one_two_three.status == True:
                if self.game.pocket_won.status == False:
                    self.game.pocket.engage(self.game)
                    self.game.pocket_won.engage(self.game)
                    self.game.pocket_number = 2
            self.delay(name="display", delay=0.1, handler=graphics.beach_beauty.display, param=self)

    def sw_hole3_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(3)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            if self.game.one_two_three.status == True:
                if self.game.pocket_won.status == False:
                    self.game.pocket.engage(self.game)
                    self.game.pocket_won.engage(self.game)
                    self.game.pocket_number = 3
            self.delay(name="display", delay=0.1, handler=graphics.beach_beauty.display, param=self)

    def sw_hole4_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(4)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            if self.game.four_five_six_seven.status == True:
                if self.game.pocket_won.status == False:
                    self.game.pocket.engage(self.game)
                    self.game.pocket_won.engage(self.game)
                    self.game.pocket_number = 4
            self.delay(name="display", delay=0.1, handler=graphics.beach_beauty.display, param=self)

    def sw_hole5_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(5)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            if self.game.four_five_six_seven.status == True:
                if self.game.pocket_won.status == False:
                    self.game.pocket.engage(self.game)
                    self.game.pocket_won.engage(self.game)
                    self.game.pocket_number = 5
            self.delay(name="display", delay=0.1, handler=graphics.beach_beauty.display, param=self)

    def sw_hole6_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(6)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            if self.game.four_five_six_seven.status == True:
                if self.game.pocket_won.status == False:
                    self.game.pocket.engage(self.game)
                    self.game.pocket_won.engage(self.game)
                    self.game.pocket_number = 6
            self.delay(name="display", delay=0.1, handler=graphics.beach_beauty.display, param=self)

    def sw_hole7_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(7)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            if self.game.four_five_six_seven.status == True:
                if self.game.pocket_won.status == False:
                    self.game.pocket.engage(self.game)
                    self.game.pocket_won.engage(self.game)
                    self.game.pocket_number = 7
            self.delay(name="display", delay=0.1, handler=graphics.beach_beauty.display, param=self)

    def sw_hole8_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(8)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.beach_beauty.display, param=self)

    def sw_hole9_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(9)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.beach_beauty.display, param=self)

    def sw_hole10_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(10)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.beach_beauty.display, param=self)

    def sw_hole11_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(11)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.beach_beauty.display, param=self)

    def sw_hole12_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(12)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.beach_beauty.display, param=self)

    def sw_hole13_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(13)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.beach_beauty.display, param=self)

    def sw_hole14_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(14)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.beach_beauty.display, param=self)

    def sw_hole15_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(15)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.beach_beauty.display, param=self)

    def sw_hole16_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(16)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.beach_beauty.display, param=self)

    def sw_hole17_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(17)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.beach_beauty.display, param=self)

    def sw_hole18_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(18)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.beach_beauty.display, param=self)

    def sw_hole19_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(19)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.beach_beauty.display, param=self)

    def sw_hole20_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(20)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.beach_beauty.display, param=self)

    def sw_hole21_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(21)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.beach_beauty.display, param=self)

    def sw_hole22_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(22)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.beach_beauty.display, param=self)

    def sw_hole23_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(23)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.beach_beauty.display, param=self)

    def sw_hole24_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(24)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.beach_beauty.display, param=self)

    def sw_hole25_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(25)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.beach_beauty.display, param=self)

    def sw_replayReset_active(self, sw):
        self.game.anti_cheat.disengage()
        self.holes = []
#        self.cancel_delayed(name="blink_title")
        graphics.beach_beauty.display(self)
        self.tilt_actions()
#        self.delay(name="blink_title", delay=1, handler=self.blink_title)
        self.replay_step_down(self.game.replays)

    def tilt_actions(self):
        self.game.start.disengage()
        self.cancel_delayed(name="replay_reset")
        self.cancel_delayed(name="card1_replay_step_up")
        self.cancel_delayed(name="corners_replay_step_up")
        self.game.card1_replay_counter.reset()
        self.game.corners.disengage()
        self.game.corners_replay_counter.reset()
        self.game.start.engage(self.game)
        self.game.selector.reset()
        self.game.ball_count.reset()
        self.game.extra_ball.reset()
        self.game.odds.reset()
        self.game.eb_play.disengage()
        self.game.search_index.disengage()
        self.game.super_card.reset()
        self.game.pocket.disengage()
        self.game.pocket_won.disengage()
        self.game.wild_pockets.reset()
        if self.game.ball_count.position == 0:
            if self.game.switches.shutter.is_active():
                self.game.coils.shutter.enable()
        self.holes = []
        self.game.anti_cheat.engage(game)
        self.game.tilt.engage(self.game)
        self.game.sound.stop_music()
        self.game.sound.play('tilt')
        # displays "Tilt" on the backglass, you have to recoin.
        self.delay(name="display", delay=0.1, handler=graphics.beach_beauty.display, param=self)

    def sw_tilt_active(self, sw):
        if self.game.tilt.status == False:
            self.tilt_actions()

    def replay_step_down(self, number=0):
        if number > 0:
            if number > 1:
                self.game.replays -= 1
                graphics.replay_step_down(self.game.replays, graphics.beach_beauty.reel1, graphics.beach_beauty.reel10, graphics.beach_beauty.reel100)
                self.game.coils.registerDown.pulse()
                number -= 1
                graphics.beach_beauty.display(self)
                self.delay(name="replay_reset", delay=0.0, handler=self.replay_step_down, param=number)
            elif number == 1:
                self.game.replays -= 1
                graphics.replay_step_down(self.game.replays, graphics.beach_beauty.reel1, graphics.beach_beauty.reel10, graphics.beach_beauty.reel100)
                self.game.coils.registerDown.pulse()
                number -= 1
                graphics.beach_beauty.display(self)
                self.cancel_delayed(name="replay_reset")
        else: 
            if self.game.replays > 0:
                self.game.replays -= 1
                graphics.replay_step_down(self.game.replays, graphics.beach_beauty.reel1, graphics.beach_beauty.reel10, graphics.beach_beauty.reel100)
                self.delay(name="display", delay=0.1, handler=graphics.beach_beauty.display, param=self)
            self.game.coils.registerDown.pulse()

    def replay_step_up(self):
        if self.game.replays < 899:
            self.game.replays += 1
            graphics.replay_step_up(self.game.replays, graphics.beach_beauty.reel1, graphics.beach_beauty.reel10, graphics.beach_beauty.reel100)
        self.game.coils.registerUp.pulse()
        self.game.reflex.increase()
        graphics.beach_beauty.display(self)

    def sw_yellow_active(self, sw):
        if self.game.ball_count.position >= 5:
            if self.game.eb_play.status == False:
                self.game.spotting.spin()
                self.game.mixer1.spin()
                self.game.mixer2.spin()
                self.game.mixer3.spin()
                self.game.mixer4.spin()
                self.game.eb_play.engage(self.game)
                self.delay(name="display", delay=0.1, handler=graphics.beach_beauty.display, param=self)
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
                self.delay(name="display", delay=0.1, handler=graphics.beach_beauty.display, param=self)
            
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
            self.sc = self.r[3]

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
                        if self.game.selector.position >= 1:
                            if s >= 3:
                                self.find_winner(s, self.card, self.corners, self.sc)
                                break
#        self.delay(name="blink_title", delay=3, handler=self.blink_title)

    def find_winner(self, relays, card, corners, sc):
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
                fiveodds = 120
            elif self.game.odds.position == 5:
                threeodds = 18
                fourodds = 48
                fiveodds = 150
            elif self.game.odds.position == 6:
                threeodds = 24
                fourodds = 64
                fiveodds = 160
            elif self.game.odds.position == 7:
                threeodds = 36
                fourodds = 72
                fiveodds = 180
            elif self.game.odds.position == 8:
                threeodds = 48
                fourodds = 100
                fiveodds = 192
            elif self.game.odds.position == 9:
                threeodds = 64
                fourodds = 200
                fiveodds = 300

            if relays == 3:
                if not corners:
                    if sc == 1 and self.game.super_card.position >= 5:
                        if self.game.card1_replay_counter.position < fourodds:
                            self.game.search_index.engage(self.game)
                            self.card1_replay_step_up(fourodds - self.game.card1_replay_counter.position)
                    elif sc == 2 and self.game.super_card.position >= 10:
                        if self.game.card1_replay_counter.position < fourodds:
                            self.game.search_index.engage(self.game)
                            self.card1_replay_step_up(fourodds - self.game.card1_replay_counter.position)
                    else:
                        if self.game.card1_replay_counter.position < threeodds:
                            self.game.search_index.engage(self.game)
                            self.card1_replay_step_up(threeodds - self.game.card1_replay_counter.position)
            if relays == 4:
                if corners and self.game.corners.status == True:
                    if self.game.corners.status == True:
                        if self.game.corners_replay_counter.position < 300:
                            self.game.search_index.engage(self.game)
                            self.corners_replay_step_up(300 - self.game.corners_replay_counter.position)
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
        self.pos[0] = {}
        self.pos[1] = {9:1, 13:2, 15:3, 24:4, 3:5}
        self.pos[2] = {10:1, 19:2, 14:3, 20:4, 1:5}
        self.pos[3] = {2:1, 18:2, 16:3, 12:4, 25:5}
        self.pos[4] = {8:1, 22:2, 4:3, 21:4, 17:5}
        self.pos[5] = {11:1, 7:2, 5:3, 23:4, 6:5}
        self.pos[6] = {9:1, 10:2, 2:3, 8:4, 11:5}
        self.pos[7] = {13:1, 19:2, 18:3, 22:4, 7:5}
        self.pos[8] = {15:1, 14:2, 16:3, 4:4, 5:5}
        self.pos[9] = {24:1, 20:2, 12:3, 21:4, 23:5}
        self.pos[10] = {3:1, 1:2, 25:3, 17:4, 6:5}
        self.pos[11] = {9:1, 19:2, 16:3, 21:4, 6:5}
        self.pos[12] = {3:1, 20:2, 16:3, 22:4, 11:5}
        self.pos[13] = {}
        self.pos[14] = {9:1, 3:2, 6:3, 11:4}
        self.pos[15] = {}
        self.pos[16] = {}
        self.pos[17] = {15:1, 10:2, 19:3}
        self.pos[18] = {14:1, 20:2, 12:3}
        self.pos[19] = {25:1, 22:2, 17:3}
        self.pos[20] = {15:1, 14:2, 25:3}
        self.pos[21] = {10:1, 20:2, 22:3}
        self.pos[22] = {19:1, 12:2, 17:3}
        self.pos[23] = {15:1, 20:2, 17:3}
        self.pos[24] = {19:1, 20:2, 25:3}
        self.pos[25] = {}
        self.pos[26] = {24:1, 3:2, 14:3}
        self.pos[27] = {1:1, 25:2, 8:3}
        self.pos[28] = {11:1, 5:2, 23:3}
        self.pos[29] = {24:1, 1:2, 11:3}
        self.pos[30] = {3:1, 25:2, 5:3}
        self.pos[31] = {14:1, 8:2, 23:3}
        self.pos[32] = {24:1, 25:2, 23:3}
        self.pos[33] = {14:1, 25:2, 11:3}
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
        sc = 0

        if rivets in range(0, 13):
            card = 1
        if rivets == 14:
            corners = True

        if rivets in range(17, 25):
            sc = 1
        if rivets in range(26, 34):
            sc = 2

        return (self.pos[rivets], card, corners, sc)
    
    def scan_all(self):
        #Animate scanning of everything - this happens through the spotting disc
        self.all_probability()

    def all_probability(self):
        if self.game.odds.position < 3:
            self.game.odds.step()
        #Used Surf Club's mixers - wrong, but lacking documentation.
        mix1 = self.game.mixer1.connected_rivet()
        if self.game.reflex.connected_rivet() == 0 and (mix1 == 1 or mix1 == 9 or mix1 == 15):
            self.scan_odds()
            self.scan_features()
        elif self.game.reflex.connected_rivet() == 1 and (mix1 == 2 or mix1 == 14 or mix1 == 24 or mix1 == 1 or mix1 == 9 or mix1 == 15):
            self.scan_odds()
            self.scan_features()
        elif self.game.reflex.connected_rivet() == 2 and (mix1 == 6 or mix1 == 13 or mix1 == 22 or mix1 == 2 or mix1 == 14 or mix1 == 24 or mix1 == 1 or mix1 == 9 or mix1 == 15):
            self.scan_odds()
            self.scan_features()
        elif self.game.reflex.connected_rivet() == 3:
            self.scan_odds()
            self.scan_features()
        elif self.game.reflex.connected_rivet() == 4:
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
                i = random.randint(1,5)
                self.extra_step(i)
            else:
                self.game.odds.step()

    def extra_step(self, number):
        if number > 0:
            self.game.odds.step()
            self.game.coils.counter.pulse()
            self.delay(name="display", delay=0, handler=graphics.beach_beauty.display, param=self)
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
                if sd == 2:
                    return 1
                else:
                    return 0
            elif self.game.odds.position == 4:
                if sd == 28:
                    return 1
                else:
                    return 0
            elif self.game.odds.position == 5:
                if sd == 58:
                    return 1
                else:
                    return 0
            elif self.game.odds.position == 6:
                if sd == 9:
                    return 1
                else:
                    return 0
            elif self.game.odds.position == 7:
                if sd == 8:
                    return 1
                else:
                    return 0
            elif self.game.odds.position == 8:
                if sd == 7:
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

        if self.game.odds.position > 1:
            m3 = self.check_mixer3()
            if m3 == True:
                m2 = self.check_mixer2()
                if m2 == True:
                    m4 = self.check_mixer4()
                    if m4 == True:
                        self.features_spotting()

    def check_mixer4(self):
        mix4 = self.game.mixer4.position

        if mix4 == 12 or mix4 == 22 or mix4 == 20 or mix4 == 10 or mix4 == 4:
            return 1
        else:
            return 0

    def check_mixer2(self):
        mix2 = self.game.mixer2.position
        odds = self.game.odds.position
        if odds < 4:
            if mix2 != 15 or mix2 != 19 or mix2 != 23 or mix2 != 7 or mix2 != 9:
                return 1
            else:
                return 0
        elif odds == 4:
            if mix2 != 19 or mix2 != 23 or mix2 != 7 or mix2 != 9:
                return 1
            else:
                return 0
        elif odds == 5:
            if mix2 != 23 or mix2 != 7 or mix2 != 9 or mix2 != 15:
                return 1
            else:
                return 0
        elif odds == 6:
            if mix2 != 7 or mix2 != 9 or mix2 != 19 or mix2 != 15:
                return 1
            else:
                return 0
        elif odds == 7 or odds == 8:
            if mix2 != 9 or mix2 != 19 or mix2 != 15 or mix2 != 23:
                return 1
            else:
                return 0

    def check_mixer3(self):
        mix3 = self.game.mixer3.position
        if self.game.cu:
            if mix3 == 3 or mix3 == 5 or mix3 == 7 or mix3 == 10 or mix3 == 12:
                return 1
            else:
                return 0 
        elif mix3 != 22 or mix3 != 20 or mix3 != 17:
            return 1
        else:
            return 0


    def features_spotting(self):
        sd = self.game.spotting.position
        if sd == 34:
            self.step_wild_pockets(12)
        if sd == 1:
            self.step_wild_pockets(6 - self.game.wild_pockets.position)
        if sd == 6:
            if self.game.wild_pockets.position >= 6:
                self.step_wild_pockets(12)
        if sd == 2:
            self.step_wild_pockets(3 - self.game.wild_pockets.position)
        if sd == 8:
            if self.game.wild_pockets.position >= 5:
                self.step_wild_pockets(10 - self.game.wild_pockets.position)
            else:
                self.step_wild_pockets(5 - self.game.wild_pockets.position)
        if self.game.cu:
            self.step_wild_pockets(1)
        else:
            self.step_sc(1)
        if sd == 11:
            self.step_sc(5 - self.game.super_card.position)
        if sd == 30:
            self.step_sc(10)
        if sd == 18:
            self.step_sc(10)
        if sd == 47:
            self.step_sc(4 - self.game.super_card.position)
        if sd == 50:
            if self.game.one_two_three.status == False:
                if self.game.four_five_six_seven.status == False:
                    self.game.corners.engage(self.game)

    def step_sc(self, number):
        if number >= 1:
            self.game.super_card.step()
            number -= 1
            self.delay(name="display", delay=0.1, handler=graphics.beach_beauty.display, param=self)
            self.delay(name="step_sc", delay=0.1, handler=self.step_sc, param=number)

    def step_wild_pockets(self, number):
        if number >= 1:
            self.game.wild_pockets.step()
            if self.game.wild_pockets.position == 5:
                if self.game.cu:
                    self.game.one_two_three.engage(self.game)
                else:
                    self.game.four_five_six_seven.engage(self.game)
            number -= 1
            self.delay(name="display", delay=0.1, handler=graphics.beach_beauty.display, param=self)
            self.delay(name="step_wild_pockets", delay=0.1, handler=self.step_wild_pockets, param=number)


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
        self.delay(name="display", delay=0.1, handler=graphics.beach_beauty.display, param=self)

    def animate_odds_scan(self, s):
        if s > 1:
            self.delay(name="odds_animation", delay=0, handler=graphics.beach_beauty.odds_animation, param=s)
            self.delay(name="display", delay=0.1, handler=graphics.beach_beauty.display, param=self)
            s -= 1
            #self.delay(name="animate_odds", delay=0.1, handler=self.animate_odds_scan, param=s)
        else:
            self.delay(name="display", delay=0.1, handler=graphics.beach_beauty.display, param=self)

    def animate_feature_scan(self, s):
        if s > 1:
            self.delay(name="feature_animation", delay=0.1, handler=graphics.beach_beauty.feature_animation, param=s)
            self.delay(name="display", delay=0.1, handler=graphics.beach_beauty.display, param=self)
            s -= 1
            #self.delay(name="animate_feature", delay=0.1, handler=self.animate_feature_scan, param=s)
        else:
            self.delay(name="display", delay=0.1, handler=graphics.beach_beauty.display, param=self)

    def animate_eb_scan(self, s):
        if s > 1:
            self.delay(name="eb_animation", delay=0.1, handler=graphics.beach_beauty.eb_animation, param=s)
            self.delay(name="display", delay=0.1, handler=graphics.beach_beauty.display, param=self)
            s -= 1
            #self.delay(name="animate_eb", delay=0.1, handler=self.animate_eb_scan, param=s)
        else:
            self.delay(name="display", delay=0.1, handler=graphics.beach_beauty.display, param=self)

    def check_eb_spotting(self):
        sd = self.game.spotting.position
        if sd == 50:
            if self.game.mixer3.position == 24:
                self.step_eb(9 - self.game.extra_ball.position)
        elif sd == 46:
            self.step_eb(3 - self.game.extra_ball.position)
        elif sd == 27:
            if self.game.extra_ball.position < 6:
                self.step_eb(6 - self.game.extra_ball.position)
            else:
                self.step_eb(9 - self.game.extra_ball.position)
        else:
            self.game.extra_ball.step()

    def eb_probability(self):
        #Used Surf Club's mixers - wrong, but lacking documentation.
        mix1 = self.game.mixer1.connected_rivet()

        if self.game.reflex.connected_rivet() == 0 and (mix1 == 1 or mix1 == 9 or mix1 == 15):
            m3 = self.check_mixer3()
            if m3 == 1:
                self.check_eb_spotting()
        elif self.game.reflex.connected_rivet() == 1 and (mix1 == 2 or mix1 == 14 or mix1 == 24 or mix1 == 1 or mix1 == 9 or mix1 == 15):
            m3 = self.check_mixer3()
            if m3 == 1:
                self.check_eb_spotting()
        elif self.game.reflex.connected_rivet() == 2 and (mix1 == 6 or mix1 == 13 or mix1 == 22 or mix1 == 2 or mix1 == 14 or mix1 == 24 or mix1 == 1 or mix1 == 9 or mix1 == 15):
            m3 = self.check_mixer3()
            if m3 == 1:
                self.check_eb_spotting()
        else:
            m3 = self.check_mixer3()
            if m3 == 1:
                self.check_eb_spotting()

    def step_eb(self, number):
        if number >= 1:
            self.game.extra_ball.step()
            self.check_lifter_status()
            number -= 1
            self.delay(name="display", delay=0.1, handler=graphics.beach_beauty.display, param=self)
            self.delay(name="step_eb", delay=0.1, handler=self.step_eb, param=number)

    def blink_title(self):
        title1 = random.randint(0,1)
        title2 = random.randint(0,1)
        title3 = random.randint(0,1)
        title4 = random.randint(0,1)
        if title1 == 1:
            pos = [167,257]
            image = pygame.image.load('beach_beauty/assets/title1_on.png').convert_alpha()
            screen.blit(image, pos)
        if title2 == 1:
            pos = [241,290]
            image = pygame.image.load('beach_beauty/assets/title2_on.png').convert_alpha()
            screen.blit(image, pos)
        if title3 == 1:
            pos = [346,298]
            image = pygame.image.load('beach_beauty/assets/title3_on.png').convert_alpha()
            screen.blit(image, pos)
        if title4 == 1:
            pos = [431,264]
            image = pygame.image.load('beach_beauty/assets/title4_on.png').convert_alpha()
            screen.blit(image, pos)
            
        pygame.display.update()
        self.delay(name="display", delay=0.1, handler=graphics.beach_beauty.display, param=self)
#        self.delay(name="blink_title", delay=3, handler=self.blink_title)

    # Define reset as the knock-off, anti-cheat relay disabled, and replay reset enabled.  Motors turn while credits are knocked off.
    # When meter reaches zero and the zero limit switch is hit, turn off motor sound and leave backglass gi on, but with tilt displayed.

    def startup(self):        
        # Every bingo requires the meter to register '0' 
        # before allowing coin entry --
        # also needs to show a plain 'off' backglass.
        self.eb = False
        self.game.anti_cheat.engage(self.game)
        self.tilt_actions()
#        self.delay(name="blink_title", delay=1, handler=self.blink_title)


class BeachBeauty(procgame.game.BasicGame):
    """ Palm Beach was the first game with Super Cards """
    def __init__(self, machine_type):
        super(BeachBeauty, self).__init__(machine_type)
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
        self.odds = units.Stepper("odds", 9, 'beach_beauty')

        #Replay Counter
        self.card1_replay_counter = units.Stepper("card1_replay_counter", 500)
        #Corners Replay Counter
        self.corners_replay_counter = units.Stepper("corners_replay_counter", 400)

        #Initialize stepper units used to keep track of features or timing.
        self.timer = units.Stepper("timer", 40)
        self.ball_count = units.Stepper("ball_count", 8)

        # Initialize reflex(es) and mixers unique to this game
        # NOTE: reflex unit drawing was not available for this game, so until I convince
        #       another Palm Beach owner to take their game apart, I'll note that there
        #       are five lugs, four of which provide another path to the mixer, and one which is always connected
        #       and bypasses the mixer entirely.  There are no games from 1951 or 52 that have the reflex documented.
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
        self.wild_pockets = units.Stepper("wild_pockets", 12)
        self.spotted = units.Stepper("spotted", 12, "beach_beauty", "continuous")
        self.pocket = units.Relay("pocket")
        self.pocket_won = units.Relay("pocket_won")
        self.pocket_number = 0

        self.super_card = units.Stepper("super_card", 10)

        self.one_two_three = units.Relay("one_two_three")
        self.four_five_six_seven = units.Relay("four_five_six_seven")
        self.wild_red = units.Relay("wild_red")
        self.wild_green = units.Relay("wild_green")

        self.replays = 0
        self.returned = False

    def reset(self):
        super(BeachBeauty, self).reset()
        self.logger = logging.getLogger('game')
        self.load_config('bingo.yaml')
        
        main_mode = SinglecardBingo(self)
        self.modes.add(main_mode)
        
game = BeachBeauty(machine_type='pdb')
game.reset()
game.run_loop()
