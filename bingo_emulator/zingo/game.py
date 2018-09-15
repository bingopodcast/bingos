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
from bingo_emulator.graphics.zingo import *

class MulticardBingo(procgame.game.Mode):
    def __init__(self, game):
        super(MulticardBingo, self).__init__(game=game, priority=5)
        self.holes = []
        self.game.anti_cheat.engage(self.game)
        self.startup()
        self.game.sound.register_music('motor', "audio/six_card_motor.wav")
        self.game.sound.register_music('search', "audio/old_search.wav")
        self.game.sound.register_sound('add', "audio/six_card_add_card.wav")
        self.game.sound.register_sound('tilt', "audio/tilt.wav")
        self.game.sound.register_sound('step', "audio/step.wav")
        self.game.sound.register_sound('eb_search', "audio/EB_Search.wav")

    def sw_coin_active(self, sw):
        self.game.tilt.disengage()
        self.regular_play()
        self.delay(name="display", delay=0.1, handler=graphics.zingo.display, param=self)

    def sw_startButton_active(self, sw):
        if self.game.replays > 0 or self.game.switches.freeplay.is_active():
            self.regular_play()
            self.delay(name="display", delay=0.1, handler=graphics.zingo.display, param=self)

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
            self.game.ball_count.position -= 1
            self.game.returned = True
            self.check_lifter_status()
        else:
            self.check_lifter_status()

    def sw_enter_active(self, sw):
        if self.game.switches.left.is_active() and self.game.switches.right.is_active():
            self.game.end_run_loop()
            os.system("/home/nbaldridge/proc/bingo_emulator/start_game.sh zingo")

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
        self.game.sound.stop('add')
        self.game.sound.play('add')
        self.game.sound.stop_music()
        self.game.search_index.disengage()
        self.game.coils.counter.pulse()
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
            self.game.card1_replay_counter.reset()
            self.game.card2_replay_counter.reset()
            self.game.card3_replay_counter.reset()
            self.game.selector.reset()
            self.game.ball_count.reset()
            self.game.timer.reset()
            self.regular_play()
            self.check_lifter_status()
        self.delay(name="display", delay=0.1, handler=graphics.zingo.display, param=self)
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
        if (self.game.ball_count.position >= 7 and self.game.switches.trough1.is_inactive()):
            self.game.coils.lifter.disable()

    def sw_ballLift_active_for_500ms(self, sw):
        if self.game.switches.shooter.is_open():
            if self.game.ball_count.position < 5:
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
        if self.game.ball_count.position <= 4:
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
            self.delay(name="display", delay=0.1, handler=graphics.zingo.display, param=self)

    def sw_hole2_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(2)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.zingo.display, param=self)

    def sw_hole3_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(3)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.zingo.display, param=self)

    def sw_hole4_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(4)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.zingo.display, param=self)

    def sw_hole5_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(5)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.zingo.display, param=self)

    def sw_hole6_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(6)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.zingo.display, param=self)

    def sw_hole7_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(7)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.zingo.display, param=self)

    def sw_hole8_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(8)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.zingo.display, param=self)

    def sw_hole9_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(9)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.zingo.display, param=self)

    def sw_hole10_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(10)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.zingo.display, param=self)

    def sw_hole11_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(11)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.zingo.display, param=self)

    def sw_hole12_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(12)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.zingo.display, param=self)

    def sw_hole13_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(13)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.zingo.display, param=self)

    def sw_hole14_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(14)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.zingo.display, param=self)

    def sw_hole15_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(15)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.zingo.display, param=self)

    def sw_hole16_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(16)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.zingo.display, param=self)

    def sw_hole17_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(17)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.zingo.display, param=self)

    def sw_hole18_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(18)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.zingo.display, param=self)

    def sw_hole19_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(19)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.zingo.display, param=self)

    def sw_hole20_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(20)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.zingo.display, param=self)

    def sw_hole21_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(21)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.zingo.display, param=self)

    def sw_hole22_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(22)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.zingo.display, param=self)

    def sw_hole23_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(23)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.zingo.display, param=self)

    def sw_hole24_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(24)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.zingo.display, param=self)

    def sw_hole25_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.holes.append(25)
            if self.game.ball_count.position >= 4:
                if self.game.search_index.status == False:
                    self.search()
            self.delay(name="display", delay=0.1, handler=graphics.zingo.display, param=self)

    def sw_replayReset_active(self, sw):
        self.game.anti_cheat.disengage()
        self.holes = []
        graphics.zingo.display(self)
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
        # displays "Tilt" on the backglass, you have to recoin.
        self.delay(name="display", delay=0.1, handler=graphics.zingo.display, param=self)

    def sw_tilt_active(self, sw):
        if self.game.tilt.status == False:
            self.tilt_actions()

    def replay_step_down(self, number=0):
        if number > 0:
            if number > 1:
                self.game.replays -= 1
                self.game.coils.registerDown.pulse()
                number -= 1
                graphics.zingo.display(self)
                self.delay(name="replay_reset", delay=0.13, handler=self.replay_step_down, param=number)
            elif number == 1:
                self.game.replays -= 1
                self.game.coils.registerDown.pulse()
                number -= 1
                graphics.zingo.display(self)
                self.cancel_delayed(name="replay_reset")
        else: 
            if self.game.replays > 0:
                self.game.replays -= 1
                self.delay(name="display", delay=0.1, handler=graphics.zingo.display, param=self)
            self.game.coils.registerDown.pulse()

    def replay_step_up(self):
        if self.game.replays < 400:
            self.game.replays += 1
            self.game.coils.registerUp.pulse()
            self.game.coils.bell.pulse()
            graphics.zingo.display(self)


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

        for i in range(0, 49): 
            self.r = self.closed_search_relays(self.game.searchdisc.position)
            self.game.searchdisc.spin()
            self.wipers = self.r[0]
            self.card = self.r[1]

            # From here, I need to determine based on the value of r, whether to latch the search index and score. For Coney Island,
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
        if self.game.search_index.status == False and self.game.replays < 400:
            if card == 1:
                if relays == 3:
                    if self.game.card1_replay_counter.position < 4:
                        self.game.search_index.engage(self.game)
                        self.card1_replay_step_up(4 - self.game.card1_replay_counter.position)
                if relays == 4:
                    if self.game.card1_replay_counter.position < 16:
                        self.game.search_index.engage(self.game)
                        self.card1_replay_step_up(16 - self.game.card1_replay_counter.position)
                if relays == 5:
                    if self.game.card1_replay_counter.position < 100:
                        self.game.search_index.engage(self.game)
                        self.card1_replay_step_up(100 - self.game.card1_replay_counter.position)
            if card == 2:
                if relays == 3:
                    if self.game.card2_replay_counter.position < 4:
                        self.game.search_index.engage(self.game)
                        self.card2_replay_step_up(4 - self.game.card2_replay_counter.position)
                if relays == 4:
                    if self.game.card2_replay_counter.position < 16:
                        self.game.search_index.engage(self.game)
                        self.card2_replay_step_up(16 - self.game.card2_replay_counter.position)
                if relays == 5:
                    if self.game.card2_replay_counter.position < 100:
                        self.game.search_index.engage(self.game)
                        self.card2_replay_step_up(100 - self.game.card2_replay_counter.position)
            if card == 3:
                if relays == 3:
                    if self.game.card3_replay_counter.position < 4:
                        self.game.search_index.engage(self.game)
                        self.card3_replay_step_up(4 - self.game.card3_replay_counter.position)
                if relays == 4:
                    if self.game.card3_replay_counter.position < 16:
                        self.game.search_index.engage(self.game)
                        self.card3_replay_step_up(16 - self.game.card3_replay_counter.position)
                if relays == 5:
                    if self.game.card3_replay_counter.position < 100:
                        self.game.search_index.engage(self.game)
                        self.card3_replay_step_up(100 - self.game.card3_replay_counter.position)

    def card1_replay_step_up(self, number):
        self.game.sound.stop_music()
        if self.game.replays < 400 and number >= 1:
            self.game.card1_replay_counter.step()
            number -= 1
            self.replay_step_up()
            self.delay(name="card1_replay_step_up", delay=0.1, handler=self.card1_replay_step_up, param=number)
        else:
            self.game.search_index.disengage()
            self.cancel_delayed(name="card1_replay_step_up")
            self.search()

    def card2_replay_step_up(self, number):
        self.game.sound.stop_music()
        if self.game.replays < 400 and number >= 1:
            self.game.card2_replay_counter.step()
            number -= 1
            self.replay_step_up()
            self.delay(name="card2_replay_step_up", delay=0.1, handler=self.card2_replay_step_up, param=number)
        else:
            self.game.search_index.disengage()
            self.cancel_delayed(name="card2_replay_step_up")
            self.search()

    def card3_replay_step_up(self, number):
        self.game.sound.stop_music()
        if self.game.replays < 400 and number >= 1:
            self.game.card3_replay_counter.step()
            number -= 1
            self.replay_step_up()
            self.delay(name="card3_replay_step_up", delay=0.1, handler=self.card3_replay_step_up, param=number)
        else:
            self.game.search_index.disengage()
            self.cancel_delayed(name="card3_replay_step_up")
            self.search()

    def closed_search_relays(self, rivets):
        # This function is critical, as it will determine which card is returned, etc.  I need to check both the position of the
        # replay counter for the card, as well as the selector unit to ensure that the card is selected. We will get a row back
        # that has the numbers on the position which will return the search relay connected.  When three out of the five relays
        # are connected, we get a winner!
        
        self.pos = {}
        # Card 1
        self.pos[0] = {}
        self.pos[1] = {1:1, 8:2, 22:3, 18:4, 6:5}
        self.pos[2] = {7:1, 24:2, 17:3, 4:4, 23:5}
        self.pos[3] = {13:1, 20:2, 3:3, 15:4, 10:5}
        self.pos[4] = {21:1, 14:2, 11:3, 9:4, 2:5}
        self.pos[5] = {5:1, 25:2, 16:3, 19:4, 12:5}
        self.pos[6] = {1:1, 7:2, 13:3, 21:4, 5:5}
        self.pos[7] = {8:1, 24:2, 20:3, 14:4, 25:5}
        self.pos[8] = {22:1, 17:2, 3:3, 11:4, 16:5}
        self.pos[9] = {18:1, 4:2, 15:3, 9:4, 19:5}
        self.pos[10] = {6:1, 23:2, 10:3, 2:4, 12:5}
        self.pos[11] = {}
        self.pos[12] = {}
        self.pos[13] = {}
        self.pos[14] = {}
        self.pos[15] = {}
        self.pos[16] = {}
        self.pos[17] = {}

        # There are five blank positions in between cards.  Early games have less to search!
        # Card 2
        self.pos[18] = {7:1, 13:2, 9:3, 3:4, 20:5}
        self.pos[19] = {19:1, 23:2, 14:3, 16:4, 2:5}
        self.pos[20] = {21:1, 25:2, 5:3, 10:4, 18:5}
        self.pos[21] = {4:1, 6:2, 12:3, 22:4, 24:5}
        self.pos[22] = {11:1, 8:2, 17:3, 1:4, 15:5}
        self.pos[23] = {7:1, 19:2, 21:3, 4:4, 11:5}
        self.pos[24] = {13:1, 23:2, 25:3, 6:4, 8:5}
        self.pos[25] = {9:1, 14:2, 5:3, 12:4, 17:5}
        self.pos[26] = {3:1, 16:2, 10:3, 22:4, 1:5}
        self.pos[27] = {20:1, 2:2, 18:3, 24:4, 15:5}
        self.pos[28] = {}
        self.pos[29] = {}
        self.pos[30] = {}
        self.pos[31] = {}
        self.pos[32] = {}
        self.pos[33] = {}
        self.pos[34] = {}

        # Another five blank positions.  Can you believe it?
        # Card 3
        self.pos[35] = {17:1, 9:2, 20:3, 4:4, 10:5}
        self.pos[36] = {12:1, 23:2, 6:3, 21:4, 16:5}
        self.pos[37] = {8:1, 19:2, 1:3, 7:4, 24:5}
        self.pos[38] = {22:1, 15:2, 11:3, 2:4, 13:5}
        self.pos[39] = {14:1, 5:2, 18:3, 25:4, 3:5}
        self.pos[40] = {17:1, 12:2, 8:3, 22:4, 14:5}
        self.pos[41] = {9:1, 23:2, 19:3, 15:4, 5:5}
        self.pos[42] = {20:1, 6:2, 1:3, 11:4, 18:5}
        self.pos[43] = {4:1, 21:2, 7:3, 2:4, 25:5}
        self.pos[44] = {10:1, 16:2, 24:3, 13:4, 3:5}
        self.pos[45] = {}
        self.pos[46] = {}
        self.pos[47] = {}
        self.pos[48] = {}
        self.pos[49] = {}
        self.pos[50] = {}

        if rivets in range(0,18):
            card = 1
        if rivets in range(18,35):
            card = 2
        if rivets in range(35,50):
            card = 3

        return (self.pos[rivets], card)
            
    # Define reset as the knock-off, anti-cheat relay disabled, and replay reset enabled.  Motors turn while credits are knocked off.
    # When meter reaches zero and the zero limit switch is hit, turn off motor sound and leave backglass gi on, but with tilt displayed.

    def startup(self):        
        self.tilt_actions()

class Zingo(procgame.game.BasicGame):
    """ Zingo was one of the first games United produced using the standard Bally playfield layout """
    def __init__(self, machine_type):
        super(Zingo, self).__init__(machine_type)
        pygame.mixer.pre_init(44100,-16,2,512)
        self.sound = procgame.sound.SoundController(self)
        self.sound.set_volume(1.0)
        # NOTE: trough_count only counts the number of switches present in the  trough.  It does _not_ count
        #       the number of balls present.   In this game, there  should  be  8  balls.
        self.trough_count = 6

        # Subclass my units unique to this game -  modifications must be made to set up mixers and steppers unique to the game
        # NOTE: 'top' positions are indexed using a 0 index, so the top on a 24 position unit is actually 23.

        self.searchdisc = units.Search("searchdisc", 49)

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

        #Initialize stepper units used to keep track of features or timing.
        self.selector = units.Stepper("selector", 3)
        self.timer = units.Stepper("timer", 40)
        self.ball_count = units.Stepper("ball_count", 7)

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

        self.replays = 0
        self.returned = False

    def reset(self):
        super(Zingo, self).reset()
        self.logger = logging.getLogger('game')
        self.load_config('bingo.yaml')
        
        main_mode = MulticardBingo(self)
        self.modes.add(main_mode)

game = Zingo(machine_type='pdb')
game.reset()
game.run_loop()
