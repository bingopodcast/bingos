
import pygame
import random

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

meter = pygame.image.load('graphics/assets/black_register_cover.png').convert()
odds = pygame.image.load('london/assets/odds.png').convert_alpha()
eb = pygame.image.load('london/assets/eb.png').convert_alpha()
eb_number = pygame.image.load('london/assets/eb_number.png').convert_alpha()
extra_balls = pygame.image.load('london/assets/extra_balls.png').convert_alpha()
time = pygame.image.load('london/assets/time.png').convert_alpha()
ml_letter = pygame.image.load('london/assets/ml_letter.png').convert_alpha()
ml_arrow = pygame.image.load('london/assets/ml_arrow.png').convert_alpha()
ml_a = pygame.image.load('london/assets/ml_a.png').convert_alpha()
ml_b = pygame.image.load('london/assets/ml_b.png').convert_alpha()
ml_c = pygame.image.load('london/assets/ml_c.png').convert_alpha()
select_now = pygame.image.load('london/assets/select_now.png').convert_alpha()
tilt = pygame.image.load('london/assets/tilt.png').convert_alpha()
button = pygame.image.load('london/assets/pap.png').convert_alpha()
red_double = pygame.image.load('london/assets/red_double.png').convert_alpha()
green_double = pygame.image.load('london/assets/green_double.png').convert_alpha()
yellow_double = pygame.image.load('london/assets/yellow_double.png').convert_alpha()
blue_double = pygame.image.load('london/assets/blue_double.png').convert_alpha()
four_stars = pygame.image.load('london/assets/four_stars.png').convert_alpha()
six_stars = pygame.image.load('london/assets/six_stars.png').convert_alpha()
three_stars = pygame.image.load('london/assets/three_stars.png').convert_alpha()
three_red = pygame.image.load('london/assets/three_red.png').convert_alpha()
two_red = pygame.image.load('london/assets/two_red.png').convert_alpha()
red_letter = pygame.image.load('london/assets/red_letter.png').convert_alpha()
letter1 = pygame.image.load('london/assets/letter1.png').convert_alpha()
letter2 = pygame.image.load('london/assets/letter2.png').convert_alpha()
letter3 = pygame.image.load('london/assets/letter3.png').convert_alpha()
letter4 = pygame.image.load('london/assets/letter4.png').convert_alpha()
letter5 = pygame.image.load('london/assets/letter5.png').convert_alpha()
letter6 = pygame.image.load('london/assets/letter6.png').convert_alpha()
red_letter1 = pygame.image.load('london/assets/red_letter1.png').convert_alpha()
red_letter2 = pygame.image.load('london/assets/red_letter2.png').convert_alpha()
red_letter3 = pygame.image.load('london/assets/red_letter3.png').convert_alpha()
red_letter4 = pygame.image.load('london/assets/red_letter4.png').convert_alpha()
red_letter5 = pygame.image.load('london/assets/red_letter5.png').convert_alpha()
red_letter6 = pygame.image.load('london/assets/red_letter6.png').convert_alpha()
number_card = pygame.image.load('london/assets/number_card.png').convert_alpha()
number = pygame.image.load('london/assets/number.png').convert_alpha()
columnb1 = pygame.image.load('london/assets/columnb1.png').convert_alpha()
columnb2 = pygame.image.load('london/assets/columnb2.png').convert_alpha()
columna = pygame.image.load('london/assets/columna.png').convert_alpha()
columnc1 = pygame.image.load('london/assets/columnc1.png').convert_alpha()
columnc2 = pygame.image.load('london/assets/columnc2.png').convert_alpha()
double_triple = pygame.image.load('london/assets/double_triple.png').convert_alpha()
ball = pygame.image.load('london/assets/ball.png').convert_alpha()
eo = pygame.image.load('london/assets/eo.png').convert_alpha()
dn = pygame.image.load('london/assets/dn.png').convert_alpha()
collected = pygame.image.load('london/assets/collected.png').convert_alpha()
missed = pygame.image.load('london/assets/missed.png').convert_alpha()
special_odds = pygame.image.load('london/assets/special_odds.png').convert_alpha()
golden = pygame.image.load('london/assets/golden.png').convert_alpha()
color = pygame.image.load('london/assets/color.png').convert_alpha()
twin_number = pygame.image.load('london/assets/twin_number.png').convert_alpha()
bg_menu = pygame.image.load('london/assets/london_menu.png').convert_alpha()
bg_gi = pygame.image.load('london/assets/london_gi.png').convert_alpha()
bg_off = pygame.image.load('london/assets/london_off.png').convert_alpha()

class scorereel():
    """ Score Reels are used to count replays """
    def __init__(self, pos, image):
        self.position = pos
        self.default_y = self.position[1]
        self.image = pygame.image.load(image).convert()

reel1 = scorereel([110,800], "graphics/assets/white_reel.png")
reel10 = scorereel([91,800], "graphics/assets/white_reel.png")
reel100 = scorereel([72,800], "graphics/assets/white_reel.png")
reel1000 = scorereel([53,800], "graphics/assets/white_reel.png")

def display(s, replays=0, menu=False):
    
    meter.set_colorkey((255,0,252))
    meter_position = [44,800]

    screen.blit(reel1.image, reel1.position)
    screen.blit(reel10.image, reel10.position)
    screen.blit(reel100.image, reel100.position)
    screen.blit(reel1000.image, reel1000.position)
    screen.blit(meter, meter_position)

    if s.game.line2.position == 0:
        p = [233,368]
        screen.blit(columnb1, p)
        p = [286,369]
        screen.blit(columnb2, p)
    else:
        p = [233,368]
        screen.blit(columnb2, p)
        p = [286,369]
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


    nc_p = [228,368]
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
        eb_position = [38,1044]
        screen.blit(extra_balls, eb_position)

    if s.game.extra_ball.position >= 1:
        eb_position = [147,1044]
        screen.blit(eb_number, eb_position)
    if s.game.extra_ball.position >= 2:
        eb_position = [197,1044]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 3:
        eb_position = [261,1044]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 4:
        eb_position = [322,1044]
        screen.blit(eb_number, eb_position)
    if s.game.extra_ball.position >= 5:
        eb_position = [373,1044]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 6:
        eb_position = [434,1044]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 7:
        eb_position = [498,1044]
        screen.blit(eb_number, eb_position)
    if s.game.extra_ball.position >= 8:
        eb_position = [548,1044]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 9:
        eb_position = [612,1044]
        screen.blit(eb, eb_position)

    if s.game.red_star.status == True:
        rs_position = [14,460]
        screen.blit(time, rs_position)
    if s.game.yellow_star.status == True:
        rs_position = [14,506]
        screen.blit(time, rs_position)

    if s.game.mystic_lines.position >= 4 or s.game.two_red_letter.status == True or s.game.three_red_letter.status == True:
        if s.game.selection_feature.position < 7:
            bfp = [15,550]
            screen.blit(time, bfp)
        elif s.game.selection_feature.position in [7,8]:
            bfp = [15,415]
            screen.blit(time, bfp)
        elif s.game.selection_feature.position == 9:
            bfp = [14,372]
            screen.blit(time, bfp)

    if s.game.ball_count.position < 1:
        if s.game.odds_only.status == True:
            b = [16,876]
            screen.blit(button, b)
        elif s.game.features.status == True:
            b = [15,915]
            screen.blit(button, b)
        elif s.game.special.status == True:
            b = [13,990]
            screen.blit(button, b)
        else:
            b = [14,952]
            screen.blit(button, b)


    if s.game.mystic_lines.position == 1:
        p = [198,681]
        screen.blit(ml_arrow, p)
    if s.game.mystic_lines.position == 2:
        p = [231,681]
        screen.blit(ml_arrow, p)
    if s.game.mystic_lines.position == 3:
        p = [263,680]
        screen.blit(ml_arrow, p)
    if s.game.mystic_lines.position >= 4:
        p = [299,681]
        screen.blit(ml_a, p)
        p = [334,589]
        screen.blit(ml_letter, p)
    if s.game.mystic_lines.position == 5:
        p = [330,681]
        screen.blit(ml_arrow, p)
    if s.game.mystic_lines.position == 6:
        p = [360,681]
        screen.blit(ml_arrow, p)
    if s.game.mystic_lines.position >= 7:
        p = [396,680]
        screen.blit(ml_b, p)
        p = [260,590]
        screen.blit(ml_letter, p)
    if s.game.mystic_lines.position == 8:
        p = [429,680]
        screen.blit(ml_arrow, p)
    if s.game.mystic_lines.position == 9:
        p = [458,680]
        screen.blit(ml_arrow, p)
    if s.game.mystic_lines.position == 10:
        p = [492,680]
        screen.blit(ml_c, p)
        p = [410,590]
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
                    p = [287,471]
                    screen.blit(number, p)
                else:
                    p = [235,471]
                    screen.blit(number, p)
            if 2 in s.holes:
                if s.game.line3.position == 0:
                    p = [389,471]
                    screen.blit(number, p)
                else:
                    p = [440,471]
                    screen.blit(number, p)
            if 3 in s.holes:
                if s.game.line3.position == 0:
                    p = [389,522]
                    screen.blit(number, p)
                else:
                    p = [441,521]
                    screen.blit(number, p)
            if 4 in s.holes:
                if s.game.line2.position == 0:
                    p = [287,371]
                    screen.blit(number, p)
                else:
                    p = [236,371]
                    screen.blit(number, p)
            if 5 in s.holes:
                if s.game.line1.position == 0 or s.game.line1.position == 2:
                    p = [336,521]
                    screen.blit(number, p)
                elif s.game.line1.position == 1:
                    p = [337,371]
                    screen.blit(number, p)
                else:
                    p = [337,471]
                    screen.blit(number, p)
            if 6 in s.holes:
                if s.game.line3.position == 0:
                    p = [389,421]
                    screen.blit(number, p)
                else:
                    p = [441,419]
                    screen.blit(number, p)
            if 7 in s.holes:
                if s.game.line1.position == 0 or s.game.line1.position == 2:
                    p = [337,370]
                    screen.blit(number, p)
                elif s.game.line1.position == 1:
                    p = [337,420]
                    screen.blit(number, p)
                else:
                    p = [335,521]
                    screen.blit(number, p)
            if 8 in s.holes:
                if s.game.line2.position == 0:
                    p = [286,421]
                    screen.blit(number, p)
                else:
                    p = [233,420]
                    screen.blit(number, p)
            if 9 in s.holes:
                if s.game.line3.position == 0:
                    p = [389,369]
                    screen.blit(number, p)
                else:
                    p = [440,371]
                    screen.blit(number, p)
            if 10 in s.holes:
                if s.game.line3.position == 0:
                    p = [440,521]
                    screen.blit(number, p)
                else:
                    p = [389,521]
                    screen.blit(number, p)
            if 11 in s.holes:
                if s.game.line2.position == 0:
                    p = [233,420]
                    screen.blit(number, p)
                else:
                    p = [286,420]
                    screen.blit(number, p)
            if 12 in s.holes:
                if s.game.line1.position in [0,2]:
                    p = [336,419]
                    screen.blit(number, p)
                elif s.game.line1.position == 1:
                    p = [336,471]
                    screen.blit(number, p)
                else:
                    p = [337,370]
                    screen.blit(number, p)
            if 13 in s.holes:
                if s.game.line3.position == 0:
                    p = [440,420]
                    screen.blit(number, p)
                else:
                    p = [388,420]
                    screen.blit(number, p)
            if 14 in s.holes:
                if s.game.line2.position == 0:
                    p = [285,521]
                    screen.blit(number, p)
                else:
                    p = [233,521]
                    screen.blit(number, p)
            if 15 in s.holes:
                if s.game.line2.position == 0:
                    p = [234,470]
                    screen.blit(number, p)
                else:
                    p = [286,471]
                    screen.blit(number, p)
            if 16 in s.holes:
                if s.game.line2.position == 0:
                    p = [234,521]
                    screen.blit(number, p)
                else:
                    p = [285,521]
                    screen.blit(number, p)
            if 17 in s.holes:
                if s.game.line3.position == 0:
                    p = [440,370]
                    screen.blit(number, p)
                else:
                    p = [389,370]
                    screen.blit(number, p)
            if 18 in s.holes:
                if s.game.line2.position == 0:
                    p = [235,370]
                    screen.blit(number, p)
                else:
                    p = [286,370]
                    screen.blit(number, p)
            if 19 in s.holes:
                if s.game.line3.position == 0:
                    p = [441,470]
                    screen.blit(number, p)
                else:
                    p = [389,470]
                    screen.blit(number, p)
            if 20 in s.holes:
                if s.game.line1.position in [0,2]:
                    p = [337,471]
                    screen.blit(number, p)
                elif s.game.line1.position == 1:
                    p = [336,521]
                    screen.blit(number, p)
                else:
                    p = [337,370]
                    screen.blit(number, p)

    if s.game.red_odds.position == 1:
        o = [192,783]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 2:
        o = [242,783]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 3:
        o = [290,783]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 4:
        o = [339,783]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 5:
        o = [387,783]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 6:
        o = [433,783]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 7:
        o = [481,783]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 8:
        o = [529,783]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 9:
        o = [577,783]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 10:
        o = [626,783]
        screen.blit(odds, o)

    if s.game.yellow_odds.position == 1:
        o = [192,913]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 2:
        o = [242,913]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 3:
        o = [290,913]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 4:
        o = [339,913]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 5:
        o = [387,913]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 6:
        o = [433,913]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 7:
        o = [481,913]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 8:
        o = [529,913]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 9:
        o = [577,913]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 10:
        o = [626,913]
        screen.blit(odds, o)

    if s.game.green_odds.position == 1:
        o = [192,846]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 2:
        o = [242,846]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 3:
        o = [290,846]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 4:
        o = [339,846]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 5:
        o = [387,846]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 6:
        o = [433,846]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 7:
        o = [481,846]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 8:
        o = [529,846]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 9:
        o = [577,846]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 10:
        o = [626,846]
        screen.blit(odds, o)

    if s.game.blue_odds.position == 1:
        o = [192,976]
        screen.blit(odds, o)
    elif s.game.blue_odds.position == 2:
        o = [242,976]
        screen.blit(odds, o)
    elif s.game.blue_odds.position == 3:
        o = [290,976]
        screen.blit(odds, o)
    elif s.game.blue_odds.position == 4:
        o = [339,976]
        screen.blit(odds, o)
    elif s.game.blue_odds.position == 5:
        o = [387,976]
        screen.blit(odds, o)
    elif s.game.blue_odds.position == 6:
        o = [433,976]
        screen.blit(odds, o)
    elif s.game.blue_odds.position == 7:
        o = [481,976]
        screen.blit(odds, o)
    elif s.game.blue_odds.position == 8:
        o = [529,976]
        screen.blit(odds, o)
    elif s.game.blue_odds.position == 9:
        o = [577,976]
        screen.blit(odds, o)
    elif s.game.blue_odds.position == 10:
        o = [626,976]
        screen.blit(odds, o)


    p = [387,212]
    screen.blit(letter1, p)
    p = [424,212]
    screen.blit(letter2, p)
    p = [474,212]
    screen.blit(letter3, p)
    p = [529,212]
    screen.blit(letter4, p)
    p = [580,212]
    screen.blit(letter5, p)
    p = [634,212]
    screen.blit(letter6, p)

    if s.game.red_odds.position < 5:
        p = [387,212]
        screen.blit(red_letter1, p)
    if s.game.red_odds.position in [5,6]:
        p = [424,212]
        screen.blit(red_letter2, p)
    if s.game.red_odds.position == 7:
        p = [474,212]
        screen.blit(red_letter3, p)
    if s.game.red_odds.position == 8:
        p = [529,212]
        screen.blit(red_letter4, p)
    if s.game.red_odds.position == 9:
        p = [580,212]
        screen.blit(red_letter5, p)
    if s.game.red_odds.position == 10:
        p = [634,212]
        screen.blit(red_letter6, p)

    if s.game.two_red_letter.status == True:
        p = [16,258]
        screen.blit(red_letter, p)
        p = [90,218]
        screen.blit(two_red, p)
    if s.game.three_red_letter.status == True:
        p = [16,258]
        screen.blit(red_letter, p)
        p = [15,219]
        screen.blit(three_red, p)

    if s.game.three_stars.status == True:
        p = [14,296]
        screen.blit(four_stars, p)
        p = [14,333]
        screen.blit(three_stars, p)
    if s.game.six_stars.status == True:
        p = [14,296]
        screen.blit(four_stars, p)
        p = [88,333]
        screen.blit(six_stars, p)

    if s.game.double_red.status == True:
        p = [14,612]
        screen.blit(red_double, p)
    if s.game.double_yellow.status == True:
        p = [88,612]
        screen.blit(yellow_double, p)
    if s.game.double_green.status == True:
        p = [15,686]
        screen.blit(green_double, p)
    if s.game.double_blue.status == True:
        p = [88,686]
        screen.blit(blue_double, p)

    if s.game.triple.status == False and (s.game.double_red.status == True or s.game.double_yellow.status == True or s.game.double_green.status == True or s.game.double_blue.status == True):
        p = [49,684]
        screen.blit(double_triple, p)

    if s.game.triple.status == True and (s.game.double_red.status == True or s.game.double_yellow.status == True or s.game.double_green.status == True or s.game.double_blue.status == True):
        p = [48,651]
        screen.blit(double_triple, p)

    if s.game.tilt.status == True:
        tilt_position = [218,202]
        screen.blit(tilt, tilt_position)

    # Special Game
    if s.game.missed.status == False:
        if s.game.special_odds.position > 0:
            s.cancel_delayed("blink_circle")
            s.cancel_delayed("blink_triangle")
            s.cancel_delayed("blink_square")
        #Blink all three symbols until they are made, then light solid.
            if s.game.special_game.position == 0:
                if s.game.circle.status == False:
                    blink_circle([s,1,1,(606,650)])
                else:
                    p = [606,650]
                    screen.blit(color, p)
                if s.game.triangle.status == False:
                    blink_triangle([s,1,1,(605,686)])
                else:
                    p = [605,686]
                    screen.blit(color, p)
                if s.game.square.status == False:
                    blink_square([s,1,1,(606,614)])
                else:
                    p = [606,614]
                    screen.blit(color, p)
            if s.game.special_game.position == 1:
                p = [606,650]
                screen.blit(color, p)
                p = [605,686]
                screen.blit(color, p)
                p = [606,614]
                screen.blit(color, p)
                if s.game.orange1.status == True:
                    blink_circle([s,1,1,(640,650)])
                if s.game.white1.status == True:
                    blink_square([s,1,1,(640,614)])
                if s.game.pink1.status == True:
                    blink_triangle([s,1,1,(640,686)])
            if s.game.special_game.position == 2:
                p = [606,650]
                screen.blit(color, p)
                p = [605,686]
                screen.blit(color, p)
                p = [606,614]
                screen.blit(color, p)
                if s.game.orange1.status == True:
                    p = [640,650]
                    screen.blit(color, p)
                if s.game.white1.status == True:
                    p = [640,614]
                    screen.blit(color, p)
                if s.game.pink1.status == True:
                    p = [640,686]
                    screen.blit(color, p)
                if s.game.orange2.status == True:
                    blink_circle([s,1,1,(674,650)])
                if s.game.white2.status == True:
                    blink_square([s,1,1,(674,614)])
                if s.game.pink2.status == True:
                    blink_triangle([s,1,1,(674,686)])

            if s.game.special_game.position == 3:
                p = [542,384]
                screen.blit(golden, p)
            if s.game.special_game.position in [1,2]:
                p = [542,438]
                screen.blit(dn, p)
            if s.game.special_replay_counter.position > 0:
                p = [542,334]
                screen.blit(collected, p)
    if s.game.missed.status == True:
        p = [542,545]
        screen.blit(missed, p)

    if s.game.special_odds.position == 1:
        p = [605,567]
        screen.blit(special_odds, p)
    elif s.game.special_odds.position == 2:
        p = [606,538]
        screen.blit(special_odds, p)
    elif s.game.special_odds.position == 3:
        p = [606,505]
        screen.blit(special_odds, p)
    elif s.game.special_odds.position == 4:
        p = [606,474]
        screen.blit(special_odds, p)
    elif s.game.special_odds.position == 5:
        p = [605,442]
        screen.blit(special_odds, p)
    elif s.game.special_odds.position == 6:
        p = [605,411]
        screen.blit(special_odds, p)
    elif s.game.special_odds.position == 7:
        p = [604,380]
        screen.blit(special_odds, p)
    elif s.game.special_odds.position == 8:
        p = [604,350]
        screen.blit(special_odds, p)
    elif s.game.special_odds.position == 9:
        p = [604,320]
        screen.blit(special_odds, p)

    if s.game.twin_number.position == 1:
        p = [200,740]
        screen.blit(ml_arrow, p)
    elif s.game.twin_number.position == 2:
        p = [232,740]
        screen.blit(ml_arrow, p)
    elif s.game.twin_number.position == 3:
        p = [265,740]
        screen.blit(ml_arrow, p)
    if s.game.twin_number.position >= 4:
        if s.game.eleven.status == True:
            p = [299,755]
            screen.blit(twin_number, p)
        if s.game.seventeen.status == True:
            p = [299,731]
            screen.blit(twin_number, p)
    if s.game.twin_number.position == 5:
        p = [366,740]
        screen.blit(ml_arrow, p)
    elif s.game.twin_number.position == 6:
        p = [398,740]
        screen.blit(ml_arrow, p)
    elif s.game.twin_number.position == 7:
        p = [430,740]
        screen.blit(ml_arrow, p)
    if s.game.twin_number.position == 8:
        if s.game.eleven.status == True:
            p = [462,730]
            screen.blit(twin_number, p)
        if s.game.seventeen.status == True:
            p = [462,754]
            screen.blit(twin_number, p)


    pygame.display.update()

def blink_circle(args):
    dirty_rects = []
    s = args[0]
    b = args[1]
    sn = args[2]
    p = args[3]

    if b == 0:
        if sn == 1:
            dirty_rects.append(screen.blit(color, p))
        pygame.display.update(dirty_rects)
    else:
        dirty_rects.append(screen.blit(bg_gi, (p[0],p[1]), pygame.Rect(p[0],p[1],35,37)))
        pygame.display.update(dirty_rects)
    b = not b

    args = [s,b,sn,p]

    s.delay(name="blink_circle", delay=0.3, handler=blink_circle, param=args)

def blink_square(args):
    dirty_rects = []
    s = args[0]
    b = args[1]
    sn = args[2]
    p = args[3]

    if b == 0:
        if sn == 1:
            dirty_rects.append(screen.blit(color, p))
        pygame.display.update(dirty_rects)
    else:
        dirty_rects.append(screen.blit(bg_gi, (p[0],p[1]), pygame.Rect(p[0],p[1],35,37)))
        pygame.display.update(dirty_rects)
    b = not b

    args = [s,b,sn,p]

    s.delay(name="blink_square", delay=0.3, handler=blink_square, param=args)

def blink_triangle(args):
    dirty_rects = []
    s = args[0]
    b = args[1]
    sn = args[2]
    p = args[3]

    if b == 0:
        if sn == 1:
            dirty_rects.append(screen.blit(color, p))
        pygame.display.update(dirty_rects)
    else:
        dirty_rects.append(screen.blit(bg_gi, (p[0],p[1]), pygame.Rect(p[0],p[1],35,37)))
        pygame.display.update(dirty_rects)
    b = not b

    args = [s,b,sn,p]

    s.delay(name="blink_triangle", delay=0.3, handler=blink_triangle, param=args)

def blink(args):
    dirty_rects = []
    s = args[0]
    b = args[1]
    sn = args[2]

    if b == 0:
        if sn == 1:
            p = [286,643]
            dirty_rects.append(screen.blit(select_now, p))
        pygame.display.update(dirty_rects)
    else:
        dirty_rects.append(screen.blit(bg_gi, (286,643), pygame.Rect(286,643,146,30)))
        pygame.display.update(dirty_rects)
    b = not b

    args = [s,b,sn]

    s.delay(name="blink", delay=0.1, handler=blink, param=args)

def eb_animation(num):
    global screen

    if num == 3:
        eb_position = [498,1044]
        screen.blit(eb_number, eb_position)
        pygame.display.update()
    if num == 2:
        eb_position = [548,1044]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 1:
        eb_position = [612,1044]
        screen.blit(eb, eb_position)
        pygame.display.update()

def feature_animation(num):
    global screen

    if num == 4:
        p = [458,680]
        screen.blit(ml_arrow, p)
        pygame.display.update()
    else:
        p = [492,680]
        screen.blit(ml_c, p)
        p = [410,590]
        screen.blit(ml_letter, p)
        pygame.display.update()


def odds_animation(num):
    global screen

    if num == 8:
        o = [192,783]
        screen.blit(odds, o)
    if num == 7:
        o = [242,783]
        screen.blit(odds, o)
    if num == 6:
        o = [290,783]
        screen.blit(odds, o)
    if num == 5:
        o = [339,783]
        screen.blit(odds, o)
    if num == 4:
        o = [387,783]
        screen.blit(odds, o)
    if num == 3:
        o = [433,783]
        screen.blit(odds, o)
    if num == 2:
        o = [481,783]
        screen.blit(odds, o)
    if num == 1:
        o = [529,783]
        screen.blit(odds, o)
    pygame.display.update()


