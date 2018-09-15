
import pygame
import random

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

meter = pygame.image.load('graphics/assets/register_cover.png').convert()
magic_screen = pygame.image.load('ballerina/assets/magic_screen.png').convert()
number_card = pygame.image.load('ballerina/assets/number_card.png').convert()
odds = pygame.image.load('ballerina/assets/odds.png').convert_alpha()
eb = pygame.image.load('ballerina/assets/extra_ball.png').convert_alpha()
eb_number = pygame.image.load('ballerina/assets/eb_number.png').convert_alpha()
extra_balls = pygame.image.load('ballerina/assets/extra_balls.png').convert_alpha()
feature = pygame.image.load('ballerina/assets/selection.png').convert_alpha()
ms_indicator = pygame.image.load('ballerina/assets/ms_arrow.png').convert_alpha()
ms_teaser = pygame.image.load('ballerina/assets/ms_teaser.png').convert_alpha()
ti = pygame.image.load('ballerina/assets/selection_arrow.png').convert_alpha()
super_section = pygame.image.load('ballerina/assets/super_section.png').convert_alpha()
ms_letter = pygame.image.load('ballerina/assets/ms_letter.png').convert_alpha()
number = pygame.image.load('ballerina/assets/number.png').convert_alpha()
select_now = pygame.image.load('ballerina/assets/select_now.png').convert_alpha()
three_blue = pygame.image.load('ballerina/assets/blue_section.png').convert_alpha()
tilt = pygame.image.load('ballerina/assets/tilt.png').convert_alpha()
one_seven_feature = pygame.image.load('ballerina/assets/one_seven_feature.png').convert_alpha()
one_seven = pygame.image.load('ballerina/assets/one_seven.png').convert_alpha()
bg_menu = pygame.image.load('ballerina/assets/ballerina_menu.png').convert_alpha()
bg_gi = pygame.image.load('ballerina/assets/ballerina_gi.png').convert_alpha()
bg_off = pygame.image.load('ballerina/assets/ballerina_off.png').convert_alpha()

class scorereel():
    """ Score Reels are used to count replays """
    def __init__(self, pos, image):
        self.position = pos
        self.default_y = self.position[1]
        self.image = pygame.image.load(image).convert()

reel1 = scorereel([97,785], "graphics/assets/white_reel.png")
reel10 = scorereel([78,785], "graphics/assets/white_reel.png")
reel100 = scorereel([59,785], "graphics/assets/white_reel.png")

def display(s, replays=0, menu=False):
    
    meter.set_colorkey((255,0,252))
    meter_position = [51,785]

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
        magic_screen_position = [-42,358]
    elif s.game.magic_screen.position == 7:
        magic_screen_position = [-89,358]
    elif s.game.magic_screen.position == 8:
        magic_screen_position = [-136,358]
    elif s.game.magic_screen.position == 9:
        magic_screen_position = [-183,358]


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
        eb_position = [41,1014]
        screen.blit(extra_balls, eb_position)

    if s.game.extra_ball.position >= 1:
        eb_position = [151,1014]
        screen.blit(eb_number, eb_position)
    if s.game.extra_ball.position >= 2:
        eb_position = [198,1014]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 3:
        eb_position = [262,1014]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 4:
        eb_position = [330,1014]
        screen.blit(eb_number, eb_position)
    if s.game.extra_ball.position >= 5:
        eb_position = [376,1014]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 6:
        eb_position = [436,1014]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 7:
        eb_position = [506,1014]
        screen.blit(eb_number, eb_position)
    if s.game.extra_ball.position >= 8:
        eb_position = [554,1014]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 9:
        eb_position = [617,1014]
        screen.blit(eb, eb_position)
    

    if s.game.magic_screen_feature.position >= 4:
        if s.game.before_fourth.status == True:
            p = [551,572]
            screen.blit(feature, p)
        if s.game.rollovers.status == True:
            p = [549,519]
            screen.blit(feature, p)
        if s.game.before_fifth.status == True:
            p = [549,465]
            screen.blit(feature, p)
        if s.game.after_fifth.status == True:
            p = [550,409]
            screen.blit(feature, p)

    if s.game.one_seven_feature.status == True:
        p = [527,231]
        screen.blit(one_seven_feature, p)
        if s.game.one_seven.status == True:
            p = [527,295]
            screen.blit(one_seven, p)
        if s.game.seven_one.status == True:
            p = [527,329]
            screen.blit(one_seven, p)

    if s.game.magic_screen_feature.position >= 8:
        if s.game.three_blue.status == True:
            bp = [51,359]
            screen.blit(three_blue, bp)
        elif s.game.two_blue.status == True:
            bp = [112,357]
            screen.blit(three_blue, bp)

    if s.game.yellow_super_section.status == True:
        rss = [50,452]
        screen.blit(super_section, rss)
    if s.game.red_super_section.status == True:
        yss = [50,539]
        screen.blit(super_section, yss)

    if s.game.magic_screen_feature.position >= 1:
        ms = [31,669]
        screen.blit(ms_letter, ms)
    if s.game.magic_screen_feature.position >= 2:
        ms = [68,669]
        screen.blit(ms_letter, ms)
    if s.game.magic_screen_feature.position >= 3:
        ms = [105,669]
        screen.blit(ms_letter, ms)
    if s.game.magic_screen_feature.position >= 4:
        ms = [142,669]
        screen.blit(ms_letter, ms)
    if s.game.magic_screen_feature.position == 5:
        ms = [183,680]
        screen.blit(ms_teaser, ms)
    if s.game.magic_screen_feature.position >= 6:
        ms = [211,669]
        screen.blit(ms_letter, ms)
    if s.game.magic_screen_feature.position == 7:
        ms = [249,681]
        screen.blit(ms_teaser, ms)
    if s.game.magic_screen_feature.position >= 8:
        ms = [277,669]
        screen.blit(ms_letter, ms)
    if s.game.magic_screen_feature.position == 9:
        ms = [315,681]
        screen.blit(ms_teaser, ms)
    if s.game.magic_screen_feature.position >= 10:
        ms = [343,669]
        screen.blit(ms_letter, ms)
    if s.game.magic_screen_feature.position == 11:
        ms = [381,680]
        screen.blit(ms_teaser, ms)
    if s.game.magic_screen_feature.position >= 12:
        ms = [408,669]
        screen.blit(ms_letter, ms)

    if s.game.magic_screen.position == 1:
        ms = [30,724]
        screen.blit(ms_indicator, ms)
    if s.game.magic_screen.position == 2:
        ms = [67,724]
        screen.blit(ms_indicator, ms)
    if s.game.magic_screen.position == 3:
        ms = [103,724]
        screen.blit(ms_indicator, ms)
    if s.game.magic_screen.position == 4:
        ms = [141,724]
        screen.blit(ms_indicator, ms)
    if s.game.magic_screen.position == 5:
        ms = [211,724]
        screen.blit(ms_indicator, ms)
    if s.game.magic_screen.position == 6:
        ms = [275,724]
        screen.blit(ms_indicator, ms)
    if s.game.magic_screen.position == 7:
        ms = [342,724]
        screen.blit(ms_indicator, ms)
    if s.game.magic_screen.position == 8:
        ms = [409,724]
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
        o = [190,765]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 2:
        o = [250,765]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 3:
        o = [312,765]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 4:
        o = [373,765]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 5:
        o = [425,765]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 6:
        o = [474,765]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 7:
        o = [522,765]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 8:
        o = [568,765]
        screen.blit(odds, o)

    if s.game.yellow_odds.position == 1:
        o = [190,831]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 2:
        o = [250,831]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 3:
        o = [312,831]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 4:
        o = [373,831]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 5:
        o = [425,831]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 6:
        o = [474,831]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 7:
        o = [522,831]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 8:
        o = [568,831]
        screen.blit(odds, o)

    if s.game.green_odds.position == 1:
        o = [190,903]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 2:
        o = [250,903]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 3:
        o = [312,903]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 4:
        o = [373,903]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 5:
        o = [425,903]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 6:
        o = [474,903]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 7:
        o = [522,903]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 8:
        o = [572,903]
        screen.blit(odds, o)

    if s.game.magic_screen_feature.position >= 1:
        if s.game.before_fourth.status == True and s.game.ball_count.position == 3:
            s.cancel_delayed(name="blink")
            blink([s,1,1])
        elif s.game.before_fifth.status == True and s.game.ball_count.position == 4:
            s.cancel_delayed(name="blink")
            blink([s,1,1])
        elif s.game.after_fifth.status == True and s.game.ball_count.position == 5:
            s.cancel_delayed(name="blink")
            blink([s,1,1])
        else:
            s.cancel_delayed(name="blink")


    if s.game.tilt.status == True:
        tilt_position = [572,632]
        screen.blit(tilt, tilt_position)

    pygame.display.update()

def blink(args):
    dirty_rects = []
    s = args[0]
    b = args[1]
    sn = args[2]

    if b == 0:
        if sn == 1:
            p = [575,677]
            dirty_rects.append(screen.blit(select_now, p))
        pygame.display.update(dirty_rects)
    else:
        dirty_rects.append(screen.blit(bg_gi, (575,677), pygame.Rect(575,677,123,32)))
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
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],612,280)))
    else:
        dirty_rects.append(screen.blit(bg_off, p, pygame.Rect(p[0],p[1],612,280)))
    
    if s.game.magic_screen_feature.position >= 9:
        if s.game.three_blue.status == True:
            bp = [51,359]
            dirty_rects.append(screen.blit(bg_gi, bp, pygame.Rect(bp[0],bp[1],46,77)))
            dirty_rects.append(screen.blit(three_blue, bp))
        elif s.game.two_blue.status == True:
            bp = [112,357]
            dirty_rects.append(screen.blit(bg_gi, bp, pygame.Rect(bp[0],bp[1],46,77)))
            dirty_rects.append(screen.blit(three_blue, bp))

    if s.game.magic_screen_feature.position >= 4:
        if s.game.before_fourth.status == True:
            p = [551,572]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],124,54)))
            dirty_rects.append(screen.blit(feature, p))
        if s.game.rollovers.status == True:
            p = [549,519]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],124,54)))
            dirty_rects.append(screen.blit(feature, p))
        if s.game.before_fifth.status == True:
            p = [549,465]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],124,54)))
            dirty_rects.append(screen.blit(feature, p))
        if s.game.after_fifth.status == True:
            p = [550,409]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],124,54)))
            dirty_rects.append(screen.blit(feature, p))

    if s.game.red_super_section.status == True:
        yss = [50,539]
        dirty_rects.append(screen.blit(bg_gi, (50,539), pygame.Rect(50,539,121,81)))
        dirty_rects.append(screen.blit(super_section, rss))
    if s.game.yellow_super_section.status == True:
        rss = [50,452]
        dirty_rects.append(screen.blit(bg_gi, (50,452), pygame.Rect(50,452,121,81)))
        dirty_rects.append(screen.blit(super_section, yss))

    pygame.display.update(dirty_rects)


def eb_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]
    if s.game.extra_ball.position < 1:
        dirty_rects.append(screen.blit(bg_gi, (151,1014), pygame.Rect(151,1014,47,33)))
    if s.game.extra_ball.position < 2:
        dirty_rects.append(screen.blit(bg_gi, (198,1014), pygame.Rect(198,1014,63,36)))
    if s.game.extra_ball.position < 3:
        dirty_rects.append(screen.blit(bg_gi, (262,1014), pygame.Rect(262,1014,63,36)))
    if s.game.extra_ball.position < 4:
        dirty_rects.append(screen.blit(bg_gi, (330,1014), pygame.Rect(330,1014,47,33)))
    if s.game.extra_ball.position < 5:
        dirty_rects.append(screen.blit(bg_gi, (376,1014), pygame.Rect(376,1014,63,36)))
    if s.game.extra_ball.position < 6:
        dirty_rects.append(screen.blit(bg_gi, (436,1014), pygame.Rect(436,1014,63,36)))
    if s.game.extra_ball.position < 7:
        dirty_rects.append(screen.blit(bg_gi, (506,1014), pygame.Rect(506,1014,47,33)))
    if s.game.extra_ball.position < 8:
        dirty_rects.append(screen.blit(bg_gi, (554,1014), pygame.Rect(554,1014,63,36)))
    if s.game.extra_ball.position < 9:
        dirty_rects.append(screen.blit(bg_gi, (617,1014), pygame.Rect(617,1014,63,36)))
    pygame.display.update(dirty_rects)

    if num in [0,25,14,49]:
        if s.game.extra_ball.position < 1:
            p = [151,1014]
            dirty_rects.append(screen.blit(eb_number, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [39,1,26,15]:
        if s.game.extra_ball.position < 2:
            p = [198,1014]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [3,4,17,28,29,40]:
        if s.game.extra_ball.position < 3:
            p = [262,1014]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [5,18,30,43]:
        if s.game.extra_ball.position < 4:
            p = [330,1014]
            dirty_rects.append(screen.blit(eb_number, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [7,8,19,32,33,44]:
        if s.game.extra_ball.position < 5:
            p = [376,1014]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [9,10,20,34,35,45]:
        if s.game.extra_ball.position < 6:
            p = [436,1014]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [11,21,36,46]:
        if s.game.extra_ball.position < 7:
            p = [506,1014]
            dirty_rects.append(screen.blit(eb_number, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [12,22,37,47]:
        if s.game.extra_ball.position < 8:
            p = [554,1014]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [2,6,13,16,23,27,31,38,41,48]:
        if s.game.extra_ball.position < 9:
            p = [617,1014]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return

def clear_odds(s, num):
    global screen

    dirty_rects = []

    if s.game.yellow_odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (190,831), pygame.Rect(190,831,46,68)))
    if s.game.yellow_odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (250,831), pygame.Rect(250,831,46,68)))
    if s.game.yellow_odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (312,831), pygame.Rect(312,831,46,68)))
    if s.game.yellow_odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (373,831), pygame.Rect(373,831,46,68)))
    if s.game.yellow_odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (425,831), pygame.Rect(425,831,46,68)))
    if s.game.yellow_odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (474,831), pygame.Rect(474,831,46,68)))
    if s.game.yellow_odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (522,831), pygame.Rect(522,831,46,68)))
    if s.game.yellow_odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (568,831), pygame.Rect(568,831,46,68)))

    if s.game.red_odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (190,765), pygame.Rect(190,765,46,68)))
    if s.game.red_odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (250,765), pygame.Rect(250,765,46,68)))
    if s.game.red_odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (312,765), pygame.Rect(312,765,46,68)))
    if s.game.red_odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (373,765), pygame.Rect(373,765,46,68)))
    if s.game.red_odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (425,765), pygame.Rect(425,765,46,68)))
    if s.game.red_odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (474,765), pygame.Rect(474,765,46,68)))
    if s.game.red_odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (522,765), pygame.Rect(522,765,46,68)))
    if s.game.red_odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (568,765), pygame.Rect(568,765,46,68)))

    if s.game.green_odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (190,903), pygame.Rect(190,903,46,68)))
    if s.game.green_odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (250,903), pygame.Rect(250,903,46,68)))
    if s.game.green_odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (312,903), pygame.Rect(312,903,46,68)))
    if s.game.green_odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (373,903), pygame.Rect(373,903,46,68)))
    if s.game.green_odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (425,903), pygame.Rect(425,903,46,68)))
    if s.game.green_odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (474,903), pygame.Rect(474,903,46,68)))
    if s.game.green_odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (522,903), pygame.Rect(522,903,46,68)))
    if s.game.green_odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (568,903), pygame.Rect(568,903,46,68)))


    pygame.display.update(dirty_rects)

def draw_odds_animation(s, num):
    global screen
    dirty_rects = []

    if num in [5,30]:
        if s.game.yellow_odds.position != 1:
            p = [190,831]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [4,29]:
        if s.game.yellow_odds.position != 2:
            p = [250,831]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [7,32]:
        if s.game.yellow_odds.position != 3:
            p = [312,831]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [13,38]:
        if s.game.yellow_odds.position != 4:
            p = [373,831]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [23,48]:
        if s.game.yellow_odds.position != 5:
            p = [425,831]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [17,42]:
        if s.game.yellow_odds.position != 6:
            p = [474,831]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [19,44]:
        if s.game.yellow_odds.position != 7:
            p = [522,831]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [11,36]:
        if s.game.yellow_odds.position != 8:
            p = [568,831]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [2,27]:
        if s.game.red_odds.position != 1:
            p = [190,765]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [15,40]:
        if s.game.red_odds.position != 2:
            p = [250,765]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [0,25]:
        if s.game.red_odds.position != 3:
            p = [312,765]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [9,34]:
        if s.game.red_odds.position != 4:
            p = [373,765]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [20,45]:
        if s.game.red_odds.position != 5:
            p = [425,765]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [12,37]:
        if s.game.red_odds.position != 6:
            p = [474,765]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [1,26]:
        if s.game.red_odds.position != 7:
            p = [522,765]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [6,31]:
        if s.game.red_odds.position != 8:
            p = [568,765]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [17,42]:
        if s.game.green_odds.position != 1:
            p = [190,903]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [19,44]:
        if s.game.green_odds.position != 2:
            p = [250,903]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [14,39]:
        if s.game.green_odds.position != 3:
            p = [312,903]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [3,28]:
        if s.game.green_odds.position != 4:
            p = [373,903]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [23,48]:
        if s.game.green_odds.position != 5:
            p = [425,903]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [8,33]:
        if s.game.green_odds.position != 6:
            p = [474,903]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [21,46]:
        if s.game.green_odds.position != 7:
            p = [522,903]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [10,35]:
        if s.game.green_odds.position != 8:
            p = [568,903]
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
    if s.game.one_seven_feature.status == False:
        dirty_rects.append(screen.blit(bg_gi, (527,231), pygame.Rect(527,231,169,63)))
    if s.game.before_fourth.status == False:
        dirty_rects.append(screen.blit(bg_gi, (551,572), pygame.Rect(551,572,124,54)))
    if s.game.rollovers.status == False:
        dirty_rects.append(screen.blit(bg_gi, (549,519), pygame.Rect(549,519,124,54)))
    if s.game.before_fifth.status == False:
        dirty_rects.append(screen.blit(bg_gi, (549,465), pygame.Rect(549,465,124,54)))
    if s.game.after_fifth.status == False:
        dirty_rects.append(screen.blit(bg_gi, (550,409), pygame.Rect(550,409,124,54)))
    if s.game.yellow_super_section.status == False:
        dirty_rects.append(screen.blit(bg_gi, (50,452), pygame.Rect(50,452,122,88)))
    if s.game.red_super_section.status == False:
        dirty_rects.append(screen.blit(bg_gi, (50,539), pygame.Rect(50,539,122,88)))
    if s.game.magic_screen_feature.position < 4:
        dirty_rects.append(screen.blit(bg_gi, (31,669), pygame.Rect(31,669,36,49)))
        dirty_rects.append(screen.blit(bg_gi, (68,669), pygame.Rect(68,669,36,49)))
        dirty_rects.append(screen.blit(bg_gi, (105,669), pygame.Rect(105,669,36,49)))
        dirty_rects.append(screen.blit(bg_gi, (142,669), pygame.Rect(142,669,36,49)))
    if s.game.magic_screen_feature.position < 6:
        dirty_rects.append(screen.blit(bg_gi, (211,669), pygame.Rect(211,669,36,49)))
    if s.game.magic_screen_feature.position < 8:
        dirty_rects.append(screen.blit(bg_gi, (277,669), pygame.Rect(277,669,36,49)))
        dirty_rects.append(screen.blit(bg_gi, (51,359), pygame.Rect(51,359,57,92)))
        dirty_rects.append(screen.blit(bg_gi, (112,357), pygame.Rect(112,357,57,92)))
    if s.game.magic_screen_feature.position < 10:
        dirty_rects.append(screen.blit(bg_gi, (343,669), pygame.Rect(343,669,36,49)))
    if s.game.magic_screen_feature.position < 12:
        dirty_rects.append(screen.blit(bg_gi, (408,669), pygame.Rect(408,669,36,49)))

    pygame.display.update(dirty_rects)


def draw_feature_animation(s, num):
    global screen
    dirty_rects = []
    
    if num in [4,13,29,38]:
        if s.game.one_seven_feature.status == False:
            p = [527,231]
            dirty_rects.append(screen.blit(one_seven_feature, p))
            pygame.display.update(dirty_rects)
            return
    if num in [10,19,35,44]:
        if s.game.before_fourth.status == False:
            p = [551,572]
            dirty_rects.append(screen.blit(feature, p))
            pygame.display.update(dirty_rects)
            return
    if num in [9,24,34,49]:
        if s.game.before_fifth.status == False:
            p = [549,465]
            dirty_rects.append(screen.blit(feature, p))
            pygame.display.update(dirty_rects)
            return
    if num in [6,17,21,31,42,46]:
        if s.game.after_fifth.status == False:
            p = [550,409]
            dirty_rects.append(screen.blit(feature, p))
            pygame.display.update(dirty_rects)
            return
    if num in [11,36]:
        if s.game.rollovers.status == False:
            p = [549,519]
            dirty_rects.append(screen.blit(feature, p))
            s.game.coils.redROLamp.pulse()
            s.game.coils.yellowROLamp.pulse()
            pygame.display.update(dirty_rects)
            return
    if num in [7,0,25,32]:
        if s.game.yellow_super_section.status == False:
            if s.game.red_super_section.status == False:
                p = [50,452]
                dirty_rects.append(screen.blit(super_section, p))
                pygame.display.update(dirty_rects)
                return
    if num in [18,24,49,43]:
        if s.game.red_super_section.status == False:
            if s.game.yellow_super_section.status == False:
                p = [50,539]
                dirty_rects.append(screen.blit(super_section, p))
                pygame.display.update(dirty_rects)
                return
    if num in [2,12,27,37]:
        if s.game.magic_screen_feature.position < 4:
            p = [31,669]
            dirty_rects.append(screen.blit(ms_letter, p))
            p = [68,669]
            dirty_rects.append(screen.blit(ms_letter, p))
            p = [105,669]
            dirty_rects.append(screen.blit(ms_letter, p))
            p = [142,669]
            dirty_rects.append(screen.blit(ms_letter, p))
            pygame.display.update(dirty_rects)
            return
    if num in [22,47]:
        if s.game.magic_screen_feature.position < 6:
            p = [211,669]
            dirty_rects.append(screen.blit(ms_letter, p))
            pygame.display.update(dirty_rects)
            return
    if num in [14,25,39,50]:
        if s.game.magic_screen_feature.position < 8:
            p = [277,669]
            dirty_rects.append(screen.blit(ms_letter, p))
            p = [51,359]
            dirty_rects.append(screen.blit(three_blue, p))
            p = [112,357]
            dirty_rects.append(screen.blit(three_blue, p))
            pygame.display.update(dirty_rects)
            return
    if num in [5,15,30,40]:
        if s.game.magic_screen_feature.position < 10:
            p = [343,669]
            dirty_rects.append(screen.blit(ms_letter, p))
            pygame.display.update(dirty_rects)
            return
    if num in [16,23,41,48]:
        if s.game.magic_screen_feature.position < 12:
            p = [408,669]
            dirty_rects.append(screen.blit(ms_letter, p))
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

