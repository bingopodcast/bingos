
import pygame
import random

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

meter = pygame.image.load('graphics/assets/silver_register_cover.png').convert()
sc_arrow = pygame.image.load('nevada/assets/sc_arrow.png').convert_alpha()
sc = pygame.image.load('nevada/assets/super_card.png').convert_alpha()
eb = pygame.image.load('nevada/assets/eb.png').convert_alpha()
extra_ball = pygame.image.load('nevada/assets/extra_ball.png').convert_alpha()
extra_balls = pygame.image.load('nevada/assets/extra_balls.png').convert_alpha()
o1 = pygame.image.load('nevada/assets/odds1.png').convert_alpha()
o2 = pygame.image.load('nevada/assets/odds2.png').convert_alpha()
o3 = pygame.image.load('nevada/assets/odds3.png').convert_alpha()
o4 = pygame.image.load('nevada/assets/odds4.png').convert_alpha()
o5 = pygame.image.load('nevada/assets/odds5.png').convert_alpha()
o6 = pygame.image.load('nevada/assets/odds6.png').convert_alpha()
o7 = pygame.image.load('nevada/assets/odds7.png').convert_alpha()
o8 = pygame.image.load('nevada/assets/odds8.png').convert_alpha()
star = pygame.image.load('nevada/assets/rollover.png').convert_alpha()
number = pygame.image.load('nevada/assets/number.png').convert_alpha()
sc_number = pygame.image.load('nevada/assets/sc_number.png').convert_alpha()
tilt = pygame.image.load('nevada/assets/tilt.png').convert_alpha()
select_now = pygame.image.load('nevada/assets/select_now.png').convert_alpha()
red_number = pygame.image.load('nevada/assets/red_number.png').convert_alpha()
red_sc_number = pygame.image.load('nevada/assets/red_sc_number.png').convert_alpha()
s_number = pygame.image.load('nevada/assets/spotted_numbers.png').convert_alpha()
s_arrow = pygame.image.load('nevada/assets/selection_arrow.png').convert_alpha()
before_fourth = pygame.image.load('nevada/assets/before_fourth.png').convert_alpha()
super_selection = pygame.image.load('nevada/assets/super_selection.png').convert_alpha()
select_feature = pygame.image.load('nevada/assets/select_feature.png').convert_alpha()
red_select_feature = pygame.image.load('nevada/assets/red_select_feature.png').convert_alpha()
three_four = pygame.image.load('nevada/assets/4_as_5.png').convert_alpha()
letter_n = pygame.image.load('nevada/assets/letter_n.png').convert_alpha()
letter_e = pygame.image.load('nevada/assets/letter_e.png').convert_alpha()
letter_v = pygame.image.load('nevada/assets/letter_v.png').convert_alpha()
letter_a = pygame.image.load('nevada/assets/letter_a.png').convert_alpha()
letter_d = pygame.image.load('nevada/assets/letter_d.png').convert_alpha()
letter_a2 = pygame.image.load('nevada/assets/letter_a2.png').convert_alpha()
lite_a_name = pygame.image.load('nevada/assets/lite_a_name.png').convert_alpha()
return_arrow = pygame.image.load('nevada/assets/return_arrow.png').convert_alpha()
ball_return = pygame.image.load('nevada/assets/return.png').convert_alpha()
corners = pygame.image.load('nevada/assets/diamond_diagonal.png').convert_alpha()
dd = pygame.image.load('nevada/assets/dd.png').convert_alpha()
super_card_scores = pygame.image.load('nevada/assets/super_card_scores.png').convert_alpha()
bg_menu = pygame.image.load('nevada/assets/nevada_menu.png')
bg_gi = pygame.image.load('nevada/assets/nevada_gi.png')
bg_off = pygame.image.load('nevada/assets/nevada_off.png')

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
        p = [203,259]
        screen.blit(letter_n, p)
        p = [261,260]
        screen.blit(letter_e, p)
        p = [307,260]
        screen.blit(letter_v, p)
        p = [357,260]
        screen.blit(letter_a, p)
        p = [408,260]
        screen.blit(letter_d, p)
        p = [461,260]
        screen.blit(letter_a2, p)
    else:
        if s.game.lite_a_name.status == True:
            p = [195,307]
            screen.blit(lite_a_name, p)

        if s.game.name.position >= 1:
            p = [203,259]
            screen.blit(letter_n, p)
        if s.game.name.position >= 2:
            p = [261,260]
            screen.blit(letter_e, p)
        if s.game.name.position >= 3:
            p = [307,260]
            screen.blit(letter_v, p)
        if s.game.name.position >= 4:
            p = [357,260]
            screen.blit(letter_a, p)
        if s.game.name.position >= 5:
            p = [408,260]
            screen.blit(letter_d, p)
        if s.game.name.position >= 6:
            p = [461,260]
            screen.blit(letter_a2, p)


    if s.game.super_card.position == 1:
        p = [36,372]
        screen.blit(sc_arrow, p)
    if s.game.super_card.position == 2:
        p = [74,372]
        screen.blit(sc_arrow, p)
    if s.game.super_card.position == 3:
        p = [111,372]
        screen.blit(sc_arrow, p)
    if s.game.super_card.position == 4:
        p = [150,372]
        screen.blit(sc_arrow, p)
    if s.game.super_card.position == 5:
        p = [529,371]
        screen.blit(sc_arrow, p)
    if s.game.super_card.position == 6:
        p = [565,371]
        screen.blit(sc_arrow, p)
    if s.game.super_card.position == 7:
        p = [604,372]
        screen.blit(sc_arrow, p)
    if s.game.super_card.position == 8:
        p = [641,372]
        screen.blit(sc_arrow, p)

    if s.game.super_card.position >= 4:
        p = [20,400]
        screen.blit(sc, p)
        if s.game.super_card1_three_as_four.status == True:
            p = [15,558]
            screen.blit(super_card_scores, p)
        else:
            p = [16,595]
            screen.blit(super_card_scores, p)


    if s.game.super_card.position >= 8:
        p = [513,401]
        screen.blit(sc, p)
        if s.game.super_card1_three_as_four.status == True:
            p = [506,558]
            screen.blit(super_card_scores, p)
        else:
            p = [507,595]
            screen.blit(super_card_scores, p)


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
        eb_position = [201,980]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 5:
        eb_position = [235,980]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 6:
        eb_position = [273,980]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 7:
        eb_position = [308,980]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 8:
        eb_position = [344,980]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 9:
        eb_position = [377,980]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 10:
        eb_position = [411,980]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 11:
        eb_position = [450,980]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 12:
        eb_position = [485,980]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 13:
        eb_position = [520,980]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 14:
        eb_position = [555,980]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 15:
        eb_position = [590,980]
        screen.blit(eb, eb_position)

    if s.game.extra_ball.position >= 5 and s.game.extra_ball.position < 10:
        eb_pos = [92,1008]
        screen.blit(extra_ball, eb_pos)
    if s.game.extra_ball.position >= 10 and s.game.extra_ball.position < 15:
        eb_pos = [270,1008]
        screen.blit(extra_ball, eb_pos)
    if s.game.extra_ball.position == 15:
        eb_pos = [447,1008]
        screen.blit(extra_ball, eb_pos)

    if s.game.odds.position > 0:
        if s.game.odds.position == 1:
            odds_position = [184,787]
            screen.blit(o1, odds_position)
        if s.game.odds.position == 2:
            odds_position = [227,789]
            screen.blit(o2, odds_position)
        if s.game.odds.position == 3:
            odds_position = [274,810]
            screen.blit(o3, odds_position)
        if s.game.odds.position == 4:
            odds_position = [325,789]
            screen.blit(o4, odds_position)
        if s.game.odds.position == 5:
            odds_position = [405,813]
            screen.blit(o5, odds_position)
        if s.game.odds.position == 6:
            odds_position = [449,804]
            screen.blit(o6, odds_position)
        if s.game.odds.position == 7:
            odds_position = [512,801]
            screen.blit(o7, odds_position)
        if s.game.odds.position == 8:
            odds_position = [557,830]
            screen.blit(o8, odds_position)

    if s.game.red_star.status == True:
        rs_position = [640,973]
        screen.blit(star, rs_position)

    if s.game.corners.status == True:
        corners_position = [507,237]
        screen.blit(corners, corners_position)

    if s.game.diamond_diagonal.status == True:
        corners_position = [15,235]
        screen.blit(corners, corners_position)
        if s.game.dd_three_as_four.status == False and s.game.four_as_five.status == False:
            p = [214,335]
            screen.blit(dd, p)
        elif s.game.dd_three_as_four.status == True:
            p = [312,335]
            screen.blit(dd, p)
        elif s.game.dd_three_as_five.status == True:
            p = [408,335]
            screen.blit(dd, p)

    if s.game.tilt.status == False:
        if s.holes:
            if 1 in s.holes:
                number_position = [218,530]
                screen.blit(number, number_position)
                number_position = [546,476]
                screen.blit(sc_number, number_position)
            if 2 in s.holes:
                number_position = [218,478]
                screen.blit(number, number_position)
            if 3 in s.holes:
                number_position = [441,583]
                screen.blit(number, number_position)
                number_position = [95,437]
                screen.blit(sc_number, number_position)
            if 4 in s.holes:
                number_position = [273,370]
                screen.blit(number, number_position)
                number_position = [583,516]
                screen.blit(sc_number, number_position)
            if 5 in s.holes:
                number_position = [332,584]
                screen.blit(number, number_position)
            if 6 in s.holes:
                number_position = [441,368]
                screen.blit(number, number_position)
            if 7 in s.holes:
                number_position = [276,584]
                screen.blit(number, number_position)
                number_position = [585,439]
                screen.blit(sc_number, number_position)
            if 8 in s.holes:
                number_position = [440,422]
                screen.blit(number, number_position)
            if 9 in s.holes:
                number_position = [218,368]
                screen.blit(number, number_position)
                number_position = [54,475]
                screen.blit(sc_number, number_position)
            if 10 in s.holes:
                number_position = [218,424]
                screen.blit(number, number_position)
                number_position = [583,479]
                screen.blit(sc_number, number_position)
            if 11 in s.holes:
                number_position = [220,585]
                screen.blit(number, number_position)
                number_position = [131,475]
                screen.blit(sc_number, number_position)
                number_position = [622,439]
                screen.blit(sc_number, number_position)
            if 12 in s.holes:
                number_position = [385,478]
                screen.blit(number, number_position)
                number_position = [53,515]
                screen.blit(sc_number, number_position)
            if 13 in s.holes:
                number_position = [331,531]
                screen.blit(number, number_position)
                number_position = [623,477]
                screen.blit(sc_number, number_position)
            if 14 in s.holes:
                number_position = [332,424]
                screen.blit(number, number_position)
                number_position = [130,514]
                screen.blit(sc_number, number_position)
            if 15 in s.holes:
                number_position = [329,371]
                screen.blit(number, number_position)
                number_position = [546,438]
                screen.blit(sc_number, number_position)
            if 16 in s.holes:
                number_position = [330,478]
                screen.blit(number, number_position)
            if 17 in s.holes:
                number_position = [440,533]
                screen.blit(number, number_position)
                number_position = [545,515]
                screen.blit(sc_number, number_position)
            if 18 in s.holes:
                number_position = [276,476]
                screen.blit(number, number_position)
                number_position = [132,438]
                screen.blit(sc_number, number_position)
                number_position = [623,515]
                screen.blit(sc_number, number_position)
            if 19 in s.holes:
                number_position = [275,423]
                screen.blit(number, number_position)
            if 20 in s.holes:
                number_position = [385,424]
                screen.blit(number, number_position)
            if 21 in s.holes:
                number_position = [385,530]
                screen.blit(number, number_position)
            if 22 in s.holes:
                number_position = [276,531]
                screen.blit(number, number_position)
            if 23 in s.holes:
                number_position = [385,585]
                screen.blit(number, number_position)
                number_position = [53,438]
                screen.blit(sc_number, number_position)
            if 24 in s.holes:
                number_position = [385,368]
                screen.blit(number, number_position)
                number_position = [92,514]
                screen.blit(sc_number, number_position)
            if 25 in s.holes:
                number_position = [438,477]
                screen.blit(number, number_position)
                number_position = [93,477]
                screen.blit(sc_number, number_position)

    if s.game.tilt.status == True:
        tilt_position = [80,795]
        screen.blit(tilt, tilt_position)

    if s.game.selection_feature.position == 2:
        p = [100,685]
        screen.blit(s_arrow, p)
    if s.game.selection_feature.position == 3:
        p = [140,685]
        screen.blit(s_arrow, p)
    if s.game.selection_feature.position == 4:
        p = [180,685]
        screen.blit(s_arrow, p)
    if s.game.selection_feature.position >= 5:
        p = [213,686]
        screen.blit(s_number, p)
    if s.game.selection_feature.position >= 6:
        p = [252,686]
        screen.blit(s_number, p)
    if s.game.selection_feature.position >= 7:
        p = [291,686]
        screen.blit(s_number, p)
    if s.game.selection_feature.position >= 8:
        p = [332,686]
        screen.blit(s_number, p)
    if s.game.selection_feature.position >= 9:
        p = [368,686]
        screen.blit(s_number, p)
    if s.game.selection_feature.position >= 10:
        p = [410,686]
        screen.blit(s_number, p)
    if s.game.selection_feature.position >= 11:
        p = [447,686]
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
        p = [7,686]
        screen.blit(before_fourth, p)
    if s.game.before_fifth.status == True and (s.game.selection_feature.position > 3 or s.game.selection_feature_relay.status == True):
        p = [616,688]
        screen.blit(before_fourth, p)

    if s.game.before_fourth.status == True:
        if s.game.ball_count.position < 4:
            if s.game.select_spots.status == True:
                if s.game.selection_feature.position >= 5:
                    if s.game.spotted.position == 0:
                        #19
                        number_position = [275,423]
                        screen.blit(red_number, number_position)
                if s.game.selection_feature.position >= 6:
                    if s.game.spotted.position == 1:
                        #20
                        number_position = [385,424]
                        screen.blit(red_number, number_position)
                if s.game.selection_feature.position >= 7:
                    if s.game.spotted.position == 2:
                        #21
                        number_position = [385,530]
                        screen.blit(red_number, number_position)
                if s.game.selection_feature.position >= 8:
                    if s.game.spotted.position == 3:
                        #22
                        number_position = [276,531]
                        screen.blit(red_number, number_position)
                if s.game.selection_feature.position >= 9:
                    if s.game.spotted.position == 4:
                        #16
                        number_position = [330,478]
                        screen.blit(red_number, number_position)
                if s.game.selection_feature.position >= 10:
                    if s.game.spotted.position == 5:
                        #25
                        number_position = [438,477]
                        screen.blit(red_number, number_position)
                        number_position = [93,477]
                        screen.blit(red_sc_number, number_position)
                if s.game.selection_feature.position >= 11:
                    if s.game.spotted.position == 6:
                        #10
                        number_position = [218,424]
                        screen.blit(red_number, number_position)
                        number_position = [583,479]
                        screen.blit(red_sc_number, number_position)
            if s.game.selection_feature_relay.status == True:
                if s.game.spotted.position == 7:
                    p = [98,723]
                    screen.blit(red_select_feature, p)
                if s.game.spotted.position == 8:
                    p = [199,723]
                    screen.blit(red_select_feature, p)
                if s.game.spotted.position == 9:
                    p = [405,724]
                    screen.blit(red_select_feature, p)
                if s.game.spotted.position == 10:
                    p = [509,723]
                    screen.blit(red_select_feature, p)

    if s.game.before_fifth.status == True:
        if s.game.ball_count.position < 5:
            if s.game.select_spots.status == True:
                if s.game.selection_feature.position >= 5:
                    if s.game.spotted.position == 0:
                        #19
                        number_position = [275,423]
                        screen.blit(red_number, number_position)
                if s.game.selection_feature.position >= 6:
                    if s.game.spotted.position == 1:
                        #20
                        number_position = [385,424]
                        screen.blit(red_number, number_position)
                if s.game.selection_feature.position >= 7:
                    if s.game.spotted.position == 2:
                        #21
                        number_position = [385,530]
                        screen.blit(red_number, number_position)
                if s.game.selection_feature.position >= 8:
                    if s.game.spotted.position == 3:
                        #22
                        number_position = [276,531]
                        screen.blit(red_number, number_position)
                if s.game.selection_feature.position >= 9:
                    if s.game.spotted.position == 4:
                        #16
                        number_position = [330,478]
                        screen.blit(red_number, number_position)
                if s.game.selection_feature.position >= 10:
                    if s.game.spotted.position == 5:
                        #25
                        number_position = [438,477]
                        screen.blit(red_number, number_position)
                        number_position = [93,477]
                        screen.blit(red_sc_number, number_position)
                if s.game.selection_feature.position >= 11:
                    if s.game.spotted.position == 6:
                        #10
                        number_position = [218,424]
                        screen.blit(red_number, number_position)
                        number_position = [583,479]
                        screen.blit(red_sc_number, number_position)
            if s.game.selection_feature_relay.status == True:
                if s.game.spotted.position == 7:
                    p = [98,723]
                    screen.blit(red_select_feature, p)
                if s.game.spotted.position == 8:
                    p = [199,723]
                    screen.blit(red_select_feature, p)
                if s.game.spotted.position == 9:
                    p = [405,724]
                    screen.blit(red_select_feature, p)
                if s.game.spotted.position == 10:
                    p = [509,723]
                    screen.blit(red_select_feature, p)
                                
    if s.game.selection_feature_relay.status == True:
        p = [98,723]
        screen.blit(select_feature, p)
        p = [199,723]
        screen.blit(select_feature, p)
        p = [304,723]
        screen.blit(super_selection, p)
        p = [405,724]
        screen.blit(select_feature, p)
        p = [509,723]
        screen.blit(select_feature, p)


    if s.game.selection_feature_relay.status == True:
        if s.game.before_fourth.status == True:
            max_ball = 4
        else:
            max_ball = 5
        if s.game.ball_count.position == max_ball:
            if s.game.spotted.position == 8:
                p = [251,640]
                screen.blit(three_four, p)

    if s.game.four_as_five.status == True:
        p = [251,640]
        screen.blit(three_four, p)

    if s.game.eb_play.status == True:
        p = [26,981]
        screen.blit(extra_balls, p)

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
        p = [376,934]
        screen.blit(ball_return, p)

    pygame.display.update()

def blink(args):
    dirty_rects = []
    s = args[0]
    b = args[1]
    sn = args[2]

    if b == 0:
        if sn == 1:
            p = [485,687]
            dirty_rects.append(screen.blit(select_now, p))
        pygame.display.update(dirty_rects)
    else:
        dirty_rects.append(screen.blit(bg_gi, (485,687), pygame.Rect(485,687,130,36)))
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
        dirty_rects.append(screen.blit(bg_gi, (270,1008), pygame.Rect(270,1008,180,35)))
    if s.game.extra_ball.position < 15:
        dirty_rects.append(screen.blit(bg_gi, (447,1008), pygame.Rect(447,1008,180,35)))
        dirty_rects.append(screen.blit(bg_gi, (590,980), pygame.Rect(590,980,30,25)))
    pygame.display.update(dirty_rects)

    if num in [1,9,17,4,12,15,21]:
        if s.game.extra_ball.position < 5:
            p = [92,1008]
            dirty_rects.append(screen.blit(extra_ball, p))
            pygame.display.update(dirty_rects) 
    elif num in [2,10,18,5,7,13,16,22]:
        if s.game.extra_ball.position < 10:
            p = [270,1008]
            dirty_rects.append(screen.blit(extra_ball, p))
            pygame.display.update(dirty_rects)
    elif num in [3,11,19,6,8,14,20,23]:
        if s.game.extra_ball.position < 15:
            p = [447,1008]
            dirty_rects.append(screen.blit(extra_ball, p))
            p = [590,980]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)

def clear_odds(s, num):
    global screen
    dirty_rects = []
    if s.game.odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (184,787), pygame.Rect(184,787,37,120)))
    if s.game.odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (227,789), pygame.Rect(227,789,40,95)))
    if s.game.odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (274,810), pygame.Rect(274,810,36,98)))
    if s.game.odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (325,789), pygame.Rect(325,789,71,135)))
    if s.game.odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (405,813), pygame.Rect(405,813,35,96)))
    if s.game.odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (449,804), pygame.Rect(449,804,39,114)))
    if s.game.odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (512,801), pygame.Rect(512,801,44,120)))
    if s.game.odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (557,830), pygame.Rect(557,830,46,111)))

    pygame.display.update(dirty_rects)

def draw_odds_animation(s, num):
    global screen
    dirty_rects = []
    if num in [0,11,17]:
        if s.game.odds.position != 1:
            p = [184,787]
            dirty_rects.append(screen.blit(o1, p))
            pygame.display.update(dirty_rects)
            return
    if num in [1,10,18]:
        if s.game.odds.position != 2:
            p = [227,789]
            dirty_rects.append(screen.blit(o2, p))
            pygame.display.update(dirty_rects)
            return
    if num in [4,12,19]:
        if s.game.odds.position != 3:
            p = [274,810]
            dirty_rects.append(screen.blit(o3, p))
            pygame.display.update(dirty_rects)
            return
    if num in [3,9,20]:
        if s.game.odds.position != 4:
            p = [325,789]
            dirty_rects.append(screen.blit(o4, p))
            pygame.display.update(dirty_rects)
            return
    if num in [5,13,21]:
        if s.game.odds.position != 5:
            p = [405,813]
            dirty_rects.append(screen.blit(o5, p))
            pygame.display.update(dirty_rects)
            return
    if num in [6,14,22]:
        if s.game.odds.position != 6:
            p = [449,804]
            dirty_rects.append(screen.blit(o6, p))
            pygame.display.update(dirty_rects)
            return
    if num in [7,16,23]:
        if s.game.odds.position != 7:
            p = [512,801]
            dirty_rects.append(screen.blit(o7, p))
            pygame.display.update(dirty_rects)
            return
    if num in [8,15,24]:
        if s.game.odds.position != 8:
            p = [557,830]
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
        dirty_rects.append(screen.blit(bg_gi, (20,400), pygame.Rect(20,400,177,31)))
    if s.game.super_card.position < 8:
        dirty_rects.append(screen.blit(bg_gi, (513,401), pygame.Rect(513,401,177,31)))
    if s.game.corners.status == False:
        dirty_rects.append(screen.blit(bg_gi, (507,237), pygame.Rect(507,237,188,128)))
    if s.game.ball_return.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (376,934), pygame.Rect(376,934,175,40)))
    if s.game.red_star.status == False:
        dirty_rects.append(screen.blit(bg_gi, (640,973), pygame.Rect(640,973,61,65)))
    if s.game.dd_three_as_four.status == False:
        dirty_rects.append(screen.blit(bg_gi, (312,335), pygame.Rect(312,335,93,28)))
    if s.game.dd_three_as_five.status == False:
        dirty_rects.append(screen.blit(bg_gi, (408,335), pygame.Rect(408,335,93,28)))
    if s.game.selection_feature_relay.status == False:
        dirty_rects.append(screen.blit(bg_gi, (304,723), pygame.Rect(304,723,105,50)))
    pygame.display.update(dirty_rects)
    return

def animate_mixer1(s):
    global screen
    dirty_rects = []
    if s.game.super_card.position < 4:
        p = [20,400]
        dirty_rects.append(screen.blit(sc, p))
        pygame.display.update(dirty_rects)
        return

def animate_mixer2(s):
    global screen
    dirty_rects = []
    if s.game.super_card.position < 8:
        p = [513,401]
        dirty_rects.append(screen.blit(sc, p))
    if s.game.dd_three_as_four.status == False:
        p = [312,335]
        dirty_rects.append(screen.blit(dd, p))
    pygame.display.update(dirty_rects)
    return

def animate_mixer3(s):
    global screen
    dirty_rects = []
    if s.game.corners.status == False:
        p = [507,237]
        dirty_rects.append(screen.blit(corners, p))
    if s.game.red_star.status == False:
        p = [640,973]
        dirty_rects.append(screen.blit(star, p))
        s.game.coils.redROLamp.pulse(85)
        s.game.coils.yellowROLamp.pulse(85)
    if s.game.ball_return.position != 7:
        p = [376,934]
        dirty_rects.append(screen.blit(ball_return, p))
    pygame.display.update(dirty_rects)
    return


def animate_mixer4(s):
    global screen
    dirty_rects = []
    if s.game.dd_three_as_five.status == False:
        p = [408,335]
        dirty_rects.append(screen.blit(dd, p))
    if s.game.selection_feature_relay.status == False:
        p = [304,723]
        dirty_rects.append(screen.blit(super_selection, p))
    pygame.display.update(dirty_rects)
    return

def clear_features(s, num):
    global screen
    dirty_rects = []
    if s.game.before_fourth.status == False:
        dirty_rects.append(screen.blit(bg_gi, (7,686), pygame.Rect(7,686,89,62)))
    if s.game.before_fifth.status == False:
        dirty_rects.append(screen.blit(bg_gi, (616,688), pygame.Rect(616,688,89,62)))

    if s.game.selection_feature.position < 2:
        dirty_rects.append(screen.blit(bg_gi, (100,685), pygame.Rect(100,685,33,37)))
    if s.game.selection_feature.position < 3:
        dirty_rects.append(screen.blit(bg_gi, (140,685), pygame.Rect(140,685,33,37)))
    if s.game.selection_feature.position < 4:
        dirty_rects.append(screen.blit(bg_gi, (180,685), pygame.Rect(180,685,33,37)))
    if s.game.selection_feature.position < 6:
        dirty_rects.append(screen.blit(bg_gi, (213,686), pygame.Rect(213,686,38,37)))
        dirty_rects.append(screen.blit(bg_gi, (252,686), pygame.Rect(252,686,38,37)))
    if s.game.selection_feature.position < 7:
        dirty_rects.append(screen.blit(bg_gi, (291,686), pygame.Rect(291,686,38,37)))
    if s.game.selection_feature.position < 8:
        dirty_rects.append(screen.blit(bg_gi, (332,686), pygame.Rect(332,686,38,37)))
    if s.game.selection_feature.position < 9:
        dirty_rects.append(screen.blit(bg_gi, (368,686), pygame.Rect(368,686,38,37)))
    if s.game.selection_feature.position < 10:
        dirty_rects.append(screen.blit(bg_gi, (410,686), pygame.Rect(410,686,38,37)))
    if s.game.selection_feature.position < 11:
        dirty_rects.append(screen.blit(bg_gi, (447,686), pygame.Rect(447,686,38,37)))

    pygame.display.update(dirty_rects)

def draw_feature_animation(s, num):
    global screen
    dirty_rects = []

    if num in [4,15,10,21]:
        if s.game.before_fourth.status == False:
            p = [7,686]
            dirty_rects.append(screen.blit(before_fourth, p))
        if s.game.before_fifth.status == False and s.game.before_fourth.status == True:
            p = [616,688]
            dirty_rects.append(screen.blit(before_fourth, p))
        pygame.display.update(dirty_rects)
        return
    if num in [0,11,22]:
        if s.game.selection_feature.position < 2:
            p = [100,685]
            dirty_rects.append(screen.blit(s_arrow, p))
            pygame.display.update(dirty_rects)
            return
    if num in [9,20,23]:
        if s.game.selection_feature.position < 3:
            p = [140,685]
            dirty_rects.append(screen.blit(s_arrow, p))
            pygame.display.update(dirty_rects)
            return
    if num in [1,12,24]:
        if s.game.selection_feature.position < 4:
            p = [180,685]
            dirty_rects.append(screen.blit(s_arrow, p))
            pygame.display.update(dirty_rects)
            return
    if num in [2,13]:
        if s.game.selection_feature.position < 6:
            p = [213,686]
            dirty_rects.append(screen.blit(s_number, p))
            p = [252,686]
            dirty_rects.append(screen.blit(s_number, p))
            pygame.display.update(dirty_rects)
            return
    if num in [3,14,4,15]:
        if s.game.selection_feature.position < 7:
            p = [291,686]
            dirty_rects.append(screen.blit(s_number, p))
        pygame.display.update(dirty_rects)
        return
    if num in [5,16]:
        if s.game.selection_feature.position < 8:
            p = [332,686]
            dirty_rects.append(screen.blit(s_number, p))
        pygame.display.update(dirty_rects)
        return
    if num in [6,17]:
        if s.game.selection_feature.position < 9:
            p = [368,686]
            dirty_rects.append(screen.blit(s_number, p))
            pygame.display.update(dirty_rects)
            return
    if num in [7,18]:
        if s.game.selection_feature.position < 10:
            p = [410,686]
            dirty_rects.append(screen.blit(s_number, p))
            pygame.display.update(dirty_rects)
            return
    if num in [8,19]:
        if s.game.selection_feature.position < 11:
            p = [447,686]
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

