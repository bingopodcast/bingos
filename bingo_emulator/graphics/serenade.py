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
        backglass = pygame.image.load('serenade/assets/serenade_menu.png')
    else:
        if (s.game.anti_cheat.status == True):
            backglass = pygame.image.load('serenade/assets/serenade_gi.png')
        else:
            backglass = pygame.image.load('serenade/assets/serenade_off.png')
    backglass = pygame.transform.scale(backglass, (720, 1280))
    
    screen.blit(backglass, backglass_position)

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

    if (s.game.select_spots.status == True or s.game.selection_feature_relay.status == True or s.game.e_card.status == True) and s.game.before_fourth.status == True and s.game.ball_count.position == 3:
        p = [315,500]
        screen.blit(select_now, p)

    if (s.game.select_spots.status == True or s.game.selection_feature_relay.status == True or s.game.e_card.status == True) and s.game.before_fifth.status == True and s.game.ball_count.position == 4:
        p = [315,500]
        screen.blit(select_now, p)

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

def eb_animation(num):
    global screen

    if num == 9:
        eb_position = [96,987]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 8:
        eb_position = [132,987]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 7:
        eb_position = [169,987]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 6:
        eb_position = [204,986]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 5:
        eb_position = [239,986]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 4:
        eb_position = [277,987]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 3:
        eb_position = [312,987]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 2:
        eb_position = [347,987]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 1:
        eb_position = [381,987]
        screen.blit(eb, eb_position)
        pygame.display.update()


def feature_animation(num):
    global screen
    if num == 6:
        corners_position = [312,558]
        screen.blit(corners1, corners_position)
        pygame.display.update()

    if num == 5:
        rs_position = [646,979]
        screen.blit(star, rs_position)
        pygame.display.update()

    if num == 4:
        rs_position = [646,979]
        screen.blit(star, rs_position)
        pygame.display.update()

    if num == 3:
        p = [312,558]
        screen.blit(corners2, p)
        pygame.display.update()
    
    if num == 2:
        p = [312,558]
        screen.blit(corners1, p)
        pygame.display.update()
   
    if num == 1:
        p = [312,558]
        screen.blit(corners2, p)
        pygame.display.update()

def odds_animation(num):
    global screen

    if num == 5:
        odds_position = [188,741]
        screen.blit(o1, odds_position)
        pygame.display.update()
    if num == 4:
        odds_position = [293,763]
        screen.blit(o2, odds_position)
        pygame.display.update()
    if num == 3:
        odds_position = [431,759]
        screen.blit(o3, odds_position)
        pygame.display.update()
    if num == 2:
        odds_position = [552,741]
        screen.blit(o4, odds_position)
        pygame.display.update()
    if num == 1:
        odds_position = [265,851]
        screen.blit(o5, odds_position)
        pygame.display.update()
