
import pygame
import random

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

meter = pygame.image.load('graphics/assets/register_cover.png').convert()
magic_screen = pygame.image.load('laguna_beach/assets/magic_screen.png').convert()
number_card = pygame.image.load('laguna_beach/assets/number_card.png').convert()
odds = pygame.image.load('laguna_beach/assets/odds.png').convert_alpha()
eb = pygame.image.load('laguna_beach/assets/eb.png').convert_alpha()
eb_number = pygame.image.load('laguna_beach/assets/eb_number.png').convert_alpha()
extra_balls = pygame.image.load('laguna_beach/assets/extra_balls.png').convert_alpha()
feature = pygame.image.load('laguna_beach/assets/time.png').convert_alpha()
ms_indicator = pygame.image.load('laguna_beach/assets/ms_indicator.png').convert_alpha()
ti = pygame.image.load('laguna_beach/assets/selection_arrow.png').convert_alpha()
super_section = pygame.image.load('laguna_beach/assets/super_section.png').convert_alpha()
orange_section = pygame.image.load('laguna_beach/assets/orange_section.png').convert_alpha()
ms_letter = pygame.image.load('laguna_beach/assets/ms_letter.png').convert_alpha()
number = pygame.image.load('laguna_beach/assets/number.png').convert_alpha()
select_now = pygame.image.load('laguna_beach/assets/select_now.png').convert_alpha()
three_blue = pygame.image.load('laguna_beach/assets/blue_section.png').convert_alpha()
tilt = pygame.image.load('laguna_beach/assets/tilt.png').convert_alpha()
l = pygame.image.load('laguna_beach/assets/l.png').convert_alpha()
red_l = pygame.image.load('laguna_beach/assets/red_l.png').convert_alpha()
a = pygame.image.load('laguna_beach/assets/a.png').convert_alpha()
red_a = pygame.image.load('laguna_beach/assets/red_a.png').convert_alpha()
g = pygame.image.load('laguna_beach/assets/g.png').convert_alpha()
red_g = pygame.image.load('laguna_beach/assets/red_g.png').convert_alpha()
u = pygame.image.load('laguna_beach/assets/u.png').convert_alpha()
red_u = pygame.image.load('laguna_beach/assets/red_u.png').convert_alpha()
n = pygame.image.load('laguna_beach/assets/n.png').convert_alpha()
red_n = pygame.image.load('laguna_beach/assets/red_n.png').convert_alpha()
a2 = pygame.image.load('laguna_beach/assets/a2.png').convert_alpha()
red_a2 = pygame.image.load('laguna_beach/assets/red_a2.png').convert_alpha()
bg_menu = pygame.image.load('laguna_beach/assets/laguna_beach_menu.png').convert()
bg_menu.set_colorkey((255,0,252))
bg_gi = pygame.image.load('laguna_beach/assets/laguna_beach_gi.png').convert_alpha()
bg_off = pygame.image.load('laguna_beach/assets/laguna_beach_off.png').convert()
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
        rc = [48,264]
        screen.blit(red_l, rc)
    else:
        rc = [48,264]
        screen.blit(l, rc)

    if s.game.green_odds.position == 4:
        ro = [95,261]
        screen.blit(red_a, ro)
    else:
        ro = [95,261]
        screen.blit(a, ro)

    if s.game.green_odds.position == 5:
        ru = [146,259]
        screen.blit(red_g, ru)
    else:
        ru = [148,259]
        screen.blit(g, ru)

    if s.game.green_odds.position == 6:
        rn = [205,261]
        screen.blit(red_u, rn)
    else:
        rn = [205,261]
        screen.blit(u, rn)

    if s.game.green_odds.position == 7:
        rt = [266,261]
        screen.blit(red_n, rt)
    else:
        rt = [266,261]
        screen.blit(n, rt)

    if s.game.green_odds.position == 8:
        ry = [315,263]
        screen.blit(red_a2, ry)
    else:
        ry = [315,263]
        screen.blit(a2, ry)



    if s.game.eb_play.status == True:
        eb_position = [40,1032]
        screen.blit(extra_balls, eb_position)

    if s.game.extra_ball.position >= 1:
        eb_position = [148,1032]
        screen.blit(eb_number, eb_position)
    if s.game.extra_ball.position >= 2:
        eb_position = [196,1032]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 3:
        eb_position = [260,1032]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 4:
        eb_position = [328,1032]
        screen.blit(eb_number, eb_position)
    if s.game.extra_ball.position >= 5:
        eb_position = [376,1032]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 6:
        eb_position = [439,1032]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 7:
        eb_position = [507,1032]
        screen.blit(eb_number, eb_position)
    if s.game.extra_ball.position >= 8:
        eb_position = [555,1032]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 9:
        eb_position = [618,1032]
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
        rs_position = [550,468]
        screen.blit(feature, rs_position)
    if s.game.yellow_star.status == True:
        rs_position = [550,522]
        screen.blit(feature, rs_position)
    if s.game.orange_section.status == True:
        oss = [55,574]
        screen.blit(orange_section, oss)

    if s.game.magic_screen_feature.position >= 7 or s.game.ok.status == True:
        if s.game.selection_feature.position < 7:
            bfp = [550,576]
            screen.blit(feature, bfp)
            if s.game.ball_count.position == 3:
                s.cancel_delayed(name="blink")
                blink([s,1,1])
            else:
                s.cancel_delayed(name="blink")
        elif s.game.selection_feature.position == 7:
            bfp = [550,411]
            screen.blit(feature, bfp)
            if s.game.ball_count.position == 4:
                s.cancel_delayed(name="blink")
                blink([s,1,1])
            else:
                s.cancel_delayed(name="blink")
        elif s.game.selection_feature.position == 8:
            bfp = [550,355]
            screen.blit(feature, bfp)
            if s.game.ball_count.position == 5:
                s.cancel_delayed(name="blink")
                blink([s,1,1])
            else:
                s.cancel_delayed(name="blink")

    if s.game.magic_screen_feature.position >= 9:
        if s.game.three_blue.status == True:
            bp = [55,347]
            screen.blit(three_blue, bp)
        elif s.game.two_blue.status == True:
            bp = [114,347]
            screen.blit(three_blue, bp)

    if s.game.red_super_section.status == True:
        rss = [55,419]
        screen.blit(super_section, rss)
    if s.game.yellow_super_section.status == True:
        yss = [55,497]
        screen.blit(super_section, yss)

    if s.game.magic_screen_feature.position >= 4:
        ms = [154,670]
        screen.blit(ms_letter, ms)
    if s.game.magic_screen_feature.position >= 5:
        ms = [194,670]
        screen.blit(ms_letter, ms)
    if s.game.magic_screen_feature.position >= 6:
        ms = [236,670]
        screen.blit(ms_letter, ms)
    if s.game.magic_screen_feature.position >= 7:
        ms = [279,670]
        screen.blit(ms_letter, ms)
    if s.game.magic_screen_feature.position >= 8:
        ms = [320,670]
        screen.blit(ms_letter, ms)
    if s.game.magic_screen_feature.position >= 9:
        ms = [360,670]
        screen.blit(ms_letter, ms)
    if s.game.magic_screen_feature.position >= 10:
        ms = [402,670]
        screen.blit(ms_letter, ms)

    if s.game.ok.status == True:
        ms = [68,670]
        screen.blit(ms_letter, ms)
        ms = [28,670]
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
        o = [185,782]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 2:
        o = [244,782]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 3:
        o = [305,782]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 4:
        o = [365,782]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 5:
        o = [418,782]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 6:
        o = [468,782]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 7:
        o = [518,782]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 8:
        o = [565,782]
        screen.blit(odds, o)

    if s.game.yellow_odds.position == 1:
        o = [185,850]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 2:
        o = [244,850]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 3:
        o = [305,850]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 4:
        o = [365,850]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 5:
        o = [418,850]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 6:
        o = [468,850]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 7:
        o = [518,850]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 8:
        o = [565,850]
        screen.blit(odds, o)

    if s.game.green_odds.position == 1:
        o = [185,923]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 2:
        o = [244,923]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 3:
        o = [305,923]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 4:
        o = [365,923]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 5:
        o = [418,923]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 6:
        o = [468,923]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 7:
        o = [518,923]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 8:
        o = [565,923]
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
            p = [573,684]
            dirty_rects.append(screen.blit(select_now, p))
        pygame.display.update(dirty_rects)
    else:
        dirty_rects.append(screen.blit(bg_gi, (573,684), pygame.Rect(573,684,121,35)))
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
            bp = [55,347]
            dirty_rects.append(screen.blit(bg_gi, bp, pygame.Rect(bp[0],bp[1],56,70)))
            dirty_rects.append(screen.blit(three_blue, bp))
        elif s.game.two_blue.status == True:
            bp = [114,347]
            dirty_rects.append(screen.blit(bg_gi, bp, pygame.Rect(bp[0],bp[1],56,70)))
            dirty_rects.append(screen.blit(three_blue, bp))

    if s.game.orange_section.status == True:
        oss = [55,574]
        dirty_rects.append(screen.blit(bg_gi, oss, pygame.Rect(oss[0],oss[1],114,60)))
        dirty_rects.append(screen.blit(orange_section, oss))

    if s.game.selection_feature.position == 1:
        i = [672,594]
        dirty_rects.append(screen.blit(bg_gi, i, pygame.Rect(i[0],i[1],32,28)))
        dirty_rects.append(screen.blit(ti, i))
    if s.game.selection_feature.position == 2 or s.game.selection_feature.position == 3:
        i = [672,534]
        dirty_rects.append(screen.blit(bg_gi, i, pygame.Rect(i[0],i[1],32,28)))
        dirty_rects.append(screen.blit(ti, i))
    if s.game.selection_feature.position == 4 or s.game.selection_feature.position == 5 or s.game.selection_feature.position == 6:
        i = [672,482]
        dirty_rects.append(screen.blit(bg_gi, i, pygame.Rect(i[0],i[1],32,28)))
        dirty_rects.append(screen.blit(ti, i))
    if s.game.selection_feature.position == 7:
        i = [672,429]
        dirty_rects.append(screen.blit(bg_gi, i, pygame.Rect(i[0],i[1],32,28)))
        dirty_rects.append(screen.blit(ti, i))
    if s.game.selection_feature.position == 8:
        i = [672,368]
        dirty_rects.append(screen.blit(bg_gi, i, pygame.Rect(i[0],i[1],32,28)))
        dirty_rects.append(screen.blit(ti, i))

    if s.game.selection_feature.position < 7:
        p = [550,576]
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],119,59)))
        dirty_rects.append(screen.blit(feature, p))
    if s.game.red_star.status == True:
        p = [550,468]
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],119,59)))
        dirty_rects.append(screen.blit(feature, p))
    if s.game.yellow_star.status == True:
        p = [550,522]
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],119,59)))
        dirty_rects.append(screen.blit(feature, p))
    if s.game.selection_feature.position == 7:
        p = [550,411]
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],119,59)))
        dirty_rects.append(screen.blit(feature, p))
    if s.game.selection_feature.position == 8:
        p = [550,355]
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],119,59)))
        dirty_rects.append(screen.blit(feature, p))

    if s.game.red_super_section.status == True:
        yss = [55,419]
        dirty_rects.append(screen.blit(bg_gi, yss, pygame.Rect(yss[0],yss[1],114,77)))
        dirty_rects.append(screen.blit(super_section, rss))
    if s.game.yellow_super_section.status == True:
        rss = [55,497]
        dirty_rects.append(screen.blit(bg_gi, rss, pygame.Rect(yss[0],yss[1],114,77)))
        dirty_rects.append(screen.blit(super_section, yss))

    pygame.display.update(dirty_rects)


def eb_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]

    if s.game.extra_ball.position < 1:
        dirty_rects.append(screen.blit(bg_gi, (148,1032), pygame.Rect(148,1032,47,34)))

    if s.game.extra_ball.position < 2:
        dirty_rects.append(screen.blit(bg_gi, (196,1032), pygame.Rect(196,1032,63,35)))
    if s.game.extra_ball.position < 3:
        dirty_rects.append(screen.blit(bg_gi, (260,1032), pygame.Rect(260,1032,63,35)))
    if s.game.extra_ball.position < 4:
        dirty_rects.append(screen.blit(bg_gi, (328,1032), pygame.Rect(328,1032,47,34)))
    if s.game.extra_ball.position < 5:
        dirty_rects.append(screen.blit(bg_gi, (376,1032), pygame.Rect(376,1032,63,35)))
    if s.game.extra_ball.position < 6:
        dirty_rects.append(screen.blit(bg_gi, (439,1032), pygame.Rect(439,1032,63,35)))
    if s.game.extra_ball.position < 7:
        dirty_rects.append(screen.blit(bg_gi, (507,1032), pygame.Rect(507,1032,47,34)))
    if s.game.extra_ball.position < 8:
        dirty_rects.append(screen.blit(bg_gi, (555,1032), pygame.Rect(555,1032,63,35)))
    if s.game.extra_ball.position < 9:
        dirty_rects.append(screen.blit(bg_gi, (618,1032), pygame.Rect(618,1032,63,35)))
    pygame.display.update(dirty_rects)

    if num in [0,25,14,49]:
        if s.game.extra_ball.position < 1:
            p = [148,1032]
            dirty_rects.append(screen.blit(eb_number, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [39,1,26,15]:
        if s.game.extra_ball.position < 2:
            p = [196,1032]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [3,4,17,28,29,40]:
        if s.game.extra_ball.position < 3:
            p = [260,1032]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [5,18,30,43]:
        if s.game.extra_ball.position < 4:
            p = [328,1032]
            dirty_rects.append(screen.blit(eb_number, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [7,8,19,32,33,44]:
        if s.game.extra_ball.position < 5:
            p = [376,1032]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [9,10,20,34,35,45]:
        if s.game.extra_ball.position < 6:
            p = [439,1032]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [11,21,36,46]:
        if s.game.extra_ball.position < 7:
            p = [507,1032]
            dirty_rects.append(screen.blit(eb_number, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [12,22,37,47]:
        if s.game.extra_ball.position < 8:
            p = [555,1032]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [2,6,13,16,23,27,31,38,41,48]:
        if s.game.extra_ball.position < 9:
            p = [618,1032]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return

def clear_odds(s, num):
    global screen

    dirty_rects = []

    if s.game.yellow_odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (185,850), pygame.Rect(185,850,45,60)))
    if s.game.yellow_odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (244,850), pygame.Rect(244,850,45,60)))
    if s.game.yellow_odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (305,850), pygame.Rect(305,850,45,60)))
    if s.game.yellow_odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (365,850), pygame.Rect(365,850,45,60)))
    if s.game.yellow_odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (418,850), pygame.Rect(418,850,45,60)))
    if s.game.yellow_odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (468,850), pygame.Rect(468,850,45,60)))
    if s.game.yellow_odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (518,850), pygame.Rect(518,850,45,60)))
    if s.game.yellow_odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (565,850), pygame.Rect(565,850,45,60)))


    if s.game.red_odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (185,782), pygame.Rect(185,782,45,60)))
    if s.game.red_odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (244,782), pygame.Rect(244,782,45,60)))
    if s.game.red_odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (305,782), pygame.Rect(305,782,45,60)))
    if s.game.red_odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (365,782), pygame.Rect(365,782,45,60)))
    if s.game.red_odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (418,782), pygame.Rect(418,782,45,60)))
    if s.game.red_odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (468,782), pygame.Rect(468,782,45,60)))
    if s.game.red_odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (518,782), pygame.Rect(518,782,45,60)))
    if s.game.red_odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (565,782), pygame.Rect(565,782,45,60)))

    if s.game.green_odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (185,923), pygame.Rect(185,923,45,60)))
    if s.game.green_odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (244,923), pygame.Rect(244,923,45,60)))
    if s.game.green_odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (305,923), pygame.Rect(305,923,45,60)))
    if s.game.green_odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (365,923), pygame.Rect(365,923,45,60)))
    if s.game.green_odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (418,923), pygame.Rect(418,923,45,60)))
    if s.game.green_odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (468,923), pygame.Rect(468,923,45,60)))
    if s.game.green_odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (518,923), pygame.Rect(518,923,45,60)))
    if s.game.green_odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (565,923), pygame.Rect(565,923,45,60)))

    pygame.display.update(dirty_rects)

def draw_odds_animation(s, num):
    global screen
    dirty_rects = []

    if num in [11,36]:
        if s.game.yellow_odds.position != 1:
            p = [185,850]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [4,29]:
        if s.game.yellow_odds.position != 2:
            p = [244,850]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [7,32]:
        if s.game.yellow_odds.position != 3:
            p = [305,850]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [13,38]:
        if s.game.yellow_odds.position != 4:
            p = [365,850]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [22,47]:
        if s.game.yellow_odds.position != 5:
            p = [418,850]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [17,42]:
        if s.game.yellow_odds.position != 6:
            p = [468,850]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [19,44]:
        if s.game.yellow_odds.position != 7:
            p = [518,850]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [5,30]:
        if s.game.yellow_odds.position != 8:
            p = [565,850]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return

    if num in [0,25]:
        if s.game.red_odds.position != 1:
            p = [185,782]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [15,40]:
        if s.game.red_odds.position != 2:
            p = [244,782]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [24,49]:
        if s.game.red_odds.position != 3:
            p = [305,782]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [9,34]:
        if s.game.red_odds.position != 4:
            p = [365,782]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [20,45]:
        if s.game.red_odds.position != 5:
            p = [418,782]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [12,37]:
        if s.game.red_odds.position != 6:
            p = [468,782]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [50,26]:
        if s.game.red_odds.position != 7:
            p = [518,782]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [6,31]:
        if s.game.red_odds.position != 8:
            p = [565,782]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return

    if num in [16,41]:
        if s.game.green_odds.position != 1:
            p = [185,923]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [18,43]:
        if s.game.green_odds.position != 2:
            p = [244,923]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [14,39]:
        if s.game.green_odds.position != 3:
            p = [305,923]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [3,28]:
        if s.game.green_odds.position != 4:
            p = [365,923]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [23,48]:
        if s.game.green_odds.position != 5:
            p = [418,923]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [8,33]:
        if s.game.green_odds.position != 6:
            p = [468,923]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [22,47]:
        if s.game.green_odds.position != 7:
            p = [518,923]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [10,35]:
        if s.game.green_odds.position != 8:
            p = [565,923]
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
        dirty_rects.append(screen.blit(bg_gi, (550,576), pygame.Rect(550,576,119,59)))
    if s.game.red_star.status == False:
        dirty_rects.append(screen.blit(bg_gi, (550,468), pygame.Rect(550,468,119,59)))
    if s.game.yellow_star.status == False:
        dirty_rects.append(screen.blit(bg_gi, (550,522), pygame.Rect(550,522,119,59)))
    if s.game.selection_feature.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (550,411), pygame.Rect(550,411,119,59)))
    if s.game.selection_feature.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (553,362), pygame.Rect(553,362,118,52)))

    if s.game.yellow_super_section.status == False:
        dirty_rects.append(screen.blit(bg_gi, (55,497), pygame.Rect(55,497,114,77)))
    if s.game.red_super_section.status == False:
        dirty_rects.append(screen.blit(bg_gi, (55,419), pygame.Rect(55,419,114,77)))
    if s.game.orange_section.status == False:
        dirty_rects.append(screen.blit(bg_gi, (55,574), pygame.Rect(55,574,114,60)))
    if s.game.ok.status == False:
        dirty_rects.append(screen.blit(bg_gi, (68,670), pygame.Rect(68,670,37,50)))
        dirty_rects.append(screen.blit(bg_gi, (28,670), pygame.Rect(28,670,37,50)))
    if s.game.magic_screen_feature.position < 7:
        dirty_rects.append(screen.blit(bg_gi, (154,670), pygame.Rect(154,670,37,50)))
        dirty_rects.append(screen.blit(bg_gi, (194,670), pygame.Rect(194,670,37,50)))
        dirty_rects.append(screen.blit(bg_gi, (236,670), pygame.Rect(236,670,37,50)))
        dirty_rects.append(screen.blit(bg_gi, (279,670), pygame.Rect(279,670,37,50)))
    if s.game.magic_screen_feature.position < 8:
        dirty_rects.append(screen.blit(bg_gi, (324,672), pygame.Rect(324,672,39,48)))
    if s.game.magic_screen_feature.position < 9:
        dirty_rects.append(screen.blit(bg_gi, (364,672), pygame.Rect(364,672,39,48)))
        if s.game.three_blue.status == False:
           dirty_rects.append(screen.blit(bg_gi, (52,350), pygame.Rect(52,350,56,70)))
    if s.game.magic_screen_feature.position < 10:
        dirty_rects.append(screen.blit(bg_gi, (405,672), pygame.Rect(405,672,39,48)))
    if s.game.two_blue.status == False:
        dirty_rects.append(screen.blit(bg_gi, (114,347), pygame.Rect(114,347,56,70)))

    pygame.display.update(dirty_rects)


def draw_feature_animation(s, num):
    global screen
    dirty_rects = []
 
    if num in [10,35]:
        if (s.game.magic_screen_feature.position < 4 and s.game.ok.status == False) and s.game.selection_feature.position not in [7,8]:
            p = [550,576]
            dirty_rects.append(screen.blit(feature, p))
            pygame.display.update(dirty_rects)
            return
    if num in [9,34]:
        if s.game.selection_feature.position != 7:
            p = [550,411]
            dirty_rects.append(screen.blit(feature, p))
            pygame.display.update(dirty_rects)
            return
    if num in [6,17,21,31,42,46]:
        if s.game.selection_feature.position != 8:
            p = [553,362]
            dirty_rects.append(screen.blit(feature, p))
            pygame.display.update(dirty_rects)
            return
    if num in [4,29]:
        if s.game.red_star.status == False:
            p = [550,468]
            dirty_rects.append(screen.blit(feature, p))
            s.game.coils.redROLamp.pulse(85)
            pygame.display.update(dirty_rects)
            return
    if num in [11,36]:
        if s.game.yellow_star.status == False:
            p = [550,522]
            dirty_rects.append(screen.blit(feature, p))
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
                p = [55,419]
                dirty_rects.append(screen.blit(super_section, p))
                pygame.display.update(dirty_rects)
                return
    if num in [13,19,38,44]:
        if s.game.orange_section.status == False:
            p = [55,574]
            dirty_rects.append(screen.blit(orange_section, p))
            pygame.display.update(dirty_rects)
            return
    if num in [16,23,41,48]:
        if s.game.ok.status == False:
            p = [68,670]
            dirty_rects.append(screen.blit(ms_letter, p))
            p = [28,670]
            dirty_rects.append(screen.blit(ms_letter, p))
            pygame.display.update(dirty_rects)
            return
    if num in [2,12,27,37]:
        if s.game.magic_screen_feature.position < 7:
            p = [154,670]
            dirty_rects.append(screen.blit(ms_letter, p))
            p = [194,670]
            dirty_rects.append(screen.blit(ms_letter, p))
            p = [236,670]
            dirty_rects.append(screen.blit(ms_letter, p))
            p = [279,670]
            dirty_rects.append(screen.blit(ms_letter, p))
            pygame.display.update(dirty_rects)
            return
    if num in [3,22,28,47]:
        if s.game.magic_screen_feature.position < 8:
            p = [324,672]
            dirty_rects.append(screen.blit(ms_letter, p))
            pygame.display.update(dirty_rects)
            return
    if num in [14,25,39,50]:
        if s.game.magic_screen_feature.position < 9:
            p = [364,672]
            dirty_rects.append(screen.blit(ms_letter, p))
            if s.game.three_blue.status == False:
                p = [52,350]
                dirty_rects.append(screen.blit(three_blue, p))
            pygame.display.update(dirty_rects)
            return
    if num in [5,15,30,40]:
        if s.game.magic_screen_feature.position < 10:
            p = [405,672]
            dirty_rects.append(screen.blit(ms_letter, p))
            pygame.display.update(dirty_rects)
            return
    if num in [8,20,33,45]:
        if s.game.two_blue.status == False:
            p = [114,347]
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
