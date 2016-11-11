
import pygame
import random

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

meter = pygame.image.load('graphics/assets/register_cover.png').convert()
magic_screen = pygame.image.load('sea_island/assets/magic_screen.png').convert()
number_card = pygame.image.load('sea_island/assets/number_card.png').convert()
odds = pygame.image.load('sea_island/assets/odds.png').convert_alpha()
eb = pygame.image.load('sea_island/assets/extra_ball.png').convert_alpha()
eb_number = pygame.image.load('sea_island/assets/eb_number.png').convert_alpha()
extra_balls = pygame.image.load('sea_island/assets/extra_balls.png').convert_alpha()
feature = pygame.image.load('sea_island/assets/selection.png').convert_alpha()
ms_indicator = pygame.image.load('sea_island/assets/ms_arrow.png').convert_alpha()
ms_teaser = pygame.image.load('sea_island/assets/ms_teaser.png').convert_alpha()
ti = pygame.image.load('sea_island/assets/selection_arrow.png').convert_alpha()
super_section = pygame.image.load('sea_island/assets/super_section.png').convert_alpha()
ms_letter = pygame.image.load('sea_island/assets/ms_letter.png').convert_alpha()
number = pygame.image.load('sea_island/assets/number.png').convert_alpha()
select_now = pygame.image.load('sea_island/assets/select_now.png').convert_alpha()
three_blue = pygame.image.load('sea_island/assets/blue_section.png').convert_alpha()
tilt = pygame.image.load('sea_island/assets/tilt.png').convert_alpha()

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
        backglass = pygame.image.load('sea_island/assets/sea_island_menu.png').convert()
        backglass.set_colorkey((255,0,252))
    else:
        if (s.game.anti_cheat.status == True):
            backglass = pygame.image.load('sea_island/assets/sea_island_gi.png').convert()
            backglass.set_colorkey((255,0,252))
        else:
            backglass = pygame.image.load('sea_island/assets/sea_island_off.png').convert()
            backglass.set_colorkey((255,0,252))
    backglass = pygame.transform.scale(backglass, (720, 1280))
    
    screen.blit(backglass, backglass_position)

    if s.game.eb_play.status == True:
        eb_position = [40,1029]
        screen.blit(extra_balls, eb_position)

    if s.game.extra_ball.position >= 1:
        eb_position = [151,1029]
        screen.blit(eb_number, eb_position)
    if s.game.extra_ball.position >= 2:
        eb_position = [198,1029]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 3:
        eb_position = [262,1029]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 4:
        eb_position = [330,1029]
        screen.blit(eb_number, eb_position)
    if s.game.extra_ball.position >= 5:
        eb_position = [376,1029]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 6:
        eb_position = [436,1029]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 7:
        eb_position = [506,1029]
        screen.blit(eb_number, eb_position)
    if s.game.extra_ball.position >= 8:
        eb_position = [554,1029]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 9:
        eb_position = [617,1029]
        screen.blit(eb, eb_position)
    

    if s.game.selection_feature.position == 1:
        i = [672,583]
        screen.blit(ti, i)
    if s.game.selection_feature.position == 2 or s.game.selection_feature.position == 3:
        i = [672,528]
        screen.blit(ti, i)
    if s.game.selection_feature.position == 4 or s.game.selection_feature.position == 5 or s.game.selection_feature.position == 6:
        i = [672,476]
        screen.blit(ti, i)
    if s.game.selection_feature.position == 7:
        i = [672,422]
        screen.blit(ti, i)
    if s.game.selection_feature.position == 8:
        i = [672,368]
        screen.blit(ti, i)

    if s.game.red_star.status == True:
        rs_position = [550,459]
        screen.blit(feature, rs_position)
    if s.game.yellow_star.status == True:
        rs_position = [550,516]
        screen.blit(feature, rs_position)

    if s.game.magic_screen_feature.position >= 7:
        if s.game.selection_feature.position < 7:
            bfp = [550,568]
            screen.blit(feature, bfp)
        elif s.game.selection_feature.position == 7:
            bfp = [550,408]
            screen.blit(feature, bfp)
        elif s.game.selection_feature.position == 8:
            bfp = [550,354]
            screen.blit(feature, bfp)

    if s.game.magic_screen_feature.position >= 9:
        if s.game.three_blue.status == True:
            bp = [55,348]
            screen.blit(three_blue, bp)
        elif s.game.two_blue.status == True:
            bp = [117,348]
            screen.blit(three_blue, bp)

    if s.game.red_super_section.status == True:
        rss = [53,441]
        screen.blit(super_section, rss)
    if s.game.yellow_super_section.status == True:
        yss = [53,537]
        screen.blit(super_section, yss)

    if s.game.magic_screen_feature.position == 1:
        ms = [28,679]
        screen.blit(ms_teaser, ms)
    if s.game.magic_screen_feature.position == 2:
        ms = [68,679]
        screen.blit(ms_teaser, ms)
    if s.game.magic_screen_feature.position == 3:
        ms = [105,679]
        screen.blit(ms_teaser, ms)
    if s.game.magic_screen_feature.position >= 4:
        ms = [153,673]
        screen.blit(ms_letter, ms)
    if s.game.magic_screen_feature.position >= 5:
        ms = [190,673]
        screen.blit(ms_letter, ms)
    if s.game.magic_screen_feature.position >= 6:
        ms = [227,673]
        screen.blit(ms_letter, ms)
    if s.game.magic_screen_feature.position >= 7:
        ms = [263,673]
        screen.blit(ms_letter, ms)
    if s.game.magic_screen_feature.position >= 8:
        ms = [299,673]
        screen.blit(ms_letter, ms)
    if s.game.magic_screen_feature.position >= 9:
        ms = [334,673]
        screen.blit(ms_letter, ms)
    if s.game.magic_screen_feature.position >= 10:
        ms = [370,673]
        screen.blit(ms_letter, ms)
    if s.game.magic_screen_feature.position >= 11:
        ms = [405,673]
        screen.blit(ms_letter, ms)

    if s.game.magic_screen.position == 1:
        ms = [155,724]
        screen.blit(ms_indicator, ms)
    if s.game.magic_screen.position == 2:
        ms = [192,724]
        screen.blit(ms_indicator, ms)
    if s.game.magic_screen.position == 3:
        ms = [229,724]
        screen.blit(ms_indicator, ms)
    if s.game.magic_screen.position == 4:
        ms = [265,724]
        screen.blit(ms_indicator, ms)
    if s.game.magic_screen.position == 5:
        ms = [301,724]
        screen.blit(ms_indicator, ms)
    if s.game.magic_screen.position == 6:
        ms = [336,724]
        screen.blit(ms_indicator, ms)
    if s.game.magic_screen.position == 7:
        ms = [372,724]
        screen.blit(ms_indicator, ms)
    if s.game.magic_screen.position == 8:
        ms = [407,724]
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
        o = [190,779]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 2:
        o = [250,779]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 3:
        o = [312,779]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 4:
        o = [373,779]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 5:
        o = [425,779]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 6:
        o = [474,779]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 7:
        o = [522,779]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 8:
        o = [568,779]
        screen.blit(odds, o)

    if s.game.yellow_odds.position == 1:
        o = [190,845]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 2:
        o = [250,845]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 3:
        o = [312,845]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 4:
        o = [373,845]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 5:
        o = [425,845]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 6:
        o = [474,845]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 7:
        o = [522,845]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 8:
        o = [568,845]
        screen.blit(odds, o)

    if s.game.green_odds.position == 1:
        o = [190,917]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 2:
        o = [250,917]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 3:
        o = [312,917]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 4:
        o = [373,917]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 5:
        o = [425,917]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 6:
        o = [474,917]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 7:
        o = [522,917]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 8:
        o = [568,917]
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
        rss = [53,441]
        screen.blit(super_section, rss)
        pygame.display.update()
    else:
        yss = [53,537]
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


