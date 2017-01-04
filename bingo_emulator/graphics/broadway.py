
import pygame

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

meter = pygame.image.load('graphics/assets/register_cover.png').convert()
number = pygame.image.load('broadway/assets/number.png').convert_alpha()
ms_number = pygame.image.load('broadway/assets/ms_number.png').convert_alpha()
ms_arrow = pygame.image.load('broadway/assets/ms_arrow.png').convert_alpha()
ms_abc = pygame.image.load('broadway/assets/ms_abc.png').convert_alpha()
ms_d = pygame.image.load('broadway/assets/ms_d.png').convert_alpha()
select_now = pygame.image.load('broadway/assets/select_now.png').convert_alpha()
dt_arrow = pygame.image.load('broadway/assets/dt_arrow.png').convert_alpha()
double_triple = pygame.image.load('broadway/assets/double_triple.png').convert_alpha()
corners = pygame.image.load('broadway/assets/corners.png').convert_alpha()
ballyhole = pygame.image.load('broadway/assets/ballyhole.png').convert_alpha()
odds1 = pygame.image.load('broadway/assets/odds1.png').convert_alpha()
odds2 = pygame.image.load('broadway/assets/odds2.png').convert_alpha()
odds3 = pygame.image.load('broadway/assets/odds3.png').convert_alpha()
odds4 = pygame.image.load('broadway/assets/odds4.png').convert_alpha()
odds5 = pygame.image.load('broadway/assets/odds5.png').convert_alpha()
odds6 = pygame.image.load('broadway/assets/odds6.png').convert_alpha()
odds7 = pygame.image.load('broadway/assets/odds7.png').convert_alpha()
odds8 = pygame.image.load('broadway/assets/odds8.png').convert_alpha()
extra_balls = pygame.image.load('broadway/assets/extra_balls.png').convert_alpha()
eb = pygame.image.load('broadway/assets/eb.png').convert_alpha()
eb_number = pygame.image.load('broadway/assets/eb_number.png').convert_alpha()
tilt = pygame.image.load('broadway/assets/tilt.png').convert_alpha()
time = pygame.image.load('broadway/assets/time.png').convert_alpha()
a0 = pygame.image.load('broadway/assets/a0.png').convert_alpha()
a1 = pygame.image.load('broadway/assets/a1.png').convert_alpha()
a2 = pygame.image.load('broadway/assets/a2.png').convert_alpha()
a3 = pygame.image.load('broadway/assets/a3.png').convert_alpha()
b0 = pygame.image.load('broadway/assets/b0.png').convert_alpha()
b1 = pygame.image.load('broadway/assets/b1.png').convert_alpha()
b2 = pygame.image.load('broadway/assets/b2.png').convert_alpha()
b3 = pygame.image.load('broadway/assets/b3.png').convert_alpha()
c0 = pygame.image.load('broadway/assets/c0.png').convert_alpha()
c1 = pygame.image.load('broadway/assets/c1.png').convert_alpha()
c2 = pygame.image.load('broadway/assets/c2.png').convert_alpha()
c3 = pygame.image.load('broadway/assets/c3.png').convert_alpha()
d0 = pygame.image.load('broadway/assets/d0.png').convert_alpha()
d1 = pygame.image.load('broadway/assets/d1.png').convert_alpha()
d2 = pygame.image.load('broadway/assets/d2.png').convert_alpha()
d3 = pygame.image.load('broadway/assets/d3.png').convert_alpha()

class scorereel():
    """ Score Reels are used to count replays """
    def __init__(self, pos, image):
        self.position = pos
        self.default_y = self.position[1]
        self.image = pygame.image.load(image).convert()

reel1 = scorereel([105,310], "graphics/assets/green_reel.png")
reel10 = scorereel([86,310], "graphics/assets/green_reel.png")
reel100 = scorereel([67,310], "graphics/assets/green_reel.png")

def display(s, replays=0, menu=False):
    
    meter.set_colorkey((255,0,252))
    meter_position = [58,310]

    screen.blit(reel1.image, reel1.position)
    screen.blit(reel10.image, reel10.position)
    screen.blit(reel100.image, reel100.position)
    screen.blit(meter, meter_position)

    if s.game.square_a.position == 0:
        p = [217,337]
        screen.blit(a0, p)
    if s.game.square_a.position == 1:
        p = [217,337]
        screen.blit(a1, p)
    if s.game.square_a.position == 2:
        p = [217,337]
        screen.blit(a2, p)
    if s.game.square_a.position == 3:
        p = [217,337]
        screen.blit(a3, p)
    if s.game.square_b.position == 0:
        p = [216,508]
        screen.blit(b0, p)
    if s.game.square_b.position == 1:
        p = [216,508]
        screen.blit(b1, p)
    if s.game.square_b.position == 2:
        p = [216,508]
        screen.blit(b2, p)
    if s.game.square_b.position == 3:
        p = [216,508]
        screen.blit(b3, p)
    if s.game.square_c.position == 0:
        p = [385,337]
        screen.blit(c0, p)
    if s.game.square_c.position == 1:
        p = [385,337]
        screen.blit(c1, p)
    if s.game.square_c.position == 2:
        p = [385,337]
        screen.blit(c2, p)
    if s.game.square_c.position == 3:
        p = [385,337]
        screen.blit(c3, p)
    if s.game.square_d.position == 0:
        p = [390,509]
        screen.blit(d0, p)
    if s.game.square_d.position == 1:
        p = [390,509]
        screen.blit(d1, p)
    if s.game.square_d.position == 2:
        p = [390,509]
        screen.blit(d2, p)
    if s.game.square_d.position == 3:
        p = [390,509]
        screen.blit(d3, p)


    backglass_position = [0, 0]
    backglass = pygame.Surface(screen.get_size(), flags=pygame.SRCALPHA)
    backglass.fill((0, 0, 0))
    if menu == True:
        backglass = pygame.image.load('broadway/assets/broadway_menu.png')
    else:
        if (s.game.anti_cheat.status == True):
            backglass = pygame.image.load('broadway/assets/broadway_gi.png')
        else:
            backglass = pygame.image.load('broadway/assets/broadway_off.png')
    backglass = pygame.transform.scale(backglass, (720, 1280))
    
    screen.blit(backglass, backglass_position)


    if s.game.tilt.status == False:
        if s.holes:
            if 1 in s.holes:
                if s.game.square_a.position == 0:
                    p = [219,396]
                    screen.blit(number, p)
                elif s.game.square_a.position == 1:
                    p = [220,339]
                    screen.blit(number, p)
                elif s.game.square_a.position == 2:
                    p = [275,339]
                    screen.blit(number, p)
                else:
                    p = [275,395]
                    screen.blit(number, p)
            if 2 in s.holes:
                number_position = [219,452]
                screen.blit(number, number_position)
            if 3 in s.holes:
                if s.game.square_d.position == 0:
                    p = [446,509]
                    screen.blit(number, p)
                elif s.game.square_d.position == 1:
                    p = [447,567]
                    screen.blit(number, p)
                elif s.game.square_d.position == 2:
                    p = [389,566]
                    screen.blit(number, p)
                else:
                    p = [390,509]
                    screen.blit(number, p)
            if 4 in s.holes:
                if s.game.square_a.position == 0:
                    p = [275,339]
                    screen.blit(number, p)
                elif s.game.square_a.position == 1:
                    p = [275,395]
                    screen.blit(number, p)
                elif s.game.square_a.position == 2:
                    p = [219,396]
                    screen.blit(number, p)
                else:
                    p = [220,339]
                    screen.blit(number, p)
            if 5 in s.holes:
                number_position = [333,566]
                screen.blit(number, number_position)
            if 6 in s.holes:
                if s.game.square_c.position == 0:
                    p = [444,338]
                    screen.blit(number, p)
                elif s.game.square_c.position == 1:
                    p = [445,393]
                    screen.blit(number, p)
                elif s.game.square_c.position == 2:
                    p = [388,395]
                    screen.blit(number, p)
                else:
                    p = [389,338]
                    screen.blit(number, p)
            if 7 in s.holes:
                if s.game.square_d.position == 0:
                    p = [390,565]
                    screen.blit(number, p)
                elif s.game.square_d.position == 1:
                    p = [389,509]
                    screen.blit(number, p)
                elif s.game.square_d.position == 2:
                    p = [447,508]
                    screen.blit(number, p)
                else:
                    p = [447,565]
                    screen.blit(number, p)
            if 8 in s.holes:
                if s.game.square_c.position == 0:
                    p = [445,393]
                    screen.blit(number, p)
                elif s.game.square_c.position == 1:
                    p = [388,393]
                    screen.blit(number, p)
                elif s.game.square_c.position == 2:
                    p = [387,337]
                    screen.blit(number, p)
                else:
                    p = [443,338]
                    screen.blit(number, p)
            if 9 in s.holes:
                if s.game.square_a.position == 0:
                    p = [219,339]
                    screen.blit(number, p)
                elif s.game.square_a.position == 1:
                    p = [275,339]
                    screen.blit(number, p)
                elif s.game.square_a.position == 2:
                    p = [275,393]
                    screen.blit(number, p)
                else:
                    p = [217,394]
                    screen.blit(number, p)
            if 10 in s.holes:
                if s.game.square_b.position == 0:
                    p = [218,509]
                    screen.blit(number, p)
                elif s.game.square_b.position == 1:
                    p = [274,509]
                    screen.blit(number, p)
                elif s.game.square_b.position == 2:
                    p = [275,566]
                    screen.blit(number, p)
                else:
                    p = [219,565]
                    screen.blit(number, p)
            if 11 in s.holes:
                number_position = [446,451]
                screen.blit(number, number_position)
            if 12 in s.holes:
                number_position = [388,450]
                screen.blit(number, number_position)
            if 13 in s.holes:
                number_position = [331,507]
                screen.blit(number, number_position)
            if 14 in s.holes:
                if s.game.square_c.position == 0:
                    p = [387,338]
                    screen.blit(number, p)
                elif s.game.square_c.position == 1:
                    p = [445,338]
                    screen.blit(number, p)
                elif s.game.square_c.position == 2:
                    p = [445,394]
                    screen.blit(number, p)
                else:
                    p = [387,394]
                    screen.blit(number, p)
            if 15 in s.holes:
                if s.game.square_b.position == 0:
                    p = [219,565]
                    screen.blit(number, p)
                elif s.game.square_b.position == 1:
                    p = [219,508]
                    screen.blit(number, p)
                elif s.game.square_b.position == 2:
                    p = [274,507]
                    screen.blit(number, p)
                else:
                    p = [275,565]
                    screen.blit(number, p)
            if 16 in s.holes:
                number_position = [331,451]
                screen.blit(number, number_position)
            if 17 in s.holes:
                if s.game.square_d.position == 0:
                    p = [447,566]
                    screen.blit(number, p)
                elif s.game.square_d.position == 1:
                    p = [389,565]
                    screen.blit(number, p)
                elif s.game.square_d.position == 2:
                    p = [389,508]
                    screen.blit(number, p)
                else:
                    p = [447,507]
                    screen.blit(number, p)
            if 18 in s.holes:
                number_position = [274,450]
                screen.blit(number, number_position)
            if 19 in s.holes:
                if s.game.square_a.position == 0:
                    p = [274,393]
                    screen.blit(number, p)
                elif s.game.square_a.position == 1:
                    p = [218,394]
                    screen.blit(number, p)
                elif s.game.square_a.position == 2:
                    p = [218,337]
                    screen.blit(number, p)
                else:
                    p = [273,337]
                    screen.blit(number, p)
            if 20 in s.holes:
                if s.game.square_c.position == 0:
                    p = [387,395]
                    screen.blit(number, p)
                elif s.game.square_c.position == 1:
                    p = [387,337]
                    screen.blit(number, p)
                elif s.game.square_c.position == 2:
                    p = [444,338]
                    screen.blit(number, p)
                else:
                    p = [445,393]
                    screen.blit(number, p)
            if 21 in s.holes:
                if s.game.square_d.position == 0:
                    p = [390,509]
                    screen.blit(number, p)
                elif s.game.square_d.position == 1:
                    p = [445,508]
                    screen.blit(number, p)
                elif s.game.square_d.position == 2:
                    p = [447,566]
                    screen.blit(number, p)
                else:
                    p = [389,565]
                    screen.blit(number, p)
            if 22 in s.holes:
                if s.game.square_b.position == 0:
                    p = [275,507]
                    screen.blit(number, p)
                elif s.game.square_b.position == 1:
                    p = [274,563]
                    screen.blit(number, p)
                elif s.game.square_b.position == 2:
                    p = [217,565]
                    screen.blit(number, p)
                else:
                    p = [218,507]
                    screen.blit(number, p)
            if 23 in s.holes:
                if s.game.square_b.position == 0:
                    p = [275,563]
                    screen.blit(number, p)
                elif s.game.square_b.position == 1:
                    p = [217,565]
                    screen.blit(number, p)
                elif s.game.square_b.position == 2:
                    p = [218, 507]
                    screen.blit(number, p)
                else:
                    p = [275, 507]
                    screen.blit(number, p)
            if 24 in s.holes:
                number_position = [331,394]
                screen.blit(number, number_position)
            if 25 in s.holes:
                number_position = [332,338]
                screen.blit(number, number_position)

    if s.game.red_line.position == 1:
        p = [49,950]
        screen.blit(dt_arrow, p)
    elif s.game.red_line.position == 2:
        p = [48,905]
        screen.blit(dt_arrow, p)
    elif s.game.red_line.position == 3:
        p = [47,861]
        screen.blit(dt_arrow, p)
    elif s.game.red_line.position == 4:
        p = [47,816]
        screen.blit(dt_arrow, p)
    if s.game.red_line.position >= 5 and s.game.red_line.position < 10:
        p = [20,717]
        screen.blit(double_triple, p)
    if s.game.red_line.position == 6:
        p = [47,675]
        screen.blit(dt_arrow, p)
    elif s.game.red_line.position == 7:
        p = [48,629]
        screen.blit(dt_arrow, p)
    elif s.game.red_line.position == 8:
        p = [47,583]
        screen.blit(dt_arrow, p)
    elif s.game.red_line.position == 9:
        p = [46,535]
        screen.blit(dt_arrow, p)
    if s.game.red_line.position == 10:
        p = [20,440]
        screen.blit(double_triple, p)

    if s.game.yellow_line.position == 1:
        p = [637,950]
        screen.blit(dt_arrow, p)
    elif s.game.yellow_line.position == 2:
        p = [638,906]
        screen.blit(dt_arrow, p)
    elif s.game.yellow_line.position == 3:
        p = [638,861]
        screen.blit(dt_arrow, p)
    elif s.game.yellow_line.position == 4:
        p = [638,816]
        screen.blit(dt_arrow, p)
    if s.game.yellow_line.position >= 5 and s.game.yellow_line.position < 10:
        p = [613,718]
        screen.blit(double_triple, p)
    if s.game.yellow_line.position == 6:
        p = [638,675]
        screen.blit(dt_arrow, p)
    elif s.game.yellow_line.position == 7:
        p = [638,629]
        screen.blit(dt_arrow, p)
    elif s.game.yellow_line.position == 8:
        p = [638,583]
        screen.blit(dt_arrow, p)
    elif s.game.yellow_line.position == 9:
        p = [638,537]
        screen.blit(dt_arrow, p)
    if s.game.yellow_line.position == 10:
        p = [611,439]
        screen.blit(double_triple, p)

    if s.game.magic_squares_feature.position == 1:
        p = [100,649]
        screen.blit(ms_arrow, p)
    if s.game.magic_squares_feature.position == 2:
        p = [134,649]
        screen.blit(ms_arrow, p)
    if s.game.magic_squares_feature.position == 3:
        p = [168,649]
        screen.blit(ms_arrow, p)
    if s.game.magic_squares_feature.position == 4:
        p = [203,650]
        screen.blit(ms_arrow, p)
    if s.game.magic_squares_feature.position >= 5:
        p = [240,650]
        screen.blit(ms_abc, p)
    if s.game.magic_squares_feature.position >= 6:
        if 2 in s.holes:
            p = [413,652]
            screen.blit(ms_number, p)
        else:
            p = [462,652]
            screen.blit(ms_number, p)
    if s.game.magic_squares_feature.position == 7:
        p = [517,650]
        screen.blit(ms_d, p)

    if s.game.odds.position == 1:
        p = [93,880]
        screen.blit(odds1, p)
    elif s.game.odds.position == 2:
        p = [123,781]
        screen.blit(odds2, p)
    elif s.game.odds.position == 3:
        p = [201,781]
        screen.blit(odds3, p)
    elif s.game.odds.position == 4:
        p = [279,782]
        screen.blit(odds4, p)
    elif s.game.odds.position == 5:
        p = [370,782]
        screen.blit(odds5, p)
    elif s.game.odds.position == 6:
        p = [448,782]
        screen.blit(odds6, p)
    elif s.game.odds.position == 7:
        p = [526,783]
        screen.blit(odds7, p)
    elif s.game.odds.position == 8:
        p = [585,881]
        screen.blit(odds8, p)

    if s.game.magic_squares_feature.position >= 5:
        if s.game.before_fourth.status == True:
            p = [162,711]
            screen.blit(time, p)
            if s.game.ball_count.position == 3:
                p = [258,738]
                screen.blit(select_now, p)
        else:
            p = [467,711]
            screen.blit(time, p)
            if s.game.ball_count.position == 4:
                p = [258,738]
                screen.blit(select_now, p)

    if s.game.corners.status == True:
        p = [619,330]
        screen.blit(corners, p)

    if s.game.ballyhole.status == True:
        p = [605,242]
        screen.blit(ballyhole, p)

    if s.game.extra_ball.position >= 1:
        p = [139,1009]
        screen.blit(eb_number, p)
    if s.game.extra_ball.position >= 2:
        p = [186,1011]
        screen.blit(eb, p)
    if s.game.extra_ball.position >= 3:
        p = [253,1010]
        screen.blit(eb, p)
    if s.game.extra_ball.position >= 4:
        p = [324,1013]
        screen.blit(eb_number, p)
    if s.game.extra_ball.position >= 5:
        p = [373,1011]
        screen.blit(eb, p)
    if s.game.extra_ball.position >= 6:
        p = [440,1011]
        screen.blit(eb, p)
    if s.game.extra_ball.position >= 7:
        p = [512,1011]
        screen.blit(eb_number, p)
    if s.game.extra_ball.position >= 8:
        p = [560,1009]
        screen.blit(eb, p)
    if s.game.extra_ball.position == 9:
        p = [627,1009]
        screen.blit(eb, p)

    if s.game.eb_play.status == True:
        p = [28,1006]
        screen.blit(extra_balls, p)


    if s.game.tilt.status == True:
        tilt_position = [67,368]
        screen.blit(tilt, tilt_position)

    pygame.display.flip()
    pygame.display.update()

def eb_animation(num):

    global screen
    if num == 9:
        p = [139,1009]
        screen.blit(eb_number, p)
        pygame.display.update()
    if num == 8:
        p = [186,1011]
        screen.blit(eb, p)
        pygame.display.update()
    if num == 7:
        p = [253,1010]
        screen.blit(eb, p)
        pygame.display.update()
    if num == 6:
        p = [324,1013]
        screen.blit(eb_number, p)
        pygame.display.update()
    if num == 5:
        p = [373,1011]
        screen.blit(eb, p)
        pygame.display.update()
    if num == 4:
        p = [440,1011]
        screen.blit(eb, p)
        pygame.display.update()
    if num == 3:
        p = [512,1011]
        screen.blit(eb_number, p)
        pygame.display.update()
    if num == 2:
        p = [560,1009]
        screen.blit(eb, p)
        pygame.display.update()
    if num == 1:
        p = [627,1009]
        screen.blit(eb, p)
        pygame.display.update()


def feature_animation(num):
    global screen
    if num == 6:
        p = [619,330]
        screen.blit(corners, p)
        pygame.display.update()

    if num == 3:
        p = [240,649]
        screen.blit(ms_abc, p)
        pygame.display.update()
   

def odds_animation(num):
    global screen

    if num == 5:
        p = [93,883]
        screen.blit(odds1, p)
        pygame.display.update()
    if num == 4:
        p = [123,783]
        screen.blit(odds2, p)
        pygame.display.update()
    if num == 3:
        p = [201,784]
        screen.blit(odds3, p)
        pygame.display.update()
    if num == 2:
        p = [277,784]
        screen.blit(odds4, p)
        pygame.display.update()
    if num == 1:
        p = [376,782]
        screen.blit(odds5, p)
        pygame.display.update()
