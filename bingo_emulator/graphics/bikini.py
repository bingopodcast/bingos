
import pygame
import random

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

meter = pygame.image.load('graphics/assets/register_cover.png').convert()
magic_screen = pygame.image.load('bikini/assets/magic_screen.png').convert()
number_card = pygame.image.load('bikini/assets/number_card.png').convert()
odds = pygame.image.load('bikini/assets/odds.png').convert_alpha()
eb = pygame.image.load('bikini/assets/eb.png').convert_alpha()
eb_number = pygame.image.load('bikini/assets/eb_number.png').convert_alpha()
extra_balls = pygame.image.load('bikini/assets/extra_balls.png').convert_alpha()
time = pygame.image.load('bikini/assets/time.png').convert_alpha()
ms_indicator = pygame.image.load('bikini/assets/ms_indicator.png').convert_alpha()
ti = pygame.image.load('bikini/assets/time_indicator.png').convert_alpha()
super_section = pygame.image.load('bikini/assets/super_section.png').convert_alpha()
orange_section = pygame.image.load('bikini/assets/orange_section.png').convert_alpha()
ms_letter = pygame.image.load('bikini/assets/ms_letter.png').convert_alpha()
number = pygame.image.load('bikini/assets/number.png').convert_alpha()
select_now = pygame.image.load('bikini/assets/select_now.png').convert_alpha()
blue_section = pygame.image.load('bikini/assets/blue_section.png').convert_alpha()
tilt = pygame.image.load('bikini/assets/tilt.png').convert_alpha()
button = pygame.image.load('bikini/assets/button.png').convert_alpha()
futurity = pygame.image.load('bikini/assets/futurity.png').convert_alpha()

class scorereel():
    """ Score Reels are used to count replays """
    def __init__(self, pos, image):
        self.position = pos
        self.default_y = self.position[1]
        self.image = pygame.image.load(image).convert()

reel1 = scorereel([102,805], "graphics/assets/white_reel.png")
reel10 = scorereel([83,805], "graphics/assets/white_reel.png")
reel100 = scorereel([64,805], "graphics/assets/white_reel.png")

def display(s, replays=0, menu=False):
    
    meter.set_colorkey((255,0,252))
    meter_position = [55,805]

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
        backglass = pygame.image.load('bikini/assets/bikini_menu.png').convert_alpha()
    else:
        if (s.game.anti_cheat.status == True):
            backglass = pygame.image.load('bikini/assets/bikini_gi.png').convert_alpha()
        else:
            backglass = pygame.image.load('bikini/assets/bikini_off.png').convert_alpha()
    backglass = pygame.transform.scale(backglass, (720, 1280))
    
    screen.blit(backglass, backglass_position)


    if s.game.eb_play.status == True:
        eb_position = [37,1053]
        screen.blit(extra_balls, eb_position)

    if s.game.extra_ball.position >= 1:
        eb_position = [151,1051]
        screen.blit(eb_number, eb_position)
    if s.game.extra_ball.position >= 2:
        eb_position = [198,1051]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 3:
        eb_position = [263,1051]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 4:
        eb_position = [329,1051]
        screen.blit(eb_number, eb_position)
    if s.game.extra_ball.position >= 5:
        eb_position = [375,1051]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 6:
        eb_position = [439,1051]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 7:
        eb_position = [506,1051]
        screen.blit(eb_number, eb_position)
    if s.game.extra_ball.position >= 8:
        eb_position = [556,1051]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 9:
        eb_position = [617,1051]
        screen.blit(eb, eb_position)
    

    if s.game.selection_feature.position == 1:
        i = [672,594]
        screen.blit(ti, i)
    if s.game.selection_feature.position == 2 or s.game.selection_feature.position == 3:
        i = [672,534]
        screen.blit(ti, i)
    if s.game.selection_feature.position == 4 or s.game.selection_feature.position == 5 or s.game.selection_feature.position == 6:
        i = [672,474]
        screen.blit(ti, i)
    if s.game.selection_feature.position == 7:
        i = [672,417]
        screen.blit(ti, i)
    if s.game.selection_feature.position == 8:
        i = [672,355]
        screen.blit(ti, i)

    if s.game.red_star.status == True:
        rs_position = [552,458]
        screen.blit(time, rs_position)
    if s.game.yellow_star.status == True:
        rs_position = [552,518]
        screen.blit(time, rs_position)

    if s.game.magic_screen_feature.position >= 7 or s.game.ok.status == True:
        if s.game.selection_feature.position < 7:
            bfp = [552,575]
            screen.blit(time, bfp)
        elif s.game.selection_feature.position == 7:
            bfp = [552,400]
            screen.blit(time, bfp)
        elif s.game.selection_feature.position == 8:
            bfp = [553,340]
            screen.blit(time, bfp)

    if s.game.magic_screen_feature.position >= 9:
        if s.game.three_blue.status == True:
            bp = [45,330]
            screen.blit(blue_section, bp)
        elif s.game.three_blue_six.status == True:
            bp = [88,330]
            screen.blit(blue_section, bp)
        elif s.game.two_blue.status == True:
            bp = [133,330]
            screen.blit(blue_section, bp)


    if s.game.ball_count.position < 1:
        if s.game.odds_only.status == True:
            b = [18,887]
            screen.blit(button, b)
        elif s.game.features.status == True:
            b = [18,937]
            screen.blit(button, b)
        else:
            b = [18,990]
            screen.blit(button, b)


    if s.game.red_super_section.status == True:
        rss = [50,410]
        screen.blit(super_section, rss)
    if s.game.yellow_super_section.status == True:
        yss = [53,490]
        screen.blit(super_section, yss)
    if s.game.orange_section.status == True:
        oss = [53,572]
        screen.blit(orange_section, oss)

    if s.game.magic_screen_feature.position >= 4:
        ms = [155,675]
        screen.blit(ms_letter, ms)
    if s.game.magic_screen_feature.position >= 5:
        ms = [197,675]
        screen.blit(ms_letter, ms)
    if s.game.magic_screen_feature.position >= 6:
        ms = [239,675]
        screen.blit(ms_letter, ms)
    if s.game.magic_screen_feature.position >= 7:
        ms = [283,675]
        screen.blit(ms_letter, ms)
    if s.game.magic_screen_feature.position >= 8:
        ms = [324,675]
        screen.blit(ms_letter, ms)
    if s.game.magic_screen_feature.position >= 9:
        ms = [364,675]
        screen.blit(ms_letter, ms)
    if s.game.magic_screen_feature.position >= 10:
        ms = [405,675]
        screen.blit(ms_letter, ms)

    if s.game.ok.status == True:
        ms = [70,675]
        screen.blit(ms_letter, ms)
        ms = [28,675]
        screen.blit(ms_letter, ms)


    if s.game.magic_screen.position == 0:
        ms = [35,730]
        screen.blit(ms_indicator, ms)
    if s.game.magic_screen.position == 1:
        ms = [78,730]
        screen.blit(ms_indicator, ms)
    if s.game.magic_screen.position == 3:
        ms = [165,730]
        screen.blit(ms_indicator, ms)
    if s.game.magic_screen.position == 4:
        ms = [207,730]
        screen.blit(ms_indicator, ms)
    if s.game.magic_screen.position == 5:
        ms = [245,730]
        screen.blit(ms_indicator, ms)
    if s.game.magic_screen.position == 6:
        ms = [287,730]
        screen.blit(ms_indicator, ms)
    if s.game.magic_screen.position == 7:
        ms = [330,730]
        screen.blit(ms_indicator, ms)
    if s.game.magic_screen.position == 8:
        ms = [369,730]
        screen.blit(ms_indicator, ms)
    if s.game.magic_screen.position == 9:
        ms = [409,730]
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
        o = [187,786]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 2:
        o = [247,786]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 3:
        o = [309,786]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 4:
        o = [370,786]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 5:
        o = [423,786]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 6:
        o = [472,786]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 7:
        o = [522,786]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 8:
        o = [568,786]
        screen.blit(odds, o)

    if s.game.yellow_odds.position == 1:
        o = [187,858]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 2:
        o = [247,858]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 3:
        o = [309,858]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 4:
        o = [370,858]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 5:
        o = [423,858]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 6:
        o = [472,858]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 7:
        o = [522,858]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 8:
        o = [568,858]
        screen.blit(odds, o)

    if s.game.green_odds.position == 1:
        o = [187,930]
        screen.blit(odds, o)
        p = [36,263]
        screen.blit(futurity, p)
    elif s.game.green_odds.position == 2:
        o = [247,930]
        screen.blit(odds, o)
        p = [36,263]
        screen.blit(futurity, p)
    elif s.game.green_odds.position == 3:
        o = [309,930]
        screen.blit(odds, o)
        p = [36,263]
        screen.blit(futurity, p)
    elif s.game.green_odds.position == 4:
        o = [370,930]
        screen.blit(odds, o)
        p = [67,263]
        screen.blit(futurity, p)
    elif s.game.green_odds.position == 5:
        o = [423,930]
        screen.blit(odds, o)
        p = [98,263]
        screen.blit(futurity, p)
    elif s.game.green_odds.position == 6:
        o = [472,930]
        screen.blit(odds, o)
        p = [131,263]
        screen.blit(futurity, p)
    elif s.game.green_odds.position == 7:
        o = [522,930]
        screen.blit(odds, o)
        p = [160,263]
        screen.blit(futurity, p)
    elif s.game.green_odds.position == 8:
        o = [568,930]
        screen.blit(odds, o)
        p = [192,263]
        screen.blit(futurity, p)

    if s.game.futurity.position == 1:
        p = [496,243]
        screen.blit(futurity, p)
    if s.game.futurity.position == 2:
        p = [526,243]
        screen.blit(futurity, p)
    if s.game.futurity.position == 3:
        p = [557,243]
        screen.blit(futurity, p)
    if s.game.futurity.position == 4:
        p = [588,243]
        screen.blit(futurity, p)
    if s.game.futurity.position == 5:
        p = [621,243]
        screen.blit(futurity, p)
    if s.game.futurity.position == 6:
        p = [651,243]
        screen.blit(futurity, p)
    if s.game.futurity.position == 7:
        p = [496,278]
        screen.blit(futurity, p)
    if s.game.futurity.position == 8:
        p = [526,278]
        screen.blit(futurity, p)
    if s.game.futurity.position == 9:
        p = [557,278]
        screen.blit(futurity, p)
    if s.game.futurity.position == 10:
        p = [588,278]
        screen.blit(futurity, p)
    if s.game.futurity.position == 11:
        p = [621,278]
        screen.blit(futurity, p)
    if s.game.futurity.position == 12:
        p = [651,278]
        screen.blit(futurity, p)


    if s.game.tilt.status == True:
        tilt_position = [572,635]
        screen.blit(tilt, tilt_position)

    pygame.display.update()

def eb_animation(num):
    global screen
    if num == 3:
        eb_position = [151,1051]
        screen.blit(eb_number, eb_position)
        pygame.display.update()
    if num == 2:
        eb_position = [198,1051]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 1:
        eb_position = [263,1051]
        screen.blit(eb, eb_position)
        pygame.display.update()


def feature_animation(num):
    global screen

    if num == 4:
        rss = [50,410]
        screen.blit(super_section, rss)
        pygame.display.update()
    else:
        yss = [53,490]
        screen.blit(super_section, yss)
        pygame.display.update()


def odds_animation(num):
    global screen

    if num == 8:
        odds_position = [187,786]
        screen.blit(odds, odds_position)
    if num == 7:
        odds_position = [247,858]
        screen.blit(odds, odds_position)
    if num == 6:
        odds_position = [309,930]
        screen.blit(odds, odds_position)
    if num == 5:
        odds_position = [370,786]
        screen.blit(odds, odds_position)
    if num == 4:
        odds_position = [423,858]
        screen.blit(odds, odds_position)
    if num == 3:
        odds_position = [472,930]
        screen.blit(odds, odds_position)
    if num == 2:
        odds_position = [522,786]
        screen.blit(odds, odds_position)
    if num == 1:
        odds_position = [568,858]
        screen.blit(odd, odds_position)
    pygame.display.update()


