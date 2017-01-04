
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
        backglass = pygame.image.load('acapulco/assets/acapulco_menu.png')
    else:
        if (s.game.anti_cheat.status == True):
            backglass = pygame.image.load('acapulco/assets/acapulco_gi.png')
        else:
            backglass = pygame.image.load('acapulco/assets/acapulco_off.png')
    backglass = pygame.transform.scale(backglass, (720, 1280))
    
    screen.blit(backglass, backglass_position)


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

    if s.game.magic_numbers_feature.position > 3:
        if s.game.before_fourth.status == True:
            p = [551,597]
            screen.blit(time, p)
            if s.game.ball_count.position == 3:
                p = [557,682]
                screen.blit(select_now, p)
        if s.game.yellow_star.status == True:
            p = [551,539]
            screen.blit(time, p)
        if s.game.red_star.status == True:
            p = [551,480]
            screen.blit(time, p)
        elif s.game.before_fifth.status == True:
            p = [551,422]
            screen.blit(time, p)
            if s.game.ball_count.position == 4:
                p = [557,682]
                screen.blit(select_now, p)
        elif s.game.after_fifth.status == True:
            p = [551,364]
            screen.blit(time, p)
            if s.game.ball_count.position == 5:
                p = [557,681]
                screen.blit(select_now, p)

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
            p = [55,367]
            screen.blit(ss_select, p)
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


    if s.game.tilt.status == True:
        tilt_position = [585,306]
        screen.blit(tilt, tilt_position)
               
    if s.game.eb_play.status == True:
        p = [41,1028]
        screen.blit(extra_balls, p)

    pygame.display.update()

def eb_animation(num):
    global screen
    if num == 9:
        eb_position = [151,1028]
        screen.blit(eb_number, eb_position)
        pygame.display.update()
    if num == 8:
        eb_position = [199,1028]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 7:
        eb_position = [262,1028]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 6:
        eb_position = [328,1028]
        screen.blit(eb_number, eb_position)
        pygame.display.update()
    if num == 5:
        eb_position = [377,1028]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 4:
        eb_position = [439,1028]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 3:
        eb_position = [505,1028]
        screen.blit(eb_number, eb_position)
        pygame.display.update()
    if num == 2:
        eb_position = [554,1028]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 1:
        eb_position = [617,1028]
        screen.blit(eb, eb_position)
        pygame.display.update()


def feature_animation(num):
    global screen
    if num == 6:
        p = [37,923]
        screen.blit(pap, p)
        pygame.display.update()

    if num == 3:
        p = [487,679]
        screen.blit(letter, p)
        pygame.display.update()
    
    if num == 2:
        p = [363,679]
        screen.blit(letter, p)
        pygame.display.update()
   
    if num == 1:
        p = [551,364]
        screen.blit(time, p)
        pygame.display.update()

def odds_animation(num):
    global screen
    if num == 5:
        p = [553,931]
        screen.blit(odds, p)
        pygame.display.update()
    if num == 4:
        p = [473,854]
        screen.blit(odds, p)
        pygame.display.update()
    if num == 3:
        p = [353,779]
        screen.blit(odds, p)
        pygame.display.update()
    if num == 2:
        p = [513,931]
        screen.blit(odds, p)
        pygame.display.update()
    if num == 1:
        p = [473,854]
        screen.blit(odds, p)
        pygame.display.update()
