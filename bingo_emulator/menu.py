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
        self.game.green_three_as_five = units.Relay("green_three_as_five")
        self.game.yellow_three_as_four = units.Relay("yellow_three_as_four")
        self.game.red_three_as_four = units.Relay("red_three_as_four")
        self.game.super_card_trip = units.Relay("super_card_trip")
        self.game.super_card1 = units.Relay("super_card1")
        self.game.super_card2 = units.Relay("super_card2")
        self.game.super_line1 = units.Relay("super_line1")
        self.game.super_line2 = units.Relay("super_line2")
        self.game.super_card_replay_counter = units.Stepper("super_card_replay_counter", 400)
        self.game.feature = units.Stepper("feature", 6)
        self.game.curtains = units.Stepper("curtains", 6)
        self.game.lines = units.Stepper("lines", 6)
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
        self.game.b_return = units.Relay("b_return")
        self.game.ball_return_played = units.Relay("ball_return_played")
        self.game.diagonal_score = units.Relay("diagonal_score")
        self.game.all_advantages = units.Relay("all_advantages")
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
        self.game.super_corners = units.Relay("super_corners")
        self.game.golden = units.Relay("golden")
        self.game.gate = units.Relay("gate")
        self.game.two_gold = units.Relay("two_gold")
        self.game.odds = units.Stepper("odds", 10)
        self.game.green_odds = units.Stepper("green_odds", 10)
        self.game.red_odds = units.Stepper("red_odds", 10)
        self.game.yellow_odds = units.Stepper("yellow_odds", 10)
        self.game.white_odds = units.Stepper("white_odds", 10)
        self.game.gold_odds = units.Stepper("gold_odds", 10)
        self.game.odds_only = units.Relay("odds_only")
        self.game.features = units.Relay("features")
        self.game.orange_section = units.Relay("orange_section")
        self.game.red_super_section = units.Relay("red_super_section")
        self.game.yellow_super_section = units.Relay("yellow_super_section")
        self.game.futurity =  units.Stepper("futurity", 12)
        self.game.ok = units.Relay("ok")
        self.game.four_stars = units.Relay("four_stars")
        self.game.hole_feature = units.Relay("hole_feature")
        self.game.spot_16 = units.Relay("spot_16")
        self.game.super_line_feature = units.Relay("super_line_feature")
        self.game.extra_ok = units.Relay("extra_ok")
        self.game.super_ok = units.Relay("super_ok")
        self.game.super_card = units.Stepper("super_card", 8)
        self.game.selection_feature = units.Stepper("selection_feature", 8)
        self.game.magic_screen_feature = units.Stepper("magic_screen_feature", 8)
        self.game.magic_numbers_feature = units.Stepper("magic_numbers_feature", 8)
        self.game.roto_feature = units.Relay("roto_feature")
        self.game.roto_feature_step = units.Stepper("roto_feature_step", 8)
        self.game.super_horizontal = units.Relay("super_horizontal")
        self.game.horizontal = units.Stepper("horizontal", 8)
        self.game.special_odds = units.Stepper("special_odds", 8)
        self.game.special_game = units.Stepper("special_game", 8)
        self.game.special_replay_counter = units.Stepper("special_replay_counter", 8)
        self.game.red_replay_counter = units.Stepper("red_replay_counter", 8)
        self.game.yellow_replay_counter = units.Stepper("yellow_replay_counter", 8)
        self.game.green_replay_counter = units.Stepper("green_replay_counter", 8)
        self.game.twin_number = units.Stepper("twin_number", 8)
        self.game.color_selector = units.Stepper("color_selector", 8)
        self.game.score_select = units.Stepper("score_select", 8)
        self.game.x_feature = units.Stepper("x_feature", 8)
        self.game.magic_lines = units.Stepper("magic_lines", 8)
        self.game.hold_feature = units.Stepper("hold_feature", 8)
        self.game.m_lines = units.Relay("m_lines")
        self.game.super_score = units.Relay("super_score")
        self.game.magic_pockets = units.Relay("magic_pockets")
        self.game.spot_10 = units.Relay("spot_10")
        self.game.spot_25 = units.Relay("spot_25")
        self.game.bonus = units.Stepper("bonus", 8)
        self.game.ring = units.Stepper("ring", 8)
        self.game.two_suns = units.Relay("two_suns")
        self.game.double_double = units.Relay("double_double")
        self.game.double_up = units.Relay("double_up")
        self.game.double_colors = units.Stepper("double_colors", 8)
        self.game.wheel = units.Stepper("wheel", 8)
        self.game.three_suns = units.Relay("three_suns")
        self.game.top_odds = units.Relay("top_odds")
        self.game.missed = units.Relay("missed")
        self.game.red_star = units.Relay("red_star")
        self.game.red_rollover = units.Relay("red_rollover")
        self.game.special = units.Relay("special")
        self.game.triple = units.Relay("triple")
        self.game.yellow_star = units.Relay("yellow_star")
        self.game.yellow_rollover = units.Relay("yellow_rollover")
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
        self.game.cornersone_three = units.Relay("cornersone_three")
        self.game.cornerstwo_three = units.Relay("cornerstwo_three")
        self.game.cornersone_four = units.Relay("cornersone_four")
        self.game.cornerstwo_four = units.Relay("cornerstwo_four")

        self.game.roto = units.Stepper("roto", 6)
        self.game.roto2 = units.Stepper("roto2", 6)
        self.game.numbera = units.Stepper("numbera", 6)
        self.game.numberb = units.Stepper("numberb", 6)
        self.game.numberc = units.Stepper("numberc", 6)
        self.game.numberd = units.Stepper("numberd", 6)
        self.game.each_card = units.Stepper("each_card", 6)
        self.game.bump_feature = units.Stepper("bump_feature", 6)
        self.game.e_card = units.Relay("e_card")
        self.game.average = units.Relay("average")
        self.game.expert = units.Relay("expert")
        self.game.m_pockets = units.Stepper("m_pockets", 4)
        self.game.wild_pockets = units.Stepper("wild_pockets", 9)
        self.game.special_pocket = units.Relay("special_pocket")
        self.game.super_diagonal = units.Relay("super_diagonal")
        self.game.diagonal = units.Relay("diagonal")
        self.game.diagonal_separate = units.Stepper("diagonal_separate", 9)
        self.game.diagonals_relay = units.Relay("diagonals_relay")
        self.game.row1 = units.Relay("row1")
        self.game.row2 = units.Relay("row2")
        self.game.row3 = units.Relay("row3")
        self.game.pocket = units.Stepper("pocket", 5)
        self.game.diagonals = units.Stepper("diagonals", 5)
        self.game.diagonal_scoring = units.Stepper("diagonal_scoring", 9)
        self.game.super_super_card = units.Stepper("super_super_card", 9)

        self.game.magic_screen = units.Stepper("magic_screen", 15)
        self.game.line = units.Stepper("line", 3)
        self.game.line_feature = units.Stepper("line_feature", 3)
        self.game.line1 = units.Stepper("line1", 3)
        self.game.line2 = units.Stepper("line2", 3)
        self.game.line3 = units.Stepper("line3", 3)
        self.game.line4 = units.Stepper("line4", 3)
        self.game.line5 = units.Stepper("line5", 3)
        self.game.magic_lines_feature = units.Stepper("magic_lines_feature", 5)
        self.game.magic_card = units.Stepper("magic_card", 15)
        self.game.spot = units.Stepper("spot", 15)
        self.game.coin = units.Stepper("coin", 50)
        self.game.magic = []
        self.game.two_red_letter = units.Relay("two_red_letter")
        self.game.three_red_letter = units.Relay("three_red_letter")
        self.game.magic_spot = units.Relay("magic_spot")
        self.game.three_stars = units.Relay("three_stars")
        self.game.gate_open = units.Relay("gate_open")
        self.game.six_stars = units.Relay("six_stars")
        self.game.double_red = units.Relay("double_red")
        self.game.double_yellow = units.Relay("double_yellow")
        self.game.double_green = units.Relay("double_green")
        self.game.double_blue = units.Relay("double_blue")
        self.game.mystery_red = units.Relay("mystery_red")
        self.game.mystery_yellow = units.Relay("mystery_yellow")
        self.game.corners384 = units.Relay("corners384")
        self.game.corners300 = units.Relay("corners300")
        self.game.corners192 = units.Relay("corners192")
        self.game.start = units.Relay("start")
        self.game.search_index = units.Relay("search_index")
        self.game.nothing = units.Relay("nothing")
        self.game.onetwothree = units.Relay("onetwothree")
        self.game.fourfivesix = units.Relay("fourfivesix")
        self.game.selection_feature_relay = units.Relay("selection_feature_relay")
        self.game.left_special_card = units.Relay("left_special_card")
        self.game.right_special_card = units.Relay("right_special_card")
        self.game.letter_r = units.Relay("letter_r")
        self.game.letter_i = units.Relay("letter_i")
        self.game.letter_o = units.Relay("letter_o")
        self.game.letter_ha = units.Relay("letter_ha")
        self.game.letter_va = units.Relay("letter_va")
        self.game.letter_na = units.Relay("letter_na")
        self.game.letter_me = units.Relay("letter_me")
        self.game.letter_xi = units.Relay("letter_xi")
        self.game.letter_co = units.Relay("letter_co")
        self.game.one_seven_feature = units.Relay("one_seven_feature")
        self.game.one_seven = units.Relay("one_seven")
        self.game.seven_one = units.Relay("seven_one")
        self.game.lite_a_name = units.Relay("lite_a_name")
        self.game.rollovers = units.Relay("rollovers")
        self.game.diamond_diagonal = units.Relay("diamond_diagonal")

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

        self.game.red_double = units.Relay("red_double")
        self.game.yellow_double = units.Relay("yellow_double")
        self.game.green_double = units.Relay("green_double")
        self.game.white_double = units.Relay("white_double")

        self.game.red_missed = units.Relay("red_missed")
        self.game.yellow_missed = units.Relay("yellow_missed")
        self.game.green_missed = units.Relay("green_missed")
        self.game.white_missed = units.Relay("white_missed")

        self.game.red_regular = units.Relay("red_regular")
        self.game.yellow_regular = units.Relay("yellow_regular")
        self.game.green_regular = units.Relay("green_regular")
        self.game.white_regular = units.Relay("white_regular")

        self.game.square_a = units.Stepper("square_a", 3, "menu", "continuous")
        self.game.square_b = units.Stepper("square_b", 3, "menu", "continuous")
        self.game.square_c = units.Stepper("square_c", 3, "menu", "continuous")
        self.game.square_d = units.Stepper("square_d", 3, "menu", "continuous")
        self.game.square_e = units.Stepper("square_e", 3, "menu", "continuous")
        self.game.line_f = units.Stepper("line_f", 3, "menu", "continuous")
        self.game.magic_line_f = units.Relay("magic_line_f")
        self.game.red_line = units.Stepper("red_line", 8)
        self.game.yellow_line = units.Stepper("yellow_line", 8)
        self.game.green_line = units.Stepper("green_line", 8)
        self.game.magic_squares_feature = units.Stepper("magic_squares_feature", 10)
        self.game.ballyhole = units.Relay("ballyhole")
        self.game.top_line = units.Relay("top_line")
        self.game.bottom_line = units.Relay("bottom_line")
        self.game.spot_12 = units.Relay("spot_12")
        self.game.spot_13 = units.Relay("spot_13")
        self.game.game1 = units.Relay("game1")
        self.game.game2 = units.Relay("game2")
        self.game.shop_three = units.Relay("shop_three")
        self.game.shop_four = units.Relay("shop_four")
        self.game.score_feature = units.Stepper("score_feature", 8)
        self.game.magic_line = units.Relay("magic_line")
        self.game.select_a_score = units.Relay("select_a_score")

        self.game.odds1 = units.Stepper("odds1", 5)
        self.game.odds2 = units.Stepper("odds2", 5)
        self.game.blue_odds = units.Stepper("blue_odds", 12)
        self.game.orange_odds = units.Stepper("orange_odds", 12)


        self.game.card1_missed = units.Relay("card1_missed")
        self.game.card2_missed = units.Relay("card2_missed")
        self.game.card3_missed = units.Relay("card3_missed")
        self.game.card4_missed = units.Relay("card4_missed")
        self.game.card5_missed = units.Relay("card5_missed")
        self.game.card6_missed = units.Relay("card6_missed")

        self.game.mystic_lines = units.Stepper("mystic_lines", 6)
    
        self.game.ss = units.Relay("ss")
        self.game.skill_shot_scores = units.Stepper("skill_shot_scores",  20)
        self.game.skill_shot_replay_counter  = units.Stepper("skill_shot_replay_counter", 120)
        self.game.skill_shot_reflex = units.Reflex("skill_shot_reflex", 200)
        self.game.skill_shot_selection = []

        self.game.card1_replay_counter = units.Stepper("card1_replay_counter", 300)
        self.game.card2_replay_counter = units.Stepper("card2_replay_counter", 300)
        self.game.card3_replay_counter = units.Stepper("card3_replay_counter", 300)
        self.game.card4_replay_counter = units.Stepper("card4_replay_counter", 300)
        self.game.card5_replay_counter = units.Stepper("card5_replay_counter", 300)
        self.game.card6_replay_counter = units.Stepper("card6_replay_counter", 300)
    
        self.holes = []
        self.holes2 = []

        selection[select]
        __import__("bingo_emulator.graphics.%s" % (selection[select]))
        g = "graphics.%s.display(self,0,True)" % (selection[select])
        eval(g)

    def display_error(self, selection, select, playfield):

        errortext1 = "To play, please insert %s playfield." % (playfield)
        errortext2 = "Be careful with the Jones Plugs!"
        
        errortext3 = ""
        errortext4 = ""

        if playfield == "28 hole":
            errortext3 += "When inserting this playfield, please change the ball"
            errortext4 += "return board or the game will not function properly."
        if self.game.switches.bally28.is_active():
            errortext3 += "When inserting this playfield, please change the ball"
            errortext4 += "return board or the game will not function properly."

        errortext5 = "To choose a different game,"
        errortext6 = "press Left or Right buttons."

        pygame.font.init() # you have to call this at the start, 
                           # if you want to use this module.
        font = pygame.font.SysFont('Liberation Sans', 30)

        textsurface1=font.render(errortext1, True, (0, 0, 0))
        textsurface2=font.render(errortext2, True, (0, 0, 0))
        textsurface3=font.render(errortext3, True, (0, 0, 0))
        textsurface4=font.render(errortext4, True, (0, 0, 0))
        textsurface5=font.render(errortext5, True, (0, 0, 0))
        textsurface6=font.render(errortext6, True, (0, 0, 0))
        surface=pygame.Surface((720, 1280))
        surface.fill((255, 255, 255))
        text_rect1 = textsurface1.get_rect(center=(360, 500))
        text_rect2 = textsurface2.get_rect(center=(360, 550))
        text_rect3 = textsurface3.get_rect(center=(360, 620))
        text_rect4 = textsurface4.get_rect(center=(360, 670))
        text_rect5 = textsurface5.get_rect(center=(360, 750))
        text_rect6 = textsurface6.get_rect(center=(360, 800))
        surface.blit(textsurface1, text_rect1)
        surface.blit(textsurface2, text_rect2)
        surface.blit(textsurface3, text_rect3)
        surface.blit(textsurface4, text_rect4)
        surface.blit(textsurface5, text_rect5)
        surface.blit(textsurface6, text_rect6)
        #surface.blit(textsurface, [360,640])
        surface.set_alpha(175)
        screen.blit(surface,(0,0))
        pygame.display.update()


        return

        #ck = (127, 33, 33)
        #size = 25
        #s = pygame.Surface((50, 50))

        # first, "erase" the surface by filling it with a color and
        # setting this color as colorkey, so the surface is empty
        #s.fill(ck)
        #s.set_colorkey(ck)

        #pygame.draw.circle(s, (255, 0, 0), (size, size), size, 2)

        # after drawing the circle, we can set the 
        # alpha value (transparency) of the surface
        #s.set_alpha(75)

        #x, y = pygame.mouse.get_pos()
        #screen.blit(s, (x-size, y-size))

        #pygame.event.poll()
        #pygame.display.flip()



    def sw_enter_active(self, sw):
        try:
            s = self.game.select
            if s in [2,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,30,32,34,35,36,37,38,39,40,41,43,45,46,47,48,49,50,51,53,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,91,92,93,95,96,97,98,99,100,114,115,117,119,120,121,122,126,127,128,129,130,131,133,134,136,137,138]:
                if self.game.switches.bally25ro.is_inactive():
                    self.display_error(self.game.selection, self.game.select, "25 hole with rollovers")
                    return
            if s in [1,3]:
                if self.game.switches.unitedRoulette.is_inactive():
                    self.display_error(self.game.selection, self.game.select, "roulette")
                    return
            if s in [29,31,33]:
                if self.game.switches.bally25hold.is_inactive():
                    self.display_error(self.game.selection, self.game.select, "25 hole with hold")
                    return
            if s in [42,44]:
                if self.game.switches.bally25pockets.is_inactive():
                    self.display_error(self.game.selection, self.game.select, "25 hole with pockets")
                    return
            if s in [52,54,124,125]:
                if self.game.switches.bally18.is_inactive():
                    self.display_error(self.game.selection, self.game.select, "18 hole")
                    return
            if s in [90,94]:
                if self.game.switches.bally28.is_inactive():
                    self.display_error(self.game.selection, self.game.select, "28 hole")
                    return
            if s in [101,102,103,104,105,106,107,108,109,110,111,112,113,116,118]:
                if self.game.switches.bally20ro.is_inactive():
                    self.display_error(self.game.selection, self.game.select, "20 hole with rollovers")
                    return
            if s in [123]:
                if self.game.switches.bally20gate.is_inactive():
                    self.display_error(self.game.selection, self.game.select, "20 hole with gate")
                    return
            if s in [132]:
                if self.game.switches.bally24.is_inactive():
                    self.display_error(self.game.selection, self.game.select, "24 hole")
                    return
            if s in [135]:
                if self.game.switches.bally20hold.is_inactive():
                    self.display_error(self.game.selection, self.game.select, "20 hole with hold")
                    return

            t = thread.start_new(__import__("bingo_emulator.%s.game" % (self.game.selection[self.game.select])))
            if t.isAlive():
                t.join()

        except:
            if s in [2,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,30,32,34,35,36,37,38,39,40,41,43,45,46,47,48,49,50,51,53,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,91,92,93,95,96,97,98,99,100,114,115,117,119,120,121,122,126,127,128,129,130,131,133,134,136,137,138]:
                if self.game.switches.bally25ro.is_inactive():
                    self.display_error(self.game.selection, self.game.select, "25 hole with rollovers")
                    return
            if s in [1,3]:
                if self.game.switches.unitedRoulette.is_inactive():
                    self.display_error(self.game.selection, self.game.select, "roulette")
                    return
            if s in [29,31,33]:
                if self.game.switches.bally25hold.is_inactive():
                    self.display_error(self.game.selection, self.game.select, "25 hole with hold")
                    return
            if s in [42,44]:
                if self.game.switches.bally25pockets.is_inactive():
                    self.display_error(self.game.selection, self.game.select, "25 hole with pockets")
                    return
            if s in [52,54,124,125]:
                if self.game.switches.bally18.is_inactive():
                    self.display_error(self.game.selection, self.game.select, "18 hole")
                    return
            if s in [90,94]:
                if self.game.switches.bally28.is_inactive():
                    self.display_error(self.game.selection, self.game.select, "28 hole")
                    return
            if s in [101,102,103,104,105,106,107,108,109,110,111,112,113,116,118]:
                if self.game.switches.bally20ro.is_inactive():
                    self.display_error(self.game.selection, self.game.select, "20 hole with rollovers")
                    return
            if s in [123]:
                if self.game.switches.bally20gate.is_inactive():
                    self.display_error(self.game.selection, self.game.select, "20 hole with gate")
                    return
            if s in [132]:
                if self.game.switches.bally24.is_inactive():
                    self.display_error(self.game.selection, self.game.select, "24 hole")
                    return
            if s in [135]:
                if self.game.switches.bally20hold.is_inactive():
                    self.display_error(self.game.selection, self.game.select, "20 hole with hold")
                    return

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
    selection[1] = "abc"
    selection[2] = "bright_lights"
    selection[3] = "u345"
    selection[4] = "broadway_51"
    selection[5] = "bolero"
    selection[6] = "coney_island"
    selection[7] = "zingo"
    selection[8] = "leader"
    selection[9] = "spot_lite"
    selection[10] = "holiday"
    selection[11] = "atlantic_city"
    selection[12] = "miss_california"
    selection[13] = "palm_beach"
    selection[14] = "stars"
    selection[15] = "long_beach"
    selection[16] = "circus"
    selection[17] = "frolics"
    selection[18] = "showboat"
    selection[19] = "bright_spot"
    selection[20] = "bally_beauty"
    selection[21] = "beach_club"
    selection[22] = "rodeo_3"
    selection[23] = "yacht_club"
    selection[24] = "cabana"
    selection[25] = "dude_ranch"
    selection[26] = "tropics"
    selection[27] = "rodeo_1"
    selection[28] = "tahiti_1"
    selection[29] = "palm_springs"
    selection[30] = "rio"
    selection[31] = "ice_frolics"
    selection[32] = "havana"
    selection[33] = "surf_club"
    selection[34] = "mexico"
    selection[35] = "hi_fi"
    selection[36] = "hawaii_1"
    selection[37] = "variety"
    selection[38] = "nevada"
    selection[39] = "singapore"
    selection[40] = "big_time"
    selection[41] = "tropicana"
    selection[42] = "gayety"
    selection[43] = "manhattan"
    selection[44] = "gay_time"
    selection[45] = "serenade"
    selection[46] = "miami_beach"
    selection[47] = "triple_play"
    selection[48] = "beach_beauty"
    selection[49] = "pixies"
    selection[50] = "broadway"
    selection[51] = "starlet"
    selection[52] = "crosswords"
    selection[53] = "caravan"
    selection[54] = "spelling_bee"
    selection[55] = "night_club"
    selection[56] = "stardust"
    selection[57] = "parade"
    selection[58] = "south_seas"
    selection[59] = "double_header"
    selection[60] = "big_show"
    selection[61] = "monaco"
    selection[62] = "key_west"
    selection[63] = "brazil"
    selection[64] = "showtime"
    selection[65] = "sun_valley"
    selection[66] = "playtime"
    selection[67] = "fun_way"
    selection[68] = "miss_america"
    selection[69] = "cypress_gardens"
    selection[70] = "beach_time"
    selection[71] = "carnival_queen"
    selection[72] = "sea_island"
    selection[73] = "ballerina"
    selection[74] = "lotta_fun"
    selection[75] = "county_fair"
    selection[76] = "laguna_beach"
    selection[77] = "single_coin_pittsburgh"
    selection[78] = "roller_derby"
    selection[79] = "fun_spot"
    selection[80] = "barrel_o_fun"
    selection[81] = "touchdown"
    selection[82] = "circus_queen"
    selection[83] = "lite_a_line"
    selection[84] = "acapulco"
    selection[85] = "bikini"
    selection[86] = "barrel_o_fun_61"
    selection[87] = "fun_spot_61"
    selection[88] = "can_can"
    selection[89] = "lido"
    selection[90] = "shoot_a_line"
    selection[91] = "barrel_o_fun_62"
    selection[92] = "fun_spot_62"
    selection[93] = "fun_spot_63"
    selection[94] = "shoot_a_line_63"
    selection[95] = "golden_gate"
    selection[96] = "rainbow"
    selection[97] = "the_twist"
    selection[98] = "silver_sails"
    selection[99] = "bounty"
    selection[100] = "venus"
    selection[101] = "border_beauty"
    selection[102] = "beauty_beach"
    selection[103] = "folies_bergeres"
    selection[104] = "bahama_beach"
    selection[105] = "zodiac"
    selection[106] = "orient"
    selection[107] = "big_wheel"
    selection[108] = "venice"
    selection[109] = "magic_ring"
    selection[110] = "london"
    selection[111] = "safari"
    selection[112] = "super_7"
    selection[113] = "bonus_7"
    selection[114] = "hole_in_one"
    selection[115] = "stock_market"
    selection[116] = "double_up"
    selection[117] = "ticker_tape"
    selection[118] = "hawaii_2"
    selection[119] = "wall_street"
    selection[120] = "bali"
    selection[121] = "super_wall_street"
    selection[122] = "miss_america_75"
    selection[123] = "mystic_gate"
    selection[124] = "miss_universe"
    selection[125] = "continental_18"
    selection[126] = "blue_chip"
    selection[127] = "bull_market"
    selection[128] = "bonanza"
    selection[129] = "miss_america_supreme"
    selection[130] = "high_flyer"
    selection[131] = "miss_america_deluxe"
    selection[132] = "galaxy"
    selection[133] = "nashville"
    selection[134] = "dixieland"
    selection[135] = "tahiti_2"
    selection[136] = "malibu_beach"
    selection[137] = "continental"
    selection[138] = "mississippi_showboat"

    for i in range(1,135):
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
