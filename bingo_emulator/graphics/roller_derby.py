
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
bg_menu = pygame.image.load('roller_derby/assets/roller_derby_menu.png').convert()
bg_menu.set_colorkey((255,0,252))
bg_gi = pygame.image.load('roller_derby/assets/roller_derby_gi.png').convert()
bg_gi.set_colorkey((255,0,252))
bg_off = pygame.image.load('roller_derby/assets/roller_derby_off.png').convert()
bg_off.set_colorkey((255,0,252))

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
            if s.game.ball_count.position == 3:
                s.cancel_delayed(name="blink")
                blink([s,1,1])
            else:
                s.cancel_delayed(name="blink")
        elif s.game.selection_feature.position == 7:
            bfp = [551,409]
            screen.blit(time, bfp)
            if s.game.ball_count.position == 4:
                s.cancel_delayed(name="blink")
                blink([s,1,1])
            else:
                s.cancel_delayed(name="blink")
        elif s.game.selection_feature.position == 8:
            bfp = [551,355]
            screen.blit(time, bfp)
            if s.game.ball_count.position == 5:
                s.cancel_delayed(name="blink")
                blink([s,1,1])
            else:
                s.cancel_delayed(name="blink")

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

def blink(args):
    dirty_rects = []
    s = args[0]
    b = args[1]
    sn = args[2]

    if b == 0:
        if sn == 1:
            p = [576,678]
            dirty_rects.append(screen.blit(select_now, p))
        pygame.display.update(dirty_rects)
    else:
        dirty_rects.append(screen.blit(bg_gi, (576,678), pygame.Rect(576,678,121,40)))
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
            bp = [40,340]
            dirty_rects.append(screen.blit(bg_gi, bp, pygame.Rect(bp[0],bp[1],59,74)))
            dirty_rects.append(screen.blit(blue_section, bp))
        elif s.game.two_blue.status == True:
            bp = [102,340]
            dirty_rects.append(screen.blit(bg_gi, bp, pygame.Rect(bp[0],bp[1],59,74)))
            dirty_rects.append(screen.blit(blue_section, bp))

    if s.game.magic_screen_feature.position >= 7 or s.game.ok.status == True:
        if s.game.selection_feature.position < 7:
            bfp = [551,577]
            dirty_rects.append(screen.blit(bg_gi, bfp, pygame.Rect(bfp[0],bfp[1],118,52)))
            dirty_rects.append(screen.blit(time, bfp))
        elif s.game.selection_feature.position == 7:
            bfp = [551,409]
            dirty_rects.append(screen.blit(bg_gi, bfp, pygame.Rect(bfp[0],bfp[1],118,52)))
            screen.blit(time, bfp)
        elif s.game.selection_feature.position == 8:
            bfp = [551,355]
            dirty_rects.append(screen.blit(bg_gi, bfp, pygame.Rect(bfp[0],bfp[1],118,52)))
            screen.blit(time, bfp)
        
    if s.game.selection_feature.position == 1:
        i = [678,590]
        dirty_rects.append(screen.blit(bg_gi, i, pygame.Rect(i[0],i[1],39,29)))
        dirty_rects.append(screen.blit(ti, i))
    if s.game.selection_feature.position == 2 or s.game.selection_feature.position == 3:
        i = [678,530]
        dirty_rects.append(screen.blit(bg_gi, i, pygame.Rect(i[0],i[1],39,29)))
        dirty_rects.append(screen.blit(ti, i))
    if s.game.selection_feature.position == 4 or s.game.selection_feature.position == 5 or s.game.selection_feature.position == 6:
        i = [678,479]
        dirty_rects.append(screen.blit(bg_gi, i, pygame.Rect(i[0],i[1],39,29)))
        dirty_rects.append(screen.blit(ti, i))
    if s.game.selection_feature.position == 7:
        i = [678,426]
        dirty_rects.append(screen.blit(bg_gi, i, pygame.Rect(i[0],i[1],39,29)))
        dirty_rects.append(screen.blit(ti, i))
    if s.game.selection_feature.position == 8:
        i = [678,365]
        dirty_rects.append(screen.blit(bg_gi, i, pygame.Rect(i[0],i[1],39,29)))
        dirty_rects.append(screen.blit(ti, i))

    if s.game.red_star.status == True:
        rs_position = [551,465]
        dirty_rects.append(screen.blit(bg_gi, rs_position, pygame.Rect(rs_position[0],rs_position[1],118,52)))
        dirty_rects.append(screen.blit(time, rs_position))
    if s.game.yellow_star.status == True:
        rs_position = [551,521]
        dirty_rects.append(screen.blit(bg_gi, rs_position, pygame.Rect(rs_position[0],rs_position[1],118,52)))
        dirty_rects.append(screen.blit(time, rs_position))

    if s.game.red_super_section.status == True:
        rss = [37,416]
        dirty_rects.append(screen.blit(bg_gi, rss, pygame.Rect(rss[0],rss[1],122,75)))
        dirty_rects.append(screen.blit(super_section, rss))
    if s.game.yellow_super_section.status == True:
        yss = [37,495]
        dirty_rects.append(screen.blit(bg_gi, yss, pygame.Rect(yss[0],yss[1],122,75)))
        dirty_rects.append(screen.blit(super_section, yss))
    if s.game.orange_section.status == True:
        oss = [37,570]
        dirty_rects.append(screen.blit(bg_gi, oss, pygame.Rect(oss[0],oss[1],122,62)))
        dirty_rects.append(screen.blit(orange_section, oss))

    pygame.display.update(dirty_rects)


def eb_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]

    if s.game.extra_ball.position < 1:
        dirty_rects.append(screen.blit(bg_gi, (140,1027), pygame.Rect(140,1027,50,36)))
    if s.game.extra_ball.position < 2:
        dirty_rects.append(screen.blit(bg_gi, (190,1030), pygame.Rect(190,1030,64,33)))
    if s.game.extra_ball.position < 3:
        dirty_rects.append(screen.blit(bg_gi, (253,1030), pygame.Rect(253,1030,64,33)))
    if s.game.extra_ball.position < 4:
        dirty_rects.append(screen.blit(bg_gi, (322,1028), pygame.Rect(322,1028,50,36)))
    if s.game.extra_ball.position < 5:
        dirty_rects.append(screen.blit(bg_gi, (370,1028), pygame.Rect(370,1028,64,33)))
    if s.game.extra_ball.position < 6:
        dirty_rects.append(screen.blit(bg_gi, (433,1028), pygame.Rect(433,1028,64,33)))
    if s.game.extra_ball.position < 7:
        dirty_rects.append(screen.blit(bg_gi, (500,1027), pygame.Rect(500,1027,50,36)))
    if s.game.extra_ball.position < 8:
        dirty_rects.append(screen.blit(bg_gi, (550,1027), pygame.Rect(550,1027,64,33)))
    if s.game.extra_ball.position < 9:
        dirty_rects.append(screen.blit(bg_gi, (613,1027), pygame.Rect(613,1027,64,33)))
    pygame.display.update(dirty_rects)

    if num in [0,25,14,49]:
        if s.game.extra_ball.position < 1:
            p = [140,1027]
            dirty_rects.append(screen.blit(eb_number, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [39,1,26,15]:
        if s.game.extra_ball.position < 2:
            p = [190,1030]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [3,4,17,28,29,40]:
        if s.game.extra_ball.position < 3:
            p = [253,1030]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [5,18,30,43]:
        if s.game.extra_ball.position < 4:
            p = [322,1028]
            dirty_rects.append(screen.blit(eb_number, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [7,8,19,32,33,44]:
        if s.game.extra_ball.position < 5:
            p = [370,1028]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [9,10,20,34,35,45]:
        if s.game.extra_ball.position < 6:
            p = [433,1028]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [11,21,36,46]:
        if s.game.extra_ball.position < 7:
            p = [500,1027]
            dirty_rects.append(screen.blit(eb_number, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [12,22,37,47]:
        if s.game.extra_ball.position < 8:
            p = [550,1027]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [2,6,13,16,23,27,31,38,41,48]:
        if s.game.extra_ball.position < 9:
            p = [613,1027]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return

def clear_odds(s, num):
    global screen

    dirty_rects = []

    if s.game.yellow_odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (175,845), pygame.Rect(175,845,48,76)))
    if s.game.yellow_odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (239,845), pygame.Rect(239,845,48,76)))
    if s.game.yellow_odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (300,845), pygame.Rect(300,845,48,76)))
    if s.game.yellow_odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (364,845), pygame.Rect(364,845,48,76)))
    if s.game.yellow_odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (418,845), pygame.Rect(418,845,48,76)))
    if s.game.yellow_odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (468,845), pygame.Rect(468,845,48,76)))
    if s.game.yellow_odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (518,845), pygame.Rect(518,845,48,76)))
    if s.game.yellow_odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (566,845), pygame.Rect(566,845,48,76)))

    if s.game.red_odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (175,778), pygame.Rect(175,778,48,76)))
    if s.game.red_odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (239,778), pygame.Rect(239,778,48,76)))
    if s.game.red_odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (300,778), pygame.Rect(300,778,48,76)))
    if s.game.red_odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (364,778), pygame.Rect(364,778,48,76)))
    if s.game.red_odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (418,778), pygame.Rect(418,778,48,76)))
    if s.game.red_odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (468,778), pygame.Rect(468,778,48,76)))
    if s.game.red_odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (518,778), pygame.Rect(518,778,48,76)))
    if s.game.red_odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (566,778), pygame.Rect(566,778,48,76)))

    if s.game.green_odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (175,913), pygame.Rect(175,913,48,76)))
    if s.game.green_odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (239,913), pygame.Rect(239,913,48,76)))
    if s.game.green_odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (300,913), pygame.Rect(300,913,48,76)))
    if s.game.green_odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (364,913), pygame.Rect(364,913,48,76)))
    if s.game.green_odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (418,913), pygame.Rect(418,913,48,76)))
    if s.game.green_odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (468,913), pygame.Rect(468,913,48,76)))
    if s.game.green_odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (518,913), pygame.Rect(518,913,48,76)))
    if s.game.green_odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (566,913), pygame.Rect(566,913,48,76)))

    pygame.display.update(dirty_rects)

def draw_odds_animation(s, num):
    global screen
    dirty_rects = []

    if num in [11,36]:
        if s.game.yellow_odds.position != 1:
            p = [175,845]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [4,29]:
        if s.game.yellow_odds.position != 2:
            p = [239,845]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [7,32]:
        if s.game.yellow_odds.position != 3:
            p = [300,845]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [13,38]:
        if s.game.yellow_odds.position != 4:
            p = [364,845]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [22,47]:
        if s.game.yellow_odds.position != 5:
            p = [418,845]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [17,42]:
        if s.game.yellow_odds.position != 6:
            p = [468,845]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [19,44]:
        if s.game.yellow_odds.position != 7:
            p = [518,845]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [5,30]:
        if s.game.yellow_odds.position != 8:
            p = [566,845]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return

    if num in [0,25]:
        if s.game.red_odds.position != 1:
            p = [175,778]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [15,40]:
        if s.game.red_odds.position != 2:
            p = [239,778]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [24,49]:
        if s.game.red_odds.position != 3:
            p = [300,778]
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
            p = [518,778]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [6,31]:
        if s.game.red_odds.position != 8:
            p = [566,778]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return

    if num in [16,41]:
        if s.game.green_odds.position != 1:
            p = [175,913]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [18,43]:
        if s.game.green_odds.position != 2:
            p = [239,913]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [14,39]:
        if s.game.green_odds.position != 3:
            p = [300,913]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [3,28]:
        if s.game.green_odds.position != 4:
            p = [364,913]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [23,48]:
        if s.game.green_odds.position != 5:
            p = [418,913]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [8,33]:
        if s.game.green_odds.position != 6:
            p = [468,913]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [22,47]:
        if s.game.green_odds.position != 7:
            p = [518,913]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [10,35]:
        if s.game.green_odds.position != 8:
            p = [566,913]
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
        dirty_rects.append(screen.blit(bg_gi, (551,577), pygame.Rect(551,577,118,52)))
    if s.game.red_star.status == False:
        dirty_rects.append(screen.blit(bg_gi, (551,465), pygame.Rect(551,465,118,52)))
    if s.game.yellow_star.status == False:
        dirty_rects.append(screen.blit(bg_gi, (551,521), pygame.Rect(551,521,118,52)))
    if s.game.selection_feature.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (551,409), pygame.Rect(551,409,118,52)))
    if s.game.selection_feature.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (551,355), pygame.Rect(551,355,118,52)))

    if s.game.yellow_super_section.status == False:
        dirty_rects.append(screen.blit(bg_gi, (37,495), pygame.Rect(37,495,122,75)))
    if s.game.red_super_section.status == False:
        dirty_rects.append(screen.blit(bg_gi, (37,416), pygame.Rect(37,416,122,75)))
    if s.game.orange_section.status == False:
        dirty_rects.append(screen.blit(bg_gi, (37,570), pygame.Rect(37,570,122,62)))
    if s.game.ok.status == False:
        dirty_rects.append(screen.blit(bg_gi, (58,672), pygame.Rect(58,672,39,48)))
        dirty_rects.append(screen.blit(bg_gi, (16,672), pygame.Rect(16,672,39,48)))
    if s.game.magic_screen_feature.position < 7:
        dirty_rects.append(screen.blit(bg_gi, (144,674), pygame.Rect(144,674,39,48)))
        dirty_rects.append(screen.blit(bg_gi, (188,672), pygame.Rect(188,672,39,48)))
        dirty_rects.append(screen.blit(bg_gi, (230,672), pygame.Rect(230,672,39,48)))
        dirty_rects.append(screen.blit(bg_gi, (273,672), pygame.Rect(273,672,39,48)))
    if s.game.magic_screen_feature.position < 8:
        dirty_rects.append(screen.blit(bg_gi, (313,672), pygame.Rect(313,672,39,48)))
    if s.game.magic_screen_feature.position < 9:
        dirty_rects.append(screen.blit(bg_gi, (358,672), pygame.Rect(358,672,39,48)))
    if s.game.magic_screen_feature.position < 10:
        dirty_rects.append(screen.blit(bg_gi, (400,672), pygame.Rect(400,672,39,48)))
    if s.game.three_blue.status == False:
       dirty_rects.append(screen.blit(bg_gi, (40,340), pygame.Rect(40,340,59,74)))
    if s.game.two_blue.status == False:
        dirty_rects.append(screen.blit(bg_gi, (102,340), pygame.Rect(102,340,59,74)))

    pygame.display.update(dirty_rects)


def draw_feature_animation(s, num):
    global screen
    dirty_rects = []
 

    if num in [10,35]:
        if (s.game.magic_screen_feature.position < 4 and s.game.ok.status == False) and s.game.selection_feature.position not in [7,8]:
            p = [551,577]
            dirty_rects.append(screen.blit(time, p))
            pygame.display.update(dirty_rects)
            return
    if num in [9,34]:
        if s.game.selection_feature.position != 7:
            p = [551,409]
            dirty_rects.append(screen.blit(time, p))
            pygame.display.update(dirty_rects)
            return
    if num in [6,17,21,31,42,46]:
        if s.game.selection_feature.position != 8:
            p = [551,355]
            dirty_rects.append(screen.blit(time, p))
            pygame.display.update(dirty_rects)
            return
    if num in [4,29]:
        if s.game.red_star.status == False:
            p = [551,465]
            dirty_rects.append(screen.blit(time, p))
            s.game.coils.redROLamp.pulse(85)
            pygame.display.update(dirty_rects)
            return
    if num in [11,36]:
        if s.game.yellow_star.status == False:
            p = [551,521]
            dirty_rects.append(screen.blit(time, p))
            s.game.coils.yellowROLamp.pulse(85)
            pygame.display.update(dirty_rects)
            return
    if num in [7,32]:
        if s.game.yellow_super_section.status == False:
            if s.game.red_super_section.status == False:
                p = [37,495]
                dirty_rects.append(screen.blit(super_section, p))
                pygame.display.update(dirty_rects)
                return
    if num in [18,0,43,25]:
        if s.game.red_super_section.status == False:
            if s.game.yellow_super_section.status == False:
                p = [37,416]
                dirty_rects.append(screen.blit(super_section, p))
                pygame.display.update(dirty_rects)
                return
    if num in [13,19,38,44]:
        if s.game.orange_section.status == False:
            p = [37,570]
            dirty_rects.append(screen.blit(orange_section, p))
            pygame.display.update(dirty_rects)
            return
    
    if num in [16,41,23,48]:
        if s.game.ok.status == False:
            p = [58,672]
            dirty_rects.append(screen.blit(ms_letter, p))
            p = [16,672]
            dirty_rects.append(screen.blit(ms_letter, p))
            pygame.display.update(dirty_rects)
            return
    if num in [2,12,27,37]:
        if s.game.magic_screen_feature.position < 7:
            p = [144,674]
            dirty_rects.append(screen.blit(ms_letter, p))
            p = [188,672]
            dirty_rects.append(screen.blit(ms_letter, p))
            p = [230,672]
            dirty_rects.append(screen.blit(ms_letter, p))
            p = [273,672]
            dirty_rects.append(screen.blit(ms_letter, p))
            pygame.display.update(dirty_rects)
            return
    if num in [3,22,28,47]:
        if s.game.magic_screen_feature.position < 8:
            p = [313,672]
            dirty_rects.append(screen.blit(ms_letter, p))
            pygame.display.update(dirty_rects)
            return
    if num in [1,14,26,39]:
        if s.game.magic_screen_feature.position < 9:
            p = [358,672]
            dirty_rects.append(screen.blit(ms_letter, p))
            pygame.display.update(dirty_rects)
            return
    if num in [5,15,30,40,22,47]:
        if s.game.magic_screen_feature.position < 10:
            p = [400,672]
            dirty_rects.append(screen.blit(ms_letter, p))
            pygame.display.update(dirty_rects)
            return
    if num in [8,20,33,45]:
        if s.game.three_blue.status == False:
            p = [40,340]
            dirty_rects.append(screen.blit(blue_section, p))
            pygame.display.update(dirty_rects)
            return
        else:
            if s.game.two_blue.status == False:
                p = [102,340]
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
