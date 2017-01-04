
import pygame
import random

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

meter = pygame.image.load('graphics/assets/black_register_cover.png').convert()
eb = pygame.image.load('miss_america_deluxe/assets/eb.png').convert_alpha()
number_eb = pygame.image.load('miss_america_deluxe/assets/eb_number.png').convert_alpha()
ebs = pygame.image.load('miss_america_deluxe/assets/extra_balls.png').convert_alpha()
number = pygame.image.load('miss_america_deluxe/assets/number.png').convert_alpha()
card = pygame.image.load('miss_america_deluxe/assets/card.png').convert_alpha()
feature = pygame.image.load('miss_america_deluxe/assets/feature.png').convert_alpha()
s_letter = pygame.image.load('miss_america_deluxe/assets/s_letter.png').convert_alpha()
odds = pygame.image.load('miss_america_deluxe/assets/odds.png').convert_alpha()
rollover = pygame.image.load('miss_america_deluxe/assets/rollovers.png').convert_alpha()
s_arrow = pygame.image.load('miss_america_deluxe/assets/s_arrow.png').convert_alpha()
select_now = pygame.image.load('miss_america_deluxe/assets/select_now.png').convert_alpha()
time = pygame.image.load('miss_america_deluxe/assets/time.png').convert_alpha()
tilt = pygame.image.load('miss_america_deluxe/assets/tilt.png').convert_alpha()
line1 = pygame.image.load('miss_america_deluxe/assets/line1.png').convert_alpha()
line2 = pygame.image.load('miss_america_deluxe/assets/line2.png').convert_alpha()
line3 = pygame.image.load('miss_america_deluxe/assets/line3.png').convert_alpha()
line4 = pygame.image.load('miss_america_deluxe/assets/line4.png').convert_alpha()
line5 = pygame.image.load('miss_america_deluxe/assets/line5.png').convert_alpha()
letter1 = pygame.image.load('miss_america_deluxe/assets/letter1.png').convert_alpha()
letter2 = pygame.image.load('miss_america_deluxe/assets/letter2.png').convert_alpha()
letter3 = pygame.image.load('miss_america_deluxe/assets/letter3.png').convert_alpha()
letter4 = pygame.image.load('miss_america_deluxe/assets/letter4.png').convert_alpha()
letter5 = pygame.image.load('miss_america_deluxe/assets/letter5.png').convert_alpha()
letter6 = pygame.image.load('miss_america_deluxe/assets/letter6.png').convert_alpha()
letter7 = pygame.image.load('miss_america_deluxe/assets/letter7.png').convert_alpha()
red_letter1 = pygame.image.load('miss_america_deluxe/assets/red_letter1.png').convert_alpha()
red_letter2 = pygame.image.load('miss_america_deluxe/assets/red_letter2.png').convert_alpha()
red_letter3 = pygame.image.load('miss_america_deluxe/assets/red_letter3.png').convert_alpha()
red_letter4 = pygame.image.load('miss_america_deluxe/assets/red_letter4.png').convert_alpha()
red_letter5 = pygame.image.load('miss_america_deluxe/assets/red_letter5.png').convert_alpha()
red_letter6 = pygame.image.load('miss_america_deluxe/assets/red_letter6.png').convert_alpha()
red_letter7 = pygame.image.load('miss_america_deluxe/assets/red_letter7.png').convert_alpha()
red_stars = pygame.image.load('miss_america_deluxe/assets/red_stars.png').convert_alpha()
red_letter_game = pygame.image.load('miss_america_deluxe/assets/red_letter_game.png').convert_alpha()
four_green = pygame.image.load('miss_america_deluxe/assets/four_green.png').convert_alpha()
striped_diagonals = pygame.image.load('miss_america_deluxe/assets/striped_diagonals.png').convert_alpha()

class scorereel():
    """ Score Reels are used to count replays """
    def __init__(self, pos, image):
        self.position = pos
        self.default_y = self.position[1]
        self.image = pygame.image.load(image).convert()

reel1 = scorereel([102,815], "graphics/assets/white_reel.png")
reel10 = scorereel([84,815], "graphics/assets/white_reel.png")
reel100 = scorereel([65,815], "graphics/assets/white_reel.png")
reel1000 = scorereel([46,815], "graphics/assets/white_reel.png")

def display(s, replays=0, menu=False):
    
    meter.set_colorkey((255,0,252))
    meter_position = [36,815]

    screen.blit(reel1.image, reel1.position)
    screen.blit(reel10.image, reel10.position)
    screen.blit(reel100.image, reel100.position)
    screen.blit(reel1000.image, reel1000.position)
    screen.blit(meter, meter_position)

    if s.game.line1.position == 0 or s.game.line1.position == 2:
        p = [60,298]
        screen.blit(line1, p)
    if s.game.line1.position == 1:
        p = [95,298]
        screen.blit(line1, p)
    if s.game.line1.position == 3:
        p = [20,298]
        screen.blit(line1, p)

    if s.game.line2.position == 0 or s.game.line2.position == 2:
        p = [60,341]
        screen.blit(line2, p)
    if s.game.line2.position == 1:
        p = [95,341]
        screen.blit(line2, p)
    if s.game.line2.position == 3:
        p = [20,341]
        screen.blit(line2, p)

    if s.game.line3.position == 0 or s.game.line3.position == 2:
        p = [60,384]
        screen.blit(line3, p)
    if s.game.line3.position == 1:
        p = [95,384]
        screen.blit(line3, p)
    if s.game.line3.position == 3:
        p = [20,384]
        screen.blit(line3, p)

    if s.game.line4.position == 0 or s.game.line4.position == 2:
        p = [60,427]
        screen.blit(line4, p)
    if s.game.line4.position == 1:
        p = [95,427]
        screen.blit(line4, p)
    if s.game.line4.position == 3:
        p = [20,427]
        screen.blit(line4, p)

    if s.game.line5.position == 0 or s.game.line5.position == 2:
        p = [60,471]
        screen.blit(line5, p)
    if s.game.line5.position == 1:
        p = [95,471]
        screen.blit(line5, p)
    if s.game.line5.position == 3:
        p = [20,471]
        screen.blit(line5, p)

    backglass_position = [0, 0]
    backglass = pygame.Surface(screen.get_size(), flags=pygame.SRCALPHA)
    backglass.set_colorkey((255,0,252))
    backglass.fill((0, 0, 0))
    if menu == True:
        backglass = pygame.image.load('miss_america_deluxe/assets/miss_america_deluxe_menu.png')
    else:
        if (s.game.anti_cheat.status == True):
            backglass = pygame.image.load('miss_america_deluxe/assets/miss_america_deluxe_gi.png')
        else:
            backglass = pygame.image.load('miss_america_deluxe/assets/miss_america_deluxe_off.png')
    backglass = pygame.transform.scale(backglass, (720, 1280))
    
    screen.blit(backglass, backglass_position)

    if s.game.rollovers.status == True and s.game.selection_feature.position >= 5:
        if s.game.cu:
            p = [158,724]
            screen.blit(rollover, p)
        else:
            p = [13,724]
            screen.blit(rollover, p)

    if s.game.tilt.status == False:
        if s.game.red_odds.position == 1:
            p = [240,169]
            screen.blit(red_letter1, p)
        elif s.game.red_odds.position == 2:
            p = [302,185]
            screen.blit(red_letter2, p)
        elif s.game.red_odds.position == 3:
            p = [359,183]
            screen.blit(red_letter3, p)
        elif s.game.red_odds.position == 4:
            p = [397,179]
            screen.blit(red_letter4, p)
        elif s.game.red_odds.position == 5:
            p = [444,182]
            screen.blit(red_letter5, p)
        elif s.game.red_odds.position == 6:
            p = [469,183]
            screen.blit(red_letter6, p)
        elif s.game.red_odds.position == 7:
            p = [513,181]
            screen.blit(red_letter7, p)

        p = [240,169]
        screen.blit(letter1, p)
        p = [302,185]
        screen.blit(letter2, p)
        p = [359,183]
        screen.blit(letter3, p)
        p = [397,179]
        screen.blit(letter4, p)
        p = [444,182]
        screen.blit(letter5, p)
        p = [469,183]
        screen.blit(letter6, p)
        p = [513,181]
        screen.blit(letter7, p)


    if s.game.eb_play.status == True:
        ebs_position = [43,1072]
        screen.blit(ebs, ebs_position)


    if s.game.extra_ball.position >= 1:
        eb_position = [149,1074]
        screen.blit(number_eb, eb_position)
    if s.game.extra_ball.position >= 2:
        eb_position = [200,1074]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 3:
        eb_position = [262,1074]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 4:
        eb_position = [323,1074]
        screen.blit(number_eb, eb_position)
    if s.game.extra_ball.position >= 5:
        eb_position = [375,1074]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 6:
        eb_position = [437,1073]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 7:
        eb_position = [499,1073]
        screen.blit(number_eb, eb_position)
    if s.game.extra_ball.position >= 8:
        eb_position = [548,1071]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 9:
        eb_position = [609,1070]
        screen.blit(eb, eb_position)

    if s.game.red_odds.position == 1:
        odds_position = [189,790]
        screen.blit(odds, odds_position)
    if s.game.red_odds.position == 2:
        odds_position = [267,790]
        screen.blit(odds, odds_position)
    if s.game.red_odds.position == 3:
        odds_position = [339,790]
        screen.blit(odds, odds_position)
    if s.game.red_odds.position == 4:
        odds_position = [405,790]
        screen.blit(odds, odds_position)
    if s.game.red_odds.position == 5:
        odds_position = [471,790]
        screen.blit(odds, odds_position)
    if s.game.red_odds.position == 6:
        odds_position = [531,790]
        screen.blit(odds, odds_position)
    if s.game.red_odds.position == 7:
        odds_position = [578,790]
        screen.blit(odds, odds_position)

    if s.game.yellow_odds.position == 1:
        odds_position = [189,860]
        screen.blit(odds, odds_position)
    if s.game.yellow_odds.position == 2:
        odds_position = [267,860]
        screen.blit(odds, odds_position)
    if s.game.yellow_odds.position == 3:
        odds_position = [339,860]
        screen.blit(odds, odds_position)
    if s.game.yellow_odds.position == 4:
        odds_position = [405,860]
        screen.blit(odds, odds_position)
    if s.game.yellow_odds.position == 5:
        odds_position = [471,860]
        screen.blit(odds, odds_position)
    if s.game.yellow_odds.position == 6:
        odds_position = [531,860]
        screen.blit(odds, odds_position)
    if s.game.yellow_odds.position == 7:
        odds_position = [578,858]
        screen.blit(odds, odds_position)

    if s.game.green_odds.position == 1:
        odds_position = [189,927]
        screen.blit(odds, odds_position)
    if s.game.green_odds.position == 2:
        odds_position = [267,927]
        screen.blit(odds, odds_position)
    if s.game.green_odds.position == 3:
        odds_position = [339,927]
        screen.blit(odds, odds_position)
    if s.game.green_odds.position == 4:
        odds_position = [405,927]
        screen.blit(odds, odds_position)
    if s.game.green_odds.position == 5:
        odds_position = [471,927]
        screen.blit(odds, odds_position)
    if s.game.green_odds.position == 6:
        odds_position = [531,927]
        screen.blit(odds, odds_position)
    if s.game.green_odds.position == 7:
        odds_position = [578,925]
        screen.blit(odds, odds_position)

    if s.game.white_odds.position == 1:
        odds_position = [189,989]
        screen.blit(odds, odds_position)
    if s.game.white_odds.position == 2:
        odds_position = [267,989]
        screen.blit(odds, odds_position)
    if s.game.white_odds.position == 3:
        odds_position = [339,989]
        screen.blit(odds, odds_position)
    if s.game.white_odds.position == 4:
        odds_position = [405,989]
        screen.blit(odds, odds_position)
    if s.game.white_odds.position == 5:
        odds_position = [471,989]
        screen.blit(odds, odds_position)
    if s.game.white_odds.position == 6:
        odds_position = [531,989]
        screen.blit(odds, odds_position)
    if s.game.white_odds.position == 7:
        odds_position = [578,987]
        screen.blit(odds, odds_position)

    if s.game.tilt.status == False:
        if s.holes:
            if 1 in s.holes:
                if s.game.line4.position == 0 or s.game.line4.position == 2:
                    p = [385,429]
                    screen.blit(number, p)
                if s.game.line2.position == 0 or s.game.line2.position == 2:
                    p = [187,342]
                    screen.blit(number, p)
                if s.game.line4.position == 1:
                    p = [423,427]
                    screen.blit(number, p)
                if s.game.line2.position == 1:
                    p = [223,342]
                    screen.blit(number, p)
                if s.game.line4.position == 3:
                    p = [263,429]
                    screen.blit(number, p)
                if s.game.line2.position == 3:
                    p = [146,344]
                    screen.blit(number, p)
            if 2 in s.holes:
                if s.game.line2.position == 0 or s.game.line2.position == 2:
                    p = [107,344]
                    screen.blit(number, p)
                if s.game.line1.position == 0 or s.game.line1.position == 2:
                    p = [538,301]
                    screen.blit(number, p)
                if s.game.line2.position == 1:
                    p = [147,343]
                    screen.blit(number, p)
                if s.game.line1.position == 1:
                    p = [103,302]
                    screen.blit(number, p)
                if s.game.line2.position == 3:
                    p = [539,342]
                    screen.blit(number, p)
                if s.game.line1.position == 3:
                    p = [499,299]
                    screen.blit(number, p)
            if 3 in s.holes:
                if s.game.line3.position == 0 or s.game.line3.position == 2:
                    p = [261,385]
                    screen.blit(number, p)
                if s.game.line4.position == 0 or s.game.line4.position == 2:
                    p = [539,427]
                    screen.blit(number, p)
                if s.game.line3.position == 1:
                    p = [381,386]
                    screen.blit(number, p)
                if s.game.line4.position == 1:
                    p = [107,431]
                    screen.blit(number, p)
                if s.game.line3.position == 3:
                    p = [225,387]
                    screen.blit(number, p)
                if s.game.line4.position == 3:
                    p = [499,426]
                    screen.blit(number, p)
            if 4 in s.holes:
                if s.game.line5.position == 0 or s.game.line5.position == 2:
                    p = [541,470]
                    screen.blit(number, p)
                    p = [146,472]
                    screen.blit(number, p)
                if s.game.line5.position == 1:
                    p = [106,473]
                    screen.blit(number, p)
                    p = [185,472]
                    screen.blit(number, p)
                if s.game.line5.position == 3:
                    p = [500,469]
                    screen.blit(number, p)
                    p = [105,473]
                    screen.blit(number, p)
            if 5 in s.holes:
                if s.game.line1.position == 0 or s.game.line1.position == 2:
                    p = [105,302]
                    screen.blit(number, p)
                if s.game.line5.position == 0 or s.game.line5.position == 2:
                    p = [501,469]
                    screen.blit(number, p)
                if s.game.line1.position == 1:
                    p = [145,301]
                    screen.blit(number, p)
                if s.game.line5.position == 1:
                    p = [536,469]
                    screen.blit(number, p)
                if s.game.line1.position == 3:
                    p = [538,301]
                    screen.blit(number, p)
                if s.game.line5.position == 3:
                    p = [460,468]
                    screen.blit(number, p)
            if 6 in s.holes:
                if s.game.line1.position == 0 or s.game.line1.position == 2:
                    p = [224,301]
                    screen.blit(number, p)
                    p = [381,300]
                    screen.blit(number, p)
                if s.game.line1.position == 1:
                    p = [263,299]
                    screen.blit(number, p)
                    p = [419,302]
                    screen.blit(number, p)
                if s.game.line1.position == 3:
                    p = [185,302]
                    screen.blit(number, p)
                    p = [263,301]
                    screen.blit(number, p)
            if 7 in s.holes:
                if s.game.line2.position == 0 or s.game.line2.position == 2:
                    p = [540,343]
                    screen.blit(number, p)
                if s.game.line4.position == 0 or s.game.line4.position == 2:
                    p = [263,429]
                    screen.blit(number, p)
                if s.game.line2.position == 1:
                    p = [107,344]
                    screen.blit(number, p)
                if s.game.line4.position == 1:
                    p = [382,427]
                    screen.blit(number, p)
                if s.game.line2.position == 3:
                    p = [499,343]
                    screen.blit(number, p)
                if s.game.line4.position == 3:
                    p = [225,429]
                    screen.blit(number, p)
            if 8 in s.holes:
                if s.game.line1.position == 0 or s.game.line1.position == 2:
                    p = [185,302]
                    screen.blit(number, p)
                    p = [421,299]
                    screen.blit(number, p)
                if s.game.line1.position == 1:
                    p = [224,301]
                    screen.blit(number, p)
                    p = [460,300]
                    screen.blit(number, p)
                if s.game.line1.position == 3:
                    p = [145,303]
                    screen.blit(number, p)
                    p = [382,299]
                    screen.blit(number, p)
            if 9 in s.holes:
                if s.game.line3.position == 0 or s.game.line3.position == 2:
                    p = [147,387]
                    screen.blit(number, p)
                if s.game.line5.position == 0 or s.game.line5.position == 2:
                    p = [461,470]
                    screen.blit(number, p)
                if s.game.line3.position == 1:
                    p = [186,386]
                    screen.blit(number, p)
                if s.game.line5.position == 1:
                    p = [501,468]
                    screen.blit(number, p)
                if s.game.line3.position == 3:
                    p = [106,387]
                    screen.blit(number, p)
                if s.game.line5.position == 3:
                    p = [422,470]
                    screen.blit(number, p)
            if 10 in s.holes:
                if s.game.line1.position == 0 or s.game.line1.position == 2:
                    p = [498,299]
                    screen.blit(number, p)
                if s.game.line5.position == 0 or s.game.line5.position == 2:
                    p = [184,472]
                    screen.blit(number, p)
                if s.game.line1.position == 1:
                    p = [538,300]
                    screen.blit(number, p)
                if s.game.line5.position == 1:
                    p = [225,471]
                    screen.blit(number, p)
                if s.game.line1.position == 3:
                    p = [459,300]
                    screen.blit(number, p)
                if s.game.line5.position == 3:
                    p = [147,473]
                    screen.blit(number, p)
            if 11 in s.holes:
                if s.game.line1.position == 0 or s.game.line1.position == 2:
                    p = [459,300]
                    screen.blit(number, p)
                if s.game.line5.position == 0 or s.game.line5.position == 2:
                    p = [224,471]
                    screen.blit(number, p)
                if s.game.line1.position == 1:
                    p = [498,301]
                    screen.blit(number, p)
                if s.game.line5.position == 1:
                    p = [264,472]
                    screen.blit(number, p)
                if s.game.line1.position == 3:
                    p = [420,301]
                    screen.blit(number, p)
                if s.game.line5.position == 3:
                    p = [185,473]
                    screen.blit(number, p)
            if 12 in s.holes:
                if s.game.line3.position == 0 or s.game.line3.position == 2:
                    p = [225,387]
                    screen.blit(number, p)
                if s.game.line4.position == 0 or s.game.line4.position == 2:
                    p = [461,427]
                    screen.blit(number, p)
                if s.game.line3.position == 1:
                    p = [264,386]
                    screen.blit(number, p)
                if s.game.line4.position == 1:
                    p = [501,427]
                    screen.blit(number, p)
                if s.game.line3.position == 3:
                    p = [187,386]
                    screen.blit(number, p)
                if s.game.line4.position == 3:
                    p = [423,426]
                    screen.blit(number, p)
            if 13 in s.holes:
                if s.game.line2.position == 0 or s.game.line2.position == 2:
                    p = [265,343]
                    screen.blit(number, p)
                if s.game.line5.position == 0 or s.game.line5.position == 2:
                    p = [421,471]
                    screen.blit(number, p)
                if s.game.line2.position == 1:
                    p = [381,343]
                    screen.blit(number, p)
                if s.game.line5.position == 1:
                    p = [461,470]
                    screen.blit(number, p)
                if s.game.line2.position == 3:
                    p = [225,343]
                    screen.blit(number, p)
                if s.game.line5.position == 3:
                    p = [383,471]
                    screen.blit(number, p)
            if 14 in s.holes:
                if s.game.line1.position == 0 or s.game.line1.position == 2:
                    p = [146,302]
                    screen.blit(number, p)
                if s.game.line2.position == 0 or s.game.line2.position == 2:
                    p = [381,342]
                    screen.blit(number, p)
                if s.game.line1.position == 1:
                    p = [185,304]
                    screen.blit(number, p)
                if s.game.line2.position == 1:
                    p = [422,344]
                    screen.blit(number, p)
                if s.game.line1.position == 3:
                    p = [105,304]
                    screen.blit(number, p)
                if s.game.line2.position == 3:
                    p = [265,344]
                    screen.blit(number, p)
            if 15 in s.holes:
                if s.game.line3.position == 0 or s.game.line3.position == 2:
                    p = [383,386]
                    screen.blit(number, p)
                if s.game.line5.position == 0 or s.game.line5.position == 2:
                    p = [106,475]
                    screen.blit(number, p)
                if s.game.line3.position == 1:
                    p = [422,385]
                    screen.blit(number, p)
                if s.game.line5.position == 1:
                    p = [146,473]
                    screen.blit(number, p)
                if s.game.line3.position == 3:
                    p = [264,387]
                    screen.blit(number, p)
                if s.game.line5.position == 3:
                    p = [541,471]
                    screen.blit(number, p)
            if 16 in s.holes:
                if s.game.line3.position == 0 or s.game.line3.position == 2:
                    p = [461,385]
                    screen.blit(number, p)
                if s.game.line4.position == 0 or s.game.line4.position == 2:
                    p = [108,431]
                    screen.blit(number, p)
                if s.game.line3.position == 1:
                    p = [499,387]
                    screen.blit(number, p)
                if s.game.line4.position == 1:
                    p = [146,429]
                    screen.blit(number, p)
                if s.game.line3.position == 3:
                    p = [423,384]
                    screen.blit(number, p)
                if s.game.line4.position == 3:
                    p = [540,427]
                    screen.blit(number, p)
            if 17 in s.holes:
                if s.game.line3.position == 0 or s.game.line3.position == 2:
                    p = [186,387]
                    screen.blit(number, p)
                    p = [500,386]
                    screen.blit(number, p)
                if s.game.line3.position == 1:
                    p = [225,386]
                    screen.blit(number, p)
                    p = [539,385]
                    screen.blit(number, p)
                if s.game.line3.position == 3:
                    p = [147,387]
                    screen.blit(number, p)
                    p = [460,385]
                    screen.blit(number, p)
            if 18 in s.holes:
                if s.game.line3.position == 0 or s.game.line3.position == 2:
                    p = [423,385]
                    screen.blit(number, p)
                if s.game.line4.position == 0 or s.game.line4.position == 2:
                    p = [185,430]
                    screen.blit(number, p)
                if s.game.line3.position == 1:
                    p = [460,384]
                    screen.blit(number, p)
                if s.game.line4.position == 1:
                    p = [224,429]
                    screen.blit(number, p)
                if s.game.line3.position == 3:
                    p = [383,385]
                    screen.blit(number, p)
                if s.game.line4.position == 3:
                    p = [147,431]
                    screen.blit(number, p)
            if 19 in s.holes:
                if s.game.line2.position == 0 or s.game.line2.position == 2:
                    p = [147,345]
                    screen.blit(number, p)
                    p = [422,344]
                    screen.blit(number, p)
                if s.game.line2.position == 1:
                    p = [187,345]
                    screen.blit(number, p)
                    p = [460,343]
                    screen.blit(number, p)
                if s.game.line2.position == 3:
                    p = [107,345]
                    screen.blit(number, p)
                    p = [382,344]
                    screen.blit(number, p)
            if 20 in s.holes:
                if s.game.line2.position == 0 or s.game.line2.position == 2:
                    p = [225,344]
                    screen.blit(number, p)
                if s.game.line4.position == 0 or s.game.line4.position == 2:
                    p = [422,429]
                    screen.blit(number, p)
                if s.game.line2.position == 1:
                    p = [265,344]
                    screen.blit(number, p)
                if s.game.line4.position == 1:
                    p = [461,428]
                    screen.blit(number, p)
                if s.game.line2.position == 3:
                    p = [187,345]
                    screen.blit(number, p)
                if s.game.line4.position == 3:
                    p = [383,428]
                    screen.blit(number, p)
            if 21 in s.holes:
                if s.game.line4.position == 0 or s.game.line4.position == 2:
                    p = [225,429]
                    screen.blit(number, p)
                    p = [501,429]
                    screen.blit(number, p)
                if s.game.line4.position == 1:
                    p = [265,430]
                    screen.blit(number, p)
                    p = [541,427]
                    screen.blit(number, p)
                if s.game.line4.position == 3:
                    p = [185,431]
                    screen.blit(number, p)
                    p = [461,428]
                    screen.blit(number, p)
            if 22 in s.holes:
                if s.game.line2.position == 0 or s.game.line2.position == 2:
                    p = [499,343]
                    screen.blit(number, p)
                if s.game.line4.position == 0 or s.game.line4.position == 2:
                    p = [147,430]
                    screen.blit(number, p)
                if s.game.line2.position == 1:
                    p = [541,343]
                    screen.blit(number, p)
                if s.game.line4.position == 1:
                    p = [185,431]
                    screen.blit(number, p)
                if s.game.line2.position == 3:
                    p = [461,342]
                    screen.blit(number, p)
                if s.game.line4.position == 3:
                    p = [109,431]
                    screen.blit(number, p)
            if 23 in s.holes:
                if s.game.line2.position == 0 or s.game.line2.position == 2:
                    p = [461,343]
                    screen.blit(number, p)
                if s.game.line3.position == 0 or s.game.line3.position == 2:
                    p = [106,388]
                    screen.blit(number, p)
                if s.game.line2.position == 1:
                    p = [499,343]
                    screen.blit(number, p)
                if s.game.line3.position == 1:
                    p = [147,387]
                    screen.blit(number, p)
                if s.game.line2.position == 3:
                    p = [423,343]
                    screen.blit(number, p)
                if s.game.line3.position == 3:
                    p = [539,385]
                    screen.blit(number, p)
            if 24 in s.holes:
                if s.game.line5.position == 0 or s.game.line5.position == 2:
                    p = [265,472]
                    screen.blit(number, p)
                    p = [383,471]
                    screen.blit(number, p)
                if s.game.line5.position == 1:
                    p = [383,471]
                    screen.blit(number, p)
                    p = [422,471]
                    screen.blit(number, p)
                if s.game.line5.position == 3:
                    p = [265,472]
                    screen.blit(number, p)
                    p = [225,472]
                    screen.blit(number, p)
            if 25 in s.holes:
                if s.game.line1.position == 0 or s.game.line1.position == 2:
                    p = [264,302]
                    screen.blit(number, p)
                if s.game.line3.position == 0 or s.game.line3.position == 2:
                    p = [540,385]
                    screen.blit(number, p)
                if s.game.line1.position == 1:
                    p = [382,301]
                    screen.blit(number, p)
                if s.game.line3.position == 1:
                    p = [106,389]
                    screen.blit(number, p)
                if s.game.line1.position == 3:
                    p = [225,302]
                    screen.blit(number, p)
                if s.game.line3.position == 3:
                    p = [499,385]
                    screen.blit(number, p)

    if s.game.tilt.status == True:
        tilt_position = [161,543]
        screen.blit(tilt, tilt_position)

    if s.game.corners.status == True:
        p = [5,374]
        screen.blit(feature, p)

    if s.game.selector.position >= 1:
        p = [109,268]
        screen.blit(card, p)
    if s.game.selector.position >= 2:
        p = [379,266]
        screen.blit(card, p)
        p = [630,379]
        screen.blit(feature, p)

    if s.game.selection_feature.position >= 5:
        if s.game.before_fourth.status == True:
            p = [247,660]
            screen.blit(time, p)
        if s.game.before_fifth.status == True:
            p = [364,660]
            screen.blit(time, p)

    if s.game.selection_feature.position == 1:
        p = [30,609]
        screen.blit(s_arrow, p)
    if s.game.selection_feature.position == 2:
        p = [72,609]
        screen.blit(s_arrow, p)
    if s.game.selection_feature.position == 3:
        p = [121,609]
        screen.blit(s_arrow, p)
    if s.game.selection_feature.position == 4:
        p = [167,609]
        screen.blit(s_arrow, p)
    if s.game.selection_feature.position >= 5:
        p = [209,610]
        screen.blit(s_letter, p)
    if s.game.selection_feature.position >= 6:
        p = [255,610]
        screen.blit(s_letter, p)
    if s.game.selection_feature.position >= 7:
        p = [301,610]
        screen.blit(s_letter, p)
    if s.game.selection_feature.position >= 8:
        p = [344,610]
        screen.blit(s_letter, p)
    if s.game.selection_feature.position >= 9:
        p = [390,610]
        screen.blit(s_letter, p)

    if s.game.selection_feature.position >= 5:
        if s.game.before_fourth.status == True:
            if s.game.ball_count.position == 3:
                p = [272,725]
                screen.blit(select_now, p)
        elif s.game.before_fifth.status == True:
            if s.game.ball_count.position == 4:
                p = [272,725]
                screen.blit(select_now, p)
    if s.game.selector.position >= 2:
        if s.game.red_letter_two.status == True:
            p = [499,653]
            screen.blit(red_stars, p)
            p = [500,703]
            screen.blit(red_letter_game, p)
        if s.game.red_letter_three.status == True:
            p = [570,653]
            screen.blit(red_stars, p)
            p = [500,703]
            screen.blit(red_letter_game, p)

        if s.game.green_corners.status == True:
            p = [505,558]
            screen.blit(four_green, p)
    
        if s.game.striped_diagonals.status == True:
            p = [13,666]
            screen.blit(striped_diagonals, p)

    pygame.display.update()

def eb_animation(num):
    global screen
    if num == 9:
        eb_position = [155,1038]
        screen.blit(number_eb, eb_position)
        pygame.display.update()
    if num == 8:
        eb_position = [202,1038]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 7:
        eb_position = [267,1038]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 6:
        eb_position = [327,1036]
        screen.blit(number_eb, eb_position)
        pygame.display.update()
    if num == 5:
        eb_position = [378,1036]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 4:
        eb_position = [442,1036]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 3:
        eb_position = [503,1032]
        screen.blit(number_eb, eb_position)
        pygame.display.update()
    if num == 2:
        eb_position = [551,1032]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 1:
        eb_position = [615,1032]
        screen.blit(eb, eb_position)
        pygame.display.update()


def feature_animation(num):
    global screen
    #if num == 6:
    #    p = [573,305]
    #    screen.blit(c, p)

    #if num == 5:
    #    p = [545,644]
    #    screen.blit(wild_pocket, p)

    #if num == 4:
    #    p = [545,743]
    #    screen.blit(wild_pocket, p)

    #if num == 3:
    #    p = [394,648]
    #    screen.blit(sc, p)
    #    p = [545,446]
    #    screen.blit(super_card, p)

    #if num == 2:
    #    p = [163,650]
    #    screen.blit(sc, p)
    #    p = [36,445]
    #    screen.blit(super_card, p)

    #if num == 1:
    #    p = [573,305]
    #    screen.blit(c, p)

    #pygame.display.update()

def odds_animation(num):
    global screen
    #if num == 5:
    #    odds_position = [24,816]
    #    screen.blit(o1, odds_position)
    #    pygame.display.update()
    #if num == 4:
    #    odds_position = [99,824]
    #    screen.blit(o2, odds_position)
    #    pygame.display.update()
    #if num == 3:
    #    odds_position = [188,834]
    #    screen.blit(o3, odds_position)
    #    pygame.display.update()
    #if num == 2:
    #    odds_position = [238,804]
    #    screen.blit(o4, odds_position)
    #    pygame.display.update()
    #if num == 1:
    #    odds_position = [289,802]
    #    screen.blit(o5, odds_position)
    #    pygame.display.update()
