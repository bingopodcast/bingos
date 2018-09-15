
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
bg_menu = pygame.image.load('tahiti_2/assets/tahiti_2_menu.png').convert_alpha()
bg_gi = pygame.image.load('tahiti_2/assets/tahiti_2_gi.png').convert_alpha()
bg_off = pygame.image.load('tahiti_2/assets/tahiti_2_off.png').convert_alpha()

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

        t = 3
        if s.game.selection_feature.position in [4,5]:
            t = 4
        if s.game.selection_feature.position == 6:
            t = 5
        if s.game.ball_count.position == t:
            s.cancel_delayed(name="blink_return")
            blink_return([s,1,1])
        else:
            s.cancel_delayed("blink_return")

    if s.game.ball_return_played.status == True:
        s.cancel_delayed("blink_return")
        p = [22,687]
        screen.blit(return_ind, p)

    if s.game.tilt.status == True:
        tilt_position = [508,603]
        screen.blit(tilt, tilt_position)

    pygame.display.update()

def blink_return(args):
    dirty_rects = []
    s = args[0]
    b = args[1]
    sn = args[2]

    if b == 0:
        if sn == 1:
            p = [22,650]
            dirty_rects.append(screen.blit(return_ind, p))
        pygame.display.update(dirty_rects)
    else:
        dirty_rects.append(screen.blit(bg_gi, (22,650), pygame.Rect(22,650,141,36)))
        pygame.display.update(dirty_rects)
    b = not b

    args = [s,b,sn]

    s.delay(name="blink_return", delay=0.1, handler=blink_return, param=args)

def blink(args):
    dirty_rects = []
    s = args[0]
    b = args[1]
    sn = args[2]

    if b == 0:
        if sn == 1:
            p = [497,660]
            dirty_rects.append(screen.blit(select_now, p))
        pygame.display.update(dirty_rects)
    else:
        dirty_rects.append(screen.blit(bg_gi, (497,660), pygame.Rect(497,660,85,71)))
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
            p = [276,685]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],20,20)))
            dirty_rects.append(screen.blit(ml_arrow, p))
        if s.game.mystic_lines.position >= 2:
            p = [321,679]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],35,35)))
            dirty_rects.append(screen.blit(circle, p))
            p = [344,283]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],40,39)))
            dirty_rects.append(screen.blit(ml_letter, p))
        if s.game.mystic_lines.position == 3:
            p = [379,685]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],20,20)))
            dirty_rects.append(screen.blit(ml_arrow, p))
        if s.game.mystic_lines.position >= 4:
            if s.game.bc.status == False:
                p = [423,633]
                dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],35,35)))
                dirty_rects.append(screen.blit(circle, p))
                p = [260,283]
                dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],40,39)))
                dirty_rects.append(screen.blit(ml_letter, p))
            else:
                p = [424,723]
                dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],35,35)))
                dirty_rects.append(screen.blit(circle, p))
                p = [425,282]
                dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],40,39)))
                dirty_rects.append(screen.blit(ml_letter, p))
        if s.game.mystic_lines.position == 5:
            p = [432,679]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],19,25)))
            dirty_rects.append(screen.blit(diamond, p))
        if s.game.mystic_lines.position >= 6:
            if s.game.bc.status == False:
                p = [424,723]
                dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],35,35)))
                dirty_rects.append(screen.blit(circle, p))
                p = [425,282]
                dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],40,39)))
                dirty_rects.append(screen.blit(ml_letter, p))
            else:
                p = [423,633]
                dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],35,35)))
                dirty_rects.append(screen.blit(circle, p))
                p = [260,283]
                dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],40,39)))
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
            dirty_rects.append(screen.blit(bg_gi, (228,369), pygame.Rect(228,369,275,212)))
        else:
            dirty_rects.append(screen.blit(bg_off, (228,369), pygame.Rect(228,369,275,212)))

        if s.game.mystic_lines.position == 1:
            p = [276,685]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],20,20)))
            dirty_rects.append(screen.blit(ml_arrow, p))
        if s.game.mystic_lines.position >= 2:
            p = [321,679]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],35,35)))
            dirty_rects.append(screen.blit(circle, p))
            p = [344,283]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],40,39)))
            dirty_rects.append(screen.blit(ml_letter, p))
        if s.game.mystic_lines.position == 3:
            p = [379,685]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],20,20)))
            dirty_rects.append(screen.blit(ml_arrow, p))
        if s.game.mystic_lines.position >= 4:
            if s.game.bc.status == False:
                p = [423,633]
                dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],35,35)))
                dirty_rects.append(screen.blit(circle, p))
                p = [260,283]
                dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],40,39)))
                dirty_rects.append(screen.blit(ml_letter, p))
            else:
                p = [424,723]
                dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],35,35)))
                dirty_rects.append(screen.blit(circle, p))
                p = [425,282]
                dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],40,39)))
                dirty_rects.append(screen.blit(ml_letter, p))
        if s.game.mystic_lines.position == 5:
            p = [432,679]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],19,25)))
            dirty_rects.append(screen.blit(diamond, p))
        if s.game.mystic_lines.position >= 6:
            if s.game.bc.status == False:
                p = [424,723]
                dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],35,35)))
                dirty_rects.append(screen.blit(circle, p))
                p = [425,282]
                dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],40,39)))
                dirty_rects.append(screen.blit(ml_letter, p))
            else:
                p = [423,633]
                dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],35,35)))
                dirty_rects.append(screen.blit(circle, p))
                p = [260,283]
                dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],40,39)))
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
            dirty_rects.append(screen.blit(bg_gi, (228,369), pygame.Rect(228,369,275,212)))
        else:
            dirty_rects.append(screen.blit(bg_off, (228,369), pygame.Rect(228,369,275,212)))

        if s.game.mystic_lines.position == 1:
            p = [276,685]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],20,20)))
            dirty_rects.append(screen.blit(ml_arrow, p))
        if s.game.mystic_lines.position >= 2:
            p = [321,679]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],35,35)))
            dirty_rects.append(screen.blit(circle, p))
            p = [344,283]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],40,39)))
            dirty_rects.append(screen.blit(ml_letter, p))
        if s.game.mystic_lines.position == 3:
            p = [379,685]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],20,20)))
            dirty_rects.append(screen.blit(ml_arrow, p))
        if s.game.mystic_lines.position >= 4:
            if s.game.bc.status == False:
                p = [423,633]
                dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],35,35)))
                dirty_rects.append(screen.blit(circle, p))
                p = [260,283]
                dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],40,39)))
                dirty_rects.append(screen.blit(ml_letter, p))
            else:
                p = [424,723]
                dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],35,35)))
                dirty_rects.append(screen.blit(circle, p))
                p = [425,282]
                dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],40,39)))
                dirty_rects.append(screen.blit(ml_letter, p))
        if s.game.mystic_lines.position == 5:
            p = [432,679]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],19,25)))
            dirty_rects.append(screen.blit(diamond, p))
        if s.game.mystic_lines.position >= 6:
            if s.game.bc.status == False:
                p = [424,723]
                dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],35,35)))
                dirty_rects.append(screen.blit(circle, p))
                p = [425,282]
                dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],40,39)))
                dirty_rects.append(screen.blit(ml_letter, p))
            else:
                p = [423,633]
                dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],35,35)))
                dirty_rects.append(screen.blit(circle, p))
                p = [260,283]
                dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],40,39)))
                dirty_rects.append(screen.blit(ml_letter, p))

    pygame.display.update(dirty_rects)


def clear_odds(s, num):
    global screen

    dirty_rects = []

    dirty_rects.append(screen.blit(bg_gi, (189,774), pygame.Rect(189,774,20,20)))
    dirty_rects.append(screen.blit(bg_gi, (249,773), pygame.Rect(249,773,20,20)))
    dirty_rects.append(screen.blit(bg_gi, (307,771), pygame.Rect(307,771,20,20)))
    dirty_rects.append(screen.blit(bg_gi, (360,773), pygame.Rect(360,773,20,20)))
    dirty_rects.append(screen.blit(bg_gi, (417,772), pygame.Rect(417,772,20,20)))
    dirty_rects.append(screen.blit(bg_gi, (473,771), pygame.Rect(473,771,20,20)))
    dirty_rects.append(screen.blit(bg_gi, (531,772), pygame.Rect(531,772,20,20)))
    dirty_rects.append(screen.blit(bg_gi, (586,771), pygame.Rect(586,771,20,20)))

    pygame.display.update(dirty_rects)

def draw_odds_animation(s, num):
    global screen
    dirty_rects = []

    if num in [1,36,38,26,11,13]:
        p = [189,774]
        dirty_rects.append(screen.blit(ml_arrow, p))
        pygame.display.update(dirty_rects)
    if num in [10,39,35,14]:
        p = [249,773]
        dirty_rects.append(screen.blit(ml_arrow, p))
        pygame.display.update(dirty_rects)
    if num in [44,19]:
        p = [307,771]
        dirty_rects.append(screen.blit(ml_arrow, p))
        pygame.display.update(dirty_rects)
    if num in [17,42]:
        p = [360,773]
        dirty_rects.append(screen.blit(ml_arrow, p))
        pygame.display.update(dirty_rects)
    if num in [1,36,38,26,11,13]:
        p = [417,772]
        dirty_rects.append(screen.blit(ml_arrow, p))
        pygame.display.update(dirty_rects)
    if num in [10,39,35,14]:
        p = [473,771]
        dirty_rects.append(screen.blit(ml_arrow, p))
        pygame.display.update(dirty_rects)
    if num in [44,19]:
        p = [531,772]
        dirty_rects.append(screen.blit(ml_arrow, p))
        pygame.display.update(dirty_rects)
    if num in [17,42]:
        p = [586,771]
        dirty_rects.append(screen.blit(ml_arrow, p))
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
        dirty_rects.append(screen.blit(bg_gi, (564,435), pygame.Rect(564,435,143,52)))
    if s.game.selection_feature.position < 6:
        dirty_rects.append(screen.blit(bg_gi, (564,336), pygame.Rect(564,336,143,52)))
    if s.game.mystic_lines.position < 2:
        dirty_rects.append(screen.blit(bg_gi, (321,679), pygame.Rect(321,679,35,35)))
        dirty_rects.append(screen.blit(bg_gi, (344,283), pygame.Rect(344,283,40,39)))
    if s.game.mystic_lines.position < 4:
        if s.game.bc.status == False:
            dirty_rects.append(screen.blit(bg_gi, (423,633), pygame.Rect(423,633,35,35)))
            dirty_rects.append(screen.blit(bg_gi, (260,283), pygame.Rect(260,283,40,39)))
        else:
            dirty_rects.append(screen.blit(bg_gi, (424,723), pygame.Rect(424,723,35,35)))
            dirty_rects.append(screen.blit(bg_gi, (425,282), pygame.Rect(425,282,40,39)))
    if s.game.mystic_lines.position < 6:
        if s.game.bc.status == False:
            dirty_rects.append(screen.blit(bg_gi, (424,723), pygame.Rect(424,723,35,35)))
            dirty_rects.append(screen.blit(bg_gi, (425,282), pygame.Rect(425,282,40,39)))
        else:
            dirty_rects.append(screen.blit(bg_gi, (423,633), pygame.Rect(423,633,35,35)))
            dirty_rects.append(screen.blit(bg_gi, (260,283), pygame.Rect(260,283,40,39)))
    if s.game.three_stars.status == False:
        dirty_rects.append(screen.blit(bg_gi, (23,435), pygame.Rect(23,435,143,48)))
    if s.game.six_stars.status == False:
        dirty_rects.append(screen.blit(bg_gi, (23,337), pygame.Rect(23,337,143,48)))
    if s.game.double_red.status == False: 
        dirty_rects.append(screen.blit(bg_gi, (628,811), pygame.Rect(628,811,88,49)))
    if s.game.double_yellow.status == False: 
        dirty_rects.append(screen.blit(bg_gi, (628,942), pygame.Rect(628,942,88,49)))
    if s.game.double_green.status == False: 
        dirty_rects.append(screen.blit(bg_gi, (628,878), pygame.Rect(628,878,88,49)))
    if s.game.double_blue.status == False: 
        dirty_rects.append(screen.blit(bg_gi, (628,1009), pygame.Rect(628,1009,88,49)))
    if s.game.b_return.status == False: 
        dirty_rects.append(screen.blit(bg_gi, (24,566), pygame.Rect(24,566,71,83)))
        dirty_rects.append(screen.blit(bg_gi, (93,566), pygame.Rect(93,566,71,83)))

    pygame.display.update(dirty_rects)


def draw_feature_animation(s, num):
    global screen
    dirty_rects = []
    if num in [19,30,5,44]:
        if s.game.selection_feature.position not in [4,5]:
            p = [564,435]
            dirty_rects.append(screen.blit(time, p))
            pygame.display.update(dirty_rects)
    if num in [10,39,35,14]:
        if s.game.selection_feature.position < 6:
            p = [564,336]
            dirty_rects.append(screen.blit(time, p))
            pygame.display.update(dirty_rects)
    if num in [7,16,32,41]:
        if s.game.mystic_lines.position < 2:
            p = [321,679]
            dirty_rects.append(screen.blit(circle, p))
            p = [344,283]
            dirty_rects.append(screen.blit(ml_letter, p))
            pygame.display.update(dirty_rects)
    if num in [11,32,36,7]:
        if s.game.mystic_lines.position < 4:
            if s.game.bc.status == False:
                p = [423,633]
                dirty_rects.append(screen.blit(circle, p))
                p = [260,283]
                dirty_rects.append(screen.blit(ml_letter, p))
            else:
                p = [424,723]
                dirty_rects.append(screen.blit(circle, p))
                p = [425,282]
                dirty_rects.append(screen.blit(ml_letter, p))
            pygame.display.update(dirty_rects)
    if num in [1,36,38,26,11,13]:
        if s.game.mystic_lines.position < 6:
            if s.game.bc.status == False:
                p = [424,723]
                dirty_rects.append(screen.blit(circle, p))
                p = [425,282]
                dirty_rects.append(screen.blit(ml_letter, p))
            else:
                p = [423,633]
                dirty_rects.append(screen.blit(circle, p))
                p = [260,283]
                dirty_rects.append(screen.blit(ml_letter, p))
            pygame.display.update(dirty_rects)
    if num in [14,18,39,43]:
        if s.game.three_stars.status == False:
            p = [23,435]
            dirty_rects.append(screen.blit(stars, p))
            pygame.display.update(dirty_rects)
    if num in [44,19]:
        if s.game.six_stars.status == False:
            p = [23,337]
            dirty_rects.append(screen.blit(stars, p))
            pygame.display.update(dirty_rects)
    if num in [1,26]:
        if s.game.double_red.status == False: 
            p = [628,811]
            dirty_rects.append(screen.blit(double, p))
            pygame.display.update(dirty_rects)
    if num in [15,40]:
        if s.game.double_yellow.status == False: 
            p = [628,942]
            dirty_rects.append(screen.blit(double, p))
            pygame.display.update(dirty_rects)
    if num in [16,41]:
        if s.game.double_green.status == False: 
            p = [628,878]
            dirty_rects.append(screen.blit(double, p))
            pygame.display.update(dirty_rects)
    if num in [17,42]:
        if s.game.double_blue.status == False: 
            p = [628,1009]
            dirty_rects.append(screen.blit(double, p))
            pygame.display.update(dirty_rects)
    if num in [14,18,39,43]:
        if s.game.b_return.status == False: 
            p = [24,566]
            dirty_rects.append(screen.blit(return_letter, p))
            p = [93,566]
            dirty_rects.append(screen.blit(return_letter, p))
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

