
import pygame
import random

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

meter = pygame.image.load('graphics/assets/register_cover.png').convert()
magic_screen = pygame.image.load('roller_derby/assets/magic_screen.png').convert()
number_card = pygame.image.load('roller_derby/assets/number_card.png').convert()
odds = pygame.image.load('roller_derby/assets/odds.png').convert_alpha()
eb = pygame.image.load('roller_derby/assets/eb.png').convert_alpha()
eb_number = pygame.image.load('roller_derby/assets/eb_number.png').convert_alpha()
extra_balls = pygame.image.load('roller_derby/assets/extra_balls.png').convert_alpha()
time = pygame.image.load('roller_derby/assets/time.png').convert_alpha()
ms_indicator = pygame.image.load('roller_derby/assets/ms_indicator.png').convert_alpha()
ti = pygame.image.load('roller_derby/assets/time_indicator.png').convert_alpha()
super_section = pygame.image.load('roller_derby/assets/super_section.png').convert_alpha()
orange_section = pygame.image.load('roller_derby/assets/orange_section.png').convert_alpha()
ms_letter = pygame.image.load('roller_derby/assets/ms_letter.png').convert_alpha()
number = pygame.image.load('roller_derby/assets/number.png').convert_alpha()
select_now = pygame.image.load('roller_derby/assets/select_now.png').convert_alpha()
blue_section = pygame.image.load('roller_derby/assets/blue_section.png').convert_alpha()
tilt = pygame.image.load('roller_derby/assets/tilt.png').convert_alpha()
r = pygame.image.load('roller_derby/assets/r.png').convert_alpha()
red_r = pygame.image.load('roller_derby/assets/red_r.png').convert_alpha()
o_letter = pygame.image.load('roller_derby/assets/o.png').convert_alpha()
red_o = pygame.image.load('roller_derby/assets/red_o.png').convert_alpha()
l = pygame.image.load('roller_derby/assets/l.png').convert_alpha()
red_l = pygame.image.load('roller_derby/assets/red_l.png').convert_alpha()
l2 = pygame.image.load('roller_derby/assets/l2.png').convert_alpha()
red_l2 = pygame.image.load('roller_derby/assets/red_l2.png').convert_alpha()
e = pygame.image.load('roller_derby/assets/e.png').convert_alpha()
red_e = pygame.image.load('roller_derby/assets/red_e.png').convert_alpha()
r2 = pygame.image.load('roller_derby/assets/r2.png').convert_alpha()
red_r2 = pygame.image.load('roller_derby/assets/red_r2.png').convert_alpha()
button = pygame.image.load('roller_derby/assets/button.png').convert_alpha()

class scorereel():
    """ Score Reels are used to count replays """
    def __init__(self, pos, image):
        self.position = pos
        self.default_y = self.position[1]
        self.image = pygame.image.load(image).convert()

reel1 = scorereel([88,795], "graphics/assets/white_reel.png")
reel10 = scorereel([69,795], "graphics/assets/white_reel.png")
reel100 = scorereel([49,795], "graphics/assets/white_reel.png")

def display(s, replays=0, menu=False):
    
    meter.set_colorkey((255,0,252))
    meter_position = [40,795]

    screen.blit(reel1.image, reel1.position)
    screen.blit(reel10.image, reel10.position)
    screen.blit(reel100.image, reel100.position)
    screen.blit(meter, meter_position)

    number_card_position = [235,363]

    screen.blit(number_card, number_card_position)

    magic_screen.set_colorkey((255,0,252))
    #default position 230x 359y
    #subtract 47 per position
    if s.game.magic_screen.position == 0:
        magic_screen_position = [240,358]
    elif s.game.magic_screen.position == 1:
        magic_screen_position = [192,358]
    elif s.game.magic_screen.position == 2:
        magic_screen_position = [145,358]
    elif s.game.magic_screen.position == 3:
        magic_screen_position = [96,358]
    elif s.game.magic_screen.position == 4:
        magic_screen_position = [49,358]
    elif s.game.magic_screen.position == 5:
        magic_screen_position = [3,358]
    elif s.game.magic_screen.position == 6:
        magic_screen_position = [-42,358]
    elif s.game.magic_screen.position == 7:
        magic_screen_position = [-89,358]
    elif s.game.magic_screen.position == 8:
        magic_screen_position = [-136,358]
    elif s.game.magic_screen.position == 9:
        magic_screen_position = [-183,358]


    screen.blit(magic_screen, magic_screen_position)

    backglass_position = [0, 0]
    backglass = pygame.Surface(screen.get_size(), flags=pygame.SRCALPHA)
    backglass.fill((0, 0, 0))
    if menu == True:
        backglass = pygame.image.load('roller_derby/assets/roller_derby_menu.png').convert()
        backglass.set_colorkey((255,0,252))
    else:
        if (s.game.anti_cheat.status == True):
            backglass = pygame.image.load('roller_derby/assets/roller_derby_gi.png').convert()
            backglass.set_colorkey((255,0,252))
        else:
            backglass = pygame.image.load('roller_derby/assets/roller_derby_off.png').convert()
            backglass.set_colorkey((255,0,252))
    backglass = pygame.transform.scale(backglass, (720, 1280))
    
    screen.blit(backglass, backglass_position)

    if s.game.green_odds.position < 4:
        rc = [45,255]
        screen.blit(red_r, rc)
    else:
        rc = [45,255]
        screen.blit(r, rc)

    if s.game.green_odds.position == 4:
        ri = [97,257]
        screen.blit(red_o, ri)
    else:
        ri = [97,257]
        screen.blit(o_letter, ri)

    if s.game.green_odds.position == 5:
        rr = [147,255]
        screen.blit(red_l, rr)
    else:
        rr = [147,255]
        screen.blit(l, rr)

    if s.game.green_odds.position == 6:
        rc2 = [192,255]
        screen.blit(red_l2, rc2)
    else:
        rc2 = [192,255]
        screen.blit(l2, rc2)

    if s.game.green_odds.position == 7:
        ru = [237,254]
        screen.blit(red_e, ru)
    else:
        ru = [237,254]
        screen.blit(e, ru)

    if s.game.green_odds.position == 8:
        rs = [297,255]
        screen.blit(red_r2, rs)
    else:
        rs = [297,255]
        screen.blit(r2, rs)


    if s.game.eb_play.status == True:
        eb_position = [31,1027]
        screen.blit(extra_balls, eb_position)

    if s.game.extra_ball.position >= 1:
        eb_position = [140,1027]
        screen.blit(eb_number, eb_position)
    if s.game.extra_ball.position >= 2:
        eb_position = [190,1030]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 3:
        eb_position = [253,1030]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 4:
        eb_position = [322,1028]
        screen.blit(eb_number, eb_position)
    if s.game.extra_ball.position >= 5:
        eb_position = [370,1028]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 6:
        eb_position = [433,1028]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 7:
        eb_position = [500,1027]
        screen.blit(eb_number, eb_position)
    if s.game.extra_ball.position >= 8:
        eb_position = [550,1027]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 9:
        eb_position = [613,1027]
        screen.blit(eb, eb_position)
    

    if s.game.selection_feature.position == 1:
        i = [678,590]
        screen.blit(ti, i)
    if s.game.selection_feature.position == 2 or s.game.selection_feature.position == 3:
        i = [678,530]
        screen.blit(ti, i)
    if s.game.selection_feature.position == 4 or s.game.selection_feature.position == 5 or s.game.selection_feature.position == 6:
        i = [678,479]
        screen.blit(ti, i)
    if s.game.selection_feature.position == 7:
        i = [678,426]
        screen.blit(ti, i)
    if s.game.selection_feature.position == 8:
        i = [678,365]
        screen.blit(ti, i)

    if s.game.red_star.status == True:
        rs_position = [551,465]
        screen.blit(time, rs_position)
    if s.game.yellow_star.status == True:
        rs_position = [551,521]
        screen.blit(time, rs_position)

    if s.game.magic_screen_feature.position >= 7 or s.game.ok.status == True:
        if s.game.selection_feature.position < 7:
            bfp = [551,577]
            screen.blit(time, bfp)
        elif s.game.selection_feature.position == 7:
            bfp = [551,409]
            screen.blit(time, bfp)
        elif s.game.selection_feature.position == 8:
            bfp = [551,355]
            screen.blit(time, bfp)

    if s.game.magic_screen_feature.position >= 9:
        if s.game.three_blue.status == True:
            bp = [40,340]
            screen.blit(blue_section, bp)
        elif s.game.two_blue.status == True:
            bp = [102,340]
            screen.blit(blue_section, bp)


    if s.game.ball_count.position < 1:
        if s.game.odds_only.status == True:
            b = [11,875]
            screen.blit(button, b)
        elif s.game.features.status == True:
            b = [11,925]
            screen.blit(button, b)
        else:
            b = [11,976]
            screen.blit(button, b)


    if s.game.red_super_section.status == True:
        rss = [37,416]
        screen.blit(super_section, rss)
    if s.game.yellow_super_section.status == True:
        yss = [37,495]
        screen.blit(super_section, yss)
    if s.game.orange_section.status == True:
        oss = [37,570]
        screen.blit(orange_section, oss)

    if s.game.magic_screen_feature.position >= 4:
        ms = [144,674]
        screen.blit(ms_letter, ms)
    if s.game.magic_screen_feature.position >= 5:
        ms = [188,672]
        screen.blit(ms_letter, ms)
    if s.game.magic_screen_feature.position >= 6:
        ms = [230,672]
        screen.blit(ms_letter, ms)
    if s.game.magic_screen_feature.position >= 7:
        ms = [273,672]
        screen.blit(ms_letter, ms)
    if s.game.magic_screen_feature.position >= 8:
        ms = [313,672]
        screen.blit(ms_letter, ms)
    if s.game.magic_screen_feature.position >= 9:
        ms = [358,672]
        screen.blit(ms_letter, ms)
    if s.game.magic_screen_feature.position >= 10:
        ms = [400,672]
        screen.blit(ms_letter, ms)

    if s.game.ok.status == True:
        ms = [58,672]
        screen.blit(ms_letter, ms)
        ms = [16,672]
        screen.blit(ms_letter, ms)


    if s.game.magic_screen.position == 0:
        ms = [16,724]
        screen.blit(ms_indicator, ms)
    if s.game.magic_screen.position == 1:
        ms = [63,724]
        screen.blit(ms_indicator, ms)
    if s.game.magic_screen.position == 3:
        ms = [147,724]
        screen.blit(ms_indicator, ms)
    if s.game.magic_screen.position == 4:
        ms = [190,724]
        screen.blit(ms_indicator, ms)
    if s.game.magic_screen.position == 5:
        ms = [233,724]
        screen.blit(ms_indicator, ms)
    if s.game.magic_screen.position == 6:
        ms = [275,724]
        screen.blit(ms_indicator, ms)
    if s.game.magic_screen.position == 7:
        ms = [319,724]
        screen.blit(ms_indicator, ms)
    if s.game.magic_screen.position == 8:
        ms = [360,724]
        screen.blit(ms_indicator, ms)
    if s.game.magic_screen.position == 9:
        ms = [403,724]
        screen.blit(ms_indicator, ms)

    if s.game.tilt.status == False:
        if s.holes:
            if 1 in s.holes:
                number_position = [287,373]
                screen.blit(number, number_position)
            if 2 in s.holes:
                number_position = [333,373]
                screen.blit(number, number_position)
            if 3 in s.holes:
                number_position = [382,568]
                screen.blit(number, number_position)
            if 4 in s.holes:
                number_position = [238,423]
                screen.blit(number, number_position)
            if 5 in s.holes:
                number_position = [335,520]
                screen.blit(number, number_position)
            if 6 in s.holes:
                number_position = [238,520]
                screen.blit(number, number_position)
            if 7 in s.holes:
                number_position = [333,423]
                screen.blit(number, number_position)
            if 8 in s.holes:
                number_position = [286,568]
                screen.blit(number, number_position)
            if 9 in s.holes:
                number_position = [240,374]
                screen.blit(number, number_position)
            if 10 in s.holes:
                number_position = [430,565]
                screen.blit(number, number_position)
            if 11 in s.holes:
                number_position = [382,373]
                screen.blit(number, number_position)
            if 12 in s.holes:
                number_position = [238,568]
                screen.blit(number, number_position)
            if 13 in s.holes:
                number_position = [382,470]
                screen.blit(number, number_position)
            if 14 in s.holes:
                number_position = [334,569]
                screen.blit(number, number_position)
            if 15 in s.holes:
                number_position = [428,373]
                screen.blit(number, number_position)
            if 16 in s.holes:
                number_position = [334,470]
                screen.blit(number, number_position)
            if 17 in s.holes:
                number_position = [428,470]
                screen.blit(number, number_position)
            if 18 in s.holes:
                number_position = [428,423]
                screen.blit(number, number_position)
            if 19 in s.holes:
                number_position = [285,421]
                screen.blit(number, number_position)
            if 20 in s.holes:
                number_position = [430,520]
                screen.blit(number, number_position)
            if 21 in s.holes:
                number_position = [382,520]
                screen.blit(number, number_position)
            if 22 in s.holes:
                number_position = [382,421]
                screen.blit(number, number_position)
            if 23 in s.holes:
                number_position = [286,520]
                screen.blit(number, number_position)
            if 24 in s.holes:
                number_position = [286,470]
                screen.blit(number, number_position)
            if 25 in s.holes:
                number_position = [240,470]
                screen.blit(number, number_position)

    if s.game.red_odds.position == 1:
        o = [175,778]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 2:
        o = [239,778]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 3:
        o = [300,778]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 4:
        o = [364,778]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 5:
        o = [418,778]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 6:
        o = [468,778]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 7:
        o = [518,778]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 8:
        o = [566,778]
        screen.blit(odds, o)

    if s.game.yellow_odds.position == 1:
        o = [175,845]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 2:
        o = [239,845]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 3:
        o = [300,845]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 4:
        o = [364,845]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 5:
        o = [418,845]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 6:
        o = [468,845]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 7:
        o = [518,845]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 8:
        o = [566,845]
        screen.blit(odds, o)

    if s.game.green_odds.position == 1:
        o = [175,913]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 2:
        o = [239,913]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 3:
        o = [300,913]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 4:
        o = [364,913]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 5:
        o = [418,913]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 6:
        o = [468,913]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 7:
        o = [518,913]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 8:
        o = [566,913]
        screen.blit(odds, o)


    if s.game.tilt.status == True:
        tilt_position = [572,635]
        screen.blit(tilt, tilt_position)

    pygame.display.update()

def eb_animation(num):
    global screen

    if num == 3:
        eb_position = [140,1027]
        screen.blit(eb_number, eb_position)
        pygame.display.update()
    if num == 2:
        eb_position = [190,1030]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 1:
        eb_position = [253,1030]
        screen.blit(eb, eb_position)
        pygame.display.update()


def feature_animation(num):
    global screen
    if num == 4:
        rss = [37,416]
        screen.blit(super_section, rss)
        pygame.display.update()
    else:
        yss = [37,495]
        screen.blit(super_section, yss)
        pygame.display.update()


def odds_animation(num):
    global screen

    if num == 8:
        odds_position = [175,778]
        screen.blit(odds, odds_position)
    if num == 7:
        odds_position = [239,845]
        screen.blit(odds, odds_position)
    if num == 6:
        odds_position = [300,913]
        screen.blit(odds, odds_position)
    if num == 5:
        odds_position = [364,778]
        screen.blit(odds, odds_position)
    if num == 4:
        odds_position = [418,845]
        screen.blit(odds, odds_position)
    if num == 3:
        odds_position = [468,913]
        screen.blit(odds, odds_position)
    if num == 2:
        odds_position = [518,778]
        screen.blit(odds, odds_position)
    if num == 1:
        odds_position = [566,845]
        screen.blit(odd, odds_position)
    pygame.display.update()


