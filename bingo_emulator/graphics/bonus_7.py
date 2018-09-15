
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
bg_menu = pygame.image.load('bonus_7/assets/bonus_7_menu.png').convert_alpha()
bg_gi = pygame.image.load('bonus_7/assets/bonus_7_gi.png').convert_alpha()
bg_off = pygame.image.load('bonus_7/assets/bonus_7_off.png').convert_alpha()

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
        screen.blit(bg_menu, backglass_position)
    else:
        if (s.game.anti_cheat.status == True):
            screen.blit(bg_gi, backglass_position)
        else:
            screen.blit(bg_off, backglass_position)

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
        p = [297,684]
        screen.blit(ml_a, p)
        p = [336,589]
        screen.blit(ml_letter, p)
    if s.game.mystic_lines.position == 5:
        p = [331,681]
        screen.blit(ml_arrow, p)
    if s.game.mystic_lines.position == 6:
        p = [360,681]
        screen.blit(ml_arrow, p)
    if s.game.mystic_lines.position >= 7:
        p = [398,683]
        screen.blit(ml_b, p)
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
        t = 3
        if s.game.selection_feature.position in [7,8]:
            t = 4
        if s.game.selection_feature.position == 9:
            t = 5
        if s.game.ball_count.position == t:
            s.cancel_delayed(name="blink")
            blink([s,1,1])
        else:
            s.cancel_delayed(name="blink")

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

    if s.game.red_odds.position < 5:
        p = [297,207]
        screen.blit(red_letter1, p)
    if s.game.red_odds.position in [5,6]:
        p = [348,207]
        screen.blit(red_letter2, p)
    if s.game.red_odds.position == 7:
        p = [398,207]
        screen.blit(red_letter3, p)
    if s.game.red_odds.position == 8:
        p = [455,206]
        screen.blit(red_letter4, p)
    if s.game.red_odds.position == 9:
        p = [510,206]
        screen.blit(red_letter5, p)
    if s.game.red_odds.position == 10:
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

    if s.game.special_odds.position > 0:
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

def blink(args):
    dirty_rects = []
    s = args[0]
    b = args[1]
    sn = args[2]

    if b == 0:
        if sn == 1:
            p = [283,642]
            dirty_rects.append(screen.blit(select_now, p))
        pygame.display.update(dirty_rects)
    else:
        dirty_rects.append(screen.blit(bg_gi, (283,642), pygame.Rect(283,642,146,30)))
        pygame.display.update(dirty_rects)
    b = not b

    args = [s,b,sn]

    s.delay(name="blink", delay=0.1, handler=blink, param=args)

def line1_animation(args):
    dirty_rects = []
    s = args[0]
    num = args[1]
    line = args[2]

    if line == 1:
        if s.game.line1.position == 0:
            dirty_rects.append(screen.blit(columna, (337, 269 - num)))
        elif s.game.line1.position == 1:
            dirty_rects.append(screen.blit(columna, (337, 318 - num)))
        elif s.game.line1.position == 2:
            dirty_rects.append(screen.blit(columna, (337, 368 + num)))
        elif s.game.line1.position == 3:
            dirty_rects.append(screen.blit(columna, (337, 318 + num)))
    
        nc_p = [230,368]
        dirty_rects.append(screen.blit(number_card, nc_p))
        if (s.game.anti_cheat.status == True):
            dirty_rects.append(screen.blit(bg_gi, (224,264), pygame.Rect(224,264,270,408)))
        else:
            dirty_rects.append(screen.blit(bg_off, (224,264), pygame.Rect(224,264,270,408)))

        p = [297,207]
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],49,54)))
        dirty_rects.append(screen.blit(letter1, p))

        p = [348,207]
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],49,54)))
        dirty_rects.append(screen.blit(letter2, p))
        
        p = [398,207]
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],55,54)))
        dirty_rects.append(screen.blit(letter3, p))

        p = [455,206]
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],55,54)))
        dirty_rects.append(screen.blit(letter4, p))

        p = [510,206]
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],40,54)))
        dirty_rects.append(screen.blit(letter5, p))
        
        p = [574,205]
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],50,54)))
        dirty_rects.append(screen.blit(letter6, p))
        
        if s.game.red_odds.position < 5:
            p = [297,207]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],49,54)))
            dirty_rects.append(screen.blit(letter1, p))
            dirty_rects.append(screen.blit(red_letter1, p))
        if s.game.red_odds.position  in [5,6]:
            p = [348,207]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],49,54)))
            dirty_rects.append(screen.blit(letter2, p))
            dirty_rects.append(screen.blit(red_letter2, p))
        if s.game.red_odds.position == 7:
            p = [398,207]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],55,54)))
            dirty_rects.append(screen.blit(letter3, p))
            dirty_rects.append(screen.blit(red_letter3, p))
        if s.game.red_odds.position == 8:
            p = [455,206]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],55,54)))
            dirty_rects.append(screen.blit(letter4, p))
            dirty_rects.append(screen.blit(red_letter4, p))
        if s.game.red_odds.position == 9:
            p = [510,206]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],40,54)))
            dirty_rects.append(screen.blit(letter5, p))
            dirty_rects.append(screen.blit(red_letter5, p))
        if s.game.red_odds.position == 10:
            p = [574,205]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],50,54)))
            dirty_rects.append(screen.blit(letter6, p))
            dirty_rects.append(screen.blit(red_letter6, p))

        if s.game.mystic_lines.position >= 4:
            p = [336,589]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],49,48)))
            dirty_rects.append(screen.blit(ml_letter, p))
        if s.game.mystic_lines.position >= 7:
            p = [256,589]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],49,48)))
            dirty_rects.append(screen.blit(ml_letter, p))
        if s.game.mystic_lines.position == 10:
            p = [413,589]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],49,48)))
            dirty_rects.append(screen.blit(ml_letter, p))

    pygame.display.update(dirty_rects)

def line2_animation(args):
    dirty_rects = []
    s = args[0]
    num = args[1]
    line = args[2]
    if line == 2:
        if s.game.line2.position == 0:
            dirty_rects.append(screen.blit(columnb2, (233 - num, 369)))
            dirty_rects.append(screen.blit(columnb1, (286 + num, 369)))
        elif s.game.line2.position == 1:
            dirty_rects.append(screen.blit(columnb1, (233 - num, 369)))
            dirty_rects.append(screen.blit(columnb2, (286 + num, 369)))
     
        nc_p = [230,368]
        dirty_rects.append(screen.blit(number_card, nc_p))
        if (s.game.anti_cheat.status == True):
            dirty_rects.append(screen.blit(bg_gi, (233,369), pygame.Rect(233,369,270,212)))
        else:
            dirty_rects.append(screen.blit(bg_off, (233,369), pygame.Rect(233,369,270,212)))

        if s.game.mystic_lines.position >= 4:
            p = [336,589]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],49,48)))
            dirty_rects.append(screen.blit(ml_letter, p))
        if s.game.mystic_lines.position >= 7:
            p = [256,589]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],49,48)))
            dirty_rects.append(screen.blit(ml_letter, p))
        if s.game.mystic_lines.position == 10:
            p = [413,589]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],49,48)))
            dirty_rects.append(screen.blit(ml_letter, p))

    pygame.display.update(dirty_rects)

def line3_animation(args):
    dirty_rects = []
    s = args[0]
    num = args[1]
    line = args[2]
    
    if line == 3:
        if s.game.line3.position == 0:
            dirty_rects.append(screen.blit(columnc2, (389 - num, 369)))
            dirty_rects.append(screen.blit(columnc1, (440 + num, 369)))
        elif s.game.line3.position == 1:
            dirty_rects.append(screen.blit(columnc1, (389 - num, 369)))
            dirty_rects.append(screen.blit(columnc2, (440 + num, 369)))

        nc_p = [230,368]
        dirty_rects.append(screen.blit(number_card, nc_p))
        if (s.game.anti_cheat.status == True):
            dirty_rects.append(screen.blit(bg_gi, (230,369), pygame.Rect(230,369,273,212)))
        else:
            dirty_rects.append(screen.blit(bg_off, (230,369), pygame.Rect(230,369,273,212)))

        if s.game.mystic_lines.position >= 4:
            p = [336,589]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],49,48)))
            dirty_rects.append(screen.blit(ml_letter, p))
        if s.game.mystic_lines.position >= 7:
            p = [256,589]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],49,48)))
            dirty_rects.append(screen.blit(ml_letter, p))
        if s.game.mystic_lines.position == 10:
            p = [413,589]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],49,48)))
            dirty_rects.append(screen.blit(ml_letter, p))

    pygame.display.update(dirty_rects)


def eb_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]

    if s.game.extra_ball.position < 1:
        dirty_rects.append(screen.blit(bg_gi, (143,1043), pygame.Rect(143,1043,47,31)))
    if s.game.extra_ball.position < 2:
        dirty_rects.append(screen.blit(bg_gi, (195,1043), pygame.Rect(195,1043,59,34)))
    if s.game.extra_ball.position < 3:
        dirty_rects.append(screen.blit(bg_gi, (257,1044), pygame.Rect(257,1044,59,34)))
    if s.game.extra_ball.position < 4:
        dirty_rects.append(screen.blit(bg_gi, (319,1045), pygame.Rect(319,1045,47,31)))
    if s.game.extra_ball.position < 5:
        dirty_rects.append(screen.blit(bg_gi, (371,1045), pygame.Rect(371,1045,59,34)))
    if s.game.extra_ball.position < 6:
        dirty_rects.append(screen.blit(bg_gi, (435,1044), pygame.Rect(435,1044,59,34)))
    if s.game.extra_ball.position < 7:
        dirty_rects.append(screen.blit(bg_gi, (497,1044), pygame.Rect(497,1044,47,31)))
    if s.game.extra_ball.position < 8:
        dirty_rects.append(screen.blit(bg_gi, (549,1043), pygame.Rect(549,1043,59,34)))
    if s.game.extra_ball.position < 9:
        dirty_rects.append(screen.blit(bg_gi, (613,1042), pygame.Rect(613,1042,59,34)))
    pygame.display.update(dirty_rects)

    if num in [0,25,14,49]:
        if s.game.extra_ball.position < 1:
            p = [143,1043]
            dirty_rects.append(screen.blit(eb_number, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [39,1,26,15]:
        if s.game.extra_ball.position < 2:
            p = [195,1043]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [3,4,17,28,29,40]:
        if s.game.extra_ball.position < 3:
            p = [257,1044]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [5,18,30,43]:
        if s.game.extra_ball.position < 4:
            p = [319,1045]
            dirty_rects.append(screen.blit(eb_number, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [7,8,19,32,33,44]:
        if s.game.extra_ball.position < 5:
            p = [371,1045]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [9,10,20,34,35,45]:
        if s.game.extra_ball.position < 6:
            p = [435,1044]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [11,21,36,46]:
        if s.game.extra_ball.position < 7:
            p = [497,1044]
            dirty_rects.append(screen.blit(eb_number, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [12,22,37,47]:
        if s.game.extra_ball.position < 8:
            p = [549,1043]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [2,6,13,16,23,27,31,38,41,48]:
        if s.game.extra_ball.position < 9:
            p = [613,1042]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return

def clear_odds(s, num):
    global screen

    dirty_rects = []
    
    if s.game.double_red.status == False:
        dirty_rects.append(screen.blit(bg_gi, (7,610), pygame.Rect(7,610,74,74)))
    if s.game.double_yellow.status == False:
        dirty_rects.append(screen.blit(bg_gi, (81,608), pygame.Rect(81,608,74,74)))
    if s.game.double_green.status == False:
        dirty_rects.append(screen.blit(bg_gi, (7,683), pygame.Rect(7,683,74,74)))
    if s.game.double_blue.status == False:
        dirty_rects.append(screen.blit(bg_gi, (81,683), pygame.Rect(81,683,74,74)))

    if s.game.yellow_odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (230,917), pygame.Rect(230,917,46,61)))
    if s.game.yellow_odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (343,917), pygame.Rect(343,917,46,61)))
    if s.game.yellow_odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (385,917), pygame.Rect(385,917,46,61)))
    if s.game.yellow_odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (436,917), pygame.Rect(436,917,46,61)))
    if s.game.yellow_odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (483,917), pygame.Rect(483,917,46,61)))
    if s.game.yellow_odds.position != 9:
        dirty_rects.append(screen.blit(bg_gi, (530,917), pygame.Rect(530,917,46,61)))
    if s.game.yellow_odds.position != 10:
        dirty_rects.append(screen.blit(bg_gi, (585,917), pygame.Rect(585,917,46,61)))

    if s.game.red_odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (267,785), pygame.Rect(267,785,46,61)))
    if s.game.red_odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (305,785), pygame.Rect(305,785,46,61)))
    if s.game.red_odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (385,785), pygame.Rect(385,785,46,61)))
    if s.game.red_odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (436,785), pygame.Rect(436,785,46,61)))
    if s.game.red_odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (483,785), pygame.Rect(483,785,46,61)))
    if s.game.red_odds.position != 9:
        dirty_rects.append(screen.blit(bg_gi, (530,785), pygame.Rect(530,785,46,61)))
    if s.game.red_odds.position != 10:
        dirty_rects.append(screen.blit(bg_gi, (585,785), pygame.Rect(585,785,46,61)))

    if s.game.blue_odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (230,981), pygame.Rect(230,981,46,61)))
        dirty_rects.append(screen.blit(bg_gi, (230,849), pygame.Rect(230,849,46,61)))
    if s.game.blue_odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (343,981), pygame.Rect(343,981,46,61)))
        dirty_rects.append(screen.blit(bg_gi, (343,849), pygame.Rect(343,849,46,61)))
    if s.game.blue_odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (436,981), pygame.Rect(436,981,46,61)))
        dirty_rects.append(screen.blit(bg_gi, (436,849), pygame.Rect(436,849,46,61)))
    if s.game.blue_odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (483,981), pygame.Rect(483,981,46,61)))
        dirty_rects.append(screen.blit(bg_gi, (483,849), pygame.Rect(483,849,46,61)))
    if s.game.blue_odds.position != 9:
        dirty_rects.append(screen.blit(bg_gi, (530,981), pygame.Rect(530,981,46,61)))
        dirty_rects.append(screen.blit(bg_gi, (530,849), pygame.Rect(530,849,46,61)))
    if s.game.blue_odds.position != 10:
        dirty_rects.append(screen.blit(bg_gi, (585,981), pygame.Rect(585,981,46,61)))
        dirty_rects.append(screen.blit(bg_gi, (585,849), pygame.Rect(585,849,46,61)))

    pygame.display.update(dirty_rects)

def draw_odds_animation(s, num):
    global screen
    dirty_rects = []

    if num in [7,32]:
        if s.game.double_red.status == False:
            p = [7,610]
            dirty_rects.append(screen.blit(red_double, p))
            pygame.display.update(dirty_rects)
            return
    if num in [15,40]:
        if s.game.double_yellow.status == False:
            p = [81,608]
            dirty_rects.append(screen.blit(yellow_double, p))
            pygame.display.update(dirty_rects)
            return
    if num in [0,25]:
        if s.game.double_green.status == False:
            p = [7,683]
            dirty_rects.append(screen.blit(green_double, p))
            pygame.display.update(dirty_rects)
            return
    if num in [9,34]:
        if s.game.double_blue.status == False:
            p = [81,683]
            dirty_rects.append(screen.blit(blue_double, p))
            pygame.display.update(dirty_rects)
            return

    if num in [22,47]:
        if s.game.yellow_odds.position != 2:
            p = [230,917]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [13,38]:
        if s.game.yellow_odds.position != 5:
            p = [343,917]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [20,45]:
        if s.game.yellow_odds.position != 6:
            p = [385,917]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [20,45]:
        if s.game.yellow_odds.position != 7:
            p = [436,917]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [12,37]:
        if s.game.yellow_odds.position != 8:
            p = [483,917]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [7,32]:
        if s.game.yellow_odds.position != 9:
            p = [530,917]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [21,46]:
        if s.game.yellow_odds.position != 10:
            p = [585,917]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    
    if num in [2,27]:
        if s.game.red_odds.position != 3:
            p = [267,785]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [10,35]:
        if s.game.red_odds.position != 4:
            p = [305,785]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [12,37]:
        if s.game.red_odds.position != 6:
            p = [385,785]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [6,31]:
        if s.game.red_odds.position != 7:
            p = [436,785]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [14,39]:
        if s.game.red_odds.position != 8:
            p = [483,785]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [1,26]:
        if s.game.red_odds.position != 9:
            p = [530,785]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [20,45]:
        if s.game.red_odds.position != 10:
            p = [585,785]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return

    if num in [8,33]:
        if s.game.blue_odds.position != 2:
            p = [230,981]
            dirty_rects.append(screen.blit(odds, p))
            p = [230,849]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [23,48]:
        if s.game.blue_odds.position != 5:
            p = [343,981]
            dirty_rects.append(screen.blit(odds, p))
            p = [343,849]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [3,28]:
        if s.game.blue_odds.position != 7:
            p = [436,981]
            dirty_rects.append(screen.blit(odds, p))
            p = [436,849]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
    if num in [18,43]:
        if s.game.blue_odds.position != 8:
            p = [483,981]
            dirty_rects.append(screen.blit(odds, p))
            p = [483,849]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [5,30]:
        if s.game.blue_odds.position != 9:
            p = [530,981]
            dirty_rects.append(screen.blit(odds, p))
            p = [530,849]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [16,41]:
        if s.game.blue_odds.position != 10:
            p = [585,981]
            dirty_rects.append(screen.blit(odds, p))
            p = [585,849]
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
    
    if s.game.selection_feature.position > 7:
        dirty_rects.append(screen.blit(bg_gi, (7,546), pygame.Rect(7,546,148,48)))
    if s.game.mystic_lines.position < 4 and s.game.two_red_letter.status == False and s.game.three_red_letter.status == False:
        dirty_rects.append(screen.blit(bg_gi, (7,546), pygame.Rect(7,546,148,48)))

    if s.game.selection_feature.position not in [7,8]:
        dirty_rects.append(screen.blit(bg_gi, (9,413), pygame.Rect(9,413,148,48)))
    if s.game.mystic_lines.position < 4 and s.game.two_red_letter.status == False and s.game.three_red_letter.status == False:
        dirty_rects.append(screen.blit(bg_gi, (9,413), pygame.Rect(9,413,148,48)))
    
    if s.game.selection_feature.position < 9:
        dirty_rects.append(screen.blit(bg_gi, (10,369), pygame.Rect(10,369,148,48)))
    if s.game.mystic_lines.position < 4 and s.game.two_red_letter.status == False and s.game.three_red_letter.status == False:
        dirty_rects.append(screen.blit(bg_gi, (10,369), pygame.Rect(10,369,148,48)))

    if s.game.yellow_star.status == False:
        dirty_rects.append(screen.blit(bg_gi, (7,501), pygame.Rect(7,501,148,48)))
    if s.game.red_star.status == False:
        dirty_rects.append(screen.blit(bg_gi, (8,457), pygame.Rect(8,457,148,48)))

    if s.game.three_red_letter.status == False:
        dirty_rects.append(screen.blit(bg_gi, (12,218), pygame.Rect(12,218,76,41)))
    if s.game.two_red_letter.status == False:
        dirty_rects.append(screen.blit(bg_gi, (85,216), pygame.Rect(85,216,76,41)))
    if s.game.three_stars.status == False:
        dirty_rects.append(screen.blit(bg_gi, (10,331), pygame.Rect(10,331,77,27)))
    if s.game.six_stars.status == False:
        dirty_rects.append(screen.blit(bg_gi, (84,329), pygame.Rect(84,329,77,27)))

    if s.game.mystic_lines.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (228,682), pygame.Rect(228,682,29,29)))
    if s.game.mystic_lines.position < 4:
        dirty_rects.append(screen.blit(bg_gi, (336,589), pygame.Rect(336,589,49,48)))
    if s.game.mystic_lines.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (331,681), pygame.Rect(331,681,29,29)))
    if s.game.mystic_lines.position < 7:
        dirty_rects.append(screen.blit(bg_gi, (256,589), pygame.Rect(256,589,49,48)))
    if s.game.mystic_lines.position != 9:
        dirty_rects.append(screen.blit(bg_gi, (463,680), pygame.Rect(463,680,29,29)))
    if s.game.mystic_lines.position < 10:
        dirty_rects.append(screen.blit(bg_gi, (413,589), pygame.Rect(413,589,49,48)))

    pygame.display.update(dirty_rects)


def draw_feature_animation(s, num):
    global screen
    dirty_rects = []
    
    if num in [10,35]:
        if s.game.selection_feature.position not in [1,2,3,4,5,6] and (s.game.mystic_lines.position < 4 and s.game.two_red_letter.status == False and s.game.three_red_letter.status == False):
            p = [7,546]
            dirty_rects.append(screen.blit(time, p))
            pygame.display.update(dirty_rects)
            return
    if num in [9,34]:
        if s.game.selection_feature.position not in [7,8] and (s.game.mystic_lines.position < 4 and s.game.two_red_letter.status == False and s.game.three_red_letter.status == False):
            p = [9,413]
            dirty_rects.append(screen.blit(time, p))
            pygame.display.update(dirty_rects)
            return
    if num in [6,31]:
        if s.game.selection_feature.position not in [9] and (s.game.mystic_lines.position < 4 and s.game.two_red_letter.status == False and s.game.three_red_letter.status == False):
            p = [10,369]
            dirty_rects.append(screen.blit(time, p))
            pygame.display.update(dirty_rects)
            return
    if num in [11,36]:
        if s.game.red_star.status == False:
            p = [8,457]
            dirty_rects.append(screen.blit(time, p))
            pygame.display.update(dirty_rects)
            s.game.coils.redROLamp.pulse(85)
            return
    if num in [4,29]:
        if s.game.yellow_star.status == False:
            p = [7,501]
            dirty_rects.append(screen.blit(time, p))
            pygame.display.update(dirty_rects)
            s.game.coils.yellowROLamp.pulse(85)
            return
    if num in [13,38]:
        if s.game.three_red_letter.status == False:
            p = [12,218]
            dirty_rects.append(screen.blit(three_red, p))
            pygame.display.update(dirty_rects)
            return
    if num in [44,19]:
        if s.game.two_red_letter.status == False:
            p = [85,216]
            dirty_rects.append(screen.blit(two_red, p))
            pygame.display.update(dirty_rects)
            return
    if num in [16,41]:
        if s.game.three_stars.status == False:
            p = [10,331]
            dirty_rects.append(screen.blit(three_stars, p))
            pygame.display.update(dirty_rects)
            return
    if num in [4,29]:
        if s.game.six_stars.status == False:
            p = [84,329]
            dirty_rects.append(screen.blit(six_stars, p))
            pygame.display.update(dirty_rects)
            return
    if num in [5,30]:
        if s.game.mystic_lines.position != 2:
            p = [228,682]
            dirty_rects.append(screen.blit(ml_arrow, p))
            pygame.display.update(dirty_rects)
            return
    if num in [23,48]:
        if s.game.mystic_lines.position < 4:
            p = [336,589]
            dirty_rects.append(screen.blit(ml_letter, p))
            pygame.display.update(dirty_rects)
            return
    if num in [0,25]:
        if s.game.mystic_lines.position != 5:
            p = [331,681]
            dirty_rects.append(screen.blit(ml_arrow, p))
            pygame.display.update(dirty_rects)
            return
    if num in [12,37,22,47]:
        if s.game.mystic_lines.position < 7:
            p = [256,589]
            dirty_rects.append(screen.blit(ml_letter, p))
            pygame.display.update(dirty_rects)
            return
    if num in [9,34]:
        if s.game.mystic_lines.position != 9:
            p = [463,680]
            dirty_rects.append(screen.blit(ml_arrow, p))
            pygame.display.update(dirty_rects)
            return
    if num in [10,35,24,49]:
        if s.game.mystic_lines.position < 10:
            p = [413,589]
            dirty_rects.append(screen.blit(ml_letter, p))
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

def special_animation(args):
    global screen
    dirty_rects = []
    s = args[0]
    num = args[1]

    if s.game.special_odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (607,472), pygame.Rect(607,472,90,30)))
        dirty_rects.append(screen.blit(bg_gi, (554,473), pygame.Rect(554,473,42,32)))
    if s.game.special_odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (606,441), pygame.Rect(606,441,90,30)))
        dirty_rects.append(screen.blit(bg_gi, (553,442), pygame.Rect(553,442,42,32)))
    if s.game.special_odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (605,412), pygame.Rect(605,412,90,30)))
        dirty_rects.append(screen.blit(bg_gi, (553,413), pygame.Rect(553,413,42,32)))
    if s.game.special_odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (605,383), pygame.Rect(605,383,90,30)))
        dirty_rects.append(screen.blit(bg_gi, (553,381), pygame.Rect(553,381,42,32)))
    if s.game.special_odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (605,353), pygame.Rect(605,353,90,30)))
        dirty_rects.append(screen.blit(bg_gi, (553,353), pygame.Rect(553,353,42,32)))
    if s.game.special_odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (605,325), pygame.Rect(605,325,90,30)))
        dirty_rects.append(screen.blit(bg_gi, (552,324), pygame.Rect(552,324,42,32)))
    if s.game.special_odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (604,295), pygame.Rect(604,295,90,30)))
        dirty_rects.append(screen.blit(bg_gi, (552,295), pygame.Rect(552,295,42,32)))
    if s.game.special_odds.position != 9:
        dirty_rects.append(screen.blit(bg_gi, (604,266), pygame.Rect(604,266,90,30)))
        dirty_rects.append(screen.blit(bg_gi, (551,266), pygame.Rect(551,266,42,32)))

    pygame.display.update(dirty_rects)

    if num in [18,19,43,44]:
        if s.game.special_odds.position < 2:
            p = [607,472]
            dirty_rects.append(screen.blit(special_odds, p))
            p = [554,473]
            dirty_rects.append(screen.blit(seven_odds, p))
            pygame.display.update(dirty_rects) 
            return
    if num in [20,21,45,46]:
        if s.game.special_odds.position < 3:
            p = [606,441]
            dirty_rects.append(screen.blit(special_odds, p))
            p = [553,442]
            dirty_rects.append(screen.blit(seven_odds, p))
            pygame.display.update(dirty_rects) 
            return
    if num in [14,15,39,40]:
        if s.game.special_odds.position < 4:
            p = [605,412]
            dirty_rects.append(screen.blit(special_odds, p))
            p = [553,413]
            dirty_rects.append(screen.blit(seven_odds, p))
            pygame.display.update(dirty_rects) 
            return
    if num in [16,17,41,42]:
        if s.game.special_odds.position < 5:
            p = [605,383]
            dirty_rects.append(screen.blit(special_odds, p))
            p = [553,381]
            dirty_rects.append(screen.blit(seven_odds, p))
            pygame.display.update(dirty_rects) 
            return
    if num in [6,7,10,11,31,32,35,36]:
        if s.game.special_odds.position < 6:
            p = [605,353]
            dirty_rects.append(screen.blit(special_odds, p))
            p = [553,353]
            dirty_rects.append(screen.blit(seven_odds, p))
            pygame.display.update(dirty_rects) 
            return
    if num in [4,5,12,13,29,30,37,38]:
        if s.game.special_odds.position < 7:
            p = [605,325]
            dirty_rects.append(screen.blit(special_odds, p))
            p = [552,324]
            dirty_rects.append(screen.blit(seven_odds, p))
            pygame.display.update(dirty_rects) 
            return
    if num in [0,1,2,3,8,9,25,26,27,28,33,34]:
        if s.game.special_odds.position < 8:
            p = [604,295]
            dirty_rects.append(screen.blit(special_odds, p))
            p = [552,295]
            dirty_rects.append(screen.blit(seven_odds, p))
            pygame.display.update(dirty_rects) 
            return
    if num in [22,23,47,48]:
        if s.game.special_odds.position < 9:
            p = [604,266]
            dirty_rects.append(screen.blit(special_odds, p))
            p = [551,266]
            dirty_rects.append(screen.blit(seven_odds, p))
            pygame.display.update(dirty_rects) 
            return
