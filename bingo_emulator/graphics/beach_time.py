
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
        backglass = pygame.image.load('beach_time/assets/beach_time_menu.png')
    else:
        if (s.game.anti_cheat.status == True):
            backglass = pygame.image.load('beach_time/assets/beach_time_gi.png')
        else:
            backglass = pygame.image.load('beach_time/assets/beach_time_off.png')
    backglass = pygame.transform.scale(backglass, (720, 1280))
    
    screen.blit(backglass, backglass_position)


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
                elif s.game.square_c.position == 2:
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
        if s.game.ball_count.position == 3:
            p = [550,663]
            screen.blit(select_now, p)
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
            p = [550,663]
            screen.blit(select_now, p)
    if sf == 9:
        if s.game.magic_squares_feature.position >= 5:
            p = [570,250]
            screen.blit(after_fifth, p)
        if s.game.ball_count.position == 5:
            p = [550,663]
            screen.blit(select_now, p)

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
            p = [549,706]
            screen.blit(select_now, p)
    if s.game.score_feature.position == 5:
        p = [236,708]
        screen.blit(score, p)
        if s.game.ball_count.position == 3:
            p = [549,706]
            screen.blit(select_now, p)
    if s.game.score_feature.position == 6:
        p = [326,708]
        screen.blit(score, p)
        if s.game.ball_count.position == 4:
            p = [549,706]
            screen.blit(select_now, p)

    if s.game.tilt.status == True:
        tilt_position = [452,217]
        screen.blit(tilt, tilt_position)

    pygame.display.flip()
    pygame.display.update()

def eb_animation(num):
    global screen

    if num == 9:
        p = [136,1037]
        screen.blit(eb_number, p)
        pygame.display.update()
    if num == 8:
        p = [189,1037]
        screen.blit(eb, p)
        pygame.display.update()
    if num == 7:
        p = [256,1037]
        screen.blit(eb, p)
        pygame.display.update()
    if num == 6:
        p = [326,1037]
        screen.blit(eb_number, p)
        pygame.display.update()
    if num == 5:
        p = [376,1037]
        screen.blit(eb, p)
        pygame.display.update()
    if num == 4:
        p = [441,1037]
        screen.blit(eb, p)
        pygame.display.update()
    if num == 3:
        p = [516,1037]
        screen.blit(eb_number, p)
        pygame.display.update()
    if num == 2:
        p = [565,1035]
        screen.blit(eb, p)
        pygame.display.update()
    if num == 1:
        p = [630,1035]
        screen.blit(eb, p)
        pygame.display.update()


def feature_animation(num):
    global screen
    if num == 6:
        p = [52,370]
        screen.blit(corners, p)
        pygame.display.update()

    if num == 3:
        p = [360,658]
        screen.blit(ms_letter, p)
        pygame.display.update()
   

def odds_animation(num):
    global screen

