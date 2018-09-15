
import pygame
import random

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

meter = pygame.image.load('graphics/assets/register_cover.png').convert()
magic_screen = pygame.image.load('sea_island/assets/magic_screen.png').convert()
number_card = pygame.image.load('sea_island/assets/number_card.png').convert()
odds = pygame.image.load('sea_island/assets/odds.png').convert_alpha()
eb = pygame.image.load('sea_island/assets/extra_ball.png').convert_alpha()
eb_number = pygame.image.load('sea_island/assets/eb_number.png').convert_alpha()
extra_balls = pygame.image.load('sea_island/assets/extra_balls.png').convert_alpha()
feature = pygame.image.load('sea_island/assets/selection.png').convert_alpha()
ms_indicator = pygame.image.load('sea_island/assets/ms_arrow.png').convert_alpha()
ms_teaser = pygame.image.load('sea_island/assets/ms_teaser.png').convert_alpha()
ti = pygame.image.load('sea_island/assets/selection_arrow.png').convert_alpha()
super_section = pygame.image.load('sea_island/assets/super_section.png').convert_alpha()
ms_letter = pygame.image.load('sea_island/assets/ms_letter.png').convert_alpha()
number = pygame.image.load('sea_island/assets/number.png').convert_alpha()
select_now = pygame.image.load('sea_island/assets/select_now.png').convert_alpha()
three_blue = pygame.image.load('sea_island/assets/blue_section.png').convert_alpha()
tilt = pygame.image.load('sea_island/assets/tilt.png').convert_alpha()
bg_menu = pygame.image.load('sea_island/assets/sea_island_menu.png').convert()
bg_menu.set_colorkey((255,0,252))
bg_gi = pygame.image.load('sea_island/assets/sea_island_gi.png').convert()
bg_gi.set_colorkey((255,0,252))
bg_off = pygame.image.load('sea_island/assets/sea_island_off.png').convert()
bg_off.set_colorkey((255,0,252))

class scorereel():
    """ Score Reels are used to count replays """
    def __init__(self, pos, image):
        self.position = pos
        self.default_y = self.position[1]
        self.image = pygame.image.load(image).convert()

reel1 = scorereel([97,793], "graphics/assets/white_reel.png")
reel10 = scorereel([78,793], "graphics/assets/white_reel.png")
reel100 = scorereel([59,793], "graphics/assets/white_reel.png")

def display(s, replays=0, menu=False):
    
    meter.set_colorkey((255,0,252))
    meter_position = [50,793]

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
        eb_position = [40,1029]
        screen.blit(extra_balls, eb_position)

    if s.game.extra_ball.position >= 1:
        eb_position = [151,1029]
        screen.blit(eb_number, eb_position)
    if s.game.extra_ball.position >= 2:
        eb_position = [198,1029]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 3:
        eb_position = [262,1029]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 4:
        eb_position = [330,1029]
        screen.blit(eb_number, eb_position)
    if s.game.extra_ball.position >= 5:
        eb_position = [376,1029]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 6:
        eb_position = [436,1029]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 7:
        eb_position = [506,1029]
        screen.blit(eb_number, eb_position)
    if s.game.extra_ball.position >= 8:
        eb_position = [554,1029]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 9:
        eb_position = [617,1029]
        screen.blit(eb, eb_position)
    

    if s.game.selection_feature.position == 1 or s.game.selection_feature.position == 2:
        i = [672,583]
        screen.blit(ti, i)
    if s.game.selection_feature.position == 3:
        i = [672,528]
        screen.blit(ti, i)
    if s.game.selection_feature.position == 4 or s.game.selection_feature.position == 5 or s.game.selection_feature.position == 6:
        i = [672,476]
        screen.blit(ti, i)
    if s.game.selection_feature.position == 7:
        i = [672,422]
        screen.blit(ti, i)
    if s.game.selection_feature.position == 8:
        i = [672,368]
        screen.blit(ti, i)

    if s.game.red_star.status == True:
        rs_position = [550,459]
        screen.blit(feature, rs_position)
    if s.game.yellow_star.status == True:
        rs_position = [550,516]
        screen.blit(feature, rs_position)

    if s.game.magic_screen_feature.position >= 7:
        if s.game.selection_feature.position < 7:
            bfp = [550,568]
            screen.blit(feature, bfp)
            if s.game.ball_count.position == 3:
                s.cancel_delayed(name="blink")
                blink([s,1,1])
            else:
                s.cancel_delayed(name="blink")
        elif s.game.selection_feature.position == 7:
            bfp = [550,408]
            screen.blit(feature, bfp)
            if s.game.ball_count.position == 4:
                s.cancel_delayed(name="blink")
                blink([s,1,1])
            else:
                s.cancel_delayed(name="blink")
        elif s.game.selection_feature.position == 8:
            bfp = [550,354]
            screen.blit(feature, bfp)
            if s.game.ball_count.position == 5:
                s.cancel_delayed(name="blink")
                blink([s,1,1])
            else:
                s.cancel_delayed(name="blink")

    if s.game.magic_screen_feature.position >= 9:
        if s.game.three_blue.status == True:
            bp = [55,348]
            screen.blit(three_blue, bp)
        elif s.game.two_blue.status == True:
            bp = [117,348]
            screen.blit(three_blue, bp)

    if s.game.red_super_section.status == True:
        rss = [53,441]
        screen.blit(super_section, rss)
    if s.game.yellow_super_section.status == True:
        yss = [53,537]
        screen.blit(super_section, yss)

    if s.game.magic_screen_feature.position == 1:
        ms = [28,679]
        screen.blit(ms_teaser, ms)
    if s.game.magic_screen_feature.position == 2:
        ms = [68,679]
        screen.blit(ms_teaser, ms)
    if s.game.magic_screen_feature.position == 3:
        ms = [105,679]
        screen.blit(ms_teaser, ms)
    if s.game.magic_screen_feature.position >= 4:
        ms = [153,673]
        screen.blit(ms_letter, ms)
    if s.game.magic_screen_feature.position >= 5:
        ms = [190,673]
        screen.blit(ms_letter, ms)
    if s.game.magic_screen_feature.position >= 6:
        ms = [227,673]
        screen.blit(ms_letter, ms)
    if s.game.magic_screen_feature.position >= 7:
        ms = [263,673]
        screen.blit(ms_letter, ms)
    if s.game.magic_screen_feature.position >= 8:
        ms = [299,673]
        screen.blit(ms_letter, ms)
    if s.game.magic_screen_feature.position >= 9:
        ms = [334,673]
        screen.blit(ms_letter, ms)
    if s.game.magic_screen_feature.position >= 10:
        ms = [370,673]
        screen.blit(ms_letter, ms)
    if s.game.magic_screen_feature.position >= 11:
        ms = [405,673]
        screen.blit(ms_letter, ms)

    if s.game.magic_screen.position == 1:
        ms = [155,724]
        screen.blit(ms_indicator, ms)
    if s.game.magic_screen.position == 2:
        ms = [192,724]
        screen.blit(ms_indicator, ms)
    if s.game.magic_screen.position == 3:
        ms = [229,724]
        screen.blit(ms_indicator, ms)
    if s.game.magic_screen.position == 4:
        ms = [265,724]
        screen.blit(ms_indicator, ms)
    if s.game.magic_screen.position == 5:
        ms = [301,724]
        screen.blit(ms_indicator, ms)
    if s.game.magic_screen.position == 6:
        ms = [336,724]
        screen.blit(ms_indicator, ms)
    if s.game.magic_screen.position == 7:
        ms = [372,724]
        screen.blit(ms_indicator, ms)
    if s.game.magic_screen.position == 8:
        ms = [407,724]
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
        o = [190,779]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 2:
        o = [250,779]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 3:
        o = [312,779]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 4:
        o = [373,779]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 5:
        o = [425,779]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 6:
        o = [474,779]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 7:
        o = [522,779]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 8:
        o = [568,779]
        screen.blit(odds, o)

    if s.game.yellow_odds.position == 1:
        o = [190,845]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 2:
        o = [250,845]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 3:
        o = [312,845]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 4:
        o = [373,845]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 5:
        o = [425,845]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 6:
        o = [474,845]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 7:
        o = [522,845]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 8:
        o = [568,845]
        screen.blit(odds, o)

    if s.game.green_odds.position == 1:
        o = [190,917]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 2:
        o = [250,917]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 3:
        o = [312,917]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 4:
        o = [373,917]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 5:
        o = [425,917]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 6:
        o = [474,917]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 7:
        o = [522,917]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 8:
        o = [568,917]
        screen.blit(odds, o)


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
            p = [570,678]
            dirty_rects.append(screen.blit(select_now, p))
        pygame.display.update(dirty_rects)
    else:
        dirty_rects.append(screen.blit(bg_gi, (570,678), pygame.Rect(570,678,129,38)))
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
            bp = [55,348]
            dirty_rects.append(screen.blit(bg_gi, bp, pygame.Rect(bp[0],bp[1],57,90)))
            dirty_rects.append(screen.blit(three_blue, bp))
        elif s.game.two_blue.status == True:
            bp = [117,348]
            dirty_rects.append(screen.blit(bg_gi, bp, pygame.Rect(bp[0],bp[1],57,90)))
            dirty_rects.append(screen.blit(three_blue, bp))
    if s.game.magic_screen_feature.position >= 4:
        if s.game.selection_feature.position < 7:
            p = [550,568]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],117,54)))
            dirty_rects.append(screen.blit(feature, p))
        if s.game.red_star.status == True:
            p = [550,459]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],117,54)))
            dirty_rects.append(screen.blit(feature, p))
        if s.game.yellow_star.status == True:
            p = [550,516]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],117,54)))
            dirty_rects.append(screen.blit(feature, p))
        if s.game.selection_feature.position == 7:
            p = [550,408]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],117,54)))
            dirty_rects.append(screen.blit(feature, p))
        if s.game.selection_feature.position == 8:
            p = [550,354]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],117,54)))
            dirty_rects.append(screen.blit(feature, p))

    if s.game.red_super_section.status == True:
        yss = [53,537]
        dirty_rects.append(screen.blit(bg_gi, (53,537), pygame.Rect(53,537,121,81)))
        dirty_rects.append(screen.blit(super_section, rss))
    if s.game.yellow_super_section.status == True:
        rss = [53,441]
        dirty_rects.append(screen.blit(bg_gi, (53,441), pygame.Rect(53,441,121,81)))
        dirty_rects.append(screen.blit(super_section, yss))

    pygame.display.update(dirty_rects)


def eb_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]

    if s.game.extra_ball.position < 1:
        dirty_rects.append(screen.blit(bg_gi, (151,1029), pygame.Rect(151,1029,44,32)))
    if s.game.extra_ball.position < 2:
        dirty_rects.append(screen.blit(bg_gi, (198,1029), pygame.Rect(198,1029,61,35)))
    if s.game.extra_ball.position < 3:
        dirty_rects.append(screen.blit(bg_gi, (262,1029), pygame.Rect(262,1029,61,35)))
    if s.game.extra_ball.position < 4:
        dirty_rects.append(screen.blit(bg_gi, (330,1029), pygame.Rect(330,1029,44,32)))
    if s.game.extra_ball.position < 5:
        dirty_rects.append(screen.blit(bg_gi, (376,1029), pygame.Rect(376,1029,61,35)))
    if s.game.extra_ball.position < 6:
        dirty_rects.append(screen.blit(bg_gi, (436,1029), pygame.Rect(436,1029,61,35)))
    if s.game.extra_ball.position < 7:
        dirty_rects.append(screen.blit(bg_gi, (506,1029), pygame.Rect(506,1029,44,32)))
    if s.game.extra_ball.position < 8:
        dirty_rects.append(screen.blit(bg_gi, (554,1029), pygame.Rect(554,1029,61,35)))
    if s.game.extra_ball.position < 9:
        dirty_rects.append(screen.blit(bg_gi, (617,1029), pygame.Rect(617,1029,61,35)))
    pygame.display.update(dirty_rects)

    if num in [0,25,14,49]:
        if s.game.extra_ball.position < 1:
            p = [151,1029]
            dirty_rects.append(screen.blit(eb_number, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [39,1,26,15]:
        if s.game.extra_ball.position < 2:
            p = [198,1029]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [3,4,17,28,29,40]:
        if s.game.extra_ball.position < 3:
            p = [262,1029]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [5,18,30,43]:
        if s.game.extra_ball.position < 4:
            p = [330,1029]
            dirty_rects.append(screen.blit(eb_number, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [7,8,19,32,33,44]:
        if s.game.extra_ball.position < 5:
            p = [376,1029]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [9,10,20,34,35,45]:
        if s.game.extra_ball.position < 6:
            p = [436,1029]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [11,21,36,46]:
        if s.game.extra_ball.position < 7:
            p = [506,1029]
            dirty_rects.append(screen.blit(eb_number, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [12,22,37,47]:
        if s.game.extra_ball.position < 8:
            p = [554,1029]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [2,6,13,16,23,27,31,38,41,48]:
        if s.game.extra_ball.position < 9:
            p = [617,1029]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return

def clear_odds(s, num):
    global screen

    dirty_rects = []

    if s.game.yellow_odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (190,845), pygame.Rect(190,845,45,60)))
    if s.game.yellow_odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (250,845), pygame.Rect(250,845,45,60)))
    if s.game.yellow_odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (312,845), pygame.Rect(312,845,45,60)))
    if s.game.yellow_odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (373,845), pygame.Rect(373,845,45,60)))
    if s.game.yellow_odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (425,845), pygame.Rect(425,845,45,60)))
    if s.game.yellow_odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (474,845), pygame.Rect(474,845,45,60)))
    if s.game.yellow_odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (522,845), pygame.Rect(522,845,45,60)))
    if s.game.yellow_odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (568,845), pygame.Rect(568,845,45,60)))

    if s.game.red_odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (190,779), pygame.Rect(190,779,45,60)))
    if s.game.red_odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (250,779), pygame.Rect(250,779,45,60)))
    if s.game.red_odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (312,779), pygame.Rect(312,779,45,60)))
    if s.game.red_odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (373,779), pygame.Rect(373,779,45,60)))
    if s.game.red_odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (425,779), pygame.Rect(425,779,45,60)))
    if s.game.red_odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (474,779), pygame.Rect(474,779,45,60)))
    if s.game.red_odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (522,779), pygame.Rect(522,779,45,60)))
    if s.game.red_odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (568,779), pygame.Rect(568,779,45,60)))

    if s.game.green_odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (190,917), pygame.Rect(190,917,45,60)))
    if s.game.green_odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (250,917), pygame.Rect(250,917,45,60)))
    if s.game.green_odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (312,917), pygame.Rect(312,917,45,60)))
    if s.game.green_odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (373,917), pygame.Rect(373,917,45,60)))
    if s.game.green_odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (425,917), pygame.Rect(425,917,45,60)))
    if s.game.green_odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (474,917), pygame.Rect(474,917,45,60)))
    if s.game.green_odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (522,917), pygame.Rect(522,917,45,60)))
    if s.game.green_odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (568,917), pygame.Rect(568,917,45,60)))

    pygame.display.update(dirty_rects)

def draw_odds_animation(s, num):
    global screen
    dirty_rects = []

    if num in [11,36]:
        if s.game.yellow_odds.position != 1:
            p = [190,845]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [4,29]:
        if s.game.yellow_odds.position != 2:
            p = [250,845]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [7,32]:
        if s.game.yellow_odds.position != 3:
            p = [312,845]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [13,38]:
        if s.game.yellow_odds.position != 4:
            p = [373,845]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [22,47]:
        if s.game.yellow_odds.position != 5:
            p = [425,845]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [17,42]:
        if s.game.yellow_odds.position != 6:
            p = [474,845]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [19,44]:
        if s.game.yellow_odds.position != 7:
            p = [522,845]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [5,30]:
        if s.game.yellow_odds.position != 8:
            p = [568,845]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return

    if num in [0,25]:
        if s.game.red_odds.position != 1:
            p = [190,779]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [15,40]:
        if s.game.red_odds.position != 2:
            p = [250,779]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [24,49]:
        if s.game.red_odds.position != 3:
            p = [312,779]
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
            p = [425,779]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [12,37]:
        if s.game.red_odds.position != 6:
            p = [474,779]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [50,26]:
        if s.game.red_odds.position != 7:
            p = [522,779]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [6,31]:
        if s.game.red_odds.position != 8:
            p = [568,779]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return

    if num in [16,41]:
        if s.game.green_odds.position != 1:
            p = [190,917]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [18,43]:
        if s.game.green_odds.position != 2:
            p = [250,917]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [14,39]:
        if s.game.green_odds.position != 3:
            p = [312,917]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [3,28]:
        if s.game.green_odds.position != 4:
            p = [373,917]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [23,48]:
        if s.game.green_odds.position != 5:
            p = [425,917]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [8,33]:
        if s.game.green_odds.position != 6:
            p = [474,917]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [22,47]:
        if s.game.green_odds.position != 7:
            p = [522,917]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [10,35]:
        if s.game.green_odds.position != 8:
            p = [568,917]
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


    if s.game.selection_feature.position < 7 and (s.game.magic_screen_feature.position < 7):
        dirty_rects.append(screen.blit(bg_gi, (550,568), pygame.Rect(550,568,117,54)))
    if s.game.red_star.status == False:
        dirty_rects.append(screen.blit(bg_gi, (550,459), pygame.Rect(550,459,117,54)))
    if s.game.yellow_star.status == False:
        dirty_rects.append(screen.blit(bg_gi, (550,516), pygame.Rect(550,516,117,54)))
    if s.game.selection_feature.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (550,408), pygame.Rect(550,408,117,54)))
    if s.game.selection_feature.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (550,354), pygame.Rect(550,354,117,54)))

    if s.game.yellow_super_section.status == False:
        dirty_rects.append(screen.blit(bg_gi, (53,537), pygame.Rect(53,537,119,88)))
    if s.game.red_super_section.status == False:
        dirty_rects.append(screen.blit(bg_gi, (53,441), pygame.Rect(53,441,119,88)))
    if s.game.magic_screen_feature.position < 7:
        dirty_rects.append(screen.blit(bg_gi, (153,673), pygame.Rect(153,673,35,49)))
        dirty_rects.append(screen.blit(bg_gi, (190,673), pygame.Rect(190,673,35,49)))
        dirty_rects.append(screen.blit(bg_gi, (227,673), pygame.Rect(227,673,35,49)))
        dirty_rects.append(screen.blit(bg_gi, (263,673), pygame.Rect(263,673,35,49)))
    if s.game.magic_screen_feature.position < 8:
        dirty_rects.append(screen.blit(bg_gi, (299,673), pygame.Rect(299,673,35,49)))
    if s.game.magic_screen_feature.position < 9:
        dirty_rects.append(screen.blit(bg_gi, (334,673), pygame.Rect(334,673,35,49)))
    if s.game.magic_screen_feature.position < 10:
        dirty_rects.append(screen.blit(bg_gi, (370,673), pygame.Rect(370,673,35,49)))
    if s.game.magic_screen_feature.position < 11:
        dirty_rects.append(screen.blit(bg_gi, (405,673), pygame.Rect(405,673,35,49)))
    if s.game.three_blue.status == False:
        dirty_rects.append(screen.blit(bg_gi, (55,348), pygame.Rect(55,348,57,90)))
    if s.game.two_blue.status == False:
        dirty_rects.append(screen.blit(bg_gi, (117,348), pygame.Rect(117,348,57,90)))

    pygame.display.update(dirty_rects)


def draw_feature_animation(s, num):
    global screen
    dirty_rects = []
 

    if num in [10,35,19,44]:
        if (s.game.magic_screen_feature.position < 7) and s.game.selection_feature.position not in [7,8]:
            p = [550,568]
            dirty_rects.append(screen.blit(feature, p))
            pygame.display.update(dirty_rects)
            return
    if num in [9,34]:
        if s.game.selection_feature.position != 7:
            p = [550,408]
            dirty_rects.append(screen.blit(feature, p))
            pygame.display.update(dirty_rects)
            return
    if num in [6,17,21,31,42,46]:
        if s.game.selection_feature.position != 8:
            p = [550,354]
            dirty_rects.append(screen.blit(feature, p))
            pygame.display.update(dirty_rects)
            return
    if num in [4,29,13,38]:
        if s.game.red_star.status == False:
            p = [550,459]
            dirty_rects.append(screen.blit(feature, p))
            s.game.coils.redROLamp.pulse(85)
            pygame.display.update(dirty_rects)
            return
    if num in [11,36]:
        if s.game.yellow_star.status == False:
            p = [550,516]
            dirty_rects.append(screen.blit(feature, p))
            s.game.coils.yellowROLamp.pulse(85)
            pygame.display.update(dirty_rects)
            return
    if num in [7,32,0,26]:
        if s.game.yellow_super_section.status == False:
            if s.game.red_super_section.status == False:
                p = [53,537]
                dirty_rects.append(screen.blit(super_section, p))
                pygame.display.update(dirty_rects)
                return
    if num in [18,24,49,43]:
        if s.game.red_super_section.status == False:
            if s.game.yellow_super_section.status == False:
                p = [53,441]
                dirty_rects.append(screen.blit(super_section, p))
                pygame.display.update(dirty_rects)
                return
    

    if num in [2,12,27,37]:
        if s.game.magic_screen_feature.position < 7:
            p = [153,673]
            dirty_rects.append(screen.blit(ms_letter, p))
            p = [190,673]
            dirty_rects.append(screen.blit(ms_letter, p))
            p = [227,673]
            dirty_rects.append(screen.blit(ms_letter, p))
            p = [263,673]
            dirty_rects.append(screen.blit(ms_letter, p))
            pygame.display.update(dirty_rects)
            return
    if num in [3,22,28,47]:
        if s.game.magic_screen_feature.position < 8:
            p = [299,673]
            dirty_rects.append(screen.blit(ms_letter, p))
            pygame.display.update(dirty_rects)
            return
    if num in [14,39,25,50]:
        if s.game.magic_screen_feature.position < 9:
            p = [334,673]
            dirty_rects.append(screen.blit(ms_letter, p))
            pygame.display.update(dirty_rects)
            return
    if num in [5,15,30,40,22,47]:
        if s.game.magic_screen_feature.position < 10:
            p = [370,673]
            dirty_rects.append(screen.blit(ms_letter, p))
            pygame.display.update(dirty_rects)
            return
    if num in [16,41,23,48]:
        if s.game.magic_screen_feature.position < 11:
            p = [405,673]
            dirty_rects.append(screen.blit(ms_letter, p))
            pygame.display.update(dirty_rects)
            return
    if num in [8,20,33,45]:
        if s.game.three_blue.status == False:
            p = [55,348]
            dirty_rects.append(screen.blit(three_blue, p))
            pygame.display.update(dirty_rects)
            return
        else:
            if s.game.two_blue.status == False:
                p = [117,348]
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
