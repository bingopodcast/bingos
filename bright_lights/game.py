#!/usr/bin/python

import logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
import pinproc
import procgame.game, sys, os
import procgame.config
import threading
import time

sys.path.insert(0,os.path.pardir)
from bingo_emulator.units import units
from bingo_emulator.graphics import methods as graphics
from bingo_emulator.graphics.bright_lights import *

from modes.timeout import Timeout

class MulticardBingo(procgame.game.Mode):
    def __init__(self, game):
        super(MulticardBingo, self).__init__(game=game, priority=5)
        self.holes = []
        self.startup()

    def sw_coin_active(self, sw):
        self.regular_play()
        graphics.bright_lights.display(self.holes, self.game.selector.position, True, False)

    def sw_startButton_active(self, sw):
        if self.game.replays > 0:
            self.regular_play()
            graphics.bright_lights.display(self.holes, self.game.selector.position, True, False)

    def regular_play(self):
        if self.game.ball_count.position >= 1:
            if self.game.switches.shutter.is_active():
                self.game.coils.shutter.pulse()
            self.game.selector.reset()
            self.game.ball_count.reset()
        if self.game.selector.position < 6:
            self.game.selector.step()
        else:
            if self.game.switches.shutter.is_active():
                self.game.coils.shutter.pulse()
            self.game.selector.reset()
            self.game.ball_count.reset()
            self.game.selector.step()
        self.replay_step_down()
        if self.game.switches.shooter.is_inactive():
            self.game.coils.lifter.pulse()

    def sw_shooter_active(self, sw):
        self.game.ball_count.step()
        
    def sw_gate_inactive(self, sw):
        if self.game.switches.shooter.is_inactive():
            if self.game.ball_count.position < 5:
                self.game.coils.lifter.pulse()
                self.game.ball_count.step()

    # This is really nasty, but it is how we render graphics for each individual hole.
    # numbers are added (or removed from) a list.  In this way, I can re-use the same
    # routine even for games where there are ball return functions like Surf Club.

    def sw_hole1_active(self, sw):
        self.holes.append(1)
        graphics.bright_lights.display(self.holes, self.game.selector.position, True, False)
        self.search(self.holes)

    def sw_hole1_inactive(self, sw):
        self.holes.remove(1)
        graphics.bright_lights.display(self.holes, self.game.selector.position, True, False)

    def sw_hole2_active(self, sw):
        self.holes.append(2)
        graphics.bright_lights.display(self.holes, self.game.selector.position, True, False)
        self.search(self.holes)

    def sw_hole2_inactive(self, sw):
        self.holes.remove(2)
        graphics.bright_lights.display(self.holes, self.game.selector.position, True, False)

    def sw_hole3_active(self, sw):
        self.holes.append(3)
        graphics.bright_lights.display(self.holes, self.game.selector.position, True, False)
        self.search(self.holes)

    def sw_hole3_inactive(self, sw):
        self.holes.remove(3)
        graphics.bright_lights.display(self.holes, self.game.selector.position, True, False)

    def sw_hole4_active(self, sw):
        self.holes.append(4)
        graphics.bright_lights.display(self.holes, self.game.selector.position, True, False)
        self.search(self.holes)

    def sw_hole4_inactive(self, sw):
        self.holes.remove(4)
        graphics.bright_lights.display(self.holes, self.game.selector.position, True, False)

    def sw_hole5_active(self, sw):
        self.holes.append(5)
        graphics.bright_lights.display(self.holes, self.game.selector.position, True, False)
        self.search(self.holes)

    def sw_hole5_inactive(self, sw):
        self.holes.remove(5)
        graphics.bright_lights.display(self.holes, self.game.selector.position, True, False)

    def sw_hole6_active(self, sw):
        self.holes.append(6)
        graphics.bright_lights.display(self.holes, self.game.selector.position, True, False)
        self.search(self.holes)

    def sw_hole6_inactive(self, sw):
        self.holes.remove(6)
        graphics.bright_lights.display(self.holes, self.game.selector.position, True, False)

    def sw_hole7_active(self, sw):
        self.holes.append(7)
        graphics.bright_lights.display(self.holes, self.game.selector.position, True, False)
        self.search(self.holes)

    def sw_hole7_inactive(self, sw):
        self.holes.remove(7)
        graphics.bright_lights.display(self.holes, self.game.selector.position, True, False)

    def sw_hole8_active(self, sw):
        self.holes.append(8)
        graphics.bright_lights.display(self.holes, self.game.selector.position, True, False)
        self.search(self.holes)

    def sw_hole8_inactive(self, sw):
        self.holes.remove(8)
        graphics.bright_lights.display(self.holes, self.game.selector.position, True, False)

    def sw_hole9_active(self, sw):
        self.holes.append(9)
        graphics.bright_lights.display(self.holes, self.game.selector.position, True, False)
        self.search(self.holes)

    def sw_hole9_inactive(self, sw):
        self.holes.remove(9)
        graphics.bright_lights.display(self.holes, self.game.selector.position, True, False)

    def sw_hole10_active(self, sw):
        self.holes.append(10)
        graphics.bright_lights.display(self.holes, self.game.selector.position, True, False)
        self.search(self.holes)

    def sw_hole10_inactive(self, sw):
        self.holes.remove(10)
        graphics.bright_lights.display(self.holes, self.game.selector.position, True, False)

    def sw_hole11_active(self, sw):
        self.holes.append(11)
        graphics.bright_lights.display(self.holes, self.game.selector.position, True, False)
        self.search(self.holes)

    def sw_hole11_inactive(self, sw):
        self.holes.remove(11)
        graphics.bright_lights.display(self.holes, self.game.selector.position, True, False)

    def sw_hole12_active(self, sw):
        self.holes.append(12)
        graphics.bright_lights.display(self.holes, self.game.selector.position, True, False)
        self.search(self.holes)

    def sw_hole12_inactive(self, sw):
        self.holes.remove(12)
        graphics.bright_lights.display(self.holes, self.game.selector.position, True, False)

    def sw_hole13_active(self, sw):
        self.holes.append(13)
        graphics.bright_lights.display(self.holes, self.game.selector.position, True, False)
        self.search(self.holes)

    def sw_hole13_inactive(self, sw):
        self.holes.remove(13)
        graphics.bright_lights.display(self.holes, self.game.selector.position, True, False)

    def sw_hole14_active(self, sw):
        self.holes.append(14)
        graphics.bright_lights.display(self.holes, self.game.selector.position, True, False)
        self.search(self.holes)

    def sw_hole14_inactive(self, sw):
        self.holes.remove(14)
        graphics.bright_lights.display(self.holes, self.game.selector.position, True, False)

    def sw_hole15_active(self, sw):
        self.holes.append(15)
        graphics.bright_lights.display(self.holes, self.game.selector.position, True, False)
        self.search(self.holes)

    def sw_hole15_inactive(self, sw):
        self.holes.remove(15)
        graphics.bright_lights.display(self.holes, self.game.selector.position, True, False)

    def sw_hole16_active(self, sw):
        self.holes.append(16)
        graphics.bright_lights.display(self.holes, self.game.selector.position, True, False)
        self.search(self.holes)

    def sw_hole16_inactive(self, sw):
        self.holes.remove(16)
        graphics.bright_lights.display(self.holes, self.game.selector.position, True, False)

    def sw_hole17_active(self, sw):
        self.holes.append(17)
        graphics.bright_lights.display(self.holes, self.game.selector.position, True, False)
        self.search(self.holes)

    def sw_hole17_inactive(self, sw):
        self.holes.remove(17)
        graphics.bright_lights.display(self.holes, self.game.selector.position, True, False)

    def sw_hole18_active(self, sw):
        self.holes.append(18)
        graphics.bright_lights.display(self.holes, self.game.selector.position, True, False)
        self.search(self.holes)

    def sw_hole18_inactive(self, sw):
        self.holes.remove(18)
        graphics.bright_lights.display(self.holes, self.game.selector.position, True, False)

    def sw_hole19_active(self, sw):
        self.holes.append(19)
        graphics.bright_lights.display(self.holes, self.game.selector.position, True, False)
        self.search(self.holes)

    def sw_hole19_inactive(self, sw):
        self.holes.remove(19)
        graphics.bright_lights.display(self.holes, self.game.selector.position, True, False)

    def sw_hole20_active(self, sw):
        self.holes.append(20)
        graphics.bright_lights.display(self.holes, self.game.selector.position, True, False)
        self.search(self.holes)

    def sw_hole20_inactive(self, sw):
        self.holes.remove(20)
        graphics.bright_lights.display(self.holes, self.game.selector.position, True, False)

    def sw_hole21_active(self, sw):
        self.holes.append(21)
        graphics.bright_lights.display(self.holes, self.game.selector.position, True, False)
        self.search(self.holes)

    def sw_hole21_inactive(self, sw):
        self.holes.remove(21)
        graphics.bright_lights.display(self.holes, self.game.selector.position, True, False)

    def sw_hole22_active(self, sw):
        self.holes.append(22)
        graphics.bright_lights.display(self.holes, self.game.selector.position, True, False)
        self.search(self.holes)

    def sw_hole22_inactive(self, sw):
        self.holes.remove(22)
        graphics.bright_lights.display(self.holes, self.game.selector.position, True, False)

    def sw_hole23_active(self, sw):
        self.holes.append(23)
        graphics.bright_lights.display(self.holes, self.game.selector.position, True, False)
        self.search(self.holes)

    def sw_hole23_inactive(self, sw):
        self.holes.remove(23)
        graphics.bright_lights.display(self.holes, self.game.selector.position, True, False)

    def sw_hole24_active(self, sw):
        self.holes.append(24)
        graphics.bright_lights.display(self.holes, self.game.selector.position, True, False)
        self.search(self.holes)

    def sw_hole24_inactive(self, sw):
        self.holes.remove(24)
        graphics.bright_lights.display(self.holes, self.game.selector.position, True, False)

    def sw_hole25_active(self, sw):
        self.holes.append(25)
        graphics.bright_lights.display(self.holes, self.game.selector.position, True, False)
        self.search(self.holes)

    def sw_hole25_inactive(self, sw):
        self.holes.remove(25)
        graphics.bright_lights.display(self.holes, self.game.selector.position, True, False)

    def replay_reset(self):
        if self.game.switches.replay0.is_inactive():
            self.game.coils.sounder.pulse()

    def tilt_actions(self):
        if self.game.switches.shutter.is_inactive():
            self.game.coils.shutterMotor.pulse()
        self.holes = []
        self.game.selector.reset()
        self.game.ball_count.reset()
        self.game.tilt.engage(self.game)
        # displays "Tilt" on the backglass, you have to recoin.
        graphics.bright_lights.display(self.holes, self.game.selector.position, True, True)
        self.game.modes.remove(Timeout)

    def sw_trough4_inactive(self, sw):
        self.game.modes.add(Timeout(self.game, 7))

    def sw_yellow_active(self, sw):
        if self.game.switches.left.is_active() and self.game.switches.right.is_active():
            self.game.end_run_loop()
            import menu
            menu.main()

    def sw_tilt_active(self, sw):
        self.tilt_actions()
   
    def replay_step_down(self):
        if self.game.replays > 0:
            self.game.replays -= 1
            graphics.replay_step_down(self.game.replays, graphics.bright_lights.reel1, graphics.bright_lights.reel10, graphics.bright_lights.reel100)
            self.game.coils.sounder.pulse()

    def replay_step_up(self):
        graphics.replay_step_up(self.game.replays, graphics.bright_lights.reel1, graphics.bright_lights.reel10, graphics.bright_lights.reel100)
        self.game.replays += 1
        self.game.coils.sounder.pulse()
        graphics.bright_lights.display(self.holes, self.game.selector.position, True, False)

    def search(self, n):
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
                        for i in relays:
                            pass
                        s = count_seq(relays)
                        if self.game.selector.position >= self.card:
                            self.find_winner(s, self.card)

    def find_winner(self, relays, card):
        if card == 1:
            if relays == 3:
                if self.game.card1_replay_counter.position < 4:
                    while self.game.card1_replay_counter.position < 4:
                        self.game.card1_replay_counter.step()
                        self.replay_step_up()

            if relays == 4:
                if self.game.card1_replay_counter.position < 16:
                    while self.game.card1_replay_counter.position < 16:
                        self.game.card1_replay_counter.step()
                        self.replay_step_up()
            if relays == 5:
                if self.game.card1_replay_counter.position < 100:
                    while self.game.card1_replay_counter.position < 100:
                        self.game.card1_replay_counter.step()
                        self.replay_step_up()
        if card == 2:
            if relays == 3:
                if self.game.card2_replay_counter.position < 4:
                    while self.game.card2_replay_counter.position < 4:
                        self.game.card2_replay_counter.step()
                        self.replay_step_up()
            if relays == 4:
                if self.game.card2_replay_counter.position < 16:
                    while self.game.card2_replay_counter.position < 16:
                        self.game.card2_replay_counter.step()
                        self.replay_step_up()
            if relays == 5:
                if self.game.card2_replay_counter.position < 100:
                    while self.game.card2_replay_counter.position < 100:
                        self.game.card2_replay_counter.step()
                        self.replay_step_up()
        if card == 3:
            if relays == 3:
                if self.game.card3_replay_counter.position < 4:
                    while self.game.card3_replay_counter.position < 4:
                        self.game.card3_replay_counter.step()
                        self.replay_step_up()
            if relays == 4:
                if self.game.card3_replay_counter.position < 16:
                    while self.game.card3_replay_counter.position < 16:
                        self.game.card3_replay_counter.step()
                        self.replay_step_up()
            if relays == 5:
                if self.game.card3_replay_counter.position < 100:
                    while self.game.card3_replay_counter.position < 100:
                        self.game.card3_replay_counter.step()
                        self.replay_step_up()
        if card == 4:
            if relays == 3:
                if self.game.card4_replay_counter.position < 4:
                    while self.game.card4_replay_counter.position < 4:
                        self.game.card4_replay_counter.step()
                        self.replay_step_up()
            if relays == 4:
                if self.game.card4_replay_counter.position < 16:
                    while self.game.card4_replay_counter.position < 16:
                        self.game.card4_replay_counter.step()
                        self.replay_step_up()
            if relays == 5:
                if self.game.card4_replay_counter.position < 100:
                    while self.game.card4_replay_counter.position < 100:
                        self.game.card4_replay_counter.step()
                        self.replay_step_up()
        if card == 5:
            if relays == 3:
                if self.game.card5_replay_counter.position < 4:
                    while self.game.card5_replay_counter.position < 4:
                        self.game.card5_replay_counter.step()
                        self.replay_step_up()
            if relays == 4:
                if self.game.card5_replay_counter.position < 16:
                    while self.game.card5_replay_counter.position < 16:
                        self.game.card5_replay_counter.step()
                        self.replay_step_up()
            if relays == 5:
                if self.game.card5_replay_counter.position < 100:
                    while self.game.card5_replay_counter.position < 100:
                        self.game.card5_replay_counter.step()
                        self.replay_step_up()
        if card == 6:
            if relays == 3:
                if self.game.card6_replay_counter.position < 4:
                    while self.game.card6_replay_counter.position < 4:
                        self.game.card6_replay_counter.step()
                        self.replay_step_up()
            if relays == 4:
                if self.game.card6_replay_counter.position < 16:
                    while self.game.card6_replay_counter.position < 16:
                        self.game.card6_replay_counter.step()
                        self.replay_step_up()
            if relays == 5:
                if self.game.card6_replay_counter.position < 100:
                    while self.game.card6_replay_counter.position < 100:
                        self.game.card6_replay_counter.step()
                        self.replay_step_up()

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
        self.pos[25] = {16:1, 15:2, 15:3, 11:4, 5:5}
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
        self.pos[51] = {6:1, 7:2, 3:3, 24:4, 1:5}
        self.pos[52] = {23:1, 14:2, 12:3, 18:4, 2:5}
        self.pos[53] = {5:1, 19:2, 20:3, 16:4, 22:5}
        self.pos[54] = {11:1, 17:2, 9:3, 15:4, 25:5}
        self.pos[55] = {10:1, 13:2, 21:3, 4:4, 8:5}
        self.pos[56] = {6:1, 23:2, 5:3, 11:4, 10:5}
        self.pos[57] = {7:1, 14:2, 19:3, 17:4, 13:5}
        self.pos[58] = {3:1, 12:2, 20:3, 9:4, 21:5}
        self.pos[59] = {24:1, 18:2, 16:3, 15:4, 4:5}
        self.pos[60] = {1:1, 2:2, 22:3, 25:4, 8:5}
        self.pos[61] = {6:1, 14:2, 20:3, 15:4, 8:5}
        self.pos[62] = {1:1, 18:2, 20:3, 17:4, 10:5}
        self.pos[63] = {}
        self.pos[64] = {}
        self.pos[65] = {}
        self.pos[66] = {}
        self.pos[67] = {}

        # Card #5
        self.pos[68] = {8:1, 23:2, 10:3, 13:4, 4:5}
        self.pos[69] = {2:1, 17:2, 16:3, 14:4, 24:5}
        self.pos[70] = {20:1, 12:2, 22:3, 19:4, 5:5}
        self.pos[71] = {25:1, 15:2, 9:3, 18:4, 11:5}
        self.pos[72] = {1:1, 7:2, 21:3, 3:4, 6:5}
        self.pos[73] = {8:1, 2:2, 20:3, 25:4, 1:5}
        self.pos[74] = {23:1, 17:2, 12:3, 15:4, 7:5}
        self.pos[75] = {10:1, 16:2, 22:3, 9:4, 21:5}
        self.pos[76] = {13:1, 14:2, 19:3, 18:4, 3:5}
        self.pos[77] = {4:1, 24:2, 5:3, 11:4, 6:5}
        self.pos[78] = {8:1, 17:2, 22:3, 18:4, 6:5}
        self.pos[79] = {4:1, 14:2, 22:3, 15:4, 1:1}
        self.pos[80] = {}
        self.pos[81] = {}
        self.pos[82] = {}
        self.pos[83] = {}
        self.pos[84] = {}

        # Card #6
        self.pos[85] = {4:1, 6:2, 1:3, 23:4, 5:5}
        self.pos[86] = {25:1, 15:2, 3:3, 17:4, 13:5}
        self.pos[87] = {9:1, 19:2, 21:3, 12:4, 20:5}
        self.pos[88] = {10:1, 18:2, 16:3, 14:4, 8:5}
        self.pos[89] = {7:1, 24:2, 22:3, 2:4, 11:5}
        self.pos[90] = {4:1, 25:2, 9:3, 10:4, 7:5}
        self.pos[91] = {6:1, 15:2, 19:3, 18:4, 24:5}
        self.pos[92] = {1:1, 3:2, 21:3, 16:4, 22:5}
        self.pos[93] = {23:1, 17:2, 12:3, 14:4, 2:5}
        self.pos[94] = {5:1, 13:2, 20:3, 8:4, 11:5}
        self.pos[95] = {4:1, 15:2, 21:3, 14:4, 11:5}
        self.pos[96] = {5:1, 17:2, 21:3, 18:4, 7:5}
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


class BrightLights(procgame.game.BasicGame):
    """ Bright Lights was the first bingo produced by Bally """
    def __init__(self, machine_type):
        super(BrightLights, self).__init__(machine_type)
        # NOTE: trough_count only counts the number of switches present in the  trough.  It does _not_ count
        #       the number of balls present.   In this game, there  should  be  8  balls.
        self.trough_count = 6

        # Subclass my units unique to this game -  modifications must be made to set up mixers and steppers unique to the game
        # NOTE: 'top' positions are indexed using a 0 index, so the top on a 24 position unit is actually 23.

        self.searchdisc = units.Search("searchdisc", 49)
        self.searchdisc2 = units.Search("searchdisc2", 49)

        #Seach relays
        self.s1 = units.Relay("s1")
        self.s2 = units.Relay("s2")
        self.s3 = units.Relay("s3")
        self.s4 = units.Relay("s4")
        self.s5 = units.Relay("s5")

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
        self.ball_count = units.Stepper("ball_count", 5)

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

    def reset(self):
        super(BrightLights, self).reset()
        self.logger = logging.getLogger('game')
        self.load_config('bright_lights.yaml')
        
        main_mode = MulticardBingo(self)
        self.modes.add(main_mode)
        
#        search = Search(self)
#        self.modes.add(search)


def count_seq(nums):
    hits = 0
    for i, num in enumerate(nums):
        try:
            nxt = nums[i + 1]
        except IndexError:
            nxt = None

        try:
            prev = nums[i - 1]
        except IndexError:
            prev = None

        if (nxt == (num + 1)) or (prev == (num - 1)):
            hits += 1
    return hits

game = BrightLights(machine_type='pdb')
game.reset()
game.run_loop()
