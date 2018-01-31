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
from bingo_emulator.graphics.acapulco import *

class SinglecardBingo(procgame.game.Mode):
    def __init__(self, game):
        super(SinglecardBingo, self).__init__(game=game, priority=5)
        self.holes = []
        self.startup()
        self.game.sound.register_music('motor', "audio/other_motor.wav")
        self.game.sound.register_sound('search', "audio/six_card_search_old.wav")
        self.game.sound.register_sound('add', "audio/six_card_add_card.wav")
        self.game.sound.register_sound('tilt', "audio/tilt.wav")
        self.game.sound.register_sound('step', "audio/step.wav")
        self.game.sound.register_sound('eb_search', "audio/EB_Search.wav")

    def sw_coin_active(self, sw):
        if self.game.start.status == True:
            if self.game.all_advantages.status == True:
                self.cancel_delayed(name="blink")
                self.game.sound.stop('add')
                self.game.sound.play('add')
                self.game.cu = not self.game.cu
                self.regular_play()
                self.game.odds_only.disengage()
                self.game.eb_play.disengage()
                self.game.features.disengage()
                self.scan_all()
            elif self.game.features.status == True:
                self.cancel_delayed(name="blink")
                self.game.sound.stop('add')
                self.game.sound.play('add')
                self.game.cu = not self.game.cu
                self.regular_play()
                self.game.odds_only.disengage()
                self.game.eb_play.disengage()
                self.game.all_advantages.disengage()
                self.scan_features()
            elif self.game.odds_only.status == True:
                self.cancel_delayed(name="blink")
                self.game.sound.stop('add')
                self.game.sound.play('add')
                self.game.cu = not self.game.cu
                self.regular_play()
                self.game.eb_play.disengage()
                self.game.features.disengage()
                self.game.all_advantages.disengage()
                self.scan_odds()
        elif self.game.eb_play.status == True:
            self.game.sound.stop('add')
            self.game.sound.play('add')
            begin = self.game.spotting.position
            self.game.features.disengage()
            self.game.all_advantages.disengage()
            self.game.odds_only.disengage()
            self.game.cu = not self.game.cu
            self.game.spotting.spin()
            self.animate_eb_scan([begin,self.game.spotting.movement_amount,1])
            self.game.mixer1.spin()
            self.game.mixer2.spin()
            self.game.mixer3.spin()
            self.game.mixer4.spin()
            self.scan_eb()
        else:
            self.cancel_delayed(name="blink")
            self.game.sound.stop('add')
            self.game.sound.play('add')
            self.game.cu = not self.game.cu
            self.game.all_advantages.engage(self.game)
            self.regular_play()
            self.game.odds_only.disengage()
            self.game.eb_play.disengage()
            self.game.features.disengage()
            self.scan_all()
        self.cancel_delayed(name="display")
        self.delay(name="display", delay=0.1, handler=graphics.acapulco.display, param=self)

    def sw_startButton_active(self, sw):
        self.cancel_delayed(name="both_animation")
        self.cancel_delayed(name="odds_animation")
        self.cancel_delayed(name="feature_animation")
        self.cancel_delayed(name="blink")
        self.game.eb_play.disengage()
        self.game.odds_only.disengage()
        self.game.features.disengage()
        self.game.all_advantages.engage(self.game)
        if self.game.replays > 0 or self.game.switches.freeplay.is_active():
            self.game.sound.stop('add')
            self.game.sound.play('add')
            self.game.cu = not self.game.cu
            self.game.spotting.spin()
            self.game.mixer1.spin()
            self.game.mixer2.spin()
            self.game.mixer3.spin()
            self.game.mixer4.spin()
            self.game.tilt.disengage()
            self.regular_play()
            self.scan_all()
        self.cancel_delayed(name="display")
        self.delay(name="display", delay=0.1, handler=graphics.acapulco.display, param=self)

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
            #if self.game.start.status == False:
            #    self.delay(name="startup", delay=0.1, handler=self.sw_startButton_active, param=sw)
            #else:
            #Adding this to handle moving numbers during gameplay
            if self.game.start.status == True:
                self.game.sound.stop('add')
                self.game.sound.play('add')
                self.game.odds_only.engage(self.game)
                self.cancel_delayed(name="display")
                self.cancel_delayed(name="both_animation")
                self.delay(name="display", delay=0.1, handler=graphics.acapulco.display, param=self)
                self.regular_play()
                self.scan_odds()
                self.cancel_delayed(name="display")
                self.delay(name="display", delay=0.1, handler=graphics.acapulco.display, param=self)
        if self.game.switches.drawer.is_inactive():
            if self.game.ball_count.position > 0:
                max_ball = 0
                if self.game.before_fourth.status == True:
                    max_ball = 4
                elif self.game.before_fifth.status == True:
                    max_ball = 5
                else:
                    if self.game.after_fifth.status == True:
                        max_ball = 6
                if self.game.ball_count.position < max_ball:
                    self.game.numberc.step()
            self.cancel_delayed(name="display")
            self.delay(name="display", delay=0.1, handler=graphics.acapulco.display, param=self)

    def sw_letterc_active(self, sw):
        if self.game.switches.drawer.is_active():
            if self.game.ball_count.position > 0:
                max_ball = 0
                if self.game.before_fourth.status == True:
                    max_ball = 4
                elif self.game.before_fifth.status == True:
                    max_ball = 5
                else:
                    if self.game.after_fifth.status == True:
                        max_ball = 6
                if self.game.ball_count.position < max_ball:
                    self.game.numberc.step()
            self.cancel_delayed(name="display")
            self.delay(name="display", delay=0.1, handler=graphics.acapulco.display, param=self)

    def sw_orange_active(self, sw):
        self.cancel_delayed(name="both_animation")
        self.cancel_delayed(name="odds_animation")
        self.cancel_delayed(name="feature_animation")
        if self.game.switches.drawer.is_active():
            if self.game.start.status == True:
                self.game.features.engage(self.game)
                self.game.all_advantages.disengage()
                self.game.odds_only.disengage()
                self.game.eb_play.disengage()

            if self.game.replays > 0 or self.game.switches.freeplay.is_active():
                #if self.game.start.status == False:
                #    self.delay(name="startup", delay=0.1, handler=self.sw_startButton_active, param=sw)
                #else:
                if self.game.start.status == True:
                    self.game.sound.stop('add')
                    self.game.sound.play('add')
                    self.game.features.engage(self.game)
                    self.cancel_delayed(name="display")
                    self.delay(name="display", delay=0.1, handler=graphics.acapulco.display, param=self)
                    self.regular_play()
                    self.scan_features()
                    self.cancel_delayed(name="display")
                    self.delay(name="display", delay=0.1, handler=graphics.acapulco.display, param=self)


    def sw_green_active(self, sw):
        self.cancel_delayed(name="both_animation")
        self.cancel_delayed(name="odds_animation")
        self.cancel_delayed(name="feature_animation")
        if self.game.switches.drawer.is_inactive():
            if self.game.start.status == True:
                self.game.features.engage(self.game)
                self.game.all_advantages.disengage()
                self.game.odds_only.disengage()
                self.game.eb_play.disengage()

            if self.game.replays > 0 or self.game.switches.freeplay.is_active():
                #if self.game.start.status == False:
                #    self.delay(name="startup", delay=0.1, handler=self.sw_startButton_active, param=sw)
                #else:
                if self.game.start.status == True:
                    self.game.sound.stop('add')
                    self.game.sound.play('add')
                    self.game.features.engage(self.game)
                    self.cancel_delayed(name="display")
                    self.delay(name="display", delay=0.1, handler=graphics.acapulco.display, param=self)
                    self.regular_play()
                    self.scan_features()
                    self.cancel_delayed(name="display")
                    self.delay(name="display", delay=0.1, handler=graphics.acapulco.display, param=self)
        if self.game.switches.drawer.is_inactive():
            if self.game.ball_count.position >= 1:
                max_ball = 0
                if self.game.before_fourth.status == True:
                    max_ball = 4
                elif self.game.before_fifth.status == True:
                    max_ball = 5
                else:
                    if self.game.after_fifth.status == True:
                        max_ball = 6
                if self.game.ball_count.position < max_ball:
                    self.game.numberd.step()

            self.cancel_delayed(name="display")
            self.delay(name="display", delay=0.1, handler=graphics.acapulco.display, param=self)

    def sw_letterd_active(self, sw):
        if self.game.switches.drawer.is_active():
            if self.game.ball_count.position >= 1:
                max_ball = 0
                if self.game.before_fourth.status == True:
                    max_ball = 4
                elif self.game.before_fifth.status == True:
                    max_ball = 5
                else:
                    if self.game.after_fifth.status == True:
                        max_ball = 6
                if self.game.ball_count.position < max_ball:
                    self.game.numberd.step()

            self.cancel_delayed(name="display")
            self.delay(name="display", delay=0.1, handler=graphics.acapulco.display, param=self)

    def sw_enter_active(self, sw):
        if self.game.switches.left.is_active() and self.game.switches.right.is_active():
            self.game.end_run_loop()
            os.system("/home/nbaldridge/proc/bingo_emulator/start_game.sh acapulco")
        else:
            if self.game.ball_count.position >= 4:
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
                if self.game.before_fourth.status == True:
                    max_ball = 4
                elif self.game.before_fifth.status == True:
                    max_ball = 5
                else:
                    if self.game.after_fifth.status == True:
                        max_ball = 6
                if self.game.ball_count.position < max_ball:
                    self.game.numberb.step()
                self.cancel_delayed(name="display")
                self.delay(name="display", delay=0.1, handler=graphics.acapulco.display, param=self)

    def sw_letterb_active(self, sw):
        if self.game.switches.drawer.is_active():
            if self.game.ball_count.position > 0:
                max_ball = 0
                if self.game.before_fourth.status == True:
                    max_ball = 4
                elif self.game.before_fifth.status == True:
                    max_ball = 5
                else:
                    if self.game.after_fifth.status == True:
                        max_ball = 6
                if self.game.ball_count.position < max_ball:
                    self.game.numberb.step()
                self.cancel_delayed(name="display")
                self.delay(name="display", delay=0.1, handler=graphics.acapulco.display, param=self)

    def sw_left_active(self, sw):
        if self.game.switches.drawer.is_inactive():
            if self.game.ball_count.position > 0:
                max_ball = 0
                if self.game.before_fourth.status == True:
                    max_ball = 4
                elif self.game.before_fifth.status == True:
                    max_ball = 5
                else:
                    if self.game.after_fifth.status == True:
                        max_ball = 6
                if self.game.ball_count.position < max_ball:
                    self.game.numbera.step()
                self.cancel_delayed(name="display")
                self.delay(name="display", delay=0.1, handler=graphics.acapulco.display, param=self)

    def sw_lettera_active(self, sw):
        if self.game.switches.drawer.is_active():
            if self.game.ball_count.position > 0:
                max_ball = 0
                if self.game.before_fourth.status == True:
                    max_ball = 4
                elif self.game.before_fifth.status == True:
                    max_ball = 5
                else:
                    if self.game.after_fifth.status == True:
                        max_ball = 6
                if self.game.ball_count.position < max_ball:
                    self.game.numbera.step()
                self.cancel_delayed(name="display")
                self.delay(name="display", delay=0.1, handler=graphics.acapulco.display, param=self)

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
        self.cancel_delayed(name="both_animation")
        self.cancel_delayed(name="odds_animation")
        self.cancel_delayed(name="feature_animation")
        self.cancel_delayed(name="search")
        self.cancel_delayed(name="red_replay_step_up")
        self.cancel_delayed(name="yellow_replay_step_up")
        self.cancel_delayed(name="green_replay_step_up")
        self.cancel_delayed(name="timeout")
        self.cancel_delayed(name="blink")
        self.game.search_index.disengage()
        self.game.coils.counter.pulse()

        self.game.cu = not self.game.cu
        self.game.mixer1.spin()
        self.game.mixer2.spin()
        self.game.mixer3.spin()
        self.game.mixer4.spin()
        self.game.reflex.decrease()
        begin = self.game.spotting.position
        self.game.spotting.spin()
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
            self.check_lifter_status()
        else:
            self.holes = []
            self.game.start.engage(self.game)
            self.game.coils.redROLamp.disable()
            self.game.coils.yellowROLamp.disable()
            self.game.red_replay_counter.reset()
            self.game.yellow_replay_counter.reset()
            self.game.green_replay_counter.reset()
            self.game.red_odds.reset()
            self.game.yellow_odds.reset()
            self.game.green_odds.reset()
            self.game.yellow_star.disengage()
            self.game.red_star.disengage()
            self.game.start.engage(self.game)
            self.game.selector.reset()
            self.game.ball_count.reset()
            self.game.extra_ball.reset()
            self.game.four_stars.disengage()
            self.game.magic_numbers_feature.reset()
            self.game.timer.reset()
            self.game.super_line_feature.disengage()
            self.game.hole_feature.disengage()
            self.game.selection_feature.reset()
            if self.game.numbera.position > 0:
                self.numbera_reset(self.game.numbera.position)
            if self.game.numberb.position > 0:
                self.numberb_reset(self.game.numberb.position)
            if self.game.numberc.position > 0:
                self.numberc_reset(self.game.numberc.position)
            if self.game.numberd.position > 0:
                self.numberd_reset(self.game.numberd.position)
            self.game.before_fifth.disengage()
            self.game.after_fifth.disengage()
            self.game.before_fourth.engage(self.game)
            self.game.sound.play_music('motor', -1)
            self.regular_play()
        self.cancel_delayed(name="display")
        self.delay(name="display", delay=0.1, handler=graphics.acapulco.display, param=self)
        self.game.tilt.disengage()

    def numbera_reset(self, number):
        if number > 0:
            self.game.numbera.step()
            self.delay(name="display", delay=0, handler=graphics.acapulco.display, param=self)
            number -= 1
            self.delay(name="numbera_reset", delay=0.1, handler=self.numbera_reset, param=number)
    
    def numberb_reset(self, number):
        if number > 0:
            self.game.numberb.step()
            self.delay(name="display", delay=0, handler=graphics.acapulco.display, param=self)
            number -= 1
            self.delay(name="numberb_reset", delay=0.1, handler=self.numberb_reset, param=number)
            
    def numberc_reset(self, number):
        if number > 0:
            self.game.numberc.step()
            self.delay(name="display", delay=0, handler=graphics.acapulco.display, param=self)
            number -= 1
            self.delay(name="numberc_reset", delay=0.1, handler=self.numberc_reset, param=number)
            
    def numberd_reset(self, number):
        if number > 0:
            self.game.numberd.step()
            self.delay(name="display", delay=0, handler=graphics.acapulco.display, param=self)
            number -= 1
            self.delay(name="numberd_reset", delay=0.1, handler=self.numberd_reset, param=number)

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
        if self.game.ball_count.position >= 5:
            self.game.coils.yellowROLamp.disable()
            self.game.coils.redROLamp.disable()
        if self.game.ball_count.position <= 7:
            self.check_lifter_status()
        self.cancel_delayed(name="display")
        self.delay(name="display", delay=0.1, handler=graphics.acapulco.display, param=self)


    # This is really nasty, but it is how we render graphics for each individual hole.
    # numbers are added (or removed from) a list.  In this way, I can re-use the same
    # routine even for games where there are ball return functions like Surf Club.

    def sw_hole1_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(1)
            self.delay(name="display", delay=0.1, handler=graphics.acapulco.display, param=self)

    def sw_hole2_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(2)
            self.delay(name="display", delay=0.1, handler=graphics.acapulco.display, param=self)

    def sw_hole3_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(3)
            self.delay(name="display", delay=0.1, handler=graphics.acapulco.display, param=self)

    def sw_hole4_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(4)
            self.delay(name="display", delay=0.1, handler=graphics.acapulco.display, param=self)

    def sw_hole5_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(5)
            self.delay(name="display", delay=0.1, handler=graphics.acapulco.display, param=self)

    def sw_hole6_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(6)
            self.delay(name="display", delay=0.1, handler=graphics.acapulco.display, param=self)

    def sw_hole7_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(7)
            self.delay(name="display", delay=0.1, handler=graphics.acapulco.display, param=self)

    def sw_hole8_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(8)
            self.delay(name="display", delay=0.1, handler=graphics.acapulco.display, param=self)

    def sw_hole9_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(9)
            self.delay(name="display", delay=0.1, handler=graphics.acapulco.display, param=self)

    def sw_hole10_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(10)
            self.delay(name="display", delay=0.1, handler=graphics.acapulco.display, param=self)

    def sw_hole11_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(11)
            self.delay(name="display", delay=0.1, handler=graphics.acapulco.display, param=self)

    def sw_hole12_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(12)
            self.delay(name="display", delay=0.1, handler=graphics.acapulco.display, param=self)

    def sw_hole13_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(13)
            self.delay(name="display", delay=0.1, handler=graphics.acapulco.display, param=self)

    def sw_hole14_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(14)
            self.delay(name="display", delay=0.1, handler=graphics.acapulco.display, param=self)

    def sw_hole15_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(15)
            self.delay(name="display", delay=0.1, handler=graphics.acapulco.display, param=self)

    def sw_hole16_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(16)
            if self.game.hole_feature.status == True:
                if self.game.ball_count.position <= 3:
                    self.red_extra_step(8)
            self.delay(name="display", delay=0.1, handler=graphics.acapulco.display, param=self)

    def sw_hole17_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(17)
            self.delay(name="display", delay=0.1, handler=graphics.acapulco.display, param=self)

    def sw_hole18_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(18)
            self.delay(name="display", delay=0.1, handler=graphics.acapulco.display, param=self)

    def sw_hole19_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(19)
            self.delay(name="display", delay=0.1, handler=graphics.acapulco.display, param=self)

    def sw_hole20_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(20)
            self.delay(name="display", delay=0.1, handler=graphics.acapulco.display, param=self)

    def sw_hole21_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(21)
            self.delay(name="display", delay=0.1, handler=graphics.acapulco.display, param=self)

    def sw_hole22_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(22)
            self.delay(name="display", delay=0.1, handler=graphics.acapulco.display, param=self)

    def sw_hole23_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(23)
            self.delay(name="display", delay=0.1, handler=graphics.acapulco.display, param=self)

    def sw_hole24_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(24)
            self.delay(name="display", delay=0.1, handler=graphics.acapulco.display, param=self)

    def sw_hole25_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(25)
            self.delay(name="display", delay=0.1, handler=graphics.acapulco.display, param=self)

    def sw_replayReset_active(self, sw):
        self.game.anti_cheat.disengage()
        self.holes = []
        graphics.acapulco.display(self)
        self.tilt_actions()
        self.replay_step_down(self.game.replays)

    def sw_redstar_active(self, sw):
        if self.game.red_star.status == True:
            self.game.before_fourth.disengage()
            self.game.before_fifth.disengage()
            self.game.after_fifth.engage(self.game)
            self.game.red_star.disengage()
            self.game.coils.yellowROLamp.disable()
        self.delay(name="display", delay=0.1, handler=graphics.acapulco.display, param=self)

    def sw_yellowstar_active(self, sw):
        if self.game.yellow_star.status == True:
            if self.game.before_fifth.status == False:
                self.game.before_fourth.disengage()
                self.game.before_fifth.engage(self.game)
                self.game.yellow_star.disengage()
                self.game.coils.redROLamp.disable()
        self.delay(name="display", delay=0.1, handler=graphics.acapulco.display, param=self)

    def tilt_actions(self):
        self.game.start.disengage()
        self.cancel_delayed(name="blink")
        self.cancel_delayed(name="replay_reset")
        self.cancel_delayed(name="red_replay_step_up")
        self.cancel_delayed(name="yellow_replay_step_up")
        self.cancel_delayed(name="green_replay_step_up")
        self.cancel_delayed(name="timeout")
        self.game.coils.redROLamp.disable()
        self.game.coils.yellowROLamp.disable()
        self.game.search_index.disengage()
        if self.game.ball_count.position == 0:
            if self.game.switches.shutter.is_active():
                self.game.coils.shutter.enable()
        self.holes = []
        self.game.selector.reset()
        self.game.red_replay_counter.reset()
        self.game.yellow_replay_counter.reset()
        self.game.green_replay_counter.reset()
        self.game.yellow_star.disengage()
        self.game.red_star.disengage()
        self.game.magic_numbers_feature.reset()
        self.game.four_stars.disengage()
        self.game.before_fourth.disengage()
        self.game.before_fifth.disengage()
        self.game.after_fifth.disengage()
        self.game.selection_feature.reset()
        self.game.ball_count.reset()
        self.game.red_odds.reset()
        self.game.yellow_odds.reset()
        self.game.green_odds.reset()
        self.game.eb_play.disengage()
        self.game.extra_ball.reset()
        self.game.super_line_feature.disengage()
        self.game.hole_feature.disengage()
        self.game.anti_cheat.engage(game)
        self.game.tilt.engage(self.game)
        self.game.sound.stop_music()
        self.game.sound.play('tilt')
        # displays "Tilt" on the backglass, you have to recoin.
        self.cancel_delayed(name="display")
        self.delay(name="display", delay=0.1, handler=graphics.acapulco.display, param=self)

    def sw_tilt_active(self, sw):
        if self.game.tilt.status == False:
            self.tilt_actions()

    def replay_step_down(self, number=0):
        if number > 0:
            if number > 1:
                self.game.replays -= 1
                graphics.replay_step_down(self.game.replays, graphics.acapulco.reel1, graphics.acapulco.reel10, graphics.acapulco.reel100)
                self.game.coils.registerDown.pulse()
                number -= 1
                self.delay(name="display", delay=0, handler=graphics.acapulco.display, param=self)
                self.delay(name="replay_reset", delay=0.13, handler=self.replay_step_down, param=number)
            elif number == 1:
                self.game.replays -= 1
                graphics.replay_step_down(self.game.replays, graphics.acapulco.reel1, graphics.acapulco.reel10, graphics.acapulco.reel100)
                self.game.coils.registerDown.pulse()
                number -= 1
                self.delay(name="display", delay=0, handler=graphics.acapulco.display, param=self)
                self.cancel_delayed(name="replay_reset")
        else: 
            if self.game.replays > 0:
                self.game.replays -= 1
                graphics.replay_step_down(self.game.replays, graphics.acapulco.reel1, graphics.acapulco.reel10, graphics.acapulco.reel100)
                self.delay(name="display", delay=0.1, handler=graphics.acapulco.display, param=self)
            self.game.coils.registerDown.pulse()

    def replay_step_up(self):
        if self.game.replays < 8999:
            self.game.replays += 1
            graphics.replay_step_up(self.game.replays, graphics.acapulco.reel1, graphics.acapulco.reel10, graphics.acapulco.reel100, graphics.acapulco.reel1000)
        self.game.coils.registerUp.pulse()
        self.game.reflex.increase()
        graphics.acapulco.display(self)

    def sw_lettere_active(self, sw):
        if self.game.switches.drawer.is_active():
            if self.game.ball_count.position >= 1:
                max_ball = 4
                if self.game.ball_count.position < max_ball:
                    if self.game.super_line_feature.status == True:
                        self.game.super_line_select.step()
            self.cancel_delayed(name="display")
            self.delay(name="display", delay=0.1, handler=graphics.acapulco.display, param=self)

    def sw_yellow_active(self, sw):
        if self.game.switches.drawer.is_inactive():
            if self.game.ball_count.position < 4:
                if self.game.super_line_feature.status == True:
                    self.game.super_line_select.step()
                    self.delay(name="display", delay=0.1, handler=graphics.acapulco.display, param=self)
        if self.game.ball_count.position >= 4:
            if self.game.eb_play.status == False:
                self.game.spotting.spin()
                self.game.mixer1.spin()
                self.game.mixer2.spin()
                self.game.mixer3.spin()
                self.game.mixer4.spin()
                self.game.eb_play.engage(self.game)
                self.delay(name="display", delay=0.1, handler=graphics.acapulco.display, param=self)
                self.sw_yellow_active(sw)
            if self.game.eb_play.status == True and (self.game.replays > 0 or self.game.switches.freeplay.is_active()):
                self.game.sound.stop('add')
                self.game.sound.play('add')
                self.game.cu = not self.game.cu
                begin = self.game.spotting.position
                self.game.spotting.spin()
                self.animate_eb_scan([begin,self.game.spotting.movement_amount,1])
                self.game.mixer1.spin()
                self.game.mixer2.spin()
                self.game.mixer3.spin()
                self.game.mixer4.spin()
                self.scan_eb()
                self.replay_step_down()
                self.game.reflex.decrease()
                self.delay(name="display", delay=0.1, handler=graphics.acapulco.display, param=self)
            
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
       
        for i in range(0, 50):
            self.r = self.closed_search_relays(self.game.searchdisc.position)
            self.game.searchdisc.spin()
            self.wipers = self.r[0]
            self.red = self.r[1]
            self.yellow = self.r[2]
            self.green = self.r[3]
            self.stars = self.r[4]
            self.horizontal1 = self.r[5]
            self.horizontal2 = self.r[6]
            self.horizontal3 = self.r[7]
            self.horizontal4 = self.r[8]
            self.horizontal5 = self.r[9]

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
                        if s >= 3:
                            self.find_winner(s, self.red, self.yellow, self.green, self.stars, self.horizontal1, self.horizontal2, self.horizontal3, self.horizontal4, self.horizontal5)
                            break
            

    def find_winner(self, relays, red, yellow, green, stars, horizontal1, horizontal2, horizontal3, horizontal4, horizontal5):
        if self.game.search_index.status == False and self.game.replays < 8999:
            if self.game.red_odds.position == 1:
                redthreeodds = 4
                redfourodds = 16
                redfiveodds = 80
                redsuper = 150
            elif self.game.red_odds.position == 2:
                redthreeodds = 6
                redfourodds = 20
                redfiveodds = 80
                redsuper = 150
            elif self.game.red_odds.position == 3:
                redthreeodds = 8
                redfourodds = 24
                redfiveodds = 100
                redsuper = 192
            elif self.game.red_odds.position == 4:
                redthreeodds = 16
                redfourodds = 48
                redfiveodds = 100
                redsuper = 192
            elif self.game.red_odds.position == 5:
                redthreeodds = 32
                redfourodds = 96
                redfiveodds = 200
                redsuper = 384
            elif self.game.red_odds.position == 6:
                redthreeodds = 64
                redfourodds = 160
                redfiveodds = 320
                redsuper = 600
            elif self.game.red_odds.position == 7:
                redthreeodds = 128
                redfourodds = 256
                redfiveodds = 480
                redsuper = 960
            elif self.game.red_odds.position == 8:
                redthreeodds = 192
                redfourodds = 480
                redfiveodds = 640
                redsuper = 1200
            if self.game.yellow_odds.position == 1:
                yellowthreeodds = 4
                yellowfourodds = 16
                yellowfiveodds = 80
                yellowsuper = 150
            elif self.game.yellow_odds.position == 2:
                yellowthreeodds = 6
                yellowfourodds = 20
                yellowfiveodds = 80
                yellowsuper = 150
            elif self.game.yellow_odds.position == 3:
                yellowthreeodds = 8
                yellowfourodds = 24
                yellowfiveodds = 100
                yellowsuper = 192
            elif self.game.yellow_odds.position == 4:
                yellowthreeodds = 16
                yellowfourodds = 48
                yellowfiveodds = 100
                yellowsuper = 192
            elif self.game.yellow_odds.position == 5:
                yellowthreeodds = 32
                yellowfourodds = 96
                yellowfiveodds = 200
                yellowsuper = 384
            elif self.game.yellow_odds.position == 6:
                yellowthreeodds = 64
                yellowfourodds = 160
                yellowfiveodds = 320
                yellowsuper = 600
            elif self.game.yellow_odds.position == 7:
                yellowthreeodds = 128
                yellowfourodds = 256
                yellowfiveodds = 480
                yellowsuper = 960
            elif self.game.yellow_odds.position == 8:
                yellowthreeodds = 192
                yellowfourodds = 480
                yellowfiveodds = 640
                yellowsuper = 1200
            if self.game.green_odds.position == 1:
                greenthreeodds = 4
                greenfourodds = 16
                greenfiveodds = 80
                greensuper = 150
            elif self.game.green_odds.position == 2:
                greenthreeodds = 6
                greenfourodds = 20
                greenfiveodds = 80
                greensuper = 150
            elif self.game.green_odds.position == 3:
                greenthreeodds = 8
                greenfourodds = 24
                greenfiveodds = 100
                greensuper = 192
            elif self.game.green_odds.position == 4:
                greenthreeodds = 16
                greenfourodds = 48
                greenfiveodds = 100
                greensuper = 192
            elif self.game.green_odds.position == 5:
                greenthreeodds = 32
                greenfourodds = 96
                greenfiveodds = 200
                greensuper = 384
            elif self.game.green_odds.position == 6:
                greenthreeodds = 64
                greenfourodds = 160
                greenfiveodds = 320
                greensuper = 600
            elif self.game.green_odds.position == 7:
                greenthreeodds = 128
                greenfourodds = 256
                greenfiveodds = 480
                greensuper = 960
            elif self.game.green_odds.position == 8:
                greenthreeodds = 192
                greenfourodds = 480
                greenfiveodds = 640
                greensuper = 1200

            if relays == 3:
                if not stars:
                    if red:
                        if (self.game.super_line_select.position == 0 and horizontal1 == True) or (self.game.super_line_select.position == 3 and horizontal4 == True):
                            if self.game.red_replay_counter.position < redfourodds:
                                self.game.search_index.engage(self.game)
                                self.red_replay_step_up(redfourodds - self.game.red_replay_counter.position)
                        else:
                            if self.game.red_replay_counter.position < redthreeodds:
                                self.game.search_index.engage(self.game)
                                self.red_replay_step_up(redthreeodds - self.game.red_replay_counter.position)
                    if yellow:
                        if (self.game.super_line_select.position == 1 and horizontal2 == True) or (self.game.super_line_select.position == 4 and horizontal5 == True):
                            if self.game.yellow_replay_counter.position < yellowfourodds:
                                self.game.search_index.engage(self.game)
                                self.yellow_replay_step_up(yellowfourodds - self.game.yellow_replay_counter.position)
                        else:
                            if self.game.yellow_replay_counter.position < yellowthreeodds:
                                self.game.search_index.engage(self.game)
                                self.yellow_replay_step_up(yellowthreeodds - self.game.yellow_replay_counter.position)
                    if green:
                        if (self.game.super_line_select.position == 2 and horizontal3 == True):
                            if self.game.green_replay_counter.position < greenfourodds:
                                self.game.search_index.engage(self.game)
                                self.green_replay_step_up(greenfourodds - self.game.green_replay_counter.position)
                        else:
                            if self.game.green_replay_counter.position < greenthreeodds:
                                self.game.search_index.engage(self.game)
                                self.green_replay_step_up(greenthreeodds - self.game.green_replay_counter.position)
            if relays == 4:
                if red:
                    if (self.game.super_line_select.position == 0 and horizontal1 == True) or (self.game.super_line_select.position == 3 and horizontal4 == True):
                        if self.game.red_replay_counter.position < redfiveodds:
                            self.game.search_index.engage(self.game)
                            self.red_replay_step_up(redfiveodds - self.game.red_replay_counter.position)
                    else:
                        if self.game.red_replay_counter.position < redfourodds:
                            self.game.search_index.engage(self.game)
                            self.red_replay_step_up(redfourodds - self.game.red_replay_counter.position)
                if yellow:
                    if (self.game.super_line_select.position == 1 and horizontal2 == True) or (self.game.super_line_select.position == 4 and horizontal5 == True):
                        if self.game.yellow_replay_counter.position < yellowfiveodds:
                            self.game.search_index.engage(self.game)
                            self.yellow_replay_step_up(yellowfiveodds - self.game.yellow_replay_counter.position)
                    else:
                        if self.game.yellow_replay_counter.position < yellowfourodds:
                            self.game.search_index.engage(self.game)
                            self.yellow_replay_step_up(yellowfourodds - self.game.yellow_replay_counter.position)
                if green:
                    if (self.game.super_line_select.position == 2 and horizontal3 == True):
                        if self.game.green_replay_counter.position < greenfiveodds:
                            self.game.search_index.engage(self.game)
                            self.green_replay_step_up(greenfiveodds - self.game.green_replay_counter.position)
                    else:
                        if self.game.green_replay_counter.position < greenfourodds:
                            self.game.search_index.engage(self.game)
                            self.green_replay_step_up(greenfourodds - self.game.green_replay_counter.position)
                if stars:
                    if self.game.stars_replay_counter.position < 600:
                        self.game.search_index.engage(self.game)
                        self.stars_replay_step_up(600 - self.game.stars_replay_counter.position)
            if relays == 5:
                if red:
                    if (self.game.super_line_select.position == 0 and horizontal1 == True) or (self.game.super_line_select.position == 3 and horizontal4 == True):
                        if self.game.red_replay_counter.position < redsuperodds:
                            self.game.search_index.engage(self.game)
                            self.red_replay_step_up(redsuperodds - self.game.red_replay_counter.position)
                    else:
                        if self.game.red_replay_counter.position < redfiveodds:
                            self.game.search_index.engage(self.game)
                            self.red_replay_step_up(redfiveodds - self.game.red_replay_counter.position)
                if yellow:
                    if (self.game.super_line_select.position == 1 and horizontal2 == True) or (self.game.super_line_select.position == 4 and horizontal5 == True):
                        if self.game.yellow_replay_counter.position < yellowsuperodds:
                            self.game.search_index.engage(self.game)
                            self.yellow_replay_step_up(yellowsuperodds - self.game.yellow_replay_counter.position)
                    else:
                        if self.game.yellow_replay_counter.position < yellowfiveodds:
                            self.game.search_index.engage(self.game)
                            self.yellow_replay_step_up(yellowfiveodds - self.game.yellow_replay_counter.position)
                if green:
                    if (self.game.super_line_select.position == 2 and horizontal3 == True):
                        if self.game.green_replay_counter.position < greensuperodds:
                            self.game.search_index.engage(self.game)
                            self.green_replay_step_up(greensuperodds - self.game.green_replay_counter.position)
                    else:
                        if self.game.green_replay_counter.position < greenfiveodds:
                            self.game.search_index.engage(self.game)
                            self.green_replay_step_up(greenfiveodds - self.game.green_replay_counter.position)

    def stars_replay_step_up(self, number):
        if number >= 1:
            self.game.stars_replay_counter.step()
            number -= 1
            self.replay_step_up()
            if self.game.replays == 8999:
                number = 0
            self.delay(name="stars_replay_step_up", delay=0.1, handler=self.stars_replay_step_up, param=number)
        else:
            self.game.search_index.disengage()
            self.cancel_delayed(name="stars_replay_step_up")
            self.search()

    def red_replay_step_up(self, number):
        if number >= 1:
            self.game.red_replay_counter.step()
            number -= 1
            self.replay_step_up()
            if self.game.replays == 8999:
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
            if self.game.replays == 8999:
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
            if self.game.replays == 8999:
                number = 0
            self.delay(name="green_replay_step_up", delay=0.1, handler=self.green_replay_step_up, param=number)
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
        stars = False
        horizontal1 = False
        horizontal2 = False
        horizontal3 = False
        horizontal4 = False
        horizontal5 = False

        if self.game.numbera.position == 0:
            self.p1 = 9
            self.p2 = 1
            self.q1 = 4
            self.q2 = 19
            self.r1 = 25
            self.r2 = 24
        elif self.game.numbera.position == 1:
            self.p1 = 4
            self.p2 = 9
            self.q1 = 25
            self.q2 = 1
            self.r1 = 24
            self.r2 = 19
        elif self.game.numbera.position == 2:
            self.p1 = 25
            self.p2 = 4
            self.q1 = 24
            self.q2 = 9
            self.r1 = 19
            self.r2 = 1
        elif self.game.numbera.position == 3:
            self.p1 = 24
            self.p2 = 25
            self.q1 = 19
            self.q2 = 4
            self.r1 = 1
            self.r2 = 9
        elif self.game.numbera.position == 4:
            self.p1 = 19
            self.p2 = 24
            self.q1 = 1
            self.q2 = 25
            self.r1 = 9
            self.r2 = 4
        elif self.game.numbera.position == 5:
            self.p1 = 1
            self.p2 = 19
            self.q1 = 9
            self.q2 = 24
            self.r1 = 4
            self.r2 = 25
        if self.game.numberb.position == 0:
            self.s1 = 6
            self.s2 = 23
            self.s3 = 5
            self.t1 = 12
            self.t2 = 8
            self.t3 = 14
        elif self.game.numberb.position == 1:
            self.s1 = 12
            self.s2 = 6
            self.s3 = 23
            self.t1 = 8
            self.t2 = 14
            self.t3 = 5
        elif self.game.numberb.position == 2:
            self.s1 = 8
            self.s2 = 12
            self.s3 = 6
            self.t1 = 14
            self.t2 = 5
            self.t3 = 23
        elif self.game.numberb.position == 3:
            self.s1 = 14
            self.s2 = 8
            self.s3 = 12
            self.t1 = 5
            self.t2 = 23
            self.t3 = 6
        elif self.game.numberb.position == 4:
            self.s1 = 5
            self.s2 = 14
            self.s3 = 8
            self.t1 = 23
            self.t2 = 6
            self.t3 = 12
        elif self.game.numberb.position == 5:
            self.s1 = 23
            self.s2 = 5
            self.s3 = 14
            self.t1 = 6
            self.t2 = 12
            self.t3 = 8
        if self.game.numberc.position == 0:
            self.r4 = 13
            self.r5 = 17
            self.s4 = 21
            self.s5 = 20
            self.t4 = 3
            self.t5 = 10
        elif self.game.numberc.position == 1:
            self.r4 = 21
            self.r5 = 13
            self.s4 = 3
            self.s5 = 17
            self.t4 = 10
            self.t5 = 20
        elif self.game.numberc.position == 2:
            self.r4 = 3
            self.r5 = 21
            self.s4 = 10
            self.s5 = 13
            self.t4 = 20
            self.t5 = 17
        elif self.game.numberc.position == 3:
            self.r4 = 10
            self.r5 = 3
            self.s4 = 20
            self.s5 = 21
            self.t4 = 17
            self.t5 = 13
        elif self.game.numberc.position == 4:
            self.r4 = 20
            self.r5 = 10
            self.s4 = 17
            self.s5 = 3
            self.t4 = 13
            self.t5 = 21
        elif self.game.numberc.position == 5:
            self.r4 = 17
            self.r5 = 20
            self.s4 = 13
            self.s5 = 10
            self.t4 = 21
            self.t5 = 3
        if self.game.numberd.position == 0:
            self.p3 = 2
            self.p4 = 11
            self.p5 = 15
            self.q3 = 7
            self.q4 = 22
            self.q5 = 18
        elif self.game.numberd.position == 1:
            self.p3 = 7
            self.p4 = 2
            self.p5 = 11
            self.q3 = 22
            self.q4 = 18
            self.q5 = 15
        elif self.game.numberd.position == 2:
            self.p3 = 22
            self.p4 = 7
            self.p5 = 2
            self.q3 = 18
            self.q4 = 15
            self.q5 = 11
        elif self.game.numberd.position == 3:
            self.p3 = 18
            self.p4 = 22
            self.p5 = 7
            self.q3 = 15
            self.q4 = 11
            self.q5 = 2
        elif self.game.numberd.position == 4:
            self.p3 = 15
            self.p4 = 18
            self.p5 = 22
            self.q3 = 11
            self.q4 = 2
            self.q5 = 7
        elif self.game.numberd.position == 5:
            self.p3 = 11
            self.p4 = 15
            self.p5 = 18
            self.q3 = 2
            self.q4 = 7
            self.q5 = 22

        self.pos[0] = {}
        self.pos[1] = {self.p1:1, self.p2:2, self.p3:3, self.p4:4, self.p5:5}
        self.pos[2] = {self.q1:1, self.q2:2, self.q3:3, self.q4:4, self.q5:5}
        self.pos[3] = {self.r1:1, self.r2:2, 16:3, self.r4:4, self.r5:5}
        self.pos[4] = {self.s1:1, self.s2:2, self.s3:3, self.s4:4, self.s5:5}
        self.pos[5] = {self.t1:1, self.t2:2, self.t3:3, self.t4:4, self.t5:5}
        self.pos[6] = {self.p1:1, self.q1:2, self.r1:3, self.s1:4, self.t1:5}
        self.pos[7] = {self.p2:1, self.q2:2, self.r2:3, self.s2:4, self.t2:5}
        self.pos[8] = {self.p3:1, self.q3:2, 16:3, self.s3:4, self.t3:5}
        self.pos[9] = {self.p4:1, self.q4:2, self.r4:3, self.s4:4, self.t4:5}
        self.pos[10] = {self.p5:1, self.q5:2, self.r5:3, self.s5:4, self.t5:5}
        self.pos[11] = {self.p1:1, self.q2:2, 16:3, self.s4:4, self.t5:5}
        self.pos[12] = {self.p5:1, self.q4:2, 16:3, self.s2:4, self.t1:5}
        self.pos[13] = {}
        self.pos[14] = {self.p4:1, self.p5:2, self.q4:3, self.q5:4}
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


        if rivets == 1 or rivets == 4 or rivets == 7 or rivets == 10:
            red = True
        elif rivets == 2 or rivets == 5 or rivets == 6 or rivets == 9:
            yellow = True
        elif rivets == 14:
            stars = True
        else:
            green = True

        if rivets == 1:
            horizontal1 = True
        if rivets == 2:
            horizontal2 = True
        if rivets == 3:
            horizontal3 = True
        if rivets == 4:
            horizontal4 = True
        if rivets == 5:
            horizontal5 = True
            
        return (self.pos[rivets], red, yellow, green, stars, horizontal1, horizontal2, horizontal3, horizontal4, horizontal5)

    
    def scan_all(self):
        #Animate scanning of everything - this happens through the spotting disc
        self.all_probability()

    def all_probability(self):
        mix1 = self.game.mixer1.connected_rivet()
        if self.game.reflex.connected_rivet() == 0:
            #Worst position for reflex - requires mixer1 to be in the three liberal positions for the connection of the wires bypassing the reflex.
            if (mix1 == 18 or mix1 == 12):
                self.scan_odds()
                if self.game.green_odds.position > 0:
                    self.scan_features()
        if self.game.reflex.connected_rivet() == 1 and (mix1 in [2,7,11,14,16,20,22,24,6,5,13,15]):
            self.scan_odds()
            if self.game.green_odds.position > 0:
                self.scan_features()
        elif self.game.reflex.connected_rivet() == 2 and (mix1 in [2,7,11,14,16,20,22,24,6,5,13,15,4,9,23]):
            self.scan_odds()
            if self.game.green_odds.position > 0:
                self.scan_features()
        elif self.game.reflex.connected_rivet() == 3 and (mix1 not in [18,12]):
            self.scan_odds()
            if self.game.green_odds.position > 0:
                self.scan_features()
        elif self.game.reflex.connected_rivet() == 4:
            self.scan_odds()
            if self.game.green_odds.position > 0:
                self.scan_features()
        else:
            if self.game.yellow_odds.position == 0:
                self.game.yellow_odds.step()
            if self.game.red_odds.position == 0:
                self.game.red_odds.step()
            if self.game.green_odds.position == 0:
                self.game.green_odds.step()
        graphics.acapulco.display(self)

    def eb_reflex(self):
        mix1 = self.game.mixer1.connected_rivet()
        if self.game.reflex.connected_rivet() == 0:
            #Worst position for reflex - requires mixer1 to be in the three liberal positions for the connection of the wires bypassing the reflex.
            if (mix1 == 18 or mix1 == 12):
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

    def check_mixer2(self, sel):
        mix2 = self.game.mixer2.position
        if mix2 in [19,9,4,2]:
            return 1
        if self.game.ok.status == False:
            if mix2 == 10:
                return 1
        if sel < 8:
            if mix2 == 21:
                return 1
        if sel < 7 or self.game.ok.status == False:
            if mix2 in [17,23]:
                return 1
        if sel < 6:
            if mix2 == 7:
                return 1
        if self.game.ok.status == False:
            if mix2 in [11,18,22,24,1,6]:
                return 1
        return 0

    def scan_odds(self):
        if self.game.yellow_odds.position <= 1:
            if self.game.odds_only.status == True:
                self.yellow_extra_step(2)
            else:
                self.game.yellow_odds.step()
        if self.game.red_odds.position <= 1:
            if self.game.odds_only.status == True:
                self.red_extra_step(2)
            else:
                self.game.red_odds.step()
        if self.game.green_odds.position <= 1:
            if self.game.odds_only.status == True:
                self.green_extra_step(2)
            else:
                self.game.green_odds.step()
        if self.game.yellow_odds.position >= 2 and self.game.red_odds.position >= 2 and self.game.green_odds.position >= 2:
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
                self.game.green_odds.step()
        if self.game.odds_only.status == True or self.game.all_advantages.status == True:
            self.check_blue_features()
        graphics.acapulco.display(self)

    def green_extra_step(self, number):
        if number > 0:
            self.game.green_odds.step()
            self.delay(name="display", delay=0.1, handler=graphics.acapulco.display, param=self)
            number -= 1
            self.delay(name="extra_step", delay=0.1, handler=self.green_extra_step, param=number)

    def red_extra_step(self, number):
        if number > 0:
            self.game.red_odds.step()
            self.delay(name="display", delay=0.1, handler=graphics.acapulco.display, param=self)
            number -= 1
            self.delay(name="extra_step", delay=0.1, handler=self.red_extra_step, param=number)

    def yellow_extra_step(self, number):
        if number > 0:
            self.game.yellow_odds.step()
            self.delay(name="display", delay=0.1, handler=graphics.acapulco.display, param=self)
            number -= 1
            self.delay(name="extra_step", delay=0.1, handler=self.yellow_extra_step, param=number)

    def check_extra_step(self):
        i = random.randint(0,32)
        if i == 16:
            return 1
        else:
            return 0

    def check_blue_features(self):
        sd = self.game.spotting.position
        if sd in [9,37,45,2,40,41,49]:
            self.game.super_line_feature.engage(self.game)

    def check_odds_spotting(self, color):
        spot = self.game.spotting.position
        if color == "yellow":
            if self.game.yellow_odds.position == 2 or self.game.yellow_odds.position == 3 or self.game.yellow_odds.position == 4:
                if spot in [2,4,6,7,8,9,10,11,12,15,16,20,21,22,29,33,34,39,40,44,49]:
                    return 1
            if self.game.yellow_odds.position == 5:
                if self.game.odds_only.status == True:
                    if spot in [2,6,7,8,11,12,17,20,22,24,25,29,33,37,38,39,40,43,44,45,47,48,49]:
                        return 1
                else:
                    if spot in [14,15,19,22,23,27,29,34,40,41]:
                        return 1
            if self.game.yellow_odds.position == 6 or self.game.yellow_odds.position == 7:
                #Wipers are mounted on opposite side.  Manual reads backwards.
                if self.game.odds_only.status == True:
                    if spot in [2,3,12,13,21,25,26,30,38,42]:
                        return 1
                else:
                    if spot in [2,10,11,17,35,40,46]:
                        return 1
            return 0
        if color == "red":
            if self.game.red_odds.position == 2 or self.game.red_odds.position == 3 or self.game.red_odds.position == 4:
                if spot in [2,4,6,7,8,9,10,11,12,15,16,20,21,22,29,33,34,39,40,44,49]:
                    return 1
            if self.game.red_odds.position == 5:
                if self.game.odds_only.status == True:
                    if spot in [2,6,7,8,11,12,17,20,22,24,25,29,33,37,38,39,40,43,44,45,47,48,49]:
                        return 1
                else:
                    if spot in [14,15,19,22,23,27,29,34,40,41]:
                        return 1
            if self.game.red_odds.position == 6 or self.game.red_odds.position == 7:
                #Wipers are mounted on opposite side.  Manual reads backwards.
                if self.game.odds_only.status == True:
                    if spot in [2,3,12,13,21,25,26,30,38,42]:
                        return 1
                else:
                    if spot in [2,10,11,17,35,40,46]:
                        return 1
            return 0
        if color == "green":
            if self.game.green_odds.position == 2 or self.game.green_odds.position == 3 or self.game.green_odds.position == 4:
                #Wipers are mounted on opposite side.  Manual reads backwards.
                if spot in [2,10,11,17,35,40,46]:
                    return 1
            if self.game.green_odds.position == 5:
                if self.game.odds_only.status == True:
                    if spot in [2,3,12,13,21,25,26,30,38,42]:
                        return 1
                else:
                    if spot in [14,15,19,22,23,27,29,34,40,41]:
                        return 1
            if self.game.green_odds.position == 6 or self.game.green_odds.position == 7:
                if self.game.odds_only.status == True:
                    if spot in [2,6,7,8,11,12,17,20,22,24,25,29,33,37,38,39,40,43,44,45,47,48,49]:
                        return 1
                else:
                    if spot in [2,4,6,7,8,9,10,11,12,15,16,20,21,22,29,33,34,39,40,44,49]:
                        return 1
            return 0

        return 0

    def check_red_mixer3(self):
        mix3 = self.game.mixer3.position
        if mix3 in [5,10]:
            return 1
        if mix3 in [14,21]:
            return 1
        if mix3 in [3,9,13,17,20,23]:
            return 1
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
        if mix3 in [5,10]:
            return 1
        if mix3 in [14,21]:
            return 1
        if mix3 in [2,7,8,12,16,18]:
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
        #CHECK MIXER3 after spotting disc position
        mix3 = self.game.mixer3.position
        if mix3 in [1,4,6,11,15,19,22,24]:
            return 1
        else:
            return 0

    def scan_features(self):
        p = self.features_probability()

    def check_mixer4(self):
        m4 = self.game.mixer4.position
        if self.game.green_odds.position >= 4:
            if m4 in [12,13,15,18,20,21]:
                self.game.mixer4_relay.engage(self.game)
        elif self.game.green_odds.position >= 5:
            if m4 in [4,6,12,15,18,20]:
                self.game.mixer4_relay.engage(self.game)
        elif self.game.green_odds.position >= 6:
            if m4 in [2,5,7,13,19]:
                self.game.mixer4_relay.engage(self.game)
        elif self.game.green_odds.position >= 7:
            if m4 == 10:
                self.game.mixer4_relay.engage(self.game)
        elif self.game.green_odds.position >= 8:
            if m4 == 23:
                self.game.mixer4_relay.engage(self.game)
        if self.game.red_odds.position >= 4:
            if m4 in [7,8,12,13,17,18]:
                self.game.mixer4_relay.engage(self.game)
        elif self.game.red_odds.position >= 5:
            if m4 in [5,6,14,15,21]:
                self.game.mixer4_relay.engage(self.game)
        elif self.game.red_odds.position >= 6:
            if m4 in [3,4,10,16,20]:
                self.game.mixer4_relay.engage(self.game)
        elif self.game.red_odds.position >= 7:
            if m4 in [11,19,22]:
                self.game.mixer4_relay.engage(self.game)
        elif self.game.red_odds.position >= 8:
            if m4 == 23:
                self.game.mixer4_relay.engage(self.game)
        if self.game.yellow_odds.position >= 4:
            if m4 in [9,10,12,13,15,16]:
                self.game.mixer4_relay.engage(self.game)
        elif self.game.yellow_odds.position >= 5:
            if m4 in [4,5,6,8,14,18,19]:
                self.game.mixer4_relay.engage(self.game)
        elif self.game.yellow_odds.position >= 6:
            if m4 in [1,11,17,21]:
                self.game.mixer4_relay.engage(self.game)
        elif self.game.yellow_odds.position >= 7:
            if m4 in [7,20,22]:
                self.game.mixer4_relay.engage(self.game)
        elif self.game.yellow_odds.position >= 8:
            if m4 == 23:
                self.game.mixer4_relay.engage(self.game)

    def features_probability(self):
        self.check_mixer4()
        if self.game.mixer4_relay.status == False:
            self.features_spotting()
        else:
            self.game.mixer4_relay.disengage()

    def features_spotting(self):
        sd = self.game.spotting.position
        m = self.game.mixer3.position
        if sd == 23:
            if self.game.cu:
                self.game.four_stars.engage(self.game)
            elif self.game.magic_numbers_feature.position < 10:
                self.game.four_stars.engage(self.game)
        if sd in [4,30,32,36]:
                self.game.hole_feature.engage(self.game)
        if sd == 31:
            if self.game.magic_numbers_feature.position >= 4:
                if m in [1,4,7,9,13,15,19,22]:
                    self.game.before_fifth.engage(self.game)
                if m in [3,5,8,10,14,18,20,23]:
                    self.game.after_fifth.engage(self.game)
        if sd in [9,37,45]:
            self.game.super_line_feature.engage(self.game)
        if self.game.features.status == True:
            if sd == 45:
                self.game.four_stars.engage(self.game)
            if sd == 13:
                if self.game.cu:
                    self.holes.append(16)
            if sd == 36:
                if self.game.magic_numbers_feature.position >= 4:
                    if m in [1,4,7,9,13,15,19,22]:
                        self.game.before_fifth.engage(self.game)
                    if m in [3,5,8,10,14,18,20,23]:
                        self.game.after_fifth.engage(self.game)
        if self.game.selection_feature.position < 1:
            self.game.selection_feature.step()
        else:
            if sd == 50:
                self.step_selection(9)
            if self.game.odds_only.status == True:
                if sd == 29:
                    self.step_selection(9)
            if self.game.selection_feature.position == 1 or self.game.selection_feature.position == 2:
                if sd in [4,9,23,32,37]:
                    if self.game.selection_feature.position == 2:
                        self.step_selection(1)
                    else:
                        self.step_selection(2)
            elif self.game.selection_feature.position == 3 or self.game.selection_feature.position == 4:
                if sd in [3,14]:
                    if self.game.selection_feature.position == 4:
                        self.step_selection(1)
                    else:
                        self.step_selection(2)
                if self.game.features.status == True:
                    if sd in [17,34]:
                        if self.game.selection_feature.position == 4:
                            self.step_selection(1)
                        else:
                            self.step_selection(2)
            elif self.game.selection_feature.position == 5 or self.game.selection_feature.position == 6:
                if sd in [27,41]:
                    if self.game.selection_feature.position == 6:
                        self.step_selection(1)
                    else:
                        self.step_selection(2)
                if self.game.features.status == True:
                    if self.game.selection_feature.position == 6:
                        self.step_selection(1)
                    else:
                        self.step_selection(2)
        if self.game.magic_numbers_feature.position == 0:
            self.step_magic_number(1)
        else:
            if self.game.magic_numbers_feature.position < 4:
                if sd == 0:
                    self.step_magic_number(1)
                if sd in [21,22,26,41,49]:
                    self.step_magic_number(4 - self.game.magic_numbers_feature.position)
                if sd in [1,2,7,11,12,16,29,30,39,40,42]:
                    self.step_magic_number(4 - self.game.magic_numbers_feature.position)
            elif self.game.magic_numbers_feature.position >= 4:
                if sd in [21,22,26,41,49]:
                    if self.game.magic_numbers_feature.position % 2 == 0:
                        self.step_magic_number(2)
                    else:
                        self.step_magic_number(1)
                if sd in [1,2,7,11,12,16,29,30,39,40,42]:
                    if self.game.magic_numbers_feature.position % 2 == 0:
                        self.step_magic_number(2)
                    else:
                        self.step_magic_number(1)
            if self.game.features.status == True:
                if self.game.magic_numbers_feature.position < 4:
                    if sd == 0:
                        self.step_magic_number(1)
                    if sd in [38,43,46,47,20]:
                        self.step_magic_number(4 - self.game.magic_numbers_feature.position)
                    if sd in [3,4,6,9,10,14,17,18,28,32,34]:
                        self.step_magic_number(4 - self.game.magic_numbers_feature.position)
                elif self.game.magic_numbers_feature.position >= 4:
                    if sd in [38,43,46,47,20]:
                        if self.game.magic_numbers_feature.position % 2 == 0:
                            self.step_magic_number(2)
                        else:
                            self.step_magic_number(1)
                    if sd in [3,4,6,9,10,14,17,18,28,32,34]:
                        if self.game.magic_numbers_feature.position % 2 == 0:
                            self.step_magic_number(2)
                        else:
                            self.step_magic_number(1)
        graphics.acapulco.display(self)

    def step_magic_number(self, number):
        if number >= 1:
            self.game.magic_numbers_feature.step()
            number -= 1
            self.cancel_delayed(name="display")
            self.delay(name="display", delay=0.1, handler=graphics.acapulco.display, param=self)
            self.delay(name="step_mn", delay=0.1, handler=self.step_magic_number, param=number)

    def scan_eb(self):
        if self.game.extra_ball.position in [0,3,6]:
            self.game.extra_ball.step()
            self.check_lifter_status()
            return
        p = self.eb_reflex()
        if p == 1:
            self.eb_probability()
                                
        # Timer resets to 0 position on ball count increasing.  We are fudging this since we will have
        # no good way to measure balls as they return back to the trough.  The ball count unit cannot be
        # relied upon as we do not have a switch in the outhole, and the trough logic is too complex for
        # the task at hand.
        # TODO: implement thunk noises into the units.py to automatically play the noises.
        self.game.timer.reset()
        self.cancel_delayed(name="display")
        self.delay(name="display", delay=0.1, handler=graphics.acapulco.display, param=self)

    def animate_odds_scan(self, args):
        start = args[0]
        diff = args[1]
        num = args[2]
        if start + num >= 50:
            start = 0
        if diff >= 0:
            num = num + 1
            graphics.acapulco.odds_animation([self, start + num])
            self.cancel_delayed(name="display")
            diff = diff - 1
            args = [start,diff,num]
            self.delay(name="odds_animation", delay=0.06, handler=self.animate_odds_scan, param=args)
        else:
            self.cancel_delayed(name="odds_animation")
            self.delay(name="display", delay=0.1, handler=graphics.acapulco.display, param=self)

    def animate_features_scan(self, args):
        start = args[0]
        diff = args[1]
        num = args[2]
        if start + num >= 50:
            start = 0
        if diff >= 0:
            num = num + 1
            graphics.acapulco.feature_animation([self, start + num])
            self.cancel_delayed(name="display")
            diff = diff - 1
            args = [start,diff,num]
            self.delay(name="feature_animation", delay=0.06, handler=self.animate_features_scan, param=args)
        else:
            self.cancel_delayed(name="feature_animation")
            self.delay(name="display", delay=0.1, handler=graphics.acapulco.display, param=self)

    def animate_both(self, args):
        start = args[0]
        diff = args[1]
        num = args[2]
        if start + num >= 50:
            start = 0
        if diff >= 0:
            num = num + 1
            graphics.acapulco.both_animation([self, start + num])
            self.cancel_delayed(name="display")
            diff = diff - 1
            args = [start,diff,num]
            self.delay(name="both_animation", delay=0.06, handler=self.animate_both, param=args)
        else:
            self.cancel_delayed(name="both_animation")
            self.delay(name="display", delay=0.1, handler=graphics.acapulco.display, param=self)

    def animate_eb_scan(self, args):
        start = args[0]
        diff = args[1]
        num = args[2]
        if start + num >= 50:
            start = 0
        if diff >= 0:
            num = num + 1
            graphics.acapulco.eb_animation([self, start + num])
            self.cancel_delayed(name="display")
            diff = diff - 1
            args = [start,diff,num]
            self.delay(name="eb_animation", delay=0.06, handler=self.animate_eb_scan, param=args)
        else:
            self.cancel_delayed(name="eb_animation")
            self.delay(name="display", delay=0.1, handler=graphics.acapulco.display, param=self)

    def eb_probability(self):
        mix3 = self.game.mixer3.position
        sd = self.game.spotting.position
        if sd == 0:
            if mix3 == 12:
                self.step_eb(10 - self.game.extra_ball.position)
                self.check_lifter_status()
        if sd in [1,2,6,7,15,17,23,29,33,34,35,38,39,40,42,44,45,47,48,49]:
            if mix3 not in [6,9,10,12,17,24]:
                self.step_eb(3 - self.game.extra_ball.position)
                self.check_lifter_status()
        if sd in [16,30,43,9,22,19,24,26,10,18]:
            if self.game.cu == 1:
                self.game.extra_ball.step()
                self.check_lifter_status()
 
    def step_eb(self, number):
        if number >= 1:
            self.game.extra_ball.step()
            self.check_lifter_status()
            number -= 1
            self.delay(name="display", delay=0.1, handler=graphics.acapulco.display, param=self)
            self.delay(name="step_eb", delay=0.1, handler=self.step_eb, param=number)

    def step_selection(self, number):
        if number >= 1:
            self.game.selection_feature.step()
            if self.game.selection_feature.position == 3 or self.game.selection_feature.position == 4:
                self.game.yellow_star.engage(self.game)
                self.game.coils.redROLamp.enable()
            elif self.game.selection_feature.position == 5 or self.game.selection_feature.position == 6:
                self.game.yellow_star.disengage()
                self.game.red_star.engage(self.game)
                self.game.coils.redROLamp.disable()
                self.game.coils.yellowROLamp.enable()
            elif self.game.selection_feature.position == 7 or self.game.selection_feature.position == 8:
                self.game.before_fourth.disengage()
                self.game.before_fifth.engage(self.game)
                self.game.coils.yellowROLamp.disable()
                self.game.red_star.disengage()
            elif self.game.selection_feature.position == 9:
                self.game.before_fifth.disengage()
                self.game.after_fifth.engage(self.game)
            number -= 1
            self.cancel_delayed(name="display")
            self.delay(name="display", delay=0.1, handler=graphics.acapulco.display, param=self)
            self.delay(name="step_selection", delay=0.1, handler=self.step_selection, param=number)


    # Define reset as the knock-off, anti-cheat relay disabled, and replay reset enabled.  Motors turn while credits are knocked off.
    # When meter reaches zero and the zero limit switch is hit, turn off motor sound and leave backglass gi on, but with tilt displayed.

    def startup(self):        
        # Every bingo requires the meter to register '0' 
        # before allowing coin entry --
        # also needs to show a plain 'off' backglass.
        self.eb = False
        self.game.anti_cheat.engage(self.game)
        self.tilt_actions()


class Acapulco(procgame.game.BasicGame):
    """ Acapulco was the final game with Magic Numbers """
    def __init__(self, machine_type):
        super(Acapulco, self).__init__(machine_type)
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

        self.searchdisc = units.Search("searchdisc", 50)

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
        self.red_odds = units.Stepper("red_odds", 8, 'acapulco')
        self.yellow_odds = units.Stepper("yellow_odds", 8, 'acapulco')
        self.green_odds = units.Stepper("green_odds", 8, 'acapulco')

        #Replay Counter
        self.red_replay_counter = units.Stepper("red_replay_counter", 2000)
        self.yellow_replay_counter = units.Stepper("yellow_replay_counter", 2000)
        self.green_replay_counter = units.Stepper("green_replay_counter", 2000)
        self.stars_replay_counter = units.Stepper("stars_replay_counter", 2000)

        self.four_stars = units.Relay("four_stars")

        self.magic_numbers_feature = units.Stepper("magic_numbers_feature", 10)

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

        self.selector = units.Stepper("selector", 1)

        self.numbera = units.Stepper("numbera", 5, "acapulco", "continuous")
        self.numberb = units.Stepper("numberb", 5, "acapulco", "continuous")
        self.numberc = units.Stepper("numberc", 5, "acapulco", "continuous")
        self.numberd = units.Stepper("numberd", 5, "acapulco", "continuous")

        #Some special trip relays for spotted numbers and rollovers
        self.red_star = units.Relay("red_star")
        self.yellow_star = units.Relay("yellow_star")

        self.before_fourth = units.Relay("before_fourth")
        self.before_fifth = units.Relay("before_fifth")
        self.after_fifth = units.Relay("after_fifth")
        
        self.hole_feature = units.Relay("hole_feature")

        self.super_line_feature = units.Relay("super_line_feature")
        self.super_line_select = units.Stepper("super_line_select", 4, "acapulco", "continuous")
        self.selection_feature = units.Stepper("selection_feature", 9)

        self.mixer4_relay = units.Relay("mixer4_relay")

        self.replays = 0
        self.returned = False

    def reset(self):
        super(Acapulco, self).reset()
        self.logger = logging.getLogger('game')
        self.load_config('bingo.yaml')
        
        main_mode = SinglecardBingo(self)
        self.modes.add(main_mode)
        
game = Acapulco(machine_type='pdb')
game.reset()
game.run_loop()
