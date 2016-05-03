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
from bingo_emulator.graphics.zingo import *

from modes.timeout import Timeout

class MulticardBingo(procgame.game.Mode):
    def __init__(self, game):
        super(MulticardBingo, self).__init__(game=game, priority=5)
        self.holes = []
        self.startup()

    def sw_coin_active(self, sw):
        self.regular_play()
        graphics.zingo.display(self.holes, self.game.selector.position, True, False, self.game.replays)

    def sw_startButton_active(self, sw):
        if self.game.replays > 0:
            self.regular_play()
            self.game.extra_ball.reset()
            graphics.zingo.display(self.holes, self.game.selector.position, True, False, self.game.replays)

    def regular_play(self):
        if self.game.ball_count.position >= 1:
            if self.game.switches.shutter.is_active():
                self.game.coils.shutter.pulse()
            self.game.selector.reset()
            self.game.ball_count.reset()
        if self.game.selector.position < 3:
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
        graphics.zingo.display(self.holes, self.game.selector.position, True, False, self.game.replays)
        self.search(self.holes)

    def sw_hole1_inactive(self, sw):
        self.holes.remove(1)
        graphics.zingo.display(self.holes, self.game.selector.position, True, False, self.game.replays)

    def sw_hole2_active(self, sw):
        self.holes.append(2)
        graphics.zingo.display(self.holes, self.game.selector.position, True, False, self.game.replays)
        self.search(self.holes)

    def sw_hole2_inactive(self, sw):
        self.holes.remove(2)
        graphics.zingo.display(self.holes, self.game.selector.position, True, False, self.game.replays)

    def sw_hole3_active(self, sw):
        self.holes.append(3)
        graphics.zingo.display(self.holes, self.game.selector.position, True, False, self.game.replays)
        self.search(self.holes)

    def sw_hole3_inactive(self, sw):
        self.holes.remove(3)
        graphics.zingo.display(self.holes, self.game.selector.position, True, False, self.game.replays)

    def sw_hole4_active(self, sw):
        self.holes.append(4)
        graphics.zingo.display(self.holes, self.game.selector.position, True, False, self.game.replays)
        self.search(self.holes)

    def sw_hole4_inactive(self, sw):
        self.holes.remove(4)
        graphics.zingo.display(self.holes, self.game.selector.position, True, False, self.game.replays)

    def sw_hole5_active(self, sw):
        self.holes.append(5)
        graphics.zingo.display(self.holes, self.game.selector.position, True, False, self.game.replays)
        self.search(self.holes)

    def sw_hole5_inactive(self, sw):
        self.holes.remove(5)
        graphics.zingo.display(self.holes, self.game.selector.position, True, False, self.game.replays)

    def sw_hole6_active(self, sw):
        self.holes.append(6)
        graphics.zingo.display(self.holes, self.game.selector.position, True, False, self.game.replays)
        self.search(self.holes)

    def sw_hole6_inactive(self, sw):
        self.holes.remove(6)
        graphics.zingo.display(self.holes, self.game.selector.position, True, False, self.game.replays)

    def sw_hole7_active(self, sw):
        self.holes.append(7)
        graphics.zingo.display(self.holes, self.game.selector.position, True, False, self.game.replays)
        self.search(self.holes)

    def sw_hole7_inactive(self, sw):
        self.holes.remove(7)
        graphics.zingo.display(self.holes, self.game.selector.position, True, False, self.game.replays)

    def sw_hole8_active(self, sw):
        self.holes.append(8)
        graphics.zingo.display(self.holes, self.game.selector.position, True, False, self.game.replays)
        self.search(self.holes)

    def sw_hole8_inactive(self, sw):
        self.holes.remove(8)
        graphics.zingo.display(self.holes, self.game.selector.position, True, False, self.game.replays)

    def sw_hole9_active(self, sw):
        self.holes.append(9)
        graphics.zingo.display(self.holes, self.game.selector.position, True, False, self.game.replays)
        self.search(self.holes)

    def sw_hole9_inactive(self, sw):
        self.holes.remove(9)
        graphics.zingo.display(self.holes, self.game.selector.position, True, False, self.game.replays)

    def sw_hole10_active(self, sw):
        self.holes.append(10)
        graphics.zingo.display(self.holes, self.game.selector.position, True, False, self.game.replays)
        self.search(self.holes)

    def sw_hole10_inactive(self, sw):
        self.holes.remove(10)
        graphics.zingo.display(self.holes, self.game.selector.position, True, False, self.game.replays)

    def sw_hole11_active(self, sw):
        self.holes.append(11)
        graphics.zingo.display(self.holes, self.game.selector.position, True, False, self.game.replays)
        self.search(self.holes)

    def sw_hole11_inactive(self, sw):
        self.holes.remove(11)
        graphics.zingo.display(self.holes, self.game.selector.position, True, False, self.game.replays)

    def sw_hole12_active(self, sw):
        self.holes.append(12)
        graphics.zingo.display(self.holes, self.game.selector.position, True, False, self.game.replays)
        self.search(self.holes)

    def sw_hole12_inactive(self, sw):
        self.holes.remove(12)
        graphics.zingo.display(self.holes, self.game.selector.position, True, False, self.game.replays)

    def sw_hole13_active(self, sw):
        self.holes.append(13)
        graphics.zingo.display(self.holes, self.game.selector.position, True, False, self.game.replays)
        self.search(self.holes)

    def sw_hole13_inactive(self, sw):
        self.holes.remove(13)
        graphics.zingo.display(self.holes, self.game.selector.position, True, False, self.game.replays)

    def sw_hole14_active(self, sw):
        self.holes.append(14)
        graphics.zingo.display(self.holes, self.game.selector.position, True, False, self.game.replays)
        self.search(self.holes)

    def sw_hole14_inactive(self, sw):
        self.holes.remove(14)
        graphics.zingo.display(self.holes, self.game.selector.position, True, False, self.game.replays)

    def sw_hole15_active(self, sw):
        self.holes.append(15)
        graphics.zingo.display(self.holes, self.game.selector.position, True, False, self.game.replays)
        self.search(self.holes)

    def sw_hole15_inactive(self, sw):
        self.holes.remove(15)
        graphics.zingo.display(self.holes, self.game.selector.position, True, False, self.game.replays)

    def sw_hole16_active(self, sw):
        self.holes.append(16)
        graphics.zingo.display(self.holes, self.game.selector.position, True, False, self.game.replays)
        self.search(self.holes)

    def sw_hole16_inactive(self, sw):
        self.holes.remove(16)
        graphics.zingo.display(self.holes, self.game.selector.position, True, False, self.game.replays)

    def sw_hole17_active(self, sw):
        self.holes.append(17)
        graphics.zingo.display(self.holes, self.game.selector.position, True, False, self.game.replays)
        self.search(self.holes)

    def sw_hole17_inactive(self, sw):
        self.holes.remove(17)
        graphics.zingo.display(self.holes, self.game.selector.position, True, False, self.game.replays)

    def sw_hole18_active(self, sw):
        self.holes.append(18)
        graphics.zingo.display(self.holes, self.game.selector.position, True, False, self.game.replays)
        self.search(self.holes)

    def sw_hole18_inactive(self, sw):
        self.holes.remove(18)
        graphics.zingo.display(self.holes, self.game.selector.position, True, False, self.game.replays)

    def sw_hole19_active(self, sw):
        self.holes.append(19)
        graphics.zingo.display(self.holes, self.game.selector.position, True, False, self.game.replays)
        self.search(self.holes)

    def sw_hole19_inactive(self, sw):
        self.holes.remove(19)
        graphics.zingo.display(self.holes, self.game.selector.position, True, False, self.game.replays)

    def sw_hole20_active(self, sw):
        self.holes.append(20)
        graphics.zingo.display(self.holes, self.game.selector.position, True, False, self.game.replays)
        self.search(self.holes)

    def sw_hole20_inactive(self, sw):
        self.holes.remove(20)
        graphics.zingo.display(self.holes, self.game.selector.position, True, False, self.game.replays)

    def sw_hole21_active(self, sw):
        self.holes.append(21)
        graphics.zingo.display(self.holes, self.game.selector.position, True, False, self.game.replays)
        self.search(self.holes)

    def sw_hole21_inactive(self, sw):
        self.holes.remove(21)
        graphics.zingo.display(self.holes, self.game.selector.position, True, False, self.game.replays)

    def sw_hole22_active(self, sw):
        self.holes.append(22)
        graphics.zingo.display(self.holes, self.game.selector.position, True, False, self.game.replays)
        self.search(self.holes)

    def sw_hole22_inactive(self, sw):
        self.holes.remove(22)
        graphics.zingo.display(self.holes, self.game.selector.position, True, False, self.game.replays)

    def sw_hole23_active(self, sw):
        self.holes.append(23)
        graphics.zingo.display(self.holes, self.game.selector.position, True, False, self.game.replays)
        self.search(self.holes)

    def sw_hole23_inactive(self, sw):
        self.holes.remove(23)
        graphics.zingo.display(self.holes, self.game.selector.position, True, False, self.game.replays)

    def sw_hole24_active(self, sw):
        self.holes.append(24)
        graphics.zingo.display(self.holes, self.game.selector.position, True, False, self.game.replays)
        self.search(self.holes)

    def sw_hole24_inactive(self, sw):
        self.holes.remove(24)
        graphics.zingo.display(self.holes, self.game.selector.position, True, False, self.game.replays)

    def sw_hole25_active(self, sw):
        self.holes.append(25)
        graphics.zingo.display(self.holes, self.game.selector.position, True, False, self.game.replays)
        self.search(self.holes)

    def sw_hole25_inactive(self, sw):
        self.holes.remove(25)
        graphics.zingo.display(self.holes, self.game.selector.position, True, False, self.game.replays)

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
        graphics.zingo.display(self.holes, self.game.selector.position, True, True, self.game.replays)
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
            graphics.zingo.display(self.holes, self.game.selector.position, True, False, self.game.replays)
            self.game.coils.sounder.pulse()

    def replay_step_up(self):
        self.game.replays += 1
        self.game.coils.sounder.pulse()
        graphics.zingo.display(self.holes, self.game.selector.position, True, False, self.game.replays)

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

        for i in range(0, 49): 
            self.r = self.closed_search_relays(self.game.searchdisc.position)
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
                        for i in relays:
                            pass
                        s = count_seq(relays)
                        if self.game.selector.position >= self.card:
                            self.find_winner(s, self.card)
            self.game.searchdisc.spin()

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
    """ Zingo was the second game United produced using the standard Bally playfield layout """
    def __init__(self, machine_type):
        super(Zingo, self).__init__(machine_type)
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

        self.replays = 99

    def reset(self):
        super(Zingo, self).reset()
        self.logger = logging.getLogger('game')
        self.load_config('zingo.yaml')
        
        main_mode = MulticardBingo(self)
        self.modes.add(main_mode)

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
    
game = Zingo(machine_type='pdb')
game.reset()
game.run_loop()
