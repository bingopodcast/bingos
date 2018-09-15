
import pygame
import random

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

meter = pygame.image.load('graphics/assets/silver_register_cover.png').convert()
eb = pygame.image.load('starlet/assets/eb.png').convert_alpha()
eb_arrow = pygame.image.load('starlet/assets/eb_arrow.png').convert_alpha()
extra_balls = pygame.image.load('starlet/assets/extra_balls.png').convert_alpha()
o1 = pygame.image.load('starlet/assets/odds1.png').convert_alpha()
o2 = pygame.image.load('starlet/assets/odds2.png').convert_alpha()
o3 = pygame.image.load('starlet/assets/odds3.png').convert_alpha()
o4 = pygame.image.load('starlet/assets/odds4.png').convert_alpha()
o5 = pygame.image.load('starlet/assets/odds5.png').convert_alpha()
o6 = pygame.image.load('starlet/assets/odds6.png').convert_alpha()
o7 = pygame.image.load('starlet/assets/odds7.png').convert_alpha()
o8 = pygame.image.load('starlet/assets/odds8.png').convert_alpha()
star = pygame.image.load('starlet/assets/rollover.png').convert_alpha()
number = pygame.image.load('starlet/assets/number.png').convert_alpha()
tilt = pygame.image.load('starlet/assets/tilt.png').convert_alpha()
scoring = pygame.image.load('starlet/assets/feature.png').convert_alpha()
select_now = pygame.image.load('starlet/assets/select_now.png').convert_alpha()
spotted_arrow = pygame.image.load('starlet/assets/selected_arrow.png').convert_alpha()
before_fourth = pygame.image.load('starlet/assets/s_time.png').convert_alpha()
roto_before_fourth = pygame.image.load('starlet/assets/roto_time.png').convert_alpha()
roto = pygame.image.load('starlet/assets/roto.png').convert_alpha()
roto_time = pygame.image.load('starlet/assets/roto_time.png').convert_alpha()
roto0 = pygame.image.load('starlet/assets/roto0.png').convert_alpha()
roto1 = pygame.image.load('starlet/assets/roto1.png').convert_alpha()
roto2 = pygame.image.load('starlet/assets/roto2.png').convert_alpha()
roto3 = pygame.image.load('starlet/assets/roto3.png').convert_alpha()
roto4 = pygame.image.load('starlet/assets/roto4.png').convert_alpha()
roto5 = pygame.image.load('starlet/assets/roto5.png').convert_alpha()
roto6 = pygame.image.load('starlet/assets/roto6.png').convert_alpha()
roto7 = pygame.image.load('starlet/assets/roto7.png').convert_alpha()
s_number = pygame.image.load('starlet/assets/s_number.png').convert_alpha()
corners = pygame.image.load('starlet/assets/feature.png').convert_alpha()
horizontal_score = pygame.image.load('starlet/assets/feature.png').convert_alpha()
letter1 = pygame.image.load('starlet/assets/letter1.png').convert_alpha()
letter2 = pygame.image.load('starlet/assets/letter2.png').convert_alpha()
letter3 = pygame.image.load('starlet/assets/letter3.png').convert_alpha()
letter4 = pygame.image.load('starlet/assets/letter4.png').convert_alpha()
letter5 = pygame.image.load('starlet/assets/letter5.png').convert_alpha()
letter6 = pygame.image.load('starlet/assets/letter6.png').convert_alpha()
lite_a_name = pygame.image.load('starlet/assets/lite_a_name.png').convert_alpha()
special_arrow = pygame.image.load('starlet/assets/sp_arrow.png').convert_alpha()
s_arrow = pygame.image.load('starlet/assets/s_arrow.png').convert_alpha()
score_arrow = pygame.image.load('starlet/assets/score_arrow.png').convert_alpha()
feature = pygame.image.load('starlet/assets/feature.png').convert_alpha()
special_pocket = pygame.image.load('starlet/assets/special_pocket.png').convert_alpha()
eight_balls = pygame.image.load('starlet/assets/eight_balls.png').convert_alpha()
bg_menu = pygame.image.load('starlet/assets/starlet_menu.png')
bg_gi = pygame.image.load('starlet/assets/starlet_gi.png')
bg_off = pygame.image.load('starlet/assets/starlet_off.png')
r1 = pygame.image.load('starlet/assets/r1.png').convert_alpha()
r2 = pygame.image.load('starlet/assets/r2.png').convert_alpha()
r3 = pygame.image.load('starlet/assets/r3.png').convert_alpha()
r4 = pygame.image.load('starlet/assets/r4.png').convert_alpha()
r5 = pygame.image.load('starlet/assets/r5.png').convert_alpha()
r6 = pygame.image.load('starlet/assets/r6.png').convert_alpha()
r7 = pygame.image.load('starlet/assets/r7.png').convert_alpha()
r8 = pygame.image.load('starlet/assets/r8.png').convert_alpha()

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
        p = [274,468]
        screen.blit(roto0, p)
    elif s.game.roto.position == 1:
        p = [274,468]
        screen.blit(roto1, p)
    elif s.game.roto.position == 2:
        p = [274,468]
        screen.blit(roto2, p)
    elif s.game.roto.position == 3:
        p = [274,468]
        screen.blit(roto3, p)
    elif s.game.roto.position == 4:
        p = [274,468]
        screen.blit(roto4, p)
    elif s.game.roto.position == 5:
        p = [274,468]
        screen.blit(roto5, p)
    elif s.game.roto.position == 6:
        p = [274,468]
        screen.blit(roto6, p)
    elif s.game.roto.position == 7:
        p = [274,468]
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
        p = [226,250]
        screen.blit(letter1, p)
        p = [271,252]
        screen.blit(letter2, p)
        p = [320,250]
        screen.blit(letter3, p)
        p = [380,252]
        screen.blit(letter4, p)
        p = [418,248]
        screen.blit(letter5, p)
        p = [482,250]
        screen.blit(letter6, p)
    else:
        if s.game.lite_a_name.status == True:
            p = [550,256]
            screen.blit(lite_a_name, p)

        if s.game.name.position >= 1:
            p = [226,250]
            screen.blit(letter1, p)
        if s.game.name.position >= 2:
            p = [271,252]
            screen.blit(letter2, p)
        if s.game.name.position >= 3:
            p = [320,250]
            screen.blit(letter3, p)
        if s.game.name.position >= 4:
            p = [380,252]
            screen.blit(letter4, p)
        if s.game.name.position >= 5:
            p = [418,248]
            screen.blit(letter5, p)
        if s.game.name.position >= 6:
            p = [482,250]
            screen.blit(letter6, p)

    if s.game.extra_ball.position == 1:
        eb_position = [102,982]
        screen.blit(eb_arrow, eb_position)
    if s.game.extra_ball.position == 2:
        eb_position = [138,982]
        screen.blit(eb_arrow, eb_position)
    if s.game.extra_ball.position == 3:
        eb_position = [173,982]
        screen.blit(eb_arrow, eb_position)
    if s.game.extra_ball.position == 4:
        eb_position = [209,982]
        screen.blit(eb_arrow, eb_position)
    if s.game.extra_ball.position == 5:
        eb_position = [243,980]
        screen.blit(eb_arrow, eb_position)
    if s.game.extra_ball.position == 6:
        eb_position = [284,980]
        screen.blit(eb_arrow, eb_position)
    if s.game.extra_ball.position == 7:
        eb_position = [318,980]
        screen.blit(eb_arrow, eb_position)
    if s.game.extra_ball.position == 8:
        eb_position = [351,980]
        screen.blit(eb_arrow, eb_position)
    if s.game.extra_ball.position == 9:
        eb_position = [387,980]
        screen.blit(eb_arrow, eb_position)
    if s.game.extra_ball.position == 10:
        eb_position = [422,980]
        screen.blit(eb_arrow, eb_position)
    if s.game.extra_ball.position == 11:
        eb_position = [462,980]
        screen.blit(eb_arrow, eb_position)
    if s.game.extra_ball.position == 12:
        eb_position = [495,980]
        screen.blit(eb_arrow, eb_position)
    if s.game.extra_ball.position == 13:
        eb_position = [530,980]
        screen.blit(eb_arrow, eb_position)
    if s.game.extra_ball.position == 14:
        eb_position = [566,980]
        screen.blit(eb_arrow, eb_position)
    if s.game.extra_ball.position == 15:
        eb_position = [600,980]
        screen.blit(eb_arrow, eb_position)

    if s.game.extra_ball.position >= 5 and s.game.extra_ball.position < 10:
        eb_pos = [100,1007]
        screen.blit(eb, eb_pos)
    if s.game.extra_ball.position >= 10 and s.game.extra_ball.position < 15:
        eb_pos = [278,1007]
        screen.blit(eb, eb_pos)
    if s.game.extra_ball.position == 15:
        eb_pos = [456,1007]
        screen.blit(eb, eb_pos)

    if s.game.odds.position > 0:
        if s.game.odds.position == 1:
            odds_position = [174,766]
            screen.blit(o1, odds_position)
        if s.game.odds.position == 2:
            odds_position = [223,768]
            screen.blit(o2, odds_position)
        if s.game.odds.position == 3:
            odds_position = [267,774]
            screen.blit(o3, odds_position)
        if s.game.odds.position == 4:
            odds_position = [444,775]
            screen.blit(o4, odds_position)
        if s.game.odds.position == 5:
            odds_position = [494,772]
            screen.blit(o5, odds_position)
        if s.game.odds.position == 6:
            odds_position = [577,776]
            screen.blit(o6, odds_position)
        if s.game.odds.position == 7:
            odds_position = [222,875]
            screen.blit(o7, odds_position)
        if s.game.odds.position == 8:
            odds_position = [476,864]
            screen.blit(o8, odds_position)

    if s.game.red_star.status == True:
        rs_position = [647,978]
        screen.blit(star, rs_position)

    if s.game.corners.status == True:
        corners_position = [546,412]
        screen.blit(corners, corners_position)

    if s.game.super_horizontal.status == True:
        corners_position = [2,654]
        screen.blit(before_fourth, corners_position)

    if s.game.horizontal.position == 1:
        p = [79,615]
        screen.blit(score_arrow, p)
    elif s.game.horizontal.position == 2:
        p = [79,565]
        screen.blit(score_arrow, p)
    elif s.game.horizontal.position == 3:
        p = [78,513]
        screen.blit(score_arrow, p)
    elif s.game.horizontal.position == 4:
        p = [75,462]
        screen.blit(score_arrow, p)
    elif s.game.horizontal.position == 5:
        p = [2,410]
        screen.blit(corners, p)

    if s.game.special_pocket.status == True:
        p = [69,342]
        screen.blit(special_pocket, p)
    if s.game.pocket.position == 1:
        p = [267,346]
        screen.blit(special_arrow, p)
    if s.game.pocket.position == 2:
        p = [308,346]
        screen.blit(special_arrow, p)
    if s.game.pocket.position == 3:
        p = [350,346]
        screen.blit(special_arrow, p)
    if s.game.pocket.position == 4:
        p = [392,346]
        screen.blit(special_arrow, p)
    if s.game.pocket.position == 5:
        p = [430,346]
        screen.blit(special_arrow, p)
    if s.game.pocket.position == 6:
        p = [468,344]
        screen.blit(eight_balls, p)

    r1 = [284,478]
    r2 = [338,479]
    r3 = [393,479]
    r4 = [284,533]
    r5 = [394,531]
    r6 = [286,582]
    r7 = [340,584]
    r8 = [395,582]

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
                p = [230,581]
                screen.blit(number, p)
            if 2 in s.holes:
                p = [227,528]
                screen.blit(number, p)
            if 3 in s.holes:
                p = [449,634]
                screen.blit(number, p)
            if 4 in s.holes:
                p = [281,421]
                screen.blit(number, p)
            if 5 in s.holes:
                p = [339,633]
                screen.blit(number, p)
            if 6 in s.holes:
                p = [448,423]
                screen.blit(number, p)
            if 7 in s.holes:
                p = [285,633]
                screen.blit(number, p)
            if 8 in s.holes:
                p = [449,476]
                screen.blit(number, p)
            if 9 in s.holes:
                p = [225,421]
                screen.blit(number, p)
            if 10 in s.holes:
                p = [226,475]
                screen.blit(number, p)
            if 11 in s.holes:
                p = [231,633]
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
                p = [338,424]
                screen.blit(number, p)
            if 16 in s.holes:
                p = [338,530]
                screen.blit(number, p)
            if 17 in s.holes:
                p = [449,584]
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
                p = [394,635]
                screen.blit(number, p)
            if 24 in s.holes:
                p = [393,423]
                screen.blit(number, p)
            if 25 in s.holes:
                p = [448,531]
                screen.blit(number, p)


    if s.game.tilt.status == True:
        tilt_position = [80,775]
        screen.blit(tilt, tilt_position)

    if s.game.selection_feature.position == 1:
        p = [162,732]
        screen.blit(s_arrow, p)
    if s.game.selection_feature.position == 2:
        p = [202,732]
        screen.blit(s_arrow, p)
    if s.game.selection_feature.position == 3:
        p = [244,732]
        screen.blit(s_arrow, p)
    if s.game.selection_feature.position >= 4:
        p = [282,727]
        screen.blit(s_number, p)
    if s.game.selection_feature.position >= 5:
        p = [324,727]
        screen.blit(s_number, p)
    if s.game.selection_feature.position >= 6:
        p = [362,727]
        screen.blit(s_number, p)
    if s.game.selection_feature.position >= 7:
        p = [412,727]
        screen.blit(s_number, p)
    if s.game.selection_feature.position >= 8:
        p = [447,727]
        screen.blit(s_number, p)
    if s.game.selection_feature.position >= 9:
        p = [489,727]
        screen.blit(s_number, p)
    if s.game.selection_feature.position >= 10:
        p = [531,727]
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
        p = [5,712]
        screen.blit(before_fourth, p)
    if s.game.before_fifth.status == True and (s.game.selection_feature.position > 3):
        p = [572,712]
        screen.blit(before_fourth, p)

    if s.game.before_fourth.status == True:
        if s.game.ball_count.position < 4:
            if s.game.select_spots.status == True:
                if s.game.selection_feature.position >= 4:
                    if s.game.spotted.position == 0:
                        p = [281,698]
                        screen.blit(spotted_arrow, p)
                        #19
                        p = r19
                        screen.blit(number, p)
                if s.game.selection_feature.position >= 5:
                    if s.game.spotted.position == 1:
                        p = [325,698]
                        screen.blit(spotted_arrow, p)
                        #20
                        p = r20
                        screen.blit(number, p)
                if s.game.selection_feature.position >= 6:
                    if s.game.spotted.position == 2:
                        p = [367,698]
                        screen.blit(spotted_arrow, p)
                        #21
                        p = r21
                        screen.blit(number, p)
                if s.game.selection_feature.position >= 7:
                    if s.game.spotted.position == 3:
                        p = [410,698]
                        screen.blit(spotted_arrow, p)
                        #22
                        p = r22
                        screen.blit(number, p)
                if s.game.selection_feature.position >= 8:
                    if s.game.spotted.position == 4:
                        p = [451,698]
                        screen.blit(spotted_arrow, p)
                        #25
                        p = [448,531]
                        screen.blit(number, p)
                if s.game.selection_feature.position >= 9:
                    if s.game.spotted.position == 5:
                        p = [495,698]
                        screen.blit(spotted_arrow, p)
                        #10
                        p = [226,475]
                        screen.blit(number, p)
                if s.game.selection_feature.position >= 10:
                    if s.game.spotted.position == 6:
                        p = [539,698]
                        screen.blit(spotted_arrow, p)
                        #16
                        p = [338,530]
                        screen.blit(number, p)
                

    if s.game.before_fifth.status == True:
        if s.game.ball_count.position < 5:
            if s.game.select_spots.status == True:
                if s.game.selection_feature.position >= 4:
                    if s.game.spotted.position == 0:
                        p = [281,698]
                        screen.blit(spotted_arrow, p)
                        #19
                        p = r19
                        screen.blit(number, p)
                if s.game.selection_feature.position >= 5:
                    if s.game.spotted.position == 1:
                        p = [325,698]
                        screen.blit(spotted_arrow, p)
                        #20
                        p = r20
                        screen.blit(number, p)
                if s.game.selection_feature.position >= 6:
                    if s.game.spotted.position == 2:
                        p = [367,698]
                        screen.blit(spotted_arrow, p)
                        #21
                        p = r21
                        screen.blit(number, p)
                if s.game.selection_feature.position >= 7:
                    if s.game.spotted.position == 3:
                        p = [410,698]
                        screen.blit(spotted_arrow, p)
                        #22
                        p = r22
                        screen.blit(number, p)
                if s.game.selection_feature.position >= 8:
                    if s.game.spotted.position == 4:
                        p = [451,698]
                        screen.blit(spotted_arrow, p)
                        #25
                        p = [448,531]
                        screen.blit(number, p)
                if s.game.selection_feature.position >= 9:
                    if s.game.spotted.position == 5:
                        p = [495,698]
                        screen.blit(spotted_arrow, p)
                        #10
                        p = [226,475]
                        screen.blit(number, p)
                if s.game.selection_feature.position >= 10:
                    if s.game.spotted.position == 6:
                        p = [539,698]
                        screen.blit(spotted_arrow, p)
                        #16
                        p = [338,530]
                        screen.blit(number, p)

    if s.game.eb_play.status == True:
        p = [22,982]
        screen.blit(extra_balls, p)

    if s.game.roto_feature.status == True:
        p = [554,503]
        screen.blit(roto, p)
        if s.game.before_fourth.status == True:
            p = [549,526]
            screen.blit(roto_time, p)
            if s.game.ball_count.position == 3:
                s.cancel_delayed(name="blink_roto")
                blink_roto([s,1,1])
            else:
                s.cancel_delayed("blink_roto")
        elif s.game.before_fifth.status == True:
            p = [548,627]
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
            p = [548,576]
            dirty_rects.append(screen.blit(roto_time, p))
        pygame.display.update(dirty_rects)
    else:
        dirty_rects.append(screen.blit(bg_gi, (548,576), pygame.Rect(548,576,165,51)))
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
            p = [153,692]
            dirty_rects.append(screen.blit(select_now, p))
        pygame.display.update(dirty_rects)
    else:
        dirty_rects.append(screen.blit(bg_gi, (153,692), pygame.Rect(153,692,124,35)))
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
        p = [274,468]
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
        dirty_rects.append(screen.blit(topleft, (295  - num - 20, 480)))
        dirty_rects.append(screen.blit(topmiddle, (342  - num - 20, 480)))
        dirty_rects.append(screen.blit(topright, (392, 487 - num - 15)))
        dirty_rects.append(screen.blit(middleright, (392, 535 - num - 15)))
        dirty_rects.append(screen.blit(bottomright, (389  + num + 15, 582)))
        dirty_rects.append(screen.blit(bottommiddle, (339  + num + 15, 582)))
        dirty_rects.append(screen.blit(bottomleft, (284, 584 + num + 5)))
        dirty_rects.append(screen.blit(middleleft, (284, 534 + num + 5)))

    if (s.game.anti_cheat.status == True):
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],170,163)))
    else:
        dirty_rects.append(screen.blit(bg_off, p, pygame.Rect(p[0],p[1],170,163)))
    
    if 16 in s.holes:
        p = [338,530]
        dirty_rects.append(screen.blit(bg_gi, (338,530), pygame.Rect(338,530,50,51)))
        dirty_rects.append(screen.blit(number, p))
    pygame.display.update(dirty_rects)


def eb_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]
    if s.game.extra_ball.position < 5:
        dirty_rects.append(screen.blit(bg_gi, (100,1007), pygame.Rect(100,1007,176,32)))
    if s.game.extra_ball.position < 10:
        dirty_rects.append(screen.blit(bg_gi, (278,1007), pygame.Rect(278,1007,176,32)))
    if s.game.extra_ball.position < 15:
        dirty_rects.append(screen.blit(bg_gi, (456,1007), pygame.Rect(456,1007,176,32)))
        dirty_rects.append(screen.blit(bg_gi, (600,980), pygame.Rect(600,980,30,25)))
    pygame.display.update(dirty_rects)
    if num in [0,1,6,7,12,13,18,19,26,27,32,33,38,39,44,45]:
        if s.game.extra_ball.position < 5:
            p = [100,1007]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [2,3,8,9,14,15,20,21,28,29,34,35,40,41,46,47]:
        if s.game.extra_ball.position < 10:
            p = [278,1007]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [4,5,10,11,16,17,22,23,24,30,31,36,37,42,43,48,49,50]:
        if s.game.extra_ball.position < 15:
            p = [456,1007]
            dirty_rects.append(screen.blit(eb, p))
            p = [600,980]
            dirty_rects.append(screen.blit(eb_arrow, p))
            pygame.display.update(dirty_rects)
            return

def clear_odds(s, num):
    global screen
    dirty_rects = []
    if s.game.odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (174,766), pygame.Rect(174,766,24,92)))
    if s.game.odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (223,768), pygame.Rect(223,768,33,92)))
    if s.game.odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (267,774), pygame.Rect(267,774,37,99)))
    if s.game.odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (444,775), pygame.Rect(444,775,37,96)))
    if s.game.odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (494,772), pygame.Rect(494,772,37,81)))
    if s.game.odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (577,776), pygame.Rect(577,776,34,85)))
    if s.game.odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (222,875), pygame.Rect(222,875,52,67)))
    if s.game.odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (476,864), pygame.Rect(476,864,53,84)))

    pygame.display.update(dirty_rects)

def draw_odds_animation(s, num):
    global screen
    dirty_rects = []
    if num in [0,1,40,14,24,25]:
        if s.game.odds.position != 1:
            p = [174,766]
            dirty_rects.append(screen.blit(o1, p))
            pygame.display.update(dirty_rects)
            return
    if num in [2,3,41,15,26,27]:
        if s.game.odds.position != 2:
            p = [223,768]
            dirty_rects.append(screen.blit(o2, p))
            pygame.display.update(dirty_rects)
            return
    if num in [4,5,42,16,28,29]:
        if s.game.odds.position != 3:
            p = [267,774]
            dirty_rects.append(screen.blit(o3, p))
            pygame.display.update(dirty_rects)
            return
    if num in [6,7,43,17,30,31]:
        if s.game.odds.position != 4:
            p = [444,775]
            dirty_rects.append(screen.blit(o4, p))
            pygame.display.update(dirty_rects)
            return
    if num in [8,9,44,18,32,33]:
        if s.game.odds.position != 5:
            p = [494,772]
            dirty_rects.append(screen.blit(o5, p))
            pygame.display.update(dirty_rects)
            return
    if num in [10,11,45,19,34,35]:
        if s.game.odds.position != 6:
            p = [577,776]
            dirty_rects.append(screen.blit(o6, p))
            pygame.display.update(dirty_rects)
            return
    if num in [12,13,46,47,20,21,36,37]:
        if s.game.odds.position != 7:
            p = [222,875]
            dirty_rects.append(screen.blit(o7, p))
            pygame.display.update(dirty_rects)
            return
    if num in [14,48,49,22,23,38]:
        if s.game.odds.position != 8:
            p = [476,864]
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
        dirty_rects.append(screen.blit(bg_gi, (550,256), pygame.Rect(550,256,170,68)))
    if s.game.corners.status == False:
        dirty_rects.append(screen.blit(bg_gi, (546,412), pygame.Rect(546,412,178,57)))
    if s.game.super_horizontal.status == False:
        dirty_rects.append(screen.blit(bg_gi, (2,654), pygame.Rect(2,654,147,53)))
    if s.game.red_star.status == False:
        dirty_rects.append(screen.blit(bg_gi, (647,978), pygame.Rect(647,978,60,56)))
    if s.game.selection_feature.position < 7:
        dirty_rects.append(screen.blit(bg_gi, (412,727), pygame.Rect(412,727,39,36)))
    if s.game.selection_feature.position < 8:
        dirty_rects.append(screen.blit(bg_gi, (447,727), pygame.Rect(447,727,39,36)))
    if s.game.selection_feature.position < 9:
        dirty_rects.append(screen.blit(bg_gi, (489,727), pygame.Rect(489,727,39,36)))
    if s.game.selection_feature.position < 10:
        dirty_rects.append(screen.blit(bg_gi, (531,727), pygame.Rect(531,727,39,36)))
    if s.game.selection_feature.position !=  1:
        dirty_rects.append(screen.blit(bg_gi, (162,732), pygame.Rect(162,732,33,26)))
    if s.game.selection_feature.position !=  2:
        dirty_rects.append(screen.blit(bg_gi, (202,732), pygame.Rect(202,732,33,26)))
    if s.game.selection_feature.position !=  3:
        dirty_rects.append(screen.blit(bg_gi, (244,732), pygame.Rect(244,732,33,26)))
    pygame.display.update(dirty_rects)


def draw_feature_animation(s, num):
    global screen
    dirty_rects = []

    if num in [11,12,36,37]:
        if s.game.red_star.status == False:
            p = [647,978]
            dirty_rects.append(screen.blit(star, p))
            s.game.coils.redROLamp.pulse(85)
            s.game.coils.yellowROLamp.pulse(85)
            pygame.display.update(dirty_rects)
            return
    if num in [9,10,34,35]:
        if s.game.super_horizontal.status == False:
            p = [2,654]
            dirty_rects.append(screen.blit(before_fourth, p))
            pygame.display.update(dirty_rects)
            return
    if num in [7,8,32,33]:
        if s.game.lite_a_name.status == False:
            p = [550,256]
            dirty_rects.append(screen.blit(lite_a_name, p))
            pygame.display.update(dirty_rects)
            return
    #if num in [5,6,30,31]:
    #    if s.game.corners3.status == False:
    #        p = [515,546]
    #        dirty_rects.append(screen.blit(four_five, p))
    #        pygame.display.update(dirty_rects)
    #        return
    if num in [3,4,28,29]:
        if s.game.selection_feature.position < 8:
            p = [447,727]
            dirty_rects.append(screen.blit(s_number, p))
            pygame.display.update(dirty_rects)
            return
    if num in [1,2,26,27]:
        if s.game.selection_feature.position < 9:
            p = [489,727]
            dirty_rects.append(screen.blit(s_number, p))
            pygame.display.update(dirty_rects)
            return
    if num in [0,49,24,25]:
        if s.game.selection_feature.position < 10:
            p = [531,727]
            dirty_rects.append(screen.blit(s_number, p))
            pygame.display.update(dirty_rects)
            return
    if num in [47,48,22,23]:
        if s.game.selection_feature.position < 7:
            p = [412,727]
            dirty_rects.append(screen.blit(s_number, p))
            pygame.display.update(dirty_rects)
            return
    if num in [45,46,20,21]:
        if s.game.selection_feature.position != 3:
            p = [244,732]
            dirty_rects.append(screen.blit(s_arrow, p))
            pygame.display.update(dirty_rects)
            return
    if num in [43,44,18,19]:
        if s.game.selection_feature.position != 2:
            p = [202,732]
            dirty_rects.append(screen.blit(s_arrow, p))
            pygame.display.update(dirty_rects)
            return
    if num in [41,42,16,17]:
        if s.game.selection_feature.position != 1:
            p = [162,732]
            dirty_rects.append(screen.blit(s_arrow, p))
            pygame.display.update(dirty_rects)
            return
    if num in [39,40,14,15]:
        if s.game.corners.status == False:
            p = [546,412]
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

