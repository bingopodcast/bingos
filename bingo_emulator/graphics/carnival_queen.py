
import pygame
import random

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

meter = pygame.image.load('graphics/assets/register_cover.png').convert()
magic_screen = pygame.image.load('carnival_queen/assets/magic_screen.png').convert()
number_card = pygame.image.load('carnival_queen/assets/number_card.png').convert()
odds = pygame.image.load('carnival_queen/assets/odds.png').convert_alpha()
eb = pygame.image.load('carnival_queen/assets/eb.png').convert_alpha()
eb_number = pygame.image.load('carnival_queen/assets/eb_number.png').convert_alpha()
extra_balls = pygame.image.load('carnival_queen/assets/extra_balls.png').convert_alpha()
feature = pygame.image.load('carnival_queen/assets/feature.png').convert_alpha()
indicator = pygame.image.load('carnival_queen/assets/indicator.png').convert_alpha()
ms_indicator = pygame.image.load('carnival_queen/assets/ms_indicator.png').convert_alpha()
ms_indicator_arrow = pygame.image.load('carnival_queen/assets/ms_indicator_arrow.png').convert_alpha()
ms_letter = pygame.image.load('carnival_queen/assets/ms_letter.png').convert_alpha()
number = pygame.image.load('carnival_queen/assets/number.png').convert_alpha()
select_now = pygame.image.load('carnival_queen/assets/select_now.png').convert_alpha()
three_blue = pygame.image.load('carnival_queen/assets/three_blue.png').convert_alpha()
two_blue = pygame.image.load('carnival_queen/assets/two_blue.png').convert_alpha()
tilt = pygame.image.load('carnival_queen/assets/tilt.png').convert_alpha()
bg_menu = pygame.image.load('carnival_queen/assets/carnival_queen_menu.png').convert()
bg_menu.set_colorkey((255,0,252))
bg_gi = pygame.image.load('carnival_queen/assets/carnival_queen_gi.png').convert()
bg_gi.set_colorkey((255,0,252))
bg_off = pygame.image.load('carnival_queen/assets/carnival_queen_off.png').convert()
bg_off.set_colorkey((255,0,252))


class scorereel():
    """ Score Reels are used to count replays """
    def __init__(self, pos, image):
        self.position = pos
        self.default_y = self.position[1]
        self.image = pygame.image.load(image).convert()

reel1 = scorereel([92,795], "graphics/assets/white_reel.png")
reel10 = scorereel([74,795], "graphics/assets/white_reel.png")
reel100 = scorereel([54,795], "graphics/assets/white_reel.png")

def display(s, replays=0, menu=False):
    
    meter.set_colorkey((255,0,252))
    meter_position = [45,795]

    screen.blit(reel1.image, reel1.position)
    screen.blit(reel10.image, reel10.position)
    screen.blit(reel100.image, reel100.position)
    screen.blit(meter, meter_position)

    number_card_position = [232,347]

    screen.blit(number_card, number_card_position)

    magic_screen.set_colorkey((255,0,252))
    #default position 230x 350y
    #subtract 53 per position
    #-135x last position on this game
    if s.game.magic_screen.position == 0:
        magic_screen_position = [230,350]
    elif s.game.magic_screen.position == 1:
        magic_screen_position = [177,350]
    elif s.game.magic_screen.position == 2:
        magic_screen_position = [124,350]
    elif s.game.magic_screen.position == 3:
        magic_screen_position = [71,350]
    elif s.game.magic_screen.position == 4:
        magic_screen_position = [21,350]
    elif s.game.magic_screen.position == 5:
        magic_screen_position = [-32,350]
    elif s.game.magic_screen.position == 6:
        magic_screen_position = [-85,350]
    elif s.game.magic_screen.position == 7:
        magic_screen_position = [-135,350]


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

    if s.game.eb_play.status == True:
        eb_position = [40,1019]
        screen.blit(extra_balls, eb_position)

    if s.game.extra_ball.position >= 1:
        eb_position = [150,1022]
        screen.blit(eb_number, eb_position)
    if s.game.extra_ball.position >= 2:
        eb_position = [196,1022]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 3:
        eb_position = [259,1022]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 4:
        eb_position = [331,1024]
        screen.blit(eb_number, eb_position)
    if s.game.extra_ball.position >= 5:
        eb_position = [377,1025]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 6:
        eb_position = [441,1025]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 7:
        eb_position = [511,1021]
        screen.blit(eb_number, eb_position)
    if s.game.extra_ball.position >= 8:
        eb_position = [559,1021]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 9:
        eb_position = [621,1021]
        screen.blit(eb, eb_position)
    

    if s.game.red_star.status == True or s.game.yellow_star.status == True:
        if s.game.before_fourth.status == True:
            rs_position = [561,449]
            screen.blit(feature, rs_position)
            ip = [685,474]
            screen.blit(indicator, ip) 

    if s.game.magic_screen_feature.position >= 7:
        if s.game.before_fourth.status == True:
            bfp = [562,538]
            screen.blit(feature, bfp)
            if s.game.ball_count.position == 3:
                s.cancel_delayed(name="blink")
                blink([s,1,1])
            else:
                s.cancel_delayed(name="blink")
        elif s.game.before_fifth.status == True:
            bfp = [560,356]
            screen.blit(feature, bfp)
            ip = [683,380]
            screen.blit(indicator, ip)
            if s.game.ball_count.position == 4:
                s.cancel_delayed(name="blink")
                blink([s,1,1])
            else:
                s.cancel_delayed(name="blink")

    if s.game.magic_screen_feature.position >= 8:
        if s.game.three_blue.status == True:
            bp = [43,352]
            screen.blit(three_blue, bp)
        elif s.game.two_blue.status == True:
            bp = [0,355]
            screen.blit(two_blue, bp)

    if s.game.red_super_section.status == True:
        rss = [43,444]
        screen.blit(feature, rss)
    if s.game.yellow_super_section.status == True:
        yss = [43,536]
        screen.blit(feature, yss)

    if s.game.magic_screen_feature.position == 1:
        ms = [23,681]
        screen.blit(ms_indicator_arrow, ms)
    if s.game.magic_screen_feature.position == 2:
        ms = [65,681]
        screen.blit(ms_indicator_arrow, ms)
    if s.game.magic_screen_feature.position == 3:
        ms = [108,681]
        screen.blit(ms_indicator_arrow, ms)
    if s.game.magic_screen_feature.position >= 4:
        ms = [157,670]
        screen.blit(ms_letter, ms)
    if s.game.magic_screen_feature.position >= 5:
        ms = [197,670]
        screen.blit(ms_letter, ms)
    if s.game.magic_screen_feature.position >= 6:
        ms = [238,670]
        screen.blit(ms_letter, ms)
    if s.game.magic_screen_feature.position >= 7:
        ms = [281,670]
        screen.blit(ms_letter, ms)
    if s.game.magic_screen_feature.position >= 8:
        ms = [322,670]
        screen.blit(ms_letter, ms)
    if s.game.magic_screen_feature.position >= 9:
        ms = [364,670]
        screen.blit(ms_letter, ms)
    if s.game.magic_screen_feature.position >= 10:
        ms = [406,670]
        screen.blit(ms_letter, ms)

    if s.game.magic_screen.position == 1:
        ms = [163,724]
        screen.blit(ms_indicator, ms)
    if s.game.magic_screen.position == 2:
        ms = [205,724]
        screen.blit(ms_indicator, ms)
    if s.game.magic_screen.position == 3:
        ms = [243,724]
        screen.blit(ms_indicator, ms)
    if s.game.magic_screen.position == 4:
        ms = [285,724]
        screen.blit(ms_indicator, ms)
    if s.game.magic_screen.position == 5:
        ms = [328,724]
        screen.blit(ms_indicator, ms)
    if s.game.magic_screen.position == 6:
        ms = [370,724]
        screen.blit(ms_indicator, ms)
    if s.game.magic_screen.position == 7:
        ms = [411,724]
        screen.blit(ms_indicator, ms)

    if s.game.tilt.status == False:
        if s.holes:
            if 1 in s.holes:
                number_position = [284,365]
                screen.blit(number, number_position)
            if 2 in s.holes:
                number_position = [336,364]
                screen.blit(number, number_position)
            if 3 in s.holes:
                number_position = [390,559]
                screen.blit(number, number_position)
            if 4 in s.holes:
                number_position = [231,414]
                screen.blit(number, number_position)
            if 5 in s.holes:
                number_position = [337,511]
                screen.blit(number, number_position)
            if 6 in s.holes:
                number_position = [230,512]
                screen.blit(number, number_position)
            if 7 in s.holes:
                number_position = [337,414]
                screen.blit(number, number_position)
            if 8 in s.holes:
                number_position = [284,561]
                screen.blit(number, number_position)
            if 9 in s.holes:
                number_position = [230,364]
                screen.blit(number, number_position)
            if 10 in s.holes:
                number_position = [440,559]
                screen.blit(number, number_position)
            if 11 in s.holes:
                number_position = [390,364]
                screen.blit(number, number_position)
            if 12 in s.holes:
                number_position = [231,562]
                screen.blit(number, number_position)
            if 13 in s.holes:
                number_position = [389,461]
                screen.blit(number, number_position)
            if 14 in s.holes:
                number_position = [336,561]
                screen.blit(number, number_position)
            if 15 in s.holes:
                number_position = [441,363]
                screen.blit(number, number_position)
            if 16 in s.holes:
                number_position = [336,461]
                screen.blit(number, number_position)
            if 17 in s.holes:
                number_position = [440,462]
                screen.blit(number, number_position)
            if 18 in s.holes:
                number_position = [441,413]
                screen.blit(number, number_position)
            if 19 in s.holes:
                number_position = [282,413]
                screen.blit(number, number_position)
            if 20 in s.holes:
                number_position = [441,510]
                screen.blit(number, number_position)
            if 21 in s.holes:
                number_position = [389,510]
                screen.blit(number, number_position)
            if 22 in s.holes:
                number_position = [390,413]
                screen.blit(number, number_position)
            if 23 in s.holes:
                number_position = [284,511]
                screen.blit(number, number_position)
            if 24 in s.holes:
                number_position = [284,462]
                screen.blit(number, number_position)
            if 25 in s.holes:
                number_position = [230,462]
                screen.blit(number, number_position)

    if s.game.red_odds.position == 1:
        o = [181,779]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 2:
        o = [247,779]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 3:
        o = [309,779]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 4:
        o = [373,779]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 5:
        o = [428,779]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 6:
        o = [479,779]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 7:
        o = [533,779]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 8:
        o = [579,779]
        screen.blit(odds, o)

    if s.game.yellow_odds.position == 1:
        o = [181,840]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 2:
        o = [247,840]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 3:
        o = [309,840]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 4:
        o = [373,840]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 5:
        o = [428,840]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 6:
        o = [479,840]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 7:
        o = [533,840]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 8:
        o = [579,840]
        screen.blit(odds, o)

    if s.game.green_odds.position == 1:
        o = [181,905]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 2:
        o = [247,905]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 3:
        o = [309,905]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 4:
        o = [373,905]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 5:
        o = [428,905]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 6:
        o = [479,905]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 7:
        o = [533,905]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 8:
        o = [579,905]
        screen.blit(odds, o)


    if s.game.tilt.status == True:
        tilt_position = [47,632]
        screen.blit(tilt, tilt_position)

    pygame.display.update()

def blink(args):
    dirty_rects = []
    s = args[0]
    b = args[1]
    sn = args[2]

    if b == 0:
        if sn == 1:
            p = [578,676]
            dirty_rects.append(screen.blit(select_now, p))
        pygame.display.update(dirty_rects)
    else:
        dirty_rects.append(screen.blit(bg_gi, (578,676), pygame.Rect(578,676,135,42)))
        pygame.display.update(dirty_rects)
    b = not b

    args = [s,b,sn]

    s.delay(name="blink", delay=0.1, handler=blink, param=args)

def eb_animation(num):
    global screen

    if num == 3:
        p = [33,971]
        screen.blit(eb, p)
        pygame.display.update()
    if num == 2:
        p = [64,971]
        screen.blit(eb, p)
        pygame.display.update()
    if num == 1:
        p = [93,971]
        screen.blit(eb, p)
        pygame.display.update()


def feature_animation(num):
    global screen
    if num == 4:
        rs_position = [561,449]
        screen.blit(feature, rs_position)
        pygame.display.update()
    if num == 3:
        ys_position = [43,536]
        screen.blit(feature, ys_position)
        pygame.display.update()


def odds_animation(num):
    global screen
    if num == 8:
        odds_position = [183,789]
        screen.blit(odds, odds_position)
    if num == 7:
        odds_position = [239,816]
        screen.blit(odds, odds_position)
    if num == 6:
        odds_position = [284,787]
        screen.blit(odds, odds_position)
    if num == 5:
        odds_position = [348,822]
        screen.blit(odds, odds_position)
    if num == 4:
        odds_position = [396,790]
        screen.blit(odds, odds_position)
    if num == 3:
        odds_position = [450,788]
        screen.blit(odds, odds_position)
    if num == 2:
        odds_position = [497,844]
        screen.blit(odds, odds_position)
    if num == 1:
        odds_position = [596,818]
        screen.blit(odd, odds_position)
    pygame.display.update()


