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
from bingo_emulator.graphics.double_header import *

class SinglecardBingo(procgame.game.Mode):
    def __init__(self, game):
        super(SinglecardBingo, self).__init__(game=game, priority=5)
        self.holes = []
        self.holes2 = []
        self.startup()
        self.game.game1.engage(self.game)
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

        self.delay(name="display", delay=0.1, handler=graphics.double_header.display, param=self)

    def sw_startButton_active(self, sw):
        self.game.eb_play.disengage()
        self.game.game1.engage(self.game)
        self.game.game2.disengage()
        if self.game.replays > 0 or self.game.switches.freeplay.is_active():
            self.game.sound.stop('add')
            self.game.sound.play('add')
            self.game.tilt.disengage()
            self.regular_play()
            self.scan_all()
        self.delay(name="display", delay=0.1, handler=graphics.double_header.display, param=self)

    def sw_enter_active(self, sw):
        if self.game.switches.left.is_active() and self.game.switches.right.is_active():
            self.game.end_run_loop()
            os.system("/home/nbaldridge/proc/bingo_emulator/start_game.sh double_header")

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
        max_ball = 4
        if self.game.ball_count.position < max_ball:
            if self.game.magic_squares_feature.position >= 5:
                self.game.square_a.step()
        self.delay(name="display", delay=0.1, handler=graphics.double_header.display, param=self)

    def sw_right_active(self, sw):
        max_ball = 4
        if self.game.ball_count.position < max_ball:
            if self.game.magic_squares_feature.position >= 5:
                self.game.square_b.step()

        self.delay(name="display", delay=0.1, handler=graphics.double_header.display, param=self)

    def sw_blue_active(self, sw):
        max_ball = 4
        if self.game.ball_count.position < max_ball:
            if self.game.magic_squares_feature.position >= 5:
                self.game.square_c.step()

        self.delay(name="display", delay=0.1, handler=graphics.double_header.display, param=self)

    def sw_green_active(self, sw):
        if self.game.game1.status == True:
            self.game.game1.disengage()
            self.game.game2.engage(self.game)
            self.delay(name="display", delay=0.1, handler=graphics.double_header.display, param=self)
        if self.game.replays > 0 or self.game.switches.freeplay.is_active():
            self.game.sound.stop('add')
            self.game.sound.play('add')
            self.game.tilt.disengage()
            self.regular_play()
            self.scan_all()
            self.delay(name="display", delay=0.1, handler=graphics.double_header.display, param=self)
        max_ball = 4
        if self.game.ball_count.position < max_ball:
            if self.game.magic_squares_feature.position >= 7:
                self.game.square_d.step()

        self.delay(name="display", delay=0.1, handler=graphics.double_header.display, param=self)


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
            self.holes2= []
            self.game.start.engage(self.game)
            self.game.card1_replay_counter.reset()
            self.game.card2_replay_counter.reset()
            self.game.corners_replay_counter.reset()
            self.game.corners.disengage()
            self.game.spot_12.disengage()
            self.game.spot_13.disengage()
            self.game.selection_feature.reset()
            self.game.start.engage(self.game)
            self.game.selector.reset()
            self.game.magic_squares_feature.reset()
            self.game.red_double.disengage()
            self.game.yellow_double.disengage()
            self.game.green_double.disengage()
            if self.game.square_a.position != 0:
                self.magic_squarea_reset(self.game.square_a.position)
            if self.game.square_b.position != 0:
                self.magic_squareb_reset(self.game.square_b.position)
            if self.game.square_c.position != 0:
                self.magic_squarec_reset(self.game.square_c.position)
            if self.game.square_d.position != 0:
                self.magic_squared_reset(self.game.square_d.position)
            self.game.ball_count.reset()
            self.game.extra_ball.reset()
            self.game.odds1.reset()
            self.game.odds2.reset()
            self.game.before_fourth.engage(self.game)
            self.game.timer.reset()
            self.game.sound.play_music('motor', -1)
            self.regular_play()
        self.delay(name="display", delay=0.1, handler=graphics.double_header.display, param=self)
        self.game.tilt.disengage()

    def magic_squarea_reset(self, number):
        if number != 0:
            self.game.square_a.step()
            self.delay(name="display", delay=0, handler=graphics.double_header.display, param=self)
            number = self.game.square_a.position
            self.delay(name="magic_squarea_reset", delay=0.1, handler=self.magic_squarea_reset, param=number)

    def magic_squareb_reset(self, number):
        if number != 0:
            self.game.square_b.step()
            self.delay(name="display", delay=0, handler=graphics.double_header.display, param=self)
            number = self.game.square_b.position
            self.delay(name="magic_squareb_reset", delay=0.1, handler=self.magic_squareb_reset, param=number)

    def magic_squarec_reset(self, number):
        if number != 0:
            self.game.square_c.step()
            self.delay(name="display", delay=0, handler=graphics.double_header.display, param=self)
            number = self.game.square_c.position
            self.delay(name="magic_squarec_reset", delay=0.1, handler=self.magic_squarec_reset, param=number)

    def magic_squared_reset(self, number):
        if number != 0:
            self.game.square_d.step()
            self.delay(name="display", delay=0, handler=graphics.double_header.display, param=self)
            number = self.game.square_d.position
            self.delay(name="magic_squared_reset", delay=0.1, handler=self.magic_squared_reset, param=number)

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
        if self.game.ball_count.position >= 5:
            if self.game.search_index.status == False:
                self.search()
        self.delay(name="display", delay=0.1, handler=graphics.double_header.display, param=self)


    # This is really nasty, but it is how we render graphics for each individual hole.
    # numbers are added (or removed from) a list.  In this way, I can re-use the same
    # routine even for games where there are ball return functions like Surf Club.

    def sw_hole1_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(1)
            self.holes2.append(1)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.double_header.display, param=self)

    def sw_hole2_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(2)
            self.holes2.append(2)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.double_header.display, param=self)

    def sw_hole3_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(3)
            self.holes2.append(3)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.double_header.display, param=self)

    def sw_hole4_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(4)
            self.holes2.append(4)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.double_header.display, param=self)

    def sw_hole5_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(5)
            self.holes2.append(5)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.double_header.display, param=self)

    def sw_hole6_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(6)
            self.holes2.append(6)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.double_header.display, param=self)

    def sw_hole7_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(7)
            self.holes2.append(7)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.double_header.display, param=self)

    def sw_hole8_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(8)
            self.holes2.append(8)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.double_header.display, param=self)

    def sw_hole9_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(9)
            self.holes2.append(9)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.double_header.display, param=self)

    def sw_hole10_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(10)
            self.holes2.append(10)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.double_header.display, param=self)

    def sw_hole11_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(11)
            self.holes2.append(11)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.double_header.display, param=self)

    def sw_hole12_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(12)
            self.holes2.append(12)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.double_header.display, param=self)

    def sw_hole13_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(13)
            self.holes2.append(13)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.double_header.display, param=self)

    def sw_hole14_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(14)
            self.holes2.append(14)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.double_header.display, param=self)

    def sw_hole15_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(15)
            self.holes2.append(15)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.double_header.display, param=self)

    def sw_hole16_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(16)
            self.holes2.append(16)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.double_header.display, param=self)

    def sw_hole17_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(17)
            self.holes2.append(17)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.double_header.display, param=self)

    def sw_hole18_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(18)
            self.holes2.append(18)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.double_header.display, param=self)

    def sw_hole19_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(19)
            self.holes2.append(19)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.double_header.display, param=self)

    def sw_hole20_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(20)
            self.holes2.append(20)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.double_header.display, param=self)

    def sw_hole21_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(21)
            self.holes2.append(21)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.double_header.display, param=self)

    def sw_hole22_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(22)
            self.holes2.append(22)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.double_header.display, param=self)

    def sw_hole23_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(23)
            self.holes2.append(23)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.double_header.display, param=self)

    def sw_hole24_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(24)
            self.holes2.append(24)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.double_header.display, param=self)

    def sw_hole25_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(25)
            self.holes2.append(25)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.double_header.display, param=self)

    def sw_replayReset_active(self, sw):
        self.game.anti_cheat.disengage()
        self.holes = []
        self.holes2 = []
#        self.cancel_delayed(name="blink_title")
        graphics.double_header.display(self)
        self.tilt_actions()
#        self.delay(name="blink_title", delay=1, handler=self.blink_title)
        self.replay_step_down(self.game.replays)

    def tilt_actions(self):
        self.game.start.disengage()
        self.cancel_delayed(name="replay_reset")
        self.cancel_delayed(name="card1_replay_step_up")
        self.cancel_delayed(name="corners_replay_step_up")
        self.game.card1_replay_counter.reset()
        self.game.card2_replay_counter.reset()
        self.game.corners_replay_counter.reset()
        self.game.corners.disengage()
        self.game.spot_12.disengage()
        self.game.spot_13.disengage()
        self.game.red_double.disengage()
        self.game.yellow_double.disengage()
        self.game.green_double.disengage()
        self.game.selection_feature.reset()
        self.game.start.engage(self.game)
        self.game.selector.reset()
        self.game.ball_count.reset()
        self.game.extra_ball.reset()
        self.game.odds1.reset()
        self.game.odds2.reset()
        self.game.eb_play.disengage()
        self.game.search_index.disengage()
        self.game.magic_squares_feature.reset()
        self.game.red_line.reset()
        self.game.yellow_line.reset()
        self.game.before_fourth.disengage()
        if self.game.ball_count.position == 0:
            if self.game.switches.shutter.is_active():
                self.game.coils.shutter.enable()
        self.holes = []
        self.holes2 = []
        self.game.anti_cheat.engage(game)
        self.game.tilt.engage(self.game)
        self.game.sound.stop_music()
        self.game.sound.play('tilt')
        # displays "Tilt" on the backglass, you have to recoin.
        self.delay(name="display", delay=0.1, handler=graphics.double_header.display, param=self)

    def sw_tilt_active(self, sw):
        if self.game.tilt.status == False:
            self.tilt_actions()

    def replay_step_down(self, number=0):
        if number > 0:
            if number > 1:
                self.game.replays -= 1
                graphics.replay_step_down(self.game.replays, graphics.double_header.reel1, graphics.double_header.reel10, graphics.double_header.reel100)
                self.game.coils.registerDown.pulse()
                number -= 1
                graphics.double_header.display(self)
                self.delay(name="replay_reset", delay=0.0, handler=self.replay_step_down, param=number)
            elif number == 1:
                self.game.replays -= 1
                graphics.replay_step_down(self.game.replays, graphics.double_header.reel1, graphics.double_header.reel10, graphics.double_header.reel100)
                self.game.coils.registerDown.pulse()
                number -= 1
                graphics.double_header.display(self)
                self.cancel_delayed(name="replay_reset")
        else: 
            if self.game.replays > 0:
                self.game.replays -= 1
                graphics.replay_step_down(self.game.replays, graphics.double_header.reel1, graphics.double_header.reel10, graphics.double_header.reel100)
                self.delay(name="display", delay=0.1, handler=graphics.double_header.display, param=self)
            self.game.coils.registerDown.pulse()

    def replay_step_up(self):
        if self.game.replays < 899:
            self.game.replays += 1
            graphics.replay_step_up(self.game.replays, graphics.double_header.reel1, graphics.double_header.reel10, graphics.double_header.reel100)
        self.game.coils.registerUp.pulse()
        self.game.reflex.increase()
        graphics.double_header.display(self)

    def check_spotted(self, p):
        if p == 0:
            if self.game.selection_feature.position >= 5:
                if self.game.switches.hole5.is_inactive():
                    if 5 in self.holes:
                        self.holes.remove(5)
                if self.game.switches.hole15.is_inactive():
                    if 15 in self.holes:
                        self.holes.remove(15)
                if self.game.switches.hole2.is_inactive():
                    if 2 in self.holes:
                        self.holes.remove(2)
                if self.game.switches.hole14.is_inactive():
                    if 14 in self.holes:
                        self.holes.remove(14)
                if self.game.switches.hole12.is_inactive():
                    if 12 not in self.holes:
                        self.holes.append(12)
            else:
                if self.game.switches.hole5.is_inactive():
                    if 5 in self.holes:
                        self.holes.remove(5)
                if self.game.switches.hole15.is_inactive():
                    if 15 in self.holes:
                        self.holes.remove(15)
                if self.game.switches.hole2.is_inactive():
                    if 2 in self.holes:
                        self.holes.remove(2)
                if self.game.switches.hole14.is_inactive():
                    if 14 in self.holes:
                        self.holes.remove(14)
                if self.game.switches.hole12.is_inactive():
                    if 12 in self.holes:
                        self.holes.remove(12)
        elif p == 1:
            if self.game.selection_feature.position >= 6:
                if self.game.switches.hole5.is_inactive():
                    if 5 in self.holes:
                        self.holes.remove(5)
                if self.game.switches.hole15.is_inactive():
                    if 15 in self.holes:
                        self.holes.remove(15)
                if self.game.switches.hole2.is_inactive():
                    if 2 in self.holes:
                        self.holes.remove(2)
                if self.game.switches.hole14.is_inactive():
                    if 14 not in self.holes:
                        self.holes.append(14)
                if self.game.switches.hole12.is_inactive():
                    if 12 in self.holes:
                        self.holes.remove(12)
            else:
                if self.game.switches.hole5.is_inactive():
                    if 5 in self.holes:
                        self.holes.remove(5)
                if self.game.switches.hole15.is_inactive():
                    if 15 in self.holes:
                        self.holes.remove(15)
                if self.game.switches.hole2.is_inactive():
                    if 2 in self.holes:
                        self.holes.remove(2)
                if self.game.switches.hole14.is_inactive():
                    if 14 in self.holes:
                        self.holes.remove(14)
                if self.game.switches.hole12.is_inactive():
                    if 12 in self.holes:
                        self.holes.remove(12)

        elif p == 2:
            if self.game.selection_feature.position >= 7:
                if self.game.switches.hole5.is_inactive():
                    if 5 in self.holes:
                        self.holes.remove(5)
                if self.game.switches.hole15.is_inactive():
                    if 15 in self.holes:
                        self.holes.remove(15)
                if self.game.switches.hole2.is_inactive():
                    if 2 not in self.holes:
                        self.holes.append(2)
                if self.game.switches.hole14.is_inactive():
                    if 14 in self.holes:
                        self.holes.remove(14)
                if self.game.switches.hole12.is_inactive():
                    if 12 in self.holes:
                        self.holes.remove(12)
            else:
                if self.game.switches.hole5.is_inactive():
                    if 5 in self.holes:
                        self.holes.remove(5)
                if self.game.switches.hole15.is_inactive():
                    if 15 in self.holes:
                        self.holes.remove(15)
                if self.game.switches.hole2.is_inactive():
                    if 2 in self.holes:
                        self.holes.remove(2)
                if self.game.switches.hole14.is_inactive():
                    if 14 in self.holes:
                        self.holes.remove(14)
                if self.game.switches.hole12.is_inactive():
                    if 12 in self.holes:
                        self.holes.remove(12)

        elif p == 3:
            if self.game.selection_feature.position >= 8:
                if self.game.switches.hole5.is_inactive():
                    if 5 not in self.holes:
                        self.holes.append(5)
                if self.game.switches.hole15.is_inactive():
                    if 15 in self.holes:
                        self.holes.remove(15)
                if self.game.switches.hole2.is_inactive():
                    if 2 in self.holes:
                        self.holes.remove(2)
                if self.game.switches.hole14.is_inactive():
                    if 14 in self.holes:
                        self.holes.remove(14)
                if self.game.switches.hole12.is_inactive():
                    if 12 in self.holes:
                        self.holes.remove(12)
            else:
                if self.game.switches.hole5.is_inactive():
                    if 5 in self.holes:
                        self.holes.remove(5)
                if self.game.switches.hole15.is_inactive():
                    if 15 in self.holes:
                        self.holes.remove(15)
                if self.game.switches.hole2.is_inactive():
                    if 2 in self.holes:
                        self.holes.remove(2)
                if self.game.switches.hole14.is_inactive():
                    if 14 in self.holes:
                        self.holes.remove(14)
                if self.game.switches.hole12.is_inactive():
                    if 12 in self.holes:
                        self.holes.remove(12)

        else:
            if self.game.selection_feature.position >= 9:
                if self.game.switches.hole5.is_inactive():
                    if 5 in self.holes:
                        self.holes.remove(5)
                if self.game.switches.hole15.is_inactive():
                    if 15 not in self.holes:
                        self.holes.append(15)
                if self.game.switches.hole2.is_inactive():
                    if 2 in self.holes:
                        self.holes.remove(2)
                if self.game.switches.hole14.is_inactive():
                    if 14 in self.holes:
                        self.holes.remove(14)
                if self.game.switches.hole12.is_inactive():
                    if 12 in self.holes:
                        self.holes.remove(12)
            else:
                if self.game.switches.hole5.is_inactive():
                    if 5 in self.holes:
                        self.holes.remove(5)
                if self.game.switches.hole15.is_inactive():
                    if 15 in self.holes:
                        self.holes.remove(15)
                if self.game.switches.hole2.is_inactive():
                    if 2 in self.holes:
                        self.holes.remove(2)
                if self.game.switches.hole14.is_inactive():
                    if 14 in self.holes:
                        self.holes.remove(14)
                if self.game.switches.hole12.is_inactive():
                    if 12 in self.holes:
                        self.holes.remove(12)


        self.delay(name="display", delay=0.1, handler=graphics.double_header.display, param=self)


    def sw_yellow_active(self, sw):
        if self.game.selection_feature.position >= 5:
            if self.game.ball_count.position < 4:
                self.game.spotted.step()
                self.check_spotted(self.game.spotted.position)
        if self.game.ball_count.position >= 5:
            if self.game.eb_play.status == False:
                self.game.spotting.spin()
                self.game.mixer1.spin()
                self.game.mixer2.spin()
                self.game.mixer3.spin()
                self.game.mixer4.spin()
                self.game.eb_play.engage(self.game)
                self.delay(name="display", delay=0.1, handler=graphics.double_header.display, param=self)
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
                self.delay(name="display", delay=0.1, handler=graphics.double_header.display, param=self)
            
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
       
        if self.game.odds1.position > 0:
            for i in range(0, 50):
                self.r = self.closed_search_relays(self.game.searchdisc.position)
                self.game.searchdisc.spin()
                self.wipers = self.r[0]
                self.card = self.r[1]
                self.corners = self.r[2]
                self.yellow = self.r[3]
                self.red = self.r[4]
                self.green = self.r[5]

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
                                    self.find_winner(s, self.card, self.corners, self.yellow, self.red, self.green)
                                    break
        if self.game.odds2.position > 0:
            for i in range(0, 50):
                self.r = self.closed_search_relays_game2(self.game.searchdisc.position)
                self.game.searchdisc.spin()
                self.wipers = self.r[0]
                self.card = self.r[1]

                # From here, I need to determine based on the value of r, whether to latch the search index and score. 
                # I need to determine the best winner on each card.  To do this, I must compare the position of the replay counter before
                # determining the winner. Reminder that my replay counters are a 1:1 representation.

                self.match = []
                for key in self.wipers:
                    for number in self.holes2:
                        if number == key:
                            self.match.append(self.wipers[key])
                            relays = sorted(set(self.match))
                            #TODO Play sound for each relay closure.
                            s = functions.count_seq(relays)
                            if self.game.selector.position >= 1:
                                if s >= 3:
                                    self.find_winner(s, self.card)
                                    break

#        self.delay(name="blink_title", delay=3, handler=self.blink_title)

    def find_winner(self, relays, card, corners=0, yellow=0, red=0, green=0):
        if self.game.search_index.status == False and self.game.replays < 899:
            if card == 1:
                if self.game.odds1.position == 1:
                    threeodds = 4
                    fourodds = 16
                    fiveodds = 64
                elif self.game.odds1.position == 2:
                    threeodds = 6
                    fourodds = 18
                    fiveodds = 72
                elif self.game.odds1.position == 3:
                    threeodds = 8
                    fourodds = 24
                    fiveodds = 96
                elif self.game.odds1.position == 4:
                    threeodds = 16
                    fourodds = 48
                    fiveodds = 96
                elif self.game.odds1.position == 5:
                    threeodds = 36
                    fourodds = 96
                    fiveodds = 144
                elif self.game.odds1.position == 6:
                    threeodds = 48
                    fourodds = 144
                    fiveodds = 192
            elif card == 2:
                if self.game.odds2.position == 1:
                    threeodds = 4
                    fourodds = 16
                    fiveodds = 64
                elif self.game.odds2.position == 2:
                    threeodds = 6
                    fourodds = 18
                    fiveodds = 72
                elif self.game.odds2.position == 3:
                    threeodds = 8
                    fourodds = 24
                    fiveodds = 96
                elif self.game.odds2.position == 4:
                    threeodds = 16
                    fourodds = 48
                    fiveodds = 96
                elif self.game.odds2.position == 5:
                    threeodds = 36
                    fourodds = 96
                    fiveodds = 192

            if relays == 3:
                if card == 1:
                    if not corners:
                        if (red == True and self.game.red_double.status == True) or (yellow == True and self.game.yellow_double.status == True) or (green == True and self.game.green_double.status == True):
                            if self.game.card1_replay_counter.position < threeodds * 2:
                                self.game.search_index.engage(self.game)
                                self.card1_replay_step_up(threeodds * 2 - self.game.card1_replay_counter.position)
                        else:
                            if self.game.card1_replay_counter.position < threeodds:
                                self.game.search_index.engage(self.game)
                                self.card1_replay_step_up(threeodds - self.game.card1_replay_counter.position)
                elif card == 2:
                    if self.game.card2_replay_counter.position < threeodds:
                        self.game.search_index.engage(self.game)
                        self.card2_replay_step_up(threeodds - self.game.card2_replay_counter.position)
            if relays == 4:
                if card == 1:
                    if corners and self.game.corners.status == True:
                        if self.game.corners.status == True:
                            if self.game.corners_replay_counter.position < 300:
                                self.game.search_index.engage(self.game)
                                self.corners_replay_step_up(300 - self.game.corners_replay_counter.position)
                    else:
                        if not corners:
                            if (red == True and self.game.red_double.status == True) or (yellow == True and self.game.yellow_double.status == True) or (green == True and self.game.green_double.status == True):
                                if self.game.card1_replay_counter.position < fourodds * 2:
                                    self.game.search_index.engage(self.game)
                                    self.card1_replay_step_up(fourodds * 2 - self.game.card1_replay_counter.position)
                            else:
                                if self.game.card1_replay_counter.position < fourodds:
                                    self.game.search_index.engage(self.game)
                                    self.card1_replay_step_up(fourodds - self.game.card1_replay_counter.position)
                elif card == 2:
                    if self.game.card2_replay_counter.position < fourodds:
                        self.game.search_index.engage(self.game)
                        self.card2_replay_step_up(fourodds - self.game.card2_replay_counter.position)
            if relays == 5:
                if card == 1:
                    if (red == True and self.game.red_double.status == True) or (yellow == True and self.game.yellow_double.status == True) or (green == True and self.game.green_double.status == True):
                        if self.game.card1_replay_counter.position < fiveodds * 2:
                            self.game.search_index.engage(self.game)
                            self.card1_replay_step_up(fiveodds * 2 - self.game.card1_replay_counter.position)
                    else:
                        if self.game.card1_replay_counter.position < fiveodds:
                            self.game.search_index.engage(self.game)
                            self.card1_replay_step_up(fiveodds - self.game.card1_replay_counter.position)
                elif card == 2:
                    if self.game.card2_replay_counter.position < fiveodds:
                        self.game.search_index.engage(self.game)
                        self.card2_replay_step_up(fiveodds - self.game.card2_replay_counter.position)

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

    def closed_search_relays(self, rivets):
        # This function is critical, as it will determine which card is returned, etc.  I need to check the position of the
        # replay counter for the card. We will get a row back
        # that has the numbers on the position which will return the search relay connected.  When three out of the five relays
        # are connected, we get a winner!
       
        self.pos = {}
        self.pos[0] = {}
        self.pos[1] = {9:1, 24:2, 5:3, 4:4, 8:5}
        self.pos[2] = {11:1, 19:2, 1:3, 20:4, 25:5}
        self.pos[3] = {2:1, 18:2, 15:3, 12:4, 17:5}
        self.pos[4] = {13:1, 22:2, 14:3, 21:4, 6:5}
        self.pos[5] = {10:1, 7:2, 16:3, 23:3, 3:5}
        self.pos[6] = {9:1, 11:2, 2:3, 13:4, 10:5}
        self.pos[7] = {24:1, 19:2, 18:3, 22:4, 7:5}
        self.pos[8] = {5:1, 1:2, 15:3, 14:4, 16:5}
        self.pos[9] = {4:1, 20:2, 12:3, 21:4, 23:5}
        self.pos[10] = {8:1, 25:2, 17:3, 6:4, 3:5}
        self.pos[11] = {9:1, 19:2, 15:3, 21:4, 3:5}
        self.pos[12] = {8:1, 20:2, 15:3, 22:4, 10:5}
        self.pos[13] = {}
        self.pos[14] = {9:1, 8:2, 10:3, 3:4}
        self.pos[15] = {}
        self.pos[16] = {}
        self.pos[17] = {}
        self.pos[18] = {}
        self.pos[19] = {}
        self.pos[20] = {}
        self.pos[21] = {}
        self.pos[22] = {}
        self.pos[23] = {}
        self.pos[24] = {}
        self.pos[25] = {}
        self.pos[26] = {}
        self.pos[27] = {}
        self.pos[28] = {}
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

        card = 1
        red = False
        yellow = False
        green = False
        corners = False

        if rivets == 1 or rivets == 7 or rivets == 4 or rivets == 10:
            red = True
        if rivets == 2 or rivets == 5 or rivets == 6 or rivets == 9:
            yellow = True
        if rivets == 11 or rivets == 12:
            green = True

        if rivets == 14:
            corners = True

        return (self.pos[rivets], card, corners, yellow, red, green)

    def closed_search_relays_game2(self, rivets):
        # This function is critical, as it will determine which card is returned, etc.  I need to check the position of the
        # replay counter for the card. We will get a row back
        # that has the numbers on the position which will return the search relay connected.  When three out of the five relays
        # are connected, we get a winner!
       
        if self.game.square_a.position == 0:
            self.p1 = 9
            self.p2 = 4
            self.q1 = 1
            self.q2 = 19
        elif self.game.square_a.position == 1:
            self.p1 = 1
            self.p2 = 9
            self.q1 = 19
            self.q2 = 4
        elif self.game.square_a.position == 2:
            self.p1 = 19
            self.p2 = 1
            self.q1 = 4
            self.q2 = 9
        else:
            self.p1 = 4
            self.p2 = 19
            self.q1 = 9
            self.q2 = 1

        if self.game.square_b.position == 0:
            self.s1 = 10
            self.s2 = 22
            self.t1 = 15
            self.t2 = 23
        elif self.game.square_b.position == 1:
            self.s1 = 15
            self.s2 = 10
            self.t1 = 23
            self.t2 = 22
        elif self.game.square_b.position == 2:
            self.s1 = 23
            self.s2 = 15
            self.t1 = 22
            self.t2 = 10
        else:
            self.s1 = 22
            self.s2 = 23
            self.t1 = 10
            self.t2 = 15

        if self.game.square_c.position == 0:
            self.p4 = 14
            self.p5 = 6
            self.q4 = 20
            self.q5 = 8
        elif self.game.square_c.position == 1:
            self.p4 = 20
            self.p5 = 14
            self.q4 = 8
            self.q5 = 6
        elif self.game.square_c.position == 2:
            self.p4 = 8
            self.p5 = 20
            self.q4 = 6
            self.q5 = 14
        else:
            self.p4 = 6
            self.p5 = 8
            self.q4 = 14
            self.q5 = 20

        if self.game.square_d.position == 0:
            self.s4 = 21
            self.s5 = 3
            self.t4 = 7
            self.t5 = 17
        elif self.game.square_d.position == 1:
            self.s4 = 7
            self.s5 = 21
            self.t4 = 17
            self.t5 = 3
        elif self.game.square_d.position == 2:
            self.s4 = 17
            self.s5 = 7
            self.t4 = 3
            self.t5 = 21
        else:
            self.s4 = 3
            self.s5 = 17
            self.t4 = 21
            self.t5 = 7

        self.pos = {}
        self.pos[0] = {}
        self.pos[1] = {self.p1:1, self.p2:2, 25:3, self.p4:4, self.p5:5}
        self.pos[2] = {self.q1:1, self.q2:2, 24:3, self.q4:4, self.q5:5}
        self.pos[3] = {2:1, 18:2, 16:3, 12:4, 11:5}
        self.pos[4] = {self.s1:1, self.s2:2, 13:3, self.s4:4, self.s5:5}
        self.pos[5] = {self.t1:1, self.t2:2, 5:3, self.t4:4, self.t5:5}
        self.pos[6] = {self.p1:1, self.q1:2, 2:3, self.s1:4, self.t1:5}
        self.pos[7] = {self.p2:1, self.q2:2, 18:3, self.s2:4, self.t2:5}
        self.pos[8] = {25:1, 24:2, 16:3, 13:4, 5:5}
        self.pos[9] = {self.p4:1, self.q4:2, 12:3, self.s4:4, self.t4:5}
        self.pos[10] = {self.p5:1, self.q5:2, 11:3, self.s5:4, self.t5:5}
        self.pos[11] = {self.p1:1, self.q2:2, 16:3, self.s4:4, self.t5:5}
        self.pos[12] = {self.p5:1, self.q4:2, 16:3, self.s2:4, self.t1:5}
        self.pos[13] = {}
        self.pos[14] = {}
        self.pos[15] = {}
        self.pos[16] = {}
        self.pos[17] = {}
        self.pos[18] = {}
        self.pos[19] = {}
        self.pos[20] = {}
        self.pos[21] = {}
        self.pos[22] = {}
        self.pos[23] = {}
        self.pos[24] = {}
        self.pos[25] = {}
        self.pos[26] = {}
        self.pos[27] = {}
        self.pos[28] = {}
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

        card = 2

        return (self.pos[rivets], card)
    
    def scan_all(self):
        #Animate scanning of everything - this happens through the spotting disc
        self.all_probability()

    def all_probability(self):
        if self.game.game1.status == True:
            if self.game.odds1.position < 3:
                self.game.odds1.step()
        if self.game.game2.status == True:
            if self.game.odds2.position < 3:
                self.game.odds2.step()
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
        if self.game.game1.status == True:
            if self.game.odds1.position < 3:
                return
            s = random.randint(1,5)
            self.animate_odds_scan(s)
            p = self.odds1_probability()
            if p == 1:
                es = self.check_extra_step()
                if es == 1:
                    i = random.randint(1,5)
                    self.game1_extra_step(i)
                else:
                    self.game.odds1.step()
        else:
            if self.game.odds2.position < 3:
                return
            s = random.randint(1,5)
            self.animate_odds_scan(s)
            p = self.odds2_probability()
            if p == 1:
                es = self.check_extra_step()
                if es == 1:
                    i = random.randint(1,5)
                    self.game2_extra_step(i)
                else:
                    self.game.odds2.step()

    def game1_extra_step(self, number):
        if number > 0:
            self.game.odds1.step()
            self.delay(name="display", delay=0, handler=graphics.double_header.display, param=self)
            number -= 1
            self.delay(name="game1_extra_step", delay=0.1, handler=self.game1_extra_step, param=number)

    def game2_extra_step(self, number):
        if number > 0:
            self.game.odds2.step()
            self.delay(name="display", delay=0, handler=graphics.double_header.display, param=self)
            number -= 1
            self.delay(name="game2_extra_step", delay=0.1, handler=self.game2_extra_step, param=number)

    def check_extra_step(self):
        i = random.randint(0,32)
        if i == 16:
            return 1
        else:
            return 0

    def odds1_probability(self):
        # Check position of Mixer 2, extra scoring relays and current 
        # position of the odds, along with trip relays.
        # For first check, guaranteed single stepup.  Probability doesn't 
        # factor, so I will return as part of the initial check above.
        if self.game.game1.status == True:
            if self.game.odds1.position == 1:
                return 1
            else:
                if self.game.odds1.position == 2:
                    return 1
                sd = self.game.spotting.position
                if sd == 1 or sd == 6 or sd == 40:
                    self.game1_extra_step(3 - self.game.odds1.position)
                elif sd == 21 or sd == 42:
                    self.game1_extra_step(4 - self.game.odds1.position)
                elif sd == 15:
                    if self.game.cu:
                        self.game1_extra_step(6 - self.game.odds1.position)
                    else:
                        self.game1_extra_step(5 - self.game.odds1.position)
                if self.game.odds1.position == 3:
                    if sd == 1 or sd == 3 or sd == 5 or sd == 6 or sd == 9 or sd == 11 or sd == 16 or sd == 22 or sd == 28 or sd == 29 or sd == 36 or sd == 37 or sd == 40 or sd == 44 or sd == 47 or sd == 49:
                        return 1
                if self.game.odds1.position == 4:
                    if sd == 3 or sd == 9 or sd == 11 or sd == 22 or sd == 28 or sd == 29 or sd == 36 or sd == 37:
                        return 1
                if self.game.odds1.position == 5:
                    if sd == 1 or sd == 3 or sd == 5 or sd == 6 or sd == 9 or sd == 11 or sd == 14 or sd == 16 or sd == 21 or sd == 22 or sd == 28 or sd == 29 or sd == 33 or sd == 36 or sd == 37 or sd == 40 or sd == 43 or sd == 44 or sd == 47 or sd == 49:
                        return 1
                else:
                    return 0

    def odds2_probability(self):
        # Check position of Mixer 2, extra scoring relays and current 
        # position of the odds, along with trip relays.
        # For first check, guaranteed single stepup.  Probability doesn't 
        # factor, so I will return as part of the initial check above.
        if self.game.game2.status == True:
            if self.game.odds2.position == 1:
                return 1
            else:
                sd = self.game.spotting.position
                if self.game.odds2.position == 2:
                    if sd == 1 or sd == 3 or sd == 5 or sd == 6 or sd == 9 or sd == 11 or sd == 14 or sd == 16 or sd == 21 or sd == 22 or sd == 28 or sd == 29 or sd == 33 or sd == 36 or sd == 37 or sd == 40 or sd == 43 or sd == 44 or sd == 47 or sd == 49:
                        return 1
                elif self.game.odds2.position == 3:
                    if sd == 3 or sd == 9 or sd == 11 or sd == 22 or sd == 28 or sd == 29 or sd == 36 or sd == 37:
                        return 1
                elif self.game.odds2.position == 4:
                    return 1
                if sd == 33:
                    if self.game.cu:
                        self.game2_extra_step(4 - self.game.odds2.position)
                else:
                    return 0

    def scan_features(self):
        p = self.features_probability()

    def features_probability(self):
        s = random.randint(1,6)
        self.animate_feature_scan(s)

        m4 = self.check_mixer4()
        if m4 == True:
            self.features_spotting()

    def check_mixer4(self):
        mix4 = self.game.mixer4.position
        o1 = self.game.odds1.position
        o2 = self.game.odds2.position

        if self.game.game1.status == True:
            if o1 == 1 or o1 == 2:
                if mix4 == 2 or mix4 == 3 or mix4 == 7 or mix4 == 11 or mix4 == 12 or mix4 == 13 or mix4 == 14 or mix4 == 15 or mix4 == 18 or mix4 == 19 or mix4 == 23:
                    return 1
            elif o1 == 3 or o1 == 4:
                if mix4 == 1 or mix4 in range(3,6) or mix4 == 8 or mix4 == 10 or mix4 in range(13,16) or mix4 == 17 or mix4 == 19 or mix4 == 21 or mix4 == 22:
                    return 1
            elif o1 == 5:
                if mix4 == 6 or mix4 == 15 or mix4 == 23:
                    return 1
            else:
                return 1
        else:
            if o2 == 1:
                if mix4 == 2 or mix4 == 7 or mix4 == 11 or mix4 == 13 or mix4 == 17:
                    return 1
            if o2 <= 2:
                if mix4 == 0 or mix4 == 1 or mix4 in range(3,7) or mix4 in range(8,11) or mix4 == 12 or mix4 in range(14,17) or mix4 in range(18,24):
                    return 1
            if o2 >= 3:
                return 1

    def features_spotting(self):
        sd = self.game.spotting.position
        m2 = self.game.mixer2.position
        sf = self.game.selection_feature.position

        if self.game.game2.status == True:
            if sd == 8 or sd == 19 or sd == 23:
                if m2 != 2 and m2 != 5 and m2 != 7 and m2 != 9 and m2 != 10 and m2 != 15 and m2 != 18 and m2 != 23:
                    self.step_ms(3 - self.game.magic_squares_feature.position)
                if m2 == 2 or m2 == 5 or m2 == 7 or m2 == 9 or m2 == 10 or m2 == 15 or m2 == 18 or m2 == 23:
                    self.step_ms(5 - self.game.magic_squares_feature.position)
            if sd == 0 or sd == 10 or sd == 12 or sd == 18 or sd == 20 or sd == 25 or sd == 27 or sd == 30 or sd == 32 or sd == 34 or sd == 38 or sd == 39 or sd == 42 or sd == 45 or sd == 46 or sd == 48:
                self.step_ms(1)
            if sd == 11 or sd == 17 or sd == 33 or sd == 47:
                self.step_ms(1)
            if sd == 2 or sd == 4 or sd == 7 or sd == 24 or sd == 31:
                self.game.spot_12.engage(self.game)
                self.holes2.append(12)
            if sd == 13 or sd == 15 or sd == 26 or sd == 35 or sd == 41:
                self.game.spot_13.engage(self.game)
                self.holes2.append(13)
        else:
            if sf == 0:
                self.step_selection_feature(1)
                self.check_spotted(self.game.spotted.position)
            elif sf == 1:
                self.step_selection_feature(1)
                self.check_spotted(self.game.spotted.position)
            elif sd == 2:
                self.step_selection_feature(1)
                self.check_spotted(self.game.spotted.position)
            elif sd == 3:
                self.step_selection_feature(3)
                self.check_spotted(self.game.spotted.position)
            elif sd == 6:
                if sd == 13 or sd == 23 or sd == 34 or sd == 35 or sd == 39 or sd == 41:
                    self.step_selection_feature(1)
                    self.check_spotted(self.game.spotted.position)
            elif sd == 7:
                if sd == 15 or sd == 18 or sd == 20 or sd == 25 or sd == 26 or sd == 32 or sd == 46 or sd == 0:
                    self.step_selection_feature(1)
                    self.check_spotted(self.game.spotted.position)
            elif sd == 8:
                if sd == 1 or sd == 3 or sd == 5 or sd == 9 or sd == 16 or sd == 22 or sd == 28 or sd == 29 or sd == 36 or sd == 37:
                    self.game.selection_feature.step()
                    self.check_spotted(self.game.spotted.position)
            elif sd == 2 or sd == 10 or sd == 30:
                self.step_selection_feature(9)
            if sd == 11 or sd == 17:
                self.game.corners.engage(self.game)
            if sd == 4 or sd == 8 or sd == 14 or sd == 24 or sd == 31 or sd == 47:
                self.game.red_double.engage(self.game)
            if sd == 7 or sd == 12 or sd == 19 or sd == 38 or sd == 45 or sd == 49:
                self.game.yellow_double.engage(self.game)
            if sd == 27 or sd == 42 or sd == 48:
                self.game.green_double.engage(self.game)

    def step_ms(self, number):
        if number >= 1:
            self.game.magic_squares_feature.step()
            if self.game.magic_squares_feature.position == 3:
                self.holes2.append(2)
            if self.game.magic_squares_feature.position == 5:
                self.holes2.append(24)
            number -= 1
            self.delay(name="display", delay=0.1, handler=graphics.double_header.display, param=self)
            self.delay(name="step_ms", delay=0.1, handler=self.step_ms, param=number)

    def step_selection_feature(self, number):
        if number >= 1:
            self.game.selection_feature.step()
            self.check_spotted(self.game.spotted.position)
            number -= 1
            if self.game.selection_feature.position == 5:
                if number == 0:
                    number += 1
            self.delay(name="display", delay=0.1, handler=graphics.double_header.display, param=self)
            self.delay(name="step_selection_feature", delay=0.1, handler=self.step_selection_feature, param=number)

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
        self.delay(name="display", delay=0.1, handler=graphics.double_header.display, param=self)

    def animate_odds_scan(self, s):
        if self.game.game1.status == True:
            if s > 1:
                self.delay(name="odds_animation", delay=0, handler=graphics.double_header.odds_animation, param=s)
                self.delay(name="display", delay=0.1, handler=graphics.double_header.display, param=self)
                s -= 1
                #self.delay(name="animate_odds", delay=0.1, handler=self.animate_odds_scan, param=s)
            else:
                self.delay(name="display", delay=0.1, handler=graphics.double_header.display, param=self)
        else:
            if s > 1:
                self.delay(name="odds_animation", delay=0, handler=graphics.double_header.odds_animation2, param=s)
                self.delay(name="display", delay=0.1, handler=graphics.double_header.display, param=self)
                s -= 1
                #self.delay(name="animate_odds", delay=0.1, handler=self.animate_odds_scan, param=s)
            else:
                self.delay(name="display", delay=0.1, handler=graphics.double_header.display, param=self)


    def animate_feature_scan(self, s):
        if self.game.game1.status == True:
            if s > 1:
                self.delay(name="feature_animation", delay=0.1, handler=graphics.double_header.feature_animation, param=s)
                self.delay(name="display", delay=0.1, handler=graphics.double_header.display, param=self)
                s -= 1
                #self.delay(name="animate_feature", delay=0.1, handler=self.animate_feature_scan, param=s)
            else:
                self.delay(name="display", delay=0.1, handler=graphics.double_header.display, param=self)
        else:
            if s > 1:
                self.delay(name="feature_animation", delay=0.1, handler=graphics.double_header.feature_animation2, param=s)
                self.delay(name="display", delay=0.1, handler=graphics.double_header.display, param=self)
                s -= 1
                #self.delay(name="animate_feature", delay=0.1, handler=self.animate_feature_scan, param=s)
            else:
                self.delay(name="display", delay=0.1, handler=graphics.double_header.display, param=self)


    def animate_eb_scan(self, s):
        if s > 1:
            self.delay(name="eb_animation", delay=0.1, handler=graphics.double_header.eb_animation, param=s)
            self.delay(name="display", delay=0.1, handler=graphics.double_header.display, param=self)
            s -= 1
            #self.delay(name="animate_eb", delay=0.1, handler=self.animate_eb_scan, param=s)
        else:
            self.delay(name="display", delay=0.1, handler=graphics.double_header.display, param=self)

    def check_mixer3(self):
        sd = self.game.spotted.position
        m3 = self.game.mixer3.position
        if sd == 0:
            if m3 == 14:
                self.step_eb(9 - self.game.extra_ball.position)
                return 1
            else:
                return 0
        else:
            return 0

    def eb_probability(self):
        #Used Surf Club's mixers - wrong, but lacking documentation.
        mix1 = self.game.mixer1.connected_rivet()
        sd = self.game.spotted.position

        if self.game.reflex.connected_rivet() == 0 and (mix1 == 1 or mix1 == 9 or mix1 == 15):
            m3 = self.check_mixer3()
            if m3:
                return
            if sd in range(1,9) or sd in range(12,17) or sd == 19 or sd == 22 or sd == 23 or sd == 25 or sd == 27 or sd in range(29,32) or sd in range(33,46) or sd in range(47,50):
                self.game.extra_ball.step()

        elif self.game.reflex.connected_rivet() == 1 and (mix1 == 2 or mix1 == 14 or mix1 == 24 or mix1 == 1 or mix1 == 9 or mix1 == 15):
            m3 = self.check_mixer3()
            if m3:
                return
            if sd in range(1,9) or sd in range(12,17) or sd == 19 or sd == 22 or sd == 23 or sd == 25 or sd == 27 or sd in range(29,32) or sd in range(33,46) or sd in range(47,50):
                self.game.extra_ball.step()
        elif self.game.reflex.connected_rivet() == 2 and (mix1 == 6 or mix1 == 13 or mix1 == 22 or mix1 == 2 or mix1 == 14 or mix1 == 24 or mix1 == 1 or mix1 == 9 or mix1 == 15):
            m3 = self.check_mixer3()
            if m3:
                return
            if sd in range(1,9) or sd in range(12,17) or sd == 19 or sd == 22 or sd == 23 or sd == 25 or sd == 27 or sd in range(29,32) or sd in range(33,46) or sd in range(47,50):
                self.game.extra_ball.step()
        else:
            m3 = self.check_mixer3()
            if m3:
                return
            if sd in range(1,9) or sd in range(12,17) or sd == 19 or sd == 22 or sd == 23 or sd == 25 or sd == 27 or sd in range(29,32) or sd in range(33,46) or sd in range(47,50):
                self.game.extra_ball.step()

    def step_eb(self, number):
        if number >= 1:
            self.game.extra_ball.step()
            self.check_lifter_status()
            number -= 1
            self.delay(name="display", delay=0.1, handler=graphics.double_header.display, param=self)
            self.delay(name="step_eb", delay=0.1, handler=self.step_eb, param=number)

    def blink_title(self):
        title1 = random.randint(0,1)
        title2 = random.randint(0,1)
        title3 = random.randint(0,1)
        title4 = random.randint(0,1)
        if title1 == 1:
            pos = [167,257]
            image = pygame.image.load('double_header/assets/title1_on.png').convert_alpha()
            screen.blit(image, pos)
        if title2 == 1:
            pos = [241,290]
            image = pygame.image.load('double_header/assets/title2_on.png').convert_alpha()
            screen.blit(image, pos)
        if title3 == 1:
            pos = [346,298]
            image = pygame.image.load('double_header/assets/title3_on.png').convert_alpha()
            screen.blit(image, pos)
        if title4 == 1:
            pos = [431,264]
            image = pygame.image.load('double_header/assets/title4_on.png').convert_alpha()
            screen.blit(image, pos)
            
        pygame.display.update()
        self.delay(name="display", delay=0.1, handler=graphics.double_header.display, param=self)
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


class DoubleHeader(procgame.game.BasicGame):
    """ Palm Beach was the first game with Super Cards """
    def __init__(self, machine_type):
        super(DoubleHeader, self).__init__(machine_type)
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
        self.odds1 = units.Stepper("odds1", 8, 'double_header')
        self.odds2 = units.Stepper("odds2", 8, 'double_header')

        #Replay Counter
        self.card1_replay_counter = units.Stepper("card1_replay_counter", 500)
        self.card2_replay_counter = units.Stepper("card1_replay_counter", 500)
        self.corners_replay_counter = units.Stepper("card1_replay_counter", 500)

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

        self.game1 = units.Relay("game1")
        self.game2 = units.Relay("game2")

        #Tilt is separate from anti-cheat in that the trip will move the shutter
        #when the game is tilted with 1st ball in the lane.  Also prevents you
        #from picking back up by killing the anti-cheat.  Can be engaged by 
        #tilt bob, slam tilt switches, or timer at 39th step.
        #Immediately kills motors.
        self.tilt = units.Relay("tilt")

        # Select-a-spot setup
        self.spotted = units.Stepper("spotted", 4, "double_header", "continuous")

        #Need to define relays for playing for ebs
        self.eb_play = units.Relay("eb_play")

        #Relay for corners lighting
        self.corners = units.Relay("corners")

        self.selector = units.Stepper("selector", 1)

        self.yellow_line = units.Stepper("yellow_line", 10)
        self.red_line = units.Stepper("red_line", 10)

        self.square_a = units.Stepper("square_a", 3, "double_header", "continuous")
        self.square_b = units.Stepper("square_b", 3, "double_header", "continuous")
        self.square_c = units.Stepper("square_c", 3, "double_header", "continuous")
        self.square_d = units.Stepper("square_d", 3, "double_header", "continuous")

        self.magic_squares_feature = units.Stepper("magic_squares_feature", 7)
        self.selection_feature = units.Stepper("selection_feature", 9)

        self.before_fourth = units.Relay("before_fourth")

        self.red_double = units.Relay("red_double")
        self.yellow_double = units.Relay("yellow_double")
        self.green_double = units.Relay("green_double")
        self.spot_12 = units.Relay("spot_12")
        self.spot_13 = units.Relay("spot_13")

        self.replays = 0
        self.returned = False

    def reset(self):
        super(DoubleHeader, self).reset()
        self.logger = logging.getLogger('game')
        self.load_config('bingo.yaml')
        
        main_mode = SinglecardBingo(self)
        self.modes.add(main_mode)
        
game = DoubleHeader(machine_type='pdb')
game.reset()
game.run_loop()
