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
from bingo_emulator.graphics.rodeo_1 import *

class SinglecardBingo(procgame.game.Mode):
    def __init__(self, game):
        super(SinglecardBingo, self).__init__(game=game, priority=5)
        self.holes = []
        self.startup()
        self.game.sound.register_music('motor', "audio/other_motor.wav")
        self.game.sound.register_music('search', "audio/six_card_search_old.wav")
        self.game.sound.register_sound('add', "audio/six_card_add_card.wav")
        self.game.sound.register_sound('tilt', "audio/tilt.wav")
        self.game.sound.register_sound('step', "audio/step.wav")
        self.game.sound.register_sound('eb_search', "audio/EB_Search.wav")

    def sw_coin_active(self, sw):
        self.game.tilt.disengage()
        if self.game.all_advantages.status == True:
            self.game.sound.stop('add')
            self.game.sound.play('add')
            self.regular_play()
            self.game.odds_only.disengage()
            self.game.eb.disengage()
            self.game.features.disengage()
            self.scan_all()
        elif self.game.features.status == True:
            self.game.sound.stop('add')
            self.game.sound.play('add')
            self.regular_play()
            self.game.odds_only.disengage()
            self.game.eb.disengage()
            self.game.all_advantages.disengage()
            self.scan_features()
            self.game.features.disengage()
            self.game.all_advantages.engage(self.game)
        elif self.game.odds_only.status == True:
            self.game.sound.stop('add')
            self.game.sound.play('add')
            self.regular_play()
            self.game.eb.disengage()
            self.game.features.disengage()
            self.game.all_advantages.disengage()
            self.scan_odds()
            self.game.odds_only.disengage()
            self.game.all_advantages.engage(self.game)
        elif self.game.eb.status == True:
            self.game.sound.stop('add')
            self.game.sound.play('add')
            self.game.features.disengage()
            self.game.all_advantages.disengage()
            self.game.odds_only.disengage()
            self.scan_eb()
            self.game.eb.disengage()
            self.game.all_advantages.engage(self.game)
        else:
            self.game.sound.stop('add')
            self.game.sound.play('add')
            self.regular_play()
            self.game.all_advantages.engage(self.game)
            self.game.odds_only.disengage()
            self.game.eb.disengage()
            self.game.features.disengage()
            self.scan_all()
        self.delay(name="display", delay=0.1, handler=graphics.rodeo_1.display, param=self)

    def sw_startButton_active(self, sw):
        if self.game.replays > 0 or self.game.switches.freeplay.is_active():
            self.game.sound.stop('add')
            self.game.sound.play('add')
            self.game.tilt.disengage()
            self.regular_play()
            self.scan_all()
            self.delay(name="display", delay=0.1, handler=graphics.rodeo_1.display, param=self)

    def sw_enter_active(self, sw):
        if self.game.switches.left.is_active() and self.game.switches.right.is_active():
            self.game.end_run_loop()
            os.system("/home/nbaldridge/proc/bingo_emulator/start_game.sh rodeo_1")

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

    def sw_blue_active(self, sw):
        self.game.features.disengage()
        self.game.all_advantages.disengage()
        self.game.odds_only.disengage()
        self.game.eb.disengage()
        if self.game.replays > 0 or self.game.switches.freeplay.is_active():
            if self.game.start.status == False:
                self.delay(name="startup", delay=0.1, handler=self.sw_startButton_active, param=sw)
            else:
                self.game.sound.stop('add')
                self.game.sound.play('add')
                self.game.odds_only.engage(self.game)
                self.delay(name="display", delay=0.1, handler=graphics.rodeo_1.display, param=self)
                self.regular_play()
                self.scan_odds()
                self.game.odds_only.disengage()
                self.delay(name="display", delay=0.1, handler=graphics.rodeo_1.display, param=self)
        else:
            self.game.odds_only.engage(self.game)
            self.delay(name="display", delay=0.1, handler=graphics.rodeo_1.display, param=self)

    def sw_yellow_active(self, sw):
        self.game.features.disengage()
        self.game.all_advantages.disengage()
        self.game.odds_only.disengage()
        self.game.eb.disengage()

        if self.game.replays > 0 or self.game.switches.freeplay.is_active():
            if self.game.start.status == False:
                self.delay(name="startup", delay=0.1, handler=self.sw_startButton_active, param=sw)
            else:
                self.game.sound.stop('add')
                self.game.sound.play('add')
                self.game.features.engage(self.game)
                self.delay(name="display", delay=0.1, handler=graphics.rodeo_1.display, param=self)
                self.regular_play()
                self.scan_features()
                self.game.features.disengage()
                self.delay(name="display", delay=0.1, handler=graphics.rodeo_1.display, param=self)
        else:
            self.game.features.engage(self.game)
            self.delay(name="display", delay=0.1, handler=graphics.rodeo_1.display, param=self)

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
        self.cancel_delayed(name="timeout")
        self.game.coils.counter.pulse()
        self.cancel_delayed(name="card1_replay_step_up")
        self.cancel_delayed(name="corners_replay_step_up")
        self.game.search_index.disengage()

        self.game.cu = not self.game.cu
        self.game.spotting.spin()
        self.game.mixer1.spin()
        self.game.mixer2.spin()
        self.game.mixer3.spin()
        self.game.mixer4.spin()
        self.game.mixer5.spin()
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
            self.game.coils.redROLamp.disable()
            self.game.coils.yellowROLamp.disable()
            self.game.liteaname.disengage()
            self.game.extra_ball.reset()
            if self.game.name.position == 5:
                self.game.name.reset()
            if self.game.eight_balls.status == True:
                self.step_eb(24)
                self.game.eight_balls.disengage()
            self.game.three_as_four.disengage()
            self.game.four_as_five.disengage()
            self.game.card1_replay_counter.reset()
            self.game.corners.disengage()
            self.game.super_card.reset()
            self.game.corners_replay_counter.reset()
            self.game.yellow_star.disengage()
            self.game.red_star.disengage()
            self.game.sixteen.disengage()
            self.game.five.disengage()
            self.game.seventeen.disengage()
            self.game.two.disengage()
            self.game.fifteen.disengage()
            self.game.start.engage(self.game)
            self.game.selector.reset()
            self.game.ball_count.reset()
            self.game.odds.reset()
            self.game.timer.reset()
            self.game.sound.play_music('motor', -1)
            self.regular_play()
        self.delay(name="display", delay=0.1, handler=graphics.rodeo_1.display, param=self)
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
                            if self.game.extra_ball.position >= 8 and self.game.ball_count.position <= 5:
                                if self.game.switches.shooter.is_open() and self.game.switches.trough3.is_closed():
                                    self.game.coils.lifter.enable()
                        if self.game.switches.trough3.is_open():
                            if self.game.extra_ball.position >= 16 and self.game.ball_count.position <= 6:
                                if self.game.switches.shooter.is_open() and self.game.switches.trough2.is_closed():
                                    self.game.coils.lifter.enable()
                        if self.game.switches.trough2.is_inactive() and self.game.ball_count.position <= 7:
                            if self.game.ball_count.position <= 7:
                                if self.game.extra_ball.position >= 24:
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
                if self.game.ball_count.position == 5 and self.game.extra_ball.position >= 8:
                    self.game.coils.lifter.enable()
                if self.game.ball_count.position == 6 and self.game.extra_ball.position >= 16:
                    self.game.coils.lifter.enable()
                if self.game.ball_count.position == 7 and self.game.extra_ball.position >= 24:
                    self.game.coils.lifter.enable()

    def sw_gate_inactive_for_1ms(self, sw):
        self.game.start.disengage()
        self.game.ball_count.step()
        if self.game.switches.shutter.is_active():
            self.game.coils.shutter.enable()
        if self.game.ball_count.position >= 5:
            if self.game.search_index.status == False:
                self.search()
        if self.game.ball_count.position > 5:
            self.game.coils.yellowROLamp.disable()
            self.game.coils.redROLamp.disable()
        if self.game.ball_count.position <= 7:
            self.check_lifter_status()


    # This is really nasty, but it is how we render graphics for each individual hole.
    # numbers are added (or removed from) a list.  In this way, I can re-use the same
    # routine even for games where there are ball return functions like Surf Club.

    def sw_hole1_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(1)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.rodeo_1.display, param=self)

    def sw_hole2_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(2)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.rodeo_1.display, param=self)

    def sw_hole3_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(3)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.rodeo_1.display, param=self)

    def sw_hole4_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(4)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.rodeo_1.display, param=self)

    def sw_hole5_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(5)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.rodeo_1.display, param=self)

    def sw_hole6_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(6)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.rodeo_1.display, param=self)

    def sw_hole7_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(7)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.rodeo_1.display, param=self)

    def sw_hole8_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(8)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.rodeo_1.display, param=self)

    def sw_hole9_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(9)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.rodeo_1.display, param=self)

    def sw_hole10_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(10)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.rodeo_1.display, param=self)

    def sw_hole11_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(11)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.rodeo_1.display, param=self)

    def sw_hole12_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(12)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.rodeo_1.display, param=self)

    def sw_hole13_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(13)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.rodeo_1.display, param=self)

    def sw_hole14_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(14)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.rodeo_1.display, param=self)

    def sw_hole15_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(15)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.rodeo_1.display, param=self)

    def sw_hole16_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(16)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.rodeo_1.display, param=self)

    def sw_hole17_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(17)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.rodeo_1.display, param=self)

    def sw_hole18_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(18)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.rodeo_1.display, param=self)

    def sw_hole19_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(19)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.rodeo_1.display, param=self)

    def sw_hole20_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(20)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.rodeo_1.display, param=self)

    def sw_hole21_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(21)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.rodeo_1.display, param=self)

    def sw_hole22_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(22)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.rodeo_1.display, param=self)

    def sw_hole23_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(23)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.rodeo_1.display, param=self)

    def sw_hole24_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(24)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.rodeo_1.display, param=self)

    def sw_hole25_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(25)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.rodeo_1.display, param=self)

    def sw_replayReset_active(self, sw):
        self.game.anti_cheat.disengage()
        self.holes = []
        graphics.rodeo_1.display(self)
        self.tilt_actions()
        self.replay_step_down(self.game.replays)

    def sw_redstar_active(self, sw):
        if self.game.red_star.status == True:
            if self.game.two.status == False:
                self.game.two.engage(self.game)
                if 2 not in self.holes:
                    self.holes.append(2)
            if self.game.five.status == False:
                self.game.five.engage(self.game)
                if 5 not in self.holes:
                    self.holes.append(5)
            if self.game.fifteen.status == False:
                self.game.fifteen.engage(self.game)
                if 15 not in self.holes:
                    self.holes.append(15)
            if self.game.sixteen.status == False:
                self.game.sixteen.engage(self.game)
                if 16 not in self.holes:
                    self.holes.append(16)
            if self.game.seventeen.status == False:
                self.game.seventeen.engage(self.game)
                if 17 not in self.holes:
                    self.holes.append(17)
            if self.game.liteaname.status == True:
                self.game.name.step()
                if self.game.name.position == 5:
                    # If Lite-a-name awards replays, use the commented out section.  After 
                    # reviewing the backglass, I think it awards eight balls next game.
                    #self.game.search_index.engage(self.game)
                    #self.name_replay_step_up(self.game.odds.five)
                    self.game.eight_balls.engage(self.game)
                    
            self.delay(name="display", delay=0.1, handler=graphics.rodeo_1.display, param=self)
            if self.game.ball_count.position >= 4:
                self.search()

    def sw_yellowstar_active(self, sw):
        if self.game.yellow_star.status == True:
            if self.game.two.status == False:
                self.game.two.engage(self.game)
                if 2 not in self.holes:
                    self.holes.append(2)
            if self.game.five.status == False:
                self.game.five.engage(self.game)
                if 5 not in self.holes:
                    self.holes.append(5)
            if self.game.fifteen.status == False:
                self.game.fifteen.engage(self.game)
                if 15 not in self.holes:
                    self.holes.append(15)
            if self.game.sixteen.status == False:
                self.game.sixteen.engage(self.game)
                if 16 not in self.holes:
                    self.holes.append(16)
            if self.game.seventeen.status == False:
                self.game.seventeen.engage(self.game)
                if 17 not in self.holes:
                    self.holes.append(17)
            if self.game.liteaname.status == True:
                self.game.name.step()
                if self.game.name.position == 5:
                    # If Lite-a-name awards replays, use the commented out section.  After 
                    # reviewing the backglass, I think it awards eight balls next game.
                    #self.game.search_index.engage(self.game)
                    #self.name_replay_step_up(self.game.odds.five)
                    self.game.eight_balls.engage(self.game)
            self.delay(name="display", delay=0.1, handler=graphics.rodeo_1.display, param=self)
            if self.game.ball_count.position >= 4:
                self.search()

    def tilt_actions(self):
        self.game.start.disengage()
        self.cancel_delayed(name="replay_reset")
        self.cancel_delayed(name="card1_replay_step_up")
        self.cancel_delayed(name="corners_replay_step_up")
        self.cancel_delayed(name="timeout")
        self.game.coils.redROLamp.disable()
        self.game.coils.yellowROLamp.disable()
        self.game.search_index.disengage()
        if self.game.ball_count.position == 0:
            if self.game.switches.shutter.is_active():
                self.game.coils.shutter.enable()
        self.holes = []
        self.game.selector.reset()
        self.game.card1_replay_counter.reset()
        self.game.corners.disengage()
        self.game.super_card.reset()
        self.game.corners_replay_counter.reset()
        self.game.yellow_star.disengage()
        self.game.red_star.disengage()
        self.game.sixteen.disengage()
        self.game.five.disengage()
        self.game.seventeen.disengage()
        self.game.two.disengage()
        self.game.fifteen.disengage()
        self.game.ball_count.reset()
        self.game.odds.reset()
        self.game.extra_ball.reset()
        self.game.anti_cheat.engage(game)
        self.game.tilt.engage(self.game)
        self.game.sound.stop_music()
        self.game.sound.play('tilt')
        # displays "Tilt" on the backglass, you have to recoin.
        self.delay(name="display", delay=0.1, handler=graphics.rodeo_1.display, param=self)

    def sw_tilt_active(self, sw):
        if self.game.tilt.status == False:
            self.tilt_actions()

    def replay_step_down(self, number=0):
        if number > 0:
            if number > 1:
                self.game.replays -= 1
                graphics.replay_step_down(self.game.replays, graphics.rodeo_1.reel1, graphics.rodeo_1.reel10, graphics.rodeo_1.reel100)
                self.game.coils.registerDown.pulse()
                number -= 1
                graphics.rodeo_1.display(self)
                self.delay(name="replay_reset", delay=0.13, handler=self.replay_step_down, param=number)
            elif number == 1:
                self.game.replays -= 1
                graphics.replay_step_down(self.game.replays, graphics.rodeo_1.reel1, graphics.rodeo_1.reel10, graphics.rodeo_1.reel100)
                self.game.coils.registerDown.pulse()
                number -= 1
                graphics.rodeo_1.display(self)
                self.cancel_delayed(name="replay_reset")
        else: 
            if self.game.replays > 0:
                self.game.replays -= 1
                graphics.replay_step_down(self.game.replays, graphics.rodeo_1.reel1, graphics.rodeo_1.reel10, graphics.rodeo_1.reel100)
                self.delay(name="display", delay=0.1, handler=graphics.rodeo_1.display, param=self)
            self.game.coils.registerDown.pulse()

    def replay_step_up(self):
        if self.game.replays < 899:
            self.game.replays += 1
            graphics.replay_step_up(self.game.replays, graphics.rodeo_1.reel1, graphics.rodeo_1.reel10, graphics.rodeo_1.reel100)
        self.game.coils.registerUp.pulse()
        self.game.reflex.increase()
        graphics.rodeo_1.display(self)

    def sw_green_active(self, sw):
        if self.game.ball_count.position >= 5:
            if self.game.eb.status == False:
                self.game.features.disengage()
                self.game.all_advantages.disengage()
                self.game.odds_only.disengage()
                self.game.spotting.spin()
                self.game.mixer1.spin()
                self.game.mixer2.spin()
                self.game.mixer3.spin()
                self.game.mixer4.spin()
                self.game.mixer5.spin()
                self.game.eb.engage(self.game)
                self.delay(name="display", delay=0.1, handler=graphics.rodeo_1.display, param=self)
                self.delay(name="green", delay=0.1, handler=self.sw_green_active, param=sw)
            if self.game.eb.status == True and (self.game.replays > 0 or self.game.switches.freeplay.is_active()):
                self.game.sound.stop('add')
                self.game.sound.play('add')
                self.game.cu = not self.game.cu
                self.game.spotting.spin()
                self.game.mixer1.spin()
                self.game.mixer2.spin()
                self.game.mixer3.spin()
                self.game.mixer4.spin()
                self.game.mixer5.spin()
                self.scan_eb()
                self.replay_step_down()
                self.game.reflex.decrease()
                self.game.eb.disengage()
                self.delay(name="display", delay=0.1, handler=graphics.rodeo_1.display, param=self)
            
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
        self.game.sound.stop_music()
        self.game.sound.play_music('search', -1)
        
        for i in range(0, 50):
            self.r = self.closed_search_relays(self.game.searchdisc.position, self.game.corners.status)
            self.game.searchdisc.spin()
            self.wipers = self.r[0]
            self.card = self.r[1]
            self.horizontal = self.r[2]
            self.vertical = self.r[3]
            self.diagonal = self.r[4]
            self.corners = self.r[5]
            self.supercard = self.r[6]

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
                        if self.game.selector.position >= self.card:
                            if s >= 3:
                                self.find_winner(s, self.card, self.horizontal, self.vertical, self.diagonal, self.game.odds.horizontal, self.game.odds.vertical, self.game.odds.diagonal, self.game.odds.four, self.game.odds.five, self.corners, self.supercard)
                                break

    def find_winner(self, relays, card, horizontal, vertical, diagonal, hodds, vodds, dodds, fourodds, fiveodds, corners, supercard):
        if self.game.search_index.status == False and self.game.replays < 899:
            if card == 1:
                if relays == 3:
                    if supercard == 1:
                        if self.game.super_card.position >= 4:
                            if self.game.card1_replay_counter.position < fourodds:
                                self.game.search_index.engage(self.game)
                                self.card1_replay_step_up(fourodds - self.game.card1_replay_counter.position)
                    elif supercard == 2:
                        if self.game.super_card.position == 8:
                            if self.game.card1_replay_counter.position < fourodds:
                                self.game.search_index.engage(self.game)
                                self.card1_replay_step_up(fourodds - self.game.card1_replay_counter.position)
                    elif self.game.three_as_four.status == True:
                        if self.game.card1_replay_counter.position < fourodds:
                            self.game.search_index.engage(self.game)
                            self.card1_replay_step_up(fourodds - self.game.card1_replay_counter.position)
                    elif horizontal == True:
                        if self.game.card1_replay_counter.position < hodds:
                            self.game.search_index.engage(self.game)
                            self.card1_replay_step_up(hodds - self.game.card1_replay_counter.position)
                    elif vertical == True:
                        if self.game.card1_replay_counter.position < vodds:
                            self.game.search_index.engage(self.game)
                            self.card1_replay_step_up(vodds - self.game.card1_replay_counter.position)
                    elif diagonal == True:
                        if self.game.card1_replay_counter.position < dodds:
                            self.game.search_index.engage(self.game)
                            self.card1_replay_step_up(dodds - self.game.card1_replay_counter.position)
                if relays == 4:
                    if corners and self.game.corners.status == True:
                        if self.game.corners_replay_counter.position < 200:
                            self.game.search_index.engage(self.game)
                            self.corners_replay_step_up(200 - self.game.corners_replay_counter.position)
                    else:
                        if not corners:
                            if self.game.four_as_five.status == True:
                                if self.game.card1_replay_counter.position < fiveodds:
                                    self.game.search_index.engage(self.game)
                                    self.card1_replay_step_up(fiveodds - self.game.card1_replay_counter.position)
                            elif self.game.card1_replay_counter.position < fourodds:
                                self.game.search_index.engage(self.game)
                                self.card1_replay_step_up(fourodds - self.game.card1_replay_counter.position)
                if relays == 5:
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

    def corners_replay_step_up(self, number):
        if number >= 1:
            self.game.corners_replay_counter.step()
            number -= 1
            self.replay_step_up()
            if self.game.replays == 899:
                number = 0
            self.delay(name="corners_replay_step_up", delay=0.1, handler=self.corners_replay_step_up, param=number)
        else:
            self.game.search_index.disengage()
            self.cancel_delayed(name="corners_replay_step_up")
            self.search()

    def name_replay_step_up(self, number):
        if number >= 1:
            self.game.name_replay_counter.step()
            number -= 1
            self.replay_step_up()
            if self.game.replays == 899:
                number = 0
            self.delay(name="name_replay_step_up", delay=0.1, handler=self.name_replay_step_up, param=number)
        else:
            self.game.search_index.disengage()
            self.cancel_delayed(name="name_replay_step_up")
            self.search()

    def closed_search_relays(self, rivets, c):
        # This function is critical, as it will determine which card is returned, etc.  I need to check the position of the
        # replay counter for the card. We will get a row back
        # that has the numbers on the position which will return the search relay connected.  When three out of the five relays
        # are connected, we get a winner!
        
        self.pos = {}
        # Card 1
        self.pos[0] = {}
        self.pos[1] = {9:1, 15:2, 4:3, 24:4, 6:5}
        self.pos[2] = {13:1, 19:2, 14:3, 20:4, 17:5}
        self.pos[3] = {1:1, 18:2, 16:3, 12:4, 8:5}
        self.pos[4] = {2:1, 22:2, 11:3, 21:4, 25:5}
        self.pos[5] = {10:1, 7:2, 23:3, 5:4, 3:5}
        self.pos[6] = {9:1, 13:2, 1:3, 2:4, 10:5}
        self.pos[7] = {15:1, 19:2, 18:3, 22:4, 7:5}
        self.pos[8] = {4:1, 14:2, 16:3, 11:4, 23:5}
        self.pos[9] = {24:1, 20:2, 12:3, 21:4, 5:5}
        self.pos[10] = {6:1, 17:2, 8:3, 25:4, 3:5}
        self.pos[11] = {9:1, 19:2, 16:3, 21:4, 3:5}
        self.pos[12] = {6:1, 20:2, 16:3, 22:4, 10:5}
        self.pos[13] = {9:1, 6:2, 10:3, 3:4}
        self.pos[14] = {}
        self.pos[15] = {19:1, 7:2, 20:3}
        self.pos[16] = {1:1, 10:2, 13:3}
        self.pos[17] = {22:1, 4:2, 21:3}
        self.pos[18] = {19:1, 1:2, 22:3}
        self.pos[19] = {7:1, 10:2, 4:3}
        self.pos[20] = {20:1, 13:2, 21:3}
        self.pos[21] = {19:1, 10:2, 21:3}
        self.pos[22] = {20:1, 10:2, 22:3}
        self.pos[23] = {}
        self.pos[24] = {23:1, 3:2, 18:3}
        self.pos[25] = {9:1, 25:2, 11:3}
        self.pos[26] = {12:1, 24:2, 14:3}
        self.pos[27] = {23:1, 9:2, 12:3}
        self.pos[28] = {3:1, 25:2, 24:3}
        self.pos[29] = {18:1, 11:2, 14:3}
        self.pos[30] = {23:1, 25:2, 14:3}
        self.pos[31] = {18:1, 25:2, 12:3}
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

        horizontal = False
        vertical = False
        diagonal = False
        corners = False
        sc = 0

        if rivets in range(0,6):
            horizontal = True
        if rivets in range(6,11):
            vertical = True
        if rivets in range(11,13):
            diagonal = True
        if rivets in range(15,23):
            sc = 1
        if rivets in range(24,32):
            sc = 2
        if rivets == 13:
            corners = True
        if rivets in range(0,50):
            card = 1

        return (self.pos[rivets], card, horizontal, vertical, diagonal, corners, sc)
    
    def scan_all(self):
        #Animate scanning of everything - this happens through the spotting disc
        self.all_probability()

    def all_probability(self):
        mix1 = self.game.mixer1.connected_rivet()
        if self.game.reflex.connected_rivet() == 0 and (mix1 in [1,6,8,11,13,16,18,22,24]):
            self.scan_odds()
            self.scan_features()
            self.scan_eb()
        elif self.game.reflex.connected_rivet() == 1 and (mix1 not in [2,5,7,9,12,14,15,19,23]):
            self.scan_odds()
            self.scan_features()
            self.scan_eb()
        elif self.game.reflex.connected_rivet() == 2 and (mix1 not in [5,9,12,15,19,23]):
            self.scan_odds()
            self.scan_features()
            self.scan_eb()
        elif self.game.reflex.connected_rivet() == 3 and (mix1 not in [5,9,15,23]):
            self.scan_odds()
            self.scan_features()
            self.scan_eb()
        elif self.game.reflex.connected_rivet() == 4:
            self.scan_odds()
            self.scan_features()
            self.scan_eb()
        else:
            if self.game.odds.position == 0:
                self.game.odds.step()
            s = random.randint(1,10)
            self.animate_odds_scan(s)
            s = random.randint(1,5)
            self.animate_feature_scan(s)
            s = random.randint(1,24)
            self.animate_eb_scan(s)

    def scan_odds(self):
        s = random.randint(1,10)
        self.animate_odds_scan(s)
        p = self.odds_probability()
        if p == 1:
            es = self.check_extra_step()
            if es == 1:
                i = random.randint(1,3)
                self.extra_step(i)
            else:
                self.game.odds.step()

    def extra_step(self, number):
        if number > 0:
            self.game.odds.step()
            self.game.coils.counter.pulse()
            self.delay(name="display", delay=0.1, handler=graphics.rodeo_1.display, param=self)
            number -= 1
            self.delay(name="extra_step", delay=0.1, handler=self.extra_step, param=number)

    def check_extra_step(self):
        i = random.randint(0,32)
        if i == 16:
            return 1
        else:
            return 0

    def odds_probability(self):
        mix5 = self.game.mixer5.connected_rivet()
        # Check position of Mixer 5, Mixer 4, and Mixer 3 and current 
        # position of the odds, along with trip relays.
        # For first check, guaranteed single stepup.  Probability doesn't 
        # factor, so I will return as part of the initial check above.
        if self.game.odds.position == 0:
            return 1
        if self.game.odds_only.status == True:
            if self.game.odds.position < 4:
                return 1
        else:
            m2 = self.check_mixer2()
            if m2 == True:
                if self.game.odds.position < 4:
                    return 1
                else:
                    s = self.check_sd()
                    if s == 1:
                        return 1
                    else:
                        return 0
            else:
                return 0



    def check_sd(self):
        sd = self.game.spotting.connected_rivet()
        if self.game.odds.position in [4,5]:
            if sd in [4,6,8,9,11,12,13,19,20,22,23,25,27,29,32,35,36,38,41,45,48,50]:
                return 1
            else:
                return 0
        elif self.game.odds.position == 6:
            if sd in [2,3,14,17,24,31,39,40,46,47]:
                return 1
            else:
                return 0
        elif self.game.odds.position == 7:
            if sd in [5,7,16,26,34,37,42]:
                return 1
            else:
                return 0
        elif self.game.odds.position == 8:
            if sd in [10,16,28,44]:
                return 1
            else:
                return 0
        elif self.game.odds.position == 9:
            if sd in [18,30,43]:
                return 1
            else:
                return 0
        else:
            return 0

    def check_mixer2(self):
        mix2 = self.game.mixer2.connected_rivet()
        if mix2 in [1,3,4,8,9,10,13,15,16,18,19,20]:
            return 1
        else:
            return 0

    def check_mixer3(self):
        mix3 = self.game.mixer3.connected_rivet()
        if self.game.red_star.status == False and self.game.yellow_star.status == False and self.game.sixteen.status == False:
            return 1
        elif self.game.yellow_star.status == True:
            if mix3 in [3,6,16,24]:
                return 0
        elif self.game.sixteen.status == True:
            if mix3 in [2,5,8,11]:
                return 0
        elif self.game.red_star.status == True:
            if mix3 in [2,4,5,6,8,10,11,12,16,20,24]:
                return 0
        else:
            return 1

    def check_mixer4(self):
        mix4 = self.game.mixer4.connected_rivet()
        if self.game.super_card < 8:
            if mix4 in [4,5,11,14,18]:
                return 1
        elif self.game.super_card < 4:
            if mix4 in [6,8,10,15,16]:
                return 1
        elif mix4 not in [4,5,6,8,10,11,14,15,16,18]:
            return 1
        else:
            return 0

    def scan_features(self):
        p = self.features_probability()

    def features_probability(self):
        s = random.randint(1,5)
        self.animate_feature_scan(s)
        mix2 = self.game.mixer2.connected_rivet()
        mix3 = self.game.mixer3.connected_rivet()
        if self.game.odds.position < 5:
            spots = self.check_spot()
            m4 = self.spot_mixer4()
        elif self.game.odds.position == 5:
            if mix2 not in [5,8,14,15,20]:
                spots = self.check_spot()
                m4 = self.spot_mixer4()
        elif self.game.odds.position == 6:
            if mix3 not in [1,5,6,9,12,15,19,22]:
                spots = self.check_spot()
                m4 = self.spot_mixer4()
        elif self.game.odds.position in [7,8]:
            if mix3 not in [3,5,8,9,10,15,18,19,22]:
                spots = self.check_spot()
                m4 = self.spot_mixer4()
        elif self.game.odds.position >= 9:
            if mix3 in [1,6,9,13,18,22]:
                spots = self.check_spot()
                m4 = self.spot_mixer4()
        n = self.check_name()
        if n == True:
            self.game.liteaname.engage(self.game)
        o = self.check_three_as_four()
        if o == True:
            self.game.three_as_four.engage(self.game)
        p = self.check_four_as_five()
        if p == True:
            self.game.four_as_five.engage(self.game)

    def check_three_as_four(self):
        i = random.randint(0,32)
        if i == 8:
            return 1
        else:
            return 0

    def check_four_as_five(self):
        i = random.randint(0,32)
        if i == 8:
            return 1
        else:
            return 0

    def check_name(self):
        i = random.randint(0,32)
        if i == 8:
            return 1
        else:
            return 0

    def spot_mixer4(self):
        mix4 = self.game.mixer4.connected_rivet()
        if self.game.cu == True:
            if mix4 in [16,12,24]:
                if self.game.corners.status == False:
                    self.game.corners.engage(self.game)
            elif mix4 in [1,3,4,5,8,9,10,11,13,15,17,18,20,23]:
                if self.game.super_card.position < 8:
                    self.game.super_card.step()

    def check_spot(self):
        sd = self.game.spotting.connected_rivet()
        mix5 = self.game.mixer5.connected_rivet()
        if self.game.cu == 1:
            if sd in [1,3,5,13,16,17,19,27,39]:
                if self.game.red_star.status == False:
                    self.game.red_star.engage(self.game)
                    self.game.coils.yellowROLamp.enable()
            elif sd in [7,11,24,29,30,32,43,46,49]:
                if self.game.yellow_star.status == False:
                    self.game.yellow_star.engage(self.game)
                    self.game.coils.redROLamp.enable()
            elif sd in [14,36,31]:
                if self.game.sixteen.status == False:
                    self.game.sixteen.engage(self.game)
                    if 16 not in self.holes:
                        self.holes.append(16)
            elif sd in [20,40,42,47]:
                if self.game.five.status == False:
                    self.game.five.engage(self.game)
                    if 5 not in self.holes:
                        self.holes.append(5)
            elif sd in [12,25,37]:
                if self.game.seventeen.status == False:
                    self.game.seventeen.engage(self.game)
                    if 17 not in self.holes:
                        self.holes.append(17)
            elif sd in [4,9,33,43]:
                if self.game.two.status == False:
                    self.game.two.engage(self.game)
                    if 2 not in self.holes:
                        self.holes.append(2)
            elif sd in [23,26,41]:
                if self.game.fifteen.status == False:
                    self.game.fifteen.engage(self.game)
                    if 15 not in self.holes:
                        self.holes.append(15)
            elif sd in [2,18,28,38,40,6,44,8,10,15,21,22,34,35,50]:
                if self.game.super_card.position < 3:
                    number = 3 - self.game.super_card.position
                    self.step_super(number)
                elif self.game.super_card.position > 3:
                    number = 7 - self.game.super_card.position
                    self.step_super(number)

    def step_super(self, number):
        if number >= 1:
            self.game.super_card.step()
            number -= 1
            self.delay(name="display", delay=0.1, handler=graphics.rodeo_1.display, param=self)
            self.delay(name="step_super", delay=0.1, handler=self.step_super, param=number)

    def scan_eb(self):
        s = random.randint(1,24)
        self.animate_eb_scan(s)
        p = self.eb_probability()
        if p == 1:
            if self.game.extra_ball.position < 24:
                self.game.extra_ball.step()
                self.check_lifter_status()
                # Timer resets to 0 position on ball count increasing.  We are fudging this since we will have
                # no good way to measure balls as they return back to the trough.  The ball count unit cannot be
                # relied upon as we do not have a switch in the outhole, and the trough logic is too complex for
                # the task at hand.
                # TODO: implement thunk noises into the units.py to automatically play the noises.
                self.game.timer.reset()
        else:
            # TODO: play thunk noise of EB search bearing no fruit.
            pass
        self.delay(name="display", delay=0.1, handler=graphics.rodeo_1.display, param=self)

    def animate_odds_scan(self, s):
        if s > 1:
            self.delay(name="odds_animation", delay=0.1, handler=graphics.rodeo_1.odds_animation, param=s)
            self.delay(name="display", delay=0.1, handler=graphics.rodeo_1.display, param=self)
            s -= 1
            #self.delay(name="animate_odds", delay=0.1, handler=self.animate_odds_scan, param=s)
        else:
            self.cancel_delayed(name="odds_animation")
            self.cancel_delayed(name="display")

    def animate_feature_scan(self, s):
        if s > 1:
            self.delay(name="feature_animation", delay=0.1, handler=graphics.rodeo_1.feature_animation, param=s)
            self.delay(name="display", delay=0.1, handler=graphics.rodeo_1.display, param=self)
            s -= 1
            #self.delay(name="animate_feature", delay=0.1, handler=self.animate_feature_scan, param=s)
        else:
            self.delay(name="display", delay=0.1, handler=graphics.rodeo_1.display, param=self)

    def animate_eb_scan(self, s):
        if s > 1:
            self.delay(name="eb_animation", delay=0.1, handler=graphics.rodeo_1.eb_animation, param=s)
            self.delay(name="display", delay=0.1, handler=graphics.rodeo_1.display, param=self)
            s -= 1
            #self.delay(name="animate_eb", delay=0.1, handler=self.animate_eb_scan, param=s)
        else:
            self.delay(name="display", delay=0.1, handler=graphics.rodeo_1.display, param=self)

    def eb_probability(self):
        sd = self.game.spotting.connected_rivet()
        mix2 = self.game.mixer2.connected_rivet()
        mix3 = self.game.mixer3.connected_rivet()
        eb = self.game.extra_ball.position
        if eb == 0:
            self.game.extra_ball.step()
            self.check_lifter_status()
            self.delay(name="display", delay=0.1, handler=graphics.rodeo_1.display, param=self)

        if self.game.odds.position <= 4:
            if sd in [10,11,20,21,25,28,29,30,32,33,34,40,45,49]:
                self.game.extra_ball.step()
                self.check_lifter_status()
                self.delay(name="display", delay=0.1, handler=graphics.rodeo_1.display, param=self)
        else:
            if mix2 in [2,5,6,7,11,12,14,17,21,22,23,24]:
                if self.game.odds.position == 5:
                    m2 = self.check_mixer2()
                    if m2 == 1:
                        self.eb_check()
                elif self.game.odds.position == 6:
                    if mix3 in [2,3,4,7,8,10,11,13,14,16,17,18,20,21,23,24]:
                        self.eb_check()
                elif self.game.odds.position in [7,8]:
                    if mix3 in [1,2,4,6,7,12,13,14,16,17,20,21,23,24]:
                        self.eb_check()
                elif self.game.odds.position >= 9:
                    if mix3 in [1,6,9,13,18,22]:
                        self.eb_check()


    def eb_check(self):
        #There are three rivets documented that will run the EB run relay with
        #a 1/3 closed switch on the control unit - while that switch is closed,
        #the EB stepper will step.  I don't have the 1/3 switch emulated.  
        #I'll see how big of a problem this is in reality.  Only really happens
        #on SD positions 26 27 38 and 39.  Probably not a big deal.  It does a
        #run to the top, from what I can tell.  This run to the top works 
        #through another connection, too.
        sd = self.game.spotting.connected_rivet()
        eb = self.game.extra_ball.position

        if sd in [8,45,11,21,28,44,9,36]:
            if eb < 3:
                self.game.extra_ball.step()
                self.check_lifter_status()
                self.delay(name="display", delay=0.1, handler=graphics.rodeo_1.display, param=self)
        elif sd in [11,21,28]:
            if eb > 3 and eb <= 6:
                self.game.extra_ball.step()
                self.check_lifter_status()
                self.delay(name="display", delay=0.1, handler=graphics.rodeo_1.display, param=self)
        elif sd == 44:
            self.game.spotting.spin()
            sd2 = self.game.spotting.connected_rivet()
            if sd2 in [2,3,4,16,17,24,43,44]:
                if eb <= 7:
                    number = 7 - self.game.extra_ball.position
                    self.step_eb(number)
                elif eb >= 8 and eb < 15:
                    number = 15 - self.game.extra_ball.position
                    self.step_eb(number)
                elif eb >= 16 and eb < 23:
                    number = 23 - self.game.extra_ball.position
                    self.step_eb(number)
        elif sd in [9,36]:
            self.game.spotting.spin()
            sd2 = self.game.spotting.connected_rivet()
            if sd2 in [9,19,31,36,42,48]:
                if eb < 5:
                    number = 5 - self.game.extra_ball.position
                    self.step_eb(number)
                elif eb >= 8 and eb < 13:
                    number = 13 - self.game.extra_ball.position
                    self.step_eb(number)
                elif eb >= 16 and eb < 21:
                    number = 21 - self.game.extra_ball.position
                    self.step_eb(number)
            elif sd == 37:
                self.game.spotting.spin()
                self.game.mixer3.spin()
                sd2 = self.game.spotting.connected_rivet()
                mix32 = self.game.mixer3.connected_rivet()
                if mix32 in [2,5,14,17]:
                    if sd2 in [1,5,6,7,12,13,14,15,18,22,23,35,37,41,46,47,50]:
                        if eb < 8:
                            number = 8 - self.game.extra_ball.position
                            self.step_eb(number)
                        elif eb < 16:
                            number = 16 - self.game.extra_ball.position
                            self.step_eb(number)
                        elif eb < 24:
                            number = 24 - self.game.extra_ball.position
                            self.step_eb(number)

                elif sd == 26:
                    self.game.mixer3.spin()
                    mix32 = self.game.mixer3.connected_rivet()
                    if mix32 in [6,7,18,19]:
                        self.game.extra_ball.step()
                        self.check_lifter_status()
                        self.delay(name="display", delay=0.1, handler=graphics.rodeo_1.display, param=self)

    def step_eb(self, number):
        if number >= 1:
            self.game.extra_ball.step()
            self.check_lifter_status()
            number -= 1
            self.delay(name="display", delay=0.1, handler=graphics.rodeo_1.display, param=self)
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

class Rodeo1(procgame.game.BasicGame):
    """ Rodeo was never produced in quantity. """
    def __init__(self, machine_type):
        super(Rodeo1, self).__init__(machine_type)
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

        self.searchdisc = units.Search("searchdisc", 49)

        #Search relays
        self.s1 = units.Relay("s1")
        self.s2 = units.Relay("s2")
        self.s3 = units.Relay("s3")
        self.s4 = units.Relay("s4")
        self.s5 = units.Relay("s5")
        self.search_index = units.Relay("search_index")

        #Odds stepper
        self.odds = units.Stepper("odds", 10, 'rodeo_1')

        #Replay Counter
        self.card1_replay_counter = units.Stepper("card1_replay_counter", 200)
        #Corners Replay Counter
        self.corners_replay_counter = units.Stepper("corners_replay_counter", 200)
        self.name_replay_counter = units.Stepper("name_replay_counter", 200)

        #Initialize stepper units used to keep track of features or timing.
        self.timer = units.Stepper("timer", 40)
        self.ball_count = units.Stepper("ball_count", 8)

        # Initialize reflex(es) and mixers unique to this game
        self.reflex = units.Reflex("primary", 100)

        #This is a disc which has 50 positions
        #and will randomly complete paths through the various mixers to allow for odds or feature step.
        self.spotting = units.Spotting("spotting", 50)

        #Check for status of the replay register zero switch.  If positive
        #and machine is just powered on, this will zero out the replays.
        self.replay_reset = units.Relay("replay_reset")
        
        #Extra ball unit contains 24 positions.
        self.extra_ball = units.Stepper("extra_ball", 24)

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

        #Need to define relays for playing odds, features, eb, and all
        self.all_advantages = units.Relay("all_advantages")
        self.eb = units.Relay("eb")
        self.features = units.Relay("features")
        self.odds_only = units.Relay("odds_only")

        #Relay for corners lighting
        self.corners = units.Relay("corners")

        #Super cards are triggered through an 8 position stepper
        self.super_card = units.Stepper("super_card", 8)

        self.selector = units.Stepper("selector", 1)

        #Some special trip relays for spotted numbers and rollovers
        self.red_star = units.Relay("red_star")
        self.yellow_star = units.Relay("yellow_star")
        self.sixteen = units.Relay("sixteen")
        self.five = units.Relay("five")
        self.seventeen = units.Relay("seventeen")
        self.two = units.Relay("two")
        self.fifteen = units.Relay("fifteen")
        self.liteaname = units.Relay("liteaname")
        self.eight_balls = units.Relay("eight_balls")
        self.three_as_four = units.Relay("three_as_four")
        self.four_as_five = units.Relay("four_as_five")

        self.name = units.Stepper("name", 5)

        self.replays = 0
        self.returned = False

    def reset(self):
        super(Rodeo1, self).reset()
        self.logger = logging.getLogger('game')
        self.load_config('bingo.yaml')
        
        main_mode = SinglecardBingo(self)
        self.modes.add(main_mode)
        
game = Rodeo1(machine_type='pdb')
game.reset()
game.run_loop()
