
import pygame
import random

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

meter = pygame.image.load('graphics/assets/register_cover.png').convert()
magic_screen = pygame.image.load('bikini/assets/magic_screen.png').convert()
number_card = pygame.image.load('bikini/assets/number_card.png').convert()
odds = pygame.image.load('bikini/assets/odds.png').convert_alpha()
eb = pygame.image.load('bikini/assets/eb.png').convert_alpha()
eb_number = pygame.image.load('bikini/assets/eb_number.png').convert_alpha()
extra_balls = pygame.image.load('bikini/assets/extra_balls.png').convert_alpha()
time = pygame.image.load('bikini/assets/time.png').convert_alpha()
ms_indicator = pygame.image.load('bikini/assets/ms_indicator.png').convert_alpha()
ti = pygame.image.load('bikini/assets/time_indicator.png').convert_alpha()
super_section = pygame.image.load('bikini/assets/super_section.png').convert_alpha()
orange_section = pygame.image.load('bikini/assets/orange_section.png').convert_alpha()
ms_letter = pygame.image.load('bikini/assets/ms_letter.png').convert_alpha()
number = pygame.image.load('bikini/assets/number.png').convert_alpha()
select_now = pygame.image.load('bikini/assets/select_now.png').convert_alpha()
blue_section = pygame.image.load('bikini/assets/blue_section.png').convert_alpha()
tilt = pygame.image.load('bikini/assets/tilt.png').convert_alpha()
button = pygame.image.load('bikini/assets/button.png').convert_alpha()
futurity = pygame.image.load('bikini/assets/futurity.png').convert_alpha()
bg_menu = pygame.image.load('bikini/assets/bikini_menu.png').convert_alpha()
bg_gi = pygame.image.load('bikini/assets/bikini_gi.png').convert_alpha()
bg_off = pygame.image.load('bikini/assets/bikini_off.png').convert_alpha()

class scorereel():
    """ Score Reels are used to count replays """
    def __init__(self, pos, image):
        self.position = pos
        self.default_y = self.position[1]
        self.image = pygame.image.load(image).convert()

reel1 = scorereel([102,805], "graphics/assets/white_reel.png")
reel10 = scorereel([83,805], "graphics/assets/white_reel.png")
reel100 = scorereel([64,805], "graphics/assets/white_reel.png")

def display(s, replays=0, menu=False):
    
    meter.set_colorkey((255,0,252))
    meter_position = [55,805]

    screen.blit(reel1.image, reel1.position)
    screen.blit(reel10.image, reel10.position)
    screen.blit(reel100.image, reel100.position)
    screen.blit(meter, meter_position)

    number_card_position = [235,363]

    screen.blit(number_card, number_card_position)

    magic_screen.set_colorkey((255,0,252))
    #default position 230x 359y
    #subtract 47 per position
    if s.game.magic_screen.position == 0:
        magic_screen_position = [240,358]
    elif s.game.magic_screen.position == 1:
        magic_screen_position = [192,358]
    elif s.game.magic_screen.position == 2:
        magic_screen_position = [145,358]
    elif s.game.magic_screen.position == 3:
        magic_screen_position = [96,358]
    elif s.game.magic_screen.position == 4:
        magic_screen_position = [49,358]
    elif s.game.magic_screen.position == 5:
        magic_screen_position = [3,358]
    elif s.game.magic_screen.position == 6:
        magic_screen_position = [-45,358]
    elif s.game.magic_screen.position == 7:
        magic_screen_position = [-92,358]
    elif s.game.magic_screen.position == 8:
        magic_screen_position = [-139,358]
    elif s.game.magic_screen.position == 9:
        magic_screen_position = [-187,358]


    screen.blit(magic_screen, magic_screen_position)

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

    if s.game.eb_play.status == True:
        eb_position = [37,1053]
        screen.blit(extra_balls, eb_position)

    if s.game.extra_ball.position >= 1:
        eb_position = [151,1051]
        screen.blit(eb_number, eb_position)
    if s.game.extra_ball.position >= 2:
        eb_position = [198,1051]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 3:
        eb_position = [263,1051]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 4:
        eb_position = [329,1051]
        screen.blit(eb_number, eb_position)
    if s.game.extra_ball.position >= 5:
        eb_position = [375,1051]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 6:
        eb_position = [439,1051]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 7:
        eb_position = [506,1051]
        screen.blit(eb_number, eb_position)
    if s.game.extra_ball.position >= 8:
        eb_position = [556,1051]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 9:
        eb_position = [617,1051]
        screen.blit(eb, eb_position)
    

    if s.game.selection_feature.position == 1:
        i = [672,594]
        screen.blit(ti, i)
    if s.game.selection_feature.position == 2 or s.game.selection_feature.position == 3:
        i = [672,534]
        screen.blit(ti, i)
    if s.game.selection_feature.position == 4 or s.game.selection_feature.position == 5 or s.game.selection_feature.position == 6:
        i = [672,474]
        screen.blit(ti, i)
    if s.game.selection_feature.position == 7:
        i = [672,417]
        screen.blit(ti, i)
    if s.game.selection_feature.position == 8:
        i = [672,355]
        screen.blit(ti, i)

    if s.game.red_star.status == True:
        rs_position = [552,458]
        screen.blit(time, rs_position)
    if s.game.yellow_star.status == True:
        rs_position = [552,518]
        screen.blit(time, rs_position)

    if s.game.magic_screen_feature.position >= 7 or s.game.ok.status == True:
        if s.game.selection_feature.position < 7:
            bfp = [552,575]
            screen.blit(time, bfp)
            if s.game.ball_count.position == 3:
                s.cancel_delayed(name="blink")
                blink([s,1,1])
            else:
                s.cancel_delayed(name="blink")
        elif s.game.selection_feature.position == 7:
            bfp = [552,400]
            screen.blit(time, bfp)
            if s.game.ball_count.position == 4:
                s.cancel_delayed(name="blink")
                blink([s,1,1])
            else:
                s.cancel_delayed(name="blink")
        elif s.game.selection_feature.position == 8:
            bfp = [553,340]
            screen.blit(time, bfp)
            if s.game.ball_count.position == 5:
                s.cancel_delayed(name="blink")
                blink([s,1,1])
            else:
                s.cancel_delayed(name="blink")

    if s.game.magic_screen_feature.position >= 9:
        if s.game.three_blue.status == True:
            bp = [45,330]
            screen.blit(blue_section, bp)
        elif s.game.three_blue_six.status == True:
            bp = [88,330]
            screen.blit(blue_section, bp)
        elif s.game.two_blue.status == True:
            bp = [133,330]
            screen.blit(blue_section, bp)


    if s.game.ball_count.position < 1 or s.game.extra_ball.position > 0:
        if s.game.eb_play.status == False:
            if s.game.odds_only.status == True:
                b = [18,887]
                screen.blit(button, b)
            elif s.game.features.status == True:
                b = [18,937]
                screen.blit(button, b)
            else:
                b = [18,990]
                screen.blit(button, b)


    if s.game.red_super_section.status == True:
        rss = [50,410]
        screen.blit(super_section, rss)
    if s.game.yellow_super_section.status == True:
        yss = [53,490]
        screen.blit(super_section, yss)
    if s.game.orange_section.status == True:
        oss = [53,572]
        screen.blit(orange_section, oss)

    if s.game.magic_screen_feature.position >= 4:
        ms = [155,675]
        screen.blit(ms_letter, ms)
    if s.game.magic_screen_feature.position >= 5:
        ms = [197,675]
        screen.blit(ms_letter, ms)
    if s.game.magic_screen_feature.position >= 6:
        ms = [239,675]
        screen.blit(ms_letter, ms)
    if s.game.magic_screen_feature.position >= 7:
        ms = [280,675]
        screen.blit(ms_letter, ms)
    if s.game.magic_screen_feature.position >= 8:
        ms = [324,675]
        screen.blit(ms_letter, ms)
    if s.game.magic_screen_feature.position >= 9:
        ms = [364,675]
        screen.blit(ms_letter, ms)
    if s.game.magic_screen_feature.position >= 10:
        ms = [405,675]
        screen.blit(ms_letter, ms)

    if s.game.ok.status == True:
        ms = [70,675]
        screen.blit(ms_letter, ms)
        ms = [28,675]
        screen.blit(ms_letter, ms)


    if s.game.magic_screen.position == 0:
        ms = [35,730]
        screen.blit(ms_indicator, ms)
    if s.game.magic_screen.position == 1:
        ms = [78,730]
        screen.blit(ms_indicator, ms)
    if s.game.magic_screen.position == 3:
        ms = [165,730]
        screen.blit(ms_indicator, ms)
    if s.game.magic_screen.position == 4:
        ms = [207,730]
        screen.blit(ms_indicator, ms)
    if s.game.magic_screen.position == 5:
        ms = [245,730]
        screen.blit(ms_indicator, ms)
    if s.game.magic_screen.position == 6:
        ms = [287,730]
        screen.blit(ms_indicator, ms)
    if s.game.magic_screen.position == 7:
        ms = [330,730]
        screen.blit(ms_indicator, ms)
    if s.game.magic_screen.position == 8:
        ms = [369,730]
        screen.blit(ms_indicator, ms)
    if s.game.magic_screen.position == 9:
        ms = [409,730]
        screen.blit(ms_indicator, ms)

    if s.game.tilt.status == False:
        if s.holes:
            if 1 in s.holes:
                number_position = [287,373]
                screen.blit(number, number_position)
            if 2 in s.holes:
                number_position = [333,373]
                screen.blit(number, number_position)
            if 3 in s.holes:
                number_position = [382,568]
                screen.blit(number, number_position)
            if 4 in s.holes:
                number_position = [238,423]
                screen.blit(number, number_position)
            if 5 in s.holes:
                number_position = [335,520]
                screen.blit(number, number_position)
            if 6 in s.holes:
                number_position = [238,520]
                screen.blit(number, number_position)
            if 7 in s.holes:
                number_position = [333,423]
                screen.blit(number, number_position)
            if 8 in s.holes:
                number_position = [286,568]
                screen.blit(number, number_position)
            if 9 in s.holes:
                number_position = [240,374]
                screen.blit(number, number_position)
            if 10 in s.holes:
                number_position = [430,565]
                screen.blit(number, number_position)
            if 11 in s.holes:
                number_position = [382,373]
                screen.blit(number, number_position)
            if 12 in s.holes:
                number_position = [238,568]
                screen.blit(number, number_position)
            if 13 in s.holes:
                number_position = [382,470]
                screen.blit(number, number_position)
            if 14 in s.holes:
                number_position = [334,569]
                screen.blit(number, number_position)
            if 15 in s.holes:
                number_position = [428,373]
                screen.blit(number, number_position)
            if 16 in s.holes:
                number_position = [334,470]
                screen.blit(number, number_position)
            if 17 in s.holes:
                number_position = [428,470]
                screen.blit(number, number_position)
            if 18 in s.holes:
                number_position = [428,423]
                screen.blit(number, number_position)
            if 19 in s.holes:
                number_position = [285,421]
                screen.blit(number, number_position)
            if 20 in s.holes:
                number_position = [430,520]
                screen.blit(number, number_position)
            if 21 in s.holes:
                number_position = [382,520]
                screen.blit(number, number_position)
            if 22 in s.holes:
                number_position = [382,421]
                screen.blit(number, number_position)
            if 23 in s.holes:
                number_position = [286,520]
                screen.blit(number, number_position)
            if 24 in s.holes:
                number_position = [286,470]
                screen.blit(number, number_position)
            if 25 in s.holes:
                number_position = [240,470]
                screen.blit(number, number_position)

    if s.game.red_odds.position == 1:
        o = [187,786]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 2:
        o = [247,786]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 3:
        o = [309,786]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 4:
        o = [370,786]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 5:
        o = [423,786]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 6:
        o = [472,786]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 7:
        o = [522,786]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 8:
        o = [568,786]
        screen.blit(odds, o)

    if s.game.yellow_odds.position == 1:
        o = [187,858]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 2:
        o = [247,858]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 3:
        o = [309,858]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 4:
        o = [370,858]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 5:
        o = [423,858]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 6:
        o = [472,858]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 7:
        o = [522,858]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 8:
        o = [568,858]
        screen.blit(odds, o)

    if s.game.green_odds.position == 1:
        o = [187,930]
        screen.blit(odds, o)
        p = [36,263]
        screen.blit(futurity, p)
    elif s.game.green_odds.position == 2:
        o = [247,930]
        screen.blit(odds, o)
        p = [36,263]
        screen.blit(futurity, p)
    elif s.game.green_odds.position == 3:
        o = [309,930]
        screen.blit(odds, o)
        p = [36,263]
        screen.blit(futurity, p)
    elif s.game.green_odds.position == 4:
        o = [370,930]
        screen.blit(odds, o)
        p = [67,263]
        screen.blit(futurity, p)
    elif s.game.green_odds.position == 5:
        o = [423,930]
        screen.blit(odds, o)
        p = [98,263]
        screen.blit(futurity, p)
    elif s.game.green_odds.position == 6:
        o = [472,930]
        screen.blit(odds, o)
        p = [131,263]
        screen.blit(futurity, p)
    elif s.game.green_odds.position == 7:
        o = [522,930]
        screen.blit(odds, o)
        p = [160,263]
        screen.blit(futurity, p)
    elif s.game.green_odds.position == 8:
        o = [568,930]
        screen.blit(odds, o)
        p = [192,263]
        screen.blit(futurity, p)

    if s.game.futurity.position == 1:
        p = [496,243]
        screen.blit(futurity, p)
    if s.game.futurity.position == 2:
        p = [526,243]
        screen.blit(futurity, p)
    if s.game.futurity.position == 3:
        p = [557,243]
        screen.blit(futurity, p)
    if s.game.futurity.position == 4:
        p = [588,243]
        screen.blit(futurity, p)
    if s.game.futurity.position == 5:
        p = [621,243]
        screen.blit(futurity, p)
    if s.game.futurity.position == 6:
        p = [651,243]
        screen.blit(futurity, p)
    if s.game.futurity.position == 7:
        p = [496,278]
        screen.blit(futurity, p)
    if s.game.futurity.position == 8:
        p = [526,278]
        screen.blit(futurity, p)
    if s.game.futurity.position == 9:
        p = [557,278]
        screen.blit(futurity, p)
    if s.game.futurity.position == 10:
        p = [588,278]
        screen.blit(futurity, p)
    if s.game.futurity.position == 11:
        p = [621,278]
        screen.blit(futurity, p)
    if s.game.futurity.position == 12:
        p = [651,278]
        screen.blit(futurity, p)


    if s.game.tilt.status == True:
        tilt_position = [572,635]
        screen.blit(tilt, tilt_position)

    pygame.display.update()

def blink(args):
    dirty_rects = []
    s = args[0]
    b = args[1]
    sn = args[2]

    if b == 0:
        if sn == 1:
            p = [577,684]
            dirty_rects.append(screen.blit(select_now, p))
        pygame.display.update(dirty_rects)
    else:
        dirty_rects.append(screen.blit(bg_gi, (577,684), pygame.Rect(577,684,124,36)))
        pygame.display.update(dirty_rects)
    b = not b

    args = [s,b,sn]

    s.delay(name="blink", delay=0.1, handler=blink, param=args)

def screen_animation(args):
    dirty_rects = []
    s = args[0]
    num = args[1]
    direction = args[2]
    
    number_card_position = [235,363]

    dirty_rects.append(screen.blit(number_card, number_card_position))

    magic_screen.set_colorkey((255,0,252))

    if s.game.magic_screen.position == 0:
        p = [240,358]
    elif s.game.magic_screen.position == 1:
        p = [192,358]
    elif s.game.magic_screen.position == 2:
        p = [145,358]
    elif s.game.magic_screen.position == 3:
        p = [96,358]
    elif s.game.magic_screen.position == 4:
        p = [49,358]
    elif s.game.magic_screen.position == 5:
        p = [3,358]
    elif s.game.magic_screen.position == 6:
        p = [-45,358]
    elif s.game.magic_screen.position == 7:
        p = [-92,358]
    elif s.game.magic_screen.position == 8:
        p = [-139,358]
    elif s.game.magic_screen.position == 9:
        p = [-187,358]

    if direction == "left":
       p[0] = p[0] + num
    else:
       p[0] = p[0] - num
 
    dirty_rects.append(screen.blit(magic_screen, p))
    
    backglass_position = [0, 0]
    if (s.game.anti_cheat.status == True):
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],660,270)))
    else:
        dirty_rects.append(screen.blit(bg_off, p, pygame.Rect(p[0],p[1],660,270)))
    
    if s.game.magic_screen_feature.position >= 9:
        if s.game.three_blue.status == True:
            bp = [45,330]
            dirty_rects.append(screen.blit(bg_gi, bp, pygame.Rect(bp[0],bp[1],46,77)))
            dirty_rects.append(screen.blit(blue_section, bp))
        elif s.game.three_blue_six.status == True:
            bp = [88,330]
            dirty_rects.append(screen.blit(bg_gi, bp, pygame.Rect(bp[0],bp[1],46,77)))
            dirty_rects.append(screen.blit(blue_section, bp))
        elif s.game.two_blue.status == True:
            bp = [133,330]
            dirty_rects.append(screen.blit(bg_gi, bp, pygame.Rect(bp[0],bp[1],46,77)))
            dirty_rects.append(screen.blit(blue_section, bp))

    if s.game.magic_screen_feature.position >= 7 or s.game.ok.status == True:
        if s.game.selection_feature.position < 7:
            bfp = [552,575]
            dirty_rects.append(screen.blit(bg_gi, bfp, pygame.Rect(bfp[0],bfp[1],120,58)))
            dirty_rects.append(screen.blit(time, bfp))
        elif s.game.selection_feature.position == 7:
            bfp = [552,400]
            dirty_rects.append(screen.blit(bg_gi, bfp, pygame.Rect(bfp[0],bfp[1],120,58)))
            screen.blit(time, bfp)
        elif s.game.selection_feature.position == 8:
            bfp = [553,340]
            dirty_rects.append(screen.blit(bg_gi, bfp, pygame.Rect(bfp[0],bfp[1],120,58)))
            screen.blit(time, bfp)
        
    if s.game.selection_feature.position == 1:
        i = [672,594]
        dirty_rects.append(screen.blit(bg_gi, i, pygame.Rect(i[0],i[1],120,58)))
        dirty_rects.append(screen.blit(ti, i))
    if s.game.selection_feature.position == 2 or s.game.selection_feature.position == 3:
        i = [672,534]
        dirty_rects.append(screen.blit(bg_gi, i, pygame.Rect(i[0],i[1],120,58)))
        dirty_rects.append(screen.blit(ti, i))
    if s.game.selection_feature.position == 4 or s.game.selection_feature.position == 5 or s.game.selection_feature.position == 6:
        i = [672,474]
        dirty_rects.append(screen.blit(bg_gi, i, pygame.Rect(i[0],i[1],120,58)))
        dirty_rects.append(screen.blit(ti, i))
    if s.game.selection_feature.position == 7:
        i = [672,417]
        dirty_rects.append(screen.blit(bg_gi, i, pygame.Rect(i[0],i[1],120,58)))
        dirty_rects.append(screen.blit(ti, i))
    if s.game.selection_feature.position == 8:
        i = [672,355]
        dirty_rects.append(screen.blit(bg_gi, i, pygame.Rect(i[0],i[1],120,58)))
        dirty_rects.append(screen.blit(ti, i))

    if s.game.red_star.status == True:
        rs_position = [552,458]
        dirty_rects.append(screen.blit(bg_gi, rs_position, pygame.Rect(rs_position[0],rs_position[1],120,58)))
        dirty_rects.append(screen.blit(time, rs_position))
    if s.game.yellow_star.status == True:
        rs_position = [552,518]
        dirty_rects.append(screen.blit(bg_gi, rs_position, pygame.Rect(rs_position[0],rs_position[1],120,58)))
        dirty_rects.append(screen.blit(time, rs_position))

    if s.game.red_super_section.status == True:
        rss = [50,410]
        dirty_rects.append(screen.blit(bg_gi, (50,410), pygame.Rect(50,410,121,81)))
        dirty_rects.append(screen.blit(super_section, rss))
    if s.game.yellow_super_section.status == True:
        yss = [53,490]
        dirty_rects.append(screen.blit(bg_gi, (53,490), pygame.Rect(53,490,121,81)))
        dirty_rects.append(screen.blit(super_section, yss))
    if s.game.orange_section.status == True:
        oss = [53,572]
        dirty_rects.append(screen.blit(bg_gi, (53,572), pygame.Rect(53,572,121,64)))
        dirty_rects.append(screen.blit(orange_section, oss))

    pygame.display.update(dirty_rects)

def eb_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]

    if s.game.extra_ball.position < 1:
        dirty_rects.append(screen.blit(bg_gi, (151,1051), pygame.Rect(151,1051,50,39)))
    if s.game.extra_ball.position < 2:
        dirty_rects.append(screen.blit(bg_gi, (198,1051), pygame.Rect(198,1051,69,37)))
    if s.game.extra_ball.position < 3:
        dirty_rects.append(screen.blit(bg_gi, (263,1051), pygame.Rect(263,1051,69,37)))
    if s.game.extra_ball.position < 4:
        dirty_rects.append(screen.blit(bg_gi, (329,1051), pygame.Rect(329,1051,50,39)))
    if s.game.extra_ball.position < 5:
        dirty_rects.append(screen.blit(bg_gi, (375,1051), pygame.Rect(375,1051,69,37)))
    if s.game.extra_ball.position < 6:
        dirty_rects.append(screen.blit(bg_gi, (439,1051), pygame.Rect(439,1051,69,37)))
    if s.game.extra_ball.position < 7:
        dirty_rects.append(screen.blit(bg_gi, (506,1051), pygame.Rect(506,1051,50,39)))
    if s.game.extra_ball.position < 8:
        dirty_rects.append(screen.blit(bg_gi, (556,1051), pygame.Rect(556,1051,69,37)))
    if s.game.extra_ball.position < 9:
        dirty_rects.append(screen.blit(bg_gi, (617,1051), pygame.Rect(617,1051,69,37)))
    pygame.display.update(dirty_rects)

    if num in [0,25,14,49]:
        if s.game.extra_ball.position < 1:
            p = [151,1051]
            dirty_rects.append(screen.blit(eb_number, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [39,1,26,15]:
        if s.game.extra_ball.position < 2:
            p = [198,1051]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [3,4,17,28,29,40]:
        if s.game.extra_ball.position < 3:
            p = [263,1051]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [5,18,30,43]:
        if s.game.extra_ball.position < 4:
            p = [329,1051]
            dirty_rects.append(screen.blit(eb_number, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [7,8,19,32,33,44]:
        if s.game.extra_ball.position < 5:
            p = [375,1051]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [9,10,20,34,35,45]:
        if s.game.extra_ball.position < 6:
            p = [439,1051]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [11,21,36,46]:
        if s.game.extra_ball.position < 7:
            p = [506,1051]
            dirty_rects.append(screen.blit(eb_number, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [12,22,37,47]:
        if s.game.extra_ball.position < 8:
            p = [556,1051]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [2,6,13,16,23,27,31,38,41,48]:
        if s.game.extra_ball.position < 9:
            p = [617,1051]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return

def clear_odds(s, num):
    global screen

    dirty_rects = []

    if s.game.yellow_odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (187,858), pygame.Rect(187,858,45,71)))
    if s.game.yellow_odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (247,858), pygame.Rect(247,858,45,71)))
    if s.game.yellow_odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (309,858), pygame.Rect(309,858,45,71)))
    if s.game.yellow_odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (370,858), pygame.Rect(370,858,45,71)))
    if s.game.yellow_odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (423,858), pygame.Rect(423,858,45,71)))
    if s.game.yellow_odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (472,858), pygame.Rect(472,858,45,71)))
    if s.game.yellow_odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (522,858), pygame.Rect(522,858,45,71)))
    if s.game.yellow_odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (568,858), pygame.Rect(568,858,45,71)))

    if s.game.red_odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (187,786), pygame.Rect(187,786,45,71)))
    if s.game.red_odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (247,786), pygame.Rect(247,786,45,71)))
    if s.game.red_odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (309,786), pygame.Rect(309,786,45,71)))
    if s.game.red_odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (370,786), pygame.Rect(370,786,45,71)))
    if s.game.red_odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (423,786), pygame.Rect(423,786,45,71)))
    if s.game.red_odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (472,786), pygame.Rect(472,786,45,71)))
    if s.game.red_odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (522,786), pygame.Rect(522,786,45,71)))
    if s.game.red_odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (568,786), pygame.Rect(568,786,45,71)))

    if s.game.green_odds.position not in [1,2,3]:
        dirty_rects.append(screen.blit(bg_gi, (36,263), pygame.Rect(36,263,37,41)))
    if s.game.green_odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (187,930), pygame.Rect(187,930,45,71)))
    if s.game.green_odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (247,930), pygame.Rect(247,930,45,71)))
    if s.game.green_odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (309,930), pygame.Rect(309,930,45,71)))
    if s.game.green_odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (370,930), pygame.Rect(370,930,45,71)))
        dirty_rects.append(screen.blit(bg_gi, (67,263), pygame.Rect(67,263,37,41)))
    if s.game.green_odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (423,930), pygame.Rect(423,930,45,71)))
        dirty_rects.append(screen.blit(bg_gi, (98,263), pygame.Rect(98,263,37,41)))
    if s.game.green_odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (472,930), pygame.Rect(472,930,45,71)))
        dirty_rects.append(screen.blit(bg_gi, (131,263), pygame.Rect(131,263,37,41)))
    if s.game.green_odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (522,930), pygame.Rect(522,930,45,71)))
        dirty_rects.append(screen.blit(bg_gi, (160,263), pygame.Rect(160,263,37,41)))
    if s.game.green_odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (568,930), pygame.Rect(568,930,45,71)))
        dirty_rects.append(screen.blit(bg_gi, (192,263), pygame.Rect(192,263,37,41)))

    pygame.display.update(dirty_rects)

def draw_odds_animation(s, num):
    global screen
    dirty_rects = []

    if num in [11,26]:
        if s.game.yellow_odds.position != 1:
            p = [187,858]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [4,29]:
        if s.game.yellow_odds.position != 2:
            p = [247,858]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [7,32]:
        if s.game.yellow_odds.position != 3:
            p = [309,858]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [13,38]:
        if s.game.yellow_odds.position != 4:
            p = [370,858]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [22,47]:
        if s.game.yellow_odds.position != 5:
            p = [423,858]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [17,42]:
        if s.game.yellow_odds.position != 6:
            p = [472,858]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [19,44]:
        if s.game.yellow_odds.position != 7:
            p = [522,858]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [5,30]:
        if s.game.yellow_odds.position != 8:
            p = [568,858]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [0,25]:
        if s.game.red_odds.position != 1:
            p = [187,786]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [15,40]:
        if s.game.red_odds.position != 2:
            p = [247,786]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [24,49]:
        if s.game.red_odds.position != 3:
            p = [309,786]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [9,34]:
        if s.game.red_odds.position != 4:
            p = [370,786]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [20,45]:
        if s.game.red_odds.position != 5:
            p = [423,786]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [12,37]:
        if s.game.red_odds.position != 6:
            p = [472,786]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [50,26]:
        if s.game.red_odds.position != 7:
            p = [522,786]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [6,31]:
        if s.game.red_odds.position != 8:
            p = [568,786]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return

    if num in [16,41]:
        if s.game.green_odds.position != 1:
            p = [187,930]
            dirty_rects.append(screen.blit(odds, p))
            if s.game.green_odds.position not in [1,2,3]:
                p = [36,263]
                dirty_rects.append(screen.blit(futurity, p))
            pygame.display.update(dirty_rects)
            #FUTURITY 1
            return
    if num in [18,43]:
        if s.game.green_odds.position != 2:
            p = [247,930]
            dirty_rects.append(screen.blit(odds, p))
            if s.game.green_odds.position not in [1,2,3]:
                p = [36,263]
                dirty_rects.append(screen.blit(futurity, p))
            pygame.display.update(dirty_rects)
            #FUTURITY 1
            return
    if num in [14,39]:
        if s.game.green_odds.position != 3:
            p = [309,930]
            dirty_rects.append(screen.blit(odds, p))
            if s.game.green_odds.position not in [1,2,3]:
                p = [36,263]
                dirty_rects.append(screen.blit(futurity, p))
            pygame.display.update(dirty_rects)
            # FUTURITY 1
            return
    if num in [3,28]:
        if s.game.green_odds.position != 4:
            p = [370,930]
            dirty_rects.append(screen.blit(odds, p))
            p = [67,263]
            dirty_rects.append(screen.blit(futurity, p))
            pygame.display.update(dirty_rects)
            #FUTURITY 2
            return
    if num in [23,48]:
        if s.game.green_odds.position != 5:
            p = [423,930]
            dirty_rects.append(screen.blit(odds, p))
            p = [98,263]
            dirty_rects.append(screen.blit(futurity, p))
            pygame.display.update(dirty_rects)
            #FUTURITY 3
            return
    if num in [8,33]:
        if s.game.green_odds.position != 6:
            p = [472,930]
            dirty_rects.append(screen.blit(odds, p))
            p = [131,263]
            dirty_rects.append(screen.blit(futurity, p))
            pygame.display.update(dirty_rects)
            #FUTURITY 4
            return
    if num in [22,47]:
        if s.game.green_odds.position != 7:
            p = [522,930]
            dirty_rects.append(screen.blit(odds, p))
            p = [160,263]
            dirty_rects.append(screen.blit(futurity, p))
            pygame.display.update(dirty_rects)
            #FUTURITY 5
            return
    if num in [10,35]:
        if s.game.green_odds.position != 8:
            p = [568,930]
            dirty_rects.append(screen.blit(odds, p))
            p = [192,263]
            dirty_rects.append(screen.blit(futurity, p))
            pygame.display.update(dirty_rects)
            #FUTURITY 6
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


    if s.game.selection_feature.position < 7 and (s.game.magic_screen_feature.position < 4 and s.game.ok.status == False):
        dirty_rects.append(screen.blit(bg_gi, (552,575), pygame.Rect(552,575,120,58)))
    if s.game.red_star.status == False:
        dirty_rects.append(screen.blit(bg_gi, (552,458), pygame.Rect(552,458,120,58)))
    if s.game.yellow_star.status == False:
        dirty_rects.append(screen.blit(bg_gi, (552,518), pygame.Rect(552,518,120,58)))
    if s.game.selection_feature.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (552,400), pygame.Rect(552,400,120,58)))
    if s.game.selection_feature.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (553,340), pygame.Rect(553,340,120,58)))

    if s.game.yellow_super_section.status == False:
        dirty_rects.append(screen.blit(bg_gi, (53,490), pygame.Rect(53,490,121,81)))
    if s.game.red_super_section.status == False:
        dirty_rects.append(screen.blit(bg_gi, (50,410), pygame.Rect(50,410,121,81)))
    if s.game.orange_section.status == False:
        dirty_rects.append(screen.blit(bg_gi, (53,572), pygame.Rect(53,572,121,64)))
    if s.game.ok.status == False:
        dirty_rects.append(screen.blit(bg_gi, (70,675), pygame.Rect(70,675,45,56)))
        dirty_rects.append(screen.blit(bg_gi, (28,675), pygame.Rect(28,675,45,56)))
    if s.game.magic_screen_feature.position < 7:
        dirty_rects.append(screen.blit(bg_gi, (155,675), pygame.Rect(155,675,45,56)))
        dirty_rects.append(screen.blit(bg_gi, (197,675), pygame.Rect(197,675,45,56)))
        dirty_rects.append(screen.blit(bg_gi, (239,675), pygame.Rect(239,675,45,56)))
        dirty_rects.append(screen.blit(bg_gi, (280,675), pygame.Rect(280,675,45,56)))
    if s.game.magic_screen_feature.position < 8:
        dirty_rects.append(screen.blit(bg_gi, (324,675), pygame.Rect(324,675,45,56)))
    if s.game.magic_screen_feature.position < 9:
        dirty_rects.append(screen.blit(bg_gi, (364,675), pygame.Rect(364,675,45,56)))
    if s.game.magic_screen_feature.position < 10:
        dirty_rects.append(screen.blit(bg_gi, (405,675), pygame.Rect(405,675,45,56)))
    if s.game.three_blue.status == False:
       dirty_rects.append(screen.blit(bg_gi, (45,330), pygame.Rect(45,330,46,77)))
    if s.game.three_blue_six.status == False:
       dirty_rects.append(screen.blit(bg_gi, (88,330), pygame.Rect(88,330,46,77)))
    if s.game.two_blue.status == False:
        dirty_rects.append(screen.blit(bg_gi, (133,330), pygame.Rect(133,330,46,77)))

    pygame.display.update(dirty_rects)


def draw_feature_animation(s, num):
    global screen
    dirty_rects = []
 
    if num in [10,35]:
        if (s.game.magic_screen_feature.position < 4 and s.game.ok.status == False) and s.game.selection_feature.position not in [7,8]:
            p = [552,575]
            dirty_rects.append(screen.blit(time, p))
            pygame.display.update(dirty_rects)
            return
    if num in [9,34]:
        if s.game.selection_feature.position != 7:
            p = [552,400]
            dirty_rects.append(screen.blit(time, p))
            pygame.display.update(dirty_rects)
            return
    if num in [6,17,21,31,42,46]:
        if s.game.selection_feature.position != 8:
            p = [553,340]
            dirty_rects.append(screen.blit(time, p))
            pygame.display.update(dirty_rects)
            return
    if num in [4,29]:
        if s.game.red_star.status == False:
            p = [552,458]
            dirty_rects.append(screen.blit(time, p))
            s.game.coils.redROLamp.pulse(85)
            pygame.display.update(dirty_rects)
            return
    if num in [11,36]:
        if s.game.yellow_star.status == False:
            p = [552,518]
            dirty_rects.append(screen.blit(time, p))
            s.game.coils.yellowROLamp.pulse(85)
            pygame.display.update(dirty_rects)
            return
    if num in [7,32]:
        if s.game.yellow_super_section.status == False:
            if s.game.red_super_section.status == False:
                p = [53,490]
                dirty_rects.append(screen.blit(super_section, p))
                pygame.display.update(dirty_rects)
                return
    if num in [18,0,43,25]:
        if s.game.red_super_section.status == False:
            if s.game.yellow_super_section.status == False:
                p = [50,410]
                dirty_rects.append(screen.blit(super_section, p))
                pygame.display.update(dirty_rects)
                return
    if num in [13,19,38,44]:
        if s.game.orange_section.status == False:
            p = [53,572]
            dirty_rects.append(screen.blit(orange_section, p))
            pygame.display.update(dirty_rects)
            return
    if num in [16,41]:
        if s.game.ok.status == False:
            p = [70,675]
            dirty_rects.append(screen.blit(ms_letter, p))
            p = [28,675]
            dirty_rects.append(screen.blit(ms_letter, p))
            pygame.display.update(dirty_rects)
            return
    if num in [2,12,27,37]:
        if s.game.magic_screen_feature.position < 7:
            p = [155,675]
            dirty_rects.append(screen.blit(ms_letter, p))
            p = [197,675]
            dirty_rects.append(screen.blit(ms_letter, p))
            p = [239,675]
            dirty_rects.append(screen.blit(ms_letter, p))
            p = [280,675]
            dirty_rects.append(screen.blit(ms_letter, p))
            pygame.display.update(dirty_rects)
            return
    if num in [3,22,28,47]:
        if s.game.magic_screen_feature.position < 8:
            p = [324,675]
            dirty_rects.append(screen.blit(ms_letter, p))
            pygame.display.update(dirty_rects)
            return
    if num in [1,14,26,39]:
        if s.game.magic_screen_feature.position < 9:
            p = [364,675]
            dirty_rects.append(screen.blit(ms_letter, p))
            pygame.display.update(dirty_rects)
            return
    if num in [5,15,30,40]:
        if s.game.magic_screen_feature.position < 10:
            p = [405,675]
            dirty_rects.append(screen.blit(ms_letter, p))
            pygame.display.update(dirty_rects)
            return
    if num in [8,33]:
        if s.game.three_blue.status == False:
            p = [45,330]
            dirty_rects.append(screen.blit(blue_section, p))
            pygame.display.update(dirty_rects)
            return
        else:
            p = [88,330]
            dirty_rects.append(screen.blit(blue_section, p))
            pygame.display.update(dirty_rects)
            return
    if num in [20,45]:
        if s.game.two_blue.status == False:
            p = [133,330]
            dirty_rects.append(screen.blit(blue_section, p))
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

