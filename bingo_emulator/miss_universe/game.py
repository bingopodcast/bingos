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
from bingo_emulator.graphics.miss_universe import *

class SinglecardBingo(procgame.game.Mode):
    def __init__(self, game):
        super(SinglecardBingo, self).__init__(game=game, priority=5)
        self.holes = []
        self.startup()
        self.game.sound.register_music('motor', "audio/magic_screen_control_unit.wav")
        self.game.sound.register_sound('search', "audio/magic_screen_search_default.wav")
        self.game.sound.register_sound('search_screen', "audio/magic_screen_search.wav")
        self.game.sound.register_sound('coin1', "audio/magic_screen_coin1.wav")
        self.game.sound.register_sound('coin2', "audio/magic_screen_coin2.wav")
        self.game.sound.register_sound('coin3', "audio/magic_screen_coin3.wav")
        self.game.sound.register_sound('magic_screen', "audio/magic_screen.wav")
        self.game.sound.register_sound('tilt', "audio/tilt.wav")
        self.game.sound.register_sound('step', "audio/step.wav")
        self.game.sound.register_sound('eb_search', "audio/EB_Search.wav")

    def sw_coin_active(self, sw):
        self.game.tilt.disengage()
        self.regular_play()

        self.delay(name="display", delay=0.1, handler=graphics.miss_universe.display, param=self)

    def sw_startButton_active(self, sw):
        if self.game.replays > 0 or self.game.switches.freeplay.is_active():
            self.game.tilt.disengage()
            self.regular_play()
            self.delay(name="display", delay=0.1, handler=graphics.miss_universe.display, param=self)

    def sw_blue_active(self, sw):
        if self.game.switches.drawer.is_inactive():
            if self.game.spot.position >= 1:
                self.game.select_spot.step()
                self.check_spot()
            self.delay(name="display", delay=0.1, handler=graphics.miss_universe.display, param=self)

    def sw_lettera_active(self, sw):
        if self.game.switches.drawer.is_active():
            if self.game.spot.position >= 1:
                self.game.select_spot.position = 0
                self.check_spot()
            self.delay(name="display", delay=0.1, handler=graphics.miss_universe.display, param=self)

    def sw_letterb_active(self, sw):
        if self.game.switches.drawer.is_active():
            if self.game.spot.position >= 1:
                self.game.select_spot.position = 1
                self.check_spot()
            self.delay(name="display", delay=0.1, handler=graphics.miss_universe.display, param=self)

    def sw_letterc_active(self, sw):
        if self.game.switches.drawer.is_active():
            if self.game.spot.position >= 1:
                self.game.select_spot.position = 2
                self.check_spot()
            self.delay(name="display", delay=0.1, handler=graphics.miss_universe.display, param=self)

    def sw_enter_active(self, sw):
        if self.game.switches.left.is_active() and self.game.switches.right.is_active():
            self.game.end_run_loop()
            os.system("/home/nbaldridge/proc/bingo_emulator/start_game.sh miss_universe")
        else:
            if self.game.ball_count.position >= 2:
                self.game.sound.stop_music()
                self.game.sound.play_music('motor', -1)
                self.game.timer.reset()
                if self.game.search_index.status == False:
                    self.search()
                    self.timeout_actions()
                                
                self.delay(name="display", delay=0.1, handler=graphics.miss_universe.display, param=self)

    def sw_trough4_active_for_1s(self, sw):
        if self.game.ball_count.position >= 4:
            self.timeout_actions()
            self.game.sound.stop_music()
    
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

    def sw_left_active(self, sw):
        if self.game.ball_count.position > 0:
            max_ball = 3
            if self.game.ball_count.position < max_ball:
                if self.game.line_feature.position in [0,1,2]:
                    return
                elif self.game.line_feature.position in [3,4]:
                    if self.game.down.status == False:
                        if self.game.line.position in [0,2]:
                            self.game.line.position == 3
                        else:
                            self.game.line.position == 0
                        if self.game.line.position < 3:
                            self.game.sound.play('magic_screen')
                            self.game.line.step()
                            self.cancel_delayed("line_animation")
                            self.animate_line([self.game,1,'up'])
                    else:
                        pass
                else:
                    if self.game.line_feature.position == 5:
                        if self.game.line.position < 3:
                            self.game.sound.play('magic_screen')
                            self.game.line.step()
                            self.cancel_delayed("line_animation")
                            self.animate_line([self.game,1,'up'])
            self.delay(name="display", delay=0.1, handler=graphics.miss_universe.display, param=self)

    def sw_left_active_for_500ms(self,sw):
        if self.game.ball_count.position > 0:
            max_ball = 3
            if self.game.ball_count.position < max_ball:
                if self.game.line_feature.position in [0,1,2]:
                    return
                elif self.game.line_feature.position in [3,4]:
                    if self.game.down.status == False:
                        if self.game.line.position in [0,2]:
                            self.game.line.position == 3
                        else:
                            self.game.line.position == 0
                        if self.game.line.position < 3:
                            self.game.sound.play('magic_screen')
                            self.game.line.step()
                            self.cancel_delayed("line_animation")
                            self.animate_line([self.game,1,'up'])
                    else:
                        pass
                else:
                    if self.game.line_feature.position == 5:
                        if self.game.line.position < 3:
                            self.game.sound.play('magic_screen')
                            self.game.line.step()
                            self.cancel_delayed("line_animation")
                            self.animate_line([self.game,1,'up'])
            self.delay(name="display", delay=0.1, handler=graphics.miss_universe.display, param=self)
            self.delay(name="left", delay=0.5, handler=self.sw_left_active_for_500ms, param=sw)

    def sw_right_active(self, sw):
        max_ball = 3
        if self.game.ball_count.position < max_ball:
            if self.game.line_feature.position in [0,1,2]:
                return
            elif self.game.line_feature.position in [3,4]:
                if self.game.down.status == True:
                    if self.game.line.position != 0:
                        self.cancel_delayed("line_animation")
                        self.animate_line([self.game,1,'down'])
                        self.game.sound.play('magic_screen')
                        self.game.line.stepdown()
                else:
                    pass
            else:
                if self.game.line_feature.position == 5:
                    if self.game.line.position != 0:
                        self.cancel_delayed("line_animation")
                        self.animate_line([self.game,1,'down'])
                        self.game.sound.play('magic_screen')
                        self.game.line.stepdown()
        self.delay(name="display", delay=0.1, handler=graphics.miss_universe.display, param=self)

    def sw_right_active_for_500ms(self,sw):
        max_ball = 3
        if self.game.ball_count.position < max_ball:
            if self.game.line_feature.position in [0,1,2]:
                return
            elif self.game.line_feature.position in [3,4]:
                if self.game.down.status == True:
                    if self.game.line.position != 0:
                        self.cancel_delayed("line_animation")
                        self.animate_line([self.game,1,'down'])
                        self.game.sound.play('magic_screen')
                        self.game.line.stepdown()
                else:
                    pass
            else:
                if self.game.line_feature.position == 5:
                    if self.game.line.position != 0:
                        self.cancel_delayed("line_animation")
                        self.animate_line([self.game,1,'down'])
                        self.game.sound.play('magic_screen')
                        self.game.line.stepdown()
        self.delay(name="display", delay=0.1, handler=graphics.miss_universe.display, param=self)
        self.delay(name="right", delay=0.6, handler=self.sw_right_active_for_500ms, param=sw)

    def check_selection(self):
        self.delay(name="display", delay=0.1, handler=graphics.miss_universe.display, param=self)

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
        self.cancel_delayed(name="corners_replay_step_up")
        self.cancel_delayed(name="blink")
        self.cancel_delayed(name="blink_screen")
        self.cancel_delayed(name="both_animation")
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

        begin = self.game.program.position
        self.game.cu = not self.game.cu
        self.game.program.spin()
        self.game.scramble.spin()
        self.game.reflex.decrease()
        self.animate_both([begin,self.game.program.movement_amount,1])

        self.game.returned = False
        if self.game.start.status == True:
            if self.game.coin.position < 40:
                self.game.coin.step()
            else:
                self.game.extender.step()
            if self.game.selector.position < 1:
                self.game.selector.step()
            if self.game.switches.shutter.is_inactive():
                self.game.coils.shutter.enable()
            self.replay_step_down()
            graphics.miss_universe.display(self)
            self.check_lifter_status()
        else:
            self.holes = []
            self.game.start.engage(self.game)
            self.game.yellow_odds.reset()
            self.game.green_odds.reset()
            self.game.ball_count.reset()
            self.game.down.disengage()
            self.game.spot.reset()
            self.game.mystery_yellow.disengage()
            self.game.mystery_red.disengage()
            self.game.timer.reset()
            if self.game.line.position > 0:
                self.line_reset(self.game.line.position)
            self.game.line_feature.reset()
            self.game.red_replay_counter.reset()
            self.game.corners_replay_counter.reset()
            self.game.yellow_replay_counter.reset()
            self.game.green_replay_counter.reset()
            self.game.red_odds.reset()
            self.game.selector.reset()
            self.game.corners192.disengage()
            self.game.corners384.disengage()
            self.game.timer.reset()
            self.game.sound.play_music('motor', -1)
            self.regular_play()
        self.delay(name="display", delay=0.1, handler=graphics.miss_universe.display, param=self)
        self.game.tilt.disengage()

    def line_reset(self, number):
        if number > 0:
            self.cancel_delayed("line_animation")
            self.animate_line([self.game,1,'down'])
            self.game.sound.play('magic_screen')
            self.game.line.stepdown()
            self.delay(name="display", delay=0, handler=graphics.miss_universe.display, param=self)
            number -= 1
            self.delay(name="line_reset", delay=0.6, handler=self.line_reset, param=number)


    def check_lifter_status(self):
        if self.game.tilt.status == False:
            if self.game.switches.trough8.is_closed() and self.game.switches.trough5.is_open() and self.game.switches.trough4.is_open() and self.game.switches.trough3.is_closed() and self.game.switches.trough2.is_closed():
                if self.game.switches.shooter.is_open():
                    self.game.coils.lifter.enable()
                    self.game.returned = False
            else:
                if self.game.start.status == False:
                    if self.game.ball_count <= 2:
                        if self.game.switches.shooter.is_open():
                            if self.game.switches.gate.is_closed():
                                self.game.coils.lifter.enable()
                    else:
                        if self.game.returned == True and self.game.ball_count.position == 3:
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
                if self.game.ball_count.position < 3:
                    self.game.coils.lifter.enable()

    def sw_gate_inactive_for_1ms(self, sw):
        self.game.start.disengage()
        self.game.ball_count.step()
        if self.game.switches.shutter.is_active():
            self.game.coils.shutter.enable()
        if self.game.ball_count.position == 3:
            self.game.sound.play('tilt')
            self.game.sound.play('tilt')
        if self.game.mystery_red.status == True or self.game.mystery_yellow.status == True:
            self.game.sound.play('tilt')
            self.game.mystery_spot.spin()
            self.check_spot()
        if self.game.ball_count.position <= 2:
            self.check_lifter_status()
        self.delay(name="display", delay=0.1, handler=graphics.miss_universe.display, param=self)

    def check_spot(self):
        if self.game.spot.position >= 1:
            if self.game.select_spot.position == 0:
                if 4 not in self.holes:
                    self.holes.append(4)
                if 8 in self.holes:
                    if self.game.switches.hole8.is_inactive():
                        self.holes.remove(8)
                if 10 in self.holes:
                    if self.game.switches.hole10.is_inactive():
                        self.holes.remove(10)
            elif self.game.select_spot.position == 1:
                if 8 not in self.holes:
                    self.holes.append(8)
                if 4 in self.holes:
                    if self.game.switches.hole4.is_inactive():
                        self.holes.remove(4)
                if 10 in self.holes:
                    if self.game.switches.hole10.is_inactive():
                        self.holes.remove(10)
            elif self.game.select_spot.position == 2:
                if 10 not in self.holes:
                    self.holes.append(10)
                if 4 in self.holes:
                    if self.game.switches.hole4.is_inactive():
                        self.holes.remove(4)
                if 8 in self.holes:
                    if self.game.switches.hole8.is_inactive():
                        self.holes.remove(8)
        if self.game.spot.position >= 2:
            if self.game.select_spot.position == 0:
                if 5 not in self.holes:
                    self.holes.append(5)
                if 2 in self.holes:
                    if self.game.switches.hole2.is_inactive():
                        self.holes.remove(2)
                if 17 in self.holes:
                    if self.game.switches.hole17.is_inactive():
                        self.holes.remove(17)
            elif self.game.select_spot.position == 1:
                if 2 not in self.holes:
                    self.holes.append(2)
                if 17 in self.holes:
                    if self.game.switches.hole17.is_inactive():
                        self.holes.remove(17)
                if 5 in self.holes:
                    if self.game.switches.hole5.is_inactive():
                        self.holes.remove(5)
            elif self.game.select_spot.position == 2:
                if 17 not in self.holes:
                    self.holes.append(17)
                if 5 in self.holes:
                    if self.game.switches.hole5.is_inactive():
                        self.holes.remove(5)
                if 2 in self.holes:
                    if self.game.switches.hole2.is_inactive():
                        self.holes.remove(2)
        if self.game.spot.position >= 4:
            if self.game.select_spot.position == 0:
                if 1 not in self.holes:
                    self.holes.append(1)
                if 16 in self.holes:
                    if self.game.switches.hole16.is_inactive():
                        self.holes.remove(16)
                if 14 in self.holes:
                    if self.game.switches.hole14.is_inactive():
                        self.holes.remove(14)
            elif self.game.select_spot.position == 1:
                if 16 not in self.holes:
                    self.holes.append(16)
                if 1 in self.holes:
                    if self.game.switches.hole1.is_inactive():
                        self.holes.remove(1)
                if 14 in self.holes:
                    if self.game.switches.hole14.is_inactive():
                        self.holes.remove(14)
            elif self.game.select_spot.position == 2:
                if 14 not in self.holes:
                    self.holes.append(14)
                if 1 in self.holes:
                    if self.game.switches.hole1.is_inactive():
                        self.holes.remove(1)
                if 16 in self.holes:
                    if self.game.switches.hole16.is_inactive():
                        self.holes.remove(16)
        if self.game.mystery_red.status == True and self.game.mystery_yellow.status == False:
            if self.game.ball_count.position == 2:
                if self.game.mystery_spot.position in [0,1]:
                    if 6 not in self.holes:
                        self.holes.append(6)
                if self.game.mystery_spot.position in [2,3]:
                    if 13 not in self.holes:
                        self.holes.append(13)
                if self.game.mystery_spot.position in [4,5]:
                    if 11 not in self.holes:
                        self.holes.append(11)
        elif self.game.mystery_red.status == False and self.game.mystery_yellow.status == True:
            if self.game.ball_count.position == 2:
                if self.game.mystery_spot.position in [0,1]:
                    if 18 not in self.holes:
                        self.holes.append(18)
                if self.game.mystery_spot.position in [2,3]:
                    if 12 not in self.holes:
                        self.holes.append(12)
                if self.game.mystery_spot.position in [4,5]:
                    if 15 not in self.holes:
                        self.holes.append(15)
        elif self.game.mystery_red.status == True and self.game.mystery_yellow.status == True:
            if self.game.ball_count.position == 2:
                if self.game.mystery_spot.position in [0]:
                    if 18 not in self.holes:
                        self.holes.append(18)
                if self.game.mystery_spot.position in [1]:
                    if 6 not in self.holes:
                        self.holes.append(6)
                if self.game.mystery_spot.position in [2]:
                    if 12 not in self.holes:
                        self.holes.append(12)
                if self.game.mystery_spot.position in [3]:
                    if 13 not in self.holes:
                        self.holes.append(13)
                if self.game.mystery_spot.position in [4]:
                    if 15 not in self.holes:
                        self.holes.append(15)
                if self.game.mystery_spot.position in [5]:
                    if 11 not in self.holes:
                        self.holes.append(11)
           



    # This is really nasty, but it is how we render graphics for each individual hole.
    # numbers are added (or removed from) a list.  In this way, I can re-use the same
    # routine even for games where there are ball return functions like Surf Club.

    def sw_hole1_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(1)
            self.delay(name="display", delay=0.1, handler=graphics.miss_universe.display, param=self)

    def sw_hole2_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(2)
            self.delay(name="display", delay=0.1, handler=graphics.miss_universe.display, param=self)

    def sw_hole3_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(3)
            self.delay(name="display", delay=0.1, handler=graphics.miss_universe.display, param=self)

    def sw_hole4_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(4)
            self.delay(name="display", delay=0.1, handler=graphics.miss_universe.display, param=self)

    def sw_hole5_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(5)
            self.delay(name="display", delay=0.1, handler=graphics.miss_universe.display, param=self)

    def sw_hole6_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(6)
            self.delay(name="display", delay=0.1, handler=graphics.miss_universe.display, param=self)

    def sw_hole7_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(7)
            self.delay(name="display", delay=0.1, handler=graphics.miss_universe.display, param=self)

    def sw_hole8_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(8)
            self.delay(name="display", delay=0.1, handler=graphics.miss_universe.display, param=self)

    def sw_hole9_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(9)
            self.delay(name="display", delay=0.1, handler=graphics.miss_universe.display, param=self)

    def sw_hole10_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(10)
            self.delay(name="display", delay=0.1, handler=graphics.miss_universe.display, param=self)

    def sw_hole11_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(11)
            self.delay(name="display", delay=0.1, handler=graphics.miss_universe.display, param=self)

    def sw_hole12_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(12)
            self.delay(name="display", delay=0.1, handler=graphics.miss_universe.display, param=self)

    def sw_hole13_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(13)
            self.delay(name="display", delay=0.1, handler=graphics.miss_universe.display, param=self)

    def sw_hole14_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(14)
            self.delay(name="display", delay=0.1, handler=graphics.miss_universe.display, param=self)

    def sw_hole15_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(15)
            self.delay(name="display", delay=0.1, handler=graphics.miss_universe.display, param=self)

    def sw_hole16_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(16)
            self.delay(name="display", delay=0.1, handler=graphics.miss_universe.display, param=self)

    def sw_hole17_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(17)
            self.delay(name="display", delay=0.1, handler=graphics.miss_universe.display, param=self)

    def sw_hole18_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(18)
            self.delay(name="display", delay=0.1, handler=graphics.miss_universe.display, param=self)

    def sw_replayReset_active(self, sw):
        self.game.anti_cheat.disengage()
        self.holes = []
        graphics.miss_universe.display(self)
        self.tilt_actions()
        self.replay_step_down(self.game.replays)

    def tilt_actions(self):
        self.game.start.disengage()
        self.game.coin.reset()
        self.cancel_delayed(name="replay_reset")
        self.cancel_delayed(name="red_replay_step_up")
        self.cancel_delayed(name="yellow_replay_step_up")
        self.cancel_delayed(name="green_replay_step_up")
        self.cancel_delayed(name="corners_replay_step_up")
        self.cancel_delayed(name="blink")
        self.cancel_delayed(name="blink_screen")
        self.cancel_delayed(name="timeout")
        self.game.search_index.disengage()
        if self.game.ball_count.position == 0:
            if self.game.switches.shutter.is_active():
                self.game.coils.shutter.enable()
        self.holes = []
        self.game.yellow_odds.reset()
        self.game.green_odds.reset()
        self.game.ball_count.reset()
        self.game.down.disengage()
        self.game.mystery_yellow.disengage()
        self.game.mystery_red.disengage()
        self.game.timer.reset()
        self.game.line_feature.reset()
        self.game.red_replay_counter.reset()
        self.game.corners_replay_counter.reset()
        self.game.yellow_replay_counter.reset()
        self.game.green_replay_counter.reset()
        self.game.red_odds.reset()
        self.game.spot.reset()
        self.game.selector.reset()
        self.game.corners192.disengage()
        self.game.corners384.disengage()
        self.game.anti_cheat.engage(game)
        self.game.tilt.engage(self.game)
        self.game.sound.stop_music()
        self.game.sound.play('tilt')
        # displays "Tilt" on the backglass, you have to recoin.
        self.delay(name="display", delay=0.1, handler=graphics.miss_universe.display, param=self)

    def sw_tilt_active(self, sw):
        if self.game.tilt.status == False:
            self.tilt_actions()

    def replay_step_down(self, number=0):
        if number > 0:
            if number > 1:
                self.game.replays -= 1
                graphics.replay_step_down(self.game.replays, graphics.miss_universe.reel1, graphics.miss_universe.reel10, graphics.miss_universe.reel100, graphics.miss_universe.reel1000)
                self.game.coils.registerDown.pulse()
                number -= 1
                self.delay(name="display", delay=0, handler=graphics.miss_universe.display, param=self)
                self.delay(name="replay_reset", delay=0.13, handler=self.replay_step_down, param=number)
            elif number == 1:
                self.game.replays -= 1
                graphics.replay_step_down(self.game.replays, graphics.miss_universe.reel1, graphics.miss_universe.reel10, graphics.miss_universe.reel100, graphics.miss_universe.reel1000)
                self.game.coils.registerDown.pulse()
                number -= 1
                self.delay(name="display", delay=0, handler=graphics.miss_universe.display, param=self)
                self.cancel_delayed(name="replay_reset")
        else: 
            if self.game.replays > 0:
                self.game.replays -= 1
                graphics.replay_step_down(self.game.replays, graphics.miss_universe.reel1, graphics.miss_universe.reel10, graphics.miss_universe.reel100, graphics.miss_universe.reel1000)
                self.delay(name="display", delay=0.1, handler=graphics.miss_universe.display, param=self)
            self.game.coils.registerDown.pulse()

    def replay_step_up(self):
        if self.game.replays < 8999:
            self.game.replays += 1
            graphics.replay_step_up(self.game.replays, graphics.miss_universe.reel1, graphics.miss_universe.reel10, graphics.miss_universe.reel100, graphics.miss_universe.reel1000)
        self.game.coils.registerUp.pulse()
        self.game.reflex.increase()
        graphics.miss_universe.display(self)

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
       
        for i in range(0, 12):
            self.r = self.closed_search_relays(self.game.searchdisc.position)
            self.game.searchdisc.spin()
            self.wipers = self.r[0]
            self.red = self.r[1]
            self.yellow = self.r[2]
            self.green = self.r[3]
            self.corners = self.r[4]

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
                            self.find_winner(s, self.red, self.yellow, self.green, self.corners)
                            break
                            

    def find_winner(self, relays, red, yellow, green, corners):
        if self.game.search_index.status == False and self.game.replays < 8999:
            if self.game.red_odds.position == 1:
                redthreeodds = 4
                redfourodds = 12
                redfiveodds = 64
            elif self.game.red_odds.position == 2:
                redthreeodds = 8
                redfourodds = 24
                redfiveodds = 80
            elif self.game.red_odds.position == 3:
                redthreeodds = 12
                redfourodds = 36
                redfiveodds = 96
            elif self.game.red_odds.position == 4:
                redthreeodds = 16
                redfourodds = 48
                redfiveodds = 96
            elif self.game.red_odds.position == 5:
                redthreeodds = 24
                redfourodds = 64
                redfiveodds = 96
            elif self.game.red_odds.position == 6:
                redthreeodds = 36
                redfourodds = 72
                redfiveodds = 128
            elif self.game.red_odds.position == 7:
                redthreeodds = 48
                redfourodds = 96
                redfiveodds = 192
            elif self.game.red_odds.position == 8:
                redthreeodds = 72
                redfourodds = 144
                redfiveodds = 256
            elif self.game.red_odds.position == 9:
                redthreeodds = 96
                redfourodds = 192
                redfiveodds = 288
            elif self.game.red_odds.position == 10:
                redthreeodds = 128
                redfourodds = 256
                redfiveodds = 384
            elif self.game.red_odds.position == 11:
                redthreeodds = 160
                redfourodds = 288
                redfiveodds = 512
            elif self.game.red_odds.position == 12:
                redthreeodds = 192
                redfourodds = 384
                redfiveodds = 640
            if self.game.yellow_odds.position == 1:
                yellowthreeodds = 4
                yellowfourodds = 12
                yellowfiveodds = 64
            elif self.game.yellow_odds.position == 2:
                yellowthreeodds = 8
                yellowfourodds = 24
                yellowfiveodds = 80
            elif self.game.yellow_odds.position == 3:
                yellowthreeodds = 12
                yellowfourodds = 36
                yellowfiveodds = 96
            elif self.game.yellow_odds.position == 4:
                yellowthreeodds = 16
                yellowfourodds = 48
                yellowfiveodds = 96
            elif self.game.yellow_odds.position == 5:
                yellowthreeodds = 24
                yellowfourodds = 64
                yellowfiveodds = 96
            elif self.game.yellow_odds.position == 6:
                yellowthreeodds = 36
                yellowfourodds = 72
                yellowfiveodds = 128
            elif self.game.yellow_odds.position == 7:
                yellowthreeodds = 48
                yellowfourodds = 96
                yellowfiveodds = 192
            elif self.game.yellow_odds.position == 8:
                yellowthreeodds = 72
                yellowfourodds = 144
                yellowfiveodds = 256
            elif self.game.yellow_odds.position == 9:
                yellowthreeodds = 96
                yellowfourodds = 192
                yellowfiveodds = 288
            elif self.game.yellow_odds.position == 10:
                yellowthreeodds = 128
                yellowfourodds = 256
                yellowfiveodds = 384
            elif self.game.yellow_odds.position == 11:
                yellowthreeodds = 160
                yellowfourodds = 288
                yellowfiveodds = 512
            elif self.game.yellow_odds.position == 12:
                yellowthreeodds = 192
                yellowfourodds = 384
                yellowfiveodds = 640
            if self.game.green_odds.position == 1:
                greenthreeodds = 4
                greenfourodds = 12
                greenfiveodds = 64
            elif self.game.green_odds.position == 2:
                greenthreeodds = 8
                greenfourodds = 24
                greenfiveodds = 80
            elif self.game.green_odds.position == 3:
                greenthreeodds = 12
                greenfourodds = 36
                greenfiveodds = 96
            elif self.game.green_odds.position == 4:
                greenthreeodds = 16
                greenfourodds = 48
                greenfiveodds = 96
            elif self.game.green_odds.position == 5:
                greenthreeodds = 24
                greenfourodds = 64
                greenfiveodds = 96
            elif self.game.green_odds.position == 6:
                greenthreeodds = 36
                greenfourodds = 72
                greenfiveodds = 128
            elif self.game.green_odds.position == 7:
                greenthreeodds = 48
                greenfourodds = 96
                greenfiveodds = 192
            elif self.game.green_odds.position == 8:
                greenthreeodds = 72
                greenfourodds = 144
                greenfiveodds = 256
            elif self.game.green_odds.position == 9:
                greenthreeodds = 96
                greenfourodds = 192
                greenfiveodds = 288
            elif self.game.green_odds.position == 10:
                greenthreeodds = 128
                greenfourodds = 256
                greenfiveodds = 384
            elif self.game.green_odds.position == 11:
                greenthreeodds = 160
                greenfourodds = 288
                greenfiveodds = 512
            elif self.game.green_odds.position == 12:
                greenthreeodds = 192
                greenfourodds = 384
                greenfiveodds = 640

            redsixodds = redfiveodds + 192
            yellowsixodds = yellowfiveodds + 192
            greensixodds = greenfiveodds + 192

            if relays == 3:
                if (red == 1):
                    if self.game.search_index.status == False:
                        if self.game.red_replay_counter.position < redthreeodds:
                            self.game.search_index.engage(self.game)
                            self.red_replay_step_up(redthreeodds - self.game.red_replay_counter.position)
                if (yellow == 1):
                    if self.game.search_index.status == False:
                        if self.game.yellow_replay_counter.position < yellowthreeodds:
                            self.game.search_index.engage(self.game)
                            self.yellow_replay_step_up(yellowthreeodds - self.game.yellow_replay_counter.position)
                if (green == 1):
                    if self.game.search_index.status == False:
                        if self.game.green_replay_counter.position < greenthreeodds:
                            self.game.search_index.engage(self.game)
                            self.green_replay_step_up(greenthreeodds - self.game.green_replay_counter.position)
            if relays == 4:
                if corners:
                    if self.game.corners192.status == True:
                        if self.game.corners_replay_counter.position < 192:
                            self.game.search_index.engage(self.game)
                            self.corners_replay_step_up(192)
                    if self.game.corners384.status == True:
                        if self.game.corners_replay_counter.position < 384:
                            self.game.search_index.engage(self.game)
                            self.corners_replay_step_up(384)
                else:
                    if (red == 1):
                        if self.game.search_index.status == False:
                            if self.game.red_replay_counter.position < redfourodds:
                                self.game.search_index.engage(self.game)
                                self.red_replay_step_up(redfourodds - self.game.red_replay_counter.position)
                    if (yellow == 1):
                        if self.game.search_index.status == False:
                            if self.game.yellow_replay_counter.position < yellowfourodds:
                                self.game.search_index.engage(self.game)
                                self.yellow_replay_step_up(yellowfourodds - self.game.yellow_replay_counter.position)
                    if (green == 1):
                        if self.game.search_index.status == False:
                            if self.game.green_replay_counter.position < greenfourodds:
                                self.game.search_index.engage(self.game)
                                self.green_replay_step_up(greenfourodds - self.game.green_replay_counter.position)
            if relays == 5:
                if (red == 1):
                    if self.game.search_index.status == False:
                        if self.game.red_replay_counter.position < redfiveodds:
                            self.game.search_index.engage(self.game)
                            self.red_replay_step_up(redfiveodds - self.game.red_replay_counter.position)
                if (yellow == 1):
                    if self.game.search_index.status == False:
                        if self.game.yellow_replay_counter.position < yellowfiveodds:
                            self.game.search_index.engage(self.game)
                            self.yellow_replay_step_up(yellowfiveodds - self.game.yellow_replay_counter.position)
                if (green == 1):
                    if self.game.search_index.status == False:
                        if self.game.green_replay_counter.position < greenfiveodds:
                            self.game.search_index.engage(self.game)
                            self.green_replay_step_up(greenfiveodds - self.game.green_replay_counter.position)
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

            
    def corners_replay_step_up(self, number):
        self.game.sound.stop('search')
        if number >= 1:
            self.game.corners_replay_counter.step()
            number -= 1
            self.replay_step_up()
            if self.game.replays == 8999:
                number = 0
            self.delay(name="corners_replay_step_up", delay=0.25, handler=self.corners_replay_step_up, param=number)
        else:
            self.game.search_index.disengage()
            self.cancel_delayed(name="corners_replay_step_up")
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
        corners = False

        self.pos[0] = {}
        self.pos[1] = {16:1, 6:2, 4:3, 11:4, 9:5, 5:6}
        self.pos[2] = {7:1, 8:2, 14:3, 18:4, 2:5, 13:6}
        self.pos[3] = {10:1, 12:2, 3:3, 17:4, 1:5, 15:6}
        self.pos[4] = {}
        self.pos[5] = {16:1, 7:2, 10:3}
        self.pos[6] = {6:1, 8:2, 12:3}
        self.pos[7] = {4:1, 14:2, 3:3}
        self.pos[8] = {11:1, 18:2, 17:3}
        self.pos[9] = {9:1, 2:2, 1:3}
        self.pos[10] = {5:1, 13:2, 15:3}
        self.pos[11] = {}
        self.pos[12] = {16:1, 10:2, 5:3, 15:4}
    
        if self.game.line.position in [0,2]:
            if rivets in [0,1,5,10,4,11]:
                red = True
            if rivets in [2,6,8]:
                yellow = True
            if rivets in [3,7,9]:
                green = True
        elif self.game.line.position == 1:
            if rivets in [0,2,5,10,4,11]:
                red = True
            if rivets in [3,6,8]:
                yellow = True
            if rivets in [1,7,9]:
                green = True
        elif self.game.line.position == 2:
            if rivets in [0,3,5,10,4,11]:
                red = True
            if rivets in [1,6,8]:
                yellow = True
            if rivets in [2,7,9]:
                green = True
        
        if rivets == 12:
            corners = True
                
        return (self.pos[rivets], red, yellow, green, corners)

    
    def scan_all(self):
        self.all_probability()

    def all_probability(self):
        if self.game.red_odds.position == 0:
            self.game.red_odds.step()
        if self.game.yellow_odds.position == 0:
            self.game.yellow_odds.step()
        if self.game.green_odds.position == 0:
            self.game.green_odds.step()
        if self.game.reflex.connected_rivet() == 0:
            if self.game.red_odds.position > 0:
                self.scan_features()
        if self.game.reflex.connected_rivet() == 1:
            if self.game.red_odds.position > 0:
                self.scan_features()
        elif self.game.reflex.connected_rivet() == 2:
            if self.game.red_odds.position > 0:
                self.scan_features()
        elif self.game.reflex.connected_rivet() == 3:
            if self.game.red_odds.position > 0:
                self.scan_features()
        elif self.game.reflex.connected_rivet() == 4:
            if self.game.red_odds.position > 0:
                self.scan_features()

    def green_extra_step(self, number):
        if number > 0:
            self.game.green_odds.step()
            self.delay(name="display", delay=0.1, handler=graphics.miss_universe.display, param=self)
            number -= 1
            self.delay(name="extra_step", delay=0.1, handler=self.green_extra_step, param=number)

    def red_extra_step(self, number):
        if number > 0:
            self.game.red_odds.step()
            self.delay(name="display", delay=0.1, handler=graphics.miss_universe.display, param=self)
            number -= 1
            self.delay(name="extra_step", delay=0.1, handler=self.red_extra_step, param=number)

    def yellow_extra_step(self, number):
        if number > 0:
            self.game.yellow_odds.step()
            self.delay(name="display", delay=0.1, handler=graphics.miss_universe.display, param=self)
            number -= 1
            self.delay(name="extra_step", delay=0.1, handler=self.yellow_extra_step, param=number)

    def check_extra_step(self):
        i = random.randint(0,32)
        if i == 16:
            return 1
        else:
            return 0

    def scan_features(self):
        p = self.features_probability()

    def features_probability(self):
        self.features_spotting()

    def features_spotting(self):
        sd = self.game.program.position
        ext = self.game.extender.position
        if sd in [5,2,3,8,21,34,39,10,28]:
            if self.game.reflex.connected_rivet() >= 1:
                if self.game.cu:
                    self.game.spot.step()
        if sd in [4,37,40,41,25,32,37,41,46,9,2,21,45]:
            if self.game.coin.position < 40:
                if self.game.reflex.connected_rivet() >= 1:
                    if self.game.cu:
                        self.game.spot.step()
                else:
                    if ext in [40,45]:
                        self.game.spot.step()
        if sd in [7,13,14,21,26,33,45]:
            if self.game.coin.position < 40:
                if self.game.reflex.connected_rivet() >= 1:
                    if self.game.cu:
                        self.game.spot.step()
                elif self.game.reflex.connected_rivet() >= 2:
                    if self.game.cu:
                        self.game.line_feature.step()
            else:
                if ext == 24:
                    self.game.spot.step()
        if sd in [8,27,29,46]:
            if self.game.coin.position < 40:
                if self.game.reflex.connected_rivet() >= 1:
                    if self.game.cu:
                        self.game.line_feature.step()
            else:
                if ext in [13,53]:
                    self.game.line_feature.step()
        if sd in [10,38,39]:
            if self.game.coin.position < 40:
                if self.game.reflex.connected_rivet() >= 2:
                    if self.game.cu:
                        self.game.line_feature.step()
            else:
                if ext == 41:
                    self.game.line_feature.step()
        if sd in [0,7,33,24,26,35]:
            if self.game.coin.position < 40:
                if self.game.reflex.connected_rivet() >= 3:
                    if self.game.mystery_yellow.status == False:
                        self.game.mystery_yellow.engage(self.game)
                        self.game.sound.play('tilt')
                else:
                    self.game.spot.step()
            else:
                if ext in [37,56]:
                    if self.game.cu:
                        if self.game.mystery_red.status == False:
                            self.game.mystery_red.engage(self.game)
                            self.game.sound.play('tilt')
                    else:
                        if self.game.mystery_yellow.status == False:
                            self.game.mystery_yellow.engage(self.game)
                            self.game.sound.play('tilt')
        if sd in [14,20,35,12,21,23]:
            if self.game.reflex.connected_rivet() >= 2:
                if self.game.mystery_red.status == False:
                    self.game.mystery_red.engage(self.game)
                    self.game.sound.play('tilt')
            else:
                self.game.line_feature.step()
        if sd in [15,34,38]:
            if self.game.coin.position < 40:
                if self.game.reflex.connected_rivet() >= 2:
                    if self.game.corners384.status == False:
                        self.game.corners384.engage(self.game)
                        self.game.sound.play('tilt')
                else:
                    if self.game.corners192.status == False:
                        self.game.corners192.engage(self.game)
                        self.game.sound.play('tilt')
            else:
                if ext == 19:
                    if self.game.reflex.connected_rivet() >= 2:
                        if self.game.corners384.status == False:
                            self.game.corners384.engage(self.game)
                            self.game.sound.play('tilt')
                    else:
                        if self.game.corners192.status == False:
                            self.game.corners192.engage(self.game)
                            self.game.sound.play('tilt')
        if sd == 17:
            if self.game.corners192.status == False:
                self.game.corners192.engage(self.game)
                self.game.sound.play('tilt')
        if self.game.cu:
            if self.game.coin.position == 15:
                if self.game.down.status == False:
                    self.game.down.engage(self.game)
                    self.game.sound.play('tilt')
        if self.game.coin.position in [0,25]:
            self.game.red_odds.step()
            self.game.green_odds.step()
            self.game.yellow_odds.step()
        if sd in [0,2,4,5,6,8,9,11,15,19,20,21,23,24,26,31,37,41,42,44,47,49]:
            if self.game.coin.position < 40:
                if self.game.scramble.position in [0,5,11,14,16]:
                    self.game.red_odds.step()
            else:
                if ext == 1:
                    self.game.red_odds.step()
        if sd in [47,21,25,27]:
            if self.game.scramble.position in [0,5,11,14,16]:
                self.red_extra_step(2)
        if sd in [28,36]:
            if self.game.scramble.position in [0,5,11,14,16]:
                self.red_extra_step(3)
        if sd in [3,7,10,11,20,22,25,28,36,38,40,46,0]:
            if self.game.coin.position < 40:
                if self.game.scramble.position in [0,6,11,13]:
                    self.game.yellow_odds.step()
            else:
                if ext in [55,58]:
                    self.game.yellow_odds.step()
        if sd in [4,25,27,28,39,32]:
            if self.game.coin.position < 40:
                if self.game.scramble.position in [0,6,11,13]:
                    self.yellow_extra_step(2)
        if sd in [1,17,46]:
            if self.game.scramble.position in [0,6,11,13]:
                self.yellow_extra_step(3)
        if sd in [4,5,12,13,18,24,27,29,30,31,32,45,48]:
            if self.game.coin.position < 40:
                if self.game.scramble.position in [0,5,11,45,49]:
                    self.game.green_odds.step()
            else:
                if ext in [9,33]:
                    self.game.green_odds.step()
        if sd in [2,14,17,27,29,48]:
            if self.game.scramble.position in [0,5,11,45,49]:
                self.green_extra_step(2)
        if sd in [29,41]:
            if self.game.scramble.position in [0,5,11,45,49]:
                self.green_extra_step(3)

    def step_lines(self):
        if self.game.lines.position not in [0,2]:
            self.game.lines.step()
            self.delay(name="display", delay=0.1, handler=graphics.miss_universe.display, param=self)
            self.delay(name="step_sc", delay=0.1, handler=self.step_lines)

    def step_selection(self, number):
        if number >= 1:
            self.game.selection_feature.step()
            self.check_selection()
            number -= 1
            self.delay(name="display", delay=0.1, handler=graphics.miss_universe.display, param=self)
            self.delay(name="step_sc", delay=0.1, handler=self.step_selection, param=number)

    def animate_both(self, args):
        start = args[0]
        diff = args[1]
        num = args[2]
        if start + num >= 50:
            start = 0
        if diff >= 0:
            num = num + 1
            graphics.miss_universe.both_animation([self, start + num])
            self.cancel_delayed(name="display")
            diff = diff - 1
            args = [start,diff,num]
            self.delay(name="both_animation", delay=0.075, handler=self.animate_both, param=args)
        else:
            self.cancel_delayed(name="both_animation")
            self.delay(name="display", delay=0.1, handler=graphics.miss_universe.display, param=self)
            self.scan_all()

    def animate_line(self, args):
        self.game = args[0]
        num = args[1]
        direction = args[2]

        if num < 55:
            graphics.miss_universe.line_animation([self, num * -1,direction])
            self.cancel_delayed(name="display")
            num = num + 1
            args = [self.game,num,direction]
            self.delay(name="line_animation", delay=0.007, handler=self.animate_line, param=args)
        else:
            self.cancel_delayed(name="line_animation")
            self.delay(name="display", delay=0.1, handler=graphics.miss_universe.display, param=self)



    # Define reset as the knock-off, anti-cheat relay disabled, and replay reset enabled.  Motors turn while credits are knocked off.
    # When meter reaches zero and the zero limit switch is hit, turn off motor sound and leave backglass gi on, but with tilt displayed.

    def startup(self):        
        # Every bingo requires the meter to register '0' 
        # before allowing coin entry --
        # also needs to show a plain 'off' backglass.
        self.eb = False
        self.game.anti_cheat.engage(self.game)
        self.tilt_actions()

class MissUniverse(procgame.game.BasicGame):
    """ Miss Universe was one of two 18 hole games """
    def __init__(self, machine_type):
        super(MissUniverse, self).__init__(machine_type)
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

        self.scramble = units.Mixer("scramble", 50)

        self.searchdisc = units.Search("searchdisc", 12)

        #Search relays
        self.s1 = units.Relay("s1")
        self.s2 = units.Relay("s2")
        self.s3 = units.Relay("s3")
        self.s4 = units.Relay("s4")
        self.s5 = units.Relay("s5")
        self.search_index = units.Relay("search_index")

        #Odds steppers
        self.red_odds = units.Stepper("red_odds", 12, 'miss_universe')
        self.yellow_odds = units.Stepper("yellow_odds", 12, 'miss_universe')
        self.green_odds = units.Stepper("green_odds", 12, 'miss_universe')

        #Replay Counter
        self.red_replay_counter = units.Stepper("red_replay_counter", 1200)
        self.yellow_replay_counter = units.Stepper("yellow_replay_counter", 1200)
        self.green_replay_counter = units.Stepper("green_replay_counter", 1200)
        self.corners_replay_counter = units.Stepper("corners_replay_counter", 600)
        
        self.select_spot = units.Stepper("select_spot", 2, "miss_universe", "continuous")
        self.spot = units.Stepper("spot", 3)
        self.mystery_spot = units.Motor("mystery_spot", 5)
        self.line_feature = units.Stepper("line_feature", 5)

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

        self.selector = units.Stepper("selector", 1)

        self.line = units.Stepper("line", 3)
        
        self.down = units.Relay("down")
        self.mystery_yellow = units.Relay("mystery_yellow")
        self.mystery_red = units.Relay("mystery_red")
        self.corners192 = units.Relay("corners192")
        self.corners384 = units.Relay("corners384")
        
        self.coin = units.Stepper("coin", 40, "miss_universe")
        self.extender = units.Stepper("extender", 60, "miss_universe", "continuous")

        self.replays = 0
        self.returned = False

    def reset(self):
        super(MissUniverse, self).reset()
        self.logger = logging.getLogger('game')
        self.load_config('bingo.yaml')
        
        main_mode = SinglecardBingo(self)
        self.modes.add(main_mode)
        
game = MissUniverse(machine_type='pdb')
game.reset()
game.run_loop()
