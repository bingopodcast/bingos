
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
                elif s.game.square_c.position == 2:
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
            p = [556,649]
            dirty_rects.append(screen.blit(select_now, p))
        pygame.display.update(dirty_rects)
    else:
        dirty_rects.append(screen.blit(bg_gi, (556,649), pygame.Rect(556,649,156,43)))
        pygame.display.update(dirty_rects)
    b = not b

    args = [s,b,sn]

    s.delay(name="blink", delay=0.1, handler=blink, param=args)

def eb_animation(num):
    global screen

    if num == 9:
        p = [135,998]
        screen.blit(eb_number, p)
        pygame.display.update()
    if num == 8:
        p = [186,998]
        screen.blit(eb, p)
        pygame.display.update()
    if num == 7:
        p = [253,999]
        screen.blit(eb, p)
        pygame.display.update()
    if num == 6:
        p = [323,998]
        screen.blit(eb_number, p)
        pygame.display.update()
    if num == 5:
        p = [375,998]
        screen.blit(eb, p)
        pygame.display.update()
    if num == 4:
        p = [441,999]
        screen.blit(eb, p)
        pygame.display.update()
    if num == 3:
        p = [514,998]
        screen.blit(eb_number, p)
        pygame.display.update()
    if num == 2:
        p = [565,997]
        screen.blit(eb, p)
        pygame.display.update()
    if num == 1:
        p = [631,996]
        screen.blit(eb, p)
        pygame.display.update()


def feature_animation(num):
    global screen
    if num == 6:
        p = [37,493]
        screen.blit(corners, p)
        pygame.display.update()

    if num == 3:
        p = [380,643]
        screen.blit(ms_letter, p)
        pygame.display.update()
   

def odds_animation(num):
    global screen

