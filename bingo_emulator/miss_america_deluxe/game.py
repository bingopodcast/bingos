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
from bingo_emulator.graphics.miss_america_deluxe import *

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

        self.delay(name="display", delay=0.1, handler=graphics.miss_america_deluxe.display, param=self)

    def sw_startButton_active(self, sw):
        self.game.eb_play.disengage()
        if self.game.replays > 0 or self.game.switches.freeplay.is_active():
            self.game.sound.stop('add')
            self.game.sound.play('add')
            self.game.tilt.disengage()
            self.regular_play()
            self.scan_all()
            self.delay(name="display", delay=0.1, handler=graphics.miss_america_deluxe.display, param=self)

    def sw_enter_active(self, sw):
        if self.game.switches.left.is_active() and self.game.switches.right.is_active():
            self.game.end_run_loop()
            os.system("/home/nbaldridge/proc/bingo_emulator/start_game.sh miss_america_deluxe")
        if self.game.selection_feature.position >= 7 and (self.game.lockout.status == False):
            self.game.line3.step()
        self.delay(name="display", delay=0.1, handler=graphics.miss_america_deluxe.display, param=self)
        if self.game.ball_count.position >= 4:
            self.game.sound.stop_music()
            if self.game.search_index.status == False:
                self.game.sound.play('search')
                self.search()

    def sw_enter_active_for_2s(self, sw):
        if self.game.switches.left.is_active() and self.game.switches.right.is_active():
            self.game.end_run_loop()
            os.system("/home/nbaldridge/proc/bingo_emulator/start_game.sh miss_america_deluxe")
        else:
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.game.sound.play('search')
                    red_letter_winner = self.find_red_letter_winner()
                    self.find_winner(red_letter_winner, 0, 0, 0, 0, red_letter_winner)

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
        if self.game.selection_feature.position >= 5 and (self.game.lockout.status == False):
            self.game.line1.step()
        self.delay(name="display", delay=0.1, handler=graphics.miss_america_deluxe.display, param=self)

    def sw_right_active(self, sw):
        if self.game.selection_feature.position >= 6 and (self.game.lockout.status == False):
            self.game.line2.step()
        self.delay(name="display", delay=0.1, handler=graphics.miss_america_deluxe.display, param=self)

    def sw_blue_active(self, sw):
        if self.game.selection_feature.position >= 8 and (self.game.lockout.status == False):
            self.game.line4.step()
        self.delay(name="display", delay=0.1, handler=graphics.miss_america_deluxe.display, param=self)

    def sw_green_active(self, sw):
        if self.game.selection_feature.position >= 9 and (self.game.lockout.status == False):
            self.game.line5.step()
        self.delay(name="display", delay=0.1, handler=graphics.miss_america_deluxe.display, param=self)

    def check_shutter(self, start=0):
        if start == 1:
            if self.game.switches.smRunout.is_active():
                if self.game.switches.shutter.is_active():
                    self.game.coils.shutter.disable()
        else:
            if self.game.switches.shutter.is_inactive():
                if self.game.switches.smRunout.is_active():
                    self.game.coils.shutter.disable()


    def regular_play(self, red_letter=0):
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
            if self.game.rollovers.status == True:
                if self.game.cu:
                    self.game.coils.yellowROLamp.disable()
                    self.game.coils.redROLamp.enable()
                else:
                    self.game.coils.yellowROLamp.enable()
                    self.game.coils.redROLamp.disable()
            if self.game.switches.shutter.is_inactive():
                self.game.coils.shutter.enable()
            self.replay_step_down()
            self.check_lifter_status()
        else:
            if red_letter > 0:
                if self.game.switches.shutter.is_inactive():
                    self.game.coils.shutter.enable()
                self.check_lifter_status()
                self.holes = []
                self.game.red_replay_counter.reset()
                self.game.green_replay_counter.reset()
                self.game.yellow_replay_counter.reset()
                self.game.white_replay_counter.reset()
                self.game.rollovers.disengage()
                self.game.coils.yellowROLamp.disable()
                self.game.coils.redROLamp.disable()
                self.game.corners.disengage()
                self.game.striped_diagonals.disengage()
                self.game.green_odds.reset()
                self.game.yellow_odds.reset()
                self.game.white_odds.reset()
                self.game.selector.reset()
                self.game.lockout.disengage()
                self.game.green_corners.disengage()
                self.game.red_letter_two.disengage()
                self.game.red_letter_three.disengage()
                self.game.before_fifth.disengage()
                self.game.before_fourth.disengage()
                self.game.before_fourth.engage(self.game)
                self.game.line1.reset()
                self.game.line2.reset()
                self.game.line3.reset()
                self.game.line4.reset()
                self.game.line5.reset()
                self.game.selection_feature.reset()
                self.game.ball_count.reset()
                self.game.extra_ball.reset()
                self.game.timer.reset()
                self.game.sound.play_music('motor', -1)
                if red_letter == 1:
                    self.yellow_extra_step(3)
                    self.green_extra_step(5)
                    self.white_extra_step(3)
                    self.game.selector.step()
                    self.game.selector.step()
                    self.step_selection(7)
                    self.game.sound.play_music('motor', -1)
                    self.game.start.engage(self.game)
                if red_letter == 2:
                    self.yellow_extra_step(3)
                    self.green_extra_step(5)
                    self.white_extra_step(3)
                    self.game.selector.step()
                    self.game.selector.step()
                    self.step_selection(7)
                    self.game.sound.play_music('motor', -1)
                    self.game.start.engage(self.game)
                if red_letter == 3:
                    self.yellow_extra_step(5)
                    self.green_extra_step(4)
                    self.white_extra_step(5)
                    self.game.selector.step()
                    self.game.selector.step()
                    self.step_selection(8)
                    self.game.sound.play_music('motor', -1)
                    self.game.rollovers.engage(self.game)
                    if self.game.rollovers.status == True:
                        if self.game.cu:
                            self.game.coils.yellowROLamp.disable()
                            self.game.coils.redROLamp.enable()
                        else:
                            self.game.coils.yellowROLamp.enable()
                            self.game.coils.redROLamp.disable()
                    self.game.start.engage(self.game)
                if red_letter == 4:
                    self.yellow_extra_step(6)
                    self.green_extra_step(5)
                    self.white_extra_step(6)
                    self.game.selector.step()
                    self.game.selector.step()
                    self.step_selection(8)
                    self.game.sound.play_music('motor', -1)
                    self.game.rollovers.engage(self.game)
                    if self.game.rollovers.status == True:
                        if self.game.cu:
                            self.game.coils.yellowROLamp.disable()
                            self.game.coils.redROLamp.enable()
                        else:
                            self.game.coils.yellowROLamp.enable()
                            self.game.coils.redROLamp.disable()
                    self.game.striped_diagonals.engage(self.game)
                    self.game.start.engage(self.game)
                if red_letter == 5:
                    self.yellow_extra_step(7)
                    self.green_extra_step(6)
                    self.white_extra_step(6)
                    self.game.selector.step()
                    self.game.selector.step()
                    self.step_selection(9)
                    self.game.sound.play_music('motor', -1)
                    self.game.before_fourth.disengage()
                    self.game.before_fifth.engage(self.game)
                    self.game.corners.engage(self.game)
                    self.game.striped_diagonals.engage(self.game)
                    self.game.start.engage(self.game)
                if red_letter == 6:
                    self.yellow_extra_step(7)
                    self.green_extra_step(6)
                    self.white_extra_step(7)
                    self.game.selector.step()
                    self.game.selector.step()
                    self.step_selection(9)
                    self.game.sound.play_music('motor', -1)
                    self.game.before_fourth.disengage()
                    self.game.before_fifth.engage(self.game)
                    self.game.corners.engage(self.game)
                    self.game.green_corners.engage(self.game)
                    self.game.striped_diagonals.engage(self.game)
                    self.game.start.engage(self.game)
                if red_letter == 7:
                    self.yellow_extra_step(7)
                    self.green_extra_step(7)
                    self.white_extra_step(7)
                    self.game.selector.step()
                    self.game.selector.step()
                    self.step_selection(9)
                    self.game.sound.play_music('motor', -1)
                    self.game.before_fourth.disengage()
                    self.game.before_fifth.engage(self.game)
                    self.game.corners.engage(self.game)
                    self.game.green_corners.engage(self.game)
                    self.game.striped_diagonals.engage(self.game)
                    self.game.start.engage(self.game)
            else:
                self.holes = []
                self.game.red_replay_counter.reset()
                self.game.green_replay_counter.reset()
                self.game.yellow_replay_counter.reset()
                self.game.white_replay_counter.reset()
                self.game.corners.disengage()
                self.game.red_odds.reset()
                self.game.green_odds.reset()
                self.game.yellow_odds.reset()
                self.game.white_odds.reset()
                self.game.lockout.disengage()
                self.game.green_corners.disengage()
                self.game.red_letter_two.disengage()
                self.game.red_letter_three.disengage()
                self.game.before_fifth.disengage()
                self.game.before_fourth.disengage()
                self.game.before_fourth.engage(self.game)
                self.game.line1.reset()
                self.game.line2.reset()
                self.game.line3.reset()
                self.game.line4.reset()
                self.game.line5.reset()
                self.game.striped_diagonals.disengage()
                self.game.selection_feature.reset()
                self.game.ball_count.reset()
                self.game.extra_ball.reset()
                self.game.selector.reset()
                self.game.timer.reset()
                self.game.sound.play_music('motor', -1)
                self.game.start.engage(self.game)
                self.regular_play()
        self.delay(name="display", delay=0.1, handler=graphics.miss_america_deluxe.display, param=self)
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
        if self.game.before_fourth.status == True:
            if self.game.ball_count.position >= 4:
                self.game.before_fourth.disengage()
                self.game.lockout.engage(self.game)
        elif self.game.before_fifth.status == True:
            if self.game.ball_count.position >= 5:
                self.game.before_fifth.disengage()
                self.game.lockout.engage(self.game)
        self.delay(name="display", delay=0.1, handler=graphics.miss_america_deluxe.display, param=self)

    def sw_redstar_active(self, sw):
        if not self.game.cu:
            if self.game.rollovers.status == True:
                self.game.before_fifth.engage(self.game)
                self.game.before_fourth.disengage()
                self.game.rollovers.disengage()
                self.game.coils.yellowROLamp.disable()
        self.delay(name="display", delay=0.1, handler=graphics.miss_america_deluxe.display, param=self)

    def sw_yellowstar_active(self, sw):
        if self.game.cu:
            if self.game.rollovers.status == True:
                self.game.before_fifth.engage(self.game)
                self.game.before_fourth.disengage()
                self.game.rollovers.disengage()
                self.game.coils.redROLamp.disable()
        self.delay(name="display", delay=0.1, handler=graphics.miss_america_deluxe.display, param=self)

    # This is really nasty, but it is how we render graphics for each individual hole.
    # numbers are added (or removed from) a list.  In this way, I can re-use the same
    # routine even for games where there are ball return functions like Surf Club.

    def sw_hole1_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(1)
            self.delay(name="display", delay=0.1, handler=graphics.miss_america_deluxe.display, param=self)

    def sw_hole2_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(2)
            self.delay(name="display", delay=0.1, handler=graphics.miss_america_deluxe.display, param=self)

    def sw_hole3_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(3)
            self.delay(name="display", delay=0.1, handler=graphics.miss_america_deluxe.display, param=self)

    def sw_hole4_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(4)
            self.delay(name="display", delay=0.1, handler=graphics.miss_america_deluxe.display, param=self)

    def sw_hole5_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(5)
            self.delay(name="display", delay=0.1, handler=graphics.miss_america_deluxe.display, param=self)

    def sw_hole6_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(6)
            self.delay(name="display", delay=0.1, handler=graphics.miss_america_deluxe.display, param=self)

    def sw_hole7_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(7)
            self.delay(name="display", delay=0.1, handler=graphics.miss_america_deluxe.display, param=self)

    def sw_hole8_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(8)
            self.delay(name="display", delay=0.1, handler=graphics.miss_america_deluxe.display, param=self)

    def sw_hole9_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(9)
            self.delay(name="display", delay=0.1, handler=graphics.miss_america_deluxe.display, param=self)

    def sw_hole10_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(10)
            self.delay(name="display", delay=0.1, handler=graphics.miss_america_deluxe.display, param=self)

    def sw_hole11_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(11)
            self.delay(name="display", delay=0.1, handler=graphics.miss_america_deluxe.display, param=self)

    def sw_hole12_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(12)
            self.delay(name="display", delay=0.1, handler=graphics.miss_america_deluxe.display, param=self)

    def sw_hole13_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(13)
            self.delay(name="display", delay=0.1, handler=graphics.miss_america_deluxe.display, param=self)

    def sw_hole14_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(14)
            self.delay(name="display", delay=0.1, handler=graphics.miss_america_deluxe.display, param=self)

    def sw_hole15_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(15)
            self.delay(name="display", delay=0.1, handler=graphics.miss_america_deluxe.display, param=self)

    def sw_hole16_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(16)
            self.delay(name="display", delay=0.1, handler=graphics.miss_america_deluxe.display, param=self)

    def sw_hole17_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(17)
            self.delay(name="display", delay=0.1, handler=graphics.miss_america_deluxe.display, param=self)

    def sw_hole18_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(18)
            self.delay(name="display", delay=0.1, handler=graphics.miss_america_deluxe.display, param=self)

    def sw_hole19_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(19)
            self.delay(name="display", delay=0.1, handler=graphics.miss_america_deluxe.display, param=self)

    def sw_hole20_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(20)
            self.delay(name="display", delay=0.1, handler=graphics.miss_america_deluxe.display, param=self)

    def sw_hole21_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(21)
            self.delay(name="display", delay=0.1, handler=graphics.miss_america_deluxe.display, param=self)

    def sw_hole22_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(22)
            self.delay(name="display", delay=0.1, handler=graphics.miss_america_deluxe.display, param=self)

    def sw_hole23_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(23)
            self.delay(name="display", delay=0.1, handler=graphics.miss_america_deluxe.display, param=self)

    def sw_hole24_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(24)
            self.delay(name="display", delay=0.1, handler=graphics.miss_america_deluxe.display, param=self)

    def sw_hole25_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(25)
            self.delay(name="display", delay=0.1, handler=graphics.miss_america_deluxe.display, param=self)

    def sw_replayReset_active(self, sw):
        self.game.anti_cheat.disengage()
        self.holes = []
#        self.cancel_delayed(name="blink_title")
        graphics.miss_america_deluxe.display(self)
        self.tilt_actions()
#        self.delay(name="blink_title", delay=1, handler=self.blink_title)
        self.replay_step_down(self.game.replays)

    def tilt_actions(self):
        self.game.start.disengage()
        self.cancel_delayed(name="replay_reset")
        self.cancel_delayed(name="red_replay_step_up")
        self.cancel_delayed(name="yellow_replay_step_up")
        self.cancel_delayed(name="green_replay_step_up")
        self.cancel_delayed(name="white_replay_step_up")
        self.game.red_replay_counter.reset()
        self.game.green_replay_counter.reset()
        self.game.yellow_replay_counter.reset()
        self.game.white_replay_counter.reset()
        self.game.corners.disengage()
        self.game.red_odds.reset()
        self.game.green_odds.reset()
        self.game.yellow_odds.reset()
        self.game.white_odds.reset()
        self.game.lockout.disengage()
        self.game.green_corners.disengage()
        self.game.red_letter_two.disengage()
        self.game.red_letter_three.disengage()
        self.game.before_fifth.disengage()
        self.game.before_fourth.disengage()
        self.game.striped_diagonals.disengage()
        self.game.line1.reset()
        self.game.line2.reset()
        self.game.line3.reset()
        self.game.line4.reset()
        self.game.line5.reset()
        self.game.selection_feature.reset()
        self.game.selector.reset()
        self.game.ball_count.reset()
        self.game.extra_ball.reset()
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
        self.delay(name="display", delay=0.1, handler=graphics.miss_america_deluxe.display, param=self)

    def sw_tilt_active(self, sw):
        if self.game.tilt.status == False:
            self.tilt_actions()

    def replay_step_down(self, number=0):
        if number > 0:
            if number > 1:
                self.game.replays -= 1
                graphics.replay_step_down(self.game.replays, graphics.miss_america_deluxe.reel1, graphics.miss_america_deluxe.reel10, graphics.miss_america_deluxe.reel100)
                self.game.coils.registerDown.pulse()
                number -= 1
                graphics.miss_america_deluxe.display(self)
                self.delay(name="replay_reset", delay=0.0, handler=self.replay_step_down, param=number)
            elif number == 1:
                self.game.replays -= 1
                graphics.replay_step_down(self.game.replays, graphics.miss_america_deluxe.reel1, graphics.miss_america_deluxe.reel10, graphics.miss_america_deluxe.reel100)
                self.game.coils.registerDown.pulse()
                number -= 1
                graphics.miss_america_deluxe.display(self)
                self.cancel_delayed(name="replay_reset")
        else: 
            if self.game.replays > 0:
                self.game.replays -= 1
                graphics.replay_step_down(self.game.replays, graphics.miss_america_deluxe.reel1, graphics.miss_america_deluxe.reel10, graphics.miss_america_deluxe.reel100)
                self.delay(name="display", delay=0.1, handler=graphics.miss_america_deluxe.display, param=self)
            self.game.coils.registerDown.pulse()

    def replay_step_up(self):
        if self.game.replays < 899:
            self.game.replays += 1
            graphics.replay_step_up(self.game.replays, graphics.miss_america_deluxe.reel1, graphics.miss_america_deluxe.reel10, graphics.miss_america_deluxe.reel100)
        self.game.coils.registerUp.pulse()
        self.game.reflex.increase()
        graphics.miss_america_deluxe.display(self)

    def sw_yellow_active(self, sw):
        if self.game.ball_count.position >= 5:
            if self.game.eb_play.status == False:
                self.game.spotting.spin()
                self.game.mixer1.spin()
                self.game.mixer2.spin()
                self.game.mixer3.spin()
                self.game.mixer4.spin()
                self.game.eb_play.engage(self.game)
                self.delay(name="display", delay=0.1, handler=graphics.miss_america_deluxe.display, param=self)
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
                self.delay(name="display", delay=0.1, handler=graphics.miss_america_deluxe.display, param=self)
            
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
            self.color = self.r[3]
            self.stars = self.r[4]
            self.striped = self.r[5]

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
                            if s >= 2:
                                self.find_winner(s, self.card, self.corners, self.color, self.stars, self.striped)
                                break
#        self.delay(name="blink_title", delay=3, handler=self.blink_title)

    def find_winner(self, relays, card, corners, color, stars, striped, red_letter_winner=0):
        if self.game.search_index.status == False and self.game.replays < 899:
            if color == "red":
                if self.game.red_odds.position == 1:
                    threeodds = 4
                    fourodds = 16
                    fiveodds = 75
                elif self.game.red_odds.position == 2:
                    threeodds = 8
                    fourodds = 24
                    fiveodds = 96
                elif self.game.red_odds.position == 3:
                    threeodds = 16
                    fourodds = 50
                    fiveodds = 96
                elif self.game.red_odds.position == 4:
                    threeodds = 32
                    fourodds = 96
                    fiveodds = 200
                elif self.game.red_odds.position == 5:
                    threeodds = 64
                    fourodds = 144
                    fiveodds = 300
                elif self.game.red_odds.position == 6:
                    threeodds = 128
                    fourodds = 192
                    fiveodds = 400
                elif self.game.red_odds.position == 7:
                    threeodds = 192
                    fourodds = 400
                    fiveodds = 600
            elif color == "yellow":
                if self.game.yellow_odds.position == 1:
                    threeodds = 4
                    fourodds = 16
                    fiveodds = 75
                elif self.game.yellow_odds.position == 2:
                    threeodds = 8
                    fourodds = 24
                    fiveodds = 96
                elif self.game.yellow_odds.position == 3:
                    threeodds = 16
                    fourodds = 50
                    fiveodds = 96
                elif self.game.yellow_odds.position == 4:
                    threeodds = 32
                    fourodds = 96
                    fiveodds = 200
                elif self.game.yellow_odds.position == 5:
                    threeodds = 64
                    fourodds = 144
                    fiveodds = 300
                elif self.game.yellow_odds.position == 6:
                    threeodds = 128
                    fourodds = 192
                    fiveodds = 400
                elif self.game.yellow_odds.position == 7:
                    threeodds = 192
                    fourodds = 400
                    fiveodds = 600
            elif color == "green" or (stars >= 1):
                if self.game.green_odds.position == 1:
                    threeodds = 4
                    fourodds = 16
                    fiveodds = 75
                elif self.game.green_odds.position == 2:
                    threeodds = 8
                    fourodds = 24
                    fiveodds = 96
                elif self.game.green_odds.position == 3:
                    threeodds = 16
                    fourodds = 50
                    fiveodds = 96
                elif self.game.green_odds.position == 4:
                    threeodds = 32
                    fourodds = 96
                    fiveodds = 200
                elif self.game.green_odds.position == 5:
                    threeodds = 64
                    fourodds = 144
                    fiveodds = 300
                elif self.game.green_odds.position == 6:
                    threeodds = 128
                    fourodds = 192
                    fiveodds = 400
                elif self.game.green_odds.position == 7:
                    threeodds = 192
                    fourodds = 400
                    fiveodds = 600
            elif color == "white":
                if self.game.white_odds.position == 1:
                    threeodds = 4
                    fourodds = 16
                    fiveodds = 75
                elif self.game.white_odds.position == 2:
                    threeodds = 8
                    fourodds = 24
                    fiveodds = 96
                elif self.game.white_odds.position == 3:
                    threeodds = 16
                    fourodds = 50
                    fiveodds = 96
                elif self.game.white_odds.position == 4:
                    threeodds = 32
                    fourodds = 96
                    fiveodds = 200
                elif self.game.white_odds.position == 5:
                    threeodds = 64
                    fourodds = 144
                    fiveodds = 300
                elif self.game.white_odds.position == 6:
                    threeodds = 128
                    fourodds = 192
                    fiveodds = 400
                elif self.game.white_odds.position == 7:
                    threeodds = 192
                    fourodds = 400
                    fiveodds = 600

            if relays == 2 and red_letter_winner == 2:
                if self.game.selector.position >= 2:
                    if self.game.red_letter_two.status == True:
                        red_letter = self.game.red_odds.position
                        self.regular_play(red_letter)
            if relays == 3:
                if not corners:
                    if self.game.selector.position >= 2 and red_letter_winner == 3:
                        if self.game.red_letter_three.status == True:
                            red_letter = self.game.red_odds.position
                            self.regular_play(red_letter)
                    if self.game.selector.position >= 1:
                        if color == "red":
                            if self.game.red_replay_counter.position < threeodds:
                                self.game.search_index.engage(self.game)
                                self.red_replay_step_up(threeodds - self.game.red_replay_counter.position)
                        elif color == "yellow":
                            if self.game.yellow_replay_counter.position < threeodds:
                                self.game.search_index.engage(self.game)
                                self.yellow_replay_step_up(threeodds - self.game.yellow_replay_counter.position)
                    if self.game.selector.position >= 2:
                        if color == "green":
                            if striped == True:
                                if self.game.striped_diagonals.status == True:
                                    if self.game.green_replay_counter.position < threeodds:
                                        self.game.search_index.engage(self.game)
                                        self.green_replay_step_up(threeodds - self.game.green_replay_counter.position)
                            else:
                                if self.game.green_replay_counter.position < threeodds:
                                    self.game.search_index.engage(self.game)
                                    self.green_replay_step_up(threeodds - self.game.green_replay_counter.position)
                        elif color == "white":
                            if striped == True:
                                if self.game.striped_diagonals.status == True:
                                    if self.game.white_replay_counter.position < threeodds:
                                        self.game.search_index.engage(self.game)
                                        self.white_replay_step_up(threeodds - self.game.white_replay_counter.position)
                            else:
                                if self.game.white_replay_counter.position < threeodds:
                                    self.game.search_index.engage(self.game)
                                    self.white_replay_step_up(threeodds - self.game.white_replay_counter.position)
            if relays == 4:
                if self.game.selector.position >= 2 and red_letter_winner >= 3:
                    if self.game.red_letter_three.status == True:
                        red_letter = self.game.red_odds.position
                        self.regular_play(red_letter)
                if stars >= 1 and self.game.green_corners.status == True:
                    if self.game.green_corners.status == True and self.game.selector.position >= 2:
                        if self.game.green_replay_counter.position < fourodds:
                            self.game.search_index.engage(self.game)
                            self.green_replay_step_up(fourodds - self.game.green_replay_counter.position)
                elif corners and self.game.corners.status == True:
                    if self.game.corners.status == True:
                        if self.game.red_replay_counter.position < fiveodds:
                            self.game.search_index.engage(self.game)
                            self.red_replay_step_up(fiveodds - self.game.red_replay_counter.position)
                else:
                    if not corners:
                        if self.game.selector.position >= 1:
                            if color == "red":
                                if self.game.red_replay_counter.position < fourodds:
                                    self.game.search_index.engage(self.game)
                                    self.red_replay_step_up(fourodds - self.game.red_replay_counter.position)
                            elif color == "yellow":
                                if self.game.yellow_replay_counter.position < fourodds:
                                    self.game.search_index.engage(self.game)
                                    self.yellow_replay_step_up(fourodds - self.game.yellow_replay_counter.position)
                        if self.game.selector.position >= 2:
                            if color == "green":
                                if striped == True:
                                    if self.game.striped_diagonals.status == True:
                                        if self.game.green_replay_counter.position < fourodds:
                                            self.game.search_index.engage(self.game)
                                            self.green_replay_step_up(fourodds - self.game.green_replay_counter.position)
                                else:
                                    if self.game.green_replay_counter.position < fourodds:
                                        self.game.search_index.engage(self.game)
                                        self.green_replay_step_up(fourodds - self.game.green_replay_counter.position)
                            elif color == "white":
                                if striped == True:
                                    if self.game.striped_diagonals.status == True:
                                        if self.game.white_replay_counter.position < fourodds:
                                            self.game.search_index.engage(self.game)
                                            self.white_replay_step_up(fourodds - self.game.white_replay_counter.position)
                                else:
                                    if self.game.white_replay_counter.position < fourodds:
                                        self.game.search_index.engage(self.game)
                                        self.white_replay_step_up(fourodds - self.game.white_replay_counter.position)
            if relays == 5:
                if self.game.selector.position >= 1:
                    if color == "red":
                        if self.game.red_replay_counter.position < fiveodds:
                            self.game.search_index.engage(self.game)
                            self.red_replay_step_up(fiveodds - self.game.red_replay_counter.position)
                    elif color == "yellow":
                        if self.game.yellow_replay_counter.position < fiveodds:
                            self.game.search_index.engage(self.game)
                            self.yellow_replay_step_up(fiveodds - self.game.yellow_replay_counter.position)
                if self.game.selector.position >= 2:
                    if color == "green":
                        if self.game.green_replay_counter.position < fiveodds:
                            self.game.search_index.engage(self.game)
                            self.green_replay_step_up(fiveodds - self.game.green_replay_counter.position)
                    elif color == "white":
                        if self.game.white_replay_counter.position < fiveodds:
                            self.game.search_index.engage(self.game)
                            self.white_replay_step_up(fiveodds - self.game.white_replay_counter.position)


    def red_replay_step_up(self, number):
        if number >= 1:
            self.game.red_replay_counter.step()
            number -= 1
            self.replay_step_up()
            if self.game.replays == 899:
                number = 0
            self.delay(name="red_replay_step_up", delay=0.1, handler=self.red_replay_step_up, param=number)
        else:
            self.game.search_index.disengage()
            self.cancel_delayed(name="red_replay_step_up")
            self.search()

    def yellow_replay_step_up(self, number):
        if number >= 1:
            self.game.yellow_replay_counter.step()
            number -= 1
            self.replay_step_up()
            if self.game.replays == 899:
                number = 0
            self.delay(name="yellow_replay_step_up", delay=0.1, handler=self.yellow_replay_step_up, param=number)
        else:
            self.game.search_index.disengage()
            self.cancel_delayed(name="yellow_replay_step_up")
            self.search()

    def green_replay_step_up(self, number):
        if number >= 1:
            self.game.green_replay_counter.step()
            number -= 1
            self.replay_step_up()
            if self.game.replays == 899:
                number = 0
            self.delay(name="green_replay_step_up", delay=0.1, handler=self.green_replay_step_up, param=number)
        else:
            self.game.search_index.disengage()
            self.cancel_delayed(name="green_replay_step_up")
            self.search()

    def white_replay_step_up(self, number):
        if number >= 1:
            self.game.white_replay_counter.step()
            number -= 1
            self.replay_step_up()
            if self.game.replays == 899:
                number = 0
            self.delay(name="white_replay_step_up", delay=0.1, handler=self.white_replay_step_up, param=number)
        else:
            self.game.search_index.disengage()
            self.cancel_delayed(name="white_replay_step_up")
            self.search()

    def find_red_letter_winner(self):
        red_letter_winner = 0
        if self.game.line1.position == 0 or self.game.line1.position == 2:
            self.p8 = 11
        elif self.game.line1.position == 1:
            self.p8 = 8
        elif self.game.line1.position == 3:
            self.p8 = 10


        if self.game.line3.position == 0 or self.game.line3.position == 2:
            self.r6 = 15
            self.r10 = 25
        elif self.game.line3.position == 1:
            self.r6 = 3
            self.r10 = 17
        elif self.game.line3.position == 3:
            self.r6 = 18
            self.r10 = 23

        if self.game.line5.position == 0 or self.game.line5.position == 2:
            self.t8 = 9
        elif self.game.line5.position == 1:
            self.t8 = 13
        elif self.game.line5.position == 3:
            self.t8 = 5

        if self.p8 in self.holes:
            red_letter_winner += 1
        if self.r6 in self.holes:
            red_letter_winner += 1
        if self.r10 in self.holes:
            red_letter_winner += 1
        if self.t8 in self.holes:
            red_letter_winner += 1

        return (red_letter_winner)


    def closed_search_relays(self, rivets, c):
        # This function is critical, as it will determine which card is returned, etc.  I need to check the position of the
        # replay counter for the card. We will get a row back
        # that has the numbers on the position which will return the search relay connected.  When three out of the five relays
        # are connected, we get a winner!
        #Modifying this from the manual - too crazy.

        if self.game.line1.position == 0 or self.game.line1.position == 2:
            self.p1 = 5
            self.p2 = 14
            self.p3 = 8
            self.p4 = 6
            self.p5 = 25

            self.p6 = 6
            self.p7 = 8
            self.p8 = 11
            self.p9 = 10
            self.p10 = 2
        elif self.game.line1.position == 1:
            self.p1 = 2
            self.p2 = 5
            self.p3 = 14
            self.p4 = 8
            self.p5 = 6

            self.p6 = 25
            self.p7 = 6
            self.p8 = 8
            self.p9 = 11
            self.p10 = 10
        elif self.game.line1.position == 3:
            self.p1 = 14
            self.p2 = 8
            self.p3 = 6
            self.p4 = 25
            self.p5 = 6

            self.p6 = 8
            self.p7 = 11
            self.p8 = 10
            self.p9 = 2
            self.p10 = 5

        if self.game.line2.position == 0 or self.game.line2.position == 2:
            self.q1 = 2
            self.q2 = 19
            self.q3 = 1
            self.q4 = 20
            self.q5 = 13
            
            self.q6 = 14
            self.q7 = 19
            self.q8 = 23
            self.q9 = 22
            self.q10 = 7
        elif self.game.line2.position == 1:
            self.q1 = 7
            self.q2 = 2
            self.q3 = 19
            self.q4 = 1
            self.q5 = 20

            self.q6 = 13
            self.q7 = 14
            self.q8 = 19
            self.q9 = 23
            self.q10 = 22
        elif self.game.line2.position == 3:
            self.q1 = 19
            self.q2 = 1
            self.q3 = 20
            self.q4 = 13
            self.q5 = 14

            self.q6 = 19
            self.q7 = 23
            self.q8 = 22
            self.q9 = 7
            self.q10 = 2

        if self.game.line3.position == 0 or self.game.line3.position == 2:
            self.r1 = 23
            self.r2 = 9
            self.r3 = 17
            self.r4 = 12
            self.r5 = 3

            self.r6 = 15
            self.r7 = 18
            self.r8 = 16
            self.r9 = 17
            self.r10 = 25
        elif self.game.line3.position == 1:
            self.r1 = 25
            self.r2 = 23
            self.r3 = 9
            self.r4 = 17
            self.r5 = 12

            self.r6 = 3
            self.r7 = 15
            self.r8 = 18
            self.r9 = 16
            self.r10 = 17
        elif self.game.line3.position == 3:
            self.r1 = 9
            self.r2 = 17
            self.r3 = 12
            self.r4 = 3
            self.r5 = 15

            self.r6 = 18
            self.r7 = 16
            self.r8 = 17
            self.r9 = 25
            self.r10 = 23

        if self.game.line4.position == 0 or self.game.line4.position == 2:
            self.s1 = 16
            self.s2 = 22
            self.s3 = 18
            self.s4 = 21
            self.s5 = 7
            
            self.s6 = 1
            self.s7 = 20
            self.s8 = 12
            self.s9 = 21
            self.s10 = 3
        elif self.game.line4.position == 1:
            self.s1 = 3
            self.s2 = 16
            self.s3 = 22
            self.s4 = 18
            self.s5 = 21

            self.s6 = 7
            self.s7 = 1
            self.s8 = 20
            self.s9 = 12
            self.s10 = 21
        elif self.game.line4.position == 3:
            self.s1 = 22
            self.s2 = 18
            self.s3 = 21
            self.s4 = 7
            self.s5 = 1

            self.s6 = 20
            self.s7 = 12
            self.s8 = 21
            self.s9 = 3
            self.s10 = 16

        if self.game.line5.position == 0 or self.game.line5.position == 2:
            self.t1 = 15
            self.t2 = 4
            self.t3 = 10
            self.t4 = 11
            self.t5 = 24

            self.t6 = 24
            self.t7 = 13
            self.t8 = 9
            self.t9 = 5
            self.t10 = 4
        elif self.game.line5.position == 1:
            self.t1 = 4
            self.t2 = 15
            self.t3 = 4
            self.t4 = 10
            self.t5 = 11

            self.t6 = 24
            self.t7 = 24
            self.t8 = 13
            self.t9 = 9
            self.t10 = 5
        elif self.game.line5.position == 3:
            self.t1 = 4
            self.t2 = 10
            self.t3 = 11
            self.t4 = 24
            self.t5 = 24

            self.t6 = 13
            self.t7 = 9
            self.t8 = 5
            self.t9 = 4
            self.t10 = 15

        self.pos = {}
        self.pos[0] = {}
        #Main Card Yellow
        #Horizontal
        self.pos[1] = {self.p1:1, self.p2:2, self.p3:3, self.p4:4, self.p5:5}
        self.pos[2] = {self.q1:1, self.q2:2, self.q3:3, self.q4:4, self.q5:5}
        self.pos[3] = {self.s1:1, self.s2:2, self.s3:3, self.s4:4, self.s5:5}
        self.pos[4] = {self.t1:1, self.t2:2, self.t3:3, self.t4:4, self.t5:5}
        #Vertical
        self.pos[5] = {self.p1:1, self.q1:2, self.r1:3, self.s1:4, self.t1:5}
        self.pos[6] = {self.p3:1, self.q3:2, self.r3:3, self.s3:4, self.t3:5}
        self.pos[7] = {self.p5:1, self.q5:2, self.r5:3, self.s5:4, self.t5:5}
        self.pos[8] = {}
        #Main Card Red
        #Horizontal
        self.pos[9] = {self.r1:1, self.r2:2, self.r3:3, self.r4:4, self.r5:5}
        #Vertical
        self.pos[10] = {self.p2:1, self.q2:2, self.r2:3, self.s2:4, self.t2:5}
        self.pos[11] = {self.p4:1, self.q4:2, self.r4:3, self.s4:4, self.t4:5}
        #Diagonal
        self.pos[12] = {self.p1:1, self.q2:2, self.r3:3, self.s4:4, self.t5:5}
        self.pos[13] = {self.p5:1, self.q4:2, self.r3:3, self.s2:4, self.t1:5}
        self.pos[14] = {}
        #Corners
        self.pos[15] = {self.p1:1, self.p5:2, self.t1:3, self.t5:4}
        self.pos[16] = {}
        self.pos[17] = {}

        #Extra Card
        #White
        #Horizontal
        self.pos[18] = {self.p6:1, self.p7:2, self.p8:3, self.p9:4, self.p10:5}
        self.pos[19] = {self.q6:1, self.q7:2, self.q8:3, self.q9:4, self.q10:5}
        self.pos[20] = {self.s6:1, self.s7:2, self.s8:3, self.s9:4, self.s10:5}
        self.pos[21] = {self.t6:1, self.t7:2, self.t8:3, self.t9:4, self.t10:5}
        #Vertical
        self.pos[22] = {self.p6:1, self.q6:2, self.r6:3, self.s6:4, self.t6:5}
        self.pos[23] = {self.p8:1, self.q8:2, self.r8:3, self.s8:4, self.t8:5}
        self.pos[24] = {self.p10:1, self.q10:2, self.r10:3, self.s10:4, self.t10:5}
        self.pos[25] = {}

        #Green
        #Horizontal
        self.pos[26] = {self.r6:1, self.r7:2, self.r8:3, self.r9:4, self.r10:5}
        #Vertical
        self.pos[27] = {self.p7:1, self.q7:2, self.r7:3, self.s7:4, self.t7:5}
        self.pos[28] = {self.p9:1, self.q9:2, self.r9:3, self.s9:4, self.t9:5}
        #Diagonal
        self.pos[29] = {self.p6:1, self.q7:2, self.r8:3, self.s9:4, self.t10:5}
        self.pos[30] = {self.p10:1, self.q9:2, self.r8:3, self.s7:4, self.t6:5}
        self.pos[31] = {}
        self.pos[32] = {}
        self.pos[33] = {}
        self.pos[34] = {}
        self.pos[35] = {}
        self.pos[36] = {self.p8:1, self.r6:2, self.r10:3, self.t8:4}
        self.pos[37] = {}
        #Green Striped Diagonals
        self.pos[38] = {self.s6:1, self.r7:2, self.q8:3, self.p9:4}
        self.pos[39] = {self.q6:1, self.r7:2, self.s8:3, self.t9:4}
        self.pos[40] = {self.t8:1, self.s9:2, self.r10:3}
        self.pos[41] = {self.p8:1, self.q9:2, self.r10:3}
        self.pos[42] = {}
        self.pos[43] = {}
        #White Striped Diagonals
        self.pos[44] = {self.p7:1, self.q8:2, self.r9:3, self.s10:4}
        self.pos[45] = {self.q10:1, self.r9:2, self.s8:3, self.t7:4}
        self.pos[46] = {self.r6:1, self.s7:2, self.t8:3}
        self.pos[47] = {self.p8:1, self.q7:2, self.r6:3}
        self.pos[48] = {}
        self.pos[49] = {}
        self.pos[50] = {}

        corners = False
        card = 0
        color = None
        stars = False
        striped = False

        if rivets in range(0, 8):
            color = "yellow"
        if rivets in range(9, 17):
            color = "red"
            if rivets == 15:
                corners = True
        if rivets in range(18, 25):
            color = "white"
        if rivets in range(26, 36):
            color = "green"
        if rivets in range(38,43):
            color = "green"
            striped = True
        if rivets in range(44,50):
            color = "white"
            striped = True
        if rivets == 36:
            stars = True
        if rivets in range(37, 50):
            card = 2

        return (self.pos[rivets], card, corners, color, stars, striped)
    
    def scan_all(self):
        #Animate scanning of everything - this happens through the spotting disc
        self.all_probability()

    def all_probability(self):
        if self.game.red_odds.position < 3:
            self.game.red_odds.step()
        if self.game.white_odds.position < 3:
            self.game.white_odds.step()
        if self.game.green_odds.position < 3:
            self.game.green_odds.step()
        if self.game.yellow_odds.position < 3:
            self.game.yellow_odds.step()
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
        if self.game.red_odds.position < 3:
            return
        if self.game.green_odds.position < 3:
            return
        if self.game.yellow_odds.position < 3:
            return
        if self.game.white_odds.position < 3:
            return
        s = random.randint(1,5)
        self.animate_odds_scan(s)
        p = self.odds_probability()
        if "red" in p:
            m = self.check_mixer3("red")
            if m == 1:
                es = self.check_extra_step()
                if es == 1:
                    i = random.randint(1,5)
                    self.red_extra_step(i)
                else:
                    self.game.red_odds.step()
        if "green" in p:
            m = self.check_mixer3("green")
            if m == 1:
                es = self.check_extra_step()
                if es == 1:
                    i = random.randint(1,5)
                    self.green_extra_step(i)
                else:
                    self.game.green_odds.step()
        if "yellow" in p:
            m = self.check_mixer3("yellow")
            if m == 1:
                es = self.check_extra_step()
                if es == 1:
                    i = random.randint(1,5)
                    self.yellow_extra_step(i)
                else:
                    self.game.yellow_odds.step()
        if "white" in p:
            m = self.check_mixer3("white")
            if m == 1:
                es = self.check_extra_step()
                if es == 1:
                    i = random.randint(1,5)
                    self.white_extra_step(i)
                else:
                    self.game.white_odds.step()

    def check_mixer3(self, color):
        m3 = self.game.mixer3.position
        if color == "yellow":
            if m3 == 2 or m3 == 5 or m3 == 11 or m3 == 14 or m3 == 17 or m3 == 23:
                return 1
        if color == "red":
            if m3 == 6 or m3 == 8 or m3 == 12 or m3 == 1 or m3 == 18 or m3 == 24:
                return 1
        if color == "white":
            if m3 == 1 or m3 == 13 or m3 == 9 or m3 == 22:
                return 1
        if color == "green":
            if m3 == 3 or m3 == 15 or m3 == 4 or m3 == 16 or m3 == 7 or m3 == 20 or m3 == 10 or m3 == 22:
                return 1

    def red_extra_step(self, number):
        if number > 0:
            self.game.red_odds.step()
            self.delay(name="display", delay=0, handler=graphics.miss_america_deluxe.display, param=self)
            number -= 1
            self.delay(name="red_extra_step", delay=0.1, handler=self.red_extra_step, param=number)
            
    def green_extra_step(self, number):
        if number > 0:
            self.game.green_odds.step()
            self.delay(name="display", delay=0, handler=graphics.miss_america_deluxe.display, param=self)
            number -= 1
            self.delay(name="green_extra_step", delay=0.1, handler=self.green_extra_step, param=number)

    def yellow_extra_step(self, number):
        if number > 0:
            self.game.yellow_odds.step()
            self.delay(name="display", delay=0, handler=graphics.miss_america_deluxe.display, param=self)
            number -= 1
            self.delay(name="yellow_extra_step", delay=0.1, handler=self.yellow_extra_step, param=number)

    def white_extra_step(self, number):
        if number > 0:
            self.game.white_odds.step()
            self.delay(name="display", delay=0, handler=graphics.miss_america_deluxe.display, param=self)
            number -= 1
            self.delay(name="white_extra_step", delay=0.1, handler=self.white_extra_step, param=number)

    def check_extra_step(self):
        i = random.randint(0,32)
        if i == 16:
            return 1
        else:
            return 0

    def odds_probability(self):
        if self.game.red_odds.position == 1:
            return ["red"]
        if self.game.yellow_odds.position == 1:
            return ["yellow"]
        if self.game.green_odds.position == 1:
            return ["green"]
        if self.game.white_odds.position == 1:
            return ["white"]
        else:
            sd = self.game.spotting.position
            if self.game.red_odds.position < 4:
                return ["red", "yellow", "white"]
            if self.game.green_odds.position == 6:
                return ["green"]
            if self.game.red_odds.position == 4 or self.game.yellow_odds.position == 4 or self.game.white_odds.position == 4:
                if sd != 0 and sd != 4 and sd != 10 and sd != 11 and sd != 15 and sd != 16 and sd != 20 and sd not in range(22,28) and sd not in range (30,33) and sd not in range(38,41) and sd != 45 and sd != 46 and sd != 49:
                    return ["red", "yellow", "white"]
            if self.game.green_odds.position == 5:
                if sd != 0 and sd != 4 and sd != 10 and sd != 11 and sd != 15 and sd != 16 and sd != 20 and sd not in range(22,28) and sd not in range (30,33) and sd not in range(38,41) and sd != 45 and sd != 46 and sd != 49:
                    return ["green"]
            if self.game.red_odds.position == 5 or self.game.yellow_odds.position == 5 or self.game.white_odds.position == 5:
                if sd == 2 or sd == 10 or sd == 11 or sd == 12 or sd == 17 or sd == 18 or sd == 19 or sd == 23 or sd == 26 or sd == 27 or sd == 28 or sd == 31 or sd == 32 or sd == 38 or sd == 39 or sd == 43 or sd == 44:
                    return ["red", "yellow", "white"]
            if self.game.green_odds.position == 4:
                if sd == 2 or sd == 10 or sd == 11 or sd == 12 or sd == 17 or sd == 18 or sd == 19 or sd == 23 or sd == 26 or sd == 27 or sd == 28 or sd == 31 or sd == 32 or sd == 38 or sd == 39 or sd == 43 or sd == 44:
                    return ["green"]
            if self.game.red_odds.position == 6 or self.game.yellow_odds.position == 6 or self.game.white_odds.position == 6:
                if sd == 2 or sd == 7 or sd == 14 or sd == 18 or sd == 43 or sd == 44:
                    return ["red", "yellow", "white"]
            if self.game.green_odds.position == 3:
                if sd == 2 or sd == 7 or sd == 14 or sd == 18 or sd == 43 or sd == 44:
                    return ["green"]
            return [0]

    def scan_features(self):
        p = self.features_probability()

    def features_probability(self):
        s = random.randint(1,6)
        self.animate_feature_scan(s)
        sd = self.game.spotting.position

        if self.game.selection_feature.position == 0:
            self.game.selection_feature.step()
        else:
            if sd == 2 or sd == 5 or sd == 8 or sd == 13 or sd == 21 or sd == 22 or sd == 25 or sd == 35 or sd == 37 or sd == 42:
                self.step_selection(6 - self.game.selection_feature.position)
            elif sd == 7 or sd == 20 or sd == 24:
                if self.game.selection_feature.position >= 6:
                    if self.game.cu or self.game.corners.status == False:
                        self.step_selection(9 - self.game.selection_feature.position)
            elif sd == 0 or (sd == 23 and self.game.reflex.connected_rivet() == 4):
                self.step_selection(9 - self.game.selection_feature.position)
            else:
                m4 = self.check_mixer4()
                if m4 == 1:
                    self.game.selection_feature.step()
        
        if sd == 1 or sd == 6 or sd == 15 or sd == 29 or sd == 40 or sd == 41 or sd == 46 or sd == 47 or sd == 49:
            self.game.selector.step()
        if sd == 11 or sd == 12 or sd == 18 or sd == 19:
            if self.game.before_fifth.status == False:
                if self.game.rollovers.status == False:
                    if self.game.cu:
                        self.game.coils.redROLamp.enable()
                    else:
                        self.game.coils.yellowROLamp.enable()
                self.game.rollovers.engage(self.game)

        if sd == 12:
            if self.game.selection_feature.position < 9 or self.game.cu:
                self.game.corners.engage(self.game)
        if sd == 8:
            if self.game.rollovers.status == False:
                self.game.before_fourth.disengage()
                self.game.before_fifth.engage(self.game)
        if sd == 3 or sd == 4 or sd == 6 or sd in range(8,13) or sd in range(16,20) or sd == 22 or sd == 23 or sd == 26 or sd == 27 or sd in range(29,35) or sd == 37 or sd == 38 or sd == 39 or sd in range(42,45) or sd == 46:
            if self.game.cu:
                self.game.red_letter_three.disengage()
                self.game.red_letter_two.engage(self.game)
        if sd == 3 or sd == 4 or sd in range(10,13) or sd in range(17,20) or sd == 23 or sd == 26 or sd == 27 or sd == 31 or sd == 32 or sd == 34 or sd == 38 or sd == 39 or sd == 43 or sd == 44:
            if self.game.red_letter_two.status == False:
                self.game.red_letter_three.engage(self.game)
        if sd == 12 or sd == 24 or sd == 38 or sd == 39:
            self.game.green_corners.engage(self.game)
        if sd == 4 or sd == 22 or sd == 37:
            self.game.striped_diagonals.engage(self.game)

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
    
    def step_selection(self, number):
        if number >= 1:
            self.game.selection_feature.step()
            number -= 1
            self.delay(name="display", delay=0.1, handler=graphics.miss_america_deluxe.display, param=self)
            self.delay(name="step_selection", delay=0.1, handler=self.step_selection, param=number)

   
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
        self.delay(name="display", delay=0.1, handler=graphics.miss_america_deluxe.display, param=self)

    def animate_odds_scan(self, s):
        if s > 1:
            self.delay(name="odds_animation", delay=0, handler=graphics.miss_america_deluxe.odds_animation, param=s)
            self.delay(name="display", delay=0.1, handler=graphics.miss_america_deluxe.display, param=self)
            s -= 1
            #self.delay(name="animate_odds", delay=0.1, handler=self.animate_odds_scan, param=s)
        else:
            self.delay(name="display", delay=0.1, handler=graphics.miss_america_deluxe.display, param=self)

    def animate_feature_scan(self, s):
        if s > 1:
            self.delay(name="feature_animation", delay=0.1, handler=graphics.miss_america_deluxe.feature_animation, param=s)
            self.delay(name="display", delay=0.1, handler=graphics.miss_america_deluxe.display, param=self)
            s -= 1
            #self.delay(name="animate_feature", delay=0.1, handler=self.animate_feature_scan, param=s)
        else:
            self.delay(name="display", delay=0.1, handler=graphics.miss_america_deluxe.display, param=self)

    def animate_eb_scan(self, s):
        if s > 1:
            self.delay(name="eb_animation", delay=0.1, handler=graphics.miss_america_deluxe.eb_animation, param=s)
            self.delay(name="display", delay=0.1, handler=graphics.miss_america_deluxe.display, param=self)
            s -= 1
            #self.delay(name="animate_eb", delay=0.1, handler=self.animate_eb_scan, param=s)
        else:
            self.delay(name="display", delay=0.1, handler=graphics.miss_america_deluxe.display, param=self)

    def eb_probability(self):
        mix1 = self.game.mixer1.connected_rivet()
        if self.game.reflex.connected_rivet() == 0 and (mix1 == 1 or mix1 == 9 or mix1 == 15):
            if self.game.spotting.position == 1:
                if self.game.cu:
                    self.step_eb(1)
                else:
                    self.step_eb(6 - self.game.extra_ball.position)
                if self.game.mixer3.position == 23:
                    self.step_eb(9 - self.game.extra_ball.position) 
            if self.game.spotting.position == 50:
                if self.game.mixer3.position == 24:
                    self.step_eb(3 - self.game.extra_ball.position)

    def step_eb(self, number):
        if number >= 1:
            self.game.extra_ball.step()
            self.check_lifter_status()
            number -= 1
            self.delay(name="display", delay=0.1, handler=graphics.miss_america_deluxe.display, param=self)
            self.delay(name="step_eb", delay=0.1, handler=self.step_eb, param=number)

    def blink_title(self):
        title1 = random.randint(0,1)
        title2 = random.randint(0,1)
        title3 = random.randint(0,1)
        title4 = random.randint(0,1)
        if title1 == 1:
            pos = [167,257]
            image = pygame.image.load('miss_america_deluxe/assets/title1_on.png').convert_alpha()
            screen.blit(image, pos)
        if title2 == 1:
            pos = [241,290]
            image = pygame.image.load('miss_america_deluxe/assets/title2_on.png').convert_alpha()
            screen.blit(image, pos)
        if title3 == 1:
            pos = [346,298]
            image = pygame.image.load('miss_america_deluxe/assets/title3_on.png').convert_alpha()
            screen.blit(image, pos)
        if title4 == 1:
            pos = [431,264]
            image = pygame.image.load('miss_america_deluxe/assets/title4_on.png').convert_alpha()
            screen.blit(image, pos)
            
        pygame.display.update()
        self.delay(name="display", delay=0.1, handler=graphics.miss_america_deluxe.display, param=self)
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


class MissAmericaDeluxe(procgame.game.BasicGame):
    """ Palm Beach was the first game with Super Cards """
    def __init__(self, machine_type):
        super(MissAmericaDeluxe, self).__init__(machine_type)
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

        self.lockout = units.Relay("lockout")
        self.before_fourth = units.Relay("before_fourth")
        self.before_fifth = units.Relay("before_fifth")
        self.rollovers = units.Relay("rollovers")

        self.red_odds = units.Stepper("red_odds", 7)
        self.yellow_odds = units.Stepper("yellow_odds", 7)
        self.green_odds = units.Stepper("green_odds", 7)
        self.white_odds = units.Stepper("white_odds", 7)

        #Replay Counter
        self.red_replay_counter = units.Stepper("red_replay_counter", 600)
        self.green_replay_counter = units.Stepper("green_replay_counter", 600)
        self.yellow_replay_counter = units.Stepper("yellow_replay_counter", 600)
        self.white_replay_counter = units.Stepper("white_replay_counter", 600)

        self.red_letter_two = units.Relay("red_letter_two")
        self.red_letter_three = units.Relay("red_letter_three")

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
        self.green_corners = units.Relay("green_corners")
        self.striped_diagonals = units.Relay("striped_diagonals")
        self.selector = units.Stepper("selector", 2)

        # Select-a-spot setup
        self.selection_feature = units.Stepper("selection_feature", 9)
        self.line1 = units.Stepper("line1", 3, "miss_america_deluxe", "continuous")
        self.line2 = units.Stepper("line2", 3, "miss_america_deluxe", "continuous")
        self.line3 = units.Stepper("line3", 3, "miss_america_deluxe", "continuous")
        self.line4 = units.Stepper("line4", 3, "miss_america_deluxe", "continuous")
        self.line5 = units.Stepper("line5", 3, "miss_america_deluxe", "continuous")

        self.rollover = units.Relay("rollover")

        self.replays = 0
        self.returned = False

    def reset(self):
        super(MissAmericaDeluxe, self).reset()
        self.logger = logging.getLogger('game')
        self.load_config('bingo.yaml')
        
        main_mode = SinglecardBingo(self)
        self.modes.add(main_mode)
        
game = MissAmericaDeluxe(machine_type='pdb')
game.reset()
game.run_loop()
