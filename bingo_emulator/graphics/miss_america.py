
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
bg_menu = pygame.image.load('miss_america/assets/miss_america_menu.png')
bg_gi = pygame.image.load('miss_america/assets/miss_america_gi.png')
bg_off = pygame.image.load('miss_america/assets/miss_america_off.png')

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
        screen.blit(bg_menu, backglass_position)
    else:
        if (s.game.anti_cheat.status == True):
            screen.blit(bg_gi, backglass_position)
        else:
            screen.blit(bg_off, backglass_position)

    if s.game.rollovers.status == True and s.game.selection_feature.position >= 5 and s.game.eb_play.status == False:
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
                s.cancel_delayed(name="blink")
                blink([s,1,1])
            else:
                s.cancel_delayed(name="blink")
        elif s.game.before_fifth.status == True:
            if s.game.ball_count.position == 4:
                s.cancel_delayed(name="blink")
                blink([s,1,1])
            else:
                s.cancel_delayed(name="blink")

    pygame.display.update()

def blink(args):
    dirty_rects = []
    s = args[0]
    b = args[1]
    sn = args[2]

    if b == 0:
        if sn == 1:
            p = [483,641]
            dirty_rects.append(screen.blit(select_now, p))
        pygame.display.update(dirty_rects)
    else:
        dirty_rects.append(screen.blit(bg_gi, (483,641), pygame.Rect(483,641,151,35)))
        pygame.display.update(dirty_rects)
    b = not b

    args = [s,b,sn]

    s.delay(name="blink", delay=0.1, handler=blink, param=args)

def line_animation(args):
    dirty_rects = []
    s = args[0]
    num = args[1]
    line = args[2]

    if line == 1:
        if s.game.line1.position == 0:
            dirty_rects.append(screen.blit(line1, (19 - num, 352)))
        elif s.game.line1.position == 1:
            dirty_rects.append(screen.blit(line1, (62 - num, 352)))
        elif s.game.line1.position == 2:
            dirty_rects.append(screen.blit(line1, (101 + num, 352)))
        elif s.game.line1.position == 3:
            dirty_rects.append(screen.blit(line1, (62 + num, 352)))

        if (s.game.anti_cheat.status == True):
            dirty_rects.append(screen.blit(bg_gi, (5,352), pygame.Rect(5,352,800,44)))
        else:
            dirty_rects.append(screen.blit(bg_off, (5,352), pygame.Rect(5,352,800,50)))

    if line == 2:
        if s.game.line2.position == 0:
             dirty_rects.append(screen.blit(line2, (19 - num, 393)))
        elif s.game.line2.position == 1:
            dirty_rects.append(screen.blit(line2, (62 - num, 393)))
        elif s.game.line2.position == 2:
            dirty_rects.append(screen.blit(line2, (101 + num, 393)))
        elif s.game.line2.position == 3:
            dirty_rects.append(screen.blit(line2, (62 + num, 393)))
        
        if (s.game.anti_cheat.status == True):
            dirty_rects.append(screen.blit(bg_gi, (5,393), pygame.Rect(5,393,800,44)))
        else:
            dirty_rects.append(screen.blit(bg_off, (5,393), pygame.Rect(5,393,800,50)))

    if line == 3:
        if s.game.line3.position == 0:
             dirty_rects.append(screen.blit(line3, (19 - num, 434)))
        elif s.game.line3.position == 1:
            dirty_rects.append(screen.blit(line3, (62 - num, 434)))
        elif s.game.line3.position == 2:
            dirty_rects.append(screen.blit(line3, (101 + num, 434)))
        elif s.game.line3.position == 3:
            dirty_rects.append(screen.blit(line3, (62 + num, 434)))
        
        if (s.game.anti_cheat.status == True):
            dirty_rects.append(screen.blit(bg_gi, (5,434), pygame.Rect(5,434,800,44)))
        else:
            dirty_rects.append(screen.blit(bg_off, (5,434), pygame.Rect(5,434,800,50)))

    if line == 4:
        if s.game.line4.position == 0:
             dirty_rects.append(screen.blit(line4, (19 - num, 474)))
        elif s.game.line4.position == 1:
            dirty_rects.append(screen.blit(line4, (62 - num, 474)))
        elif s.game.line4.position == 2:
            dirty_rects.append(screen.blit(line4, (101 + num, 474)))
        elif s.game.line4.position == 3:
            dirty_rects.append(screen.blit(line4, (62 + num, 474)))
        
        if (s.game.anti_cheat.status == True):
            dirty_rects.append(screen.blit(bg_gi, (5,474), pygame.Rect(5,474,800,44)))
        else:
            dirty_rects.append(screen.blit(bg_off, (5,474), pygame.Rect(5,474,800,50)))

    if line == 5:
        if s.game.line5.position == 0:
             dirty_rects.append(screen.blit(line5, (19 - num, 515)))
        elif s.game.line5.position == 1:
            dirty_rects.append(screen.blit(line5, (62 - num, 515)))
        elif s.game.line5.position == 2:
            dirty_rects.append(screen.blit(line5, (101 + num, 515)))
        elif s.game.line5.position == 3:
            dirty_rects.append(screen.blit(line5, (62 + num, 515)))
        
        if (s.game.anti_cheat.status == True):
            dirty_rects.append(screen.blit(bg_gi, (5,515), pygame.Rect(5,515,800,44)))
        else:
            dirty_rects.append(screen.blit(bg_off, (5,515), pygame.Rect(5,515,800,50)))

    
    pygame.display.update(dirty_rects)


def eb_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]

    if s.game.extra_ball.position < 1:
        dirty_rects.append(screen.blit(bg_gi, (137,997), pygame.Rect(137,997,52,34)))
    if s.game.extra_ball.position < 2:
        dirty_rects.append(screen.blit(bg_gi, (185,997), pygame.Rect(185,997,69,35)))
    if s.game.extra_ball.position < 3:
        dirty_rects.append(screen.blit(bg_gi, (251,997), pygame.Rect(251,997,69,35)))
    if s.game.extra_ball.position < 4:
        dirty_rects.append(screen.blit(bg_gi, (325,997), pygame.Rect(325,997,52,34)))
    if s.game.extra_ball.position < 5:
        dirty_rects.append(screen.blit(bg_gi, (376,997), pygame.Rect(376,997,69,35)))
    if s.game.extra_ball.position < 6:
        dirty_rects.append(screen.blit(bg_gi, (442,997), pygame.Rect(442,997,69,35)))
    if s.game.extra_ball.position < 7:
        dirty_rects.append(screen.blit(bg_gi, (515,997), pygame.Rect(515,997,52,34)))
    if s.game.extra_ball.position < 8:
        dirty_rects.append(screen.blit(bg_gi, (564,997), pygame.Rect(564,997,69,35)))
    if s.game.extra_ball.position < 9:
        dirty_rects.append(screen.blit(bg_gi, (632,998), pygame.Rect(632,998,69,35)))
    pygame.display.update(dirty_rects)

    if num in [0,24,25,14,49,50]:
        if s.game.extra_ball.position < 1:
            p = [135,997]
            dirty_rects.append(screen.blit(number_eb, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [39,1,26,15]:
        if s.game.extra_ball.position < 2:
            p = [185,997]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [3,4,17,28,29,40]:
        if s.game.extra_ball.position < 3:
            p = [251,997]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [5,18,30,43]:
        if s.game.extra_ball.position < 4:
            p = [325,997]
            dirty_rects.append(screen.blit(number_eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [7,8,19,32,33,44]:
        if s.game.extra_ball.position < 5:
            p = [376,997]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [9,10,20,34,35,45]:
        if s.game.extra_ball.position < 6:
            p = [442,997]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [11,21,36,46]:
        if s.game.extra_ball.position < 7:
            p = [515,997]
            dirty_rects.append(screen.blit(number_eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [12,22,37,47]:
        if s.game.extra_ball.position < 8:
            p = [564,997]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [2,6,13,16,23,27,31,38,41,48]:
        if s.game.extra_ball.position < 9:
            p = [632,998]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return

def clear_odds(s, num):
    global screen

    dirty_rects = []

    if s.game.white_odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (102,888), pygame.Rect(102,888,37,60)))
    if s.game.white_odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (187,850), pygame.Rect(187,850,37,60)))
    if s.game.white_odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (291,850), pygame.Rect(291,850,37,60)))
    if s.game.white_odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (431,850), pygame.Rect(431,850,37,60)))
    if s.game.white_odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (606,882), pygame.Rect(606,882,37,60)))
    if s.game.white_odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (657,867), pygame.Rect(657,867,37,60)))

    if s.game.yellow_odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (15,868), pygame.Rect(15,868,37,60)))
    if s.game.yellow_odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (185,728), pygame.Rect(185,728,37,60)))
    if s.game.yellow_odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (430,712), pygame.Rect(430,712,37,60)))
    if s.game.yellow_odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (530,729), pygame.Rect(530,729,37,60)))
    if s.game.yellow_odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (624,730), pygame.Rect(624,730,37,60)))
    if s.game.yellow_odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (669,733), pygame.Rect(669,733,37,60)))

    if s.game.red_odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (13,633), pygame.Rect(13,633,37,60)))
    if s.game.red_odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (185,667), pygame.Rect(185,667,37,60)))
    if s.game.red_odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (288,644), pygame.Rect(288,644,37,60)))
    if s.game.red_odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (430,642), pygame.Rect(430,642,37,60)))
    if s.game.red_odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (530,670), pygame.Rect(530,670,37,60)))
    if s.game.red_odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (624,670), pygame.Rect(624,670,37,60)))

    if s.game.green_odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (58,877), pygame.Rect(58,877,37,60)))
    if s.game.green_odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (185,790), pygame.Rect(185,790,37,60)))
    if s.game.green_odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (288,780), pygame.Rect(288,780,37,60)))
    if s.game.green_odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (430,784), pygame.Rect(430,784,37,60)))
    if s.game.green_odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (534,788), pygame.Rect(534,788,37,60)))
    if s.game.green_odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (669,792), pygame.Rect(669,792,37,60)))

    pygame.display.update(dirty_rects)

def draw_odds_animation(s, num):
    global screen
    dirty_rects = []

    if num in [20,45]:
        if s.game.white_odds.position != 1:
            p = [102,888]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [12,37]:
        if s.game.white_odds.position != 2:
            p = [187,850]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [1,26]:
        if s.game.white_odds.position != 3:
            p = [291,850]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [6,31]:
        if s.game.white_odds.position != 4:
            p = [431,850]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [19,44]:
        if s.game.white_odds.position != 6:
            p = [606,882]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [18,43]:
        if s.game.white_odds.position != 7:
            p = [657,867]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return

    if num in [11,36]:
        if s.game.yellow_odds.position != 1:
            p = [15,868]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [4,29]:
        if s.game.yellow_odds.position != 2:
            p = [185,728]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [7,32]:
        if s.game.yellow_odds.position != 4:
            p = [430,712]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [13,38]:
        if s.game.yellow_odds.position != 5:
            p = [530,729]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [22,47]:
        if s.game.yellow_odds.position != 6:
            p = [624,730]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [17,42]:
        if s.game.yellow_odds.position != 7:
            p = [669,733]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return

    if num in [19,44]:
        if s.game.red_odds.position != 1:
            p = [13,633]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [5,30]:
        if s.game.red_odds.position != 2:
            p = [185,667]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [2,27]:
        if s.game.red_odds.position != 3:
            p = [288,644]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [15,40]:
        if s.game.red_odds.position != 4:
            p = [430,642]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [0,25]:
        if s.game.red_odds.position != 5:
            p = [530,670]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [9,34]:
        if s.game.red_odds.position != 6:
            p = [624,670]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return

    if num in [14,39]:
        if s.game.green_odds.position != 1:
            p = [58,877]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [3,28]:
        if s.game.green_odds.position != 2:
            p = [185,790]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [23,48]:
        if s.game.green_odds.position != 3:
            p = [288,780]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [8,33]:
        if s.game.green_odds.position != 4:
            p = [430,784]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [22,47]:
        if s.game.green_odds.position != 5:
            p = [534,788]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [10,35]:
        if s.game.green_odds.position != 7:
            p = [669,792]
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

    if s.game.before_fourth.status == False:
        dirty_rects.append(screen.blit(bg_gi, (418,585), pygame.Rect(418,585,97,55)))
    if s.game.before_fifth.status == False:
        dirty_rects.append(screen.blit(bg_gi, (511,585), pygame.Rect(511,585,97,55)))
    if not s.game.cu or s.game.rollovers.status == False:
        dirty_rects.append(screen.blit(bg_gi, (13,925), pygame.Rect(13,925,66,64)))
    if s.game.cu or s.game.rollovers.status == False:
        dirty_rects.append(screen.blit(bg_gi, (641,924), pygame.Rect(641,924,66,64)))
    if s.game.selection_feature.position < 5:
        dirty_rects.append(screen.blit(bg_gi, (173,585), pygame.Rect(173,585,52,54)))
    if s.game.selection_feature.position < 6:
        dirty_rects.append(screen.blit(bg_gi, (222,585), pygame.Rect(222,585,52,54)))
    if s.game.selection_feature.position < 7:
        dirty_rects.append(screen.blit(bg_gi, (272,585), pygame.Rect(272,585,52,54)))
    if s.game.selection_feature.position < 8:
        dirty_rects.append(screen.blit(bg_gi, (322,585), pygame.Rect(322,585,52,54)))
    if s.game.selection_feature.position < 9:
        dirty_rects.append(screen.blit(bg_gi, (370,585), pygame.Rect(370,585,52,54)))
    if s.game.corners.status == False:
        dirty_rects.append(screen.blit(bg_gi, (10,238), pygame.Rect(10,238,100,82)))
    if s.game.selector.position < 2:
        dirty_rects.append(screen.blit(bg_gi, (441,315), pygame.Rect(441,315,133,30)))
        dirty_rects.append(screen.blit(bg_gi, (607,238), pygame.Rect(607,238,100,82)))


    pygame.display.update(dirty_rects)


def draw_feature_animation(s, num):
    global screen
    dirty_rects = []

    if num in [19,34]:
        if s.game.before_fourth.status == False:
            p = [418,585]
            dirty_rects.append(screen.blit(time, p))
            pygame.display.update(dirty_rects)
            return
    if num in [17,24,42,49]:
        if s.game.before_fifth.status == False:
            p = [511,585]
            dirty_rects.append(screen.blit(time, p))
            pygame.display.update(dirty_rects)
            return
    if num in [11,25,36,0]:
        if not s.game.cu or s.game.rollovers.status == False:
            p = [13,925]
            dirty_rects.append(screen.blit(rollover, p))
            s.game.coils.yellowROLamp.pulse(85)
            pygame.display.update(dirty_rects)
            return
    if num in [10,21,25,35,46,50]:
        if s.game.cu or s.game.rollovers.status == False:
            p = [641,924]
            dirty_rects.append(screen.blit(rollover, p))
            s.game.coils.redROLamp.pulse(85)
            pygame.display.update(dirty_rects)
            return
    if num in [4,13,29,38]: 
        if s.game.selection_feature.position < 5:
            p = [173,585]
            dirty_rects.append(screen.blit(letter, p))
            p = [222,585]
            dirty_rects.append(screen.blit(letter, p))
            pygame.display.update(dirty_rects)
            return
    if num in [5,14,30,39]: 
        if s.game.selection_feature.position < 7:
            p = [272,585]
            dirty_rects.append(screen.blit(letter, p))
            pygame.display.update(dirty_rects)
            return
    if num in [6,15,31,40]:
        if s.game.selection_feature.position < 8:
            p = [322,585]
            dirty_rects.append(screen.blit(letter, p))
            pygame.display.update(dirty_rects)
            return
    if num in [7,16,32,41]:
        if s.game.selection_feature.position < 9:
            p = [370,585]
            dirty_rects.append(screen.blit(letter, p))
            pygame.display.update(dirty_rects)
            return
    if num in [2,9,22,27,34,47]:
        if s.game.corners.status == False:
            p = [10,238]
            dirty_rects.append(screen.blit(feature, p))
            pygame.display.update(dirty_rects)
            return
    if num in [3,8,12,18,23,28,33,37,43,48]:
        if s.game.selector.position < 2:
            p = [441,315]
            dirty_rects.append(screen.blit(card, p))
            p = [607,238]
            dirty_rects.append(screen.blit(feature, p))
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
