
import pygame
import random

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

meter = pygame.image.load('graphics/assets/black_register_cover.png').convert()
magic_screen = pygame.image.load('malibu_beach/assets/magic_screen.png').convert()
number_card = pygame.image.load('malibu_beach/assets/number_card.png').convert()
odds = pygame.image.load('malibu_beach/assets/odds.png').convert_alpha()
eb = pygame.image.load('malibu_beach/assets/eb.png').convert_alpha()
eb_number = pygame.image.load('malibu_beach/assets/eb_number.png').convert_alpha()
extra_balls = pygame.image.load('malibu_beach/assets/extra_balls.png').convert_alpha()
feature = pygame.image.load('malibu_beach/assets/time.png').convert_alpha()
ms_indicator = pygame.image.load('malibu_beach/assets/ms_indicator.png').convert_alpha()
ti = pygame.image.load('malibu_beach/assets/selection_arrow.png').convert_alpha()
super_section = pygame.image.load('malibu_beach/assets/super_section.png').convert_alpha()
orange_section = pygame.image.load('malibu_beach/assets/orange_section.png').convert_alpha()
ms_letter = pygame.image.load('malibu_beach/assets/ms_letter.png').convert_alpha()
number = pygame.image.load('malibu_beach/assets/number.png').convert_alpha()
select_now = pygame.image.load('malibu_beach/assets/select_now.png').convert_alpha()
three_blue = pygame.image.load('malibu_beach/assets/blue_section.png').convert_alpha()
tilt = pygame.image.load('malibu_beach/assets/tilt.png').convert_alpha()
m = pygame.image.load('malibu_beach/assets/m.png').convert_alpha()
red_m = pygame.image.load('malibu_beach/assets/red_m.png').convert_alpha()
a = pygame.image.load('malibu_beach/assets/a.png').convert_alpha()
red_a = pygame.image.load('malibu_beach/assets/red_a.png').convert_alpha()
l = pygame.image.load('malibu_beach/assets/l.png').convert_alpha()
red_l = pygame.image.load('malibu_beach/assets/red_l.png').convert_alpha()
i_letter = pygame.image.load('malibu_beach/assets/i.png').convert_alpha()
red_i = pygame.image.load('malibu_beach/assets/red_i.png').convert_alpha()
b = pygame.image.load('malibu_beach/assets/b.png').convert_alpha()
red_b = pygame.image.load('malibu_beach/assets/red_b.png').convert_alpha()
u = pygame.image.load('malibu_beach/assets/u.png').convert_alpha()
red_u = pygame.image.load('malibu_beach/assets/red_u.png').convert_alpha()
bg_menu = pygame.image.load('malibu_beach/assets/malibu_beach_menu.png').convert()
bg_menu.set_colorkey((255,0,252))
bg_gi = pygame.image.load('malibu_beach/assets/malibu_beach_gi.png').convert_alpha()
bg_off = pygame.image.load('malibu_beach/assets/malibu_beach_off.png').convert()
bg_off.set_colorkey((255,0,252))

class scorereel():
    """ Score Reels are used to count replays """
    def __init__(self, pos, image):
        self.position = pos
        self.default_y = self.position[1]
        self.image = pygame.image.load(image).convert()

reel1 = scorereel([106,837], "graphics/assets/white_reel.png")
reel10 = scorereel([88,837], "graphics/assets/white_reel.png")
reel100 = scorereel([69,837], "graphics/assets/white_reel.png")
reel1000 = scorereel([50,837], "graphics/assets/white_reel.png")

def display(s, replays=0, menu=False):
    
    meter.set_colorkey((255,0,252))
    meter_position = [40,837]

    screen.blit(reel1.image, reel1.position)
    screen.blit(reel10.image, reel10.position)
    screen.blit(reel100.image, reel100.position)
    screen.blit(reel1000.image, reel1000.position)
    screen.blit(meter, meter_position)

    number_card_position = [235,343]

    screen.blit(number_card, number_card_position)

    magic_screen.set_colorkey((255,0,252))
    #default position 230x 359y
    #subtract 47 per position
    if s.game.magic_screen.position == 0:
        magic_screen_position = [240,338]
    elif s.game.magic_screen.position == 1:
        magic_screen_position = [192,338]
    elif s.game.magic_screen.position == 2:
        magic_screen_position = [145,338]
    elif s.game.magic_screen.position == 3:
        magic_screen_position = [96,338]
    elif s.game.magic_screen.position == 4:
        magic_screen_position = [49,338]
    elif s.game.magic_screen.position == 5:
        magic_screen_position = [3,338]
    elif s.game.magic_screen.position == 6:
        magic_screen_position = [-42,338]
    elif s.game.magic_screen.position == 7:
        magic_screen_position = [-89,338]
    elif s.game.magic_screen.position == 8:
        magic_screen_position = [-136,338]
    elif s.game.magic_screen.position == 9:
        magic_screen_position = [-183,338]


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
        rc = [4,164]
        screen.blit(red_m, rc)
    else:
        rc = [4,164]
        screen.blit(m, rc)

    if s.game.green_odds.position == 4:
        ro = [98,150]
        screen.blit(red_a, ro)
    else:
        ro = [98,150]
        screen.blit(a, ro)

    if s.game.green_odds.position == 5:
        ru = [158,153]
        screen.blit(red_l, ru)
    else:
        ru = [158,153]
        screen.blit(l, ru)

    if s.game.green_odds.position == 6:
        rn = [215,159]
        screen.blit(red_i, rn)
    else:
        rn = [215,159]
        screen.blit(i_letter, rn)

    if s.game.green_odds.position == 7:
        rt = [250,170]
        screen.blit(red_b, rt)
    else:
        rt = [250,170]
        screen.blit(b, rt)

    if s.game.green_odds.position == 8:
        ry = [305,186]
        screen.blit(red_u, ry)
    else:
        ry = [305,186]
        screen.blit(u, ry)



    if s.game.eb_play.status == True:
        eb_position = [36,1077]
        screen.blit(extra_balls, eb_position)

    if s.game.extra_ball.position >= 1:
        eb_position = [146,1077]
        screen.blit(eb_number, eb_position)
    if s.game.extra_ball.position >= 2:
        eb_position = [200,1077]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 3:
        eb_position = [260,1077]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 4:
        eb_position = [321,1077]
        screen.blit(eb_number, eb_position)
    if s.game.extra_ball.position >= 5:
        eb_position = [376,1077]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 6:
        eb_position = [439,1077]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 7:
        eb_position = [501,1077]
        screen.blit(eb_number, eb_position)
    if s.game.extra_ball.position >= 8:
        eb_position = [555,1077]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 9:
        eb_position = [618,1077]
        screen.blit(eb, eb_position)
    

    if s.game.selection_feature.position == 1:
        i = [684,570]
        screen.blit(ti, i)
    if s.game.selection_feature.position == 2 or s.game.selection_feature.position == 3:
        i = [684,504]
        screen.blit(ti, i)
    if s.game.selection_feature.position == 4 or s.game.selection_feature.position == 5 or s.game.selection_feature.position == 6:
        i = [684,438]
        screen.blit(ti, i)
    if s.game.selection_feature.position == 7:
        i = [684,375]
        screen.blit(ti, i)
    if s.game.selection_feature.position == 8:
        i = [684,308]
        screen.blit(ti, i)

    if s.game.red_star.status == True:
        rs_position = [557,421]
        screen.blit(feature, rs_position)
    if s.game.yellow_star.status == True:
        rs_position = [557,486]
        screen.blit(feature, rs_position)
    if s.game.orange_section.status == True:
        oss = [38,583]
        screen.blit(orange_section, oss)

    if s.game.magic_screen_feature.position >= 7 or s.game.ok.status == True:
        if s.game.selection_feature.position < 7:
            bfp = [557,552]
            screen.blit(feature, bfp)
            if s.game.ball_count.position == 3:
                s.cancel_delayed(name="blink")
                blink([s,1,1])
            else:
                s.cancel_delayed(name="blink")
        elif s.game.selection_feature.position == 7:
            bfp = [557,356]
            screen.blit(feature, bfp)
            if s.game.ball_count.position == 4:
                s.cancel_delayed(name="blink")
                blink([s,1,1])
            else:
                s.cancel_delayed(name="blink")
        elif s.game.selection_feature.position == 8:
            bfp = [557,291]
            screen.blit(feature, bfp)
            if s.game.ball_count.position == 5:
                s.cancel_delayed(name="blink")
                blink([s,1,1])
            else:
                s.cancel_delayed(name="blink")

    if s.game.magic_screen_feature.position >= 9:
        if s.game.three_blue.status == True:
            bp = [43,319]
            screen.blit(three_blue, bp)
        elif s.game.two_blue.status == True:
            bp = [104,319]
            screen.blit(three_blue, bp)

    if s.game.red_super_section.status == True:
        rss = [40,405]
        screen.blit(super_section, rss)
    if s.game.yellow_super_section.status == True:
        yss = [40,495]
        screen.blit(super_section, yss)

    if s.game.magic_screen_feature.position >= 4:
        ms = [145,678]
        screen.blit(ms_letter, ms)
    if s.game.magic_screen_feature.position >= 5:
        ms = [188,678]
        screen.blit(ms_letter, ms)
    if s.game.magic_screen_feature.position >= 6:
        ms = [232,678]
        screen.blit(ms_letter, ms)
    if s.game.magic_screen_feature.position >= 7:
        ms = [275,678]
        screen.blit(ms_letter, ms)
    if s.game.magic_screen_feature.position >= 8:
        ms = [319,678]
        screen.blit(ms_letter, ms)
    if s.game.magic_screen_feature.position >= 9:
        ms = [362,678]
        screen.blit(ms_letter, ms)
    if s.game.magic_screen_feature.position >= 10:
        ms = [405,678]
        screen.blit(ms_letter, ms)

    if s.game.ok.status == True:
        ms = [58,678]
        screen.blit(ms_letter, ms)
        ms = [16,678]
        screen.blit(ms_letter, ms)


    if s.game.magic_screen.position == 0:
        ms = [20,745]
        screen.blit(ms_indicator, ms)
    if s.game.magic_screen.position == 1:
        ms = [62,745]
        screen.blit(ms_indicator, ms)
    if s.game.magic_screen.position == 3:
        ms = [150,745]
        screen.blit(ms_indicator, ms)
    if s.game.magic_screen.position == 4:
        ms = [195,745]
        screen.blit(ms_indicator, ms)
    if s.game.magic_screen.position == 5:
        ms = [238,745]
        screen.blit(ms_indicator, ms)
    if s.game.magic_screen.position == 6:
        ms = [280,745]
        screen.blit(ms_indicator, ms)
    if s.game.magic_screen.position == 7:
        ms = [323,745]
        screen.blit(ms_indicator, ms)
    if s.game.magic_screen.position == 8:
        ms = [368,745]
        screen.blit(ms_indicator, ms)
    if s.game.magic_screen.position == 9:
        ms = [410,745]
        screen.blit(ms_indicator, ms)

    if s.game.tilt.status == False:
        if s.holes:
            if 1 in s.holes:
                number_position = [287,353]
                screen.blit(number, number_position)
            if 2 in s.holes:
                number_position = [333,353]
                screen.blit(number, number_position)
            if 3 in s.holes:
                number_position = [382,548]
                screen.blit(number, number_position)
            if 4 in s.holes:
                number_position = [238,403]
                screen.blit(number, number_position)
            if 5 in s.holes:
                number_position = [335,500]
                screen.blit(number, number_position)
            if 6 in s.holes:
                number_position = [238,500]
                screen.blit(number, number_position)
            if 7 in s.holes:
                number_position = [333,403]
                screen.blit(number, number_position)
            if 8 in s.holes:
                number_position = [286,548]
                screen.blit(number, number_position)
            if 9 in s.holes:
                number_position = [240,354]
                screen.blit(number, number_position)
            if 10 in s.holes:
                number_position = [430,545]
                screen.blit(number, number_position)
            if 11 in s.holes:
                number_position = [382,353]
                screen.blit(number, number_position)
            if 12 in s.holes:
                number_position = [238,548]
                screen.blit(number, number_position)
            if 13 in s.holes:
                number_position = [382,450]
                screen.blit(number, number_position)
            if 14 in s.holes:
                number_position = [334,549]
                screen.blit(number, number_position)
            if 15 in s.holes:
                number_position = [428,353]
                screen.blit(number, number_position)
            if 16 in s.holes:
                number_position = [334,450]
                screen.blit(number, number_position)
            if 17 in s.holes:
                number_position = [428,450]
                screen.blit(number, number_position)
            if 18 in s.holes:
                number_position = [428,403]
                screen.blit(number, number_position)
            if 19 in s.holes:
                number_position = [285,401]
                screen.blit(number, number_position)
            if 20 in s.holes:
                number_position = [430,500]
                screen.blit(number, number_position)
            if 21 in s.holes:
                number_position = [382,500]
                screen.blit(number, number_position)
            if 22 in s.holes:
                number_position = [382,401]
                screen.blit(number, number_position)
            if 23 in s.holes:
                number_position = [286,500]
                screen.blit(number, number_position)
            if 24 in s.holes:
                number_position = [286,450]
                screen.blit(number, number_position)
            if 25 in s.holes:
                number_position = [240,450]
                screen.blit(number, number_position)

    if s.game.red_odds.position == 1:
        o = [195,865]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 2:
        o = [264,865]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 3:
        o = [339,865]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 4:
        o = [408,865]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 5:
        o = [470,865]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 6:
        o = [530,865]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 7:
        o = [578,865]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 8:
        o = [628,865]
        screen.blit(odds, o)

    if s.game.yellow_odds.position == 1:
        o = [195,937]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 2:
        o = [264,937]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 3:
        o = [339,937]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 4:
        o = [408,937]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 5:
        o = [470,937]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 6:
        o = [530,937]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 7:
        o = [578,937]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 8:
        o = [628,937]
        screen.blit(odds, o)

    if s.game.green_odds.position == 1:
        o = [195,1008]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 2:
        o = [264,1008]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 3:
        o = [339,1008]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 4:
        o = [408,1008]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 5:
        o = [470,1008]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 6:
        o = [530,1008]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 7:
        o = [578,1008]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 8:
        o = [628,1008]
        screen.blit(odds, o)


    if s.game.tilt.status == True:
        tilt_position = [572,640]
        screen.blit(tilt, tilt_position)

    pygame.display.update()

def blink(args):
    dirty_rects = []
    s = args[0]
    b = args[1]
    sn = args[2]

    if b == 0:
        if sn == 1:
            p = [583,700]
            dirty_rects.append(screen.blit(select_now, p))
        pygame.display.update(dirty_rects)
    else:
        dirty_rects.append(screen.blit(bg_gi, (583,700), pygame.Rect(583,700,116,35)))
        pygame.display.update(dirty_rects)
    b = not b

    args = [s,b,sn]

    s.delay(name="blink", delay=0.1, handler=blink, param=args)

def screen_animation(args):
    dirty_rects = []
    s = args[0]
    num = args[1]
    direction = args[2]
    
    number_card_position = [235,343]

    dirty_rects.append(screen.blit(number_card, number_card_position))

    magic_screen.set_colorkey((255,0,252))

    if s.game.magic_screen.position == 0:
        p = [240,338]
    elif s.game.magic_screen.position == 1:
        p = [192,338]
    elif s.game.magic_screen.position == 2:
        p = [145,338]
    elif s.game.magic_screen.position == 3:
        p = [96,338]
    elif s.game.magic_screen.position == 4:
        p = [49,338]
    elif s.game.magic_screen.position == 5:
        p = [3,338]
    elif s.game.magic_screen.position == 6:
        p = [-42,338]
    elif s.game.magic_screen.position == 7:
        p = [-89,338]
    elif s.game.magic_screen.position == 8:
        p = [-136,338]
    elif s.game.magic_screen.position == 9:
        p = [-183,338]

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
            bp = [43,319]
            dirty_rects.append(screen.blit(bg_gi, bp, pygame.Rect(bp[0],bp[1],60,76)))
            dirty_rects.append(screen.blit(three_blue, bp))
        elif s.game.two_blue.status == True:
            bp = [104,319]
            dirty_rects.append(screen.blit(bg_gi, bp, pygame.Rect(bp[0],bp[1],60,76)))
            dirty_rects.append(screen.blit(three_blue, bp))

    if s.game.orange_section.status == True:
        oss = [38,583]
        dirty_rects.append(screen.blit(bg_gi, oss, pygame.Rect(oss[0],oss[1],127,65)))
        dirty_rects.append(screen.blit(orange_section, oss))

    if s.game.selection_feature.position == 1:
        i = [684,570]
        dirty_rects.append(screen.blit(bg_gi, i, pygame.Rect(i[0],i[1],32,28)))
        dirty_rects.append(screen.blit(ti, i))
    if s.game.selection_feature.position == 2 or s.game.selection_feature.position == 3:
        i = [684,504]
        dirty_rects.append(screen.blit(bg_gi, i, pygame.Rect(i[0],i[1],32,28)))
        dirty_rects.append(screen.blit(ti, i))
    if s.game.selection_feature.position == 4 or s.game.selection_feature.position == 5 or s.game.selection_feature.position == 6:
        i = [684,438]
        dirty_rects.append(screen.blit(bg_gi, i, pygame.Rect(i[0],i[1],32,28)))
        dirty_rects.append(screen.blit(ti, i))
    if s.game.selection_feature.position == 7:
        i = [684,375]
        dirty_rects.append(screen.blit(bg_gi, i, pygame.Rect(i[0],i[1],32,28)))
        dirty_rects.append(screen.blit(ti, i))
    if s.game.selection_feature.position == 8:
        i = [684,308]
        dirty_rects.append(screen.blit(bg_gi, i, pygame.Rect(i[0],i[1],32,28)))
        dirty_rects.append(screen.blit(ti, i))


    if s.game.selection_feature.position < 7:
        p = [557,552]
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],122,63)))
        dirty_rects.append(screen.blit(feature, p))
    if s.game.red_star.status == True:
        p = [557,421]
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],122,63)))
        dirty_rects.append(screen.blit(feature, p))
    if s.game.yellow_star.status == True:
        p = [557,486]
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],122,63)))
        dirty_rects.append(screen.blit(feature, p))
    if s.game.selection_feature.position == 7:
        p = [557,356]
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],122,63)))
        dirty_rects.append(screen.blit(feature, p))
    if s.game.selection_feature.position == 8:
        p = [557,291]
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],122,63)))
        dirty_rects.append(screen.blit(feature, p))

    if s.game.red_super_section.status == True:
        yss = [40,405]
        dirty_rects.append(screen.blit(bg_gi, yss, pygame.Rect(yss[0],yss[1],125,81)))
        dirty_rects.append(screen.blit(super_section, rss))
    if s.game.yellow_super_section.status == True:
        rss = [40,495]
        dirty_rects.append(screen.blit(bg_gi, rss, pygame.Rect(yss[0],yss[1],125,81)))
        dirty_rects.append(screen.blit(super_section, yss))

    pygame.display.update(dirty_rects)



def eb_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]

    if s.game.extra_ball.position < 1:
        dirty_rects.append(screen.blit(bg_gi, (146,1077), pygame.Rect(146,1077,55,42)))

    if s.game.extra_ball.position < 2:
        dirty_rects.append(screen.blit(bg_gi, (200,1077), pygame.Rect(200,1077,63,38)))
    if s.game.extra_ball.position < 3:
        dirty_rects.append(screen.blit(bg_gi, (260,1077), pygame.Rect(260,1077,63,38)))
    if s.game.extra_ball.position < 4:
        dirty_rects.append(screen.blit(bg_gi, (321,1077), pygame.Rect(321,1077,55,42)))
    if s.game.extra_ball.position < 5:
        dirty_rects.append(screen.blit(bg_gi, (376,1077), pygame.Rect(376,1077,63,38)))
    if s.game.extra_ball.position < 6:
        dirty_rects.append(screen.blit(bg_gi, (439,1077), pygame.Rect(439,1077,63,38)))
    if s.game.extra_ball.position < 7:
        dirty_rects.append(screen.blit(bg_gi, (501,1077), pygame.Rect(501,1077,55,42)))
    if s.game.extra_ball.position < 8:
        dirty_rects.append(screen.blit(bg_gi, (555,1077), pygame.Rect(555,1077,63,38)))
    if s.game.extra_ball.position < 9:
        dirty_rects.append(screen.blit(bg_gi, (618,1077), pygame.Rect(618,1077,63,38)))
    pygame.display.update(dirty_rects)

    if num in [0,25,14,49]:
        if s.game.extra_ball.position < 1:
            p = [146,1077]
            dirty_rects.append(screen.blit(eb_number, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [39,1,26,15]:
        if s.game.extra_ball.position < 2:
            p = [200,1077]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [3,4,17,28,29,40]:
        if s.game.extra_ball.position < 3:
            p = [260,1077]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [5,18,30,43]:
        if s.game.extra_ball.position < 4:
            p = [321,1077]
            dirty_rects.append(screen.blit(eb_number, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [7,8,19,32,33,44]:
        if s.game.extra_ball.position < 5:
            p = [376,1077]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [9,10,20,34,35,45]:
        if s.game.extra_ball.position < 6:
            p = [439,1077]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [11,21,36,46]:
        if s.game.extra_ball.position < 7:
            p = [501,1077]
            dirty_rects.append(screen.blit(eb_number, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [12,22,37,47]:
        if s.game.extra_ball.position < 8:
            p = [555,1077]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [2,6,13,16,23,27,31,38,41,48]:
        if s.game.extra_ball.position < 9:
            p = [618,1077]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return

def clear_odds(s, num):
    global screen

    dirty_rects = []

    if s.game.yellow_odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (195,937), pygame.Rect(195,937,58,74)))
    if s.game.yellow_odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (264,937), pygame.Rect(264,937,58,74)))
    if s.game.yellow_odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (339,937), pygame.Rect(339,937,58,74)))
    if s.game.yellow_odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (408,937), pygame.Rect(408,937,58,74)))
    if s.game.yellow_odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (470,937), pygame.Rect(470,937,58,74)))
    if s.game.yellow_odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (530,937), pygame.Rect(530,937,58,74)))
    if s.game.yellow_odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (578,937), pygame.Rect(578,937,58,74)))
    if s.game.yellow_odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (628,937), pygame.Rect(628,937,58,74)))


    if s.game.red_odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (195,865), pygame.Rect(195,865,58,74)))
    if s.game.red_odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (264,865), pygame.Rect(264,865,58,74)))
    if s.game.red_odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (339,865), pygame.Rect(339,865,58,74)))
    if s.game.red_odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (408,865), pygame.Rect(408,865,58,74)))
    if s.game.red_odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (470,865), pygame.Rect(470,865,58,74)))
    if s.game.red_odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (530,865), pygame.Rect(530,865,58,74)))
    if s.game.red_odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (578,865), pygame.Rect(578,865,58,74)))
    if s.game.red_odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (628,865), pygame.Rect(628,865,58,74)))

    if s.game.green_odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (195,1008), pygame.Rect(195,1008,58,74)))
    if s.game.green_odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (264,1008), pygame.Rect(264,1008,58,74)))
    if s.game.green_odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (339,1008), pygame.Rect(339,1008,58,74)))
    if s.game.green_odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (408,1008), pygame.Rect(408,1008,58,74)))
    if s.game.green_odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (470,1008), pygame.Rect(470,1008,58,74)))
    if s.game.green_odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (530,1008), pygame.Rect(530,1008,58,74)))
    if s.game.green_odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (578,1008), pygame.Rect(578,1008,58,74)))
    if s.game.green_odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (628,1008), pygame.Rect(628,1008,58,74)))

    pygame.display.update(dirty_rects)

def draw_odds_animation(s, num):
    global screen
    dirty_rects = []

    if num in [11,36]:
        if s.game.yellow_odds.position != 1:
            p = [195,937]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [4,29]:
        if s.game.yellow_odds.position != 2:
            p = [264,937]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [7,32]:
        if s.game.yellow_odds.position != 3:
            p = [339,937]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [13,38]:
        if s.game.yellow_odds.position != 4:
            p = [408,937]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [22,47]:
        if s.game.yellow_odds.position != 5:
            p = [470,937]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [17,42]:
        if s.game.yellow_odds.position != 6:
            p = [530,937]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [19,44]:
        if s.game.yellow_odds.position != 7:
            p = [578,937]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [5,30]:
        if s.game.yellow_odds.position != 8:
            p = [628,937]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return

    if num in [0,25]:
        if s.game.red_odds.position != 1:
            p = [195,865]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [15,40]:
        if s.game.red_odds.position != 2:
            p = [264,865]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [24,49]:
        if s.game.red_odds.position != 3:
            p = [339,865]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [9,34]:
        if s.game.red_odds.position != 4:
            p = [408,865]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [20,45]:
        if s.game.red_odds.position != 5:
            p = [470,865]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [12,37]:
        if s.game.red_odds.position != 6:
            p = [530,865]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [50,26]:
        if s.game.red_odds.position != 7:
            p = [578,865]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [6,31]:
        if s.game.red_odds.position != 8:
            p = [628,865]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return

    if num in [16,41]:
        if s.game.green_odds.position != 1:
            p = [195,1008]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [18,43]:
        if s.game.green_odds.position != 2:
            p = [264,1008]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [14,39]:
        if s.game.green_odds.position != 3:
            p = [339,1008]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [3,28]:
        if s.game.green_odds.position != 4:
            p = [408,1008]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [23,48]:
        if s.game.green_odds.position != 5:
            p = [470,1008]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [8,33]:
        if s.game.green_odds.position != 6:
            p = [530,1008]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [22,47]:
        if s.game.green_odds.position != 7:
            p = [578,1008]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [10,35]:
        if s.game.green_odds.position != 8:
            p = [628,1008]
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
        dirty_rects.append(screen.blit(bg_gi, (557,552), pygame.Rect(557,552,122,63)))
    if s.game.red_star.status == False:
        dirty_rects.append(screen.blit(bg_gi, (557,421), pygame.Rect(557,421,122,63)))
    if s.game.yellow_star.status == False:
        dirty_rects.append(screen.blit(bg_gi, (557,486), pygame.Rect(557,486,122,63)))
    if s.game.selection_feature.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (557,356), pygame.Rect(557,356,122,63)))
    if s.game.selection_feature.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (557,291), pygame.Rect(557,291,122,63)))

    if s.game.yellow_super_section.status == False:
        dirty_rects.append(screen.blit(bg_gi, (40,495), pygame.Rect(40,495,125,81)))
    if s.game.red_super_section.status == False:
        dirty_rects.append(screen.blit(bg_gi, (40,405), pygame.Rect(40,405,125,81)))
    if s.game.orange_section.status == False:
        dirty_rects.append(screen.blit(bg_gi, (38,583), pygame.Rect(38,583,127,65)))
    if s.game.ok.status == False:
        dirty_rects.append(screen.blit(bg_gi, (58,678), pygame.Rect(58,678,43,66)))
        dirty_rects.append(screen.blit(bg_gi, (16,678), pygame.Rect(16,678,43,66)))

    if s.game.magic_screen_feature.position < 7:
        dirty_rects.append(screen.blit(bg_gi, (145,678), pygame.Rect(145,678,43,66)))
        dirty_rects.append(screen.blit(bg_gi, (188,678), pygame.Rect(188,678,43,66)))
        dirty_rects.append(screen.blit(bg_gi, (232,678), pygame.Rect(232,678,43,66)))
        dirty_rects.append(screen.blit(bg_gi, (275,678), pygame.Rect(275,678,43,66)))
    if s.game.magic_screen_feature.position < 8:
        dirty_rects.append(screen.blit(bg_gi, (319,678), pygame.Rect(319,678,43,66)))
    if s.game.magic_screen_feature.position < 9:
        dirty_rects.append(screen.blit(bg_gi, (362,678), pygame.Rect(362,678,43,66)))
        if s.game.three_blue.status == False:
           dirty_rects.append(screen.blit(bg_gi, (43,319), pygame.Rect(43,319,60,76)))
    if s.game.magic_screen_feature.position < 10:
        dirty_rects.append(screen.blit(bg_gi, (405,678), pygame.Rect(405,678,43,66)))
    if s.game.two_blue.status == False:
        dirty_rects.append(screen.blit(bg_gi, (104,319), pygame.Rect(104,319,60,76)))

    pygame.display.update(dirty_rects)


def draw_feature_animation(s, num):
    global screen
    dirty_rects = []
 
    if num in [10,35]:
        if (s.game.magic_screen_feature.position < 4 and s.game.ok.status == False) and s.game.selection_feature.position not in [7,8]:
            p = [557,552]
            dirty_rects.append(screen.blit(feature, p))
            pygame.display.update(dirty_rects)
            return
    if num in [9,34]:
        if s.game.selection_feature.position != 7:
            p = [557,356]
            dirty_rects.append(screen.blit(feature, p))
            pygame.display.update(dirty_rects)
            return
    if num in [6,17,21,31,42,46]:
        if s.game.selection_feature.position != 8:
            p = [557,291]
            dirty_rects.append(screen.blit(feature, p))
            pygame.display.update(dirty_rects)
            return
    if num in [4,29]:
        if s.game.red_star.status == False:
            p = [557,421]
            dirty_rects.append(screen.blit(feature, p))
            s.game.coils.redROLamp.pulse(85)
            pygame.display.update(dirty_rects)
            return
    if num in [11,36]:
        if s.game.yellow_star.status == False:
            p = [557,486]
            dirty_rects.append(screen.blit(feature, p))
            s.game.coils.yellowROLamp.pulse(85)
            pygame.display.update(dirty_rects)
            return
    if num in [7,32]:
        if s.game.yellow_super_section.status == False:
            if s.game.red_super_section.status == False:
                p = [40,495]
                dirty_rects.append(screen.blit(super_section, p))
                pygame.display.update(dirty_rects)
                return
    if num in [18,0,43,25]:
        if s.game.red_super_section.status == False:
            if s.game.yellow_super_section.status == False:
                p = [40,405]
                dirty_rects.append(screen.blit(super_section, p))
                pygame.display.update(dirty_rects)
                return
    if num in [13,19,38,44]:
        if s.game.orange_section.status == False:
            p = [38,583]
            dirty_rects.append(screen.blit(orange_section, p))
            pygame.display.update(dirty_rects)
            return
    if num in [16,23,41,48]:
        if s.game.ok.status == False:
            p = [58,678]
            dirty_rects.append(screen.blit(ms_letter, p))
            p = [16,678]
            dirty_rects.append(screen.blit(ms_letter, p))
            pygame.display.update(dirty_rects)
            return
    if num in [2,12,27,37]:
        if s.game.magic_screen_feature.position < 7:
            p = [145,678]
            dirty_rects.append(screen.blit(ms_letter, p))
            p = [188,678]
            dirty_rects.append(screen.blit(ms_letter, p))
            p = [232,678]
            dirty_rects.append(screen.blit(ms_letter, p))
            p = [275,678]
            dirty_rects.append(screen.blit(ms_letter, p))
            pygame.display.update(dirty_rects)
            return
    if num in [3,22,28,47]:
        if s.game.magic_screen_feature.position < 8:
            p = [319,678]
            dirty_rects.append(screen.blit(ms_letter, p))
            pygame.display.update(dirty_rects)
            return
    if num in [14,25,39,50]:
        if s.game.magic_screen_feature.position < 9:
            p = [362,678]
            dirty_rects.append(screen.blit(ms_letter, p))
            if s.game.three_blue.status == False:
                p = [43,319]
                dirty_rects.append(screen.blit(three_blue, p))
            pygame.display.update(dirty_rects)
            return
    if num in [5,15,30,40]:
        if s.game.magic_screen_feature.position < 10:
            p = [405,678]
            dirty_rects.append(screen.blit(ms_letter, p))
            pygame.display.update(dirty_rects)
            return
    if num in [8,20,33,45]:
        if s.game.two_blue.status == False:
            p = [104,319]
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
