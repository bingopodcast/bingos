
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
                    p = [336,419]
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

        if s.game.mystic_lines.position == 1:
            p = [217,669]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],41,39)))
            dirty_rects.append(screen.blit(ml_arrow, p))
        if s.game.mystic_lines.position >= 2:
            p = [265,667]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],47,47)))
            dirty_rects.append(screen.blit(circle, p))
            p = [331,291]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],51,50)))
            dirty_rects.append(screen.blit(mg_letter, p))
        if s.game.mystic_lines.position == 3:
            p = [319,670]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],41,39)))
            dirty_rects.append(screen.blit(ml_arrow, p))
        if s.game.mystic_lines.position >= 4:
            p = [360,667]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],47,47)))
            dirty_rects.append(screen.blit(circle, p))
            p = [259,292]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],51,50)))
            dirty_rects.append(screen.blit(mg_letter, p))
        if s.game.mystic_lines.position == 5:
            p = [414,669]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],41,39)))
            dirty_rects.append(screen.blit(ml_arrow, p))
        if s.game.mystic_lines.position >= 6:
            p = [459,667]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],47,47)))
            dirty_rects.append(screen.blit(circle, p))
            p = [410,293]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],51,50)))
            dirty_rects.append(screen.blit(mg_letter, p))
    
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
            p = [217,669]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],41,39)))
            dirty_rects.append(screen.blit(ml_arrow, p))
        if s.game.mystic_lines.position >= 2:
            p = [265,667]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],47,47)))
            dirty_rects.append(screen.blit(circle, p))
            p = [331,291]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],51,50)))
            dirty_rects.append(screen.blit(mg_letter, p))
        if s.game.mystic_lines.position == 3:
            p = [319,670]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],41,39)))
            dirty_rects.append(screen.blit(ml_arrow, p))
        if s.game.mystic_lines.position >= 4:
            p = [360,667]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],47,47)))
            dirty_rects.append(screen.blit(circle, p))
            p = [259,292]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],51,50)))
            dirty_rects.append(screen.blit(mg_letter, p))
        if s.game.mystic_lines.position == 5:
            p = [414,669]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],41,39)))
            dirty_rects.append(screen.blit(ml_arrow, p))
        if s.game.mystic_lines.position >= 6:
            p = [459,667]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],47,47)))
            dirty_rects.append(screen.blit(circle, p))
            p = [410,293]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],51,50)))
            dirty_rects.append(screen.blit(mg_letter, p))
   
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
            dirty_rects.append(screen.blit(bg_gi, (233,369), pygame.Rect(233,369,270,212)))
        else:
            dirty_rects.append(screen.blit(bg_gi, (233,369), pygame.Rect(233,369,270,212)))

        if s.game.mystic_lines.position == 1:
            p = [217,669]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],41,39)))
            dirty_rects.append(screen.blit(ml_arrow, p))
        if s.game.mystic_lines.position >= 2:
            p = [265,667]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],47,47)))
            dirty_rects.append(screen.blit(circle, p))
            p = [331,291]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],51,50)))
            dirty_rects.append(screen.blit(mg_letter, p))
        if s.game.mystic_lines.position == 3:
            p = [319,670]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],41,39)))
            dirty_rects.append(screen.blit(ml_arrow, p))
        if s.game.mystic_lines.position >= 4:
            p = [360,667]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],47,47)))
            dirty_rects.append(screen.blit(circle, p))
            p = [259,292]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],51,50)))
            dirty_rects.append(screen.blit(mg_letter, p))
        if s.game.mystic_lines.position == 5:
            p = [414,669]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],41,39)))
            dirty_rects.append(screen.blit(ml_arrow, p))
        if s.game.mystic_lines.position >= 6:
            p = [459,667]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],47,47)))
            dirty_rects.append(screen.blit(circle, p))
            p = [410,293]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],51,50)))
            dirty_rects.append(screen.blit(mg_letter, p))
   
    pygame.display.update(dirty_rects)


def clear_odds(s, num):
    global screen

    dirty_rects = []

    dirty_rects.append(screen.blit(bg_gi, (182,762), pygame.Rect(182,762,47,47)))
    dirty_rects.append(screen.blit(bg_gi, (236,761), pygame.Rect(236,761,47,47)))
    dirty_rects.append(screen.blit(bg_gi, (293,762), pygame.Rect(293,762,47,47)))
    dirty_rects.append(screen.blit(bg_gi, (348,761), pygame.Rect(348,761,47,47)))
    dirty_rects.append(screen.blit(bg_gi, (402,760), pygame.Rect(402,760,47,47)))
    dirty_rects.append(screen.blit(bg_gi, (458,762), pygame.Rect(458,762,47,47)))
    dirty_rects.append(screen.blit(bg_gi, (512,760), pygame.Rect(512,760,47,47)))
    dirty_rects.append(screen.blit(bg_gi, (566,760), pygame.Rect(566,760,47,47)))

    pygame.display.update(dirty_rects)

def draw_odds_animation(s, num):
    global screen
    dirty_rects = []

    if num in [1,36,38,26,11,13]:
        p = [182,762]
        dirty_rects.append(screen.blit(number, p))
        pygame.display.update(dirty_rects)
    if num in [10,39,35,14]:
        p = [236,761]
        dirty_rects.append(screen.blit(number, p))
        pygame.display.update(dirty_rects)
    if num in [44,19]:
        p = [293,762]
        dirty_rects.append(screen.blit(number, p))
        pygame.display.update(dirty_rects)
    if num in [17,42]:
        p = [348,761]
        dirty_rects.append(screen.blit(number, p))
        pygame.display.update(dirty_rects)
    if num in [1,36,38,26,11,13]:
        p = [402,760]
        dirty_rects.append(screen.blit(number, p))
        pygame.display.update(dirty_rects)
    if num in [10,39,35,14]:
        p = [458,762]
        dirty_rects.append(screen.blit(number, p))
        pygame.display.update(dirty_rects)
    if num in [44,19]:
        p = [512,760]
        dirty_rects.append(screen.blit(number, p))
        pygame.display.update(dirty_rects)
    if num in [17,42]:
        p = [566,760]
        dirty_rects.append(screen.blit(number, p))
        pygame.display.update(dirty_rects)

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

    if s.game.selection_feature.position not in [4,5]:
        dirty_rects.append(screen.blit(bg_gi, (551,446), pygame.Rect(551,446,145,55)))
    if s.game.selection_feature.position < 6:
        dirty_rects.append(screen.blit(bg_gi, (551,351), pygame.Rect(551,351,145,55)))
    if s.game.mystic_lines.position < 2:
        dirty_rects.append(screen.blit(bg_gi, (265,667), pygame.Rect(265,667,47,47)))
        dirty_rects.append(screen.blit(bg_gi, (331,291), pygame.Rect(331,291,51,50)))
    if s.game.mystic_lines.position < 4:
        dirty_rects.append(screen.blit(bg_gi, (360,667), pygame.Rect(360,667,47,47)))
        dirty_rects.append(screen.blit(bg_gi, (259,292), pygame.Rect(259,292,51,50)))
    if s.game.mystic_lines.position < 6:
        dirty_rects.append(screen.blit(bg_gi, (459,667), pygame.Rect(459,667,47,47)))
        dirty_rects.append(screen.blit(bg_gi, (410,293), pygame.Rect(410,293,51,50)))
    if s.game.three_stars.status == False:
        dirty_rects.append(screen.blit(bg_gi, (21,445), pygame.Rect(21,445,149,54)))
    if s.game.six_stars.status == False:
        dirty_rects.append(screen.blit(bg_gi, (21,350), pygame.Rect(21,350,149,54)))
    if s.game.double_red.status == False: 
        dirty_rects.append(screen.blit(bg_gi, (617,809), pygame.Rect(617,809,88,49)))
    if s.game.double_yellow.status == False: 
        dirty_rects.append(screen.blit(bg_gi, (615,938), pygame.Rect(615,938,88,49)))
    if s.game.double_green.status == False: 
        dirty_rects.append(screen.blit(bg_gi, (615,873), pygame.Rect(615,873,88,49)))
    if s.game.double_blue.status == False: 
        dirty_rects.append(screen.blit(bg_gi, (615,1001), pygame.Rect(615,1001,88,49)))
    if s.game.gate.status == False: 
        dirty_rects.append(screen.blit(bg_gi, (21,563), pygame.Rect(21,563,152,57)))

    pygame.display.update(dirty_rects)


def draw_feature_animation(s, num):
    global screen
    dirty_rects = []
    if num in [19,30,5,44]:
        if s.game.selection_feature.position not in [4,5]:
            p = [551,446]
            dirty_rects.append(screen.blit(time, p))
            pygame.display.update(dirty_rects)
    if num in [10,39,35,14]:
        if s.game.selection_feature.position < 6:
            p = [551,351]
            dirty_rects.append(screen.blit(time, p))
            pygame.display.update(dirty_rects)
    if num in [7,16,32,41]:
        if s.game.mystic_lines.position < 2:
            p = [265,667]
            dirty_rects.append(screen.blit(circle, p))
            p = [331,291]
            dirty_rects.append(screen.blit(mg_letter, p))
            pygame.display.update(dirty_rects)
    if num in [11,32,36,7]:
        if s.game.mystic_lines.position < 4:
            p = [360,667]
            dirty_rects.append(screen.blit(circle, p))
            p = [259,292]
            dirty_rects.append(screen.blit(mg_letter, p))
            pygame.display.update(dirty_rects)
    if num in [1,36,38,26,11,13]:
        if s.game.mystic_lines.position < 6:
            p = [459,667]
            dirty_rects.append(screen.blit(circle, p))
            p = [410,293]
            dirty_rects.append(screen.blit(mg_letter, p))
            pygame.display.update(dirty_rects)
    if num in [14,18,39,43]:
        if s.game.three_stars.status == False:
            p = [21,445]
            dirty_rects.append(screen.blit(stars, p))
            pygame.display.update(dirty_rects)
    if num in [44,19]:
        if s.game.six_stars.status == False:
            p = [21,350]
            dirty_rects.append(screen.blit(stars, p))
            pygame.display.update(dirty_rects)
    if num in [1,26]:
        if s.game.double_red.status == False: 
            p = [617,809]
            dirty_rects.append(screen.blit(double, p))
            pygame.display.update(dirty_rects)
    if num in [15,40]:
        if s.game.double_yellow.status == False: 
            p = [615,938]
            dirty_rects.append(screen.blit(double, p))
            pygame.display.update(dirty_rects)
    if num in [16,41]:
        if s.game.double_green.status == False: 
            p = [615,873]
            dirty_rects.append(screen.blit(double, p))
            pygame.display.update(dirty_rects)
    if num in [17,42]:
        if s.game.double_blue.status == False: 
            p = [615,1001]
            dirty_rects.append(screen.blit(double, p))
            pygame.display.update(dirty_rects)
    if num in [14,18,39,43]:
        if s.game.gate.status == False: 
            p = [21,563]
            dirty_rects.append(screen.blit(gate, p))
            pygame.display.update(dirty_rects)

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

