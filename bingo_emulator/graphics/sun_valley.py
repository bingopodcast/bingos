
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
        backglass = pygame.image.load('sun_valley/assets/sun_valley_menu.png')
    else:
        if (s.game.anti_cheat.status == True):
            backglass = pygame.image.load('sun_valley/assets/sun_valley_gi.png')
        else:
            backglass = pygame.image.load('sun_valley/assets/sun_valley_off.png')
    backglass = pygame.transform.scale(backglass, (720, 1280))
    
    screen.blit(backglass, backglass_position)


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
                elif s.game.square_c.position == 2:
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
        if s.game.ball_count.position == 3:
            p = [556,667]
            screen.blit(select_now, p)
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
            p = [556,667]
            screen.blit(select_now, p)
    if sf == 9:
        p = [535,310]
        screen.blit(s_arrow, p)
        if s.game.magic_squares_feature.position >= 5:
            p = [568,290]
            screen.blit(time, p)
        if s.game.ball_count.position == 5:
            p = [556,667]
            screen.blit(select_now, p)

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

    pygame.display.flip()
    pygame.display.update()

def eb_animation(num):
    global screen

    if num == 9:
        p = [136,1010]
        screen.blit(eb_number, p)
        pygame.display.update()
    if num == 8:
        p = [189,1010]
        screen.blit(eb, p)
        pygame.display.update()
    if num == 7:
        p = [256,1010]
        screen.blit(eb, p)
        pygame.display.update()
    if num == 6:
        p = [326,1010]
        screen.blit(eb_number, p)
        pygame.display.update()
    if num == 5:
        p = [376,1010]
        screen.blit(eb, p)
        pygame.display.update()
    if num == 4:
        p = [441,1010]
        screen.blit(eb, p)
        pygame.display.update()
    if num == 3:
        p = [516,1010]
        screen.blit(eb_number, p)
        pygame.display.update()
    if num == 2:
        p = [565,1008]
        screen.blit(eb, p)
        pygame.display.update()
    if num == 1:
        p = [630,1009]
        screen.blit(eb, p)
        pygame.display.update()


def feature_animation(num):
    global screen
    if num == 6:
        p = [52,408]
        screen.blit(corners, p)
        pygame.display.update()

    if num == 3:
        p = [378,664]
        screen.blit(ms_letter, p)
        pygame.display.update()
   

def odds_animation(num):
    global screen

