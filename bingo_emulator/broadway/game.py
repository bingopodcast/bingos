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
from bingo_emulator.graphics.broadway import *

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

        self.delay(name="display", delay=0.1, handler=graphics.broadway.display, param=self)

    def sw_startButton_active(self, sw):
        self.game.eb_play.disengage()
        if self.game.replays > 0 or self.game.switches.freeplay.is_active():
            self.game.sound.stop('add')
            self.game.sound.play('add')
            self.game.tilt.disengage()
            self.regular_play()
            self.scan_all()
            self.delay(name="display", delay=0.1, handler=graphics.broadway.display, param=self)

    def sw_enter_active(self, sw):
        if self.game.switches.left.is_active() and self.game.switches.right.is_active():
            self.game.end_run_loop()
            os.system("/home/nbaldridge/proc/bingo_emulator/start_game.sh broadway")

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
        if self.game.ball_count.position >= 1:
            if self.game.before_fourth.status == True:
                max_ball = 4
            else:
                max_ball = 5
            if self.game.ball_count.position < max_ball:
                if self.game.magic_squares_feature.position >= 5:
                    self.game.square_a.step()
        self.delay(name="display", delay=0.1, handler=graphics.broadway.display, param=self)

    def sw_right_active(self, sw):
        if self.game.ball_count.position >= 1:
            if self.game.before_fourth.status == True:
                max_ball = 4
            else:
                max_ball = 5
            if self.game.ball_count.position < max_ball:
                if self.game.magic_squares_feature.position >= 5:
                    self.game.square_b.step()

        self.delay(name="display", delay=0.1, handler=graphics.broadway.display, param=self)

    def sw_blue_active(self, sw):
        if self.game.ball_count.position >= 1:
            if self.game.before_fourth.status == True:
                max_ball = 4
            else:
                max_ball = 5
            if self.game.ball_count.position < max_ball:
                if self.game.magic_squares_feature.position >= 5:
                    self.game.square_c.step()

        self.delay(name="display", delay=0.1, handler=graphics.broadway.display, param=self)

    def sw_green_active(self, sw):
        if self.game.ball_count.position >= 1:
            if self.game.before_fourth.status == True:
                max_ball = 4
            else:
                max_ball = 5
            if self.game.ball_count.position < max_ball:
                if self.game.magic_squares_feature.position >= 7:
                    self.game.square_d.step()

        self.delay(name="display", delay=0.1, handler=graphics.broadway.display, param=self)


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
            self.game.start.engage(self.game)
            self.game.card1_replay_counter.reset()
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
            self.game.red_line.reset()
            self.game.yellow_line.reset()
            self.game.ball_count.reset()
            self.game.ballyhole.disengage()
            self.game.extra_ball.reset()
            self.game.odds.reset()
            self.game.before_fifth.disengage()
            self.game.before_fourth.engage(self.game)
            self.game.timer.reset()
            self.game.sound.play_music('motor', -1)
            self.regular_play()
        self.delay(name="display", delay=0.1, handler=graphics.broadway.display, param=self)
        self.game.tilt.disengage()

    def magic_squarea_reset(self, number):
        if number != 0:
            self.game.square_a.step()
            self.delay(name="display", delay=0, handler=graphics.broadway.display, param=self)
            number = self.game.square_a.position
            self.delay(name="magic_squarea_reset", delay=0.1, handler=self.magic_squarea_reset, param=number)

    def magic_squareb_reset(self, number):
        if number != 0:
            self.game.square_b.step()
            self.delay(name="display", delay=0, handler=graphics.broadway.display, param=self)
            number = self.game.square_b.position
            self.delay(name="magic_squareb_reset", delay=0.1, handler=self.magic_squareb_reset, param=number)

    def magic_squarec_reset(self, number):
        if number != 0:
            self.game.square_c.step()
            self.delay(name="display", delay=0, handler=graphics.broadway.display, param=self)
            number = self.game.square_c.position
            self.delay(name="magic_squarec_reset", delay=0.1, handler=self.magic_squarec_reset, param=number)

    def magic_squared_reset(self, number):
        if number != 0:
            self.game.square_d.step()
            self.delay(name="display", delay=0, handler=graphics.broadway.display, param=self)
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
        self.delay(name="display", delay=0.1, handler=graphics.broadway.display, param=self)


    # This is really nasty, but it is how we render graphics for each individual hole.
    # numbers are added (or removed from) a list.  In this way, I can re-use the same
    # routine even for games where there are ball return functions like Surf Club.

    def sw_hole1_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(1)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.broadway.display, param=self)

    def sw_hole2_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(2)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.broadway.display, param=self)

    def sw_hole3_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(3)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.broadway.display, param=self)

    def sw_hole4_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(4)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.broadway.display, param=self)

    def sw_hole5_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(5)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.broadway.display, param=self)

    def sw_hole6_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(6)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.broadway.display, param=self)

    def sw_hole7_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(7)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.broadway.display, param=self)

    def sw_hole8_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(8)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.broadway.display, param=self)

    def sw_hole9_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(9)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.broadway.display, param=self)

    def sw_hole10_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(10)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.broadway.display, param=self)

    def sw_hole11_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(11)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.broadway.display, param=self)

    def sw_hole12_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(12)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.broadway.display, param=self)

    def sw_hole13_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(13)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.broadway.display, param=self)

    def sw_hole14_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(14)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.broadway.display, param=self)

    def sw_hole15_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(15)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.broadway.display, param=self)

    def sw_hole16_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(16)
            if self.game.ballyhole.status == True:
                self.step_eb(3 - self.game.extra_ball.position)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.broadway.display, param=self)

    def sw_hole17_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(17)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.broadway.display, param=self)

    def sw_hole18_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(18)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.broadway.display, param=self)

    def sw_hole19_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(19)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.broadway.display, param=self)

    def sw_hole20_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(20)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.broadway.display, param=self)

    def sw_hole21_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(21)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.broadway.display, param=self)

    def sw_hole22_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(22)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.broadway.display, param=self)

    def sw_hole23_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(23)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.broadway.display, param=self)

    def sw_hole24_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(24)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.broadway.display, param=self)

    def sw_hole25_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(25)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.broadway.display, param=self)

    def sw_replayReset_active(self, sw):
        self.game.anti_cheat.disengage()
        self.holes = []
#        self.cancel_delayed(name="blink_title")
        graphics.broadway.display(self)
        self.tilt_actions()
#        self.delay(name="blink_title", delay=1, handler=self.blink_title)
        self.replay_step_down(self.game.replays)

    def tilt_actions(self):
        self.game.start.disengage()
        self.cancel_delayed(name="replay_reset")
        self.cancel_delayed(name="card1_replay_step_up")
        self.cancel_delayed(name="corners_replay_step_up")
        self.game.card1_replay_counter.reset()
        self.game.corners.disengage()
        self.game.start.engage(self.game)
        self.game.selector.reset()
        self.game.ball_count.reset()
        self.game.extra_ball.reset()
        self.game.odds.reset()
        self.game.eb_play.disengage()
        self.game.search_index.disengage()
        self.game.magic_squares_feature.reset()
        self.game.red_line.reset()
        self.game.yellow_line.reset()
        self.game.ballyhole.disengage()
        self.game.before_fifth.disengage()
        self.game.before_fourth.disengage()
        if self.game.ball_count.position == 0:
            if self.game.switches.shutter.is_active():
                self.game.coils.shutter.enable()
        self.holes = []
        self.game.anti_cheat.engage(game)
        self.game.tilt.engage(self.game)
        self.game.sound.stop_music()
        self.game.sound.play('tilt')
        # displays "Tilt" on the backglass, you have to recoin.
        self.delay(name="display", delay=0.1, handler=graphics.broadway.display, param=self)

    def sw_tilt_active(self, sw):
        if self.game.tilt.status == False:
            self.tilt_actions()

    def replay_step_down(self, number=0):
        if number > 0:
            if number > 1:
                self.game.replays -= 1
                graphics.replay_step_down(self.game.replays, graphics.broadway.reel1, graphics.broadway.reel10, graphics.broadway.reel100)
                self.game.coils.registerDown.pulse()
                number -= 1
                graphics.broadway.display(self)
                self.delay(name="replay_reset", delay=0.0, handler=self.replay_step_down, param=number)
            elif number == 1:
                self.game.replays -= 1
                graphics.replay_step_down(self.game.replays, graphics.broadway.reel1, graphics.broadway.reel10, graphics.broadway.reel100)
                self.game.coils.registerDown.pulse()
                number -= 1
                graphics.broadway.display(self)
                self.cancel_delayed(name="replay_reset")
        else: 
            if self.game.replays > 0:
                self.game.replays -= 1
                graphics.replay_step_down(self.game.replays, graphics.broadway.reel1, graphics.broadway.reel10, graphics.broadway.reel100)
                self.delay(name="display", delay=0.1, handler=graphics.broadway.display, param=self)
            self.game.coils.registerDown.pulse()

    def replay_step_up(self):
        if self.game.replays < 899:
            self.game.replays += 1
            graphics.replay_step_up(self.game.replays, graphics.broadway.reel1, graphics.broadway.reel10, graphics.broadway.reel100)
        self.game.coils.registerUp.pulse()
        self.game.reflex.increase()
        graphics.broadway.display(self)

    def sw_yellow_active(self, sw):
        if self.game.ball_count.position >= 5:
            if self.game.eb_play.status == False:
                self.game.spotting.spin()
                self.game.mixer1.spin()
                self.game.mixer2.spin()
                self.game.mixer3.spin()
                self.game.mixer4.spin()
                self.game.eb_play.engage(self.game)
                self.delay(name="display", delay=0.1, handler=graphics.broadway.display, param=self)
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
                self.delay(name="display", delay=0.1, handler=graphics.broadway.display, param=self)
            
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
            self.yellow = self.r[3]
            self.red = self.r[4]

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
                                self.find_winner(s, self.card, self.corners, self.yellow, self.red)
                                break
#        self.delay(name="blink_title", delay=3, handler=self.blink_title)

    def find_winner(self, relays, card, corners, yellow, red):
        if self.game.search_index.status == False and self.game.replays < 899:
            if self.game.odds.position == 1:
                threeodds = 4
                fourodds = 16
                fiveodds = 64
            elif self.game.odds.position == 2:
                threeodds = 6
                fourodds = 18
                fiveodds = 72
            elif self.game.odds.position == 3:
                threeodds = 8
                fourodds = 24
                fiveodds = 96
            elif self.game.odds.position == 4:
                threeodds = 12
                fourodds = 36
                fiveodds = 96
            elif self.game.odds.position == 5:
                threeodds = 18
                fourodds = 48
                fiveodds = 96
            elif self.game.odds.position == 6:
                threeodds = 24
                fourodds = 72
                fiveodds = 144
            elif self.game.odds.position == 7:
                threeodds = 36
                fourodds = 96
                fiveodds = 144
            elif self.game.odds.position == 8:
                threeodds = 48
                fourodds = 144
                fiveodds = 192

            if relays == 3:
                if not corners:
                    if red:
                        if self.game.red_line.position >= 5 and self.game.red_line.position < 10:
                            if self.game.card1_replay_counter.position < threeodds * 2:
                                self.game.search_index.engage(self.game)
                                self.card1_replay_step_up(threeodds * 2 - self.game.card1_replay_counter.position)
                        elif self.game.red_line.position == 10:
                            if self.game.card1_replay_counter.position < threeodds * 3:
                                self.game.search_index.engage(self.game)
                                self.card1_replay_step_up(threeodds * 3 - self.game.card1_replay_counter.position)
                        else:
                            if self.game.card1_replay_counter.position < threeodds:
                                self.game.search_index.engage(self.game)
                                self.card1_replay_step_up(threeodds - self.game.card1_replay_counter.position)
                    elif yellow:
                        if self.game.yellow_line.position >= 5 and self.game.yellow_line.position < 10:
                            if self.game.card1_replay_counter.position < threeodds * 2:
                                self.game.search_index.engage(self.game)
                                self.card1_replay_step_up(threeodds * 2 - self.game.card1_replay_counter.position)
                        elif self.game.yellow_line.position == 10:
                            if self.game.card1_replay_counter.position < threeodds * 3:
                                self.game.search_index.engage(self.game)
                                self.card1_replay_step_up(threeodds * 3 - self.game.card1_replay_counter.position)
                        else:
                            if self.game.card1_replay_counter.position < threeodds:
                                self.game.search_index.engage(self.game)
                                self.card1_replay_step_up(threeodds - self.game.card1_replay_counter.position)
                    else:
                        if self.game.card1_replay_counter.position < threeodds:
                            self.game.search_index.engage(self.game)
                            self.card1_replay_step_up(threeodds - self.game.card1_replay_counter.position)
            if relays == 4:
                if corners and self.game.corners.status == True:
                    if self.game.corners.status == True:
                        if self.game.card1_replay_counter.position < fiveodds:
                            self.game.search_index.engage(self.game)
                            self.card1_replay_step_up(fiveodds - self.game.card1_replay_counter.position)
                else:
                    if not corners:
                        if red:
                            if self.game.red_line.position >= 5 and self.game.red_line.position < 10:
                                if self.game.card1_replay_counter.position < fourodds * 2:
                                    self.game.search_index.engage(self.game)
                                    self.card1_replay_step_up(fourodds * 2 - self.game.card1_replay_counter.position)
                            elif self.game.red_line.position == 10:
                                if self.game.card1_replay_counter.position < fourodds * 3:
                                    self.game.search_index.engage(self.game)
                                    self.card1_replay_step_up(fourodds * 3 - self.game.card1_replay_counter.position)
                            else:
                                if self.game.card1_replay_counter.position < fourodds:
                                    self.game.search_index.engage(self.game)
                                    self.card1_replay_step_up(fourodds - self.game.card1_replay_counter.position)
                        elif yellow:
                            if self.game.yellow_line.position >= 5 and self.game.yellow_line.position < 10:
                                if self.game.card1_replay_counter.position < fourodds * 2:
                                    self.game.search_index.engage(self.game)
                                    self.card1_replay_step_up(fourodds * 2 - self.game.card1_replay_counter.position)
                            elif self.game.yellow_line.position == 10:
                                if self.game.card1_replay_counter.position < fourodds * 3:
                                    self.game.search_index.engage(self.game)
                                    self.card1_replay_step_up(fourodds * 3 - self.game.card1_replay_counter.position)
                            else:
                                if self.game.card1_replay_counter.position < fourodds:
                                    self.game.search_index.engage(self.game)
                                    self.card1_replay_step_up(fourodds - self.game.card1_replay_counter.position)
                        else:
                            if self.game.card1_replay_counter.position < fourodds:
                                self.game.search_index.engage(self.game)
                                self.card1_replay_step_up(fourodds - self.game.card1_replay_counter.position)
            if relays == 5:
                if red:
                    if self.game.red_line.position >= 5 and self.game.red_line.position < 10:
                        if self.game.card1_replay_counter.position < fiveodds * 2:
                            self.game.search_index.engage(self.game)
                            self.card1_replay_step_up(fiveodds * 2 - self.game.card1_replay_counter.position)
                    elif self.game.red_line.position == 10:
                        if self.game.card1_replay_counter.position < fiveodds * 3:
                            self.game.search_index.engage(self.game)
                            self.card1_replay_step_up(fiveodds * 3 - self.game.card1_replay_counter.position)
                    else:
                        if self.game.card1_replay_counter.position < fiveodds:
                            self.game.search_index.engage(self.game)
                            self.card1_replay_step_up(fiveodds - self.game.card1_replay_counter.position)
                elif yellow:
                    if self.game.yellow_line.position >= 5 and self.game.yellow_line.position < 10:
                        if self.game.card1_replay_counter.position < fiveodds * 2:
                            self.game.search_index.engage(self.game)
                            self.card1_replay_step_up(fiveodds * 2 - self.game.card1_replay_counter.position)
                    elif self.game.yellow_line.position == 10:
                        if self.game.card1_replay_counter.position < fiveodds * 3:
                            self.game.search_index.engage(self.game)
                            self.card1_replay_step_up(fiveodds * 3 - self.game.card1_replay_counter.position)
                    else:
                        if self.game.card1_replay_counter.position < fiveodds:
                            self.game.search_index.engage(self.game)
                            self.card1_replay_step_up(fiveodds - self.game.card1_replay_counter.position)
                else:
                    if self.game.card1_replay_counter.position < fiveodds:
                        self.game.search_index.engage(self.game)
                        self.card1_replay_step_up(fiveodds - self.game.card1_replay_counter.position)

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

    def closed_search_relays(self, rivets, c):
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
        self.pos[14] = {self.p1:1, self.p5:2, self.t1:3, self.t5:4}
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

        if rivets in range(0, 13):
            card = 1
        if rivets == 14:
            corners = True
        if rivets == 1:
            red = True
        if rivets == 2:
            yellow = True
        if rivets == 4:
            red = True
        if rivets == 5:
            yellow = True

        if rivets == 9:
            yellow = True
        if rivets == 10:
            red = True

        return (self.pos[rivets], card, corners, yellow, red)
    
    def scan_all(self):
        #Animate scanning of everything - this happens through the spotting disc
        self.all_probability()

    def all_probability(self):
        if self.game.odds.position < 3:
            self.game.odds.step()
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
        if self.game.odds.position < 3:
            return
        s = random.randint(1,5)
        self.animate_odds_scan(s)
        p = self.odds_probability()
        if p == 1:
            es = self.check_extra_step()
            if es == 1:
                i = random.randint(1,5)
                self.extra_step(i)
            else:
                self.game.odds.step()

    def extra_step(self, number):
        if number > 0:
            self.game.odds.step()
            self.game.coils.counter.pulse()
            self.delay(name="display", delay=0, handler=graphics.broadway.display, param=self)
            number -= 1
            self.delay(name="extra_step", delay=0.1, handler=self.extra_step, param=number)

    def check_extra_step(self):
        i = random.randint(0,32)
        if i == 16:
            return 1
        else:
            return 0

    def odds_probability(self):
        # Check position of Mixer 2, extra scoring relays and current 
        # position of the odds, along with trip relays.
        # For first check, guaranteed single stepup.  Probability doesn't 
        # factor, so I will return as part of the initial check above.
        if self.game.odds.position == 1:
            return 1
        else:
            sd = self.game.spotting.position
            if self.game.odds.position == 2:
                if sd == 0 or sd == 2 or sd == 3 or sd == 6 or sd in range(7,10) or sd == 11 or sd == 13 or sd in range(15,19) or sd == 21 or sd == 23 or sd == 25 or sd in range(30,33) or sd == 36 or sd == 37 or sd == 39 or sd == 40 or sd == 42 or sd == 45 or sd == 47 or sd == 50:
                    return 1
                else:
                    return 0
            elif self.game.odds.position == 3:
                if sd == 0 or sd == 2 or sd == 3 or sd in range(8,11) or sd == 14 or sd in range(16,19) or sd == 21 or sd == 23 or sd in range(30,33) or sd in range(37,40) or sd == 41 or sd == 45 or sd == 46 or sd == 49:
                    return 1
                else:
                    return 0
            elif self.game.odds.position == 4:
                if sd == 35:
                    return 1
                else:
                    return 0
            elif self.game.odds.position == 5:
                if sd == 0 or sd == 3 or sd == 8 or sd == 10 or sd == 16 or sd == 18 or sd == 21 or sd == 37 or sd == 39 or sd == 45:
                    return 1
                else:
                    return 0
            elif self.game.odds.position == 6:
                if sd == 4:
                    return 1
                else:
                    return 0
            elif self.game.odds.position == 7:
                if sd == 4:
                    return 1
                else:
                    return 0
            else:
                return 0

    def scan_features(self):
        p = self.features_probability()

    def features_probability(self):
        s = random.randint(1,6)
        self.animate_feature_scan(s)
        mix2 = self.game.mixer2.position

        if self.game.odds.position > 1:
            m3 = self.check_mixer3()
            if m3 == True:
                m2 = self.check_mixer2()
                if m2 == True:
                    m4 = self.check_mixer4()
                    if m4 == True:
                        self.features_spotting()

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

    def check_mixer3(self):
        mix3 = self.game.mixer3.position
        if self.game.cu:
            if mix3 == 3 or mix3 == 5 or mix3 == 7 or mix3 == 10 or mix3 == 12:
                return 1
            else:
                return 0 
        elif mix3 != 22 or mix3 != 20 or mix3 != 17:
            if self.game.red_line.position < 10:
                return 1
            elif self.game.yellow_line.position < 10:
                return 1
            else:
                return 0
        else:
            return 0


    def features_spotting(self):
        sd = self.game.spotting.position
        if sd == 13:
            self.step_red_line(10)
        elif sd == 10:
            self.step_red_line(5 - self.game.red_line.position)
        elif sd == 46:
            self.step_red_line(5 - self.game.red_line.position)
        elif sd == 1:
            if self.game.cu:
                if self.game.red_line.position < 5:
                    self.step_red_line(4 - self.game.red_line.position)
                else:
                    self.step_red_line(9 - self.game.red_line.position)
        else:
            if self.game.cu:
                self.game.red_line.step()
        if sd == 5:
            self.step_yellow_line(10)
        elif sd == 38:
            self.step_yellow_line(5 - self.game.yellow_line.position)
        elif sd == 9:
            self.step_yellow_line(5 - self.game.yellow_line.position)
        elif sd == 1:
            if self.game.cu:
                if self.game.yellow_line.position < 5:
                    self.step_yellow_line(4 - self.game.yellow_line.position)
                else:
                    self.step_yellow_line(9 - self.game.yellow_line.position)
        else:
            if self.game.cu:
                self.game.yellow_line.step()
        if sd == 3:
            if self.game.reflex.connected_rivet() == 4 or self.game.reflex.connected_rivet() == 3:
                self.step_ms(7 - self.game.magic_squares_feature.position)
        if sd == 4:
            self.step_ms(4 - self.game.magic_squares_feature.position)
        elif sd == 15:
            self.step_ms(5 - self.game.magic_squares_feature.position)
        elif sd == 7:
            self.step_ms(7 - self.game.magic_squares_feature.position)
        else:
            self.step_ms(1)
        if sd == 3:
            self.game.corners.engage(self.game)
        if sd == 0 or sd == 39:
            self.game.ballyhole.engage(self.game)
        if sd == 26 or sd == 43:
            self.game.before_fourth.disengage()
            self.game.before_fifth.engage(self.game)

    def step_ms(self, number):
        if number >= 1:
            self.game.magic_squares_feature.step()
            if self.game.magic_squares_feature.position == 6:
                m2 = self.game.mixer2.position
                if m2 == 4 or m2 == 6 or m2 == 10 or m2 == 12 or m2 == 15 or m2 == 17 or m2 == 19 or m2 == 21 or m2 == 23:
                    self.holes.append(18)
                else:
                    self.holes.append(2)
            number -= 1
            self.delay(name="display", delay=0.1, handler=graphics.broadway.display, param=self)
            self.delay(name="step_ms", delay=0.1, handler=self.step_ms, param=number)

    def step_red_line(self, number):
        if number >= 1:
            self.game.red_line.step()
            number -= 1
            self.delay(name="display", delay=0.1, handler=graphics.broadway.display, param=self)
            self.delay(name="step_red_line", delay=0.1, handler=self.step_red_line, param=number)

    def step_yellow_line(self, number):
        if number >= 1:
            self.game.yellow_line.step()
            number -= 1
            self.delay(name="display", delay=0.1, handler=graphics.broadway.display, param=self)
            self.delay(name="step_yellow_line", delay=0.1, handler=self.step_yellow_line, param=number)

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
        self.delay(name="display", delay=0.1, handler=graphics.broadway.display, param=self)

    def animate_odds_scan(self, s):
        if s > 1:
            self.delay(name="odds_animation", delay=0, handler=graphics.broadway.odds_animation, param=s)
            self.delay(name="display", delay=0.1, handler=graphics.broadway.display, param=self)
            s -= 1
            #self.delay(name="animate_odds", delay=0.1, handler=self.animate_odds_scan, param=s)
        else:
            self.delay(name="display", delay=0.1, handler=graphics.broadway.display, param=self)

    def animate_feature_scan(self, s):
        if s > 1:
            self.delay(name="feature_animation", delay=0.1, handler=graphics.broadway.feature_animation, param=s)
            self.delay(name="display", delay=0.1, handler=graphics.broadway.display, param=self)
            s -= 1
            #self.delay(name="animate_feature", delay=0.1, handler=self.animate_feature_scan, param=s)
        else:
            self.delay(name="display", delay=0.1, handler=graphics.broadway.display, param=self)

    def animate_eb_scan(self, s):
        if s > 1:
            self.delay(name="eb_animation", delay=0.1, handler=graphics.broadway.eb_animation, param=s)
            self.delay(name="display", delay=0.1, handler=graphics.broadway.display, param=self)
            s -= 1
            #self.delay(name="animate_eb", delay=0.1, handler=self.animate_eb_scan, param=s)
        else:
            self.delay(name="display", delay=0.1, handler=graphics.broadway.display, param=self)

    def check_eb_spotting(self):
        sd = self.game.spotting.position
        if sd == 50:
            if self.game.mixer3.position == 24:
                self.step_eb(9 - self.game.extra_ball.position)
        elif sd == 2:
            self.step_eb(3 - self.game.extra_ball.position)
        elif sd == 10:
            if self.game.mixer2.position == 18 or self.game.mixer2.position == 6 or self.game.mixer.position == 12 or self.game.mixer2.position == 22:
                if self.game.extra_ball.position < 6:
                    self.step_eb(6 - self.game.extra_ball.position)
                else:
                    self.step_eb(9 - self.game.extra_ball.position)
        else:
            self.game.extra_ball.step()

    def eb_probability(self):
        #Used Surf Club's mixers - wrong, but lacking documentation.
        mix1 = self.game.mixer1.connected_rivet()

        if self.game.reflex.connected_rivet() == 0 and (mix1 == 1 or mix1 == 9 or mix1 == 15):
            m3 = self.check_mixer3()
            if m3 == 1:
                self.check_eb_spotting()
        elif self.game.reflex.connected_rivet() == 1 and (mix1 == 2 or mix1 == 14 or mix1 == 24 or mix1 == 1 or mix1 == 9 or mix1 == 15):
            m3 = self.check_mixer3()
            if m3 == 1:
                self.check_eb_spotting()
        elif self.game.reflex.connected_rivet() == 2 and (mix1 == 6 or mix1 == 13 or mix1 == 22 or mix1 == 2 or mix1 == 14 or mix1 == 24 or mix1 == 1 or mix1 == 9 or mix1 == 15):
            m3 = self.check_mixer3()
            if m3 == 1:
                self.check_eb_spotting()
        else:
            m3 = self.check_mixer3()
            if m3 == 1:
                self.check_eb_spotting()

    def step_eb(self, number):
        if number >= 1:
            self.game.extra_ball.step()
            self.check_lifter_status()
            number -= 1
            self.delay(name="display", delay=0.1, handler=graphics.broadway.display, param=self)
            self.delay(name="step_eb", delay=0.1, handler=self.step_eb, param=number)

    def blink_title(self):
        title1 = random.randint(0,1)
        title2 = random.randint(0,1)
        title3 = random.randint(0,1)
        title4 = random.randint(0,1)
        if title1 == 1:
            pos = [167,257]
            image = pygame.image.load('broadway/assets/title1_on.png').convert_alpha()
            screen.blit(image, pos)
        if title2 == 1:
            pos = [241,290]
            image = pygame.image.load('broadway/assets/title2_on.png').convert_alpha()
            screen.blit(image, pos)
        if title3 == 1:
            pos = [346,298]
            image = pygame.image.load('broadway/assets/title3_on.png').convert_alpha()
            screen.blit(image, pos)
        if title4 == 1:
            pos = [431,264]
            image = pygame.image.load('broadway/assets/title4_on.png').convert_alpha()
            screen.blit(image, pos)
            
        pygame.display.update()
        self.delay(name="display", delay=0.1, handler=graphics.broadway.display, param=self)
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


class Broadway(procgame.game.BasicGame):
    """ Palm Beach was the first game with Super Cards """
    def __init__(self, machine_type):
        super(Broadway, self).__init__(machine_type)
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
        self.odds = units.Stepper("odds", 8, 'broadway')

        #Replay Counter
        self.card1_replay_counter = units.Stepper("card1_replay_counter", 500)

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

        self.selector = units.Stepper("selector", 1)

        self.yellow_line = units.Stepper("yellow_line", 10)
        self.red_line = units.Stepper("red_line", 10)

        self.square_a = units.Stepper("square_a", 3, "broadway", "continuous")
        self.square_b = units.Stepper("square_b", 3, "broadway", "continuous")
        self.square_c = units.Stepper("square_c", 3, "broadway", "continuous")
        self.square_d = units.Stepper("square_d", 3, "broadway", "continuous")

        self.magic_squares_feature = units.Stepper("magic_squares_feature", 7)

        self.before_fourth = units.Relay("before_fourth")
        self.before_fifth = units.Relay("before_fifth")

        self.ballyhole = units.Relay("ballyhole")

        self.replays = 0
        self.returned = False

    def reset(self):
        super(Broadway, self).reset()
        self.logger = logging.getLogger('game')
        self.load_config('bingo.yaml')
        
        main_mode = SinglecardBingo(self)
        self.modes.add(main_mode)
        
game = Broadway(machine_type='pdb')
game.reset()
game.run_loop()
