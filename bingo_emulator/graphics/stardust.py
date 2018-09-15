
import pygame
import random

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

meter = pygame.image.load('graphics/assets/silver_register_cover.png').convert()
eb = pygame.image.load('stardust/assets/eb.png').convert_alpha()
eb_arrow = pygame.image.load('stardust/assets/eb_arrow.png').convert_alpha()
extra_balls = pygame.image.load('stardust/assets/extra_balls.png').convert_alpha()
o1 = pygame.image.load('stardust/assets/odds1.png').convert_alpha()
o2 = pygame.image.load('stardust/assets/odds2.png').convert_alpha()
o3 = pygame.image.load('stardust/assets/odds3.png').convert_alpha()
o4 = pygame.image.load('stardust/assets/odds4.png').convert_alpha()
o5 = pygame.image.load('stardust/assets/odds5.png').convert_alpha()
o6 = pygame.image.load('stardust/assets/odds6.png').convert_alpha()
o7 = pygame.image.load('stardust/assets/odds7.png').convert_alpha()
o8 = pygame.image.load('stardust/assets/odds8.png').convert_alpha()
star = pygame.image.load('stardust/assets/rollovers.png').convert_alpha()
number = pygame.image.load('stardust/assets/number.png').convert_alpha()
card = pygame.image.load('stardust/assets/card.png').convert_alpha()
tilt = pygame.image.load('stardust/assets/tilt.png').convert_alpha()
select_now = pygame.image.load('stardust/assets/select_now.png').convert_alpha()
before_fourth = pygame.image.load('stardust/assets/before_fourth.png').convert_alpha()
before_fifth = pygame.image.load('stardust/assets/before_fifth.png').convert_alpha()
r_arrow = pygame.image.load('stardust/assets/r_arrow.png').convert_alpha()
spot_18 = pygame.image.load('stardust/assets/spot_18.png').convert_alpha()
roto0 = pygame.image.load('stardust/assets/roto0.png').convert_alpha()
roto1 = pygame.image.load('stardust/assets/roto1.png').convert_alpha()
roto2 = pygame.image.load('stardust/assets/roto2.png').convert_alpha()
roto3 = pygame.image.load('stardust/assets/roto3.png').convert_alpha()
roto4 = pygame.image.load('stardust/assets/roto4.png').convert_alpha()
roto5 = pygame.image.load('stardust/assets/roto5.png').convert_alpha()
roto6 = pygame.image.load('stardust/assets/roto6.png').convert_alpha()
roto7 = pygame.image.load('stardust/assets/roto7.png').convert_alpha()
roto20 = pygame.image.load('stardust/assets/roto20.png').convert_alpha()
roto21 = pygame.image.load('stardust/assets/roto21.png').convert_alpha()
roto22 = pygame.image.load('stardust/assets/roto22.png').convert_alpha()
roto23 = pygame.image.load('stardust/assets/roto23.png').convert_alpha()
roto24 = pygame.image.load('stardust/assets/roto24.png').convert_alpha()
roto25 = pygame.image.load('stardust/assets/roto25.png').convert_alpha()
roto26 = pygame.image.load('stardust/assets/roto26.png').convert_alpha()
roto27 = pygame.image.load('stardust/assets/roto27.png').convert_alpha()
special_arrow = pygame.image.load('stardust/assets/special_arrow.png').convert_alpha()
special_pocket = pygame.image.load('stardust/assets/special_pocket.png').convert_alpha()
eight_balls = pygame.image.load('stardust/assets/eight_balls.png').convert_alpha()
corners3 = pygame.image.load('stardust/assets/corners3.png').convert_alpha()
corners4 = pygame.image.load('stardust/assets/corners4.png').convert_alpha()
horizontal_scores = pygame.image.load('stardust/assets/horizontal_scores.png').convert_alpha()
h_arrow = pygame.image.load('stardust/assets/h_arrow.png').convert_alpha()
h_left = pygame.image.load('stardust/assets/h_left.png').convert_alpha()
h_right = pygame.image.load('stardust/assets/h_right.png').convert_alpha()
bg_menu = pygame.image.load('stardust/assets/stardust_menu.png')
bg_gi = pygame.image.load('stardust/assets/stardust_gi.png')
bg_off = pygame.image.load('stardust/assets/stardust_off.png')
r1 = pygame.image.load('stardust/assets/r1.png').convert_alpha()
r2 = pygame.image.load('stardust/assets/r2.png').convert_alpha()
r3 = pygame.image.load('stardust/assets/r3.png').convert_alpha()
r4 = pygame.image.load('stardust/assets/r4.png').convert_alpha()
r5 = pygame.image.load('stardust/assets/r5.png').convert_alpha()
r6 = pygame.image.load('stardust/assets/r6.png').convert_alpha()
r7 = pygame.image.load('stardust/assets/r7.png').convert_alpha()
r8 = pygame.image.load('stardust/assets/r8.png').convert_alpha()
r21 = pygame.image.load('stardust/assets/r21.png').convert_alpha()
r22 = pygame.image.load('stardust/assets/r22.png').convert_alpha()
r23 = pygame.image.load('stardust/assets/r23.png').convert_alpha()
r24 = pygame.image.load('stardust/assets/r24.png').convert_alpha()
r25 = pygame.image.load('stardust/assets/r25.png').convert_alpha()
r26 = pygame.image.load('stardust/assets/r26.png').convert_alpha()
r27 = pygame.image.load('stardust/assets/r27.png').convert_alpha()
r28 = pygame.image.load('stardust/assets/r28.png').convert_alpha()

class scorereel():
    """ Score Reels are used to count replays """
    def __init__(self, pos, image):
        self.position = pos
        self.default_y = self.position[1]
        self.image = pygame.image.load(image).convert()

reel1 = scorereel([112,837], "graphics/assets/white_reel.png")
reel10 = scorereel([93,837], "graphics/assets/white_reel.png")
reel100 = scorereel([74,837], "graphics/assets/white_reel.png")

def display(s, replays=0, menu=False):
    
    meter.set_colorkey((255,0,252))
    meter_position = [65,837]

    screen.blit(reel1.image, reel1.position)
    screen.blit(reel10.image, reel10.position)
    screen.blit(reel100.image, reel100.position)
    screen.blit(meter, meter_position)

    if s.game.roto.position == 0:
        p = [86,488]
        screen.blit(roto0, p)
    elif s.game.roto.position == 1:
        p = [86,488]
        screen.blit(roto1, p)
    elif s.game.roto.position == 2:
        p = [86,488]
        screen.blit(roto2, p)
    elif s.game.roto.position == 3:
        p = [86,488]
        screen.blit(roto3, p)
    elif s.game.roto.position == 4:
        p = [86,488]
        screen.blit(roto4, p)
    elif s.game.roto.position == 5:
        p = [86,488]
        screen.blit(roto5, p)
    elif s.game.roto.position == 6:
        p = [86,488]
        screen.blit(roto6, p)
    elif s.game.roto.position == 7:
        p = [86,488]
        screen.blit(roto7, p)

    if s.game.roto2.position == 0:
        p = [488,490]
        screen.blit(roto20, p)
    elif s.game.roto2.position == 1:
        p = [488,490]
        screen.blit(roto21, p)
    elif s.game.roto2.position == 2:
        p = [488,490]
        screen.blit(roto22, p)
    elif s.game.roto2.position == 3:
        p = [488,490]
        screen.blit(roto23, p)
    elif s.game.roto2.position == 4:
        p = [488,490]
        screen.blit(roto24, p)
    elif s.game.roto2.position == 5:
        p = [488,490]
        screen.blit(roto25, p)
    elif s.game.roto2.position == 6:
        p = [488,490]
        screen.blit(roto26, p)
    elif s.game.roto2.position == 7:
        p = [488,490]
        screen.blit(roto27, p)

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

    if s.game.selector.position >= 1:
        p = [132,367]
        screen.blit(card, p)
    if s.game.selector.position >= 2:
        p = [529,369]
        screen.blit(card, p)

    if s.game.extra_ball.position == 1:
        eb_position = [106,984]
        screen.blit(eb_arrow, eb_position)
    if s.game.extra_ball.position == 2:
        eb_position = [140,984]
        screen.blit(eb_arrow, eb_position)
    if s.game.extra_ball.position == 3:
        eb_position = [176,984]
        screen.blit(eb_arrow, eb_position)
    if s.game.extra_ball.position == 4:
        eb_position = [211,984]
        screen.blit(eb_arrow, eb_position)
    if s.game.extra_ball.position == 5:
        eb_position = [245,984]
        screen.blit(eb_arrow, eb_position)
    if s.game.extra_ball.position == 6:
        eb_position = [284,984]
        screen.blit(eb_arrow, eb_position)
    if s.game.extra_ball.position == 7:
        eb_position = [318,984]
        screen.blit(eb_arrow, eb_position)
    if s.game.extra_ball.position == 8:
        eb_position = [354,984]
        screen.blit(eb_arrow, eb_position)
    if s.game.extra_ball.position == 9:
        eb_position = [388,984]
        screen.blit(eb_arrow, eb_position)
    if s.game.extra_ball.position == 10:
        eb_position = [424,984]
        screen.blit(eb_arrow, eb_position)
    if s.game.extra_ball.position == 11:
        eb_position = [464,984]
        screen.blit(eb_arrow, eb_position)
    if s.game.extra_ball.position == 12:
        eb_position = [497,984]
        screen.blit(eb_arrow, eb_position)
    if s.game.extra_ball.position == 13:
        eb_position = [532,983]
        screen.blit(eb_arrow, eb_position)
    if s.game.extra_ball.position == 14:
        eb_position = [568,982]
        screen.blit(eb_arrow, eb_position)
    if s.game.extra_ball.position == 15:
        eb_position = [602,980]
        screen.blit(eb_arrow, eb_position)

    if s.game.extra_ball.position >= 5 and s.game.extra_ball.position < 10:
        eb_pos = [100,1015]
        screen.blit(eb, eb_pos)
    if s.game.extra_ball.position >= 10 and s.game.extra_ball.position < 15:
        eb_pos = [278,1017]
        screen.blit(eb, eb_pos)
    if s.game.extra_ball.position == 15:
        eb_pos = [456,1013]
        screen.blit(eb, eb_pos)

    if s.game.odds.position > 0:
        if s.game.odds.position == 1:
            odds_position = [240,889]
            screen.blit(o1, odds_position)
        if s.game.odds.position == 2:
            odds_position = [203,766]
            screen.blit(o2, odds_position)
        if s.game.odds.position == 3:
            odds_position = [280,776]
            screen.blit(o3, odds_position)
        if s.game.odds.position == 4:
            odds_position = [437,762]
            screen.blit(o4, odds_position)
        if s.game.odds.position == 5:
            odds_position = [558,764]
            screen.blit(o5, odds_position)
        if s.game.odds.position == 6:
            odds_position = [614,798]
            screen.blit(o6, odds_position)
        if s.game.odds.position == 7:
            odds_position = [656,765]
            screen.blit(o7, odds_position)
        if s.game.odds.position == 8:
            odds_position = [619,911]
            screen.blit(o8, odds_position)

    if s.game.red_star.status == True:
        rs_position = [642,978]
        screen.blit(star, rs_position)

    if s.game.cornersone_three.status == True:
        corners_position = [30,388]
        screen.blit(corners3, corners_position)

    if s.game.cornersone_four.status == True:
        corners_position = [202,389]
        screen.blit(corners4, corners_position)

    if s.game.cornerstwo_three.status == True:
        corners_position = [430,390]
        screen.blit(corners3, corners_position)

    if s.game.cornerstwo_four.status == True:
        corners_position = [596,392]
        screen.blit(corners4, corners_position)

    if s.game.horizontal.position >= 1:
        p = [312,354]
        screen.blit(horizontal_scores, p)
    if s.game.horizontal.position >= 2:
        p = [316,448]
        screen.blit(h_left, p)
        p = [374,448]
        screen.blit(h_right, p)
    if s.game.horizontal.position == 3:
        p = [360,476]
        screen.blit(h_arrow, p)
    if s.game.horizontal.position >= 4:
        p = [318,504]
        screen.blit(h_left, p)
        p = [375,503]
        screen.blit(h_right, p)
    if s.game.horizontal.position == 5:
        p = [360,530]
        screen.blit(h_arrow, p)
    if s.game.horizontal.position >= 6:
        p = [318,557]
        screen.blit(h_left, p)
        p = [374,556]
        screen.blit(h_right, p)
    if s.game.horizontal.position == 7:
        p = [360,584]
        screen.blit(h_arrow, p)
    if s.game.horizontal.position >= 8:
        p = [318,611]
        screen.blit(h_left, p)
        p = [374,611]
        screen.blit(h_right, p)
    if s.game.horizontal.position == 9:
        p = [360,640]
        screen.blit(h_arrow, p)
    if s.game.horizontal.position == 10:
        p = [318,667]
        screen.blit(h_left, p)
        p = [374,665]
        screen.blit(h_right, p)

    if s.game.special_pocket.status == True:
        p = [76,309]
        screen.blit(special_pocket, p)
    if s.game.pocket.position == 1:
        p = [269,314]
        screen.blit(special_arrow, p)
    if s.game.pocket.position == 2:
        p = [310,314]
        screen.blit(special_arrow, p)
    if s.game.pocket.position == 3:
        p = [354,314]
        screen.blit(special_arrow, p)
    if s.game.pocket.position == 4:
        p = [394,314]
        screen.blit(special_arrow, p)
    if s.game.pocket.position == 5:
        p = [437,314]
        screen.blit(special_arrow, p)
    if s.game.pocket.position == 6:
        p = [474,307]
        screen.blit(eight_balls, p)

    r1 = [90,494]
    r2 = [144,494]
    r3 = [199,494]
    r4 = [90,548]
    r5 = [200,548]
    r6 = [92,603]
    r7 = [146,603]
    r8 = [200,603]

    s0 = [494,496]
    s1 = [546,496]
    s2 = [599,496]
    s3 = [493,550]
    s4 = [599,550]
    s5 = [494,603]
    s6 = [546,603]
    s7 = [600,603]

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

    if s.game.roto2.position == 0:
        q5 = s0
        q17 = s1
        q11 = s2
        q19 = s3
        q23 = s4
        q10 = s5
        q16 = s6
        q18 = s7
    elif s.game.roto2.position == 1:
        q19 = s0
        q5 = s1
        q17 = s2
        q10 = s3
        q11 = s4
        q16 = s5
        q18 = s6
        q23 = s7
    elif s.game.roto2.position == 2:
        q10 = s0
        q19 = s1
        q5 = s2
        q16 = s3
        q17 = s4
        q18 = s5
        q23 = s6
        q11 = s7
    elif s.game.roto2.position == 3:
        q16 = s0
        q10 = s1
        q19 = s2
        q18 = s3
        q5 = s4
        q23 = s5
        q11 = s6
        q17 = s7
    elif s.game.roto2.position == 4:
        q18 = s0
        q16 = s1
        q10 = s2
        q23 = s3
        q19 = s4
        q11 = s5
        q17 = s6
        q5 = s7
    elif s.game.roto2.position == 5:
        q23 = s0
        q18 = s1
        q16 = s2
        q11 = s3
        q10 = s4
        q17 = s5
        q5 = s6
        q19 = s7
    elif s.game.roto2.position == 6:
        q11 = s0
        q23 = s1
        q18 = s2
        q17 = s3
        q16 = s4
        q5 = s5
        q19 = s6
        q10 = s7
    elif s.game.roto2.position == 7:
        q17 = s0
        q11 = s1
        q23 = s2
        q5 = s3
        q18 = s4
        q19 = s5
        q10 = s6
        q16 = s7

    if s.game.tilt.status == False:
        if s.holes:
            if 1 in s.holes:
                p = [38,604]
                screen.blit(number, p)
                p = [492,441]
                screen.blit(number, p)
            if 2 in s.holes:
                p = [38,549]
                screen.blit(number, p)
                p = [546,658]
                screen.blit(number, p)
            if 3 in s.holes:
                p = [254,658]
                screen.blit(number, p)
                p = [650,443]
                screen.blit(number, p)
            if 4 in s.holes:
                p = [90,442]
                screen.blit(number, p)
                p = [652,656]
                screen.blit(number, p)
            if 5 in s.holes:
                p = [144,658]
                screen.blit(number, p)
                p = q5
                screen.blit(number, p)
            if 6 in s.holes:
                p = [256,442]
                screen.blit(number, p)
                p = [438,548]
                screen.blit(number, p)
            if 7 in s.holes:
                p = [89,658]
                screen.blit(number, p)
                p = [651,549]
                screen.blit(number, p)
            if 8 in s.holes:
                p = [255,494]
                screen.blit(number, p)
                p = [440,494]
                screen.blit(number, p)
            if 9 in s.holes:
                p = [38,442]
                screen.blit(number, p)
                p = [546,442]
                screen.blit(number, p)
            if 10 in s.holes:
                p = [37,494]
                screen.blit(number, p)
                p = q10
                screen.blit(number, p)
            if 11 in s.holes:
                p = [36,657]
                screen.blit(number, p)
                p = q11
                screen.blit(number, p)
            if 12 in s.holes:
                p = r12
                screen.blit(number, p)
                p = [438,658]
                screen.blit(number, p)
            if 13 in s.holes:
                p = r13
                screen.blit(number, p)
                p = [652,602]
                screen.blit(number, p)
            if 14 in s.holes:
                p = r14
                screen.blit(number, p)
                p = [438,442]
                screen.blit(number, p)
            if 15 in s.holes:
                p = [147,440]
                screen.blit(number, p)
                p = [600,658]
                screen.blit(number, p)
            if 16 in s.holes:
                p = [146,549]
                screen.blit(number, p)
                p = q16
                screen.blit(number, p)
            if 17 in s.holes:
                p = [254,603]
                screen.blit(number, p)
                p = q17
                screen.blit(number, p)
            if 18 in s.holes:
                p = r18
                screen.blit(number, p)
                p = q18
                screen.blit(number, p)
            if 19 in s.holes:
                p = r19
                screen.blit(number, p)
                p = q19
                screen.blit(number, p)
            if 20 in s.holes:
                p = r20
                screen.blit(number, p)
                p = [652,496]
                screen.blit(number, p)
            if 21 in s.holes:
                p = r21
                screen.blit(number, p)
                p = [492,658]
                screen.blit(number, p)
            if 22 in s.holes:
                p = r22
                screen.blit(number, p)
                p = [546,550]
                screen.blit(number, p)
            if 23 in s.holes:
                p = [199,658]
                screen.blit(number, p)
                p = q23
                screen.blit(number, p)
            if 24 in s.holes:
                p = [200,442]
                screen.blit(number, p)
                p = [438,603]
                screen.blit(number, p)
            if 25 in s.holes:
                p = [254,550]
                screen.blit(number, p)
                p = [598,442]
                screen.blit(number, p)


    if s.game.tilt.status == True:
        tilt_position = [19,258]
        screen.blit(tilt, tilt_position)

    if s.game.roto_feature_step.position == 1:
        p = [24,717]
        screen.blit(r_arrow, p)
    if s.game.roto_feature_step.position == 2:
        p = [76,719]
        screen.blit(r_arrow, p)
    if s.game.roto_feature_step.position == 3:
        p = [128,718]
        screen.blit(r_arrow, p)
    if s.game.roto_feature_step.position >= 4 and s.game.roto_feature_step.position < 6:
        p = [175,712]
        screen.blit(before_fourth, p)
        if s.game.ball_count.position == 3:
            s.cancel_delayed(name="blink")
            blink([s,1,1])
        else:
            s.cancel_delayed(name="blink")
    if s.game.roto_feature_step.position >= 5:
        p = [320,712]
        screen.blit(spot_18, p)
    if s.game.roto_feature_step.position == 6:
        p = [423,712]
        screen.blit(before_fourth, p)
        if s.game.ball_count.position == 4:
            s.cancel_delayed(name="blink")
            blink([s,1,1])
        else:
            s.cancel_delayed(name="blink")
               
    if s.game.eb_play.status == True:
        p = [21,984]
        screen.blit(extra_balls, p)

    pygame.display.update()

def blink(args):
    dirty_rects = []
    s = args[0]
    b = args[1]
    sn = args[2]

    if b == 0:
        if sn == 1:
            p = [567,712]
            dirty_rects.append(screen.blit(select_now, p))
        pygame.display.update(dirty_rects)
    else:
        dirty_rects.append(screen.blit(bg_gi, (567,712), pygame.Rect(567,712,140,47)))
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
        p = [86,488]
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
        dirty_rects.append(screen.blit(topleft, (107  - num - 20, 500)))
        dirty_rects.append(screen.blit(topmiddle, (158  - num - 20, 500)))
        dirty_rects.append(screen.blit(topright, (204, 507 - num - 15)))
        dirty_rects.append(screen.blit(middleright, (204, 555 - num - 15)))
        dirty_rects.append(screen.blit(bottomright, (201  + num + 15, 602)))
        dirty_rects.append(screen.blit(bottommiddle, (151  + num + 15, 602)))
        dirty_rects.append(screen.blit(bottomleft, (96, 604 + num + 5)))
        dirty_rects.append(screen.blit(middleleft, (96, 555 + num + 5)))

    if (s.game.anti_cheat.status == True):
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],170,163)))
    else:
        dirty_rects.append(screen.blit(bg_off, p, pygame.Rect(p[0],p[1],170,163)))
    
    if 16 in s.holes:
        p = [146,549]
        dirty_rects.append(screen.blit(bg_gi, (146,549), pygame.Rect(146,549,50,51)))
        dirty_rects.append(screen.blit(number, p))
    
    pygame.display.update(dirty_rects)

def roto2_animation(args):
    dirty_rects = []
    s = args[0]
    num = args[1]
    square = args[2]
    
    p = [488,490]
    if s.game.roto2.position == 0:
        image = roto27
        topleft = r22
        topmiddle = r23
        topright = r24
        middleright = r25
        bottomright = r26
        bottommiddle = r27
        bottomleft = r28
        middleleft = r21
    elif s.game.roto2.position == 1:
        image = roto20
        topleft = r21
        topmiddle = r22
        topright = r23
        middleright = r24
        bottomright = r25
        bottommiddle = r26
        bottomleft = r27
        middleleft = r28
    elif s.game.roto2.position == 2:
        image = roto21
        topleft = r28
        topmiddle = r21
        topright = r22
        middleright = r23
        bottomright = r24
        bottommiddle = r25
        bottomleft = r26
        middleleft = r27
    elif s.game.roto2.position == 3:
        image = roto22
        topleft = r27
        topmiddle = r28
        topright = r21
        middleright = r22
        bottomright = r23
        bottommiddle = r24
        bottomleft = r25
        middleleft = r26
    elif s.game.roto2.position == 4:
        image = roto23
        topleft = r26
        topmiddle = r27
        topright = r28
        middleright = r21
        bottomright = r22
        bottommiddle = r23
        bottomleft = r24
        middleleft = r25
    elif s.game.roto2.position == 5:
        image = roto24
        topleft = r25
        topmiddle = r26
        topright = r27
        middleright = r28
        bottomright = r21
        bottommiddle = r22
        bottomleft = r23
        middleleft = r24
    elif s.game.roto2.position == 6:
        image = roto25
        topleft = r24
        topmiddle = r25
        topright = r26
        middleright = r27
        bottomright = r28
        bottommiddle = r21
        bottomleft = r22
        middleleft = r23
    elif s.game.roto2.position == 7:
        image = roto26
        topleft = r23
        topmiddle = r24
        topright = r25
        middleright = r26
        bottomright = r27
        bottommiddle = r28
        bottomleft = r21
        middleleft = r22


    rect = pygame.Rect(p[0],p[1],200,200)

    #letter A
    if square == 2: 
        dirty_rects.append(screen.blit(topleft, (509  - num - 20, 502)))
        dirty_rects.append(screen.blit(topmiddle, (556  - num - 20, 502)))
        dirty_rects.append(screen.blit(topright, (606, 509 - num - 15)))
        dirty_rects.append(screen.blit(middleright, (606, 557 - num - 15)))
        dirty_rects.append(screen.blit(bottomright, (603  + num + 15, 604)))
        dirty_rects.append(screen.blit(bottommiddle, (553  + num + 15, 604)))
        dirty_rects.append(screen.blit(bottomleft, (498, 606 + num + 5)))
        dirty_rects.append(screen.blit(middleleft, (498, 555 + num + 5)))



    if (s.game.anti_cheat.status == True):
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],170,163)))
    else:
        dirty_rects.append(screen.blit(bg_off, p, pygame.Rect(p[0],p[1],170,163)))
    
    if 22 in s.holes:
        p = [546,550]
        dirty_rects.append(screen.blit(bg_gi, (546,550), pygame.Rect(546,550,50,51)))
        dirty_rects.append(screen.blit(number, p))
    
    pygame.display.update(dirty_rects)



def eb_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]
    if s.game.extra_ball.position < 5:
        dirty_rects.append(screen.blit(bg_gi, (100,1015), pygame.Rect(100,1015,173,32)))
    if s.game.extra_ball.position < 10:
        dirty_rects.append(screen.blit(bg_gi, (278,1017), pygame.Rect(278,1017,173,32)))
    if s.game.extra_ball.position < 15:
        dirty_rects.append(screen.blit(bg_gi, (456,1013), pygame.Rect(456,1013,173,32)))
        dirty_rects.append(screen.blit(bg_gi, (602,980), pygame.Rect(602,980,23,32)))
    pygame.display.update(dirty_rects)
    if num in [0,1,6,7,12,13,18,19,26,27,32,33,38,39,44,45]:
        if s.game.extra_ball.position < 5:
            p = [100,1015]
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
            p = [456,1013]
            dirty_rects.append(screen.blit(eb, p))
            p = [602,980]
            dirty_rects.append(screen.blit(eb_arrow, p))
            pygame.display.update(dirty_rects)
            return

def clear_odds(s, num):
    global screen
    dirty_rects = []
    if s.game.odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (240,889), pygame.Rect(240,889,88,86)))
    if s.game.odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (203,766), pygame.Rect(203,766,56,103)))
    if s.game.odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (280,776), pygame.Rect(280,776,34,112)))
    if s.game.odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (437,762), pygame.Rect(437,762,69,107)))
    if s.game.odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (558,764), pygame.Rect(558,764,52,110)))
    if s.game.odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (614,798), pygame.Rect(614,798,35,109)))
    if s.game.odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (656,765), pygame.Rect(656,765,44,108)))
    if s.game.odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (619,911), pygame.Rect(619,911,86,69)))

    pygame.display.update(dirty_rects)

def draw_odds_animation(s, num):
    global screen
    dirty_rects = []
    if num in [0,1,40,14,24,25]:
        if s.game.odds.position != 1:
            p = [240,889]
            dirty_rects.append(screen.blit(o1, p))
            pygame.display.update(dirty_rects)
            return
    if num in [2,3,41,15,26,27]:
        if s.game.odds.position != 2:
            p = [203,766]
            dirty_rects.append(screen.blit(o2, p))
            pygame.display.update(dirty_rects)
            return
    if num in [4,5,42,16,28,29]:
        if s.game.odds.position != 3:
            p = [280,776]
            dirty_rects.append(screen.blit(o3, p))
            pygame.display.update(dirty_rects)
            return
    if num in [6,7,43,17,30,31]:
        if s.game.odds.position != 4:
            p = [437,762]
            dirty_rects.append(screen.blit(o4, p))
            pygame.display.update(dirty_rects)
            return
    if num in [8,9,44,18,32,33]:
        if s.game.odds.position != 5:
            p = [558,764]
            dirty_rects.append(screen.blit(o5, p))
            pygame.display.update(dirty_rects)
            return
    if num in [10,11,45,19,34,35]:
        if s.game.odds.position != 6:
            p = [614,798]
            dirty_rects.append(screen.blit(o6, p))
            pygame.display.update(dirty_rects)
            return
    if num in [12,13,46,47,20,21,36,37]:
        if s.game.odds.position != 7:
            p = [656,765]
            dirty_rects.append(screen.blit(o7, p))
            pygame.display.update(dirty_rects)
            return
    if num in [14,48,49,22,23,38]:
        if s.game.odds.position != 8:
            p = [619,911]
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
   
    if s.game.red_star.status == False:
        dirty_rects.append(screen.blit(bg_gi, (642,978), pygame.Rect(642,978,58,58)))
    if s.game.cornerstwo_three.status == False:
        dirty_rects.append(screen.blit(bg_gi, (430,390), pygame.Rect(430,390,106,44)))
    if s.game.cornerstwo_four.status == False:
        dirty_rects.append(screen.blit(bg_gi, (596,392), pygame.Rect(596,392,110,41)))
    if s.game.cornersone_three.status == False:
        dirty_rects.append(screen.blit(bg_gi, (30,388), pygame.Rect(30,388,106,44)))
    if s.game.roto_feature_step.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (423,712), pygame.Rect(423,712, 143,47)))
    if s.game.roto_feature_step.position < 5:
        dirty_rects.append(screen.blit(bg_gi, (320,712), pygame.Rect(320,712,104,47)))
    if s.game.roto_feature_step.position < 4:
        dirty_rects.append(screen.blit(bg_gi, (175,712), pygame.Rect(175,712,143,47)))
    if s.game.roto_feature_step.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (128,718), pygame.Rect(128,718,42,37)))
    if s.game.roto_feature_step.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (76,719), pygame.Rect(76,719,42,37)))
    if s.game.roto_feature_step.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (24,717), pygame.Rect(24,717,42,37)))
    if s.game.cornersone_four.status == False:
        dirty_rects.append(screen.blit(bg_gi, (202,389), pygame.Rect(202,389,110,41)))

    pygame.display.update(dirty_rects)


def draw_feature_animation(s, num):
    global screen
    dirty_rects = []

    if num in [11,12,36,37]:
        if s.game.red_star.status == False:
            p = [642,978]
            dirty_rects.append(screen.blit(star, p))
            s.game.coils.redROLamp.pulse(85)
            s.game.coils.yellowROLamp.pulse(85)
            pygame.display.update(dirty_rects)
            return
    if num in [9,10,34,35]:
        if s.game.cornerstwo_three.status == False:
            p = [430,390]
            dirty_rects.append(screen.blit(corners3, p))
            pygame.display.update(dirty_rects)
            return
    if num in [7,8,32,33]:
        if s.game.cornerstwo_four.status == False:
            p = [596,392]
            dirty_rects.append(screen.blit(corners4, p))
            pygame.display.update(dirty_rects)
            return
    if num in [5,6,30,31]:
        if s.game.cornersone_three.status == False:
            p = [30,388]
            dirty_rects.append(screen.blit(corners3, p))
            pygame.display.update(dirty_rects)
            return
    #if num in [3,4,28,29]:
    #    if s.game.selection_feature.position < 8:
    #        p = [447,727]
    #        dirty_rects.append(screen.blit(s_number, p))
    #        pygame.display.update(dirty_rects)
    #        return
    if num in [1,2,26,27]:
        if s.game.roto_feature_step.position < 6:
            p = [423,712]
            dirty_rects.append(screen.blit(before_fourth, p))
            pygame.display.update(dirty_rects)
            return
    if num in [0,49,24,25]:
        if s.game.roto_feature_step.position < 5:
            p = [320,712]
            dirty_rects.append(screen.blit(spot_18, p))
            pygame.display.update(dirty_rects)
            return
    if num in [47,48,22,23]:
        if s.game.roto_feature_step.position < 4:
            p = [175,712]
            dirty_rects.append(screen.blit(before_fourth, p))
            pygame.display.update(dirty_rects)
            return
    if num in [45,46,20,21]:
        if s.game.roto_feature_step.position != 3:
            p = [128,718]
            dirty_rects.append(screen.blit(r_arrow, p))
            pygame.display.update(dirty_rects)
            return
    if num in [43,44,18,19]:
        if s.game.roto_feature_step.position != 2:
            p = [76,719]
            dirty_rects.append(screen.blit(r_arrow, p))
            pygame.display.update(dirty_rects)
            return
    if num in [41,42,16,17]:
        if s.game.roto_feature_step.position != 1:
            p = [24,717]
            dirty_rects.append(screen.blit(r_arrow, p))
            pygame.display.update(dirty_rects)
            return
    if num in [39,40,14,15]:
        if s.game.cornersone_four.status == False:
            p = [202,389]
            dirty_rects.append(screen.blit(corners4, p))
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

