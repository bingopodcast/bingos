
import pygame
import random

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

meter = pygame.image.load('graphics/assets/black_register_cover.png').convert()
odds = pygame.image.load('double_up/assets/odds.png').convert_alpha()
eb = pygame.image.load('double_up/assets/eb.png').convert_alpha()
eb_number = pygame.image.load('double_up/assets/eb_number.png').convert_alpha()
extra_balls = pygame.image.load('double_up/assets/extra_balls.png').convert_alpha()
time = pygame.image.load('double_up/assets/time.png').convert_alpha()
ml_letter = pygame.image.load('double_up/assets/ml_letter.png').convert_alpha()
ml_arrow = pygame.image.load('double_up/assets/ml_arrow.png').convert_alpha()
select_now = pygame.image.load('double_up/assets/select_now.png').convert_alpha()
tilt = pygame.image.load('double_up/assets/tilt.png').convert_alpha()
button = pygame.image.load('double_up/assets/pap.png').convert_alpha()
double = pygame.image.load('double_up/assets/double.png').convert_alpha()
four_stars = pygame.image.load('double_up/assets/four_stars.png').convert_alpha()
six_stars = pygame.image.load('double_up/assets/six_stars.png').convert_alpha()
two_red = pygame.image.load('double_up/assets/two_red.png').convert_alpha()
red_letter = pygame.image.load('double_up/assets/red_letter.png').convert_alpha()
letter1 = pygame.image.load('double_up/assets/letter1.png').convert_alpha()
letter2 = pygame.image.load('double_up/assets/letter2.png').convert_alpha()
letter3 = pygame.image.load('double_up/assets/letter3.png').convert_alpha()
letter4 = pygame.image.load('double_up/assets/letter4.png').convert_alpha()
letter5 = pygame.image.load('double_up/assets/letter5.png').convert_alpha()
letter6 = pygame.image.load('double_up/assets/letter6.png').convert_alpha()
red_letter1 = pygame.image.load('double_up/assets/red_letter1.png').convert_alpha()
red_letter2 = pygame.image.load('double_up/assets/red_letter2.png').convert_alpha()
red_letter3 = pygame.image.load('double_up/assets/red_letter3.png').convert_alpha()
red_letter4 = pygame.image.load('double_up/assets/red_letter4.png').convert_alpha()
red_letter5 = pygame.image.load('double_up/assets/red_letter5.png').convert_alpha()
red_letter6 = pygame.image.load('double_up/assets/red_letter6.png').convert_alpha()
number_card = pygame.image.load('double_up/assets/number_card.png').convert_alpha()
number = pygame.image.load('double_up/assets/number.png').convert_alpha()
columnb1 = pygame.image.load('double_up/assets/columnb1.png').convert_alpha()
columnb2 = pygame.image.load('double_up/assets/columnb2.png').convert_alpha()
columna = pygame.image.load('double_up/assets/columna.png').convert_alpha()
columnc1 = pygame.image.load('double_up/assets/columnc1.png').convert_alpha()
columnc2 = pygame.image.load('double_up/assets/columnc2.png').convert_alpha()
no_scores_changed = pygame.image.load('double_up/assets/no_scores_changed.png').convert_alpha()
scores = pygame.image.load('double_up/assets/scores.png').convert_alpha()
score_arrow = pygame.image.load('double_up/assets/scores_arrow.png').convert_alpha()
bg_menu = pygame.image.load('double_up/assets/double_up_menu.png').convert_alpha()
bg_gi = pygame.image.load('double_up/assets/double_up_gi.png').convert_alpha()
bg_off = pygame.image.load('double_up/assets/double_up_off.png').convert_alpha()

class scorereel():
    """ Score Reels are used to count replays """
    def __init__(self, pos, image):
        self.position = pos
        self.default_y = self.position[1]
        self.image = pygame.image.load(image).convert()

reel1 = scorereel([109,807], "graphics/assets/white_reel.png")
reel10 = scorereel([90,807], "graphics/assets/white_reel.png")
reel100 = scorereel([71,807], "graphics/assets/white_reel.png")
reel1000 = scorereel([52,807], "graphics/assets/white_reel.png")

def display(s, replays=0, menu=False):
    
    meter.set_colorkey((255,0,252))
    meter_position = [43,807]

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
        eb_position = [46,1045]
        screen.blit(extra_balls, eb_position)

    if s.game.extra_ball.position >= 1:
        eb_position = [152,1045]
        screen.blit(eb_number, eb_position)
    if s.game.extra_ball.position >= 2:
        eb_position = [203,1045]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 3:
        eb_position = [266,1045]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 4:
        eb_position = [326,1045]
        screen.blit(eb_number, eb_position)
    if s.game.extra_ball.position >= 5:
        eb_position = [379,1045]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 6:
        eb_position = [441,1045]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 7:
        eb_position = [503,1045]
        screen.blit(eb_number, eb_position)
    if s.game.extra_ball.position >= 8:
        eb_position = [554,1045]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 9:
        eb_position = [616,1045]
        screen.blit(eb, eb_position)

    if s.game.red_star.status == True:
        rs_position = [559,426]
        screen.blit(time, rs_position)
    if s.game.yellow_star.status == True:
        rs_position = [559,471]
        screen.blit(time, rs_position)

    if s.game.mystic_lines.position >= 4 or s.game.two_red_letter.status == True or s.game.three_red_letter.status == True:
        if s.game.selection_feature.position < 7:
            bfp = [559,516]
            screen.blit(time, bfp)
        elif s.game.selection_feature.position in [7,8]:
            bfp = [559,382]
            screen.blit(time, bfp)
        elif s.game.selection_feature.position == 9:
            bfp = [559,338]
            screen.blit(time, bfp)

    if s.game.ball_count.position < 1:
        if s.game.odds_only.status == True:
            b = [15,914]
            screen.blit(button, b)
        elif s.game.features.status == True:
            b = [17,956]
            screen.blit(button, b)
        else:
            b = [18,995]
            screen.blit(button, b)


    if s.game.mystic_lines.position == 1:
        p = [104,606]
        screen.blit(ml_arrow, p)
    if s.game.mystic_lines.position == 2:
        p = [105,570]
        screen.blit(ml_arrow, p)
    if s.game.mystic_lines.position == 3:
        p = [105,534]
        screen.blit(ml_arrow, p)
    if s.game.mystic_lines.position >= 4:
        p = [94,483]
        screen.blit(ml_letter, p)
        p = [333,293]
        screen.blit(ml_letter, p)
    if s.game.mystic_lines.position == 5:
        p = [105,458]
        screen.blit(ml_arrow, p)
    if s.game.mystic_lines.position == 6:
        p = [105,422]
        screen.blit(ml_arrow, p)
    if s.game.mystic_lines.position >= 7:
        p = [96,374]
        screen.blit(ml_letter, p)
        p = [258,293]
        screen.blit(ml_letter, p)
    if s.game.mystic_lines.position == 8:
        p = [107,349]
        screen.blit(ml_arrow, p)
    if s.game.mystic_lines.position == 9:
        p = [107,313]
        screen.blit(ml_arrow, p)
    if s.game.mystic_lines.position == 10:
        p = [97,267]
        screen.blit(ml_letter, p)
        p = [410,293]
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
        o = [192,790]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 2:
        o = [235,790]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 3:
        o = [274,790]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 4:
        o = [312,790]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 5:
        o = [349,790]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 6:
        o = [391,790]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 7:
        o = [441,790]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 8:
        o = [489,790]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 9:
        o = [537,790]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 10:
        o = [585,790]
        screen.blit(odds, o)

    if s.game.green_odds.position == 1:
        o = [192,856]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 2:
        o = [235,856]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 3:
        o = [274,856]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 4:
        o = [312,856]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 5:
        o = [349,856]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 6:
        o = [391,856]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 7:
        o = [441,856]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 8:
        o = [489,856]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 9:
        o = [537,856]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 10:
        o = [585,856]
        screen.blit(odds, o)

    if s.game.yellow_odds.position == 1:
        o = [192,919]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 2:
        o = [235,919]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 3:
        o = [274,919]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 4:
        o = [312,919]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 5:
        o = [349,919]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 6:
        o = [391,919]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 7:
        o = [441,919]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 8:
        o = [489,919]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 9:
        o = [537,919]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 10:
        o = [585,919]
        screen.blit(odds, o)

    if s.game.blue_odds.position == 1:
        o = [192,982]
        screen.blit(odds, o)
    elif s.game.blue_odds.position == 2:
        o = [235,982]
        screen.blit(odds, o)
    elif s.game.blue_odds.position == 3:
        o = [274,982]
        screen.blit(odds, o)
    elif s.game.blue_odds.position == 4:
        o = [312,982]
        screen.blit(odds, o)
    elif s.game.blue_odds.position == 5:
        o = [349,982]
        screen.blit(odds, o)
    elif s.game.blue_odds.position == 6:
        o = [391,982]
        screen.blit(odds, o)
    elif s.game.blue_odds.position == 7:
        o = [441,982]
        screen.blit(odds, o)
    elif s.game.blue_odds.position == 8:
        o = [489,982]
        screen.blit(odds, o)
    elif s.game.blue_odds.position == 9:
        o = [537,982]
        screen.blit(odds, o)
    elif s.game.blue_odds.position == 10:
        o = [585,982]
        screen.blit(odds, o)

    p = [199,216]
    screen.blit(letter1, p)
    p = [253,216]
    screen.blit(letter2, p)
    p = [305,216]
    screen.blit(letter3, p)
    p = [363,216]
    screen.blit(letter4, p)
    p = [415,216]
    screen.blit(letter5, p)
    p = [460,216]
    screen.blit(letter6, p)

    if s.game.red_odds.position < 5:
        p = [199,216]
        screen.blit(red_letter1, p)
    if s.game.red_odds.position in [5,6]:
        p = [253,216]
        screen.blit(red_letter2, p)
    if s.game.red_odds.position == 7:
        p = [305,216]
        screen.blit(red_letter3, p)
    if s.game.red_odds.position == 8:
        p = [363,216]
        screen.blit(red_letter4, p)
    if s.game.red_odds.position == 9:
        p = [415,216]
        screen.blit(red_letter5, p)
    if s.game.red_odds.position == 10:
        p = [460,216]
        screen.blit(red_letter6, p)

    if s.game.two_red_letter.status == True:
        p = [10,366]
        screen.blit(red_letter, p)
        p = [51,274]
        screen.blit(two_red, p)
    if s.game.three_red_letter.status == True:
        p = [10,366]
        screen.blit(red_letter, p)
        p = [11,276]
        screen.blit(two_red, p)

    if s.game.three_stars.status == True:
        p = [8,453]
        screen.blit(four_stars, p)
        p = [8,545]
        screen.blit(six_stars, p)
    if s.game.six_stars.status == True:
        p = [8,453]
        screen.blit(four_stars, p)
        p = [48,544]
        screen.blit(six_stars, p)

    if s.game.tilt.status == False:
        if s.game.color_selector.position != 0:
            p = [534,746]
            screen.blit(double, p)
            p = [578,746]
            screen.blit(double, p)
            p = [624,746]
            screen.blit(double, p)
            p = [669,746]
            screen.blit(double, p)
            # Red DD
            if s.game.color_selector.position == 1:
                if s.game.double_red.status == True:
                    p = [533,597]
                    screen.blit(double, p)
                else:
                    #Red D
                    p = [534,634]
                    screen.blit(double, p)
                if s.game.double_yellow.status == True:
                    p = [578,671]
                    screen.blit(double, p)
                else:
                    p = [579,709]
                    screen.blit(double, p)
                if s.game.double_green.status == True:
                    p = [624,671]
                    screen.blit(double, p)
                else:
                    p = [624,709]
                    screen.blit(double, p)
                if s.game.double_blue.status == True:
                    p = [668,670]
                    screen.blit(double, p)
                else:
                    p = [668,709]
                    screen.blit(double, p)
            elif s.game.color_selector.position == 2:
                #Yellow DD
                if s.game.double_yellow.status == True:
                    p = [578,597]
                    screen.blit(double, p)
                else:
                    p = [578,634]
                    screen.blit(double, p)
                if s.game.double_red.status == True:
                    p = [534,671]
                    screen.blit(double, p)
                else:
                    p = [534,709]
                    screen.blit(double, p)
                if s.game.double_green.status == True:
                    p = [624,671]
                    screen.blit(double, p)
                else:
                    p = [624,709]
                    screen.blit(double, p)
                if s.game.double_blue.status == True:
                    p = [668,670]
                    screen.blit(double, p)
                else:
                    p = [668,709]
                    screen.blit(double, p)

            elif s.game.color_selector.position == 3:
                #Green DD
                if s.game.double_green.status == True:
                    p = [623,597]
                    screen.blit(double, p)
                else:
                    p = [623,634]
                    screen.blit(double, p)
                if s.game.double_red.status == True:
                    p = [534,671]
                    screen.blit(double, p)
                else:
                    p = [534,709]
                    screen.blit(double, p)
                if s.game.double_yellow.status == True:
                    p = [578,671]
                    screen.blit(double, p)
                else:
                    p = [579,709]
                    screen.blit(double, p)
                if s.game.double_blue.status == True:
                    p = [668,670]
                    screen.blit(double, p)
                else:
                    p = [668,709]
                    screen.blit(double, p)
            elif s.game.color_selector.position == 4:
                #Blue DD
                if s.game.double_blue.status == True:
                    p = [668,598]
                    screen.blit(double, p)
                else:
                    p = [668,634]
                    screen.blit(double, p)
                if s.game.double_red.status == True:
                    p = [534,671]
                    screen.blit(double, p)
                else:
                    p = [534,709]
                    screen.blit(double, p)
                if s.game.double_yellow.status == True:
                    p = [578,671]
                    screen.blit(double, p)
                else:
                    p = [579,709]
                    screen.blit(double, p)
                if s.game.double_green.status == True:
                    p = [624,671]
                    screen.blit(double, p)
                else:
                    p = [624,709]
                    screen.blit(double, p)
        else:
            if s.game.double_red.status == True:
                p = [534,634]
                screen.blit(double, p)
            if s.game.double_yellow.status == True:
                p = [578,634]
                screen.blit(double, p)
            if s.game.double_green.status == True:
                p = [623,634]
                screen.blit(double, p)
            if s.game.double_blue.status == True:
                p = [668,634]
                screen.blit(double, p)
            if s.game.double_red.status == False and s.game.double_yellow.status == False and s.game.double_green.status == False and s.game.double_blue.status == False:
                p = [486,597]
                screen.blit(no_scores_changed, p)
                p = [534,671]
                screen.blit(double, p)
                p = [578,671]
                screen.blit(double, p)
                p = [624,671]
                screen.blit(double, p)
                p = [668,671]
                screen.blit(double, p)

    if s.game.score_select.position == 1:
        p = [90,674]
        screen.blit(score_arrow, p)
    if s.game.score_select.position == 2:
        p = [132,674]
        screen.blit(score_arrow, p)
    if s.game.score_select.position == 3:
        p = [172,674]
        screen.blit(score_arrow, p)
    if s.game.score_select.position in [4,5,6,7]:
        p = [206,649]
        screen.blit(scores, p)
        if s.game.ball_count.position == 1:
            s.cancel_delayed(name="blink_score")
            blink_score([s,1,1])
        else:
            s.cancel_delayed(name="blink_score")
    if s.game.score_select.position == 5:
        p = [295,674]
        screen.blit(score_arrow, p)
    if s.game.score_select.position == 6:
        p = [332,674]
        screen.blit(score_arrow, p)
    if s.game.score_select.position == 7:
        p = [373,674]
        screen.blit(score_arrow, p)
    if s.game.score_select.position == 8:
        p = [405,648]
        screen.blit(scores, p)
        if s.game.ball_count.position == 2:
            s.cancel_delayed(name="blink_score")
            blink_score([s,1,1])
        else:
            s.cancel_delayed(name="blink_score")


    if s.game.tilt.status == True:
        tilt_position = [659,820]
        screen.blit(tilt, tilt_position)

    pygame.display.update()

def blink_score(args):
    dirty_rects = []
    s = args[0]
    b = args[1]
    sn = args[2]

    if b == 0:
        if sn == 1:
            p = [7,649]
            dirty_rects.append(screen.blit(scores, p))
        pygame.display.update(dirty_rects)
    else:
        dirty_rects.append(screen.blit(bg_gi, (7,649), pygame.Rect(7,649,77,77)))
        pygame.display.update(dirty_rects)
    b = not b

    args = [s,b,sn]

    s.delay(name="blink_score", delay=0.1, handler=blink_score, param=args)


def blink(args):
    dirty_rects = []
    s = args[0]
    b = args[1]
    sn = args[2]

    if b == 0:
        if sn == 1:
            p = [279,624]
            dirty_rects.append(screen.blit(select_now, p))
        pygame.display.update(dirty_rects)
    else:
        dirty_rects.append(screen.blit(bg_gi, (279,624), pygame.Rect(279,624,161,23)))
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

        p = [199,216]
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],52,52)))
        dirty_rects.append(screen.blit(letter1, p))

        p = [253,216]
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],52,55)))
        dirty_rects.append(screen.blit(letter2, p))
        
        p = [305,216]
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],54,54)))
        dirty_rects.append(screen.blit(letter3, p))

        p = [363,216]
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],54,54)))
        dirty_rects.append(screen.blit(letter4, p))

        p = [415,216]
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],50,54)))
        dirty_rects.append(screen.blit(letter5, p))
        
        p = [460,216]
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],50,54)))
        dirty_rects.append(screen.blit(letter6, p))
        
        if s.game.red_odds.position < 5:
            p = [199,216]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],52,52)))
            dirty_rects.append(screen.blit(letter1, p))
            dirty_rects.append(screen.blit(red_letter1, p))
        if s.game.red_odds.position  in [5,6]:
            p = [253,216]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],52,55)))
            dirty_rects.append(screen.blit(letter2, p))
            dirty_rects.append(screen.blit(red_letter2, p))
        if s.game.red_odds.position == 7:
            p = [305,216]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],54,54)))
            dirty_rects.append(screen.blit(letter3, p))
            dirty_rects.append(screen.blit(red_letter3, p))
        if s.game.red_odds.position == 8:
            p = [363,216]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],54,54)))
            dirty_rects.append(screen.blit(letter4, p))
            dirty_rects.append(screen.blit(red_letter4, p))
        if s.game.red_odds.position == 9:
            p = [415,216]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],50,54)))
            dirty_rects.append(screen.blit(letter5, p))
            dirty_rects.append(screen.blit(red_letter5, p))
        if s.game.red_odds.position == 10:
            p = [460,216]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],50,54)))
            dirty_rects.append(screen.blit(letter6, p))
            dirty_rects.append(screen.blit(red_letter6, p))

        if s.game.score_select.position == 5:
            p = [295,674]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],28,30)))
            dirty_rects.append(screen.blit(score_arrow, p))
        if s.game.score_select.position == 6:
            p = [332,674]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],28,30)))
            dirty_rects.append(screen.blit(score_arrow, p))
        if s.game.score_select.position == 7:
            p = [373,674]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],28,30)))
            dirty_rects.append(screen.blit(score_arrow, p))
        if s.game.score_select.position == 8:
            p = [405,648]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],77,77)))
            dirty_rects.append(screen.blit(scores, p))

        if s.game.double_red.status == False and s.game.double_yellow.status == False and s.game.double_green.status == False and s.game.double_blue.status == False:
            p = [486,597]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],46,182)))
            dirty_rects.append(screen.blit(no_scores_changed, p))

        if s.game.mystic_lines.position == 1:
            p = [104,606]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],25,29)))
            dirty_rects.append(screen.blit(ml_arrow, p))
        if s.game.mystic_lines.position == 2:
            p = [105,570]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],25,29)))
            dirty_rects.append(screen.blit(ml_arrow, p))
        if s.game.mystic_lines.position == 3:
            p = [105,534]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],25,29)))
            dirty_rects.append(screen.blit(ml_arrow, p))
        if s.game.mystic_lines.position >= 4:
            p = [333,293]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],47,47)))
            dirty_rects.append(screen.blit(ml_letter, p))
            p = [94,483]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],47,47)))
            dirty_rects.append(screen.blit(ml_letter, p))
        if s.game.mystic_lines.position == 5:
            p = [105,458]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],25,29)))
            dirty_rects.append(screen.blit(ml_arrow, p))
        if s.game.mystic_lines.position == 6:
            p = [105,422]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],25,29)))
            dirty_rects.append(screen.blit(ml_arrow, p))
        if s.game.mystic_lines.position >= 7:
            p = [96,374]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],47,47)))
            dirty_rects.append(screen.blit(ml_letter, p))
            p = [258,293]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],47,47)))
            dirty_rects.append(screen.blit(ml_letter, p))
        if s.game.mystic_lines.position == 8:
            p = [107,349]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],25,29)))
            dirty_rects.append(screen.blit(ml_arrow, p))
        if s.game.mystic_lines.position == 9:
            p = [107,313]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],25,29)))
            dirty_rects.append(screen.blit(ml_arrow, p))
        if s.game.mystic_lines.position == 10:
            p = [97,267]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],47,47)))
            dirty_rects.append(screen.blit(ml_letter, p))
            p = [410,293]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],47,47)))
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
            p = [104,606]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],25,29)))
            dirty_rects.append(screen.blit(ml_arrow, p))
        if s.game.mystic_lines.position == 2:
            p = [105,570]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],25,29)))
            dirty_rects.append(screen.blit(ml_arrow, p))
        if s.game.mystic_lines.position == 3:
            p = [105,534]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],25,29)))
            dirty_rects.append(screen.blit(ml_arrow, p))
        if s.game.mystic_lines.position >= 4:
            p = [333,293]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],47,47)))
            dirty_rects.append(screen.blit(ml_letter, p))
            p = [94,483]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],47,47)))
            dirty_rects.append(screen.blit(ml_letter, p))
        if s.game.mystic_lines.position == 5:
            p = [105,458]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],25,29)))
            dirty_rects.append(screen.blit(ml_arrow, p))
        if s.game.mystic_lines.position == 6:
            p = [105,422]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],25,29)))
            dirty_rects.append(screen.blit(ml_arrow, p))
        if s.game.mystic_lines.position >= 7:
            p = [96,374]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],47,47)))
            dirty_rects.append(screen.blit(ml_letter, p))
            p = [258,293]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],47,47)))
            dirty_rects.append(screen.blit(ml_letter, p))
        if s.game.mystic_lines.position == 8:
            p = [107,349]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],25,29)))
            dirty_rects.append(screen.blit(ml_arrow, p))
        if s.game.mystic_lines.position == 9:
            p = [107,313]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],25,29)))
            dirty_rects.append(screen.blit(ml_arrow, p))
        if s.game.mystic_lines.position == 10:
            p = [97,267]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],47,47)))
            dirty_rects.append(screen.blit(ml_letter, p))
            p = [410,293]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],47,47)))
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
            p = [104,606]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],25,29)))
            dirty_rects.append(screen.blit(ml_arrow, p))
        if s.game.mystic_lines.position == 2:
            p = [105,570]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],25,29)))
            dirty_rects.append(screen.blit(ml_arrow, p))
        if s.game.mystic_lines.position == 3:
            p = [105,534]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],25,29)))
            dirty_rects.append(screen.blit(ml_arrow, p))
        if s.game.mystic_lines.position >= 4:
            p = [333,293]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],47,47)))
            dirty_rects.append(screen.blit(ml_letter, p))
            p = [94,483]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],47,47)))
            dirty_rects.append(screen.blit(ml_letter, p))
        if s.game.mystic_lines.position == 5:
            p = [105,458]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],25,29)))
            dirty_rects.append(screen.blit(ml_arrow, p))
        if s.game.mystic_lines.position == 6:
            p = [105,422]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],25,29)))
            dirty_rects.append(screen.blit(ml_arrow, p))
        if s.game.mystic_lines.position >= 7:
            p = [96,374]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],47,47)))
            dirty_rects.append(screen.blit(ml_letter, p))
            p = [258,293]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],47,47)))
            dirty_rects.append(screen.blit(ml_letter, p))
        if s.game.mystic_lines.position == 8:
            p = [107,349]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],25,29)))
            dirty_rects.append(screen.blit(ml_arrow, p))
        if s.game.mystic_lines.position == 9:
            p = [107,313]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],25,29)))
            dirty_rects.append(screen.blit(ml_arrow, p))
        if s.game.mystic_lines.position == 10:
            p = [97,267]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],47,47)))
            dirty_rects.append(screen.blit(ml_letter, p))
            p = [410,293]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],47,47)))
            dirty_rects.append(screen.blit(ml_letter, p))

    pygame.display.update(dirty_rects)



def eb_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]

    if s.game.extra_ball.position < 1:
        dirty_rects.append(screen.blit(bg_gi, (152,1045), pygame.Rect(152,1045,47,31)))
    if s.game.extra_ball.position < 2:
        dirty_rects.append(screen.blit(bg_gi, (203,1045), pygame.Rect(203,1045,59,34)))
    if s.game.extra_ball.position < 3:
        dirty_rects.append(screen.blit(bg_gi, (266,1045), pygame.Rect(266,1045,59,34)))
    if s.game.extra_ball.position < 4:
        dirty_rects.append(screen.blit(bg_gi, (326,1045), pygame.Rect(326,1045,47,31)))
    if s.game.extra_ball.position < 5:
        dirty_rects.append(screen.blit(bg_gi, (379,1045), pygame.Rect(379,1045,59,34)))
    if s.game.extra_ball.position < 6:
        dirty_rects.append(screen.blit(bg_gi, (441,1045), pygame.Rect(441,1045,59,34)))
    if s.game.extra_ball.position < 7:
        dirty_rects.append(screen.blit(bg_gi, (503,1045), pygame.Rect(503,1045,47,31)))
    if s.game.extra_ball.position < 8:
        dirty_rects.append(screen.blit(bg_gi, (554,1045), pygame.Rect(554,1045,59,34)))
    if s.game.extra_ball.position < 9:
        dirty_rects.append(screen.blit(bg_gi, (616,1045), pygame.Rect(616,1045,59,34)))
    pygame.display.update(dirty_rects)

    if num in [0,1,25,26]:
        if s.game.extra_ball.position < 1:
            p = [152,1045]
            dirty_rects.append(screen.blit(eb_number, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [8,9,33,34]:
        if s.game.extra_ball.position < 2:
            p = [203,1045]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [18,19,43,44]:
        if s.game.extra_ball.position < 3:
            p = [266,1045]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [4,5,29,30]:
        if s.game.extra_ball.position < 4:
            p = [326,1045]
            dirty_rects.append(screen.blit(eb_number, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [14,15,39,40]:
        if s.game.extra_ball.position < 5:
            p = [379,1045]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [12,13,37,38]:
        if s.game.extra_ball.position < 6:
            p = [441,1045]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [2,3,27,28]:
        if s.game.extra_ball.position < 7:
            p = [503,1045]
            dirty_rects.append(screen.blit(eb_number, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [10,11,35,36]:
        if s.game.extra_ball.position < 8:
            p = [554,1045]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [6,7,16,17,22,23,31,32,41,42,47,48]:
        if s.game.extra_ball.position < 9:
            p = [616,1045]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return

def clear_odds(s, num):
    global screen

    dirty_rects = []

    if s.game.score_select.position not in [4,5,6,7]:
        dirty_rects.append(screen.blit(bg_gi, (206,649), pygame.Rect(206,649,77,77)))
    if s.game.score_select.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (405,648), pygame.Rect(405,648,77,77)))
    if s.game.double_red.status == False:
        dirty_rects.append(screen.blit(bg_gi, (534,634), pygame.Rect(534,634,42,34)))
    if s.game.double_yellow.status == False:
        dirty_rects.append(screen.blit(bg_gi, (578,634), pygame.Rect(578,634,42,34)))
    if s.game.double_green.status == False:
        dirty_rects.append(screen.blit(bg_gi, (623,634), pygame.Rect(623,634,42,34)))
    if s.game.double_blue.status == False:
        dirty_rects.append(screen.blit(bg_gi, (668,634), pygame.Rect(668,634,42,34)))

    if s.game.yellow_odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (235,919), pygame.Rect(235,919,46,61)))
    if s.game.yellow_odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (349,919), pygame.Rect(349,919,46,61)))
    if s.game.yellow_odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (391,919), pygame.Rect(391,919,46,61)))
    if s.game.yellow_odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (489,919), pygame.Rect(489,919,46,61)))
    if s.game.yellow_odds.position != 9:
        dirty_rects.append(screen.blit(bg_gi, (537,919), pygame.Rect(537,919,46,61)))
    if s.game.yellow_odds.position != 10:
        dirty_rects.append(screen.blit(bg_gi, (585,919), pygame.Rect(585,919,46,61)))

    if s.game.red_odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (274,790), pygame.Rect(274,790,46,61)))
    if s.game.red_odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (312,790), pygame.Rect(312,790,46,61)))
    if s.game.red_odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (441,790), pygame.Rect(441,790,46,61)))
    if s.game.red_odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (489,790), pygame.Rect(489,790,46,61)))
    if s.game.red_odds.position != 9:
        dirty_rects.append(screen.blit(bg_gi, (537,790), pygame.Rect(537,790,46,61)))
    if s.game.red_odds.position != 10:
        dirty_rects.append(screen.blit(bg_gi, (585,790), pygame.Rect(585,790,46,61)))

    if s.game.green_odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (235,856), pygame.Rect(235,856,46,61)))
    if s.game.green_odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (349,856), pygame.Rect(349,856,46,61)))
    if s.game.green_odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (441,856), pygame.Rect(441,856,46,61)))
    if s.game.green_odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (489,856), pygame.Rect(489,856,46,61)))
    if s.game.green_odds.position != 9:
        dirty_rects.append(screen.blit(bg_gi, (537,856), pygame.Rect(537,856,46,61)))
    if s.game.green_odds.position != 10:
        dirty_rects.append(screen.blit(bg_gi, (585,856), pygame.Rect(585,856,46,61)))

    if s.game.blue_odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (235,982), pygame.Rect(235,982,46,61)))
    if s.game.blue_odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (349,982), pygame.Rect(349,982,46,61)))
    if s.game.blue_odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (441,982), pygame.Rect(441,982,46,61)))
    if s.game.blue_odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (489,982), pygame.Rect(489,982,46,61)))
    if s.game.blue_odds.position != 9:
        dirty_rects.append(screen.blit(bg_gi, (537,982), pygame.Rect(537,982,46,61)))
    if s.game.blue_odds.position != 10:
        dirty_rects.append(screen.blit(bg_gi, (585,982), pygame.Rect(585,982,46,61)))

    pygame.display.update(dirty_rects)

def draw_odds_animation(s, num):
    global screen
    dirty_rects = []

    if num in [4,29]:
        if s.game.score_select.position not in [4,5,6,7]:
            p = [206,649]
            dirty_rects.append(screen.blit(scores, p))
            pygame.display.update(dirty_rects)
            return
    if num in [12,37]:
        if s.game.score_select.position not in [8]:
            p = [405,648]
            dirty_rects.append(screen.blit(scores, p))
            pygame.display.update(dirty_rects)
            return
    if num in [15,40]:
        if s.game.double_yellow.status == False:
            p = [578,634]
            dirty_rects.append(screen.blit(double, p))
            pygame.display.update(dirty_rects)
            return
    if num in [0,25]:
        if s.game.double_green.status == False:
            p = [623,634]
            dirty_rects.append(screen.blit(double, p))
            pygame.display.update(dirty_rects)
            return
    if num in [9,34]:
        if s.game.double_blue.status == False:
            p = [668,634]
            dirty_rects.append(screen.blit(double, p))
            pygame.display.update(dirty_rects)
            return
    if num in [19,44]:
        if s.game.double_red.status == False:
            p = [534,634]
            dirty_rects.append(screen.blit(double, p))
            pygame.display.update(dirty_rects)
            return

    if num in [22,47]:
        if s.game.yellow_odds.position != 2:
            p = [235,919]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [13,38]:
        if s.game.yellow_odds.position != 5:
            p = [349,919]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [17,42]:
        if s.game.yellow_odds.position != 6:
            p = [391,919]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [11,36]:
        if s.game.yellow_odds.position != 8:
            p = [489,919]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [7,32]:
        if s.game.yellow_odds.position != 9:
            p = [537,919]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [21,46]:
        if s.game.yellow_odds.position != 10:
            p = [585,919]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return

    if num in [2,27]:
        if s.game.red_odds.position != 3:
            p = [274,790]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [10,35]:
        if s.game.red_odds.position != 4:
            p = [312,790]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [6,31]:
        if s.game.red_odds.position != 7:
            p = [441,790]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [14,39]:
        if s.game.red_odds.position != 8:
            p = [489,790]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [1,26]:
        if s.game.red_odds.position != 9:
            p = [537,790]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [20,45]:
        if s.game.red_odds.position != 10:
            p = [585,790]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return

    if num in [8,33]:
        if s.game.blue_odds.position != 2:
            p = [235,982]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [23,48]:
        if s.game.blue_odds.position != 5:
            p = [349,982]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [3,28]:
        if s.game.blue_odds.position != 7:
            p = [441,982]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [18,43]:
        if s.game.blue_odds.position != 8:
            p = [489,982]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [5,30]:
        if s.game.blue_odds.position != 9:
            p = [537,982]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [16,41]:
        if s.game.blue_odds.position != 10:
            p = [585,982]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return

    if num in [8,33]:
        if s.game.green_odds.position != 2:
            p = [235,856]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [23,48]:
        if s.game.green_odds.position != 5:
            p = [349,856]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [3,28]:
        if s.game.green_odds.position != 7:
            p = [441,856]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [18,43]:
        if s.game.green_odds.position != 8:
            p = [489,856]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [5,30]:
        if s.game.green_odds.position != 9:
            p = [537,856]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [16,41]:
        if s.game.green_odds.position != 10:
            p = [585,856]
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
    
    if (s.game.mystic_lines.position < 4 and s.game.two_red_letter.status == False and s.game.three_red_letter.status == False) and s.game.selection_feature.position < 6:
        dirty_rects.append(screen.blit(bg_gi, (559,516), pygame.Rect(559,516,148,45)))

    if (s.game.mystic_lines.position < 4 and s.game.two_red_letter.status == False and s.game.three_red_letter.status == False) and s.game.selection_feature.position not in [7,8]:
        dirty_rects.append(screen.blit(bg_gi, (559,382), pygame.Rect(559,382,148,45)))
    
    if (s.game.mystic_lines.position < 4 and s.game.two_red_letter.status == False and s.game.three_red_letter.status == False) and s.game.selection_feature.position < 9:
        dirty_rects.append(screen.blit(bg_gi, (559,338), pygame.Rect(559,338,148,45)))

    if s.game.yellow_star.status == False:
        dirty_rects.append(screen.blit(bg_gi, (559,471), pygame.Rect(559,471,148,45)))
    if s.game.red_star.status == False:
        dirty_rects.append(screen.blit(bg_gi, (559,426), pygame.Rect(559,426,148,45)))

    if s.game.three_red_letter.status == False:
        dirty_rects.append(screen.blit(bg_gi, (11,276), pygame.Rect(11,276,38,90)))
    if s.game.two_red_letter.status == False:
        dirty_rects.append(screen.blit(bg_gi, (51,274), pygame.Rect(51,274,38,90)))
    if s.game.three_stars.status == False:
        dirty_rects.append(screen.blit(bg_gi, (8,545), pygame.Rect(8,545,80,91)))
    if s.game.six_stars.status == False:
        dirty_rects.append(screen.blit(bg_gi, (48,544), pygame.Rect(48,544,80,91)))
    if s.game.mystic_lines.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (105,570), pygame.Rect(105,570,25,24)))
    if s.game.mystic_lines.position < 4:
        dirty_rects.append(screen.blit(bg_gi, (94,483), pygame.Rect(94,483,47,47)))
        dirty_rects.append(screen.blit(bg_gi, (333,293), pygame.Rect(333,293,47,47)))
    if s.game.mystic_lines.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (105,458), pygame.Rect(105,458,25,24)))
    if s.game.mystic_lines.position < 7:
        dirty_rects.append(screen.blit(bg_gi, (96,374), pygame.Rect(96,374,47,47)))
        dirty_rects.append(screen.blit(bg_gi, (258,293), pygame.Rect(258,293,47,47)))
    if s.game.mystic_lines.position != 9:
        dirty_rects.append(screen.blit(bg_gi, (107,313), pygame.Rect(107,313,25,24)))
    if s.game.mystic_lines.position < 10:
        dirty_rects.append(screen.blit(bg_gi, (97,267), pygame.Rect(97,267,47,47)))
        dirty_rects.append(screen.blit(bg_gi, (410,293), pygame.Rect(410,293,47,47)))

    pygame.display.update(dirty_rects)


def draw_feature_animation(s, num):
    global screen
    dirty_rects = []
 

    if num in [14,18,39,43]:
        if s.game.selection_feature.position not in [1,2,3,4,5,6] and (s.game.mystic_lines.position < 4 and s.game.two_red_letter.status == False and s.game.three_red_letter.status == False):
            p = [557,516]
            dirty_rects.append(screen.blit(time, p))
            pygame.display.update(dirty_rects)
            return
    if num in [15,40]:
        if s.game.selection_feature.position not in [7,8] and (s.game.mystic_lines.position < 4 and s.game.two_red_letter.status == False and s.game.three_red_letter.status == False):
            p = [559,382]
            dirty_rects.append(screen.blit(time, p))
            pygame.display.update(dirty_rects)
            return
    if num in [3,7,28,32]:
        if s.game.selection_feature.position not in [9] and (s.game.mystic_lines.position < 4 and s.game.two_red_letter.status == False and s.game.three_red_letter.status == False):
            p = [559,338]
            dirty_rects.append(screen.blit(time, p))
            pygame.display.update(dirty_rects)
            return
    if num in [20,45]:
        if s.game.red_star.status == False:
            p = [559,426]
            dirty_rects.append(screen.blit(time, p))
            s.game.coils.redROLamp.pulse(85)
            pygame.display.update(dirty_rects)
            return
    if num in [13,38]:
        if s.game.yellow_star.status == False:
            p = [559,471]
            dirty_rects.append(screen.blit(time, p))
            s.game.coils.yellowROLamp.pulse(85)
            pygame.display.update(dirty_rects)
            return
    if num in [1,8,26,33]:
        if s.game.three_red_letter.status == False:
            p = [11,276]
            dirty_rects.append(screen.blit(two_red, p))
            pygame.display.update(dirty_rects)
            return
    if num in [17,42]:
        if s.game.two_red_letter.status == False:
            p = [51,274]
            dirty_rects.append(screen.blit(two_red, p))
            pygame.display.update(dirty_rects)
            return
    if num in [16,41]:
        if s.game.three_stars.status == False:
            p = [8,545]
            dirty_rects.append(screen.blit(six_stars, p))
            pygame.display.update(dirty_rects)
            return
    if num in [4,29]:
        if s.game.six_stars.status == False:
            p = [48,544]
            dirty_rects.append(screen.blit(six_stars, p))
            pygame.display.update(dirty_rects)
            return
   
    if num in [5,11,30,36]:
        if s.game.mystic_lines.position != 2:
            p = [105,570]
            dirty_rects.append(screen.blit(ml_arrow, p))
            pygame.display.update(dirty_rects)
            return
    if num in [2,21,27,46]:
        if s.game.mystic_lines.position < 4:
            p = [94,483]
            dirty_rects.append(screen.blit(ml_letter, p))
            p = [333,293]
            dirty_rects.append(screen.blit(ml_letter, p))
            pygame.display.update(dirty_rects)
            return
    if num in [0,25]:
        if s.game.mystic_lines.position != 5:
            p = [105,458]
            dirty_rects.append(screen.blit(ml_arrow, p))
            pygame.display.update(dirty_rects)
            return
    if num in [12,22,37,47]:
        if s.game.mystic_lines.position < 7:
            p = [96,374]
            dirty_rects.append(screen.blit(ml_letter, p))
            p = [258,293]
            dirty_rects.append(screen.blit(ml_letter, p))
            pygame.display.update(dirty_rects)
            return
    if num in [9,19,34,44]:
        if s.game.mystic_lines.position != 9:
            p = [107,313]
            dirty_rects.append(screen.blit(ml_arrow, p))
            pygame.display.update(dirty_rects)
            return
    if num in [10,23,35,48]:
        if s.game.mystic_lines.position < 10:
            p = [97,267]
            dirty_rects.append(screen.blit(ml_letter, p))
            p = [410,293]
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
