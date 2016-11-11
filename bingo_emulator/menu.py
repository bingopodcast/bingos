#!/usr/bin/python

import logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
import pinproc
import procgame.game, sys, os
import procgame.config
import pygame
import time
import thread
import procgame.sound

sys.path.insert(0,os.path.pardir)
from bingo_emulator.graphics import methods as graphics
from bingo_emulator.common import units

#pygame.init()
pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])

class Menu(procgame.game.BasicGame):
    """ This menu lets you select games to play """
    def __init__(self, machine_type):
        super(Menu, self).__init__(machine_type)

    def reset(self, selection, select):
        super(Menu, self).reset()
        self.load_config('bingo.yaml')
        mainmenu = MainMenu(self, selection, select)
        self.modes.add(mainmenu)
        self.logger = logging.getLogger('game')



        
class MainMenu(procgame.game.Mode):
    def __init__(self, game, selection, select):
        super(MainMenu, self).__init__(game=game, priority=5)
        self.game.replays = 0
        self.game.select = select
        self.game.selection = selection
        self.game.anti_cheat = units.Relay("anti_cheat")
        self.game.super_card_trip = units.Relay("super_card_trip")
        self.game.super_line1 = units.Relay("super_line1")
        self.game.super_line2 = units.Relay("super_line2")
        self.game.super_card_replay_counter = units.Stepper("super_card_replay_counter", 400)
        self.game.feature = units.Stepper("feature", 6)
        self.game.before_fourth = units.Relay("before_fourth")
        self.game.searched = units.Relay("searched")
        self.game.before_fifth = units.Relay("before_fifth")
        self.game.lock = units.Relay("lock")
        self.game.tilt = units.Relay("tilt")
        self.game.liteaname = units.Relay("liteaname")
        self.game.eight_balls = units.Relay("eight_balls")
        self.game.three_as_four = units.Relay("three_as_four")
        self.game.four_as_five = units.Relay("four_as_five")
        self.game.selector = units.Stepper("selector", 6)
        self.game.name = units.Stepper("name", 6)
        self.game.select_card = units.Stepper("select_card", 6)
        self.game.card = units.Stepper("card", 6)
        self.game.spotting = units.Stepper("spotting", 49)
        self.game.eb_play = units.Relay("eb_play")
        self.game.eb = units.Relay("eb")
        self.game.spotted_numbers = units.Stepper("spotted_numbers", 8)
        self.game.ball_count = units.Stepper("ball_count", 8)
        self.game.ball_return = units.Stepper("ball_return", 15)
        self.game.extra_ball = units.Stepper("extra_ball", 3)
        self.game.double = units.Relay("double")
        self.game.special_feature = units.Relay("special_feature")
        self.game.special_1 = units.Relay("special_1")
        self.game.special_2 = units.Relay("special_2")
        self.game.special_3 = units.Relay("special_3")
        self.game.special_4 = units.Relay("special_4")
        self.game.special_5 = units.Relay("special_5")
        self.game.special_6 = units.Relay("special_6")
        self.game.c1_double = units.Relay("c1_double")
        self.game.c2_double = units.Relay("c2_double")
        self.game.c3_double = units.Relay("c3_double")
        self.game.c4_double = units.Relay("c4_double")
        self.game.c5_double = units.Relay("c5_double")
        self.game.c6_double = units.Relay("c6_double")
        self.game.c1_triple = units.Relay("c1_triple")
        self.game.c2_triple = units.Relay("c2_triple")
        self.game.c3_triple = units.Relay("c3_triple")
        self.game.c4_triple = units.Relay("c4_triple")
        self.game.c5_triple = units.Relay("c5_triple")
        self.game.c6_triple = units.Relay("c6_triple")
        self.game.all_double = units.Relay("all_double")
        self.game.all_triple = units.Relay("all_triple")
        self.game.corners = units.Relay("corners")
        self.game.golden = units.Relay("golden")
        self.game.gate = units.Relay("gate")
        self.game.two_gold = units.Relay("two_gold")
        self.game.odds = units.Stepper("odds", 10)
        self.game.green_odds = units.Stepper("green_odds", 10)
        self.game.red_odds = units.Stepper("red_odds", 10)
        self.game.yellow_odds = units.Stepper("yellow_odds", 10)
        self.game.gold_odds = units.Stepper("gold_odds", 10)
        self.game.odds_only = units.Relay("odds_only")
        self.game.features = units.Relay("features")
        self.game.orange_section = units.Relay("orange_section")
        self.game.red_super_section = units.Relay("red_super_section")
        self.game.yellow_super_section = units.Relay("yellow_super_section")
        self.game.ok = units.Relay("ok")
        self.game.super_card = units.Stepper("super_card", 8)
        self.game.selection_feature = units.Stepper("selection_feature", 8)
        self.game.magic_screen_feature = units.Stepper("magic_screen_feature", 8)
        self.game.red_star = units.Relay("red_star")
        self.game.yellow_star = units.Relay("yellow_star")
        self.game.corners1 = units.Relay("corners1")
        self.game.corners2 = units.Relay("corners2")
        self.game.corners3 = units.Relay("corners3")
        self.game.corners4 = units.Relay("corners4")
        self.game.corners5 = units.Relay("corners5")
        self.game.corners6 = units.Relay("corners6")
        self.game.select_spots = units.Relay("select_spots")
        self.game.fss = units.Relay("fss")
        self.game.fnt = units.Relay("fnt")
        self.game.sixteen = units.Relay("sixteen")
        self.game.fourteen_eighteen = units.Relay("fourteen_eighteen")
        self.game.fifteen_seventeen = units.Relay("fifteen_seventeen")
        self.game.fifteen = units.Relay("fifteen")
        self.game.seventeen = units.Relay("seventeen")
        self.game.twenty = units.Relay("twenty")
        self.game.twentyone = units.Relay("twentyone")
        self.game.twentytwo = units.Relay("twentytwo")
        self.game.good = units.Relay("good")
        self.game.excellent = units.Relay("excellent")
        self.game.superior = units.Relay("superior")
        self.game.dd1 = units.Relay("dd1")
        self.game.dd2 = units.Relay("dd2")
        self.game.dd3 = units.Relay("dd3")
        self.game.dd4 = units.Relay("dd4")
        self.game.dd5 = units.Relay("dd5")
        self.game.dd6 = units.Relay("dd6")
        self.game.before_third = units.Relay("before_third")
        self.game.before_fourth = units.Relay("before_fourth")
        self.game.top_score = units.Relay("top_score")

        self.game.magic_screen = units.Stepper("magic_screen", 15)
        self.game.magic = []
        self.game.onetwothree = units.Relay("onetwothree")
        self.game.fourfivesix = units.Relay("fourfivesix")

        self.game.super1 = units.Relay("super1")
        self.game.super2 = units.Relay("super2")
        self.game.super3 = units.Relay("super3")
        self.game.super4 = units.Relay("super4")
        self.game.super5 = units.Relay("super5")
        self.game.super6 = units.Relay("super6")

        self.game.card1_double = units.Relay("card1_double")
        self.game.card2_double = units.Relay("card2_double")
        self.game.card3_double = units.Relay("card3_double")
        self.game.card4_double = units.Relay("card4_double")
        self.game.card5_double = units.Relay("card5_double")
        self.game.card6_double = units.Relay("card6_double")


        self.game.card1_missed = units.Relay("card1_missed")
        self.game.card2_missed = units.Relay("card2_missed")
        self.game.card3_missed = units.Relay("card3_missed")
        self.game.card4_missed = units.Relay("card4_missed")
        self.game.card5_missed = units.Relay("card5_missed")
        self.game.card6_missed = units.Relay("card6_missed")


        self.game.card1_replay_counter = units.Stepper("card1_replay_counter", 300)
        self.game.card2_replay_counter = units.Stepper("card2_replay_counter", 300)
        self.game.card3_replay_counter = units.Stepper("card3_replay_counter", 300)
        self.game.card4_replay_counter = units.Stepper("card4_replay_counter", 300)
        self.game.card5_replay_counter = units.Stepper("card5_replay_counter", 300)
        self.game.card6_replay_counter = units.Stepper("card6_replay_counter", 300)
    
        self.holes = []

        selection[select]
        __import__("bingo_emulator.graphics.%s" % (selection[select]))
        g = "graphics.%s.display(self,0,True)" % (selection[select])
        eval(g)

    def sw_enter_active(self, sw):
        try:
            t = thread.start_new(__import__("bingo_emulator.%s.game" % (self.game.selection[self.game.select])))
            if t.isAlive():
                t.join()

        except:
            g = (__import__("bingo_emulator.%s.game" % (self.game.selection[self.game.select])))

            t = thread.start_new(eval(g))
            self.game.end_run_loop()
            if t.isAlive():
                t.join()
        self.game.reset(self.game.selection, self.game.select)

    def sw_left_active(self, sw):
        if self.game.select != 1:
            self.game.select -= 1
            self.game.selection[self.game.select]
            __import__("bingo_emulator.graphics.%s" % (self.game.selection[self.game.select]))
            g = "graphics.%s.display(self,0,True)" % (self.game.selection[self.game.select])
            eval(g)
            os.system("ssh pi@10.0.0.51 /home/pi/ic.sh %s &" % (self.game.selection[self.game.select]))
            os.system("ssh pi@10.0.0.52 /home/pi/sd.sh %s &" % (self.game.selection[self.game.select]))
    def sw_right_active(self, sw):
        if self.game.select != len(self.game.selection):
            self.game.select += 1
            self.game.selection[self.game.select]
            __import__("bingo_emulator.graphics.%s" % (self.game.selection[self.game.select]))
            g = "graphics.%s.display(self,0,True)" % (self.game.selection[self.game.select])
            eval(g)
	    os.system("ssh pi@10.0.0.51 /home/pi/ic.sh %s &" % (self.game.selection[self.game.select]))
	    os.system("ssh pi@10.0.0.52 /home/pi/sd.sh %s &" % (self.game.selection[self.game.select]))

def main(sel):
    selection = {}
    selection[1] = "bright_lights"
    selection[2] = "broadway_51"
    selection[3] = "coney_island"
    selection[4] = "zingo"
    selection[5] = "leader"
    selection[6] = "spot_lite"
    selection[7] = "holiday"
    selection[8] = "atlantic_city"
    selection[9] = "miss_california"
    selection[10] = "palm_beach"
    selection[11] = "stars"
    selection[12] = "long_beach"
    selection[13] = "circus"
    selection[14] = "frolics"
    selection[15] = "showboat"
    selection[16] = "bright_spot"
    selection[17] = "bally_beauty"
    selection[18] = "beach_club"
    selection[19] = "rodeo_3"
    selection[20] = "yacht_club"
    selection[21] = "dude_ranch"
    selection[22] = "rodeo_1"
    selection[23] = "fun_way"
    selection[24] = "carnival_queen"
    selection[25] = "sea_island"
    selection[26] = "lotta_fun"
    selection[27] = "county_fair"
    selection[28] = "laguna_beach"
    selection[29] = "fun_spot"
    selection[30] = "roller_derby"
    selection[31] = "circus_queen"
    selection[32] = "lite_a_line"
    selection[33] = "barrel_o_fun_61"
    selection[34] = "golden_gate"
    selection[35] = "silver_sails"
    selection[36] = "hole_in_one"
    selection[37] = "stock_market"
    selection[38] = "ticker_tape"
    selection[39] = "wall_street"
    selection[40] = "bali"
    selection[41] = "super_wall_street"
    selection[42] = "blue_chip"
    selection[43] = "bull_market"
    selection[44] = "high_flyer"
    selection[45] = "nashville"
    selection[46] = "dixieland"
    selection[47] = "malibu_beach"
    selection[48] = "continental"
    selection[49] = "mississippi_showboat"
    #selection[13] = "barrel_o_fun"
    #selection[16] = "fun_spot_61"
    #selection[17] = "barrel_o_fun_62"
    #selection[18] = "fun_spot_62"
    #selection[19] = "barrel_o_fun_63"
    #selection[20] = "fun_spot_63"

    for i in range(1,100):
        if sel in selection[i]:
            select = i
            break

    os.system("ssh pi@10.0.0.51 /home/pi/ic.sh %s &" % (selection[select]))
    os.system("ssh pi@10.0.0.52 /home/pi/sd.sh %s &" % (selection[select]))
    game = Menu(machine_type='pdb')
    game.reset(selection, select)
    game.run_loop()

if __name__ == "__main__":
    main(sys.argv[1])
