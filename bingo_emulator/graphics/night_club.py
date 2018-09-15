
import pygame

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

meter = pygame.image.load('graphics/assets/register_cover.png').convert()
number = pygame.image.load('night_club/assets/number.png').convert_alpha()
ms_letter = pygame.image.load('night_club/assets/ms_letter.png').convert_alpha()
ms_number = pygame.image.load('night_club/assets/ms_number.png').convert_alpha()
ms_arrow = pygame.image.load('night_club/assets/ms_arrow.png').convert_alpha()
ms_abc = pygame.image.load('night_club/assets/ms_abc.png').convert_alpha()
ms_d = pygame.image.load('night_club/assets/ms_d.png').convert_alpha()
select_now = pygame.image.load('night_club/assets/select_now.png').convert_alpha()
dt_arrow = pygame.image.load('night_club/assets/dt_arrow.png').convert_alpha()
double = pygame.image.load('night_club/assets/double.png').convert_alpha()
triple = pygame.image.load('night_club/assets/triple.png').convert_alpha()
quadruple = pygame.image.load('night_club/assets/quadruple.png').convert_alpha()
corners = pygame.image.load('night_club/assets/corners.png').convert_alpha()
ballyhole = pygame.image.load('night_club/assets/corners.png').convert_alpha()
odds1 = pygame.image.load('night_club/assets/odds1.png').convert_alpha()
odds2 = pygame.image.load('night_club/assets/odds2.png').convert_alpha()
odds3 = pygame.image.load('night_club/assets/odds3.png').convert_alpha()
odds4 = pygame.image.load('night_club/assets/odds4.png').convert_alpha()
odds5 = pygame.image.load('night_club/assets/odds5.png').convert_alpha()
odds6 = pygame.image.load('night_club/assets/odds6.png').convert_alpha()
odds7 = pygame.image.load('night_club/assets/odds7.png').convert_alpha()
odds8 = pygame.image.load('night_club/assets/odds8.png').convert_alpha()
extra_balls = pygame.image.load('night_club/assets/extra_balls.png').convert_alpha()
eb = pygame.image.load('night_club/assets/eb.png').convert_alpha()
eb_number = pygame.image.load('night_club/assets/eb_number.png').convert_alpha()
tilt = pygame.image.load('night_club/assets/tilt.png').convert_alpha()
time = pygame.image.load('night_club/assets/time.png').convert_alpha()
a0 = pygame.image.load('night_club/assets/a0.png').convert_alpha()
a1 = pygame.image.load('night_club/assets/a1.png').convert_alpha()
a2 = pygame.image.load('night_club/assets/a2.png').convert_alpha()
a3 = pygame.image.load('night_club/assets/a3.png').convert_alpha()
b0 = pygame.image.load('night_club/assets/b0.png').convert_alpha()
b1 = pygame.image.load('night_club/assets/b1.png').convert_alpha()
b2 = pygame.image.load('night_club/assets/b2.png').convert_alpha()
b3 = pygame.image.load('night_club/assets/b3.png').convert_alpha()
c0 = pygame.image.load('night_club/assets/c0.png').convert_alpha()
c1 = pygame.image.load('night_club/assets/c1.png').convert_alpha()
c2 = pygame.image.load('night_club/assets/c2.png').convert_alpha()
c3 = pygame.image.load('night_club/assets/c3.png').convert_alpha()
d0 = pygame.image.load('night_club/assets/d0.png').convert_alpha()
d1 = pygame.image.load('night_club/assets/d1.png').convert_alpha()
d2 = pygame.image.load('night_club/assets/d2.png').convert_alpha()
d3 = pygame.image.load('night_club/assets/d3.png').convert_alpha()
bg_menu = pygame.image.load('night_club/assets/night_club_menu.png')
bg_gi = pygame.image.load('night_club/assets/night_club_gi.png')
bg_off = pygame.image.load('night_club/assets/night_club_off.png')
a_1 = pygame.image.load('night_club/assets/a-1.png').convert_alpha()
a_2 = pygame.image.load('night_club/assets/a-2.png').convert_alpha()
a_3 = pygame.image.load('night_club/assets/a-3.png').convert_alpha()
a_4 = pygame.image.load('night_club/assets/a-4.png').convert_alpha()
b_1 = pygame.image.load('night_club/assets/b-1.png').convert_alpha()
b_2 = pygame.image.load('night_club/assets/b-2.png').convert_alpha()
b_3 = pygame.image.load('night_club/assets/b-3.png').convert_alpha()
b_4 = pygame.image.load('night_club/assets/b-4.png').convert_alpha()
c_1 = pygame.image.load('night_club/assets/c-1.png').convert_alpha()
c_2 = pygame.image.load('night_club/assets/c-2.png').convert_alpha()
c_3 = pygame.image.load('night_club/assets/c-3.png').convert_alpha()
c_4 = pygame.image.load('night_club/assets/c-4.png').convert_alpha()
d_1 = pygame.image.load('night_club/assets/d-1.png').convert_alpha()
d_2 = pygame.image.load('night_club/assets/d-2.png').convert_alpha()
d_3 = pygame.image.load('night_club/assets/d-3.png').convert_alpha()
d_4 = pygame.image.load('night_club/assets/d-4.png').convert_alpha()


class scorereel():
    """ Score Reels are used to count replays """
    def __init__(self, pos, image):
        self.position = pos
        self.default_y = self.position[1]
        self.image = pygame.image.load(image).convert()

reel1 = scorereel([105,303], "graphics/assets/white_reel.png")
reel10 = scorereel([86,303], "graphics/assets/white_reel.png")
reel100 = scorereel([67,303], "graphics/assets/white_reel.png")

def display(s, replays=0, menu=False):
    
    meter.set_colorkey((255,0,252))
    meter_position = [58,303]

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
        screen.blit(bg_menu, backglass_position)
    else:
        if (s.game.anti_cheat.status == True):
            screen.blit(bg_gi, backglass_position)
        else:
            screen.blit(bg_off, backglass_position)

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
        p = [49,963]
        screen.blit(dt_arrow, p)
    elif s.game.red_line.position == 2:
        p = [48,931]
        screen.blit(dt_arrow, p)
    elif s.game.red_line.position == 3:
        p = [48,898]
        screen.blit(dt_arrow, p)
    elif s.game.red_line.position == 4:
        p = [49,868]
        screen.blit(dt_arrow, p)
    if s.game.red_line.position >= 5 and s.game.red_line.position < 10:
        p = [33,793]
        screen.blit(double, p)
    if s.game.red_line.position == 6:
        p = [50,758]
        screen.blit(dt_arrow, p)
    elif s.game.red_line.position == 7:
        p = [50,726]
        screen.blit(dt_arrow, p)
    elif s.game.red_line.position == 8:
        p = [50,694]
        screen.blit(dt_arrow, p)
    elif s.game.red_line.position == 9:
        p = [50,662]
        screen.blit(dt_arrow, p)
    if s.game.red_line.position >= 10 and s.game.red_line.position < 15:
        p = [30,583]
        screen.blit(triple, p)
    if s.game.red_line.position == 11:
        p = [50,547]
        screen.blit(dt_arrow, p)
    elif s.game.red_line.position == 12:
        p = [50,517]
        screen.blit(dt_arrow, p)
    elif s.game.red_line.position == 13:
        p = [50,484]
        screen.blit(dt_arrow, p)
    elif s.game.red_line.position == 14:
        p = [50,451]
        screen.blit(dt_arrow, p)
    if s.game.red_line.position == 15:
        p = [27,370]
        screen.blit(quadruple, p)


    if s.game.yellow_line.position == 1:
        p = [633,964]
        screen.blit(dt_arrow, p)
    elif s.game.yellow_line.position == 2:
        p = [633,931]
        screen.blit(dt_arrow, p)
    elif s.game.yellow_line.position == 3:
        p = [633,899]
        screen.blit(dt_arrow, p)
    elif s.game.yellow_line.position == 4:
        p = [634,869]
        screen.blit(dt_arrow, p)
    if s.game.yellow_line.position >= 5 and s.game.yellow_line.position < 10:
        p = [618,794]
        screen.blit(double, p)
    if s.game.yellow_line.position == 6:
        p = [636,759]
        screen.blit(dt_arrow, p)
    elif s.game.yellow_line.position == 7:
        p = [636,726]
        screen.blit(dt_arrow, p)
    elif s.game.yellow_line.position == 8:
        p = [636,694]
        screen.blit(dt_arrow, p)
    elif s.game.yellow_line.position == 9:
        p = [636,662]
        screen.blit(dt_arrow, p)
    if s.game.yellow_line.position >= 10 and s.game.yellow_line.position < 15:
        p = [615,584]
        screen.blit(triple, p)
    if s.game.yellow_line.position == 11:
        p = [636,548]
        screen.blit(dt_arrow, p)
    elif s.game.yellow_line.position == 12:
        p = [636,517]
        screen.blit(dt_arrow, p)
    elif s.game.yellow_line.position == 13:
        p = [636,485]
        screen.blit(dt_arrow, p)
    elif s.game.yellow_line.position == 14:
        p = [636,452]
        screen.blit(dt_arrow, p)
    if s.game.yellow_line.position == 15:
        p = [612,370]
        screen.blit(quadruple, p)

    if s.game.magic_squares_feature.position == 1:
        p = [119,652]
        screen.blit(ms_arrow, p)
    if s.game.magic_squares_feature.position == 2:
        p = [150,652]
        screen.blit(ms_arrow, p)
    if s.game.magic_squares_feature.position == 3:
        p = [181,652]
        screen.blit(ms_arrow, p)
    if s.game.magic_squares_feature.position == 4:
        p = [214,652]
        screen.blit(ms_arrow, p)
    if s.game.magic_squares_feature.position >= 5:
        p = [247,647]
        screen.blit(ms_abc, p)
    if s.game.magic_squares_feature.position >= 6:
        if 2 in s.holes:
            p = [408,651]
            screen.blit(ms_number, p)
        else:
            p = [457,651]
            screen.blit(ms_number, p)
    if s.game.magic_squares_feature.position == 7:
        p = [500,647]
        screen.blit(ms_d, p)

    if s.game.odds.position == 1:
        p = [120,777]
        screen.blit(odds1, p)
    elif s.game.odds.position == 2:
        p = [179,820]
        screen.blit(odds2, p)
    elif s.game.odds.position == 3:
        p = [249,777]
        screen.blit(odds3, p)
    elif s.game.odds.position == 4:
        p = [307,816]
        screen.blit(odds4, p)
    elif s.game.odds.position == 5:
        p = [377,816]
        screen.blit(odds5, p)
    elif s.game.odds.position == 6:
        p = [424,776]
        screen.blit(odds6, p)
    elif s.game.odds.position == 7:
        p = [497,814]
        screen.blit(odds7, p)
    elif s.game.odds.position == 8:
        p = [552,777]
        screen.blit(odds8, p)

    if s.game.magic_squares_feature.position >= 5:
        p = [166,371]
        screen.blit(ms_letter, p)
        p = [166,540]
        screen.blit(ms_letter, p)
        p = [500,372]
        screen.blit(ms_letter, p)
        if s.game.before_fourth.status == True:
            p = [134,707]
            screen.blit(time, p)
            if s.game.ball_count.position == 3:
                s.cancel_delayed(name="blink")
                blink([s,1,1])
            else:
                s.cancel_delayed(name="blink")
        elif s.game.before_fifth.status == True:
            p = [414,709]
            screen.blit(time, p)
            if s.game.ball_count.position == 4:
                s.cancel_delayed(name="blink")
                blink([s,1,1])
            else:
                s.cancel_delayed(name="blink")
        elif s.game.after_fifth.status == True:
            p = [500,709]
            screen.blit(time, p)
            if s.game.ball_count.position == 5:
                s.cancel_delayed(name="blink")
                blink([s,1,1])
            else:
                s.cancel_delayed(name="blink")
    if s.game.magic_squares_feature.position == 7:
        p = [500,540]
        screen.blit(ms_letter, p)

    if s.game.corners.status == True:
        p = [615,275]
        screen.blit(corners, p)

    if s.game.ballyhole.status == True:
        p = [539,275]
        screen.blit(ballyhole, p)

    if s.game.extra_ball.position >= 1:
        p = [140,1004]
        screen.blit(eb_number, p)
    if s.game.extra_ball.position >= 2:
        p = [189,1004]
        screen.blit(eb, p)
    if s.game.extra_ball.position >= 3:
        p = [257,1004]
        screen.blit(eb, p)
    if s.game.extra_ball.position >= 4:
        p = [325,1004]
        screen.blit(eb_number, p)
    if s.game.extra_ball.position >= 5:
        p = [375,1004]
        screen.blit(eb, p)
    if s.game.extra_ball.position >= 6:
        p = [444,1004]
        screen.blit(eb, p)
    if s.game.extra_ball.position >= 7:
        p = [511,1004]
        screen.blit(eb_number, p)
    if s.game.extra_ball.position >= 8:
        p = [560,1004]
        screen.blit(eb, p)
    if s.game.extra_ball.position == 9:
        p = [628,1004]
        screen.blit(eb, p)

    if s.game.eb_play.status == True:
        p = [26,1004]
        screen.blit(extra_balls, p)


    if s.game.tilt.status == True:
        tilt_position = [556,501]
        screen.blit(tilt, tilt_position)

    pygame.display.update()

def blink(args):
    dirty_rects = []
    s = args[0]
    b = args[1]
    sl = args[2]

    if b == 0:
        if sl == 1:
            p = [220,735]
            dirty_rects.append(screen.blit(select_now, p))
        pygame.display.update(dirty_rects)
    else:
        dirty_rects.append(screen.blit(bg_gi, (220,735), pygame.Rect(220,735,193,31)))
        pygame.display.update(dirty_rects)
    b = not b

    args = [s,b,sl]

    s.delay(name="blink", delay=0.1, handler=blink, param=args)

def squarea_animation(args):
    dirty_rects = []
    s = args[0]
    num = args[1]
    square = args[2]
    
    if square == 1:
        p = [217,337]
        if s.game.square_a.position == 0:
            image = a3
            topleft = a_2
            topright = a_4
            bottomleft = a_1
            bottomright = a_3
        elif s.game.square_a.position == 1:
            image = a0
            topleft = a_1
            topright = a_2
            bottomleft = a_3
            bottomright = a_4
        elif s.game.square_a.position == 2:
            image = a1
            topleft = a_3
            topright = a_1
            bottomleft = a_4
            bottomright = a_2
        else:
            image = a2
            topleft = a_4
            topright = a_3
            bottomleft = a_2
            bottomright = a_1
   

    rect = pygame.Rect(p[0],p[1],200,200)

    #letter A
    if square == 1: 
        dirty_rects.append(screen.blit(topleft, (236  - num - 20, 340)))
        dirty_rects.append(screen.blit(topright, (276, 345 - num - 10)))
        dirty_rects.append(screen.blit(bottomright, (269  + num + 15, 397)))
        dirty_rects.append(screen.blit(bottomleft, (223, 398 + num + 5)))

    if (s.game.anti_cheat.status == True):
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],130,130)))
    else:
        dirty_rects.append(screen.blit(bg_off, p, pygame.Rect(p[0],p[1],130,130)))
    
    if 2 in s.holes:
        number_position = [219,452]
        dirty_rects.append(screen.blit(bg_gi, number_position, pygame.Rect(number_position[0],number_position[1],49,50)))
        dirty_rects.append(screen.blit(number, number_position))
    if 16 in s.holes:
        number_position = [331,451]
        dirty_rects.append(screen.blit(bg_gi, number_position, pygame.Rect(number_position[0],number_position[1],49,50)))
        dirty_rects.append(screen.blit(number, number_position))
    if 18 in s.holes:
        number_position = [274,450]
        dirty_rects.append(screen.blit(bg_gi, number_position, pygame.Rect(number_position[0],number_position[1],49,50)))
        dirty_rects.append(screen.blit(number, number_position))
    if 24 in s.holes:
        number_position = [331,394]
        dirty_rects.append(screen.blit(bg_gi, number_position, pygame.Rect(number_position[0],number_position[1],49,50)))
        dirty_rects.append(screen.blit(number, number_position))
    if 25 in s.holes:
        number_position = [332,338]
        dirty_rects.append(screen.blit(bg_gi, number_position, pygame.Rect(number_position[0],number_position[1],49,50)))
        dirty_rects.append(screen.blit(number, number_position))

    if s.game.magic_squares_feature.position >= 5:
        p = [166,371]
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],53,51)))
        dirty_rects.append(screen.blit(ms_letter, p))
    pygame.display.update(dirty_rects)

def squareb_animation(args):
    dirty_rects = []
    s = args[0]
    num = args[1]
    square = args[2]
    
    if square == 2:
        p = [216,508]
        if s.game.square_b.position == 0:
            image = b3
            topleft = b_2
            topright = b_4
            bottomleft = b_1
            bottomright = b_3
        elif s.game.square_b.position == 1:
            image = b0
            topleft = b_1
            topright = b_2
            bottomleft = b_3
            bottomright = b_4
        elif s.game.square_b.position == 2:
            image = b1
            topleft = b_3
            topright = b_1
            bottomleft = b_4
            bottomright = b_2
        else:
            image = b2
            topleft = b_4
            topright = b_3
            bottomleft = b_2
            bottomright = b_1

    rect = pygame.Rect(p[0],p[1],200,200)

    if square == 2:
        dirty_rects.append(screen.blit(topleft, (232  - num - 20, 514)))
        dirty_rects.append(screen.blit(topright, (273, 516 - num - 9)))
        dirty_rects.append(screen.blit(bottomright, (269  + num + 15, 564)))
        dirty_rects.append(screen.blit(bottomleft, (223, 568 + num + 8)))
    
    if (s.game.anti_cheat.status == True):
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],130,130)))
    else:
        dirty_rects.append(screen.blit(bg_off, p, pygame.Rect(p[0],p[1],130,130)))
    
    if 2 in s.holes:
        number_position = [219,452]
        dirty_rects.append(screen.blit(bg_gi, number_position, pygame.Rect(number_position[0],number_position[1],49,50)))
        dirty_rects.append(screen.blit(number, number_position))
    if 5 in s.holes:
        number_position = [333,566]
        dirty_rects.append(screen.blit(bg_gi, number_position, pygame.Rect(number_position[0],number_position[1],49,50)))
        dirty_rects.append(screen.blit(number, number_position))
    if 13 in s.holes:
        number_position = [331,507]
        dirty_rects.append(screen.blit(bg_gi, number_position, pygame.Rect(number_position[0],number_position[1],49,50)))
        dirty_rects.append(screen.blit(number, number_position))
    if 18 in s.holes:
        number_position = [274,450]
        dirty_rects.append(screen.blit(bg_gi, number_position, pygame.Rect(number_position[0],number_position[1],49,50)))
        dirty_rects.append(screen.blit(number, number_position))

    if s.game.magic_squares_feature.position >= 5:
        p = [247,647]
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],151,47)))
        dirty_rects.append(screen.blit(ms_abc, p))
        p = [166,540]
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],53,51)))
        dirty_rects.append(screen.blit(ms_letter, p))

    pygame.display.update(dirty_rects)

def squarec_animation(args):
    dirty_rects = []
    s = args[0]
    num = args[1]
    square = args[2]
    
    if square == 3:
        p = [385,337]
        if s.game.square_c.position == 0:
            image = c3
            topleft = c_2
            topright = c_4
            bottomleft = c_1
            bottomright = c_3
        elif s.game.square_c.position == 1:
            image = c0
            topleft = c_1
            topright = c_2
            bottomleft = c_3
            bottomright = c_4
        elif s.game.square_c.position == 2:
            image = c1
            topleft = c_3
            topright = c_1
            bottomleft = c_4
            bottomright = c_2
        else:
            image = c2
            topleft = c_4
            topright = c_3
            bottomleft = c_2
            bottomright = c_1

    rect = pygame.Rect(p[0],p[1],200,200)

    if square == 3:
        dirty_rects.append(screen.blit(topleft, (394  - num - 10, 343)))
        dirty_rects.append(screen.blit(topright, (438, 337 - num + 0)))
        dirty_rects.append(screen.blit(bottomright, (432  + num + 20, 395)))
        dirty_rects.append(screen.blit(bottomleft, (392, 397 + num + 6)))
    
    if (s.game.anti_cheat.status == True):
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],130,130)))
    else:
        dirty_rects.append(screen.blit(bg_off, p, pygame.Rect(p[0],p[1],130,130)))
    
    if 11 in s.holes:
        number_position = [446,451]
        dirty_rects.append(screen.blit(bg_gi, number_position, pygame.Rect(number_position[0],number_position[1],49,50)))
        dirty_rects.append(screen.blit(number, number_position))
    if 12 in s.holes:
        number_position = [388,450]
        dirty_rects.append(screen.blit(bg_gi, number_position, pygame.Rect(number_position[0],number_position[1],49,50)))
        dirty_rects.append(screen.blit(number, number_position))
    if 24 in s.holes:
        number_position = [331,394]
        dirty_rects.append(screen.blit(bg_gi, number_position, pygame.Rect(number_position[0],number_position[1],49,50)))
        dirty_rects.append(screen.blit(number, number_position))
    if 25 in s.holes:
        number_position = [332,338]
        dirty_rects.append(screen.blit(bg_gi, number_position, pygame.Rect(number_position[0],number_position[1],49,50)))
        dirty_rects.append(screen.blit(number, number_position))

    if s.game.magic_squares_feature.position >= 5:
        p = [500,372]
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],53,51)))
        dirty_rects.append(screen.blit(ms_letter, p))

    pygame.display.update(dirty_rects)

def squared_animation(args):
    dirty_rects = []
    s = args[0]
    num = args[1]
    square = args[2]
    
    p = [390,509]
    if s.game.square_d.position == 0:
        image = d3
        topleft = d_2
        topright = d_4
        bottomleft = d_1
        bottomright = d_3
    elif s.game.square_d.position == 1:
        image = d0
        topleft = d_1
        topright = d_2
        bottomleft = d_3
        bottomright = d_4
    elif s.game.square_d.position == 2:
        image = d1
        topleft = d_3
        topright = d_1
        bottomleft = d_4
        bottomright = d_2
    else:
        image = d2
        topleft = d_4
        topright = d_3
        bottomleft = d_2
        bottomright = d_1

    rect = pygame.Rect(p[0],p[1],200,200)

    if square == 4:
        dirty_rects.append(screen.blit(topleft, (396 - num - 6, 514)))
        dirty_rects.append(screen.blit(topright, (442, 522 - num - 13)))
        dirty_rects.append(screen.blit(bottomright, (425  + num + 29, 564)))
        dirty_rects.append(screen.blit(bottomleft, (391, 563 + num + 12)))
    
    if (s.game.anti_cheat.status == True):
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],130,130)))
    else:
        dirty_rects.append(screen.blit(bg_off, p, pygame.Rect(p[0],p[1],130,130)))
    
    if 5 in s.holes:
        number_position = [333,566]
        dirty_rects.append(screen.blit(bg_gi, number_position, pygame.Rect(number_position[0],number_position[1],52,52)))
        dirty_rects.append(screen.blit(number, number_position))
    if 11 in s.holes:
        number_position = [446,451]
        dirty_rects.append(screen.blit(bg_gi, number_position, pygame.Rect(number_position[0],number_position[1],52,52)))
        dirty_rects.append(screen.blit(number, number_position))
    if 12 in s.holes:
        number_position = [388,450]
        dirty_rects.append(screen.blit(bg_gi, number_position, pygame.Rect(number_position[0],number_position[1],52,52)))
        dirty_rects.append(screen.blit(number, number_position))
    if 13 in s.holes:
        number_position = [331,507]
        dirty_rects.append(screen.blit(bg_gi, number_position, pygame.Rect(number_position[0],number_position[1],52,52)))
        dirty_rects.append(screen.blit(number, number_position))

    if s.game.magic_squares_feature.position >= 5:
        p = [500,540]
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],53,51)))
        dirty_rects.append(screen.blit(ms_letter, p))
    if s.game.magic_squares_feature.position >= 6:
        if 2 in s.holes:
            p = [408,651]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],32,32)))
            dirty_rects.append(screen.blit(ms_number, p))
        else:
            p = [457,651]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],32,32)))
            dirty_rects.append(screen.blit(ms_number, p))
    if s.game.magic_squares_feature.position == 7:
        p = [500,647]
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],97,47)))
        dirty_rects.append(screen.blit(ms_d, p))

    pygame.display.update(dirty_rects)

def eb_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]
    if s.game.extra_ball.position < 1:
        dirty_rects.append(screen.blit(bg_gi, (140,1004), pygame.Rect(140,1004,51,34)))
    if s.game.extra_ball.position < 2:
        dirty_rects.append(screen.blit(bg_gi, (189,1004), pygame.Rect(189,1004,67,34)))
    if s.game.extra_ball.position < 3:
        dirty_rects.append(screen.blit(bg_gi, (257,1004), pygame.Rect(257,1004,67,34)))
    if s.game.extra_ball.position < 4:
        dirty_rects.append(screen.blit(bg_gi, (325,1004), pygame.Rect(325,1004,51,34)))
    if s.game.extra_ball.position < 5:
        dirty_rects.append(screen.blit(bg_gi, (375,1004), pygame.Rect(375,1004,67,34)))
    if s.game.extra_ball.position < 6:
        dirty_rects.append(screen.blit(bg_gi, (444,1004), pygame.Rect(444,1004,67,34)))
    if s.game.extra_ball.position < 7:
        dirty_rects.append(screen.blit(bg_gi, (511,1004), pygame.Rect(511,1004,51,34)))
    if s.game.extra_ball.position < 8:
        dirty_rects.append(screen.blit(bg_gi, (560,1004), pygame.Rect(560,1004,67,34)))
    if s.game.extra_ball.position < 9:
        dirty_rects.append(screen.blit(bg_gi, (628,1004), pygame.Rect(628,1004,67,34)))

    pygame.display.update(dirty_rects)

    if num in [0,24,25,49]:
        if s.game.extra_ball.position < 1:
            p = [140,1004]
            dirty_rects.append(screen.blit(eb_number, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [1,15,26,40]:
        if s.game.extra_ball.position < 2:
            p = [189,1004]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [3,4,17,28,29,42]:
        if s.game.extra_ball.position < 3:
            p = [257,1004]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [5,18,30,43]:
        if s.game.extra_ball.position < 4:
            p = [325,1004]
            dirty_rects.append(screen.blit(eb_number, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [7,8,19,32,33,44]:
        if s.game.extra_ball.position < 5:
            p = [375,1004]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [9,10,20,34,35,45]:
        if s.game.extra_ball.position < 6:
            p = [444,1004]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [11,21,36,46]:
        if s.game.extra_ball.position < 7:
            p = [511,1004]
            dirty_rects.append(screen.blit(eb_number, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [12,22,37,47]:
        if s.game.extra_ball.position < 8:
            p = [560,1004]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [2,6,13,16,23,27,31,38,41,48]:
        if s.game.extra_ball.position < 9:
            p = [628,1004]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects) 
            return

def clear_odds(s, num):
    global screen

    dirty_rects = []

    if s.game.odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (120,777), pygame.Rect(120,777,41,162)))
    if s.game.odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (179,820), pygame.Rect(179,820,33,88)))
    if s.game.odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (249,777), pygame.Rect(249,777,40,162)))
    if s.game.odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (307,816), pygame.Rect(307,816,35,92)))
    if s.game.odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (377,816), pygame.Rect(377,816,39,92)))
    if s.game.odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (424,776), pygame.Rect(424,776,50,165)))
    if s.game.odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (497,814), pygame.Rect(497,814,40,93)))
    if s.game.odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (552,777), pygame.Rect(552,777,51,169)))

    pygame.display.update(dirty_rects)

def draw_odds_animation(s, num):
    global screen
    dirty_rects = []

    if num in [2,3,12,27,28,37]:
        if s.game.odds.position != 1:
            p = [120,777]
            dirty_rects.append(screen.blit(odds1, p))
            pygame.display.update(dirty_rects)
            return
    if num in [13,14,38,39]:
        if s.game.odds.position != 2:
            p = [179,820]
            dirty_rects.append(screen.blit(odds2, p))
            pygame.display.update(dirty_rects)
            return
    if num in [4,5,15,16,29,30,40,41]:
        if s.game.odds.position != 3:
            p = [249,777]
            dirty_rects.append(screen.blit(odds3, p))
            pygame.display.update(dirty_rects)
            return
    if num in [17,18,42,43]:
        if s.game.odds.position != 4:
            p = [307,816]
            dirty_rects.append(screen.blit(odds4, p))
            pygame.display.update(dirty_rects)
            return
    if num in [6,7,19,20,31,32,44,45]:
        if s.game.odds.position != 5:
            p = [377,816]
            dirty_rects.append(screen.blit(odds5, p))
            pygame.display.update(dirty_rects)
            return
    if num in [21,22,46,47]:
        if s.game.odds.position != 6:
            p = [424,776]
            dirty_rects.append(screen.blit(odds6, p))
            pygame.display.update(dirty_rects)
            return
    if num in [8,9,23,24,33,34,48,49]:
        if s.game.odds.position != 7:
            p = [497,814]
            dirty_rects.append(screen.blit(odds7, p))
            pygame.display.update(dirty_rects)
            return
    if num in [10,11,25,26,0,35,36,50]:
        if s.game.odds.position != 8:
            p = [552,777]
            dirty_rects.append(screen.blit(odds8, p))
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

    if s.game.magic_squares_feature.position < 5:
        dirty_rects.append(screen.blit(bg_gi, (247,647), pygame.Rect(247,647,151,47)))
        dirty_rects.append(screen.blit(bg_gi, (166,371), pygame.Rect(166,371,53,51)))
        dirty_rects.append(screen.blit(bg_gi, (166,540), pygame.Rect(166,540,53,51)))
        dirty_rects.append(screen.blit(bg_gi, (500,372), pygame.Rect(500,372,53,51)))
    if s.game.magic_squares_feature.position < 6:
        if 2 not in s.holes:
            dirty_rects.append(screen.blit(bg_gi, (408,651), pygame.Rect(408,651,32,32)))
        if 18 not in s.holes:
            dirty_rects.append(screen.blit(bg_gi, (457,651), pygame.Rect(457,651,32,32)))
    if s.game.before_fourth.status == False or s.game.magic_squares_feature.position < 5:
        dirty_rects.append(screen.blit(bg_gi, (134,707), pygame.Rect(134,707,85,60)))
    if s.game.before_fifth.status == False:
        dirty_rects.append(screen.blit(bg_gi, (414,709), pygame.Rect(414,709,85,60)))
    if s.game.after_fifth.status == False:
        dirty_rects.append(screen.blit(bg_gi, (500,709), pygame.Rect(500,709,85,60)))
    if s.game.magic_squares_feature.position < 7:
        dirty_rects.append(screen.blit(bg_gi, (500,647), pygame.Rect(500,647,97,47)))
        dirty_rects.append(screen.blit(bg_gi, (500,540), pygame.Rect(500,540,53,51)))
    if s.game.corners.status == False:
        dirty_rects.append(screen.blit(bg_gi, (615,275), pygame.Rect(615,275,74,74)))
    if s.game.ballyhole.status == False:
        dirty_rects.append(screen.blit(bg_gi, (539,275), pygame.Rect(539,275,74,74)))
    if s.game.yellow_line.position < 5:
        dirty_rects.append(screen.blit(bg_gi, (618,794), pygame.Rect(618,794,70,71)))
    if s.game.yellow_line.position < 10:
        dirty_rects.append(screen.blit(bg_gi, (615,584), pygame.Rect(615,584,75,75)))
    if s.game.yellow_line.position < 15:
        dirty_rects.append(screen.blit(bg_gi, (612,370), pygame.Rect(612,370,82,79)))
    if s.game.red_line.position < 5:
        dirty_rects.append(screen.blit(bg_gi, (33,793), pygame.Rect(33,793,70,71)))
    if s.game.red_line.position < 10:
        dirty_rects.append(screen.blit(bg_gi, (30,583), pygame.Rect(30,583,75,75)))
    if s.game.red_line.position < 15:
        dirty_rects.append(screen.blit(bg_gi, (27,370), pygame.Rect(27,370,82,79)))
    pygame.display.update(dirty_rects)


def draw_feature_animation(s, num):
    global screen
    dirty_rects = []
 
    if num in [13,14,38,39]:
        if s.game.magic_squares_feature.position < 5:
            p = [247,647]
            dirty_rects.append(screen.blit(ms_abc, p))
            p = [166,371]
            dirty_rects.append(screen.blit(ms_letter, p))
            p = [166,540]
            dirty_rects.append(screen.blit(ms_letter, p))
            p = [500,372]
            dirty_rects.append(screen.blit(ms_letter, p))
            pygame.display.update(dirty_rects)
            return
        if s.game.before_fourth.status == False or s.game.magic_squares_feature.position < 5:
            p = [134,707]
            dirty_rects.append(screen.blit(time, p))
            pygame.display.update(dirty_rects)
            return
    if num in [19,20,44,45]:
        if s.game.before_fifth.status == False:
            p = [414,709]
            dirty_rects.append(screen.blit(time, p))
            pygame.display.update(dirty_rects)
            return
    if num in [21,22,46,47]:
        if s.game.after_fifth.status == False:
            p = [500,709]
            dirty_rects.append(screen.blit(time, p))
            pygame.display.update(dirty_rects)
            return
    if num in [15,16,40,41]:
        if s.game.magic_squares_feature.position < 6:
            if 2 not in s.holes:
                p = [408,651]
                dirty_rects.append(screen.blit(ms_number, p))
                pygame.display.update(dirty_rects)
                return
            if 18 not in s.holes:
                p = [457,651]
                dirty_rects.append(screen.blit(ms_number, p))
                pygame.display.update(dirty_rects)
                return
    if num in [17,18,42,43]:
        if s.game.magic_squares_feature.position < 7:
            p = [500,647]
            dirty_rects.append(screen.blit(ms_d, p))
            p = [500,540]
            dirty_rects.append(screen.blit(ms_letter, p))
            pygame.display.update(dirty_rects)
            return
    if num in [23,48]:
        if s.game.corners.status == False:
            p = [615,275]
            dirty_rects.append(screen.blit(corners, p))
            pygame.display.update(dirty_rects)
            return
    if num in [24,49]:
        if s.game.ballyhole.status == False:
            p = [539,275]
            dirty_rects.append(screen.blit(ballyhole, p))
            pygame.display.update(dirty_rects)
            return
    if num in [7,8,32,33]:
        if s.game.yellow_line.position < 5:
            p = [618,794]
            dirty_rects.append(screen.blit(double, p))
            pygame.display.update(dirty_rects)
            return
    if num in [9,10,34,35]:
        if s.game.yellow_line.position < 10:
            p = [615,584]
            dirty_rects.append(screen.blit(triple, p))
            pygame.display.update(dirty_rects)
            return
    if num in [11,12,36,37]:
        if s.game.yellow_line.position < 15:
            p = [612,370]
            dirty_rects.append(screen.blit(quadruple, p))
            pygame.display.update(dirty_rects)
            return
    if num in [1,2,26,27]:
        if s.game.red_line.position < 5:
            p = [33,793]
            dirty_rects.append(screen.blit(double, p))
            pygame.display.update(dirty_rects)
            return
    if num in [3,4,28,29]:
        if s.game.red_line.position < 10:
            p = [30,583]
            dirty_rects.append(screen.blit(triple, p))
            pygame.display.update(dirty_rects)
    if num in [5,6,30,31]:
        if s.game.red_line.position < 15:
            p = [27,370]
            dirty_rects.append(screen.blit(quadruple, p))
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


