
import pygame

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

meter = pygame.image.load('graphics/assets/register_cover.png').convert()
number = pygame.image.load('cypress_gardens/assets/number.png').convert_alpha()
feature = pygame.image.load('cypress_gardens/assets/feature.png').convert_alpha()
ms_letter = pygame.image.load('cypress_gardens/assets/ms_letter.png').convert_alpha()
ms_arrow = pygame.image.load('cypress_gardens/assets/ms_arrow.png').convert_alpha()
select_now = pygame.image.load('cypress_gardens/assets/select_now.png').convert_alpha()
corners = pygame.image.load('cypress_gardens/assets/corners.png').convert_alpha()
ballyhole = pygame.image.load('cypress_gardens/assets/feature.png').convert_alpha()
odds = pygame.image.load('cypress_gardens/assets/odds.png').convert_alpha()
extra_balls = pygame.image.load('cypress_gardens/assets/extra_ball.png').convert_alpha()
eb = pygame.image.load('cypress_gardens/assets/eb.png').convert_alpha()
eb_number = pygame.image.load('cypress_gardens/assets/eb_number.png').convert_alpha()
tilt = pygame.image.load('cypress_gardens/assets/tilt.png').convert_alpha()
time = pygame.image.load('cypress_gardens/assets/time.png').convert_alpha()
s_arrow = pygame.image.load('cypress_gardens/assets/s_arrow.png').convert_alpha()
a0 = pygame.image.load('cypress_gardens/assets/a0.png').convert_alpha()
a1 = pygame.image.load('cypress_gardens/assets/a1.png').convert_alpha()
a2 = pygame.image.load('cypress_gardens/assets/a2.png').convert_alpha()
a3 = pygame.image.load('cypress_gardens/assets/a3.png').convert_alpha()
b0 = pygame.image.load('cypress_gardens/assets/b0.png').convert_alpha()
b1 = pygame.image.load('cypress_gardens/assets/b1.png').convert_alpha()
b2 = pygame.image.load('cypress_gardens/assets/b2.png').convert_alpha()
b3 = pygame.image.load('cypress_gardens/assets/b3.png').convert_alpha()
c0 = pygame.image.load('cypress_gardens/assets/c0.png').convert_alpha()
c1 = pygame.image.load('cypress_gardens/assets/c1.png').convert_alpha()
c2 = pygame.image.load('cypress_gardens/assets/c2.png').convert_alpha()
c3 = pygame.image.load('cypress_gardens/assets/c3.png').convert_alpha()
d0 = pygame.image.load('cypress_gardens/assets/d0.png').convert_alpha()
d1 = pygame.image.load('cypress_gardens/assets/d1.png').convert_alpha()
d2 = pygame.image.load('cypress_gardens/assets/d2.png').convert_alpha()
d3 = pygame.image.load('cypress_gardens/assets/d3.png').convert_alpha()
e0 = pygame.image.load('cypress_gardens/assets/e0.png').convert_alpha()
e1 = pygame.image.load('cypress_gardens/assets/e1.png').convert_alpha()
e2 = pygame.image.load('cypress_gardens/assets/e2.png').convert_alpha()
e3 = pygame.image.load('cypress_gardens/assets/e3.png').convert_alpha()
rollover = pygame.image.load('cypress_gardens/assets/rollover.png').convert_alpha()
bg_menu = pygame.image.load('cypress_gardens/assets/cypress_gardens_menu.png')
bg_gi = pygame.image.load('cypress_gardens/assets/cypress_gardens_gi.png')
bg_off = pygame.image.load('cypress_gardens/assets/cypress_gardens_off.png')
a_1 = pygame.image.load('cypress_gardens/assets/a-1.png').convert_alpha()
a_2 = pygame.image.load('cypress_gardens/assets/a-2.png').convert_alpha()
a_3 = pygame.image.load('cypress_gardens/assets/a-3.png').convert_alpha()
a_4 = pygame.image.load('cypress_gardens/assets/a-4.png').convert_alpha()
b_1 = pygame.image.load('cypress_gardens/assets/b-1.png').convert_alpha()
b_2 = pygame.image.load('cypress_gardens/assets/b-2.png').convert_alpha()
b_3 = pygame.image.load('cypress_gardens/assets/b-3.png').convert_alpha()
b_4 = pygame.image.load('cypress_gardens/assets/b-4.png').convert_alpha()
c_1 = pygame.image.load('cypress_gardens/assets/c-1.png').convert_alpha()
c_2 = pygame.image.load('cypress_gardens/assets/c-2.png').convert_alpha()
c_3 = pygame.image.load('cypress_gardens/assets/c-3.png').convert_alpha()
c_4 = pygame.image.load('cypress_gardens/assets/c-4.png').convert_alpha()
d_1 = pygame.image.load('cypress_gardens/assets/d-1.png').convert_alpha()
d_2 = pygame.image.load('cypress_gardens/assets/d-2.png').convert_alpha()
d_3 = pygame.image.load('cypress_gardens/assets/d-3.png').convert_alpha()
d_4 = pygame.image.load('cypress_gardens/assets/d-4.png').convert_alpha()
e_1 = pygame.image.load('cypress_gardens/assets/e-1.png').convert_alpha()
e_2 = pygame.image.load('cypress_gardens/assets/e-2.png').convert_alpha()
e_3 = pygame.image.load('cypress_gardens/assets/e-3.png').convert_alpha()
e_4 = pygame.image.load('cypress_gardens/assets/e-4.png').convert_alpha()




class scorereel():
    """ Score Reels are used to count replays """
    def __init__(self, pos, image):
        self.position = pos
        self.default_y = self.position[1]
        self.image = pygame.image.load(image).convert()

reel1 = scorereel([95,285], "graphics/assets/white_reel.png")
reel10 = scorereel([76,285], "graphics/assets/white_reel.png")
reel100 = scorereel([57,285], "graphics/assets/white_reel.png")

def display(s, replays=0, menu=False):
    
    meter.set_colorkey((255,0,252))
    meter_position = [48,285]

    screen.blit(reel1.image, reel1.position)
    screen.blit(reel10.image, reel10.position)
    screen.blit(reel100.image, reel100.position)
    screen.blit(meter, meter_position)

    if s.game.square_a.position == 0:
        p = [222,328]
        screen.blit(a0, p)
    if s.game.square_a.position == 1:
        p = [222,328]
        screen.blit(a1, p)
    if s.game.square_a.position == 2:
        p = [222,328]
        screen.blit(a2, p)
    if s.game.square_a.position == 3:
        p = [222,328]
        screen.blit(a3, p)
    if s.game.square_b.position == 0:
        p = [222,442]
        screen.blit(b0, p)
    if s.game.square_b.position == 1:
        p = [222,442]
        screen.blit(b1, p)
    if s.game.square_b.position == 2:
        p = [222,442]
        screen.blit(b2, p)
    if s.game.square_b.position == 3:
        p = [222,442]
        screen.blit(b3, p)
    if s.game.square_c.position == 0:
        p = [333,328]
        screen.blit(c0, p)
    if s.game.square_c.position == 1:
        p = [333,328]
        screen.blit(c1, p)
    if s.game.square_c.position == 2:
        p = [333,328]
        screen.blit(c2, p)
    if s.game.square_c.position == 3:
        p = [333,328]
        screen.blit(c3, p)
    if s.game.square_d.position == 0:
        p = [330,442]
        screen.blit(d0, p)
    if s.game.square_d.position == 1:
        p = [330,442]
        screen.blit(d1, p)
    if s.game.square_d.position == 2:
        p = [330,442]
        screen.blit(d2, p)
    if s.game.square_d.position == 3:
        p = [330,442]
        screen.blit(d3, p)
    if s.game.square_e.position == 0:
        p = [222,549]
        screen.blit(e0, p)
    if s.game.square_e.position == 1:
        p = [222,549]
        screen.blit(e1, p)
    if s.game.square_e.position == 2:
        p = [222,549]
        screen.blit(e2, p)
    if s.game.square_e.position == 3:
        p = [222,549]
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
                    p = [281,331]
                    screen.blit(number, p)
                elif s.game.square_a.position == 1:
                    p = [281,387]
                    screen.blit(number, p)
                elif s.game.square_a.position == 2:
                    p = [227,389]
                    screen.blit(number, p)
                else:
                    p = [229,331]
                    screen.blit(number, p)
            if 2 in s.holes:
                if s.game.square_c.position == 0:
                    p = [335,331]
                    screen.blit(number, p)
                elif s.game.square_c.position == 1:
                    p = [389,331]
                    screen.blit(number, p)
                elif s.game.square_c.position == 2:
                    p = [389,388]
                    screen.blit(number, p)
                else:
                    p = [335,389]
                    screen.blit(number, p)
            if 3 in s.holes:
                if s.game.square_e.position == 0:
                    p = [389,557]
                    screen.blit(number, p)
                elif s.game.square_e.position == 1:
                    p = [229,557]
                    screen.blit(number, p)
                elif s.game.square_e.position == 2:
                    p = [282,557]
                    screen.blit(number, p)
                else:
                    p = [335,557]
                    screen.blit(number, p)
            if 4 in s.holes:
                if s.game.square_a.position == 0:
                    p = [228,388]
                    screen.blit(number, p)
                elif s.game.square_a.position == 1:
                    p = [229,331]
                    screen.blit(number, p)
                elif s.game.square_a.position == 2:
                    p = [282,331]
                    screen.blit(number, p)
                else:
                    p = [282,388]
                    screen.blit(number, p)
            if 5 in s.holes:
                if s.game.square_d.position == 0:
                    p = [335,502]
                    screen.blit(number, p)
                elif s.game.square_d.position == 1:
                    p = [335,445]
                    screen.blit(number, p)
                elif s.game.square_d.position == 2:
                    p = [388,445]
                    screen.blit(number, p)
                else:
                    p = [388,502]
                    screen.blit(number, p)
            if 6 in s.holes:
                if s.game.square_b.position == 0:
                    p = [229,501]
                    screen.blit(number, p)
                elif s.game.square_b.position == 1:
                    p = [229,445]
                    screen.blit(number, p)
                elif s.game.square_b.position == 2:
                    p = [283,445]
                    screen.blit(number, p)
                else:
                    p = [282,501]
                    screen.blit(number, p)
            if 7 in s.holes:
                if s.game.square_c.position == 0:
                    p = [335,389]
                    screen.blit(number, p)
                elif s.game.square_c.position == 1:
                    p = [335,332]
                    screen.blit(number, p)
                elif s.game.square_c.position == 2:
                    p = [389,331]
                    screen.blit(number, p)
                else:
                    p = [389,388]
                    screen.blit(number, p)
            if 8 in s.holes:
                if s.game.square_e.position == 0:
                    p = [283,557]
                    screen.blit(number, p)
                elif s.game.square_e.position == 1:
                    p = [336,557]
                    screen.blit(number, p)
                elif s.game.square_e.position == 2:
                    p = [389,557]
                    screen.blit(number, p)
                else:
                    p = [229,557]
                    screen.blit(number, p)
            if 9 in s.holes:
                if s.game.square_a.position == 0:
                    p = [229,331]
                    screen.blit(number, p)
                elif s.game.square_a.position == 1:
                    p = [282,331]
                    screen.blit(number, p)
                elif s.game.square_a.position == 2:
                    p = [281,388]
                    screen.blit(number, p)
                else:
                    p = [228,389]
                    screen.blit(number, p)
            if 10 in s.holes:
                p = [444,559]
                screen.blit(number, p)
            if 11 in s.holes:
                if s.game.square_c.position == 0:
                    p = [389,331]
                    screen.blit(number, p)
                elif s.game.square_c.position == 1:
                    p = [389,389]
                    screen.blit(number, p)
                elif s.game.square_c.position == 2:
                    p = [336,388]
                    screen.blit(number, p)
                else:
                    p = [335,332]
                    screen.blit(number, p)
            if 12 in s.holes:
                if s.game.square_e.position == 0:
                    p = [231,558]
                    screen.blit(number, p)
                elif s.game.square_e.position == 1:
                    p = [283,557]
                    screen.blit(number, p)
                elif s.game.square_e.position == 2:
                    p = [336,557]
                    screen.blit(number, p)
                else:
                    p = [389,557]
                    screen.blit(number, p)
            if 13 in s.holes:
                if s.game.square_d.position == 0:
                    p = [389,445]
                    screen.blit(number, p)
                elif s.game.square_d.position == 1:
                    p = [389,501]
                    screen.blit(number, p)
                elif s.game.square_d.position == 2:
                    p = [336,503]
                    screen.blit(number, p)
                else:
                    p = [336,445]
                    screen.blit(number, p)
            if 14 in s.holes:
                if s.game.square_e.position == 0:
                    p = [335,558]
                    screen.blit(number, p)
                elif s.game.square_e.position == 1:
                    p = [390,558]
                    screen.blit(number, p)
                elif s.game.square_e.position == 2:
                    p = [229,558]
                    screen.blit(number, p)
                else:
                    p = [283,558]
                    screen.blit(number, p)
            if 15 in s.holes:
                p = [443,331]
                screen.blit(number, p)
            if 16 in s.holes:
                if s.game.square_d.position == 0:
                    p = [336,445]
                    screen.blit(number, p)
                elif s.game.square_d.position == 1:
                    p = [389,445]
                    screen.blit(number, p)
                elif s.game.square_d.position == 2:
                    p = [387,503]
                    screen.blit(number, p)
                else:
                    p = [336,503]
                    screen.blit(number, p)
            if 17 in s.holes:
                p = [444,445]
                screen.blit(number, p)
            if 18 in s.holes:
                number_position = [444,389]
                screen.blit(number, number_position)
            if 19 in s.holes:
                if s.game.square_a.position == 0:
                    p = [281,388]
                    screen.blit(number, p)
                elif s.game.square_a.position == 1:
                    p = [228,388]
                    screen.blit(number, p)
                elif s.game.square_a.position == 2:
                    p = [228,332]
                    screen.blit(number, p)
                else:
                    p = [282,332]
                    screen.blit(number, p)
            if 20 in s.holes:
                p = [443,502]
                screen.blit(number, p)
            if 21 in s.holes:
                if s.game.square_d.position == 0:
                    p = [389,501]
                    screen.blit(number, p)
                elif s.game.square_d.position == 1:
                    p = [335,502]
                    screen.blit(number, p)
                elif s.game.square_d.position == 2:
                    p = [336,446]
                    screen.blit(number, p)
                else:
                    p = [389,446]
                    screen.blit(number, p)
            if 22 in s.holes:
                if s.game.square_c.position == 0:
                    p = [389,388]
                    screen.blit(number, p)
                elif s.game.square_c.position == 1:
                    p = [335,388]
                    screen.blit(number, p)
                elif s.game.square_c.position == 2:
                    p = [336,331]
                    screen.blit(number, p)
                else:
                    p = [389,331]
                    screen.blit(number, p)
            if 23 in s.holes:
                if s.game.square_b.position == 0:
                    p = [283,501]
                    screen.blit(number, p)
                elif s.game.square_b.position == 1:
                    p = [230,501]
                    screen.blit(number, p)
                elif s.game.square_b.position == 2:
                    p = [229,445]
                    screen.blit(number, p)
                else:
                    p = [283,445]
                    screen.blit(number, p)
            if 24 in s.holes:
                if s.game.square_b.position == 0:
                    p = [282,446]
                    screen.blit(number, p)
                elif s.game.square_b.position == 1:
                    p = [283,501]
                    screen.blit(number, p)
                elif s.game.square_b.position == 2:
                    p = [229,502]
                    screen.blit(number, p)
                else:
                    p = [229,446]
                    screen.blit(number, p)
            if 25 in s.holes:
                if s.game.square_b.position == 0:
                    p = [229,446]
                    screen.blit(number, p)
                elif s.game.square_b.position == 1:
                    p = [283,447]
                    screen.blit(number, p)
                elif s.game.square_b.position == 2:
                    p = [282,502]
                    screen.blit(number, p)
                else:
                    p = [229,501]
                    screen.blit(number, p)


    if s.game.magic_squares_feature.position == 1:
        p = [24,660]
        screen.blit(ms_arrow, p)
    if s.game.magic_squares_feature.position == 2:
        p = [62,660]
        screen.blit(ms_arrow, p)
    if s.game.magic_squares_feature.position == 3:
        p = [102,660]
        screen.blit(ms_arrow, p)
    if s.game.magic_squares_feature.position == 4:
        p = [143,660]
        screen.blit(ms_arrow, p)
    if s.game.magic_squares_feature.position >= 5:
        p = [178,654]
        screen.blit(ms_letter, p)
    if s.game.magic_squares_feature.position >= 6:
        p = [228,654]
        screen.blit(ms_letter, p)
    if s.game.magic_squares_feature.position >= 7:
        p = [276,654]
        screen.blit(ms_letter, p)
    if s.game.magic_squares_feature.position >= 8:
        p = [324,654]
        screen.blit(ms_letter, p)
    if s.game.magic_squares_feature.position == 9:
        p = [373,654]
        screen.blit(ms_letter, p)

    if s.game.magic_squares_feature.position >= 5:
        sf = s.game.selection_feature.position 
        if sf <= 6:
            p = [565,559]
            screen.blit(time, p)
        if sf == 1:
            p = [532,578]
            screen.blit(s_arrow, p)
        if sf == 2:
            p = [532,545]
            screen.blit(s_arrow, p)
        if sf == 3:
            p = [532,511]
            screen.blit(s_arrow, p)
        if sf == 4:
            p = [532,477]
            screen.blit(s_arrow, p)
        if sf == 5:
            p = [532,444]
            screen.blit(s_arrow, p)
        if sf == 6:
            p = [532,410]
            screen.blit(s_arrow, p)
        if s.game.ball_count.position == 3:
            s.cancel_delayed(name="blink")
            blink([s,1,1])
        else:
            s.cancel_delayed(name="blink")
        if sf == 3 or sf == 4:
            p = [137,965]
            screen.blit(rollover, p)
            p = [567,492]
            screen.blit(time, p)
        if sf == 5 or sf == 6:
            p = [527,965]
            screen.blit(rollover, p)
            p = [567,423]
            screen.blit(time, p)
        if sf == 7 or sf == 8:
            if sf == 7:
                p = [532,375]
                screen.blit(s_arrow, p)
            if sf == 8:
                p = [532,341]
                screen.blit(s_arrow, p)
            p = [567,354]
            screen.blit(time, p)
            if s.game.ball_count.position == 4:
                s.cancel_delayed(name="blink")
                blink([s,1,1])
            else:
                s.cancel_delayed(name="blink")
        if sf == 9:
            p = [532,306]
            screen.blit(s_arrow, p)
            p = [569,285]
            screen.blit(time, p)
            if s.game.ball_count.position == 5:
                s.cancel_delayed(name="blink")
                blink([s,1,1])
            else:
                s.cancel_delayed(name="blink")

    if s.game.corners.status == True:
        p = [24,381]
        screen.blit(corners, p)

    if s.game.ballyhole.status == True:
        p = [24,433]
        screen.blit(ballyhole, p)

    if s.game.shop_three.status == True:
        if s.game.ball_count.position == 2:
            s.cancel_delayed(name="blink_score")
            blink_score([s,1,1,0])
        else:
            s.cancel_delayed(name="blink_score")
            p = [25,499]
            screen.blit(ballyhole, p)

    if s.game.shop_four.status == True:
        if s.game.ball_count.position == 3:
            s.cancel_delayed(name="blink_score")
            blink_score([s,1,1,1])
        else:
            s.cancel_delayed(name="blink_score")
            p = [25,562]
            screen.blit(ballyhole, p)

    if s.game.extra_ball.position >= 1:
        p = [141,1031]
        screen.blit(eb_number, p)
    if s.game.extra_ball.position >= 2:
        p = [190,1031]
        screen.blit(eb, p)
    if s.game.extra_ball.position >= 3:
        p = [255,1031]
        screen.blit(eb, p)
    if s.game.extra_ball.position >= 4:
        p = [325,1031]
        screen.blit(eb_number, p)
    if s.game.extra_ball.position >= 5:
        p = [374,1031]
        screen.blit(eb, p)
    if s.game.extra_ball.position >= 6:
        p = [439,1031]
        screen.blit(eb, p)
    if s.game.extra_ball.position >= 7:
        p = [511,1033]
        screen.blit(eb_number, p)
    if s.game.extra_ball.position >= 8:
        p = [560,1034]
        screen.blit(eb, p)
    if s.game.extra_ball.position == 9:
        p = [626,1035]
        screen.blit(eb, p)

    if s.game.eb_play.status == True:
        p = [27,1031]
        screen.blit(extra_balls, p)

    if s.game.red_odds.position == 1:
        p = [110,736]
        screen.blit(odds, p)
    elif s.game.red_odds.position == 2:
        p = [182,736]
        screen.blit(odds, p)
    elif s.game.red_odds.position == 3:
        p = [265,736]
        screen.blit(odds, p)
    elif s.game.red_odds.position == 4:
        p = [344,736]
        screen.blit(odds, p)
    elif s.game.red_odds.position == 5:
        p = [404,736]
        screen.blit(odds, p)
    elif s.game.red_odds.position == 6:
        p = [460,736]
        screen.blit(odds, p)
    elif s.game.red_odds.position == 7:
        p = [512,736]
        screen.blit(odds, p)
    elif s.game.red_odds.position == 8:
        p = [564,736]
        screen.blit(odds, p)

    if s.game.yellow_odds.position == 1:
        p = [110,814]
        screen.blit(odds, p)
    elif s.game.yellow_odds.position == 2:
        p = [182,814]
        screen.blit(odds, p)
    elif s.game.yellow_odds.position == 3:
        p = [265,814]
        screen.blit(odds, p)
    elif s.game.yellow_odds.position == 4:
        p = [344,814]
        screen.blit(odds, p)
    elif s.game.yellow_odds.position == 5:
        p = [404,814]
        screen.blit(odds, p)
    elif s.game.yellow_odds.position == 6:
        p = [460,814]
        screen.blit(odds, p)
    elif s.game.yellow_odds.position == 7:
        p = [512,814]
        screen.blit(odds, p)
    elif s.game.yellow_odds.position == 8:
        p = [564,814]
        screen.blit(odds, p)

    if s.game.green_odds.position == 1:
        p = [110,893]
        screen.blit(odds, p)
    elif s.game.green_odds.position == 2:
        p = [182,893]
        screen.blit(odds, p)
    elif s.game.green_odds.position == 3:
        p = [265,893]
        screen.blit(odds, p)
    elif s.game.green_odds.position == 4:
        p = [344,893]
        screen.blit(odds, p)
    elif s.game.green_odds.position == 5:
        p = [404,893]
        screen.blit(odds, p)
    elif s.game.green_odds.position == 6:
        p = [460,893]
        screen.blit(odds, p)
    elif s.game.green_odds.position == 7:
        p = [512,893]
        screen.blit(odds, p)
    elif s.game.green_odds.position == 8:
        p = [564,893]
        screen.blit(odds, p)

    if s.game.tilt.status == True:
        tilt_position = [605,234]
        screen.blit(tilt, tilt_position)

    pygame.display.update()

def blink_score(args):
    dirty_rects = []
    s = args[0]
    b = args[1]
    sl = args[2]
    t = args[3]

    if b == 0:
        if sl == 1:
            if t == 0:
                p = [25,499]
            else:
                p = [25,562]
            dirty_rects.append(screen.blit(ballyhole, p))
        pygame.display.update(dirty_rects)
    else:
        if t == 0:
            dirty_rects.append(screen.blit(bg_gi, (25,499), pygame.Rect(25,499,130,64)))
        else:
            dirty_rects.append(screen.blit(bg_gi, (25,562), pygame.Rect(25,562,130,64)))
        pygame.display.update(dirty_rects)
    b = not b

    args = [s,b,sl,t]

    s.delay(name="blink_score", delay=0.1, handler=blink_score, param=args)


def blink(args):
    dirty_rects = []
    s = args[0]
    b = args[1]
    sl = args[2]

    if b == 0:
        if sl == 1:
            p = [543,664]
            dirty_rects.append(screen.blit(select_now, p))
        pygame.display.update(dirty_rects)
    else:
        dirty_rects.append(screen.blit(bg_gi, (543,664), pygame.Rect(543,664,141,39)))
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
        p = [222,328]
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
        dirty_rects.append(screen.blit(topleft, (241  - num - 20, 332)))
        dirty_rects.append(screen.blit(topright, (278, 339 - num - 10)))
        dirty_rects.append(screen.blit(bottomright, (272  + num + 15, 383)))
        dirty_rects.append(screen.blit(bottomleft, (224, 384 + num + 5)))

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
        p = [222,442]
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
        dirty_rects.append(screen.blit(topleft, (240 - num - 20, 446)))
        dirty_rects.append(screen.blit(topright, (278, 450 - num - 9)))
        dirty_rects.append(screen.blit(bottomright, (278  + num + 10, 498)))
        dirty_rects.append(screen.blit(bottomleft, (224, 500 + num + 8)))
    
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
        p = [333,328]
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
        dirty_rects.append(screen.blit(topleft, (344  - num - 10, 331)))
        dirty_rects.append(screen.blit(topright, (388, 332 - num - 5)))
        dirty_rects.append(screen.blit(bottomright, (380  + num + 15, 382)))
        dirty_rects.append(screen.blit(bottomleft, (333, 382 + num + 6)))
    
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
    
    p = [330,442]
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
        dirty_rects.append(screen.blit(topleft, (339 - num - 10, 446)))
        dirty_rects.append(screen.blit(topright, (385, 454 - num - 13)))
        dirty_rects.append(screen.blit(bottomright, (362  + num + 29, 500)))
        dirty_rects.append(screen.blit(bottomleft, (335, 499 + num + 12)))
    
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
    
    p = [222,549]
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
    dirty_rects.append(screen.blit(topleft, (230 - num - 10, 556)))
    if num > -40:
        dirty_rects.append(screen.blit(topright, (276, 554 - num)))
    else:
        dirty_rects.append(screen.blit(topright, (331, 612 + num)))
    dirty_rects.append(screen.blit(bottomleft, (331 - num - 10, 554)))
    if num > -40:
        dirty_rects.append(screen.blit(bottomright, (386, 556 - num)))
    else:
        dirty_rects.append(screen.blit(bottomright, (222, 612 + num)))
    
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
        dirty_rects.append(screen.blit(bg_gi, (141,1031), pygame.Rect(141,1031,46,29)))
    if s.game.extra_ball.position < 2:
        dirty_rects.append(screen.blit(bg_gi, (190,1031), pygame.Rect(190,1031,63,29)))
    if s.game.extra_ball.position < 3:
        dirty_rects.append(screen.blit(bg_gi, (255,1031), pygame.Rect(255,1031,63,29)))
    if s.game.extra_ball.position < 4:
        dirty_rects.append(screen.blit(bg_gi, (325,1031), pygame.Rect(325,1031,46,29)))
    if s.game.extra_ball.position < 5:
        dirty_rects.append(screen.blit(bg_gi, (374,1031), pygame.Rect(374,1031,63,29)))
    if s.game.extra_ball.position < 6:
        dirty_rects.append(screen.blit(bg_gi, (439,1031), pygame.Rect(439,1031,63,29)))
    if s.game.extra_ball.position < 7:
        dirty_rects.append(screen.blit(bg_gi, (511,1033), pygame.Rect(511,1033,46,29)))
    if s.game.extra_ball.position < 8:
        dirty_rects.append(screen.blit(bg_gi, (560,1034), pygame.Rect(560,1034,63,29)))
    if s.game.extra_ball.position < 9:
        dirty_rects.append(screen.blit(bg_gi, (626,1035), pygame.Rect(626,1035,63,29)))

    pygame.display.update(dirty_rects)

    if num in [0,24,25,49]:
        if s.game.extra_ball.position < 1:
            p = [141,1031]
            dirty_rects.append(screen.blit(eb_number, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [1,15,26,40]:
        if s.game.extra_ball.position < 2:
            p = [190,1031]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [3,4,17,28,29,42]:
        if s.game.extra_ball.position < 3:
            p = [255,1031]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [5,18,30,43]:
        if s.game.extra_ball.position < 4:
            p = [325,1031]
            dirty_rects.append(screen.blit(eb_number, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [7,8,19,32,33,44]:
        if s.game.extra_ball.position < 5:
            p = [374,1031]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [9,10,20,34,35,45]:
        if s.game.extra_ball.position < 6:
            p = [439,1031]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [11,21,36,46]:
        if s.game.extra_ball.position < 7:
            p = [511,1033]
            dirty_rects.append(screen.blit(eb_number, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [12,22,37,47]:
        if s.game.extra_ball.position < 8:
            p = [560,1034]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [2,6,13,16,23,27,31,38,41,48]:
        if s.game.extra_ball.position < 9:
            p = [626,1035]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects) 
            return

def clear_odds(s, num):
    global screen

    dirty_rects = []

    if s.game.yellow_odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (110,814), pygame.Rect(110,814,49,75)))
    if s.game.yellow_odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (182,814), pygame.Rect(182,814,49,75)))
    if s.game.yellow_odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (265,814), pygame.Rect(265,814,49,75)))
    if s.game.yellow_odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (344,814), pygame.Rect(344,814,49,75)))
    if s.game.yellow_odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (404,814), pygame.Rect(404,814,49,75)))
    if s.game.yellow_odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (460,814), pygame.Rect(460,814,49,75)))
    if s.game.yellow_odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (512,814), pygame.Rect(512,814,49,75)))
    if s.game.yellow_odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (564,814), pygame.Rect(564,814,49,75)))

    if s.game.red_odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (110,736), pygame.Rect(110,736,49,75)))
    if s.game.red_odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (182,736), pygame.Rect(182,736,49,75)))
    if s.game.red_odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (265,736), pygame.Rect(265,736,49,75)))
    if s.game.red_odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (344,736), pygame.Rect(344,736,49,75)))
    if s.game.red_odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (404,736), pygame.Rect(404,736,49,75)))
    if s.game.red_odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (460,736), pygame.Rect(460,736,49,75)))
    if s.game.red_odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (512,736), pygame.Rect(512,736,49,75)))
    if s.game.red_odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (564,736), pygame.Rect(564,736,49,75)))

    if s.game.green_odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (110,893), pygame.Rect(110,893,49,75)))
    if s.game.green_odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (182,893), pygame.Rect(182,893,49,75)))
    if s.game.green_odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (265,893), pygame.Rect(265,893,49,75)))
    if s.game.green_odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (344,893), pygame.Rect(344,893,49,75)))
    if s.game.green_odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (404,893), pygame.Rect(404,893,49,75)))
    if s.game.green_odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (460,893), pygame.Rect(460,893,49,75)))
    if s.game.green_odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (512,893), pygame.Rect(512,893,49,75)))
    if s.game.green_odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (564,893), pygame.Rect(564,893,49,75)))

    pygame.display.update(dirty_rects)

def draw_odds_animation(s, num):
    global screen
    dirty_rects = []

    if num in [11,36]:
        if s.game.yellow_odds.position != 1:
            p = [110,814]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [4,29]:
        if s.game.yellow_odds.position != 2:
            p = [182,814]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [7,32]:
        if s.game.yellow_odds.position != 3:
            p = [265,814]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [13,38]:
        if s.game.yellow_odds.position != 4:
            p = [344,814]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [22,47]:
        if s.game.yellow_odds.position != 5:
            p = [404,814]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [17,42]:
        if s.game.yellow_odds.position != 6:
            p = [460,814]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [19,44]:
        if s.game.yellow_odds.position != 7:
            p = [512,814]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [5,30]:
        if s.game.yellow_odds.position != 8:
            p = [564,814]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return

    if num in [0,25]:
        if s.game.red_odds.position != 1:
            p = [110,736]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [15,40]:
        if s.game.red_odds.position != 2:
            p = [182,736]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [24,49]:
        if s.game.red_odds.position != 3:
            p = [265,736]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [9,34]:
        if s.game.red_odds.position != 4:
            p = [344,736]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [20,45]:
        if s.game.red_odds.position != 5:
            p = [404,736]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [12,37]:
        if s.game.red_odds.position != 6:
            p = [460,736]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [50,26]:
        if s.game.red_odds.position != 7:
            p = [512,736]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [6,31]:
        if s.game.red_odds.position != 8:
            p = [564,736]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return

    if num in [16,41]:
        if s.game.green_odds.position != 1:
            p = [110,893]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [18,43]:
        if s.game.green_odds.position != 2:
            p = [182,893]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [14,39]:
        if s.game.green_odds.position != 3:
            p = [265,893]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [3,28]:
        if s.game.green_odds.position != 4:
            p = [344,893]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [23,48]:
        if s.game.green_odds.position != 5:
            p = [404,893]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [8,33]:
        if s.game.green_odds.position != 6:
            p = [460,893]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [22,47]:
        if s.game.green_odds.position != 7:
            p = [512,893]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [10,35]:
        if s.game.green_odds.position != 8:
            p = [564,893]
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
    if s.game.magic_squares_feature.position < 5:
        dirty_rects.append(screen.blit(bg_gi, (178,654), pygame.Rect(178,654,45,53)))
    if s.game.magic_squares_feature.position < 6:
        dirty_rects.append(screen.blit(bg_gi, (228,654), pygame.Rect(228,654,45,53)))
    if s.game.magic_squares_feature.position < 7:
        dirty_rects.append(screen.blit(bg_gi, (276,654), pygame.Rect(276,654,45,53)))
    if s.game.magic_squares_feature.position < 8:
        dirty_rects.append(screen.blit(bg_gi, (324,654), pygame.Rect(324,654,45,53)))
    if s.game.magic_squares_feature.position < 9:
        dirty_rects.append(screen.blit(bg_gi, (373,654), pygame.Rect(373,654,45,53)))

    if s.game.selection_feature.position not in [3,4]:
        dirty_rects.append(screen.blit(bg_gi, (137,965), pygame.Rect(137,965,58,60)))
        dirty_rects.append(screen.blit(bg_gi, (567,492), pygame.Rect(567,492,131,67)))
    if s.game.selection_feature.position not in [5,6]:
        dirty_rects.append(screen.blit(bg_gi, (527,965), pygame.Rect(527,965,58,60)))
        dirty_rects.append(screen.blit(bg_gi, (567,423), pygame.Rect(567,423,131,67)))
    if s.game.ballyhole.status == False:
        dirty_rects.append(screen.blit(bg_gi, (24,433), pygame.Rect(24,433,130,64)))
    if s.game.corners.status == False:
        dirty_rects.append(screen.blit(bg_gi, (24,381), pygame.Rect(24,381,131,53)))
    if s.game.selection_feature.position not in [7,8]:
        dirty_rects.append(screen.blit(bg_gi, (567,354), pygame.Rect(567,354,131,67)))
    if s.game.selection_feature.position != 9:
        dirty_rects.append(screen.blit(bg_gi, (569,285), pygame.Rect(569,285,131,67)))
    if s.game.shop_three.status == False:
        dirty_rects.append(screen.blit(bg_gi, (25,499), pygame.Rect(25,499,130,64)))
    if s.game.shop_four.status == False:
        dirty_rects.append(screen.blit(bg_gi, (25,562), pygame.Rect(25,562,130,64)))
    pygame.display.update(dirty_rects)


def draw_feature_animation(s, num):
    global screen
    dirty_rects = []

    if num in [11,21,36,46]:
        if s.game.magic_squares_feature.position < 6:
            p = [178,654]
            dirty_rects.append(screen.blit(ms_letter, p))
            p = [228,654]
            dirty_rects.append(screen.blit(ms_letter, p))
            pygame.display.update(dirty_rects)
            return
    if num in [16,22,41,47]:
        if s.game.magic_squares_feature.position < 7:
            p = [276,654]
            dirty_rects.append(screen.blit(ms_letter, p))
            pygame.display.update(dirty_rects)
            return
    if num in [14,23,39,48]:
        if s.game.magic_squares_feature.position < 8:
            p = [324,654]
            dirty_rects.append(screen.blit(ms_letter, p))
            pygame.display.update(dirty_rects)
            return
    if num in [9,19,24,34,44,49]:
        if s.game.magic_squares_feature.position < 9:
            p = [373,654]
            dirty_rects.append(screen.blit(ms_letter, p))
            pygame.display.update(dirty_rects)
            return
    if num in [17,42]:
        if s.game.selection_feature.position not in [3,4]:
            p = [137,965]
            dirty_rects.append(screen.blit(rollover, p))
            p = [567,492]
            dirty_rects.append(screen.blit(time, p))
            s.game.coils.yellowROLamp.pulse(85)
            pygame.display.update(dirty_rects)
            return
    if num in [2,27]:
        if s.game.selection_feature.position not in [5,6]:
            p = [527,965]
            dirty_rects.append(screen.blit(rollover, p))
            p = [567,423]
            dirty_rects.append(screen.blit(time, p))
            s.game.coils.redROLamp.pulse(85)
            pygame.display.update(dirty_rects)
            return
    if num in [3,13,28,38]:
        if s.game.ballyhole.status == False:
            p = [24,433]
            dirty_rects.append(screen.blit(ballyhole, p))
            pygame.display.update(dirty_rects)
            return
    if num in [8,18,33,43]:
        if s.game.corners.status == False:
            p = [24,381]
            dirty_rects.append(screen.blit(corners, p))
            pygame.display.update(dirty_rects)
            return
    if num in [10,35]:
        if s.game.selection_feature.position not in [7,8]:
            p = [567,354]
            dirty_rects.append(screen.blit(time, p))
            pygame.display.update(dirty_rects)
            return
    if num in [5,30]:
        if s.game.selection_feature.position != 9:
            p = [569,285]
            dirty_rects.append(screen.blit(time, p))
            pygame.display.update(dirty_rects)
            return
    if num in [4,6,15,29,31,40]:
        if s.game.shop_three.status == False:
            p = [25,499]
            dirty_rects.append(screen.blit(ballyhole, p))
            pygame.display.update(dirty_rects)
            return
    if num in [1,7,12,20,26,32,37,45]:
        if s.game.shop_four.status == False:
            p = [25,562]
            dirty_rects.append(screen.blit(ballyhole, p))
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


def blink(args):
    dirty_rects = []
    s = args[0]
    b = args[1]
    sn = args[2]

    if b == 0:
        if sn == 1:
            p = [543,662]
            dirty_rects.append(screen.blit(select_now, p))
        pygame.display.update(dirty_rects)
    else:
        dirty_rects.append(screen.blit(bg_gi, (543,662), pygame.Rect(543,662,141,39)))
        pygame.display.update(dirty_rects)
    b = not b

    args = [s,b,sn]

    s.delay(name="blink", delay=0.1, handler=blink, param=args)

