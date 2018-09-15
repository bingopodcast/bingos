
import pygame
import random

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

meter = pygame.image.load('graphics/assets/silver_register_cover.png').convert()
sc_arrow = pygame.image.load('havana/assets/sc_arrow.png').convert_alpha()
sc = pygame.image.load('havana/assets/super_card.png').convert_alpha()
eb = pygame.image.load('havana/assets/eb.png').convert_alpha()
extra_ball = pygame.image.load('havana/assets/extra_ball.png').convert_alpha()
extra_balls = pygame.image.load('havana/assets/extra_balls.png').convert_alpha()
o1 = pygame.image.load('havana/assets/odds1.png').convert_alpha()
o2 = pygame.image.load('havana/assets/odds2.png').convert_alpha()
o3 = pygame.image.load('havana/assets/odds3.png').convert_alpha()
o4 = pygame.image.load('havana/assets/odds4.png').convert_alpha()
o5 = pygame.image.load('havana/assets/odds5.png').convert_alpha()
o6 = pygame.image.load('havana/assets/odds6.png').convert_alpha()
o7 = pygame.image.load('havana/assets/odds7.png').convert_alpha()
o8 = pygame.image.load('havana/assets/odds8.png').convert_alpha()
star = pygame.image.load('havana/assets/rollover.png').convert_alpha()
number = pygame.image.load('havana/assets/number.png').convert_alpha()
sc_number = pygame.image.load('havana/assets/sc_number.png').convert_alpha()
tilt = pygame.image.load('havana/assets/tilt.png').convert_alpha()
select_now = pygame.image.load('havana/assets/select_now.png').convert_alpha()
red_number = pygame.image.load('havana/assets/red_number.png').convert_alpha()
red_sc_number = pygame.image.load('havana/assets/red_sc_number.png').convert_alpha()
s_number = pygame.image.load('havana/assets/spotted_numbers.png').convert_alpha()
s_arrow = pygame.image.load('havana/assets/selection_arrow.png').convert_alpha()
before_fourth = pygame.image.load('havana/assets/before_fourth.png').convert_alpha()
select_feature = pygame.image.load('havana/assets/select_feature.png').convert_alpha()
red_select_feature = pygame.image.load('havana/assets/red_select_feature.png').convert_alpha()
three_four = pygame.image.load('havana/assets/3_as_4.png').convert_alpha()
special_card = pygame.image.load('havana/assets/special_card.png').convert_alpha()
letter_ha = pygame.image.load('havana/assets/letter_ha.png').convert_alpha()
letter_va = pygame.image.load('havana/assets/letter_va.png').convert_alpha()
letter_na = pygame.image.load('havana/assets/letter_na.png').convert_alpha()
lite_a_name = pygame.image.load('havana/assets/lite_a_name.png').convert_alpha()
return_arrow = pygame.image.load('havana/assets/return_arrow.png').convert_alpha()
ball_return = pygame.image.load('havana/assets/return.png').convert_alpha()
bg_menu = pygame.image.load('havana/assets/havana_menu.png')
bg_gi = pygame.image.load('havana/assets/havana_gi.png')
bg_off = pygame.image.load('havana/assets/havana_off.png')

class scorereel():
    """ Score Reels are used to count replays """
    def __init__(self, pos, image):
        self.position = pos
        self.default_y = self.position[1]
        self.image = pygame.image.load(image).convert()

reel1 = scorereel([113,831], "graphics/assets/green_reel.png")
reel10 = scorereel([94,831], "graphics/assets/green_reel.png")
reel100 = scorereel([75,831], "graphics/assets/green_reel.png")

def display(s, replays=0, menu=False):
    
    meter.set_colorkey((255,0,252))
    meter_position = [65,829]

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

    if s.game.tilt.status == True:
        p = [231,263]
        screen.blit(letter_ha, p)
        p = [317,263]
        screen.blit(letter_va, p)
        p = [408,263]
        screen.blit(letter_na, p)
    else:
        p = [218,309]
        screen.blit(lite_a_name, p)

    if s.game.super_card.position == 1:
        p = [45,412]
        screen.blit(sc_arrow, p)
    if s.game.super_card.position == 2:
        p = [80,412]
        screen.blit(sc_arrow, p)
    if s.game.super_card.position == 3:
        p = [120,412]
        screen.blit(sc_arrow, p)
    if s.game.super_card.position == 4:
        p = [155,412]
        screen.blit(sc_arrow, p)
    if s.game.super_card.position == 5:
        p = [552,412]
        screen.blit(sc_arrow, p)
    if s.game.super_card.position == 6:
        p = [589,412]
        screen.blit(sc_arrow, p)
    if s.game.super_card.position == 7:
        p = [620,412]
        screen.blit(sc_arrow, p)
    if s.game.super_card.position == 8:
        p = [658,412]
        screen.blit(sc_arrow, p)

    if s.game.super_card.position >= 4:
        p = [49,245]
        screen.blit(sc, p)

    if s.game.super_card.position >= 8:
        p = [549,243]
        screen.blit(sc, p)

    if s.game.extra_ball.position == 1:
        eb_position = [99,969]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 2:
        eb_position = [132,969]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 3:
        eb_position = [167,969]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 4:
        eb_position = [202,969]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 5:
        eb_position = [238,969]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 6:
        eb_position = [278,969]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 7:
        eb_position = [314,969]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 8:
        eb_position = [350,969]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 9:
        eb_position = [382,969]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 10:
        eb_position = [418,969]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 11:
        eb_position = [458,969]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 12:
        eb_position = [494,969]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 13:
        eb_position = [530,969]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 14:
        eb_position = [564,969]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 15:
        eb_position = [599,969]
        screen.blit(eb, eb_position)

    if s.game.extra_ball.position >= 5 and s.game.extra_ball.position < 10:
        eb_pos = [96,998]
        screen.blit(extra_ball, eb_pos)
    if s.game.extra_ball.position >= 10 and s.game.extra_ball.position < 15:
        eb_pos = [275,998]
        screen.blit(extra_ball, eb_pos)
    if s.game.extra_ball.position == 15:
        eb_pos = [456,998]
        screen.blit(extra_ball, eb_pos)

    if s.game.odds.position > 0:
        if s.game.odds.position == 1:
            odds_position = [200,818]
            screen.blit(o1, odds_position)
        if s.game.odds.position == 2:
            odds_position = [268,822]
            screen.blit(o2, odds_position)
        if s.game.odds.position == 3:
            odds_position = [326,822]
            screen.blit(o3, odds_position)
        if s.game.odds.position == 4:
            odds_position = [387,825]
            screen.blit(o4, odds_position)
        if s.game.odds.position == 5:
            odds_position = [450,823]
            screen.blit(o5, odds_position)
        if s.game.odds.position == 6:
            odds_position = [515,820]
            screen.blit(o6, odds_position)
        if s.game.odds.position == 7:
            odds_position = [580,820]
            screen.blit(o7, odds_position)
        if s.game.odds.position == 8:
            odds_position = [638,820]
            screen.blit(o8, odds_position)

    if s.game.red_star.status == True:
        rs_position = [635,934]
        screen.blit(star, rs_position)

    if s.game.corners.status == True:
        corners_position = [367,625]
        screen.blit(three_four, corners_position)

    if s.game.tilt.status == False:
        if s.holes:
            if 1 in s.holes:
                number_position = [227,511]
                screen.blit(number, number_position)
                number_position = [548,324]
                screen.blit(sc_number, number_position)
                number_position = [67,535]
                screen.blit(sc_number, number_position)
            if 2 in s.holes:
                number_position = [227,456]
                screen.blit(number, number_position)
            if 3 in s.holes:
                number_position = [450,564]
                screen.blit(number, number_position)
                number_position = [92,282]
                screen.blit(sc_number, number_position)
            if 4 in s.holes:
                number_position = [282,348]
                screen.blit(number, number_position)
                number_position = [597,371]
                screen.blit(sc_number, number_position)
                number_position = [65,579]
                screen.blit(sc_number, number_position)
            if 5 in s.holes:
                number_position = [339,564]
                screen.blit(number, number_position)
            if 6 in s.holes:
                number_position = [450,349]
                screen.blit(number, number_position)
                number_position = [620,582]
                screen.blit(sc_number, number_position)
            if 7 in s.holes:
                number_position = [284,564]
                screen.blit(number, number_position)
                number_position = [596,280]
                screen.blit(sc_number, number_position)
            if 8 in s.holes:
                number_position = [450,402]
                screen.blit(number, number_position)
            if 9 in s.holes:
                number_position = [226,350]
                screen.blit(number, number_position)
                number_position = [46,328]
                screen.blit(sc_number, number_position)
                number_position = [619,538]
                screen.blit(sc_number, number_position)
            if 10 in s.holes:
                number_position = [226,403]
                screen.blit(number, number_position)
                number_position = [596,325]
                screen.blit(sc_number, number_position)
            if 11 in s.holes:
                number_position = [228,564]
                screen.blit(number, number_position)
                number_position = [137,326]
                screen.blit(sc_number, number_position)
                number_position = [643,282]
                screen.blit(sc_number, number_position)
            if 12 in s.holes:
                number_position = [393,456]
                screen.blit(number, number_position)
                number_position = [45,372]
                screen.blit(sc_number, number_position)
                number_position = [112,536]
                screen.blit(sc_number, number_position)
            if 13 in s.holes:
                number_position = [340,509]
                screen.blit(number, number_position)
                number_position = [643,326]
                screen.blit(sc_number, number_position)
            if 14 in s.holes:
                number_position = [338,402]
                screen.blit(number, number_position)
                number_position = [138,373]
                screen.blit(sc_number, number_position)
            if 15 in s.holes:
                number_position = [338,348]
                screen.blit(number, number_position)
                number_position = [546,284]
                screen.blit(sc_number, number_position)
            if 16 in s.holes:
                number_position = [338,457]
                screen.blit(number, number_position)
            if 17 in s.holes:
                number_position = [449,510]
                screen.blit(number, number_position)
                number_position = [548,371]
                screen.blit(sc_number, number_position)
                number_position = [572,583]
                screen.blit(sc_number, number_position)
            if 18 in s.holes:
                number_position = [282,456]
                screen.blit(number, number_position)
                number_position = [139,281]
                screen.blit(sc_number, number_position)
                number_position = [643,371]
                screen.blit(sc_number, number_position)
            if 19 in s.holes:
                number_position = [282,402]
                screen.blit(number, number_position)
            if 20 in s.holes:
                number_position = [394,402]
                screen.blit(number, number_position)
            if 21 in s.holes:
                number_position = [395,510]
                screen.blit(number, number_position)
            if 22 in s.holes:
                number_position = [285,509]
                screen.blit(number, number_position)
            if 23 in s.holes:
                number_position = [395,563]
                screen.blit(number, number_position)
                number_position = [47,283]
                screen.blit(sc_number, number_position)
                number_position = [573,536]
                screen.blit(sc_number, number_position)
            if 24 in s.holes:
                number_position = [395,348]
                screen.blit(number, number_position)
                number_position = [93,373]
                screen.blit(sc_number, number_position)
                number_position = [112,580]
                screen.blit(sc_number, number_position)
            if 25 in s.holes:
                number_position = [451,456]
                screen.blit(number, number_position)
                number_position = [91,328]
                screen.blit(sc_number, number_position)

    if s.game.tilt.status == True:
        tilt_position = [67,774]
        screen.blit(tilt, tilt_position)

    if s.game.selection_feature.position == 2:
        p = [104,681]
        screen.blit(s_arrow, p)
    if s.game.selection_feature.position == 3:
        p = [144,681]
        screen.blit(s_arrow, p)
    if s.game.selection_feature.position == 4:
        p = [182,681]
        screen.blit(s_arrow, p)
    if s.game.selection_feature.position >= 5:
        p = [215,679]
        screen.blit(s_number, p)
    if s.game.selection_feature.position >= 6:
        p = [256,679]
        screen.blit(s_number, p)
    if s.game.selection_feature.position >= 7:
        p = [295,679]
        screen.blit(s_number, p)
    if s.game.selection_feature.position >= 8:
        p = [334,679]
        screen.blit(s_number, p)
    if s.game.selection_feature.position >= 9:
        p = [374,679]
        screen.blit(s_number, p)
    if s.game.selection_feature.position >= 10:
        p = [412,679]
        screen.blit(s_number, p)
    if s.game.selection_feature.position >= 11:
        p = [453,679]
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
        p = [14,676]
        screen.blit(before_fourth, p)
    if s.game.before_fifth.status == True and (s.game.selection_feature.position > 3 or s.game.selection_feature_relay.status == True):
        p = [631,679]
        screen.blit(before_fourth, p)

    if s.game.before_fourth.status == True:
        if s.game.ball_count.position < 4:
            if s.game.select_spots.status == True:
                if s.game.selection_feature.position >= 5:
                    if s.game.spotted.position == 0:
                        #19
                        number_position = [282,402]
                        screen.blit(red_number, number_position)
                if s.game.selection_feature.position >= 6:
                    if s.game.spotted.position == 1:
                        #20
                        number_position = [394,402]
                        screen.blit(red_number, number_position)
                if s.game.selection_feature.position >= 7:
                    if s.game.spotted.position == 2:
                        #21
                        number_position = [395,510]
                        screen.blit(red_number, number_position)
                if s.game.selection_feature.position >= 8:
                    if s.game.spotted.position == 3:
                        #22
                        number_position = [285,509]
                        screen.blit(red_number, number_position)
                if s.game.selection_feature.position >= 9:
                    if s.game.spotted.position == 4:
                        #16
                        number_position = [338,457]
                        screen.blit(red_number, number_position)
                if s.game.selection_feature.position >= 10:
                    if s.game.spotted.position == 5:
                        #25
                        number_position = [451,456]
                        screen.blit(red_number, number_position)
                        number_position = [91,328]
                        screen.blit(red_sc_number, number_position)
                if s.game.selection_feature.position >= 11:
                    if s.game.spotted.position == 6:
                        #10
                        number_position = [226,403]
                        screen.blit(red_number, number_position)
                        number_position = [596,325]
                        screen.blit(red_sc_number, number_position)
            if s.game.selection_feature_relay.status == True:
                if s.game.spotted.position == 7:
                    p = [114,720]
                    screen.blit(red_select_feature, p)
                if s.game.spotted.position == 8:
                    p = [240,721]
                    screen.blit(red_select_feature, p)
                if s.game.spotted.position == 9:
                    p = [368,721]
                    screen.blit(red_select_feature, p)
                if s.game.spotted.position == 10:
                    p = [494,722]
                    screen.blit(red_select_feature, p)

    if s.game.before_fifth.status == True:
        if s.game.ball_count.position < 5:
            if s.game.select_spots.status == True:
                if s.game.selection_feature.position >= 5:
                    if s.game.spotted.position == 0:
                        #19
                        number_position = [282,402]
                        screen.blit(red_number, number_position)
                if s.game.selection_feature.position >= 6:
                    if s.game.spotted.position == 1:
                        #20
                        number_position = [394,402]
                        screen.blit(red_number, number_position)
                if s.game.selection_feature.position >= 7:
                    if s.game.spotted.position == 2:
                        #21
                        number_position = [395,510]
                        screen.blit(red_number, number_position)
                if s.game.selection_feature.position >= 8:
                    if s.game.spotted.position == 3:
                        #22
                        number_position = [285,509]
                        screen.blit(red_number, number_position)
                if s.game.selection_feature.position >= 9:
                    if s.game.spotted.position == 4:
                        #16
                        number_position = [338,457]
                        screen.blit(red_number, number_position)
                if s.game.selection_feature.position >= 10:
                    if s.game.spotted.position == 5:
                        #25
                        number_position = [451,456]
                        screen.blit(red_number, number_position)
                        number_position = [91,328]
                        screen.blit(red_sc_number, number_position)
                if s.game.selection_feature.position >= 11:
                    if s.game.spotted.position == 6:
                        #10
                        number_position = [226,403]
                        screen.blit(red_number, number_position)
                        number_position = [596,325]
                        screen.blit(red_sc_number, number_position)
            if s.game.selection_feature_relay.status == True:
                if s.game.spotted.position == 7:
                    p = [114,720]
                    screen.blit(red_select_feature, p)
                if s.game.spotted.position == 8:
                    p = [240,721]
                    screen.blit(red_select_feature, p)
                if s.game.spotted.position == 9:
                    p = [368,721]
                    screen.blit(red_select_feature, p)
                if s.game.spotted.position == 10:
                    p = [494,722]
                    screen.blit(red_select_feature, p)
                
    if s.game.selection_feature_relay.status == True:
        p = [114,720]
        screen.blit(select_feature, p)
        p = [240,721]
        screen.blit(select_feature, p)
        p = [368,721]
        screen.blit(select_feature, p)
        p = [494,722]
        screen.blit(select_feature, p)


    if s.game.selection_feature_relay.status == True:
        if s.game.before_fourth.status == True:
            max_ball = 4
        else:
            max_ball = 5
        if s.game.ball_count.position == max_ball:
            if s.game.spotted.position == 8:
                p = [256,625]
                screen.blit(three_four, p)

    if s.game.three_as_four.status == True:
        p = [256,625]
        screen.blit(three_four, p)

    if s.game.left_special_card.status == True:
        p = [66,495]
        screen.blit(special_card, p)
    if s.game.right_special_card.status == True:
        p = [572,496]
        screen.blit(special_card, p)

    if s.game.eb_play.status == True:
        p = [10,969]
        screen.blit(extra_balls, p)

    if s.game.letter_ha.status == True:
        p = [231,263]
        screen.blit(letter_ha, p)
    if s.game.letter_va.status == True:
        p = [317,263]
        screen.blit(letter_va, p)
    if s.game.letter_na.status == True:
        p = [408,263]
        screen.blit(letter_na, p)

    if s.game.ball_return.position == 1:
        p = [187,929]
        screen.blit(return_arrow, p)
    if s.game.ball_return.position == 2:
        p = [219,928]
        screen.blit(return_arrow, p)
    if s.game.ball_return.position == 3:
        p = [251,929]
        screen.blit(return_arrow, p)
    if s.game.ball_return.position == 4:
        p = [286,929]
        screen.blit(return_arrow, p)
    if s.game.ball_return.position == 5:
        p = [322,929]
        screen.blit(return_arrow, p)
        p = [364,928]
        screen.blit(ball_return, p)

    pygame.display.update()

def blink(args):
    dirty_rects = []
    s = args[0]
    b = args[1]
    sn = args[2]

    if b == 0:
        if sn == 1:
            p = [493,679]
            dirty_rects.append(screen.blit(select_now, p))
        pygame.display.update(dirty_rects)
    else:
        dirty_rects.append(screen.blit(bg_gi, (493,679), pygame.Rect(493,679,136,43)))
        pygame.display.update(dirty_rects)
    b = not b

    args = [s,b,sn]

    s.delay(name="blink", delay=0.1, handler=blink, param=args)

def eb_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]
    if s.game.extra_ball.position < 5:
        dirty_rects.append(screen.blit(bg_gi, (96,998), pygame.Rect(96,998,176,35)))
    if s.game.extra_ball.position < 10:
        dirty_rects.append(screen.blit(bg_gi, (275,998), pygame.Rect(275,998,176,35)))
    if s.game.extra_ball.position < 15:
        dirty_rects.append(screen.blit(bg_gi, (456,998), pygame.Rect(456,998,176,35)))
        dirty_rects.append(screen.blit(bg_gi, (599,969), pygame.Rect(599,969,30,31)))
    pygame.display.update(dirty_rects)

    if num in [1,9,17,4,12,15,21]:
        if s.game.extra_ball.position < 5:
            p = [96,998]
            dirty_rects.append(screen.blit(extra_ball, p))
            pygame.display.update(dirty_rects) 
    elif num in [2,10,18,5,7,13,16,22]:
        if s.game.extra_ball.position < 10:
            p = [275,998]
            dirty_rects.append(screen.blit(extra_ball, p))
            pygame.display.update(dirty_rects)
    elif num in [3,11,19,6,8,14,20,23]:
        if s.game.extra_ball.position < 15:
            p = [456,998]
            dirty_rects.append(screen.blit(extra_ball, p))
            p = [599,969]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)

def clear_odds(s, num):
    global screen
    dirty_rects = []
    if s.game.odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (200,818), pygame.Rect(200,818,61,86)))
    if s.game.odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (268,822), pygame.Rect(268,822,52,82)))
    if s.game.odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (326,822), pygame.Rect(326,822,52,84)))
    if s.game.odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (387,825), pygame.Rect(387,825,57,81)))
    if s.game.odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (450,823), pygame.Rect(450,823,57,84)))
    if s.game.odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (515,820), pygame.Rect(515,820,54,85)))
    if s.game.odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (580,820), pygame.Rect(580,820,56,88)))
    if s.game.odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (638,820), pygame.Rect(638,820,56,86)))

    pygame.display.update(dirty_rects)

def draw_odds_animation(s, num):
    global screen
    dirty_rects = []

    if num in [0,11,17]:
        if s.game.odds.position != 1:
            p = [200,818]
            dirty_rects.append(screen.blit(o1, p))
            pygame.display.update(dirty_rects)
            return
    if num in [1,10,18]:
        if s.game.odds.position != 2:
            p = [268,822]
            dirty_rects.append(screen.blit(o2, p))
            pygame.display.update(dirty_rects)
            return
    if num in [4,12,19]:
        if s.game.odds.position != 3:
            p = [326,822]
            dirty_rects.append(screen.blit(o3, p))
            pygame.display.update(dirty_rects)
            return
    if num in [3,9,20]:
        if s.game.odds.position != 4:
            p = [387,825]
            dirty_rects.append(screen.blit(o4, p))
            pygame.display.update(dirty_rects)
            return
    if num in [5,13,21]:
        if s.game.odds.position != 5:
            p = [450,823]
            dirty_rects.append(screen.blit(o5, p))
            pygame.display.update(dirty_rects)
            return
    if num in [6,14,22]:
        if s.game.odds.position != 6:
            p = [515,820]
            dirty_rects.append(screen.blit(o6, p))
            pygame.display.update(dirty_rects)
            return
    if num in [7,16,23]:
        if s.game.odds.position != 7:
            p = [580,820]
            dirty_rects.append(screen.blit(o7, p))
            pygame.display.update(dirty_rects)
            return
    if num in [8,15,24]:
        if s.game.odds.position != 8:
            p = [638,820]
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
        dirty_rects.append(screen.blit(bg_gi, (49,245), pygame.Rect(49,245,135,30)))
    if s.game.super_card.position < 8:
        dirty_rects.append(screen.blit(bg_gi, (549,243), pygame.Rect(549,243,135,30)))
    if s.game.corners.status == False:
        dirty_rects.append(screen.blit(bg_gi, (367,625), pygame.Rect(367,625,103,46)))
    if s.game.ball_return.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (364,928), pygame.Rect(364,928,178,38)))
    if s.game.red_star.status == False:
        dirty_rects.append(screen.blit(bg_gi, (635,934), pygame.Rect(635,934,73,95)))
    if s.game.left_special_card.status == False:
        dirty_rects.append(screen.blit(bg_gi, (66,495), pygame.Rect(66,495,92,35)))
    if s.game.right_special_card.status == False:
        dirty_rects.append(screen.blit(bg_gi, (572,496), pygame.Rect(572,496,92,35)))
    pygame.display.update(dirty_rects)
    return

def animate_mixer1(s):
    global screen
    dirty_rects = []
    if s.game.super_card.position < 4:
        p = [49,245]
        dirty_rects.append(screen.blit(sc, p))
        pygame.display.update(dirty_rects)
        return

def animate_mixer2(s):
    global screen
    dirty_rects = []
    if s.game.super_card.position < 8:
        p = [549,243]
        dirty_rects.append(screen.blit(sc, p))
    if s.game.left_special_card.status == False:
        p = [66,495]
        dirty_rects.append(screen.blit(special_card, p))
    pygame.display.update(dirty_rects)
    return

def animate_mixer3(s):
    global screen
    dirty_rects = []
    if s.game.corners.status == False:
        p = [367,625]
        dirty_rects.append(screen.blit(three_four, p))
    if s.game.red_star.status == False:
        p = [635,934]
        dirty_rects.append(screen.blit(star, p))
        s.game.coils.redROLamp.pulse(85)
        s.game.coils.yellowROLamp.pulse(85)
    if s.game.ball_return.position != 5:
        p = [364,928]
        dirty_rects.append(screen.blit(ball_return, p))
    pygame.display.update(dirty_rects)
    return

def animate_mixer4(s):
    global screen
    dirty_rects = []
    if s.game.right_special_card.status == False:
        p = [572,496]
        dirty_Rects.append(screen.blit(special_card, p))
    pygame.display.update(dirty_rects)
    return

def clear_features(s, num):
    global screen
    dirty_rects = []
    if s.game.before_fourth.status == False:
        dirty_rects.append(screen.blit(bg_gi, (14,676), pygame.Rect(14,676,83,69)))
    if s.game.before_fifth.status == False:
        dirty_rects.append(screen.blit(bg_gi, (631,679), pygame.Rect(631,679,83,69)))

    if s.game.selection_feature.position < 2:
        dirty_rects.append(screen.blit(bg_gi, (104,681), pygame.Rect(104,681,33,32)))
    if s.game.selection_feature.position < 3:
        dirty_rects.append(screen.blit(bg_gi, (144,681), pygame.Rect(144,681,33,32)))
    if s.game.selection_feature.position < 4:
        dirty_rects.append(screen.blit(bg_gi, (182,681), pygame.Rect(182,681,33,32)))
    if s.game.selection_feature.position < 5:
        dirty_rects.append(screen.blit(bg_gi, (215,679), pygame.Rect(215,679,40,40)))
    if s.game.selection_feature.position < 7:
        dirty_rects.append(screen.blit(bg_gi, (295,679), pygame.Rect(295,679,40,40)))
        if s.game.selection_feature_relay.status == False:
            dirty_rects.append(screen.blit(bg_gi, (114,720), pygame.Rect(114,720,118,42)))
            dirty_rects.append(screen.blit(bg_gi, (240,721), pygame.Rect(240,721,118,42)))
            dirty_rects.append(screen.blit(bg_gi, (368,721), pygame.Rect(368,721,118,42)))
            dirty_rects.append(screen.blit(bg_gi, (494,722), pygame.Rect(494,722,118,42)))
    if s.game.selection_feature.position < 6:
        dirty_rects.append(screen.blit(bg_gi, (256,679), pygame.Rect(256,679,40,40)))
    if s.game.selection_feature.position < 8:
        dirty_rects.append(screen.blit(bg_gi, (334,679), pygame.Rect(334,679,40,40)))
    if s.game.selection_feature.position < 9:
        dirty_rects.append(screen.blit(bg_gi, (374,679), pygame.Rect(374,679,40,40)))
    if s.game.selection_feature.position < 10:
        dirty_rects.append(screen.blit(bg_gi, (412,679), pygame.Rect(412,679,40,40)))
    if s.game.selection_feature.position < 11:
        dirty_rects.append(screen.blit(bg_gi, (453,679), pygame.Rect(453,679,40,40)))

    pygame.display.update(dirty_rects)

def draw_feature_animation(s, num):
    global screen
    dirty_rects = []
    if num in [4,15,10,21]:
        if s.game.before_fourth.status == False:
            p = [14,676]
            dirty_rects.append(screen.blit(before_fourth, p))
        if s.game.before_fifth.status == False and s.game.before_fourth.status == True:
            p = [631,679]
            dirty_rects.append(screen.blit(before_fourth, p))
        pygame.display.update(dirty_rects)
        return
   
    if num in [0,11,22]:
        if s.game.selection_feature.position < 2:
            p = [104,681]
            dirty_rects.append(screen.blit(s_arrow, p))
            pygame.display.update(dirty_rects)
            return
    if num in [9,20,23]:
        if s.game.selection_feature.position < 3:
            p = [144,681]
            dirty_rects.append(screen.blit(s_arrow, p))
            pygame.display.update(dirty_rects)
            return
    if num in [1,12,24]:
        if s.game.selection_feature.position < 4:
            p = [182,681]
            dirty_rects.append(screen.blit(s_arrow, p))
            pygame.display.update(dirty_rects)
            return
    if num in [2,13]:
        if s.game.selection_feature.position < 6:
            p = [215,679]
            dirty_rects.append(screen.blit(s_number, p))
            p = [295,679]
            dirty_rects.append(screen.blit(s_number, p))
            pygame.display.update(dirty_rects)
            return
    if num in [3,14,4,15]:
        if s.game.selection_feature.position < 7:
            p = [256,679]
            dirty_rects.append(screen.blit(s_number, p))
        if s.game.selection_feature_relay.status == False:
            p = [114,720]
            dirty_rects.append(screen.blit(select_feature, p))
            p = [240,721]
            dirty_rects.append(screen.blit(select_feature, p))
            p = [368,721]
            dirty_rects.append(screen.blit(select_feature, p))
            p = [494,722]
            dirty_rects.append(screen.blit(select_feature, p))
        pygame.display.update(dirty_rects)
        return
    if num in [5,16]:
        if s.game.selection_feature.position < 8:
            p = [334,679]
            dirty_rects.append(screen.blit(s_number, p))
        pygame.display.update(dirty_rects)
        return
    if num in [6,17]:
        if s.game.selection_feature.position < 9:
            p = [374,679]
            dirty_rects.append(screen.blit(s_number, p))
            pygame.display.update(dirty_rects)
            return
    if num in [7,18]:
        if s.game.selection_feature.position < 10:
            p = [412,679]
            dirty_rects.append(screen.blit(s_number, p))
            pygame.display.update(dirty_rects)
            return
    if num in [8,19]:
        if s.game.selection_feature.position < 11:
            p = [453,679]
            dirty_rects.append(screen.blit(s_number, p))
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

