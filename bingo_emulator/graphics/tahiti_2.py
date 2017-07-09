
import pygame
import random

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

meter = pygame.image.load('graphics/assets/black_register_cover.png').convert()
odds = pygame.image.load('tahiti_2/assets/odds.png').convert_alpha()
time = pygame.image.load('tahiti_2/assets/time.png').convert_alpha()
ml_letter = pygame.image.load('tahiti_2/assets/ml_letter.png').convert_alpha()
ml_arrow = pygame.image.load('tahiti_2/assets/ml_arrow.png').convert_alpha()
diamond = pygame.image.load('tahiti_2/assets/diamond.png').convert_alpha()
up = pygame.image.load('tahiti_2/assets/up.png').convert_alpha()
select_now = pygame.image.load('tahiti_2/assets/select_now.png').convert_alpha()
tilt = pygame.image.load('tahiti_2/assets/tilt.png').convert_alpha()
double = pygame.image.load('tahiti_2/assets/double.png').convert_alpha()
stars = pygame.image.load('tahiti_2/assets/stars.png').convert_alpha()
number_card = pygame.image.load('tahiti_2/assets/number_card.png').convert_alpha()
number = pygame.image.load('tahiti_2/assets/number.png').convert_alpha()
columnb1 = pygame.image.load('tahiti_2/assets/columnb1.png').convert_alpha()
columnb2 = pygame.image.load('tahiti_2/assets/columnb2.png').convert_alpha()
columna = pygame.image.load('tahiti_2/assets/columna.png').convert_alpha()
columnc1 = pygame.image.load('tahiti_2/assets/columnc1.png').convert_alpha()
columnc2 = pygame.image.load('tahiti_2/assets/columnc2.png').convert_alpha()
ball_return = pygame.image.load('tahiti_2/assets/return.png').convert_alpha()
circle = pygame.image.load('tahiti_2/assets/circle.png').convert_alpha()
return_letter = pygame.image.load('tahiti_2/assets/return_letter.png').convert_alpha()
return_ind = pygame.image.load('tahiti_2/assets/return.png').convert_alpha()

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
        backglass = pygame.image.load('tahiti_2/assets/tahiti_2_menu.png').convert_alpha()
    else:
        if (s.game.anti_cheat.status == True):
            backglass = pygame.image.load('tahiti_2/assets/tahiti_2_gi.png').convert_alpha()
        else:
            backglass = pygame.image.load('tahiti_2/assets/tahiti_2_off.png').convert_alpha()
    backglass = pygame.transform.scale(backglass, (720, 1280))
    
    screen.blit(backglass, backglass_position)

    if s.game.mystic_lines.position >= 2:
        if s.game.selection_feature.position in [1,2,3]:
            bfp = [564,532]
            screen.blit(time, bfp)
        elif s.game.selection_feature.position in [4,5]:
            bfp = [564,435]
            screen.blit(time, bfp)
        elif s.game.selection_feature.position == 6:
            bfp = [564,336]
            screen.blit(time, bfp)
        if s.game.selection_feature.position == 3:
            p = [629,500]
            screen.blit(up, p)
        if s.game.selection_feature.position == 5:
            p = [629,403]
            screen.blit(up, p)

    if s.game.mystic_lines.position == 1:
        p = [276,685]
        screen.blit(ml_arrow, p)
    if s.game.mystic_lines.position >= 2:
        p = [321,679]
        screen.blit(circle, p)
        p = [344,283]
        screen.blit(ml_letter, p)
    if s.game.mystic_lines.position == 3:
        p = [379,685]
        screen.blit(ml_arrow, p)
    if s.game.mystic_lines.position >= 4:
        if s.game.bc.status == False:
            p = [423,633]
            screen.blit(circle, p)
            p = [260,283]
            screen.blit(ml_letter, p)
        else:
            p = [424,723]
            screen.blit(circle, p)
            p = [425,282]
            screen.blit(ml_letter, p)
    if s.game.mystic_lines.position == 5:
        p = [432,679]
        screen.blit(diamond, p)
    if s.game.mystic_lines.position == 6:
        if s.game.bc.status == False:
            p = [424,723]
            screen.blit(circle, p)
            p = [425,282]
            screen.blit(ml_letter, p)
        else:
            p = [423,633]
            screen.blit(circle, p)
            p = [260,283]
            screen.blit(ml_letter, p)


    if s.game.mystic_lines.position >= 2:
        t = 4
        if s.game.selection_feature.position in [4,5]:
            t = 5
        if s.game.selection_feature.position == 6:
            t = 6
        if s.game.ball_count.position == t:
            p = [497,660]
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
        o = [185,808]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 2:
        o = [220,808]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 3:
        o = [259,808]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 4:
        o = [295,808]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 5:
        o = [332,808]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 6:
        o = [375,808]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 7:
        o = [423,808]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 8:
        o = [484,808]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 9:
        o = [531,808]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 10:
        o = [580,808]
        screen.blit(odds, o)

    if s.game.yellow_odds.position == 1:
        o = [185,938]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 2:
        o = [220,938]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 3:
        o = [259,938]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 4:
        o = [295,938]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 5:
        o = [332,938]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 6:
        o = [375,938]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 7:
        o = [423,938]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 8:
        o = [484,938]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 9:
        o = [531,938]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 10:
        o = [580,938]
        screen.blit(odds, o)

    if s.game.green_odds.position == 1:
        o = [185,872]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 2:
        o = [220,872]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 3:
        o = [259,872]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 4:
        o = [295,872]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 5:
        o = [332,872]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 6:
        o = [375,872]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 7:
        o = [423,872]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 8:
        o = [484,872]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 9:
        o = [531,872]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 10:
        o = [580,872]
        screen.blit(odds, o)

    if s.game.blue_odds.position == 1:
        o = [185,1004]
        screen.blit(odds, o)
    elif s.game.blue_odds.position == 2:
        o = [220,1004]
        screen.blit(odds, o)
    elif s.game.blue_odds.position == 3:
        o = [259,1004]
        screen.blit(odds, o)
    elif s.game.blue_odds.position == 4:
        o = [295,1004]
        screen.blit(odds, o)
    elif s.game.blue_odds.position == 5:
        o = [332,1004]
        screen.blit(odds, o)
    elif s.game.blue_odds.position == 6:
        o = [375,1004]
        screen.blit(odds, o)
    elif s.game.blue_odds.position == 7:
        o = [423,1004]
        screen.blit(odds, o)
    elif s.game.blue_odds.position == 8:
        o = [484,1004]
        screen.blit(odds, o)
    elif s.game.blue_odds.position == 9:
        o = [531,1004]
        screen.blit(odds, o)
    elif s.game.blue_odds.position == 10:
        o = [580,1004]
        screen.blit(odds, o)


    if s.game.three_stars.status == True:
        p = [23,435]
        screen.blit(stars, p)
    if s.game.six_stars.status == True:
        p = [23,337]
        screen.blit(stars, p)

    if s.game.double_red.status == True:
        p = [628,811]
        screen.blit(double, p)
    if s.game.double_yellow.status == True:
        p = [628,942]
        screen.blit(double, p)
    if s.game.double_green.status == True:
        p = [628,878]
        screen.blit(double, p)
    if s.game.double_blue.status == True:
        p = [628,1009]
        screen.blit(double, p)

    if s.game.b_return.status == True:
        p = [24,566]
        screen.blit(return_letter, p)
        p = [93,566]
        screen.blit(return_letter, p)

        t = 4
        if s.game.selection_feature.position in [4,5]:
            t = 5
        if s.game.selection_feature.position == 6:
            t = 6
        if s.game.ball_count.position == t:
            p = [22,650]
            screen.blit(return_ind, p)

    if s.game.ball_return_played.status == True:
        p = [22,686]
        screen.blit(return_ind, p)

    if s.game.tilt.status == True:
        tilt_position = [508,603]
        screen.blit(tilt, tilt_position)

    pygame.display.update()

def feature_animation(num):
    global screen

    if num == 4:
        p = [379,685]
        screen.blit(ml_arrow, p)
        pygame.display.update()
    else:
        p = [423,633]
        screen.blit(circle, p)
        p = [260,283]
        screen.blit(ml_letter, p)
        pygame.display.update()


def odds_animation(num):
    global screen

    if num == 8:
        o = [185,872]
        screen.blit(odds, o)
    if num == 7:
        o = [220,872]
        screen.blit(odds, o)
    if num == 6:
        o = [259,872]
        screen.blit(odds, o)
    if num == 5:
        o = [295,872]
        screen.blit(odds, o)
    if num == 4:
        o = [332,872]
        screen.blit(odds, o)
    if num == 3:
        o = [375,872]
        screen.blit(odds, o)
    if num == 2:
        o = [423,872]
        screen.blit(odds, o)
    if num == 1:
        o = [484,872]
        screen.blit(odds, o)
    pygame.display.update()


