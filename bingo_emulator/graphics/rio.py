
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
        backglass = pygame.image.load('rio/assets/rio_menu.png')
    else:
        if (s.game.anti_cheat.status == True):
            backglass = pygame.image.load('rio/assets/rio_gi.png')
        else:
            backglass = pygame.image.load('rio/assets/rio_off.png')
    backglass = pygame.transform.scale(backglass, (720, 1280))
    
    screen.blit(backglass, backglass_position)

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

    if (s.game.select_spots.status == True or s.game.selection_feature_relay.status == True) and s.game.before_fourth.status == True and s.game.ball_count.position == 3:
        p = [493,686]
        screen.blit(select_now, p)
    
    if (s.game.select_spots.status == True or s.game.selection_feature_relay.status == True) and s.game.before_fifth.status == True and s.game.ball_count.position == 4:
        p = [493,686]
        screen.blit(select_now, p)

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

def eb_animation(num):
    global screen
    if num == 9:
        eb_position = [96,972]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 8:
        eb_position = [129,972]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 7:
        eb_position = [163,972]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 6:
        eb_position = [199,972]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 5:
        eb_position = [234,972]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 4:
        eb_position = [275,972]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 3:
        eb_position = [310,972]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 2:
        eb_position = [344,972]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 1:
        eb_position = [379,972]
        screen.blit(eb, eb_position)
        pygame.display.update()


def feature_animation(num):
    global screen
    if num == 6:
        corners_position = [365,636]
        screen.blit(three_four, corners_position)
        pygame.display.update()

    if num == 5:
        rs_position = [634,980]
        screen.blit(star, rs_position)
        pygame.display.update()

    if num == 4:
        ys_position = [34,980]
        screen.blit(star, ys_position)
        pygame.display.update()

    if num == 3:
        p = [37,421]
        screen.blit(sc_arrow, p)
        pygame.display.update()

    if num == 2:
        p = [36,248]
        screen.blit(sc, p)
        pygame.display.update()

    if num == 1:
        p = [539,246]
        screen.blit(sc, p)
        pygame.display.update()


def odds_animation(num):
    global screen

    if num == 5:
        odds_position = [178,815]
        o = pygame.image.load('rio/assets/odds1.png').convert_alpha()
        screen.blit(o, odds_position)
        pygame.display.update()
    if num == 4:
        odds_position = [223,769]
        o = pygame.image.load('rio/assets/odds2.png').convert_alpha()
        screen.blit(o, odds_position)
        pygame.display.update()
    if num == 3:
        odds_position = [362,766]
        o = pygame.image.load('rio/assets/odds3.png').convert_alpha()
        screen.blit(o, odds_position)
        pygame.display.update()
    if num == 2:
        odds_position = [405,786]
        o = pygame.image.load('rio/assets/odds4.png').convert_alpha()
        screen.blit(o, odds_position)
        pygame.display.update()
    if num == 1:
        odds_position = [455,811]
        o = pygame.image.load('rio/assets/odds5.png').convert_alpha()
        screen.blit(o, odds_position)
        pygame.display.update()
