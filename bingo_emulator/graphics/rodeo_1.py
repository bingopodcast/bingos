
import pygame
import random

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

meter = pygame.image.load('graphics/assets/silver_register_cover.png').convert()
arrow = pygame.image.load('rodeo_1/assets/arrow.png').convert_alpha()
r_name = pygame.image.load('rodeo_1/assets/r_name.png').convert_alpha()
o_name = pygame.image.load('rodeo_1/assets/o_name.png').convert_alpha()
d_name = pygame.image.load('rodeo_1/assets/d_name.png').convert_alpha()
e_name = pygame.image.load('rodeo_1/assets/e_name.png').convert_alpha()
o2_name = pygame.image.load('rodeo_1/assets/o2_name.png').convert_alpha()
eb = pygame.image.load('rodeo_1/assets/extra_ball.png').convert_alpha()
exb = pygame.image.load('rodeo_1/assets/extra_balls.png').convert_alpha()
og = pygame.image.load('rodeo_1/assets/odds_gi.png').convert_alpha()
o10 = pygame.image.load('rodeo_1/assets/odds_10.png').convert_alpha()
o = pygame.image.load('rodeo_1/assets/odds_1.png').convert_alpha()
o2 = pygame.image.load('rodeo_1/assets/odds_2.png').convert_alpha()
o3 = pygame.image.load('rodeo_1/assets/odds_3.png').convert_alpha()
o4 = pygame.image.load('rodeo_1/assets/odds_4.png').convert_alpha()
o5 = pygame.image.load('rodeo_1/assets/odds_5.png').convert_alpha()
o6 = pygame.image.load('rodeo_1/assets/odds_6.png').convert_alpha()
o7 = pygame.image.load('rodeo_1/assets/odds_7.png').convert_alpha()
o8 = pygame.image.load('rodeo_1/assets/odds_8.png').convert_alpha()
o9 = pygame.image.load('rodeo_1/assets/odds_9.png').convert_alpha()
sc = pygame.image.load('rodeo_1/assets/super_card.png').convert_alpha()
star = pygame.image.load('rodeo_1/assets/star.png').convert_alpha()
c = pygame.image.load('rodeo_1/assets/corners.png').convert_alpha()
number = pygame.image.load('rodeo_1/assets/number.png').convert_alpha()
sc_number = pygame.image.load('rodeo_1/assets/sc_number.png').convert_alpha()
tilt = pygame.image.load('rodeo_1/assets/tilt.png').convert_alpha()
oo = pygame.image.load('rodeo_1/assets/play.png').convert_alpha()
f = pygame.image.load('rodeo_1/assets/play.png').convert_alpha()
ebs = pygame.image.load('rodeo_1/assets/extra_balls.png').convert_alpha()
lan = pygame.image.load('rodeo_1/assets/liteaname.png').convert_alpha()
three_as_four = pygame.image.load('rodeo_1/assets/3_as_4.png').convert_alpha()
four_as_five = pygame.image.load('rodeo_1/assets/4_as_5.png').convert_alpha()
eight_balls = pygame.image.load('rodeo_1/assets/eight_balls.png').convert_alpha()

class scorereel():
    """ Score Reels are used to count replays """
    def __init__(self, pos, image):
        self.position = pos
        self.default_y = self.position[1]
        self.image = pygame.image.load(image).convert()

reel1 = scorereel([104,605], "graphics/assets/white_reel.png")
reel10 = scorereel([84,605], "graphics/assets/white_reel.png")
reel100 = scorereel([66,605], "graphics/assets/white_reel.png")

def display(s, replays=0, menu=False):
    
    meter.set_colorkey((255,0,252))
    meter_position = [56,604]

    screen.blit(reel1.image, reel1.position)
    screen.blit(reel10.image, reel10.position)
    screen.blit(reel100.image, reel100.position)
    screen.blit(meter, meter_position)

    backglass_position = [0, 0]
    backglass = pygame.Surface(screen.get_size(), flags=pygame.SRCALPHA)
    backglass.fill((0, 0, 0))
    if menu == True:
        backglass = pygame.image.load('rodeo_1/assets/rodeo_1_menu.png')
    else:
        if (s.game.anti_cheat.status == True):
            backglass = pygame.image.load('rodeo_1/assets/rodeo_1_gi.png')
        else:
            backglass = pygame.image.load('rodeo_1/assets/rodeo_1_off.png')
    backglass = pygame.transform.scale(backglass, (720, 1280))
    
    screen.blit(backglass, backglass_position)

    if s.game.extra_ball.position == 1 or s.game.extra_ball.position == 10:
        eb_position = [53,995]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 2 or s.game.extra_ball.position == 11:
        eb_position = [124,995]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 3 or s.game.extra_ball.position == 12:
        eb_position = [197,993]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 4 or s.game.extra_ball.position == 13 or s.game.extra_ball.position == 19:
        eb_position = [270,993]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 5 or s.game.extra_ball.position == 14 or s.game.extra_ball.position == 20:
        eb_position = [343,994]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 6 or s.game.extra_ball.position == 15 or s.game.extra_ball.position == 21:
        eb_position = [416,993]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 7 or s.game.extra_ball.position == 16 or s.game.extra_ball.position == 22:
        eb_position = [489,993]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 8 or s.game.extra_ball.position == 17 or s.game.extra_ball.position == 23:
        eb_position = [561,994]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 9 or s.game.extra_ball.position == 18 or s.game.extra_ball.position == 24:
        eb_position = [631,993]
        screen.blit(eb, eb_position)

    if s.game.extra_ball.position >= 9:
        eb_position = [41,1043]
        screen.blit(exb, eb_position)
    if s.game.extra_ball.position >= 18:
        eb_position = [260,1042]
        screen.blit(exb, eb_position)
    if s.game.extra_ball.position >= 24:
        eb_position = [477,1041]
        screen.blit(exb, eb_position)

    if s.game.odds.position > 0:
        odds_position = [7,287]
        screen.blit(og, odds_position)
        if s.game.odds.position == 1:
            odds_position = [153,335]
            screen.blit(o, odds_position)
        if s.game.odds.position == 2:
            odds_position = [209,345]
            screen.blit(o2, odds_position)
        if s.game.odds.position == 3:
            odds_position = [263,353]
            screen.blit(o3, odds_position)
        if s.game.odds.position == 4:
            odds_position = [319,358]
            screen.blit(o4, odds_position)
        if s.game.odds.position == 5:
            odds_position = [374,359]
            screen.blit(o5, odds_position)
        if s.game.odds.position == 6:
            odds_position = [430,355]
            screen.blit(o6, odds_position)
        if s.game.odds.position == 7:
            odds_position = [485,349]
            screen.blit(o7, odds_position)
        if s.game.odds.position == 8:
            odds_position = [540,334]
            screen.blit(o8, odds_position)
        if s.game.odds.position == 9:
            odds_position = [595,321]
            screen.blit(o9, odds_position)
        if s.game.odds.position == 10:
            odds_position = [649,299]
            screen.blit(o10, odds_position)

    if s.game.super_card.position > 0:
        if s.game.super_card.position == 1:
            sc_position = [34,953]
            screen.blit(arrow, sc_position)
        if s.game.super_card.position == 2:
            sc_position = [67,953]
            screen.blit(arrow, sc_position)
        if s.game.super_card.position == 3:
            sc_position = [101,953]
            screen.blit(arrow, sc_position)
        if s.game.super_card.position == 4:
            sc_position = [135,955]
            screen.blit(arrow, sc_position)
        if s.game.super_card.position == 5:
            sc_position = [560,953]
            screen.blit(arrow, sc_position)
        if s.game.super_card.position == 6:
            sc_position = [594,953]
            screen.blit(arrow, sc_position)
        if s.game.super_card.position == 7:
            sc_position = [627,953]
            screen.blit(arrow, sc_position)
        if s.game.super_card.position == 8:
            sc_position = [660,953]
            screen.blit(arrow, sc_position)
        if s.game.super_card.position >= 4:
            s_position = [47,917]
            screen.blit(sc, s_position)
        if s.game.super_card.position >= 8:
            s2_position = [573,916]
            screen.blit(sc, s2_position)

    if s.game.red_star.status == True:
        rs_position = [471,916]
        screen.blit(star, rs_position)

    if s.game.yellow_star.status == True:
        ys_position = [185,916]
        screen.blit(star, ys_position)

    if s.game.corners.status == True:
        corners_position = [572,582]
        screen.blit(c, corners_position)

    if s.game.tilt.status == False:
        if s.holes:
            if 1 in s.holes:
                number_position = [206,706]
                screen.blit(number, number_position)
                number_position = [35,798]
                screen.blit(sc_number, number_position)
            if 2 in s.holes:
                number_position = [208,773]
                screen.blit(number, number_position)
            if 3 in s.holes:
                number_position = [460,839]
                screen.blit(number, number_position)
                number_position = [607,750]
                screen.blit(sc_number, number_position)
            if 4 in s.holes:
                number_position = [332,573]
                screen.blit(number, number_position)
                number_position = [78,845]
                screen.blit(sc_number, number_position)
            if 5 in s.holes:
                number_position = [397,840]
                screen.blit(number, number_position)
            if 6 in s.holes:
                number_position = [462,572]
                screen.blit(number, number_position)
            if 7 in s.holes:
                number_position = [269,839]
                screen.blit(number, number_position)
                number_position = [78,752]
                screen.blit(sc_number, number_position)
            if 8 in s.holes:
                number_position = [463,707]
                screen.blit(number, number_position)
            if 9 in s.holes:
                number_position = [206,573]
                screen.blit(number, number_position)
                number_position = [563,796]
                screen.blit(sc_number, number_position)
            if 10 in s.holes:
                number_position = [207,841]
                screen.blit(number, number_position)
                number_position = [77,797]
                screen.blit(sc_number, number_position)
            if 11 in s.holes:
                number_position = [334,773]
                screen.blit(number, number_position)
                number_position = [648,796]
                screen.blit(sc_number, number_position)
            if 12 in s.holes:
                number_position = [397,706]
                screen.blit(number, number_position)
                number_position = [563,842]
                screen.blit(sc_number, number_position)
            if 13 in s.holes:
                number_position = [205,639]
                screen.blit(number, number_position)
                number_position = [121,798]
                screen.blit(sc_number, number_position)
            if 14 in s.holes:
                number_position = [334,639]
                screen.blit(number, number_position)
                number_position = [648,842]
                screen.blit(sc_number, number_position)
            if 15 in s.holes:
                number_position = [269,573]
                screen.blit(number, number_position)
            if 16 in s.holes:
                number_position = [333,706]
                screen.blit(number, number_position)
            if 17 in s.holes:
                number_position = [462,639]
                screen.blit(number, number_position)
            if 18 in s.holes:
                number_position = [271,706]
                screen.blit(number, number_position)
                number_position = [649,750]
                screen.blit(sc_number, number_position)
            if 19 in s.holes:
                number_position = [270,641]
                screen.blit(number, number_position)
                number_position = [34,751]
                screen.blit(sc_number, number_position)
            if 20 in s.holes:
                number_position = [397,639]
                screen.blit(number, number_position)
                number_position = [123,752]
                screen.blit(sc_number, number_position)
            if 21 in s.holes:
                number_position = [397,774]
                screen.blit(number, number_position)
                number_position = [122,844]
                screen.blit(sc_number, number_position)
            if 22 in s.holes:
                number_position = [270,774]
                screen.blit(number, number_position)
                number_position = [35,844]
                screen.blit(sc_number, number_position)
            if 23 in s.holes:
                number_position = [333,842]
                screen.blit(number, number_position)
                number_position = [563,750]
                screen.blit(sc_number, number_position)
            if 24 in s.holes:
                number_position = [398,570]
                screen.blit(number, number_position)
                number_position = [605,843]
                screen.blit(sc_number, number_position)
            if 25 in s.holes:
                number_position = [460,773]
                screen.blit(number, number_position)
                number_position = [606,796]
                screen.blit(sc_number, number_position)

    if s.game.name.position >= 1:
        n_position = [216,243]
        screen.blit(r_name, n_position)
    if s.game.name.position >= 2:
        n_position = [273,254]
        screen.blit(o_name, n_position)
    if s.game.name.position >= 3:
        n_position = [341,257]
        screen.blit(d_name, n_position)
    if s.game.name.position >= 4:
        n_position = [404,255]
        screen.blit(e_name, n_position)
    if s.game.name.position >= 5:
        n_position = [459,249]
        screen.blit(o2_name, n_position)

    if s.game.eight_balls.status == True:
        eb_position = [260,316]
        screen.blit(eight_balls, eb_position)
    if s.game.three_as_four.status == True:
        t_position = [49,269]
        screen.blit(three_as_four, t_position)
    if s.game.four_as_five.status == True:
        f_position = [472,271]
        screen.blit(four_as_five, f_position)

    if s.game.liteaname.status == True:
        lan_position = [565,505]
        screen.blit(lan, lan_position)

    if s.game.tilt.status == True:
        tilt_position = [48,507]
        screen.blit(tilt, tilt_position)

    if s.game.odds_only.status == True:
        oo_position = [256,923]
        screen.blit(oo, oo_position)

    if s.game.features.status == True:
        f_position = [326,923]
        screen.blit(f, f_position)

    if s.game.eb.status == True:
        ebs_position = [395,923]
        screen.blit(f, ebs_position)

    pygame.display.update()

def eb_animation(num):
    global screen
    if num == 24 or num == 15:
        eb_position = [53,995]
        pygame.display.update(screen.blit(eb, eb_position))
    if num == 23 or num == 14:
        eb_position = [124,995]
        pygame.display.update(screen.blit(eb, eb_position))
    if num == 22 or num == 13:
        eb_position = [197,993]
        pygame.display.update(screen.blit(eb, eb_position))
    if num == 21 or num == 12 or num == 6:
        eb_position = [270,993]
        pygame.display.update(screen.blit(eb, eb_position))
    if num == 20 or num == 11 or num == 5:
        eb_position = [343,994]
        pygame.display.update(screen.blit(eb, eb_position))
    if num == 19 or num == 10 or num == 4:
        eb_position = [416,993]
        pygame.display.update(screen.blit(eb, eb_position))
    if num == 18 or num == 9 or num == 3:
        eb_position = [489,993]
        pygame.display.update(screen.blit(eb, eb_position))
    if num == 17 or num == 8 or num == 2:
        eb_position = [561,994]
        pygame.display.update(screen.blit(eb, eb_position))
    if num == 16 or num == 7 or num == 1:
        eb_position = [631,993]
        pygame.display.update(screen.blit(eb, eb_position))

def feature_animation(num):
    global screen

    if num == 5:
        corners_position = [572,582]
        screen.blit(c, corners_position)
        pygame.display.update()

    if num == 4:
        rs_position = [471,916]
        screen.blit(star, rs_position)
        pygame.display.update()

    if num == 3:
        ys_position = [185,916]
        screen.blit(star, ys_position)
        pygame.display.update()

    if num == 2:
        s_position = [47,917]
        screen.blit(sc, s_position)
        pygame.display.update()
    if num == 1:
        s2_position = [573,916]
        screen.blit(sc, s2_position)
        pygame.display.update()


def odds_animation(num):
    global screen
    if num == 10:
        odds_position = [153,335]
        pygame.display.update(screen.blit(o, odds_position))
    if num == 9:
        odds_position = [209,345]
        pygame.display.update(screen.blit(o2, odds_position))
    if num == 8:
        odds_position = [263,353]
        pygame.display.update(screen.blit(o3, odds_position))
    if num == 7:
        odds_position = [319,358]
        pygame.display.update(screen.blit(o4, odds_position))
    if num == 6:
        odds_position = [374,359]
        pygame.display.update(screen.blit(o5, odds_position))
    if num == 5:
        odds_position = [430,355]
        pygame.display.update(screen.blit(o6, odds_position))
    if num == 4:
        odds_position = [485,349]
        pygame.display.update(screen.blit(o7, odds_position))
    if num == 3:
        odds_position = [540,334]
        pygame.display.update(screen.blit(o8, odds_position))
    if num == 2:
        odds_position = [595,321]
        pygame.display.update(screen.blit(o9, odds_position))
    if num == 1:
        odds_position = [649,299]
        pygame.display.update(screen.blit(o10, odds_position))
