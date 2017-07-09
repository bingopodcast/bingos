
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
columna = pygame.image.load('galaxy/assets/columna.png').convert_alpha()
columnc = pygame.image.load('galaxy/assets/columnc.png').convert_alpha()
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
        p = [218,360]
        screen.blit(columna, p)
    else:
        p = [218,268]
        screen.blit(columna, p)

    if s.game.line2.position in [0,2]:
        p = [311,315]
        screen.blit(columnb, p)
    elif s.game.line2.position == 1:
        p = [311,360]
        screen.blit(columnb, p)
    else:
        p = [311,268]
        screen.blit(columnb, p)

    if s.game.line3.position in [0,2]:
        p = [407,315]
        screen.blit(columnc, p)
    elif s.game.line3.position == 1:
        p = [407,360]
        screen.blit(columnc, p)
    else:
        p = [407,268]
        screen.blit(columnc, p)


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

    if s.game.mystic_lines.position >= 1:
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
        t = 4
        if s.game.selection_feature.position in [4,5]:
            t = 5
        if s.game.selection_feature.position == 6:
            t = 6
        if s.game.ball_count.position == t:
            p = [299,702]
            screen.blit(select_now, p)

    if s.game.b_return.status == True:
        t = 4
        if s.game.selection_feature.position in [4,5]:
            t = 5
        if s.game.selection_feature.position == 6:
            t = 6
        if s.game.ball_count.position == t:
            p = [17,493]
            screen.blit(return_select_now, p)


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
                    p = [220,361]
                    screen.blit(number, p)
                else:
                    p = [221,459]
                    screen.blit(number, p)
            if 3 in s.holes:
                if s.game.line3.position in [0,2]:
                    p = [411,411]
                    screen.blit(number, p)
                elif s.game.line3.position == 1:
                    p = [411,461]
                    screen.blit(number, p)
                else:
                    p = [411,363]
                    screen.blit(number, p)
            if 4 in s.holes:
                if s.game.line3.position in [0,2]:
                    p = [460,363]
                    screen.blit(number, p)
                elif s.game.line3.position == 1:
                    p = [460,413]
                    screen.blit(number, p)
                else:
                    p = [460,510]
                    screen.blit(number, p)
            if 5 in s.holes:
                if s.game.line3.position in [0,2]:
                    p = [411,509]
                    screen.blit(number, p)
                elif s.game.line3.position == 1:
                    p = [411,363]
                    screen.blit(number, p)
                else:
                    p = [411,461]
                    screen.blit(number, p)
            if 6 in s.holes:
                if s.game.line2.position in [0,2]:
                    p = [365,362]
                    screen.blit(number, p)
                elif s.game.line2.position == 1:
                    p = [365,410]
                    screen.blit(number, p)
                else:
                    p = [365,510]
                    screen.blit(number, p)
            if 7 in s.holes:
                if s.game.line1.position in [0,2]:
                    p = [221,410]
                    screen.blit(number, p)
                elif s.game.line1.position == 1:
                    p = [221,459]
                    screen.blit(number, p)
                else:
                    p = [221,360]
                    screen.blit(number, p)
            if 8 in s.holes:
                if s.game.line1.position in [0,2]:
                    p = [269,360]
                    screen.blit(number, p)
                elif s.game.line1.position == 1:
                    p = [269,409]
                    screen.blit(number, p)
                else:
                    p = [269,509]
                    screen.blit(number, p)
            if 9 in s.holes:
                if s.game.line1.position in [0,2]:
                    p = [220,360]
                    screen.blit(number, p)
                elif s.game.line1.position == 1:
                    p = [221,409]
                    screen.blit(number, p)
                else:
                    p = [221,509]
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
                    p = [317,461]
                    screen.blit(number, p)
                else:
                    p = [317,362]
                    screen.blit(number, p)
            if 13 in s.holes:
                if s.game.line2.position in [0,2]:
                    p = [317,509]
                    screen.blit(number, p)
                elif s.game.line2.position == 1:
                    p = [317,363]
                    screen.blit(number, p)
                else:
                    p = [317,460]
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
                    p = [365,362]
                    screen.blit(number, p)
                else:
                    p = [365,461]
                    screen.blit(number, p)
            if 16 in s.holes:
                if s.game.line1.position in [0,2]:
                    p = [222,459]
                    screen.blit(number, p)
                elif s.game.line1.position == 1:
                    p = [221,509]
                    screen.blit(number, p)
                else:
                    p = [221,409]
                    screen.blit(number, p)
            if 17 in s.holes:
                if s.game.line1.position in [0,2]:
                    p = [269,509]
                    screen.blit(number, p)
                elif s.game.line1.position == 1:
                    p = [269,361]
                    screen.blit(number, p)
                else:
                    p = [269,459]
                    screen.blit(number, p)
            if 18 in s.holes:
                if s.game.line3.position in [0,2]:
                    p = [412,363]
                    screen.blit(number, p)
                elif s.game.line3.position == 1:
                    p = [413,410]
                    screen.blit(number, p)
                else:
                    p = [412,509]
                    screen.blit(number, p)
            if 19 in s.holes:
                if s.game.line2.position in [0,2]:
                    p = [317,461]
                    screen.blit(number, p)
                elif s.game.line2.position == 1:
                    p = [318,509]
                    screen.blit(number, p)
                else:
                    p = [317,411]
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
                    p = [411,509]
                    screen.blit(number, p)
                else:
                    p = [411,411]
                    screen.blit(number, p)
            if 22 in s.holes:
                if s.game.line2.position in [0,2]:
                    p = [317,361]
                    screen.blit(number, p)
                elif s.game.line2.position == 1:
                    p = [317,410]
                    screen.blit(number, p)
                else:
                    p = [317,507]
                    screen.blit(number, p)
            if 23 in s.holes:
                if s.game.line3.position in [0,2]:
                    p = [461,509]
                    screen.blit(number, p)
                elif s.game.line3.position == 1:
                    p = [460,362]
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

def eb_animation(num):
    pass

def feature_animation(num):
    global screen

    if num == 4:
        p = [393,613]
        screen.blit(ml_arrow, p)
        pygame.display.update()
    else:
        p = [437,605]
        screen.blit(ml_letter, p)
        pygame.display.update()


def odds_animation(num):
    global screen

    if num == 8:
        o = [183,827]
        screen.blit(odds, o)
    if num == 7:
        o = [243,827]
        screen.blit(odds, o)
    if num == 6:
        o = [298,827]
        screen.blit(odds, o)
    if num == 5:
        o = [350,827]
        screen.blit(odds, o)
    if num == 4:
        o = [399,827]
        screen.blit(odds, o)
    if num == 3:
        o = [445,827]
        screen.blit(odds, o)
    if num == 2:
        o = [490,827]
        screen.blit(odds, o)
    if num == 1:
        o = [535,827]
        screen.blit(odds, o)
    pygame.display.update()


