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
from bingo_emulator.graphics.yacht_club import *

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

        self.delay(name="display", delay=0.1, handler=graphics.yacht_club.display, param=self)

    def sw_startButton_active(self, sw):
        self.game.eb_play.disengage()
        if self.game.replays > 0 or self.game.switches.freeplay.is_active():
            self.game.sound.stop('add')
            self.game.sound.play('add')
            self.game.tilt.disengage()
            self.regular_play()
            self.scan_all()
            self.delay(name="display", delay=0.1, handler=graphics.yacht_club.display, param=self)

    def sw_enter_active(self, sw):
        if self.game.switches.left.is_active() and self.game.switches.right.is_active():
            self.game.end_run_loop()
            os.system("/home/nbaldridge/proc/bingo_emulator/start_game.sh yacht_club")

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
        max_ball = 4
        max_card = 0

        if self.game.select_card.position == 6:
            max_card = 3
        elif self.game.select_card.position == 7:
            max_card = 4
        elif self.game.select_card.position == 8:
            max_card = 5

        if self.game.ball_count.position < max_ball:
            self.game.card.stepdown()
                        
        self.delay(name="display", delay=0.1, handler=graphics.yacht_club.display, param=self)

    def sw_right_active(self, sw):
        max_ball = 4
        max_card = 0

        if self.game.select_card.position == 6:
            max_card = 3
        elif self.game.select_card.position == 7:
            max_card = 4
        elif self.game.select_card.position == 8:
            max_card = 5

        if self.game.ball_count.position < max_ball:
            if self.game.card.position + 1 < max_card:
                self.game.card.step()
                        
        self.delay(name="display", delay=0.1, handler=graphics.yacht_club.display, param=self)

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

        self.game.cu = not self.game.cu
        self.game.spotting.spin()
        self.game.mixer1.spin()
        self.game.mixer2.spin()
        self.game.mixer3.spin()
        self.game.mixer4.spin()
        self.game.reflex.decrease()

        self.game.returned = False
        if self.game.start.status == True:
            if self.game.selector.position < 3:
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
            self.game.card1_replay_counter.reset()
            self.game.super_card.reset()
            self.game.select_card.reset()
            self.game.yellow_star.disengage()
            self.game.red_star.disengage()
            self.game.start.engage(self.game)
            self.game.selector.reset()
            self.game.ball_count.reset()
            self.game.extra_ball.reset()
            self.game.odds.reset()
            self.game.card.reset()
            self.game.timer.reset()
            self.game.sound.play_music('motor', -1)
            self.regular_play()
        self.delay(name="display", delay=0.1, handler=graphics.yacht_club.display, param=self)
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
                        if self.game.extra_ball.position >= 7 and self.game.ball_count.position <= 5:
                            if self.game.switches.shooter.is_inactive() and self.game.switches.trough3.is_active():
                                self.game.coils.lifter.enable()
                    if self.game.switches.trough3.is_inactive():
                        if self.game.extra_ball.position >= 14 and self.game.ball_count.position <= 6:
                            if self.game.switches.shooter.is_inactive() and self.game.switches.trough2.is_active():
                                self.game.coils.lifter.enable()
                    if self.game.switches.trough2.is_inactive() and self.game.ball_count.position <= 7:
                        if self.game.ball_count.position <= 7:
                            if self.game.extra_ball.position >= 21:
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
                elif self.game.ball_count.position == 5 and self.game.extra_ball.position >= 7:
                    self.game.coils.lifter.enable()
                elif self.game.ball_count.position == 6 and self.game.extra_ball.position >= 14:
                    self.game.coils.lifter.enable()
                else:
                    if self.game.ball_count.position == 7 and self.game.extra_ball.position >= 21:
                        self.game.coils.lifter.enable()

    def sw_gate_inactive_for_1ms(self, sw):
        self.game.start.disengage()
        self.game.ball_count.step()
        if self.game.switches.shutter.is_active():
            self.game.coils.shutter.enable()
        if self.game.ball_count.position >= 4:
            if self.game.search_index.status == False:
                self.search()
        if self.game.ball_count.position > 5:
            self.game.coils.yellowROLamp.disable()
            self.game.coils.redROLamp.disable()
        self.delay(name="display", delay=0.1, handler=graphics.yacht_club.display, param=self)


    # This is really nasty, but it is how we render graphics for each individual hole.
    # numbers are added (or removed from) a list.  In this way, I can re-use the same
    # routine even for games where there are ball return functions like Surf Club.

    def sw_hole1_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(1)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.yacht_club.display, param=self)

    def sw_hole2_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(2)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.yacht_club.display, param=self)

    def sw_hole3_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(3)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.yacht_club.display, param=self)

    def sw_hole4_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(4)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.yacht_club.display, param=self)

    def sw_hole5_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(5)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.yacht_club.display, param=self)

    def sw_hole6_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(6)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.yacht_club.display, param=self)

    def sw_hole7_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(7)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.yacht_club.display, param=self)

    def sw_hole8_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(8)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.yacht_club.display, param=self)

    def sw_hole9_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(9)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.yacht_club.display, param=self)

    def sw_hole10_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(10)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.yacht_club.display, param=self)

    def sw_hole11_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(11)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.yacht_club.display, param=self)

    def sw_hole12_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(12)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.yacht_club.display, param=self)

    def sw_hole13_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(13)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.yacht_club.display, param=self)

    def sw_hole14_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(14)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.yacht_club.display, param=self)

    def sw_hole15_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(15)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.yacht_club.display, param=self)

    def sw_hole16_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(16)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.yacht_club.display, param=self)

    def sw_hole17_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(17)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.yacht_club.display, param=self)

    def sw_hole18_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(18)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.yacht_club.display, param=self)

    def sw_hole19_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(19)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.yacht_club.display, param=self)

    def sw_hole20_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(20)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.yacht_club.display, param=self)

    def sw_hole21_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(21)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.yacht_club.display, param=self)

    def sw_hole22_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(22)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.yacht_club.display, param=self)

    def sw_hole23_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(23)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.yacht_club.display, param=self)

    def sw_hole24_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(24)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.yacht_club.display, param=self)

    def sw_hole25_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(25)
            if self.game.ball_count.position >= 5:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.yacht_club.display, param=self)

    def sw_replayReset_active(self, sw):
        self.game.anti_cheat.disengage()
        self.holes = []
#        self.cancel_delayed(name="blink_title")
        graphics.yacht_club.display(self)
        self.tilt_actions()
#        self.delay(name="blink_title", delay=1, handler=self.blink_title)
        self.replay_step_down(self.game.replays)

    def sw_redstar_active(self, sw):
        if self.game.red_star.status == True:
            if self.game.right_rollover.status == False:
                self.game.right_rollover.engage(self.game)
                if 23 not in self.holes:
                    self.holes.append(23)
                if 24 not in self.holes:
                    self.holes.append(24)
            self.delay(name="display", delay=0.1, handler=graphics.yacht_club.display, param=self)
            if self.game.ball_count >= 5:
                self.search()

    def sw_yellowstar_active(self, sw):
        if self.game.yellow_star.status == True:
            if self.game.left_rollover.status == False:
                self.game.left_rollover.engage(self.game)
                if 15 not in self.holes:
                    self.holes.append(15)
                if 16 not in self.holes:
                    self.holes.append(16)
            self.delay(name="display", delay=0.1, handler=graphics.yacht_club.display, param=self)
            if self.game.ball_count >= 5:
                self.search()

    def tilt_actions(self):
        self.game.start.disengage()
        self.cancel_delayed(name="replay_reset")
        self.cancel_delayed(name="card1_replay_step_up")
        self.game.coils.redROLamp.disable()
        self.game.coils.yellowROLamp.disable()
        self.game.search_index.disengage()
        if self.game.ball_count.position == 0:
            if self.game.switches.shutter.is_active():
                self.game.coils.shutter.enable()
        self.holes = []
        self.game.selector.reset()
        self.game.card1_replay_counter.reset()
        self.game.super_card.reset()
        self.game.yellow_star.disengage()
        self.game.red_star.disengage()
        self.game.select_card.reset()
        self.game.ball_count.reset()
        self.game.card.reset()
        self.game.odds.reset()
        self.game.eb_play.disengage()
        self.game.extra_ball.reset()
        self.game.anti_cheat.engage(game)
        self.game.tilt.engage(self.game)
        self.game.sound.stop_music()
        self.game.sound.play('tilt')
        # displays "Tilt" on the backglass, you have to recoin.
        self.delay(name="display", delay=0.1, handler=graphics.yacht_club.display, param=self)

    def sw_tilt_active(self, sw):
        if self.game.tilt.status == False:
            self.tilt_actions()

    def replay_step_down(self, number=0):
        if number > 0:
            if number > 1:
                self.game.replays -= 1
                graphics.replay_step_down(self.game.replays, graphics.yacht_club.reel1, graphics.yacht_club.reel10, graphics.yacht_club.reel100)
                self.game.coils.registerDown.pulse()
                number -= 1
                self.delay(name="display", delay=0, handler=graphics.yacht_club.display, param=self)
                self.delay(name="replay_reset", delay=0.0, handler=self.replay_step_down, param=number)
            elif number == 1:
                self.game.replays -= 1
                graphics.replay_step_down(self.game.replays, graphics.yacht_club.reel1, graphics.yacht_club.reel10, graphics.yacht_club.reel100)
                self.game.coils.registerDown.pulse()
                number -= 1
                self.delay(name="display", delay=0, handler=graphics.yacht_club.display, param=self)
                self.cancel_delayed(name="replay_reset")
        else: 
            if self.game.replays > 0:
                self.game.replays -= 1
                graphics.replay_step_down(self.game.replays, graphics.yacht_club.reel1, graphics.yacht_club.reel10, graphics.yacht_club.reel100)
                self.delay(name="display", delay=0.1, handler=graphics.yacht_club.display, param=self)
            self.game.coils.registerDown.pulse()

    def replay_step_up(self):
        if self.game.replays < 899:
            self.game.replays += 1
            graphics.replay_step_up(self.game.replays, graphics.yacht_club.reel1, graphics.yacht_club.reel10, graphics.yacht_club.reel100)
        self.game.coils.registerUp.pulse()
        self.game.coils.sounder.pulse()
        self.game.reflex.increase()
        graphics.yacht_club.display(self)

    def sw_yellow_active(self, sw):
        if self.game.ball_count.position >= 5:
            if self.game.eb_play.status == False:
                self.game.spotting.spin()
                self.game.mixer1.spin()
                self.game.mixer2.spin()
                self.game.mixer3.spin()
                self.game.mixer4.spin()
                self.game.eb_play.engage(self.game)
                self.delay(name="display", delay=0.1, handler=graphics.yacht_club.display, param=self)
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
                self.delay(name="display", delay=0.1, handler=graphics.yacht_club.display, param=self)
            
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
        
        for i in range(0, 60):
            self.r = self.closed_search_relays(self.game.searchdisc.position)
            self.game.searchdisc.spin()
            self.wipers = self.r[0]
            self.card = self.r[1]
            self.supercard = self.r[2]

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
                        if self.game.card.position + 1 >= self.card:
                            if s >= 2:
                                self.find_winner(s, self.card, self.supercard)
                                break
#        self.delay(name="blink_title", delay=3, handler=self.blink_title)

    def find_winner(self, relays, card, supercard):
        if self.game.search_index.status == False and self.game.replays < 899:
            if self.game.odds.position == 1:
                threeodds = 4
                fourodds = 12
                fiveodds = 96
            elif self.game.odds.position == 2:
                threeodds = 6
                fourodds = 16
                fiveodds = 96
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
                fourodds = 100
                fiveodds = 192
            elif self.game.odds.position == 8:
                threeodds = 64
                fourodds = 200
                fiveodds = 300

            print self.game.card.position
            if self.game.card.position + 1 == card:
                if relays == 2:
                    if supercard == 1:
                        if self.game.super_card.position > 4:
                            if self.game.card1_replay_counter.position < threeodds:
                                self.game.search_index.engage(self.game)
                                self.card1_replay_step_up(threeodds - self.game.card1_replay_counter.position)
                    elif supercard == 2:
                        if self.game.super_card.position == 10:
                            if self.game.card1_replay_counter.position < fourodds:
                                self.game.search_index.engage(self.game)
                                self.card1_replay_step_up(fourodds - self.game.card1_replay_counter.position)
                    else:
                        pass
                if relays == 3:
                    if self.game.card1_replay_counter.position < threeodds:
                        self.game.search_index.engage(self.game)
                        self.card1_replay_step_up(threeodds - self.game.card1_replay_counter.position)
                if relays == 4:
                    if self.game.card1_replay_counter.position < fourodds:
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

    def closed_search_relays(self, rivets):
        # This function is critical, as it will determine which card is returned, etc.  I need to check the position of the
        # replay counter for the card. We will get a row back
        # that has the numbers on the position which will return the search relay connected.  When three out of the five relays
        # are connected, we get a winner!
        
        self.pos = {}
        # Card 1
        self.pos[0] = {}
        self.pos[1] = {10:1, 1:2, 12:3, 7:4, 16:5}
        self.pos[2] = {6:1, 19:2, 8:3, 20:4, 24:5}
        self.pos[3] = {18:1, 5:2, 17:3, 25:4, 15:5}
        self.pos[4] = {9:1, 22:2, 3:3, 21:4, 23:5}
        self.pos[5] = {2:1, 13:2, 11:3, 4:4, 14:5}
        self.pos[6] = {10:1, 6:2, 18:3, 9:4, 2:5}
        self.pos[7] = {1:1, 19:2, 5:3, 22:4, 13:5}
        self.pos[8] = {12:1, 8:2, 17:3, 3:4, 11:5}
        self.pos[9] = {7:1, 20:2, 25:3, 21:4, 4:5}
        self.pos[10] = {16:1, 24:2, 15:3, 23:4, 14:5}
        self.pos[11] = {16:1, 20:2, 17:3, 22:4, 2:5}
        self.pos[12] = {10:1, 19:2, 17:3, 21:4, 14:5}
        self.pos[13] = {1:1, 12:2, 7:3, 16:4, 18:5}
        self.pos[14] = {19:1, 8:2, 20:3, 24:4, 9:5}
        self.pos[15] = {5:1, 17:2, 25:3, 15:4, 10:5}
        self.pos[16] = {22:1, 3:2, 21:3, 23:4, 2:5}
        self.pos[17] = {13:1, 11:2, 4:3, 14:4, 6:5}
        self.pos[18] = {1:1, 19:2, 5:3, 22:4, 13:5}
        self.pos[19] = {12:1, 8:2, 17:3, 3:4, 11:5}
        self.pos[20] = {7:1, 20:2, 25:3, 21:4, 4:5}
        self.pos[21] = {16:1, 24:2, 15:3, 23:4, 14:5}
        self.pos[22] = {18:1, 9:2, 10:3, 2:4, 6:5}
        self.pos[23] = {18:1, 24:2, 25:3, 3:4, 13:5}
        self.pos[24] = {1:1, 8:2, 25:3, 23:4, 6:5}
        self.pos[25] = {12:1, 7:2, 16:3, 18:4, 19:5}
        self.pos[26] = {8:1, 20:2, 24:3, 9:4, 13:5}
        self.pos[27] = {17:1, 25:2, 15:3, 10:4, 1:5}
        self.pos[28] = {3:1, 21:2, 23:3, 2:4, 5:5}
        self.pos[29] = {11:1, 4:2, 14:3, 6:4, 22:5}
        self.pos[30] = {12:1, 8:2, 17:3, 3:4, 11:5}
        self.pos[31] = {7:1, 20:2, 25:3, 21:4, 4:5}
        self.pos[32] = {16:1, 24:2, 15:3, 23:4, 14:5}
        self.pos[33] = {18:1, 9:2, 10:3, 2:4, 6:5}
        self.pos[34] = {19:1, 13:2, 1:3, 5:4, 22:5}
        self.pos[35] = {19:1, 9:2, 15:3, 21:4, 11:5}
        self.pos[36] = {12:1, 20:2, 15:3, 2:4, 22:5}
        self.pos[37] = {7:1, 16:2, 18:3, 19:4, 3:5}
        self.pos[38] = {20:1, 24:2, 9:3, 13:4, 8:5}
        self.pos[39] = {25:1, 15:2, 10:3, 1:4, 11:5}
        self.pos[40] = {21:1, 23:2, 2:3, 5:4, 12:5}
        self.pos[41] = {4:1, 14:2, 6:3, 22:4, 17:5}
        self.pos[42] = {7:1, 20:2, 25:3, 21:4, 4:5}
        self.pos[43] = {16:1, 24:2, 15:3, 23:4, 14:5}
        self.pos[44] = {18:1, 9:2, 10:3, 2:4, 6:5}
        self.pos[45] = {19:1, 13:2, 1:3, 5:4, 22:5}
        self.pos[46] = {3:1, 8:2, 11:3, 12:4, 17:5}
        self.pos[47] = {3:1, 13:2, 10:3, 23:4, 4:5}
        self.pos[48] = {7:1, 24:2, 10:3, 5:4, 17:5}
        self.pos[49] = {16:1, 18:2, 19:3, 3:4, 25:5}
        self.pos[50] = {24:1, 9:2, 13:3, 8:4, 7:5}
        self.pos[51] = {15:1, 10:2, 1:3, 11:4, 21:5}
        self.pos[52] = {23:1, 2:2, 5:3, 12:4, 4:5}
        self.pos[53] = {14:1, 6:2, 22:3, 17:4, 20:5}
        self.pos[54] = {16:1, 24:2, 15:3, 23:4, 14:5}
        self.pos[55] = {18:1, 9:2, 10:3, 2:4, 6:5}
        self.pos[56] = {19:1, 13:2, 1:3, 5:4, 22:5}
        self.pos[57] = {3:1, 8:2, 11:3, 12:4, 17:5}
        self.pos[58] = {25:1, 7:2, 21:3, 4:4, 20:5}
        self.pos[59] = {25:1, 8:2, 1:3, 2:4, 14:5}
        self.pos[60] = {16:1, 9:2, 1:3, 12:4, 20:5}

        sc = 0
        card = 0

        if rivets in range(0, 13):
            card = 1
        if rivets in range(13, 25):
            card = 2
        if rivets in range(25, 37):
            card = 3
        if rivets in range(37, 49):
            card = 4
        if rivets in range(49, 60):
            card = 5
        if rivets == 2 or rivets == 14 or rivets == 26 or rivets == 38 or rivets == 50:
            sc = 2
        if rivets == 4 or rivets == 16 or rivets == 28 or rivets == 40 or rivets == 52:
            sc = 1

        return (self.pos[rivets], card, sc)
    
    def scan_all(self):
        #Animate scanning of everything - this happens through the spotting disc
        self.all_probability()

    def all_probability(self):
        mix1 = self.game.mixer1.connected_rivet()
        if self.game.reflex.connected_rivet() == 0 and (mix1 == 1 or mix1 == 6 or mix1 == 8 or mix1 == 11 or mix1 == 13 or mix1 == 16 or mix1 == 18 or mix1 == 22 or mix1 == 24):
            self.scan_odds()
            self.scan_features()
        elif self.game.reflex.connected_rivet() == 1 and (mix1 != 2 or mix1 != 5 or mix1 != 7 or mix1 != 9 or mix1 != 12 or mix1 != 14 or mix1 != 15 or mix1 != 19 or mix1 != 23):
            self.scan_odds()
            self.scan_features()
        elif self.game.reflex.connected_rivet() == 2 and (mix1 != 5 or mix1 != 9 or mix1 != 12 or mix1 != 15 or mix1 != 19 or mix1 != 23):
            self.scan_odds()
            self.scan_features()
        elif self.game.reflex.connected_rivet() == 3 and (mix1 != 5 or mix1 != 9 or mix1 != 15 or mix1 != 23):
            self.scan_odds()
            self.scan_features()
        elif self.game.reflex.connected_rivet() == 4:
            self.scan_odds()
            self.scan_features()
        else:
            s = random.randint(1,8)
            self.animate_odds_scan(s)
            s = random.randint(1,4)
            self.animate_feature_scan(s)
            if self.game.odds.position == 0:
                self.game.odds.step()

    def scan_odds(self):
        if self.game.odds.position == 0:
            self.game.odds.step()
        s = random.randint(1,8)
        self.animate_odds_scan(s)
        p = self.odds_probability()
        if p == 1:
            es = self.check_extra_step()
            if es == 1:
                i = random.randint(1,6)
                self.extra_step(i)
            else:
                self.game.odds.step()

    def extra_step(self, number):
        if number > 0:
            self.game.odds.step()
            self.game.coils.counter.pulse()
            self.delay(name="display", delay=0.1, handler=graphics.yacht_club.display, param=self)
            number -= 1
            self.delay(name="extra_step", delay=0.1, handler=self.extra_step, param=number)

    def check_extra_step(self):
        i = random.randint(0,32)
        if i == 16:
            return 1
        else:
            return 0

    def odds_probability(self):
        # Check position of Mixer 5, Mixer 4, and Mixer 3 and current 
        # position of the odds, along with trip relays.
        # For first check, guaranteed single stepup.  Probability doesn't 
        # factor, so I will return as part of the initial check above.
        if self.game.odds.position == 0:
            return 1
        else:
            m3 = self.check_mixer3()
            if m3 == True:
                m = False
                if self.game.select_card.position >= True:
                    m = self.check_mixer32()
                if m == True or self.game.select_card.position < 6:
                    m2 = self.check_mixer2()
                    if m2 == True:
                        return 1
                    else:
                        return 0
                else:
                    return 0
            else:
                return 0
            
            return 0


    def check_mixer3(self):
        mix3 = self.game.mixer3.connected_rivet()
        if self.game.super_card.position < 8:
            if mix3 == 20 or mix3 == 21 or mix3 == 22 or mix3 == 23 or mix3 == 24 or mix3 == 17 or mix3 == 18 or mix3 == 19:
                return 1
            else:
                return 0
        else:
            if mix3 == 20 or mix3 == 21 or mix3 == 22 or mix3 == 23 or mix3 == 24:
                return 1
            else:
                return 0

    def check_mixer32(self):
        mix3 = self.game.mixer3.connected_rivet()
        if self.game.eb_play.status == False:
            if mix3 == 6 or mix3 == 7 or mix3 == 8 or mix3 == 9 or mix3 == 10 or mix3 == 11 or mix3 == 12 or mix3 == 13 or mix3 == 14 or mix3 == 18 or mix3 == 19 or mix3 == 20 or mix3 == 23 or mix3 == 24:
                return 1
            else:
                return 0
        else:
            if mix3 == 6 or mix3 == 7 or mix3 == 8 or mix3 == 9 or mix3 == 10 or mix3 == 11 or mix3 == 12 or mix3 == 13 or mix3 == 14 or mix3 == 23 or mix3 == 24:
                return 1
            else:
                return 0

    def check_mixer2(self):
        mix2 = self.game.mixer2.connected_rivet()
        if mix2 == 2 or mix2 == 3 or mix2 == 4 or mix2 == 12 or mix2 == 13 or mix2 == 14 or mix2 == 16 or mix2 == 9 or mix2 == 20:
            return 1
        else:
            return 0

    def scan_features(self):
        p = self.features_probability()

    def features_probability(self):
        s = random.randint(1,4)
        self.animate_feature_scan(s)
        mix2 = self.game.mixer2.connected_rivet()
        mix3 = self.game.mixer3.connected_rivet()
        #if self.game.selector.position == 1: Killing this - no wonder why it didn't give anything.
        if self.game.odds.position == 0 or self.game.odds.position == 1:
            if mix2 == 3:
                self.features_spotting()
        elif self.game.odds.position == 2:
            self.features_spotting()
        elif self.game.odds.position == 3 or self.game.odds.position == 4:
            if mix2 == 22:
                self.features_spotting()
        elif self.game.odds.position == 5 or self.game.odds.position == 6:
            if mix2 == 24:
                self.features_spotting()
        elif self.game.odds.position == 7 or self.game.odds.position == 8:
            if mix2 == 20:
                self.features_spotting()

    def features_spotting(self):
        if self.game.spotting.position == 25 or (self.game.spotting.position == 5 and self.game.reflex.connected_rivet() == 4):
            self.select_card_step(8 - self.game.select_card.position)
        if self.game.spotting.position == 6:
            if self.game.select_card.position < 7:
                self.select_card_step(7 - self.game.select_card.position)
            else:
                self.select_card_step(8 - self.game.select_card.position)
        if self.game.spotting.position == 3 or self.game.spotting.position == 5 or self.game.spotting.position == 8 or self.game.spotting.position == 11:
            #if self.game.cu:
            self.game.select_card.step()
            self.game.super_card.step()
        if self.game.spotting.position == 40:
            if self.game.red_star.status == False:
                self.game.red_star.engage(self.game)
                self.game.coils.yellowROLamp.enable()
        if self.game.spotting.position == 29 and self.game.yellow_star.status == False:
            self.game.red_star.engage(self.game)
            self.game.coils.yellowROLamp.enable()
        if self.game.spotting.position == 10:
            self.game.yellow_star.engage(self.game)
            self.game.coils.redROLamp.enable()
        if self.game.spotting.position == 27 and self.game.red_star.status == False:
            self.game.yellow_star.engage(self.game)
            self.game.coils.redROLamp.enable()
        if self.game.spotting.position == 4:
            self.step_sc(10 - self.game.super_card.position)
        if self.game.spotting.position == 2:
            self.step_sc(5 - self.game.super_card.position)
        if self.game.spotting.position == 31:
            if self.game.super_card.position >= 5:
                self.step_sc(10 - self.game.super_card.position)

    def select_card_step(self, number):
        if number >= 1:
            self.game.select_card.step()
            number -= 1
            self.delay(name="display", delay=0.1, handler=graphics.yacht_club.display, param=self)
            self.delay(name="select_card_step", delay=0.1, handler=self.select_card_step, param=number)

    def step_sc(self, number):
        if number >= 1:
            self.game.super_card.step()
            number -= 1
            self.delay(name="display", delay=0.1, handler=graphics.yacht_club.display, param=self)
            self.delay(name="step_sc", delay=0.1, handler=self.step_sc, param=number)

    def scan_eb(self):
        s = random.randint(1,3)
        self.animate_eb_scan(s)
        if self.game.extra_ball.position == 0:
            self.game.extra_ball.step()
            self.check_lifter_status()
        p = self.eb_probability()
        if p == 1:
            if self.game.extra_ball.position < 21:
                m3 = self.check_mixer3()
                if m3 == True:
                    m = False
                    if self.game.select_card.position >= 6:
                        m = self.check_mixer32()
                    if m == True or self.game.select_card.position < 6:
                        if self.game.left_rollover.status == False:
                            if self.game.right_rollover.status == False:
                                mix4 = self.game.mixer4.connected_rivet()
                                if mix4 == 1 or mix4 == 2 or mix4 == 3 or mix4 == 4 or mix4 == 5 or mix4 == 6 or mix4 == 7 or mix4 == 14 or mix4 == 15 or mix4 == 16 or mix4 == 17 or mix4 == 21 or mix4 == 22 or mix4 == 23 or mix4 == 24:
                                    if self.game.spotting.position == 50 and self.game.mixer4.position == 24:
                                        self.step_eb(21 - self.game.extra_ball.position)
                                    elif self.game.spotting.position == 21:
                                        if self.game.extra_ball.position < 7:
                                            self.step_eb(7 - self.game.extra_ball.position)
                                    elif self.game.spotting.position == 10:
                                        if self.game.extra_ball.position < 14:
                                            self.step_eb(14 - self.game.extra_ball.position)
                                        else:
                                            self.step_eb(21 - self.game.extra_ball.position)
                                    elif self.game.spotting.position == 3:
                                        if self.game.cu == 1:
                                            self.step_eb(6)
                                        else:
                                            self.step_eb(4)
                                    else:
                                        self.step_eb(1)
                            else:
                                if self.game.left_rollover.status == False:
                                    mix4 = self.game.mixer4.connected_rivet()
                                    if mix4 == 4 or mix4 == 5 or mix4 == 6 or mix4 == 7 or mix4 == 14 or mix4 == 15 or mix4 == 16 or mix4 == 17 or mix4 == 21 or mix4 == 22 or mix4 == 23 or mix4 == 24:
                                        if self.game.spotting.position == 50 and self.game.mixer4.position == 24:
                                            self.step_eb(21 - self.game.extra_ball.position)
                                        elif self.game.spotting.position == 21:
                                            if self.game.extra_ball.position < 7:
                                                self.step_eb(7 - self.game.extra_ball.position)
                                        elif self.game.spotting.position == 10:
                                            if self.game.extra_ball.position < 14:
                                                self.step_eb(14 - self.game.extra_ball.position)
                                            else:
                                                self.step_eb(21 - self.game.extra_ball.position)
                                        elif self.game.spotting.position == 3:
                                            if self.game.cu == 1:
                                                self.step_eb(6)
                                            else:
                                                self.step_eb(4)
                                        else:
                                            self.step_eb(1)
                                else:
                                    mix4 = self.game.mixer4.connected_rivet()
                                    if mix4 == 1 or mix4 == 2 or mix4 == 3 or mix4 == 14 or mix4 == 15 or mix4 == 16 or mix4 == 17 or mix4 == 21 or mix4 == 22 or mix4 == 23 or mix4 == 24:
                                        if self.game.spotting.position == 50 and self.game.mixer4.position == 24:
                                            self.step_eb(21 - self.game.extra_ball.position)
                                        elif self.game.spotting.position == 21:
                                            if self.game.extra_ball.position < 7:
                                                self.step_eb(7 - self.game.extra_ball.position)
                                        elif self.game.spotting.position == 10:
                                            if self.game.extra_ball.position < 14:
                                                self.step_eb(14 - self.game.extra_ball.position)
                                            else:
                                                self.step_eb(21 - self.game.extra_ball.position)
                                        elif self.game.spotting.position == 3:
                                            if self.game.cu == 1:
                                                self.step_eb(6)
                                            else:
                                                self.step_eb(4)
                                        else:
                                            self.step_eb(1)
                        else:
                            mix4 = self.game.mixer4.connected_rivet()
                            if mix4 == 14 or mix4 == 15 or mix4 == 16 or mix4 == 17 or mix4 == 21 or mix4 == 22 or mix4 == 23 or mix4 == 24:
                                if self.game.spotting.position == 50 and self.game.mixer4.position == 24:
                                    self.step_eb(21 - self.game.extra_ball.position)
                                elif self.game.spotting.position == 21:
                                    if self.game.extra_ball.position < 7:
                                        self.step_eb(7 - self.game.extra_ball.position)
                                elif self.game.spotting.position == 10:
                                    if self.game.extra_ball.position < 14:
                                        self.step_eb(14 - self.game.extra_ball.position)
                                    else:
                                        self.step_eb(21 - self.game.extra_ball.position)
                                elif self.game.spotting.position == 3:
                                    if self.game.cu == 1:
                                        self.step_eb(6)
                                    else:
                                        self.step_eb(4)
                                else:
                                    self.step_eb(1)
                                
        # Timer resets to 0 position on ball count increasing.  We are fudging this since we will have
        # no good way to measure balls as they return back to the trough.  The ball count unit cannot be
        # relied upon as we do not have a switch in the outhole, and the trough logic is too complex for
        # the task at hand.
        # TODO: implement thunk noises into the units.py to automatically play the noises.
        self.game.timer.reset()
        self.delay(name="display", delay=0.1, handler=graphics.yacht_club.display, param=self)

    def animate_odds_scan(self, s):
        if s > 1:
            self.delay(name="odds_animation", delay=0.1, handler=graphics.yacht_club.odds_animation, param=s)
            self.delay(name="display", delay=0.1, handler=graphics.yacht_club.display, param=self)
            s -= 1
            #self.delay(name="animate_odds", delay=0.1, handler=self.animate_odds_scan, param=s)
        else:
            self.cancel_delayed(name="odds_animation")
            self.cancel_delayed(name="display")

    def animate_feature_scan(self, s):
        if s > 1:
            self.delay(name="feature_animation", delay=0.1, handler=graphics.yacht_club.feature_animation, param=s)
            self.delay(name="display", delay=0.1, handler=graphics.yacht_club.display, param=self)
            s -= 1
            #self.delay(name="animate_feature", delay=0.1, handler=self.animate_feature_scan, param=s)
        else:
            self.delay(name="display", delay=0.1, handler=graphics.yacht_club.display, param=self)

    def animate_eb_scan(self, s):
        if s > 1:
            self.delay(name="eb_animation", delay=0.1, handler=graphics.yacht_club.eb_animation, param=s)
            self.delay(name="display", delay=0.1, handler=graphics.yacht_club.display, param=self)
            s -= 1
            #self.delay(name="animate_eb", delay=0.1, handler=self.animate_eb_scan, param=s)
        else:
            self.delay(name="display", delay=0.1, handler=graphics.yacht_club.display, param=self)

    def eb_probability(self):
        mix1 = self.game.mixer1.connected_rivet()
        if self.game.reflex.connected_rivet() == 0 and (mix1 == 1 or mix1 == 6 or mix1 == 8 or mix1 == 11 or mix1 == 13 or mix1 == 16 or mix1 == 18 or mix1 == 22 or mix1 == 24):
            return 1
        elif self.game.reflex.connected_rivet() == 1 and (mix1 != 2 or mix1 != 5 or mix1 != 7 or mix1 != 9 or mix1 != 12 or mix1 != 14 or mix1 != 15 or mix1 != 19 or mix1 != 23):
            return 1
        elif self.game.reflex.connected_rivet() == 2 and (mix1 != 5 or mix1 != 9 or mix1 != 12 or mix1 != 15 or mix1 != 19 or mix1 != 23):
            return 1
        elif self.game.reflex.connected_rivet() == 3 and (mix1 != 5 or mix1 != 9 or mix1 != 15 or mix1 != 23):
            return 1
        elif self.game.reflex.connected_rivet() == 4:
            return 1
        else:
            return 0

    def step_eb(self, number):
        if number >= 1:
            self.game.extra_ball.step()
            self.check_lifter_status()
            number -= 1
            self.delay(name="display", delay=0.1, handler=graphics.yacht_club.display, param=self)
            self.delay(name="step_eb", delay=0.1, handler=self.step_eb, param=number)

    def blink_title(self):
        title1 = random.randint(0,1)
        title2 = random.randint(0,1)
        title3 = random.randint(0,1)
        title4 = random.randint(0,1)
        if title1 == 1:
            pos = [167,257]
            image = pygame.image.load('yacht_club/assets/title1_on.png').convert_alpha()
            screen.blit(image, pos)
        if title2 == 1:
            pos = [241,290]
            image = pygame.image.load('yacht_club/assets/title2_on.png').convert_alpha()
            screen.blit(image, pos)
        if title3 == 1:
            pos = [346,298]
            image = pygame.image.load('yacht_club/assets/title3_on.png').convert_alpha()
            screen.blit(image, pos)
        if title4 == 1:
            pos = [431,264]
            image = pygame.image.load('yacht_club/assets/title4_on.png').convert_alpha()
            screen.blit(image, pos)
            
        pygame.display.update()
        self.delay(name="display", delay=0.1, handler=graphics.yacht_club.display, param=self)
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


class YachtClub(procgame.game.BasicGame):
    """ Palm Beach was the first game with Super Cards """
    def __init__(self, machine_type):
        super(YachtClub, self).__init__(machine_type)
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

        self.searchdisc = units.Search("searchdisc", 60)

        #Search relays
        self.s1 = units.Relay("s1")
        self.s2 = units.Relay("s2")
        self.s3 = units.Relay("s3")
        self.s4 = units.Relay("s4")
        self.s5 = units.Relay("s5")
        self.search_index = units.Relay("search_index")

        #Odds stepper
        self.odds = units.Stepper("odds", 8, 'yacht_club')

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
        self.extra_ball = units.Stepper("extra_ball", 21)

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

        self.selector = units.Stepper("selector", 1)

        # Select-a-spot setup
        self.select_card = units.Stepper("select_card", 8)
        self.card = units.Stepper("card", 6)

        self.super_card = units.Stepper("super_card", 10)

        #Some special trip relays for spotted numbers and rollovers
        self.red_star = units.Relay("red_star")
        self.yellow_star = units.Relay("yellow_star")

        #Yellow spots 15 and 16
        self.left_rollover = units.Relay("left_rollover")
        #Red spots 23 and 24
        self.right_rollover = units.Relay("right_rollover")

        self.replays = 0
        self.returned = False

    def reset(self):
        super(YachtClub, self).reset()
        self.logger = logging.getLogger('game')
        self.load_config('bingo.yaml')
        
        main_mode = SinglecardBingo(self)
        self.modes.add(main_mode)
        
game = YachtClub(machine_type='pdb')
game.reset()
game.run_loop()
