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
from bingo_emulator.graphics.showboat import *

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
        self.game.tilt.disengage()
        self.regular_play()

        self.delay(name="display", delay=0.1, handler=graphics.showboat.display, param=self)

    def sw_startButton_active(self, sw):
        if self.game.replays > 0 or self.game.switches.freeplay.is_active():
            self.game.tilt.disengage()
            self.regular_play()

            self.delay(name="display", delay=0.1, handler=graphics.showboat.display, param=self)

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
            os.system("/home/nbaldridge/proc/bingo_emulator/start_game.sh showboat")

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
        self.cancel_delayed(name="card4_replay_step_up")
        self.cancel_delayed(name="card5_replay_step_up")
        self.cancel_delayed(name="card6_replay_step_up")
        self.cancel_delayed(name="timeout")
        self.cancel_delayed(name="both_animation")
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
            if self.game.selector.position < 6:
                self.game.selector.step()
            if self.game.switches.shutter.is_inactive():
                self.game.coils.shutter.enable()
            self.game.cu = not self.game.cu
            self.game.reflex1.step()
            self.game.reflex2.step()
            
            current = self.game.flash.connected_rivet()
            self.game.flash.spin()
            new = self.game.flash.connected_rivet()
            self.animate_both([current,self.game.flash.movement_amount,1])
            self.replay_step_down()
            graphics.showboat.display(self)
            self.check_lifter_status()
        else:
            self.holes = []
            self.game.start.engage(self.game)
            self.game.card1_replay_counter.reset()
            self.game.card2_replay_counter.reset()
            self.game.card3_replay_counter.reset()
            self.game.card4_replay_counter.reset()
            self.game.card5_replay_counter.reset()
            self.game.card6_replay_counter.reset()
            self.game.c1_double.disengage()
            self.game.c2_double.disengage()
            self.game.c3_double.disengage()
            self.game.c4_double.disengage()
            self.game.c5_double.disengage()
            self.game.c6_double.disengage()
            self.game.c1_triple.disengage()
            self.game.c2_triple.disengage()
            self.game.c3_triple.disengage()
            self.game.c4_triple.disengage()
            self.game.c5_triple.disengage()
            self.game.c6_triple.disengage()
            self.game.extra_ball.reset()
            self.game.timer.reset()
            self.game.sixteen.disengage()
            self.game.fifteen_seventeen.disengage()
            self.game.fourteen_eighteen.disengage()
            self.game.start.engage(self.game)
            self.game.selector.reset()
            self.game.ball_count.reset()
            self.game.sound.stop_music()
            self.regular_play()
        self.delay(name="display", delay=0.1, handler=graphics.showboat.display, param=self)
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
                            if self.game.extra_ball.position >= 1 and self.game.ball_count.position <= 5:
                                if self.game.switches.shooter.is_open() and self.game.switches.trough3.is_closed():
                                    self.game.coils.lifter.enable()
                        if self.game.switches.trough3.is_open():
                            if self.game.extra_ball.position >= 2 and self.game.ball_count.position <= 6:
                                if self.game.switches.shooter.is_open() and self.game.switches.trough2.is_closed():
                                    self.game.coils.lifter.enable()
                        if self.game.switches.trough2.is_inactive() and self.game.ball_count.position <= 7:
                            if self.game.ball_count.position <= 7:
                                if self.game.extra_ball.position >= 3:
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
        if (self.game.ball_count.position >= 7 and self.game.switches.trough1.is_inactive()):
            self.game.coils.lifter.disable()

    def sw_ballLift_active_for_500ms(self, sw):
        if self.game.tilt.status == False:
            if self.game.switches.shooter.is_open():
                if self.game.ball_count.position < 5:
                    self.game.coils.lifter.enable()
                if self.game.ball_count.position == 5 and self.game.extra_ball.position >= 1:
                    self.game.coils.lifter.enable()
                if self.game.ball_count.position == 6 and self.game.extra_ball.position >= 2:
                    self.game.coils.lifter.enable()
                if self.game.ball_count.position == 7 and self.game.extra_ball.position >= 3:
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
            self.delay(name="display", delay=0.1, handler=graphics.showboat.display, param=self)

    def sw_hole2_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(2)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.showboat.display, param=self)

    def sw_hole3_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(3)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.showboat.display, param=self)

    def sw_hole4_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(4)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.showboat.display, param=self)

    def sw_hole5_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(5)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.showboat.display, param=self)

    def sw_hole6_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(6)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.showboat.display, param=self)

    def sw_hole7_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(7)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.showboat.display, param=self)

    def sw_hole8_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(8)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.showboat.display, param=self)

    def sw_hole9_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(9)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.showboat.display, param=self)

    def sw_hole10_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(10)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.showboat.display, param=self)

    def sw_hole11_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(11)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.showboat.display, param=self)

    def sw_hole12_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(12)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.showboat.display, param=self)

    def sw_hole13_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(13)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.showboat.display, param=self)

    def sw_hole14_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(14)
            if self.game.fourteen_eighteen.status == True:
                if 18 not in self.holes:
                    self.game.extra_ball.step()
                    self.check_lifter_status()
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.showboat.display, param=self)

    def sw_hole15_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(15)
            if self.game.fifteen_seventeen.status == True:
                if 17 not in self.holes:
                    self.game.extra_ball.step()
                    self.check_lifter_status()
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.showboat.display, param=self)

    def sw_hole16_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(16)
            if self.game.sixteen.status == True:
                self.game.extra_ball.step()
                self.check_lifter_status()
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.showboat.display, param=self)

    def sw_hole17_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(17)
            if self.game.fifteen_seventeen.status == True:
                if 15 not in self.holes:
                    self.game.extra_ball.step()
                    self.check_lifter_status()
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.showboat.display, param=self)

    def sw_hole18_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(18)
            if self.game.fourteen_eighteen.status == True:
                if 14 not in self.holes:
                    self.game.extra_ball.step()
                    self.check_lifter_status()
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.showboat.display, param=self)

    def sw_hole19_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(19)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.showboat.display, param=self)

    def sw_hole20_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(20)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.showboat.display, param=self)

    def sw_hole21_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(21)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.showboat.display, param=self)

    def sw_hole22_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(22)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.showboat.display, param=self)

    def sw_hole23_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(23)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.showboat.display, param=self)

    def sw_hole24_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(24)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.showboat.display, param=self)

    def sw_hole25_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(25)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.search_sounds()
            self.delay(name="display", delay=0.1, handler=graphics.showboat.display, param=self)
    
    def sw_replayReset_active(self, sw):
        self.game.lock.disengage()
        self.holes = []
        self.delay(name="display", delay=0.1, handler=graphics.showboat.display, param=self)
        self.tilt_actions()
        self.replay_step_down(self.game.replays)

    def tilt_actions(self):
        self.game.start.disengage()
        self.cancel_delayed(name="replay_reset")
        self.cancel_delayed(name="card1_replay_step_up")
        self.cancel_delayed(name="card2_replay_step_up")
        self.cancel_delayed(name="card3_replay_step_up")
        self.cancel_delayed(name="card4_replay_step_up")
        self.cancel_delayed(name="card5_replay_step_up")
        self.cancel_delayed(name="card6_replay_step_up")
        self.cancel_delayed(name="timeout")
        self.cancel_delayed(name="both_animation")
        self.game.search_index.disengage()
        if self.game.switches.shutter.is_active() and self.game.ball_count.position == 0:
            self.game.coils.shutter.enable()
        self.holes = []
        self.game.selector.reset()
        self.game.extra_ball.reset()
        self.game.c1_double.disengage()
        self.game.c2_double.disengage()
        self.game.c3_double.disengage()
        self.game.c4_double.disengage()
        self.game.c5_double.disengage()
        self.game.c6_double.disengage()
        self.game.c1_triple.disengage()
        self.game.c2_triple.disengage()
        self.game.c3_triple.disengage()
        self.game.c4_triple.disengage()
        self.game.c5_triple.disengage()
        self.game.c6_triple.disengage()
        self.game.extra_ball.reset()
        self.game.sixteen.disengage()
        self.game.fifteen_seventeen.disengage()
        self.game.fourteen_eighteen.disengage()
        self.game.ball_count.reset()
        self.game.lock.engage(game)
        self.game.tilt.engage(self.game)
        self.game.sound.stop_music()
        self.game.sound.play('tilt')
        # displays "Tilt" on the backglass, you have to recoin.
        self.delay(name="display", delay=0.1, handler=graphics.showboat.display, param=self)

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
                graphics.replay_step_down(self.game.replays, graphics.showboat.reel1, graphics.showboat.reel10, graphics.showboat.reel100)
                self.game.coils.registerDown.pulse()
                number -= 1
                graphics.showboat.display(self)
                self.delay(name="replay_reset", delay=0.13, handler=self.replay_step_down, param=number)
            elif number == 1:
                self.game.replays -= 1
                graphics.replay_step_down(self.game.replays, graphics.showboat.reel1, graphics.showboat.reel10, graphics.showboat.reel100)
                self.game.coils.registerDown.pulse()
                number -= 1
                graphics.showboat.display(self)
                self.cancel_delayed(name="replay_reset")
        else: 
            if self.game.replays > 0:
                self.game.replays -= 1
                graphics.replay_step_down(self.game.replays, graphics.showboat.reel1, graphics.showboat.reel10, graphics.showboat.reel100)
                self.delay(name="display", delay=0.1, handler=graphics.showboat.display, param=self)
            self.game.coils.registerDown.pulse()

    def replay_step_up(self):
        if self.game.replays < 899:
            self.game.replays += 1
            graphics.replay_step_up(self.game.replays, graphics.showboat.reel1, graphics.showboat.reel10, graphics.showboat.reel100)
        self.game.coils.registerUp.pulse()
        #self.game.coils.bell.pulse()
        self.game.reflex1.stepdown()
        graphics.showboat.display(self)

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
            for i in range(0, 100):
                if i <= 50:
                    self.r = self.closed_search_relays(self.game.searchdisc.position)
                    self.game.searchdisc.spin()
                if i >= 51:
                    self.r = self.closed_search_relays(self.game.searchdisc2.position + 50)
                    self.game.searchdisc2.spin()
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
                            if self.game.card1_replay_counter.position < 4:
                                self.game.search_index.engage(self.game)
                                self.card1_replay_step_up(4 - self.game.card1_replay_counter.position)
                        elif self.game.c1_triple.status == True:
                            if self.game.card1_replay_counter.position < 6:
                                self.game.search_index.engage(self.game)
                                self.card1_replay_step_up(6 - self.game.card1_replay_counter.position)
                        else:
                            if self.game.card1_replay_counter.position < 2:
                                self.game.search_index.engage(self.game)
                                self.card1_replay_step_up(2 - self.game.card1_replay_counter.position)
                    if relays == 4:
                        if self.game.c1_double.status == True:
                            if self.game.card1_replay_counter.position < 20:
                                self.game.search_index.engage(self.game)
                                self.card1_replay_step_up(20 - self.game.card1_replay_counter.position)
                        elif self.game.c1_triple.status == True:
                            if self.game.card1_replay_counter.position < 30:
                                self.game.search_index.engage(self.game)
                                self.card1_replay_step_up(30 - self.game.card1_replay_counter.position)
                        elif self.game.card1_replay_counter.position < 10:
                            self.game.search_index.engage(self.game)
                            self.card1_replay_step_up(10 - self.game.card1_replay_counter.position)
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
                            if self.game.card2_replay_counter.position < 4:
                                self.game.search_index.engage(self.game)
                                self.card2_replay_step_up(4 - self.game.card2_replay_counter.position)
                        elif self.game.c2_triple.status == True:
                            if self.game.card2_replay_counter.position < 6:
                                self.game.search_index.engage(self.game)
                                self.card2_replay_step_up(6 - self.game.card2_replay_counter.position)
                        else:
                            if self.game.card2_replay_counter.position < 2:
                                self.game.search_index.engage(self.game)
                                self.card2_replay_step_up(2 - self.game.card2_replay_counter.position)
                    if relays == 4:
                        if self.game.c2_double.status == True:
                            if self.game.card2_replay_counter.position < 20:
                                self.game.search_index.engage(self.game)
                                self.card2_replay_step_up(20 - self.game.card2_replay_counter.position)
                        elif self.game.c2_triple.status == True:
                            if self.game.card2_replay_counter.position < 30:
                                self.game.search_index.engage(self.game)
                                self.card2_replay_step_up(30 - self.game.card2_replay_counter.position)
                        elif self.game.card2_replay_counter.position < 10:
                            self.game.search_index.engage(self.game)
                            self.card2_replay_step_up(10 - self.game.card2_replay_counter.position)
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
                            if self.game.card3_replay_counter.position < 4:
                                self.game.search_index.engage(self.game)
                                self.card3_replay_step_up(4 - self.game.card3_replay_counter.position)
                        elif self.game.c3_triple.status == True:
                            if self.game.card3_replay_counter.position < 6:
                                self.game.search_index.engage(self.game)
                                self.card3_replay_step_up(6 - self.game.card3_replay_counter.position)
                        else:
                            if self.game.card3_replay_counter.position < 2:
                                self.game.search_index.engage(self.game)
                                self.card3_replay_step_up(2 - self.game.card3_replay_counter.position)
                    if relays == 4:
                        if self.game.c3_double.status == True:
                            if self.game.card3_replay_counter.position < 20:
                                self.game.search_index.engage(self.game)
                                self.card3_replay_step_up(20 - self.game.card3_replay_counter.position)
                        elif self.game.c3_triple.status == True:
                            if self.game.card3_replay_counter.position < 30:
                                self.game.search_index.engage(self.game)
                                self.card3_replay_step_up(30 - self.game.card3_replay_counter.position)
                        elif self.game.card3_replay_counter.position < 10:
                            self.game.search_index.engage(self.game)
                            self.card3_replay_step_up(10 - self.game.card3_replay_counter.position)
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
            if selector >= 4:
                if card == 4:
                    if relays == 3:
                        if self.game.c4_double.status == True:
                            if self.game.card4_replay_counter.position < 4:
                                self.game.search_index.engage(self.game)
                                self.card4_replay_step_up(4 - self.game.card4_replay_counter.position)
                        elif self.game.c4_triple.status == True:
                            if self.game.card4_replay_counter.position < 6:
                                self.game.search_index.engage(self.game)
                                self.card4_replay_step_up(6 - self.game.card4_replay_counter.position)
                        else:
                            if self.game.card4_replay_counter.position < 2:
                                self.game.search_index.engage(self.game)
                                self.card4_replay_step_up(2 - self.game.card4_replay_counter.position)
                    if relays == 4:
                        if self.game.c4_double.status == True:
                            if self.game.card4_replay_counter.position < 20:
                                self.game.search_index.engage(self.game)
                                self.card4_replay_step_up(20 - self.game.card4_replay_counter.position)
                        elif self.game.c4_triple.status == True:
                            if self.game.card4_replay_counter.position < 30:
                                self.game.search_index.engage(self.game)
                                self.card4_replay_step_up(30 - self.game.card4_replay_counter.position)
                        elif self.game.card4_replay_counter.position < 10:
                            self.game.search_index.engage(self.game)
                            self.card4_replay_step_up(10 - self.game.card4_replay_counter.position)
                    if relays == 5:
                        if self.game.c4_double.status == True:
                            if self.game.card4_replay_counter.position < 200:
                                self.game.search_index.engage(self.game)
                                self.card4_replay_step_up(200 - self.game.card4_replay_counter.position)
                        elif self.game.c4_triple.status == True:
                            if self.game.card4_replay_counter.position < 300:
                                self.game.search_index.engage(self.game)
                                self.card4_replay_step_up(300 - self.game.card4_replay_counter.position)
                        elif self.game.card4_replay_counter.position < 100:
                            self.game.search_index.engage(self.game)
                            self.card4_replay_step_up(100 - self.game.card4_replay_counter.position)
            if selector >= 5:
                if card == 5:
                    if relays == 3:
                        if self.game.c5_double.status == True:
                            if self.game.card5_replay_counter.position < 4:
                                self.game.search_index.engage(self.game)
                                self.card5_replay_step_up(4 - self.game.card5_replay_counter.position)
                        elif self.game.c5_triple.status == True:
                            if self.game.card5_replay_counter.position < 6:
                                self.game.search_index.engage(self.game)
                                self.card5_replay_step_up(6 - self.game.card5_replay_counter.position)
                        else:
                            if self.game.card5_replay_counter.position < 2:
                                self.game.search_index.engage(self.game)
                                self.card5_replay_step_up(2 - self.game.card5_replay_counter.position)
                    if relays == 4:
                        if self.game.c5_double.status == True:
                            if self.game.card5_replay_counter.position < 20:
                                self.game.search_index.engage(self.game)
                                self.card5_replay_step_up(20 - self.game.card5_replay_counter.position)
                        elif self.game.c5_triple.status == True:
                            if self.game.card5_replay_counter.position < 30:
                                self.game.search_index.engage(self.game)
                                self.card5_replay_step_up(30 - self.game.card5_replay_counter.position)
                        elif self.game.card5_replay_counter.position < 10:
                            self.game.search_index.engage(self.game)
                            self.card5_replay_step_up(10 - self.game.card5_replay_counter.position)
                    if relays == 5:
                        if self.game.c5_double.status == True:
                            if self.game.card5_replay_counter.position < 200:
                                self.game.search_index.engage(self.game)
                                self.card5_replay_step_up(200 - self.game.card5_replay_counter.position)
                        elif self.game.c5_triple.status == True:
                            if self.game.card5_replay_counter.position < 300:
                                self.game.search_index.engage(self.game)
                                self.card5_replay_step_up(300 - self.game.card5_replay_counter.position)
                        elif self.game.card5_replay_counter.position < 100:
                            self.game.search_index.engage(self.game)
                            self.card5_replay_step_up(100 - self.game.card5_replay_counter.position)
            if selector >= 6:
                if card == 6:
                    if relays == 3:
                        if self.game.c6_double.status == True:
                            if self.game.card6_replay_counter.position < 4:
                                self.game.search_index.engage(self.game)
                                self.card6_replay_step_up(4 - self.game.card6_replay_counter.position)
                        elif self.game.c6_triple.status == True:
                            if self.game.card6_replay_counter.position < 6:
                                self.game.search_index.engage(self.game)
                                self.card6_replay_step_up(6 - self.game.card6_replay_counter.position)
                        else:
                            if self.game.card6_replay_counter.position < 2:
                                self.game.search_index.engage(self.game)
                                self.card6_replay_step_up(2 - self.game.card6_replay_counter.position)
                    if relays == 4:
                        if self.game.c6_double.status == True:
                            if self.game.card6_replay_counter.position < 20:
                                self.game.search_index.engage(self.game)
                                self.card6_replay_step_up(20 - self.game.card6_replay_counter.position)
                        elif self.game.c6_triple.status == True:
                            if self.game.card6_replay_counter.position < 30:
                                self.game.search_index.engage(self.game)
                                self.card6_replay_step_up(30 - self.game.card6_replay_counter.position)
                        elif self.game.card6_replay_counter.position < 10:
                            self.game.search_index.engage(self.game)
                            self.card6_replay_step_up(10 - self.game.card6_replay_counter.position)
                    if relays == 5:
                        if self.game.c6_double.status == True:
                            if self.game.card6_replay_counter.position < 200:
                                self.game.search_index.engage(self.game)
                                self.card6_replay_step_up(200 - self.game.card6_replay_counter.position)
                        elif self.game.c6_triple.status == True:
                            if self.game.card6_replay_counter.position < 300:
                                self.game.search_index.engage(self.game)
                                self.card6_replay_step_up(300 - self.game.card6_replay_counter.position)
                        elif self.game.card6_replay_counter.position < 100:
                            self.game.search_index.engage(self.game)
                            self.card6_replay_step_up(100 - self.game.card6_replay_counter.position)

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

    def card4_replay_step_up(self, number):
        self.game.sound.stop_music()
        if number >= 1:
            self.game.card4_replay_counter.step()
            number -= 1
            self.replay_step_up()
            if self.game.replays == 899:
                number = 0
            self.delay(name="card4_replay_step_up", delay=0.25, handler=self.card4_replay_step_up, param=number)
        else:
            self.game.search_index.disengage()
            self.cancel_delayed(name="card4_replay_step_up")
            self.search_sounds()
            self.search()

    def card5_replay_step_up(self, number):
        self.game.sound.stop_music()
        if number >= 1:
            self.game.card5_replay_counter.step()
            number -= 1
            self.replay_step_up()
            if self.game.replays == 899:
                number = 0
            self.delay(name="card5_replay_step_up", delay=0.25, handler=self.card5_replay_step_up, param=number)
        else:
            self.game.search_index.disengage()
            self.cancel_delayed(name="card5_replay_step_up")
            self.search_sounds()
            self.search()

    def card6_replay_step_up(self, number):
        self.game.sound.stop_music()
        if number >= 1:
            self.game.card6_replay_counter.step()
            number -= 1
            self.replay_step_up()
            if self.game.replays == 899:
                number = 0
            self.delay(name="card6_replay_step_up", delay=0.25, handler=self.card6_replay_step_up, param=number)
        else:
            self.game.search_index.disengage()
            self.cancel_delayed(name="card6_replay_step_up")
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
        # Card #1
        self.pos[0] = {}
        self.pos[1] = {5:1, 1:2, 14:3, 17:4, 9:5}
        self.pos[2] = {13:1, 15:2, 8:3, 21:4, 24:5}
        self.pos[3] = {4:1, 19:2, 23:3, 10:4, 2:5}
        self.pos[4] = {25:1, 20:2, 11:3, 16:4, 6:5}
        self.pos[5] = {12:1, 7:2, 3:3, 22:4, 18:5}
        self.pos[6] = {5:1, 13:2, 4:3, 25:4, 12:5}
        self.pos[7] = {1:1, 15:2, 19:3, 20:4, 7:5}
        self.pos[8] = {14:1, 8:2, 23:3, 11:4, 3:5}
        self.pos[9] = {17:1, 21:2, 10:3, 16:4, 22:5}
        self.pos[10] = {9:1, 24:2, 2:3, 6:4, 18:5}
        self.pos[11] = {5:1, 15:2, 23:3, 16:4, 18:5}
        self.pos[12] = {9:1, 21:2, 23:3, 20:4, 12:5}
        self.pos[13] = {}

        # Card #2
        self.pos[14] = {}
        self.pos[15] = {7:1, 13:2, 6:3, 21:4, 10:5}
        self.pos[16] = {8:1, 16:2, 4:3, 17:4, 25:5}
        self.pos[17] = {1:1, 18:2, 24:3, 19:4, 3:5}
        self.pos[18] = {22:1, 14:2, 20:3, 9:4, 15:5}
        self.pos[19] = {11:1, 2:2, 5:3, 23:4, 12:5}
        self.pos[20] = {7:1, 8:2, 1:3, 22:4, 11:5}
        self.pos[21] = {13:1, 16:2, 18:3, 14:4, 2:5}
        self.pos[22] = {6:1, 4:2, 24:3, 20:4, 5:5}
        self.pos[23] = {21:1, 17:2, 19:3, 9:4, 23:5}
        self.pos[24] = {10:1, 25:2, 3:3, 15:4, 12:5}
        self.pos[25] = {7:1, 16:2, 24:3, 9:4, 12:5}
        self.pos[26] = {10:1, 17:2, 24:3, 14:4, 11:5}
        self.pos[27] = {}

        # Card #3
        self.pos[28] = {}
        self.pos[29] = {3:1, 12:2, 2:3, 24:4, 8:5}
        self.pos[30] = {4:1, 17:2, 15:3, 6:4, 20:5}
        self.pos[31] = {9:1, 18:2, 25:3, 14:4, 10:5}
        self.pos[32] = {16:1, 11:2, 7:3, 19:4, 23:5}
        self.pos[33] = {13:1, 22:2, 5:3, 21:4, 1:5}
        self.pos[34] = {3:1, 4:2, 9:3, 16:4, 13:5}
        self.pos[35] = {12:1, 17:2, 18:3, 11:4, 22:5}
        self.pos[36] = {2:1, 15:2, 25:3, 7:4, 5:5}
        self.pos[37] = {24:1, 6:2, 14:3, 19:4, 21:5}
        self.pos[38] = {8:1, 20:2, 10:3, 23:4, 1:5}
        self.pos[39] = {3:1, 17:2, 25:3, 19:4, 1:5}
        self.pos[40] = {8:1, 6:2, 25:3, 11:4, 13:5}
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

        # Card #4
        self.pos[51] = {}
        self.pos[52] = {16:1, 25:2, 20:3, 6:4, 11:5}
        self.pos[53] = {17:1, 5:2, 1:3, 9:4, 14:5}
        self.pos[54] = {21:1, 13:2, 15:3, 24:4, 8:5}
        self.pos[55] = {22:1, 12:2, 7:3, 18:4, 3:5}
        self.pos[56] = {10:1, 4:2, 19:3, 2:4, 23:5}
        self.pos[57] = {16:1, 17:2, 21:3, 22:4, 10:5}
        self.pos[58] = {25:1, 5:2, 13:3, 12:4, 4:5}
        self.pos[59] = {20:1, 1:2, 15:3, 7:4, 19:5}
        self.pos[60] = {6:1, 9:2, 24:3, 18:4, 2:5}
        self.pos[61] = {11:1, 14:2, 8:3, 3:4, 23:5}
        self.pos[62] = {16:1, 5:2, 15:3, 18:4, 23:5}
        self.pos[63] = {11:1, 9:2, 15:3, 12:4, 10:5}
        self.pos[64] = {}
        self.pos[65] = {}
        self.pos[66] = {}
        self.pos[67] = {}

        # Card #5
        self.pos[68] = {}
        self.pos[69] = {9:1, 22:2, 14:3, 15:4, 20:5}
        self.pos[70] = {21:1, 7:2, 13:3, 10:4, 6:5}
        self.pos[71] = {17:1, 8:2, 16:3, 25:4, 4:5}
        self.pos[72] = {23:1, 11:2, 2:3, 12:4, 5:5}
        self.pos[73] = {19:1, 1:2, 18:3, 3:4, 24:5}
        self.pos[74] = {9:1, 21:2, 17:3, 23:4, 19:5}
        self.pos[75] = {22:1, 7:2, 8:3, 11:4, 1:5}
        self.pos[76] = {14:1, 13:2, 16:3, 2:4, 18:5}
        self.pos[77] = {15:1, 10:2, 25:3, 12:4, 3:5}
        self.pos[78] = {20:1, 6:2, 4:3, 5:4, 24:5}
        self.pos[79] = {9:1, 7:2, 16:3, 12:4, 24:5}
        self.pos[80] = {20:1, 10:2, 16:3, 11:4, 19:5}
        self.pos[81] = {}
        self.pos[82] = {}
        self.pos[83] = {}
        self.pos[84] = {}

        # Card #6
        self.pos[85] = {}
        self.pos[86] = {19:1, 16:2, 11:3, 23:4, 7:5}
        self.pos[87] = {24:1, 3:2, 12:3, 8:4, 2:5}
        self.pos[88] = {6:1, 4:2, 17:3, 20:4, 15:5}
        self.pos[89] = {21:1, 13:2, 22:3, 1:4, 5:5}
        self.pos[90] = {14:1, 9:2, 18:3, 10:4, 25:5}
        self.pos[91] = {19:1, 24:2, 6:3, 21:4, 14:5}
        self.pos[92] = {16:1, 3:2, 4:3, 13:4, 9:5}
        self.pos[93] = {11:1, 12:2, 17:3, 22:4, 18:5}
        self.pos[94] = {23:1, 8:2, 20:3, 1:4, 10:5}
        self.pos[95] = {7:1, 2:2, 15:3, 5:4, 25:5}
        self.pos[96] = {19:1, 3:2, 17:3, 1:4, 25:5}
        self.pos[97] = {7:1, 8:2, 17:3, 13:4, 14:5}
        self.pos[98] = {}
        self.pos[99] = {}
        self.pos[100] = {}

        card = 0

        if rivets in range(0,14):
            card = 1
        if rivets in range(14,28):
            card = 2
        if rivets in range(28,50):
            card = 3
        if rivets in range(50,68):
            card = 4
        if rivets in range(68,85):
            card = 5
        if rivets in range(85,100):
            card = 6

        return (self.pos[rivets], card)

    def scan_all(self):
        #Animate scanning of everything - this happens through the flash disc
        self.all_probability()

    def check_reflex2(self):
        r2 = self.game.reflex2.position
        mix1 = self.game.mixer1.connected_rivet()
        if r2 in [15,16,17,19]:
            if mix1 in [3,5]:
                return 1
            else:
                return 0
        elif r2 in range(19,23):
            if mix1 in [3,9,14,21]:
                return 1
            else:
                return 0
        elif r2 == 5 or r2 in range (23,30):
            if mix1 in [2,6,11,17,21]:
                return 1
            else:
                return 0
        elif r2 in range(30,36):
            if mix1 in [0,5,8,12,17,20,23]:
                return 1
            else:
                return 0
        elif r2 in range(36,44):
            if mix1 in [0,2,6,8,11,14,15,18,20,23]:
                return 1
            else:
                return 0
        elif r2 in range(44,49):
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
        if mix2 in range(0,10) or mix2 in [11,13,15,17,19,21,23]:
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
                if mix2 in [6,3]:
                    return 1
            elif self.game.c4_double.status == False:
                if mix2 in [8,22,24]:
                    return 1
            else:
                return 0

    def all_probability(self):
        r2 = self.check_reflex2()
        if r2 == 1:
            m2 = self.check_mixer2()
            if m2 == 1:
                sd = self.game.flash.connected_rivet()
                # Check for double/triple scoring per card
                if sd in [12,15,18,24,38,42,44]:
                    if self.game.c1_triple.status == False:
                        if self.game.c1_double.status == False:
                            self.game.c1_double.engage(self.game)
                            self.game.sound.play('tilt')
                if sd in [0,8,30,31,33,45,47]:
                    if self.game.c2_triple.status == False:
                        if self.game.c2_double.status == False:
                            self.game.c2_double.engage(self.game)
                            self.game.sound.play('tilt')
                if sd in [2,10,11,13,25,27,49]:
                    if self.game.c3_triple.status == False:
                        if self.game.c3_double.status == False:
                            self.game.c3_double.engage(self.game)
                            self.game.sound.play('tilt')
                if sd in [3,5,6,7,9,22,28,32,40]:
                    if self.game.c4_triple.status == False:
                        if self.game.c4_double.status == False:
                            self.game.c4_double.engage(self.game)
                            self.game.sound.play('tilt')
                    if self.game.c6_triple.status == False:
                        if self.game.c6_double.status == False:
                            self.game.c6_double.engage(self.game)
                            self.game.sound.play('tilt')
                if sd in [1,14,20,26,29,37,43]:
                    if self.game.c5_triple.status == False:
                        if self.game.c5_double.status == False:
                            self.game.c5_double.engage(self.game)
                            self.game.sound.play('tilt')

                # Now we need to check Mixer1 if we're at card #6
                if self.game.selector.position == 6:
                    mix1 = self.game.mixer1.connected_rivet()
                    if mix1 in [0,11]:
                        if self.game.c1_triple.status == False:
                            self.game.c1_double.disengage()
                            self.game.c1_triple.engage(self.game)
                            self.game.sound.play('tilt')
                    if mix1 in [1,12]:
                        if self.game.c2_triple.status == False:
                            self.game.c2_double.disengage()
                            self.game.c2_triple.engage(self.game)
                            self.game.sound.play('tilt')
                    if mix1 in [3,10,14]:
                        if self.game.c3_triple.status == False:
                            self.game.c3_double.disengage()
                            self.game.c3_triple.engage(self.game)
                            self.game.sound.play('tilt')
                    if mix1 in [2,17,19]:
                        if self.game.c4_triple.status == False:
                            self.game.c4_double.disengage()
                            self.game.c4_triple.engage(self.game)
                            self.game.sound.play('tilt')
                    if mix1 in [5,6,16,18]:
                        if self.game.c5_triple.status == False:
                            self.game.c5_double.disengage()
                            self.game.c5_triple.engage(self.game)
                            self.game.sound.play('tilt')
                    if mix1 in [4,7,8,15]:
                        if self.game.c6_triple.status == False:
                            self.game.c6_double.disengage()
                            self.game.c6_triple.engage(self.game)
                            self.game.sound.play('tilt')
                else:
                    if sd in [16,48]:
                        if self.game.c1_triple.status == False:
                            self.game.c1_double.disengage()
                            self.game.c1_triple.engage(self.game)
                            self.game.sound.play('tilt')
                    if sd in [4,41]:
                        if self.game.c2_triple.status == False:
                            self.game.c2_double.disengage()
                            self.game.c2_triple.engage(self.game)
                            self.game.sound.play('tilt')
                    if sd in [17,19]:
                        if self.game.c3_triple.status == False:
                            self.game.c3_double.disengage()
                            self.game.c3_triple.engage(self.game)
                            self.game.sound.play('tilt')
                    if sd in [23,34]:
                        if self.game.c4_triple.status == False:
                            self.game.c4_double.disengage()
                            self.game.c4_triple.engage(self.game)
                            self.game.sound.play('tilt')
                    if sd in [35,46]:
                        if self.game.c5_triple.status == False:
                            self.game.c5_double.disengage()
                            self.game.c5_triple.engage(self.game)
                            self.game.sound.play('tilt')
                    if sd in [21,36,39]:
                        if self.game.c6_triple.status == False:
                            self.game.c6_double.disengage()
                            self.game.c6_triple.engage(self.game)
                            self.game.sound.play('tilt')


                # Check for multi-steps on the cards
                if sd in [0,17,22]:
                    if self.game.fourteen_eighteen.status == False:
                        self.game.fourteen_eighteen.engage(self.game)
                        self.game.sound.play('tilt')
                if self.game.c5_triple.status == False:
                    if sd == 2:
                        if self.game.fourteen_eighteen.status == False:
                            self.game.fourteen_eighteen.engage(self.game)
                            self.game.sound.play('tilt')
                if self.game.c2_triple.status == False:
                    if sd == 5:
                        if self.game.fourteen_eighteen.status == False:
                            self.game.fourteen_eighteen.engage(self.game)
                            self.game.sound.play('tilt')
                if sd in [15,1,24,12,7]:
                    if self.game.fifteen_seventeen.status == False:
                        self.game.fifteen_seventeen.engage(self.game)
                        self.game.sound.play('tilt')
                if self.game.c3_triple.status == False:
                    if sd == 6:
                        if self.game.fifteen_seventeen.status == False:
                            self.game.fifteen_seventeen.engage(self.game)
                            self.game.sound.play('tilt')
                if sd in [3,10,13,14]:
                    if self.game.sixteen.status == False:
                        self.game.sixteen.engage(self.game)
                        self.game.sound.play('tilt')
                if self.game.c4_triple.status == False:
                    if sd == 8:
                        if self.game.sixteen.status == False:
                            self.game.sixteen.engage(self.game)
                            self.game.sound.play('tilt')
                if self.game.c1_triple.status == False:
                    if sd == 20:
                        if self.game.sixteen.status == False:
                            self.game.sixteen.engage(self.game)
                            self.game.sound.play('tilt')
                if self.game.c6_triple.status == False:
                    if sd == 18:
                        if self.game.sixteen.status == False:
                            self.game.sixteen.engage(self.game)
                            self.game.sound.play('tilt')
                if sd in [11,9,21,4,16,19,23]:
                    # Check Mixer 1 to determine if we can step multiple cards
                    mix1 = self.game.mixer1.position
                    if self.game.selector.position == 1:
                        if mix1 in [9,11,14,17,21,24]:
                            z = self.check_multi_step()
                            if z == 1:
                                n = random.randint(1,4)
                                extra_step(n)
                    if self.game.selector.position == 2:
                        if mix1 in [1,4,7,8,13,16,18,20,23]:
                            z = self.check_multi_step()
                            if z == 1:
                                n = random.randint(1,4)
                                extra_step(n)
                    if self.game.selector.position == 3:
                        if mix1 in [2,3,12,15,22]:
                            z = self.check_multi_step()
                            if z == 1:
                                n = random.randint(1,4)
                                extra_step(n)
                    if self.game.selector.position == 4:
                        if mix1 in [5,6,19]:
                            z = self.check_multi_step()
                            if z == 1:
                                n = random.randint(1,4)
                                extra_step(n)
                    if self.game.selector.position == 5:
                        if mix1 in [0,10]:
                            z = self.check_multi_step()
                            if z == 1:
                                n = random.randint(1,4)
                                extra_step(n)
            self.delay(name="display", delay=0.1, handler=graphics.showboat.display, param=self)

    def extra_step(self, number):
        if number > 0:
            self.game.selector.step()
            self.delay(name="display", delay=0.1, handler=graphics.showboat.display, param=self)
            number -= 1
            self.delay(name="extra_step", delay=0.1, handler=self.extra_step, param=number)

    def check_multi_step(self):
        i = random.randint(0,32)
        if i == 16:
            return 1
        else:
            return 0

    def animate_both(self, args):
        start = args[0]
        diff = args[1]
        num = args[2]
        if start + num >= 25:
            start = 0
        if diff >= 0:
            num = num + 1
            rivet = start + num
            if rivet in [1,3,12,14,17,21,24,26,29,32,34,37,41,44,47,49]:
                self.game.mixer1.step()
                graphics.showboat.animate_mixer1(self)
            if rivet in [2,6,10,11,20,23,27,31,35,36,45,48,50]:
                self.game.mixer2.step()
                graphics.showboat.animate_mixer2(self)
            graphics.showboat.both_animation([self, start + num])
            self.cancel_delayed(name="display")
            diff = diff - 1
            args = [start,diff,num]
            self.delay(name="both_animation", delay=0.08, handler=self.animate_both, param=args)
        else:
            self.cancel_delayed(name="both_animation")
            self.delay(name="display", delay=0.1, handler=graphics.showboat.display, param=self)
            self.scan_all()

    # Define reset as the knock-off, anti-cheat relay disabled, and replay reset enabled.  Motors turn while credits are knocked off.
    # When meter reaches zero and the zero limit switch is hit, turn off motor sound and leave backglass gi on, but with tilt displayed.

    def startup(self):        
        # Every bingo requires the meter to register '0' 
        # before allowing coin entry --
        # also needs to show a plain 'off' backglass.
        self.eb = False
        self.tilt_actions()


class Showboat(procgame.game.BasicGame):
    """ Showboat is the only United six card """
    def __init__(self, machine_type):
        super(Showboat, self).__init__(machine_type)
        # NOTE: trough_count only counts the number of switches present in the  trough.  It does _not_ count
        #       the number of balls present.   In this game, there  should  be  8  balls.
        pygame.mixer.pre_init(44100,-16,2,512)
        self.sound = procgame.sound.SoundController(self)
        self.sound.set_volume(1.0)
        self.trough_count = 6

        # Now, the control unit can be in one of two positions, essentially.
        self.cu = 1

        # Subclass my units unique to this game -  modifications must be made to set up mixers and steppers unique to the game
        # NOTE: 'top' positions are indexed using a 0 index, so the top on a 24 position unit is actually 23.

        self.mixer1 = units.Mixer("mixer1", 23)
        self.mixer1.position = random.randint(0,23)
        self.mixer2 = units.Mixer("mixer2", 23)
        self.mixer2.spin()

        self.searchdisc = units.Search("searchdisc", 49)
        self.searchdisc2 = units.Search("searchdisc", 49)

        #Search relays
        self.s1 = units.Relay("s1")
        self.s2 = units.Relay("s2")
        self.s3 = units.Relay("s3")
        self.s4 = units.Relay("s4")
        self.s5 = units.Relay("s5")

        #Replay Counter
        self.card1_replay_counter = units.Stepper("card1_replay_counter", 200)
        self.card2_replay_counter = units.Stepper("card2_replay_counter", 200)
        self.card3_replay_counter = units.Stepper("card3_replay_counter", 200)
        self.card4_replay_counter = units.Stepper("card4_replay_counter", 200)
        self.card5_replay_counter = units.Stepper("card5_replay_counter", 200)
        self.card6_replay_counter = units.Stepper("card6_replay_counter", 200)
        
        #Initialize stepper units used to keep track of features or timing.
        self.timer = units.Stepper("timer", 40)
        self.ball_count = units.Stepper("ball_count", 8)

        # Initialize reflex(es) and mixers unique to this game
        # NOTE:  Reflexes in United games are actually comprised of two
        # separate steppers.  These act as normal continuous steppers, so I
        # need to subclass as steppers.
        self.reflex1 = units.Stepper("reflex1", 50, "Showboat", "continuous")
        self.reflex2 = units.Stepper("reflex2", 50, "Showboat")

        self.search_index = units.Relay("search_index")

        #In United games, they call this spotting motor the 'flash' motor, 
        #similar to the ball bowlers.
        self.flash = units.Spotting("flash", 50)

        #Check for status of the replay register zero switch.  If positive
        #and machine is just powered on, this will zero out the replays.
        self.replay_reset = units.Relay("replay_reset")
        
        #Extra ball unit contains 3 positions.  Max of 3 EBs.
        self.extra_ball = units.Stepper("extra_ball", 3)

        #When engage()d, light 6v circuit, and enable game features, scoring,
        #etc. Disengage()d means that the machine is 'soft' tilted. In United
        #games, they call this the lock relay, similar to many other pin
        #manufacturers.
        self.lock = units.Relay("lock")

        #Card score doubling trip relays
        self.c1_double = units.Relay("c1_double")
        self.c2_double = units.Relay("c2_double")
        self.c3_double = units.Relay("c3_double")
        self.c4_double = units.Relay("c4_double")
        self.c5_double = units.Relay("c5_double")
        self.c6_double = units.Relay("c6_double")

        #Card score tripling trip relays
        self.c1_triple = units.Relay("c1_triple")
        self.c2_triple = units.Relay("c2_triple")
        self.c3_triple = units.Relay("c3_triple")
        self.c4_triple = units.Relay("c4_triple")
        self.c5_triple = units.Relay("c5_triple")
        self.c6_triple = units.Relay("c6_triple")

        #Selector keeps track of cards in play - in United games, they call
        #this the card step-up, but I'll call it selector for consistency with other
        #multi-card Bally games.
        self.selector = units.Stepper("selector", 6)

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

        #Relays for spotted numbers
        self.sixteen = units.Relay("sixteen")
        self.fifteen_seventeen = units.Relay("fifteen_seventeen")
        self.fourteen_eighteen = units.Relay("fourteen_eighteen")

        self.replays = 0
        self.returned = False

    def reset(self):
        super(Showboat, self).reset()
        self.logger = logging.getLogger('game')
        self.load_config('bingo.yaml')
        self.lock.engage(game)
        
        main_mode = MulticardBingo(self)
        self.modes.add(main_mode)
        

game = Showboat(machine_type='pdb')
game.reset()
game.run_loop()
