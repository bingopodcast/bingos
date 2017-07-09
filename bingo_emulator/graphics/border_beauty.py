
import pygame
import random

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

meter = pygame.image.load('graphics/assets/black_register_cover.png').convert()
odds = pygame.image.load('border_beauty/assets/odds.png').convert_alpha()
eb = pygame.image.load('border_beauty/assets/eb.png').convert_alpha()
eb_number = pygame.image.load('border_beauty/assets/eb_number.png').convert_alpha()
extra_balls = pygame.image.load('border_beauty/assets/extra_balls.png').convert_alpha()
time = pygame.image.load('border_beauty/assets/time.png').convert_alpha()
ml_letter = pygame.image.load('border_beauty/assets/ml_letter.png').convert_alpha()
ml_arrow = pygame.image.load('border_beauty/assets/ml_arrow.png').convert_alpha()
ml_a = pygame.image.load('border_beauty/assets/ml_a.png').convert_alpha()
ml_b = pygame.image.load('border_beauty/assets/ml_b.png').convert_alpha()
ml_c = pygame.image.load('border_beauty/assets/ml_c.png').convert_alpha()
select_now = pygame.image.load('border_beauty/assets/select_now.png').convert_alpha()
tilt = pygame.image.load('border_beauty/assets/tilt.png').convert_alpha()
button = pygame.image.load('border_beauty/assets/pap.png').convert_alpha()
red_double = pygame.image.load('border_beauty/assets/red_double.png').convert_alpha()
green_double = pygame.image.load('border_beauty/assets/green_double.png').convert_alpha()
yellow_double = pygame.image.load('border_beauty/assets/yellow_double.png').convert_alpha()
blue_double = pygame.image.load('border_beauty/assets/blue_double.png').convert_alpha()
four_stars = pygame.image.load('border_beauty/assets/four_stars.png').convert_alpha()
six_stars = pygame.image.load('border_beauty/assets/six_stars.png').convert_alpha()
three_stars = pygame.image.load('border_beauty/assets/three_stars.png').convert_alpha()
three_red = pygame.image.load('border_beauty/assets/three_red.png').convert_alpha()
two_red = pygame.image.load('border_beauty/assets/two_red.png').convert_alpha()
red_letter = pygame.image.load('border_beauty/assets/red_letter.png').convert_alpha()
letter1 = pygame.image.load('border_beauty/assets/letter1.png').convert_alpha()
letter2 = pygame.image.load('border_beauty/assets/letter2.png').convert_alpha()
letter3 = pygame.image.load('border_beauty/assets/letter3.png').convert_alpha()
letter4 = pygame.image.load('border_beauty/assets/letter4.png').convert_alpha()
letter5 = pygame.image.load('border_beauty/assets/letter5.png').convert_alpha()
letter6 = pygame.image.load('border_beauty/assets/letter6.png').convert_alpha()
red_letter1 = pygame.image.load('border_beauty/assets/red_letter1.png').convert_alpha()
red_letter2 = pygame.image.load('border_beauty/assets/red_letter2.png').convert_alpha()
red_letter3 = pygame.image.load('border_beauty/assets/red_letter3.png').convert_alpha()
red_letter4 = pygame.image.load('border_beauty/assets/red_letter4.png').convert_alpha()
red_letter5 = pygame.image.load('border_beauty/assets/red_letter5.png').convert_alpha()
red_letter6 = pygame.image.load('border_beauty/assets/red_letter6.png').convert_alpha()
number_card = pygame.image.load('border_beauty/assets/number_card.png').convert_alpha()
number = pygame.image.load('border_beauty/assets/number.png').convert_alpha()
columnb1 = pygame.image.load('border_beauty/assets/columnb1.png').convert_alpha()
columnb2 = pygame.image.load('border_beauty/assets/columnb2.png').convert_alpha()
columna = pygame.image.load('border_beauty/assets/columna.png').convert_alpha()
columnc1 = pygame.image.load('border_beauty/assets/columnc1.png').convert_alpha()
columnc2 = pygame.image.load('border_beauty/assets/columnc2.png').convert_alpha()

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
        backglass = pygame.image.load('border_beauty/assets/border_beauty_menu.png').convert_alpha()
    else:
        if (s.game.anti_cheat.status == True):
            backglass = pygame.image.load('border_beauty/assets/border_beauty_gi.png').convert_alpha()
        else:
            backglass = pygame.image.load('border_beauty/assets/border_beauty_off.png').convert_alpha()
    backglass = pygame.transform.scale(backglass, (720, 1280))
    
    screen.blit(backglass, backglass_position)


    if s.game.eb_play.status == True:
        eb_position = [37,1030]
        screen.blit(extra_balls, eb_position)

    if s.game.extra_ball.position >= 1:
        eb_position = [142,1032]
        screen.blit(eb_number, eb_position)
    if s.game.extra_ball.position >= 2:
        eb_position = [192,1032]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 3:
        eb_position = [255,1033]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 4:
        eb_position = [319,1034]
        screen.blit(eb_number, eb_position)
    if s.game.extra_ball.position >= 5:
        eb_position = [369,1034]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 6:
        eb_position = [432,1033]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 7:
        eb_position = [496,1032]
        screen.blit(eb_number, eb_position)
    if s.game.extra_ball.position >= 8:
        eb_position = [546,1031]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 9:
        eb_position = [609,1031]
        screen.blit(eb, eb_position)

    if s.game.red_star.status == True:
        rs_position = [560,467]
        screen.blit(time, rs_position)
    if s.game.yellow_star.status == True:
        rs_position = [560,520]
        screen.blit(time, rs_position)

    if s.game.mystic_lines.position >= 4 or s.game.two_red_letter.status == True or s.game.three_red_letter.status == True:
        if s.game.selection_feature.position < 7:
            bfp = [559,577]
            screen.blit(time, bfp)
        elif s.game.selection_feature.position in [7,8]:
            bfp = [558,412]
            screen.blit(time, bfp)
        elif s.game.selection_feature.position == 9:
            bfp = [558,356]
            screen.blit(time, bfp)

    if s.game.ball_count.position < 1:
        if s.game.odds_only.status == True:
            b = [16,873]
            screen.blit(button, b)
        elif s.game.features.status == True:
            b = [18,916]
            screen.blit(button, b)
        else:
            b = [19,957]
            screen.blit(button, b)


    if s.game.mystic_lines.position == 1:
        p = [198,703]
        screen.blit(ml_arrow, p)
    if s.game.mystic_lines.position == 2:
        p = [231,703]
        screen.blit(ml_arrow, p)
    if s.game.mystic_lines.position == 3:
        p = [264,703]
        screen.blit(ml_arrow, p)
    if s.game.mystic_lines.position >= 4:
        p = [290,697]
        screen.blit(ml_a, p)
        p = [337,575]
        screen.blit(ml_letter, p)
    if s.game.mystic_lines.position == 5:
        p = [330,703]
        screen.blit(ml_arrow, p)
    if s.game.mystic_lines.position == 6:
        p = [364,703]
        screen.blit(ml_arrow, p)
    if s.game.mystic_lines.position >= 7:
        p = [391,697]
        screen.blit(ml_b, p)
        p = [260,575]
        screen.blit(ml_letter, p)
    if s.game.mystic_lines.position == 8:
        p = [430,703]
        screen.blit(ml_arrow, p)
    if s.game.mystic_lines.position == 9:
        p = [463,703]
        screen.blit(ml_arrow, p)
    if s.game.mystic_lines.position == 10:
        p = [487,697]
        screen.blit(ml_c, p)
        p = [416,576]
        screen.blit(ml_letter, p)

    if s.game.mystic_lines.position >= 4:
        t = 4
        if s.game.selection_feature.position in [7,8]:
            t = 5
        if s.game.selection_feature.position == 9:
            t = 6
        if s.game.ball_count.position == t:
            p = [523,716]
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
        o = [208,769]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 2:
        o = [267,769]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 3:
        o = [327,769]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 4:
        o = [388,769]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 5:
        o = [444,769]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 6:
        o = [504,769]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 7:
        o = [563,769]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 8:
        o = [620,769]
        screen.blit(odds, o)

    if s.game.yellow_odds.position == 1:
        o = [208,895]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 2:
        o = [267,895]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 3:
        o = [327,895]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 4:
        o = [388,895]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 5:
        o = [444,895]
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
        o = [208,831]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 2:
        o = [267,831]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 3:
        o = [327,831]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 4:
        o = [388,831]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 5:
        o = [444,831]
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
        o = [208,959]
        screen.blit(odds, o)
    elif s.game.blue_odds.position == 2:
        o = [267,959]
        screen.blit(odds, o)
    elif s.game.blue_odds.position == 3:
        o = [327,959]
        screen.blit(odds, o)
    elif s.game.blue_odds.position == 4:
        o = [388,959]
        screen.blit(odds, o)
    elif s.game.blue_odds.position == 5:
        o = [444,959]
        screen.blit(odds, o)
    elif s.game.blue_odds.position == 6:
        o = [504,959]
        screen.blit(odds, o)
    elif s.game.blue_odds.position == 7:
        o = [563,959]
        screen.blit(odds, o)
    elif s.game.blue_odds.position == 8:
        o = [620,959]
        screen.blit(odds, o)

    p = [22,249]
    screen.blit(letter1, p)
    p = [76,238]
    screen.blit(letter2, p)
    p = [128,230]
    screen.blit(letter3, p)
    p = [181,222]
    screen.blit(letter4, p)
    p = [240,221]
    screen.blit(letter5, p)
    p = [286,220]
    screen.blit(letter6, p)

    if s.game.red_odds.position < 4:
        p = [22,249]
        screen.blit(red_letter1, p)
    if s.game.red_odds.position == 4:
        p = [76,238]
        screen.blit(red_letter2, p)
    if s.game.red_odds.position == 5:
        p = [128,230]
        screen.blit(red_letter3, p)
    if s.game.red_odds.position == 6:
        p = [181,222]
        screen.blit(red_letter4, p)
    if s.game.red_odds.position == 7:
        p = [240,221]
        screen.blit(red_letter5, p)
    if s.game.red_odds.position == 8:
        p = [286,220]
        screen.blit(red_letter6, p)

    if s.game.two_red_letter.status == True:
        p = [9,404]
        screen.blit(red_letter, p)
        p = [84,351]
        screen.blit(two_red, p)
    if s.game.three_red_letter.status == True:
        p = [9,404]
        screen.blit(red_letter, p)
        p = [9,353]
        screen.blit(three_red, p)

    if s.game.three_stars.status == True:
        p = [9,446]
        screen.blit(four_stars, p)
        p = [9,497]
        screen.blit(three_stars, p)
    if s.game.six_stars.status == True:
        p = [9,446]
        screen.blit(four_stars, p)
        p = [82,495]
        screen.blit(six_stars, p)

    if s.game.double_red.status == True:
        p = [8,556]
        screen.blit(red_double, p)
    if s.game.double_yellow.status == True:
        p = [87,555]
        screen.blit(yellow_double, p)
    if s.game.double_green.status == True:
        p = [8,633]
        screen.blit(green_double, p)
    if s.game.double_blue.status == True:
        p = [87,633]
        screen.blit(blue_double, p)

    if s.game.tilt.status == True:
        tilt_position = [551,317]
        screen.blit(tilt, tilt_position)

    pygame.display.update()

def eb_animation(num):
    global screen

    if num == 3:
        eb_position = [142,1032]
        screen.blit(eb_number, eb_position)
        pygame.display.update()
    if num == 2:
        eb_position = [192,1032]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 1:
        eb_position = [255,1033]
        screen.blit(eb, eb_position)
        pygame.display.update()

def feature_animation(num):
    global screen

    if num == 4:
        p = [465,706]
        screen.blit(ml_arrow, p)
        pygame.display.update()
    else:
        p = [493,700]
        screen.blit(ml_c, p)
        p = [418,578]
        screen.blit(ml_letter, p)
        pygame.display.update()


def odds_animation(num):
    global screen
    if num == 8:
        o = [211,769]
        screen.blit(odds, o)
    if num == 7:
        o = [270,895]
        screen.blit(odds, o)
    if num == 6:
        o = [329,831]
        screen.blit(odds, o)
    if num == 5:
        o = [388,959]
        screen.blit(odds, o)
    if num == 4:
        o = [448,769]
        screen.blit(odds, o)
    if num == 3:
        o = [508,895]
        screen.blit(odds, o)
    if num == 2:
        o = [565,831]
        screen.blit(odds, o)
    if num == 1:
        o = [620,959]
        screen.blit(odds, o)
    pygame.display.update()


