
import pygame
import random

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

meter = pygame.image.load('graphics/assets/register_cover.png').convert()
eb = pygame.image.load('spot_lite/assets/arrow.png').convert_alpha()
exb = pygame.image.load('spot_lite/assets/extra_ball.png').convert_alpha()
o1 = pygame.image.load('spot_lite/assets/odds_gi.png').convert_alpha()
o = pygame.image.load('spot_lite/assets/odds.png').convert_alpha()
o10 = pygame.image.load('spot_lite/assets/odds10.png').convert_alpha()
c = pygame.image.load('spot_lite/assets/corners.png').convert_alpha()
number = pygame.image.load('spot_lite/assets/number.png').convert_alpha()
tilt = pygame.image.load('spot_lite/assets/tilt.png').convert_alpha()
bg_menu = pygame.image.load('spot_lite/assets/spot_lite_menu.png')
bg_gi = pygame.image.load('spot_lite/assets/spot_lite_gi.png')
bg_off = pygame.image.load('spot_lite/assets/spot_lite_off.png')

class scorereel():
    """ Score Reels are used to count replays """
    def __init__(self, pos, image):
        self.position = pos
        self.default_y = self.position[1]
        self.image = pygame.image.load(image).convert()

reel1 = scorereel([625,782], "graphics/assets/green_reel.png")
reel10 = scorereel([605,782], "graphics/assets/green_reel.png")
reel100 = scorereel([587,782], "graphics/assets/green_reel.png")

def display(s, replays=0, menu=False):
    
    meter.set_colorkey((255,0,252))
    meter_position = [577,782]

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

    if s.game.extra_ball.position == 1:
        eb_position = [32,934]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 2:
        eb_position = [58,934]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 3:
        eb_position = [85,934]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 4:
        eb_position = [111,934]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 5:
        eb_position = [136,934]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 6:
        eb_position = [161,934]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 7:
        eb_position = [188,934]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 8:
        eb_position = [215,934]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 9:
        eb_position = [241,934]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 10:
        eb_position = [267,934]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 11:
        eb_position = [293,934]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 12:
        eb_position = [319,934]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 13:
        eb_position = [377,934]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 14:
        eb_position = [403,934]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 15:
        eb_position = [428,934]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 16:
        eb_position = [455,934]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 17:
        eb_position = [481,934]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 18:
        eb_position = [507,934]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 19:
        eb_position = [533,934]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 20:
        eb_position = [559,934]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 21:
        eb_position = [586,934]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 22:
        eb_position = [612,934]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 23:
        eb_position = [634,934]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 24:
        eb_position = [663,934]
        screen.blit(eb, eb_position)

    if s.game.extra_ball.position >= 12:
        eb_position = [29,979]
        screen.blit(exb, eb_position)
    if s.game.extra_ball.position >= 24:
        eb_position = [374,979]
        screen.blit(exb, eb_position)

    if s.game.odds.position > 0:
        odds_position = [19,371]
        screen.blit(o1, odds_position)
        if s.game.odds.position == 1:
            odds_position = [154,371]
            screen.blit(o, odds_position)
        if s.game.odds.position == 2:
            odds_position = [206,371]
            screen.blit(o, odds_position)
        if s.game.odds.position == 3:
            odds_position = [258,371]
            screen.blit(o, odds_position)
        if s.game.odds.position == 4:
            odds_position = [311,371]
            screen.blit(o, odds_position)
        if s.game.odds.position == 5:
            odds_position = [363,371]
            screen.blit(o, odds_position)
        if s.game.odds.position == 6:
            odds_position = [415,371]
            screen.blit(o, odds_position)
        if s.game.odds.position == 7:
            odds_position = [468,371]
            screen.blit(o, odds_position)
        if s.game.odds.position == 8:
            odds_position = [521,371]
            screen.blit(o, odds_position)
        if s.game.odds.position == 9:
            odds_position = [573,371]
            screen.blit(o, odds_position)
        if s.game.odds.position == 10:
            odds_position = [625,371]
            screen.blit(o10, odds_position)

    if s.game.corners.status == True:
        corners_position = [37,741]
        screen.blit(c, corners_position)

    if s.game.tilt.status == False:
        if s.holes:
            if 1 in s.holes:
                number_position = [199,772]
                screen.blit(number, number_position)
            if 2 in s.holes:
                number_position = [199,706]
                screen.blit(number, number_position)
            if 3 in s.holes:
                number_position = [465,838]
                screen.blit(number, number_position)
            if 4 in s.holes:
                number_position = [398,571]
                screen.blit(number, number_position)
            if 5 in s.holes:
                number_position = [333,838]
                screen.blit(number, number_position)
            if 6 in s.holes:
                number_position = [464,571]
                screen.blit(number, number_position)
            if 7 in s.holes:
                number_position = [265,841]
                screen.blit(number, number_position)
            if 8 in s.holes:
                number_position = [466,772]
                screen.blit(number, number_position)
            if 9 in s.holes:
                number_position = [199,573]
                screen.blit(number, number_position)
            if 10 in s.holes:
                number_position = [201,838]
                screen.blit(number, number_position)
            if 11 in s.holes:
                number_position = [333,772]
                screen.blit(number, number_position)
            if 12 in s.holes:
                number_position = [398,707]
                screen.blit(number, number_position)
            if 13 in s.holes:
                number_position = [200,639]
                screen.blit(number, number_position)
            if 14 in s.holes:
                number_position = [331,640]
                screen.blit(number, number_position)
            if 15 in s.holes:
                number_position = [331,571]
                screen.blit(number, number_position)
            if 16 in s.holes:
                number_position = [333,705]
                screen.blit(number, number_position)
            if 17 in s.holes:
                number_position = [463,707]
                screen.blit(number, number_position)
            if 18 in s.holes:
                number_position = [267,705]
                screen.blit(number, number_position)
            if 19 in s.holes:
                number_position = [266,637]
                screen.blit(number, number_position)
            if 20 in s.holes:
                number_position = [398,637]
                screen.blit(number, number_position)
            if 21 in s.holes:
                number_position = [398,771]
                screen.blit(number, number_position)
            if 22 in s.holes:
                number_position = [267,771]
                screen.blit(number, number_position)
            if 23 in s.holes:
                number_position = [397,839]
                screen.blit(number, number_position)
            if 24 in s.holes:
                number_position = [267,572]
                screen.blit(number, number_position)
            if 25 in s.holes:
                number_position = [465,639]
                screen.blit(number, number_position)

    if s.game.tilt.status == True:
        tilt_position = [82,882]
        screen.blit(tilt, tilt_position)

    pygame.display.update()

def eb_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]

    if s.game.extra_ball.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (85,934), pygame.Rect(85,934,27,31)))
    if s.game.extra_ball.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (161,934), pygame.Rect(161,934,27,31)))
    if s.game.extra_ball.position != 9:
        dirty_rects.append(screen.blit(bg_gi, (241,934), pygame.Rect(241,934,27,31)))
    if s.game.extra_ball.position != 12:
        dirty_rects.append(screen.blit(bg_gi, (319,934), pygame.Rect(319,934,27,31)))
    if s.game.extra_ball.position != 15:
        dirty_rects.append(screen.blit(bg_gi, (428,934), pygame.Rect(428,934,27,31)))
    if s.game.extra_ball.position != 18:
        dirty_rects.append(screen.blit(bg_gi, (507,934), pygame.Rect(507,934,27,31)))
    if s.game.extra_ball.position != 21:
        dirty_rects.append(screen.blit(bg_gi, (586,934), pygame.Rect(586,934,27,31)))
    if s.game.extra_ball.position != 24:
        dirty_rects.append(screen.blit(bg_gi, (663,934), pygame.Rect(663,934,27,31)))
    pygame.display.update(dirty_rects)

    if num in [2,10,18,27,35,43]:
        if s.game.extra_ball.position != 3:
            p = [85,934]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [3,11,19,28,36,44]:
        if s.game.extra_ball.position != 6:
            p = [161,934]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [4,12,20,29,37,45]:
        if s.game.extra_ball.position != 9:
            p = [241,934]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [5,13,21,30,38,46]:
        if s.game.extra_ball.position != 12:
            p = [319,934]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [6,14,22,31,39,47]:
        if s.game.extra_ball.position != 15:
            p = [428,934]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [7,15,23,32,40,48]:
        if s.game.extra_ball.position != 18:
            p = [507,934]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [8,16,24,33,41,49]:
        if s.game.extra_ball.position != 21:
            p = [586,934]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [9,17,25,34,42,0]:
        if s.game.extra_ball.position != 24:
            p = [663,934]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return

def clear_odds(s, num):
    global screen

    dirty_rects = []

    if s.game.odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (154,371), pygame.Rect(154,371,62,181)))
    if s.game.odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (206,371), pygame.Rect(206,371,62,181)))
    if s.game.odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (258,371), pygame.Rect(258,371,62,181)))
    if s.game.odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (311,371), pygame.Rect(311,371,62,181)))
    if s.game.odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (363,371), pygame.Rect(363,371,62,181)))
    if s.game.odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (415,371), pygame.Rect(415,371,62,181)))
    if s.game.odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (468,371), pygame.Rect(468,371,62,181)))
    if s.game.odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (521,371), pygame.Rect(521,371,62,181)))
    if s.game.odds.position != 9:
        dirty_rects.append(screen.blit(bg_gi, (573,371), pygame.Rect(573,371,62,181)))
    if s.game.odds.position != 10:
        dirty_rects.append(screen.blit(bg_gi, (625,371), pygame.Rect(625,371,69,181)))
    pygame.display.update(dirty_rects)

def draw_odds_animation(s, num):
    global screen
    dirty_rects = []

    if num in [8,33]:
        if s.game.odds.position != 1:
            p = [153,371]
            dirty_rects.append(screen.blit(o, p))
            pygame.display.update(dirty_rects)
            return
    if num in [2,16,21,27,31,46]:
        if s.game.odds.position != 2:
            p = [206,371]
            dirty_rects.append(screen.blit(o, p))
            pygame.display.update(dirty_rects)
            return
    if num in [1,6,13,20,26,31,38,45]:
        if s.game.odds.position != 3:
            p = [258,371]
            dirty_rects.append(screen.blit(o, p))
            pygame.display.update(dirty_rects)
            return
    if num in [11,25,36,0]:
        if s.game.odds.position != 4:
            p = [311,371]
            dirty_rects.append(screen.blit(o, p))
            pygame.display.update(dirty_rects)
            return
    if num in [3,15,22,28,40,47]:
        if s.game.odds.position != 5:
            p = [363,371]
            dirty_rects.append(screen.blit(o, p))
            pygame.display.update(dirty_rects)
            return
    if num in [5,10,19,30,35,44]:
        if s.game.odds.position != 6:
            p = [415,371]
            dirty_rects.append(screen.blit(o, p))
            pygame.display.update(dirty_rects)
            return
    if num in [12,24,37,49]:
        if s.game.odds.position != 7:
            p = [468,371]
            dirty_rects.append(screen.blit(o, p))
            pygame.display.update(dirty_rects)
            return
    if num in [14,18,39,43]:
        if s.game.odds.position != 8:
            p = [521,371]
            dirty_rects.append(screen.blit(o, p))
            pygame.display.update(dirty_rects)
            return
    if num in [7,17,32,42]:
        if s.game.odds.position != 9:
            p = [573,371]
            dirty_rects.append(screen.blit(o, p))
            pygame.display.update(dirty_rects)
            return
    if num in [4,9,23,29,34,48]:
        if s.game.odds.position != 10:
            p = [625,371]
            dirty_rects.append(screen.blit(o10, p))
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
    if 2 not in s.holes:
        dirty_rects.append(screen.blit(bg_gi, (199,706), pygame.Rect(199,706,59,55)))
    if 5 not in s.holes:
        dirty_rects.append(screen.blit(bg_gi, (333,838), pygame.Rect(333,838,59,55)))
    if 15 not in s.holes:
        dirty_rects.append(screen.blit(bg_gi, (331,571), pygame.Rect(331,571,59,55)))
    if 16 not in s.holes:
        dirty_rects.append(screen.blit(bg_gi, (333,705), pygame.Rect(333,705,59,55)))
    if 17 not in s.holes:
        dirty_rects.append(screen.blit(bg_gi, (463,707), pygame.Rect(463,707,59,55)))
    if s.game.corners.status == False:
        dirty_rects.append(screen.blit(bg_gi, (37,741), pygame.Rect(37,741,135,135)))

    pygame.display.update(dirty_rects)


def draw_feature_animation(s, num):
    global screen
    dirty_rects = []

    if num in [2,8,18,20,27,33,43,45]:
        if 2 not in s.holes:
            p = [199,706]
            dirty_rects.append(screen.blit(number, p))
            pygame.display.update(dirty_rects)
            return
    if num in [5,10,16,22,30,35,41,47]:
        if 5 not in s.holes:
            p = [333,838]
            dirty_rects.append(screen.blit(number, p))
            pygame.display.update(dirty_rects)
            return
    if num in [6,12,15,23,31,37,40,48]:
        if 15 not in s.holes:
            p = [331,571]
            dirty_rects.append(screen.blit(number, p))
            pygame.display.update(dirty_rects)
            return
    if num in [1,4,11,14,24,26,29,36,39,49]:
        if 16 not in s.holes:
            p = [333,705]
            dirty_rects.append(screen.blit(number, p))
            pygame.display.update(dirty_rects)
            return
    if num in [3,9,17,21,28,34,42,46]:
        if 17 not in s.holes:
            p = [463,707]
            dirty_rects.append(screen.blit(number, p))
            pygame.display.update(dirty_rects)
            return
    if num in [7,13,19,25,32,38,44,0]:
        if s.game.corners.status == False:
            p = [37,741]
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

