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
from bingo_emulator.graphics.mystic_gate import *

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
            self.game.sound.stop('add')
            self.game.sound.play('add')
            self.game.cu = not self.game.cu
            self.game.scramble.spin()
            self.game.program.spin()
            self.regular_play()
            if self.game.coin.position < 40:
                self.scan_all()
        else:
            self.game.sound.stop('add')
            self.game.sound.play('add')
            self.game.cu = not self.game.cu
            self.game.scramble.spin()
            self.game.program.spin()
            self.regular_play()
            if self.game.coin.position < 40:
                self.scan_all()
        self.delay(name="display", delay=0.1, handler=graphics.mystic_gate.display, param=self)

    def sw_startButton_active(self, sw):
        if self.game.replays > 0 or self.game.switches.freeplay.is_active():
            self.game.sound.stop('add')
            self.game.sound.play('add')
            self.game.cu = not self.game.cu
            self.game.scramble.spin()
            self.game.program.spin()
            self.game.tilt.disengage()
            self.regular_play()
            if self.game.start.status == True and self.game.coin.position < 40:
                self.scan_all()

        self.delay(name="display", delay=0.1, handler=graphics.mystic_gate.display, param=self)

    def sw_blue_active(self, sw):
        if self.game.gate.status == True:
            self.check_gate(self)
        self.delay(name="display", delay=0.1, handler=graphics.mystic_gate.display, param=self)

    def check_gate(self):
        #Forget about writing this until the appropriate switches are wired in.
        pass

    def sw_enter_active(self, sw):
        if self.game.switches.left.is_active() and self.game.switches.right.is_active():
            self.game.end_run_loop()
            os.system("/home/nbaldridge/proc/bingo_emulator/start_game.sh mystic_gate")
        else:
            if self.game.ball_count.position >= 4:
                self.game.sound.stop_music()
                self.game.sound.play_music('motor', -1)
                self.game.timer.reset()
                if self.game.search_index.status == False:
                    self.search()
                    self.timeout_actions()
            if self.game.switches.drawer.is_inactive():
                if self.game.ball_count.position > 0:
                    max_ball = 0
                    if self.game.selection_feature.position < 7:
                        max_ball = 4
                    elif self.game.selection_feature.position < 8:
                        max_ball = 5
                    else:
                        if self.game.selection_feature.position == 9:
                            max_ball = 6
                    msu = self.game.mystic_lines.position

                    if self.game.ball_count.position < max_ball:
                        if self.game.mystic_lines.position >= 6:
                            self.game.line3.step()
                                    
                    self.delay(name="display", delay=0.1, handler=graphics.mystic_gate.display, param=self)

    def sw_letterc_active(self, sw):
        if self.game.switches.drawer.is_active():
            if self.game.ball_count.position > 0:
                max_ball = 0
                if self.game.selection_feature.position < 7:
                    max_ball = 4
                elif self.game.selection_feature.position < 8:
                    max_ball = 5
                else:
                    if self.game.selection_feature.position == 9:
                        max_ball = 6
                msu = self.game.mystic_lines.position

                if self.game.ball_count.position < max_ball:
                    if self.game.mystic_lines.position >= 6:
                        self.game.line3.step()
                                
                self.delay(name="display", delay=0.1, handler=graphics.mystic_gate.display, param=self)

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
        if self.game.switches.drawer.is_inactive():
            if self.game.ball_count.position > 0:
                max_ball = 0
                if self.game.selection_feature.position < 7:
                    max_ball = 4
                elif self.game.selection_feature.position < 8:
                    max_ball = 5
                else:
                    if self.game.selection_feature.position == 9:
                        max_ball = 6
                msu = self.game.mystic_lines.position

                if self.game.ball_count.position < max_ball:
                    if self.game.mystic_lines.position >= 6:
                        self.game.line2.step()
                                
                self.delay(name="display", delay=0.1, handler=graphics.mystic_gate.display, param=self)

    def sw_letterb_active(self, sw):
        if self.game.switches.drawer.is_active():
            if self.game.ball_count.position > 0:
                max_ball = 0
                if self.game.selection_feature.position < 7:
                    max_ball = 4
                elif self.game.selection_feature.position < 8:
                    max_ball = 5
                else:
                    if self.game.selection_feature.position == 9:
                        max_ball = 6
                msu = self.game.mystic_lines.position

                if self.game.ball_count.position < max_ball:
                    if self.game.mystic_lines.position >= 6:
                        self.game.line2.step()
                                
                self.delay(name="display", delay=0.1, handler=graphics.mystic_gate.display, param=self)


    def sw_left_active(self, sw):
        if self.game.switches.drawer.is_inactive():
            if self.game.ball_count.position > 0:
                max_ball = 0
                if self.game.selection_feature.position < 7:
                    max_ball = 4
                elif self.game.selection_feature.position < 8:
                    max_ball = 5
                else:
                    if self.game.selection_feature.position == 9:
                        max_ball = 6
                msu = self.game.mystic_lines.position

                if self.game.ball_count.position < max_ball:
                    if self.game.mystic_lines.position >= 2:
                        self.game.line1.step()
                                
                self.delay(name="display", delay=0.1, handler=graphics.mystic_gate.display, param=self)

    def sw_lettera_active(self, sw):
        if self.game.switches.drawer.is_active():
            if self.game.ball_count.position > 0:
                max_ball = 0
                if self.game.selection_feature.position < 7:
                    max_ball = 4
                elif self.game.selection_feature.position < 8:
                    max_ball = 5
                else:
                    if self.game.selection_feature.position == 9:
                        max_ball = 6
                msu = self.game.mystic_lines.position

                if self.game.ball_count.position < max_ball:
                    if self.game.mystic_lines.position >= 2:
                        self.game.line1.step()
                                
                self.delay(name="display", delay=0.1, handler=graphics.mystic_gate.display, param=self)

    def check_selection(self):
        self.delay(name="display", delay=0.1, handler=graphics.mystic_gate.display, param=self)

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
        self.cancel_delayed(name="blue_replay_step_up")
        self.cancel_delayed(name="blink")
        self.cancel_delayed(name="timeout")
        self.game.search_index.disengage()
        self.game.coils.counter.pulse()
        self.game.sound.play_music('motor', -1)

        self.game.cu = not self.game.cu
        self.game.program.spin()
        self.game.scramble.spin()
        self.game.reflex.decrease()

        self.game.returned = False
        if self.game.start.status == True:
            self.game.coin.step()
            if self.game.selector.position < 1:
                self.game.selector.step()
            if self.game.switches.shutter.is_inactive():
                self.game.coils.shutter.enable()
            self.replay_step_down()
            self.check_lifter_status()
        else:
            self.holes = []
            self.game.start.engage(self.game)
            self.game.yellow_odds.reset()
            self.game.green_odds.reset()
            self.game.blue_odds.reset()
            self.game.ball_count.reset()
            self.game.gate.disengage()
            self.game.selection_feature.reset()
            self.game.timer.reset()
            if self.game.line2.position == 1:
                self.game.line2.step()
            if self.game.line3.position == 1:
                self.game.line3.step()
            if self.game.line1.position != 0:
                self.game.line1.step()
                if self.game.line1.position != 0:
                    self.game.line1.step()
            self.game.mystic_lines.reset()
            self.game.double_red.disengage()
            self.game.double_yellow.disengage()
            self.game.double_green.disengage()
            self.game.double_blue.disengage()
            self.game.red_replay_counter.reset()
            self.game.blue_replay_counter.reset()
            self.game.yellow_replay_counter.reset()
            self.game.green_replay_counter.reset()
            self.game.stars_replay_counter.reset()
            self.game.red_odds.reset()
            self.game.selector.reset()
            self.game.three_stars.disengage()
            self.game.six_stars.disengage()
            self.game.timer.reset()
            self.game.sound.play_music('motor', -1)
            self.regular_play()
        self.delay(name="display", delay=0.1, handler=graphics.mystic_gate.display, param=self)
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
                if self.game.ball_count.position < 5:
                    self.game.coils.lifter.enable()

    def sw_gate_inactive_for_1ms(self, sw):
        self.game.start.disengage()
        self.game.ball_count.step()
        if self.game.switches.shutter.is_active():
            self.game.coils.shutter.enable()
        if self.game.ball_count.position <= 4:
            self.check_lifter_status()
        self.delay(name="display", delay=0.1, handler=graphics.mystic_gate.display, param=self)


    # This is really nasty, but it is how we render graphics for each individual hole.
    # numbers are added (or removed from) a list.  In this way, I can re-use the same
    # routine even for games where there are ball return functions like Surf Club.

    def sw_hole1_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(1)
            self.delay(name="display", delay=0.1, handler=graphics.mystic_gate.display, param=self)

    def sw_hole2_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(2)
            self.delay(name="display", delay=0.1, handler=graphics.mystic_gate.display, param=self)

    def sw_hole3_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(3)
            self.delay(name="display", delay=0.1, handler=graphics.mystic_gate.display, param=self)

    def sw_hole4_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(4)
            self.delay(name="display", delay=0.1, handler=graphics.mystic_gate.display, param=self)

    def sw_hole5_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(5)
            self.delay(name="display", delay=0.1, handler=graphics.mystic_gate.display, param=self)

    def sw_hole6_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(6)
            self.delay(name="display", delay=0.1, handler=graphics.mystic_gate.display, param=self)

    def sw_hole7_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(7)
            self.delay(name="display", delay=0.1, handler=graphics.mystic_gate.display, param=self)

    def sw_hole8_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(8)
            self.delay(name="display", delay=0.1, handler=graphics.mystic_gate.display, param=self)

    def sw_hole9_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(9)
            self.delay(name="display", delay=0.1, handler=graphics.mystic_gate.display, param=self)

    def sw_hole10_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(10)
            self.delay(name="display", delay=0.1, handler=graphics.mystic_gate.display, param=self)

    def sw_hole11_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(11)
            self.delay(name="display", delay=0.1, handler=graphics.mystic_gate.display, param=self)

    def sw_hole12_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(12)
            self.delay(name="display", delay=0.1, handler=graphics.mystic_gate.display, param=self)

    def sw_hole13_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(13)
            self.delay(name="display", delay=0.1, handler=graphics.mystic_gate.display, param=self)

    def sw_hole14_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(14)
            self.delay(name="display", delay=0.1, handler=graphics.mystic_gate.display, param=self)

    def sw_hole15_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(15)
            self.delay(name="display", delay=0.1, handler=graphics.mystic_gate.display, param=self)

    def sw_hole16_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(16)
            self.delay(name="display", delay=0.1, handler=graphics.mystic_gate.display, param=self)

    def sw_hole17_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(17)
            self.delay(name="display", delay=0.1, handler=graphics.mystic_gate.display, param=self)

    def sw_hole18_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(18)
            self.delay(name="display", delay=0.1, handler=graphics.mystic_gate.display, param=self)

    def sw_hole19_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(19)
            self.delay(name="display", delay=0.1, handler=graphics.mystic_gate.display, param=self)

    def sw_hole20_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(20)
            self.delay(name="display", delay=0.1, handler=graphics.mystic_gate.display, param=self)

    def sw_replayReset_active(self, sw):
        self.game.anti_cheat.disengage()
        self.holes = []
        graphics.mystic_gate.display(self)
        self.tilt_actions()
        self.replay_step_down(self.game.replays)

    def tilt_actions(self):
        self.game.start.disengage()
        self.game.coin.reset()
        self.cancel_delayed(name="replay_reset")
        self.cancel_delayed(name="red_replay_step_up")
        self.cancel_delayed(name="yellow_replay_step_up")
        self.cancel_delayed(name="green_replay_step_up")
        self.cancel_delayed(name="blue_replay_step_up")
        self.cancel_delayed(name="blink")
        self.cancel_delayed(name="timeout")
        self.game.search_index.disengage()
        if self.game.ball_count.position == 0:
            if self.game.switches.shutter.is_active():
                self.game.coils.shutter.enable()
        self.holes = []
        self.game.yellow_odds.reset()
        self.game.green_odds.reset()
        self.game.blue_odds.reset()
        self.game.ball_count.reset()
        self.game.gate.disengage()
        self.game.selection_feature.reset()
        self.game.timer.reset()
        if self.game.line2.position == 1:
            self.game.line2.step()
        if self.game.line3.position == 1:
            self.game.line3.step()
        if self.game.line1.position != 0:
            self.game.line1.step()
            if self.game.line1.position != 0:
                self.game.line1.step()
        self.game.mystic_lines.reset()
        self.game.double_red.disengage()
        self.game.double_yellow.disengage()
        self.game.double_green.disengage()
        self.game.double_blue.disengage()
        self.game.red_replay_counter.reset()
        self.game.blue_replay_counter.reset()
        self.game.yellow_replay_counter.reset()
        self.game.green_replay_counter.reset()
        self.game.stars_replay_counter.reset()
        self.game.red_odds.reset()
        self.game.selector.reset()
        self.game.three_stars.disengage()
        self.game.six_stars.disengage()
        self.game.selector.reset()
        self.game.anti_cheat.engage(game)
        self.game.tilt.engage(self.game)
        self.game.sound.stop_music()
        self.game.sound.play('tilt')
        # displays "Tilt" on the backglass, you have to recoin.
        self.delay(name="display", delay=0.1, handler=graphics.mystic_gate.display, param=self)

    def sw_tilt_active(self, sw):
        if self.game.tilt.status == False:
            self.tilt_actions()

    def replay_step_down(self, number=0):
        if number > 0:
            if number > 1:
                self.game.replays -= 1
                graphics.replay_step_down(self.game.replays, graphics.mystic_gate.reel1, graphics.mystic_gate.reel10, graphics.mystic_gate.reel100, graphics.mystic_gate.reel1000)
                self.game.coils.registerDown.pulse()
                number -= 1
                self.delay(name="display", delay=0, handler=graphics.mystic_gate.display, param=self)
                self.delay(name="replay_reset", delay=0.13, handler=self.replay_step_down, param=number)
            elif number == 1:
                self.game.replays -= 1
                graphics.replay_step_down(self.game.replays, graphics.mystic_gate.reel1, graphics.mystic_gate.reel10, graphics.mystic_gate.reel100, graphics.mystic_gate.reel1000)
                self.game.coils.registerDown.pulse()
                number -= 1
                self.delay(name="display", delay=0, handler=graphics.mystic_gate.display, param=self)
                self.cancel_delayed(name="replay_reset")
        else: 
            if self.game.replays > 0:
                self.game.replays -= 1
                graphics.replay_step_down(self.game.replays, graphics.mystic_gate.reel1, graphics.mystic_gate.reel10, graphics.mystic_gate.reel100, graphics.mystic_gate.reel1000)
                self.delay(name="display", delay=0.1, handler=graphics.mystic_gate.display, param=self)
            self.game.coils.registerDown.pulse()

    def replay_step_up(self):
        if self.game.replays < 8999:
            self.game.replays += 1
            graphics.replay_step_up(self.game.replays, graphics.mystic_gate.reel1, graphics.mystic_gate.reel10, graphics.mystic_gate.reel100, graphics.mystic_gate.reel1000)
        self.game.coils.registerUp.pulse()
        self.game.reflex.increase()
        graphics.mystic_gate.display(self)

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
       
        for i in range(0, 6):
            self.r = self.closed_search_relays(self.game.searchdisc.position)
            self.game.searchdisc.spin()
            self.wipers = self.r[0]
            self.red = self.r[1]
            self.yellow = self.r[2]
            self.green = self.r[3]
            self.blue = self.r[4]
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
                        if relays == 4:
                            if self.red == True:
                                if self.game.line3.position == 0:
                                    if 6 in self.holes:
                                        relays += 1
                                else:
                                    if 13 in self.holes:
                                        relays += 1
                            elif self.green == True:
                                if self.game.line3.position == 0:
                                    if 17 in self.holes:
                                        relays += 1
                                else:
                                    if 9 in self.holes:
                                        relays += 1
                            elif self.yellow == True:
                                if self.game.line2.position == 0:
                                    if 1 in self.holes:
                                        relays += 1
                                else:
                                    if 15 in self.holes:
                                        relays += 1
                            elif self.blue == True:
                                if self.game.line2.position == 0:
                                    if 16 in self.holes:
                                        relays += 1
                                else:
                                    if 14 in self.holes:
                                        relays += 1
                        #TODO Play sound for each relay closure.
                        s = relays 
                        if s >= 2:
                            self.find_winner(s, self.red, self.yellow, self.green, self.blue, self.stars)
                            break
                            
    def find_winner(self, relays, red, yellow, green, blue, stars):
        if self.game.search_index.status == False and self.game.replays < 8999:
            if self.game.red_odds.position == 1:
                redthreeodds = 4
                redfourodds = 16
                redfiveodds = 75
            elif self.game.red_odds.position == 2:
                redthreeodds = 6
                redfourodds = 20
                redfiveodds = 75
            elif self.game.red_odds.position == 3:
                redthreeodds = 8
                redfourodds = 24
                redfiveodds = 96
            elif self.game.red_odds.position == 4:
                redthreeodds = 12
                redfourodds = 36
                redfiveodds = 96
            elif self.game.red_odds.position == 5:
                redthreeodds = 16
                redfourodds = 50
                redfiveodds = 96
            elif self.game.red_odds.position == 6:
                redthreeodds = 24
                redfourodds = 64
                redfiveodds = 144
            elif self.game.red_odds.position == 7:
                redthreeodds = 36
                redfourodds = 96
                redfiveodds = 216
            elif self.game.red_odds.position == 8:
                redthreeodds = 64
                redfourodds = 144
                redfiveodds = 300
            elif self.game.red_odds.position == 9:
                redthreeodds = 120
                redfourodds = 240
                redfiveodds = 450
            elif self.game.red_odds.position == 10:
                redthreeodds = 192
                redfourodds = 480
                redfiveodds = 600
            if self.game.yellow_odds.position == 1:
                yellowthreeodds = 4
                yellowfourodds = 16
                yellowfiveodds = 75
            elif self.game.yellow_odds.position == 2:
                yellowthreeodds = 6
                yellowfourodds = 20
                yellowfiveodds = 75
            elif self.game.yellow_odds.position == 3:
                yellowthreeodds = 8
                yellowfourodds = 24
                yellowfiveodds = 96
            elif self.game.yellow_odds.position == 4:
                yellowthreeodds = 12
                yellowfourodds = 36
                yellowfiveodds = 96
            elif self.game.yellow_odds.position == 5:
                yellowthreeodds = 16
                yellowfourodds = 50
                yellowfiveodds = 96
            elif self.game.yellow_odds.position == 6:
                yellowthreeodds = 24
                yellowfourodds = 64
                yellowfiveodds = 144
            elif self.game.yellow_odds.position == 7:
                yellowthreeodds = 36
                yellowfourodds = 96
                yellowfiveodds = 216
            elif self.game.yellow_odds.position == 8:
                yellowthreeodds = 64
                yellowfourodds = 144
                yellowfiveodds = 300
            elif self.game.yellow_odds.position == 9:
                yellowthreeodds = 120
                yellowfourodds = 240
                yellowfiveodds = 450
            elif self.game.yellow_odds.position == 10:
                yellowthreeodds = 192
                yellowfourodds = 480
                yellowfiveodds = 600
            if self.game.green_odds.position == 1:
                greenthreeodds = 4
                greenfourodds = 16
                greenfiveodds = 75
            elif self.game.green_odds.position == 2:
                greenthreeodds = 6
                greenfourodds = 20
                greenfiveodds = 75
            elif self.game.green_odds.position == 3:
                greenthreeodds = 8
                greenfourodds = 24
                greenfiveodds = 96
            elif self.game.green_odds.position == 4:
                greenthreeodds = 12
                greenfourodds = 36
                greenfiveodds = 96
            elif self.game.green_odds.position == 5:
                greenthreeodds = 16
                greenfourodds = 50
                greenfiveodds = 96
            elif self.game.green_odds.position == 6:
                greenthreeodds = 24
                greenfourodds = 64
                greenfiveodds = 144
            elif self.game.green_odds.position == 7:
                greenthreeodds = 36
                greenfourodds = 96
                greenfiveodds = 216
            elif self.game.green_odds.position == 8:
                greenthreeodds = 64
                greenfourodds = 144
                greenfiveodds = 300
            elif self.game.green_odds.position == 9:
                greenthreeodds = 120
                greenfourodds = 240
                greenfiveodds = 450
            elif self.game.green_odds.position == 10:
                greenthreeodds = 192
                greenfourodds = 480
                greenfiveodds = 600
            if self.game.blue_odds.position == 1:
                bluethreeodds = 4
                bluefourodds = 16
                bluefiveodds = 75
            elif self.game.blue_odds.position == 2:
                bluethreeodds = 6
                bluefourodds = 20
                bluefiveodds = 75
            elif self.game.blue_odds.position == 3:
                bluethreeodds = 8
                bluefourodds = 24
                bluefiveodds = 96
            elif self.game.blue_odds.position == 4:
                bluethreeodds = 12
                bluefourodds = 36
                bluefiveodds = 96
            elif self.game.blue_odds.position == 5:
                bluethreeodds = 16
                bluefourodds = 50
                bluefiveodds = 96
            elif self.game.blue_odds.position == 6:
                bluethreeodds = 24
                bluefourodds = 64
                bluefiveodds = 144
            elif self.game.blue_odds.position == 7:
                bluethreeodds = 36
                bluefourodds = 96
                bluefiveodds = 216
            elif self.game.blue_odds.position == 8:
                bluethreeodds = 64
                bluefourodds = 144
                bluefiveodds = 300
            elif self.game.blue_odds.position == 9:
                bluethreeodds = 120
                bluefourodds = 240
                bluefiveodds = 450
            elif self.game.blue_odds.position == 10:
                bluethreeodds = 192
                bluefourodds = 480
                bluefiveodds = 600


            if self.game.double_red.status == True:
                redthreeodds = redthreeodds * 2
                redfourodds = redfourodds * 2
                redfiveodds = redfiveodds * 2
            if self.game.double_yellow.status == True:
                yellowthreeodds = yellowthreeodds * 2
                yellowfourodds = yellowfourodds * 2
                yellowfiveodds = yellowfiveodds * 2
            if self.game.double_green.status == True:
                greenthreeodds = greenthreeodds * 2
                greenfourodds = greenfourodds * 2
                greenfiveodds = greenfiveodds * 2
            if self.game.double_blue.status == True:
                bluethreeodds = bluethreeodds * 2
                bluefourodds = bluefourodds * 2
                bluefiveodds = bluefiveodds * 2

            if relays == 3:
                if stars:
                    if self.game.three_stars.status == True:
                        if self.game.stars_replay_counter.position < 25:
                            self.game.search_index.engage(self.game)
                            self.stars_replay_step_up(25)
                if (red == 1 and relays == 3):
                    if self.game.search_index.status == False:
                        if self.game.red_replay_counter.position < redthreeodds:
                            self.game.search_index.engage(self.game)
                            self.red_replay_step_up(redthreeodds - self.game.red_replay_counter.position)
                if (yellow == 1 and relays == 3):
                    if self.game.search_index.status == False:
                        if self.game.yellow_replay_counter.position < yellowthreeodds:
                            self.game.search_index.engage(self.game)
                            self.yellow_replay_step_up(yellowthreeodds - self.game.yellow_replay_counter.position)
                if (green == 1 and relays == 3):
                    if self.game.search_index.status == False:
                        if self.game.green_replay_counter.position < greenthreeodds:
                            self.game.search_index.engage(self.game)
                            self.green_replay_step_up(greenthreeodds - self.game.green_replay_counter.position)
                if (blue == 1 and relays == 3):
                    if self.game.search_index.status == False:
                        if self.game.blue_replay_counter.position < bluethreeodds:
                            self.game.search_index.engage(self.game)
                            self.blue_replay_step_up(bluethreeodds - self.game.blue_replay_counter.position)
            if relays == 4:
                if stars:
                    if self.game.six_stars.status == True:
                        if self.game.stars_replay_counter.position < 100:
                            self.game.search_index.engage(self.game)
                            self.stars_replay_step_up(100)
                else:
                    if (red == 1 and relays == 4):
                        if self.game.search_index.status == False:
                            if self.game.red_replay_counter.position < redfourodds:
                                self.game.search_index.engage(self.game)
                                self.red_replay_step_up(redfourodds - self.game.red_replay_counter.position)
                    if (yellow == 1 and relays == 4):
                        if self.game.search_index.status == False:
                            if self.game.yellow_replay_counter.position < yellowfourodds:
                                self.game.search_index.engage(self.game)
                                self.yellow_replay_step_up(yellowfourodds - self.game.yellow_replay_counter.position)
                    if (green == 1 and relays == 4):
                        if self.game.search_index.status == False:
                            if self.game.green_replay_counter.position < greenfourodds:
                                self.game.search_index.engage(self.game)
                                self.green_replay_step_up(greenfourodds - self.game.green_replay_counter.position)
                    if (blue == 1 and relays == 4):
                        if self.game.search_index.status == False:
                            if self.game.blue_replay_counter.position < bluefourodds:
                                self.game.search_index.engage(self.game)
                                self.blue_replay_step_up(bluefourodds - self.game.blue_replay_counter.position)
            if relays == 5:
                if (red == 1 and relays == 5):
                    if self.game.search_index.status == False:
                        if self.game.red_replay_counter.position < redfiveodds:
                            self.game.search_index.engage(self.game)
                            self.red_replay_step_up(redfiveodds - self.game.red_replay_counter.position)
                if (yellow == 1 and relays == 5):
                    if self.game.search_index.status == False:
                        if self.game.yellow_replay_counter.position < yellowfiveodds:
                            self.game.search_index.engage(self.game)
                            self.yellow_replay_step_up(yellowfiveodds - self.game.yellow_replay_counter.position)
                if (green == 1 and relays == 5):
                    if self.game.search_index.status == False:
                        if self.game.green_replay_counter.position < greenfiveodds:
                            self.game.search_index.engage(self.game)
                            self.green_replay_step_up(greenfiveodds - self.game.green_replay_counter.position)
                if (blue == 1 and relays == 5):
                    if self.game.search_index.status == False:
                        if self.game.blue_replay_counter.position < bluefiveodds:
                            self.game.search_index.engage(self.game)
                            self.blue_replay_step_up(bluefiveodds - self.game.blue_replay_counter.position)

    def blue_replay_step_up(self, number):
        if number >= 1:
            self.game.blue_replay_counter.step()
            number -= 1
            self.replay_step_up()
            if self.game.replays == 8999:
                number = 0
            self.delay(name="blue_replay_step_up", delay=0.1, handler=self.blue_replay_step_up, param=number)
        else:
            self.game.search_index.disengage()
            self.cancel_delayed(name="blue_replay_step_up")
            self.search()

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
            self.cancel_delayed(name="red_replay_step_up")
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
            self.cancel_delayed(name="yellow_replay_step_up")
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
            self.cancel_delayed(name="green_replay_step_up")
            self.search()

    def stars_replay_step_up(self, number):
        if number >= 1:
            self.game.stars_replay_counter.step()
            number -= 1
            self.replay_step_up()
            if self.game.replays == 8999:
                number = 0
            self.delay(name="stars_replay_step_up", delay=0.1, handler=self.stars_replay_step_up, param=number)
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
        blue = False
        stars = False

        if self.game.line2.position == 0:
            self.p1 = 18
            self.p2 = 4
            self.q1 = 11
            self.q2 = 8
            self.r1 = 15
            self.r2 = 1
            self.s1 = 16
            self.s2 = 14
        elif self.game.line2.position == 1:
            self.p1 = 4
            self.p2 = 18
            self.q1 = 8
            self.q2 = 11
            self.r1 = 1
            self.r2 = 15
            self.s1 = 14
            self.s2 = 16

        if self.game.line1.position in [0,2]:
            self.p3 = 7
            self.q3 = 12
            self.r3 = 20
            self.s3 = 5
        elif self.game.line1.position == 1:
            self.p3 = 5
            self.q3 = 7
            self.r3 = 12
            self.s3 = 20
        elif self.game.line1.position == 3:
            self.p3 = 12
            self.q3 = 20
            self.r3 = 5
            self.s3 = 7

        if self.game.line3.position == 0:
            self.p4 = 9
            self.p5 = 17
            self.q4 = 6
            self.q5 = 13
            self.r4 = 2
            self.r5 = 19
            self.s4 = 3
            self.s5 = 10
        elif self.game.line3.position == 1:
            self.p4 = 17
            self.p5 = 9
            self.q4 = 13
            self.q5 = 6
            self.r4 = 19
            self.r5 = 2
            self.s4 = 10
            self.s5 = 3

        self.pos[0] = {}
        # Blue section
        self.pos[1] = {self.q1:1, self.r1:2, self.s2:3, self.s3:4}
        # Yellow section
        self.pos[2] = {self.p1:1, self.q2:2, self.r3:3, self.s4:4}
        # Red section
        self.pos[3] = {self.p2:1, self.q3:2, self.r4:3, self.s5:4}
        # Green Section
        self.pos[4] = {self.p3:1, self.p4:2, self.q5:3, self.r5:4}
        # Stars
        self.pos[5] = {self.p5:1, self.q4:2, self.r2:3, self.s1:4}

        if rivets == 1:
            blue = True
        if rivets == 2:
            yellow = True
        if rivets == 3:
            red = True
        if rivets == 4:
            green = True
        if rivets == 5:
            stars = True
                
        return (self.pos[rivets], red, yellow, green, blue, stars)

    
    def scan_all(self):
        self.all_probability()

    def all_probability(self):
        if self.game.red_odds.position == 0:
            self.game.red_odds.step()
        if self.game.yellow_odds.position == 0:
            self.game.yellow_odds.step()
        if self.game.green_odds.position == 0:
            self.game.green_odds.step()
        if self.game.blue_odds.position == 0:
            self.game.blue_odds.step()
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
        else:
            if self.game.cu:
                s = random.randint(1,8)
                self.animate_odds_scan(s)
                s = random.randint(1,4)
                self.animate_feature_scan(s)
                self.animate_odds_scan(s)


    def green_extra_step(self, number):
        if number > 0:
            self.game.green_odds.step()
            self.delay(name="display", delay=0.1, handler=graphics.mystic_gate.display, param=self)
            number -= 1
            self.delay(name="extra_step", delay=0.1, handler=self.green_extra_step, param=number)

    def red_extra_step(self, number):
        if number > 0:
            self.game.red_odds.step()
            self.delay(name="display", delay=0.1, handler=graphics.mystic_gate.display, param=self)
            number -= 1
            self.delay(name="extra_step", delay=0.1, handler=self.red_extra_step, param=number)

    def yellow_extra_step(self, number):
        if number > 0:
            self.game.yellow_odds.step()
            self.delay(name="display", delay=0.1, handler=graphics.mystic_gate.display, param=self)
            number -= 1
            self.delay(name="extra_step", delay=0.1, handler=self.yellow_extra_step, param=number)

    def blue_extra_step(self, number):
        if number > 0:
            self.game.blue_odds.step()
            self.delay(name="display", delay=0.1, handler=graphics.mystic_gate.display, param=self)
            number -= 1
            self.delay(name="extra_step", delay=0.1, handler=self.blue_extra_step, param=number)

    def check_extra_step(self):
        i = random.randint(0,32)
        if i == 16:
            return 1
        else:
            return 0

    def scan_features(self):
        p = self.features_probability()

    def features_probability(self):
        s = random.randint(1,4)
        self.animate_feature_scan(s)
        self.features_spotting()

    def features_spotting(self):
        sd = self.game.program.position
        if sd in [23,32,38,49]:
            # Diagram has 5 equidistant wipers on the program disc.  Not sure how those are wired as there's no docs, so I'm playing it safe
            #   33,42,48,9,43,2,8,19,3,12,18,29,13,22,28,49]:
            if self.game.cu:
                self.game.gate.engage(self.game)
            else:
                self.game.selection_feature.step()
        if sd in [13,21,40]:
            # See comment above
            #   ,23,31,0,33,41,10,43,1,20,3,10,30]:
            self.game.six_stars.engage(self.game)
        if sd in [8,19]:
            # See comment above
            #    ,18,29,28,39,38,49,48,9]:
            self.game.three_stars.engage(self.game)
        if sd in [12,13,20,34,45,47]:
            if self.game.mystic_lines.position < 2:
                if self.game.cu:
                    self.step_mystic_lines(6)
                else:
                    self.step_mystic_lines(1)
        if sd in range (21,31):
            if self.game.mystic_lines.position == 2:
                self.step_mystic_lines(1)
            else:
                if self.game.mystic_lines.position < 4:
                    if self.game.cu:
                        self.step_mystic_lines(1)
        if sd in [36,1,32,35,38,44]:
            if self.game.mystic_lines.position == 4:
                self.step_mystic_lines(1)
            else:
                if self.game.mystic_lines.position < 6:
                    if self.game.cu:
                        self.step_mystic_lines(1)

        if sd == 23:
            if self.game.scramble.position in [25,30,36,39,41]:
                if self.game.cu:
                    self.game.double_red.engage(self.game)
        if sd in [26,37]:
            if self.game.scramble.position in [0,6,11,13]:
                if self.game.cu:
                    self.game.double_yellow.engage(self.game)
        if sd == 0:
            if self.game.scramble.position in [0,5,10,44,49]:
                if self.game.cu:
                    self.game.double_green.engage(self.game)
        if sd in [17,34]:
            if self.game.scramble.position in [0,7,41,44,47]:
                if self.game.cu:
                    self.game.double_blue.engage(self.game)
        if sd == 41:
            if self.game.cu:
                if self.game.selection_feature.position < 3:
                    self.step_selection(2)
            else:
                if self.game.selection_feature.position < 3:
                    self.step_selection(1)
        if sd == 30:
            if self.game.cu:
                self.step_selection(6)
            else:
                if self.game.selection_feature.position >= 3:
                    self.step_selection(1)
        if self.game.coin.position in [0,25]:
            self.game.red_odds.step()
            self.game.blue_odds.step()
            self.game.green_odds.step()
            self.game.yellow_odds.step()
        if sd in [0,2,4,5,6,8,9,11,15,19,20,21,23,24,26,31,37,41,42,44,47,49]:
            if self.game.scramble.position in [0,5,11,14,16]:
                self.game.red_odds.step()
        if sd in [47,21,25,27]:
            if self.game.scramble.position in [0,5,11,14,16]:
                self.red_extra_step(2)
        if sd in [28,36]:
            if self.game.scramble.position in [0,5,11,14,16]:
                self.red_extra_step(3)
        if sd in [3,7,10,11,20,22,25,28,36,38,40,46,0]:
            if self.game.scramble.position in [0,6,11,13]:
                self.game.yellow_odds.step()
        if sd in [4,25,27,28,39,32]:
            if self.game.scramble.position in [0,6,11,13]:
                self.yellow_extra_step(2)
        if sd in [1,17,46]:
            if self.game.scramble.position in [0,6,11,13]:
                self.yellow_extra_step(3)
        if sd in [4,5,12,13,18,24,27,29,30,31,32,45,48]:
            if self.game.scramble.position in [0,5,11,45,49]:
                self.game.green_odds.step()
        if sd in [2,14,17,27,29,48]:
            if self.game.scramble.position in [0,5,11,45,49]:
                self.green_extra_step(2)
        if sd in [29,41]:
            if self.game.scramble.position in [0,5,11,45,49]:
                self.green_extra_step(3)
        if sd in [1,3,11,16,18,21,22,31,33,36]:
            if self.game.scramble.position in [0,7,41,44,47]:
                self.game.blue_odds.step()
        if sd in [15,16,33,34,35,37,42]:
            if self.game.scramble.position in [0,7,41,44,47]:
                self.blue_extra_step(2)
        if sd in [9]:
            if self.game.scramble.position in [0,7,41,44,47]:
                self.blue_extra_step(3)

    def step_mystic_lines(self, number):
        if number >= 1:
            self.game.mystic_lines.step()
            number -= 1
            self.delay(name="display", delay=0.1, handler=graphics.mystic_gate.display, param=self)
            self.delay(name="step_sc", delay=0.1, handler=self.step_mystic_lines, param=number)

    def step_selection(self, number):
        if number >= 1:
            self.game.selection_feature.step()
            self.check_selection()
            number -= 1
            self.delay(name="display", delay=0.1, handler=graphics.mystic_gate.display, param=self)
            self.delay(name="step_sc", delay=0.1, handler=self.step_selection, param=number)

    def animate_odds_scan(self, s):
        if s > 1:
            self.delay(name="odds_animation", delay=0.1, handler=graphics.mystic_gate.odds_animation, param=s)
            self.delay(name="display", delay=0.1, handler=graphics.mystic_gate.display, param=self)
            s -= 1
            #self.delay(name="animate_odds", delay=0.1, handler=self.animate_odds_scan, param=s)
        else:
            self.cancel_delayed(name="odds_animation")
            self.cancel_delayed(name="display")

    def animate_feature_scan(self, s):
        if s > 1:
            self.delay(name="feature_animation", delay=0.1, handler=graphics.mystic_gate.feature_animation, param=s)
            self.delay(name="display", delay=0.1, handler=graphics.mystic_gate.display, param=self)
            s -= 1
            #self.delay(name="animate_feature", delay=0.1, handler=self.animate_feature_scan, param=s)
        else:
            self.delay(name="display", delay=0.1, handler=graphics.mystic_gate.display, param=self)

    # Define reset as the knock-off, anti-cheat relay disabled, and replay reset enabled.  Motors turn while credits are knocked off.
    # When meter reaches zero and the zero limit switch is hit, turn off motor sound and leave backglass gi on, but with tilt displayed.

    def startup(self):        
        # Every bingo requires the meter to register '0' 
        # before allowing coin entry --
        # also needs to show a plain 'off' backglass.
        self.eb = False
        self.game.anti_cheat.engage(self.game)
        self.tilt_actions()

class MysticGate(procgame.game.BasicGame):
    """ Mystic Gate was the only 20 hole game with a lifting rebound rubber """
    def __init__(self, machine_type):
        super(MysticGate, self).__init__(machine_type)
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

        self.searchdisc = units.Search("searchdisc", 5)

        #Search relays
        self.s1 = units.Relay("s1")
        self.s2 = units.Relay("s2")
        self.s3 = units.Relay("s3")
        self.s4 = units.Relay("s4")
        self.s5 = units.Relay("s5")
        self.search_index = units.Relay("search_index")

        #Odds steppers
        self.red_odds = units.Stepper("red_odds", 10, 'mystic_gate')
        self.yellow_odds = units.Stepper("yellow_odds", 10, 'mystic_gate')
        self.green_odds = units.Stepper("green_odds", 10, 'mystic_gate')
        self.blue_odds = units.Stepper("blue_odds", 10, 'mystic_gate')

        #Replay Counter
        self.red_replay_counter = units.Stepper("red_replay_counter", 1200)
        self.yellow_replay_counter = units.Stepper("yellow_replay_counter", 1200)
        self.green_replay_counter = units.Stepper("green_replay_counter", 1200)
        self.blue_replay_counter = units.Stepper("blue_replay_counter", 1200)
        self.stars_replay_counter = units.Stepper("stars_replay_counter", 600)
        
        self.selection_feature = units.Stepper("selection_feature", 6)

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

        self.mystic_lines = units.Stepper("mystic_lines", 6)

        self.line1 = units.Stepper("line1", 3, "mystic_gate", "continuous")
        self.line2 = units.Stepper("line2", 1, "mystic_gate", "continuous")
        self.line3 = units.Stepper("line3", 1, "mystic_gate", "continuous")

        self.double_red = units.Relay("double_red")
        self.double_yellow = units.Relay("double_yellow")
        self.double_green = units.Relay("double_green")
        self.double_blue = units.Relay("double_blue")

        self.six_stars = units.Relay("six_stars")
        self.three_stars = units.Relay("three_stars")
        
        self.gate = units.Relay("gate")
        self.gate_open = units.Relay("gate_open")

        self.coin = units.Stepper("coin", 40, "mystic_gate")

        self.replays = 0
        self.returned = False

    def reset(self):
        super(MysticGate, self).reset()
        self.logger = logging.getLogger('game')
        self.load_config('bingo.yaml')
        
        main_mode = SinglecardBingo(self)
        self.modes.add(main_mode)
        
game = MysticGate(machine_type='pdb')
game.reset()
game.run_loop()
