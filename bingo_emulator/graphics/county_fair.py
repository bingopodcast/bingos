
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
bg_gi = pygame.image.load('county_fair/assets/county_fair_gi.png').convert_alpha()
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

def screen_animation(args):
    dirty_rects = []
    s = args[0]
    num = args[1]
    direction = args[2]
    
    number_card_position = [235,363]

    dirty_rects.append(screen.blit(number_card, number_card_position))

    magic_screen.set_colorkey((255,0,252))

    if s.game.magic_screen.position == 0:
        p = [240,358]
    elif s.game.magic_screen.position == 1:
        p = [192,358]
    elif s.game.magic_screen.position == 2:
        p = [145,358]
    elif s.game.magic_screen.position == 3:
        p = [96,358]
    elif s.game.magic_screen.position == 4:
        p = [49,358]
    elif s.game.magic_screen.position == 5:
        p = [3,358]
    elif s.game.magic_screen.position == 6:
        p = [-45,358]
    elif s.game.magic_screen.position == 7:
        p = [-92,358]
    elif s.game.magic_screen.position == 8:
        p = [-139,358]
    elif s.game.magic_screen.position == 9:
        p = [-187,358]

    if direction == "left":
       p[0] = p[0] + num
    else:
       p[0] = p[0] - num
 
    dirty_rects.append(screen.blit(magic_screen, p))
    
    backglass_position = [0, 0]
    if (s.game.anti_cheat.status == True):
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],660,280)))
    else:
        dirty_rects.append(screen.blit(bg_off, p, pygame.Rect(p[0],p[1],660,280)))
    if s.game.magic_screen_feature.position >= 9:
        if s.game.three_blue.status == True:
            bp = [48,353]
            dirty_rects.append(screen.blit(bg_gi, bp, pygame.Rect(bp[0],bp[1],56,94)))
            dirty_rects.append(screen.blit(three_blue, bp))
        elif s.game.two_blue.status == True:
            bp = [113,353]
            dirty_rects.append(screen.blit(bg_gi, bp, pygame.Rect(bp[0],bp[1],56,94)))
            dirty_rects.append(screen.blit(three_blue, bp))

    if s.game.selection_feature.position < 7:
        p = [550,572]
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],119,59)))
        dirty_rects.append(screen.blit(feature, p))
    if s.game.red_star.status == True:
        p = [550,461]
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],119,59)))
        dirty_rects.append(screen.blit(feature, p))
    if s.game.yellow_star.status == True:
        p = [550,516]
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],119,59)))
        dirty_rects.append(screen.blit(feature, p))
    if s.game.selection_feature.position == 7:
        p = [550,407]
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],119,59)))
        dirty_rects.append(screen.blit(feature, p))
    if s.game.selection_feature.position == 8:
        p = [550,349]
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],119,59)))
        dirty_rects.append(screen.blit(feature, p))

    if s.game.red_super_section.status == True:
        yss = [45,450]
        dirty_rects.append(screen.blit(bg_gi, (45,450), pygame.Rect(45,450,127,84)))
        dirty_rects.append(screen.blit(super_section, rss))
    if s.game.yellow_super_section.status == True:
        rss = [45,541]
        dirty_rects.append(screen.blit(bg_gi, (45,541), pygame.Rect(45,541,127,84)))
        dirty_rects.append(screen.blit(super_section, yss))

    pygame.display.update(dirty_rects)


def eb_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]

    if s.game.extra_ball.position < 1:
        dirty_rects.append(screen.blit(bg_gi, (145,1026), pygame.Rect(145,1026,50,34)))
    if s.game.extra_ball.position < 2:
        dirty_rects.append(screen.blit(bg_gi, (195,1025), pygame.Rect(195,1025,67,35)))
    if s.game.extra_ball.position < 3:
        dirty_rects.append(screen.blit(bg_gi, (257,1025), pygame.Rect(257,1025,67,35)))
    if s.game.extra_ball.position < 4:
        dirty_rects.append(screen.blit(bg_gi, (327,1025), pygame.Rect(327,1025,50,34)))
    if s.game.extra_ball.position < 5:
        dirty_rects.append(screen.blit(bg_gi, (373,1025), pygame.Rect(373,1025,67,35)))
    if s.game.extra_ball.position < 6:
        dirty_rects.append(screen.blit(bg_gi, (436,1025), pygame.Rect(436,1025,67,35)))
    if s.game.extra_ball.position < 7:
        dirty_rects.append(screen.blit(bg_gi, (504,1025), pygame.Rect(504,1025,50,34)))
    if s.game.extra_ball.position < 8:
        dirty_rects.append(screen.blit(bg_gi, (552,1025), pygame.Rect(552,1025,67,35)))
    if s.game.extra_ball.position < 9:
        dirty_rects.append(screen.blit(bg_gi, (615,1025), pygame.Rect(615,1025,67,35)))
    pygame.display.update(dirty_rects)

    if num in [0,25,14,49]:
        if s.game.extra_ball.position < 1:
            p = [145,1026]
            dirty_rects.append(screen.blit(eb_number, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [39,1,26,15]:
        if s.game.extra_ball.position < 2:
            p = [195,1025]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [3,4,17,28,29,40]:
        if s.game.extra_ball.position < 3:
            p = [257,1025]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [5,18,30,43]:
        if s.game.extra_ball.position < 4:
            p = [327,1025]
            dirty_rects.append(screen.blit(eb_number, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [7,8,19,32,33,44]:
        if s.game.extra_ball.position < 5:
            p = [373,1025]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [9,10,20,34,35,45]:
        if s.game.extra_ball.position < 6:
            p = [436,1025]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [11,21,36,46]:
        if s.game.extra_ball.position < 7:
            p = [504,1025]
            dirty_rects.append(screen.blit(eb_number, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [12,22,37,47]:
        if s.game.extra_ball.position < 8:
            p = [552,1025]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [2,6,13,16,23,27,31,38,41,48]:
        if s.game.extra_ball.position < 9:
            p = [615,1025]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return

def clear_odds(s, num):
    global screen

    dirty_rects = []

    if s.game.yellow_odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (187,838), pygame.Rect(187,838,48,76)))
    if s.game.yellow_odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (247,838), pygame.Rect(247,838,48,76)))
    if s.game.yellow_odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (309,838), pygame.Rect(309,838,48,76)))
    if s.game.yellow_odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (370,838), pygame.Rect(370,838,48,76)))
    if s.game.yellow_odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (423,838), pygame.Rect(423,838,48,76)))
    if s.game.yellow_odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (472,838), pygame.Rect(472,838,48,76)))
    if s.game.yellow_odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (522,838), pygame.Rect(522,838,48,76)))
    if s.game.yellow_odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (568,838), pygame.Rect(568,838,48,76)))

    if s.game.red_odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (187,772), pygame.Rect(187,772,48,76)))
    if s.game.red_odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (247,772), pygame.Rect(247,772,48,76)))
    if s.game.red_odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (309,772), pygame.Rect(309,772,48,76)))
    if s.game.red_odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (370,772), pygame.Rect(370,772,48,76)))
    if s.game.red_odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (423,772), pygame.Rect(423,772,48,76)))
    if s.game.red_odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (472,772), pygame.Rect(472,772,48,76)))
    if s.game.red_odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (522,772), pygame.Rect(522,772,48,76)))
    if s.game.red_odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (568,772), pygame.Rect(568,772,48,76)))

    if s.game.green_odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (187,908), pygame.Rect(187,908,48,76)))
    if s.game.green_odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (247,908), pygame.Rect(247,908,48,76)))
    if s.game.green_odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (309,908), pygame.Rect(309,908,48,76)))
    if s.game.green_odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (370,908), pygame.Rect(370,908,48,76)))
    if s.game.green_odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (423,908), pygame.Rect(423,908,48,76)))
    if s.game.green_odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (472,908), pygame.Rect(472,908,48,76)))
    if s.game.green_odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (522,908), pygame.Rect(522,908,48,76)))
    if s.game.green_odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (568,908), pygame.Rect(568,908,48,76)))

    pygame.display.update(dirty_rects)

def draw_odds_animation(s, num):
    global screen
    dirty_rects = []

    if num in [11,36]:
        if s.game.yellow_odds.position != 1:
            p = [187,838]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [4,29]:
        if s.game.yellow_odds.position != 2:
            p = [247,838]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [7,32]:
        if s.game.yellow_odds.position != 3:
            p = [309,838]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [13,38]:
        if s.game.yellow_odds.position != 4:
            p = [370,838]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [22,47]:
        if s.game.yellow_odds.position != 5:
            p = [423,838]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [17,42]:
        if s.game.yellow_odds.position != 6:
            p = [472,838]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [19,44]:
        if s.game.yellow_odds.position != 7:
            p = [522,838]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [5,30]:
        if s.game.yellow_odds.position != 8:
            p = [568,838]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return

    if num in [0,25]:
        if s.game.red_odds.position != 1:
            p = [187,772]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [15,40]:
        if s.game.red_odds.position != 2:
            p = [247,772]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [24,49]:
        if s.game.red_odds.position != 3:
            p = [309,772]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [9,34]:
        if s.game.red_odds.position != 4:
            p = [370,772]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [20,45]:
        if s.game.red_odds.position != 5:
            p = [423,772]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [12,37]:
        if s.game.red_odds.position != 6:
            p = [472,772]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [50,26]:
        if s.game.red_odds.position != 7:
            p = [522,772]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [6,31]:
        if s.game.red_odds.position != 8:
            p = [568,772]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return

    if num in [16,41]:
        if s.game.green_odds.position != 1:
            p = [187,908]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [18,43]:
        if s.game.green_odds.position != 2:
            p = [247,908]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [14,39]:
        if s.game.green_odds.position != 3:
            p = [309,908]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [3,28]:
        if s.game.green_odds.position != 4:
            p = [370,908]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [23,48]:
        if s.game.green_odds.position != 5:
            p = [423,908]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [8,33]:
        if s.game.green_odds.position != 6:
            p = [472,908]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [22,47]:
        if s.game.green_odds.position != 7:
            p = [522,908]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [10,35]:
        if s.game.green_odds.position != 8:
            p = [568,908]
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


    if s.game.selection_feature.position <= 7 and (s.game.magic_screen_feature.position < 4 and s.game.ok.status == False):
        dirty_rects.append(screen.blit(bg_gi, (550,572), pygame.Rect(550,572,119,59)))
    if s.game.red_star.status == False:
        dirty_rects.append(screen.blit(bg_gi, (550,461), pygame.Rect(550,461,119,59)))
    if s.game.yellow_star.status == False:
        dirty_rects.append(screen.blit(bg_gi, (550,516), pygame.Rect(550,516,119,59)))
    if s.game.selection_feature.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (550,407), pygame.Rect(550,407,119,59)))
    if s.game.selection_feature.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (550,349), pygame.Rect(550,349,119,59)))

    if s.game.yellow_super_section.status == False:
        dirty_rects.append(screen.blit(bg_gi, (45,541), pygame.Rect(45,541,127,84)))
    if s.game.red_super_section.status == False:
        dirty_rects.append(screen.blit(bg_gi, (45,450), pygame.Rect(45,450,127,84)))
    if s.game.ok.status == False:
        dirty_rects.append(screen.blit(bg_gi, (68,667), pygame.Rect(68,667,45,59)))
        dirty_rects.append(screen.blit(bg_gi, (25,667), pygame.Rect(25,667,45,59)))
    if s.game.magic_screen_feature.position < 7:
        dirty_rects.append(screen.blit(bg_gi, (150,667), pygame.Rect(150,667,45,59)))
        dirty_rects.append(screen.blit(bg_gi, (190,667), pygame.Rect(190,667,45,59)))
        dirty_rects.append(screen.blit(bg_gi, (230,667), pygame.Rect(230,667,45,59)))
        dirty_rects.append(screen.blit(bg_gi, (275,667), pygame.Rect(275,667,45,59)))
    if s.game.magic_screen_feature.position < 8:
        dirty_rects.append(screen.blit(bg_gi, (316,667), pygame.Rect(316,667,45,59)))
    if s.game.magic_screen_feature.position < 9:
        dirty_rects.append(screen.blit(bg_gi, (354,667), pygame.Rect(354,667,45,59)))
    if s.game.magic_screen_feature.position < 10:
        dirty_rects.append(screen.blit(bg_gi, (393,667), pygame.Rect(393,667,45,59)))
    if s.game.three_blue.status == False:
       dirty_rects.append(screen.blit(bg_gi, (48,353), pygame.Rect(48,353,56,94)))
    if s.game.two_blue.status == False:
        dirty_rects.append(screen.blit(bg_gi, (113,353), pygame.Rect(113,353,56,94)))

    pygame.display.update(dirty_rects)


def draw_feature_animation(s, num):
    global screen
    dirty_rects = []
 
    if num in [10,19,35,44]:
        if (s.game.magic_screen_feature.position < 4 and s.game.ok.status == False) and s.game.selection_feature.position not in [7,8]:
            p = [550,572]
            dirty_rects.append(screen.blit(feature, p))
            pygame.display.update(dirty_rects)
            return
    if num in [9,34]:
        if s.game.selection_feature.position != 7:
            p = [550,407]
            dirty_rects.append(screen.blit(feature, p))
            pygame.display.update(dirty_rects)
            return
    if num in [6,17,21,31,42,46]:
        if s.game.selection_feature.position != 8:
            p = [550,349]
            dirty_rects.append(screen.blit(feature, p))
            pygame.display.update(dirty_rects)
            return
    if num in [4,13,29,38]:
        if s.game.red_star.status == False:
            p = [550,461]
            dirty_rects.append(screen.blit(feature, p))
            s.game.coils.redROLamp.pulse(85)
            pygame.display.update(dirty_rects)
            return
    if num in [11,36]:
        if s.game.yellow_star.status == False:
            p = [550,516]
            dirty_rects.append(screen.blit(feature, p))
            s.game.coils.yellowROLamp.pulse(85)
            pygame.display.update(dirty_rects)
            return
    if num in [0,7,25,32]:
        if s.game.yellow_super_section.status == False:
            if s.game.red_super_section.status == False:
                p = [45,541]
                dirty_rects.append(screen.blit(super_section, p))
                pygame.display.update(dirty_rects)
                return
    if num in [18,43]:
        if s.game.red_super_section.status == False:
            if s.game.yellow_super_section.status == False:
                p = [45,450]
                dirty_rects.append(screen.blit(super_section, p))
                pygame.display.update(dirty_rects)
                return
    if num in [23,48]:
        if s.game.ok.status == False:
            p = [68,667]
            dirty_rects.append(screen.blit(ms_letter, p))
            p = [25,667]
            dirty_rects.append(screen.blit(ms_letter, p))
            pygame.display.update(dirty_rects)
            return
    if num in [2,12,27,37]:
        if s.game.magic_screen_feature.position < 7:
            p = [150,667]
            dirty_rects.append(screen.blit(ms_letter, p))
            p = [190,667]
            dirty_rects.append(screen.blit(ms_letter, p))
            p = [230,667]
            dirty_rects.append(screen.blit(ms_letter, p))
            p = [275,667]
            dirty_rects.append(screen.blit(ms_letter, p))
            pygame.display.update(dirty_rects)
            return
    if num in [3,22,28,47]:
        if s.game.magic_screen_feature.position < 8:
            p = [316,667]
            dirty_rects.append(screen.blit(ms_letter, p))
            pygame.display.update(dirty_rects)
            return
    if num in [14,39,25,50]:
        if s.game.magic_screen_feature.position < 9:
            p = [354,667]
            dirty_rects.append(screen.blit(ms_letter, p))
            pygame.display.update(dirty_rects)
            return
    if num in [5,15,30,40]:
        if s.game.magic_screen_feature.position < 10:
            p = [393,667]
            dirty_rects.append(screen.blit(ms_letter, p))
            pygame.display.update(dirty_rects)
            return
    if num in [8,33]:
        if s.game.three_blue.status == False and s.game.two_blue.status == False:
            p = [48,353]
            dirty_rects.append(screen.blit(three_blue, p))
            pygame.display.update(dirty_rects)
            return
    if num in [8,33]:
        if s.game.two_blue.status == False and s.game.three_blue.status == True:
            p = [113,353]
            dirty_rects.append(screen.blit(three_blue, p))
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
