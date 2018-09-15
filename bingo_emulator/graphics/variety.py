
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

    if s.game.line1.position in [0,2]:
        line1_position = [232,507]
    elif s.game.line1.position == 1:
        line1_position = [232,555]
    elif s.game.line1.position == 3:
        line1_position = [232,460]
    
    screen.blit(line1, line1_position)

    if s.game.line2.position in [0,2]:
        line2_position = [284,503]
    elif s.game.line2.position == 1:
        line2_position = [284,555]
    elif s.game.line2.position == 3:
        line2_position = [284,460]
    
    screen.blit(line2, line2_position)

    if s.game.line3.position in [0,2]:
        line3_position = [335,503]
    elif s.game.line3.position == 1:
        line3_position = [335,555]
    elif s.game.line3.position == 3:
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
                if s.game.line1.position in [0,2]:
                    number_position = [230,697]
                    screen.blit(number, number_position)
                elif s.game.line1.position == 1:
                    number_position = [230,745]
                    screen.blit(number, number_position)
                elif s.game.line1.position == 3:
                    number_position = [230,650]
                    screen.blit(number, number_position)
                number_position = [544,792]
                screen.blit(sc_number, number_position)
            if 2 in s.holes:
                if s.game.line1.position in [0,2]:
                    number_position = [230,648]
                    screen.blit(number, number_position)
                elif s.game.line1.position == 1:
                    number_position = [230,695]
                    screen.blit(number, number_position)
                elif s.game.line1.position == 3:
                    number_position = [230,601]
                    screen.blit(number, number_position)
            if 3 in s.holes:
                number_position = [440,746]
                screen.blit(number, number_position)
                number_position = [81,747]
                screen.blit(sc_number, number_position)
            if 4 in s.holes:
                if s.game.line2.position in [0,2]:
                    number_position = [282,554]
                    screen.blit(number, number_position)
                elif s.game.line2.position == 1:
                    number_position = [282,602]
                    screen.blit(number, number_position)
                elif s.game.line2.position == 3:
                    number_position = [282,745]
                    screen.blit(number, number_position)
                number_position = [593,837]
                screen.blit(sc_number, number_position)
            if 5 in s.holes:
                if s.game.line3.position in [0,2]:
                    number_position = [334,744]
                    screen.blit(number, number_position)
                elif s.game.line3.position == 1:
                    number_position = [334,555]
                    screen.blit(number, number_position)
                elif s.game.line3.position == 3:
                    number_position = [334,696]
                    screen.blit(number, number_position)
            if 6 in s.holes:
                number_position = [440,555]
                screen.blit(number, number_position)
            if 7 in s.holes:
                if s.game.line2.position in [0,2]:
                    number_position = [281,746]
                    screen.blit(number, number_position)
                elif s.game.line2.position == 1:
                    number_position = [281,553]
                    screen.blit(number, number_position)
                elif s.game.line2.position == 3:
                    number_position = [282,697]
                    screen.blit(number, number_position)
                number_position = [593,747]
                screen.blit(sc_number, number_position)
            if 8 in s.holes:
                number_position = [441,604]
                screen.blit(number, number_position)
            if 9 in s.holes:
                if s.game.line1.position in [0,2]:
                    number_position = [228,555]
                    screen.blit(number, number_position)
                elif s.game.line1.position == 1:
                    number_position = [228,601]
                    screen.blit(number, number_position)
                elif s.game.line1.position == 3:
                    number_position = [228,745]
                    screen.blit(number, number_position)
                number_position = [32,791]
                screen.blit(sc_number, number_position)
            if 10 in s.holes:
                if s.game.line1.position in [0,2]:
                    number_position = [228,602]
                    screen.blit(number, number_position)
                elif s.game.line1.position == 1:
                    number_position = [228,650]
                    screen.blit(number, number_position)
                elif s.game.line1.position == 3:
                    number_position = [228,554]
                    screen.blit(number, number_position)
                number_position = [594,793]
                screen.blit(sc_number, number_position)
            if 11 in s.holes:
                if s.game.line1.position in [0,2]:
                    number_position = [228,745]
                    screen.blit(number, number_position)
                elif s.game.line1.position == 1:
                    number_position = [228,553]
                    screen.blit(number, number_position)
                elif s.game.line1.position == 3:
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
                if s.game.line3.position in [0,2]:
                    number_position = [334,697]
                    screen.blit(number, number_position)
                elif s.game.line3.position == 1:
                    number_position = [333,745]
                    screen.blit(number, number_position)
                elif s.game.line3.position == 3:
                    number_position = [334,648]
                    screen.blit(number, number_position)
                number_position = [642,793]
                screen.blit(sc_number, number_position)
            if 14 in s.holes:
                if s.game.line3.position in [0,2]:
                    number_position = [334,601]
                    screen.blit(number, number_position)
                elif s.game.line3.position == 1:
                    number_position = [334,650]
                    screen.blit(number, number_position)
                elif s.game.line3.position == 3:
                    number_position = [334,553]
                    screen.blit(number, number_position)
                number_position = [130,836]
                screen.blit(sc_number, number_position)
            if 15 in s.holes:
                if s.game.line3.position in [0,2]:
                    number_position = [334,554]
                    screen.blit(number, number_position)
                elif s.game.line3.position == 1:
                    number_position = [336,602]
                    screen.blit(number, number_position)
                elif s.game.line3.position == 3:
                    number_position = [334,745]
                    screen.blit(number, number_position)
                number_position = [544,748]
                screen.blit(sc_number, number_position)
            if 16 in s.holes:
                if s.game.line3.position in [0,2]:
                    number_position = [335,650]
                    screen.blit(number, number_position)
                elif s.game.line3.position == 1:
                    number_position = [334,697]
                    screen.blit(number, number_position)
                elif s.game.line3.position == 3:
                    number_position = [334,602]
                    screen.blit(number, number_position)
            if 17 in s.holes:
                number_position = [441,699]
                screen.blit(number, number_position)
                number_position = [544,837]
                screen.blit(sc_number, number_position)
            if 18 in s.holes:
                if s.game.line2.position in [0,2]:
                    number_position = [282,650]
                    screen.blit(number, number_position)
                elif s.game.line2.position == 1:
                    number_position = [282,696]
                    screen.blit(number, number_position)
                elif s.game.line2.position == 3:
                    number_position = [282,600]
                    screen.blit(number, number_position)
                number_position = [131,748]
                screen.blit(sc_number, number_position)
                number_position = [642,837]
                screen.blit(sc_number, number_position)
            if 19 in s.holes:
                if s.game.line2.position in [0,2]:
                    number_position = [282,602]
                    screen.blit(number, number_position)
                elif s.game.line2.position == 1:
                    number_position = [282,650]
                    screen.blit(number, number_position)
                elif s.game.line2.position == 3:
                    number_position = [282,553]
                    screen.blit(number, number_position)
            if 20 in s.holes:
                number_position = [389,604]
                screen.blit(number, number_position)
            if 21 in s.holes:
                number_position = [389,698]
                screen.blit(number, number_position)
            if 22 in s.holes:
                if s.game.line2.position in [0,2]:
                    number_position = [282,696]
                    screen.blit(number, number_position)
                elif s.game.line2.position == 1:
                    number_position = [281,745]
                    screen.blit(number, number_position)
                elif s.game.line2.position == 3:
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
    elif s.game.line1.position == 3:
        p = [233,824]
        screen.blit(movement, p)

    if s.game.line2.position == 1:
        p = [285,481]
        screen.blit(movement, p)
    elif s.game.line2.position == 3:
        p = [286,824]
        screen.blit(movement, p)

    if s.game.line3.position == 1:
        p = [338,481]
        screen.blit(movement, p)
    elif s.game.line3.position == 3:
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

def line1_animation(args):
    dirty_rects = []
    s = args[0]
    num = args[1]
    line = args[2]

    if line == 1:
        if num % 45 == 0:
            if s.game.line1.position == 0:
                dirty_rects.append(screen.blit(line1, (232, 460 - num - 5)))
            elif s.game.line1.position == 1:
                dirty_rects.append(screen.blit(line1, (232, 507 - num - 5)))
            elif s.game.line1.position == 2:
                dirty_rects.append(screen.blit(line1, (232, 555 + num - 5)))
            elif s.game.line1.position == 3:
                dirty_rects.append(screen.blit(line1, (232, 507 + num - 5)))

        if (s.game.anti_cheat.status == True):
            dirty_rects.append(screen.blit(bg_gi, (232,450), pygame.Rect(232,450,45,706)))
        else:
            dirty_rects.append(screen.blit(bg_off, (232,450), pygame.Rect(232,450,45,706)))
        
        if s.game.magic_lines_feature.position == 4:
            dirty_rects.append(screen.blit(bg_gi, (226,908), pygame.Rect(226,908,146,40)))
            dirty_rects.append(screen.blit(magic_lines, (226,908,146,40))) 
    pygame.display.update(dirty_rects)

def line2_animation(args):
    dirty_rects = []
    s = args[0]
    num = args[1]
    line = args[2]

    if line == 2:
        if num % 45 == 0:
            if s.game.line2.position == 0:
                dirty_rects.append(screen.blit(line2, (284, 460 - num - 5)))
            elif s.game.line2.position == 1:
                dirty_rects.append(screen.blit(line2, (284,503 - num - 5)))
            elif s.game.line2.position == 2:
                dirty_rects.append(screen.blit(line2, (284,555 + num - 5)))
            elif s.game.line2.position == 3:
                dirty_rects.append(screen.blit(line2, (284,503 + num - 5)))

        if (s.game.anti_cheat.status == True):
            dirty_rects.append(screen.blit(bg_gi, (284,450), pygame.Rect(284,450,47,706)))
        else:
            dirty_rects.append(screen.blit(bg_off, (284,450), pygame.Rect(284,450,47,706)))
        
        if s.game.magic_lines_feature.position == 4:
            dirty_rects.append(screen.blit(bg_gi, (226,908), pygame.Rect(226,908,146,40)))
            dirty_rects.append(screen.blit(magic_lines, (226,908,146,40))) 
    pygame.display.update(dirty_rects)

def line3_animation(args):
    dirty_rects = []
    s = args[0]
    num = args[1]
    line = args[2]

    if line == 3:
        if num % 45 == 0:
            if s.game.line3.position == 0:
                dirty_rects.append(screen.blit(line3, (335, 460 - num - 5)))
            elif s.game.line3.position == 1:
                dirty_rects.append(screen.blit(line3, (335, 503 - num - 5)))
            elif s.game.line3.position == 2:
                dirty_rects.append(screen.blit(line3, (335, 555 + num - 5)))
            elif s.game.line3.position == 3:
                dirty_rects.append(screen.blit(line3, (335, 503 + num - 5)))

        if (s.game.anti_cheat.status == True):
            dirty_rects.append(screen.blit(bg_gi, (335,450), pygame.Rect(335,450,47,706)))
        else:
            dirty_rects.append(screen.blit(bg_off, (335,450), pygame.Rect(335,450,47,706)))
        
        if s.game.magic_lines_feature.position == 4:
            dirty_rects.append(screen.blit(bg_gi, (226,908), pygame.Rect(226,908,146,40)))
            dirty_rects.append(screen.blit(magic_lines, (226,908,146,40))) 
    pygame.display.update(dirty_rects)



def eb_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]

    if s.game.extra_ball.position < 1:
        dirty_rects.append(screen.blit(bg_gi, (142,969), pygame.Rect(142,969,50,38)))
    if s.game.extra_ball.position < 2:
        dirty_rects.append(screen.blit(bg_gi, (191,969), pygame.Rect(191,969,65,35)))
    if s.game.extra_ball.position < 3:
        dirty_rects.append(screen.blit(bg_gi, (258,969), pygame.Rect(258,969,65,35)))
    if s.game.extra_ball.position < 4:
        dirty_rects.append(screen.blit(bg_gi, (328,969), pygame.Rect(328,969,48,35)))
    if s.game.extra_ball.position < 5:
        dirty_rects.append(screen.blit(bg_gi, (377,969), pygame.Rect(377,969,65,35)))
    if s.game.extra_ball.position < 6:
        dirty_rects.append(screen.blit(bg_gi, (442,969), pygame.Rect(442,969,65,35)))
    if s.game.extra_ball.position < 7:
        dirty_rects.append(screen.blit(bg_gi, (514,969), pygame.Rect(514,969,48,35)))
    if s.game.extra_ball.position < 8:
        dirty_rects.append(screen.blit(bg_gi, (563,969), pygame.Rect(563,969,65,35)))
    if s.game.extra_ball.position < 9:
        dirty_rects.append(screen.blit(bg_gi, (626,969), pygame.Rect(626,969,65,35)))
    pygame.display.update(dirty_rects)

    if num in [0,25,14,49]:
        if s.game.extra_ball.position < 1:
            p = [142,969]
            dirty_rects.append(screen.blit(number_eb, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [39,1,26,15]:
        if s.game.extra_ball.position < 2:
            p = [191,969]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [3,4,17,28,29,40]:
        if s.game.extra_ball.position < 3:
            p = [258,969]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [5,18,30,43]:
        if s.game.extra_ball.position < 4:
            p = [328,969]
            dirty_rects.append(screen.blit(number_eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [7,8,19,32,33,44]:
        if s.game.extra_ball.position < 5:
            p = [377,969]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [9,10,20,34,35,45]:
        if s.game.extra_ball.position < 6:
            p = [442,969]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [11,21,36,46]:
        if s.game.extra_ball.position < 7:
            p = [514,969]
            dirty_rects.append(screen.blit(number_eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [12,22,37,47]:
        if s.game.extra_ball.position < 8:
            p = [563,969]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [2,6,13,16,23,27,31,38,41,48]:
        if s.game.extra_ball.position < 9:
            p = [626,969]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return

def clear_odds(s, num):
    global screen

    dirty_rects = []
    if s.game.odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (162,310), pygame.Rect(162,310,66,132)))
    if s.game.odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (204,307), pygame.Rect(204,307,77,102)))
    if s.game.odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (272,321), pygame.Rect(272,321,64,84)))
    if s.game.odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (347,281), pygame.Rect(347,281,57,125)))
    if s.game.odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (401,280), pygame.Rect(401,280,70,120)))
    if s.game.odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (474,282), pygame.Rect(474,282,66,124)))
    if s.game.odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (510,277), pygame.Rect(510,277,70,128)))
    if s.game.odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (620,335), pygame.Rect(620,335,56,76)))
    
    pygame.display.update(dirty_rects)

def draw_odds_animation(s, num):
    global screen
    dirty_rects = []

    if num in [2,3,12,27,28,37]:
        if s.game.odds.position != 1:
            p = [162,310]
            dirty_rects.append(screen.blit(o1, p))
            pygame.display.update(dirty_rects)
            return
    if num in [4,5,17,29,30,42]:
        if s.game.odds.position != 2:
            p = [204,307]
            dirty_rects.append(screen.blit(o2, p))
            pygame.display.update(dirty_rects)
            return
    if num in [6,7,18,19,31,32,43,44]:
        if s.game.odds.position != 3:
            p = [272,321]
            dirty_rects.append(screen.blit(o3, p))
            pygame.display.update(dirty_rects)
            return
    if num in [8,9,20,21,33,34,45,46]:
        if s.game.odds.position != 4:
            p = [347,281]
            dirty_rects.append(screen.blit(o4, p))
            pygame.display.update(dirty_rects)
            return
    if num in [10,11,22,23,35,36,47,48]:
        if s.game.odds.position != 5:
            p = [401,280]
            dirty_rects.append(screen.blit(o5, p))
            pygame.display.update(dirty_rects)
            return
    if num in [12,13,23,37,38,48]:
        if s.game.odds.position != 6:
            p = [474,282]
            dirty_rects.append(screen.blit(o6, p))
            pygame.display.update(dirty_rects)
            return
    if num in [14,15,24,39,40,49]:
        if s.game.odds.position != 7:
            p = [510,277]
            dirty_rects.append(screen.blit(o7, p))
            pygame.display.update(dirty_rects)
            return
    if num in [16,25,41,50]:
        if s.game.odds.position != 8:
            p = [620,335]
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
        dirty_rects.append(screen.blit(bg_gi, (25,894), pygame.Rect(25,894,84,62)))
    if s.game.before_fifth.status == False:
        dirty_rects.append(screen.blit(bg_gi, (609,894), pygame.Rect(609,894,84,62)))
    if s.game.magic_lines_feature.position < 4:
        dirty_rects.append(screen.blit(bg_gi, (226,908), pygame.Rect(226,908,146,40)))
    if s.game.red_star.status == False:
        dirty_rects.append(screen.blit(bg_gi, (638,276), pygame.Rect(638,276,68,62)))
    if s.game.yellow_star.status == False:
        dirty_rects.append(screen.blit(bg_gi, (14,273), pygame.Rect(14,273,68,62)))
    if s.game.super_card.position < 4:
        dirty_rects.append(screen.blit(bg_gi, (51,720), pygame.Rect(51,720,106,24)))
    if s.game.super_card.position < 8:
        dirty_rects.append(screen.blit(bg_gi, (562,719), pygame.Rect(562,719,106,24)))
    if s.game.corners.status == False:
        dirty_rects.append(screen.blit(bg_gi, (61,546), pygame.Rect(61,546,110,70)))

    pygame.display.update(dirty_rects)


def draw_feature_animation(s, num):
    global screen
    dirty_rects = []
 
    
    if num in [8,9,21,22,33,34,46,47]:
        if s.game.before_fourth.status == False:
            p = [25,894]
            dirty_rects.append(screen.blit(time, p))
            pygame.display.update(dirty_rects)
            return
    if num in [4,5,17,18,29,30,42,43]:
        if s.game.before_fifth.status == False:
            p = [609,894]
            dirty_rects.append(screen.blit(time, p))
            pygame.display.update(dirty_rects)
            return
    if num in [6,7,19,20,31,32,44,45]:
        if s.game.magic_lines_feature.position < 4:
            p = [226,908]
            dirty_rects.append(screen.blit(magic_lines, p))
            pygame.display.update(dirty_rects)
            return
    if num in [12,13,37,38]:
        if s.game.red_star.status == False:
            p = [638,276]
            dirty_rects.append(screen.blit(star, p))
            pygame.display.update(dirty_rects)
            s.game.coils.redROLamp.pulse(85)
            return
    if num in [14,39]:
        if s.game.yellow_star.status == False:
            p = [14,273]
            dirty_rects.append(screen.blit(star, p))
            pygame.display.update(dirty_rects)
            s.game.coils.yellowROLamp.pulse(85)
            return
    if num in [10,11,24,25,35,36,49,0]:
        if s.game.super_card.position < 4:
            p = [51,720]
            dirty_rects.append(screen.blit(sc, p))
            pygame.display.update(dirty_rects)
            return
    if num in [2,3,15,16,27,28,40,41]:
        if s.game.super_card.position < 8:
            p = [562,719]
            dirty_rects.append(screen.blit(sc, p))
            pygame.display.update(dirty_rects)
            return
    if num in [0,1,25,26]:
        if s.game.corners.status == False:
            p = [61,546]
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

