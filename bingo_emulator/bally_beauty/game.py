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
from bingo_emulator.graphics.bally_beauty import *

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
            begin = self.game.spotting.position
            self.cancel_delayed("eb_animation")
            self.game.spotting.spin()
            self.animate_eb_scan([begin,self.game.spotting.movement_amount,self.game.spotting.movement_amount])
            self.game.mixer1.spin()
            self.game.mixer2.spin()
            self.game.mixer3.spin()
            self.scan_eb()
            self.replay_step_down()
            self.game.reflex.decrease()

        self.delay(name="display", delay=0.1, handler=graphics.bally_beauty.display, param=self)

    def sw_startButton_active(self, sw):
        self.game.eb_play.disengage()
        if self.game.replays > 0 or self.game.switches.freeplay.is_active():
            self.game.sound.stop('add')
            self.game.sound.play('add')
            self.game.tilt.disengage()
            self.regular_play()
            self.scan_all()
            self.delay(name="display", delay=0.1, handler=graphics.bally_beauty.display, param=self)

    def sw_enter_active(self, sw):
        if self.game.switches.left.is_active() and self.game.switches.right.is_active():
            self.game.end_run_loop()
            os.system("/home/nbaldridge/proc/bingo_emulator/start_game.sh bally_beauty")

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
        self.delay(name="display", delay=0.1, handler=graphics.bally_beauty.display, param=self)

    def sw_left_active(self, sw):
        if self.game.select_spots.status == True:
            if self.game.ball_count.position < 5:
                self.game.spotted.stepdown()
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
                if self.game.spotted.position == 1:
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
                if self.game.spotted.position == 2:
                    if 20 in self.holes:
                        if self.game.switches.hole20.is_inactive():
                            self.holes.remove(20)
                    if 19 in self.holes:
                        if self.game.switches.hole19.is_inactive():
                            self.holes.remove(19)
                    if 22 in self.holes:
                        if self.game.switches.hole22.is_inactive():
                            self.holes.remove(22)
                    if 21 not in self.holes:
                        self.holes.append(21)
                if self.game.spotted.position == 3:
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

            self.delay(name="display", delay=0.1, handler=graphics.bally_beauty.display, param=self)

    def sw_right_active(self, sw):
        if self.game.select_spots.status == True:
            if self.game.ball_count.position < 5:
                self.game.spotted.step()
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
                if self.game.spotted.position == 1:
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
                if self.game.spotted.position == 2:
                    if 20 in self.holes:
                        if self.game.switches.hole20.is_inactive():
                            self.holes.remove(20)
                    if 19 in self.holes:
                        if self.game.switches.hole19.is_inactive():
                            self.holes.remove(19)
                    if 22 in self.holes:
                        if self.game.switches.hole22.is_inactive():
                            self.holes.remove(22)
                    if 21 not in self.holes:
                        self.holes.append(21)
                if self.game.spotted.position == 3:
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
            self.delay(name="display", delay=0.1, handler=graphics.bally_beauty.display, param=self)

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
        self.cancel_delayed(name="card2_replay_step_up")
        self.cancel_delayed(name="card3_replay_step_up")
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
        self.game.reflex.decrease()

        self.game.returned = False
        if self.game.start.status == True:
            if self.game.selector.position < 3:
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
            self.game.card2_replay_counter.reset()
            self.game.card3_replay_counter.reset()
            self.game.super1.disengage()
            self.game.super2.disengage()
            self.game.super3.disengage()
            self.game.corners.disengage()
            self.game.corners_replay_counter.reset()
            self.game.yellow_star.disengage()
            self.game.red_star.disengage()
            self.game.start.engage(self.game)
            self.game.selector.reset()
            self.game.select_spots.disengage()
            self.game.ball_count.reset()
            self.game.extra_ball.reset()
            self.game.odds.reset()
            self.game.timer.reset()
            self.game.sound.play_music('motor', -1)
            self.regular_play()
        self.delay(name="display", delay=0.1, handler=graphics.bally_beauty.display, param=self)
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
        if self.game.ball_count.position == 4 or self.game.ball_count.position == 5:
            self.delay(name="display", delay=0.1, handler=graphics.bally_beauty.display, param=self)
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

    # This is really nasty, but it is how we render graphics for each individual hole.
    # numbers are added (or removed from) a list.  In this way, I can re-use the same
    # routine even for games where there are ball return functions like Surf Club.

    def sw_hole1_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(1)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.bally_beauty.display, param=self)

    def sw_hole2_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(2)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.bally_beauty.display, param=self)

    def sw_hole3_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(3)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.bally_beauty.display, param=self)

    def sw_hole4_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(4)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.bally_beauty.display, param=self)

    def sw_hole5_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(5)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.bally_beauty.display, param=self)

    def sw_hole6_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(6)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.bally_beauty.display, param=self)

    def sw_hole7_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(7)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.bally_beauty.display, param=self)

    def sw_hole8_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(8)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.bally_beauty.display, param=self)

    def sw_hole9_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(9)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.bally_beauty.display, param=self)

    def sw_hole10_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(10)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.bally_beauty.display, param=self)

    def sw_hole11_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(11)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.bally_beauty.display, param=self)

    def sw_hole12_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(12)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.bally_beauty.display, param=self)

    def sw_hole13_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(13)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.bally_beauty.display, param=self)

    def sw_hole14_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(14)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.bally_beauty.display, param=self)

    def sw_hole15_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(15)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.bally_beauty.display, param=self)

    def sw_hole16_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(16)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.bally_beauty.display, param=self)

    def sw_hole17_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(17)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.bally_beauty.display, param=self)

    def sw_hole18_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(18)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.bally_beauty.display, param=self)

    def sw_hole19_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(19)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.bally_beauty.display, param=self)

    def sw_hole20_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(20)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.bally_beauty.display, param=self)

    def sw_hole21_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(21)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.bally_beauty.display, param=self)

    def sw_hole22_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(22)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.bally_beauty.display, param=self)

    def sw_hole23_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(23)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.bally_beauty.display, param=self)

    def sw_hole24_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(24)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.bally_beauty.display, param=self)

    def sw_hole25_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(25)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.bally_beauty.display, param=self)

    def sw_replayReset_active(self, sw):
        self.game.anti_cheat.disengage()
        self.holes = []
        self.delay(name="display", delay=0.1, handler=graphics.bally_beauty.display, param=self)
        self.tilt_actions()
        self.replay_step_down(self.game.replays)

    def sw_redstar_active(self, sw):
        if self.game.red_star.status == True:
            if self.game.all_spot.status == False:
                self.game.all_spot.engage(self.game)
                if 2 not in self.holes:
                    self.holes.append(2)
                if 4 not in self.holes:
                    self.holes.append(4)
                if 6 not in self.holes:
                    self.holes.append(6)
            self.delay(name="display", delay=0.1, handler=graphics.bally_beauty.display, param=self)
            if self.game.ball_count >= 5:
                self.search()

    def sw_yellowstar_active(self, sw):
        if self.game.yellow_star.status == True:
            if self.game.all_spot.status == False:
                self.game.all_spot.engage(self.game)
                if 2 not in self.holes:
                    self.holes.append(2)
                if 4 not in self.holes:
                    self.holes.append(4)
                if 6 not in self.holes:
                    self.holes.append(6)
            self.delay(name="display", delay=0.1, handler=graphics.bally_beauty.display, param=self)
            if self.game.ball_count >= 5:
                self.search()

    def tilt_actions(self):
        self.game.start.disengage()
        self.cancel_delayed(name="replay_reset")
        self.cancel_delayed(name="card1_replay_step_up")
        self.cancel_delayed(name="card2_replay_step_up")
        self.cancel_delayed(name="card3_replay_step_up")
        self.cancel_delayed(name="corners_replay_step_up")
        self.cancel_delayed(name="blink")
        self.cancel_delayed(name="timeout")
        self.game.search_index.disengage()
        if self.game.ball_count.position == 0:
            if self.game.switches.shutter.is_active():
                self.game.coils.shutter.enable()
        self.holes = []
        self.game.selector.reset()
        self.game.select_spots.disengage()
        self.game.card1_replay_counter.reset()
        self.game.corners.disengage()
        self.game.corners_replay_counter.reset()
        self.game.super1.disengage()
        self.game.super2.disengage()
        self.game.super3.disengage()
        self.game.yellow_star.disengage()
        self.game.red_star.disengage()
        self.game.ball_count.reset()
        self.game.odds.reset()
        self.game.eb_play.disengage()
        self.game.extra_ball.reset()
        self.game.anti_cheat.engage(game)
        self.game.tilt.engage(self.game)
        self.game.sound.stop_music()
        self.game.sound.play('tilt')
        # displays "Tilt" on the backglass, you have to recoin.
        self.delay(name="display", delay=0.1, handler=graphics.bally_beauty.display, param=self)

    def sw_tilt_active(self, sw):
        if self.game.tilt.status == False:
            self.tilt_actions()

    def replay_step_down(self, number=0):
        if number > 0:
            if number > 1:
                self.game.replays -= 1
                graphics.replay_step_down(self.game.replays, graphics.bally_beauty.reel1, graphics.bally_beauty.reel10, graphics.bally_beauty.reel100)
                self.game.coils.registerDown.pulse()
                number -= 1
                graphics.bally_beauty.display(self)
                self.delay(name="replay_reset", delay=0.13, handler=self.replay_step_down, param=number)
            elif number == 1:
                self.game.replays -= 1
                graphics.replay_step_down(self.game.replays, graphics.bally_beauty.reel1, graphics.bally_beauty.reel10, graphics.bally_beauty.reel100)
                self.game.coils.registerDown.pulse()
                number -= 1
                graphics.bally_beauty.display(self)
                self.cancel_delayed(name="replay_reset")
        else: 
            if self.game.replays > 0:
                self.game.replays -= 1
                graphics.replay_step_down(self.game.replays, graphics.bally_beauty.reel1, graphics.bally_beauty.reel10, graphics.bally_beauty.reel100)
                self.delay(name="display", delay=0.1, handler=graphics.bally_beauty.display, param=self)
            self.game.coils.registerDown.pulse()

    def replay_step_up(self):
        if self.game.replays < 899:
            self.game.replays += 1
            graphics.replay_step_up(self.game.replays, graphics.bally_beauty.reel1, graphics.bally_beauty.reel10, graphics.bally_beauty.reel100)
        self.game.coils.registerUp.pulse()
        self.game.reflex.increase()
        graphics.bally_beauty.display(self)

    def sw_yellow_active(self, sw):
        if self.game.ball_count.position >= 5:
            if self.game.eb_play.status == False:
                self.game.spotting.spin()
                self.game.mixer1.spin()
                self.game.mixer2.spin()
                self.game.mixer3.spin()
                self.game.eb_play.engage(self.game)
                self.delay(name="display", delay=0.1, handler=graphics.bally_beauty.display, param=self)
                self.sw_yellow_active(sw)
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
                self.scan_eb()
                self.replay_step_down()
                self.game.reflex.decrease()
                self.delay(name="display", delay=0.1, handler=graphics.bally_beauty.display, param=self)
            
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
                                self.find_winner(s, self.card, self.corners)
                                break

    def find_winner(self, relays, card, corners):

        if self.game.search_index.status == False and self.game.replays < 899:
            if card == 1:
                if relays == 3:
                    if not corners:
                        if self.game.super1.status == True:
                            if self.game.odds.position == 1:
                                hit = 6
                            elif self.game.odds.position == 2:
                                hit = 8
                            elif self.game.odds.position == 3:
                                hit = 12
                            elif self.game.odds.position == 4:
                                hit = 16
                            elif self.game.odds.position == 5:
                                hit = 24
                        else:
                            hit = 4
                        if self.game.card1_replay_counter.position < hit:
                            self.game.search_index.engage(self.game)
                            self.card1_replay_step_up(hit - self.game.card1_replay_counter.position)
                if relays == 4:
                    if corners and self.game.corners.status == True:
                        if self.game.corners_replay_counter.position < 200:
                            self.game.search_index.engage(self.game)
                            self.corners_replay_step_up(200 - self.game.corners_replay_counter.position)
                    else:
                        if not corners:
                            if self.game.super1.status == True:
                                if self.game.odds.position == 1:
                                    hit = 30
                                elif self.game.odds.position == 2:
                                    hit = 40
                                elif self.game.odds.position == 3:
                                    hit = 60
                                elif self.game.odds.position == 4:
                                    hit = 80
                                elif self.game.odds.position == 5:
                                    hit = 120
                            else:
                                hit = 20
                            if self.game.card1_replay_counter.position < hit:
                                self.game.search_index.engage(self.game)
                                self.card1_replay_step_up(hit - self.game.card1_replay_counter.position)
                if relays == 5:
                    if self.game.super1.status == True:
                        if self.game.odds.position == 1:
                            hit = 96
                        elif self.game.odds.position == 2:
                            hit = 100
                        elif self.game.odds.position == 3:
                            hit = 150
                        elif self.game.odds.position == 4:
                            hit = 200
                        elif self.game.odds.position == 5:
                            hit = 300
                    else:
                        hit = 96

                    if self.game.card1_replay_counter.position < hit:
                        self.game.search_index.engage(self.game)
                        self.card1_replay_step_up(hit - self.game.card1_replay_counter.position)
            if card == 2:
                if relays == 3:
                    if not corners:
                        if self.game.super2.status == True:
                            if self.game.odds.position == 1:
                                hit = 6
                            elif self.game.odds.position == 2:
                                hit = 8
                            elif self.game.odds.position == 3:
                                hit = 12
                            elif self.game.odds.position == 4:
                                hit = 16
                            elif self.game.odds.position == 5:
                                hit = 24
                        else:
                            hit = 4
                        if self.game.card2_replay_counter.position < hit:
                            self.game.search_index.engage(self.game)
                            self.card2_replay_step_up(hit - self.game.card2_replay_counter.position)
                if relays == 4:
                    if corners and self.game.corners.status == True:
                        if self.game.corners_replay_counter.position < 200:
                            self.game.search_index.engage(self.game)
                            self.corners_replay_step_up(200 - self.game.corners_replay_counter.position)
                    else:
                        if not corners:
                            if self.game.super2.status == True:
                                if self.game.odds.position == 1:
                                    hit = 30
                                elif self.game.odds.position == 2:
                                    hit = 40
                                elif self.game.odds.position == 3:
                                    hit = 60
                                elif self.game.odds.position == 4:
                                    hit = 80
                                elif self.game.odds.position == 5:
                                    hit = 120
                            else:
                                hit = 20
                            if self.game.card2_replay_counter.position < hit:
                                self.game.search_index.engage(self.game)
                                self.card2_replay_step_up(hit - self.game.card2_replay_counter.position)
                if relays == 5:
                    if self.game.super2.status == True:
                        if self.game.odds.position == 1:
                            hit = 96
                        elif self.game.odds.position == 2:
                            hit = 100
                        elif self.game.odds.position == 3:
                            hit = 150
                        elif self.game.odds.position == 4:
                            hit = 200
                        elif self.game.odds.position == 5:
                            hit = 300
                    else:
                        hit = 96

                    if self.game.card2_replay_counter.position < hit:
                        self.game.search_index.engage(self.game)
                        self.card2_replay_step_up(hit - self.game.card2_replay_counter.position)
            if card == 3:
                if relays == 3:
                    if not corners:
                        if self.game.super3.status == True:
                            if self.game.odds.position == 1:
                                hit = 6
                            elif self.game.odds.position == 2:
                                hit = 8
                            elif self.game.odds.position == 3:
                                hit = 12
                            elif self.game.odds.position == 4:
                                hit = 16
                            elif self.game.odds.position == 5:
                                hit = 24
                        else:
                            hit = 4
                        if self.game.card3_replay_counter.position < hit:
                            self.game.search_index.engage(self.game)
                            self.card3_replay_step_up(hit - self.game.card3_replay_counter.position)
                if relays == 4:
                    if corners and self.game.corners.status == True:
                        if self.game.corners_replay_counter.position < 200:
                            self.game.search_index.engage(self.game)
                            self.corners_replay_step_up(200 - self.game.corners_replay_counter.position)
                    else:
                        if not corners:
                            if self.game.super3.status == True:
                                if self.game.odds.position == 1:
                                    hit = 30
                                elif self.game.odds.position == 2:
                                    hit = 40
                                elif self.game.odds.position == 3:
                                    hit = 60
                                elif self.game.odds.position == 4:
                                    hit = 80
                                elif self.game.odds.position == 5:
                                    hit = 120
                            else:
                                hit = 20
                            if self.game.card3_replay_counter.position < hit:
                                self.game.search_index.engage(self.game)
                                self.card3_replay_step_up(hit - self.game.card3_replay_counter.position)
                if relays == 5:
                    if self.game.super3.status == True:
                        if self.game.odds.position == 1:
                            hit = 96
                        elif self.game.odds.position == 2:
                            hit = 100
                        elif self.game.odds.position == 3:
                            hit = 150
                        elif self.game.odds.position == 4:
                            hit = 200
                        elif self.game.odds.position == 5:
                            hit = 300
                    else:
                        hit = 96

                    if self.game.card3_replay_counter.position < hit:
                        self.game.search_index.engage(self.game)
                        self.card3_replay_step_up(hit - self.game.card3_replay_counter.position)


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
        self.pos[0] = {}
        self.pos[1] = {5:1, 1:2, 9:3, 25:4, 3:5}
        self.pos[2] = {8:1, 22:2, 10:3, 19:4, 7:5}
        self.pos[3] = {6:1, 18:2, 16:3, 11:4, 17:5}
        self.pos[4] = {24:1, 21:2, 14:3, 20:4, 13:5}
        self.pos[5] = {12:1, 23:2, 2:3, 4:4, 15:5}
        self.pos[6] = {5:1, 8:2, 6:3, 24:4, 12:5}
        self.pos[7] = {1:1, 22:2, 18:3, 21:4, 23:5}
        self.pos[8] = {9:1, 10:2, 16:3, 14:4, 2:5}
        self.pos[9] = {25:1, 19:2, 11:3, 20:4, 4:5}
        self.pos[10] = {3:1, 7:2, 17:3, 13:4, 15:5}
        self.pos[11] = {3:1, 19:2, 16:3, 21:4, 12:5}
        self.pos[12] = {5:1, 22:2, 16:3, 20:4, 15:5}
        self.pos[13] = {5:1, 3:2, 15:3, 12:4}
        self.pos[14] = {}
        self.pos[15] = {}
        self.pos[16] = {}
        self.pos[17] = {9:1, 24:2, 16:3, 4:4, 6:5}
        self.pos[18] = {13:1, 19:2, 14:3, 20:4, 25:5}
        self.pos[19] = {2:1, 18:2, 15:3, 12:4, 17:5}
        self.pos[20] = {1:1, 22:2, 11:3, 21:4, 8:5}
        self.pos[21] = {10:1, 7:2, 5:3, 23:4, 3:5}
        self.pos[22] = {9:1, 13:2, 2:3, 1:4, 10:5}
        self.pos[23] = {24:1, 19:2, 18:3, 22:4, 7:5}
        self.pos[24] = {16:1, 14:2, 15:3, 11:4, 5:5}
        self.pos[25] = {4:1, 20:2, 12:3, 21:4, 23:5}
        self.pos[26] = {6:1, 25:2, 17:3, 8:4, 3:5}
        self.pos[27] = {6:1, 20:2, 15:3, 22:4, 10:5}
        self.pos[28] = {9:1, 19:2, 15:3, 21:4, 3:5}
        self.pos[29] = {9:1, 6:2, 3:3, 10:4}
        self.pos[30] = {}
        self.pos[31] = {}
        self.pos[32] = {}
        self.pos[33] = {24:1, 7:2, 10:3, 4:4, 9:5}
        self.pos[34] = {3:1, 21:2, 18:3, 22:4, 8:5}
        self.pos[35] = {15:1, 14:2, 17:3, 11:4, 2:5}
        self.pos[36] = {13:1, 20:2, 12:3, 19:4, 23:5}
        self.pos[37] = {25:1, 6:2, 16:3, 1:4, 5:5}
        self.pos[38] = {24:1, 3:2, 15:3, 13:4, 25:5}
        self.pos[39] = {7:1, 21:2, 14:3, 20:4, 6:5}
        self.pos[40] = {10:1, 18:2, 17:3, 12:4, 16:5}
        self.pos[41] = {4:1, 22:2, 11:3, 19:4, 1:5}
        self.pos[42] = {9:1, 8:2, 2:3, 23:4, 5:5}
        self.pos[43] = {9:1, 22:2, 17:3, 20:4, 25:5}
        self.pos[44] = {24:1, 21:2, 17:3, 19:4, 5:5}
        self.pos[45] = {24:1, 9:2, 5:3, 25:4}
        self.pos[46] = {}
        self.pos[47] = {}
        self.pos[48] = {}
        self.pos[49] = {}
        self.pos[50] = {}

        corners = False
        card = 0

        if rivets in range(0, 14):
            card = 1
        if rivets == 13:
            corners = True
        if rivets in range(16, 30):
            card = 2
        if rivets == 29:
            corners = True
        if rivets in range(32, 46):
            card = 3
        if rivets == 45:
            corners = True

        return (self.pos[rivets], card, corners)
    
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
            s = random.randint(1,5)
            self.animate_odds_scan(s)
            #s = random.randint(1,7)
            #self.animate_feature_scan(s)

    def scan_odds(self):
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
            self.delay(name="display", delay=0, handler=graphics.bally_beauty.display, param=self)
            number -= 1
            self.delay(name="extra_step", delay=0.1, handler=self.extra_step, param=number)

    def check_extra_step(self):
        i = random.randint(0,32)
        if i == 16:
            return 1
        else:
            return 0

    def odds_probability(self):
        mix5 = self.game.mixer3.connected_rivet()
        # Check position of Mixer 5, Mixer 4, and Mixer 3 and current 
        # position of the odds, along with trip relays.
        # For first check, guaranteed single stepup.  Probability doesn't 
        # factor, so I will return as part of the initial check above.
        if self.game.odds.position == 0:
            return 1
        else:
            m2 = self.check_mixer2()
            if m2 == True:
                s = self.game.spotting.connected_rivet()
                if s in [2,13,18]:
                    if self.game.odds.position == 4:
                        if self.game.mixer3.position == 4:
                            return 1
                        else:
                            return 0
                    else:
                        return 1
                else:
                    return 0
            else:
                return 0



    def check_sd(self):
        sd = self.game.spotting.connected_rivet()
        if self.game.odds.position in [4,5]:
            if sd in [4,6,8,9,11,12,13,19,20,22,23,25,27,29,32,35,36,38,41,45,48,50]:
                return 1
            else:
                return 0
        elif self.game.odds.position == 6:
            if sd in [2,3,14,17,24,31,39,40,46,47]:
                return 1
            else:
                return 0
        elif self.game.odds.position == 7:
            if sd in [5,7,16,26,34,37,42]:
                return 1
            else:
                return 0
        elif self.game.odds.position == 8:
            if sd in [10,16,28,44]:
                return 1
            else:
                return 0
        elif self.game.odds.position == 9:
            if sd in [18,30,43]:
                return 1
            else:
                return 0
        else:
            return 0

    def check_mixer2(self):
        mix2 = self.game.mixer2.connected_rivet()
        if mix2 in [1,4,8,9,10,13,15,16,18,19,20]:
            return 1
        elif self.game.super1.status == False:
            if mix2 == 22:
                return 1
        elif self.game.super2.status == False:
            if mix2 == 3:
                return 1
        elif self.game.super3.status == False:
            if mix2 == 24:
                return 1
        else:
            return 0

    def scan_features(self):
        p = self.features_probability()

    def features_probability(self):
        s = random.randint(1,7)
        self.animate_feature_scan(s)
        mix2 = self.game.mixer2.connected_rivet()
        mix3 = self.game.mixer3.connected_rivet()
        if self.game.selector.position < 3:
            if mix3 in [24,1,12,13] or self.game.reflex.connected_rivet() == 4:
                if self.game.odds.position in [0,1]:
                    if self.game.spotting.position in [4,7,11,13,30,32,33,41,45,48]:
                        self.game.select_spots.engage(self.game)
                        self.check_spot()
                    if self.game.spotting.position in [2,8,21,25,29]:
                        self.game.super1.engage(self.game)
                    if self.game.spotting.position in [9,39]:
                        self.game.corners.engage(self.game)
                    if self.game.spotting.position in [6,15,24,44]:
                        self.game.yellow_star.engage(self.game)
                        self.game.coils.redROLamp.enable()
                    if self.game.spotting.position in [20,37]:
                        self.game.super2.engage(self.game)
                    if self.game.spotting.position in [2,36]:
                        self.game.red_star.engage(self.game)
                        self.game.coils.yellowROLamp.enable()
                    if self.game.spotting.position in [3,8,21,22,25,29,35]:
                        self.game.super3.engage(self.game)
                else:
                    if mix2 in [1,2,3,4,21,22,23]:
                        if self.game.spotting.position in [4,7,11,13,30,32,33,41,45,48]:
                            self.game.select_spots.engage(self.game)
                            self.check_spot()
                        if self.game.spotting.position in [2,8,21,25,29]:
                            self.game.super1.engage(self.game)
                        if self.game.spotting.position in [9,39]:
                            self.game.corners.engage(self.game)
                        if self.game.spotting.position in [6,15,24,44]:
                            self.game.yellow_star.engage(self.game)
                            self.game.coils.redROLamp.enable()
                        if self.game.spotting.position in [20,37]:
                            self.game.super2.engage(self.game)
                        if self.game.spotting.position in [2,36]:
                            self.game.red_star.engage(self.game)
                            self.game.coils.yellowROLamp.enable()
                        if self.game.spotting.position in [3,8,21,22,25,29,35]:
                            self.game.super3.engage(self.game)
        else:
            if self.game.odds.position in [0,1]:
                if self.game.spotting.position in [4,7,11,13,30,32,33,41,45,48]:
                    self.game.select_spots.engage(self.game)
                    self.check_spot()
                if self.game.spotting.position in [2,8,21,25,29]:
                    self.game.super1.engage(self.game)
                if self.game.spotting.position in [9,39]:
                    self.game.corners.engage(self.game)
                if self.game.spotting.position in [6,15,24,44]:
                    self.game.yellow_star.engage(self.game)
                    self.game.coils.redROLamp.enable()
                if self.game.spotting.position in [20,37]:
                    self.game.super2.engage(self.game)
                if self.game.spotting.position in [2,36]:
                    self.game.red_star.engage(self.game)
                    self.game.coils.yellowROLamp.enable()
                if self.game.spotting.position in [3,8,21,22,25,29,35]:
                    self.game.super3.engage(self.game)
            else:
                if mix2 in [1,2,3,4,21,22,23]:
                    if self.game.spotting.position in [4,7,11,13,30,32,33,41,45,48]:
                        self.game.select_spots.engage(self.game)
                        self.check_spot()
                    if self.game.spotting.position in [2,8,21,25,29]:
                        self.game.super1.engage(self.game)
                    if self.game.spotting.position in [9,39]:
                        self.game.corners.engage(self.game)
                    if self.game.spotting.position in [6,15,24,44]:
                        self.game.yellow_star.engage(self.game)
                        self.game.coils.redROLamp.enable()
                    if self.game.spotting.position in [20,37]:
                        self.game.super2.engage(self.game)
                    if self.game.spotting.position in [2,36]:
                        self.game.red_star.engage(self.game)
                        self.game.coils.yellowROLamp.enable()
                    if self.game.spotting.position in [3,8,21,22,25,29,35]:
                        self.game.super3.engage(self.game)

    def scan_eb(self):
        if self.game.extra_ball.position == 0:
            self.game.extra_ball.step()
            self.check_lifter_status()
        p = self.eb_probability()
        if p == 1:
            if self.game.extra_ball.position < 9:
                m = self.eb_mixer2()
                if m == 1:
                    t = self.eb_mixer3()
                    if t == 1:
                        s = self.eb_check()

        # Timer resets to 0 position on ball count increasing.  We are fudging this since we will have
        # no good way to measure balls as they return back to the trough.  The ball count unit cannot be
        # relied upon as we do not have a switch in the outhole, and the trough logic is too complex for
        # the task at hand.
        self.game.timer.reset()
        self.delay(name="display", delay=0, handler=graphics.bally_beauty.display, param=self)

    def animate_odds_scan(self, s):
        if s > 1:
            self.delay(name="odds_animation", delay=0.1, handler=graphics.bally_beauty.odds_animation, param=s)
            self.delay(name="display", delay=0.1, handler=graphics.bally_beauty.display, param=self)
            s -= 1
            #self.delay(name="animate_odds", delay=0.1, handler=self.animate_odds_scan, param=s)
        else:
            self.cancel_delayed(name="odds_animation")
            self.cancel_delayed(name="display")

    def animate_feature_scan(self, s):
        if s > 1:
            self.delay(name="feature_animation", delay=0.1, handler=graphics.bally_beauty.feature_animation, param=s)
            self.delay(name="display", delay=0.1, handler=graphics.bally_beauty.display, param=self)
            s -= 1
            #self.delay(name="animate_feature", delay=0.1, handler=self.animate_feature_scan, param=s)
        else:
            self.delay(name="display", delay=0.1, handler=graphics.bally_beauty.display, param=self)

    def animate_eb_scan(self, args):
        start = args[0]
        diff = args[1]
        num = args[2]
        if start + num >= 50:
            start = 0
        if diff >= 0:
            num = num + 1
            graphics.bally_beauty.eb_animation([self, start + num])
            self.cancel_delayed(name="display")
            diff = diff - 1
            args = [start,diff,num]
            self.delay(name="eb_animation", delay=0.06, handler=self.animate_eb_scan, param=args)
        else:
            self.cancel_delayed(name="eb_animation")
            self.delay(name="display", delay=0.1, handler=graphics.bally_beauty.display, param=self)

    def eb_probability(self):
        mix1 = self.game.mixer1.connected_rivet()
        if self.game.reflex.connected_rivet() == 0 and (mix1 in [1,6,8,11,13,16,18,22,24]):
            return 1
        elif self.game.reflex.connected_rivet() == 1 and (mix1 not in [2,5,7,9,12,14,15,19,23]):
            return 1
        elif self.game.reflex.connected_rivet() == 2 and (mix1 not in [5,9,12,15,19,23]):
            return 1
        elif self.game.reflex.connected_rivet() == 3 and (mix1 not in [5,9,15,23]):
            return 1
        elif self.game.reflex.connected_rivet() == 4:
            return 1
        else:
            return 0

    def eb_mixer2(self):
        o = self.game.odds.position
        mix2 = self.game.mixer2.connected_rivet()
        if o >= 4:
            if self.game.super1.status == False:
                if mix2 in [22,11,5,24,6,8]:
                    return 1
            if self.game.super2.status == False:
                if mix2 in [22,13,5,24,6,8]:
                    return 1
            if self.game.super3.status == False:
                if mix2 in [22,20,5,24,6,8]:
                    return 1
            if mix2 in [22,5,24,6,8]:
                return 1
            else:
                return 0
        if o >= 3:
            if self.game.super1.status == False:
                if mix2 in [22,11,5,24,6,8,10]:
                    return 1
            if self.game.super2.status == False:
                if mix2 in [22,13,5,24,6,8,10]:
                    return 1
            if self.game.super3.status == False:
                if mix2 in [22,20,5,24,6,8,10]:
                    return 1
            if mix2 in [22,5,24,6,8,10]:
                return 1
            else:
                return 0
        if o >= 2:
            if self.game.super1.status == False:
                if mix2 in [22,11,5,24,6,8,10,12]:
                    return 1
            if self.game.super2.status == False:
                if mix2 in [22,13,5,24,6,8,10,12]:
                    return 1
            if self.game.super3.status == False:
                if mix2 in [22,20,5,24,6,8,10,12]:
                    return 1
            if mix2 in [22,5,24,6,8,10,12]:
                return 1
            else:
                return 0
        if o <= 1:
            if self.game.super1.status == False:
                if mix2 in [22,11,5,24,6,8,10,12,15]:
                    return 1
            if self.game.super2.status == False:
                if mix2 in [22,13,5,24,6,8,10,12,15]:
                    return 1
            if self.game.super3.status == False:
                if mix2 in [22,20,5,24,6,8,10,12,15]:
                    return 1
            if mix2 in [22,5,24,6,8,10,12,15]:
                return 1
            else:
                return 0

    def eb_mixer3(self):
        mix3 = self.game.mixer3.connected_rivet()
        if self.game.select_spots.status == False:
            if self.game.all_spot.status == False:
                return 1
            else:
                return 0
        else:
            if mix3 is not 21:
                return 1
            else:
                return 0

    def eb_check(self):
        sd = self.game.spotting.connected_rivet()
        eb = self.game.extra_ball.position

        if sd == 29 and self.game.mixer3.connected_rivet() == 21:
            self.step_eb(9 - eb)
        if sd == 6:
            if eb < 3:
                self.step_eb(3 - eb)
        if sd == 3:
            if eb < 6:
                self.step_eb(6 - eb)
        if sd == 20:
            if eb < 9:
                self.step_eb(9 - eb)
        if eb < 3:
            if sd == 8:
                self.step_eb(1)
        if eb >= 3 and eb < 6:
            if sd == 13:
                self.step_eb(1)
        if sd == 4 or sd == 5:
            self.step_eb(1)

    def step_eb(self, number):
        if number >= 1:
            self.game.extra_ball.step()
            self.check_lifter_status()
            number -= 1
            self.delay(name="display", delay=0, handler=graphics.bally_beauty.display, param=self)
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

class BallyBeauty(procgame.game.BasicGame):
    """ Bally Beauty was the first game with select-a-spot """
    def __init__(self, machine_type):
        super(BallyBeauty, self).__init__(machine_type)
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

        #Odds stepper
        self.odds = units.Stepper("odds", 5, 'bally_beauty')

        #Replay Counter
        self.card1_replay_counter = units.Stepper("card1_replay_counter", 500)
        self.card2_replay_counter = units.Stepper("card1_replay_counter", 500)
        self.card3_replay_counter = units.Stepper("card1_replay_counter", 500)
        #Corners Replay Counter
        self.corners_replay_counter = units.Stepper("corners_replay_counter", 200)

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

        self.selector = units.Stepper("selector", 3)

        # Select-a-spot setup
        self.select_spots = units.Relay("select_spots")
        self.spotted = units.Stepper("spotted", 3, "bally_beauty", "continuous")

        #Some special trip relays for spotted numbers and rollovers
        self.red_star = units.Relay("red_star")
        self.yellow_star = units.Relay("yellow_star")

        self.super1 = units.Relay("super1")
        self.super2 = units.Relay("super2")
        self.super3 = units.Relay("super3")
        self.all_spot = units.Relay("all_spot")
        
        self.replays = 0
        self.returned = False

    def reset(self):
        super(BallyBeauty, self).reset()
        self.logger = logging.getLogger('game')
        self.load_config('bingo.yaml')
        
        main_mode = SinglecardBingo(self)
        self.modes.add(main_mode)
         
game = BallyBeauty(machine_type='pdb')
game.reset()
game.run_loop()
