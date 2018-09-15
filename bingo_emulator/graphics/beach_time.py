
import pygame

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

meter = pygame.image.load('graphics/assets/register_cover.png').convert()
number = pygame.image.load('beach_time/assets/number.png').convert_alpha()
feature = pygame.image.load('beach_time/assets/corners.png').convert_alpha()
score = pygame.image.load('beach_time/assets/score.png').convert_alpha()
ms_letter = pygame.image.load('beach_time/assets/ms_letter.png').convert_alpha()
ms_arrow = pygame.image.load('beach_time/assets/ms_arrow.png').convert_alpha()
select_now = pygame.image.load('beach_time/assets/select_now.png').convert_alpha()
corners = pygame.image.load('beach_time/assets/corners.png').convert_alpha()
ballyhole = pygame.image.load('beach_time/assets/ballyhole.png').convert_alpha()
carryover = pygame.image.load('beach_time/assets/carryover.png').convert_alpha()
odds = pygame.image.load('beach_time/assets/odds.png').convert_alpha()
line_f = pygame.image.load('beach_time/assets/line_f.png').convert_alpha()
extra_balls = pygame.image.load('beach_time/assets/extra_ball.png').convert_alpha()
eb = pygame.image.load('beach_time/assets/eb.png').convert_alpha()
eb_number = pygame.image.load('beach_time/assets/eb_number.png').convert_alpha()
tilt = pygame.image.load('beach_time/assets/tilt.png').convert_alpha()
time = pygame.image.load('beach_time/assets/time.png').convert_alpha()
after_fifth = pygame.image.load('beach_time/assets/after_fifth.png').convert_alpha()
a0 = pygame.image.load('beach_time/assets/a0.png').convert_alpha()
a1 = pygame.image.load('beach_time/assets/a1.png').convert_alpha()
a2 = pygame.image.load('beach_time/assets/a2.png').convert_alpha()
a3 = pygame.image.load('beach_time/assets/a3.png').convert_alpha()
b0 = pygame.image.load('beach_time/assets/b0.png').convert_alpha()
b1 = pygame.image.load('beach_time/assets/b1.png').convert_alpha()
b2 = pygame.image.load('beach_time/assets/b2.png').convert_alpha()
b3 = pygame.image.load('beach_time/assets/b3.png').convert_alpha()
c0 = pygame.image.load('beach_time/assets/c0.png').convert_alpha()
c1 = pygame.image.load('beach_time/assets/c1.png').convert_alpha()
c2 = pygame.image.load('beach_time/assets/c2.png').convert_alpha()
c3 = pygame.image.load('beach_time/assets/c3.png').convert_alpha()
d0 = pygame.image.load('beach_time/assets/d0.png').convert_alpha()
d1 = pygame.image.load('beach_time/assets/d1.png').convert_alpha()
d2 = pygame.image.load('beach_time/assets/d2.png').convert_alpha()
d3 = pygame.image.load('beach_time/assets/d3.png').convert_alpha()
e0 = pygame.image.load('beach_time/assets/e0.png').convert_alpha()
e1 = pygame.image.load('beach_time/assets/e1.png').convert_alpha()
e2 = pygame.image.load('beach_time/assets/e2.png').convert_alpha()
e3 = pygame.image.load('beach_time/assets/e3.png').convert_alpha()
f0 = pygame.image.load('beach_time/assets/f0.png').convert_alpha()
rollover = pygame.image.load('beach_time/assets/ro.png').convert_alpha()
bg_menu = pygame.image.load('beach_time/assets/beach_time_menu.png')
bg_gi = pygame.image.load('beach_time/assets/beach_time_gi.png')
bg_off = pygame.image.load('beach_time/assets/beach_time_off.png')
a_1 = pygame.image.load('beach_time/assets/a-1.png').convert_alpha()
a_2 = pygame.image.load('beach_time/assets/a-2.png').convert_alpha()
a_3 = pygame.image.load('beach_time/assets/a-3.png').convert_alpha()
a_4 = pygame.image.load('beach_time/assets/a-4.png').convert_alpha()
b_1 = pygame.image.load('beach_time/assets/b-1.png').convert_alpha()
b_2 = pygame.image.load('beach_time/assets/b-2.png').convert_alpha()
b_3 = pygame.image.load('beach_time/assets/b-3.png').convert_alpha()
b_4 = pygame.image.load('beach_time/assets/b-4.png').convert_alpha()
c_1 = pygame.image.load('beach_time/assets/c-1.png').convert_alpha()
c_2 = pygame.image.load('beach_time/assets/c-2.png').convert_alpha()
c_3 = pygame.image.load('beach_time/assets/c-3.png').convert_alpha()
c_4 = pygame.image.load('beach_time/assets/c-4.png').convert_alpha()
d_1 = pygame.image.load('beach_time/assets/d-1.png').convert_alpha()
d_2 = pygame.image.load('beach_time/assets/d-2.png').convert_alpha()
d_3 = pygame.image.load('beach_time/assets/d-3.png').convert_alpha()
d_4 = pygame.image.load('beach_time/assets/d-4.png').convert_alpha()
e_1 = pygame.image.load('beach_time/assets/e-1.png').convert_alpha()
e_2 = pygame.image.load('beach_time/assets/e-2.png').convert_alpha()
e_3 = pygame.image.load('beach_time/assets/e-3.png').convert_alpha()
e_4 = pygame.image.load('beach_time/assets/e-4.png').convert_alpha()



class scorereel():
    """ Score Reels are used to count replays """
    def __init__(self, pos, image):
        self.position = pos
        self.default_y = self.position[1]
        self.image = pygame.image.load(image).convert()

reel1 = scorereel([103,280], "graphics/assets/white_reel.png")
reel10 = scorereel([84,280], "graphics/assets/white_reel.png")
reel100 = scorereel([65,280], "graphics/assets/white_reel.png")

def display(s, replays=0, menu=False):
    
    meter.set_colorkey((255,0,252))
    meter_position = [55,280]

    screen.blit(reel1.image, reel1.position)
    screen.blit(reel10.image, reel10.position)
    screen.blit(reel100.image, reel100.position)
    screen.blit(meter, meter_position)

    if s.game.square_a.position == 0:
        p = [225,330]
        screen.blit(a0, p)
    if s.game.square_a.position == 1:
        p = [225,330]
        screen.blit(a1, p)
    if s.game.square_a.position == 2:
        p = [225,330]
        screen.blit(a2, p)
    if s.game.square_a.position == 3:
        p = [225,330]
        screen.blit(a3, p)
    if s.game.square_b.position == 0:
        p = [225,447]
        screen.blit(b0, p)
    if s.game.square_b.position == 1:
        p = [225,447]
        screen.blit(b1, p)
    if s.game.square_b.position == 2:
        p = [225,447]
        screen.blit(b2, p)
    if s.game.square_b.position == 3:
        p = [225,447]
        screen.blit(b3, p)
    if s.game.square_c.position == 0:
        p = [335,330]
        screen.blit(c0, p)
    if s.game.square_c.position == 1:
        p = [335,330]
        screen.blit(c1, p)
    if s.game.square_c.position == 2:
        p = [335,330]
        screen.blit(c2, p)
    if s.game.square_c.position == 3:
        p = [335,330]
        screen.blit(c3, p)
    if s.game.square_d.position == 0:
        p = [332,443]
        screen.blit(d0, p)
    if s.game.square_d.position == 1:
        p = [332,443]
        screen.blit(d1, p)
    if s.game.square_d.position == 2:
        p = [332,443]
        screen.blit(d2, p)
    if s.game.square_d.position == 3:
        p = [332,443]
        screen.blit(d3, p)
    if s.game.square_e.position == 0:
        p = [225,555]
        screen.blit(e0, p)
    if s.game.square_e.position == 1:
        p = [225,555]
        screen.blit(e1, p)
    if s.game.square_e.position == 2:
        p = [225,555]
        screen.blit(e2, p)
    if s.game.square_e.position == 3:
        p = [225,555]
        screen.blit(e3, p)
    if s.game.line_f.position == 0 or s.game.line_f.position == 2:
        p = [438,270]
        screen.blit(f0, p)
    elif s.game.line_f.position == 1:
        p = [438,325]
        screen.blit(f0, p)
    elif s.game.line_f.position == 3:
        p = [438,214]
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
                    p = [282,328]
                    screen.blit(number, p)
                elif s.game.square_a.position == 1:
                    p = [282,386]
                    screen.blit(number, p)
                elif s.game.square_a.position == 2:
                    p = [227,386]
                    screen.blit(number, p)
                else:
                    p = [227,328]
                    screen.blit(number, p)
            if 2 in s.holes:
                if s.game.square_c.position == 0:
                    p = [336,328]
                    screen.blit(number, p)
                elif s.game.square_c.position == 1:
                    p = [390,328]
                    screen.blit(number, p)
                elif s.game.square_c.position == 2:
                    p = [390,387]
                    screen.blit(number, p)
                else:
                    p = [336,387]
                    screen.blit(number, p)
            if 3 in s.holes:
                if s.game.square_e.position == 0:
                    p = [388,560]
                    screen.blit(number, p)
                elif s.game.square_e.position == 1:
                    p = [226,560]
                    screen.blit(number, p)
                elif s.game.square_e.position == 2:
                    p = [280,560]
                    screen.blit(number, p)
                else:
                    p = [334,560]
                    screen.blit(number, p)
            if 4 in s.holes:
                if s.game.square_a.position == 0:
                    p = [227,386]
                    screen.blit(number, p)
                elif s.game.square_a.position == 1:
                    p = [227,328]
                    screen.blit(number, p)
                elif s.game.square_a.position == 2:
                    p = [282,328]
                    screen.blit(number, p)
                else:
                    p = [282,386]
                    screen.blit(number, p)
            if 5 in s.holes:
                if s.game.square_d.position == 0:
                    p = [337,504]
                    screen.blit(number, p)
                elif s.game.square_d.position == 1:
                    p = [337,446]
                    screen.blit(number, p)
                elif s.game.square_d.position == 2:
                    p = [391,446]
                    screen.blit(number, p)
                else:
                    p = [391,503]
                    screen.blit(number, p)
            if 6 in s.holes:
                if s.game.square_b.position == 0:
                    p = [230,502]
                    screen.blit(number, p)
                elif s.game.square_b.position == 1:
                    p = [230,445]
                    screen.blit(number, p)
                elif s.game.square_b.position == 2:
                    p = [281,446]
                    screen.blit(number, p)
                else:
                    p = [282,503]
                    screen.blit(number, p)
            if 7 in s.holes:
                if s.game.square_c.position == 0:
                    p = [338,388]
                    screen.blit(number, p)
                elif s.game.square_c.position == 1:
                    p = [338,328]
                    screen.blit(number, p)
                elif s.game.square_c.position == 2:
                    p = [391,328]
                    screen.blit(number, p)
                else:
                    p = [391,387]
                    screen.blit(number, p)
            if 8 in s.holes:
                if s.game.square_e.position == 0:
                    p = [282,562]
                    screen.blit(number, p)
                elif s.game.square_e.position == 1:
                    p = [336,562]
                    screen.blit(number, p)
                elif s.game.square_e.position == 2:
                    p = [390,562]
                    screen.blit(number, p)
                else:
                    p = [230,562]
                    screen.blit(number, p)
            if 9 in s.holes:
                if s.game.square_a.position == 0:
                    p = [228,329]
                    screen.blit(number, p)
                elif s.game.square_a.position == 1:
                    p = [283,329]
                    screen.blit(number, p)
                elif s.game.square_a.position == 2:
                    p = [282,388]
                    screen.blit(number, p)
                else:
                    p = [229,388]
                    screen.blit(number, p)
            if 10 in s.holes:
                if s.game.line_f.position == 0 or s.game.line_f.position == 2:
                    p = [446,562]
                    screen.blit(number, p)
                elif s.game.line_f.position == 1:
                    p = [446,330]
                    screen.blit(number, p)
                else:
                    p = [446,502]
                    screen.blit(number, p)
            if 11 in s.holes:
                if s.game.square_c.position == 0:
                    p = [392,329]
                    screen.blit(number, p)
                elif s.game.square_c.position == 1:
                    p = [391,387]
                    screen.blit(number, p)
                elif s.game.square_c.position == 2:
                    p = [338,388]
                    screen.blit(number, p)
                else:
                    p = [338,330]
                    screen.blit(number, p)
            if 12 in s.holes:
                if s.game.square_e.position == 0:
                    p = [230,562]
                    screen.blit(number, p)
                elif s.game.square_e.position == 1:
                    p = [283,562]
                    screen.blit(number, p)
                elif s.game.square_e.position == 2:
                    p = [336,562]
                    screen.blit(number, p)
                else:
                    p = [390,562]
                    screen.blit(number, p)
            if 13 in s.holes:
                if s.game.square_d.position == 0:
                    p = [390,447]
                    screen.blit(number, p)
                elif s.game.square_d.position == 1:
                    p = [390,504]
                    screen.blit(number, p)
                elif s.game.square_d.position == 2:
                    p = [338,504]
                    screen.blit(number, p)
                else:
                    p = [338,446]
                    screen.blit(number, p)
            if 14 in s.holes:
                if s.game.square_e.position == 0:
                    p = [336,562]
                    screen.blit(number, p)
                elif s.game.square_e.position == 1:
                    p = [391,562]
                    screen.blit(number, p)
                elif s.game.square_e.position == 2:
                    p = [230,562]
                    screen.blit(number, p)
                else:
                    p = [283,563]
                    screen.blit(number, p)
            if 15 in s.holes:
                if s.game.line_f.position == 0 or s.game.line_f.position == 2:
                    p = [446,331]
                    screen.blit(number, p)
                if s.game.line_f.position == 1:
                    p = [446,388]
                    screen.blit(number, p)
                if s.game.line_f.position == 3:
                    p = [446,562]
                    screen.blit(number, p)
            if 16 in s.holes:
                if s.game.square_d.position == 0:
                    p = [337,446]
                    screen.blit(number, p)
                elif s.game.square_d.position == 1:
                    p = [392,446]
                    screen.blit(number, p)
                elif s.game.square_d.position == 2:
                    p = [390,504]
                    screen.blit(number, p)
                else:
                    p = [338,504]
                    screen.blit(number, p)
            if 17 in s.holes:
                if s.game.line_f.position == 0 or s.game.line_f.position == 2:
                    p = [445,446]
                    screen.blit(number, p)
                elif s.game.line_f.position == 1:
                    p = [445,502]
                    screen.blit(number, p)
                elif s.game.line_f.position == 3:
                    p = [445,388]
                    screen.blit(number, p)
            if 18 in s.holes:
                if s.game.line_f.position == 0 or s.game.line_f.position == 2:
                    p = [446,388]
                    screen.blit(number, p)
                elif s.game.line_f.position == 1:
                    p = [445,446]
                    screen.blit(number, p)
                elif s.game.line_f.position == 3:
                    p = [446,329]
                    screen.blit(number, p)
            if 19 in s.holes:
                if s.game.square_a.position == 0:
                    p = [283,386]
                    screen.blit(number, p)
                elif s.game.square_a.position == 1:
                    p = [230,388]
                    screen.blit(number, p)
                elif s.game.square_a.position == 2:
                    p = [230,330]
                    screen.blit(number, p)
                else:
                    p = [283,330]
                    screen.blit(number, p)
            if 20 in s.holes:
                if s.game.line_f.position == 0 or s.game.line_f.position == 2:
                    p = [446,503]
                    screen.blit(number, p)
                elif s.game.line_f.position == 1:
                    p = [446,562]
                    screen.blit(number, p)
                elif s.game.line_f.position == 3:
                    p = [446,446]
                    screen.blit(number, p)
            if 21 in s.holes:
                if s.game.square_d.position == 0:
                    p = [390,504]
                    screen.blit(number, p)
                elif s.game.square_d.position == 1:
                    p = [337,505]
                    screen.blit(number, p)
                elif s.game.square_d.position == 2:
                    p = [337,446]
                    screen.blit(number, p)
                else:
                    p = [391,446]
                    screen.blit(number, p)
            if 22 in s.holes:
                if s.game.square_c.position == 0:
                    p = [392,388]
                    screen.blit(number, p)
                elif s.game.square_c.position == 1:
                    p = [338,388]
                    screen.blit(number, p)
                elif s.game.square_c.position == 2:
                    p = [338,330]
                    screen.blit(number, p)
                else:
                    p = [392,329]
                    screen.blit(number, p)
            if 23 in s.holes:
                if s.game.square_b.position == 0:
                    p = [282,504]
                    screen.blit(number, p)
                elif s.game.square_b.position == 1:
                    p = [229,504]
                    screen.blit(number, p)
                elif s.game.square_b.position == 2:
                    p = [228,446]
                    screen.blit(number, p)
                else:
                    p = [282,446]
                    screen.blit(number, p)
            if 24 in s.holes:
                if s.game.square_b.position == 0:
                    p = [282,446]
                    screen.blit(number, p)
                elif s.game.square_b.position == 1:
                    p = [282,504]
                    screen.blit(number, p)
                elif s.game.square_b.position == 2:
                    p = [229,504]
                    screen.blit(number, p)
                else:
                    p = [228,446]
                    screen.blit(number, p)
            if 25 in s.holes:
                if s.game.square_b.position == 0:
                    p = [228,446]
                    screen.blit(number, p)
                elif s.game.square_b.position == 1:
                    p = [282,446]
                    screen.blit(number, p)
                elif s.game.square_b.position == 2:
                    p = [282,504]
                    screen.blit(number, p)
                else:
                    p = [229,504]
                    screen.blit(number, p)


    if s.game.magic_squares_feature.position == 1:
        p = [20,662]
        screen.blit(ms_arrow, p)
    if s.game.magic_squares_feature.position == 2:
        p = [62,662]
        screen.blit(ms_arrow, p)
    if s.game.magic_squares_feature.position == 3:
        p = [102,662]
        screen.blit(ms_arrow, p)
    if s.game.magic_squares_feature.position == 4:
        p = [143,662]
        screen.blit(ms_arrow, p)
    if s.game.magic_squares_feature.position >= 5:
        p = [204,658]
        screen.blit(ms_letter, p)
    if s.game.magic_squares_feature.position >= 6:
        p = [243,658]
        screen.blit(ms_letter, p)
    if s.game.magic_squares_feature.position >= 7:
        p = [283,658]
        screen.blit(ms_letter, p)
    if s.game.magic_squares_feature.position >= 8:
        p = [321,658]
        screen.blit(ms_letter, p)
    if s.game.magic_squares_feature.position == 9:
        p = [360,658]
        screen.blit(ms_letter, p)

    sf = s.game.selection_feature.position 
    if s.game.magic_squares_feature.position >= 5 and sf <= 6:
        p = [580,552]
        screen.blit(time, p)
    if sf <= 6:
        if s.game.magic_squares_feature.position >= 5:
            if s.game.ball_count.position == 3:
                s.cancel_delayed(name="blink")
                blink([s,1,1])
            else:
                s.cancel_delayed(name="blink")
    if sf == 3 or sf == 4:
        if s.game.magic_squares_feature.position >= 5:
            p = [580,552]
            screen.blit(time, p)
            p = [568,502]
            screen.blit(rollover, p)
    if sf == 5 or sf == 6:
        if s.game.magic_squares_feature.position >= 5:
            p = [580,552]
            screen.blit(time, p)
            p = [568,452]
            screen.blit(rollover, p)
    if sf == 7 or sf == 8:
        if s.game.magic_squares_feature.position >= 5:
            p = [581,368]
            screen.blit(time, p)
        if s.game.ball_count.position == 4:
            s.cancel_delayed(name="blink")
            blink([s,1,1])
        else:
            s.cancel_delayed(name="blink")
    if sf == 9:
        if s.game.magic_squares_feature.position >= 5:
            p = [570,250]
            screen.blit(after_fifth, p)
        if s.game.ball_count.position == 5:
            s.cancel_delayed(name="blink")
            blink([s,1,1])
        else:
            s.cancel_delayed(name="blink")

    if s.game.corners.status == True:
        p = [52,370]
        screen.blit(corners, p)
    if s.game.ballyhole.status == True:
        p = [32,448]
        screen.blit(ballyhole, p)
        if 16 in s.holes:
            p = [32,489]
            screen.blit(carryover, p)
    if s.game.magic_line_f.status == True:
        p = [52,589]
        screen.blit(line_f, p)

    if s.game.extra_ball.position >= 1:
        p = [136,1037]
        screen.blit(eb_number, p)
    if s.game.extra_ball.position >= 2:
        p = [189,1037]
        screen.blit(eb, p)
    if s.game.extra_ball.position >= 3:
        p = [256,1037]
        screen.blit(eb, p)
    if s.game.extra_ball.position >= 4:
        p = [326,1037]
        screen.blit(eb_number, p)
    if s.game.extra_ball.position >= 5:
        p = [376,1037]
        screen.blit(eb, p)
    if s.game.extra_ball.position >= 6:
        p = [441,1037]
        screen.blit(eb, p)
    if s.game.extra_ball.position >= 7:
        p = [516,1037]
        screen.blit(eb_number, p)
    if s.game.extra_ball.position >= 8:
        p = [565,1035]
        screen.blit(eb, p)
    if s.game.extra_ball.position == 9:
        p = [630,1035]
        screen.blit(eb, p)

    if s.game.eb_play.status == True:
        p = [25,1037]
        screen.blit(extra_balls, p)

    if s.game.red_odds.position == 1:
        p = [103,750]
        screen.blit(odds, p)
    elif s.game.red_odds.position == 2:
        p = [176,750]
        screen.blit(odds, p)
    elif s.game.red_odds.position == 3:
        p = [255,750]
        screen.blit(odds, p)
    elif s.game.red_odds.position == 4:
        p = [338,750]
        screen.blit(odds, p)
    elif s.game.red_odds.position == 5:
        p = [402,750]
        screen.blit(odds, p)
    elif s.game.red_odds.position == 6:
        p = [457,750]
        screen.blit(odds, p)
    elif s.game.red_odds.position == 7:
        p = [510,750]
        screen.blit(odds, p)
    elif s.game.red_odds.position == 8:
        p = [565,750]
        screen.blit(odds, p)

    if s.game.yellow_odds.position == 1:
        p = [103,828]
        screen.blit(odds, p)
    elif s.game.yellow_odds.position == 2:
        p = [176,828]
        screen.blit(odds, p)
    elif s.game.yellow_odds.position == 3:
        p = [255,828]
        screen.blit(odds, p)
    elif s.game.yellow_odds.position == 4:
        p = [338,828]
        screen.blit(odds, p)
    elif s.game.yellow_odds.position == 5:
        p = [402,828]
        screen.blit(odds, p)
    elif s.game.yellow_odds.position == 6:
        p = [457,828]
        screen.blit(odds, p)
    elif s.game.yellow_odds.position == 7:
        p = [510,828]
        screen.blit(odds, p)
    elif s.game.yellow_odds.position == 8:
        p = [565,828]
        screen.blit(odds, p)

    if s.game.green_odds.position == 1:
        p = [103,906]
        screen.blit(odds, p)
    elif s.game.green_odds.position == 2:
        p = [176,906]
        screen.blit(odds, p)
    elif s.game.green_odds.position == 3:
        p = [255,906]
        screen.blit(odds, p)
    elif s.game.green_odds.position == 4:
        p = [338,906]
        screen.blit(odds, p)
    elif s.game.green_odds.position == 5:
        p = [402,906]
        screen.blit(odds, p)
    elif s.game.green_odds.position == 6:
        p = [457,906]
        screen.blit(odds, p)
    elif s.game.green_odds.position == 7:
        p = [510,906]
        screen.blit(odds, p)
    elif s.game.green_odds.position == 8:
        p = [565,906]
        screen.blit(odds, p)

    if s.game.score_feature.position == 1:
        p = [22,706]
        screen.blit(ms_arrow, p)
    if s.game.score_feature.position == 2:
        p = [63,706]
        screen.blit(ms_arrow, p)
    if s.game.score_feature.position == 3:
        p = [104,706]
        screen.blit(ms_arrow, p)
    if s.game.score_feature.position == 4:
        p = [148,708]
        screen.blit(score, p)
        if s.game.ball_count.position == 2:
            s.cancel_delayed(name="blink_score")
            blink_score([s,1,1])            
        else:
            if s.game.ball_count.position > 2:
                s.cancel_delayed(name="blink_score")
    if s.game.score_feature.position == 5:
        p = [236,708]
        screen.blit(score, p)
        if s.game.ball_count.position == 3:
            s.cancel_delayed(name="blink_score")
            blink_score([s,1,1])            
        else:
            if s.game.ball_count.position > 3:
                s.cancel_delayed(name="blink_score")
    if s.game.score_feature.position == 6:
        p = [326,708]
        screen.blit(score, p)
        if s.game.ball_count.position == 4:
            s.cancel_delayed(name="blink_score")
            blink_score([s,1,1])            
        else:
            if s.game.ball_count.position > 4:
                s.cancel_delayed(name="blink_score")

    if s.game.tilt.status == True:
        tilt_position = [452,217]
        screen.blit(tilt, tilt_position)

    pygame.display.update()

def blink(args):
    dirty_rects = []
    s = args[0]
    b = args[1]
    sl = args[2]

    if b == 0:
        if sl == 1:
            p = [550,663]
            dirty_rects.append(screen.blit(select_now, p))
        pygame.display.update(dirty_rects)
    else:
        dirty_rects.append(screen.blit(bg_gi, (550,663), pygame.Rect(550,663,152,40)))
        pygame.display.update(dirty_rects)
    b = not b

    args = [s,b,sl]

    s.delay(name="blink", delay=0.1, handler=blink, param=args)

def blink_score(args):
    dirty_rects = []
    s = args[0]
    b = args[1]
    sn = args[2]

    if b == 0:
        if sn == 1:
            p = [549,706]
            dirty_rects.append(screen.blit(select_now, p))
        pygame.display.update(dirty_rects)
    else:
        dirty_rects.append(screen.blit(bg_gi, (549,706), pygame.Rect(549,706,152,40)))
        pygame.display.update(dirty_rects)
    b = not b

    args = [s,b,sn]

    s.delay(name="blink_score", delay=0.1, handler=blink_score, param=args)

def line_animation(args):
    dirty_rects = []
    s = args[0]
    num = args[1]
    line = args[2]

    if line == 1:
        if s.game.line_f.position == 0:
            dirty_rects.append(screen.blit(f0, (438, 214 - num)))
        elif s.game.line_f.position == 1:
            dirty_rects.append(screen.blit(f0, (438, 270 - num)))
        elif s.game.line_f.position == 2:
            dirty_rects.append(screen.blit(f0, (438, 325 + num)))
        elif s.game.line_f.position == 3:
            dirty_rects.append(screen.blit(f0, (438, 270 + num)))

        if (s.game.anti_cheat.status == True):
            dirty_rects.append(screen.blit(bg_gi, (438,214), pygame.Rect(438,214,58,706)))
        else:
            dirty_rects.append(screen.blit(bg_off, (438,214), pygame.Rect(438,214,58,706)))
        
        if s.game.yellow_odds.position == 5:
            p = [402,828]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],55,74)))
            dirty_rects.append(screen.blit(odds, p))
        elif s.game.yellow_odds.position == 6:
            p = [457,828]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],55,74)))
            dirty_rects.append(screen.blit(odds, p))
        
        if s.game.red_odds.position == 5:
            p = [402,750]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],55,74)))
            dirty_rects.append(screen.blit(odds, p))
        elif s.game.red_odds.position == 6:
            p = [457,750]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],55,74)))
            dirty_rects.append(screen.blit(odds, p))
     
        if s.game.green_odds.position == 5:
            p = [402,906]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],55,74)))
            dirty_rects.append(screen.blit(odds, p))
        elif s.game.green_odds.position == 6:
            p = [457,906]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],55,74)))
            dirty_rects.append(screen.blit(odds, p))
     
    pygame.display.update(dirty_rects)




def squarea_animation(args):
    dirty_rects = []
    s = args[0]
    num = args[1]
    square = args[2]
    
    if square == 1:
        p = [225,330]
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
        dirty_rects.append(screen.blit(topleft, (244  - num - 20, 334)))
        dirty_rects.append(screen.blit(topright, (281, 341 - num - 10)))
        dirty_rects.append(screen.blit(bottomright, (275  + num + 15, 385)))
        dirty_rects.append(screen.blit(bottomleft, (227, 386 + num + 5)))

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
        p = [225,447]
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
        dirty_rects.append(screen.blit(topleft, (243 - num - 20, 451)))
        dirty_rects.append(screen.blit(topright, (281, 455 - num - 9)))
        dirty_rects.append(screen.blit(bottomright, (281  + num + 10, 503)))
        dirty_rects.append(screen.blit(bottomleft, (227, 505 + num + 8)))
    
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
        p = [335,330]
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
        dirty_rects.append(screen.blit(topleft, (346  - num - 10, 333)))
        dirty_rects.append(screen.blit(topright, (390, 334 - num - 5)))
        dirty_rects.append(screen.blit(bottomright, (382  + num + 15, 384)))
        dirty_rects.append(screen.blit(bottomleft, (335, 384 + num + 6)))
    
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
    
    p = [332,443]
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
        dirty_rects.append(screen.blit(topleft, (341 - num - 10, 447)))
        dirty_rects.append(screen.blit(topright, (387, 455 - num - 13)))
        dirty_rects.append(screen.blit(bottomright, (364  + num + 29, 501)))
        dirty_rects.append(screen.blit(bottomleft, (337, 500 + num + 12)))
    
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
    
    p = [225,555]
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
    dirty_rects.append(screen.blit(topleft, (233 - num - 10, 562)))
    if num > -40:
        dirty_rects.append(screen.blit(topright, (279, 560 - num)))
    else:
        dirty_rects.append(screen.blit(topright, (334, 618 + num)))
    dirty_rects.append(screen.blit(bottomleft, (334 - num - 10, 560)))
    if num > -40:
        dirty_rects.append(screen.blit(bottomright, (389, 562 - num)))
    else:
        dirty_rects.append(screen.blit(bottomright, (225, 618 + num)))
    
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
        dirty_rects.append(screen.blit(bg_gi, (136,1037), pygame.Rect(136,1037,47,31)))
    if s.game.extra_ball.position < 2:
        dirty_rects.append(screen.blit(bg_gi, (189,1037), pygame.Rect(189,1037,64,32)))
    if s.game.extra_ball.position < 3:
        dirty_rects.append(screen.blit(bg_gi, (256,1037), pygame.Rect(256,1037,64,32)))
    if s.game.extra_ball.position < 4:
        dirty_rects.append(screen.blit(bg_gi, (326,1037), pygame.Rect(326,1037,47,31)))
    if s.game.extra_ball.position < 5:
        dirty_rects.append(screen.blit(bg_gi, (376,1037), pygame.Rect(376,1037,64,32)))
    if s.game.extra_ball.position < 6:
        dirty_rects.append(screen.blit(bg_gi, (441,1037), pygame.Rect(441,1037,64,32)))
    if s.game.extra_ball.position < 7:
        dirty_rects.append(screen.blit(bg_gi, (516,1037), pygame.Rect(516,1037,47,31)))
    if s.game.extra_ball.position < 8:
        dirty_rects.append(screen.blit(bg_gi, (565,1035), pygame.Rect(565,1035,64,32)))
    if s.game.extra_ball.position < 9:
        dirty_rects.append(screen.blit(bg_gi, (630,1035), pygame.Rect(630,1035,64,32)))
    pygame.display.update(dirty_rects)

    if num in [0,25,14,49]:
        if s.game.extra_ball.position < 1:
            p = [136,1037]
            dirty_rects.append(screen.blit(eb_number, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [39,1,26,15]:
        if s.game.extra_ball.position < 2:
            p = [189,1037]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [3,4,17,28,29,40]:
        if s.game.extra_ball.position < 3:
            p = [256,1037]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [5,18,30,43]:
        if s.game.extra_ball.position < 4:
            p = [326,1037]
            dirty_rects.append(screen.blit(eb_number, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [7,8,19,32,33,44]:
        if s.game.extra_ball.position < 5:
            p = [376,1037]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [9,10,20,34,35,45]:
        if s.game.extra_ball.position < 6:
            p = [441,1037]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [11,21,36,46]:
        if s.game.extra_ball.position < 7:
            p = [516,1037]
            dirty_rects.append(screen.blit(eb_number, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [12,22,37,47]:
        if s.game.extra_ball.position < 8:
            p = [565,1035]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [2,6,13,16,23,27,31,38,41,48]:
        if s.game.extra_ball.position < 9:
            p = [630,1035]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return

def clear_odds(s, num):
    global screen

    dirty_rects = []


    if s.game.yellow_odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (103,828), pygame.Rect(103,828,55,74)))
    if s.game.yellow_odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (176,828), pygame.Rect(176,828,55,74)))
    if s.game.yellow_odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (255,828), pygame.Rect(255,828,55,74)))
    if s.game.yellow_odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (338,828), pygame.Rect(338,828,55,74)))
    if s.game.yellow_odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (402,828), pygame.Rect(402,828,55,74)))
    if s.game.yellow_odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (457,828), pygame.Rect(457,828,55,74)))
    if s.game.yellow_odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (510,828), pygame.Rect(510,828,55,74)))
    if s.game.yellow_odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (565,828), pygame.Rect(565,828,55,74)))

    if s.game.red_odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (103,750), pygame.Rect(103,750,55,74)))
    if s.game.red_odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (176,750), pygame.Rect(176,750,55,74)))
    if s.game.red_odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (255,750), pygame.Rect(255,750,55,74)))
    if s.game.red_odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (338,750), pygame.Rect(338,750,55,74)))
    if s.game.red_odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (402,750), pygame.Rect(402,750,55,74)))
    if s.game.red_odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (457,750), pygame.Rect(457,750,55,74)))
    if s.game.red_odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (510,750), pygame.Rect(510,750,55,74)))
    if s.game.red_odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (565,750), pygame.Rect(565,750,55,74)))

    if s.game.green_odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (103,906), pygame.Rect(103,906,55,74)))
    if s.game.green_odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (176,906), pygame.Rect(176,906,55,74)))
    if s.game.green_odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (255,906), pygame.Rect(255,906,55,74)))
    if s.game.green_odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (338,906), pygame.Rect(338,906,55,74)))
    if s.game.green_odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (402,906), pygame.Rect(402,906,55,74)))
    if s.game.green_odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (457,906), pygame.Rect(457,906,55,74)))
    if s.game.green_odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (510,906), pygame.Rect(510,906,55,74)))
    if s.game.green_odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (565,906), pygame.Rect(565,906,55,74)))


    pygame.display.update(dirty_rects)

def draw_odds_animation(s, num):
    global screen
    dirty_rects = []

    if num in [10,35]:
        if s.game.yellow_odds.position != 1:
            p = [103,828]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [4,29]:
        if s.game.yellow_odds.position != 2:
            p = [176,828]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [7,32]:
        if s.game.yellow_odds.position != 3:
            p = [255,828]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [13,38]:
        if s.game.yellow_odds.position != 4:
            p = [338,828]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [23,48]:
        if s.game.yellow_odds.position != 5:
            p = [402,828]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [17,42]:
        if s.game.yellow_odds.position != 6:
            p = [457,828]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [19,44]:
        if s.game.yellow_odds.position != 7:
            p = [510,828]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [5,30]:
        if s.game.yellow_odds.position != 8:
            p = [565,828]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return

    if num in [2,27]:
        if s.game.red_odds.position != 1:
            p = [103,750]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [15,40]:
        if s.game.red_odds.position != 2:
            p = [176,750]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [0,25]:
        if s.game.red_odds.position != 3:
            p = [255,750]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [9,34]:
        if s.game.red_odds.position != 4:
            p = [338,750]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [20,45]:
        if s.game.red_odds.position != 5:
            p = [402,750]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [12,37]:
        if s.game.red_odds.position != 6:
            p = [457,750]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [1,26]:
        if s.game.red_odds.position != 7:
            p = [510,750]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [6,31]:
        if s.game.red_odds.position != 8:
            p = [565,750]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return

    if num in [16,41]:
        if s.game.green_odds.position != 1:
            p = [103,906]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [18,43]:
        if s.game.green_odds.position != 2:
            p = [176,906]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [14,39]:
        if s.game.green_odds.position != 3:
            p = [255,906]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [3,28]:
        if s.game.green_odds.position != 4:
            p = [338,906]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [24,49]:
        if s.game.green_odds.position != 5:
            p = [402,906]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [8,33]:
        if s.game.green_odds.position != 6:
            p = [457,906]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [21,46]:
        if s.game.green_odds.position != 7:
            p = [510,906]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [11,36]:
        if s.game.green_odds.position != 8:
            p = [565,906]
            dirty_rects.append(screen.blit(odds, p))
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

    if s.game.magic_squares_feature.position < 6:
        dirty_rects.append(screen.blit(bg_gi, (204,658), pygame.Rect(204,658,33,48)))
        dirty_rects.append(screen.blit(bg_gi, (243,658), pygame.Rect(243,658,33,48)))
    if s.game.magic_squares_feature.position < 7:
        dirty_rects.append(screen.blit(bg_gi, (283,658), pygame.Rect(283,658,33,48)))
    if s.game.magic_squares_feature.position < 8:
        dirty_rects.append(screen.blit(bg_gi, (321,658), pygame.Rect(321,658,33,48)))
    if s.game.magic_squares_feature.position < 9:
        dirty_rects.append(screen.blit(bg_gi, (360,658), pygame.Rect(360,658,33,48)))
    if s.game.magic_line_f.status == False:
        dirty_rects.append(screen.blit(bg_gi, (52,589), pygame.Rect(52,589,79,45)))
    sf = s.game.selection_feature.position 
    if sf < 3 or s.game.magic_squares_feature.position < 5:
        dirty_rects.append(screen.blit(bg_gi, (568,502), pygame.Rect(568,502,120,48)))
    if sf < 5 or s.game.magic_squares_feature.position < 5:
        dirty_rects.append(screen.blit(bg_gi, (568,452), pygame.Rect(568,452,120,48)))
    if sf < 7:
        dirty_rects.append(screen.blit(bg_gi, (581,368), pygame.Rect(581,368,94,84)))
    if sf < 9:
        dirty_rects.append(screen.blit(bg_gi, (570,250), pygame.Rect(570,250,109,118)))
    if s.game.corners.status == False:
        dirty_rects.append(screen.blit(bg_gi, (52,370), pygame.Rect(52,370,82,77)))
    if s.game.ballyhole.status == False:
        dirty_rects.append(screen.blit(bg_gi, (32,448), pygame.Rect(32,448,121,41)))
    if s.game.score_feature.position < 4:
        dirty_rects.append(screen.blit(bg_gi, (148,708), pygame.Rect(148,708,86,37)))
    if s.game.score_feature.position < 5:
        dirty_rects.append(screen.blit(bg_gi, (236,708), pygame.Rect(236,708,86,37)))
    if s.game.score_feature.position < 6:
        dirty_rects.append(screen.blit(bg_gi, (326,708), pygame.Rect(326,708,86,37)))

    pygame.display.update(dirty_rects)


def draw_feature_animation(s, num):
    global screen
    dirty_rects = []
    

    if num in [2,27]:
        if s.game.magic_squares_feature.position < 5:
            p = [204,658]
            dirty_rects.append(screen.blit(ms_letter, p))
            p = [243,658]
            dirty_rects.append(screen.blit(ms_letter, p))
            pygame.display.update(dirty_rects)
            return
    if num in [3,17,28,42]:
        if s.game.magic_squares_feature.position < 7:
            p = [283,658]
            dirty_rects.append(screen.blit(ms_letter, p))
            pygame.display.update(dirty_rects)
            return
    if num in [4,18,29,43]:
        if s.game.magic_squares_feature.position < 8:
            p = [321,658]
            dirty_rects.append(screen.blit(ms_letter, p))
            pygame.display.update(dirty_rects)
            return
    if num in [5,19,30,44]:
        if s.game.magic_squares_feature.position < 9:
            p = [360,658]
            dirty_rects.append(screen.blit(ms_letter, p))
            pygame.display.update(dirty_rects)
            return
    if num in [13,38]:
        if s.game.magic_line_f.status == False:
            p = [52,589]
            dirty_rects.append(screen.blit(line_f, p))
            pygame.display.update(dirty_rects)
            return
    sf = s.game.selection_feature.position
    if num in [8,22,33,47]:
        if sf < 3 or s.game.magic_squares_feature.position < 5:
            s.game.coils.yellowROLamp.pulse(85)
            p = [568,452]
            dirty_rects.append(screen.blit(rollover, p))
            pygame.display.update(dirty_rects)
            return
    if num in [9,23,34,48]:
        if sf < 5 or s.game.magic_squares_feature.position < 5:
            s.game.coils.redROLamp.pulse(85)
            p = [568,452]
            dirty_rects.append(screen.blit(rollover, p))
            pygame.display.update(dirty_rects)
            return
    if num in [7,21,32,46]:
        if s.game.ballyhole.status == False:
            p = [32,448]
            dirty_rects.append(screen.blit(ballyhole, p))
            pygame.display.update(dirty_rects)
            return
    if num in [6,20,31,45]:
        if s.game.corners.status == False:
            p = [52,370]
            dirty_rects.append(screen.blit(corners, p))
            pygame.display.update(dirty_rects)
            return
    if num in [10,24,35,49]:
        if sf < 7:
            p = [581,368]
            dirty_rects.append(screen.blit(time, p))
            pygame.display.update(dirty_rects)
            return
    if num in [11,36]:
        if sf < 9:
            p = [570,250]
            dirty_rects.append(screen.blit(after_fifth, p))
            pygame.display.update(dirty_rects)
            return
    if num in [1,15,26,40]:
        if s.game.score_feature.position < 4:
            p = [148,708]
            dirty_rects.append(screen.blit(score, p))
            pygame.display.update(dirty_rects)
            return
    if num in [12,37]:
        if s.game.score_feature.position < 5:
            p = [236,708]
            dirty_rects.append(screen.blit(score, p))
            pygame.display.update(dirty_rects)
            return
    if num in [14,39]:
        if s.game.score_feature.position < 6:
            p = [326,708]
            dirty_rects.append(screen.blit(score, p))
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

