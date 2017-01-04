
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
        backglass = pygame.image.load('double_header/assets/double_header_menu.png')
    else:
        if (s.game.anti_cheat.status == True):
            backglass = pygame.image.load('double_header/assets/double_header_gi.png')
        else:
            backglass = pygame.image.load('double_header/assets/double_header_off.png')
    backglass = pygame.transform.scale(backglass, (720, 1280))
    
    screen.blit(backglass, backglass_position)


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
            p = [440,731]
            screen.blit(select_now, p)
    if s.game.selection_feature.position >= 5:
        if s.game.ball_count.position == 3:
            p = [215,733]
            screen.blit(turn_now, p)
        
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

    pygame.display.flip()
    pygame.display.update()

def eb_animation(num):

    global screen
    if num == 9:
        p = [151,1009]
        screen.blit(eb_number, p)
        pygame.display.update()
    if num == 8:
        p = [198,1009]
        screen.blit(eb, p)
        pygame.display.update()
    if num == 7:
        p = [261,1009]
        screen.blit(eb, p)
        pygame.display.update()
    if num == 6:
        p = [328,1008]
        screen.blit(eb_number, p)
        pygame.display.update()
    if num == 5:
        p = [377,1009]
        screen.blit(eb, p)
        pygame.display.update()
    if num == 4:
        p = [439,1009]
        screen.blit(eb, p)
        pygame.display.update()
    if num == 3:
        p = [507,1009]
        screen.blit(eb_number, p)
        pygame.display.update()
    if num == 2:
        p = [554,1008]
        screen.blit(eb, p)
        pygame.display.update()
    if num == 1:
        p = [615,1008]
        screen.blit(eb, p)
        pygame.display.update()


def feature_animation(num):
    global screen

    if num == 6:
        p = [157,253]
        screen.blit(corners, p)
    if num == 5:
        p = [33,697]
        screen.blit(double, p)
    if num == 4:
        p = [95,697]
        screen.blit(double, p)
    if num == 3:
        p = [154,698]
        screen.blit(double, p)
    pygame.display.update()
 
def feature_animation2(num):
    global screen

    if num == 6:
        p = [240,649]
        screen.blit(ms_ab, p)
    if num == 5:
        p = [459,777]
        screen.blit(ms_c, p)
    if num == 4:
        p = [576,777]
        screen.blit(ms_d, p)
    if num == 3:
        p = [371,704]
        screen.blit(large_spotted, p)
    if num == 2:
        p = [637,704]
        screen.blit(large_spotted, p)

    pygame.display.update()
  

def odds_animation(num):
    global screen
    if num == 5:
        p = [13,840]
        screen.blit(g1o1, p)
    if num == 4:
        p = [64,842]
        screen.blit(g1o2, p)
    if num == 3:
        p = [167,840]
        screen.blit(g1o3, p)
    if num == 2:
        p = [203,836]
        screen.blit(g1o4, p)
    if num == 1:
        p = [240,836]
        screen.blit(g1o5, p)
    pygame.display.update()

def odds_animation2(num):
    global screen
    if num == 5:
        p = [384,836]
        screen.blit(g2o1, p)
    if num == 4:
        p = [450,838]
        screen.blit(g2o2, p)
    if num == 3:
        p = [534,839]
        screen.blit(g2o3, p)
    if num == 2:
        p = [600,840]
        screen.blit(g2o4, p)
    if num == 1:
        p = [628,838]
        screen.blit(g2o5, p)
    pygame.display.update()
