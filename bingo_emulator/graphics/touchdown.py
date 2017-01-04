
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
        backglass = pygame.image.load('touchdown/assets/touchdown_menu.png')
    else:
        if (s.game.anti_cheat.status == True):
            backglass = pygame.image.load('touchdown/assets/touchdown_gi.png')
        else:
            backglass = pygame.image.load('touchdown/assets/touchdown_off.png')
    backglass = pygame.transform.scale(backglass, (720, 1280))
    
    screen.blit(backglass, backglass_position)


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
                p = [576,600]
                screen.blit(time, p)
        elif s.game.before_fifth.status == True:
            p = [574,444]
            screen.blit(time, p)
            if s.game.ball_count.position == 4:
                p = [576,600]
                screen.blit(time, p)
        elif s.game.after_fifth.status == True:
            p = [574,366]
            screen.blit(time, p)
            if s.game.ball_count.position == 5:
                p = [576,600]
                screen.blit(time, p)
            if s.game.tilt.status == True:
                tilt_position = [34,750]
                screen.blit(tilt, tilt_position)
               
    if s.game.eb_play.status == True:
        p = [34,1022]
        screen.blit(extra_balls, p)

    pygame.display.update()

def eb_animation(num):
    global screen

    if num == 9:
        eb_position = [143,1024]
        screen.blit(eb_number, eb_position)
        pygame.display.update()
    if num == 8:
        eb_position = [192,1025]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 7:
        eb_position = [254,1025]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 6:
        eb_position = [323,1026]
        screen.blit(eb_number, eb_position)
        pygame.display.update()
    if num == 5:
        eb_position = [371,1026]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 4:
        eb_position = [435,1026]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 3:
        eb_position = [501,1025]
        screen.blit(eb_number, eb_position)
        pygame.display.update()
    if num == 2:
        eb_position = [552,1024]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 1:
        eb_position = [615,1024]
        screen.blit(eb, eb_position)
        pygame.display.update()


def feature_animation(num):
    global screen
    if num == 6:
        p = [21,367]
        screen.blit(pap, p)
        pygame.display.update()

    if num == 5:
        rs_position = [635,956]
        screen.blit(star, rs_position)
        pygame.display.update()

    if num == 4:
        ys_position = [23,954]
        screen.blit(star, ys_position)
        pygame.display.update()

    if num == 3:
        p = [370,686]
        screen.blit(letter, p)
        pygame.display.update()
    
    if num == 2:
        p = [434,686]
        screen.blit(letter, p)
        pygame.display.update()
   
    if num == 1:
        p = [574,366]
        screen.blit(time, p)
        pygame.display.update()

def odds_animation(num):
    global screen
    if num == 5:
        p = [556,890]
        screen.blit(odds, p)
        pygame.display.update()
    if num == 4:
        p = [452,822]
        screen.blit(odds, p)
        pygame.display.update()
    if num == 3:
        p = [653,758]
        screen.blit(odds, p)
        pygame.display.update()
    if num == 2:
        p = [651,890]
        screen.blit(odds, p)
        pygame.display.update()
    if num == 1:
        p = [556,822]
        screen.blit(odds, p)
        pygame.display.update()
