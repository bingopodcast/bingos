
import pygame
import random

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

meter = pygame.image.load('graphics/assets/register_cover.png').convert()
eb = pygame.image.load('gayety/assets/eb.png').convert_alpha()
ebs = pygame.image.load('gayety/assets/extra_balls.png').convert_alpha()
number_eb = pygame.image.load('gayety/assets/eb_number.png').convert_alpha()
o1 = pygame.image.load('gayety/assets/odds1.png').convert_alpha()
o2 = pygame.image.load('gayety/assets/odds2.png').convert_alpha()
o3 = pygame.image.load('gayety/assets/odds3.png').convert_alpha()
o4 = pygame.image.load('gayety/assets/odds4.png').convert_alpha()
o5 = pygame.image.load('gayety/assets/odds5.png').convert_alpha()
o6 = pygame.image.load('gayety/assets/odds6.png').convert_alpha()
o7 = pygame.image.load('gayety/assets/odds7.png').convert_alpha()
o8 = pygame.image.load('gayety/assets/odds8.png').convert_alpha()
c = pygame.image.load('gayety/assets/corners.png').convert_alpha()
m = pygame.image.load('gayety/assets/magic.png').convert_alpha()
number = pygame.image.load('gayety/assets/number.png').convert_alpha()
tilt = pygame.image.load('gayety/assets/tilt.png').convert_alpha()
magic_arrow = pygame.image.load('gayety/assets/magic_arrow.png').convert_alpha()
select_now = pygame.image.load('gayety/assets/select_now.png').convert_alpha()
line1 = pygame.image.load('gayety/assets/line1.png').convert_alpha()
line2 = pygame.image.load('gayety/assets/line2.png').convert_alpha()
line3 = pygame.image.load('gayety/assets/line3.png').convert_alpha()

class scorereel():
    """ Score Reels are used to count replays """
    def __init__(self, pos, image):
        self.position = pos
        self.default_y = self.position[1]
        self.image = pygame.image.load(image).convert()

reel1 = scorereel([91,314], "graphics/assets/green_reel.png")
reel10 = scorereel([72,314], "graphics/assets/green_reel.png")
reel100 = scorereel([53,314], "graphics/assets/green_reel.png")

def display(s, replays=0, menu=False):
    
    meter.set_colorkey((255,0,252))
    meter_position = [44,314]

    screen.blit(reel1.image, reel1.position)
    screen.blit(reel10.image, reel10.position)
    screen.blit(reel100.image, reel100.position)
    screen.blit(meter, meter_position)

    if s.game.line1.position == 0:
        line1_position = [228,347]
    elif s.game.line1.position == 1:
        line1_position = [228,402]
    elif s.game.line1.position == 2:
        line1_position = [228,292]
    
    screen.blit(line1, line1_position)

    if s.game.line2.position == 0:
        line2_position = [283,347]
    elif s.game.line2.position == 1:
        line2_position = [283,402]
    elif s.game.line2.position == 2:
        line2_position = [283,292]
    
    screen.blit(line2, line2_position)

    if s.game.line3.position == 0:
        line3_position = [335,347]
    elif s.game.line3.position == 1:
        line3_position = [335,402]
    elif s.game.line3.position == 2:
        line3_position = [335,292]
    
    screen.blit(line3, line3_position)

    backglass_position = [0, 0]
    backglass = pygame.Surface(screen.get_size(), flags=pygame.SRCALPHA)
    backglass.fill((0, 0, 0))
    if menu == True:
        backglass = pygame.image.load('gayety/assets/gayety_menu.png').convert()
        backglass.set_colorkey((255,0,252))
    else:
        if (s.game.anti_cheat.status == True):
            backglass = pygame.image.load('gayety/assets/gayety_gi.png').convert()
            backglass.set_colorkey((255,0,252))
        else:
            backglass = pygame.image.load('gayety/assets/gayety_off.png').convert()
            backglass.set_colorkey((255,0,252))
    backglass = pygame.transform.scale(backglass, (720, 1280))
    
    screen.blit(backglass, backglass_position)

    if s.game.extra_ball.position >= 1:
        eb_position = [146,1018]
        screen.blit(number_eb, eb_position)
    if s.game.extra_ball.position >= 2:
        eb_position = [192,1017]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 3:
        eb_position = [261,1016]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 4:
        eb_position = [332,1016]
        screen.blit(number_eb, eb_position)
    if s.game.extra_ball.position >= 5:
        eb_position = [381,1015]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 6:
        eb_position = [448,1015]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 7:
        eb_position = [520,1014]
        screen.blit(number_eb, eb_position)
    if s.game.extra_ball.position >= 8:
        eb_position = [568,1014]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 9:
        eb_position = [634,1013]
        screen.blit(eb, eb_position)
    
    
    if s.game.odds.position > 0:
        if s.game.odds.position == 1:
            odds_position = [37,817]
            screen.blit(o1, odds_position)
        if s.game.odds.position == 2:
            odds_position = [107,816]
            screen.blit(o2, odds_position)
        if s.game.odds.position == 3:
            odds_position = [174,815]
            screen.blit(o3, odds_position)
        if s.game.odds.position == 4:
            odds_position = [240,813]
            screen.blit(o4, odds_position)
        if s.game.odds.position == 5:
            odds_position = [313,813]
            screen.blit(o5, odds_position)
        if s.game.odds.position == 6:
            odds_position = [482,812]
            screen.blit(o6, odds_position)
        if s.game.odds.position == 7:
            odds_position = [552,810]
            screen.blit(o7, odds_position)
        if s.game.odds.position == 8:
            odds_position = [617,811]
            screen.blit(o8, odds_position)

    if s.game.corners.status == True:
        corners_position = [22,467]
        screen.blit(c, corners_position)
    if s.game.corners300.status == True:
        corners_position = [119,466]
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
                number_position = [389,510]
                screen.blit(number, number_position)
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
                number_position = [391,454]
                screen.blit(number, number_position)
            if 21 in s.holes:
                number_position = [391,564]
                screen.blit(number, number_position)
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
                number_position = [389,616]
                screen.blit(number, number_position)
            if 24 in s.holes:
                number_position = [390,400]
                screen.blit(number, number_position)
            if 25 in s.holes:
                number_position = [441,508]
                screen.blit(number, number_position)

    if s.game.tilt.status == True:
        tilt_position = [147,263]
        screen.blit(tilt, tilt_position)

    if s.game.eb_play.status == True:
        ebs_position = [30,1018]
        screen.blit(ebs, ebs_position)

    if s.game.m_pockets.position == 1:
        p = [539,511]
        screen.blit(magic_arrow, p)
    elif s.game.m_pockets.position == 2:
        p = [577,511]
        screen.blit(magic_arrow, p)
    elif s.game.m_pockets.position == 3:
        p = [614,511]
        screen.blit(magic_arrow, p)
    elif s.game.m_pockets.position == 4:
        p = [652,511]
        screen.blit(magic_arrow, p)
        p = [519,548]
        screen.blit(m, p)
        if s.game.ball_count.position == 3:
            p = [520,756]
            screen.blit(select_now, p)


    if s.game.m_lines.status == True:
        p = [22,550]
        screen.blit(m, p)
        if s.game.ball_count.position == 3:
            p = [24,758]
            screen.blit(select_now, p)
    

    pygame.display.update()

def eb_animation(num):
    global screen

    if num == 9:
        eb_position = [146,1018]
        screen.blit(number_eb, eb_position)
        pygame.display.update()
    if num == 8:
        eb_position = [192,1017]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 7:
        eb_position = [261,1016]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 6:
        eb_position = [332,1016]
        screen.blit(number_eb, eb_position)
        pygame.display.update()
    if num == 5:
        eb_position = [381,1015]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 4:
        eb_position = [448,1015]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 3:
        eb_position = [520,1014]
        screen.blit(number_eb, eb_position)
        pygame.display.update()
    if num == 2:
        eb_position = [568,1014]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 1:
        eb_position = [634,1013]
        screen.blit(eb, eb_position)
        pygame.display.update()


def feature_animation(num):
    global screen
    if num == 6:
        corners_position = [22,467]
        screen.blit(c, corners_position)
        pygame.display.update()

    if num == 5:
        corners_position = [119,466]
        screen.blit(c, corners_position)
        pygame.display.update()

    if num == 4:
        corners_position = [22,467]
        screen.blit(c, corners_position)
        pygame.display.update()

    if num == 3:
        p = [22,550]
        screen.blit(m, p)
        pygame.display.update()
   
    if num == 2:
        p = [519,548]
        screen.blit(m, p)
        pygame.display.update()

    if num == 1:
        p = [441,508]
        screen.blit(number, p)
        pygame.display.update()


def odds_animation(num):
    global screen

    if num == 5:
        odds_position = [37,817]
        o = pygame.image.load('gayety/assets/odds1.png').convert_alpha()
        screen.blit(o, odds_position)
        pygame.display.update()
    if num == 4:
        odds_position = [107,816]
        o = pygame.image.load('gayety/assets/odds2.png').convert_alpha()
        screen.blit(o, odds_position)
        pygame.display.update()
    if num == 3:
        odds_position = [174,815]
        o = pygame.image.load('gayety/assets/odds3.png').convert_alpha()
        screen.blit(o, odds_position)
        pygame.display.update()
    if num == 2:
        odds_position = [240,813]
        o = pygame.image.load('gayety/assets/odds4.png').convert_alpha()
        screen.blit(o, odds_position)
        pygame.display.update()
    if num == 1:
        odds_position = [313,813]
        o = pygame.image.load('gayety/assets/odds5.png').convert_alpha()
        screen.blit(o, odds_position)
        pygame.display.update()
