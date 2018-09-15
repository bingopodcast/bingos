
import pygame

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

meter = pygame.image.load('graphics/assets/register_cover.png').convert()
number = pygame.image.load('sun_valley/assets/number.png').convert_alpha()
feature = pygame.image.load('sun_valley/assets/feature.png').convert_alpha()
ms_letter = pygame.image.load('sun_valley/assets/ms_letter.png').convert_alpha()
ms_arrow = pygame.image.load('sun_valley/assets/ms_arrow.png').convert_alpha()
select_now = pygame.image.load('sun_valley/assets/select_now.png').convert_alpha()
corners = pygame.image.load('sun_valley/assets/feature.png').convert_alpha()
ballyhole = pygame.image.load('sun_valley/assets/feature.png').convert_alpha()
red_odds1 = pygame.image.load('sun_valley/assets/red_odds1.png').convert_alpha()
red_odds2 = pygame.image.load('sun_valley/assets/red_odds2.png').convert_alpha()
red_odds3 = pygame.image.load('sun_valley/assets/red_odds3.png').convert_alpha()
red_odds4 = pygame.image.load('sun_valley/assets/red_odds4.png').convert_alpha()
red_odds5 = pygame.image.load('sun_valley/assets/red_odds5.png').convert_alpha()
red_odds6 = pygame.image.load('sun_valley/assets/red_odds6.png').convert_alpha()
red_odds7 = pygame.image.load('sun_valley/assets/red_odds7.png').convert_alpha()
red_odds8 = pygame.image.load('sun_valley/assets/red_odds8.png').convert_alpha()
yellow_odds1 = pygame.image.load('sun_valley/assets/yellow_odds1.png').convert_alpha()
yellow_odds2 = pygame.image.load('sun_valley/assets/yellow_odds2.png').convert_alpha()
yellow_odds3 = pygame.image.load('sun_valley/assets/yellow_odds3.png').convert_alpha()
yellow_odds4 = pygame.image.load('sun_valley/assets/yellow_odds4.png').convert_alpha()
yellow_odds5 = pygame.image.load('sun_valley/assets/yellow_odds5.png').convert_alpha()
yellow_odds6 = pygame.image.load('sun_valley/assets/yellow_odds6.png').convert_alpha()
yellow_odds7 = pygame.image.load('sun_valley/assets/yellow_odds7.png').convert_alpha()
yellow_odds8 = pygame.image.load('sun_valley/assets/yellow_odds8.png').convert_alpha()
green_odds1 = pygame.image.load('sun_valley/assets/green_odds1.png').convert_alpha()
green_odds2 = pygame.image.load('sun_valley/assets/green_odds2.png').convert_alpha()
green_odds3 = pygame.image.load('sun_valley/assets/green_odds3.png').convert_alpha()
green_odds4 = pygame.image.load('sun_valley/assets/green_odds4.png').convert_alpha()
green_odds5 = pygame.image.load('sun_valley/assets/green_odds5.png').convert_alpha()
green_odds6 = pygame.image.load('sun_valley/assets/green_odds6.png').convert_alpha()
green_odds7 = pygame.image.load('sun_valley/assets/green_odds7.png').convert_alpha()
green_odds8 = pygame.image.load('sun_valley/assets/green_odds8.png').convert_alpha()
extra_balls = pygame.image.load('sun_valley/assets/extra_balls.png').convert_alpha()
eb = pygame.image.load('sun_valley/assets/eb.png').convert_alpha()
eb_number = pygame.image.load('sun_valley/assets/eb_number.png').convert_alpha()
tilt = pygame.image.load('sun_valley/assets/tilt.png').convert_alpha()
time = pygame.image.load('sun_valley/assets/time.png').convert_alpha()
s_arrow = pygame.image.load('sun_valley/assets/sf_arrow.png').convert_alpha()
a0 = pygame.image.load('sun_valley/assets/a0.png').convert_alpha()
a1 = pygame.image.load('sun_valley/assets/a1.png').convert_alpha()
a2 = pygame.image.load('sun_valley/assets/a2.png').convert_alpha()
a3 = pygame.image.load('sun_valley/assets/a3.png').convert_alpha()
b0 = pygame.image.load('sun_valley/assets/b0.png').convert_alpha()
b1 = pygame.image.load('sun_valley/assets/b1.png').convert_alpha()
b2 = pygame.image.load('sun_valley/assets/b2.png').convert_alpha()
b3 = pygame.image.load('sun_valley/assets/b3.png').convert_alpha()
c0 = pygame.image.load('sun_valley/assets/c0.png').convert_alpha()
c1 = pygame.image.load('sun_valley/assets/c1.png').convert_alpha()
c2 = pygame.image.load('sun_valley/assets/c2.png').convert_alpha()
c3 = pygame.image.load('sun_valley/assets/c3.png').convert_alpha()
d0 = pygame.image.load('sun_valley/assets/d0.png').convert_alpha()
d1 = pygame.image.load('sun_valley/assets/d1.png').convert_alpha()
d2 = pygame.image.load('sun_valley/assets/d2.png').convert_alpha()
d3 = pygame.image.load('sun_valley/assets/d3.png').convert_alpha()
e0 = pygame.image.load('sun_valley/assets/e0.png').convert_alpha()
e1 = pygame.image.load('sun_valley/assets/e1.png').convert_alpha()
e2 = pygame.image.load('sun_valley/assets/e2.png').convert_alpha()
e3 = pygame.image.load('sun_valley/assets/e3.png').convert_alpha()
f0 = pygame.image.load('sun_valley/assets/f0.png').convert_alpha()
rollover = pygame.image.load('sun_valley/assets/rollover.png').convert_alpha()
bg_menu = pygame.image.load('sun_valley/assets/sun_valley_menu.png')
bg_gi = pygame.image.load('sun_valley/assets/sun_valley_gi.png')
bg_off = pygame.image.load('sun_valley/assets/sun_valley_off.png')
a_1 = pygame.image.load('sun_valley/assets/a-1.png').convert_alpha()
a_2 = pygame.image.load('sun_valley/assets/a-2.png').convert_alpha()
a_3 = pygame.image.load('sun_valley/assets/a-3.png').convert_alpha()
a_4 = pygame.image.load('sun_valley/assets/a-4.png').convert_alpha()
b_1 = pygame.image.load('sun_valley/assets/b-1.png').convert_alpha()
b_2 = pygame.image.load('sun_valley/assets/b-2.png').convert_alpha()
b_3 = pygame.image.load('sun_valley/assets/b-3.png').convert_alpha()
b_4 = pygame.image.load('sun_valley/assets/b-4.png').convert_alpha()
c_1 = pygame.image.load('sun_valley/assets/c-1.png').convert_alpha()
c_2 = pygame.image.load('sun_valley/assets/c-2.png').convert_alpha()
c_3 = pygame.image.load('sun_valley/assets/c-3.png').convert_alpha()
c_4 = pygame.image.load('sun_valley/assets/c-4.png').convert_alpha()
d_1 = pygame.image.load('sun_valley/assets/d-1.png').convert_alpha()
d_2 = pygame.image.load('sun_valley/assets/d-2.png').convert_alpha()
d_3 = pygame.image.load('sun_valley/assets/d-3.png').convert_alpha()
d_4 = pygame.image.load('sun_valley/assets/d-4.png').convert_alpha()
e_1 = pygame.image.load('sun_valley/assets/e-1.png').convert_alpha()
e_2 = pygame.image.load('sun_valley/assets/e-2.png').convert_alpha()
e_3 = pygame.image.load('sun_valley/assets/e-3.png').convert_alpha()
e_4 = pygame.image.load('sun_valley/assets/e-4.png').convert_alpha()

class scorereel():
    """ Score Reels are used to count replays """
    def __init__(self, pos, image):
        self.position = pos
        self.default_y = self.position[1]
        self.image = pygame.image.load(image).convert()

reel1 = scorereel([103,293], "graphics/assets/white_reel.png")
reel10 = scorereel([84,293], "graphics/assets/white_reel.png")
reel100 = scorereel([65,293], "graphics/assets/white_reel.png")

def display(s, replays=0, menu=False):
    
    meter.set_colorkey((255,0,252))
    meter_position = [55,293]

    screen.blit(reel1.image, reel1.position)
    screen.blit(reel10.image, reel10.position)
    screen.blit(reel100.image, reel100.position)
    screen.blit(meter, meter_position)

    if s.game.square_a.position == 0:
        p = [228,345]
        screen.blit(a0, p)
    if s.game.square_a.position == 1:
        p = [228,345]
        screen.blit(a1, p)
    if s.game.square_a.position == 2:
        p = [228,345]
        screen.blit(a2, p)
    if s.game.square_a.position == 3:
        p = [228,345]
        screen.blit(a3, p)
    if s.game.square_b.position == 0:
        p = [228,453]
        screen.blit(b0, p)
    if s.game.square_b.position == 1:
        p = [228,453]
        screen.blit(b1, p)
    if s.game.square_b.position == 2:
        p = [228,453]
        screen.blit(b2, p)
    if s.game.square_b.position == 3:
        p = [228,453]
        screen.blit(b3, p)
    if s.game.square_c.position == 0:
        p = [339,346]
        screen.blit(c0, p)
    if s.game.square_c.position == 1:
        p = [339,346]
        screen.blit(c1, p)
    if s.game.square_c.position == 2:
        p = [339,346]
        screen.blit(c2, p)
    if s.game.square_c.position == 3:
        p = [339,346]
        screen.blit(c3, p)
    if s.game.square_d.position == 0:
        p = [338,453]
        screen.blit(d0, p)
    if s.game.square_d.position == 1:
        p = [338,453]
        screen.blit(d1, p)
    if s.game.square_d.position == 2:
        p = [338,453]
        screen.blit(d2, p)
    if s.game.square_d.position == 3:
        p = [338,453]
        screen.blit(d3, p)
    if s.game.square_e.position == 0:
        p = [230,561]
        screen.blit(e0, p)
    if s.game.square_e.position == 1:
        p = [230,561]
        screen.blit(e1, p)
    if s.game.square_e.position == 2:
        p = [230,561]
        screen.blit(e2, p)
    if s.game.square_e.position == 3:
        p = [230,561]
        screen.blit(e3, p)
    if s.game.line_f.position == 0 or s.game.line_f.position == 2:
        p = [442,288]
        screen.blit(f0, p)
    elif s.game.line_f.position == 1:
        p = [442,342]
        screen.blit(f0, p)
    elif s.game.line_f.position == 3:
        p = [442,235]
        screen.blit(f0, p)


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
                    p = [286,348]
                    screen.blit(number, p)
                elif s.game.square_a.position == 1:
                    p = [285,400]
                    screen.blit(number, p)
                elif s.game.square_a.position == 2:
                    p = [231,401]
                    screen.blit(number, p)
                else:
                    p = [231,348]
                    screen.blit(number, p)
            if 2 in s.holes:
                if s.game.square_c.position == 0:
                    p = [340,348]
                    screen.blit(number, p)
                elif s.game.square_c.position == 1:
                    p = [394,348]
                    screen.blit(number, p)
                elif s.game.square_c.position == 2:
                    p = [393,400]
                    screen.blit(number, p)
                else:
                    p = [340,400]
                    screen.blit(number, p)
            if 3 in s.holes:
                if s.game.square_e.position == 0:
                    p = [396,563]
                    screen.blit(number, p)
                elif s.game.square_e.position == 1:
                    p = [232,562]
                    screen.blit(number, p)
                elif s.game.square_e.position == 2:
                    p = [286,563]
                    screen.blit(number, p)
                else:
                    p = [340,564]
                    screen.blit(number, p)
            if 4 in s.holes:
                if s.game.square_a.position == 0:
                    p = [231,400]
                    screen.blit(number, p)
                elif s.game.square_a.position == 1:
                    p = [232,349]
                    screen.blit(number, p)
                elif s.game.square_a.position == 2:
                    p = [285,348]
                    screen.blit(number, p)
                else:
                    p = [285,400]
                    screen.blit(number, p)
            if 5 in s.holes:
                if s.game.square_d.position == 0:
                    p = [341,509]
                    screen.blit(number, p)
                elif s.game.square_d.position == 1:
                    p = [340,455]
                    screen.blit(number, p)
                elif s.game.square_d.position == 2:
                    p = [394,454]
                    screen.blit(number, p)
                else:
                    p = [396,508]
                    screen.blit(number, p)
            if 6 in s.holes:
                if s.game.square_b.position == 0:
                    p = [231,509]
                    screen.blit(number, p)
                elif s.game.square_b.position == 1:
                    p = [232,454]
                    screen.blit(number, p)
                elif s.game.square_b.position == 2:
                    p = [285,454]
                    screen.blit(number, p)
                else:
                    p = [286,509]
                    screen.blit(number, p)
            if 7 in s.holes:
                if s.game.square_c.position == 0:
                    p = [341,401]
                    screen.blit(number, p)
                elif s.game.square_c.position == 1:
                    p = [340,349]
                    screen.blit(number, p)
                elif s.game.square_c.position == 2:
                    p = [394,348]
                    screen.blit(number, p)
                else:
                    p = [395,401]
                    screen.blit(number, p)
            if 8 in s.holes:
                if s.game.square_e.position == 0:
                    p = [286,562]
                    screen.blit(number, p)
                elif s.game.square_e.position == 1:
                    p = [340,562]
                    screen.blit(number, p)
                elif s.game.square_e.position == 2:
                    p = [396,562]
                    screen.blit(number, p)
                else:
                    p = [231,562]
                    screen.blit(number, p)
            if 9 in s.holes:
                if s.game.square_a.position == 0:
                    p = [232,349]
                    screen.blit(number, p)
                elif s.game.square_a.position == 1:
                    p = [286,348]
                    screen.blit(number, p)
                elif s.game.square_a.position == 2:
                    p = [286,399]
                    screen.blit(number, p)
                else:
                    p = [232,400]
                    screen.blit(number, p)
            if 10 in s.holes:
                if s.game.line_f.position == 0 or s.game.line_f.position == 2:
                    p = [446,564]
                    screen.blit(number, p)
                elif s.game.line_f.position == 1:
                    p = [447,349]
                    screen.blit(number, p)
                else:
                    p = [446,510]
                    screen.blit(number, p)
            if 11 in s.holes:
                if s.game.square_c.position == 0:
                    p = [394,350]
                    screen.blit(number, p)
                elif s.game.square_c.position == 1:
                    p = [394,402]
                    screen.blit(number, p)
                elif s.game.square_c.position == 2:
                    p = [341,400]
                    screen.blit(number, p)
                else:
                    p = [340,348]
                    screen.blit(number, p)
            if 12 in s.holes:
                if s.game.square_e.position == 0:
                    p = [231,562]
                    screen.blit(number, p)
                elif s.game.square_e.position == 1:
                    p = [286,564]
                    screen.blit(number, p)
                elif s.game.square_e.position == 2:
                    p = [342,562]
                    screen.blit(number, p)
                else:
                    p = [396,562]
                    screen.blit(number, p)
            if 13 in s.holes:
                if s.game.square_d.position == 0:
                    p = [395,454]
                    screen.blit(number, p)
                elif s.game.square_d.position == 1:
                    p = [396,508]
                    screen.blit(number, p)
                elif s.game.square_d.position == 2:
                    p = [342,510]
                    screen.blit(number, p)
                else:
                    p = [342,455]
                    screen.blit(number, p)
            if 14 in s.holes:
                if s.game.square_e.position == 0:
                    p = [342,562]
                    screen.blit(number, p)
                elif s.game.square_e.position == 1:
                    p = [396,562]
                    screen.blit(number, p)
                elif s.game.square_e.position == 2:
                    p = [232,562]
                    screen.blit(number, p)
                else:
                    p = [287,563]
                    screen.blit(number, p)
            if 15 in s.holes:
                if s.game.line_f.position == 0 or s.game.line_f.position == 2:
                    p = [446,350]
                    screen.blit(number, p)
                if s.game.line_f.position == 1:
                    p = [446,404]
                    screen.blit(number, p)
                if s.game.line_f.position == 3:
                    p = [446,564]
                    screen.blit(number, p)
            if 16 in s.holes:
                if s.game.square_d.position == 0:
                    p = [341,456]
                    screen.blit(number, p)
                elif s.game.square_d.position == 1:
                    p = [394,454]
                    screen.blit(number, p)
                elif s.game.square_d.position == 2:
                    p = [396,508]
                    screen.blit(number, p)
                else:
                    p = [342,510]
                    screen.blit(number, p)
            if 17 in s.holes:
                if s.game.line_f.position == 0 or s.game.line_f.position == 2:
                    p = [446,456]
                    screen.blit(number, p)
                elif s.game.line_f.position == 1:
                    p = [446,510]
                    screen.blit(number, p)
                elif s.game.line_f.position == 3:
                    p = [446,404]
                    screen.blit(number, p)
            if 18 in s.holes:
                if s.game.line_f.position == 0 or s.game.line_f.position == 2:
                    p = [447,403]
                    screen.blit(number, p)
                elif s.game.line_f.position == 1:
                    p = [446,456]
                    screen.blit(number, p)
                elif s.game.line_f.position == 3:
                    p = [446,349]
                    screen.blit(number, p)
            if 19 in s.holes:
                if s.game.square_a.position == 0:
                    p = [286,400]
                    screen.blit(number, p)
                elif s.game.square_a.position == 1:
                    p = [231,400]
                    screen.blit(number, p)
                elif s.game.square_a.position == 2:
                    p = [232,350]
                    screen.blit(number, p)
                else:
                    p = [286,350]
                    screen.blit(number, p)
            if 20 in s.holes:
                if s.game.line_f.position == 0 or s.game.line_f.position == 2:
                    p = [447,511]
                    screen.blit(number, p)
                elif s.game.line_f.position == 1:
                    p = [447,564]
                    screen.blit(number, p)
                elif s.game.line_f.position == 3:
                    p = [447,457]
                    screen.blit(number, p)
            if 21 in s.holes:
                if s.game.square_d.position == 0:
                    p = [396,508]
                    screen.blit(number, p)
                elif s.game.square_d.position == 1:
                    p = [342,510]
                    screen.blit(number, p)
                elif s.game.square_d.position == 2:
                    p = [341,454]
                    screen.blit(number, p)
                else:
                    p = [394,454]
                    screen.blit(number, p)
            if 22 in s.holes:
                if s.game.square_c.position == 0:
                    p = [395,402]
                    screen.blit(number, p)
                elif s.game.square_c.position == 1:
                    p = [341,401]
                    screen.blit(number, p)
                elif s.game.square_c.position == 2:
                    p = [340,349]
                    screen.blit(number, p)
                else:
                    p = [394,349]
                    screen.blit(number, p)
            if 23 in s.holes:
                if s.game.square_b.position == 0:
                    p = [286,509]
                    screen.blit(number, p)
                elif s.game.square_b.position == 1:
                    p = [231,508]
                    screen.blit(number, p)
                elif s.game.square_b.position == 2:
                    p = [232,454]
                    screen.blit(number, p)
                else:
                    p = [286,454]
                    screen.blit(number, p)
            if 24 in s.holes:
                if s.game.square_b.position == 0:
                    p = [286,454]
                    screen.blit(number, p)
                elif s.game.square_b.position == 1:
                    p = [286,509]
                    screen.blit(number, p)
                elif s.game.square_b.position == 2:
                    p = [231,508]
                    screen.blit(number, p)
                else:
                    p = [232,454]
                    screen.blit(number, p)
            if 25 in s.holes:
                if s.game.square_b.position == 0:
                    p = [232,454]
                    screen.blit(number, p)
                elif s.game.square_b.position == 1:
                    p = [286,454]
                    screen.blit(number, p)
                elif s.game.square_b.position == 2:
                    p = [286,509]
                    screen.blit(number, p)
                else:
                    p = [231,508]
                    screen.blit(number, p)


    if s.game.magic_squares_feature.position == 1:
        p = [20,670]
        screen.blit(ms_arrow, p)
    if s.game.magic_squares_feature.position == 2:
        p = [58,670]
        screen.blit(ms_arrow, p)
    if s.game.magic_squares_feature.position == 3:
        p = [98,670]
        screen.blit(ms_arrow, p)
    if s.game.magic_squares_feature.position == 4:
        p = [139,670]
        screen.blit(ms_arrow, p)
    if s.game.magic_squares_feature.position >= 5:
        p = [180,664]
        screen.blit(ms_letter, p)
    if s.game.magic_squares_feature.position >= 6:
        p = [232,664]
        screen.blit(ms_letter, p)
    if s.game.magic_squares_feature.position >= 7:
        p = [280,664]
        screen.blit(ms_letter, p)
    if s.game.magic_squares_feature.position >= 8:
        p = [330,664]
        screen.blit(ms_letter, p)
    if s.game.magic_squares_feature.position == 9:
        p = [378,664]
        screen.blit(ms_letter, p)

    sf = s.game.selection_feature.position 
    if s.game.magic_squares_feature.position >= 5 and sf <= 6:
        p = [568,591]
        screen.blit(time, p)
    if sf <= 6:
        if sf == 1:
            p = [533,610]
            screen.blit(s_arrow, p)
        if sf == 2:
            p = [533,572]
            screen.blit(s_arrow, p)
        if sf == 3:
            p = [533,534]
            screen.blit(s_arrow, p)
        if sf == 4:
            p = [533,498]
            screen.blit(s_arrow, p)
        if sf == 5:
            p = [533,458]
            screen.blit(s_arrow, p)
        if sf == 6:
            p = [533,422]
            screen.blit(s_arrow, p)
        if s.game.magic_squares_feature.position >= 5 or s.game.magic_line_f.status == True:
            if s.game.ball_count.position == 3:
                s.cancel_delayed(name="blink")
                blink([s,1,1])
            else:
                s.cancel_delayed(name="blink")
    if sf == 3 or sf == 4:
        if s.game.magic_squares_feature.position >= 5:
            p = [568,516]
            screen.blit(time, p)
            p = [35,934]
            screen.blit(rollover, p)
    if sf == 5 or sf == 6:
        if s.game.magic_squares_feature.position >= 5:
            p = [568,440]
            screen.blit(time, p)
            p = [624,934]
            screen.blit(rollover, p)
    if sf == 7 or sf == 8:
        if sf == 7:
            p = [533,384]
            screen.blit(s_arrow, p)
        if sf == 8:
            p = [533,348]
            screen.blit(s_arrow, p)
        if s.game.magic_squares_feature.position >= 5:
            p = [568,365]
            screen.blit(time, p)
        if s.game.ball_count.position == 4:
            s.cancel_delayed(name="blink")
            blink([s,1,1])
        else:
            s.cancel_delayed(name="blink")
    if sf == 9:
        p = [535,310]
        screen.blit(s_arrow, p)
        if s.game.magic_squares_feature.position >= 5:
            p = [568,290]
            screen.blit(time, p)
        if s.game.ball_count.position == 5:
            s.cancel_delayed(name="blink")
            blink([s,1,1])
        else:
            s.cancel_delayed(name="blink")

    if s.game.corners.status == True:
        p = [52,408]
        screen.blit(corners, p)
    if s.game.three_as_four.status == True:
        p = [52,490]
        screen.blit(corners, p)
    if s.game.magic_line_f.status == True:
        p = [52,569]
        screen.blit(corners, p)

    if s.game.extra_ball.position >= 1:
        p = [136,1010]
        screen.blit(eb_number, p)
    if s.game.extra_ball.position >= 2:
        p = [189,1010]
        screen.blit(eb, p)
    if s.game.extra_ball.position >= 3:
        p = [256,1010]
        screen.blit(eb, p)
    if s.game.extra_ball.position >= 4:
        p = [326,1010]
        screen.blit(eb_number, p)
    if s.game.extra_ball.position >= 5:
        p = [376,1010]
        screen.blit(eb, p)
    if s.game.extra_ball.position >= 6:
        p = [441,1010]
        screen.blit(eb, p)
    if s.game.extra_ball.position >= 7:
        p = [516,1010]
        screen.blit(eb_number, p)
    if s.game.extra_ball.position >= 8:
        p = [565,1008]
        screen.blit(eb, p)
    if s.game.extra_ball.position == 9:
        p = [630,1009]
        screen.blit(eb, p)

    if s.game.eb_play.status == True:
        p = [28,1006]
        screen.blit(extra_balls, p)

    if s.game.red_odds.position == 1:
        p = [19,719]
        screen.blit(red_odds1, p)
    elif s.game.red_odds.position == 2:
        p = [150,716]
        screen.blit(red_odds2, p)
    elif s.game.red_odds.position == 3:
        p = [205,725]
        screen.blit(red_odds3, p)
    elif s.game.red_odds.position == 4:
        p = [293,719]
        screen.blit(red_odds4, p)
    elif s.game.red_odds.position == 5:
        p = [378,719]
        screen.blit(red_odds5, p)
    elif s.game.red_odds.position == 6:
        p = [488,717]
        screen.blit(red_odds6, p)
    elif s.game.red_odds.position == 7:
        p = [526,721]
        screen.blit(red_odds7, p)
    elif s.game.red_odds.position == 8:
        p = [654,715]
        screen.blit(red_odds8, p)

    if s.game.yellow_odds.position == 1:
        p = [27,797]
        screen.blit(yellow_odds1, p)
    elif s.game.yellow_odds.position == 2:
        p = [134,802]
        screen.blit(yellow_odds2, p)
    elif s.game.yellow_odds.position == 3:
        p = [183,831]
        screen.blit(yellow_odds3, p)
    elif s.game.yellow_odds.position == 4:
        p = [297,787]
        screen.blit(yellow_odds4, p)
    elif s.game.yellow_odds.position == 5:
        p = [395,823]
        screen.blit(yellow_odds5, p)
    elif s.game.yellow_odds.position == 6:
        p = [470,809]
        screen.blit(yellow_odds6, p)
    elif s.game.yellow_odds.position == 7:
        p = [541,810]
        screen.blit(yellow_odds7, p)
    elif s.game.yellow_odds.position == 8:
        p = [674,828]
        screen.blit(yellow_odds8, p)

    if s.game.green_odds.position == 1:
        p = [20,877]
        screen.blit(green_odds1, p)
    elif s.game.green_odds.position == 2:
        p = [147,867]
        screen.blit(green_odds2, p)
    elif s.game.green_odds.position == 3:
        p = [220,874]
        screen.blit(green_odds3, p)
    elif s.game.green_odds.position == 4:
        p = [279,887]
        screen.blit(green_odds4, p)
    elif s.game.green_odds.position == 5:
        p = [389,901]
        screen.blit(green_odds5, p)
    elif s.game.green_odds.position == 6:
        p = [464,884]
        screen.blit(green_odds6, p)
    elif s.game.green_odds.position == 7:
        p = [514,867]
        screen.blit(green_odds7, p)
    elif s.game.green_odds.position == 8:
        p = [665,888]
        screen.blit(green_odds8, p)

    if s.game.tilt.status == True:
        tilt_position = [66,356]
        screen.blit(tilt, tilt_position)

    pygame.display.update()

def blink(args):
    dirty_rects = []
    s = args[0]
    b = args[1]
    sn = args[2]

    if b == 0:
        if sn == 1:
            p = [556,667]
            dirty_rects.append(screen.blit(select_now, p))
        pygame.display.update(dirty_rects)
    else:
        dirty_rects.append(screen.blit(bg_gi, (556,667), pygame.Rect(556,667,147,35)))
        pygame.display.update(dirty_rects)
    b = not b

    args = [s,b,sn]

    s.delay(name="blink", delay=0.1, handler=blink, param=args)

def line_animation(args):
    dirty_rects = []
    s = args[0]
    num = args[1]
    line = args[2]

    if line == 1:
        if s.game.line_f.position == 0:
            dirty_rects.append(screen.blit(f0, (442, 235 - num)))
        elif s.game.line_f.position == 1:
            dirty_rects.append(screen.blit(f0, (442, 288 - num)))
        elif s.game.line_f.position == 2:
            dirty_rects.append(screen.blit(f0, (442, 342 + num)))
        elif s.game.line_f.position == 3:
            dirty_rects.append(screen.blit(f0, (442, 288 + num)))

        if (s.game.anti_cheat.status == True):
            dirty_rects.append(screen.blit(bg_gi, (442,235), pygame.Rect(442,235,58,706)))
        else:
            dirty_rects.append(screen.blit(bg_off, (442,235), pygame.Rect(442,235,58,706)))
        
        if s.game.yellow_odds.position == 5:
            p = [395,823]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],43,53)))
            dirty_rects.append(screen.blit(yellow_odds5, p))
        elif s.game.yellow_odds.position == 6:
            p = [470,809]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],37,51)))
            dirty_rects.append(screen.blit(yellow_odds6, p))
        
        if s.game.red_odds.position == 5:
            p = [378,719]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],34,52)))
            dirty_rects.append(screen.blit(red_odds5, p))
        elif s.game.red_odds.position == 6:
            p = [488,717]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],34,52)))
            dirty_rects.append(screen.blit(red_odds6, p))
     
        if s.game.green_odds.position == 5:
            p = [389,901]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],37,53)))
            dirty_rects.append(screen.blit(green_odds5, p))
        elif s.game.green_odds.position == 6:
            p = [464,884]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],37,53)))
            dirty_rects.append(screen.blit(green_odds6, p))
     
    pygame.display.update(dirty_rects)




def squarea_animation(args):
    dirty_rects = []
    s = args[0]
    num = args[1]
    square = args[2]
    
    if square == 1:
        p = [228,345]
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
        dirty_rects.append(screen.blit(topleft, (247  - num - 20, 349)))
        dirty_rects.append(screen.blit(topright, (284, 356 - num - 10)))
        dirty_rects.append(screen.blit(bottomright, (278  + num + 15, 400)))
        dirty_rects.append(screen.blit(bottomleft, (230, 401 + num + 5)))

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
        p = [228,453]
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
        dirty_rects.append(screen.blit(topleft, (246 - num - 20, 457)))
        dirty_rects.append(screen.blit(topright, (284, 461 - num - 9)))
        dirty_rects.append(screen.blit(bottomright, (284  + num + 10, 509)))
        dirty_rects.append(screen.blit(bottomleft, (230, 511 + num + 8)))
    
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
        p = [339,346]
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
        dirty_rects.append(screen.blit(topleft, (350  - num - 10, 349)))
        dirty_rects.append(screen.blit(topright, (394, 350 - num - 5)))
        dirty_rects.append(screen.blit(bottomright, (386  + num + 15, 400)))
        dirty_rects.append(screen.blit(bottomleft, (339, 400 + num + 6)))
    
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
    
    p = [338,453]
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
        dirty_rects.append(screen.blit(topleft, (347 - num - 10, 457)))
        dirty_rects.append(screen.blit(topright, (393, 465 - num - 13)))
        dirty_rects.append(screen.blit(bottomright, (370  + num + 29, 511)))
        dirty_rects.append(screen.blit(bottomleft, (343, 510 + num + 12)))
    
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
    
    p = [230,561]
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
    dirty_rects.append(screen.blit(topleft, (238 - num - 10, 568)))
    if num > -40:
        dirty_rects.append(screen.blit(topright, (284, 566 - num)))
    else:
        dirty_rects.append(screen.blit(topright, (339, 624 + num)))
    dirty_rects.append(screen.blit(bottomleft, (339 - num - 10, 566)))
    if num > -40:
        dirty_rects.append(screen.blit(bottomright, (394, 568 - num)))
    else:
        dirty_rects.append(screen.blit(bottomright, (230, 624 + num)))
    
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
        dirty_rects.append(screen.blit(bg_gi, (136,1010), pygame.Rect(136,1010,45,29)))
    if s.game.extra_ball.position < 2:
        dirty_rects.append(screen.blit(bg_gi, (189,1010), pygame.Rect(189,1010,63,29)))
    if s.game.extra_ball.position < 3:
        dirty_rects.append(screen.blit(bg_gi, (256,1010), pygame.Rect(256,1010,63,29)))
    if s.game.extra_ball.position < 4:
        dirty_rects.append(screen.blit(bg_gi, (326,1010), pygame.Rect(326,1010,45,29)))
    if s.game.extra_ball.position < 5:
        dirty_rects.append(screen.blit(bg_gi, (376,1010), pygame.Rect(376,1010,63,29)))
    if s.game.extra_ball.position < 6:
        dirty_rects.append(screen.blit(bg_gi, (441,1010), pygame.Rect(441,1010,63,29)))
    if s.game.extra_ball.position < 7:
        dirty_rects.append(screen.blit(bg_gi, (516,1010), pygame.Rect(516,1010,45,29)))
    if s.game.extra_ball.position < 8:
        dirty_rects.append(screen.blit(bg_gi, (565,1009), pygame.Rect(565,1009,63,29)))
    if s.game.extra_ball.position < 9:
        dirty_rects.append(screen.blit(bg_gi, (630,1009), pygame.Rect(630,1009,63,29)))

    pygame.display.update(dirty_rects)

    if num in [0,24,25,49]:
        if s.game.extra_ball.position < 1:
            p = [136,1010]
            dirty_rects.append(screen.blit(eb_number, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [1,15,26,40]:
        if s.game.extra_ball.position < 2:
            p = [189,1010]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [3,4,17,28,29,42]:
        if s.game.extra_ball.position < 3:
            p = [256,1010]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [5,18,30,43]:
        if s.game.extra_ball.position < 4:
            p = [326,1010]
            dirty_rects.append(screen.blit(eb_number, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [7,8,19,32,33,44]:
        if s.game.extra_ball.position < 5:
            p = [376,1010]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [9,10,20,34,35,45]:
        if s.game.extra_ball.position < 6:
            p = [441,1010]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [11,21,36,46]:
        if s.game.extra_ball.position < 7:
            p = [516,1010]
            dirty_rects.append(screen.blit(eb_number, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [12,22,37,47]:
        if s.game.extra_ball.position < 8:
            p = [565,1008]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [2,6,13,16,23,27,31,38,41,48]:
        if s.game.extra_ball.position < 9:
            p = [630,1009]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects) 
            return

def clear_odds(s, num):
    global screen

    dirty_rects = []

    if s.game.yellow_odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (27,797), pygame.Rect(27,797,24,50)))
    if s.game.yellow_odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (134,802), pygame.Rect(134,802,24,50)))
    if s.game.yellow_odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (183,831), pygame.Rect(183,831,24,50)))
    if s.game.yellow_odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (297,787), pygame.Rect(297,787,26,53)))
    if s.game.yellow_odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (395,823), pygame.Rect(395,823,43,53)))
    if s.game.yellow_odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (470,809), pygame.Rect(470,809,37,51)))
    if s.game.yellow_odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (541,810), pygame.Rect(541,810,33,51)))
    if s.game.yellow_odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (674,828), pygame.Rect(674,828,36,52)))

    if s.game.red_odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (19,719), pygame.Rect(19,719,32,48)))
    if s.game.red_odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (150,716), pygame.Rect(150,716,32,50)))
    if s.game.red_odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (205,725), pygame.Rect(205,725,24,50)))
    if s.game.red_odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (293,719), pygame.Rect(293,719,24,50)))
    if s.game.red_odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (378,719), pygame.Rect(378,719,34,52)))
    if s.game.red_odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (488,717), pygame.Rect(488,717,34,52)))
    if s.game.red_odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (526,721), pygame.Rect(526,721,34,52)))
    if s.game.red_odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (654,715), pygame.Rect(654,715,34,52)))


    if s.game.green_odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (20,877), pygame.Rect(20,877,24,50)))
    if s.game.green_odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (147,867), pygame.Rect(147,867,24,51)))
    if s.game.green_odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (220,874), pygame.Rect(220,874,24,51)))
    if s.game.green_odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (279,887), pygame.Rect(279,887,30,51)))
    if s.game.green_odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (389,901), pygame.Rect(389,901,37,53)))
    if s.game.green_odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (464,884), pygame.Rect(464,884,37,53)))
    if s.game.green_odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (514,867), pygame.Rect(514,867,37,53)))
    if s.game.green_odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (665,888), pygame.Rect(665,888,34,51)))

    pygame.display.update(dirty_rects)

def draw_odds_animation(s, num):
    global screen
    dirty_rects = []

    if num in [11,36]:
        if s.game.yellow_odds.position != 1:
            p = [27,797]
            dirty_rects.append(screen.blit(yellow_odds1, p))
            pygame.display.update(dirty_rects)
            return
    if num in [4,29]:
        if s.game.yellow_odds.position != 2:
            p = [134,802]
            dirty_rects.append(screen.blit(yellow_odds2, p))
            pygame.display.update(dirty_rects)
            return
    if num in [7,32]:
        if s.game.yellow_odds.position != 3:
            p = [183,831]
            dirty_rects.append(screen.blit(yellow_odds3, p))
            pygame.display.update(dirty_rects)
            return
    if num in [13,38]:
        if s.game.yellow_odds.position != 4:
            p = [297,787]
            dirty_rects.append(screen.blit(yellow_odds4, p))
            pygame.display.update(dirty_rects)
            return
    if num in [22,47]:
        if s.game.yellow_odds.position != 5:
            p = [395,823]
            dirty_rects.append(screen.blit(yellow_odds5, p))
            pygame.display.update(dirty_rects)
            return
    if num in [17,42]:
        if s.game.yellow_odds.position != 6:
            p = [470,809]
            dirty_rects.append(screen.blit(yellow_odds6, p))
            pygame.display.update(dirty_rects)
            return
    if num in [19,44]:
        if s.game.yellow_odds.position != 7:
            p = [541,810]
            dirty_rects.append(screen.blit(yellow_odds7, p))
            pygame.display.update(dirty_rects)
            return
    if num in [5,30]:
        if s.game.yellow_odds.position != 8:
            p = [674,828]
            dirty_rects.append(screen.blit(yellow_odds8, p))
            pygame.display.update(dirty_rects)
            return

    if num in [2,27]:
        if s.game.red_odds.position != 1:
            p = [19,719]
            dirty_rects.append(screen.blit(red_odds1, p))
            pygame.display.update(dirty_rects)
            return
    if num in [15,40]:
        if s.game.red_odds.position != 2:
            p = [150,716]
            dirty_rects.append(screen.blit(red_odds2, p))
            pygame.display.update(dirty_rects)
            return
    if num in [0,25]:
        if s.game.red_odds.position != 3:
            p = [205,725]
            dirty_rects.append(screen.blit(red_odds3, p))
            pygame.display.update(dirty_rects)
            return
    if num in [9,34]:
        if s.game.red_odds.position != 4:
            p = [293,719]
            dirty_rects.append(screen.blit(red_odds4, p))
            pygame.display.update(dirty_rects)
            return
    if num in [20,45]:
        if s.game.red_odds.position != 5:
            p = [378,719]
            dirty_rects.append(screen.blit(red_odds5, p))
            pygame.display.update(dirty_rects)
            return
    if num in [12,37]:
        if s.game.red_odds.position != 6:
            p = [488,717]
            dirty_rects.append(screen.blit(red_odds6, p))
            pygame.display.update(dirty_rects)
            return
    if num in [1,26]:
        if s.game.red_odds.position != 7:
            p = [526,721]
            dirty_rects.append(screen.blit(red_odds7, p))
            pygame.display.update(dirty_rects)
            return
    if num in [6,31]:
        if s.game.red_odds.position != 8:
            p = [654,715]
            dirty_rects.append(screen.blit(red_odds8, p))
            pygame.display.update(dirty_rects)
            return

    if num in [16,41]:
        if s.game.green_odds.position != 1:
            p = [20,877]
            dirty_rects.append(screen.blit(green_odds1, p))
            pygame.display.update(dirty_rects)
            return
    if num in [18,43]:
        if s.game.green_odds.position != 2:
            p = [147,867]
            dirty_rects.append(screen.blit(green_odds2, p))
            pygame.display.update(dirty_rects)
            return
    if num in [14,39]:
        if s.game.green_odds.position != 3:
            p = [220,874]
            dirty_rects.append(screen.blit(green_odds3, p))
            pygame.display.update(dirty_rects)
            return
    if num in [3,28]:
        if s.game.green_odds.position != 4:
            p = [279,887]
            dirty_rects.append(screen.blit(green_odds4, p))
            pygame.display.update(dirty_rects)
            return
    if num in [24,49]:
        if s.game.green_odds.position != 5:
            p = [389,901]
            dirty_rects.append(screen.blit(green_odds5, p))
            pygame.display.update(dirty_rects)
            return
    if num in [8,33]:
        if s.game.green_odds.position != 6:
            p = [464,884]
            dirty_rects.append(screen.blit(green_odds6, p))
            pygame.display.update(dirty_rects)
            return
    if num in [22,47]:
        if s.game.green_odds.position != 7:
            p = [514,867]
            dirty_rects.append(screen.blit(green_odds7, p))
            pygame.display.update(dirty_rects)
            return
    if num in [10,35]:
        if s.game.green_odds.position != 8:
            p = [665,888]
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
        dirty_rects.append(screen.blit(bg_gi, (180,664), pygame.Rect(180,664,46,46)))
    if s.game.magic_squares_feature.position < 6:
        dirty_rects.append(screen.blit(bg_gi, (232,664), pygame.Rect(232,664,46,46)))
    if s.game.magic_squares_feature.position < 7:
        dirty_rects.append(screen.blit(bg_gi, (280,664), pygame.Rect(280,664,46,46)))
    if s.game.magic_squares_feature.position < 8:
        dirty_rects.append(screen.blit(bg_gi, (330,664), pygame.Rect(330,664,46,46)))
    if s.game.magic_squares_feature.position < 9:
        dirty_rects.append(screen.blit(bg_gi, (378,664), pygame.Rect(378,664,46,46)))

    if s.game.selection_feature.position not in [3,4]:
        dirty_rects.append(screen.blit(bg_gi, (35,934), pygame.Rect(35,934,61,59)))
        dirty_rects.append(screen.blit(bg_gi, (568,516), pygame.Rect(568,516,129,64)))
    if s.game.selection_feature.position not in [5,6]:
        dirty_rects.append(screen.blit(bg_gi, (624,934), pygame.Rect(624,934,61,59)))
        dirty_rects.append(screen.blit(bg_gi, (568,440), pygame.Rect(568,440,129,64)))
    if s.game.magic_line_f.status == False:
        dirty_rects.append(screen.blit(bg_gi, (52,569), pygame.Rect(52,569,119,69)))
    if s.game.corners.status == False:
        dirty_rects.append(screen.blit(bg_gi, (52,408), pygame.Rect(52,408,114,68)))
    if s.game.selection_feature.position not in [7,8]:
        dirty_rects.append(screen.blit(bg_gi, (568,365), pygame.Rect(568,365,129,64)))
    if s.game.selection_feature.position != 9:
        dirty_rects.append(screen.blit(bg_gi, (568,290), pygame.Rect(568,290,129,64)))
    pygame.display.update(dirty_rects)


def draw_feature_animation(s, num):
    global screen
    dirty_rects = []

    if num in [2,12,22,27,37,47]:
        if s.game.magic_squares_feature.position < 6:
            p = [180,664]
            dirty_rects.append(screen.blit(ms_letter, p))
            p = [232,664]
            dirty_rects.append(screen.blit(ms_letter, p))
            pygame.display.update(dirty_rects)
            return
    if num in [17,23,42,48]:
        if s.game.magic_squares_feature.position < 7:
            p = [280,664]
            dirty_rects.append(screen.blit(ms_letter, p))
            pygame.display.update(dirty_rects)
            return
    if num in [5,15,24,30,40,49]:
        if s.game.magic_squares_feature.position < 8:
            p = [330,664]
            dirty_rects.append(screen.blit(ms_letter, p))
            pygame.display.update(dirty_rects)
            return
    if num in [10,20,25,35,45,50]:
        if s.game.magic_squares_feature.position < 9:
            p = [378,664]
            dirty_rects.append(screen.blit(ms_letter, p))
            pygame.display.update(dirty_rects)
            return

    if num in [8,18,33,43]:
        if s.game.selection_feature.position not in [3,4]:
            p = [35,934]
            dirty_rects.append(screen.blit(rollover, p))
            p = [568,516]
            dirty_rects.append(screen.blit(time, p))
            s.game.coils.yellowROLamp.pulse(85)
            pygame.display.update(dirty_rects)
            return
    if num in [3,13,28,38]:
        if s.game.selection_feature.position not in [5,6]:
            p = [624,934]
            dirty_rects.append(screen.blit(rollover, p))
            p = [568,440]
            dirty_rects.append(screen.blit(time, p))
            s.game.coils.redROLamp.pulse(85)
            pygame.display.update(dirty_rects)
            return
    if num in [4,14,29,39]:
        if s.game.magic_line_f.status == False:
            p = [52,569]
            dirty_rects.append(screen.blit(corners, p))
            pygame.display.update(dirty_rects)
            return
    if num in [9,19,34,44]:
        if s.game.corners.status == False:
            p = [52,408]
            dirty_rects.append(screen.blit(corners, p))
            pygame.display.update(dirty_rects)
            return
    if num in [11,21,36,46]:
        if s.game.selection_feature.position not in [7,8]:
            p = [568,365]
            dirty_rects.append(screen.blit(time, p))
            pygame.display.update(dirty_rects)
            return
    if num in [0,6,16,25,31,41]:
        if s.game.selection_feature.position != 9:
            p = [568,290]
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


