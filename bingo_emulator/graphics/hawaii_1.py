
import pygame
import random

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

meter = pygame.image.load('graphics/assets/silver_register_cover.png').convert()
sc_arrow = pygame.image.load('hawaii_1/assets/sc_arrow.png').convert_alpha()
sc = pygame.image.load('hawaii_1/assets/super_card.png').convert_alpha()
eb = pygame.image.load('hawaii_1/assets/eb.png').convert_alpha()
extra_ball = pygame.image.load('hawaii_1/assets/extra_ball.png').convert_alpha()
extra_balls = pygame.image.load('hawaii_1/assets/extra_balls.png').convert_alpha()
o1 = pygame.image.load('hawaii_1/assets/odds1.png').convert_alpha()
o2 = pygame.image.load('hawaii_1/assets/odds2.png').convert_alpha()
o3 = pygame.image.load('hawaii_1/assets/odds3.png').convert_alpha()
o4 = pygame.image.load('hawaii_1/assets/odds4.png').convert_alpha()
o5 = pygame.image.load('hawaii_1/assets/odds5.png').convert_alpha()
o6 = pygame.image.load('hawaii_1/assets/odds6.png').convert_alpha()
o7 = pygame.image.load('hawaii_1/assets/odds7.png').convert_alpha()
o8 = pygame.image.load('hawaii_1/assets/odds8.png').convert_alpha()
star = pygame.image.load('hawaii_1/assets/rollover.png').convert_alpha()
number = pygame.image.load('hawaii_1/assets/number.png').convert_alpha()
sc_number = pygame.image.load('hawaii_1/assets/sc_number.png').convert_alpha()
tilt = pygame.image.load('hawaii_1/assets/tilt.png').convert_alpha()
select_now = pygame.image.load('hawaii_1/assets/select_now.png').convert_alpha()
red_number = pygame.image.load('hawaii_1/assets/red_number.png').convert_alpha()
red_sc_number = pygame.image.load('hawaii_1/assets/red_sc_number.png').convert_alpha()
s_number = pygame.image.load('hawaii_1/assets/spotted_numbers.png').convert_alpha()
s_arrow = pygame.image.load('hawaii_1/assets/selection_arrow.png').convert_alpha()
before_fourth = pygame.image.load('hawaii_1/assets/before_fourth.png').convert_alpha()
super_selection = pygame.image.load('hawaii_1/assets/super_selection.png').convert_alpha()
select_feature = pygame.image.load('hawaii_1/assets/select_feature.png').convert_alpha()
red_select_feature = pygame.image.load('hawaii_1/assets/red_select_feature.png').convert_alpha()
three_four = pygame.image.load('hawaii_1/assets/4_as_5.png').convert_alpha()
letter_ha = pygame.image.load('hawaii_1/assets/letter_ha.png').convert_alpha()
letter_wa = pygame.image.load('hawaii_1/assets/letter_wa.png').convert_alpha()
letter_ii = pygame.image.load('hawaii_1/assets/letter_ii.png').convert_alpha()
lite_a_name = pygame.image.load('hawaii_1/assets/lite_a_name.png').convert_alpha()
return_arrow = pygame.image.load('hawaii_1/assets/return_arrow.png').convert_alpha()
ball_return = pygame.image.load('hawaii_1/assets/return.png').convert_alpha()
corners = pygame.image.load('hawaii_1/assets/diamond_diagonal.png').convert_alpha()
dd = pygame.image.load('hawaii_1/assets/dd.png').convert_alpha()
bg_menu = pygame.image.load('hawaii_1/assets/hawaii_1_menu.png')
bg_gi = pygame.image.load('hawaii_1/assets/hawaii_1_gi.png')
bg_off = pygame.image.load('hawaii_1/assets/hawaii_1_off.png')

class scorereel():
    """ Score Reels are used to count replays """
    def __init__(self, pos, image):
        self.position = pos
        self.default_y = self.position[1]
        self.image = pygame.image.load(image).convert()

reel1 = scorereel([109,837], "graphics/assets/green_reel.png")
reel10 = scorereel([90,837], "graphics/assets/green_reel.png")
reel100 = scorereel([71,837], "graphics/assets/green_reel.png")

def display(s, replays=0, menu=False):
    
    meter.set_colorkey((255,0,252))
    meter_position = [62,835]

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
        p = [212,259]
        screen.blit(letter_ha, p)
        p = [321,260]
        screen.blit(letter_wa, p)
        p = [460,261]
        screen.blit(letter_ii, p)
    else:
        if s.game.lite_a_name.status == True:
            p = [190,305]
            screen.blit(lite_a_name, p)

    if s.game.super_card.position == 1:
        p = [39,370]
        screen.blit(sc_arrow, p)
    if s.game.super_card.position == 2:
        p = [77,370]
        screen.blit(sc_arrow, p)
    if s.game.super_card.position == 3:
        p = [114,370]
        screen.blit(sc_arrow, p)
    if s.game.super_card.position == 4:
        p = [153,370]
        screen.blit(sc_arrow, p)
    if s.game.super_card.position == 5:
        p = [536,370]
        screen.blit(sc_arrow, p)
    if s.game.super_card.position == 6:
        p = [573,372]
        screen.blit(sc_arrow, p)
    if s.game.super_card.position == 7:
        p = [611,372]
        screen.blit(sc_arrow, p)
    if s.game.super_card.position == 8:
        p = [650,372]
        screen.blit(sc_arrow, p)

    if s.game.super_card.position >= 4:
        p = [42,400]
        screen.blit(sc, p)

    if s.game.super_card.position >= 8:
        p = [537,405]
        screen.blit(sc, p)

    if s.game.extra_ball.position == 1:
        eb_position = [95,980]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 2:
        eb_position = [132,980]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 3:
        eb_position = [167,980]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 4:
        eb_position = [202,980]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 5:
        eb_position = [237,980]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 6:
        eb_position = [275,980]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 7:
        eb_position = [311,980]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 8:
        eb_position = [347,980]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 9:
        eb_position = [381,980]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 10:
        eb_position = [415,980]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 11:
        eb_position = [458,980]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 12:
        eb_position = [493,980]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 13:
        eb_position = [527,980]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 14:
        eb_position = [561,980]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 15:
        eb_position = [596,980]
        screen.blit(eb, eb_position)

    if s.game.extra_ball.position >= 5 and s.game.extra_ball.position < 10:
        eb_pos = [92,1008]
        screen.blit(extra_ball, eb_pos)
    if s.game.extra_ball.position >= 10 and s.game.extra_ball.position < 15:
        eb_pos = [273,1008]
        screen.blit(extra_ball, eb_pos)
    if s.game.extra_ball.position == 15:
        eb_pos = [454,1008]
        screen.blit(extra_ball, eb_pos)

    if s.game.odds.position > 0:
        if s.game.odds.position == 1:
            odds_position = [189,827]
            screen.blit(o1, odds_position)
        if s.game.odds.position == 2:
            odds_position = [241,808]
            screen.blit(o2, odds_position)
        if s.game.odds.position == 3:
            odds_position = [257,771]
            screen.blit(o3, odds_position)
        if s.game.odds.position == 4:
            odds_position = [360,825]
            screen.blit(o4, odds_position)
        if s.game.odds.position == 5:
            odds_position = [430,821]
            screen.blit(o5, odds_position)
        if s.game.odds.position == 6:
            odds_position = [513,790]
            screen.blit(o6, odds_position)
        if s.game.odds.position == 7:
            odds_position = [566,773]
            screen.blit(o7, odds_position)
        if s.game.odds.position == 8:
            odds_position = [656,792]
            screen.blit(o8, odds_position)

    if s.game.red_star.status == True:
        rs_position = [652,942]
        screen.blit(star, rs_position)

    if s.game.corners.status == True:
        corners_position = [513,241]
        screen.blit(corners, corners_position)

    if s.game.diamond_diagonal.status == True:
        corners_position = [17,239]
        screen.blit(corners, corners_position)
        if s.game.dd_three_as_four.status == False and s.game.four_as_five.status == False:
            p = [218,334]
            screen.blit(dd, p)
        elif s.game.dd_three_as_four.status == True:
            p = [319,334]
            screen.blit(dd, p)
        elif s.game.dd_three_as_five.status == True:
            p = [418,334]
            screen.blit(dd, p)

    if s.game.tilt.status == False:
        if s.holes:
            if 1 in s.holes:
                number_position = [225,527]
                screen.blit(number, number_position)
                number_position = [552,476]
                screen.blit(sc_number, number_position)
            if 2 in s.holes:
                number_position = [225,473]
                screen.blit(number, number_position)
            if 3 in s.holes:
                number_position = [446,583]
                screen.blit(number, number_position)
                number_position = [95,437]
                screen.blit(sc_number, number_position)
            if 4 in s.holes:
                number_position = [280,366]
                screen.blit(number, number_position)
                number_position = [592,516]
                screen.blit(sc_number, number_position)
            if 5 in s.holes:
                number_position = [337,584]
                screen.blit(number, number_position)
            if 6 in s.holes:
                number_position = [448,366]
                screen.blit(number, number_position)
            if 7 in s.holes:
                number_position = [282,584]
                screen.blit(number, number_position)
                number_position = [592,439]
                screen.blit(sc_number, number_position)
            if 8 in s.holes:
                number_position = [448,419]
                screen.blit(number, number_position)
            if 9 in s.holes:
                number_position = [225,365]
                screen.blit(number, number_position)
                number_position = [54,475]
                screen.blit(sc_number, number_position)
            if 10 in s.holes:
                number_position = [224,419]
                screen.blit(number, number_position)
                number_position = [590,477]
                screen.blit(sc_number, number_position)
            if 11 in s.holes:
                number_position = [225,585]
                screen.blit(number, number_position)
                number_position = [133,475]
                screen.blit(sc_number, number_position)
                number_position = [630,437]
                screen.blit(sc_number, number_position)
            if 12 in s.holes:
                number_position = [393,473]
                screen.blit(number, number_position)
                number_position = [55,513]
                screen.blit(sc_number, number_position)
            if 13 in s.holes:
                number_position = [338,528]
                screen.blit(number, number_position)
                number_position = [630,477]
                screen.blit(sc_number, number_position)
            if 14 in s.holes:
                number_position = [339,420]
                screen.blit(number, number_position)
                number_position = [132,512]
                screen.blit(sc_number, number_position)
            if 15 in s.holes:
                number_position = [337,365]
                screen.blit(number, number_position)
                number_position = [551,437]
                screen.blit(sc_number, number_position)
            if 16 in s.holes:
                number_position = [338,474]
                screen.blit(number, number_position)
            if 17 in s.holes:
                number_position = [446,528]
                screen.blit(number, number_position)
                number_position = [550,515]
                screen.blit(sc_number, number_position)
            if 18 in s.holes:
                number_position = [282,474]
                screen.blit(number, number_position)
                number_position = [134,437]
                screen.blit(sc_number, number_position)
                number_position = [630,515]
                screen.blit(sc_number, number_position)
            if 19 in s.holes:
                number_position = [282,419]
                screen.blit(number, number_position)
            if 20 in s.holes:
                number_position = [394,420]
                screen.blit(number, number_position)
            if 21 in s.holes:
                number_position = [394,528]
                screen.blit(number, number_position)
            if 22 in s.holes:
                number_position = [281,528]
                screen.blit(number, number_position)
            if 23 in s.holes:
                number_position = [393,583]
                screen.blit(number, number_position)
                number_position = [56,436]
                screen.blit(sc_number, number_position)
            if 24 in s.holes:
                number_position = [393,365]
                screen.blit(number, number_position)
                number_position = [95,512]
                screen.blit(sc_number, number_position)
            if 25 in s.holes:
                number_position = [447,473]
                screen.blit(number, number_position)
                number_position = [95,474]
                screen.blit(sc_number, number_position)

    if s.game.tilt.status == True:
        tilt_position = [80,795]
        screen.blit(tilt, tilt_position)

    if s.game.selection_feature.position == 2:
        p = [100,684]
        screen.blit(s_arrow, p)
    if s.game.selection_feature.position == 3:
        p = [140,684]
        screen.blit(s_arrow, p)
    if s.game.selection_feature.position == 4:
        p = [180,684]
        screen.blit(s_arrow, p)
    if s.game.selection_feature.position >= 5:
        p = [215,684]
        screen.blit(s_number, p)
    if s.game.selection_feature.position >= 6:
        p = [254,684]
        screen.blit(s_number, p)
    if s.game.selection_feature.position >= 7:
        p = [295,684]
        screen.blit(s_number, p)
    if s.game.selection_feature.position >= 8:
        p = [334,684]
        screen.blit(s_number, p)
    if s.game.selection_feature.position >= 9:
        p = [374,684]
        screen.blit(s_number, p)
    if s.game.selection_feature.position >= 10:
        p = [412,684]
        screen.blit(s_number, p)
    if s.game.selection_feature.position >= 11:
        p = [453,684]
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
        p = [7,685]
        screen.blit(before_fourth, p)
    if s.game.before_fifth.status == True and (s.game.selection_feature.position > 3 or s.game.selection_feature_relay.status == True):
        p = [624,685]
        screen.blit(before_fourth, p)

    if s.game.before_fourth.status == True:
        if s.game.ball_count.position < 4:
            if s.game.select_spots.status == True:
                if s.game.selection_feature.position >= 5:
                    if s.game.spotted.position == 0:
                        #19
                        number_position = [282,419]
                        screen.blit(red_number, number_position)
                if s.game.selection_feature.position >= 6:
                    if s.game.spotted.position == 1:
                        #20
                        number_position = [394,420]
                        screen.blit(red_number, number_position)
                if s.game.selection_feature.position >= 7:
                    if s.game.spotted.position == 2:
                        #21
                        number_position = [394,528]
                        screen.blit(red_number, number_position)
                if s.game.selection_feature.position >= 8:
                    if s.game.spotted.position == 3:
                        #22
                        number_position = [281,528]
                        screen.blit(red_number, number_position)
                if s.game.selection_feature.position >= 9:
                    if s.game.spotted.position == 4:
                        #16
                        number_position = [338,474]
                        screen.blit(red_number, number_position)
                if s.game.selection_feature.position >= 10:
                    if s.game.spotted.position == 5:
                        #25
                        number_position = [447,473]
                        screen.blit(red_number, number_position)
                        number_position = [95,474]
                        screen.blit(red_sc_number, number_position)
                if s.game.selection_feature.position >= 11:
                    if s.game.spotted.position == 6:
                        #10
                        number_position = [224,419]
                        screen.blit(red_number, number_position)
                        number_position = [590,477]
                        screen.blit(red_sc_number, number_position)
            if s.game.selection_feature_relay.status == True:
                if s.game.spotted.position == 7:
                    p = [98,719]
                    screen.blit(red_select_feature, p)
                if s.game.spotted.position == 8:
                    p = [203,719]
                    screen.blit(red_select_feature, p)
                if s.game.spotted.position == 9:
                    p = [413,719]
                    screen.blit(red_select_feature, p)
                if s.game.spotted.position == 10:
                    p = [517,719]
                    screen.blit(red_select_feature, p)

    if s.game.before_fifth.status == True:
        if s.game.ball_count.position < 5:
            if s.game.select_spots.status == True:
                if s.game.selection_feature.position >= 5:
                    if s.game.spotted.position == 0:
                        #19
                        number_position = [282,419]
                        screen.blit(red_number, number_position)
                if s.game.selection_feature.position >= 6:
                    if s.game.spotted.position == 1:
                        #20
                        number_position = [394,420]
                        screen.blit(red_number, number_position)
                if s.game.selection_feature.position >= 7:
                    if s.game.spotted.position == 2:
                        #21
                        number_position = [394,528]
                        screen.blit(red_number, number_position)
                if s.game.selection_feature.position >= 8:
                    if s.game.spotted.position == 3:
                        #22
                        number_position = [281,528]
                        screen.blit(red_number, number_position)
                if s.game.selection_feature.position >= 9:
                    if s.game.spotted.position == 4:
                        #16
                        number_position = [338,474]
                        screen.blit(red_number, number_position)
                if s.game.selection_feature.position >= 10:
                    if s.game.spotted.position == 5:
                        #25
                        number_position = [447,473]
                        screen.blit(red_number, number_position)
                        number_position = [95,474]
                        screen.blit(red_sc_number, number_position)
                if s.game.selection_feature.position >= 11:
                    if s.game.spotted.position == 6:
                        #10
                        number_position = [224,419]
                        screen.blit(red_number, number_position)
                        number_position = [590,477]
                        screen.blit(red_sc_number, number_position)
            if s.game.selection_feature_relay.status == True:
                if s.game.spotted.position == 7:
                    p = [98,719]
                    screen.blit(red_select_feature, p)
                if s.game.spotted.position == 8:
                    p = [203,719]
                    screen.blit(red_select_feature, p)
                if s.game.spotted.position == 9:
                    p = [413,719]
                    screen.blit(red_select_feature, p)
                if s.game.spotted.position == 10:
                    p = [517,719]
                    screen.blit(red_select_feature, p)
                
    if s.game.selection_feature_relay.status == True:
        p = [98,719]
        screen.blit(select_feature, p)
        p = [203,719]
        screen.blit(select_feature, p)
        p = [310,719]
        screen.blit(super_selection, p)
        p = [413,719]
        screen.blit(select_feature, p)
        p = [517,719]
        screen.blit(select_feature, p)


    if s.game.selection_feature_relay.status == True:
        if s.game.before_fourth.status == True:
            max_ball = 4
        else:
            max_ball = 5
        if s.game.ball_count.position == max_ball:
            if s.game.spotted.position == 8:
                p = [254,640]
                screen.blit(three_four, p)

    if s.game.four_as_five.status == True:
        p = [254,640]
        screen.blit(three_four, p)

    if s.game.eb_play.status == True:
        p = [22,981]
        screen.blit(extra_balls, p)

    if s.game.lite_a_name.status == True:
        if s.game.letter_ha.status == True:
            p = [212,259]
            screen.blit(letter_ha, p)
        if s.game.letter_wa.status == True:
            p = [321,260]
            screen.blit(letter_wa, p)
        if s.game.letter_ii.status == True:
            p = [460,261]
            screen.blit(letter_ii, p)

    if s.game.ball_return.position == 1:
        p = [183,937]
        screen.blit(return_arrow, p)
    if s.game.ball_return.position == 2:
        p = [216,937]
        screen.blit(return_arrow, p)
    if s.game.ball_return.position == 3:
        p = [247,937]
        screen.blit(return_arrow, p)
    if s.game.ball_return.position == 4:
        p = [281,937]
        screen.blit(return_arrow, p)
    if s.game.ball_return.position == 5:
        p = [313,937]
        screen.blit(return_arrow, p)
    if s.game.ball_return.position == 6:
        p = [344,937]
        screen.blit(return_arrow, p)
    if s.game.ball_return.position == 7:
        p = [379,934]
        screen.blit(ball_return, p)

    pygame.display.update()

def blink(args):
    dirty_rects = []
    s = args[0]
    b = args[1]
    sn = args[2]

    if b == 0:
        if sn == 1:
            p = [491,684]
            dirty_rects.append(screen.blit(select_now, p))
        pygame.display.update(dirty_rects)
    else:
        dirty_rects.append(screen.blit(bg_gi, (491,684), pygame.Rect(491,684,130,36)))
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
        dirty_rects.append(screen.blit(bg_gi, (92,1008), pygame.Rect(92,1008,180,35)))
    if s.game.extra_ball.position < 10:
        dirty_rects.append(screen.blit(bg_gi, (273,1008), pygame.Rect(273,1008,180,35)))
    if s.game.extra_ball.position < 15:
        dirty_rects.append(screen.blit(bg_gi, (454,1008), pygame.Rect(454,1008,180,35)))
        dirty_rects.append(screen.blit(bg_gi, (596,980), pygame.Rect(596,980,27,23)))
    pygame.display.update(dirty_rects)

    if num in [1,9,17,4,12,15,21]:
        if s.game.extra_ball.position < 5:
            p = [92,1008]
            dirty_rects.append(screen.blit(extra_ball, p))
            pygame.display.update(dirty_rects) 
    elif num in [2,10,18,5,7,13,16,22]:
        if s.game.extra_ball.position < 10:
            p = [273,1008]
            dirty_rects.append(screen.blit(extra_ball, p))
            pygame.display.update(dirty_rects)
    elif num in [3,11,19,6,8,14,20,23]:
        if s.game.extra_ball.position < 15:
            p = [454,1008]
            dirty_rects.append(screen.blit(extra_ball, p))
            p = [596,980]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)

def clear_odds(s, num):
    global screen
    dirty_rects = []
    if s.game.odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (189,827), pygame.Rect(189,827,41,98)))
    if s.game.odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (241,808), pygame.Rect(241,808,51,105)))
    if s.game.odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (257,771), pygame.Rect(257,771,90,124)))
    if s.game.odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (360,825), pygame.Rect(360,825,64,100)))
    if s.game.odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (430,821), pygame.Rect(430,821,61,94)))
    if s.game.odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (513,790), pygame.Rect(513,790,45,115)))
    if s.game.odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (566,773), pygame.Rect(566,773,53,102)))
    if s.game.odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (656,792), pygame.Rect(656,792,51,129)))

    pygame.display.update(dirty_rects)

def draw_odds_animation(s, num):
    global screen
    dirty_rects = []
    if num in [0,11,17]:
        if s.game.odds.position != 1:
            p = [189,827]
            dirty_rects.append(screen.blit(o1, p))
            pygame.display.update(dirty_rects)
            return
    if num in [1,10,18]:
        if s.game.odds.position != 2:
            p = [241,808]
            dirty_rects.append(screen.blit(o2, p))
            pygame.display.update(dirty_rects)
            return
    if num in [4,12,19]:
        if s.game.odds.position != 3:
            p = [257,771]
            dirty_rects.append(screen.blit(o3, p))
            pygame.display.update(dirty_rects)
            return
    if num in [3,9,20]:
        if s.game.odds.position != 4:
            p = [360,825]
            dirty_rects.append(screen.blit(o4, p))
            pygame.display.update(dirty_rects)
            return
    if num in [5,13,21]:
        if s.game.odds.position != 5:
            p = [430,821]
            dirty_rects.append(screen.blit(o5, p))
            pygame.display.update(dirty_rects)
            return
    if num in [6,14,22]:
        if s.game.odds.position != 6:
            p = [513,790]
            dirty_rects.append(screen.blit(o6, p))
            pygame.display.update(dirty_rects)
            return
    if num in [7,16,23]:
        if s.game.odds.position != 7:
            p = [566,773]
            dirty_rects.append(screen.blit(o7, p))
            pygame.display.update(dirty_rects)
            return
    if num in [8,15,24]:
        if s.game.odds.position != 8:
            p = [656,792]
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

    if s.game.super_card.position < 4:
        dirty_rects.append(screen.blit(bg_gi, (42,400), pygame.Rect(42,400,148,28)))
    if s.game.super_card.position < 8:
        dirty_rects.append(screen.blit(bg_gi, (537,405), pygame.Rect(537,405,148,28)))
    if s.game.corners.status == False:
        dirty_rects.append(screen.blit(bg_gi, (513,241), pygame.Rect(513,241,192,124)))
    if s.game.ball_return.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (379,934), pygame.Rect(379,934,175,40)))
    if s.game.red_star.status == False:
        dirty_rects.append(screen.blit(bg_gi, (652,942), pygame.Rect(652,942,68,94)))
    if s.game.dd_three_as_four.status == False:
        dirty_rects.append(screen.blit(bg_gi, (319,334), pygame.Rect(319,334,93,28)))
    if s.game.dd_three_as_five.status == False:
        dirty_rects.append(screen.blit(bg_gi, (418,334), pygame.Rect(418,334,93,28)))
    if s.game.selection_feature_relay.status == False:
        dirty_rects.append(screen.blit(bg_gi, (310,719), pygame.Rect(310,719,105,50)))
    pygame.display.update(dirty_rects)
    return

def animate_mixer1(s):
    global screen
    dirty_rects = []
    if s.game.super_card.position < 4:
        p = [42,400]
        dirty_rects.append(screen.blit(sc, p))
        pygame.display.update(dirty_rects)
        return

def animate_mixer2(s):
    global screen
    dirty_rects = []
    if s.game.super_card.position < 8:
        p = [537,405]
        dirty_rects.append(screen.blit(sc, p))
    if s.game.dd_three_as_four.status == False:
        p = [319,334]
        dirty_rects.append(screen.blit(dd, p))
    pygame.display.update(dirty_rects)
    return

def animate_mixer3(s):
    global screen
    dirty_rects = []
    if s.game.corners.status == False:
        p = [513,241]
        dirty_rects.append(screen.blit(corners, p))
    if s.game.red_star.status == False:
        p = [652,942]
        dirty_rects.append(screen.blit(star, p))
        s.game.coils.redROLamp.pulse(85)
        s.game.coils.yellowROLamp.pulse(85)
    if s.game.ball_return.position != 7:
        p = [379,934]
        dirty_rects.append(screen.blit(ball_return, p))
    pygame.display.update(dirty_rects)
    return

def animate_mixer4(s):
    global screen
    dirty_rects = []
    if s.game.dd_three_as_five.status == False:
        p = [418,334]
        dirty_rects.append(screen.blit(dd, p))
    if s.game.selection_feature_relay.status == False:
        p = [310,719]
        dirty_rects.append(screen.blit(super_selection, p))
    pygame.display.update(dirty_rects)
    return

def clear_features(s, num):
    global screen
    dirty_rects = []
    if s.game.before_fourth.status == False:
        dirty_rects.append(screen.blit(bg_gi, (7,685), pygame.Rect(7,685,89,62)))
    if s.game.before_fifth.status == False:
        dirty_rects.append(screen.blit(bg_gi, (624,685), pygame.Rect(624,685,89,62)))

    if s.game.selection_feature.position < 2:
        dirty_rects.append(screen.blit(bg_gi, (100,684), pygame.Rect(100,684,33,37)))
    if s.game.selection_feature.position < 3:
        dirty_rects.append(screen.blit(bg_gi, (140,684), pygame.Rect(140,684,33,37)))
    if s.game.selection_feature.position < 4:
        dirty_rects.append(screen.blit(bg_gi, (180,684), pygame.Rect(180,684,33,37)))
    if s.game.selection_feature.position < 6:
        dirty_rects.append(screen.blit(bg_gi, (215,684), pygame.Rect(215,684,38,37)))
        dirty_rects.append(screen.blit(bg_gi, (254,684), pygame.Rect(254,684,38,37)))
    if s.game.selection_feature.position < 7:
        dirty_rects.append(screen.blit(bg_gi, (295,684), pygame.Rect(295,684,38,37)))
    if s.game.selection_feature.position < 8:
        dirty_rects.append(screen.blit(bg_gi, (334,684), pygame.Rect(334,684,38,37)))
    if s.game.selection_feature.position < 9:
        dirty_rects.append(screen.blit(bg_gi, (374,684), pygame.Rect(374,684,38,37)))
    if s.game.selection_feature.position < 10:
        dirty_rects.append(screen.blit(bg_gi, (412,684), pygame.Rect(412,684,38,37)))
    if s.game.selection_feature.position < 11:
        dirty_rects.append(screen.blit(bg_gi, (453,684), pygame.Rect(453,684,38,37)))

    pygame.display.update(dirty_rects)

def draw_feature_animation(s, num):
    global screen
    dirty_rects = []

    if num in [4,15,10,21]:
        if s.game.before_fourth.status == False:
            p = [7,685]
            dirty_rects.append(screen.blit(before_fourth, p))
        if s.game.before_fifth.status == False and s.game.before_fourth.status == True:
            p = [624,685]
            dirty_rects.append(screen.blit(before_fourth, p))
        pygame.display.update(dirty_rects)
        return
   
    if num in [0,11,22]:
        if s.game.selection_feature.position < 2:
            p = [100,684]
            dirty_rects.append(screen.blit(s_arrow, p))
            pygame.display.update(dirty_rects)
            return
    if num in [9,20,23]:
        if s.game.selection_feature.position < 3:
            p = [140,684]
            dirty_rects.append(screen.blit(s_arrow, p))
            pygame.display.update(dirty_rects)
            return
    if num in [1,12,24]:
        if s.game.selection_feature.position < 4:
            p = [180,684]
            dirty_rects.append(screen.blit(s_arrow, p))
            pygame.display.update(dirty_rects)
            return
    if num in [2,13]:
        if s.game.selection_feature.position < 6:
            p = [215,684]
            dirty_rects.append(screen.blit(s_number, p))
            p = [254,684]
            dirty_rects.append(screen.blit(s_number, p))
            pygame.display.update(dirty_rects)
            return
    if num in [3,14,4,15]:
        if s.game.selection_feature.position < 7:
            p = [295,684]
            dirty_rects.append(screen.blit(s_number, p))
        pygame.display.update(dirty_rects)
        return
    if num in [5,16]:
        if s.game.selection_feature.position < 8:
            p = [334,684]
            dirty_rects.append(screen.blit(s_number, p))
        pygame.display.update(dirty_rects)
        return
    if num in [6,17]:
        if s.game.selection_feature.position < 9:
            p = [374,684]
            dirty_rects.append(screen.blit(s_number, p))
            pygame.display.update(dirty_rects)
            return
    if num in [7,18]:
        if s.game.selection_feature.position < 10:
            p = [412,684]
            dirty_rects.append(screen.blit(s_number, p))
            pygame.display.update(dirty_rects)
            return
    if num in [8,19]:
        if s.game.selection_feature.position < 11:
            p = [453,684]
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

