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
from bingo_emulator.graphics.galaxy import *

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
        self.game.sound.register_sound('magic_screen', "audio/magic_square.wav")
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
            self.game.scramble.spin()
            self.game.probability.spin()
            begin = self.game.program.position
            self.game.program.spin()
            self.game.coils.counter.pulse()
            self.animate_eb_scan([begin,self.game.program.movement_amount,self.game.program.movement_amount])
        else:
            self.game.all_advantages.engage(self.game)
            self.game.odds_only.disengage()
            self.game.eb_play.disengage()
            self.game.features.disengage()
            self.regular_play()
        self.delay(name="display", delay=0.1, handler=graphics.galaxy.display, param=self)

    def sw_startButton_active(self, sw):
        self.cancel_delayed(name="both_animation")
        self.cancel_delayed(name="odds_animation")
        self.cancel_delayed(name="feature_animation")
        self.cancel_delayed(name="blink")
        self.game.eb_play.disengage()
        self.game.odds_only.disengage()
        self.game.features.disengage()
        self.game.all_advantages.engage(self.game)
        self.delay(name="display", delay=0.1, handler=graphics.galaxy.display, param=self)

        if self.game.replays > 0 or self.game.switches.freeplay.is_active():
            self.game.cu = not self.game.cu
            self.game.scramble.spin()
            self.game.probability.spin()
            self.game.program.spin()
            self.game.tilt.disengage()
            self.regular_play()
        self.delay(name="display", delay=0.1, handler=graphics.galaxy.display, param=self)

    def sw_yellow_active(self, sw):
        if self.game.start.status == False:
            if self.game.ball_count.position >= 4:
                if self.game.eb_play.status == True and (self.game.replays > 0 or self.game.switches.freeplay.is_active()):
                    self.game.sound.play('eb_search')
                    if self.game.timer.position >= 8:
                        self.game.timer.reset()
                        self.game.sound.play_music('motor', -1)
                        self.timeout_actions()
                    self.game.cu = not self.game.cu
                    self.game.scramble.spin()
                    self.game.probability.spin()
                    begin = self.game.program.position
                    self.game.program.spin()
                    self.replay_step_down()
                    self.game.reflex.decrease()
                    graphics.galaxy.display(self)
                    self.game.coils.counter.pulse()
                    self.animate_eb_scan([begin,self.game.program.movement_amount,1])
                    self.delay(name="display", delay=0.1, handler=graphics.galaxy.display, param=self)
                    return
                if self.game.eb_play.status == False:
                    self.game.eb_play.engage(self.game)
                    self.delay(name="display", delay=0.1, handler=graphics.galaxy.display, param=self)
                    self.delay(name="yellow", delay=0.1, handler=self.sw_yellow_active, param=sw)

    def sw_blue_active(self, sw):
        self.cancel_delayed(name="both_animation")
        self.cancel_delayed(name="odds_animation")
        self.cancel_delayed(name="feature_animation")
        if self.game.start.status == True:
            self.game.features.disengage()
            self.game.all_advantages.disengage()
            self.game.eb_play.disengage()
            self.game.odds_only.engage(self.game)
            self.delay(name="display", delay=0.1, handler=graphics.galaxy.display, param=self)
        if self.game.replays > 0 or self.game.switches.freeplay.is_active():
            if self.game.start.status == False:
                self.delay(name="startup", delay=0.1, handler=self.sw_startButton_active, param=sw)
            if self.game.odds_only.status == True:
                self.delay(name="display", delay=0.1, handler=graphics.galaxy.display, param=self)
                self.regular_play()
                self.delay(name="display", delay=0.1, handler=graphics.galaxy.display, param=self)
       
    def sw_green_active(self, sw):
        self.cancel_delayed(name="both_animation")
        self.cancel_delayed(name="odds_animation")
        self.cancel_delayed(name="feature_animation")
        if self.game.start.status == True:
            self.game.features.engage(self.game)
            self.game.all_advantages.disengage()
            self.game.odds_only.disengage()
            self.game.eb_play.disengage()
            self.delay(name="display", delay=0.1, handler=graphics.galaxy.display, param=self)
        if self.game.replays > 0 or self.game.switches.freeplay.is_active():
            if self.game.start.status == False:
                self.delay(name="startup", delay=0.1, handler=self.sw_startButton_active, param=sw)
            if self.game.features.status == True:
                self.delay(name="display", delay=0.1, handler=graphics.galaxy.display, param=self)
                self.regular_play()
                self.delay(name="display", delay=0.1, handler=graphics.galaxy.display, param=self)

    def sw_enter_active(self, sw):
        if self.game.switches.left.is_active() and self.game.switches.right.is_active():
            self.game.end_run_loop()
            os.system("/home/nbaldridge/proc/bingo_emulator/start_game.sh galaxy")
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
                        if self.game.mystic_lines.position >= 6:
                            self.game.sound.play('magic_screen')
                            self.game.line3.step()
                            self.cancel_delayed("line3_animation")
                            self.animate_line3([self.game,1,3])
                                    
                    self.delay(name="display", delay=0.1, handler=graphics.galaxy.display, param=self)

    def sw_enter_active_for_500ms(self,sw):
        if self.game.switches.left.is_active() and self.game.switches.right.is_active():
            self.game.end_run_loop()
            os.system("/home/nbaldridge/proc/bingo_emulator/start_game.sh galaxy")
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
                        if self.game.mystic_lines.position >= 6:
                            self.game.sound.play('magic_screen')
                            self.game.line3.step()
                            self.cancel_delayed("line3_animation")
                            self.animate_line3([self.game,1,3])
                                    
                    self.delay(name="display", delay=0.1, handler=graphics.galaxy.display, param=self)
                    self.delay(name="enter", delay=0.6, handler=self.sw_enter_active_for_500ms, param=sw)


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
                    if self.game.mystic_lines.position >= 6:
                        self.game.sound.play('magic_screen')
                        self.game.line3.step()
                        self.cancel_delayed("line3_animation")
                        self.animate3_line([self.game,1,3])
                                
                self.delay(name="display", delay=0.1, handler=graphics.galaxy.display, param=self)

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
                    if self.game.mystic_lines.position >= 6:
                        self.game.sound.play('magic_screen')
                        self.game.line3.step()
                        self.cancel_delayed("line3_animation")
                        self.animate_line3([self.game,1,3])
                                
                self.delay(name="display", delay=0.1, handler=graphics.galaxy.display, param=self)
                self.delay(name="letterc", delay=0.6, handler=self.sw_letterc_active_for_500ms, param=sw)


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
                    if self.game.mystic_lines.position >= 4:
                        self.game.sound.play('magic_screen')
                        self.game.line2.step()
                        self.cancel_delayed("line2_animation")
                        self.animate_line2([self.game,1,2])
                                
                self.delay(name="display", delay=0.1, handler=graphics.galaxy.display, param=self)

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
                    if self.game.mystic_lines.position >= 4:
                        self.game.sound.play('magic_screen')
                        self.game.line2.step()
                        self.cancel_delayed("line2_animation")
                        self.animate_line2([self.game,1,2])
                                
                self.delay(name="display", delay=0.1, handler=graphics.galaxy.display, param=self)
                self.delay(name="right", delay=0.6, handler=self.sw_right_active_for_500ms, param=sw)


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
                    if self.game.mystic_lines.position >= 4:
                        self.game.sound.play('magic_screen')
                        self.game.line2.step()
                        self.cancel_delayed("line2_animation")
                        self.animate_line2([self.game,1,2])
                                
                self.delay(name="display", delay=0.1, handler=graphics.galaxy.display, param=self)

    def sw_letterb_active_for_500ms(self,sw):
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
                        self.game.sound.play('magic_screen')
                        self.game.line2.step()
                        self.cancel_delayed("line2_animation")
                        self.animate_line2([self.game,1,2])
                                
                self.delay(name="display", delay=0.1, handler=graphics.galaxy.display, param=self)
                self.delay(name="letterb", delay=0.6, handler=self.sw_letterb_active_for_500ms, param=sw)

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

                if self.game.ball_count.position < max_ball:
                    if self.game.mystic_lines.position >= 2:
                        self.game.sound.play('magic_screen')
                        self.game.line1.step()
                        self.cancel_delayed("line1_animation")
                        self.animate_line1([self.game,1,1])
                                
                self.delay(name="display", delay=0.1, handler=graphics.galaxy.display, param=self)

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

                if self.game.ball_count.position < max_ball:
                    if self.game.mystic_lines.position >= 2:
                        self.game.sound.play('magic_screen')
                        self.game.line1.step()
                        self.cancel_delayed("line1_animation")
                        self.animate_line1([self.game,1,1])
                                
                self.delay(name="display", delay=0.1, handler=graphics.galaxy.display, param=self)
                self.delay(name="left", delay=0.6, handler=self.sw_left_active_for_500ms, param=sw)

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

                if self.game.ball_count.position < max_ball:
                    if self.game.mystic_lines.position >= 2:
                        self.game.sound.play('magic_screen')
                        self.game.line1.step()
                        self.cancel_delayed("line1_animation")
                        self.animate_line1([self.game,1,1])
                                
                self.delay(name="display", delay=0.1, handler=graphics.galaxy.display, param=self)

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

                if self.game.ball_count.position < max_ball:
                    if self.game.mystic_lines.position >= 2:
                        self.game.sound.play('magic_screen')
                        self.game.line1.step()
                        self.cancel_delayed("line1_animation")
                        self.animate_line1([self.game,1,1])
                                
                self.delay(name="display", delay=0.1, handler=graphics.galaxy.display, param=self)
                self.delay(name="lettera", delay=0.6, handler=self.sw_lettera_active_for_500ms, param=sw)


    def sw_left_active_for_2s(self, sw):
        max_ball = 0
        if self.game.selection_feature.position < 7:
            max_ball = 4
        elif self.game.selection_feature.position < 8:
            max_ball = 5
        else:
            if self.game.selection_feature.position == 9:
                max_ball = 6

        if self.game.ball_count.position < max_ball:

            if self.game.b_return.status == True:
                self.game.coils.holdLeft.enable()
                self.check_shutter()
                self.game.b_return.disengage()
                self.game.ball_return_played.engage(self.game)
                self.game.sound.play('tilt')
                self.game.coils.holdLeft.disable()
                if 9 in self.holes:
                    if self.game.switches.hole9.is_inactive():
                        self.holes.remove(9)
                if 7 in self.holes:
                    if self.game.switches.hole7.is_inactive():
                        self.holes.remove(7)
                if 16 in self.holes:
                    if self.game.switches.hole16.is_inactive():
                        self.holes.remove(16)
                if 2 in self.holes:
                    if self.game.switches.hole2.is_inactive():
                        self.holes.remove(2)
                if 8 in self.holes:
                    if self.game.switches.hole8.is_inactive():
                        self.holes.remove(8)
                if 20 in self.holes:
                    if self.game.switches.hole20.is_inactive():
                        self.holes.remove(20)
                if 11 in self.holes:
                    if self.game.switches.hole11.is_inactive():
                        self.holes.remove(11)
                if 17 in self.holes:
                    if self.game.switches.hole17.is_inactive():
                        self.holes.remove(17)
                if 22 in self.holes:
                    if self.game.switches.hole22.is_inactive():
                        self.holes.remove(22)
                if 12 in self.holes:
                    if self.game.switches.hole12.is_inactive():
                        self.holes.remove(12)
                if 19 in self.holes:
                    if self.game.switches.hole19.is_inactive():
                        self.holes.remove(19)
                if 13 in self.holes:
                    if self.game.switches.hole13.is_inactive():
                        self.holes.remove(13)

        graphics.galaxy.display(self)

        self.delay(name="display", delay=0.1, handler=graphics.galaxy.display, param=self)

    def sw_right_active_for_2s(self, sw):
        max_ball = 0
        if self.game.selection_feature.position < 7:
            max_ball = 4
        elif self.game.selection_feature.position < 8:
            max_ball = 5
        else:
            if self.game.selection_feature.position == 9:
                max_ball = 6

        if self.game.ball_count.position < max_ball:

            if self.game.b_return.status == True:
                self.game.coils.holdRight.enable()
                self.check_shutter()
                self.game.b_return.disengage()
                self.game.ball_return_played.engage(self.game)
                self.game.sound.play('tilt')
                self.game.coils.holdRight.disable()
                if 6 in self.holes:
                    if self.game.switches.hole6.is_inactive():
                        self.holes.remove(6)
                if 14 in self.holes:
                    if self.game.switches.hole14.is_inactive():
                        self.holes.remove(14)
                if 24 in self.holes:
                    if self.game.switches.hole24.is_inactive():
                        self.holes.remove(24)
                if 15 in self.holes:
                    if self.game.switches.hole15.is_inactive():
                        self.holes.remove(15)
                if 18 in self.holes:
                    if self.game.switches.hole18.is_inactive():
                        self.holes.remove(18)
                if 3 in self.holes:
                    if self.game.switches.hole3.is_inactive():
                        self.holes.remove(3)
                if 21 in self.holes:
                    if self.game.switches.hole21.is_inactive():
                        self.holes.remove(21)
                if 5 in self.holes:
                    if self.game.switches.hole5.is_inactive():
                        self.holes.remove(5)
                if 4 in self.holes:
                    if self.game.switches.hole4.is_inactive():
                        self.holes.remove(4)
                if 10 in self.holes:
                    if self.game.switches.hole10.is_inactive():
                        self.holes.remove(10)
                if 1 in self.holes:
                    if self.game.switches.hole1.is_inactive():
                        self.holes.remove(1)
                if 23 in self.holes:
                    if self.game.switches.hole23.is_inactive():
                        self.holes.remove(23)
        graphics.galaxy.display(self)

        self.delay(name="display", delay=0.1, handler=graphics.galaxy.display, param=self)


    def check_selection(self):
        self.delay(name="display", delay=0.1, handler=graphics.galaxy.display, param=self)

    def check_shutter(self, start=0):
        if start == 1 or self.game.b_return.status == True:
            if self.game.switches.smRunout.is_active():
                if self.game.switches.shutter.is_active():
                    self.game.coils.shutter.disable()
        else:
            if self.game.switches.shutter.is_inactive():
                if self.game.switches.smRunout.is_active():
                    self.game.coils.shutter.disable()


    def regular_play(self):
        self.cancel_delayed(name="both_animation")
        self.cancel_delayed(name="odds_animation")
        self.cancel_delayed(name="feature_animation")
        self.cancel_delayed(name="search")
        self.cancel_delayed(name="red_replay_step_up")
        self.cancel_delayed(name="yellow_replay_step_up")
        self.cancel_delayed(name="green_replay_step_up")
        self.cancel_delayed(name="blue_replay_step_up")
        self.cancel_delayed(name="blink")
        self.cancel_delayed(name="blink_return")
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
        begin = self.game.program.position
        self.game.program.spin()
        self.game.scramble.spin()
        self.game.probability.spin()
        self.game.reflex.decrease()
        if self.game.features.status == True:
            self.animate_features_scan([begin,self.game.program.movement_amount,1])
        if self.game.all_advantages.status == True:
            self.animate_both([begin,self.game.program.movement_amount,1])
        if self.game.odds_only.status == True:
            self.animate_odds_scan([begin,self.game.program.movement_amount,1])

        self.game.returned = False
        if self.game.start.status == True:
            self.game.coin.step()
            if self.game.selector.position < 1:
                self.game.selector.step()
            if self.game.switches.shutter.is_inactive():
                self.game.coils.shutter.enable()
            self.replay_step_down()
            graphics.galaxy.display(self)
            self.check_lifter_status()
        else:
            self.holes = []
            self.game.start.engage(self.game)
            self.game.yellow_odds.reset()
            self.game.green_odds.reset()
            self.game.blue_odds.reset()
            self.game.ball_count.reset()
            self.game.extra_ball.reset()
            self.game.b_return.disengage()
            self.game.ball_return_played.disengage()
            self.game.selection_feature.reset()
            self.game.timer.reset()
            if self.game.line1.position not in [0,2]:
                self.game.sound.play('magic_screen')
                self.game.line1.step()
                self.cancel_delayed("line1_animation")
                self.animate_line1([self.game,1,1])
            if self.game.line2.position not in [0,2]:
                self.game.sound.play('magic_screen')
                self.game.line2.step()
                self.cancel_delayed("line2_animation")
                self.animate_line2([self.game,1,2])
            if self.game.line3.position not in [0,2]:
                self.game.sound.play('magic_screen')
                self.game.line3.step()
                self.cancel_delayed("line3_animation")
                self.animate_line3([self.game,1,3])
            self.game.mystic_lines.reset()
            self.game.red_replay_counter.reset()
            self.game.blue_replay_counter.reset()
            self.game.yellow_replay_counter.reset()
            self.game.green_replay_counter.reset()
            self.game.diagonal_score.disengage()
            self.game.red_odds.reset()
            self.game.selector.reset()
            self.game.timer.reset()
            self.game.sound.play_music('motor', -1)
            self.regular_play()
        self.delay(name="display", delay=0.1, handler=graphics.galaxy.display, param=self)
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
        if self.game.ball_count.position == 4:
            self.game.sound.play('tilt')
            self.game.sound.play('tilt')
        if self.game.switches.shutter.is_active():
            self.game.coils.shutter.enable()
        if self.game.ball_count.position <= 7:
            self.check_lifter_status()
        self.delay(name="display", delay=0.1, handler=graphics.galaxy.display, param=self)


    # This is really nasty, but it is how we render graphics for each individual hole.
    # numbers are added (or removed from) a list.  In this way, I can re-use the same
    # routine even for games where there are ball return functions like Surf Club.

    def sw_hole1_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(1)
            self.delay(name="display", delay=0.1, handler=graphics.galaxy.display, param=self)

    def sw_hole2_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(2)
            self.delay(name="display", delay=0.1, handler=graphics.galaxy.display, param=self)

    def sw_hole3_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(3)
            self.delay(name="display", delay=0.1, handler=graphics.galaxy.display, param=self)

    def sw_hole4_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(4)
            self.delay(name="display", delay=0.1, handler=graphics.galaxy.display, param=self)

    def sw_hole5_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(5)
            self.delay(name="display", delay=0.1, handler=graphics.galaxy.display, param=self)

    def sw_hole6_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(6)
            self.delay(name="display", delay=0.1, handler=graphics.galaxy.display, param=self)

    def sw_hole7_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(7)
            self.delay(name="display", delay=0.1, handler=graphics.galaxy.display, param=self)

    def sw_hole8_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(8)
            self.delay(name="display", delay=0.1, handler=graphics.galaxy.display, param=self)

    def sw_hole9_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(9)
            self.delay(name="display", delay=0.1, handler=graphics.galaxy.display, param=self)

    def sw_hole10_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(10)
            self.delay(name="display", delay=0.1, handler=graphics.galaxy.display, param=self)

    def sw_hole11_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(11)
            self.delay(name="display", delay=0.1, handler=graphics.galaxy.display, param=self)

    def sw_hole12_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(12)
            self.delay(name="display", delay=0.1, handler=graphics.galaxy.display, param=self)

    def sw_hole13_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(13)
            self.delay(name="display", delay=0.1, handler=graphics.galaxy.display, param=self)

    def sw_hole14_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(14)
            self.delay(name="display", delay=0.1, handler=graphics.galaxy.display, param=self)

    def sw_hole15_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(15)
            self.delay(name="display", delay=0.1, handler=graphics.galaxy.display, param=self)

    def sw_hole16_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(16)
            self.delay(name="display", delay=0.1, handler=graphics.galaxy.display, param=self)

    def sw_hole17_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(17)
            self.delay(name="display", delay=0.1, handler=graphics.galaxy.display, param=self)

    def sw_hole18_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(18)
            self.delay(name="display", delay=0.1, handler=graphics.galaxy.display, param=self)

    def sw_hole19_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(19)
            self.delay(name="display", delay=0.1, handler=graphics.galaxy.display, param=self)

    def sw_hole20_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(20)
            self.delay(name="display", delay=0.1, handler=graphics.galaxy.display, param=self)

    def sw_hole21_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(21)
            self.delay(name="display", delay=0.1, handler=graphics.galaxy.display, param=self)
    
    def sw_hole22_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(22)
            self.delay(name="display", delay=0.1, handler=graphics.galaxy.display, param=self)
    
    def sw_hole23_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(23)
            self.delay(name="display", delay=0.1, handler=graphics.galaxy.display, param=self)
    
    def sw_hole24_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(24)
            self.delay(name="display", delay=0.1, handler=graphics.galaxy.display, param=self)

    def sw_replayReset_active(self, sw):
        self.game.anti_cheat.disengage()
        self.holes = []
        graphics.galaxy.display(self)
        self.tilt_actions()
        self.replay_step_down(self.game.replays)

    def tilt_actions(self):
        self.game.start.disengage()
        self.game.coin.reset()
        self.cancel_delayed(name="replay_reset")
        self.cancel_delayed(name="red_replay_step_up")
        self.cancel_delayed(name="yellow_replay_step_up")
        self.cancel_delayed(name="green_replay_step_up")
        self.cancel_delayed(name="blue_replay_step_up")
        self.cancel_delayed(name="blink")
        self.cancel_delayed(name="blink_return")
        self.cancel_delayed(name="timeout")
        self.game.search_index.disengage()
        if self.game.ball_count.position == 0:
            if self.game.switches.shutter.is_active():
                self.game.coils.shutter.enable()
        self.holes = []
        self.game.yellow_odds.reset()
        self.game.green_odds.reset()
        self.game.blue_odds.reset()
        self.game.ball_count.reset()
        self.game.extra_ball.reset()
        self.game.eb_play.disengage()
        self.game.features.disengage()
        self.game.odds_only.disengage()
        self.game.all_advantages.engage(self.game)
        self.game.b_return.disengage()
        self.game.ball_return_played.disengage()
        self.game.selection_feature.reset()
        self.game.timer.reset()
        self.game.mystic_lines.reset()
        self.game.red_replay_counter.reset()
        self.game.diagonal_score.disengage()
        self.game.blue_replay_counter.reset()
        self.game.yellow_replay_counter.reset()
        self.game.green_replay_counter.reset()
        self.game.red_odds.reset()
        self.game.selector.reset()
        self.game.selector.reset()
        self.game.anti_cheat.engage(game)
        self.game.tilt.engage(self.game)
        self.game.sound.stop_music()
        self.game.sound.play('tilt')
        # displays "Tilt" on the backglass, you have to recoin.
        self.delay(name="display", delay=0.1, handler=graphics.galaxy.display, param=self)

    def sw_tilt_active(self, sw):
        if self.game.tilt.status == False:
            self.tilt_actions()

    def replay_step_down(self, number=0):
        if number > 0:
            if number > 1:
                self.game.replays -= 1
                graphics.replay_step_down(self.game.replays, graphics.galaxy.reel1, graphics.galaxy.reel10, graphics.galaxy.reel100, graphics.galaxy.reel1000)
                self.game.coils.registerDown.pulse()
                number -= 1
                self.delay(name="display", delay=0, handler=graphics.galaxy.display, param=self)
                self.delay(name="replay_reset", delay=0.13, handler=self.replay_step_down, param=number)
            elif number == 1:
                self.game.replays -= 1
                graphics.replay_step_down(self.game.replays, graphics.galaxy.reel1, graphics.galaxy.reel10, graphics.galaxy.reel100, graphics.galaxy.reel1000)
                self.game.coils.registerDown.pulse()
                number -= 1
                self.delay(name="display", delay=0, handler=graphics.galaxy.display, param=self)
                self.cancel_delayed(name="replay_reset")
        else: 
            if self.game.replays > 0:
                self.game.replays -= 1
                graphics.replay_step_down(self.game.replays, graphics.galaxy.reel1, graphics.galaxy.reel10, graphics.galaxy.reel100, graphics.galaxy.reel1000)
                self.delay(name="display", delay=0.1, handler=graphics.galaxy.display, param=self)
            self.game.coils.registerDown.pulse()

    def replay_step_up(self):
        if self.game.replays < 8999:
            self.game.replays += 1
            graphics.replay_step_up(self.game.replays, graphics.galaxy.reel1, graphics.galaxy.reel10, graphics.galaxy.reel100, graphics.galaxy.reel1000)
        self.game.coils.registerUp.pulse()
        self.game.reflex.increase()
        graphics.galaxy.display(self)

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
       
        for i in range(0, 15):
            self.r = self.closed_search_relays(self.game.searchdisc.position)
            self.game.searchdisc.spin()
            self.wipers = self.r[0]
            self.red = self.r[1]
            self.yellow = self.r[2]
            self.green = self.r[3]
            self.blue = self.r[4]
            self.diagonal_score = self.r[5]

            # From here, I need to determine based on the value of r, whether to latch the search index and score. 
            # I need to determine the best winner on each card.  To do this, I must compare the position of the replay counter before
            # determining the winner. Reminder that my replay counters are a 1:1 representation.

            self.match = []
            relays = 0
            for key in self.wipers:
                for number in self.holes:
                    if number == key:
                        self.match.append(self.wipers[key])
                        relays = sorted(set(self.match))
                        #TODO Play sound for each relay closure.
                        s = functions.count_seq(relays)
                        if s >= 2:
                            self.find_winner(s, self.red, self.yellow, self.green, self.blue, self.diagonal_score)
                            break


    def find_winner(self, relays, red, yellow, green, blue, diagonal_score):
        if self.game.search_index.status == False and self.game.replays < 8999:
            if self.game.red_odds.position == 1:
                redthreeodds = 4
                redfourodds = 8
                redfiveodds = 32
            elif self.game.red_odds.position == 2:
                redthreeodds = 8
                redfourodds = 16
                redfiveodds = 64
            elif self.game.red_odds.position == 3:
                redthreeodds = 12
                redfourodds = 24
                redfiveodds = 96
            elif self.game.red_odds.position == 4:
                redthreeodds = 24
                redfourodds = 48
                redfiveodds = 128
            elif self.game.red_odds.position == 5:
                redthreeodds = 48
                redfourodds = 96
                redfiveodds = 192
            elif self.game.red_odds.position == 6:
                redthreeodds = 72
                redfourodds = 144
                redfiveodds = 216
            elif self.game.red_odds.position == 7:
                redthreeodds = 96
                redfourodds = 192
                redfiveodds = 288
            elif self.game.red_odds.position == 8:
                redthreeodds = 120
                redfourodds = 216
                redfiveodds = 384
            elif self.game.red_odds.position == 9:
                redthreeodds = 144
                redfourodds = 240
                redfiveodds = 432
            elif self.game.red_odds.position == 10:
                redthreeodds = 168
                redfourodds = 288
                redfiveodds = 576
            elif self.game.red_odds.position == 11:
                redthreeodds = 192
                redfourodds = 384
                redfiveodds = 768
            if self.game.green_odds.position == 1:
                greenthreeodds = 4
                greenfourodds = 8
                greenfiveodds = 32
            elif self.game.green_odds.position == 2:
                greenthreeodds = 8
                greenfourodds = 16
                greenfiveodds = 64
            elif self.game.green_odds.position == 3:
                greenthreeodds = 12
                greenfourodds = 24
                greenfiveodds = 96
            elif self.game.green_odds.position == 4:
                greenthreeodds = 24
                greenfourodds = 48
                greenfiveodds = 128
            elif self.game.green_odds.position == 5:
                greenthreeodds = 48
                greenfourodds = 96
                greenfiveodds = 192
            elif self.game.green_odds.position == 6:
                greenthreeodds = 72
                greenfourodds = 144
                greenfiveodds = 216
            elif self.game.green_odds.position == 7:
                greenthreeodds = 96
                greenfourodds = 192
                greenfiveodds = 288
            elif self.game.green_odds.position == 8:
                greenthreeodds = 120
                greenfourodds = 216
                greenfiveodds = 384
            elif self.game.green_odds.position == 9:
                greenthreeodds = 144
                greenfourodds = 240
                greenfiveodds = 432
            elif self.game.green_odds.position == 10:
                greenthreeodds = 168
                greenfourodds = 288
                greenfiveodds = 576
            elif self.game.green_odds.position == 11:
                greenthreeodds = 192
                greenfourodds = 384
                greenfiveodds = 768
            if self.game.yellow_odds.position == 1:
                yellowthreeodds = 4
                yellowfourodds = 8
                yellowfiveodds = 32
            elif self.game.yellow_odds.position == 2:
                yellowthreeodds = 8
                yellowfourodds = 16
                yellowfiveodds = 64
            elif self.game.yellow_odds.position == 3:
                yellowthreeodds = 12
                yellowfourodds = 24
                yellowfiveodds = 96
            elif self.game.yellow_odds.position == 4:
                yellowthreeodds = 24
                yellowfourodds = 48
                yellowfiveodds = 128
            elif self.game.yellow_odds.position == 5:
                yellowthreeodds = 48
                yellowfourodds = 96
                yellowfiveodds = 192
            elif self.game.yellow_odds.position == 6:
                yellowthreeodds = 72
                yellowfourodds = 144
                yellowfiveodds = 216
            elif self.game.yellow_odds.position == 7:
                yellowthreeodds = 96
                yellowfourodds = 192
                yellowfiveodds = 288
            elif self.game.yellow_odds.position == 8:
                yellowthreeodds = 120
                yellowfourodds = 216
                yellowfiveodds = 384
            elif self.game.yellow_odds.position == 9:
                yellowthreeodds = 144
                yellowfourodds = 240
                yellowfiveodds = 432
            elif self.game.yellow_odds.position == 10:
                yellowthreeodds = 168
                yellowfourodds = 288
                yellowfiveodds = 576
            elif self.game.yellow_odds.position == 11:
                yellowthreeodds = 192
                yellowfourodds = 384
                yellowfiveodds = 768
            if self.game.blue_odds.position == 1:
                bluethreeodds = 4
                bluefourodds = 8
                bluefiveodds = 32
            elif self.game.blue_odds.position == 2:
                bluethreeodds = 8
                bluefourodds = 16
                bluefiveodds = 64
            elif self.game.blue_odds.position == 3:
                bluethreeodds = 12
                bluefourodds = 24
                bluefiveodds = 96
            elif self.game.blue_odds.position == 4:
                bluethreeodds = 24
                bluefourodds = 48
                bluefiveodds = 128
            elif self.game.blue_odds.position == 5:
                bluethreeodds = 48
                bluefourodds = 96
                bluefiveodds = 192
            elif self.game.blue_odds.position == 6:
                bluethreeodds = 72
                bluefourodds = 144
                bluefiveodds = 216
            elif self.game.blue_odds.position == 7:
                bluethreeodds = 96
                bluefourodds = 192
                bluefiveodds = 288
            elif self.game.blue_odds.position == 8:
                bluethreeodds = 120
                bluefourodds = 216
                bluefiveodds = 384
            elif self.game.blue_odds.position == 9:
                bluethreeodds = 144
                bluefourodds = 240
                bluefiveodds = 432
            elif self.game.blue_odds.position == 10:
                bluethreeodds = 168
                bluefourodds = 288
                bluefiveodds = 576
            elif self.game.blue_odds.position == 11:
                bluethreeodds = 192
                bluefourodds = 384
                bluefiveodds = 768

            redsixodds = redfiveodds + 192
            yellowsixodds = yellowfiveodds + 192
            greensixodds = greenfiveodds + 192
            bluesixodds = bluefiveodds + 192

            if relays == 3:
                if diagonal_score:
                    if self.game.diagonal_score.status == True:
                        if red:
                            if self.game.red_replay_counter.position < redthreeodds:
                                self.game.search_index.engage(self.game)
                                self.red_replay_step_up(redthreeodds - self.game.red_replay_counter.position)
                        if yellow:
                            if self.game.yellow_replay_counter.position < yellowthreeodds:
                                self.game.search_index.engage(self.game)
                                self.yellow_replay_step_up(yellowthreeodds - self.game.yellow_replay_counter.position)
                        if green:
                            if self.game.green_replay_counter.position < greenthreeodds:
                                self.game.search_index.engage(self.game)
                                self.green_replay_step_up(greenthreeodds - self.game.green_replay_counter.position)
                        if blue:
                            if self.game.blue_replay_counter.position < bluethreeodds:
                                self.game.search_index.engage(self.game)
                                self.blue_replay_step_up(bluethreeodds - self.game.blue_replay_counter.position)
                else:
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
                if diagonal_score:
                    if self.game.diagonal_score.status == True:
                        if red == 1:
                            if self.game.red_replay_counter.position < redfourodds:
                                self.game.search_index.engage(self.game)
                                self.red_replay_step_up(redfourodds - self.game.red_replay_counter.position)
                        elif yellow == 1:
                            if self.game.yellow_replay_counter.position < yellowfourodds:
                                self.game.search_index.engage(self.game)
                                self.yellow_replay_step_up(yellowfourodds - self.game.yellow_replay_counter.position)
                        elif green == 1:
                            if self.game.green_replay_counter.position < greenfourodds:
                                self.game.search_index.engage(self.game)
                                self.green_replay_step_up(greenfourodds - self.game.green_replay_counter.position)
                        elif blue == 1:
                            if self.game.blue_replay_counter.position < bluefourodds:
                                self.game.search_index.engage(self.game)
                                self.blue_replay_step_up(bluefourodds - self.game.blue_replay_counter.position)
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
            if relays == 6:
                if (red == 1):
                    if self.game.search_index.status == False:
                        if self.game.red_replay_counter.position < redsixodds:
                            self.game.search_index.engage(self.game)
                            self.red_replay_step_up(redsixodds - self.game.red_replay_counter.position)
                if (yellow == 1):
                    if self.game.search_index.status == False:
                        if self.game.yellow_replay_counter.position < yellowsixodds:
                            self.game.search_index.engage(self.game)
                            self.yellow_replay_step_up(yellowsixodds - self.game.yellow_replay_counter.position)
                if (green == 1):
                    if self.game.search_index.status == False:
                        if self.game.green_replay_counter.position < greensixodds:
                            self.game.search_index.engage(self.game)
                            self.green_replay_step_up(greensixodds - self.game.green_replay_counter.position)
                if (blue == 1):
                    if self.game.search_index.status == False:
                        if self.game.blue_replay_counter.position < bluesixodds:
                            self.game.search_index.engage(self.game)
                            self.blue_replay_step_up(bluesixodds - self.game.blue_replay_counter.position)


    def blue_replay_step_up(self, number):
        self.game.sound.stop('search')
        if number >= 1:
            self.game.blue_replay_counter.step()
            number -= 1
            self.replay_step_up()
            if self.game.replays == 8999:
                number = 0
            self.delay(name="blue_replay_step_up", delay=0.15, handler=self.blue_replay_step_up, param=number)
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
            self.delay(name="red_replay_step_up", delay=0.15, handler=self.red_replay_step_up, param=number)
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
            self.delay(name="yellow_replay_step_up", delay=0.15, handler=self.yellow_replay_step_up, param=number)
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
            self.delay(name="green_replay_step_up", delay=0.15, handler=self.green_replay_step_up, param=number)
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
        blue = False
        diagonal = False

        if self.game.line1.position in [0,2]:
            self.p1 = 9
            self.p2 = 8
            self.q1 = 7
            self.q2 = 20
            self.r1 = 16
            self.r2 = 11
            self.s1 = 2
            self.s2 = 17
        elif self.game.line1.position == 1:
            self.p1 = 7
            self.p2 = 9
            self.q1 = 16
            self.q2 = 8
            self.r1 = 2
            self.r2 = 20
            self.s1 = 17
            self.s2 = 11
        elif self.game.line1.position == 3:
            self.p1 = 8
            self.p2 = 20
            self.q1 = 9
            self.q2 = 11
            self.r1 = 7
            self.r2 = 17
            self.s1 = 16
            self.s2 = 2

        if self.game.line2.position in [0,2]:
            self.p3 = 22
            self.p4 = 6
            self.q3 = 12
            self.q4 = 14
            self.r3 = 19
            self.r4 = 24
            self.s3 = 13
            self.s4 = 15
        elif self.game.line2.position == 1:
            self.p3 = 12
            self.p4 = 22
            self.q3 = 19
            self.q4 = 6
            self.r3 = 13
            self.r4 = 14
            self.s3 = 15
            self.s4 = 24
        elif self.game.line2.position == 3:
            self.p3 = 6
            self.p4 = 14
            self.q3 = 22
            self.q4 = 24
            self.r3 = 12
            self.r4 = 15
            self.s3 = 19
            self.s4 = 13

        if self.game.line3.position in [0,2]:
            self.p5 = 18
            self.p6 = 4
            self.q5 = 3
            self.q6 = 10
            self.r5 = 21
            self.r6 = 1
            self.s5 = 5
            self.s6 = 23
        elif self.game.line3.position == 1:
            self.p5 = 3
            self.p6 = 18
            self.q5 = 21
            self.q6 = 4
            self.r5 = 5
            self.r6 = 10
            self.s5 = 23
            self.s6 = 1
        elif self.game.line3.position == 3:
            self.p5 = 4
            self.p6 = 10
            self.q5 = 18
            self.q6 = 1
            self.r5 = 3
            self.r6 = 23
            self.s5 = 21
            self.s6 = 5

        self.pos[0] = {}
        #Red
        self.pos[1] = {self.p1:1, self.p2:2, self.p3:3, self.p4:4, self.p5:5, self.p6:6}
        self.pos[2] = {self.p2:1, self.q2:2, self.r2:3, self.s2:4}
        self.pos[3] = {self.p4:1, self.q4:2, self.r4:3, self.s4:4}
        #D
        self.pos[4] = {self.p1:1, self.q2:2, self.r3:3, self.s4:4}
        #Green
        self.pos[5] = {self.q1:1, self.q2:2, self.q3:3, self.q4:4, self.q5:5, self.q6:6}
        self.pos[6] = {self.p1:1, self.q1:2, self.r1:3, self.s1:4}
        #D
        self.pos[7] = {self.p3:1, self.q4:2, self.r5:3, self.s6:4}
        #Yellow
        self.pos[8] = {self.r1:1, self.r2:2, self.r3:3, self.r4:4, self.r5:5, self.r6:6}
        self.pos[9] = {self.p3:1, self.q3:2, self.r3:3, self.s3:4}
        self.pos[10] = {self.p5:1, self.q5:2, self.r5:3, self.s5:4}
        #D
        self.pos[11] = {self.s1:1, self.r2:2, self.q3:3, self.p4:4}
        #Blue
        self.pos[12] = {self.s1:1, self.s2:2, self.s3:3, self.s4:4, self.s5:5, self.s6:6}
        self.pos[13] = {self.p6:1, self.q6:2, self.r6:3, self.s6:4}
        #D
        self.pos[14] = {self.s3:1, self.r4:2, self.q5:3, self.p6:4}

        if rivets in [1,2,3,4]:
            red = True
            if rivets == 4:
                diagonal = True
        if rivets in [5,6,7]:
            green = True
            if rivets == 7:
                diagonal = True
        if rivets in [8,9,10,11]:
            yellow = True
            if rivets == 11:
                diagonal = True
        if rivets in [12,13,14]:
            blue = True
            if rivets == 14:
                diagonal = True
                
        return (self.pos[rivets], red, yellow, green, blue, diagonal)

    
    def scan_all(self):
        self.all_probability()

    def all_probability(self):
        if self.game.red_odds.position <= 1 or self.game.yellow_odds.position <= 1 or self.game.green_odds.position <= 1 or self.game.blue_odds.position <= 1:
            self.scan_odds()
            return
        if self.game.reflex.connected_rivet() == 0:
            self.scan_odds()
            if self.game.red_odds.position > 0:
                self.scan_features()
        if self.game.reflex.connected_rivet() == 1:
            self.scan_odds()
            if self.game.red_odds.position > 0:
                self.scan_features()
        elif self.game.reflex.connected_rivet() == 2:
            self.scan_odds()
            if self.game.red_odds.position > 0:
                self.scan_features()
        elif self.game.reflex.connected_rivet() == 3:
            self.scan_odds()
            if self.game.red_odds.position > 0:
                self.scan_features()
        elif self.game.reflex.connected_rivet() == 4:
            self.scan_odds()
            if self.game.red_odds.position > 0:
                self.scan_features()
        else:
            if self.game.cu:
                self.scan_odds()


    def green_extra_step(self, number):
        if number > 0:
            self.game.green_odds.step()
            self.delay(name="display", delay=0.1, handler=graphics.galaxy.display, param=self)
            number -= 1
            self.delay(name="extra_step", delay=0.1, handler=self.green_extra_step, param=number)

    def red_extra_step(self, number):
        if number > 0:
            self.game.red_odds.step()
            self.delay(name="display", delay=0.1, handler=graphics.galaxy.display, param=self)
            number -= 1
            self.delay(name="extra_step", delay=0.1, handler=self.red_extra_step, param=number)

    def yellow_extra_step(self, number):
        if number > 0:
            self.game.yellow_odds.step()
            self.delay(name="display", delay=0.1, handler=graphics.galaxy.display, param=self)
            number -= 1
            self.delay(name="extra_step", delay=0.1, handler=self.yellow_extra_step, param=number)

    def blue_extra_step(self, number):
        if number > 0:
            self.game.blue_odds.step()
            self.delay(name="display", delay=0.1, handler=graphics.galaxy.display, param=self)
            number -= 1
            self.delay(name="extra_step", delay=0.1, handler=self.blue_extra_step, param=number)

    def check_extra_step(self):
        i = random.randint(0,32)
        if i == 16:
            return 1
        else:
            return 0

    def scan_odds(self):
        if self.game.odds_only.status == True and self.game.red_odds.position > 0:
            if self.game.red_odds.position < 3:
                self.red_extra_step(3 - self.game.red_odds.position)
            if self.game.yellow_odds.position < 3:
                self.yellow_extra_step(3 - self.game.yellow_odds.position)
            if self.game.green_odds.position < 3:
                self.green_extra_step(3 - self.game.green_odds.position)
            if self.game.blue_odds.position < 3:
                self.blue_extra_step(3 - self.game.blue_odds.position)
            return
        if self.game.red_odds.position <= 1 or self.game.yellow_odds.position <= 1 or self.game.green_odds.position <= 1 or self.game.blue_odds.position <= 1:
            if self.game.red_odds.position <= 1:
                self.game.red_odds.step()
            if self.game.yellow_odds.position <= 1:
                self.game.yellow_odds.step()
            if self.game.green_odds.position <= 1:
                self.game.green_odds.step()
            if self.game.blue_odds.position <= 1:
                self.game.blue_odds.step()
            return
        sd = self.game.program.position
        prob = self.game.probability.position
        if sd == 5:
            if prob in [0,1,2,3,4,5,6,9,10,11,12,13,16,17,18,19,20,21,25,26,27,28,30,31,32,33,34,37,38,39,40,41,44,45,46,47,48,49]:
                self.game.red_odds.step()
                self.game.yellow_odds.step()
                self.game.green_odds.step()
                self.game.blue_odds.step()
                return
        if sd == 6:
            if prob in [7,42,3,4,5,8,9,10,11,12,17,18,19,20,21,26,27,28,29,30,35,36,37,38,43,44,45,46,47,48]:
                self.game.red_odds.step()
                self.game.yellow_odds.step()
                self.game.green_odds.step()
                self.game.blue_odds.step()
                return
        if sd == 7:
            if prob in [49,0,1,2,6,7,13,14,15,16,22,23,24,25,31,32,33,34,39,40,41,42]:
                self.game.red_odds.step()
                self.game.yellow_odds.step()
                self.game.green_odds.step()
                self.game.blue_odds.step()
                return
        if sd in [8,9]:
            if prob in [4,5,12,13,14,18,19,20,24,25,31,32,41,42,43]:
                self.game.red_odds.step()
                self.game.yellow_odds.step()
                self.game.green_odds.step()
                self.game.blue_odds.step()
                return
        if sd == 10:
            if prob in [3,6,7,8,21,22,35,36,44,45,46]:
                self.game.red_odds.step()
                self.game.yellow_odds.step()
                self.game.green_odds.step()
                self.game.blue_odds.step()
                return
        if sd == 11:
            if prob in [15,16,17,26,27,38,39,48,49]:
                self.game.red_odds.step()
                self.game.yellow_odds.step()
                self.game.green_odds.step()
                self.game.blue_odds.step()
                return
        if sd == 12:
            if prob in [7,14,28,35,49]:
                self.game.red_odds.step()
                self.game.yellow_odds.step()
                self.game.green_odds.step()
                self.game.blue_odds.step()
                return
        if sd in [0,2,4,5,6,8,9,11,15,19,20,21,23,24,26,31,37,41,42,44,47,49]:
            if self.game.scramble.position in [0,5,11,14,16]:
                self.game.red_odds.step()
        if sd in [47,21,25,27]:
            if self.game.scramble.position in [0,5,11,14,16]:
                self.red_extra_step(2)
        if sd in [28,36]:
            if self.game.scramble.position in [0,5,11,14,16]:
                self.red_extra_step(3)
        if sd in [3,7,10,11,20,22,25,28,36,38,40,46,0]:
            if self.game.scramble.position in [0,6,11,13]:
                self.game.yellow_odds.step()
        if sd in [4,25,27,28,39,32]:
            if self.game.scramble.position in [0,6,11,13]:
                self.yellow_extra_step(2)
        if sd in [1,17,46]:
            if self.game.scramble.position in [0,6,11,13]:
                self.yellow_extra_step(3)
        if sd in [4,5,12,13,18,24,27,29,30,31,32,45,48]:
            if self.game.scramble.position in [0,5,11,45,49]:
                self.game.green_odds.step()
        if sd in [2,14,17,27,29,48]:
            if self.game.scramble.position in [0,5,11,45,49]:
                self.green_extra_step(2)
        if sd in [29,41]:
            if self.game.scramble.position in [0,5,11,45,49]:
                self.green_extra_step(3)
        if sd in [1,3,11,16,18,21,22,31,33,36]:
            if self.game.scramble.position in [0,7,41,44,47]:
                self.game.blue_odds.step()
        if sd in [15,16,33,34,35,37,42]:
            if self.game.scramble.position in [0,7,41,44,47]:
                self.blue_extra_step(2)
        if sd in [9]:
            if self.game.scramble.position in [0,7,41,44,47]:
                self.blue_extra_step(3)

    def scan_features(self):
        p = self.features_probability()

    def features_probability(self):
        self.features_spotting()

    def features_spotting(self):
        if self.game.probability.position in [3,4,9,10,15,16]:
            if self.game.mystic_lines.position in [1,3]:
                self.step_mystic_lines(1)
        if self.game.probability.position in [19,20,45,46]:
            if self.game.selection_feature.position in [1,3]:
                self.step_selection(1)
        sd = self.game.program.position
        if sd in [6,36,41,14,31,32,43]:
            if self.game.b_return.status == False:
                self.game.b_return.engage(self.game)
                self.game.sound.play('tilt')
        if sd in [3,5,7,4,11]:
            if self.game.diagonal_score.status == False:
                self.game.diagonal_score.engage(self.game)
                self.game.sound.play('tilt')
        if sd in [12,13,20,34,45,47]:
            if self.game.mystic_lines.position < 2:
                if self.game.cu:
                    self.step_mystic_lines(6)
                else:
                    self.step_mystic_lines(1)
        if sd in range (21,31):
            if self.game.mystic_lines.position == 2:
                self.step_mystic_lines(1)
            else:
                if self.game.mystic_lines.position < 4:
                    if self.game.cu:
                        self.step_mystic_lines(1)
        if sd in [36,1,32,35,38,44]:
            if self.game.mystic_lines.position == 4:
                self.step_mystic_lines(1)
            else:
                if self.game.mystic_lines.position < 6:
                    if self.game.cu:
                        self.step_mystic_lines(1)
        if sd in [8,39,9,21,5]:
            if self.game.selection_feature.position == 1:
                self.step_selection(1)
        if sd in [11,41,10,9]:
                if self.game.selection_feature.position == 2:
                    self.step_selection(1)
        
    def step_mystic_lines(self, number):
        if number >= 1:
            self.game.mystic_lines.step()
            if self.game.selection_feature.position == 0:
                self.game.selection_feature.step()
            number -= 1
            self.delay(name="display", delay=0.1, handler=graphics.galaxy.display, param=self)
            self.delay(name="step_sc", delay=0.1, handler=self.step_mystic_lines, param=number)

    def step_selection(self, number):
        if number >= 1:
            self.game.selection_feature.step()
            self.check_selection()
            number -= 1
            self.delay(name="display", delay=0.1, handler=graphics.galaxy.display, param=self)
            self.delay(name="step_sc", delay=0.1, handler=self.step_selection, param=number)

    def scan_eb(self):
        if self.game.extra_ball.position == 0:
            self.game.extra_ball.step()
            self.check_lifter_status()
        self.eb_probability()
                                
        # Timer resets to 0 position on ball count increasing.  We are fudging this since we will have
        # no good way to measure balls as they return back to the trough.  The ball count unit cannot be
        # relied upon as we do not have a switch in the outhole, and the trough logic is too complex for
        # the task at hand.
        # TODO: implement thunk noises into the units.py to automatically play the noises.
        self.game.timer.reset()
        self.delay(name="display", delay=0.1, handler=graphics.galaxy.display, param=self)

    def animate_odds_scan(self, args):
        start = args[0]
        diff = args[1]
        num = args[2]
        if start + num >= 50:
            start = 0
        if diff >= 0:
            num = num + 1
            graphics.galaxy.odds_animation([self, start + num])
            self.cancel_delayed(name="display")
            diff = diff - 1
            args = [start,diff,num]
            self.delay(name="odds_animation", delay=0.07, handler=self.animate_odds_scan, param=args)
        else:
            self.cancel_delayed(name="odds_animation")
            self.delay(name="display", delay=0.1, handler=graphics.galaxy.display, param=self)
            self.scan_odds()

    def animate_features_scan(self, args):
        start = args[0]
        diff = args[1]
        num = args[2]
        if start + num >= 50:
            start = 0
        if diff >= 0:
            num = num + 1
            graphics.galaxy.feature_animation([self, start + num])
            self.cancel_delayed(name="display")
            diff = diff - 1
            args = [start,diff,num]
            self.delay(name="feature_animation", delay=0.07, handler=self.animate_features_scan, param=args)
        else:
            self.cancel_delayed(name="feature_animation")
            self.delay(name="display", delay=0.1, handler=graphics.galaxy.display, param=self)
            self.scan_features()

    def animate_both(self, args):
        start = args[0]
        diff = args[1]
        num = args[2]
        if start + num >= 50:
            start = 0
        if diff >= 0:
            num = num + 1
            graphics.galaxy.both_animation([self, start + num])
            self.cancel_delayed(name="display")
            diff = diff - 1
            args = [start,diff,num]
            self.delay(name="both_animation", delay=0.07, handler=self.animate_both, param=args)
        else:
            self.cancel_delayed(name="both_animation")
            self.delay(name="display", delay=0.1, handler=graphics.galaxy.display, param=self)
            self.scan_all()

    def animate_eb_scan(self, args):
        start = args[0]
        diff = args[1]
        num = args[2]
        if start + num >= 50:
            start = 0
        if diff >= 0:
            num = num + 1
            graphics.galaxy.eb_animation([self, start + num])
            self.cancel_delayed(name="display")
            diff = diff - 1
            args = [start,diff,num]
            self.delay(name="eb_animation", delay=0.07, handler=self.animate_eb_scan, param=args)
        else:
            self.cancel_delayed(name="eb_animation")
            self.delay(name="display", delay=0.1, handler=graphics.galaxy.display, param=self)
            self.scan_eb()

    def animate_line1(self, args):
        self.game = args[0]
        num = args[1]
        line = args[2]
        if num < 55:
            graphics.galaxy.line1_animation([self, num * -1, line])
            self.cancel_delayed(name="display")
            num = num + 1
            args = [self.game,num,line]
            self.delay(name="line1_animation", delay=0.007, handler=self.animate_line1, param=args)
        else:
            self.cancel_delayed(name="line1_animation")
            self.delay(name="display", delay=0.1, handler=graphics.galaxy.display, param=self)

    def animate_line2(self, args):
        self.game = args[0]
        num = args[1]
        line = args[2]
        if num < 55:
            graphics.galaxy.line2_animation([self, num * -1, line])
            self.cancel_delayed(name="display")
            num = num + 1
            args = [self.game,num,line]
            self.delay(name="line2_animation", delay=0.007, handler=self.animate_line2, param=args)
        else:
            self.cancel_delayed(name="line2_animation")
            self.delay(name="display", delay=0.1, handler=graphics.galaxy.display, param=self)

    def animate_line3(self, args):
        self.game = args[0]
        num = args[1]
        line = args[2]
        if num < 55:
            graphics.galaxy.line3_animation([self, num * -1, line])
            self.cancel_delayed(name="display")
            num = num + 1
            args = [self.game,num,line]
            self.delay(name="line3_animation", delay=0.007, handler=self.animate_line3, param=args)
        else:
            self.cancel_delayed(name="line3_animation")
            self.delay(name="display", delay=0.1, handler=graphics.galaxy.display, param=self)

    def eb_probability(self):
        scramble = self.game.scramble.position
        if scramble in [8,12,14,16,23]:
            if self.game.extra_ball.position < 3:
                self.step_eb(3 - self.game.extra_ball.position)
        if scramble in [1,4,7,15]:
            if self.game.extra_ball.position >= 3 and self.game.extra_ball.position < 6:
                self.step_eb(6 - self.game.extra_ball.position)
        if scramble in [0,3,10,17,19,21]:
            if self.game.extra_ball.position >= 6 and self.game.extra_ball.position < 9:
                self.step_eb(9 - self.game.extra_ball.position)
        if self.game.selection_feature.position in [4,5]:
            if scramble in [6]:
                if self.game.extra_ball.position >= 6 and self.game.extra_ball.position < 9:
                    self.step_eb(9 - self.game.extra_ball.position)
        elif self.game.selection_feature.position == 6:
            if scramble in [13]:
                if self.game.extra_ball.position >= 6 and self.game.extra_ball.position < 9:
                    self.step_eb(9 - self.game.extra_ball.position)
 
    def step_eb(self, number):
        if number >= 1:
            self.game.extra_ball.step()
            self.check_lifter_status()
            number -= 1
            self.delay(name="display", delay=0.1, handler=graphics.galaxy.display, param=self)
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

class Galaxy(procgame.game.BasicGame):
    """ Galaxy was the only 24 hole game """
    def __init__(self, machine_type):
        super(Galaxy, self).__init__(machine_type)
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

        self.scramble = units.Spotting("scramble", 50)
        self.probability = units.Spotting("probability", 50)

        self.searchdisc = units.Search("searchdisc", 14)

        #Search relays
        self.s1 = units.Relay("s1")
        self.s2 = units.Relay("s2")
        self.s3 = units.Relay("s3")
        self.s4 = units.Relay("s4")
        self.s5 = units.Relay("s5")
        self.search_index = units.Relay("search_index")

        #Odds steppers
        self.red_odds = units.Stepper("red_odds", 11, 'galaxy')
        self.yellow_odds = units.Stepper("yellow_odds", 11, 'galaxy')
        self.green_odds = units.Stepper("green_odds", 11, 'galaxy')
        self.blue_odds = units.Stepper("blue_odds", 11, 'galaxy')

        #Replay Counter
        self.red_replay_counter = units.Stepper("red_replay_counter", 1200)
        self.yellow_replay_counter = units.Stepper("yellow_replay_counter", 1200)
        self.green_replay_counter = units.Stepper("green_replay_counter", 1200)
        self.blue_replay_counter = units.Stepper("blue_replay_counter", 1200)
        
        self.selection_feature = units.Stepper("selection_feature", 6)

        #Initialize stepper units used to keep track of features or timing.
        self.timer = units.Stepper("timer", 8)
        self.ball_count = units.Stepper("ball_count", 8)

        # Initialize reflex(es) and mixers unique to this game
        self.reflex = units.Reflex("primary", 200)

        #This is a disc which has 50 positions
        #and will randomly complete paths through the various mixers to allow for odds or feature step.
        self.program = units.Spotting("program", 50)

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

        self.eb_play = units.Relay("eb_play")

        self.selector = units.Stepper("selector", 1)

        self.extra_ball = units.Stepper("extra_ball", 9)

        self.mystic_lines = units.Stepper("mystic_lines", 6)

        self.line1 = units.Stepper("line1", 3, "galaxy", "continuous")
        self.line2 = units.Stepper("line2", 3, "galaxy", "continuous")
        self.line3 = units.Stepper("line3", 3, "galaxy", "continuous")

        self.diagonal_score = units.Relay("diagonal_score")
        #Pic-a-play
        self.all_advantages = units.Relay("all_advantages")
        self.odds_only = units.Relay("odds_only")
        self.features = units.Relay("features")


        self.b_return = units.Relay("b_return")
        self.ball_return_played = units.Relay("ball_return_played")

        self.coin = units.Stepper("coin", 40, "galaxy")

        self.replays = 0
        self.returned = False

    def reset(self):
        super(Galaxy, self).reset()
        self.logger = logging.getLogger('game')
        self.load_config('bingo.yaml')
        
        main_mode = SinglecardBingo(self)
        self.modes.add(main_mode)
        
game = Galaxy(machine_type='pdb')
game.reset()
game.run_loop()
