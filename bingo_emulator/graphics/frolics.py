
import pygame, random

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

meter = pygame.image.load('graphics/assets/register_cover.png').convert()
card = pygame.image.load('frolics/assets/card.png').convert_alpha()
odds1 = pygame.image.load('frolics/assets/odds1.png').convert_alpha()
odds2 = pygame.image.load('frolics/assets/odds2.png').convert_alpha()
odds3 = pygame.image.load('frolics/assets/odds3.png').convert_alpha()
odds4 = pygame.image.load('frolics/assets/odds4.png').convert_alpha()
odds5 = pygame.image.load('frolics/assets/odds5.png').convert_alpha()
super_score = pygame.image.load('frolics/assets/super.png').convert_alpha()
star = pygame.image.load('frolics/assets/star.png').convert_alpha()
top_score = pygame.image.load('frolics/assets/top_score.png').convert_alpha()
extra_balls = pygame.image.load('frolics/assets/extra_balls.png').convert_alpha()
i = pygame.image.load('frolics/assets/eb.png').convert_alpha()
number = pygame.image.load('frolics/assets/number.png').convert_alpha()
tilt = pygame.image.load('frolics/assets/tilt.png').convert_alpha()


class scorereel():
    """ Score Reels are used to count replays """
    def __init__(self, pos, image):
        self.position = pos
        self.default_y = self.position[1]
        self.image = pygame.image.load(image).convert()

reel1 = scorereel([107,880], "graphics/assets/green_reel.png")
reel10 = scorereel([87,880], "graphics/assets/green_reel.png")
reel100 = scorereel([67,880], "graphics/assets/green_reel.png")

def display(s, replays=0, menu=False):
    
    meter.set_colorkey((255,0,252))
    meter_position = [58,880]

    screen.blit(reel1.image, reel1.position)
    screen.blit(reel10.image, reel10.position)
    screen.blit(reel100.image, reel100.position)
    screen.blit(meter, meter_position)

    backglass_position = [0, 0]
    backglass = pygame.Surface((0,0), pygame.SRCALPHA)
    backglass.fill((0, 0, 0))
    if menu == True:
        backglass = pygame.image.load('frolics/assets/frolics_menu.png')
    else:
        if (s.game.anti_cheat.status == True):
            backglass = pygame.image.load('frolics/assets/frolics_gi.png')
        else:
            backglass = pygame.image.load('frolics/assets/frolics_off.png')
    screen.blit(backglass, backglass_position)

    if s.game.selector.position >= 1:
        card1_position = [86,279]
        screen.blit(card, card1_position)
    if s.game.selector.position >= 2:
        card2_position = [309,279]
        screen.blit(card, card2_position)
    if s.game.selector.position >= 3:
        card3_position = [533,279]
        screen.blit(card, card3_position)
    if s.game.selector.position >= 4:
        card4_position = [86,529]
        screen.blit(card, card4_position)
    if s.game.selector.position >= 5:
        card5_position = [309,529]
        screen.blit(card, card5_position)
    if s.game.selector.position >= 6:
        card6_position = [532,529]
        screen.blit(card, card6_position)

    if s.game.odds.position == 1:
        p = [176,778]
        screen.blit(odds1, p)
    if s.game.odds.position == 2:
        p = [253,775]
        screen.blit(odds2, p)
    if s.game.odds.position == 3:
        p = [325,775]
        screen.blit(odds3, p)
    if s.game.odds.position == 4:
        p = [393,775]
        screen.blit(odds4, p)
    if s.game.odds.position == 5:
        p = [468,778]
        screen.blit(odds5, p)

    if s.game.super1.status == True:
        p = [66,305]
        screen.blit(super_score, p)
    if s.game.super2.status == True:
        p = [289,305]
        screen.blit(super_score, p)
    if s.game.super3.status == True:
        p = [511,305]
        screen.blit(super_score, p)
    if s.game.super4.status == True:
        p = [65,555]
        screen.blit(super_score, p)
    if s.game.super5.status == True:
        p = [287,555]
        screen.blit(super_score, p)
    if s.game.super6.status == True:
        p = [509,555]
        screen.blit(super_score, p)

    if s.game.red_star.status == True:
        p = [573,824]
        screen.blit(star, p)

    if s.game.yellow_star.status == True:
        p = [632,824]
        screen.blit(star, p)

    if s.game.top_score.status == True:
        p = [569,871]
        screen.blit(top_score, p)

    if s.game.eb_play.status == True:
        p = [284,997]
        screen.blit(extra_balls, p)

    if s.game.extra_ball.position >= 1:
        p = [82,1029]
        screen.blit(i, p)
    if s.game.extra_ball.position >= 2:
        p = [169,1029]
        screen.blit(i, p)
    if s.game.extra_ball.position >= 3:
        p = [256,1029]
        screen.blit(i, p)
    if s.game.extra_ball.position >= 4:
        p = [378,1029]
        screen.blit(i, p)
    if s.game.extra_ball.position >= 5:
        p = [464,1029]
        screen.blit(i, p)
    if s.game.extra_ball.position >= 6:
        p = [550,1029]
        screen.blit(i, p)


    if s.game.tilt.status == False:
        if s.holes:
            if 1 in s.holes:
                number_position = [90,348]
                screen.blit(number, number_position)
                number_position = [278,449]
                screen.blit(number, number_position)
                number_position = [603,481]
                screen.blit(number, number_position)
                number_position = [123,633]
                screen.blit(number, number_position)
                number_position = [313,599]
                screen.blit(number, number_position)
                number_position = [500,698]
                screen.blit(number, number_position)
            if 2 in s.holes:
                number_position = [122,480]
                screen.blit(number, number_position)
                number_position = [279,415]
                screen.blit(number, number_position)
                number_position = [636,416]
                screen.blit(number, number_position)
                number_position = [189,699]
                screen.blit(number, number_position)
                number_position = [312,732]
                screen.blit(number, number_position)
                number_position = [601,732]
                screen.blit(number, number_position)

            if 3 in s.holes:
                number_position = [190,348]
                screen.blit(number, number_position)
                number_position = [412,482]
                screen.blit(number, number_position)
                number_position = [502,348]
                screen.blit(number, number_position)
                number_position = [156,632]
                screen.blit(number, number_position)
                number_position = [378,698]
                screen.blit(number, number_position)
                number_position = [534,632]
                screen.blit(number, number_position)

            if 4 in s.holes:
                number_position = [156,481]
                screen.blit(number, number_position)
                number_position = [379,349]
                screen.blit(number, number_position)
                number_position = [602,348]
                screen.blit(number, number_position)
                number_position = [54,698]
                screen.blit(number, number_position)
                number_position = [278,632]
                screen.blit(number, number_position)
                number_position = [501,632]
                screen.blit(number, number_position)
            if 5 in s.holes:
                number_position = [56,347]
                screen.blit(number, number_position)
                number_position = [346,481]
                screen.blit(number, number_position)
                number_position = [636,481]
                screen.blit(number, number_position)
                number_position = [89,632]
                screen.blit(number, number_position)
                number_position = [412,698]
                screen.blit(number, number_position)
                number_position = [601,698]
                screen.blit(number, number_position)
            if 6 in s.holes:
                number_position = [56,414]
                screen.blit(number, number_position)
                number_position = [413,348]
                screen.blit(number, number_position)
                number_position = [502,482]
                screen.blit(number, number_position)
                number_position = [89,732]
                screen.blit(number, number_position)
                number_position = [378,632]
                screen.blit(number, number_position)
                number_position = [534,698]
                screen.blit(number, number_position)

            if 7 in s.holes:
                number_position = [190,380]
                screen.blit(number, number_position)
                number_position = [312,482]
                screen.blit(number, number_position)
                number_position = [536,348]
                screen.blit(number, number_position)
                number_position = [156,666]
                screen.blit(number, number_position)
                number_position = [346,698]
                screen.blit(number, number_position)
                number_position = [568,632]
                screen.blit(number, number_position)

            if 8 in s.holes:
                number_position = [56,381]
                screen.blit(number, number_position)
                number_position = [412,448]
                screen.blit(number, number_position)
                number_position = [636,382]
                screen.blit(number, number_position)
                number_position = [89,665]
                screen.blit(number, number_position)
                number_position = [379,599]
                screen.blit(number, number_position)
                number_position = [602,665]
                screen.blit(number, number_position)

            if 9 in s.holes:
                number_position = [123,348]
                screen.blit(number, number_position)
                number_position = [279,348]
                screen.blit(number, number_position)
                number_position = [636,348]
                screen.blit(number, number_position)
                number_position = [190,632]
                screen.blit(number, number_position)
                number_position = [312,632]
                screen.blit(number, number_position)
                number_position = [601,632]
                screen.blit(number, number_position)

            if 10 in s.holes:
                number_position = [123,381]
                screen.blit(number, number_position)
                number_position = [278,482]
                screen.blit(number, number_position)
                number_position = [569,348]
                screen.blit(number, number_position)
                number_position = [190,666]
                screen.blit(number, number_position)
                number_position = [312,698]
                screen.blit(number, number_position)
                number_position = [634,632]
                screen.blit(number, number_position)

            if 11 in s.holes:
                number_position = [154,414]
                screen.blit(number, number_position)
                number_position = [346,448]
                screen.blit(number, number_position)
                number_position = [603,415]
                screen.blit(number, number_position)
                number_position = [56,732]
                screen.blit(number, number_position)
                number_position = [413,598]
                screen.blit(number, number_position)
                number_position = [500,732]
                screen.blit(number, number_position)

            if 12 in s.holes:
                number_position = [56,480]
                screen.blit(number, number_position)
                number_position = [380,415]
                screen.blit(number, number_position)
                number_position = [569,448]
                screen.blit(number, number_position)
                number_position = [89,699]
                screen.blit(number, number_position)
                number_position = [278,732]
                screen.blit(number, number_position)
                number_position = [634,598]
                screen.blit(number, number_position)

            if 13 in s.holes:
                number_position = [189,448]
                screen.blit(number, number_position)
                number_position = [280,382]
                screen.blit(number, number_position)
                number_position = [502,448]
                screen.blit(number, number_position)
                number_position = [156,599]
                screen.blit(number, number_position)
                number_position = [312,665]
                screen.blit(number, number_position)
                number_position = [536,598]
                screen.blit(number, number_position)

            if 14 in s.holes:
                number_position = [123,448]
                screen.blit(number, number_position)
                number_position = [346,382]
                screen.blit(number, number_position)
                number_position = [536,415]
                screen.blit(number, number_position)
                number_position = [190,599]
                screen.blit(number, number_position)
                number_position = [413,666]
                screen.blit(number, number_position)
                number_position = [568,732]
                screen.blit(number, number_position)

            if 15 in s.holes:
                number_position = [190,482]
                screen.blit(number, number_position)
                number_position = [346,414]
                screen.blit(number, number_position)
                number_position = [502,415]
                screen.blit(number, number_position)
                number_position = [156,698]
                screen.blit(number, number_position)
                number_position = [412,732]
                screen.blit(number, number_position)
                number_position = [534,732]
                screen.blit(number, number_position)

            if 16 in s.holes:
                number_position = [123,414]
                screen.blit(number, number_position)
                number_position = [346,348]
                screen.blit(number, number_position)
                number_position = [568,482]
                screen.blit(number, number_position)
                number_position = [188,732]
                screen.blit(number, number_position)
                number_position = [412,632]
                screen.blit(number, number_position)
                number_position = [634,698]
                screen.blit(number, number_position)

            if 17 in s.holes:
                number_position = [190,414]
                screen.blit(number, number_position)
                number_position = [412,414]
                screen.blit(number, number_position)
                number_position = [568,414]
                screen.blit(number, number_position)
                number_position = [156,732]
                screen.blit(number, number_position)
                number_position = [379,732]
                screen.blit(number, number_position)
                number_position = [634,732]
                screen.blit(number, number_position)

            if 18 in s.holes:
                number_position = [90,414]
                screen.blit(number, number_position)
                number_position = [313,415]
                screen.blit(number, number_position)
                number_position = [569,382]
                screen.blit(number, number_position)
                number_position = [122,733]
                screen.blit(number, number_position)
                number_position = [344,732]
                screen.blit(number, number_position)
                number_position = [635,665]
                screen.blit(number, number_position)

            if 19 in s.holes:
                number_position = [157,382]
                screen.blit(number, number_position)
                number_position = [313,382]
                screen.blit(number, number_position)
                number_position = [602,449]
                screen.blit(number, number_position)
                number_position = [55,666]
                screen.blit(number, number_position)
                number_position = [346,666]
                screen.blit(number, number_position)
                number_position = [500,598]
                screen.blit(number, number_position)

            if 20 in s.holes:
                number_position = [157,448]
                screen.blit(number, number_position)
                number_position = [379,382]
                screen.blit(number, number_position)
                number_position = [535,448]
                screen.blit(number, number_position)
                number_position = [55,599]
                screen.blit(number, number_position)
                number_position = [278,665]
                screen.blit(number, number_position)
                number_position = [568,598]
                screen.blit(number, number_position)

            if 21 in s.holes:
                number_position = [90,448]
                screen.blit(number, number_position)
                number_position = [380,448]
                screen.blit(number, number_position)
                number_position = [536,382]
                screen.blit(number, number_position)
                number_position = [123,599]
                screen.blit(number, number_position)
                number_position = [278,599]
                screen.blit(number, number_position)
                number_position = [568,665]
                screen.blit(number, number_position)

            if 22 in s.holes:
                number_position = [89,381]
                screen.blit(number, number_position)
                number_position = [313,447]
                screen.blit(number, number_position)
                number_position = [602,381]
                screen.blit(number, number_position)
                number_position = [122,665]
                screen.blit(number, number_position)
                number_position = [345,598]
                screen.blit(number, number_position)
                number_position = [501,664]
                screen.blit(number, number_position)

            if 23 in s.holes:
                number_position = [90,482]
                screen.blit(number, number_position)
                number_position = [380,482]
                screen.blit(number, number_position)
                number_position = [636,448]
                screen.blit(number, number_position)
                number_position = [123,699]
                screen.blit(number, number_position)
                number_position = [279,698]
                screen.blit(number, number_position)
                number_position = [602,599]
                screen.blit(number, number_position)

            if 24 in s.holes:
                number_position = [56,448]
                screen.blit(number, number_position)
                number_position = [314,348]
                screen.blit(number, number_position)
                number_position = [502,381]
                screen.blit(number, number_position)
                number_position = [90,599]
                screen.blit(number, number_position)
                number_position = [346,632]
                screen.blit(number, number_position)
                number_position = [535,666]
                screen.blit(number, number_position)

            if 25 in s.holes:
                number_position = [157,348]
                screen.blit(number, number_position)
                number_position = [414,382]
                screen.blit(number, number_position)
                number_position = [536,482]
                screen.blit(number, number_position)
                number_position = [56,632]
                screen.blit(number, number_position)
                number_position = [379,665]
                screen.blit(number, number_position)
                number_position = [568,699]
                screen.blit(number, number_position)


    if s.game.tilt.status == True:
        tilt_position = [577,215]
        screen.blit(tilt, tilt_position)

    pygame.display.flip()
    pygame.display.update()

def eb_animation(num):
    global screen
    if num == 6:
        p = [82,1029]
        screen.blit(i, p)
        pygame.display.update()
    if num == 5:
        p = [169,1029]
        screen.blit(i, p)
        pygame.display.update()
    if num == 4:
        p = [256,1027]
        screen.blit(i, p)
        pygame.display.update()
    if num == 3:
        p = [378,1029]
        screen.blit(i, p)
        pygame.display.update()
    if num == 2:
        p = [464,1029]
        screen.blit(i, p)
        pygame.display.update()
    if num == 1:
        p = [550,1029]
        screen.blit(i, p)
        pygame.display.update()

def feature_animation(num):
    global screen
    if num == 5:
        p = [176,778]
        screen.blit(odds1, p)
        pygame.display.update()
    if num == 4:
        p = [253,778]
        i = pygame.image.load('frolics/assets/odds2.png').convert_alpha()
        screen.blit(odds2, p)
        pygame.display.update()
    if num == 3:
        p = [325,778]
        screen.blit(odds3, p)
        pygame.display.update()
    if num == 2:
        p = [393,775]
        screen.blit(odds4, p)
        pygame.display.update()
    if num == 1:
        p = [468,778]
        screen.blit(odds5, p)
        pygame.display.update()

