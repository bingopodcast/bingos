
import pygame
import random

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

meter = pygame.image.load('graphics/assets/silver_register_cover.png').convert()
eb = pygame.image.load('caravan/assets/eb.png').convert_alpha()
eb_arrow = pygame.image.load('caravan/assets/eb_arrow.png').convert_alpha()
extra_balls = pygame.image.load('caravan/assets/extra_balls.png').convert_alpha()
o1 = pygame.image.load('caravan/assets/odds1.png').convert_alpha()
o2 = pygame.image.load('caravan/assets/odds2.png').convert_alpha()
o3 = pygame.image.load('caravan/assets/odds3.png').convert_alpha()
o4 = pygame.image.load('caravan/assets/odds4.png').convert_alpha()
o5 = pygame.image.load('caravan/assets/odds5.png').convert_alpha()
o6 = pygame.image.load('caravan/assets/odds6.png').convert_alpha()
o7 = pygame.image.load('caravan/assets/odds7.png').convert_alpha()
o8 = pygame.image.load('caravan/assets/odds8.png').convert_alpha()
star = pygame.image.load('caravan/assets/rollover.png').convert_alpha()
number = pygame.image.load('caravan/assets/number.png').convert_alpha()
tilt = pygame.image.load('caravan/assets/tilt.png').convert_alpha()
scoring = pygame.image.load('caravan/assets/feature.png').convert_alpha()
select_now = pygame.image.load('caravan/assets/select_now.png').convert_alpha()
spotted_arrow = pygame.image.load('caravan/assets/selected_arrow.png').convert_alpha()
before_fourth = pygame.image.load('caravan/assets/s_time.png').convert_alpha()
roto_before_fourth = pygame.image.load('caravan/assets/roto_time.png').convert_alpha()
roto = pygame.image.load('caravan/assets/roto.png').convert_alpha()
roto_time = pygame.image.load('caravan/assets/roto_time.png').convert_alpha()
roto0 = pygame.image.load('caravan/assets/roto0.png').convert_alpha()
roto1 = pygame.image.load('caravan/assets/roto1.png').convert_alpha()
roto2 = pygame.image.load('caravan/assets/roto2.png').convert_alpha()
roto3 = pygame.image.load('caravan/assets/roto3.png').convert_alpha()
roto4 = pygame.image.load('caravan/assets/roto4.png').convert_alpha()
roto5 = pygame.image.load('caravan/assets/roto5.png').convert_alpha()
roto6 = pygame.image.load('caravan/assets/roto6.png').convert_alpha()
roto7 = pygame.image.load('caravan/assets/roto7.png').convert_alpha()
s_number = pygame.image.load('caravan/assets/s_number.png').convert_alpha()
corners = pygame.image.load('caravan/assets/feature.png').convert_alpha()
diagonal_score = pygame.image.load('caravan/assets/feature.png').convert_alpha()
letter1 = pygame.image.load('caravan/assets/letter1.png').convert_alpha()
letter2 = pygame.image.load('caravan/assets/letter2.png').convert_alpha()
letter3 = pygame.image.load('caravan/assets/letter3.png').convert_alpha()
letter4 = pygame.image.load('caravan/assets/letter4.png').convert_alpha()
letter5 = pygame.image.load('caravan/assets/letter5.png').convert_alpha()
letter6 = pygame.image.load('caravan/assets/letter6.png').convert_alpha()
lite_a_name = pygame.image.load('caravan/assets/lite_a_name.png').convert_alpha()
special_arrow = pygame.image.load('caravan/assets/sp_arrow.png').convert_alpha()
s_arrow = pygame.image.load('caravan/assets/s_arrow.png').convert_alpha()
score_arrow = pygame.image.load('caravan/assets/score_arrow.png').convert_alpha()
feature = pygame.image.load('caravan/assets/feature.png').convert_alpha()
special_pocket = pygame.image.load('caravan/assets/special_pocket.png').convert_alpha()
red_diagonals = pygame.image.load('caravan/assets/red_diagonals.png').convert_alpha()
eight_balls = pygame.image.load('caravan/assets/eight_balls.png').convert_alpha()
bg_menu = pygame.image.load('caravan/assets/caravan_menu.png')
bg_gi = pygame.image.load('caravan/assets/caravan_gi.png')
bg_off = pygame.image.load('caravan/assets/caravan_off.png')
r1 = pygame.image.load('caravan/assets/r1.png').convert_alpha()
r2 = pygame.image.load('caravan/assets/r2.png').convert_alpha()
r3 = pygame.image.load('caravan/assets/r3.png').convert_alpha()
r4 = pygame.image.load('caravan/assets/r4.png').convert_alpha()
r5 = pygame.image.load('caravan/assets/r5.png').convert_alpha()
r6 = pygame.image.load('caravan/assets/r6.png').convert_alpha()
r7 = pygame.image.load('caravan/assets/r7.png').convert_alpha()
r8 = pygame.image.load('caravan/assets/r8.png').convert_alpha()

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

    if s.game.roto.position == 0:
        p = [278,448]
        screen.blit(roto0, p)
    elif s.game.roto.position == 1:
        p = [278,448]
        screen.blit(roto1, p)
    elif s.game.roto.position == 2:
        p = [278,448]
        screen.blit(roto2, p)
    elif s.game.roto.position == 3:
        p = [278,448]
        screen.blit(roto3, p)
    elif s.game.roto.position == 4:
        p = [278,448]
        screen.blit(roto4, p)
    elif s.game.roto.position == 5:
        p = [278,448]
        screen.blit(roto5, p)
    elif s.game.roto.position == 6:
        p = [278,448]
        screen.blit(roto6, p)
    elif s.game.roto.position == 7:
        p = [278,448]
        screen.blit(roto7, p)

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
        p = [209,241]
        screen.blit(letter1, p)
        p = [265,241]
        screen.blit(letter2, p)
        p = [324,241]
        screen.blit(letter3, p)
        p = [388,241]
        screen.blit(letter4, p)
        p = [430,241]
        screen.blit(letter5, p)
        p = [487,241]
        screen.blit(letter6, p)
    else:
        if s.game.lite_a_name.status == True:
            p = [560,239]
            screen.blit(lite_a_name, p)
        if s.game.name.position >= 1:
            p = [209,241]
            screen.blit(letter1, p)
        if s.game.name.position >= 2:
            p = [265,241]
            screen.blit(letter2, p)
        if s.game.name.position >= 3:
            p = [324,241]
            screen.blit(letter3, p)
        if s.game.name.position >= 4:
            p = [388,241]
            screen.blit(letter4, p)
        if s.game.name.position >= 5:
            p = [430,241]
            screen.blit(letter5, p)
        if s.game.name.position >= 6:
            p = [487,241]
            screen.blit(letter6, p)

    if s.game.extra_ball.position == 1:
        eb_position = [101,985]
        screen.blit(eb_arrow, eb_position)
    if s.game.extra_ball.position == 2:
        eb_position = [136,985]
        screen.blit(eb_arrow, eb_position)
    if s.game.extra_ball.position == 3:
        eb_position = [172,985]
        screen.blit(eb_arrow, eb_position)
    if s.game.extra_ball.position == 4:
        eb_position = [206,985]
        screen.blit(eb_arrow, eb_position)
    if s.game.extra_ball.position == 5:
        eb_position = [240,985]
        screen.blit(eb_arrow, eb_position)
    if s.game.extra_ball.position == 6:
        eb_position = [279,985]
        screen.blit(eb_arrow, eb_position)
    if s.game.extra_ball.position == 7:
        eb_position = [313,985]
        screen.blit(eb_arrow, eb_position)
    if s.game.extra_ball.position == 8:
        eb_position = [349,985]
        screen.blit(eb_arrow, eb_position)
    if s.game.extra_ball.position == 9:
        eb_position = [383,985]
        screen.blit(eb_arrow, eb_position)
    if s.game.extra_ball.position == 10:
        eb_position = [419,985]
        screen.blit(eb_arrow, eb_position)
    if s.game.extra_ball.position == 11:
        eb_position = [459,985]
        screen.blit(eb_arrow, eb_position)
    if s.game.extra_ball.position == 12:
        eb_position = [492,985]
        screen.blit(eb_arrow, eb_position)
    if s.game.extra_ball.position == 13:
        eb_position = [527,985]
        screen.blit(eb_arrow, eb_position)
    if s.game.extra_ball.position == 14:
        eb_position = [563,985]
        screen.blit(eb_arrow, eb_position)
    if s.game.extra_ball.position == 15:
        eb_position = [597,985]
        screen.blit(eb_arrow, eb_position)

    if s.game.extra_ball.position >= 5 and s.game.extra_ball.position < 10:
        eb_pos = [100,1017]
        screen.blit(eb, eb_pos)
    if s.game.extra_ball.position >= 10 and s.game.extra_ball.position < 15:
        eb_pos = [278,1017]
        screen.blit(eb, eb_pos)
    if s.game.extra_ball.position == 15:
        eb_pos = [456,1017]
        screen.blit(eb, eb_pos)

    if s.game.odds.position > 0:
        if s.game.odds.position == 1:
            odds_position = [187,775]
            screen.blit(o1, odds_position)
        if s.game.odds.position == 2:
            odds_position = [225,776]
            screen.blit(o2, odds_position)
        if s.game.odds.position == 3:
            odds_position = [269,802]
            screen.blit(o3, odds_position)
        if s.game.odds.position == 4:
            odds_position = [437,838]
            screen.blit(o4, odds_position)
        if s.game.odds.position == 5:
            odds_position = [514,764]
            screen.blit(o5, odds_position)
        if s.game.odds.position == 6:
            odds_position = [627,769]
            screen.blit(o6, odds_position)
        if s.game.odds.position == 7:
            odds_position = [219,886]
            screen.blit(o7, odds_position)
        if s.game.odds.position == 8:
            odds_position = [648,893]
            screen.blit(o8, odds_position)

    if s.game.red_star.status == True:
        rs_position = [642,982]
        screen.blit(star, rs_position)

    if s.game.corners.status == True:
        corners_position = [525,607]
        screen.blit(corners, corners_position)

    if s.game.super_diagonal.status == True:
        corners_position = [23,388]
        screen.blit(corners, corners_position)
    
    if s.game.diagonal.status == True:
        p = [35,632]
        screen.blit(red_diagonals, p)

    if s.game.diagonal_separate.position == 1:
        p = [111,591]
        screen.blit(score_arrow, p)
    elif s.game.diagonal_separate.position == 2:
        p = [76,559]
        screen.blit(score_arrow, p)
    elif s.game.diagonal_separate.position == 3:
        p = [111,529]
        screen.blit(score_arrow, p)
    elif s.game.diagonal_separate.position == 4:
        p = [78,499]
        screen.blit(score_arrow, p)
    elif s.game.diagonal_separate.position == 5:
        p = [22,441]
        screen.blit(corners, p)

    if s.game.special_pocket.status == True:
        p = [84,318]
        screen.blit(special_pocket, p)
    if s.game.pocket.position == 1:
        p = [273,321]
        screen.blit(special_arrow, p)
    if s.game.pocket.position == 2:
        p = [313,321]
        screen.blit(special_arrow, p)
    if s.game.pocket.position == 3:
        p = [353,321]
        screen.blit(special_arrow, p)
    if s.game.pocket.position == 4:
        p = [389,321]
        screen.blit(special_arrow, p)
    if s.game.pocket.position == 5:
        p = [427,321]
        screen.blit(special_arrow, p)
    if s.game.pocket.position == 6:
        p = [465,316]
        screen.blit(eight_balls, p)

    r1 = [285,450]
    r2 = [339,451]
    r3 = [394,451]
    r4 = [285,505]
    r5 = [393,504]
    r6 = [285,559]
    r7 = [339,560]
    r8 = [393,560]

    if s.game.roto.position == 0:
        r21 = r1
        r13 = r2
        r22 = r3
        r12 = r4
        r18 = r5
        r20 = r6
        r14 = r7
        r19 = r8
    elif s.game.roto.position == 1:
        r12 = r1
        r21 = r2
        r13 = r3
        r20 = r4
        r22 = r5
        r14 = r6
        r19 = r7
        r18 = r8
    elif s.game.roto.position == 2:
        r20 = r1
        r12 = r2
        r21 = r3
        r14 = r4
        r13 = r5
        r19 = r6
        r18 = r7
        r22 = r8
    elif s.game.roto.position == 3:
        r14 = r1
        r20 = r2
        r12 = r3
        r19 = r4
        r21 = r5
        r18 = r6
        r22 = r7
        r13 = r8
    elif s.game.roto.position == 4:
        r19 = r1
        r14 = r2
        r20 = r3
        r18 = r4
        r12 = r5
        r22 = r6
        r13 = r7
        r21 = r8
    elif s.game.roto.position == 5:
        r18 = r1
        r19 = r2
        r14 = r3
        r22 = r4
        r20 = r5
        r13 = r6
        r21 = r7
        r12 = r8
    elif s.game.roto.position == 6:
        r22 = r1
        r18 = r2
        r19 = r3
        r13 = r4
        r14 = r5
        r21 = r6
        r12 = r7
        r20 = r8
    elif s.game.roto.position == 7:
        r13 = r1
        r22 = r2
        r18 = r3
        r21 = r4
        r19 = r5
        r12 = r6
        r20 = r7
        r14 = r8

    if s.game.tilt.status == False:
        if s.holes:
            if 1 in s.holes:
                p = [230,561]
                screen.blit(number, p)
            if 2 in s.holes:
                p = [227,508]
                screen.blit(number, p)
            if 3 in s.holes:
                p = [446,614]
                screen.blit(number, p)
            if 4 in s.holes:
                p = [281,398]
                screen.blit(number, p)
            if 5 in s.holes:
                p = [337,613]
                screen.blit(number, p)
            if 6 in s.holes:
                p = [446,399]
                screen.blit(number, p)
            if 7 in s.holes:
                p = [283,613]
                screen.blit(number, p)
            if 8 in s.holes:
                p = [446,452]
                screen.blit(number, p)
            if 9 in s.holes:
                p = [227,399]
                screen.blit(number, p)
            if 10 in s.holes:
                p = [227,453]
                screen.blit(number, p)
            if 11 in s.holes:
                p = [229,613]
                screen.blit(number, p)
            if 12 in s.holes:
                p = r12
                screen.blit(number, p)
            if 13 in s.holes:
                p = r13
                screen.blit(number, p)
            if 14 in s.holes:
                p = r14
                screen.blit(number, p)
            if 15 in s.holes:
                p = [337,397]
                screen.blit(number, p)
            if 16 in s.holes:
                p = [337,506]
                screen.blit(number, p)
            if 17 in s.holes:
                p = [447,561]
                screen.blit(number, p)
            if 18 in s.holes:
                p = r18
                screen.blit(number, p)
            if 19 in s.holes:
                p = r19
                screen.blit(number, p)
            if 20 in s.holes:
                p = r20
                screen.blit(number, p)
            if 21 in s.holes:
                p = r21
                screen.blit(number, p)
            if 22 in s.holes:
                p = r22
                screen.blit(number, p)
            if 23 in s.holes:
                p = [392,615]
                screen.blit(number, p)
            if 24 in s.holes:
                p = [391,399]
                screen.blit(number, p)
            if 25 in s.holes:
                p = [445,506]
                screen.blit(number, p)


    if s.game.tilt.status == True:
        tilt_position = [148,558]
        screen.blit(tilt, tilt_position)

    if s.game.selection_feature.position == 1:
        p = [197,718]
        screen.blit(s_arrow, p)
    if s.game.selection_feature.position == 2:
        p = [239,718]
        screen.blit(s_arrow, p)
    if s.game.selection_feature.position == 3:
        p = [280,718]
        screen.blit(s_arrow, p)
    if s.game.selection_feature.position >= 4:
        p = [321,716]
        screen.blit(s_number, p)
    if s.game.selection_feature.position >= 5:
        p = [360,716]
        screen.blit(s_number, p)
    if s.game.selection_feature.position >= 6:
        p = [404,716]
        screen.blit(s_number, p)
    if s.game.selection_feature.position >= 7:
        p = [447,716]
        screen.blit(s_number, p)
    if s.game.selection_feature.position >= 8:
        p = [489,716]
        screen.blit(s_number, p)

    if (s.game.select_spots.status == True or s.game.selection_feature_relay.status == True) and s.game.before_fourth.status == True:
        if s.game.ball_count.position == 3:
            s.cancel_delayed(name="blink")
            blink([s,1,1])
        else:
            s.cancel_delayed(name="blink")

    if (s.game.select_spots.status == True or s.game.selection_feature_relay.status == True) and s.game.before_fifth.status == True:
        if s.game.ball_count.position == 4:
            s.cancel_delayed(name="blink")
            blink([s,1,1])
        else:
            s.cancel_delayed(name="blink")

    if s.game.before_fourth.status == True and (s.game.selection_feature.position > 3):
        p = [29,690]
        screen.blit(before_fourth, p)
    if s.game.before_fifth.status == True and (s.game.selection_feature.position > 3):
        p = [533,690]
        screen.blit(before_fourth, p)

    if s.game.before_fourth.status == True:
        if s.game.ball_count.position < 4:
            if s.game.select_spots.status == True:
                if s.game.selection_feature.position >= 4:
                    if s.game.spotted.position == 0:
                        p = [324,685]
                        screen.blit(spotted_arrow, p)
                if s.game.selection_feature.position >= 5:
                    if s.game.spotted.position == 1:
                        p = [368,685]
                        screen.blit(spotted_arrow, p)
                if s.game.selection_feature.position >= 6:
                    if s.game.spotted.position == 2:
                        p = [406,685]
                        screen.blit(spotted_arrow, p)
                if s.game.selection_feature.position >= 7:
                    if s.game.spotted.position == 3:
                        p = [449,684]
                        screen.blit(spotted_arrow, p)
                if s.game.selection_feature.position >= 8:
                    if s.game.spotted.position == 4:
                        p = [492,685]
                        screen.blit(spotted_arrow, p)
                

    if s.game.before_fifth.status == True:
        if s.game.ball_count.position < 5:
            if s.game.select_spots.status == True:
                if s.game.selection_feature.position >= 4:
                    if s.game.spotted.position == 0:
                        p = [324,685]
                        screen.blit(spotted_arrow, p)
                if s.game.selection_feature.position >= 5:
                    if s.game.spotted.position == 1:
                        p = [368,685]
                        screen.blit(spotted_arrow, p)
                if s.game.selection_feature.position >= 6:
                    if s.game.spotted.position == 2:
                        p = [406,685]
                        screen.blit(spotted_arrow, p)
                if s.game.selection_feature.position >= 7:
                    if s.game.spotted.position == 3:
                        p = [449,684]
                        screen.blit(spotted_arrow, p)
                if s.game.selection_feature.position >= 8:
                    if s.game.spotted.position == 4:
                        p = [492,685]
                        screen.blit(spotted_arrow, p)
               
    if s.game.eb_play.status == True:
        p = [24,983]
        screen.blit(extra_balls, p)

    if s.game.roto_feature.status == True:
        p = [538,390]
        screen.blit(roto, p)
        if s.game.before_fourth.status == True:
            p = [528,413]
            screen.blit(roto_time, p)
            if s.game.ball_count.position == 3:
                s.cancel_delayed(name="blink_roto")
                blink_roto([s,1,1])
            else:
                s.cancel_delayed("blink_roto")
        elif s.game.before_fifth.status == True:
            p = [528,520]
            screen.blit(roto_time, p)
            if s.game.ball_count.position == 4:
                s.cancel_delayed(name="blink_roto")
                blink_roto([s,1,1])
            else:
                s.cancel_delayed("blink_roto")

    pygame.display.update()

def blink_roto(args):
    dirty_rects = []
    s = args[0]
    b = args[1]
    sn = args[2]

    if b == 0:
        if sn == 1:
            p = [526,465]
            dirty_rects.append(screen.blit(roto_time, p))
        pygame.display.update(dirty_rects)
    else:
        dirty_rects.append(screen.blit(bg_gi, (526,465), pygame.Rect(526,465,170,59)))
        pygame.display.update(dirty_rects)
    b = not b

    args = [s,b,sn]

    s.delay(name="blink_roto", delay=0.1, handler=blink_roto, param=args)

def blink(args):
    dirty_rects = []
    s = args[0]
    b = args[1]
    sn = args[2]

    if b == 0:
        if sn == 1:
            p = [188,676]
            dirty_rects.append(screen.blit(select_now, p))
        pygame.display.update(dirty_rects)
    else:
        dirty_rects.append(screen.blit(bg_gi, (188,676), pygame.Rect(188,676,128,43)))
        pygame.display.update(dirty_rects)
    b = not b

    args = [s,b,sn]

    s.delay(name="blink", delay=0.1, handler=blink, param=args)

def roto_animation(args):
    dirty_rects = []
    s = args[0]
    num = args[1]
    square = args[2]
    
    if square == 1:
        p = [278,448]
        if s.game.roto.position == 0:
            image = roto7
            topleft = r2
            topmiddle = r3
            topright = r4
            middleright = r5
            bottomright = r6
            bottommiddle = r7
            bottomleft = r8
            middleleft = r1
        elif s.game.roto.position == 1:
            image = roto0
            topleft = r1
            topmiddle = r2
            topright = r3
            middleright = r4
            bottomright = r5
            bottommiddle = r6
            bottomleft = r7
            middleleft = r8
        elif s.game.roto.position == 2:
            image = roto1
            topleft = r8
            topmiddle = r1
            topright = r2
            middleright = r3
            bottomright = r4
            bottommiddle = r5
            bottomleft = r6
            middleleft = r7
        elif s.game.roto.position == 3:
            image = roto2
            topleft = r7
            topmiddle = r8
            topright = r1
            middleright = r2
            bottomright = r3
            bottommiddle = r4
            bottomleft = r5
            middleleft = r6
        elif s.game.roto.position == 4:
            image = roto3
            topleft = r6
            topmiddle = r7
            topright = r8
            middleright = r1
            bottomright = r2
            bottommiddle = r3
            bottomleft = r4
            middleleft = r5
        elif s.game.roto.position == 5:
            image = roto4
            topleft = r5
            topmiddle = r6
            topright = r7
            middleright = r8
            bottomright = r1
            bottommiddle = r2
            bottomleft = r3
            middleleft = r4
        elif s.game.roto.position == 6:
            image = roto5
            topleft = r4
            topmiddle = r5
            topright = r6
            middleright = r7
            bottomright = r8
            bottommiddle = r1
            bottomleft = r2
            middleleft = r3
        elif s.game.roto.position == 7:
            image = roto6
            topleft = r3
            topmiddle = r4
            topright = r5
            middleright = r6
            bottomright = r7
            bottommiddle = r8
            bottomleft = r1
            middleleft = r2


    rect = pygame.Rect(p[0],p[1],200,200)

    #letter A
    if square == 1: 
        dirty_rects.append(screen.blit(topleft, (299  - num - 20, 460)))
        dirty_rects.append(screen.blit(topmiddle, (346  - num - 20, 460)))
        dirty_rects.append(screen.blit(topright, (396, 467 - num - 15)))
        dirty_rects.append(screen.blit(middleright, (396, 515 - num - 15)))
        dirty_rects.append(screen.blit(bottomright, (393  + num + 15, 562)))
        dirty_rects.append(screen.blit(bottommiddle, (343  + num + 15, 562)))
        dirty_rects.append(screen.blit(bottomleft, (288, 564 + num + 5)))
        dirty_rects.append(screen.blit(middleleft, (288, 514 + num + 5)))

    if (s.game.anti_cheat.status == True):
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],170,163)))
    else:
        dirty_rects.append(screen.blit(bg_off, p, pygame.Rect(p[0],p[1],170,163)))
   
    if 16 in s.holes:
        p = [337,506]
        dirty_rects.append(screen.blit(bg_gi, (337,506), pygame.Rect(337,506,50,51)))
        dirty_rects.append(screen.blit(number, p))


    pygame.display.update(dirty_rects)


def eb_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]

    if s.game.extra_ball.position < 5:
        dirty_rects.append(screen.blit(bg_gi, (100,1017), pygame.Rect(100,1017,172,37)))
    if s.game.extra_ball.position < 10:
        dirty_rects.append(screen.blit(bg_gi, (278,1017), pygame.Rect(278,1017,172,37)))
    if s.game.extra_ball.position < 15:
        dirty_rects.append(screen.blit(bg_gi, (456,1017), pygame.Rect(456,1017,172,37)))
    pygame.display.update(dirty_rects)

    if num in [0,1,6,7,12,13,18,19,26,27,32,33,38,39,44,45]:
        if s.game.extra_ball.position < 5:
            p = [100,1017]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [2,3,8,9,14,15,20,21,28,29,34,35,40,41,46,47]:
        if s.game.extra_ball.position < 10:
            p = [278,1017]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [4,5,10,11,16,17,22,23,24,30,31,36,37,42,43,48,49,50]:
        if s.game.extra_ball.position < 15:
            p = [456,1017]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return

def clear_odds(s, num):
    global screen

    dirty_rects = []

    if s.game.odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (187,775), pygame.Rect(187,775,30,88)))
    if s.game.odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (225,776), pygame.Rect(225,776,30,88)))
    if s.game.odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (269,802), pygame.Rect(269,802,44,95)))
    if s.game.odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (437,838), pygame.Rect(437,838,70,91)))
    if s.game.odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (514,764), pygame.Rect(514,764,49,93)))
    if s.game.odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (627,769), pygame.Rect(627,769,49,91)))
    if s.game.odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (219,886), pygame.Rect(219,886,37,85)))
    if s.game.odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (648,893), pygame.Rect(648,893,37,85)))

    pygame.display.update(dirty_rects)

def draw_odds_animation(s, num):
    global screen
    dirty_rects = []

    if num in [0,1,40,14,24,25]:
        if s.game.odds.position != 1:
            p = [187,775]
            dirty_rects.append(screen.blit(o1, p))
            pygame.display.update(dirty_rects)
            return
    if num in [2,3,41,15,26,27]:
        if s.game.odds.position != 2:
            p = [225,776]
            dirty_rects.append(screen.blit(o2, p))
            pygame.display.update(dirty_rects)
            return
    if num in [4,5,42,16,28,29]:
        if s.game.odds.position != 3:
            p = [269,802]
            dirty_rects.append(screen.blit(o3, p))
            pygame.display.update(dirty_rects)
            return
    if num in [6,7,43,17,30,31]:
        if s.game.odds.position != 4:
            p = [437,838]
            dirty_rects.append(screen.blit(o4, p))
            pygame.display.update(dirty_rects)
            return
    if num in [8,9,44,18,32,33]:
        if s.game.odds.position != 5:
            p = [514,764]
            dirty_rects.append(screen.blit(o5, p))
            pygame.display.update(dirty_rects)
            return
    if num in [10,11,45,19,34,35]:
        if s.game.odds.position != 6:
            p = [627,769]
            dirty_rects.append(screen.blit(o6, p))
            pygame.display.update(dirty_rects)
            return
    if num in [12,13,46,47,20,21,36,37]:
        if s.game.odds.position != 7:
            p = [219,886]
            dirty_rects.append(screen.blit(o7, p))
            pygame.display.update(dirty_rects)
            return
    if num in [14,48,49,22,23,38]:
        if s.game.odds.position != 8:
            p = [648,893]
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

def clear_features(s, num):
    global screen

    dirty_rects = []
    if s.game.lite_a_name.status == False:
        dirty_rects.append(screen.blit(bg_gi, (560,239), pygame.Rect(560,239,148,76)))
    if s.game.corners.status == False:
        dirty_rects.append(screen.blit(bg_gi, (525,607), pygame.Rect(525,607,180,59)))
    if s.game.red_star.status == False:
        dirty_rects.append(screen.blit(bg_gi, (642,982), pygame.Rect(642,982,62,63)))
    if s.game.diagonal_separate.position < 5:
        dirty_rects.append(screen.blit(bg_gi, (22,441), pygame.Rect(22,441,180,59)))
    if s.game.super_diagonal.status == False:
        dirty_rects.append(screen.blit(bg_gi, (23,388), pygame.Rect(23,388,180,59)))
    if s.game.selection_feature.position < 5:
        dirty_rects.append(screen.blit(bg_gi, (360,716), pygame.Rect(360,716,41,42)))
    if s.game.selection_feature.position < 6:
        dirty_rects.append(screen.blit(bg_gi, (404,716), pygame.Rect(404,716,41,42)))
    if s.game.selection_feature.position < 7:
        dirty_rects.append(screen.blit(bg_gi, (447,716), pygame.Rect(447,716,41,42)))
    if s.game.selection_feature.position < 8:
        dirty_rects.append(screen.blit(bg_gi, (489,716), pygame.Rect(489,716,41,42)))
    if s.game.selection_feature.position !=  1:
        dirty_rects.append(screen.blit(bg_gi, (197,718), pygame.Rect(197,718,34,34)))
    if s.game.selection_feature.position !=  2:
        dirty_rects.append(screen.blit(bg_gi, (239,718), pygame.Rect(239,718,34,34)))
    if s.game.selection_feature.position !=  3:
        dirty_rects.append(screen.blit(bg_gi, (280,718), pygame.Rect(280,718,34,34)))
    pygame.display.update(dirty_rects)


def draw_feature_animation(s, num):
    global screen
    dirty_rects = []
    
    if num in [11,12,36,37]:
        if s.game.red_star.status == False:
            p = [642,982]
            dirty_rects.append(screen.blit(star, p))
            s.game.coils.redROLamp.pulse(85)
            s.game.coils.yellowROLamp.pulse(85)
            pygame.display.update(dirty_rects)
            return
    if num in [9,10,34,35]:
        if s.game.diagonal_separate.position < 5:
            p = [22,441]
            dirty_rects.append(screen.blit(corners, p))
            pygame.display.update(dirty_rects)
            return
    if num in [7,8,32,33]:
        if s.game.lite_a_name.status == False:
            p = [560,239]
            dirty_rects.append(screen.blit(lite_a_name, p))
            pygame.display.update(dirty_rects)
            return
    if num in [5,6,30,31]:
        if s.game.super_diagonal.status == False:
            p = [23,388]
            dirty_rects.append(screen.blit(corners, p))
            pygame.display.update(dirty_rects)
            return
    if num in [3,4,28,29]:
        if s.game.selection_feature.position < 6:
            p = [404,716]
            dirty_rects.append(screen.blit(s_number, p))
            pygame.display.update(dirty_rects)
            return
    if num in [1,2,26,27]:
        if s.game.selection_feature.position < 7:
            p = [447,716]
            dirty_rects.append(screen.blit(s_number, p))
            pygame.display.update(dirty_rects)
            return
    if num in [0,49,24,25]:
        if s.game.selection_feature.position < 8:
            p = [489,716]
            dirty_rects.append(screen.blit(s_number, p))
            pygame.display.update(dirty_rects)
            return
    if num in [47,48,22,23]:
        if s.game.selection_feature.position < 5:
            p = [360,716]
            dirty_rects.append(screen.blit(s_number, p))
            pygame.display.update(dirty_rects)
            return
    if num in [45,46,20,21]:
        if s.game.selection_feature.position != 3:
            p = [280,718]
            dirty_rects.append(screen.blit(s_arrow, p))
            pygame.display.update(dirty_rects)
            return
    if num in [43,44,18,19]:
        if s.game.selection_feature.position != 2:
            p = [239,718]
            dirty_rects.append(screen.blit(s_arrow, p))
            pygame.display.update(dirty_rects)
            return
    if num in [41,42,16,17]:
        if s.game.selection_feature.position != 1:
            p = [197,718]
            dirty_rects.append(screen.blit(s_arrow, p))
            pygame.display.update(dirty_rects)
            return
    if num in [39,40,14,15]:
        if s.game.corners.status == False:
            p = [525,607]
            dirty_rects.append(screen.blit(corners, p))
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

