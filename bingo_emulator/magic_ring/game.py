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
from bingo_emulator.graphics.magic_ring import *

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
                self.game.sound.stop('add')
                self.game.sound.play('add')
                self.game.cu = not self.game.cu
                self.game.spotting.spin()
                self.game.mixer1.spin()
                self.game.mixer2.spin()
                self.game.mixer3.spin()
                self.regular_play()
                self.game.odds_only.disengage()
                self.game.features.disengage()
                self.scan_all()
            elif self.game.features.status == True:
                self.game.sound.stop('add')
                self.game.sound.play('add')
                self.game.cu = not self.game.cu
                self.game.spotting.spin()
                self.game.mixer1.spin()
                self.game.mixer2.spin()
                self.game.mixer3.spin()
                self.regular_play()
                self.game.odds_only.disengage()
                self.game.all_advantages.disengage()
                self.scan_features()
            elif self.game.odds_only.status == True:
                self.game.sound.stop('add')
                self.game.sound.play('add')
                self.game.cu = not self.game.cu
                self.game.spotting.spin()
                self.game.mixer1.spin()
                self.game.mixer2.spin()
                self.game.mixer3.spin()
                self.regular_play()
                self.game.features.disengage()
                self.game.all_advantages.disengage()
                self.scan_odds()
            elif self.game.special.status == True:
                self.game.sound.stop('add')
                self.game.sound.play('add')
                self.game.cu = not self.game.cu
                self.game.spotting.spin()
                self.game.mixer1.spin()
                self.game.mixer2.spin()
                self.game.mixer3.spin()
                self.regular_play()
                self.scan_special()
                self.game.features.disengage()
                self.game.all_advantages.disengage()
                self.game.odds_only.disengage()
        else:
            self.game.sound.stop('add')
            self.game.sound.play('add')
            self.game.cu = not self.game.cu
            self.game.spotting.spin()
            self.game.mixer1.spin()
            self.game.mixer2.spin()
            self.game.mixer3.spin()
            self.regular_play()
            self.game.all_advantages.engage(self.game)
            self.game.odds_only.disengage()
            self.game.features.disengage()
            self.game.special.disengage()
            self.scan_all()
        self.delay(name="display", delay=0.1, handler=graphics.magic_ring.display, param=self)

    

    def sw_startButton_active(self, sw):
        self.game.odds_only.disengage()
        self.game.special.disengage()
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
            self.game.tilt.disengage()
            self.regular_play()
            self.scan_all()
        self.delay(name="display", delay=0.1, handler=graphics.magic_ring.display, param=self)

    def sw_blue_active(self, sw):
        if self.game.start.status == True:
            self.game.features.disengage()
            self.game.special.disengage()
            self.game.all_advantages.disengage()
            self.game.odds_only.engage(self.game)
        if self.game.replays > 0 or self.game.switches.freeplay.is_active():
            self.game.sound.stop('add')
            self.game.sound.play('add')
            self.game.odds_only.engage(self.game)
            self.delay(name="display", delay=0.1, handler=graphics.magic_ring.display, param=self)
            self.regular_play()
            self.scan_odds()
            self.delay(name="display", delay=0.1, handler=graphics.magic_ring.display, param=self)
        self.delay(name="display", delay=0.1, handler=graphics.magic_ring.display, param=self)

    def sw_green_active(self, sw):
        if self.game.start.status == True:
            self.game.features.engage(self.game)
            self.game.special.disengage()
            self.game.all_advantages.disengage()
            self.game.odds_only.disengage()

        if self.game.replays > 0 or self.game.switches.freeplay.is_active():
            if self.game.start.status == False:
                self.delay(name="startup", delay=0.1, handler=self.sw_startButton_active, param=sw)
            else:
                self.game.sound.stop('add')
                self.game.sound.play('add')
                self.game.features.engage(self.game)
                self.delay(name="display", delay=0.1, handler=graphics.magic_ring.display, param=self)
                self.regular_play()
                self.scan_features()
                self.delay(name="display", delay=0.1, handler=graphics.magic_ring.display, param=self)
        self.delay(name="display", delay=0.1, handler=graphics.magic_ring.display, param=self)


    def sw_enter_active(self, sw):
        if self.game.switches.left.is_active() and self.game.switches.right.is_active():
            self.game.end_run_loop()
            os.system("/home/nbaldridge/proc/bingo_emulator/start_game.sh magic_ring")
        else:
            if self.game.ball_count.position >= 4:
                self.game.sound.stop_music()
                self.game.sound.play_music('motor', -1)
                self.game.timer.reset()
                if self.game.search_index.status == False:
                    self.game.sound.play('search')
                    self.search(1)
                    self.find_stars()
                self.delay(name="display", delay=0.1, handler=graphics.magic_ring.display, param=self)


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
                        self.game.ring.step()
                #B
                elif self.game.wheel.position in [3,4]:
                    if rp < 8:
                        self.game.ring.step()
                #C
                elif self.game.wheel.position in [5,6]:
                    if rp < 13:
                        self.game.ring.step()
                #D
                elif self.game.wheel.position in [7,8]:
                    if rp < 17:
                        self.game.ring.step()
                #E
                else:
                    self.game.ring.step()
            
            self.search()
                            
            self.delay(name="display", delay=0.1, handler=graphics.magic_ring.display, param=self)

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
                        self.game.ring.stepdown()
                else:
                    self.game.ring.stepdown()
            
            self.search()
                            
            self.delay(name="display", delay=0.1, handler=graphics.magic_ring.display, param=self)

    def check_selection(self):
        if self.game.selection_feature.position == 9:
            self.game.red_star.disengage()
            self.game.yellow_star.disengage()
            self.game.coils.yellowROLamp.disable()
            self.game.coils.redROLamp.disable()
        self.delay(name="display", delay=0.1, handler=graphics.magic_ring.display, param=self)

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
        # Need to add a method to handle double or nothing game.  Treat it like a Red Letter win, as guaranteed odds will appear on the BG.  Otherwise, acts like a regular game, but only 3 balls.

        self.cancel_delayed(name="search")
        self.cancel_delayed(name="red_replay_step_up")
        self.cancel_delayed(name="yellow_replay_step_up")
        self.cancel_delayed(name="green_replay_step_up")
        self.cancel_delayed(name="stars_replay_step_up")
        self.cancel_delayed(name="blink")
        self.cancel_delayed(name="blink_double")
        self.cancel_delayed(name="timeout")

        self.game.search_index.disengage()
        self.game.coils.counter.pulse()
        self.game.sound.play_music('motor', -1)

        self.game.cu = not self.game.cu
        self.game.spotting.spin()
        self.game.mixer1.spin()
        self.game.mixer2.spin()
        self.game.mixer3.spin()
        self.game.reflex.decrease()
        if self.game.ring.position != 0:
            self.reset_ring()

        self.game.returned = False
        if self.game.start.status == True:
            if self.game.selector.position < 1:
                self.game.selector.step()
            if self.game.switches.shutter.is_inactive():
                self.game.coils.shutter.enable()
            self.replay_step_down()
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
            self.game.red_odds.reset()
            self.game.green_odds.reset()
            self.game.yellow_odds.reset()
            self.game.yellow_star.disengage()
            self.game.double_colors.reset()
            self.game.double.disengage()
            self.game.six_stars.disengage()
            self.game.three_stars.disengage()
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
            self.game.red_replay_counter.reset()
            self.game.yellow_replay_counter.reset()
            self.game.green_replay_counter.reset()
            self.game.selector.reset()
            self.game.ball_count.reset()
            self.game.timer.reset()
            self.game.red_winner_amount = 0
            self.game.yellow_winner_amount = 0
            self.game.green_winner_amount = 0
            self.game.sound.play_music('motor', -1)
            self.regular_play()
        self.delay(name="display", delay=0.1, handler=graphics.magic_ring.display, param=self)
        self.game.tilt.disengage()

    def reset_ring(self):
        if self.game.ring.position != 0:
            self.game.ring.step()
            self.delay(name="ring_step", delay=0.1, handler=self.reset_ring)
            self.delay(name="display", delay=0.1, handler=graphics.magic_ring.display, param=self)


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
        if self.game.ball_count.position >= 5:
            self.game.coils.yellowROLamp.disable()
            self.game.coils.redROLamp.disable()
            self.search()
        if self.game.double.status == False and self.game.ball_count.position < 5:
            self.check_lifter_status()
        elif self.game.double.status == True and self.game.ball_count.position < 3:
            self.check_lifter_status()
        elif self.game.double_double.status == True and self.game.ball_count.position < 3:
            self.check_lifter_status()
        self.delay(name="display", delay=0.1, handler=graphics.magic_ring.display, param=self)


    # This is really nasty, but it is how we render graphics for each individual hole.
    # numbers are added (or removed from) a list.  In this way, I can re-use the same
    # routine even for games where there are ball return functions like Surf Club.

    def sw_hole1_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(1)
            self.delay(name="display", delay=0.1, handler=graphics.magic_ring.display, param=self)

    def sw_hole2_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(2)
            self.delay(name="display", delay=0.1, handler=graphics.magic_ring.display, param=self)

    def sw_hole3_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(3)
            self.delay(name="display", delay=0.1, handler=graphics.magic_ring.display, param=self)

    def sw_hole4_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(4)
            self.delay(name="display", delay=0.1, handler=graphics.magic_ring.display, param=self)

    def sw_hole5_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(5)
            self.delay(name="display", delay=0.1, handler=graphics.magic_ring.display, param=self)

    def sw_hole6_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(6)
            self.delay(name="display", delay=0.1, handler=graphics.magic_ring.display, param=self)

    def sw_hole7_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(7)
            self.delay(name="display", delay=0.1, handler=graphics.magic_ring.display, param=self)

    def sw_hole8_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(8)
            self.delay(name="display", delay=0.1, handler=graphics.magic_ring.display, param=self)

    def sw_hole9_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(9)
            self.delay(name="display", delay=0.1, handler=graphics.magic_ring.display, param=self)

    def sw_hole10_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(10)
            self.delay(name="display", delay=0.1, handler=graphics.magic_ring.display, param=self)

    def sw_hole11_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(11)
            self.delay(name="display", delay=0.1, handler=graphics.magic_ring.display, param=self)

    def sw_hole12_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(12)
            self.delay(name="display", delay=0.1, handler=graphics.magic_ring.display, param=self)

    def sw_hole13_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(13)
            self.delay(name="display", delay=0.1, handler=graphics.magic_ring.display, param=self)

    def sw_hole14_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(14)
            self.delay(name="display", delay=0.1, handler=graphics.magic_ring.display, param=self)

    def sw_hole15_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(15)
            self.delay(name="display", delay=0.1, handler=graphics.magic_ring.display, param=self)

    def sw_hole16_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(16)
            self.delay(name="display", delay=0.1, handler=graphics.magic_ring.display, param=self)

    def sw_hole17_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(17)
            self.delay(name="display", delay=0.1, handler=graphics.magic_ring.display, param=self)

    def sw_hole18_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(18)
            self.delay(name="display", delay=0.1, handler=graphics.magic_ring.display, param=self)

    def sw_hole19_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(19)
            self.delay(name="display", delay=0.1, handler=graphics.magic_ring.display, param=self)

    def sw_hole20_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(20)
            self.delay(name="display", delay=0.1, handler=graphics.magic_ring.display, param=self)

    def sw_replayReset_active(self, sw):
        self.game.anti_cheat.disengage()
        self.holes = []
        graphics.magic_ring.display(self)
        self.tilt_actions()
        self.replay_step_down(self.game.replays)

    def sw_redstar_active(self, sw):
        if self.game.red_star.status == True:
            if self.game.selection_feature.position < 9:
                self.game.selection_feature.step()
                self.game.coils.yellowROLamp.disable()
            self.delay(name="display", delay=0.1, handler=graphics.magic_ring.display, param=self)

    def sw_yellowstar_active(self, sw):
        if self.game.yellow_star.status == True:
            if self.game.selection_feature.position < 9:
                self.game.selection_feature.step()
                self.game.yellow_star.disengage()
                self.game.coils.redROLamp.disable()
            self.delay(name="display", delay=0.1, handler=graphics.magic_ring.display, param=self)

    def tilt_actions(self):
        self.game.start.disengage()
        self.cancel_delayed(name="replay_reset")
        self.cancel_delayed(name="red_replay_step_up")
        self.cancel_delayed(name="yellow_replay_step_up")
        self.cancel_delayed(name="green_replay_step_up")
        self.cancel_delayed(name="stars_replay_step_up")
        self.cancel_delayed(name="blink")
        self.cancel_delayed(name="blink_double")
        self.cancel_delayed(name="timeout")
        self.game.coils.redROLamp.disable()
        self.game.coils.yellowROLamp.disable()
        self.game.search_index.disengage()
        if self.game.ball_count.position == 0:
            if self.game.switches.shutter.is_active():
                self.game.coils.shutter.enable()
        self.holes = []
        self.game.red_odds.reset()
        self.game.yellow_odds.reset()
        self.game.green_odds.reset()
        self.game.start.engage(self.game)
        self.game.ball_count.reset()
        self.game.selection_feature.reset()
        self.game.three_stars.disengage()
        self.game.six_stars.disengage()
        self.game.timer.reset()
        self.game.wheel.reset()
        self.game.double_up.disengage()
        self.game.double_colors.reset()
        self.game.double.disengage()
        self.game.double_double.disengage()
        self.game.red_replay_counter.reset()
        self.game.yellow_replay_counter.reset()
        self.game.green_replay_counter.reset()
        self.game.yellow_star.disengage()
        self.game.red_star.disengage()
        self.game.selector.reset()
        self.game.ball_count.reset()
        self.game.selection_feature.reset()
        self.game.anti_cheat.engage(game)
        self.game.tilt.engage(self.game)
        self.game.sound.stop_music()
        self.game.sound.play('tilt')
        # displays "Tilt" on the backglass, you have to recoin.
        self.delay(name="display", delay=0.1, handler=graphics.magic_ring.display, param=self)

    def sw_tilt_active(self, sw):
        if self.game.tilt.status == False:
            self.tilt_actions()

    def replay_step_down(self, number=0):
        if number > 0:
            if number > 1:
                self.game.replays -= 1
                graphics.replay_step_down(self.game.replays, graphics.magic_ring.reel1, graphics.magic_ring.reel10, graphics.magic_ring.reel100, graphics.magic_ring.reel1000)
                self.game.coils.registerDown.pulse()
                number -= 1
                self.delay(name="display", delay=0, handler=graphics.magic_ring.display, param=self)
                self.delay(name="replay_reset", delay=0.13, handler=self.replay_step_down, param=number)
            elif number == 1:
                self.game.replays -= 1
                graphics.replay_step_down(self.game.replays, graphics.magic_ring.reel1, graphics.magic_ring.reel10, graphics.magic_ring.reel100, graphics.magic_ring.reel1000)
                self.game.coils.registerDown.pulse()
                number -= 1
                self.delay(name="display", delay=0, handler=graphics.magic_ring.display, param=self)
                self.cancel_delayed(name="replay_reset")
        else: 
            if self.game.replays > 0:
                self.game.replays -= 1
                graphics.replay_step_down(self.game.replays, graphics.magic_ring.reel1, graphics.magic_ring.reel10, graphics.magic_ring.reel100, graphics.magic_ring.reel1000)
                self.delay(name="display", delay=0.1, handler=graphics.magic_ring.display, param=self)
            self.game.coils.registerDown.pulse()

    def sw_yellow_active(self, sw):
        if self.game.start.status == False:
            if self.game.switches.drawer.is_inactive():
                if self.game.ball_count.position >= 3:
                    if self.game.three.status == True or self.game.four.status == True or self.game.five.status == True:
                        if (self.game.red_replay_counter.position == 0 and self.game.red_winner.status == True) or (self.game.yellow_replay_counter.position == 0 and self.game.yellow_winner.status == True) or (self.game.green_replay_counter.position == 0 and self.game.green_winner.status == True):
                            if self.game.red_winner_amount > 0 or self.game.yellow_winner_amount > 0 or self.game.green_winner_amount > 0:
                                if self.game.double.status == True and self.game.ball_count.position == 3:
                                    self.game.spotting.spin()
                                    self.game.mixer1.spin()
                                    self.game.mixer2.spin()
                                    self.game.mixer3.spin()
                                    self.game.mixer4.spin()
                                    self.game.mixer5.spin()
                                    self.game.special.engage(self.game)
                                    self.game.all_advantages.disengage()
                                    self.game.odds_only.disengage()
                                    self.game.features.disengage()
                                    self.game.double_double.engage(self.game)
                                    self.regular_play(red_letter=1)
                                    self.game.double_colors.step()
                                    self.game.reflex.decrease()
                                    self.delay(name="display", delay=0.1, handler=graphics.magic_ring.display, param=self)
                                elif self.game.double.status == False:
                                    self.game.spotting.spin()
                                    self.game.mixer1.spin()
                                    self.game.mixer2.spin()
                                    self.game.mixer3.spin()
                                    self.game.mixer4.spin()
                                    self.game.mixer5.spin()
                                    self.game.special.engage(self.game)
                                    self.game.all_advantages.disengage()
                                    self.game.odds_only.disengage()
                                    self.game.features.disengage()
                                    self.game.double.engage(self.game)
                                    self.regular_play(red_letter=1)
                                    self.game.double_colors.step()
                                    self.game.reflex.decrease()
                                    self.delay(name="display", delay=0.1, handler=graphics.magic_ring.display, param=self)
                                if self.game.double_colors.position >= 1 and self.game.ball_count.position == 0 and self.game.start.status == True:
                                    self.game.special.engage(self.game)
                                    if self.game.replays > 0 or self.game.switches.freeplay.is_active():
                                        self.game.sound.stop('add')
                                        self.game.sound.play('add')
                                        self.game.cu = not self.game.cu
                                        self.game.spotting.spin()
                                        self.game.mixer1.spin()
                                        self.game.mixer2.spin()
                                        self.game.mixer3.spin()
                                        self.regular_play()
                                        self.scan_special()
                                        self.game.features.disengage()
                                        self.game.all_advantages.disengage()
                                        self.game.odds_only.disengage()
                    self.delay(name="display", delay=0.1, handler=graphics.magic_ring.display, param=self)

    def sw_orange_active(self, sw):
        if self.game.switches.drawer.is_active():
            if self.game.start.status == False:
                if self.game.ball_count.position >= 3:
                    if self.game.three.status == True or self.game.four.status == True or self.game.five.status == True:
                        if (self.game.red_replay_counter.position == 0 and self.game.red_winner.status == True) or (self.game.yellow_replay_counter.position == 0 and self.game.yellow_winner.status == True) or (self.game.green_replay_counter.position == 0 and self.game.green_winner.status == True):
                            if self.game.red_winner_amount > 0 or self.game.yellow_winner_amount > 0 or self.game.green_winner_amount > 0:
                                if self.game.double.status == True and self.game.ball_count.position == 3:
                                    self.game.spotting.spin()
                                    self.game.mixer1.spin()
                                    self.game.mixer2.spin()
                                    self.game.mixer3.spin()
                                    self.game.mixer4.spin()
                                    self.game.mixer5.spin()
                                    self.game.special.engage(self.game)
                                    self.game.all_advantages.disengage()
                                    self.game.odds_only.disengage()
                                    self.game.features.disengage()
                                    self.game.double_double.engage(self.game)
                                    self.regular_play(red_letter=1)
                                    self.game.double_colors.step()
                                    self.game.reflex.decrease()
                                    self.delay(name="display", delay=0.1, handler=graphics.magic_ring.display, param=self)
                                elif self.game.double.status == False:
                                    self.game.spotting.spin()
                                    self.game.mixer1.spin()
                                    self.game.mixer2.spin()
                                    self.game.mixer3.spin()
                                    self.game.mixer4.spin()
                                    self.game.mixer5.spin()
                                    self.game.special.engage(self.game)
                                    self.game.all_advantages.disengage()
                                    self.game.odds_only.disengage()
                                    self.game.features.disengage()
                                    self.game.double.engage(self.game)
                                    self.regular_play(red_letter=1)
                                    self.game.double_colors.step()
                                    self.game.reflex.decrease()
                                    self.delay(name="display", delay=0.1, handler=graphics.magic_ring.display, param=self)


    def sw_white_active(self, sw):
        if self.game.switches.drawer.is_active():
            if self.game.double_colors.position >= 1 and self.game.ball_count.position == 0 and self.game.start.status == True:
                self.game.special.engage(self.game)
                if self.game.replays > 0 or self.game.switches.freeplay.is_active():
                    self.game.sound.stop('add')
                    self.game.sound.play('add')
                    self.game.cu = not self.game.cu
                    self.game.spotting.spin()
                    self.game.mixer1.spin()
                    self.game.mixer2.spin()
                    self.game.mixer3.spin()
                    self.game.mixer4.spin()
                    self.game.mixer5.spin()
                    self.regular_play()
                    self.scan_special()
                    self.game.features.disengage()
                    self.game.all_advantages.disengage()
                    self.game.odds_only.disengage()
            self.delay(name="display", delay=0.1, handler=graphics.magic_ring.display, param=self)

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
                        #TODO Play sound for each relay closure.
                        s = relays 
                        if s >= 2:
                            self.add_winner(s, self.red, self.yellow, self.green, self.striped_green)
                            if score == 1:
                                self.find_winner(s, self.red, self.yellow, self.green, self.striped_green, self.stars, self.game.red_winner_amount, self.game.yellow_winner_amount, self.game.green_winner_amount)
                            break
                            
    
    def find_stars(self):
        self.game.sound.stop_music()
        self.game.sound.play_music('search', -1)
       
        for i in range(0, 5):
            self.r = self.closed_search_relays(self.game.searchdisc.position)
            self.game.searchdisc.spin()
            self.wipers = self.r[0]
            self.red = self.r[1]
            self.yellow = self.r[2]
            self.green = self.r[3]
            self.striped_green = self.r[4]
            self.stars = self.r[5]
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
                            self.find_winner(s, 0, 0, 0, 0, self.stars, self.game.red_winner_amount, self.game.yellow_winner_amount, self.game.green_winner_amount)
                            break



    def add_winner(self, relays, red, yellow, green, striped_green):
        if self.game.red_odds.position == 1:
            redthreeodds = 9
        if self.game.red_odds.position == 2:
            redthreeodds = 12
        if self.game.red_odds.position == 3:
            redthreeodds = 18
        if self.game.red_odds.position == 4:
            redthreeodds = 24
        if self.game.red_odds.position == 5:
            redthreeodds = 36
        if self.game.red_odds.position == 6:
            redthreeodds = 48
        if self.game.red_odds.position == 7:
            redthreeodds = 72
        if self.game.red_odds.position == 8:
            redthreeodds = 144
        if self.game.red_odds.position == 9:
            redthreeodds = 200
        if self.game.yellow_odds.position == 1:
            yellowthreeodds = 6
            yellowfourodds = 9
        if self.game.yellow_odds.position == 2:
            yellowthreeodds = 9
            yellowfourodds = 12
        if self.game.yellow_odds.position == 3:
            yellowthreeodds = 12
            yellowfourodds = 18
        if self.game.yellow_odds.position == 4:
            yellowthreeodds = 18
            yellowfourodds = 24
        if self.game.yellow_odds.position == 5:
            yellowthreeodds = 24
            yellowfourodds = 36
        if self.game.yellow_odds.position == 6:
            yellowthreeodds = 36
            yellowfourodds = 48
        if self.game.yellow_odds.position == 7:
            yellowthreeodds = 48
            yellowfourodds = 72
        if self.game.yellow_odds.position == 8:
            yellowthreeodds = 100
            yellowfourodds = 144
        if self.game.yellow_odds.position == 9:
            yellowthreeodds = 144
            yellowfourodds = 200
        if self.game.green_odds.position == 1:
            greenthreeodds = 3
            greenfourodds = 6
            greenfiveodds = 25
        if self.game.green_odds.position == 2:
            greenthreeodds = 6
            greenfourodds = 9
            greenfiveodds = 36
        if self.game.green_odds.position == 3:
            greenthreeodds = 9
            greenfourodds = 12
            greenfiveodds = 50
        if self.game.green_odds.position == 4:
            greenthreeodds = 12
            greenfourodds = 18
            greenfiveodds = 100
        if self.game.green_odds.position == 5:
            greenthreeodds = 18
            greenfourodds = 24
            greenfiveodds = 100
        if self.game.green_odds.position == 6:
            greenthreeodds = 24
            greenfourodds = 36
            greenfiveodds = 144
        if self.game.green_odds.position == 7:
            greenthreeodds = 36
            greenfourodds = 48
            greenfiveodds = 200
        if self.game.green_odds.position == 8:
            greenthreeodds = 64
            greenfourodds = 100
            greenfiveodds = 200
        if self.game.green_odds.position == 9:
            greenthreeodds = 100
            greenfourodds = 144
            greenfiveodds = 200

        if relays == 3:
            if red == 1:
                if self.game.red_winner_amount < redthreeodds:
                    self.game.red_winner_amount += redthreeodds
                    self.game.red_winner.engage(self.game)
                    self.game.three.engage(self.game)
            if yellow == 1:
                if self.game.yellow_winner_amount < yellowthreeodds:
                    self.game.yellow_winner_amount += yellowthreeodds
                    self.game.yellow_winner.engage(self.game)
                    self.game.three.engage(self.game)
            if green == 1:
                if self.game.green_winner_amount < greenthreeodds:
                    self.game.green_winner_amount += greenthreeodds
                    self.game.green_winner.engage(self.game)
                    self.game.three.engage(self.game)
        if relays == 4:
            if yellow == 1:
                if self.game.yellow_winner_amount < yellowfourodds:
                    self.game.yellow_winner_amount += yellowfourodds
                    self.game.three.disengage()
                    self.game.four.engage(self.game)
                    self.game.yellow_winner.engage(self.game)
            if green == 1:
                if self.game.green_winner_amount < greenfourodds:
                    self.game.green_winner_amount += greenfourodds
                    self.game.three.disengage()
                    self.game.four.engage(self.game)
                    self.game.green_winner.engage(self.game)
            if stars == 1:
                if self.game.three_stars.status == True:
                    self.game.stars_winner_amount = 300
        if relays == 5:
            if green == 1:
                if self.game.green_winner_amount < greenfiveodds:
                    self.game.green_winner_amount += greenfiveodds
                    self.game.three.disengage()
                    self.game.four.disengage()
                    self.game.five.engage(self.game)
                    self.game.green_winner.engage(self.game)

    def find_winner(self, relays, red, yellow, green, striped_green, stars, red_winner_amount=0, yellow_winner_amount=0, green_winner_amount=0, ok_winner=0, red_letter_winner=0):
        if self.game.search_index.status == False and self.game.replays < 8999:
            redthreeodds =    red_winner_amount
            yellowfourodds =  yellow_winner_amount
            greenfiveodds =   green_winner_amount
            yellowthreeodds = yellow_winner_amount
            greenfourodds =   green_winner_amount
            greenthreeodds =  green_winner_amount

            if self.game.double.status == True and self.game.double_double.status == False:
                if self.game.red_winner.status == True and self.game.red_replay_counter.position == 0:
                    if self.game.three.status == True:
                        redthreeodds =    red_winner_amount * 2
                elif self.game.yellow_winner.status == True and self.game.yellow_replay_counter.position == 0:
                    if self.game.four.status == True:
                        yellowfourodds =  yellow_winner_amount * 2
                    if self.game.three.status == True:
                        yellowthreeodds = yellow_winner_amount * 2
                elif self.game.green_winner.status == True and self.game.green_replay_counter.position == 0:
                    if self.game.five.status == True:
                        greenfiveodds =   green_winner_amount * 2
                    if self.game.four.status == True:
                        greenfourodds =   green_winner_amount * 2
                    if self.game.three.status == True:
                        greenthreeodds =  green_winner_amount * 2
            if self.game.double.status == True and self.game.double_double.status == True:
                if self.game.red_winner.status == True and self.game.red_replay_counter.position == 0:
                    if self.game.three.status == True:
                        redthreeodds =    red_winner_amount * 2 * 2
                elif self.game.yellow_winner.status == True and self.game.yellow_replay_counter.position == 0:
                    if self.game.four.status == True:
                        yellowfourodds =  yellow_winner_amount * 2 * 2
                    if self.game.three.status == True:
                        yellowthreeodds = yellow_winner_amount * 2 * 2
                elif self.game.green_winner.status == True and self.game.green_replay_counter.position == 0:
                    if self.game.five.status == True:
                        greenfiveodds =   green_winner_amount * 2 * 2
                    if self.game.four.status == True:
                        greenfourodds =   green_winner_amount * 2 * 2
                    if self.game.three.status == True:
                        greenthreeodds =  green_winner_amount * 2 * 2

            if relays == 2:
                if (red_winner_amount > 0 or yellow_winner_amount > 0 or green_winner_amount > 0):
                    if self.game.double.status == True:
                        if self.game.double_colors.position >= 1:
                            if red == 1:
                                if self.game.search_index.status == False:
                                    if self.game.double_up.status == True:
                                        if self.game.red_winner.status == True and self.game.red_replay_counter.position == 0:
                                            if self.game.red_replay_counter.position < redthreeodds:
                                                self.game.search_index.engage(self.game)
                                                self.red_replay_step_up(redthreeodds - self.game.red_replay_counter.position)
                                        elif self.game.yellow_winner.status == True and self.game.yellow_replay_counter.position == 0:
                                            if self.game.three.status == True:
                                                if self.game.yellow_replay_counter.position < yellowthreeodds:
                                                    self.game.search_index.engage(self.game)
                                                    self.yellow_replay_step_up(yellowthreeodds - self.game.yellow_replay_counter.position)
                                            elif self.game.four.status == True:
                                                if self.game.yellow_replay_counter.position < yellowfourodds:
                                                    self.game.search_index.engage(self.game)
                                                    self.yellow_replay_step_up(yellowfourodds - self.game.yellow_replay_counter.position)
                                        elif self.game.green_winner.status == True and self.game.green_replay_counter.position == 0:
                                            if self.game.three.status == True:
                                                if self.game.green_replay_counter.position < greenthreeodds:
                                                    self.game.search_index.engage(self.game)
                                                    self.green_replay_step_up(greenthreeodds - self.game.green_replay_counter.position)
                                            elif self.game.four.status == True:
                                                if self.game.green_replay_counter.position < greenfourodds:
                                                    self.game.search_index.engage(self.game)
                                                    self.green_replay_step_up(greenfourodds - self.game.green_replay_counter.position)
                                            elif self.game.five.status == True:
                                                if self.game.green_replay_counter.position < greenfiveodds:
                                                    self.game.search_index.engage(self.game)
                                                    self.green_replay_step_up(greenfiveodds - self.game.green_replay_counter.position)
                                    else:
                                        if self.game.red_winner.status == True and self.game.red_replay_counter.position == 0:
                                            if self.game.red_replay_counter.position < redthreeodds:
                                                self.game.search_index.engage(self.game)
                                                self.red_replay_step_up(redthreeodds - self.game.red_replay_counter.position)


                        if self.game.double_colors.position >= 4:
                            if yellow == 1:
                                if self.game.search_index.status == False:
                                    if self.game.double_up.status == True:
                                        if self.game.red_winner.status == True and self.game.red_replay_counter.position == 0:
                                            if self.game.red_replay_counter.position < redthreeodds:
                                                self.game.search_index.engage(self.game)
                                                self.red_replay_step_up(redthreeodds - self.game.red_replay_counter.position)
                                        elif self.game.yellow_winner.status == True and self.game.yellow_replay_counter.position == 0:
                                            if self.game.three.status == True:
                                                if self.game.yellow_replay_counter.position < yellowthreeodds:
                                                    self.game.search_index.engage(self.game)
                                                    self.yellow_replay_step_up(yellowthreeodds - self.game.yellow_replay_counter.position)
                                            elif self.game.four.status == True:
                                                if self.game.yellow_replay_counter.position < yellowfourodds:
                                                    self.game.search_index.engage(self.game)
                                                    self.yellow_replay_step_up(yellowfourodds - self.game.yellow_replay_counter.position)
                                        elif self.game.green_winner.status == True and self.game.green_replay_counter.position == 0:
                                            if self.game.three.status == True:
                                                if self.game.green_replay_counter.position < greenthreeodds:
                                                    self.game.search_index.engage(self.game)
                                                    self.green_replay_step_up(greenthreeodds - self.game.green_replay_counter.position)
                                            elif self.game.four.status == True:
                                                if self.game.green_replay_counter.position < greenfourodds:
                                                    self.game.search_index.engage(self.game)
                                                    self.green_replay_step_up(greenfourodds - self.game.green_replay_counter.position)
                                            elif self.game.five.status == True:
                                                if self.game.green_replay_counter.position < greenfiveodds:
                                                    self.game.search_index.engage(self.game)
                                                    self.green_replay_step_up(greenfiveodds - self.game.green_replay_counter.position)
                                    else:
                                        if self.game.yellow_winner.status == True and self.game.yellow_replay_counter.position == 0:
                                            if self.game.three.status == True:
                                                if self.game.yellow_replay_counter.position < yellowthreeodds:
                                                    self.game.search_index.engage(self.game)
                                                    self.yellow_replay_step_up(yellowthreeodds - self.game.yellow_replay_counter.position)
                                            elif self.game.four.status == True:
                                                if self.game.yellow_replay_counter.position < yellowfourodds:
                                                    self.game.search_index.engage(self.game)
                                                    self.yellow_replay_step_up(yellowfourodds - self.game.yellow_replay_counter.position)
                        if self.game.double_colors.position >= 7:
                            if green == 1:
                                if self.game.search_index.status == False:
                                    if self.game.double_up.status == True:
                                        if self.game.red_winner.status == True and self.game.red_replay_counter.position == 0:
                                            if self.game.red_replay_counter.position < redthreeodds:
                                                self.game.search_index.engage(self.game)
                                                self.red_replay_step_up(redthreeodds - self.game.red_replay_counter.position)
                                        elif self.game.yellow_winner.status == True and self.game.yellow_replay_counter.position == 0:
                                            if self.game.three.status == True:
                                                if self.game.yellow_replay_counter.position < yellowthreeodds:
                                                    self.game.search_index.engage(self.game)
                                                    self.yellow_replay_step_up(yellowthreeodds - self.game.yellow_replay_counter.position)
                                            elif self.game.four.status == True:
                                                if self.game.yellow_replay_counter.position < yellowfourodds:
                                                    self.game.search_index.engage(self.game)
                                                    self.yellow_replay_step_up(yellowfourodds - self.game.yellow_replay_counter.position)
                                        elif self.game.green_winner.status == True and self.game.green_replay_counter.position == 0:
                                            if self.game.three.status == True:
                                                if self.game.green_replay_counter.position < greenthreeodds:
                                                    self.game.search_index.engage(self.game)
                                                    self.green_replay_step_up(greenthreeodds - self.game.green_replay_counter.position)
                                            elif self.game.four.status == True:
                                                if self.game.green_replay_counter.position < greenfourodds:
                                                    self.game.search_index.engage(self.game)
                                                    self.green_replay_step_up(greenfourodds - self.game.green_replay_counter.position)
                                            elif self.game.five.status == True:
                                                if self.game.green_replay_counter.position < greenfiveodds:
                                                    self.game.search_index.engage(self.game)
                                                    self.green_replay_step_up(greenfiveodds - self.game.green_replay_counter.position)
                                    else:
                                        if self.game.green_winner.status == True and self.game.green_replay_counter.position == 0:
                                            if self.game.three.status == True:
                                                if self.game.green_replay_counter.position < greenthreeodds:
                                                    self.game.search_index.engage(self.game)
                                                    self.green_replay_step_up(greenthreeodds - self.game.green_replay_counter.position)
                                            elif self.game.four.status == True:
                                                if self.game.green_replay_counter.position < greenfourodds:
                                                    self.game.search_index.engage(self.game)
                                                    self.green_replay_step_up(greenfourodds - self.game.green_replay_counter.position)
                                            elif self.game.five.status == True:
                                                if self.game.green_replay_counter.position < greenfiveodds:
                                                    self.game.search_index.engage(self.game)
                                                    self.green_replay_step_up(greenfiveodds - self.game.green_replay_counter.position)
                        if self.game.double_colors.position >= 10:
                            if striped_green == 1:
                                if self.game.search_index.status == False:
                                    if self.game.double_up.status == True:
                                        if self.game.red_winner.status == True and self.game.red_replay_counter.position == 0:
                                            if self.game.red_replay_counter.position < redthreeodds:
                                                self.game.search_index.engage(self.game)
                                                self.red_replay_step_up(redthreeodds - self.game.red_replay_counter.position)
                                        elif self.game.yellow_winner.status == True and self.game.yellow_replay_counter.position == 0:
                                            if self.game.three.status == True:
                                                if self.game.yellow_replay_counter.position < yellowthreeodds:
                                                    self.game.search_index.engage(self.game)
                                                    self.yellow_replay_step_up(yellowthreeodds - self.game.yellow_replay_counter.position)
                                            elif self.game.four.status == True:
                                                if self.game.yellow_replay_counter.position < yellowfourodds:
                                                    self.game.search_index.engage(self.game)
                                                    self.yellow_replay_step_up(yellowfourodds - self.game.yellow_replay_counter.position)
                                        elif self.game.green_winner.status == True and self.game.green_replay_counter.position == 0:
                                            if self.game.three.status == True:
                                                if self.game.green_replay_counter.position < greenthreeodds:
                                                    self.game.search_index.engage(self.game)
                                                    self.green_replay_step_up(greenthreeodds - self.game.green_replay_counter.position)
                                            elif self.game.four.status == True:
                                                if self.game.green_replay_counter.position < greenfourodds:
                                                    self.game.search_index.engage(self.game)
                                                    self.green_replay_step_up(greenfourodds - self.game.green_replay_counter.position)
                                            elif self.game.five.status == True:
                                                if self.game.green_replay_counter.position < greenfiveodds:
                                                    self.game.search_index.engage(self.game)
                                                    self.green_replay_step_up(greenfiveodds - self.game.green_replay_counter.position)
                                    else:
                                        if self.game.green_winner.status == True and self.game.green_replay_counter.position == 0:
                                            if self.game.three.status == True:
                                                if self.game.green_replay_counter.position < greenthreeodds:
                                                    self.game.search_index.engage(self.game)
                                                    self.green_replay_step_up(greenthreeodds - self.game.green_replay_counter.position)
                                            elif self.game.four.status == True:
                                                if self.game.green_replay_counter.position < greenfourodds:
                                                    self.game.search_index.engage(self.game)
                                                    self.green_replay_step_up(greenfourodds - self.game.green_replay_counter.position)
                                            elif self.game.five.status == True:
                                                if self.game.green_replay_counter.position < greenfiveodds:
                                                    self.game.search_index.engage(self.game)
                                                    self.green_replay_step_up(greenfiveodds - self.game.green_replay_counter.position)
            if self.game.double_colors.position == 0:
                if relays == 3:
                    if red == 1:
                        if self.game.search_index.status == False:
                            if self.game.red_replay_counter.position < redthreeodds:
                                self.game.search_index.engage(self.game)
                                self.red_replay_step_up(redthreeodds - self.game.red_replay_counter.position)
                    if yellow == 1:
                        if self.game.search_index.status == False:
                            if self.game.yellow_replay_counter.position < yellowthreeodds:
                                self.game.search_index.engage(self.game)
                                self.yellow_replay_step_up(yellowthreeodds - self.game.yellow_replay_counter.position)
                    if green == 1:
                        if self.game.search_index.status == False:
                            if self.game.green_replay_counter.position < greenthreeodds:
                                self.game.search_index.engage(self.game)
                                self.green_replay_step_up(greenthreeodds - self.game.green_replay_counter.position)
                if relays == 4:
                    if yellow == 1:
                        if self.game.search_index.status == False:
                            if self.game.yellow_replay_counter.position < yellowfourodds:
                                self.game.search_index.engage(self.game)
                                self.yellow_replay_step_up(yellowfourodds - self.game.yellow_replay_counter.position)
                    if green == 1:
                        if self.game.search_index.status == False:
                            if self.game.green_replay_counter.position < greenfourodds:
                                self.game.search_index.engage(self.game)
                                self.green_replay_step_up(greenfourodds - self.game.green_replay_counter.position)
                    if stars == 1:
                        if self.game.search_index.status == False:
                            if self.game.three_stars.status == True:
                                if self.game.stars_replay_counter.position < 300:
                                    self.game.search_index.engage(self.game)
                                    self.stars_replay_step_up(300 - self.game.stars_replay_counter.position)
                            if self.game.six_stars.status == True:
                                if self.game.stars_replay_counter.position < 600:
                                    self.game.search_index.engage(self.game)
                                    self.stars_replay_step_up(600 - self.game.stars_replay_counter.position)
                if relays == 5:
                    if green == 1:
                        if self.game.search_index.status == False:
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
            self.game.red_winner.disengage()
            if self.game.double_up.status == False:
                self.game.double.disengage()
                self.game.double_double.disengage()
            else:
                if self.game.yellow_winner.status == False and self.game.green_winner.status == False:
                    self.game.double.disengage()
                    self.game.double_double.disengage()
            self.delay(name="display", delay=0.1, handler=graphics.magic_ring.display, param=self)
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
            self.game.yellow_winner.disengage()
            if self.game.double_up.status == False:
                self.game.double.disengage()
                self.game.double_double.disengage()
            else:
                if self.game.yellow_winner.status == False and self.game.green_winner.status == False:
                    self.game.double.disengage()
                    self.game.double_double.disengage()
            self.delay(name="display", delay=0.1, handler=graphics.magic_ring.display, param=self)
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
            self.game.green_winner.disengage()
            if self.game.double_up.status == False:
                self.game.double.disengage()
                self.game.double_double.disengage()
            else:
                if self.game.yellow_winner.status == False and self.game.green_winner.status == False:
                    self.game.double.disengage()
                    self.game.double_double.disengage()
            self.delay(name="display", delay=0.1, handler=graphics.magic_ring.display, param=self)
            self.search()

    def replay_step_up(self):
        if self.game.replays < 8999:
            self.game.replays += 1
            graphics.replay_step_up(self.game.replays, graphics.magic_ring.reel1, graphics.magic_ring.reel10, graphics.magic_ring.reel100, graphics.magic_ring.reel1000)
        self.game.coils.registerUp.pulse()
        self.game.reflex.increase()
        graphics.magic_ring.display(self)

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
        stars = False

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

        self.pos[5] = {4:1, 14:2, 17:3, 18:4}

        if rivets == 1:
            yellow = True
        if rivets == 2:
            striped_green = True
        if rivets == 3:
            green = True
        if rivets == 4:
            red = True
        if rivets == 5:
            stars = True
                
        return (self.pos[rivets], red, yellow, green, striped_green, stars)

    
    def scan_all(self):
        #Animate scanning of everything - this happens through the spotting disc
        self.all_probability()

    def check_reflex(self):
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
            s = random.randint(1,8)
            self.animate_odds_scan(s)
            s = random.randint(1,4)
            self.animate_feature_scan(s)
            self.delay(name="display", delay=0.1, handler=graphics.magic_ring.display, param=self)

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
        r = self.check_reflex()
        if self.game.red_odds.position < 2:
            self.game.red_odds.step()
            if self.game.odds_only.status == True:
                if self.game.red_odds.position < 2:
                    self.game.red_odds.step()
            if self.game.yellow_odds.position < 2:
                self.game.yellow_odds.step()
            if self.game.odds_only.status == True:
                if self.game.yellow_odds.position < 2:
                    self.game.yellow_odds.step()
            if self.game.green_odds.position < 2:
                self.game.green_odds.step()
            if self.game.odds_only.status == True:
                if self.game.green_odds.position < 2:
                    self.game.green_odds.step()
            return
        sd = self.game.spotting.position
        if sd in [0,6,7,8,11,12,13,15,16,18,19,27,28,30,34,36,37,38,43,44,45,48]:
            r = self.check_red_mixer3()
            if r == 1:
               if self.game.red_odds.position in [3,4,5]:
                   self.game.red_odds.step()
            y = self.check_yellow_mixer3()
            if y == 1:
                if self.game.yellow_odds.position in [3,4,5]:
                    self.game.yellow_odds.step()
            g = self.check_green_mixer3()
            if g == 1:
               if self.game.green_odds.position in [3,4,5]:
                   self.game.green_odds.step()
            return
        if self.game.features.status == True:
            if sd in [3,4,24,26,29,35,39,42,47,49]:
                r = self.check_red_mixer3()
                if r == 1:
                    if self.game.red_odds.position in [3,4,5]:
                        self.game.red_odds.step()
                y = self.check_yellow_mixer3()
                if y == 1:
                    if self.game.yellow_odds.position in [3,4,5]:
                        self.game.yellow_odds.step()
                g = self.check_green_mixer3()
                if g == 1:
                    if self.game.green_odds.position in [3,4,5]:
                        self.game.green_odds.step()
            return
        if self.game.green_odds.position == 2:
            self.game.green_odds.step()
        if self.game.red_odds.position == 2:
            self.game.red_odds.step()
        if self.game.yellow_odds.position == 2:
            self.game.yellow_odds.step()
        if sd in [0,5,6,12,16,23,30,32,34,38,41,45]:
            r = self.check_red_mixer3()
            if r == 1:
                if self.game.red_odds.position in [6]:
                    self.game.red_odds.step()
            y = self.check_yellow_mixer3()
            if y == 1:
                if self.game.yellow_odds.position in [6]:
                    self.game.yellow_odds.step()
            g = self.check_green_mixer3()
            if g == 1:
                if self.game.green_odds.position in [6]:
                    self.game.green_odds.step()
            return
        if sd in [14,17,24,25,26,29,35,39,42,47,49]:
            if self.game.odds_only.status == True:
                r = self.check_red_mixer3()
                if r == 1:
                    if self.game.red_odds.position in [6]:
                        self.game.red_odds.step()
                y = self.check_yellow_mixer3()
                if y == 1:
                    if self.game.yellow_odds.position in [6]:
                        self.game.yellow_odds.step()
                g = self.check_green_mixer3()
                if g == 1:
                    if self.game.green_odds.position in [6]:
                        self.game.green_odds.step()
                return
        if sd in [18,22,37,43]:
            r = self.check_red_mixer3()
            if r == 1:
                if self.game.red_odds.position in [7]:
                    self.game.red_odds.step()
            y = self.check_yellow_mixer3()
            if y == 1:
                if self.game.yellow_odds.position in [7]:
                    self.game.yellow_odds.step()
            g = self.check_green_mixer3()
            if g == 1:
                if self.game.green_odds.position in [7]:
                    self.game.green_odds.step()
            return
        if sd in [2,17,25,32,46]:
            if self.game.odds_only.status == True:
                r = self.check_red_mixer3()
                if r == 1:
                    if self.game.red_odds.position in [7]:
                        self.game.red_odds.step()
                y = self.check_yellow_mixer3()
                if y == 1:
                    if self.game.yellow_odds.position in [7]:
                        self.game.yellow_odds.step()
                g = self.check_green_mixer3()
                if g == 1:
                    if self.game.green_odds.position in [7]:
                        self.game.green_odds.step()
                return
        if sd in [1,28,44,48]:
            r = self.check_red_mixer3()
            if r == 1:
                if self.game.red_odds.position in [8]:
                    self.game.red_odds.step()
            y = self.check_yellow_mixer3()
            if y == 1:
                if self.game.yellow_odds.position in [8]:
                    self.game.yellow_odds.step()
            g = self.check_green_mixer3()
            if g == 1:
                if self.game.green_odds.position in [8]:
                    self.game.green_odds.step()
            return
        if sd in [2,20,40]:
            if self.game.odds_only.status == True:
                r = self.check_red_mixer3()
                if r == 1:
                    if self.game.red_odds.position in [8]:
                        self.game.red_odds.step()
                y = self.check_yellow_mixer3()
                if y == 1:
                    if self.game.yellow_odds.position in [8]:
                        self.game.yellow_odds.step()
                g = self.check_green_mixer3()
                if g == 1:
                    if self.game.green_odds.position in [8]:
                        self.game.green_odds.step()
                return

    def check_red_mixer3(self):
        m3 = self.game.mixer3.position
        if m3 in [3,5,7,11,12,17,20,22,0]:
            return 1
        else:
            return 0
    def check_yellow_mixer3(self):
        m3 = self.game.mixer3.position
        if m3 in [2,6,10,14,15,18,19,23]:
            return 1
        else:
            return 0
    def check_green_mixer3(self):
        m3 = self.game.mixer3.position
        if m3 in [1,4,8,9,13,16,21]:
            return 1
        else:
            return 0

    def scan_features(self):
        p = self.features_probability()

    def scan_special(self):
        sd = self.game.spotting.position
        if self.game.double_colors.position < 3:
            self.game.double_colors.step()
        else:
            m = self.check_mixer4()
            if self.game.mixer4_relay.status == True:
                self.game.mixer4_relay.disengage()
                if self.game.cu:
                    if sd in [1,5,6,7,8,9,10,11,14,17,18,19,20,21,22,25,26,38,44]:
                        self.game.double_colors.step()
        self.delay(name="display", delay=0.1, handler=graphics.magic_ring.display, param=self)

    def check_mixer4(self):
        m4 = self.game.mixer4.position
        if self.game.green_odds.position == 0:
            self.game.mixer4_relay.engage(self.game)
            return
        if self.game.green_odds.position <= 4:
            if m4 in [12,13,21,22]:
                self.game.mixer4_relay.engage(self.game)
                return
        if self.game.green_odds.position == 5:
            if m4 in [2,3,8,10,17,18]:
                self.game.mixer4_relay.engage(self.game)
                return
        if self.game.green_odds.position == 6:
            if m4 in [0,5,6]:
                self.game.mixer4_relay.engage(self.game)
                return
        if self.game.green_odds.position == 7:
            if m4 in [14,15]:
                self.game.mixer4_relay.engage(self.game)
                return
        if self.game.green_odds.position == 8:
            if m4 in [1,4,7]:
                self.game.mixer4_relay.engage(self.game)
                return
        if self.game.green_odds.position == 9:
            if m4 in [11]:
                self.game.mixer4_relay.engage(self.game)
                return
        if self.game.yellow_odds.position <= 4:
            if m4 in [10,12]:
                self.game.mixer4_relay.engage(self.game)
                return
        if self.game.yellow_odds.position == 5:
            if m4 in [2,3,6,22]:
                self.game.mixer4_relay.engage(self.game)
                return
        if self.game.yellow_odds.position == 6:
            if m4 in [0,5,15]:
                self.game.mixer4_relay.engage(self.game)
                return
        if self.game.yellow_odds.position == 7:
            if m4 in [4,18]:
                self.game.mixer4_relay.engage(self.game)
                return
        if self.game.yellow_odds.position == 8:
            if m4 in [11]:
                self.game.mixer4_relay.engage(self.game)
                return
        if self.game.yellow_odds.position == 9:
            if m4 in [7,16]:
                self.game.mixer4_relay.engage(self.game)
                return
        if self.game.red_odds.position <= 3:
            self.game.mixer4_relay.engage(self.game)
            return
        if self.game.red_odds.position == 4:
            if m4 in [12,19]:
                self.game.mixer4_relay.engage(self.game)
                return
        if self.game.red_odds.position == 5:
            if m4 in [3,8,18,22]:
                self.game.mixer4_relay.engage(self.game)
                return
        if self.game.red_odds.position == 6:
            if m4 in [0,5,6]:
                self.game.mixer4_relay.engage(self.game)
                return
        if self.game.red_odds.position == 7:
            if m4 in [1,2]:
                self.game.mixer4_relay.engage(self.game)
                return
        if self.game.red_odds.position == 8:
            if m4 in [14,16]:
                self.game.mixer4_relay.engage(self.game)
                return
        if self.game.red_odds.position == 9:
            if m4 in [20]:
                self.game.mixer4_relay.engage(self.game)
                return
        self.game.mixer4_relay.disengage()

    def features_probability(self):
        s = random.randint(1,4)
        self.animate_feature_scan(s)
        self.check_mixer4()
        if self.game.mixer4_relay.status == True:
            self.features_spotting()
            self.game.mixer4_relay.disengage()
        else:
            self.game.mixer4_relay.disengage()

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
    
        if sd in [17]:
            if self.game.six_stars.status == False:
                self.game.three_stars.engage(self.game)
        if sd in [41]:
            self.game.six_stars.engage(self.game)
            if self.game.three_stars.status == True:
                self.game.three_stars.disengage()
        if sd in [13,27,44,49,5,6,30,34]:
            self.game.double_up.engage(self.game)

    def step_wheel(self, number):
        if number >= 1:
            self.game.wheel.step()
            number -= 1
            self.delay(name="display", delay=0.1, handler=graphics.magic_ring.display, param=self)
            self.delay(name="step_wheel", delay=0.1, handler=self.step_wheel, param=number)


    def step_selection(self, number):
        if number >= 1:
            self.game.selection_feature.step()
            self.check_selection()
            number -= 1
            self.delay(name="display", delay=0.1, handler=graphics.magic_ring.display, param=self)
            self.delay(name="step_sc", delay=0.1, handler=self.step_selection, param=number)

    def animate_odds_scan(self, s):
        if s > 1:
            self.delay(name="odds_animation", delay=0.1, handler=graphics.magic_ring.odds_animation, param=s)
            self.delay(name="display", delay=0.1, handler=graphics.magic_ring.display, param=self)
            s -= 1
            #self.delay(name="animate_odds", delay=0.1, handler=self.animate_odds_scan, param=s)
        else:
            self.cancel_delayed(name="odds_animation")
            self.cancel_delayed(name="display")

    def animate_feature_scan(self, s):
        if s > 1:
            self.delay(name="feature_animation", delay=0.1, handler=graphics.magic_ring.feature_animation, param=s)
            self.delay(name="display", delay=0.1, handler=graphics.magic_ring.display, param=self)
            s -= 1
            #self.delay(name="animate_feature", delay=0.1, handler=self.animate_feature_scan, param=s)
        else:
            self.delay(name="display", delay=0.1, handler=graphics.magic_ring.display, param=self)

    # Define reset as the knock-off, anti-cheat relay disabled, and replay reset enabled.  Motors turn while credits are knocked off.
    # When meter reaches zero and the zero limit switch is hit, turn off motor sound and leave backglass gi on, but with tilt displayed.

    def startup(self):        
        # Every bingo requires the meter to register '0' 
        # before allowing coin entry --
        # also needs to show a plain 'off' backglass.
        self.game.anti_cheat.engage(self.game)
        self.tilt_actions()
        self.game.all_advantages.engage(self.game)

class MagicRing(procgame.game.BasicGame):
    """Magic Ring is the last wheel unit game """
    def __init__(self, machine_type):
        super(MagicRing, self).__init__(machine_type)
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
        self.special = units.Relay("special")

        #Odds steppers
        self.red_odds = units.Stepper("red_odds", 9, 'magic_ring')
        self.yellow_odds = units.Stepper("yellow_odds", 9, 'magic_ring')
        self.green_odds = units.Stepper("green_odds", 9, 'magic_ring')

        self.red_winner = units.Relay("red_winner")
        self.yellow_winner = units.Relay("yellow_winner")
        self.green_winner = units.Relay("green_winner")

        #Replay Counter
        self.red_replay_counter = units.Stepper("red_replay_counter", 1800)
        self.yellow_replay_counter = units.Stepper("yellow_replay_counter", 1800)
        self.green_replay_counter = units.Stepper("green_replay_counter", 1800)
        self.stars_replay_counter = units.Stepper("stars_replay_counter", 1800)
      
        self.wheel = units.Stepper("wheel", 9)

        self.ring = units.Stepper("ring", 19, 'magic_ring', 'continuous')

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
        
        self.three_stars = units.Relay("three_stars")
        self.six_stars = units.Relay("six_stars")
        self.double_up = units.Relay("double_up")

        self.selector = units.Stepper("selector", 1)

        self.three = units.Relay("three")
        self.four = units.Relay("four")
        self.five = units.Relay("five")
        self.red_winner_amount = 0
        self.green_winner_amount = 0
        self.yellow_winner_amount = 0

        self.double = units.Relay("double")
        self.double_double = units.Relay("double_double")
        self.double_colors = units.Stepper("double_colors", 10)

        self.yellow_star = units.Relay("yellow_star")
        self.red_star = units.Relay("red_star")
        
        self.mixer2_relay = units.Relay("mixer2_relay")
        self.mixer4_relay = units.Relay("mixer4_relay")

        self.replays = 0
        self.returned = False

    def reset(self):
        super(MagicRing, self).reset()
        self.logger = logging.getLogger('game')
        self.load_config('bingo.yaml')
        
        main_mode = SinglecardBingo(self)
        self.modes.add(main_mode)
        
game = MagicRing(machine_type='pdb')
game.reset()
game.run_loop()
