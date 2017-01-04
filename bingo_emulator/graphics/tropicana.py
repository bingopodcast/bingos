
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
        backglass = pygame.image.load('tropicana/assets/tropicana_menu.png')
    else:
        if (s.game.anti_cheat.status == True):
            backglass = pygame.image.load('tropicana/assets/tropicana_gi.png')
        else:
            backglass = pygame.image.load('tropicana/assets/tropicana_off.png')
    backglass = pygame.transform.scale(backglass, (720, 1280))
    
    screen.blit(backglass, backglass_position)

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

    if (s.game.select_spots.status == True or s.game.selection_feature_relay.status == True) and s.game.before_fourth.status == True and s.game.ball_count.position == 3:
        p = [495,645]
        screen.blit(select_now, p)

    if (s.game.select_spots.status == True or s.game.selection_feature_relay.status == True) and s.game.before_fifth.status == True and s.game.ball_count.position == 4:
        p = [495,645]
        screen.blit(select_now, p)

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

def eb_animation(num):
    global screen
    if num == 9:
        eb_position = [91,994]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 8:
        eb_position = [128,994]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 7:
        eb_position = [163,994]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 6:
        eb_position = [197,994]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 5:
        eb_position = [235,994]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 4:
        eb_position = [274,994]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 3:
        eb_position = [310,994]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 2:
        eb_position = [346,994]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 1:
        eb_position = [382,994]
        screen.blit(eb, eb_position)
        pygame.display.update()


def feature_animation(num):
    global screen
    if num == 6:
        corners_position = [362,612]
        screen.blit(four_five, corners_position)
        pygame.display.update()

    if num == 5:
        rs_position = [650,980]
        screen.blit(star, rs_position)
        pygame.display.update()

    if num == 4:
        rs_position = [650,980]
        screen.blit(star, rs_position)
        pygame.display.update()

    if num == 3:
        p = [36,427]
        screen.blit(special_held, p)
        pygame.display.update()

    if num == 2:
        p = [542,365]
        screen.blit(sc, p)
        pygame.display.update()

    if num == 1:
        p = [38,562]
        screen.blit(sc, p)
        pygame.display.update()


def odds_animation(num):
    global screen
    if num == 5:
        odds_position = [170,768]
        o = pygame.image.load('tropicana/assets/odds1.png').convert_alpha()
        screen.blit(o, odds_position)
        pygame.display.update()
    if num == 4:
        odds_position = [197,832]
        o = pygame.image.load('tropicana/assets/odds2.png').convert_alpha()
        screen.blit(o, odds_position)
        pygame.display.update()
    if num == 3:
        odds_position = [278,737]
        o = pygame.image.load('tropicana/assets/odds3.png').convert_alpha()
        screen.blit(o, odds_position)
        pygame.display.update()
    if num == 2:
        odds_position = [345,753]
        o = pygame.image.load('tropicana/assets/odds4.png').convert_alpha()
        screen.blit(o, odds_position)
        pygame.display.update()
    if num == 1:
        odds_position = [420,816]
        o = pygame.image.load('tropicana/assets/odds5.png').convert_alpha()
        screen.blit(o, odds_position)
        pygame.display.update()
