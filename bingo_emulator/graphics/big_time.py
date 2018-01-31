
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
bg_menu = pygame.image.load('big_time/assets/big_time_menu.png').convert()
bg_gi = pygame.image.load('big_time/assets/big_time_gi.png').convert()
bg_off = pygame.image.load('big_time/assets/big_time_off.png').convert()
bg_gi.set_colorkey((255,0,252))
bg_menu.set_colorkey((255,0,252))
bg_off.set_colorkey((255,0,252))

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
        screen.blit(bg_menu, backglass_position)
    else:
        if (s.game.anti_cheat.status == True):
            screen.blit(bg_gi, backglass_position)
        else:
            screen.blit(bg_off, backglass_position)

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

    if s.game.before_fifth.status == False:
        if s.game.magic_lines_feature.position >= 4:
            p = [540,747]
            screen.blit(time, p)
            if s.game.ball_count.position == 3:
                s.cancel_delayed(name="blink")
                blink([s,1,1])
            else:
                s.cancel_delayed(name="blink")
    if s.game.before_fifth.status == True:
        if s.game.magic_lines_feature.position >= 4:
            p = [627,747]
            screen.blit(time, p)
            if s.game.ball_count.position == 4:
                s.cancel_delayed(name="blink")
                blink([s,1,1])
            else:
                s.cancel_delayed(name="blink")

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

def blink(args):
    dirty_rects = []
    s = args[0]
    b = args[1]
    sn = args[2]

    if b == 1:
        if sn == 1:
            p = [556,793]
            dirty_rects.append(screen.blit(select_now, p))
        pygame.display.update(dirty_rects)
    else:
        dirty_rects.append(screen.blit(bg_gi, (556,793), pygame.Rect(556,793,118,28)))
        pygame.display.update(dirty_rects)
    b = not b

    args = [s,b,sn]

    s.delay(name="blink", delay=0.1, handler=blink, param=args)

def eb_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]

    if s.game.extra_ball.position < 1:
        dirty_rects.append(screen.blit(bg_gi, (142,986), pygame.Rect(142,986,50,38)))
    if s.game.extra_ball.position < 2:
        dirty_rects.append(screen.blit(bg_gi, (192,986), pygame.Rect(192,986,65,35)))
    if s.game.extra_ball.position < 3:
        dirty_rects.append(screen.blit(bg_gi, (258,986), pygame.Rect(258,986,65,35)))
    if s.game.extra_ball.position < 4:
        dirty_rects.append(screen.blit(bg_gi, (332,983), pygame.Rect(332,983,48,35)))
    if s.game.extra_ball.position < 5:
        dirty_rects.append(screen.blit(bg_gi, (380,985), pygame.Rect(380,985,65,35)))
    if s.game.extra_ball.position < 6:
        dirty_rects.append(screen.blit(bg_gi, (447,985), pygame.Rect(447,985,65,35)))
    if s.game.extra_ball.position < 7:
        dirty_rects.append(screen.blit(bg_gi, (518,982), pygame.Rect(518,982,48,35)))
    if s.game.extra_ball.position < 8:
        dirty_rects.append(screen.blit(bg_gi, (568,984), pygame.Rect(568,984,65,35)))
    if s.game.extra_ball.position < 9:
        dirty_rects.append(screen.blit(bg_gi, (635,984), pygame.Rect(635,984,65,35)))
    pygame.display.update(dirty_rects)

    if num in [0,25,14,49]:
        if s.game.extra_ball.position < 1:
            p = [142,986]
            dirty_rects.append(screen.blit(number_eb, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [39,1,26,15]:
        if s.game.extra_ball.position < 2:
            p = [192,986]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [3,4,17,28,29,40]:
        if s.game.extra_ball.position < 3:
            p = [258,986]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [5,18,30,43]:
        if s.game.extra_ball.position < 4:
            p = [332,983]
            dirty_rects.append(screen.blit(number_eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [7,8,19,32,33,44]:
        if s.game.extra_ball.position < 5:
            p = [380,985]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [9,10,20,34,35,45]:
        if s.game.extra_ball.position < 6:
            p = [447,985]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [11,21,36,46]:
        if s.game.extra_ball.position < 7:
            p = [518,982]
            dirty_rects.append(screen.blit(number_eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [12,22,37,47]:
        if s.game.extra_ball.position < 8:
            p = [568,984]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [2,6,13,16,23,27,31,38,41,48]:
        if s.game.extra_ball.position < 9:
            p = [635,984]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return

def clear_odds(s, num):
    global screen

    dirty_rects = []
    if s.game.odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (82,873), pygame.Rect(82,873,75,104)))
    if s.game.odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (154,870), pygame.Rect(154,870,70,112)))
    if s.game.odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (220,872), pygame.Rect(220,872,77,101)))
    if s.game.odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (291,876), pygame.Rect(291,876,73,95)))
    if s.game.odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (362,873), pygame.Rect(362,873,68,97)))
    if s.game.odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (429,871), pygame.Rect(429,871,70,95)))
    if s.game.odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (498,873), pygame.Rect(498,873,71,91)))
    if s.game.odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (564,872), pygame.Rect(564,872,79,95)))
    
    pygame.display.update(dirty_rects)

def draw_odds_animation(s, num):
    global screen
    dirty_rects = []

    if num in [2,3,12,27,28,37]:
        if s.game.odds.position != 1:
            p = [82,873]
            dirty_rects.append(screen.blit(o1, p))
            pygame.display.update(dirty_rects)
            return
    if num in [4,5,17,29,30,42]:
        if s.game.odds.position != 2:
            p = [154,870]
            dirty_rects.append(screen.blit(o2, p))
            pygame.display.update(dirty_rects)
            return
    if num in [6,7,18,19,31,32,43,44]:
        if s.game.odds.position != 3:
            p = [220,872]
            dirty_rects.append(screen.blit(o3, p))
            pygame.display.update(dirty_rects)
            return
    if num in [8,9,20,21,33,34,45,46]:
        if s.game.odds.position != 4:
            p = [291,876]
            dirty_rects.append(screen.blit(o4, p))
            pygame.display.update(dirty_rects)
            return
    if num in [10,11,22,23,35,36,47,48]:
        if s.game.odds.position != 5:
            p = [362,873]
            dirty_rects.append(screen.blit(o5, p))
            pygame.display.update(dirty_rects)
            return
    if num in [12,13,23,37,38,48]:
        if s.game.odds.position != 6:
            p = [429,871]
            dirty_rects.append(screen.blit(o6, p))
            pygame.display.update(dirty_rects)
            return
    if num in [14,15,24,39,40,49]:
        if s.game.odds.position != 7:
            p = [498,873]
            dirty_rects.append(screen.blit(o7, p))
            pygame.display.update(dirty_rects)
            return
    if num in [16,25,41,50]:
        if s.game.odds.position != 8:
            p = [564,872]
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

    if s.game.before_fourth.status == False:
        dirty_rects.append(screen.blit(bg_gi, (540,747), pygame.Rect(540,747,73,43)))
    if s.game.before_fifth.status == False:
        dirty_rects.append(screen.blit(bg_gi, (627,747), pygame.Rect(627,747,73,43)))
    if s.game.magic_lines_feature.position < 4:
        dirty_rects.append(screen.blit(bg_gi, (206,792), pygame.Rect(206,792,146,40)))
    if s.game.magic_lines_feature.position < 5:
        dirty_rects.append(screen.blit(bg_gi, (314,792), pygame.Rect(314,792,103,29)))
    if s.game.magic_lines_feature.position < 6:
        dirty_rects.append(screen.blit(bg_gi, (420,792), pygame.Rect(420,792,103,29)))
    if s.game.red_star.status == False:
        dirty_rects.append(screen.blit(bg_gi, (648,916), pygame.Rect(648,916,68,62)))
        s.game.coils.yellowROLamp.pulse()
    if s.game.yellow_star.status == False:
        dirty_rects.append(screen.blit(bg_gi, (6,925), pygame.Rect(6,925,68,62)))
        s.game.coils.redROLamp.pulse()
    if s.game.super_card.position < 4:
        dirty_rects.append(screen.blit(bg_gi, (54,574), pygame.Rect(54,574,106,24)))
    if s.game.super_card.position < 8:
        dirty_rects.append(screen.blit(bg_gi, (566,572), pygame.Rect(566,572,106,24)))
    if s.game.corners.status == False:
        dirty_rects.append(screen.blit(bg_gi, (17,750), pygame.Rect(17,750,54,76)))

    pygame.display.update(dirty_rects)


def draw_feature_animation(s, num):
    global screen
    dirty_rects = []
 
    
    if num in [10,11,35,36]:
        if s.game.before_fourth.status == False:
            p = [540,747]
            dirty_rects.append(screen.blit(time, p))
            pygame.display.update(dirty_rects)
            return
    if num in [12,13,37,38]:
        if s.game.before_fifth.status == False:
            p = [627,747]
            dirty_rects.append(screen.blit(time, p))
            pygame.display.update(dirty_rects)
            return
    if num in [3,4,20,21,28,29,45,46]:
        if s.game.magic_lines_feature.position < 4:
            p = [206,792]
            dirty_rects.append(screen.blit(magic_lines4, p))
            pygame.display.update(dirty_rects)
            return
    if num in [5,6,22,23,30,31,47,48]:
        if s.game.magic_lines_feature.position < 5:
            p = [314,792]
            dirty_rects.append(screen.blit(magic_lines4, p))
            pygame.display.update(dirty_rects)
            return
    if num in [7,8,24,32,33,49]:
        if s.game.magic_lines_feature.position < 6:
            p = [420,792]
            dirty_rects.append(screen.blit(magic_lines4, p))
            pygame.display.update(dirty_rects)
            return
    if num in [19,44]:
        if s.game.red_star.status == False:
            p = [648,916]
            dirty_rects.append(screen.blit(star, p))
            pygame.display.update(dirty_rects)
            s.game.coils.yellowROLamp.pulse()
            return
    if num in [9,34]:
        if s.game.yellow_star.status == False:
            p = [6,925]
            dirty_rects.append(screen.blit(star, p))
            pygame.display.update(dirty_rects)
            s.game.coils.redROLamp.pulse()
            return
    if num in [0,1,16,17,25,26,41,42]:
        if s.game.super_card.position < 4:
            p = [54,574]
            dirty_rects.append(screen.blit(sc, p))
            pygame.display.update(dirty_rects)
            return
    if num in [14,15,39,40]:
        if s.game.super_card.position < 8:
            p = [566,572]
            dirty_rects.append(screen.blit(sc, p))
            pygame.display.update(dirty_rects)
            return
    if num in [2,18,27,43]:
        if s.game.corners.status == False:
            p = [17,750]
            dirty_rects.append(screen.blit(c, p))
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


