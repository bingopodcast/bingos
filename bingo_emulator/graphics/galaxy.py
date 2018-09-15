
import pygame
import random

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

meter = pygame.image.load('graphics/assets/black_register_cover.png').convert()
odds = pygame.image.load('galaxy/assets/odds.png').convert_alpha()
time = pygame.image.load('galaxy/assets/time.png').convert_alpha()
select_now = pygame.image.load('galaxy/assets/select_now.png').convert_alpha()
tilt = pygame.image.load('galaxy/assets/tilt.png').convert_alpha()
number_card = pygame.image.load('galaxy/assets/screen.png').convert_alpha()
number = pygame.image.load('galaxy/assets/number.png').convert_alpha()
columnb = pygame.image.load('galaxy/assets/columnb.png').convert_alpha()
columnb2 = pygame.image.load('galaxy/assets/columnb2.png').convert_alpha()
columnb3 = pygame.image.load('galaxy/assets/columnb3.png').convert_alpha()
columnbleft = pygame.image.load('galaxy/assets/columnbleft.png').convert_alpha()
columnbright = pygame.image.load('galaxy/assets/columnbright.png').convert_alpha()
columna = pygame.image.load('galaxy/assets/columna.png').convert_alpha()
columna2 = pygame.image.load('galaxy/assets/columna2.png').convert_alpha()
columna3 = pygame.image.load('galaxy/assets/columna3.png').convert_alpha()
columnaleft = pygame.image.load('galaxy/assets/columnaleft.png').convert_alpha()
columnaright = pygame.image.load('galaxy/assets/columnaright.png').convert_alpha()
columnc = pygame.image.load('galaxy/assets/columnc.png').convert_alpha()
columnc2 = pygame.image.load('galaxy/assets/columnc2.png').convert_alpha()
columnc3 = pygame.image.load('galaxy/assets/columnc3.png').convert_alpha()
columncleft = pygame.image.load('galaxy/assets/columncleft.png').convert_alpha()
columncright = pygame.image.load('galaxy/assets/columncright.png').convert_alpha()
return_letter = pygame.image.load('galaxy/assets/return_letter.png').convert_alpha()
diagonal_score = pygame.image.load('galaxy/assets/diagonals.png').convert_alpha()
eb = pygame.image.load('galaxy/assets/eb.png').convert_alpha()
eb_number = pygame.image.load('galaxy/assets/eb_number.png').convert_alpha()
extra_balls = pygame.image.load('galaxy/assets/extra_balls.png').convert_alpha()
feature_played = pygame.image.load('galaxy/assets/feature_played.png').convert_alpha()
ml_letter = pygame.image.load('galaxy/assets/letter.png').convert_alpha()
ml_arrow = pygame.image.load('galaxy/assets/line_arrow.png').convert_alpha()
button = pygame.image.load('galaxy/assets/pap.png').convert_alpha()
return_select_now = pygame.image.load('galaxy/assets/return_select_now.png').convert_alpha()
sf_arrow = pygame.image.load('galaxy/assets/sf_arrow.png').convert_alpha()
bg_menu = pygame.image.load('galaxy/assets/galaxy_menu.png').convert_alpha()
bg_gi = pygame.image.load('galaxy/assets/galaxy_gi.png').convert_alpha()
bg_off = pygame.image.load('galaxy/assets/galaxy_off.png').convert_alpha()

class scorereel():
    """ Score Reels are used to count replays """
    def __init__(self, pos, image):
        self.position = pos
        self.default_y = self.position[1]
        self.image = pygame.image.load(image).convert()

reel1 = scorereel([110,802], "graphics/assets/white_reel.png")
reel10 = scorereel([91,802], "graphics/assets/white_reel.png")
reel100 = scorereel([72,802], "graphics/assets/white_reel.png")
reel1000 = scorereel([53,802], "graphics/assets/white_reel.png")

def display(s, replays=0, menu=False):
    
    meter.set_colorkey((255,0,252))
    meter_position = [44,802]

    screen.blit(reel1.image, reel1.position)
    screen.blit(reel10.image, reel10.position)
    screen.blit(reel100.image, reel100.position)
    screen.blit(reel1000.image, reel1000.position)
    screen.blit(meter, meter_position)

    if s.game.line1.position in [0,2]:
        p = [218,315]
        screen.blit(columna, p)
    elif s.game.line1.position == 1:
        p = [218,315]
        screen.blit(columna2, p)
    else:
        p = [218,315]
        screen.blit(columna3, p)

    if s.game.line2.position in [0,2]:
        p = [311,315]
        screen.blit(columnb, p)
    elif s.game.line2.position == 1:
        p = [311,315]
        screen.blit(columnb2, p)
    else:
        p = [311,315]
        screen.blit(columnb3, p)

    if s.game.line3.position in [0,2]:
        p = [407,315]
        screen.blit(columnc, p)
    elif s.game.line3.position == 1:
        p = [407,315]
        screen.blit(columnc2, p)
    else:
        p = [407,315]
        screen.blit(columnc3, p)


    nc_p = [204,353]
    screen.blit(number_card, nc_p)

    backglass_position = [0, 0]
    backglass = pygame.Surface(screen.get_size(), flags=pygame.SRCALPHA)
    backglass.fill((0, 0, 0))
    if menu == True:
        backglass = pygame.image.load('galaxy/assets/galaxy_menu.png').convert_alpha()
    else:
        if (s.game.anti_cheat.status == True):
            backglass = pygame.image.load('galaxy/assets/galaxy_gi.png').convert_alpha()
        else:
            backglass = pygame.image.load('galaxy/assets/galaxy_off.png').convert_alpha()
    backglass = pygame.transform.scale(backglass, (720, 1280))
    
    screen.blit(backglass, backglass_position)

    if s.game.mystic_lines.position >= 2:
        if s.game.selection_feature.position in [1,2]:
            bfp = [584,581]
            screen.blit(time, bfp)
        elif s.game.selection_feature.position in [3,4]:
            bfp = [584,468]
            screen.blit(time, bfp)
        elif s.game.selection_feature.position == 5:
            bfp = [584,354]
            screen.blit(time, bfp)
        if s.game.selection_feature.position == 2:
            p = [618,536]
            screen.blit(sf_arrow, p)
        if s.game.selection_feature.position == 4:
            p = [618,427]
            screen.blit(sf_arrow, p)

    if s.game.mystic_lines.position >= 2:
        p = [237,605]
        screen.blit(ml_letter, p)
    if s.game.mystic_lines.position == 3:
        p = [293,613]
        screen.blit(ml_arrow, p)
    if s.game.mystic_lines.position >= 4:
        p = [335,605]
        screen.blit(ml_letter, p)
    if s.game.mystic_lines.position == 5:
        p = [393,613]
        screen.blit(ml_arrow, p)
    if s.game.mystic_lines.position == 6:
        p = [437,605]
        screen.blit(ml_letter, p)

    if s.game.mystic_lines.position >= 2:
        t = 3
        if s.game.selection_feature.position in [3,4,5]:
            t = 4
        if s.game.selection_feature.position == 6:
            t = 5
        if s.game.ball_count.position == t:
            s.cancel_delayed(name="blink")
            blink([s,1,1])
        else:
            s.cancel_delayed(name="blink")

    if s.game.b_return.status == True:
        t = 3
        if s.game.selection_feature.position in [3,4,5]:
            t = 4
        if s.game.selection_feature.position == 6:
            t = 5
        if s.game.ball_count.position == t:
            s.cancel_delayed(name="blink_return")
            blink_return([s,1,1])
        else:
            s.cancel_delayed(name="blink_return")


    if s.game.tilt.status == False:
        if s.holes:
            if 1 in s.holes:
                if s.game.line3.position in [0,2]:
                    p = [459,461]
                    screen.blit(number, p)
                elif s.game.line3.position == 1:
                    p = [459,508]
                    screen.blit(number, p)
                else:
                    p = [459,412]
                    screen.blit(number, p)
            if 2 in s.holes:
                if s.game.line1.position in [0,2]:
                    p = [220,509]
                    screen.blit(number, p)
                elif s.game.line1.position == 1:
                    p = [222,459]
                    screen.blit(number, p)
                else:
                    p = [269,509]
                    screen.blit(number, p)
            if 3 in s.holes:
                if s.game.line3.position in [0,2]:
                    p = [411,411]
                    screen.blit(number, p)
                elif s.game.line3.position == 1:
                    p = [412,363]
                    screen.blit(number, p)
                else:
                    p = [412,460]
                    screen.blit(number, p)
            if 4 in s.holes:
                if s.game.line3.position in [0,2]:
                    p = [460,363]
                    screen.blit(number, p)
                elif s.game.line3.position == 1:
                    p = [460,413]
                    screen.blit(number, p)
                else:
                    p = [412,363]
                    screen.blit(number, p)
            if 5 in s.holes:
                if s.game.line3.position in [0,2]:
                    p = [411,509]
                    screen.blit(number, p)
                elif s.game.line3.position == 1:
                    p = [412,460]
                    screen.blit(number, p)
                else:
                    p = [461,509]
                    screen.blit(number, p)
            if 6 in s.holes:
                if s.game.line2.position in [0,2]:
                    p = [365,362]
                    screen.blit(number, p)
                elif s.game.line2.position == 1:
                    p = [365,410]
                    screen.blit(number, p)
                else:
                    p = [317,361]
                    screen.blit(number, p)
            if 7 in s.holes:
                if s.game.line1.position in [0,2]:
                    p = [221,410]
                    screen.blit(number, p)
                elif s.game.line1.position == 1:
                    p = [221,360]
                    screen.blit(number, p)
                else:
                    p = [221,459]
                    screen.blit(number, p)
            if 8 in s.holes:
                if s.game.line1.position in [0,2]:
                    p = [269,360]
                    screen.blit(number, p)
                elif s.game.line1.position == 1:
                    p = [269,409]
                    screen.blit(number, p)
                else:
                    p = [220,360]
                    screen.blit(number, p)
            if 9 in s.holes:
                if s.game.line1.position in [0,2]:
                    p = [220,360]
                    screen.blit(number, p)
                elif s.game.line1.position == 1:
                    p = [269,360]
                    screen.blit(number, p)
                else:
                    p = [221,409]
                    screen.blit(number, p)
            if 10 in s.holes:
                if s.game.line3.position in [0,2]:
                    p = [460,412]
                    screen.blit(number, p)
                elif s.game.line3.position == 1:
                    p = [460,461]
                    screen.blit(number, p)
                else:
                    p = [460,363]
                    screen.blit(number, p)
            if 11 in s.holes:
                if s.game.line1.position in [0,2]:
                    p = [269,459]
                    screen.blit(number, p)
                elif s.game.line1.position == 1:
                    p = [269,509]
                    screen.blit(number, p)
                else:
                    p = [269,411]
                    screen.blit(number, p)
            if 12 in s.holes:
                if s.game.line2.position in [0,2]:
                    p = [317,411]
                    screen.blit(number, p)
                elif s.game.line2.position == 1:
                    p = [317,361]
                    screen.blit(number, p)
                else:
                    p = [317,461]
                    screen.blit(number, p)
            if 13 in s.holes:
                if s.game.line2.position in [0,2]:
                    p = [317,509]
                    screen.blit(number, p)
                elif s.game.line2.position == 1:
                    p = [317,460]
                    screen.blit(number, p)
                else:
                    p = [365,510]
                    screen.blit(number, p)
            if 14 in s.holes:
                if s.game.line2.position in [0,2]:
                    p = [365,411]
                    screen.blit(number, p)
                elif s.game.line2.position == 1:
                    p = [365,461]
                    screen.blit(number, p)
                else:
                    p = [365,362]
                    screen.blit(number, p)
            if 15 in s.holes:
                if s.game.line2.position in [0,2]:
                    p = [365,510]
                    screen.blit(number, p)
                elif s.game.line2.position == 1:
                    p = [317,509]
                    screen.blit(number, p)
                else:
                    p = [365,461]
                    screen.blit(number, p)
            if 16 in s.holes:
                if s.game.line1.position in [0,2]:
                    p = [222,459]
                    screen.blit(number, p)
                elif s.game.line1.position == 1:
                    p = [221,409]
                    screen.blit(number, p)
                else:
                    p = [221,509]
                    screen.blit(number, p)
            if 17 in s.holes:
                if s.game.line1.position in [0,2]:
                    p = [269,509]
                    screen.blit(number, p)
                elif s.game.line1.position == 1:
                    p = [220,509]
                    screen.blit(number, p)
                else:
                    p = [269,459]
                    screen.blit(number, p)
            if 18 in s.holes:
                if s.game.line3.position in [0,2]:
                    p = [412,363]
                    screen.blit(number, p)
                elif s.game.line3.position == 1:
                    p = [460,363]
                    screen.blit(number, p)
                else:
                    p = [413,410]
                    screen.blit(number, p)
            if 19 in s.holes:
                if s.game.line2.position in [0,2]:
                    p = [317,461]
                    screen.blit(number, p)
                elif s.game.line2.position == 1:
                    p = [317,411]
                    screen.blit(number, p)
                else:
                    p = [318,509]
                    screen.blit(number, p)
            if 20 in s.holes:
                if s.game.line1.position in [0,2]:
                    p = [270,411]
                    screen.blit(number, p)
                elif s.game.line1.position == 1:
                    p = [269,460]
                    screen.blit(number, p)
                else:
                    p = [270,361]
                    screen.blit(number, p)
            if 21 in s.holes:
                if s.game.line3.position in [0,2]:
                    p = [412,460]
                    screen.blit(number, p)
                elif s.game.line3.position == 1:
                    p = [411,411]
                    screen.blit(number, p)
                else:
                    p = [411,509]
                    screen.blit(number, p)
            if 22 in s.holes:
                if s.game.line2.position in [0,2]:
                    p = [317,361]
                    screen.blit(number, p)
                elif s.game.line2.position == 1:
                    p = [365,362]
                    screen.blit(number, p)
                else:
                    p = [317,410]
                    screen.blit(number, p)
            if 23 in s.holes:
                if s.game.line3.position in [0,2]:
                    p = [461,509]
                    screen.blit(number, p)
                elif s.game.line3.position == 1:
                    p = [411,509]
                    screen.blit(number, p)
                else:
                    p = [461,461]
                    screen.blit(number, p)
            if 24 in s.holes:
                if s.game.line2.position in [0,2]:
                    p = [364,461]
                    screen.blit(number, p)
                elif s.game.line2.position == 1:
                    p = [364,509]
                    screen.blit(number, p)
                else:
                    p = [365,410]
                    screen.blit(number, p)

    if s.game.red_odds.position == 1:
        o = [183,757]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 2:
        o = [243,757]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 3:
        o = [298,757]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 4:
        o = [350,757]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 5:
        o = [399,757]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 6:
        o = [445,757]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 7:
        o = [490,757]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 8:
        o = [535,757]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 9:
        o = [577,757]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 10:
        o = [621,757]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 11:
        o = [666,759]
        screen.blit(odds, o)

    if s.game.green_odds.position == 1:
        o = [183,827]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 2:
        o = [243,827]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 3:
        o = [298,827]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 4:
        o = [350,827]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 5:
        o = [399,827]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 6:
        o = [445,827]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 7:
        o = [490,827]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 8:
        o = [535,827]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 9:
        o = [577,827]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 10:
        o = [621,827]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 11:
        o = [667,829]
        screen.blit(odds, o)

    if s.game.yellow_odds.position == 1:
        o = [183,900]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 2:
        o = [243,900]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 3:
        o = [298,900]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 4:
        o = [350,900]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 5:
        o = [399,900]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 6:
        o = [445,900]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 7:
        o = [490,900]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 8:
        o = [535,900]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 9:
        o = [577,900]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 10:
        o = [621,901]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 11:
        o = [666,901]
        screen.blit(odds, o)

    if s.game.blue_odds.position == 1:
        o = [183,970]
        screen.blit(odds, o)
    elif s.game.blue_odds.position == 2:
        o = [243,970]
        screen.blit(odds, o)
    elif s.game.blue_odds.position == 3:
        o = [298,970]
        screen.blit(odds, o)
    elif s.game.blue_odds.position == 4:
        o = [350,970]
        screen.blit(odds, o)
    elif s.game.blue_odds.position == 5:
        o = [399,970]
        screen.blit(odds, o)
    elif s.game.blue_odds.position == 6:
        o = [445,970]
        screen.blit(odds, o)
    elif s.game.blue_odds.position == 7:
        o = [490,970]
        screen.blit(odds, o)
    elif s.game.blue_odds.position == 8:
        o = [535,970]
        screen.blit(odds, o)
    elif s.game.blue_odds.position == 9:
        o = [577,970]
        screen.blit(odds, o)
    elif s.game.blue_odds.position == 10:
        o = [623,971]
        screen.blit(odds, o)
    elif s.game.blue_odds.position == 11:
        o = [666,973]
        screen.blit(odds, o)


    if s.game.b_return.status == True:
        p = [15,403]
        screen.blit(return_letter, p)
        p = [83,403]
        screen.blit(return_letter, p)

    if s.game.ball_return_played.status == True:
        p = [33,529]
        screen.blit(feature_played, p)

    if s.game.diagonal_score.status == True:
        p = [16,574]
        screen.blit(diagonal_score, p)

    if s.game.eb_play.status == True:
        p = [43,1048]
        screen.blit(extra_balls, p)
    if s.game.extra_ball.position >= 1:
        p = [151,1047]
        screen.blit(eb_number, p)
    if s.game.extra_ball.position >= 2:
        p = [203,1047]
        screen.blit(eb, p)
    if s.game.extra_ball.position >= 3:
        p = [263,1047]
        screen.blit(eb, p)
    if s.game.extra_ball.position >= 4:
        p = [325,1046]
        screen.blit(eb_number, p)
    if s.game.extra_ball.position >= 5:
        p = [376,1046]
        screen.blit(eb, p)
    if s.game.extra_ball.position >= 6:
        p = [439,1047]
        screen.blit(eb, p)
    if s.game.extra_ball.position >= 7:
        p = [500,1046]
        screen.blit(eb_number, p)
    if s.game.extra_ball.position >= 8:
        p = [551,1046]
        screen.blit(eb, p)
    if s.game.extra_ball.position == 9:
        p = [613,1047]
        screen.blit(eb, p)

    if s.game.ball_count.position == 0:
        if s.game.all_advantages.status == True:
            p = [18,992]
            screen.blit(button, p)
        if s.game.odds_only.status == True:
            p = [19,912]
            screen.blit(button, p)
        if s.game.features.status == True:
            p = [18,951]
            screen.blit(button, p)

    if s.game.tilt.status == True:
        tilt_position = [627,224]
        screen.blit(tilt, tilt_position)

    pygame.display.update()

def blink(args):
    dirty_rects = []
    s = args[0]
    b = args[1]
    sn = args[2]

    if b == 0:
        if sn == 1:
            p = [299,702]
            dirty_rects.append(screen.blit(select_now, p))
        pygame.display.update(dirty_rects)
    else:
        dirty_rects.append(screen.blit(bg_gi, (299,702), pygame.Rect(299,702,125,33)))
        pygame.display.update(dirty_rects)
    b = not b

    args = [s,b,sn]

    s.delay(name="blink", delay=0.1, handler=blink, param=args)

def blink_return(args):
    dirty_rects = []
    s = args[0]
    b = args[1]
    sn = args[2]

    if b == 0:
        if sn == 1:
            p = [17,493]
            dirty_rects.append(screen.blit(return_select_now, p))
        pygame.display.update(dirty_rects)
    else:
        dirty_rects.append(screen.blit(bg_gi, (17,493), pygame.Rect(17,493,133,36)))
        pygame.display.update(dirty_rects)
    b = not b

    args = [s,b,sn]

    s.delay(name="blink_return", delay=0.1, handler=blink_return, param=args)

def line1_animation(args):
    dirty_rects = []
    s = args[0]
    num = args[1]
    line = args[2]

    if line == 1:
        if s.game.line1.position == 0:
            dirty_rects.append(screen.blit(columnaleft, (218, 369 + num)))
            dirty_rects.append(screen.blit(columnaright, (263, 262 - num)))
        elif s.game.line1.position == 1:
            dirty_rects.append(screen.blit(columnaleft, (218, 315 + num)))
            dirty_rects.append(screen.blit(columnaright, (263, 315 - num)))
        elif s.game.line1.position == 2:
            dirty_rects.append(screen.blit(columnaleft, (218, 262 - num)))
            dirty_rects.append(screen.blit(columnaright, (263, 369 + num)))
        elif s.game.line1.position == 3:
            dirty_rects.append(screen.blit(columnaleft, (218, 315 -  num)))
            dirty_rects.append(screen.blit(columnaright, (263, 315 + num)))

    nc_p = [204,353]
    dirty_rects.append(screen.blit(number_card, nc_p))
   
    if s.game.tilt.status == False:
        dirty_rects.append(screen.blit(bg_gi, (204,260), pygame.Rect(204,260,105,406)))
    else:
        dirty_rects.append(screen.blit(bg_off, (204,260), pygame.Rect(204,260,105,406)))
   
    if s.game.mystic_lines.position >= 2:
        p = [237,605]
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],49,50)))
        dirty_rects.append(screen.blit(ml_letter, p))
    if s.game.mystic_lines.position == 3:
        p = [293,613]
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],33,34)))
        dirty_rects.append(screen.blit(ml_arrow, p))
    if s.game.mystic_lines.position >= 4:
        p = [335,605]
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],49,50)))
        dirty_rects.append(screen.blit(ml_letter, p))
    if s.game.mystic_lines.position == 5:
        p = [393,613]
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],33,34)))
        dirty_rects.append(screen.blit(ml_arrow, p))
    if s.game.mystic_lines.position == 6:
        p = [437,605]
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],49,50)))
        dirty_rects.append(screen.blit(ml_letter, p))

    pygame.display.update(dirty_rects)

def line2_animation(args):
    dirty_rects = []
    s = args[0]
    num = args[1]
    line = args[2]

    if line == 2:
        if s.game.line2.position == 0:
            dirty_rects.append(screen.blit(columnbleft, (311, 369 + num)))
            dirty_rects.append(screen.blit(columnbright, (356, 262 - num)))
        elif s.game.line2.position == 1:
            dirty_rects.append(screen.blit(columnbleft, (311, 315 + num)))
            dirty_rects.append(screen.blit(columnbright, (356, 315 - num)))
        elif s.game.line2.position == 2:
            dirty_rects.append(screen.blit(columnbleft, (311, 262 - num)))
            dirty_rects.append(screen.blit(columnbright, (356, 369 + num)))
        elif s.game.line2.position == 3:
            dirty_rects.append(screen.blit(columnbleft, (311, 315 - num)))
            dirty_rects.append(screen.blit(columnbright, (356, 315 + num)))

    nc_p = [204,353]
    dirty_rects.append(screen.blit(number_card, nc_p))

    if s.game.tilt.status == False:
        dirty_rects.append(screen.blit(bg_gi, (311,260), pygame.Rect(311,260,105,406)))
    else:
        dirty_rects.append(screen.blit(bg_off, (311,260), pygame.Rect(311,260,105,406)))

    if s.game.mystic_lines.position >= 2:
        p = [237,605]
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],49,50)))
        dirty_rects.append(screen.blit(ml_letter, p))
    if s.game.mystic_lines.position == 3:
        p = [293,613]
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],33,34)))
        dirty_rects.append(screen.blit(ml_arrow, p))
    if s.game.mystic_lines.position >= 4:
        p = [335,605]
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],49,50)))
        dirty_rects.append(screen.blit(ml_letter, p))
    if s.game.mystic_lines.position == 5:
        p = [393,613]
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],33,34)))
        dirty_rects.append(screen.blit(ml_arrow, p))
    if s.game.mystic_lines.position == 6:
        p = [437,605]
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],49,50)))
        dirty_rects.append(screen.blit(ml_letter, p))


    pygame.display.update(dirty_rects)

def line3_animation(args):
    dirty_rects = []
    s = args[0]
    num = args[1]
    line = args[2]

    if line == 3:
        if s.game.line3.position == 0:
            dirty_rects.append(screen.blit(columncleft, (407, 369 + num)))
            dirty_rects.append(screen.blit(columncright, (452, 262 - num)))
        elif s.game.line3.position == 1:
            dirty_rects.append(screen.blit(columncleft, (407, 315 + num)))
            dirty_rects.append(screen.blit(columncright, (452, 315 - num)))
        elif s.game.line3.position == 2:
            dirty_rects.append(screen.blit(columncleft, (407, 262 - num)))
            dirty_rects.append(screen.blit(columncright, (452, 369 + num)))
        elif s.game.line3.position == 3:
            dirty_rects.append(screen.blit(columncleft, (407, 315 - num)))
            dirty_rects.append(screen.blit(columncright, (452, 315 + num)))
        
    nc_p = [204,353]
    dirty_rects.append(screen.blit(number_card, nc_p))

    if s.game.tilt.status == False:
        dirty_rects.append(screen.blit(bg_gi, (407,260), pygame.Rect(407,260,105,406)))
    else:
        dirty_rects.append(screen.blit(bg_off, (407,260), pygame.Rect(407,260,105,406)))
 
    if s.game.mystic_lines.position >= 2:
        p = [237,605]
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],49,50)))
        dirty_rects.append(screen.blit(ml_letter, p))
    if s.game.mystic_lines.position == 3:
        p = [293,613]
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],33,34)))
        dirty_rects.append(screen.blit(ml_arrow, p))
    if s.game.mystic_lines.position >= 4:
        p = [335,605]
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],49,50)))
        dirty_rects.append(screen.blit(ml_letter, p))
    if s.game.mystic_lines.position == 5:
        p = [393,613]
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],33,34)))
        dirty_rects.append(screen.blit(ml_arrow, p))
    if s.game.mystic_lines.position == 6:
        p = [437,605]
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],49,50)))
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
    if s.game.red_odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (399,757), pygame.Rect(399,757,39,67)))
    if s.game.red_odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (490,757), pygame.Rect(490,757,39,67)))
    if s.game.red_odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (535,757), pygame.Rect(535,757,39,67)))
    if s.game.red_odds.position != 9:
        dirty_rects.append(screen.blit(bg_gi, (577,757), pygame.Rect(577,757,39,67)))
    if s.game.red_odds.position != 10:
        dirty_rects.append(screen.blit(bg_gi, (621,757), pygame.Rect(621,757,39,67)))
    if s.game.red_odds.position != 11:
        dirty_rects.append(screen.blit(bg_gi, (666,757), pygame.Rect(666,757,39,67)))

    if s.game.yellow_odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (350,900), pygame.Rect(350,900,39,67)))
    if s.game.yellow_odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (445,900), pygame.Rect(445,900,39,67)))
    if s.game.yellow_odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (490,900), pygame.Rect(490,900,39,67)))
    if s.game.yellow_odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (535,900), pygame.Rect(535,900,39,67)))
    if s.game.yellow_odds.position != 10:
        dirty_rects.append(screen.blit(bg_gi, (621,901), pygame.Rect(621,901,39,67)))
    if s.game.yellow_odds.position != 11:
        dirty_rects.append(screen.blit(bg_gi, (666,901), pygame.Rect(666,901,39,67)))

    if s.game.green_odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (350,827), pygame.Rect(350,827,39,67)))
    if s.game.green_odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (445,827), pygame.Rect(445,827,39,67)))
    if s.game.green_odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (490,827), pygame.Rect(490,827,39,67)))
    if s.game.green_odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (535,827), pygame.Rect(535,827,39,67)))
    if s.game.green_odds.position != 9:
        dirty_rects.append(screen.blit(bg_gi, (577,827), pygame.Rect(577,827,39,67)))
    if s.game.green_odds.position != 11:
        dirty_rects.append(screen.blit(bg_gi, (667,829), pygame.Rect(667,829,39,67)))

    if s.game.blue_odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (399,970), pygame.Rect(399,970,46,61)))
    if s.game.blue_odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (445,970), pygame.Rect(445,970,46,61)))
    if s.game.blue_odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (535,970), pygame.Rect(535,970,46,61)))
    if s.game.blue_odds.position != 9:
        dirty_rects.append(screen.blit(bg_gi, (577,970), pygame.Rect(577,970,46,61)))
    if s.game.blue_odds.position != 10:
        dirty_rects.append(screen.blit(bg_gi, (623,971), pygame.Rect(623,971,46,61)))
    if s.game.blue_odds.position != 11:
        dirty_rects.append(screen.blit(bg_gi, (666,973), pygame.Rect(666,973,46,61)))

    pygame.display.update(dirty_rects)

def draw_odds_animation(s, num):
    global screen
    dirty_rects = []

    if num in [18,43]:
        if s.game.yellow_odds.position != 4:
            p = [350,900]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [6,31]:
        if s.game.yellow_odds.position != 6:
            p = [445,900]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [14,39]:
        if s.game.yellow_odds.position != 7:
            p = [490,900]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [23,48]:
        if s.game.yellow_odds.position != 8:
            p = [535,900]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [2,27]:
        if s.game.yellow_odds.position != 10:
            p = [621,901]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [20,45]:
        if s.game.yellow_odds.position != 11:
            p = [666,901]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return

    if num in [1,26]:
        if s.game.red_odds.position != 5:
            p = [399,757]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [19,44]:
        if s.game.red_odds.position != 7:
            p = [490,757]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [10,35]:
        if s.game.red_odds.position != 8:
            p = [535,757]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [16,41]:
        if s.game.red_odds.position != 9:
            p = [577,757]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [8,33]:
        if s.game.red_odds.position != 10:
            p = [621,757]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [13,38]:
        if s.game.red_odds.position != 11:
            p = [666,757]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return

    if num in [9,34]:
        if s.game.blue_odds.position != 5:
            p = [399,970]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [15,40]:
        if s.game.blue_odds.position != 6:
            p = [445,970]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [7,32]:
        if s.game.blue_odds.position != 8:
            p = [535,970]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [12,37]:
        if s.game.blue_odds.position != 9:
            p = [577,970]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [21,46]:
        if s.game.blue_odds.position != 10:
            p = [623,971]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [4,29]:
        if s.game.blue_odds.position != 11:
            p = [666,973]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return

    if num in [11,36]:
        if s.game.green_odds.position != 4:
            p = [350,827]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [3,28]:
        if s.game.green_odds.position != 6:
            p = [445,827]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [22,47]:
        if s.game.green_odds.position != 7:
            p = [490,827]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [5,30]:
        if s.game.green_odds.position != 8:
            p = [535,827]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [24,49]:
        if s.game.green_odds.position != 9:
            p = [577,827]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [17,42]:
        if s.game.green_odds.position != 11:
            p = [667,829]
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
    
    if s.game.selection_feature.position in [0,3,4,5,6]:
        dirty_rects.append(screen.blit(bg_gi, (584,581), pygame.Rect(584,581,113,55)))
    if s.game.selection_feature.position not in [3,4,5]:
        dirty_rects.append(screen.blit(bg_gi, (584,468), pygame.Rect(584,468,113,55)))
    if s.game.selection_feature.position < 6:
        dirty_rects.append(screen.blit(bg_gi, (584,354), pygame.Rect(584,354,113,55)))
    if s.game.mystic_lines.position < 2:
        dirty_rects.append(screen.blit(bg_gi, (237,605), pygame.Rect(237,605,49,50)))
    if s.game.mystic_lines.position < 4:
        dirty_rects.append(screen.blit(bg_gi, (335,605), pygame.Rect(335,605,49,50)))
    if s.game.mystic_lines.position < 6:
        dirty_rects.append(screen.blit(bg_gi, (437,605), pygame.Rect(437,605,49,50)))
    if s.game.b_return.status == False:
        dirty_rects.append(screen.blit(bg_gi, (15,403), pygame.Rect(15,403,65,90)))
        dirty_rects.append(screen.blit(bg_gi, (83,403), pygame.Rect(83,403,65,90)))
    if s.game.diagonal_score.status == False:
        dirty_rects.append(screen.blit(bg_gi, (16,574), pygame.Rect(16,574,129,79)))

    pygame.display.update(dirty_rects)


def draw_feature_animation(s, num):
    global screen
    dirty_rects = []

    if num in [8,14,24,33,39,49]:
        if s.game.selection_feature.position in [0,3,4,5,6]:
            p = [584,581]
            dirty_rects.append(screen.blit(time, p))
            pygame.display.update(dirty_rects)
            return
    if num in [7,9,18,32,34,43]:
        if s.game.selection_feature.position not in [2,3,4,5]:
            p = [584,468]
            dirty_rects.append(screen.blit(time, p))
            pygame.display.update(dirty_rects)
            return
    if num in [6,13,20,31,38,45]:
        if s.game.selection_feature.position < 6:
            p = [584,468]
            dirty_rects.append(screen.blit(time, p))
            pygame.display.update(dirty_rects)
            return
    if num in [5,12,21,30,37,46]:
        if s.game.mystic_lines.position < 2:
            p = [237,605]
            dirty_rects.append(screen.blit(ml_letter, p))
            pygame.display.update(dirty_rects)
            return
    if num in [4,11,16,29,36,41]:
        if s.game.mystic_lines.position < 4:
            p = [335,605]
            dirty_rects.append(screen.blit(ml_letter, p))
            pygame.display.update(dirty_rects)
            return
    if num in [3,17,23,28,42,48]:
        if s.game.mystic_lines.position < 6:
            p = [437,605]
            dirty_rects.append(screen.blit(ml_letter, p))
            pygame.display.update(dirty_rects)
            return
    if num in [2,10,19,27,35,44]:
        if s.game.b_return.status == False:
            p = [15,403]
            dirty_rects.append(screen.blit(return_letter, p))
            p = [83,403]
            dirty_rects.append(screen.blit(return_letter, p))
            pygame.display.update(dirty_rects)
            return
    if num in [1,15,22,26,40,47]:
        if s.game.diagonal_score.status == False:
            p = [16,574]
            dirty_rects.append(screen.blit(diagonal_score, p))
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
