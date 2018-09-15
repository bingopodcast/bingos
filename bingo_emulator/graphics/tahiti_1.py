
import pygame
import random

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

meter = pygame.image.load('graphics/assets/silver_register_cover.png').convert()
sc_arrow = pygame.image.load('tahiti_1/assets/sc_arrow.png').convert_alpha()
sc = pygame.image.load('tahiti_1/assets/super_card.png').convert_alpha()
eb = pygame.image.load('tahiti_1/assets/eb.png').convert_alpha()
extra_ball = pygame.image.load('tahiti_1/assets/extra_ball.png').convert_alpha()
extra_balls = pygame.image.load('tahiti_1/assets/extra_balls.png').convert_alpha()
o1 = pygame.image.load('tahiti_1/assets/odds1.png').convert_alpha()
o2 = pygame.image.load('tahiti_1/assets/odds2.png').convert_alpha()
o3 = pygame.image.load('tahiti_1/assets/odds3.png').convert_alpha()
o4 = pygame.image.load('tahiti_1/assets/odds4.png').convert_alpha()
o5 = pygame.image.load('tahiti_1/assets/odds5.png').convert_alpha()
o6 = pygame.image.load('tahiti_1/assets/odds6.png').convert_alpha()
o7 = pygame.image.load('tahiti_1/assets/odds7.png').convert_alpha()
o8 = pygame.image.load('tahiti_1/assets/odds8.png').convert_alpha()
star = pygame.image.load('tahiti_1/assets/rollover.png').convert_alpha()
number = pygame.image.load('tahiti_1/assets/number.png').convert_alpha()
sc_number = pygame.image.load('tahiti_1/assets/sc_number.png').convert_alpha()
tilt = pygame.image.load('tahiti_1/assets/tilt.png').convert_alpha()
select_now = pygame.image.load('tahiti_1/assets/select_now.png').convert_alpha()
red_number = pygame.image.load('tahiti_1/assets/red_number.png').convert_alpha()
red_sc_number = pygame.image.load('tahiti_1/assets/red_sc_number.png').convert_alpha()
s_number = pygame.image.load('tahiti_1/assets/spotted_numbers.png').convert_alpha()
s_arrow = pygame.image.load('tahiti_1/assets/selection_arrow.png').convert_alpha()
before_fourth = pygame.image.load('tahiti_1/assets/before_fourth.png').convert_alpha()
select_feature = pygame.image.load('tahiti_1/assets/select_feature.png').convert_alpha()
red_select_feature = pygame.image.load('tahiti_1/assets/red_select_feature.png').convert_alpha()
three_four = pygame.image.load('tahiti_1/assets/3_as_4.png').convert_alpha()
special_card = pygame.image.load('tahiti_1/assets/special_card.png').convert_alpha()
bg_menu = pygame.image.load('tahiti_1/assets/tahiti_1_menu.png')
bg_gi = pygame.image.load('tahiti_1/assets/tahiti_1_gi.png')
bg_off = pygame.image.load('tahiti_1/assets/tahiti_1_off.png')

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
        screen.blit(bg_menu, backglass_position)
    else:
        if (s.game.anti_cheat.status == True):
            screen.blit(bg_gi, backglass_position)
        else:
            screen.blit(bg_off, backglass_position)

    if s.game.super_card.position == 1:
        p = [37,423]
        screen.blit(sc_arrow, p)
    if s.game.super_card.position == 2:
        p = [72,423]
        screen.blit(sc_arrow, p)
    if s.game.super_card.position == 3:
        p = [108,422]
        screen.blit(sc_arrow, p)
    if s.game.super_card.position == 4:
        p = [143,422]
        screen.blit(sc_arrow, p)
    if s.game.super_card.position == 5:
        p = [548,422]
        screen.blit(sc_arrow, p)
    if s.game.super_card.position == 6:
        p = [582,422]
        screen.blit(sc_arrow, p)
    if s.game.super_card.position == 7:
        p = [614,422]
        screen.blit(sc_arrow, p)
    if s.game.super_card.position == 8:
        p = [652,422]
        screen.blit(sc_arrow, p)

    if s.game.super_card.position >= 4:
        p = [43,253]
        screen.blit(sc, p)

    if s.game.super_card.position >= 8:
        p = [550,253]
        screen.blit(sc, p)

    if s.game.eb_play.status == True:
        p = [294,943]
        screen.blit(extra_balls, p)

    if s.game.extra_ball.position == 1:
        eb_position = [96,966]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 2:
        eb_position = [129,966]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 3:
        eb_position = [163,966]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 4:
        eb_position = [197,967]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 5:
        eb_position = [231,967]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 6:
        eb_position = [275,968]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 7:
        eb_position = [310,968]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 8:
        eb_position = [344,969]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 9:
        eb_position = [379,969]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 10:
        eb_position = [413,969]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 11:
        eb_position = [457,969]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 12:
        eb_position = [491,969]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 13:
        eb_position = [526,968]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 14:
        eb_position = [560,967]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 15:
        eb_position = [595,966]
        screen.blit(eb, eb_position)
    
    if s.game.extra_ball.position >= 5 and s.game.extra_ball.position < 10:
        eb_pos = [96,995]
        screen.blit(extra_ball, eb_pos)
    if s.game.extra_ball.position >= 10 and s.game.extra_ball.position < 15:
        eb_pos = [275,996]
        screen.blit(extra_ball, eb_pos)
    if s.game.extra_ball.position == 15:
        eb_pos = [456,995]
        screen.blit(extra_ball, eb_pos)
    
    if s.game.odds.position > 0:
        if s.game.odds.position == 1:
            odds_position = [156,872]
            screen.blit(o1, odds_position)
        if s.game.odds.position == 2:
            odds_position = [199,837]
            screen.blit(o2, odds_position)
        if s.game.odds.position == 3:
            odds_position = [249,815]
            screen.blit(o3, odds_position)
        if s.game.odds.position == 4:
            odds_position = [307,803]
            screen.blit(o4, odds_position)
        if s.game.odds.position == 5:
            odds_position = [368,799]
            screen.blit(o5, odds_position)
        if s.game.odds.position == 6:
            odds_position = [400,807]
            screen.blit(o6, odds_position)
        if s.game.odds.position == 7:
            odds_position = [437,835]
            screen.blit(o7, odds_position)
        if s.game.odds.position == 8:
            odds_position = [466,869]
            screen.blit(o8, odds_position)

    if s.game.red_star.status == True:
        rs_position = [651,972]
        screen.blit(star, rs_position)

    if s.game.yellow_star.status == True:
        ys_position = [34,973]
        screen.blit(star, ys_position)

    if s.game.corners.status == True:
        corners_position = [390,596]
        screen.blit(three_four, corners_position)

    if s.game.tilt.status == False:
        if s.holes:
            if 1 in s.holes:
                number_position = [224,487]
                screen.blit(number, number_position)
                number_position = [552,339]
                screen.blit(sc_number, number_position)
                number_position = [63,545]
                screen.blit(sc_number, number_position)
            if 2 in s.holes:
                number_position = [223,433]
                screen.blit(number, number_position)
            if 3 in s.holes:
                number_position = [449,539]
                screen.blit(number, number_position)
                number_position = [91,296]
                screen.blit(sc_number, number_position)
            if 4 in s.holes:
                number_position = [281,327]
                screen.blit(number, number_position)
                number_position = [599,382]
                screen.blit(sc_number, number_position)
                number_position = [63,589]
                screen.blit(sc_number, number_position)
            if 5 in s.holes:
                number_position = [335,541]
                screen.blit(number, number_position)
            if 6 in s.holes:
                number_position = [449,328]
                screen.blit(number, number_position)
                number_position = [623,589]
                screen.blit(sc_number, number_position)
            if 7 in s.holes:
                number_position = [279,540]
                screen.blit(number, number_position)
                number_position = [598,297]
                screen.blit(sc_number, number_position)
            if 8 in s.holes:
                number_position = [450,380]
                screen.blit(number, number_position)
            if 9 in s.holes:
                number_position = [225,328]
                screen.blit(number, number_position)
                number_position = [43,339]
                screen.blit(sc_number, number_position)
                number_position = [624,543]
                screen.blit(sc_number, number_position)
            if 10 in s.holes:
                number_position = [225,380]
                screen.blit(number, number_position)
                number_position = [599,339]
                screen.blit(sc_number, number_position)
            if 11 in s.holes:
                number_position = [223,540]
                screen.blit(number, number_position)
                number_position = [643,297]
                screen.blit(sc_number, number_position)
                number_position = [136,338]
                screen.blit(sc_number, number_position)
            if 12 in s.holes:
                number_position = [392,433]
                screen.blit(number, number_position)
                number_position = [43,382]
                screen.blit(sc_number, number_position)
                number_position = [109,543]
                screen.blit(sc_number, number_position)
            if 13 in s.holes:
                number_position = [335,487]
                screen.blit(number, number_position)
                number_position = [643,341]
                screen.blit(sc_number, number_position)
            if 14 in s.holes:
                number_position = [335,379]
                screen.blit(number, number_position)
                number_position = [135,381]
                screen.blit(sc_number, number_position)
            if 15 in s.holes:
                number_position = [337,328]
                screen.blit(number, number_position)
                number_position = [553,296]
                screen.blit(sc_number, number_position)
            if 16 in s.holes:
                number_position = [335,434]
                screen.blit(number, number_position)
            if 17 in s.holes:
                number_position = [450,485]
                screen.blit(number, number_position)
                number_position = [553,382]
                screen.blit(sc_number, number_position)
                number_position = [577,587]
                screen.blit(sc_number, number_position)
            if 18 in s.holes:
                number_position = [279,433]
                screen.blit(number, number_position)
                number_position = [136,295]
                screen.blit(sc_number, number_position)
                number_position = [644,383]
                screen.blit(sc_number, number_position)
            if 19 in s.holes:
                number_position = [279,379]
                screen.blit(number, number_position)
            if 20 in s.holes:
                number_position = [392,379]
                screen.blit(number, number_position)
            if 21 in s.holes:
                number_position = [391,487]
                screen.blit(number, number_position)
            if 22 in s.holes:
                number_position = [280,488]
                screen.blit(number, number_position)
            if 23 in s.holes:
                number_position = [391,542]
                screen.blit(number, number_position)
                number_position = [44,297]
                screen.blit(sc_number, number_position)
                number_position = [577,543]
                screen.blit(sc_number, number_position)
            if 24 in s.holes:
                number_position = [393,329]
                screen.blit(number, number_position)
                number_position = [89,382]
                screen.blit(sc_number, number_position)
                number_position = [109,589]
                screen.blit(sc_number, number_position)
            if 25 in s.holes:
                number_position = [447,433]
                screen.blit(number, number_position)
                number_position = [90,339]
                screen.blit(sc_number, number_position)

    if s.game.tilt.status == True:
        tilt_position = [375,765]
        screen.blit(tilt, tilt_position)

    if s.game.selection_feature.position == 2:
        p = [269,649]
        screen.blit(s_arrow, p)
    if s.game.selection_feature.position == 3:
        p = [330,649]
        screen.blit(s_arrow, p)
    if s.game.selection_feature.position == 4:
        p = [390,649]
        screen.blit(s_arrow, p)
    if s.game.selection_feature.position >= 5:
        p = [93,684]
        screen.blit(s_number, p)
    if s.game.selection_feature.position >= 6:
        p = [145,683]
        screen.blit(s_number, p)
    if s.game.selection_feature.position >= 7:
        p = [198,683]
        screen.blit(s_number, p)
    if s.game.selection_feature.position >= 8:
        p = [251,682]
        screen.blit(s_number, p)
    if s.game.selection_feature.position >= 9:
        p = [303,683]
        screen.blit(s_number, p)
    if s.game.selection_feature.position >= 10:
        p = [354,684]
        screen.blit(s_number, p)
    if s.game.selection_feature.position >= 11:
        p = [406,684]
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

    if s.game.before_fourth.status == True and (s.game.selection_feature.position > 3 or s.game.selection_feature_relay.status == True):
        p = [9,669]
        screen.blit(before_fourth, p)
    if s.game.before_fifth.status == True and (s.game.selection_feature.position > 3 or s.game.selection_feature_relay.status == True):
        p = [633,670]
        screen.blit(before_fourth, p)

    if s.game.before_fourth.status == True:
        if s.game.ball_count.position < 4:
            if s.game.select_spots.status == True:
                if s.game.selection_feature.position >= 5:
                    if s.game.spotted.position == 0:
                        #19
                        number_position = [279,379]
                        screen.blit(red_number, number_position)
                if s.game.selection_feature.position >= 6:
                    if s.game.spotted.position == 1:
                        #20
                        number_position = [389,379]
                        screen.blit(red_number, number_position)
                if s.game.selection_feature.position >= 7:
                    if s.game.spotted.position == 2:
                        #21
                        number_position = [391,487]
                        screen.blit(red_number, number_position)
                if s.game.selection_feature.position >= 8:
                    if s.game.spotted.position == 3:
                        #22
                        number_position = [280,488]
                        screen.blit(red_number, number_position)
                if s.game.selection_feature.position >= 9:
                    if s.game.spotted.position == 4:
                        #16
                        number_position = [335,434]
                        screen.blit(red_number, number_position)
                if s.game.selection_feature.position >= 10:
                    if s.game.spotted.position == 5:
                        #25
                        number_position = [447,433]
                        screen.blit(red_number, number_position)
                        number_position = [90,339]
                        screen.blit(red_sc_number, number_position)
                if s.game.selection_feature.position >= 11:
                    if s.game.spotted.position == 6:
                        #10
                        number_position = [223,379]
                        screen.blit(red_number, number_position)
                        number_position = [599,339]
                        screen.blit(red_sc_number, number_position)
            if s.game.selection_feature_relay.status == True:
                if s.game.spotted.position == 7:
                    p = [106,723]
                    screen.blit(red_select_feature, p)
                if s.game.spotted.position == 8:
                    p = [234,723]
                    screen.blit(red_select_feature, p)
                if s.game.spotted.position == 9:
                    p = [362,723]
                    screen.blit(red_select_feature, p)
                if s.game.spotted.position == 10:
                    p = [491,723]
                    screen.blit(red_select_feature, p)

    if s.game.before_fifth.status == True:
        if s.game.ball_count.position < 5:
            if s.game.select_spots.status == True:
                if s.game.selection_feature.position >= 5:
                    if s.game.spotted.position == 0:
                        #19
                        number_position = [279,379]
                        screen.blit(red_number, number_position)
                if s.game.selection_feature.position >= 6:
                    if s.game.spotted.position == 1:
                        #20
                        number_position = [389,379]
                        screen.blit(red_number, number_position)
                if s.game.selection_feature.position >= 7:
                    if s.game.spotted.position == 2:
                        #21
                        number_position = [391,487]
                        screen.blit(red_number, number_position)
                if s.game.selection_feature.position >= 8:
                    if s.game.spotted.position == 3:
                        #22
                        number_position = [280,488]
                        screen.blit(red_number, number_position)
                if s.game.selection_feature.position >= 9:
                    if s.game.spotted.position == 4:
                        #16
                        number_position = [335,434]
                        screen.blit(red_number, number_position)
                if s.game.selection_feature.position >= 10:
                    if s.game.spotted.position == 5:
                        #25
                        number_position = [447,433]
                        screen.blit(red_number, number_position)
                        number_position = [90,339]
                        screen.blit(red_sc_number, number_position)
                if s.game.selection_feature.position >= 11:
                    if s.game.spotted.position == 6:
                        #10
                        number_position = [223,379]
                        screen.blit(red_number, number_position)
                        number_position = [599,339]
                        screen.blit(red_sc_number, number_position)
            if s.game.selection_feature_relay.status == True:
                if s.game.spotted.position == 7:
                    p = [106,723]
                    screen.blit(red_select_feature, p)
                if s.game.spotted.position == 8:
                    p = [234,723]
                    screen.blit(red_select_feature, p)
                if s.game.spotted.position == 9:
                    p = [362,723]
                    screen.blit(red_select_feature, p)
                if s.game.spotted.position == 10:
                    p = [491,723]
                    screen.blit(red_select_feature, p)

    if s.game.selection_feature_relay.status == True:
        p = [106,723]
        screen.blit(select_feature, p)
        p = [234,723]
        screen.blit(select_feature, p)
        p = [362,723]
        screen.blit(select_feature, p)
        p = [491,723]
        screen.blit(select_feature, p)


    if s.game.selection_feature_relay.status == True:
        if s.game.before_fourth.status == True:
            max_ball = 4
        else:
            max_ball = 5
        if s.game.ball_count.position == max_ball:
            if s.game.spotted.position == 8:
                p = [218,598]
                screen.blit(three_four, p)

    if s.game.three_as_four.status == True:
        p = [218,598]
        screen.blit(three_four, p)

    if s.game.left_special_card.status == True:
        p = [55,507]
        screen.blit(special_card, p)
    if s.game.right_special_card.status == True:
        p = [569,507]
        screen.blit(special_card, p)

    pygame.display.update()

def blink(args):
    dirty_rects = []
    s = args[0]
    b = args[1]
    sn = args[2]

    if b == 0:
        if sn == 1:
            p = [461,683]
            dirty_rects.append(screen.blit(select_now, p))
        pygame.display.update(dirty_rects)
    else:
        dirty_rects.append(screen.blit(bg_gi, (461,683), pygame.Rect(461,683,167,38)))
        pygame.display.update(dirty_rects)
    b = not b

    args = [s,b,sn]

    s.delay(name="blink", delay=0.1, handler=blink, param=args)

def eb_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]

    if s.game.extra_ball.position < 2:
        dirty_rects.append(screen.blit(bg_gi, (129,966), pygame.Rect(129,966,31,27)))
    if s.game.extra_ball.position < 3:
        dirty_rects.append(screen.blit(bg_gi, (163,966), pygame.Rect(163,966,31,27)))
    if s.game.extra_ball.position < 4:
        dirty_rects.append(screen.blit(bg_gi, (197,967), pygame.Rect(197,967,31,27)))
    if s.game.extra_ball.position < 5:
        dirty_rects.append(screen.blit(bg_gi, (231,967), pygame.Rect(231,967,31,27)))
    if s.game.extra_ball.position < 6:
        dirty_rects.append(screen.blit(bg_gi, (275,968), pygame.Rect(275,968,31,27)))
    if s.game.extra_ball.position < 7:
        dirty_rects.append(screen.blit(bg_gi, (310,968), pygame.Rect(310,968,31,27)))
    if s.game.extra_ball.position < 8:
        dirty_rects.append(screen.blit(bg_gi, (344,969), pygame.Rect(344,969,31,27)))
    if s.game.extra_ball.position < 9:
        dirty_rects.append(screen.blit(bg_gi, (379,969), pygame.Rect(379,969,31,27)))
    if s.game.extra_ball.position < 10:
        dirty_rects.append(screen.blit(bg_gi, (413,969), pygame.Rect(413,969,31,27)))
    if s.game.extra_ball.position < 11:
        dirty_rects.append(screen.blit(bg_gi, (457,969), pygame.Rect(457,969,31,27)))
    if s.game.extra_ball.position < 12:
        dirty_rects.append(screen.blit(bg_gi, (491,969), pygame.Rect(491,969,31,27)))
    if s.game.extra_ball.position < 13:
        dirty_rects.append(screen.blit(bg_gi, (526,968), pygame.Rect(526,968,31,27)))
    if s.game.extra_ball.position < 14:
        dirty_rects.append(screen.blit(bg_gi, (560,967), pygame.Rect(560,967,31,27)))
    if s.game.extra_ball.position < 15:
        dirty_rects.append(screen.blit(bg_gi, (595,966), pygame.Rect(595,966,31,27)))
    pygame.display.update(dirty_rects)

    if num in [0,14,3,17]:
        if s.game.extra_ball.position < 2:
            p = [129,966]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects) 
    elif num in [1,15,4,18]:
        if s.game.extra_ball.position < 3:
            p = [163,966]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects) 
    elif num in [2,16,5,19]:
        if s.game.extra_ball.position < 4:
            p = [197,967]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
    elif num in [3,17,6,20]:
        if s.game.extra_ball.position < 5:
            p = [231,967]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
    elif num in [4,18,7,21]:
        if s.game.extra_ball.position < 6:
            p = [275,968]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
    elif num in [5,19,8,22]:
        if s.game.extra_ball.position < 7:
            p = [310,968]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
    elif num in [6,20,9,23]:
        if s.game.extra_ball.position < 8:
            p = [344,969]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
    elif num in [7,21,10,24]:
        if s.game.extra_ball.position < 9:
            p = [379,969]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
    elif num in [8,22,11]:
        if s.game.extra_ball.position < 10:
            p = [413,969]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
    elif num in [9,23,12]:
        if s.game.extra_ball.position < 11:
            p = [457,969]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
    elif num in [10,24,13]:
        if s.game.extra_ball.position < 12:
            p = [491,969]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
    elif num in [11,0,14]:
        if s.game.extra_ball.position < 13:
            p = [526,968]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
    elif num in [12,1,15]:
        if s.game.extra_ball.position < 14:
            p = [560,967]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
    elif num in [13,2,16]:
        if s.game.extra_ball.position < 15:
            p = [595,966]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)

def clear_odds(s, num):
    global screen

    dirty_rects = []

    if s.game.odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (156,872), pygame.Rect(156,872,102,81)))
    if s.game.odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (199,837), pygame.Rect(199,837,78,92)))
    if s.game.odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (249,815), pygame.Rect(249,815,63,101)))
    if s.game.odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (307,803), pygame.Rect(307,803,45,106)))
    if s.game.odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (368,799), pygame.Rect(368,799,42,107)))
    if s.game.odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (400,807), pygame.Rect(400,807,69,106)))
    if s.game.odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (437,835), pygame.Rect(437,835,85,99)))
    if s.game.odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (466,869), pygame.Rect(466,869,102,88)))

    pygame.display.update(dirty_rects)

def draw_odds_animation(s, num):
    global screen
    dirty_rects = []

    if num in [0,11,17]:
        if s.game.odds.position != 1:
            p = [156,872]
            dirty_rects.append(screen.blit(o1, p))
            pygame.display.update(dirty_rects)
            return
    if num in [1,10,18]:
        if s.game.odds.position != 2:
            p = [199,837]
            dirty_rects.append(screen.blit(o2, p))
            pygame.display.update(dirty_rects)
            return
    if num in [4,12,19]:
        if s.game.odds.position != 3:
            p = [249,815]
            dirty_rects.append(screen.blit(o3, p))
            pygame.display.update(dirty_rects)
            return
    if num in [3,9,20]:
        if s.game.odds.position != 4:
            p = [307,803]
            dirty_rects.append(screen.blit(o4, p))
            pygame.display.update(dirty_rects)
            return
    if num in [5,13,21]:
        if s.game.odds.position != 5:
            p = [368,799]
            dirty_rects.append(screen.blit(o5, p))
            pygame.display.update(dirty_rects)
            return
    if num in [6,14,22]:
        if s.game.odds.position != 6:
            p = [400,807]
            dirty_rects.append(screen.blit(o6, p))
            pygame.display.update(dirty_rects)
            return
    if num in [7,16,23]:
        if s.game.odds.position != 7:
            p = [437,835]
            dirty_rects.append(screen.blit(o7, p))
            pygame.display.update(dirty_rects)
            return
    if num in [8,15,24]:
        if s.game.odds.position != 8:
            p = [466,869]
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

def clear_mixers(s):
    global screen
    dirty_rects = []
    if s.game.super_card.position < 4:
        dirty_rects.append(screen.blit(bg_gi, (43,253), pygame.Rect(43,253,134,39)))
    if s.game.super_card.position < 8:
        dirty_rects.append(screen.blit(bg_gi, (550,253), pygame.Rect(550,253,134,39)))
    if s.game.left_special_card.status == False:
        dirty_rects.append(screen.blit(bg_gi, (55,507), pygame.Rect(55,507,100,32)))
    if s.game.corners.status == False:
        dirty_rects.append(screen.blit(bg_gi, (390,596), pygame.Rect(390,596,114,48)))
    if s.game.yellow_star.status == False:
        dirty_rects.append(screen.blit(bg_gi, (34,973), pygame.Rect(34,973,39,36)))
    if s.game.red_star.status == False:
        dirty_rects.append(screen.blit(bg_gi, (651,972), pygame.Rect(651,972,39,36)))
    if s.game.right_special_card.status == False:
        dirty_rects.append(screen.blit(bg_gi, (569,507), pygame.Rect(569,507,100,32)))
    pygame.display.update(dirty_rects)
    return

def animate_mixer1(s):
    global screen
    dirty_rects = []
    if s.game.super_card.position < 4:
        p = [43,253]
        dirty_rects.append(screen.blit(sc, p))
        pygame.display.update(dirty_rects)
        return

def animate_mixer2(s):
    global screen
    dirty_rects = []
    clear_mixers(s)
    if s.game.super_card.position < 8:
        p = [550,253]
        dirty_rects.append(screen.blit(sc, p))
    if s.game.left_special_card.status == False:
        p = [55,507]
        dirty_rects.append(screen.blit(special_card, p))
    pygame.display.update(dirty_rects)
    return

def animate_mixer3(s):
    global screen
    dirty_rects = []
    
    if s.game.corners.status == False:
        p = [390,596]
        dirty_rects.append(screen.blit(three_four, p))
    if s.game.red_star.status == False:
        p = [651,972]
        dirty_rects.append(screen.blit(star, p))
        s.game.coils.yellowROLamp.pulse(85)
    if s.game.yellow_star.status == False:
        p = [34,973]
        dirty_rects.append(screen.blit(star, p))
        s.game.coils.redROLamp.pulse(85)
    pygame.display.update(dirty_rects)
    return

def animate_mixer4(s):
    global screen
    dirty_rects = []
    if s.game.right_special_card.status == False:
        p = [569,507]
        dirty_rects.append(screen.blit(special_card, p))
    pygame.display.update(dirty_rects)
    return

def clear_features(s, num):
    global screen
    dirty_rects = []

    if s.game.before_fourth.status == False:
        dirty_rects.append(screen.blit(bg_gi, (9,669), pygame.Rect(9,669,82,67)))
    if s.game.before_fifth.status == False:
        dirty_rects.append(screen.blit(bg_gi, (633,670), pygame.Rect(633,670,82,67)))

    if s.game.selection_feature.position < 2:
        dirty_rects.append(screen.blit(bg_gi, (269,649), pygame.Rect(269,649,61,36)))
    if s.game.selection_feature.position < 3:
        dirty_rects.append(screen.blit(bg_gi, (330,649), pygame.Rect(330,649,61,36)))
    if s.game.selection_feature.position < 4:
        dirty_rects.append(screen.blit(bg_gi, (390,649), pygame.Rect(390,649,61,36)))
    if s.game.selection_feature.position < 6:
        dirty_rects.append(screen.blit(bg_gi, (93,684), pygame.Rect(93,684,51,37)))
        dirty_rects.append(screen.blit(bg_gi, (145,683), pygame.Rect(145,683,51,37)))
    if s.game.selection_feature.position < 7:
        dirty_rects.append(screen.blit(bg_gi, (198,683), pygame.Rect(198,683,51,37)))
        if s.game.selection_feature_relay.status == False:
            dirty_rects.append(screen.blit(bg_gi, (106,723), pygame.Rect(106,723,126,45)))
            dirty_rects.append(screen.blit(bg_gi, (234,723), pygame.Rect(234,723,126,45)))
            dirty_rects.append(screen.blit(bg_gi, (362,723), pygame.Rect(362,723,126,45)))
            dirty_rects.append(screen.blit(bg_gi, (491,723), pygame.Rect(491,723,126,45)))
    if s.game.selection_feature.position < 8:
        dirty_rects.append(screen.blit(bg_gi, (251,682), pygame.Rect(251,682,51,37)))
    if s.game.selection_feature.position < 9:
        dirty_rects.append(screen.blit(bg_gi, (303,683), pygame.Rect(303,683,51,37)))
    if s.game.selection_feature.position < 10:
        dirty_rects.append(screen.blit(bg_gi, (354,684), pygame.Rect(354,684,51,37)))
    if s.game.selection_feature.position < 11:
        dirty_rects.append(screen.blit(bg_gi, (406,684), pygame.Rect(406,684,51,37)))

    pygame.display.update(dirty_rects)

def draw_feature_animation(s, num):
    global screen
    dirty_rects = []
 
    if num in [4,15]:
        if s.game.before_fourth.status == False:
            p = [9,669]
            dirty_rects.append(screen.blit(before_fourth, p))
            pygame.display.update(dirty_rects)
            return
    if num in [10,21]:
        if s.game.before_fifth.status == False:
            p = [633,670]
            dirty_rects.append(screen.blit(before_fourth, p))
            pygame.display.update(dirty_rects)
            return
    if num in [0,11,22]:
        if s.game.selection_feature.position < 2:
            p = [269,649]
            dirty_rects.append(screen.blit(s_arrow, p))
            pygame.display.update(dirty_rects)
            return
    if num in [9,20,23]:
        if s.game.selection_feature.position < 3:
            p = [330,649]
            dirty_rects.append(screen.blit(s_arrow, p))
            pygame.display.update(dirty_rects)
            return
    if num in [1,12,24]:
        if s.game.selection_feature.position < 4:
            p = [390,649]
            dirty_rects.append(screen.blit(s_arrow, p))
            pygame.display.update(dirty_rects)
            return
    if num in [2,13]:
        if s.game.selection_feature.position < 6:
            p = [93,684]
            dirty_rects.append(screen.blit(s_number, p))
            p = [145,683]
            dirty_rects.append(screen.blit(s_number, p))
            pygame.display.update(dirty_rects)
            return
    if num in [3,14]:
        if s.game.selection_feature.position < 7:
            p = [198,683]
            dirty_rects.append(screen.blit(s_number, p))
            pygame.display.update(dirty_rects)
            return
    if num in [5,16]:
        if s.game.selection_feature.position < 8:
            p = [251,682]
            dirty_rects.append(screen.blit(s_number, p))
            pygame.display.update(dirty_rects)
            return
    if num in [6,17]:
        if s.game.selection_feature.position < 9:
            p = [303,683]
            dirty_rects.append(screen.blit(s_number, p))
            pygame.display.update(dirty_rects)
            return
    if num in [7,18]:
        if s.game.selection_feature.position < 10:
            p = [354,684]
            dirty_rects.append(screen.blit(s_number, p))
            pygame.display.update(dirty_rects)
            return
    if num in [8,19]:
        if s.game.selection_feature.position < 11:
            p = [406,684]
            dirty_rects.append(screen.blit(s_number, p))
            pygame.display.update(dirty_rects)
            return
    if num in [4,15]:
        if s.game.selection_feature_relay.status == False:
            p = [106,723]
            dirty_rects.append(screen.blit(select_feature, p))
            p = [234,723]
            dirty_rects.append(screen.blit(select_feature, p))
            p = [362,723]
            dirty_rects.append(screen.blit(select_feature, p))
            p = [491,723]
            dirty_rects.append(screen.blit(select_feature, p))
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

    if num % 2 == 0:
        clear_mixers(s)

    draw_odds_animation(s, num)
    draw_feature_animation(s, num)

