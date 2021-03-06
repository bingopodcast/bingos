#!/usr/bin/python

import logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
import procgame.game, sys, os
import procgame.config
import random
import procgame.sound
import pygame

sys.path.insert(0,os.path.pardir)
import bingo_emulator.common.units as units
import bingo_emulator.common.functions as functions
from bingo_emulator.graphics import methods as graphics
from bingo_emulator.graphics.the_twist import *

class SinglecardBingo(procgame.game.Mode):
    def __init__(self, game):
        super(SinglecardBingo, self).__init__(game=game, priority=5)
        self.holes = []
        self.startup()
        self.game.sound.register_music('motor', "audio/magic_screen_control_unit.wav")
        self.game.sound.register_sound('search', "audio/magic_screen_search_default.wav")
        self.game.sound.register_sound('search_screen', "audio/magic_screen_search.wav")
        self.game.sound.register_sound('coin1', "audio/magic_screen_coin1.wav")
        self.game.sound.register_sound('coin2', "audio/magic_screen_coin2.wav")
        self.game.sound.register_sound('coin3', "audio/magic_screen_coin3.wav")
        self.game.sound.register_sound('magic_screen', "audio/magic_screen.wav")
        self.game.sound.register_sound('tilt', "audio/tilt.wav")
        self.game.sound.register_sound('step', "audio/step.wav")
        self.game.sound.register_sound('eb_search', "audio/EB_Search.wav")

    def sw_coin_active(self, sw):
        if self.game.eb_play.status == False:
            self.game.tilt.disengage()
            self.regular_play()
        else:
            self.cancel_delayed("eb_animation")
            self.game.sound.play('eb_search')
            if self.game.timer.position >= 8:
                self.game.timer.reset()
                self.game.sound.play_music('motor', -1)
                self.timeout_actions()
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
            self.animate_eb_scan([begin,self.game.spotting.movement_amount,self.game.spotting.movement_amount])

        self.delay(name="display", delay=0.1, handler=graphics.the_twist.display, param=self)

    def sw_startButton_active(self, sw):
        self.cancel_delayed(name="both_animation")
        self.cancel_delayed(name="blink_letter")
        self.cancel_delayed(name="blink_time")
        self.cancel_delayed(name="blink")
        self.game.eb_play.disengage()
        self.delay(name="display", delay=0.1, handler=graphics.the_twist.display, param=self)
        if self.game.replays > 0 or self.game.switches.freeplay.is_active():
            self.game.tilt.disengage()
            self.regular_play()
            self.cancel_delayed(name="display")
            self.delay(name="display", delay=0.1, handler=graphics.the_twist.display, param=self)

    def sw_enter_active(self, sw):
        if self.game.switches.left.is_active() and self.game.switches.right.is_active():
            self.game.end_run_loop()
            os.system("/home/nbaldridge/proc/bingo_emulator/start_game.sh the_twist")
        else:
            if self.game.ball_count.position >= 4:
                self.cancel_delayed(name="blink_letter")
                graphics.the_twist.blink_letter([self,1,self.game.magic_screen.position])
                self.game.sound.stop_music()
                self.game.sound.play_music('motor', -1)
                self.game.timer.reset()
                if self.game.search_index.status == False:
                    self.search()
                    self.timeout_actions()


    def sw_trough4_active_for_1s(self, sw):
        if self.game.ball_count.position >= 4:
            self.timeout_actions()
    
    def timeout_actions(self):
        if (self.game.timer.position < 7):
            self.game.timer.step()
            self.delay(name="timeout", delay=5.0, handler=self.timeout_actions)
        else:
            self.game.timer.step()
            self.cancel_delayed(name="blink_letter")
            self.cancel_delayed(name="blink_time")
            self.cancel_delayed(name="blink")
            self.game.sound.stop_music()

    def sw_trough8_closed(self, sw):
        if self.game.start.status == False:
            if self.game.ball_count.position >= 5:
                self.game.returned = True
            self.game.ball_count.position -= 1
            self.check_lifter_status()
        else:
            self.check_lifter_status()

    def sw_right_active(self, sw):
        if self.game.ball_count.position > 0:
            self.cancel_delayed("blink_letter")
            self.cancel_delayed(name="blink_time")
            max_ball = 0
            if self.game.before_fourth.status == True:
                max_ball = 4
            elif self.game.before_fifth.status == True:
                max_ball = 5
            msu = self.game.magic_card.position

            if self.game.ball_count.position < max_ball:
                if self.game.magic_screen.position > 0:
                    self.game.sound.play('magic_screen')
                    self.game.magic_screen.stepdown()
                    self.cancel_delayed("left_animation")
                    self.cancel_delayed("right_animation")
                    self.animate_screen_right([self.game,47])
                            
            graphics.the_twist.blink_letter([self,1,self.game.magic_screen.position])
            self.delay(name="display", delay=0.1, handler=graphics.the_twist.display, param=self)

    def sw_right_active_for_500ms(self,sw):
        if self.game.ball_count.position > 0:
            self.cancel_delayed("blink_letter")
            max_ball = 0
            if self.game.before_fourth.status == True:
                max_ball = 4
            elif self.game.before_fifth.status == True:
                max_ball = 5
            msu = self.game.magic_card.position

            if self.game.ball_count.position < max_ball:
                if self.game.magic_screen.position > 0:
                    self.game.sound.play('magic_screen')
                    self.game.magic_screen.stepdown()
                    self.cancel_delayed("left_animation")
                    self.cancel_delayed("right_animation")
                    self.animate_screen_right([self.game,47])
                            
            graphics.the_twist.blink_letter([self,1,self.game.magic_screen.position])
            self.delay(name="display", delay=0.1, handler=graphics.the_twist.display, param=self)
            self.delay(name="right", delay=0.5, handler=self.sw_right_active_for_500ms, param=sw)

    def sw_left_active(self, sw):
        if self.game.ball_count.position > 0:
            self.cancel_delayed("blink_letter")
            max_ball = 0
            if self.game.before_fourth.status == True:
                max_ball = 4
            elif self.game.before_fifth.status == True:
                max_ball = 5
            msu = self.game.magic_card.position
            max_position = msu

            if self.game.ball_count.position < max_ball:
                if self.game.magic_screen.position < max_position:
                    self.game.sound.play('magic_screen')
                    self.game.magic_screen.step()
                    self.cancel_delayed("left_animation")
                    self.cancel_delayed("right_animation")
                    self.animate_screen_left([self.game,47])
            graphics.the_twist.blink_letter([self,1,self.game.magic_screen.position])
            self.delay(name="display", delay=0.1, handler=graphics.the_twist.display, param=self)

    def sw_left_active_for_500ms(self,sw):
        if self.game.ball_count.position > 0:
            self.cancel_delayed("blink_letter")
            max_ball = 0
            if self.game.before_fourth.status == True:
                max_ball = 4
            elif self.game.before_fifth.status == True:
                max_ball = 5
            msu = self.game.magic_card.position
            max_position = msu

            if self.game.ball_count.position < max_ball:
                if self.game.magic_screen.position < max_position:
                    self.game.sound.play('magic_screen')
                    self.game.magic_screen.step()
                    self.cancel_delayed("left_animation")
                    self.cancel_delayed("right_animation")
                    self.animate_screen_left([self.game,47])
            graphics.the_twist.blink_letter([self,1,self.game.magic_screen.position])
            self.delay(name="display", delay=0.1, handler=graphics.the_twist.display, param=self)
            self.delay(name="left", delay=0.5, handler=self.sw_left_active_for_500ms, param=sw)

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
        self.cancel_delayed(name="red_replay_step_up")
        self.cancel_delayed(name="yellow_replay_step_up")
        self.cancel_delayed(name="green_replay_step_up")
        self.cancel_delayed(name="both_animation")
        self.cancel_delayed(name="blink_letter")
        self.cancel_delayed(name="blink_time")
        self.cancel_delayed(name="blink")
        self.cancel_delayed(name="timeout")
        r = random.randint(1,3)
        if r == 1:
            self.game.sound.play('coin1')
        elif r == 2:
            self.game.sound.play('coin2')
        elif r == 3:
            self.game.sound.play('coin3')
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
            if self.game.selector.position < 1:
                self.game.selector.step()
            if self.game.switches.shutter.is_inactive():
                self.game.coils.shutter.enable()
            self.replay_step_down()
            graphics.the_twist.display(self)
            self.check_lifter_status()
        else:
            self.holes = []
            self.game.start.engage(self.game)
            self.game.red_replay_counter.reset()
            self.game.yellow_replay_counter.reset()
            self.game.green_replay_counter.reset()
            self.game.red_odds.reset()
            self.game.yellow_odds.reset()
            self.game.green_odds.reset()
            self.game.start.engage(self.game)
            self.game.selector.reset()
            self.game.ball_count.reset()
            self.game.extra_ball.reset()
            self.game.timer.reset()
            self.game.advance_green.disengage()
            self.game.advance_red.disengage()
            self.game.advance_yellow.disengage()
            self.game.advance_card.disengage()
            if self.game.magic_screen.position > 0:
                self.magic_screen_reset(self.game.magic_screen.position)
            if self.game.magic_screen.position < 0:
                self.magic_screen_reset_up(self.game.magic_screen.position)
            self.game.magic_card.reset()
            self.game.before_fourth.disengage()
            self.game.before_fifth.disengage()
            
            self.game.sound.play_music('motor', -1)
            self.regular_play()
        self.delay(name="display", delay=0.1, handler=graphics.the_twist.display, param=self)
        self.game.tilt.disengage()

    def magic_screen_reset_up(self, number):
        if number != 2:
            self.game.sound.play('magic_screen')
            self.game.magic_screen.step()
            self.cancel_delayed("left_animation")
            self.cancel_delayed("right_animation")
            self.animate_screen_left([self.game,47])
            self.delay(name="display", delay=0, handler=graphics.the_twist.display, param=self)
            number += 1
            self.delay(name="magic_screen_reset_up", delay=0.3, handler=self.magic_screen_reset_up, param=number)

    def magic_screen_reset(self, number):
        if number > 0:
            self.game.sound.play('magic_screen')
            self.game.magic_screen.stepdown()
            self.cancel_delayed("left_animation")
            self.cancel_delayed("right_animation")
            self.animate_screen_right([self.game,47])
            self.delay(name="display", delay=0, handler=graphics.the_twist.display, param=self)
            number -= 1
            self.delay(name="magic_screen_reset", delay=0.3, handler=self.magic_screen_reset, param=number)

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
                elif self.game.ball_count.position == 5 and self.game.extra_ball.position >= 3:
                    self.game.coils.lifter.enable()
                elif self.game.ball_count.position == 6 and self.game.extra_ball.position >= 6:
                    self.game.coils.lifter.enable()
                else:
                    if self.game.ball_count.position == 7 and self.game.extra_ball.position >= 9:
                        self.game.coils.lifter.enable()

    def sw_gate_inactive_for_1ms(self, sw):
        self.game.start.disengage()
        self.game.ball_count.step()
        if self.game.ball_count.position == 1:
            graphics.the_twist.blink_letter([self,1,self.game.magic_screen.position])
        if self.game.switches.shutter.is_active():
            self.game.coils.shutter.enable()
        if self.game.ball_count.position == 4:
            self.game.sound.play('tilt')
            self.game.sound.play('tilt')
        if self.game.ball_count.position >= 4:
            self.game.coils.yellowROLamp.disable()
        if self.game.ball_count.position >= 5:
            self.game.coils.redROLamp.disable()
        if self.game.ball_count.position <= 7:
            self.check_lifter_status()
        self.delay(name="display", delay=0.1, handler=graphics.the_twist.display, param=self)


    # This is really nasty, but it is how we render graphics for each individual hole.
    # numbers are added (or removed from) a list.  In this way, I can re-use the same
    # routine even for games where there are ball return functions like Surf Club.

    def sw_hole1_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(1)
            self.delay(name="display", delay=0.1, handler=graphics.the_twist.display, param=self)

    def sw_hole2_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(2)
            self.delay(name="display", delay=0.1, handler=graphics.the_twist.display, param=self)

    def sw_hole3_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(3)
            self.delay(name="display", delay=0.1, handler=graphics.the_twist.display, param=self)

    def sw_hole4_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(4)
            self.delay(name="display", delay=0.1, handler=graphics.the_twist.display, param=self)

    def sw_hole5_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(5)
            self.delay(name="display", delay=0.1, handler=graphics.the_twist.display, param=self)

    def sw_hole6_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(6)
            self.delay(name="display", delay=0.1, handler=graphics.the_twist.display, param=self)

    def sw_hole7_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(7)
            self.delay(name="display", delay=0.1, handler=graphics.the_twist.display, param=self)

    def sw_hole8_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(8)
            self.delay(name="display", delay=0.1, handler=graphics.the_twist.display, param=self)

    def sw_hole9_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(9)
            self.delay(name="display", delay=0.1, handler=graphics.the_twist.display, param=self)

    def sw_hole10_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(10)
            self.delay(name="display", delay=0.1, handler=graphics.the_twist.display, param=self)

    def sw_hole11_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(11)
            self.delay(name="display", delay=0.1, handler=graphics.the_twist.display, param=self)

    def sw_hole12_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(12)
            self.delay(name="display", delay=0.1, handler=graphics.the_twist.display, param=self)

    def sw_hole13_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(13)
            self.delay(name="display", delay=0.1, handler=graphics.the_twist.display, param=self)

    def sw_hole14_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(14)
            self.delay(name="display", delay=0.1, handler=graphics.the_twist.display, param=self)

    def sw_hole15_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(15)
            self.delay(name="display", delay=0.1, handler=graphics.the_twist.display, param=self)

    def sw_hole16_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(16)
            self.delay(name="display", delay=0.1, handler=graphics.the_twist.display, param=self)

    def sw_hole17_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(17)
            self.delay(name="display", delay=0.1, handler=graphics.the_twist.display, param=self)

    def sw_hole18_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(18)
            self.delay(name="display", delay=0.1, handler=graphics.the_twist.display, param=self)

    def sw_hole19_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(19)
            self.delay(name="display", delay=0.1, handler=graphics.the_twist.display, param=self)

    def sw_hole20_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(20)
            self.delay(name="display", delay=0.1, handler=graphics.the_twist.display, param=self)

    def sw_hole21_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(21)
            self.delay(name="display", delay=0.1, handler=graphics.the_twist.display, param=self)

    def sw_hole22_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(22)
            self.delay(name="display", delay=0.1, handler=graphics.the_twist.display, param=self)

    def sw_hole23_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(23)
            self.delay(name="display", delay=0.1, handler=graphics.the_twist.display, param=self)

    def sw_hole24_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(24)
            self.delay(name="display", delay=0.1, handler=graphics.the_twist.display, param=self)

    def sw_hole25_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(25)
            self.delay(name="display", delay=0.1, handler=graphics.the_twist.display, param=self)

    def sw_replayReset_active(self, sw):
        self.game.anti_cheat.disengage()
        self.holes = []
        graphics.the_twist.display(self)
        self.tilt_actions()
        self.replay_step_down(self.game.replays)

    def sw_redstar_active(self, sw):
        if self.game.red_star.status == True:
            if self.game.selection_feature.position < 8:
                self.game.selection_feature.position = 8
                self.game.red_star.disengage()
                self.game.coils.redROLamp.disable()
            self.delay(name="display", delay=0.1, handler=graphics.the_twist.display, param=self)

    def sw_yellowstar_active(self, sw):
        if self.game.yellow_star.status == True:
            if self.game.selection_feature.position < 7:
                self.game.selection_feature.position = 7
                self.game.yellow_star.disengage()
                self.game.coils.yellowROLamp.disable()
            self.delay(name="display", delay=0.1, handler=graphics.the_twist.display, param=self)

    def tilt_actions(self):
        self.game.start.disengage()
        self.cancel_delayed(name="replay_reset")
        self.cancel_delayed(name="red_replay_step_up")
        self.cancel_delayed(name="yellow_replay_step_up")
        self.cancel_delayed(name="green_replay_step_up")
        self.cancel_delayed(name="blink_letter")
        self.cancel_delayed(name="blink_time")
        self.cancel_delayed(name="blink")
        self.cancel_delayed(name="timeout")
        self.game.eb_play.disengage()
        self.game.search_index.disengage()
        if self.game.ball_count.position == 0:
            if self.game.switches.shutter.is_active():
                self.game.coils.shutter.enable()
        self.holes = []
        self.game.selector.reset()
        self.game.red_replay_counter.reset()
        self.game.yellow_replay_counter.reset()
        self.game.green_replay_counter.reset()
        self.game.magic_card.reset()
        self.game.before_fourth.disengage()
        self.game.before_fifth.disengage()
        self.game.ball_count.reset()
        self.game.red_odds.reset()
        self.game.yellow_odds.reset()
        self.game.green_odds.reset()
        self.game.advance_green.disengage()
        self.game.advance_red.disengage()
        self.game.advance_yellow.disengage()
        self.game.advance_card.disengage()
        self.game.eb_play.disengage()
        self.game.extra_ball.reset()
        self.game.anti_cheat.engage(game)
        self.game.tilt.engage(self.game)
        self.game.sound.stop_music()
        self.game.sound.play('tilt')
        # displays "Tilt" on the backglass, you have to recoin.
        self.delay(name="display", delay=0.1, handler=graphics.the_twist.display, param=self)

    def sw_tilt_active(self, sw):
        if self.game.tilt.status == False:
            self.tilt_actions()

    def replay_step_down(self, number=0):
        if number > 0:
            if number > 1:
                self.game.replays -= 1
                graphics.replay_step_down(self.game.replays, graphics.the_twist.reel1, graphics.the_twist.reel10, graphics.the_twist.reel100)
                self.game.coils.registerDown.pulse()
                number -= 1
                self.delay(name="display", delay=0, handler=graphics.the_twist.display, param=self)
                self.delay(name="replay_reset", delay=0.13, handler=self.replay_step_down, param=number)
            elif number == 1:
                self.game.replays -= 1
                graphics.replay_step_down(self.game.replays, graphics.the_twist.reel1, graphics.the_twist.reel10, graphics.the_twist.reel100)
                self.game.coils.registerDown.pulse()
                number -= 1
                self.delay(name="display", delay=0, handler=graphics.the_twist.display, param=self)
                self.cancel_delayed(name="replay_reset")
        else: 
            if self.game.replays > 0:
                self.game.replays -= 1
                graphics.replay_step_down(self.game.replays, graphics.the_twist.reel1, graphics.the_twist.reel10, graphics.the_twist.reel100)
                self.delay(name="display", delay=0.1, handler=graphics.the_twist.display, param=self)
            self.game.coils.registerDown.pulse()

    def replay_step_up(self):
        if self.game.replays < 899:
            self.game.replays += 1
            graphics.replay_step_up(self.game.replays, graphics.the_twist.reel1, graphics.the_twist.reel10, graphics.the_twist.reel100)
        self.game.coils.registerUp.pulse()
        self.game.reflex.increase()
        graphics.the_twist.display(self)

    def sw_yellow_active(self, sw):
        if self.game.ball_count.position >= 4:
            if self.game.eb_play.status == True and (self.game.replays > 0 or self.game.switches.freeplay.is_active()):
                self.cancel_delayed("eb_animation")
                self.game.sound.play('eb_search')
                if self.game.timer.position >= 8:
                    self.game.timer.reset()
                    self.game.sound.play_music('motor', -1)
                    self.timeout_actions()
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
                graphics.the_twist.display(self)
                self.animate_eb_scan([begin,self.game.spotting.movement_amount,self.game.spotting.movement_amount])
                self.delay(name="display", delay=0.1, handler=graphics.the_twist.display, param=self)
                return
            if self.game.eb_play.status == False:
                self.game.eb_play.engage(self.game)
                self.delay(name="display", delay=0.1, handler=graphics.the_twist.display, param=self)
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
        self.game.sound.play('search')
       
        if self.game.magic_screen.position <= 10:
            for i in range(0, 13):
                self.r = self.closed_search_relays(self.game.searchdisc.position)
                self.game.searchdisc.spin()
                self.wipers = self.r[0]
                self.red = self.r[1]
                self.yellow = self.r[2]
                self.green = self.r[3]
                self.rivets = self.r[4]

                # From here, I need to determine based on the value of r, whether to latch the search index and score. 
                # I need to determine the best winner on each card.  To do this, I must compare the position of the replay counter before
                # determining the winner. Reminder that my replay counters are a 1:1 representation.

                self.match = []
                for key in self.wipers:
                    for number in self.holes:
                        if number == key:
                            self.match.append(self.wipers[key])
                            relays = sorted(set(self.match))
                            if self.game.magic_screen.position == 1:
                                if self.red == True:
                                    if self.rivets == 1:
                                        if 3 in self.holes:
                                            if 1 not in relays:
                                                relays.append(1)
                                            if 5 not in relays:
                                                relays.append(5)
                            if self.game.magic_screen.position == 2:
                                if self.green == True:
                                    if self.rivets == 11:
                                        if 25 in self.holes:
                                            if 3 not in relays:
                                                relays.append(3)
                                            if 5 not in relays:
                                                relays.append(5)
                            if self.game.magic_screen.position == 3:
                                if self.green == True:
                                    if self.rivets == 12:
                                        if 1 in self.holes:
                                            if 2 not in relays:
                                                relays.append(2)
                                            if 5 not in relays:
                                                relays.append(5)
                            if self.game.magic_screen.position == 7:
                                if self.green == True:
                                    if self.rivets == 12:
                                        if 21 in self.holes:
                                            if 2 not in relays:
                                                relays.append(2)
                                            if 5 not in relays:
                                                relays.append(5)
                            relays = sorted(relays)
                            #TODO Play sound for each relay closure.
                            s = functions.count_seq(relays)
                            if s >= 3:
                                self.find_winner(s, self.red, self.yellow, self.green)
                                break


    # THIS NEEDS TO BE CALLED IF THE SCREEN IF OUT OF INDEX POSITION

    def find_winner(self, relays, red, yellow, green):
        if self.game.search_index.status == False and self.game.replays < 899:
            if self.game.red_odds.position == 1:
                redthreeodds = 4
                redfourodds = 12
                redfiveodds = 60
            elif self.game.red_odds.position == 2:
                redthreeodds = 4
                redfourodds = 16
                redfiveodds = 72
            elif self.game.red_odds.position == 3:
                redthreeodds = 6
                redfourodds = 24
                redfiveodds = 96
            elif self.game.red_odds.position == 4:
                redthreeodds = 8
                redfourodds = 32
                redfiveodds = 128
            elif self.game.red_odds.position == 5:
                redthreeodds = 12
                redfourodds = 36
                redfiveodds = 144
            elif self.game.red_odds.position == 6:
                redthreeodds = 16
                redfourodds = 48
                redfiveodds = 192
            elif self.game.red_odds.position == 7:
                redthreeodds = 20
                redfourodds = 60
                redfiveodds = 240
            elif self.game.red_odds.position == 8:
                redthreeodds = 24
                redfourodds = 72
                redfiveodds = 360
            elif self.game.red_odds.position == 9:
                redthreeodds = 30
                redfourodds = 96
                redfiveodds = 480
            elif self.game.red_odds.position == 10:
                redthreeodds = 36
                redfourodds = 120
                redfiveodds = 600
            if self.game.yellow_odds.position == 1:
                yellowthreeodds = 4
                yellowfourodds = 12
                yellowfiveodds = 60
            elif self.game.yellow_odds.position == 2:
                yellowthreeodds = 4
                yellowfourodds = 16
                yellowfiveodds = 72
            elif self.game.yellow_odds.position == 3:
                yellowthreeodds = 6
                yellowfourodds = 24
                yellowfiveodds = 96
            elif self.game.yellow_odds.position == 4:
                yellowthreeodds = 8
                yellowfourodds = 32
                yellowfiveodds = 128
            elif self.game.yellow_odds.position == 5:
                yellowthreeodds = 12
                yellowfourodds = 36
                yellowfiveodds = 144
            elif self.game.yellow_odds.position == 6:
                yellowthreeodds = 16
                yellowfourodds = 48
                yellowfiveodds = 192
            elif self.game.yellow_odds.position == 7:
                yellowthreeodds = 20
                yellowfourodds = 60
                yellowfiveodds = 240
            elif self.game.yellow_odds.position == 8:
                yellowthreeodds = 24
                yellowfourodds = 72
                yellowfiveodds = 360
            elif self.game.yellow_odds.position == 9:
                yellowthreeodds = 30
                yellowfourodds = 96
                yellowfiveodds = 480
            elif self.game.yellow_odds.position == 10:
                yellowthreeodds = 36
                yellowfourodds = 120
                yellowfiveodds = 600
            if self.game.green_odds.position == 1:
                greenthreeodds = 4
                greenfourodds = 12
                greenfiveodds = 60
            elif self.game.green_odds.position == 2:
                greenthreeodds = 4
                greenfourodds = 16
                greenfiveodds = 72
            elif self.game.green_odds.position == 3:
                greenthreeodds = 6
                greenfourodds = 24
                greenfiveodds = 96
            elif self.game.green_odds.position == 4:
                greenthreeodds = 8
                greenfourodds = 32
                greenfiveodds = 128
            elif self.game.green_odds.position == 5:
                greenthreeodds = 12
                greenfourodds = 36
                greenfiveodds = 144
            elif self.game.green_odds.position == 6:
                greenthreeodds = 16
                greenfourodds = 48
                greenfiveodds = 192
            elif self.game.green_odds.position == 7:
                greenthreeodds = 20
                greenfourodds = 60
                greenfiveodds = 240
            elif self.game.green_odds.position == 8:
                greenthreeodds = 24
                greenfourodds = 72
                greenfiveodds = 360
            elif self.game.green_odds.position == 9:
                greenthreeodds = 30
                greenfourodds = 96
                greenfiveodds = 480
            elif self.game.green_odds.position == 10:
                greenthreeodds = 36
                greenfourodds = 120
                greenfiveodds = 600



            if relays == 3:
                if (red == 1 and relays == 3):
                    if self.game.search_index.status == False:
                        if self.game.red_replay_counter.position < redthreeodds:
                            self.game.search_index.engage(self.game)
                            self.red_replay_step_up(redthreeodds - self.game.red_replay_counter.position)
                if (yellow == 1 and relays == 3):
                    if self.game.search_index.status == False:
                        if self.game.yellow_replay_counter.position < yellowthreeodds:
                            self.game.search_index.engage(self.game)
                            self.yellow_replay_step_up(yellowthreeodds - self.game.yellow_replay_counter.position)
                if (green == 1 and relays == 3):
                    if self.game.search_index.status == False:
                        if self.game.green_replay_counter.position < greenthreeodds:
                            self.game.search_index.engage(self.game)
                            self.green_replay_step_up(greenthreeodds - self.game.green_replay_counter.position)
            if relays == 4:
                if (red == 1 and relays == 4):
                    if self.game.search_index.status == False:
                        if self.game.red_replay_counter.position < redfourodds:
                            self.game.search_index.engage(self.game)
                            self.red_replay_step_up(redfourodds - self.game.red_replay_counter.position)
                if (yellow == 1 and relays == 4):
                    if self.game.search_index.status == False:
                        if self.game.yellow_replay_counter.position < yellowfourodds:
                            self.game.search_index.engage(self.game)
                            self.yellow_replay_step_up(yellowfourodds - self.game.yellow_replay_counter.position)
                if (green == 1 and relays == 4):
                    if self.game.search_index.status == False:
                        if self.game.green_replay_counter.position < greenfourodds:
                            self.game.search_index.engage(self.game)
                            self.green_replay_step_up(greenfourodds - self.game.green_replay_counter.position)
            if relays == 5:
                if (red == 1 and relays == 5):
                    if self.game.search_index.status == False:
                        if self.game.red_replay_counter.position < redfiveodds:
                            self.game.search_index.engage(self.game)
                            self.red_replay_step_up(redfiveodds - self.game.red_replay_counter.position)
                if (yellow == 1 and relays == 5):
                    if self.game.search_index.status == False:
                        if self.game.yellow_replay_counter.position < yellowfiveodds:
                            self.game.search_index.engage(self.game)
                            self.yellow_replay_step_up(yellowfiveodds - self.game.yellow_replay_counter.position)
                if (green == 1 and relays == 5):
                    if self.game.search_index.status == False:
                        if self.game.green_replay_counter.position < greenfiveodds:
                            self.game.search_index.engage(self.game)
                            self.green_replay_step_up(greenfiveodds - self.game.green_replay_counter.position)


    def red_replay_step_up(self, number):
        self.game.sound.stop('search')
        self.game.sound.stop('search_screen')
        if number >= 1:
            self.game.red_replay_counter.step()
            number -= 1
            self.replay_step_up()
            if self.game.replays == 899:
                number = 0
            self.delay(name="red_replay_step_up", delay=0.25, handler=self.red_replay_step_up, param=number)
        else:
            self.game.search_index.disengage()
            self.cancel_delayed(name="red_replay_step_up")
            self.search()
            
    def yellow_replay_step_up(self, number):
        self.game.sound.stop('search')
        self.game.sound.stop('search_screen')
        if number >= 1:
            self.game.yellow_replay_counter.step()
            number -= 1
            self.replay_step_up()
            if self.game.replays == 899:
                number = 0
            self.delay(name="yellow_replay_step_up", delay=0.25, handler=self.yellow_replay_step_up, param=number)
        else:
            self.game.search_index.disengage()
            self.cancel_delayed(name="yellow_replay_step_up")
            self.search()

    def green_replay_step_up(self, number):
        self.game.sound.stop('search')
        self.game.sound.stop('search_screen')
        if number >= 1:
            self.game.green_replay_counter.step()
            number -= 1
            self.replay_step_up()
            if self.game.replays == 899:
                number = 0
            self.delay(name="green_replay_step_up", delay=0.25, handler=self.green_replay_step_up, param=number)
        else:
            self.game.search_index.disengage()
            self.cancel_delayed(name="green_replay_step_up")
            self.search()


    def closed_search_relays(self, rivets):
        # This function is critical, as it will determine which card is returned, etc.  I need to check the position of the
        # replay counter for the card. We will get a row back
        # that has the numbers on the position which will return the search relay connected.  When three out of the five relays
        # are connected, we get a winner!

        # I have to adjust this quite a bit for magic screen games.  I will implement the standard search relays based on
        # what I decide (commented) because the search logic is insanely complex in the real deal.  It will be easier
        # for non-section wins to search based on what I enter here.

        # For section wins, see find_section_winner() further into the code.
        
        self.pos = {}
        red = False
        yellow = False
        green = False

        if self.game.magic_screen.position == 0:
            # Basic Position
            self.pos[0] = {}
 
            #Red Winners
            self.pos[1] = {10:1, 3:2, 14:3, 8:4, 12:5}
            self.pos[2] = {3:1, 21:2, 13:3, 22:4, 11:5}
            self.pos[3] = {12:1, 6:2, 25:3, 4:4, 9:5}
            self.pos[4] = {19:1, 22:2, 7:3, 18:4, 4:5}

            #Yellow Winners
            self.pos[5] = {10:1, 20:2, 17:3, 19:4, 15:5}
            self.pos[6] = {20:1, 21:2, 5:3, 23:4, 6:5}
            self.pos[7] = {8:1, 23:2, 24:3, 18:4, 1:5}
            self.pos[8] = {15:1, 11:2, 2:3, 1:4, 9:5}

            #Green Winners
            self.pos[9] = {17:1, 13:2, 16:3, 24:4, 25:5}
            self.pos[10] = {14:1, 5:2, 16:3, 7:4, 2:5}
            self.pos[11] = {10:1, 21:2, 16:3, 18:4, 9:5}
            self.pos[12] = {12:1, 23:2, 16:3, 22:4, 15:5}
          
        if self.game.magic_screen.position == 1:
            # Basic Position
            self.pos[0] = {}
           
            #Red Winners
            self.pos[1] = {3:1, 14:2, 8:3, 12:4, 3:5}
            self.pos[2] = {14:1, 5:2, 16:3, 7:4, 2:5}
            self.pos[3] = {3:1, 14:2, 22:3, 16:4, 8:5}
            self.pos[4] = {22:1, 7:2, 18:3, 4:4, 16:5}

            #Yellow Winners
            self.pos[5] = {3:1, 21:2, 13:3, 22:4, 11:5}
            self.pos[6] = {21:1, 5:2, 23:3, 6:4, 14:5}
            self.pos[7] = {12:1, 6:2, 25:3, 4:4, 9:5}
            self.pos[8] = {11:1, 2:2, 1:3, 9:4, 8:5}

            #Green Winners
            self.pos[9] = {13:1, 16:2, 24:3, 25:4, 22:5}
            self.pos[10] = {8:1, 23:2, 24:3, 18:4, 1:5}
            self.pos[11] = {3:1, 5:2, 24:3, 4:4, 8:5}
            self.pos[12] = {3:1, 6:2, 24:3, 7:4, 11:5}

        if self.game.magic_screen.position == 2:
            # Basic Position
            self.pos[0] = {}
           
            #Red Winners
            self.pos[1] = {14:1, 8:2, 12:3, 3:4, 24:5}
            self.pos[2] = {8:1, 23:2, 24:3, 18:4, 1:5}
            self.pos[3] = {24:1, 1:2, 19:3, 5:4, 25:5}
            self.pos[4] = {7:1, 18:2, 4:3, 16:4, 5:5}

            #Yellow Winners
            self.pos[5] = {14:1, 5:2, 16:3, 7:4, 2:5}
            self.pos[6] = {5:1, 23:2, 6:3, 14:4, 1:5}
            self.pos[7] = {3:1, 14:2, 22:3, 16:4, 8:5}
            self.pos[8] = {2:1, 1:2, 9:3, 8:4, 25:5}

            #Green Winners
            self.pos[9] = {16:1, 24:2, 25:3, 22:4, 19:5}
            self.pos[10] = {12:1, 6:2, 25:3, 4:4, 9:5}
            self.pos[11] = {14:1, 23:2, 25:3, 16:4, 25:5}
            self.pos[12] = {24:1, 14:2, 25:3, 18:4, 2:5}

        if self.game.magic_screen.position == 3:
            # Basic Position
            self.pos[0] = {}
           
            #Red Winners
            self.pos[1] = {8:1, 12:2, 3:3, 24:4, 20:5}
            self.pos[2] = {12:1, 6:2, 25:3, 4:4, 9:5}
            self.pos[3] = {20:1, 12:2, 9:3, 23:4, 21:5}
            self.pos[4] = {18:1, 4:2, 16:3, 5:4, 23:5}

            #Yellow Winners
            self.pos[5] = {8:1, 23:2, 24:3, 18:4, 1:5}
            self.pos[6] = {23:1, 6:2, 14:3, 1:4, 12:5}
            self.pos[7] = {24:1, 1:2, 19:3, 5:4, 25:5}
            self.pos[8] = {1:1, 9:2, 8:3, 25:4, 21:5}

            #Green Winners
            self.pos[9] = {24:1, 25:2, 22:3, 19:4, 9:5}
            self.pos[10] = {3:1, 14:2, 22:3, 16:4, 8:5}
            self.pos[11] = {8:1, 6:2, 22:3, 5:4, 21:5}
            self.pos[12] = {20:1, 1:2, 22:3, 4:4, 1:5}

        if self.game.magic_screen.position == 4:
            # Basic Position
            self.pos[0] = {}
           
            #Red Winners
            self.pos[1] = {12:1, 3:2, 24:3, 20:4, 17:5}
            self.pos[2] = {3:1, 14:2, 22:3, 16:4, 8:5}
            self.pos[3] = {17:1, 4:2, 7:3, 13:4, 15:5}
            self.pos[4] = {4:1, 16:2, 5:3, 23:4, 13:5}

            #Yellow Winners
            self.pos[5] = {12:1, 6:2, 25:3, 4:4, 9:5}
            self.pos[6] = {6:1, 14:2, 1:3, 12:4, 4:5}
            self.pos[7] = {20:1, 12:2, 9:3, 23:4, 21:5}
            self.pos[8] = {9:1, 8:2, 25:3, 21:4, 15:5}

            #Green Winners
            self.pos[9] = {25:1, 22:2, 19:3, 9:4, 7:5}
            self.pos[10] = {24:1, 1:2, 19:3, 5:4, 25:5}
            self.pos[11] = {12:1, 14:2, 19:3, 23:4, 15:5}
            self.pos[12] = {17:1, 12:2, 19:3, 16:4, 9:5}

        if self.game.magic_screen.position == 5:
            # Basic Position
            self.pos[0] = {}
           
            #Red Winners
            self.pos[1] = {3:1, 24:2, 20:3, 17:4, 6:5}
            self.pos[2] = {24:1, 1:2, 19:3, 5:4, 25:5}
            self.pos[3] = {6:1, 10:2, 18:3, 11:4, 2:5}
            self.pos[4] = {16:1, 5:2, 23:3, 13:4, 11:5}

            #Yellow Winners
            self.pos[5] = {3:1, 14:2, 22:3, 16:4, 8:5}
            self.pos[6] = {14:1, 1:2, 12:3, 4:4, 10:5}
            self.pos[7] = {17:1, 4:2, 7:3, 13:4, 15:5}
            self.pos[8] = {8:1, 25:2, 21:3, 15:4, 2:5}

            #Green Winners
            self.pos[9] = {22:1, 19:2, 9:3, 7:4, 18:5}
            self.pos[10] = {20:1, 12:2, 9:3, 23:4, 21:5}
            self.pos[11] = {3:1, 1:2, 9:3, 13:4, 2:5}
            self.pos[12] = {6:1, 4:2, 9:3, 5:4, 8:5}

        if self.game.magic_screen.position == 6:
            # Basic Position
            self.pos[0] = {}
           
            #Red Winners
            self.pos[1] = {24:1, 20:2, 17:3, 6:4, 13:5}
            self.pos[2] = {20:1, 12:2, 9:3, 23:4, 21:5}
            self.pos[3] = {13:1, 21:2, 12:3, 19:4, 4:5}
            self.pos[4] = {5:1, 23:2, 13:3, 11:4, 19:5}

            #Yellow Winners
            self.pos[5] = {24:1, 1:2, 19:3, 5:4, 25:5}
            self.pos[6] = {1:1, 12:2, 4:3, 10:4, 21:5}
            self.pos[7] = {6:1, 10:2, 18:3, 11:4, 2:5}
            self.pos[8] = {25:1, 21:2, 15:3, 2:4, 4:5}

            #Green Winners
            self.pos[9] = {19:1, 9:2, 7:3, 18:4, 12:5}
            self.pos[10] = {17:1, 4:2, 7:3, 13:4, 15:5}
            self.pos[11] = {24:1, 12:2, 7:3, 11:4, 4:5}
            self.pos[12] = {13:1, 10:2, 7:3, 23:4, 25:5}
            
        if self.game.magic_screen.position == 7:
            # Basic Position
            self.pos[0] = {}
           
            #Red Winners
            self.pos[1] = {20:1, 17:2, 6:3, 13:4, 9:5}
            self.pos[2] = {17:1, 4:2, 7:3, 13:4, 15:5}
            self.pos[3] = {9:1, 2:2, 23:3, 6:4, 20:5}
            self.pos[4] = {23:1, 13:2, 11:3, 19:4, 6:5}

            #Yellow Winners
            self.pos[5] = {20:1, 12:2, 9:3, 23:4, 21:5}
            self.pos[6] = {12:1, 4:2, 10:3, 21:4, 2:5}
            self.pos[7] = {13:1, 21:2, 12:3, 19:4, 4:5}
            self.pos[8] = {21:1, 15:2, 2:3, 4:4, 20:5}

            #Green Winners
            self.pos[9] = {9:1, 7:2, 18:3, 12:4, 23:5}
            self.pos[10] = {6:1, 10:2, 18:3, 11:4, 2:5}
            self.pos[11] = {20:1, 4:2, 18:3, 19:4, 20:5}
            self.pos[12] = {9:1, 21:2, 18:3, 13:4, 21:5}

        if self.game.magic_screen.position == 8:
            # Basic Position
            self.pos[0] = {}
           
            #Red Winners
            self.pos[1] = {17:1, 6:2, 13:3, 9:4, 18:5}
            self.pos[2] = {6:1, 10:2, 18:3, 11:4, 2:5}
            self.pos[3] = {18:1, 15:2, 11:3, 17:4, 10:5}
            self.pos[4] = {13:1, 11:2, 19:3, 6:4, 17:5}

            #Yellow Winners
            self.pos[5] = {17:1, 4:2, 7:3, 13:4, 15:5}
            self.pos[6] = {4:1, 10:2, 21:3, 2:4, 15:5}
            self.pos[7] = {9:1, 2:2, 23:3, 6:4, 20:5}
            self.pos[8] = {15:1, 2:2, 4:3, 20:4, 10:5}

            #Green Winners
            self.pos[9] = {7:1, 18:2, 12:3, 23:4, 11:5}
            self.pos[10] = {13:1, 21:2, 12:3, 19:4, 4:5}
            self.pos[11] = {17:1, 10:2, 12:3, 6:4, 10:5}
            self.pos[12] = {18:1, 2:2, 12:3, 11:4, 15:5}

        if self.game.magic_screen.position == 9:
            # Basic Position
            self.pos[0] = {}
           
            #Red Winners
            self.pos[1] = {6:1, 13:2, 9:3, 18:4, 7:5}
            self.pos[2] = {13:1, 21:2, 12:3, 19:4, 4:5}
            self.pos[3] = {7:1, 8:2, 16:3, 1:4, 22:5}
            self.pos[4] = {11:1, 19:2, 6:3, 17:4, 1:5}

            #Yellow Winners
            self.pos[5] = {6:1, 10:2, 18:3, 11:4, 2:5}
            self.pos[6] = {10:1, 21:2, 2:3, 15:4, 8:5}
            self.pos[7] = {18:1, 15:2, 11:3, 17:4, 10:5}
            self.pos[8] = {2:1, 4:2, 20:3, 10:4, 22:5}

            #Green Winners
            self.pos[9] = {18:1, 12:2, 23:3, 11:4, 16:5}
            self.pos[10] = {9:1, 2:2, 23:3, 6:4, 20:5}
            self.pos[11] = {6:1, 21:2, 23:3, 17:4, 22:5}
            self.pos[12] = {7:1, 15:2, 23:3, 19:4, 2:5}

        if self.game.magic_screen.position == 10:
            # Basic Position
            self.pos[0] = {}
           
            #Red Winners
            self.pos[1] = {13:1, 9:2, 18:3, 7:4, 5:5}
            self.pos[2] = {9:1, 2:2, 23:3, 6:4, 20:5}
            self.pos[3] = {5:1, 25:2, 24:3, 14:4, 3:5}
            self.pos[4] = {19:1, 6:2, 17:3, 1:4, 14:5}

            #Yellow Winners
            self.pos[5] = {13:1, 21:2, 12:3, 19:4, 4:5}
            self.pos[6] = {21:1, 2:2, 15:3, 8:4, 25:5}
            self.pos[7] = {7:1, 8:2, 16:3, 1:4, 22:5}
            self.pos[8] = {4:1, 20:2, 10:3, 22:4, 3:5}

            #Green Winners
            self.pos[9] = {12:1, 23:2, 11:3, 16:4, 24:5}
            self.pos[10] = {18:1, 15:2, 11:3, 17:4, 10:5}
            self.pos[11] = {13:1, 2:2, 11:3, 1:4, 3:5}
            self.pos[12] = {5:1, 8:2, 11:3, 6:4, 4:5}

        if rivets in [1,2,3,4]:
            red = True
        if rivets in [5,6,7,8]:
            yellow = True
        if rivets in [9,10,11,12]:
            green = True
            
        return (self.pos[rivets], red, yellow, green, rivets)


    
    def scan_all(self):
        #Animate scanning of everything - this happens through the spotting disc
        self.all_probability()

    def all_probability(self):
        mix1 = self.game.mixer1.connected_rivet()
        if self.game.reflex.connected_rivet() == 0:
            #Worst position for reflex - requires mixer1 to be in the three liberal positions for the connection of the wires bypassing the reflex.
            if (mix1 in [18,12]):
                self.check_advance()
        if self.game.reflex.connected_rivet() == 1 and (mix1 in [2,7,11,14,16,20,22,24,6,5,13,15]):
            self.check_advance()
        elif self.game.reflex.connected_rivet() == 2 and (mix1 in [2,7,11,14,16,20,22,24,6,5,13,15,4,9,23]):
            self.check_advance()
        elif self.game.reflex.connected_rivet() == 3 and (mix1 not in [18,12]):
            self.check_advance()
        elif self.game.reflex.connected_rivet() == 4:
            self.check_advance()
        else:
            self.check_advance()

    def check_advance(self):
        if self.game.green_odds.position == 0:
            self.game.green_odds.step()
            if self.game.red_odds.position == 0:
                self.game.red_odds.step()
            if self.game.yellow_odds.position == 0:
                self.game.yellow_odds.step()
            self.game.before_fourth.engage(self.game)
            self.check_sd()
            self.delay(name="display", delay=0.1, handler=graphics.the_twist.display, param=self)
            return
        else:
            if self.game.advance_green.status == True:
                self.game.green_odds.step()
            elif self.game.advance_red.status == True:
                self.game.red_odds.step()
            elif self.game.advance_yellow.status == True:
                self.game.yellow_odds.step()
            elif self.game.advance_card.status == True:
                self.game.magic_card.step()

            self.game.advance_green.disengage()
            self.game.advance_red.disengage()
            self.game.advance_yellow.disengage()
            self.game.advance_card.disengage()

            self.check_sd()

    def check_sd(self):

        sd = self.game.spotting.connected_rivet()

        if sd in [1,8,10,12,20,25]:
            if self.game.yellow_odds.position < 10:
                self.game.advance_yellow.engage(self.game)
            else:
                if self.game.green_odds.position < 10:
                    self.game.advance_green.engage(self.game)
                else:
                    if self.game.red_odds.position < 10:
                        self.game.advance_red.engage(self.game)
                    else:
                        if self.game.magic_card.position < 10:
                            self.game.advance_card.engage(self.game)
        elif sd in [3,7,13,14,16,21]:
            if self.game.green_odds.position < 10:
                self.game.advance_green.engage(self.game)
            else:
                if self.game.red_odds.position < 10:
                    self.game.advance_red.engage(self.game)
                else:
                    if self.game.magic_card.position < 10:
                        self.game.advance_card.engage(self.game)
                    else:
                        if self.game.yellow_odds.position < 10:
                            self.game.advance_yellow.engage(self.game)
        elif sd in [2,4,9,11,17,22,24]:
            if self.game.red_odds.position < 10:
                self.game.advance_red.engage(self.game)
            else:
                if self.game.magic_card.position < 10:
                    self.game.advance_card.engage(self.game)
                else:
                    if self.game.yellow_odds.position < 10:
                        self.game.advance_yellow.engage(self.game)
                    else:
                        if self.game.green_odds.position < 10:
                            self.game.advance_green.engage(self.game)
        elif sd in [5,6,15,18,19,23]:
            if self.game.magic_card.position < 10:
                self.game.advance_card.engage(self.game)
            else:
                if self.game.yellow_odds.position < 10:
                    self.game.advance_yellow.engage(self.game)
                else:
                    if self.game.green_odds.position < 10:
                        self.game.advance_green.engage(self.game)
                    else:
                        if self.game.red_odds.position < 10:
                            self.game.advance_red.engage(self.game)

        if sd in [1,2,3,7,8,9,10,15,17,18,19,20,23,24]:
            if self.game.cu == True:
                if self.game.before_fourth.status == True:
                    self.game.before_fourth.disengage()
                    self.game.before_fifth.engage(self.game)

        self.delay(name="display", delay=0.1, handler=graphics.the_twist.display, param=self)

    def eb_reflex(self):
        mix1 = self.game.mixer1.connected_rivet()
        if self.game.reflex.connected_rivet() == 0:
            #Worst position for reflex - requires mixer1 to be in the three liberal positions for the connection of the wires bypassing the reflex.
            if (mix1 in [18,12]):
                return 1
        elif self.game.reflex.connected_rivet() == 1 and (mix1 in [2,7,11,14,16,20,22,24,6,5,13,15]):
            return 1
        elif self.game.reflex.connected_rivet() == 2 and (mix1 in [2,7,11,14,16,20,22,24,6,5,13,15,4,9,23]):
            return 1
        elif self.game.reflex.connected_rivet() == 3 and (mix1 not in [18,12]):
            return 1
        elif self.game.reflex.connected_rivet() == 4:
            return 1
        else:
            return 0

    def step_magic_screen(self, number):
        if number >= 1:
            self.game.magic_screen_feature.step()
            number -= 1
            self.delay(name="display", delay=0.1, handler=graphics.the_twist.display, param=self)
            self.delay(name="step_sc", delay=0.1, handler=self.step_magic_screen, param=number)

    def scan_eb(self):
        if self.game.extra_ball.position == 0:
            self.game.extra_ball.step()
            self.check_lifter_status()
        p = self.eb_reflex()
        if p == 1:
            self.eb_probability()
                                
        # Timer resets to 0 position on ball count increasing.  We are fudging this since we will have
        # no good way to measure balls as they return back to the trough.  The ball count unit cannot be
        # relied upon as we do not have a switch in the outhole, and the trough logic is too complex for
        # the task at hand.
        # TODO: implement thunk noises into the units.py to automatically play the noises.
        self.game.timer.reset()
        self.delay(name="display", delay=0.1, handler=graphics.the_twist.display, param=self)

    def animate_both(self, args):
        start = args[0]
        diff = args[1]
        num = args[2]
        if start + num >= 50:
            start = 0
        if diff >= 0:
            num = num + 1
            graphics.the_twist.both_animation([self, start + num])
            self.cancel_delayed(name="display")
            diff = diff - 1
            args = [start,diff,num]
            self.delay(name="both_animation", delay=0.08, handler=self.animate_both, param=args)
        else:
            self.cancel_delayed(name="both_animation")
            self.delay(name="display", delay=0.1, handler=graphics.the_twist.display, param=self)
            self.scan_all()

    def animate_screen_right(self, args):
        self.game = args[0]
        num = args[1]
        if num >= 0:
            graphics.the_twist.screen_animation([self, num, "right"])
            self.cancel_delayed(name="display")
            num = num - 1
            args = [self.game,num,"right"]
            self.delay(name="right_animation", delay=0.004, handler=self.animate_screen_right, param=args)
        else:
            self.cancel_delayed(name="right_animation")
            self.delay(name="display", delay=0.1, handler=graphics.the_twist.display, param=self)

    def animate_screen_left(self, args):
        self.game = args[0]
        num = args[1]
        if num >= 0:
            graphics.the_twist.screen_animation([self, num, "left"])
            self.cancel_delayed(name="display")
            num = num - 1
            args = [self.game,num,"left"]
            self.delay(name="left_animation", delay=0.004, handler=self.animate_screen_left, param=args)
        else:
            self.cancel_delayed(name="left_animation")
            self.delay(name="display", delay=0.1, handler=graphics.the_twist.display, param=self)


    def animate_eb_scan(self, args):
        start = args[0]
        diff = args[1]
        num = args[2]
        if start + num >= 50:
            start = 0
        if diff >= 0:
            num = num + 1
            graphics.the_twist.eb_animation([self, start + num])
            self.cancel_delayed(name="display")
            diff = diff - 1
            args = [start,diff,num]
            self.delay(name="eb_animation", delay=0.08, handler=self.animate_eb_scan, param=args)
        else:
            self.cancel_delayed(name="eb_animation")
            self.delay(name="display", delay=0.1, handler=graphics.the_twist.display, param=self)
            self.scan_eb()

    def eb_probability(self):
        mix2 = self.game.mixer2.position
        sd = self.game.spotting.position
        if sd in [2,12,23]:
            if mix2 == 12:
                if self.game.cu == True:
                    self.step_eb(10 - self.game.extra_ball.position)
        else:
            if self.game.cu == True:
                self.step_eb(1)
 
    def step_eb(self, number):
        if number >= 1:
            self.game.extra_ball.step()
            self.check_lifter_status()
            number -= 1
            self.delay(name="display", delay=0.1, handler=graphics.the_twist.display, param=self)
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

class TheTwist(procgame.game.BasicGame):
    """ The Twist is the only game with Magic Cards """
    def __init__(self, machine_type):
        super(TheTwist, self).__init__(machine_type)
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

        self.searchdisc = units.Search("searchdisc", 12)

        #Search relays
        self.s1 = units.Relay("s1")
        self.s2 = units.Relay("s2")
        self.s3 = units.Relay("s3")
        self.s4 = units.Relay("s4")
        self.s5 = units.Relay("s5")
        self.search_index = units.Relay("search_index")

        #Odds steppers
        self.red_odds = units.Stepper("red_odds", 10, 'the_twist')
        self.yellow_odds = units.Stepper("yellow_odds", 10, 'the_twist')
        self.green_odds = units.Stepper("green_odds", 10, 'the_twist')

        #Replay Counter
        self.red_replay_counter = units.Stepper("red_replay_counter", 600)
        self.yellow_replay_counter = units.Stepper("yellow_replay_counter", 600)
        self.green_replay_counter = units.Stepper("green_replay_counter", 600)

        self.advance_green = units.Relay("advance_green")
        self.advance_yellow = units.Relay("advance_yellow")
        self.advance_red = units.Relay("advance_red")
        self.advance_card = units.Relay("advance_card")

        self.magic_card = units.Stepper("magic_card", 10)

        self.before_fourth = units.Relay("before_fourth")
        self.before_fifth = units.Relay("before_fifth")

        #Initialize stepper units used to keep track of features or timing.
        self.timer = units.Stepper("timer", 8)
        self.ball_count = units.Stepper("ball_count", 8)

        # Initialize reflex(es) and mixers unique to this game
        self.reflex = units.Reflex("primary", 200)

        #This is a disc which has 50 positions
        #and will randomly complete paths through the various mixers to allow for odds or feature step.
        self.spotting = units.Motor("spotting", 25)

        #Check for status of the replay register zero switch.  If positive
        #and machine is just powered on, this will zero out the replays.
        self.replay_reset = units.Relay("replay_reset")
        
        #Extra ball unit contains 24 positions.
        self.extra_ball = units.Stepper("extra_ball", 21)

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

        self.selector = units.Stepper("selector", 1)

        self.magic_screen = units.Stepper("magic_screen", 10)

        #Some special trip relays for spotted numbers and rollovers
        self.red_star = units.Relay("red_star")
        self.yellow_star = units.Relay("yellow_star")
        
        self.mixer4_relay = units.Relay("mixer4_relay")

        self.replays = 0
        self.returned = False

    def reset(self):
        super(TheTwist, self).reset()
        self.logger = logging.getLogger('game')
        self.load_config('bingo.yaml')
        
        main_mode = SinglecardBingo(self)
        self.modes.add(main_mode)
        
game = TheTwist(machine_type='pdb')
game.reset()
game.run_loop()
