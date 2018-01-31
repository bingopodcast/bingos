
import pygame
import random

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

meter = pygame.image.load('graphics/assets/black_register_cover.png').convert()
odds = pygame.image.load('venice/assets/odds.png').convert_alpha()
eb = pygame.image.load('venice/assets/eb.png').convert_alpha()
eb_number = pygame.image.load('venice/assets/eb_number.png').convert_alpha()
extra_balls = pygame.image.load('venice/assets/extra_balls.png').convert_alpha()
time = pygame.image.load('venice/assets/time.png').convert_alpha()
ml_letter = pygame.image.load('venice/assets/ml_letter.png').convert_alpha()
ml_arrow = pygame.image.load('venice/assets/ml_arrow.png').convert_alpha()
ml_a = pygame.image.load('venice/assets/ml_a.png').convert_alpha()
select_now = pygame.image.load('venice/assets/select_now.png').convert_alpha()
tilt = pygame.image.load('venice/assets/tilt.png').convert_alpha()
button = pygame.image.load('venice/assets/pap.png').convert_alpha()
red_double = pygame.image.load('venice/assets/red_double.png').convert_alpha()
green_double = pygame.image.load('venice/assets/green_double.png').convert_alpha()
yellow_double = pygame.image.load('venice/assets/yellow_double.png').convert_alpha()
blue_double = pygame.image.load('venice/assets/blue_double.png').convert_alpha()
four_stars = pygame.image.load('venice/assets/four_stars.png').convert_alpha()
six_stars = pygame.image.load('venice/assets/six_stars.png').convert_alpha()
three_stars = pygame.image.load('venice/assets/three_stars.png').convert_alpha()
three_red = pygame.image.load('venice/assets/three_red.png').convert_alpha()
two_red = pygame.image.load('venice/assets/two_red.png').convert_alpha()
red_letter = pygame.image.load('venice/assets/red_letter.png').convert_alpha()
letter1 = pygame.image.load('venice/assets/letter1.png').convert_alpha()
letter2 = pygame.image.load('venice/assets/letter2.png').convert_alpha()
letter3 = pygame.image.load('venice/assets/letter3.png').convert_alpha()
letter4 = pygame.image.load('venice/assets/letter4.png').convert_alpha()
letter5 = pygame.image.load('venice/assets/letter5.png').convert_alpha()
letter6 = pygame.image.load('venice/assets/letter6.png').convert_alpha()
red_letter1 = pygame.image.load('venice/assets/red_letter1.png').convert_alpha()
red_letter2 = pygame.image.load('venice/assets/red_letter2.png').convert_alpha()
red_letter3 = pygame.image.load('venice/assets/red_letter3.png').convert_alpha()
red_letter4 = pygame.image.load('venice/assets/red_letter4.png').convert_alpha()
red_letter5 = pygame.image.load('venice/assets/red_letter5.png').convert_alpha()
red_letter6 = pygame.image.load('venice/assets/red_letter6.png').convert_alpha()
number_card = pygame.image.load('venice/assets/number_card.png').convert_alpha()
number = pygame.image.load('venice/assets/number.png').convert_alpha()
columnb1 = pygame.image.load('venice/assets/columnb1.png').convert_alpha()
columnb2 = pygame.image.load('venice/assets/columnb2.png').convert_alpha()
columna = pygame.image.load('venice/assets/columna.png').convert_alpha()
columnc1 = pygame.image.load('venice/assets/columnc1.png').convert_alpha()
columnc2 = pygame.image.load('venice/assets/columnc2.png').convert_alpha()
double_triple = pygame.image.load('venice/assets/double_triple.png').convert_alpha()
ball = pygame.image.load('venice/assets/ball.png').convert_alpha()
eo = pygame.image.load('venice/assets/eo.png').convert_alpha()
dn = pygame.image.load('venice/assets/dn.png').convert_alpha()
collected = pygame.image.load('venice/assets/collected.png').convert_alpha()
missed = pygame.image.load('venice/assets/missed.png').convert_alpha()
special_odds = pygame.image.load('venice/assets/special_odds.png').convert_alpha()
golden = pygame.image.load('venice/assets/golden.png').convert_alpha()
bg_menu = pygame.image.load('venice/assets/venice_menu.png').convert_alpha()
bg_gi = pygame.image.load('venice/assets/venice_gi.png').convert_alpha()
bg_off = pygame.image.load('venice/assets/venice_off.png').convert_alpha()

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
        eb_position = [147,1041]
        screen.blit(eb_number, eb_position)
    if s.game.extra_ball.position >= 2:
        eb_position = [197,1041]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 3:
        eb_position = [261,1041]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 4:
        eb_position = [322,1041]
        screen.blit(eb_number, eb_position)
    if s.game.extra_ball.position >= 5:
        eb_position = [373,1041]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 6:
        eb_position = [434,1041]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 7:
        eb_position = [498,1041]
        screen.blit(eb_number, eb_position)
    if s.game.extra_ball.position >= 8:
        eb_position = [548,1041]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 9:
        eb_position = [612,1041]
        screen.blit(eb, eb_position)

    if s.game.red_star.status == True:
        rs_position = [546,460]
        screen.blit(time, rs_position)
    if s.game.yellow_star.status == True:
        rs_position = [546,504]
        screen.blit(time, rs_position)

    if s.game.mystic_lines.position >= 4 or s.game.two_red_letter.status == True or s.game.three_red_letter.status == True:
        if s.game.selection_feature.position < 7:
            bfp = [546,549]
            screen.blit(time, bfp)
        elif s.game.selection_feature.position in [7,8]:
            bfp = [546,417]
            screen.blit(time, bfp)
        elif s.game.selection_feature.position == 9:
            bfp = [546,372]
            screen.blit(time, bfp)

    if s.game.ball_count.position < 1:
        if s.game.odds_only.status == True:
            b = [20,875]
            screen.blit(button, b)
        elif s.game.features.status == True:
            b = [20,916]
            screen.blit(button, b)
        elif s.game.special.status == True:
            b = [20,997]
            screen.blit(button, b)
        else:
            b = [20,956]
            screen.blit(button, b)


    if s.game.mystic_lines.position == 1:
        p = [199,684]
        screen.blit(ml_arrow, p)
    if s.game.mystic_lines.position == 2:
        p = [234,684]
        screen.blit(ml_arrow, p)
    if s.game.mystic_lines.position == 3:
        p = [267,684]
        screen.blit(ml_arrow, p)
    if s.game.mystic_lines.position >= 4:
        p = [287,674]
        screen.blit(ml_a, p)
        p = [332,592]
        screen.blit(ml_letter, p)
    if s.game.mystic_lines.position == 5:
        p = [331,684]
        screen.blit(ml_arrow, p)
    if s.game.mystic_lines.position == 6:
        p = [363,684]
        screen.blit(ml_arrow, p)
    if s.game.mystic_lines.position >= 7:
        p = [255,590]
        screen.blit(ml_letter, p)
        p = [384,673]
        screen.blit(ml_a, p)
    if s.game.mystic_lines.position == 8:
        p = [429,684]
        screen.blit(ml_arrow, p)
    if s.game.mystic_lines.position == 9:
        p = [459,684]
        screen.blit(ml_arrow, p)
    if s.game.mystic_lines.position == 10:
        p = [480,673]
        screen.blit(ml_a, p)
        p = [406,590]
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

    p = [25,215]
    screen.blit(letter1, p)
    p = [65,215]
    screen.blit(letter2, p)
    p = [115,215]
    screen.blit(letter3, p)
    p = [171,215]
    screen.blit(letter4, p)
    p = [205,215]
    screen.blit(letter5, p)
    p = [262,215]
    screen.blit(letter6, p)

    if s.game.red_odds.position < 5:
        p = [25,215]
        screen.blit(red_letter1, p)
    if s.game.red_odds.position in [5,6]:
        p = [65,215]
        screen.blit(red_letter2, p)
    if s.game.red_odds.position == 7:
        p = [115,215]
        screen.blit(red_letter3, p)
    if s.game.red_odds.position == 8:
        p = [171,215]
        screen.blit(red_letter4, p)
    if s.game.red_odds.position == 9:
        p = [205,215]
        screen.blit(red_letter5, p)
    if s.game.red_odds.position == 10:
        p = [262,215]
        screen.blit(red_letter6, p)

    if s.game.two_red_letter.status == True:
        p = [546,256]
        screen.blit(red_letter, p)
        p = [619,217]
        screen.blit(two_red, p)
    if s.game.three_red_letter.status == True:
        p = [546,256]
        screen.blit(red_letter, p)
        p = [547,218]
        screen.blit(three_red, p)

    if s.game.three_stars.status == True:
        p = [547,294]
        screen.blit(four_stars, p)
        p = [547,333]
        screen.blit(three_stars, p)
    if s.game.six_stars.status == True:
        p = [547,294]
        screen.blit(four_stars, p)
        p = [618,333]
        screen.blit(six_stars, p)

    if s.game.double_red.status == True:
        p = [547,608]
        screen.blit(red_double, p)
    if s.game.double_yellow.status == True:
        p = [622,609]
        screen.blit(yellow_double, p)
    if s.game.double_green.status == True:
        p = [547,684]
        screen.blit(green_double, p)
    if s.game.double_blue.status == True:
        p = [623,684]
        screen.blit(blue_double, p)

    if s.game.triple.status == False and (s.game.double_red.status == True or s.game.double_yellow.status == True or s.game.double_green.status == True or s.game.double_blue.status == True):
        p = [584,650]
        screen.blit(double_triple, p)

    if s.game.triple.status == True and (s.game.double_red.status == True or s.game.double_yellow.status == True or s.game.double_green.status == True or s.game.double_blue.status == True):
        p = [584,684]
        screen.blit(double_triple, p)

    if s.game.tilt.status == True:
        tilt_position = [427,317]
        screen.blit(tilt, tilt_position)

    # Special Game
    if s.game.missed.status == False:
        if s.game.special_odds.position > 0:
            if s.game.special_game.position == 0:
                p = [10,707]
                screen.blit(eo, p)
            if s.game.special_game.position == 1:
                p = [11,623]
                screen.blit(ball, p)
                p = [97,707]
                screen.blit(eo, p)
            if s.game.special_game.position == 2:
                p = [47,622]
                screen.blit(ball, p)
                p = [10,707]
                screen.blit(eo, p)
            if s.game.special_game.position == 3:
                p = [80,623]
                screen.blit(ball, p)
                p = [97,707]
                screen.blit(eo, p)
            if s.game.special_game.position == 4:
                p = [115,623]
                screen.blit(ball, p)
                p = [10,707]
                screen.blit(eo, p)
            if s.game.special_game.position == 5:
                p = [150,623]
                screen.blit(ball, p)
                p = [17,405]
                screen.blit(golden, p)
            if s.game.special_game.position in [3,4]:
                p = [16,459]
                screen.blit(dn, p)
            if s.game.special_replay_counter.position > 0:
                p = [18,358]
                screen.blit(collected, p)
    if s.game.missed.status == True:
        p = [17,568]
        screen.blit(missed, p)

    if s.game.special_odds.position == 1:
        p = [81,592]
        screen.blit(special_odds, p)
    elif s.game.special_odds.position == 2:
        p = [81,560]
        screen.blit(special_odds, p)
    elif s.game.special_odds.position == 3:
        p = [81,529]
        screen.blit(special_odds, p)
    elif s.game.special_odds.position == 4:
        p = [81,498]
        screen.blit(special_odds, p)
    elif s.game.special_odds.position == 5:
        p = [81,466]
        screen.blit(special_odds, p)
    elif s.game.special_odds.position == 6:
        p = [81,437]
        screen.blit(special_odds, p)
    elif s.game.special_odds.position == 7:
        p = [81,405]
        screen.blit(special_odds, p)
    elif s.game.special_odds.position == 8:
        p = [81,374]
        screen.blit(special_odds, p)
    elif s.game.special_odds.position == 9:
        p = [81,344]
        screen.blit(special_odds, p)

    pygame.display.update()

def blink(args):
    dirty_rects = []
    s = args[0]
    b = args[1]
    sn = args[2]

    if b == 0:
        if sn == 1:
            p = [384,719]
            dirty_rects.append(screen.blit(select_now, p))
        pygame.display.update(dirty_rects)
    else:
        dirty_rects.append(screen.blit(bg_gi, (384,719), pygame.Rect(384,719,132,41)))
        pygame.display.update(dirty_rects)
    b = not b

    args = [s,b,sn]

    s.delay(name="blink", delay=0.1, handler=blink, param=args)

def eb_animation(num):
    global screen

    if num == 3:
        eb_position = [498,1041]
        screen.blit(eb_number, eb_position)
        pygame.display.update()
    if num == 2:
        eb_position = [548,1041]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 1:
        eb_position = [612,1041]
        screen.blit(eb, eb_position)
        pygame.display.update()

def feature_animation(num):
    global screen

    if num == 4:
        p = [459,684]
        screen.blit(ml_arrow, p)
        pygame.display.update()
    else:
        p = [480,673]
        screen.blit(ml_a, p)
        p = [406,590]
        screen.blit(ml_letter, p)
        pygame.display.update()


def odds_animation(num):
    global screen

    if num == 8:
        o = [180,905]
        screen.blit(odds, o)
    if num == 7:
        o = [228,905]
        screen.blit(odds, o)
    if num == 6:
        o = [280,905]
        screen.blit(odds, o)
    if num == 5:
        o = [329,905]
        screen.blit(odds, o)
    if num == 4:
        o = [380,905]
        screen.blit(odds, o)
    if num == 3:
        o = [429,905]
        screen.blit(odds, o)
    if num == 2:
        o = [478,905]
        screen.blit(odds, o)
    if num == 1:
        o = [530,905]
        screen.blit(odds, o)
    pygame.display.update()


