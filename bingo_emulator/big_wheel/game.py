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
from bingo_emulator.graphics.big_wheel import *

class SinglecardBingo(procgame.game.Mode):
    def __init__(self, game):
        super(SinglecardBingo, self).__init__(game=game, priority=5)
        self.holes = []
        self.startup()
        self.game.sound.register_music('motor', "audio/magic_screen_control_unit.wav")
        self.game.sound.register_sound('search', "audio/mystic_line_search.wav")
        self.game.sound.register_sound('coin1', "audio/magic_screen_coin1.wav")
        self.game.sound.register_sound('coin2', "audio/magic_screen_coin2.wav")
        self.game.sound.register_sound('coin3', "audio/magic_screen_coin3.wav")
        self.game.sound.register_sound('square', "audio/magic_square.wav")
        self.game.sound.register_sound('tilt', "audio/tilt.wav")
        self.game.sound.register_sound('step', "audio/step.wav")
        self.game.sound.register_sound('eb_search', "audio/EB_Search.wav")

    def sw_coin_active(self, sw):
        if self.game.start.status == True:
            if self.game.all_advantages.status == True:
                self.game.odds_only.disengage()
                self.game.features.disengage()
                self.regular_play()
            elif self.game.features.status == True:
                self.game.odds_only.disengage()
                self.game.all_advantages.disengage()
                self.regular_play()
            elif self.game.odds_only.status == True:
                self.game.features.disengage()
                self.game.all_advantages.disengage()
                self.regular_play()
            elif self.game.special.status == True:
                self.game.features.disengage()
                self.game.all_advantages.disengage()
                self.game.odds_only.disengage()
                self.regular_play()
        else:
            self.game.all_advantages.engage(self.game)
            self.game.odds_only.disengage()
            self.game.features.disengage()
            self.game.special.disengage()
            self.regular_play()
        self.delay(name="display", delay=0.1, handler=graphics.big_wheel.display, param=self)

    

    def sw_startButton_active(self, sw):
        self.cancel_delayed(name="both_animation")
        self.cancel_delayed(name="odds_animation")
        self.cancel_delayed(name="feature_animation")
        self.cancel_delayed(name="double_animation")
        self.cancel_delayed(name="blink")
        self.game.odds_only.disengage()
        self.game.special.disengage()
        self.game.features.disengage()
        self.game.all_advantages.engage(self.game)
        self.delay(name="display", delay=0.1, handler=graphics.big_wheel.display, param=self)
        if self.game.replays > 0 or self.game.switches.freeplay.is_active():
            self.game.tilt.disengage()
            self.regular_play()
        self.delay(name="display", delay=0.1, handler=graphics.big_wheel.display, param=self)

    def sw_blue_active(self, sw):
        if self.game.start.status == True:
            self.game.features.disengage()
            self.game.special.disengage()
            self.game.all_advantages.disengage()
            self.game.odds_only.engage(self.game)
            self.delay(name="display", delay=0.1, handler=graphics.big_wheel.display, param=self)
        if self.game.replays > 0 or self.game.switches.freeplay.is_active():
            if self.game.start.status == False:
                self.delay(name="startup", delay=0.1, handler=self.sw_startButton_active, param=sw)
            if self.game.odds_only.status == True:
                self.delay(name="display", delay=0.1, handler=graphics.big_wheel.display, param=self)
                self.regular_play()
                self.delay(name="display", delay=0.1, handler=graphics.big_wheel.display, param=self)


    def sw_green_active(self, sw):
        self.cancel_delayed(name="both_animation")
        self.cancel_delayed(name="odds_animation")
        self.cancel_delayed(name="feature_animation")
        if self.game.start.status == True:
            self.game.features.engage(self.game)
            self.game.special.disengage()
            self.game.all_advantages.disengage()
            self.game.odds_only.disengage()
            self.delay(name="display", delay=0.1, handler=graphics.big_wheel.display, param=self)
        if self.game.replays > 0 or self.game.switches.freeplay.is_active():
            if self.game.start.status == False:
                self.delay(name="startup", delay=0.1, handler=self.sw_startButton_active, param=sw)
            if self.game.features.status == True:
                self.delay(name="display", delay=0.1, handler=graphics.big_wheel.display, param=self)
                self.regular_play()
                self.delay(name="display", delay=0.1, handler=graphics.big_wheel.display, param=self)


    def sw_enter_active(self, sw):
        if self.game.switches.left.is_active() and self.game.switches.right.is_active():
            self.game.end_run_loop()
            os.system("/home/nbaldridge/proc/bingo_emulator/start_game.sh big_wheel")
        else:
            if self.game.ball_count.position >= 4:
                self.game.sound.stop_music()
                self.game.sound.play_music('motor', -1)
                self.game.timer.reset()
                if self.game.search_index.status == False:
                    self.search(1)
                    self.timeout_actions()
                self.delay(name="display", delay=0.1, handler=graphics.big_wheel.display, param=self)


    def sw_trough4_active_for_1s(self, sw):
        if self.game.ball_count.position >= 4:
            self.timeout_actions()
    
    def timeout_actions(self):
        if (self.game.timer.position < 7):
            self.game.timer.step()
            self.delay(name="timeout", delay=5.0, handler=self.timeout_actions)
        else:
            self.game.timer.step()
            self.game.sound.stop_music()

    def sw_trough8_closed(self, sw):
        if self.game.start.status == False:
            self.game.ball_count.position -= 1
            self.game.returned = True
            self.check_lifter_status()
        else:
            self.check_lifter_status()

    def sw_right_active(self, sw):
        if self.game.ball_count.position > 0:
            max_ball = 0
            if self.game.selection_feature.position < 5:
                max_ball = 4
            elif self.game.selection_feature.position < 9:
                max_ball = 5
            else:
                if self.game.selection_feature.position == 9:
                    max_ball = 6

            if self.game.ball_count.position < max_ball:
                #Limit to A
                rp = self.game.ring.position + 1
                if self.game.wheel.position in [1,2]:
                    if rp < 4:
                        self.game.sound.play('square')
                        self.game.ring.step()
                        self.cancel_delayed("left_animation")
                        self.cancel_delayed("right_animation")
                        self.animate_wheel_right([self.game,30])
                #B
                elif self.game.wheel.position in [3,4]:
                    if rp < 8:
                        self.game.sound.play('square')
                        self.game.ring.step()
                        self.cancel_delayed("left_animation")
                        self.cancel_delayed("right_animation")
                        self.animate_wheel_right([self.game,30])
                #C
                elif self.game.wheel.position in [5,6]:
                    if rp < 13:
                        self.game.sound.play('square')
                        self.game.ring.step()
                        self.cancel_delayed("left_animation")
                        self.cancel_delayed("right_animation")
                        self.animate_wheel_right([self.game,30])
                #D
                elif self.game.wheel.position in [7,8]:
                    if rp < 17:
                        self.game.sound.play('square')
                        self.game.ring.step()
                        self.cancel_delayed("left_animation")
                        self.cancel_delayed("right_animation")
                        self.animate_wheel_right([self.game,30])
                #E
                elif self.game.wheel.position == 9:
                    self.game.sound.play('square')
                    self.game.ring.step()
                    self.cancel_delayed("left_animation")
                    self.cancel_delayed("right_animation")
                    self.animate_wheel_right([self.game,30])
                            
            self.delay(name="display", delay=0.1, handler=graphics.big_wheel.display, param=self)

    def sw_right_active_for_400ms(self,sw):
        if self.game.ball_count.position > 0:
            max_ball = 0
            if self.game.selection_feature.position < 5:
                max_ball = 4
            elif self.game.selection_feature.position < 9:
                max_ball = 5
            else:
                if self.game.selection_feature.position == 9:
                    max_ball = 6

            if self.game.ball_count.position < max_ball:
                #Limit to A
                rp = self.game.ring.position + 1
                if self.game.wheel.position in [1,2]:
                    if rp < 4:
                        self.game.sound.play('square')
                        self.game.ring.step()
                        self.cancel_delayed("left_animation")
                        self.cancel_delayed("right_animation")
                        self.animate_wheel_right([self.game,30])
                #B
                elif self.game.wheel.position in [3,4]:
                    if rp < 8:
                        self.game.sound.play('square')
                        self.game.ring.step()
                        self.cancel_delayed("left_animation")
                        self.cancel_delayed("right_animation")
                        self.animate_wheel_right([self.game,30])
                #C
                elif self.game.wheel.position in [5,6]:
                    if rp < 13:
                        self.game.sound.play('square')
                        self.game.ring.step()
                        self.cancel_delayed("left_animation")
                        self.cancel_delayed("right_animation")
                        self.animate_wheel_right([self.game,30])
                #D
                elif self.game.wheel.position in [7,8]:
                    if rp < 17:
                        self.game.sound.play('square')
                        self.game.ring.step()
                        self.cancel_delayed("left_animation")
                        self.cancel_delayed("right_animation")
                        self.animate_wheel_right([self.game,30])
                #E
                elif self.game.wheel.position == 9:
                    self.game.sound.play('square')
                    self.game.ring.step()
                    self.cancel_delayed("left_animation")
                    self.cancel_delayed("right_animation")
                    self.animate_wheel_right([self.game,30])
                            
            self.delay(name="display", delay=0.1, handler=graphics.big_wheel.display, param=self)
            self.delay(name="right", delay=0.1, handler=self.sw_right_active_for_400ms, param=sw)

    def sw_left_active(self, sw):
        if self.game.ball_count.position > 0:
            max_ball = 0
            if self.game.selection_feature.position < 5:
                max_ball = 4
            elif self.game.selection_feature.position < 9:
                max_ball = 5
            else:
                if self.game.selection_feature.position == 9:
                    max_ball = 6

            if self.game.ball_count.position < max_ball:
                #Limit to A
                rp = self.game.ring.position - 1
                if self.game.wheel.position in [1,2,3,4,5,6,7,8]:
                    if rp > -1:
                        self.game.sound.play('square')
                        self.game.ring.stepdown()
                        self.cancel_delayed("left_animation")
                        self.cancel_delayed("right_animation")
                        self.animate_wheel_left([self.game,30])
                elif self.game.wheel.position == 9:
                    self.game.sound.play('square')
                    self.game.ring.stepdown()
                    self.cancel_delayed("left_animation")
                    self.cancel_delayed("right_animation")
                    self.animate_wheel_left([self.game,30])
                            
            self.delay(name="display", delay=0.1, handler=graphics.big_wheel.display, param=self)

    def sw_left_active_for_400ms(self,sw):
        if self.game.ball_count.position > 0:
            max_ball = 0
            if self.game.selection_feature.position < 5:
                max_ball = 4
            elif self.game.selection_feature.position < 9:
                max_ball = 5
            else:
                if self.game.selection_feature.position == 9:
                    max_ball = 6

            if self.game.ball_count.position < max_ball:
                #Limit to A
                rp = self.game.ring.position - 1
                if self.game.wheel.position in [1,2,3,4,5,6,7,8]:
                    if rp > -1:
                        self.game.sound.play('square')
                        self.game.ring.stepdown()
                        self.cancel_delayed("left_animation")
                        self.cancel_delayed("right_animation")
                        self.animate_wheel_left([self.game,30])
                elif self.game.wheel.position == 9:
                    self.game.sound.play('square')
                    self.game.ring.stepdown()
                    self.cancel_delayed("left_animation")
                    self.cancel_delayed("right_animation")
                    self.animate_wheel_left([self.game,30])
                            
            self.delay(name="display", delay=0.1, handler=graphics.big_wheel.display, param=self)
            self.delay(name="left", delay=0.1, handler=self.sw_left_active_for_400ms, param=sw)

    def check_selection(self):
        if self.game.selection_feature.position == 9:
            self.game.red_star.disengage()
            self.game.yellow_star.disengage()
            self.game.coils.yellowROLamp.disable()
            self.game.coils.redROLamp.disable()
        self.delay(name="display", delay=0.1, handler=graphics.big_wheel.display, param=self)

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
        self.cancel_delayed(name="double_animation")
        self.cancel_delayed(name="feature_animation")
        self.cancel_delayed(name="both_animation")
        self.cancel_delayed(name="odds_animation")
        self.cancel_delayed(name="special_animation")
        self.cancel_delayed(name="blink")
        self.cancel_delayed(name="blink_double")
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
        self.game.sound.play_music('motor', -1)

        self.game.cu = not self.game.cu
        begin = self.game.spotting.position
        self.game.spotting.spin()
        self.game.mixer1.spin()
        self.game.mixer2.spin()
        self.game.mixer3.spin()
        self.game.reflex.decrease()
        if self.game.features.status == True:
            self.animate_features_scan([begin,self.game.spotting.movement_amount,1])
        if self.game.all_advantages.status == True:
            self.animate_both([begin,self.game.spotting.movement_amount,1])
        if self.game.odds_only.status == True:
            self.animate_odds_scan([begin,self.game.spotting.movement_amount,1])
        if self.game.special.status == True:    
            self.animate_double_scan([begin,self.game.spotting.movement_amount,1])

        self.game.returned = False
        if self.game.start.status == True:
            if self.game.selector.position < 1:
                self.game.selector.step()
            if self.game.switches.shutter.is_inactive():
                self.game.coils.shutter.enable()
            self.replay_step_down()
            graphics.big_wheel.display(self)
            self.check_lifter_status()
        elif red_letter == 1:
            self.holes = []
            self.game.double_colors.reset()
            self.game.start.engage(self.game)
            self.game.yellow_star.disengage()
            self.game.red_star.disengage()
            self.game.start.engage(self.game)
            self.game.ball_count.reset()
            self.game.selection_feature.reset()
            self.game.timer.reset()
            if self.game.ring.position != 0:
                self.reset_ring()
            self.game.wheel.reset()
            self.game.coils.redROLamp.disable()
            self.game.coils.yellowROLamp.disable()
            self.step_selection(1)
            self.step_wheel(9)
            self.game.sound.play_music('motor', -1)
            self.regular_play()
        else:
            self.holes = []
            self.game.start.engage(self.game)
            self.game.odds.reset()
            self.game.yellow_star.disengage()
            self.game.double_colors.reset()
            self.game.double.disengage()
            self.game.double_double.disengage()
            self.game.red_star.disengage()
            self.game.start.engage(self.game)
            self.game.ball_count.reset()
            self.game.selection_feature.reset()
            self.game.timer.reset()
            if self.game.ring.position != 0:
                self.reset_ring()
            self.game.wheel.reset()
            self.game.coils.redROLamp.disable()
            self.game.coils.yellowROLamp.disable()
            self.game.replay_counter.reset()
            self.game.selector.reset()
            self.game.ball_count.reset()
            self.game.timer.reset()
            self.game.winner = 0
            self.game.sound.play_music('motor', -1)
            self.regular_play()
        self.delay(name="display", delay=0.1, handler=graphics.big_wheel.display, param=self)
        self.game.tilt.disengage()

    def reset_ring(self):
        if self.game.ring.position != 0:
            self.game.sound.play('square')
            self.game.ring.step()
            self.cancel_delayed("left_animation")
            self.cancel_delayed("right_animation")
            self.animate_wheel_right([self.game,30])
            self.delay(name="ring_step", delay=0.1, handler=self.reset_ring)
            self.delay(name="display", delay=0.1, handler=graphics.big_wheel.display, param=self)


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
                    if self.game.returned == True and self.game.ball_count.position == 4:
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
                if self.game.ball_count.position < 5 and self.game.double.status == False and self.game.double_double.status == False:
                    self.game.coils.lifter.enable()
                elif self.game.ball_count.position < 3 and self.game.double.status == True:
                    self.game.coils.lifter.enable()

    def sw_gate_inactive_for_1ms(self, sw):
        self.cancel_delayed("lifter_status")
        self.game.start.disengage()
        self.game.ball_count.step()
        if self.game.switches.shutter.is_active():
            self.game.coils.shutter.enable()
        if self.game.ball_count.position == 4:
            self.game.sound.play('tilt')
            self.game.sound.play('tilt')
        if self.game.ball_count.position >= 5:
            self.game.coils.yellowROLamp.disable()
            self.game.coils.redROLamp.disable()
            self.search()
            self.game.sound.stop('search')
        if self.game.double.status == False and self.game.ball_count.position < 5:
            self.check_lifter_status()
        elif self.game.double.status == True and self.game.ball_count.position < 3:
            self.check_lifter_status()
        elif self.game.double_double.status == True and self.game.ball_count.position < 3:
            self.check_lifter_status()
        self.delay(name="display", delay=0.1, handler=graphics.big_wheel.display, param=self)


    # This is really nasty, but it is how we render graphics for each individual hole.
    # numbers are added (or removed from) a list.  In this way, I can re-use the same
    # routine even for games where there are ball return functions like Surf Club.

    def sw_hole1_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(1)
            self.delay(name="display", delay=0.1, handler=graphics.big_wheel.display, param=self)

    def sw_hole2_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(2)
            self.delay(name="display", delay=0.1, handler=graphics.big_wheel.display, param=self)

    def sw_hole3_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(3)
            self.delay(name="display", delay=0.1, handler=graphics.big_wheel.display, param=self)

    def sw_hole4_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(4)
            self.delay(name="display", delay=0.1, handler=graphics.big_wheel.display, param=self)

    def sw_hole5_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(5)
            self.delay(name="display", delay=0.1, handler=graphics.big_wheel.display, param=self)

    def sw_hole6_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(6)
            self.delay(name="display", delay=0.1, handler=graphics.big_wheel.display, param=self)

    def sw_hole7_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(7)
            self.delay(name="display", delay=0.1, handler=graphics.big_wheel.display, param=self)

    def sw_hole8_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(8)
            self.delay(name="display", delay=0.1, handler=graphics.big_wheel.display, param=self)

    def sw_hole9_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(9)
            self.delay(name="display", delay=0.1, handler=graphics.big_wheel.display, param=self)

    def sw_hole10_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(10)
            self.delay(name="display", delay=0.1, handler=graphics.big_wheel.display, param=self)

    def sw_hole11_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(11)
            self.delay(name="display", delay=0.1, handler=graphics.big_wheel.display, param=self)

    def sw_hole12_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(12)
            self.delay(name="display", delay=0.1, handler=graphics.big_wheel.display, param=self)

    def sw_hole13_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(13)
            self.delay(name="display", delay=0.1, handler=graphics.big_wheel.display, param=self)

    def sw_hole14_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(14)
            self.delay(name="display", delay=0.1, handler=graphics.big_wheel.display, param=self)

    def sw_hole15_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(15)
            self.delay(name="display", delay=0.1, handler=graphics.big_wheel.display, param=self)

    def sw_hole16_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(16)
            self.delay(name="display", delay=0.1, handler=graphics.big_wheel.display, param=self)

    def sw_hole17_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(17)
            self.delay(name="display", delay=0.1, handler=graphics.big_wheel.display, param=self)

    def sw_hole18_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(18)
            self.delay(name="display", delay=0.1, handler=graphics.big_wheel.display, param=self)

    def sw_hole19_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(19)
            self.delay(name="display", delay=0.1, handler=graphics.big_wheel.display, param=self)

    def sw_hole20_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(20)
            self.delay(name="display", delay=0.1, handler=graphics.big_wheel.display, param=self)

    def sw_replayReset_active(self, sw):
        self.game.anti_cheat.disengage()
        self.holes = []
        graphics.big_wheel.display(self)
        self.tilt_actions()
        self.replay_step_down(self.game.replays)

    def sw_redstar_active(self, sw):
        if self.game.red_star.status == True:
            if self.game.selection_feature.position < 9:
                self.game.sound.play('tilt')
                self.game.selection_feature.step()
                self.game.coils.redROLamp.disable()
            self.delay(name="display", delay=0.1, handler=graphics.big_wheel.display, param=self)

    def sw_yellowstar_active(self, sw):
        if self.game.yellow_star.status == True:
            if self.game.selection_feature.position < 9:
                self.game.sound.play('tilt')
                self.game.selection_feature.step()
                self.game.yellow_star.disengage()
                self.game.coils.yellowROLamp.disable()
            self.delay(name="display", delay=0.1, handler=graphics.big_wheel.display, param=self)

    def tilt_actions(self):
        self.game.start.disengage()
        self.cancel_delayed(name="replay_reset")
        self.cancel_delayed(name="replay_step_up")
        self.cancel_delayed(name="blink")
        self.cancel_delayed(name="blink_double")
        self.cancel_delayed(name="double_animation")
        self.cancel_delayed(name="feature_animation")
        self.cancel_delayed(name="both_animation")
        self.cancel_delayed(name="odds_animation")
        self.cancel_delayed(name="timeout")
        self.game.coils.redROLamp.disable()
        self.game.coils.yellowROLamp.disable()
        self.game.search_index.disengage()
        if self.game.ball_count.position == 0:
            if self.game.switches.shutter.is_active():
                self.game.coils.shutter.enable()
        self.holes = []
        self.game.odds.reset()
        self.game.start.engage(self.game)
        self.game.ball_count.reset()
        self.game.selection_feature.reset()
        self.game.timer.reset()
        self.game.ring.reset()
        self.game.double_colors.reset()
        self.game.double.disengage()
        self.game.double_double.disengage()
        self.game.replay_counter.reset()
        self.game.yellow_star.disengage()
        self.game.red_star.disengage()
        self.game.selector.reset()
        self.game.ball_count.reset()
        self.game.selection_feature.reset()
        self.game.anti_cheat.engage(game)
        self.game.all_advantages.engage(self.game)
        self.game.odds_only.disengage()
        self.game.features.disengage()
        self.game.special.disengage()
        self.game.tilt.engage(self.game)
        self.game.wheel.reset()
        self.game.sound.stop_music()
        self.game.sound.play('tilt')
        # displays "Tilt" on the backglass, you have to recoin.
        self.delay(name="display", delay=0.1, handler=graphics.big_wheel.display, param=self)

    def sw_tilt_active(self, sw):
        if self.game.tilt.status == False:
            self.tilt_actions()

    def replay_step_down(self, number=0):
        if number > 0:
            if number > 1:
                self.game.replays -= 1
                graphics.replay_step_down(self.game.replays, graphics.big_wheel.reel1, graphics.big_wheel.reel10, graphics.big_wheel.reel100)
                self.game.coils.registerDown.pulse()
                number -= 1
                self.delay(name="display", delay=0, handler=graphics.big_wheel.display, param=self)
                self.delay(name="replay_reset", delay=0.13, handler=self.replay_step_down, param=number)
            elif number == 1:
                self.game.replays -= 1
                graphics.replay_step_down(self.game.replays, graphics.big_wheel.reel1, graphics.big_wheel.reel10, graphics.big_wheel.reel100)
                self.game.coils.registerDown.pulse()
                number -= 1
                self.delay(name="display", delay=0, handler=graphics.big_wheel.display, param=self)
                self.cancel_delayed(name="replay_reset")
        else: 
            if self.game.replays > 0:
                self.game.replays -= 1
                graphics.replay_step_down(self.game.replays, graphics.big_wheel.reel1, graphics.big_wheel.reel10, graphics.big_wheel.reel100)
                self.delay(name="display", delay=0.1, handler=graphics.big_wheel.display, param=self)
            self.game.coils.registerDown.pulse()

    def sw_orange_active(self, sw):
        if self.game.switches.drawer.is_active():
            if self.game.start.status == False:
                if self.game.ball_count.position >= 3:
                    if self.game.three.status == True or self.game.four.status == True or self.game.five.status == True:
                        if self.game.replay_counter.position == 0:
                            if self.game.winner > 0:
                                if self.game.double.status == True and self.game.ball_count.position == 3:
                                    self.game.spotting.spin()
                                    self.game.mixer1.spin()
                                    self.game.mixer2.spin()
                                    self.game.mixer3.spin()
                                    self.game.special.engage(self.game)
                                    self.game.all_advantages.disengage()
                                    self.game.odds_only.disengage()
                                    self.game.features.disengage()
                                    self.game.double_double.engage(self.game)
                                    self.regular_play(red_letter=1)
                                    self.game.double_colors.step()
                                    self.game.reflex.decrease()
                                    self.delay(name="display", delay=0.1, handler=graphics.big_wheel.display, param=self)
                                elif self.game.double.status == False:
                                    self.game.spotting.spin()
                                    self.game.mixer1.spin()
                                    self.game.mixer2.spin()
                                    self.game.mixer3.spin()
                                    self.game.special.engage(self.game)
                                    self.game.all_advantages.disengage()
                                    self.game.odds_only.disengage()
                                    self.game.features.disengage()
                                    self.game.double.engage(self.game)
                                    self.regular_play(red_letter=1)
                                    self.game.double_colors.step()
                                    self.game.reflex.decrease()
                                    self.delay(name="display", delay=0.1, handler=graphics.big_wheel.display, param=self)


    def sw_white_active(self, sw):
        if self.game.switches.drawer.is_active():
            if self.game.double_colors.position >= 1 and self.game.ball_count.position == 0 and self.game.start.status == True:
                self.game.special.engage(self.game)
                if self.game.replays > 0 or self.game.switches.freeplay.is_active():
                    self.game.features.disengage()
                    self.game.all_advantages.disengage()
                    self.game.odds_only.disengage()
                    self.regular_play()
            self.delay(name="display", delay=0.1, handler=graphics.big_wheel.display, param=self)


    def sw_yellow_active(self, sw):
        if self.game.switches.drawer.is_inactive():
            if self.game.start.status == False:
                if self.game.ball_count.position >= 3:
                    if self.game.three.status == True or self.game.four.status == True or self.game.five.status == True:
                        if self.game.replay_counter.position == 0:
                            if self.game.winner > 0:
                                if self.game.double.status == True and self.game.ball_count.position == 3:
                                    self.game.special.engage(self.game)
                                    self.game.all_advantages.disengage()
                                    self.game.odds_only.disengage()
                                    self.game.features.disengage()
                                    self.game.double_double.engage(self.game)
                                    self.regular_play(red_letter=1)
                                    self.game.double_colors.step()
                                    self.delay(name="display", delay=0.1, handler=graphics.big_wheel.display, param=self)
                                elif self.game.double.status == False:
                                    self.game.special.engage(self.game)
                                    self.game.all_advantages.disengage()
                                    self.game.odds_only.disengage()
                                    self.game.features.disengage()
                                    self.game.double.engage(self.game)
                                    self.regular_play(red_letter=1)
                                    self.game.double_colors.step()
                                    self.game.reflex.decrease()
                                    self.delay(name="display", delay=0.1, handler=graphics.big_wheel.display, param=self)
                                if self.game.double_colors.position >= 1 and self.game.ball_count.position == 0 and self.game.start.status == True:
                                    self.game.special.engage(self.game)
                                    if self.game.replays > 0 or self.game.switches.freeplay.is_active():
                                        self.game.features.disengage()
                                        self.game.all_advantages.disengage()
                                        self.game.odds_only.disengage()
                                        self.regular_play()
                    self.delay(name="display", delay=0.1, handler=graphics.big_wheel.display, param=self)

    def search(self, score=0):
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
       
        for i in range(0, 5):
            self.r = self.closed_search_relays(self.game.searchdisc.position)
            self.game.searchdisc.spin()
            self.wipers = self.r[0]
            self.red = self.r[1]
            self.yellow = self.r[2]
            self.green = self.r[3]
            self.striped_green = self.r[4]

            # From here, I need to determine based on the value of r, whether to latch the search index and score. 
            # I need to determine the best winner on each card.  To do this, I must compare the position of the replay counter before
            # determining the winner. Reminder that my replay counters are a 1:1 representation.

            self.match = []
            relays = 0
            for key in self.wipers:
                for number in self.holes:
                    if number == key:
                        self.match.append(self.wipers[key])
                        relays += 1
                        #TODO Play sound for each relay closure.
                        s = relays 
                        if s >= 2:
                            self.add_winner(s, self.red, self.yellow, self.green, self.striped_green)
                            if score == 1:
                                self.find_winner(s, self.red, self.yellow, self.green, self.striped_green, self.game.winner)
                            break
                            
    
    def add_winner(self, relays, red, yellow, green, striped_green):
        if self.game.odds.position == 1:
            redthreeodds = 9
            yellowfourodds = 9
            greenfiveodds = 9
            yellowthreeodds = 6
            greenfourodds = 6
            greenthreeodds = 3
        elif self.game.odds.position == 2:
            redthreeodds = 12
            yellowfourodds = 12
            greenfiveodds = 12
            yellowthreeodds = 9
            greenfourodds = 9
            greenthreeodds = 6
        elif self.game.odds.position == 3:
            redthreeodds = 18
            yellowfourodds = 18
            greenfiveodds = 18
            yellowthreeodds = 12
            greenfourodds = 12
            greenthreeodds = 9
        elif self.game.odds.position == 4:
            redthreeodds = 24
            yellowfourodds = 24
            greenfiveodds = 24
            yellowthreeodds = 18
            greenfourodds = 18
            greenthreeodds = 12
        elif self.game.odds.position == 5:
            redthreeodds = 36
            yellowfourodds = 36
            greenfiveodds = 36
            yellowthreeodds = 24
            greenfourodds = 24
            greenthreeodds = 18
        elif self.game.odds.position == 6:
            redthreeodds = 48
            yellowfourodds = 48
            greenfiveodds = 48
            yellowthreeodds = 36
            greenfourodds = 36
            greenthreeodds = 24
        elif self.game.odds.position == 7:
            redthreeodds = 72
            yellowfourodds = 72
            greenfiveodds = 72
            yellowthreeodds = 48
            greenfourodds = 48
            greenthreeodds = 36
        elif self.game.odds.position == 8:
            redthreeodds = 144
            yellowfourodds = 144
            greenfiveodds = 144
            yellowthreeodds = 100
            greenfourodds = 100
            greenthreeodds = 64
        elif self.game.odds.position == 9:
            redthreeodds = 200
            yellowfourodds = 200
            greenfiveodds = 200
            yellowthreeodds = 144
            greenfourodds = 144
            greenthreeodds = 100

        if relays == 3:
            if red == 1:
                if self.game.winner < redthreeodds:
                    self.game.winner += redthreeodds - self.game.winner
                    self.game.three.engage(self.game)
            if yellow == 1:
                if self.game.winner < yellowthreeodds:
                    self.game.winner += yellowthreeodds - self.game.winner
                    self.game.three.engage(self.game)
            if green == 1:
                if self.game.winner < greenthreeodds:
                    self.game.winner += greenthreeodds - self.game.winner
                    self.game.three.engage(self.game)
        if relays == 4:
            if yellow == 1:
                if self.game.winner < yellowfourodds:
                    self.game.winner += yellowfourodds - self.game.winner
                    self.game.three.disengage()
                    self.game.four.engage(self.game)
            if green == 1:
                if self.game.winner < greenfourodds:
                    self.game.winner += greenfourodds - self.game.winner
                    self.game.three.disengage()
                    self.game.four.engage(self.game)
        if relays == 5:
            if green == 1:
                if self.game.winner < greenfiveodds:
                    self.game.winner += greenfiveodds - self.game.winner
                    self.game.three.disengage()
                    self.game.four.disengage()
                    self.game.five.engage(self.game)

    def find_winner(self, relays, red, yellow, green, striped_green, winner_amount=0, ok_winner=0, red_letter_winner=0):
        if self.game.search_index.status == False and self.game.replays < 899:
            redthreeodds =    winner_amount
            yellowfourodds =  winner_amount
            greenfiveodds =   winner_amount
            yellowthreeodds = winner_amount
            greenfourodds =   winner_amount
            greenthreeodds =  winner_amount

            if self.game.double.status == True and self.game.double_double.status == False:
                redthreeodds =    winner_amount * 2
                yellowfourodds =  winner_amount * 2
                greenfiveodds =   winner_amount * 2
                yellowthreeodds = winner_amount * 2
                greenfourodds =   winner_amount * 2
                greenthreeodds =  winner_amount * 2
            if self.game.double.status == True and self.game.double_double.status == True:
                redthreeodds =    winner_amount * 2 * 2
                yellowfourodds =  winner_amount * 2 * 2
                greenfiveodds =   winner_amount * 2 * 2
                yellowthreeodds = winner_amount * 2 * 2
                greenfourodds =   winner_amount * 2 * 2
                greenthreeodds =  winner_amount * 2 * 2


            if relays == 2:
                if winner_amount > 0 and self.game.double.status == True:
                    if self.game.double_colors.position >= 1:
                        if red == 1:
                            if self.game.search_index.status == False:
                                if self.game.replay_counter.position < redthreeodds:
                                    self.game.search_index.engage(self.game)
                                    self.all_replay_step_up(redthreeodds - self.game.replay_counter.position)
                    if self.game.double_colors.position >= 4:
                        if yellow == 1:
                            if self.game.search_index.status == False:
                                if self.game.replay_counter.position < yellowthreeodds:
                                    self.game.search_index.engage(self.game)
                                    self.all_replay_step_up(yellowthreeodds - self.game.replay_counter.position)
                    if self.game.double_colors.position >= 7:
                        if green == 1:
                            if self.game.search_index.status == False:
                                if self.game.replay_counter.position < greenthreeodds:
                                    self.game.search_index.engage(self.game)
                                    self.all_replay_step_up(greenthreeodds - self.game.replay_counter.position)
                    if self.game.double_colors.position >= 10:
                        if striped_green == 1:
                            if self.game.search_index.status == False:
                                if self.game.replay_counter.position < greenthreeodds:
                                    self.game.search_index.engage(self.game)
                                    self.all_replay_step_up(greenthreeodds - self.game.replay_counter.position)
            if self.game.double_colors.position == 0:
                if relays == 3:
                    if red == 1:
                        if self.game.search_index.status == False:
                            if self.game.replay_counter.position < redthreeodds:
                                self.game.search_index.engage(self.game)
                                self.all_replay_step_up(redthreeodds - self.game.replay_counter.position)
                    if yellow == 1:
                        if self.game.search_index.status == False:
                            if self.game.replay_counter.position < yellowthreeodds:
                                self.game.search_index.engage(self.game)
                                self.all_replay_step_up(yellowthreeodds - self.game.replay_counter.position)
                    if green == 1:
                        if self.game.search_index.status == False:
                            if self.game.replay_counter.position < greenthreeodds:
                                self.game.search_index.engage(self.game)
                                self.all_replay_step_up(greenthreeodds - self.game.replay_counter.position)
                if relays == 4:
                    if yellow == 1:
                        if self.game.search_index.status == False:
                            if self.game.replay_counter.position < yellowfourodds:
                                self.game.search_index.engage(self.game)
                                self.all_replay_step_up(yellowfourodds - self.game.replay_counter.position)
                    if green == 1:
                        if self.game.search_index.status == False:
                            if self.game.replay_counter.position < greenfourodds:
                                self.game.search_index.engage(self.game)
                                self.all_replay_step_up(greenfourodds - self.game.replay_counter.position)
                if relays == 5:
                    if green == 1:
                        if self.game.search_index.status == False:
                            if self.game.replay_counter.position < greenfiveodds:
                                self.game.search_index.engage(self.game)
                                self.all_replay_step_up(greenfiveodds - self.game.replay_counter.position)

    def all_replay_step_up(self, number):
        self.game.sound.stop('search')
        if number >= 1:
            self.game.replay_counter.step()
            number -= 1
            self.replay_step_up()
            if self.game.replays == 899:
                number = 0
            self.delay(name="replay_step_up", delay=0.25, handler=self.all_replay_step_up, param=number)
        else:
            self.game.search_index.disengage()
            self.game.double.disengage()
            self.game.double_double.disengage()
            self.delay(name="display", delay=0.1, handler=graphics.big_wheel.display, param=self)
            self.search()

    def replay_step_up(self):
        if self.game.replays < 899:
            self.game.replays += 1
            graphics.replay_step_up(self.game.replays, graphics.big_wheel.reel1, graphics.big_wheel.reel10, graphics.big_wheel.reel100)
        self.game.coils.registerUp.pulse()
        self.game.reflex.increase()
        graphics.big_wheel.display(self)

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
        striped_green = False

        self.pos[0] = {}
        if self.game.ring.position == 0:
            self.pos[1] = {10:1, 17:2, 7:3, 16:4}
            self.pos[2] = {6:1, 18:2}
            self.pos[3] = {13:1, 19:2, 3:3, 14:4, 20:5}
            self.pos[4] = {8:1, 4:2, 9:3}
        elif self.game.ring.position == 1:
            self.pos[1] = {17:1, 7:2, 16:3, 5:4}
            self.pos[2] = {6:1, 13:2}
            self.pos[3] = {19:1, 3:2, 14:3, 20:4, 1:5}
            self.pos[4] = {4:1, 9:2, 11:3}
        elif self.game.ring.position == 2:
            self.pos[1] = {7:1, 16:2, 5:3, 12:4}
            self.pos[2] = {13:1, 19:2}
            self.pos[3] = {3:1, 14:2, 20:3, 1:4, 15:5}
            self.pos[4] = {9:1, 11:2, 2:3}
        elif self.game.ring.position == 3:
            self.pos[1] = {16:1, 5:2, 12:3, 18:4}
            self.pos[2] = {19:1, 3:2}
            self.pos[3] = {14:1, 20:2, 1:3, 15:4, 8:5}
            self.pos[4] = {11:1, 2:2, 10:3}
        elif self.game.ring.position == 4:
            self.pos[1] = {5:1, 12:2, 18:3, 6:4}
            self.pos[2] = {3:1, 14:2}
            self.pos[3] = {20:1, 1:2, 15:3, 8:4, 4:5}
            self.pos[4] = {2:1, 10:2, 17:3}
        elif self.game.ring.position == 5:
            self.pos[1] = {12:1, 18:2, 6:3, 13:4}
            self.pos[2] = {14:1, 20:2}
            self.pos[3] = {1:1, 15:2, 8:3, 4:4, 9:5}
            self.pos[4] = {10:1, 17:2, 7:3}
        elif self.game.ring.position == 6:
            self.pos[1] = {18:1, 6:2, 13:3, 19:4}
            self.pos[2] = {20:1, 1:2}
            self.pos[3] = {15:1, 8:2, 4:3, 9:4, 11:5}
            self.pos[4] = {17:1, 7:2, 16:3}
        elif self.game.ring.position == 7:
            self.pos[1] = {6:1, 13:2, 19:3, 3:4}
            self.pos[2] = {1:1, 15:2}
            self.pos[3] = {8:1, 4:2, 9:3, 11:4, 2:5}
            self.pos[4] = {7:1, 16:2, 5:3}
        elif self.game.ring.position == 8:
            self.pos[1] = {13:1, 19:2, 3:3, 14:4}
            self.pos[2] = {15:1, 8:2}
            self.pos[3] = {4:1, 9:2, 11:3, 2:4, 10:5}
            self.pos[4] = {16:1, 5:2, 12:3}
        elif self.game.ring.position == 9:
            self.pos[1] = {19:1, 3:2, 14:3, 20:4}
            self.pos[2] = {8:1, 4:2}
            self.pos[3] = {9:1, 11:2, 2:3, 10:4, 17:5}
            self.pos[4] = {5:1, 12:2, 18:3}
        elif self.game.ring.position == 10:
            self.pos[1] = {3:1, 14:2, 20:3, 1:4}
            self.pos[2] = {4:1, 9:2}
            self.pos[3] = {11:1, 2:2, 10:3, 17:4, 7:5}
            self.pos[4] = {12:1, 18:2, 6:3}
        elif self.game.ring.position == 11:
            self.pos[1] = {14:1, 20:2, 1:3, 15:4}
            self.pos[2] = {9:1, 11:2}
            self.pos[3] = {2:1, 10:2, 17:3, 7:4, 16:5}
            self.pos[4] = {18:1, 6:2, 13:3}
        elif self.game.ring.position == 12:
            self.pos[1] = {20:1, 1:2, 15:3, 8:4}
            self.pos[2] = {11:1, 2:2}
            self.pos[3] = {10:1, 17:2, 7:3, 16:4, 5:5}
            self.pos[4] = {6:1, 13:2, 19:3}
        elif self.game.ring.position == 13:
            self.pos[1] = {1:1, 15:2, 8:3, 4:4}
            self.pos[2] = {2:1, 10:2}
            self.pos[3] = {17:1, 7:2, 16:3, 5:4, 12:5}
            self.pos[4] = {13:1, 19:2, 3:3}
        elif self.game.ring.position == 14:
            self.pos[1] = {15:1, 8:2, 4:3, 9:5}
            self.pos[2] = {10:1, 17:2}
            self.pos[3] = {7:1, 16:2, 5:3, 12:4, 18:5}
            self.pos[4] = {19:1, 3:2, 14:3}
        elif self.game.ring.position == 15:
            self.pos[1] = {8:1, 4:2, 9:3, 11:4}
            self.pos[2] = {17:1, 7:2}
            self.pos[3] = {16:1, 5:2, 12:3, 18:4, 6:5}
            self.pos[4] = {3:1, 14:2, 20:3}
        elif self.game.ring.position == 16:
            self.pos[1] = {4:1, 9:2, 11:3, 2:4}
            self.pos[2] = {7:1, 16:2}
            self.pos[3] = {5:1, 12:2, 18:3, 6:4, 13:5}
            self.pos[4] = {14:1, 20:2, 1:3}
        elif self.game.ring.position == 17:
            self.pos[1] = {9:1, 11:2, 2:3, 10:4}
            self.pos[2] = {16:1, 5:2}
            self.pos[3] = {12:1, 18:2, 6:3, 13:4, 19:5}
            self.pos[4] = {20:1, 1:2, 15:3}
        elif self.game.ring.position == 18:
            self.pos[1] = {11:1, 2:2, 10:3, 17:4}
            self.pos[2] = {5:1, 12:2}
            self.pos[3] = {18:1, 6:2, 13:3, 19:4, 3:5}
            self.pos[4] = {1:1, 15:2, 8:3}
        elif self.game.ring.position == 19:
            self.pos[1] = {2:1, 10:2, 17:3, 7:4}
            self.pos[2] = {12:1, 18:2}
            self.pos[3] = {6:1, 13:2, 19:3, 3:4, 14:5}
            self.pos[4] = {15:1, 8:2, 4:3}

        if rivets == 1:
            yellow = True
        if rivets == 2:
            striped_green = True
        if rivets == 3:
            green = True
        if rivets == 4:
            red = True
                
        return (self.pos[rivets], red, yellow, green, striped_green)

    
    def scan_all(self):
        #Animate scanning of everything - this happens through the spotting disc
        self.all_probability()

    def all_probability(self):
        mix1 = self.game.mixer1.connected_rivet()
        if self.game.reflex.connected_rivet() == 0:
            #Worst position for reflex - requires mixer1 to be in the three liberal positions for the connection of the wires bypassing the reflex.
            if mix1 in [2,21,17]:
                self.scan_odds()
                if self.game.odds.position > 0:
                    self.scan_features()
                else:
                    self.game.odds.step()
        if self.game.reflex.connected_rivet() == 1 and (mix1 in [2,21,17,4,23]):
            self.scan_odds()
            if self.game.odds.position > 0:
                self.scan_features()
            else:
                self.game.odds.step()
        elif self.game.reflex.connected_rivet() == 2 and (mix1 in [2,21,17,4,23,12]):
            self.scan_odds()
            if self.game.odds.position > 0:
                self.scan_features()
            else:
                self.game.odds.step()
        elif self.game.reflex.connected_rivet() == 3 and (mix1 in [2,21,17,4,23,12,1,10,19]):
            self.scan_odds()
            if self.game.odds.position > 0:
                self.scan_features()
            else:
                self.game.odds.step()
        elif self.game.reflex.connected_rivet() == 4 and (mix1 in [2,21,17,4,23,12,1,10,19,18]):
            self.scan_odds()
            if self.game.odds.position > 0:
                self.scan_features()
            else:
                self.game.odds.step()
        else:
            self.game.odds.step()
            self.delay(name="display", delay=0.1, handler=graphics.big_wheel.display, param=self)

    def check_mixer2(self, sel):
        mix2 = self.game.mixer2.position
        ml = self.game.mystic_lines.position
        sf = self.game.selection_feature.position
        if ml < 4:
            if mix2 in [16,20,23,5,19,1,2,3,4,12,13,14,15,17,18,7,8,9,10,21]:
                if sf <= 1:
                    return 1
        elif ml in [4,5,6]:
            if mix2 in [8,17,23,7,9,19,0,4]:
                if sf in [2,3]:
                    return 1
        elif ml in [7,8,9]:
            if mix2 in [6,16,22,11]:
                if sf in [4,5]:
                    return 1
        elif ml in [10]:
            if mix2 in [7,19,5,21]:
                if sf in [6,7]:
                    return 1
        else:
            return 0

    def scan_odds(self):
        if self.game.odds.position < 2:
            self.game.odds.step()
            return
        sd = self.game.spotting.position
        if sd == 31:
            if self.game.odds.position in [2,3,4,5]:
                self.game.odds.step()
        if sd in [0,34]:
            if self.game.odds.position in [6,7,8,9]:
                self.game.odds.step()
        if sd in [7,19,43] and self.game.odds_only.status == True:
            if self.game.odds.position in [6,7,8,9]:
                self.game.odds.step()
        if sd in [9,11,18]:
            if self.game.cu:
                self.step_odds(2)
        if sd in [10,12,13,15,16,28,30,37,44,45,48]:
            if self.game.odds_only.status == True:
                if self.game.cu:
                    self.step_odds(3)

    def step_odds(self, number):
        if number > 0:
            self.game.odds.step()
            self.delay(name="display", delay=0.1, handler=graphics.big_wheel.display, param=self)
            number -= 1
            self.delay(name="step_odds", delay=0.1, handler=self.step_odds, param=number)
    
    def scan_features(self):
        p = self.features_probability()

    def scan_special(self):
        sd = self.game.spotting.position
        if self.game.double_colors.position < 3:
            self.game.double_colors.step()
        else:
            m = self.check_mixer3()
            if self.game.mixer3_relay.status == True:
                self.game.mixer3_relay.disengage()
                if self.game.cu:
                    if sd in [1,5,6,7,8,9,10,11,14,17,18,19,20,21,22,25,26,38,44]:
                        self.game.double_colors.step()
        self.delay(name="display", delay=0.1, handler=graphics.big_wheel.display, param=self)

    def check_mixer3(self):
        m3 = self.game.mixer3.position
        m1 = self.game.mixer1.position
        if m1 in [0,2,3,4,5,6,7,9,10,11]:
            if self.game.odds.position == 0:
                self.game.mixer3_relay.engage(self.game)
        if m3 in [1,7,9,15,17,19,21,23]:
            if self.game.odds.position in [1,2,3]:
                self.game.mixer3_relay.engage(self.game)
        if m3 in [1,2,3,5,7,9,10]:
            if self.game.odds.position == 4:
                self.game.mixer3_relay.engage(self.game)
        if m3 in [6,17,19,20]:
            if self.game.odds.position == 5:
                self.game.mixer3_relay.engage(self.game)
        if m3 in [13,14]:
            if self.game.odds.position == 6:
                self.game.mixer3_relay.engage(self.game)
        if m3 == 20:
            if self.game.odds.position == 7:
                self.game.mixer3_relay.engage(self.game)
        if self.game.odds.position > 3:
            if self.game.cu:
                self.game.mixer3_relay.engage(self.game)
            else:
                self.game.mixer3_relay.engage(self.game)
        if m3 in [1,3,5,7,9]:
            if self.game.odds.position in [1,2,3]:
                self.game.mixer3_relay.engage(self.game)
        if m3 in [4,12,13,15,21,23]:
            if self.game.odds.position == 4:
                self.game.mixer3_relay.engage(self.game)
        if m3 in [2,10,14,16]:
            if self.game.odds.position == 5:
                self.game.mixer3_relay.engage(self.game)
        if m3 in [6,17,19,20]:
            if self.game.odds.position == 6:
                self.game.mixer3_relay.engage(self.game)
        if m3 == 22:
            if self.game.odds.position == 7:
                self.game.mixer3_relay.engage(self.game)
        if self.game.odds.position > 3:
            self.game.mixer3_relay.engage(self.game)
        if m3 in [7,9,11,13,15]:
            if self.game.odds.position in [1,2,3]:
                self.game.mixer3_relay.engage(self.game)
        if m3 in [3,5,17,19,21,23]:
            if self.game.odds.position == 4:
                self.game.mixer3_relay.engage(self.game)
        if m3 in [6,8,10]:
            if self.game.odds.position == 5:
                self.game.mixer3_relay.engage(self.game)
        if m3 in [1,2,18,20]:
            if self.game.odds.position == 6:
                self.game.mixer3_relay.engage(self.game)
        if m3 == 22:
            if self.game.odds.position == 7:
                self.game.mixer3_relay.engage(self.game)
        if self.game.odds.position > 3:
            self.game.mixer3_relay.engage(self.game)

    def features_probability(self):
        self.check_mixer3()
        if self.game.mixer3_relay.status == True:
            self.features_spotting()
            self.game.mixer3_relay.disengage()
        else:
            self.game.mixer3_relay.disengage()

    def features_spotting(self):
        sd = self.game.spotting.position
        if sd in [11,13,20,24,29,37]:
            if self.game.features.status == True:
                self.step_wheel(9)
        if sd in [41]:
            self.step_wheel(9)
        if sd in [1,20,21,40]:
            if self.game.selection_feature.position < 5:
                self.game.wheel.step()
        if sd in [28]:
            if self.game.selection_feature.position in [5,6,7]:
                self.game.wheel.step()
        if sd in [38,42]:
            if self.game.features.status == True:
                if self.game.selection_feature.position in [5,6,7]:
                    self.game.wheel.step()
        if sd in [6,11,12,19,20,31,35,44]:
            if self.game.selection_feature.position >= 7:
                self.game.wheel.step()
        if sd in [0,7,15,36,45]:
            self.game.selection_feature.step()
        if sd == 4:
            if self.game.wheel.position < 9:
                if self.game.cu:
                    self.step_selection(9)
        if sd in [22,23,39]:
            if self.game.wheel.position in [2,3]:
                self.step_selection(7)
        if sd in [5,6,11,18,19,30,34]:
            if self.game.features.status == True:
                if self.game.wheel.position in [4,5]:
                    self.step_selection(7)
        if sd in [24,31]:
            self.step_selection(7)
        if sd in [16,22,27,37]:
            if self.game.wheel.position in [4,5]:
                self.step_selection(7)
        if sd in [14,15,37]:
            self.step_selection(7)

        if self.game.selection_feature.position == 0:
            self.game.selection_feature.step()

    def step_wheel(self, number):
        if number >= 1:
            self.game.wheel.step()
            number -= 1
            self.delay(name="display", delay=0.1, handler=graphics.big_wheel.display, param=self)
            self.delay(name="step_wheel", delay=0.1, handler=self.step_wheel, param=number)


    def step_selection(self, number):
        if number >= 1:
            self.game.selection_feature.step()
            self.check_selection()
            number -= 1
            self.delay(name="display", delay=0.1, handler=graphics.big_wheel.display, param=self)
            self.delay(name="step_sc", delay=0.1, handler=self.step_selection, param=number)

    def animate_odds_scan(self, args):
        start = args[0]
        diff = args[1]
        num = args[2]
        if start + num >= 50:
            start = 0
        if diff >= 0:
            num = num + 1
            graphics.big_wheel.odds_animation([self, start + num])
            self.cancel_delayed(name="display")
            diff = diff - 1
            args = [start,diff,num]
            self.delay(name="odds_animation", delay=0.08, handler=self.animate_odds_scan, param=args)
        else:
            self.cancel_delayed(name="odds_animation")
            self.delay(name="display", delay=0.1, handler=graphics.big_wheel.display, param=self)
            self.scan_odds()

    def animate_wheel_right(self, args):
        self.game = args[0]
        num = args[1]
        if num >= 0:
            graphics.big_wheel.wheel_animation([self, num, "right"])
            self.cancel_delayed(name="display")
            num = num - 1
            args = [self.game,num,"right"]
            self.delay(name="right_animation", delay=0.005, handler=self.animate_wheel_right, param=args)
        else:
            self.cancel_delayed(name="right_animation")
            self.delay(name="display", delay=0.1, handler=graphics.big_wheel.display, param=self)

    def animate_wheel_left(self, args):
        self.game = args[0]
        num = args[1]
        if num >= 0:
            graphics.big_wheel.wheel_animation([self, num, "left"])
            self.cancel_delayed(name="display")
            num = num - 1
            args = [self.game,num,"left"]
            self.delay(name="left_animation", delay=0.005, handler=self.animate_wheel_left, param=args)
        else:
            self.cancel_delayed(name="left_animation")
            self.delay(name="display", delay=0.1, handler=graphics.big_wheel.display, param=self)

    def animate_features_scan(self, args):
        start = args[0]
        diff = args[1]
        num = args[2]
        if start + num >= 50:
            start = 0
        if diff >= 0:
            num = num + 1
            graphics.big_wheel.feature_animation([self, start + num])
            self.cancel_delayed(name="display")
            diff = diff - 1
            args = [start,diff,num]
            self.delay(name="feature_animation", delay=0.08, handler=self.animate_features_scan, param=args)
        else:
            self.cancel_delayed(name="feature_animation")
            self.delay(name="display", delay=0.1, handler=graphics.big_wheel.display, param=self)
            self.scan_features()

    def animate_double_scan(self, args):
        start = args[0]
        diff = args[1]
        num = args[2]
        if start + num >= 50:
            start = 0
        if diff >= 0:
            num = num + 1
            graphics.big_wheel.draw_double_animation([self, start + num])
            self.cancel_delayed(name="display")
            diff = diff - 1
            args = [start,diff,num]
            self.delay(name="double_animation", delay=0.08, handler=self.animate_double_scan, param=args)
        else:
            self.cancel_delayed(name="double_animation")
            self.delay(name="display", delay=0.1, handler=graphics.big_wheel.display, param=self)
            self.scan_special()


    def animate_both(self, args):
        start = args[0]
        diff = args[1]
        num = args[2]
        if start + num >= 50:
            start = 0
        if diff >= 0:
            num = num + 1
            graphics.big_wheel.both_animation([self, start + num])
            self.cancel_delayed(name="display")
            diff = diff - 1
            args = [start,diff,num]
            self.delay(name="both_animation", delay=0.08, handler=self.animate_both, param=args)
        else:
            self.cancel_delayed(name="both_animation")
            self.delay(name="display", delay=0.1, handler=graphics.big_wheel.display, param=self)
            self.scan_all()

    # Define reset as the knock-off, anti-cheat relay disabled, and replay reset enabled.  Motors turn while credits are knocked off.
    # When meter reaches zero and the zero limit switch is hit, turn off motor sound and leave backglass gi on, but with tilt displayed.

    def startup(self):        
        # Every bingo requires the meter to register '0' 
        # before allowing coin entry --
        # also needs to show a plain 'off' backglass.
        self.game.anti_cheat.engage(self.game)
        self.tilt_actions()
        self.game.all_advantages.engage(self.game)


class BigWheel(procgame.game.BasicGame):
    """ Big Wheel was the first 20 hole with the Wheel Unit """
    def __init__(self, machine_type):
        super(BigWheel, self).__init__(machine_type)
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

        self.searchdisc = units.Search("searchdisc", 4)

        #Search relays
        self.s1 = units.Relay("s1")
        self.s2 = units.Relay("s2")
        self.s3 = units.Relay("s3")
        self.s4 = units.Relay("s4")
        self.s5 = units.Relay("s5")
        self.search_index = units.Relay("search_index")

        #Pic-a-play
        self.all_advantages = units.Relay("all_advantages")
        self.odds_only = units.Relay("odds_only")
        self.features = units.Relay("features")
        self.special = units.Relay("special")

        #Odds steppers
        self.odds = units.Stepper("odds", 9, 'big_wheel')

        #Replay Counter
        self.replay_counter = units.Stepper("replay_counter", 1800)
      
        self.wheel = units.Stepper("wheel", 9)

        self.ring = units.Stepper("ring", 19, 'big_wheel', 'continuous')

        self.selection_feature = units.Stepper("selection_feature", 9)

        #Initialize stepper units used to keep track of features or timing.
        self.timer = units.Stepper("timer", 8)
        self.ball_count = units.Stepper("ball_count", 8)

        # Initialize reflex(es) and mixers unique to this game
        self.reflex = units.Reflex("primary", 200)

        #This is a disc which has 50 positions
        #and will randomly complete paths through the various mixers to allow for odds or feature step.
        self.spotting = units.Spotting("spotting", 50)

        #Check for status of the replay register zero switch.  If positive
        #and machine is just powered on, this will zero out the replays.
        self.replay_reset = units.Relay("replay_reset")
        
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

        self.selector = units.Stepper("selector", 1)

        self.three = units.Relay("three")
        self.four = units.Relay("four")
        self.five = units.Relay("five")
        self.winner = 0

        self.double = units.Relay("double")
        self.double_double = units.Relay("double_double")
        self.double_colors = units.Stepper("double_colors", 10)

        self.yellow_star = units.Relay("yellow_star")
        self.red_star = units.Relay("red_star")
        
        self.mixer2_relay = units.Relay("mixer2_relay")
        self.mixer3_relay = units.Relay("mixer3_relay")

        self.replays = 0
        self.returned = False

    def reset(self):
        super(BigWheel, self).reset()
        self.logger = logging.getLogger('game')
        self.load_config('bingo.yaml')
        
        main_mode = SinglecardBingo(self)
        self.modes.add(main_mode)
        
game = BigWheel(machine_type='pdb')
game.reset()
game.run_loop()
