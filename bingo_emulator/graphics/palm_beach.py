
import pygame
import random

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

meter = pygame.image.load('graphics/assets/register_cover.png').convert()
eb = pygame.image.load('palm_beach/assets/arrow.png').convert_alpha()
exb = pygame.image.load('palm_beach/assets/extra_ball.png').convert_alpha()
og = pygame.image.load('palm_beach/assets/odds_gi.png').convert_alpha()
o10 = pygame.image.load('palm_beach/assets/odds10.png').convert_alpha()
o = pygame.image.load('palm_beach/assets/odds.png').convert_alpha()
sc = pygame.image.load('palm_beach/assets/super_card.png').convert_alpha()
star = pygame.image.load('palm_beach/assets/star.png').convert_alpha()
c = pygame.image.load('palm_beach/assets/corners.png').convert_alpha()
number = pygame.image.load('palm_beach/assets/number.png').convert_alpha()
sc_number = pygame.image.load('palm_beach/assets/sc_number.png').convert_alpha()
tilt = pygame.image.load('palm_beach/assets/tilt.png').convert_alpha()
oo = pygame.image.load('palm_beach/assets/play.png').convert_alpha()
f = pygame.image.load('palm_beach/assets/play.png').convert_alpha()
ebs = pygame.image.load('palm_beach/assets/extra_balls.png').convert_alpha()
bg_menu = pygame.image.load('palm_beach/assets/palm_beach_menu.png')
bg_gi = pygame.image.load('palm_beach/assets/palm_beach_gi.png')
bg_off = pygame.image.load('palm_beach/assets/palm_beach_off.png')

class scorereel():
    """ Score Reels are used to count replays """
    def __init__(self, pos, image):
        self.position = pos
        self.default_y = self.position[1]
        self.image = pygame.image.load(image).convert()

reel1 = scorereel([110,569], "graphics/assets/green_reel.png")
reel10 = scorereel([90,569], "graphics/assets/green_reel.png")
reel100 = scorereel([72,569], "graphics/assets/green_reel.png")

def display(s, replays=0, menu=False):
    
    meter.set_colorkey((255,0,252))
    meter_position = [61,570]

    screen.blit(reel1.image, reel1.position)
    screen.blit(reel10.image, reel10.position)
    screen.blit(reel100.image, reel100.position)
    screen.blit(meter, meter_position)

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

    if s.game.extra_ball.position == 1:
        eb_position = [31,960]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 2:
        eb_position = [57,960]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 3:
        eb_position = [84,960]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 4:
        eb_position = [111,960]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 5:
        eb_position = [137,960]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 6:
        eb_position = [163,960]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 7:
        eb_position = [189,960]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 8:
        eb_position = [215,960]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 9:
        eb_position = [259,960]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 10:
        eb_position = [286,960]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 11:
        eb_position = [312,960]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 12:
        eb_position = [339,960]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 13:
        eb_position = [365,960]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 14:
        eb_position = [391,960]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 15:
        eb_position = [417,960]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 16:
        eb_position = [445,960]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 17:
        eb_position = [487,960]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 18:
        eb_position = [515,960]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 19:
        eb_position = [540,960]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 20:
        eb_position = [567,960]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 21:
        eb_position = [593,960]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 22:
        eb_position = [618,960]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 23:
        eb_position = [645,960]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 24:
        eb_position = [672,960]
        screen.blit(eb, eb_position)

    if s.game.extra_ball.position >= 8:
        eb_position = [28,986]
        screen.blit(exb, eb_position)
    if s.game.extra_ball.position >= 16:
        eb_position = [256,986]
        screen.blit(exb, eb_position)
    if s.game.extra_ball.position >= 24:
        eb_position = [483,986]
        screen.blit(exb, eb_position)

    if s.game.odds.position > 0:
        odds_position = [39,398]
        screen.blit(og, odds_position)
        if s.game.odds.position == 1:
            odds_position = [159,397]
            screen.blit(o, odds_position)
        if s.game.odds.position == 2:
            odds_position = [212,397]
            screen.blit(o, odds_position)
        if s.game.odds.position == 3:
            odds_position = [265,397]
            screen.blit(o, odds_position)
        if s.game.odds.position == 4:
            odds_position = [318,397]
            screen.blit(o, odds_position)
        if s.game.odds.position == 5:
            odds_position = [370,397]
            screen.blit(o, odds_position)
        if s.game.odds.position == 6:
            odds_position = [421,397]
            screen.blit(o, odds_position)
        if s.game.odds.position == 7:
            odds_position = [474,397]
            screen.blit(o, odds_position)
        if s.game.odds.position == 8:
            odds_position = [526,397]
            screen.blit(o, odds_position)
        if s.game.odds.position == 9:
            odds_position = [578,397]
            screen.blit(o, odds_position)
        if s.game.odds.position == 10:
            odds_position = [631,397]
            screen.blit(o10, odds_position)

    if s.game.super_card.position > 0:
        if s.game.super_card.position == 1:
            sc_position = [51,691]
            screen.blit(eb, sc_position)
        if s.game.super_card.position == 2:
            sc_position = [77,691]
            screen.blit(eb, sc_position)
        if s.game.super_card.position == 3:
            sc_position = [105,691]
            screen.blit(eb, sc_position)
        if s.game.super_card.position == 4:
            sc_position = [131,691]
            screen.blit(eb, sc_position)
        if s.game.super_card.position == 5:
            sc_position = [568,691]
            screen.blit(eb, sc_position)
        if s.game.super_card.position == 6:
            sc_position = [595,691]
            screen.blit(eb, sc_position)
        if s.game.super_card.position == 7:
            sc_position = [621,691]
            screen.blit(eb, sc_position)
        if s.game.super_card.position == 8:
            sc_position = [648,691]
            screen.blit(eb, sc_position)
        if s.game.super_card.position >= 4:
            s_position = [47,719]
            screen.blit(sc, s_position)
        if s.game.super_card.position >= 8:
            s2_position = [564,719]
            screen.blit(sc, s2_position)

    if s.game.red_star.status == True:
        rs_position = [72,884]
        screen.blit(star, rs_position)

    if s.game.yellow_star.status == True:
        ys_position = [586,884]
        screen.blit(star, ys_position)

    if s.game.corners.status == True:
        corners_position = [568,555]
        screen.blit(c, corners_position)

    if s.game.tilt.status == False:
        if s.holes:
            if 1 in s.holes:
                number_position = [203,704]
                screen.blit(number, number_position)
                number_position = [43,793]
                screen.blit(sc_number, number_position)
            if 2 in s.holes:
                number_position = [203,768]
                screen.blit(number, number_position)
            if 3 in s.holes:
                number_position = [466,836]
                screen.blit(number, number_position)
                number_position = [602,755]
                screen.blit(sc_number, number_position)
            if 4 in s.holes:
                number_position = [332,575]
                screen.blit(number, number_position)
                number_position = [84,832]
                screen.blit(sc_number, number_position)
            if 5 in s.holes:
                number_position = [398,836]
                screen.blit(number, number_position)
            if 6 in s.holes:
                number_position = [465,578]
                screen.blit(number, number_position)
            if 7 in s.holes:
                number_position = [269,836]
                screen.blit(number, number_position)
                number_position = [83,752]
                screen.blit(sc_number, number_position)
            if 8 in s.holes:
                number_position = [465,707]
                screen.blit(number, number_position)
            if 9 in s.holes:
                number_position = [203,577]
                screen.blit(number, number_position)
                number_position = [561,793]
                screen.blit(sc_number, number_position)
            if 10 in s.holes:
                number_position = [203,836]
                screen.blit(number, number_position)
                number_position = [84,794]
                screen.blit(sc_number, number_position)
            if 11 in s.holes:
                number_position = [334,772]
                screen.blit(number, number_position)
                number_position = [642,793]
                screen.blit(sc_number, number_position)
            if 12 in s.holes:
                number_position = [399,705]
                screen.blit(number, number_position)
                number_position = [561,834]
                screen.blit(sc_number, number_position)
            if 13 in s.holes:
                number_position = [203,641]
                screen.blit(number, number_position)
                number_position = [124,794]
                screen.blit(sc_number, number_position)
            if 14 in s.holes:
                number_position = [335,641]
                screen.blit(number, number_position)
                number_position = [642,832]
                screen.blit(sc_number, number_position)
            if 15 in s.holes:
                number_position = [269,575]
                screen.blit(number, number_position)
            if 16 in s.holes:
                number_position = [333,704]
                screen.blit(number, number_position)
            if 17 in s.holes:
                number_position = [466,641]
                screen.blit(number, number_position)
            if 18 in s.holes:
                number_position = [267,704]
                screen.blit(number, number_position)
                number_position = [641,752]
                screen.blit(sc_number, number_position)
            if 19 in s.holes:
                number_position = [270,641]
                screen.blit(number, number_position)
                number_position = [44,753]
                screen.blit(sc_number, number_position)
            if 20 in s.holes:
                number_position = [400,641]
                screen.blit(number, number_position)
                number_position = [123,752]
                screen.blit(sc_number, number_position)
            if 21 in s.holes:
                number_position = [400,770]
                screen.blit(number, number_position)
                number_position = [124,835]
                screen.blit(sc_number, number_position)
            if 22 in s.holes:
                number_position = [266,772]
                screen.blit(number, number_position)
                number_position = [44,833]
                screen.blit(sc_number, number_position)
            if 23 in s.holes:
                number_position = [335,836]
                screen.blit(number, number_position)
                number_position = [561,754]
                screen.blit(sc_number, number_position)
            if 24 in s.holes:
                number_position = [400,577]
                screen.blit(number, number_position)
                number_position = [601,833]
                screen.blit(sc_number, number_position)
            if 25 in s.holes:
                number_position = [464,771]
                screen.blit(number, number_position)
                number_position = [600,793]
                screen.blit(sc_number, number_position)

    if s.game.tilt.status == True:
        tilt_position = [550,890]
        screen.blit(tilt, tilt_position)

    if s.game.odds_only.status == True:
        oo_position = [196,906]
        screen.blit(oo, oo_position)

    if s.game.features.status == True:
        f_position = [444,906]
        screen.blit(f, f_position)

    if s.game.eb.status == True:
        ebs_position = [302,925]
        screen.blit(ebs, ebs_position)

    pygame.display.update()

def eb_animation(num):
    global screen
    if num == 24:
        eb_position = [31,960]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 23:
        eb_position = [57,960]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 22:
        eb_position = [84,960]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 21:
        eb_position = [111,960]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 20:
        eb_position = [137,960]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 19:
        eb_position = [163,960]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 18:
        eb_position = [189,960]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 17:
        eb_position = [215,960]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 16:
        eb_position = [259,960]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 15:
        eb_position = [286,960]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 14:
        eb_position = [312,960]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 13:
        eb_position = [339,960]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 12:
        eb_position = [365,960]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 11:
        eb_position = [391,960]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 10:
        eb_position = [417,960]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 9:
        eb_position = [445,960]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 8:
        eb_position = [487,960]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 7:
        eb_position = [515,960]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 6:
        eb_position = [540,960]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 5:
        eb_position = [567,960]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 4:
        eb_position = [593,960]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 3:
        eb_position = [618,960]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 2:
        eb_position = [645,960]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 1:
        eb_position = [672,960]
        screen.blit(eb, eb_position)
        pygame.display.update()

def feature_animation(num):
    global screen
    if num == 5:
        corners_position = [568,555]
        screen.blit(c, corners_position)
        pygame.display.update()

    if num == 4:
        rs_position = [72,884]
        screen.blit(star, rs_position)
        pygame.display.update()

    if num == 3:
        ys_position = [586,884]
        screen.blit(star, ys_position)
        pygame.display.update()

    if num == 2:
        s_position = [47,719]
        screen.blit(sc, s_position)
        pygame.display.update()
    if num == 1:
        s2_position = [564,719]
        screen.blit(sc, s2_position)
        pygame.display.update()


def odds_animation(num):
    global screen
    if num == 10:
        odds_position = [159,397]
        screen.blit(o, odds_position)
        pygame.display.update()
    if num == 9:
        odds_position = [212,397]
        screen.blit(o, odds_position)
        pygame.display.update()
    if num == 8:
        odds_position = [265,397]
        screen.blit(o, odds_position)
        pygame.display.update()
    if num == 7:
        odds_position = [318,397]
        screen.blit(o, odds_position)
        pygame.display.update()
    if num == 6:
        odds_position = [370,397]
        screen.blit(o, odds_position)
        pygame.display.update()
    if num == 5:
        odds_position = [421,397]
        screen.blit(o, odds_position)
        pygame.display.update()
    if num == 4:
        odds_position = [474,397]
        screen.blit(o, odds_position)
        pygame.display.update()
    if num == 3:
        odds_position = [526,397]
        screen.blit(o, odds_position)
        pygame.display.update()
    if num == 2:
        odds_position = [578,397]
        screen.blit(o, odds_position)
        pygame.display.update()
    if num == 1:
        odds_position = [631,397]
        screen.blit(o10, odds_position)
        pygame.display.update()
