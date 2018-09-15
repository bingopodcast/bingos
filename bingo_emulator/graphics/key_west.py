
import pygame

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

meter = pygame.image.load('graphics/assets/register_cover.png').convert()
number = pygame.image.load('key_west/assets/number.png').convert_alpha()
feature = pygame.image.load('key_west/assets/feature.png').convert_alpha()
ms_letter = pygame.image.load('key_west/assets/ms_letter.png').convert_alpha()
ms_number = pygame.image.load('key_west/assets/ms_number.png').convert_alpha()
ms_arrow = pygame.image.load('key_west/assets/ms_arrow.png').convert_alpha()
ms_abc = pygame.image.load('key_west/assets/ms_abc.png').convert_alpha()
ms_d = pygame.image.load('key_west/assets/ms_d.png').convert_alpha()
select_now = pygame.image.load('key_west/assets/time.png').convert_alpha()
select_a_score = pygame.image.load('key_west/assets/select_a_score.png').convert_alpha()
score_selected = pygame.image.load('key_west/assets/selected_score.png').convert_alpha()
corners = pygame.image.load('key_west/assets/feature.png').convert_alpha()
ballyhole = pygame.image.load('key_west/assets/ballyhole.png').convert_alpha()
red_odds1 = pygame.image.load('key_west/assets/red_odds1.png').convert_alpha()
red_odds2 = pygame.image.load('key_west/assets/red_odds2.png').convert_alpha()
red_odds3 = pygame.image.load('key_west/assets/red_odds3.png').convert_alpha()
red_odds4 = pygame.image.load('key_west/assets/red_odds4.png').convert_alpha()
red_odds5 = pygame.image.load('key_west/assets/red_odds5.png').convert_alpha()
red_odds6 = pygame.image.load('key_west/assets/red_odds6.png').convert_alpha()
red_odds7 = pygame.image.load('key_west/assets/red_odds7.png').convert_alpha()
red_odds8 = pygame.image.load('key_west/assets/red_odds8.png').convert_alpha()
yellow_odds1 = pygame.image.load('key_west/assets/yellow_odds1.png').convert_alpha()
yellow_odds2 = pygame.image.load('key_west/assets/yellow_odds2.png').convert_alpha()
yellow_odds3 = pygame.image.load('key_west/assets/yellow_odds3.png').convert_alpha()
yellow_odds4 = pygame.image.load('key_west/assets/yellow_odds4.png').convert_alpha()
yellow_odds5 = pygame.image.load('key_west/assets/yellow_odds5.png').convert_alpha()
yellow_odds6 = pygame.image.load('key_west/assets/yellow_odds6.png').convert_alpha()
yellow_odds7 = pygame.image.load('key_west/assets/yellow_odds7.png').convert_alpha()
yellow_odds8 = pygame.image.load('key_west/assets/yellow_odds8.png').convert_alpha()
green_odds1 = pygame.image.load('key_west/assets/green_odds1.png').convert_alpha()
green_odds2 = pygame.image.load('key_west/assets/green_odds2.png').convert_alpha()
green_odds3 = pygame.image.load('key_west/assets/green_odds3.png').convert_alpha()
green_odds4 = pygame.image.load('key_west/assets/green_odds4.png').convert_alpha()
green_odds5 = pygame.image.load('key_west/assets/green_odds5.png').convert_alpha()
green_odds6 = pygame.image.load('key_west/assets/green_odds6.png').convert_alpha()
green_odds7 = pygame.image.load('key_west/assets/green_odds7.png').convert_alpha()
green_odds8 = pygame.image.load('key_west/assets/green_odds8.png').convert_alpha()
extra_balls = pygame.image.load('key_west/assets/extra_balls.png').convert_alpha()
eb = pygame.image.load('key_west/assets/eb.png').convert_alpha()
eb_number = pygame.image.load('key_west/assets/eb_number.png').convert_alpha()
tilt = pygame.image.load('key_west/assets/tilt.png').convert_alpha()
time = pygame.image.load('key_west/assets/time.png').convert_alpha()
a0 = pygame.image.load('key_west/assets/a0.png').convert_alpha()
a1 = pygame.image.load('key_west/assets/a1.png').convert_alpha()
a2 = pygame.image.load('key_west/assets/a2.png').convert_alpha()
a3 = pygame.image.load('key_west/assets/a3.png').convert_alpha()
b0 = pygame.image.load('key_west/assets/b0.png').convert_alpha()
b1 = pygame.image.load('key_west/assets/b1.png').convert_alpha()
b2 = pygame.image.load('key_west/assets/b2.png').convert_alpha()
b3 = pygame.image.load('key_west/assets/b3.png').convert_alpha()
c0 = pygame.image.load('key_west/assets/c0.png').convert_alpha()
c1 = pygame.image.load('key_west/assets/c1.png').convert_alpha()
c2 = pygame.image.load('key_west/assets/c2.png').convert_alpha()
c3 = pygame.image.load('key_west/assets/c3.png').convert_alpha()
d0 = pygame.image.load('key_west/assets/d0.png').convert_alpha()
d1 = pygame.image.load('key_west/assets/d1.png').convert_alpha()
d2 = pygame.image.load('key_west/assets/d2.png').convert_alpha()
d3 = pygame.image.load('key_west/assets/d3.png').convert_alpha()
rollover = pygame.image.load('key_west/assets/star.png').convert_alpha()
bg_menu = pygame.image.load('key_west/assets/key_west_menu.png')
bg_gi = pygame.image.load('key_west/assets/key_west_gi.png')
bg_off = pygame.image.load('key_west/assets/key_west_off.png')
a_1 = pygame.image.load('key_west/assets/a-1.png').convert_alpha()
a_2 = pygame.image.load('key_west/assets/a-2.png').convert_alpha()
a_3 = pygame.image.load('key_west/assets/a-3.png').convert_alpha()
a_4 = pygame.image.load('key_west/assets/a-4.png').convert_alpha()
b_1 = pygame.image.load('key_west/assets/b-1.png').convert_alpha()
b_2 = pygame.image.load('key_west/assets/b-2.png').convert_alpha()
b_3 = pygame.image.load('key_west/assets/b-3.png').convert_alpha()
b_4 = pygame.image.load('key_west/assets/b-4.png').convert_alpha()
c_1 = pygame.image.load('key_west/assets/c-1.png').convert_alpha()
c_2 = pygame.image.load('key_west/assets/c-2.png').convert_alpha()
c_3 = pygame.image.load('key_west/assets/c-3.png').convert_alpha()
c_4 = pygame.image.load('key_west/assets/c-4.png').convert_alpha()
d_1 = pygame.image.load('key_west/assets/d-1.png').convert_alpha()
d_2 = pygame.image.load('key_west/assets/d-2.png').convert_alpha()
d_3 = pygame.image.load('key_west/assets/d-3.png').convert_alpha()
d_4 = pygame.image.load('key_west/assets/d-4.png').convert_alpha()


class scorereel():
    """ Score Reels are used to count replays """
    def __init__(self, pos, image):
        self.position = pos
        self.default_y = self.position[1]
        self.image = pygame.image.load(image).convert()

reel1 = scorereel([97,289], "graphics/assets/white_reel.png")
reel10 = scorereel([78,289], "graphics/assets/white_reel.png")
reel100 = scorereel([59,289], "graphics/assets/white_reel.png")

def display(s, replays=0, menu=False):
    
    meter.set_colorkey((255,0,252))
    meter_position = [50,289]

    screen.blit(reel1.image, reel1.position)
    screen.blit(reel10.image, reel10.position)
    screen.blit(reel100.image, reel100.position)
    screen.blit(meter, meter_position)

    if s.game.square_a.position == 0:
        p = [217,332]
        screen.blit(a0, p)
    if s.game.square_a.position == 1:
        p = [217,332]
        screen.blit(a1, p)
    if s.game.square_a.position == 2:
        p = [217,332]
        screen.blit(a2, p)
    if s.game.square_a.position == 3:
        p = [217,332]
        screen.blit(a3, p)
    if s.game.square_b.position == 0:
        p = [216,505]
        screen.blit(b0, p)
    if s.game.square_b.position == 1:
        p = [216,505]
        screen.blit(b1, p)
    if s.game.square_b.position == 2:
        p = [216,505]
        screen.blit(b2, p)
    if s.game.square_b.position == 3:
        p = [216,505]
        screen.blit(b3, p)
    if s.game.square_c.position == 0:
        p = [394,332]
        screen.blit(c0, p)
    if s.game.square_c.position == 1:
        p = [394,332]
        screen.blit(c1, p)
    if s.game.square_c.position == 2:
        p = [394,332]
        screen.blit(c2, p)
    if s.game.square_c.position == 3:
        p = [394,332]
        screen.blit(c3, p)
    if s.game.square_d.position == 0:
        p = [394,505]
        screen.blit(d0, p)
    if s.game.square_d.position == 1:
        p = [394,505]
        screen.blit(d1, p)
    if s.game.square_d.position == 2:
        p = [394,505]
        screen.blit(d2, p)
    if s.game.square_d.position == 3:
        p = [394,505]
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
                    p = [220,389]
                    screen.blit(number, p)
                elif s.game.square_a.position == 1:
                    p = [221,332]
                    screen.blit(number, p)
                elif s.game.square_a.position == 2:
                    p = [279,332]
                    screen.blit(number, p)
                else:
                    p = [279,389]
                    screen.blit(number, p)
            if 2 in s.holes:
                number_position = [219,444]
                screen.blit(number, number_position)
            if 3 in s.holes:
                if s.game.square_d.position == 0:
                    p = [454,501]
                    screen.blit(number, p)
                elif s.game.square_d.position == 1:
                    p = [456,558]
                    screen.blit(number, p)
                elif s.game.square_d.position == 2:
                    p = [396,556]
                    screen.blit(number, p)
                else:
                    p = [397,501]
                    screen.blit(number, p)
            if 4 in s.holes:
                if s.game.square_a.position == 0:
                    p = [280,332]
                    screen.blit(number, p)
                elif s.game.square_a.position == 1:
                    p = [278,386]
                    screen.blit(number, p)
                elif s.game.square_a.position == 2:
                    p = [219,386]
                    screen.blit(number, p)
                else:
                    p = [222,332]
                    screen.blit(number, p)
            if 5 in s.holes:
                number_position = [339,560]
                screen.blit(number, number_position)
            if 6 in s.holes:
                if s.game.square_c.position == 0:
                    p = [454,332]
                    screen.blit(number, p)
                elif s.game.square_c.position == 1:
                    p = [454,386]
                    screen.blit(number, p)
                elif s.game.square_c.position == 2:
                    p = [397,386]
                    screen.blit(number, p)
                else:
                    p = [399,332]
                    screen.blit(number, p)
            if 7 in s.holes:
                if s.game.square_d.position == 0:
                    p = [397,558]
                    screen.blit(number, p)
                elif s.game.square_d.position == 1:
                    p = [398,502]
                    screen.blit(number, p)
                elif s.game.square_d.position == 2:
                    p = [457,502]
                    screen.blit(number, p)
                else:
                    p = [456,558]
                    screen.blit(number, p)
            if 8 in s.holes:
                if s.game.square_c.position == 0:
                    p = [453,389]
                    screen.blit(number, p)
                elif s.game.square_c.position == 1:
                    p = [393,390]
                    screen.blit(number, p)
                elif s.game.square_c.position == 2:
                    p = [394,331]
                    screen.blit(number, p)
                else:
                    p = [452,331]
                    screen.blit(number, p)
            if 9 in s.holes:
                if s.game.square_a.position == 0:
                    p = [222,332]
                    screen.blit(number, p)
                elif s.game.square_a.position == 1:
                    p = [280,332]
                    screen.blit(number, p)
                elif s.game.square_a.position == 2:
                    p = [279,387]
                    screen.blit(number, p)
                else:
                    p = [220,388]
                    screen.blit(number, p)
            if 10 in s.holes:
                if s.game.square_b.position == 0:
                    p = [218,500]
                    screen.blit(number, p)
                elif s.game.square_b.position == 1:
                    p = [277,502]
                    screen.blit(number, p)
                elif s.game.square_b.position == 2:
                    p = [278,557]
                    screen.blit(number, p)
                else:
                    p = [219,557]
                    screen.blit(number, p)
            if 11 in s.holes:
                number_position = [455,446]
                screen.blit(number, number_position)
            if 12 in s.holes:
                number_position = [395,446]
                screen.blit(number, number_position)
            if 13 in s.holes:
                number_position = [336,502]
                screen.blit(number, number_position)
            if 14 in s.holes:
                if s.game.square_c.position == 0:
                    p = [395,330]
                    screen.blit(number, p)
                elif s.game.square_c.position == 1:
                    p = [454,332]
                    screen.blit(number, p)
                elif s.game.square_c.position == 2:
                    p = [454,387]
                    screen.blit(number, p)
                else:
                    p = [395,387]
                    screen.blit(number, p)
            if 15 in s.holes:
                if s.game.square_b.position == 0:
                    p = [219,565]
                    screen.blit(number, p)
                elif s.game.square_b.position == 1:
                    p = [219,509]
                    screen.blit(number, p)
                elif s.game.square_b.position == 2:
                    p = [279,510]
                    screen.blit(number, p)
                else:
                    p = [279,567]
                    screen.blit(number, p)
            if 16 in s.holes:
                number_position = [338,445]
                screen.blit(number, number_position)
            if 17 in s.holes:
                if s.game.square_d.position == 0:
                    p = [453,560]
                    screen.blit(number, p)
                elif s.game.square_d.position == 1:
                    p = [395,560]
                    screen.blit(number, p)
                elif s.game.square_d.position == 2:
                    p = [396,504]
                    screen.blit(number, p)
                else:
                    p = [454,504]
                    screen.blit(number, p)
            if 18 in s.holes:
                number_position = [279,448]
                screen.blit(number, number_position)
            if 19 in s.holes:
                if s.game.square_a.position == 0:
                    p = [277,390]
                    screen.blit(number, p)
                elif s.game.square_a.position == 1:
                    p = [218,390]
                    screen.blit(number, p)
                elif s.game.square_a.position == 2:
                    p = [220,335]
                    screen.blit(number, p)
                else:
                    p = [278,356]
                    screen.blit(number, p)
            if 20 in s.holes:
                if s.game.square_c.position == 0:
                    p = [393,390]
                    screen.blit(number, p)
                elif s.game.square_c.position == 1:
                    p = [393,333]
                    screen.blit(number, p)
                elif s.game.square_c.position == 2:
                    p = [452,333]
                    screen.blit(number, p)
                else:
                    p = [453,390]
                    screen.blit(number, p)
            if 21 in s.holes:
                if s.game.square_d.position == 0:
                    p = [394,500]
                    screen.blit(number, p)
                elif s.game.square_d.position == 1:
                    p = [453,500]
                    screen.blit(number, p)
                elif s.game.square_d.position == 2:
                    p = [453,556]
                    screen.blit(number, p)
                else:
                    p = [395,556]
                    screen.blit(number, p)
            if 22 in s.holes:
                if s.game.square_b.position == 0:
                    p = [279,504]
                    screen.blit(number, p)
                elif s.game.square_b.position == 1:
                    p = [279,561]
                    screen.blit(number, p)
                elif s.game.square_b.position == 2:
                    p = [220,561]
                    screen.blit(number, p)
                else:
                    p = [221,503]
                    screen.blit(number, p)
            if 23 in s.holes:
                if s.game.square_b.position == 0:
                    p = [279,563]
                    screen.blit(number, p)
                elif s.game.square_b.position == 1:
                    p = [220,562]
                    screen.blit(number, p)
                elif s.game.square_b.position == 2:
                    p = [221,505]
                    screen.blit(number, p)
                else:
                    p = [279,506]
                    screen.blit(number, p)
            if 24 in s.holes:
                number_position = [336,390]
                screen.blit(number, number_position)
            if 25 in s.holes:
                number_position = [337,332]
                screen.blit(number, number_position)


    if s.game.magic_squares_feature.position == 1:
        p = [15,648]
        screen.blit(ms_arrow, p)
    if s.game.magic_squares_feature.position == 2:
        p = [56,646]
        screen.blit(ms_arrow, p)
    if s.game.magic_squares_feature.position == 3:
        p = [96,646]
        screen.blit(ms_arrow, p)
    if s.game.magic_squares_feature.position == 4:
        p = [135,646]
        screen.blit(ms_arrow, p)
    if s.game.magic_squares_feature.position >= 5:
        p = [173,644]
        screen.blit(ms_abc, p)
    if s.game.magic_squares_feature.position >= 6:
        if 2 in s.holes:
            p = [330,649]
            screen.blit(ms_number, p)
        else:
            p = [379,649]
            screen.blit(ms_number, p)
    if s.game.magic_squares_feature.position == 7:
        p = [418,645]
        screen.blit(ms_d, p)

    if s.game.rollovers.status == True:
        if s.game.active == "yellow":
            p = [28,942]
            screen.blit(rollover, p)
        else:
            p = [631,941]
            screen.blit(rollover, p)

    if s.game.magic_squares_feature.position >= 5:
        p = [166,359]
        screen.blit(ms_letter, p)
        p = [166,533]
        screen.blit(ms_letter, p)
        p = [508,360]
        screen.blit(ms_letter, p)
        if s.game.before_fourth.status == True:
            p = [27,517]
            screen.blit(feature, p)
            if s.game.ball_count.position == 3:
                s.cancel_delayed(name="blink")
                blink([s,1,1])
            else:
                s.cancel_delayed(name="blink")
        elif s.game.after_fifth.status == True:
            p = [9,583]
            screen.blit(time, p)
            if s.game.ball_count.position == 4:
                s.cancel_delayed(name="blink")
                blink([s,1,1])
            else:
                s.cancel_delayed(name="blink")
    if s.game.magic_squares_feature.position == 7:
        p = [506,534]
        screen.blit(ms_letter, p)

    if s.game.corners.status == True:
        p = [27,378]
        screen.blit(corners, p)

    if s.game.ballyhole.status == True:
        p = [34,448]
        screen.blit(ballyhole, p)

    if s.game.extra_ball.position >= 1:
        p = [134,1015]
        screen.blit(eb_number, p)
    if s.game.extra_ball.position >= 2:
        p = [182,1015]
        screen.blit(eb, p)
    if s.game.extra_ball.position >= 3:
        p = [252,1015]
        screen.blit(eb, p)
    if s.game.extra_ball.position >= 4:
        p = [323,1015]
        screen.blit(eb_number, p)
    if s.game.extra_ball.position >= 5:
        p = [373,1015]
        screen.blit(eb, p)
    if s.game.extra_ball.position >= 6:
        p = [440,1015]
        screen.blit(eb, p)
    if s.game.extra_ball.position >= 7:
        p = [513,1015]
        screen.blit(eb_number, p)
    if s.game.extra_ball.position >= 8:
        p = [562,1015]
        screen.blit(eb, p)
    if s.game.extra_ball.position == 9:
        p = [630,1015]
        screen.blit(eb, p)

    if s.game.eb_play.status == True:
        p = [19,1013]
        screen.blit(extra_balls, p)

    if s.game.red_odds.position == 1:
        p = [76,705]
        screen.blit(red_odds1, p)
    elif s.game.red_odds.position == 2:
        p = [125,721]
        screen.blit(red_odds2, p)
    elif s.game.red_odds.position == 3:
        p = [210,705]
        screen.blit(red_odds3, p)
    elif s.game.red_odds.position == 4:
        p = [286,721]
        screen.blit(red_odds4, p)
    elif s.game.red_odds.position == 5:
        p = [431,729]
        screen.blit(red_odds5, p)
    elif s.game.red_odds.position == 6:
        p = [501,716]
        screen.blit(red_odds6, p)
    elif s.game.red_odds.position == 7:
        p = [551,711]
        screen.blit(red_odds7, p)
    elif s.game.red_odds.position == 8:
        p = [596,703]
        screen.blit(red_odds8, p)

    if s.game.yellow_odds.position == 1:
        p = [19,827]
        screen.blit(yellow_odds1, p)
    elif s.game.yellow_odds.position == 2:
        p = [120,799]
        screen.blit(yellow_odds2, p)
    elif s.game.yellow_odds.position == 3:
        p = [218,802]
        screen.blit(yellow_odds3, p)
    elif s.game.yellow_odds.position == 4:
        p = [323,794]
        screen.blit(yellow_odds4, p)
    elif s.game.yellow_odds.position == 5:
        p = [440,807]
        screen.blit(yellow_odds5, p)
    elif s.game.yellow_odds.position == 6:
        p = [491,800]
        screen.blit(yellow_odds6, p)
    elif s.game.yellow_odds.position == 7:
        p = [537,783]
        screen.blit(yellow_odds7, p)
    elif s.game.yellow_odds.position == 8:
        p = [639,804]
        screen.blit(yellow_odds8, p)

    if s.game.green_odds.position == 1:
        p = [31,889]
        screen.blit(green_odds1, p)
    elif s.game.green_odds.position == 2:
        p = [113,886]
        screen.blit(green_odds2, p)
    elif s.game.green_odds.position == 3:
        p = [240,919]
        screen.blit(green_odds3, p)
    elif s.game.green_odds.position == 4:
        p = [295,931]
        screen.blit(green_odds4, p)
    elif s.game.green_odds.position == 5:
        p = [401,915]
        screen.blit(green_odds5, p)
    elif s.game.green_odds.position == 6:
        p = [471,890]
        screen.blit(green_odds6, p)
    elif s.game.green_odds.position == 7:
        p = [601,863]
        screen.blit(green_odds7, p)
    elif s.game.green_odds.position == 8:
        p = [653,867]
        screen.blit(green_odds8, p)

    if s.game.select_a_score.status == True:
        p = [560,313]
        screen.blit(select_a_score, p)
        if s.game.swapped == True:
            p = [635,423]
            screen.blit(score_selected, p)
        else:
            p = [574,423]
            screen.blit(score_selected, p)

    if s.game.tilt.status == True:
        tilt_position = [59,235]
        screen.blit(tilt, tilt_position)

    pygame.display.update()

def blink(args):
    dirty_rects = []
    s = args[0]
    b = args[1]
    sl = args[2]

    if b == 0:
        if sl == 1:
            p = [559,583]
            dirty_rects.append(screen.blit(select_now, p))
        pygame.display.update(dirty_rects)
    else:
        dirty_rects.append(screen.blit(bg_gi, (559,583), pygame.Rect(559,583,154,43)))
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
        p = [217,332]
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
        dirty_rects.append(screen.blit(topleft, (236  - num - 20, 335)))
        dirty_rects.append(screen.blit(topright, (276, 340 - num - 10)))
        dirty_rects.append(screen.blit(bottomright, (269  + num + 15, 392)))
        dirty_rects.append(screen.blit(bottomleft, (223, 393 + num + 5)))

    if (s.game.anti_cheat.status == True):
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],130,130)))
    else:
        dirty_rects.append(screen.blit(bg_off, p, pygame.Rect(p[0],p[1],130,130)))
    
    if 2 in s.holes:
        number_position = [219,444]
        dirty_rects.append(screen.blit(bg_gi, number_position, pygame.Rect(number_position[0],number_position[1],50,52)))
        dirty_rects.append(screen.blit(number, number_position))
    if 16 in s.holes:
        number_position = [338,445]
        dirty_rects.append(screen.blit(bg_gi, number_position, pygame.Rect(number_position[0],number_position[1],50,52)))
        dirty_rects.append(screen.blit(number, number_position))
    if 18 in s.holes:
        number_position = [279,448]
        dirty_rects.append(screen.blit(bg_gi, number_position, pygame.Rect(number_position[0],number_position[1],50,52)))
        dirty_rects.append(screen.blit(number, number_position))
    if 24 in s.holes:
        number_position = [336,390]
        dirty_rects.append(screen.blit(bg_gi, number_position, pygame.Rect(number_position[0],number_position[1],50,52)))
        dirty_rects.append(screen.blit(number, number_position))
    if 25 in s.holes:
        number_position = [337,332]
        dirty_rects.append(screen.blit(bg_gi, number_position, pygame.Rect(number_position[0],number_position[1],50,52)))
        dirty_rects.append(screen.blit(number, number_position))

    if s.game.magic_squares_feature.position >= 5:
        p = [166,359]
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],49,49)))
        dirty_rects.append(screen.blit(ms_letter, p))
    pygame.display.update(dirty_rects)

def squareb_animation(args):
    dirty_rects = []
    s = args[0]
    num = args[1]
    square = args[2]
    
    if square == 2:
        p = [216,505]
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
        dirty_rects.append(screen.blit(topleft, (235  - num - 20, 511)))
        dirty_rects.append(screen.blit(topright, (273, 513 - num - 9)))
        dirty_rects.append(screen.blit(bottomright, (269  + num + 15, 561)))
        dirty_rects.append(screen.blit(bottomleft, (223, 565 + num + 8)))
    
    if (s.game.anti_cheat.status == True):
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],130,130)))
    else:
        dirty_rects.append(screen.blit(bg_off, p, pygame.Rect(p[0],p[1],130,130)))
    
    if 2 in s.holes:
        number_position = [219,444]
        dirty_rects.append(screen.blit(bg_gi, number_position, pygame.Rect(number_position[0],number_position[1],50,52)))
        dirty_rects.append(screen.blit(number, number_position))
    if 5 in s.holes:
        number_position = [339,560]
        dirty_rects.append(screen.blit(bg_gi, number_position, pygame.Rect(number_position[0],number_position[1],50,52)))
        dirty_rects.append(screen.blit(number, number_position))
    if 13 in s.holes:
        number_position = [336,502]
        dirty_rects.append(screen.blit(bg_gi, number_position, pygame.Rect(number_position[0],number_position[1],50,52)))
        dirty_rects.append(screen.blit(number, number_position))
    if 18 in s.holes:
        number_position = [279,448]
        dirty_rects.append(screen.blit(bg_gi, number_position, pygame.Rect(number_position[0],number_position[1],50,52)))
        dirty_rects.append(screen.blit(number, number_position))

    if s.game.magic_squares_feature.position >= 5:
        p = [173,644]
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],146,43)))
        dirty_rects.append(screen.blit(ms_abc, p))
        p = [166,533]
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],49,49)))
        dirty_rects.append(screen.blit(ms_letter, p))

    pygame.display.update(dirty_rects)

def squarec_animation(args):
    dirty_rects = []
    s = args[0]
    num = args[1]
    square = args[2]
    
    if square == 3:
        p = [394,332]
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
        dirty_rects.append(screen.blit(topleft, (403  - num - 10, 337)))
        dirty_rects.append(screen.blit(topright, (448, 341 - num - 5)))
        dirty_rects.append(screen.blit(bottomright, (449  + num + 15, 390)))
        dirty_rects.append(screen.blit(bottomleft, (398, 394 + num + 6)))
    
    if (s.game.anti_cheat.status == True):
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],130,130)))
    else:
        dirty_rects.append(screen.blit(bg_off, p, pygame.Rect(p[0],p[1],130,130)))
    
    if 11 in s.holes:
        number_position = [455,446]
        dirty_rects.append(screen.blit(bg_gi, number_position, pygame.Rect(number_position[0],number_position[1],50,52)))
        dirty_rects.append(screen.blit(number, number_position))
    if 12 in s.holes:
        number_position = [395,446]
        dirty_rects.append(screen.blit(bg_gi, number_position, pygame.Rect(number_position[0],number_position[1],50,52)))
        dirty_rects.append(screen.blit(number, number_position))
    if 24 in s.holes:
        number_position = [336,390]
        dirty_rects.append(screen.blit(bg_gi, number_position, pygame.Rect(number_position[0],number_position[1],50,52)))
        dirty_rects.append(screen.blit(number, number_position))
    if 25 in s.holes:
        number_position = [337,332]
        dirty_rects.append(screen.blit(bg_gi, number_position, pygame.Rect(number_position[0],number_position[1],50,52)))
        dirty_rects.append(screen.blit(number, number_position))

    if s.game.magic_squares_feature.position >= 5:
        p = [508,360]
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],49,49)))
        dirty_rects.append(screen.blit(ms_letter, p))

    pygame.display.update(dirty_rects)

def squared_animation(args):
    dirty_rects = []
    s = args[0]
    num = args[1]
    square = args[2]
    
    p = [394,505]
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
        dirty_rects.append(screen.blit(topleft, (400 - num - 6, 510)))
        dirty_rects.append(screen.blit(topright, (446, 518 - num - 13)))
        dirty_rects.append(screen.blit(bottomright, (429  + num + 29, 560)))
        dirty_rects.append(screen.blit(bottomleft, (395, 559 + num + 12)))
    
    if (s.game.anti_cheat.status == True):
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],130,130)))
    else:
        dirty_rects.append(screen.blit(bg_off, p, pygame.Rect(p[0],p[1],130,130)))
    
    if 5 in s.holes:
        number_position = [339,560]
        dirty_rects.append(screen.blit(bg_gi, number_position, pygame.Rect(number_position[0],number_position[1],50,52)))
        dirty_rects.append(screen.blit(number, number_position))
    if 11 in s.holes:
        number_position = [455,446]
        dirty_rects.append(screen.blit(bg_gi, number_position, pygame.Rect(number_position[0],number_position[1],50,52)))
        dirty_rects.append(screen.blit(number, number_position))
    if 12 in s.holes:
        number_position = [395,446]
        dirty_rects.append(screen.blit(bg_gi, number_position, pygame.Rect(number_position[0],number_position[1],50,52)))
        dirty_rects.append(screen.blit(number, number_position))
    if 13 in s.holes:
        number_position = [336,502]
        dirty_rects.append(screen.blit(bg_gi, number_position, pygame.Rect(number_position[0],number_position[1],50,52)))
        dirty_rects.append(screen.blit(number, number_position))

    if s.game.magic_squares_feature.position >= 5:
        p = [506,534]
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],49,49)))
        dirty_rects.append(screen.blit(ms_letter, p))
    if s.game.magic_squares_feature.position >= 6:
        if 2 in s.holes:
            p = [330,649]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],29,28)))
            dirty_rects.append(screen.blit(ms_number, p))
        else:
            p = [379,649]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],29,28)))
            dirty_rects.append(screen.blit(ms_number, p))
    if s.game.magic_squares_feature.position == 7:
        p = [418,645]
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],94,44)))
        dirty_rects.append(screen.blit(ms_d, p))

    pygame.display.update(dirty_rects)


def eb_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]

    if s.game.extra_ball.position < 1:
        dirty_rects.append(screen.blit(bg_gi, (134,1015), pygame.Rect(134,1015,48,34)))
    if s.game.extra_ball.position < 2:
        dirty_rects.append(screen.blit(bg_gi, (182,1015), pygame.Rect(182,1015,67,33)))
    if s.game.extra_ball.position < 3:
        dirty_rects.append(screen.blit(bg_gi, (252,1015), pygame.Rect(252,1015,67,33)))
    if s.game.extra_ball.position < 4:
        dirty_rects.append(screen.blit(bg_gi, (323,1015), pygame.Rect(323,1015,48,34)))
    if s.game.extra_ball.position < 5:
        dirty_rects.append(screen.blit(bg_gi, (373,1015), pygame.Rect(373,1015,67,33)))
    if s.game.extra_ball.position < 6:
        dirty_rects.append(screen.blit(bg_gi, (440,1015), pygame.Rect(440,1015,67,33)))
    if s.game.extra_ball.position < 7:
        dirty_rects.append(screen.blit(bg_gi, (513,1015), pygame.Rect(513,1015,48,34)))
    if s.game.extra_ball.position < 8:
        dirty_rects.append(screen.blit(bg_gi, (562,1015), pygame.Rect(562,1015,67,33)))
    if s.game.extra_ball.position < 9:
        dirty_rects.append(screen.blit(bg_gi, (630,1015), pygame.Rect(630,1015,67,33)))
    pygame.display.update(dirty_rects)

    if num in [0,25,14,49]:
        if s.game.extra_ball.position < 1:
            p = [134,1015]
            dirty_rects.append(screen.blit(eb_number, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [39,1,26,15]:
        if s.game.extra_ball.position < 2:
            p = [182,1015]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [3,4,17,28,29,40]:
        if s.game.extra_ball.position < 3:
            p = [252,1015]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [5,18,30,43]:
        if s.game.extra_ball.position < 4:
            p = [323,1015]
            dirty_rects.append(screen.blit(eb_number, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [7,8,19,32,33,44]:
        if s.game.extra_ball.position < 5:
            p = [373,1015]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [9,10,20,34,35,45]:
        if s.game.extra_ball.position < 6:
            p = [440,1015]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [11,21,36,46]:
        if s.game.extra_ball.position < 7:
            p = [513,1015]
            dirty_rects.append(screen.blit(eb_number, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [12,22,37,47]:
        if s.game.extra_ball.position < 8:
            p = [562,1015]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [2,6,13,16,23,27,31,38,41,48]:
        if s.game.extra_ball.position < 9:
            p = [630,1015]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return

def clear_odds(s, num):
    global screen

    dirty_rects = []

    if s.game.yellow_odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (19,827), pygame.Rect(19,827,31,53)))
    if s.game.yellow_odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (120,799), pygame.Rect(120,799,31,53)))
    if s.game.yellow_odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (218,802), pygame.Rect(218,802,31,53)))
    if s.game.yellow_odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (323,794), pygame.Rect(323,794,31,53)))
    if s.game.yellow_odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (440,807), pygame.Rect(440,807,40,52)))
    if s.game.yellow_odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (491,800), pygame.Rect(491,800,40,52)))
    if s.game.yellow_odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (537,783), pygame.Rect(537,783,40,52)))
    if s.game.yellow_odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (639,804), pygame.Rect(639,804,43,54)))

    if s.game.red_odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (76,705), pygame.Rect(76,705,30,55)))
    if s.game.red_odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (125,721), pygame.Rect(125,721,30,55)))
    if s.game.red_odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (210,705), pygame.Rect(210,705,31,55)))
    if s.game.red_odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (286,721), pygame.Rect(286,721,31,55)))
    if s.game.red_odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (431,729), pygame.Rect(431,729,37,55)))
    if s.game.red_odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (501,716), pygame.Rect(501,716,37,55)))
    if s.game.red_odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (551,711), pygame.Rect(551,711,37,55)))
    if s.game.red_odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (596,703), pygame.Rect(596,703,45,58)))


    if s.game.green_odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (31,889), pygame.Rect(31,889,28,53)))
    if s.game.green_odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (113,886), pygame.Rect(113,886,28,53)))
    if s.game.green_odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (240,919), pygame.Rect(240,919,30,54)))
    if s.game.green_odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (295,931), pygame.Rect(295,931,35,53)))
    if s.game.green_odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (401,915), pygame.Rect(401,915,44,56)))
    if s.game.green_odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (471,890), pygame.Rect(471,890,38,57)))
    if s.game.green_odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (601,863), pygame.Rect(601,863,38,57)))
    if s.game.green_odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (653,867), pygame.Rect(653,867,38,57)))


    pygame.display.update(dirty_rects)

def draw_odds_animation(s, num):
    global screen
    dirty_rects = []

    if num in [11,36]:
        if s.game.yellow_odds.position != 1:
            p = [19,827]
            dirty_rects.append(screen.blit(yellow_odds1, p))
            pygame.display.update(dirty_rects)
            return
    if num in [4,29]:
        if s.game.yellow_odds.position != 2:
            p = [120,799]
            dirty_rects.append(screen.blit(yellow_odds2, p))
            pygame.display.update(dirty_rects)
            return
    if num in [7,32]:
        if s.game.yellow_odds.position != 3:
            p = [218,802]
            dirty_rects.append(screen.blit(yellow_odds3, p))
            pygame.display.update(dirty_rects)
            return
    if num in [13,38]:
        if s.game.yellow_odds.position != 4:
            p = [323,794]
            dirty_rects.append(screen.blit(yellow_odds4, p))
            pygame.display.update(dirty_rects)
            return
    if num in [23,48]:
        if s.game.yellow_odds.position != 5:
            p = [440,807]
            dirty_rects.append(screen.blit(yellow_odds5, p))
            pygame.display.update(dirty_rects)
            return
    if num in [17,42]:
        if s.game.yellow_odds.position != 6:
            p = [491,800]
            dirty_rects.append(screen.blit(yellow_odds6, p))
            pygame.display.update(dirty_rects)
            return
    if num in [19,44]:
        if s.game.yellow_odds.position != 7:
            p = [537,783]
            dirty_rects.append(screen.blit(yellow_odds7, p))
            pygame.display.update(dirty_rects)
            return
    if num in [5,30]:
        if s.game.yellow_odds.position != 8:
            p = [639,804]
            dirty_rects.append(screen.blit(yellow_odds8, p))
            pygame.display.update(dirty_rects)
            return

    if num in [2,27]:
        if s.game.red_odds.position != 1:
            p = [76,705]
            dirty_rects.append(screen.blit(red_odds1, p))
            pygame.display.update(dirty_rects)
            return
    if num in [15,40]:
        if s.game.red_odds.position != 2:
            p = [125,721]
            dirty_rects.append(screen.blit(red_odds2, p))
            pygame.display.update(dirty_rects)
            return
    if num in [0,25]:
        if s.game.red_odds.position != 3:
            p = [210,705]
            dirty_rects.append(screen.blit(red_odds3, p))
            pygame.display.update(dirty_rects)
            return
    if num in [9,34]:
        if s.game.red_odds.position != 4:
            p = [286,721]
            dirty_rects.append(screen.blit(red_odds4, p))
            pygame.display.update(dirty_rects)
            return
    if num in [20,45]:
        if s.game.red_odds.position != 5:
            p = [431,729]
            dirty_rects.append(screen.blit(red_odds5, p))
            pygame.display.update(dirty_rects)
            return
    if num in [12,37]:
        if s.game.red_odds.position != 6:
            p = [501,716]
            dirty_rects.append(screen.blit(red_odds6, p))
            pygame.display.update(dirty_rects)
            return
    if num in [1,26]:
        if s.game.red_odds.position != 7:
            p = [551,711]
            dirty_rects.append(screen.blit(red_odds7, p))
            pygame.display.update(dirty_rects)
            return
    if num in [6,31]:
        if s.game.red_odds.position != 8:
            p = [596,703]
            dirty_rects.append(screen.blit(red_odds8, p))
            pygame.display.update(dirty_rects)
            return

    if num in [16,41]:
        if s.game.green_odds.position != 1:
            p = [31,889]
            dirty_rects.append(screen.blit(green_odds1, p))
            pygame.display.update(dirty_rects)
            return
    if num in [18,43]:
        if s.game.green_odds.position != 2:
            p = [113,886]
            dirty_rects.append(screen.blit(green_odds2, p))
            pygame.display.update(dirty_rects)
            return
    if num in [14,39]:
        if s.game.green_odds.position != 3:
            p = [240,919]
            dirty_rects.append(screen.blit(green_odds3, p))
            pygame.display.update(dirty_rects)
            return
    if num in [3,28]:
        if s.game.green_odds.position != 4:
            p = [295,931]
            dirty_rects.append(screen.blit(green_odds4, p))
            pygame.display.update(dirty_rects)
            return
    if num in [24,49]:
        if s.game.green_odds.position != 5:
            p = [401,915]
            dirty_rects.append(screen.blit(green_odds5, p))
            pygame.display.update(dirty_rects)
            return
    if num in [8,33]:
        if s.game.green_odds.position != 6:
            p = [471,890]
            dirty_rects.append(screen.blit(green_odds6, p))
            pygame.display.update(dirty_rects)
            return
    if num in [21,46]:
        if s.game.green_odds.position != 7:
            p = [601,863]
            dirty_rects.append(screen.blit(green_odds7, p))
            pygame.display.update(dirty_rects)
            return
    if num in [11,36]:
        if s.game.green_odds.position != 8:
            p = [653,867]
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

        dirty_rects.append(screen.blit(bg_gi, (173,644), pygame.Rect(173,644,146,43)))
        dirty_rects.append(screen.blit(bg_gi, (166,359), pygame.Rect(166,359,49,49)))
        dirty_rects.append(screen.blit(bg_gi, (166,533), pygame.Rect(166,533,49,49)))
        dirty_rects.append(screen.blit(bg_gi, (508,360), pygame.Rect(508,360,49,49)))
    if s.game.magic_squares_feature.position < 6:
        if 2 not in s.holes:
            dirty_rects.append(screen.blit(bg_gi, (330,649), pygame.Rect(330,649,29,28)))
        if 18 not in s.holes:
            dirty_rects.append(screen.blit(bg_gi, (379,649), pygame.Rect(379,649,29,28)))
    if s.game.magic_squares_feature.position < 7:
        dirty_rects.append(screen.blit(bg_gi, (418,645), pygame.Rect(418,645,94,44)))
        dirty_rects.append(screen.blit(bg_gi, (506,534), pygame.Rect(506,534,49,49)))
    if s.game.corners.status == False:
        dirty_rects.append(screen.blit(bg_gi, (27,378), pygame.Rect(27,378,117,64)))
    if s.game.ballyhole.status == False:
        dirty_rects.append(screen.blit(bg_gi, (34,448), pygame.Rect(34,448,101,63)))
    if s.game.select_a_score.status == False:
        dirty_rects.append(screen.blit(bg_gi, (560,313), pygame.Rect(560,313,150,58)))

    pygame.display.update(dirty_rects)


def draw_feature_animation(s, num):
    global screen
    dirty_rects = []


    if num in [3,28,10,35,17,42,23,48]:
        if s.game.magic_squares_feature.position < 5:
            p = [173,644]
            dirty_rects.append(screen.blit(ms_abc, p))
            p = [166,359]
            dirty_rects.append(screen.blit(ms_letter, p))
            p = [166,533]
            dirty_rects.append(screen.blit(ms_letter, p))
            p = [508,360]
            dirty_rects.append(screen.blit(ms_letter, p))
            pygame.display.update(dirty_rects)
            return
    if num in [5,12,19,30,37,44]:
        if s.game.magic_squares_feature.position < 6:
            p = [330,649]
            dirty_rects.append(screen.blit(ms_number, p))
            pygame.display.update(dirty_rects)
            return
    if num in [8,15,22,33,40,47]:
        if s.game.magic_squares_feature.position < 6:
            p = [379,649]
            dirty_rects.append(screen.blit(ms_number, p))
            pygame.display.update(dirty_rects)
            return
    if num in [7,14,21,25,50,46,39,32]:
        if s.game.magic_squares_feature.position < 7:
            p = [418,645]
            dirty_rects.append(screen.blit(ms_d, p))
            p = [506,534]
            dirty_rects.append(screen.blit(ms_letter, p))
            pygame.display.update(dirty_rects)
            return
    if num in [2,9,16,27,34,41]:
        if s.game.corners.status == False:
            p = [27,378]
            dirty_rects.append(screen.blit(corners, p))
            pygame.display.update(dirty_rects)
            return
    if num in [6,13,20,24,31,38,45,49]:
        if s.game.ballyhole.status == False:
            p = [34,448]
            dirty_rects.append(screen.blit(ballyhole, p))
            pygame.display.update(dirty_rects)
            return
    if num in [0,29,35,41,25,4,10,16]:
        if s.game.select_a_score.status == False:
            p = [560,313]
            dirty_rects.append(screen.blit(select_a_score, p))
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


