
import pygame
import random

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

meter = pygame.image.load('graphics/assets/silver_register_cover.png').convert()
sc = pygame.image.load('tropicana/assets/special_card.png').convert_alpha()
eb = pygame.image.load('tropicana/assets/eb.png').convert_alpha()
extra_ball = pygame.image.load('tropicana/assets/extra_ball.png').convert_alpha()
extra_balls = pygame.image.load('tropicana/assets/extra_balls.png').convert_alpha()
o1 = pygame.image.load('tropicana/assets/odds1.png').convert_alpha()
o2 = pygame.image.load('tropicana/assets/odds2.png').convert_alpha()
o3 = pygame.image.load('tropicana/assets/odds3.png').convert_alpha()
o4 = pygame.image.load('tropicana/assets/odds4.png').convert_alpha()
o5 = pygame.image.load('tropicana/assets/odds5.png').convert_alpha()
o6 = pygame.image.load('tropicana/assets/odds6.png').convert_alpha()
o7 = pygame.image.load('tropicana/assets/odds7.png').convert_alpha()
o8 = pygame.image.load('tropicana/assets/odds8.png').convert_alpha()
star = pygame.image.load('tropicana/assets/rollover.png').convert_alpha()
number = pygame.image.load('tropicana/assets/number.png').convert_alpha()
sc_number = pygame.image.load('tropicana/assets/sc_number.png').convert_alpha()
tilt = pygame.image.load('tropicana/assets/tilt.png').convert_alpha()
select_now = pygame.image.load('tropicana/assets/select_now.png').convert_alpha()
red_number = pygame.image.load('tropicana/assets/red_number.png').convert_alpha()
red_sc_number = pygame.image.load('tropicana/assets/red_sc_number.png').convert_alpha()
s_number = pygame.image.load('tropicana/assets/spotted_numbers.png').convert_alpha()
s_arrow = pygame.image.load('tropicana/assets/selection_arrow.png').convert_alpha()
before_fourth = pygame.image.load('tropicana/assets/before_fourth.png').convert_alpha()
super_selection = pygame.image.load('tropicana/assets/super_selection.png').convert_alpha()
select_feature = pygame.image.load('tropicana/assets/select_feature.png').convert_alpha()
red_select_feature = pygame.image.load('tropicana/assets/red_select_feature.png').convert_alpha()
four_five = pygame.image.load('tropicana/assets/4_as_5.png').convert_alpha()
letter_s = pygame.image.load('tropicana/assets/letter_t.png').convert_alpha()
letter_i = pygame.image.load('tropicana/assets/letter_r.png').convert_alpha()
letter_n = pygame.image.load('tropicana/assets/letter_o.png').convert_alpha()
letter_g = pygame.image.load('tropicana/assets/letter_p.png').convert_alpha()
letter_a = pygame.image.load('tropicana/assets/letter_i.png').convert_alpha()
letter_p = pygame.image.load('tropicana/assets/letter_c.png').convert_alpha()
letter_o = pygame.image.load('tropicana/assets/letter_a.png').convert_alpha()
letter_r = pygame.image.load('tropicana/assets/letter_n.png').convert_alpha()
letter_e = pygame.image.load('tropicana/assets/letter_a2.png').convert_alpha()
lite_a_name = pygame.image.load('tropicana/assets/lite_a_name.png').convert_alpha()
return_arrow = pygame.image.load('tropicana/assets/return_arrow.png').convert_alpha()
ball_return = pygame.image.load('tropicana/assets/return.png').convert_alpha()
special_held = pygame.image.load('tropicana/assets/special_held.png').convert_alpha()
bg_menu = pygame.image.load('tropicana/assets/tropicana_menu.png')
bg_gi = pygame.image.load('tropicana/assets/tropicana_gi.png')
bg_off = pygame.image.load('tropicana/assets/tropicana_off.png')

class scorereel():
    """ Score Reels are used to count replays """
    def __init__(self, pos, image):
        self.position = pos
        self.default_y = self.position[1]
        self.image = pygame.image.load(image).convert()

reel1 = scorereel([109,847], "graphics/assets/green_reel.png")
reel10 = scorereel([90,847], "graphics/assets/green_reel.png")
reel100 = scorereel([71,847], "graphics/assets/green_reel.png")

def display(s, replays=0, menu=False):
    
    meter.set_colorkey((255,0,252))
    meter_position = [62,845]

    screen.blit(reel1.image, reel1.position)
    screen.blit(reel10.image, reel10.position)
    screen.blit(reel100.image, reel100.position)
    screen.blit(meter, meter_position)

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

    if s.game.tilt.status == True:
        p = [196,250]
        screen.blit(letter_s, p)
        p = [233,250]
        screen.blit(letter_i, p)
        p = [275,250]
        screen.blit(letter_n, p)
        p = [314,250]
        screen.blit(letter_g, p)
        p = [350,250]
        screen.blit(letter_a, p)
        p = [374,250]
        screen.blit(letter_p, p)
        p = [412,250]
        screen.blit(letter_o, p)
        p = [448,250]
        screen.blit(letter_r, p)
        p = [484,250]
        screen.blit(letter_e, p)
    else:
        if s.game.lite_a_name.status == True:
            p = [180,288]
            screen.blit(lite_a_name, p)

        if s.game.name.position >= 1:
            p = [196,250]
            screen.blit(letter_s, p)
        if s.game.name.position >= 2:
            p = [233,250]
            screen.blit(letter_i, p)
        if s.game.name.position >= 3:
            p = [275,250]
            screen.blit(letter_n, p)
        if s.game.name.position >= 4:
            p = [314,250]
            screen.blit(letter_g, p)
        if s.game.name.position >= 5:
            p = [350,250]
            screen.blit(letter_a, p)
        if s.game.name.position >= 6:
            p = [374,250]
            screen.blit(letter_p, p)
        if s.game.name.position >= 7:
            p = [412,250]
            screen.blit(letter_o, p)
        if s.game.name.position >= 8:
            p = [448,250]
            screen.blit(letter_r, p)
        if s.game.name.position >= 9:
            p = [484,250]
            screen.blit(letter_e, p)

    if s.game.tilt.status == False:
        if s.game.super_card.position >= 1:
            p = [38,365]
            screen.blit(sc, p)
        if s.game.super_card.position >= 2:
            p = [542,365]
            screen.blit(sc, p)
        if s.game.super_card.position >= 3:
            p = [38,562]
            screen.blit(sc, p)
            if s.game.super_card3_hold.status == True:
                p = [36,427]
                screen.blit(special_held, p)
        if s.game.super_card.position >= 4:
            p = [545,561]
            screen.blit(sc, p)
            if s.game.super_card4_hold.status == True:
                p = [543,427]
                screen.blit(special_held, p)

    if s.game.extra_ball.position == 1:
        eb_position = [91,994]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 2:
        eb_position = [128,994]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 3:
        eb_position = [163,994]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 4:
        eb_position = [197,994]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 5:
        eb_position = [235,994]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 6:
        eb_position = [274,994]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 7:
        eb_position = [310,994]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 8:
        eb_position = [346,994]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 9:
        eb_position = [382,994]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 10:
        eb_position = [417,994]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 11:
        eb_position = [457,994]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 12:
        eb_position = [493,994]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 13:
        eb_position = [525,994]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 14:
        eb_position = [562,992]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 15:
        eb_position = [598,992]
        screen.blit(eb, eb_position)

    if s.game.extra_ball.position >= 5 and s.game.extra_ball.position < 10:
        eb_pos = [93,1026]
        screen.blit(extra_ball, eb_pos)
    if s.game.extra_ball.position >= 10 and s.game.extra_ball.position < 15:
        eb_pos = [277,1024]
        screen.blit(extra_ball, eb_pos)
    if s.game.extra_ball.position == 15:
        eb_pos = [455,1023]
        screen.blit(extra_ball, eb_pos)

    if s.game.odds.position > 0:
        if s.game.odds.position == 1:
            odds_position = [170,768]
            screen.blit(o1, odds_position)
        if s.game.odds.position == 2:
            odds_position = [197,832]
            screen.blit(o2, odds_position)
        if s.game.odds.position == 3:
            odds_position = [278,737]
            screen.blit(o3, odds_position)
        if s.game.odds.position == 4:
            odds_position = [345,753]
            screen.blit(o4, odds_position)
        if s.game.odds.position == 5:
            odds_position = [420,816]
            screen.blit(o5, odds_position)
        if s.game.odds.position == 6:
            odds_position = [458,738]
            screen.blit(o6, odds_position)
        if s.game.odds.position == 7:
            odds_position = [546,733]
            screen.blit(o7, odds_position)
        if s.game.odds.position == 8:
            odds_position = [588,760]
            screen.blit(o8, odds_position)

    if s.game.red_star.status == True:
        rs_position = [650,980]
        screen.blit(star, rs_position)

    if s.game.corners.status == True:
        corners_position = [362,612]
        screen.blit(four_five, corners_position)

    if s.game.tilt.status == False:
        if s.holes:
            if 1 in s.holes:
                number_position = [221,500]
                screen.blit(number, number_position)
                number_position = [566,277]
                screen.blit(sc_number, number_position)
            if 2 in s.holes:
                number_position = [221,445]
                screen.blit(number, number_position)
                number_position = [65,275]
                screen.blit(sc_number, number_position)
            if 3 in s.holes:
                number_position = [448,553]
                screen.blit(number, number_position)
                number_position = [569,467]
                screen.blit(sc_number, number_position)
            if 4 in s.holes:
                number_position = [278,330]
                screen.blit(number, number_position)
                number_position = [569,323]
                screen.blit(sc_number, number_position)
            if 5 in s.holes:
                number_position = [334,554]
                screen.blit(number, number_position)
            if 6 in s.holes:
                number_position = [446,332]
                screen.blit(number, number_position)
                number_position = [114,320]
                screen.blit(sc_number, number_position)
            if 7 in s.holes:
                number_position = [278,556]
                screen.blit(number, number_position)
                number_position = [65,470]
                screen.blit(sc_number, number_position)
            if 8 in s.holes:
                number_position = [446,387]
                screen.blit(number, number_position)
            if 9 in s.holes:
                number_position = [222,332]
                screen.blit(number, number_position)
                number_position = [115,274]
                screen.blit(sc_number, number_position)
            if 10 in s.holes:
                number_position = [222,388]
                screen.blit(number, number_position)
                number_position = [65,520]
                screen.blit(sc_number, number_position)
            if 11 in s.holes:
                number_position = [221,554]
                screen.blit(number, number_position)
                number_position = [569,517]
                screen.blit(sc_number, number_position)
            if 12 in s.holes:
                number_position = [392,440]
                screen.blit(number, number_position)
                number_position = [613,277]
                screen.blit(sc_number, number_position)
            if 13 in s.holes:
                number_position = [334,495]
                screen.blit(number, number_position)
            if 14 in s.holes:
                number_position = [335,383]
                screen.blit(number, number_position)
                number_position = [113,468]
                screen.blit(sc_number, number_position)
            if 15 in s.holes:
                number_position = [334,329]
                screen.blit(number, number_position)
            if 16 in s.holes:
                number_position = [335,440]
                screen.blit(number, number_position)
            if 17 in s.holes:
                number_position = [446,498]
                screen.blit(number, number_position)
                number_position = [65,323]
                screen.blit(sc_number, number_position)
            if 18 in s.holes:
                number_position = [278,441]
                screen.blit(number, number_position)
                number_position = [617,468]
                screen.blit(sc_number, number_position)
            if 19 in s.holes:
                number_position = [276,384]
                screen.blit(number, number_position)
            if 20 in s.holes:
                number_position = [392,384]
                screen.blit(number, number_position)
            if 21 in s.holes:
                number_position = [392,498]
                screen.blit(number, number_position)
            if 22 in s.holes:
                number_position = [280,498]
                screen.blit(number, number_position)
            if 23 in s.holes:
                number_position = [391,553]
                screen.blit(number, number_position)
                number_position = [112,517]
                screen.blit(sc_number, number_position)
            if 24 in s.holes:
                number_position = [390,330]
                screen.blit(number, number_position)
                number_position = [614,324]
                screen.blit(sc_number, number_position)
            if 25 in s.holes:
                number_position = [445,445]
                screen.blit(number, number_position)
                number_position = [618,518]
                screen.blit(sc_number, number_position)

    if s.game.tilt.status == True:
        tilt_position = [80,775]
        screen.blit(tilt, tilt_position)

    if s.game.selection_feature.position == 2:
        p = [100,646]
        screen.blit(s_arrow, p)
    if s.game.selection_feature.position == 3:
        p = [140,645]
        screen.blit(s_arrow, p)
    if s.game.selection_feature.position == 4:
        p = [180,645]
        screen.blit(s_arrow, p)
    if s.game.selection_feature.position >= 5:
        p = [213,645]
        screen.blit(s_number, p)
    if s.game.selection_feature.position >= 6:
        p = [252,645]
        screen.blit(s_number, p)
    if s.game.selection_feature.position >= 7:
        p = [291,645]
        screen.blit(s_number, p)
    if s.game.selection_feature.position >= 8:
        p = [332,645]
        screen.blit(s_number, p)
    if s.game.selection_feature.position >= 9:
        p = [372,645]
        screen.blit(s_number, p)
    if s.game.selection_feature.position >= 10:
        p = [413,645]
        screen.blit(s_number, p)
    if s.game.selection_feature.position >= 11:
        p = [451,645]
        screen.blit(s_number, p)

    if (s.game.select_spots.status == True or s.game.selection_feature_relay.status == True):
        if s.game.before_fourth.status == True:
            if s.game.ball_count.position == 3:
                s.cancel_delayed(name="blink")
                blink([s,1,1])
            else:
                s.cancel_delayed(name="blink")

    if (s.game.select_spots.status == True or s.game.selection_feature_relay.status == True):
        if s.game.before_fifth.status == True:
            if s.game.ball_count.position == 4:
                s.cancel_delayed(name="blink")
                blink([s,1,1])
            else:
                s.cancel_delayed(name="blink")

    if s.game.before_fourth.status == True and (s.game.selection_feature.position > 3 or s.game.selection_feature_relay.status == True):
        p = [3,622]
        screen.blit(before_fourth, p)
    if s.game.before_fifth.status == True and (s.game.selection_feature.position > 3 or s.game.selection_feature_relay.status == True):
        p = [626,622]
        screen.blit(before_fourth, p)

    if s.game.before_fourth.status == True:
        if s.game.ball_count.position < 4:
            if s.game.select_spots.status == True:
                if s.game.selection_feature.position >= 5:
                    if s.game.spotted.position == 0:
                        #19
                        number_position = [276,384]
                        screen.blit(red_number, number_position)
                if s.game.selection_feature.position >= 6:
                    if s.game.spotted.position == 1:
                        #20
                        number_position = [392,384]
                        screen.blit(red_number, number_position)
                if s.game.selection_feature.position >= 7:
                    if s.game.spotted.position == 2:
                        #21
                        number_position = [392,498]
                        screen.blit(red_number, number_position)
                if s.game.selection_feature.position >= 8:
                    if s.game.spotted.position == 3:
                        #22
                        number_position = [280,498]
                        screen.blit(red_number, number_position)
                if s.game.selection_feature.position >= 9:
                    if s.game.spotted.position == 4:
                        #16
                        number_position = [335,440]
                        screen.blit(red_number, number_position)
                if s.game.selection_feature.position >= 10:
                    if s.game.spotted.position == 5:
                        #25
                        number_position = [445,445]
                        screen.blit(red_number, number_position)
                        number_position = [618,518]
                        screen.blit(red_sc_number, number_position)
                if s.game.selection_feature.position >= 11:
                    if s.game.spotted.position == 6:
                        #10
                        number_position = [222,388]
                        screen.blit(red_number, number_position)
                        number_position = [65,520]
                        screen.blit(red_sc_number, number_position)
            if s.game.selection_feature_relay.status == True:
                if s.game.spotted.position == 7:
                    p = [98,689]
                    screen.blit(red_select_feature, p)
                if s.game.spotted.position == 8:
                    p = [202,689]
                    screen.blit(red_select_feature, p)
                if s.game.spotted.position == 9:
                    p = [416,689]
                    screen.blit(red_select_feature, p)
                if s.game.spotted.position == 10:
                    p = [522,689]
                    screen.blit(red_select_feature, p)

    if s.game.before_fifth.status == True:
        if s.game.ball_count.position < 5:
            if s.game.select_spots.status == True:
                if s.game.selection_feature.position >= 5:
                    if s.game.spotted.position == 0:
                        #19
                        number_position = [276,384]
                        screen.blit(red_number, number_position)
                if s.game.selection_feature.position >= 6:
                    if s.game.spotted.position == 1:
                        #20
                        number_position = [392,384]
                        screen.blit(red_number, number_position)
                if s.game.selection_feature.position >= 7:
                    if s.game.spotted.position == 2:
                        #21
                        number_position = [392,498]
                        screen.blit(red_number, number_position)
                if s.game.selection_feature.position >= 8:
                    if s.game.spotted.position == 3:
                        #22
                        number_position = [280,498]
                        screen.blit(red_number, number_position)
                if s.game.selection_feature.position >= 9:
                    if s.game.spotted.position == 4:
                        #16
                        number_position = [335,440]
                        screen.blit(red_number, number_position)
                if s.game.selection_feature.position >= 10:
                    if s.game.spotted.position == 5:
                        #25
                        number_position = [445,445]
                        screen.blit(red_number, number_position)
                        number_position = [618,518]
                        screen.blit(red_sc_number, number_position)
                if s.game.selection_feature.position >= 11:
                    if s.game.spotted.position == 6:
                        #10
                        number_position = [222,388]
                        screen.blit(red_number, number_position)
                        number_position = [65,520]
                        screen.blit(red_sc_number, number_position)
            if s.game.selection_feature_relay.status == True:
                if s.game.spotted.position == 7:
                    p = [98,689]
                    screen.blit(red_select_feature, p)
                if s.game.spotted.position == 8:
                    p = [202,689]
                    screen.blit(red_select_feature, p)
                if s.game.spotted.position == 9:
                    p = [416,689]
                    screen.blit(red_select_feature, p)
                if s.game.spotted.position == 10:
                    p = [522,689]
                    screen.blit(red_select_feature, p)

                                
    if s.game.selection_feature_relay.status == True:
        p = [98,689]
        screen.blit(select_feature, p)
        p = [202,689]
        screen.blit(select_feature, p)
        p = [310,684]
        screen.blit(super_selection, p)
        p = [416,689]
        screen.blit(select_feature, p)
        p = [522,689]
        screen.blit(select_feature, p)


    if s.game.selection_feature_relay.status == True:
        if s.game.before_fourth.status == True:
            max_ball = 4
        else:
            max_ball = 5
        if s.game.ball_count.position == max_ball:
            if s.game.spotted.position == 8:
                p = [169,612]
                screen.blit(four_five, p)

    if s.game.four_as_five.status == True:
        p = [169,612]
        screen.blit(four_five, p)

    if s.game.eb_play.status == True:
        p = [26,998]
        screen.blit(extra_balls, p)

    if s.game.ball_return.position == 1:
        p = [180,953]
        screen.blit(return_arrow, p)
    if s.game.ball_return.position == 2:
        p = [213,953]
        screen.blit(return_arrow, p)
    if s.game.ball_return.position == 3:
        p = [245,953]
        screen.blit(return_arrow, p)
    if s.game.ball_return.position == 4:
        p = [280,953]
        screen.blit(return_arrow, p)
    if s.game.ball_return.position == 5:
        p = [312,953]
        screen.blit(return_arrow, p)
    if s.game.ball_return.position == 6:
        p = [345,953]
        screen.blit(return_arrow, p)
    if s.game.ball_return.position == 7:
        p = [380,945]
        screen.blit(ball_return, p)

    pygame.display.update()

def blink(args):
    dirty_rects = []
    s = args[0]
    b = args[1]
    sn = args[2]

    if b == 0:
        if sn == 1:
            p = [495,645]
            dirty_rects.append(screen.blit(select_now, p))
        pygame.display.update(dirty_rects)
    else:
        dirty_rects.append(screen.blit(bg_gi, (495,645), pygame.Rect(495,645,134,40)))
        pygame.display.update(dirty_rects)
    b = not b

    args = [s,b,sn]

    s.delay(name="blink", delay=0.1, handler=blink, param=args)

def eb_animation(args):
    global screen
    dirty_rects = []
    s = args[0]
    num = args[1]
    if s.game.extra_ball.position < 5:
        dirty_rects.append(screen.blit(bg_gi, (93,1026), pygame.Rect(93,1026,176,36)))
    if s.game.extra_ball.position < 10:
        dirty_rects.append(screen.blit(bg_gi, (277,1024), pygame.Rect(277,1024,176,36)))
    if s.game.extra_ball.position < 15:
        dirty_rects.append(screen.blit(bg_gi, (455,1023), pygame.Rect(455,1023,176,36)))
        dirty_rects.append(screen.blit(bg_gi, (598,992), pygame.Rect(598,992,37,31)))
    pygame.display.update(dirty_rects)

    if num in [1,9,17,4,12,15,21]:
        if s.game.extra_ball.position < 5:
            p = [93,1026]
            dirty_rects.append(screen.blit(extra_ball, p))
            pygame.display.update(dirty_rects) 
    elif num in [2,10,18,5,7,13,16,22]:
        if s.game.extra_ball.position < 10:
            p = [277,1024]
            dirty_rects.append(screen.blit(extra_ball, p))
            pygame.display.update(dirty_rects)
    elif num in [3,11,19,6,8,14,20,23]:
        if s.game.extra_ball.position < 15:
            p = [455,1023]
            dirty_rects.append(screen.blit(extra_ball, p))
            p = [598,992]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)

def clear_odds(s, num):
    global screen
    dirty_rects = []
    if s.game.odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (170,768), pygame.Rect(170,768,38,101)))
    if s.game.odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (197,832), pygame.Rect(197,832,56,90)))
    if s.game.odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (278,737), pygame.Rect(278,737,49,90)))
    if s.game.odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (345,753), pygame.Rect(345,753,55,103)))
    if s.game.odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (420,816), pygame.Rect(420,816,39,99)))
    if s.game.odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (458,738), pygame.Rect(458,738,52,104)))
    if s.game.odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (546,733), pygame.Rect(546,733,59,94)))
    if s.game.odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (588,760), pygame.Rect(588,760,56,109)))

    pygame.display.update(dirty_rects)

def draw_odds_animation(s, num):
    global screen
    dirty_rects = []
    if num in [0,11,17]:
        if s.game.odds.position != 1:
            p = [170,768]
            dirty_rects.append(screen.blit(o1, p))
            pygame.display.update(dirty_rects)
            return
    if num in [1,10,18]:
        if s.game.odds.position != 2:
            p = [197,832]
            dirty_rects.append(screen.blit(o2, p))
            pygame.display.update(dirty_rects)
            return
    if num in [4,12,19]:
        if s.game.odds.position != 3:
            p = [278,737]
            dirty_rects.append(screen.blit(o3, p))
            pygame.display.update(dirty_rects)
            return
    if num in [3,9,20]:
        if s.game.odds.position != 4:
            p = [345,753]
            dirty_rects.append(screen.blit(o4, p))
            pygame.display.update(dirty_rects)
            return
    if num in [5,13,21]:
        if s.game.odds.position != 5:
            p = [420,816]
            dirty_rects.append(screen.blit(o5, p))
            pygame.display.update(dirty_rects)
            return
    if num in [6,14,22]:
        if s.game.odds.position != 6:
            p = [458,738]
            dirty_rects.append(screen.blit(o6, p))
            pygame.display.update(dirty_rects)
            return
    if num in [7,16,23]:
        if s.game.odds.position != 7:
            p = [546,733]
            dirty_rects.append(screen.blit(o7, p))
            pygame.display.update(dirty_rects)
            return
    if num in [8,15,24]:
        if s.game.odds.position != 8:
            p = [588,760]
            dirty_rects.append(screen.blit(o8, p))
            pygame.display.update(dirty_rects)
            return

def odds_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]

    clear_odds(s, num)

    draw_odds_animation(s, num)

def clear_mixers(s):
    global screen
    dirty_rects = []

    if s.game.super_card.position < 3:
        dirty_rects.append(screen.blit(bg_gi, (38,562), pygame.Rect(38,562,138,58)))
    if s.game.super_card.position < 4:
        dirty_rects.append(screen.blit(bg_gi, (545,561), pygame.Rect(545,561,138,58)))
    if s.game.corners.status == False:
        dirty_rects.append(screen.blit(bg_gi, (362,612), pygame.Rect(362,612,191,34)))
    if s.game.ball_return.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (380,945), pygame.Rect(380,945,179,44)))
    if s.game.red_star.status == False:
        dirty_rects.append(screen.blit(bg_gi, (650,980), pygame.Rect(650,980,61,65)))
    if s.game.selection_feature_relay.status == False:
        dirty_rects.append(screen.blit(bg_gi, (310,684), pygame.Rect(310,684,103,51)))
    pygame.display.update(dirty_rects)
    return

def animate_mixer1(s):
    return

def animate_mixer2(s):
    global screen
    dirty_rects = []
    if s.game.super_card.position < 3:
        p = [38,562]
        dirty_rects.append(screen.blit(sc, p))
    if s.game.super_card.position < 4:
        p = [545,561]
        dirty_rects.append(screen.blit(sc, p))
    if s.game.ball_return.position != 7:
        p = [380,945]
        dirty_rects.append(screen.blit(ball_return, p))
    pygame.display.update(dirty_rects)
    return

def animate_mixer3(s):
    global screen
    dirty_rects = []
    if s.game.corners.status == False:
        p = [362,612]
        dirty_rects.append(screen.blit(four_five, p))
    if s.game.red_star.status == False:
        p = [650,980]
        dirty_rects.append(screen.blit(star, p))
        s.game.coils.redROLamp.pulse(85)
        s.game.coils.yellowROLamp.pulse(85)
    pygame.display.update(dirty_rects)
    return


def animate_mixer4(s):
    global screen
    dirty_rects = []
    if s.game.selection_feature_relay.status == False:
        p = [310,684]
        dirty_rects.append(screen.blit(super_selection, p))
    pygame.display.update(dirty_rects)
    return

def clear_features(s, num):
    global screen
    dirty_rects = []
    if s.game.before_fourth.status == False:
        dirty_rects.append(screen.blit(bg_gi, (3,622), pygame.Rect(3,622,89,64)))
    if s.game.before_fifth.status == False:
        dirty_rects.append(screen.blit(bg_gi, (626,622), pygame.Rect(626,622,89,64)))
    if s.game.selection_feature.position < 2:
        dirty_rects.append(screen.blit(bg_gi, (100,646), pygame.Rect(100,646,32,33)))
    if s.game.selection_feature.position < 3:
        dirty_rects.append(screen.blit(bg_gi, (140,645), pygame.Rect(140,645,32,33)))
    if s.game.selection_feature.position < 4:
        dirty_rects.append(screen.blit(bg_gi, (180,645), pygame.Rect(180,645,32,33)))
    if s.game.selection_feature.position < 6:
        dirty_rects.append(screen.blit(bg_gi, (213,645), pygame.Rect(213,645,42,39)))
        dirty_rects.append(screen.blit(bg_gi, (252,645), pygame.Rect(252,645,42,39)))
    if s.game.selection_feature.position < 7:
        dirty_rects.append(screen.blit(bg_gi, (291,645), pygame.Rect(291,645,42,39)))
    if s.game.selection_feature.position < 8:
        dirty_rects.append(screen.blit(bg_gi, (332,645), pygame.Rect(332,645,42,39)))
    if s.game.selection_feature.position < 9:
        dirty_rects.append(screen.blit(bg_gi, (372,645), pygame.Rect(372,645,42,39)))
    if s.game.selection_feature.position < 10:
        dirty_rects.append(screen.blit(bg_gi, (413,645), pygame.Rect(413,645,42,39)))
    if s.game.selection_feature.position < 11:
        dirty_rects.append(screen.blit(bg_gi, (451,645), pygame.Rect(451,645,42,39)))

    pygame.display.update(dirty_rects)

def draw_feature_animation(s, num):
    global screen
    dirty_rects = []

    if num in [4,15,10,21]:
        if s.game.before_fourth.status == False:
            p = [3,622]
            dirty_rects.append(screen.blit(before_fourth, p))
        if s.game.before_fifth.status == False and s.game.before_fourth.status == True:
            p = [626,622]
            dirty_rects.append(screen.blit(before_fourth, p))
        pygame.display.update(dirty_rects)
        return
    if num in [0,11,22]:
        if s.game.selection_feature.position < 2:
            p = [100,646]
            dirty_rects.append(screen.blit(s_arrow, p))
            pygame.display.update(dirty_rects)
            return
    if num in [9,20,23]:
        if s.game.selection_feature.position < 3:
            p = [140,645]
            dirty_rects.append(screen.blit(s_arrow, p))
            pygame.display.update(dirty_rects)
            return
    if num in [1,12,24]:
        if s.game.selection_feature.position < 4:
            p = [180,645]
            dirty_rects.append(screen.blit(s_arrow, p))
            pygame.display.update(dirty_rects)
            return
    if num in [2,13]:
        if s.game.selection_feature.position < 6:
            p = [213,645]
            dirty_rects.append(screen.blit(s_number, p))
            p = [252,645]
            dirty_rects.append(screen.blit(s_number, p))
            pygame.display.update(dirty_rects)
            return
    if num in [3,14,4,15]:
        if s.game.selection_feature.position < 7:
            p = [291,645]
            dirty_rects.append(screen.blit(s_number, p))
        pygame.display.update(dirty_rects)
        return
    if num in [5,16]:
        if s.game.selection_feature.position < 8:
            p = [332,645]
            dirty_rects.append(screen.blit(s_number, p))
        pygame.display.update(dirty_rects)
        return
    if num in [6,17]:
        if s.game.selection_feature.position < 9:
            p = [372,645]
            dirty_rects.append(screen.blit(s_number, p))
            pygame.display.update(dirty_rects)
            return
    if num in [7,18]:
        if s.game.selection_feature.position < 10:
            p = [413,645]
            dirty_rects.append(screen.blit(s_number, p))
            pygame.display.update(dirty_rects)
            return
    if num in [8,19]:
        if s.game.selection_feature.position < 11:
            p = [451,645]
            dirty_rects.append(screen.blit(s_number, p))
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

    if num % 2 == 0:
        clear_mixers(s)

    draw_odds_animation(s, num)
    draw_feature_animation(s, num)

