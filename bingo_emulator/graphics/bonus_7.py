
import pygame
import random

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

meter = pygame.image.load('graphics/assets/black_register_cover.png').convert()
odds = pygame.image.load('bonus_7/assets/odds.png').convert_alpha()
eb = pygame.image.load('bonus_7/assets/eb.png').convert_alpha()
eb_number = pygame.image.load('bonus_7/assets/eb_number.png').convert_alpha()
extra_balls = pygame.image.load('bonus_7/assets/extra_balls.png').convert_alpha()
time = pygame.image.load('bonus_7/assets/time.png').convert_alpha()
ml_letter = pygame.image.load('bonus_7/assets/ml_letter.png').convert_alpha()
ml_arrow = pygame.image.load('bonus_7/assets/ml_arrow.png').convert_alpha()
ml_a = pygame.image.load('bonus_7/assets/ml_a.png').convert_alpha()
ml_b = pygame.image.load('bonus_7/assets/ml_b.png').convert_alpha()
ml_c = pygame.image.load('bonus_7/assets/ml_c.png').convert_alpha()
select_now = pygame.image.load('bonus_7/assets/select_now.png').convert_alpha()
tilt = pygame.image.load('bonus_7/assets/tilt.png').convert_alpha()
button = pygame.image.load('bonus_7/assets/pap.png').convert_alpha()
red_double = pygame.image.load('bonus_7/assets/red_double.png').convert_alpha()
green_double = pygame.image.load('bonus_7/assets/green_double.png').convert_alpha()
yellow_double = pygame.image.load('bonus_7/assets/yellow_double.png').convert_alpha()
blue_double = pygame.image.load('bonus_7/assets/blue_double.png').convert_alpha()
four_stars = pygame.image.load('bonus_7/assets/four_stars.png').convert_alpha()
six_stars = pygame.image.load('bonus_7/assets/six_stars.png').convert_alpha()
three_stars = pygame.image.load('bonus_7/assets/three_stars.png').convert_alpha()
three_red = pygame.image.load('bonus_7/assets/three_red.png').convert_alpha()
two_red = pygame.image.load('bonus_7/assets/two_red.png').convert_alpha()
red_letter = pygame.image.load('bonus_7/assets/red_letter.png').convert_alpha()
letter1 = pygame.image.load('bonus_7/assets/letter1.png').convert_alpha()
letter2 = pygame.image.load('bonus_7/assets/letter2.png').convert_alpha()
letter3 = pygame.image.load('bonus_7/assets/letter3.png').convert_alpha()
letter4 = pygame.image.load('bonus_7/assets/letter4.png').convert_alpha()
letter5 = pygame.image.load('bonus_7/assets/letter5.png').convert_alpha()
letter6 = pygame.image.load('bonus_7/assets/letter6.png').convert_alpha()
red_letter1 = pygame.image.load('bonus_7/assets/red_letter1.png').convert_alpha()
red_letter2 = pygame.image.load('bonus_7/assets/red_letter2.png').convert_alpha()
red_letter3 = pygame.image.load('bonus_7/assets/red_letter3.png').convert_alpha()
red_letter4 = pygame.image.load('bonus_7/assets/red_letter4.png').convert_alpha()
red_letter5 = pygame.image.load('bonus_7/assets/red_letter5.png').convert_alpha()
red_letter6 = pygame.image.load('bonus_7/assets/red_letter6.png').convert_alpha()
number_card = pygame.image.load('bonus_7/assets/number_card.png').convert_alpha()
number = pygame.image.load('bonus_7/assets/number.png').convert_alpha()
columnb1 = pygame.image.load('bonus_7/assets/columnb1.png').convert_alpha()
columnb2 = pygame.image.load('bonus_7/assets/columnb2.png').convert_alpha()
columna = pygame.image.load('bonus_7/assets/columna.png').convert_alpha()
columnc1 = pygame.image.load('bonus_7/assets/columnc1.png').convert_alpha()
columnc2 = pygame.image.load('bonus_7/assets/columnc2.png').convert_alpha()
double_triple = pygame.image.load('bonus_7/assets/double_triple.png').convert_alpha()
collected = pygame.image.load('bonus_7/assets/collected.png').convert_alpha()
special_odds = pygame.image.load('bonus_7/assets/special_odds.png').convert_alpha()
twin_number = pygame.image.load('bonus_7/assets/twin_number.png').convert_alpha()
seven_odds = pygame.image.load('bonus_7/assets/seven_odds.png').convert_alpha()
diamond = pygame.image.load('bonus_7/assets/diamond.png').convert_alpha()
diamond_7 = pygame.image.load('bonus_7/assets/diamond_7.png').convert_alpha()
ball = pygame.image.load('bonus_7/assets/ball.png').convert_alpha()
suns = pygame.image.load('bonus_7/assets/suns.png').convert_alpha()
three_suns = pygame.image.load('bonus_7/assets/three_suns.png').convert_alpha()
top_odds = pygame.image.load('bonus_7/assets/top_odds.png').convert_alpha()


class scorereel():
    """ Score Reels are used to count replays """
    def __init__(self, pos, image):
        self.position = pos
        self.default_y = self.position[1]
        self.image = pygame.image.load(image).convert()

reel1 = scorereel([110,797], "graphics/assets/white_reel.png")
reel10 = scorereel([91,797], "graphics/assets/white_reel.png")
reel100 = scorereel([72,797], "graphics/assets/white_reel.png")
reel1000 = scorereel([53,797], "graphics/assets/white_reel.png")

def display(s, replays=0, menu=False):
    
    meter.set_colorkey((255,0,252))
    meter_position = [44,797]

    screen.blit(reel1.image, reel1.position)
    screen.blit(reel10.image, reel10.position)
    screen.blit(reel100.image, reel100.position)
    screen.blit(reel1000.image, reel1000.position)
    screen.blit(meter, meter_position)

    if s.game.line2.position == 0:
        p = [233,368]
        screen.blit(columnb1, p)
        p = [284,369]
        screen.blit(columnb2, p)
    else:
        p = [233,368]
        screen.blit(columnb2, p)
        p = [284,369]
        screen.blit(columnb1, p)

    if s.game.line1.position == 0 or s.game.line1.position == 2:
        p = [337,318]
        screen.blit(columna, p)
    elif s.game.line1.position == 1:
        p = [337,368]
        screen.blit(columna, p)
    else:
        p = [337,269]
        screen.blit(columna, p)

    if s.game.line3.position == 0:
        p = [389,368]
        screen.blit(columnc1, p)
        p = [440,369]
        screen.blit(columnc2, p)
    else:
        p = [389,368]
        screen.blit(columnc2, p)
        p = [440,369]
        screen.blit(columnc1, p)


    nc_p = [230,368]
    screen.blit(number_card, nc_p)

    backglass_position = [0, 0]
    backglass = pygame.Surface(screen.get_size(), flags=pygame.SRCALPHA)
    backglass.fill((0, 0, 0))
    if menu == True:
        backglass = pygame.image.load('bonus_7/assets/bonus_7_menu.png').convert_alpha()
    else:
        if (s.game.anti_cheat.status == True):
            backglass = pygame.image.load('bonus_7/assets/bonus_7_gi.png').convert_alpha()
        else:
            backglass = pygame.image.load('bonus_7/assets/bonus_7_off.png').convert_alpha()
    backglass = pygame.transform.scale(backglass, (720, 1280))
    
    screen.blit(backglass, backglass_position)


    if s.game.eb_play.status == True:
        eb_position = [37,1041]
        screen.blit(extra_balls, eb_position)

    if s.game.extra_ball.position >= 1:
        eb_position = [143,1043]
        screen.blit(eb_number, eb_position)
    if s.game.extra_ball.position >= 2:
        eb_position = [195,1043]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 3:
        eb_position = [257,1044]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 4:
        eb_position = [319,1045]
        screen.blit(eb_number, eb_position)
    if s.game.extra_ball.position >= 5:
        eb_position = [371,1045]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 6:
        eb_position = [435,1044]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 7:
        eb_position = [497,1044]
        screen.blit(eb_number, eb_position)
    if s.game.extra_ball.position >= 8:
        eb_position = [549,1043]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 9:
        eb_position = [613,1042]
        screen.blit(eb, eb_position)

    if s.game.red_star.status == True:
        rs_position = [8,457]
        screen.blit(time, rs_position)
    if s.game.yellow_star.status == True:
        rs_position = [7,501]
        screen.blit(time, rs_position)

    if s.game.mystic_lines.position >= 4 or s.game.two_red_letter.status == True or s.game.three_red_letter.status == True:
        if s.game.selection_feature.position < 7:
            bfp = [7,546]
            screen.blit(time, bfp)
        elif s.game.selection_feature.position in [7,8]:
            bfp = [9,413]
            screen.blit(time, bfp)
        elif s.game.selection_feature.position == 9:
            bfp = [10,369]
            screen.blit(time, bfp)

    if s.game.ball_count.position < 1:
        if s.game.odds_only.status == True:
            b = [9,877]
            screen.blit(button, b)
        elif s.game.features.status == True:
            b = [10,915]
            screen.blit(button, b)
        elif s.game.special.status == True:
            b = [11,991]
            screen.blit(button, b)
        else:
            b = [11,952]
            screen.blit(button, b)


    if s.game.mystic_lines.position == 1:
        p = [195,682]
        screen.blit(ml_arrow, p)
    if s.game.mystic_lines.position == 2:
        p = [228,682]
        screen.blit(ml_arrow, p)
    if s.game.mystic_lines.position == 3:
        p = [260,681]
        screen.blit(ml_arrow, p)
    if s.game.mystic_lines.position >= 4:
        p = [398,683]
        screen.blit(ml_b, p)
        p = [336,589]
        screen.blit(ml_letter, p)
    if s.game.mystic_lines.position == 5:
        p = [331,681]
        screen.blit(ml_arrow, p)
    if s.game.mystic_lines.position == 6:
        p = [360,681]
        screen.blit(ml_arrow, p)
    if s.game.mystic_lines.position >= 7:
        p = [297,684]
        screen.blit(ml_a, p)
        p = [256,589]
        screen.blit(ml_letter, p)
    if s.game.mystic_lines.position == 8:
        p = [433,680]
        screen.blit(ml_arrow, p)
    if s.game.mystic_lines.position == 9:
        p = [463,680]
        screen.blit(ml_arrow, p)
    if s.game.mystic_lines.position == 10:
        p = [496,681]
        screen.blit(ml_c, p)
        p = [413,589]
        screen.blit(ml_letter, p)

    if s.game.mystic_lines.position >= 4:
        t = 4
        if s.game.selection_feature.position in [7,8]:
            t = 5
        if s.game.selection_feature.position == 9:
            t = 6
        if s.game.ball_count.position == t:
            p = [283,642]
            screen.blit(select_now, p)

    if s.game.tilt.status == False:
        if s.holes:
            if 1 in s.holes:
                if s.game.line2.position == 0:
                    p = [284,526]
                    screen.blit(number, p)
                else:
                    p = [234,529]
                    screen.blit(number, p)
            if 2 in s.holes:
                if s.game.line2.position == 0:
                    p = [282,377]
                    screen.blit(number, p)
                else:
                    p = [232,378]
                    screen.blit(number, p)
            if 3 in s.holes:
                if s.game.line2.position == 0:
                    p = [232,427]
                    screen.blit(number, p)
                else:
                    p = [282,426]
                    screen.blit(number, p)
            if 4 in s.holes:
                if s.game.line3.position == 0:
                    p = [387,378]
                    screen.blit(number, p)
                else:
                    p = [440,378]
                    screen.blit(number, p)
            if 5 in s.holes:
                if s.game.line1.position == 0 or s.game.line1.position == 2:
                    p = [336,477]
                    screen.blit(number, p)
                elif s.game.line1.position == 1:
                    p = [336,526]
                    screen.blit(number, p)
                else:
                    p = [336,428]
                    screen.blit(number, p)
            if 6 in s.holes:
                if s.game.line3.position == 0:
                    p = [440,378]
                    screen.blit(number, p)
                else:
                    p = [387,378]
                    screen.blit(number, p)
            if 7 in s.holes:
                if s.game.line1.position == 0 or s.game.line1.position == 2:
                    p = [336,526]
                    screen.blit(number, p)
                elif s.game.line1.position == 1:
                    p = [334,377]
                    screen.blit(number, p)
                else:
                    p = [336,476]
                    screen.blit(number, p)
            if 8 in s.holes:
                if s.game.line2.position == 0:
                    p = [232,378]
                    screen.blit(number, p)
                else:
                    p = [282,378]
                    screen.blit(number, p)
            if 9 in s.holes:
                if s.game.line1.position == 0 or s.game.line1.position == 2:
                    p = [336,427]
                    screen.blit(number, p)
                elif s.game.line1.position == 1:
                    p = [336,476]
                    screen.blit(number, p)
                else:
                    p = [336,377]
                    screen.blit(number, p)
            if 10 in s.holes:
                if s.game.line3.position == 0:
                    p = [442,477]
                    screen.blit(number, p)
                else:
                    p = [388,476]
                    screen.blit(number, p)
            if 11 in s.holes:
                if s.game.line3.position == 0:
                    p = [388,428]
                    screen.blit(number, p)
                else:
                    p = [442,428]
                    screen.blit(number, p)
            if 12 in s.holes:
                if s.game.line3.position == 0:
                    p = [387,476]
                    screen.blit(number, p)
                else:
                    p = [442,478]
                    screen.blit(number, p)
            if 13 in s.holes:
                if s.game.line3.position == 0:
                    p = [442,526]
                    screen.blit(number, p)
                else:
                    p = [387,526]
                    screen.blit(number, p)
            if 14 in s.holes:
                if s.game.line3.position == 0:
                    p = [442,428]
                    screen.blit(number, p)
                else:
                    p = [388,428]
                    screen.blit(number, p)
            if 15 in s.holes:
                if s.game.line2.position == 0:
                    p = [282,426]
                    screen.blit(number, p)
                else:
                    p = [232,426]
                    screen.blit(number, p)
            if 16 in s.holes:
                if s.game.line1.position == 0 or s.game.line1.position == 2:
                    p = [336,378]
                    screen.blit(number, p)
                elif s.game.line1.position == 1:
                    p = [336,428]
                    screen.blit(number, p)
                else:
                    p = [336,526]
                    screen.blit(number, p)
            if 17 in s.holes:
                if s.game.line2.position == 0:
                    p = [285,479]
                    screen.blit(number, p)
                else:
                    p = [233,479]
                    screen.blit(number, p)
            if 18 in s.holes:
                if s.game.line2.position == 0:
                    p = [233,479]
                    screen.blit(number, p)
                else:
                    p = [285,479]
                    screen.blit(number, p)
            if 19 in s.holes:
                if s.game.line3.position == 0:
                    p = [387,526]
                    screen.blit(number, p)
                else:
                    p = [442,526]
                    screen.blit(number, p)
            if 20 in s.holes:
                if s.game.line2.position == 0:
                    p = [232,528]
                    screen.blit(number, p)
                else:
                    p = [284,526]
                    screen.blit(number, p)

    if s.game.red_odds.position == 1:
        o = [192,785]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 2:
        o = [230,785]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 3:
        o = [267,785]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 4:
        o = [305,785]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 5:
        o = [343,785]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 6:
        o = [385,785]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 7:
        o = [436,785]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 8:
        o = [483,785]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 9:
        o = [530,785]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 10:
        o = [585,785]
        screen.blit(odds, o)

    if s.game.green_odds.position == 1:
        o = [192,849]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 2:
        o = [230,849]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 3:
        o = [267,849]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 4:
        o = [305,849]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 5:
        o = [343,849]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 6:
        o = [385,849]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 7:
        o = [436,849]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 8:
        o = [483,849]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 9:
        o = [530,849]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 10:
        o = [585,849]
        screen.blit(odds, o)

    if s.game.yellow_odds.position == 1:
        o = [192,917]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 2:
        o = [230,917]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 3:
        o = [267,917]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 4:
        o = [305,917]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 5:
        o = [343,917]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 6:
        o = [385,917]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 7:
        o = [436,917]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 8:
        o = [483,917]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 9:
        o = [530,917]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 10:
        o = [585,917]
        screen.blit(odds, o)
        
    if s.game.blue_odds.position == 1:
        o = [192,981]
        screen.blit(odds, o)
    elif s.game.blue_odds.position == 2:
        o = [230,981]
        screen.blit(odds, o)
    elif s.game.blue_odds.position == 3:
        o = [267,981]
        screen.blit(odds, o)
    elif s.game.blue_odds.position == 4:
        o = [305,981]
        screen.blit(odds, o)
    elif s.game.blue_odds.position == 5:
        o = [343,981]
        screen.blit(odds, o)
    elif s.game.blue_odds.position == 6:
        o = [385,981]
        screen.blit(odds, o)
    elif s.game.blue_odds.position == 7:
        o = [436,981]
        screen.blit(odds, o)
    elif s.game.blue_odds.position == 8:
        o = [483,981]
        screen.blit(odds, o)
    elif s.game.blue_odds.position == 9:
        o = [530,981]
        screen.blit(odds, o)
    elif s.game.blue_odds.position == 10:
        o = [585,981]
        screen.blit(odds, o)
   
    p = [297,207]
    screen.blit(letter1, p)
    p = [348,207]
    screen.blit(letter2, p)
    p = [398,207]
    screen.blit(letter3, p)
    p = [455,206]
    screen.blit(letter4, p)
    p = [510,206]
    screen.blit(letter5, p)
    p = [574,205]
    screen.blit(letter6, p)

    if s.game.red_odds.position < 4:
        p = [297,207]
        screen.blit(red_letter1, p)
    if s.game.red_odds.position == 4:
        p = [348,207]
        screen.blit(red_letter2, p)
    if s.game.red_odds.position == 5:
        p = [398,207]
        screen.blit(red_letter3, p)
    if s.game.red_odds.position == 6:
        p = [455,206]
        screen.blit(red_letter4, p)
    if s.game.red_odds.position == 7:
        p = [510,206]
        screen.blit(red_letter5, p)
    if s.game.red_odds.position == 8:
        p = [574,205]
        screen.blit(red_letter6, p)

    if s.game.two_red_letter.status == True:
        p = [11,255]
        screen.blit(red_letter, p)
        p = [85,216]
        screen.blit(two_red, p)
    if s.game.three_red_letter.status == True:
        p = [11,255]
        screen.blit(red_letter, p)
        p = [12,218]
        screen.blit(three_red, p)

    if s.game.three_stars.status == True:
        p = [11,293]
        screen.blit(four_stars, p)
        p = [10,331]
        screen.blit(three_stars, p)
    if s.game.six_stars.status == True:
        p = [11,293]
        screen.blit(four_stars, p)
        p = [84,329]
        screen.blit(six_stars, p)

    if s.game.double_red.status == True:
        p = [7,610]
        screen.blit(red_double, p)
    if s.game.double_yellow.status == True:
        p = [81,608]
        screen.blit(yellow_double, p)
    if s.game.double_green.status == True:
        p = [7,683]
        screen.blit(green_double, p)
    if s.game.double_blue.status == True:
        p = [81,683]
        screen.blit(blue_double, p)

    if s.game.triple.status == False and (s.game.double_red.status == True or s.game.double_yellow.status == True or s.game.double_green.status == True or s.game.double_blue.status == True):
        p = [41,683]
        screen.blit(double_triple, p)

    if s.game.triple.status == True and (s.game.double_red.status == True or s.game.double_yellow.status == True or s.game.double_green.status == True or s.game.double_blue.status == True):
        p = [41,649]
        screen.blit(double_triple, p)

    if s.game.tilt.status == True:
        tilt_position = [632,211]
        screen.blit(tilt, tilt_position)

    # Special Game
    if s.game.special_odds.position > 0:
        if s.game.special_odds.position == 1:
            p = [607,502]
            screen.blit(special_odds, p)
            p = [555,503]
            screen.blit(seven_odds, p)
        if s.game.special_odds.position == 2:
            p = [607,472]
            screen.blit(special_odds, p)
            p = [554,473]
            screen.blit(seven_odds, p)
        if s.game.special_odds.position == 3:
            p = [606,441]
            screen.blit(special_odds, p)
            p = [553,442]
            screen.blit(seven_odds, p)
        if s.game.special_odds.position == 4:
            p = [605,412]
            screen.blit(special_odds, p)
            p = [553,413]
            screen.blit(seven_odds, p)
        if s.game.special_odds.position == 5:
            p = [605,383]
            screen.blit(special_odds, p)
            p = [553,381]
            screen.blit(seven_odds, p)
        if s.game.special_odds.position == 6:
            p = [605,353]
            screen.blit(special_odds, p)
            p = [553,353]
            screen.blit(seven_odds, p)
        if s.game.special_odds.position == 7:
            p = [605,325]
            screen.blit(special_odds, p)
            p = [552,324]
            screen.blit(seven_odds, p)
        if s.game.special_odds.position == 8:
            p = [604,295]
            screen.blit(special_odds, p)
            p = [552,295]
            screen.blit(seven_odds, p)
        if s.game.special_odds.position == 9:
            p = [604,266]
            screen.blit(special_odds, p)
            p = [551,266]
            screen.blit(seven_odds, p)

    if s.game.special_replay_counter.position > 0:
        p = [615,734]
        screen.blit(collected, p)
    
    if s.game.ball_count.position < 3:
        p = [539,734]
        screen.blit(collected, p)

    if s.game.special_game.position == 2:
        p = [608,535]
        screen.blit(ball, p)
        p = [618,633]
        screen.blit(collected, p)
    if s.game.special_game.position == 3:
        p = [637,535]
        screen.blit(ball, p)
        p = [618,633]
        screen.blit(collected, p)
    if s.game.special_game.position == 4:
        p = [668,535]
        screen.blit(ball, p)
        p = [618,633]
        screen.blit(collected, p)

    if s.game.missed.status == True:
        p = [615,683]
        screen.blit(collected, p)

    if s.game.twin_number.position == 1:
        p = [196,743]
        screen.blit(ml_arrow, p)
    elif s.game.twin_number.position == 2:
        p = [228,742]
        screen.blit(ml_arrow, p)
    elif s.game.twin_number.position == 3:
        p = [261,742]
        screen.blit(ml_arrow, p)
    if s.game.twin_number.position >= 4:
        if s.game.twelve.status == True:
            p = [295,733]
            screen.blit(twin_number, p)
        if s.game.eight.status == True:
            p = [295,757]
            screen.blit(twin_number, p)
    if s.game.twin_number.position == 5:
        p = [367,742]
        screen.blit(ml_arrow, p)
    elif s.game.twin_number.position == 6:
        p = [398,741]
        screen.blit(ml_arrow, p)
    elif s.game.twin_number.position == 7:
        p = [431,741]
        screen.blit(ml_arrow, p)
    if s.game.twin_number.position == 8:
        if s.game.eight.status == True:
            p = [465,731]
            screen.blit(twin_number, p)
        if s.game.twelve.status == True:
            p = [465,755]
            screen.blit(twin_number, p)

    if s.game.bonus.position == 1:
        p = [561,702]
        screen.blit(diamond, p)
    elif s.game.bonus.position == 2:
        p = [541,685]
        screen.blit(diamond, p)
    elif s.game.bonus.position == 3:
        p = [541,658]
        screen.blit(diamond, p)
    elif s.game.bonus.position == 4:
        p = [541,631]
        screen.blit(diamond, p)
    elif s.game.bonus.position == 5:
        p = [541,604]
        screen.blit(diamond, p)
    elif s.game.bonus.position == 6:
        p = [541,577]
        screen.blit(diamond, p)
    elif s.game.bonus.position == 7:
        p = [556,546]
        screen.blit(diamond_7, p)
    elif s.game.bonus.position == 8:
        p = [581,575]
        screen.blit(diamond, p)
    elif s.game.bonus.position == 9:
        p = [581,604]
        screen.blit(diamond, p)
    elif s.game.bonus.position == 10:
        p = [581,631]
        screen.blit(diamond, p)
    elif s.game.bonus.position == 11:
        p = [581,657]
        screen.blit(diamond, p)
    elif s.game.bonus.position == 12:
        p = [581,686]
        screen.blit(diamond, p)

    if s.game.two_suns.status == True:
        p = [628,874]
        screen.blit(suns, p)
    if s.game.three_suns.status == True:
        p = [629,784]
        screen.blit(three_suns, p)

    if s.game.top_odds.status == True:
        p = [625,949]
        screen.blit(top_odds, p)

    pygame.display.update()

def eb_animation(num):
    global screen

    if num == 3:
        eb_position = [497,1044]
        screen.blit(eb_number, eb_position)
        pygame.display.update()
    if num == 2:
        eb_position = [549,1043]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 1:
        eb_position = [613,1042]
        screen.blit(eb, eb_position)
        pygame.display.update()

def feature_animation(num):
    global screen

    if num == 4:
        p = [463,680]
        screen.blit(ml_arrow, p)
        pygame.display.update()
    else:
        p = [496,681]
        screen.blit(ml_c, p)
        p = [413,589]
        screen.blit(ml_letter, p)
        pygame.display.update()


def odds_animation(num):
    global screen

    if num == 8:
        o = [192,849]
        screen.blit(odds, o)
    if num == 7:
        o = [230,849]
        screen.blit(odds, o)
    if num == 6:
        o = [267,849]
        screen.blit(odds, o)
    if num == 5:
        o = [305,849]
        screen.blit(odds, o)
    if num == 4:
        o = [343,849]
        screen.blit(odds, o)
    if num == 3:
        o = [385,849]
        screen.blit(odds, o)
    if num == 2:
        o = [436,849]
        screen.blit(odds, o)
    if num == 1:
        o = [483,849]
        screen.blit(odds, o)
    pygame.display.update()


