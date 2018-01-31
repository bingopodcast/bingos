
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
                elif s.game.square_c.position == 2:
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
        screen.blit(ms_letter, p)
        pygame.display.update()
   

def odds_animation(num):
    global screen

