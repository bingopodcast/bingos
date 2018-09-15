
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
top_line = pygame.image.load('parade/assets/top_line.png').convert_alpha()
bottom_line = pygame.image.load('parade/assets/bottom_line.png').convert_alpha()
bg_menu = pygame.image.load('parade/assets/parade_menu.png')
bg_gi = pygame.image.load('parade/assets/parade_gi.png')
bg_off = pygame.image.load('parade/assets/parade_off.png')
a_1 = pygame.image.load('parade/assets/a-1.png').convert_alpha()
a_2 = pygame.image.load('parade/assets/a-2.png').convert_alpha()
a_3 = pygame.image.load('parade/assets/a-3.png').convert_alpha()
a_4 = pygame.image.load('parade/assets/a-4.png').convert_alpha()
b_1 = pygame.image.load('parade/assets/b-1.png').convert_alpha()
b_2 = pygame.image.load('parade/assets/b-2.png').convert_alpha()
b_3 = pygame.image.load('parade/assets/b-3.png').convert_alpha()
b_4 = pygame.image.load('parade/assets/b-4.png').convert_alpha()
c_1 = pygame.image.load('parade/assets/c-1.png').convert_alpha()
c_2 = pygame.image.load('parade/assets/c-2.png').convert_alpha()
c_3 = pygame.image.load('parade/assets/c-3.png').convert_alpha()
c_4 = pygame.image.load('parade/assets/c-4.png').convert_alpha()
d_1 = pygame.image.load('parade/assets/d-1.png').convert_alpha()
d_2 = pygame.image.load('parade/assets/d-2.png').convert_alpha()
d_3 = pygame.image.load('parade/assets/d-3.png').convert_alpha()
d_4 = pygame.image.load('parade/assets/d-4.png').convert_alpha()

class scorereel():
    """ Score Reels are used to count replays """
    def __init__(self, pos, image):
        self.position = pos
        self.default_y = self.position[1]
        self.image = pygame.image.load(image).convert()

reel1 = scorereel([96,287], "graphics/assets/white_reel.png")
reel10 = scorereel([77,287], "graphics/assets/white_reel.png")
reel100 = scorereel([58,287], "graphics/assets/white_reel.png")

def display(s, replays=0, menu=False):
    
    meter.set_colorkey((255,0,252))
    meter_position = [48,287]

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
        screen.blit(bg_menu, backglass_position)
    else:
        if (s.game.anti_cheat.status == True):
            screen.blit(bg_gi, backglass_position)
        else:
            screen.blit(bg_off, backglass_position)

    if s.game.top_line.status == True:
        p = [10,954]
        screen.blit(line, p)
        p = [224,361]
        screen.blit(top_line, p)
    else:
        p = [224,361]
        screen.blit(extra, p)

    if s.game.bottom_line.status == True:
        p = [102,956]
        screen.blit(line, p)
        p = [223,715]
        screen.blit(bottom_line, p)
    else:
        p = [223,715]
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
                    p = [335,709]
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
                    p = [218,711]
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
                    p = [220,357]
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
                    p = [279,357]
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
                    p = [277,711]
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
                    p = [335,357]
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
                    p = [451,358]
                    screen.blit(number, p)
            if 18 in s.holes:
                number_position = [281,537]
                screen.blit(number, number_position)
                if s.game.top_line.status == True:
                    p = [393,357]
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
                    p = [392,711]
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
                    p = [450,711]
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
        p = [572,925]
        screen.blit(dt_arrow, p)
    elif s.game.red_line.position == 2:
        p = [572,893]
        screen.blit(dt_arrow, p)
    elif s.game.red_line.position == 3:
        p = [571,860]
        screen.blit(dt_arrow, p)
    elif s.game.red_line.position == 4:
        p = [572,829]
        screen.blit(dt_arrow, p)
    if s.game.red_line.position >= 5 and s.game.red_line.position < 10:
        p = [550,748]
        screen.blit(double, p)
    if s.game.red_line.position == 6:
        p = [572,713]
        screen.blit(dt_arrow, p)
    elif s.game.red_line.position == 7:
        p = [572,681]
        screen.blit(dt_arrow, p)
    elif s.game.red_line.position == 8:
        p = [571,649]
        screen.blit(dt_arrow, p)
    elif s.game.red_line.position == 9:
        p = [571,617]
        screen.blit(dt_arrow, p)
    if s.game.red_line.position >= 10 and s.game.red_line.position < 15:
        p = [551,537]
        screen.blit(triple, p)
    if s.game.red_line.position == 11:
        p = [571,501]
        screen.blit(dt_arrow, p)
    elif s.game.red_line.position == 12:
        p = [571,469]
        screen.blit(dt_arrow, p)
    elif s.game.red_line.position == 13:
        p = [571,439]
        screen.blit(dt_arrow, p)
    elif s.game.red_line.position == 14:
        p = [571,407]
        screen.blit(dt_arrow, p)
    if s.game.red_line.position == 15:
        p = [552,327]
        screen.blit(quadruple, p)


    if s.game.green_line.position == 1:
        p = [655,924]
        screen.blit(dt_arrow, p)
    elif s.game.green_line.position == 2:
        p = [655,892]
        screen.blit(dt_arrow, p)
    elif s.game.green_line.position == 3:
        p = [655,859]
        screen.blit(dt_arrow, p)
    elif s.game.green_line.position == 4:
        p = [656,828]
        screen.blit(dt_arrow, p)
    if s.game.green_line.position >= 5 and s.game.green_line.position < 10:
        p = [634,749]
        screen.blit(double, p)
    if s.game.green_line.position == 6:
        p = [654,711]
        screen.blit(dt_arrow, p)
    elif s.game.green_line.position == 7:
        p = [654,679]
        screen.blit(dt_arrow, p)
    elif s.game.green_line.position == 8:
        p = [654,646]
        screen.blit(dt_arrow, p)
    elif s.game.green_line.position == 9:
        p = [654,616]
        screen.blit(dt_arrow, p)
    if s.game.green_line.position >= 10 and s.game.green_line.position < 15:
        p = [634,537]
        screen.blit(triple, p)
    if s.game.green_line.position == 11:
        p = [655,500]
        screen.blit(dt_arrow, p)
    elif s.game.green_line.position == 12:
        p = [655,468]
        screen.blit(dt_arrow, p)
    elif s.game.green_line.position == 13:
        p = [655,436]
        screen.blit(dt_arrow, p)
    elif s.game.green_line.position == 14:
        p = [655,405]
        screen.blit(dt_arrow, p)
    if s.game.green_line.position == 15:
        p = [635,325]
        screen.blit(quadruple, p)

    if s.game.magic_squares_feature.position == 1:
        p = [194,972]
        screen.blit(ms_arrow, p)
    if s.game.magic_squares_feature.position == 2:
        p = [226,970]
        screen.blit(ms_arrow, p)
    if s.game.magic_squares_feature.position == 3:
        p = [256,972]
        screen.blit(ms_arrow, p)
    if s.game.magic_squares_feature.position == 4:
        p = [287,971]
        screen.blit(ms_arrow, p)
    if s.game.magic_squares_feature.position >= 5:
        p = [321,967]
        screen.blit(ms_abc, p)
    if s.game.magic_squares_feature.position == 7:
        p = [449,970]
        screen.blit(ms_d, p)

    if s.game.odds.position == 1:
        p = [21,877]
        screen.blit(odds1, p)
    elif s.game.odds.position == 2:
        p = [31,778]
        screen.blit(odds2, p)
    elif s.game.odds.position == 3:
        p = [26,716]
        screen.blit(odds3, p)
    elif s.game.odds.position == 4:
        p = [29,636]
        screen.blit(odds4, p)
    elif s.game.odds.position == 5:
        p = [24,586]
        screen.blit(odds5, p)
    elif s.game.odds.position == 6:
        p = [22,522]
        screen.blit(odds6, p)
    elif s.game.odds.position == 7:
        p = [26,456]
        screen.blit(odds7, p)
    elif s.game.odds.position == 8:
        p = [16,392]
        screen.blit(odds8, p)

    if s.game.magic_squares_feature.position >= 5:
        p = [167,446]
        screen.blit(ms_letter, p)
        p = [165,622]
        screen.blit(ms_letter, p)
        p = [507,446]
        screen.blit(ms_letter, p)
        if s.game.before_fourth.status == True:
            p = [530,959]
            screen.blit(time, p)
            if s.game.ball_count.position == 3:
                s.cancel_delayed(name="blink")
                blink([s,1,1])
            else:
                s.cancel_delayed(name="blink")
        elif s.game.before_fifth.status == True:
            p = [621,960]
            screen.blit(time, p)
            if s.game.ball_count.position == 4:
                s.cancel_delayed(name="blink")
                blink([s,1,1])
            else:
                s.cancel_delayed(name="blink")
    if s.game.magic_squares_feature.position == 7:
        p = [507,623]
        screen.blit(ms_letter, p)

    if s.game.ballyhole.status == True:
        p = [594,243]
        screen.blit(ballyhole, p)

    if s.game.extra_ball.position >= 1:
        p = [133,1030]
        screen.blit(eb_number, p)
    if s.game.extra_ball.position >= 2:
        p = [183,1031]
        screen.blit(eb, p)
    if s.game.extra_ball.position >= 3:
        p = [252,1032]
        screen.blit(eb, p)
    if s.game.extra_ball.position >= 4:
        p = [325,1031]
        screen.blit(eb_number, p)
    if s.game.extra_ball.position >= 5:
        p = [377,1032]
        screen.blit(eb, p)
    if s.game.extra_ball.position >= 6:
        p = [444,1031]
        screen.blit(eb, p)
    if s.game.extra_ball.position >= 7:
        p = [520,1032]
        screen.blit(eb_number, p)
    if s.game.extra_ball.position >= 8:
        p = [571,1032]
        screen.blit(eb, p)
    if s.game.extra_ball.position == 9:
        p = [638,1032]
        screen.blit(eb, p)

    if s.game.eb_play.status == True:
        p = [10,1027]
        screen.blit(extra_balls, p)


    if s.game.tilt.status == True:
        tilt_position = [463,801]
        screen.blit(tilt, tilt_position)

    pygame.display.update()

def blink(args):
    dirty_rects = []
    s = args[0]
    b = args[1]
    sl = args[2]

    if b == 0:
        if sl == 1:
            p = [257,933]
            dirty_rects.append(screen.blit(select_now, p))
        pygame.display.update(dirty_rects)
    else:
        dirty_rects.append(screen.blit(bg_gi, (257,933), pygame.Rect(257,933,206,35)))
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
        p = [218,412]
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
        dirty_rects.append(screen.blit(topleft, (240  - num - 20, 418)))
        dirty_rects.append(screen.blit(topright, (278, 418 - num - 10)))
        dirty_rects.append(screen.blit(bottomright, (278  + num + 10, 475)))
        dirty_rects.append(screen.blit(bottomleft, (220, 476 + num + 5)))

    if (s.game.anti_cheat.status == True):
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],130,130)))
    else:
        dirty_rects.append(screen.blit(bg_off, p, pygame.Rect(p[0],p[1],130,130)))
    
    if 2 in s.holes:
        number_position = [221,535]
        dirty_rects.append(screen.blit(bg_gi, number_position, pygame.Rect(number_position[0],number_position[1],49,50)))
        dirty_rects.append(screen.blit(number, number_position))
    if 16 in s.holes:
        number_position = [339,536]
        dirty_rects.append(screen.blit(bg_gi, number_position, pygame.Rect(number_position[0],number_position[1],49,50)))
        dirty_rects.append(screen.blit(number, number_position))
    if 18 in s.holes:
        number_position = [281,537]
        dirty_rects.append(screen.blit(bg_gi, number_position, pygame.Rect(number_position[0],number_position[1],49,50)))
        dirty_rects.append(screen.blit(number, number_position))
    if 24 in s.holes:
        number_position = [339,477]
        dirty_rects.append(screen.blit(bg_gi, number_position, pygame.Rect(number_position[0],number_position[1],49,50)))
        dirty_rects.append(screen.blit(number, number_position))
    if 25 in s.holes:
        number_position = [340,419]
        dirty_rects.append(screen.blit(bg_gi, number_position, pygame.Rect(number_position[0],number_position[1],49,50)))
        dirty_rects.append(screen.blit(number, number_position))

    if s.game.magic_squares_feature.position >= 5:
        p = [167,446]
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],52,48)))
        dirty_rects.append(screen.blit(ms_letter, p))
    if s.game.top_line.status == False: 
        p = [224,361]
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],274,45)))
        dirty_rects.append(screen.blit(extra, p))
    else:
        p = [224,361]
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],274,45)))
        dirty_rects.append(screen.blit(top_line, p))
        if 6 in s.holes:
            p = [220,357]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],49,50)))
            dirty_rects.append(screen.blit(number, p))
        if 7 in s.holes:
            p = [279,357]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],49,50)))
            dirty_rects.append(screen.blit(number, p))
        if 13 in s.holes:
            p = [335,357]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],49,50)))
            dirty_rects.append(screen.blit(number, p))
        if 17 in s.holes:
            p = [451,358]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],49,50)))
            dirty_rects.append(screen.blit(number, p))
        if 18 in s.holes:
            p = [393,357]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],49,50)))
            dirty_rects.append(screen.blit(number, p))

    pygame.display.update(dirty_rects)

def squareb_animation(args):
    dirty_rects = []
    s = args[0]
    num = args[1]
    square = args[2]
    
    if square == 2:
        p = [217,590]
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
        dirty_rects.append(screen.blit(topleft, (240  - num - 25, 593)))
        dirty_rects.append(screen.blit(topright, (275, 597 - num - 9)))
        dirty_rects.append(screen.blit(bottomright, (260  + num + 29, 649)))
        dirty_rects.append(screen.blit(bottomleft, (220, 651 + num + 8)))
    
    if (s.game.anti_cheat.status == True):
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],130,130)))
    else:
        dirty_rects.append(screen.blit(bg_off, p, pygame.Rect(p[0],p[1],130,130)))
    
    if 2 in s.holes:
        number_position = [221,535]
        dirty_rects.append(screen.blit(bg_gi, number_position, pygame.Rect(number_position[0],number_position[1],49,50)))
        dirty_rects.append(screen.blit(number, number_position))
    if 5 in s.holes:
        number_position = [337,651]
        dirty_rects.append(screen.blit(bg_gi, number_position, pygame.Rect(number_position[0],number_position[1],49,50)))
        dirty_rects.append(screen.blit(number, number_position))
    if 13 in s.holes:
        number_position = [338,595]
        dirty_rects.append(screen.blit(bg_gi, number_position, pygame.Rect(number_position[0],number_position[1],49,50)))
        dirty_rects.append(screen.blit(number, number_position))
    if 18 in s.holes:
        number_position = [281,537]
        dirty_rects.append(screen.blit(bg_gi, number_position, pygame.Rect(number_position[0],number_position[1],49,50)))
        dirty_rects.append(screen.blit(number, number_position))

    if s.game.magic_squares_feature.position >= 5:
        p = [165,622]
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],52,48)))
        dirty_rects.append(screen.blit(ms_letter, p))

    if s.game.bottom_line.status == False: 
        p = [223,715]
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],274,45)))
        dirty_rects.append(screen.blit(extra, p))
    else:
        p = [223,715]
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],274,45)))
        dirty_rects.append(screen.blit(bottom_line, p))
        if 3 in s.holes:
            p = [335,709]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],49,50)))
            dirty_rects.append(screen.blit(number, p))
        if 5 in s.holes:
            p = [218,711]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],49,50)))
            dirty_rects.append(screen.blit(number, p))
        if 8 in s.holes:
            p = [277,711]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],49,50)))
            dirty_rects.append(screen.blit(number, p))
        if 19 in s.holes:
            p = [392,711]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],49,50)))
            dirty_rects.append(screen.blit(number, p))
        if 22 in s.holes:
            p = [450,711]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],49,50)))
            dirty_rects.append(screen.blit(number, p))

    pygame.display.update(dirty_rects)

def squarec_animation(args):
    dirty_rects = []
    s = args[0]
    num = args[1]
    square = args[2]
    
    if square == 3:
        p = [393,412]
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
        dirty_rects.append(screen.blit(topleft, (407  - num - 15, 416)))
        dirty_rects.append(screen.blit(topright, (448, 411 - num - 0)))
        dirty_rects.append(screen.blit(bottomright, (440  + num + 15, 470)))
        dirty_rects.append(screen.blit(bottomleft, (397, 475 + num + 6)))
    
    if (s.game.anti_cheat.status == True):
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],130,130)))
    else:
        dirty_rects.append(screen.blit(bg_off, p, pygame.Rect(p[0],p[1],130,130)))
    
    if 11 in s.holes:
        number_position = [455,535]
        dirty_rects.append(screen.blit(bg_gi, number_position, pygame.Rect(number_position[0],number_position[1],49,50)))
        dirty_rects.append(screen.blit(number, number_position))
    if 12 in s.holes:
        number_position = [398,534]
        dirty_rects.append(screen.blit(bg_gi, number_position, pygame.Rect(number_position[0],number_position[1],49,50)))
        dirty_rects.append(screen.blit(number, number_position))
    if 24 in s.holes:
        number_position = [339,477]
        dirty_rects.append(screen.blit(bg_gi, number_position, pygame.Rect(number_position[0],number_position[1],49,50)))
        dirty_rects.append(screen.blit(number, number_position))
    if 25 in s.holes:
        number_position = [340,419]
        dirty_rects.append(screen.blit(bg_gi, number_position, pygame.Rect(number_position[0],number_position[1],49,50)))
        dirty_rects.append(screen.blit(number, number_position))

    if s.game.magic_squares_feature.position >= 5:
        p = [507,446]
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],52,48)))
        dirty_rects.append(screen.blit(ms_letter, p))

    if s.game.top_line.status == False: 
        p = [224,361]
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],274,45)))
        dirty_rects.append(screen.blit(extra, p))
    else:
        p = [224,361]
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],274,45)))
        dirty_rects.append(screen.blit(top_line, p))
        if 6 in s.holes:
            p = [220,357]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],49,50)))
            dirty_rects.append(screen.blit(number, p))
        if 7 in s.holes:
            p = [279,357]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],49,50)))
            dirty_rects.append(screen.blit(number, p))
        if 13 in s.holes:
            p = [335,357]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],49,50)))
            dirty_rects.append(screen.blit(number, p))
        if 17 in s.holes:
            p = [451,358]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],49,50)))
            dirty_rects.append(screen.blit(number, p))
        if 18 in s.holes:
            p = [393,357]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],49,50)))
            dirty_rects.append(screen.blit(number, p))


    pygame.display.update(dirty_rects)

def squared_animation(args):
    dirty_rects = []
    s = args[0]
    num = args[1]
    square = args[2]
    
    p = [391,592]
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
        dirty_rects.append(screen.blit(topleft, (396 - num - 6, 595)))
        dirty_rects.append(screen.blit(topright, (450, 604 - num - 13)))
        dirty_rects.append(screen.blit(bottomright, (435  + num + 29, 654)))
        dirty_rects.append(screen.blit(bottomleft, (393, 650 + num + 12)))
    
    if (s.game.anti_cheat.status == True):
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],130,130)))
    else:
        dirty_rects.append(screen.blit(bg_off, p, pygame.Rect(p[0],p[1],130,130)))
    
    if 5 in s.holes:
        number_position = [337,651]
        dirty_rects.append(screen.blit(bg_gi, number_position, pygame.Rect(number_position[0],number_position[1],49,50)))
        dirty_rects.append(screen.blit(number, number_position))
    if 11 in s.holes:
        number_position = [455,535]
        dirty_rects.append(screen.blit(bg_gi, number_position, pygame.Rect(number_position[0],number_position[1],49,50)))
        dirty_rects.append(screen.blit(number, number_position))
    if 12 in s.holes:
        number_position = [398,534]
        dirty_rects.append(screen.blit(bg_gi, number_position, pygame.Rect(number_position[0],number_position[1],49,50)))
        dirty_rects.append(screen.blit(number, number_position))
    if 13 in s.holes:
        number_position = [338,595]
        dirty_rects.append(screen.blit(bg_gi, number_position, pygame.Rect(number_position[0],number_position[1],49,50)))
        dirty_rects.append(screen.blit(number, number_position))

    if s.game.magic_squares_feature.position >= 5:
        p = [507,623]
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],52,48)))
        dirty_rects.append(screen.blit(ms_letter, p))

    if s.game.bottom_line.status == False: 
        p = [223,715]
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],274,45)))
        dirty_rects.append(screen.blit(extra, p))
    else:
        p = [223,715]
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],274,45)))
        dirty_rects.append(screen.blit(bottom_line, p))
        if 3 in s.holes:
            p = [335,709]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],49,50)))
            dirty_rects.append(screen.blit(number, p))
        if 5 in s.holes:
            p = [218,711]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],49,50)))
            dirty_rects.append(screen.blit(number, p))
        if 8 in s.holes:
            p = [277,711]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],49,50)))
            dirty_rects.append(screen.blit(number, p))
        if 19 in s.holes:
            p = [392,711]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],49,50)))
            dirty_rects.append(screen.blit(number, p))
        if 22 in s.holes:
            p = [450,711]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],49,50)))
            dirty_rects.append(screen.blit(number, p))



    pygame.display.update(dirty_rects)



def eb_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]

    if s.game.extra_ball.position < 1:
        dirty_rects.append(screen.blit(bg_gi, (133,1030), pygame.Rect(133,1030,52,36)))
    if s.game.extra_ball.position < 2:
        dirty_rects.append(screen.blit(bg_gi, (183,1031), pygame.Rect(183,1031,69,36)))
    if s.game.extra_ball.position < 3:
        dirty_rects.append(screen.blit(bg_gi, (252,1032), pygame.Rect(252,1032,69,36)))
    if s.game.extra_ball.position < 4:
        dirty_rects.append(screen.blit(bg_gi, (325,1031), pygame.Rect(325,1031,52,36)))
    if s.game.extra_ball.position < 5:
        dirty_rects.append(screen.blit(bg_gi, (377,1032), pygame.Rect(377,1032,69,36)))
    if s.game.extra_ball.position < 6:
        dirty_rects.append(screen.blit(bg_gi, (444,1031), pygame.Rect(444,1031,69,36)))
    if s.game.extra_ball.position < 7:
        dirty_rects.append(screen.blit(bg_gi, (520,1032), pygame.Rect(520,1032,52,36)))
    if s.game.extra_ball.position < 8:
        dirty_rects.append(screen.blit(bg_gi, (571,1032), pygame.Rect(571,1032,69,36)))
    if s.game.extra_ball.position < 9:
        dirty_rects.append(screen.blit(bg_gi, (638,1032), pygame.Rect(638,1032,69,36)))

    pygame.display.update(dirty_rects)

    if num in [0,24,25,49]:
        if s.game.extra_ball.position < 1:
            p = [133,1030]
            dirty_rects.append(screen.blit(eb_number, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [1,15,26,40]:
        if s.game.extra_ball.position < 2:
            p = [183,1031]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [3,4,17,28,29,42]:
        if s.game.extra_ball.position < 3:
            p = [252,1032]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [5,18,30,43]:
        if s.game.extra_ball.position < 4:
            p = [325,1031]
            dirty_rects.append(screen.blit(eb_number, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [7,8,19,32,33,44]:
        if s.game.extra_ball.position < 5:
            p = [377,1032]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [9,10,20,34,35,45]:
        if s.game.extra_ball.position < 6:
            p = [444,1031]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [11,21,36,46]:
        if s.game.extra_ball.position < 7:
            p = [520,1032]
            dirty_rects.append(screen.blit(eb_number, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [12,22,37,47]:
        if s.game.extra_ball.position < 8:
            p = [571,1032]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [2,6,13,16,23,27,31,38,41,48]:
        if s.game.extra_ball.position < 9:
            p = [638,1032]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects) 
            return

def clear_odds(s, num):
    global screen

    dirty_rects = []

    if s.game.odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (21,877), pygame.Rect(21,877,153,36)))
    if s.game.odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (31,778), pygame.Rect(31,778,159,39)))
    if s.game.odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (26,716), pygame.Rect(26,716,136,37)))
    if s.game.odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (29,636), pygame.Rect(29,636,123,47)))
    if s.game.odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (24,586), pygame.Rect(24,586,132,34)))
    if s.game.odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (22,522), pygame.Rect(22,522,136,36)))
    if s.game.odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (26,456), pygame.Rect(26,456,129,38)))
    if s.game.odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (16,392), pygame.Rect(16,392,141,35)))

    pygame.display.update(dirty_rects)

def draw_odds_animation(s, num):
    global screen
    dirty_rects = []

    if num in [2,3,12,27,28,37]:
        if s.game.odds.position != 1:
            p = [21,877]
            dirty_rects.append(screen.blit(odds1, p))
            pygame.display.update(dirty_rects)
            return
    if num in [13,14,38,39]:
        if s.game.odds.position != 2:
            p = [31,778]
            dirty_rects.append(screen.blit(odds2, p))
            pygame.display.update(dirty_rects)
            return
    if num in [4,5,15,16,29,30,40,41]:
        if s.game.odds.position != 3:
            p = [26,716]
            dirty_rects.append(screen.blit(odds3, p))
            pygame.display.update(dirty_rects)
            return
    if num in [17,18,42,43]:
        if s.game.odds.position != 4:
            p = [29,636]
            dirty_rects.append(screen.blit(odds4, p))
            pygame.display.update(dirty_rects)
            return
    if num in [6,7,19,20,31,32,44,45]:
        if s.game.odds.position != 5:
            p = [24,586]
            dirty_rects.append(screen.blit(odds5, p))
            pygame.display.update(dirty_rects)
            return
    if num in [21,22,46,47]:
        if s.game.odds.position != 6:
            p = [22,522]
            dirty_rects.append(screen.blit(odds6, p))
            pygame.display.update(dirty_rects)
            return
    if num in [8,9,23,24,33,34,48,49]:
        if s.game.odds.position != 7:
            p = [26,456]
            dirty_rects.append(screen.blit(odds7, p))
            pygame.display.update(dirty_rects)
            return
    if num in [10,11,25,26,0,35,36,50]:
        if s.game.odds.position != 8:
            p = [16,392]
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
        dirty_rects.append(screen.blit(bg_gi, (321,967), pygame.Rect(321,967,122,43)))
        dirty_rects.append(screen.blit(bg_gi, (167,446), pygame.Rect(167,446,52,48)))
        dirty_rects.append(screen.blit(bg_gi, (165,622), pygame.Rect(165,622,52,48)))
        dirty_rects.append(screen.blit(bg_gi, (507,446), pygame.Rect(507,446,52,48)))
    if s.game.before_fourth.status == False or s.game.magic_squares_feature.position < 5:
        dirty_rects.append(screen.blit(bg_gi, (530,959), pygame.Rect(530,959,90,62)))
    if s.game.before_fifth.status == False:
        dirty_rects.append(screen.blit(bg_gi, (621,960), pygame.Rect(621,960,90,62)))
    if s.game.magic_squares_feature.position < 7:
        dirty_rects.append(screen.blit(bg_gi, (449,970), pygame.Rect(449,970,74,42)))
        dirty_rects.append(screen.blit(bg_gi, (507,623), pygame.Rect(507,623,52,48)))
    if s.game.ballyhole.status == False:
        dirty_rects.append(screen.blit(bg_gi, (594,243), pygame.Rect(594,243,81,83)))
    if s.game.green_line.position < 5:
        dirty_rects.append(screen.blit(bg_gi, (634,749), pygame.Rect(634,749,79,78)))
    if s.game.green_line.position < 10:
        dirty_rects.append(screen.blit(bg_gi, (634,537), pygame.Rect(634,537,79,78)))
    if s.game.green_line.position < 15:
        dirty_rects.append(screen.blit(bg_gi, (635,325), pygame.Rect(635,325,79,78)))
    if s.game.red_line.position < 5:
        dirty_rects.append(screen.blit(bg_gi, (550,748), pygame.Rect(550,748,79,78)))
    if s.game.red_line.position < 10:
        dirty_rects.append(screen.blit(bg_gi, (551,537), pygame.Rect(551,537,79,78)))
    if s.game.red_line.position < 15:
        dirty_rects.append(screen.blit(bg_gi, (552,327), pygame.Rect(552,327,79,78)))
    if s.game.top_line.status == False:
        dirty_rects.append(screen.blit(bg_gi, (10,954), pygame.Rect(10,954,85,62)))
    if s.game.bottom_line.status == False:
        dirty_rects.append(screen.blit(bg_gi, (102,956), pygame.Rect(102,956,85,62)))

    pygame.display.update(dirty_rects)


def draw_feature_animation(s, num):
    global screen
    dirty_rects = []
 
    if num in [18,19,43,44]:
        if s.game.magic_squares_feature.position < 5:
            p = [321,967]
            dirty_rects.append(screen.blit(ms_abc, p))
            p = [167,446]
            dirty_rects.append(screen.blit(ms_letter, p))
            p = [165,622]
            dirty_rects.append(screen.blit(ms_letter, p))
            p = [507,446]
            dirty_rects.append(screen.blit(ms_letter, p))
            pygame.display.update(dirty_rects)
            return
        if s.game.before_fourth.status == False or s.game.magic_squares_feature.position < 5:
            p = [530,959]
            dirty_rects.append(screen.blit(time, p))
            pygame.display.update(dirty_rects)
            return
    if num in [5,6,30,31]:
        if s.game.before_fifth.status == False:
            p = [621,960]
            dirty_rects.append(screen.blit(time, p))
            pygame.display.update(dirty_rects)
            return
    if num in [9,10,34,35]:
        if s.game.magic_squares_feature.position < 7:
            p = [449,970]
            dirty_rects.append(screen.blit(ms_d, p))
            p = [507,623]
            dirty_rects.append(screen.blit(ms_letter, p))
            pygame.display.update(dirty_rects)
            return
    if num in [11,36]:
        if s.game.ballyhole.status == False:
            p = [594,243]
            dirty_rects.append(screen.blit(ballyhole, p))
            pygame.display.update(dirty_rects)
            return
    if num in [7,8,32,33]:
        if s.game.green_line.position < 5:
            p = [634,749]
            dirty_rects.append(screen.blit(double, p))
            pygame.display.update(dirty_rects)
            return
    if num in [18,19,43,44]:
        if s.game.green_line.position < 10:
            p = [634,537]
            dirty_rects.append(screen.blit(triple, p))
            pygame.display.update(dirty_rects)
            return
    if num in [1,2,26,27]:
        if s.game.green_line.position < 15:
            p = [635,325]
            dirty_rects.append(screen.blit(quadruple, p))
            pygame.display.update(dirty_rects)
            return
    if num in [3,4,28,29]:
        if s.game.red_line.position < 5:
            p = [550,748]
            dirty_rects.append(screen.blit(double, p))
            pygame.display.update(dirty_rects)
            return
    if num in [12,13,37,38]:
        if s.game.red_line.position < 10:
            p = [551,537]
            dirty_rects.append(screen.blit(triple, p))
            pygame.display.update(dirty_rects)
    if num in [20,21,45,46]:
        if s.game.red_line.position < 15:
            p = [552,327]
            dirty_rects.append(screen.blit(quadruple, p))
            pygame.display.update(dirty_rects)
    if num in [14,15,39,40]:
        if s.game.top_line.status == False:
            p = [10,954]
            dirty_rects.append(screen.blit(line, p))
            pygame.display.update(dirty_rects)
    if num in [22,23,47,48]:
        if s.game.bottom_line.status == False:
            p = [102,956]
            dirty_rects.append(screen.blit(line, p))
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

