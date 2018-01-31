
import pygame
import random

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

meter = pygame.image.load('graphics/assets/silver_register_cover.png').convert()
eb = pygame.image.load('south_seas/assets/eb.png').convert_alpha()
extra_ball = pygame.image.load('south_seas/assets/extra_ball.png').convert_alpha()
extra_balls = pygame.image.load('south_seas/assets/extra_balls.png').convert_alpha()
o1 = pygame.image.load('south_seas/assets/odds1.png').convert_alpha()
o2 = pygame.image.load('south_seas/assets/odds2.png').convert_alpha()
o3 = pygame.image.load('south_seas/assets/odds3.png').convert_alpha()
o4 = pygame.image.load('south_seas/assets/odds4.png').convert_alpha()
o5 = pygame.image.load('south_seas/assets/odds5.png').convert_alpha()
o6 = pygame.image.load('south_seas/assets/odds6.png').convert_alpha()
o7 = pygame.image.load('south_seas/assets/odds7.png').convert_alpha()
o8 = pygame.image.load('south_seas/assets/odds8.png').convert_alpha()
star = pygame.image.load('south_seas/assets/rollover.png').convert_alpha()
number = pygame.image.load('south_seas/assets/number.png').convert_alpha()
tilt = pygame.image.load('south_seas/assets/tilt.png').convert_alpha()
scoring = pygame.image.load('south_seas/assets/feature.png').convert_alpha()
select_now = pygame.image.load('south_seas/assets/select_now.png').convert_alpha()
red_number = pygame.image.load('south_seas/assets/red_number.png').convert_alpha()
spotted_arrow = pygame.image.load('south_seas/assets/s_arrow.png').convert_alpha()
selection_arrow = pygame.image.load('south_seas/assets/selection_arrow.png').convert_alpha()
before_fourth = pygame.image.load('south_seas/assets/before_fourth.png').convert_alpha()
s_number = pygame.image.load('south_seas/assets/spotted_number.png').convert_alpha()
corners = pygame.image.load('south_seas/assets/corners.png').convert_alpha()
special_arrow = pygame.image.load('south_seas/assets/feature_arrow.png').convert_alpha()
feature = pygame.image.load('south_seas/assets/feature.png').convert_alpha()
bg_menu = pygame.image.load('south_seas/assets/south_seas_menu.png')
bg_gi = pygame.image.load('south_seas/assets/south_seas_gi.png')
bg_off = pygame.image.load('south_seas/assets/south_seas_off.png')

class scorereel():
    """ Score Reels are used to count replays """
    def __init__(self, pos, image):
        self.position = pos
        self.default_y = self.position[1]
        self.image = pygame.image.load(image).convert()

reel1 = scorereel([115,823], "graphics/assets/white_reel.png")
reel10 = scorereel([96,823], "graphics/assets/white_reel.png")
reel100 = scorereel([77,823], "graphics/assets/white_reel.png")

def display(s, replays=0, menu=False):
    
    meter.set_colorkey((255,0,252))
    meter_position = [68,820]

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

    if s.game.extra_ball.position == 1:
        eb_position = [102,953]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 2:
        eb_position = [138,953]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 3:
        eb_position = [173,953]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 4:
        eb_position = [208,953]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 5:
        eb_position = [242,953]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 6:
        eb_position = [280,953]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 7:
        eb_position = [315,951]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 8:
        eb_position = [347,951]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 9:
        eb_position = [382,951]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 10:
        eb_position = [416,951]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 11:
        eb_position = [456,951]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 12:
        eb_position = [490,951]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 13:
        eb_position = [522,951]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 14:
        eb_position = [554,951]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 15:
        eb_position = [590,951]
        screen.blit(eb, eb_position)

    if s.game.extra_ball.position >= 5 and s.game.extra_ball.position < 10:
        eb_pos = [106,979]
        screen.blit(extra_ball, eb_pos)
    if s.game.extra_ball.position >= 10 and s.game.extra_ball.position < 15:
        eb_pos = [280,979]
        screen.blit(extra_ball, eb_pos)
    if s.game.extra_ball.position == 15:
        eb_pos = [455,977]
        screen.blit(extra_ball, eb_pos)

    if s.game.odds.position > 0:
        if s.game.odds.position == 1:
            odds_position = [175,749]
            screen.blit(o1, odds_position)
        if s.game.odds.position == 2:
            odds_position = [432,749]
            screen.blit(o2, odds_position)
        if s.game.odds.position == 3:
            odds_position = [481,751]
            screen.blit(o3, odds_position)
        if s.game.odds.position == 4:
            odds_position = [657,747]
            screen.blit(o4, odds_position)
        if s.game.odds.position == 5:
            odds_position = [190,819]
            screen.blit(o5, odds_position)
        if s.game.odds.position == 6:
            odds_position = [330,879]
            screen.blit(o6, odds_position)
        if s.game.odds.position == 7:
            odds_position = [420,861]
            screen.blit(o7, odds_position)
        if s.game.odds.position == 8:
            odds_position = [639,826]
            screen.blit(o8, odds_position)

    if s.game.red_star.status == True:
        rs_position = [643,947]
        screen.blit(star, rs_position)

    if s.game.corners.status == True:
        corners_position = [25,334]
        screen.blit(corners, corners_position)

    if s.game.super_corners.status == True:
        corners_position = [473,335]
        screen.blit(corners, corners_position)

    if s.game.diagonals_relay.status == True:
        corners_position = [251,335]
        screen.blit(corners, corners_position)

    if s.game.special_pocket.status == True:
        p = [25,390]
        screen.blit(feature, p)
    if s.game.pocket.position == 1:
        p = [88,648]
        screen.blit(special_arrow, p)
    if s.game.pocket.position == 2:
        p = [88,612]
        screen.blit(special_arrow, p)
    if s.game.pocket.position == 3:
        p = [89,573]
        screen.blit(special_arrow, p)
    if s.game.pocket.position == 4:
        p = [90,534]
        screen.blit(special_arrow, p)
    if s.game.pocket.position == 5:
        p = [91,497]
        screen.blit(special_arrow, p)
    if s.game.pocket.position == 6:
        p = [23,443]
        screen.blit(feature, p)

    if s.game.diagonal_scoring.position == 1:
        p = [594,648]
        screen.blit(special_arrow, p)
    if s.game.diagonal_scoring.position == 2:
        p = [596,610]
        screen.blit(special_arrow, p)
    if s.game.diagonal_scoring.position == 3:
        p = [596,570]
        screen.blit(special_arrow, p)
    if s.game.diagonal_scoring.position == 4:
        p = [596,534]
        screen.blit(special_arrow, p)
    if s.game.diagonal_scoring.position == 5:
        p = [594,496]
        screen.blit(special_arrow, p)
    if s.game.diagonal_scoring.position == 6:
        p = [526,440]
        screen.blit(feature, p)

    if s.game.super_diagonal.status == True:
        p = [525,387]
        screen.blit(feature, p)

    if s.game.tilt.status == False:
        if s.holes:
            if 1 in s.holes:
                p = [221,554]
                screen.blit(number, p)
            if 2 in s.holes:
                p = [221,498]
                screen.blit(number, p)
            if 3 in s.holes:
                p = [453,609]
                screen.blit(number, p)
            if 4 in s.holes:
                p = [281,386]
                screen.blit(number, p)
            if 5 in s.holes:
                p = [337,610]
                screen.blit(number, p)
            if 6 in s.holes:
                p = [454,386]
                screen.blit(number, p)
            if 7 in s.holes:
                p = [279,611]
                screen.blit(number, p)
            if 8 in s.holes:
                p = [452,439]
                screen.blit(number, p)
            if 9 in s.holes:
                p = [221,385]
                screen.blit(number, p)
            if 10 in s.holes:
                p = [221,441]
                screen.blit(number, p)
            if 11 in s.holes:
                p = [221,611]
                screen.blit(number, p)
            if 12 in s.holes:
                p = [395,497]
                screen.blit(number, p)
            if 13 in s.holes:
                p = [337,553]
                screen.blit(number, p)
            if 14 in s.holes:
                p = [338,441]
                screen.blit(number, p)
            if 15 in s.holes:
                p = [339,385]
                screen.blit(number, p)
            if 16 in s.holes:
                p = [338,498]
                screen.blit(number, p)
            if 17 in s.holes:
                p = [453,554]
                screen.blit(number, p)
            if 18 in s.holes:
                p = [280,497]
                screen.blit(number, p)
            if 19 in s.holes:
                p = [281,441]
                screen.blit(number, p)
            if 20 in s.holes:
                p = [396,441]
                screen.blit(number, p)
            if 21 in s.holes:
                p = [395,552]
                screen.blit(number, p)
            if 22 in s.holes:
                p = [278,552]
                screen.blit(number, p)
            if 23 in s.holes:
                p = [395,610]
                screen.blit(number, p)
            if 24 in s.holes:
                p = [396,386]
                screen.blit(number, p)
            if 25 in s.holes:
                p = [453,497]
                screen.blit(number, p)


    if s.game.tilt.status == True:
        tilt_position = [80,775]
        screen.blit(tilt, tilt_position)

    if s.game.selection_feature.position == 1:
        p = [167,709]
        screen.blit(selection_arrow, p)
    if s.game.selection_feature.position == 2:
        p = [208,709]
        screen.blit(selection_arrow, p)
    if s.game.selection_feature.position == 3:
        p = [250,709]
        screen.blit(selection_arrow, p)
    if s.game.selection_feature.position >= 4:
        p = [282,703]
        screen.blit(s_number, p)
    if s.game.selection_feature.position >= 5:
        p = [322,703]
        screen.blit(s_number, p)
    if s.game.selection_feature.position >= 6:
        p = [360,703]
        screen.blit(s_number, p)
    if s.game.selection_feature.position >= 7:
        p = [404,703]
        screen.blit(s_number, p)
    if s.game.selection_feature.position >= 8:
        p = [445,703]
        screen.blit(s_number, p)
    if s.game.selection_feature.position >= 9:
        p = [484,703]
        screen.blit(s_number, p)
    if s.game.selection_feature.position >= 10:
        p = [525,703]
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

    if s.game.before_fourth.status == True and (s.game.selection_feature.position > 3):
        p = [16,691]
        screen.blit(before_fourth, p)
    if s.game.before_fifth.status == True and (s.game.selection_feature.position > 3):
        p = [562,693]
        screen.blit(before_fourth, p)

    if s.game.before_fourth.status == True:
        if s.game.ball_count.position < 4:
            if s.game.select_spots.status == True:
                if s.game.selection_feature.position >= 4:
                    if s.game.spotted.position == 0:
                        p = [282,675]
                        screen.blit(spotted_arrow, p)
                        #19
                        p = [281,441]
                        screen.blit(red_number, p)
                if s.game.selection_feature.position >= 5:
                    if s.game.spotted.position == 1:
                        p = [324,675]
                        screen.blit(spotted_arrow, p)
                        #20
                        p = [396,441]
                        screen.blit(red_number, p)
                if s.game.selection_feature.position >= 6:
                    if s.game.spotted.position == 2:
                        p = [363,675]
                        screen.blit(spotted_arrow, p)
                        #21
                        p = [395,552]
                        screen.blit(red_number, p)
                if s.game.selection_feature.position >= 7:
                    if s.game.spotted.position == 3:
                        p = [405,675]
                        screen.blit(spotted_arrow, p)
                        #22
                        p = [278,552]
                        screen.blit(red_number, p)
                if s.game.selection_feature.position >= 8:
                    if s.game.spotted.position == 4:
                        p = [446,675]
                        screen.blit(spotted_arrow, p)
                        #25
                        p = [453,497]
                        screen.blit(red_number, p)
                if s.game.selection_feature.position >= 9:
                    if s.game.spotted.position == 5:
                        p = [486,675]
                        screen.blit(spotted_arrow, p)
                        #10
                        p = [221,441]
                        screen.blit(red_number, p)
                if s.game.selection_feature.position >= 10:
                    if s.game.spotted.position == 6:
                        p = [528,675]
                        screen.blit(spotted_arrow, p)
                        #16
                        p = [338,498]
                        screen.blit(red_number, p)
                

    if s.game.before_fifth.status == True:
        if s.game.ball_count.position < 5:
            if s.game.select_spots.status == True:
                if s.game.selection_feature.position >= 4:
                    if s.game.spotted.position == 0:
                        p = [282,675]
                        screen.blit(spotted_arrow, p)
                        #19
                        p = [281,441]
                        screen.blit(red_number, p)
                if s.game.selection_feature.position >= 5:
                    if s.game.spotted.position == 1:
                        p = [324,675]
                        screen.blit(spotted_arrow, p)
                        #20
                        p = [396,441]
                        screen.blit(red_number, p)
                if s.game.selection_feature.position >= 6:
                    if s.game.spotted.position == 2:
                        p = [363,675]
                        screen.blit(spotted_arrow, p)
                        #21
                        p = [395,552]
                        screen.blit(red_number, p)
                if s.game.selection_feature.position >= 7:
                    if s.game.spotted.position == 3:
                        p = [405,675]
                        screen.blit(spotted_arrow, p)
                        #22
                        p = [278,552]
                        screen.blit(red_number, p)
                if s.game.selection_feature.position >= 8:
                    if s.game.spotted.position == 4:
                        p = [446,675]
                        screen.blit(spotted_arrow, p)
                        #25
                        p = [453,497]
                        screen.blit(red_number, p)
                if s.game.selection_feature.position >= 9:
                    if s.game.spotted.position == 5:
                        p = [486,675]
                        screen.blit(spotted_arrow, p)
                        #10
                        p = [221,441]
                        screen.blit(red_number, p)
                if s.game.selection_feature.position >= 10:
                    if s.game.spotted.position == 6:
                        p = [528,675]
                        screen.blit(spotted_arrow, p)
                        #16
                        p = [338,498]
                        screen.blit(red_number, p)
                

    if s.game.eb_play.status == True:
        p = [26,952]
        screen.blit(extra_balls, p)

    pygame.display.update()

def blink(args):
    dirty_rects = []
    s = args[0]
    b = args[1]
    sn = args[2]

    if b == 0:
        if sn == 1:
            p = [157,674]
            dirty_rects.append(screen.blit(select_now, p))
        pygame.display.update(dirty_rects)
    else:
        dirty_rects.append(screen.blit(bg_gi, (157,674), pygame.Rect(157,674,119,36)))
        pygame.display.update(dirty_rects)
    b = not b

    args = [s,b,sn]

    s.delay(name="blink", delay=0.1, handler=blink, param=args)

def eb_animation(num):
    global screen
    if num == 9:
        eb_position = [102,953]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 8:
        eb_position = [138,953]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 7:
        eb_position = [173,953]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 6:
        eb_position = [208,953]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 5:
        eb_position = [242,953]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 4:
        eb_position = [280,953]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 3:
        eb_position = [315,951]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 2:
        eb_position = [347,951]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 1:
        eb_position = [382,951]
        screen.blit(eb, eb_position)
        pygame.display.update()


def feature_animation(num):
    global screen
    if num == 6:
        screen.blit(corners, corners_position)
        pygame.display.update()

    if num == 5:
        rs_position = [643,947]
        screen.blit(star, rs_position)
        pygame.display.update()

    if num == 4:
        rs_position = [643,947]
        screen.blit(star, rs_position)
        pygame.display.update()

    if num == 3:
        p = [473,335]
        screen.blit(corners, p)
        pygame.display.update()
    
    if num == 2:
        p = [25,334]
        screen.blit(corners, p)
        pygame.display.update()
   
    if num == 1:
        p = [473,335]
        screen.blit(corners, p)
        pygame.display.update()

def odds_animation(num):
    global screen
    if num == 5:
        odds_position = [175,749]
        o = pygame.image.load('south_seas/assets/odds1.png').convert_alpha()
        screen.blit(o, odds_position)
        pygame.display.update()
    if num == 4:
        odds_position = [432,749]
        o = pygame.image.load('south_seas/assets/odds2.png').convert_alpha()
        screen.blit(o, odds_position)
        pygame.display.update()
    if num == 3:
        odds_position = [481,751]
        o = pygame.image.load('south_seas/assets/odds3.png').convert_alpha()
        screen.blit(o, odds_position)
        pygame.display.update()
    if num == 2:
        odds_position = [657,747]
        o = pygame.image.load('south_seas/assets/odds4.png').convert_alpha()
        screen.blit(o, odds_position)
        pygame.display.update()
    if num == 1:
        odds_position = [190,819]
        o = pygame.image.load('south_seas/assets/odds5.png').convert_alpha()
        screen.blit(o, odds_position)
        pygame.display.update()
