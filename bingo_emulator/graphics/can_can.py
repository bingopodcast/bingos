
import pygame
import random

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

meter = pygame.image.load('graphics/assets/register_cover.png').convert()
magic_screen = pygame.image.load('can_can/assets/magic_screen.png').convert()
number_card = pygame.image.load('can_can/assets/number_card.png').convert()
odds = pygame.image.load('can_can/assets/odds.png').convert_alpha()
eb = pygame.image.load('can_can/assets/eb.png').convert_alpha()
eb_number = pygame.image.load('can_can/assets/eb_number.png').convert_alpha()
extra_balls = pygame.image.load('can_can/assets/extra_balls.png').convert_alpha()
time = pygame.image.load('can_can/assets/time.png').convert_alpha()
ms_indicator = pygame.image.load('can_can/assets/ms_indicator.png').convert_alpha()
ti = pygame.image.load('can_can/assets/time_indicator.png').convert_alpha()
super_section = pygame.image.load('can_can/assets/super_section.png').convert_alpha()
orange_section = pygame.image.load('can_can/assets/orange_section.png').convert_alpha()
ms_letter = pygame.image.load('can_can/assets/ms_letter.png').convert_alpha()
number = pygame.image.load('can_can/assets/number.png').convert_alpha()
select_now = pygame.image.load('can_can/assets/select_now.png').convert_alpha()
blue_section = pygame.image.load('can_can/assets/blue_section.png').convert_alpha()
tilt = pygame.image.load('can_can/assets/tilt.png').convert_alpha()
button = pygame.image.load('can_can/assets/button.png').convert_alpha()
letter1 = pygame.image.load('can_can/assets/letter1.png').convert_alpha()
letter2 = pygame.image.load('can_can/assets/letter2.png').convert_alpha()
letter3 = pygame.image.load('can_can/assets/letter3.png').convert_alpha()
letter4 = pygame.image.load('can_can/assets/letter4.png').convert_alpha()
letter5 = pygame.image.load('can_can/assets/letter5.png').convert_alpha()
letter6 = pygame.image.load('can_can/assets/letter6.png').convert_alpha()
red_letter1 = pygame.image.load('can_can/assets/red_letter1.png').convert_alpha()
red_letter2 = pygame.image.load('can_can/assets/red_letter2.png').convert_alpha()
red_letter3 = pygame.image.load('can_can/assets/red_letter3.png').convert_alpha()
red_letter4 = pygame.image.load('can_can/assets/red_letter4.png').convert_alpha()
red_letter5 = pygame.image.load('can_can/assets/red_letter5.png').convert_alpha()
red_letter6 = pygame.image.load('can_can/assets/red_letter6.png').convert_alpha()
bg_menu = pygame.image.load('can_can/assets/can_can_menu.png').convert_alpha()
bg_gi = pygame.image.load('can_can/assets/can_can_gi.png').convert_alpha()
bg_off = pygame.image.load('can_can/assets/can_can_off.png').convert_alpha()

class scorereel():
    """ Score Reels are used to count replays """
    def __init__(self, pos, image):
        self.position = pos
        self.default_y = self.position[1]
        self.image = pygame.image.load(image).convert()

reel1 = scorereel([97,799], "graphics/assets/white_reel.png")
reel10 = scorereel([78,799], "graphics/assets/white_reel.png")
reel100 = scorereel([59,799], "graphics/assets/white_reel.png")

def display(s, replays=0, menu=False):
    
    meter.set_colorkey((255,0,252))
    meter_position = [50,799]

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
        magic_screen_position = [-184,358]


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
        eb_position = [31,1037]
        screen.blit(extra_balls, eb_position)

    if s.game.extra_ball.position >= 1:
        eb_position = [142,1037]
        screen.blit(eb_number, eb_position)
    if s.game.extra_ball.position >= 2:
        eb_position = [189,1037]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 3:
        eb_position = [254,1037]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 4:
        eb_position = [323,1037]
        screen.blit(eb_number, eb_position)
    if s.game.extra_ball.position >= 5:
        eb_position = [371,1037]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 6:
        eb_position = [435,1037]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 7:
        eb_position = [502,1037]
        screen.blit(eb_number, eb_position)
    if s.game.extra_ball.position >= 8:
        eb_position = [552,1037]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 9:
        eb_position = [613,1037]
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
        i = [672,364]
        screen.blit(ti, i)

    if s.game.red_star.status == True:
        rs_position = [550,464]
        screen.blit(time, rs_position)
    if s.game.yellow_star.status == True:
        rs_position = [550,520]
        screen.blit(time, rs_position)

    if s.game.magic_screen_feature.position >= 7 or s.game.ok.status == True:
        if s.game.selection_feature.position < 7:
            bfp = [550,578]
            screen.blit(time, bfp)
            if s.game.ball_count.position == 3:
                s.cancel_delayed(name="blink")
                blink([s,1,1])
            else:
                s.cancel_delayed(name="blink")
        elif s.game.selection_feature.position == 7:
            bfp = [550,408]
            screen.blit(time, bfp)
            if s.game.ball_count.position == 4:
                s.cancel_delayed(name="blink")
                blink([s,1,1])
            else:
                s.cancel_delayed(name="blink")
        elif s.game.selection_feature.position == 8:
            bfp = [550,349]
            screen.blit(time, bfp)
            if s.game.ball_count.position == 5:
                s.cancel_delayed(name="blink")
                blink([s,1,1])
            else:
                s.cancel_delayed(name="blink")

    if s.game.magic_screen_feature.position >= 9:
        if s.game.three_blue.status == True:
            bp = [45,339]
            screen.blit(blue_section, bp)
        elif s.game.three_blue_six.status == True:
            bp = [88,339]
            screen.blit(blue_section, bp)
        elif s.game.two_blue.status == True:
            bp = [133,339]
            screen.blit(blue_section, bp)


    if s.game.ball_count.position < 1:
        if s.game.ss.status == True:
            b = [539,276]
            screen.blit(button, b)
        elif s.game.odds_only.status == True:
            b = [38,224]
            screen.blit(button, b)
        elif s.game.features.status == True:
            b = [37,275]
            screen.blit(button, b)
        else:
            b = [538,225]
            screen.blit(button, b)


    if s.game.red_super_section.status == True:
        rss = [49,415]
        screen.blit(super_section, rss)
    if s.game.yellow_super_section.status == True:
        yss = [47,495]
        screen.blit(super_section, yss)
    if s.game.orange_section.status == True:
        oss = [47,573]
        screen.blit(orange_section, oss)

    if s.game.magic_screen_feature.position >= 4:
        ms = [153,673]
        screen.blit(ms_letter, ms)
    if s.game.magic_screen_feature.position >= 5:
        ms = [195,673]
        screen.blit(ms_letter, ms)
    if s.game.magic_screen_feature.position >= 6:
        ms = [237,673]
        screen.blit(ms_letter, ms)
    if s.game.magic_screen_feature.position >= 7:
        ms = [281,673]
        screen.blit(ms_letter, ms)
    if s.game.magic_screen_feature.position >= 8:
        ms = [321,673]
        screen.blit(ms_letter, ms)
    if s.game.magic_screen_feature.position >= 9:
        ms = [361,673]
        screen.blit(ms_letter, ms)
    if s.game.magic_screen_feature.position >= 10:
        ms = [402,673]
        screen.blit(ms_letter, ms)

    if s.game.ok.status == True:
        ms = [68,673]
        screen.blit(ms_letter, ms)
        ms = [26,673]
        screen.blit(ms_letter, ms)


    if s.game.magic_screen.position == 0:
        ms = [32,730]
        screen.blit(ms_indicator, ms)
    if s.game.magic_screen.position == 1:
        ms = [75,730]
        screen.blit(ms_indicator, ms)
    if s.game.magic_screen.position == 3:
        ms = [162,730]
        screen.blit(ms_indicator, ms)
    if s.game.magic_screen.position == 4:
        ms = [201,730]
        screen.blit(ms_indicator, ms)
    if s.game.magic_screen.position == 5:
        ms = [240,730]
        screen.blit(ms_indicator, ms)
    if s.game.magic_screen.position == 6:
        ms = [283,730]
        screen.blit(ms_indicator, ms)
    if s.game.magic_screen.position == 7:
        ms = [325,730]
        screen.blit(ms_indicator, ms)
    if s.game.magic_screen.position == 8:
        ms = [364,730]
        screen.blit(ms_indicator, ms)
    if s.game.magic_screen.position == 9:
        ms = [405,730]
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
        o = [182,782]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 2:
        o = [242,782]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 3:
        o = [304,782]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 4:
        o = [365,782]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 5:
        o = [418,782]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 6:
        o = [467,782]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 7:
        o = [512,782]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 8:
        o = [563,782]
        screen.blit(odds, o)

    if s.game.yellow_odds.position == 1:
        o = [182,850]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 2:
        o = [242,850]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 3:
        o = [304,850]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 4:
        o = [365,850]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 5:
        o = [418,850]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 6:
        o = [467,850]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 7:
        o = [512,850]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 8:
        o = [563,850]
        screen.blit(odds, o)

    if s.game.green_odds.position == 1:
        o = [182,920]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 2:
        o = [242,920]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 3:
        o = [304,920]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 4:
        o = [365,920]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 5:
        o = [418,920]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 6:
        o = [467,920]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 7:
        o = [512,920]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 8:
        o = [563,920]
        screen.blit(odds, o)

    p = [204,249]
    screen.blit(letter1, p)
    p = [248,249]
    screen.blit(letter2, p)
    p = [301,249]
    screen.blit(letter3, p)
    p = [374,249]
    screen.blit(letter4, p)
    p = [420,249]
    screen.blit(letter5, p)
    p = [472,249]
    screen.blit(letter6, p)

    if s.game.green_odds.position <= 3:
        p = [204,249]
        screen.blit(red_letter1, p)
    if s.game.green_odds.position == 4:
        p = [248,249]
        screen.blit(red_letter2, p)
    if s.game.green_odds.position == 5:
        p = [301,249]
        screen.blit(red_letter3, p)
    if s.game.green_odds.position == 6:
        p = [374,249]
        screen.blit(red_letter4, p)
    if s.game.green_odds.position == 7:
        p = [420,249]
        screen.blit(red_letter5, p)
    if s.game.green_odds.position == 8:
        p = [472,249]
        screen.blit(red_letter6, p)

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
            p = [576,682]
            dirty_rects.append(screen.blit(select_now, p))
        pygame.display.update(dirty_rects)
    else:
        dirty_rects.append(screen.blit(bg_gi, (575,677), pygame.Rect(575,677,123,39)))
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
            bp = [45,339]
            dirty_rects.append(screen.blit(bg_gi, bp, pygame.Rect(bp[0],bp[1],43,72)))
            dirty_rects.append(screen.blit(blue_section, bp))
        elif s.game.three_blue_six.status == True:
            bp = [88,339]
            dirty_rects.append(screen.blit(bg_gi, bp, pygame.Rect(bp[0],bp[1],43,72)))
            dirty_rects.append(screen.blit(blue_section, bp))
        elif s.game.two_blue.status == True:
            bp = [133,339]
            dirty_rects.append(screen.blit(bg_gi, bp, pygame.Rect(bp[0],bp[1],43,72)))
            dirty_rects.append(screen.blit(blue_section, bp))

    if s.game.magic_screen_feature.position >= 7 or s.game.ok.status == True:
        if s.game.selection_feature.position < 7:
            bfp = [550,578]
            dirty_rects.append(screen.blit(bg_gi, bfp, pygame.Rect(bfp[0],bfp[1],118,55)))
            dirty_rects.append(screen.blit(time, bfp))
        elif s.game.selection_feature.position == 7:
            bfp = [550,408]
            dirty_rects.append(screen.blit(bg_gi, bfp, pygame.Rect(bfp[0],bfp[1],118,55)))
            screen.blit(time, bfp)
        elif s.game.selection_feature.position == 8:
            bfp = [550,349]
            dirty_rects.append(screen.blit(bg_gi, bfp, pygame.Rect(bfp[0],bfp[1],118,55)))
            screen.blit(time, bfp)
        
    if s.game.selection_feature.position == 1:
        i = [672,594]
        dirty_rects.append(screen.blit(bg_gi, i, pygame.Rect(i[0],i[1],39,29)))
        dirty_rects.append(screen.blit(ti, i))
    if s.game.selection_feature.position == 2 or s.game.selection_feature.position == 3:
        i = [672,534]
        dirty_rects.append(screen.blit(bg_gi, i, pygame.Rect(i[0],i[1],39,29)))
        dirty_rects.append(screen.blit(ti, i))
    if s.game.selection_feature.position == 4 or s.game.selection_feature.position == 5 or s.game.selection_feature.position == 6:
        i = [672,474]
        dirty_rects.append(screen.blit(bg_gi, i, pygame.Rect(i[0],i[1],39,29)))
        dirty_rects.append(screen.blit(ti, i))
    if s.game.selection_feature.position == 7:
        i = [672,417]
        dirty_rects.append(screen.blit(bg_gi, i, pygame.Rect(i[0],i[1],39,29)))
        dirty_rects.append(screen.blit(ti, i))
    if s.game.selection_feature.position == 8:
        i = [672,364]
        dirty_rects.append(screen.blit(bg_gi, i, pygame.Rect(i[0],i[1],39,29)))
        dirty_rects.append(screen.blit(ti, i))

    if s.game.red_star.status == True:
        rs_position = [550,464]
        dirty_rects.append(screen.blit(bg_gi, rs_position, pygame.Rect(rs_position[0],rs_position[1],118,55)))
        dirty_rects.append(screen.blit(time, rs_position))
    if s.game.yellow_star.status == True:
        rs_position = [550,520]
        dirty_rects.append(screen.blit(bg_gi, rs_position, pygame.Rect(rs_position[0],rs_position[1],118,55)))
        dirty_rects.append(screen.blit(time, rs_position))

    if s.game.red_super_section.status == True:
        rss = [49,415]
        dirty_rects.append(screen.blit(bg_gi, rss, pygame.Rect(rss[0],rss[1],123,78)))
        dirty_rects.append(screen.blit(super_section, rss))
    if s.game.yellow_super_section.status == True:
        yss = [47,495]
        dirty_rects.append(screen.blit(bg_gi, yss, pygame.Rect(yss[0],yss[1],123,78)))
        dirty_rects.append(screen.blit(super_section, yss))
    if s.game.orange_section.status == True:
        oss = [47,573]
        dirty_rects.append(screen.blit(bg_gi, oss, pygame.Rect(oss[0],oss[1],125,60)))
        dirty_rects.append(screen.blit(orange_section, oss))

    pygame.display.update(dirty_rects)


def eb_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]

    if s.game.extra_ball.position < 1:
        dirty_rects.append(screen.blit(bg_gi, (149,1037), pygame.Rect(149,1037,49,33)))
    if s.game.extra_ball.position < 2:
        dirty_rects.append(screen.blit(bg_gi, (189,1037), pygame.Rect(189,1037,64,36)))
    if s.game.extra_ball.position < 3:
        dirty_rects.append(screen.blit(bg_gi, (254,1037), pygame.Rect(254,1037,64,36)))
    if s.game.extra_ball.position < 4:
        dirty_rects.append(screen.blit(bg_gi, (323,1037), pygame.Rect(323,1037,49,33)))
    if s.game.extra_ball.position < 5:
        dirty_rects.append(screen.blit(bg_gi, (371,1037), pygame.Rect(371,1037,64,36)))
    if s.game.extra_ball.position < 6:
        dirty_rects.append(screen.blit(bg_gi, (435,1037), pygame.Rect(435,1037,64,36)))
    if s.game.extra_ball.position < 7:
        dirty_rects.append(screen.blit(bg_gi, (502,1037), pygame.Rect(502,1037,49,33)))
    if s.game.extra_ball.position < 8:
        dirty_rects.append(screen.blit(bg_gi, (552,1037), pygame.Rect(552,1037,64,36)))
    if s.game.extra_ball.position < 9:
        dirty_rects.append(screen.blit(bg_gi, (613,1037), pygame.Rect(613,1037,64,36)))
    pygame.display.update(dirty_rects)

    if num in [0,25,14,49]:
        if s.game.extra_ball.position < 1:
            p = [149,1037]
            dirty_rects.append(screen.blit(eb_number, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [39,1,26,15]:
        if s.game.extra_ball.position < 2:
            p = [189,1037]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [3,4,17,28,29,40]:
        if s.game.extra_ball.position < 3:
            p = [254,1037]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [5,18,30,43]:
        if s.game.extra_ball.position < 4:
            p = [323,1037]
            dirty_rects.append(screen.blit(eb_number, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [7,8,19,32,33,44]:
        if s.game.extra_ball.position < 5:
            p = [371,1037]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [9,10,20,34,35,45]:
        if s.game.extra_ball.position < 6:
            p = [435,1037]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [11,21,36,46]:
        if s.game.extra_ball.position < 7:
            p = [502,1037]
            dirty_rects.append(screen.blit(eb_number, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [12,22,37,47]:
        if s.game.extra_ball.position < 8:
            p = [552,1037]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [2,6,13,16,23,27,31,38,41,48]:
        if s.game.extra_ball.position < 9:
            p = [613,1037]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return

def clear_odds(s, num):
    global screen

    dirty_rects = []

    if s.game.yellow_odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (182,850), pygame.Rect(182,850,49,73)))
    if s.game.yellow_odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (242,850), pygame.Rect(242,850,49,73)))
    if s.game.yellow_odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (304,850), pygame.Rect(304,850,49,73)))
    if s.game.yellow_odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (365,850), pygame.Rect(365,850,49,73)))
    if s.game.yellow_odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (418,850), pygame.Rect(418,850,49,73)))
    if s.game.yellow_odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (467,850), pygame.Rect(467,850,49,73)))
    if s.game.yellow_odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (512,850), pygame.Rect(512,850,49,73)))
    if s.game.yellow_odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (563,850), pygame.Rect(563,850,49,73)))

    if s.game.red_odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (182,782), pygame.Rect(182,782,49,73)))
    if s.game.red_odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (242,782), pygame.Rect(242,782,49,73)))
    if s.game.red_odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (304,782), pygame.Rect(304,782,49,73)))
    if s.game.red_odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (365,782), pygame.Rect(365,782,49,73)))
    if s.game.red_odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (418,782), pygame.Rect(418,782,49,73)))
    if s.game.red_odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (467,782), pygame.Rect(467,782,49,73)))
    if s.game.red_odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (512,782), pygame.Rect(512,782,49,73)))
    if s.game.red_odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (563,782), pygame.Rect(563,782,49,73)))

    if s.game.green_odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (182,920), pygame.Rect(182,920,49,73)))
    if s.game.green_odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (242,920), pygame.Rect(242,920,49,73)))
    if s.game.green_odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (304,920), pygame.Rect(304,920,49,73)))
    if s.game.green_odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (365,920), pygame.Rect(365,920,49,73)))
    if s.game.green_odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (418,920), pygame.Rect(418,920,49,73)))
    if s.game.green_odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (467,920), pygame.Rect(467,920,49,73)))
    if s.game.green_odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (512,920), pygame.Rect(512,920,49,73)))
    if s.game.green_odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (563,920), pygame.Rect(563,920,49,73)))

    pygame.display.update(dirty_rects)

def draw_odds_animation(s, num):
    global screen
    dirty_rects = []

    if num in [11,36]:
        if s.game.yellow_odds.position != 1:
            p = [182,850]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [4,29]:
        if s.game.yellow_odds.position != 2:
            p = [242,850]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [7,32]:
        if s.game.yellow_odds.position != 3:
            p = [304,850]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [13,38]:
        if s.game.yellow_odds.position != 4:
            p = [365,850]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [22,47]:
        if s.game.yellow_odds.position != 5:
            p = [418,850]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [17,42]:
        if s.game.yellow_odds.position != 6:
            p = [467,850]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [19,44]:
        if s.game.yellow_odds.position != 7:
            p = [512,850]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [5,30]:
        if s.game.yellow_odds.position != 8:
            p = [563,850]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return

    if num in [0,25]:
        if s.game.red_odds.position != 1:
            p = [182,782]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [15,40]:
        if s.game.red_odds.position != 2:
            p = [242,782]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [24,49]:
        if s.game.red_odds.position != 3:
            p = [304,782]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [9,34]:
        if s.game.red_odds.position != 4:
            p = [365,782]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [20,45]:
        if s.game.red_odds.position != 5:
            p = [418,782]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [12,37]:
        if s.game.red_odds.position != 6:
            p = [467,782]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [50,26]:
        if s.game.red_odds.position != 7:
            p = [512,782]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [6,31]:
        if s.game.red_odds.position != 8:
            p = [563,782]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return

    if num in [16,41]:
        if s.game.green_odds.position != 1:
            p = [182,920]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [18,43]:
        if s.game.green_odds.position != 2:
            p = [242,920]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [14,39]:
        if s.game.green_odds.position != 3:
            p = [304,920]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [3,28]:
        if s.game.green_odds.position != 4:
            p = [365,920]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [23,48]:
        if s.game.green_odds.position != 5:
            p = [418,920]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [8,33]:
        if s.game.green_odds.position != 6:
            p = [467,920]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [22,47]:
        if s.game.green_odds.position != 7:
            p = [512,920]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [10,35]:
        if s.game.green_odds.position != 8:
            p = [563,920]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return

def odds_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]

    clear_odds(s, num)

    draw_odds_animation(s, num)

def clear_ss(s, num):
    global screen

    dirty_rects = []
    if s.game.yellow_super_section.status == False:
        dirty_rects.append(screen.blit(bg_gi, (47,495), pygame.Rect(47,495,123,78)))
    if s.game.red_super_section.status == False:
        dirty_rects.append(screen.blit(bg_gi, (49,415), pygame.Rect(49,415,123,78)))
    pygame.display.update(dirty_rects)

def draw_ss_animation(s, num):
    global screen
    dirty_rects = []
 
    if num in [7,32]:
        if s.game.yellow_super_section.status == False:
            p = [47,495]
            dirty_rects.append(screen.blit(super_section, p))
            pygame.display.update(dirty_rects)
            return
    if num in [18,0,43,25]:
        if s.game.red_super_section.status == False:
            p = [49,415]
            dirty_rects.append(screen.blit(super_section, p))
            pygame.display.update(dirty_rects)
            return

def ss_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]

    clear_ss(s, num)

    draw_ss_animation(s, num)


def clear_features(s, num):
    global screen

    dirty_rects = []


    if s.game.selection_feature.position < 4 and (s.game.magic_screen_feature.position < 4 and s.game.ok.status == False):
        dirty_rects.append(screen.blit(bg_gi, (550,578), pygame.Rect(550,578,120,58)))
    if s.game.red_star.status == False:
        dirty_rects.append(screen.blit(bg_gi, (550,464), pygame.Rect(550,464,120,58)))
    if s.game.yellow_star.status == False:
        dirty_rects.append(screen.blit(bg_gi, (550,520), pygame.Rect(550,520,120,58)))
    if s.game.selection_feature.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (550,408), pygame.Rect(550,408,120,58)))
    if s.game.selection_feature.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (550,349), pygame.Rect(550,349,120,58)))

    if s.game.yellow_super_section.status == False:
        dirty_rects.append(screen.blit(bg_gi, (47,495), pygame.Rect(47,495,123,78)))
    if s.game.red_super_section.status == False:
        dirty_rects.append(screen.blit(bg_gi, (49,415), pygame.Rect(49,415,123,78)))
    if s.game.orange_section.status == False:
        dirty_rects.append(screen.blit(bg_gi, (47,573), pygame.Rect(47,573,125,60)))
    if s.game.ok.status == False:
        dirty_rects.append(screen.blit(bg_gi, (68,673), pygame.Rect(68,673,45,56)))
        dirty_rects.append(screen.blit(bg_gi, (26,673), pygame.Rect(26,673,45,56)))
    if s.game.magic_screen_feature.position < 7:
        dirty_rects.append(screen.blit(bg_gi, (153,673), pygame.Rect(153,673,45,56)))
        dirty_rects.append(screen.blit(bg_gi, (195,673), pygame.Rect(195,673,45,56)))
        dirty_rects.append(screen.blit(bg_gi, (237,673), pygame.Rect(237,673,45,56)))
        dirty_rects.append(screen.blit(bg_gi, (281,673), pygame.Rect(281,673,45,56)))
    if s.game.magic_screen_feature.position < 8:
        dirty_rects.append(screen.blit(bg_gi, (321,673), pygame.Rect(321,673,45,56)))
    if s.game.magic_screen_feature.position < 9:
        dirty_rects.append(screen.blit(bg_gi, (361,673), pygame.Rect(361,673,45,56)))
    if s.game.magic_screen_feature.position < 10:
        dirty_rects.append(screen.blit(bg_gi, (402,673), pygame.Rect(402,673,45,56)))
    if s.game.three_blue.status == False:
       dirty_rects.append(screen.blit(bg_gi, (45,339), pygame.Rect(45,339,46,77)))
    if s.game.three_blue_six.status == False:
       dirty_rects.append(screen.blit(bg_gi, (88,339), pygame.Rect(88,339,46,77)))
    if s.game.two_blue.status == False:
        dirty_rects.append(screen.blit(bg_gi, (133,339), pygame.Rect(133,339,46,77)))

    pygame.display.update(dirty_rects)


def draw_feature_animation(s, num):
    global screen
    dirty_rects = []
 
    if num in [10,35]:
        if (s.game.magic_screen_feature.position < 4 and s.game.ok.status == False) and s.game.selection_feature.position not in [7,8]:
            p = [550,578]
            dirty_rects.append(screen.blit(time, p))
            pygame.display.update(dirty_rects)
            return
    if num in [9,34]:
        if s.game.selection_feature.position != 7:
            p = [550,408]
            dirty_rects.append(screen.blit(time, p))
            pygame.display.update(dirty_rects)
            return
    if num in [6,17,21,31,42,46]:
        if s.game.selection_feature.position != 8:
            p = [550,349]
            dirty_rects.append(screen.blit(time, p))
            pygame.display.update(dirty_rects)
            return
    if num in [4,29]:
        if s.game.red_star.status == False:
            p = [550,464]
            dirty_rects.append(screen.blit(time, p))
            s.game.coils.redROLamp.pulse(85)
            pygame.display.update(dirty_rects)
            return
    if num in [11,36]:
        if s.game.yellow_star.status == False:
            p = [550,520]
            dirty_rects.append(screen.blit(time, p))
            s.game.coils.yellowROLamp.pulse(85)
            pygame.display.update(dirty_rects)
            return
    if num in [7,32]:
        if s.game.yellow_super_section.status == False:
            if s.game.red_super_section.status == False:
                p = [47,495]
                dirty_rects.append(screen.blit(super_section, p))
                pygame.display.update(dirty_rects)
                return
    if num in [18,0,43,25]:
        if s.game.red_super_section.status == False:
            if s.game.yellow_super_section.status == False:
                p = [49,415]
                dirty_rects.append(screen.blit(super_section, p))
                pygame.display.update(dirty_rects)
                return
    if num in [13,19,38,44]:
        if s.game.orange_section.status == False:
            p = [47,573]
            dirty_rects.append(screen.blit(orange_section, p))
            pygame.display.update(dirty_rects)
            return
    if num in [16,41]:
        if s.game.ok.status == False:
            p = [68,673]
            dirty_rects.append(screen.blit(ms_letter, p))
            p = [26,673]
            dirty_rects.append(screen.blit(ms_letter, p))
            pygame.display.update(dirty_rects)
            return
    if num in [2,12,27,37]:
        if s.game.magic_screen_feature.position < 7:
            p = [153,673]
            dirty_rects.append(screen.blit(ms_letter, p))
            p = [195,673]
            dirty_rects.append(screen.blit(ms_letter, p))
            p = [237,673]
            dirty_rects.append(screen.blit(ms_letter, p))
            p = [281,673]
            dirty_rects.append(screen.blit(ms_letter, p))
            pygame.display.update(dirty_rects)
            return
    if num in [3,22,28,47]:
        if s.game.magic_screen_feature.position < 8:
            p = [321,673]
            dirty_rects.append(screen.blit(ms_letter, p))
            pygame.display.update(dirty_rects)
            return
    if num in [1,14,26,39]:
        if s.game.magic_screen_feature.position < 9:
            p = [361,673]
            dirty_rects.append(screen.blit(ms_letter, p))
            pygame.display.update(dirty_rects)
            return
    if num in [5,15,30,40]:
        if s.game.magic_screen_feature.position < 10:
            p = [402,673]
            dirty_rects.append(screen.blit(ms_letter, p))
            pygame.display.update(dirty_rects)
            return
    if num in [8,33]:
        if s.game.three_blue.status == False:
            p = [45,339]
            dirty_rects.append(screen.blit(blue_section, p))
            pygame.display.update(dirty_rects)
            return
        else:
            p = [88,339]
            dirty_rects.append(screen.blit(blue_section, p))
            pygame.display.update(dirty_rects)
            return
    if num in [20,45]:
        if s.game.two_blue.status == False:
            p = [133,339]
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
