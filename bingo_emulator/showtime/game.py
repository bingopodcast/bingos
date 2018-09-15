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
from bingo_emulator.graphics.showtime import *

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
            graphics.showtime.display(self)
            self.animate_eb_scan([begin,self.game.spotting.movement_amount,self.game.spotting.movement_amount])

        self.delay(name="display", delay=0.1, handler=graphics.showtime.display, param=self)

    def sw_startButton_active(self, sw):
        self.game.eb_play.disengage()
        self.delay(name="display", delay=0.1, handler=graphics.showtime.display, param=self)
        if self.game.replays > 0 or self.game.switches.freeplay.is_active():
            self.game.sound.stop('add')
            self.game.sound.play('add')
            self.game.tilt.disengage()
            self.regular_play()
            self.delay(name="display", delay=0.1, handler=graphics.showtime.display, param=self)

    def sw_enter_active(self, sw):
        if self.game.switches.left.is_active() and self.game.switches.right.is_active():
            self.game.end_run_loop()
            os.system("/home/nbaldridge/proc/bingo_emulator/start_game.sh showtime")
        if self.game.switches.drawer.is_inactive():
            if self.game.selection_feature.position >= 1:
                max_ball = 4
            if self.game.selection_feature.position >= 7:
                max_ball = 5
            if self.game.selection_feature.position == 9:
                max_ball = 6
            if self.game.magic_squares_feature.position == 9:
                if self.game.ball_count.position < max_ball:
                    self.game.sound.play('square')
                    self.game.square_e.step()
                    self.cancel_delayed("squaree_animation")
                    self.animate_squaree([self.game,1,5])
            self.delay(name="display", delay=0.1, handler=graphics.showtime.display, param=self)
        if self.game.ball_count.position >= 5:
            self.search()

    def sw_enter_active_for_500ms(self,sw):
        if self.game.switches.left.is_active() and self.game.switches.right.is_active():
            self.game.end_run_loop()
            os.system("/home/nbaldridge/proc/bingo_emulator/start_game.sh showtime")
        if self.game.switches.drawer.is_inactive():
            if self.game.selection_feature.position >= 1:
                max_ball = 4
            if self.game.selection_feature.position >= 7:
                max_ball = 5
            if self.game.selection_feature.position == 9:
                max_ball = 6
            if self.game.magic_squares_feature.position == 9:
                if self.game.ball_count.position < max_ball:
                    self.game.sound.play('square')
                    self.game.square_e.step()
                    self.cancel_delayed("squaree_animation")
                    self.animate_squaree([self.game,1,5])
            self.delay(name="display", delay=0.1, handler=graphics.showtime.display, param=self)
            self.delay(name="enter", delay=0.6, handler=self.sw_enter_active_for_500ms, param=sw)

    def sw_lettere_active(self, sw):
        if self.game.switches.drawer.is_active():
            if self.game.selection_feature.position >= 1:
                max_ball = 4
            if self.game.selection_feature.position >= 7:
                max_ball = 5
            if self.game.selection_feature.position == 9:
                max_ball = 6
            if self.game.magic_squares_feature.position == 9:
                if self.game.ball_count.position < max_ball:
                    self.game.sound.play('square')
                    self.game.square_e.step()
                    self.cancel_delayed("squaree_animation")
                    self.animate_squaree([self.game,1,5])
            self.delay(name="display", delay=0.1, handler=graphics.showtime.display, param=self)

    def sw_lettere_active_for_500ms(self,sw):
        if self.game.switches.drawer.is_active():
            if self.game.selection_feature.position >= 1:
                max_ball = 4
            if self.game.selection_feature.position >= 7:
                max_ball = 5
            if self.game.selection_feature.position == 9:
                max_ball = 6
            if self.game.magic_squares_feature.position == 9:
                if self.game.ball_count.position < max_ball:
                    self.game.sound.play('square')
                    self.game.square_e.step()
                    self.cancel_delayed("squaree_animation")
                    self.animate_squaree([self.game,1,5])
            self.delay(name="display", delay=0.1, handler=graphics.showtime.display, param=self)
            self.delay(name="lettere", delay=0.6, handler=self.sw_lettere_active_for_500ms, param=sw)


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
            if self.game.ball_count.position >= 1:
                if self.game.selection_feature.position >= 1:
                    max_ball = 4
                if self.game.selection_feature.position >= 7:
                    max_ball = 5
                if self.game.selection_feature.position == 9:
                    max_ball = 6
                if self.game.ball_count.position < max_ball:
                    if self.game.magic_squares_feature.position >= 5:
                        self.game.sound.play('square')
                        self.game.square_a.step()
                        self.cancel_delayed("squarea_animation")
                        self.animate_squarea([self.game,1,1])
                if self.game.ball_count.position >= 5:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.showtime.display, param=self)

    def sw_left_active_for_500ms(self,sw):
        if self.game.switches.drawer.is_inactive():
            if self.game.ball_count.position >= 1:
                if self.game.selection_feature.position >= 1:
                    max_ball = 4
                if self.game.selection_feature.position >= 7:
                    max_ball = 5
                if self.game.selection_feature.position == 9:
                    max_ball = 6
                if self.game.ball_count.position < max_ball:
                    if self.game.magic_squares_feature.position >= 5:
                        self.game.sound.play('square')
                        self.game.square_a.step()
                        self.cancel_delayed("squarea_animation")
                        self.animate_squarea([self.game,1,1])
                if self.game.ball_count.position >= 5:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.showtime.display, param=self)
            self.delay(name="left", delay=0.6, handler=self.sw_left_active_for_500ms, param=sw)

    def sw_lettera_active(self, sw):
        if self.game.switches.drawer.is_active():
            if self.game.ball_count.position >= 1:
                if self.game.selection_feature.position >= 1:
                    max_ball = 4
                if self.game.selection_feature.position >= 7:
                    max_ball = 5
                if self.game.selection_feature.position == 9:
                    max_ball = 6
                if self.game.ball_count.position < max_ball:
                    if self.game.magic_squares_feature.position >= 5:
                        self.game.sound.play('square')
                        self.game.square_a.step()
                        self.cancel_delayed("squarea_animation")
                        self.animate_squarea([self.game,1,1])
                if self.game.ball_count.position >= 5:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.showtime.display, param=self)

    def sw_lettera_active_for_500ms(self,sw):
        if self.game.switches.drawer.is_active():
            if self.game.ball_count.position >= 1:
                if self.game.selection_feature.position >= 1:
                    max_ball = 4
                if self.game.selection_feature.position >= 7:
                    max_ball = 5
                if self.game.selection_feature.position == 9:
                    max_ball = 6
                if self.game.ball_count.position < max_ball:
                    if self.game.magic_squares_feature.position >= 5:
                        self.game.sound.play('square')
                        self.game.square_a.step()
                        self.cancel_delayed("squarea_animation")
                        self.animate_squarea([self.game,1,1])
                if self.game.ball_count.position >= 5:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.showtime.display, param=self)
            self.delay(name="lettera", delay=0.6, handler=self.sw_lettera_active_for_500ms, param=sw)


    def sw_right_active(self, sw):
        if self.game.switches.drawer.is_inactive():
            if self.game.ball_count.position >= 1:
                if self.game.selection_feature.position >= 1:
                    max_ball = 4
                if self.game.selection_feature.position >= 7:
                    max_ball = 5
                if self.game.selection_feature.position == 9:
                    max_ball = 6
                if self.game.ball_count.position < max_ball:
                    if self.game.magic_squares_feature.position >= 5:
                        self.game.sound.play('square')
                        self.game.square_b.step()
                        self.cancel_delayed("squareb_animation")
                        self.animate_squareb([self.game,1,2])
                if self.game.ball_count.position >= 5:
                    self.search()

            self.delay(name="display", delay=0.1, handler=graphics.showtime.display, param=self)

    def sw_right_active_for_500ms(self,sw):
        if self.game.switches.drawer.is_inactive():
            if self.game.ball_count.position >= 1:
                if self.game.selection_feature.position >= 1:
                    max_ball = 4
                if self.game.selection_feature.position >= 7:
                    max_ball = 5
                if self.game.selection_feature.position == 9:
                    max_ball = 6
                if self.game.ball_count.position < max_ball:
                    if self.game.magic_squares_feature.position >= 5:
                        self.game.sound.play('square')
                        self.game.square_b.step()
                        self.cancel_delayed("squareb_animation")
                        self.animate_squareb([self.game,1,2])
                if self.game.ball_count.position >= 5:
                    self.search()

            self.delay(name="display", delay=0.1, handler=graphics.showtime.display, param=self)
            self.delay(name="right", delay=0.6, handler=self.sw_right_active_for_500ms, param=sw)


    def sw_letterb_active(self, sw):        
        if self.game.switches.drawer.is_active():
            if self.game.ball_count.position >= 1:
                if self.game.selection_feature.position >= 1:
                    max_ball = 4
                if self.game.selection_feature.position >= 7:
                    max_ball = 5
                if self.game.selection_feature.position == 9:
                    max_ball = 6
                if self.game.ball_count.position < max_ball:
                    if self.game.magic_squares_feature.position >= 5:
                        self.game.sound.play('square')
                        self.game.square_b.step()
                        self.cancel_delayed("squareb_animation")
                        self.animate_squareb([self.game,1,2])
                if self.game.ball_count.position >= 5:
                    self.search()

            self.delay(name="display", delay=0.1, handler=graphics.showtime.display, param=self)

    def sw_letterb_active_for_500ms(self,sw):
        if self.game.switches.drawer.is_active():
            if self.game.ball_count.position >= 1:
                if self.game.selection_feature.position >= 1:
                    max_ball = 4
                if self.game.selection_feature.position >= 7:
                    max_ball = 5
                if self.game.selection_feature.position == 9:
                    max_ball = 6
                if self.game.ball_count.position < max_ball:
                    if self.game.magic_squares_feature.position >= 5:
                        self.game.sound.play('square')
                        self.game.square_b.step()
                        self.cancel_delayed("squareb_animation")
                        self.animate_squareb([self.game,1,2])
                if self.game.ball_count.position >= 5:
                    self.search()

            self.delay(name="display", delay=0.1, handler=graphics.showtime.display, param=self)
            self.delay(name="letterb", delay=0.6, handler=self.sw_letterb_active_for_500ms, param=sw)


    def sw_blue_active(self, sw):
        if self.game.switches.drawer.is_inactive():
            if self.game.ball_count.position >= 1:
                if self.game.selection_feature.position >= 1:
                    max_ball = 4
                if self.game.selection_feature.position >= 7:
                    max_ball = 5
                if self.game.selection_feature.position == 9:
                    max_ball = 6
                if self.game.ball_count.position < max_ball:
                    if self.game.magic_squares_feature.position >= 5:
                        self.game.sound.play('square')
                        self.game.square_c.step()
                        self.cancel_delayed("squarec_animation")
                        self.animate_squarec([self.game,1,3])
                if self.game.ball_count.position >= 5:
                    self.search()

            self.delay(name="display", delay=0.1, handler=graphics.showtime.display, param=self)

    def sw_blue_active_for_500ms(self,sw):
        if self.game.switches.drawer.is_inactive():
            if self.game.ball_count.position >= 1:
                if self.game.selection_feature.position >= 1:
                    max_ball = 4
                if self.game.selection_feature.position >= 7:
                    max_ball = 5
                if self.game.selection_feature.position == 9:
                    max_ball = 6
                if self.game.ball_count.position < max_ball:
                    if self.game.magic_squares_feature.position >= 5:
                        self.game.sound.play('square')
                        self.game.square_c.step()
                        self.cancel_delayed("squarec_animation")
                        self.animate_squarec([self.game,1,3])
                if self.game.ball_count.position >= 5:
                    self.search()

            self.delay(name="display", delay=0.1, handler=graphics.showtime.display, param=self)
            self.delay(name="blue", delay=0.6, handler=self.sw_blue_active_for_500ms, param=sw)

    def sw_letterc_active(self, sw):
        if self.game.switches.drawer.is_active():
            if self.game.ball_count.position >= 1:
                if self.game.selection_feature.position >= 1:
                    max_ball = 4
                if self.game.selection_feature.position >= 7:
                    max_ball = 5
                if self.game.selection_feature.position == 9:
                    max_ball = 6
                if self.game.ball_count.position < max_ball:
                    if self.game.magic_squares_feature.position >= 5:
                        self.game.sound.play('square')
                        self.game.square_c.step()
                        self.cancel_delayed("squarec_animation")
                        self.animate_squarec([self.game,1,3])
                if self.game.ball_count.position >= 5:
                    self.search()

            self.delay(name="display", delay=0.1, handler=graphics.showtime.display, param=self)

    def sw_letterc_active_for_500ms(self,sw):
        if self.game.switches.drawer.is_active():
            if self.game.ball_count.position >= 1:
                if self.game.selection_feature.position >= 1:
                    max_ball = 4
                if self.game.selection_feature.position >= 7:
                    max_ball = 5
                if self.game.selection_feature.position == 9:
                    max_ball = 6
                if self.game.ball_count.position < max_ball:
                    if self.game.magic_squares_feature.position >= 5:
                        self.game.sound.play('square')
                        self.game.square_c.step()
                        self.cancel_delayed("squarec_animation")
                        self.animate_squarec([self.game,1,3])
                if self.game.ball_count.position >= 5:
                    self.search()

            self.delay(name="display", delay=0.1, handler=graphics.showtime.display, param=self)
            self.delay(name="letterc", delay=0.6, handler=self.sw_letterc_active_for_500ms, param=sw)


    def sw_green_active(self, sw):
        if self.game.switches.drawer.is_inactive():
            if self.game.ball_count.position >= 1:
                if self.game.selection_feature.position >= 1:
                    max_ball = 4
                if self.game.selection_feature.position >= 7:
                    max_ball = 5
                if self.game.selection_feature.position == 9:
                    max_ball = 6
                if self.game.ball_count.position < max_ball:
                    if self.game.magic_squares_feature.position >= 8:
                        self.game.sound.play('square')
                        self.game.square_d.step()
                        self.cancel_delayed("squared_animation")
                        self.animate_squared([self.game,1,4])
                if self.game.ball_count.position >= 5:
                    self.search()

            self.delay(name="display", delay=0.1, handler=graphics.showtime.display, param=self)

    def sw_green_active_for_500ms(self,sw):
        if self.game.switches.drawer.is_inactive():
            if self.game.ball_count.position >= 1:
                if self.game.selection_feature.position >= 1:
                    max_ball = 4
                if self.game.selection_feature.position >= 7:
                    max_ball = 5
                if self.game.selection_feature.position == 9:
                    max_ball = 6
                if self.game.ball_count.position < max_ball:
                    if self.game.magic_squares_feature.position >= 8:
                        self.game.sound.play('square')
                        self.game.square_d.step()
                        self.cancel_delayed("squared_animation")
                        self.animate_squared([self.game,1,4])
                if self.game.ball_count.position >= 5:
                    self.search()

            self.delay(name="display", delay=0.1, handler=graphics.showtime.display, param=self)
            self.delay(name="green", delay=0.6, handler=self.sw_green_active_for_500ms, param=sw)


    def sw_letterd_active(self, sw):
        if self.game.switches.drawer.is_active():
            if self.game.ball_count.position >= 1:
                if self.game.selection_feature.position >= 1:
                    max_ball = 4
                if self.game.selection_feature.position >= 7:
                    max_ball = 5
                if self.game.selection_feature.position == 9:
                    max_ball = 6
                if self.game.ball_count.position < max_ball:
                    if self.game.magic_squares_feature.position >= 8:
                        self.game.sound.play('square')
                        self.game.square_d.step()
                        self.cancel_delayed("squared_animation")
                        self.animate_squared([self.game,1,4])
                if self.game.ball_count.position >= 5:
                    self.search()

            self.delay(name="display", delay=0.1, handler=graphics.showtime.display, param=self)

    def sw_letterd_active_for_500ms(self,sw):
        if self.game.switches.drawer.is_active():
            if self.game.ball_count.position >= 1:
                if self.game.selection_feature.position >= 1:
                    max_ball = 4
                if self.game.selection_feature.position >= 7:
                    max_ball = 5
                if self.game.selection_feature.position == 9:
                    max_ball = 6
                if self.game.ball_count.position < max_ball:
                    if self.game.magic_squares_feature.position >= 8:
                        self.game.sound.play('square')
                        self.game.square_d.step()
                        self.cancel_delayed("squared_animation")
                        self.animate_squared([self.game,1,4])
                if self.game.ball_count.position >= 5:
                    self.search()

            self.delay(name="display", delay=0.1, handler=graphics.showtime.display, param=self)
            self.delay(name="letterd", delay=0.6, handler=self.sw_letterd_active_for_500ms, param=sw)


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
        self.cancel_delayed(name="green_replay_step_up")
        self.cancel_delayed(name="yellow_replay_step_up")
        self.cancel_delayed(name="red_replay_step_up")
        self.cancel_delayed(name="corners_replay_step_up")
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
            if self.game.switches.shutter.is_inactive():
                self.game.coils.shutter.enable()
            self.replay_step_down()
            graphics.showtime.display(self)
            self.check_lifter_status()
        else:
            self.holes = []
            self.game.red_replay_counter.reset()
            self.game.yellow_replay_counter.reset()
            self.game.green_replay_counter.reset()
            self.game.corners.disengage()
            self.game.start.engage(self.game)
            self.game.selector.reset()
            self.game.magic_squares_feature.reset()
            if self.game.square_a.position != 0:
                self.magic_squarea_reset(self.game.square_a.position)
            if self.game.square_b.position != 0:
                self.magic_squareb_reset(self.game.square_b.position)
            if self.game.square_c.position != 0:
                self.magic_squarec_reset(self.game.square_c.position)
            if self.game.square_d.position != 0:
                self.magic_squared_reset(self.game.square_d.position)
            if self.game.square_e.position != 0:
                self.magic_squaree_reset(self.game.square_e.position)
            self.game.ball_count.reset()
            self.game.ballyhole.disengage()
            self.game.extra_ball.reset()
            self.game.green_odds.reset()
            self.game.red_odds.reset()
            self.game.selection_feature.reset()
            self.game.coils.redROLamp.disable()
            self.game.coils.yellowROLamp.disable()
            self.game.yellow_odds.reset()
            self.game.timer.reset()
            self.game.sound.play_music('motor', -1)
            self.regular_play()
        self.delay(name="display", delay=0.1, handler=graphics.showtime.display, param=self)
        self.game.tilt.disengage()

    def magic_squarea_reset(self, number):
        if number != 0:
            self.game.sound.play('square')
            self.game.square_a.step()
            self.delay(name="display", delay=0, handler=graphics.showtime.display, param=self)
            self.cancel_delayed("squarea_animation")
            self.animate_squarea([self.game,1,1])
            number = self.game.square_a.position
            self.delay(name="magic_squarea_reset", delay=0.7, handler=self.magic_squarea_reset, param=number)

    def magic_squareb_reset(self, number):
        if number != 0:
            self.game.sound.play('square')
            self.game.square_b.step()
            self.delay(name="display", delay=0, handler=graphics.showtime.display, param=self)
            self.cancel_delayed("squareb_animation")
            self.animate_squareb([self.game,1,2])
            number = self.game.square_b.position
            self.delay(name="magic_squareb_reset", delay=0.7, handler=self.magic_squareb_reset, param=number)

    def magic_squarec_reset(self, number):
        if number != 0:
            self.game.sound.play('square')
            self.game.square_c.step()
            self.delay(name="display", delay=0, handler=graphics.showtime.display, param=self)
            self.cancel_delayed("squarec_animation")
            self.animate_squarec([self.game,1,3])
            number = self.game.square_c.position
            self.delay(name="magic_squarec_reset", delay=0.7, handler=self.magic_squarec_reset, param=number)

    def magic_squared_reset(self, number):
        if number != 0:
            self.game.sound.play('square')
            self.game.square_d.step()
            self.delay(name="display", delay=0, handler=graphics.showtime.display, param=self)
            self.cancel_delayed("squared_animation")
            self.animate_squared([self.game,1,4])
            number = self.game.square_d.position
            self.delay(name="magic_squared_reset", delay=0.7, handler=self.magic_squared_reset, param=number)

    def magic_squaree_reset(self, number):
        if number != 0:
            self.game.sound.play('square')
            self.game.square_e.step()
            self.delay(name="display", delay=0, handler=graphics.showtime.display, param=self)
            self.cancel_delayed("squaree_animation")
            self.animate_squaree([self.game,1,5])
            number = self.game.square_e.position
            self.delay(name="magic_squaree_reset", delay=0.1, handler=self.magic_squaree_reset, param=number)

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
        if self.game.ball_count.position == 5:
            self.game.sound.play('tilt')
            self.game.sound.play('tilt')
        if self.game.ball_count.position >= 5:
            if self.game.search_index.status == False:
                self.search()
        if self.game.ball_count.position <= 7:
            self.check_lifter_status()
        self.delay(name="display", delay=0.1, handler=graphics.showtime.display, param=self)


    # This is really nasty, but it is how we render graphics for each individual hole.
    # numbers are added (or removed from) a list.  In this way, I can re-use the same
    # routine even for games where there are ball return functions like Surf Club.

    def sw_hole1_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(1)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.showtime.display, param=self)

    def sw_hole2_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(2)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.showtime.display, param=self)

    def sw_hole3_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(3)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.showtime.display, param=self)

    def sw_hole4_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(4)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.showtime.display, param=self)

    def sw_hole5_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(5)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.showtime.display, param=self)

    def sw_hole6_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(6)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.showtime.display, param=self)

    def sw_hole7_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(7)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.showtime.display, param=self)

    def sw_hole8_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(8)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.showtime.display, param=self)

    def sw_hole9_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(9)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.showtime.display, param=self)

    def sw_hole10_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(10)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.showtime.display, param=self)

    def sw_hole11_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(11)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.showtime.display, param=self)

    def sw_hole12_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(12)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.showtime.display, param=self)

    def sw_hole13_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(13)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.showtime.display, param=self)

    def sw_hole14_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(14)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.showtime.display, param=self)

    def sw_hole15_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(15)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.showtime.display, param=self)

    def sw_hole16_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(16)
            if self.game.ballyhole.status == True:
                self.step_eb(3 - self.game.extra_ball.position)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.showtime.display, param=self)

    def sw_hole17_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(17)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.showtime.display, param=self)

    def sw_hole18_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(18)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.showtime.display, param=self)

    def sw_hole19_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(19)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.showtime.display, param=self)

    def sw_hole20_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(20)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.showtime.display, param=self)

    def sw_hole21_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(21)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.showtime.display, param=self)

    def sw_hole22_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(22)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.showtime.display, param=self)

    def sw_hole23_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(23)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.showtime.display, param=self)

    def sw_hole24_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(24)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.showtime.display, param=self)

    def sw_hole25_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(25)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.showtime.display, param=self)

    def sw_replayReset_active(self, sw):
        self.game.anti_cheat.disengage()
        self.holes = []
        graphics.showtime.display(self)
        self.tilt_actions()
        self.replay_step_down(self.game.replays)

    def tilt_actions(self):
        self.game.start.disengage()
        self.cancel_delayed(name="replay_reset")
        self.cancel_delayed(name="red_replay_step_up")
        self.cancel_delayed(name="yellow_replay_step_up")
        self.cancel_delayed(name="green_replay_step_up")
        self.cancel_delayed(name="corners_replay_step_up")
        self.cancel_delayed(name="blink")
        self.cancel_delayed(name="timeout")
        self.game.red_replay_counter.reset()
        self.game.yellow_replay_counter.reset()
        self.game.green_replay_counter.reset()
        self.game.corners.disengage()
        self.game.selector.reset()
        self.game.ball_count.reset()
        self.game.extra_ball.reset()
        self.game.green_odds.reset()
        self.game.yellow_odds.reset()
        self.game.red_odds.reset()
        self.game.eb_play.disengage()
        self.game.search_index.disengage()
        self.game.magic_squares_feature.reset()
        self.game.ballyhole.disengage()
        if self.game.ball_count.position == 0:
            if self.game.switches.shutter.is_active():
                self.game.coils.shutter.enable()
        self.holes = []
        self.game.anti_cheat.engage(game)
        self.game.tilt.engage(self.game)
        self.game.sound.stop_music()
        self.game.sound.play('tilt')
        # displays "Tilt" on the backglass, you have to recoin.
        self.delay(name="display", delay=0.1, handler=graphics.showtime.display, param=self)

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
                graphics.replay_step_down(self.game.replays, graphics.showtime.reel1, graphics.showtime.reel10, graphics.showtime.reel100)
                self.game.coils.registerDown.pulse()
                number -= 1
                graphics.showtime.display(self)
                self.delay(name="replay_reset", delay=0.13, handler=self.replay_step_down, param=number)
            elif number == 1:
                self.game.replays -= 1
                graphics.replay_step_down(self.game.replays, graphics.showtime.reel1, graphics.showtime.reel10, graphics.showtime.reel100)
                self.game.coils.registerDown.pulse()
                number -= 1
                graphics.showtime.display(self)
                self.cancel_delayed(name="replay_reset")
        else: 
            if self.game.replays > 0:
                self.game.replays -= 1
                graphics.replay_step_down(self.game.replays, graphics.showtime.reel1, graphics.showtime.reel10, graphics.showtime.reel100)
                self.delay(name="display", delay=0.1, handler=graphics.showtime.display, param=self)
            self.game.coils.registerDown.pulse()

    def replay_step_up(self):
        if self.game.replays < 899:
            self.game.replays += 1
            graphics.replay_step_up(self.game.replays, graphics.showtime.reel1, graphics.showtime.reel10, graphics.showtime.reel100)
        self.game.coils.registerUp.pulse()
        self.game.reflex.increase()
        graphics.showtime.display(self)

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
                graphics.showtime.display(self)
                self.animate_eb_scan([begin,self.game.spotting.movement_amount,self.game.spotting.movement_amount])
                self.delay(name="display", delay=0.1, handler=graphics.showtime.display, param=self)
                return
            if self.game.eb_play.status == False:
                self.game.eb_play.engage(self.game)
                self.delay(name="display", delay=0.1, handler=graphics.showtime.display, param=self)
                self.sw_yellow_active(sw)
           
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

    def find_winner(self, relays, card, corners, yellow, red, green):
        if self.game.search_index.status == False and self.game.replays < 899:
            if red == True:
                if self.game.red_odds.position == 1:
                    threeodds = 4
                    fourodds = 16
                    fiveodds = 75
                elif self.game.red_odds.position == 2:
                    threeodds = 6
                    fourodds = 20
                    fiveodds = 75
                elif self.game.red_odds.position == 3:
                    threeodds = 8
                    fourodds = 24
                    fiveodds = 96
                elif self.game.red_odds.position == 4:
                    threeodds = 16
                    fourodds = 50
                    fiveodds = 96
                elif self.game.red_odds.position == 5:
                    threeodds = 32
                    fourodds = 96
                    fiveodds = 200
                elif self.game.red_odds.position == 6:
                    threeodds = 64
                    fourodds = 144
                    fiveodds = 300
                elif self.game.red_odds.position == 7:
                    threeodds = 120
                    fourodds = 240
                    fiveodds = 450
                elif self.game.red_odds.position == 8:
                    threeodds = 192
                    fourodds = 480
                    fiveodds = 600
            elif yellow == True:
                if self.game.yellow_odds.position == 1:
                    threeodds = 4
                    fourodds = 16
                    fiveodds = 75
                elif self.game.yellow_odds.position == 2:
                    threeodds = 6
                    fourodds = 20
                    fiveodds = 75
                elif self.game.yellow_odds.position == 3:
                    threeodds = 8
                    fourodds = 24
                    fiveodds = 96
                elif self.game.yellow_odds.position == 4:
                    threeodds = 16
                    fourodds = 50
                    fiveodds = 96
                elif self.game.yellow_odds.position == 5:
                    threeodds = 32
                    fourodds = 96
                    fiveodds = 200
                elif self.game.yellow_odds.position == 6:
                    threeodds = 64
                    fourodds = 144
                    fiveodds = 300
                elif self.game.yellow_odds.position == 7:
                    threeodds = 120
                    fourodds = 240
                    fiveodds = 450
                elif self.game.yellow_odds.position == 8:
                    threeodds = 192
                    fourodds = 480
                    fiveodds = 600
            elif green == True or corners == True:
                if self.game.green_odds.position == 1:
                    threeodds = 4
                    fourodds = 16
                    fiveodds = 75
                elif self.game.green_odds.position == 2:
                    threeodds = 6
                    fourodds = 20
                    fiveodds = 75
                elif self.game.green_odds.position == 3:
                    threeodds = 8
                    fourodds = 24
                    fiveodds = 96
                elif self.game.green_odds.position == 4:
                    threeodds = 16
                    fourodds = 50
                    fiveodds = 96
                elif self.game.green_odds.position == 5:
                    threeodds = 32
                    fourodds = 96
                    fiveodds = 200
                elif self.game.green_odds.position == 6:
                    threeodds = 64
                    fourodds = 144
                    fiveodds = 300
                elif self.game.green_odds.position == 7:
                    threeodds = 120
                    fourodds = 240
                    fiveodds = 450
                elif self.game.green_odds.position == 8:
                    threeodds = 192
                    fourodds = 480
                    fiveodds = 600

            if relays == 3:
                if not corners:
                    if red:
                        if self.game.red_replay_counter.position < threeodds:
                            self.game.search_index.engage(self.game)
                            self.red_replay_step_up(threeodds - self.game.red_replay_counter.position)
                    elif yellow:
                        if self.game.yellow_replay_counter.position < threeodds:
                            self.game.search_index.engage(self.game)
                            self.yellow_replay_step_up(threeodds - self.game.yellow_replay_counter.position)
                    else:
                        if self.game.green_replay_counter.position < threeodds:
                            self.game.search_index.engage(self.game)
                            self.green_replay_step_up(threeodds - self.game.green_replay_counter.position)
            if relays == 4:
                if corners and self.game.corners.status == True:
                    if self.game.corners.status == True:
                        if self.game.green_replay_counter.position < fiveodds:
                            self.game.search_index.engage(self.game)
                            self.green_replay_step_up(fiveodds - self.game.green_replay_counter.position)
                else:
                    if not corners:
                        if red:
                            if self.game.red_replay_counter.position < fourodds:
                                self.game.search_index.engage(self.game)
                                self.red_replay_step_up(fourodds - self.game.red_replay_counter.position)
                        elif yellow:
                            if self.game.yellow_replay_counter.position < fourodds:
                                self.game.search_index.engage(self.game)
                                self.yellow_replay_step_up(fourodds - self.game.yellow_replay_counter.position)
                        else:
                            if self.game.green_replay_counter.position < fourodds:
                                self.game.search_index.engage(self.game)
                                self.green_replay_step_up(fourodds - self.game.green_replay_counter.position)
            if relays == 5:
                if red:
                    if self.game.red_replay_counter.position < fiveodds:
                        self.game.search_index.engage(self.game)
                        self.red_replay_step_up(fiveodds - self.game.red_replay_counter.position)
                elif yellow:
                    if self.game.yellow_replay_counter.position < fiveodds:
                        self.game.search_index.engage(self.game)
                        self.yellow_replay_step_up(fiveodds - self.game.yellow_replay_counter.position)
                else:
                    if self.game.green_replay_counter.position < fiveodds:
                        self.game.search_index.engage(self.game)
                        self.green_replay_step_up(fiveodds - self.game.green_replay_counter.position)

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

    def closed_search_relays(self, rivets, c):
        # This function is critical, as it will determine which card is returned, etc.  I need to check the position of the
        # replay counter for the card. We will get a row back
        # that has the numbers on the position which will return the search relay connected.  When three out of the five relays
        # are connected, we get a winner!
       
        if self.game.square_a.position == 0:
            self.p1 = 9
            self.p2 = 1
            self.q1 = 4
            self.q2 = 19
        elif self.game.square_a.position == 1:
            self.p1 = 4
            self.p2 = 9
            self.q1 = 19
            self.q2 = 1
        elif self.game.square_a.position == 2:
            self.p1 = 19
            self.p2 = 4
            self.q1 = 1
            self.q2 = 9
        else:
            self.p1 = 1
            self.p2 = 19
            self.q1 = 9
            self.q2 = 4

        if self.game.square_b.position == 0:
            self.r1 = 25
            self.r2 = 24
            self.s1 = 6
            self.s2 = 23
        elif self.game.square_b.position == 1:
            self.r1 = 6
            self.r2 = 25
            self.s1 = 23
            self.s2 = 24
        elif self.game.square_b.position == 2:
            self.r1 = 23
            self.r2 = 6
            self.s1 = 24
            self.s2 = 25
        else:
            self.r1 = 24
            self.r2 = 23
            self.s1 = 25
            self.s2 = 6

        if self.game.square_c.position == 0:
            self.p3 = 2
            self.p4 = 11
            self.q3 = 7
            self.q4 = 22
        elif self.game.square_c.position == 1:
            self.p3 = 7
            self.p4 = 2
            self.q3 = 22
            self.q4 = 11
        elif self.game.square_c.position == 2:
            self.p3 = 22
            self.p4 = 7
            self.q3 = 11
            self.q4 = 2
        else:
            self.p3 = 11
            self.p4 = 22
            self.q3 = 2
            self.q4 = 7

        if self.game.square_d.position == 0:
            self.r3 = 16
            self.r4 = 13
            self.s3 = 5
            self.s4 = 21
        elif self.game.square_d.position == 1:
            self.r3 = 5
            self.r4 = 16
            self.s3 = 21
            self.s4 = 13
        elif self.game.square_d.position == 2:
            self.r3 = 21
            self.r4 = 5
            self.s3 = 13
            self.s4 = 16
        else:
            self.r3 = 13
            self.r4 = 21
            self.s3 = 16
            self.s4 = 5

        if self.game.square_e.position == 0:
            self.t1 = 12
            self.t2 = 8
            self.t3 = 14
            self.t4 = 3
        elif self.game.square_e.position == 1:
            self.t1 = 3
            self.t2 = 12
            self.t3 = 8
            self.t4 = 14
        elif self.game.square_e.position == 2:
            self.t1 = 14
            self.t2 = 3
            self.t3 = 12
            self.t4 = 8
        else:
            self.t1 = 8
            self.t2 = 14
            self.t3 = 3
            self.t4 = 12

        self.pos = {}
        self.pos[0] = {}
        self.pos[1] = {self.p1:1, self.p2:2, self.p3:3, self.p4:4, 15:5}
        self.pos[2] = {self.q1:1, self.q2:2, self.q3:3, self.q4:4, 18:5}
        self.pos[3] = {self.r1:1, self.r2:2, self.r3:3, self.r4:4, 17:5}
        self.pos[4] = {self.s1:1, self.s2:2, self.s3:3, self.s4:4, 20:5}
        self.pos[5] = {self.t1:1, self.t2:2, self.t3:3, self.t4:4, 10:5}
        self.pos[6] = {self.p1:1, self.q1:2, self.r1:3, self.s1:4, self.t1:5}
        self.pos[7] = {self.p2:1, self.q2:2, self.r2:3, self.s2:4, self.t2:5}
        self.pos[8] = {self.p3:1, self.q3:2, self.r3:3, self.s3:4, self.t3:5}
        self.pos[9] = {self.p4:1, self.q4:2, self.r4:3, self.s4:4, self.t4:5}
        self.pos[10] = {15:1, 18:2, 17:3, 20:4, 10:5}
        self.pos[11] = {self.p1:1, self.q2:2, self.r3:3, self.s4:4, 10:5}
        self.pos[12] = {15:1, self.q4:2, self.r3:3, self.s2:4, self.t1:5}
        self.pos[13] = {}
        self.pos[14] = {self.p1:1, 15:2, self.t1:3, 10:4}
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

        corners = False
        card = 0
        yellow = False
        red = False
        green = False

        if rivets in range(0, 13):
            card = 1
        if rivets == 14:
            corners = True
        if rivets == 1:
            red = True
        if rivets == 2:
            yellow = True
        if rivets == 3:
            green = True
        if rivets == 4:
            red = True
        if rivets == 5:
            yellow = True
        if rivets == 6:
            yellow = True
        if rivets == 7:
            red = True
        if rivets == 8:
            green = True
        if rivets == 9:
            yellow = True
        if rivets == 10:
            red = True
        if rivets == 11:
            green = True
        if rivets == 12:
            green = True

        return (self.pos[rivets], card, corners, yellow, red, green)
    
    def scan_all(self):
        #Animate scanning of everything - this happens through the spotting disc
        self.all_probability()

    def all_probability(self):
        initial = False
        if self.game.yellow_odds.position <= 2 or self.game.red_odds.position <= 2 or self.game.green_odds.position <= 2:
            initial = True
            self.scan_odds()
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
        if self.game.yellow_odds.position <= 2 or self.game.red_odds.position <= 2 or self.game.green_odds.position <= 2:
            if self.game.yellow_odds.position <= 2:
                self.game.yellow_odds.step()
            if self.game.red_odds.position <= 2:
                self.game.red_odds.step()
            if self.game.green_odds.position <= 2:
                self.game.green_odds.step()
            return
        if self.game.yellow_odds.position >= 2 and self.game.red_odds.position >= 2 and self.game.green_odds.position >= 2:
            m3 = self.game.mixer3.position
            p = self.red_odds_probability()
            if p == 1:
                if m3 in [3,5,9,13,17,20,23]:
                    es = self.check_extra_step()
                    if es == 1:
                        i = random.randint(1,3)
                        self.red_extra_step(i)
                    else:
                        self.red_extra_step(1)
            p = self.yellow_odds_probability()
            if p == 1:
                if m3 in [2,7,8,12,16,18,21]:    
                    es = self.check_extra_step()
                    if es == 1:
                        i = random.randint(1,3)
                        self.yellow_extra_step(i)
                    else:
                        self.yellow_extra_step(1)
            p = self.green_odds_probability()
            if p == 1:
                if m3 in [1,4,6,10,11,14,15,19,22,24]:
                    es = self.check_extra_step()
                    if es == 1:
                        i = random.randint(1,3)
                        self.green_extra_step(i)
                    else:
                        self.green_extra_step(1)

    def yellow_extra_step(self, number):
        if number > 0:
            self.game.yellow_odds.step()
            self.delay(name="display", delay=0, handler=graphics.showtime.display, param=self)
            self.game.coils.sounder.pulse()
            number -= 1
            self.delay(name="yellow_extra_step", delay=0.1, handler=self.yellow_extra_step, param=number)

    def green_extra_step(self, number):
        if number > 0:
            self.game.green_odds.step()
            self.delay(name="display", delay=0, handler=graphics.showtime.display, param=self)
            self.game.coils.sounder.pulse()
            number -= 1
            self.delay(name="green_extra_step", delay=0.1, handler=self.green_extra_step, param=number)

    def red_extra_step(self, number):
        if number > 0:
            self.game.red_odds.step()
            self.delay(name="display", delay=0, handler=graphics.showtime.display, param=self)
            self.game.coils.sounder.pulse()
            number -= 1
            self.delay(name="red_extra_step", delay=0.1, handler=self.red_extra_step, param=number)

    def check_extra_step(self):
        i = random.randint(0,32)
        if i == 16:
            return 1
        else:
            return 0

    def red_odds_probability(self):
        # Check position of Mixer 2, extra scoring relays and current 
        # position of the odds, along with trip relays.
        # For first check, guaranteed single stepup.  Probability doesn't 
        # factor, so I will return as part of the initial check above.
        if self.game.red_odds.position == 1:
            return 1
        else:
            sd = self.game.spotting.position
            if self.game.red_odds.position < 5:
                if self.game.cu:
                    return 1
            elif self.game.red_odds.position == 5:
                if sd in [4,8,10,14,15,19,22,23,24,27,29,31,32,41,42,46,47,48] or sd in range(34,38):
                    return 1
                else:
                    return 0
            elif self.game.red_odds.position == 6:
                if sd in [4,5,8,14,15,23,29,35,36,40,45,47]:
                    return 1
                else:
                    return 0
            elif self.game.red_odds.position == 7:
                if sd in [4,14,15,23,35,40,45]:
                    return 1
                else:
                    return 0
            else:
                return 0

    def yellow_odds_probability(self):
        # Check position of Mixer 2, extra scoring relays and current 
        # position of the odds, along with trip relays.
        # For first check, guaranteed single stepup.  Probability doesn't 
        # factor, so I will return as part of the initial check above.
        if self.game.yellow_odds.position == 1:
            return 1
        else:
            sd = self.game.spotting.position
            if self.game.yellow_odds.position < 5:
                if not self.game.cu:
                    return 1
            elif self.game.yellow_odds.position == 5:
                if sd in [4,8,10,14,15,19,22,23,24,27,29,31,32,41,42,46,47,48] or sd in range(34,38):
                    return 1
                else:
                    return 0
            elif self.game.yellow_odds.position == 6:
                if sd in [4,5,8,14,15,23,29,35,36,40,45,47]:
                    return 1
                else:
                    return 0
            elif self.game.yellow_odds.position == 7:
                if sd in [4,14,15,23,35,40,45]:
                    return 1
                else:
                    return 0
            else:
                return 0

    def green_odds_probability(self):
        # Check position of Mixer 2, extra scoring relays and current 
        # position of the odds, along with trip relays.
        # For first check, guaranteed single stepup.  Probability doesn't 
        # factor, so I will return as part of the initial check above.
        if self.game.green_odds.position == 1:
            return 1
        else:
            sd = self.game.spotting.position
            if self.game.green_odds.position < 5:
                if self.game.cu:
                    return 1
            elif self.game.green_odds.position == 5:
                if sd in [4,5,8,14,15,23,29,35,36,40,45,47]:
                    return 1
                else:
                    return 0
            elif self.game.green_odds.position == 6:
                if sd in [4,14,15,23,35,40,45]:
                    return 1
                else:
                    return 0
            elif self.game.green_odds.position == 7:
                if sd in [4,8,10,14,15,19,22,23,24,27,29,31,32,41,42,46,47,48] or sd in range(34,38):
                    return 1
                else:
                    return 0
            else:
                return 0

    def scan_features(self):
        p = self.features_probability()

    def features_probability(self):
        if self.game.red_odds.position > 1 and self.game.green_odds.position > 1 and self.game.yellow_odds.position > 1:
            m4 = self.check_mixer4()
            if m4 == True:
                self.features_spotting()

    def check_mixer4(self):
        m = self.game.mixer4.position
        g = self.game.green_odds.position
        y = self.game.yellow_odds.position
        r = self.game.red_odds.position

        if g < 4:
            if m not in [0,7,20]:
                return 1
        if g == 4:
            if m in [8,9,11,14,16,17]:
                return 1
        if g == 5:
            if m in [4,6,12,15,18,20]:
                return 1
        if g == 6:
            if m in [2,5,7,13,19]:
                return 1
        if g == 7:
            if m in [10,21,22]:
                return 1
        if g == 8:
            if m == 23:
                return 1
        if y == 4:
            if m in [9,10,12,13,15,16]:
                return 1
        if y == 5:
            if m in [4,5,8,14,18,19]:
                return 1
        if y == 6:
            if m in [1,6,11,17,21]:
                return 1
        if y == 7:
            if m in [7,20,22]:
                return 1
        if y == 8:
            if m == 23:
                return 1
        if r == 4:
            if m in [7,8,12,13,17,18]:
                return 1
        if r == 5:
            if m in [5,6,14,15,21]:
                return 1
        if r == 6:
            if m in [3,4,10,16,20]:
                return 1
        if r == 7:
            if m in [11,19,22]:
                return 1
        if r == 8:
            if m == 23:
                return 1

        return 0

    def check_mixer2(self):
        m2 = self.game.mixer2.position
        ms = self.game.magic_squares_feature.position
        if self.game.selection_feature.position == 9:
            if m2 in [1,10,13,15,17,19,21,23,24] or m2 in range(3,6):
                return 1
        if ms <= 5:
            if m2 in [14,10,12,16,20,7,22] or m2 in range(6,10):
                return 1
            else:
                return 0
        if ms == 6:
            if m2 in [7,22]:
                return 1
            else:
                return 0
        if ms >= 7:
            if m2 in [11,18]:
                return 1
            else:
                return 0

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

    def features_spotting(self):
        sd = self.game.spotting.position
        ms = self.game.magic_squares_feature.position
        if ms <= 2:
            self.step_ms(1)
        if ms == 3:
            if sd in [6,7,12,13,20,21,25,28,32,38,43,46,48,49]:
                self.step_ms(1)
        if sd in [8,19]:
            self.step_ms(9)
        if ms == 4:
            if sd in [24,31]:
                self.step_ms(1)
        if ms == 5:
            if sd in [6,12,20,28,32,43]:
                self.step_ms(1)
        if ms == 6:
            if sd in [0,33]:
                self.step_ms(1)
        if self.game.selection_feature.position < 2:
            self.step_sf(2 - self.game.selection_feature.position)
        if self.game.selection_feature.position in [2,3]:
            if sd in [2,17,30,34,37,39,44,45,47]:
                self.step_sf(1)
        if self.game.selection_feature.position in [4,5]:
            if sd in [5,9,11,16,18,26]:
                self.step_sf(1)
        if self.game.selection_feature.position in [6,7]:
            if sd == 2 or sd == 26:
                self.step_sf(1)
        if self.game.selection_feature.position == 8:
            if sd == 1:
                self.step_sf(1)
        if sd in [4,10]:
            if self.game.corners.status == False:
                self.game.corners.engage(self.game)
                self.game.sound.play('tilt')
        if sd == 8:
            if self.game.ballyhole.status == False:
                self.game.ballyhole.engage(self.game)
                self.game.sound.play('tilt')

    def step_sf(self, number):
        if number >= 1:
            self.game.selection_feature.step()
            if self.game.selection_feature.position in [3,4]:
                self.game.coils.yellowROLamp.enable()
                self.game.coils.redROLamp.disable()
            if self.game.selection_feature.position in [5,6]:
                self.game.coils.redROLamp.enable()
                self.game.coils.yellowROLamp.disable()
            number -= 1
            self.delay(name="display", delay=0.1, handler=graphics.showtime.display, param=self)
            self.delay(name="step_sf", delay=0.1, handler=self.step_sf, param=number)


    def sw_redstar_active(self, sw):
        if self.game.selection_feature.position == 5 or self.game.selection_feature.position == 6:
            self.game.sound.play('tilt')
            self.step_sf(9 - self.game.selection_feature.position)
        self.delay(name="display", delay=0.1, handler=graphics.showtime.display, param=self)

    def sw_yellowstar_active(self, sw):
        if self.game.selection_feature.position == 3 or self.game.selection_feature.position == 4:
            self.game.sound.play('tilt')
            self.step_sf(7 - self.game.selection_feature.position)
        self.delay(name="display", delay=0.1, handler=graphics.showtime.display, param=self)

    def step_ms(self, number):
        if number >= 1:
            self.game.magic_squares_feature.step()
            number -= 1
            if self.game.magic_squares_feature.position == 5:
                if number == 0:
                    number += 1
            self.delay(name="display", delay=0.1, handler=graphics.showtime.display, param=self)
            self.delay(name="step_ms", delay=0.1, handler=self.step_ms, param=number)

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
        self.delay(name="display", delay=0.1, handler=graphics.showtime.display, param=self)

    def animate_squarea(self, args):
        self.game = args[0]
        num = args[1]
        square = args[2]
        if num < 55:
            graphics.showtime.squarea_animation([self, num * -1, square])
            self.cancel_delayed(name="display")
            num = num + 1
            args = [self.game,num,square]
            self.delay(name="squarea_animation", delay=0.005, handler=self.animate_squarea, param=args)
        else:
            self.cancel_delayed(name="squarea_animation")
            self.delay(name="display", delay=0.1, handler=graphics.showtime.display, param=self)

    def animate_squareb(self, args):
        self.game = args[0]
        num = args[1]
        square = args[2]
        if num < 55:
            graphics.showtime.squareb_animation([self, num * -1, square])
            self.cancel_delayed(name="display")
            num = num + 1
            args = [self.game,num,square]
            self.delay(name="squareb_animation", delay=0.005, handler=self.animate_squareb, param=args)
        else:
            self.cancel_delayed(name="squareb_animation")
            self.delay(name="display", delay=0.1, handler=graphics.showtime.display, param=self)

    def animate_squarec(self, args):
        self.game = args[0]
        num = args[1]
        square = args[2]
        if num < 62:
            graphics.showtime.squarec_animation([self, num * -1, square])
            self.cancel_delayed(name="display")
            num = num + 1
            args = [self.game,num,square]
            self.delay(name="squarec_animation", delay=0.005, handler=self.animate_squarec, param=args)
        else:
            self.cancel_delayed(name="squarec_animation")
            self.delay(name="display", delay=0.1, handler=graphics.showtime.display, param=self)

    def animate_squared(self, args):
        self.game = args[0]
        num = args[1]
        square = args[2]
        if num < 60:
            graphics.showtime.squared_animation([self, num * -1, square])
            self.cancel_delayed(name="display")
            num = num + 1
            args = [self.game,num,square]
            self.delay(name="squared_animation", delay=0.005, handler=self.animate_squared, param=args)
        else:
            self.cancel_delayed(name="squared_animation")
            self.delay(name="display", delay=0.1, handler=graphics.showtime.display, param=self)

    def animate_squaree(self, args):
        self.game = args[0]
        num = args[1]
        square = args[2]
        if num < 60:
            graphics.showtime.squaree_animation([self, num * -1, square])
            self.cancel_delayed(name="display")
            num = num + 1
            args = [self.game,num,square]
            self.delay(name="squaree_animation", delay=0.007, handler=self.animate_squaree, param=args)
        else:
            self.cancel_delayed(name="squaree_animation")
            self.delay(name="display", delay=0.1, handler=graphics.showtime.display, param=self)

    def animate_both(self, args):
        start = args[0]
        diff = args[1]
        num = args[2]
        if start + num >= 50:
            start = 0
        if diff >= 0:
            num = num + 1
            graphics.showtime.both_animation([self, start + num])
            self.cancel_delayed(name="display")
            diff = diff - 1
            args = [start,diff,num]
            self.delay(name="both_animation", delay=0.08, handler=self.animate_both, param=args)
        else:
            self.cancel_delayed(name="both_animation")
            self.delay(name="display", delay=0.1, handler=graphics.showtime.display, param=self)
            self.scan_all()

    def animate_eb_scan(self, args):
        start = args[0]
        diff = args[1]
        num = args[2]
        if start + num >= 50:
            start = 0
        if diff >= 0:
            num = num + 1
            graphics.showtime.eb_animation([self, start + num])
            self.cancel_delayed(name="display")
            diff = diff - 1
            args = [start,diff,num]
            self.delay(name="eb_animation", delay=0.08, handler=self.animate_eb_scan, param=args)
        else:
            self.cancel_delayed(name="eb_animation")
            self.delay(name="display", delay=0.1, handler=graphics.showtime.display, param=self)
            self.scan_eb()

    def check_eb_spotting(self):
        sd = self.game.spotting.position
        if sd == 50:
            if self.game.mixer3.position == 24:
                self.step_eb(9 - self.game.extra_ball.position)
        elif sd == 18:
            if self.game.mixer3.position == 23:
                self.step_eb(3 - self.game.extra_ball.position)
        elif sd == 1:
            self.step_eb(3 - self.game.extra_ball.position)
        else:
            if self.game.cu:
                self.game.extra_ball.step()
                self.check_lifter_status()

    def eb_probability(self):
        mix1 = self.game.mixer1.connected_rivet()

        if self.game.reflex.connected_rivet() == 0 and (mix1 in [1,9,15]):
            m2 = self.check_mixer2()
            if m2 == 1:
                self.check_eb_spotting()
        elif self.game.reflex.connected_rivet() == 1 and (mix1 in [2,14,24,1,9,15]):
            m2 = self.check_mixer2()
            if m2 == 1:
                self.check_eb_spotting()
        elif self.game.reflex.connected_rivet() == 2 and (mix1 in [6,13,22,2,14,24,1,9,15]):
            m2 = self.check_mixer2()
            if m2 == 1:
                self.check_eb_spotting()
        else:
            m2 = self.check_mixer2()
            if m2 == 1:
                self.check_eb_spotting()

    def step_eb(self, number):
        if number >= 1:
            self.game.extra_ball.step()
            self.check_lifter_status()
            number -= 1
            self.delay(name="display", delay=0.1, handler=graphics.showtime.display, param=self)
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

class Showtime(procgame.game.BasicGame):
    """ Showtime was made for Bally's 25th anniversary """
    def __init__(self, machine_type):
        super(Showtime, self).__init__(machine_type)
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
        self.red_odds = units.Stepper("red_odds", 8, 'showtime')
        self.yellow_odds = units.Stepper("yellow_odds", 8, 'showtime')
        self.green_odds = units.Stepper("green_odds", 8, 'showtime')

        #Replay Counter
        self.red_replay_counter = units.Stepper("red_replay_counter", 1000)
        self.yellow_replay_counter = units.Stepper("yellow_replay_counter", 1000)
        self.green_replay_counter = units.Stepper("green_replay_counter", 1000)

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

        self.selector = units.Stepper("selector", 1)

        self.square_a = units.Stepper("square_a", 3, "showtime", "continuous")
        self.square_b = units.Stepper("square_b", 3, "showtime", "continuous")
        self.square_c = units.Stepper("square_c", 3, "showtime", "continuous")
        self.square_d = units.Stepper("square_d", 3, "showtime", "continuous")
        self.square_e = units.Stepper("square_e", 3, "showtime", "continuous")

        self.magic_squares_feature = units.Stepper("magic_squares_feature", 9)

        self.selection_feature = units.Stepper("selection_feature", 9)
        self.ballyhole = units.Relay("ballyhole")

        self.replays = 0
        self.returned = False

    def reset(self):
        super(Showtime, self).reset()
        self.logger = logging.getLogger('game')
        self.load_config('bingo.yaml')
        
        main_mode = SinglecardBingo(self)
        self.modes.add(main_mode)
        
game = Showtime(machine_type='pdb')
game.reset()
game.run_loop()
