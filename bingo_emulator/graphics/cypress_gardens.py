
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
        backglass = pygame.image.load('cypress_gardens/assets/cypress_gardens_menu.png')
    else:
        if (s.game.anti_cheat.status == True):
            backglass = pygame.image.load('cypress_gardens/assets/cypress_gardens_gi.png')
        else:
            backglass = pygame.image.load('cypress_gardens/assets/cypress_gardens_off.png')
    backglass = pygame.transform.scale(backglass, (720, 1280))
    
    screen.blit(backglass, backglass_position)


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
            p = [543,664]
            screen.blit(select_now, p)
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
                p = [543,664]
                screen.blit(select_now, p)
        if sf == 9:
            p = [532,306]
            screen.blit(s_arrow, p)
            p = [569,285]
            screen.blit(time, p)
            if s.game.ball_count.position == 5:
                p = [543,664]
                screen.blit(select_now, p)

    if s.game.corners.status == True:
        p = [24,381]
        screen.blit(corners, p)

    if s.game.ballyhole.status == True:
        p = [24,433]
        screen.blit(ballyhole, p)

    if s.game.shop_three.status == True:
        p = [25,499]
        screen.blit(ballyhole, p)

    if s.game.shop_four.status == True:
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

    pygame.display.flip()
    pygame.display.update()

def eb_animation(num):
    global screen

    if num == 9:
        p = [141,1031]
        screen.blit(eb_number, p)
        pygame.display.update()
    if num == 8:
        p = [190,1031]
        screen.blit(eb, p)
        pygame.display.update()
    if num == 7:
        p = [255,1031]
        screen.blit(eb, p)
        pygame.display.update()
    if num == 6:
        p = [325,1031]
        screen.blit(eb_number, p)
        pygame.display.update()
    if num == 5:
        p = [374,1031]
        screen.blit(eb, p)
        pygame.display.update()
    if num == 4:
        p = [439,1031]
        screen.blit(eb, p)
        pygame.display.update()
    if num == 3:
        p = [511,1033]
        screen.blit(eb_number, p)
        pygame.display.update()
    if num == 2:
        p = [560,1034]
        screen.blit(eb, p)
        pygame.display.update()
    if num == 1:
        p = [626,1035]
        screen.blit(eb, p)
        pygame.display.update()


def feature_animation(num):
    global screen
    if num == 6:
        p = [24,381]
        screen.blit(corners, p)
        pygame.display.update()

    if num == 3:
        p = [373,654]
        screen.blit(ms_letter, p)
        pygame.display.update()
   

def odds_animation(num):
    global screen

