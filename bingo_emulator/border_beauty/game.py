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
from bingo_emulator.graphics.border_beauty import *

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
                self.game.eb_play.disengage()
                self.game.features.disengage()
                self.regular_play()
            elif self.game.features.status == True:
                self.game.odds_only.disengage()
                self.game.eb_play.disengage()
                self.game.all_advantages.disengage()
                self.regular_play()
            elif self.game.odds_only.status == True:
                self.game.eb_play.disengage()
                self.game.features.disengage()
                self.game.all_advantages.disengage()
                self.regular_play()
        elif self.game.eb_play.status == True:
            self.game.sound.play('eb_search')
            if self.game.timer.position >= 8:
                self.game.timer.reset()
                self.game.sound.play_music('motor', -1)
                self.timeout_actions()
            self.game.features.disengage()
            self.game.all_advantages.disengage()
            self.game.odds_only.disengage()
            self.game.cu = not self.game.cu
            begin = self.game.spotting.position
            self.game.spotting.spin()
            self.game.mixer1.spin()
            self.game.mixer2.spin()
            self.game.mixer3.spin()
            self.game.mixer4.spin()
            self.game.coils.counter.pulse()
            self.animate_eb_scan([begin,self.game.spotting.movement_amount,self.game.spotting.movement_amount])
        else:
            self.game.all_advantages.engage(self.game)
            self.game.odds_only.disengage()
            self.game.eb_play.disengage()
            self.game.features.disengage()
            self.regular_play()
        self.delay(name="display", delay=0.1, handler=graphics.border_beauty.display, param=self)

    def sw_startButton_active(self, sw):
        self.cancel_delayed(name="both_animation")
        self.cancel_delayed(name="odds_animation")
        self.cancel_delayed(name="feature_animation")
        self.cancel_delayed(name="blink")
        self.game.eb_play.disengage()
        self.game.odds_only.disengage()
        self.game.features.disengage()
        self.game.all_advantages.engage(self.game)
        self.delay(name="display", delay=0.1, handler=graphics.border_beauty.display, param=self)
        if self.game.replays > 0 or self.game.switches.freeplay.is_active():
            self.game.tilt.disengage()
            self.regular_play()
        self.delay(name="display", delay=0.1, handler=graphics.border_beauty.display, param=self)

    def sw_blue_active(self, sw):
        self.cancel_delayed(name="both_animation")
        self.cancel_delayed(name="odds_animation")
        self.cancel_delayed(name="feature_animation")
        if self.game.start.status == True:
            self.game.features.disengage()
            self.game.all_advantages.disengage()
            self.game.eb_play.disengage()
            self.game.odds_only.engage(self.game)
        if self.game.replays > 0 or self.game.switches.freeplay.is_active():
            if self.game.start.status == False:
                self.delay(name="startup", delay=0.1, handler=self.sw_startButton_active, param=sw)
            if self.game.odds_only.status == True:
                self.delay(name="display", delay=0.1, handler=graphics.border_beauty.display, param=self)
                self.regular_play()
                self.delay(name="display", delay=0.1, handler=graphics.border_beauty.display, param=self)
        self.delay(name="display", delay=0.1, handler=graphics.border_beauty.display, param=self)

    def sw_green_active(self, sw):
        self.cancel_delayed(name="both_animation")
        self.cancel_delayed(name="odds_animation")
        self.cancel_delayed(name="feature_animation")
        if self.game.start.status == True:
            self.game.features.engage(self.game)
            self.game.all_advantages.disengage()
            self.game.odds_only.disengage()
            self.game.eb_play.disengage()
        if self.game.replays > 0 or self.game.switches.freeplay.is_active():
            if self.game.start.status == False:
                self.delay(name="startup", delay=0.1, handler=self.sw_startButton_active, param=sw)
            if self.game.features.status == True:
                self.delay(name="display", delay=0.1, handler=graphics.border_beauty.display, param=self)
                self.regular_play()
                self.delay(name="display", delay=0.1, handler=graphics.border_beauty.display, param=self)
        self.delay(name="display", delay=0.1, handler=graphics.border_beauty.display, param=self)

    def sw_enter_active(self, sw):
        if self.game.switches.left.is_active() and self.game.switches.right.is_active():
            self.game.end_run_loop()
            os.system("/home/nbaldridge/proc/bingo_emulator/start_game.sh border_beauty")
        else:
            if self.game.ball_count.position >= 4:
                self.game.sound.stop_music()
                self.game.sound.play_music('motor', -1)
                self.game.timer.reset()
                if self.game.search_index.status == False:
                    self.search()
                    self.timeout_actions()
            if self.game.switches.drawer.is_inactive():
                if self.game.ball_count.position > 0:
                    max_ball = 0
                    if self.game.selection_feature.position < 7:
                        max_ball = 4
                    elif self.game.selection_feature.position < 8:
                        max_ball = 5
                    else:
                        if self.game.selection_feature.position == 9:
                            max_ball = 6
                    msu = self.game.mystic_lines.position

                    if self.game.ball_count.position < max_ball:
                        if self.game.mystic_lines.position >= 10:
                            self.game.sound.play('square')
                            self.game.line3.step()
                            self.cancel_delayed("line3_animation")
                            self.animate_line3([self.game,1,3])
                                    
                    self.delay(name="display", delay=0.1, handler=graphics.border_beauty.display, param=self)

    def sw_enter_active_for_500ms(self,sw):
        if self.game.switches.drawer.is_inactive():
            if self.game.ball_count.position > 0:
                max_ball = 0
                if self.game.selection_feature.position < 7:
                    max_ball = 4
                elif self.game.selection_feature.position < 8:
                    max_ball = 5
                else:
                    if self.game.selection_feature.position == 9:
                        max_ball = 6
                msu = self.game.mystic_lines.position

                if self.game.ball_count.position < max_ball:
                    if self.game.mystic_lines.position >= 10:
                        self.game.sound.play('square')
                        self.game.line3.step()
                        self.cancel_delayed("line3_animation")
                        self.animate_line3([self.game,1,3])
                                
                self.delay(name="display", delay=0.1, handler=graphics.border_beauty.display, param=self)
                self.delay(name="enter", delay=0.5, handler=self.sw_enter_active_for_500ms, param=sw)


    def sw_letterc_active(self, sw):
        if self.game.switches.drawer.is_active():
            if self.game.ball_count.position > 0:
                max_ball = 0
                if self.game.selection_feature.position < 7:
                    max_ball = 4
                elif self.game.selection_feature.position < 8:
                    max_ball = 5
                else:
                    if self.game.selection_feature.position == 9:
                        max_ball = 6
                msu = self.game.mystic_lines.position

                if self.game.ball_count.position < max_ball:
                    if self.game.mystic_lines.position >= 10:
                        self.game.sound.play('square')
                        self.game.line3.step()
                        self.cancel_delayed("line3_animation")
                        self.animate_line3([self.game,1,3])
                                
                self.delay(name="display", delay=0.1, handler=graphics.border_beauty.display, param=self)

    def sw_letterc_active_for_500ms(self,sw):
        if self.game.switches.drawer.is_active():
            if self.game.ball_count.position > 0:
                max_ball = 0
                if self.game.selection_feature.position < 7:
                    max_ball = 4
                elif self.game.selection_feature.position < 8:
                    max_ball = 5
                else:
                    if self.game.selection_feature.position == 9:
                        max_ball = 6
                msu = self.game.mystic_lines.position

                if self.game.ball_count.position < max_ball:
                    if self.game.mystic_lines.position >= 10:
                        self.game.sound.play('square')
                        self.game.line3.step()
                        self.cancel_delayed("line3_animation")
                        self.animate_line3([self.game,1,3])
                                
                self.delay(name="display", delay=0.1, handler=graphics.border_beauty.display, param=self)
                self.delay(name="letterc", delay=0.5, handler=self.sw_letterc_active_for_500ms, param=sw)


    def sw_enter_active_for_2s(self, sw):
        if self.game.switches.left.is_active() and self.game.switches.right.is_active():
            self.game.end_run_loop()
            os.system("/home/nbaldridge/proc/bingo_emulator/start_game.sh border_beauty")
        else:
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    ok_winner = self.find_ok_winner()
                    if ok_winner >= 2 and self.game.two_red_letter.status == True:
                        self.find_winner(0, 0, 0, 0, 0, 0, 0, ok_winner)
                    elif ok_winner >= 3 and self.game.three_red_letter.status == True:
                        self.find_winner(0, 0, 0, 0, 0, 0, 0, ok_winner)

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
            if self.game.ball_count.position >= 5:
                self.game.returned = True
            self.game.ball_count.position -= 1
            self.check_lifter_status()
        else:
            self.check_lifter_status()

    def sw_right_active(self, sw):
        if self.game.switches.drawer.is_inactive():
            if self.game.ball_count.position > 0:
                max_ball = 0
                if self.game.selection_feature.position < 7:
                    max_ball = 4
                elif self.game.selection_feature.position < 8:
                    max_ball = 5
                else:
                    if self.game.selection_feature.position == 9:
                        max_ball = 6
                msu = self.game.mystic_lines.position

                if self.game.ball_count.position < max_ball:
                    if self.game.mystic_lines.position >= 7:
                        self.game.sound.play('square')
                        self.game.line2.step()
                        self.cancel_delayed("line2_animation")
                        self.animate_line2([self.game,1,2])
                                
                self.delay(name="display", delay=0.1, handler=graphics.border_beauty.display, param=self)

    def sw_right_active_for_500ms(self,sw):
        if self.game.switches.drawer.is_inactive():
            if self.game.ball_count.position > 0:
                max_ball = 0
                if self.game.selection_feature.position < 7:
                    max_ball = 4
                elif self.game.selection_feature.position < 8:
                    max_ball = 5
                else:
                    if self.game.selection_feature.position == 9:
                        max_ball = 6
                msu = self.game.mystic_lines.position

                if self.game.ball_count.position < max_ball:
                    if self.game.mystic_lines.position >= 7:
                        self.game.sound.play('square')
                        self.game.line2.step()
                        self.cancel_delayed("line2_animation")
                        self.animate_line2([self.game,1,2])
                                
                self.delay(name="display", delay=0.1, handler=graphics.border_beauty.display, param=self)
                self.delay(name="right", delay=0.5, handler=self.sw_right_active_for_500ms, param=sw)

    def sw_letterb_active(self, sw):
        if self.game.switches.drawer.is_active():
            if self.game.ball_count.position > 0:
                max_ball = 0
                if self.game.selection_feature.position < 7:
                    max_ball = 4
                elif self.game.selection_feature.position < 8:
                    max_ball = 5
                else:
                    if self.game.selection_feature.position == 9:
                        max_ball = 6
                msu = self.game.mystic_lines.position

                if self.game.ball_count.position < max_ball:
                    if self.game.mystic_lines.position >= 7:
                        self.game.sound.play('square')
                        self.game.line2.step()
                        self.cancel_delayed("line2_animation")
                        self.animate_line2([self.game,1,2])
                                
                self.delay(name="display", delay=0.1, handler=graphics.border_beauty.display, param=self)

    def sw_letterb_active_for_500ms(self,sw):
        if self.game.switches.drawer.is_active():
            if self.game.ball_count.position > 0:
                max_ball = 0
                if self.game.selection_feature.position < 7:
                    max_ball = 4
                elif self.game.selection_feature.position < 8:
                    max_ball = 5
                else:
                    if self.game.selection_feature.position == 9:
                        max_ball = 6
                msu = self.game.mystic_lines.position

                if self.game.ball_count.position < max_ball:
                    if self.game.mystic_lines.position >= 7:
                        self.game.sound.play('square')
                        self.game.line2.step()
                        self.cancel_delayed("line2_animation")
                        self.animate_line2([self.game,1,2])
                                
                self.delay(name="display", delay=0.1, handler=graphics.border_beauty.display, param=self)
                self.delay(name="letterb", delay=0.5, handler=self.sw_letterb_active_for_500ms, param=sw)


    def sw_left_active(self, sw):
        if self.game.switches.drawer.is_inactive():
            if self.game.ball_count.position > 0:
                max_ball = 0
                if self.game.selection_feature.position < 7:
                    max_ball = 4
                elif self.game.selection_feature.position < 8:
                    max_ball = 5
                else:
                    if self.game.selection_feature.position == 9:
                        max_ball = 6
                msu = self.game.mystic_lines.position

                if self.game.ball_count.position < max_ball:
                    if self.game.mystic_lines.position >= 4:
                        self.game.sound.play('square')
                        self.game.line1.step()
                        self.cancel_delayed("line1_animation")
                        self.animate_line1([self.game,1,1])
                self.delay(name="display", delay=0.1, handler=graphics.border_beauty.display, param=self)

    def sw_left_active_for_500ms(self,sw):
        if self.game.switches.drawer.is_inactive():
            if self.game.ball_count.position > 0:
                max_ball = 0
                if self.game.selection_feature.position < 7:
                    max_ball = 4
                elif self.game.selection_feature.position < 8:
                    max_ball = 5
                else:
                    if self.game.selection_feature.position == 9:
                        max_ball = 6
                msu = self.game.mystic_lines.position

                if self.game.ball_count.position < max_ball:
                    if self.game.mystic_lines.position >= 4:
                        self.game.sound.play('square')
                        self.game.line1.step()
                        self.cancel_delayed("line1_animation")
                        self.animate_line1([self.game,1,1])
                self.delay(name="display", delay=0.1, handler=graphics.border_beauty.display, param=self)
                self.delay(name="left", delay=0.5, handler=self.sw_left_active_for_500ms, param=sw)

    def sw_lettera_active(self, sw):
        if self.game.switches.drawer.is_active():
            if self.game.ball_count.position > 0:
                max_ball = 0
                if self.game.selection_feature.position < 7:
                    max_ball = 4
                elif self.game.selection_feature.position < 8:
                    max_ball = 5
                else:
                    if self.game.selection_feature.position == 9:
                        max_ball = 6
                msu = self.game.mystic_lines.position

                if self.game.ball_count.position < max_ball:
                    if self.game.mystic_lines.position >= 4:
                        self.game.sound.play('square')
                        self.game.line1.step()
                        self.cancel_delayed("line1_animation")
                        self.animate_line1([self.game,1,1])
                                
                self.delay(name="display", delay=0.1, handler=graphics.border_beauty.display, param=self)

    def sw_lettera_active_for_500ms(self,sw):
        if self.game.switches.drawer.is_active():
            if self.game.ball_count.position > 0:
                max_ball = 0
                if self.game.selection_feature.position < 7:
                    max_ball = 4
                elif self.game.selection_feature.position < 8:
                    max_ball = 5
                else:
                    if self.game.selection_feature.position == 9:
                        max_ball = 6
                msu = self.game.mystic_lines.position

                if self.game.ball_count.position < max_ball:
                    if self.game.mystic_lines.position >= 4:
                        self.game.sound.play('square')
                        self.game.line1.step()
                        self.cancel_delayed("line1_animation")
                        self.animate_line1([self.game,1,1])
                                
                self.delay(name="display", delay=0.1, handler=graphics.border_beauty.display, param=self)
                self.delay(name="lettera", delay=0.5, handler=self.sw_lettera_active_for_500ms, param=sw)

    def check_selection(self):
        if self.game.mystic_lines.position >= 4:
            if self.game.selection_feature.position > 1 and self.game.selection_feature.position < 3:
                if self.game.yellow_star.status == False:
                    self.game.yellow_star.engage(self.game)
                    self.game.coils.yellowROLamp.enable()
                    self.game.sound.play('tilt')
            elif self.game.selection_feature.position >= 4 and self.game.selection_feature.position < 8:
                if self.game.red_star.status == False:
                    self.game.yellow_star.disengage()
                    self.game.coils.yellowROLamp.disable()
                    self.game.red_star.engage(self.game)
                    self.game.coils.redROLamp.enable()
                    self.game.sound.play('tilt')
            elif self.game.selection_feature.position == 9:
                self.game.red_star.disengage()
                self.game.coils.redROLamp.disable()
        self.delay(name="display", delay=0.1, handler=graphics.border_beauty.display, param=self)

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
        self.cancel_delayed(name="both_animation")
        self.cancel_delayed(name="odds_animation")
        self.cancel_delayed(name="feature_animation")
        self.cancel_delayed(name="search")
        self.cancel_delayed(name="red_replay_step_up")
        self.cancel_delayed(name="yellow_replay_step_up")
        self.cancel_delayed(name="green_replay_step_up")
        self.cancel_delayed(name="blue_replay_step_up")
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
        self.game.sound.play_music('motor', -1)

        self.game.cu = not self.game.cu
        begin = self.game.spotting.position
        self.game.spotting.spin()
        self.game.mixer1.spin()
        self.game.mixer2.spin()
        self.game.mixer3.spin()
        self.game.mixer4.spin()
        self.game.reflex.decrease()
        
        if self.game.features.status == True:
            self.animate_features_scan([begin,self.game.spotting.movement_amount,1])
        if self.game.all_advantages.status == True:
            self.animate_both([begin,self.game.spotting.movement_amount,1])
        if self.game.odds_only.status == True:
            self.animate_odds_scan([begin,self.game.spotting.movement_amount,1])

        self.game.returned = False
        if self.game.start.status == True:
            if self.game.selector.position < 1:
                self.game.selector.step()
            if self.game.switches.shutter.is_inactive():
                self.game.coils.shutter.enable()
            self.replay_step_down()
            graphics.border_beauty.display(self)
            self.check_lifter_status()
        else:
            if red_letter > 0:
                if self.game.switches.shutter.is_inactive():
                    self.game.coils.shutter.enable()

                #OK WINNER
                self.holes = []
                self.game.start.engage(self.game)
                self.game.coils.redROLamp.disable()
                self.game.coils.yellowROLamp.disable()
                self.game.red_replay_counter.reset()
                self.game.blue_replay_counter.reset()
                self.game.yellow_replay_counter.reset()
                self.game.green_replay_counter.reset()
                self.game.stars_replay_counter.reset()
                # Red odds stay, reset the rest
                #self.game.red_odds.reset()
                self.game.eb_play.disengage()
                self.game.odds_only.disengage()
                self.game.features.disengage()
                self.game.all_advantages.engage(self.game)
                self.game.yellow_odds.reset()
                self.game.green_odds.reset()
                self.game.blue_odds.reset()
                self.game.yellow_star.disengage()
                self.game.red_star.disengage()
                self.game.start.engage(self.game)
                self.game.ball_count.reset()
                self.game.extra_ball.reset()
                self.game.two_red_letter.disengage()
                self.game.three_red_letter.disengage()
                self.game.three_stars.disengage()
                self.game.six_stars.disengage()
                self.game.selection_feature.reset()
                self.game.timer.reset()
                if self.game.line2.position == 1:
                    self.game.sound.play('square')
                    self.game.line2.step()
                    self.cancel_delayed("line2_animation")
                    self.animate_line2([self.game,1,2])
                if self.game.line3.position == 1:
                    self.game.sound.play('square')
                    self.game.line3.step()
                    self.cancel_delayed("line3_animation")
                    self.animate_line3([self.game,1,3])
                if self.game.line1.position not in [0,2]:
                    self.game.sound.play('square')
                    self.game.line1.step()
                    self.cancel_delayed("line1_animation")
                    self.animate_line1([self.game,1,1])
                self.game.mystic_lines.reset()
                self.game.double_red.disengage()
                self.game.double_yellow.disengage()
                self.game.double_green.disengage()
                self.game.double_blue.disengage()
                self.check_lifter_status()
                # This happens for all red letter winners, but now I need to set the specific characteristics.
                if red_letter == 1:
                    self.green_extra_step(4)
                    self.blue_extra_step(4)
                    self.yellow_extra_step(6)
                    self.step_mystic_lines(10)
                    self.game.selection_feature.step()
                elif red_letter == 2:
                    self.green_extra_step(5)
                    self.yellow_extra_step(6)
                    self.blue_extra_step(5)
                    self.step_mystic_lines(10)
                    if self.game.red_odds.position < 4:
                        self.red_extra_step(4 - self.game.red_odds.position)
                    self.game.double_yellow.engage(self.game)
                    self.game.sound.play('tilt')
                    self.step_sf(5)
                    self.delay(name="check_selection", delay=0.1, handler=self.check_selection)
                elif red_letter == 3:
                    self.green_extra_step(6)
                    self.yellow_extra_step(6)
                    self.blue_extra_step(6)
                    self.step_mystic_lines(10)
                    if self.game.red_odds.position < 5:
                        self.red_extra_step(5 - self.game.red_odds.position)
                    self.game.double_yellow.engage(self.game)
                    self.game.sound.play('tilt')
                    self.game.double_green.engage(self.game)
                    self.game.sound.play('tilt')
                    self.step_sf(7)
                    self.delay(name="check_selection", delay=0.1, handler=self.check_selection)
                elif red_letter == 4:
                    self.green_extra_step(6)
                    self.yellow_extra_step(8)
                    self.blue_extra_step(6)
                    self.step_mystic_lines(10)
                    if self.game.red_odds.position < 6:
                        self.red_extra_step(6 - self.game.red_odds.position)
                    self.game.double_green.engage(self.game)
                    self.game.sound.play('tilt')
                    self.game.double_blue.engage(self.game)
                    self.game.sound.play('tilt')
                    self.step_sf(7)
                    self.delay(name="check_selection", delay=0.1, handler=self.check_selection)
                elif red_letter == 5:
                    self.green_extra_step(7)
                    self.yellow_extra_step(8)
                    self.blue_extra_step(7)
                    self.step_mystic_lines(10)
                    if self.game.red_odds.position < 7:
                        self.red_extra_step(7 - self.game.red_odds.position)
                    self.game.double_red.engage(self.game)
                    self.game.sound.play('tilt')
                    self.game.double_blue.engage(self.game)
                    self.game.sound.play('tilt')
                    self.step_sf(9)
                    self.delay(name="check_selection", delay=0.1, handler=self.check_selection)
                elif red_letter == 6:
                    self.green_extra_step(8)
                    self.yellow_extra_step(8)
                    self.blue_extra_step(8)
                    self.step_mystic_lines(10)
                    if self.game.red_odds.position < 8:
                        self.red_extra_step(8 - self.game.red_odds.position)
                    self.game.double_red.engage(self.game)
                    self.game.sound.play('tilt')
                    self.game.double_yellow.engage(self.game)
                    self.game.sound.play('tilt')
                    self.step_sf(9)
                    self.delay(name="check_selection", delay=0.1, handler=self.check_selection)
            else:
                self.holes = []
                self.game.start.engage(self.game)
                self.game.yellow_odds.reset()
                self.game.green_odds.reset()
                self.game.blue_odds.reset()
                self.game.yellow_star.disengage()
                self.game.red_star.disengage()
                self.game.start.engage(self.game)
                self.game.ball_count.reset()
                self.game.extra_ball.reset()
                self.game.two_red_letter.disengage()
                self.game.three_red_letter.disengage() 
                self.game.three_stars.disengage()
                self.game.six_stars.disengage()
                self.game.selection_feature.reset()
                self.game.timer.reset()
                if self.game.line2.position == 1:
                    self.game.sound.play('square')
                    self.game.line2.step()
                    self.cancel_delayed("line2_animation")
                    self.animate_line2([self.game,1,2])
                if self.game.line3.position == 1:
                    self.game.sound.play('square')
                    self.game.line3.step()
                    self.cancel_delayed("line3_animation")
                    self.animate_line3([self.game,1,3])
                if self.game.line1.position not in [0,2]:
                    self.game.sound.play('square')
                    self.game.line1.step()
                    self.cancel_delayed("line1_animation")
                    self.animate_line1([self.game,1,1])
                self.game.mystic_lines.reset()
                self.game.double_red.disengage()
                self.game.double_yellow.disengage()
                self.game.double_green.disengage()
                self.game.double_blue.disengage()
                self.game.coils.redROLamp.disable()
                self.game.coils.yellowROLamp.disable()
                self.game.red_replay_counter.reset()
                self.game.blue_replay_counter.reset()
                self.game.yellow_replay_counter.reset()
                self.game.green_replay_counter.reset()
                self.game.stars_replay_counter.reset()
                self.game.red_odds.reset()
                self.game.yellow_star.disengage()
                self.game.red_star.disengage()
                self.game.selector.reset()
                self.game.ball_count.reset()
                self.game.extra_ball.reset()
                self.game.two_red_letter.disengage()
                self.game.three_red_letter.disengage()
                self.game.selection_feature.reset()
                self.game.timer.reset()
                self.game.sound.play_music('motor', -1)
                self.regular_play()
        self.delay(name="display", delay=0.1, handler=graphics.border_beauty.display, param=self)
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
        self.delay(name="display", delay=0.1, handler=graphics.border_beauty.display, param=self)


    # This is really nasty, but it is how we render graphics for each individual hole.
    # numbers are added (or removed from) a list.  In this way, I can re-use the same
    # routine even for games where there are ball return functions like Surf Club.

    def sw_hole1_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(1)
            self.delay(name="display", delay=0.1, handler=graphics.border_beauty.display, param=self)

    def sw_hole2_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(2)
            self.delay(name="display", delay=0.1, handler=graphics.border_beauty.display, param=self)

    def sw_hole3_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(3)
            self.delay(name="display", delay=0.1, handler=graphics.border_beauty.display, param=self)

    def sw_hole4_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(4)
            self.delay(name="display", delay=0.1, handler=graphics.border_beauty.display, param=self)

    def sw_hole5_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(5)
            self.delay(name="display", delay=0.1, handler=graphics.border_beauty.display, param=self)

    def sw_hole6_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(6)
            self.delay(name="display", delay=0.1, handler=graphics.border_beauty.display, param=self)

    def sw_hole7_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(7)
            self.delay(name="display", delay=0.1, handler=graphics.border_beauty.display, param=self)

    def sw_hole8_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(8)
            self.delay(name="display", delay=0.1, handler=graphics.border_beauty.display, param=self)

    def sw_hole9_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(9)
            self.delay(name="display", delay=0.1, handler=graphics.border_beauty.display, param=self)

    def sw_hole10_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(10)
            self.delay(name="display", delay=0.1, handler=graphics.border_beauty.display, param=self)

    def sw_hole11_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(11)
            self.delay(name="display", delay=0.1, handler=graphics.border_beauty.display, param=self)

    def sw_hole12_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(12)
            self.delay(name="display", delay=0.1, handler=graphics.border_beauty.display, param=self)

    def sw_hole13_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(13)
            self.delay(name="display", delay=0.1, handler=graphics.border_beauty.display, param=self)

    def sw_hole14_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(14)
            self.delay(name="display", delay=0.1, handler=graphics.border_beauty.display, param=self)

    def sw_hole15_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(15)
            self.delay(name="display", delay=0.1, handler=graphics.border_beauty.display, param=self)

    def sw_hole16_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(16)
            self.delay(name="display", delay=0.1, handler=graphics.border_beauty.display, param=self)

    def sw_hole17_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(17)
            self.delay(name="display", delay=0.1, handler=graphics.border_beauty.display, param=self)

    def sw_hole18_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(18)
            self.delay(name="display", delay=0.1, handler=graphics.border_beauty.display, param=self)

    def sw_hole19_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(19)
            self.delay(name="display", delay=0.1, handler=graphics.border_beauty.display, param=self)

    def sw_hole20_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(20)
            self.delay(name="display", delay=0.1, handler=graphics.border_beauty.display, param=self)

    def sw_replayReset_active(self, sw):
        self.game.anti_cheat.disengage()
        self.holes = []
        graphics.border_beauty.display(self)
        self.tilt_actions()
        self.replay_step_down(self.game.replays)

    def sw_redstar_active(self, sw):
        if self.game.red_star.status == True:
            if self.game.selection_feature.position < 9:
                self.game.sound.play('tilt')
                self.game.selection_feature.position = 9
                self.game.red_star.disengage()
                self.game.coils.redROLamp.disable()
            self.delay(name="display", delay=0.1, handler=graphics.border_beauty.display, param=self)

    def sw_yellowstar_active(self, sw):
        if self.game.yellow_star.status == True:
            if self.game.selection_feature.position < 7:
                self.game.sound.play('tilt')
                self.game.selection_feature.position = 7
                self.game.yellow_star.disengage()
                self.game.coils.yellowROLamp.disable()
            self.delay(name="display", delay=0.1, handler=graphics.border_beauty.display, param=self)

    def tilt_actions(self):
        self.game.start.disengage()
        self.cancel_delayed(name="replay_reset")
        self.cancel_delayed(name="red_replay_step_up")
        self.cancel_delayed(name="yellow_replay_step_up")
        self.cancel_delayed(name="green_replay_step_up")
        self.cancel_delayed(name="blue_replay_step_up")
        self.cancel_delayed(name="blink")
        self.cancel_delayed(name="timeout")
        self.game.eb_play.disengage()
        self.game.all_advantages.disengage()
        self.game.odds_only.disengage()
        self.game.features.disengage()
        self.game.coils.redROLamp.disable()
        self.game.coils.yellowROLamp.disable()
        self.game.search_index.disengage()
        if self.game.ball_count.position == 0:
            if self.game.switches.shutter.is_active():
                self.game.coils.shutter.enable()
        self.holes = []
        self.game.yellow_odds.reset()
        self.game.green_odds.reset()
        self.game.blue_odds.reset()
        self.game.yellow_star.disengage()
        self.game.red_star.disengage()
        self.game.start.engage(self.game)
        self.game.ball_count.reset()
        self.game.extra_ball.reset()
        self.game.two_red_letter.disengage()
        self.game.three_red_letter.disengage()
        self.game.three_stars.disengage()
        self.game.six_stars.disengage()
        self.game.selection_feature.reset()
        self.game.timer.reset()
        self.game.mystic_lines.reset()
        self.game.double_red.disengage()
        self.game.double_yellow.disengage()
        self.game.double_green.disengage()
        self.game.double_blue.disengage()
        self.game.coils.redROLamp.disable()
        self.game.coils.yellowROLamp.disable()
        self.game.red_replay_counter.reset()
        self.game.blue_replay_counter.reset()
        self.game.yellow_replay_counter.reset()
        self.game.green_replay_counter.reset()
        self.game.stars_replay_counter.reset()
        self.game.red_odds.reset()
        self.game.yellow_star.disengage()
        self.game.red_star.disengage()
        self.game.selector.reset()
        self.game.ball_count.reset()
        self.game.extra_ball.reset()
        self.game.two_red_letter.disengage()
        self.game.three_red_letter.disengage()
        self.game.selection_feature.reset()
        self.game.anti_cheat.engage(game)
        self.game.tilt.engage(self.game)
        self.game.sound.stop_music()
        self.game.sound.play('tilt')
        # displays "Tilt" on the backglass, you have to recoin.
        self.delay(name="display", delay=0.1, handler=graphics.border_beauty.display, param=self)

    def sw_tilt_active(self, sw):
        if self.game.tilt.status == False:
            self.tilt_actions()

    def replay_step_down(self, number=0):
        if number > 0:
            if number > 1:
                self.game.replays -= 1
                graphics.replay_step_down(self.game.replays, graphics.border_beauty.reel1, graphics.border_beauty.reel10, graphics.border_beauty.reel100, graphics.border_beauty.reel1000)
                self.game.coils.registerDown.pulse()
                number -= 1
                self.delay(name="display", delay=0, handler=graphics.border_beauty.display, param=self)
                self.delay(name="replay_reset", delay=0.13, handler=self.replay_step_down, param=number)
            elif number == 1:
                self.game.replays -= 1
                graphics.replay_step_down(self.game.replays, graphics.border_beauty.reel1, graphics.border_beauty.reel10, graphics.border_beauty.reel100, graphics.border_beauty.reel1000)
                self.game.coils.registerDown.pulse()
                number -= 1
                self.delay(name="display", delay=0, handler=graphics.border_beauty.display, param=self)
                self.cancel_delayed(name="replay_reset")
        else: 
            if self.game.replays > 0:
                self.game.replays -= 1
                graphics.replay_step_down(self.game.replays, graphics.border_beauty.reel1, graphics.border_beauty.reel10, graphics.border_beauty.reel100, graphics.border_beauty.reel1000)
                self.delay(name="display", delay=0.1, handler=graphics.border_beauty.display, param=self)
            self.game.coils.registerDown.pulse()

    def replay_step_up(self):
        if self.game.replays < 8999:
            self.game.replays += 1
            graphics.replay_step_up(self.game.replays, graphics.border_beauty.reel1, graphics.border_beauty.reel10, graphics.border_beauty.reel100, graphics.border_beauty.reel1000)
        self.game.coils.registerUp.pulse()
        self.game.reflex.increase()
        graphics.border_beauty.display(self)

    def sw_yellow_active(self, sw):
        if self.game.start.status == False:
            if self.game.ball_count.position >= 4:
                if self.game.eb_play.status == True and (self.game.replays > 0 or self.game.switches.freeplay.is_active()):
                    self.cancel_delayed(name="eb_animation")
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
                    graphics.border_beauty.display(self)
                    self.animate_eb_scan([begin,self.game.spotting.movement_amount,1])
                    self.delay(name="display", delay=0.1, handler=graphics.border_beauty.display, param=self)
                    return
                if self.game.eb_play.status == False:
                    self.game.eb_play.engage(self.game)
                    self.delay(name="display", delay=0.1, handler=graphics.border_beauty.display, param=self)
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
       
        for i in range(0, 6):
            self.r = self.closed_search_relays(self.game.searchdisc.position)
            self.game.searchdisc.spin()
            self.wipers = self.r[0]
            self.red = self.r[1]
            self.yellow = self.r[2]
            self.green = self.r[3]
            self.blue = self.r[4]
            self.stars = self.r[5]

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
                        if relays == 4:
                            if self.red == True:
                                if self.game.line3.position == 0:
                                    if 6 in self.holes:
                                        relays += 1
                                else:
                                    if 13 in self.holes:
                                        relays += 1
                            elif self.green == True:
                                if self.game.line3.position == 0:
                                    if 17 in self.holes:
                                        relays += 1
                                else:
                                    if 9 in self.holes:
                                        relays += 1
                            elif self.yellow == True:
                                if self.game.line2.position == 0:
                                    if 1 in self.holes:
                                        relays += 1
                                else:
                                    if 15 in self.holes:
                                        relays += 1
                            elif self.blue == True:
                                if self.game.line2.position == 0:
                                    if 16 in self.holes:
                                        relays += 1
                                else:
                                    if 14 in self.holes:
                                        relays += 1
                        #TODO Play sound for each relay closure.
                        s = relays 
                        if s >= 2:
                            self.find_winner(s, self.red, self.yellow, self.green, self.blue, self.stars)
                            break
                            
    # THIS NEEDS TO BE CALLED IF THE SCREEN IF OUT OF INDEX POSITION

    def find_ok_winner(self):
        self.red_letter_winner = 0
        if self.game.line2.position == 0:
            if 16 in self.holes:
                self.red_letter_winner += 1
            if 1 in self.holes:
                self.red_letter_winner += 1
        else:
            if 14 in self.holes:
                self.red_letter_winner += 1
            if 15 in self.holes:
                self.red_letter_winner += 1
        if self.game.line3.position == 0:
            if 6 in self.holes:
                self.red_letter_winner += 1
            if 17 in self.holes:
                self.red_letter_winner += 1
        else:
            if 9 in self.holes:
                self.red_letter_winner += 1
            if 13 in self.holes:
                self.red_letter_winner += 1
        return self.red_letter_winner

    def find_winner(self, relays, red, yellow, green, blue, stars, ok_winner=0, red_letter_winner=0):
        if self.game.search_index.status == False and self.game.replays < 8999:
            if self.game.red_odds.position == 1:
                redthreeodds = 4
                redfourodds = 16
                redfiveodds = 75
            elif self.game.red_odds.position == 2:
                redthreeodds = 6
                redfourodds = 20
                redfiveodds = 75
            elif self.game.red_odds.position == 3:
                redthreeodds = 8
                redfourodds = 24
                redfiveodds = 96
            elif self.game.red_odds.position == 4:
                redthreeodds = 16
                redfourodds = 50
                redfiveodds = 96
            elif self.game.red_odds.position == 5:
                redthreeodds = 32
                redfourodds = 96
                redfiveodds = 200
            elif self.game.red_odds.position == 6:
                redthreeodds = 64
                redfourodds = 144
                redfiveodds = 300
            elif self.game.red_odds.position == 7:
                redthreeodds = 120
                redfourodds = 240
                redfiveodds = 450
            elif self.game.red_odds.position == 8:
                redthreeodds = 192
                redfourodds = 480
                redfiveodds = 600
            if self.game.yellow_odds.position == 1:
                yellowthreeodds = 4
                yellowfourodds = 16
                yellowfiveodds = 75
            elif self.game.yellow_odds.position == 2:
                yellowthreeodds = 6
                yellowfourodds = 20
                yellowfiveodds = 75
            elif self.game.yellow_odds.position == 3:
                yellowthreeodds = 8
                yellowfourodds = 24
                yellowfiveodds = 96
            elif self.game.yellow_odds.position == 4:
                yellowthreeodds = 16
                yellowfourodds = 50
                yellowfiveodds = 96
            elif self.game.yellow_odds.position == 5:
                yellowthreeodds = 32
                yellowfourodds = 96
                yellowfiveodds = 200
            elif self.game.yellow_odds.position == 6:
                yellowthreeodds = 64
                yellowfourodds = 144
                yellowfiveodds = 300
            elif self.game.yellow_odds.position == 7:
                yellowthreeodds = 120
                yellowfourodds = 240
                yellowfiveodds = 450
            elif self.game.yellow_odds.position == 8:
                yellowthreeodds = 192
                yellowfourodds = 480
                yellowfiveodds = 600
            if self.game.green_odds.position == 1:
                greenthreeodds = 4
                greenfourodds = 16
                greenfiveodds = 75
            elif self.game.green_odds.position == 2:
                greenthreeodds = 6
                greenfourodds = 20
                greenfiveodds = 75
            elif self.game.green_odds.position == 3:
                greenthreeodds = 8
                greenfourodds = 24
                greenfiveodds = 96
            elif self.game.green_odds.position == 4:
                greenthreeodds = 16
                greenfourodds = 50
                greenfiveodds = 96
            elif self.game.green_odds.position == 5:
                greenthreeodds = 32
                greenfourodds = 96
                greenfiveodds = 200
            elif self.game.green_odds.position == 6:
                greenthreeodds = 64
                greenfourodds = 144
                greenfiveodds = 300
            elif self.game.green_odds.position == 7:
                greenthreeodds = 120
                greenfourodds = 240
                greenfiveodds = 450
            elif self.game.green_odds.position == 8:
                greenthreeodds = 192
                greenfourodds = 480
                greenfiveodds = 600
            if self.game.blue_odds.position == 1:
                bluethreeodds = 4
                bluefourodds = 16
                bluefiveodds = 75
            elif self.game.blue_odds.position == 2:
                bluethreeodds = 6
                bluefourodds = 20
                bluefiveodds = 75
            elif self.game.blue_odds.position == 3:
                bluethreeodds = 8
                bluefourodds = 24
                bluefiveodds = 96
            elif self.game.blue_odds.position == 4:
                bluethreeodds = 16
                bluefourodds = 50
                bluefiveodds = 96
            elif self.game.blue_odds.position == 5:
                bluethreeodds = 32
                bluefourodds = 96
                bluefiveodds = 200
            elif self.game.blue_odds.position == 6:
                bluethreeodds = 64
                bluefourodds = 144
                bluefiveodds = 300
            elif self.game.blue_odds.position == 7:
                bluethreeodds = 120
                bluefourodds = 240
                bluefiveodds = 450
            elif self.game.blue_odds.position == 8:
                bluethreeodds = 192
                bluefourodds = 480
                bluefiveodds = 600

            if self.game.double_red.status == True:
                redthreeodds = redthreeodds * 2
                redfourodds = redfourodds * 2
                redfiveodds = redfiveodds * 2
            if self.game.double_yellow.status == True:
                yellowthreeodds = yellowthreeodds * 2
                yellowfourodds = yellowfourodds * 2
                yellowfiveodds = yellowfiveodds * 2
            if self.game.double_green.status == True:
                greenthreeodds = greenthreeodds * 2
                greenfourodds = greenfourodds * 2
                greenfiveodds = greenfiveodds * 2
            if self.game.double_blue.status == True:
                bluethreeodds = bluethreeodds * 2
                bluefourodds = bluefourodds * 2
                bluefiveodds = bluefiveodds * 2

            if self.game.two_red_letter.status == True or self.game.three_red_letter.status == True:
                if red_letter_winner >= 2:
                    # WIN OK GAME, CHECK RED LETTER UNIT
                    if self.game.red_odds.position <= 3:
                        red_letter = 1
                    else:
                        red_letter = self.game.red_odds.position - 2
                    self.regular_play(red_letter)
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
                if (blue == 1 and relays == 3):
                    if self.game.search_index.status == False:
                        if self.game.blue_replay_counter.position < bluethreeodds:
                            self.game.search_index.engage(self.game)
                            self.blue_replay_step_up(bluethreeodds - self.game.blue_replay_counter.position)
            if relays == 4:
                if stars:
                    if self.game.six_stars.status == True:
                        if self.game.stars_replay_counter.position < 600:
                            self.game.search_index.engage(self.game)
                            self.stars_replay_step_up(600 - self.game.stars_replay_counter.position)
                    elif self.game.three_stars.status == True:
                        if self.game.stars_replay_counter.position < 300:
                            self.game.search_index.engage(self.game)
                            self.stars_replay_step_up(300 - self.game.stars_replay_counter.position)
                else:
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
                    if (blue == 1 and relays == 4):
                        if self.game.search_index.status == False:
                            if self.game.blue_replay_counter.position < bluefourodds:
                                self.game.search_index.engage(self.game)
                                self.blue_replay_step_up(bluefourodds - self.game.blue_replay_counter.position)
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
                if (blue == 1 and relays == 5):
                    if self.game.search_index.status == False:
                        if self.game.blue_replay_counter.position < bluefiveodds:
                            self.game.search_index.engage(self.game)
                            self.blue_replay_step_up(bluefiveodds - self.game.blue_replay_counter.position)

    def blue_replay_step_up(self, number):
        self.game.sound.stop('search')
        if number >= 1:
            self.game.blue_replay_counter.step()
            number -= 1
            self.replay_step_up()
            if self.game.replays == 8999:
                number = 0
            self.delay(name="blue_replay_step_up", delay=0.25, handler=self.blue_replay_step_up, param=number)
        else:
            self.game.search_index.disengage()
            self.cancel_delayed(name="blue_replay_step_up")
            self.search()

    def red_replay_step_up(self, number):
        self.game.sound.stop('search')
        if number >= 1:
            self.game.red_replay_counter.step()
            number -= 1
            self.replay_step_up()
            if self.game.replays == 8999:
                number = 0
            self.delay(name="red_replay_step_up", delay=0.25, handler=self.red_replay_step_up, param=number)
        else:
            self.game.search_index.disengage()
            self.cancel_delayed(name="red_replay_step_up")
            self.search()
            
    def yellow_replay_step_up(self, number):
        self.game.sound.stop('search')
        if number >= 1:
            self.game.yellow_replay_counter.step()
            number -= 1
            self.replay_step_up()
            if self.game.replays == 8999:
                number = 0
            self.delay(name="yellow_replay_step_up", delay=0.25, handler=self.yellow_replay_step_up, param=number)
        else:
            self.game.search_index.disengage()
            self.cancel_delayed(name="yellow_replay_step_up")
            self.search()

    def green_replay_step_up(self, number):
        self.game.sound.stop('search')
        if number >= 1:
            self.game.green_replay_counter.step()
            number -= 1
            self.replay_step_up()
            if self.game.replays == 8999:
                number = 0
            self.delay(name="green_replay_step_up", delay=0.25, handler=self.green_replay_step_up, param=number)
        else:
            self.game.search_index.disengage()
            self.cancel_delayed(name="green_replay_step_up")
            self.search()

    def stars_replay_step_up(self, number):
        self.game.sound.stop('search')
        if number >= 1:
            self.game.stars_replay_counter.step()
            number -= 1
            self.replay_step_up()
            if self.game.replays == 8999:
                number = 0
            self.delay(name="stars_replay_step_up", delay=0.25, handler=self.stars_replay_step_up, param=number)
        else:
            self.game.search_index.disengage()
            self.cancel_delayed(name="stars_replay_step_up")
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
        blue = False
        stars = False

        if self.game.line2.position == 0:
            self.p1 = 18
            self.p2 = 4
            self.q1 = 11
            self.q2 = 8
            self.r1 = 15
            self.r2 = 1
            self.s1 = 16
            self.s2 = 14
        elif self.game.line2.position == 1:
            self.p1 = 4
            self.p2 = 18
            self.q1 = 8
            self.q2 = 11
            self.r1 = 1
            self.r2 = 15
            self.s1 = 14
            self.s2 = 16

        if self.game.line1.position in [0,2]:
            self.p3 = 7
            self.q3 = 12
            self.r3 = 20
            self.s3 = 5
        elif self.game.line1.position == 1:
            self.p3 = 5
            self.q3 = 7
            self.r3 = 12
            self.s3 = 20
        elif self.game.line1.position == 3:
            self.p3 = 12
            self.q3 = 20
            self.r3 = 5
            self.s3 = 7

        if self.game.line3.position == 0:
            self.p4 = 9
            self.p5 = 17
            self.q4 = 6
            self.q5 = 13
            self.r4 = 2
            self.r5 = 19
            self.s4 = 3
            self.s5 = 10
        elif self.game.line3.position == 1:
            self.p4 = 17
            self.p5 = 9
            self.q4 = 13
            self.q5 = 6
            self.r4 = 19
            self.r5 = 2
            self.s4 = 10
            self.s5 = 3

        self.pos[0] = {}
        # Blue section
        self.pos[1] = {self.q1:1, self.r1:2, self.s2:3, self.s3:4}
        # Yellow section
        self.pos[2] = {self.p1:1, self.q2:2, self.r3:3, self.s4:4}
        # Red section
        self.pos[3] = {self.p2:1, self.q3:2, self.r4:3, self.s5:4}
        # Green Section
        self.pos[4] = {self.p3:1, self.p4:2, self.q5:3, self.r5:4}
        # Stars
        self.pos[5] = {self.p5:1, self.q4:2, self.r2:3, self.s1:4}

        if rivets == 1:
            blue = True
        if rivets == 2:
            yellow = True
        if rivets == 3:
            red = True
        if rivets == 4:
            green = True
        if rivets == 5:
            stars = True
                
        return (self.pos[rivets], red, yellow, green, blue, stars)

    
    def scan_all(self):
        #Animate scanning of everything - this happens through the spotting disc
        self.all_probability()

    def all_probability(self):
        mix1 = self.game.mixer1.connected_rivet()
        if self.game.reflex.connected_rivet() == 0:
            #Worst position for reflex - requires mixer1 to be in the three liberal positions for the connection of the wires bypassing the reflex.
            if mix1 in [2,21,17]:
                self.scan_odds()
                if self.game.red_odds.position > 0:
                    self.scan_features()
        if self.game.reflex.connected_rivet() == 1 and (mix1 in [2,21,17,4,23]):
            self.scan_odds()
            if self.game.red_odds.position > 0:
                self.scan_features()
        elif self.game.reflex.connected_rivet() == 2 and (mix1 in [2,21,17,4,23,12]):
            self.scan_odds()
            if self.game.red_odds.position > 0:
                self.scan_features()
        elif self.game.reflex.connected_rivet() == 3 and (mix1 in [2,21,17,4,23,12,1,10,19]):
            self.scan_odds()
            if self.game.red_odds.position > 0:
                self.scan_features()
        elif self.game.reflex.connected_rivet() == 4 and (mix1 in [2,21,17,4,23,12,1,10,19,18]):
            self.scan_odds()
            if self.game.red_odds.position > 0:
                self.scan_features()
        else:
            self.scan_odds()

    def eb_reflex(self):
        mix1 = self.game.mixer1.connected_rivet()
        if self.game.reflex.connected_rivet() == 0:
            #Worst position for reflex - requires mixer1 to be in the three liberal positions for the connection of the wires bypassing the reflex.
            if mix1 in [2,21,17]:
                return 1
        if self.game.reflex.connected_rivet() == 1 and (mix1 in [2,21,17,4,23]):
            return 1
        elif self.game.reflex.connected_rivet() == 2 and (mix1 in [2,21,17,4,23,12]):
            return 1
        elif self.game.reflex.connected_rivet() == 3 and (mix1 in [2,21,17,4,23,12,1,10,19]):
            return 1
        elif self.game.reflex.connected_rivet() == 4 and (mix1 in [2,21,17,4,23,12,1,10,19,18]):
            return 1
        else:
            return 0

    def check_selection_ok(self):
        if self.game.cu == 1:
            return 1
        else:
            if self.game.selection_feature.position != 8:
                i = self.check_mixer2(self.game.selection_feature.position)
                if i == 1:
                    return 1
                else:
                    return 0
            elif self.game.selection_feature.position <= 6:
                i = self.check_mixer2(self.game.selection_feature.position)
                if i == 1:
                    return 1
                else:
                    return 0
            elif self.game.selection_feature.position <= 4:
                i = self.check_mixer2(self.game.selection_feature.position)
                if i == 1:
                    return 1
                else:
                    return 0
            elif self.game.selection_feature.position <= 1:
                i = self.check_mixer2(self.game.selection_feature.position)
                if i == 1:
                    return 1
                else:
                    return 0
               
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
        if self.game.odds_only.status == True:
            if self.game.yellow_odds.position < 3 or self.game.red_odds.position < 3 or self.game.green_odds.position < 3 or self.game.blue_odds.position < 3:
                if self.game.yellow_odds.position <= 2:
                    if self.game.yellow_odds.position == 1:
                        self.yellow_extra_step(2)
                    else:
                        if self.game.yellow_odds.position == 2:
                            self.yellow_extra_step(1)
                if self.game.red_odds.position <= 2:
                    if self.game.red_odds.position == 1:
                        self.red_extra_step(2)
                    else:
                        if self.game.red_odds.position == 2:
                            self.red_extra_step(1)
                if self.game.green_odds.position <= 2:
                    if self.game.green_odds.position == 1:
                        self.green_extra_step(2)
                    else:
                        if self.game.green_odds.position == 2:
                            self.green_extra_step(1)
                if self.game.blue_odds.position <= 2:
                    if self.game.blue_odds.position == 1:
                        self.blue_extra_step(2)
                    else:
                        if self.game.blue_odds.position == 2:
                            self.blue_extra_step(1)
                return
        else:
            if self.game.all_advantages.status == True:
                if self.game.yellow_odds.position in [0,1] or self.game.red_odds.position in [0,1] or self.game.green_odds.position in [0,1] or self.game.blue_odds.position in [0,1]:
                    if self.game.yellow_odds.position < 2:
                        self.yellow_extra_step(1)
                    if self.game.red_odds.position < 2:
                        self.red_extra_step(1)
                    if self.game.green_odds.position < 2:
                        self.green_extra_step(1)
                    if self.game.blue_odds.position < 2:
                        self.blue_extra_step(1)
                    return
        if self.game.yellow_odds.position >= 2 and self.game.red_odds.position >= 2 and self.game.green_odds.position >= 2 and self.game.blue_odds.position >= 2:
            i = self.check_selection_ok()
            if i == 1:
                p = self.red_odds_probability()
                if p == 1:
                    es = self.check_extra_step()
                    if es == 1:
                        i = random.randint(1,3)
                        self.red_extra_step(i)
                    else:
                        self.game.red_odds.step()
                p = self.yellow_odds_probability()
                if p == 1:
                    es = self.check_extra_step()
                    if es == 1:
                        i = random.randint(1,3)
                        self.yellow_extra_step(i)
                    else:
                        self.game.yellow_odds.step()
                p = self.green_odds_probability()
                if p == 1:
                    es = self.check_extra_step()
                    if es == 1:
                        i = random.randint(1,3)
                        self.green_extra_step(i)
                        self.blue_extra_step(i)
                    else:
                        self.game.blue_odds.step()
                        self.game.green_odds.step()

    def green_extra_step(self, number):
        if number > 0:
            self.game.green_odds.step()
            self.delay(name="display", delay=0.1, handler=graphics.border_beauty.display, param=self)
            number -= 1
            self.delay(name="extra_step", delay=0.1, handler=self.green_extra_step, param=number)

    def red_extra_step(self, number):
        if number > 0:
            self.game.red_odds.step()
            self.delay(name="display", delay=0.1, handler=graphics.border_beauty.display, param=self)
            number -= 1
            self.delay(name="extra_step", delay=0.1, handler=self.red_extra_step, param=number)

    def yellow_extra_step(self, number):
        if number > 0:
            self.game.yellow_odds.step()
            self.delay(name="display", delay=0.1, handler=graphics.border_beauty.display, param=self)
            number -= 1
            self.delay(name="extra_step", delay=0.1, handler=self.yellow_extra_step, param=number)

    def blue_extra_step(self, number):
        if number > 0:
            self.game.blue_odds.step()
            self.delay(name="display", delay=0.1, handler=graphics.border_beauty.display, param=self)
            number -= 1
            self.delay(name="extra_step", delay=0.1, handler=self.blue_extra_step, param=number)

    def check_extra_step(self):
        i = random.randint(0,32)
        if i == 16:
            return 1
        else:
            return 0

    def check_odds_spotting(self, color):
        spot = self.game.spotting.position
        mix2 = self.check_mixer2(self.game.selection_feature.position)
        if mix2 == 1 or (self.game.cu and self.game.three_stars.status == False and self.game.six_stars.status == False and self.game.eb_play.status == False):
            if color == "yellow":
                if self.game.yellow_odds.position in [2,3]:
                    if spot in [0,10,11,12,19,20,21,27,28,31,32,33,34,35,38,39,40,45,46,47,48,49]:
                        return 1
                    elif self.game.odds_only.status == True:
                        if spot in [2,3,4,6,7,8,13,14,15,16,17,22,23,25,26,29,30,36,37,42,43,44]:
                            return 1
                if self.game.yellow_odds.position == 4:
                    if spot in [0,19,20,21,27,32,34,35,45,46,47,48,49]:
                        return 1
                    elif self.game.odds_only.status == True:
                        if spot in [1,5,9,15,16,17,18,24,29,30,36,37,41,44]:
                            return 1
                if self.game.yellow_odds.position == 5:
                    if spot in [10,11,12,28,31,38]:
                        return 1
                    elif self.game.odds_only.status == True:
                        if spot in [2,3,4,25,26,39,40]:
                            return 1
                if self.game.yellow_odds.position == 6:
                   return 1
                if self.game.yellow_odds.position == 7:
                   if spot in [6,8,14,22,23,43]:
                       return 1
                   elif self.game.odds_only.status == True:
                       if spot in [7,13,33,42]:
                           return 1
                return 0
            if color == "red":
                if self.game.red_odds.position in [2,3]:
                    if spot in [0,10,11,12,19,20,21,27,28,31,32,33,34,35,38,39,40,45,46,47,48,49]:
                        return 1
                    elif self.game.odds_only.status == True:
                        if spot in [2,3,4,6,7,8,13,14,15,16,17,22,23,25,26,29,30,36,37,42,43,44]:
                            return 1
                if self.game.red_odds.position == 4:
                    if spot in [0,19,20,21,27,32,34,35,45,46,47,48,49]:
                        return 1
                    elif self.game.odds_only.status == True:
                        if spot in [1,5,9,15,16,17,18,24,29,30,36,37,41,44]:
                            return 1
                if self.game.red_odds.position == 5:
                    if spot in [10,11,12,28,31,38]:
                        return 1
                    elif self.game.odds_only.status == True:
                        if spot in [2,3,4,25,26,39,40]:
                            return 1
                if self.game.red_odds.position == 6:
                   return 1
                if self.game.red_odds.position == 7:
                   if spot in [6,8,14,22,23,43]:
                       return 1
                   elif self.game.odds_only.status == True:
                       if spot in [7,13,33,42]:
                           return 1
                return 0
            if color == "blue" or color == "green":
                if self.game.blue_odds.position in [2,3]:
                    if spot in [0,10,11,12,19,20,21,27,28,31,32,33,34,35,38,39,40,45,46,47,48,49]:
                        return 1
                    elif self.game.odds_only.status == True:
                        if spot in [2,3,4,6,7,8,13,14,15,16,17,22,23,25,26,29,30,36,37,42,43,44]:
                            return 1
                if self.game.blue_odds.position == 4:
                    if spot in [0,19,20,21,27,32,34,35,45,46,47,48,49]:
                        return 1
                    elif self.game.odds_only.status == True:
                        if spot in [1,5,9,15,16,17,18,24,29,30,36,37,41,44]:
                            return 1
                if self.game.blue_odds.position == 5:
                    if spot in [10,11,12,28,31,38]:
                        return 1
                    elif self.game.odds_only.status == True:
                        if spot in [2,3,4,25,26,39,40]:
                            return 1
                if self.game.blue_odds.position == 6:
                   return 1
                if self.game.blue_odds.position == 7:
                   if spot in [6,8,14,22,23,43]:
                       return 1
                   elif self.game.odds_only.status == True:
                       if spot in [7,13,33,42]:
                           return 1
                return 0

        return 0

    def check_red_mixer3(self):
        mix3 = self.game.mixer3.position
        if self.game.three_red_letter.status == False and self.game.two_red_letter.status == False:
            if mix3 in [15,16]:
                if self.game.double_red.status == False:
                    return 1
                elif self.game.cu:
                    return 1
        else:
            if self.game.two_red_letter.status == False:
                if mix3 in [8,23]:
                    if self.game.double_red.status == False:
                        return 1
                    elif self.game.cu:
                        return 1
        if mix3 in [3,4,5,12,13]:
            if self.game.double_red.status == False:
                return 1
            elif self.game.cu:
                return 1
        else:
            return 0

    def red_odds_probability(self):
        i = self.check_odds_spotting('red')
        if i == 1:
            g = self.check_red_mixer3()
            if g == 1:
                return 1
            else:
                return 0

    def yellow_odds_probability(self):
        i = self.check_odds_spotting('yellow')
        if i == 1:
            g = self.check_yellow_mixer3()
            if g == 1:
                return 1
            else:
                return 0

    def check_yellow_mixer3(self):
        mix3 = self.game.mixer3.position
        if mix3 in [1,2,5,9,13,18,21,22]:
            if self.game.double_yellow.status == False:
                return 1
            elif self.game.cu:
                return 1
        return 0
        
    def green_odds_probability(self):
        i = self.check_odds_spotting('green')
        if i == 1:
            g = self.check_green_mixer3()
            if g == 1:
                return 1
            else:
                return 0

    def check_green_mixer3(self):
        mix3 = self.game.mixer3.position
        if mix3 in [0,6,7,10,14,17,19,20]:
            if self.game.double_blue.status == False and self.game.double_green.status == False:
                return 1
            elif self.game.cu:
                return 1
        else:
            return 0

    def scan_features(self):
        p = self.features_probability()

    def check_mixer4(self):
        m4 = self.game.mixer4.position
        m1 = self.game.mixer1.position
        if m1 in [0,2,3,4,5,6,7,9,10,11]:
            if self.game.blue_odds.position == 0:
                self.game.mixer4_relay.engage(self.game)
        if m4 in [1,7,9,15,17,19,21,23]:
            if self.game.blue_odds.position in [1,2,3]:
                self.game.mixer4_relay.engage(self.game)
        if m4 in [1,2,3,5,7,9,10]:
            if self.game.blue_odds.position == 4:
                self.game.mixer4_relay.engage(self.game)
        if m4 in [6,17,19,20]:
            if self.game.blue_odds.position == 5:
                self.game.mixer4_relay.engage(self.game)
        if m4 in [13,14]:
            if self.game.blue_odds.position == 6:
                self.game.mixer4_relay.engage(self.game)
        if m4 == 20:
            if self.game.blue_odds.position == 7:
                self.game.mixer4_relay.engage(self.game)
        if self.game.blue_odds.position > 3:
            if self.game.cu:
                if self.game.double_blue.status == False:
                    self.game.mixer4_relay.engage(self.game)
            else:
                if self.game.double_green.status == False:
                    self.game.mixer4_relay.engage(self.game)
        if m4 in [1,3,5,7,9]:
            if self.game.yellow_odds.position in [1,2,3]:
                self.game.mixer4_relay.engage(self.game)
        if m4 in [4,12,13,15,21,23]:
            if self.game.yellow_odds.position == 4:
                self.game.mixer4_relay.engage(self.game)
        if m4 in [2,10,14,16]:
            if self.game.yellow_odds.position == 5:
                self.game.mixer4_relay.engage(self.game)
        if m4 in [6,17,19,20]:
            if self.game.yellow_odds.position == 6:
                self.game.mixer4_relay.engage(self.game)
        if m4 == 22:
            if self.game.yellow_odds.position == 7:
                self.game.mixer4_relay.engage(self.game)
        if self.game.yellow_odds.position > 3:
            if self.game.double_yellow.status == False:
                self.game.mixer4_relay.engage(self.game)
        if m4 in [7,9,11,13,15]:
            if self.game.red_odds.position in [1,2,3]:
                self.game.mixer4_relay.engage(self.game)
        if m4 in [3,5,17,19,21,23]:
            if self.game.red_odds.position == 4:
                self.game.mixer4_relay.engage(self.game)
        if m4 in [6,8,10]:
            if self.game.red_odds.position == 5:
                self.game.mixer4_relay.engage(self.game)
        if m4 in [1,2,18,20]:
            if self.game.red_odds.position == 6:
                self.game.mixer4_relay.engage(self.game)
        if m4 == 22:
            if self.game.red_odds.position == 7:
                self.game.mixer4_relay.engage(self.game)
        if self.game.red_odds.position > 3:
            if self.game.double_red.status == False:
                self.game.mixer4_relay.engage(self.game)

    def features_probability(self):
        self.check_double_trips()
        self.check_mixer4()
        if self.game.mixer4_relay.status == True:
            self.features_spotting()
        else:
            self.game.mixer4_relay.disengage()

    def check_double_trips(self):
        m1 = self.game.mixer1.position
        m3 = self.game.mixer3.position
        m4 = self.game.mixer4.position
        if m1 in [0,3,6,9,10,11,16,17,19,20,21,23]:
            if m4 in [3,8]:
                if self.game.green_odds.position > 3:
                    if m3 in [1,2,5,9,13,18,21,22]:
                        if self.game.double_yellow.status == False:
                            self.game.double_yellow.engage(self.game)
                            self.game.sound.play('tilt')
                    if m3 in [3,4,8,11,12,15,16,23]:
                        if self.game.double_red.status == False:
                            self.game.double_red.engage(self.game)
                            self.game.sound.play('tilt')
                    if m3 in [6,7,14,19]:
                        if self.game.double_blue.status == False:
                            self.game.double_blue.engage(self.game)
                            self.game.sound.play('tilt')
                    if m3 in [10,17,20,0]:
                        if self.game.double_green.status == False:
                            self.game.double_green.engage(self.game)
                            self.game.sound.play('tilt')

    def features_spotting(self):
        sd = self.game.spotting.position
        if sd in [29,36,37]:
            if self.game.two_red_letter.status == False:
                if self.game.three_red_letter.status == False:
                    self.game.three_red_letter.engage(self.game)
                    self.game.sound.play('tilt')
        if sd in [11,34]:
            if self.game.mystic_lines.position == 10:
                if self.game.three_red_letter.status == True:
                    self.game.three_red_letter.disengage()
                if self.game.two_red_letter.status == False:
                    self.game.two_red_letter.engage(self.game)
                    self.game.sound.play('tilt')
        if sd == 15:
            if self.game.cu:
                if self.game.three_red_letter.status == True:
                    self.game.three_red_letter.disengage()
                if self.game.two_red_letter.status == False:
                    self.game.two_red_letter.engage(self.game)
                    self.game.sound.play('tilt')
        if sd == 10:
            if self.game.selection_feature.position < 5:
                if self.game.six_stars.status == False:
                    self.game.three_stars.disengage()
                    self.game.six_stars.engage(self.game)
                    self.game.sound.play('tilt')
            elif self.game.cu:
                if self.game.six_stars.status == False:
                    self.game.three_stars.disengage()
                    self.game.six_stars.engage(self.game)
                    self.game.sound.play('tilt')
        if sd == 33:
            if self.game.selection_feature.position < 5:
                if self.game.six_stars.status == False:
                    if self.game.three_stars.status == False:
                        self.game.three_stars.engage(self.game)
                        self.game.sound.play('tilt')
            elif self.game.cu:
                if self.game.six_stars.status == False:
                    if self.game.three_stars.status == False:
                        self.game.three_stars.engage(self.game)
                        self.game.sound.play('tilt')
        if self.game.mystic_lines.position >= 4:
            if sd in [0,19,20,21,27,32,35,49]:
                if self.game.selection_feature.position == 1:
                    self.step_selection(2)
            if sd in [1,5,18]:
                if self.game.selection_feature.position < 5:
                    self.step_selection(5 - self.game.selection_feature.position)
            if sd in [9,24,41,45,46]:
                if self.game.selection_feature.position < 9:
                    self.step_selection(9)
            if self.game.selection_feature.position in [1,3,5]:
                self.step_selection(2)
        if sd in [21,27,35,45]:
            self.step_mystic_lines(1)
        if self.game.cu or self.game.selection_feature.position < 9:
            if sd in [0,10,11,12,13,14,15,30,31,32,33,34,35,45,46,47,48,49]:
                if self.game.mystic_lines.position < 4:
                    self.step_mystic_lines(4 - self.game.mystic_lines.position)
                if self.game.mystic_lines.position >= 4 and self.game.mystic_lines.position < 7:
                    self.step_mystic_lines(7 - self.game.mystic_lines.position)
                if self.game.mystic_lines.position >= 7:
                    self.step_mystic_lines(10)
            if sd in [6,7,8,13,14,22,23,42,43,44]:
                if self.game.mystic_lines.position < 4:
                    self.step_mystic_lines(3 - self.game.mystic_lines.position)
                if self.game.mystic_lines.position >= 5:
                    self.step_mystic_lines(10)
            if sd in [2,3,4,16,17,25,26,30,39,40]:
                if self.game.mystic_lines.position < 4:
                    self.step_mystic_lines(4 - self.game.mystic_lines.position)
            if sd in [2,3,4]:
                if self.game.mystic_lines.position >= 7:
                    self.step_mystic_lines(10)

    def step_mystic_lines(self, number):
        if number >= 1:
            self.game.mystic_lines.step()
            self.check_selection()
            number -= 1
            self.delay(name="display", delay=0.1, handler=graphics.border_beauty.display, param=self)
            self.delay(name="step_sc", delay=0.1, handler=self.step_mystic_lines, param=number)

    def step_selection(self, number):
        if number >= 1:
            self.game.selection_feature.step()
            self.check_selection()
            number -= 1
            self.delay(name="display", delay=0.1, handler=graphics.border_beauty.display, param=self)
            self.delay(name="step_sc", delay=0.1, handler=self.step_selection, param=number)

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
        self.delay(name="display", delay=0.1, handler=graphics.border_beauty.display, param=self)

    def animate_odds_scan(self, args):
        start = args[0]
        diff = args[1]
        num = args[2]
        if start + num >= 50:
            start = 0
        if diff >= 0:
            num = num + 1
            graphics.border_beauty.odds_animation([self, start + num])
            self.cancel_delayed(name="display")
            diff = diff - 1
            args = [start,diff,num]
            self.delay(name="odds_animation", delay=0.08, handler=self.animate_odds_scan, param=args)
        else:
            self.cancel_delayed(name="odds_animation")
            self.delay(name="display", delay=0.1, handler=graphics.border_beauty.display, param=self)
            self.scan_odds()

    def animate_features_scan(self, args):
        start = args[0]
        diff = args[1]
        num = args[2]
        if start + num >= 50:
            start = 0
        if diff >= 0:
            num = num + 1
            graphics.border_beauty.feature_animation([self, start + num])
            self.cancel_delayed(name="display")
            diff = diff - 1
            args = [start,diff,num]
            self.delay(name="feature_animation", delay=0.08, handler=self.animate_features_scan, param=args)
        else:
            self.cancel_delayed(name="feature_animation")
            self.delay(name="display", delay=0.1, handler=graphics.border_beauty.display, param=self)
            self.scan_features()

    def animate_both(self, args):
        start = args[0]
        diff = args[1]
        num = args[2]
        if start + num >= 50:
            start = 0
        if diff >= 0:
            num = num + 1
            graphics.border_beauty.both_animation([self, start + num])
            self.cancel_delayed(name="display")
            diff = diff - 1
            args = [start,diff,num]
            self.delay(name="both_animation", delay=0.08, handler=self.animate_both, param=args)
        else:
            self.cancel_delayed(name="both_animation")
            self.delay(name="display", delay=0.1, handler=graphics.border_beauty.display, param=self)
            self.scan_all()

    def animate_line1(self, args):
        self.game = args[0]
        num = args[1]
        line = args[2]
        if num < 55:
            graphics.border_beauty.line1_animation([self, num * -1, line])
            self.cancel_delayed(name="display")
            num = num + 1
            args = [self.game,num,line]
            self.delay(name="line1_animation", delay=0.007, handler=self.animate_line1, param=args)
        else:
            self.cancel_delayed(name="line1_animation")
            self.delay(name="display", delay=0.1, handler=graphics.border_beauty.display, param=self)

    def animate_line2(self, args):
        self.game = args[0]
        num = args[1]
        line = args[2]
        if num < 55:
            graphics.border_beauty.line2_animation([self, num * -1, line])
            self.cancel_delayed(name="display")
            num = num + 1
            args = [self.game,num,line]
            self.delay(name="line2_animation", delay=0.007, handler=self.animate_line2, param=args)
        else:
            self.cancel_delayed(name="line2_animation")
            self.delay(name="display", delay=0.1, handler=graphics.border_beauty.display, param=self)

    def animate_line3(self, args):
        self.game = args[0]
        num = args[1]
        line = args[2]
        if num < 55:
            graphics.border_beauty.line3_animation([self, num * -1, line])
            self.cancel_delayed(name="display")
            num = num + 1
            args = [self.game,num,line]
            self.delay(name="line3_animation", delay=0.007, handler=self.animate_line3, param=args)
        else:
            self.cancel_delayed(name="line3_animation")
            self.delay(name="display", delay=0.1, handler=graphics.border_beauty.display, param=self)

    def animate_eb_scan(self, args):
        start = args[0]
        diff = args[1]
        num = args[2]
        if start + num >= 50:
            start = 0
        if diff >= 0:
            num = num + 1
            graphics.border_beauty.eb_animation([self, start + num])
            self.cancel_delayed(name="display")
            diff = diff - 1
            args = [start,diff,num]
            self.delay(name="eb_animation", delay=0.08, handler=self.animate_eb_scan, param=args)
        else:
            self.cancel_delayed(name="eb_animation")
            self.delay(name="display", delay=0.1, handler=graphics.border_beauty.display, param=self)
            self.scan_eb()

    def eb_probability(self):
        m4 = self.game.mixer4.position
        sd = self.game.spotting.position
        if sd in [2,4,6,7,14,17,23,27,29,33,34,35,37,39,41,42,43,45,47,48]:
            if self.game.extra_ball.position < 3:
                self.step_eb(3 - self.game.extra_ball.position)
            elif self.game.extra_ball.position >= 3 and self.game.extra_ball.position < 6:
                if m4 in [1,5,7,9,12,15,17,19]:
                    self.step_eb(6 - self.game.extra_ball.position)
            else:
                if self.game.cu:
                    self.step_eb(9)
                else:
                    self.step_eb(1)
        if self.game.extra_ball.position == 3:
            self.step_eb(1)
        elif self.game.extra_ball.position == 6:
            self.step_eb(1)
 
    def step_sf(self, number):
        if number >= 1:
            self.game.selection_feature.step()
            number -= 1
            self.delay(name="display", delay=0.1, handler=graphics.border_beauty.display, param=self)
            self.delay(name="step_sf", delay=0.1, handler=self.step_sf, param=number)

    def step_eb(self, number):
        if number >= 1:
            self.game.extra_ball.step()
            self.check_lifter_status()
            number -= 1
            self.delay(name="display", delay=0.1, handler=graphics.border_beauty.display, param=self)
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
        self.game.all_advantages.engage(self.game)

class BorderBeauty(procgame.game.BasicGame):
    """ Border Beauty was the first Mystic Lines game """
    def __init__(self, machine_type):
        super(BorderBeauty, self).__init__(machine_type)
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

        self.searchdisc = units.Search("searchdisc", 5)

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

        #Odds steppers
        self.red_odds = units.Stepper("red_odds", 8, 'border_beauty')
        self.yellow_odds = units.Stepper("yellow_odds", 8, 'border_beauty')
        self.green_odds = units.Stepper("green_odds", 8, 'border_beauty')
        self.blue_odds = units.Stepper("blue_odds", 8, 'border_beauty')

        #Replay Counter
        self.red_replay_counter = units.Stepper("red_replay_counter", 1200)
        self.yellow_replay_counter = units.Stepper("yellow_replay_counter", 1200)
        self.green_replay_counter = units.Stepper("green_replay_counter", 1200)
        self.blue_replay_counter = units.Stepper("blue_replay_counter", 1200)
        self.stars_replay_counter = units.Stepper("stars_replay_counter", 600)
        
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

        self.mystic_lines = units.Stepper("mystic_lines", 10)

        self.line1 = units.Stepper("line1", 3, "border_beauty", "continuous")
        self.line2 = units.Stepper("line2", 1, "border_beauty", "continuous")
        self.line3 = units.Stepper("line3", 1, "border_beauty", "continuous")

        self.two_red_letter = units.Relay("two_red_letter")
        self.three_red_letter = units.Relay("three_red_letter")

        self.double_red = units.Relay("double_red")
        self.double_yellow = units.Relay("double_yellow")
        self.double_green = units.Relay("double_green")
        self.double_blue = units.Relay("double_blue")

        self.yellow_star = units.Relay("yellow_star")
        self.red_star = units.Relay("red_star")

        self.six_stars = units.Relay("six_stars")
        self.three_stars = units.Relay("three_stars")
        
        self.mixer2_relay = units.Relay("mixer2_relay")
        self.mixer4_relay = units.Relay("mixer4_relay")

        self.replays = 0
        self.returned = False

    def reset(self):
        super(BorderBeauty, self).reset()
        self.logger = logging.getLogger('game')
        self.load_config('bingo.yaml')
        
        main_mode = SinglecardBingo(self)
        self.modes.add(main_mode)
        
game = BorderBeauty(machine_type='pdb')
game.reset()
game.run_loop()
