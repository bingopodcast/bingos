
import pygame
import random

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

meter = pygame.image.load('graphics/assets/register_cover.png').convert()
arrow = pygame.image.load('big_time/assets/arrow.png').convert_alpha()
sc = pygame.image.load('big_time/assets/sc.png').convert_alpha()
eb = pygame.image.load('big_time/assets/eb.png').convert_alpha()
ebs = pygame.image.load('big_time/assets/extra_balls.png').convert_alpha()
number_eb = pygame.image.load('big_time/assets/eb_number.png').convert_alpha()
o1 = pygame.image.load('big_time/assets/odds1.png').convert_alpha()
o2 = pygame.image.load('big_time/assets/odds2.png').convert_alpha()
o3 = pygame.image.load('big_time/assets/odds3.png').convert_alpha()
o4 = pygame.image.load('big_time/assets/odds4.png').convert_alpha()
o5 = pygame.image.load('big_time/assets/odds5.png').convert_alpha()
o6 = pygame.image.load('big_time/assets/odds6.png').convert_alpha()
o7 = pygame.image.load('big_time/assets/odds7.png').convert_alpha()
o8 = pygame.image.load('big_time/assets/odds8.png').convert_alpha()
c = pygame.image.load('big_time/assets/corners.png').convert_alpha()
star = pygame.image.load('big_time/assets/star.png').convert_alpha()
number = pygame.image.load('big_time/assets/number.png').convert_alpha()
sc_number = pygame.image.load('big_time/assets/sc_number.png').convert_alpha()
tilt = pygame.image.load('big_time/assets/tilt.png').convert_alpha()
sc_arrow = pygame.image.load('big_time/assets/sc_arrow.png').convert_alpha()
time = pygame.image.load('big_time/assets/time.png').convert_alpha()
magic_lines = pygame.image.load('big_time/assets/magic_lines.png').convert_alpha()
magic_lines4 = pygame.image.load('big_time/assets/magic_line4.png').convert_alpha()
select_now = pygame.image.load('big_time/assets/select_now.png').convert_alpha()
line1 = pygame.image.load('big_time/assets/line1.png').convert_alpha()
line2 = pygame.image.load('big_time/assets/line2.png').convert_alpha()
line3 = pygame.image.load('big_time/assets/line3.png').convert_alpha()
line4 = pygame.image.load('big_time/assets/line4.png').convert_alpha()
line5 = pygame.image.load('big_time/assets/line5.png').convert_alpha()

class scorereel():
    """ Score Reels are used to count replays """
    def __init__(self, pos, image):
        self.position = pos
        self.default_y = self.position[1]
        self.image = pygame.image.load(image).convert()

reel1 = scorereel([92,328], "graphics/assets/white_reel.png")
reel10 = scorereel([73,328], "graphics/assets/white_reel.png")
reel100 = scorereel([53,328], "graphics/assets/white_reel.png")

def display(s, replays=0, menu=False):
    
    meter.set_colorkey((255,0,252))
    meter_position = [44,328]

    screen.blit(reel1.image, reel1.position)
    screen.blit(reel10.image, reel10.position)
    screen.blit(reel100.image, reel100.position)
    screen.blit(meter, meter_position)

    if s.game.line1.position == 0:
        line1_position = [233,373]
    elif s.game.line1.position == 1:
        line1_position = [233,419]
    elif s.game.line1.position == 2:
        line1_position = [233,328]
    
    screen.blit(line1, line1_position)

    if s.game.line2.position == 0:
        line2_position = [286,373]
    elif s.game.line2.position == 1:
        line2_position = [286,419]
    elif s.game.line2.position == 2:
        line2_position = [286,328]
    
    screen.blit(line2, line2_position)

    if s.game.line3.position == 0:
        line3_position = [339,373]
    elif s.game.line3.position == 1:
        line3_position = [339,419]
    elif s.game.line3.position == 2:
        line3_position = [339,331]
    
    screen.blit(line3, line3_position)

    if s.game.line4.position == 0:
        line4_position = [395,357]
    elif s.game.line4.position == 1:
        line4_position = [395,412]
    elif s.game.line4.position == 2:
        line4_position = [395,310]
    
    screen.blit(line4, line4_position)

    if s.game.line5.position == 0:
        line5_position = [447,357]
    elif s.game.line5.position == 1:
        line5_position = [447,412]
    elif s.game.line5.position == 2:
        line5_position = [447,310]
    
    screen.blit(line5, line5_position)

    backglass_position = [0, 0]
    backglass = pygame.Surface(screen.get_size(), flags=pygame.SRCALPHA)
    backglass.fill((0, 0, 0))
    if menu == True:
        backglass = pygame.image.load('big_time/assets/big_time_menu.png').convert()
        backglass.set_colorkey((255,0,252))
    else:
        if (s.game.anti_cheat.status == True):
            backglass = pygame.image.load('big_time/assets/big_time_gi.png').convert()
            backglass.set_colorkey((255,0,252))
        else:
            backglass = pygame.image.load('big_time/assets/big_time_off.png').convert()
            backglass.set_colorkey((255,0,252))
    backglass = pygame.transform.scale(backglass, (720, 1280))
    
    screen.blit(backglass, backglass_position)

    if s.game.super_card.position == 1:
        p = [42,544]
        screen.blit(sc_arrow, p)
    if s.game.super_card.position == 2:
        p = [76,545]
        screen.blit(sc_arrow, p)
    if s.game.super_card.position == 3:
        p = [110,545]
        screen.blit(sc_arrow, p)
    if s.game.super_card.position == 4:
        p = [144,545]
        screen.blit(sc_arrow, p)
    if s.game.super_card.position == 5:
        p = [552,545]
        screen.blit(sc_arrow, p)
    if s.game.super_card.position == 6:
        p = [586,545]
        screen.blit(sc_arrow, p)
    if s.game.super_card.position == 7:
        p = [620,545]
        screen.blit(sc_arrow, p)
    if s.game.super_card.position == 8:
        p = [652,545]
        screen.blit(sc_arrow, p)

    if s.game.super_card.position >= 4:
        p = [54,574]
        screen.blit(sc, p)

    if s.game.super_card.position >= 8:
        p = [566,572]
        screen.blit(sc, p)

    if s.game.extra_ball.position >= 1:
        eb_position = [142,986]
        screen.blit(number_eb, eb_position)
    if s.game.extra_ball.position >= 2:
        eb_position = [192,986]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 3:
        eb_position = [258,986]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 4:
        eb_position = [332,983]
        screen.blit(number_eb, eb_position)
    if s.game.extra_ball.position >= 5:
        eb_position = [380,985]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 6:
        eb_position = [447,985]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 7:
        eb_position = [518,982]
        screen.blit(number_eb, eb_position)
    if s.game.extra_ball.position >= 8:
        eb_position = [568,984]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 9:
        eb_position = [635,984]
        screen.blit(eb, eb_position)


    if s.game.odds.position > 0:
        if s.game.odds.position == 1:
            odds_position = [82,873]
            screen.blit(o1, odds_position)
        if s.game.odds.position == 2:
            odds_position = [154,870]
            screen.blit(o2, odds_position)
        if s.game.odds.position == 3:
            odds_position = [220,872]
            screen.blit(o3, odds_position)
        if s.game.odds.position == 4:
            odds_position = [291,876]
            screen.blit(o4, odds_position)
        if s.game.odds.position == 5:
            odds_position = [362,873]
            screen.blit(o5, odds_position)
        if s.game.odds.position == 6:
            odds_position = [429,871]
            screen.blit(o6, odds_position)
        if s.game.odds.position == 7:
            odds_position = [498,873]
            screen.blit(o7, odds_position)
        if s.game.odds.position == 8:
            odds_position = [564,872]
            screen.blit(o8, odds_position)

    if s.game.red_star.status == True:
        rs_position = [648,916]
        screen.blit(star, rs_position)

    if s.game.yellow_star.status == True:
        ys_position = [6,925]
        screen.blit(star, ys_position)

    if s.game.corners.status == True:
        corners_position = [17,750]
        screen.blit(c, corners_position)

    if s.game.tilt.status == False:
        if s.holes:
            if 1 in s.holes:
                if s.game.line1.position == 0:
                    number_position = [233,570]
                    screen.blit(number, number_position)
                elif s.game.line1.position == 1:
                    number_position = [233,618]
                    screen.blit(number, number_position)
                elif s.game.line1.position == 2:
                    number_position = [233,519]
                    screen.blit(number, number_position)
                number_position = [552,649]
                screen.blit(sc_number, number_position)
            if 2 in s.holes:
                if s.game.line1.position == 0:
                    number_position = [233,519]
                    screen.blit(number, number_position)
                elif s.game.line1.position == 1:
                    number_position = [233,568]
                    screen.blit(number, number_position)
                elif s.game.line1.position == 2:
                    number_position = [233,468]
                    screen.blit(number, number_position)
            if 3 in s.holes:
                if s.game.line5.position == 0:
                    n = [444,618]
                    screen.blit(number, n)
                elif s.game.line5.position == 1:
                    n = [444,416]
                    screen.blit(number, n)
                elif s.game.line5.position == 2:
                    n = [443,567]
                    screen.blit(number, n)
                number_position = [86,606]
                screen.blit(sc_number, number_position)
            if 4 in s.holes:
                if s.game.line2.position == 0:
                    number_position = [284,416]
                    screen.blit(number, number_position)
                elif s.game.line2.position == 1:
                    number_position = [284,467]
                    screen.blit(number, number_position)
                elif s.game.line2.position == 2:
                    number_position = [284,617]
                    screen.blit(number, number_position)
                number_position = [596,691]
                screen.blit(sc_number, number_position)
            if 5 in s.holes:
                if s.game.line3.position == 0:
                    number_position = [338,617]
                    screen.blit(number, number_position)
                elif s.game.line3.position == 1:
                    number_position = [338,416]
                    screen.blit(number, number_position)
                elif s.game.line3.position == 2:
                    number_position = [338,567]
                    screen.blit(number, number_position)
            if 6 in s.holes:
                if s.game.line5.position == 0:
                    n = [444,415]
                    screen.blit(number, n)
                elif s.game.line5.position == 1:
                    n = [444,467]
                    screen.blit(number, n)
                elif s.game.line5.position == 2:
                    n = [444,617]
                    screen.blit(number, n)
            if 7 in s.holes:
                if s.game.line2.position == 0:
                    number_position = [284,618]
                    screen.blit(number, number_position)
                elif s.game.line2.position == 1:
                    number_position = [284,416]
                    screen.blit(number, number_position)
                elif s.game.line2.position == 2:
                    number_position = [284,568]
                    screen.blit(number, number_position)
                number_position = [597,607]
                screen.blit(sc_number, number_position)
            if 8 in s.holes:
                if s.game.line5.position == 0:
                    n = [444,466]
                    screen.blit(number, n)
                elif s.game.line5.position == 1:
                    n = [444,518]
                    screen.blit(number, n)
                elif s.game.line5.position == 2:
                    n = [444,415]
                    screen.blit(number, n)
            if 9 in s.holes:
                if s.game.line1.position == 0:
                    number_position = [230,414]
                    screen.blit(number, number_position)
                elif s.game.line1.position == 1:
                    number_position = [230,468]
                    screen.blit(number, number_position)
                elif s.game.line1.position == 2:
                    number_position = [230,617]
                    screen.blit(number, number_position)
                number_position = [39,651]
                screen.blit(sc_number, number_position)
            if 10 in s.holes:
                if s.game.line1.position == 0:
                    number_position = [230,466]
                    screen.blit(number, number_position)
                elif s.game.line1.position == 1:
                    number_position = [230,518]
                    screen.blit(number, number_position)
                elif s.game.line1.position == 2:
                    number_position = [230,415]
                    screen.blit(number, number_position)
                number_position = [596,650]
                screen.blit(sc_number, number_position)
            if 11 in s.holes:
                if s.game.line1.position == 0:
                    number_position = [230,618]
                    screen.blit(number, number_position)
                elif s.game.line1.position == 1:
                    number_position = [230,416]
                    screen.blit(number, number_position)
                elif s.game.line1.position == 2:
                    number_position = [230,567]
                    screen.blit(number, number_position)
                number_position = [133,651]
                screen.blit(sc_number, number_position)
                number_position = [642,606]
                screen.blit(sc_number, number_position)
            if 12 in s.holes:
                if s.game.line4.position == 0:
                    n = [390,518]
                    screen.blit(number, n)
                elif s.game.line4.position == 1:
                    n = [390,568]
                    screen.blit(number, n)
                elif s.game.line4.position == 2:
                    n = [390,468]
                    screen.blit(number, n)
                number_position = [40,694]
                screen.blit(sc_number, number_position)
            if 13 in s.holes:
                if s.game.line3.position == 0:
                    number_position = [337,568]
                    screen.blit(number, number_position)
                elif s.game.line3.position == 1:
                    number_position = [337,617]
                    screen.blit(number, number_position)
                elif s.game.line3.position == 2:
                    number_position = [337,517]
                    screen.blit(number, number_position)
                number_position = [643,649]
                screen.blit(sc_number, number_position)
            if 14 in s.holes:
                if s.game.line3.position == 0:
                    number_position = [337,467]
                    screen.blit(number, number_position)
                elif s.game.line3.position == 1:
                    number_position = [337,518]
                    screen.blit(number, number_position)
                elif s.game.line3.position == 2:
                    number_position = [337,415]
                    screen.blit(number, number_position)
                number_position = [133,693]
                screen.blit(sc_number, number_position)
            if 15 in s.holes:
                if s.game.line3.position == 0:
                    number_position = [337,415]
                    screen.blit(number, number_position)
                elif s.game.line3.position == 1:
                    number_position = [337,467]
                    screen.blit(number, number_position)
                elif s.game.line3.position == 2:
                    number_position = [337,617]
                    screen.blit(number, number_position)
                number_position = [552,607]
                screen.blit(sc_number, number_position)
            if 16 in s.holes:
                if s.game.line3.position == 0:
                    number_position = [337,516]
                    screen.blit(number, number_position)
                elif s.game.line3.position == 1:
                    number_position = [337,566]
                    screen.blit(number, number_position)
                elif s.game.line3.position == 2:
                    number_position = [337,465]
                    screen.blit(number, number_position)
            if 17 in s.holes:
                if s.game.line5.position == 0:
                    n = [442,566]
                    screen.blit(number, n)
                elif s.game.line5.position == 1:
                    n = [442,618]
                    screen.blit(number, n)
                elif s.game.line5.position == 2:
                    n = [443,516]
                    screen.blit(number, n)
                number_position = [552,690]
                screen.blit(sc_number, number_position)
            if 18 in s.holes:
                if s.game.line2.position == 0:
                    number_position = [284,517]
                    screen.blit(number, number_position)
                elif s.game.line2.position == 1:
                    number_position = [284,568]
                    screen.blit(number, number_position)
                elif s.game.line2.position == 2:
                    number_position = [284,466]
                    screen.blit(number, number_position)
                number_position = [132,608]
                screen.blit(sc_number, number_position)
                number_position = [642,690]
                screen.blit(sc_number, number_position)
            if 19 in s.holes:
                if s.game.line2.position == 0:
                    number_position = [284,466]
                    screen.blit(number, number_position)
                elif s.game.line2.position == 1:
                    number_position = [284,517]
                    screen.blit(number, number_position)
                elif s.game.line2.position == 2:
                    number_position = [284,416]
                    screen.blit(number, number_position)
            if 20 in s.holes:
                if s.game.line4.position == 0:
                    n = [390,467]
                    screen.blit(number, n)
                elif s.game.line4.position == 1:
                    n = [390,517]
                    screen.blit(number, n)
                elif s.game.line4.position == 2:
                    n = [390,416]
                    screen.blit(number, n)
            if 21 in s.holes:
                if s.game.line4.position == 0:
                    n = [390,568]
                    screen.blit(number, n)
                elif s.game.line4.position == 1:
                    n = [390,616]
                    screen.blit(number, n)
                elif s.game.line4.position == 2:
                    n = [390,517]
                    screen.blit(number, n)
            if 22 in s.holes:
                if s.game.line2.position == 0:
                    number_position = [285,568]
                    screen.blit(number, number_position)
                elif s.game.line2.position == 1:
                    number_position = [285,617]
                    screen.blit(number, number_position)
                elif s.game.line2.position == 2:
                    number_position = [285,518]
                    screen.blit(number, number_position)
            if 23 in s.holes:
                if s.game.line4.position == 0:
                    n = [390,617]
                    screen.blit(number, n)
                elif s.game.line4.position == 1:
                    n = [390,416]
                    screen.blit(number, n)
                elif s.game.line4.position == 2:
                    n = [390,567]
                    screen.blit(number, n)
                number_position = [39,608]
                screen.blit(sc_number, number_position)
            if 24 in s.holes:
                if s.game.line4.position == 0:
                    n = [390,416]
                    screen.blit(number, n)
                elif s.game.line4.position == 1:
                    n = [390,468]
                    screen.blit(number, n)
                elif s.game.line4.position == 2:
                    n = [390,617]
                    screen.blit(number, n)
                number_position = [88,694]
                screen.blit(sc_number, number_position)
            if 25 in s.holes:
                if s.game.line5.position == 0:
                    n = [444,517]
                    screen.blit(number, n)
                elif s.game.line5.position == 1:
                    n = [444,567]
                    screen.blit(number, n)
                elif s.game.line5.position == 2:
                    n = [444,466]
                    screen.blit(number, n)
                number_position = [88,650]
                screen.blit(sc_number, number_position)

    if s.game.before_fourth.status == True and s.game.magic_lines_feature.position >= 4:
        p = [540,747]
        screen.blit(time, p)
        if s.game.ball_count.position == 3:
            p = [556,793]
            screen.blit(select_now, p)
    elif s.game.before_fifth.status == True and s.game.magic_lines_feature.position >= 4:
        p = [627,747]
        screen.blit(time, p)
        if s.game.ball_count.position == 4:
            p = [556,793]
            screen.blit(select_now, p)

    if s.game.tilt.status == True:
        tilt_position = [51,279]
        screen.blit(tilt, tilt_position)

    if s.game.eb_play.status == True:
        ebs_position = [26,990]
        screen.blit(ebs, ebs_position)

    if s.game.magic_lines_feature.position == 1:
        p = [78,793]
        screen.blit(arrow, p)
    elif s.game.magic_lines_feature.position == 2:
        p = [114,793]
        screen.blit(arrow, p)
    elif s.game.magic_lines_feature.position == 3:
        p = [148,793]
        screen.blit(arrow, p)
    elif s.game.magic_lines_feature.position == 4:
        p = [182,793]
        screen.blit(arrow, p)
        p = [206,792]
        screen.blit(magic_lines4, p)
    elif s.game.magic_lines_feature.position == 5:
        p = [314,792]
        screen.blit(magic_lines4, p)
    elif s.game.magic_lines_feature.position == 6:
        p = [420,792]
        screen.blit(magic_lines4, p)
                
    pygame.display.update()

def eb_animation(num):
    global screen
    if num == 9:
        eb_position = [142,986]
        screen.blit(number_eb, eb_position)
        pygame.display.update()
    if num == 8:
        eb_position = [192,986]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 7:
        eb_position = [258,986]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 6:
        eb_position = [332,983]
        screen.blit(number_eb, eb_position)
        pygame.display.update()
    if num == 5:
        eb_position = [380,985]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 4:
        eb_position = [447,985]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 3:
        eb_position = [518,982]
        screen.blit(number_eb, eb_position)
        pygame.display.update()
    if num == 2:
        eb_position = [568,984]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 1:
        eb_position = [635,984]
        screen.blit(eb, eb_position)
        pygame.display.update()


def feature_animation(num):
    global screen
    if num == 6:
        corners_position = [17,750]
        screen.blit(c, corners_position)
        pygame.display.update()

    if num == 5:
        rs_position = [648,916]
        screen.blit(star, rs_position)
        pygame.display.update()

    if num == 4:
        ys_position = [6,925]
        screen.blit(star, ys_position)
        pygame.display.update()

    if num == 3:
        p = [314,792]
        screen.blit(magic_lines4, p)
        pygame.display.update()
        
        screen.blit(sc, p)

    if num == 2:
        p = [54,574]
        screen.blit(sc, p)
        pygame.display.update()

    if num == 1:
        p = [566,572]
        screen.blit(sc, p)
        pygame.display.update()


def odds_animation(num):
    global screen
    if num == 5:
        odds_position = [82,873]
        o = pygame.image.load('big_time/assets/odds1.png').convert_alpha()
        screen.blit(o, odds_position)
        pygame.display.update()
    if num == 4:
        odds_position = [154,870]
        o = pygame.image.load('big_time/assets/odds2.png').convert_alpha()
        screen.blit(o, odds_position)
        pygame.display.update()
    if num == 3:
        odds_position = [220,872]
        o = pygame.image.load('big_time/assets/odds3.png').convert_alpha()
        screen.blit(o, odds_position)
        pygame.display.update()
    if num == 2:
        odds_position = [291,876]
        o = pygame.image.load('big_time/assets/odds4.png').convert_alpha()
        screen.blit(o, odds_position)
        pygame.display.update()
    if num == 1:
        odds_position = [362,873]
        o = pygame.image.load('big_time/assets/odds5.png').convert_alpha()
        screen.blit(o, odds_position)
        pygame.display.update()
