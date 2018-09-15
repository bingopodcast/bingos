
import pygame
import random

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

meter = pygame.image.load('graphics/assets/register_cover.png').convert()
magic_screen = pygame.image.load('carnival_queen/assets/magic_screen.png').convert()
number_card = pygame.image.load('carnival_queen/assets/number_card.png').convert()
odds = pygame.image.load('carnival_queen/assets/odds.png').convert_alpha()
eb = pygame.image.load('carnival_queen/assets/eb.png').convert_alpha()
eb_number = pygame.image.load('carnival_queen/assets/eb_number.png').convert_alpha()
extra_balls = pygame.image.load('carnival_queen/assets/extra_balls.png').convert_alpha()
feature = pygame.image.load('carnival_queen/assets/feature.png').convert_alpha()
indicator = pygame.image.load('carnival_queen/assets/indicator.png').convert_alpha()
ms_indicator = pygame.image.load('carnival_queen/assets/ms_indicator.png').convert_alpha()
ms_indicator_arrow = pygame.image.load('carnival_queen/assets/ms_indicator_arrow.png').convert_alpha()
ms_letter = pygame.image.load('carnival_queen/assets/ms_letter.png').convert_alpha()
number = pygame.image.load('carnival_queen/assets/number.png').convert_alpha()
select_now = pygame.image.load('carnival_queen/assets/select_now.png').convert_alpha()
three_blue = pygame.image.load('carnival_queen/assets/three_blue.png').convert_alpha()
two_blue = pygame.image.load('carnival_queen/assets/two_blue.png').convert_alpha()
tilt = pygame.image.load('carnival_queen/assets/tilt.png').convert_alpha()
bg_menu = pygame.image.load('carnival_queen/assets/carnival_queen_menu.png').convert()
bg_menu.set_colorkey((255,0,252))
bg_gi = pygame.image.load('carnival_queen/assets/carnival_queen_gi.png').convert_alpha()
bg_off = pygame.image.load('carnival_queen/assets/carnival_queen_off.png').convert()
bg_off.set_colorkey((255,0,252))


class scorereel():
    """ Score Reels are used to count replays """
    def __init__(self, pos, image):
        self.position = pos
        self.default_y = self.position[1]
        self.image = pygame.image.load(image).convert()

reel1 = scorereel([92,795], "graphics/assets/white_reel.png")
reel10 = scorereel([74,795], "graphics/assets/white_reel.png")
reel100 = scorereel([54,795], "graphics/assets/white_reel.png")

def display(s, replays=0, menu=False):
    
    meter.set_colorkey((255,0,252))
    meter_position = [45,795]

    screen.blit(reel1.image, reel1.position)
    screen.blit(reel10.image, reel10.position)
    screen.blit(reel100.image, reel100.position)
    screen.blit(meter, meter_position)

    number_card_position = [232,347]

    screen.blit(number_card, number_card_position)

    magic_screen.set_colorkey((255,0,252))
    #default position 230x 350y
    #subtract 53 per position
    #-135x last position on this game
    if s.game.magic_screen.position == 0:
        magic_screen_position = [230,350]
    elif s.game.magic_screen.position == 1:
        magic_screen_position = [177,350]
    elif s.game.magic_screen.position == 2:
        magic_screen_position = [124,350]
    elif s.game.magic_screen.position == 3:
        magic_screen_position = [71,350]
    elif s.game.magic_screen.position == 4:
        magic_screen_position = [21,350]
    elif s.game.magic_screen.position == 5:
        magic_screen_position = [-32,350]
    elif s.game.magic_screen.position == 6:
        magic_screen_position = [-85,350]
    elif s.game.magic_screen.position == 7:
        magic_screen_position = [-135,350]


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
        eb_position = [40,1019]
        screen.blit(extra_balls, eb_position)

    if s.game.extra_ball.position >= 1:
        eb_position = [150,1022]
        screen.blit(eb_number, eb_position)
    if s.game.extra_ball.position >= 2:
        eb_position = [196,1022]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 3:
        eb_position = [259,1022]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 4:
        eb_position = [331,1024]
        screen.blit(eb_number, eb_position)
    if s.game.extra_ball.position >= 5:
        eb_position = [377,1025]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 6:
        eb_position = [441,1025]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 7:
        eb_position = [511,1021]
        screen.blit(eb_number, eb_position)
    if s.game.extra_ball.position >= 8:
        eb_position = [559,1021]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 9:
        eb_position = [621,1021]
        screen.blit(eb, eb_position)
    

    if s.game.red_star.status == True or s.game.yellow_star.status == True:
        if s.game.before_fourth.status == True:
            rs_position = [561,449]
            screen.blit(feature, rs_position)
            ip = [685,474]
            screen.blit(indicator, ip) 

    if s.game.magic_screen_feature.position >= 7:
        if s.game.before_fourth.status == True:
            bfp = [562,538]
            screen.blit(feature, bfp)
            if s.game.ball_count.position == 3:
                s.cancel_delayed(name="blink")
                blink([s,1,1])
            else:
                s.cancel_delayed(name="blink")
        elif s.game.before_fifth.status == True:
            bfp = [560,356]
            screen.blit(feature, bfp)
            ip = [683,380]
            screen.blit(indicator, ip)
            if s.game.ball_count.position == 4:
                s.cancel_delayed(name="blink")
                blink([s,1,1])
            else:
                s.cancel_delayed(name="blink")

    if s.game.magic_screen_feature.position >= 8:
        if s.game.three_blue.status == True:
            bp = [43,352]
            screen.blit(three_blue, bp)
        elif s.game.two_blue.status == True:
            bp = [0,355]
            screen.blit(two_blue, bp)

    if s.game.red_super_section.status == True:
        rss = [43,444]
        screen.blit(feature, rss)
    if s.game.yellow_super_section.status == True:
        yss = [43,536]
        screen.blit(feature, yss)

    if s.game.magic_screen_feature.position == 1:
        ms = [23,681]
        screen.blit(ms_indicator_arrow, ms)
    if s.game.magic_screen_feature.position == 2:
        ms = [65,681]
        screen.blit(ms_indicator_arrow, ms)
    if s.game.magic_screen_feature.position == 3:
        ms = [108,681]
        screen.blit(ms_indicator_arrow, ms)
    if s.game.magic_screen_feature.position >= 4:
        ms = [157,670]
        screen.blit(ms_letter, ms)
    if s.game.magic_screen_feature.position >= 5:
        ms = [197,670]
        screen.blit(ms_letter, ms)
    if s.game.magic_screen_feature.position >= 6:
        ms = [238,670]
        screen.blit(ms_letter, ms)
    if s.game.magic_screen_feature.position >= 7:
        ms = [281,670]
        screen.blit(ms_letter, ms)
    if s.game.magic_screen_feature.position >= 8:
        ms = [322,670]
        screen.blit(ms_letter, ms)
    if s.game.magic_screen_feature.position >= 9:
        ms = [364,670]
        screen.blit(ms_letter, ms)
    if s.game.magic_screen_feature.position >= 10:
        ms = [406,670]
        screen.blit(ms_letter, ms)

    if s.game.magic_screen.position == 1:
        ms = [163,724]
        screen.blit(ms_indicator, ms)
    if s.game.magic_screen.position == 2:
        ms = [205,724]
        screen.blit(ms_indicator, ms)
    if s.game.magic_screen.position == 3:
        ms = [243,724]
        screen.blit(ms_indicator, ms)
    if s.game.magic_screen.position == 4:
        ms = [285,724]
        screen.blit(ms_indicator, ms)
    if s.game.magic_screen.position == 5:
        ms = [328,724]
        screen.blit(ms_indicator, ms)
    if s.game.magic_screen.position == 6:
        ms = [370,724]
        screen.blit(ms_indicator, ms)
    if s.game.magic_screen.position == 7:
        ms = [411,724]
        screen.blit(ms_indicator, ms)

    if s.game.tilt.status == False:
        if s.holes:
            if 1 in s.holes:
                number_position = [284,365]
                screen.blit(number, number_position)
            if 2 in s.holes:
                number_position = [336,364]
                screen.blit(number, number_position)
            if 3 in s.holes:
                number_position = [390,559]
                screen.blit(number, number_position)
            if 4 in s.holes:
                number_position = [231,414]
                screen.blit(number, number_position)
            if 5 in s.holes:
                number_position = [337,511]
                screen.blit(number, number_position)
            if 6 in s.holes:
                number_position = [230,512]
                screen.blit(number, number_position)
            if 7 in s.holes:
                number_position = [337,414]
                screen.blit(number, number_position)
            if 8 in s.holes:
                number_position = [284,561]
                screen.blit(number, number_position)
            if 9 in s.holes:
                number_position = [230,364]
                screen.blit(number, number_position)
            if 10 in s.holes:
                number_position = [440,559]
                screen.blit(number, number_position)
            if 11 in s.holes:
                number_position = [390,364]
                screen.blit(number, number_position)
            if 12 in s.holes:
                number_position = [231,562]
                screen.blit(number, number_position)
            if 13 in s.holes:
                number_position = [389,461]
                screen.blit(number, number_position)
            if 14 in s.holes:
                number_position = [336,561]
                screen.blit(number, number_position)
            if 15 in s.holes:
                number_position = [441,363]
                screen.blit(number, number_position)
            if 16 in s.holes:
                number_position = [336,461]
                screen.blit(number, number_position)
            if 17 in s.holes:
                number_position = [440,462]
                screen.blit(number, number_position)
            if 18 in s.holes:
                number_position = [441,413]
                screen.blit(number, number_position)
            if 19 in s.holes:
                number_position = [282,413]
                screen.blit(number, number_position)
            if 20 in s.holes:
                number_position = [441,510]
                screen.blit(number, number_position)
            if 21 in s.holes:
                number_position = [389,510]
                screen.blit(number, number_position)
            if 22 in s.holes:
                number_position = [390,413]
                screen.blit(number, number_position)
            if 23 in s.holes:
                number_position = [284,511]
                screen.blit(number, number_position)
            if 24 in s.holes:
                number_position = [284,462]
                screen.blit(number, number_position)
            if 25 in s.holes:
                number_position = [230,462]
                screen.blit(number, number_position)

    if s.game.red_odds.position == 1:
        o = [181,779]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 2:
        o = [247,779]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 3:
        o = [309,779]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 4:
        o = [373,779]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 5:
        o = [428,779]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 6:
        o = [479,779]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 7:
        o = [533,779]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 8:
        o = [579,779]
        screen.blit(odds, o)

    if s.game.yellow_odds.position == 1:
        o = [181,840]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 2:
        o = [247,840]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 3:
        o = [309,840]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 4:
        o = [373,840]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 5:
        o = [428,840]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 6:
        o = [479,840]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 7:
        o = [533,840]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 8:
        o = [579,840]
        screen.blit(odds, o)

    if s.game.green_odds.position == 1:
        o = [181,905]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 2:
        o = [247,905]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 3:
        o = [309,905]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 4:
        o = [373,905]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 5:
        o = [428,905]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 6:
        o = [479,905]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 7:
        o = [533,905]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 8:
        o = [579,905]
        screen.blit(odds, o)


    if s.game.tilt.status == True:
        tilt_position = [47,632]
        screen.blit(tilt, tilt_position)

    pygame.display.update()

def blink(args):
    dirty_rects = []
    s = args[0]
    b = args[1]
    sn = args[2]

    if b == 0:
        if sn == 1:
            p = [578,676]
            dirty_rects.append(screen.blit(select_now, p))
        pygame.display.update(dirty_rects)
    else:
        dirty_rects.append(screen.blit(bg_gi, (578,676), pygame.Rect(578,676,135,42)))
        pygame.display.update(dirty_rects)
    b = not b

    args = [s,b,sn]

    s.delay(name="blink", delay=0.1, handler=blink, param=args)

def screen_animation(args):
    dirty_rects = []
    s = args[0]
    num = args[1]
    direction = args[2]
    
    number_card_position = [232,347]

    dirty_rects.append(screen.blit(number_card, number_card_position))

    magic_screen.set_colorkey((255,0,252))

    if s.game.magic_screen.position == 0:
        p = [230,350]
    elif s.game.magic_screen.position == 1:
        p = [177,350]
    elif s.game.magic_screen.position == 2:
        p = [124,350]
    elif s.game.magic_screen.position == 3:
        p = [71,350]
    elif s.game.magic_screen.position == 4:
        p = [21,350]
    elif s.game.magic_screen.position == 5:
        p = [-32,350]
    elif s.game.magic_screen.position == 6:
        p = [-85,350]
    elif s.game.magic_screen.position == 7:
        p = [-135,350]

    if direction == "left":
       p[0] = p[0] + num
    else:
       p[0] = p[0] - num
 
    dirty_rects.append(screen.blit(magic_screen, p))
    
    backglass_position = [0, 0]
    if (s.game.anti_cheat.status == True):
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],625,320)))
    else:
        dirty_rects.append(screen.blit(bg_off, p, pygame.Rect(p[0],p[1],625,320)))
    
    if s.game.magic_screen_feature.position >= 9:
        if s.game.three_blue.status == True:
            bp = [43,352]
            dirty_rects.append(screen.blit(bg_gi, bp, pygame.Rect(bp[0],bp[1],59,90)))
            dirty_rects.append(screen.blit(three_blue, bp))
        elif s.game.two_blue.status == True:
            bp = [0,355]
            dirty_rects.append(screen.blit(bg_gi, bp, pygame.Rect(bp[0],bp[1],164,85)))
            dirty_rects.append(screen.blit(two_blue, bp))

    if s.game.magic_screen_feature.position >= 4:
        if s.game.before_fourth.status == True:
            p = [562,538]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],119,85)))
            dirty_rects.append(screen.blit(feature, p))
        if s.game.red_star.status == True or s.game.yellow_star.status == True:
            p = [561,449]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],119,85)))
            dirty_rects.append(screen.blit(feature, p))
            ip = [685,474]
            dirty_rects.append(screen.blit(bg_gi, ip, pygame.Rect(ip[0],ip[1],33,37)))
            dirty_rects.append(screen.blit(indicator, ip))
        if s.game.before_fifth.status == True:
            p = [560,356]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],119,85)))
            dirty_rects.append(screen.blit(feature, p))
            ip = [683,380]
            dirty_rects.append(screen.blit(bg_gi, ip, pygame.Rect(ip[0],ip[1],33,37)))
            dirty_rects.append(screen.blit(indicator, ip))

    if s.game.red_super_section.status == True:
        rss = [43,444]
        dirty_rects.append(screen.blit(bg_gi, (43,444), pygame.Rect(43,444,119,85)))
        dirty_rects.append(screen.blit(feature, rss))
    if s.game.yellow_super_section.status == True:
        yss = [43,536]
        dirty_rects.append(screen.blit(bg_gi, (43,536), pygame.Rect(43,536,119,85)))
        dirty_rects.append(screen.blit(feature, yss))

    pygame.display.update(dirty_rects)


def eb_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]

    if s.game.extra_ball.position < 1:
        dirty_rects.append(screen.blit(bg_gi, (150,1022), pygame.Rect(150,1022,46,32)))
    if s.game.extra_ball.position < 2:
        dirty_rects.append(screen.blit(bg_gi, (196,1022), pygame.Rect(196,1022,64,32)))
    if s.game.extra_ball.position < 3:
        dirty_rects.append(screen.blit(bg_gi, (259,1022), pygame.Rect(259,1022,64,32)))
    if s.game.extra_ball.position < 4:
        dirty_rects.append(screen.blit(bg_gi, (331,1024), pygame.Rect(331,1024,46,32)))
    if s.game.extra_ball.position < 5:
        dirty_rects.append(screen.blit(bg_gi, (377,1025), pygame.Rect(377,1025,64,32)))
    if s.game.extra_ball.position < 6:
        dirty_rects.append(screen.blit(bg_gi, (441,1025), pygame.Rect(441,1025,64,32)))
    if s.game.extra_ball.position < 7:
        dirty_rects.append(screen.blit(bg_gi, (511,1021), pygame.Rect(511,1021,46,32)))
    if s.game.extra_ball.position < 8:
        dirty_rects.append(screen.blit(bg_gi, (559,1021), pygame.Rect(559,1021,64,32)))
    if s.game.extra_ball.position < 9:
        dirty_rects.append(screen.blit(bg_gi, (621,1021), pygame.Rect(621,1021,64,32)))
    pygame.display.update(dirty_rects)

    if num in [0,25,14,49]:
        if s.game.extra_ball.position < 1:
            p = [150,1022]
            dirty_rects.append(screen.blit(eb_number, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [39,1,26,15]:
        if s.game.extra_ball.position < 2:
            p = [196,1022]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [3,4,17,28,29,40]:
        if s.game.extra_ball.position < 3:
            p = [259,1022]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [5,18,30,43]:
        if s.game.extra_ball.position < 4:
            p = [331,1024]
            dirty_rects.append(screen.blit(eb_number, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [7,8,19,32,33,44]:
        if s.game.extra_ball.position < 5:
            p = [377,1025]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [9,10,20,34,35,45]:
        if s.game.extra_ball.position < 6:
            p = [441,1025]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [11,21,36,46]:
        if s.game.extra_ball.position < 7:
            p = [511,1021]
            dirty_rects.append(screen.blit(eb_number, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [12,22,37,47]:
        if s.game.extra_ball.position < 8:
            p = [559,1021]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [2,6,13,16,23,27,31,38,41,48]:
        if s.game.extra_ball.position < 9:
            p = [621,1021]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return

def clear_odds(s, num):
    global screen

    dirty_rects = []

   
    if s.game.yellow_odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (181,840), pygame.Rect(181,840,46,73)))
    if s.game.yellow_odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (247,840), pygame.Rect(247,840,46,73)))
    if s.game.yellow_odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (309,840), pygame.Rect(309,840,46,73)))
    if s.game.yellow_odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (373,840), pygame.Rect(373,840,46,73)))
    if s.game.yellow_odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (428,840), pygame.Rect(428,840,46,73)))
    if s.game.yellow_odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (479,840), pygame.Rect(479,840,46,73)))
    if s.game.yellow_odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (533,840), pygame.Rect(533,840,46,73)))
    if s.game.yellow_odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (579,840), pygame.Rect(579,840,46,73)))

    if s.game.red_odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (181,779), pygame.Rect(181,779,46,73)))
    if s.game.red_odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (247,779), pygame.Rect(247,779,46,73)))
    if s.game.red_odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (309,779), pygame.Rect(309,779,46,73)))
    if s.game.red_odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (373,779), pygame.Rect(373,779,46,73)))
    if s.game.red_odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (428,779), pygame.Rect(428,779,46,73)))
    if s.game.red_odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (479,779), pygame.Rect(479,779,46,73)))
    if s.game.red_odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (533,779), pygame.Rect(533,779,46,73)))
    if s.game.red_odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (579,779), pygame.Rect(579,779,46,73)))

    if s.game.green_odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (181,905), pygame.Rect(181,905,46,73)))
    if s.game.green_odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (247,905), pygame.Rect(247,905,46,73)))
    if s.game.green_odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (309,905), pygame.Rect(309,905,46,73)))
    if s.game.green_odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (373,905), pygame.Rect(373,905,46,73)))
    if s.game.green_odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (428,905), pygame.Rect(428,905,46,73)))
    if s.game.green_odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (479,905), pygame.Rect(479,905,46,73)))
    if s.game.green_odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (533,905), pygame.Rect(533,905,46,73)))
    if s.game.green_odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (579,905), pygame.Rect(579,905,46,73)))

    pygame.display.update(dirty_rects)

def draw_odds_animation(s, num):
    global screen
    dirty_rects = []

    if num in [11,36]:
        if s.game.yellow_odds.position != 1:
            p = [181,840]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [4,29]:
        if s.game.yellow_odds.position != 2:
            p = [247,840]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [7,32]:
        if s.game.yellow_odds.position != 3:
            p = [309,840]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [13,38]:
        if s.game.yellow_odds.position != 4:
            p = [373,840]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [22,47]:
        if s.game.yellow_odds.position != 5:
            p = [428,840]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [17,42]:
        if s.game.yellow_odds.position != 6:
            p = [479,840]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [19,44]:
        if s.game.yellow_odds.position != 7:
            p = [533,840]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [5,30]:
        if s.game.yellow_odds.position != 8:
            p = [579,840]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return

    if num in [0,25]:
        if s.game.red_odds.position != 1:
            p = [181,779]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [15,40]:
        if s.game.red_odds.position != 2:
            p = [247,779]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [24,49]:
        if s.game.red_odds.position != 3:
            p = [309,779]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [9,34]:
        if s.game.red_odds.position != 4:
            p = [373,779]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [20,45]:
        if s.game.red_odds.position != 5:
            p = [428,779]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [12,37]:
        if s.game.red_odds.position != 6:
            p = [479,779]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [50,26]:
        if s.game.red_odds.position != 7:
            p = [533,779]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [6,31]:
        if s.game.red_odds.position != 8:
            p = [579,779]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return

    if num in [16,41]:
        if s.game.green_odds.position != 1:
            p = [181,905]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [18,43]:
        if s.game.green_odds.position != 2:
            p = [247,905]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [14,39]:
        if s.game.green_odds.position != 3:
            p = [309,905]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [3,28]:
        if s.game.green_odds.position != 4:
            p = [373,905]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [23,48]:
        if s.game.green_odds.position != 5:
            p = [428,905]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [8,33]:
        if s.game.green_odds.position != 6:
            p = [479,905]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [22,47]:
        if s.game.green_odds.position != 7:
            p = [533,905]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [10,35]:
        if s.game.green_odds.position != 8:
            p = [577,905]
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

def clear_features(s, num):
    global screen

    dirty_rects = []

    if s.game.yellow_super_section.status == False:
        dirty_rects.append(screen.blit(bg_gi, (43,536), pygame.Rect(43,536,119,85)))
    if s.game.red_super_section.status == False:
        dirty_rects.append(screen.blit(bg_gi, (43,444), pygame.Rect(43,444,119,85)))
    if s.game.red_star.status == False and s.game.yellow_star.status == False:
        dirty_rects.append(screen.blit(bg_gi, (561,449), pygame.Rect(561,449,119,85)))
    if s.game.before_fourth.status == False:
        dirty_rects.append(screen.blit(bg_gi, (562,538), pygame.Rect(562,538,119,85)))
    if s.game.before_fifth.status == False:
        dirty_rects.append(screen.blit(bg_gi, (560,356), pygame.Rect(560,356,119,85)))

    if s.game.magic_screen_feature.position < 7:
        dirty_rects.append(screen.blit(bg_gi, (157,670), pygame.Rect(157,670,42,51)))
        dirty_rects.append(screen.blit(bg_gi, (197,670), pygame.Rect(197,670,42,51)))
        dirty_rects.append(screen.blit(bg_gi, (238,670), pygame.Rect(238,670,42,51)))
        dirty_rects.append(screen.blit(bg_gi, (281,670), pygame.Rect(281,670,42,51)))
    if s.game.magic_screen_feature.position < 8:
        dirty_rects.append(screen.blit(bg_gi, (322,670), pygame.Rect(322,670,42,51)))
    if s.game.magic_screen_feature.position < 9:
        dirty_rects.append(screen.blit(bg_gi, (364,670), pygame.Rect(364,670,42,51)))
    if s.game.magic_screen_feature.position < 10:
        dirty_rects.append(screen.blit(bg_gi, (406,670), pygame.Rect(406,670,42,51)))
    if s.game.two_blue.status == False:
        dirty_rects.append(screen.blit(bg_gi, (103,352), pygame.Rect(103,352,59,90)))
    if s.game.three_blue.status == False:
       dirty_rects.append(screen.blit(bg_gi, (43,352), pygame.Rect(43,352,59,90)))

    pygame.display.update(dirty_rects)


def draw_feature_animation(s, num):
    global screen
    dirty_rects = []
 
    if num in [0,25,46,19]:
        if s.game.yellow_super_section.status == False:
            if s.game.red_super_section.status == False:
                p = [43,536]
                dirty_rects.append(screen.blit(feature, p))
                pygame.display.update(dirty_rects)
                return
    if num in [8,18,24,33,43,49]:
        if s.game.red_super_section.status == False:
            if s.game.yellow_super_section.status == False:
                p = [43,444]
                dirty_rects.append(screen.blit(feature, p))
                pygame.display.update(dirty_rects)
                return
    if num in [11,19,36,44]:
        if s.game.red_star.status == False and s.game.yellow_star.status == False:
            p = [561,449]
            dirty_rects.append(screen.blit(feature, p))
            s.game.coils.yellowROLamp.pulse(85)
            s.game.coils.redROLamp.pulse(85)
            pygame.display.update(dirty_rects)
            return
    if num in [9,34]:
        if s.game.before_fourth.status == False:
            p = [562,538]
            dirty_rects.append(screen.blit(feature, p))
            pygame.display.update(dirty_rects)
            return
    if num in [6,17,21,31,32,46]:
        if s.game.before_fifth.status == False:
            p = [560,356]
            dirty_rects.append(screen.blit(feature, p))
            pygame.display.update(dirty_rects)
            return
    if num in [2,12,27,37]:
        if s.game.magic_screen_feature.position < 7:
            p = [157,670]
            dirty_rects.append(screen.blit(ms_letter, p))
            p = [197,670]
            dirty_rects.append(screen.blit(ms_letter, p))
            p = [238,670]
            dirty_rects.append(screen.blit(ms_letter, p))
            p = [281,670]
            dirty_rects.append(screen.blit(ms_letter, p))
            pygame.display.update(dirty_rects)
            return
    if num in [3,13,28,38]:
        if s.game.magic_screen_feature.position < 8:
            p = [322,670]
            dirty_rects.append(screen.blit(ms_letter, p))
            pygame.display.update(dirty_rects)
            return
    if num in [4,14,25,29,39,50]:
        if s.game.magic_screen_feature.position < 9:
            p = [364,670]
            dirty_rects.append(screen.blit(ms_letter, p))
            pygame.display.update(dirty_rects)
            return
        if s.game.three_blue.status == False:
            p = [43,352]
            dirty_rects.append(screen.blit(three_blue, p))
            pygame.display.update(dirty_rects)
            return
        else:
            if s.game.two_blue.status == False:
                p = [103,352]
                dirty_rects.append(screen.blit(three_blue, p))
                pygame.display.update(dirty_rects)
                return
    if num in [5,15,30,40]:
        if s.game.magic_screen_feature.position < 10:
            p = [406,670]
            dirty_rects.append(screen.blit(ms_letter, p))
            pygame.display.update(dirty_rects)
            return
    if num in [10,16,23,35,41,48]:
        if s.game.two_blue.status == False:
            p = [103,352]
            dirty_rects.append(screen.blit(three_blue, p))
            pygame.display.update(dirty_rects)
            return
        else:
            if s.game.three_blue.status == False:
                p = [43,352]
                dirty_rects.append(screen.blit(three_blue, p))
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
