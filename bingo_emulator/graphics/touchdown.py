
import pygame
import random

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

meter = pygame.image.load('graphics/assets/register_cover.png').convert()
eb = pygame.image.load('touchdown/assets/eb.png').convert_alpha()
eb_number = pygame.image.load('touchdown/assets/eb_number.png').convert_alpha()
extra_balls = pygame.image.load('touchdown/assets/extra_balls.png').convert_alpha()
odds = pygame.image.load('touchdown/assets/odds.png').convert_alpha()
star = pygame.image.load('touchdown/assets/star.png').convert_alpha()
number = pygame.image.load('touchdown/assets/number.png').convert_alpha()
tilt = pygame.image.load('touchdown/assets/tilt.png').convert_alpha()
time = pygame.image.load('touchdown/assets/time.png').convert_alpha()
mn_arrow = pygame.image.load('touchdown/assets/mn_arrow.png').convert_alpha()
pap = pygame.image.load('touchdown/assets/pap.png').convert_alpha()
spot_16 = pygame.image.load('touchdown/assets/spot_16.png').convert_alpha()
letter_a = pygame.image.load('touchdown/assets/letter_a.png').convert_alpha()
letter_b = pygame.image.load('touchdown/assets/letter_b.png').convert_alpha()
letter_c = pygame.image.load('touchdown/assets/letter_c.png').convert_alpha()
letter_d = pygame.image.load('touchdown/assets/letter_d.png').convert_alpha()
letter = pygame.image.load('touchdown/assets/letter.png').convert_alpha()
letter_separator = pygame.image.load('touchdown/assets/letter_separator.png').convert_alpha()

numbera0 = pygame.image.load('touchdown/assets/numbera0.png').convert()
numbera1 = pygame.image.load('touchdown/assets/numbera1.png').convert()
numbera2 = pygame.image.load('touchdown/assets/numbera2.png').convert()
numbera3 = pygame.image.load('touchdown/assets/numbera3.png').convert()
numbera4 = pygame.image.load('touchdown/assets/numbera4.png').convert()
numbera5 = pygame.image.load('touchdown/assets/numbera5.png').convert()
numberb0 = pygame.image.load('touchdown/assets/numberb0.png').convert()
numberb1 = pygame.image.load('touchdown/assets/numberb1.png').convert()
numberb2 = pygame.image.load('touchdown/assets/numberb2.png').convert()
numberb3 = pygame.image.load('touchdown/assets/numberb3.png').convert()
numberb4 = pygame.image.load('touchdown/assets/numberb4.png').convert()
numberb5 = pygame.image.load('touchdown/assets/numberb5.png').convert()
numberc0 = pygame.image.load('touchdown/assets/numberc0.png').convert()
numberc1 = pygame.image.load('touchdown/assets/numberc1.png').convert()
numberc2 = pygame.image.load('touchdown/assets/numberc2.png').convert()
numberc3 = pygame.image.load('touchdown/assets/numberc3.png').convert()
numberc4 = pygame.image.load('touchdown/assets/numberc4.png').convert()
numberc5 = pygame.image.load('touchdown/assets/numberc5.png').convert()
numberd0 = pygame.image.load('touchdown/assets/numberd0.png').convert()
numberd1 = pygame.image.load('touchdown/assets/numberd1.png').convert()
numberd2 = pygame.image.load('touchdown/assets/numberd2.png').convert()
numberd3 = pygame.image.load('touchdown/assets/numberd3.png').convert()
numberd4 = pygame.image.load('touchdown/assets/numberd4.png').convert()
numberd5 = pygame.image.load('touchdown/assets/numberd5.png').convert()
number16 = pygame.image.load('touchdown/assets/number16.png').convert()
bg_menu = pygame.image.load('touchdown/assets/touchdown_menu.png')
bg_gi = pygame.image.load('touchdown/assets/touchdown_gi.png')
bg_off = pygame.image.load('touchdown/assets/touchdown_off.png')
a_1 = pygame.image.load('touchdown/assets/a-1.png').convert_alpha()
a_2 = pygame.image.load('touchdown/assets/a-2.png').convert_alpha()
a_3 = pygame.image.load('touchdown/assets/a-3.png').convert_alpha()
a_4 = pygame.image.load('touchdown/assets/a-4.png').convert_alpha()
a_5 = pygame.image.load('touchdown/assets/a-5.png').convert_alpha()
a_6 = pygame.image.load('touchdown/assets/a-6.png').convert_alpha()
b_1 = pygame.image.load('touchdown/assets/b-1.png').convert_alpha()
b_2 = pygame.image.load('touchdown/assets/b-2.png').convert_alpha()
b_3 = pygame.image.load('touchdown/assets/b-3.png').convert_alpha()
b_4 = pygame.image.load('touchdown/assets/b-4.png').convert_alpha()
b_5 = pygame.image.load('touchdown/assets/b-5.png').convert_alpha()
b_6 = pygame.image.load('touchdown/assets/b-6.png').convert_alpha()
c_1 = pygame.image.load('touchdown/assets/c-1.png').convert_alpha()
c_2 = pygame.image.load('touchdown/assets/c-2.png').convert_alpha()
c_3 = pygame.image.load('touchdown/assets/c-3.png').convert_alpha()
c_4 = pygame.image.load('touchdown/assets/c-4.png').convert_alpha()
c_5 = pygame.image.load('touchdown/assets/c-5.png').convert_alpha()
c_6 = pygame.image.load('touchdown/assets/c-6.png').convert_alpha()
d_1 = pygame.image.load('touchdown/assets/d-1.png').convert_alpha()
d_2 = pygame.image.load('touchdown/assets/d-2.png').convert_alpha()
d_3 = pygame.image.load('touchdown/assets/d-3.png').convert_alpha()
d_4 = pygame.image.load('touchdown/assets/d-4.png').convert_alpha()
d_5 = pygame.image.load('touchdown/assets/d-5.png').convert_alpha()
d_6 = pygame.image.load('touchdown/assets/d-6.png').convert_alpha()



class scorereel():
    """ Score Reels are used to count replays """
    def __init__(self, pos, image):
        self.position = pos
        self.default_y = self.position[1]
        self.image = pygame.image.load(image).convert()

reel1 = scorereel([88,793], "graphics/assets/white_reel.png")
reel10 = scorereel([69,793], "graphics/assets/white_reel.png")
reel100 = scorereel([50,793], "graphics/assets/white_reel.png")

def display(s, replays=0, menu=False):
    
    meter.set_colorkey((255,0,252))
    meter_position = [40,793]

    screen.blit(reel1.image, reel1.position)
    screen.blit(reel10.image, reel10.position)
    screen.blit(reel100.image, reel100.position)
    screen.blit(meter, meter_position)

    if s.game.numbera.position == 0:
        p = [217,357]
        screen.blit(numbera0, p)
    elif s.game.numbera.position == 1:
        p = [217,357]
        screen.blit(numbera1, p)
    elif s.game.numbera.position == 2:
        p = [217,357]
        screen.blit(numbera2, p)
    elif s.game.numbera.position == 3:
        p = [217,357]
        screen.blit(numbera3, p)
    elif s.game.numbera.position == 4:
        p = [217,357]
        screen.blit(numbera4, p)
    elif s.game.numbera.position == 5:
        p = [217,357]
        screen.blit(numbera5, p)

    if s.game.numberb.position == 0:
        p = [220,528]
        screen.blit(numberb0, p)
    elif s.game.numberb.position == 1:
        p = [220,528]
        screen.blit(numberb1, p)
    elif s.game.numberb.position == 2:
        p = [220,528]
        screen.blit(numberb2, p)
    elif s.game.numberb.position == 3:
        p = [220,528]
        screen.blit(numberb3, p)
    elif s.game.numberb.position == 4:
        p = [220,528]
        screen.blit(numberb4, p)
    elif s.game.numberb.position == 5:
        p = [220,528]
        screen.blit(numberb5, p)

    if s.game.numberc.position == 0:
        p = [393,470]
        screen.blit(numberc0, p)
    elif s.game.numberc.position == 1:
        p = [393,470]
        screen.blit(numberc1, p)
    elif s.game.numberc.position == 2:
        p = [393,470]
        screen.blit(numberc2, p)
    elif s.game.numberc.position == 3:
        p = [393,470]
        screen.blit(numberc3, p)
    elif s.game.numberc.position == 4:
        p = [393,470]
        screen.blit(numberc4, p)
    elif s.game.numberc.position == 5:
        p = [393,470]
        screen.blit(numberc5, p)

    if s.game.numberd.position == 0:
        p = [339,358]
        screen.blit(numberd0, p)
    elif s.game.numberd.position == 1:
        p = [339,358]
        screen.blit(numberd1, p)
    elif s.game.numberd.position == 2:
        p = [339,358]
        screen.blit(numberd2, p)
    elif s.game.numberd.position == 3:
        p = [339,358]
        screen.blit(numberd3, p)
    elif s.game.numberd.position == 4:
        p = [339,358]
        screen.blit(numberd4, p)
    elif s.game.numberd.position == 5:
        p = [339,358]
        screen.blit(numberd5, p)

    p = [339,475]
    screen.blit(number16, p)

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

    if s.game.extra_ball.position >= 1:
        eb_position = [143,1024]
        screen.blit(eb_number, eb_position)
    if s.game.extra_ball.position >= 2:
        eb_position = [192,1025]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 3:
        eb_position = [254,1025]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 4:
        eb_position = [323,1026]
        screen.blit(eb_number, eb_position)
    if s.game.extra_ball.position >= 5:
        eb_position = [371,1026]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 6:
        eb_position = [435,1026]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 7:
        eb_position = [501,1025]
        screen.blit(eb_number, eb_position)
    if s.game.extra_ball.position >= 8:
        eb_position = [552,1024]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 9:
        eb_position = [615,1024]
        screen.blit(eb, eb_position)

    if s.game.start.status == True:
        if s.game.all_advantages.status == True:
            p = [21,601]
            screen.blit(pap, p)
        if s.game.odds_only.status == True:
            p = [21,445]
            screen.blit(pap, p)
        if s.game.features.status == True:
            p = [21,523]
            screen.blit(pap, p)

    if s.game.red_star.status == True:
        rs_position = [635,956]
        screen.blit(star, rs_position)

    if s.game.yellow_star.status == True:
        ys_position = [23,954]
        screen.blit(star, ys_position)

    if s.game.four_stars.status == True:
        p = [21,367]
        screen.blit(pap, p)

    if s.game.red_odds.position == 1:
        p = [327,758]
        screen.blit(odds, p)
    elif s.game.red_odds.position == 2:
        p = [388,758]
        screen.blit(odds, p)
    elif s.game.red_odds.position == 3:
        p = [452,758]
        screen.blit(odds, p)
    elif s.game.red_odds.position == 4:
        p = [507,758]
        screen.blit(odds, p)
    elif s.game.red_odds.position == 5:
        p = [556,758]
        screen.blit(odds, p)
    elif s.game.red_odds.position == 6:
        p = [605,758]
        screen.blit(odds, p)
    elif s.game.red_odds.position == 7:
        p = [653,758]
        screen.blit(odds, p)

    if s.game.yellow_odds.position == 1:
        p = [327,822]
        screen.blit(odds, p)
    elif s.game.yellow_odds.position == 2:
        p = [388,822]
        screen.blit(odds, p)
    elif s.game.yellow_odds.position == 3:
        p = [452,822]
        screen.blit(odds, p)
    elif s.game.yellow_odds.position == 4:
        p = [507,822]
        screen.blit(odds, p)
    elif s.game.yellow_odds.position == 5:
        p = [556,822]
        screen.blit(odds, p)
    elif s.game.yellow_odds.position == 6:
        p = [605,822]
        screen.blit(odds, p)
    elif s.game.yellow_odds.position == 7:
        p = [651,822]
        screen.blit(odds, p)

    if s.game.green_odds.position == 1:
        p = [265,890]
        screen.blit(odds, p)
    elif s.game.green_odds.position == 2:
        p = [327,890]
        screen.blit(odds, p)
    elif s.game.green_odds.position == 3:
        p = [388,890]
        screen.blit(odds, p)
    elif s.game.green_odds.position == 4:
        p = [452,890]
        screen.blit(odds, p)
    elif s.game.green_odds.position == 5:
        p = [507,890]
        screen.blit(odds, p)
    elif s.game.green_odds.position == 6:
        p = [556,890]
        screen.blit(odds, p)
    elif s.game.green_odds.position == 7:
        p = [605,890]
        screen.blit(odds, p)
    elif s.game.green_odds.position == 8:
        p = [651,890]
        screen.blit(odds, p)

    if s.game.spot_16.status == True:
        p = [20,684]
        screen.blit(spot_16, p)

    a1 = [220,361]
    a2 = [280,360]
    a3 = [219,417]
    a4 = [279,417]
    a5 = [220,473]
    a6 = [279,474]

    b1 = [220,532]
    b2 = [279,531]
    b3 = [339,531]
    b4 = [219,589]
    b5 = [279,589]
    b6 = [340,589]

    c1 = [399,473]
    c2 = [459,474]
    c3 = [400,531]
    c4 = [460,531]
    c5 = [400,589]
    c6 = [460,589]

    d1 = [340,360]
    d2 = [399,359]
    d3 = [457,360]
    d4 = [339,417]
    d5 = [399,417]
    d6 = [459,417]

    if s.game.numbera.position == 0:
        n9 = a1
        n1 = a2
        n4 = a3
        n19 = a4
        n25 = a5
        n24 = a6
    elif s.game.numbera.position == 1:
        n4 = a1
        n9 = a2
        n25 = a3
        n1 = a4
        n24 = a5
        n19 = a6
    elif s.game.numbera.position == 2:
        n25 = a1
        n4 = a2
        n24 = a3
        n9 = a4
        n19 = a5
        n1 = a6
    elif s.game.numbera.position == 3:
        n24 = a1
        n25 = a2
        n19 = a3
        n4 = a4
        n1 = a5
        n9 = a6
    elif s.game.numbera.position == 4:
        n19 = a1
        n24 = a2
        n1 = a3
        n25 = a4
        n9 = a5
        n4 = a6
    elif s.game.numbera.position == 5:
        n1 = a1
        n19 = a2
        n9 = a3
        n24 = a4
        n4 = a5
        n25 = a6

    if s.game.numberb.position == 0:
        n6 = b1
        n23 = b2
        n5 = b3
        n12 = b4
        n8 = b5
        n14 = b6
    elif s.game.numberb.position == 1:
        n12 = b1
        n6 = b2
        n23 = b3
        n8 = b4
        n14 = b5
        n5 = b6
    elif s.game.numberb.position == 2:
        n8 = b1
        n12 = b2
        n6 = b3
        n14 = b4
        n5 = b5
        n23 = b6
    elif s.game.numberb.position == 3:
        n14 = b1
        n8 = b2
        n12 = b3
        n5 = b4
        n23 = b5
        n6 = b6
    elif s.game.numberb.position == 4:
        n5 = b1
        n14 = b2
        n8 = b3
        n23 = b4
        n6 = b5
        n12 = b6
    elif s.game.numberb.position == 5:
        n23 = b1
        n5 = b2
        n14 = b3
        n6 = b4
        n12 = b5
        n8 = b6

    if s.game.numberc.position == 0:
        n13 = c1
        n17 = c2
        n21 = c3
        n20 = c4
        n3 = c5
        n10 = c6
    elif s.game.numberc.position == 1:
        n21 = c1
        n13 = c2
        n3 = c3
        n17 = c4
        n10 = c5
        n20 = c6
    elif s.game.numberc.position == 2:
        n3 = c1
        n21 = c2
        n10 = c3
        n13 = c4
        n20 = c5
        n17 = c6
    elif s.game.numberc.position == 3:
        n10 = c1
        n3 = c2
        n20 = c3
        n21 = c4
        n17 = c5
        n13 = c6
    elif s.game.numberc.position == 4:
        n20 = c1
        n10 = c2
        n17 = c3
        n3 = c4
        n13 = c5
        n21 = c6
    elif s.game.numberc.position == 5:
        n17 = c1
        n20 = c2
        n13 = c3
        n10 = c4
        n21 = c5
        n3 = c6

    if s.game.numberd.position == 0:
        n2 = d1
        n11 = d2
        n15 = d3
        n7 = d4
        n22 = d5
        n18 = d6
    elif s.game.numberd.position == 1:
        n7 = d1
        n2 = d2
        n11 = d3
        n22 = d4
        n18 = d5
        n15 = d6
    elif s.game.numberd.position == 2:
        n22 = d1
        n7 = d2
        n2 = d3
        n18 = d4
        n15 = d5
        n11 = d6
    elif s.game.numberd.position == 3:
        n18 = d1
        n22 = d2
        n7 = d3
        n15 = d4
        n11 = d5
        n2 = d6
    elif s.game.numberd.position == 4:
        n15 = d1
        n18 = d2
        n22 = d3
        n11 = d4
        n2 = d5
        n7 = d6
    elif s.game.numberd.position == 5:
        n11 = d1
        n15 = d2
        n18 = d3
        n2 = d4
        n7 = d5
        n22 = d6

    if s.game.tilt.status == False:
        if s.holes:
            if 1 in s.holes:
                p = n1
                screen.blit(number, p)
            if 2 in s.holes:
                p = n2
                screen.blit(number, p)
            if 3 in s.holes:
                p = n3
                screen.blit(number, p)
            if 4 in s.holes:
                p = n4
                screen.blit(number, p)
            if 5 in s.holes:
                p = n5
                screen.blit(number, p)
            if 6 in s.holes:
                p = n6
                screen.blit(number, p)
            if 7 in s.holes:
                p = n7
                screen.blit(number, p)
            if 8 in s.holes:
                p = n8
                screen.blit(number, p)
            if 9 in s.holes:
                p = n9
                screen.blit(number, p)
            if 10 in s.holes:
                p = n10
                screen.blit(number, p)
            if 11 in s.holes:
                p = n11
                screen.blit(number, p)
            if 12 in s.holes:
                p = n12
                screen.blit(number, p)
            if 13 in s.holes:
                p = n13
                screen.blit(number, p)
            if 14 in s.holes:
                p = n14
                screen.blit(number, p)
            if 15 in s.holes:
                p = n15
                screen.blit(number, p)
            if 16 in s.holes:
                p = [339,473]
                screen.blit(number, p)
            if 17 in s.holes:
                p = n17
                screen.blit(number, p)
            if 18 in s.holes:
                p = n18
                screen.blit(number, p)
            if 19 in s.holes:
                p = n19
                screen.blit(number, p)
            if 20 in s.holes:
                p = n20
                screen.blit(number, p)
            if 21 in s.holes:
                p = n21
                screen.blit(number, p)
            if 22 in s.holes:
                p = n22
                screen.blit(number, p)
            if 23 in s.holes:
                p = n23
                screen.blit(number, p)
            if 24 in s.holes:
                p = n24
                screen.blit(number, p)
            if 25 in s.holes:
                p = n25
                screen.blit(number, p)

    if s.game.magic_numbers_feature.position == 1:
        p = [122,694]
        screen.blit(mn_arrow, p)
    elif s.game.magic_numbers_feature.position == 2:
        p = [160,694]
        screen.blit(mn_arrow, p)
    elif s.game.magic_numbers_feature.position == 3:
        p = [198,694]
        screen.blit(mn_arrow, p)
    if s.game.magic_numbers_feature.position >= 4:
        p = [242,686]
        screen.blit(letter,p)
        p = [188,420]
        screen.blit(letter_a, p)
    if s.game.magic_numbers_feature.position == 5:
        p = [278,695]
        screen.blit(letter_separator, p)
    if s.game.magic_numbers_feature.position >= 6:
        p = [306,686]
        screen.blit(letter, p)
        p = [286,632]
        screen.blit(letter_b, p)
    if s.game.magic_numbers_feature.position == 7:
        p = [341,694]
        screen.blit(letter_separator, p)
    if s.game.magic_numbers_feature.position >= 8:
        p = [370,686]
        screen.blit(letter, p)
        p = [504,535]
        screen.blit(letter_c, p)
    if s.game.magic_numbers_feature.position == 9:
        p = [406,696]
        screen.blit(letter_separator, p)
    if s.game.magic_numbers_feature.position == 10:
        p = [434,686]
        screen.blit(letter, p)
        p = [407,323]
        screen.blit(letter_d, p)

    if s.game.magic_numbers_feature.position > 3:
        if s.game.before_fourth.status == True:
            p = [574,522]
            screen.blit(time, p)
            if s.game.ball_count.position == 3:
                s.cancel_delayed(name="blink")
                blink([s,1,1])
            else:
                s.cancel_delayed(name="blink")
        elif s.game.before_fifth.status == True:
            p = [574,444]
            screen.blit(time, p)
            if s.game.ball_count.position == 4:
                s.cancel_delayed(name="blink")
                blink([s,1,1])
            else:
                s.cancel_delayed(name="blink")
        elif s.game.after_fifth.status == True:
            p = [574,366]
            screen.blit(time, p)
            if s.game.ball_count.position == 5:
                s.cancel_delayed(name="blink")
                blink([s,1,1])
            else:
                s.cancel_delayed(name="blink")

    if s.game.tilt.status == True:
        tilt_position = [34,750]
        screen.blit(tilt, tilt_position)
               
    if s.game.eb_play.status == True:
        p = [34,1022]
        screen.blit(extra_balls, p)

    pygame.display.update()

def blink(args):
    dirty_rects = []
    s = args[0]
    b = args[1]
    sn = args[2]

    if b == 0:
        if sn == 1:
            p = [576,600]
            dirty_rects.append(screen.blit(time, p))
        pygame.display.update(dirty_rects)
    else:
        dirty_rects.append(screen.blit(bg_gi, (576,600), pygame.Rect(576,600,120,57)))
        pygame.display.update(dirty_rects)
    b = not b

    args = [s,b,sn]

    s.delay(name="blink", delay=0.1, handler=blink, param=args)

def numbera_animation(args):
    dirty_rects = []
    s = args[0]
    num = args[1]
    number = args[2]
    
    if number == 1:
        p = [217,357]
        if s.game.numbera.position == 0:
            image = numbera5
            topleft = a_2
            topright = a_4
            middleleft = a_1
            middleright = a_6
            bottomleft = a_3
            bottomright = a_5
        elif s.game.numbera.position == 1:
            image = numbera0
            topleft = a_1
            topright = a_2
            middleleft = a_3
            middleright = a_4
            bottomleft = a_5
            bottomright = a_6
        elif s.game.numbera.position == 2:
            image = numbera1
            topleft = a_3
            topright = a_1
            middleleft = a_5
            middleright = a_2
            bottomleft = a_6
            bottomright = a_4
        elif s.game.numbera.position == 3:
            image = numbera2
            topleft = a_5
            topright = a_3
            middleleft = a_6
            middleright = a_1
            bottomleft = a_4
            bottomright = a_2
        elif s.game.numbera.position == 4:
            image = numbera3
            topleft = a_6
            topright = a_5
            middleleft = a_4
            middleright = a_3
            bottomleft = a_2
            bottomright = a_1
        elif s.game.numbera.position == 5:
            image = numbera4
            topleft = a_4
            topright = a_6
            middleleft = a_2
            middleright = a_5
            bottomleft = a_1
            bottomright = a_3

    rect = pygame.Rect(p[0],p[1],200,200)

    #letter A
    if number == 1: 
        dirty_rects.append(screen.blit(topleft, (222  - num, 365)))
        dirty_rects.append(screen.blit(topright, (280, 360 - num - 2)))
        dirty_rects.append(screen.blit(middleleft, (222, 417 + num + 10)))
        dirty_rects.append(screen.blit(middleright, (278, 416 - num - 10)))
        dirty_rects.append(screen.blit(bottomleft, (222, 474 + num + 10)))
        dirty_rects.append(screen.blit(bottomright, (278  + num + 10, 474)))

    if (s.game.anti_cheat.status == True):
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],113,166)))
    else:
        dirty_rects.append(screen.blit(bg_off, p, pygame.Rect(p[0],p[1],113,166)))

    pygame.display.update(dirty_rects)

def numberb_animation(args):
    dirty_rects = []
    s = args[0]
    num = args[1]
    number = args[2]
    
    if number == 2:
        p = [220,528]
        if s.game.numberb.position == 0:
            image = numberb5
            topleft = b_2
            topmiddle = b_3
            topright = b_4
            bottomright = b_5
            bottommiddle = b_6
            bottomleft = b_1
        elif s.game.numberb.position == 1:
            image = numberb0
            topleft = b_1
            topmiddle = b_2
            topright = b_3
            bottomright = b_4
            bottommiddle = b_5
            bottomleft = b_6
        elif s.game.numberb.position == 2:
            image = numberb1
            topleft = b_6
            topmiddle = b_1
            topright = b_2
            bottomright = b_3
            bottommiddle = b_4
            bottomleft = b_5
        elif s.game.numberb.position == 3:
            image = numberb2
            topleft = b_5
            topmiddle = b_6
            topright = b_1
            bottomright = b_2
            bottommiddle = b_3
            bottomleft = b_4
        elif s.game.numberb.position == 4:
            image = numberb3
            topleft = b_4
            topmiddle = b_5
            topright = b_6
            bottomright = b_1
            bottommiddle = b_2
            bottomleft = b_3
        elif s.game.numberb.position == 5:
            image = numberb4
            topleft = b_3
            topmiddle = b_4
            topright = b_5
            bottomright = b_6
            bottommiddle = b_1
            bottomleft = b_2

    rect = pygame.Rect(p[0],p[1],200,200)

    if number == 2: 
        dirty_rects.append(screen.blit(topleft, (218  - num, 538)))
        dirty_rects.append(screen.blit(topmiddle, (277 - num, 538)))
        dirty_rects.append(screen.blit(topright, (335, 542 - num - 15)))
        dirty_rects.append(screen.blit(bottomright, (338 + num + 10, 592)))
        dirty_rects.append(screen.blit(bottommiddle, (278 + num + 10, 592)))
        dirty_rects.append(screen.blit(bottomleft, (224, 592 + num + 15)))

    if (s.game.anti_cheat.status == True):
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],171,111)))
    else:
        dirty_rects.append(screen.blit(bg_off, p, pygame.Rect(p[0],p[1],171,111)))

    p = [286,632]
    dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],22,29)))
    dirty_rects.append(screen.blit(letter_b, p))

    pygame.display.update(dirty_rects)


def numberc_animation(args):
    dirty_rects = []
    s = args[0]
    num = args[1]
    number = args[2]
    
    if number == 3:
        p = [393,470]
        if s.game.numberc.position == 0:
            image = numberc5
            topleft = c_2
            topright = c_4
            middleleft = c_1
            middleright = c_6
            bottomleft = c_3
            bottomright = c_5
        elif s.game.numberc.position == 1:
            image = numberc0
            topleft = c_1
            topright = c_2
            middleleft = c_3
            middleright = c_4
            bottomleft = c_5
            bottomright = c_6
        elif s.game.numberc.position == 2:
            image = numberc1
            topleft = c_3
            topright = c_1
            middleleft = c_5
            middleright = c_2
            bottomleft = c_6
            bottomright = c_4
        elif s.game.numberc.position == 3:
            image = numberc2
            topleft = c_5
            topright = c_3
            middleleft = c_6
            middleright = c_1
            bottomleft = c_4
            bottomright = c_2
        elif s.game.numberc.position == 4:
            image = numberc3
            topleft = c_6
            topright = c_5
            middleleft = c_4
            middleright = c_3
            bottomleft = c_2
            bottomright = c_1
        elif s.game.numberc.position == 5:
            image = numberc4
            topleft = c_4
            topright = c_6
            middleleft = c_2
            middleright = c_5
            bottomleft = c_1
            bottomright = c_3

    rect = pygame.Rect(p[0],p[1],200,200)

    if number == 3: 
        dirty_rects.append(screen.blit(topleft, (398  - num, 478)))
        dirty_rects.append(screen.blit(topright, (458, 472 - num - 2)))
        dirty_rects.append(screen.blit(middleleft, (398,531 + num + 10)))
        dirty_rects.append(screen.blit(middleright, (458,530 - num - 10)))
        dirty_rects.append(screen.blit(bottomleft, (398,588 + num + 10)))
        dirty_rects.append(screen.blit(bottomright, (458  + num + 10, 588)))

    if (s.game.anti_cheat.status == True):
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],113,166)))
    else:
        dirty_rects.append(screen.blit(bg_off, p, pygame.Rect(p[0],p[1],113,166)))

    pygame.display.update(dirty_rects)


def numberd_animation(args):
    dirty_rects = []
    s = args[0]
    num = args[1]
    number = args[2]
    
    if number == 4:
        p = [339,358]
        if s.game.numberd.position == 0:
            image = numberd5
            topleft = d_2
            topmiddle = d_3
            topright = d_4
            bottomright = d_5
            bottommiddle = d_6
            bottomleft = d_1
        elif s.game.numberd.position == 1:
            image = numberd0
            topleft = d_1
            topmiddle = d_2
            topright = d_3
            bottomright = d_4
            bottommiddle = d_5
            bottomleft = d_6
        elif s.game.numberd.position == 2:
            image = numberd1
            topleft = d_6
            topmiddle = d_1
            topright = d_2
            bottomright = d_3
            bottommiddle = d_4
            bottomleft = d_5
        elif s.game.numberd.position == 3:
            image = numberd2
            topleft = d_5
            topmiddle = d_6
            topright = d_1
            bottomright = d_2
            bottommiddle = d_3
            bottomleft = d_4
        elif s.game.numberd.position == 4:
            image = numberd3
            topleft = d_4
            topmiddle = d_5
            topright = d_6
            bottomright = d_1
            bottommiddle = d_2
            bottomleft = d_3
        elif s.game.numberd.position == 5:
            image = numberd4
            topleft = d_3
            topmiddle = d_4
            topright = d_5
            bottomright = d_6
            bottommiddle = d_1
            bottomleft = d_2

    rect = pygame.Rect(p[0],p[1],200,200)

    if number == 4: 
        dirty_rects.append(screen.blit(topleft, (337  - num, 368)))
        dirty_rects.append(screen.blit(topmiddle, (398 - num, 368)))
        dirty_rects.append(screen.blit(topright, (456, 372 - num - 15)))
        dirty_rects.append(screen.blit(bottomright, (457 + num + 10, 416)))
        dirty_rects.append(screen.blit(bottommiddle, (397 + num + 10, 416)))
        dirty_rects.append(screen.blit(bottomleft, (340, 416 + num + 15)))

    if (s.game.anti_cheat.status == True):
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],171,111)))
    else:
        dirty_rects.append(screen.blit(bg_off, p, pygame.Rect(p[0],p[1],171,111)))

    p = [286,632]
    dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],22,29)))
    dirty_rects.append(screen.blit(letter_b, p))

    pygame.display.update(dirty_rects)


def eb_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]

    if s.game.extra_ball.position < 1:
        dirty_rects.append(screen.blit(bg_gi, (143,1024), pygame.Rect(143,1024,45,30)))
    if s.game.extra_ball.position < 2:
        dirty_rects.append(screen.blit(bg_gi, (192,1025), pygame.Rect(192,1025,65,30)))
    if s.game.extra_ball.position < 3:
        dirty_rects.append(screen.blit(bg_gi, (254,1025), pygame.Rect(254,1025,65,30)))
    if s.game.extra_ball.position < 4:
        dirty_rects.append(screen.blit(bg_gi, (323,1026), pygame.Rect(323,1026,45,30)))
    if s.game.extra_ball.position < 5:
        dirty_rects.append(screen.blit(bg_gi, (371,1026), pygame.Rect(371,1026,65,30)))
    if s.game.extra_ball.position < 6:
        dirty_rects.append(screen.blit(bg_gi, (435,1026), pygame.Rect(435,1026,65,30)))
    if s.game.extra_ball.position < 7:
        dirty_rects.append(screen.blit(bg_gi, (501,1025), pygame.Rect(501,1025,45,30)))
    if s.game.extra_ball.position < 8:
        dirty_rects.append(screen.blit(bg_gi, (552,1024), pygame.Rect(552,1024,65,30)))
    if s.game.extra_ball.position < 9:
        dirty_rects.append(screen.blit(bg_gi, (615,1024), pygame.Rect(615,1024,65,30)))
    pygame.display.update(dirty_rects)

    if num in [0,25,14,49]:
        if s.game.extra_ball.position < 1:
            p = [143,1024]
            dirty_rects.append(screen.blit(eb_number, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [39,1,26,15]:
        if s.game.extra_ball.position < 2:
            p = [192,1025]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [3,4,17,28,29,40]:
        if s.game.extra_ball.position < 3:
            p = [254,1025]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [5,18,30,43]:
        if s.game.extra_ball.position < 4:
            p = [323,1026]
            dirty_rects.append(screen.blit(eb_number, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [7,8,19,32,33,44]:
        if s.game.extra_ball.position < 5:
            p = [371,1026]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [9,10,20,34,35,45]:
        if s.game.extra_ball.position < 6:
            p = [435,1026]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [11,21,36,46]:
        if s.game.extra_ball.position < 7:
            p = [501,1025]
            dirty_rects.append(screen.blit(eb_number, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [12,22,37,47]:
        if s.game.extra_ball.position < 8:
            p = [552,1024]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [2,6,13,16,23,27,31,38,41,48]:
        if s.game.extra_ball.position < 9:
            p = [615,1024]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return

def clear_odds(s, num):
    global screen

    dirty_rects = []

    if s.game.four_stars.status == False:
        dirty_rects.append(screen.blit(bg_gi, (21,367), pygame.Rect(21,367,122,57)))
    if s.game.spot_16.status == False:
        dirty_rects.append(screen.blit(bg_gi, (20,684), pygame.Rect(20,684,96,52)))
    
    if s.game.yellow_odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (327,822), pygame.Rect(327,822,47,66)))
    if s.game.yellow_odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (388,822), pygame.Rect(388,822,47,66)))
    if s.game.yellow_odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (452,822), pygame.Rect(452,822,47,66)))
    if s.game.yellow_odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (507,822), pygame.Rect(507,822,47,66)))
    if s.game.yellow_odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (556,822), pygame.Rect(556,822,47,66)))
    if s.game.yellow_odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (605,822), pygame.Rect(605,822,47,66)))
    if s.game.yellow_odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (651,822), pygame.Rect(651,822,47,66)))

    if s.game.red_odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (327,758), pygame.Rect(327,758,47,66)))
    if s.game.red_odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (388,758), pygame.Rect(388,758,47,66)))
    if s.game.red_odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (452,758), pygame.Rect(452,758,47,66)))
    if s.game.red_odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (507,758), pygame.Rect(507,758,47,66)))
    if s.game.red_odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (556,758), pygame.Rect(556,758,47,66)))
    if s.game.red_odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (605,758), pygame.Rect(605,758,47,66)))
    if s.game.red_odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (653,758), pygame.Rect(653,758,47,66)))

    if s.game.green_odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (265,890), pygame.Rect(265,890,47,66)))
    if s.game.green_odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (327,890), pygame.Rect(327,890,47,66)))
    if s.game.green_odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (388,890), pygame.Rect(388,890,47,66)))
    if s.game.green_odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (452,890), pygame.Rect(452,890,47,66)))
    if s.game.green_odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (507,890), pygame.Rect(507,890,47,66)))
    if s.game.green_odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (556,890), pygame.Rect(556,890,47,66)))
    if s.game.green_odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (605,890), pygame.Rect(605,890,47,66)))
    if s.game.green_odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (651,890), pygame.Rect(651,890,47,66)))

    pygame.display.update(dirty_rects)

def draw_odds_animation(s, num):
    global screen
    dirty_rects = []

    if num in [9,18,34,43]:
        if s.game.four_stars.status == False:
            p = [21,367]
            dirty_rects.append(screen.blit(pap, p))
            pygame.display.update(dirty_rects)
            return
    if num in [3,12,20,28,37,45]:
        if s.game.spot_16.status == False:
            p = [20,684]
            dirty_rects.append(screen.blit(spot_16, p))
            pygame.display.update(dirty_rects)
            return

    if num in [11,36]:
        if s.game.yellow_odds.position != 1:
            p = [327,822]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [4,29]:
        if s.game.yellow_odds.position != 2:
            p = [388,822]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [7,32]:
        if s.game.yellow_odds.position != 3:
            p = [452,854]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [13,38]:
        if s.game.yellow_odds.position != 4:
            p = [507,854]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [22,47]:
        if s.game.yellow_odds.position != 5:
            p = [556,854]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [17,42]:
        if s.game.yellow_odds.position != 6:
            p = [605,854]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [19,21,44,46]:
        if s.game.yellow_odds.position != 7:
            p = [651,854]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
  
    if num in [5,30]:
        if s.game.red_odds.position != 1:
            p = [327,758]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [26,0]:
        if s.game.red_odds.position != 2:
            p = [388,758]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [15,40]:
        if s.game.red_odds.position != 3:
            p = [452,758]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [24,49]:
        if s.game.red_odds.position != 4:
            p = [507,758]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [9,34]:
        if s.game.red_odds.position != 5:
            p = [556,758]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [20,45]:
        if s.game.red_odds.position != 6:
            p = [605,758]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [12,37]:
        if s.game.red_odds.position != 7:
            p = [653,758]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return

    if num in [50,25]:
        if s.game.green_odds.position != 1:
            p = [265,890]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [6,31]:
        if s.game.green_odds.position != 2:
            p = [327,890]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [16,41]:
        if s.game.green_odds.position != 3:
            p = [388,890]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [18,43]:
        if s.game.green_odds.position != 4:
            p = [452,890]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [14,39]:
        if s.game.green_odds.position != 5:
            p = [507,890]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [3,28]:
        if s.game.green_odds.position != 6:
            p = [556,890]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [48,23]:
        if s.game.green_odds.position != 7:
            p = [605,890]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [8,33]:
        if s.game.green_odds.position != 8:
            p = [651,890]
            dirty_rects.append(screen.blit(odds, p))
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

    if s.game.magic_numbers_feature.position < 4:
        dirty_rects.append(screen.blit(bg_gi, (242,686), pygame.Rect(242,686,41,53)))
        dirty_rects.append(screen.blit(bg_gi, (188,420), pygame.Rect(188,420,24,32)))
    if s.game.magic_numbers_feature.position < 6:
        dirty_rects.append(screen.blit(bg_gi, (306,686), pygame.Rect(306,686,41,53)))
        dirty_rects.append(screen.blit(bg_gi, (286,632), pygame.Rect(286,632,22,29)))
    if s.game.magic_numbers_feature.position < 8:
        dirty_rects.append(screen.blit(bg_gi, (370,686), pygame.Rect(370,686,41,53)))
        dirty_rects.append(screen.blit(bg_gi, (504,535), pygame.Rect(504,535,21,30)))
    if s.game.magic_numbers_feature.position < 10:
        dirty_rects.append(screen.blit(bg_gi, (434,686), pygame.Rect(434,686,41,53)))
        dirty_rects.append(screen.blit(bg_gi, (407,323), pygame.Rect(407,323,22,28)))
    if s.game.yellow_star.status == False:
        dirty_rects.append(screen.blit(bg_gi, (23,954), pygame.Rect(23,954,55,54)))
    if s.game.red_star.status == False:
        dirty_rects.append(screen.blit(bg_gi, (635,956), pygame.Rect(635,956,55,54)))
    if s.game.before_fifth.status == False:
        dirty_rects.append(screen.blit(bg_gi, (574,444), pygame.Rect(574,444,120,57)))
    if s.game.after_fifth.status == False:
        dirty_rects.append(screen.blit(bg_gi, (574,366), pygame.Rect(574,366,120,57)))
    

    pygame.display.update(dirty_rects)


def draw_feature_animation(s, num):
    global screen
    dirty_rects = []
 
    if num in [4,13,21,29,38,46]:
        if s.game.magic_numbers_feature.position < 4:
            p = [242,686]
            dirty_rects.append(screen.blit(letter, p))
            p = [188,420]
            dirty_rects.append(screen.blit(letter_a, p))
            pygame.display.update(dirty_rects)
            return
    if num in [5,14,22,30,39,47]:
        if s.game.magic_numbers_feature.position < 6:
            p = [306,686]
            dirty_rects.append(screen.blit(letter, p))
            p = [286,632]
            dirty_rects.append(screen.blit(letter_b, p))
            pygame.display.update(dirty_rects)
            return
    if num in [6,15,23,31,40,48]:
        if s.game.magic_numbers_feature.position < 8:
            p = [370,686]
            dirty_rects.append(screen.blit(letter, p))
            p = [504,535]
            dirty_rects.append(screen.blit(letter_c, p))
            pygame.display.update(dirty_rects)
            return
    if num in [7,16,24,0,32,41]:
        if s.game.magic_numbers_feature.position < 10:
            p = [434,686]
            dirty_rects.append(screen.blit(letter, p))
            p = [407,323]
            dirty_rects.append(screen.blit(letter_d, p))
            pygame.display.update(dirty_rects)
            return
    if num in [8,19,33,44]:
        if s.game.yellow_star.status == False:
            p = [23,954]
            dirty_rects.append(screen.blit(star, p))
            s.game.coils.yellowROLamp.pulse(85)
            pygame.display.update(dirty_rects)
            return
    if num in [1,11,26,36]:
        if s.game.red_star.status == False:
            p = [635,956]
            dirty_rects.append(screen.blit(star, p))
            s.game.coils.redROLamp.pulse(85)
            pygame.display.update(dirty_rects)
            return
    if num in [10,35]:
        if s.game.before_fifth.status == False:
            p = [574,444]
            dirty_rects.append(screen.blit(time, p))
            pygame.display.update(dirty_rects)
            return
    if num in [2,17,27,42]:
        if s.game.after_fifth.status == False:
            p = [574,366]
            dirty_rects.append(screen.blit(time, p))
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

  
