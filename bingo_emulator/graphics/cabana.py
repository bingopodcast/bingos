
import pygame
import random

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

meter = pygame.image.load('graphics/assets/silver_register_cover.png').convert()
sc_arrow = pygame.image.load('cabana/assets/sc_arrow.png').convert_alpha()
s_arrow = pygame.image.load('cabana/assets/spot_arrow.png').convert_alpha()
sc = pygame.image.load('cabana/assets/super_card.png').convert_alpha()
eb = pygame.image.load('cabana/assets/eb.png').convert_alpha()
extra_ball = pygame.image.load('cabana/assets/extra_ball.png').convert_alpha()
o1 = pygame.image.load('cabana/assets/odds1.png').convert_alpha()
o2 = pygame.image.load('cabana/assets/odds2.png').convert_alpha()
o3 = pygame.image.load('cabana/assets/odds3.png').convert_alpha()
o4 = pygame.image.load('cabana/assets/odds4.png').convert_alpha()
o5 = pygame.image.load('cabana/assets/odds5.png').convert_alpha()
o6 = pygame.image.load('cabana/assets/odds6.png').convert_alpha()
o7 = pygame.image.load('cabana/assets/odds7.png').convert_alpha()
o8 = pygame.image.load('cabana/assets/odds8.png').convert_alpha()
c = pygame.image.load('cabana/assets/corners.png').convert_alpha()
star = pygame.image.load('cabana/assets/rollover.png').convert_alpha()
number = pygame.image.load('cabana/assets/number.png').convert_alpha()
sc_number = pygame.image.load('cabana/assets/sc_number.png').convert_alpha()
tilt = pygame.image.load('cabana/assets/tilt.png').convert_alpha()
select_now = pygame.image.load('cabana/assets/select_now.png').convert_alpha()
before_fourth = pygame.image.load('cabana/assets/before_fourth.png').convert_alpha()
before_fifth = pygame.image.load('cabana/assets/before_fifth.png').convert_alpha()
red_number = pygame.image.load('cabana/assets/red_number.png').convert_alpha()
red_sc_number = pygame.image.load('cabana/assets/red_sc_number.png').convert_alpha()
select_number = pygame.image.load('cabana/assets/select_number.png').convert_alpha()
s_number = pygame.image.load('cabana/assets/spotted_numbers.png').convert_alpha()
bg_menu = pygame.image.load('cabana/assets/cabana_menu.png')
bg_gi = pygame.image.load('cabana/assets/cabana_gi.png')
bg_off = pygame.image.load('cabana/assets/cabana_off.png')

class scorereel():
    """ Score Reels are used to count replays """
    def __init__(self, pos, image):
        self.position = pos
        self.default_y = self.position[1]
        self.image = pygame.image.load(image).convert()

reel1 = scorereel([108,530], "graphics/assets/green_reel.png")
reel10 = scorereel([89,530], "graphics/assets/green_reel.png")
reel100 = scorereel([70,530], "graphics/assets/green_reel.png")

def display(s, replays=0, menu=False):
    
    meter.set_colorkey((255,0,252))
    meter_position = [60,528]

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
        p = [36,404]
        screen.blit(sc_arrow, p)
    if s.game.super_card.position == 2:
        p = [69,402]
        screen.blit(sc_arrow, p)
    if s.game.super_card.position == 3:
        p = [101,402]
        screen.blit(sc_arrow, p)
    if s.game.super_card.position == 4:
        p = [137,402]
        screen.blit(sc_arrow, p)
    if s.game.super_card.position == 5:
        p = [556,404]
        screen.blit(sc_arrow, p)
    if s.game.super_card.position == 6:
        p = [591,404]
        screen.blit(sc_arrow, p)
    if s.game.super_card.position == 7:
        p = [623,404]
        screen.blit(sc_arrow, p)
    if s.game.super_card.position == 8:
        p = [658,405]
        screen.blit(sc_arrow, p)

    if s.game.super_card.position >= 4:
        p = [31,364]
        screen.blit(sc, p)

    if s.game.super_card.position >= 8:
        p = [552,365]
        screen.blit(sc, p)

    if s.game.extra_ball.position == 1 or s.game.extra_ball.position == 10 or s.game.extra_ball.position == 19:
        eb_position = [106,1014]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 2 or s.game.extra_ball.position == 11 or s.game.extra_ball.position == 20:
        eb_position = [166,1015]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 3 or s.game.extra_ball.position == 12 or s.game.extra_ball.position == 21:
        eb_position = [225,1015]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 4 or s.game.extra_ball.position == 13 or s.game.extra_ball.position == 22:
        eb_position = [283,1013]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 5 or s.game.extra_ball.position == 14 or s.game.extra_ball.position == 23:
        eb_position = [342,1012]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 6 or s.game.extra_ball.position == 15:
        eb_position = [401,1013]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 7 or s.game.extra_ball.position == 16:
        eb_position = [461,1012]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 8 or s.game.extra_ball.position == 17:
        eb_position = [520,1013]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 9 or s.game.extra_ball.position == 18:
        eb_position = [578,1013]
        screen.blit(eb, eb_position)
    
    if s.game.extra_ball.position >= 9 and s.game.extra_ball.position < 18:
        eb_pos = [105,1062]
        screen.blit(extra_ball, eb_pos)
    if s.game.extra_ball.position >= 18 and s.game.extra_ball.position < 24:
        eb_pos = [285,1062]
        screen.blit(extra_ball, eb_pos)
    if s.game.extra_ball.position == 24:
        eb_pos = [458,1061]
        screen.blit(extra_ball, eb_pos)

    
    if s.game.odds.position > 0:
        if s.game.odds.position == 1:
            odds_position = [193,739]
            screen.blit(o1, odds_position)
        if s.game.odds.position == 2:
            odds_position = [252,735]
            screen.blit(o2, odds_position)
        if s.game.odds.position == 3:
            odds_position = [286,785]
            screen.blit(o3, odds_position)
        if s.game.odds.position == 4:
            odds_position = [346,730]
            screen.blit(o4, odds_position)
        if s.game.odds.position == 5:
            odds_position = [395,790]
            screen.blit(o5, odds_position)
        if s.game.odds.position == 6:
            odds_position = [446,727]
            screen.blit(o6, odds_position)
        if s.game.odds.position == 7:
            odds_position = [482,801]
            screen.blit(o7, odds_position)
        if s.game.odds.position == 8:
            odds_position = [502,726]
            screen.blit(o8, odds_position)

    if s.game.red_star.status == True:
        rs_position = [636,1008]
        screen.blit(star, rs_position)

    if s.game.yellow_star.status == True:
        ys_position = [8,1011]
        screen.blit(star, ys_position)

    if s.game.corners.status == True:
        corners_position = [567,515]
        screen.blit(c, corners_position)

    if s.game.tilt.status == False:
        if s.holes:
            if 1 in s.holes:
                number_position = [219,453]
                screen.blit(number, number_position)
                number_position = [549,255]
                screen.blit(sc_number, number_position)
            if 2 in s.holes:
                number_position = [219,387]
                screen.blit(number, number_position)
            if 3 in s.holes:
                number_position = [449,518]
                screen.blit(number, number_position)
                number_position = [77,197]
                screen.blit(sc_number, number_position)
            if 4 in s.holes:
                number_position = [277,256]
                screen.blit(number, number_position)
                number_position = [599,310]
                screen.blit(sc_number, number_position)
            if 5 in s.holes:
                number_position = [334,518]
                screen.blit(number, number_position)
            if 6 in s.holes:
                number_position = [448,254]
                screen.blit(number, number_position)
            if 7 in s.holes:
                number_position = [277,518]
                screen.blit(number, number_position)
                number_position = [598,199]
                screen.blit(sc_number, number_position)
            if 8 in s.holes:
                number_position = [449,321]
                screen.blit(number, number_position)
            if 9 in s.holes:
                number_position = [219,254]
                screen.blit(number, number_position)
                number_position = [26,254]
                screen.blit(sc_number, number_position)
            if 10 in s.holes:
                number_position = [219,320]
                screen.blit(number, number_position)
                number_position = [600,256]
                screen.blit(sc_number, number_position)
            if 11 in s.holes:
                number_position = [219,519]
                screen.blit(number, number_position)
                number_position = [646,201]
                screen.blit(sc_number, number_position)
                number_position = [127,254]
                screen.blit(sc_number, number_position)
            if 12 in s.holes:
                number_position = [391,386]
                screen.blit(number, number_position)
                number_position = [27,309]
                screen.blit(sc_number, number_position)
            if 13 in s.holes:
                number_position = [334,452]
                screen.blit(number, number_position)
                number_position = [648,256]
                screen.blit(sc_number, number_position)
            if 14 in s.holes:
                number_position = [335,321]
                screen.blit(number, number_position)
                number_position = [127,307]
                screen.blit(sc_number, number_position)
            if 15 in s.holes:
                number_position = [334,255]
                screen.blit(number, number_position)
                number_position = [549,199]
                screen.blit(sc_number, number_position)
            if 16 in s.holes:
                number_position = [334,387]
                screen.blit(number, number_position)
            if 17 in s.holes:
                number_position = [449,453]
                screen.blit(number, number_position)
                number_position = [549,310]
                screen.blit(sc_number, number_position)
            if 18 in s.holes:
                number_position = [278,386]
                screen.blit(number, number_position)
                number_position = [129,198]
                screen.blit(sc_number, number_position)
                number_position = [649,311]
                screen.blit(sc_number, number_position)
            if 19 in s.holes:
                number_position = [278,320]
                screen.blit(number, number_position)
            if 20 in s.holes:
                number_position = [392,321]
                screen.blit(number, number_position)
            if 21 in s.holes:
                number_position = [392,451]
                screen.blit(number, number_position)
            if 22 in s.holes:
                number_position = [278,452]
                screen.blit(number, number_position)
            if 23 in s.holes:
                number_position = [392,518]
                screen.blit(number, number_position)
                number_position = [27,197]
                screen.blit(sc_number, number_position)
            if 24 in s.holes:
                number_position = [392,255]
                screen.blit(number, number_position)
                number_position = [77,309]
                screen.blit(sc_number, number_position)
            if 25 in s.holes:
                number_position = [450,387]
                screen.blit(number, number_position)
                number_position = [78,254]
                screen.blit(sc_number, number_position)

    if s.game.tilt.status == True:
        tilt_position = [57,628]
        screen.blit(tilt, tilt_position)

    if s.game.selection_feature.position == 1:
        p = [187,602]
        screen.blit(s_arrow, p)
    if s.game.selection_feature.position == 2:
        p = [228,602]
        screen.blit(s_arrow, p)
    if s.game.selection_feature.position == 3:
        p = [266,602]
        screen.blit(s_arrow, p)
    if s.game.selection_feature.position >= 4:
        p = [307,601]
        screen.blit(s_arrow, p)
        p = [326,596]
        screen.blit(select_number, p)
    if s.game.selection_feature.position >= 5:
        p = [206,644]
        screen.blit(s_number, p)
    if s.game.selection_feature.position >= 6:
        p = [250,646]
        screen.blit(s_number, p)
    if s.game.selection_feature.position >= 7:
        p = [296,644]
        screen.blit(s_number, p)
    if s.game.selection_feature.position >= 8:
        p = [340,646]
        screen.blit(s_number, p)
    if s.game.selection_feature.position >= 9:
        p = [384,646]
        screen.blit(s_number, p)
    if s.game.selection_feature.position >= 10:
        p = [428,647]
        screen.blit(s_number, p)
    if s.game.selection_feature.position >= 11:
        p = [472,646]
        screen.blit(s_number, p)

    if s.game.select_spots.status == True and s.game.before_fourth.status == True:
        if s.game.ball_count.position == 3:
            s.cancel_delayed(name="blink")
            blink([s,1,1])
        else:
            s.cancel_delayed(name="blink")
    
    if s.game.select_spots.status == True and s.game.before_fifth.status == True:
        if s.game.ball_count.position == 4:
            s.cancel_delayed(name="blink")
            blink([s,1,1])
        else:
            s.cancel_delayed(name="blink")

    if s.game.before_fourth.status == True and s.game.selection_feature.position > 3:
        p = [14,673]
        screen.blit(before_fourth, p)
    if s.game.before_fifth.status == True and s.game.selection_feature.position > 3:
        p = [552,672]
        screen.blit(before_fifth, p)

    if s.game.select_spots.status == True:
        if s.game.before_fourth.status == True:
            if s.game.ball_count.position < 4:
                if s.game.selection_feature.position >= 5:
                    if s.game.spotted.position == 0:
                        #19
                        number_position = [278,320]
                        screen.blit(red_number, number_position)
                if s.game.selection_feature.position >= 6:
                    if s.game.spotted.position == 1:
                        #20
                        number_position = [392,321]
                        screen.blit(red_number, number_position)
                if s.game.selection_feature.position >= 7:
                    if s.game.spotted.position == 2:
                        #21
                        number_position = [392,451]
                        screen.blit(red_number, number_position)
                if s.game.selection_feature.position >= 8:
                    if s.game.spotted.position == 3:
                        #22
                        number_position = [278,452]
                        screen.blit(red_number, number_position)
                if s.game.selection_feature.position >= 9:
                    if s.game.spotted.position == 4:
                        #16
                        number_position = [334,387]
                        screen.blit(red_number, number_position)
                if s.game.selection_feature.position >= 10:
                    if s.game.spotted.position == 5:
                        #25
                        number_position = [450,387]
                        screen.blit(red_number, number_position)
                        number_position = [78,254]
                        screen.blit(red_sc_number, number_position)
                if s.game.selection_feature.position >= 11:
                    if s.game.spotted.position == 6:
                        #10
                        number_position = [219,320]
                        screen.blit(red_number, number_position)
                        number_position = [600,256]
                        screen.blit(red_sc_number, number_position)
        if s.game.before_fifth.status == True:
            if s.game.ball_count.position < 5:
                if s.game.selection_feature.position >= 5:
                    if s.game.spotted.position == 0:
                        #19
                        number_position = [278,320]
                        screen.blit(red_number, number_position)
                if s.game.selection_feature.position >= 6:
                    if s.game.spotted.position == 1:
                        #20
                        number_position = [392,321]
                        screen.blit(red_number, number_position)
                if s.game.selection_feature.position >= 7:
                    if s.game.spotted.position == 2:
                        #21
                        number_position = [392,451]
                        screen.blit(red_number, number_position)
                if s.game.selection_feature.position >= 8:
                    if s.game.spotted.position == 3:
                        #22
                        number_position = [278,452]
                        screen.blit(red_number, number_position)
                if s.game.selection_feature.position >= 9:
                    if s.game.spotted.position == 4:
                        #16
                        number_position = [334,387]
                        screen.blit(red_number, number_position)
                if s.game.selection_feature.position >= 10:
                    if s.game.spotted.position == 5:
                        #25
                        number_position = [450,387]
                        screen.blit(red_number, number_position)
                        number_position = [78,254]
                        screen.blit(red_sc_number, number_position)
                if s.game.selection_feature.position >= 11:
                    if s.game.spotted.position == 6:
                        #10
                        number_position = [219,320]
                        screen.blit(red_number, number_position)
                        number_position = [600,256]
                        screen.blit(red_sc_number, number_position)
                
    pygame.display.update()

def blink(args):
    dirty_rects = []
    s = args[0]
    b = args[1]
    sn = args[2]

    if b == 0:
        if sn == 1:
            p = [426,598]
            dirty_rects.append(screen.blit(select_now, p))
        pygame.display.update(dirty_rects)
    else:
        dirty_rects.append(screen.blit(bg_gi, (426,598), pygame.Rect(426,598,113,43)))
        pygame.display.update(dirty_rects)
    b = not b

    args = [s,b,sn]

    s.delay(name="blink", delay=0.1, handler=blink, param=args)

def eb_animation(num):
    global screen
    if num == 9:
        eb_position = [578,1013]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 8:
        eb_position = [520,1013]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 7:
        eb_position = [461,1012]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 6:
        eb_position = [401,1013]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 5:
        eb_position = [342,1012]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 4:
        eb_position = [283,1013]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 3:
        eb_position = [225,1015]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 2:
        eb_position = [166,1015]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 1:
        eb_position = [106,1014]
        screen.blit(eb, eb_position)
        pygame.display.update()


def feature_animation(num):
    global screen
    if num == 6:
        corners_position = [567,515]
        screen.blit(c, corners_position)
        pygame.display.update()

    if num == 5:
        rs_position = [636,1008]
        screen.blit(star, rs_position)
        pygame.display.update()

    if num == 4:
        ys_position = [8,1011]
        screen.blit(star, ys_position)
        pygame.display.update()

    if num == 3:
        p = [36,404]
        screen.blit(sc_arrow, p)
        pygame.display.update()

    if num == 2:
        p = [31,364]
        screen.blit(sc, p)
        pygame.display.update()

    if num == 1:
        p = [552,365]
        screen.blit(sc, p)
        pygame.display.update()


def odds_animation(num):
    global screen
    if num == 5:
        odds_position = [193,739]
        o = pygame.image.load('cabana/assets/odds1.png').convert_alpha()
        screen.blit(o, odds_position)
        pygame.display.update()
    if num == 4:
        odds_position = [252,735]
        o = pygame.image.load('cabana/assets/odds2.png').convert_alpha()
        screen.blit(o, odds_position)
        pygame.display.update()
    if num == 3:
        odds_position = [286,785]
        o = pygame.image.load('cabana/assets/odds3.png').convert_alpha()
        screen.blit(o, odds_position)
        pygame.display.update()
    if num == 2:
        odds_position = [346,730]
        o = pygame.image.load('cabana/assets/odds4.png').convert_alpha()
        screen.blit(o, odds_position)
        pygame.display.update()
    if num == 1:
        odds_position = [395,790]
        o = pygame.image.load('cabana/assets/odds5.png').convert_alpha()
        screen.blit(o, odds_position)
        pygame.display.update()
