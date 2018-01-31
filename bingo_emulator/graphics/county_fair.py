
import pygame
import random

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

meter = pygame.image.load('graphics/assets/register_cover.png').convert()
magic_screen = pygame.image.load('county_fair/assets/magic_screen.png').convert()
number_card = pygame.image.load('county_fair/assets/number_card.png').convert()
odds = pygame.image.load('county_fair/assets/odds.png').convert_alpha()
eb = pygame.image.load('county_fair/assets/eb.png').convert_alpha()
eb_number = pygame.image.load('county_fair/assets/eb_number.png').convert_alpha()
extra_balls = pygame.image.load('county_fair/assets/extra_balls.png').convert_alpha()
feature = pygame.image.load('county_fair/assets/feature.png').convert_alpha()
ms_indicator = pygame.image.load('county_fair/assets/ms_indicator.png').convert_alpha()
ti = pygame.image.load('county_fair/assets/time_indicator.png').convert_alpha()
super_section = pygame.image.load('county_fair/assets/super_section.png').convert_alpha()
ms_letter = pygame.image.load('county_fair/assets/ms_letter.png').convert_alpha()
number = pygame.image.load('county_fair/assets/number.png').convert_alpha()
select_now = pygame.image.load('county_fair/assets/select_now.png').convert_alpha()
three_blue = pygame.image.load('county_fair/assets/three_blue.png').convert_alpha()
tilt = pygame.image.load('county_fair/assets/tilt.png').convert_alpha()
c = pygame.image.load('county_fair/assets/c.png').convert_alpha()
red_c = pygame.image.load('county_fair/assets/red_c.png').convert_alpha()
yo = pygame.image.load('county_fair/assets/o.png').convert_alpha()
red_o = pygame.image.load('county_fair/assets/red_o.png').convert_alpha()
u = pygame.image.load('county_fair/assets/u.png').convert_alpha()
red_u = pygame.image.load('county_fair/assets/red_u.png').convert_alpha()
n = pygame.image.load('county_fair/assets/n.png').convert_alpha()
red_n = pygame.image.load('county_fair/assets/red_n.png').convert_alpha()
t = pygame.image.load('county_fair/assets/t.png').convert_alpha()
red_t = pygame.image.load('county_fair/assets/red_t.png').convert_alpha()
y = pygame.image.load('county_fair/assets/y.png').convert_alpha()
red_y = pygame.image.load('county_fair/assets/red_y.png').convert_alpha()
bg_menu = pygame.image.load('county_fair/assets/county_fair_menu.png').convert()
bg_menu.set_colorkey((255,0,252))
bg_gi = pygame.image.load('county_fair/assets/county_fair_gi.png').convert()
bg_gi.set_colorkey((255,0,252))
bg_off = pygame.image.load('county_fair/assets/county_fair_off.png').convert()
bg_off.set_colorkey((255,0,252))

class scorereel():
    """ Score Reels are used to count replays """
    def __init__(self, pos, image):
        self.position = pos
        self.default_y = self.position[1]
        self.image = pygame.image.load(image).convert()

reel1 = scorereel([97,793], "graphics/assets/white_reel.png")
reel10 = scorereel([78,793], "graphics/assets/white_reel.png")
reel100 = scorereel([59,793], "graphics/assets/white_reel.png")

def display(s, replays=0, menu=False):
    
    meter.set_colorkey((255,0,252))
    meter_position = [50,793]

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
        screen.blit(bg_menu, backglass_position)
    else:
        if (s.game.anti_cheat.status == True):
            screen.blit(bg_gi, backglass_position)
        else:
            screen.blit(bg_off, backglass_position)

    if s.game.green_odds.position < 4:
        rc = [108,255]
        screen.blit(red_c, rc)
    else:
        rc = [108,255]
        screen.blit(c, rc)

    if s.game.green_odds.position == 4:
        ro = [154,258]
        screen.blit(red_o, ro)
    else:
        ro = [154,258]
        screen.blit(yo, ro)

    if s.game.green_odds.position == 5:
        ru = [204,258]
        screen.blit(red_u, ru)
    else:
        ru = [204,258]
        screen.blit(u, ru)

    if s.game.green_odds.position == 6:
        rn = [256,258]
        screen.blit(red_n, rn)
    else:
        rn = [256,258]
        screen.blit(n, rn)

    if s.game.green_odds.position == 7:
        rt = [305,259]
        screen.blit(red_t, rt)
    else:
        rt = [305,259]
        screen.blit(t, rt)

    if s.game.green_odds.position == 8:
        ry = [350,259]
        screen.blit(red_y, ry)
    else:
        ry = [350,259]
        screen.blit(y, ry)


    if s.game.eb_play.status == True:
        eb_position = [37,1027]
        screen.blit(extra_balls, eb_position)

    if s.game.extra_ball.position >= 1:
        eb_position = [145,1026]
        screen.blit(eb_number, eb_position)
    if s.game.extra_ball.position >= 2:
        eb_position = [195,1025]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 3:
        eb_position = [257,1025]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 4:
        eb_position = [327,1025]
        screen.blit(eb_number, eb_position)
    if s.game.extra_ball.position >= 5:
        eb_position = [373,1025]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 6:
        eb_position = [436,1025]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 7:
        eb_position = [504,1025]
        screen.blit(eb_number, eb_position)
    if s.game.extra_ball.position >= 8:
        eb_position = [552,1025]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 9:
        eb_position = [615,1025]
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
        rs_position = [550,461]
        screen.blit(feature, rs_position)
    if s.game.yellow_star.status == True:
        rs_position = [550,516]
        screen.blit(feature, rs_position)

    if s.game.magic_screen_feature.position >= 7 or s.game.ok.status == True:
        if s.game.selection_feature.position < 7:
            bfp = [550,572]
            screen.blit(feature, bfp)
            if s.game.ball_count.position == 3:
                s.cancel_delayed(name="blink")
                blink([s,1,1])
            else:
                s.cancel_delayed(name="blink")
        elif s.game.selection_feature.position == 7:
            bfp = [550,407]
            screen.blit(feature, bfp)
            if s.game.ball_count.position == 4:
                s.cancel_delayed(name="blink")
                blink([s,1,1])
            else:
                s.cancel_delayed(name="blink")
        elif s.game.selection_feature.position == 8:
            bfp = [550,349]
            screen.blit(feature, bfp)
            if s.game.ball_count.position == 5:
                s.cancel_delayed(name="blink")
                blink([s,1,1])
            else:
                s.cancel_delayed(name="blink")

    if s.game.magic_screen_feature.position >= 9:
        if s.game.three_blue.status == True:
            bp = [48,353]
            screen.blit(three_blue, bp)
        elif s.game.two_blue.status == True:
            bp = [113,353]
            screen.blit(three_blue, bp)

    if s.game.red_super_section.status == True:
        rss = [45,450]
        screen.blit(super_section, rss)
    if s.game.yellow_super_section.status == True:
        yss = [45,541]
        screen.blit(super_section, yss)

    if s.game.magic_screen_feature.position >= 4:
        ms = [150,667]
        screen.blit(ms_letter, ms)
    if s.game.magic_screen_feature.position >= 5:
        ms = [190,667]
        screen.blit(ms_letter, ms)
    if s.game.magic_screen_feature.position >= 6:
        ms = [230,667]
        screen.blit(ms_letter, ms)
    if s.game.magic_screen_feature.position >= 7:
        ms = [275,667]
        screen.blit(ms_letter, ms)
    if s.game.magic_screen_feature.position >= 8:
        ms = [316,667]
        screen.blit(ms_letter, ms)
    if s.game.magic_screen_feature.position >= 9:
        ms = [354,667]
        screen.blit(ms_letter, ms)
    if s.game.magic_screen_feature.position >= 10:
        ms = [393,667]
        screen.blit(ms_letter, ms)

    if s.game.ok.status == True:
        ms = [68,667]
        screen.blit(ms_letter, ms)
        ms = [25,667]
        screen.blit(ms_letter, ms)


    if s.game.magic_screen.position == 0:
        ms = [32,726]
        screen.blit(ms_indicator, ms)
    if s.game.magic_screen.position == 1:
        ms = [75,726]
        screen.blit(ms_indicator, ms)
    if s.game.magic_screen.position == 3:
        ms = [158,724]
        screen.blit(ms_indicator, ms)
    if s.game.magic_screen.position == 4:
        ms = [200,724]
        screen.blit(ms_indicator, ms)
    if s.game.magic_screen.position == 5:
        ms = [238,724]
        screen.blit(ms_indicator, ms)
    if s.game.magic_screen.position == 6:
        ms = [280,724]
        screen.blit(ms_indicator, ms)
    if s.game.magic_screen.position == 7:
        ms = [323,724]
        screen.blit(ms_indicator, ms)
    if s.game.magic_screen.position == 8:
        ms = [362,724]
        screen.blit(ms_indicator, ms)
    if s.game.magic_screen.position == 9:
        ms = [402,724]
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
        tilt_position = [572,632]
        screen.blit(tilt, tilt_position)

    pygame.display.update()

def blink(args):
    dirty_rects = []
    s = args[0]
    b = args[1]
    sn = args[2]

    if b == 0:
        if sn == 1:
            p = [571,680]
            dirty_rects.append(screen.blit(select_now, p))
        pygame.display.update(dirty_rects)
    else:
        dirty_rects.append(screen.blit(bg_gi, (571,680), pygame.Rect(571,680,124,35)))
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
        rss = [45,450]
        screen.blit(super_section, rss)
        pygame.display.update()
    else:
        yss = [45,541]
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


