
import pygame

pygame.display.set_caption("multi bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

meter = pygame.image.load('graphics/assets/silver_register_cover.png').convert()
number = pygame.image.load('playtime/assets/number.png').convert_alpha()
feature = pygame.image.load('playtime/assets/feature.png').convert_alpha()
ms_letter = pygame.image.load('playtime/assets/ms_letter.png').convert_alpha()
ms_arrow = pygame.image.load('playtime/assets/ms_arrow.png').convert_alpha()
select_now = pygame.image.load('playtime/assets/select_now.png').convert_alpha()
corners = pygame.image.load('playtime/assets/feature.png').convert_alpha()
ballyhole = pygame.image.load('playtime/assets/feature.png').convert_alpha()
orange_odds1 = pygame.image.load('playtime/assets/orange_odds1.png').convert_alpha()
orange_odds2 = pygame.image.load('playtime/assets/orange_odds2.png').convert_alpha()
orange_odds3 = pygame.image.load('playtime/assets/orange_odds3.png').convert_alpha()
orange_odds4 = pygame.image.load('playtime/assets/orange_odds4.png').convert_alpha()
orange_odds5 = pygame.image.load('playtime/assets/orange_odds5.png').convert_alpha()
orange_odds6 = pygame.image.load('playtime/assets/orange_odds6.png').convert_alpha()
orange_odds7 = pygame.image.load('playtime/assets/orange_odds7.png').convert_alpha()
orange_odds8 = pygame.image.load('playtime/assets/orange_odds8.png').convert_alpha()
yellow_odds1 = pygame.image.load('playtime/assets/yellow_odds1.png').convert_alpha()
yellow_odds2 = pygame.image.load('playtime/assets/yellow_odds2.png').convert_alpha()
yellow_odds3 = pygame.image.load('playtime/assets/yellow_odds3.png').convert_alpha()
yellow_odds4 = pygame.image.load('playtime/assets/yellow_odds4.png').convert_alpha()
yellow_odds5 = pygame.image.load('playtime/assets/yellow_odds5.png').convert_alpha()
yellow_odds6 = pygame.image.load('playtime/assets/yellow_odds6.png').convert_alpha()
yellow_odds7 = pygame.image.load('playtime/assets/yellow_odds7.png').convert_alpha()
yellow_odds8 = pygame.image.load('playtime/assets/yellow_odds8.png').convert_alpha()
red_odds1 = pygame.image.load('playtime/assets/red_odds1.png').convert_alpha()
red_odds2 = pygame.image.load('playtime/assets/red_odds2.png').convert_alpha()
red_odds3 = pygame.image.load('playtime/assets/red_odds3.png').convert_alpha()
red_odds4 = pygame.image.load('playtime/assets/red_odds4.png').convert_alpha()
red_odds5 = pygame.image.load('playtime/assets/red_odds5.png').convert_alpha()
red_odds6 = pygame.image.load('playtime/assets/red_odds6.png').convert_alpha()
red_odds7 = pygame.image.load('playtime/assets/red_odds7.png').convert_alpha()
red_odds8 = pygame.image.load('playtime/assets/red_odds8.png').convert_alpha()
extra_balls = pygame.image.load('playtime/assets/extra_balls.png').convert_alpha()
eb = pygame.image.load('playtime/assets/eb.png').convert_alpha()
eb_number = pygame.image.load('playtime/assets/eb_number.png').convert_alpha()
tilt = pygame.image.load('playtime/assets/tilt.png').convert_alpha()
time = pygame.image.load('playtime/assets/time.png').convert_alpha()
s_arrow = pygame.image.load('playtime/assets/sf_arrow.png').convert_alpha()
a0 = pygame.image.load('playtime/assets/a0.png').convert_alpha()
a1 = pygame.image.load('playtime/assets/a1.png').convert_alpha()
a2 = pygame.image.load('playtime/assets/a2.png').convert_alpha()
a3 = pygame.image.load('playtime/assets/a3.png').convert_alpha()
b0 = pygame.image.load('playtime/assets/b0.png').convert_alpha()
b1 = pygame.image.load('playtime/assets/b1.png').convert_alpha()
b2 = pygame.image.load('playtime/assets/b2.png').convert_alpha()
b3 = pygame.image.load('playtime/assets/b3.png').convert_alpha()
c0 = pygame.image.load('playtime/assets/c0.png').convert_alpha()
c1 = pygame.image.load('playtime/assets/c1.png').convert_alpha()
c2 = pygame.image.load('playtime/assets/c2.png').convert_alpha()
c3 = pygame.image.load('playtime/assets/c3.png').convert_alpha()
d0 = pygame.image.load('playtime/assets/d0.png').convert_alpha()
d1 = pygame.image.load('playtime/assets/d1.png').convert_alpha()
d2 = pygame.image.load('playtime/assets/d2.png').convert_alpha()
d3 = pygame.image.load('playtime/assets/d3.png').convert_alpha()
e0 = pygame.image.load('playtime/assets/e0.png').convert_alpha()
e1 = pygame.image.load('playtime/assets/e1.png').convert_alpha()
e2 = pygame.image.load('playtime/assets/e2.png').convert_alpha()
e3 = pygame.image.load('playtime/assets/e3.png').convert_alpha()
rollover = pygame.image.load('playtime/assets/rollover.png').convert_alpha()
bg_menu = pygame.image.load('playtime/assets/playtime_menu.png')
bg_gi = pygame.image.load('playtime/assets/playtime_gi.png')
bg_off = pygame.image.load('playtime/assets/playtime_off.png')
a_1 = pygame.image.load('playtime/assets/a-1.png').convert_alpha()
a_2 = pygame.image.load('playtime/assets/a-2.png').convert_alpha()
a_3 = pygame.image.load('playtime/assets/a-3.png').convert_alpha()
a_4 = pygame.image.load('playtime/assets/a-4.png').convert_alpha()
b_1 = pygame.image.load('playtime/assets/b-1.png').convert_alpha()
b_2 = pygame.image.load('playtime/assets/b-2.png').convert_alpha()
b_3 = pygame.image.load('playtime/assets/b-3.png').convert_alpha()
b_4 = pygame.image.load('playtime/assets/b-4.png').convert_alpha()
c_1 = pygame.image.load('playtime/assets/c-1.png').convert_alpha()
c_2 = pygame.image.load('playtime/assets/c-2.png').convert_alpha()
c_3 = pygame.image.load('playtime/assets/c-3.png').convert_alpha()
c_4 = pygame.image.load('playtime/assets/c-4.png').convert_alpha()
d_1 = pygame.image.load('playtime/assets/d-1.png').convert_alpha()
d_2 = pygame.image.load('playtime/assets/d-2.png').convert_alpha()
d_3 = pygame.image.load('playtime/assets/d-3.png').convert_alpha()
d_4 = pygame.image.load('playtime/assets/d-4.png').convert_alpha()
e_1 = pygame.image.load('playtime/assets/e-1.png').convert_alpha()
e_2 = pygame.image.load('playtime/assets/e-2.png').convert_alpha()
e_3 = pygame.image.load('playtime/assets/e-3.png').convert_alpha()
e_4 = pygame.image.load('playtime/assets/e-4.png').convert_alpha()


class scorereel():
    """ Score Reels are used to count replays """
    def __init__(self, pos, image):
        self.position = pos
        self.default_y = self.position[1]
        self.image = pygame.image.load(image).convert()

reel1 = scorereel([101,325], "graphics/assets/white_reel.png")
reel10 = scorereel([82,325], "graphics/assets/white_reel.png")
reel100 = scorereel([63,325], "graphics/assets/white_reel.png")

def display(s, replays=0, menu=False):
    
    meter.set_colorkey((255,0,252))
    meter_position = [53,325]

    screen.blit(reel1.image, reel1.position)
    screen.blit(reel10.image, reel10.position)
    screen.blit(reel100.image, reel100.position)
    screen.blit(meter, meter_position)

    if s.game.square_a.position == 0:
        p = [223,334]
        screen.blit(a0, p)
    if s.game.square_a.position == 1:
        p = [223,334]
        screen.blit(a1, p)
    if s.game.square_a.position == 2:
        p = [223,334]
        screen.blit(a2, p)
    if s.game.square_a.position == 3:
        p = [223,334]
        screen.blit(a3, p)
    if s.game.square_b.position == 0:
        p = [220,443]
        screen.blit(b0, p)
    if s.game.square_b.position == 1:
        p = [220,443]
        screen.blit(b1, p)
    if s.game.square_b.position == 2:
        p = [220,443]
        screen.blit(b2, p)
    if s.game.square_b.position == 3:
        p = [220,443]
        screen.blit(b3, p)
    if s.game.square_c.position == 0:
        p = [332,334]
        screen.blit(c0, p)
    if s.game.square_c.position == 1:
        p = [332,334]
        screen.blit(c1, p)
    if s.game.square_c.position == 2:
        p = [332,334]
        screen.blit(c2, p)
    if s.game.square_c.position == 3:
        p = [332,334]
        screen.blit(c3, p)
    if s.game.square_d.position == 0:
        p = [332,440]
        screen.blit(d0, p)
    if s.game.square_d.position == 1:
        p = [332,440]
        screen.blit(d1, p)
    if s.game.square_d.position == 2:
        p = [332,440]
        screen.blit(d2, p)
    if s.game.square_d.position == 3:
        p = [332,440]
        screen.blit(d3, p)
    if s.game.square_e.position == 0:
        p = [223,544]
        screen.blit(e0, p)
    if s.game.square_e.position == 1:
        p = [223,544]
        screen.blit(e1, p)
    if s.game.square_e.position == 2:
        p = [223,544]
        screen.blit(e2, p)
    if s.game.square_e.position == 3:
        p = [223,544]
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
                    p = [281,340]
                    screen.blit(number, p)
                elif s.game.square_a.position == 1:
                    p = [281,392]
                    screen.blit(number, p)
                elif s.game.square_a.position == 2:
                    p = [227,393]
                    screen.blit(number, p)
                else:
                    p = [227,340]
                    screen.blit(number, p)
            if 2 in s.holes:
                if s.game.square_c.position == 0:
                    p = [337,339]
                    screen.blit(number, p)
                elif s.game.square_c.position == 1:
                    p = [391,339]
                    screen.blit(number, p)
                elif s.game.square_c.position == 2:
                    p = [390,391]
                    screen.blit(number, p)
                else:
                    p = [337,391]
                    screen.blit(number, p)
            if 3 in s.holes:
                if s.game.square_e.position == 0:
                    p = [392,551]
                    screen.blit(number, p)
                elif s.game.square_e.position == 1:
                    p = [228,551]
                    screen.blit(number, p)
                elif s.game.square_e.position == 2:
                    p = [282,551]
                    screen.blit(number, p)
                else:
                    p = [336,551]
                    screen.blit(number, p)
            if 4 in s.holes:
                if s.game.square_a.position == 0:
                    p = [227,394]
                    screen.blit(number, p)
                elif s.game.square_a.position == 1:
                    p = [228,343]
                    screen.blit(number, p)
                elif s.game.square_a.position == 2:
                    p = [281,334]
                    screen.blit(number, p)
                else:
                    p = [281,386]
                    screen.blit(number, p)
            if 5 in s.holes:
                if s.game.square_d.position == 0:
                    p = [337,499]
                    screen.blit(number, p)
                elif s.game.square_d.position == 1:
                    p = [335,445]
                    screen.blit(number, p)
                elif s.game.square_d.position == 2:
                    p = [390,445]
                    screen.blit(number, p)
                else:
                    p = [390,499]
                    screen.blit(number, p)
            if 6 in s.holes:
                if s.game.square_b.position == 0:
                    p = [228,500]
                    screen.blit(number, p)
                elif s.game.square_b.position == 1:
                    p = [227,448]
                    screen.blit(number, p)
                elif s.game.square_b.position == 2:
                    p = [281,446]
                    screen.blit(number, p)
                else:
                    p = [281,499]
                    screen.blit(number, p)
            if 7 in s.holes:
                if s.game.square_c.position == 0:
                    p = [336,393]
                    screen.blit(number, p)
                elif s.game.square_c.position == 1:
                    p = [337,340]
                    screen.blit(number, p)
                elif s.game.square_c.position == 2:
                    p = [392,341]
                    screen.blit(number, p)
                else:
                    p = [392,393]
                    screen.blit(number, p)
            if 8 in s.holes:
                if s.game.square_e.position == 0:
                    p = [283,552]
                    screen.blit(number, p)
                elif s.game.square_e.position == 1:
                    p = [337,552]
                    screen.blit(number, p)
                elif s.game.square_e.position == 2:
                    p = [392,552]
                    screen.blit(number, p)
                else:
                    p = [228,552]
                    screen.blit(number, p)
            if 9 in s.holes:
                if s.game.square_a.position == 0:
                    p = [228,340]
                    screen.blit(number, p)
                elif s.game.square_a.position == 1:
                    p = [281,341]
                    screen.blit(number, p)
                elif s.game.square_a.position == 2:
                    p = [281,393]
                    screen.blit(number, p)
                else:
                    p = [227,393]
                    screen.blit(number, p)
            if 10 in s.holes:
                p = [448,552]
                screen.blit(number, p)
            if 11 in s.holes:
                if s.game.square_c.position == 0:
                    p = [392,340]
                    screen.blit(number, p)
                elif s.game.square_c.position == 1:
                    p = [391,392]
                    screen.blit(number, p)
                elif s.game.square_c.position == 2:
                    p = [336,393]
                    screen.blit(number, p)
                else:
                    p = [337,340]
                    screen.blit(number, p)
            if 12 in s.holes:
                if s.game.square_e.position == 0:
                    p = [229,553]
                    screen.blit(number, p)
                elif s.game.square_e.position == 1:
                    p = [283,553]
                    screen.blit(number, p)
                elif s.game.square_e.position == 2:
                    p = [336,553]
                    screen.blit(number, p)
                else:
                    p = [393,553]
                    screen.blit(number, p)
            if 13 in s.holes:
                if s.game.square_d.position == 0:
                    p = [391,445]
                    screen.blit(number, p)
                elif s.game.square_d.position == 1:
                    p = [393,499]
                    screen.blit(number, p)
                elif s.game.square_d.position == 2:
                    p = [337,499]
                    screen.blit(number, p)
                else:
                    p = [337,445]
                    screen.blit(number, p)
            if 14 in s.holes:
                if s.game.square_e.position == 0:
                    p = [337,553]
                    screen.blit(number, p)
                elif s.game.square_e.position == 1:
                    p = [391,553]
                    screen.blit(number, p)
                elif s.game.square_e.position == 2:
                    p = [228,553]
                    screen.blit(number, p)
                else:
                    p = [282,553]
                    screen.blit(number, p)
            if 15 in s.holes:
                p = [448,339]
                screen.blit(number, p)
            if 16 in s.holes:
                if s.game.square_d.position == 0:
                    p = [337,445]
                    screen.blit(number, p)
                elif s.game.square_d.position == 1:
                    p = [391,446]
                    screen.blit(number, p)
                elif s.game.square_d.position == 2:
                    p = [393,499]
                    screen.blit(number, p)
                else:
                    p = [337,499]
                    screen.blit(number, p)
            if 17 in s.holes:
                p = [447,445]
                screen.blit(number, p)
            if 18 in s.holes:
                number_position = [447,393]
                screen.blit(number, number_position)
            if 19 in s.holes:
                if s.game.square_a.position == 0:
                    p = [282,392]
                    screen.blit(number, p)
                elif s.game.square_a.position == 1:
                    p = [227,393]
                    screen.blit(number, p)
                elif s.game.square_a.position == 2:
                    p = [229,340]
                    screen.blit(number, p)
                else:
                    p = [281,340]
                    screen.blit(number, p)
            if 20 in s.holes:
                p = [447,499]
                screen.blit(number, p)
            if 21 in s.holes:
                if s.game.square_d.position == 0:
                    p = [392,499]
                    screen.blit(number, p)
                elif s.game.square_d.position == 1:
                    p = [337,499]
                    screen.blit(number, p)
                elif s.game.square_d.position == 2:
                    p = [337,446]
                    screen.blit(number, p)
                else:
                    p = [392,446]
                    screen.blit(number, p)
            if 22 in s.holes:
                if s.game.square_c.position == 0:
                    p = [393,392]
                    screen.blit(number, p)
                elif s.game.square_c.position == 1:
                    p = [337,395]
                    screen.blit(number, p)
                elif s.game.square_c.position == 2:
                    p = [338,341]
                    screen.blit(number, p)
                else:
                    p = [393,341]
                    screen.blit(number, p)
            if 23 in s.holes:
                if s.game.square_b.position == 0:
                    p = [283,500]
                    screen.blit(number, p)
                elif s.game.square_b.position == 1:
                    p = [228,500]
                    screen.blit(number, p)
                elif s.game.square_b.position == 2:
                    p = [228,447]
                    screen.blit(number, p)
                else:
                    p = [281,446]
                    screen.blit(number, p)
            if 24 in s.holes:
                if s.game.square_b.position == 0:
                    p = [281,446]
                    screen.blit(number, p)
                elif s.game.square_b.position == 1:
                    p = [283,500]
                    screen.blit(number, p)
                elif s.game.square_b.position == 2:
                    p = [227,500]
                    screen.blit(number, p)
                else:
                    p = [227,447]
                    screen.blit(number, p)
            if 25 in s.holes:
                if s.game.square_b.position == 0:
                    p = [227,447]
                    screen.blit(number, p)
                elif s.game.square_b.position == 1:
                    p = [281,447]
                    screen.blit(number, p)
                elif s.game.square_b.position == 2:
                    p = [283,500]
                    screen.blit(number, p)
                else:
                    p = [227,501]
                    screen.blit(number, p)


    if s.game.magic_squares_feature.position == 1:
        p = [13,655]
        screen.blit(ms_arrow, p)
    if s.game.magic_squares_feature.position == 2:
        p = [51,655]
        screen.blit(ms_arrow, p)
    if s.game.magic_squares_feature.position == 3:
        p = [91,655]
        screen.blit(ms_arrow, p)
    if s.game.magic_squares_feature.position == 4:
        p = [131,655]
        screen.blit(ms_arrow, p)
    if s.game.magic_squares_feature.position >= 5:
        p = [172,643]
        screen.blit(ms_letter, p)
    if s.game.magic_squares_feature.position >= 6:
        p = [223,643]
        screen.blit(ms_letter, p)
    if s.game.magic_squares_feature.position >= 7:
        p = [275,643]
        screen.blit(ms_letter, p)
    if s.game.magic_squares_feature.position >= 8:
        p = [328,643]
        screen.blit(ms_letter, p)
    if s.game.magic_squares_feature.position == 9:
        p = [380,643]
        screen.blit(ms_letter, p)

    if s.game.magic_squares_feature.position >= 5:
        sf = s.game.selection_feature.position 
        if sf <= 6:
            p = [564,567]
            screen.blit(time, p)
            if sf == 1:
                p = [539,593]
                screen.blit(s_arrow, p)
            if sf == 2:
                p = [540,556]
                screen.blit(s_arrow, p)
            if sf == 3:
                p = [539,519]
                screen.blit(s_arrow, p)
            if sf == 4:
                p = [538,482]
                screen.blit(s_arrow, p)
            if sf == 5:
                p = [539,443]
                screen.blit(s_arrow, p)
            if sf == 6:
                p = [539,409]
                screen.blit(s_arrow, p)
            if s.game.ball_count.position == 3:
                s.cancel_delayed(name="blink")
                blink([s,1,1])
            else:
                s.cancel_delayed(name="blink")
        if sf == 3 or sf == 4:
            p = [33,932]
            screen.blit(rollover, p)
            p = [567,495]
            screen.blit(time, p)
        if sf == 5 or sf == 6:
            p = [631,929]
            screen.blit(rollover, p)
            p = [565,418]
            screen.blit(time, p)
        if sf == 7 or sf == 8:
            if sf == 7:
                p = [539,369]
                screen.blit(s_arrow, p)
            if sf == 8:
                p = [539,333]
                screen.blit(s_arrow, p)
            p = [563,344]
            screen.blit(time, p)
            if s.game.ball_count.position == 4:
                s.cancel_delayed(name="blink")
                blink([s,1,1])
            else:
                s.cancel_delayed(name="blink")
        if sf == 9:
            p = [539,297]
            screen.blit(s_arrow, p)
            p = [565,272]
            screen.blit(time, p)
            if s.game.ball_count.position == 5:
                s.cancel_delayed(name="blink")
                blink([s,1,1])
            else:
                s.cancel_delayed(name="blink")

    if s.game.corners.status == True:
        p = [37,493]
        screen.blit(corners, p)

    if s.game.ballyhole.status == True:
        p = [37,569]
        screen.blit(ballyhole, p)

    if s.game.extra_ball.position >= 1:
        p = [135,998]
        screen.blit(eb_number, p)
    if s.game.extra_ball.position >= 2:
        p = [186,998]
        screen.blit(eb, p)
    if s.game.extra_ball.position >= 3:
        p = [253,999]
        screen.blit(eb, p)
    if s.game.extra_ball.position >= 4:
        p = [323,998]
        screen.blit(eb_number, p)
    if s.game.extra_ball.position >= 5:
        p = [375,998]
        screen.blit(eb, p)
    if s.game.extra_ball.position >= 6:
        p = [441,999]
        screen.blit(eb, p)
    if s.game.extra_ball.position >= 7:
        p = [514,998]
        screen.blit(eb_number, p)
    if s.game.extra_ball.position >= 8:
        p = [565,997]
        screen.blit(eb, p)
    if s.game.extra_ball.position == 9:
        p = [631,996]
        screen.blit(eb, p)

    if s.game.eb_play.status == True:
        p = [23,997]
        screen.blit(extra_balls, p)

    if s.game.red_odds.position == 1:
        p = [29,761]
        screen.blit(red_odds1, p)
    elif s.game.red_odds.position == 2:
        p = [140,714]
        screen.blit(red_odds2, p)
    elif s.game.red_odds.position == 3:
        p = [197,714]
        screen.blit(red_odds3, p)
    elif s.game.red_odds.position == 4:
        p = [284,704]
        screen.blit(red_odds4, p)
    elif s.game.red_odds.position == 5:
        p = [403,709]
        screen.blit(red_odds5, p)
    elif s.game.red_odds.position == 6:
        p = [493,713]
        screen.blit(red_odds6, p)
    elif s.game.red_odds.position == 7:
        p = [546,713]
        screen.blit(red_odds7, p)
    elif s.game.red_odds.position == 8:
        p = [676,745]
        screen.blit(red_odds8, p)


    if s.game.orange_odds.position == 1:
        p = [26,817]
        screen.blit(orange_odds1, p)
    elif s.game.orange_odds.position == 2:
        p = [145,787]
        screen.blit(orange_odds2, p)
    elif s.game.orange_odds.position == 3:
        p = [187,786]
        screen.blit(orange_odds3, p)
    elif s.game.orange_odds.position == 4:
        p = [274,776]
        screen.blit(orange_odds4, p)
    elif s.game.orange_odds.position == 5:
        p = [401,776]
        screen.blit(orange_odds5, p)
    elif s.game.orange_odds.position == 6:
        p = [509,785]
        screen.blit(orange_odds6, p)
    elif s.game.orange_odds.position == 7:
        p = [551,780]
        screen.blit(orange_odds7, p)
    elif s.game.orange_odds.position == 8:
        p = [665,819]
        screen.blit(orange_odds8, p)

    if s.game.yellow_odds.position == 1:
        p = [36,879]
        screen.blit(yellow_odds1, p)
    elif s.game.yellow_odds.position == 2:
        p = [147,868]
        screen.blit(yellow_odds2, p)
    elif s.game.yellow_odds.position == 3:
        p = [193,859]
        screen.blit(yellow_odds3, p)
    elif s.game.yellow_odds.position == 4:
        p = [277,873]
        screen.blit(yellow_odds4, p)
    elif s.game.yellow_odds.position == 5:
        p = [400,872]
        screen.blit(yellow_odds5, p)
    elif s.game.yellow_odds.position == 6:
        p = [502,851]
        screen.blit(yellow_odds6, p)
    elif s.game.yellow_odds.position == 7:
        p = [552,849]
        screen.blit(yellow_odds7, p)
    elif s.game.yellow_odds.position == 8:
        p = [665,878]
        screen.blit(yellow_odds8, p)

    if s.game.tilt.status == True:
        tilt_position = [59,405]
        screen.blit(tilt, tilt_position)

    pygame.display.update()

def blink(args):
    dirty_rects = []
    s = args[0]
    b = args[1]
    sn = args[2]

    if b == 0:
        if sn == 1:
            p = [556,649]
            dirty_rects.append(screen.blit(select_now, p))
        pygame.display.update(dirty_rects)
    else:
        dirty_rects.append(screen.blit(bg_gi, (556,649), pygame.Rect(556,649,156,43)))
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
        p = [223,334]
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
        dirty_rects.append(screen.blit(topleft, (242  - num - 20, 338)))
        dirty_rects.append(screen.blit(topright, (279, 347 - num - 10)))
        dirty_rects.append(screen.blit(bottomright, (273  + num + 15, 389)))
        dirty_rects.append(screen.blit(bottomleft, (225, 390 + num + 5)))

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
        p = [220,443]
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
        dirty_rects.append(screen.blit(topleft, (238 - num - 20, 447)))
        dirty_rects.append(screen.blit(topright, (276, 451 - num - 9)))
        dirty_rects.append(screen.blit(bottomright, (276  + num + 10, 499)))
        dirty_rects.append(screen.blit(bottomleft, (222, 501 + num + 8)))
    
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
        p = [332,334]
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
        dirty_rects.append(screen.blit(topleft, (343  - num - 10, 337)))
        dirty_rects.append(screen.blit(topright, (387, 338 - num - 5)))
        dirty_rects.append(screen.blit(bottomright, (379  + num + 15, 390)))
        dirty_rects.append(screen.blit(bottomleft, (334, 390 + num + 6)))
    
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
    
    p = [332,440]
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
        dirty_rects.append(screen.blit(topleft, (341 - num - 10, 444)))
        dirty_rects.append(screen.blit(topright, (387, 452 - num - 13)))
        dirty_rects.append(screen.blit(bottomright, (364  + num + 29, 498)))
        dirty_rects.append(screen.blit(bottomleft, (337, 497 + num + 12)))
    
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
    
    p = [223,544]
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
    dirty_rects.append(screen.blit(topleft, (231 - num - 10, 551)))
    if num > -40:
        dirty_rects.append(screen.blit(topright, (277, 549 - num)))
    else:
        dirty_rects.append(screen.blit(topright, (332, 607 + num)))
    dirty_rects.append(screen.blit(bottomleft, (332 - num - 10, 549)))
    if num > -40:
        dirty_rects.append(screen.blit(bottomright, (387, 551 - num)))
    else:
        dirty_rects.append(screen.blit(bottomright, (223, 607 + num)))
    
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
        dirty_rects.append(screen.blit(bg_gi, (135,998), pygame.Rect(135,998,56,35)))
    if s.game.extra_ball.position < 2:
        dirty_rects.append(screen.blit(bg_gi, (186,998), pygame.Rect(186,998,73,35)))
    if s.game.extra_ball.position < 3:
        dirty_rects.append(screen.blit(bg_gi, (253,999), pygame.Rect(253,999,73,35)))
    if s.game.extra_ball.position < 4:
        dirty_rects.append(screen.blit(bg_gi, (323,998), pygame.Rect(323,998,56,35)))
    if s.game.extra_ball.position < 5:
        dirty_rects.append(screen.blit(bg_gi, (375,998), pygame.Rect(375,998,73,35)))
    if s.game.extra_ball.position < 6:
        dirty_rects.append(screen.blit(bg_gi, (441,999), pygame.Rect(441,999,73,35)))
    if s.game.extra_ball.position < 7:
        dirty_rects.append(screen.blit(bg_gi, (514,998), pygame.Rect(514,998,56,35)))
    if s.game.extra_ball.position < 8:
        dirty_rects.append(screen.blit(bg_gi, (565,997), pygame.Rect(565,997,73,35)))
    if s.game.extra_ball.position < 9:
        dirty_rects.append(screen.blit(bg_gi, (631,996), pygame.Rect(631,996,73,35)))

    pygame.display.update(dirty_rects)

    if num in [0,24,25,49,14,39]:
        if s.game.extra_ball.position < 1:
            p = [135,998]
            dirty_rects.append(screen.blit(eb_number, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [1,15,26,40]:
        if s.game.extra_ball.position < 2:
            p = [186,998]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [3,4,17,28,29,42]:
        if s.game.extra_ball.position < 3:
            p = [253,999]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [5,18,30,43]:
        if s.game.extra_ball.position < 4:
            p = [323,998]
            dirty_rects.append(screen.blit(eb_number, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [7,8,19,32,33,44]:
        if s.game.extra_ball.position < 5:
            p = [375,998]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [9,10,20,34,35,45]:
        if s.game.extra_ball.position < 6:
            p = [441,999]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [11,21,36,46]:
        if s.game.extra_ball.position < 7:
            p = [514,998]
            dirty_rects.append(screen.blit(eb_number, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [12,22,37,47]:
        if s.game.extra_ball.position < 8:
            p = [565,997]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [2,6,13,16,23,27,31,38,41,48]:
        if s.game.extra_ball.position < 9:
            p = [631,996]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects) 
            return

def clear_odds(s, num):
    global screen

    dirty_rects = []
    if s.game.yellow_odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (36,879), pygame.Rect(36,879,28,53)))
    if s.game.yellow_odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (147,868), pygame.Rect(147,868,28,53)))
    if s.game.yellow_odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (193,859), pygame.Rect(193,859,28,53)))
    if s.game.yellow_odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (277,873), pygame.Rect(277,873,28,53)))
    if s.game.yellow_odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (400,872), pygame.Rect(400,872,37,53)))
    if s.game.yellow_odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (502,851), pygame.Rect(502,851,37,53)))
    if s.game.yellow_odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (552,849), pygame.Rect(552,849,37,53)))
    if s.game.yellow_odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (665,878), pygame.Rect(665,878,37,53)))

    if s.game.red_odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (29,761), pygame.Rect(29,761,26,53)))
    if s.game.red_odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (140,714), pygame.Rect(140,714,28,53)))
    if s.game.red_odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (197,714), pygame.Rect(197,714,28,53)))
    if s.game.red_odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (284,704), pygame.Rect(284,704,28,53)))
    if s.game.red_odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (403,709), pygame.Rect(403,709,37,53)))
    if s.game.red_odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (493,713), pygame.Rect(493,713,37,53)))
    if s.game.red_odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (546,713), pygame.Rect(546,713,37,53)))
    if s.game.red_odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (676,745), pygame.Rect(676,745,37,53)))

    if s.game.orange_odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (26,817), pygame.Rect(26,817,28,53)))
    if s.game.orange_odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (145,787), pygame.Rect(145,787,28,53)))
    if s.game.orange_odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (187,786), pygame.Rect(187,786,28,53)))
    if s.game.orange_odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (274,776), pygame.Rect(274,776,28,53)))
    if s.game.orange_odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (401,776), pygame.Rect(401,776,37,53)))
    if s.game.orange_odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (509,785), pygame.Rect(509,785,37,53)))
    if s.game.orange_odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (551,780), pygame.Rect(551,780,37,53)))
    if s.game.orange_odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (665,819), pygame.Rect(665,819,37,53)))

    pygame.display.update(dirty_rects)

def draw_odds_animation(s, num):
    global screen
    dirty_rects = []
    if num in [2,7,36,27,32,11]:
        if s.game.yellow_odds.position != 1:
            p = [36,879]
            dirty_rects.append(screen.blit(yellow_odds1, p))
            pygame.display.update(dirty_rects)
            return
    if num in [47,23]:
        if s.game.yellow_odds.position != 2:
            p = [147,868]
            dirty_rects.append(screen.blit(yellow_odds2, p))
            pygame.display.update(dirty_rects)
            return
    if num in [8,31]:
        if s.game.yellow_odds.position != 3:
            p = [193,859]
            dirty_rects.append(screen.blit(yellow_odds3, p))
            pygame.display.update(dirty_rects)
            return
    if num in [25,50]:
        if s.game.yellow_odds.position != 4:
            p = [277,873]
            dirty_rects.append(screen.blit(yellow_odds4, p))
            pygame.display.update(dirty_rects)
            return
    if num in [3,28]:
        if s.game.yellow_odds.position != 5:
            p = [400,872]
            dirty_rects.append(screen.blit(yellow_odds5, p))
            pygame.display.update(dirty_rects)
            return
    if num in [14,30]:
        if s.game.yellow_odds.position != 6:
            p = [502,851]
            dirty_rects.append(screen.blit(yellow_odds6, p))
            pygame.display.update(dirty_rects)
            return
    if num in [18,43]:
        if s.game.yellow_odds.position != 7:
            p = [552,849]
            dirty_rects.append(screen.blit(yellow_odds7, p))
            pygame.display.update(dirty_rects)
            return
    if num in [16,41]:
        if s.game.yellow_odds.position != 8:
            p = [665,878]
            dirty_rects.append(screen.blit(yellow_odds8, p))
            pygame.display.update(dirty_rects)
            return

    if num in [6,31]:
        if s.game.red_odds.position != 1:
            p = [29,761]
            dirty_rects.append(screen.blit(red_odds1, p))
            pygame.display.update(dirty_rects)
            return
    if num in [1,26]:
        if s.game.red_odds.position != 2:
            p = [140,714]
            dirty_rects.append(screen.blit(red_odds2, p))
            pygame.display.update(dirty_rects)
            return
    if num in [12,37]:
        if s.game.red_odds.position != 3:
            p = [197,714]
            dirty_rects.append(screen.blit(red_odds3, p))
            pygame.display.update(dirty_rects)
            return
    if num in [20,45]:
        if s.game.red_odds.position != 4:
            p = [284,704]
            dirty_rects.append(screen.blit(red_odds4, p))
            pygame.display.update(dirty_rects)
            return
    if num in [9,34]:
        if s.game.red_odds.position != 5:
            p = [403,709]
            dirty_rects.append(screen.blit(red_odds5, p))
            pygame.display.update(dirty_rects)
            return
    if num in [0,26]:
        if s.game.red_odds.position != 6:
            p = [493,713]
            dirty_rects.append(screen.blit(red_odds6, p))
            pygame.display.update(dirty_rects)
            return
    if num in [15,40]:
        if s.game.red_odds.position != 7:
            p = [546,713]
            dirty_rects.append(screen.blit(red_odds7, p))
            pygame.display.update(dirty_rects)
            return
    if num in [2,27]:
        if s.game.red_odds.position != 8:
            p = [676,745]
            dirty_rects.append(screen.blit(red_odds8, p))
            pygame.display.update(dirty_rects)
            return

    if num in [5,30]:
        if s.game.orange_odds.position != 1:
            p = [26,817]
            dirty_rects.append(screen.blit(orange_odds1, p))
            pygame.display.update(dirty_rects)
            return
    if num in [19,44]:
        if s.game.orange_odds.position != 2:
            p = [145,787]
            dirty_rects.append(screen.blit(orange_odds2, p))
            pygame.display.update(dirty_rects)
            return
    if num in [17,42]:
        if s.game.orange_odds.position != 3:
            p = [187,786]
            dirty_rects.append(screen.blit(orange_odds3, p))
            pygame.display.update(dirty_rects)
            return
    if num in [22,47]:
        if s.game.orange_odds.position != 4:
            p = [274,776]
            dirty_rects.append(screen.blit(orange_odds4, p))
            pygame.display.update(dirty_rects)
            return
    if num in [13,38]:
        if s.game.orange_odds.position != 5:
            p = [401,776]
            dirty_rects.append(screen.blit(orange_odds5, p))
            pygame.display.update(dirty_rects)
            return
    if num in [7,32]:
        if s.game.orange_odds.position != 6:
            p = [509,785]
            dirty_rects.append(screen.blit(orange_odds6, p))
            pygame.display.update(dirty_rects)
            return
    if num in [4,29]:
        if s.game.orange_odds.position != 7:
            p = [551,780]
            dirty_rects.append(screen.blit(orange_odds7, p))
            pygame.display.update(dirty_rects)
            return
    if num in [11,36]:
        if s.game.orange_odds.position != 8:
            p = [665,819]
            dirty_rects.append(screen.blit(orange_odds8, p))
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
        dirty_rects.append(screen.blit(bg_gi, (172,643), pygame.Rect(172,643,56,56)))
    if s.game.magic_squares_feature.position < 6:
        dirty_rects.append(screen.blit(bg_gi, (223,643), pygame.Rect(223,643,56,56)))
    if s.game.magic_squares_feature.position < 7:
        dirty_rects.append(screen.blit(bg_gi, (275,643), pygame.Rect(275,643,56,56)))
    if s.game.magic_squares_feature.position < 8:
        dirty_rects.append(screen.blit(bg_gi, (328,643), pygame.Rect(328,643,56,56)))
    if s.game.magic_squares_feature.position < 9:
        dirty_rects.append(screen.blit(bg_gi, (380,643), pygame.Rect(380,643,56,56)))

    if s.game.selection_feature.position not in [3,4]:
        dirty_rects.append(screen.blit(bg_gi, (33,932), pygame.Rect(33,932,63,59)))
        dirty_rects.append(screen.blit(bg_gi, (567,495), pygame.Rect(567,495,144,76)))
    if s.game.selection_feature.position not in [5,6]:
        dirty_rects.append(screen.blit(bg_gi, (631,929), pygame.Rect(631,929,63,59)))
        dirty_rects.append(screen.blit(bg_gi, (565,418), pygame.Rect(565,418,144,76)))
    if s.game.ballyhole.status == False:
        dirty_rects.append(screen.blit(bg_gi, (37,569), pygame.Rect(37,569,124,74)))
    if s.game.corners.status == False:
        dirty_rects.append(screen.blit(bg_gi, (37,493), pygame.Rect(37,493,124,74)))
    if s.game.selection_feature.position not in [7,8]:
        dirty_rects.append(screen.blit(bg_gi, (563,344), pygame.Rect(563,344,144,76)))
    if s.game.selection_feature.position != 9:
        dirty_rects.append(screen.blit(bg_gi, (565,272), pygame.Rect(565,272,144,76)))
    pygame.display.update(dirty_rects)


def draw_feature_animation(s, num):
    global screen
    dirty_rects = []

    if num in [10,20,25,35,45,50]:
        if s.game.magic_squares_feature.position < 6:
            p = [172,643]
            dirty_rects.append(screen.blit(ms_letter, p))
            p = [223,643]
            dirty_rects.append(screen.blit(ms_letter, p))
            pygame.display.update(dirty_rects)
            return
    if num in [5,15,24,30,40,49]:
        if s.game.magic_squares_feature.position < 7:
            p = [275,643]
            dirty_rects.append(screen.blit(ms_letter, p))
            pygame.display.update(dirty_rects)
            return
    if num in [17,23,42,48]:
        if s.game.magic_squares_feature.position < 8:
            p = [328,643]
            dirty_rects.append(screen.blit(ms_letter, p))
            pygame.display.update(dirty_rects)
            return
    if num in [12,22,37,47]:
        if s.game.magic_squares_feature.position < 9:
            p = [380,643]
            dirty_rects.append(screen.blit(ms_letter, p))
            pygame.display.update(dirty_rects)
            return

    if num in [8,18,33,43]:
        if s.game.selection_feature.position not in [3,4]:
            p = [33,932]
            dirty_rects.append(screen.blit(rollover, p))
            p = [567,495]
            dirty_rects.append(screen.blit(time, p))
            s.game.coils.redROLamp.pulse(85)
            pygame.display.update(dirty_rects)
            return
    if num in [3,13,28,38]:
        if s.game.selection_feature.position not in [5,6]:
            p = [631,929]
            dirty_rects.append(screen.blit(rollover, p))
            p = [565,418]
            dirty_rects.append(screen.blit(time, p))
            s.game.coils.yellowROLamp.pulse(85)
            pygame.display.update(dirty_rects)
            return
    if num in [4,14,29,39]:
        if s.game.ballyhole.status == False:
            p = [37,569]
            dirty_rects.append(screen.blit(ballyhole, p))
            pygame.display.update(dirty_rects)
            return
    if num in [9,19,34,44]:
        if s.game.corners.status == False:
            p = [37,493]
            dirty_rects.append(screen.blit(corners, p))
            pygame.display.update(dirty_rects)
            return
    if num in [11,21,36,46]:
        if s.game.selection_feature.position not in [7,8]:
            p = [563,344]
            dirty_rects.append(screen.blit(time, p))
            pygame.display.update(dirty_rects)
            return
    if num in [0,6,16,25,31,41]:
        if s.game.selection_feature.position != 9:
            p = [565,272]
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

