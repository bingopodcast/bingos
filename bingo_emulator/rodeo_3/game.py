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
from bingo_emulator.graphics.rodeo_3 import *

class MulticardBingo(procgame.game.Mode):
    def __init__(self, game):
        super(MulticardBingo, self).__init__(game=game, priority=5)
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
        self.game.sound.register_sound('coin1', "audio/united_coin1.wav")
        self.game.sound.register_sound('coin2', "audio/united_coin2.wav")
        self.game.sound.register_sound('coin3', "audio/united_coin3.wav")
        self.game.sound.register_sound('tilt', "audio/tilt.wav")
        self.game.sound.register_sound('step', "audio/step.wav")
        self.game.sound.register_sound('eb_search', "audio/EB_Search.wav")

    def sw_coin_active(self, sw):
        if self.game.eb_play.status == True and self.game.tilt.status == False:
            self.cancel_delayed("eb_animation")
            self.regular_play()
            graphics.rodeo_3.display(self)
            self.game.eb_play.disengage()
        else:
            self.game.tilt.disengage()
            self.regular_play()
        self.delay(name="display", delay=0.1, handler=graphics.rodeo_3.display, param=self)

    def sw_startButton_active(self, sw):
        self.game.eb_play.disengage()
        if self.game.replays > 0 or self.game.switches.freeplay.is_active():
            self.game.tilt.disengage()
            self.regular_play()
            self.delay(name="display", delay=0.1, handler=graphics.rodeo_3.display, param=self)

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

    def sw_enter_active(self, sw):
        if self.game.switches.left.is_active() and self.game.switches.right.is_active():
            self.game.end_run_loop()
            os.system("/home/nbaldridge/proc/bingo_emulator/start_game.sh rodeo_3")

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
        self.cancel_delayed(name="card1_replay_step_up")
        self.cancel_delayed(name="card2_replay_step_up")
        self.cancel_delayed(name="card3_replay_step_up")
        self.cancel_delayed(name="timeout")
        self.game.search_index.disengage()
        self.game.coils.counter.pulse()

        self.game.returned = False
        r = random.randint(1,3)
        if r == 1:
            self.game.sound.play('coin1')
        elif r == 2:
            self.game.sound.play('coin2')
        elif r == 3:
            self.game.sound.play('coin3')
        if self.game.start.status == True:
            if self.game.selector.position < 3:
                self.game.selector.step()
            if self.game.switches.shutter.is_inactive():
                self.game.coils.shutter.enable()
            self.game.cu = not self.game.cu
            self.game.reflex1.step()
            self.game.reflex2.step()
            
            current = self.game.flash.connected_rivet()
            self.game.flash.spin()
            new = self.game.flash.connected_rivet()
            if self.game.eb_play.status == False:
                self.animate_both([current,self.game.flash.movement_amount,1])
            self.replay_step_down()
            graphics.rodeo_3.display(self)
            self.check_lifter_status()
        else:
            if self.game.eb_play.status == True:
                self.game.cu = not self.game.cu
                self.game.reflex1.step()
                self.game.reflex2.step()
                
                current = self.game.flash.connected_rivet()
                self.game.flash.spin()
                new = self.game.flash.connected_rivet()
                self.animate_eb_scan([current,self.game.flash.movement_amount,self.game.flash.movement_amount])
                self.replay_step_down()
                graphics.rodeo_3.display(self)
                self.check_lifter_status()
            else:
                self.holes = []
                self.game.start.engage(self.game)
                self.game.card1_replay_counter.reset()
                self.game.card2_replay_counter.reset()
                self.game.card3_replay_counter.reset()
                self.game.c1_double.disengage()
                self.game.c2_double.disengage()
                self.game.c3_double.disengage()
                self.game.all_double.disengage()
                self.game.c1_triple.disengage()
                self.game.c2_triple.disengage()
                self.game.c3_triple.disengage()
                self.game.all_triple.disengage()
                self.game.sixteen.disengage()
                self.game.fifteen.disengage()
                self.game.fourteen.disengage()
                self.game.nineteen.disengage()
                self.game.seventeen.disengage()
                self.game.twentytwo.disengage()
                self.game.fss.disengage()
                self.game.fnt.disengage()
                self.game.start.engage(self.game)
                self.game.selector.reset()
                self.game.timer.reset()
                self.game.ball_count.reset()
                self.game.extra_ball.reset()
                self.game.sound.stop_music()
                self.regular_play()
        self.delay(name="display", delay=0.1, handler=graphics.rodeo_3.display, param=self)
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
                            if self.game.extra_ball.position >= 9 and self.game.ball_count.position <= 5:
                                if self.game.switches.shooter.is_open() and self.game.switches.trough3.is_closed():
                                    self.game.coils.lifter.enable()
                        if self.game.switches.trough3.is_open():
                            if self.game.extra_ball.position >= 18 and self.game.ball_count.position <= 6:
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
                if self.game.ball_count.position == 5 and self.game.extra_ball.position >= 9:
                    self.game.coils.lifter.enable()
                if self.game.ball_count.position == 6 and self.game.extra_ball.position >= 18:
                    self.game.coils.lifter.enable()
                if self.game.ball_count.position == 7 and self.game.extra_ball.position >= 24:
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
            if self.game.search_index.status == False:
                self.search()
        if self.game.ball_count.position <= 7:
            self.check_lifter_status()

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
            self.delay(name="display", delay=0.1, handler=graphics.rodeo_3.display, param=self)

    def sw_hole2_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(2)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.rodeo_3.display, param=self)

    def sw_hole3_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(3)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.rodeo_3.display, param=self)

    def sw_hole4_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(4)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.rodeo_3.display, param=self)

    def sw_hole5_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(5)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.rodeo_3.display, param=self)

    def sw_hole6_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(6)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.rodeo_3.display, param=self)

    def sw_hole7_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(7)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.rodeo_3.display, param=self)

    def sw_hole8_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(8)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.rodeo_3.display, param=self)

    def sw_hole9_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(9)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.rodeo_3.display, param=self)

    def sw_hole10_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(10)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.rodeo_3.display, param=self)

    def sw_hole11_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(11)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.rodeo_3.display, param=self)

    def sw_hole12_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(12)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.rodeo_3.display, param=self)

    def sw_hole13_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(13)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.rodeo_3.display, param=self)

    def sw_hole14_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(14)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.rodeo_3.display, param=self)

    def sw_hole15_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(15)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.rodeo_3.display, param=self)

    def sw_hole16_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(16)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.rodeo_3.display, param=self)

    def sw_hole17_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(17)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.rodeo_3.display, param=self)

    def sw_hole18_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(18)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.rodeo_3.display, param=self)

    def sw_hole19_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(19)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.rodeo_3.display, param=self)

    def sw_hole20_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(20)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.rodeo_3.display, param=self)

    def sw_hole21_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(21)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.rodeo_3.display, param=self)

    def sw_hole22_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(22)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.rodeo_3.display, param=self)

    def sw_hole23_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(23)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.rodeo_3.display, param=self)

    def sw_hole24_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(24)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.rodeo_3.display, param=self)

    def sw_hole25_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(25)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.rodeo_3.display, param=self)
    
    def sw_replayReset_active(self, sw):
        self.game.anti_cheat.disengage()
        self.holes = []
        graphics.rodeo_3.display(self)
        self.tilt_actions()
        self.replay_step_down(self.game.replays)

    def tilt_actions(self):
        self.game.start.disengage()
        self.cancel_delayed(name="replay_reset")
        self.cancel_delayed(name="card1_replay_step_up")
        self.cancel_delayed(name="card2_replay_step_up")
        self.cancel_delayed(name="card3_replay_step_up")
        self.cancel_delayed(name="timeout")
        self.game.search_index.disengage()
        if self.game.switches.shutter.is_active() and self.game.ball_count.position == 0:
            self.game.coils.shutter.enable()
        self.holes = []
        self.game.selector.reset()
        self.game.extra_ball.reset()
        self.game.c1_double.disengage()
        self.game.c2_double.disengage()
        self.game.c3_double.disengage()
        self.game.all_double.disengage()
        self.game.c1_triple.disengage()
        self.game.c2_triple.disengage()
        self.game.c3_triple.disengage()
        self.game.all_triple.disengage()
        self.game.sixteen.disengage()
        self.game.fifteen.disengage()
        self.game.fourteen.disengage()
        self.game.nineteen.disengage()
        self.game.seventeen.disengage()
        self.game.twentytwo.disengage()
        self.game.fss.disengage()
        self.game.fnt.disengage()
        self.game.ball_count.reset()
        self.game.anti_cheat.engage(game)
        self.game.eb_play.disengage()
        self.game.tilt.engage(self.game)
        self.game.sound.stop_music()
        self.game.sound.play('tilt')
        # displays "Tilt" on the backglass, you have to recoin.
        self.delay(name="display", delay=0.1, handler=graphics.rodeo_3.display, param=self)

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
                graphics.replay_step_down(self.game.replays, graphics.rodeo_3.reel1, graphics.rodeo_3.reel10, graphics.rodeo_3.reel100)
                self.game.coils.registerDown.pulse()
                number -= 1
                graphics.rodeo_3.display(self)
                self.delay(name="replay_reset", delay=0.13, handler=self.replay_step_down, param=number)
            elif number == 1:
                self.game.replays -= 1
                graphics.replay_step_down(self.game.replays, graphics.rodeo_3.reel1, graphics.rodeo_3.reel10, graphics.rodeo_3.reel100)
                self.game.coils.registerDown.pulse()
                number -= 1
                graphics.rodeo_3.display(self)
                self.cancel_delayed(name="replay_reset")
        else: 
            if self.game.replays > 0:
                self.game.replays -= 1
                graphics.replay_step_down(self.game.replays, graphics.rodeo_3.reel1, graphics.rodeo_3.reel10, graphics.rodeo_3.reel100)
                self.delay(name="display", delay=0.1, handler=graphics.rodeo_3.display, param=self)
            self.game.coils.registerDown.pulse()

    def replay_step_up(self):
        if self.game.replays < 899:
            self.game.replays += 1
            graphics.replay_step_up(self.game.replays, graphics.rodeo_3.reel1, graphics.rodeo_3.reel10, graphics.rodeo_3.reel100)
        self.game.coils.registerUp.pulse()
        self.game.coils.bell.pulse()
        self.game.reflex1.stepdown()
        graphics.rodeo_3.display(self)

    def sw_yellow_active(self, sw):
         if self.game.ball_count.position >= 4:
            if self.game.eb_play.status == False:
                self.game.eb_play.engage(self.game)
                self.delay(name="display", delay=0.1, handler=graphics.rodeo_3.display, param=self)
            if self.game.eb_play.status == True and (self.game.replays > 0 or self.game.switches.freeplay.is_active()):
                self.regular_play()
                self.delay(name="display", delay=0.1, handler=graphics.rodeo_3.display, param=self)
                self.game.eb_play.disengage()
                self.delay(name="display", delay=0.1, handler=graphics.rodeo_3.display, param=self)
                return

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
        # Replay counters also need to be implemented to prevent the supplemental searches from scoring.

        if self.game.search_index.status == False:
            for i in range(0, 50):
                self.r = self.closed_search_relays(self.game.searchdisc.position)
                self.game.searchdisc.spin()
                self.wipers = self.r[0]
                self.card = self.r[1]

                # From here, I need to determine based on the value of r, whether to latch the search index and scores.  
                #I need to determine the best winner on each card.  To do this, I must compare the position of the replay counter before
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
                                    self.find_winner(s, self.game.selector.position, self.card)
                                    break

    def find_winner(self, relays, selector, card):
        if self.game.search_index.status == False and self.game.replays < 899:
            if selector >= 1:
                if card == 1:
                    if relays == 3:
                        if self.game.c1_double.status == True:
                            if self.game.card1_replay_counter.position < 8:
                                self.game.search_index.engage(self.game)
                                self.card1_replay_step_up(8 - self.game.card1_replay_counter.position)
                        elif self.game.c1_triple.status == True:
                            if self.game.card1_replay_counter.position < 12:
                                self.game.search_index.engage(self.game)
                                self.card1_replay_step_up(12 - self.game.card1_replay_counter.position)
                        else:
                            if self.game.card1_replay_counter.position < 4:
                                self.game.search_index.engage(self.game)
                                self.card1_replay_step_up(4 - self.game.card1_replay_counter.position)
                    if relays == 4:
                        if self.game.c1_double.status == True:
                            if self.game.card1_replay_counter.position < 40:
                                self.game.search_index.engage(self.game)
                                self.card1_replay_step_up(40 - self.game.card1_replay_counter.position)
                        elif self.game.c1_triple.status == True:
                            if self.game.card1_replay_counter.position < 60:
                                self.game.search_index.engage(self.game)
                                self.card1_replay_step_up(60 - self.game.card1_replay_counter.position)
                        elif self.game.card1_replay_counter.position < 20:
                            self.game.search_index.engage(self.game)
                            self.card1_replay_step_up(20 - self.game.card1_replay_counter.position)
                    if relays == 5:
                        if self.game.c1_double.status == True:
                            if self.game.card1_replay_counter.position < 200:
                                self.game.search_index.engage(self.game)
                                self.card1_replay_step_up(200 - self.game.card1_replay_counter.position)
                        elif self.game.c1_triple.status == True:
                            if self.game.card1_replay_counter.position < 300:
                                self.game.search_index.engage(self.game)
                                self.card1_replay_step_up(300 - self.game.card1_replay_counter.position)
                        elif self.game.card1_replay_counter.position < 100:
                            self.game.search_index.engage(self.game)
                            self.card1_replay_step_up(100 - self.game.card1_replay_counter.position)
            if selector >= 2:
                if card == 2:
                    if relays == 3:
                        if self.game.c2_double.status == True:
                            if self.game.card2_replay_counter.position < 8:
                                self.game.search_index.engage(self.game)
                                self.card2_replay_step_up(8 - self.game.card2_replay_counter.position)
                        elif self.game.c2_triple.status == True:
                            if self.game.card2_replay_counter.position < 12:
                                self.game.search_index.engage(self.game)
                                self.card2_replay_step_up(12 - self.game.card2_replay_counter.position)
                        else:
                            if self.game.card2_replay_counter.position < 4:
                                self.game.search_index.engage(self.game)
                                self.card2_replay_step_up(4 - self.game.card2_replay_counter.position)
                    if relays == 4:
                        if self.game.c2_double.status == True:
                            if self.game.card2_replay_counter.position < 40:
                                self.game.search_index.engage(self.game)
                                self.card2_replay_step_up(40 - self.game.card2_replay_counter.position)
                        elif self.game.c2_triple.status == True:
                            if self.game.card2_replay_counter.position < 60:
                                self.game.search_index.engage(self.game)
                                self.card2_replay_step_up(60 - self.game.card2_replay_counter.position)
                        elif self.game.card2_replay_counter.position < 20:
                            self.game.search_index.engage(self.game)
                            self.card2_replay_step_up(20 - self.game.card2_replay_counter.position)
                    if relays == 5:
                        if self.game.c2_double.status == True:
                            if self.game.card2_replay_counter.position < 200:
                                self.game.search_index.engage(self.game)
                                self.card2_replay_step_up(200 - self.game.card2_replay_counter.position)
                        elif self.game.c2_triple.status == True:
                            if self.game.card2_replay_counter.position < 300:
                                self.game.search_index.engage(self.game)
                                self.card2_replay_step_up(300 - self.game.card2_replay_counter.position)
                        elif self.game.card2_replay_counter.position < 100:
                            self.game.search_index.engage(self.game)
                            self.card2_replay_step_up(100 - self.game.card2_replay_counter.position)
            if selector >= 3:
                if card == 3:
                    if relays == 3:
                        if self.game.c3_double.status == True:
                            if self.game.card3_replay_counter.position < 8:
                                self.game.search_index.engage(self.game)
                                self.card3_replay_step_up(8 - self.game.card3_replay_counter.position)
                        elif self.game.c3_triple.status == True:
                            if self.game.card3_replay_counter.position < 12:
                                self.game.search_index.engage(self.game)
                                self.card3_replay_step_up(12 - self.game.card3_replay_counter.position)
                        else:
                            if self.game.card3_replay_counter.position < 4:
                                self.game.search_index.engage(self.game)
                                self.card3_replay_step_up(4 - self.game.card3_replay_counter.position)
                    if relays == 4:
                        if self.game.c3_double.status == True:
                            if self.game.card3_replay_counter.position < 40:
                                self.game.search_index.engage(self.game)
                                self.card3_replay_step_up(40 - self.game.card3_replay_counter.position)
                        elif self.game.c3_triple.status == True:
                            if self.game.card3_replay_counter.position < 60:
                                self.game.search_index.engage(self.game)
                                self.card3_replay_step_up(60 - self.game.card3_replay_counter.position)
                        elif self.game.card3_replay_counter.position < 20:
                            self.game.search_index.engage(self.game)
                            self.card3_replay_step_up(20 - self.game.card3_replay_counter.position)
                    if relays == 5:
                        if self.game.c3_double.status == True:
                            if self.game.card3_replay_counter.position < 200:
                                self.game.search_index.engage(self.game)
                                self.card3_replay_step_up(200 - self.game.card3_replay_counter.position)
                        elif self.game.c3_triple.status == True:
                            if self.game.card3_replay_counter.position < 300:
                                self.game.search_index.engage(self.game)
                                self.card3_replay_step_up(300 - self.game.card3_replay_counter.position)
                        elif self.game.card3_replay_counter.position < 100:
                            self.game.search_index.engage(self.game)
                            self.card3_replay_step_up(100 - self.game.card3_replay_counter.position)

    def card1_replay_step_up(self, number):
        self.game.sound.stop_music()
        if number >= 1:
            self.game.card1_replay_counter.step()
            number -= 1
            self.replay_step_up()
            if self.game.replays == 899:
                number = 0
            self.delay(name="card1_replay_step_up", delay=0.25, handler=self.card1_replay_step_up, param=number)
        else:
            self.game.search_index.disengage()
            self.cancel_delayed(name="card1_replay_step_up")
            self.search_sounds()
            self.search()
       
    def card2_replay_step_up(self, number):
        self.game.sound.stop_music()
        if number >= 1:
            self.game.card2_replay_counter.step()
            number -= 1
            self.replay_step_up()
            if self.game.replays == 899:
                number = 0
            self.delay(name="card2_replay_step_up", delay=0.25, handler=self.card2_replay_step_up, param=number)
        else:
            self.game.search_index.disengage()
            self.cancel_delayed(name="card2_replay_step_up")
            self.search_sounds()
            self.search()

    def card3_replay_step_up(self, number):
        self.game.sound.stop_music()
        if number >= 1:
            self.game.card3_replay_counter.step()
            number -= 1
            self.replay_step_up()
            if self.game.replays == 899:
                number = 0
            self.delay(name="card3_replay_step_up", delay=0.25, handler=self.card3_replay_step_up, param=number)
        else:
            self.game.search_index.disengage()
            self.cancel_delayed(name="card3_replay_step_up")
            self.search_sounds()
            self.search()
    

    def closed_search_relays(self, rivets):
        # This function is critical, as it will determine which card is returned, etc.  I need to check the position of the
        # replay counter for the card. We will get a row back
        # that has the numbers on the position which will return the search relay connected.  When three out of the five relays
        # are connected, we get a winner!
        
        self.pos = {}
        # Card 1
        # Note in United Games, that vertical columns are scanned first
        # Horizontal rows scanned after vertical columns, diagonal last
        # Now, the image shown is horizontal, then vertical, so I'm totally
        # confused.  As such, since my search is almost instantaneous, I have
        # to keep this the same as Bally, which scans horizontal, then vertical
        # then diagonal.  I can change this later if needed, but I think
        # this is correct?
        self.pos[0] = {}
        self.pos[1] = {5:1, 1:2, 9:3, 25:4, 3:5}
        self.pos[2] = {8:1, 22:2, 10:3, 19:4, 17:5}
        self.pos[3] = {6:1, 18:2, 16:3, 11:4, 7:5}
        self.pos[4] = {24:1, 21:2, 14:3, 20:4, 13:5}
        self.pos[5] = {12:1, 23:2, 2:3, 15:4, 4:5}
        self.pos[6] = {5:1, 8:2, 6:3, 24:4, 12:5}
        self.pos[7] = {1:1, 22:2, 18:3, 21:4, 23:5}
        self.pos[8] = {9:1, 10:2, 16:3, 14:4, 2:5}
        self.pos[9] = {25:1, 19:2, 11:3, 20:4, 15:5}
        self.pos[10] = {3:1, 17:2, 7:3, 13:4, 4:5}
        self.pos[11] = {5:1, 22:2, 16:3, 20:4, 4:5}
        self.pos[12] = {3:1, 19:2, 16:3, 21:4, 12:5}
        self.pos[13] = {}
        self.pos[14] = {}
        self.pos[15] = {9:1, 24:2, 4:3, 16:4, 6:5}
        self.pos[16] = {13:1, 19:2, 14:3, 20:4, 25:5}
        self.pos[17] = {2:1, 18:2, 15:3, 12:4, 8:5}
        self.pos[18] = {1:1, 22:2, 11:3, 21:4, 17:5}
        self.pos[19] = {10:1, 7:2, 5:3, 23:4, 3:5}
        self.pos[20] = {9:1, 13:2, 2:3, 1:4, 10:5}
        self.pos[21] = {24:1, 19:2, 18:3, 22:4, 7:5}
        self.pos[22] = {4:1, 14:2, 15:3, 11:4, 5:5}
        self.pos[23] = {16:1, 20:2, 12:3, 21:4, 23:5}
        self.pos[24] = {6:1, 25:2, 8:3, 17:4, 3:5}
        self.pos[25] = {9:1, 19:2, 15:3, 21:4, 3:5}
        self.pos[26] = {6:1, 20:2, 15:3, 22:4, 10:5}
        self.pos[27] = {}
        self.pos[28] = {}
        self.pos[29] = {21:1, 7:2, 10:3, 4:4, 9:5}
        self.pos[30] = {15:1, 3:2, 18:3, 22:4, 8:5}
        self.pos[31] = {24:1, 14:2, 17:3, 11:4, 2:5}
        self.pos[32] = {13:1, 6:2, 12:3, 19:4, 23:5}
        self.pos[33] = {20:1, 25:2, 1:3, 16:4, 5:5}
        self.pos[34] = {21:1, 15:2, 24:3, 13:4, 20:5}
        self.pos[35] = {7:1, 3:2, 14:3, 6:4, 25:5}
        self.pos[36] = {10:1, 18:2, 17:3, 12:4, 1:5}
        self.pos[37] = {4:1, 22:2, 11:3, 19:4, 16:5}
        self.pos[38] = {9:1, 8:2, 2:3, 23:4, 5:5}
        self.pos[39] = {21:1, 3:2, 17:3, 19:4, 5:5}
        self.pos[40] = {9:1, 22:2, 17:3, 6:4, 20:5}
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

        card = 0

        if rivets in range(0,14):
            card = 1
        elif rivets in range(15,28):
            card = 2
        elif rivets in range(29, 42):
            card = 3

        return (self.pos[rivets], card)
    
    def scan_all(self):
        #Animate scanning of everything - this happens through the flash disc
        self.all_probability()
        self.check_outer_mixer3()

    def check_reflex2(self):
        r2 = self.game.reflex2.position
        mix1 = self.game.mixer1.connected_rivet()
        if r2 in [15,16,17,19]:
            if mix1 in [3,5]:
                return 1
            else:
                return 0
        elif r2 in range(19,22):
            if mix1 in [3,9,14,21]:
                return 1
            else:
                return 0
        elif r2 == 5 or r2 in range (23,29):
            if mix1 in [2,6,11,17,21]:
                return 1
            else:
                return 0
        elif r2 in range(30,35):
            if mix1 in [0,5,8,12,17,20,23]:
                return 1
            else:
                return 0
        elif r2 in range(36,43):
            if mix1 in [0,2,6,8,11,14,15,18,20,23]:
                return 1
            else:
                return 0
        elif r2 in range(44,48):
            return 1
        else:
            return 1

    def check_mixer2(self):
        mix2 = self.game.mixer2.connected_rivet()
        if self.game.card1_replay_counter.position == 0 and self.game.card2_replay_counter.position == 0 and self.game.card3_replay_counter.position == 0:
            if mix2 in [10,12,14,16,18,20,22,24]:
                self.game.mixer2.spin()
                mix2 = self.game.mixer2.connected_rivet()
            else:
                if mix2 in range(0,9) or mix2 in [11,13,15,17,19,21,23]:
                    return 1
                else:
                    return 0
        
        # Check mix2 position.  Inner and outer row of rivets are not emulated
        # properly.  I have no idea the position of the various fingers.
        if mix2 in range(0,9) or mix2 in [11,13,15,17,19,21,23]:
            self.game.mixer2.spin()
            mix2 = self.game.mixer2.connected_rivet()
            if mix2 in [0,4,6,8,12,14,18,19,20,21,22,23]:
                    return 1
            if self.game.c1_double.status == False:
                if mix2 in [1,7,10,13]:
                    return 1
            elif self.game.c2_double.status == False:
                if mix2 in [3,9,15,16]:
                    return 1
            elif self.game.c3_double.status == False:
                if mix2 in [5,11,17,24]:
                    return 1
            else:
                return 0
                
    def check_inner_mixer3(self):
        mix3 = self.game.mixer3.connected_rivet()
        if mix3 in [0,18,14,40]:
            if self.game.fourteen.status == False:
                self.game.fourteen.engage(self.game)
                self.game.sound.play('tilt')
            if 14 not in self.holes:
                self.holes.append(14)
            if self.game.fourteen.status == True and self.game.nineteen.status == True and self.game.twentytwo.status == True:
                if self.game.fnt.status == False:
                    self.game.fnt.engage(self.game)
                    self.game.sound.play('tilt')
            self.delay(name="display", delay=0.1, handler=graphics.rodeo_3.display, param=self)
        elif mix3 in [7,18,25,38]:
            if self.game.nineteen.status == False:
                self.game.nineteen.engage(self.game)
                self.game.sound.play('tilt')
            if 19 not in self.holes:
                self.holes.append(19)
            if self.game.fourteen.status == True and self.game.nineteen.status == True and self.game.twentytwo.status == True:
                if self.game.fnt.status == False:
                    self.game.fnt.engage(self.game)
                    self.game.sound.play('tilt')
            self.delay(name="display", delay=0.1, handler=graphics.rodeo_3.display, param=self)
        elif mix3 in [2,18,32,48]:
            if self.game.twentytwo.status == False:
                self.game.twentytwo.engage(self.game)
                self.game.sound.play('tilt')
            if 22 not in self.holes:
                self.holes.append(22)
            if self.game.fourteen.status == True and self.game.nineteen.status == True and self.game.twentytwo.status == True:
                if self.game.fnt.status == False:
                    self.game.fnt.engage(self.game)
                    self.game.sound.play('tilt')
            self.delay(name="display", delay=0.1, handler=graphics.rodeo_3.display, param=self)
        elif mix3 in [3,9]:
            if self.game.selector.position == 3:
                if self.game.fifteen.status == False:
                    self.game.fifteen.engage(self.game)
                    self.game.sound.play('tilt')
                if 15 not in self.holes:
                    self.holes.append(15)
                if self.game.fifteen.status == True and self.game.sixteen.status == True and self.game.seventeen.status == True:
                    if self.game.fss.status == False:
                        self.game.fss.engage(self.game)
                        self.game.sound.play('tilt')
                self.delay(name="display", delay=0.1, handler=graphics.rodeo_3.display, param=self)
        elif mix3 in [9,39]:
            if self.game.selector.position == 3:
                if self.game.sixteen.status == False:
                    self.game.sixteen.engage(self.game)
                    self.game.sound.play('tilt')
                if 16 not in self.holes:
                    self.holes.append(16)
                if self.game.fifteen.status == True and self.game.sixteen.status == True and self.game.seventeen.status == True:
                    if self.game.fss.status == False:
                        self.game.fss.engage(self.game)
                        self.game.sound.play('tilt')
                self.delay(name="display", delay=0.1, handler=graphics.rodeo_3.display, param=self)
        elif mix3 in [9,29]:
            if self.game.selector.position == 3:
                if self.game.seventeen.status == False:
                    self.game.seventeen.engage(self.game)
                    self.game.sound.play('tilt')
                if 17 not in self.holes:
                    self.holes.append(17)
                if self.game.fifteen.status == True and self.game.sixteen.status == True and self.game.seventeen.status == True:
                    if self.game.fss.status == False:
                        self.game.fss.engage(self.game)
                        self.game.sound.play('tilt')
                self.delay(name="display", delay=0.1, handler=graphics.rodeo_3.display, param=self)

    def all_probability(self):
        r2 = self.check_reflex2()
        if r2 == 1:
            m2 = self.check_mixer2()
            if m2 == 1:
                # Mixer 3 actually handles the main portioning for this game.
                m4 = self.check_mixer4()
                if m4 == 1:
                    m3 = self.check_inner_mixer3()
                    m3 = self.check_outer_mixer3()

    def check_outer_mixer3(self):
        mix3 = self.game.mixer3.connected_rivet()
        if self.game.eb_play.status == False:
            if mix3 == 1:
                if self.game.all_double.status == False:
                    if self.game.c1_double.status == True and self.game.c2_double.status == True and self.game.c3_double.status == True:
                        self.game.all_double.engage(self.game)
                        self.game.sound.play('tilt')
                if self.game.all_triple.status == False:
                    if self.game.all_double.status == False:
                        self.game.all_double.engage(self.game)
                        self.game.sound.play('tilt')
                    if self.game.c1_triple.status == False:
                        if self.game.c1_double.status == False:
                            self.game.c1_double.engage(self.game)
                            self.game.sound.play('tilt')
                    if self.game.c2_triple.status == False:
                        if self.game.c2_double.status == False:
                            self.game.c2_double.engage(self.game)
                            self.game.sound.play('tilt')
                    if self.game.c3_triple.status == False:
                        if self.game.c3_double.status == False:
                            self.game.c3_double.engage(self.game)
                            self.game.sound.play('tilt')
            elif mix3 == 26:
                if self.game.all_double.status == False:
                    if self.game.all_triple.status == False:
                        self.game.all_triple.engage(self.game)
                        self.game.all_double.disengage()
                        self.game.sound.play('tilt')
                if self.game.all_double.status == False:
                    if self.game.all_triple.status == False:
                        self.game.all_triple.engage(self.game)
                        self.game.sound.play('tilt')
                    if self.game.c1_double.status == False:
                        if self.game.c1_triple.status == False:
                            self.game.c1_triple.engage(self.game)
                            self.game.sound.play('tilt')
                    if self.game.c2_double.status == False:
                        if self.game.c2_triple.status == False:
                            self.game.c2_triple.engage(self.game)
                            self.game.sound.play('tilt')
                    if self.game.c3_double.status == False:
                        if self.game.c3_triple.status == False:
                            self.game.c3_triple.engage(self.game)
                            self.game.sound.play('tilt')
            elif mix3 in [11,21,33]:
                if self.game.c1_triple.status == False:
                    if self.game.c1_double.status == False:
                        self.game.c1_double.engage(self.game)
                        self.game.sound.play('tilt')
            elif mix3 == 5:
                if self.game.c1_double.status == True:
                    self.game.c1_double.disengage()
                if self.game.c1_triple.status == False:
                    self.game.c1_triple.engage(self.game)
                    self.game.sound.play('tilt')
            elif mix3 in [15,23,34]:
                if self.game.c1_double.status == True:
                    if self.game.c1_triple.status == False:
                        self.game.c1_double.disengage()
                        self.game.c1_triple.engage(self.game)
                        self.game.sound.play('tilt')
            elif mix3 in [4,14,24,31]:
                if self.game.c2_triple.status == False:
                    if self.game.c2_double.status == False:
                        self.game.c2_double.engage(self.game)
                        self.game.sound.play('tilt')
            elif mix3 == 20:
                if self.game.c2_double.status == True:
                    self.game.c2_double.disengage()
                if self.game.c2_triple.status == False:
                    self.game.c2_triple.engage(self.game)
                    self.game.sound.play('tilt')
            elif mix3 in [8,30,45]:
                if self.game.c2_double.status == True:
                    if self.game.c2_double.status == False:
                        self.game.c2_double.disengage()
                        self.game.c2_triple.engage(self.game)
                        self.game.sound.play('tilt')
            elif mix3 in [7,27,37,43]:
                if self.game.c3_triple.status == False:
                    if self.game.c3_double.status == False:
                        self.game.c3_double.engage(self.game)
                        self.game.sound.play('tilt')
            elif mix3 == 36:
                if self.game.c3_double.status == True:
                    self.game.c3_double.disengage()
                if self.game.c3_triple.status == False:
                    self.game.c3_triple.engage(self.game)
                    self.game.sound.play('tilt')
            elif mix3 in [12,41,47]:
                if self.game.c3_double.status == True:
                    self.game.c3_double.disengage()
                if self.game.c3_triple.status == False:
                    self.game.c3_triple.engage(self.game)
                    self.game.sound.play('tilt')
        else:
            if mix3 in [0,3,6,7,10,13,18,28,29,33,35,39,42,46,49]:
                self.check_extra_ball(1)
            elif mix3 == 10:
                self.check_extra_ball(8, 9)
            else:
                self.check_extra_ball(8, 1)

    def check_extra_ball(self, maximum, starting=None):
        r1 = self.game.reflex1.position
        if r1 in [3,7,8,9,11,14,18,20,21,22,24,25,26,29,31,34,37,40,42,43,44,46]:
            if self.game.extra_ball.position < 24:
                if maximum == 1:
                    self.game.extra_ball.step()
                    self.check_lifter_status()
                elif maximum == 8:
                    if self.game.extra_ball.position < starting:
                        num = maximum - self.game.extra_ball.position
                        self.step_eb(num)

    def step_eb(self, number):
        if number > 0:
            number -= 1
            self.game.extra_ball.step()
            self.delay(name="display", delay=0, handler=graphics.rodeo_3.display, param=self)
            self.check_lifter_status()
            self.delay(name="step_eb", delay=0.1, handler=self.step_eb, param=number)
            if self.game.extra_ball.position >= 9:
                self.check_lifter_status()

    def check_mixer4(self):
        mix4 = self.game.mixer4.connected_rivet()
        if self.game.fifteen.status == False and self.game.sixteen.status == False and self.game.seventeen.status == False and self.game.fourteen.status == False and self.game.nineteen.status == False and self.game.twentytwo.status == False:
            if mix4 == 1:
                return 0
            else:
                return 1
        elif self.game.fifteen.status == True:
            if mix4 in [1,6,8,14,17,22]:
                return 0
        elif self.game.sixteen.status == True:
            if mix4 in [5,7,12,15,21,23]:
                return 0
        elif self.game.seventeen.status == True:
            if mix4 in [0,2,9,10,16,19]:
                return 0
        elif self.game.fourteen.status == True:
            if mix4 in [1,5,9,13]:
                return 0
        elif self.game.nineteen.status == True:
            if mix4 in [0,4,17,21]:
                return 0
        elif self.game.twentytwo.status == True:
            if mix4 in [8,12,16,20]:
                return 0
        else:
            if mix4 in [2,3,4,6,7,10,11,13,14,15,18,19,20,22,23,24]:
                return 1
            else:
                return 0

    def scan_eb(self):
        if self.game.eb_play.status == True:
            self.check_outer_mixer3()
            # Timer resets to 0 position on ball count increasing.  We are fudging this since we will have
            # no good way to measure balls as they return back to the trough.  The ball count unit cannot be
            # relied upon as we do not have a switch in the outhole, and the trough logic is too complex for
            # the task at hand.
            # TODO: implement thunk noises into the units.py to automatically play the noises.
            self.game.timer.reset()
        else:
            # TODO: play thunk noise of EB search bearing no fruit.
            pass
        self.delay(name="display", delay=0.1, handler=graphics.rodeo_3.display, param=self)

    def animate_both(self, args):
        start = args[0]
        diff = args[1]
        num = args[2]
        if start + num >= 25:
            start = 0
        if diff >= 0:
            num = num + 1
            rivet = start + num
            if rivet in [0,4,7,8,16,18]:
                self.game.mixer4.step()
                graphics.rodeo_3.animate_mixer4(self)
            if rivet in [1,3,12,14,17,21,24]:
                self.game.mixer1.step()
                graphics.rodeo_3.animate_mixer1(self)
            if rivet in [2,6,10,11,20,23]:
                self.game.mixer2.step()
                graphics.rodeo_3.animate_mixer2(self)
            if rivet in [5,9,13,15,19,22]:
                self.game.mixer3.step()
                graphics.rodeo_3.animate_mixer3(self)
            graphics.rodeo_3.both_animation([self, start + num])
            self.cancel_delayed(name="display")
            diff = diff - 1
            args = [start,diff,num]
            self.delay(name="both_animation", delay=0.08, handler=self.animate_both, param=args)
        else:
            self.cancel_delayed(name="both_animation")
            self.delay(name="display", delay=0.1, handler=graphics.rodeo_3.display, param=self)
            self.scan_all()

    def animate_eb_scan(self, args):
        start = args[0]
        diff = args[1]
        num = args[2]
        if start + num >= 25:
            start = 0
        if diff >= 0:
            num = num + 1
            rivet = start + num
            if rivet in [0,4,7,8,16,18]:
                self.game.mixer4.step()
            if rivet in [1,3,12,14,17,21,24]:
                self.game.mixer1.step()
            if rivet in [2,6,10,11,20,23]:
                self.game.mixer2.step()
            if rivet in [5,9,13,15,19,22]:
                self.game.mixer3.step()
            graphics.rodeo_3.eb_animation([self, start + num])
            self.cancel_delayed(name="display")
            diff = diff - 1
            args = [start,diff,num]
            self.delay(name="eb_animation", delay=0.08, handler=self.animate_eb_scan, param=args)
        else:
            self.cancel_delayed(name="eb_animation")
            self.delay(name="display", delay=0.1, handler=graphics.rodeo_3.display, param=self)
            self.scan_eb()

    # Define reset as the knock-off, anti-cheat relay disabled, and replay reset enabled.  Motors turn while credits are knocked off.
    # When meter reaches zero and the zero limit switch is hit, turn off motor sound and leave backglass gi on, but with tilt displayed.

    def startup(self):        
        # Every bingo requires the meter to register '0' 
        # before allowing coin entry --
        # also needs to show a plain 'off' backglass.
        self.eb = False
        self.tilt_actions()

class Rodeo3(procgame.game.BasicGame):
    """ Rodeo -- another?  United tried to make two different games called Rodeo. """
    def __init__(self, machine_type):
        super(Rodeo3, self).__init__(machine_type)
        pygame.mixer.pre_init(44100,-16,2,512)
        self.sound = procgame.sound.SoundController(self)
        self.sound.set_volume(1.0)
        # NOTE: trough_count only counts the number of switches present in the  trough.  It does _not_ count
        #       the number of balls present.   In this game, there  should  be  8  balls.
        self.trough_count = 6

        # Now, the control unit can be in one of two positions, essentially.
        self.cu = 1

        # Subclass my units unique to this game -  modifications must be made to set up mixers and steppers unique to the game
        # NOTE: 'top' positions are indexed using a 0 index, so the top on a 24 position unit is actually 23.

        self.mixer1 = units.Mixer("mixer1", 23)
        self.mixer1.position = random.randint(0,23)
        self.mixer2 = units.Mixer("mixer2", 23)
        self.mixer2.spin()
        self.mixer3 = units.Mixer("mixer3", 50)
        self.mixer3.spin()
        self.mixer4 = units.Mixer("mixer4", 23)
        self.mixer4.spin()

        self.searchdisc = units.Search("searchdisc", 49)

        #Search relays
        self.s1 = units.Relay("s1")
        self.s2 = units.Relay("s2")
        self.s3 = units.Relay("s3")
        self.s4 = units.Relay("s4")
        self.s5 = units.Relay("s5")
        self.search_index = units.Relay("search_index")

        #Replay Counter
        self.card1_replay_counter = units.Stepper("card1_replay_counter", 200)
        self.card2_replay_counter = units.Stepper("card2_replay_counter", 200)
        self.card3_replay_counter = units.Stepper("card3_replay_counter", 200)
 
        #Initialize stepper units used to keep track of features or timing.
        self.timer = units.Stepper("timer", 40)
        self.ball_count = units.Stepper("ball_count", 8)

        # Initialize reflex(es) and mixers unique to this game
        # NOTE:  Reflexes in United games are actually comprised of two
        # separate steppers.  These act as normal continuous steppers, so I
        # need to subclass as steppers.
        self.reflex1 = units.Stepper("reflex1", 50, "Rodeo3", "continuous")
        self.reflex2 = units.Stepper("reflex2", 50, "Rodeo3")

        #In United games, they call this spotting motor the 'flash' motor, 
        #similar to the ball bowlers.
        self.flash = units.Spotting("flash", 24)

        #Check for status of the replay register zero switch.  If positive
        #and machine is just powered on, this will zero out the replays.
        self.replay_reset = units.Relay("replay_reset")
        
        #Extra ball unit contains 24 positions.  Max of 3 EBs.
        self.extra_ball = units.Stepper("extra_ball", 24)

        #When engage()d, light 6v circuit, and enable game features, scoring,
        #etc. Disengage()d means that the machine is 'soft' tilted. In United
        #games, they call this the lock relay, similar to many other pin
        #manufacturers.
        self.lock = units.Relay("lock")

        #Card score doubling trip relays
        self.c1_double = units.Relay("c1_double")
        self.c2_double = units.Relay("c2_double")
        self.c3_double = units.Relay("c3_double")

        #Card score tripling trip relays
        self.c1_triple = units.Relay("c1_triple")
        self.c2_triple = units.Relay("c2_triple")
        self.c3_triple = units.Relay("c3_triple")

        self.eb_play = units.Relay("eb_play")

        #Selector keeps track of cards in play - in United games, they call
        #this the card step-up, but I'll call it selector for consistency with other
        #multi-card Bally games.
        self.selector = units.Stepper("selector", 3)

        #When engage()d, spin.
        self.start = units.Relay("start")

        #Tilt is separate from anti-cheat in that the trip will move the shutter
        #when the game is tilted with 1st ball in the lane.  Also prevents you
        #from picking back up by killing the anti-cheat.  Can be engaged by 
        #tilt bob, slam tilt switches, or timer at 39th step.
        #Immediately kills motors.
        self.tilt = units.Relay("tilt")

        #Need to define relays for playing ebs
        self.eb = units.Relay("eb")

        #Relay for lighting all doubles
        self.all_double = units.Relay("all_double")
        #Relay for lighting all triples
        self.all_triple = units.Relay("all_triple")

        #Relays for spotted numbers
        self.sixteen = units.Relay("sixteen")
        self.fifteen = units.Relay("fifteen")
        self.fourteen = units.Relay("fourteen")
        self.nineteen = units.Relay("nineteen")
        self.seventeen = units.Relay("seventeen")
        self.twentytwo = units.Relay("twentytwo")
        self.fss = units.Relay("fss")
        self.fnt = units.Relay("fnt")

        self.anti_cheat = units.Relay("anti_cheat")

        self.replays = 0
        self.returned = False

    def reset(self):
        super(Rodeo3, self).reset()
        self.logger = logging.getLogger('game')
        self.load_config('bingo.yaml')
        self.lock.engage(game)
        
        main_mode = MulticardBingo(self)
        self.modes.add(main_mode)
        

game = Rodeo3(machine_type='pdb')
game.reset()
game.run_loop()
