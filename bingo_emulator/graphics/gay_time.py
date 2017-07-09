
import pygame
import random

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

meter = pygame.image.load('graphics/assets/register_cover.png').convert()
eb = pygame.image.load('gay_time/assets/eb.png').convert_alpha()
ebs = pygame.image.load('gay_time/assets/extra_balls.png').convert_alpha()
number_eb = pygame.image.load('gay_time/assets/eb_number.png').convert_alpha()
o1 = pygame.image.load('gay_time/assets/odds1.png').convert_alpha()
o2 = pygame.image.load('gay_time/assets/odds2.png').convert_alpha()
o3 = pygame.image.load('gay_time/assets/odds3.png').convert_alpha()
o4 = pygame.image.load('gay_time/assets/odds4.png').convert_alpha()
o5 = pygame.image.load('gay_time/assets/odds5.png').convert_alpha()
o6 = pygame.image.load('gay_time/assets/odds6.png').convert_alpha()
o7 = pygame.image.load('gay_time/assets/odds7.png').convert_alpha()
o8 = pygame.image.load('gay_time/assets/odds8.png').convert_alpha()
o9 = pygame.image.load('gay_time/assets/odds9.png').convert_alpha()
o10 = pygame.image.load('gay_time/assets/odds10.png').convert_alpha()
c = pygame.image.load('gay_time/assets/corners.png').convert_alpha()
m = pygame.image.load('gay_time/assets/pockets.png').convert_alpha()
number = pygame.image.load('gay_time/assets/number.png').convert_alpha()
tilt = pygame.image.load('gay_time/assets/tilt.png').convert_alpha()
magic_arrow = pygame.image.load('gay_time/assets/magic_arrow.png').convert_alpha()
magic_line = pygame.image.load('gay_time/assets/magic_line.png').convert_alpha()
magic_line2 = pygame.image.load('gay_time/assets/magic_line2.png').convert_alpha()
select_now = pygame.image.load('gay_time/assets/select_now.png').convert_alpha()
pockets_now = pygame.image.load('gay_time/assets/pockets_now.png').convert_alpha()
line1 = pygame.image.load('gay_time/assets/line1.png').convert_alpha()
line2 = pygame.image.load('gay_time/assets/line2.png').convert_alpha()
line3 = pygame.image.load('gay_time/assets/line3.png').convert_alpha()
line4 = pygame.image.load('gay_time/assets/line4.png').convert_alpha()
three_as_four = pygame.image.load('gay_time/assets/three_as_four.png').convert_alpha()
spotted = pygame.image.load('gay_time/assets/spotted.png').convert_alpha()

class scorereel():
    """ Score Reels are used to count replays """
    def __init__(self, pos, image):
        self.position = pos
        self.default_y = self.position[1]
        self.image = pygame.image.load(image).convert()

reel1 = scorereel([98,300], "graphics/assets/green_reel.png")
reel10 = scorereel([79,300], "graphics/assets/green_reel.png")
reel100 = scorereel([61,300], "graphics/assets/green_reel.png")

def display(s, replays=0, menu=False):
    
    meter.set_colorkey((255,0,252))
    meter_position = [51,300]

    screen.blit(reel1.image, reel1.position)
    screen.blit(reel10.image, reel10.position)
    screen.blit(reel100.image, reel100.position)
    screen.blit(meter, meter_position)

    if s.game.line1.position == 0:
        line1_position = [227,344]
    elif s.game.line1.position == 1:
        line1_position = [227,399]
    elif s.game.line1.position == 2:
        line1_position = [227,289]
    
    screen.blit(line1, line1_position)

    if s.game.line2.position == 0:
        line2_position = [280,344]
    elif s.game.line2.position == 1:
        line2_position = [280,399]
    elif s.game.line2.position == 2:
        line2_position = [280,289]
    
    screen.blit(line2, line2_position)

    if s.game.line3.position == 0:
        line3_position = [333,344]
    elif s.game.line3.position == 1:
        line3_position = [333,399]
    elif s.game.line3.position == 2:
        line3_position = [333,289]
    
    screen.blit(line3, line3_position)

    if s.game.line4.position == 0:
        line4_position = [387,344]
    elif s.game.line4.position == 1:
        line4_position = [387,399]
    elif s.game.line4.position == 2:
        line4_position = [387,289]

    screen.blit(line4, line4_position)

    backglass_position = [0, 0]
    backglass = pygame.Surface(screen.get_size(), flags=pygame.SRCALPHA)
    backglass.fill((0, 0, 0))
    if menu == True:
        backglass = pygame.image.load('gay_time/assets/gay_time_menu.png').convert()
        backglass.set_colorkey((255,0,252))
    else:
        if (s.game.anti_cheat.status == True):
            backglass = pygame.image.load('gay_time/assets/gay_time_gi.png').convert()
            backglass.set_colorkey((255,0,252))
        else:
            backglass = pygame.image.load('gay_time/assets/gay_time_off.png').convert()
            backglass.set_colorkey((255,0,252))
    backglass = pygame.transform.scale(backglass, (720, 1280))
    
    screen.blit(backglass, backglass_position)

    if s.game.extra_ball.position >= 1:
        eb_position = [140,1016]
        screen.blit(number_eb, eb_position)
    if s.game.extra_ball.position >= 2:
        eb_position = [185,1016]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 3:
        eb_position = [253,1016]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 4:
        eb_position = [326,1016]
        screen.blit(number_eb, eb_position)
    if s.game.extra_ball.position >= 5:
        eb_position = [375,1016]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 6:
        eb_position = [442,1016]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 7:
        eb_position = [512,1016]
        screen.blit(number_eb, eb_position)
    if s.game.extra_ball.position >= 8:
        eb_position = [564,1016]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 9:
        eb_position = [630,1016]
        screen.blit(eb, eb_position)
    
    
    if s.game.odds.position > 0:
        if s.game.odds.position == 1:
            odds_position = [21,889]
            screen.blit(o1, odds_position)
        if s.game.odds.position == 2:
            odds_position = [104,846]
            screen.blit(o2, odds_position)
        if s.game.odds.position == 3:
            odds_position = [174,844]
            screen.blit(o3, odds_position)
        if s.game.odds.position == 4:
            odds_position = [234,871]
            screen.blit(o4, odds_position)
        if s.game.odds.position == 5:
            odds_position = [292,850]
            screen.blit(o5, odds_position)
        if s.game.odds.position == 6:
            odds_position = [365,847]
            screen.blit(o6, odds_position)
        if s.game.odds.position == 7:
            odds_position = [424,880]
            screen.blit(o7, odds_position)
        if s.game.odds.position == 8:
            odds_position = [470,851]
            screen.blit(o8, odds_position)
        if s.game.odds.position == 9:
            odds_position = [568,852]
            screen.blit(o9, odds_position)
        if s.game.odds.position == 10:
            odds_position = [620,880]
            screen.blit(o10, odds_position)

    if s.game.corners.status == True:
        corners_position = [72,456]
        screen.blit(c, corners_position)


    if s.game.tilt.status == False:
        if s.holes:
            if 1 in s.holes:
                if s.game.line1.position == 0:
                    number_position = [339,565]
                    screen.blit(number, number_position)
                elif s.game.line1.position == 1:
                    number_position = [339,618]
                    screen.blit(number, number_position)
                elif s.game.line1.position == 2:
                    number_position = [337,509]
                    screen.blit(number, number_position)
            if 2 in s.holes:
                if s.game.line1.position == 0:
                    number_position = [230,507]
                    screen.blit(number, number_position)
                elif s.game.line1.position == 1:
                    number_position = [230,564]
                    screen.blit(number, number_position)
                elif s.game.line1.position == 2:
                    number_position = [230,453]
                    screen.blit(number, number_position)
            if 3 in s.holes:
                number_position = [444,617]
                screen.blit(number, number_position)
            if 4 in s.holes:
                if s.game.line2.position == 0:
                    number_position = [282,400]
                    screen.blit(number, number_position)
                elif s.game.line2.position == 1:
                    number_position = [282,456]
                    screen.blit(number, number_position)
                elif s.game.line2.position == 2:
                    number_position = [282,618]
                    screen.blit(number, number_position)
            if 5 in s.holes:
                if s.game.line3.position == 0:
                    number_position = [338,618]
                    screen.blit(number, number_position)
                elif s.game.line3.position == 1:
                    number_position = [338,400]
                    screen.blit(number, number_position)
                elif s.game.line3.position == 2:
                    number_position = [338,564]
                    screen.blit(number, number_position)
            if 6 in s.holes:
                number_position = [443,454]
                screen.blit(number, number_position)
            if 7 in s.holes:
                if s.game.line2.position == 0:
                    number_position = [285,618]
                    screen.blit(number, number_position)
                elif s.game.line2.position == 1:
                    number_position = [285,400]
                    screen.blit(number, number_position)
                elif s.game.line2.position == 2:
                    number_position = [285,564]
                    screen.blit(number, number_position)
            if 8 in s.holes:
                number_position = [442,401]
                screen.blit(number, number_position)
            if 9 in s.holes:
                if s.game.line1.position == 0:
                    number_position = [228,402]
                    screen.blit(number, number_position)
                elif s.game.line1.position == 1:
                    number_position = [228,454]
                    screen.blit(number, number_position)
                elif s.game.line1.position == 2:
                    number_position = [230,618]
                    screen.blit(number, number_position)
            if 10 in s.holes:
                if s.game.line1.position == 0:
                    number_position = [228,454]
                    screen.blit(number, number_position)
                elif s.game.line1.position == 1:
                    number_position = [228,508]
                    screen.blit(number, number_position)
                elif s.game.line1.position == 2:
                    number_position = [228,402]
                    screen.blit(number, number_position)
            if 11 in s.holes:
                if s.game.line1.position == 0:
                    number_position = [228,618]
                    screen.blit(number, number_position)
                elif s.game.line1.position == 1:
                    number_position = [228,399]
                    screen.blit(number, number_position)
                elif s.game.line1.position == 2:
                    number_position = [228,564]
                    screen.blit(number, number_position)
            if 12 in s.holes:
                if s.game.line4.position == 0:
                    p = [389,508]
                    screen.blit(number, p)
                elif s.game.line4.position == 1:
                    p = [389,563]
                    screen.blit(number, p)
                elif s.game.line4.position == 2:
                    p = [389,451]
                    screen.blit(number, p)
            if 13 in s.holes:
                if s.game.line3.position == 0:
                    number_position = [230,564]
                    screen.blit(number, number_position)
                elif s.game.line3.position == 1:
                    number_position = [230,618]
                    screen.blit(number, number_position)
                elif s.game.line3.position == 2:
                    number_position = [228,509]
                    screen.blit(number, number_position)
            if 14 in s.holes:
                if s.game.line3.position == 0:
                    number_position = [337,455]
                    screen.blit(number, number_position)
                elif s.game.line3.position == 1:
                    number_position = [337,510]
                    screen.blit(number, number_position)
                elif s.game.line3.position == 2:
                    number_position = [337,400]
                    screen.blit(number, number_position)
            if 15 in s.holes:
                if s.game.line3.position == 0:
                    number_position = [337,400]
                    screen.blit(number, number_position)
                elif s.game.line3.position == 1:
                    number_position = [337,455]
                    screen.blit(number, number_position)
                elif s.game.line3.position == 2:
                    number_position = [337,618]
                    screen.blit(number, number_position)
            if 16 in s.holes:
                if s.game.line3.position == 0:
                    number_position = [337,509]
                    screen.blit(number, number_position)
                elif s.game.line3.position == 1:
                    number_position = [337,564]
                    screen.blit(number, number_position)
                elif s.game.line3.position == 2:
                    number_position = [337,454]
                    screen.blit(number, number_position)
            if 17 in s.holes:
                number_position = [442,562]
                screen.blit(number, number_position)
            if 18 in s.holes:
                if s.game.line2.position == 0:
                    number_position = [282,510]
                    screen.blit(number, number_position)
                elif s.game.line2.position == 1:
                    number_position = [282,564]
                    screen.blit(number, number_position)
                elif s.game.line2.position == 2:
                    number_position = [282,454]
                    screen.blit(number, number_position)
            if 19 in s.holes:
                if s.game.line2.position == 0:
                    number_position = [282,455]
                    screen.blit(number, number_position)
                elif s.game.line2.position == 1:
                    number_position = [282,508]
                    screen.blit(number, number_position)
                elif s.game.line2.position == 2:
                    number_position = [282,400]
                    screen.blit(number, number_position)
            if 20 in s.holes:
                if s.game.line4.position == 0:
                    p = [389,450]
                    screen.blit(number, p)
                elif s.game.line4.position == 1:
                    p = [389,506]
                    screen.blit(number, p)
                elif s.game.line4.position == 2:
                    p = [389,398]
                    screen.blit(number, p)
            if 21 in s.holes:
                if s.game.line4.position == 0:
                    p = [389,564]
                    screen.blit(number, p)
                elif s.game.line4.position == 1:
                    p = [389,618]
                    screen.blit(number, p)
                elif s.game.line4.position == 2:
                    p = [389,507]
                    screen.blit(number, p)
            if 22 in s.holes:
                if s.game.line2.position == 0:
                    number_position = [282,564]
                    screen.blit(number, number_position)
                elif s.game.line2.position == 1:
                    number_position = [282,618]
                    screen.blit(number, number_position)
                elif s.game.line2.position == 2:
                    number_position = [282,508]
                    screen.blit(number, number_position)
            if 23 in s.holes:
                if s.game.line4.position == 0:
                    p = [389,616]
                    screen.blit(number, p)
                elif s.game.line4.position == 1:
                    p = [389,397]
                    screen.blit(number, p)
                elif s.game.line4.position == 2:
                    p = [389,562]
                    screen.blit(number, p)
            if 24 in s.holes:
                if s.game.line4.position == 0:
                    p = [389,397]
                    screen.blit(number, p)
                elif s.game.line4.position == 1:
                    p = [389,451]
                    screen.blit(number, p)
                elif s.game.line4.position == 2:
                    p = [389,616]
                    screen.blit(number, p)
            if 25 in s.holes:
                number_position = [441,508]
                screen.blit(number, number_position)

    if s.game.tilt.status == True:
        tilt_position = [443,692]
        screen.blit(tilt, tilt_position)

    if s.game.eb_play.status == True:
        ebs_position = [23,1015]
        screen.blit(ebs, ebs_position)

    if s.game.magic_lines.position == 1:
        p = [41,803]
        screen.blit(magic_arrow, p)
    elif s.game.magic_lines.position == 2:
        p = [76,803]
        screen.blit(magic_arrow, p)
    elif s.game.magic_lines.position == 3:
        p = [111,803]
        screen.blit(magic_arrow, p)
    elif s.game.magic_lines.position == 4:
        p = [148,803]
        screen.blit(magic_arrow, p)
    elif s.game.magic_lines.position >= 5:
        p = [184,807]
        screen.blit(magic_line, p)
        if s.game.ball_count.position == 3:
            p = [525,799]
            screen.blit(select_now, p)
    if s.game.magic_lines.position >= 5:
        p = [307,807]
        screen.blit(magic_line2, p)
    if s.game.magic_lines.position >= 6:
        p = [413,807]
        screen.blit(magic_line2, p)


    if s.game.magic_pockets.status == True:
        p = [29,545]
        screen.blit(m, p)
        if s.game.ball_count.position == 3:
            p = [28,735]
            screen.blit(pockets_now, p)
   
    if s.game.red_three_as_four.status == True:
        p = [544,527]
        screen.blit(three_as_four, p)
    if s.game.yellow_three_as_four.status == True:
        p = [543,661]
        screen.blit(three_as_four, p)

    if s.game.spot_10.status == True:
        p = [538,454]
        screen.blit(spotted, p)
    if s.game.spot_25.status == True:
        p = [617,454]
        screen.blit(spotted, p)

    pygame.display.update()

def eb_animation(num):
    global screen

    if num == 9:
        eb_position = [140,1016]
        screen.blit(number_eb, eb_position)
        pygame.display.update()
    if num == 8:
        eb_position = [185,1016]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 7:
        eb_position = [253,1016]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 6:
        eb_position = [326,1016]
        screen.blit(number_eb, eb_position)
        pygame.display.update()
    if num == 5:
        eb_position = [375,1016]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 4:
        eb_position = [442,1016]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 3:
        eb_position = [512,1016]
        screen.blit(number_eb, eb_position)
        pygame.display.update()
    if num == 2:
        eb_position = [564,1016]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 1:
        eb_position = [630,1016]
        screen.blit(eb, eb_position)
        pygame.display.update()


def feature_animation(num):
    global screen
    if num == 6:
        corners_position = [72,456]
        screen.blit(c, corners_position)
        pygame.display.update()

    if num == 5:
        p = [538,454]
        screen.blit(spotted, p)
        pygame.display.update()

    if num == 4:
        p = [617,454]
        screen.blit(spotted, p)
        pygame.display.update()

    if num == 3:
        p = [29,545]
        screen.blit(m, p)
        pygame.display.update()
   
    if num == 2:
        p = [307,807]
        screen.blit(magic_line2, p)
        pygame.display.update()

    if num == 1:
        p = [307,807]
        screen.blit(magic_line2, p)
        pygame.display.update()


def odds_animation(num):
    global screen

    if num == 5:
        odds_position = [21,889]
        o = pygame.image.load('gay_time/assets/odds1.png').convert_alpha()
        screen.blit(o, odds_position)
        pygame.display.update()
    if num == 4:
        odds_position = [104,846]
        o = pygame.image.load('gay_time/assets/odds2.png').convert_alpha()
        screen.blit(o, odds_position)
        pygame.display.update()
    if num == 3:
        odds_position = [174,844]
        o = pygame.image.load('gay_time/assets/odds3.png').convert_alpha()
        screen.blit(o, odds_position)
        pygame.display.update()
    if num == 2:
        odds_position = [234,871]
        o = pygame.image.load('gay_time/assets/odds4.png').convert_alpha()
        screen.blit(o, odds_position)
        pygame.display.update()
    if num == 1:
        odds_position = [292,850]
        o = pygame.image.load('gay_time/assets/odds5.png').convert_alpha()
        screen.blit(o, odds_position)
        pygame.display.update()
