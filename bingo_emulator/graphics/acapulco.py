
import pygame
import random

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

meter = pygame.image.load('graphics/assets/black_register_cover.png').convert()
eb = pygame.image.load('acapulco/assets/eb.png').convert_alpha()
eb_number = pygame.image.load('acapulco/assets/eb_number.png').convert_alpha()
extra_balls = pygame.image.load('acapulco/assets/extra_balls.png').convert_alpha()
odds = pygame.image.load('acapulco/assets/odds.png').convert_alpha()
number = pygame.image.load('acapulco/assets/number.png').convert_alpha()
tilt = pygame.image.load('acapulco/assets/tilt.png').convert_alpha()
time = pygame.image.load('acapulco/assets/time.png').convert_alpha()
mn_arrow = pygame.image.load('acapulco/assets/mn_arrow.png').convert_alpha()
sf_arrow = pygame.image.load('acapulco/assets/sf_arrow.png').convert_alpha()
ss_arrow = pygame.image.load('acapulco/assets/ss_arrow.png').convert_alpha()
ss_select = pygame.image.load('acapulco/assets/ss_select.png').convert_alpha()
pap = pygame.image.load('acapulco/assets/pap.png').convert_alpha()
ss = pygame.image.load('acapulco/assets/ss.png').convert_alpha()
letter_a = pygame.image.load('acapulco/assets/letter_a.png').convert_alpha()
letter_b = pygame.image.load('acapulco/assets/letter_b.png').convert_alpha()
letter_c = pygame.image.load('acapulco/assets/letter_c.png').convert_alpha()
letter_d = pygame.image.load('acapulco/assets/letter_d.png').convert_alpha()
letter = pygame.image.load('acapulco/assets/letter.png').convert_alpha()
select_now = pygame.image.load('acapulco/assets/select_now.png').convert_alpha()

numbera0 = pygame.image.load('acapulco/assets/numbera0.png').convert()
numbera1 = pygame.image.load('acapulco/assets/numbera1.png').convert()
numbera2 = pygame.image.load('acapulco/assets/numbera2.png').convert()
numbera3 = pygame.image.load('acapulco/assets/numbera3.png').convert()
numbera4 = pygame.image.load('acapulco/assets/numbera4.png').convert()
numbera5 = pygame.image.load('acapulco/assets/numbera5.png').convert()
numberb0 = pygame.image.load('acapulco/assets/numberb0.png').convert()
numberb1 = pygame.image.load('acapulco/assets/numberb1.png').convert()
numberb2 = pygame.image.load('acapulco/assets/numberb2.png').convert()
numberb3 = pygame.image.load('acapulco/assets/numberb3.png').convert()
numberb4 = pygame.image.load('acapulco/assets/numberb4.png').convert()
numberb5 = pygame.image.load('acapulco/assets/numberb5.png').convert()
numberc0 = pygame.image.load('acapulco/assets/numberc0.png').convert()
numberc1 = pygame.image.load('acapulco/assets/numberc1.png').convert()
numberc2 = pygame.image.load('acapulco/assets/numberc2.png').convert()
numberc3 = pygame.image.load('acapulco/assets/numberc3.png').convert()
numberc4 = pygame.image.load('acapulco/assets/numberc4.png').convert()
numberc5 = pygame.image.load('acapulco/assets/numberc5.png').convert()
numberd0 = pygame.image.load('acapulco/assets/numberd0.png').convert()
numberd1 = pygame.image.load('acapulco/assets/numberd1.png').convert()
numberd2 = pygame.image.load('acapulco/assets/numberd2.png').convert()
numberd3 = pygame.image.load('acapulco/assets/numberd3.png').convert()
numberd4 = pygame.image.load('acapulco/assets/numberd4.png').convert()
numberd5 = pygame.image.load('acapulco/assets/numberd5.png').convert()
number16 = pygame.image.load('acapulco/assets/number16.png').convert()

bg_menu = pygame.image.load('acapulco/assets/acapulco_menu.png')
bg_gi = pygame.image.load('acapulco/assets/acapulco_gi.png')
bg_off = pygame.image.load('acapulco/assets/acapulco_off.png')
a_1 = pygame.image.load('acapulco/assets/a-1.png').convert_alpha()
a_2 = pygame.image.load('acapulco/assets/a-2.png').convert_alpha()
a_3 = pygame.image.load('acapulco/assets/a-3.png').convert_alpha()
a_4 = pygame.image.load('acapulco/assets/a-4.png').convert_alpha()
a_5 = pygame.image.load('acapulco/assets/a-5.png').convert_alpha()
a_6 = pygame.image.load('acapulco/assets/a-6.png').convert_alpha()
b_1 = pygame.image.load('acapulco/assets/b-1.png').convert_alpha()
b_2 = pygame.image.load('acapulco/assets/b-2.png').convert_alpha()
b_3 = pygame.image.load('acapulco/assets/b-3.png').convert_alpha()
b_4 = pygame.image.load('acapulco/assets/b-4.png').convert_alpha()
b_5 = pygame.image.load('acapulco/assets/b-5.png').convert_alpha()
b_6 = pygame.image.load('acapulco/assets/b-6.png').convert_alpha()
c_1 = pygame.image.load('acapulco/assets/c-1.png').convert_alpha()
c_2 = pygame.image.load('acapulco/assets/c-2.png').convert_alpha()
c_3 = pygame.image.load('acapulco/assets/c-3.png').convert_alpha()
c_4 = pygame.image.load('acapulco/assets/c-4.png').convert_alpha()
c_5 = pygame.image.load('acapulco/assets/c-5.png').convert_alpha()
c_6 = pygame.image.load('acapulco/assets/c-6.png').convert_alpha()
d_1 = pygame.image.load('acapulco/assets/d-1.png').convert_alpha()
d_2 = pygame.image.load('acapulco/assets/d-2.png').convert_alpha()
d_3 = pygame.image.load('acapulco/assets/d-3.png').convert_alpha()
d_4 = pygame.image.load('acapulco/assets/d-4.png').convert_alpha()
d_5 = pygame.image.load('acapulco/assets/d-5.png').convert_alpha()
d_6 = pygame.image.load('acapulco/assets/d-6.png').convert_alpha()


class scorereel():
    """ Score Reels are used to count replays """
    def __init__(self, pos, image):
        self.position = pos
        self.default_y = self.position[1]
        self.image = pygame.image.load(image).convert()

reel1 = scorereel([122,793], "graphics/assets/white_reel.png")
reel10 = scorereel([103,793], "graphics/assets/white_reel.png")
reel100 = scorereel([83,793], "graphics/assets/white_reel.png")
reel1000 = scorereel([65,793], "graphics/assets/white_reel.png")

def display(s, replays=0, menu=False):
    
    meter.set_colorkey((255,0,252))
    meter_position = [55,793]

    screen.blit(reel1.image, reel1.position)
    screen.blit(reel10.image, reel10.position)
    screen.blit(reel100.image, reel100.position)
    screen.blit(reel1000.image, reel1000.position)
    screen.blit(meter, meter_position)

    if s.game.numbera.position == 0:
        p = [225,357]
        screen.blit(numbera0, p)
    elif s.game.numbera.position == 1:
        p = [225,357]
        screen.blit(numbera1, p)
    elif s.game.numbera.position == 2:
        p = [225,357]
        screen.blit(numbera2, p)
    elif s.game.numbera.position == 3:
        p = [225,357]
        screen.blit(numbera3, p)
    elif s.game.numbera.position == 4:
        p = [225,357]
        screen.blit(numbera4, p)
    elif s.game.numbera.position == 5:
        p = [225,357]
        screen.blit(numbera5, p)

    if s.game.numberb.position == 0:
        p = [225,528]
        screen.blit(numberb0, p)
    elif s.game.numberb.position == 1:
        p = [225,528]
        screen.blit(numberb1, p)
    elif s.game.numberb.position == 2:
        p = [225,528]
        screen.blit(numberb2, p)
    elif s.game.numberb.position == 3:
        p = [225,528]
        screen.blit(numberb3, p)
    elif s.game.numberb.position == 4:
        p = [225,528]
        screen.blit(numberb4, p)
    elif s.game.numberb.position == 5:
        p = [225,528]
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

    p = [342,474]
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
        eb_position = [151,1028]
        screen.blit(eb_number, eb_position)
    if s.game.extra_ball.position >= 2:
        eb_position = [199,1028]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 3:
        eb_position = [262,1028]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 4:
        eb_position = [328,1028]
        screen.blit(eb_number, eb_position)
    if s.game.extra_ball.position >= 5:
        eb_position = [377,1028]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 6:
        eb_position = [439,1028]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 7:
        eb_position = [505,1028]
        screen.blit(eb_number, eb_position)
    if s.game.extra_ball.position >= 8:
        eb_position = [554,1028]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 9:
        eb_position = [617,1028]
        screen.blit(eb, eb_position)

    if s.game.start.status == True:
        if s.game.all_advantages.status == True:
            p = [37,973]
            screen.blit(pap, p)
        if s.game.odds_only.status == True:
            p = [37,873]
            screen.blit(pap, p)
        if s.game.features.status == True:
            p = [37,923]
            screen.blit(pap, p)

    if s.game.red_odds.position == 1:
        p = [313,779]
        screen.blit(odds, p)
    elif s.game.red_odds.position == 2:
        p = [353,779]
        screen.blit(odds, p)
    elif s.game.red_odds.position == 3:
        p = [393,779]
        screen.blit(odds, p)
    elif s.game.red_odds.position == 4:
        p = [434,779]
        screen.blit(odds, p)
    elif s.game.red_odds.position == 5:
        p = [473,779]
        screen.blit(odds, p)
    elif s.game.red_odds.position == 6:
        p = [513,779]
        screen.blit(odds, p)
    elif s.game.red_odds.position == 7:
        p = [553,779]
        screen.blit(odds, p)
    elif s.game.red_odds.position == 8:
        p = [593,779]
        screen.blit(odds, p)

    if s.game.yellow_odds.position == 1:
        p = [313,854]
        screen.blit(odds, p)
    elif s.game.yellow_odds.position == 2:
        p = [353,854]
        screen.blit(odds, p)
    elif s.game.yellow_odds.position == 3:
        p = [393,854]
        screen.blit(odds, p)
    elif s.game.yellow_odds.position == 4:
        p = [434,854]
        screen.blit(odds, p)
    elif s.game.yellow_odds.position == 5:
        p = [473,854]
        screen.blit(odds, p)
    elif s.game.yellow_odds.position == 6:
        p = [513,854]
        screen.blit(odds, p)
    elif s.game.yellow_odds.position == 7:
        p = [553,854]
        screen.blit(odds, p)
    elif s.game.yellow_odds.position == 8:
        p = [593,854]
        screen.blit(odds, p)


    if s.game.green_odds.position == 1:
        p = [313,931]
        screen.blit(odds, p)
    elif s.game.green_odds.position == 2:
        p = [353,931]
        screen.blit(odds, p)
    elif s.game.green_odds.position == 3:
        p = [393,931]
        screen.blit(odds, p)
    elif s.game.green_odds.position == 4:
        p = [434,931]
        screen.blit(odds, p)
    elif s.game.green_odds.position == 5:
        p = [473,931]
        screen.blit(odds, p)
    elif s.game.green_odds.position == 6:
        p = [513,931]
        screen.blit(odds, p)
    elif s.game.green_odds.position == 7:
        p = [553,931]
        screen.blit(odds, p)
    elif s.game.green_odds.position == 8:
        p = [593,931]
        screen.blit(odds, p)

    a1 = [228,357]
    a2 = [285,357]
    a3 = [228,413]
    a4 = [285,413]
    a5 = [228,472]
    a6 = [285,472]

    b1 = [228,529]
    b2 = [285,529]
    b3 = [343,529]
    b4 = [228,587]
    b5 = [285,587]
    b6 = [343,587]

    c1 = [399,472]
    c2 = [456,472]
    c3 = [399,529]
    c4 = [456,529]
    c5 = [399,585]
    c6 = [456,585]

    d1 = [342,357]
    d2 = [399,357]
    d3 = [455,357]
    d4 = [342,414]
    d5 = [399,414]
    d6 = [455,414]

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
                p = [343,472]
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
        p = [184,689]
        screen.blit(mn_arrow, p)
    elif s.game.magic_numbers_feature.position == 2:
        p = [221,689]
        screen.blit(mn_arrow, p)
    elif s.game.magic_numbers_feature.position == 3:
        p = [259,689]
        screen.blit(mn_arrow, p)
    if s.game.magic_numbers_feature.position >= 4:
        p = [303,679]
        screen.blit(letter,p)
        p = [263,316]
        screen.blit(letter_a, p)
    if s.game.magic_numbers_feature.position >= 6:
        p = [363,679]
        screen.blit(letter, p)
        p = [293,627]
        screen.blit(letter_b, p)
    if s.game.magic_numbers_feature.position >= 8:
        p = [427,679]
        screen.blit(letter, p)
        p = [433,627]
        screen.blit(letter_c, p)
    if s.game.magic_numbers_feature.position == 10:
        p = [487,679]
        screen.blit(letter, p)
        p = [408,318]
        screen.blit(letter_d, p)


    if s.game.selection_feature.position == 1:
        p = [681,611]
        screen.blit(sf_arrow, p)
    elif s.game.selection_feature.position == 2:
        p = [681,585] 
        screen.blit(sf_arrow, p)
    elif s.game.selection_feature.position == 3:
        p = [681,555]
        screen.blit(sf_arrow, p)
    elif s.game.selection_feature.position == 4:
        p = [681,525]
        screen.blit(sf_arrow, p)
    elif s.game.selection_feature.position == 5:
        p = [681,495]
        screen.blit(sf_arrow, p)
    elif s.game.selection_feature.position == 6:
        p = [681,467]
        screen.blit(sf_arrow, p)
    elif s.game.selection_feature.position == 7:
        p = [681,437]
        screen.blit(sf_arrow, p)
    elif s.game.selection_feature.position == 8:
        p = [681,409]
        screen.blit(sf_arrow, p)
    elif s.game.selection_feature.position == 9:
        p = [681,380]
        screen.blit(sf_arrow, p)

    if s.game.four_stars.status == True:
        p = [57,585]
        screen.blit(ss, p)

    if s.game.hole_feature.status == True:
        p = [57,493]
        screen.blit(ss, p)

    if s.game.super_line_feature.status == True:
        p = [57,398]
        screen.blit(ss, p)
        if s.game.ball_count.position == 3:
            s.cancel_delayed(name="blink")
            blink([s,1,1,0])
        else:
            s.cancel_delayed(name="blink")
        if s.game.super_line_select.position == 0:
            p = [179,364]
            screen.blit(ss_arrow, p)
        elif s.game.super_line_select.position == 1:
            p = [179,421]
            screen.blit(ss_arrow, p)
        elif s.game.super_line_select.position == 2:
            p = [179,477]
            screen.blit(ss_arrow, p)
        elif s.game.super_line_select.position == 3:
            p = [179,536]
            screen.blit(ss_arrow, p)
        elif s.game.super_line_select.position == 4:
            p = [179,593]
            screen.blit(ss_arrow, p)

    if s.game.magic_numbers_feature.position > 3:
        if s.game.before_fourth.status == True:
            p = [551,597]
            screen.blit(time, p)
            if s.game.ball_count.position == 3:
                s.cancel_delayed(name="blink")
                blink([s,1,0,1])
            else:
                s.cancel_delayed(name="blink")
        if s.game.yellow_star.status == True:
            p = [551,539]
            screen.blit(time, p)
        if s.game.red_star.status == True:
            p = [551,480]
            screen.blit(time, p)
        if s.game.before_fifth.status == True:
            p = [551,422]
            screen.blit(time, p)
            if s.game.ball_count.position == 4:
                s.cancel_delayed(name="blink")
                blink([s,1,0,1])
            else:
                if s.game.ball_count.position > 4:
                    s.cancel_delayed(name="blink")
        elif s.game.after_fifth.status == True:
            p = [551,364]
            screen.blit(time, p)
            if s.game.ball_count.position == 5:
                s.cancel_delayed(name="blink")
                blink([s,1,0,1])
            else:
                if s.game.ball_count.position > 5:
                    s.cancel_delayed(name="blink")

    if s.game.tilt.status == True:
        tilt_position = [585,306]
        screen.blit(tilt, tilt_position)
               
    if s.game.eb_play.status == True:
        p = [41,1028]
        screen.blit(extra_balls, p)

    pygame.display.update()

def blink(args):
    dirty_rects = []
    s = args[0]
    b = args[1]
    sl = args[2]
    sn = args[3]

    if b == 0:
        if sl == 1:
            p = [55,367]
            dirty_rects.append(screen.blit(ss_select, p))
        if sn == 1:
            p = [554,680]
            dirty_rects.append(screen.blit(select_now, p))
        pygame.display.update(dirty_rects)
    else:
        dirty_rects.append(screen.blit(bg_gi, (55,367), pygame.Rect(55,367,117,30)))
        dirty_rects.append(screen.blit(bg_gi, (554,680), pygame.Rect(554,680,133,53)))
        pygame.display.update(dirty_rects)
    b = not b

    args = [s,b,sl,sn]

    s.delay(name="blink", delay=0.1, handler=blink, param=args)

def numbera_animation(args):
    dirty_rects = []
    s = args[0]
    num = args[1]
    number = args[2]
    
    if number == 1:
        p = [225,357]
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
        dirty_rects.append(screen.blit(topleft, (230  - num, 365)))
        dirty_rects.append(screen.blit(topright, (288, 360 - num - 2)))
        dirty_rects.append(screen.blit(middleleft, (230, 417 + num + 10)))
        dirty_rects.append(screen.blit(middleright, (286, 416 - num - 10)))
        dirty_rects.append(screen.blit(bottomleft, (230, 474 + num + 10)))
        dirty_rects.append(screen.blit(bottomright, (286  + num + 10, 474)))

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
        p = [225,528]
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
        dirty_rects.append(screen.blit(topleft, (223  - num, 537)))
        dirty_rects.append(screen.blit(topmiddle, (282 - num, 537)))
        dirty_rects.append(screen.blit(topright, (340, 543 - num - 15)))
        dirty_rects.append(screen.blit(bottomright, (343 + num + 10, 582)))
        dirty_rects.append(screen.blit(bottommiddle, (283 + num + 10, 582)))
        dirty_rects.append(screen.blit(bottomleft, (229, 582 + num + 15)))

    if (s.game.anti_cheat.status == True):
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],171,111)))
    else:
        dirty_rects.append(screen.blit(bg_off, p, pygame.Rect(p[0],p[1],171,111)))

    p = [293,627]
    dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],25,37)))
    dirty_rects.append(screen.blit(letter_b, p))

    pygame.display.update(dirty_rects)


def numberc_animation(args):
    dirty_rects = []
    s = args[0]
    num = args[1]
    number = args[2]
    
    p = [393,470]
    if number == 3:
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

    p = [433,627]
    dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],25,37)))
    dirty_rects.append(screen.blit(letter_c, p))
    
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

    pygame.display.update(dirty_rects)


def eb_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]

    if s.game.extra_ball.position < 1:
        dirty_rects.append(screen.blit(bg_gi, (151,1028), pygame.Rect(151,1028,48,32)))
    if s.game.extra_ball.position < 2:
        dirty_rects.append(screen.blit(bg_gi, (199,1028), pygame.Rect(199,1028,66,32)))
    if s.game.extra_ball.position < 3:
        dirty_rects.append(screen.blit(bg_gi, (262,1028), pygame.Rect(262,1028,66,32)))
    if s.game.extra_ball.position < 4:
        dirty_rects.append(screen.blit(bg_gi, (328,1028), pygame.Rect(328,1028,48,32)))
    if s.game.extra_ball.position < 5:
        dirty_rects.append(screen.blit(bg_gi, (377,1028), pygame.Rect(377,1028,66,32)))
    if s.game.extra_ball.position < 6:
        dirty_rects.append(screen.blit(bg_gi, (439,1028), pygame.Rect(439,1028,66,32)))
    if s.game.extra_ball.position < 7:
        dirty_rects.append(screen.blit(bg_gi, (505,1028), pygame.Rect(505,1028,48,32)))
    if s.game.extra_ball.position < 8:
        dirty_rects.append(screen.blit(bg_gi, (554,1028), pygame.Rect(554,1028,66,32)))
    if s.game.extra_ball.position < 9:
        dirty_rects.append(screen.blit(bg_gi, (617,1028), pygame.Rect(617,1028,66,32)))
    pygame.display.update(dirty_rects)

    if num in [0,25,14,49]:
        if s.game.extra_ball.position < 1:
            p = [151,1028]
            dirty_rects.append(screen.blit(eb_number, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [39,1,26,15]:
        if s.game.extra_ball.position < 2:
            p = [199,1028]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [3,4,17,28,29,40]:
        if s.game.extra_ball.position < 3:
            p = [262,1028]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [5,18,30,43]:
        if s.game.extra_ball.position < 4:
            p = [328,1028]
            dirty_rects.append(screen.blit(eb_number, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [7,8,19,32,33,44]:
        if s.game.extra_ball.position < 5:
            p = [377,1028]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [9,10,20,34,35,45]:
        if s.game.extra_ball.position < 6:
            p = [439,1028]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [11,21,36,46]:
        if s.game.extra_ball.position < 7:
            p = [505,1028]
            dirty_rects.append(screen.blit(eb_number, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [12,22,37,47]:
        if s.game.extra_ball.position < 8:
            p = [554,1028]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [2,6,13,16,23,27,31,38,41,48]:
        if s.game.extra_ball.position < 9:
            p = [617,1028]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return

def clear_odds(s, num):
    global screen

    dirty_rects = []

    if s.game.four_stars.status == False:
        dirty_rects.append(screen.blit(bg_gi, (57,585), pygame.Rect(57,585,117,70)))
    if s.game.hole_feature.status == False:
        dirty_rects.append(screen.blit(bg_gi, (57,493), pygame.Rect(57,493,117,70)))
    if s.game.super_line_feature.status == False:
        dirty_rects.append(screen.blit(bg_gi, (57,398), pygame.Rect(57,398,117,70)))
    
    if s.game.yellow_odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (353,854), pygame.Rect(353,854,46,71)))
    if s.game.yellow_odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (393,854), pygame.Rect(393,854,46,71)))
    if s.game.yellow_odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (434,854), pygame.Rect(434,854,46,71)))
    if s.game.yellow_odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (473,854), pygame.Rect(473,854,46,71)))
    if s.game.yellow_odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (513,854), pygame.Rect(513,854,46,71)))
    if s.game.yellow_odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (553,854), pygame.Rect(553,854,46,71)))
    if s.game.yellow_odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (593,854), pygame.Rect(593,854,46,71)))

    if s.game.red_odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (353,779), pygame.Rect(353,779,46,71)))
    if s.game.red_odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (393,779), pygame.Rect(393,779,46,71)))
    if s.game.red_odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (434,779), pygame.Rect(434,779,46,71)))
    if s.game.red_odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (473,779), pygame.Rect(473,779,46,71)))
    if s.game.red_odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (513,779), pygame.Rect(513,779,46,71)))
    if s.game.red_odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (553,779), pygame.Rect(553,779,46,71)))
    if s.game.red_odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (593,779), pygame.Rect(593,779,46,71)))

    if s.game.green_odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (353,931), pygame.Rect(353,931,46,71)))
    if s.game.green_odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (393,931), pygame.Rect(393,931,46,71)))
    if s.game.green_odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (434,931), pygame.Rect(434,931,46,71)))
    if s.game.green_odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (473,931), pygame.Rect(473,931,46,71)))
    if s.game.green_odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (513,931), pygame.Rect(513,931,46,71)))
    if s.game.green_odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (553,931), pygame.Rect(553,931,46,71)))
    if s.game.green_odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (593,931), pygame.Rect(593,931,46,71)))

    pygame.display.update(dirty_rects)

def draw_odds_animation(s, num):
    global screen
    dirty_rects = []

    if num in [8,33]:
        if s.game.four_stars.status == False:
            p = [57,585]
            dirty_rects.append(screen.blit(ss, p))
            pygame.display.update(dirty_rects)
            return
    if num in [21,46]:
        if s.game.hole_feature.status == False:
            p = [57,493]
            dirty_rects.append(screen.blit(ss, p))
            pygame.display.update(dirty_rects)
            return
    if num in [10,35]:
        if s.game.super_line_feature.status == False:
            p = [57,398]
            dirty_rects.append(screen.blit(ss, p))
            pygame.display.update(dirty_rects)
            return
    if num in [11,36]:
        if s.game.yellow_odds.position != 2:
            p = [353,854]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [4,29]:
        if s.game.yellow_odds.position != 3:
            p = [393,854]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [7,32]:
        if s.game.yellow_odds.position != 4:
            p = [434,854]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [13,38]:
        if s.game.yellow_odds.position != 5:
            p = [473,854]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [22,47]:
        if s.game.yellow_odds.position != 6:
            p = [513,854]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [17,42]:
        if s.game.yellow_odds.position != 7:
            p = [553,854]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [19,44]:
        if s.game.yellow_odds.position != 8:
            p = [553,854]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    
    if num in [5,30]:
        if s.game.red_odds.position != 2:
            p = [353,779]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [26,0]:
        if s.game.red_odds.position != 3:
            p = [393,779]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [15,40]:
        if s.game.red_odds.position != 4:
            p = [434,779]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [24,49]:
        if s.game.red_odds.position != 5:
            p = [473,779]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [9,34]:
        if s.game.red_odds.position != 6:
            p = [513,779]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [20,45]:
        if s.game.red_odds.position != 7:
            p = [553,779]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [12,37]:
        if s.game.red_odds.position != 8:
            p = [553,779]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return

    if num in [50,25]:
        if s.game.green_odds.position != 2:
            p = [353,931]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [6,31]:
        if s.game.green_odds.position != 3:
            p = [393,931]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [16,41]:
        if s.game.green_odds.position != 4:
            p = [434,931]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [18,43]:
        if s.game.green_odds.position != 5:
            p = [473,931]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [14,39]:
        if s.game.green_odds.position != 6:
            p = [513,931]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [3,28]:
        if s.game.green_odds.position != 7:
            p = [553,931]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [48,23]:
        if s.game.green_odds.position != 8:
            p = [553,931]
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
        dirty_rects.append(screen.blit(bg_gi, (303,679), pygame.Rect(303,679,57,52)))
    if s.game.magic_numbers_feature.position < 6:
        dirty_rects.append(screen.blit(bg_gi, (363,679), pygame.Rect(363,679,57,52)))
    if s.game.magic_numbers_feature.position < 8:
        dirty_rects.append(screen.blit(bg_gi, (427,679), pygame.Rect(427,679,57,52)))
    if s.game.magic_numbers_feature.position < 10:
        dirty_rects.append(screen.blit(bg_gi, (487,679), pygame.Rect(487,679,57,52)))
    if s.game.yellow_star.status == False:
        dirty_rects.append(screen.blit(bg_gi, (551,539), pygame.Rect(551,539,117,59)))
    if s.game.red_star.status == False:
        dirty_rects.append(screen.blit(bg_gi, (551,480), pygame.Rect(551,480,117,59)))
    if s.game.before_fifth.status == False:
        dirty_rects.append(screen.blit(bg_gi, (551,422), pygame.Rect(551,422,117,59)))
    if s.game.after_fifth.status == False:
        dirty_rects.append(screen.blit(bg_gi, (551,364), pygame.Rect(551,364,117,59)))
    

    pygame.display.update(dirty_rects)


def draw_feature_animation(s, num):
    global screen
    dirty_rects = []
    
    if num in [3,11,19,28,36,44]:
        if s.game.magic_numbers_feature.position < 4:
            p = [303,679]
            dirty_rects.append(screen.blit(letter, p))
            pygame.display.update(dirty_rects)
            return
    if num in [5,13,21,30,38,46]:
        if s.game.magic_numbers_feature.position < 6:
            p = [363,679]
            dirty_rects.append(screen.blit(letter, p))
            pygame.display.update(dirty_rects)
            return
    if num in [7,15,23,32,40,48]:
        if s.game.magic_numbers_feature.position < 8:
            p = [427,679]
            dirty_rects.append(screen.blit(letter, p))
            pygame.display.update(dirty_rects)
            return
    if num in [9,17,25,34,42,50]:
        if s.game.magic_numbers_feature.position < 10:
            p = [487,679]
            dirty_rects.append(screen.blit(letter, p))
            pygame.display.update(dirty_rects)
            return
    if num in [4,12,20,29,37,45]:
        if s.game.yellow_star.status == False:
            p = [551,539]
            dirty_rects.append(screen.blit(time, p))
            s.game.coils.yellowROLamp.pulse(85)
            pygame.display.update(dirty_rects)
            return
    if num in [6,14,22,31,39,47]:
        if s.game.red_star.status == False:
            p = [551,480]
            dirty_rects.append(screen.blit(time, p))
            s.game.coils.redROLamp.pulse(85)
            pygame.display.update(dirty_rects)
            return
    if num in [8,16,24,33,41]:
        if s.game.before_fifth.status == False:
            p = [551,422]
            dirty_rects.append(screen.blit(time, p))
            pygame.display.update(dirty_rects)
            return
    if num in [10,18,0,35,33,25]:
        if s.game.after_fifth.status == False:
            p = [551,364]
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

  
