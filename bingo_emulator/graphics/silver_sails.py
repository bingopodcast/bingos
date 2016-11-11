
import pygame
import random

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

meter = pygame.image.load('graphics/assets/register_cover.png').convert()
magic_screen = pygame.image.load('silver_sails/assets/magic_screen.png').convert()
number_card = pygame.image.load('silver_sails/assets/number_card.png').convert()
odds = pygame.image.load('silver_sails/assets/odds.png').convert_alpha()
eb = pygame.image.load('silver_sails/assets/eb.png').convert_alpha()
eb_number = pygame.image.load('silver_sails/assets/eb_number.png').convert_alpha()
extra_balls = pygame.image.load('silver_sails/assets/extra_balls.png').convert_alpha()
time = pygame.image.load('silver_sails/assets/time.png').convert_alpha()
ms_indicator = pygame.image.load('silver_sails/assets/ms_indicator.png').convert_alpha()
ti = pygame.image.load('silver_sails/assets/time_indicator.png').convert_alpha()
super_section = pygame.image.load('silver_sails/assets/super_section.png').convert_alpha()
ms_letter = pygame.image.load('silver_sails/assets/ms_letter.png').convert_alpha()
number = pygame.image.load('silver_sails/assets/number.png').convert_alpha()
select_now = pygame.image.load('silver_sails/assets/select_now.png').convert_alpha()
blue_section = pygame.image.load('silver_sails/assets/blue_section.png').convert_alpha()
gold_section = pygame.image.load('silver_sails/assets/gold_section.png').convert_alpha()
gold_arrow = pygame.image.load('silver_sails/assets/gold_arrow.png').convert_alpha()
gold_odds = pygame.image.load('silver_sails/assets/gold_odds.png').convert_alpha()
golden_game = pygame.image.load('silver_sails/assets/golden_game.png').convert_alpha()
tilt = pygame.image.load('silver_sails/assets/tilt.png').convert_alpha()
button = pygame.image.load('silver_sails/assets/button.png').convert_alpha()
ok_gate = pygame.image.load('silver_sails/assets/ok_gate.png').convert_alpha()
red_s = pygame.image.load('silver_sails/assets/red_s.png').convert_alpha()
s_letter = pygame.image.load('silver_sails/assets/s.png').convert_alpha()
red_i = pygame.image.load('silver_sails/assets/red_i.png').convert_alpha()
i_letter = pygame.image.load('silver_sails/assets/i_letter.png').convert_alpha()
red_l = pygame.image.load('silver_sails/assets/red_l.png').convert_alpha()
l = pygame.image.load('silver_sails/assets/l.png').convert_alpha()
red_v = pygame.image.load('silver_sails/assets/red_v.png').convert_alpha()
v = pygame.image.load('silver_sails/assets/v.png').convert_alpha()
red_e = pygame.image.load('silver_sails/assets/red_e.png').convert_alpha()
e = pygame.image.load('silver_sails/assets/e.png').convert_alpha()
red_r = pygame.image.load('silver_sails/assets/red_r.png').convert_alpha()
r = pygame.image.load('silver_sails/assets/r.png').convert_alpha()

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
        magic_screen_position = [228,360]
    elif s.game.magic_screen.position == 1:
        magic_screen_position = [181,360]
    elif s.game.magic_screen.position == 2:
        magic_screen_position = [136,360]
    elif s.game.magic_screen.position == 3:
        magic_screen_position = [90,360]
    elif s.game.magic_screen.position == 4:
        magic_screen_position = [44,360]
    elif s.game.magic_screen.position == 5:
        magic_screen_position = [-1,360]
    elif s.game.magic_screen.position == 6:
        magic_screen_position = [-46,360]
    elif s.game.magic_screen.position == 7:
        magic_screen_position = [-96,360]
    elif s.game.magic_screen.position == 8:
        magic_screen_position = [-144,360]
    elif s.game.magic_screen.position == 9:
        magic_screen_position = [-190,360]
    elif s.game.magic_screen.position == 10:
        magic_screen_position = [-239,360]
    elif s.game.magic_screen.position == 11:
        magic_screen_position = [-285,360]
    elif s.game.magic_screen.position == 12:
        magic_screen_position = [-332,360]
    elif s.game.magic_screen.position == 13:
        magic_screen_position = [-380,360]
    elif s.game.magic_screen.position == 14:
        magic_screen_position = [-427,360]


    screen.blit(magic_screen, magic_screen_position)

    backglass_position = [0, 0]
    backglass = pygame.Surface(screen.get_size(), flags=pygame.SRCALPHA)
    backglass.fill((0, 0, 0))
    if menu == True:
        backglass = pygame.image.load('silver_sails/assets/silver_sails_menu.png').convert()
        backglass.set_colorkey((255,0,252))
    else:
        if (s.game.anti_cheat.status == True):
            backglass = pygame.image.load('silver_sails/assets/silver_sails_gi.png').convert()
            backglass.set_colorkey((255,0,252))
        else:
            backglass = pygame.image.load('silver_sails/assets/silver_sails_off.png').convert()
            backglass.set_colorkey((255,0,252))
    backglass = pygame.transform.scale(backglass, (720, 1280))
    
    screen.blit(backglass, backglass_position)

    if s.game.green_odds.position < 4:
        rc = [145,205]
        screen.blit(red_s, rc)
    else:
        rc = [145,205]
        screen.blit(s_letter, rc)

    if s.game.green_odds.position == 4:
        ri = [187,205]
        screen.blit(red_i, ri)
    else:
        ri = [187,205]
        screen.blit(i_letter, ri)

    if s.game.green_odds.position == 5:
        rr = [229,205]
        screen.blit(red_l, rr)
    else:
        rr = [229,205]
        screen.blit(l, rr)

    if s.game.green_odds.position == 6:
        rc2 = [268,205]
        screen.blit(red_v, rc2)
    else:
        rc2 = [268,205]
        screen.blit(v, rc2)

    if s.game.green_odds.position == 7:
        ru = [312,205]
        screen.blit(red_e, ru)
    else:
        ru = [312,205]
        screen.blit(e, ru)

    if s.game.green_odds.position == 8:
        rs = [355,205]
        screen.blit(red_r, rs)
    else:
        rs = [355,205]
        screen.blit(r, rs)

    if s.game.green_odds.position == 1 or s.game.green_odds.position == 2 or s.game.gold_odds == 75:
        go = [29,590]
        screen.blit(gold_odds, go)
    elif s.game.green_odds.position == 3 or s.game.green_odds.position == 4 or s.game.gold_odds == 96:
        go = [30,562]
        screen.blit(gold_odds, go)
    elif s.game.green_odds.position == 5 or s.game.gold_odds == 200:
        go = [30,533]
        screen.blit(gold_odds, go)
    elif s.game.green_odds.position == 6 or s.game.gold_odds == 300:
        go = [30,504]
        screen.blit(gold_odds, go)
    elif s.game.green_odds.position == 7 or s.game.gold_odds == 450:
        go = [30,474]
        screen.blit(gold_odds, go)
    elif s.game.green_odds.position == 8 or s.game.gold_odds == 600:
        go = [30,446]
        screen.blit(gold_odds, go)

    if s.game.eb_play.status == True:
        eb_position = [38,1032]
        screen.blit(extra_balls, eb_position)

    if s.game.extra_ball.position >= 1:
        eb_position = [150,1032]
        screen.blit(eb_number, eb_position)
    if s.game.extra_ball.position >= 2:
        eb_position = [200,1032]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 3:
        eb_position = [268,1032]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 4:
        eb_position = [332,1032]
        screen.blit(eb_number, eb_position)
    if s.game.extra_ball.position >= 5:
        eb_position = [378,1032]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 6:
        eb_position = [446,1032]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 7:
        eb_position = [509,1032]
        screen.blit(eb_number, eb_position)
    if s.game.extra_ball.position >= 8:
        eb_position = [557,1032]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 9:
        eb_position = [623,1031]
        screen.blit(eb, eb_position)


    if s.game.selection_feature.position == 1:
        i = [672,585]
        screen.blit(ti, i)
    if s.game.selection_feature.position == 2 or s.game.selection_feature.position == 3:
        i = [672,525]
        screen.blit(ti, i)
    if s.game.selection_feature.position == 4 or s.game.selection_feature.position == 5 or s.game.selection_feature.position == 6:
        i = [672,473]
        screen.blit(ti, i)
    if s.game.selection_feature.position == 7:
        i = [672,420]
        screen.blit(ti, i)
    if s.game.selection_feature.position == 8:
        i = [672,359]
        screen.blit(ti, i)

    if s.game.red_star.status == True:
        rs_position = [550,458]
        screen.blit(time, rs_position)
    if s.game.yellow_star.status == True:
        rs_position = [550,515]
        screen.blit(time, rs_position)

    if s.game.magic_screen_feature.position >= 7 or s.game.ok.status == True or s.game.golden.status == True:
        if s.game.selection_feature.position < 7:
            bfp = [551,573]
            screen.blit(time, bfp)
        elif s.game.selection_feature.position == 7:
            bfp = [551,402]
            screen.blit(time, bfp)
        elif s.game.selection_feature.position == 8:
            bfp = [551,346]
            screen.blit(time, bfp)

    if s.game.magic_screen_feature.position >= 9:
        if s.game.three_blue.status == True:
            bp = [23,379]
            screen.blit(blue_section, bp)
        elif s.game.three_blue_six.status == True:
            bp = [23,349]
            screen.blit(blue_section, bp)
        elif s.game.two_blue.status == True:
            bp = [23,320]
            screen.blit(blue_section, bp)


    if s.game.ball_count.position < 1:
        if s.game.odds_only.status == True:
            b = [21,876]
            screen.blit(button, b)
        elif s.game.features.status == True:
            b = [21,926]
            screen.blit(button, b)
        else:
            b = [21,976]
            screen.blit(button, b)


    if s.game.red_super_section.status == True:
        rss = [585,203]
        screen.blit(super_section, rss)
    if s.game.yellow_super_section.status == True:
        yss = [25,203]
        screen.blit(super_section, yss)

    if s.game.magic_screen_feature.position >= 4:
        ms = [250,669]
        screen.blit(ms_letter, ms)
    if s.game.magic_screen_feature.position >= 5:
        ms = [292,670]
        screen.blit(ms_letter, ms)
    if s.game.magic_screen_feature.position >= 6:
        ms = [330,670]
        screen.blit(ms_letter, ms)
    if s.game.magic_screen_feature.position >= 7:
        ms = [370,670]
        screen.blit(ms_letter, ms)
    if s.game.magic_screen_feature.position >= 8:
        ms = [409,670]
        screen.blit(ms_letter, ms)
    if s.game.magic_screen_feature.position >= 9:
        ms = [451,670]
        screen.blit(ms_letter, ms)
    if s.game.magic_screen_feature.position >= 10:
        ms = [491,670]
        screen.blit(ms_letter, ms)

    if s.game.ok.status == True:
        ms = [114,668]
        screen.blit(ok_gate, ms)

    if s.game.gate.status == True:
        ms = [27,668]
        screen.blit(ok_gate, ms)
    else:
        if s.game.two_gold.status == True:
            ma = [104,589]
            screen.blit(gold_arrow, ma)

    if s.game.golden.status == True:
        ms = [33,413]
        screen.blit(golden_game, ms)
        if s.game.two_gold.status == False:
            ms = [70,438]
            screen.blit(gold_section, ms)
        else:
            ms = [70,515]
            screen.blit(gold_section, ms)
            ma = [104,589]
            screen.blit(gold_arrow, ma)

    if s.game.magic_screen.position == 8:
        ms = [253,724]
        screen.blit(ms_indicator, ms)
    if s.game.magic_screen.position == 9:
        ms = [294,724]
        screen.blit(ms_indicator, ms)
    if s.game.magic_screen.position == 10:
        ms = [334,724]
        screen.blit(ms_indicator, ms)
    if s.game.magic_screen.position == 11:
        ms = [375,724]
        screen.blit(ms_indicator, ms)
    if s.game.magic_screen.position == 12:
        ms = [415,724]
        screen.blit(ms_indicator, ms)
    if s.game.magic_screen.position == 13:
        ms = [457,724]
        screen.blit(ms_indicator, ms)
    if s.game.magic_screen.position == 14:
        ms = [497,724]
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
                number_position = [427,567]
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
        o = [187,784]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 2:
        o = [250,784]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 3:
        o = [310,784]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 4:
        o = [371,784]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 5:
        o = [428,784]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 6:
        o = [476,784]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 7:
        o = [525,784]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 8:
        o = [573,784]
        screen.blit(odds, o)

    if s.game.yellow_odds.position == 1:
        o = [187,850]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 2:
        o = [250,850]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 3:
        o = [310,850]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 4:
        o = [371,850]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 5:
        o = [428,850]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 6:
        o = [476,850]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 7:
        o = [525,850]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 8:
        o = [573,850]
        screen.blit(odds, o)

    if s.game.green_odds.position == 1:
        o = [187,920]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 2:
        o = [250,920]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 3:
        o = [310,920]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 4:
        o = [371,920]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 5:
        o = [428,920]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 6:
        o = [476,920]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 7:
        o = [525,920]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 8:
        o = [573,920]
        screen.blit(odds, o)


    if s.game.tilt.status == True:
        tilt_position = [572,710]
        screen.blit(tilt, tilt_position)

    pygame.display.update()

def eb_animation(num):
    global screen

    if num == 3:
        eb_position = [150,1032]
        screen.blit(eb_number, eb_position)
        pygame.display.update()
    if num == 2:
        eb_position = [200,1032]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 1:
        eb_position = [268,1032]
        screen.blit(eb, eb_position)
        pygame.display.update()


def feature_animation(num):
    global screen
    if num == 4:
        rss = [581,201]
        screen.blit(super_section, rss)
        pygame.display.update()
    else:
        yss = [18,205]
        screen.blit(super_section, yss)
        pygame.display.update()


def odds_animation(num):
    global screen

    if num == 8:
        odds_position = [187,778]
        screen.blit(odds, odds_position)
    if num == 7:
        odds_position = [247,842]
        screen.blit(odds, odds_position)
    if num == 6:
        odds_position = [309,912]
        screen.blit(odds, odds_position)
    if num == 5:
        odds_position = [370,778]
        screen.blit(odds, odds_position)
    if num == 4:
        odds_position = [423,842]
        screen.blit(odds, odds_position)
    if num == 3:
        odds_position = [472,912]
        screen.blit(odds, odds_position)
    if num == 2:
        odds_position = [522,778]
        screen.blit(odds, odds_position)
    if num == 1:
        odds_position = [568,842]
        screen.blit(odd, odds_position)
    pygame.display.update()


