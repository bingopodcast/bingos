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
from bingo_emulator.graphics.miss_america import *

class SinglecardBingo(procgame.game.Mode):
    def __init__(self, game):
        super(SinglecardBingo, self).__init__(game=game, priority=5)
        self.holes = []
        self.startup()
        self.game.sound.register_music('motor', "audio/woodrail_motor.wav")
        self.game.sound.register_music('search1', "audio/automatic_search_one_ball.wav")
        self.game.sound.register_music('search2', "audio/automatic_search_two_ball.wav")
        self.game.sound.register_music('search3', "audio/automatic_search_three_ball.wav")
        self.game.sound.register_music('search4', "audio/automatic_search_four_ball.wav")
        self.game.sound.register_music('search5', "audio/automatic_search_five_ball.wav")
        self.game.sound.register_music('search6', "audio/automatic_search_six_ball.wav")
        self.game.sound.register_music('search7', "audio/automatic_search_seven_ball.wav")
        self.game.sound.register_music('search8', "audio/automatic_search_eight_ball.wav")
        self.game.sound.register_sound('add', "audio/woodrail_coin.wav")
        self.game.sound.register_sound('square', "audio/magic_square.wav")
        self.game.sound.register_sound('tilt', "audio/tilt.wav")
        self.game.sound.register_sound('step', "audio/step.wav")
        self.game.sound.register_sound('eb_search', "audio/EB_Search.wav")

    def sw_coin_active(self, sw):
        if self.game.eb_play.status == False:
            self.game.sound.play_music('motor', -1)
            self.game.tilt.disengage()
            self.regular_play()
        else:
            self.cancel_delayed("eb_animation")
            self.game.sound.stop('add')
            self.game.sound.play('add')
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
            graphics.miss_america.display(self)
            self.animate_eb_scan([begin,self.game.spotting.movement_amount,self.game.spotting.movement_amount])

        self.delay(name="display", delay=0.1, handler=graphics.miss_america.display, param=self)

    def sw_startButton_active(self, sw):
        self.game.eb_play.disengage()
        self.delay(name="display", delay=0.1, handler=graphics.miss_america.display, param=self)
        if self.game.replays > 0 or self.game.switches.freeplay.is_active():
            self.game.sound.stop('add')
            self.game.sound.play('add')
            self.game.tilt.disengage()
            self.regular_play()
            self.delay(name="display", delay=0.1, handler=graphics.miss_america.display, param=self)

    def sw_enter_active(self, sw):
        if self.game.switches.left.is_active() and self.game.switches.right.is_active():
            self.game.end_run_loop()
            os.system("/home/nbaldridge/proc/bingo_emulator/start_game.sh miss_america")
        if self.game.switches.drawer.is_inactive():
            if self.game.selection_feature.position >= 7 and (self.game.lockout.status == False):
                self.game.sound.play('square')
                self.game.line3.step()
                self.cancel_delayed("line_animation")
                self.animate_line([self.game,1,3])
            self.delay(name="display", delay=0.1, handler=graphics.miss_america.display, param=self)

    def sw_enter_active_for_500ms(self,sw):
        if self.game.switches.left.is_active() and self.game.switches.right.is_active():
            self.game.end_run_loop()
            os.system("/home/nbaldridge/proc/bingo_emulator/start_game.sh miss_america")
        if self.game.switches.drawer.is_inactive():
            if self.game.selection_feature.position >= 7 and (self.game.lockout.status == False):
                self.game.sound.play('square')
                self.game.line3.step()
                self.cancel_delayed("line_animation")
                self.animate_line([self.game,1,3])
            self.delay(name="display", delay=0.1, handler=graphics.miss_america.display, param=self)
            self.delay(name="enter", delay=0.6, handler=self.sw_enter_active_for_500ms, param=sw)

    def sw_letterc_active(self, sw):
        if self.game.switches.drawer.is_active():
            if self.game.selection_feature.position >= 7 and (self.game.lockout.status == False):
                self.game.sound.play('square')
                self.game.line3.step()
                self.cancel_delayed("line_animation")
                self.animate_line([self.game,1,3])
            self.delay(name="display", delay=0.1, handler=graphics.miss_america.display, param=self)
    
    def sw_letterc_active_for_500ms(self,sw):
        if self.game.switches.drawer.is_active():
            if self.game.selection_feature.position >= 7 and (self.game.lockout.status == False):
                self.game.sound.play('square')
                self.game.line3.step()
                self.cancel_delayed("line_animation")
                self.animate_line([self.game,1,3])
            self.delay(name="display", delay=0.1, handler=graphics.miss_america.display, param=self)
            self.delay(name="letterc", delay=0.6, handler=self.sw_letterc_active_for_500ms, param=sw)
    
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

    def sw_left_active(self, sw):
        if self.game.switches.drawer.is_inactive():
            if self.game.selection_feature.position >= 5 and (self.game.lockout.status == False):
                self.game.sound.play('square')
                self.game.line1.step()
                self.cancel_delayed("line_animation")
                self.animate_line([self.game,1,1])
            self.delay(name="display", delay=0.1, handler=graphics.miss_america.display, param=self)

    def sw_left_active_for_500ms(self,sw):
        if self.game.switches.drawer.is_inactive():
            if self.game.selection_feature.position >= 5 and (self.game.lockout.status == False):
                self.game.sound.play('square')
                self.game.line1.step()
                self.cancel_delayed("line_animation")
                self.animate_line([self.game,1,1])
            self.delay(name="display", delay=0.1, handler=graphics.miss_america.display, param=self)
            self.delay(name="left", delay=0.6, handler=self.sw_left_active_for_500ms, param=sw)

    def sw_lettera_active(self, sw):
        if self.game.switches.drawer.is_active():
            if self.game.selection_feature.position >= 5 and (self.game.lockout.status == False):
                self.game.sound.play('square')
                self.game.line1.step()
                self.cancel_delayed("line_animation")
                self.animate_line([self.game,1,1])
            self.delay(name="display", delay=0.1, handler=graphics.miss_america.display, param=self)

    def sw_lettera_active_for_500ms(self,sw):
        if self.game.switches.drawer.is_active():
            if self.game.selection_feature.position >= 5 and (self.game.lockout.status == False):
                self.game.sound.play('square')
                self.game.line1.step()
                self.cancel_delayed("line_animation")
                self.animate_line([self.game,1,1])
            self.delay(name="display", delay=0.1, handler=graphics.miss_america.display, param=self)
            self.delay(name="lettera", delay=0.6, handler=self.sw_lettera_active_for_500ms, param=sw)

    def sw_right_active(self, sw):
        if self.game.switches.drawer.is_inactive():
            if self.game.selection_feature.position >= 6 and (self.game.lockout.status == False):
                self.game.sound.play('square')
                self.game.line2.step()
                self.cancel_delayed("line_animation")
                self.animate_line([self.game,1,2])
            self.delay(name="display", delay=0.1, handler=graphics.miss_america.display, param=self)

    def sw_right_active_for_500ms(self,sw):
        if self.game.switches.drawer.is_inactive():
            if self.game.selection_feature.position >= 6 and (self.game.lockout.status == False):
                self.game.sound.play('square')
                self.game.line2.step()
                self.cancel_delayed("line_animation")
                self.animate_line([self.game,1,2])
            self.delay(name="display", delay=0.1, handler=graphics.miss_america.display, param=self)
            self.delay(name="right", delay=0.6, handler=self.sw_right_active_for_500ms, param=sw)

    def sw_letterb_active(self, sw):
        if self.game.switches.drawer.is_active():
            if self.game.selection_feature.position >= 6 and (self.game.lockout.status == False):
                self.game.sound.play('square')
                self.game.line2.step()
                self.cancel_delayed("line_animation")
                self.animate_line([self.game,1,2])
            self.delay(name="display", delay=0.1, handler=graphics.miss_america.display, param=self)

    def sw_letterb_active_for_500ms(self,sw):
        if self.game.switches.drawer.is_active():
            if self.game.selection_feature.position >= 6 and (self.game.lockout.status == False):
                self.game.sound.play('square')
                self.game.line2.step()
                self.cancel_delayed("line_animation")
                self.animate_line([self.game,1,2])
            self.delay(name="display", delay=0.1, handler=graphics.miss_america.display, param=self)
            self.delay(name="letterb", delay=0.6, handler=self.sw_letterb_active_for_500ms, param=sw)

    def sw_blue_active(self, sw):
        if self.game.switches.drawer.is_inactive():
            if self.game.selection_feature.position >= 8 and (self.game.lockout.status == False):
                self.game.sound.play('square')
                self.game.line4.step()
                self.cancel_delayed("line_animation")
                self.animate_line([self.game,1,4])
            self.delay(name="display", delay=0.1, handler=graphics.miss_america.display, param=self)

    def sw_blue_active_for_500ms(self,sw):
        if self.game.switches.drawer.is_inactive():
            if self.game.selection_feature.position >= 8 and (self.game.lockout.status == False):
                self.game.sound.play('square')
                self.game.line4.step()
                self.cancel_delayed("line_animation")
                self.animate_line([self.game,1,4])
            self.delay(name="display", delay=0.1, handler=graphics.miss_america.display, param=self)
            self.delay(name="blue", delay=0.6, handler=self.sw_blue_active_for_500ms, param=sw)


    def sw_letterd_active(self, sw):
        if self.game.switches.drawer.is_active():
            if self.game.selection_feature.position >= 8 and (self.game.lockout.status == False):
                self.game.sound.play('square')
                self.game.line4.step()
                self.cancel_delayed("line_animation")
                self.animate_line([self.game,1,4])
            self.delay(name="display", delay=0.1, handler=graphics.miss_america.display, param=self)

    def sw_letterd_active_for_500ms(self,sw):
        if self.game.switches.drawer.is_active():
            if self.game.selection_feature.position >= 8 and (self.game.lockout.status == False):
                self.game.sound.play('square')
                self.game.line4.step()
                self.cancel_delayed("line_animation")
                self.animate_line([self.game,1,4])
            self.delay(name="display", delay=0.1, handler=graphics.miss_america.display, param=self)
            self.delay(name="letterd", delay=0.6, handler=self.sw_letterd_active_for_500ms, param=sw)


    def sw_green_active(self, sw):
        if self.game.switches.drawer.is_inactive():
            if self.game.selection_feature.position >= 9 and (self.game.lockout.status == False):
                self.game.sound.play('square')
                self.game.line5.step()
                self.cancel_delayed("line_animation")
                self.animate_line([self.game,1,5])
            self.delay(name="display", delay=0.1, handler=graphics.miss_america.display, param=self)

    def sw_green_active_for_500ms(self,sw):
        if self.game.switches.drawer.is_inactive():
            if self.game.selection_feature.position >= 9 and (self.game.lockout.status == False):
                self.game.sound.play('square')
                self.game.line5.step()
                self.cancel_delayed("line_animation")
                self.animate_line([self.game,1,5])
            self.delay(name="display", delay=0.1, handler=graphics.miss_america.display, param=self)
            self.delay(name="green", delay=0.6, handler=self.sw_green_active_for_500ms, param=sw)

    def sw_lettere_active(self, sw):
        if self.game.switches.drawer.is_active():
            if self.game.selection_feature.position >= 9 and (self.game.lockout.status == False):
                self.game.sound.play('square')
                self.game.line5.step()
                self.cancel_delayed("line_animation")
                self.animate_line([self.game,1,5])
            self.delay(name="display", delay=0.1, handler=graphics.miss_america.display, param=self)

    def sw_lettere_active_for_500ms(self,sw):
        if self.game.switches.drawer.is_active():
            if self.game.selection_feature.position >= 9 and (self.game.lockout.status == False):
                self.game.sound.play('square')
                self.game.line5.step()
                self.cancel_delayed("line_animation")
                self.animate_line([self.game,1,5])
            self.delay(name="display", delay=0.1, handler=graphics.miss_america.display, param=self)
            self.delay(name="lettere", delay=0.6, handler=self.sw_lettere_active_for_500ms, param=sw)


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
        self.cancel_delayed(name="white_replay_step_up")
        self.cancel_delayed(name="both_animation")
        self.cancel_delayed(name="blink")
        self.cancel_delayed(name="timeout")
        self.game.sound.play('add')
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
            if self.game.rollovers.status == True and self.game.eb_play.status == False:
                if self.game.cu:
                    self.game.coils.yellowROLamp.enable()
                    self.game.coils.redROLamp.disable()
                else:
                    self.game.coils.yellowROLamp.disable()
                    self.game.coils.redROLamp.enable()
            if self.game.switches.shutter.is_inactive():
                self.game.coils.shutter.enable()
            self.replay_step_down()
            graphics.miss_america.display(self)
            self.check_lifter_status()
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
            self.game.before_fifth.disengage()
            self.game.before_fourth.disengage()
            self.game.before_fourth.engage(self.game)
            if self.game.line1.position not in [0,2]:
                self.game.sound.play('square')
                self.game.line1.step()
                self.animate_line([self.game,1,1])
            if self.game.line2.position not in [0,2]:
                self.game.sound.play('square')
                self.game.line2.step()
                self.animate_line([self.game,1,2])
            if self.game.line3.position not in [0,2]:
                self.game.sound.play('square')
                self.game.line3.step()
                self.animate_line([self.game,1,3])
            if self.game.line4.position not in [0,2]:
                self.game.sound.play('square')
                self.game.line4.step()
                self.animate_line([self.game,1,4])
            if self.game.line5.position not in [0,2]:
                self.game.sound.play('square')
                self.game.line5.step()
                self.animate_line([self.game,1,5])
            self.game.selection_feature.reset()
            self.game.ball_count.reset()
            self.game.extra_ball.reset()
            self.game.selector.reset()
            self.game.timer.reset()
            self.game.sound.play_music('motor', -1)
            self.game.start.engage(self.game)
            self.regular_play()
        self.delay(name="display", delay=0.1, handler=graphics.miss_america.display, param=self)
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
        if self.game.ball_count.position == 5:
            self.game.sound.play('tilt')
            self.game.sound.play('tilt')
        if self.game.before_fourth.status == True:
            if self.game.ball_count.position >= 4:
                self.game.lockout.engage(self.game)
                self.game.sound.play('tilt')
        elif self.game.before_fifth.status == True:
            if self.game.ball_count.position >= 5:
                self.game.lockout.engage(self.game)
                self.game.sound.play('tilt')
                self.game.coils.redROLamp.disable()
                self.game.coils.yellowROLamp.disable()
        if self.game.ball_count.position <= 7:
            self.check_lifter_status()
        self.delay(name="display", delay=0.1, handler=graphics.miss_america.display, param=self)

    def sw_redstar_active(self, sw):
        if not self.game.cu:
            if self.game.rollovers.status == True:
                self.game.before_fifth.engage(self.game)
                self.game.sound.play('tilt')
                self.game.before_fourth.disengage()
                self.game.rollovers.disengage()
                self.game.coils.redROLamp.disable()
        self.delay(name="display", delay=0.1, handler=graphics.miss_america.display, param=self)

    def sw_yellowstar_active(self, sw):
        if self.game.cu:
            if self.game.rollovers.status == True:
                self.game.before_fifth.engage(self.game)
                self.game.sound.play('tilt')
                self.game.before_fourth.disengage()
                self.game.rollovers.disengage()
                self.game.coils.yellowROLamp.disable()
        self.delay(name="display", delay=0.1, handler=graphics.miss_america.display, param=self)

    # This is really nasty, but it is how we render graphics for each individual hole.
    # numbers are added (or removed from) a list.  In this way, I can re-use the same
    # routine even for games where there are ball return functions like Surf Club.

    def sw_hole1_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(1)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.miss_america.display, param=self)

    def sw_hole2_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(2)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.miss_america.display, param=self)

    def sw_hole3_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(3)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.miss_america.display, param=self)

    def sw_hole4_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(4)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.miss_america.display, param=self)

    def sw_hole5_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(5)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.miss_america.display, param=self)

    def sw_hole6_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(6)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.miss_america.display, param=self)

    def sw_hole7_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(7)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.miss_america.display, param=self)

    def sw_hole8_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(8)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.miss_america.display, param=self)

    def sw_hole9_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(9)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.miss_america.display, param=self)

    def sw_hole10_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(10)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.miss_america.display, param=self)

    def sw_hole11_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(11)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.miss_america.display, param=self)

    def sw_hole12_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(12)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.miss_america.display, param=self)

    def sw_hole13_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(13)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.miss_america.display, param=self)

    def sw_hole14_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(14)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.miss_america.display, param=self)

    def sw_hole15_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(15)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.miss_america.display, param=self)

    def sw_hole16_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(16)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.miss_america.display, param=self)

    def sw_hole17_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(17)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.miss_america.display, param=self)

    def sw_hole18_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(18)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.miss_america.display, param=self)

    def sw_hole19_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(19)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.miss_america.display, param=self)

    def sw_hole20_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(20)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.miss_america.display, param=self)

    def sw_hole21_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(21)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.miss_america.display, param=self)

    def sw_hole22_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(22)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.miss_america.display, param=self)

    def sw_hole23_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(23)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.miss_america.display, param=self)

    def sw_hole24_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(24)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.miss_america.display, param=self)

    def sw_hole25_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(25)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.miss_america.display, param=self)

    def sw_replayReset_active(self, sw):
        self.game.anti_cheat.disengage()
        self.holes = []
        graphics.miss_america.display(self)
        self.tilt_actions()
        self.replay_step_down(self.game.replays)

    def tilt_actions(self):
        self.game.start.disengage()
        self.cancel_delayed(name="replay_reset")
        self.cancel_delayed(name="red_replay_step_up")
        self.cancel_delayed(name="yellow_replay_step_up")
        self.cancel_delayed(name="green_replay_step_up")
        self.cancel_delayed(name="white_replay_step_up")
        self.cancel_delayed(name="blink")
        self.cancel_delayed(name="timeout")
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
        self.game.before_fifth.disengage()
        self.game.before_fourth.disengage()
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
        self.delay(name="display", delay=0.1, handler=graphics.miss_america.display, param=self)

    def search_sounds(self):
        self.game.sound.stop_music()
        if self.game.ball_count.position == 1:
            self.game.sound.play_music('search1', -1)
        if self.game.ball_count.position == 2:
            self.game.sound.play_music('search2', -1)
        if self.game.ball_count.position == 3:
            self.game.sound.play_music('search3', -1)
        if self.game.ball_count.position == 4:
            self.game.sound.play_music('search4', -1)
        if self.game.ball_count.position == 5:
            self.game.sound.play_music('search5', -1)
        if self.game.ball_count.position == 6:
            self.game.sound.play_music('search6', -1)
        if self.game.ball_count.position == 7:
            self.game.sound.play_music('search7', -1)
        if self.game.ball_count.position == 8:
            self.game.sound.play_music('search8', -1)

    def sw_tilt_active(self, sw):
        if self.game.tilt.status == False:
            self.tilt_actions()

    def replay_step_down(self, number=0):
        if number > 0:
            if number > 1:
                self.game.replays -= 1
                graphics.replay_step_down(self.game.replays, graphics.miss_america.reel1, graphics.miss_america.reel10, graphics.miss_america.reel100)
                self.game.coils.registerDown.pulse()
                number -= 1
                graphics.miss_america.display(self)
                self.delay(name="replay_reset", delay=0.13, handler=self.replay_step_down, param=number)
            elif number == 1:
                self.game.replays -= 1
                graphics.replay_step_down(self.game.replays, graphics.miss_america.reel1, graphics.miss_america.reel10, graphics.miss_america.reel100)
                self.game.coils.registerDown.pulse()
                number -= 1
                graphics.miss_america.display(self)
                self.cancel_delayed(name="replay_reset")
        else: 
            if self.game.replays > 0:
                self.game.replays -= 1
                graphics.replay_step_down(self.game.replays, graphics.miss_america.reel1, graphics.miss_america.reel10, graphics.miss_america.reel100)
                self.delay(name="display", delay=0.1, handler=graphics.miss_america.display, param=self)
            self.game.coils.registerDown.pulse()

    def replay_step_up(self):
        if self.game.replays < 899:
            self.game.replays += 1
            graphics.replay_step_up(self.game.replays, graphics.miss_america.reel1, graphics.miss_america.reel10, graphics.miss_america.reel100)
        self.game.coils.registerUp.pulse()
        self.game.reflex.increase()
        graphics.miss_america.display(self)

    def sw_yellow_active(self, sw):
        if self.game.ball_count.position >= 5:
            if self.game.eb_play.status == True and (self.game.replays > 0 or self.game.switches.freeplay.is_active()):
                self.cancel_delayed("eb_animation")
                self.game.sound.stop('add')
                self.game.sound.play('add')
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
                graphics.miss_america.display(self)
                self.animate_eb_scan([begin,self.game.spotting.movement_amount,self.game.spotting.movement_amount])
                self.delay(name="display", delay=0.1, handler=graphics.miss_america.display, param=self)
                return
            if self.game.eb_play.status == False:
                self.game.eb_play.engage(self.game)
                self.delay(name="display", delay=0.1, handler=graphics.miss_america.display, param=self)
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
        
        for i in range(0, 50):
            self.r = self.closed_search_relays(self.game.searchdisc.position, self.game.corners.status)
            self.game.searchdisc.spin()
            self.wipers = self.r[0]
            self.card = self.r[1]
            self.corners = self.r[2]
            self.color = self.r[3]
            self.num = self.r[4]

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
                            if self.color == "red":
                                if self.game.line1.position == 1:
                                    if self.num == 12:
                                        if 2 in self.holes:
                                            s += 1
                            if self.color == "yellow":
                                if self.game.line1.position == 3:
                                    if self.num == 1:
                                        if 6 in self.holes:
                                            s += 1
                                if self.game.line5.position == 1:
                                    if self.num == 4:
                                        if 4 in self.holes:
                                            s += 1
                                if self.game.line5.position == 3:
                                    if self.num == 4:
                                        if 24 in self.holes:
                                            s += 2
                            if self.color == "white":
                                if self.game.line1.position in [0,2]:
                                    if self.game.line2.position == 3:
                                        if self.num == 24:
                                            if 2 in self.holes:
                                                s += 2
                                if self.game.line5.position == 1:
                                    if self.num == 21:
                                        if 24 in self.holes:
                                            s += 1
                            if s >= 3:
                                self.find_winner(s, self.card, self.corners, self.color)
                                break

    def find_winner(self, relays, card, corners, color):
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
            elif color == "green":
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


            if relays == 3:
                if not corners:
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
                            if self.game.green_replay_counter.position < threeodds:
                                self.game.search_index.engage(self.game)
                                self.green_replay_step_up(threeodds - self.game.green_replay_counter.position)
                        elif color == "white":
                            if self.game.white_replay_counter.position < threeodds:
                                self.game.search_index.engage(self.game)
                                self.white_replay_step_up(threeodds - self.game.white_replay_counter.position)
            if relays == 4:
                if corners and self.game.corners.status == True:
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
                                if self.game.green_replay_counter.position < fourodds:
                                    self.game.search_index.engage(self.game)
                                    self.green_replay_step_up(fourodds - self.game.green_replay_counter.position)
                            elif color == "white":
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
        self.game.sound.stop_music()
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
            self.search_sounds()
            self.search()

    def yellow_replay_step_up(self, number):
        self.game.sound.stop_music()
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
            self.search_sounds()
            self.search()

    def green_replay_step_up(self, number):
        self.game.sound.stop_music()
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
            self.search_sounds()
            self.search()

    def white_replay_step_up(self, number):
        self.game.sound.stop_music()
        if number >= 1:
            self.game.white_replay_counter.step()
            number -= 1
            self.replay_step_up()
            if self.game.replays == 899:
                number = 0
            self.delay(name="white_replay_step_up", delay=0.25, handler=self.white_replay_step_up, param=number)
        else:
            self.game.search_index.disengage()
            self.cancel_delayed(name="white_replay_step_up")
            self.search_sounds()
            self.search()

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
            self.q10 = 15
        elif self.game.line2.position == 1:
            self.q1 = 15
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
            self.q9 = 15
            self.q10 = 2

        if self.game.line3.position == 0 or self.game.line3.position == 2:
            self.r1 = 9
            self.r2 = 23
            self.r3 = 17
            self.r4 = 12
            self.r5 = 3

            self.r6 = 7
            self.r7 = 18
            self.r8 = 16
            self.r9 = 17
            self.r10 = 25
        elif self.game.line3.position == 1:
            self.r1 = 25
            self.r2 = 9
            self.r3 = 23
            self.r4 = 17
            self.r5 = 12

            self.r6 = 3
            self.r7 = 7
            self.r8 = 18
            self.r9 = 16
            self.r10 = 17
        elif self.game.line3.position == 3:
            self.r1 = 23
            self.r2 = 17
            self.r3 = 12
            self.r4 = 3
            self.r5 = 7

            self.r6 = 18
            self.r7 = 16
            self.r8 = 17
            self.r9 = 25
            self.r10 = 9

        if self.game.line4.position == 0 or self.game.line4.position == 2:
            self.s1 = 16
            self.s2 = 22
            self.s3 = 18
            self.s4 = 21
            self.s5 = 15
            
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

            self.s6 = 15
            self.s7 = 1
            self.s8 = 20
            self.s9 = 12
            self.s10 = 21
        elif self.game.line4.position == 3:
            self.s1 = 22
            self.s2 = 18
            self.s3 = 21
            self.s4 = 15
            self.s5 = 1

            self.s6 = 20
            self.s7 = 12
            self.s8 = 21
            self.s9 = 3
            self.s10 = 16

        if self.game.line5.position == 0 or self.game.line5.position == 2:
            self.t1 = 7
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
            self.t2 = 7
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
            self.t10 = 7

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
        color = None

        if rivets in range(0,15):
            card = 1
        else:
            card = 2

        if rivets in range(0, 8):
            color = "yellow"
        if rivets in range(9, 17):
            color = "red"
            if rivets == 15:
                corners = True
        if rivets in range(18, 25):
            color = "white"
        if rivets in range(26, 50):
            color = "green"

        return (self.pos[rivets], card, corners, color, rivets)
    
    def scan_all(self):
        #Animate scanning of everything - this happens through the spotting disc
        self.all_probability()

    def all_probability(self):
        initial = False
        if self.game.red_odds.position < 3:
            self.game.red_odds.step()
            self.game.coils.sounder.pulse()
            initial = True
        if self.game.white_odds.position < 3:
            self.game.white_odds.step()
            self.game.coils.sounder.pulse()
            initial = True
        if self.game.green_odds.position < 3:
            self.game.green_odds.step()
            self.game.coils.sounder.pulse()
            initial = True
        if self.game.yellow_odds.position < 3:
            self.game.yellow_odds.step()
            self.game.coils.sounder.pulse()
            initial = True
        mix1 = self.game.mixer1.connected_rivet()
        if self.game.reflex.connected_rivet() == 0 and (mix1 in [1,9,15]):
            if initial != True:
                self.scan_odds()
            self.scan_features()
        elif self.game.reflex.connected_rivet() == 1 and (mix1 in [2,14,24,1,9,15]):
            if initial != True:
                self.scan_odds()
            self.scan_features()
        elif self.game.reflex.connected_rivet() == 2 and (mix1 in [6,13,22,2,14,24,1,9,15]):
            if initial != True:
                self.scan_odds()
            self.scan_features()
        elif self.game.reflex.connected_rivet() == 3:
            if initial != True:
                self.scan_odds()
            self.scan_features()
        elif self.game.reflex.connected_rivet() == 4:
            if initial != True:
                self.scan_odds()
            self.scan_features()

    def scan_odds(self):
        if self.game.red_odds.position < 3:
            return
        if self.game.green_odds.position < 3:
            return
        if self.game.yellow_odds.position < 3:
            return
        if self.game.white_odds.position < 3:
            return
        p = self.odds_probability()
        if "red" in p:
            m = self.check_mixer3("red")
            if m == 1:
                es = self.check_extra_step()
                if self.game.red_odds.position < 7:
                    if es == 1:
                        i = random.randint(1,3)
                        self.red_extra_step(i)
                    else:
                        self.game.red_odds.step()
                        self.game.coils.sounder.pulse()
        if "green" in p:
            m = self.check_mixer3("green")
            if m == 1:
                es = self.check_extra_step()
                if self.game.green_odds.position < 7:
                    if es == 1:
                        i = random.randint(1,3)
                        self.green_extra_step(i)
                    else:
                        self.game.green_odds.step()
                        self.game.coils.sounder.pulse()
        if "yellow" in p:
            m = self.check_mixer3("yellow")
            if m == 1:
                es = self.check_extra_step()
                if self.game.yellow_odds.position < 7:
                    if es == 1:
                        i = random.randint(1,3)
                        self.yellow_extra_step(i)
                    else:
                        self.game.yellow_odds.step()
                        self.game.coils.sounder.pulse()
        if "white" in p:
            m = self.check_mixer3("white")
            if m == 1:
                es = self.check_extra_step()
                if self.game.white_odds.position < 7:
                    if es == 1:
                        i = random.randint(1,3)
                        self.white_extra_step(i)
                    else:
                        self.game.white_odds.step()
                        self.game.coils.sounder.pulse()

    def check_mixer3(self, color):
        m3 = self.game.mixer3.position
        if color == "yellow":
            if m3 in [2,5,11,14,17,23]:
                return 1
        if color == "red":
            if m3 in [6,8,12,1,18,24]:
                return 1
        if color == "white":
            if m3 in [1,13,9,22]:
                return 1
        if color == "green":
            if m3 in [3,15,4,16,7,20,10,22]:
                return 1

    def red_extra_step(self, number):
        if number > 0:
            self.game.red_odds.step()
            self.game.coils.sounder.pulse()
            self.delay(name="display", delay=0, handler=graphics.miss_america.display, param=self)
            number -= 1
            self.delay(name="red_extra_step", delay=0.1, handler=self.red_extra_step, param=number)
            
    def green_extra_step(self, number):
        if number > 0:
            self.game.green_odds.step()
            self.game.coils.sounder.pulse()
            self.delay(name="display", delay=0, handler=graphics.miss_america.display, param=self)
            number -= 1
            self.delay(name="green_extra_step", delay=0.1, handler=self.green_extra_step, param=number)

    def yellow_extra_step(self, number):
        if number > 0:
            self.game.yellow_odds.step()
            self.game.coils.sounder.pulse()
            self.delay(name="display", delay=0, handler=graphics.miss_america.display, param=self)
            number -= 1
            self.delay(name="yellow_extra_step", delay=0.1, handler=self.yellow_extra_step, param=number)

    def white_extra_step(self, number):
        if number > 0:
            self.game.white_odds.step()
            self.game.coils.sounder.pulse()
            self.delay(name="display", delay=0, handler=graphics.miss_america.display, param=self)
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
                if sd not in [0,4,10,11,15,16,20,45,46,49] and sd not in range(22,28) and sd not in range (30,33) and sd not in range(38,41):
                    return ["red", "yellow", "white"]
            if self.game.green_odds.position == 5:
                if sd not in [0,4,10,11,15,16,20,45,46,49] and sd not in range(22,28) and sd not in range (30,33) and sd not in range(38,41):
                    return ["green"]
            if self.game.red_odds.position == 5 or self.game.yellow_odds.position == 5 or self.game.white_odds.position == 5:
                if sd in [2,10,11,12,17,18,19,23,26,27,28,31,32,38,39,43,44]:
                    return ["red", "yellow", "white"]
            if self.game.green_odds.position == 4:
                if sd in [2,10,11,12,17,18,19,23,26,27,28,31,32,38,39,43,44]:
                    return ["green"]
            if self.game.red_odds.position == 6 or self.game.yellow_odds.position == 6 or self.game.white_odds.position == 6:
                if sd in [2,7,14,18,43,44]:
                    return ["red", "yellow", "white"]
            if self.game.green_odds.position == 3:
                if sd in [2,7,14,18,43,44]:
                    return ["green"]
            return [0]

    def scan_features(self):
        p = self.features_probability()

    def features_probability(self):
        sd = self.game.spotting.position

        if self.game.selection_feature.position == 0:
            self.game.selection_feature.step()
            self.game.coils.sounder.pulse()
        else:
            if sd in [2,5,8,13,21,22,25,35,37,42]:
                self.step_selection(6 - self.game.selection_feature.position)
            elif sd in [7,20,24]:
                if self.game.selection_feature.position >= 6:
                    if self.game.cu or self.game.corners.status == False:
                        self.step_selection(9 - self.game.selection_feature.position)
            elif sd == 0 or (sd == 23 and self.game.reflex.connected_rivet() == 4):
                self.step_selection(9 - self.game.selection_feature.position)
            else:
                m4 = self.check_mixer4()
                if m4 == 1:
                    self.game.selection_feature.step()
                    self.game.coils.sounder.pulse()
        
        if sd in [1,6,15,29,40,41,46,47,49]:
            self.game.selector.step()
        if sd in [11,12,18,19]:
            if self.game.before_fifth.status == False:
                if self.game.rollovers.status == False:
                    if self.game.cu:
                        self.game.coils.redROLamp.enable()
                    else:
                        self.game.coils.yellowROLamp.enable()
                if self.game.rollovers.status == False:
                    self.game.rollovers.engage(self.game)
                    self.game.sound.play('tilt')
        if sd == 12:
            if self.game.selection_feature.position < 9 or self.game.cu:
                if self.game.corners.status == False:
                    self.game.corners.engage(self.game)
                    self.game.sound.play('tilt')
        if sd == 8:
            if self.game.rollovers.status == False:
                if self.game.before_fifth.status == False:
                    self.game.before_fourth.disengage()
                    self.game.before_fifth.engage(self.game)
                    self.game.sound.play('tilt')

    def check_mixer4(self):
        mix4 = self.game.mixer4.position

        if mix4 in [12,22,20,10,4]:
            return 1
        else:
            return 0

    def check_mixer2(self):
        mix2 = self.game.mixer2.position
        odds = self.game.odds.position
        if odds < 4:
            if mix2 not in [15,19,23,7,9]:
                return 1
            else:
                return 0
        elif odds == 4:
            if mix2 not in [19,23,7,9]:
                return 1
            else:
                return 0
        elif odds == 5:
            if mix2 not in [23,7,9,15]:
                return 1
            else:
                return 0
        elif odds == 6:
            if mix2 not in [7,9,19,15]:
                return 1
            else:
                return 0
        elif odds in [7,8]:
            if mix2 not in [9,19,15,23]:
                return 1
            else:
                return 0
    
    def step_selection(self, number):
        if number >= 1:
            self.game.selection_feature.step()
            self.game.coils.sounder.pulse()
            number -= 1
            self.delay(name="display", delay=0.1, handler=graphics.miss_america.display, param=self)
            self.delay(name="step_selection", delay=0.1, handler=self.step_selection, param=number)

   
    def scan_eb(self):
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
        self.delay(name="display", delay=0.1, handler=graphics.miss_america.display, param=self)

    def animate_both(self, args):
        start = args[0]
        diff = args[1]
        num = args[2]
        if start + num >= 50:
            start = 0
        if diff >= 0:
            num = num + 1
            graphics.miss_america.both_animation([self, start + num])
            self.cancel_delayed(name="display")
            diff = diff - 1
            args = [start,diff,num]
            self.delay(name="both_animation", delay=0.08, handler=self.animate_both, param=args)
        else:
            self.cancel_delayed(name="both_animation")
            self.delay(name="display", delay=0.1, handler=graphics.miss_america.display, param=self)
            self.scan_all()

    def animate_line(self, args):
        self.game = args[0]
        num = args[1]
        line = args[2]
        if num < 45:
            graphics.miss_america.line_animation([self, num * -1, line])
            self.cancel_delayed(name="display")
            num = num + 1
            args = [self.game,num,line]
            self.delay(name="line_animation", delay=0.007, handler=self.animate_line, param=args)
        else:
            self.cancel_delayed(name="line_animation")
            self.delay(name="display", delay=0.1, handler=graphics.miss_america.display, param=self)


    def animate_eb_scan(self, args):
        start = args[0]
        diff = args[1]
        num = args[2]
        if start + num >= 50:
            start = 0
        if diff >= 0:
            num = num + 1
            graphics.miss_america.eb_animation([self, start + num])
            self.cancel_delayed(name="display")
            diff = diff - 1
            args = [start,diff,num]
            self.delay(name="eb_animation", delay=0.08, handler=self.animate_eb_scan, param=args)
        else:
            self.cancel_delayed(name="eb_animation")
            self.delay(name="display", delay=0.1, handler=graphics.miss_america.display, param=self)
            self.scan_eb()


    def eb_probability(self):
        mix1 = self.game.mixer1.connected_rivet()
        if self.game.reflex.connected_rivet() == 0 and (mix1 in [1,9,15]):
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
        else:
            if self.game.cu:
                self.step_eb(1)

    def step_eb(self, number):
        if number >= 1:
            self.game.extra_ball.step()
            self.check_lifter_status()
            number -= 1
            self.delay(name="display", delay=0.1, handler=graphics.miss_america.display, param=self)
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

class MissAmerica(procgame.game.BasicGame):
    """ The first of the Miss America series - wildly popular """
    def __init__(self, machine_type):
        super(MissAmerica, self).__init__(machine_type)
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

        self.selector = units.Stepper("selector", 2)

        # Select-a-spot setup
        self.selection_feature = units.Stepper("selection_feature", 9)
        self.line1 = units.Stepper("line1", 3, "miss_america", "continuous")
        self.line2 = units.Stepper("line2", 3, "miss_america", "continuous")
        self.line3 = units.Stepper("line3", 3, "miss_america", "continuous")
        self.line4 = units.Stepper("line4", 3, "miss_america", "continuous")
        self.line5 = units.Stepper("line5", 3, "miss_america", "continuous")

        self.rollover = units.Relay("rollover")

        self.replays = 0
        self.returned = False

    def reset(self):
        super(MissAmerica, self).reset()
        self.logger = logging.getLogger('game')
        self.load_config('bingo.yaml')
        
        main_mode = SinglecardBingo(self)
        self.modes.add(main_mode)
        
game = MissAmerica(machine_type='pdb')
game.reset()
game.run_loop()
