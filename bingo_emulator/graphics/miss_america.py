
import pygame
import random

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

meter = pygame.image.load('graphics/assets/black_register_cover.png').convert()
eb = pygame.image.load('miss_america/assets/eb.png').convert_alpha()
number_eb = pygame.image.load('miss_america/assets/eb_number.png').convert_alpha()
ebs = pygame.image.load('miss_america/assets/extra_balls.png').convert_alpha()
number = pygame.image.load('miss_america/assets/number.png').convert_alpha()
card = pygame.image.load('miss_america/assets/card.png').convert_alpha()
feature = pygame.image.load('miss_america/assets/feature.png').convert_alpha()
letter = pygame.image.load('miss_america/assets/letter.png').convert_alpha()
odds = pygame.image.load('miss_america/assets/odds.png').convert_alpha()
rollover = pygame.image.load('miss_america/assets/rollover.png').convert_alpha()
s_arrow = pygame.image.load('miss_america/assets/s_arrow.png').convert_alpha()
select_now = pygame.image.load('miss_america/assets/select_now.png').convert_alpha()
time = pygame.image.load('miss_america/assets/time.png').convert_alpha()
tilt = pygame.image.load('miss_america/assets/tilt.png').convert_alpha()
line1 = pygame.image.load('miss_america/assets/line1.png').convert_alpha()
line2 = pygame.image.load('miss_america/assets/line2.png').convert_alpha()
line3 = pygame.image.load('miss_america/assets/line3.png').convert_alpha()
line4 = pygame.image.load('miss_america/assets/line4.png').convert_alpha()
line5 = pygame.image.load('miss_america/assets/line5.png').convert_alpha()

class scorereel():
    """ Score Reels are used to count replays """
    def __init__(self, pos, image):
        self.position = pos
        self.default_y = self.position[1]
        self.image = pygame.image.load(image).convert()

reel1 = scorereel([87,758], "graphics/assets/white_reel.png")
reel10 = scorereel([68,758], "graphics/assets/white_reel.png")
reel100 = scorereel([49,758], "graphics/assets/white_reel.png")

def display(s, replays=0, menu=False):
    
    meter.set_colorkey((255,0,252))
    meter_position = [40,758]

    screen.blit(reel1.image, reel1.position)
    screen.blit(reel10.image, reel10.position)
    screen.blit(reel100.image, reel100.position)
    screen.blit(meter, meter_position)

    if s.game.line1.position == 0 or s.game.line1.position == 2:
        p = [62,352]
        screen.blit(line1, p)
    if s.game.line1.position == 1:
        p = [101,352]
        screen.blit(line1, p)
    if s.game.line1.position == 3:
        p = [19,352]
        screen.blit(line1, p)

    if s.game.line2.position == 0 or s.game.line2.position == 2:
        p = [62,393]
        screen.blit(line2, p)
    if s.game.line2.position == 1:
        p = [101,393]
        screen.blit(line2, p)
    if s.game.line2.position == 3:
        p = [19,393]
        screen.blit(line2, p)

    if s.game.line3.position == 0 or s.game.line3.position == 2:
        p = [62,434]
        screen.blit(line3, p)
    if s.game.line3.position == 1:
        p = [101,434]
        screen.blit(line3, p)
    if s.game.line3.position == 3:
        p = [19,434]
        screen.blit(line3, p)

    if s.game.line4.position == 0 or s.game.line4.position == 2:
        p = [62,474]
        screen.blit(line4, p)
    if s.game.line4.position == 1:
        p = [101,474]
        screen.blit(line4, p)
    if s.game.line4.position == 3:
        p = [19,474]
        screen.blit(line4, p)

    if s.game.line5.position == 0 or s.game.line5.position == 2:
        p = [62,515]
        screen.blit(line5, p)
    if s.game.line5.position == 1:
        p = [101,515]
        screen.blit(line5, p)
    if s.game.line5.position == 3:
        p = [19,515]
        screen.blit(line5, p)

    backglass_position = [0, 0]
    backglass = pygame.Surface(screen.get_size(), flags=pygame.SRCALPHA)
    backglass.set_colorkey((255,0,252))
    backglass.fill((0, 0, 0))
    if menu == True:
        backglass = pygame.image.load('miss_america/assets/miss_america_menu.png')
    else:
        if (s.game.anti_cheat.status == True):
            backglass = pygame.image.load('miss_america/assets/miss_america_gi.png')
        else:
            backglass = pygame.image.load('miss_america/assets/miss_america_off.png')
    backglass = pygame.transform.scale(backglass, (720, 1280))
    
    screen.blit(backglass, backglass_position)

    if s.game.rollovers.status == True and s.game.selection_feature.position >= 5:
        if s.game.cu:
            p = [13,925]
            screen.blit(rollover, p)
        else:
            p = [641,924]
            screen.blit(rollover, p)


    if s.game.extra_ball.position >= 1:
        eb_position = [135,997]
        screen.blit(number_eb, eb_position)
    if s.game.extra_ball.position >= 2:
        eb_position = [185,997]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 3:
        eb_position = [251,997]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 4:
        eb_position = [325,997]
        screen.blit(number_eb, eb_position)
    if s.game.extra_ball.position >= 5:
        eb_position = [376,997]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 6:
        eb_position = [442,997]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 7:
        eb_position = [515,997]
        screen.blit(number_eb, eb_position)
    if s.game.extra_ball.position >= 8:
        eb_position = [564,997]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 9:
        eb_position = [632,998]
        screen.blit(eb, eb_position)

    if s.game.red_odds.position == 1:
        odds_position = [13,633]
        screen.blit(odds, odds_position)
    if s.game.red_odds.position == 2:
        odds_position = [185,667]
        screen.blit(odds, odds_position)
    if s.game.red_odds.position == 3:
        odds_position = [288,644]
        screen.blit(odds, odds_position)
    if s.game.red_odds.position == 4:
        odds_position = [430,642]
        screen.blit(odds, odds_position)
    if s.game.red_odds.position == 5:
        odds_position = [530,670]
        screen.blit(odds, odds_position)
    if s.game.red_odds.position == 6:
        odds_position = [624,670]
        screen.blit(odds, odds_position)
    if s.game.red_odds.position == 7:
        odds_position = [669,670]
        screen.blit(odds, odds_position)

    if s.game.yellow_odds.position == 1:
        odds_position = [15,868]
        screen.blit(odds, odds_position)
    if s.game.yellow_odds.position == 2:
        odds_position = [185,728]
        screen.blit(odds, odds_position)
    if s.game.yellow_odds.position == 3:
        odds_position = [288,712]
        screen.blit(odds, odds_position)
    if s.game.yellow_odds.position == 4:
        odds_position = [430,712]
        screen.blit(odds, odds_position)
    if s.game.yellow_odds.position == 5:
        odds_position = [530,729]
        screen.blit(odds, odds_position)
    if s.game.yellow_odds.position == 6:
        odds_position = [624,730]
        screen.blit(odds, odds_position)
    if s.game.yellow_odds.position == 7:
        odds_position = [669,733]
        screen.blit(odds, odds_position)

    if s.game.green_odds.position == 1:
        odds_position = [58,877]
        screen.blit(odds, odds_position)
    if s.game.green_odds.position == 2:
        odds_position = [185,790]
        screen.blit(odds, odds_position)
    if s.game.green_odds.position == 3:
        odds_position = [288,780]
        screen.blit(odds, odds_position)
    if s.game.green_odds.position == 4:
        odds_position = [430,784]
        screen.blit(odds, odds_position)
    if s.game.green_odds.position == 5:
        odds_position = [534,788]
        screen.blit(odds, odds_position)
    if s.game.green_odds.position == 6:
        odds_position = [624,792]
        screen.blit(odds, odds_position)
    if s.game.green_odds.position == 7:
        odds_position = [669,792]
        screen.blit(odds, odds_position)

    if s.game.white_odds.position == 1:
        odds_position = [102,888]
        screen.blit(odds, odds_position)
    if s.game.white_odds.position == 2:
        odds_position = [187,850]
        screen.blit(odds, odds_position)
    if s.game.white_odds.position == 3:
        odds_position = [291,850]
        screen.blit(odds, odds_position)
    if s.game.white_odds.position == 4:
        odds_position = [431,850]
        screen.blit(odds, odds_position)
    if s.game.white_odds.position == 5:
        odds_position = [530,850]
        screen.blit(odds, odds_position)
    if s.game.white_odds.position == 6:
        odds_position = [606,882]
        screen.blit(odds, odds_position)
    if s.game.white_odds.position == 7:
        odds_position = [657,867]
        screen.blit(odds, odds_position)


    if s.game.tilt.status == False:
        if s.holes:
            if 1 in s.holes:
                if s.game.line2.position == 0 or s.game.line2.position == 2:
                    p = [192,396]
                    screen.blit(number, p)
                if s.game.line4.position == 0 or s.game.line4.position == 2:
                    p = [403,480]
                    screen.blit(number, p)
                if s.game.line2.position == 1:
                    p = [235,397]
                    screen.blit(number, p)
                if s.game.line4.position == 1:
                    p = [444,479]
                    screen.blit(number, p)
                if s.game.line2.position == 3:
                    p = [150,396]
                    screen.blit(number, p)
                if s.game.line4.position == 3:
                    p = [277,478]
                    screen.blit(number, p)
            if 2 in s.holes:
                if s.game.line2.position == 0 or s.game.line2.position == 2:
                    p = [107,395]
                    screen.blit(number, p)
                if s.game.line1.position == 0 or s.game.line1.position == 2:
                    p = [571,355]
                    screen.blit(number, p)
                if s.game.line2.position == 1:
                    p = [150,395]
                    screen.blit(number, p)
                if s.game.line1.position == 1:
                    p = [107,352]
                    screen.blit(number, p)
                if s.game.line2.position == 3:
                    p = [571,396]
                    screen.blit(number, p)
                if s.game.line1.position == 3:
                    p = [528,354]
                    screen.blit(number, p)
            if 3 in s.holes:
                if s.game.line3.position == 0 or s.game.line3.position == 2:
                    p = [277,436]
                    screen.blit(number, p)
                if s.game.line4.position == 0 or s.game.line4.position == 2:
                    p = [571,479]
                    screen.blit(number, p)
                if s.game.line3.position == 1:
                    p = [402,437]
                    screen.blit(number, p)
                if s.game.line4.position == 1:
                    p = [107,477]
                    screen.blit(number, p)
                if s.game.line3.position == 3:
                    p = [235,437]
                    screen.blit(number, p)
                if s.game.line4.position == 3:
                    p = [529,479]
                    screen.blit(number, p)
            if 4 in s.holes:
                if s.game.line5.position == 0 or s.game.line5.position == 2:
                    p = [150,518]
                    screen.blit(number, p)
                    p = [571,520]
                    screen.blit(number, p)
                if s.game.line5.position == 1:
                    p = [193,518]
                    screen.blit(number, p)
                    p = [109,518]
                    screen.blit(number, p)
                if s.game.line5.position == 3:
                    p = [109,518]
                    screen.blit(number, p)
                    p = [529,519]
                    screen.blit(number, p)
            if 5 in s.holes:
                if s.game.line1.position == 0 or s.game.line1.position == 2:
                    p = [107,353]
                    screen.blit(number, p)
                if s.game.line5.position == 0 or s.game.line5.position == 2:
                    p = [529,519]
                    screen.blit(number, p)
                if s.game.line1.position == 1:
                    p = [150,353]
                    screen.blit(number, p)
                if s.game.line5.position == 1:
                    p = [571,519]
                    screen.blit(number, p)
                if s.game.line1.position == 3:
                    p = [572,355]
                    screen.blit(number, p)
                if s.game.line5.position == 3:
                    p = [488,519]
                    screen.blit(number, p)
            if 6 in s.holes:
                if s.game.line1.position == 0 or s.game.line1.position == 2:
                    p = [235,354]
                    screen.blit(number, p)
                    p = [403,355]
                    screen.blit(number, p)
                if s.game.line1.position == 1:
                    p = [277,354]
                    screen.blit(number, p)
                    p = [446,355]
                    screen.blit(number, p)
                if s.game.line1.position == 3:
                    p = [193,354]
                    screen.blit(number, p)
                    p = [277,355]
                    screen.blit(number, p)
            if 7 in s.holes:
                if s.game.line3.position == 0 or s.game.line3.position == 2:
                    p = [403,438]
                    screen.blit(number, p)
                if s.game.line5.position == 0 or s.game.line5.position == 2:
                    p = [109,519]
                    screen.blit(number, p)
                if s.game.line3.position == 1:
                    p = [445,438]
                    screen.blit(number, p)
                if s.game.line5.position == 1:
                    p = [151,519]
                    screen.blit(number, p)
                if s.game.line3.position == 3:
                    p = [277,438]
                    screen.blit(number, p)
                if s.game.line5.position == 3:
                    p = [570,521]
                    screen.blit(number, p)
            if 8 in s.holes:
                if s.game.line1.position == 0 or s.game.line1.position == 2:
                    p = [193,355]
                    screen.blit(number, p)
                    p = [446,356]
                    screen.blit(number, p)
                if s.game.line1.position == 1:
                    p = [236,355]
                    screen.blit(number, p)
                    p = [488,355]
                    screen.blit(number, p)
                if s.game.line1.position == 3:
                    p = [150,353]
                    screen.blit(number, p)
                    p = [404,356]
                    screen.blit(number, p)
            if 9 in s.holes:
                if s.game.line3.position == 0 or s.game.line3.position == 2:
                    p = [107,436]
                    screen.blit(number, p)
                if s.game.line5.position == 0 or s.game.line5.position == 2:
                    p = [487,519]
                    screen.blit(number, p)
                if s.game.line3.position == 1:
                    p = [151,437]
                    screen.blit(number, p)
                if s.game.line5.position == 1:
                    p = [530,520]
                    screen.blit(number, p)
                if s.game.line3.position == 3:
                    p = [571,439]
                    screen.blit(number, p)
            if 10 in s.holes:
                if s.game.line1.position == 0 or s.game.line1.position == 2:
                    p = [529,355]
                    screen.blit(number, p)
                if s.game.line5.position == 0 or s.game.line5.position == 2:
                    p = [193,519]
                    screen.blit(number, p)
                if s.game.line1.position == 1:
                    p = [572,356]
                    screen.blit(number, p)
                if s.game.line5.position == 1:
                    p = [236,519]
                    screen.blit(number, p)
                if s.game.line1.position == 3:
                    p = [488,355]
                    screen.blit(number, p)
                if s.game.line5.position == 3:
                    p = [151,519]
                    screen.blit(number, p)
            if 11 in s.holes:
                if s.game.line1.position == 0 or s.game.line1.position == 2:
                    p = [488,355]
                    screen.blit(number, p)
                if s.game.line5.position == 0 or s.game.line5.position == 2:
                    p = [236,519]
                    screen.blit(number, p)
                if s.game.line1.position == 1:
                    p = [530,355]
                    screen.blit(number, p)
                if s.game.line5.position == 1:
                    p = [278,520]
                    screen.blit(number, p)
                if s.game.line1.position == 3:
                    p = [446,355]
                    screen.blit(number, p)
                if s.game.line5.position == 3:
                    p = [195,519]
                    screen.blit(number, p)
            if 12 in s.holes:
                if s.game.line3.position == 0 or s.game.line3.position == 2:
                    p = [235,437]
                    screen.blit(number, p)
                if s.game.line4.position == 0 or s.game.line4.position == 2:
                    p = [486,479]
                    screen.blit(number, p)
                if s.game.line3.position == 1:
                    p = [278,438]
                    screen.blit(number, p)
                if s.game.line4.position == 1:
                    p = [529,479]
                    screen.blit(number, p)
                if s.game.line3.position == 3:
                    p = [193,438]
                    screen.blit(number, p)
                if s.game.line4.position == 3:
                    p = [445,479]
                    screen.blit(number, p)
            if 13 in s.holes:
                if s.game.line2.position == 0 or s.game.line2.position == 2:
                    p = [277,397]
                    screen.blit(number, p)
                if s.game.line5.position == 0 or s.game.line5.position == 2:
                    p = [446,519]
                    screen.blit(number, p)
                if s.game.line2.position == 1:
                    p = [404,398]
                    screen.blit(number, p)
                if s.game.line5.position == 1:
                    p = [487,520]
                    screen.blit(number, p)
                if s.game.line2.position == 3:
                    p = [236,396]
                    screen.blit(number, p)
                if s.game.line5.position == 3:
                    p = [403,519]
                    screen.blit(number, p)
            if 14 in s.holes:
                if s.game.line1.position == 0 or s.game.line1.position == 2:
                    p = [151,354]
                    screen.blit(number, p)
                if s.game.line2.position == 0 or s.game.line2.position == 2:
                    p = [403,398]
                    screen.blit(number, p)
                if s.game.line1.position == 1:
                    p = [193,354]
                    screen.blit(number, p)
                if s.game.line2.position == 1:
                    p = [445,397]
                    screen.blit(number, p)
                if s.game.line1.position == 3:
                    p = [107,355]
                    screen.blit(number, p)
                if s.game.line2.position == 3:
                    p = [278,397]
                    screen.blit(number, p)
            if 15 in s.holes:
                if s.game.line2.position == 0 or s.game.line2.position == 2:
                    p = [571,398]
                    screen.blit(number, p)
                if s.game.line4.position == 0 or s.game.line4.position == 2:
                    p = [278,479]
                    screen.blit(number, p)
                if s.game.line2.position == 1:
                    p = [108,396]
                    screen.blit(number, p)
                if s.game.line4.position == 1:
                    p = [404,479]
                    screen.blit(number, p)
                if s.game.line2.position == 3:
                    p = [530,397]
                    screen.blit(number, p)
                if s.game.line4.position == 3:
                    p = [235,479]
                    screen.blit(number, p)
            if 16 in s.holes:
                if s.game.line3.position == 0 or s.game.line3.position == 2:
                    p = [487,438]
                    screen.blit(number, p)
                if s.game.line4.position == 0 or s.game.line4.position == 2:
                    p = [108,478]
                    screen.blit(number, p)
                if s.game.line3.position == 1:
                    p = [528,438]
                    screen.blit(number, p)
                if s.game.line4.position == 1:
                    p = [152,478]
                    screen.blit(number, p)
                if s.game.line3.position == 3:
                    p = [446,438]
                    screen.blit(number, p)
                if s.game.line4.position == 3:
                    p = [571,480]
                    screen.blit(number, p)
            if 17 in s.holes:
                if s.game.line3.position == 0 or s.game.line3.position == 2:
                    p = [192,438]
                    screen.blit(number, p)
                    p = [528,438]
                    screen.blit(number, p)
                if s.game.line3.position == 1:
                    p = [235,438]
                    screen.blit(number, p)
                    p = [571,438]
                    screen.blit(number, p)
                if s.game.line3.position == 3:
                    p = [151,436]
                    screen.blit(number, p)
                    p = [487,437]
                    screen.blit(number, p)
            if 18 in s.holes:
                if s.game.line3.position == 0 or s.game.line3.position == 2:
                    p = [445,438]
                    screen.blit(number, p)
                if s.game.line4.position == 0 or s.game.line4.position == 2:
                    p = [194,478]
                    screen.blit(number, p)
                if s.game.line3.position == 1:
                    p = [487,437]
                    screen.blit(number, p)
                if s.game.line4.position == 1:
                    p = [235,478]
                    screen.blit(number, p)
                if s.game.line3.position == 3:
                    p = [403,439]
                    screen.blit(number, p)
                if s.game.line4.position == 3:
                    p = [151,478]
                    screen.blit(number, p)
            if 19 in s.holes:
                if s.game.line2.position == 0 or s.game.line2.position == 2:
                    p = [151,396]
                    screen.blit(number, p)
                    p = [445,397]
                    screen.blit(number, p)
                if s.game.line2.position == 1:
                    p = [193,396]
                    screen.blit(number, p)
                    p = [446,398]
                    screen.blit(number, p)
                if s.game.line2.position == 3:
                    p = [109,393]
                    screen.blit(number, p)
                    p = [404,398]
                    screen.blit(number, p)
            if 20 in s.holes:
                if s.game.line2.position == 0 or s.game.line2.position == 2:
                    p = [236,396]
                    screen.blit(number, p)
                if s.game.line4.position == 0 or s.game.line4.position == 2:
                    p = [445,479]
                    screen.blit(number, p)
                if s.game.line2.position == 1:
                    p = [278,397]
                    screen.blit(number, p)
                if s.game.line4.position == 1:
                    p = [488,479]
                    screen.blit(number, p)
                if s.game.line2.position == 3:
                    p = [193,397]
                    screen.blit(number, p)
                if s.game.line4.position == 3:
                    p = [404,479]
                    screen.blit(number, p)
            if 21 in s.holes:
                if s.game.line4.position == 0 or s.game.line4.position == 2:
                    p = [236,478]
                    screen.blit(number, p)
                    p = [530,479]
                    screen.blit(number, p)
                if s.game.line4.position == 1:
                    p = [278,479]
                    screen.blit(number, p)
                    p = [571,480]
                    screen.blit(number, p)
                if s.game.line4.position == 3:
                    p = [194,478]
                    screen.blit(number, p)
                    p = [488,479]
                    screen.blit(number, p)
            if 22 in s.holes:
                if s.game.line2.position == 0 or s.game.line2.position == 2:
                    p = [531,397]
                    screen.blit(number, p)
                if s.game.line4.position == 0 or s.game.line4.position == 2:
                    p = [151,478]
                    screen.blit(number, p)
                if s.game.line2.position == 1:
                    p = [572,398]
                    screen.blit(number, p)
                if s.game.line4.position == 1:
                    p = [194,478]
                    screen.blit(number, p)
                if s.game.line2.position == 3:
                    p = [488,397]
                    screen.blit(number, p)
                if s.game.line4.position == 3:
                    p = [108,478]
                    screen.blit(number, p)
            if 23 in s.holes:
                if s.game.line2.position == 0 or s.game.line2.position == 2:
                    p = [488,397]
                    screen.blit(number, p)
                if s.game.line3.position == 0 or s.game.line3.position == 2:
                    p = [151,437]
                    screen.blit(number, p)
                if s.game.line2.position == 1:
                    p = [529,398]
                    screen.blit(number, p)
                if s.game.line3.position == 1:
                    p = [193,438]
                    screen.blit(number, p)
                if s.game.line2.position == 3:
                    p = [446,397]
                    screen.blit(number, p)
                if s.game.line3.position == 3:
                    p = [107,437]
                    screen.blit(number, p)
            if 24 in s.holes:
                if s.game.line5.position == 0 or s.game.line5.position == 2:
                    p = [278,520]
                    screen.blit(number, p)
                    p = [404,520]
                    screen.blit(number, p)
                if s.game.line5.position == 1:
                    p = [404,520]
                    screen.blit(number, p)
                    p = [446,520]
                    screen.blit(number, p)
                if s.game.line5.position == 3:
                    p = [278,520]
                    screen.blit(number, p)
                    p = [237,519]
                    screen.blit(number, p)
            if 25 in s.holes:
                if s.game.line1.position == 0 or s.game.line1.position == 2:
                    p = [278,355]
                    screen.blit(number, p)
                if s.game.line3.position == 0 or s.game.line3.position == 2:
                    p = [571,438]
                    screen.blit(number, p)
                if s.game.line1.position == 1:
                    p = [404,356]
                    screen.blit(number, p)
                if s.game.line3.position == 1:
                    p = [108,436]
                    screen.blit(number, p)
                if s.game.line1.position == 3:
                    p = [235,355]
                    screen.blit(number, p)
                if s.game.line3.position == 3:
                    p = [529,438]
                    screen.blit(number, p)

    if s.game.tilt.status == True:
        tilt_position = [36,710]
        screen.blit(tilt, tilt_position)

    if s.game.eb_play.status == True:
        ebs_position = [19,1000]
        screen.blit(ebs, ebs_position)

    if s.game.corners.status == True:
        p = [10,238]
        screen.blit(feature, p)

    if s.game.selector.position >= 1:
        p = [147,315]
        screen.blit(card, p)
    if s.game.selector.position >= 2:
        p = [441,315]
        screen.blit(card, p)
        p = [607,238]
        screen.blit(feature, p)

    if s.game.selection_feature.position >= 5:
        if s.game.before_fourth.status == True:
            p = [418,585]
            screen.blit(time, p)
        if s.game.before_fifth.status == True:
            p = [511,585]
            screen.blit(time, p)

    if s.game.selection_feature.position == 1:
        p = [23,592]
        screen.blit(s_arrow, p)
    if s.game.selection_feature.position == 2:
        p = [62,592]
        screen.blit(s_arrow, p)
    if s.game.selection_feature.position == 3:
        p = [102,592]
        screen.blit(s_arrow, p)
    if s.game.selection_feature.position == 4:
        p = [142,592]
        screen.blit(s_arrow, p)
    if s.game.selection_feature.position >= 5:
        p = [173,585]
        screen.blit(letter, p)
    if s.game.selection_feature.position >= 6:
        p = [222,585]
        screen.blit(letter, p)
    if s.game.selection_feature.position >= 7:
        p = [272,585]
        screen.blit(letter, p)
    if s.game.selection_feature.position >= 8:
        p = [322,585]
        screen.blit(letter, p)
    if s.game.selection_feature.position >= 9:
        p = [370,585]
        screen.blit(letter, p)

    if s.game.selection_feature.position >= 5:
        if s.game.before_fourth.status == True:
            if s.game.ball_count.position == 3:
                p = [483,641]
                screen.blit(select_now, p)
        elif s.game.before_fifth.status == True:
            if s.game.ball_count.position == 4:
                p = [483,641]
                screen.blit(select_now, p)

    pygame.display.update()

def eb_animation(num):
    global screen
    if num == 9:
        eb_position = [140,1004]
        screen.blit(number_eb, eb_position)
        pygame.display.update()
    if num == 8:
        eb_position = [190,1004]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 7:
        eb_position = [256,1004]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 6:
        eb_position = [326,1004]
        screen.blit(number_eb, eb_position)
        pygame.display.update()
    if num == 5:
        eb_position = [370,1004]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 4:
        eb_position = [437,1004]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 3:
        eb_position = [510,1004]
        screen.blit(number_eb, eb_position)
        pygame.display.update()
    if num == 2:
        eb_position = [560,1004]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 1:
        eb_position = [628,1004]
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
