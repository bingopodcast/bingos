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
from bingo_emulator.graphics.dixieland import *

#from modes.timeout import Timeout

class MulticardBingo(procgame.game.Mode):
    def __init__(self, game):
        super(MulticardBingo, self).__init__(game=game, priority=5)
        self.holes = []
        self.startup()
        self.game.sound.register_music('motor', "audio/six_card_motor.wav")
        self.game.sound.register_sound('search', "audio/six_card_search_old.wav")
        self.game.sound.register_sound('add', "audio/six_card_add_card.wav")
        self.game.sound.register_sound('tilt', "audio/tilt.wav")
        self.game.sound.register_sound('step', "audio/step.wav")

    def sw_coin_active(self, sw):
        self.game.tilt.disengage()
        self.regular_play()
        self.delay(name="display", delay=0.1, handler=graphics.dixieland.display, param=self)

    def sw_startButton_active(self, sw):
        if self.game.replays > 0 or self.game.switches.freeplay.is_active():
            self.game.tilt.disengage()
            self.regular_play()
            self.delay(name="display", delay=0.1, handler=graphics.dixieland.display, param=self)


    def sw_trough4_active_for_1s(self, sw):
        if self.game.ball_count.position >= 4:
        #    self.game.modes.add(Timeout(self.game, 7))
            self.game.probability.spin()

    def sw_trough8_inactive_for_1ms(self, sw):
        if self.game.start.status == False:
            self.game.ball_count.position -= 1
            self.game.returned = True
            self.check_lifter_status()

    def sw_enter_active(self, sw):
        if self.game.switches.left.is_active() and self.game.switches.right.is_active():
            self.game.end_run_loop()
            os.system("/home/nbaldridge/proc/bingo_emulator/start_game.sh dixieland")
        else:
            if self.game.ball_count.position >= 4:
                self.game.sound.stop_music()
                if self.game.search_index.status == False:
                    self.game.sound.play('search')
                    self.search()

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
        self.holes = []
        self.cancel_delayed(name="search")
        self.cancel_delayed(name="lifter_status")
        self.cancel_delayed(name="card1_replay_step_up")
        self.cancel_delayed(name="card2_replay_step_up")
        self.cancel_delayed(name="card3_replay_step_up")
        self.cancel_delayed(name="card4_replay_step_up")
        self.cancel_delayed(name="card5_replay_step_up")
        self.cancel_delayed(name="card6_replay_step_up")
        self.game.search_index.disengage()
        self.game.coils.counter.pulse()
        self.game.returned = False
        self.game.sound.stop('add')
        self.game.sound.play('add')
        self.game.reflex.decrease()
        if self.game.reflex.position < 40:
            self.game.cu = 1
        else:
            self.game.cu = 0
        self.game.probability.spin()
        if self.game.start.status == True:
            if self.game.selector.position < 11:
                self.game.selector.step()
                if self.check_corners() == True:
                    if self.game.selector.position == 1:
                        self.game.corners1.engage(self.game)
                    elif self.game.selector.position == 2:
                        self.game.corners2.engage(self.game)
                    elif self.game.selector.position == 3:
                        self.game.corners3.engage(self.game)
                    elif self.game.selector.position == 4:
                        self.game.corners4.engage(self.game)
                    elif self.game.selector.position == 5:
                        self.game.corners5.engage(self.game)
                    elif self.game.selector.position == 6:
                        self.game.corners6.engage(self.game)
                if self.check_super() == True:
                    if self.game.selector.position == 1:
                        self.game.super1.engage(self.game)
                    elif self.game.selector.position == 2:
                        self.game.super2.engage(self.game)
                    elif self.game.selector.position == 3:
                        self.game.super3.engage(self.game)
                    elif self.game.selector.position == 4:
                        self.game.super4.engage(self.game)
                    elif self.game.selector.position == 5:
                        self.game.super5.engage(self.game)
                    elif self.game.selector.position == 6:
                        self.game.super6.engage(self.game)
                if self.check_trip() == True:
                    self.game.corners_rollover.engage(self.game)
                if self.game.switches.shutter.is_inactive():
                    self.game.coils.shutter.enable()
                self.replay_step_down()
                self.check_lifter_status()
        else:
            self.game.magic = []
            self.game.coils.redROLamp.disable()
            self.game.coils.yellowROLamp.disable()
            self.game.corners_rollover.disengage()
            self.game.card1_replay_counter.reset()
            self.game.card2_replay_counter.reset()
            self.game.card3_replay_counter.reset()
            self.game.card4_replay_counter.reset()
            self.game.card5_replay_counter.reset()
            self.game.card6_replay_counter.reset()
            self.game.dd1.disengage()
            self.game.dd2.disengage()
            self.game.dd3.disengage()
            self.game.dd4.disengage()
            self.game.dd5.disengage()
            self.game.dd6.disengage()
            self.game.card1_double.disengage()
            self.game.card1_regular.disengage()
            self.game.card1_missed.disengage()
            self.game.card2_double.disengage()
            self.game.card2_regular.disengage()
            self.game.card2_missed.disengage()
            self.game.card3_double.disengage()
            self.game.card3_regular.disengage()
            self.game.card3_missed.disengage()
            self.game.card4_double.disengage()
            self.game.card4_regular.disengage()
            self.game.card4_missed.disengage()
            self.game.card5_double.disengage()
            self.game.card5_regular.disengage()
            self.game.card5_missed.disengage()
            self.game.card6_double.disengage()
            self.game.card6_regular.disengage()
            self.game.card6_missed.disengage()
            self.game.corners1.disengage()
            self.game.corners2.disengage()
            self.game.corners3.disengage()
            self.game.corners4.disengage()
            self.game.corners5.disengage()
            self.game.corners6.disengage()
            self.game.super1.disengage()
            self.game.super2.disengage()
            self.game.super3.disengage()
            self.game.super4.disengage()
            self.game.super5.disengage()
            self.game.super6.disengage()
            self.game.onetwothree.disengage()
            self.game.fourfivesix.disengage()
            self.game.start.engage(self.game)
            self.game.selector.reset()
            self.game.ball_count.reset()
            self.game.sound.play_music('motor', -1)
            self.regular_play()
        self.delay(name="display", delay=0.1, handler=graphics.dixieland.display, param=self)
        self.game.tilt.disengage()

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
            if self.game.returned == True and self.game.ball_count.position == 4:
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

    def sw_ballLift_active_for_500ms(self, sw):
        if self.game.tilt.status == False:
            if self.game.switches.shooter.is_inactive():
                if self.game.ball_count.position < 5:
                    self.game.coils.lifter.enable()

    def sw_gate_inactive_for_1ms(self, sw):
        if self.game.ball_count.position == 0:
            if self.game.corners_rollover.status == True:
                self.game.coils.redROLamp.enable()
                self.game.coils.yellowROLamp.enable()
            if self.game.selector.position >= 9:
                self.animate_magic()
            if self.game.selector.position == 11:
                self.animate_dd()
        self.game.start.disengage()
        if self.game.switches.shutter.is_active():
            self.game.coils.shutter.enable()
        self.game.ball_count.step()
        if self.game.ball_count.position == 4:
            self.game.sound.stop_music()
        self.game.probability.spin()
        if self.game.ball_count.position == 5:
            self.game.coils.redROLamp.disable()
            self.game.coils.yellowROLamp.disable()
 
    def animate_magic(self):
        #self.delay(name="add_magic", delay=0, handler=self.game.magic.append, param=1)
        #self.delay(name="display", delay=0, handler=graphics.dixieland.display, param=self)
        #self.delay(name="remove_magic", delay=0, handler=self.game.magic.remove, param=1)
        #self.delay(name="display", delay=0, handler=graphics.dixieland.display, param=self)
        #self.delay(name="add_magic", delay=0, handler=self.game.magic.append, param=7)
        #self.delay(name="display", delay=0, handler=graphics.dixieland.display, param=self)
        #self.delay(name="remove_magic", delay=0, handler=self.game.magic.remove, param=7)
        #self.delay(name="display", delay=0, handler=graphics.dixieland.display, param=self)
        self.delay(name="add_magic", delay=0, handler=self.game.magic.append, param=9)
        self.delay(name="display", delay=0, handler=graphics.dixieland.display, param=self)
        self.delay(name="remove_magic", delay=0, handler=self.game.magic.remove, param=9)
        self.delay(name="display", delay=0, handler=graphics.dixieland.display, param=self)
        #self.delay(name="add_magic", delay=0, handler=self.game.magic.append, param=22)
        #self.delay(name="display", delay=0, handler=graphics.dixieland.display, param=self)
        #self.delay(name="remove_magic", delay=0, handler=self.game.magic.remove, param=22)
        #self.delay(name="display", delay=0, handler=graphics.dixieland.display, param=self)
        #self.delay(name="add_magic", delay=0, handler=self.game.magic.append, param=25)
        #self.delay(name="display", delay=0, handler=graphics.dixieland.display, param=self)
        #self.delay(name="remove_magic", delay=0, handler=self.game.magic.remove, param=25)
        #self.delay(name="display", delay=0, handler=graphics.dixieland.display, param=self)
        self.delay(name="pick_magic", delay=0, handler=self.pick_magic)

    def animate_dd(self):
        #self.delay(name="engage_dd", delay=0, handler=self.game.dd1.engage, param=self.game)
        #self.delay(name="display", delay=0, handler=graphics.dixieland.display, param=self)
        #self.delay(name="disengage_dd", delay=0, handler=self.game.dd1.disengage)
        #self.delay(name="display", delay=0, handler=graphics.dixieland.display, param=self)
        self.delay(name="engage_dd", delay=0, handler=self.game.dd2.engage, param=self.game)
        self.delay(name="display", delay=0, handler=graphics.dixieland.display, param=self)
        self.delay(name="disengage_dd", delay=0, handler=self.game.dd2.disengage)
        self.delay(name="display", delay=0, handler=graphics.dixieland.display, param=self)
        #self.delay(name="engage_dd", delay=0, handler=self.game.dd3.engage, param=self.game)
        #self.delay(name="display", delay=0, handler=graphics.dixieland.display, param=self)
        #self.delay(name="disengage_dd", delay=0, handler=self.game.dd3.disengage)
        #self.delay(name="display", delay=0, handler=graphics.dixieland.display, param=self)
        #self.delay(name="engage_dd", delay=0, handler=self.game.dd4.engage, param=self.game)
        #self.delay(name="display", delay=0, handler=graphics.dixieland.display, param=self)
        #self.delay(name="disengage_dd", delay=0, handler=self.game.dd4.disengage)
        #self.delay(name="display", delay=0, handler=graphics.dixieland.display, param=self)
        #self.delay(name="engage_dd", delay=0, handler=self.game.dd5.engage, param=self.game)
        #self.delay(name="display", delay=0, handler=graphics.dixieland.display, param=self)
        #self.delay(name="disengage_dd", delay=0, handler=self.game.dd5.disengage)
        #self.delay(name="display", delay=0, handler=graphics.dixieland.display, param=self)
        #self.delay(name="engage_dd", delay=0, handler=self.game.dd6.engage, param=self.game)
        #self.delay(name="display", delay=0, handler=graphics.dixieland.display, param=self)
        #self.delay(name="disengage_dd", delay=0, handler=self.game.dd6.disengage)
        #self.delay(name="display", delay=0.1, handler=graphics.dixieland.display, param=self)
        self.delay(name="pick_dd", delay=0, handler=self.pick_dd)

    def pick_magic(self):
        self.game.magic_motor.spin()
        if self.game.cu == 1:
            if self.game.magic_motor.position == 1:
                self.game.magic.append(22)
                self.game.magic.append(1)
            elif self.game.magic_motor.position == 2:
                self.game.magic.append(1)
            elif self.game.magic_motor.position == 3:
                self.game.magic.append(9)
            elif self.game.magic_motor.position == 4:
                self.game.magic.append(25)
            elif self.game.magic_motor.position == 5:
                self.game.magic.append(7)
                self.game.magic.append(8)
        else:
            if self.game.magic_motor.position == 1:
                self.game.magic.append(22)
            elif self.game.magic_motor.position == 2:
                self.game.magic.append(1)
            elif self.game.magic_motor.position == 3:
                self.game.magic.append(9)
            elif self.game.magic_motor.position == 4:
                self.game.magic.append(25)
            elif self.game.magic_motor.position == 5:
                self.game.magic.append(7)
        self.delay(name="display", delay=0.1, handler=graphics.dixieland.display, param=self)

    def pick_dd(self):
        dpos = self.game.dd_motor.spin()
        if dpos == 1:
            self.game.dd1.engage(self.game)
        elif dpos == 2:
            self.game.dd2.engage(self.game)
        elif dpos == 3:
            self.game.dd3.engage(self.game)
        dpos = self.game.dd_motor.spin()
        if dpos == 1:
            self.game.dd4.engage(self.game)
        elif dpos == 2:
            self.game.dd5.engage(self.game)
        elif dpos == 3:
            self.game.dd6.engage(self.game)
        self.delay(name="display", delay=0.1, handler=graphics.dixieland.display, param=self)

    # This is really nasty, but it is how we render graphics for each individual hole.
    # numbers are added (or removed from) a list.  In this way, I can re-use the same
    # routine even for games where there are ball return functions like Surf Club.

    def sw_hole1_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(1)
            if 1 in self.game.magic:
                if self.game.selector.position >= 9:
                    self.game.onetwothree.engage(self.game)
                if self.game.selector.position >= 10:
                    self.game.fourfivesix.engage(self.game)
            self.delay(name="display", delay=0.1, handler=graphics.dixieland.display, param=self)

    def sw_hole2_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(2)
            self.delay(name="display", delay=0.1, handler=graphics.dixieland.display, param=self)

    def sw_hole3_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(3)
            self.delay(name="display", delay=0.1, handler=graphics.dixieland.display, param=self)

    def sw_hole4_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(4)
            self.delay(name="display", delay=0.1, handler=graphics.dixieland.display, param=self)

    def sw_hole5_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(5)
            self.delay(name="display", delay=0.1, handler=graphics.dixieland.display, param=self)

    def sw_hole6_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(6)
            self.delay(name="display", delay=0.1, handler=graphics.dixieland.display, param=self)

    def sw_hole7_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(7)
            if 7 in self.game.magic:
                if self.game.selector.position >= 9:
                    self.game.onetwothree.engage(self.game)
                if self.game.selector.position >= 10:
                    self.game.fourfivesix.engage(self.game)
            self.delay(name="display", delay=0.1, handler=graphics.dixieland.display, param=self)

    def sw_hole8_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(8)
            if 8 in self.game.magic:
                if self.game.selector.position >= 9:
                    self.game.onetwothree.engage(self.game)
                if self.game.selector.position >= 10:
                    self.game.fourfivesix.engage(self.game)
            self.delay(name="display", delay=0.1, handler=graphics.dixieland.display, param=self)

    def sw_hole9_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(9)
            if 9 in self.game.magic:
                if self.game.selector.position >= 9:
                    self.game.onetwothree.engage(self.game)
                if self.game.selector.position >= 10:
                    self.game.fourfivesix.engage(self.game)
            self.delay(name="display", delay=0.1, handler=graphics.dixieland.display, param=self)

    def sw_hole10_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(10)
            self.delay(name="display", delay=0.1, handler=graphics.dixieland.display, param=self)

    def sw_hole11_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(11)
            self.delay(name="display", delay=0.1, handler=graphics.dixieland.display, param=self)

    def sw_hole12_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(12)
            self.delay(name="display", delay=0.1, handler=graphics.dixieland.display, param=self)

    def sw_hole13_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(13)
            self.delay(name="display", delay=0.1, handler=graphics.dixieland.display, param=self)

    def sw_hole14_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(14)
            self.delay(name="display", delay=0.1, handler=graphics.dixieland.display, param=self)

    def sw_hole15_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(15)
            self.delay(name="display", delay=0.1, handler=graphics.dixieland.display, param=self)

    def sw_hole16_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(16)
            self.delay(name="display", delay=0.1, handler=graphics.dixieland.display, param=self)

    def sw_hole17_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(17)
            self.delay(name="display", delay=0.1, handler=graphics.dixieland.display, param=self)

    def sw_hole18_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(18)
            self.delay(name="display", delay=0.1, handler=graphics.dixieland.display, param=self)

    def sw_hole19_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(19)
            self.delay(name="display", delay=0.1, handler=graphics.dixieland.display, param=self)

    def sw_hole20_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(20)
            self.delay(name="display", delay=0.1, handler=graphics.dixieland.display, param=self)

    def sw_hole21_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(21)
            self.delay(name="display", delay=0.1, handler=graphics.dixieland.display, param=self)

    def sw_hole22_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(22)
            if 22 in self.game.magic:
                if self.game.selector.position >= 9:
                    self.game.onetwothree.engage(self.game)
                if self.game.selector.position >= 10:
                    self.game.fourfivesix.engage(self.game)
            self.delay(name="display", delay=0.1, handler=graphics.dixieland.display, param=self)

    def sw_hole23_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(23)
            self.delay(name="display", delay=0.1, handler=graphics.dixieland.display, param=self)

    def sw_hole24_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(24)
            self.delay(name="display", delay=0.1, handler=graphics.dixieland.display, param=self)

    def sw_hole25_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(25)
            if 25 in self.game.magic:
                if self.game.selector.position >= 9:
                    self.game.onetwothree.engage(self.game)
                if self.game.selector.position >= 10:
                    self.game.fourfivesix.engage(self.game)
            self.delay(name="display", delay=0.1, handler=graphics.dixieland.display, param=self)

    def sw_redstar_active(self, sw):
        if self.game.corners_rollover.status == True:
            self.game.corners1.engage(self.game)
            self.game.corners2.engage(self.game)
            self.game.corners3.engage(self.game)
            self.game.corners4.engage(self.game)
            self.game.corners5.engage(self.game)
            self.game.corners6.engage(self.game)
            self.game.coils.yellowROLamp.disable()
            self.delay(name="display", delay=0.1, handler=graphics.dixieland.display, param=self)

    def sw_yellowstar_active(self, sw):
        if self.game.corners_rollover.status == True:
            self.game.super1.engage(self.game)
            self.game.super2.engage(self.game)
            self.game.super3.engage(self.game)
            self.game.super4.engage(self.game)
            self.game.super5.engage(self.game)
            self.game.super6.engage(self.game)
            self.game.coils.redROLamp.disable()
            self.delay(name="display", delay=0.1, handler=graphics.dixieland.display, param=self)

    def sw_replayReset_active(self, sw):
        self.game.anti_cheat.disengage()
        self.holes = []
##        self.cancel_delayed(name="blink_title")
        graphics.dixieland.display(self, 0)
        self.tilt_actions()
#        self.delay(name="blink_title", delay=1, handler=self.blink_title)
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
        self.game.search_index.disengage()
        if self.game.ball_count.position == 0:
            if self.game.switches.shutter.is_active():
                self.game.coils.shutter.enable()
        self.holes = []
        self.game.selector.reset()
        self.game.ball_count.reset()
        self.game.anti_cheat.engage(game)
        self.game.tilt.engage(self.game)
        self.game.sound.stop_music()
        self.game.sound.play('tilt')
        self.game.coils.redROLamp.disable()
        self.game.coils.yellowROLamp.disable()
        # displays "Tilt" on the backglass, you have to recoin.
        self.delay(name="display", delay=0.1, handler=graphics.dixieland.display, param=self)
        #self.game.modes.remove(Timeout)

    def sw_tilt_active(self, sw):
        if self.game.tilt.status == False:
            self.tilt_actions()

    def replay_step_down(self, number=0):
        if number > 0:
            if number > 1:
                self.game.replays -= 1
                graphics.replay_step_down(self.game.replays, graphics.dixieland.reel1, graphics.dixieland.reel10, graphics.dixieland.reel100, graphics.dixieland.reel1000)
                self.game.coils.registerDown.pulse()
                number -= 1
                graphics.dixieland.display(self)
                self.delay(name="replay_reset", delay=0.0, handler=self.replay_step_down, param=number)
            elif number == 1:
                self.game.replays -= 1
                graphics.replay_step_down(self.game.replays, graphics.dixieland.reel1, graphics.dixieland.reel10, graphics.dixieland.reel100, graphics.dixieland.reel1000)
                self.game.coils.registerDown.pulse()
                number -= 1
                graphics.dixieland.display(self)
                self.cancel_delayed(name="replay_reset")
        else: 
            if self.game.replays > 0:
                self.game.replays -= 1
                graphics.replay_step_down(self.game.replays, graphics.dixieland.reel1, graphics.dixieland.reel10, graphics.dixieland.reel100, graphics.dixieland.reel1000)
                self.delay(name="display", delay=0.1, handler=graphics.dixieland.display, param=self)
            self.game.coils.registerDown.pulse()

    def replay_step_up(self):
        if self.game.replays < 8999:
            self.game.replays += 1
            graphics.replay_step_up(self.game.replays, graphics.dixieland.reel1, graphics.dixieland.reel10, graphics.dixieland.reel100, graphics.dixieland.reel1000)
        self.game.reflex.increase()
        self.game.coils.registerUp.pulse()
        graphics.dixieland.display(self)
 
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
#        self.cancel_delayed(name="blink_title")
        self.game.sound.stop_music()

        self.cancel_delayed(name="research")
        for i in range(0, 150):
            if i <= 50:
                self.r = self.closed_search_relays(self.game.searchdisc.position, self.game.corners1.status, self.game.corners2.status, self.game.super1.status, self.game.super2.status)
                self.game.searchdisc.spin()
            if i >= 51 and i <= 100:
                self.r = self.closed_search_relays(self.game.searchdisc2.position + 50, self.game.corners3.status, self.game.corners4.status, self.game.super3.status, self.game.super4.status)
                self.game.searchdisc2.spin()
            if i >= 101:
                self.r = self.closed_search_relays(self.game.searchdisc3.position + 100, self.game.corners5.status, self.game.corners6.status, self.game.super5.status, self.game.super6.status)
                self.game.searchdisc3.spin()
            self.wipers = self.r[0]
            self.card = self.r[1]
            self.corners = self.r[2]
            self.super_line = self.r[3]
            self.red_diagonal = self.r[4]

            # From here, I need to determine based on the value of r, whether to latch the search index and score. For Bright Lights,
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
                            if self.card == 1:
                                g = self.game.card1_missed.status
                            elif self.card == 2:
                                g = self.game.card2_missed.status
                            elif self.card == 3:
                                g = self.game.card3_missed.status
                            elif self.card == 4:
                                g = self.game.card4_missed.status
                            elif self.card == 5:
                                g = self.game.card5_missed.status
                            elif self.card == 6:
                                g = self.game.card6_missed.status
                            if g == False:
                                if s >= 3:
                                    self.find_winner(s, self.card, self.corners, self.super_line, self.red_diagonal)
#        self.delay(name="blink_title", delay=3, handler=self.blink_title)

    def find_winner(self, relays, card, corners, super_line, red_diagonal):
        if self.game.search_index.status == False and self.game.replays < 8999:
            if self.game.card1_missed.status == False:
                if card == 1:
                    if relays == 3:
                        if corners == True:
                            pass
                        elif red_diagonal == True and self.game.selector.position < 7:
                            pass
                        else:
                            if super_line == True and self.game.super1.status == True:
                                    if self.game.card1_replay_counter.position < 16:
                                        self.game.search_index.engage(self.game)
                                        self.game.sound.stop('search')
                                        self.wait_for_input((1, 16))
                            else:
                                if self.game.card1_replay_counter.position < 4:
                                    self.game.search_index.engage(self.game)
                                    self.game.sound.stop('search')
                                    self.wait_for_input((1, 4))
                    if relays == 4:
                        if corners == True:
                            if self.game.corners1.status == True:
                                if self.game.card1_replay_counter.position < 100:
                                    self.game.search_index.engage(self.game)
                                    self.game.sound.stop('search')
                                    self.wait_for_input((1, 100))
                        elif red_diagonal == True and self.game.selector.position < 7:
                            pass
                        else:
                            if self.game.super1.status == True and super_line == True:
                                    if self.game.card1_replay_counter.position < 100:
                                        self.game.search_index.engage(self.game)
                                        self.game.sound.stop('search')
                                        self.wait_for_input((1, 100))
                            else:
                                if self.game.card1_replay_counter.position < 16:
                                    self.game.search_index.engage(self.game)
                                    self.game.sound.stop('search')
                                    self.wait_for_input((1, 16))
                    if relays == 5:
                        if self.game.card1_replay_counter.position < 100:
                            self.game.search_index.engage(self.game)
                            self.game.sound.stop('search')
                            self.wait_for_input((1, 100))
            if self.game.card2_missed.status == False:
                if card == 2:
                    if relays == 3:
                        if corners == True:
                            pass
                        elif red_diagonal == True and self.game.selector.position < 7:
                            pass
                        else:
                            if super_line == True and self.game.super2.status == True:
                                    if self.game.card2_replay_counter.position < 20:
                                        self.game.search_index.engage(self.game)
                                        self.game.sound.stop('search')
                                        self.wait_for_input((2, 20))
                            else:
                                if self.game.card2_replay_counter.position < 4:
                                    self.game.search_index.engage(self.game)
                                    self.game.sound.stop('search')
                                    self.wait_for_input((2, 4))
                    if relays == 4:
                        if corners == True:
                            if self.corners2.status == True:
                                if self.game.card2_replay_counter.position < 100:
                                    self.game.search_index.engage(self.game)
                                    self.game.sound.stop('search')
                                    self.wait_for_input((2, 100))
                        elif red_diagonal == True and self.game.selector.position < 7:
                            pass
                        else:
                            if super_line == True and self.game.super2.status == True:
                                    if self.game.card2_replay_counter.position < 100:
                                        self.game.search_index.engage(self.game)
                                        self.game.sound.stop('search')
                                        self.wait_for_input((2, 100))
                            else:
                                if self.game.card2_replay_counter.position < 20:
                                    self.game.search_index.engage(self.game)
                                    self.game.sound.stop('search')
                                    self.wait_for_input((2, 20))
                    if relays == 5:
                        if self.game.card2_replay_counter.position < 100:
                            self.game.search_index.engage(self.game)
                            self.game.sound.stop('search')
                            self.wait_for_input((2, 100))
            if self.game.card3_missed.status == False:
                if card == 3:
                    if relays == 3:
                        if corners == True:
                            pass
                        elif red_diagonal == True and self.game.selector.position < 7:
                            pass
                        else:
                            if super_line == True and self.game.super3.status == True:
                                    if self.game.card3_replay_counter.position < 20:
                                        self.game.search_index.engage(self.game)
                                        self.game.sound.stop('search')
                                        self.wait_for_input((3, 20))
                            else:
                                if self.game.card3_replay_counter.position < 4:
                                    self.game.search_index.engage(self.game)
                                    self.game.sound.stop('search')
                                    self.wait_for_input((3, 4))
                    if relays == 4:
                        if corners == True:
                            if self.game.corners3.status == True:
                                if self.game.card3_replay_counter.position < 120:
                                    self.game.search_index.engage(self.game)
                                    self.game.sound.stop('search')
                                    self.wait_for_input((3, 120))
                        elif red_diagonal == True and self.game.selector.position < 7:
                            pass
                        else:
                            if super_line == True and self.game.super3.status == True:
                                    if self.game.card3_replay_counter.position < 120:
                                        self.game.search_index.engage(self.game)
                                        self.game.sound.stop('search')
                                        self.wait_for_input((3, 120))
                            else:
                                if self.game.card3_replay_counter.position < 20:
                                    self.game.search_index.engage(self.game)
                                    self.game.sound.stop('search')
                                    self.wait_for_input((3, 20))
                    if relays == 5:
                        if self.game.card3_replay_counter.position < 120:
                            self.game.search_index.engage(self.game)
                            self.game.sound.stop('search')
                            self.wait_for_input((3, 120))
            if self.game.card4_missed.status == False:
                if card == 4:
                    if relays == 3:
                        if corners == True:
                            pass
                        elif red_diagonal == True and self.game.selector.position < 8:
                            pass
                        else:
                            if super_line == True and self.game.super4.status == True:
                                    if self.game.card4_replay_counter.position < 24:
                                        self.game.search_index.engage(self.game)
                                        self.game.sound.stop('search')
                                        self.wait_for_input((4, 24))
                            else:
                                if self.game.card4_replay_counter.position < 4:
                                    self.game.search_index.engage(self.game)
                                    self.game.sound.stop('search')
                                    self.wait_for_input((4, 4))
                    if relays == 4:
                        if corners == True:
                            if self.game.corners4.status == True:
                                if self.game.card4_replay_counter.position < 140:
                                    self.game.search_index.engage(self.game)
                                    self.game.sound.stop('search')
                                    self.wait_for_input((4, 140))
                        elif red_diagonal == True and self.game.selector.position < 8:
                            pass
                        else:
                            if super_line == True and self.game.super4.status == True:
                                    if self.game.card4_replay_counter.position < 140:
                                        self.game.search_index.engage(self.game)
                                        self.game.sound.stop('search')
                                        self.wait_for_input((4, 140))
                            else:
                                if self.game.card4_replay_counter.position < 24:
                                    self.game.search_index.engage(self.game)
                                    self.game.sound.stop('search')
                                    self.wait_for_input((4, 24))
                    if relays == 5:
                        if self.game.card4_replay_counter.position < 140:
                            self.game.search_index.engage(self.game)
                            self.game.sound.stop('search')
                            self.wait_for_input((4, 140))
            if self.game.card5_missed.status == False:
                if card == 5:
                    if relays == 3:
                        if corners == True:
                            pass
                        elif red_diagonal == True and self.game.selector.position < 8:
                            pass
                        else:
                            if super_line == True and self.game.super5.status == True:
                                    if self.game.card5_replay_counter.position < 36:
                                        self.game.search_index.engage(self.game)
                                        self.game.sound.stop('search')
                                        self.wait_for_input((5, 36))
                            else:
                                if self.game.card5_replay_counter.position < 4:
                                    self.game.search_index.engage(self.game)
                                    self.game.sound.stop('search')
                                    self.wait_for_input((5, 4))
                    if relays == 4:
                        if corners == True:
                            if self.game.corners5.status == True:
                                if self.game.card5_replay_counter.position < 240:
                                    self.game.search_index.engage(self.game)
                                    self.game.sound.stop('search')
                                    self.wait_for_input((5, 240))
                        elif red_diagonal == True and self.game.selector.position < 8:
                            pass
                        else:
                            if super_line == True and self.game.super5.status == True:
                                    if self.game.card5_replay_counter.position < 240:
                                        self.game.search_index.engage(self.game)
                                        self.game.sound.stop('search')
                                        self.wait_for_input((5, 240))
                            else:
                                if self.game.card5_replay_counter.position < 36:
                                    self.game.search_index.engage(self.game)
                                    self.game.sound.stop('search')
                                    self.wait_for_input((5, 36))
                    if relays == 5:
                        if self.game.card5_replay_counter.position < 240:
                            self.game.search_index.engage(self.game)
                            self.game.sound.stop('search')
                            self.wait_for_input((5, 240))
            if self.game.card6_missed.status == False:
                if card == 6:
                    if relays == 3:
                        if corners == True:
                            pass
                        elif red_diagonal == True and self.game.selector.position < 8:
                            pass
                        else:
                            if super_line == True and self.game.super6.status == True:
                                    if self.game.card6_replay_counter.position < 44:
                                        self.game.search_index.engage(self.game)
                                        self.game.sound.stop('search')
                                        self.wait_for_input((6, 44))
                            else:
                                if self.game.card6_replay_counter.position < 4:
                                    self.game.search_index.engage(self.game)
                                    self.game.sound.stop('search')
                                    self.wait_for_input((6, 4))
                    if relays == 4:
                        if corners == True:
                            if self.game.corners6.status == True:
                                if self.game.card6_replay_counter.position < 300:
                                    self.game.search_index.engage(self.game)
                                    self.game.sound.stop('search')
                                    self.wait_for_input((6, 300))
                        elif red_diagonal == True and self.game.selector.position < 8:
                            pass
                        else:
                            if super_line == True and self.game.super6.status == True:
                                    if self.game.card6_replay_counter.position < 300:
                                        self.game.search_index.engage(self.game)
                                        self.game.sound.stop('search')
                                        self.wait_for_input((6, 300))
                            else:
                                if self.game.card6_replay_counter.position < 44:
                                    self.game.search_index.engage(self.game)
                                    self.game.sound.stop('search')
                                    self.wait_for_input((6, 44))
                    if relays == 5:
                        if self.game.card6_replay_counter.position < 300:
                            self.game.search_index.engage(self.game)
                            self.game.sound.stop('search')
                            self.wait_for_input((6, 300))

    def wait_for_input(self, i):
        if (i[0] == 1 or i[0] == 2 or i[0] == 3) and self.game.onetwothree.status == True:
            rc = i[1] * 2
        elif (i[0] == 4 or i[0] == 5 or i[0] == 6) and self.game.fourfivesix.status == True:
            rc = i[1] * 2
        else:
            rc = i[1]

        if i[0] == 1:
            if self.game.dd1.status == True and self.game.onetwothree.status == True:
                rc = rc * 2
        if i[0] == 2:
            if self.game.dd2.status == True and self.game.onetwothree.status == True:
                rc = rc * 2
        if i[0] == 3:
            if self.game.dd3.status == True and self.game.onetwothree.status == True:
                rc = rc * 2
        if i[0] == 4:
            if self.game.dd4.status == True and self.game.fourfivesix.status == True:
                rc = rc * 2
        if i[0] == 5:
            if self.game.dd5.status == True and self.game.fourfivesix.status == True:
                rc = rc * 2
        if i[0] == 6:
            if self.game.dd6.status == True and self.game.fourfivesix.status == True:
                rc = rc * 2
   
        if self.game.switches.left.is_inactive() and self.game.switches.right.is_inactive():
            if i[0] == 1 and self.game.card1_replay_counter.position > 0:
                if self.game.card1_double.status == True:
                    self.cancel_delayed(name="blink_double")
                    self.delay(name="display", delay=0.1, handler=graphics.dixieland.display, param=self)
                    self.game.blink = 0
                    self.card1_replay_step_up((rc * 2) - self.game.card1_replay_counter.position)
                else:
                    self.cancel_delayed(name="blink_double")
                    self.delay(name="display", delay=0.1, handler=graphics.dixieland.display, param=self)
                    self.game.blink = 0
                    self.card1_replay_step_up(rc - self.game.card1_replay_counter.position)
            elif i[0] == 2 and self.game.card2_replay_counter.position > 0:
                if self.game.card2_double.status == True:
                    self.cancel_delayed(name="blink_double")
                    self.delay(name="display", delay=0.1, handler=graphics.dixieland.display, param=self)
                    self.game.blink = 0
                    self.card2_replay_step_up((rc * 2) - self.game.card2_replay_counter.position)
                else:
                    self.cancel_delayed(name="blink_double")
                    self.delay(name="display", delay=0.1, handler=graphics.dixieland.display, param=self)
                    self.game.blink = 0
                    self.card2_replay_step_up(rc - self.game.card2_replay_counter.position)
            elif i[0] == 3 and self.game.card3_replay_counter.position > 0:
                if self.game.card3_double.status == True:
                    self.cancel_delayed(name="blink_double")
                    self.delay(name="display", delay=0.1, handler=graphics.dixieland.display, param=self)
                    self.game.blink = 0
                    self.card3_replay_step_up((rc * 2) - self.game.card3_replay_counter.position)
                else:
                    self.cancel_delayed(name="blink_double")
                    self.delay(name="display", delay=0.1, handler=graphics.dixieland.display, param=self)
                    self.game.blink = 0
                    self.card3_replay_step_up(rc - self.game.card3_replay_counter.position)
            elif i[0] == 4 and self.game.card4_replay_counter.position > 0:
                if self.game.card4_double.status == True:
                    self.cancel_delayed(name="blink_double")
                    self.delay(name="display", delay=0.1, handler=graphics.dixieland.display, param=self)
                    self.game.blink = 0
                    self.card4_replay_step_up((rc * 2) - self.game.card4_replay_counter.position)
                else:
                    self.cancel_delayed(name="blink_double")
                    self.delay(name="display", delay=0.1, handler=graphics.dixieland.display, param=self)
                    self.game.blink = 0
                    self.card4_replay_step_up(rc - self.game.card4_replay_counter.position)
            elif i[0] == 5 and self.game.card5_replay_counter.position > 0:
                if self.game.card5_double.status == True:
                    self.cancel_delayed(name="blink_double")
                    self.delay(name="display", delay=0.1, handler=graphics.dixieland.display, param=self)
                    self.game.blink = 0
                    self.card5_replay_step_up((rc * 2) - self.game.card5_replay_counter.position)
                else:
                    self.cancel_delayed(name="blink_double")
                    self.delay(name="display", delay=0.1, handler=graphics.dixieland.display, param=self)
                    self.game.blink = 0
                    self.card5_replay_step_up(rc - self.game.card5_replay_counter.position)
            elif i[0] == 6 and self.game.card6_replay_counter.position > 0:
                if self.game.card6_double.status == True:
                    self.cancel_delayed(name="blink_double")
                    self.delay(name="display", delay=0.1, handler=graphics.dixieland.display, param=self)
                    self.game.blink = 0
                    self.card6_replay_step_up((rc * 2) - self.game.card6_replay_counter.position)
                else:
                    self.cancel_delayed(name="blink_double")
                    self.delay(name="display", delay=0.1, handler=graphics.dixieland.display, param=self)
                    self.game.blink = 0
                    self.card6_replay_step_up(rc - self.game.card6_replay_counter.position)
            else:
                if i[0] == 1 and self.game.card1_missed.status == True:
                    self.delay(name="display", delay=0.1, handler=graphics.dixieland.display, param=self)
                elif i[0] == 2 and self.game.card2_missed.status == True:
                    self.delay(name="display", delay=0.1, handler=graphics.dixieland.display, param=self)
                elif i[0] == 3 and self.game.card3_missed.status == True:
                    self.delay(name="display", delay=0.1, handler=graphics.dixieland.display, param=self)
                elif i[0] == 4 and self.game.card4_missed.status == True:
                    self.delay(name="display", delay=0.1, handler=graphics.dixieland.display, param=self)
                elif i[0] == 5 and self.game.card5_missed.status == True:
                    self.delay(name="display", delay=0.1, handler=graphics.dixieland.display, param=self)
                elif i[0] == 6 and self.game.card6_missed.status == True:
                    self.delay(name="display", delay=0.1, handler=graphics.dixieland.display, param=self)
                else:
                    graphics.dixieland.blink_double(self)
                    self.delay(name="blink_double", delay=0.2, handler=self.wait_for_input, param=i)
        if self.game.switches.left.is_active():
            self.cancel_delayed(name="blink_double")
            self.delay(name="display", delay=0.1, handler=graphics.dixieland.display, param=self)
            self.game.blink = 0
            if i[0] == 1:
                self.card1_replay_step_up(rc - self.game.card1_replay_counter.position)
                self.game.card1_regular.engage(self.game)
            elif i[0] == 2:
                self.card2_replay_step_up(rc - self.game.card2_replay_counter.position)
                self.game.card2_regular.engage(self.game)
            elif i[0] == 3:
                self.card3_replay_step_up(rc - self.game.card3_replay_counter.position)
                self.game.card3_regular.engage(self.game)
            elif i[0] == 4:
                self.card4_replay_step_up(rc - self.game.card4_replay_counter.position)
                self.game.card4_regular.engage(self.game)
            elif i[0] == 5:
                self.card5_replay_step_up(rc - self.game.card5_replay_counter.position)
                self.game.card5_regular.engage(self.game)
            elif i[0] == 6:
                self.card6_replay_step_up(rc - self.game.card6_replay_counter.position)
                self.game.card6_regular.engage(self.game)
            self.delay(name="display", delay=0.1, handler=graphics.dixieland.display, param=self)
        if self.game.switches.right.is_active():
            self.cancel_delayed(name="blink_double")
            dp = self.check_double_probability()
            if dp == True:
                if i[0] == 1:
                    self.game.card1_double.engage(self.game)
                    self.card1_replay_step_up((rc * 2) - self.game.card1_replay_counter.position)
                elif i[0] == 2:
                    self.game.card2_double.engage(self.game)
                    self.card2_replay_step_up((rc * 2) - self.game.card2_replay_counter.position)
                elif i[0] == 3:
                    self.game.card3_double.engage(self.game)
                    self.card3_replay_step_up((rc * 2) - self.game.card3_replay_counter.position)
                elif i[0] == 4:
                    self.game.card4_double.engage(self.game)
                    self.card4_replay_step_up((rc * 2) - self.game.card4_replay_counter.position)
                elif i[0] == 5:
                    self.game.card5_double.engage(self.game)
                    self.card5_replay_step_up((rc * 2) - self.game.card5_replay_counter.position)
                elif i[0] == 6:
                    self.game.card6_double.engage(self.game)
                    self.card6_replay_step_up((rc * 2) - self.game.card6_replay_counter.position)
                self.delay(name="display", delay=0.1, handler=graphics.dixieland.display, param=self)
            else:
                if i[0] == 1:
                    self.game.card1_missed.engage(self.game)
                    self.game.search_index.disengage()
                    self.cancel_delayed(name="blink_double")
                    self.delay(name="display", delay=0.1, handler=graphics.dixieland.display, param=self)
                    self.delay(name="research", delay=1, handler=self.search)
                elif i[0] == 2:
                    self.game.card2_missed.engage(self.game)
                    self.game.search_index.disengage()
                    self.cancel_delayed(name="blink_double")
                    self.delay(name="display", delay=0.1, handler=graphics.dixieland.display, param=self)
                    self.delay(name="research", delay=1, handler=self.search)
                elif i[0] == 3:
                    self.game.card3_missed.engage(self.game)
                    self.game.search_index.disengage()
                    self.cancel_delayed(name="blink_double")
                    self.delay(name="display", delay=0.1, handler=graphics.dixieland.display, param=self)
                    self.delay(name="research", delay=1, handler=self.search)
                elif i[0] == 4:
                    self.game.card4_missed.engage(self.game)
                    self.game.search_index.disengage()
                    self.cancel_delayed(name="blink_double")
                    self.delay(name="display", delay=0.1, handler=graphics.dixieland.display, param=self)
                    self.delay(name="research", delay=1, handler=self.search)
                elif i[0] == 5:
                    self.game.card5_missed.engage(self.game)
                    self.game.search_index.disengage()
                    self.cancel_delayed(name="blink_double")
                    self.delay(name="display", delay=0.1, handler=graphics.dixieland.display, param=self)
                    self.delay(name="research", delay=1, handler=self.search)
                elif i[0] == 6:
                    self.game.card6_missed.engage(self.game)
                    self.game.search_index.disengage()
                    self.cancel_delayed(name="blink_double")
                    self.delay(name="display", delay=0.1, handler=graphics.dixieland.display, param=self)
                    self.delay(name="research", delay=1, handler=self.search)

    def check_double_probability(self):
        pos = self.game.probability.spin()
        if pos == 1 or pos == 4 or pos == 5 or pos == 6 or pos == 8 or pos == 10 or pos == 11 or pos == 15 or pos == 16 or pos == 17 or pos == 19 or pos == 21 or pos == 22 or pos == 24 or pos == 25 or pos == 27 or pos == 29 or pos == 30 or pos == 33 or pos == 34 or pos == 39 or pos == 40 or pos == 44 or pos == 46 or pos == 48:
            return 1
        elif self.game.probability.position == 3 or self.game.probability == 10:
            return 1
        else:
            return 0

    def check_corners(self):
        pos = self.game.probability.position
        if self.game.cu:
            if self.game.selector.position <= 4:
                if pos == 4 or pos == 6 or pos == 7 or pos == 9 or pos == 10 or pos == 13:
                    return 1
            else:
                if pos == 1 or pos == 2 or pos == 18 or pos == 19 or pos == 22:
                    return 1
            return 0
        else:
            if self.game.selector.position <= 4:
                if pos == 6 or pos == 9 or pos == 10:
                    return 1
            else:
                if pos == 1 or pos == 2 or pos == 19:
                    return 1
            return 0
            
    def check_super(self):
        pos = self.game.probability.position
        if self.game.cu:
            if self.game.selector.position <= 4:
                if pos == 4 or pos == 5 or pos == 8 or pos == 12 or pos == 13 or pos == 15:
                    return 1
            else:
                if pos == 20 or pos == 21 or pos == 24:
                    return 1
            return 0
        else:
            if self.game.selector.position <= 4:
                if pos == 5 or pos == 8 or pos == 12:
                    return 1
            else:
                if pos == 20 or pos == 24:
                    return 1
            return 0

    def check_trip(self):
        pos = self.game.probability.position
        if pos == 1 or pos == 3 or pos == 7 or pos == 10 or pos == 15 or pos == 17 or pos == 20 or pos == 22 or pos == 24:
            return 1
        else:
            return 0

    def card1_replay_step_up(self, number):
        if number >= 1:
            self.game.card1_replay_counter.step()
            number -= 1
            self.replay_step_up()
            self.delay(name="card1_replay_step_up", delay=0.1, handler=self.card1_replay_step_up, param=number)
        else:
            self.game.search_index.disengage()
            self.cancel_delayed(name="card1_replay_step_up")
            self.search()

    def card2_replay_step_up(self, number):
        if number >= 1:
            self.game.card2_replay_counter.step()
            number -= 1
            self.replay_step_up()
            if self.game.replays == 8999:
                number = 0
            self.delay(name="card2_replay_step_up", delay=0.1, handler=self.card2_replay_step_up, param=number)
        else:
            self.game.search_index.disengage()
            self.cancel_delayed(name="card2_replay_step_up")
            self.search()

    def card3_replay_step_up(self, number):
        if number >= 1:
            self.game.card3_replay_counter.step()
            number -= 1
            self.replay_step_up()
            if self.game.replays == 8999:
                number = 0
            self.delay(name="card3_replay_step_up", delay=0.1, handler=self.card3_replay_step_up, param=number)
        else:
            self.game.search_index.disengage()
            self.cancel_delayed(name="card3_replay_step_up")
            self.search()

    def card4_replay_step_up(self, number):
        if number >= 1:
            self.game.card4_replay_counter.step()
            number -= 1
            self.replay_step_up()
            if self.game.replays == 8999:
                number = 0
            self.delay(name="card4_replay_step_up", delay=0.1, handler=self.card4_replay_step_up, param=number)
        else:
            self.game.search_index.disengage()
            self.cancel_delayed(name="card4_replay_step_up")
            self.search()

    def card5_replay_step_up(self, number):
        if number >= 1:
            self.game.card5_replay_counter.step()
            number -= 1
            self.replay_step_up()
            if self.game.replays == 8999:
                number = 0
            self.delay(name="card5_replay_step_up", delay=0.1, handler=self.card5_replay_step_up, param=number)
        else:
            self.game.search_index.disengage()
            self.cancel_delayed(name="card5_replay_step_up")
            self.search()

    def card6_replay_step_up(self, number):
        if number >= 1:
            self.game.card6_replay_counter.step()
            number -= 1
            self.replay_step_up()
            if self.game.replays == 8999:
                number = 0
            self.delay(name="card6_replay_step_up", delay=0.1, handler=self.card6_replay_step_up, param=number)
        else:
            self.game.search_index.disengage()
            self.cancel_delayed(name="card6_replay_step_up")
            self.search()

    def closed_search_relays(self, rivets, c1, c2, s1, s2):
        # This function is critical, as it will determine which card is returned, etc.  I need to check both the position of the
        # replay counter for the card, as well as the selector unit to ensure that the card is selected. We will get a row back
        # that has the numbers on the position which will return the search relay connected.  When three out of the five relays
        # are connected, we get a winner!
        
        # The orientation of the rivets shows that cards are scanned in reverse order on the search discs.  This is FUUUNNNKY.
        # I am taking the liberty of rearranging these to make logical sense.  Starting at position 8, the game in reality scans
        # for corners on card #3.  BUT because the machine physically searches from 50-0, I will rearrange to emulate properly.

        # I am also changing the way corners are scored.  Since search relay #3 is not used, I cannot emulate 100%.  My search
        # function _requires_ that the relays are sequential.  I'm not rewriting a well-working search function just to emulate
        # the relays correctly.  You know, since they don't exist in this game. :-)

        self.pos = {}
        # Card 1
        self.pos[0] = {5:1, 3:2, 12:3, 15:4}
        self.pos[1] = {9:1, 19:2, 17:3}
        self.pos[2] = {1:1, 10:2, 11:3, 13:4}
        self.pos[3] = {8:1, 18:2, 14:3, 4:4}
        self.pos[4] = {6:1, 21:2, 2:3}
        self.pos[5] = {2:1, 20:2, 17:3}
        self.pos[6] = {23:1, 14:2, 11:3, 7:4}
        self.pos[7] = {24:1, 18:2, 10:3, 25:4}
        self.pos[8] = {6:1, 22:2, 9:3}
        self.pos[9] = {3:1, 19:2, 16:3, 21:4, 12:5}
        self.pos[10] = {5:1, 22:2, 16:3, 20:4, 15:5}
        self.pos[11] = {3:1, 7:2, 17:3, 13:4, 15:5}
        self.pos[12] = {25:1, 19:2, 11:3, 20:4, 4:5}
        self.pos[13] = {9:1, 10:2, 16:3, 14:4, 2:5}
        self.pos[14] = {1:1, 22:2, 18:3, 21:4, 23:5}
        self.pos[15] = {5:1, 8:2, 6:3, 24:4, 12:5}
        self.pos[16] = {12:1, 23:2, 2:3, 4:4, 15:5}
        self.pos[17] = {24:1, 21:2, 14:3, 20:4, 13:5}
        self.pos[18] = {6:1, 18:2, 16:3, 11:4, 17:5}
        self.pos[19] = {8:1, 22:2, 10:3, 19:4, 7:5}
        self.pos[20] = {5:1, 1:2, 9:3, 25:4, 3:5}
        self.pos[21] = {}
        self.pos[22] = {}

        # Card 2
        self.pos[23] = {}
        self.pos[24] = {}
        self.pos[25] = {}
        self.pos[26] = {}
        self.pos[27] = {}
        self.pos[28] = {9:1, 6:2, 10:3, 3:4}
        self.pos[29] = {16:1, 20:2, 17:3}
        self.pos[30] = {24:1, 14:2, 12:3, 8:4}
        self.pos[31] = {13:1, 18:2, 11:3, 23:4}
        self.pos[32] = {2:1, 22:2, 5:3}
        self.pos[33] = {5:1, 21:2, 17:3}
        self.pos[34] = {7:1, 11:2, 12:3, 25:4}
        self.pos[35] = {1:1, 18:2, 14:3, 4:4}
        self.pos[36] = {2:1, 19:2, 16:3}
        self.pos[37] = {6:1, 20:2, 15:3, 22:4, 10:5}
        self.pos[38] = {9:1, 19:2, 15:3, 21:4, 3:5}
        self.pos[39] = {6:1, 25:2, 17:3, 8:4, 3:5}
        self.pos[40] = {4:1, 20:2, 12:3, 21:4, 23:5}
        self.pos[41] = {16:1, 14:2, 15:3, 11:4, 5:5}
        self.pos[42] = {24:1, 19:2, 18:3, 22:4, 7:5}
        self.pos[43] = {9:1, 13:2, 2:3, 1:4, 10:5}
        self.pos[44] = {10:1, 7:2, 5:3, 23:4, 3:5}
        self.pos[45] = {1:1, 22:2, 11:3, 21:4, 8:5}
        self.pos[46] = {2:1, 18:2, 15:3, 12:4, 17:5}
        self.pos[47] = {13:1, 19:2, 14:3, 20:4, 25:5}
        self.pos[48] = {9:1, 24:2, 16:3, 4:4, 6:5}
        self.pos[49] = {}

        # Start of the second search disc modeled as part
        # of the same array for simplicity. Parent function
        # calls this subset.
        # Card 3
        self.pos[50] = {}
        self.pos[51] = {6:1, 1:2, 10:3, 8:4}
        self.pos[52] = {3:1, 18:2, 22:3}
        self.pos[53] = {7:1, 12:2, 16:3, 25:4}
        self.pos[54] = {23:1, 19:2, 9:3, 4:4}
        self.pos[55] = {5:1, 17:2, 21:3}
        self.pos[56] = {21:1, 15:2, 22:3}
        self.pos[57] = {13:1, 9:2, 16:3, 2:4}
        self.pos[58] = {11:1, 19:2, 12:3, 24:4}
        self.pos[59] = {5:1, 14:2, 3:3}
        self.pos[60] = {1:1, 18:2, 20:3, 17:4, 10:5}
        self.pos[61] = {6:1, 14:2, 20:3, 15:4, 8:5}
        self.pos[62] = {1:1, 2:2, 22:3, 25:4, 8:5}
        self.pos[63] = {24:1, 18:2, 16:3, 15:4, 4:5}
        self.pos[64] = {3:1, 12:2, 20:3, 9:4, 21:5}
        self.pos[65] = {7:1, 14:2, 19:3, 17:4, 13:5}
        self.pos[66] = {6:1, 23:2, 5:3, 11:4, 10:5}
        self.pos[67] = {10:1, 13:2, 21:3, 4:4, 8:5}
        self.pos[68] = {11:1, 17:2, 9:3, 15:4, 25:5}
        self.pos[69] = {5:1, 19:2, 20:3, 16:4, 22:5}
        self.pos[70] = {23:1, 14:2, 12:3, 18:4, 2:5}
        self.pos[71] = {6:1, 7:2, 3:3, 24:4, 1:5}
        self.pos[72] = {}
        self.pos[73] = {}
 
        # Card 4
        self.pos[74] = {}
        self.pos[75] = {}
        self.pos[76] = {}
        self.pos[77] = {}
        self.pos[78] = {}
        self.pos[79] = {3:1, 9:2, 6:3, 5:4}
        self.pos[80] = {10:1, 22:2, 2:3}
        self.pos[81] = {7:1, 18:2, 11:3, 23:4}
        self.pos[82] = {24:1, 14:2, 12:3, 1:4}
        self.pos[83] = {15:1, 20:2, 16:3}
        self.pos[84] = {16:1, 19:2, 2:3}
        self.pos[85] = {25:1, 12:2, 11:3, 8:4}
        self.pos[86] = {13:1, 14:2, 18:3, 4:4}
        self.pos[87] = {15:1, 21:2, 10:3}
        self.pos[88] = {9:1, 22:2, 17:3, 20:4, 6:5}
        self.pos[89] = {3:1, 21:2, 17:3, 19:4, 5:5}
        self.pos[90] = {9:1, 8:2, 2:3, 23:4, 5:5}
        self.pos[91] = {4:1, 22:2, 11:3, 19:4, 1:5}
        self.pos[92] = {10:1, 18:2, 17:3, 12:4, 16:5}
        self.pos[93] = {7:1, 21:2, 14:3, 20:4, 25:5}
        self.pos[94] = {3:1, 24:2, 15:3, 13:4, 6:5}
        self.pos[95] = {6:1, 25:2, 16:3, 1:4, 5:5}
        self.pos[96] = {13:1, 20:2, 12:3, 19:4, 23:5}
        self.pos[97] = {15:1, 14:2, 17:3, 11:4, 2:5}
        self.pos[98] = {24:1, 21:2, 18:3, 22:4, 8:5}
        self.pos[99] = {3:1, 7:2, 10:3, 4:4, 9:5}

       
        
        # Card 5
        self.pos[100] = {4:1, 5:2, 7:3, 11:4}
        self.pos[101] = {1:1, 17:2, 20:3}
        self.pos[102] = {6:1, 3:2, 12:3, 8:4}
        self.pos[103] = {25:1, 19:2, 16:3, 2:4}
        self.pos[104] = {9:1, 18:2, 22:3}
        self.pos[105] = {22:1, 14:2, 20:3}
        self.pos[106] = {24:1, 16:2, 12:3, 13:4}
        self.pos[107] = {10:1, 19:2, 3:3, 23:4}
        self.pos[108] = {9:1, 15:2, 1:3}
        self.pos[109] = {5:1, 17:2, 21:3, 18:4, 7:5}
        self.pos[110] = {4:1, 15:2, 21:3, 14:4, 11:5}
        self.pos[111] = {5:1, 13:2, 20:3, 8:4, 11:5}
        self.pos[112] = {23:1, 17:2, 12:3, 14:4, 2:5}
        self.pos[113] = {1:1, 3:2, 21:3, 16:4, 22:5}
        self.pos[114] = {6:1, 15:2, 19:3, 18:4, 24:5}
        self.pos[115] = {4:1, 25:2, 9:3, 10:4, 7:5}
        self.pos[116] = {7:1, 24:2, 22:3, 2:4, 11:5}
        self.pos[117] = {10:1, 18:2, 16:3, 14:4, 8:5}
        self.pos[118] = {9:1, 19:2, 21:3, 12:4, 20:5}
        self.pos[119] = {25:1, 15:2, 3:3, 17:4, 13:5}
        self.pos[120] = {4:1, 6:2, 1:3, 23:4, 5:5}
        self.pos[121] = {}

        # Card 6
        self.pos[122] = {}
        self.pos[123] = {}
        self.pos[124] = {}
        self.pos[125] = {}
        self.pos[126] = {}
        self.pos[127] = {8:1, 4:2, 1:3, 6:4}
        self.pos[128] = {10:1, 14:2, 5:3}
        self.pos[129] = {23:1, 16:2, 19:3, 11:4}
        self.pos[130] = {2:1, 12:2, 9:3, 3:4}
        self.pos[131] = {20:1, 15:2, 21:3}
        self.pos[132] = {21:1, 18:2, 5:3}
        self.pos[133] = {7:1, 9:2, 19:3, 24:4}
        self.pos[134] = {25:1, 12:2, 16:3, 13:4}
        self.pos[135] = {20:1, 17:2, 10:3}
        self.pos[136] = {4:1, 14:2, 22:3, 15:4, 1:5}
        self.pos[137] = {8:1, 17:2, 22:3, 18:4, 6:5}
        self.pos[138] = {4:1, 24:2, 5:3, 11:4, 6:5}
        self.pos[139] = {13:1, 14:2, 19:3, 18:4, 3:5}
        self.pos[140] = {10:1, 16:2, 22:3, 9:4, 21:5}
        self.pos[141] = {23:1, 17:2, 12:3, 15:4, 7:5}
        self.pos[142] = {8:1, 2:2, 20:3, 25:4, 1:5}
        self.pos[143] = {1:1, 7:2, 21:3, 3:4, 6:5}
        self.pos[144] = {25:1, 15:2, 9:3, 18:4, 11:5}
        self.pos[145] = {20:1, 12:2, 22:3, 19:4, 5:5}
        self.pos[146] = {2:1, 17:2, 16:3, 14:4, 24:5}
        self.pos[147] = {8:1, 23:2, 10:3, 13:4, 4:5}
        self.pos[148] = {}
        self.pos[149] = {}
        self.pos[150] = {}
        
        corners = False
        super_line = False
        red_diagonal = False
        card = 0

        if rivets in range(0,23):
            card = 1
            if rivets == 0:
                corners = True
            if rivets == 17:
                super_line = True
            if rivets in range(1,8):
                red_diagonal = True

        if rivets in range(23,50):
            card = 2
            if rivets == 28:
                corners = True
            if rivets == 45:
                super_line = True
            if rivets in range(29,36):
                red_diagonal = True

        if rivets in range(50,74):
            card = 3
            if rivets == 51:
                corners = True
            if rivets == 68:
                super_line = True
            if rivets in range(52,59):
                red_diagonal = True

        if rivets in range(74,100):
            card = 4
            if rivets == 79:
                corners = True
            if rivets == 96:
                super_line = True
            if rivets in range(80,87):
                red_diagonal = True

        if rivets in range(100,122):
            card = 5
            if rivets == 100:
                corners = True
            if rivets == 117:
                super_line = True
            if rivets in range(101,108):
                red_diagonal = True

        if rivets in range(122,151):
            card = 6
            if rivets == 127:
                corners = True
            if rivets == 144:
                super_line = True
            if rivets in range(128,135):
                red_diagonal = True

        return (self.pos[rivets], card, corners, super_line, red_diagonal)
            
    def blink_title(self):
        title1 = random.randint(0,1)
        title2 = random.randint(0,1)
        title3 = random.randint(0,1)
        title4 = random.randint(0,1)
        if title1 == 1:
            pos = [61,251]
            image = pygame.image.load('dixieland/assets/title1_on.png').convert_alpha()
            screen.blit(image, pos)
        if title2 == 1:
            pos = [218,251]
            image = pygame.image.load('dixieland/assets/title2_on.png').convert_alpha()
            screen.blit(image, pos)
        if title3 == 1:
            pos = [406,252]
            image = pygame.image.load('dixieland/assets/title3_on.png').convert_alpha()
            screen.blit(image, pos)
        if title4 == 1:
            pos = [529,266]
            image = pygame.image.load('dixieland/assets/title4_on.png').convert_alpha()
            screen.blit(image, pos)

        pygame.display.update()
        self.delay(name="display", delay=0.1, handler=graphics.dixieland.display, param=self)
#        self.delay(name="blink_title", delay=3, handler=self.blink_title)
                               
    # Define reset as the knock-off, anti-cheat relay disabled, and replay reset enabled.  Motors turn while credits are knocked off.
    # When meter reaches zero and the zero limit switch is hit, turn off motor sound and leave backglass gi on, but with tilt displayed.

    def startup(self):        
        # Every bingo requires the meter to register '0' 
        # before allowing coin entry --
        # also needs to show a plain 'off' backglass.
        self.eb = False
        self.tilt_actions()
#        self.delay(name="blink_title", delay=1, handler=self.blink_title)

class Dixieland(procgame.game.BasicGame):
    """ Bright Lights was the first bingo produced by Bally """
    def __init__(self, machine_type):
        super(Dixieland, self).__init__(machine_type)
        pygame.mixer.pre_init(44100,-16,2,512)
        self.sound = procgame.sound.SoundController(self)
        self.sound.set_volume(1.0)
        # NOTE: trough_count only counts the number of switches present in the  trough.  It does _not_ count
        #       the number of balls present.   In this game, there  should  be  8  balls.
        self.trough_count = 6

        # Subclass my units unique to this game -  modifications must be made to set up mixers and steppers unique to the game
        # NOTE: 'top' positions are indexed using a 0 index, so the top on a 24 position unit is actually 23.

        self.searchdisc = units.Search("searchdisc", 49)
        self.searchdisc2 = units.Search("searchdisc2", 49)
        self.searchdisc3 = units.Search("searchdisc3", 49)

        #Seach relays
        self.s1 = units.Relay("s1")
        self.s2 = units.Relay("s2")
        self.s3 = units.Relay("s3")
        self.s4 = units.Relay("s4")
        self.s5 = units.Relay("s5")
        self.search_index = units.Relay("search_index")

        #Replay Counter
        self.card1_replay_counter = units.Stepper("card1_replay_counter", 600)
        self.card2_replay_counter = units.Stepper("card2_replay_counter", 600)
        self.card3_replay_counter = units.Stepper("card3_replay_counter", 600)
        self.card4_replay_counter = units.Stepper("card4_replay_counter", 600)
        self.card5_replay_counter = units.Stepper("card5_replay_counter", 600)
        self.card6_replay_counter = units.Stepper("card6_replay_counter", 600)
        
        #Initialize stepper units used to keep track of features or timing.
        self.selector = units.Stepper("selector", 11)
        self.timer = units.Stepper("timer", 40)
        self.ball_count = units.Stepper("ball_count", 5)

        #Have to keep track of which cards have corners scoring enabled.
        self.corners1 = units.Relay("corners1")
        self.corners2 = units.Relay("corners2")
        self.corners3 = units.Relay("corners3")
        self.corners4 = units.Relay("corners4")
        self.corners5 = units.Relay("corners5")
        self.corners6 = units.Relay("corners6")
        self.corners_rollover = units.Relay("corners_rollover")

        #Super lines tracking
        self.super1 = units.Relay("super1")
        self.super2 = units.Relay("super2")
        self.super3 = units.Relay("super3")
        self.super4 = units.Relay("super4")
        self.super5 = units.Relay("super5")
        self.super6 = units.Relay("super6")

        #Check for status of the replay register zero switch.  If positive
        #and machine is just powered on, this will zero out the replays.
        self.replay_reset = units.Relay("replay_reset")
        
        #When engage()d, light 6v circuit, and enable game features, scoring,
        #etc. Disengage()d means that the machine is 'soft' tilted. 
        self.anti_cheat = units.Relay("anti_cheat")

        #Reflex controls extra connections to the double winners and corners trips
        self.reflex = units.Reflex("primary", 200)

        #When engage()d, spin.
        self.start = units.Relay("start")

        # Now, the control unit can be in one of two positions, essentially.
        # This alternates by coin, and is used to help portion the corners trips.
        self.cu = 1

        #The probability disc handles the dispersion of corners for each card
        #upon coin or button press.  It also handles the probability for
        #the double or nothing routine. In Ticker Tape, it's called the
        #'Random Disc' and is driven by a motor.
        self.probability = units.Spotting("probability", 24)

        #Tilt is separate from anti-cheat in that the trip will move the shutter
        #when the game is tilted with 1st ball in the lane.  Also prevents you
        #from picking back up by killing the anti-cheat.  Can be engaged by 
        #tilt bob, slam tilt switches, or timer at 39th step.
        #Immediately kills motors.
        self.tilt = units.Relay("tilt")

        self.replays = 0

        #Just a little variable to help track the status of blinking elements to make them blink in sync.
        self.blink = 0

        #Magic Number stuff
        self.magic = []
        self.magic_motor = units.Spotting("magic_motor", 5)
        self.onetwothree = units.Relay("onetwothree")
        self.fourfivesix = units.Relay("fourfivesix")

        #Double-Double feature
        self.dd_motor = units.Spotting("dd_motor", 3)
        self.dd1 = units.Relay("dd1")
        self.dd2 = units.Relay("dd2")
        self.dd3 = units.Relay("dd3")
        self.dd4 = units.Relay("dd4")
        self.dd5 = units.Relay("dd5")
        self.dd6 = units.Relay("dd6")

        #Regular Winner Relays
        self.card1_regular = units.Relay("card1_regular")
        self.card2_regular = units.Relay("card2_regular")
        self.card3_regular = units.Relay("card3_regular")
        self.card4_regular = units.Relay("card4_regular")
        self.card5_regular = units.Relay("card5_regular")
        self.card6_regular = units.Relay("card6_regular")

        #Double Relays
        self.card1_double = units.Relay("card1_double")
        self.card2_double = units.Relay("card2_double")
        self.card3_double = units.Relay("card3_double")
        self.card4_double = units.Relay("card4_double")
        self.card5_double = units.Relay("card5_double")
        self.card6_double = units.Relay("card6_double")

        #Missed Relays
        self.card1_missed = units.Relay("card1_missed")
        self.card2_missed = units.Relay("card2_missed")
        self.card3_missed = units.Relay("card3_missed")
        self.card4_missed = units.Relay("card4_missed")
        self.card5_missed = units.Relay("card5_missed")
        self.card6_missed = units.Relay("card6_missed")

        self.returned = False

    def reset(self):
        super(Dixieland, self).reset()
        self.logger = logging.getLogger('game')
        self.load_config('bingo.yaml')
        
        main_mode = MulticardBingo(self)
        self.modes.add(main_mode)
        
game = Dixieland(machine_type='pdb')
game.reset()
game.run_loop()
