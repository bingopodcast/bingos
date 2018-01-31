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
from bingo_emulator.graphics.frolics import *

class MulticardBingo(procgame.game.Mode):
    def __init__(self, game):
        super(MulticardBingo, self).__init__(game=game, priority=5)
        self.holes = []
        self.startup()
        self.game.sound.register_music('motor', "audio/six_card_motor.wav")
        self.game.sound.register_music('search', "audio/six_card_search_old.wav")
        self.game.sound.register_sound('add', "audio/six_card_add_card.wav")
        self.game.sound.register_sound('tilt', "audio/tilt.wav")
        self.game.sound.register_sound('step', "audio/step.wav")

    def sw_coin_active(self, sw):
        self.game.cu = not self.game.cu 
        if self.game.eb_play.status == False:
            self.game.tilt.disengage()
            self.regular_play()
        else:
            self.sw_yellow_active(sw)
        self.delay(name="display", delay=0.1, handler=graphics.frolics.display, param=self)

    def sw_startButton_active(self, sw):
        if self.game.eb_play.status == True:
            self.game.eb_play.disengage()
            self.delay(name="display", delay=0.1, handler=graphics.frolics.display, param=self)
        if self.game.replays > 0 or self.game.switches.freeplay.is_active():
            self.game.tilt.disengage()
            self.regular_play()

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
            os.system("/home/nbaldridge/proc/bingo_emulator/start_game.sh frolics")


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
        self.cancel_delayed(name="card1_replay_step_up")
        self.cancel_delayed(name="card2_replay_step_up")
        self.cancel_delayed(name="card3_replay_step_up")
        self.cancel_delayed(name="card4_replay_step_up")
        self.cancel_delayed(name="card5_replay_step_up")
        self.cancel_delayed(name="card6_replay_step_up")
        self.cancel_delayed(name="timeout")
        self.game.search_index.disengage()
        self.game.coils.counter.pulse()
        self.game.returned = False
        self.game.cu = not self.game.cu
        self.game.sound.stop('add')
        self.game.sound.play('add')
        self.game.mixer1.spin()
        self.game.spotting.spin()
        self.game.mixer2.spin()
        if self.game.start.status == True:
            s = random.randint(1,2)
            self.animate_feature_scan(s)
            if self.game.selector.position <= 5:
                self.game.selector.step()
            self.check_odds()
            self.check_super()
            if self.game.switches.shutter.is_inactive():
                self.game.coils.shutter.enable()
            self.replay_step_down()
            self.check_lifter_status()
        else:
            self.game.start.engage(self.game)
            self.game.card1_replay_counter.reset()
            self.game.card2_replay_counter.reset()
            self.game.card3_replay_counter.reset()
            self.game.card4_replay_counter.reset()
            self.game.card5_replay_counter.reset()
            self.game.card6_replay_counter.reset()
            self.game.eb_play.disengage()
            self.game.odds.reset()
            self.game.super1.disengage()
            self.game.super2.disengage()
            self.game.super3.disengage()
            self.game.super4.disengage()
            self.game.super5.disengage()
            self.game.super6.disengage()
            self.game.timer.reset()
            self.game.red_star.disengage()
            self.game.coils.redROLamp.disable()
            self.game.yellow_star.disengage()
            self.game.coils.yellowROLamp.disable()
            self.game.selector.reset()
            self.game.extra_ball.reset()
            self.game.ball_count.reset()
            self.game.sound.play_music('motor', -1)
            if self.game.top_score.status == True:
                self.game.odds.step()
                self.delay(name="display", delay=0.1, handler=graphics.frolics.display, param=self)
                self.game.odds.step()
                self.delay(name="display", delay=0.1, handler=graphics.frolics.display, param=self)
                self.game.odds.step()
                self.delay(name="display", delay=0.1, handler=graphics.frolics.display, param=self)
                self.game.odds.step()
                self.delay(name="display", delay=0.1, handler=graphics.frolics.display, param=self)
                self.game.odds.step()
                self.delay(name="display", delay=0.1, handler=graphics.frolics.display, param=self)
                self.game.top_score.disengage()
            self.regular_play()
        self.delay(name="display", delay=0.1, handler=graphics.frolics.display, param=self)
        self.game.tilt.disengage()

    def check_mixer(self):
        if self.game.reflex.connected_rivet(5) == 5:
            return 1
        elif self.game.mixer1.position in [1,7,11,15,19] and self.game.reflex.connected_rivet(5) >= 4:
            return 1
        elif self.game.mixer1.position in [2,8,12,16,20] and self.game.reflex.connected_rivet(5) >= 3:
            return 1
        elif (self.game.mixer1.position in [3,4,9,13,17,21]) and self.game.reflex.connected_rivet(5) >= 2:
            return 1
        elif (self.game.mixer1.position in [5,6,10,14,18,22]) and self.game.reflex.connected_rivet(5) >= 1:
            return 1
        else:
            return 0


    def check_super(self):
        i = self.check_mixer()
        if i == True:
            if self.game.selector.position < 6:
                if self.game.spotting.position == 31:
                    self.game.super1.engage(self.game)
                if self.game.spotting.position == 13 and self.game.super4.status == False:
                    self.game.super1.engage(self.game)
                if self.game.spotting.position == 8:
                    self.game.super2.engage(self.game)
                if self.game.spotting.position == 18 and self.game.super5.status == False:
                    self.game.super2.engage(self.game)
                if self.game.spotting.position == 48:
                    self.game.super3.engage(self.game)
                if self.game.spotting.position == 7 and self.game.super6.status == False:
                    self.game.super3.engage(self.game)
                if self.game.spotting.position == 20:
                    self.game.super4.engage(self.game)
                if self.game.spotting.position == 23 and self.game.super1.status == False:
                    self.game.super4.engage(self.game)
                if self.game.spotting.position == 12:
                    self.game.super5.engage(self.game)
                if self.game.spotting.position == 25 and self.game.super2.status == False:
                    self.game.super5.engage(self.game)
                if self.game.spotting.position == 35:
                    self.game.super6.engage(self.game)
                if self.game.spotting.position == 38 and self.game.super3.status == False:
                    self.game.super6.engage(self.game)
                if self.game.spotting.position == 22:
                    self.game.yellow_star.engage(self.game)
                    self.game.coils.redROLamp.enable()
                if self.game.spotting.position == 33:
                    self.game.red_star.engage(self.game)
                    self.game.coils.yellowROLamp.enable()
            else:
                #This adds another connection to the spotting disc.  When you have all six
                #cards awarded, you can earn two advantages at once.
                if self.game.spotting.position == 31:
                    self.game.super1.engage(self.game)
                    self.game.super6.engage(self.game)
                if self.game.spotting.position == 13 and self.game.super4.status == False:
                    self.game.super1.engage(self.game)
                    if self.game.super3.status == False:
                        self.game.super6.engage(self.game)
                if self.game.spotting.position == 8:
                    self.game.super2.engage(self.game)
                    self.game.red_star.engage(self.game)
                    self.game.coils.yellowROLamp.enable()
                if self.game.spotting.position == 18:
                    if self.game.super5.status == False:
                        self.game.super2.engage(self.game)
                    self.game.yellow_star.engage(self.game)
                    self.game.coils.redROLamp.enable()
                if self.game.spotting.position == 48:
                    self.game.super3.engage(self.game)
                    self.game.super1.engage(self.game)
                if self.game.spotting.position == 7 and self.game.super6.status == False:
                    self.game.super3.engage(self.game)
                    if self.game.super4.status == False:
                        self.game.super1.engage(self.game)
                if self.game.spotting.position == 20:
                    self.game.super4.engage(self.game)
                    self.game.super2.engage(self.game)
                if self.game.spotting.position == 23:
                    if self.game.super1.status == False:
                        self.game.super4.engage(self.game)
                    if self.game.super5.status == False:
                        self.game.super2.engage(self.game)
                if self.game.spotting.position == 12:
                    self.game.super5.engage(self.game)
                    self.game.super3.engage(self.game)
                if self.game.spotting.position == 25:
                    if self.game.super2.status == False:
                        self.game.super5.engage(self.game)
                    if self.game.super6.status == False:
                        self.game.super3.engage(self.game)
                if self.game.spotting.position == 35:
                    self.game.super6.engage(self.game)
                    self.game.super4.engage(self.game)
                if self.game.spotting.position == 38:
                    if self.game.super3.status == False:
                        self.game.super6.engage(self.game)
                    if self.game.super1.status == False:
                        self.game.super4.engage(self.game)
                if self.game.spotting.position == 22:
                    self.game.yellow_star.engage(self.game)
                    self.game.coils.redROLamp.enable()
                    if self.game.super2.status == False:
                        self.game.super5.engage(self.game)
                if self.game.spotting.position == 33:
                    self.game.red_star.engage(self.game)
                    self.game.coils.yellowROLamp.enable()
                    self.game.super5.engage(self.game)


    def check_odds(self):
        p = self.odds_probability()
        if p == 1:
            es = self.check_extra_step()
            if es == 1:
                i = random.randint(1,3)
                self.extra_step(i)
            else:
                self.game.odds.step()

    def odds_probability(self):
        return self.check_mixer()

    def check_extra_step(self):
        i = random.randint(0,32)
        if i == 16:
            return 1
        else:
            return 0

    def extra_step(self, number):
        if number > 0:
            self.game.odds.step()
            self.game.coils.counter.pulse()
            self.delay(name="display", delay=0.1, handler=graphics.frolics.display, param=self)
            number -= 1
            self.delay(name="extra_step", delay=0.1, handler=self.extra_step, param=number)

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
                    if self.game.returned == True and self.game.ball_count.position in [4,5,6]:
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


    def sw_gate_inactive_for_1ms(self, sw):
        self.game.start.disengage()
        if self.game.switches.shutter.is_active():
            self.game.coils.shutter.enable()
        self.game.ball_count.step()
        if self.game.ball_count.position >= 4:
            if self.game.search_index.status == False:
                self.search()
        if self.game.ball_count.position <= 6:
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
            self.delay(name="display", delay=0.1, handler=graphics.frolics.display, param=self)

    def sw_hole2_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(2)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.frolics.display, param=self)

    def sw_hole3_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(3)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.frolics.display, param=self)

    def sw_hole4_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(4)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.frolics.display, param=self)

    def sw_hole5_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(5)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.frolics.display, param=self)

    def sw_hole6_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(6)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.frolics.display, param=self)

    def sw_hole7_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(7)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.frolics.display, param=self)

    def sw_hole8_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(8)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.frolics.display, param=self)

    def sw_hole9_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(9)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.frolics.display, param=self)

    def sw_hole10_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(10)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.frolics.display, param=self)

    def sw_hole11_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(11)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.frolics.display, param=self)

    def sw_hole12_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(12)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.frolics.display, param=self)

    def sw_hole13_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(13)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.frolics.display, param=self)

    def sw_hole14_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(14)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.frolics.display, param=self)

    def sw_hole15_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(15)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.frolics.display, param=self)

    def sw_hole16_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(16)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.frolics.display, param=self)

    def sw_hole17_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(17)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.frolics.display, param=self)

    def sw_hole18_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(18)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.frolics.display, param=self)

    def sw_hole19_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(19)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.frolics.display, param=self)

    def sw_hole20_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(20)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.frolics.display, param=self)

    def sw_hole21_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(21)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.frolics.display, param=self)

    def sw_hole22_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(22)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.frolics.display, param=self)

    def sw_hole23_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(23)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.frolics.display, param=self)

    def sw_hole24_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(24)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.frolics.display, param=self)

    def sw_hole25_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(25)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.frolics.display, param=self)

    def sw_replayReset_active(self, sw):
        self.game.anti_cheat.disengage()
        self.holes = []
        graphics.frolics.display(self)
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
        self.game.search_index.disengage()
        self.game.coils.redROLamp.disable()
        self.game.coils.yellowROLamp.disable()
        if self.game.ball_count.position == 0:
            if self.game.switches.shutter.is_active():
                self.game.coils.shutter.enable()
        self.holes = []
        self.game.selector.reset()
        self.game.ball_count.reset()
        self.game.odds.reset()
        self.game.extra_ball.reset()
        self.game.super1.disengage()
        self.game.super2.disengage()
        self.game.super3.disengage()
        self.game.super4.disengage()
        self.game.super5.disengage()
        self.game.super6.disengage()
        self.game.red_star.disengage()
        self.game.coils.redROLamp.disable()
        self.game.yellow_star.disengage()
        self.game.coils.yellowROLamp.disable()
        self.game.eb_play.disengage()
        self.game.anti_cheat.engage(game)
        self.game.tilt.engage(self.game)
        self.game.sound.stop_music()
        self.game.sound.play('tilt')
        # displays "Tilt" on the backglass, you have to recoin.
        self.delay(name="display", delay=0.1, handler=graphics.frolics.display, param=self)

    def sw_tilt_active(self, sw):
        if self.game.tilt.status == False:
            self.tilt_actions()

    def sw_yellow_active(self, sw):
        self.game.cu = not self.game.cu
        if self.game.ball_count.position >= 4:
            if self.game.eb_play.status == False:
                self.game.eb_play.engage(self.game)
                self.delay(name="display", delay=0.1, handler=graphics.frolics.display, param=self)
                self.sw_yellow_active(sw)
            if self.game.eb_play.status == True and (self.game.replays > 0 or self.game.switches.freeplay.is_active() or self.game.switches.coin.is_active()):
                self.game.sound.stop('add')
                self.game.sound.play('add')
                self.game.cu = not self.game.cu
                self.game.spotting.spin()
                self.game.mixer1.spin()
                self.game.mixer2.spin()
                self.scan_eb()
                self.replay_step_down()
                self.game.reflex.decrease()
                self.delay(name="display", delay=0.1, handler=graphics.frolics.display, param=self)

    def sw_redstar_active(self, sw):
        if self.game.red_star.status == True:
            self.game.top_score.engage(self.game)
            self.game.red_star.disengage()
            self.game.yellow_star.disengage()
            self.game.coils.redROLamp.disable()
            self.game.coils.yellowROLamp.disable()
            self.delay(name="display", delay=0.1, handler=graphics.frolics.display, param=self)

    def sw_yellowstar_active(self, sw):
        if self.game.yellow_star.status == True:
            self.game.top_score.engage(self.game)
            self.game.yellow_star.disengage()
            self.game.red_star.disengage()
            self.game.coils.redROLamp.disable()
            self.game.coils.yellowROLamp.disable()
            self.delay(name="display", delay=0.1, handler=graphics.frolics.display, param=self)


    def scan_eb(self):
        s = random.randint(1,6)
        self.animate_eb_scan(s)
        i = self.check_mixer()
        if i == True:
            if self.game.super1.status == False:
                if self.game.mixer2.position == 1:
                    self.check_spotting()
            if self.game.super2.status == False:
                if self.game.mixer2.position == 2:
                    self.check_spotting()
            if self.game.super3.status == False:
                if self.game.mixer2.position == 3:
                    self.check_spotting()
            if self.game.super4.status == False:
                if self.game.mixer2.position == 4:
                    self.check_spotting()
            if self.game.super5.status == False:
                if self.game.mixer2.position == 5:
                    self.check_spotting()
            if self.game.super6.status == False:
                if self.game.mixer2.position == 6:
                    self.check_spotting()
            self.game.spotting.spin()
            self.check_spotting()

    def animate_feature_scan(self, s):
        if s > 1:
            self.delay(name="feature_animation", delay=0.1, handler=graphics.frolics.feature_animation, param=s)
            self.delay(name="display", delay=0.1, handler=graphics.frolics.display, param=self)
            s -= 1
            #self.delay(name="animate_feature", delay=0.1, handler=self.animate_feature_scan, param=s)
        else:
            self.delay(name="display", delay=0.1, handler=graphics.frolics.display, param=self)

    def animate_eb_scan(self, s):
        if s > 1:
            self.delay(name="eb_animation", delay=0.1, handler=graphics.frolics.eb_animation, param=s)
            self.delay(name="display", delay=0.1, handler=graphics.frolics.display, param=self)
            s -= 1
            #self.delay(name="animate_eb", delay=0.1, handler=self.animate_eb_scan, param=s)
        else:
            self.delay(name="display", delay=0.1, handler=graphics.frolics.display, param=self)


    def check_spotting(self):
        if self.game.spotting.position in [1,5,17]:
            self.game.extra_ball.step()
            self.check_lifter_status()
            self.delay(name="display", delay=0.1, handler=graphics.frolics.display, param=self)
        if self.game.spotting.position in [14,20,33,40]:
            if self.game.extra_ball.position < 3:
                self.game.extra_ball.step()
                self.check_lifter_status()
                self.delay(name="display", delay=0.1, handler=graphics.frolics.display, param=self)
        if self.game.spotting.position == 15:
            number = 6 - self.game.extra_ball.position
            self.step_eb(number)
            self.check_lifter_status()
            self.delay(name="display", delay=0.1, handler=graphics.frolics.display, param=self)
        if self.game.spotting.position == 4:
            if self.game.extra_ball.position < 4:
                number = 3 - self.game.extra_ball.position
                self.step_eb(number)
                self.check_lifter_status()
                self.delay(name="display", delay=0.1, handler=graphics.frolics.display, param=self)
        if self.game.spotting.position == 36:
            number = 6 - self.game.extra_ball.position
            self.step_eb(number)
            self.check_lifter_status()
            self.delay(name="display", delay=0.1, handler=graphics.frolics.display, param=self)
        if self.game.extra_ball.position == 3 or self.game.extra_ball.position == 6:
            self.check_lifter_status()

    def step_eb(self, number):
        if number > 0:
            self.game.extra_ball.step()
            self.check_lifter_status()
            self.delay(name="display", delay=0.1, handler=graphics.frolics.display, param=self)
            number -= 1
            self.delay(name="step_eb", delay=0.1, handler=self.step_eb, param=number)

    def replay_step_down(self, number=0):
        if number > 0:
            if number > 1:
                self.game.replays -= 1
                graphics.replay_step_down(self.game.replays, graphics.frolics.reel1, graphics.frolics.reel10, graphics.frolics.reel100)
                self.game.coils.registerDown.pulse()
                number -= 1
                graphics.frolics.display(self)
                self.delay(name="replay_reset", delay=0.13, handler=self.replay_step_down, param=number)
            elif number == 1:
                self.game.replays -= 1
                graphics.replay_step_down(self.game.replays, graphics.frolics.reel1, graphics.frolics.reel10, graphics.frolics.reel100)
                self.game.coils.registerDown.pulse()
                number -= 1
                graphics.frolics.display(self)
                self.cancel_delayed(name="replay_reset")
        else: 
            if self.game.replays > 0:
                self.game.replays -= 1
                graphics.replay_step_down(self.game.replays, graphics.frolics.reel1, graphics.frolics.reel10, graphics.frolics.reel100)
                self.delay(name="display", delay=0.1, handler=graphics.frolics.display, param=self)
            self.game.coils.registerDown.pulse()

    def replay_step_up(self):
        if self.game.replays < 899:
            self.game.replays += 1
            graphics.replay_step_up(self.game.replays, graphics.frolics.reel1, graphics.frolics.reel10, graphics.frolics.reel100)
        self.game.coils.registerUp.pulse()
        graphics.frolics.display(self)
 
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
        self.game.sound.stop_music()
        self.game.sound.play_music('search', -1)

        for i in range(0, 100):
            if i <= 50:
                self.r = self.closed_search_relays(self.game.searchdisc.position)
                self.game.searchdisc.spin()
            if i >= 51:
                self.r = self.closed_search_relays(self.game.searchdisc2.position + 50)
                self.game.searchdisc2.spin()
            self.wipers = self.r[0]
            self.card = self.r[1]

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
                            if s >= 3:
                                self.find_winner(s, self.card)
                                break
        

    def find_winner(self, relays, card):
        if self.game.search_index.status == False and self.game.replays < 899:
            if card == 1:
                if relays == 3:
                    if self.game.super1.status == False:
                        if self.game.card1_replay_counter.position < 3:
                            self.game.search_index.engage(self.game)
                            self.card1_replay_step_up(3 - self.game.card1_replay_counter.position)
                    else:
                        if self.game.odds.position == 1:
                            hit = 4
                        elif self.game.odds.position == 2:
                            hit = 6
                        elif self.game.odds.position == 3:
                            hit = 8
                        elif self.game.odds.position == 4:
                            hit = 12
                        elif self.game.odds.position == 5:
                            hit = 16
                        if self.game.card1_replay_counter.position < hit:
                            self.game.search_index.engage(self.game)
                            self.card1_replay_step_up(hit - self.game.card1_replay_counter.position)
                if relays == 4:
                    if self.game.super1.status == False:
                        if self.game.card1_replay_counter.position < 16:
                            self.game.search_index.engage(self.game)
                            self.card1_replay_step_up(16 - self.game.card1_replay_counter.position)
                    else:
                        if self.game.odds.position == 1:
                            hit = 24
                        elif self.game.odds.position == 2:
                            hit = 36
                        elif self.game.odds.position == 3:
                            hit = 48
                        elif self.game.odds.position == 4:
                            hit = 72
                        elif self.game.odds.position == 5:
                            hit = 96
                        if self.game.card1_replay_counter.position < hit:
                            self.game.search_index.engage(self.game)
                            self.card1_replay_step_up(hit - self.game.card1_replay_counter.position)
                if relays == 5:
                    if self.game.super1.status == False:
                        if self.game.card1_replay_counter.position < 50:
                            self.game.search_index.engage(self.game)
                            self.card1_replay_step_up(50 - self.game.card1_replay_counter.position)
                    else:
                        if self.game.odds.position == 1:
                            hit = 50
                        elif self.game.odds.position == 2:
                            hit = 75
                        elif self.game.odds.position == 3:
                            hit = 100
                        elif self.game.odds.position == 4:
                            hit = 150
                        elif self.game.odds.position == 5:
                            hit = 200
                        if self.game.card1_replay_counter.position < hit:
                            self.game.search_index.engage(self.game)
                            self.card1_replay_step_up(hit - self.game.card1_replay_counter.position)
            if card == 2:
                if relays == 3:
                    if self.game.super2.status == False:
                        if self.game.card2_replay_counter.position < 3:
                            self.game.search_index.engage(self.game)
                            self.card2_replay_step_up(3 - self.game.card2_replay_counter.position)
                    else:
                        if self.game.odds.position == 1:
                            hit = 4
                        elif self.game.odds.position == 2:
                            hit = 6
                        elif self.game.odds.position == 3:
                            hit = 8
                        elif self.game.odds.position == 4:
                            hit = 12
                        elif self.game.odds.position == 5:
                            hit = 16
                        if self.game.card2_replay_counter.position < hit:
                            self.game.search_index.engage(self.game)
                            self.card2_replay_step_up(hit - self.game.card2_replay_counter.position)
                if relays == 4:
                    if self.game.super2.status == False:
                        if self.game.card2_replay_counter.position < 16:
                            self.game.search_index.engage(self.game)
                            self.card2_replay_step_up(16 - self.game.card2_replay_counter.position)
                    else:
                        if self.game.odds.position == 1:
                            hit = 24
                        elif self.game.odds.position == 2:
                            hit = 36
                        elif self.game.odds.position == 3:
                            hit = 48
                        elif self.game.odds.position == 4:
                            hit = 72
                        elif self.game.odds.position == 5:
                            hit = 96
                        if self.game.card2_replay_counter.position < hit:
                            self.game.search_index.engage(self.game)
                            self.card2_replay_step_up(hit - self.game.card2_replay_counter.position)
                if relays == 5:
                    if self.game.super2.status == False:
                        if self.game.card2_replay_counter.position < 50:
                            self.game.search_index.engage(self.game)
                            self.card2_replay_step_up(50 - self.game.card2_replay_counter.position)
                    else:
                        if self.game.odds.position == 1:
                            hit = 50
                        elif self.game.odds.position == 2:
                            hit = 75
                        elif self.game.odds.position == 3:
                            hit = 100
                        elif self.game.odds.position == 4:
                            hit = 150
                        elif self.game.odds.position == 5:
                            hit = 200
                        if self.game.card2_replay_counter.position < hit:
                            self.game.search_index.engage(self.game)
                            self.card2_replay_step_up(hit - self.game.card2_replay_counter.position)
            if card == 3:
                if relays == 3:
                    if self.game.super3.status == False:
                        if self.game.card3_replay_counter.position < 3:
                            self.game.search_index.engage(self.game)
                            self.card3_replay_step_up(3 - self.game.card3_replay_counter.position)
                    else:
                        if self.game.odds.position == 1:
                            hit = 4
                        elif self.game.odds.position == 2:
                            hit = 6
                        elif self.game.odds.position == 3:
                            hit = 8
                        elif self.game.odds.position == 4:
                            hit = 12
                        elif self.game.odds.position == 5:
                            hit = 16
                        if self.game.card3_replay_counter.position < hit:
                            self.game.search_index.engage(self.game)
                            self.card3_replay_step_up(hit - self.game.card3_replay_counter.position)
                if relays == 4:
                    if self.game.super3.status == False:
                        if self.game.card3_replay_counter.position < 16:
                            self.game.search_index.engage(self.game)
                            self.card3_replay_step_up(16 - self.game.card3_replay_counter.position)
                    else:
                        if self.game.odds.position == 1:
                            hit = 24
                        elif self.game.odds.position == 2:
                            hit = 36
                        elif self.game.odds.position == 3:
                            hit = 48
                        elif self.game.odds.position == 4:
                            hit = 72
                        elif self.game.odds.position == 5:
                            hit = 96
                        if self.game.card3_replay_counter.position < hit:
                            self.game.search_index.engage(self.game)
                            self.card3_replay_step_up(hit - self.game.card3_replay_counter.position)
                if relays == 5:
                    if self.game.super3.status == False:
                        if self.game.card3_replay_counter.position < 50:
                            self.game.search_index.engage(self.game)
                            self.card3_replay_step_up(50 - self.game.card3_replay_counter.position)
                    else:
                        if self.game.odds.position == 1:
                            hit = 50
                        elif self.game.odds.position == 2:
                            hit = 75
                        elif self.game.odds.position == 3:
                            hit = 100
                        elif self.game.odds.position == 4:
                            hit = 150
                        elif self.game.odds.position == 5:
                            hit = 200
                        if self.game.card3_replay_counter.position < hit:
                            self.game.search_index.engage(self.game)
                            self.card3_replay_step_up(hit - self.game.card3_replay_counter.position)
            if card == 4:
                if relays == 3:
                    if self.game.super4.status == False:
                        if self.game.card4_replay_counter.position < 3:
                            self.game.search_index.engage(self.game)
                            self.card4_replay_step_up(3 - self.game.card4_replay_counter.position)
                    else:
                        if self.game.odds.position == 1:
                            hit = 4
                        elif self.game.odds.position == 2:
                            hit = 6
                        elif self.game.odds.position == 3:
                            hit = 8
                        elif self.game.odds.position == 4:
                            hit = 12
                        elif self.game.odds.position == 5:
                            hit = 16
                        if self.game.card4_replay_counter.position < hit:
                            self.game.search_index.engage(self.game)
                            self.card4_replay_step_up(hit - self.game.card4_replay_counter.position)

                if relays == 4:
                    if self.game.super4.status == False:
                        if self.game.card4_replay_counter.position < 16:
                            self.game.search_index.engage(self.game)
                            self.card4_replay_step_up(16 - self.game.card4_replay_counter.position)
                    else:
                        if self.game.odds.position == 1:
                            hit = 24
                        elif self.game.odds.position == 2:
                            hit = 36
                        elif self.game.odds.position == 3:
                            hit = 48
                        elif self.game.odds.position == 4:
                            hit = 72
                        elif self.game.odds.position == 5:
                            hit = 96
                        if self.game.card4_replay_counter.position < hit:
                            self.game.search_index.engage(self.game)
                            self.card4_replay_step_up(hit - self.game.card4_replay_counter.position)

                if relays == 5:
                    if self.game.super4.status == False:
                        if self.game.card4_replay_counter.position < 50:
                            self.game.search_index.engage(self.game)
                            self.card4_replay_step_up(50 - self.game.card4_replay_counter.position)
                    else:
                        if self.game.odds.position == 1:
                            hit = 50
                        elif self.game.odds.position == 2:
                            hit = 75
                        elif self.game.odds.position == 3:
                            hit = 100
                        elif self.game.odds.position == 4:
                            hit = 150
                        elif self.game.odds.position == 5:
                            hit = 200
                        if self.game.card4_replay_counter.position < hit:
                            self.game.search_index.engage(self.game)
                            self.card4_replay_step_up(hit - self.game.card4_replay_counter.position)

            if card == 5:
                if relays == 3:
                    if self.game.super5.status == False:
                        if self.game.card5_replay_counter.position < 3:
                            self.game.search_index.engage(self.game)
                            self.card5_replay_step_up(3 - self.game.card5_replay_counter.position)
                    else:
                        if self.game.odds.position == 1:
                            hit = 4
                        elif self.game.odds.position == 2:
                            hit = 6
                        elif self.game.odds.position == 3:
                            hit = 8
                        elif self.game.odds.position == 4:
                            hit = 12
                        elif self.game.odds.position == 5:
                            hit = 16
                        if self.game.card5_replay_counter.position < hit:
                            self.game.search_index.engage(self.game)
                            self.card5_replay_step_up(hit - self.game.card5_replay_counter.position)

                if relays == 4:
                    if self.game.super5.status == False:
                        if self.game.card5_replay_counter.position < 16:
                            self.game.search_index.engage(self.game)
                            self.card5_replay_step_up(16 - self.game.card5_replay_counter.position)
                    else:
                        if self.game.odds.position == 1:
                            hit = 24
                        elif self.game.odds.position == 2:
                            hit = 36
                        elif self.game.odds.position == 3:
                            hit = 48
                        elif self.game.odds.position == 4:
                            hit = 72
                        elif self.game.odds.position == 5:
                            hit = 96
                        if self.game.card5_replay_counter.position < hit:
                            self.game.search_index.engage(self.game)
                            self.card5_replay_step_up(hit - self.game.card5_replay_counter.position)

                if relays == 5:
                    if self.game.super5.status == False:
                        if self.game.card5_replay_counter.position < 50:
                            self.game.search_index.engage(self.game)
                            self.card5_replay_step_up(50 - self.game.card5_replay_counter.position)
                    else:
                        if self.game.odds.position == 1:
                            hit = 50
                        elif self.game.odds.position == 2:
                            hit = 75
                        elif self.game.odds.position == 3:
                            hit = 100
                        elif self.game.odds.position == 4:
                            hit = 150
                        elif self.game.odds.position == 5:
                            hit = 200
                        if self.game.card5_replay_counter.position < hit:
                            self.game.search_index.engage(self.game)
                            self.card5_replay_step_up(hit - self.game.card5_replay_counter.position)

            if card == 6:
                if relays == 3:
                    if self.game.super6.status == False:
                        if self.game.card6_replay_counter.position < 3:
                            self.game.search_index.engage(self.game)
                            self.card6_replay_step_up(3 - self.game.card6_replay_counter.position)
                    else:
                        if self.game.odds.position == 1:
                            hit = 4
                        elif self.game.odds.position == 2:
                            hit = 6
                        elif self.game.odds.position == 3:
                            hit = 8
                        elif self.game.odds.position == 4:
                            hit = 12
                        elif self.game.odds.position == 5:
                            hit = 16
                        if self.game.card6_replay_counter.position < hit:
                            self.game.search_index.engage(self.game)
                            self.card6_replay_step_up(hit - self.game.card6_replay_counter.position)

                if relays == 4:
                    if self.game.super6.status == False:
                        if self.game.card6_replay_counter.position < 16:
                            self.game.search_index.engage(self.game)
                            self.card6_replay_step_up(16 - self.game.card6_replay_counter.position)
                    else:
                        if self.game.odds.position == 1:
                            hit = 24
                        elif self.game.odds.position == 2:
                            hit = 36
                        elif self.game.odds.position == 3:
                            hit = 48
                        elif self.game.odds.position == 4:
                            hit = 72
                        elif self.game.odds.position == 5:
                            hit = 96
                        if self.game.card6_replay_counter.position < hit:
                            self.game.search_index.engage(self.game)
                            self.card6_replay_step_up(hit - self.game.card6_replay_counter.position)

                if relays == 5:
                    if self.game.super6.status == False:
                        if self.game.card6_replay_counter.position < 50:
                            self.game.search_index.engage(self.game)
                            self.card6_replay_step_up(50 - self.game.card6_replay_counter.position)
                    else:
                        if self.game.odds.position == 1:
                            hit = 50
                        elif self.game.odds.position == 2:
                            hit = 75
                        elif self.game.odds.position == 3:
                            hit = 100
                        elif self.game.odds.position == 4:
                            hit = 150
                        elif self.game.odds.position == 5:
                            hit = 200
                        if self.game.card6_replay_counter.position < hit:
                            self.game.search_index.engage(self.game)
                            self.card6_replay_step_up(hit - self.game.card6_replay_counter.position)


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

    def card2_replay_step_up(self, number):
        if number >= 1:
            self.game.card2_replay_counter.step()
            number -= 1
            self.replay_step_up()
            if self.game.replays == 899:
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
            if self.game.replays == 899:
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
            if self.game.replays == 899:
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
            if self.game.replays == 899:
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
            if self.game.replays == 899:
                number = 0
            self.delay(name="card6_replay_step_up", delay=0.1, handler=self.card6_replay_step_up, param=number)
        else:
            self.game.search_index.disengage()
            self.cancel_delayed(name="card6_replay_step_up")
            self.search()

    def closed_search_relays(self, rivets):
        # This function is critical, as it will determine which card is returned, etc.  I need to check both the position of the
        # replay counter for the card, as well as the selector unit to ensure that the card is selected. We will get a row back
        # that has the numbers on the position which will return the search relay connected.  When three out of the five relays
        # are connected, we get a winner!
        
        self.pos = {}
        # Card 1
        self.pos[0] = {}
        self.pos[1] = {5:1, 1:2, 9:3, 25:4, 3:5}
        self.pos[2] = {8:1, 22:2, 10:3, 19:4, 7:5}
        self.pos[3] = {6:1, 18:2, 16:3, 11:4, 17:5}
        self.pos[4] = {24:1, 21:2, 14:3, 20:4, 13:5}
        self.pos[5] = {12:1, 23:2, 2:3, 4:4, 15:5}
        self.pos[6] = {5:1, 8:2, 6:3, 24:4, 12:5}
        self.pos[7] = {1:1, 22:2, 18:3, 21:4, 23:5}
        self.pos[8] = {9:1, 10:2, 16:3, 14:4, 2:5}
        self.pos[9] = {25:1, 19:2, 11:3, 20:4, 4:5}
        self.pos[10] = {3:1, 7:2, 17:3, 13:4, 15:5}
        self.pos[11] = {5:1, 22:2, 16:3, 20:4, 15:5}
        self.pos[12] = {3:1, 19:2, 16:3, 21:4, 12:5}
        self.pos[13] = {}
        self.pos[14] = {}
        self.pos[15] = {}
        self.pos[16] = {}
        self.pos[17] = {}

        # There are five blank positions in between cards.  Early games have less to search!
        # Card 2
        self.pos[18] = {9:1, 24:2, 16:3, 4:4, 6:5}
        self.pos[19] = {13:1, 19:2, 14:3, 20:4, 25:5}
        self.pos[20] = {2:1, 18:2, 15:3, 12:4, 17:5}
        self.pos[21] = {1:1, 22:2, 11:3, 21:4, 8:5}
        self.pos[22] = {10:1, 7:2, 5:3, 23:4, 3:5}
        self.pos[23] = {9:1, 13:2, 2:3, 1:4, 10:5}
        self.pos[24] = {24:1, 19:2, 18:3, 22:4, 7:5}
        self.pos[25] = {16:1, 14:2, 15:3, 11:4, 5:5}
        self.pos[26] = {4:1, 20:2, 12:3, 21:4, 23:5}
        self.pos[27] = {6:1, 25:2, 17:3, 8:4, 3:5}
        self.pos[28] = {9:1, 19:2, 15:3, 21:4, 3:5}
        self.pos[29] = {6:1, 20:2, 15:3, 22:4, 10:5}
        self.pos[30] = {}
        self.pos[31] = {}
        self.pos[32] = {}
        self.pos[33] = {}
        self.pos[34] = {}

        # Another five blank positions.  Can you believe it?
        # Card 3
        self.pos[35] = {3:1, 7:2, 10:3, 4:4, 9:5}
        self.pos[36] = {24:1, 21:2, 18:3, 22:4, 8:5}
        self.pos[37] = {15:1, 14:2, 17:3, 11:4, 2:5}
        self.pos[38] = {13:1, 20:2, 12:3, 19:4, 23:5}
        self.pos[39] = {6:1, 25:2, 16:3, 1:4, 5:5}
        self.pos[40] = {3:1, 24:2, 15:3, 13:4, 6:5}
        self.pos[41] = {7:1, 21:2, 14:3, 20:4, 25:5}
        self.pos[42] = {10:1, 18:2, 17:3, 12:4, 16:5}
        self.pos[43] = {4:1, 22:2, 11:3, 19:4, 1:5}
        self.pos[44] = {9:1, 8:2, 2:3, 23:4, 5:5}
        self.pos[45] = {3:1, 21:2, 17:3, 19:4, 5:5}
        self.pos[46] = {9:1, 22:2, 17:3, 20:4, 6:5}
        self.pos[47] = {}
        self.pos[48] = {}
        self.pos[49] = {}
        self.pos[50] = {}

        # Start of the second search disc modeled as part
        # of the same array for simplicity. Parent function
        # calls this subset.
        # Card #4
        self.pos[51] = {20:1, 24:2, 21:3, 13:4, 14:5}
        self.pos[52] = {25:1, 5:2, 1:3, 3:4, 9:5}
        self.pos[53] = {19:1, 8:2, 22:3, 7:4, 10:5}
        self.pos[54] = {4:1, 12:2, 23:3, 15:4, 2:5}
        self.pos[55] = {11:1, 6:2, 18:3, 17:4, 16:5}
        self.pos[56] = {20:1, 25:2, 19:3, 4:4, 11:5}
        self.pos[57] = {24:1, 5:2, 8:3, 12:4, 6:5}
        self.pos[58] = {21:1, 1:2, 22:3, 23:4, 18:5}
        self.pos[59] = {13:1, 3:2, 7:3, 15:4, 17:5}
        self.pos[60] = {14:1, 9:2, 10:3, 2:4, 16:5}
        self.pos[61] = {20:1, 5:2, 22:3, 15:4, 16:5}
        self.pos[62] = {14:1, 3:2, 22:3, 12:4, 11:5}
        self.pos[63] = {}
        self.pos[64] = {}
        self.pos[65] = {}
        self.pos[66] = {}
        self.pos[67] = {}

        # Card #5
        self.pos[68] = {21:1, 1:2, 22:3, 8:4, 11:5}
        self.pos[69] = {4:1, 9:2, 24:3, 6:4, 16:5}
        self.pos[70] = {20:1, 13:2, 19:3, 25:4, 14:5}
        self.pos[71] = {23:1, 10:2, 7:3, 3:4, 5:5}
        self.pos[72] = {12:1, 2:2, 18:3, 17:4, 15:5}
        self.pos[73] = {21:1, 4:2, 20:3, 23:4, 12:5}
        self.pos[74] = {1:1, 9:2, 13:3, 10:4, 2:5}
        self.pos[75] = {22:1, 24:2, 19:3, 7:4, 18:5}
        self.pos[76] = {8:1, 6:2, 25:3, 3:4, 17:5}
        self.pos[77] = {11:1, 16:2, 14:3, 5:4, 15:5}
        self.pos[78] = {21:1, 9:2, 19:3, 3:4, 15:5}
        self.pos[79] = {11:1, 6:2, 19:3, 10:4, 12:5}
        self.pos[80] = {}
        self.pos[81] = {}
        self.pos[82] = {}
        self.pos[83] = {}
        self.pos[84] = {}

        # Card #6
        self.pos[85] = {19:1, 13:2, 20:3, 23:4, 12:5}
        self.pos[86] = {4:1, 3:2, 7:3, 9:4, 10:5}
        self.pos[87] = {22:1, 24:2, 21:3, 8:4, 18:5}
        self.pos[88] = {1:1, 6:2, 25:3, 5:4, 16:5}
        self.pos[89] = {11:1, 15:2, 14:3, 2:4, 17:5}
        self.pos[90] = {19:1, 4:2, 22:3, 1:4, 11:5}
        self.pos[91] = {13:1, 3:2, 24:3, 6:4, 15:5}
        self.pos[92] = {20:1, 7:2, 21:3, 25:4, 14:5}
        self.pos[93] = {23:1, 9:2, 8:3, 5:4, 2:5}
        self.pos[94] = {12:1, 10:2, 18:3, 16:4, 17:5}
        self.pos[95] = {19:1, 3:2, 21:3, 5:4, 17:5}
        self.pos[96] = {12:1, 9:2, 21:3, 6:4, 11:5}
        self.pos[97] = {}
        self.pos[98] = {}
        self.pos[99] = {}
        self.pos[100] = {}

        if rivets in range(0,18):
            card = 1
        if rivets in range(18,35):
            card = 2
        if rivets in range(35,50):
            card = 3
        if rivets in range(50,68):
            card = 4
        if rivets in range(68,85):
            card = 5
        if rivets in range(85,100):
            card = 6

        return (self.pos[rivets], card)
            
    # Define reset as the knock-off, anti-cheat relay disabled, and replay reset enabled.  Motors turn while credits are knocked off.
    # When meter reaches zero and the zero limit switch is hit, turn off motor sound and leave backglass gi on, but with tilt displayed.

    def startup(self):        
        # Every bingo requires the meter to register '0' 
        # before allowing coin entry --
        # also needs to show a plain 'off' backglass.
        self.eb = False
        self.tilt_actions()

class Frolics(procgame.game.BasicGame):
    """ Frolics was one of the only six cards with advancing odds """
    def __init__(self, machine_type):
        super(Frolics, self).__init__(machine_type)
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

        self.cu = 1
        self.mixer1 = units.Mixer("mixer3", 23)
        self.mixer2 = units.Mixer("mixer2", 23)

        # Initialize reflex(es) and mixers unique to this game
        self.reflex = units.Reflex("primary", 200)

        # Noted as selection unit.
        self.spotting = units.Spotting("spotting", 50)

        self.extra_ball = units.Stepper("extra_ball", 6)

        self.super1 = units.Relay("super1")
        self.super2 = units.Relay("super2")
        self.super3 = units.Relay("super3")
        self.super4 = units.Relay("super4")
        self.super5 = units.Relay("super5")
        self.super6 = units.Relay("super6")

        self.odds = units.Stepper("odds", 5)

        self.top_score = units.Relay("top_score")
        self.red_star = units.Relay("red_star")
        self.yellow_star = units.Relay("yellow_star")

        self.eb_play = units.Relay("eb_play")
        self.cu = 1

        #Seach relays
        self.s1 = units.Relay("s1")
        self.s2 = units.Relay("s2")
        self.s3 = units.Relay("s3")
        self.s4 = units.Relay("s4")
        self.s5 = units.Relay("s5")
        self.search_index = units.Relay("search_index")

        #Replay Counter
        self.card1_replay_counter = units.Stepper("card1_replay_counter", 100)
        self.card2_replay_counter = units.Stepper("card2_replay_counter", 100)
        self.card3_replay_counter = units.Stepper("card3_replay_counter", 100)
        self.card4_replay_counter = units.Stepper("card4_replay_counter", 100)
        self.card5_replay_counter = units.Stepper("card5_replay_counter", 100)
        self.card6_replay_counter = units.Stepper("card6_replay_counter", 100)

        #Initialize stepper units used to keep track of features or timing.
        self.selector = units.Stepper("selector", 6)
        self.timer = units.Stepper("timer", 40)
        self.ball_count = units.Stepper("ball_count", 8)

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

        self.replays = 0
        self.returned = False       

    def reset(self):
        super(Frolics, self).reset()
        self.logger = logging.getLogger('game')
        self.load_config('bingo.yaml')
        
        main_mode = MulticardBingo(self)
        self.modes.add(main_mode)
        
game = Frolics(machine_type='pdb')
game.reset()
game.run_loop()
