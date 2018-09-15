
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
bg_menu = pygame.image.load('silver_sails/assets/silver_sails_menu.png').convert()
bg_menu.set_colorkey((255,0,252))
bg_gi = pygame.image.load('silver_sails/assets/silver_sails_gi.png').convert()
bg_gi.set_colorkey((255,0,252))
bg_off = pygame.image.load('silver_sails/assets/silver_sails_off.png').convert()
bg_off.set_colorkey((255,0,252))

class scorereel():
    """ Score Reels are used to count replays """
    def __init__(self, pos, image):
        self.position = pos
        self.default_y = self.position[1]
        self.image = pygame.image.load(image).convert()

reel1 = scorereel([102,795], "graphics/assets/white_reel.png")
reel10 = scorereel([83,795], "graphics/assets/white_reel.png")
reel100 = scorereel([64,795], "graphics/assets/white_reel.png")

def display(s, replays=0, menu=False):
    
    meter.set_colorkey((255,0,252))
    meter_position = [55,795]

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
            if s.game.ball_count.position == 3:
                s.cancel_delayed(name="blink")
                blink([s,1,1])
            else:
                s.cancel_delayed(name="blink")
        elif s.game.selection_feature.position == 7:
            bfp = [551,402]
            screen.blit(time, bfp)
            if s.game.ball_count.position == 4:
                s.cancel_delayed(name="blink")
                blink([s,1,1])
            else:
                s.cancel_delayed(name="blink")
        elif s.game.selection_feature.position == 8:
            bfp = [551,346]
            screen.blit(time, bfp)
            if s.game.ball_count.position == 5:
                s.cancel_delayed(name="blink")
                blink([s,1,1])
            else:
                s.cancel_delayed(name="blink")

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
            if s.game.all_advantages.status == True:
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

def blink(args):
    dirty_rects = []
    s = args[0]
    b = args[1]
    sn = args[2]

    if b == 0:
        if sn == 1:
            p = [576,676]
            dirty_rects.append(screen.blit(select_now, p))
        pygame.display.update(dirty_rects)
    else:
        dirty_rects.append(screen.blit(bg_gi, (576,676), pygame.Rect(576,676,121,41)))
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
        bp = [33,413]
        dirty_rects.append(screen.blit(bg_gi, bp, pygame.Rect(bp[0],bp[1],152,28)))
        dirty_rects.append(screen.blit(golden_game, bp))
        if s.game.two_gold.status == False:
            bp = [70,438]
            dirty_rects.append(screen.blit(bg_gi, bp, pygame.Rect(bp[0],bp[1],124,79)))
            dirty_rects.append(screen.blit(gold_section, bp))
        else:
            bp = [70,515]
            dirty_rects.append(screen.blit(bg_gi, bp, pygame.Rect(bp[0],bp[1],124,79)))
            dirty_rects.append(screen.blit(gold_section, bp))
            bp = [104,589]
            dirty_rects.append(screen.blit(bg_gi, bp, pygame.Rect(bp[0],bp[1],46,33)))
            dirty_rects.append(screen.blit(gold_arrow, bp))

    if s.game.green_odds.position == 1 or s.game.green_odds.position == 2 or s.game.gold_odds == 75:
        bp = [29,590]
        dirty_rects.append(screen.blit(bg_gi, bp, pygame.Rect(bp[0],bp[1],43,30)))
        dirty_rects.append(screen.blit(gold_odds, bp))
    elif s.game.green_odds.position == 3 or s.game.green_odds.position == 4 or s.game.gold_odds == 96:
        bp = [30,562]
        dirty_rects.append(screen.blit(bg_gi, bp, pygame.Rect(bp[0],bp[1],43,30)))
        dirty_rects.append(screen.blit(gold_odds, bp))
    elif s.game.green_odds.position == 5 or s.game.gold_odds == 200:
        bp = [30,533]
        dirty_rects.append(screen.blit(bg_gi, bp, pygame.Rect(bp[0],bp[1],43,30)))
        dirty_rects.append(screen.blit(gold_odds, bp))
    elif s.game.green_odds.position == 6 or s.game.gold_odds == 300:
        bp = [30,504]
        dirty_rects.append(screen.blit(bg_gi, bp, pygame.Rect(bp[0],bp[1],43,30)))
        dirty_rects.append(screen.blit(gold_odds, bp))
    elif s.game.green_odds.position == 7 or s.game.gold_odds == 450:
        bp = [30,474]
        dirty_rects.append(screen.blit(bg_gi, bp, pygame.Rect(bp[0],bp[1],43,30)))
        dirty_rects.append(screen.blit(gold_odds, bp))
    elif s.game.green_odds.position == 8 or s.game.gold_odds == 600:
        bp = [30,446]
        dirty_rects.append(screen.blit(bg_gi, bp, pygame.Rect(bp[0],bp[1],43,30)))
        dirty_rects.append(screen.blit(gold_odds, bp))

    if s.game.magic_screen_feature.position >= 9:
        if s.game.three_blue.status == True:
            bp = [23,379]
            dirty_rects.append(screen.blit(bg_gi, bp, pygame.Rect(bp[0],bp[1],173,35)))
            dirty_rects.append(screen.blit(blue_section, bp))
        elif s.game.three_blue_six.status == True:
            bp = [23,349]
            dirty_rects.append(screen.blit(bg_gi, bp, pygame.Rect(bp[0],bp[1],173,35)))
            dirty_rects.append(screen.blit(blue_section, bp))
        elif s.game.two_blue.status == True:
            bp = [23,320]
            dirty_rects.append(screen.blit(bg_gi, bp, pygame.Rect(bp[0],bp[1],173,35)))
            dirty_rects.append(screen.blit(blue_section, bp))

    if s.game.magic_screen_feature.position >= 7 or s.game.ok.status == True or s.game.golden.status == True:
        if s.game.selection_feature.position < 7:
            bfp = [551,573]
            dirty_rects.append(screen.blit(bg_gi, bfp, pygame.Rect(bfp[0],bfp[1],120,56)))
            dirty_rects.append(screen.blit(time, bfp))
        elif s.game.selection_feature.position == 7:
            bfp = [551,402]
            dirty_rects.append(screen.blit(bg_gi, bfp, pygame.Rect(bfp[0],bfp[1],120,56)))
            screen.blit(time, bfp)
        elif s.game.selection_feature.position == 8:
            bfp = [551,346]
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
        rs_position = [550,458]
        dirty_rects.append(screen.blit(bg_gi, rs_position, pygame.Rect(rs_position[0],rs_position[1],120,56)))
        dirty_rects.append(screen.blit(time, rs_position))
    if s.game.yellow_star.status == True:
        rs_position = [550,515]
        dirty_rects.append(screen.blit(bg_gi, rs_position, pygame.Rect(rs_position[0],rs_position[1],120,56)))
        dirty_rects.append(screen.blit(time, rs_position))

    if s.game.red_super_section.status == True:
        rss = [585,203]
        dirty_rects.append(screen.blit(bg_gi, rss, pygame.Rect(rss[0],rss[1],120,86)))
        dirty_rects.append(screen.blit(super_section, rss))
    if s.game.yellow_super_section.status == True:
        yss = [25,203]
        dirty_rects.append(screen.blit(bg_gi, yss, pygame.Rect(yss[0],yss[1],120,86)))
        dirty_rects.append(screen.blit(super_section, yss))

    pygame.display.update(dirty_rects)

def eb_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]

    if s.game.extra_ball.position < 1:
        dirty_rects.append(screen.blit(bg_gi, (150,1032), pygame.Rect(150,1032,52,38)))
    if s.game.extra_ball.position < 2:
        dirty_rects.append(screen.blit(bg_gi, (200,1032), pygame.Rect(200,1032,60,38)))
    if s.game.extra_ball.position < 3:
        dirty_rects.append(screen.blit(bg_gi, (268,1032), pygame.Rect(268,1032,60,38)))
    if s.game.extra_ball.position < 4:
        dirty_rects.append(screen.blit(bg_gi, (332,1032), pygame.Rect(332,1032,52,38)))
    if s.game.extra_ball.position < 5:
        dirty_rects.append(screen.blit(bg_gi, (378,1032), pygame.Rect(378,1032,60,38)))
    if s.game.extra_ball.position < 6:
        dirty_rects.append(screen.blit(bg_gi, (446,1032), pygame.Rect(446,1032,60,38)))
    if s.game.extra_ball.position < 7:
        dirty_rects.append(screen.blit(bg_gi, (509,1032), pygame.Rect(509,1032,52,38)))
    if s.game.extra_ball.position < 8:
        dirty_rects.append(screen.blit(bg_gi, (557,1032), pygame.Rect(557,1032,60,38)))
    if s.game.extra_ball.position < 9:
        dirty_rects.append(screen.blit(bg_gi, (623,1031), pygame.Rect(623,1031,60,38)))
    pygame.display.update(dirty_rects)

    if num in [0,25,14,49]:
        if s.game.extra_ball.position < 1:
            p = [150,1032]
            dirty_rects.append(screen.blit(eb_number, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [39,1,26,15]:
        if s.game.extra_ball.position < 2:
            p = [200,1032]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [3,4,17,28,29,40]:
        if s.game.extra_ball.position < 3:
            p = [268,1032]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [5,18,30,43]:
        if s.game.extra_ball.position < 4:
            p = [332,1032]
            dirty_rects.append(screen.blit(eb_number, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [7,8,19,32,33,44]:
        if s.game.extra_ball.position < 5:
            p = [378,1032]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [9,10,20,34,35,45]:
        if s.game.extra_ball.position < 6:
            p = [446,1032]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [11,21,36,46]:
        if s.game.extra_ball.position < 7:
            p = [509,1032]
            dirty_rects.append(screen.blit(eb_number, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [12,22,37,47]:
        if s.game.extra_ball.position < 8:
            p = [557,1032]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [2,6,13,16,23,27,31,38,41,48]:
        if s.game.extra_ball.position < 9:
            p = [623,1031]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return

def clear_odds(s, num):
    global screen

    dirty_rects = []

    if s.game.yellow_odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (187,850), pygame.Rect(187,850,48,76)))
    if s.game.yellow_odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (250,850), pygame.Rect(250,850,48,76)))
    if s.game.yellow_odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (310,850), pygame.Rect(310,850,48,76)))
    if s.game.yellow_odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (371,850), pygame.Rect(371,850,48,76)))
    if s.game.yellow_odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (428,850), pygame.Rect(428,850,48,76)))
    if s.game.yellow_odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (476,850), pygame.Rect(476,850,48,76)))
    if s.game.yellow_odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (525,850), pygame.Rect(525,850,48,76)))
    if s.game.yellow_odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (573,850), pygame.Rect(573,850,48,76)))

    if s.game.red_odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (187,784), pygame.Rect(187,784,48,76)))
    if s.game.red_odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (250,784), pygame.Rect(250,784,48,76)))
    if s.game.red_odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (310,784), pygame.Rect(310,784,48,76)))
    if s.game.red_odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (371,784), pygame.Rect(371,784,48,76)))
    if s.game.red_odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (428,784), pygame.Rect(428,784,48,76)))
    if s.game.red_odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (476,784), pygame.Rect(476,784,48,76)))
    if s.game.red_odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (525,784), pygame.Rect(525,784,48,76)))
    if s.game.red_odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (573,784), pygame.Rect(573,784,48,76)))

    if s.game.green_odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (187,920), pygame.Rect(187,920,48,76)))
    if s.game.green_odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (250,920), pygame.Rect(250,920,48,76)))
    if s.game.green_odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (310,920), pygame.Rect(310,920,48,76)))
    if s.game.green_odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (371,920), pygame.Rect(371,920,48,76)))
    if s.game.green_odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (428,920), pygame.Rect(428,920,48,76)))
    if s.game.green_odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (476,920), pygame.Rect(476,920,48,76)))
    if s.game.green_odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (525,920), pygame.Rect(525,920,48,76)))
    if s.game.green_odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (573,920), pygame.Rect(573,920,48,76)))

    pygame.display.update(dirty_rects)

def draw_odds_animation(s, num):
    global screen
    dirty_rects = []

    if num in [11,36]:
        if s.game.yellow_odds.position != 1:
            p = [187,850]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [4,29]:
        if s.game.yellow_odds.position != 2:
            p = [250,850]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [7,32]:
        if s.game.yellow_odds.position != 3:
            p = [310,850]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [13,38]:
        if s.game.yellow_odds.position != 4:
            p = [371,850]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [22,47]:
        if s.game.yellow_odds.position != 5:
            p = [428,850]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [17,42]:
        if s.game.yellow_odds.position != 6:
            p = [476,850]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [19,44]:
        if s.game.yellow_odds.position != 7:
            p = [525,850]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [5,30]:
        if s.game.yellow_odds.position != 8:
            p = [573,850]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return

    if num in [0,25]:
        if s.game.red_odds.position != 1:
            p = [187,784]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [15,40]:
        if s.game.red_odds.position != 2:
            p = [250,784]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [24,49]:
        if s.game.red_odds.position != 3:
            p = [310,784]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [9,34]:
        if s.game.red_odds.position != 4:
            p = [371,784]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [20,45]:
        if s.game.red_odds.position != 5:
            p = [428,784]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [12,37]:
        if s.game.red_odds.position != 6:
            p = [476,784]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [50,26]:
        if s.game.red_odds.position != 7:
            p = [525,784]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [6,31]:
        if s.game.red_odds.position != 8:
            p = [573,784]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return

    if num in [16,41]:
        if s.game.green_odds.position != 1:
            p = [187,920]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [18,43]:
        if s.game.green_odds.position != 2:
            p = [250,920]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [14,39]:
        if s.game.green_odds.position != 3:
            p = [310,920]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [3,28]:
        if s.game.green_odds.position != 4:
            p = [371,920]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [23,48]:
        if s.game.green_odds.position != 5:
            p = [428,920]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [8,33]:
        if s.game.green_odds.position != 6:
            p = [476,920]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [22,47]:
        if s.game.green_odds.position != 7:
            p = [525,920]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [10,35]:
        if s.game.green_odds.position != 8:
            p = [573,920]
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
        dirty_rects.append(screen.blit(bg_gi, (551,573), pygame.Rect(551,573,120,56)))
    if s.game.red_star.status == False:
        dirty_rects.append(screen.blit(bg_gi, (550,458), pygame.Rect(550,458,120,56)))
    if s.game.yellow_star.status == False:
        dirty_rects.append(screen.blit(bg_gi, (550,515), pygame.Rect(550,515,120,56)))
    if s.game.selection_feature.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (551,402), pygame.Rect(551,402,120,56)))
    if s.game.selection_feature.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (551,346), pygame.Rect(551,346,120,56)))

    if s.game.yellow_super_section.status == False:
        dirty_rects.append(screen.blit(bg_gi, (25,203), pygame.Rect(25,203,120,86)))
    if s.game.red_super_section.status == False:
        dirty_rects.append(screen.blit(bg_gi, (585,203), pygame.Rect(585,203,120,86)))
    if s.game.gate.status == False:
        dirty_rects.append(screen.blit(bg_gi, (27,668), pygame.Rect(27,668,86,52)))
    if s.game.ok.status == False:
        dirty_rects.append(screen.blit(bg_gi, (114,668), pygame.Rect(114,668,86,52)))
    if s.game.magic_screen_feature.position < 7:
        dirty_rects.append(screen.blit(bg_gi, (250,669), pygame.Rect(250,669,41,51)))
        dirty_rects.append(screen.blit(bg_gi, (292,670), pygame.Rect(292,670,41,51)))
        dirty_rects.append(screen.blit(bg_gi, (330,670), pygame.Rect(330,670,41,51)))
        dirty_rects.append(screen.blit(bg_gi, (370,670), pygame.Rect(370,670,41,51)))
    if s.game.magic_screen_feature.position < 8:
        dirty_rects.append(screen.blit(bg_gi, (409,670), pygame.Rect(409,670,41,51)))
    if s.game.magic_screen_feature.position < 9:
        dirty_rects.append(screen.blit(bg_gi, (451,670), pygame.Rect(451,670,41,51)))
    if s.game.magic_screen_feature.position < 10:
        dirty_rects.append(screen.blit(bg_gi, (491,670), pygame.Rect(491,670,41,51)))
    if s.game.three_blue.status == False:
       dirty_rects.append(screen.blit(bg_gi, (23,379), pygame.Rect(23,379,173,35)))
    if s.game.three_blue_six.status == False:
       dirty_rects.append(screen.blit(bg_gi, (23,349), pygame.Rect(23,349,173,35)))
    if s.game.two_blue.status == False:
        dirty_rects.append(screen.blit(bg_gi, (23,320), pygame.Rect(23,320,173,35)))

    pygame.display.update(dirty_rects)


def draw_feature_animation(s, num):
    global screen
    dirty_rects = []
 
    if num in [10,35]:
        if (s.game.magic_screen_feature.position <= 4 and s.game.ok.status == False) and s.game.selection_feature.position not in [7,8]:
            p = [551,573]
            dirty_rects.append(screen.blit(time, p))
            pygame.display.update(dirty_rects)
            return
    if num in [9,34]:
        if s.game.selection_feature.position != 7:
            p = [551,402]
            dirty_rects.append(screen.blit(time, p))
            pygame.display.update(dirty_rects)
            return
    if num in [6,17,21,31,42,46]:
        if s.game.selection_feature.position != 8:
            p = [551,346]
            dirty_rects.append(screen.blit(time, p))
            pygame.display.update(dirty_rects)
            return
    if num in [4,29]:
        if s.game.red_star.status == False:
            p = [550,458]
            dirty_rects.append(screen.blit(time, p))
            s.game.coils.redROLamp.pulse(85)
            pygame.display.update(dirty_rects)
            return
    if num in [11,36]:
        if s.game.yellow_star.status == False:
            p = [550,515]
            dirty_rects.append(screen.blit(time, p))
            s.game.coils.yellowROLamp.pulse(85)
            pygame.display.update(dirty_rects)
            return
    if num in [7,32]:
        if s.game.yellow_super_section.status == False:
            if s.game.red_super_section.status == False:
                p = [25,203]
                dirty_rects.append(screen.blit(super_section, p))
                pygame.display.update(dirty_rects)
                return
    if num in [0,25]:
        if s.game.red_super_section.status == False:
            if s.game.yellow_super_section.status == False:
                p = [585,203]
                dirty_rects.append(screen.blit(super_section, p))
                pygame.display.update(dirty_rects)
                return
    if num in [19,44]:
        if s.game.gate.status == False:
            p = [27,668]
            dirty_rects.append(screen.blit(ok_gate, p))
            pygame.display.update(dirty_rects)
            return
    if num in [16,41,23,48]:
        if s.game.ok.status == False:
            p = [114,668]
            dirty_rects.append(screen.blit(ok_gate, p))
            pygame.display.update(dirty_rects)
            return
    if num in [2,12,27,37]:
        if s.game.magic_screen_feature.position < 7:
            p = [250,669]
            dirty_rects.append(screen.blit(ms_letter, p))
            p = [292,670]
            dirty_rects.append(screen.blit(ms_letter, p))
            p = [330,670]
            dirty_rects.append(screen.blit(ms_letter, p))
            p = [370,670]
            dirty_rects.append(screen.blit(ms_letter, p))
            pygame.display.update(dirty_rects)
            return
    if num in [3,22,28,47]:
        if s.game.magic_screen_feature.position < 8:
            p = [409,670]
            dirty_rects.append(screen.blit(ms_letter, p))
            pygame.display.update(dirty_rects)
            return
    if num in [1,14,26,39]:
        if s.game.magic_screen_feature.position < 9:
            p = [451,670]
            dirty_rects.append(screen.blit(ms_letter, p))
            pygame.display.update(dirty_rects)
            return
    if num in [5,15,30,40]:
        if s.game.magic_screen_feature.position < 10:
            p = [491,670]
            dirty_rects.append(screen.blit(ms_letter, p))
            pygame.display.update(dirty_rects)
            return
    if num in [8,33]:
        if s.game.three_blue.status == False:
            p = [23,379]
            dirty_rects.append(screen.blit(blue_section, p))
            pygame.display.update(dirty_rects)
            return
        else:
            p = [23,349]
            dirty_rects.append(screen.blit(blue_section, p))
            pygame.display.update(dirty_rects)
            return
    if num in [20,45]:
        if s.game.two_blue.status == False:
            p = [23,320]
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
