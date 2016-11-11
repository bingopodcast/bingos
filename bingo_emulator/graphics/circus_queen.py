
import pygame
import random

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

meter = pygame.image.load('graphics/assets/register_cover.png').convert()
magic_screen = pygame.image.load('circus_queen/assets/magic_screen.png').convert()
number_card = pygame.image.load('circus_queen/assets/number_card.png').convert()
odds = pygame.image.load('circus_queen/assets/odds.png').convert_alpha()
eb = pygame.image.load('circus_queen/assets/eb.png').convert_alpha()
eb_number = pygame.image.load('circus_queen/assets/eb_number.png').convert_alpha()
extra_balls = pygame.image.load('circus_queen/assets/extra_balls.png').convert_alpha()
time = pygame.image.load('circus_queen/assets/time.png').convert_alpha()
ms_indicator = pygame.image.load('circus_queen/assets/ms_indicator.png').convert_alpha()
ti = pygame.image.load('circus_queen/assets/time_indicator.png').convert_alpha()
super_section = pygame.image.load('circus_queen/assets/super_section.png').convert_alpha()
orange_section = pygame.image.load('circus_queen/assets/orange_section.png').convert_alpha()
ms_letter = pygame.image.load('circus_queen/assets/ms_letter.png').convert_alpha()
number = pygame.image.load('circus_queen/assets/number.png').convert_alpha()
select_now = pygame.image.load('circus_queen/assets/select_now.png').convert_alpha()
blue_section = pygame.image.load('circus_queen/assets/blue_section.png').convert_alpha()
tilt = pygame.image.load('circus_queen/assets/tilt.png').convert_alpha()
c = pygame.image.load('circus_queen/assets/c.png').convert_alpha()
red_c = pygame.image.load('circus_queen/assets/red_c.png').convert_alpha()
i_letter = pygame.image.load('circus_queen/assets/i.png').convert_alpha()
red_i = pygame.image.load('circus_queen/assets/red_i.png').convert_alpha()
r = pygame.image.load('circus_queen/assets/r.png').convert_alpha()
red_r = pygame.image.load('circus_queen/assets/red_r.png').convert_alpha()
c2 = pygame.image.load('circus_queen/assets/c2.png').convert_alpha()
red_c2 = pygame.image.load('circus_queen/assets/red_c2.png').convert_alpha()
u = pygame.image.load('circus_queen/assets/u.png').convert_alpha()
red_u = pygame.image.load('circus_queen/assets/red_u.png').convert_alpha()
s_letter = pygame.image.load('circus_queen/assets/s.png').convert_alpha()
red_s = pygame.image.load('circus_queen/assets/red_s.png').convert_alpha()
button = pygame.image.load('circus_queen/assets/button.png').convert_alpha()

class scorereel():
    """ Score Reels are used to count replays """
    def __init__(self, pos, image):
        self.position = pos
        self.default_y = self.position[1]
        self.image = pygame.image.load(image).convert()

reel1 = scorereel([102,793], "graphics/assets/white_reel.png")
reel10 = scorereel([83,793], "graphics/assets/white_reel.png")
reel100 = scorereel([64,793], "graphics/assets/white_reel.png")

def display(s, replays=0, menu=False):
    
    meter.set_colorkey((255,0,252))
    meter_position = [55,793]

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
        backglass = pygame.image.load('circus_queen/assets/circus_queen_menu.png').convert()
        backglass.set_colorkey((255,0,252))
    else:
        if (s.game.anti_cheat.status == True):
            backglass = pygame.image.load('circus_queen/assets/circus_queen_gi.png').convert()
            backglass.set_colorkey((255,0,252))
        else:
            backglass = pygame.image.load('circus_queen/assets/circus_queen_off.png').convert()
            backglass.set_colorkey((255,0,252))
    backglass = pygame.transform.scale(backglass, (720, 1280))
    
    screen.blit(backglass, backglass_position)

    if s.game.green_odds.position < 4:
        rc = [53,261]
        screen.blit(red_c, rc)
    else:
        rc = [53,261]
        screen.blit(c, rc)

    if s.game.green_odds.position == 4:
        ri = [97,264]
        screen.blit(red_i, ri)
    else:
        ri = [97,264]
        screen.blit(i_letter, ri)

    if s.game.green_odds.position == 5:
        rr = [145,265]
        screen.blit(red_r, rr)
    else:
        rr = [143,267]
        screen.blit(r, rr)

    if s.game.green_odds.position == 6:
        rc2 = [206,264]
        screen.blit(red_c2, rc2)
    else:
        rc2 = [206,265]
        screen.blit(c2, rc2)

    if s.game.green_odds.position == 7:
        ru = [259,262]
        screen.blit(red_u, ru)
    else:
        ru = [260,264]
        screen.blit(u, ru)

    if s.game.green_odds.position == 8:
        rs = [314,265]
        screen.blit(red_s, rs)
    else:
        rs = [312,267]
        screen.blit(s_letter, rs)


    if s.game.eb_play.status == True:
        eb_position = [40,1028]
        screen.blit(extra_balls, eb_position)

    if s.game.extra_ball.position >= 1:
        eb_position = [151,1026]
        screen.blit(eb_number, eb_position)
    if s.game.extra_ball.position >= 2:
        eb_position = [198,1025]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 3:
        eb_position = [263,1025]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 4:
        eb_position = [329,1025]
        screen.blit(eb_number, eb_position)
    if s.game.extra_ball.position >= 5:
        eb_position = [375,1025]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 6:
        eb_position = [439,1025]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 7:
        eb_position = [506,1025]
        screen.blit(eb_number, eb_position)
    if s.game.extra_ball.position >= 8:
        eb_position = [556,1025]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 9:
        eb_position = [617,1025]
        screen.blit(eb, eb_position)
    

    if s.game.selection_feature.position == 1:
        i = [672,594]
        screen.blit(ti, i)
    if s.game.selection_feature.position == 2 or s.game.selection_feature.position == 3:
        i = [672,534]
        screen.blit(ti, i)
    if s.game.selection_feature.position == 4 or s.game.selection_feature.position == 5 or s.game.selection_feature.position == 6:
        i = [672,482]
        screen.blit(ti, i)
    if s.game.selection_feature.position == 7:
        i = [672,429]
        screen.blit(ti, i)
    if s.game.selection_feature.position == 8:
        i = [672,368]
        screen.blit(ti, i)

    if s.game.red_star.status == True:
        rs_position = [552,473]
        screen.blit(time, rs_position)
    if s.game.yellow_star.status == True:
        rs_position = [552,527]
        screen.blit(time, rs_position)

    if s.game.magic_screen_feature.position >= 7 or s.game.ok.status == True:
        if s.game.selection_feature.position < 7:
            bfp = [552,580]
            screen.blit(time, bfp)
        elif s.game.selection_feature.position == 7:
            bfp = [552,417]
            screen.blit(time, bfp)
        elif s.game.selection_feature.position == 8:
            bfp = [553,362]
            screen.blit(time, bfp)

    if s.game.magic_screen_feature.position >= 9:
        if s.game.three_blue.status == True:
            bp = [52,350]
            screen.blit(blue_section, bp)
        elif s.game.three_blue_six.status == True:
            bp = [95,349]
            screen.blit(blue_section, bp)
        elif s.game.two_blue.status == True:
            bp = [139,350]
            screen.blit(blue_section, bp)


    if s.game.ball_count.position < 1:
        if s.game.odds_only.status == True:
            b = [22,870]
            screen.blit(button, b)
        elif s.game.features.status == True:
            b = [22,920]
            screen.blit(button, b)
        else:
            b = [22,970]
            screen.blit(button, b)


    if s.game.red_super_section.status == True:
        rss = [55,422]
        screen.blit(super_section, rss)
    if s.game.yellow_super_section.status == True:
        yss = [55,497]
        screen.blit(super_section, yss)
    if s.game.orange_section.status == True:
        oss = [55,572]
        screen.blit(orange_section, oss)

    if s.game.magic_screen_feature.position >= 4:
        ms = [162,672]
        screen.blit(ms_letter, ms)
    if s.game.magic_screen_feature.position >= 5:
        ms = [202,672]
        screen.blit(ms_letter, ms)
    if s.game.magic_screen_feature.position >= 6:
        ms = [243,672]
        screen.blit(ms_letter, ms)
    if s.game.magic_screen_feature.position >= 7:
        ms = [283,672]
        screen.blit(ms_letter, ms)
    if s.game.magic_screen_feature.position >= 8:
        ms = [324,672]
        screen.blit(ms_letter, ms)
    if s.game.magic_screen_feature.position >= 9:
        ms = [364,672]
        screen.blit(ms_letter, ms)
    if s.game.magic_screen_feature.position >= 10:
        ms = [405,672]
        screen.blit(ms_letter, ms)

    if s.game.ok.status == True:
        ms = [76,672]
        screen.blit(ms_letter, ms)
        ms = [34,672]
        screen.blit(ms_letter, ms)


    if s.game.magic_screen.position == 0:
        ms = [37,724]
        screen.blit(ms_indicator, ms)
    if s.game.magic_screen.position == 1:
        ms = [80,724]
        screen.blit(ms_indicator, ms)
    if s.game.magic_screen.position == 3:
        ms = [165,724]
        screen.blit(ms_indicator, ms)
    if s.game.magic_screen.position == 4:
        ms = [207,724]
        screen.blit(ms_indicator, ms)
    if s.game.magic_screen.position == 5:
        ms = [245,724]
        screen.blit(ms_indicator, ms)
    if s.game.magic_screen.position == 6:
        ms = [287,724]
        screen.blit(ms_indicator, ms)
    if s.game.magic_screen.position == 7:
        ms = [330,724]
        screen.blit(ms_indicator, ms)
    if s.game.magic_screen.position == 8:
        ms = [369,724]
        screen.blit(ms_indicator, ms)
    if s.game.magic_screen.position == 9:
        ms = [409,724]
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
        o = [187,772]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 2:
        o = [247,772]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 3:
        o = [309,772]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 4:
        o = [370,772]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 5:
        o = [423,772]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 6:
        o = [472,772]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 7:
        o = [522,772]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 8:
        o = [568,772]
        screen.blit(odds, o)

    if s.game.yellow_odds.position == 1:
        o = [187,838]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 2:
        o = [247,838]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 3:
        o = [309,838]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 4:
        o = [370,838]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 5:
        o = [423,838]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 6:
        o = [472,838]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 7:
        o = [522,838]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 8:
        o = [568,838]
        screen.blit(odds, o)

    if s.game.green_odds.position == 1:
        o = [187,908]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 2:
        o = [247,908]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 3:
        o = [309,908]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 4:
        o = [370,908]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 5:
        o = [423,908]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 6:
        o = [472,908]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 7:
        o = [522,908]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 8:
        o = [568,908]
        screen.blit(odds, o)


    if s.game.tilt.status == True:
        tilt_position = [572,635]
        screen.blit(tilt, tilt_position)

    pygame.display.update()

def eb_animation(num):
    global screen
    
    if num == 3:
        eb_position = [151,1026]
        screen.blit(eb_number, eb_position)
        pygame.display.update()
    if num == 2:
        eb_position = [198,1025]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 1:
        eb_position = [263,1025]
        screen.blit(eb, eb_position)
        pygame.display.update()


def feature_animation(num):
    global screen
    if num == 4:
        rss = [55,422]
        screen.blit(super_section, rss)
        pygame.display.update()
    else:
        yss = [55,497]
        screen.blit(super_section, yss)
        pygame.display.update()


def odds_animation(num):
    global screen

    if num == 8:
        odds_position = [187,772]
        screen.blit(odds, odds_position)
    if num == 7:
        odds_position = [247,838]
        screen.blit(odds, odds_position)
    if num == 6:
        odds_position = [309,908]
        screen.blit(odds, odds_position)
    if num == 5:
        odds_position = [370,772]
        screen.blit(odds, odds_position)
    if num == 4:
        odds_position = [423,838]
        screen.blit(odds, odds_position)
    if num == 3:
        odds_position = [472,908]
        screen.blit(odds, odds_position)
    if num == 2:
        odds_position = [522,772]
        screen.blit(odds, odds_position)
    if num == 1:
        odds_position = [568,838]
        screen.blit(odd, odds_position)
    pygame.display.update()


