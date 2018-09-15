# NOTE: The animations are hacked in based off of Spot-Lite's animations.  I feel this is a reasonable alternative to knowing someone with the game.


import pygame
import random

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

meter = pygame.image.load('graphics/assets/register_cover.png').convert()
eb = pygame.image.load('palm_beach/assets/arrow.png').convert_alpha()
exb = pygame.image.load('palm_beach/assets/extra_ball.png').convert_alpha()
og = pygame.image.load('palm_beach/assets/odds_gi.png').convert_alpha()
o10 = pygame.image.load('palm_beach/assets/odds10.png').convert_alpha()
o = pygame.image.load('palm_beach/assets/odds.png').convert_alpha()
sc = pygame.image.load('palm_beach/assets/super_card.png').convert_alpha()
star = pygame.image.load('palm_beach/assets/star.png').convert_alpha()
c = pygame.image.load('palm_beach/assets/corners.png').convert_alpha()
number = pygame.image.load('palm_beach/assets/number.png').convert_alpha()
sc_number = pygame.image.load('palm_beach/assets/sc_number.png').convert_alpha()
tilt = pygame.image.load('palm_beach/assets/tilt.png').convert_alpha()
oo = pygame.image.load('palm_beach/assets/play.png').convert_alpha()
f = pygame.image.load('palm_beach/assets/play.png').convert_alpha()
ebs = pygame.image.load('palm_beach/assets/extra_balls.png').convert_alpha()
bg_menu = pygame.image.load('palm_beach/assets/palm_beach_menu.png')
bg_gi = pygame.image.load('palm_beach/assets/palm_beach_gi.png')
bg_off = pygame.image.load('palm_beach/assets/palm_beach_off.png')

class scorereel():
    """ Score Reels are used to count replays """
    def __init__(self, pos, image):
        self.position = pos
        self.default_y = self.position[1]
        self.image = pygame.image.load(image).convert()

reel1 = scorereel([110,569], "graphics/assets/green_reel.png")
reel10 = scorereel([90,569], "graphics/assets/green_reel.png")
reel100 = scorereel([72,569], "graphics/assets/green_reel.png")

def display(s, replays=0, menu=False):
    
    meter.set_colorkey((255,0,252))
    meter_position = [61,570]

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
        eb_position = [31,960]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 2:
        eb_position = [57,960]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 3:
        eb_position = [84,960]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 4:
        eb_position = [111,960]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 5:
        eb_position = [137,960]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 6:
        eb_position = [163,960]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 7:
        eb_position = [189,960]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 8:
        eb_position = [215,960]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 9:
        eb_position = [259,960]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 10:
        eb_position = [286,960]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 11:
        eb_position = [312,960]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 12:
        eb_position = [339,960]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 13:
        eb_position = [365,960]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 14:
        eb_position = [391,960]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 15:
        eb_position = [417,960]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 16:
        eb_position = [445,960]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 17:
        eb_position = [487,960]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 18:
        eb_position = [515,960]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 19:
        eb_position = [540,960]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 20:
        eb_position = [567,960]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 21:
        eb_position = [593,960]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 22:
        eb_position = [618,960]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 23:
        eb_position = [645,960]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 24:
        eb_position = [672,960]
        screen.blit(eb, eb_position)

    if s.game.extra_ball.position >= 8:
        eb_position = [28,986]
        screen.blit(exb, eb_position)
    if s.game.extra_ball.position >= 16:
        eb_position = [256,986]
        screen.blit(exb, eb_position)
    if s.game.extra_ball.position >= 24:
        eb_position = [483,986]
        screen.blit(exb, eb_position)

    if s.game.odds.position > 0:
        odds_position = [39,398]
        screen.blit(og, odds_position)
        if s.game.odds.position == 1:
            odds_position = [159,397]
            screen.blit(o, odds_position)
        if s.game.odds.position == 2:
            odds_position = [212,397]
            screen.blit(o, odds_position)
        if s.game.odds.position == 3:
            odds_position = [265,397]
            screen.blit(o, odds_position)
        if s.game.odds.position == 4:
            odds_position = [318,397]
            screen.blit(o, odds_position)
        if s.game.odds.position == 5:
            odds_position = [370,397]
            screen.blit(o, odds_position)
        if s.game.odds.position == 6:
            odds_position = [421,397]
            screen.blit(o, odds_position)
        if s.game.odds.position == 7:
            odds_position = [474,397]
            screen.blit(o, odds_position)
        if s.game.odds.position == 8:
            odds_position = [526,397]
            screen.blit(o, odds_position)
        if s.game.odds.position == 9:
            odds_position = [578,397]
            screen.blit(o, odds_position)
        if s.game.odds.position == 10:
            odds_position = [631,397]
            screen.blit(o10, odds_position)

    if s.game.super_card.position > 0:
        if s.game.super_card.position == 1:
            sc_position = [51,691]
            screen.blit(eb, sc_position)
        if s.game.super_card.position == 2:
            sc_position = [77,691]
            screen.blit(eb, sc_position)
        if s.game.super_card.position == 3:
            sc_position = [105,691]
            screen.blit(eb, sc_position)
        if s.game.super_card.position == 4:
            sc_position = [131,691]
            screen.blit(eb, sc_position)
        if s.game.super_card.position == 5:
            sc_position = [568,691]
            screen.blit(eb, sc_position)
        if s.game.super_card.position == 6:
            sc_position = [595,691]
            screen.blit(eb, sc_position)
        if s.game.super_card.position == 7:
            sc_position = [621,691]
            screen.blit(eb, sc_position)
        if s.game.super_card.position == 8:
            sc_position = [648,691]
            screen.blit(eb, sc_position)
        if s.game.super_card.position >= 4:
            s_position = [47,719]
            screen.blit(sc, s_position)
        if s.game.super_card.position >= 8:
            s2_position = [564,719]
            screen.blit(sc, s2_position)

    if s.game.red_star.status == True:
        rs_position = [72,884]
        screen.blit(star, rs_position)

    if s.game.yellow_star.status == True:
        ys_position = [586,884]
        screen.blit(star, ys_position)

    if s.game.corners.status == True:
        corners_position = [568,555]
        screen.blit(c, corners_position)

    if s.game.tilt.status == False:
        if s.holes:
            if 1 in s.holes:
                number_position = [203,704]
                screen.blit(number, number_position)
                number_position = [43,793]
                screen.blit(sc_number, number_position)
            if 2 in s.holes:
                number_position = [203,768]
                screen.blit(number, number_position)
            if 3 in s.holes:
                number_position = [466,836]
                screen.blit(number, number_position)
                number_position = [602,755]
                screen.blit(sc_number, number_position)
            if 4 in s.holes:
                number_position = [332,575]
                screen.blit(number, number_position)
                number_position = [84,832]
                screen.blit(sc_number, number_position)
            if 5 in s.holes:
                number_position = [398,836]
                screen.blit(number, number_position)
            if 6 in s.holes:
                number_position = [465,578]
                screen.blit(number, number_position)
            if 7 in s.holes:
                number_position = [269,836]
                screen.blit(number, number_position)
                number_position = [83,752]
                screen.blit(sc_number, number_position)
            if 8 in s.holes:
                number_position = [465,707]
                screen.blit(number, number_position)
            if 9 in s.holes:
                number_position = [203,577]
                screen.blit(number, number_position)
                number_position = [561,793]
                screen.blit(sc_number, number_position)
            if 10 in s.holes:
                number_position = [203,836]
                screen.blit(number, number_position)
                number_position = [84,794]
                screen.blit(sc_number, number_position)
            if 11 in s.holes:
                number_position = [334,772]
                screen.blit(number, number_position)
                number_position = [642,793]
                screen.blit(sc_number, number_position)
            if 12 in s.holes:
                number_position = [399,705]
                screen.blit(number, number_position)
                number_position = [561,834]
                screen.blit(sc_number, number_position)
            if 13 in s.holes:
                number_position = [203,641]
                screen.blit(number, number_position)
                number_position = [124,794]
                screen.blit(sc_number, number_position)
            if 14 in s.holes:
                number_position = [335,641]
                screen.blit(number, number_position)
                number_position = [642,832]
                screen.blit(sc_number, number_position)
            if 15 in s.holes:
                number_position = [269,575]
                screen.blit(number, number_position)
            if 16 in s.holes:
                number_position = [333,704]
                screen.blit(number, number_position)
            if 17 in s.holes:
                number_position = [466,641]
                screen.blit(number, number_position)
            if 18 in s.holes:
                number_position = [267,704]
                screen.blit(number, number_position)
                number_position = [641,752]
                screen.blit(sc_number, number_position)
            if 19 in s.holes:
                number_position = [270,641]
                screen.blit(number, number_position)
                number_position = [44,753]
                screen.blit(sc_number, number_position)
            if 20 in s.holes:
                number_position = [400,641]
                screen.blit(number, number_position)
                number_position = [123,752]
                screen.blit(sc_number, number_position)
            if 21 in s.holes:
                number_position = [400,770]
                screen.blit(number, number_position)
                number_position = [124,835]
                screen.blit(sc_number, number_position)
            if 22 in s.holes:
                number_position = [266,772]
                screen.blit(number, number_position)
                number_position = [44,833]
                screen.blit(sc_number, number_position)
            if 23 in s.holes:
                number_position = [335,836]
                screen.blit(number, number_position)
                number_position = [561,754]
                screen.blit(sc_number, number_position)
            if 24 in s.holes:
                number_position = [400,577]
                screen.blit(number, number_position)
                number_position = [601,833]
                screen.blit(sc_number, number_position)
            if 25 in s.holes:
                number_position = [464,771]
                screen.blit(number, number_position)
                number_position = [600,793]
                screen.blit(sc_number, number_position)

    if s.game.tilt.status == True:
        tilt_position = [550,890]
        screen.blit(tilt, tilt_position)

    if s.game.odds_only.status == True:
        oo_position = [196,906]
        screen.blit(oo, oo_position)

    if s.game.features.status == True:
        f_position = [444,906]
        screen.blit(f, f_position)

    if s.game.eb.status == True:
        ebs_position = [302,925]
        screen.blit(ebs, ebs_position)

    pygame.display.update()

def eb_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]
    if s.game.extra_ball.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (84,960), pygame.Rect(84,960,23,27)))
    if s.game.extra_ball.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (163,960), pygame.Rect(163,960,23,27)))
    if s.game.extra_ball.position != 9:
        dirty_rects.append(screen.blit(bg_gi, (259,960), pygame.Rect(259,960,23,27)))
    if s.game.extra_ball.position != 12:
        dirty_rects.append(screen.blit(bg_gi, (339,960), pygame.Rect(339,960,23,27)))
    if s.game.extra_ball.position != 15:
        dirty_rects.append(screen.blit(bg_gi, (417,960), pygame.Rect(417,960,23,27)))
    if s.game.extra_ball.position != 18:
        dirty_rects.append(screen.blit(bg_gi, (515,960), pygame.Rect(515,960,23,27)))
    if s.game.extra_ball.position != 21:
        dirty_rects.append(screen.blit(bg_gi, (593,960), pygame.Rect(593,960,23,27)))
    if s.game.extra_ball.position != 24:
        dirty_rects.append(screen.blit(bg_gi, (672,960), pygame.Rect(672,960,23,27)))
    pygame.display.update(dirty_rects)

    if num in [2,10,18,27,35,43]:
        if s.game.extra_ball.position != 3:
            p = [84,960]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [3,11,19,28,36,44]:
        if s.game.extra_ball.position != 6:
            p = [163,960]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [4,12,20,29,37,45]:
        if s.game.extra_ball.position != 9:
            p = [259,960]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [5,13,21,30,38,46]:
        if s.game.extra_ball.position != 12:
            p = [339,960]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [6,14,22,31,39,47]:
        if s.game.extra_ball.position != 15:
            p = [417,960]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [7,15,23,32,40,48]:
        if s.game.extra_ball.position != 18:
            p = [515,960]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [8,16,24,33,41,49]:
        if s.game.extra_ball.position != 21:
            p = [593,960]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [9,17,25,34,42,0]:
        if s.game.extra_ball.position != 24:
            p = [672,960]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return

def clear_odds(s, num):
    global screen

    dirty_rects = []
    if s.game.odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (159,397), pygame.Rect(159,397,53,157)))
    if s.game.odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (212,397), pygame.Rect(212,397,53,157)))
    if s.game.odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (265,397), pygame.Rect(265,397,53,157)))
    if s.game.odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (318,397), pygame.Rect(318,397,53,157)))
    if s.game.odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (370,397), pygame.Rect(370,397,53,157)))
    if s.game.odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (421,397), pygame.Rect(421,397,53,157)))
    if s.game.odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (474,397), pygame.Rect(474,397,53,157)))
    if s.game.odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (526,397), pygame.Rect(526,397,53,157)))
    if s.game.odds.position != 9:
        dirty_rects.append(screen.blit(bg_gi, (578,397), pygame.Rect(578,397,53,157)))
    if s.game.odds.position != 10:
        dirty_rects.append(screen.blit(bg_gi, (631,397), pygame.Rect(631,397,56,157)))
    pygame.display.update(dirty_rects)

def draw_odds_animation(s, num):
    global screen
    dirty_rects = []

    if num in [8,33]:
        if s.game.odds.position != 1:
            p = [159,397]
            dirty_rects.append(screen.blit(o, p))
            pygame.display.update(dirty_rects)
            return
    if num in [2,16,21,27,31,46]:
        if s.game.odds.position != 2:
            p = [212,397]
            dirty_rects.append(screen.blit(o, p))
            pygame.display.update(dirty_rects)
            return
    if num in [1,6,13,20,26,31,38,45]:
        if s.game.odds.position != 3:
            p = [265,397]
            dirty_rects.append(screen.blit(o, p))
            pygame.display.update(dirty_rects)
            return
    if num in [11,25,36,0]:
        if s.game.odds.position != 4:
            p = [318,397]
            dirty_rects.append(screen.blit(o, p))
            pygame.display.update(dirty_rects)
            return
    if num in [3,15,22,28,40,47]:
        if s.game.odds.position != 5:
            p = [370,397]
            dirty_rects.append(screen.blit(o, p))
            pygame.display.update(dirty_rects)
            return
    if num in [5,10,19,30,35,44]:
        if s.game.odds.position != 6:
            p = [421,397]
            dirty_rects.append(screen.blit(o, p))
            pygame.display.update(dirty_rects)
            return
    if num in [12,24,37,49]:
        if s.game.odds.position != 7:
            p = [474,397]
            dirty_rects.append(screen.blit(o, p))
            pygame.display.update(dirty_rects)
            return
    if num in [14,18,39,43]:
        if s.game.odds.position != 8:
            p = [526,397]
            dirty_rects.append(screen.blit(o, p))
            pygame.display.update(dirty_rects)
            return
    if num in [7,17,32,42]:
        if s.game.odds.position != 9:
            p = [578,397]
            dirty_rects.append(screen.blit(o, p))
            pygame.display.update(dirty_rects)
            return
    if num in [4,9,23,29,34,48]:
        if s.game.odds.position != 10:
            p = [631,397]
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
        dirty_rects.append(screen.blit(bg_gi, (203,768), pygame.Rect(203,768,58,56)))
    if 5 not in s.holes:
        dirty_rects.append(screen.blit(bg_gi, (398,836), pygame.Rect(398,836,58,56)))
    if 15 not in s.holes:
        dirty_rects.append(screen.blit(bg_gi, (269,575), pygame.Rect(269,575,58,56)))
    if 16 not in s.holes:
        dirty_rects.append(screen.blit(bg_gi, (333,704), pygame.Rect(333,704,58,56)))
    if 17 not in s.holes:
        dirty_rects.append(screen.blit(bg_gi, (466,641), pygame.Rect(466,641,58,56)))
    if s.game.corners.status == False:
        dirty_rects.append(screen.blit(bg_gi, (568,555), pygame.Rect(568,555,100,83)))
    if s.game.super_card.position < 4:
        dirty_rects.append(screen.blit(bg_gi, (47,719), pygame.Rect(47,719,112,31)))
    if s.game.super_card.position < 8:
        dirty_rects.append(screen.blit(bg_gi, (564,719), pygame.Rect(564,719,112,31)))
    if s.game.red_star.status == False:
        dirty_rects.append(screen.blit(bg_gi, (72,884), pygame.Rect(72,884,62,64)))
    if s.game.yellow_star.status == False:
        dirty_rects.append(screen.blit(bg_gi, (586,884), pygame.Rect(586,884,62,64)))

    pygame.display.update(dirty_rects)


def draw_feature_animation(s, num):
    global screen
    dirty_rects = []


    if num in [2,8,18,20,27,33,43,45]:
        if 2 not in s.holes:
            p = [203,768]
            dirty_rects.append(screen.blit(number, p))
            pygame.display.update(dirty_rects)
            return
    if num in [5,10,16,22,30,35,41,47]:
        if 5 not in s.holes:
            p = [398,836]
            dirty_rects.append(screen.blit(number, p))
            pygame.display.update(dirty_rects)
            return
    if num in [6,12,15,23,31,37,40,48]:
        if 15 not in s.holes:
            p = [269,575]
            dirty_rects.append(screen.blit(number, p))
            pygame.display.update(dirty_rects)
            return
    if num in [1,4,11,14,24,26,29,36,39,49]:
        if 16 not in s.holes:
            p = [333,704]
            dirty_rects.append(screen.blit(number, p))
            pygame.display.update(dirty_rects)
            return
    if num in [9,17,21,34,42,46]:
        if 17 not in s.holes:
            p = [466,641]
            dirty_rects.append(screen.blit(number, p))
            pygame.display.update(dirty_rects)
            return
    if num in [7,32,16,41]:
        if s.game.corners.status == False:
            p = [568,555]
            dirty_rects.append(screen.blit(c, p))
            pygame.display.update(dirty_rects)
            return
    if num in [13,38,18,43]:
        if s.game.super_card.position < 4:
            p = [47,719]
            dirty_rects.append(screen.blit(sc, p))
            pygame.display.update(dirty_rects)
            return
    if num in [19,44,12,37]:
        if s.game.super_card.position < 8:
            p = [564,719]
            dirty_rects.append(screen.blit(sc, p))
            pygame.display.update(dirty_rects)
            return
    if num in [25,0,4,29]:
        if s.game.yellow_star.status == False:
            p = [586,884]
            dirty_rects.append(screen.blit(star, p))
            s.game.coils.redROLamp.pulse(85)
            pygame.display.update(dirty_rects)
            return
    if num in [3,28,1,26]:
        if s.game.red_star.status == False:
            p = [72,884]
            dirty_rects.append(screen.blit(star, p))
            s.game.coils.yellowROLamp.pulse(85)
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

