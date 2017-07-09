
import pygame
import random

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

meter = pygame.image.load('graphics/assets/black_register_cover.png').convert()
odds = pygame.image.load('beauty_beach/assets/odds.png').convert_alpha()
eb = pygame.image.load('beauty_beach/assets/eb.png').convert_alpha()
eb_number = pygame.image.load('beauty_beach/assets/eb_number.png').convert_alpha()
extra_balls = pygame.image.load('beauty_beach/assets/extra_balls.png').convert_alpha()
time = pygame.image.load('beauty_beach/assets/time.png').convert_alpha()
ml_letter = pygame.image.load('beauty_beach/assets/ml_letter.png').convert_alpha()
ml_arrow = pygame.image.load('beauty_beach/assets/ml_arrow.png').convert_alpha()
ml_a = pygame.image.load('beauty_beach/assets/ml_a.png').convert_alpha()
ml_b = pygame.image.load('beauty_beach/assets/ml_b.png').convert_alpha()
ml_c = pygame.image.load('beauty_beach/assets/ml_c.png').convert_alpha()
select_now = pygame.image.load('beauty_beach/assets/select_now.png').convert_alpha()
tilt = pygame.image.load('beauty_beach/assets/tilt.png').convert_alpha()
button = pygame.image.load('beauty_beach/assets/pap.png').convert_alpha()
red_double = pygame.image.load('beauty_beach/assets/red_double.png').convert_alpha()
green_double = pygame.image.load('beauty_beach/assets/green_double.png').convert_alpha()
yellow_double = pygame.image.load('beauty_beach/assets/yellow_double.png').convert_alpha()
blue_double = pygame.image.load('beauty_beach/assets/blue_double.png').convert_alpha()
four_stars = pygame.image.load('beauty_beach/assets/four_stars.png').convert_alpha()
six_stars = pygame.image.load('beauty_beach/assets/six_stars.png').convert_alpha()
three_stars = pygame.image.load('beauty_beach/assets/three_stars.png').convert_alpha()
three_red = pygame.image.load('beauty_beach/assets/three_red.png').convert_alpha()
two_red = pygame.image.load('beauty_beach/assets/two_red.png').convert_alpha()
red_letter = pygame.image.load('beauty_beach/assets/red_letter.png').convert_alpha()
letter1 = pygame.image.load('beauty_beach/assets/letter1.png').convert_alpha()
letter2 = pygame.image.load('beauty_beach/assets/letter2.png').convert_alpha()
letter3 = pygame.image.load('beauty_beach/assets/letter3.png').convert_alpha()
letter4 = pygame.image.load('beauty_beach/assets/letter4.png').convert_alpha()
letter5 = pygame.image.load('beauty_beach/assets/letter5.png').convert_alpha()
letter6 = pygame.image.load('beauty_beach/assets/letter6.png').convert_alpha()
red_letter1 = pygame.image.load('beauty_beach/assets/red_letter1.png').convert_alpha()
red_letter2 = pygame.image.load('beauty_beach/assets/red_letter2.png').convert_alpha()
red_letter3 = pygame.image.load('beauty_beach/assets/red_letter3.png').convert_alpha()
red_letter4 = pygame.image.load('beauty_beach/assets/red_letter4.png').convert_alpha()
red_letter5 = pygame.image.load('beauty_beach/assets/red_letter5.png').convert_alpha()
red_letter6 = pygame.image.load('beauty_beach/assets/red_letter6.png').convert_alpha()
number_card = pygame.image.load('beauty_beach/assets/number_card.png').convert_alpha()
number = pygame.image.load('beauty_beach/assets/number.png').convert_alpha()
columnb1 = pygame.image.load('beauty_beach/assets/columnb1.png').convert_alpha()
columnb2 = pygame.image.load('beauty_beach/assets/columnb2.png').convert_alpha()
columna = pygame.image.load('beauty_beach/assets/columna.png').convert_alpha()
columnc1 = pygame.image.load('beauty_beach/assets/columnc1.png').convert_alpha()
columnc2 = pygame.image.load('beauty_beach/assets/columnc2.png').convert_alpha()
double_triple = pygame.image.load('beauty_beach/assets/double_triple.png').convert_alpha()

class scorereel():
    """ Score Reels are used to count replays """
    def __init__(self, pos, image):
        self.position = pos
        self.default_y = self.position[1]
        self.image = pygame.image.load(image).convert()

reel1 = scorereel([109,799], "graphics/assets/white_reel.png")
reel10 = scorereel([90,799], "graphics/assets/white_reel.png")
reel100 = scorereel([71,799], "graphics/assets/white_reel.png")
reel1000 = scorereel([52,799], "graphics/assets/white_reel.png")

def display(s, replays=0, menu=False):
    
    meter.set_colorkey((255,0,252))
    meter_position = [43,799]

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
        backglass = pygame.image.load('beauty_beach/assets/beauty_beach_menu.png').convert_alpha()
    else:
        if (s.game.anti_cheat.status == True):
            backglass = pygame.image.load('beauty_beach/assets/beauty_beach_gi.png').convert_alpha()
        else:
            backglass = pygame.image.load('beauty_beach/assets/beauty_beach_off.png').convert_alpha()
    backglass = pygame.transform.scale(backglass, (720, 1280))
    
    screen.blit(backglass, backglass_position)


    if s.game.eb_play.status == True:
        eb_position = [37,1036]
        screen.blit(extra_balls, eb_position)

    if s.game.extra_ball.position >= 1:
        eb_position = [142,1036]
        screen.blit(eb_number, eb_position)
    if s.game.extra_ball.position >= 2:
        eb_position = [192,1036]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 3:
        eb_position = [255,1036]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 4:
        eb_position = [319,1036]
        screen.blit(eb_number, eb_position)
    if s.game.extra_ball.position >= 5:
        eb_position = [369,1036]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 6:
        eb_position = [432,1036]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 7:
        eb_position = [496,1036]
        screen.blit(eb_number, eb_position)
    if s.game.extra_ball.position >= 8:
        eb_position = [546,1036]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 9:
        eb_position = [609,1036]
        screen.blit(eb, eb_position)

    if s.game.red_star.status == True:
        rs_position = [560,462]
        screen.blit(time, rs_position)
    if s.game.yellow_star.status == True:
        rs_position = [560,515]
        screen.blit(time, rs_position)

    if s.game.mystic_lines.position >= 4 or s.game.two_red_letter.status == True or s.game.three_red_letter.status == True:
        if s.game.selection_feature.position < 7:
            bfp = [559,569]
            screen.blit(time, bfp)
        elif s.game.selection_feature.position in [7,8]:
            bfp = [558,406]
            screen.blit(time, bfp)
        elif s.game.selection_feature.position == 9:
            bfp = [558,351]
            screen.blit(time, bfp)

    if s.game.ball_count.position < 1:
        if s.game.odds_only.status == True:
            b = [16,873]
            screen.blit(button, b)
        elif s.game.features.status == True:
            b = [18,916]
            screen.blit(button, b)
        else:
            b = [19,961]
            screen.blit(button, b)


    if s.game.mystic_lines.position == 1:
        p = [203,699]
        screen.blit(ml_arrow, p)
    if s.game.mystic_lines.position == 2:
        p = [235,699]
        screen.blit(ml_arrow, p)
    if s.game.mystic_lines.position == 3:
        p = [268,699]
        screen.blit(ml_arrow, p)
    if s.game.mystic_lines.position >= 4:
        p = [294,691]
        screen.blit(ml_a, p)
        p = [341,584]
        screen.blit(ml_letter, p)
    if s.game.mystic_lines.position == 5:
        p = [333,699]
        screen.blit(ml_arrow, p)
    if s.game.mystic_lines.position == 6:
        p = [366,699]
        screen.blit(ml_arrow, p)
    if s.game.mystic_lines.position >= 7:
        p = [392,691]
        screen.blit(ml_b, p)
        p = [265,584]
        screen.blit(ml_letter, p)
    if s.game.mystic_lines.position == 8:
        p = [430,699]
        screen.blit(ml_arrow, p)
    if s.game.mystic_lines.position == 9:
        p = [462,699]
        screen.blit(ml_arrow, p)
    if s.game.mystic_lines.position == 10:
        p = [488,690]
        screen.blit(ml_c, p)
        p = [417,584]
        screen.blit(ml_letter, p)

    if s.game.mystic_lines.position >= 4:
        t = 4
        if s.game.selection_feature.position in [7,8]:
            t = 5
        if s.game.selection_feature.position == 9:
            t = 6
        if s.game.ball_count.position == t:
            p = [521,710]
            screen.blit(select_now, p)

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
        o = [212,765]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 2:
        o = [269,765]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 3:
        o = [327,765]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 4:
        o = [388,765]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 5:
        o = [445,763]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 6:
        o = [504,763]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 7:
        o = [562,765]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 8:
        o = [620,765]
        screen.blit(odds, o)

    if s.game.yellow_odds.position == 1:
        o = [212,895]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 2:
        o = [269,895]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 3:
        o = [327,895]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 4:
        o = [388,895]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 5:
        o = [445,895]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 6:
        o = [504,895]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 7:
        o = [563,895]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 8:
        o = [620,895]
        screen.blit(odds, o)

    if s.game.green_odds.position == 1:
        o = [212,831]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 2:
        o = [269,831]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 3:
        o = [327,831]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 4:
        o = [388,831]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 5:
        o = [445,831]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 6:
        o = [504,831]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 7:
        o = [563,831]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 8:
        o = [620,831]
        screen.blit(odds, o)

    if s.game.blue_odds.position == 1:
        o = [212,959]
        screen.blit(odds, o)
    elif s.game.blue_odds.position == 2:
        o = [269,959]
        screen.blit(odds, o)
    elif s.game.blue_odds.position == 3:
        o = [327,959]
        screen.blit(odds, o)
    elif s.game.blue_odds.position == 4:
        o = [388,959]
        screen.blit(odds, o)
    elif s.game.blue_odds.position == 5:
        o = [445,959]
        screen.blit(odds, o)
    elif s.game.blue_odds.position == 6:
        o = [504,959]
        screen.blit(odds, o)
    elif s.game.blue_odds.position == 7:
        o = [561,960]
        screen.blit(odds, o)
    elif s.game.blue_odds.position == 8:
        o = [618,960]
        screen.blit(odds, o)

    p = [46,215]
    screen.blit(letter1, p)
    p = [94,215]
    screen.blit(letter2, p)
    p = [134,215]
    screen.blit(letter3, p)
    p = [185,213]
    screen.blit(letter4, p)
    p = [242,212]
    screen.blit(letter5, p)
    p = [278,213]
    screen.blit(letter6, p)

    if s.game.red_odds.position < 4:
        p = [46,215]
        screen.blit(red_letter1, p)
    if s.game.red_odds.position == 4:
        p = [94,215]
        screen.blit(red_letter2, p)
    if s.game.red_odds.position == 5:
        p = [134,215]
        screen.blit(red_letter3, p)
    if s.game.red_odds.position == 6:
        p = [185,213]
        screen.blit(red_letter4, p)
    if s.game.red_odds.position == 7:
        p = [242,212]
        screen.blit(red_letter5, p)
    if s.game.red_odds.position == 8:
        p = [278,213]
        screen.blit(red_letter6, p)

    if s.game.two_red_letter.status == True:
        p = [16,401]
        screen.blit(red_letter, p)
        p = [93,349]
        screen.blit(two_red, p)
    if s.game.three_red_letter.status == True:
        p = [16,401]
        screen.blit(red_letter, p)
        p = [18,349]
        screen.blit(three_red, p)

    if s.game.three_stars.status == True:
        p = [15,442]
        screen.blit(four_stars, p)
        p = [15,496]
        screen.blit(three_stars, p)
    if s.game.six_stars.status == True:
        p = [15,442]
        screen.blit(four_stars, p)
        p = [92,494]
        screen.blit(six_stars, p)

    if s.game.double_red.status == True:
        p = [21,555]
        screen.blit(red_double, p)
    if s.game.double_yellow.status == True:
        p = [93,555]
        screen.blit(yellow_double, p)
    if s.game.double_green.status == True:
        p = [18,657]
        screen.blit(green_double, p)
    if s.game.double_blue.status == True:
        p = [93,657]
        screen.blit(blue_double, p)

    if s.game.triple.status == False and (s.game.double_red.status == True or s.game.double_yellow.status == True or s.game.double_green.status == True or s.game.double_blue.status == True):
        p = [51,657]
        screen.blit(double_triple, p)
    
    if s.game.triple.status == True and (s.game.double_red.status == True or s.game.double_yellow.status == True or s.game.double_green.status == True or s.game.double_blue.status == True):
        p = [51,602]
        screen.blit(double_triple, p)

    if s.game.tilt.status == True:
        tilt_position = [551,317]
        screen.blit(tilt, tilt_position)

    pygame.display.update()

def eb_animation(num):
    global screen

    if num == 3:
        eb_position = [142,1036]
        screen.blit(eb_number, eb_position)
        pygame.display.update()
    if num == 2:
        eb_position = [192,1036]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 1:
        eb_position = [255,1036]
        screen.blit(eb, eb_position)
        pygame.display.update()

def feature_animation(num):
    global screen

    if num == 4:
        p = [462,699]
        screen.blit(ml_arrow, p)
        pygame.display.update()
    else:
        p = [488,690]
        screen.blit(ml_c, p)
        p = [417,584]
        screen.blit(ml_letter, p)
        pygame.display.update()


def odds_animation(num):
    global screen

    if num == 8:
        o = [212,959]
        screen.blit(odds, o)
    if num == 7:
        o = [269,959]
        screen.blit(odds, o)
    if num == 6:
        o = [327,959]
        screen.blit(odds, o)
    if num == 5:
        o = [388,959]
        screen.blit(odds, o)
    if num == 4:
        o = [445,959]
        screen.blit(odds, o)
    if num == 3:
        o = [504,959]
        screen.blit(odds, o)
    if num == 2:
        o = [561,960]
        screen.blit(odds, o)
    if num == 1:
        o = [618,960]
        screen.blit(odds, o)
    pygame.display.update()

