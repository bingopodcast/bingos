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
from bingo_emulator.graphics.stardust import *

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
        self.game.sound.register_sound('eb_search', "audio/EB_Search.wav")

    def sw_coin_active(self, sw):
        if self.game.eb_play.status == True and self.game.tilt.status == False:
            self.game.sound.stop('add')
            self.game.sound.play('add')
            self.scan_eb()
            self.game.eb_play.disengage()
        else:
            self.game.tilt.disengage()
            self.regular_play()
            self.scan_all()
        self.delay(name="display", delay=0.1, handler=graphics.stardust.display, param=self)

    def sw_startButton_active(self, sw):
        if self.game.replays > 0 or self.game.switches.freeplay.is_active():
            self.game.tilt.disengage()
            self.regular_play()
            self.scan_all()
            self.delay(name="display", delay=0.1, handler=graphics.stardust.display, param=self)

    def sw_trough4_active_for_1s(self, sw):
        if self.game.ball_count.position >= 5:
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

    def sw_enter_active(self, sw):
        if self.game.switches.left.is_active() and self.game.switches.right.is_active():
            self.game.end_run_loop()
            os.system("/home/nbaldridge/proc/bingo_emulator/start_game.sh stardust")


    def sw_left_active(self, sw):
        max_ball = 4
        if self.game.roto_feature_step.position == 6:
            max_ball = 5
        if self.game.roto_feature_step.position >= 4:
            if self.game.ball_count.position < max_ball:
                self.game.roto.step()

        self.delay(name="display", delay=0.1, handler=graphics.stardust.display, param=self)

    def sw_right_active(self, sw):
        max_ball = 4
        if self.game.roto_feature_step.position == 6:
            max_ball = 5
        if self.game.roto_feature_step.position >= 4:
            if self.game.ball_count.position < max_ball:
                self.game.roto2.step()

        self.delay(name="display", delay=0.1, handler=graphics.stardust.display, param=self)

    def sw_redstar_active(self, sw):
        if self.game.red_star.status == True:
            self.game.all_spot.engage(self.game)
            if 5 not in self.holes:
                self.holes.append(5)
            if 8 not in self.holes:
                self.holes.append(8)
            if self.game.ball_count.position >= 5:
                self.search()
        self.delay(name="display", delay=0.1, handler=graphics.stardust.display, param=self)

    def sw_yellowstar_active(self, sw):
        if self.game.yellow_star.status == True:
            self.game.all_spot.engage(self.game)
            if 2 not in self.holes:
                self.holes.append(2)
            if 15 not in self.holes:
                self.holes.append(15)
            if self.game.ball_count.position >= 5:
                self.search()
        self.delay(name="display", delay=0.1, handler=graphics.stardust.display, param=self)
        

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
        self.game.search_index.disengage()
        self.game.coils.counter.pulse()
        self.game.returned = False
        self.game.sound.stop('add')
        self.game.sound.play('add')
        if self.game.start.status == True:
            if self.game.selector.position < 2:
                self.game.selector.step()
            if self.game.switches.shutter.is_inactive():
                self.game.coils.shutter.enable()
            self.game.cu = not self.game.cu
            self.game.reflex.decrease()
            self.game.spotting.spin()
            self.game.mixer1.spin()
            self.game.mixer2.spin()
            self.game.mixer3.spin()
            self.game.mixer4.spin()
            
            self.replay_step_down()
            self.check_lifter_status()
        else:
            self.holes = []
            self.game.start.engage(self.game)
            self.game.card1_replay_counter.reset()
            self.game.card2_replay_counter.reset()
            self.game.cornerstwo_three.disengage()
            self.game.cornerstwo_four.disengage()
            self.game.cornersone_three.disengage()
            self.game.cornersone_four.disengage()
            self.game.horizontal.reset()
            self.game.special_pocket.disengage()
            self.game.red_star.disengage()
            self.game.yellow_star.disengage()
            self.game.coils.redROLamp.disable()
            self.game.coils.yellowROLamp.disable()
            self.game.odds.reset()
            self.game.roto_feature_step.reset()
            self.game.roto.step()
            self.game.roto2.step()
            graphics.stardust.display(self)
            self.game.roto.step()
            self.game.roto2.step()
            graphics.stardust.display(self)
            self.game.start.engage(self.game)
            self.game.selector.reset()
            self.game.timer.reset()
            self.game.ball_count.reset()
            self.game.extra_ball.reset()
            if self.game.pocket.position == 6:
                self.step_eb(15 - self.game.extra_ball.position)
                self.game.pocket.reset()
            self.game.sound.play_music('motor', -1)
            self.regular_play()

        self.delay(name="display", delay=0.1, handler=graphics.stardust.display, param=self)
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
                else:
                    if self.game.switches.trough4.is_inactive():
                        if self.game.extra_ball.position >= 5 and self.game.ball_count.position <= 5:
                            if self.game.switches.shooter.is_inactive() and self.game.switches.trough3.is_active():
                                self.game.coils.lifter.enable()
                    if self.game.switches.trough3.is_inactive():
                        if self.game.extra_ball.position >= 10 and self.game.ball_count.position <= 6:
                            if self.game.switches.shooter.is_inactive() and self.game.switches.trough2.is_active():
                                self.game.coils.lifter.enable()
                    if self.game.switches.trough2.is_inactive() and self.game.ball_count.position <= 7:
                        if self.game.extra_ball.position >= 15:
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
                if self.game.ball_count.position == 5 and self.game.extra_ball.position >= 5:
                    self.game.coils.lifter.enable()
                if self.game.ball_count.position == 6 and self.game.extra_ball.position >= 10:
                    self.game.coils.lifter.enable()
                if self.game.ball_count.position == 7 and self.game.extra_ball.position >= 15:
                    self.game.coils.lifter.enable()

    def sw_gate_inactive_for_1ms(self, sw):
        self.game.start.disengage()
        self.game.ball_count.step()
        if self.game.switches.shutter.is_active():
            self.game.coils.shutter.enable()
        if self.game.ball_count.position >= 5:
            if self.game.search_index.status == False:
                self.search()
        self.delay(name="display", delay=0.1, handler=graphics.stardust.display, param=self)

    # This is really nasty, but it is how we render graphics for each individual hole.
    # numbers are added (or removed from) a list.  In this way, I can re-use the same
    # routine even for games where there are ball return functions like Surf Club.

    def sw_hole1_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(1)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.stardust.display, param=self)

    def sw_hole2_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(2)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.stardust.display, param=self)

    def sw_hole3_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(3)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.stardust.display, param=self)

    def sw_hole4_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(4)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.stardust.display, param=self)

    def sw_hole5_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(5)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.stardust.display, param=self)

    def sw_hole6_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(6)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.stardust.display, param=self)

    def sw_hole7_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(7)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.stardust.display, param=self)

    def sw_hole8_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(8)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.stardust.display, param=self)

    def sw_hole9_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(9)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.stardust.display, param=self)

    def sw_hole10_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(10)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.stardust.display, param=self)

    def sw_hole11_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(11)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.stardust.display, param=self)

    def sw_hole12_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(12)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.stardust.display, param=self)

    def sw_hole13_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(13)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.stardust.display, param=self)

    def sw_hole14_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(14)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.stardust.display, param=self)

    def sw_hole15_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(15)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.stardust.display, param=self)

    def sw_hole16_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(16)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.stardust.display, param=self)

    def sw_hole17_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(17)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.stardust.display, param=self)

    def sw_hole18_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(18)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.stardust.display, param=self)

    def sw_hole19_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(19)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.stardust.display, param=self)

    def sw_hole20_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(20)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.stardust.display, param=self)

    def sw_hole21_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(21)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.stardust.display, param=self)

    def sw_hole22_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(22)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.stardust.display, param=self)

    def sw_hole23_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(23)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.stardust.display, param=self)

    def sw_hole24_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(24)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            if self.game.special_pocket.status == True:
                self.game.pocket.step()
            self.delay(name="display", delay=0.1, handler=graphics.stardust.display, param=self)

    def sw_hole25_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(25)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.stardust.display, param=self)
    
    def sw_replayReset_active(self, sw):
        self.game.anti_cheat.disengage()
        self.holes = []
#        self.cancel_delayed(name="blink_title")
        graphics.stardust.display(self)
        self.tilt_actions()
#        self.delay(name="blink_title", delay=1, handler=self.blink_title)
        self.replay_step_down(self.game.replays)

    def tilt_actions(self):
        self.game.start.disengage()
        self.cancel_delayed(name="replay_reset")
        self.cancel_delayed(name="card1_replay_step_up")
        self.cancel_delayed(name="card2_replay_step_up")
        self.game.search_index.disengage()
        if self.game.switches.shutter.is_active() and self.game.ball_count.position == 0:
            self.game.coils.shutter.enable()
        self.holes = []
        self.game.selector.reset()
        self.game.extra_ball.reset()
        self.game.cornerstwo_three.disengage()
        self.game.cornerstwo_four.disengage()
        self.game.cornersone_three.disengage()
        self.game.cornersone_four.disengage()
        self.game.horizontal.reset()
        self.game.special_pocket.disengage()
        self.game.red_star.disengage()
        self.game.yellow_star.disengage()
        self.game.roto_feature_step.reset()
        self.game.coils.redROLamp.disable()
        self.game.coils.yellowROLamp.disable()
        self.game.odds.reset()
        self.game.ball_count.reset()
        self.game.anti_cheat.engage(game)
        self.game.tilt.engage(self.game)
        self.game.sound.stop_music()
        self.game.sound.play('tilt')
        # displays "Tilt" on the backglass, you have to recoin.
        self.delay(name="display", delay=0.1, handler=graphics.stardust.display, param=self)

    def sw_tilt_active(self, sw):
        if self.game.tilt.status == False:
            self.tilt_actions()

    def replay_step_down(self, number=0):
        if number > 0:
            if number > 1:
                self.game.replays -= 1
                graphics.replay_step_down(self.game.replays, graphics.stardust.reel1, graphics.stardust.reel10, graphics.stardust.reel100)
                self.game.coils.registerDown.pulse()
                number -= 1
                graphics.stardust.display(self)
                self.delay(name="replay_reset", delay=0.0, handler=self.replay_step_down, param=number)
            elif number == 1:
                self.game.replays -= 1
                graphics.replay_step_down(self.game.replays, graphics.stardust.reel1, graphics.stardust.reel10, graphics.stardust.reel100)
                self.game.coils.registerDown.pulse()
                number -= 1
                graphics.stardust.display(self)
                self.cancel_delayed(name="replay_reset")
        else: 
            if self.game.replays > 0:
                self.game.replays -= 1
                graphics.replay_step_down(self.game.replays, graphics.stardust.reel1, graphics.stardust.reel10, graphics.stardust.reel100)
                self.delay(name="display", delay=0.1, handler=graphics.stardust.display, param=self)
            self.game.coils.registerDown.pulse()

    def replay_step_up(self):
        if self.game.replays < 899:
            self.game.replays += 1
            graphics.replay_step_up(self.game.replays, graphics.stardust.reel1, graphics.stardust.reel10, graphics.stardust.reel100)
        self.game.coils.registerUp.pulse()
        self.game.reflex.increase()
        graphics.stardust.display(self)

    def sw_yellow_active(self, sw):
        if self.game.ball_count.position >= 4:
            if self.game.eb_play.status == False:
                self.game.eb_play.engage(self.game)
                self.delay(name="display", delay=0.1, handler=graphics.stardust.display, param=self)
            if self.game.eb_play.status == True and (self.game.replays > 0 or self.game.switches.freeplay.is_active()):
                self.replay_step_down()
                self.game.sound.stop('add')
                self.game.sound.play('add')
                self.game.cu = not self.game.cu
                self.game.reflex.decrease()
                self.game.spotting.spin()
                self.game.mixer1.spin()
                self.game.mixer2.spin()
                self.game.mixer3.spin()
                self.game.mixer4.spin()
                self.scan_eb()
                self.delay(name="display", delay=0.1, handler=graphics.stardust.display, param=self)
                self.game.eb_play.disengage()
                self.delay(name="display", delay=0.1, handler=graphics.stardust.display, param=self)
  

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
        self.game.sound.play_music('search', -1)
        
        for i in range(0, 50):
            self.r = self.closed_search_relays(self.game.searchdisc.position)
            self.game.searchdisc.spin()
            self.wipers = self.r[0]
            self.card = self.r[1]
            self.corners = self.r[2]
            self.horizontal1 = self.r[3]
            self.horizontal2 = self.r[4]
            self.horizontal3 = self.r[5]
            self.horizontal4 = self.r[6]
            self.horizontal5 = self.r[7]

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
                            if s >= 2:
                                self.find_winner(s, self.card, self.corners, self.horizontal1, self.horizontal2, self.horizontal3, self.horizontal4, self.horizontal5)
                                break
#        self.delay(name="blink_title", delay=3, handler=self.blink_title)

    def find_winner(self, relays, card, corners, horizontal1, horizontal2, horizontal3, horizontal4, horizontal5):
        if self.game.search_index.status == False and self.game.replays < 899:
            if self.game.odds.position == 1:
                threeodds = 4
                fourodds = 16
                fiveodds = 50
            elif self.game.odds.position == 2:
                threeodds = 4
                fourodds = 20
                fiveodds = 75
            elif self.game.odds.position == 3:
                threeodds = 8
                fourodds = 24
                fiveodds = 100
            elif self.game.odds.position == 4:
                threeodds = 12
                fourodds = 32
                fiveodds = 100
            elif self.game.odds.position == 5:
                threeodds = 18
                fourodds = 48
                fiveodds = 150
            elif self.game.odds.position == 6:
                threeodds = 36
                fourodds = 72
                fiveodds = 150
            elif self.game.odds.position == 7:
                threeodds = 48
                fourodds = 96
                fiveodds = 200
            elif self.game.odds.position == 8:
                threeodds = 64
                fourodds = 200
                fiveodds = 300


            if relays == 3:
                if card == 1:
                    if self.game.selector.position >= 1:
                        if corners:
                            if self.game.cornersone_three.status == True:
                                if self.game.card1_replay_counter.position < fourodds:
                                    self.game.search_index.engage(self.game)
                                    self.card1_replay_step_up(fourodds - self.game.card1_replay_counter.position)
                        else:
                            if horizontal1 == True:
                                if self.game.horizontal.position >= 2:
                                    if self.game.card1_replay_counter.position < fourodds:
                                        self.game.search_index.engage(self.game)
                                        self.card1_replay_step_up(fourodds - self.game.card1_replay_counter.position)
                                else:
                                    if self.game.card1_replay_counter.position < threeodds:
                                        self.game.search_index.engage(self.game)
                                        self.card1_replay_step_up(threeodds - self.game.card1_replay_counter.position)
                            elif horizontal2 == True:
                                if self.game.horizontal.position >= 4:
                                    if self.game.card1_replay_counter.position < fourodds:
                                        self.game.search_index.engage(self.game)
                                        self.card1_replay_step_up(fourodds - self.game.card1_replay_counter.position)
                                else:
                                    if self.game.card1_replay_counter.position < threeodds:
                                        self.game.search_index.engage(self.game)
                                        self.card1_replay_step_up(threeodds - self.game.card1_replay_counter.position)
                            elif horizontal3 == True:
                                if self.game.horizontal.position >= 6:
                                    if self.game.card1_replay_counter.position < fourodds:
                                        self.game.search_index.engage(self.game)
                                        self.card1_replay_step_up(fourodds - self.game.card1_replay_counter.position)
                                else:
                                    if self.game.card1_replay_counter.position < threeodds:
                                        self.game.search_index.engage(self.game)
                                        self.card1_replay_step_up(threeodds - self.game.card1_replay_counter.position)
                            elif horizontal4 == True:
                                if self.game.horizontal.position >= 8:
                                    if self.game.card1_replay_counter.position < fourodds:
                                        self.game.search_index.engage(self.game)
                                        self.card1_replay_step_up(fourodds - self.game.card1_replay_counter.position)
                                else:
                                    if self.game.card1_replay_counter.position < threeodds:
                                        self.game.search_index.engage(self.game)
                                        self.card1_replay_step_up(threeodds - self.game.card1_replay_counter.position)
                            elif horizontal5 == True:
                                if self.game.horizontal.position >= 10:
                                    if self.game.card1_replay_counter.position < fourodds:
                                        self.game.search_index.engage(self.game)
                                        self.card1_replay_step_up(fourodds - self.game.card1_replay_counter.position)
                                else:
                                    if self.game.card1_replay_counter.position < threeodds:
                                        self.game.search_index.engage(self.game)
                                        self.card1_replay_step_up(threeodds - self.game.card1_replay_counter.position)
                            else:
                                if self.game.card1_replay_counter.position < threeodds:
                                    self.game.search_index.engage(self.game)
                                    self.card1_replay_step_up(threeodds - self.game.card1_replay_counter.position)
                else:
                    if self.game.selector.position >= 2:
                        if corners:
                            if self.game.cornerstwo_three.status == True:
                                if self.game.card2_replay_counter.position < fourodds:
                                    self.game.search_index.engage(self.game)
                                    self.card2_replay_step_up(fourodds - self.game.card2_replay_counter.position)
                        else:
                            if horizontal1 == True:
                                if self.game.horizontal.position >= 2:
                                    if self.game.card2_replay_counter.position < fourodds:
                                        self.game.search_index.engage(self.game)
                                        self.card2_replay_step_up(fourodds - self.game.card2_replay_counter.position)
                                else:
                                    if self.game.card2_replay_counter.position < threeodds:
                                        self.game.search_index.engage(self.game)
                                        self.card2_replay_step_up(threeodds - self.game.card2_replay_counter.position)
                            elif horizontal2 == True:
                                if self.game.horizontal.position >= 4:
                                    if self.game.card2_replay_counter.position < fourodds:
                                        self.game.search_index.engage(self.game)
                                        self.card2_replay_step_up(fourodds - self.game.card2_replay_counter.position)
                                else:
                                    if self.game.card2_replay_counter.position < threeodds:
                                        self.game.search_index.engage(self.game)
                                        self.card2_replay_step_up(threeodds - self.game.card2_replay_counter.position)
                            elif horizontal3 == True:
                                if self.game.horizontal.position >= 6:
                                    if self.game.card2_replay_counter.position < fourodds:
                                        self.game.search_index.engage(self.game)
                                        self.card2_replay_step_up(fourodds - self.game.card2_replay_counter.position)
                                else:
                                    if self.game.card2_replay_counter.position < threeodds:
                                        self.game.search_index.engage(self.game)
                                        self.card2_replay_step_up(threeodds - self.game.card2_replay_counter.position)
                            elif horizontal4 == True:
                                if self.game.horizontal.position >= 8:
                                    if self.game.card2_replay_counter.position < fourodds:
                                        self.game.search_index.engage(self.game)
                                        self.card2_replay_step_up(fourodds - self.game.card2_replay_counter.position)
                                else:
                                    if self.game.card2_replay_counter.position < threeodds:
                                        self.game.search_index.engage(self.game)
                                        self.card2_replay_step_up(threeodds - self.game.card2_replay_counter.position)
                            elif horizontal5 == True:
                                if self.game.horizontal.position >= 10:
                                    if self.game.card2_replay_counter.position < fourodds:
                                        self.game.search_index.engage(self.game)
                                        self.card2_replay_step_up(fourodds - self.game.card2_replay_counter.position)
                                else:
                                    if self.game.card2_replay_counter.position < threeodds:
                                        self.game.search_index.engage(self.game)
                                        self.card2_replay_step_up(threeodds - self.game.card2_replay_counter.position)
                            else:
                                if self.game.card2_replay_counter.position < threeodds:
                                    self.game.search_index.engage(self.game)
                                    self.card2_replay_step_up(threeodds - self.game.card2_replay_counter.position)
            if relays == 4:
                if card == 1:
                    if self.game.selector.position >= 1:
                        if corners:
                            if self.game.cornersone_four.status == True:
                                if self.game.card1_replay_counter.position < fiveodds:
                                    self.game.search_index.engage(self.game)
                                    self.card1_replay_step_up(fiveodds - self.game.card1_replay_counter.position)
                        else:
                            if horizontal1 == True:
                                if self.game.horizontal.position >= 2:
                                    if self.game.card1_replay_counter.position < fiveodds:
                                        self.game.search_index.engage(self.game)
                                        self.card1_replay_step_up(fiveodds - self.game.card1_replay_counter.position)
                                else:
                                    if self.game.card1_replay_counter.position < fourodds:
                                        self.game.search_index.engage(self.game)
                                        self.card1_replay_step_up(fourodds - self.game.card1_replay_counter.position)
                            elif horizontal2 == True:
                                if self.game.horizontal.position >= 4:
                                    if self.game.card1_replay_counter.position < fiveodds:
                                        self.game.search_index.engage(self.game)
                                        self.card1_replay_step_up(fiveodds - self.game.card1_replay_counter.position)
                                else:
                                    if self.game.card1_replay_counter.position < fourodds:
                                        self.game.search_index.engage(self.game)
                                        self.card1_replay_step_up(fourodds - self.game.card1_replay_counter.position)
                            elif horizontal3 == True:
                                if self.game.horizontal.position >= 6:
                                    if self.game.card1_replay_counter.position < fiveodds:
                                        self.game.search_index.engage(self.game)
                                        self.card1_replay_step_up(fiveodds - self.game.card1_replay_counter.position)
                                else:
                                    if self.game.card1_replay_counter.position < fourodds:
                                        self.game.search_index.engage(self.game)
                                        self.card1_replay_step_up(fourodds - self.game.card1_replay_counter.position)
                            elif horizontal4 == True:
                                if self.game.horizontal.position >= 8:
                                    if self.game.card1_replay_counter.position < fiveodds:
                                        self.game.search_index.engage(self.game)
                                        self.card1_replay_step_up(fiveodds - self.game.card1_replay_counter.position)
                                else:
                                    if self.game.card1_replay_counter.position < fourodds:
                                        self.game.search_index.engage(self.game)
                                        self.card1_replay_step_up(fourodds - self.game.card1_replay_counter.position)
                            elif horizontal5 == True:
                                if self.game.horizontal.position >= 10:
                                    if self.game.card1_replay_counter.position < fiveodds:
                                        self.game.search_index.engage(self.game)
                                        self.card1_replay_step_up(fiveodds - self.game.card1_replay_counter.position)
                                else:
                                    if self.game.card1_replay_counter.position < fourodds:
                                        self.game.search_index.engage(self.game)
                                        self.card1_replay_step_up(fourodds - self.game.card1_replay_counter.position)
                            else:
                                if self.game.card1_replay_counter.position < fourodds:
                                    self.game.search_index.engage(self.game)
                                    self.card1_replay_step_up(fourodds - self.game.card1_replay_counter.position)
                else:
                    if self.game.selector.position >= 2:
                        if corners:
                            if self.game.cornerstwo_four.status == True:
                                if self.game.card2_replay_counter.position < fiveodds:
                                    self.game.search_index.engage(self.game)
                                    self.card2_replay_step_up(fiveodds - self.game.card2_replay_counter.position)
                        else:
                            if horizontal1 == True:
                                if self.game.horizontal.position >= 2:
                                    if self.game.card2_replay_counter.position < fiveodds:
                                        self.game.search_index.engage(self.game)
                                        self.card2_replay_step_up(fiveodds - self.game.card2_replay_counter.position)
                                else:
                                    if self.game.card2_replay_counter.position < fourodds:
                                        self.game.search_index.engage(self.game)
                                        self.card2_replay_step_up(fourodds - self.game.card2_replay_counter.position)
                            elif horizontal2 == True:
                                if self.game.horizontal.position >= 4:
                                    if self.game.card2_replay_counter.position < fiveodds:
                                        self.game.search_index.engage(self.game)
                                        self.card2_replay_step_up(fiveodds - self.game.card2_replay_counter.position)
                                else:
                                    if self.game.card2_replay_counter.position < fourodds:
                                        self.game.search_index.engage(self.game)
                                        self.card2_replay_step_up(fourodds - self.game.card2_replay_counter.position)
                            elif horizontal3 == True:
                                if self.game.horizontal.position >= 6:
                                    if self.game.card2_replay_counter.position < fiveodds:
                                        self.game.search_index.engage(self.game)
                                        self.card2_replay_step_up(fiveodds - self.game.card2_replay_counter.position)
                                else:
                                    if self.game.card2_replay_counter.position < fourodds:
                                        self.game.search_index.engage(self.game)
                                        self.card2_replay_step_up(fourodds - self.game.card2_replay_counter.position)
                            elif horizontal4 == True:
                                if self.game.horizontal.position >= 8:
                                    if self.game.card2_replay_counter.position < fiveodds:
                                        self.game.search_index.engage(self.game)
                                        self.card2_replay_step_up(fiveodds - self.game.card2_replay_counter.position)
                                else:
                                    if self.game.card2_replay_counter.position < fourodds:
                                        self.game.search_index.engage(self.game)
                                        self.card2_replay_step_up(fourodds - self.game.card2_replay_counter.position)
                            elif horizontal5 == True:
                                if self.game.horizontal.position >= 10:
                                    if self.game.card2_replay_counter.position < fiveodds:
                                        self.game.search_index.engage(self.game)
                                        self.card2_replay_step_up(fiveodds - self.game.card2_replay_counter.position)
                                else:
                                    if self.game.card2_replay_counter.position < fourodds:
                                        self.game.search_index.engage(self.game)
                                        self.card2_replay_step_up(fourodds - self.game.card2_replay_counter.position)
                            else:
                                if self.game.card2_replay_counter.position < fourodds:
                                    self.game.search_index.engage(self.game)
                                    self.card2_replay_step_up(fourodds - self.game.card2_replay_counter.position)
            if relays == 5:
                if card == 1:
                    if self.game.selector.position >= 1:
                        if self.game.card1_replay_counter.position < fiveodds:
                            self.game.search_index.engage(self.game)
                            self.card1_replay_step_up(fiveodds - self.game.card1_replay_counter.position)
                else:
                    if self.game.selector.position >= 2:
                        if self.game.card2_replay_counter.position < fiveodds:
                            self.game.search_index.engage(self.game)
                            self.card2_replay_step_up(fiveodds - self.game.card2_replay_counter.position)
                
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

    def closed_search_relays(self, rivets):
        # This function is critical, as it will determine which card is returned, etc.  I need to check the position of the
        # replay counter for the card. We will get a row back
        # that has the numbers on the position which will return the search relay connected.  When three out of the five relays
        # are connected, we get a winner!

        if self.game.roto.position == 0:
            self.q2 = 21
            self.q3 = 13
            self.q4 = 22
            self.r2 = 12
            self.r4 = 18
            self.s2 = 20
            self.s3 = 14
            self.s4 = 19
        elif self.game.roto.position == 1:
            self.q2 = 12
            self.q3 = 21
            self.q4 = 13
            self.r2 = 20
            self.r4 = 22
            self.s2 = 14
            self.s3 = 19
            self.s4 = 18
        elif self.game.roto.position == 2:
            self.q2 = 20
            self.q3 = 12
            self.q4 = 21
            self.r2 = 14
            self.r4 = 13
            self.s2 = 19
            self.s3 = 18
            self.s4 = 22
        elif self.game.roto.position == 3:
            self.q2 = 14
            self.q3 = 20
            self.q4 = 12
            self.r2 = 19
            self.r4 = 21
            self.s2 = 18
            self.s3 = 22
            self.s4 = 13
        elif self.game.roto.position == 4:
            self.q2 = 19
            self.q3 = 14
            self.q4 = 20
            self.r2 = 18
            self.r4 = 12
            self.s2 = 22
            self.s3 = 13
            self.s4 = 21
        elif self.game.roto.position == 5:
            self.q2 = 18
            self.q3 = 19
            self.q4 = 14
            self.r2 = 22
            self.r4 = 20
            self.s2 = 13
            self.s3 = 21
            self.s4 = 12
        elif self.game.roto.position == 6:
            self.q2 = 22
            self.q3 = 18
            self.q4 = 19
            self.r2 = 13
            self.r4 = 14
            self.s2 = 21
            self.s3 = 12
            self.s4 = 20
        elif self.game.roto.position == 7:
            self.q2 = 13
            self.q3 = 22
            self.q4 = 18
            self.r2 = 21
            self.r4 = 19
            self.s2 = 12
            self.s3 = 20
            self.s4 = 14

        if self.game.roto2.position == 0:
            self.q22 = 5
            self.q23 = 17
            self.q24 = 11
            self.r22 = 19
            self.r24 = 23
            self.s22 = 10
            self.s23 = 16
            self.s24 = 18
        elif self.game.roto2.position == 1:
            self.q22 = 19
            self.q23 = 5
            self.q24 = 17
            self.r22 = 10
            self.r24 = 11
            self.s22 = 16
            self.s23 = 18
            self.s24 = 23
        elif self.game.roto2.position == 2:
            self.q22 = 10
            self.q23 = 19
            self.q24 = 5
            self.r22 = 16
            self.r24 = 17
            self.s22 = 18
            self.s23 = 23
            self.s24 = 11
        elif self.game.roto2.position == 3:
            self.q22 = 16
            self.q23 = 10
            self.q24 = 19
            self.r22 = 18
            self.r24 = 5
            self.s22 = 23
            self.s23 = 11
            self.s24 = 17
        elif self.game.roto2.position == 4:
            self.q22 = 18
            self.q23 = 16
            self.q24 = 10
            self.r22 = 23
            self.r24 = 19
            self.s22 = 11
            self.s23 = 17
            self.s24 = 5
        elif self.game.roto2.position == 5:
            self.q22 = 23
            self.q23 = 18
            self.q24 = 16
            self.r22 = 11
            self.r24 = 10
            self.s22 = 17
            self.s23 = 5
            self.s24 = 19
        elif self.game.roto2.position == 6:
            self.q22 = 11
            self.q23 = 23
            self.q24 = 18
            self.r22 = 17
            self.r24 = 16
            self.s22 = 5
            self.s23 = 19
            self.s24 = 10
        elif self.game.roto2.position == 7:
            self.q22 = 17
            self.q23 = 11
            self.q24 = 23
            self.r22 = 5
            self.r24 = 18
            self.s22 = 19
            self.s23 = 10
            self.s24 = 16

        self.pos = {}
        self.pos[0] = {}
        self.pos[1] = {14:1, 1:2, 9:3, 25:4, 3:5}
        self.pos[2] = {8:1, self.q22:2, self.q23:3, self.q24:4, 20:5}
        self.pos[3] = {6:1, self.r22:2, 22:3, self.r24:4, 7:5}
        self.pos[4] = {24:1, self.s22:2, self.s23:3, self.s24:4, 13:5}
        self.pos[5] = {12:1, 21:2, 2:3, 15:4, 4:5}
        self.pos[6] = {14:1, 8:2, 6:3, 24:4, 12:5}
        self.pos[7] = {1:1, self.q22:2, self.r22:3, self.s22:4, 21:5}
        self.pos[8] = {9:1, self.q23:2, 22:3, self.s23:4, 2:5}
        self.pos[9] = {25:1, self.q24:2, self.r24:3, self.s24:4, 15:5}
        self.pos[10] = {3:1, 20:2, 7:3, 13:4, 4:5}
        self.pos[11] = {14:1, self.q22:2, 22:3, self.s24:4, 4:5}
        self.pos[12] = {3:1, self.q24:2, 22:3, self.s22:4, 12:5}
        self.pos[13] = {}
        self.pos[14] = {14:1, 3:2, 12:3, 4:4}
        self.pos[15] = {3:1, 12:2, 4:3, 14:4}
        self.pos[16] = {}
        self.pos[17] = {}
        self.pos[18] = {}
        self.pos[19] = {}
        self.pos[20] = {}
        self.pos[21] = {}
        self.pos[22] = {}
        self.pos[23] = {}
        self.pos[24] = {}
        self.pos[25] = {9:1, 4:2, 15:3, 24:4, 6:5}
        self.pos[26] = {10:1, self.q2:2, self.q3:3, self.q4:4, 8:5}
        self.pos[27] = {2:1, self.r2:2, 16:3, self.r4:4, 25:5}
        self.pos[28] = {1:1, self.s2:2, self.s3:3, self.s4:4, 17:5}
        self.pos[29] = {11:1, 7:2, 5:3, 23:4, 3:5}
        self.pos[30] = {9:1, 10:2, 2:3, 1:4, 11:5}
        self.pos[31] = {4:1, self.q2:2, self.r2:3, self.s2:4, 7:5}
        self.pos[32] = {15:1, self.q3:2, 16:3, self.s3:4, 5:5}
        self.pos[33] = {24:1, self.q4:2, self.r4:3, self.s4:4, 23:5}
        self.pos[34] = {6:1, 8:2, 25:3, 17:4, 3:5}
        self.pos[35] = {9:1, self.q2:2, 16:3, self.s4:4, 3:5}
        self.pos[36] = {6:1, self.q4:2, 16:3, self.s2:4, 11:5}
        self.pos[37] = {}
        self.pos[38] = {9:1, 6:2, 3:3, 11:4}
        self.pos[39] = {6:1, 3:2, 11:3, 9:4}
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
        horizontal1 = False
        horizontal2 = False
        horizontal3 = False
        horizontal4 = False
        horizontal5 = False
        card = 0

        if rivets in range(25,50):
            card = 1
            if rivets == 38 or rivets == 39:
                corners = True
            if rivets == 25:
                horizontal1 = True
            if rivets == 26:
                horizontal2 = True
            if rivets == 27:
                horizontal3 = True
            if rivets == 28:
                horizontal4 = True
            if rivets == 29:
                horizontal5 = True
        else:
            card = 2
            if rivets == 14 or rivets == 15:
                corners = True
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

        return (self.pos[rivets], card, corners, horizontal1, horizontal2, horizontal3, horizontal4, horizontal5)
       
    
    def blink_title(self):
        title1 = random.randint(0,1)
        title2 = random.randint(0,1)
        title3 = random.randint(0,1)
        if title1 == 1:
            pos = [284,249]
            image = pygame.image.load('stardust/assets/title1_on.png').convert_alpha()
            screen.blit(image, pos)
        if title2 == 1:
            pos = [229,275]
            image = pygame.image.load('stardust/assets/title2_on.png').convert_alpha()
            screen.blit(image, pos)
        if title3 == 1:
            pos = [347,272]
            image = pygame.image.load('stardust/assets/title3_on.png').convert_alpha()
            screen.blit(image, pos)
        
        pygame.display.update()
        self.delay(name="display", delay=0.1, handler=graphics.stardust.display, param=self)
#        self.delay(name="blink_title", delay=3, handler=self.blink_title)

    
    def scan_all(self):
        #Animate scanning of everything - this happens through the flash disc
        if self.game.odds.position < 1:
            self.game.odds.step()
            self.delay(name="display", delay=0, handler=graphics.stardust.display, param=self)
        else:
            if self.game.odds.position < 2:
                self.game.odds.step()
            self.all_probability()
            s = random.randint(1,5)
            self.animate_feature_scan(s)
            self.delay(name="display", delay=0, handler=graphics.stardust.display, param=self)

    def all_probability(self):
        mix1 = self.game.mixer1.position
        if self.game.reflex.connected_rivet() == 0:
            #Worst position for reflex - requires mixer1 to be in the three liberal positions for the connection of the wires bypassing the reflex.
            if (mix1 == 1 or mix1 == 3):
                self.scan_odds()
        if self.game.reflex.connected_rivet() == 1 and (mix1 == 1 or mix1 == 3 or mix1 == 21):
            self.scan_odds()
        elif self.game.reflex.connected_rivet() == 2 and (mix1 == 1 or mix1 == 3 or mix1 == 21 or mix1 == 6):
            self.scan_odds()
        elif self.game.reflex.connected_rivet() == 3 and (mix1 == 1 or mix1 == 3 or mix1 == 21 or mix1 == 6 or mix1 == 20):
            self.scan_odds()
        elif self.game.reflex.connected_rivet() == 4 and (mix1 == 1 or mix1 == 3 or mix1 == 21 or mix1 == 6 or mix1 == 20 or mix1 == 5):
            self.scan_odds()
        elif self.game.reflex.connected_rivet() == 5:
            self.scan_odds()
        else:
            s = random.randint(1,8)
            self.animate_odds_scan(s)
            s = random.randint(1,4)
            self.animate_feature_scan(s)

    def check_extra_step(self):
        i = random.randint(0,32)
        if i == 16:
            return 1
        else:
            return 0

    def scan_odds(self):
        m2 = self.game.mixer2.position
        s = random.randint(1,8)
        self.animate_odds_scan(s)
        if self.game.odds.position < 3:
            o = self.odds_probability()
            if o == 1:
                es = self.check_extra_step()
                if es == 1:
                    i = random.randint(1,6)
                    self.step_odds(i)
                else:
                    self.game.odds.step()
            self.features_probability()
        elif m2 == 17:
            o = self.odds_probability()
            if o == 1:
                es = self.check_extra_step()
                if es == 1:
                    i = random.randint(1,6)
                    self.step_odds(i)
                else:
                    self.game.odds.step()
            self.features_probability()
        elif self.game.odds.position ==  3:
            if m2 == 5 or m2 == 15:
                o = self.odds_probability()
                if o == 1:
                    es = self.check_extra_step()
                    if es == 1:
                        i = random.randint(1,6)
                        self.step_odds(i)
                    else:
                        self.game.odds.step()
                self.features_probability()
            elif self.game.cu:
                if m2 == 9:
                    o = self.odds_probability()
                    if o == 1:
                        es = self.check_extra_step()
                        if es == 1:
                            i = random.randint(1,6)
                            self.step_odds(i)
                        else:
                            self.game.odds.step()
                    self.features_probability()
        else:
            self.features_probability()

    def features_probability(self):
        sd = self.game.spotting.position
        if sd == 45:
            self.game.red_star.engage(self.game)
            self.game.yellow_star.engage(self.game)
            self.game.coils.redROLamp.enable()
            self.game.coils.yellowROLamp.enable()
        if sd == 4:
            self.game.cornersone_four.engage(self.game)
        if sd == 47:
            self.game.cornersone_three.engage(self.game)
        if sd == 0 or sd == 25:
            self.step_horizontal(1)
        if sd == 1 or sd == 26:
            self.step_horizontal(10)
        if sd == 24:
            self.game.cornerstwo_three.engage(self.game)
        if sd == 9:
            self.game.cornerstwo_four.engage(self.game)
        if sd == 18:
            self.game.special_pocket.engage(self.game)
            if self.game.roto_feature_step.position < 5:
                if self.game.roto_feature_step.position < 4:
                    self.step_roto(4 - self.game.roto_feature_step.position)
                else:
                    self.step_roto(1)
            else:
                self.step_roto(1)
        if self.game.mixer1.position == 1:
            self.step_roto(2)
        
    def odds_probability(self):
        m3 = self.game.mixer3.position
        if m3 == 2 or m3 == 1:
            return 1
        if m3 == 8 or m3 == 15 or m3 == 5:
            return 1
        if m3 == 11:
            return 1
        if m3 == 4:
            return 1
        
    def eb_probability(self):
        mix1 = self.game.mixer1.connected_rivet()
        if self.game.reflex.connected_rivet() == 0:
            #Worst position for reflex - requires mixer1 to be in the three liberal positions for the connection of the wires bypassing the reflex.
            if (mix1 == 1 or mix1 == 3):
                if self.game.mixer4.position == 1 or self.game.mixer4.position == 3 or self.game.mixer4.position == 4:
                    self.game.extra_ball.step()
                if self.game.spotting.position == 25 and self.game.mixer1.position == 4:
                    self.step_eb(15 - self.game.extra_ball.position)
                if self.game.spotting.position == 8:
                    self.step_eb(10 - self.game.extra_ball.position)
                if self.game.spotting.position == 0:
                    self.step_eb(5 - self.game.extra_ball.position)
        elif self.game.reflex.connected_rivet() == 1 and (mix1 == 1 or mix1 == 3 or mix1 == 21):
            if self.game.mixer4.position == 1 or self.game.mixer4.position == 3 or self.game.mixer4.position == 4:
                self.game.extra_ball.step()
            if self.game.spotting.position == 25 and self.game.mixer1.position == 4:
                self.step_eb(15 - self.game.extra_ball.position)
            if self.game.spotting.position == 8:
                self.step_eb(10 - self.game.extra_ball.position)
            if self.game.spotting.position == 0:
                self.step_eb(5 - self.game.extra_ball.position)
        elif self.game.reflex.connected_rivet() == 2 and (mix1 == 1 or mix1 == 3 or mix1 == 21 or mix1 == 6):
            if self.game.mixer4.position == 1 or self.game.mixer4.position == 3 or self.game.mixer4.position == 4:
                self.game.extra_ball.step()
            if self.game.spotting.position == 25 and self.game.mixer1.position == 4:
                self.step_eb(15 - self.game.extra_ball.position)
            if self.game.spotting.position == 8:
                self.step_eb(10 - self.game.extra_ball.position)
            if self.game.spotting.position == 0:
                self.step_eb(5 - self.game.extra_ball.position)
        elif self.game.reflex.connected_rivet() == 3 and (mix1 == 1 or mix1 == 3 or mix1 == 21 or mix1 == 6 or mix1 == 20):
            if self.game.mixer4.position == 1 or self.game.mixer4.position == 3 or self.game.mixer4.position == 4:
                self.game.extra_ball.step()
            if self.game.spotting.position == 25 and self.game.mixer1.position == 4:
                self.step_eb(15 - self.game.extra_ball.position)
            if self.game.spotting.position == 8:
                self.step_eb(10 - self.game.extra_ball.position)
            if self.game.spotting.position == 0:
                self.step_eb(5 - self.game.extra_ball.position)
        elif self.game.reflex.connected_rivet() == 4 and (mix1 == 1 or mix1 == 3 or mix1 == 21 or mix1 == 6 or mix1 == 20 or mix1 == 5):
            if self.game.mixer4.position == 1 or self.game.mixer4.position == 3 or self.game.mixer4.position == 4:
                self.game.extra_ball.step()
            if self.game.spotting.position == 25 and self.game.mixer1.position == 4:
                self.step_eb(15 - self.game.extra_ball.position)
            if self.game.spotting.position == 8:
                self.step_eb(10 - self.game.extra_ball.position)
            if self.game.spotting.position == 0:
                self.step_eb(5 - self.game.extra_ball.position)
        elif self.game.reflex.connected_rivet() == 5:
            if self.game.mixer4.position == 1 or self.game.mixer4.position == 3 or self.game.mixer4.position == 4:
                self.game.extra_ball.step()
            if self.game.spotting.position == 25 and self.game.mixer1.position == 4:
                self.step_eb(15 - self.game.extra_ball.position)
            if self.game.spotting.position == 8:
                self.step_eb(10 - self.game.extra_ball.position)
            if self.game.spotting.position == 0:
                self.step_eb(5 - self.game.extra_ball.position)
        
            
        self.check_lifter_status()
        self.delay(name="display", delay=0, handler=graphics.stardust.display, param=self)
            
    def step_eb(self, number):
        if number > 0:
            number -= 1
            self.game.extra_ball.step()
            self.delay(name="display", delay=0, handler=graphics.stardust.display, param=self)
            self.check_lifter_status()
            self.delay(name="step_eb", delay=0.1, handler=self.step_eb, param=number)
            if self.game.extra_ball.position >= 9:
                self.check_lifter_status()

    def step_odds(self, number):
        if number > 0:
            number -= 1
            self.game.odds.step()
            self.delay(name="display", delay=0, handler=graphics.stardust.display, param=self)
            self.check_lifter_status()
            self.delay(name="step_odds", delay=0.1, handler=self.step_odds, param=number)
        else:
            self.search()

    def step_roto(self, number):
        if number > 0:
            number -= 1
            self.game.roto_feature_step.step()
            if self.game.roto_feature_step.position == 5:
                self.holes.append(18)
            self.delay(name="display", delay=0, handler=graphics.stardust.display, param=self)
            self.delay(name="step_roto", delay=0.1, handler=self.step_roto, param=number)

    def step_horizontal(self, number):
        if number > 0:
            number -= 1
            self.game.horizontal.step()
            if self.game.horizontal.position < 4:
                number = 4 - self.game.horizontal.position
            self.delay(name="display", delay=0, handler=graphics.stardust.display, param=self)
            self.delay(name="step_horizontal", delay=0.1, handler=self.step_horizontal, param=number)

    def scan_eb(self):
        if self.game.eb_play.status == True:
            s = random.randint(1,9)
            self.animate_eb_scan(s)
            self.eb_probability()
            # Timer resets to 0 position on ball count increasing.  We are fudging this since we will have
            # no good way to measure balls as they return back to the trough.  The ball count unit cannot be
            # relied upon as we do not have a switch in the outhole, and the trough logic is too complex for
            # the task at hand.
            # TODO: implement thunk noises into the units.py to automatically play the noises.
            self.game.timer.reset()
        else:
            # TODO: play thunk noise of EB search bearing no fruit.
            pass
        self.delay(name="display", delay=0.1, handler=graphics.stardust.display, param=self)

    def animate_feature_scan(self, s):
        if s > 1:
            self.delay(name="feature_animation", delay=0.1, handler=graphics.stardust.feature_animation, param=s)
            self.delay(name="display", delay=0.1, handler=graphics.stardust.display, param=self)
            s -= 1
            #self.delay(name="animate_feature", delay=0.1, handler=self.animate_feature_scan, param=s)
        else:
            self.cancel_delayed(name="feature_animation")
            self.cancel_delayed(name="display")

    def animate_odds_scan(self, s):
        if s > 1:
            self.delay(name="odds_animation", delay=0.1, handler=graphics.stardust.odds_animation, param=s)
            self.delay(name="display", delay=0.1, handler=graphics.stardust.display, param=self)
            s -= 1
            #self.delay(name="animate_odds", delay=0.1, handler=self.animate_odds_scan, param=s)
        else:
            self.cancel_delayed(name="odds_animation")
            self.cancel_delayed(name="display")

    def animate_eb_scan(self, s):
        if s > 1:
            self.delay(name="eb_animation", delay=0.1, handler=graphics.stardust.eb_animation, param=s)
            self.delay(name="display", delay=0.1, handler=graphics.stardust.display, param=self)
            s -= 1
            #self.delay(name="animate_eb", delay=0.1, handler=self.animate_eb_scan, param=s)
        else:
            self.cancel_delayed(name="eb_animation")
            self.cancel_delayed(name="display")


    # Define reset as the knock-off, anti-cheat relay disabled, and replay reset enabled.  Motors turn while credits are knocked off.
    # When meter reaches zero and the zero limit switch is hit, turn off motor sound and leave backglass gi on, but with tilt displayed.

    def startup(self):        
        # Every bingo requires the meter to register '0' 
        # before allowing coin entry --
        # also needs to show a plain 'off' backglass.
        self.eb = False
        self.tilt_actions()
#        self.delay(name="blink_title", delay=1, handler=self.blink_title)


class Stardust(procgame.game.BasicGame):
    def __init__(self, machine_type):
        super(Stardust, self).__init__(machine_type)
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

        self.roto_feature_step = units.Stepper("roto_feature_step", 6)
        self.roto = units.Stepper("roto", 7, 'stardust', "continuous")
        self.roto2 = units.Stepper("roto2", 7, 'stardust', "continuous")

        #Odds stepper
        self.odds = units.Stepper("odds", 8, 'stardust')
        
        #Replay Counter
        self.card1_replay_counter = units.Stepper("card1_replay_counter", 300)
        self.card2_replay_counter = units.Stepper("card2_replay_counter", 300)
 
        #Initialize stepper units used to keep track of features or timing.
        self.timer = units.Stepper("timer", 40)
        self.ball_count = units.Stepper("ball_count", 8)

        # Initialize reflex(es) and mixers unique to this game
        self.reflex = units.Reflex("primary", 100)

        #In United games, they call this spotting motor the 'flash' motor, 
        #similar to the ball bowlers.
        self.spotting = units.Spotting("spotting", 49)

        #Check for status of the replay register zero switch.  If positive
        #and machine is just powered on, this will zero out the replays.
        self.replay_reset = units.Relay("replay_reset")
        
        #Extra ball unit contains 15 positions.  Max of 3 EBs.
        self.extra_ball = units.Stepper("extra_ball", 15)


        #When engage()d, light 6v circuit, and enable game features, scoring,
        #etc. Disengage()d means that the machine is 'soft' tilted. In United
        #games, they call this the lock relay, similar to many other pin
        #manufacturers.
        self.lock = units.Relay("lock")

        self.eb_play = units.Relay("eb_play")
        
        #Relay for corners lighting
        self.cornersone_three = units.Relay("cornersone_three")
        self.cornersone_four = units.Relay("cornersone_four")
        self.cornerstwo_three = units.Relay("cornerstwo_three")
        self.cornerstwo_four = units.Relay("cornerstwo_four")

        #Selector keeps track of cards in play - in United games, they call
        #this the card step-up, but I'll call it selector for consistency with other
        self.selector = units.Stepper("selector", 2)

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

        #Some special trip relays for spotted numbers and rollovers
        self.red_star = units.Relay("red_star")
        self.yellow_star = units.Relay("yellow_star")

        self.all_spot = units.Relay("all_spot")

        self.special_pocket = units.Relay("special_pocket")
        self.pocket = units.Stepper("pocket", 6)

        self.horizontal = units.Stepper("horizontal", 10)

        self.anti_cheat = units.Relay("anti_cheat")

        self.replays = 0
        self.returned = False

    def reset(self):
        super(Stardust, self).reset()
        self.logger = logging.getLogger('game')
        self.load_config('bingo.yaml')
        self.lock.engage(game)
        
        main_mode = MulticardBingo(self)
        self.modes.add(main_mode)
        

game = Stardust(machine_type='pdb')
game.reset()
game.run_loop()
