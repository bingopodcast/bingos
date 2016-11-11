
import pygame
import random

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

meter = pygame.image.load('graphics/assets/black_register_cover.png').convert()
magic_screen = pygame.image.load('malibu_beach/assets/magic_screen.png').convert()
number_card = pygame.image.load('malibu_beach/assets/number_card.png').convert()
odds = pygame.image.load('malibu_beach/assets/odds.png').convert_alpha()
eb = pygame.image.load('malibu_beach/assets/eb.png').convert_alpha()
eb_number = pygame.image.load('malibu_beach/assets/eb_number.png').convert_alpha()
extra_balls = pygame.image.load('malibu_beach/assets/extra_balls.png').convert_alpha()
feature = pygame.image.load('malibu_beach/assets/time.png').convert_alpha()
ms_indicator = pygame.image.load('malibu_beach/assets/ms_indicator.png').convert_alpha()
ti = pygame.image.load('malibu_beach/assets/selection_arrow.png').convert_alpha()
super_section = pygame.image.load('malibu_beach/assets/super_section.png').convert_alpha()
orange_section = pygame.image.load('malibu_beach/assets/orange_section.png').convert_alpha()
ms_letter = pygame.image.load('malibu_beach/assets/ms_letter.png').convert_alpha()
number = pygame.image.load('malibu_beach/assets/number.png').convert_alpha()
select_now = pygame.image.load('malibu_beach/assets/select_now.png').convert_alpha()
three_blue = pygame.image.load('malibu_beach/assets/blue_section.png').convert_alpha()
tilt = pygame.image.load('malibu_beach/assets/tilt.png').convert_alpha()
m = pygame.image.load('malibu_beach/assets/m.png').convert_alpha()
red_m = pygame.image.load('malibu_beach/assets/red_m.png').convert_alpha()
a = pygame.image.load('malibu_beach/assets/a.png').convert_alpha()
red_a = pygame.image.load('malibu_beach/assets/red_a.png').convert_alpha()
l = pygame.image.load('malibu_beach/assets/l.png').convert_alpha()
red_l = pygame.image.load('malibu_beach/assets/red_l.png').convert_alpha()
i_letter = pygame.image.load('malibu_beach/assets/i.png').convert_alpha()
red_i = pygame.image.load('malibu_beach/assets/red_i.png').convert_alpha()
b = pygame.image.load('malibu_beach/assets/b.png').convert_alpha()
red_b = pygame.image.load('malibu_beach/assets/red_b.png').convert_alpha()
u = pygame.image.load('malibu_beach/assets/u.png').convert_alpha()
red_u = pygame.image.load('malibu_beach/assets/red_u.png').convert_alpha()

class scorereel():
    """ Score Reels are used to count replays """
    def __init__(self, pos, image):
        self.position = pos
        self.default_y = self.position[1]
        self.image = pygame.image.load(image).convert()

reel1 = scorereel([106,837], "graphics/assets/white_reel.png")
reel10 = scorereel([88,837], "graphics/assets/white_reel.png")
reel100 = scorereel([69,837], "graphics/assets/white_reel.png")
reel1000 = scorereel([50,837], "graphics/assets/white_reel.png")

def display(s, replays=0, menu=False):
    
    meter.set_colorkey((255,0,252))
    meter_position = [40,837]

    screen.blit(reel1.image, reel1.position)
    screen.blit(reel10.image, reel10.position)
    screen.blit(reel100.image, reel100.position)
    screen.blit(reel1000.image, reel1000.position)
    screen.blit(meter, meter_position)

    number_card_position = [235,343]

    screen.blit(number_card, number_card_position)

    magic_screen.set_colorkey((255,0,252))
    #default position 230x 359y
    #subtract 47 per position
    if s.game.magic_screen.position == 0:
        magic_screen_position = [240,338]
    elif s.game.magic_screen.position == 1:
        magic_screen_position = [192,338]
    elif s.game.magic_screen.position == 2:
        magic_screen_position = [145,338]
    elif s.game.magic_screen.position == 3:
        magic_screen_position = [96,338]
    elif s.game.magic_screen.position == 4:
        magic_screen_position = [49,338]
    elif s.game.magic_screen.position == 5:
        magic_screen_position = [3,338]
    elif s.game.magic_screen.position == 6:
        magic_screen_position = [-42,338]
    elif s.game.magic_screen.position == 7:
        magic_screen_position = [-89,338]
    elif s.game.magic_screen.position == 8:
        magic_screen_position = [-136,338]
    elif s.game.magic_screen.position == 9:
        magic_screen_position = [-183,338]


    screen.blit(magic_screen, magic_screen_position)

    backglass_position = [0, 0]
    backglass = pygame.Surface(screen.get_size(), flags=pygame.SRCALPHA)
    backglass.fill((0, 0, 0))
    if menu == True:
        backglass = pygame.image.load('malibu_beach/assets/malibu_beach_menu.png').convert()
        backglass.set_colorkey((255,0,252))
    else:
        if (s.game.anti_cheat.status == True):
            backglass = pygame.image.load('malibu_beach/assets/malibu_beach_gi.png').convert()
            backglass.set_colorkey((255,0,252))
        else:
            backglass = pygame.image.load('malibu_beach/assets/malibu_beach_off.png').convert()
            backglass.set_colorkey((255,0,252))
    backglass = pygame.transform.scale(backglass, (720, 1280))
    
    screen.blit(backglass, backglass_position)

    if s.game.green_odds.position < 4:
        rc = [4,164]
        screen.blit(red_m, rc)
    else:
        rc = [4,164]
        screen.blit(m, rc)

    if s.game.green_odds.position == 4:
        ro = [98,150]
        screen.blit(red_a, ro)
    else:
        ro = [98,150]
        screen.blit(a, ro)

    if s.game.green_odds.position == 5:
        ru = [158,153]
        screen.blit(red_l, ru)
    else:
        ru = [158,153]
        screen.blit(l, ru)

    if s.game.green_odds.position == 6:
        rn = [215,159]
        screen.blit(red_i, rn)
    else:
        rn = [215,159]
        screen.blit(i_letter, rn)

    if s.game.green_odds.position == 7:
        rt = [250,170]
        screen.blit(red_b, rt)
    else:
        rt = [250,170]
        screen.blit(b, rt)

    if s.game.green_odds.position == 8:
        ry = [305,186]
        screen.blit(red_u, ry)
    else:
        ry = [305,186]
        screen.blit(u, ry)



    if s.game.eb_play.status == True:
        eb_position = [36,1077]
        screen.blit(extra_balls, eb_position)

    if s.game.extra_ball.position >= 1:
        eb_position = [146,1077]
        screen.blit(eb_number, eb_position)
    if s.game.extra_ball.position >= 2:
        eb_position = [200,1077]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 3:
        eb_position = [260,1077]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 4:
        eb_position = [321,1077]
        screen.blit(eb_number, eb_position)
    if s.game.extra_ball.position >= 5:
        eb_position = [376,1077]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 6:
        eb_position = [439,1077]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 7:
        eb_position = [501,1077]
        screen.blit(eb_number, eb_position)
    if s.game.extra_ball.position >= 8:
        eb_position = [555,1077]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 9:
        eb_position = [618,1077]
        screen.blit(eb, eb_position)
    

    if s.game.selection_feature.position == 1:
        i = [684,570]
        screen.blit(ti, i)
    if s.game.selection_feature.position == 2 or s.game.selection_feature.position == 3:
        i = [684,504]
        screen.blit(ti, i)
    if s.game.selection_feature.position == 4 or s.game.selection_feature.position == 5 or s.game.selection_feature.position == 6:
        i = [684,438]
        screen.blit(ti, i)
    if s.game.selection_feature.position == 7:
        i = [684,375]
        screen.blit(ti, i)
    if s.game.selection_feature.position == 8:
        i = [684,308]
        screen.blit(ti, i)

    if s.game.red_star.status == True:
        rs_position = [557,421]
        screen.blit(feature, rs_position)
    if s.game.yellow_star.status == True:
        rs_position = [557,486]
        screen.blit(feature, rs_position)
    if s.game.orange_section.status == True:
        oss = [38,583]
        screen.blit(orange_section, oss)

    if s.game.magic_screen_feature.position >= 7 or s.game.ok.status == True:
        if s.game.selection_feature.position < 7:
            bfp = [557,552]
            screen.blit(feature, bfp)
        elif s.game.selection_feature.position == 7:
            bfp = [557,356]
            screen.blit(feature, bfp)
        elif s.game.selection_feature.position == 8:
            bfp = [557,291]
            screen.blit(feature, bfp)

    if s.game.magic_screen_feature.position >= 9:
        if s.game.three_blue.status == True:
            bp = [43,319]
            screen.blit(three_blue, bp)
        elif s.game.two_blue.status == True:
            bp = [104,319]
            screen.blit(three_blue, bp)

    if s.game.red_super_section.status == True:
        rss = [40,405]
        screen.blit(super_section, rss)
    if s.game.yellow_super_section.status == True:
        yss = [40,495]
        screen.blit(super_section, yss)

    if s.game.magic_screen_feature.position >= 4:
        ms = [145,678]
        screen.blit(ms_letter, ms)
    if s.game.magic_screen_feature.position >= 5:
        ms = [188,678]
        screen.blit(ms_letter, ms)
    if s.game.magic_screen_feature.position >= 6:
        ms = [232,678]
        screen.blit(ms_letter, ms)
    if s.game.magic_screen_feature.position >= 7:
        ms = [275,678]
        screen.blit(ms_letter, ms)
    if s.game.magic_screen_feature.position >= 8:
        ms = [319,678]
        screen.blit(ms_letter, ms)
    if s.game.magic_screen_feature.position >= 9:
        ms = [362,678]
        screen.blit(ms_letter, ms)
    if s.game.magic_screen_feature.position >= 10:
        ms = [405,678]
        screen.blit(ms_letter, ms)

    if s.game.ok.status == True:
        ms = [58,678]
        screen.blit(ms_letter, ms)
        ms = [16,678]
        screen.blit(ms_letter, ms)


    if s.game.magic_screen.position == 0:
        ms = [20,745]
        screen.blit(ms_indicator, ms)
    if s.game.magic_screen.position == 1:
        ms = [62,745]
        screen.blit(ms_indicator, ms)
    if s.game.magic_screen.position == 3:
        ms = [150,745]
        screen.blit(ms_indicator, ms)
    if s.game.magic_screen.position == 4:
        ms = [195,745]
        screen.blit(ms_indicator, ms)
    if s.game.magic_screen.position == 5:
        ms = [238,745]
        screen.blit(ms_indicator, ms)
    if s.game.magic_screen.position == 6:
        ms = [280,745]
        screen.blit(ms_indicator, ms)
    if s.game.magic_screen.position == 7:
        ms = [323,745]
        screen.blit(ms_indicator, ms)
    if s.game.magic_screen.position == 8:
        ms = [368,745]
        screen.blit(ms_indicator, ms)
    if s.game.magic_screen.position == 9:
        ms = [410,745]
        screen.blit(ms_indicator, ms)

    if s.game.tilt.status == False:
        if s.holes:
            if 1 in s.holes:
                number_position = [287,353]
                screen.blit(number, number_position)
            if 2 in s.holes:
                number_position = [333,353]
                screen.blit(number, number_position)
            if 3 in s.holes:
                number_position = [382,548]
                screen.blit(number, number_position)
            if 4 in s.holes:
                number_position = [238,403]
                screen.blit(number, number_position)
            if 5 in s.holes:
                number_position = [335,500]
                screen.blit(number, number_position)
            if 6 in s.holes:
                number_position = [238,500]
                screen.blit(number, number_position)
            if 7 in s.holes:
                number_position = [333,403]
                screen.blit(number, number_position)
            if 8 in s.holes:
                number_position = [286,548]
                screen.blit(number, number_position)
            if 9 in s.holes:
                number_position = [240,354]
                screen.blit(number, number_position)
            if 10 in s.holes:
                number_position = [430,545]
                screen.blit(number, number_position)
            if 11 in s.holes:
                number_position = [382,353]
                screen.blit(number, number_position)
            if 12 in s.holes:
                number_position = [238,548]
                screen.blit(number, number_position)
            if 13 in s.holes:
                number_position = [382,450]
                screen.blit(number, number_position)
            if 14 in s.holes:
                number_position = [334,549]
                screen.blit(number, number_position)
            if 15 in s.holes:
                number_position = [428,353]
                screen.blit(number, number_position)
            if 16 in s.holes:
                number_position = [334,450]
                screen.blit(number, number_position)
            if 17 in s.holes:
                number_position = [428,450]
                screen.blit(number, number_position)
            if 18 in s.holes:
                number_position = [428,403]
                screen.blit(number, number_position)
            if 19 in s.holes:
                number_position = [285,401]
                screen.blit(number, number_position)
            if 20 in s.holes:
                number_position = [430,500]
                screen.blit(number, number_position)
            if 21 in s.holes:
                number_position = [382,500]
                screen.blit(number, number_position)
            if 22 in s.holes:
                number_position = [382,401]
                screen.blit(number, number_position)
            if 23 in s.holes:
                number_position = [286,500]
                screen.blit(number, number_position)
            if 24 in s.holes:
                number_position = [286,450]
                screen.blit(number, number_position)
            if 25 in s.holes:
                number_position = [240,450]
                screen.blit(number, number_position)

    if s.game.red_odds.position == 1:
        o = [195,865]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 2:
        o = [264,865]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 3:
        o = [339,865]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 4:
        o = [408,865]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 5:
        o = [470,865]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 6:
        o = [530,865]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 7:
        o = [578,865]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 8:
        o = [628,865]
        screen.blit(odds, o)

    if s.game.yellow_odds.position == 1:
        o = [195,937]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 2:
        o = [264,937]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 3:
        o = [339,937]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 4:
        o = [408,937]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 5:
        o = [470,937]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 6:
        o = [530,937]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 7:
        o = [578,937]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 8:
        o = [628,937]
        screen.blit(odds, o)

    if s.game.green_odds.position == 1:
        o = [195,1008]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 2:
        o = [264,1008]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 3:
        o = [339,1008]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 4:
        o = [408,1008]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 5:
        o = [470,1008]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 6:
        o = [530,1008]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 7:
        o = [578,1008]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 8:
        o = [628,1008]
        screen.blit(odds, o)


    if s.game.tilt.status == True:
        tilt_position = [572,640]
        screen.blit(tilt, tilt_position)

    pygame.display.update()

def eb_animation(num):
    global screen
    
    if num == 3:
        eb_position = [146,1077]
        screen.blit(eb_number, eb_position)
        pygame.display.update()
    if num == 2:
        eb_position = [200,1077]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 1:
        eb_position = [260,1077]
        screen.blit(eb, eb_position)
        pygame.display.update()


def feature_animation(num):
    global screen
    if num == 4:
        rss = [40,405]
        screen.blit(super_section, rss)
        pygame.display.update()
    else:
        yss = [40,495]
        screen.blit(super_section, yss)
        pygame.display.update()


def odds_animation(num):
    global screen

    if num == 8:
        odds_position = [195,865]
        screen.blit(odds, odds_position)
    if num == 7:
        odds_position = [264,937]
        screen.blit(odds, odds_position)
    if num == 6:
        odds_position = [339,1008]
        screen.blit(odds, odds_position)
    if num == 5:
        odds_position = [408,865]
        screen.blit(odds, odds_position)
    if num == 4:
        odds_position = [470,937]
        screen.blit(odds, odds_position)
    if num == 3:
        odds_position = [530,1008]
        screen.blit(odds, odds_position)
    if num == 2:
        odds_position = [578,865]
        screen.blit(odds, odds_position)
    if num == 1:
        odds_position = [628,937]
        screen.blit(odd, odds_position)
    pygame.display.update()

