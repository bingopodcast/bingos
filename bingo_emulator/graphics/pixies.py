
import pygame
import random

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

meter = pygame.image.load('graphics/assets/silver_register_cover.png').convert()
eb = pygame.image.load('pixies/assets/eb.png').convert_alpha()
extra_ball = pygame.image.load('pixies/assets/extra_ball.png').convert_alpha()
extra_balls = pygame.image.load('pixies/assets/extra_balls.png').convert_alpha()
o1 = pygame.image.load('pixies/assets/odds1.png').convert_alpha()
o2 = pygame.image.load('pixies/assets/odds2.png').convert_alpha()
o3 = pygame.image.load('pixies/assets/odds3.png').convert_alpha()
o4 = pygame.image.load('pixies/assets/odds4.png').convert_alpha()
o5 = pygame.image.load('pixies/assets/odds5.png').convert_alpha()
o6 = pygame.image.load('pixies/assets/odds6.png').convert_alpha()
o7 = pygame.image.load('pixies/assets/odds7.png').convert_alpha()
o8 = pygame.image.load('pixies/assets/odds8.png').convert_alpha()
star = pygame.image.load('pixies/assets/rollover.png').convert_alpha()
number = pygame.image.load('pixies/assets/number.png').convert_alpha()
tilt = pygame.image.load('pixies/assets/tilt.png').convert_alpha()
scoring = pygame.image.load('pixies/assets/left_feature.png').convert_alpha()
select_now = pygame.image.load('pixies/assets/select_now.png').convert_alpha()
red_number = pygame.image.load('pixies/assets/red_number.png').convert_alpha()
spotted_arrow = pygame.image.load('pixies/assets/spotted_arrow.png').convert_alpha()
before_fourth = pygame.image.load('pixies/assets/before_fourth.png').convert_alpha()
s_number = pygame.image.load('pixies/assets/s_number.png').convert_alpha()
corners = pygame.image.load('pixies/assets/corners.png').convert_alpha()
diagonals_score = pygame.image.load('pixies/assets/diagonals_score.png').convert_alpha()
letter1 = pygame.image.load('pixies/assets/letter1.png').convert_alpha()
letter2 = pygame.image.load('pixies/assets/letter2.png').convert_alpha()
letter3 = pygame.image.load('pixies/assets/letter3.png').convert_alpha()
letter4 = pygame.image.load('pixies/assets/letter4.png').convert_alpha()
letter5 = pygame.image.load('pixies/assets/letter5.png').convert_alpha()
letter6 = pygame.image.load('pixies/assets/letter6.png').convert_alpha()
lite_a_name = pygame.image.load('pixies/assets/lite_a_name.png').convert_alpha()
special_arrow = pygame.image.load('pixies/assets/special_arrow.png').convert_alpha()
d_arrow = pygame.image.load('pixies/assets/d_arrow.png').convert_alpha()
diagonal_arrow = pygame.image.load('pixies/assets/diagonal_arrow.png').convert_alpha()
left_feature = pygame.image.load('pixies/assets/left_feature.png').convert_alpha()
right_feature = pygame.image.load('pixies/assets/right_feature.png').convert_alpha()

class scorereel():
    """ Score Reels are used to count replays """
    def __init__(self, pos, image):
        self.position = pos
        self.default_y = self.position[1]
        self.image = pygame.image.load(image).convert()

reel1 = scorereel([109,840], "graphics/assets/white_reel.png")
reel10 = scorereel([90,840], "graphics/assets/white_reel.png")
reel100 = scorereel([71,840], "graphics/assets/white_reel.png")

def display(s, replays=0, menu=False):
    
    meter.set_colorkey((255,0,252))
    meter_position = [62,840]

    screen.blit(reel1.image, reel1.position)
    screen.blit(reel10.image, reel10.position)
    screen.blit(reel100.image, reel100.position)
    screen.blit(meter, meter_position)

    backglass_position = [0, 0]
    backglass = pygame.Surface(screen.get_size(), flags=pygame.SRCALPHA)
    backglass.fill((0, 0, 0))
    if menu == True:
        backglass = pygame.image.load('pixies/assets/pixies_menu.png')
    else:
        if (s.game.anti_cheat.status == True):
            backglass = pygame.image.load('pixies/assets/pixies_gi.png')
        else:
            backglass = pygame.image.load('pixies/assets/pixies_off.png')
    backglass = pygame.transform.scale(backglass, (720, 1280))
    
    screen.blit(backglass, backglass_position)

    if s.game.tilt.status == True:
        p = [191,253]
        screen.blit(letter1, p)
        p = [253,263]
        screen.blit(letter2, p)
        p = [295,266]
        screen.blit(letter3, p)
        p = [360,267]
        screen.blit(letter4, p)
        p = [404,265]
        screen.blit(letter5, p)
        p = [464,253]
        screen.blit(letter6, p)
    else:
        if s.game.lite_a_name.status == True:
            p = [568,252]
            screen.blit(lite_a_name, p)

        if s.game.name.position >= 1:
            p = [191,253]
            screen.blit(letter1, p)
        if s.game.name.position >= 2:
            p = [253,263]
            screen.blit(letter2, p)
        if s.game.name.position >= 3:
            p = [295,266]
            screen.blit(letter3, p)
        if s.game.name.position >= 4:
            p = [360,267]
            screen.blit(letter4, p)
        if s.game.name.position >= 5:
            p = [404,265]
            screen.blit(letter5, p)
        if s.game.name.position >= 6:
            p = [464,253]
            screen.blit(letter6, p)

    if s.game.extra_ball.position == 1:
        eb_position = [100,981]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 2:
        eb_position = [133,981]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 3:
        eb_position = [168,981]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 4:
        eb_position = [204,981]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 5:
        eb_position = [238,981]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 6:
        eb_position = [277,981]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 7:
        eb_position = [312,981]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 8:
        eb_position = [347,981]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 9:
        eb_position = [382,981]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 10:
        eb_position = [416,981]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 11:
        eb_position = [458,981]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 12:
        eb_position = [492,981]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 13:
        eb_position = [526,979]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 14:
        eb_position = [560,979]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 15:
        eb_position = [596,977]
        screen.blit(eb, eb_position)

    if s.game.extra_ball.position >= 5 and s.game.extra_ball.position < 10:
        eb_pos = [101,1008]
        screen.blit(extra_ball, eb_pos)
    if s.game.extra_ball.position >= 10 and s.game.extra_ball.position < 15:
        eb_pos = [279,1008]
        screen.blit(extra_ball, eb_pos)
    if s.game.extra_ball.position == 15:
        eb_pos = [457,1007]
        screen.blit(extra_ball, eb_pos)

    if s.game.odds.position > 0:
        if s.game.odds.position == 1:
            odds_position = [158,770]
            screen.blit(o1, odds_position)
        if s.game.odds.position == 2:
            odds_position = [207,770]
            screen.blit(o2, odds_position)
        if s.game.odds.position == 3:
            odds_position = [440,768]
            screen.blit(o3, odds_position)
        if s.game.odds.position == 4:
            odds_position = [499,768]
            screen.blit(o4, odds_position)
        if s.game.odds.position == 5:
            odds_position = [162,855]
            screen.blit(o5, odds_position)
        if s.game.odds.position == 6:
            odds_position = [208,856]
            screen.blit(o6, odds_position)
        if s.game.odds.position == 7:
            odds_position = [445,855]
            screen.blit(o7, odds_position)
        if s.game.odds.position == 8:
            odds_position = [500,855]
            screen.blit(o8, odds_position)

    if s.game.red_star.status == True:
        rs_position = [644,970]
        screen.blit(star, rs_position)

    if s.game.corners.status == True:
        corners_position = [83,328]
        screen.blit(corners, corners_position)

    if s.game.diagonal_scoring.position == 1:
        p = [311,327]
        screen.blit(d_arrow, p)
    if s.game.diagonal_scoring.position == 2:
        p = [351,327]
        screen.blit(d_arrow, p)
    if s.game.diagonal_scoring.position == 3:
        p = [393,327]
        screen.blit(d_arrow, p)
        corners_position = [412,328]
        screen.blit(diagonals_score, corners_position)

    if s.game.special_pocket.status == True:
        p = [20,388]
        screen.blit(left_feature, p)
    if s.game.pocket.position == 1:
        p = [83,650]
        screen.blit(special_arrow, p)
    if s.game.pocket.position == 2:
        p = [82,611]
        screen.blit(special_arrow, p)
    if s.game.pocket.position == 3:
        p = [81,572]
        screen.blit(special_arrow, p)
    if s.game.pocket.position == 4:
        p = [82,535]
        screen.blit(special_arrow, p)
    if s.game.pocket.position == 5:
        p = [84,495]
        screen.blit(special_arrow, p)
    if s.game.pocket.position == 6:
        p = [21,443]
        screen.blit(left_feature, p)

    if s.game.diagonals.position == 1:
        p = [596,648]
        screen.blit(diagonal_arrow, p)
    if s.game.diagonals.position == 2:
        p = [599,611]
        screen.blit(diagonal_arrow, p)
    if s.game.diagonals.position == 3:
        p = [596,569]
        screen.blit(diagonal_arrow, p)
    if s.game.diagonals.position == 4:
        p = [598,533]
        screen.blit(diagonal_arrow, p)
    if s.game.diagonals.position == 5:
        p = [597,494]
        screen.blit(diagonal_arrow, p)
    if s.game.diagonals.position == 6:
        p = [529,436]
        screen.blit(right_feature, p)

    if s.game.super_diagonal.status == True:
        p = [528,382]
        screen.blit(right_feature, p)

    if s.game.tilt.status == False:
        if s.holes:
            if 1 in s.holes:
                p = [211,552]
                screen.blit(number, p)
            if 2 in s.holes:
                p = [211,493]
                screen.blit(number, p)
            if 3 in s.holes:
                p = [451,610]
                screen.blit(number, p)
            if 4 in s.holes:
                p = [269,376]
                screen.blit(number, p)
            if 5 in s.holes:
                p = [335,611]
                screen.blit(number, p)
            if 6 in s.holes:
                p = [448,377]
                screen.blit(number, p)
            if 7 in s.holes:
                p = [271,611]
                screen.blit(number, p)
            if 8 in s.holes:
                p = [449,435]
                screen.blit(number, p)
            if 9 in s.holes:
                p = [211,377]
                screen.blit(number, p)
            if 10 in s.holes:
                p = [213,435]
                screen.blit(number, p)
            if 11 in s.holes:
                p = [214,612]
                screen.blit(number, p)
            if 12 in s.holes:
                p = [393,492]
                screen.blit(number, p)
            if 13 in s.holes:
                p = [331,551]
                screen.blit(number, p)
            if 14 in s.holes:
                p = [333,435]
                screen.blit(number, p)
            if 15 in s.holes:
                p = [329,375]
                screen.blit(number, p)
            if 16 in s.holes:
                p = [333,494]
                screen.blit(number, p)
            if 17 in s.holes:
                p = [450,551]
                screen.blit(number, p)
            if 18 in s.holes:
                p = [274,493]
                screen.blit(number, p)
            if 19 in s.holes:
                p = [273,435]
                screen.blit(number, p)
            if 20 in s.holes:
                p = [393,434]
                screen.blit(number, p)
            if 21 in s.holes:
                p = [394,552]
                screen.blit(number, p)
            if 22 in s.holes:
                p = [274,552]
                screen.blit(number, p)
            if 23 in s.holes:
                p = [394,610]
                screen.blit(number, p)
            if 24 in s.holes:
                p = [392,377]
                screen.blit(number, p)
            if 25 in s.holes:
                p = [451,492]
                screen.blit(number, p)


    if s.game.tilt.status == True:
        tilt_position = [80,775]
        screen.blit(tilt, tilt_position)

    if s.game.selection_feature.position == 1:
        p = [160,713]
        screen.blit(d_arrow, p)
    if s.game.selection_feature.position == 2:
        p = [201,713]
        screen.blit(d_arrow, p)
    if s.game.selection_feature.position == 3:
        p = [243,713]
        screen.blit(d_arrow, p)
    if s.game.selection_feature.position >= 4:
        p = [277,716]
        screen.blit(s_number, p)
    if s.game.selection_feature.position >= 5:
        p = [320,716]
        screen.blit(s_number, p)
    if s.game.selection_feature.position >= 6:
        p = [360,716]
        screen.blit(s_number, p)
    if s.game.selection_feature.position >= 7:
        p = [404,716]
        screen.blit(s_number, p)
    if s.game.selection_feature.position >= 8:
        p = [447,716]
        screen.blit(s_number, p)
    if s.game.selection_feature.position >= 9:
        p = [489,714]
        screen.blit(s_number, p)
    if s.game.selection_feature.position >= 10:
        p = [531,714]
        screen.blit(s_number, p)

    if (s.game.select_spots.status == True or s.game.selection_feature_relay.status == True) and s.game.before_fourth.status == True and s.game.ball_count.position == 3:
        p = [153,674]
        screen.blit(select_now, p)

    if (s.game.select_spots.status == True or s.game.selection_feature_relay.status == True) and s.game.before_fifth.status == True and s.game.ball_count.position == 4:
        p = [153,674]
        screen.blit(select_now, p)

    if s.game.before_fourth.status == True and (s.game.selection_feature.position > 3):
        p = [5,694]
        screen.blit(before_fourth, p)
    if s.game.before_fifth.status == True and (s.game.selection_feature.position > 3):
        p = [565,694]
        screen.blit(before_fourth, p)

    if s.game.before_fourth.status == True:
        if s.game.ball_count.position < 4:
            if s.game.select_spots.status == True:
                if s.game.selection_feature.position >= 4:
                    if s.game.spotted.position == 0:
                        p = [281,685]
                        screen.blit(spotted_arrow, p)
                        #19
                        p = [273,435]
                        screen.blit(red_number, p)
                if s.game.selection_feature.position >= 5:
                    if s.game.spotted.position == 1:
                        p = [325,683]
                        screen.blit(spotted_arrow, p)
                        #20
                        p = [393,434]
                        screen.blit(red_number, p)
                if s.game.selection_feature.position >= 6:
                    if s.game.spotted.position == 2:
                        p = [360,682]
                        screen.blit(spotted_arrow, p)
                        #21
                        p = [394,552]
                        screen.blit(red_number, p)
                if s.game.selection_feature.position >= 7:
                    if s.game.spotted.position == 3:
                        p = [409,683]
                        screen.blit(spotted_arrow, p)
                        #22
                        p = [274,552]
                        screen.blit(red_number, p)
                if s.game.selection_feature.position >= 8:
                    if s.game.spotted.position == 4:
                        p = [451,682]
                        screen.blit(spotted_arrow, p)
                        #25
                        p = [451,492]
                        screen.blit(red_number, p)
                if s.game.selection_feature.position >= 9:
                    if s.game.spotted.position == 5:
                        p = [494,682]
                        screen.blit(spotted_arrow, p)
                        #10
                        p = [213,435]
                        screen.blit(red_number, p)
                if s.game.selection_feature.position >= 10:
                    if s.game.spotted.position == 6:
                        p = [536,682]
                        screen.blit(spotted_arrow, p)
                        #16
                        p = [333,494]
                        screen.blit(red_number, p)
                

    if s.game.before_fifth.status == True:
        if s.game.ball_count.position < 5:
            if s.game.select_spots.status == True:
                if s.game.selection_feature.position >= 4:
                    if s.game.spotted.position == 0:
                        p = [281,685]
                        screen.blit(spotted_arrow, p)
                        #19
                        p = [273,435]
                        screen.blit(red_number, p)
                if s.game.selection_feature.position >= 5:
                    if s.game.spotted.position == 1:
                        p = [325,683]
                        screen.blit(spotted_arrow, p)
                        #20
                        p = [393,434]
                        screen.blit(red_number, p)
                if s.game.selection_feature.position >= 6:
                    if s.game.spotted.position == 2:
                        p = [360,682]
                        screen.blit(spotted_arrow, p)
                        #21
                        p = [394,552]
                        screen.blit(red_number, p)
                if s.game.selection_feature.position >= 7:
                    if s.game.spotted.position == 3:
                        p = [409,683]
                        screen.blit(spotted_arrow, p)
                        #22
                        p = [274,552]
                        screen.blit(red_number, p)
                if s.game.selection_feature.position >= 8:
                    if s.game.spotted.position == 4:
                        p = [451,682]
                        screen.blit(spotted_arrow, p)
                        #25
                        p = [451,492]
                        screen.blit(red_number, p)
                if s.game.selection_feature.position >= 9:
                    if s.game.spotted.position == 5:
                        p = [494,682]
                        screen.blit(spotted_arrow, p)
                        #10
                        p = [213,435]
                        screen.blit(red_number, p)
                if s.game.selection_feature.position >= 10:
                    if s.game.spotted.position == 6:
                        p = [536,682]
                        screen.blit(spotted_arrow, p)
                        #16
                        p = [333,494]
                        screen.blit(red_number, p)


    if s.game.eb_play.status == True:
        p = [29,989]
        screen.blit(extra_balls, p)

    pygame.display.update()

def eb_animation(num):
    global screen
    if num == 9:
        eb_position = [100,981]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 8:
        eb_position = [133,981]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 7:
        eb_position = [168,981]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 6:
        eb_position = [204,981]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 5:
        eb_position = [238,981]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 4:
        eb_position = [277,981]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 3:
        eb_position = [312,981]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 2:
        eb_position = [347,981]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 1:
        eb_position = [382,981]
        screen.blit(eb, eb_position)
        pygame.display.update()


def feature_animation(num):
    global screen
    if num == 6:
        corners_position = [83,328]
        screen.blit(corners, corners_position)
        pygame.display.update()

    if num == 5:
        rs_position = [644,970]
        screen.blit(star, rs_position)
        pygame.display.update()

    if num == 4:
        rs_position = [644,970]
        screen.blit(star, rs_position)
        pygame.display.update()

    if num == 3:
        p = [412,328]
        screen.blit(corners, p)
        pygame.display.update()
    
    if num == 2:
        p = [83,328]
        screen.blit(corners, p)
        pygame.display.update()
   
    if num == 1:
        p = [412,328]
        screen.blit(corners, p)
        pygame.display.update()

def odds_animation(num):
    global screen
    if num == 5:
        odds_position = [158,770]
        o = pygame.image.load('pixies/assets/odds1.png').convert_alpha()
        screen.blit(o, odds_position)
        pygame.display.update()
    if num == 4:
        odds_position = [207,770]
        o = pygame.image.load('pixies/assets/odds2.png').convert_alpha()
        screen.blit(o, odds_position)
        pygame.display.update()
    if num == 3:
        odds_position = [440,768]
        o = pygame.image.load('pixies/assets/odds3.png').convert_alpha()
        screen.blit(o, odds_position)
        pygame.display.update()
    if num == 2:
        odds_position = [499,768]
        o = pygame.image.load('pixies/assets/odds4.png').convert_alpha()
        screen.blit(o, odds_position)
        pygame.display.update()
    if num == 1:
        odds_position = [162,855]
        o = pygame.image.load('pixies/assets/odds5.png').convert_alpha()
        screen.blit(o, odds_position)
        pygame.display.update()
