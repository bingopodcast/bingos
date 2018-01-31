
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
bg_gi = pygame.image.load('laguna_beach/assets/laguna_beach_gi.png').convert()
bg_gi.set_colorkey((255,0,252))
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

def eb_animation(num):
    global screen

    if num == 3:
        eb_position = [148,1032]
        screen.blit(eb_number, eb_position)
        pygame.display.update()
    if num == 2:
        eb_position = [196,1032]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 1:
        eb_position = [260,1032]
        screen.blit(eb, eb_position)
        pygame.display.update()


def feature_animation(num):
    global screen
    if num == 4:
        rss = [55,419]
        screen.blit(super_section, rss)
        pygame.display.update()
    else:
        yss = [55,497]
        screen.blit(super_section, yss)
        pygame.display.update()


def odds_animation(num):
    global screen

    if num == 8:
        odds_position = [185,782]
        screen.blit(odds, odds_position)
    if num == 7:
        odds_position = [244,850]
        screen.blit(odds, odds_position)
    if num == 6:
        odds_position = [305,923]
        screen.blit(odds, odds_position)
    if num == 5:
        odds_position = [365,782]
        screen.blit(odds, odds_position)
    if num == 4:
        odds_position = [418,850]
        screen.blit(odds, odds_position)
    if num == 3:
        odds_position = [468,923]
        screen.blit(odds, odds_position)
    if num == 2:
        odds_position = [518,782]
        screen.blit(odds, odds_position)
    if num == 1:
        odds_position = [565,850]
        screen.blit(odd, odds_position)
    pygame.display.update()


