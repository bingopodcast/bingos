
import pygame
import random

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

meter = pygame.image.load('graphics/assets/register_cover.png').convert()
c = pygame.image.load('beach_beauty/assets/corners.png').convert_alpha()
eb = pygame.image.load('beach_beauty/assets/eb.png').convert_alpha()
number_eb = pygame.image.load('beach_beauty/assets/eb_number.png').convert_alpha()
ebs = pygame.image.load('beach_beauty/assets/extra_balls.png').convert_alpha()
number = pygame.image.load('beach_beauty/assets/number.png').convert_alpha()
sc_number = pygame.image.load('beach_beauty/assets/sc_number.png').convert_alpha()
sc_arrow = pygame.image.load('beach_beauty/assets/sc_arrow.png').convert_alpha()
sc = pygame.image.load('beach_beauty/assets/sc.png').convert_alpha()
super_card = pygame.image.load('beach_beauty/assets/super_card.png').convert_alpha()
o1 = pygame.image.load('beach_beauty/assets/odds1.png').convert_alpha()
o2 = pygame.image.load('beach_beauty/assets/odds2.png').convert_alpha()
o3 = pygame.image.load('beach_beauty/assets/odds3.png').convert_alpha()
o4 = pygame.image.load('beach_beauty/assets/odds4.png').convert_alpha()
o5 = pygame.image.load('beach_beauty/assets/odds5.png').convert_alpha()
o6 = pygame.image.load('beach_beauty/assets/odds6.png').convert_alpha()
o7 = pygame.image.load('beach_beauty/assets/odds7.png').convert_alpha()
o8 = pygame.image.load('beach_beauty/assets/odds8.png').convert_alpha()
o9 = pygame.image.load('beach_beauty/assets/odds9.png').convert_alpha()
select_number = pygame.image.load('beach_beauty/assets/select_number.png').convert_alpha()
select_now = pygame.image.load('beach_beauty/assets/select_now.png').convert_alpha()
tilt = pygame.image.load('beach_beauty/assets/tilt.png').convert_alpha()
wpa = pygame.image.load('beach_beauty/assets/wp_arrow.png').convert_alpha()
wa = pygame.image.load('beach_beauty/assets/wild_arrow.png').convert_alpha()
select_number = pygame.image.load('beach_beauty/assets/select_number.png').convert_alpha()
select_now = pygame.image.load('beach_beauty/assets/select_now.png').convert_alpha()
wild_pocket = pygame.image.load('beach_beauty/assets/wild_pocket.png').convert_alpha()
bg_menu = pygame.image.load('beach_beauty/assets/beach_beauty_menu.png')
bg_gi = pygame.image.load('beach_beauty/assets/beach_beauty_gi.png')
bg_off = pygame.image.load('beach_beauty/assets/beach_beauty_off.png')

class scorereel():
    """ Score Reels are used to count replays """
    def __init__(self, pos, image):
        self.position = pos
        self.default_y = self.position[1]
        self.image = pygame.image.load(image).convert()

reel1 = scorereel([107,312], "graphics/assets/green_reel.png")
reel10 = scorereel([88,312], "graphics/assets/green_reel.png")
reel100 = scorereel([70,312], "graphics/assets/green_reel.png")

def display(s, replays=0, menu=False):
    
    meter.set_colorkey((255,0,252))
    meter_position = [60,312]

    screen.blit(reel1.image, reel1.position)
    screen.blit(reel10.image, reel10.position)
    screen.blit(reel100.image, reel100.position)
    screen.blit(meter, meter_position)


    backglass_position = [0, 0]
    backglass = pygame.Surface(screen.get_size(), flags=pygame.SRCALPHA)
    backglass.set_colorkey((255,0,252))
    backglass.fill((0, 0, 0))
    if menu == True:
        screen.blit(bg_menu, backglass_position)
    else:
        if (s.game.anti_cheat.status == True):
            screen.blit(bg_gi, backglass_position)
        else:
            screen.blit(bg_off, backglass_position)

    if s.game.extra_ball.position >= 1:
        eb_position = [140,1004]
        screen.blit(number_eb, eb_position)
    if s.game.extra_ball.position >= 2:
        eb_position = [190,1004]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 3:
        eb_position = [256,1004]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 4:
        eb_position = [326,1004]
        screen.blit(number_eb, eb_position)
    if s.game.extra_ball.position >= 5:
        eb_position = [370,1004]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 6:
        eb_position = [437,1004]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 7:
        eb_position = [510,1004]
        screen.blit(number_eb, eb_position)
    if s.game.extra_ball.position >= 8:
        eb_position = [560,1004]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 9:
        eb_position = [628,1004]
        screen.blit(eb, eb_position)
   
    if s.game.odds.position > 0:
        if s.game.odds.position == 1:
            odds_position = [24,816]
            screen.blit(o1, odds_position)
        if s.game.odds.position == 2:
            odds_position = [99,824]
            screen.blit(o2, odds_position)
        if s.game.odds.position == 3:
            odds_position = [188,834]
            screen.blit(o3, odds_position)
        if s.game.odds.position == 4:
            odds_position = [238,804]
            screen.blit(o4, odds_position)
        if s.game.odds.position == 5:
            odds_position = [289,802]
            screen.blit(o5, odds_position)
        if s.game.odds.position == 6:
            odds_position = [348,830]
            screen.blit(o6, odds_position)
        if s.game.odds.position == 7:
            odds_position = [379,811]
            screen.blit(o7, odds_position)
        if s.game.odds.position == 8:
            odds_position = [467,816]
            screen.blit(o8, odds_position)
        if s.game.odds.position == 9:
            odds_position = [503,814]
            screen.blit(o9, odds_position)

    if s.game.tilt.status == False:
        if s.holes:
            if 1 in s.holes:
                number_position = [448,402]
                screen.blit(number, number_position)
                p = [544,532]
                screen.blit(sc_number, p)
            if 2 in s.holes:
                number_position = [222,458]
                screen.blit(number, number_position)
            if 3 in s.holes:
                number_position = [448,346]
                screen.blit(number, number_position)
                p = [592,484]
                screen.blit(sc_number, p)
            if 4 in s.holes:
                number_position = [335,513]
                screen.blit(number, number_position)
            if 5 in s.holes:
                number_position = [335,569]
                screen.blit(number, number_position)
                p = [592,580]
                screen.blit(sc_number, p)
            if 6 in s.holes:
                number_position = [448,570]
                screen.blit(number, number_position)
            if 7 in s.holes:
                number_position = [280,570]
                screen.blit(number, number_position)
            if 8 in s.holes:
                number_position = [224,514]
                screen.blit(number, number_position)
                p = [642,532]
                screen.blit(sc_number, p)
            if 9 in s.holes:
                number_position = [223,346]
                screen.blit(number, number_position)
            if 10 in s.holes:
                number_position = [224,402]
                screen.blit(number, number_position)
                p = [84,483]
                screen.blit(sc_number, p)
            if 11 in s.holes:
                number_position = [223,571]
                screen.blit(number, number_position)
                p = [544,581]
                screen.blit(sc_number, p)
            if 12 in s.holes:
                number_position = [392,458]
                screen.blit(number, number_position)
                p = [134,534]
                screen.blit(sc_number, p)
            if 13 in s.holes:
                number_position = [280,346]
                screen.blit(number, number_position)
            if 14 in s.holes:
                number_position = [336,402]
                screen.blit(number, number_position)
                p = [37,534]
                screen.blit(sc_number, p)
                p = [642,484]
                screen.blit(sc_number, p)
            if 15 in s.holes:
                number_position = [335,345]
                screen.blit(number, number_position)
                p = [35,483]
                screen.blit(sc_number, p)
            if 16 in s.holes:
                number_position = [335,458]
                screen.blit(number, number_position)
            if 17 in s.holes:
                number_position = [448,514]
                screen.blit(number, number_position)
                p = [134,582]
                screen.blit(sc_number, p)
            if 18 in s.holes:
                number_position = [280,458]
                screen.blit(number, number_position)
            if 19 in s.holes:
                number_position = [280,402]
                screen.blit(number, number_position)
                p = [132,484]
                screen.blit(sc_number, p)
            if 20 in s.holes:
                number_position = [392,401]
                screen.blit(number, number_position)
                p = [84,533]
                screen.blit(sc_number, p)
            if 21 in s.holes:
                number_position = [392,513]
                screen.blit(number, number_position)
            if 22 in s.holes:
                number_position = [279,515]
                screen.blit(number, number_position)
                p = [86,583]
                screen.blit(sc_number, p)
            if 23 in s.holes:
                number_position = [392,570]
                screen.blit(number, number_position)
                p = [641,580]
                screen.blit(sc_number, p)
            if 24 in s.holes:
                number_position = [392,345]
                screen.blit(number, number_position)
                p = [545,484]
                screen.blit(sc_number, p)
            if 25 in s.holes:
                number_position = [448,459]
                screen.blit(number, number_position)
                p = [37,583]
                screen.blit(sc_number, p)
                p = [593,533]
                screen.blit(sc_number, p)

    if s.game.super_card.position == 1:
        p = [27,659]
        screen.blit(sc_arrow, p)
    if s.game.super_card.position == 2:
        p = [60,659]
        screen.blit(sc_arrow, p)
    if s.game.super_card.position == 3:
        p = [95,659]
        screen.blit(sc_arrow, p)
    if s.game.super_card.position == 4:
        p = [127,659]
        screen.blit(sc_arrow, p)
    if s.game.super_card.position >= 5:
        p = [163,650]
        screen.blit(sc, p)
        p = [36,445]
        screen.blit(super_card, p)
    if s.game.super_card.position == 6:
        p = [257,659]
        screen.blit(sc_arrow, p)
    if s.game.super_card.position == 7:
        p = [290,659]
        screen.blit(sc_arrow, p)
    if s.game.super_card.position == 8:
        p = [324,659]
        screen.blit(sc_arrow, p)
    if s.game.super_card.position == 9:
        p = [360,659]
        screen.blit(sc_arrow, p)
    if s.game.super_card.position == 10:
        p = [394,648]
        screen.blit(sc, p)
        p = [545,446]
        screen.blit(super_card, p)

    if s.game.tilt.status == True:
        tilt_position = [52,267]
        screen.blit(tilt, tilt_position)

    if s.game.eb_play.status == True:
        ebs_position = [29,1004]
        screen.blit(ebs, ebs_position)

    if s.game.corners.status == True:
        p = [573,305]
        screen.blit(c, p)

    if s.game.wild_pockets.position == 1:
        p = [28,731]
        screen.blit(wpa, p)
    if s.game.wild_pockets.position == 2:
        p = [62,731]
        screen.blit(wpa, p)
    if s.game.wild_pockets.position == 3:
        p = [94,731]
        screen.blit(wpa, p)
    if s.game.wild_pockets.position == 4:
        p = [128,731]
        screen.blit(wpa, p)
    if s.game.wild_pockets.position == 5:
        p = [162,731]
        screen.blit(wpa, p)
    if s.game.wild_pockets.position >= 6:
        if s.game.one_two_three.status == True:
            p = [195,712]
            screen.blit(wa, p)
        else:
            p = [196,750]
            screen.blit(wa, p)
    if s.game.wild_pockets.position == 7:
        p = [253,731]
        screen.blit(wpa, p)
    if s.game.wild_pockets.position == 8:
        p = [286,731]
        screen.blit(wpa, p)
    if s.game.wild_pockets.position == 9:
        p = [320,731]
        screen.blit(wpa, p)
    if s.game.wild_pockets.position == 10:
        p = [355,731]
        screen.blit(wpa, p)
    if s.game.wild_pockets.position == 11:
        p = [388,731]
        screen.blit(wpa, p)
    if s.game.wild_pockets.position == 12:
        p = [424,722]
        screen.blit(select_number, p)
        if s.game.one_two_three.status == True:
            p = [545,644]
            screen.blit(wild_pocket, p)
        else:
            p = [545,743]
            screen.blit(wild_pocket, p)

    if s.game.ball_count.position >= 3:
        if s.game.pocket.status == True:
            s.cancel_delayed(name="blink")
            blink([s,1,1])
        else:
            s.cancel_delayed(name="blink")

    pygame.display.update()

def blink(args):
    dirty_rects = []
    s = args[0]
    b = args[1]
    sn = args[2]

    if b == 0:
        if sn == 1:
            p = [546,964]
            dirty_rects.append(screen.blit(select_now, p))
        pygame.display.update(dirty_rects)
    else:
        dirty_rects.append(screen.blit(bg_gi, (546,964), pygame.Rect(546,964,152,31)))
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
        dirty_rects.append(screen.blit(bg_gi, (140,1004), pygame.Rect(140,1004,48,35)))
    if s.game.extra_ball.position < 2:
        dirty_rects.append(screen.blit(bg_gi, (190,1004), pygame.Rect(190,1004,68,37)))
    if s.game.extra_ball.position < 3:
        dirty_rects.append(screen.blit(bg_gi, (256,1004), pygame.Rect(256,1004,68,37)))
    if s.game.extra_ball.position < 4:
        dirty_rects.append(screen.blit(bg_gi, (326,1004), pygame.Rect(326,1004,48,35)))
    if s.game.extra_ball.position < 5:
        dirty_rects.append(screen.blit(bg_gi, (370,1004), pygame.Rect(370,1004,68,37)))
    if s.game.extra_ball.position < 6:
        dirty_rects.append(screen.blit(bg_gi, (437,1004), pygame.Rect(437,1004,68,37)))
    if s.game.extra_ball.position < 7:
        dirty_rects.append(screen.blit(bg_gi, (510,1004), pygame.Rect(510,1004,48,35)))
    if s.game.extra_ball.position < 8:
        dirty_rects.append(screen.blit(bg_gi, (560,1004), pygame.Rect(560,1004,68,37)))
    if s.game.extra_ball.position < 9:
        dirty_rects.append(screen.blit(bg_gi, (628,1004), pygame.Rect(628,1004,68,37)))
    pygame.display.update(dirty_rects)

    if num in [0,25,14,49]:
        if s.game.extra_ball.position < 1:
            p = [140,1004]
            dirty_rects.append(screen.blit(number_eb, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [39,1,26,15]:
        if s.game.extra_ball.position < 2:
            p = [190,1004]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [3,4,17,28,29,40]:
        if s.game.extra_ball.position < 3:
            p = [256,1004]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [5,18,30,43]:
        if s.game.extra_ball.position < 4:
            p = [326,1004]
            dirty_rects.append(screen.blit(number_eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [7,8,19,32,33,44]:
        if s.game.extra_ball.position < 5:
            p = [370,1004]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [9,10,20,34,35,45]:
        if s.game.extra_ball.position < 6:
            p = [437,1004]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [11,21,36,46]:
        if s.game.extra_ball.position < 7:
            p = [510,1004]
            dirty_rects.append(screen.blit(number_eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [12,22,37,47]:
        if s.game.extra_ball.position < 8:
            p = [560,1004]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [2,6,13,16,23,27,31,38,41,48]:
        if s.game.extra_ball.position < 9:
            p = [628,1004]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return

def clear_odds(s, num):
    global screen

    dirty_rects = []

    if s.game.odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (24,816), pygame.Rect(24,816,28,126)))
    if s.game.odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (99,824), pygame.Rect(99,824,46,106)))
    if s.game.odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (188,834), pygame.Rect(188,834,31,100)))
    if s.game.odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (238,804), pygame.Rect(238,804,32,82)))
    if s.game.odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (289,802), pygame.Rect(289,802,31,83)))
    if s.game.odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (348,830), pygame.Rect(348,830,31,91)))
    if s.game.odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (379,811), pygame.Rect(379,811,49,91)))
    if s.game.odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (467,816), pygame.Rect(467,816,35,107)))
    if s.game.odds.position != 9:
        dirty_rects.append(screen.blit(bg_gi, (503,814), pygame.Rect(503,814,37,107)))
    
    pygame.display.update(dirty_rects)

def draw_odds_animation(s, num):
    global screen
    dirty_rects = []

    if num in [2,3,12,27,28,37]:
        if s.game.odds.position != 1:
            p = [24,816]
            dirty_rects.append(screen.blit(o1, p))
            pygame.display.update(dirty_rects)
            return
    if num in [13,14,38,39]:
        if s.game.odds.position != 2:
            p = [99,824]
            dirty_rects.append(screen.blit(o2, p))
            pygame.display.update(dirty_rects)
            return
    if num in [4,5,15,16,29,30,40,41]:
        if s.game.odds.position != 3:
            p = [188,834]
            dirty_rects.append(screen.blit(o3, p))
            pygame.display.update(dirty_rects)
            return
    if num in [17,18,42,43]:
        if s.game.odds.position != 4:
            p = [238,804]
            dirty_rects.append(screen.blit(o4, p))
            pygame.display.update(dirty_rects)
            return
    if num in [6,7,19,31,32,44]:
        if s.game.odds.position != 5:
            p = [289,802]
            dirty_rects.append(screen.blit(o5, p))
            pygame.display.update(dirty_rects)
            return
    if num in [20,21,45,46]:
        if s.game.odds.position != 6:
            p = [348,830]
            dirty_rects.append(screen.blit(o6, p))
            pygame.display.update(dirty_rects)
            return
    if num in [8,9,22,23,33,34,47,48]:
        if s.game.odds.position != 7:
            p = [379,811]
            dirty_rects.append(screen.blit(o7, p))
            pygame.display.update(dirty_rects)
            return
    if num in [0,25,50]:
        if s.game.odds.position != 8:
            p = [467,816]
            dirty_rects.append(screen.blit(o8, p))
            pygame.display.update(dirty_rects)
            return
    if num in [1,10,11,26,35,36]:
        if s.game.odds.position != 9:
            p = [503,814]
            dirty_rects.append(screen.blit(o9, p))
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
    if s.game.one_two_three.status == False:
        dirty_rects.append(screen.blit(bg_gi, (545,644), pygame.Rect(545,644,152,66)))
    else:
        dirty_rects.append(screen.blit(bg_gi, (545,743), pygame.Rect(545,743,152,66)))
    if s.game.wild_pockets.position < 12:
        dirty_rects.append(screen.blit(bg_gi, (424,722), pygame.Rect(424,722,89,54)))
    if s.game.super_card.position < 5:
        dirty_rects.append(screen.blit(bg_gi, (163,650), pygame.Rect(163,650,92,56)))
    if s.game.super_card.position < 10:
        dirty_rects.append(screen.blit(bg_gi, (394,648), pygame.Rect(394,648,92,56)))
    if s.game.corners.status == False:
        dirty_rects.append(screen.blit(bg_gi, (573,305), pygame.Rect(573,305,83,81)))

    pygame.display.update(dirty_rects)


def draw_feature_animation(s, num):
    global screen
    dirty_rects = []
 
    if num in [2,3,16,17,27,28,41,42]:
        if s.game.one_two_three.status == False:
            p = [545,644]
            dirty_rects.append(screen.blit(wild_pocket, p))
            pygame.display.update(dirty_rects)
            return
        else:
            p = [545,743]
            dirty_rects.append(screen.blit(wild_pocket, p))
            pygame.display.update(dirty_rects)
            return
    if num in [4,5,14,15,29,30,39,40]:
        if s.game.super_card.position < 5:
            p = [163,650]
            dirty_rects.append(screen.blit(sc, p))
            pygame.display.update(dirty_rects)
            return
    if num in [10,11,22,23,35,36,47,48]:
        if s.game.super_card.position < 10:
            p = [394,648]
            dirty_rects.append(screen.blit(sc, p))
            pygame.display.update(dirty_rects)
            return
    if num in [8,9,20,21,33,34,45,46]:
        if s.game.wild_pockets.position < 12:
            p = [424,722]
            dirty_rects.append(screen.blit(select_number, p))
            pygame.display.update(dirty_rects)
            return
    if num in [6,7,18,19,31,32,43,44]:
        if s.game.corners.status == False:
            p = [573,305]
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


