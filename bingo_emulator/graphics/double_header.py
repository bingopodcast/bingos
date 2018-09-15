
import pygame

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

meter = pygame.image.load('graphics/assets/register_cover.png').convert()
number = pygame.image.load('double_header/assets/number.png').convert_alpha()
corners = pygame.image.load('double_header/assets/corners.png').convert_alpha()
double = pygame.image.load('double_header/assets/double.png').convert_alpha()
extra_balls = pygame.image.load('double_header/assets/extra_balls.png').convert_alpha()
eb = pygame.image.load('double_header/assets/eb.png').convert_alpha()
eb_number = pygame.image.load('double_header/assets/eb_number.png').convert_alpha()
g1o1 = pygame.image.load('double_header/assets/g1o1.png').convert_alpha()
g1o2 = pygame.image.load('double_header/assets/g1o2.png').convert_alpha()
g1o3 = pygame.image.load('double_header/assets/g1o3.png').convert_alpha()
g1o4 = pygame.image.load('double_header/assets/g1o4.png').convert_alpha()
g1o5 = pygame.image.load('double_header/assets/g1o5.png').convert_alpha()
g1o6 = pygame.image.load('double_header/assets/g1o6.png').convert_alpha()
g2o1 = pygame.image.load('double_header/assets/g2o1.png').convert_alpha()
g2o2 = pygame.image.load('double_header/assets/g2o2.png').convert_alpha()
g2o3 = pygame.image.load('double_header/assets/g2o3.png').convert_alpha()
g2o4 = pygame.image.load('double_header/assets/g2o4.png').convert_alpha()
g2o5 = pygame.image.load('double_header/assets/g2o5.png').convert_alpha()
game = pygame.image.load('double_header/assets/game.png').convert_alpha()
large_spotted = pygame.image.load('double_header/assets/large_spotted.png').convert_alpha()
ms_ab = pygame.image.load('double_header/assets/ms_ab.png').convert_alpha()
ms_c = pygame.image.load('double_header/assets/ms_c.png').convert_alpha()
ms_d = pygame.image.load('double_header/assets/ms_c.png').convert_alpha()
ms_letter = pygame.image.load('double_header/assets/ms_letter.png').convert_alpha()
s_arrow = pygame.image.load('double_header/assets/s_arrow.png').convert_alpha()
select_now = pygame.image.load('double_header/assets/select_now.png').convert_alpha()
small_spotted = pygame.image.load('double_header/assets/small_spotted.png').convert_alpha()
s_number = pygame.image.load('double_header/assets/s_number.png').convert_alpha()
turn_now = pygame.image.load('double_header/assets/turn_now.png').convert_alpha()
tilt = pygame.image.load('double_header/assets/tilt.png').convert_alpha()
a0 = pygame.image.load('double_header/assets/a0.png').convert_alpha()
a1 = pygame.image.load('double_header/assets/a1.png').convert_alpha()
a2 = pygame.image.load('double_header/assets/a2.png').convert_alpha()
a3 = pygame.image.load('double_header/assets/a3.png').convert_alpha()
b0 = pygame.image.load('double_header/assets/b0.png').convert_alpha()
b1 = pygame.image.load('double_header/assets/b1.png').convert_alpha()
b2 = pygame.image.load('double_header/assets/b2.png').convert_alpha()
b3 = pygame.image.load('double_header/assets/b3.png').convert_alpha()
c0 = pygame.image.load('double_header/assets/c0.png').convert_alpha()
c1 = pygame.image.load('double_header/assets/c1.png').convert_alpha()
c2 = pygame.image.load('double_header/assets/c2.png').convert_alpha()
c3 = pygame.image.load('double_header/assets/c3.png').convert_alpha()
d0 = pygame.image.load('double_header/assets/d0.png').convert_alpha()
d1 = pygame.image.load('double_header/assets/d1.png').convert_alpha()
d2 = pygame.image.load('double_header/assets/d2.png').convert_alpha()
d3 = pygame.image.load('double_header/assets/d3.png').convert_alpha()
bg_menu = pygame.image.load('double_header/assets/double_header_menu.png')
bg_gi = pygame.image.load('double_header/assets/double_header_gi.png')
bg_off = pygame.image.load('double_header/assets/double_header_off.png')
a_1 = pygame.image.load('double_header/assets/a-1.png').convert_alpha()
a_2 = pygame.image.load('double_header/assets/a-2.png').convert_alpha()
a_3 = pygame.image.load('double_header/assets/a-3.png').convert_alpha()
a_4 = pygame.image.load('double_header/assets/a-4.png').convert_alpha()
b_1 = pygame.image.load('double_header/assets/b-1.png').convert_alpha()
b_2 = pygame.image.load('double_header/assets/b-2.png').convert_alpha()
b_3 = pygame.image.load('double_header/assets/b-3.png').convert_alpha()
b_4 = pygame.image.load('double_header/assets/b-4.png').convert_alpha()
c_1 = pygame.image.load('double_header/assets/c-1.png').convert_alpha()
c_2 = pygame.image.load('double_header/assets/c-2.png').convert_alpha()
c_3 = pygame.image.load('double_header/assets/c-3.png').convert_alpha()
c_4 = pygame.image.load('double_header/assets/c-4.png').convert_alpha()
d_1 = pygame.image.load('double_header/assets/d-1.png').convert_alpha()
d_2 = pygame.image.load('double_header/assets/d-2.png').convert_alpha()
d_3 = pygame.image.load('double_header/assets/d-3.png').convert_alpha()
d_4 = pygame.image.load('double_header/assets/d-4.png').convert_alpha()



class scorereel():
    """ Score Reels are used to count replays """
    def __init__(self, pos, image):
        self.position = pos
        self.default_y = self.position[1]
        self.image = pygame.image.load(image).convert()

reel1 = scorereel([90,298], "graphics/assets/white_reel.png")
reel10 = scorereel([72,298], "graphics/assets/white_reel.png")
reel100 = scorereel([52,298], "graphics/assets/white_reel.png")

def display(s, replays=0, menu=False):
    
    meter.set_colorkey((255,0,252))
    meter_position = [42,298]

    screen.blit(reel1.image, reel1.position)
    screen.blit(reel10.image, reel10.position)
    screen.blit(reel100.image, reel100.position)
    screen.blit(meter, meter_position)

    if s.game.square_a.position == 0:
        p = [398,385]
        screen.blit(a0, p)
    if s.game.square_a.position == 1:
        p = [398,385]
        screen.blit(a1, p)
    if s.game.square_a.position == 2:
        p = [398,385]
        screen.blit(a2, p)
    if s.game.square_a.position == 3:
        p = [398,385]
        screen.blit(a3, p)
    if s.game.square_b.position == 0:
        p = [397,560]
        screen.blit(b0, p)
    if s.game.square_b.position == 1:
        p = [397,560]
        screen.blit(b1, p)
    if s.game.square_b.position == 2:
        p = [397,560]
        screen.blit(b2, p)
    if s.game.square_b.position == 3:
        p = [397,560]
        screen.blit(b3, p)
    if s.game.square_c.position == 0:
        p = [561,388]
        screen.blit(c0, p)
    if s.game.square_c.position == 1:
        p = [561,388]
        screen.blit(c1, p)
    if s.game.square_c.position == 2:
        p = [561,388]
        screen.blit(c2, p)
    if s.game.square_c.position == 3:
        p = [561,388]
        screen.blit(c3, p)
    if s.game.square_d.position == 0:
        p = [561,561]
        screen.blit(d0, p)
    if s.game.square_d.position == 1:
        p = [561,561]
        screen.blit(d1, p)
    if s.game.square_d.position == 2:
        p = [561,561]
        screen.blit(d2, p)
    if s.game.square_d.position == 3:
        p = [561,561]
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
                p = [161,448]
                screen.blit(number, p)
            if 2 in s.holes:
                p = [51,504]
                screen.blit(number, p)
            if 3 in s.holes:
                p = [268,621]
                screen.blit(number, p)
            if 4 in s.holes:
                p = [214,389]
                screen.blit(number, p)
            if 5 in s.holes:
                p = [157,390]
                screen.blit(number, p)
            if 6 in s.holes:
                p = [266,563]
                screen.blit(number, p)
            if 7 in s.holes:
                p = [105,620]
                screen.blit(number, p)
            if 8 in s.holes:
                p = [269,390]
                screen.blit(number, p)
            if 9 in s.holes:
                p = [51,390]
                screen.blit(number, p)
            if 10 in s.holes:
                p = [50,619]
                screen.blit(number, p)
            if 11 in s.holes:
                p = [51,445]
                screen.blit(number, p)
            if 12 in s.holes:
                p = [214,505]
                screen.blit(number, p)
            if 13 in s.holes:
                p = [51,562]
                screen.blit(number, p)
            if 14 in s.holes:
                p = [159,563]
                screen.blit(number, p)
            if 15 in s.holes:
                p = [160,504]
                screen.blit(number, p)
            if 16 in s.holes:
                p = [159,621]
                screen.blit(number, p)
            if 17 in s.holes:
                p = [268,503]
                screen.blit(number, p)
            if 18 in s.holes:
                p = [105,503]
                screen.blit(number, p)
            if 19 in s.holes:
                p = [107,447]
                screen.blit(number, p)
            if 20 in s.holes:
                p = [215,447]
                screen.blit(number, p)
            if 21 in s.holes:
                p = [213,563]
                screen.blit(number, p)
            if 22 in s.holes:
                p = [104,563]
                screen.blit(number, p)
            if 23 in s.holes:
                p = [213,621]
                screen.blit(number, p)
            if 24 in s.holes:
                p = [107,389]
                screen.blit(number, p)
            if 25 in s.holes:
                p = [268,447]
                screen.blit(number, p)
        if s.holes2:
            if 1 in s.holes2:
                if s.game.square_a.position == 0:
                    p = [400,447]
                    screen.blit(number, p)
                elif s.game.square_a.position == 1:
                    p = [399,390]
                    screen.blit(number, p)
                elif s.game.square_a.position == 2:
                    p = [454,390]
                    screen.blit(number, p)
                elif s.game.square_a.position == 3:
                    p = [453,447]
                    screen.blit(number, p)
            if 2 in s.holes2:
                p = [400,505]
                screen.blit(number, p)
            if 3 in s.holes2:
                if s.game.square_d.position == 0:
                    p = [617,565]
                    screen.blit(number, p)
                elif s.game.square_d.position == 1:
                    p = [618,622]
                    screen.blit(number, p)
                elif s.game.square_d.position == 2:
                    p = [564,622]
                    screen.blit(number, p)
                elif s.game.square_d.position == 3:
                    p = [564,564]
                    screen.blit(number, p)
            if 4 in s.holes2:
                if s.game.square_a.position == 0:
                    p = [453,390]
                    screen.blit(number, p)
                elif s.game.square_a.position == 1:
                    p = [454,447]
                    screen.blit(number, p)
                elif s.game.square_a.position == 2:
                    p = [398,446]
                    screen.blit(number, p)
                elif s.game.square_a.position == 3:
                    p = [398,388]
                    screen.blit(number, p)
            if 5 in s.holes2:
                p = [508,621]
                screen.blit(number, p)
            if 6 in s.holes2:
                if s.game.square_c.position == 0:
                    p = [618,392]
                    screen.blit(number, p)
                elif s.game.square_c.position == 1:
                    p = [620,450]
                    screen.blit(number, p)
                elif s.game.square_c.position == 2:
                    p = [565,448]
                    screen.blit(number, p)
                elif s.game.square_c.position == 3:
                    p = [564,391]
                    screen.blit(number, p)
            if 7 in s.holes2:
                if s.game.square_d.position == 0:
                    p = [564,622]
                    screen.blit(number, p)
                elif s.game.square_d.position == 1:
                    p = [563,563]
                    screen.blit(number, p)
                elif s.game.square_d.position == 2:
                    p = [618,565]
                    screen.blit(number, p)
                elif s.game.square_d.position == 3:
                    p = [617,622]
                    screen.blit(number, p)
            if 8 in s.holes2:
                if s.game.square_c.position == 0:
                    p = [620,449]
                    screen.blit(number, p)
                elif s.game.square_c.position == 1:
                    p = [565,448]
                    screen.blit(number, p)
                elif s.game.square_d.position == 2:
                    p = [566,391]
                    screen.blit(number, p)
                elif s.game.square_d.position == 3:
                    p = [619,391]
                    screen.blit(number, p)
            if 9 in s.holes2:
                if s.game.square_a.position == 0:
                    p = [399,388]
                    screen.blit(number, p)
                elif s.game.square_a.position == 1:
                    p = [453,390]
                    screen.blit(number, p)
                elif s.game.square_a.position == 2:
                    p = [454,446]
                    screen.blit(number, p)
                elif s.game.square_a.position == 3:
                    p = [399,447]
                    screen.blit(number, p)
            if 10 in s.holes2:
                if s.game.square_b.position == 0:
                    p = [400,562]
                    screen.blit(number, p)
                elif s.game.square_b.position == 1:
                    p = [454,563]
                    screen.blit(number, p)
                elif s.game.square_b.position == 2:
                    p = [453,620]
                    screen.blit(number, p)
                elif s.game.square_b.position == 3:
                    p = [399,619]
                    screen.blit(number, p)
            if 11 in s.holes2:
                p = [620,509]
                screen.blit(number, p)
            if 12 in s.holes2:
                p = [565,506]
                screen.blit(number, p)
            if 13 in s.holes2:
                p = [511,565]
                screen.blit(number, p)
            if 14 in s.holes2:
                if s.game.square_c.position == 0:
                    p = [564,391]
                    screen.blit(number, p)
                elif s.game.square_c.position == 1:
                    p = [618,392]
                    screen.blit(number, p)
                elif s.game.square_c.position == 2:
                    p = [620,448]
                    screen.blit(number, p)
                elif s.game.square_c.position == 3:
                    p = [565,448]
                    screen.blit(number, p)
            if 15 in s.holes2:
                if s.game.square_b.position == 0:
                    p = [400,621]
                    screen.blit(number, p)
                elif s.game.square_b.position == 1:
                    p = [400,563]
                    screen.blit(number, p)
                elif s.game.square_b.position == 2:
                    p = [453,562]
                    screen.blit(number, p)
                elif s.game.square_b.position == 3:
                    p = [453,620]
                    screen.blit(number, p)
            if 16 in s.holes2:
                p = [510,506]
                screen.blit(number, p)
            if 17 in s.holes2:
                if s.game.square_d.position == 0:
                    p = [618,620]
                    screen.blit(number, p)
                elif s.game.square_d.position == 1:
                    p = [564,522]
                    screen.blit(number, p)
                elif s.game.square_d.position == 2:
                    p = [564,563]
                    screen.blit(number, p)
                elif s.game.square_d.position == 3:
                    p = [617,565]
                    screen.blit(number, p)
            if 18 in s.holes2:
                p = [455,505]
                screen.blit(number, p)
            if 19 in s.holes2:
                if s.game.square_a.position == 0:
                    p = [455,446]
                    screen.blit(number, p)
                elif s.game.square_a.position == 1:
                    p = [399,447]
                    screen.blit(number, p)
                elif s.game.square_a.position == 2:
                    p = [400,389]
                    screen.blit(number, p)
                elif s.game.square_a.position == 3:
                    p = [454,389]
                    screen.blit(number, p)
            if 20 in s.holes2:
                if s.game.square_c.position == 0:
                    p = [566,448]
                    screen.blit(number, p)
                elif s.game.square_c.position == 1:
                    p = [565,392]
                    screen.blit(number, p)
                elif s.game.square_c.position == 2:
                    p = [619,393]
                    screen.blit(number, p)
                elif s.game.square_c.position == 3:
                    p = [619,450]
                    screen.blit(number, p)
            if 21 in s.holes2:
                if s.game.square_d.position == 0:
                    p = [564,563]
                    screen.blit(number, p)
                elif s.game.square_d.position == 1:
                    p = [616,565]
                    screen.blit(number, p)
                elif s.game.square_d.position == 2:
                    p = [617,622]
                    screen.blit(number, p)
                elif s.game.square_d.position == 3:
                    p = [564,621]
                    screen.blit(number, p)
            if 22 in s.holes2:
                if s.game.square_b.position == 0:
                    p = [453,563]
                    screen.blit(number, p)
                elif s.game.square_b.position == 1:
                    p = [454,620]
                    screen.blit(number, p)
                elif s.game.square_b.position == 2:
                    p = [399,620]
                    screen.blit(number, p)
                elif s.game.square_b.position == 3:
                    p = [399,564]
                    screen.blit(number, p)
            if 23 in s.holes2:
                if s.game.square_b.position == 0:
                    p = [454,620]
                    screen.blit(number, p)
                elif s.game.square_b.position == 1:
                    p = [399,620]
                    screen.blit(number, p)
                elif s.game.square_b.position == 2:
                    p = [399,564]
                    screen.blit(number, p)
                elif s.game.square_b.position == 3:
                    p = [453,563]
                    screen.blit(number, p)
            if 24 in s.holes2:
                p = [510,448]
                screen.blit(number, p)
            if 25 in s.holes2:
                p = [510,391]
                screen.blit(number, p)


    if s.game.spot_12.status == True:
        p = [371,704]
        screen.blit(large_spotted, p)
    if s.game.spot_13.status == True:
        p = [637,704]
        screen.blit(large_spotted, p)

    if s.game.magic_squares_feature.position >= 1:
        p = [372,775]
        screen.blit(ms_ab, p)
        p = [358,417]
        screen.blit(ms_letter, p)
        p = [358,589]
        screen.blit(ms_letter, p)
    if s.game.magic_squares_feature.position >= 2:
        p = [459,777]
        screen.blit(ms_c, p)
        p = [669,419]
        screen.blit(ms_letter, p)
    if s.game.magic_squares_feature.position >= 3:
        p = [521,777]
        screen.blit(small_spotted, p)
    if s.game.magic_squares_feature.position >= 4:
        p = [576,777]
        screen.blit(ms_d, p)
        p = [670,592]
        screen.blit(ms_letter, p)
    if s.game.magic_squares_feature.position >= 5:
        p = [638,777]
        screen.blit(small_spotted, p)

    if s.game.odds1.position == 1:
        p = [13,840]
        screen.blit(g1o1, p)
    elif s.game.odds1.position == 2:
        p = [64,842]
        screen.blit(g1o2, p)
    elif s.game.odds1.position == 3:
        p = [167,840]
        screen.blit(g1o3, p)
    elif s.game.odds1.position == 4:
        p = [203,836]
        screen.blit(g1o4, p)
    elif s.game.odds1.position == 5:
        p = [240,836]
        screen.blit(g1o5, p)
    elif s.game.odds1.position == 6:
        p = [282,832]
        screen.blit(g1o6, p)

    if s.game.odds2.position == 1:
        p = [384,836]
        screen.blit(g2o1, p)
    elif s.game.odds2.position == 2:
        p = [450,838]
        screen.blit(g2o2, p)
    elif s.game.odds2.position == 3:
        p = [534,839]
        screen.blit(g2o3, p)
    elif s.game.odds2.position == 4:
        p = [600,840]
        screen.blit(g2o4, p)
    elif s.game.odds2.position == 5:
        p = [628,838]
        screen.blit(g2o5, p)

    if s.game.magic_squares_feature.position >= 1:
        if s.game.ball_count.position == 3:
            s.cancel_delayed(name="blink")
            blink([s,1,1])
        else:
            s.cancel_delayed(name="blink")
    if s.game.selection_feature.position >= 5:
        if s.game.ball_count.position == 3:
            s.cancel_delayed(name="blink_turn")
            blink_turn([s,1,1])
        else:
            s.cancel_delayed(name="blink_turn")
        
    if s.game.corners.status == True:
        p = [157,253]
        screen.blit(corners, p)

    if s.game.extra_ball.position >= 1:
        p = [151,1009]
        screen.blit(eb_number, p)
    if s.game.extra_ball.position >= 2:
        p = [198,1009]
        screen.blit(eb, p)
    if s.game.extra_ball.position >= 3:
        p = [261,1009]
        screen.blit(eb, p)
    if s.game.extra_ball.position >= 4:
        p = [328,1008]
        screen.blit(eb_number, p)
    if s.game.extra_ball.position >= 5:
        p = [377,1009]
        screen.blit(eb, p)
    if s.game.extra_ball.position >= 6:
        p = [439,1009]
        screen.blit(eb, p)
    if s.game.extra_ball.position >= 7:
        p = [507,1009]
        screen.blit(eb_number, p)
    if s.game.extra_ball.position >= 8:
        p = [554,1008]
        screen.blit(eb, p)
    if s.game.extra_ball.position == 9:
        p = [615,1008]
        screen.blit(eb, p)

    if s.game.eb_play.status == True:
        p = [41,1005]
        screen.blit(extra_balls, p)

    if s.game.red_double.status == True:
        p = [33,697]
        screen.blit(double, p)
    if s.game.yellow_double.status == True:
        p = [95,697]
        screen.blit(double, p)
    if s.game.green_double.status == True:
        p = [154,698]
        screen.blit(double, p)

    if s.game.selection_feature.position == 1:
        p = [37,776]
        screen.blit(s_arrow, p)
    if s.game.selection_feature.position == 2:
        p = [67,776]
        screen.blit(s_arrow, p)
    if s.game.selection_feature.position == 3:
        p = [99,777]
        screen.blit(s_arrow, p)
    if s.game.selection_feature.position == 4:
        p = [133,779]
        screen.blit(s_arrow, p)
    if s.game.selection_feature.position >= 5:
        p = [166,779]
        screen.blit(s_number, p)
    if s.game.selection_feature.position >= 6:
        p = [198,779]
        screen.blit(s_number, p)
    if s.game.selection_feature.position >= 7:
        p = [231,779]
        screen.blit(s_number, p)
    if s.game.selection_feature.position >= 8:
        p = [263,780]
        screen.blit(s_number, p)
    if s.game.selection_feature.position >= 9:
        p = [296,780]
        screen.blit(s_number, p)

    if s.game.game1.status == True and s.game.ball_count.position < 1:
        p = [127,340]
        screen.blit(game, p)
    if s.game.game2.status == True and s.game.ball_count.position < 1:
        p = [478,343]
        screen.blit(game, p)

    if s.game.tilt.status == True:
        tilt_position = [30,239]
        screen.blit(tilt, tilt_position)

    pygame.display.update()

def blink(args):
    dirty_rects = []
    s = args[0]
    b = args[1]
    sl = args[2]

    if b == 0:
        if sl == 1:
            p = [440,731]
            dirty_rects.append(screen.blit(select_now, p))
        pygame.display.update(dirty_rects)
    else:
        dirty_rects.append(screen.blit(bg_gi, (440,731), pygame.Rect(440,731,186,35)))
        pygame.display.update(dirty_rects)
    b = not b

    args = [s,b,sl]

    s.delay(name="blink", delay=0.1, handler=blink, param=args)

def blink_turn(args):
    dirty_rects = []
    s = args[0]
    b = args[1]
    sl = args[2]

    if b == 0:
        if sl == 1:
            p = [215,733]
            dirty_rects.append(screen.blit(turn_now, p))
        pygame.display.update(dirty_rects)
    else:
        dirty_rects.append(screen.blit(bg_gi, (215,733), pygame.Rect(215,733,118,32)))
        pygame.display.update(dirty_rects)
    b = not b

    args = [s,b,sl]

    s.delay(name="blink_turn", delay=0.1, handler=blink_turn, param=args)

def squarea_animation(args):
    dirty_rects = []
    s = args[0]
    num = args[1]
    square = args[2]
    
    if square == 1:
        p = [398,385]
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
        dirty_rects.append(screen.blit(topleft, (410  - num - 10, 392)))
        dirty_rects.append(screen.blit(topright, (456, 395 - num - 7)))
        dirty_rects.append(screen.blit(bottomright, (456  + num + 15, 444)))
        dirty_rects.append(screen.blit(bottomleft, (399, 448 + num + 5)))

    if (s.game.anti_cheat.status == True):
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],120,120)))
    else:
        dirty_rects.append(screen.blit(bg_off, p, pygame.Rect(p[0],p[1],120,120)))
    
    if 2 in s.holes2:
        number_position = [400,505]
        dirty_rects.append(screen.blit(bg_gi, number_position, pygame.Rect(number_position[0],number_position[1],49,51)))
        dirty_rects.append(screen.blit(number, number_position))
    if 12 in s.holes2:
        number_position = [565,506]
        dirty_rects.append(screen.blit(bg_gi, number_position, pygame.Rect(number_position[0],number_position[1],49,51)))
        dirty_rects.append(screen.blit(number, number_position))
    if 16 in s.holes2:
        number_position = [510,506]
        dirty_rects.append(screen.blit(bg_gi, number_position, pygame.Rect(number_position[0],number_position[1],49,51)))
        dirty_rects.append(screen.blit(number, number_position))
    if 18 in s.holes2:
        number_position = [455,505]
        dirty_rects.append(screen.blit(bg_gi, number_position, pygame.Rect(number_position[0],number_position[1],49,51)))
        dirty_rects.append(screen.blit(number, number_position))
    if 24 in s.holes2:
        number_position = [510,448]
        dirty_rects.append(screen.blit(bg_gi, number_position, pygame.Rect(number_position[0],number_position[1],49,51)))
        dirty_rects.append(screen.blit(number, number_position))
    if 25 in s.holes2:
        number_position = [510,391]
        dirty_rects.append(screen.blit(bg_gi, number_position, pygame.Rect(number_position[0],number_position[1],49,51)))
        dirty_rects.append(screen.blit(number, number_position))

    if s.game.magic_squares_feature.position >= 5:
        p = [358,417]
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],42,58)))
        dirty_rects.append(screen.blit(ms_letter, p))
    pygame.display.update(dirty_rects)

def squareb_animation(args):
    dirty_rects = []
    s = args[0]
    num = args[1]
    square = args[2]
    
    if square == 2:
        p = [397,560]
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
        dirty_rects.append(screen.blit(topleft, (418  - num - 23, 565)))
        dirty_rects.append(screen.blit(topright, (454, 568 - num - 9)))
        dirty_rects.append(screen.blit(bottomright, (452  + num + 12, 620)))
        dirty_rects.append(screen.blit(bottomleft, (400, 620 + num + 8)))
    
    if (s.game.anti_cheat.status == True):
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],120,120)))
    else:
        dirty_rects.append(screen.blit(bg_off, p, pygame.Rect(p[0],p[1],120,120)))
    
    if 2 in s.holes2:
        number_position = [400,505]
        dirty_rects.append(screen.blit(bg_gi, number_position, pygame.Rect(number_position[0],number_position[1],49,51)))
        dirty_rects.append(screen.blit(number, number_position))
    if 5 in s.holes2:
        number_position = [508,621]
        dirty_rects.append(screen.blit(bg_gi, number_position, pygame.Rect(number_position[0],number_position[1],49,51)))
        dirty_rects.append(screen.blit(number, number_position))
    if 13 in s.holes2:
        number_position = [511,565]
        dirty_rects.append(screen.blit(bg_gi, number_position, pygame.Rect(number_position[0],number_position[1],49,51)))
        dirty_rects.append(screen.blit(number, number_position))
    if 18 in s.holes2:
        number_position = [455,505]
        dirty_rects.append(screen.blit(bg_gi, number_position, pygame.Rect(number_position[0],number_position[1],49,51)))
        dirty_rects.append(screen.blit(number, number_position))

    if s.game.spot_12.status == True:
        p = [371,704]
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],58,55)))
        dirty_rects.append(screen.blit(large_spotted, p))


    if s.game.magic_squares_feature.position >= 5:
        p = [358,589]
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],42,58)))
        dirty_rects.append(screen.blit(ms_letter, p))

    pygame.display.update(dirty_rects)

def squarec_animation(args):
    dirty_rects = []
    s = args[0]
    num = args[1]
    square = args[2]
    
    if square == 3:
        p = [561,388]
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
        dirty_rects.append(screen.blit(topleft, (576  - num - 16, 394)))
        dirty_rects.append(screen.blit(topright, (617, 388 - num + 0)))
        dirty_rects.append(screen.blit(bottomright, (604  + num + 20, 448)))
        dirty_rects.append(screen.blit(bottomleft, (566, 448 + num + 6)))
    
    if (s.game.anti_cheat.status == True):
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],110,116)))
    else:
        dirty_rects.append(screen.blit(bg_off, p, pygame.Rect(p[0],p[1],110,116)))
    
    if 11 in s.holes2:
        number_position = [620,509]
        dirty_rects.append(screen.blit(bg_gi, number_position, pygame.Rect(number_position[0],number_position[1],49,51)))
        dirty_rects.append(screen.blit(number, number_position))
    if 12 in s.holes2:
        number_position = [565,506]
        dirty_rects.append(screen.blit(bg_gi, number_position, pygame.Rect(number_position[0],number_position[1],49,51)))
        dirty_rects.append(screen.blit(number, number_position))
    if 24 in s.holes2:
        number_position = [510,448]
        dirty_rects.append(screen.blit(bg_gi, number_position, pygame.Rect(number_position[0],number_position[1],49,51)))
        dirty_rects.append(screen.blit(number, number_position))
    if 25 in s.holes2:
        number_position = [510,391]
        dirty_rects.append(screen.blit(bg_gi, number_position, pygame.Rect(number_position[0],number_position[1],49,51)))
        dirty_rects.append(screen.blit(number, number_position))

    if s.game.magic_squares_feature.position >= 5:
        p = [669,419]
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],42,58)))
        dirty_rects.append(screen.blit(ms_letter, p))

    pygame.display.update(dirty_rects)

def squared_animation(args):
    dirty_rects = []
    s = args[0]
    num = args[1]
    square = args[2]
    
    p = [561,561]
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
        dirty_rects.append(screen.blit(topleft, (566 - num - 7, 567)))
        dirty_rects.append(screen.blit(topright, (616, 572 - num - 13)))
        dirty_rects.append(screen.blit(bottomright, (598  + num + 29, 618)))
        dirty_rects.append(screen.blit(bottomleft, (564, 624 + num + 8)))
    
    if (s.game.anti_cheat.status == True):
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],120,120)))
    else:
        dirty_rects.append(screen.blit(bg_off, p, pygame.Rect(p[0],p[1],120,120)))
    
    if 5 in s.holes2:
        number_position = [508,621]
        dirty_rects.append(screen.blit(bg_gi, number_position, pygame.Rect(number_position[0],number_position[1],49,51)))
        dirty_rects.append(screen.blit(number, number_position))
    if 11 in s.holes2:
        number_position = [620,509]
        dirty_rects.append(screen.blit(bg_gi, number_position, pygame.Rect(number_position[0],number_position[1],49,51)))
        dirty_rects.append(screen.blit(number, number_position))
    if 12 in s.holes2:
        number_position = [565,506]
        dirty_rects.append(screen.blit(bg_gi, number_position, pygame.Rect(number_position[0],number_position[1],49,51)))
        dirty_rects.append(screen.blit(number, number_position))
    if 13 in s.holes2:
        number_position = [511,565]
        dirty_rects.append(screen.blit(bg_gi, number_position, pygame.Rect(number_position[0],number_position[1],49,51)))
        dirty_rects.append(screen.blit(number, number_position))

    if s.game.magic_squares_feature.position >= 5:
        p = [670,592]
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],42,58)))
        dirty_rects.append(screen.blit(ms_letter, p))
    pygame.display.update(dirty_rects)


def eb_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]

    if s.game.extra_ball.position < 1:
        dirty_rects.append(screen.blit(bg_gi, (151,1009), pygame.Rect(151,1009,48,34)))
    if s.game.extra_ball.position < 2:
        dirty_rects.append(screen.blit(bg_gi, (198,1009), pygame.Rect(198,1009,63,34)))
    if s.game.extra_ball.position < 3:
        dirty_rects.append(screen.blit(bg_gi, (261,1009), pygame.Rect(261,1009,63,34)))
    if s.game.extra_ball.position < 4:
        dirty_rects.append(screen.blit(bg_gi, (328,1008), pygame.Rect(328,1008,48,34)))
    if s.game.extra_ball.position < 5:
        dirty_rects.append(screen.blit(bg_gi, (377,1009), pygame.Rect(377,1009,63,34)))
    if s.game.extra_ball.position < 6:
        dirty_rects.append(screen.blit(bg_gi, (439,1009), pygame.Rect(439,1009,63,34)))
    if s.game.extra_ball.position < 7:
        dirty_rects.append(screen.blit(bg_gi, (507,1009), pygame.Rect(507,1009,48,34)))
    if s.game.extra_ball.position < 8:
        dirty_rects.append(screen.blit(bg_gi, (554,1008), pygame.Rect(554,1008,63,34)))
    if s.game.extra_ball.position < 9:
        dirty_rects.append(screen.blit(bg_gi, (615,1008), pygame.Rect(615,1008,63,34)))

    pygame.display.update(dirty_rects)

    if num in [1,16,17,26,41,42]:
        if s.game.extra_ball.position < 1:
            p = [151,1009]
            dirty_rects.append(screen.blit(eb_number, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [2,3,18,27,28,43]:
        if s.game.extra_ball.position < 2:
            p = [198,1009]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [4,5,19,29,30,44]:
        if s.game.extra_ball.position < 3:
            p = [261,1009]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [6,7,20,31,32,45]:
        if s.game.extra_ball.position < 4:
            p = [328,1008]
            dirty_rects.append(screen.blit(eb_number, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [8,9,21,33,34,46]:
        if s.game.extra_ball.position < 5:
            p = [377,1009]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [10,11,22,35,36,47]:
        if s.game.extra_ball.position < 6:
            p = [439,1009]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [12,13,23,37,38,48]:
        if s.game.extra_ball.position < 7:
            p = [507,1009]
            dirty_rects.append(screen.blit(eb_number, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [14,15,24,39,40,49]:
        if s.game.extra_ball.position < 8:
            p = [554,1008]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [0,25]:
        if s.game.extra_ball.position < 9:
            p = [615,1008]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects) 
            return

def clear_odds(s, num):
    global screen

    dirty_rects = []

    if s.game.odds1.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (13,840), pygame.Rect(13,840,28,80)))
    if s.game.odds1.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (64,842), pygame.Rect(64,842,30,83)))
    if s.game.odds1.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (167,840), pygame.Rect(167,840,31,88)))
    if s.game.odds1.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (203,836), pygame.Rect(203,836,31,88)))
    if s.game.odds1.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (240,836), pygame.Rect(240,836,34,92)))
    if s.game.odds1.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (282,832), pygame.Rect(282,832,36,96)))
    pygame.display.update(dirty_rects)

def draw_odds_animation(s, num):
    global screen
    dirty_rects = []

    if num in [0,1,25,26]:
        if s.game.odds1.position != 1:
            p = [13,840]
            dirty_rects.append(screen.blit(g1o1, p))
            pygame.display.update(dirty_rects)
            return
    if num in [2,3,27,28]:
        if s.game.odds1.position != 2:
            p = [64,842]
            dirty_rects.append(screen.blit(g1o2, p))
            pygame.display.update(dirty_rects)
            return
    if num in [4,5,29,30]:
        if s.game.odds1.position != 3:
            p = [167,840]
            dirty_rects.append(screen.blit(g1o3, p))
            pygame.display.update(dirty_rects)
            return
    if num in [6,7,31,32]:
        if s.game.odds1.position != 4:
            p = [203,836]
            dirty_rects.append(screen.blit(g1o4, p))
            pygame.display.update(dirty_rects)
            return
    if num in [8,9,33,34]:
        if s.game.odds1.position != 5:
            p = [240,836]
            dirty_rects.append(screen.blit(g1o5, p))
            pygame.display.update(dirty_rects)
            return
    if num in [10,11,35,36]:
        if s.game.odds1.position != 6:
            p = [282,832]
            dirty_rects.append(screen.blit(g1o6, p))
            pygame.display.update(dirty_rects)
            return

def odds_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]

    clear_odds(s, num)

    draw_odds_animation(s, num)

def clear_odds2(s, num):
    global screen

    dirty_rects = []

    if s.game.odds2.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (384,836), pygame.Rect(384,836,58,134)))
    if s.game.odds2.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (450,838), pygame.Rect(450,838,55,138)))
    if s.game.odds2.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (534,839), pygame.Rect(534,839,70,140)))
    if s.game.odds2.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (600,840), pygame.Rect(600,840,36,150)))
    if s.game.odds2.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (628,838), pygame.Rect(628,838,67,144)))
    pygame.display.update(dirty_rects)

def draw_odds_animation2(s, num):
    global screen
    dirty_rects = []

    if num in [14,15,39,40]:
        if s.game.odds2.position != 1:
            p = [384,836]
            dirty_rects.append(screen.blit(g2o1, p))
            pygame.display.update(dirty_rects)
            return
    if num in [16,17,41,42]:
        if s.game.odds2.position != 2:
            p = [450,838]
            dirty_rects.append(screen.blit(g2o2, p))
            pygame.display.update(dirty_rects)
            return
    if num in [18,19,43,44]:
        if s.game.odds2.position != 3:
            p = [534,839]
            dirty_rects.append(screen.blit(g2o3, p))
            pygame.display.update(dirty_rects)
            return
    if num in [20,21,45,46]:
        if s.game.odds2.position != 4:
            p = [600,840]
            dirty_rects.append(screen.blit(g2o4, p))
            pygame.display.update(dirty_rects)
            return
#    if num in [22,23,47,48]:
#        if s.game.odds2.position != 5:
#            p = [628,838]
#            dirty_rects.append(screen.blit(g2o5, p))
#            pygame.display.update(dirty_rects)
#            return

def odds_animation2(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]

    clear_odds2(s, num)

    draw_odds_animation2(s, num)

def clear_features(s, num):
    global screen

    dirty_rects = []

    if s.game.selection_feature.position < 6:
        dirty_rects.append(screen.blit(bg_gi, (166,779), pygame.Rect(166,779,32,34)))
        dirty_rects.append(screen.blit(bg_gi, (198,779), pygame.Rect(198,779,32,34)))
    if s.game.selection_feature.position < 8:
        dirty_rects.append(screen.blit(bg_gi, (231,779), pygame.Rect(231,779,32,34)))
        dirty_rects.append(screen.blit(bg_gi, (263,780), pygame.Rect(263,780,32,34)))
    if s.game.selection_feature.position < 9:
        dirty_rects.append(screen.blit(bg_gi, (296,780), pygame.Rect(296,780,32,34)))
    if s.game.corners.status == False:
        dirty_rects.append(screen.blit(bg_gi, (157,253), pygame.Rect(157,253,58,62)))
    if s.game.red_double.status == False:
        dirty_rects.append(screen.blit(bg_gi, (33,697), pygame.Rect(33,697,55,66)))
    if s.game.yellow_double.status == False:
        dirty_rects.append(screen.blit(bg_gi, (95,697), pygame.Rect(95,697,55,66)))
    if s.game.green_double.status == False:
        dirty_rects.append(screen.blit(bg_gi, (154,698), pygame.Rect(154,698,55,66)))
    
    pygame.display.update(dirty_rects)


def draw_feature_animation(s, num):
    global screen
    dirty_rects = []
    
    if num in [19,20,44,45]:
        if s.game.selection_feature.position < 6:
            p = [166,779]
            dirty_rects.append(screen.blit(s_number, p))
            p = [198,779]
            dirty_rects.append(screen.blit(s_number, p))
            pygame.display.update(dirty_rects)
            return
    if num in [21,22,46,47]:
        if s.game.selection_feature.position < 8:
            p = [231,779]
            dirty_rects.append(screen.blit(s_number, p))
            p = [263,780]
            dirty_rects.append(screen.blit(s_number, p))
            pygame.display.update(dirty_rects)
            return
    if num in [23,24,48,49]:
        if s.game.selection_feature.position < 9:
            p = [296,780]
            dirty_rects.append(screen.blit(s_number, p))
            pygame.display.update(dirty_rects)
            return
    if num in [18,43]:
        if s.game.corners.status == False:
            p = [157,253]
            dirty_rects.append(screen.blit(corners, p))
            pygame.display.update(dirty_rects)
            return
    if num in [16,17,41,42]:
        if s.game.red_double.status == False:
            p = [33,697]
            dirty_rects.append(screen.blit(double, p))
            pygame.display.update(dirty_rects)
            return
    if num in [12,13,37,38]:
        if s.game.yellow_double.status == False:
            p = [95,697]
            dirty_rects.append(screen.blit(double, p))
            pygame.display.update(dirty_rects)
            return
    if num in [14,15,39,40]:
        if s.game.green_double.status == False:
            p = [154,698]
            dirty_rects.append(screen.blit(double, p))
            pygame.display.update(dirty_rects)
            return

def feature_animation2(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]

    clear_features2(s, num)

    draw_feature_animation2(s, num)

def clear_features2(s, num):
    global screen

    dirty_rects = []

    if s.game.magic_squares_feature.position < 1:
        dirty_rects.append(screen.blit(bg_gi, (372,775), pygame.Rect(372,775,87,44)))
        dirty_rects.append(screen.blit(bg_gi, (358,417), pygame.Rect(358,417,42,58)))
        dirty_rects.append(screen.blit(bg_gi, (358,589), pygame.Rect(358,589,42,58)))
    if s.game.magic_squares_feature.position < 2:
        dirty_rects.append(screen.blit(bg_gi, (459,777), pygame.Rect(459,777,64,43)))
        dirty_rects.append(screen.blit(bg_gi, (669,419), pygame.Rect(669,419,42,58)))
    if s.game.magic_squares_feature.position < 3:
        dirty_rects.append(screen.blit(bg_gi, (521,777), pygame.Rect(521,777,57,42)))
    if s.game.magic_squares_feature.position < 4:
        dirty_rects.append(screen.blit(bg_gi, (576,777), pygame.Rect(576,777,62,46)))
        dirty_rects.append(screen.blit(bg_gi, (670,592), pygame.Rect(670,592,42,58)))
    if s.game.magic_squares_feature.position < 5:
        dirty_rects.append(screen.blit(bg_gi, (638,777), pygame.Rect(638,777,57,42)))
    if s.game.spot_12.status == False:
        dirty_rects.append(screen.blit(bg_gi, (371,704), pygame.Rect(371,704,58,55)))
    if s.game.spot_13.status == False:
        dirty_rects.append(screen.blit(bg_gi, (637,704), pygame.Rect(637,704,58,55)))
    
    pygame.display.update(dirty_rects)


def draw_feature_animation2(s, num):
    global screen
    dirty_rects = []
    
    if num in [21,22,46,47]:
        if s.game.magic_squares_feature.position < 1:
            p = [372,775]
            dirty_rects.append(screen.blit(ms_ab, p))
            p = [358,417]
            dirty_rects.append(screen.blit(ms_letter, p))
            p = [358,589]
            dirty_rects.append(screen.blit(ms_letter, p))
            pygame.display.update(dirty_rects)
            return
    if num in [23,24,48,49]:
        if s.game.magic_squares_feature.position < 2:
            p = [459,777]
            dirty_rects.append(screen.blit(ms_c, p))
            p = [669,419]
            dirty_rects.append(screen.blit(ms_letter, p))
    if num in [0,1,25,26]:
        if s.game.magic_squares_feature.position < 3:
            p = [521,777]
            dirty_rects.append(screen.blit(small_spotted, p))
            pygame.display.update(dirty_rects)
            return
    if num in [2,3,27,28]:
        if s.game.magic_squares_feature.position < 4:
            p = [576,777]
            dirty_rects.append(screen.blit(ms_d, p))
            p = [670,592]
            dirty_rects.append(screen.blit(ms_letter, p))
            pygame.display.update(dirty_rects)
            return
    if num in [4,5,29,30]:
        if s.game.magic_squares_feature.position < 5:
            p = [638,777]
            dirty_rects.append(screen.blit(small_spotted, p))
            pygame.display.update(dirty_rects)
            return
    if num in [6,7,31,32,10,11,35,36]:
        if s.game.spot_12.status == False:
            p = [371,704]
            dirty_rects.append(screen.blit(large_spotted, p))
            pygame.display.update(dirty_rects)
            return
    if num in [8,9,33,34]:
        if s.game.spot_13.status == False:
            p = [637,704]
            dirty_rects.append(screen.blit(large_spotted, p))
            pygame.display.update(dirty_rects)
            return

def feature_animation2(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]

    clear_features2(s, num)

    draw_feature_animation2(s, num)

def both_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]

    clear_features(s, num)
    clear_odds(s, num)

    draw_odds_animation(s, num)
    draw_feature_animation(s, num)

def both_animation2(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]

    clear_features2(s, num)
    clear_odds2(s, num)

    draw_odds_animation2(s, num)
    draw_feature_animation2(s, num)

