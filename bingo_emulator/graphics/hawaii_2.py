
import pygame
import random

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

meter = pygame.image.load('graphics/assets/black_register_cover.png').convert()
odds = pygame.image.load('hawaii_2/assets/odds.png').convert_alpha()
eb = pygame.image.load('hawaii_2/assets/eb.png').convert_alpha()
eb_number = pygame.image.load('hawaii_2/assets/eb_number.png').convert_alpha()
extra_balls = pygame.image.load('hawaii_2/assets/extra_balls.png').convert_alpha()
time = pygame.image.load('hawaii_2/assets/time.png').convert_alpha()
ml_letter = pygame.image.load('hawaii_2/assets/ml_letter.png').convert_alpha()
ml_arrow = pygame.image.load('hawaii_2/assets/ml_arrow.png').convert_alpha()
select_now = pygame.image.load('hawaii_2/assets/select_now.png').convert_alpha()
tilt = pygame.image.load('hawaii_2/assets/tilt.png').convert_alpha()
button = pygame.image.load('hawaii_2/assets/pap.png').convert_alpha()
double = pygame.image.load('hawaii_2/assets/double.png').convert_alpha()
four_stars = pygame.image.load('hawaii_2/assets/four_stars.png').convert_alpha()
six_stars = pygame.image.load('hawaii_2/assets/six_stars.png').convert_alpha()
two_red = pygame.image.load('hawaii_2/assets/two_red.png').convert_alpha()
red_letter = pygame.image.load('hawaii_2/assets/red_letter.png').convert_alpha()
letter1 = pygame.image.load('hawaii_2/assets/letter1.png').convert_alpha()
letter2 = pygame.image.load('hawaii_2/assets/letter2.png').convert_alpha()
letter3 = pygame.image.load('hawaii_2/assets/letter3.png').convert_alpha()
letter4 = pygame.image.load('hawaii_2/assets/letter4.png').convert_alpha()
letter5 = pygame.image.load('hawaii_2/assets/letter5.png').convert_alpha()
letter6 = pygame.image.load('hawaii_2/assets/letter6.png').convert_alpha()
red_letter1 = pygame.image.load('hawaii_2/assets/red_letter1.png').convert_alpha()
red_letter2 = pygame.image.load('hawaii_2/assets/red_letter2.png').convert_alpha()
red_letter3 = pygame.image.load('hawaii_2/assets/red_letter3.png').convert_alpha()
red_letter4 = pygame.image.load('hawaii_2/assets/red_letter4.png').convert_alpha()
red_letter5 = pygame.image.load('hawaii_2/assets/red_letter5.png').convert_alpha()
red_letter6 = pygame.image.load('hawaii_2/assets/red_letter6.png').convert_alpha()
number_card = pygame.image.load('hawaii_2/assets/number_card.png').convert_alpha()
number = pygame.image.load('hawaii_2/assets/number.png').convert_alpha()
columnb1 = pygame.image.load('hawaii_2/assets/columnb1.png').convert_alpha()
columnb2 = pygame.image.load('hawaii_2/assets/columnb2.png').convert_alpha()
columna = pygame.image.load('hawaii_2/assets/columna.png').convert_alpha()
columnc1 = pygame.image.load('hawaii_2/assets/columnc1.png').convert_alpha()
columnc2 = pygame.image.load('hawaii_2/assets/columnc2.png').convert_alpha()
no_scores_changed = pygame.image.load('hawaii_2/assets/no_scores_changed.png').convert_alpha()
scores = pygame.image.load('hawaii_2/assets/scores.png').convert_alpha()
score_arrow = pygame.image.load('hawaii_2/assets/scores_arrow.png').convert_alpha()
stop_shop = pygame.image.load('hawaii_2/assets/stop_shop.png').convert_alpha()
play_ss = pygame.image.load('hawaii_2/assets/play_ss.png').convert_alpha()
bg_menu = pygame.image.load('hawaii_2/assets/hawaii_2_menu.png').convert_alpha()
bg_gi = pygame.image.load('hawaii_2/assets/hawaii_2_gi.png').convert_alpha()
bg_off = pygame.image.load('hawaii_2/assets/hawaii_2_off.png').convert_alpha()

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
        eb_position = [36,1051]
        screen.blit(extra_balls, eb_position)

    if s.game.extra_ball.position >= 1:
        eb_position = [144,1050]
        screen.blit(eb_number, eb_position)
    if s.game.extra_ball.position >= 2:
        eb_position = [196,1050]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 3:
        eb_position = [258,1050]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 4:
        eb_position = [320,1050]
        screen.blit(eb_number, eb_position)
    if s.game.extra_ball.position >= 5:
        eb_position = [372,1050]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 6:
        eb_position = [436,1049]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 7:
        eb_position = [498,1049]
        screen.blit(eb_number, eb_position)
    if s.game.extra_ball.position >= 8:
        eb_position = [550,1049]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 9:
        eb_position = [614,1049]
        screen.blit(eb, eb_position)

    if s.game.red_star.status == True:
        rs_position = [562,408]
        screen.blit(time, rs_position)
    if s.game.yellow_star.status == True:
        rs_position = [562,454]
        screen.blit(time, rs_position)

    if s.game.mystic_lines.position >= 4 or s.game.two_red_letter.status == True or s.game.three_red_letter.status == True:
        if s.game.selection_feature.position < 7:
            bfp = [562,498]
            screen.blit(time, bfp)
        elif s.game.selection_feature.position in [7,8]:
            bfp = [564,363]
            screen.blit(time, bfp)
        elif s.game.selection_feature.position == 9:
            bfp = [564,318]
            screen.blit(time, bfp)

    if s.game.ball_count.position < 1 or (s.game.ball_count.position == 2 and s.game.x_feature.position == 6):
        if s.game.odds_only.status == True:
            b = [12,920]
            screen.blit(button, b)
        elif s.game.features.status == True:
            b = [11,960]
            screen.blit(button, b)
        else:
            b = [11,998]
            screen.blit(button, b)


    if s.game.mystic_lines.position == 1:
        p = [108,610]
        screen.blit(ml_arrow, p)
    if s.game.mystic_lines.position == 2:
        p = [108,573]
        screen.blit(ml_arrow, p)
    if s.game.mystic_lines.position == 3:
        p = [108,538]
        screen.blit(ml_arrow, p)
    if s.game.mystic_lines.position >= 4:
        p = [98,490]
        screen.blit(ml_letter, p)
        p = [340,295]
        screen.blit(ml_letter, p)
    if s.game.mystic_lines.position == 5:
        p = [108,462]
        screen.blit(ml_arrow, p)
    if s.game.mystic_lines.position == 6:
        p = [108,425]
        screen.blit(ml_arrow, p)
    if s.game.mystic_lines.position >= 7:
        p = [98,378]
        screen.blit(ml_letter, p)
        p = [264,296]
        screen.blit(ml_letter, p)
    if s.game.mystic_lines.position == 8:
        p = [108,349]
        screen.blit(ml_arrow, p)
    if s.game.mystic_lines.position == 9:
        p = [108,312]
        screen.blit(ml_arrow, p)
    if s.game.mystic_lines.position == 10:
        p = [98,266]
        screen.blit(ml_letter, p)
        p = [416,294]
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

    p = [198,210]
    screen.blit(letter1, p)
    p = [262,210]
    screen.blit(letter2, p)
    p = [321,210]
    screen.blit(letter3, p)
    p = [412,210]
    screen.blit(letter4, p)
    p = [472,210]
    screen.blit(letter5, p)
    p = [509,210]
    screen.blit(letter6, p)

    if s.game.red_odds.position < 5:
        p = [198,210]
        screen.blit(red_letter1, p)
    if s.game.red_odds.position in [5,6]:
        p = [262,210]
        screen.blit(red_letter2, p)
    if s.game.red_odds.position == 7:
        p = [321,210]
        screen.blit(red_letter3, p)
    if s.game.red_odds.position == 8:
        p = [412,210]
        screen.blit(red_letter4, p)
    if s.game.red_odds.position == 9:
        p = [472,210]
        screen.blit(red_letter5, p)
    if s.game.red_odds.position == 10:
        p = [509,210]
        screen.blit(red_letter6, p)

    if s.game.two_red_letter.status == True:
        p = [8,366]
        screen.blit(red_letter, p)
        p = [51,274]
        screen.blit(two_red, p)
    if s.game.three_red_letter.status == True:
        p = [8,366]
        screen.blit(red_letter, p)
        p = [11,276]
        screen.blit(two_red, p)

    if s.game.three_stars.status == True:
        p = [8,460]
        screen.blit(four_stars, p)
        p = [8,548]
        screen.blit(six_stars, p)
    if s.game.six_stars.status == True:
        p = [8,460]
        screen.blit(four_stars, p)
        p = [50,547]
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
        p = [91,671]
        screen.blit(score_arrow, p)
    if s.game.score_select.position == 2:
        p = [134,670]
        screen.blit(score_arrow, p)
    if s.game.score_select.position == 3:
        p = [171,670]
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
        p = [297,670]
        screen.blit(score_arrow, p)
    if s.game.score_select.position == 6:
        p = [335,670]
        screen.blit(score_arrow, p)
    if s.game.score_select.position == 7:
        p = [376,670]
        screen.blit(score_arrow, p)
    if s.game.score_select.position == 8:
        p = [405,648]
        screen.blit(scores, p)
        if s.game.ball_count.position == 2:
            s.cancel_delayed(name="blink_score")
            blink_score([s,1,1])
        else:
            s.cancel_delayed(name="blink_score")
    if s.game.x_feature.position == 1:
        p = [120,736]
        screen.blit(score_arrow, p)
    if s.game.x_feature.position == 2:
        p = [161,736]
        screen.blit(score_arrow, p)
    if s.game.x_feature.position == 3:
        p = [203,736]
        screen.blit(score_arrow, p)
    if s.game.x_feature.position == 4:
        p = [242,736]
        screen.blit(score_arrow, p)
    if s.game.x_feature.position == 5:
        p = [283,736]
        screen.blit(score_arrow, p)
    if s.game.x_feature.position == 6:
        p = [315,722]
        screen.blit(stop_shop, p)
        if s.game.ball_count.position == 2:
            p = [417,720]
            screen.blit(play_ss, p)

    if s.game.tilt.status == True:
        tilt_position = [662,823]
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
        dirty_rects.append(screen.blit(bg_gi, (7,649), pygame.Rect(7,649,85,68)))
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
            p = [284,627]
            dirty_rects.append(screen.blit(select_now, p))
        pygame.display.update(dirty_rects)
    else:
        dirty_rects.append(screen.blit(bg_gi, (284,627), pygame.Rect(284,627,161,23)))
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

        p = [198,210]
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],60,68)))
        dirty_rects.append(screen.blit(letter1, p))

        p = [262,210]
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],60,68)))
        dirty_rects.append(screen.blit(letter2, p))
        
        p = [321,210]
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],87,68)))
        dirty_rects.append(screen.blit(letter3, p))

        p = [412,210]
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],58,68)))
        dirty_rects.append(screen.blit(letter4, p))

        p = [472,210]
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],35,67)))
        dirty_rects.append(screen.blit(letter5, p))
        
        p = [509,210]
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],35,67)))
        dirty_rects.append(screen.blit(letter6, p))
        
        if s.game.red_odds.position < 5:
            p = [198,210]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],60,68)))
            dirty_rects.append(screen.blit(letter1, p))
            dirty_rects.append(screen.blit(red_letter1, p))
        if s.game.red_odds.position  in [5,6]:
            p = [262,210]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],60,68)))
            dirty_rects.append(screen.blit(letter2, p))
            dirty_rects.append(screen.blit(red_letter2, p))
        if s.game.red_odds.position == 7:
            p = [321,210]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],87,68)))
            dirty_rects.append(screen.blit(letter3, p))
            dirty_rects.append(screen.blit(red_letter3, p))
        if s.game.red_odds.position == 8:
            p = [412,210]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],58,68)))
            dirty_rects.append(screen.blit(letter4, p))
            dirty_rects.append(screen.blit(red_letter4, p))
        if s.game.red_odds.position == 9:
            p = [472,210]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],35,67)))
            dirty_rects.append(screen.blit(letter5, p))
            dirty_rects.append(screen.blit(red_letter5, p))
        if s.game.red_odds.position == 10:
            p = [509,210]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],35,67)))
            dirty_rects.append(screen.blit(letter6, p))
            dirty_rects.append(screen.blit(red_letter6, p))

        if s.game.score_select.position == 5:
            p = [297,670]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],28,30)))
            dirty_rects.append(screen.blit(score_arrow, p))
        if s.game.score_select.position == 6:
            p = [335,670]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],28,30)))
            dirty_rects.append(screen.blit(score_arrow, p))
        if s.game.score_select.position == 7:
            p = [376,670]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],28,30)))
            dirty_rects.append(screen.blit(score_arrow, p))
        if s.game.score_select.position == 8:
            p = [405,648]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],85,68)))
            dirty_rects.append(screen.blit(scores, p))

        if s.game.double_red.status == False and s.game.double_yellow.status == False and s.game.double_green.status == False and s.game.double_blue.status == False:
            p = [486,597]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],46,182)))
            dirty_rects.append(screen.blit(no_scores_changed, p))

        if s.game.mystic_lines.position >= 4:
            p = [340,295]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],47,47)))
            dirty_rects.append(screen.blit(ml_letter, p))
        if s.game.mystic_lines.position >= 7:
            p = [264,296]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],47,47)))
            dirty_rects.append(screen.blit(ml_letter, p))
        if s.game.mystic_lines.position == 10:
            p = [416,294]
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

        if s.game.mystic_lines.position >= 4:
            p = [340,295]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],47,47)))
            dirty_rects.append(screen.blit(ml_letter, p))
        if s.game.mystic_lines.position >= 7:
            p = [264,296]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],47,47)))
            dirty_rects.append(screen.blit(ml_letter, p))
        if s.game.mystic_lines.position == 10:
            p = [416,294]
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
            dirty_rects.append(screen.blit(bg_gi, (230,369), pygame.Rect(230,369,273,212)))
        else:
            dirty_rects.append(screen.blit(bg_off, (230,369), pygame.Rect(230,369,273,212)))

        if s.game.mystic_lines.position >= 4:
            p = [340,295]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],47,47)))
            dirty_rects.append(screen.blit(ml_letter, p))
        if s.game.mystic_lines.position >= 7:
            p = [264,296]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],47,47)))
            dirty_rects.append(screen.blit(ml_letter, p))
        if s.game.mystic_lines.position == 10:
            p = [416,294]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],47,47)))
            dirty_rects.append(screen.blit(ml_letter, p))

    pygame.display.update(dirty_rects)


def eb_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]

    if s.game.extra_ball.position < 1:
        dirty_rects.append(screen.blit(bg_gi, (144,1050), pygame.Rect(144,1050,47,31)))
    if s.game.extra_ball.position < 2:
        dirty_rects.append(screen.blit(bg_gi, (196,1050), pygame.Rect(196,1050,59,34)))
    if s.game.extra_ball.position < 3:
        dirty_rects.append(screen.blit(bg_gi, (258,1050), pygame.Rect(258,1050,59,34)))
    if s.game.extra_ball.position < 4:
        dirty_rects.append(screen.blit(bg_gi, (320,1050), pygame.Rect(320,1050,47,31)))
    if s.game.extra_ball.position < 5:
        dirty_rects.append(screen.blit(bg_gi, (372,1050), pygame.Rect(372,1050,59,34)))
    if s.game.extra_ball.position < 6:
        dirty_rects.append(screen.blit(bg_gi, (436,1049), pygame.Rect(436,1049,59,34)))
    if s.game.extra_ball.position < 7:
        dirty_rects.append(screen.blit(bg_gi, (498,1049), pygame.Rect(498,1049,47,31)))
    if s.game.extra_ball.position < 8:
        dirty_rects.append(screen.blit(bg_gi, (550,1049), pygame.Rect(550,1049,59,34)))
    if s.game.extra_ball.position < 9:
        dirty_rects.append(screen.blit(bg_gi, (614,1049), pygame.Rect(614,1049,59,34)))
    pygame.display.update(dirty_rects)

    if num in [0,1,25,26]:
        if s.game.extra_ball.position < 1:
            p = [144,1050]
            dirty_rects.append(screen.blit(eb_number, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [8,9,20,21,33,34,45,46]:
        if s.game.extra_ball.position < 2:
            p = [196,1050]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [18,19,43,44]:
        if s.game.extra_ball.position < 3:
            p = [258,1050]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [4,5,29,30]:
        if s.game.extra_ball.position < 4:
            p = [320,1050]
            dirty_rects.append(screen.blit(eb_number, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [14,15,39,40]:
        if s.game.extra_ball.position < 5:
            p = [372,1050]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [12,13,37,38]:
        if s.game.extra_ball.position < 6:
            p = [436,1049]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [2,3,27,28]:
        if s.game.extra_ball.position < 7:
            p = [498,1049]
            dirty_rects.append(screen.blit(eb_number, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [10,11,35,36]:
        if s.game.extra_ball.position < 8:
            p = [550,1049]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [6,7,16,17,22,23,31,32,41,42,47,48]:
        if s.game.extra_ball.position < 9:
            p = [614,1049]
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
        dirty_rects.append(screen.blit(bg_gi, (562,498), pygame.Rect(562,498,156,48)))

    if (s.game.mystic_lines.position < 4 and s.game.two_red_letter.status == False and s.game.three_red_letter.status == False) and s.game.selection_feature.position not in [7,8]:
        dirty_rects.append(screen.blit(bg_gi, (564,363), pygame.Rect(564,363,156,48)))
    
    if (s.game.mystic_lines.position < 4 and s.game.two_red_letter.status == False and s.game.three_red_letter.status == False) and s.game.selection_feature.position < 9:
        dirty_rects.append(screen.blit(bg_gi, (564,318), pygame.Rect(564,318,156,48)))

    if s.game.yellow_star.status == False:
        dirty_rects.append(screen.blit(bg_gi, (562,454), pygame.Rect(562,454,156,48)))
    if s.game.red_star.status == False:
        dirty_rects.append(screen.blit(bg_gi, (562,408), pygame.Rect(562,408,156,48)))

    if s.game.three_red_letter.status == False:
        dirty_rects.append(screen.blit(bg_gi, (11,276), pygame.Rect(11,276,38,90)))
    if s.game.two_red_letter.status == False:
        dirty_rects.append(screen.blit(bg_gi, (51,274), pygame.Rect(51,274,38,90)))
    if s.game.three_stars.status == False:
        dirty_rects.append(screen.blit(bg_gi, (8,548), pygame.Rect(8,548,80,91)))
    if s.game.six_stars.status == False:
        dirty_rects.append(screen.blit(bg_gi, (50,547), pygame.Rect(50,547,80,91)))


    if s.game.mystic_lines.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (108,573), pygame.Rect(108,573,25,24)))
    if s.game.mystic_lines.position < 4:
        dirty_rects.append(screen.blit(bg_gi, (98,490), pygame.Rect(98,490,47,47)))
        dirty_rects.append(screen.blit(bg_gi, (340,295), pygame.Rect(340,295,47,47)))
    if s.game.mystic_lines.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (108,462), pygame.Rect(108,462,25,24)))
    if s.game.mystic_lines.position < 7:
        dirty_rects.append(screen.blit(bg_gi, (98,378), pygame.Rect(98,378,47,47)))
        dirty_rects.append(screen.blit(bg_gi, (264,296), pygame.Rect(264,296,47,47)))
    if s.game.mystic_lines.position != 9:
        dirty_rects.append(screen.blit(bg_gi, (108,312), pygame.Rect(108,312,25,24)))
    if s.game.mystic_lines.position < 10:
        dirty_rects.append(screen.blit(bg_gi, (98,266), pygame.Rect(98,266,47,47)))
        dirty_rects.append(screen.blit(bg_gi, (416,294), pygame.Rect(416,294,47,47)))

    pygame.display.update(dirty_rects)


def draw_feature_animation(s, num):
    global screen
    dirty_rects = []
     
    if num in [14,18,39,43]:
        if s.game.selection_feature.position not in [1,2,3,4,5,6] and (s.game.mystic_lines.position < 4 and s.game.two_red_letter.status == False and s.game.three_red_letter.status == False):
            p = [562,498]
            dirty_rects.append(screen.blit(time, p))
            pygame.display.update(dirty_rects)
            return
    if num in [15,40]:
        if s.game.selection_feature.position not in [7,8] and (s.game.mystic_lines.position < 4 and s.game.two_red_letter.status == False and s.game.three_red_letter.status == False):
            p = [564,363]
            dirty_rects.append(screen.blit(time, p))
            pygame.display.update(dirty_rects)
            return
    if num in [3,7,28,32]:
        if s.game.selection_feature.position not in [9] and (s.game.mystic_lines.position < 4 and s.game.two_red_letter.status == False and s.game.three_red_letter.status == False):
            p = [564,318]
            dirty_rects.append(screen.blit(time, p))
            pygame.display.update(dirty_rects)
            return
    if num in [20,45]:
        if s.game.red_star.status == False:
            p = [562,408]
            dirty_rects.append(screen.blit(time, p))
            s.game.coils.redROLamp.pulse(85)
            pygame.display.update(dirty_rects)
            return
    if num in [13,38]:
        if s.game.yellow_star.status == False:
            p = [562,454]
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
            p = [8,548]
            dirty_rects.append(screen.blit(six_stars, p))
            pygame.display.update(dirty_rects)
            return
    if num in [4,29]:
        if s.game.six_stars.status == False:
            p = [50,547]
            dirty_rects.append(screen.blit(six_stars, p))
            pygame.display.update(dirty_rects)
            return
   
    if num in [5,11,30,36]:
        if s.game.mystic_lines.position != 2:
            p = [108,573]
            dirty_rects.append(screen.blit(ml_arrow, p))
            pygame.display.update(dirty_rects)
            return
    if num in [2,21,27,46]:
        if s.game.mystic_lines.position < 4:
            p = [98,490]
            dirty_rects.append(screen.blit(ml_letter, p))
            p = [340,295]
            dirty_rects.append(screen.blit(ml_letter, p))
            pygame.display.update(dirty_rects)
            return
    if num in [0,25]:
        if s.game.mystic_lines.position != 5:
            p = [108,462]
            dirty_rects.append(screen.blit(ml_arrow, p))
            pygame.display.update(dirty_rects)
            return
    if num in [12,22,37,47]:
        if s.game.mystic_lines.position < 7:
            p = [98,378]
            dirty_rects.append(screen.blit(ml_letter, p))
            p = [264,296]
            dirty_rects.append(screen.blit(ml_letter, p))
            pygame.display.update(dirty_rects)
            return
    if num in [9,19,34,44]:
        if s.game.mystic_lines.position != 9:
            p = [108,312]
            dirty_rects.append(screen.blit(ml_arrow, p))
            pygame.display.update(dirty_rects)
            return
    if num in [10,23,35,48]:
        if s.game.mystic_lines.position < 10:
            p = [98,266]
            dirty_rects.append(screen.blit(ml_letter, p))
            p = [416,294]
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
