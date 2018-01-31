
import pygame
import random

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

meter = pygame.image.load('graphics/assets/black_register_cover.png').convert()
odds = pygame.image.load('mystic_gate/assets/odds.png').convert_alpha()
time = pygame.image.load('mystic_gate/assets/time.png').convert_alpha()
mg_letter = pygame.image.load('mystic_gate/assets/mg_letter.png').convert_alpha()
ml_arrow = pygame.image.load('mystic_gate/assets/ml_arrow.png').convert_alpha()
select_now = pygame.image.load('mystic_gate/assets/select_now.png').convert_alpha()
tilt = pygame.image.load('mystic_gate/assets/tilt.png').convert_alpha()
double = pygame.image.load('mystic_gate/assets/double.png').convert_alpha()
stars = pygame.image.load('mystic_gate/assets/stars.png').convert_alpha()
number_card = pygame.image.load('mystic_gate/assets/number_card.png').convert_alpha()
number = pygame.image.load('mystic_gate/assets/number.png').convert_alpha()
columnb1 = pygame.image.load('mystic_gate/assets/columnb1.png').convert_alpha()
columnb2 = pygame.image.load('mystic_gate/assets/columnb2.png').convert_alpha()
columna = pygame.image.load('mystic_gate/assets/columna.png').convert_alpha()
columnc1 = pygame.image.load('mystic_gate/assets/columnc1.png').convert_alpha()
columnc2 = pygame.image.load('mystic_gate/assets/columnc2.png').convert_alpha()
gate = pygame.image.load('mystic_gate/assets/gate.png').convert_alpha()
circle = pygame.image.load('mystic_gate/assets/circle.png').convert_alpha()
coin_limit = pygame.image.load('mystic_gate/assets/coin_limit.png').convert_alpha()
open_gate = pygame.image.load('mystic_gate/assets/open_gate.png').convert_alpha()
bg_menu = pygame.image.load('mystic_gate/assets/mystic_gate_menu.png').convert_alpha()
bg_gi = pygame.image.load('mystic_gate/assets/mystic_gate_gi.png').convert_alpha()
bg_off = pygame.image.load('mystic_gate/assets/mystic_gate_off.png').convert_alpha()

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

    if s.game.mystic_lines.position >= 2:
        if s.game.selection_feature.position in [1,2,3]:
            bfp = [551,538]
            screen.blit(time, bfp)
        elif s.game.selection_feature.position in [4,5]:
            bfp = [551,446]
            screen.blit(time, bfp)
        elif s.game.selection_feature.position == 6:
            bfp = [551,351]
            screen.blit(time, bfp)
        if s.game.selection_feature.position == 3:
            p = [604,496]
            screen.blit(circle, p)
        if s.game.selection_feature.position == 5:
            p = [604,403]
            screen.blit(circle, p)



    if s.game.mystic_lines.position == 1:
        p = [217,669]
        screen.blit(ml_arrow, p)
    if s.game.mystic_lines.position >= 2:
        p = [265,667]
        screen.blit(circle, p)
        p = [331,291]
        screen.blit(mg_letter, p)
    if s.game.mystic_lines.position == 3:
        p = [319,670]
        screen.blit(ml_arrow, p)
    if s.game.mystic_lines.position >= 4:
        p = [360,667]
        screen.blit(circle, p)
        p = [259,292]
        screen.blit(mg_letter, p)
    if s.game.mystic_lines.position == 5:
        p = [414,669]
        screen.blit(ml_arrow, p)
    if s.game.mystic_lines.position == 6:
        p = [459,667]
        screen.blit(circle, p)
        p = [410,293]
        screen.blit(mg_letter, p)

    if s.game.mystic_lines.position >= 2:
        t = 3
        if s.game.selection_feature.position in [4,5]:
            t = 4
        if s.game.selection_feature.position == 6:
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
        o = [185,804]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 2:
        o = [220,804]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 3:
        o = [259,804]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 4:
        o = [295,804]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 5:
        o = [332,804]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 6:
        o = [375,804]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 7:
        o = [423,804]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 8:
        o = [469,804]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 9:
        o = [517,804]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 10:
        o = [563,804]
        screen.blit(odds, o)

    if s.game.yellow_odds.position == 1:
        o = [185,934]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 2:
        o = [220,934]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 3:
        o = [259,934]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 4:
        o = [295,934]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 5:
        o = [332,934]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 6:
        o = [375,934]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 7:
        o = [423,934]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 8:
        o = [469,934]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 9:
        o = [517,934]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 10:
        o = [563,934]
        screen.blit(odds, o)

    if s.game.green_odds.position == 1:
        o = [185,868]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 2:
        o = [220,868]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 3:
        o = [259,868]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 4:
        o = [295,868]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 5:
        o = [332,868]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 6:
        o = [375,868]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 7:
        o = [423,868]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 8:
        o = [469,868]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 9:
        o = [517,868]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 10:
        o = [563,868]
        screen.blit(odds, o)

    if s.game.blue_odds.position == 1:
        o = [185,998]
        screen.blit(odds, o)
    elif s.game.blue_odds.position == 2:
        o = [220,998]
        screen.blit(odds, o)
    elif s.game.blue_odds.position == 3:
        o = [259,998]
        screen.blit(odds, o)
    elif s.game.blue_odds.position == 4:
        o = [295,998]
        screen.blit(odds, o)
    elif s.game.blue_odds.position == 5:
        o = [332,998]
        screen.blit(odds, o)
    elif s.game.blue_odds.position == 6:
        o = [375,998]
        screen.blit(odds, o)
    elif s.game.blue_odds.position == 7:
        o = [423,998]
        screen.blit(odds, o)
    elif s.game.blue_odds.position == 8:
        o = [469,998]
        screen.blit(odds, o)
    elif s.game.blue_odds.position == 9:
        o = [517,998]
        screen.blit(odds, o)
    elif s.game.blue_odds.position == 10:
        o = [563,998]
        screen.blit(odds, o)


    if s.game.three_stars.status == True:
        p = [21,445]
        screen.blit(stars, p)
    if s.game.six_stars.status == True:
        p = [21,350]
        screen.blit(stars, p)

    if s.game.double_red.status == True:
        p = [617,809]
        screen.blit(double, p)
    if s.game.double_yellow.status == True:
        p = [615,938]
        screen.blit(double, p)
    if s.game.double_green.status == True:
        p = [615,873]
        screen.blit(double, p)
    if s.game.double_blue.status == True:
        p = [615,1001]
        screen.blit(double, p)

    if s.game.tilt.status == True:
        tilt_position = [629,750]
        screen.blit(tilt, tilt_position)

    if s.game.coin.position == 40:
        p = [27,946]
        screen.blit(coin_limit, p)

    if s.game.gate_open.status == True:
        p = [26,1039]
        screen.blit(gate_open, p)

    if s.game.gate.status == True:
        p = [21,563]
        screen.blit(gate, p)

    pygame.display.update()

def blink(args):
    dirty_rects = []
    s = args[0]
    b = args[1]
    sn = args[2]

    if b == 0:
        if sn == 1:
            p = [517,655]
            dirty_rects.append(screen.blit(select_now, p))
        pygame.display.update(dirty_rects)
    else:
        dirty_rects.append(screen.blit(bg_gi, (517,655), pygame.Rect(517,655,87,68)))
        pygame.display.update(dirty_rects)
    b = not b

    args = [s,b,sn]

    s.delay(name="blink", delay=0.1, handler=blink, param=args)

p = [517,655]

def feature_animation(num):
    global screen

    if num == 4:
        p = [414,669]
        screen.blit(ml_arrow, p)
        pygame.display.update()
    else:
        p = [459,667]
        screen.blit(circle, p)
        p = [410,293]
        screen.blit(mg_letter, p)
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


