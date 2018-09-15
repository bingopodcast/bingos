
import pygame

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

meter = pygame.image.load('graphics/assets/register_cover.png').convert()
number = pygame.image.load('showtime/assets/number.png').convert_alpha()
feature = pygame.image.load('showtime/assets/feature.png').convert_alpha()
ms_letter = pygame.image.load('showtime/assets/ms_letter.png').convert_alpha()
ms_arrow = pygame.image.load('showtime/assets/ms_arrow.png').convert_alpha()
select_now = pygame.image.load('showtime/assets/select_now.png').convert_alpha()
corners = pygame.image.load('showtime/assets/feature.png').convert_alpha()
ballyhole = pygame.image.load('showtime/assets/feature.png').convert_alpha()
red_odds1 = pygame.image.load('showtime/assets/red_odds1.png').convert_alpha()
red_odds2 = pygame.image.load('showtime/assets/red_odds2.png').convert_alpha()
red_odds3 = pygame.image.load('showtime/assets/red_odds3.png').convert_alpha()
red_odds4 = pygame.image.load('showtime/assets/red_odds4.png').convert_alpha()
red_odds5 = pygame.image.load('showtime/assets/red_odds5.png').convert_alpha()
red_odds6 = pygame.image.load('showtime/assets/red_odds6.png').convert_alpha()
red_odds7 = pygame.image.load('showtime/assets/red_odds7.png').convert_alpha()
red_odds8 = pygame.image.load('showtime/assets/red_odds8.png').convert_alpha()
yellow_odds1 = pygame.image.load('showtime/assets/yellow_odds1.png').convert_alpha()
yellow_odds2 = pygame.image.load('showtime/assets/yellow_odds2.png').convert_alpha()
yellow_odds3 = pygame.image.load('showtime/assets/yellow_odds3.png').convert_alpha()
yellow_odds4 = pygame.image.load('showtime/assets/yellow_odds4.png').convert_alpha()
yellow_odds5 = pygame.image.load('showtime/assets/yellow_odds5.png').convert_alpha()
yellow_odds6 = pygame.image.load('showtime/assets/yellow_odds6.png').convert_alpha()
yellow_odds7 = pygame.image.load('showtime/assets/yellow_odds7.png').convert_alpha()
yellow_odds8 = pygame.image.load('showtime/assets/yellow_odds8.png').convert_alpha()
green_odds1 = pygame.image.load('showtime/assets/green_odds1.png').convert_alpha()
green_odds2 = pygame.image.load('showtime/assets/green_odds2.png').convert_alpha()
green_odds3 = pygame.image.load('showtime/assets/green_odds3.png').convert_alpha()
green_odds4 = pygame.image.load('showtime/assets/green_odds4.png').convert_alpha()
green_odds5 = pygame.image.load('showtime/assets/green_odds5.png').convert_alpha()
green_odds6 = pygame.image.load('showtime/assets/green_odds6.png').convert_alpha()
green_odds7 = pygame.image.load('showtime/assets/green_odds7.png').convert_alpha()
green_odds8 = pygame.image.load('showtime/assets/green_odds8.png').convert_alpha()
extra_balls = pygame.image.load('showtime/assets/extra_balls.png').convert_alpha()
eb = pygame.image.load('showtime/assets/eb.png').convert_alpha()
eb_number = pygame.image.load('showtime/assets/eb_number.png').convert_alpha()
tilt = pygame.image.load('showtime/assets/tilt.png').convert_alpha()
time = pygame.image.load('showtime/assets/time.png').convert_alpha()
s_arrow = pygame.image.load('showtime/assets/sf_arrow.png').convert_alpha()
a0 = pygame.image.load('showtime/assets/a0.png').convert_alpha()
a1 = pygame.image.load('showtime/assets/a1.png').convert_alpha()
a2 = pygame.image.load('showtime/assets/a2.png').convert_alpha()
a3 = pygame.image.load('showtime/assets/a3.png').convert_alpha()
b0 = pygame.image.load('showtime/assets/b0.png').convert_alpha()
b1 = pygame.image.load('showtime/assets/b1.png').convert_alpha()
b2 = pygame.image.load('showtime/assets/b2.png').convert_alpha()
b3 = pygame.image.load('showtime/assets/b3.png').convert_alpha()
c0 = pygame.image.load('showtime/assets/c0.png').convert_alpha()
c1 = pygame.image.load('showtime/assets/c1.png').convert_alpha()
c2 = pygame.image.load('showtime/assets/c2.png').convert_alpha()
c3 = pygame.image.load('showtime/assets/c3.png').convert_alpha()
d0 = pygame.image.load('showtime/assets/d0.png').convert_alpha()
d1 = pygame.image.load('showtime/assets/d1.png').convert_alpha()
d2 = pygame.image.load('showtime/assets/d2.png').convert_alpha()
d3 = pygame.image.load('showtime/assets/d3.png').convert_alpha()
e0 = pygame.image.load('showtime/assets/e0.png').convert_alpha()
e1 = pygame.image.load('showtime/assets/e1.png').convert_alpha()
e2 = pygame.image.load('showtime/assets/e2.png').convert_alpha()
e3 = pygame.image.load('showtime/assets/e3.png').convert_alpha()
rollover = pygame.image.load('showtime/assets/rollover.png').convert_alpha()
bg_menu = pygame.image.load('showtime/assets/showtime_menu.png')
bg_gi = pygame.image.load('showtime/assets/showtime_gi.png')
bg_off = pygame.image.load('showtime/assets/showtime_off.png')
a_1 = pygame.image.load('showtime/assets/a-1.png').convert_alpha()
a_2 = pygame.image.load('showtime/assets/a-2.png').convert_alpha()
a_3 = pygame.image.load('showtime/assets/a-3.png').convert_alpha()
a_4 = pygame.image.load('showtime/assets/a-4.png').convert_alpha()
b_1 = pygame.image.load('showtime/assets/b-1.png').convert_alpha()
b_2 = pygame.image.load('showtime/assets/b-2.png').convert_alpha()
b_3 = pygame.image.load('showtime/assets/b-3.png').convert_alpha()
b_4 = pygame.image.load('showtime/assets/b-4.png').convert_alpha()
c_1 = pygame.image.load('showtime/assets/c-1.png').convert_alpha()
c_2 = pygame.image.load('showtime/assets/c-2.png').convert_alpha()
c_3 = pygame.image.load('showtime/assets/c-3.png').convert_alpha()
c_4 = pygame.image.load('showtime/assets/c-4.png').convert_alpha()
d_1 = pygame.image.load('showtime/assets/d-1.png').convert_alpha()
d_2 = pygame.image.load('showtime/assets/d-2.png').convert_alpha()
d_3 = pygame.image.load('showtime/assets/d-3.png').convert_alpha()
d_4 = pygame.image.load('showtime/assets/d-4.png').convert_alpha()
e_1 = pygame.image.load('showtime/assets/e-1.png').convert_alpha()
e_2 = pygame.image.load('showtime/assets/e-2.png').convert_alpha()
e_3 = pygame.image.load('showtime/assets/e-3.png').convert_alpha()
e_4 = pygame.image.load('showtime/assets/e-4.png').convert_alpha()


class scorereel():
    """ Score Reels are used to count replays """
    def __init__(self, pos, image):
        self.position = pos
        self.default_y = self.position[1]
        self.image = pygame.image.load(image).convert()

reel1 = scorereel([101,302], "graphics/assets/white_reel.png")
reel10 = scorereel([82,302], "graphics/assets/white_reel.png")
reel100 = scorereel([63,302], "graphics/assets/white_reel.png")

def display(s, replays=0, menu=False):
    
    meter.set_colorkey((255,0,252))
    meter_position = [54,302]

    screen.blit(reel1.image, reel1.position)
    screen.blit(reel10.image, reel10.position)
    screen.blit(reel100.image, reel100.position)
    screen.blit(meter, meter_position)

    if s.game.square_a.position == 0:
        p = [228,334]
        screen.blit(a0, p)
    if s.game.square_a.position == 1:
        p = [228,334]
        screen.blit(a1, p)
    if s.game.square_a.position == 2:
        p = [228,334]
        screen.blit(a2, p)
    if s.game.square_a.position == 3:
        p = [228,334]
        screen.blit(a3, p)
    if s.game.square_b.position == 0:
        p = [228,440]
        screen.blit(b0, p)
    if s.game.square_b.position == 1:
        p = [228,440]
        screen.blit(b1, p)
    if s.game.square_b.position == 2:
        p = [228,440]
        screen.blit(b2, p)
    if s.game.square_b.position == 3:
        p = [228,440]
        screen.blit(b3, p)
    if s.game.square_c.position == 0:
        p = [339,334]
        screen.blit(c0, p)
    if s.game.square_c.position == 1:
        p = [339,334]
        screen.blit(c1, p)
    if s.game.square_c.position == 2:
        p = [339,334]
        screen.blit(c2, p)
    if s.game.square_c.position == 3:
        p = [339,334]
        screen.blit(c3, p)
    if s.game.square_d.position == 0:
        p = [338,440]
        screen.blit(d0, p)
    if s.game.square_d.position == 1:
        p = [338,440]
        screen.blit(d1, p)
    if s.game.square_d.position == 2:
        p = [338,440]
        screen.blit(d2, p)
    if s.game.square_d.position == 3:
        p = [338,440]
        screen.blit(d3, p)
    if s.game.square_e.position == 0:
        p = [230,547]
        screen.blit(e0, p)
    if s.game.square_e.position == 1:
        p = [230,547]
        screen.blit(e1, p)
    if s.game.square_e.position == 2:
        p = [230,547]
        screen.blit(e2, p)
    if s.game.square_e.position == 3:
        p = [230,547]
        screen.blit(e3, p)


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
                    p = [286,338]
                    screen.blit(number, p)
                elif s.game.square_a.position == 1:
                    p = [285,390]
                    screen.blit(number, p)
                elif s.game.square_a.position == 2:
                    p = [231,391]
                    screen.blit(number, p)
                else:
                    p = [231,338]
                    screen.blit(number, p)
            if 2 in s.holes:
                if s.game.square_c.position == 0:
                    p = [340,338]
                    screen.blit(number, p)
                elif s.game.square_c.position == 1:
                    p = [394,338]
                    screen.blit(number, p)
                elif s.game.square_c.position == 2:
                    p = [393,390]
                    screen.blit(number, p)
                else:
                    p = [340,390]
                    screen.blit(number, p)
            if 3 in s.holes:
                if s.game.square_e.position == 0:
                    p = [396,553]
                    screen.blit(number, p)
                elif s.game.square_e.position == 1:
                    p = [232,552]
                    screen.blit(number, p)
                elif s.game.square_e.position == 2:
                    p = [286,553]
                    screen.blit(number, p)
                else:
                    p = [340,554]
                    screen.blit(number, p)
            if 4 in s.holes:
                if s.game.square_a.position == 0:
                    p = [231,390]
                    screen.blit(number, p)
                elif s.game.square_a.position == 1:
                    p = [232,339]
                    screen.blit(number, p)
                elif s.game.square_a.position == 2:
                    p = [285,338]
                    screen.blit(number, p)
                else:
                    p = [285,390]
                    screen.blit(number, p)
            if 5 in s.holes:
                if s.game.square_d.position == 0:
                    p = [341,499]
                    screen.blit(number, p)
                elif s.game.square_d.position == 1:
                    p = [340,445]
                    screen.blit(number, p)
                elif s.game.square_d.position == 2:
                    p = [394,444]
                    screen.blit(number, p)
                else:
                    p = [396,498]
                    screen.blit(number, p)
            if 6 in s.holes:
                if s.game.square_b.position == 0:
                    p = [231,499]
                    screen.blit(number, p)
                elif s.game.square_b.position == 1:
                    p = [232,444]
                    screen.blit(number, p)
                elif s.game.square_b.position == 2:
                    p = [285,444]
                    screen.blit(number, p)
                else:
                    p = [286,499]
                    screen.blit(number, p)
            if 7 in s.holes:
                if s.game.square_c.position == 0:
                    p = [341,391]
                    screen.blit(number, p)
                elif s.game.square_c.position == 1:
                    p = [340,339]
                    screen.blit(number, p)
                elif s.game.square_c.position == 2:
                    p = [394,338]
                    screen.blit(number, p)
                else:
                    p = [395,391]
                    screen.blit(number, p)
            if 8 in s.holes:
                if s.game.square_e.position == 0:
                    p = [286,552]
                    screen.blit(number, p)
                elif s.game.square_e.position == 1:
                    p = [340,552]
                    screen.blit(number, p)
                elif s.game.square_e.position == 2:
                    p = [396,552]
                    screen.blit(number, p)
                else:
                    p = [231,552]
                    screen.blit(number, p)
            if 9 in s.holes:
                if s.game.square_a.position == 0:
                    p = [232,339]
                    screen.blit(number, p)
                elif s.game.square_a.position == 1:
                    p = [286,338]
                    screen.blit(number, p)
                elif s.game.square_a.position == 2:
                    p = [286,389]
                    screen.blit(number, p)
                else:
                    p = [232,390]
                    screen.blit(number, p)
            if 10 in s.holes:
                p = [452,552]
                screen.blit(number, p)
            if 11 in s.holes:
                if s.game.square_c.position == 0:
                    p = [394,340]
                    screen.blit(number, p)
                elif s.game.square_c.position == 1:
                    p = [394,392]
                    screen.blit(number, p)
                elif s.game.square_c.position == 2:
                    p = [341,390]
                    screen.blit(number, p)
                else:
                    p = [340,338]
                    screen.blit(number, p)
            if 12 in s.holes:
                if s.game.square_e.position == 0:
                    p = [231,552]
                    screen.blit(number, p)
                elif s.game.square_e.position == 1:
                    p = [286,554]
                    screen.blit(number, p)
                elif s.game.square_e.position == 2:
                    p = [342,552]
                    screen.blit(number, p)
                else:
                    p = [396,552]
                    screen.blit(number, p)
            if 13 in s.holes:
                if s.game.square_d.position == 0:
                    p = [395,444]
                    screen.blit(number, p)
                elif s.game.square_d.position == 1:
                    p = [396,498]
                    screen.blit(number, p)
                elif s.game.square_d.position == 2:
                    p = [342,500]
                    screen.blit(number, p)
                else:
                    p = [342,445]
                    screen.blit(number, p)
            if 14 in s.holes:
                if s.game.square_e.position == 0:
                    p = [342,552]
                    screen.blit(number, p)
                elif s.game.square_e.position == 1:
                    p = [396,552]
                    screen.blit(number, p)
                elif s.game.square_e.position == 2:
                    p = [232,552]
                    screen.blit(number, p)
                else:
                    p = [287,553]
                    screen.blit(number, p)
            if 15 in s.holes:
                p = [449,339]
                screen.blit(number, p)
            if 16 in s.holes:
                if s.game.square_d.position == 0:
                    p = [341,446]
                    screen.blit(number, p)
                elif s.game.square_d.position == 1:
                    p = [394,444]
                    screen.blit(number, p)
                elif s.game.square_d.position == 2:
                    p = [396,498]
                    screen.blit(number, p)
                else:
                    p = [342,500]
                    screen.blit(number, p)
            if 17 in s.holes:
                p = [451,444]
                screen.blit(number, p)
            if 18 in s.holes:
                number_position = [450,392]
                screen.blit(number, number_position)
            if 19 in s.holes:
                if s.game.square_a.position == 0:
                    p = [286,390]
                    screen.blit(number, p)
                elif s.game.square_a.position == 1:
                    p = [231,390]
                    screen.blit(number, p)
                elif s.game.square_a.position == 2:
                    p = [232,340]
                    screen.blit(number, p)
                else:
                    p = [286,340]
                    screen.blit(number, p)
            if 20 in s.holes:
                p = [452,499]
                screen.blit(number, p)
            if 21 in s.holes:
                if s.game.square_d.position == 0:
                    p = [396,498]
                    screen.blit(number, p)
                elif s.game.square_d.position == 1:
                    p = [342,500]
                    screen.blit(number, p)
                elif s.game.square_d.position == 2:
                    p = [341,444]
                    screen.blit(number, p)
                else:
                    p = [394,444]
                    screen.blit(number, p)
            if 22 in s.holes:
                if s.game.square_c.position == 0:
                    p = [395,392]
                    screen.blit(number, p)
                elif s.game.square_c.position == 1:
                    p = [341,391]
                    screen.blit(number, p)
                elif s.game.square_c.position == 2:
                    p = [340,339]
                    screen.blit(number, p)
                else:
                    p = [394,339]
                    screen.blit(number, p)
            if 23 in s.holes:
                if s.game.square_b.position == 0:
                    p = [286,499]
                    screen.blit(number, p)
                elif s.game.square_b.position == 1:
                    p = [231,498]
                    screen.blit(number, p)
                elif s.game.square_b.position == 2:
                    p = [232,444]
                    screen.blit(number, p)
                else:
                    p = [286,444]
                    screen.blit(number, p)
            if 24 in s.holes:
                if s.game.square_b.position == 0:
                    p = [286,444]
                    screen.blit(number, p)
                elif s.game.square_b.position == 1:
                    p = [286,499]
                    screen.blit(number, p)
                elif s.game.square_b.position == 2:
                    p = [231,498]
                    screen.blit(number, p)
                else:
                    p = [232,444]
                    screen.blit(number, p)
            if 25 in s.holes:
                if s.game.square_b.position == 0:
                    p = [232,444]
                    screen.blit(number, p)
                elif s.game.square_b.position == 1:
                    p = [286,444]
                    screen.blit(number, p)
                elif s.game.square_b.position == 2:
                    p = [286,499]
                    screen.blit(number, p)
                else:
                    p = [231,498]
                    screen.blit(number, p)


    if s.game.magic_squares_feature.position == 1:
        p = [20,660]
        screen.blit(ms_arrow, p)
    if s.game.magic_squares_feature.position == 2:
        p = [58,660]
        screen.blit(ms_arrow, p)
    if s.game.magic_squares_feature.position == 3:
        p = [98,660]
        screen.blit(ms_arrow, p)
    if s.game.magic_squares_feature.position == 4:
        p = [139,660]
        screen.blit(ms_arrow, p)
    if s.game.magic_squares_feature.position >= 5:
        p = [179,654]
        screen.blit(ms_letter, p)
    if s.game.magic_squares_feature.position >= 6:
        p = [232,654]
        screen.blit(ms_letter, p)
    if s.game.magic_squares_feature.position >= 7:
        p = [285,654]
        screen.blit(ms_letter, p)
    if s.game.magic_squares_feature.position >= 8:
        p = [338,654]
        screen.blit(ms_letter, p)
    if s.game.magic_squares_feature.position == 9:
        p = [389,654]
        screen.blit(ms_letter, p)

    if s.game.magic_squares_feature.position >= 5:
        sf = s.game.selection_feature.position 
        if sf <= 6:
            p = [572,576]
            screen.blit(time, p)
            if sf == 1:
                p = [542,596]
                screen.blit(s_arrow, p)
            if sf == 2:
                p = [543,558]
                screen.blit(s_arrow, p)
            if sf == 3:
                p = [542,520]
                screen.blit(s_arrow, p)
            if sf == 4:
                p = [542,482]
                screen.blit(s_arrow, p)
            if sf == 5:
                p = [542,446]
                screen.blit(s_arrow, p)
            if sf == 6:
                p = [540,408]
                screen.blit(s_arrow, p)
            if s.game.ball_count.position == 3:
                s.cancel_delayed(name="blink")
                blink([s,1,1])
            else:
                s.cancel_delayed(name="blink")
        if sf == 3 or sf == 4:
            p = [41,938]
            screen.blit(rollover, p)
            p = [569,500]
            screen.blit(time, p)
        if sf == 5 or sf == 6:
            p = [635,935]
            screen.blit(rollover, p)
            p = [569,426]
            screen.blit(time, p)
        if sf == 7 or sf == 8:
            if sf == 7:
                p = [540,372]
                screen.blit(s_arrow, p)
            if sf == 8:
                p = [540,336]
                screen.blit(s_arrow, p)
            p = [569,352]
            screen.blit(time, p)
            if s.game.ball_count.position == 4:
                s.cancel_delayed(name="blink")
                blink([s,1,1])
            else:
                s.cancel_delayed(name="blink")
        if sf == 9:
            p = [540,298]
            screen.blit(s_arrow, p)
            p = [569,280]
            screen.blit(time, p)
            if s.game.ball_count.position == 5:
                s.cancel_delayed(name="blink")
                blink([s,1,1])
            else:
                s.cancel_delayed(name="blink")

    if s.game.corners.status == True:
        p = [46,418]
        screen.blit(corners, p)

    if s.game.ballyhole.status == True:
        p = [45,500]
        screen.blit(ballyhole, p)

    if s.game.extra_ball.position >= 1:
        p = [144,1010]
        screen.blit(eb_number, p)
    if s.game.extra_ball.position >= 2:
        p = [193,1010]
        screen.blit(eb, p)
    if s.game.extra_ball.position >= 3:
        p = [260,1010]
        screen.blit(eb, p)
    if s.game.extra_ball.position >= 4:
        p = [330,1010]
        screen.blit(eb_number, p)
    if s.game.extra_ball.position >= 5:
        p = [380,1010]
        screen.blit(eb, p)
    if s.game.extra_ball.position >= 6:
        p = [445,1010]
        screen.blit(eb, p)
    if s.game.extra_ball.position >= 7:
        p = [520,1010]
        screen.blit(eb_number, p)
    if s.game.extra_ball.position >= 8:
        p = [569,1008]
        screen.blit(eb, p)
    if s.game.extra_ball.position == 9:
        p = [634,1007]
        screen.blit(eb, p)

    if s.game.eb_play.status == True:
        p = [34,1006]
        screen.blit(extra_balls, p)

    if s.game.red_odds.position == 1:
        p = [30,762]
        screen.blit(red_odds1, p)
    elif s.game.red_odds.position == 2:
        p = [148,716]
        screen.blit(red_odds2, p)
    elif s.game.red_odds.position == 3:
        p = [202,715]
        screen.blit(red_odds3, p)
    elif s.game.red_odds.position == 4:
        p = [290,706]
        screen.blit(red_odds4, p)
    elif s.game.red_odds.position == 5:
        p = [407,704]
        screen.blit(red_odds5, p)
    elif s.game.red_odds.position == 6:
        p = [504,709]
        screen.blit(red_odds6, p)
    elif s.game.red_odds.position == 7:
        p = [552,715]
        screen.blit(red_odds7, p)
    elif s.game.red_odds.position == 8:
        p = [678,744]
        screen.blit(red_odds8, p)

    if s.game.yellow_odds.position == 1:
        p = [36,824]
        screen.blit(yellow_odds1, p)
    elif s.game.yellow_odds.position == 2:
        p = [150,788]
        screen.blit(yellow_odds2, p)
    elif s.game.yellow_odds.position == 3:
        p = [192,792]
        screen.blit(yellow_odds3, p)
    elif s.game.yellow_odds.position == 4:
        p = [276,779]
        screen.blit(yellow_odds4, p)
    elif s.game.yellow_odds.position == 5:
        p = [412,776]
        screen.blit(yellow_odds5, p)
    elif s.game.yellow_odds.position == 6:
        p = [498,786]
        screen.blit(yellow_odds6, p)
    elif s.game.yellow_odds.position == 7:
        p = [552,786]
        screen.blit(yellow_odds7, p)
    elif s.game.yellow_odds.position == 8:
        p = [662,817]
        screen.blit(yellow_odds8, p)

    if s.game.green_odds.position == 1:
        p = [36,883]
        screen.blit(green_odds1, p)
    elif s.game.green_odds.position == 2:
        p = [151,859]
        screen.blit(green_odds2, p)
    elif s.game.green_odds.position == 3:
        p = [196,862]
        screen.blit(green_odds3, p)
    elif s.game.green_odds.position == 4:
        p = [282,876]
        screen.blit(green_odds4, p)
    elif s.game.green_odds.position == 5:
        p = [413,886]
        screen.blit(green_odds5, p)
    elif s.game.green_odds.position == 6:
        p = [504,852]
        screen.blit(green_odds6, p)
    elif s.game.green_odds.position == 7:
        p = [552,856]
        screen.blit(green_odds7, p)
    elif s.game.green_odds.position == 8:
        p = [677,882]
        screen.blit(green_odds8, p)

    if s.game.tilt.status == True:
        tilt_position = [59,235]
        screen.blit(tilt, tilt_position)

    pygame.display.update()

def blink(args):
    dirty_rects = []
    s = args[0]
    b = args[1]
    sn = args[2]

    if b == 0:
        if sn == 1:
            p = [561,656]
            dirty_rects.append(screen.blit(select_now, p))
        pygame.display.update(dirty_rects)
    else:
        dirty_rects.append(screen.blit(bg_gi, (561,656), pygame.Rect(561,656,146,39)))
        pygame.display.update(dirty_rects)
    b = not b

    args = [s,b,sn]

    s.delay(name="blink", delay=0.1, handler=blink, param=args)

def squarea_animation(args):
    dirty_rects = []
    s = args[0]
    num = args[1]
    square = args[2]
    
    if square == 1:
        p = [228,334]
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
        dirty_rects.append(screen.blit(topleft, (247  - num - 20, 338)))
        dirty_rects.append(screen.blit(topright, (284, 347 - num - 10)))
        dirty_rects.append(screen.blit(bottomright, (278  + num + 15, 389)))
        dirty_rects.append(screen.blit(bottomleft, (230, 390 + num + 5)))

    if (s.game.anti_cheat.status == True):
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],130,130)))
    else:
        dirty_rects.append(screen.blit(bg_off, p, pygame.Rect(p[0],p[1],130,130)))
    
    pygame.display.update(dirty_rects)

def squareb_animation(args):
    dirty_rects = []
    s = args[0]
    num = args[1]
    square = args[2]
    
    if square == 2:
        p = [228,440]
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
        dirty_rects.append(screen.blit(topleft, (246 - num - 20, 444)))
        dirty_rects.append(screen.blit(topright, (284, 448 - num - 9)))
        dirty_rects.append(screen.blit(bottomright, (284  + num + 10, 496)))
        dirty_rects.append(screen.blit(bottomleft, (230, 498 + num + 8)))
    
    if (s.game.anti_cheat.status == True):
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],130,130)))
    else:
        dirty_rects.append(screen.blit(bg_off, p, pygame.Rect(p[0],p[1],130,130)))
    
    pygame.display.update(dirty_rects)

def squarec_animation(args):
    dirty_rects = []
    s = args[0]
    num = args[1]
    square = args[2]
    
    if square == 3:
        p = [339,334]
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
        dirty_rects.append(screen.blit(topleft, (350  - num - 10, 337)))
        dirty_rects.append(screen.blit(topright, (394, 338 - num - 5)))
        dirty_rects.append(screen.blit(bottomright, (386  + num + 15, 390)))
        dirty_rects.append(screen.blit(bottomleft, (341, 390 + num + 6)))
    
    if (s.game.anti_cheat.status == True):
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],130,130)))
    else:
        dirty_rects.append(screen.blit(bg_off, p, pygame.Rect(p[0],p[1],130,130)))
    
    pygame.display.update(dirty_rects)

def squared_animation(args):
    dirty_rects = []
    s = args[0]
    num = args[1]
    square = args[2]
    
    p = [338,440]
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
        dirty_rects.append(screen.blit(topleft, (347 - num - 10, 444)))
        dirty_rects.append(screen.blit(topright, (393, 452 - num - 13)))
        dirty_rects.append(screen.blit(bottomright, (370  + num + 29, 498)))
        dirty_rects.append(screen.blit(bottomleft, (343, 497 + num + 12)))
    
    if (s.game.anti_cheat.status == True):
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],130,130)))
    else:
        dirty_rects.append(screen.blit(bg_off, p, pygame.Rect(p[0],p[1],130,130)))
    
    pygame.display.update(dirty_rects)

def squaree_animation(args):
    dirty_rects = []
    s = args[0]
    num = args[1]
    square = args[2]
    
    p = [230,547]
    if s.game.square_e.position == 0:
        image = e3
        topleft = e_2
        topright = e_3
        bottomleft = e_4
        bottomright = e_1
    elif s.game.square_e.position == 1:
        image = e0
        topleft = e_1
        topright = e_2
        bottomleft = e_3
        bottomright = e_4
    elif s.game.square_e.position == 2:
        image = e1
        topleft = e_4
        topright = e_1
        bottomleft = e_2
        bottomright = e_3
    else:
        image = e2
        topleft = e_3
        topright = e_4
        bottomleft = e_1
        bottomright = e_2

    rect = pygame.Rect(p[0],p[1],200,200)

    #images are actually rendered left-right, but keeping naming convention in case I want to add some fancier rotation
    dirty_rects.append(screen.blit(topleft, (238 - num - 10, 554)))
    if num > -40:
        dirty_rects.append(screen.blit(topright, (284, 552 - num)))
    else:
        dirty_rects.append(screen.blit(topright, (339, 610 + num)))
    dirty_rects.append(screen.blit(bottomleft, (339 - num - 10, 552)))
    if num > -40:
        dirty_rects.append(screen.blit(bottomright, (394, 554 - num)))
    else:
        dirty_rects.append(screen.blit(bottomright, (230, 610 + num)))
    
    if (s.game.anti_cheat.status == True):
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],220,100)))
    else:
        dirty_rects.append(screen.blit(bg_off, p, pygame.Rect(p[0],p[1],220,100)))
    
    pygame.display.update(dirty_rects)


def eb_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]

    if s.game.extra_ball.position < 1:
        dirty_rects.append(screen.blit(bg_gi, (144,1010), pygame.Rect(144,1010,48,33)))
    if s.game.extra_ball.position < 2:
        dirty_rects.append(screen.blit(bg_gi, (193,1010), pygame.Rect(193,1010,66,34)))
    if s.game.extra_ball.position < 3:
        dirty_rects.append(screen.blit(bg_gi, (260,1010), pygame.Rect(260,1010,66,34)))
    if s.game.extra_ball.position < 4:
        dirty_rects.append(screen.blit(bg_gi, (330,1010), pygame.Rect(330,1010,48,33)))
    if s.game.extra_ball.position < 5:
        dirty_rects.append(screen.blit(bg_gi, (380,1010), pygame.Rect(380,1010,66,34)))
    if s.game.extra_ball.position < 6:
        dirty_rects.append(screen.blit(bg_gi, (445,1010), pygame.Rect(445,1010,66,34)))
    if s.game.extra_ball.position < 7:
        dirty_rects.append(screen.blit(bg_gi, (520,1010), pygame.Rect(520,1010,48,33)))
    if s.game.extra_ball.position < 8:
        dirty_rects.append(screen.blit(bg_gi, (569,1008), pygame.Rect(569,1008,66,34)))
    if s.game.extra_ball.position < 9:
        dirty_rects.append(screen.blit(bg_gi, (634,1007), pygame.Rect(634,1007,66,34)))

    pygame.display.update(dirty_rects)

    if num in [0,24,25,49]:
        if s.game.extra_ball.position < 1:
            p = [144,1010]
            dirty_rects.append(screen.blit(eb_number, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [1,15,26,40]:
        if s.game.extra_ball.position < 2:
            p = [193,1010]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [3,4,17,28,29,42]:
        if s.game.extra_ball.position < 3:
            p = [260,1010]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [5,18,30,43]:
        if s.game.extra_ball.position < 4:
            p = [330,1010]
            dirty_rects.append(screen.blit(eb_number, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [7,8,19,32,33,44]:
        if s.game.extra_ball.position < 5:
            p = [380,1010]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [9,10,20,34,35,45]:
        if s.game.extra_ball.position < 6:
            p = [445,1010]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [11,21,36,46]:
        if s.game.extra_ball.position < 7:
            p = [520,1010]
            dirty_rects.append(screen.blit(eb_number, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [12,22,37,47]:
        if s.game.extra_ball.position < 8:
            p = [569,1008]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [2,6,13,16,23,27,31,38,41,48]:
        if s.game.extra_ball.position < 9:
            p = [634,1007]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects) 
            return

def clear_odds(s, num):
    global screen

    dirty_rects = []

    if s.game.yellow_odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (38,824), pygame.Rect(38,824,27,51)))
    if s.game.yellow_odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (150,788), pygame.Rect(150,788,27,51)))
    if s.game.yellow_odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (192,792), pygame.Rect(192,792,27,51)))
    if s.game.yellow_odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (276,779), pygame.Rect(276,779,29,51)))
    if s.game.yellow_odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (412,776), pygame.Rect(412,776,38,53)))
    if s.game.yellow_odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (498,786), pygame.Rect(498,786,38,53)))
    if s.game.yellow_odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (552,786), pygame.Rect(552,786,38,53)))
    if s.game.yellow_odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (662,817), pygame.Rect(662,817,38,50)))

    if s.game.red_odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (30,762), pygame.Rect(30,762,29,55)))
    if s.game.red_odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (148,716), pygame.Rect(148,716,29,55)))
    if s.game.red_odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (202,715), pygame.Rect(202,715,29,55)))
    if s.game.red_odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (290,706), pygame.Rect(290,706,29,55)))
    if s.game.red_odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (407,704), pygame.Rect(407,704,40,56)))
    if s.game.red_odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (504,709), pygame.Rect(504,709,40,56)))
    if s.game.red_odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (552,715), pygame.Rect(552,715,40,56)))
    if s.game.red_odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (678,744), pygame.Rect(678,744,40,56)))

    if s.game.green_odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (36,883), pygame.Rect(36,883,26,50)))
    if s.game.green_odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (151,859), pygame.Rect(151,859,26,52)))
    if s.game.green_odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (196,862), pygame.Rect(196,862,26,52)))
    if s.game.green_odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (282,876), pygame.Rect(282,876,26,52)))
    if s.game.green_odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (413,886), pygame.Rect(413,886,37,55)))
    if s.game.green_odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (504,852), pygame.Rect(504,852,37,55)))
    if s.game.green_odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (552,856), pygame.Rect(552,856,37,52)))
    if s.game.green_odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (677,882), pygame.Rect(677,882,37,52)))

    pygame.display.update(dirty_rects)

def draw_odds_animation(s, num):
    global screen
    dirty_rects = []

    if num in [11,36]:
        if s.game.yellow_odds.position != 1:
            p = [36,824]
            dirty_rects.append(screen.blit(yellow_odds1, p))
            pygame.display.update(dirty_rects)
            return
    if num in [4,29]:
        if s.game.yellow_odds.position != 2:
            p = [150,788]
            dirty_rects.append(screen.blit(yellow_odds2, p))
            pygame.display.update(dirty_rects)
            return
    if num in [7,32]:
        if s.game.yellow_odds.position != 3:
            p = [192,792]
            dirty_rects.append(screen.blit(yellow_odds3, p))
            pygame.display.update(dirty_rects)
            return
    if num in [13,38]:
        if s.game.yellow_odds.position != 4:
            p = [276,779]
            dirty_rects.append(screen.blit(yellow_odds4, p))
            pygame.display.update(dirty_rects)
            return
    if num in [22,47]:
        if s.game.yellow_odds.position != 5:
            p = [412,776]
            dirty_rects.append(screen.blit(yellow_odds5, p))
            pygame.display.update(dirty_rects)
            return
    if num in [17,42]:
        if s.game.yellow_odds.position != 6:
            p = [498,786]
            dirty_rects.append(screen.blit(yellow_odds6, p))
            pygame.display.update(dirty_rects)
            return
    if num in [19,44]:
        if s.game.yellow_odds.position != 7:
            p = [552,786]
            dirty_rects.append(screen.blit(yellow_odds7, p))
            pygame.display.update(dirty_rects)
            return
    if num in [5,30]:
        if s.game.yellow_odds.position != 8:
            p = [662,817]
            dirty_rects.append(screen.blit(yellow_odds8, p))
            pygame.display.update(dirty_rects)
            return

    if num in [2,27]:
        if s.game.red_odds.position != 1:
            p = [30,762]
            dirty_rects.append(screen.blit(red_odds1, p))
            pygame.display.update(dirty_rects)
            return
    if num in [15,40]:
        if s.game.red_odds.position != 2:
            p = [148,716]
            dirty_rects.append(screen.blit(red_odds2, p))
            pygame.display.update(dirty_rects)
            return
    if num in [0,25]:
        if s.game.red_odds.position != 3:
            p = [202,715]
            dirty_rects.append(screen.blit(red_odds3, p))
            pygame.display.update(dirty_rects)
            return
    if num in [9,34]:
        if s.game.red_odds.position != 4:
            p = [290,706]
            dirty_rects.append(screen.blit(red_odds4, p))
            pygame.display.update(dirty_rects)
            return
    if num in [20,45]:
        if s.game.red_odds.position != 5:
            p = [407,704]
            dirty_rects.append(screen.blit(red_odds5, p))
            pygame.display.update(dirty_rects)
            return
    if num in [12,37]:
        if s.game.red_odds.position != 6:
            p = [507,709]
            dirty_rects.append(screen.blit(red_odds6, p))
            pygame.display.update(dirty_rects)
            return
    if num in [1,26]:
        if s.game.red_odds.position != 7:
            p = [552,715]
            dirty_rects.append(screen.blit(red_odds7, p))
            pygame.display.update(dirty_rects)
            return
    if num in [6,31]:
        if s.game.red_odds.position != 8:
            p = [678,744]
            dirty_rects.append(screen.blit(red_odds8, p))
            pygame.display.update(dirty_rects)
            return

    if num in [16,41]:
        if s.game.green_odds.position != 1:
            p = [36,883]
            dirty_rects.append(screen.blit(green_odds1, p))
            pygame.display.update(dirty_rects)
            return
    if num in [18,43]:
        if s.game.green_odds.position != 2:
            p = [151,859]
            dirty_rects.append(screen.blit(green_odds2, p))
            pygame.display.update(dirty_rects)
            return
    if num in [14,39]:
        if s.game.green_odds.position != 3:
            p = [196,862]
            dirty_rects.append(screen.blit(green_odds3, p))
            pygame.display.update(dirty_rects)
            return
    if num in [3,28]:
        if s.game.green_odds.position != 4:
            p = [282,876]
            dirty_rects.append(screen.blit(green_odds4, p))
            pygame.display.update(dirty_rects)
            return
    if num in [24,49]:
        if s.game.green_odds.position != 5:
            p = [413,886]
            dirty_rects.append(screen.blit(green_odds5, p))
            pygame.display.update(dirty_rects)
            return
    if num in [8,33]:
        if s.game.green_odds.position != 6:
            p = [504,852]
            dirty_rects.append(screen.blit(green_odds6, p))
            pygame.display.update(dirty_rects)
            return
    if num in [22,47]:
        if s.game.green_odds.position != 7:
            p = [552,856]
            dirty_rects.append(screen.blit(green_odds7, p))
            pygame.display.update(dirty_rects)
            return
    if num in [10,35]:
        if s.game.green_odds.position != 8:
            p = [677,882]
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
        dirty_rects.append(screen.blit(bg_gi, (179,654), pygame.Rect(179,654,51,51)))
    if s.game.magic_squares_feature.position < 6:
        dirty_rects.append(screen.blit(bg_gi, (232,654), pygame.Rect(232,654,51,51)))
    if s.game.magic_squares_feature.position < 7:
        dirty_rects.append(screen.blit(bg_gi, (285,654), pygame.Rect(285,654,51,51)))
    if s.game.magic_squares_feature.position < 8:
        dirty_rects.append(screen.blit(bg_gi, (338,654), pygame.Rect(338,654,51,51)))
    if s.game.magic_squares_feature.position < 9:
        dirty_rects.append(screen.blit(bg_gi, (389,654), pygame.Rect(389,654,51,51)))

    if s.game.selection_feature.position not in [3,4]:
        dirty_rects.append(screen.blit(bg_gi, (41,938), pygame.Rect(41,938,59,58)))
        dirty_rects.append(screen.blit(bg_gi, (569,500), pygame.Rect(569,500,134,70)))
    if s.game.selection_feature.position not in [5,6]:
        dirty_rects.append(screen.blit(bg_gi, (635,935), pygame.Rect(635,935,59,58)))
        dirty_rects.append(screen.blit(bg_gi, (569,426), pygame.Rect(569,426,134,70)))
    if s.game.ballyhole.status == False:
        dirty_rects.append(screen.blit(bg_gi, (45,500), pygame.Rect(45,500,119,69)))
    if s.game.corners.status == False:
        dirty_rects.append(screen.blit(bg_gi, (46,418), pygame.Rect(46,418,119,69)))
    if s.game.selection_feature.position not in [7,8]:
        dirty_rects.append(screen.blit(bg_gi, (569,352), pygame.Rect(569,352,134,70)))
    if s.game.selection_feature.position != 9:
        dirty_rects.append(screen.blit(bg_gi, (569,280), pygame.Rect(569,280,134,70)))
    pygame.display.update(dirty_rects)


def draw_feature_animation(s, num):
    global screen
    dirty_rects = []

    if num in [2,12,22,27,37,47]:
        if s.game.magic_squares_feature.position < 6:
            p = [179,654]
            dirty_rects.append(screen.blit(ms_letter, p))
            p = [232,654]
            dirty_rects.append(screen.blit(ms_letter, p))
            pygame.display.update(dirty_rects)
            return
    if num in [17,23,42,48]:
        if s.game.magic_squares_feature.position < 7:
            p = [285,654]
            dirty_rects.append(screen.blit(ms_letter, p))
            pygame.display.update(dirty_rects)
            return
    if num in [5,15,24,30,40,49]:
        if s.game.magic_squares_feature.position < 8:
            p = [338,654]
            dirty_rects.append(screen.blit(ms_letter, p))
            pygame.display.update(dirty_rects)
            return
    if num in [10,20,25,35,45,50]:
        if s.game.magic_squares_feature.position < 9:
            p = [389,654]
            dirty_rects.append(screen.blit(ms_letter, p))
            pygame.display.update(dirty_rects)
            return

    if num in [8,18,33,43]:
        if s.game.selection_feature.position not in [3,4]:
            p = [41,938]
            dirty_rects.append(screen.blit(rollover, p))
            p = [569,500]
            dirty_rects.append(screen.blit(time, p))
            s.game.coils.yellowROLamp.pulse(85)
            pygame.display.update(dirty_rects)
            return
    if num in [3,13,28,38]:
        if s.game.selection_feature.position not in [5,6]:
            p = [635,935]
            dirty_rects.append(screen.blit(rollover, p))
            p = [569,426]
            dirty_rects.append(screen.blit(time, p))
            s.game.coils.redROLamp.pulse(85)
            pygame.display.update(dirty_rects)
            return
    if num in [4,14,29,39]:
        if s.game.ballyhole.status == False:
            p = [45,500]
            dirty_rects.append(screen.blit(ballyhole, p))
            pygame.display.update(dirty_rects)
            return
    if num in [9,19,34,44]:
        if s.game.corners.status == False:
            p = [46,418]
            dirty_rects.append(screen.blit(corners, p))
            pygame.display.update(dirty_rects)
            return
    if num in [11,21,36,46]:
        if s.game.selection_feature.position not in [7,8]:
            p = [569,352]
            dirty_rects.append(screen.blit(time, p))
            pygame.display.update(dirty_rects)
            return
    if num in [0,6,16,25,31,41]:
        if s.game.selection_feature.position != 9:
            p = [569,280]
            dirty_rects.append(screen.blit(time, p))
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


