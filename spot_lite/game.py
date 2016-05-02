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
from bingo_emulator.graphics.spot_lite import *

from modes.timeout import Timeout

class SinglecardBingo(procgame.game.Mode):
    def __init__(self, game):
        super(SinglecardBingo, self).__init__(game=game, priority=5)
        self.holes = []
        self.startup()

    def sw_coin_active(self, sw):
        #TODO: animate for each coin - write specific function in game graphics library.
        self.regular_play()
        graphics.spot_lite.display(self.holes, self.game.odds.position, True, False)

    def sw_startButton_active(self, sw):
        if self.game.replays > 0:
            self.regular_play()
            graphics.spot_lite.display(self.holes, self.game.odds.position, True, False)

    def regular_play(self):
        if self.game.ball_count.position >= 1:
            self.game.odds.reset()
            if self.game.switches.shutter.is_active():
                self.game.coils.shutter.pulse()
            self.game.ball_count.reset()
        if self.game.odds.position == 0:
            self.game.odds.step()
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
        graphics.spot_lite.display(self.holes, self.game.odds.position, True, False)
        self.search(self.holes)

    def sw_hole1_inactive(self, sw):
        self.holes.remove(1)
        graphics.spot_lite.display(self.holes, self.game.odds.position, True, False)

    def sw_hole2_active(self, sw):
        self.holes.append(2)
        graphics.spot_lite.display(self.holes, self.game.odds.position, True, False)
        self.search(self.holes)

    def sw_hole2_inactive(self, sw):
        self.holes.remove(2)
        graphics.spot_lite.display(self.holes, self.game.odds.position, True, False)

    def sw_hole3_active(self, sw):
        self.holes.append(3)
        graphics.spot_lite.display(self.holes, self.game.odds.position, True, False)
        self.search(self.holes)

    def sw_hole3_inactive(self, sw):
        self.holes.remove(3)
        graphics.spot_lite.display(self.holes, self.game.odds.position, True, False)

    def sw_hole4_active(self, sw):
        self.holes.append(4)
        graphics.spot_lite.display(self.holes, self.game.odds.position, True, False)
        self.search(self.holes)

    def sw_hole4_inactive(self, sw):
        self.holes.remove(4)
        graphics.spot_lite.display(self.holes, self.game.odds.position, True, False)

    def sw_hole5_active(self, sw):
        self.holes.append(5)
        graphics.spot_lite.display(self.holes, self.game.odds.position, True, False)
        self.search(self.holes)

    def sw_hole5_inactive(self, sw):
        self.holes.remove(5)
        graphics.spot_lite.display(self.holes, self.game.odds.position, True, False)

    def sw_hole6_active(self, sw):
        self.holes.append(6)
        graphics.spot_lite.display(self.holes, self.game.odds.position, True, False)
        self.search(self.holes)

    def sw_hole6_inactive(self, sw):
        self.holes.remove(6)
        graphics.spot_lite.display(self.holes, self.game.odds.position, True, False)

    def sw_hole7_active(self, sw):
        self.holes.append(7)
        graphics.spot_lite.display(self.holes, self.game.odds.position, True, False)
        self.search(self.holes)

    def sw_hole7_inactive(self, sw):
        self.holes.remove(7)
        graphics.spot_lite.display(self.holes, self.game.odds.position, True, False)

    def sw_hole8_active(self, sw):
        self.holes.append(8)
        graphics.spot_lite.display(self.holes, self.game.odds.position, True, False)
        self.search(self.holes)

    def sw_hole8_inactive(self, sw):
        self.holes.remove(8)
        graphics.spot_lite.display(self.holes, self.game.odds.position, True, False)

    def sw_hole9_active(self, sw):
        self.holes.append(9)
        graphics.spot_lite.display(self.holes, self.game.odds.position, True, False)
        self.search(self.holes)

    def sw_hole9_inactive(self, sw):
        self.holes.remove(9)
        graphics.spot_lite.display(self.holes, self.game.odds.position, True, False)

    def sw_hole10_active(self, sw):
        self.holes.append(10)
        graphics.spot_lite.display(self.holes, self.game.odds.position, True, False)
        self.search(self.holes)

    def sw_hole10_inactive(self, sw):
        self.holes.remove(10)
        graphics.spot_lite.display(self.holes, self.game.odds.position, True, False)

    def sw_hole11_active(self, sw):
        self.holes.append(11)
        graphics.spot_lite.display(self.holes, self.game.odds.position, True, False)
        self.search(self.holes)

    def sw_hole11_inactive(self, sw):
        self.holes.remove(11)
        graphics.spot_lite.display(self.holes, self.game.odds.position, True, False)

    def sw_hole12_active(self, sw):
        self.holes.append(12)
        graphics.spot_lite.display(self.holes, self.game.odds.position, True, False)
        self.search(self.holes)

    def sw_hole12_inactive(self, sw):
        self.holes.remove(12)
        graphics.spot_lite.display(self.holes, self.game.odds.position, True, False)

    def sw_hole13_active(self, sw):
        self.holes.append(13)
        graphics.spot_lite.display(self.holes, self.game.odds.position, True, False)
        self.search(self.holes)

    def sw_hole13_inactive(self, sw):
        self.holes.remove(13)
        graphics.spot_lite.display(self.holes, self.game.odds.position, True, False)

    def sw_hole14_active(self, sw):
        self.holes.append(14)
        graphics.spot_lite.display(self.holes, self.game.odds.position, True, False)
        self.search(self.holes)

    def sw_hole14_inactive(self, sw):
        self.holes.remove(14)
        graphics.spot_lite.display(self.holes, self.game.odds.position, True, False)

    def sw_hole15_active(self, sw):
        self.holes.append(15)
        graphics.spot_lite.display(self.holes, self.game.odds.position, True, False)
        self.search(self.holes)

    def sw_hole15_inactive(self, sw):
        self.holes.remove(15)
        graphics.spot_lite.display(self.holes, self.game.odds.position, True, False)

    def sw_hole16_active(self, sw):
        self.holes.append(16)
        graphics.spot_lite.display(self.holes, self.game.odds.position, True, False)
        self.search(self.holes)

    def sw_hole16_inactive(self, sw):
        self.holes.remove(16)
        graphics.spot_lite.display(self.holes, self.game.odds.position, True, False)

    def sw_hole17_active(self, sw):
        self.holes.append(17)
        graphics.spot_lite.display(self.holes, self.game.odds.position, True, False)
        self.search(self.holes)

    def sw_hole17_inactive(self, sw):
        self.holes.remove(17)
        graphics.spot_lite.display(self.holes, self.game.odds.position, True, False)

    def sw_hole18_active(self, sw):
        self.holes.append(18)
        graphics.spot_lite.display(self.holes, self.game.odds.position, True, False)
        self.search(self.holes)

    def sw_hole18_inactive(self, sw):
        self.holes.remove(18)
        graphics.spot_lite.display(self.holes, self.game.odds.position, True, False)

    def sw_hole19_active(self, sw):
        self.holes.append(19)
        graphics.spot_lite.display(self.holes, self.game.odds.position, True, False)
        self.search(self.holes)

    def sw_hole19_inactive(self, sw):
        self.holes.remove(19)
        graphics.spot_lite.display(self.holes, self.game.odds.position, True, False)

    def sw_hole20_active(self, sw):
        self.holes.append(20)
        graphics.spot_lite.display(self.holes, self.game.odds.position, True, False)
        self.search(self.holes)

    def sw_hole20_inactive(self, sw):
        self.holes.remove(20)
        graphics.spot_lite.display(self.holes, self.game.odds.position, True, False)

    def sw_hole21_active(self, sw):
        self.holes.append(21)
        graphics.spot_lite.display(self.holes, self.game.odds.position, True, False)
        self.search(self.holes)

    def sw_hole21_inactive(self, sw):
        self.holes.remove(21)
        graphics.spot_lite.display(self.holes, self.game.odds.position, True, False)

    def sw_hole22_active(self, sw):
        self.holes.append(22)
        graphics.spot_lite.display(self.holes, self.game.odds.position, True, False)
        self.search(self.holes)

    def sw_hole22_inactive(self, sw):
        self.holes.remove(22)
        graphics.spot_lite.display(self.holes, self.game.odds.position, True, False)

    def sw_hole23_active(self, sw):
        self.holes.append(23)
        graphics.spot_lite.display(self.holes, self.game.odds.position, True, False)
        self.search(self.holes)

    def sw_hole23_inactive(self, sw):
        self.holes.remove(23)
        graphics.spot_lite.display(self.holes, self.game.odds.position, True, False)

    def sw_hole24_active(self, sw):
        self.holes.append(24)
        graphics.spot_lite.display(self.holes, self.game.odds.position, True, False)
        self.search(self.holes)

    def sw_hole24_inactive(self, sw):
        self.holes.remove(24)
        graphics.spot_lite.display(self.holes, self.game.odds.position, True, False)

    def sw_hole25_active(self, sw):
        self.holes.append(25)
        graphics.spot_lite.display(self.holes, self.game.odds.position, True, False)
        self.search(self.holes)

    def sw_hole25_inactive(self, sw):
        self.holes.remove(25)
        graphics.spot_lite.display(self.holes, self.game.odds.position, True, False)

    def replay_reset(self):
        if self.game.switches.replay0.is_inactive():
            self.game.coils.sounder.pulse()

    def tilt_actions(self):
        if self.game.switches.shutter.is_inactive():
            self.game.coils.shutterMotor.pulse()
        self.holes = []
        self.game.ball_count.reset()
        self.game.odds.reset()
        self.game.tilt.engage(self.game)
        # displays "Tilt" on the backglass, you have to recoin.
        graphics.spot_lite.display(self.holes, self.game.odds.position, True, True)
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
            graphics.replay_step_down(self.game.replays, graphics.broadway_51.reel1, graphics.broadway_51.reel10, graphics.broadway_51.reel100)
            self.game.coils.sounder.pulse()

    def replay_step_up(self):
        graphics.replay_step_up(self.game.replays, graphics.spot_lite.reel1, graphics.spot_lite.reel10, graphics.spot_lite.reel100)
        self.game.replays += 1
        self.game.coils.sounder.pulse()
        graphics.spot_lite.display(self.holes, self.game.odds.position, True, False)

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

        for i in range(0, 50):
            self.r = self.closed_search_relays(self.game.searchdisc.position)
            self.game.searchdisc.spin()
            self.wipers = self.r[0]
            self.card = self.r[1]
            self.horizontal = self.r[2]
            self.vertical = self.r[3]
            self.diagonal = self.r[4]

            # From here, I need to determine based on the value of r, whether to latch the search index and score. For Bright Lights,
            # I need to determine the best winner on each card.  To do this, I must compare the position of the replay counter before
            # determining the winner. Reminder that my replay counters are a 1:1 representation.

            self.match = []
            for key in self.wipers:
                for number in self.holes:
                    if number == key:
                        print self.match
                        self.match.append(self.wipers[key])
                        relays = sorted(set(self.match))
                        #TODO Play sound for each relay closure.
                        for i in relays:
                            pass
                        s = count_seq(relays)
                        self.find_winner(s, self.card, self.horizontal, self.vertical, self.diagonal, self.game.odds.horizontal, self.game.odds.vertical, self.game.odds.diagonal, self.game.odds.four, self.game.odds.five)

    def find_winner(self, relays, card, horizontal, vertical, diagonal, hodds, vodds, dodds, fourodds, fiveodds):
        print "Hor" + str(horizontal)
        print "Vertical" + str(vertical)
        print "Diagonal" + str(diagonal)
        if card == 1:
            if relays == 3:
                if horizontal == True:
                    if self.game.card1_replay_counter.position < hodds:
                        while self.game.card1_replay_counter.position < hodds:
                            self.game.card1_replay_counter.step()
                            self.replay_step_up()
                if vertical == True:
                    if self.game.card1_replay_counter.position < vodds:
                        while self.game.card1_replay_counter.position < vodds:
                            self.game.card1_replay_counter.step()
                            self.replay_step_up()
                if diagonal == True:
                    if self.game.card1_replay_counter.position < dodds:
                        while self.game.card1_replay_counter.position < dodds:
                            self.game.card1_replay_counter.step()
                            self.replay_step_up()
            if relays == 4:
                if self.game.card1_replay_counter.position < fourodds:
                    while self.game.card1_replay_counter.position < fourodds:
                        self.game.card1_replay_counter.step()
                        self.replay_step_up()
            if relays == 5:
                if self.game.card1_replay_counter.position < fiveodds:
                    while self.game.card1_replay_counter.position < fiveodds:
                        self.game.card1_replay_counter.step()
                        self.replay_step_up()

    def closed_search_relays(self, rivets):
        # This function is critical, as it will determine which card is returned, etc.  I need to check the position of the
        # replay counter for the card. We will get a row back
        # that has the numbers on the position which will return the search relay connected.  When three out of the five relays
        # are connected, we get a winner!
        
        self.pos = {}
        # Card 1
        self.pos[0] = {}
        self.pos[1] = {9:1, 24:2, 15:3, 4:4, 6:5}
        self.pos[2] = {13:1, 19:2, 14:3, 20:4, 25:5}
        self.pos[3] = {2:1, 18:2, 16:3, 12:4, 17:5}
        self.pos[4] = {1:1, 22:2, 11:3, 21:4, 8:5}
        self.pos[5] = {10:1, 7:2, 5:3, 23:4, 3:5}
        self.pos[6] = {9:1, 13:2, 2:3, 1:4, 10:5}
        self.pos[7] = {24:1, 19:2, 18:3, 22:4, 7:5}
        self.pos[8] = {15:1, 14:2, 16:3, 11:4, 5:5}
        self.pos[9] = {4:1, 20:2, 12:3, 21:4, 23:5}
        self.pos[10] = {6:1, 25:2, 17:3, 8:4, 3:5}
        self.pos[11] = {9:1, 19:2, 16:3, 21:4, 3:5}
        self.pos[12] = {10:1, 22:2, 16:3, 20:4, 6:5}
        self.pos[13] = {}
        self.pos[14] = {}
        self.pos[15] = {}
        self.pos[16] = {}
        self.pos[17] = {}
        self.pos[18] = {}
        self.pos[19] = {}
        self.pos[20] = {}
        self.pos[21] = {}
        self.pos[22] = {}
        self.pos[23] = {}
        self.pos[24] = {}
        self.pos[25] = {}
        self.pos[26] = {}
        self.pos[27] = {}
        self.pos[28] = {}
        self.pos[29] = {}
        self.pos[30] = {}
        self.pos[31] = {}
        self.pos[32] = {}
        self.pos[33] = {}
        self.pos[34] = {}
        self.pos[35] = {}
        self.pos[36] = {}
        self.pos[37] = {}
        self.pos[38] = {}
        self.pos[39] = {}
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

        horizontal = False
        vertical = False
        diagonal = False

        if rivets in range(0,6):
            horizontal = True
        if rivets in range(6,11):
            vertical = True
        if rivets in range(11,13):
            diagonal = True
        if rivets in range(0,50):
            card = 1

        return (self.pos[rivets], card, horizontal, vertical, diagonal)
            
                                            
    # Define reset as the knock-off, anti-cheat relay disabled, and replay reset enabled.  Motors turn while credits are knocked off.
    # When meter reaches zero and the zero limit switch is hit, turn off motor sound and leave backglass gi on, but with tilt displayed.

    def startup(self):        
        # Every bingo requires the meter to register '0' 
        # before allowing coin entry --
        # also needs to show a plain 'off' backglass.
        self.eb = False
        self.tilt_actions()


class SpotLite(procgame.game.BasicGame):
    """ Spot-Lite was the first game with Pic-A-Play and advancing odds """
    def __init__(self, machine_type):
        super(SpotLite, self).__init__(machine_type)
        # NOTE: trough_count only counts the number of switches present in the  trough.  It does _not_ count
        #       the number of balls present.   In this game, there  should  be  8  balls.
        self.trough_count = 6

        # Subclass my units unique to this game -  modifications must be made to set up mixers and steppers unique to the game
        # NOTE: 'top' positions are indexed using a 0 index, so the top on a 24 position unit is actually 23.

        self.searchdisc = units.Search("searchdisc", 49)

        #Search relays
        self.s1 = units.Relay("s1")
        self.s2 = units.Relay("s2")
        self.s3 = units.Relay("s3")
        self.s4 = units.Relay("s4")
        self.s5 = units.Relay("s5")

        #Odds stepper
        self.odds = units.Stepper("odds", 10, 'spot_lite')

        #Replay Counter
        self.card1_replay_counter = units.Stepper("card1_replay_counter", 100)

        #Initialize stepper units used to keep track of features or timing.
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
        super(SpotLite, self).reset()
        self.logger = logging.getLogger('game')
        self.load_config('broadway_51.yaml')
        
        main_mode = SinglecardBingo(self)
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

game = SpotLite(machine_type='pdb')
game.reset()
game.run_loop()
