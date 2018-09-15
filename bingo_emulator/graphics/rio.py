
import pygame
import random

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

meter = pygame.image.load('graphics/assets/silver_register_cover.png').convert()
sc_arrow = pygame.image.load('rio/assets/sc_arrow.png').convert_alpha()
sc = pygame.image.load('rio/assets/super_card.png').convert_alpha()
eb = pygame.image.load('rio/assets/eb.png').convert_alpha()
extra_ball = pygame.image.load('rio/assets/extra_ball.png').convert_alpha()
extra_balls = pygame.image.load('rio/assets/extra_balls.png').convert_alpha()
o1 = pygame.image.load('rio/assets/odds1.png').convert_alpha()
o2 = pygame.image.load('rio/assets/odds2.png').convert_alpha()
o3 = pygame.image.load('rio/assets/odds3.png').convert_alpha()
o4 = pygame.image.load('rio/assets/odds4.png').convert_alpha()
o5 = pygame.image.load('rio/assets/odds5.png').convert_alpha()
o6 = pygame.image.load('rio/assets/odds6.png').convert_alpha()
o7 = pygame.image.load('rio/assets/odds7.png').convert_alpha()
o8 = pygame.image.load('rio/assets/odds8.png').convert_alpha()
star = pygame.image.load('rio/assets/rollover.png').convert_alpha()
number = pygame.image.load('rio/assets/number.png').convert_alpha()
sc_number = pygame.image.load('rio/assets/sc_number.png').convert_alpha()
tilt = pygame.image.load('rio/assets/tilt.png').convert_alpha()
select_now = pygame.image.load('rio/assets/select_now.png').convert_alpha()
red_number = pygame.image.load('rio/assets/red_number.png').convert_alpha()
red_sc_number = pygame.image.load('rio/assets/red_sc_number.png').convert_alpha()
s_number = pygame.image.load('rio/assets/spotted_numbers.png').convert_alpha()
s_arrow = pygame.image.load('rio/assets/selection_arrow.png').convert_alpha()
before_fourth = pygame.image.load('rio/assets/before_fourth.png').convert_alpha()
select_feature = pygame.image.load('rio/assets/select_feature.png').convert_alpha()
red_select_feature = pygame.image.load('rio/assets/red_select_feature.png').convert_alpha()
three_four = pygame.image.load('rio/assets/3_as_4.png').convert_alpha()
special_card = pygame.image.load('rio/assets/special_card.png').convert_alpha()
letter_r = pygame.image.load('rio/assets/r.png').convert_alpha()
letter_o = pygame.image.load('rio/assets/o.png').convert_alpha()
letter_i = pygame.image.load('rio/assets/i.png').convert_alpha()
lite_a_name = pygame.image.load('rio/assets/lite_a_name.png').convert_alpha()
bg_menu = pygame.image.load('rio/assets/rio_menu.png')
bg_gi = pygame.image.load('rio/assets/rio_gi.png')
bg_off = pygame.image.load('rio/assets/rio_off.png')

class scorereel():
    """ Score Reels are used to count replays """
    def __init__(self, pos, image):
        self.position = pos
        self.default_y = self.position[1]
        self.image = pygame.image.load(image).convert()

reel1 = scorereel([108,831], "graphics/assets/green_reel.png")
reel10 = scorereel([89,831], "graphics/assets/green_reel.png")
reel100 = scorereel([70,831], "graphics/assets/green_reel.png")

def display(s, replays=0, menu=False):
    
    meter.set_colorkey((255,0,252))
    meter_position = [60,829]

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
        p = [240,256]
        screen.blit(letter_r, p)
        p = [332,268]
        screen.blit(letter_i, p)
        p = [390,258]
        screen.blit(letter_o, p)
    else:
        p = [232,305]
        screen.blit(lite_a_name, p)

    if s.game.super_card.position == 1:
       p = [37,421]
       screen.blit(sc_arrow, p)
    if s.game.super_card.position == 2:
       p = [72,421]
       screen.blit(sc_arrow, p)
    if s.game.super_card.position == 3:
       p = [108,421]
       screen.blit(sc_arrow, p)
    if s.game.super_card.position == 4:
       p = [143,421]
       screen.blit(sc_arrow, p)
    if s.game.super_card.position == 5:
       p = [543,418]
       screen.blit(sc_arrow, p)
    if s.game.super_card.position == 6:
       p = [578,418]
       screen.blit(sc_arrow, p)
    if s.game.super_card.position == 7:
       p = [613,418]
       screen.blit(sc_arrow, p)
    if s.game.super_card.position == 8:
       p = [649,418]
       screen.blit(sc_arrow, p)

    if s.game.super_card.position >= 4:
       p = [36,248]
       screen.blit(sc, p)

    if s.game.super_card.position >= 8:
       p = [539,246]
       screen.blit(sc, p)

    if s.game.extra_ball.position == 1:
       eb_position = [96,972]
       screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 2:
       eb_position = [129,972]
       screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 3:
       eb_position = [163,972]
       screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 4:
       eb_position = [199,972]
       screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 5:
       eb_position = [234,972]
       screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 6:
       eb_position = [275,972]
       screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 7:
       eb_position = [310,972]
       screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 8:
       eb_position = [344,972]
       screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 9:
       eb_position = [379,972]
       screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 10:
       eb_position = [413,972]
       screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 11:
       eb_position = [457,972]
       screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 12:
       eb_position = [491,972]
       screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 13:
       eb_position = [526,972]
       screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 14:
       eb_position = [560,972]
       screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 15:
        eb_position = [595,972]
        screen.blit(eb, eb_position)
    
    if s.game.extra_ball.position >= 5 and s.game.extra_ball.position < 10:
        eb_pos = [96,1002]
        screen.blit(extra_ball, eb_pos)
    if s.game.extra_ball.position >= 10 and s.game.extra_ball.position < 15:
        eb_pos = [275,1002]
        screen.blit(extra_ball, eb_pos)
    if s.game.extra_ball.position == 15:
        eb_pos = [456,1002]
        screen.blit(extra_ball, eb_pos)
    
    if s.game.odds.position > 0:
        if s.game.odds.position == 1:
           odds_position = [178,815]
           screen.blit(o1, odds_position)
        if s.game.odds.position == 2:
           odds_position = [223,769]
           screen.blit(o2, odds_position)
        if s.game.odds.position == 3:
           odds_position = [362,766]
           screen.blit(o3, odds_position)
        if s.game.odds.position == 4:
           odds_position = [405,786]
           screen.blit(o4, odds_position)
        if s.game.odds.position == 5:
           odds_position = [455,811]
           screen.blit(o5, odds_position)
        if s.game.odds.position == 6:
           odds_position = [566,770]
           screen.blit(o6, odds_position)
        if s.game.odds.position == 7:
           odds_position = [615,818]
           screen.blit(o7, odds_position)
        if s.game.odds.position == 8:
            odds_position = [659,757]
            screen.blit(o8, odds_position)

    if s.game.red_star.status == True:
        rs_position = [634,980]
        screen.blit(star, rs_position)

    if s.game.yellow_star.status == True:
        ys_position = [34,980]
        screen.blit(star, ys_position)

    if s.game.corners.status == True:
        corners_position = [365,636]
        screen.blit(three_four, corners_position)

    if s.game.tilt.status == False:
        if s.holes:
            if 1 in s.holes:
                number_position = [225,522]
                screen.blit(number, number_position)
                number_position = [546,334]
                screen.blit(sc_number, number_position)
                number_position = [63,545]
                screen.blit(sc_number, number_position)
            if 2 in s.holes:
                number_position = [225,466]
                screen.blit(number, number_position)
            if 3 in s.holes:
                number_position = [448,574]
                screen.blit(number, number_position)
                number_position = [88,291]
                screen.blit(sc_number, number_position)
            if 4 in s.holes:
                number_position = [280,358]
                screen.blit(number, number_position)
                number_position = [595,379]
                screen.blit(sc_number, number_position)
                number_position = [63,589]
                screen.blit(sc_number, number_position)
            if 5 in s.holes:
                number_position = [337,574]
                screen.blit(number, number_position)
            if 6 in s.holes:
                number_position = [448,359]
                screen.blit(number, number_position)
                number_position = [618,587]
                screen.blit(sc_number, number_position)
            if 7 in s.holes:
                number_position = [282,574]
                screen.blit(number, number_position)
                number_position = [594,288]
                screen.blit(sc_number, number_position)
            if 8 in s.holes:
                number_position = [448,412]
                screen.blit(number, number_position)
            if 9 in s.holes:
                number_position = [224,360]
                screen.blit(number, number_position)
                number_position = [39,335]
                screen.blit(sc_number, number_position)
                number_position = [617,542]
                screen.blit(sc_number, number_position)
            if 10 in s.holes:
                number_position = [224,413]
                screen.blit(number, number_position)
                number_position = [594,331]
                screen.blit(sc_number, number_position)
            if 11 in s.holes:
                number_position = [226,574]
                screen.blit(number, number_position)
                number_position = [134,336]
                screen.blit(sc_number, number_position)
                number_position = [640,287]
                screen.blit(sc_number, number_position)
            if 12 in s.holes:
                number_position = [390,466]
                screen.blit(number, number_position)
                number_position = [42,380]
                screen.blit(sc_number, number_position)
                number_position = [109,543]
                screen.blit(sc_number, number_position)
            if 13 in s.holes:
                number_position = [338,518]
                screen.blit(number, number_position)
                number_position = [642,332]
                screen.blit(sc_number, number_position)
            if 14 in s.holes:
                number_position = [336,410]
                screen.blit(number, number_position)
                number_position = [135,380]
                screen.blit(sc_number, number_position)
            if 15 in s.holes:
                number_position = [336,358]
                screen.blit(number, number_position)
                number_position = [546,286]
                screen.blit(sc_number, number_position)
            if 16 in s.holes:
                number_position = [336,465]
                screen.blit(number, number_position)
            if 17 in s.holes:
                number_position = [447,518]
                screen.blit(number, number_position)
                number_position = [548,379]
                screen.blit(sc_number, number_position)
                number_position = [570,587]
                screen.blit(sc_number, number_position)
            if 18 in s.holes:
                number_position = [280,466]
                screen.blit(number, number_position)
                number_position = [134,290]
                screen.blit(sc_number, number_position)
                number_position = [641,378]
                screen.blit(sc_number, number_position)
            if 19 in s.holes:
                number_position = [279,412]
                screen.blit(number, number_position)
            if 20 in s.holes:
                number_position = [391,410]
                screen.blit(number, number_position)
            if 21 in s.holes:
                number_position = [392,518]
                screen.blit(number, number_position)
            if 22 in s.holes:
                number_position = [282,519]
                screen.blit(number, number_position)
            if 23 in s.holes:
                number_position = [392,572]
                screen.blit(number, number_position)
                number_position = [38,290]
                screen.blit(sc_number, number_position)
                number_position = [570,542]
                screen.blit(sc_number, number_position)
            if 24 in s.holes:
                number_position = [392,358]
                screen.blit(number, number_position)
                number_position = [89,382]
                screen.blit(sc_number, number_position)
                number_position = [109,589]
                screen.blit(sc_number, number_position)
            if 25 in s.holes:
                number_position = [448,466]
                screen.blit(number, number_position)
                number_position = [87,334]
                screen.blit(sc_number, number_position)

    if s.game.tilt.status == True:
        tilt_position = [40,774]
        screen.blit(tilt, tilt_position)

    if s.game.selection_feature.position == 2:
        p = [104,686]
        screen.blit(s_arrow, p)
    if s.game.selection_feature.position == 3:
        p = [144,686]
        screen.blit(s_arrow, p)
    if s.game.selection_feature.position == 4:
        p = [182,686]
        screen.blit(s_arrow, p)
    if s.game.selection_feature.position >= 5:
        p = [215,687]
        screen.blit(s_number, p)
    if s.game.selection_feature.position >= 6:
        p = [256,686]
        screen.blit(s_number, p)
    if s.game.selection_feature.position >= 7:
        p = [295,686]
        screen.blit(s_number, p)
    if s.game.selection_feature.position >= 8:
        p = [334,686]
        screen.blit(s_number, p)
    if s.game.selection_feature.position >= 9:
        p = [374,688]
        screen.blit(s_number, p)
    if s.game.selection_feature.position >= 10:
        p = [412,687]
        screen.blit(s_number, p)
    if s.game.selection_feature.position >= 11:
        p = [453,686]
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
        p = [14,686]
        screen.blit(before_fourth, p)
    if s.game.before_fifth.status == True and (s.game.selection_feature.position > 3 or s.game.selection_feature_relay.status == True):
        p = [627,684]
        screen.blit(before_fourth, p)

    if s.game.before_fourth.status == True:
        if s.game.ball_count.position < 4:
            if s.game.select_spots.status == True:
                if s.game.selection_feature.position >= 5:
                    if s.game.spotted.position == 0:
                        #19
                        number_position = [279,412]
                        screen.blit(red_number, number_position)
                if s.game.selection_feature.position >= 6:
                    if s.game.spotted.position == 1:
                        #20
                        number_position = [391,410]
                        screen.blit(red_number, number_position)
                if s.game.selection_feature.position >= 7:
                    if s.game.spotted.position == 2:
                        #21
                        number_position = [392,518]
                        screen.blit(red_number, number_position)
                if s.game.selection_feature.position >= 8:
                    if s.game.spotted.position == 3:
                        #22
                        number_position = [282,519]
                        screen.blit(red_number, number_position)
                if s.game.selection_feature.position >= 9:
                    if s.game.spotted.position == 4:
                        #16
                        number_position = [336,465]
                        screen.blit(red_number, number_position)
                if s.game.selection_feature.position >= 10:
                    if s.game.spotted.position == 5:
                        #25
                        number_position = [448,466]
                        screen.blit(red_number, number_position)
                        number_position = [87,334]
                        screen.blit(red_sc_number, number_position)
                if s.game.selection_feature.position >= 11:
                    if s.game.spotted.position == 6:
                        #10
                        number_position = [224,413]
                        screen.blit(red_number, number_position)
                        number_position = [594,331]
                        screen.blit(red_sc_number, number_position)
            if s.game.selection_feature_relay.status == True:
                if s.game.spotted.position == 7:
                    p = [114,726]
                    screen.blit(red_select_feature, p)
                if s.game.spotted.position == 8:
                    p = [240,726]
                    screen.blit(red_select_feature, p)
                if s.game.spotted.position == 9:
                    p = [368,726]
                    screen.blit(red_select_feature, p)
                if s.game.spotted.position == 10:
                    p = [494,726]
                    screen.blit(red_select_feature, p)

    if s.game.before_fifth.status == True:
        if s.game.ball_count.position < 5:
            if s.game.select_spots.status == True:
                if s.game.selection_feature.position >= 5:
                    if s.game.spotted.position == 0:
                        #19
                        number_position = [279,412]
                        screen.blit(red_number, number_position)
                if s.game.selection_feature.position >= 6:
                    if s.game.spotted.position == 1:
                        #20
                        number_position = [391,410]
                        screen.blit(red_number, number_position)
                if s.game.selection_feature.position >= 7:
                    if s.game.spotted.position == 2:
                        #21
                        number_position = [392,518]
                        screen.blit(red_number, number_position)
                if s.game.selection_feature.position >= 8:
                    if s.game.spotted.position == 3:
                        #22
                        number_position = [282,519]
                        screen.blit(red_number, number_position)
                if s.game.selection_feature.position >= 9:
                    if s.game.spotted.position == 4:
                        #16
                        number_position = [336,465]
                        screen.blit(red_number, number_position)
                if s.game.selection_feature.position >= 10:
                    if s.game.spotted.position == 5:
                        #25
                        number_position = [448,466]
                        screen.blit(red_number, number_position)
                        number_position = [87,334]
                        screen.blit(red_sc_number, number_position)
                if s.game.selection_feature.position >= 11:
                    if s.game.spotted.position == 6:
                        #10
                        number_position = [224,413]
                        screen.blit(red_number, number_position)
                        number_position = [594,331]
                        screen.blit(red_sc_number, number_position)
            if s.game.selection_feature_relay.status == True:
                if s.game.spotted.position == 7:
                    p = [114,726]
                    screen.blit(red_select_feature, p)
                if s.game.spotted.position == 8:
                    p = [240,726]
                    screen.blit(red_select_feature, p)
                if s.game.spotted.position == 9:
                    p = [368,726]
                    screen.blit(red_select_feature, p)
                if s.game.spotted.position == 10:
                    p = [494,726]
                    screen.blit(red_select_feature, p)

    if s.game.selection_feature_relay.status == True:
        p = [114,726]
        screen.blit(select_feature, p)
        p = [240,726]
        screen.blit(select_feature, p)
        p = [368,726]
        screen.blit(select_feature, p)
        p = [494,726]
        screen.blit(select_feature, p)


    if s.game.selection_feature_relay.status == True:
        if s.game.before_fourth.status == True:
            max_ball = 4
        else:
            max_ball = 5
        if s.game.ball_count.position == max_ball:
            if s.game.spotted.position == 8:
                p = [256,633]
                screen.blit(three_four, p)

    if s.game.three_as_four.status == True:
        p = [256,633]
        screen.blit(three_four, p)

    if s.game.left_special_card.status == True:
        p = [57,505]
        screen.blit(special_card, p)
    if s.game.right_special_card.status == True:
        p = [565,504]
        screen.blit(special_card, p)

    if s.game.eb_play.status == True:
        p = [301,942]
        screen.blit(extra_balls, p)


    if s.game.letter_r.status == True:
        p = [240,256]
        screen.blit(letter_r, p)
    if s.game.letter_i.status == True:
        p = [332,268]
        screen.blit(letter_i, p)
    if s.game.letter_o.status == True:
        p = [390,258]
        screen.blit(letter_o, p)

    pygame.display.update()

def blink(args):
    dirty_rects = []
    s = args[0]
    b = args[1]
    sn = args[2]

    if b == 0:
        if sn == 1:
            p = [493,686]
            dirty_rects.append(screen.blit(select_now, p))
        pygame.display.update(dirty_rects)
    else:
        dirty_rects.append(screen.blit(bg_gi, (493,686), pygame.Rect(493,686,129,37)))
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
        dirty_rects.append(screen.blit(bg_gi, (96,1002), pygame.Rect(96,1002,170,33)))
    if s.game.extra_ball.position < 10:
        dirty_rects.append(screen.blit(bg_gi, (275,1002), pygame.Rect(275,1002,170,33)))
    if s.game.extra_ball.position < 15:
        dirty_rects.append(screen.blit(bg_gi, (456,1002), pygame.Rect(456,1002,170,33)))
        dirty_rects.append(screen.blit(bg_gi, (595,972), pygame.Rect(595,972,32,28)))
    pygame.display.update(dirty_rects)

    if num in [1,9,17,4,12,15,21]:
        if s.game.extra_ball.position < 5:
            p = [96,1002]
            dirty_rects.append(screen.blit(extra_ball, p))
            pygame.display.update(dirty_rects) 
    elif num in [2,10,18,5,7,13,16,22]:
        if s.game.extra_ball.position < 10:
            p = [275,1002]
            dirty_rects.append(screen.blit(extra_ball, p))
            pygame.display.update(dirty_rects)
    elif num in [3,11,19,6,8,14,20,23]:
        if s.game.extra_ball.position < 15:
            p = [456,1002]
            dirty_rects.append(screen.blit(extra_ball, p))
            p = [595,972]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)

def clear_odds(s, num):
    global screen

    dirty_rects = []
    if s.game.odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (178,815), pygame.Rect(178,815,84,107)))
    if s.game.odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (223,769), pygame.Rect(223,769,74,115)))
    if s.game.odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (362,766), pygame.Rect(362,766,63,120)))
    if s.game.odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (405,786), pygame.Rect(405,786,63,120)))
    if s.game.odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (455,811), pygame.Rect(455,811,58,120)))
    if s.game.odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (566,770), pygame.Rect(566,770,54,120)))
    if s.game.odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (615,818), pygame.Rect(615,818,51,118)))
    if s.game.odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (659,757), pygame.Rect(659,757,51,118)))

    pygame.display.update(dirty_rects)

def draw_odds_animation(s, num):
    global screen
    dirty_rects = []
    if num in [0,11,17]:
        if s.game.odds.position != 1:
            p = [178,815]
            dirty_rects.append(screen.blit(o1, p))
            pygame.display.update(dirty_rects)
            return
    if num in [1,10,18]:
        if s.game.odds.position != 2:
            p = [223,769]
            dirty_rects.append(screen.blit(o2, p))
            pygame.display.update(dirty_rects)
            return
    if num in [4,12,19]:
        if s.game.odds.position != 3:
            p = [362,766]
            dirty_rects.append(screen.blit(o3, p))
            pygame.display.update(dirty_rects)
            return
    if num in [3,9,20]:
        if s.game.odds.position != 4:
            p = [405,786]
            dirty_rects.append(screen.blit(o4, p))
            pygame.display.update(dirty_rects)
            return
    if num in [5,13,21]:
        if s.game.odds.position != 5:
            p = [455,811]
            dirty_rects.append(screen.blit(o5, p))
            pygame.display.update(dirty_rects)
            return
    if num in [6,14,22]:
        if s.game.odds.position != 6:
            p = [566,770]
            dirty_rects.append(screen.blit(o6, p))
            pygame.display.update(dirty_rects)
            return
    if num in [7,16,23]:
        if s.game.odds.position != 7:
            p = [615,818]
            dirty_rects.append(screen.blit(o7, p))
            pygame.display.update(dirty_rects)
            return
    if num in [8,15,24]:
        if s.game.odds.position != 8:
            p = [659,757]
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
        dirty_rects.append(screen.blit(bg_gi, (36,248), pygame.Rect(36,248,144,34)))
    if s.game.super_card.position < 8:
        dirty_rects.append(screen.blit(bg_gi, (539,246), pygame.Rect(539,246,144,34)))
    if s.game.corners.status == False:
        dirty_rects.append(screen.blit(bg_gi, (365,636), pygame.Rect(365,636,98,42)))
    if s.game.yellow_star.status == False:
        dirty_rects.append(screen.blit(bg_gi, (34,980), pygame.Rect(34,980,58,55)))
    if s.game.red_star.status == False:
        dirty_rects.append(screen.blit(bg_gi, (634,980), pygame.Rect(634,980,58,55)))
    if s.game.left_special_card.status == False:
        dirty_rects.append(screen.blit(bg_gi, (57,505), pygame.Rect(57,505,100,34)))
    if s.game.right_special_card.status == False:
        dirty_rects.append(screen.blit(bg_gi, (565,504), pygame.Rect(565,504,100,34)))
    pygame.display.update(dirty_rects)
    return

def animate_mixer1(s):
    global screen
    dirty_rects = []
    if s.game.super_card.position < 4:
        p = [36,248]
        dirty_rects.append(screen.blit(sc, p))
        pygame.display.update(dirty_rects)
        return

def animate_mixer2(s):
    global screen
    dirty_rects = []
    if s.game.super_card.position < 8:
        p = [539,246]
        dirty_rects.append(screen.blit(sc, p))
    if s.game.left_special_card.status == False:
        p = [57,505]
        dirty_rects.append(screen.blit(special_card, p))
    pygame.display.update(dirty_rects)
    return

def animate_mixer3(s):
    global screen
    dirty_rects = []
    if s.game.corners.status == False:
        p = [365,636]
        dirty_rects.append(screen.blit(three_four, p))
    if s.game.red_star.status == False:
        p = [634,980]
        dirty_rects.append(screen.blit(star, p))
        s.game.coils.redROLamp.pulse(85)
    if s.game.yellow_star.status == False:
        p = [34,980]
        dirty_rects.append(screen.blit(star, p))
        s.game.coils.yellowROLamp.pulse(85)
    pygame.display.update(dirty_rects)
    return

def animate_mixer4(s):
    global screen
    dirty_rects = []
    if s.game.right_special_card.status == False:
        p = [565,504]
        dirty_Rects.append(screen.blit(special_card, p))
    pygame.display.update(dirty_rects)
    return

def clear_features(s, num):
    global screen
    dirty_rects = []
    if s.game.before_fourth.status == False:
        dirty_rects.append(screen.blit(bg_gi, (14,686), pygame.Rect(14,686,81,64)))
    if s.game.before_fifth.status == False:
        dirty_rects.append(screen.blit(bg_gi, (627,684), pygame.Rect(627,684,81,64)))

    if s.game.selection_feature.position < 2:
        dirty_rects.append(screen.blit(bg_gi, (104,686), pygame.Rect(104,686,32,40)))
    if s.game.selection_feature.position < 3:
        dirty_rects.append(screen.blit(bg_gi, (144,686), pygame.Rect(144,686,32,40)))
    if s.game.selection_feature.position < 4:
        dirty_rects.append(screen.blit(bg_gi, (182,686), pygame.Rect(182,686,32,40)))
    if s.game.selection_feature.position < 5:
        dirty_rects.append(screen.blit(bg_gi, (215,687), pygame.Rect(215,687,40,37)))
    if s.game.selection_feature.position < 7:
        dirty_rects.append(screen.blit(bg_gi, (295,686), pygame.Rect(295,686,40,37)))
        if s.game.selection_feature_relay.status == False:
            dirty_rects.append(screen.blit(bg_gi, (114,726), pygame.Rect(114,726,117,43)))
            dirty_rects.append(screen.blit(bg_gi, (240,726), pygame.Rect(240,726,117,43)))
            dirty_rects.append(screen.blit(bg_gi, (368,726), pygame.Rect(368,726,117,43)))
            dirty_rects.append(screen.blit(bg_gi, (494,726), pygame.Rect(494,726,117,43)))
    if s.game.selection_feature.position < 6:
        dirty_rects.append(screen.blit(bg_gi, (256,686), pygame.Rect(256,686,40,37)))
    if s.game.selection_feature.position < 8:
        dirty_rects.append(screen.blit(bg_gi, (334,686), pygame.Rect(334,686,40,37)))
    if s.game.selection_feature.position < 9:
        dirty_rects.append(screen.blit(bg_gi, (374,688), pygame.Rect(374,688,40,37)))
    if s.game.selection_feature.position < 10:
        dirty_rects.append(screen.blit(bg_gi, (412,687), pygame.Rect(412,687,40,37)))
    if s.game.selection_feature.position < 11:
        dirty_rects.append(screen.blit(bg_gi, (453,686), pygame.Rect(453,686,40,37)))

    pygame.display.update(dirty_rects)

def draw_feature_animation(s, num):
    global screen
    dirty_rects = []
    if num in [4,15,10,21]:
        if s.game.before_fourth.status == False:
            p = [14,686]
            dirty_rects.append(screen.blit(before_fourth, p))
        if s.game.before_fifth.status == False and s.game.before_fourth.status == True:
            p = [627,684]
            dirty_rects.append(screen.blit(before_fourth, p))
        pygame.display.update(dirty_rects)
        return
   
    if num in [0,11,22]:
        if s.game.selection_feature.position < 2:
            p = [104,686]
            dirty_rects.append(screen.blit(s_arrow, p))
            pygame.display.update(dirty_rects)
            return
    if num in [9,20,23]:
        if s.game.selection_feature.position < 3:
            p = [144,686]
            dirty_rects.append(screen.blit(s_arrow, p))
            pygame.display.update(dirty_rects)
            return
    if num in [1,12,24]:
        if s.game.selection_feature.position < 4:
            p = [182,686]
            dirty_rects.append(screen.blit(s_arrow, p))
            pygame.display.update(dirty_rects)
            return
    if num in [2,13]:
        if s.game.selection_feature.position < 6:
            p = [215,687]
            dirty_rects.append(screen.blit(s_number, p))
            p = [295,686]
            dirty_rects.append(screen.blit(s_number, p))
            pygame.display.update(dirty_rects)
            return
    if num in [3,14,4,15]:
        if s.game.selection_feature.position < 7:
            p = [256,686]
            dirty_rects.append(screen.blit(s_number, p))
        if s.game.selection_feature_relay.status == False:
            p = [114,726]
            dirty_rects.append(screen.blit(select_feature, p))
            p = [240,726]
            dirty_rects.append(screen.blit(select_feature, p))
            p = [368,726]
            dirty_rects.append(screen.blit(select_feature, p))
            p = [494,726]
            dirty_rects.append(screen.blit(select_feature, p))
        pygame.display.update(dirty_rects)
        return
    if num in [5,16]:
        if s.game.selection_feature.position < 8:
            p = [334,686]
            dirty_rects.append(screen.blit(s_number, p))
        pygame.display.update(dirty_rects)
        return
    if num in [6,17]:
        if s.game.selection_feature.position < 9:
            p = [374,688]
            dirty_rects.append(screen.blit(s_number, p))
            pygame.display.update(dirty_rects)
            return
    if num in [7,18]:
        if s.game.selection_feature.position < 10:
            p = [412,687]
            dirty_rects.append(screen.blit(s_number, p))
            pygame.display.update(dirty_rects)
            return
    if num in [8,19]:
        if s.game.selection_feature.position < 11:
            p = [453,686]
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

