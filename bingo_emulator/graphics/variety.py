
import pygame
import random

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

meter = pygame.image.load('graphics/assets/register_cover.png').convert()
arrow = pygame.image.load('variety/assets/arrow.png').convert_alpha()
sc = pygame.image.load('variety/assets/sc.png').convert_alpha()
eb = pygame.image.load('variety/assets/eb.png').convert_alpha()
ebs = pygame.image.load('variety/assets/extra_balls.png').convert_alpha()
number_eb = pygame.image.load('variety/assets/eb_number.png').convert_alpha()
o1 = pygame.image.load('variety/assets/odds1.png').convert_alpha()
o2 = pygame.image.load('variety/assets/odds2.png').convert_alpha()
o3 = pygame.image.load('variety/assets/odds3.png').convert_alpha()
o4 = pygame.image.load('variety/assets/odds4.png').convert_alpha()
o5 = pygame.image.load('variety/assets/odds5.png').convert_alpha()
o6 = pygame.image.load('variety/assets/odds6.png').convert_alpha()
o7 = pygame.image.load('variety/assets/odds7.png').convert_alpha()
o8 = pygame.image.load('variety/assets/odds8.png').convert_alpha()
c = pygame.image.load('variety/assets/corners.png').convert_alpha()
star = pygame.image.load('variety/assets/star.png').convert_alpha()
number = pygame.image.load('variety/assets/number.png').convert_alpha()
sc_number = pygame.image.load('variety/assets/sc_number.png').convert_alpha()
tilt = pygame.image.load('variety/assets/tilt.png').convert_alpha()
sc_arrow = pygame.image.load('variety/assets/sc_arrow.png').convert_alpha()
time = pygame.image.load('variety/assets/time.png').convert_alpha()
magic_lines = pygame.image.load('variety/assets/magic_lines.png').convert_alpha()
select_now = pygame.image.load('variety/assets/select_now.png').convert_alpha()
movement = pygame.image.load('variety/assets/movement.png').convert_alpha()
line1 = pygame.image.load('variety/assets/line1.png').convert_alpha()
line2 = pygame.image.load('variety/assets/line2.png').convert_alpha()
line3 = pygame.image.load('variety/assets/line3.png').convert_alpha()
bg_menu = pygame.image.load('variety/assets/variety_menu.png').convert()
bg_menu.set_colorkey((255,0,252))
bg_gi = pygame.image.load('variety/assets/variety_gi.png').convert()
bg_gi.set_colorkey((255,0,252))
bg_off = pygame.image.load('variety/assets/variety_off.png').convert()
bg_off.set_colorkey((255,0,252))

class scorereel():
    """ Score Reels are used to count replays """
    def __init__(self, pos, image):
        self.position = pos
        self.default_y = self.position[1]
        self.image = pygame.image.load(image).convert()

reel1 = scorereel([609,555], "graphics/assets/white_reel.png")
reel10 = scorereel([590,555], "graphics/assets/white_reel.png")
reel100 = scorereel([572,555], "graphics/assets/white_reel.png")

def display(s, replays=0, menu=False):
    
    meter.set_colorkey((255,0,252))
    meter_position = [562,555]

    screen.blit(reel1.image, reel1.position)
    screen.blit(reel10.image, reel10.position)
    screen.blit(reel100.image, reel100.position)
    screen.blit(meter, meter_position)

    if s.game.line1.position == 0:
        line1_position = [232,507]
    elif s.game.line1.position == 1:
        line1_position = [232,555]
    elif s.game.line1.position == 2:
        line1_position = [232,460]
    
    screen.blit(line1, line1_position)

    if s.game.line2.position == 0:
        line2_position = [284,503]
    elif s.game.line2.position == 1:
        line2_position = [284,555]
    elif s.game.line2.position == 2:
        line2_position = [284,460]
    
    screen.blit(line2, line2_position)

    if s.game.line3.position == 0:
        line3_position = [335,503]
    elif s.game.line3.position == 1:
        line3_position = [335,555]
    elif s.game.line3.position == 2:
        line3_position = [335,460]
    
    screen.blit(line3, line3_position)

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
        p = [46,692]
        screen.blit(sc_arrow, p)
    if s.game.super_card.position == 2:
        p = [76,692]
        screen.blit(sc_arrow, p)
    if s.game.super_card.position == 3:
        p = [103,692]
        screen.blit(sc_arrow, p)
    if s.game.super_card.position == 4:
        p = [129,692]
        screen.blit(sc_arrow, p)
    if s.game.super_card.position == 5:
        p = [560,692]
        screen.blit(sc_arrow, p)
    if s.game.super_card.position == 6:
        p = [586,692]
        screen.blit(sc_arrow, p)
    if s.game.super_card.position == 7:
        p = [613,692]
        screen.blit(sc_arrow, p)
    if s.game.super_card.position == 8:
        p = [639,692]
        screen.blit(sc_arrow, p)

    if s.game.super_card.position >= 4:
        p = [51,720]
        screen.blit(sc, p)

    if s.game.super_card.position >= 8:
        p = [562,719]
        screen.blit(sc, p)

    if s.game.extra_ball.position >= 1:
        eb_position = [142,969]
        screen.blit(number_eb, eb_position)
    if s.game.extra_ball.position >= 2:
        eb_position = [191,969]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 3:
        eb_position = [258,969]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 4:
        eb_position = [328,969]
        screen.blit(number_eb, eb_position)
    if s.game.extra_ball.position >= 5:
        eb_position = [377,969]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 6:
        eb_position = [442,969]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 7:
        eb_position = [514,969]
        screen.blit(number_eb, eb_position)
    if s.game.extra_ball.position >= 8:
        eb_position = [563,969]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 9:
        eb_position = [626,969]
        screen.blit(eb, eb_position)
    
    
    if s.game.odds.position > 0:
        if s.game.odds.position == 1:
            odds_position = [162,310]
            screen.blit(o1, odds_position)
        if s.game.odds.position == 2:
            odds_position = [204,307]
            screen.blit(o2, odds_position)
        if s.game.odds.position == 3:
            odds_position = [272,321]
            screen.blit(o3, odds_position)
        if s.game.odds.position == 4:
            odds_position = [347,281]
            screen.blit(o4, odds_position)
        if s.game.odds.position == 5:
            odds_position = [401,280]
            screen.blit(o5, odds_position)
        if s.game.odds.position == 6:
            odds_position = [474,282]
            screen.blit(o6, odds_position)
        if s.game.odds.position == 7:
            odds_position = [510,277]
            screen.blit(o7, odds_position)
        if s.game.odds.position == 8:
            odds_position = [620,335]
            screen.blit(o8, odds_position)

    if s.game.red_star.status == True:
        rs_position = [638,276]
        screen.blit(star, rs_position)

    if s.game.yellow_star.status == True:
        ys_position = [14,273]
        screen.blit(star, ys_position)

    if s.game.corners.status == True:
        corners_position = [61,546]
        screen.blit(c, corners_position)

    if s.game.tilt.status == False:
        if s.holes:
            if 1 in s.holes:
                if s.game.line1.position == 0:
                    number_position = [230,697]
                    screen.blit(number, number_position)
                elif s.game.line1.position == 1:
                    number_position = [230,745]
                    screen.blit(number, number_position)
                elif s.game.line1.position == 2:
                    number_position = [230,650]
                    screen.blit(number, number_position)
                number_position = [544,792]
                screen.blit(sc_number, number_position)
            if 2 in s.holes:
                if s.game.line1.position == 0:
                    number_position = [230,648]
                    screen.blit(number, number_position)
                elif s.game.line1.position == 1:
                    number_position = [230,695]
                    screen.blit(number, number_position)
                elif s.game.line1.position == 2:
                    number_position = [230,601]
                    screen.blit(number, number_position)
            if 3 in s.holes:
                number_position = [440,746]
                screen.blit(number, number_position)
                number_position = [81,747]
                screen.blit(sc_number, number_position)
            if 4 in s.holes:
                if s.game.line2.position == 0:
                    number_position = [282,554]
                    screen.blit(number, number_position)
                elif s.game.line2.position == 1:
                    number_position = [282,602]
                    screen.blit(number, number_position)
                elif s.game.line2.position == 2:
                    number_position = [282,745]
                    screen.blit(number, number_position)
                number_position = [593,837]
                screen.blit(sc_number, number_position)
            if 5 in s.holes:
                if s.game.line3.position == 0:
                    number_position = [334,744]
                    screen.blit(number, number_position)
                elif s.game.line3.position == 1:
                    number_position = [334,555]
                    screen.blit(number, number_position)
                elif s.game.line3.position == 2:
                    number_position = [334,696]
                    screen.blit(number, number_position)
            if 6 in s.holes:
                number_position = [440,555]
                screen.blit(number, number_position)
            if 7 in s.holes:
                if s.game.line2.position == 0:
                    number_position = [281,746]
                    screen.blit(number, number_position)
                elif s.game.line2.position == 1:
                    number_position = [281,553]
                    screen.blit(number, number_position)
                elif s.game.line2.position == 2:
                    number_position = [282,697]
                    screen.blit(number, number_position)
                number_position = [593,747]
                screen.blit(sc_number, number_position)
            if 8 in s.holes:
                number_position = [441,604]
                screen.blit(number, number_position)
            if 9 in s.holes:
                if s.game.line1.position == 0:
                    number_position = [228,555]
                    screen.blit(number, number_position)
                elif s.game.line1.position == 1:
                    number_position = [228,601]
                    screen.blit(number, number_position)
                elif s.game.line1.position == 2:
                    number_position = [228,745]
                    screen.blit(number, number_position)
                number_position = [32,791]
                screen.blit(sc_number, number_position)
            if 10 in s.holes:
                if s.game.line1.position == 0:
                    number_position = [228,602]
                    screen.blit(number, number_position)
                elif s.game.line1.position == 1:
                    number_position = [228,650]
                    screen.blit(number, number_position)
                elif s.game.line1.position == 2:
                    number_position = [228,554]
                    screen.blit(number, number_position)
                number_position = [594,793]
                screen.blit(sc_number, number_position)
            if 11 in s.holes:
                if s.game.line1.position == 0:
                    number_position = [228,745]
                    screen.blit(number, number_position)
                elif s.game.line1.position == 1:
                    number_position = [228,553]
                    screen.blit(number, number_position)
                elif s.game.line1.position == 2:
                    number_position = [228,697]
                    screen.blit(number, number_position)
                number_position = [130,793]
                screen.blit(sc_number, number_position)
                number_position = [641,748]
                screen.blit(sc_number, number_position)
            if 12 in s.holes:
                number_position = [389,652]
                screen.blit(number, number_position)
                number_position = [32,837]
                screen.blit(sc_number, number_position)
            if 13 in s.holes:
                if s.game.line3.position == 0:
                    number_position = [334,697]
                    screen.blit(number, number_position)
                elif s.game.line3.position == 1:
                    number_position = [333,745]
                    screen.blit(number, number_position)
                elif s.game.line3.position == 2:
                    number_position = [334,648]
                    screen.blit(number, number_position)
                number_position = [642,793]
                screen.blit(sc_number, number_position)
            if 14 in s.holes:
                if s.game.line3.position == 0:
                    number_position = [334,601]
                    screen.blit(number, number_position)
                elif s.game.line3.position == 1:
                    number_position = [334,650]
                    screen.blit(number, number_position)
                elif s.game.line3.position == 2:
                    number_position = [334,553]
                    screen.blit(number, number_position)
                number_position = [130,836]
                screen.blit(sc_number, number_position)
            if 15 in s.holes:
                if s.game.line3.position == 0:
                    number_position = [334,554]
                    screen.blit(number, number_position)
                elif s.game.line3.position == 1:
                    number_position = [336,602]
                    screen.blit(number, number_position)
                elif s.game.line3.position == 2:
                    number_position = [334,745]
                    screen.blit(number, number_position)
                number_position = [544,748]
                screen.blit(sc_number, number_position)
            if 16 in s.holes:
                if s.game.line3.position == 0:
                    number_position = [335,650]
                    screen.blit(number, number_position)
                elif s.game.line3.position == 1:
                    number_position = [334,697]
                    screen.blit(number, number_position)
                elif s.game.line3.position == 2:
                    number_position = [334,602]
                    screen.blit(number, number_position)
            if 17 in s.holes:
                number_position = [441,699]
                screen.blit(number, number_position)
                number_position = [544,837]
                screen.blit(sc_number, number_position)
            if 18 in s.holes:
                if s.game.line2.position == 0:
                    number_position = [282,650]
                    screen.blit(number, number_position)
                elif s.game.line2.position == 1:
                    number_position = [282,696]
                    screen.blit(number, number_position)
                elif s.game.line2.position == 2:
                    number_position = [282,600]
                    screen.blit(number, number_position)
                number_position = [131,748]
                screen.blit(sc_number, number_position)
                number_position = [642,837]
                screen.blit(sc_number, number_position)
            if 19 in s.holes:
                if s.game.line2.position == 0:
                    number_position = [282,602]
                    screen.blit(number, number_position)
                elif s.game.line2.position == 1:
                    number_position = [282,650]
                    screen.blit(number, number_position)
                elif s.game.line2.position == 2:
                    number_position = [282,553]
                    screen.blit(number, number_position)
            if 20 in s.holes:
                number_position = [389,604]
                screen.blit(number, number_position)
            if 21 in s.holes:
                number_position = [389,698]
                screen.blit(number, number_position)
            if 22 in s.holes:
                if s.game.line2.position == 0:
                    number_position = [282,696]
                    screen.blit(number, number_position)
                elif s.game.line2.position == 1:
                    number_position = [281,745]
                    screen.blit(number, number_position)
                elif s.game.line2.position == 2:
                    number_position = [282,650]
                    screen.blit(number, number_position)
            if 23 in s.holes:
                number_position = [389,747]
                screen.blit(number, number_position)
                number_position = [33,747]
                screen.blit(sc_number, number_position)
            if 24 in s.holes:
                number_position = [388,556]
                screen.blit(number, number_position)
                number_position = [83,837]
                screen.blit(sc_number, number_position)
            if 25 in s.holes:
                number_position = [441,652]
                screen.blit(number, number_position)
                number_position = [83,793]
                screen.blit(sc_number, number_position)

    if s.game.line1.position == 1:
        p = [233,481]
        screen.blit(movement, p)
    elif s.game.line1.position == 2:
        p = [233,824]
        screen.blit(movement, p)

    if s.game.line2.position == 1:
        p = [285,481]
        screen.blit(movement, p)
    elif s.game.line2.position == 2:
        p = [286,824]
        screen.blit(movement, p)

    if s.game.line3.position == 1:
        p = [338,481]
        screen.blit(movement, p)
    elif s.game.line3.position == 2:
        p = [337,823]
        screen.blit(movement, p)

    if s.game.before_fourth.status == True and s.game.magic_lines_feature.position == 4:
        p = [25,894]
        screen.blit(time, p)
        if s.game.ball_count.position == 3:
            s.cancel_delayed(name="blink")
            blink([s,1,1])
        else:
            s.cancel_delayed(name="blink")
    elif s.game.before_fifth.status == True and s.game.magic_lines_feature.position == 4:
        p = [609,894]
        screen.blit(time, p)
        if s.game.ball_count.position == 4:
            s.cancel_delayed(name="blink")
            blink([s,1,1])
        else:
            s.cancel_delayed(name="blink")

    if s.game.tilt.status == True:
        tilt_position = [558,500]
        screen.blit(tilt, tilt_position)

    if s.game.eb_play.status == True:
        ebs_position = [23,971]
        screen.blit(ebs, ebs_position)

    if s.game.magic_lines_feature.position == 1:
        p = [120,912]
        screen.blit(arrow, p)
    elif s.game.magic_lines_feature.position == 2:
        p = [156,912]
        screen.blit(arrow, p)
    elif s.game.magic_lines_feature.position == 3:
        p = [190,912]
        screen.blit(arrow, p)
    elif s.game.magic_lines_feature.position == 4:
        p = [226,908]
        screen.blit(magic_lines, p)
                
    pygame.display.update()

def blink(args):
    dirty_rects = []
    s = args[0]
    b = args[1]
    sn = args[2]

    if b == 0:
        if sn == 1:
            p = [400,913]
            dirty_rects.append(screen.blit(select_now, p))
        pygame.display.update(dirty_rects)
    else:
        dirty_rects.append(screen.blit(bg_gi, (400,913), pygame.Rect(400,913,118,28)))
        pygame.display.update(dirty_rects)
    b = not b

    args = [s,b,sn]

    s.delay(name="blink", delay=0.1, handler=blink, param=args)

def eb_animation(num):
    global screen
    if num == 9:
        eb_position = [142,969]
        screen.blit(number_eb, eb_position)
        pygame.display.update()
    if num == 8:
        eb_position = [191,969]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 7:
        eb_position = [258,969]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 6:
        eb_position = [328,969]
        screen.blit(number_eb, eb_position)
        pygame.display.update()
    if num == 5:
        eb_position = [377,969]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 4:
        eb_position = [442,969]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 3:
        eb_position = [514,969]
        screen.blit(number_eb, eb_position)
        pygame.display.update()
    if num == 2:
        eb_position = [563,969]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 1:
        eb_position = [626,969]
        screen.blit(eb, eb_position)
        pygame.display.update()


def feature_animation(num):
    global screen
    if num == 6:
        corners_position = [61,546]
        screen.blit(c, corners_position)
        pygame.display.update()

    if num == 5:
        rs_position = [638,276]
        screen.blit(star, rs_position)
        pygame.display.update()

    if num == 4:
        ys_position = [14,273]
        screen.blit(star, ys_position)
        pygame.display.update()

    if num == 3:
        p = [226,908]
        screen.blit(magic_lines, p)
        pygame.display.update()
   
    if num == 2:
        p = [51,720]
        screen.blit(sc, p)
        pygame.display.update()

    if num == 1:
        p = [562,719]
        screen.blit(sc, p)
        pygame.display.update()


def odds_animation(num):
    global screen
    if num == 5:
        odds_position = [162,310]
        o = pygame.image.load('variety/assets/odds1.png').convert_alpha()
        screen.blit(o, odds_position)
        pygame.display.update()
    if num == 4:
        odds_position = [204,307]
        o = pygame.image.load('variety/assets/odds2.png').convert_alpha()
        screen.blit(o, odds_position)
        pygame.display.update()
    if num == 3:
        odds_position = [272,321]
        o = pygame.image.load('variety/assets/odds3.png').convert_alpha()
        screen.blit(o, odds_position)
        pygame.display.update()
    if num == 2:
        odds_position = [347,281]
        o = pygame.image.load('variety/assets/odds4.png').convert_alpha()
        screen.blit(o, odds_position)
        pygame.display.update()
    if num == 1:
        odds_position = [401,280]
        o = pygame.image.load('variety/assets/odds5.png').convert_alpha()
        screen.blit(o, odds_position)
        pygame.display.update()
