
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
bg_menu = pygame.image.load('circus_queen/assets/circus_queen_menu.png').convert()
bg_menu.set_colorkey((255,0,252))
bg_gi = pygame.image.load('circus_queen/assets/circus_queen_gi.png').convert_alpha()
bg_off = pygame.image.load('circus_queen/assets/circus_queen_off.png').convert()
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
        magic_screen_position = [-45,358]
    elif s.game.magic_screen.position == 7:
        magic_screen_position = [-92,358]
    elif s.game.magic_screen.position == 8:
        magic_screen_position = [-139,358]
    elif s.game.magic_screen.position == 9:
        magic_screen_position = [-187,358]


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
            if s.game.ball_count.position == 3:
                s.cancel_delayed(name="blink")
                blink([s,1,1])
            else:
                s.cancel_delayed(name="blink")
        elif s.game.selection_feature.position == 7:
            bfp = [552,417]
            screen.blit(time, bfp)
            if s.game.ball_count.position == 4:
                s.cancel_delayed(name="blink")
                blink([s,1,1])
            else:
                s.cancel_delayed(name="blink")
        elif s.game.selection_feature.position == 8:
            bfp = [553,362]
            screen.blit(time, bfp)
            if s.game.ball_count.position == 5:
                s.cancel_delayed(name="blink")
                blink([s,1,1])
            else:
                s.cancel_delayed(name="blink")

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

def blink(args):
    dirty_rects = []
    s = args[0]
    b = args[1]
    sn = args[2]

    if b == 0:
        if sn == 1:
            p = [575,675]
            dirty_rects.append(screen.blit(select_now, p))
        pygame.display.update(dirty_rects)
    else:
        dirty_rects.append(screen.blit(bg_gi, (575,675), pygame.Rect(575,675,135,42)))
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
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],660,270)))
    else:
        dirty_rects.append(screen.blit(bg_off, p, pygame.Rect(p[0],p[1],660,270)))
    
    if s.game.magic_screen_feature.position >= 9:
        if s.game.three_blue.status == True:
            bp = [52,350]
            dirty_rects.append(screen.blit(bg_gi, bp, pygame.Rect(bp[0],bp[1],42,71)))
            dirty_rects.append(screen.blit(blue_section, bp))
        elif s.game.three_blue_six.status == True:
            bp = [95,349]
            dirty_rects.append(screen.blit(bg_gi, bp, pygame.Rect(bp[0],bp[1],42,71)))
            dirty_rects.append(screen.blit(blue_section, bp))
        elif s.game.two_blue.status == True:
            bp = [139,350]
            dirty_rects.append(screen.blit(bg_gi, bp, pygame.Rect(bp[0],bp[1],42,71)))
            dirty_rects.append(screen.blit(blue_section, bp))

    if s.game.magic_screen_feature.position >= 7 or s.game.ok.status == True:
        if s.game.selection_feature.position < 7:
            bfp = [552,580]
            dirty_rects.append(screen.blit(bg_gi, bfp, pygame.Rect(bfp[0],bfp[1],118,52)))
            dirty_rects.append(screen.blit(time, bfp))
        elif s.game.selection_feature.position == 7:
            bfp = [552,417]
            dirty_rects.append(screen.blit(bg_gi, bfp, pygame.Rect(bfp[0],bfp[1],118,52)))
            screen.blit(time, bfp)
        elif s.game.selection_feature.position == 8:
            bfp = [553,362]
            dirty_rects.append(screen.blit(bg_gi, bfp, pygame.Rect(bfp[0],bfp[1],118,52)))
            screen.blit(time, bfp)
        
    if s.game.selection_feature.position == 1:
        i = [672,594]
        dirty_rects.append(screen.blit(bg_gi, i, pygame.Rect(i[0],i[1],39,29)))
        dirty_rects.append(screen.blit(ti, i))
    if s.game.selection_feature.position == 2 or s.game.selection_feature.position == 3:
        i = [672,534]
        dirty_rects.append(screen.blit(bg_gi, i, pygame.Rect(i[0],i[1],39,29)))
        dirty_rects.append(screen.blit(ti, i))
    if s.game.selection_feature.position == 4 or s.game.selection_feature.position == 5 or s.game.selection_feature.position == 6:
        i = [672,482]
        dirty_rects.append(screen.blit(bg_gi, i, pygame.Rect(i[0],i[1],39,29)))
        dirty_rects.append(screen.blit(ti, i))
    if s.game.selection_feature.position == 7:
        i = [672,429]
        dirty_rects.append(screen.blit(bg_gi, i, pygame.Rect(i[0],i[1],39,29)))
        dirty_rects.append(screen.blit(ti, i))
    if s.game.selection_feature.position == 8:
        i = [672,368]
        dirty_rects.append(screen.blit(bg_gi, i, pygame.Rect(i[0],i[1],39,29)))
        dirty_rects.append(screen.blit(ti, i))

    if s.game.red_star.status == True:
        rs_position = [552,473]
        dirty_rects.append(screen.blit(bg_gi, rs_position, pygame.Rect(rs_position[0],rs_position[1],118,52)))
        dirty_rects.append(screen.blit(time, rs_position))
    if s.game.yellow_star.status == True:
        rs_position = [552,527]
        dirty_rects.append(screen.blit(bg_gi, rs_position, pygame.Rect(rs_position[0],rs_position[1],118,52)))
        dirty_rects.append(screen.blit(time, rs_position))

    if s.game.red_super_section.status == True:
        rss = [55,422]
        dirty_rects.append(screen.blit(bg_gi, rss, pygame.Rect(rss[0],rss[1],122,75)))
        dirty_rects.append(screen.blit(super_section, rss))
    if s.game.yellow_super_section.status == True:
        yss = [55,497]
        dirty_rects.append(screen.blit(bg_gi, yss, pygame.Rect(yss[0],yss[1],122,75)))
        dirty_rects.append(screen.blit(super_section, yss))
    if s.game.orange_section.status == True:
        oss = [55,572]
        dirty_rects.append(screen.blit(bg_gi, oss, pygame.Rect(oss[0],oss[1],122,62)))
        dirty_rects.append(screen.blit(orange_section, oss))

    pygame.display.update(dirty_rects)


def eb_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]

    if s.game.extra_ball.position < 1:
        dirty_rects.append(screen.blit(bg_gi, (151,1026), pygame.Rect(151,1026,45,31)))
    if s.game.extra_ball.position < 2:
        dirty_rects.append(screen.blit(bg_gi, (198,1025), pygame.Rect(198,1025,61,34)))
    if s.game.extra_ball.position < 3:
        dirty_rects.append(screen.blit(bg_gi, (263,1025), pygame.Rect(263,1025,61,34)))
    if s.game.extra_ball.position < 4:
        dirty_rects.append(screen.blit(bg_gi, (329,1025), pygame.Rect(329,1025,45,31)))
    if s.game.extra_ball.position < 5:
        dirty_rects.append(screen.blit(bg_gi, (375,1025), pygame.Rect(375,1025,61,34)))
    if s.game.extra_ball.position < 6:
        dirty_rects.append(screen.blit(bg_gi, (439,1025), pygame.Rect(439,1025,61,34)))
    if s.game.extra_ball.position < 7:
        dirty_rects.append(screen.blit(bg_gi, (506,1025), pygame.Rect(506,1025,45,31)))
    if s.game.extra_ball.position < 8:
        dirty_rects.append(screen.blit(bg_gi, (556,1025), pygame.Rect(556,1025,61,34)))
    if s.game.extra_ball.position < 9:
        dirty_rects.append(screen.blit(bg_gi, (617,1025), pygame.Rect(617,1025,61,34)))
    pygame.display.update(dirty_rects)

    if num in [0,25,14,49]:
        if s.game.extra_ball.position < 1:
            p = [151,1026]
            dirty_rects.append(screen.blit(eb_number, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [39,1,26,15]:
        if s.game.extra_ball.position < 2:
            p = [198,1025]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [3,4,17,28,29,40]:
        if s.game.extra_ball.position < 3:
            p = [263,1025]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [5,18,30,43]:
        if s.game.extra_ball.position < 4:
            p = [329,1025]
            dirty_rects.append(screen.blit(eb_number, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [7,8,19,32,33,44]:
        if s.game.extra_ball.position < 5:
            p = [375,1025]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [9,10,20,34,35,45]:
        if s.game.extra_ball.position < 6:
            p = [439,1025]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [11,21,36,46]:
        if s.game.extra_ball.position < 7:
            p = [506,1025]
            dirty_rects.append(screen.blit(eb_number, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [12,22,37,47]:
        if s.game.extra_ball.position < 8:
            p = [556,1025]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [2,6,13,16,23,27,31,38,41,48]:
        if s.game.extra_ball.position < 9:
            p = [617,1025]
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


    if s.game.selection_feature.position < 7 and (s.game.magic_screen_feature.position < 4 and s.game.ok.status == False):
        dirty_rects.append(screen.blit(bg_gi, (552,580), pygame.Rect(552,580,118,52)))
    if s.game.red_star.status == False:
        dirty_rects.append(screen.blit(bg_gi, (552,473), pygame.Rect(552,473,118,52)))
    if s.game.yellow_star.status == False:
        dirty_rects.append(screen.blit(bg_gi, (552,527), pygame.Rect(552,527,118,52)))
    if s.game.selection_feature.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (552,417), pygame.Rect(552,417,118,52)))
    if s.game.selection_feature.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (553,362), pygame.Rect(553,362,118,52)))

    if s.game.yellow_super_section.status == False:
        dirty_rects.append(screen.blit(bg_gi, (55,497), pygame.Rect(55,497,122,75)))
    if s.game.red_super_section.status == False:
        dirty_rects.append(screen.blit(bg_gi, (55,422), pygame.Rect(55,422,122,75)))
    if s.game.orange_section.status == False:
        dirty_rects.append(screen.blit(bg_gi, (55,572), pygame.Rect(55,572,122,62)))
    if s.game.ok.status == False:
        dirty_rects.append(screen.blit(bg_gi, (76,672), pygame.Rect(76,672,39,48)))
        dirty_rects.append(screen.blit(bg_gi, (34,672), pygame.Rect(34,672,39,48)))
    if s.game.magic_screen_feature.position < 7:
        dirty_rects.append(screen.blit(bg_gi, (162,672), pygame.Rect(162,672,39,48)))
        dirty_rects.append(screen.blit(bg_gi, (202,672), pygame.Rect(202,672,39,48)))
        dirty_rects.append(screen.blit(bg_gi, (243,672), pygame.Rect(243,672,39,48)))
        dirty_rects.append(screen.blit(bg_gi, (283,672), pygame.Rect(283,672,39,48)))
    if s.game.magic_screen_feature.position < 8:
        dirty_rects.append(screen.blit(bg_gi, (324,672), pygame.Rect(324,672,39,48)))
    if s.game.magic_screen_feature.position < 9:
        dirty_rects.append(screen.blit(bg_gi, (364,672), pygame.Rect(364,672,39,48)))
    if s.game.magic_screen_feature.position < 10:
        dirty_rects.append(screen.blit(bg_gi, (405,672), pygame.Rect(405,672,39,48)))
    if s.game.three_blue.status == False:
       dirty_rects.append(screen.blit(bg_gi, (52,350), pygame.Rect(52,350,42,71)))
    if s.game.three_blue_six.status == False:
       dirty_rects.append(screen.blit(bg_gi, (95,349), pygame.Rect(95,349,42,71)))
    if s.game.two_blue.status == False:
        dirty_rects.append(screen.blit(bg_gi, (139,350), pygame.Rect(139,350,42,71)))

    pygame.display.update(dirty_rects)


def draw_feature_animation(s, num):
    global screen
    dirty_rects = []
 
    if num in [10,35]:
        if (s.game.magic_screen_feature.position < 4 and s.game.ok.status == False) and s.game.selection_feature.position not in [7,8]:
            p = [552,580]
            dirty_rects.append(screen.blit(time, p))
            pygame.display.update(dirty_rects)
            return
    if num in [9,34]:
        if s.game.selection_feature.position != 7:
            p = [552,417]
            dirty_rects.append(screen.blit(time, p))
            pygame.display.update(dirty_rects)
            return
    if num in [6,17,21,31,42,46]:
        if s.game.selection_feature.position != 8:
            p = [553,362]
            dirty_rects.append(screen.blit(time, p))
            pygame.display.update(dirty_rects)
            return
    if num in [4,29]:
        if s.game.red_star.status == False:
            p = [552,473]
            dirty_rects.append(screen.blit(time, p))
            s.game.coils.redROLamp.pulse(85)
            pygame.display.update(dirty_rects)
            return
    if num in [11,36]:
        if s.game.yellow_star.status == False:
            p = [552,527]
            dirty_rects.append(screen.blit(time, p))
            s.game.coils.yellowROLamp.pulse(85)
            pygame.display.update(dirty_rects)
            return
    if num in [7,32]:
        if s.game.yellow_super_section.status == False:
            if s.game.red_super_section.status == False:
                p = [55,497]
                dirty_rects.append(screen.blit(super_section, p))
                pygame.display.update(dirty_rects)
                return
    if num in [18,0,43,25]:
        if s.game.red_super_section.status == False:
            if s.game.yellow_super_section.status == False:
                p = [55,422]
                dirty_rects.append(screen.blit(super_section, p))
                pygame.display.update(dirty_rects)
                return
    if num in [13,19,38,44]:
        if s.game.orange_section.status == False:
            p = [55,572]
            dirty_rects.append(screen.blit(orange_section, p))
            pygame.display.update(dirty_rects)
            return
    if num in [16,41]:
        if s.game.ok.status == False:
            p = [76,672]
            dirty_rects.append(screen.blit(ms_letter, p))
            p = [34,672]
            dirty_rects.append(screen.blit(ms_letter, p))
            pygame.display.update(dirty_rects)
            return
    if num in [2,12,27,37]:
        if s.game.magic_screen_feature.position < 7:
            p = [162,672]
            dirty_rects.append(screen.blit(ms_letter, p))
            p = [202,672]
            dirty_rects.append(screen.blit(ms_letter, p))
            p = [243,672]
            dirty_rects.append(screen.blit(ms_letter, p))
            p = [283,672]
            dirty_rects.append(screen.blit(ms_letter, p))
            pygame.display.update(dirty_rects)
            return
    if num in [3,22,28,47]:
        if s.game.magic_screen_feature.position < 8:
            p = [324,672]
            dirty_rects.append(screen.blit(ms_letter, p))
            pygame.display.update(dirty_rects)
            return
    if num in [1,14,26,39]:
        if s.game.magic_screen_feature.position < 9:
            p = [364,672]
            dirty_rects.append(screen.blit(ms_letter, p))
            pygame.display.update(dirty_rects)
            return
    if num in [5,15,30,40]:
        if s.game.magic_screen_feature.position < 10:
            p = [405,672]
            dirty_rects.append(screen.blit(ms_letter, p))
            pygame.display.update(dirty_rects)
            return
    if num in [8,33]:
        if s.game.three_blue.status == False:
            p = [52,350]
            dirty_rects.append(screen.blit(blue_section, p))
            pygame.display.update(dirty_rects)
            return
        else:
            p = [95,349]
            dirty_rects.append(screen.blit(blue_section, p))
            pygame.display.update(dirty_rects)
            return
    if num in [20,45]:
        if s.game.two_blue.status == False:
            p = [139,350]
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
