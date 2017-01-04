
import pygame

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

meter = pygame.image.load('graphics/assets/register_cover.png').convert()
number = pygame.image.load('parade/assets/number.png').convert_alpha()
ms_letter = pygame.image.load('parade/assets/ms_letter.png').convert_alpha()
ms_number = pygame.image.load('parade/assets/ms_number.png').convert_alpha()
ms_arrow = pygame.image.load('parade/assets/ms_arrow.png').convert_alpha()
ms_abc = pygame.image.load('parade/assets/ms_abc.png').convert_alpha()
ms_d = pygame.image.load('parade/assets/ms_d.png').convert_alpha()
select_now = pygame.image.load('parade/assets/select_now.png').convert_alpha()
dt_arrow = pygame.image.load('parade/assets/dt_arrow.png').convert_alpha()
double = pygame.image.load('parade/assets/double.png').convert_alpha()
triple = pygame.image.load('parade/assets/triple.png').convert_alpha()
quadruple = pygame.image.load('parade/assets/quadruple.png').convert_alpha()
corners = pygame.image.load('parade/assets/corners.png').convert_alpha()
ballyhole = pygame.image.load('parade/assets/corners.png').convert_alpha()
odds1 = pygame.image.load('parade/assets/odds1.png').convert_alpha()
odds2 = pygame.image.load('parade/assets/odds2.png').convert_alpha()
odds3 = pygame.image.load('parade/assets/odds3.png').convert_alpha()
odds4 = pygame.image.load('parade/assets/odds4.png').convert_alpha()
odds5 = pygame.image.load('parade/assets/odds5.png').convert_alpha()
odds6 = pygame.image.load('parade/assets/odds6.png').convert_alpha()
odds7 = pygame.image.load('parade/assets/odds7.png').convert_alpha()
odds8 = pygame.image.load('parade/assets/odds8.png').convert_alpha()
extra_balls = pygame.image.load('parade/assets/extra_balls.png').convert_alpha()
eb = pygame.image.load('parade/assets/eb.png').convert_alpha()
eb_number = pygame.image.load('parade/assets/eb_number.png').convert_alpha()
tilt = pygame.image.load('parade/assets/tilt.png').convert_alpha()
time = pygame.image.load('parade/assets/time.png').convert_alpha()
a0 = pygame.image.load('parade/assets/a0.png').convert_alpha()
a1 = pygame.image.load('parade/assets/a1.png').convert_alpha()
a2 = pygame.image.load('parade/assets/a2.png').convert_alpha()
a3 = pygame.image.load('parade/assets/a3.png').convert_alpha()
b0 = pygame.image.load('parade/assets/b0.png').convert_alpha()
b1 = pygame.image.load('parade/assets/b1.png').convert_alpha()
b2 = pygame.image.load('parade/assets/b2.png').convert_alpha()
b3 = pygame.image.load('parade/assets/b3.png').convert_alpha()
c0 = pygame.image.load('parade/assets/c0.png').convert_alpha()
c1 = pygame.image.load('parade/assets/c1.png').convert_alpha()
c2 = pygame.image.load('parade/assets/c2.png').convert_alpha()
c3 = pygame.image.load('parade/assets/c3.png').convert_alpha()
d0 = pygame.image.load('parade/assets/d0.png').convert_alpha()
d1 = pygame.image.load('parade/assets/d1.png').convert_alpha()
d2 = pygame.image.load('parade/assets/d2.png').convert_alpha()
d3 = pygame.image.load('parade/assets/d3.png').convert_alpha()
line = pygame.image.load('parade/assets/line.png').convert_alpha()
extra = pygame.image.load('parade/assets/extra.png').convert_alpha()
bottom_line = pygame.image.load('parade/assets/bottom_line.png').convert_alpha()

class scorereel():
    """ Score Reels are used to count replays """
    def __init__(self, pos, image):
        self.position = pos
        self.default_y = self.position[1]
        self.image = pygame.image.load(image).convert()

reel1 = scorereel([105,295], "graphics/assets/white_reel.png")
reel10 = scorereel([86,295], "graphics/assets/white_reel.png")
reel100 = scorereel([67,295], "graphics/assets/white_reel.png")

def display(s, replays=0, menu=False):
    
    meter.set_colorkey((255,0,252))
    meter_position = [58,295]

    screen.blit(reel1.image, reel1.position)
    screen.blit(reel10.image, reel10.position)
    screen.blit(reel100.image, reel100.position)
    screen.blit(meter, meter_position)

    if s.game.square_a.position == 0:
        p = [218,412]
        screen.blit(a0, p)
    if s.game.square_a.position == 1:
        p = [218,412]
        screen.blit(a1, p)
    if s.game.square_a.position == 2:
        p = [218,412]
        screen.blit(a2, p)
    if s.game.square_a.position == 3:
        p = [218,412]
        screen.blit(a3, p)
    if s.game.square_b.position == 0:
        p = [217,590]
        screen.blit(b0, p)
    if s.game.square_b.position == 1:
        p = [217,590]
        screen.blit(b1, p)
    if s.game.square_b.position == 2:
        p = [217,590]
        screen.blit(b2, p)
    if s.game.square_b.position == 3:
        p = [217,590]
        screen.blit(b3, p)
    if s.game.square_c.position == 0:
        p = [393,412]
        screen.blit(c0, p)
    if s.game.square_c.position == 1:
        p = [393,412]
        screen.blit(c1, p)
    if s.game.square_c.position == 2:
        p = [393,412]
        screen.blit(c2, p)
    if s.game.square_c.position == 3:
        p = [393,412]
        screen.blit(c3, p)
    if s.game.square_d.position == 0:
        p = [391,592]
        screen.blit(d0, p)
    if s.game.square_d.position == 1:
        p = [391,592]
        screen.blit(d1, p)
    if s.game.square_d.position == 2:
        p = [391,592]
        screen.blit(d2, p)
    if s.game.square_d.position == 3:
        p = [391,592]
        screen.blit(d3, p)


    backglass_position = [0, 0]
    backglass = pygame.Surface(screen.get_size(), flags=pygame.SRCALPHA)
    backglass.fill((0, 0, 0))
    if menu == True:
        backglass = pygame.image.load('parade/assets/parade_menu.png')
    else:
        if (s.game.anti_cheat.status == True):
            backglass = pygame.image.load('parade/assets/parade_gi.png')
        else:
            backglass = pygame.image.load('parade/assets/parade_off.png')
    backglass = pygame.transform.scale(backglass, (720, 1280))
    
    screen.blit(backglass, backglass_position)

    if s.game.top_line.status == True:
        p = [17,944]
        screen.blit(line, p)
    else:
        p = [226,360]
        screen.blit(extra, p)

    if s.game.bottom_line.status == True:
        p = [106,946]
        screen.blit(line, p)
        p = [226,714]
        screen.blit(bottom_line, p)
    else:
        p = [222,714]
        screen.blit(extra, p)

    if s.game.tilt.status == False:
        if s.holes:
            if 1 in s.holes:
                if s.game.square_a.position == 0:
                    p = [223,477]
                    screen.blit(number, p)
                elif s.game.square_a.position == 1:
                    p = [224,418]
                    screen.blit(number, p)
                elif s.game.square_a.position == 2:
                    p = [281,417]
                    screen.blit(number, p)
                else:
                    p = [280,476]
                    screen.blit(number, p)
            if 2 in s.holes:
                number_position = [221,535]
                screen.blit(number, number_position)
            if 3 in s.holes:
                if s.game.square_d.position == 0:
                    p = [453,594]
                    screen.blit(number, p)
                elif s.game.square_d.position == 1:
                    p = [453,653]
                    screen.blit(number, p)
                elif s.game.square_d.position == 2:
                    p = [393,653]
                    screen.blit(number, p)
                else:
                    p = [397,595]
                    screen.blit(number, p)
                if s.game.bottom_line.status == True:
                    p = [337,713]
                    screen.blit(number, p)
            if 4 in s.holes:
                if s.game.square_a.position == 0:
                    p = [281,417]
                    screen.blit(number, p)
                elif s.game.square_a.position == 1:
                    p = [281,477]
                    screen.blit(number, p)
                elif s.game.square_a.position == 2:
                    p = [223,476]
                    screen.blit(number, p)
                else:
                    p = [225,417]
                    screen.blit(number, p)
            if 5 in s.holes:
                number_position = [337,651]
                screen.blit(number, number_position)
                if s.game.bottom_line.status == True:
                    p = [221,713]
                    screen.blit(number, p)
            if 6 in s.holes:
                if s.game.square_c.position == 0:
                    p = [455,416]
                    screen.blit(number, p)
                elif s.game.square_c.position == 1:
                    p = [454,475]
                    screen.blit(number, p)
                elif s.game.square_c.position == 2:
                    p = [397,475]
                    screen.blit(number, p)
                else:
                    p = [397,417]
                    screen.blit(number, p)
                if s.game.top_line.status == True:
                    p = [225,360]
                    screen.blit(number, p)
            if 7 in s.holes:
                if s.game.square_d.position == 0:
                    p = [395,653]
                    screen.blit(number, p)
                elif s.game.square_d.position == 1:
                    p = [395,595]
                    screen.blit(number, p)
                elif s.game.square_d.position == 2:
                    p = [452,593]
                    screen.blit(number, p)
                else:
                    p = [453,653]
                    screen.blit(number, p)
                if s.game.top_line.status == True:
                    p = [283,359]
                    screen.blit(number, p)
            if 8 in s.holes:
                if s.game.square_c.position == 0:
                    p = [453,476]
                    screen.blit(number, p)
                elif s.game.square_c.position == 1:
                    p = [397,476]
                    screen.blit(number, p)
                elif s.game.square_c.position == 2:
                    p = [397,417]
                    screen.blit(number, p)
                else:
                    p = [455,417]
                    screen.blit(number, p)
                if s.game.bottom_line.status == True:
                    p = [278,713]
                    screen.blit(number, p)
            if 9 in s.holes:
                if s.game.square_a.position == 0:
                    p = [224,417]
                    screen.blit(number, p)
                elif s.game.square_a.position == 1:
                    p = [282,418]
                    screen.blit(number, p)
                elif s.game.square_a.position == 2:
                    p = [281,475]
                    screen.blit(number, p)
                else:
                    p = [224,477]
                    screen.blit(number, p)
            if 10 in s.holes:
                if s.game.square_b.position == 0:
                    p = [223,595]
                    screen.blit(number, p)
                elif s.game.square_b.position == 1:
                    p = [279,594]
                    screen.blit(number, p)
                elif s.game.square_b.position == 2:
                    p = [279,652]
                    screen.blit(number, p)
                else:
                    p = [221,653]
                    screen.blit(number, p)
            if 11 in s.holes:
                number_position = [455,535]
                screen.blit(number, number_position)
            if 12 in s.holes:
                number_position = [398,534]
                screen.blit(number, number_position)
            if 13 in s.holes:
                number_position = [338,595]
                screen.blit(number, number_position)
                if s.game.top_line.status == True:
                    p = [340,359]
                    screen.blit(number, p)
            if 14 in s.holes:
                if s.game.square_c.position == 0:
                    p = [397,416]
                    screen.blit(number, p)
                elif s.game.square_c.position == 1:
                    p = [455,416]
                    screen.blit(number, p)
                elif s.game.square_c.position == 2:
                    p = [454,476]
                    screen.blit(number, p)
                else:
                    p = [397,475]
                    screen.blit(number, p)
            if 15 in s.holes:
                if s.game.square_b.position == 0:
                    p = [221,653]
                    screen.blit(number, p)
                elif s.game.square_b.position == 1:
                    p = [223,594]
                    screen.blit(number, p)
                elif s.game.square_b.position == 2:
                    p = [281,594]
                    screen.blit(number, p)
                else:
                    p = [279,652]
                    screen.blit(number, p)
            if 16 in s.holes:
                number_position = [339,536]
                screen.blit(number, number_position)
            if 17 in s.holes:
                if s.game.square_d.position == 0:
                    p = [453,654]
                    screen.blit(number, p)
                elif s.game.square_d.position == 1:
                    p = [395,655]
                    screen.blit(number, p)
                elif s.game.square_d.position == 2:
                    p = [396,594]
                    screen.blit(number, p)
                else:
                    p = [453,594]
                    screen.blit(number, p)
                if s.game.top_line.status == True:
                    p = [455,360]
                    screen.blit(number, p)
            if 18 in s.holes:
                number_position = [281,537]
                screen.blit(number, number_position)
                if s.game.top_line.status == True:
                    p = [397,358]
                    screen.blit(number, p)
            if 19 in s.holes:
                if s.game.square_a.position == 0:
                    p = [281,477]
                    screen.blit(number, p)
                elif s.game.square_a.position == 1:
                    p = [224,477]
                    screen.blit(number, p)
                elif s.game.square_a.position == 2:
                    p = [225,418]
                    screen.blit(number, p)
                else:
                    p = [282,418]
                    screen.blit(number, p)
                if s.game.bottom_line.status == True:
                    p = [395,714]
                    screen.blit(number, p)
            if 20 in s.holes:
                if s.game.square_c.position == 0:
                    p = [397,477]
                    screen.blit(number, p)
                elif s.game.square_c.position == 1:
                    p = [397,417]
                    screen.blit(number, p)
                elif s.game.square_c.position == 2:
                    p = [456,417]
                    screen.blit(number, p)
                else:
                    p = [455,476]
                    screen.blit(number, p)
            if 21 in s.holes:
                if s.game.square_d.position == 0:
                    p = [397,594]
                    screen.blit(number, p)
                elif s.game.square_d.position == 1:
                    p = [453,594]
                    screen.blit(number, p)
                elif s.game.square_d.position == 2:
                    p = [453,653]
                    screen.blit(number, p)
                else:
                    p = [395,654]
                    screen.blit(number, p)
            if 22 in s.holes:
                if s.game.square_b.position == 0:
                    p = [280,593]
                    screen.blit(number, p)
                elif s.game.square_b.position == 1:
                    p = [279,652]
                    screen.blit(number, p)
                elif s.game.square_b.position == 2:
                    p = [221,653]
                    screen.blit(number, p)
                else:
                    p = [223,594]
                    screen.blit(number, p)
                if s.game.bottom_line.status == True:
                    p = [453,714]
                    screen.blit(number, p)
            if 23 in s.holes:
                if s.game.square_b.position == 0:
                    p = [280,653]
                    screen.blit(number, p)
                elif s.game.square_b.position == 1:
                    p = [221,654]
                    screen.blit(number, p)
                elif s.game.square_b.position == 2:
                    p = [223,594]
                    screen.blit(number, p)
                else:
                    p = [279,593]
                    screen.blit(number, p)
            if 24 in s.holes:
                number_position = [339,477]
                screen.blit(number, number_position)
            if 25 in s.holes:
                number_position = [340,419]
                screen.blit(number, number_position)

    if s.game.red_line.position == 1:
        p = [567,912]
        screen.blit(dt_arrow, p)
    elif s.game.red_line.position == 2:
        p = [567,883]
        screen.blit(dt_arrow, p)
    elif s.game.red_line.position == 3:
        p = [567,852]
        screen.blit(dt_arrow, p)
    elif s.game.red_line.position == 4:
        p = [568,821]
        screen.blit(dt_arrow, p)
    if s.game.red_line.position >= 5 and s.game.red_line.position < 10:
        p = [546,742]
        screen.blit(double, p)
    if s.game.red_line.position == 6:
        p = [567,707]
        screen.blit(dt_arrow, p)
    elif s.game.red_line.position == 7:
        p = [569,675]
        screen.blit(dt_arrow, p)
    elif s.game.red_line.position == 8:
        p = [569,644]
        screen.blit(dt_arrow, p)
    elif s.game.red_line.position == 9:
        p = [569,613]
        screen.blit(dt_arrow, p)
    if s.game.red_line.position >= 10 and s.game.red_line.position < 15:
        p = [549,534]
        screen.blit(triple, p)
    if s.game.red_line.position == 11:
        p = [571,497]
        screen.blit(dt_arrow, p)
    elif s.game.red_line.position == 12:
        p = [571,464]
        screen.blit(dt_arrow, p)
    elif s.game.red_line.position == 13:
        p = [571,433]
        screen.blit(dt_arrow, p)
    elif s.game.red_line.position == 14:
        p = [571,403]
        screen.blit(dt_arrow, p)
    if s.game.red_line.position == 15:
        p = [549,325]
        screen.blit(quadruple, p)


    if s.game.green_line.position == 1:
        p = [648,915]
        screen.blit(dt_arrow, p)
    elif s.game.green_line.position == 2:
        p = [649,882]
        screen.blit(dt_arrow, p)
    elif s.game.green_line.position == 3:
        p = [649,849]
        screen.blit(dt_arrow, p)
    elif s.game.green_line.position == 4:
        p = [650,821]
        screen.blit(dt_arrow, p)
    if s.game.green_line.position >= 5 and s.game.green_line.position < 10:
        p = [627,742]
        screen.blit(double, p)
    if s.game.green_line.position == 6:
        p = [651,706]
        screen.blit(dt_arrow, p)
    elif s.game.green_line.position == 7:
        p = [651,673]
        screen.blit(dt_arrow, p)
    elif s.game.green_line.position == 8:
        p = [650,643]
        screen.blit(dt_arrow, p)
    elif s.game.green_line.position == 9:
        p = [651,612]
        screen.blit(dt_arrow, p)
    if s.game.green_line.position >= 10 and s.game.green_line.position < 15:
        p = [630,534]
        screen.blit(triple, p)
    if s.game.green_line.position == 11:
        p = [653,496]
        screen.blit(dt_arrow, p)
    elif s.game.green_line.position == 12:
        p = [653,466]
        screen.blit(dt_arrow, p)
    elif s.game.green_line.position == 13:
        p = [653,433]
        screen.blit(dt_arrow, p)
    elif s.game.green_line.position == 14:
        p = [653,402]
        screen.blit(dt_arrow, p)
    if s.game.green_line.position == 15:
        p = [629,327]
        screen.blit(quadruple, p)

    if s.game.magic_squares_feature.position == 1:
        p = [199,963]
        screen.blit(ms_arrow, p)
    if s.game.magic_squares_feature.position == 2:
        p = [227,963]
        screen.blit(ms_arrow, p)
    if s.game.magic_squares_feature.position == 3:
        p = [258,963]
        screen.blit(ms_arrow, p)
    if s.game.magic_squares_feature.position == 4:
        p = [290,963]
        screen.blit(ms_arrow, p)
    if s.game.magic_squares_feature.position >= 5:
        p = [321,961]
        screen.blit(ms_abc, p)
    if s.game.magic_squares_feature.position == 6:
        p = [447,961]
        screen.blit(ms_d, p)

    if s.game.odds.position == 1:
        p = [28,869]
        screen.blit(odds1, p)
    elif s.game.odds.position == 2:
        p = [35,774]
        screen.blit(odds2, p)
    elif s.game.odds.position == 3:
        p = [21,713]
        screen.blit(odds3, p)
    elif s.game.odds.position == 4:
        p = [31,639]
        screen.blit(odds4, p)
    elif s.game.odds.position == 5:
        p = [31,582]
        screen.blit(odds5, p)
    elif s.game.odds.position == 6:
        p = [27,519]
        screen.blit(odds6, p)
    elif s.game.odds.position == 7:
        p = [29,457]
        screen.blit(odds7, p)
    elif s.game.odds.position == 8:
        p = [24,394]
        screen.blit(odds8, p)

    if s.game.magic_squares_feature.position >= 5:
        p = [167,446]
        screen.blit(ms_letter, p)
        p = [165,622]
        screen.blit(ms_letter, p)
        p = [507,446]
        screen.blit(ms_letter, p)
        if s.game.before_fourth.status == True:
            p = [525,951]
            screen.blit(time, p)
            if s.game.ball_count.position == 3:
                p = [257,925]
                screen.blit(select_now, p)
        elif s.game.before_fifth.status == True:
            p = [614,950]
            screen.blit(time, p)
            if s.game.ball_count.position == 4:
                p = [257,925]
                screen.blit(select_now, p)
    if s.game.magic_squares_feature.position == 6:
        p = [507,623]
        screen.blit(ms_letter, p)

    if s.game.ballyhole.status == True:
        p = [592,243]
        screen.blit(ballyhole, p)

    if s.game.extra_ball.position >= 1:
        p = [140,1020]
        screen.blit(eb_number, p)
    if s.game.extra_ball.position >= 2:
        p = [189,1020]
        screen.blit(eb, p)
    if s.game.extra_ball.position >= 3:
        p = [257,1020]
        screen.blit(eb, p)
    if s.game.extra_ball.position >= 4:
        p = [325,1020]
        screen.blit(eb_number, p)
    if s.game.extra_ball.position >= 5:
        p = [375,1020]
        screen.blit(eb, p)
    if s.game.extra_ball.position >= 6:
        p = [444,1020]
        screen.blit(eb, p)
    if s.game.extra_ball.position >= 7:
        p = [511,1020]
        screen.blit(eb_number, p)
    if s.game.extra_ball.position >= 8:
        p = [560,1020]
        screen.blit(eb, p)
    if s.game.extra_ball.position == 9:
        p = [628,1020]
        screen.blit(eb, p)

    if s.game.eb_play.status == True:
        p = [24,1014]
        screen.blit(extra_balls, p)


    if s.game.tilt.status == True:
        tilt_position = [463,801]
        screen.blit(tilt, tilt_position)

    pygame.display.flip()
    pygame.display.update()

def eb_animation(num):
    global screen
    if num == 9:
        p = [140,1020]
        screen.blit(eb_number, p)
        pygame.display.update()
    if num == 8:
        p = [189,1020]
        screen.blit(eb, p)
        pygame.display.update()
    if num == 7:
        p = [257,1020]
        screen.blit(eb, p)
        pygame.display.update()
    if num == 6:
        p = [325,1020]
        screen.blit(eb_number, p)
        pygame.display.update()
    if num == 5:
        p = [375,1020]
        screen.blit(eb, p)
        pygame.display.update()
    if num == 4:
        p = [444,1020]
        screen.blit(eb, p)
        pygame.display.update()
    if num == 3:
        p = [511,1020]
        screen.blit(eb_number, p)
        pygame.display.update()
    if num == 2:
        p = [560,1020]
        screen.blit(eb, p)
        pygame.display.update()
    if num == 1:
        p = [628,1020]
        screen.blit(eb, p)
        pygame.display.update()


def feature_animation(num):
    global screen
    if num == 6:
        p = [592,243]
        screen.blit(ballyhole, p)
        pygame.display.update()

    if num == 3:
        p = [321,961]
        screen.blit(ms_abc, p)
        pygame.display.update()
   

def odds_animation(num):
    global screen
    if num == 5:
        p = [28,869]
        screen.blit(odds1, p)
        pygame.display.update()
    if num == 4:
        p = [35,774]
        screen.blit(odds2, p)
        pygame.display.update()
    if num == 3:
        p = [21,713]
        screen.blit(odds3, p)
        pygame.display.update()
    if num == 2:
        p = [31,639]
        screen.blit(odds4, p)
        pygame.display.update()
    if num == 1:
        p = [31,582]
        screen.blit(odds5, p)
        pygame.display.update()
