
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
bg_menu = pygame.image.load('big_show/assets/big_show_menu.png')
bg_gi = pygame.image.load('big_show/assets/big_show_gi.png')
bg_off = pygame.image.load('big_show/assets/big_show_off.png')

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
                s.cancel_delayed(name="blink")
                blink([s,1,1])
            else:
                s.cancel_delayed(name="blink")
        elif s.game.before_fifth.status == True:
            p = [20,551]
            screen.blit(time, p)
            if s.game.ball_count.position == 4:
                s.cancel_delayed(name="blink")
                blink([s,1,1])
            else:
                s.cancel_delayed(name="blink")

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

    pygame.display.update()


def blink(args):
    dirty_rects = []
    s = args[0]
    b = args[1]
    sl = args[2]

    if b == 0:
        if sl == 1:
            p = [522,668]
            dirty_rects.append(screen.blit(select_now, p))
        pygame.display.update(dirty_rects)
    else:
        dirty_rects.append(screen.blit(bg_gi, (522,668), pygame.Rect(522,668,186,31)))
        pygame.display.update(dirty_rects)
    b = not b

    args = [s,b,sl]

    s.delay(name="blink", delay=0.1, handler=blink, param=args)

def eb_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]
    if s.game.extra_ball.position < 1:
        dirty_rects.append(screen.blit(bg_gi, (134,994), pygame.Rect(134,994,47,29)))
    if s.game.extra_ball.position < 2:
        dirty_rects.append(screen.blit(bg_gi, (182,994), pygame.Rect(182,994,68,31)))
    if s.game.extra_ball.position < 3:
        dirty_rects.append(screen.blit(bg_gi, (252,994), pygame.Rect(252,994,68,31)))
    if s.game.extra_ball.position < 4:
        dirty_rects.append(screen.blit(bg_gi, (323,996), pygame.Rect(323,996,47,29)))
    if s.game.extra_ball.position < 5:
        dirty_rects.append(screen.blit(bg_gi, (373,994), pygame.Rect(373,994,68,31)))
    if s.game.extra_ball.position < 6:
        dirty_rects.append(screen.blit(bg_gi, (440,994), pygame.Rect(440,994,68,31)))
    if s.game.extra_ball.position < 7:
        dirty_rects.append(screen.blit(bg_gi, (513,995), pygame.Rect(513,995,47,29)))
    if s.game.extra_ball.position < 8:
        dirty_rects.append(screen.blit(bg_gi, (562,994), pygame.Rect(562,994,68,31)))
    if s.game.extra_ball.position < 9:
        dirty_rects.append(screen.blit(bg_gi, (630,993), pygame.Rect(630,993,68,31)))
    pygame.display.update(dirty_rects)

    if num in [0,25,14,49]:
        if s.game.extra_ball.position < 1:
            p = [134,994]
            dirty_rects.append(screen.blit(eb_number, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [39,1,26,15]:
        if s.game.extra_ball.position < 2:
            p = [182,994]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [3,4,17,28,29,40]:
        if s.game.extra_ball.position < 3:
            p = [252,994]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [5,18,30,43]:
        if s.game.extra_ball.position < 4:
            p = [323,996]
            dirty_rects.append(screen.blit(eb_number, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [7,8,19,32,33,44]:
        if s.game.extra_ball.position < 5:
            p = [373,994]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [9,10,20,34,35,45]:
        if s.game.extra_ball.position < 6:
            p = [440,994]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [11,21,36,46]:
        if s.game.extra_ball.position < 7:
            p = [513,995]
            dirty_rects.append(screen.blit(eb_number, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [12,22,37,47]:
        if s.game.extra_ball.position < 8:
            p = [562,994]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [2,6,13,16,23,27,31,38,41,48]:
        if s.game.extra_ball.position < 9:
            p = [630,993]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return

def clear_odds(s, num):
    global screen

    dirty_rects = []

    if s.game.yellow_odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (78,821), pygame.Rect(78,821,38,51)))
    if s.game.yellow_odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (129,797), pygame.Rect(129,797,38,51)))
    if s.game.yellow_odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (248,824), pygame.Rect(248,824,38,51)))
    if s.game.yellow_odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (303,795), pygame.Rect(303,795,38,51)))
    if s.game.yellow_odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (384,792), pygame.Rect(384,792,38,51)))
    if s.game.yellow_odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (435,823), pygame.Rect(435,823,38,51)))
    if s.game.yellow_odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (553,793), pygame.Rect(553,793,38,51)))
    if s.game.yellow_odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (601,824), pygame.Rect(601,824,38,51)))

    if s.game.red_odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (33,716), pygame.Rect(33,716,38,51)))
    if s.game.red_odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (122,736), pygame.Rect(122,736,38,51)))
    if s.game.red_odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (205,718), pygame.Rect(205,718,38,51)))
    if s.game.red_odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (296,738), pygame.Rect(296,738,38,51)))
    if s.game.red_odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (394,737), pygame.Rect(394,737,38,51)))
    if s.game.red_odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (481,720), pygame.Rect(481,720,38,51)))
    if s.game.red_odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (563,733), pygame.Rect(563,733,38,51)))
    if s.game.red_odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (648,721), pygame.Rect(648,721,38,51)))

    if s.game.green_odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (16,867), pygame.Rect(16,867,38,51)))
    if s.game.green_odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (140,847), pygame.Rect(140,847,38,51)))
    if s.game.green_odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (187,870), pygame.Rect(187,870,38,51)))
    if s.game.green_odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (306,849), pygame.Rect(306,849,42,50)))
    if s.game.green_odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (367,847), pygame.Rect(367,847,48,50)))
    if s.game.green_odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (496,874), pygame.Rect(496,874,35,48)))
    if s.game.green_odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (540,849), pygame.Rect(540,849,43,52)))
    if s.game.green_odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (661,892), pygame.Rect(661,892,43,52)))


    pygame.display.update(dirty_rects)

def draw_odds_animation(s, num):
    global screen
    dirty_rects = []

    if num in [11,36]:
        if s.game.yellow_odds.position != 1:
            p = [78,821]
            dirty_rects.append(screen.blit(yellow_odds1, p))
            pygame.display.update(dirty_rects)
            return
    if num in [4,29]:
        if s.game.yellow_odds.position != 2:
            p = [129,797]
            dirty_rects.append(screen.blit(yellow_odds2, p))
            pygame.display.update(dirty_rects)
            return
    if num in [7,32]:
        if s.game.yellow_odds.position != 3:
            p = [248,824]
            dirty_rects.append(screen.blit(yellow_odds3, p))
            pygame.display.update(dirty_rects)
            return
    if num in [13,38]:
        if s.game.yellow_odds.position != 4:
            p = [303,795]
            dirty_rects.append(screen.blit(yellow_odds4, p))
            pygame.display.update(dirty_rects)
            return
    if num in [23,48]:
        if s.game.yellow_odds.position != 5:
            p = [384,792]
            dirty_rects.append(screen.blit(yellow_odds5, p))
            pygame.display.update(dirty_rects)
            return
    if num in [17,42]:
        if s.game.yellow_odds.position != 6:
            p = [435,823]
            dirty_rects.append(screen.blit(yellow_odds6, p))
            pygame.display.update(dirty_rects)
            return
    if num in [19,44]:
        if s.game.yellow_odds.position != 7:
            p = [553,793]
            dirty_rects.append(screen.blit(yellow_odds7, p))
            pygame.display.update(dirty_rects)
            return
    if num in [5,30]:
        if s.game.yellow_odds.position != 8:
            p = [601,824]
            dirty_rects.append(screen.blit(yellow_odds8, p))
            pygame.display.update(dirty_rects)
            return

    if num in [2,27]:
        if s.game.red_odds.position != 1:
            p = [33,716]
            dirty_rects.append(screen.blit(red_odds1, p))
            pygame.display.update(dirty_rects)
            return
    if num in [15,40]:
        if s.game.red_odds.position != 2:
            p = [122,736]
            dirty_rects.append(screen.blit(red_odds2, p))
            pygame.display.update(dirty_rects)
            return
    if num in [0,25]:
        if s.game.red_odds.position != 3:
            p = [205,718]
            dirty_rects.append(screen.blit(red_odds3, p))
            pygame.display.update(dirty_rects)
            return
    if num in [9,34]:
        if s.game.red_odds.position != 4:
            p = [296,738]
            dirty_rects.append(screen.blit(red_odds4, p))
            pygame.display.update(dirty_rects)
            return
    if num in [20,45]:
        if s.game.red_odds.position != 5:
            p = [394,737]
            dirty_rects.append(screen.blit(red_odds5, p))
            pygame.display.update(dirty_rects)
            return
    if num in [12,37]:
        if s.game.red_odds.position != 6:
            p = [481,720]
            dirty_rects.append(screen.blit(red_odds6, p))
            pygame.display.update(dirty_rects)
            return
    if num in [1,26]:
        if s.game.red_odds.position != 7:
            p = [563,733]
            dirty_rects.append(screen.blit(red_odds7, p))
            pygame.display.update(dirty_rects)
            return
    if num in [6,31]:
        if s.game.red_odds.position != 8:
            p = [648,721]
            dirty_rects.append(screen.blit(red_odds8, p))
            pygame.display.update(dirty_rects)
            return

    if num in [16,41]:
        if s.game.green_odds.position != 1:
            p = [16,867]
            dirty_rects.append(screen.blit(green_odds1, p))
            pygame.display.update(dirty_rects)
            return
    if num in [18,43]:
        if s.game.green_odds.position != 2:
            p = [140,847]
            dirty_rects.append(screen.blit(green_odds2, p))
            pygame.display.update(dirty_rects)
            return
    if num in [14,39]:
        if s.game.green_odds.position != 3:
            p = [187,870]
            dirty_rects.append(screen.blit(green_odds3, p))
            pygame.display.update(dirty_rects)
            return
    if num in [3,28]:
        if s.game.green_odds.position != 4:
            p = [306,849]
            dirty_rects.append(screen.blit(green_odds4, p))
            pygame.display.update(dirty_rects)
            return
    if num in [24,49]:
        if s.game.green_odds.position != 5:
            p = [367,847]
            dirty_rects.append(screen.blit(green_odds5, p))
            pygame.display.update(dirty_rects)
            return
    if num in [8,33]:
        if s.game.green_odds.position != 6:
            p = [496,874]
            dirty_rects.append(screen.blit(green_odds6, p))
            pygame.display.update(dirty_rects)
            return
    if num in [21,46]:
        if s.game.green_odds.position != 7:
            p = [540,849]
            dirty_rects.append(screen.blit(green_odds7, p))
            pygame.display.update(dirty_rects)
            return
    if num in [11,36]:
        if s.game.green_odds.position != 8:
            p = [661,892]
            dirty_rects.append(screen.blit(green_odds8, p))
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
        dirty_rects.append(screen.blit(bg_gi, (166,376), pygame.Rect(166,376,49,46)))
        dirty_rects.append(screen.blit(bg_gi, (166,544), pygame.Rect(166,544,49,46)))
        dirty_rects.append(screen.blit(bg_gi, (516,377), pygame.Rect(516,377,49,46)))
        dirty_rects.append(screen.blit(bg_gi, (19,479), pygame.Rect(19,479,134,74)))
    if s.game.before_fifth.status == False:
        dirty_rects.append(screen.blit(bg_gi, (20,551), pygame.Rect(20,551,134,74)))
    if s.game.magic_squares_feature.position < 6:
        if 2 not in s.holes:
            dirty_rects.append(screen.blit(bg_gi, (330,653), pygame.Rect(330,653,29,30)))
        if 18 not in s.holes:
            dirty_rects.append(screen.blit(bg_gi, (381,653), pygame.Rect(381,653,29,30)))
    if s.game.magic_squares_feature.position < 7:
        dirty_rects.append(screen.blit(bg_gi, (514,545), pygame.Rect(514,545,49,46)))
    if s.game.corners.status == False:
        dirty_rects.append(screen.blit(bg_gi, (575,483), pygame.Rect(575,483,131,71)))
    if s.game.ballyhole.status == False:
        dirty_rects.append(screen.blit(bg_gi, (574,554), pygame.Rect(574,554,131,71)))

    pygame.display.update(dirty_rects)


def draw_feature_animation(s, num):
    global screen
    dirty_rects = []


    if num in [3,28,10,35,17,42,23,48]:
        if s.game.magic_squares_feature.position < 5:
            p = [166,376]
            dirty_rects.append(screen.blit(ms_letter, p))
            p = [166,544]
            dirty_rects.append(screen.blit(ms_letter, p))
            p = [516,377]
            dirty_rects.append(screen.blit(ms_letter, p))
            p = [19,479]
            dirty_rects.append(screen.blit(time, p))
            pygame.display.update(dirty_rects)
            return
    if num in [0,29,35,41,25,4,10,16]:
        if s.game.before_fifth.status == False:
            p = [20,551]
            dirty_rects.append(screen.blit(time, p))
            pygame.display.update(dirty_rects)
            return
    if num in [5,12,19,30,37,44]:
        if s.game.magic_squares_feature.position < 6:
            p = [330,653]
            dirty_rects.append(screen.blit(ms_number, p))
            pygame.display.update(dirty_rects)
            return
    if num in [8,15,22,33,40,47]:
        if s.game.magic_squares_feature.position < 6:
            p = [381,653]
            dirty_rects.append(screen.blit(ms_number, p))
            pygame.display.update(dirty_rects)
            return
    if num in [7,14,21,25,50,46,39,32]:
        if s.game.magic_squares_feature.position < 7:
            p = [514,545]
            dirty_rects.append(screen.blit(ms_letter, p))
            pygame.display.update(dirty_rects)
            return
    if num in [2,9,16,27,34,41]:
        if s.game.corners.status == False:
            p = [575,483]
            dirty_rects.append(screen.blit(corners, p))
            pygame.display.update(dirty_rects)
            return
    if num in [6,13,20,24,31,38,45,49]:
        if s.game.ballyhole.status == False:
            p = [574,554]
            dirty_rects.append(screen.blit(ballyhole, p))
            pygame.display.update(dirty_rects)
            return

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


