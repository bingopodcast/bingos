
import pygame
import random

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

meter = pygame.image.load('graphics/assets/register_cover.png').convert()
card = pygame.image.load('bally_beauty/assets/card.png').convert_alpha()
super_score = pygame.image.load('bally_beauty/assets/super_score.png').convert_alpha()
number_eb = pygame.image.load('bally_beauty/assets/number_eb.png').convert_alpha()
eb = pygame.image.load('bally_beauty/assets/eb.png').convert_alpha()
o1 = pygame.image.load('bally_beauty/assets/odds1.png').convert_alpha()
o2 = pygame.image.load('bally_beauty/assets/odds2.png').convert_alpha()
o3 = pygame.image.load('bally_beauty/assets/odds3.png').convert_alpha()
o4 = pygame.image.load('bally_beauty/assets/odds4.png').convert_alpha()
o5 = pygame.image.load('bally_beauty/assets/odds5.png').convert_alpha()
trophy = pygame.image.load('bally_beauty/assets/trophy.png').convert_alpha()
c = pygame.image.load('bally_beauty/assets/corners.png').convert_alpha()
number = pygame.image.load('bally_beauty/assets/number.png').convert_alpha()
tilt = pygame.image.load('bally_beauty/assets/tilt.png').convert_alpha()
f = pygame.image.load('bally_beauty/assets/feature.png').convert_alpha()
ebs = pygame.image.load('bally_beauty/assets/extra_ball.png').convert_alpha()
red = pygame.image.load('bally_beauty/assets/red_number.png').convert_alpha()


class scorereel():
    """ Score Reels are used to count replays """
    def __init__(self, pos, image):
        self.position = pos
        self.default_y = self.position[1]
        self.image = pygame.image.load(image).convert()

reel1 = scorereel([622,268], "graphics/assets/green_reel.png")
reel10 = scorereel([603,268], "graphics/assets/green_reel.png")
reel100 = scorereel([584,268], "graphics/assets/green_reel.png")

def display(s, replays=0, menu=False):
    
    meter.set_colorkey((255,0,252))
    meter_position = [574,268]

    screen.blit(reel1.image, reel1.position)
    screen.blit(reel10.image, reel10.position)
    screen.blit(reel100.image, reel100.position)
    screen.blit(meter, meter_position)

    backglass_position = [0, 0]
    backglass = pygame.Surface(screen.get_size(), flags=pygame.SRCALPHA)
    backglass.fill((0, 0, 0))
    if menu == True:
        backglass = pygame.image.load('bally_beauty/assets/bally_beauty_menu.png')
    else:
        if (s.game.anti_cheat.status == True):
            backglass = pygame.image.load('bally_beauty/assets/bally_beauty_gi.png')
        else:
            backglass = pygame.image.load('bally_beauty/assets/bally_beauty_off.png')
    backglass = pygame.transform.scale(backglass, (720, 1280))
    
    screen.blit(backglass, backglass_position)

    if s.game.selector.position >= 1:
        p = [72,396]
        screen.blit(card, p)
    if s.game.selector.position >= 2:
        p = [300,276]
        screen.blit(card, p)
    if s.game.selector.position >= 3:
        p = [534,393]
        screen.blit(card, p)

    if s.game.super1.status == True:
        p = [52,432]
        screen.blit(super_score, p)
    if s.game.super2.status == True:
        p = [282,310]
        screen.blit(super_score, p)
    if s.game.super3.status == True:
        p = [513,429]
        screen.blit(super_score, p)

    if s.game.extra_ball.position >= 1:
        eb_position = [72,1056]
        screen.blit(number_eb, eb_position)
    if s.game.extra_ball.position >= 2:
        eb_position = [118,1058]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 3:
        eb_position = [184,1058]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 4:
        eb_position = [266,1058]
        screen.blit(number_eb, eb_position)
    if s.game.extra_ball.position >= 5:
        eb_position = [312,1060]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 6:
        eb_position = [380,1060]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 7:
        eb_position = [460,1058]
        screen.blit(number_eb, eb_position)
    if s.game.extra_ball.position >= 8:
        eb_position = [508,1056]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 9:
        eb_position = [576,1058]
        screen.blit(eb, eb_position)
    
    
    if s.game.odds.position > 0:
        if s.game.odds.position == 1:
            odds_position = [110,732]
            screen.blit(o1, odds_position)
        if s.game.odds.position == 2:
            odds_position = [215,732]
            screen.blit(o2, odds_position)
        if s.game.odds.position == 3:
            odds_position = [318,732]
            screen.blit(o3, odds_position)
        if s.game.odds.position == 4:
            odds_position = [420,732]
            screen.blit(o4, odds_position)
        if s.game.odds.position == 5:
            odds_position = [524,732]
            screen.blit(o5, odds_position)

    if s.game.red_star.status == True:
        rs_position = [24,855]
        screen.blit(trophy, rs_position)

    if s.game.yellow_star.status == True:
        ys_position = [624,856]
        screen.blit(trophy, ys_position)

    if s.game.corners.status == True:
        corners_position = [64,261]
        screen.blit(c, corners_position)

    if s.game.tilt.status == False:
        if s.holes:
            if 1 in s.holes:
                number_position = [69,480]
                screen.blit(number, number_position)
                number_position = [256,502]
                screen.blit(number, number_position)
                number_position = [616,672]
                screen.blit(number, number_position)
            if 2 in s.holes:
                number_position = [108,672]
                screen.blit(number, number_position)
                number_position = [258,453]
                screen.blit(number, number_position)
                number_position = [662,576]
                screen.blit(number, number_position)
            if 3 in s.holes:
                number_position = [195,478]
                screen.blit(number, number_position)
                number_position = [429,549]
                screen.blit(number, number_position)
                number_position = [490,526]
                screen.blit(number, number_position)
            if 4 in s.holes:
                number_position = [152,676]
                screen.blit(number, number_position)
                number_position = [388,359]
                screen.blit(number, number_position)
                number_position = [620,479]
                screen.blit(number, number_position)
            if 5 in s.holes:
                number_position = [31,481]
                screen.blit(number, number_position)
                number_position = [345,552]
                screen.blit(number, number_position)
                number_position = [661,676]
                screen.blit(number, number_position)
            if 6 in s.holes:
                number_position = [28,577]
                screen.blit(number, number_position)
                number_position = [430,359]
                screen.blit(number, number_position)
                number_position = [534,676]
                screen.blit(number, number_position)
            if 7 in s.holes:
                number_position = [197,529]
                screen.blit(number, number_position)
                number_position = [302,552]
                screen.blit(number, number_position)
                number_position = [534,480]
                screen.blit(number, number_position)
            if 8 in s.holes:
                number_position = [29,529]
                screen.blit(number, number_position)
                number_position = [430,504]
                screen.blit(number, number_position)
                number_position = [664,529]
                screen.blit(number, number_position)
            if 9 in s.holes:
                number_position = [114,481]
                screen.blit(number, number_position)
                number_position = [261,360]
                screen.blit(number, number_position)
                number_position = [662,481]
                screen.blit(number, number_position)
            if 10 in s.holes:
                number_position = [112,529]
                screen.blit(number, number_position)
                number_position = [258,553]
                screen.blit(number, number_position)
                number_position = [578,480]
                screen.blit(number, number_position)
            if 11 in s.holes:
                number_position = [154,578]
                screen.blit(number, number_position)
                number_position = [344,504]
                screen.blit(number, number_position)
                number_position = [620,577]
                screen.blit(number, number_position)
            if 12 in s.holes:
                number_position = [26,674]
                screen.blit(number, number_position)
                number_position = [387,454]
                screen.blit(number, number_position)
                number_position = [578,626]
                screen.blit(number, number_position)
            if 13 in s.holes:
                number_position = [195,626]
                screen.blit(number, number_position)
                number_position = [260,406]
                screen.blit(number, number_position)
                number_position = [492,627]
                screen.blit(number, number_position)
            if 14 in s.holes:
                number_position = [111,627]
                screen.blit(number, number_position)
                number_position = [345,406]
                screen.blit(number, number_position)
                number_position = [535,577]
                screen.blit(number, number_position)
            if 15 in s.holes:
                number_position = [195,675]
                screen.blit(number, number_position)
                number_position = [345,454]
                screen.blit(number, number_position)
                number_position = [491,578]
                screen.blit(number, number_position)
            if 16 in s.holes:
                number_position = [112,577]
                screen.blit(number, number_position)
                number_position = [346,358]
                screen.blit(number, number_position)
                number_position = [577,676]
                screen.blit(number, number_position)
            if 17 in s.holes:
                number_position = [196,577]
                screen.blit(number, number_position)
                number_position = [430,455]
                screen.blit(number, number_position)
                number_position = [578,577]
                screen.blit(number, number_position)
            if 18 in s.holes:
                number_position = [70,578]
                screen.blit(number, number_position)
                number_position = [302,455]
                screen.blit(number, number_position)
                number_position = [579,528]
                screen.blit(number, number_position)
            if 19 in s.holes:
                number_position = [154,529]
                screen.blit(number, number_position)
                number_position = [303,406]
                screen.blit(number, number_position)
                number_position = [620,625]
                screen.blit(number, number_position)
            if 20 in s.holes:
                number_position = [152,626]
                screen.blit(number, number_position)
                number_position = [388,406]
                screen.blit(number, number_position)
                number_position = [535,626]
                screen.blit(number, number_position)
            if 21 in s.holes:
                number_position = [69,626]
                screen.blit(number, number_position)
                number_position = [388,503]
                screen.blit(number, number_position)
                number_position = [536,528]
                screen.blit(number, number_position)
            if 22 in s.holes:
                number_position = [71,528]
                screen.blit(number, number_position)
                number_position = [302,503]
                screen.blit(number, number_position)
                number_position = [620,529]
                screen.blit(number, number_position)
            if 23 in s.holes:
                number_position = [68,675]
                screen.blit(number, number_position)
                number_position = [386,552]
                screen.blit(number, number_position)
                number_position = [662,627]
                screen.blit(number, number_position)
            if 24 in s.holes:
                number_position = [28,626]
                screen.blit(number, number_position)
                number_position = [304,358]
                screen.blit(number, number_position)
                number_position = [492,480]
                screen.blit(number, number_position)
            if 25 in s.holes:
                number_position = [155,481]
                screen.blit(number, number_position)
                number_position = [430,406]
                screen.blit(number, number_position)
                number_position = [492,675]
                screen.blit(number, number_position)

    if s.game.tilt.status == True:
        tilt_position = [16,184]
        screen.blit(tilt, tilt_position)

    if s.game.select_spots.status == True:
        f_position = [291,615]
        screen.blit(f, f_position)

    if s.game.select_spots.status == True and s.game.ball_count.position == 4:
        p = [291,672]
        screen.blit(f, p)

    if s.game.eb_play.status == True:
        ebs_position = [287,1028]
        screen.blit(ebs, ebs_position)

    if s.game.select_spots.status == True:
        if s.game.ball_count.position < 5:
            if s.game.spotted.position == 0:
                p = [153,526]
                screen.blit(red, p)
                p = [303,405]
                screen.blit(red, p)
                p = [620,624]
                screen.blit(red, p)
            elif s.game.spotted.position == 1:
                p = [152,624]
                screen.blit(red, p)
                p = [386,404]
                screen.blit(red, p)
                p = [534,626]
                screen.blit(red, p)
            elif s.game.spotted.position == 2:
                p = [68,624]
                screen.blit(red, p)
                p = [386,501]
                screen.blit(red, p)
                p = [536,528]
                screen.blit(red, p)
            elif s.game.spotted.position == 3:
                p = [70,528]
                screen.blit(red, p)
                p = [302,502]
                screen.blit(red, p)
                p = [620,528]
                screen.blit(red, p)
                
    pygame.display.flip()
    pygame.display.update()

def eb_animation(num):
    global screen
    if num == 9:
        eb_position = [72,1056]
        screen.blit(number_eb, eb_position)
        pygame.display.update()
    if num == 8:
        eb_position = [118,1058]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 7:
        eb_position = [184,1058]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 6:
        eb_position = [266,1058]
        screen.blit(number_eb, eb_position)
        pygame.display.update()
    if num == 5:
        eb_position = [312,1060]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 4:
        eb_position = [380,1060]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 3:
        eb_position = [460,1058]
        screen.blit(number_eb, eb_position)
        pygame.display.update()
    if num == 2:
        eb_position = [508,1056]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 1:
        eb_position = [576,1058]
        screen.blit(eb, eb_position)
        pygame.display.update()


def feature_animation(num):
    global screen
    if num == 7:
        corners_position = [64,261]
        screen.blit(c, corners_position)
        pygame.display.update()
    if num == 6:
        rs_position = [24,855]
        screen.blit(trophy, rs_position)
        pygame.display.update()
    if num == 5:
        ys_position = [624,856]
        screen.blit(trophy, ys_position)
        pygame.display.update()
    if num == 4:
        p = [291,616]
        screen.blit(f, p)
        pygame.display.update()
    if num == 3: 
        p = [52,432]
        screen.blit(super_score, p)
        pygame.display.update()
    if num == 2:
        p = [282,310]
        screen.blit(super_score, p)
        pygame.display.update()
    if num == 1:
        p = [513,429]
        screen.blit(super_score, p)
        pygame.display.update()

def odds_animation(num):
    global screen
    if num == 5:
        odds_position = [110,732]
        screen.blit(o1, odds_position)
        pygame.display.update()
    if num == 4:
        odds_position = [215,732]
        screen.blit(o2, odds_position)
        pygame.display.update()
    if num == 3:
        odds_position = [318,732]
        screen.blit(o3, odds_position)
        pygame.display.update()
    if num == 2:
        odds_position = [420,732]
        screen.blit(o4, odds_position)
        pygame.display.update()
    if num == 1:
        odds_position = [524,732]
        screen.blit(o5, odds_position)
        pygame.display.update()

