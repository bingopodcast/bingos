
import pygame
import random

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

meter = pygame.image.load('graphics/assets/register_cover.png').convert()
magic_screen = pygame.image.load('golden_gate/assets/magic_screen.png').convert()
number_card = pygame.image.load('golden_gate/assets/number_card.png').convert()
odds = pygame.image.load('golden_gate/assets/odds.png').convert_alpha()
eb = pygame.image.load('golden_gate/assets/eb.png').convert_alpha()
eb_number = pygame.image.load('golden_gate/assets/eb_number.png').convert_alpha()
extra_balls = pygame.image.load('golden_gate/assets/extra_balls.png').convert_alpha()
time = pygame.image.load('golden_gate/assets/time.png').convert_alpha()
ms_indicator = pygame.image.load('golden_gate/assets/ms_indicator.png').convert_alpha()
ti = pygame.image.load('golden_gate/assets/time_indicator.png').convert_alpha()
super_section = pygame.image.load('golden_gate/assets/super_section.png').convert_alpha()
ms_letter = pygame.image.load('golden_gate/assets/ms_letter.png').convert_alpha()
number = pygame.image.load('golden_gate/assets/number.png').convert_alpha()
select_now = pygame.image.load('golden_gate/assets/select_now.png').convert_alpha()
blue_section = pygame.image.load('golden_gate/assets/blue_section.png').convert_alpha()
gold_section = pygame.image.load('golden_gate/assets/gold_section.png').convert_alpha()
gold_arrow = pygame.image.load('golden_gate/assets/gold_arrow.png').convert_alpha()
gold_odds = pygame.image.load('golden_gate/assets/gold_odds.png').convert_alpha()
golden_game = pygame.image.load('golden_gate/assets/golden_game.png').convert_alpha()
tilt = pygame.image.load('golden_gate/assets/tilt.png').convert_alpha()
button = pygame.image.load('golden_gate/assets/button.png').convert_alpha()
ok_gate = pygame.image.load('golden_gate/assets/ok_gate.png').convert_alpha()
red_g = pygame.image.load('golden_gate/assets/red_g.png').convert_alpha()
g = pygame.image.load('golden_gate/assets/g.png').convert_alpha()
red_o = pygame.image.load('golden_gate/assets/red_o.png').convert_alpha()
o_letter = pygame.image.load('golden_gate/assets/o_letter.png').convert_alpha()
red_l = pygame.image.load('golden_gate/assets/red_l.png').convert_alpha()
l = pygame.image.load('golden_gate/assets/l.png').convert_alpha()
red_d = pygame.image.load('golden_gate/assets/red_d.png').convert_alpha()
d = pygame.image.load('golden_gate/assets/d.png').convert_alpha()
red_e = pygame.image.load('golden_gate/assets/red_e.png').convert_alpha()
e = pygame.image.load('golden_gate/assets/e.png').convert_alpha()
red_n = pygame.image.load('golden_gate/assets/red_n.png').convert_alpha()
n = pygame.image.load('golden_gate/assets/n.png').convert_alpha()
bg_menu = pygame.image.load('golden_gate/assets/golden_gate_menu.png').convert()
bg_menu.set_colorkey((255,0,252))
bg_gi = pygame.image.load('golden_gate/assets/golden_gate_gi.png').convert()
bg_gi.set_colorkey((255,0,252))
bg_off = pygame.image.load('golden_gate/assets/golden_gate_off.png').convert()
bg_off.set_colorkey((255,0,252))

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
        magic_screen_position = [-377,360]
    elif s.game.magic_screen.position == 14:
        magic_screen_position = [-424,360]


    screen.blit(magic_screen, magic_screen_position)

    backglass_position = [0, 0]
    backglass = pygame.Surface(screen.get_size(), flags=pygame.SRCALPHA)
    backglass.fill((0, 0, 0))
    if menu == True:
        screen.blit(bg_menu, backglass_position)
    else:
        if (s.game.anti_cheat.status == True):
            screen.blit(bg_gi, backglass_position)
        else:
            screen.blit(bg_off, backglass_position)

    if s.game.green_odds.position < 4:
        rc = [137,210]
        screen.blit(red_g, rc)
    else:
        rc = [137,210]
        screen.blit(g, rc)

    if s.game.green_odds.position == 4:
        ri = [179,210]
        screen.blit(red_o, ri)
    else:
        ri = [179,210]
        screen.blit(o_letter, ri)

    if s.game.green_odds.position == 5:
        rr = [221,210]
        screen.blit(red_l, rr)
    else:
        rr = [221,210]
        screen.blit(l, rr)

    if s.game.green_odds.position == 6:
        rc2 = [260,210]
        screen.blit(red_d, rc2)
    else:
        rc2 = [260,210]
        screen.blit(d, rc2)

    if s.game.green_odds.position == 7:
        ru = [304,210]
        screen.blit(red_e, ru)
    else:
        ru = [304,210]
        screen.blit(e, ru)

    if s.game.green_odds.position == 8:
        rs = [347,210]
        screen.blit(red_n, rs)
    else:
        rs = [347,210]
        screen.blit(n, rs)

    if s.game.green_odds.position == 1 or s.game.green_odds.position == 2 or s.game.gold_odds == 75:
        go = [27,593]
        screen.blit(gold_odds, go)
    elif s.game.green_odds.position == 3 or s.game.green_odds.position == 4 or s.game.gold_odds == 96:
        go = [27,565]
        screen.blit(gold_odds, go)
    elif s.game.green_odds.position == 5 or s.game.gold_odds == 200:
        go = [27,536]
        screen.blit(gold_odds, go)
    elif s.game.green_odds.position == 6 or s.game.gold_odds == 300:
        go = [27,507]
        screen.blit(gold_odds, go)
    elif s.game.green_odds.position == 7 or s.game.gold_odds == 450:
        go = [27,477]
        screen.blit(gold_odds, go)
    elif s.game.green_odds.position == 8 or s.game.gold_odds == 600:
        go = [27,449]
        screen.blit(gold_odds, go)

    if s.game.eb_play.status == True:
        eb_position = [34,1027]
        screen.blit(extra_balls, eb_position)

    if s.game.extra_ball.position >= 1:
        eb_position = [142,1029]
        screen.blit(eb_number, eb_position)
    if s.game.extra_ball.position >= 2:
        eb_position = [192,1029]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 3:
        eb_position = [260,1029]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 4:
        eb_position = [324,1029]
        screen.blit(eb_number, eb_position)
    if s.game.extra_ball.position >= 5:
        eb_position = [370,1029]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 6:
        eb_position = [437,1029]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 7:
        eb_position = [501,1029]
        screen.blit(eb_number, eb_position)
    if s.game.extra_ball.position >= 8:
        eb_position = [549,1029]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 9:
        eb_position = [615,1029]
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
        rs_position = [542,458]
        screen.blit(time, rs_position)
    if s.game.yellow_star.status == True:
        rs_position = [542,515]
        screen.blit(time, rs_position)

    if s.game.magic_screen_feature.position >= 7 or s.game.ok.status == True or s.game.golden.status == True:
        if s.game.selection_feature.position < 7:
            bfp = [540,570]
            screen.blit(time, bfp)
            if s.game.ball_count.position == 3:
                s.cancel_delayed(name="blink")
                blink([s,1,1])
            else:
                s.cancel_delayed(name="blink")
        elif s.game.selection_feature.position == 7:
            bfp = [542,403]
            screen.blit(time, bfp)
            if s.game.ball_count.position == 4:
                s.cancel_delayed(name="blink")
                blink([s,1,1])
            else:
                s.cancel_delayed(name="blink")
        elif s.game.selection_feature.position == 8:
            bfp = [543,347]
            screen.blit(time, bfp)
            if s.game.ball_count.position == 5:
                s.cancel_delayed(name="blink")
                blink([s,1,1])
            else:
                s.cancel_delayed(name="blink")

    if s.game.magic_screen_feature.position >= 9:
        if s.game.three_blue.status == True:
            bp = [19,382]
            screen.blit(blue_section, bp)
        elif s.game.three_blue_six.status == True:
            bp = [19,352]
            screen.blit(blue_section, bp)
        elif s.game.two_blue.status == True:
            bp = [19,324]
            screen.blit(blue_section, bp)


    if s.game.ball_count.position < 1:
        if s.game.odds_only.status == True:
            b = [18,872]
            screen.blit(button, b)
        elif s.game.features.status == True:
            b = [18,922]
            screen.blit(button, b)
        else:
            if s.game.all_advantages.status == True:
                b = [18,972]
                screen.blit(button, b)


    if s.game.red_super_section.status == True:
        rss = [581,201]
        screen.blit(super_section, rss)
    if s.game.yellow_super_section.status == True:
        yss = [18,205]
        screen.blit(super_section, yss)

    if s.game.magic_screen_feature.position >= 4:
        ms = [247,667]
        screen.blit(ms_letter, ms)
    if s.game.magic_screen_feature.position >= 5:
        ms = [287,667]
        screen.blit(ms_letter, ms)
    if s.game.magic_screen_feature.position >= 6:
        ms = [325,667]
        screen.blit(ms_letter, ms)
    if s.game.magic_screen_feature.position >= 7:
        ms = [366,667]
        screen.blit(ms_letter, ms)
    if s.game.magic_screen_feature.position >= 8:
        ms = [404,667]
        screen.blit(ms_letter, ms)
    if s.game.magic_screen_feature.position >= 9:
        ms = [443,667]
        screen.blit(ms_letter, ms)
    if s.game.magic_screen_feature.position >= 10:
        ms = [482,667]
        screen.blit(ms_letter, ms)

    if s.game.ok.status == True:
        ms = [112,667]
        screen.blit(ok_gate, ms)

    if s.game.gate.status == True:
        ms = [25,667]
        screen.blit(ok_gate, ms)
    else:
        if s.game.two_gold.status == True:
            ma = [104,591]
            screen.blit(gold_arrow, ma)

    if s.game.golden.status == True:
        ms = [30,417]
        screen.blit(golden_game, ms)
        if s.game.two_gold.status == False:
            ms = [67,444]
            screen.blit(gold_section, ms)
        else:
            ms = [70,518]
            screen.blit(gold_section, ms)
            ma = [104,591]
            screen.blit(gold_arrow, ma)

    if s.game.magic_screen.position == 8:
        ms = [249,724]
        screen.blit(ms_indicator, ms)
    if s.game.magic_screen.position == 9:
        ms = [289,724]
        screen.blit(ms_indicator, ms)
    if s.game.magic_screen.position == 10:
        ms = [327,724]
        screen.blit(ms_indicator, ms)
    if s.game.magic_screen.position == 11:
        ms = [368,724]
        screen.blit(ms_indicator, ms)
    if s.game.magic_screen.position == 12:
        ms = [406,724]
        screen.blit(ms_indicator, ms)
    if s.game.magic_screen.position == 13:
        ms = [445,724]
        screen.blit(ms_indicator, ms)
    if s.game.magic_screen.position == 14:
        ms = [484,724]
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
        o = [187,778]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 2:
        o = [247,778]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 3:
        o = [307,778]
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
        o = [515,778]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 8:
        o = [563,778]
        screen.blit(odds, o)

    if s.game.yellow_odds.position == 1:
        o = [187,842]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 2:
        o = [247,842]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 3:
        o = [307,842]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 4:
        o = [364,842]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 5:
        o = [418,842]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 6:
        o = [468,842]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 7:
        o = [515,842]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 8:
        o = [563,842]
        screen.blit(odds, o)

    if s.game.green_odds.position == 1:
        o = [187,912]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 2:
        o = [247,912]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 3:
        o = [307,912]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 4:
        o = [364,912]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 5:
        o = [418,912]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 6:
        o = [468,912]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 7:
        o = [515,912]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 8:
        o = [563,912]
        screen.blit(odds, o)


    if s.game.tilt.status == True:
        tilt_position = [572,710]
        screen.blit(tilt, tilt_position)

    pygame.display.update()

def blink(args):
    dirty_rects = []
    s = args[0]
    b = args[1]
    sn = args[2]

    if b == 0:
        if sn == 1:
            p = [565,673]
            dirty_rects.append(screen.blit(select_now, p))
        pygame.display.update(dirty_rects)
    else:
        dirty_rects.append(screen.blit(bg_gi, (565,673), pygame.Rect(565,673,121,41)))
        pygame.display.update(dirty_rects)
    b = not b

    args = [s,b,sn]

    s.delay(name="blink", delay=0.1, handler=blink, param=args)

def eb_animation(num):
    global screen

    if num == 3:
        eb_position = [145,1026]
        screen.blit(eb_number, eb_position)
        pygame.display.update()
    if num == 2:
        eb_position = [195,1025]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 1:
        eb_position = [257,1025]
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


