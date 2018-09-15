
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
bg_gi = pygame.image.load('golden_gate/assets/golden_gate_gi.png').convert_alpha()
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

def screen_animation(args):
    dirty_rects = []
    s = args[0]
    num = args[1]
    direction = args[2]
    
    number_card_position = [235,363]

    dirty_rects.append(screen.blit(number_card, number_card_position))

    magic_screen.set_colorkey((255,0,252))

    if s.game.magic_screen.position == 0:
        p = [228,360]
    elif s.game.magic_screen.position == 1:
        p = [181,360]
    elif s.game.magic_screen.position == 2:
        p = [136,360]
    elif s.game.magic_screen.position == 3:
        p = [90,360]
    elif s.game.magic_screen.position == 4:
        p = [44,360]
    elif s.game.magic_screen.position == 5:
        p = [-1,360]
    elif s.game.magic_screen.position == 6:
        p = [-46,360]
    elif s.game.magic_screen.position == 7:
        p = [-96,360]
    elif s.game.magic_screen.position == 8:
        p = [-144,360]
    elif s.game.magic_screen.position == 9:
        p = [-190,360]
    elif s.game.magic_screen.position == 10:
        p = [-239,360]
    elif s.game.magic_screen.position == 11:
        p = [-285,360]
    elif s.game.magic_screen.position == 12:
        p = [-332,360]
    elif s.game.magic_screen.position == 13:
        p = [-377,360]
    elif s.game.magic_screen.position == 14:
        p = [-424,360]

    if direction == "left":
       p[0] = p[0] + num
    else:
       p[0] = p[0] - num
 
    dirty_rects.append(screen.blit(magic_screen, p))
    
    backglass_position = [0, 0]
    if (s.game.anti_cheat.status == True):
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],900,270)))
    else:
        dirty_rects.append(screen.blit(bg_off, p, pygame.Rect(p[0],p[1],900,270)))
    
    if s.game.golden.status == True:
        bp = [30,417]
        dirty_rects.append(screen.blit(bg_gi, bp, pygame.Rect(bp[0],bp[1],152,28)))
        dirty_rects.append(screen.blit(golden_game, bp))
        if s.game.two_gold.status == False:
            bp = [67,444]
            dirty_rects.append(screen.blit(bg_gi, bp, pygame.Rect(bp[0],bp[1],124,79)))
            dirty_rects.append(screen.blit(gold_section, bp))
        else:
            bp = [70,518]
            dirty_rects.append(screen.blit(bg_gi, bp, pygame.Rect(bp[0],bp[1],124,79)))
            dirty_rects.append(screen.blit(gold_section, bp))
            bp = [104,591]
            dirty_rects.append(screen.blit(bg_gi, bp, pygame.Rect(bp[0],bp[1],46,33)))
            dirty_rects.append(screen.blit(gold_arrow, bp))
    if s.game.green_odds.position == 1 or s.game.green_odds.position == 2 or s.game.gold_odds == 75:
        bp = [27,593]
        dirty_rects.append(screen.blit(bg_gi, bp, pygame.Rect(bp[0],bp[1],43,30)))
        dirty_rects.append(screen.blit(gold_odds, bp))
    elif s.game.green_odds.position == 3 or s.game.green_odds.position == 4 or s.game.gold_odds == 96:
        bp = [27,565]
        dirty_rects.append(screen.blit(bg_gi, bp, pygame.Rect(bp[0],bp[1],43,30)))
        dirty_rects.append(screen.blit(gold_odds, bp))
    elif s.game.green_odds.position == 5 or s.game.gold_odds == 200:
        bp = [27,536]
        dirty_rects.append(screen.blit(bg_gi, bp, pygame.Rect(bp[0],bp[1],43,30)))
        dirty_rects.append(screen.blit(gold_odds, bp))
    elif s.game.green_odds.position == 6 or s.game.gold_odds == 300:
        bp = [27,507]
        dirty_rects.append(screen.blit(bg_gi, bp, pygame.Rect(bp[0],bp[1],43,30)))
        dirty_rects.append(screen.blit(gold_odds, bp))
    elif s.game.green_odds.position == 7 or s.game.gold_odds == 450:
        bp = [27,477]
        dirty_rects.append(screen.blit(bg_gi, bp, pygame.Rect(bp[0],bp[1],43,30)))
        dirty_rects.append(screen.blit(gold_odds, bp))
    elif s.game.green_odds.position == 8 or s.game.gold_odds == 600:
        bp = [27,449]
        dirty_rects.append(screen.blit(bg_gi, bp, pygame.Rect(bp[0],bp[1],43,30)))
        dirty_rects.append(screen.blit(gold_odds, bp))



    if s.game.magic_screen_feature.position >= 9:
        if s.game.three_blue.status == True:
            bp = [19,382]
            dirty_rects.append(screen.blit(bg_gi, bp, pygame.Rect(bp[0],bp[1],173,35)))
            dirty_rects.append(screen.blit(blue_section, bp))
        elif s.game.three_blue_six.status == True:
            bp = [19,352]
            dirty_rects.append(screen.blit(bg_gi, bp, pygame.Rect(bp[0],bp[1],173,35)))
            dirty_rects.append(screen.blit(blue_section, bp))
        elif s.game.two_blue.status == True:
            bp = [19,324]
            dirty_rects.append(screen.blit(bg_gi, bp, pygame.Rect(bp[0],bp[1],173,35)))
            dirty_rects.append(screen.blit(blue_section, bp))

    if s.game.magic_screen_feature.position >= 7 or s.game.ok.status == True or s.game.golden.status == True:
        if s.game.selection_feature.position < 7:
            bfp = [540,570]
            dirty_rects.append(screen.blit(bg_gi, bfp, pygame.Rect(bfp[0],bfp[1],120,56)))
            dirty_rects.append(screen.blit(time, bfp))
        elif s.game.selection_feature.position == 7:
            bfp = [542,403]
            dirty_rects.append(screen.blit(bg_gi, bfp, pygame.Rect(bfp[0],bfp[1],120,56)))
            screen.blit(time, bfp)
        elif s.game.selection_feature.position == 8:
            bfp = [543,347]
            dirty_rects.append(screen.blit(bg_gi, bfp, pygame.Rect(bfp[0],bfp[1],120,56)))
            screen.blit(time, bfp)
        
    if s.game.selection_feature.position == 1:
        i = [672,585]
        dirty_rects.append(screen.blit(bg_gi, i, pygame.Rect(i[0],i[1],39,29)))
        dirty_rects.append(screen.blit(ti, i))
    if s.game.selection_feature.position == 2 or s.game.selection_feature.position == 3:
        i = [672,525]
        dirty_rects.append(screen.blit(bg_gi, i, pygame.Rect(i[0],i[1],39,29)))
        dirty_rects.append(screen.blit(ti, i))
    if s.game.selection_feature.position == 4 or s.game.selection_feature.position == 5 or s.game.selection_feature.position == 6:
        i = [672,473]
        dirty_rects.append(screen.blit(bg_gi, i, pygame.Rect(i[0],i[1],39,29)))
        dirty_rects.append(screen.blit(ti, i))
    if s.game.selection_feature.position == 7:
        i = [672,420]
        dirty_rects.append(screen.blit(bg_gi, i, pygame.Rect(i[0],i[1],39,29)))
        dirty_rects.append(screen.blit(ti, i))
    if s.game.selection_feature.position == 8:
        i = [672,359]
        dirty_rects.append(screen.blit(bg_gi, i, pygame.Rect(i[0],i[1],39,29)))
        dirty_rects.append(screen.blit(ti, i))

    if s.game.red_star.status == True:
        rs_position = [542,458]
        dirty_rects.append(screen.blit(bg_gi, rs_position, pygame.Rect(rs_position[0],rs_position[1],120,56)))
        dirty_rects.append(screen.blit(time, rs_position))
    if s.game.yellow_star.status == True:
        rs_position = [542,515]
        dirty_rects.append(screen.blit(bg_gi, rs_position, pygame.Rect(rs_position[0],rs_position[1],120,56)))
        dirty_rects.append(screen.blit(time, rs_position))

    if s.game.red_super_section.status == True:
        rss = [581,201]
        dirty_rects.append(screen.blit(bg_gi, rss, pygame.Rect(rss[0],rss[1],120,86)))
        dirty_rects.append(screen.blit(super_section, rss))
    if s.game.yellow_super_section.status == True:
        yss = [18,205]
        dirty_rects.append(screen.blit(bg_gi, yss, pygame.Rect(yss[0],yss[1],120,86)))
        dirty_rects.append(screen.blit(super_section, yss))

    pygame.display.update(dirty_rects)


def eb_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]

    if s.game.extra_ball.position < 1:
        dirty_rects.append(screen.blit(bg_gi, (142,1029), pygame.Rect(142,1029,52,38)))
    if s.game.extra_ball.position < 2:
        dirty_rects.append(screen.blit(bg_gi, (192,1029), pygame.Rect(192,1029,60,38)))
    if s.game.extra_ball.position < 3:
        dirty_rects.append(screen.blit(bg_gi, (260,1029), pygame.Rect(260,1029,60,38)))
    if s.game.extra_ball.position < 4:
        dirty_rects.append(screen.blit(bg_gi, (324,1029), pygame.Rect(324,1029,52,38)))
    if s.game.extra_ball.position < 5:
        dirty_rects.append(screen.blit(bg_gi, (370,1029), pygame.Rect(370,1029,60,38)))
    if s.game.extra_ball.position < 6:
        dirty_rects.append(screen.blit(bg_gi, (437,1029), pygame.Rect(437,1029,60,38)))
    if s.game.extra_ball.position < 7:
        dirty_rects.append(screen.blit(bg_gi, (501,1029), pygame.Rect(501,1029,52,38)))
    if s.game.extra_ball.position < 8:
        dirty_rects.append(screen.blit(bg_gi, (549,1029), pygame.Rect(549,1029,60,38)))
    if s.game.extra_ball.position < 9:
        dirty_rects.append(screen.blit(bg_gi, (615,1029), pygame.Rect(615,1029,60,38)))
    pygame.display.update(dirty_rects)

    if num in [0,25,14,49]:
        if s.game.extra_ball.position < 1:
            p = [142,1029]
            dirty_rects.append(screen.blit(eb_number, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [39,1,26,15]:
        if s.game.extra_ball.position < 2:
            p = [192,1029]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [3,4,17,28,29,40]:
        if s.game.extra_ball.position < 3:
            p = [260,1029]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [5,18,30,43]:
        if s.game.extra_ball.position < 4:
            p = [324,1029]
            dirty_rects.append(screen.blit(eb_number, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [7,8,19,32,33,44]:
        if s.game.extra_ball.position < 5:
            p = [370,1029]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [9,10,20,34,35,45]:
        if s.game.extra_ball.position < 6:
            p = [437,1029]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [11,21,36,46]:
        if s.game.extra_ball.position < 7:
            p = [501,1029]
            dirty_rects.append(screen.blit(eb_number, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [12,22,37,47]:
        if s.game.extra_ball.position < 8:
            p = [549,1029]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [2,6,13,16,23,27,31,38,41,48]:
        if s.game.extra_ball.position < 9:
            p = [615,1029]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return

def clear_odds(s, num):
    global screen

    dirty_rects = []

    if s.game.yellow_odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (187,842), pygame.Rect(187,842,48,76)))
    if s.game.yellow_odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (247,842), pygame.Rect(247,842,48,76)))
    if s.game.yellow_odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (307,842), pygame.Rect(307,842,48,76)))
    if s.game.yellow_odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (364,842), pygame.Rect(364,842,48,76)))
    if s.game.yellow_odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (418,842), pygame.Rect(418,842,48,76)))
    if s.game.yellow_odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (468,842), pygame.Rect(468,842,48,76)))
    if s.game.yellow_odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (515,842), pygame.Rect(515,842,48,76)))
    if s.game.yellow_odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (563,842), pygame.Rect(563,842,48,76)))

    if s.game.red_odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (187,778), pygame.Rect(187,778,48,76)))
    if s.game.red_odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (247,778), pygame.Rect(247,778,48,76)))
    if s.game.red_odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (307,778), pygame.Rect(307,778,48,76)))
    if s.game.red_odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (364,778), pygame.Rect(364,778,48,76)))
    if s.game.red_odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (418,778), pygame.Rect(418,778,48,76)))
    if s.game.red_odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (468,778), pygame.Rect(468,778,48,76)))
    if s.game.red_odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (515,778), pygame.Rect(515,778,48,76)))
    if s.game.red_odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (563,778), pygame.Rect(563,778,48,76)))

    if s.game.green_odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (187,912), pygame.Rect(187,912,48,76)))
    if s.game.green_odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (247,912), pygame.Rect(247,912,48,76)))
    if s.game.green_odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (307,912), pygame.Rect(307,912,48,76)))
    if s.game.green_odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (364,912), pygame.Rect(364,912,48,76)))
    if s.game.green_odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (418,912), pygame.Rect(418,912,48,76)))
    if s.game.green_odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (468,912), pygame.Rect(468,912,48,76)))
    if s.game.green_odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (515,912), pygame.Rect(515,912,48,76)))
    if s.game.green_odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (563,912), pygame.Rect(563,912,48,76)))

    pygame.display.update(dirty_rects)

def draw_odds_animation(s, num):
    global screen
    dirty_rects = []

    if num in [11,36]:
        if s.game.yellow_odds.position != 1:
            p = [187,842]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [4,29]:
        if s.game.yellow_odds.position != 2:
            p = [247,842]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [7,32]:
        if s.game.yellow_odds.position != 3:
            p = [307,842]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [13,38]:
        if s.game.yellow_odds.position != 4:
            p = [364,842]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [22,47]:
        if s.game.yellow_odds.position != 5:
            p = [418,842]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [17,42]:
        if s.game.yellow_odds.position != 6:
            p = [468,842]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [19,44]:
        if s.game.yellow_odds.position != 7:
            p = [515,842]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [5,30]:
        if s.game.yellow_odds.position != 8:
            p = [563,842]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return

    if num in [0,25]:
        if s.game.red_odds.position != 1:
            p = [187,778]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [15,40]:
        if s.game.red_odds.position != 2:
            p = [247,778]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [24,49]:
        if s.game.red_odds.position != 3:
            p = [307,778]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [9,34]:
        if s.game.red_odds.position != 4:
            p = [364,778]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [20,45]:
        if s.game.red_odds.position != 5:
            p = [418,778]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [12,37]:
        if s.game.red_odds.position != 6:
            p = [468,778]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [50,26]:
        if s.game.red_odds.position != 7:
            p = [515,778]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [6,31]:
        if s.game.red_odds.position != 8:
            p = [563,778]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return

    if num in [16,41]:
        if s.game.green_odds.position != 1:
            p = [187,912]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [18,43]:
        if s.game.green_odds.position != 2:
            p = [247,912]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [14,39]:
        if s.game.green_odds.position != 3:
            p = [307,912]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [3,28]:
        if s.game.green_odds.position != 4:
            p = [364,912]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [23,48]:
        if s.game.green_odds.position != 5:
            p = [418,912]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [8,33]:
        if s.game.green_odds.position != 6:
            p = [468,912]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [22,47]:
        if s.game.green_odds.position != 7:
            p = [515,912]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [10,35]:
        if s.game.green_odds.position != 8:
            p = [563,912]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return

def odds_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]

    clear_odds(s, num)

    draw_odds_animation(s, num)

def clear_features(s, num):
    global screen

    dirty_rects = []

    if s.game.selection_feature.position < 7 and (s.game.magic_screen_feature.position <= 4 and s.game.ok.status == False):
        dirty_rects.append(screen.blit(bg_gi, (540,570), pygame.Rect(540,570,120,56)))
    if s.game.red_star.status == False:
        dirty_rects.append(screen.blit(bg_gi, (542,458), pygame.Rect(542,458,120,56)))
    if s.game.yellow_star.status == False:
        dirty_rects.append(screen.blit(bg_gi, (542,515), pygame.Rect(542,515,120,56)))
    if s.game.selection_feature.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (542,403), pygame.Rect(542,403,120,56)))
    if s.game.selection_feature.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (543,347), pygame.Rect(543,347,120,56)))

    if s.game.yellow_super_section.status == False:
        dirty_rects.append(screen.blit(bg_gi, (18,205), pygame.Rect(18,205,120,86)))
    if s.game.red_super_section.status == False:
        dirty_rects.append(screen.blit(bg_gi, (581,201), pygame.Rect(581,201,120,86)))
    if s.game.gate.status == False:
        dirty_rects.append(screen.blit(bg_gi, (25,667), pygame.Rect(25,667,86,52)))
    if s.game.ok.status == False:
        dirty_rects.append(screen.blit(bg_gi, (112,667), pygame.Rect(112,667,86,52)))
    if s.game.magic_screen_feature.position < 7:
        dirty_rects.append(screen.blit(bg_gi, (247,667), pygame.Rect(247,667,41,51)))
        dirty_rects.append(screen.blit(bg_gi, (287,667), pygame.Rect(287,667,41,51)))
        dirty_rects.append(screen.blit(bg_gi, (325,667), pygame.Rect(325,667,41,51)))
        dirty_rects.append(screen.blit(bg_gi, (366,667), pygame.Rect(366,667,41,51)))
    if s.game.magic_screen_feature.position < 8:
        dirty_rects.append(screen.blit(bg_gi, (404,667), pygame.Rect(404,667,41,51)))
    if s.game.magic_screen_feature.position < 9:
        dirty_rects.append(screen.blit(bg_gi, (443,667), pygame.Rect(443,667,41,51)))
    if s.game.magic_screen_feature.position < 10:
        dirty_rects.append(screen.blit(bg_gi, (482,667), pygame.Rect(482,667,41,51)))
    if s.game.three_blue.status == False:
       dirty_rects.append(screen.blit(bg_gi, (19,382), pygame.Rect(19,382,173,35)))
    if s.game.three_blue_six.status == False:
       dirty_rects.append(screen.blit(bg_gi, (19,352), pygame.Rect(19,352,173,35)))
    if s.game.two_blue.status == False:
        dirty_rects.append(screen.blit(bg_gi, (19,324), pygame.Rect(19,324,173,35)))

    pygame.display.update(dirty_rects)


def draw_feature_animation(s, num):
    global screen
    dirty_rects = []
 
    if num in [10,35]:
        if (s.game.magic_screen_feature.position <= 4 and s.game.ok.status == False) and s.game.selection_feature.position not in [7,8]:
            p = [540,570]
            dirty_rects.append(screen.blit(time, p))
            pygame.display.update(dirty_rects)
            return
    if num in [9,34]:
        if s.game.selection_feature.position != 7:
            p = [542,403]
            dirty_rects.append(screen.blit(time, p))
            pygame.display.update(dirty_rects)
            return
    if num in [6,17,21,31,42,46]:
        if s.game.selection_feature.position != 8:
            p = [543,347]
            dirty_rects.append(screen.blit(time, p))
            pygame.display.update(dirty_rects)
            return
    if num in [4,29]:
        if s.game.red_star.status == False:
            p = [542,458]
            dirty_rects.append(screen.blit(time, p))
            s.game.coils.redROLamp.pulse(85)
            pygame.display.update(dirty_rects)
            return
    if num in [11,36]:
        if s.game.yellow_star.status == False:
            p = [542,515]
            dirty_rects.append(screen.blit(time, p))
            s.game.coils.yellowROLamp.pulse(85)
            pygame.display.update(dirty_rects)
            return
    if num in [7,32]:
        if s.game.yellow_super_section.status == False:
            if s.game.red_super_section.status == False:
                p = [18,205]
                dirty_rects.append(screen.blit(super_section, p))
                pygame.display.update(dirty_rects)
                return
    if num in [0,25]:
        if s.game.red_super_section.status == False:
            if s.game.yellow_super_section.status == False:
                p = [581,201]
                dirty_rects.append(screen.blit(super_section, p))
                pygame.display.update(dirty_rects)
                return
    if num in [19,44]:
        if s.game.gate.status == False:
            p = [25,667]
            dirty_rects.append(screen.blit(ok_gate, p))
            pygame.display.update(dirty_rects)
            return
    if num in [16,41,23,48]:
        if s.game.ok.status == False:
            p = [112,667]
            dirty_rects.append(screen.blit(ok_gate, p))
            pygame.display.update(dirty_rects)
            return
    if num in [2,12,27,37]:
        if s.game.magic_screen_feature.position < 7:
            p = [247,667]
            dirty_rects.append(screen.blit(ms_letter, p))
            p = [287,667]
            dirty_rects.append(screen.blit(ms_letter, p))
            p = [325,667]
            dirty_rects.append(screen.blit(ms_letter, p))
            p = [366,667]
            dirty_rects.append(screen.blit(ms_letter, p))
            pygame.display.update(dirty_rects)
            return
    if num in [3,22,28,47]:
        if s.game.magic_screen_feature.position < 8:
            p = [404,667]
            dirty_rects.append(screen.blit(ms_letter, p))
            pygame.display.update(dirty_rects)
            return
    if num in [1,14,26,39]:
        if s.game.magic_screen_feature.position < 9:
            p = [443,667]
            dirty_rects.append(screen.blit(ms_letter, p))
            pygame.display.update(dirty_rects)
            return
    if num in [5,15,30,40]:
        if s.game.magic_screen_feature.position < 10:
            p = [482,667]
            dirty_rects.append(screen.blit(ms_letter, p))
            pygame.display.update(dirty_rects)
            return
    if num in [8,33]:
        if s.game.three_blue.status == False:
            p = [19,382]
            dirty_rects.append(screen.blit(blue_section, p))
            pygame.display.update(dirty_rects)
            return
        else:
            p = [19,352]
            dirty_rects.append(screen.blit(blue_section, p))
            pygame.display.update(dirty_rects)
            return
    if num in [20,45]:
        if s.game.two_blue.status == False:
            p = [19,324]
            dirty_rects.append(screen.blit(blue_section, p))
            pygame.display.update(dirty_rects)
            return


def feature_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]

    clear_features(s, num)

    draw_feature_animation(s, num)

def both_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]

    clear_features(s, num)
    clear_odds(s, num)

    draw_odds_animation(s, num)
    draw_feature_animation(s, num)
