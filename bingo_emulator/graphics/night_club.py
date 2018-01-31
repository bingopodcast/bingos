
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

def eb_animation(num):
    global screen
    if num == 9:
        p = [140,1004]
        screen.blit(eb_number, p)
        pygame.display.update()
    if num == 8:
        p = [189,1004]
        screen.blit(eb, p)
        pygame.display.update()
    if num == 7:
        p = [257,1004]
        screen.blit(eb, p)
        pygame.display.update()
    if num == 6:
        p = [325,1004]
        screen.blit(eb_number, p)
        pygame.display.update()
    if num == 5:
        p = [375,1004]
        screen.blit(eb, p)
        pygame.display.update()
    if num == 4:
        p = [444,1004]
        screen.blit(eb, p)
        pygame.display.update()
    if num == 3:
        p = [511,1004]
        screen.blit(eb_number, p)
        pygame.display.update()
    if num == 2:
        p = [560,1004]
        screen.blit(eb, p)
        pygame.display.update()
    if num == 1:
        p = [628,1004]
        screen.blit(eb, p)
        pygame.display.update()


def feature_animation(num):
    global screen
    if num == 6:
        p = [615,275]
        screen.blit(corners, p)
        pygame.display.update()

    if num == 3:
        p = [247,647]
        screen.blit(ms_abc, p)
        pygame.display.update()
   

def odds_animation(num):
    global screen
    if num == 5:
        p = [120,777]
        screen.blit(odds1, p)
        pygame.display.update()
    if num == 4:
        p = [179,820]
        screen.blit(odds2, p)
        pygame.display.update()
    if num == 3:
        p = [249,777]
        screen.blit(odds3, p)
        pygame.display.update()
    if num == 2:
        p = [307,816]
        screen.blit(odds4, p)
        pygame.display.update()
    if num == 1:
        p = [377,816]
        screen.blit(odds5, p)
        pygame.display.update()
