
import pygame
import random

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

meter = pygame.image.load('graphics/assets/register_cover.png').convert()
card = pygame.image.load('dude_ranch/assets/card.png').convert_alpha()
c = pygame.image.load('dude_ranch/assets/corners.png').convert_alpha()
eb = pygame.image.load('dude_ranch/assets/eb.png').convert_alpha()
number_eb = pygame.image.load('dude_ranch/assets/eb_number.png').convert_alpha()
ebs = pygame.image.load('dude_ranch/assets/extra_balls.png').convert_alpha()
feature = pygame.image.load('dude_ranch/assets/feature.png').convert_alpha()
feature_arrow = pygame.image.load('dude_ranch/assets/feature_arrow.png').convert_alpha()
number = pygame.image.load('dude_ranch/assets/number.png').convert_alpha()
o1 = pygame.image.load('dude_ranch/assets/odds1.png').convert_alpha()
o2 = pygame.image.load('dude_ranch/assets/odds2.png').convert_alpha()
o3 = pygame.image.load('dude_ranch/assets/odds3.png').convert_alpha()
o4 = pygame.image.load('dude_ranch/assets/odds4.png').convert_alpha()
o5 = pygame.image.load('dude_ranch/assets/odds5.png').convert_alpha()
o6 = pygame.image.load('dude_ranch/assets/odds6.png').convert_alpha()
o7 = pygame.image.load('dude_ranch/assets/odds7.png').convert_alpha()
o8 = pygame.image.load('dude_ranch/assets/odds8.png').convert_alpha()
select_arrow = pygame.image.load('dude_ranch/assets/select_arrow.png').convert_alpha()
select_now = pygame.image.load('dude_ranch/assets/select_now.png').convert_alpha()
select_spots = pygame.image.load('dude_ranch/assets/select_spots.png').convert_alpha()
selector = pygame.image.load('dude_ranch/assets/selector.png').convert_alpha()
star = pygame.image.load('dude_ranch/assets/star.png').convert_alpha()
sc = pygame.image.load('dude_ranch/assets/super_card.png').convert_alpha()
sl1 = pygame.image.load('dude_ranch/assets/super_line1.png').convert_alpha()
sl2 = pygame.image.load('dude_ranch/assets/super_line2.png').convert_alpha()
tilt = pygame.image.load('dude_ranch/assets/tilt.png').convert_alpha()
red_number = pygame.image.load('dude_ranch/assets/red_number.png').convert_alpha()
bg_menu = pygame.image.load('dude_ranch/assets/dude_ranch_menu.png')
bg_gi = pygame.image.load('dude_ranch/assets/dude_ranch_gi.png')
bg_off = pygame.image.load('dude_ranch/assets/dude_ranch_off.png')

class scorereel():
    """ Score Reels are used to count replays """
    def __init__(self, pos, image):
        self.position = pos
        self.default_y = self.position[1]
        self.image = pygame.image.load(image).convert()

reel1 = scorereel([617,323], "graphics/assets/green_reel.png")
reel10 = scorereel([598,323], "graphics/assets/green_reel.png")
reel100 = scorereel([579,323], "graphics/assets/green_reel.png")

def display(s, replays=0, menu=False):
    
    meter.set_colorkey((255,0,252))
    meter_position = [569,323]

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

    if s.game.selector.position >= 1:
        c_pos = [72,439]
        screen.blit(card, c_pos)
    if s.game.selector.position == 2:
        c_pos = [508,441]
        screen.blit(card, c_pos)

    if s.game.super_card_trip.status == True:
        sc_pos = [219,312]
        screen.blit(sc, sc_pos)

    if s.game.extra_ball.position >= 1:
        eb_position = [86,994]
        screen.blit(number_eb, eb_position)
    if s.game.extra_ball.position >= 2:
        eb_position = [135,994]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 3:
        eb_position = [200,994]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 4:
        eb_position = [273,994]
        screen.blit(number_eb, eb_position)
    if s.game.extra_ball.position >= 5:
        eb_position = [321,994]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 6:
        eb_position = [386,994]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 7:
        eb_position = [460,994]
        screen.blit(number_eb, eb_position)
    if s.game.extra_ball.position >= 8:
        eb_position = [508,994]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 9:
        eb_position = [573,994]
        screen.blit(eb, eb_position)
    
    
    if s.game.odds.position > 0:
        if s.game.odds.position == 1:
            odds_position = [126,804]
            screen.blit(o1, odds_position)
        if s.game.odds.position == 2:
            odds_position = [217,803]
            screen.blit(o2, odds_position)
        if s.game.odds.position == 3:
            odds_position = [272,804]
            screen.blit(o3, odds_position)
        if s.game.odds.position == 4:
            odds_position = [311,811]
            screen.blit(o4, odds_position)
        if s.game.odds.position == 5:
            odds_position = [402,812]
            screen.blit(o5, odds_position)
        if s.game.odds.position == 6:
            odds_position = [449,822]
            screen.blit(o6, odds_position)
        if s.game.odds.position == 7:
            odds_position = [515,817]
            screen.blit(o7, odds_position)
        if s.game.odds.position == 8:
            odds_position = [593,818]
            screen.blit(o8, odds_position)

    if s.game.red_star.status == True:
        rs_position = [632,924]
        screen.blit(star, rs_position)

    if s.game.yellow_star.status == True:
        ys_position = [29,924]
        screen.blit(star, ys_position)

    if s.game.corners.status == True:
        corners_position = [69,298]
        screen.blit(c, corners_position)

    if s.game.tilt.status == False:
        if s.holes:
            if 1 in s.holes:
                number_position = [82,568]
                screen.blit(number, number_position)
                number_position = [478,612]
                screen.blit(number, number_position)
                number_position = [300,377]
                screen.blit(number, number_position)
            if 2 in s.holes:
                number_position = [124,652]
                screen.blit(number, number_position)
                number_position = [477,570]
                screen.blit(number, number_position)
            if 3 in s.holes:
                number_position = [206,486]
                screen.blit(number, number_position)
                number_position = [643,653]
                screen.blit(number, number_position)
            if 4 in s.holes:
                number_position = [163,652]
                screen.blit(number, number_position)
                number_position = [602,570]
                screen.blit(number, number_position)
                number_position = [344,418]
                screen.blit(number, number_position)
            if 5 in s.holes:
                number_position = [41,487]
                screen.blit(number, number_position)
                number_position = [560,653]
                screen.blit(number, number_position)
            if 6 in s.holes:
                number_position = [39,568]
                screen.blit(number, number_position)
                number_position = [644,489]
                screen.blit(number, number_position)
            if 7 in s.holes:
                number_position = [205,527]
                screen.blit(number, number_position)
                number_position = [519,651]
                screen.blit(number, number_position)
                number_position = [343,334]
                screen.blit(number, number_position)
            if 8 in s.holes:
                number_position = [41,528]
                screen.blit(number, number_position)
                number_position = [642,610]
                screen.blit(number, number_position)
            if 9 in s.holes:
                number_position = [124,487]
                screen.blit(number, number_position)
                number_position = [479,489]
                screen.blit(number, number_position)
            if 10 in s.holes:
                number_position = [123,527]
                screen.blit(number, number_position)
                number_position = [477,653]
                screen.blit(number, number_position)
                number_position = [342,377]
                screen.blit(number, number_position)
            if 11 in s.holes:
                number_position = [164,567]
                screen.blit(number, number_position)
                number_position = [561,611]
                screen.blit(number, number_position)
                number_position = [383,335]
                screen.blit(number, number_position)
            if 12 in s.holes:
                number_position = [41,651]
                screen.blit(number, number_position)
                number_position = [602,486]
                screen.blit(number, number_position)
            if 13 in s.holes:
                number_position = [205,609]
                screen.blit(number, number_position)
                number_position = [478,528]
                screen.blit(number, number_position)
                number_position = [384,376]
                screen.blit(number, number_position)
            if 14 in s.holes:
                number_position = [123,610]
                screen.blit(number, number_position)
                number_position = [560,529]
                screen.blit(number, number_position)
                number_position = [301,335]
                screen.blit(number, number_position)
            if 15 in s.holes:
                number_position = [205,649]
                screen.blit(number, number_position)
                number_position = [560,569]
                screen.blit(number, number_position)
            if 16 in s.holes:
                number_position = [123,567]
                screen.blit(number, number_position)
                number_position = [560,485]
                screen.blit(number, number_position)
            if 17 in s.holes:
                number_position = [205,569]
                screen.blit(number, number_position)
                number_position = [643,569]
                screen.blit(number, number_position)
                number_position = [301,419]
                screen.blit(number, number_position)
            if 18 in s.holes:
                number_position = [83,487]
                screen.blit(number, number_position)
                number_position = [520,569]
                screen.blit(number, number_position)
                number_position = [383,419]
                screen.blit(number, number_position)
            if 19 in s.holes:
                number_position = [165,528]
                screen.blit(number, number_position)
                number_position = [520,529]
                screen.blit(number, number_position)
            if 20 in s.holes:
                number_position = [165,609]
                screen.blit(number, number_position)
                number_position = [601,530]
                screen.blit(number, number_position)
            if 21 in s.holes:
                number_position = [82,610]
                screen.blit(number, number_position)
                number_position = [601,612]
                screen.blit(number, number_position)
            if 22 in s.holes:
                number_position = [83,528]
                screen.blit(number, number_position)
                number_position = [519,611]
                screen.blit(number, number_position)
            if 23 in s.holes:
                number_position = [82,651]
                screen.blit(number, number_position)
                number_position = [602,653]
                screen.blit(number, number_position)
            if 24 in s.holes:
                number_position = [41,610]
                screen.blit(number, number_position)
                number_position = [521,488]
                screen.blit(number, number_position)
            if 25 in s.holes:
                number_position = [165,487]
                screen.blit(number, number_position)
                number_position = [642,529]
                screen.blit(number, number_position)

    if s.game.tilt.status == True:
        tilt_position = [80,397]
        screen.blit(tilt, tilt_position)

    if s.game.spotted_numbers.position == 1:
        p = [39,719]
        screen.blit(select_arrow, p)
    if s.game.spotted_numbers.position == 2:
        p = [72,719]
        screen.blit(select_arrow, p)
    if s.game.spotted_numbers.position == 3:
        p = [107,719]
        screen.blit(select_arrow, p)
    if s.game.spotted_numbers.position == 4:
        p = [143,719]
        screen.blit(select_arrow, p)
    if s.game.spotted_numbers.position == 5:
        p = [176,719]
        screen.blit(select_arrow, p)
    if s.game.spotted_numbers.position >= 6:
        p = [213,703]
        screen.blit(selector, p)
    if s.game.spotted_numbers.position >= 7:
        p = [401,718]
        screen.blit(number, p)
    if s.game.spotted_numbers.position >= 8:
        p = [443,718]
        screen.blit(number, p)
    if s.game.spotted_numbers.position >= 9:
        p = [485,718]
        screen.blit(number, p)
    if s.game.spotted_numbers.position >= 10:
        p = [525,718]
        screen.blit(number, p)
    if s.game.spotted_numbers.position >= 11:
        p = [569,718]
        screen.blit(number, p)
    if s.game.spotted_numbers.position >= 12:
        p = [609,718]
        screen.blit(number, p)
    if s.game.spotted_numbers.position >= 13:
        p = [650,718]
        screen.blit(number, p)

    if s.game.spotted_numbers.position > 6:
        if s.game.ball_count.position == 3:
            s.cancel_delayed(name="blink")
            blink([s,1,1])
        else:
            s.cancel_delayed(name="blink")
    if s.game.feature.position > 5:
        if s.game.ball_count.position == 2:
            s.cancel_delayed(name="blink_select")
            blink_select([s,1,1])
        else:
            s.cancel_delayed(name="blink_select")

    if s.game.feature.position == 1:
        p = [278,537]
        screen.blit(feature_arrow, p)
    if s.game.feature.position == 2:
        p = [312,537]
        screen.blit(feature_arrow, p)
    if s.game.feature.position == 3:
        p = [347,537]
        screen.blit(feature_arrow, p)
    if s.game.feature.position == 4:
        p = [383,537]
        screen.blit(feature_arrow, p)
    if s.game.feature.position == 5:
        p = [416,537]
        screen.blit(feature_arrow, p)
    if s.game.feature.position == 6:
        p = [275,571]
        screen.blit(feature, p)

    if s.game.super_line1.status == True:
        p = [249,482]
        screen.blit(sl1, p)
    if s.game.super_line2.status == True:
        p = [367,481]
        screen.blit(sl2, p)

    if s.game.eb_play.status == True:
        ebs_position = [294,963]
        screen.blit(ebs, ebs_position)

    if s.game.spotted_numbers.position > 6:
        if s.game.ball_count.position < 4:
            if s.game.spotted_numbers.position >= 7:
                if s.game.spotted.position == 0:
                    #19
                    number_position = [165,528]
                    screen.blit(red_number, number_position)
                    number_position = [520,529]
                    screen.blit(red_number, number_position)
            if s.game.spotted_numbers.position >= 8:
                if s.game.spotted.position == 1:
                    #20
                    number_position = [165,609]
                    screen.blit(red_number, number_position)
                    number_position = [601,530]
                    screen.blit(red_number, number_position)
            if s.game.spotted_numbers.position >= 9:
                if s.game.spotted.position == 2:
                    #21
                    number_position = [82,610]
                    screen.blit(red_number, number_position)
                    number_position = [601,612]
                    screen.blit(red_number, number_position)
            if s.game.spotted_numbers.position >= 10:
                if s.game.spotted.position == 3:
                    #22
                    number_position = [83,528]
                    screen.blit(red_number, number_position)
                    number_position = [519,611]
                    screen.blit(red_number, number_position)
            if s.game.spotted_numbers.position >= 11:
                if s.game.spotted.position == 4:
                    #15
                    number_position = [205,649]
                    screen.blit(red_number, number_position)
                    number_position = [560,569]
                    screen.blit(red_number, number_position)
            if s.game.spotted_numbers.position >= 12:
                if s.game.spotted.position == 5:
                    #16
                    number_position = [123,567]
                    screen.blit(red_number, number_position)
                    number_position = [560,485]
                    screen.blit(red_number, number_position)
            if s.game.spotted_numbers.position >= 13:
                if s.game.spotted.position == 6:
                    #10
                    number_position = [123,527]
                    screen.blit(red_number, number_position)
                    number_position = [477,653]
                    screen.blit(red_number, number_position)
                    number_position = [342,377]
                    screen.blit(red_number, number_position)
                    
    pygame.display.update()

def blink_select(args):
    dirty_rects = []
    s = args[0]
    b = args[1]
    sl = args[2]

    if b == 0:
        if sl == 1:
            p = [278,661]
            dirty_rects.append(screen.blit(select_now, p))
        pygame.display.update(dirty_rects)
    else:
        dirty_rects.append(screen.blit(bg_gi, (278,661), pygame.Rect(278,661,176,37)))
        pygame.display.update(dirty_rects)
    b = not b

    args = [s,b,sl]

    s.delay(name="blink_select", delay=0.1, handler=blink_select, param=args)

def blink(args):
    dirty_rects = []
    s = args[0]
    b = args[1]
    sl = args[2]

    if b == 0:
        if sl == 1:
            p = [238,760]
            dirty_rects.append(screen.blit(select_spots, p))
        pygame.display.update(dirty_rects)
    else:
        dirty_rects.append(screen.blit(bg_gi, (238,760), pygame.Rect(238,760,152,32)))
        pygame.display.update(dirty_rects)
    b = not b

    args = [s,b,sl]

    s.delay(name="blink", delay=0.1, handler=blink, param=args)

def eb_animation(num):

    global screen
    if num == 9:
        eb_position = [86,994]
        screen.blit(number_eb, eb_position)
        pygame.display.update()
    if num == 8:
        eb_position = [135,994]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 7:
        eb_position = [200,994]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 6:
        eb_position = [273,994]
        screen.blit(number_eb, eb_position)
        pygame.display.update()
    if num == 5:
        eb_position = [321,994]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 4:
        eb_position = [386,994]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 3:
        eb_position = [460,994]
        screen.blit(number_eb, eb_position)
        pygame.display.update()
    if num == 2:
        eb_position = [508,994]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 1:
        eb_position = [573,994]
        screen.blit(eb, eb_position)
        pygame.display.update()


def feature_animation(num):
    global screen
    if num == 6:
        corners_position = [69,298]
        screen.blit(c, corners_position)
        pygame.display.update()

    if num == 5:
        rs_position = [632,924]
        screen.blit(star, rs_position)
        pygame.display.update()

    if num == 4:
        ys_position = [29,924]
        screen.blit(star, ys_position)
        pygame.display.update()

    if num == 3:
        p = [275,571]
        screen.blit(feature, p)
        pygame.display.update()
   
    if num == 2:
        p = [249,482]
        screen.blit(sl1, p)
        pygame.display.update()

    if num == 1:
        p = [367,481]
        screen.blit(sl2, p)
        pygame.display.update()


def odds_animation(num):

    global screen
    if num == 5:
        odds_position = [126,804]
        screen.blit(o1, odds_position)
        pygame.display.update()
    if num == 4:
        odds_position = [217,803]
        screen.blit(o2, odds_position)
        pygame.display.update()
    if num == 3:
        odds_position = [272,804]
        screen.blit(o3, odds_position)
        pygame.display.update()
    if num == 2:
        odds_position = [311,811]
        screen.blit(o4, odds_position)
        pygame.display.update()
    if num == 1:
        odds_position = [402,812]
        screen.blit(o5, odds_position)
        pygame.display.update()
