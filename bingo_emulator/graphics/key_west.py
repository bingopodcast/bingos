
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
        backglass = pygame.image.load('key_west/assets/key_west_menu.png')
    else:
        if (s.game.anti_cheat.status == True):
            backglass = pygame.image.load('key_west/assets/key_west_gi.png')
        else:
            backglass = pygame.image.load('key_west/assets/key_west_off.png')
    backglass = pygame.transform.scale(backglass, (720, 1280))
    
    screen.blit(backglass, backglass_position)


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
                p = [559,583]
                screen.blit(select_now, p)
        elif s.game.after_fifth.status == True:
            p = [9,583]
            screen.blit(time, p)
            if s.game.ball_count.position == 4:
                p = [559,583]
                screen.blit(select_now, p)
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
        p = [21,1015]
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

    pygame.display.flip()
    pygame.display.update()

def eb_animation(num):
    global screen

    if num == 9:
        p = [134,1015]
        screen.blit(eb_number, p)
        pygame.display.update()
    if num == 8:
        p = [182,1015]
        screen.blit(eb, p)
        pygame.display.update()
    if num == 7:
        p = [252,1015]
        screen.blit(eb, p)
        pygame.display.update()
    if num == 6:
        p = [323,1015]
        screen.blit(eb_number, p)
        pygame.display.update()
    if num == 5:
        p = [373,1015]
        screen.blit(eb, p)
        pygame.display.update()
    if num == 4:
        p = [440,1015]
        screen.blit(eb, p)
        pygame.display.update()
    if num == 3:
        p = [513,1015]
        screen.blit(eb_number, p)
        pygame.display.update()
    if num == 2:
        p = [562,1015]
        screen.blit(eb, p)
        pygame.display.update()
    if num == 1:
        p = [630,1015]
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

