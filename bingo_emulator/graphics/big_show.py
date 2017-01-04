
import pygame

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

meter = pygame.image.load('graphics/assets/register_cover.png').convert()
number = pygame.image.load('big_show/assets/number.png').convert_alpha()
ms_letter = pygame.image.load('big_show/assets/ms_letter.png').convert_alpha()
ms_number = pygame.image.load('big_show/assets/ms_number.png').convert_alpha()
ms_arrow = pygame.image.load('big_show/assets/ms_arrow.png').convert_alpha()
ms_abc = pygame.image.load('big_show/assets/ms_abc.png').convert_alpha()
ms_d = pygame.image.load('big_show/assets/ms_d.png').convert_alpha()
select_now = pygame.image.load('big_show/assets/select_now.png').convert_alpha()
corners = pygame.image.load('big_show/assets/feature.png').convert_alpha()
ballyhole = pygame.image.load('big_show/assets/feature.png').convert_alpha()
red_odds1 = pygame.image.load('big_show/assets/red_odds1.png').convert_alpha()
red_odds2 = pygame.image.load('big_show/assets/red_odds2.png').convert_alpha()
red_odds3 = pygame.image.load('big_show/assets/red_odds3.png').convert_alpha()
red_odds4 = pygame.image.load('big_show/assets/red_odds4.png').convert_alpha()
red_odds5 = pygame.image.load('big_show/assets/red_odds5.png').convert_alpha()
red_odds6 = pygame.image.load('big_show/assets/red_odds6.png').convert_alpha()
red_odds7 = pygame.image.load('big_show/assets/red_odds7.png').convert_alpha()
red_odds8 = pygame.image.load('big_show/assets/red_odds8.png').convert_alpha()
yellow_odds1 = pygame.image.load('big_show/assets/yellow_odds1.png').convert_alpha()
yellow_odds2 = pygame.image.load('big_show/assets/yellow_odds2.png').convert_alpha()
yellow_odds3 = pygame.image.load('big_show/assets/yellow_odds3.png').convert_alpha()
yellow_odds4 = pygame.image.load('big_show/assets/yellow_odds4.png').convert_alpha()
yellow_odds5 = pygame.image.load('big_show/assets/yellow_odds5.png').convert_alpha()
yellow_odds6 = pygame.image.load('big_show/assets/yellow_odds6.png').convert_alpha()
yellow_odds7 = pygame.image.load('big_show/assets/yellow_odds7.png').convert_alpha()
yellow_odds8 = pygame.image.load('big_show/assets/yellow_odds8.png').convert_alpha()
green_odds1 = pygame.image.load('big_show/assets/green_odds1.png').convert_alpha()
green_odds2 = pygame.image.load('big_show/assets/green_odds2.png').convert_alpha()
green_odds3 = pygame.image.load('big_show/assets/green_odds3.png').convert_alpha()
green_odds4 = pygame.image.load('big_show/assets/green_odds4.png').convert_alpha()
green_odds5 = pygame.image.load('big_show/assets/green_odds5.png').convert_alpha()
green_odds6 = pygame.image.load('big_show/assets/green_odds6.png').convert_alpha()
green_odds7 = pygame.image.load('big_show/assets/green_odds7.png').convert_alpha()
green_odds8 = pygame.image.load('big_show/assets/green_odds8.png').convert_alpha()
extra_balls = pygame.image.load('big_show/assets/extra_balls.png').convert_alpha()
eb = pygame.image.load('big_show/assets/eb.png').convert_alpha()
eb_number = pygame.image.load('big_show/assets/eb_number.png').convert_alpha()
tilt = pygame.image.load('big_show/assets/tilt.png').convert_alpha()
time = pygame.image.load('big_show/assets/time.png').convert_alpha()
a0 = pygame.image.load('big_show/assets/a0.png').convert_alpha()
a1 = pygame.image.load('big_show/assets/a1.png').convert_alpha()
a2 = pygame.image.load('big_show/assets/a2.png').convert_alpha()
a3 = pygame.image.load('big_show/assets/a3.png').convert_alpha()
b0 = pygame.image.load('big_show/assets/b0.png').convert_alpha()
b1 = pygame.image.load('big_show/assets/b1.png').convert_alpha()
b2 = pygame.image.load('big_show/assets/b2.png').convert_alpha()
b3 = pygame.image.load('big_show/assets/b3.png').convert_alpha()
c0 = pygame.image.load('big_show/assets/c0.png').convert_alpha()
c1 = pygame.image.load('big_show/assets/c1.png').convert_alpha()
c2 = pygame.image.load('big_show/assets/c2.png').convert_alpha()
c3 = pygame.image.load('big_show/assets/c3.png').convert_alpha()
d0 = pygame.image.load('big_show/assets/d0.png').convert_alpha()
d1 = pygame.image.load('big_show/assets/d1.png').convert_alpha()
d2 = pygame.image.load('big_show/assets/d2.png').convert_alpha()
d3 = pygame.image.load('big_show/assets/d3.png').convert_alpha()

class scorereel():
    """ Score Reels are used to count replays """
    def __init__(self, pos, image):
        self.position = pos
        self.default_y = self.position[1]
        self.image = pygame.image.load(image).convert()

reel1 = scorereel([97,308], "graphics/assets/white_reel.png")
reel10 = scorereel([78,308], "graphics/assets/white_reel.png")
reel100 = scorereel([59,308], "graphics/assets/white_reel.png")

def display(s, replays=0, menu=False):
    
    meter.set_colorkey((255,0,252))
    meter_position = [50,308]

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
        p = [397,342]
        screen.blit(c0, p)
    if s.game.square_c.position == 1:
        p = [397,342]
        screen.blit(c1, p)
    if s.game.square_c.position == 2:
        p = [397,342]
        screen.blit(c2, p)
    if s.game.square_c.position == 3:
        p = [397,342]
        screen.blit(c3, p)
    if s.game.square_d.position == 0:
        p = [398,509]
        screen.blit(d0, p)
    if s.game.square_d.position == 1:
        p = [398,509]
        screen.blit(d1, p)
    if s.game.square_d.position == 2:
        p = [398,509]
        screen.blit(d2, p)
    if s.game.square_d.position == 3:
        p = [398,509]
        screen.blit(d3, p)


    backglass_position = [0, 0]
    backglass = pygame.Surface(screen.get_size(), flags=pygame.SRCALPHA)
    backglass.fill((0, 0, 0))
    if menu == True:
        backglass = pygame.image.load('big_show/assets/big_show_menu.png')
    else:
        if (s.game.anti_cheat.status == True):
            backglass = pygame.image.load('big_show/assets/big_show_gi.png')
        else:
            backglass = pygame.image.load('big_show/assets/big_show_off.png')
    backglass = pygame.transform.scale(backglass, (720, 1280))
    
    screen.blit(backglass, backglass_position)


    if s.game.tilt.status == False:
        if s.holes:
            if 1 in s.holes:
                if s.game.square_a.position == 0:
                    p = [220,403]
                    screen.blit(number, p)
                elif s.game.square_a.position == 1:
                    p = [221,347]
                    screen.blit(number, p)
                elif s.game.square_a.position == 2:
                    p = [279,347]
                    screen.blit(number, p)
                else:
                    p = [279,403]
                    screen.blit(number, p)
            if 2 in s.holes:
                number_position = [219,459]
                screen.blit(number, number_position)
            if 3 in s.holes:
                if s.game.square_d.position == 0:
                    p = [454,514]
                    screen.blit(number, p)
                elif s.game.square_d.position == 1:
                    p = [456,571]
                    screen.blit(number, p)
                elif s.game.square_d.position == 2:
                    p = [396,569]
                    screen.blit(number, p)
                else:
                    p = [397,514]
                    screen.blit(number, p)
            if 4 in s.holes:
                if s.game.square_a.position == 0:
                    p = [280,347]
                    screen.blit(number, p)
                elif s.game.square_a.position == 1:
                    p = [278,401]
                    screen.blit(number, p)
                elif s.game.square_a.position == 2:
                    p = [219,403]
                    screen.blit(number, p)
                else:
                    p = [222,347]
                    screen.blit(number, p)
            if 5 in s.holes:
                number_position = [339,572]
                screen.blit(number, number_position)
            if 6 in s.holes:
                if s.game.square_c.position == 0:
                    p = [456,349]
                    screen.blit(number, p)
                elif s.game.square_c.position == 1:
                    p = [457,403]
                    screen.blit(number, p)
                elif s.game.square_c.position == 2:
                    p = [397,404]
                    screen.blit(number, p)
                else:
                    p = [399,347]
                    screen.blit(number, p)
            if 7 in s.holes:
                if s.game.square_d.position == 0:
                    p = [397,570]
                    screen.blit(number, p)
                elif s.game.square_d.position == 1:
                    p = [398,514]
                    screen.blit(number, p)
                elif s.game.square_d.position == 2:
                    p = [457,514]
                    screen.blit(number, p)
                else:
                    p = [456,569]
                    screen.blit(number, p)
            if 8 in s.holes:
                if s.game.square_c.position == 0:
                    p = [457,404]
                    screen.blit(number, p)
                elif s.game.square_c.position == 1:
                    p = [397,405]
                    screen.blit(number, p)
                elif s.game.square_c.position == 2:
                    p = [398,346]
                    screen.blit(number, p)
                else:
                    p = [456,347]
                    screen.blit(number, p)
            if 9 in s.holes:
                if s.game.square_a.position == 0:
                    p = [222,347]
                    screen.blit(number, p)
                elif s.game.square_a.position == 1:
                    p = [280,347]
                    screen.blit(number, p)
                elif s.game.square_a.position == 2:
                    p = [279,402]
                    screen.blit(number, p)
                else:
                    p = [220,403]
                    screen.blit(number, p)
            if 10 in s.holes:
                if s.game.square_b.position == 0:
                    p = [218,513]
                    screen.blit(number, p)
                elif s.game.square_b.position == 1:
                    p = [277,515]
                    screen.blit(number, p)
                elif s.game.square_b.position == 2:
                    p = [278,570]
                    screen.blit(number, p)
                else:
                    p = [219,570]
                    screen.blit(number, p)
            if 11 in s.holes:
                number_position = [457,461]
                screen.blit(number, number_position)
            if 12 in s.holes:
                number_position = [398,461]
                screen.blit(number, number_position)
            if 13 in s.holes:
                number_position = [339,515]
                screen.blit(number, number_position)
            if 14 in s.holes:
                if s.game.square_c.position == 0:
                    p = [399,347]
                    screen.blit(number, p)
                elif s.game.square_c.position == 1:
                    p = [457,349]
                    screen.blit(number, p)
                elif s.game.square_c.position == 2:
                    p = [457,404]
                    screen.blit(number, p)
                else:
                    p = [397,404]
                    screen.blit(number, p)
            if 15 in s.holes:
                if s.game.square_b.position == 0:
                    p = [219,569]
                    screen.blit(number, p)
                elif s.game.square_b.position == 1:
                    p = [219,513]
                    screen.blit(number, p)
                elif s.game.square_b.position == 2:
                    p = [279,514]
                    screen.blit(number, p)
                else:
                    p = [279,571]
                    screen.blit(number, p)
            if 16 in s.holes:
                number_position = [338,459]
                screen.blit(number, number_position)
            if 17 in s.holes:
                if s.game.square_d.position == 0:
                    p = [455,571]
                    screen.blit(number, p)
                elif s.game.square_d.position == 1:
                    p = [397,571]
                    screen.blit(number, p)
                elif s.game.square_d.position == 2:
                    p = [398,515]
                    screen.blit(number, p)
                else:
                    p = [456,515]
                    screen.blit(number, p)
            if 18 in s.holes:
                number_position = [279,461]
                screen.blit(number, number_position)
            if 19 in s.holes:
                if s.game.square_a.position == 0:
                    p = [280,402]
                    screen.blit(number, p)
                elif s.game.square_a.position == 1:
                    p = [221,402]
                    screen.blit(number, p)
                elif s.game.square_a.position == 2:
                    p = [222,347]
                    screen.blit(number, p)
                else:
                    p = [280,348]
                    screen.blit(number, p)
            if 20 in s.holes:
                if s.game.square_c.position == 0:
                    p = [398,404]
                    screen.blit(number, p)
                elif s.game.square_c.position == 1:
                    p = [398,347]
                    screen.blit(number, p)
                elif s.game.square_c.position == 2:
                    p = [458,347]
                    screen.blit(number, p)
                else:
                    p = [457,404]
                    screen.blit(number, p)
            if 21 in s.holes:
                if s.game.square_d.position == 0:
                    p = [398,515]
                    screen.blit(number, p)
                elif s.game.square_d.position == 1:
                    p = [457,515]
                    screen.blit(number, p)
                elif s.game.square_d.position == 2:
                    p = [457,571]
                    screen.blit(number, p)
                else:
                    p = [397,570]
                    screen.blit(number, p)
            if 22 in s.holes:
                if s.game.square_b.position == 0:
                    p = [279,514]
                    screen.blit(number, p)
                elif s.game.square_b.position == 1:
                    p = [279,571]
                    screen.blit(number, p)
                elif s.game.square_b.position == 2:
                    p = [220,570]
                    screen.blit(number, p)
                else:
                    p = [221,513]
                    screen.blit(number, p)
            if 23 in s.holes:
                if s.game.square_b.position == 0:
                    p = [279,571]
                    screen.blit(number, p)
                elif s.game.square_b.position == 1:
                    p = [220,570]
                    screen.blit(number, p)
                elif s.game.square_b.position == 2:
                    p = [221,513]
                    screen.blit(number, p)
                else:
                    p = [279,514]
                    screen.blit(number, p)
            if 24 in s.holes:
                number_position = [339,405]
                screen.blit(number, number_position)
            if 25 in s.holes:
                number_position = [341,350]
                screen.blit(number, number_position)


    if s.game.magic_squares_feature.position == 1:
        p = [15,653]
        screen.blit(ms_arrow, p)
    if s.game.magic_squares_feature.position == 2:
        p = [54,653]
        screen.blit(ms_arrow, p)
    if s.game.magic_squares_feature.position == 3:
        p = [94,653]
        screen.blit(ms_arrow, p)
    if s.game.magic_squares_feature.position == 4:
        p = [133,653]
        screen.blit(ms_arrow, p)
    if s.game.magic_squares_feature.position >= 5:
        p = [169,650]
        screen.blit(ms_abc, p)
    if s.game.magic_squares_feature.position >= 6:
        if 2 in s.holes:
            p = [330,653]
            screen.blit(ms_number, p)
        else:
            p = [381,653]
            screen.blit(ms_number, p)
    if s.game.magic_squares_feature.position == 7:
        p = [422,651]
        screen.blit(ms_d, p)

    if s.game.magic_squares_feature.position >= 5:
        p = [166,376]
        screen.blit(ms_letter, p)
        p = [166,544]
        screen.blit(ms_letter, p)
        p = [516,377]
        screen.blit(ms_letter, p)
        if s.game.before_fourth.status == True:
            p = [19,479]
            screen.blit(time, p)
            if s.game.ball_count.position == 3:
                p = [522,668]
                screen.blit(select_now, p)
        elif s.game.before_fifth.status == True:
            p = [20,551]
            screen.blit(time, p)
            if s.game.ball_count.position == 4:
                p = [522,668]
                screen.blit(select_now, p)
    if s.game.magic_squares_feature.position == 7:
        p = [514,545]
        screen.blit(ms_letter, p)

    if s.game.corners.status == True:
        p = [575,483]
        screen.blit(corners, p)

    if s.game.ballyhole.status == True:
        p = [574,554]
        screen.blit(ballyhole, p)

    if s.game.extra_ball.position >= 1:
        p = [134,994]
        screen.blit(eb_number, p)
    if s.game.extra_ball.position >= 2:
        p = [182,994]
        screen.blit(eb, p)
    if s.game.extra_ball.position >= 3:
        p = [252,994]
        screen.blit(eb, p)
    if s.game.extra_ball.position >= 4:
        p = [323,996]
        screen.blit(eb_number, p)
    if s.game.extra_ball.position >= 5:
        p = [373,994]
        screen.blit(eb, p)
    if s.game.extra_ball.position >= 6:
        p = [440,994]
        screen.blit(eb, p)
    if s.game.extra_ball.position >= 7:
        p = [513,995]
        screen.blit(eb_number, p)
    if s.game.extra_ball.position >= 8:
        p = [562,994]
        screen.blit(eb, p)
    if s.game.extra_ball.position == 9:
        p = [630,993]
        screen.blit(eb, p)

    if s.game.eb_play.status == True:
        p = [21,990]
        screen.blit(extra_balls, p)

    if s.game.red_odds.position == 1:
        p = [33,716]
        screen.blit(red_odds1, p)
    elif s.game.red_odds.position == 2:
        p = [ 122,736]
        screen.blit(red_odds2, p)
    elif s.game.red_odds.position == 3:
        p = [205,718]
        screen.blit(red_odds3, p)
    elif s.game.red_odds.position == 4:
        p = [296,738]
        screen.blit(red_odds4, p)
    elif s.game.red_odds.position == 5:
        p = [394,737]
        screen.blit(red_odds5, p)
    elif s.game.red_odds.position == 6:
        p = [481,720]
        screen.blit(red_odds6, p)
    elif s.game.red_odds.position == 7:
        p = [563,733]
        screen.blit(red_odds7, p)
    elif s.game.red_odds.position == 8:
        p = [648,721]
        screen.blit(red_odds8, p)

    if s.game.yellow_odds.position == 1:
        p = [78,821]
        screen.blit(yellow_odds1, p)
    elif s.game.yellow_odds.position == 2:
        p = [129,797]
        screen.blit(yellow_odds2, p)
    elif s.game.yellow_odds.position == 3:
        p = [248,824]
        screen.blit(yellow_odds3, p)
    elif s.game.yellow_odds.position == 4:
        p = [303,795]
        screen.blit(yellow_odds4, p)
    elif s.game.yellow_odds.position == 5:
        p = [384,792]
        screen.blit(yellow_odds5, p)
    elif s.game.yellow_odds.position == 6:
        p = [435,823]
        screen.blit(yellow_odds6, p)
    elif s.game.yellow_odds.position == 7:
        p = [553,793]
        screen.blit(yellow_odds7, p)
    elif s.game.yellow_odds.position == 8:
        p = [601,824]
        screen.blit(yellow_odds8, p)

    if s.game.green_odds.position == 1:
        p = [16,867]
        screen.blit(green_odds1, p)
    elif s.game.green_odds.position == 2:
        p = [140,847]
        screen.blit(green_odds2, p)
    elif s.game.green_odds.position == 3:
        p = [187,870]
        screen.blit(green_odds3, p)
    elif s.game.green_odds.position == 4:
        p = [306,849]
        screen.blit(green_odds4, p)
    elif s.game.green_odds.position == 5:
        p = [367,847]
        screen.blit(green_odds5, p)
    elif s.game.green_odds.position == 6:
        p = [496,874]
        screen.blit(green_odds6, p)
    elif s.game.green_odds.position == 7:
        p = [540,849]
        screen.blit(green_odds7, p)
    elif s.game.green_odds.position == 8:
        p = [661,892]
        screen.blit(green_odds8, p)

    if s.game.tilt.status == True:
        tilt_position = [59,245]
        screen.blit(tilt, tilt_position)

    pygame.display.flip()
    pygame.display.update()

def eb_animation(num):
    global screen

    if num == 9:
        p = [134,994]
        screen.blit(eb_number, p)
        pygame.display.update()
    if num == 8:
        p = [182,994]
        screen.blit(eb, p)
        pygame.display.update()
    if num == 7:
        p = [252,994]
        screen.blit(eb, p)
        pygame.display.update()
    if num == 6:
        p = [323,996]
        screen.blit(eb_number, p)
        pygame.display.update()
    if num == 5:
        p = [373,994]
        screen.blit(eb, p)
        pygame.display.update()
    if num == 4:
        p = [440,994]
        screen.blit(eb, p)
        pygame.display.update()
    if num == 3:
        p = [513,995]
        screen.blit(eb_number, p)
        pygame.display.update()
    if num == 2:
        p = [562,994]
        screen.blit(eb, p)
        pygame.display.update()
    if num == 1:
        p = [630,993]
        screen.blit(eb, p)
        pygame.display.update()


def feature_animation(num):
    global screen
    if num == 6:
        p = [575,483]
        screen.blit(corners, p)
        pygame.display.update()

    if num == 3:
        p = [169,650]
        screen.blit(ms_abc, p)
        pygame.display.update()
   

def odds_animation(num):
    global screen

