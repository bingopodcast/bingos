
import pygame
import random

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

meter = pygame.image.load('graphics/assets/register_cover.png').convert()
magic_screen = pygame.image.load('ballerina/assets/magic_screen.png').convert()
number_card = pygame.image.load('ballerina/assets/number_card.png').convert()
odds = pygame.image.load('ballerina/assets/odds.png').convert_alpha()
eb = pygame.image.load('ballerina/assets/extra_ball.png').convert_alpha()
eb_number = pygame.image.load('ballerina/assets/eb_number.png').convert_alpha()
extra_balls = pygame.image.load('ballerina/assets/extra_balls.png').convert_alpha()
feature = pygame.image.load('ballerina/assets/selection.png').convert_alpha()
ms_indicator = pygame.image.load('ballerina/assets/ms_arrow.png').convert_alpha()
ms_teaser = pygame.image.load('ballerina/assets/ms_teaser.png').convert_alpha()
ti = pygame.image.load('ballerina/assets/selection_arrow.png').convert_alpha()
super_section = pygame.image.load('ballerina/assets/super_section.png').convert_alpha()
ms_letter = pygame.image.load('ballerina/assets/ms_letter.png').convert_alpha()
number = pygame.image.load('ballerina/assets/number.png').convert_alpha()
select_now = pygame.image.load('ballerina/assets/select_now.png').convert_alpha()
three_blue = pygame.image.load('ballerina/assets/blue_section.png').convert_alpha()
tilt = pygame.image.load('ballerina/assets/tilt.png').convert_alpha()
one_seven_feature = pygame.image.load('ballerina/assets/one_seven_feature.png').convert_alpha()
one_seven = pygame.image.load('ballerina/assets/one_seven.png').convert_alpha()

class scorereel():
    """ Score Reels are used to count replays """
    def __init__(self, pos, image):
        self.position = pos
        self.default_y = self.position[1]
        self.image = pygame.image.load(image).convert()

reel1 = scorereel([97,785], "graphics/assets/white_reel.png")
reel10 = scorereel([78,785], "graphics/assets/white_reel.png")
reel100 = scorereel([59,785], "graphics/assets/white_reel.png")

def display(s, replays=0, menu=False):
    
    meter.set_colorkey((255,0,252))
    meter_position = [51,785]

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
        backglass = pygame.image.load('ballerina/assets/ballerina_menu.png').convert_alpha()
    else:
        if (s.game.anti_cheat.status == True):
            backglass = pygame.image.load('ballerina/assets/ballerina_gi.png').convert_alpha()
        else:
            backglass = pygame.image.load('ballerina/assets/ballerina_off.png').convert_alpha()
    backglass = pygame.transform.scale(backglass, (720, 1280))
    
    screen.blit(backglass, backglass_position)

    if s.game.eb_play.status == True:
        eb_position = [41,1014]
        screen.blit(extra_balls, eb_position)

    if s.game.extra_ball.position >= 1:
        eb_position = [151,1014]
        screen.blit(eb_number, eb_position)
    if s.game.extra_ball.position >= 2:
        eb_position = [198,1014]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 3:
        eb_position = [262,1014]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 4:
        eb_position = [330,1014]
        screen.blit(eb_number, eb_position)
    if s.game.extra_ball.position >= 5:
        eb_position = [376,1014]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 6:
        eb_position = [436,1014]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 7:
        eb_position = [506,1014]
        screen.blit(eb_number, eb_position)
    if s.game.extra_ball.position >= 8:
        eb_position = [554,1014]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 9:
        eb_position = [617,1014]
        screen.blit(eb, eb_position)
    

    if s.game.magic_screen_feature.position >= 4:
        if s.game.before_fourth.status == True:
            p = [551,572]
            screen.blit(feature, p)
        if s.game.rollovers.status == True:
            p = [549,519]
            screen.blit(feature, p)
        if s.game.before_fifth.status == True:
            p = [549,465]
            screen.blit(feature, p)
        if s.game.after_fifth.status == True:
            p = [550,409]
            screen.blit(feature, p)

    if s.game.one_seven_feature.status == True:
        p = [527,231]
        screen.blit(one_seven_feature, p)
        if s.game.one_seven.status == True:
            p = [527,295]
            screen.blit(one_seven, p)
        if s.game.seven_one.status == True:
            p = [527,329]
            screen.blit(one_seven, p)

    if s.game.magic_screen_feature.position >= 8:
        if s.game.three_blue.status == True:
            bp = [51,359]
            screen.blit(three_blue, bp)
        elif s.game.two_blue.status == True:
            bp = [112,357]
            screen.blit(three_blue, bp)

    if s.game.yellow_super_section.status == True:
        rss = [50,452]
        screen.blit(super_section, rss)
    if s.game.red_super_section.status == True:
        yss = [50,539]
        screen.blit(super_section, yss)

    if s.game.magic_screen_feature.position >= 1:
        ms = [31,669]
        screen.blit(ms_letter, ms)
    if s.game.magic_screen_feature.position >= 2:
        ms = [68,669]
        screen.blit(ms_letter, ms)
    if s.game.magic_screen_feature.position >= 3:
        ms = [105,669]
        screen.blit(ms_letter, ms)
    if s.game.magic_screen_feature.position >= 4:
        ms = [142,669]
        screen.blit(ms_letter, ms)
    if s.game.magic_screen_feature.position == 5:
        ms = [183,680]
        screen.blit(ms_teaser, ms)
    if s.game.magic_screen_feature.position >= 6:
        ms = [211,669]
        screen.blit(ms_letter, ms)
    if s.game.magic_screen_feature.position == 7:
        ms = [249,681]
        screen.blit(ms_teaser, ms)
    if s.game.magic_screen_feature.position >= 8:
        ms = [277,669]
        screen.blit(ms_letter, ms)
    if s.game.magic_screen_feature.position == 9:
        ms = [315,681]
        screen.blit(ms_teaser, ms)
    if s.game.magic_screen_feature.position >= 10:
        ms = [343,669]
        screen.blit(ms_letter, ms)
    if s.game.magic_screen_feature.position == 11:
        ms = [381,680]
        screen.blit(ms_teaser, ms)
    if s.game.magic_screen_feature.position >= 12:
        ms = [408,669]
        screen.blit(ms_letter, ms)

    if s.game.magic_screen.position == 1:
        ms = [30,724]
        screen.blit(ms_indicator, ms)
    if s.game.magic_screen.position == 2:
        ms = [67,724]
        screen.blit(ms_indicator, ms)
    if s.game.magic_screen.position == 3:
        ms = [103,724]
        screen.blit(ms_indicator, ms)
    if s.game.magic_screen.position == 4:
        ms = [141,724]
        screen.blit(ms_indicator, ms)
    if s.game.magic_screen.position == 5:
        ms = [211,724]
        screen.blit(ms_indicator, ms)
    if s.game.magic_screen.position == 6:
        ms = [275,724]
        screen.blit(ms_indicator, ms)
    if s.game.magic_screen.position == 7:
        ms = [342,724]
        screen.blit(ms_indicator, ms)
    if s.game.magic_screen.position == 8:
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
        o = [190,765]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 2:
        o = [250,765]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 3:
        o = [312,765]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 4:
        o = [373,765]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 5:
        o = [425,765]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 6:
        o = [474,765]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 7:
        o = [522,765]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 8:
        o = [568,765]
        screen.blit(odds, o)

    if s.game.yellow_odds.position == 1:
        o = [190,831]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 2:
        o = [250,831]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 3:
        o = [312,831]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 4:
        o = [373,831]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 5:
        o = [425,831]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 6:
        o = [474,831]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 7:
        o = [522,831]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 8:
        o = [568,831]
        screen.blit(odds, o)

    if s.game.green_odds.position == 1:
        o = [190,903]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 2:
        o = [250,903]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 3:
        o = [312,903]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 4:
        o = [373,903]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 5:
        o = [425,903]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 6:
        o = [474,903]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 7:
        o = [522,903]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 8:
        o = [572,903]
        screen.blit(odds, o)


    if s.game.tilt.status == True:
        tilt_position = [572,632]
        screen.blit(tilt, tilt_position)

    pygame.display.update()

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
        rss = [50,539]
        screen.blit(super_section, rss)
        pygame.display.update()
    else:
        yss = [50,452]
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


