
import pygame
import random

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

meter = pygame.image.load('graphics/assets/black_register_cover.png').convert()
odds = pygame.image.load('orient/assets/odds.png').convert_alpha()
eb = pygame.image.load('orient/assets/eb.png').convert_alpha()
eb_number = pygame.image.load('orient/assets/eb_number.png').convert_alpha()
extra_balls = pygame.image.load('orient/assets/extra_balls.png').convert_alpha()
time = pygame.image.load('orient/assets/time.png').convert_alpha()
ml_letter = pygame.image.load('orient/assets/ml_letter.png').convert_alpha()
ml_arrow = pygame.image.load('orient/assets/ml_arrow.png').convert_alpha()
ml_a = pygame.image.load('orient/assets/ml_a.png').convert_alpha()
select_now = pygame.image.load('orient/assets/select_now.png').convert_alpha()
tilt = pygame.image.load('orient/assets/tilt.png').convert_alpha()
button = pygame.image.load('orient/assets/pap.png').convert_alpha()
red_double = pygame.image.load('orient/assets/red_double.png').convert_alpha()
green_double = pygame.image.load('orient/assets/green_double.png').convert_alpha()
yellow_double = pygame.image.load('orient/assets/yellow_double.png').convert_alpha()
blue_double = pygame.image.load('orient/assets/blue_double.png').convert_alpha()
four_stars = pygame.image.load('orient/assets/four_stars.png').convert_alpha()
six_stars = pygame.image.load('orient/assets/six_stars.png').convert_alpha()
three_stars = pygame.image.load('orient/assets/three_stars.png').convert_alpha()
three_red = pygame.image.load('orient/assets/three_red.png').convert_alpha()
two_red = pygame.image.load('orient/assets/two_red.png').convert_alpha()
red_letter = pygame.image.load('orient/assets/red_letter.png').convert_alpha()
letter1 = pygame.image.load('orient/assets/letter1.png').convert_alpha()
letter2 = pygame.image.load('orient/assets/letter2.png').convert_alpha()
letter3 = pygame.image.load('orient/assets/letter3.png').convert_alpha()
letter4 = pygame.image.load('orient/assets/letter4.png').convert_alpha()
letter5 = pygame.image.load('orient/assets/letter5.png').convert_alpha()
letter6 = pygame.image.load('orient/assets/letter6.png').convert_alpha()
red_letter1 = pygame.image.load('orient/assets/red_letter1.png').convert_alpha()
red_letter2 = pygame.image.load('orient/assets/red_letter2.png').convert_alpha()
red_letter3 = pygame.image.load('orient/assets/red_letter3.png').convert_alpha()
red_letter4 = pygame.image.load('orient/assets/red_letter4.png').convert_alpha()
red_letter5 = pygame.image.load('orient/assets/red_letter5.png').convert_alpha()
red_letter6 = pygame.image.load('orient/assets/red_letter6.png').convert_alpha()
number_card = pygame.image.load('orient/assets/number_card.png').convert_alpha()
number = pygame.image.load('orient/assets/number.png').convert_alpha()
columnb1 = pygame.image.load('orient/assets/columnb1.png').convert_alpha()
columnb2 = pygame.image.load('orient/assets/columnb2.png').convert_alpha()
columna = pygame.image.load('orient/assets/columna.png').convert_alpha()
columnc1 = pygame.image.load('orient/assets/columnc1.png').convert_alpha()
columnc2 = pygame.image.load('orient/assets/columnc2.png').convert_alpha()
double_triple = pygame.image.load('orient/assets/double_triple.png').convert_alpha()
top = pygame.image.load('orient/assets/top.png').convert_alpha()
bottom = pygame.image.load('orient/assets/bottom.png').convert_alpha()
ball = pygame.image.load('orient/assets/ball.png').convert_alpha()
eo = pygame.image.load('orient/assets/eo.png').convert_alpha()
dn = pygame.image.load('orient/assets/dn.png').convert_alpha()
collected = pygame.image.load('orient/assets/collected.png').convert_alpha()
missed = pygame.image.load('orient/assets/missed.png').convert_alpha()
special_odds = pygame.image.load('orient/assets/special_odds.png').convert_alpha()
golden = pygame.image.load('orient/assets/golden.png').convert_alpha()
bg_menu = pygame.image.load('orient/assets/orient_menu.png').convert_alpha()
bg_gi = pygame.image.load('orient/assets/orient_gi.png').convert_alpha()
bg_off = pygame.image.load('orient/assets/orient_off.png').convert_alpha()

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
        eb_position = [38,1041]
        screen.blit(extra_balls, eb_position)

    if s.game.extra_ball.position >= 1:
        eb_position = [147,1043]
        screen.blit(eb_number, eb_position)
    if s.game.extra_ball.position >= 2:
        eb_position = [197,1043]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 3:
        eb_position = [261,1043]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 4:
        eb_position = [322,1043]
        screen.blit(eb_number, eb_position)
    if s.game.extra_ball.position >= 5:
        eb_position = [373,1044]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 6:
        eb_position = [434,1043]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 7:
        eb_position = [498,1044]
        screen.blit(eb_number, eb_position)
    if s.game.extra_ball.position >= 8:
        eb_position = [548,1045]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 9:
        eb_position = [612,1044]
        screen.blit(eb, eb_position)

    if s.game.red_star.status == True:
        rs_position = [19,463]
        screen.blit(button, rs_position)
    if s.game.yellow_star.status == True:
        rs_position = [19,507]
        screen.blit(button, rs_position)

    if s.game.mystic_lines.position >= 4 or s.game.two_red_letter.status == True or s.game.three_red_letter.status == True:
        if s.game.selection_feature.position < 7:
            bfp = [19,552]
            screen.blit(bottom, bfp)
        elif s.game.selection_feature.position in [7,8]:
            bfp = [19,417]
            screen.blit(button, bfp)
        elif s.game.selection_feature.position == 9:
            bfp = [17,372]
            screen.blit(top, bfp)

    if s.game.ball_count.position < 1:
        if s.game.odds_only.status == True:
            b = [20,877]
            screen.blit(top, b)
        elif s.game.features.status == True:
            b = [21,916]
            screen.blit(button, b)
        elif s.game.special.status == True:
            b = [21,1000]
            screen.blit(bottom, b)
        else:
            b = [21,956]
            screen.blit(button, b)


    if s.game.mystic_lines.position == 1:
        p = [204,687]
        screen.blit(ml_arrow, p)
    if s.game.mystic_lines.position == 2:
        p = [236,687]
        screen.blit(ml_arrow, p)
    if s.game.mystic_lines.position == 3:
        p = [269,687]
        screen.blit(ml_arrow, p)
    if s.game.mystic_lines.position >= 4:
        p = [295,681]
        screen.blit(ml_a, p)
        p = [341,595]
        screen.blit(ml_letter, p)
    if s.game.mystic_lines.position == 5:
        p = [334,687]
        screen.blit(ml_arrow, p)
    if s.game.mystic_lines.position == 6:
        p = [366,687]
        screen.blit(ml_arrow, p)
    if s.game.mystic_lines.position >= 7:
        p = [392,681]
        screen.blit(ml_a, p)
        p = [265,595]
        screen.blit(ml_letter, p)
    if s.game.mystic_lines.position == 8:
        p = [433,687]
        screen.blit(ml_arrow, p)
    if s.game.mystic_lines.position == 9:
        p = [463,687]
        screen.blit(ml_arrow, p)
    if s.game.mystic_lines.position == 10:
        p = [489,681]
        screen.blit(ml_a, p)
        p = [416,595]
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
                    p = [336,419]
                    screen.blit(number, p)

    if s.game.red_odds.position == 1:
        o = [175,773]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 2:
        o = [223,773]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 3:
        o = [275,773]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 4:
        o = [324,773]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 5:
        o = [375,773]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 6:
        o = [425,773]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 7:
        o = [473,773]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 8:
        o = [525,773]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 9:
        o = [576,773]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 10:
        o = [625,773]
        screen.blit(odds, o)

    if s.game.yellow_odds.position == 1:
        o = [175,905]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 2:
        o = [223,905]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 3:
        o = [275,905]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 4:
        o = [324,905]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 5:
        o = [375,905]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 6:
        o = [424,905]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 7:
        o = [473,905]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 8:
        o = [525,905]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 9:
        o = [576,905]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 10:
        o = [625,905]
        screen.blit(odds, o)

    if s.game.green_odds.position == 1:
        o = [175,842]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 2:
        o = [223,842]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 3:
        o = [275,842]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 4:
        o = [324,842]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 5:
        o = [375,842]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 6:
        o = [424,842]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 7:
        o = [473,842]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 8:
        o = [525,842]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 9:
        o = [576,842]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 10:
        o = [625,840]
        screen.blit(odds, o)

    if s.game.blue_odds.position == 1:
        o = [175,970]
        screen.blit(odds, o)
    elif s.game.blue_odds.position == 2:
        o = [223,970]
        screen.blit(odds, o)
    elif s.game.blue_odds.position == 3:
        o = [275,970]
        screen.blit(odds, o)
    elif s.game.blue_odds.position == 4:
        o = [324,970]
        screen.blit(odds, o)
    elif s.game.blue_odds.position == 5:
        o = [375,970]
        screen.blit(odds, o)
    elif s.game.blue_odds.position == 6:
        o = [424,970]
        screen.blit(odds, o)
    elif s.game.blue_odds.position == 7:
        o = [473,970]
        screen.blit(odds, o)
    elif s.game.blue_odds.position == 8:
        o = [525,970]
        screen.blit(odds, o)
    elif s.game.blue_odds.position == 9:
        o = [574,970]
        screen.blit(odds, o)
    elif s.game.blue_odds.position == 10:
        o = [622,970]
        screen.blit(odds, o)

    p = [381,207]
    screen.blit(letter1, p)
    p = [425,197]
    screen.blit(letter2, p)
    p = [489,206]
    screen.blit(letter3, p)
    p = [520,209]
    screen.blit(letter4, p)
    p = [568,211]
    screen.blit(letter5, p)
    p = [637,203]
    screen.blit(letter6, p)

    if s.game.red_odds.position < 5:
        p = [381,207]
        screen.blit(red_letter1, p)
    if s.game.red_odds.position in [5,6]:
        p = [425,197]
        screen.blit(red_letter2, p)
    if s.game.red_odds.position == 7:
        p = [489,206]
        screen.blit(red_letter3, p)
    if s.game.red_odds.position == 8:
        p = [520,209]
        screen.blit(red_letter4, p)
    if s.game.red_odds.position == 9:
        p = [568,211]
        screen.blit(red_letter5, p)
    if s.game.red_odds.position == 10:
        p = [637,203]
        screen.blit(red_letter6, p)

    if s.game.two_red_letter.status == True:
        p = [17,255]
        screen.blit(red_letter, p)
        p = [91,217]
        screen.blit(two_red, p)
    if s.game.three_red_letter.status == True:
        p = [17,255]
        screen.blit(red_letter, p)
        p = [17,216]
        screen.blit(three_red, p)

    if s.game.three_stars.status == True:
        p = [17,294]
        screen.blit(four_stars, p)
        p = [17,333]
        screen.blit(three_stars, p)
    if s.game.six_stars.status == True:
        p = [17,294]
        screen.blit(four_stars, p)
        p = [91,334]
        screen.blit(six_stars, p)

    if s.game.double_red.status == True:
        p = [20,613]
        screen.blit(red_double, p)
    if s.game.double_yellow.status == True:
        p = [94,611]
        screen.blit(yellow_double, p)
    if s.game.double_green.status == True:
        p = [21,685]
        screen.blit(green_double, p)
    if s.game.double_blue.status == True:
        p = [95,685]
        screen.blit(blue_double, p)

    if s.game.triple.status == False and (s.game.double_red.status == True or s.game.double_yellow.status == True or s.game.double_green.status == True or s.game.double_blue.status == True):
        p = [56,685]
        screen.blit(double_triple, p)

    if s.game.triple.status == True and (s.game.double_red.status == True or s.game.double_yellow.status == True or s.game.double_green.status == True or s.game.double_blue.status == True):
        p = [56,651]
        screen.blit(double_triple, p)

    if s.game.tilt.status == True:
        tilt_position = [327,325]
        screen.blit(tilt, tilt_position)

    # Special Game
    if s.game.missed.status == False:
        if s.game.special_odds.position > 0:
            if s.game.special_game.position == 0:
                p = [527,697]
                screen.blit(eo, p)
            if s.game.special_game.position == 1:
                p = [527,608]
                screen.blit(ball, p)
                p = [617,700]
                screen.blit(eo, p)
            if s.game.special_game.position == 2:
                p = [562,609]
                screen.blit(ball, p)
                p = [527,697]
                screen.blit(eo, p)
            if s.game.special_game.position == 3:
                p = [598,611]
                screen.blit(ball, p)
                p = [617,700]
                screen.blit(eo, p)
            if s.game.special_game.position == 4:
                p = [634,612]
                screen.blit(ball, p)
                p = [527,697]
                screen.blit(eo, p)
            if s.game.special_game.position == 5:
                p = [668,613]
                screen.blit(ball, p)
                p = [536,398]
                screen.blit(golden, p)
            if s.game.special_game.position in [3,4]:
                p = [535,455]
                screen.blit(dn, p)
            if s.game.special_replay_counter.position > 0:
                p = [535,347]
                screen.blit(collected, p)
    if s.game.missed.status == True:
        p = [533,563]
        screen.blit(missed, p)

    if s.game.special_odds.position == 1:
        p = [599,577]
        screen.blit(special_odds, p)
    elif s.game.special_odds.position == 2:
        p = [599,544]
        screen.blit(special_odds, p)
    elif s.game.special_odds.position == 3:
        p = [599,511]
        screen.blit(special_odds, p)
    elif s.game.special_odds.position == 4:
        p = [599,478]
        screen.blit(special_odds, p)
    elif s.game.special_odds.position == 5:
        p = [599,443]
        screen.blit(special_odds, p)
    elif s.game.special_odds.position == 6:
        p = [599,411]
        screen.blit(special_odds, p)
    elif s.game.special_odds.position == 7:
        p = [599,377]
        screen.blit(special_odds, p)
    elif s.game.special_odds.position == 8:
        p = [600,344]
        screen.blit(special_odds, p)

    pygame.display.update()

def blink(args):
    dirty_rects = []
    s = args[0]
    b = args[1]
    sn = args[2]

    if b == 0:
        if sn == 1:
            p = [390,724]
            dirty_rects.append(screen.blit(select_now, p))
        pygame.display.update(dirty_rects)
    else:
        dirty_rects.append(screen.blit(bg_gi, (390,724), pygame.Rect(390,724,128,36)))
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
    
        nc_p = [228,368]
        dirty_rects.append(screen.blit(number_card, nc_p))
        if (s.game.anti_cheat.status == True):
            dirty_rects.append(screen.blit(bg_gi, (224,264), pygame.Rect(224,264,270,408)))
        else:
            dirty_rects.append(screen.blit(bg_off, (224,264), pygame.Rect(224,264,270,408)))

            
        dirty_rects.append(screen.blit(bg_gi, (376,196), pygame.Rect(376,196,330,106)))
        
        p = [381,207]
        dirty_rects.append(screen.blit(letter1, p))
        p = [425,197]
        dirty_rects.append(screen.blit(letter2, p))
        p = [489,206]
        dirty_rects.append(screen.blit(letter3, p))
        p = [520,209]
        dirty_rects.append(screen.blit(letter4, p))
        p = [568,211]
        dirty_rects.append(screen.blit(letter5, p))
        p = [637,203]
        dirty_rects.append(screen.blit(letter6, p))

        if s.game.red_odds.position < 5:
            p = [381,207]
            dirty_rects.append(screen.blit(red_letter1, p))
        if s.game.red_odds.position in [5,6]:
            p = [425,197]
            dirty_rects.append(screen.blit(red_letter2, p))
        if s.game.red_odds.position == 7:
            p = [489,206]
            dirty_rects.append(screen.blit(red_letter3, p))
        if s.game.red_odds.position == 8:
            p = [520,209]
            dirty_rects.append(screen.blit(red_letter4, p))
        if s.game.red_odds.position == 9:
            p = [568,211]
            dirty_rects.append(screen.blit(red_letter5, p))
        if s.game.red_odds.position == 10:
            p = [637,203]
            dirty_rects.append(screen.blit(red_letter6, p))

        if s.game.mystic_lines.position == 1:
            p = [204,687]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],25,29)))
            dirty_rects.append(screen.blit(ml_arrow, p))
        if s.game.mystic_lines.position == 2:
            p = [236,687]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],25,29)))
            dirty_rects.append(screen.blit(ml_arrow, p))
        if s.game.mystic_lines.position == 3:
            p = [269,687]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],25,29)))
            dirty_rects.append(screen.blit(ml_arrow, p))
        if s.game.mystic_lines.position >= 4:
            p = [295,681]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],38,46)))
            dirty_rects.append(screen.blit(ml_a, p))
            p = [341,595]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],44,50)))
            dirty_rects.append(screen.blit(ml_letter, p))
        if s.game.mystic_lines.position == 5:
            p = [334,687]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],25,29)))
            dirty_rects.append(screen.blit(ml_arrow, p))
        if s.game.mystic_lines.position == 6:
            p = [366,687]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],25,29)))
            dirty_rects.append(screen.blit(ml_arrow, p))
        if s.game.mystic_lines.position >= 7:
            p = [392,681]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],38,46)))
            dirty_rects.append(screen.blit(ml_a, p))
            p = [265,595]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],44,50)))
            dirty_rects.append(screen.blit(ml_letter, p))
        if s.game.mystic_lines.position == 8:
            p = [433,687]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],25,29)))
            dirty_rects.append(screen.blit(ml_arrow, p))
        if s.game.mystic_lines.position == 9:
            p = [463,687]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],25,29)))
            dirty_rects.append(screen.blit(ml_arrow, p))
        if s.game.mystic_lines.position == 10:
            p = [489,681]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],38,46)))
            dirty_rects.append(screen.blit(ml_a, p))
            p = [416,595]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],44,50)))
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
     
        nc_p = [228,368]
        dirty_rects.append(screen.blit(number_card, nc_p))
        if (s.game.anti_cheat.status == True):
            dirty_rects.append(screen.blit(bg_gi, (233,369), pygame.Rect(233,369,270,212)))
        else:
            dirty_rects.append(screen.blit(bg_off, (233,369), pygame.Rect(233,369,270,212)))

        if s.game.mystic_lines.position == 1:
            p = [204,687]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],25,29)))
            dirty_rects.append(screen.blit(ml_arrow, p))
        if s.game.mystic_lines.position == 2:
            p = [236,687]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],25,29)))
            dirty_rects.append(screen.blit(ml_arrow, p))
        if s.game.mystic_lines.position == 3:
            p = [269,687]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],25,29)))
            dirty_rects.append(screen.blit(ml_arrow, p))
        if s.game.mystic_lines.position >= 4:
            p = [295,681]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],38,46)))
            dirty_rects.append(screen.blit(ml_a, p))
            p = [341,595]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],44,50)))
            dirty_rects.append(screen.blit(ml_letter, p))
        if s.game.mystic_lines.position == 5:
            p = [334,687]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],25,29)))
            dirty_rects.append(screen.blit(ml_arrow, p))
        if s.game.mystic_lines.position == 6:
            p = [366,687]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],25,29)))
            dirty_rects.append(screen.blit(ml_arrow, p))
        if s.game.mystic_lines.position >= 7:
            p = [392,681]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],38,46)))
            dirty_rects.append(screen.blit(ml_a, p))
            p = [265,595]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],44,50)))
            dirty_rects.append(screen.blit(ml_letter, p))
        if s.game.mystic_lines.position == 8:
            p = [433,687]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],25,29)))
            dirty_rects.append(screen.blit(ml_arrow, p))
        if s.game.mystic_lines.position == 9:
            p = [463,687]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],25,29)))
            dirty_rects.append(screen.blit(ml_arrow, p))
        if s.game.mystic_lines.position == 10:
            p = [489,681]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],38,46)))
            dirty_rects.append(screen.blit(ml_a, p))
            p = [416,595]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],44,50)))
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

        nc_p = [228,368]
        dirty_rects.append(screen.blit(number_card, nc_p))
        if (s.game.anti_cheat.status == True):
            dirty_rects.append(screen.blit(bg_gi, (389,369), pygame.Rect(389,369,100,212)))
        else:
            dirty_rects.append(screen.blit(bg_off, (389,369), pygame.Rect(389,369,100,212)))

        if s.game.mystic_lines.position == 1:
            p = [204,687]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],25,29)))
            dirty_rects.append(screen.blit(ml_arrow, p))
        if s.game.mystic_lines.position == 2:
            p = [236,687]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],25,29)))
            dirty_rects.append(screen.blit(ml_arrow, p))
        if s.game.mystic_lines.position == 3:
            p = [269,687]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],25,29)))
            dirty_rects.append(screen.blit(ml_arrow, p))
        if s.game.mystic_lines.position >= 4:
            p = [295,681]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],38,46)))
            dirty_rects.append(screen.blit(ml_a, p))
            p = [341,595]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],44,50)))
            dirty_rects.append(screen.blit(ml_letter, p))
        if s.game.mystic_lines.position == 5:
            p = [334,687]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],25,29)))
            dirty_rects.append(screen.blit(ml_arrow, p))
        if s.game.mystic_lines.position == 6:
            p = [366,687]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],25,29)))
            dirty_rects.append(screen.blit(ml_arrow, p))
        if s.game.mystic_lines.position >= 7:
            p = [392,681]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],38,46)))
            dirty_rects.append(screen.blit(ml_a, p))
            p = [265,595]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],44,50)))
            dirty_rects.append(screen.blit(ml_letter, p))
        if s.game.mystic_lines.position == 8:
            p = [433,687]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],25,29)))
            dirty_rects.append(screen.blit(ml_arrow, p))
        if s.game.mystic_lines.position == 9:
            p = [463,687]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],25,29)))
            dirty_rects.append(screen.blit(ml_arrow, p))
        if s.game.mystic_lines.position == 10:
            p = [489,681]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],38,46)))
            dirty_rects.append(screen.blit(ml_a, p))
            p = [416,595]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],44,50)))
            dirty_rects.append(screen.blit(ml_letter, p))

    pygame.display.update(dirty_rects)

def eb_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]

    if s.game.extra_ball.position < 1:
        dirty_rects.append(screen.blit(bg_gi, (147,1043), pygame.Rect(147,1043,47,31)))
    if s.game.extra_ball.position < 2:
        dirty_rects.append(screen.blit(bg_gi, (197,1043), pygame.Rect(197,1043,59,34)))
    if s.game.extra_ball.position < 3:
        dirty_rects.append(screen.blit(bg_gi, (261,1043), pygame.Rect(261,1043,59,34)))
    if s.game.extra_ball.position < 4:
        dirty_rects.append(screen.blit(bg_gi, (322,1043), pygame.Rect(322,1043,47,31)))
    if s.game.extra_ball.position < 5:
        dirty_rects.append(screen.blit(bg_gi, (373,1044), pygame.Rect(373,1044,59,34)))
    if s.game.extra_ball.position < 6:
        dirty_rects.append(screen.blit(bg_gi, (434,1043), pygame.Rect(434,1043,59,34)))
    if s.game.extra_ball.position < 7:
        dirty_rects.append(screen.blit(bg_gi, (498,1044), pygame.Rect(498,1044,47,31)))
    if s.game.extra_ball.position < 8:
        dirty_rects.append(screen.blit(bg_gi, (548,1045), pygame.Rect(548,1045,59,34)))
    if s.game.extra_ball.position < 9:
        dirty_rects.append(screen.blit(bg_gi, (612,1044), pygame.Rect(612,1044,59,34)))
    pygame.display.update(dirty_rects)

    if num in [0,25,14,49]:
        if s.game.extra_ball.position < 1:
            p = [147,1043]
            dirty_rects.append(screen.blit(eb_number, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [39,1,26,15]:
        if s.game.extra_ball.position < 2:
            p = [197,1043]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [3,4,17,28,29,40]:
        if s.game.extra_ball.position < 3:
            p = [261,1043]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [5,18,30,43]:
        if s.game.extra_ball.position < 4:
            p = [322,1043]
            dirty_rects.append(screen.blit(eb_number, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [7,8,19,32,33,44]:
        if s.game.extra_ball.position < 5:
            p = [373,1044]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [9,10,20,34,35,45]:
        if s.game.extra_ball.position < 6:
            p = [434,1043]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [11,21,36,46]:
        if s.game.extra_ball.position < 7:
            p = [498,1044]
            dirty_rects.append(screen.blit(eb_number, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [12,22,37,47]:
        if s.game.extra_ball.position < 8:
            p = [548,1045]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [2,6,13,16,23,27,31,38,41,48]:
        if s.game.extra_ball.position < 9:
            p = [612,1044]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return

def clear_odds(s, num):
    global screen

    dirty_rects = []
    
    if s.game.double_red.status == False:
        dirty_rects.append(screen.blit(bg_gi, (20,613), pygame.Rect(20,613,75,72)))
    if s.game.double_yellow.status == False:
        dirty_rects.append(screen.blit(bg_gi, (94,611), pygame.Rect(94,611,75,73)))
    if s.game.double_green.status == False:
        dirty_rects.append(screen.blit(bg_gi, (21,685), pygame.Rect(21,685,75,73)))
    if s.game.double_blue.status == False:
        dirty_rects.append(screen.blit(bg_gi, (95,685), pygame.Rect(95,685,75,73)))

    if s.game.yellow_odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (223,905), pygame.Rect(223,905,46,61)))
    if s.game.yellow_odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (375,905), pygame.Rect(375,905,46,61)))
    if s.game.yellow_odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (473,905), pygame.Rect(473,905,46,61)))
    if s.game.yellow_odds.position != 9:
        dirty_rects.append(screen.blit(bg_gi, (576,905), pygame.Rect(576,905,46,61)))
    if s.game.yellow_odds.position != 10:
        dirty_rects.append(screen.blit(bg_gi, (625,905), pygame.Rect(625,905,46,61)))

    if s.game.red_odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (275,773), pygame.Rect(275,773,46,61)))
    if s.game.red_odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (473,773), pygame.Rect(473,773,46,61)))
    if s.game.red_odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (525,773), pygame.Rect(525,773,46,61)))
    if s.game.red_odds.position != 9:
        dirty_rects.append(screen.blit(bg_gi, (576,773), pygame.Rect(576,773,46,61)))
    if s.game.red_odds.position != 10:
        dirty_rects.append(screen.blit(bg_gi, (625,773), pygame.Rect(625,773,46,61)))

    if s.game.blue_odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (223,970), pygame.Rect(223,970,46,61)))
    if s.game.blue_odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (375,970), pygame.Rect(375,970,46,61)))
    if s.game.blue_odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (525,970), pygame.Rect(525,970,46,61)))
    if s.game.blue_odds.position != 9:
        dirty_rects.append(screen.blit(bg_gi, (574,970), pygame.Rect(574,970,46,61)))
    if s.game.blue_odds.position != 10:
        dirty_rects.append(screen.blit(bg_gi, (622,970), pygame.Rect(622,970,46,61)))

    if s.game.green_odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (275,842), pygame.Rect(275,842,46,61)))
    if s.game.green_odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (375,842), pygame.Rect(375,842,46,61)))
    if s.game.green_odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (473,842), pygame.Rect(473,842,46,61)))
    if s.game.green_odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (525,842), pygame.Rect(525,842,46,61)))
    if s.game.green_odds.position != 10:
        dirty_rects.append(screen.blit(bg_gi, (625,840), pygame.Rect(625,840,46,61)))

    pygame.display.update(dirty_rects)

def draw_odds_animation(s, num):
    global screen
    dirty_rects = []

    if num in [7,32]:
        if s.game.double_red.status == False:
            p = [20,613]
            dirty_rects.append(screen.blit(red_double, p))
            pygame.display.update(dirty_rects)
            return
    if num in [11,36]:
        if s.game.double_yellow.status == False:
            p = [94,611]
            dirty_rects.append(screen.blit(yellow_double, p))
            pygame.display.update(dirty_rects)
            return
    if num in [0,25]:
        if s.game.double_green.status == False:
            p = [21,685]
            dirty_rects.append(screen.blit(green_double, p))
            pygame.display.update(dirty_rects)
            return
    if num in [17,42]:
        if s.game.double_blue.status == False:
            p = [95,685]
            dirty_rects.append(screen.blit(blue_double, p))
            pygame.display.update(dirty_rects)
            return

    if num in [4,29]:
        if s.game.yellow_odds.position != 2:
            p = [223,905]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [13,38]:
        if s.game.yellow_odds.position != 5:
            p = [375,905]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [22,47]:
        if s.game.yellow_odds.position != 7:
            p = [473,905]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [19,44]:
        if s.game.yellow_odds.position != 9:
            p = [576,905]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [5,30]:
        if s.game.yellow_odds.position != 10:
            p = [625,905]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    
    if num in [23,48]:
        if s.game.red_odds.position != 3:
            p = [275,773]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [20,45]:
        if s.game.red_odds.position != 7:
            p = [473,773]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [12,37]:
        if s.game.red_odds.position != 8:
            p = [525,773]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [25,0]:
        if s.game.red_odds.position != 9:
            p = [576,773]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [6,31]:
        if s.game.red_odds.position != 10:
            p = [625,773]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return

    if num in [18,43]:
        if s.game.blue_odds.position != 2:
            p = [223,970]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [3,28]:
        if s.game.blue_odds.position != 5:
            p = [375,970]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [8,33]:
        if s.game.blue_odds.position != 8:
            p = [525,970]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [21,46]:
        if s.game.blue_odds.position != 9:
            p = [574,970]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [10,35]:
        if s.game.blue_odds.position != 10:
            p = [622,970]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return

    if num in [15,40]:
        if s.game.green_odds.position != 3:
            p = [275,842]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [9,34]:
        if s.game.green_odds.position != 5:
            p = [375,842]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [16,41]:
        if s.game.green_odds.position != 7:
            p = [473,842]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [14,39]:
        if s.game.green_odds.position != 8:
            p = [525,842]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [23,48]:
        if s.game.green_odds.position != 10:
            p = [625,840]
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
    
    if s.game.mystic_lines.position < 4 and s.game.two_red_letter.status == False and s.game.three_red_letter.status == False and s.game.selection_feature.position < 7:
        dirty_rects.append(screen.blit(bg_gi, (19,552), pygame.Rect(19,552,149,48)))
    if s.game.mystic_lines.position < 4 and s.game.two_red_letter.status == False and s.game.three_red_letter.status == False and s.game.selection_feature.position not in [7,8]:
        dirty_rects.append(screen.blit(bg_gi, (19,417), pygame.Rect(19,417,149,48)))
    
    if s.game.selection_feature.position < 9:
        dirty_rects.append(screen.blit(bg_gi, (17,372), pygame.Rect(17,372,150,45)))
    if s.game.mystic_lines.position < 4 and s.game.two_red_letter.status == False and s.game.three_red_letter.status == False:
        dirty_rects.append(screen.blit(bg_gi, (17,372), pygame.Rect(17,372,150,45)))

    if s.game.yellow_star.status == False:
        dirty_rects.append(screen.blit(bg_gi, (19,507), pygame.Rect(19,507,151,48)))
    if s.game.red_star.status == False:
        dirty_rects.append(screen.blit(bg_gi, (19,463), pygame.Rect(19,463,151,48)))

    if s.game.three_red_letter.status == False:
        dirty_rects.append(screen.blit(bg_gi, (17,216), pygame.Rect(17,216,76,41)))
    if s.game.two_red_letter.status == False:
        dirty_rects.append(screen.blit(bg_gi, (91,217), pygame.Rect(91,217,76,41)))
    if s.game.three_stars.status == False:
        dirty_rects.append(screen.blit(bg_gi, (17,333), pygame.Rect(17,333,74,26)))
    if s.game.six_stars.status == False:
        dirty_rects.append(screen.blit(bg_gi, (91,334), pygame.Rect(91,334,74,26)))


    if s.game.mystic_lines.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (236,687), pygame.Rect(236,687,18,22)))
    if s.game.mystic_lines.position < 4:
        dirty_rects.append(screen.blit(bg_gi, (295,681), pygame.Rect(295,681,31,36)))
        dirty_rects.append(screen.blit(bg_gi, (341,595), pygame.Rect(341,595,37,42)))
    if s.game.mystic_lines.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (334,687), pygame.Rect(334,687,18,22)))
    if s.game.mystic_lines.position < 7:
        dirty_rects.append(screen.blit(bg_gi, (392,681), pygame.Rect(392,681,31,36)))
        dirty_rects.append(screen.blit(bg_gi, (265,595), pygame.Rect(265,595,37,42)))
    if s.game.mystic_lines.position != 9:
        dirty_rects.append(screen.blit(bg_gi, (463,687), pygame.Rect(463,687,18,22)))
    if s.game.mystic_lines.position < 10:
        dirty_rects.append(screen.blit(bg_gi, (489,681), pygame.Rect(489,681,31,36)))
        dirty_rects.append(screen.blit(bg_gi, (416,595), pygame.Rect(416,595,37,42)))

    pygame.display.update(dirty_rects)


def draw_feature_animation(s, num):
    global screen
    dirty_rects = []
    
    if num in [10,35]:
        if s.game.mystic_lines.position < 4 and s.game.two_red_letter.status == False and s.game.three_red_letter.status == False and s.game.selection_feature.position < 7:
            p = [19,552]
            dirty_rects.append(screen.blit(bottom, p))
            pygame.display.update(dirty_rects)
            return
    if num in [9,34]:
        if s.game.mystic_lines.position < 4 and s.game.two_red_letter.status == False and s.game.three_red_letter.status == False and s.game.selection_feature.position not in [7,8]:
            p = [19,417]
            dirty_rects.append(screen.blit(button, p))
            pygame.display.update(dirty_rects)
            return
    if num in [6,31,17,42,21,46]:
        if s.game.selection_feature.position not in [9] or (s.game.mystic_lines.position < 4 and s.game.two_red_letter.status == False and s.game.three_red_letter.status == False):
            p = [17,372]
            dirty_rects.append(screen.blit(top, p))
            pygame.display.update(dirty_rects)
            return
    if num in [4,29]:
        if s.game.red_star.status == False:
            p = [19,463]
            dirty_rects.append(screen.blit(button, p))
            pygame.display.update(dirty_rects)
            s.game.coils.redROLamp.pulse(85)
            return
    if num in [11,36]:
        if s.game.yellow_star.status == False:
            p = [19,507]
            dirty_rects.append(screen.blit(button, p))
            pygame.display.update(dirty_rects)
            s.game.coils.yellowROLamp.pulse(85)
            return
    if num in [16,41]:
        if s.game.three_red_letter.status == False:
            p = [17,216]
            dirty_rects.append(screen.blit(three_red, p))
            pygame.display.update(dirty_rects)
            return
    if num in [7,32]:
        if s.game.two_red_letter.status == False:
            p = [91,217]
            dirty_rects.append(screen.blit(two_red, p))
            pygame.display.update(dirty_rects)
            return

    if num in [8,33]:
        if s.game.three_stars.status == False:
            p = [17,333]
            dirty_rects.append(screen.blit(three_stars, p))
            pygame.display.update(dirty_rects)
            return
    if num in [20,45]:
        if s.game.six_stars.status == False:
            p = [91,334]
            dirty_rects.append(screen.blit(six_stars, p))
            pygame.display.update(dirty_rects)
            return

    if num in [13,19,38,44]:
        if s.game.mystic_lines.position != 2:
            p = [236,687]
            dirty_rects.append(screen.blit(ml_arrow, p))
            pygame.display.update(dirty_rects)
            return
    if num in [3,22,28,47]:
        if s.game.mystic_lines.position < 4:
            p = [295,681]
            dirty_rects.append(screen.blit(ml_a, p))
            p = [341,595]
            dirty_rects.append(screen.blit(ml_letter, p))
            pygame.display.update(dirty_rects)
            return
    if num in [18,25,43,0]:
        if s.game.mystic_lines.position != 5:
            p = [334,687]
            dirty_rects.append(screen.blit(ml_arrow, p))
            pygame.display.update(dirty_rects)
            return
    if num in [2,12,27,37]:
        if s.game.mystic_lines.position < 7:
            p = [265,595]
            dirty_rects.append(screen.blit(ml_letter, p))
            p = [392,681]
            dirty_rects.append(screen.blit(ml_a, p))
            pygame.display.update(dirty_rects)
            return
    if num in [15,40]:
        if s.game.mystic_lines.position != 9:
            p = [463,687]
            dirty_rects.append(screen.blit(ml_arrow, p))
            pygame.display.update(dirty_rects)
            return
    if num in [1,14,26,39]:
        if s.game.mystic_lines.position < 10:
            p = [416,595]
            dirty_rects.append(screen.blit(ml_letter, p))
            p = [489,681]
            dirty_rects.append(screen.blit(ml_a, p))
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

    if s.game.special_odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (599,577), pygame.Rect(599,577,103,34)))
    if s.game.special_odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (599,544), pygame.Rect(599,544,103,34)))
    if s.game.special_odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (599,511), pygame.Rect(599,511,103,34)))
    if s.game.special_odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (599,478), pygame.Rect(599,478,103,34)))
    if s.game.special_odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (599,443), pygame.Rect(599,443,103,34)))
    if s.game.special_odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (599,411), pygame.Rect(599,411,103,34)))
    if s.game.special_odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (599,377), pygame.Rect(599,377,103,34)))
    if s.game.special_odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (600,344), pygame.Rect(600,344,103,34)))

    pygame.display.update(dirty_rects)

    if num in [3,28]:
        if s.game.special_odds.position != 1:
            p = [599,577]
            dirty_rects.append(screen.blit(special_odds, p))
            pygame.display.update(dirty_rects) 
            return
    if num in [6,7,31,32]:
        if s.game.special_odds.position < 2:
            p = [599,544]
            dirty_rects.append(screen.blit(special_odds, p))
            pygame.display.update(dirty_rects) 
            return
    if num in [3,4,28,29]:
        if s.game.special_odds.position < 3:
            p = [599,511]
            dirty_rects.append(screen.blit(special_odds, p))
            pygame.display.update(dirty_rects) 
            return
    if num in [10,11,35,36]:
        if s.game.special_odds.position < 4:
            p = [599,478]
            dirty_rects.append(screen.blit(special_odds, p))
            pygame.display.update(dirty_rects) 
            return
    if num in [8,9,33,34]:
        if s.game.special_odds.position < 5:
            p = [599,443]
            dirty_rects.append(screen.blit(special_odds, p))
            pygame.display.update(dirty_rects) 
            return
    if num in [14,15,39,40]:
        if s.game.special_odds.position < 6:
            p = [599,411]
            dirty_rects.append(screen.blit(special_odds, p))
            pygame.display.update(dirty_rects) 
            return
    if num in [12,13,21,22,37,38,46,47]:
        if s.game.special_odds.position < 7:
            p = [599,377]
            dirty_rects.append(screen.blit(special_odds, p))
            pygame.display.update(dirty_rects) 
            return
    if num in [16,17,23,24,25,41,42,48,49]:
        if s.game.special_odds.position < 8:
            p = [600,344]
            dirty_rects.append(screen.blit(special_odds, p))
            pygame.display.update(dirty_rects) 
            return

