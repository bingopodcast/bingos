import pygame
import random

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

meter = pygame.image.load('graphics/assets/silver_register_cover.png').convert()
eb = pygame.image.load('serenade/assets/eb_arrow.png').convert_alpha()
extra_ball = pygame.image.load('serenade/assets/eb.png').convert_alpha()
extra_balls = pygame.image.load('serenade/assets/extra_ball.png').convert_alpha()
o1 = pygame.image.load('serenade/assets/odds1.png').convert_alpha()
o2 = pygame.image.load('serenade/assets/odds2.png').convert_alpha()
o3 = pygame.image.load('serenade/assets/odds3.png').convert_alpha()
o4 = pygame.image.load('serenade/assets/odds4.png').convert_alpha()
o5 = pygame.image.load('serenade/assets/odds5.png').convert_alpha()
o6 = pygame.image.load('serenade/assets/odds6.png').convert_alpha()
o7 = pygame.image.load('serenade/assets/odds7.png').convert_alpha()
o8 = pygame.image.load('serenade/assets/odds8.png').convert_alpha()
star = pygame.image.load('serenade/assets/rollover.png').convert_alpha()
number = pygame.image.load('serenade/assets/number.png').convert_alpha()
tilt = pygame.image.load('serenade/assets/tilt.png').convert_alpha()
select_now = pygame.image.load('serenade/assets/select_now.png').convert_alpha()
sf_arrow = pygame.image.load('serenade/assets/sf_arrow.png').convert_alpha()
before_fourth = pygame.image.load('serenade/assets/time.png').convert_alpha()
s_number = pygame.image.load('serenade/assets/selected.png').convert_alpha()
s_arrow = pygame.image.load('serenade/assets/s_arrow.png').convert_alpha()
corners1 = pygame.image.load('serenade/assets/corners.png').convert_alpha()
corners2 = pygame.image.load('serenade/assets/corners.png').convert_alpha()
letter0 = pygame.image.load('serenade/assets/letter0.png').convert_alpha()
letter1 = pygame.image.load('serenade/assets/letter1.png').convert_alpha()
letter2 = pygame.image.load('serenade/assets/letter2.png').convert_alpha()
letter3 = pygame.image.load('serenade/assets/letter3.png').convert_alpha()
letter4 = pygame.image.load('serenade/assets/letter4.png').convert_alpha()
letter5 = pygame.image.load('serenade/assets/letter5.png').convert_alpha()
letter6 = pygame.image.load('serenade/assets/letter6.png').convert_alpha()
letter7 = pygame.image.load('serenade/assets/letter7.png').convert_alpha()
lite_a_name = pygame.image.load('serenade/assets/lite_a_name.png').convert_alpha()
select_card = pygame.image.load('serenade/assets/select_card.png').convert_alpha()
selected_card = pygame.image.load('serenade/assets/selected_card.png').convert_alpha()
bg_menu = pygame.image.load('serenade/assets/serenade_menu.png')
bg_gi = pygame.image.load('serenade/assets/serenade_gi.png')
bg_off = pygame.image.load('serenade/assets/serenade_off.png')

class scorereel():
    """ Score Reels are used to count replays """
    def __init__(self, pos, image):
        self.position = pos
        self.default_y = self.position[1]
        self.image = pygame.image.load(image).convert()

reel1 = scorereel([112,840], "graphics/assets/white_reel.png")
reel10 = scorereel([93,840], "graphics/assets/white_reel.png")
reel100 = scorereel([74,840], "graphics/assets/white_reel.png")

def display(s, replays=0, menu=False):
    
    meter.set_colorkey((255,0,252))
    meter_position = [65,840]

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

    if s.game.tilt.status == True:
        p = [183,251]
        screen.blit(letter0, p)
        p = [232,240]
        screen.blit(letter1, p)
        p = [281,239]
        screen.blit(letter2, p)
        p = [327,244]
        screen.blit(letter3, p)
        p = [374,245]
        screen.blit(letter4, p)
        p = [420,239]
        screen.blit(letter5, p)
        p = [464,241]
        screen.blit(letter6, p)
        p = [509,249]
        screen.blit(letter7, p)
    else:
        if s.game.lite_a_name.status == True:
            p = [572,232]
            screen.blit(lite_a_name, p)

        p = [183,251]
        screen.blit(letter0, p)

        if s.game.name.position >= 1:
            p = [232,240]
            screen.blit(letter1, p)
        if s.game.name.position >= 2:
            p = [281,239]
            screen.blit(letter2, p)
        if s.game.name.position >= 3:
            p = [327,244]
            screen.blit(letter3, p)
        if s.game.name.position >= 4:
            p = [374,245]
            screen.blit(letter4, p)
        if s.game.name.position >= 5:
            p = [420,239]
            screen.blit(letter5, p)
        if s.game.name.position >= 6:
            p = [464,241]
            screen.blit(letter6, p)
        if s.game.name.position >= 7:
            p = [509,249]
            screen.blit(letter7, p)

    if s.game.extra_ball.position == 1:
        eb_position = [96,987]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 2:
        eb_position = [132,987]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 3:
        eb_position = [169,987]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 4:
        eb_position = [204,986]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 5:
        eb_position = [239,986]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 6:
        eb_position = [277,987]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 7:
        eb_position = [312,987]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 8:
        eb_position = [347,987]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 9:
        eb_position = [381,987]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 10:
        eb_position = [416,987]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 11:
        eb_position = [456,987]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 12:
        eb_position = [490,987]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 13:
        eb_position = [524,987]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 14:
        eb_position = [561,987]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 15:
        eb_position = [597,987]
        screen.blit(eb, eb_position)

    if s.game.extra_ball.position >= 5 and s.game.extra_ball.position < 10:
        eb_pos = [107,1013]
        screen.blit(extra_balls, eb_pos)
    if s.game.extra_ball.position >= 10 and s.game.extra_ball.position < 15:
        eb_pos = [281,1013]
        screen.blit(extra_balls, eb_pos)
    if s.game.extra_ball.position == 15:
        eb_pos = [459,1013]
        screen.blit(extra_balls, eb_pos)

    if s.game.odds.position > 0:
        if s.game.odds.position == 1:
            odds_position = [188,741]
            screen.blit(o1, odds_position)
        if s.game.odds.position == 2:
            odds_position = [293,763]
            screen.blit(o2, odds_position)
        if s.game.odds.position == 3:
            odds_position = [431,759]
            screen.blit(o3, odds_position)
        if s.game.odds.position == 4:
            odds_position = [552,741]
            screen.blit(o4, odds_position)
        if s.game.odds.position == 5:
            odds_position = [265,851]
            screen.blit(o5, odds_position)
        if s.game.odds.position == 6:
            odds_position = [322,867]
            screen.blit(o6, odds_position)
        if s.game.odds.position == 7:
            odds_position = [467,853]
            screen.blit(o7, odds_position)
        if s.game.odds.position == 8:
            odds_position = [581,854]
            screen.blit(o8, odds_position)

    if s.game.red_star.status == True:
        rs_position = [646,980]
        screen.blit(star, rs_position)

    if s.game.corners1.status == True or s.game.corners2.status == True:
        corners_position = [312,558]
        screen.blit(corners1, corners_position)

    if s.game.tilt.status == False:
        if s.holes:
            if 1 in s.holes:
                p = [15,488]
                screen.blit(number, p)
                p = [667,433]
                screen.blit(number, p)
            if 2 in s.holes:
                p = [13,431]
                screen.blit(number, p)
                p = [612,319]
                screen.blit(number, p)
            if 3 in s.holes:
                p = [248,547]
                screen.blit(number, p)
                p = [605,547]
                screen.blit(number, p)
            if 4 in s.holes:
                p = [69,315]
                screen.blit(number, p)
                p = [492,491]
                screen.blit(number, p)
            if 5 in s.holes:
                p = [134,547]
                screen.blit(number, p)
                p = [607,491]
                screen.blit(number, p)
            if 6 in s.holes:
                p = [246,318]
                screen.blit(number, p)
                p = [610,376]
                screen.blit(number, p)
            if 7 in s.holes:
                p = [76,547]
                screen.blit(number, p)
                p = [496,376]
                screen.blit(number, p)
            if 8 in s.holes:
                p = [245,375]
                screen.blit(number, p)
                p = [495,434]
                screen.blit(number, p)
            if 9 in s.holes:
                p = [10,316]
                screen.blit(number, p)
                p = [665,490]
                screen.blit(number, p)
            if 10 in s.holes:
                p = [12,373]
                screen.blit(number, p)
                p = [551,433]
                screen.blit(number, p)
            if 11 in s.holes:
                p = [17,546]
                screen.blit(number, p)
                p = [554,318]
                screen.blit(number, p)
            if 12 in s.holes:
                p = [188,434]
                screen.blit(number, p)
                p = [553,376]
                screen.blit(number, p)
            if 13 in s.holes:
                p = [132,490]
                screen.blit(number, p)
                p = [550,491]
                screen.blit(number, p)
            if 14 in s.holes:
                p = [129,375]
                screen.blit(number, p)
                p = [610,434]
                screen.blit(number, p)
            if 15 in s.holes:
                p = [127,316]
                screen.blit(number, p)
                p = [435,547]
                screen.blit(number, p)
            if 16 in s.holes:
                p = [132,433]
                screen.blit(number, p)
                p = [438,377]
                screen.blit(number, p)
            if 17 in s.holes:
                p = [247,491]
                screen.blit(number, p)
                p = [438,319]
                screen.blit(number, p)
            if 18 in s.holes:
                p = [72,433]
                screen.blit(number, p)
                p = [669,378]
                screen.blit(number, p)
            if 19 in s.holes:
                p = [70,375]
                screen.blit(number, p)
                p = [491,549]
                screen.blit(number, p)
            if 20 in s.holes:
                p = [188,376]
                screen.blit(number, p)
                p = [671,319]
                screen.blit(number, p)
            if 21 in s.holes:
                p = [190,489]
                screen.blit(number, p)
                p = [548,549]
                screen.blit(number, p)
            if 22 in s.holes:
                p = [74,489]
                screen.blit(number, p)
                p = [496,318]
                screen.blit(number, p)
            if 23 in s.holes:
                p = [192,547]
                screen.blit(number, p)
                p = [663,548]
                screen.blit(number, p)
            if 24 in s.holes:
                p = [187,317]
                screen.blit(number, p)
                p = [437,435]
                screen.blit(number, p)
            if 25 in s.holes:
                p = [247,435]
                screen.blit(number, p)
                p = [436,492]
                screen.blit(number, p)

    if s.game.e_card.status == True:
        p = [305,311]
        screen.blit(select_card, p)
        if s.game.selector.position == 1:
            p = [302,428]
            screen.blit(selected_card, p)
        else:
            p = [368,428]
            screen.blit(selected_card, p)

    if s.game.tilt.status == True:
        tilt_position = [220,675]
        screen.blit(tilt, tilt_position)

    if s.game.selection_feature.position >= 1:
        if s.game.spotted.position == 0:
            p = [278,690]
            screen.blit(s_arrow, p)
        elif s.game.spotted.position == 1:
            p = [324,690]
            screen.blit(s_arrow, p)
        elif s.game.spotted.position == 2:
            p = [370,690]
            screen.blit(s_arrow, p)
        elif s.game.spotted.position == 3:
            p = [419,692]
            screen.blit(s_arrow, p)
        elif s.game.spotted.position == 4:
            p = [466,692]
            screen.blit(s_arrow, p)
        elif s.game.spotted.position == 5:
            p = [515,692]
            screen.blit(s_arrow, p)
        elif s.game.spotted.position == 6:
            p = [563,692]
            screen.blit(s_arrow, p)

    if s.game.selection_feature.position == 1:
        p = [132,628]
        screen.blit(sf_arrow, p)
    if s.game.selection_feature.position == 2:
        p = [179,628]
        screen.blit(sf_arrow, p)
    if s.game.selection_feature.position == 3:
        p = [230,628]
        screen.blit(sf_arrow, p)
    if s.game.selection_feature.position >= 4:
        p = [274,610]
        screen.blit(s_number, p)
    if s.game.selection_feature.position >= 5:
        p = [322,610]
        screen.blit(s_number, p)
    if s.game.selection_feature.position >= 6:
        p = [370,610]
        screen.blit(s_number, p)
    if s.game.selection_feature.position >= 7:
        p = [418,610]
        screen.blit(s_number, p)
    if s.game.selection_feature.position >= 8:
        p = [466,610]
        screen.blit(s_number, p)
    if s.game.selection_feature.position >= 9:
        p = [515,610]
        screen.blit(s_number, p)
    if s.game.selection_feature.position >= 10:
        p = [563,610]
        screen.blit(s_number, p)

    if (s.game.select_spots.status == True or s.game.selection_feature_relay.status == True or s.game.e_card.status == True):
        if s.game.before_fourth.status == True:
            if s.game.ball_count.position == 3:
                s.cancel_delayed(name="blink")
                blink([s,1,1])
            else:
                s.cancel_delayed(name="blink")

    if (s.game.select_spots.status == True or s.game.selection_feature_relay.status == True or s.game.e_card.status == True):
        if s.game.before_fifth.status == True:
            if s.game.ball_count.position == 4:
                s.cancel_delayed(name="blink")
                blink([s,1,1])
            else:
                s.cancel_delayed(name="blink")

    if s.game.before_fourth.status == True and (s.game.selection_feature.position > 3):
        p = [12,610]
        screen.blit(before_fourth, p)
    if s.game.before_fifth.status == True and (s.game.selection_feature.position > 3):
        p = [613,612]
        screen.blit(before_fourth, p)

    if s.game.eb_play.status == True:
        p = [20,981]
        screen.blit(extra_ball, p)

    pygame.display.update()

def blink(args):
    dirty_rects = []
    s = args[0]
    b = args[1]
    sn = args[2]

    if b == 0:
        if sn == 1:
            p = [315,500]
            dirty_rects.append(screen.blit(select_now, p))
        pygame.display.update(dirty_rects)
    else:
        dirty_rects.append(screen.blit(bg_gi, (315,500), pygame.Rect(315,500,105,58)))
        pygame.display.update(dirty_rects)
    b = not b

    args = [s,b,sn]

    s.delay(name="blink", delay=0.1, handler=blink, param=args)

def eb_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]
    if s.game.extra_ball.position < 5:
        dirty_rects.append(screen.blit(bg_gi, (107,1013), pygame.Rect(107,1013,166,32)))
    if s.game.extra_ball.position < 10:
        dirty_rects.append(screen.blit(bg_gi, (281,1013), pygame.Rect(281,1013,166,32)))
    if s.game.extra_ball.position < 15:
        dirty_rects.append(screen.blit(bg_gi, (459,1013), pygame.Rect(459,1013,166,32)))
        dirty_rects.append(screen.blit(bg_gi, (597,987), pygame.Rect(597,987,78,53)))
    pygame.display.update(dirty_rects)

    if num in [0,1,6,7,12,13,18,19,26,27,32,33,38,39,44,45]:
        if s.game.extra_ball.position < 5:
            p = [107,1013]
            dirty_rects.append(screen.blit(extra_balls, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [2,3,8,9,14,15,20,21,28,29,34,35,40,41,46,47]:
        if s.game.extra_ball.position < 10:
            p = [281,1013]
            dirty_rects.append(screen.blit(extra_balls, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [4,5,10,11,16,17,22,23,24,30,31,36,37,42,43,48,49,50]:
        if s.game.extra_ball.position < 15:
            p = [459,1013]
            dirty_rects.append(screen.blit(extra_balls, p))
            p = [597,987]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return

def clear_odds(s, num):
    global screen
    dirty_rects = []
    if s.game.odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (188,741), pygame.Rect(188,741,32,85)))
    if s.game.odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (293,763), pygame.Rect(293,763,51,80)))
    if s.game.odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (431,759), pygame.Rect(431,759,58,80)))
    if s.game.odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (552,741), pygame.Rect(552,741,40,87)))
    if s.game.odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (265,851), pygame.Rect(265,851,43,86)))
    if s.game.odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (322,867), pygame.Rect(322,867,48,89)))
    if s.game.odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (467,853), pygame.Rect(467,853,50,84)))
    if s.game.odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (581,854), pygame.Rect(581,854,55,87)))

    pygame.display.update(dirty_rects)

def draw_odds_animation(s, num):
    global screen
    dirty_rects = []
    if num in [0,1,40,14,24,25]:
        if s.game.odds.position != 1:
            p = [188,741]
            dirty_rects.append(screen.blit(o1, p))
            pygame.display.update(dirty_rects)
            return
    if num in [2,3,41,15,26,27]:
        if s.game.odds.position != 2:
            p = [293,763]
            dirty_rects.append(screen.blit(o2, p))
            pygame.display.update(dirty_rects)
            return
    if num in [4,5,42,16,28,29]:
        if s.game.odds.position != 3:
            p = [431,759]
            dirty_rects.append(screen.blit(o3, p))
            pygame.display.update(dirty_rects)
            return
    if num in [6,7,43,17,30,31]:
        if s.game.odds.position != 4:
            p = [552,741]
            dirty_rects.append(screen.blit(o4, p))
            pygame.display.update(dirty_rects)
            return
    if num in [8,9,44,18,32,33]:
        if s.game.odds.position != 5:
            p = [265,851]
            dirty_rects.append(screen.blit(o5, p))
            pygame.display.update(dirty_rects)
            return
    if num in [10,11,45,19,34,35]:
        if s.game.odds.position != 6:
            p = [322,867]
            dirty_rects.append(screen.blit(o6, p))
            pygame.display.update(dirty_rects)
            return
    if num in [12,13,46,47,20,21,36,37]:
        if s.game.odds.position != 7:
            p = [467,853]
            dirty_rects.append(screen.blit(o7, p))
            pygame.display.update(dirty_rects)
            return
    if num in [14,48,49,22,23,38]:
        if s.game.odds.position != 8:
            p = [581,854]
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

    if s.game.lite_a_name.status == False:
        dirty_rects.append(screen.blit(bg_gi, (572,232), pygame.Rect(572,232,112,79)))
    if s.game.corners1.status == False:
        dirty_rects.append(screen.blit(bg_gi, (312,558), pygame.Rect(312,558,107,49)))
    if s.game.e_card.status == False:
        dirty_rects.append(screen.blit(bg_gi, (305,311), pygame.Rect(305,311,122,112)))
    if s.game.red_star.status == False:
        dirty_rects.append(screen.blit(bg_gi, (646,980), pygame.Rect(646,980,62,60)))
    if s.game.selection_feature.position < 6:
        dirty_rects.append(screen.blit(bg_gi, (370,610), pygame.Rect(370,610,45,98)))
    if s.game.selection_feature.position < 7:
        dirty_rects.append(screen.blit(bg_gi, (418,610), pygame.Rect(418,610,45,98)))
    if s.game.selection_feature.position < 8:
        dirty_rects.append(screen.blit(bg_gi, (466,610), pygame.Rect(466,610,45,98)))
    if s.game.selection_feature.position < 9:
        dirty_rects.append(screen.blit(bg_gi, (515,610), pygame.Rect(515,610,45,98)))
    if s.game.selection_feature.position < 10:
        dirty_rects.append(screen.blit(bg_gi, (563,610), pygame.Rect(563,610,45,98)))
    if s.game.selection_feature.position !=  1:
        dirty_rects.append(screen.blit(bg_gi, (132,628), pygame.Rect(132,628,40,39)))
    if s.game.selection_feature.position !=  2:
        dirty_rects.append(screen.blit(bg_gi, (179,628), pygame.Rect(179,628,40,39)))
    if s.game.selection_feature.position !=  3:
        dirty_rects.append(screen.blit(bg_gi, (230,628), pygame.Rect(230,628,40,39)))
    pygame.display.update(dirty_rects)


def draw_feature_animation(s, num):
    global screen
    dirty_rects = []
   
    if num in [11,12,36,37]:
        if s.game.red_star.status == False:
            p = [646,980]
            dirty_rects.append(screen.blit(star, p))
            s.game.coils.redROLamp.pulse(85)
            s.game.coils.yellowROLamp.pulse(85)
            pygame.display.update(dirty_rects)
            return
    if num in [9,10,34,35]:
        if s.game.e_card.status == False:
            p = [305,311]
            dirty_rects.append(screen.blit(select_card, p))
            pygame.display.update(dirty_rects)
            return
    if num in [7,8,32,33]:
        if s.game.lite_a_name.status == False:
            p = [572,232]
            dirty_rects.append(screen.blit(lite_a_name, p))
            pygame.display.update(dirty_rects)
            return
    if num in [5,6,30,31]:
        if s.game.selection_feature.position < 6:
            p = [370,610]
            dirty_rects.append(screen.blit(s_number, p))
            pygame.display.update(dirty_rects)
            return
    if num in [3,4,28,29]:
        if s.game.selection_feature.position < 8:
            p = [466,610]
            dirty_rects.append(screen.blit(s_number, p))
            pygame.display.update(dirty_rects)
            return
    if num in [1,2,26,27]:
        if s.game.selection_feature.position < 9:
            p = [515,610]
            dirty_rects.append(screen.blit(s_number, p))
            pygame.display.update(dirty_rects)
            return
    if num in [0,49,24,25]:
        if s.game.selection_feature.position < 10:
            p = [563,610]
            dirty_rects.append(screen.blit(s_number, p))
            pygame.display.update(dirty_rects)
            return
    if num in [47,48,22,23]:
        if s.game.selection_feature.position < 7:
            p = [418,610]
            dirty_rects.append(screen.blit(s_number, p))
            pygame.display.update(dirty_rects)
            return
    if num in [45,46,20,21]:
        if s.game.selection_feature.position != 3:
            p = [230,628]
            dirty_rects.append(screen.blit(sf_arrow, p))
            pygame.display.update(dirty_rects)
            return
    if num in [43,44,18,19]:
        if s.game.selection_feature.position != 2:
            p = [179,628]
            dirty_rects.append(screen.blit(sf_arrow, p))
            pygame.display.update(dirty_rects)
            return
    if num in [41,42,16,17]:
        if s.game.selection_feature.position != 1:
            p = [132,628]
            dirty_rects.append(screen.blit(sf_arrow, p))
            pygame.display.update(dirty_rects)
            return
    if num in [39,40,14,15]:
        if s.game.corners1.status == False:
            p = [312,558]
            dirty_rects.append(screen.blit(corners1, p))
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

