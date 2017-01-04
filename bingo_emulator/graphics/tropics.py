
import pygame
import random

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

meter = pygame.image.load('graphics/assets/silver_register_cover.png').convert()
sc_arrow = pygame.image.load('tropics/assets/sc_arrow.png').convert_alpha()
sc = pygame.image.load('tropics/assets/super_card.png').convert_alpha()
eb = pygame.image.load('tropics/assets/eb.png').convert_alpha()
extra_ball = pygame.image.load('tropics/assets/extra_ball.png').convert_alpha()
o1 = pygame.image.load('tropics/assets/odds1.png').convert_alpha()
o2 = pygame.image.load('tropics/assets/odds2.png').convert_alpha()
o3 = pygame.image.load('tropics/assets/odds3.png').convert_alpha()
o4 = pygame.image.load('tropics/assets/odds4.png').convert_alpha()
o5 = pygame.image.load('tropics/assets/odds5.png').convert_alpha()
o6 = pygame.image.load('tropics/assets/odds6.png').convert_alpha()
o7 = pygame.image.load('tropics/assets/odds7.png').convert_alpha()
o8 = pygame.image.load('tropics/assets/odds8.png').convert_alpha()
c = pygame.image.load('tropics/assets/corners.png').convert_alpha()
star = pygame.image.load('tropics/assets/rollover.png').convert_alpha()
number = pygame.image.load('tropics/assets/number.png').convert_alpha()
sc_number = pygame.image.load('tropics/assets/sc_number.png').convert_alpha()
tilt = pygame.image.load('tropics/assets/tilt.png').convert_alpha()
select_now = pygame.image.load('tropics/assets/select_now.png').convert_alpha()
red_number = pygame.image.load('tropics/assets/red_number.png').convert_alpha()
red_sc_number = pygame.image.load('tropics/assets/red_sc_number.png').convert_alpha()
s_number = pygame.image.load('tropics/assets/spotted_number.png').convert_alpha()
s_arrow1 = pygame.image.load('tropics/assets/s_arrow1.png').convert_alpha()
s_arrow2 = pygame.image.load('tropics/assets/s_arrow2.png').convert_alpha()
s_arrow3 = pygame.image.load('tropics/assets/s_arrow3.png').convert_alpha()
before_fourth = pygame.image.load('tropics/assets/time.png').convert_alpha()
s_eb = pygame.image.load('tropics/assets/s_eb.png').convert_alpha()
s_scores = pygame.image.load('tropics/assets/s_scores.png').convert_alpha()
s_sc = pygame.image.load('tropics/assets/s_sc.png').convert_alpha()
s_corners = pygame.image.load('tropics/assets/s_corners.png').convert_alpha()
advance_score = pygame.image.load('tropics/assets/advance_scores.png').convert_alpha()

class scorereel():
    """ Score Reels are used to count replays """
    def __init__(self, pos, image):
        self.position = pos
        self.default_y = self.position[1]
        self.image = pygame.image.load(image).convert()

reel1 = scorereel([108,544], "graphics/assets/green_reel.png")
reel10 = scorereel([89,544], "graphics/assets/green_reel.png")
reel100 = scorereel([70,544], "graphics/assets/green_reel.png")

def display(s, replays=0, menu=False):
    
    meter.set_colorkey((255,0,252))
    meter_position = [60,543]

    screen.blit(reel1.image, reel1.position)
    screen.blit(reel10.image, reel10.position)
    screen.blit(reel100.image, reel100.position)
    screen.blit(meter, meter_position)

    backglass_position = [0, 0]
    backglass = pygame.Surface(screen.get_size(), flags=pygame.SRCALPHA)
    backglass.fill((0, 0, 0))
    if menu == True:
        backglass = pygame.image.load('tropics/assets/tropics_menu.png')
    else:
        if (s.game.anti_cheat.status == True):
            backglass = pygame.image.load('tropics/assets/tropics_gi.png')
        else:
            backglass = pygame.image.load('tropics/assets/tropics_off.png')
    backglass = pygame.transform.scale(backglass, (720, 1280))
    
    screen.blit(backglass, backglass_position)

    if s.game.super_card.position == 1:
        p = [33,443]
        screen.blit(sc_arrow, p)
    if s.game.super_card.position == 2:
        p = [69,443]
        screen.blit(sc_arrow, p)
    if s.game.super_card.position == 3:
        p = [103,445]
        screen.blit(sc_arrow, p)
    if s.game.super_card.position == 4:
        p = [138,443]
        screen.blit(sc_arrow, p)
    if s.game.super_card.position == 5:
        p = [555,443]
        screen.blit(sc_arrow, p)
    if s.game.super_card.position == 6:
        p = [591,443]
        screen.blit(sc_arrow, p)
    if s.game.super_card.position == 7:
        p = [623,443]
        screen.blit(sc_arrow, p)
    if s.game.super_card.position == 8:
        p = [658,442]
        screen.blit(sc_arrow, p)

    if s.game.super_card.position >= 4:
        p = [32,409]
        screen.blit(sc, p)

    if s.game.super_card.position >= 8:
        p = [552,409]
        screen.blit(sc, p)

    if s.game.extra_ball.position == 1 or s.game.extra_ball.position == 10 or s.game.extra_ball.position == 19:
        eb_position = [106,962]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 2 or s.game.extra_ball.position == 11 or s.game.extra_ball.position == 20:
        eb_position = [167,960]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 3 or s.game.extra_ball.position == 12 or s.game.extra_ball.position == 21:
        eb_position = [223,960]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 4 or s.game.extra_ball.position == 13 or s.game.extra_ball.position == 22:
        eb_position = [282,960]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 5 or s.game.extra_ball.position == 14 or s.game.extra_ball.position == 23:
        eb_position = [341,959]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 6 or s.game.extra_ball.position == 15:
        eb_position = [402,960]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 7 or s.game.extra_ball.position == 16:
        eb_position = [461,961]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 8 or s.game.extra_ball.position == 17:
        eb_position = [519,959]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 9 or s.game.extra_ball.position == 18:
        eb_position = [579,960]
        screen.blit(eb, eb_position)
    
    if s.game.extra_ball.position >= 9 and s.game.extra_ball.position < 18:
        eb_pos = [106,1002]
        screen.blit(extra_ball, eb_pos)
    if s.game.extra_ball.position >= 18 and s.game.extra_ball.position < 24:
        eb_pos = [283,1002]
        screen.blit(extra_ball, eb_pos)
    if s.game.extra_ball.position == 24:
        eb_pos = [461,1002]
        screen.blit(extra_ball, eb_pos)

    
    if s.game.odds.position > 0:
        if s.game.odds.position == 1:
            odds_position = [34,741]
            screen.blit(o1, odds_position)
        if s.game.odds.position == 2:
            odds_position = [139,748]
            screen.blit(o2, odds_position)
        if s.game.odds.position == 3:
            odds_position = [230,730]
            screen.blit(o3, odds_position)
        if s.game.odds.position == 4:
            odds_position = [292,755]
            screen.blit(o4, odds_position)
        if s.game.odds.position == 5:
            odds_position = [360,754]
            screen.blit(o5, odds_position)
        if s.game.odds.position == 6:
            odds_position = [470,737]
            screen.blit(o6, odds_position)
        if s.game.odds.position == 7:
            odds_position = [532,728]
            screen.blit(o7, odds_position)
        if s.game.odds.position == 8:
            odds_position = [638,745]
            screen.blit(o8, odds_position)

    if s.game.red_star.status == True:
        rs_position = [6,959]
        screen.blit(star, rs_position)

    if s.game.yellow_star.status == True:
        ys_position = [643,959]
        screen.blit(star, ys_position)

    if s.game.corners.status == True:
        corners_position = [565,535]
        screen.blit(c, corners_position)

    if s.game.tilt.status == False:
        if s.holes:
            if 1 in s.holes:
                number_position = [224,487]
                screen.blit(number, number_position)
                number_position = [547,311]
                screen.blit(sc_number, number_position)
            if 2 in s.holes:
                number_position = [223,433]
                screen.blit(number, number_position)
            if 3 in s.holes:
                number_position = [445,541]
                screen.blit(number, number_position)
                number_position = [74,264]
                screen.blit(sc_number, number_position)
            if 4 in s.holes:
                number_position = [279,324]
                screen.blit(number, number_position)
                number_position = [597,361]
                screen.blit(sc_number, number_position)
            if 5 in s.holes:
                number_position = [335,541]
                screen.blit(number, number_position)
            if 6 in s.holes:
                number_position = [445,324]
                screen.blit(number, number_position)
            if 7 in s.holes:
                number_position = [281,542]
                screen.blit(number, number_position)
                number_position = [597,263]
                screen.blit(sc_number, number_position)
            if 8 in s.holes:
                number_position = [446,379]
                screen.blit(number, number_position)
            if 9 in s.holes:
                number_position = [221,325]
                screen.blit(number, number_position)
                number_position = [25,313]
                screen.blit(sc_number, number_position)
            if 10 in s.holes:
                number_position = [223,379]
                screen.blit(number, number_position)
                number_position = [597,312]
                screen.blit(sc_number, number_position)
            if 11 in s.holes:
                number_position = [224,542]
                screen.blit(number, number_position)
                number_position = [647,263]
                screen.blit(sc_number, number_position)
                number_position = [125,314]
                screen.blit(sc_number, number_position)
            if 12 in s.holes:
                number_position = [390,434]
                screen.blit(number, number_position)
                number_position = [26,361]
                screen.blit(sc_number, number_position)
            if 13 in s.holes:
                number_position = [335,489]
                screen.blit(number, number_position)
                number_position = [647,312]
                screen.blit(sc_number, number_position)
            if 14 in s.holes:
                number_position = [334,379]
                screen.blit(number, number_position)
                number_position = [125,361]
                screen.blit(sc_number, number_position)
            if 15 in s.holes:
                number_position = [333,323]
                screen.blit(number, number_position)
                number_position = [547,263]
                screen.blit(sc_number, number_position)
            if 16 in s.holes:
                number_position = [335,434]
                screen.blit(number, number_position)
            if 17 in s.holes:
                number_position = [445,488]
                screen.blit(number, number_position)
                number_position = [547,361]
                screen.blit(sc_number, number_position)
            if 18 in s.holes:
                number_position = [279,433]
                screen.blit(number, number_position)
                number_position = [124,265]
                screen.blit(sc_number, number_position)
                number_position = [648,359]
                screen.blit(sc_number, number_position)
            if 19 in s.holes:
                number_position = [279,379]
                screen.blit(number, number_position)
            if 20 in s.holes:
                number_position = [389,379]
                screen.blit(number, number_position)
            if 21 in s.holes:
                number_position = [391,487]
                screen.blit(number, number_position)
            if 22 in s.holes:
                number_position = [280,488]
                screen.blit(number, number_position)
            if 23 in s.holes:
                number_position = [391,542]
                screen.blit(number, number_position)
                number_position = [25,265]
                screen.blit(sc_number, number_position)
            if 24 in s.holes:
                number_position = [389,324]
                screen.blit(number, number_position)
                number_position = [75,362]
                screen.blit(sc_number, number_position)
            if 25 in s.holes:
                number_position = [447,433]
                screen.blit(number, number_position)
                number_position = [75,313]
                screen.blit(sc_number, number_position)

    if s.game.tilt.status == True:
        tilt_position = [57,628]
        screen.blit(tilt, tilt_position)

    if s.game.selection_feature.position == 2:
        p = [174,647]
        screen.blit(s_arrow1, p)
    if s.game.selection_feature.position == 3:
        p = [211,632]
        screen.blit(s_arrow2, p)
    if s.game.selection_feature.position == 4:
        p = [249,623]
        screen.blit(s_arrow3, p)
    if s.game.selection_feature.position >= 5:
        p = [285,616]
        screen.blit(s_number, p)
    if s.game.selection_feature.position >= 6:
        p = [323,609]
        screen.blit(s_number, p)
    if s.game.selection_feature.position >= 7:
        p = [360,611]
        screen.blit(s_number, p)
    if s.game.selection_feature.position >= 8:
        p = [400,615]
        screen.blit(s_number, p)
    if s.game.selection_feature.position >= 9:
        p = [437,623]
        screen.blit(s_number, p)
    if s.game.selection_feature.position >= 10:
        p = [473,635]
        screen.blit(s_number, p)
    if s.game.selection_feature.position >= 11:
        p = [507,649]
        screen.blit(s_number, p)

    if (s.game.select_spots.status == True or s.game.selection_feature_relay.status == True) and s.game.before_fourth.status == True and s.game.ball_count.position == 3:
        p = [269,700]
        screen.blit(select_now, p)
    
    if (s.game.select_spots.status == True or s.game.selection_feature_relay.status == True) and s.game.before_fifth.status == True and s.game.ball_count.position == 4:
        p = [269,700]
        screen.blit(select_now, p)

    if s.game.before_fourth.status == True and (s.game.selection_feature.position > 3 or s.game.selection_feature_relay.status == True):
        p = [14,673]
        screen.blit(before_fourth, p)
    if s.game.before_fifth.status == True and (s.game.selection_feature.position > 3 or s.game.selection_feature_relay.status == True):
        p = [535,672]
        screen.blit(before_fourth, p)

    if s.game.before_fourth.status == True:
        if s.game.ball_count.position < 4:
            if s.game.select_spots.status == True:
                if s.game.selection_feature.position >= 5:
                    if s.game.spotted.position == 0:
                        #19
                        number_position = [279,379]
                        screen.blit(red_number, number_position)
                if s.game.selection_feature.position >= 6:
                    if s.game.spotted.position == 1:
                        #20
                        number_position = [389,379]
                        screen.blit(red_number, number_position)
                if s.game.selection_feature.position >= 7:
                    if s.game.spotted.position == 2:
                        #21
                        number_position = [391,487]
                        screen.blit(red_number, number_position)
                if s.game.selection_feature.position >= 8:
                    if s.game.spotted.position == 3:
                        #22
                        number_position = [280,488]
                        screen.blit(red_number, number_position)
                if s.game.selection_feature.position >= 9:
                    if s.game.spotted.position == 4:
                        #16
                        number_position = [335,434]
                        screen.blit(red_number, number_position)
                if s.game.selection_feature.position >= 10:
                    if s.game.spotted.position == 5:
                        #25
                        number_position = [447,433]
                        screen.blit(red_number, number_position)
                        number_position = [75,313]
                        screen.blit(red_sc_number, number_position)
                if s.game.selection_feature.position >= 11:
                    if s.game.spotted.position == 6:
                        #10
                        number_position = [223,379]
                        screen.blit(red_number, number_position)
                        number_position = [597,312]
                        screen.blit(red_sc_number, number_position)
            if s.game.selection_feature_relay.status == True:
                if s.game.spotted.position == 7:
                    p = [197,662]
                    screen.blit(s_eb, p)
                if s.game.spotted.position == 8:
                    p = [277,649]
                    screen.blit(s_scores, p)
                if s.game.spotted.position == 9:
                    p = [359,649]
                    screen.blit(s_sc, p)
                if s.game.spotted.position == 10:
                    p = [439,659]
                    screen.blit(s_corners, p)

    if s.game.before_fifth.status == True:
        if s.game.ball_count.position < 5:
            if s.game.select_spots.status == True:
                if s.game.selection_feature.position >= 5:
                    if s.game.spotted.position == 0:
                        #19
                        number_position = [279,379]
                        screen.blit(red_number, number_position)
                if s.game.selection_feature.position >= 6:
                    if s.game.spotted.position == 1:
                        #20
                        number_position = [389,379]
                        screen.blit(red_number, number_position)
                if s.game.selection_feature.position >= 7:
                    if s.game.spotted.position == 2:
                        #21
                        number_position = [391,487]
                        screen.blit(red_number, number_position)
                if s.game.selection_feature.position >= 8:
                    if s.game.spotted.position == 3:
                        #22
                        number_position = [280,488]
                        screen.blit(red_number, number_position)
                if s.game.selection_feature.position >= 9:
                    if s.game.spotted.position == 4:
                        #16
                        number_position = [335,434]
                        screen.blit(red_number, number_position)
                if s.game.selection_feature.position >= 10:
                    if s.game.spotted.position == 5:
                        #25
                        number_position = [447,433]
                        screen.blit(red_number, number_position)
                        number_position = [75,313]
                        screen.blit(red_sc_number, number_position)
                if s.game.selection_feature.position >= 11:
                    if s.game.spotted.position == 6:
                        #10
                        number_position = [223,379]
                        screen.blit(red_number, number_position)
                        number_position = [597,312]
                        screen.blit(red_sc_number, number_position)
            if s.game.selection_feature_relay.status == True:
                if s.game.spotted.position == 7:
                    p = [197,662]
                    screen.blit(s_eb, p)
                if s.game.spotted.position == 8:
                    p = [277,649]
                    screen.blit(s_scores, p)
                if s.game.spotted.position == 9:
                    p = [359,649]
                    screen.blit(s_sc, p)
                if s.game.spotted.position == 10:
                    p = [439,659]
                    screen.blit(s_corners, p)


    if s.game.selection_feature_relay.status == True:
        if s.game.before_fourth.status == True:
            max_ball = 4
        else:
            max_ball = 5
        if s.game.ball_count.position == max_ball:
            if s.game.spotted.position == 8:
                if s.game.odds.position < 8:
                    p = [287,918]
                    screen.blit(advance_score, p)

    pygame.display.update()

def eb_animation(num):
    global screen

    if num == 9:
        eb_position = [106,962]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 8:
        eb_position = [167,960]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 7:
        eb_position = [223,960]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 6:
        eb_position = [282,960]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 5:
        eb_position = [341,959]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 4:
        eb_position = [402,960]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 3:
        eb_position = [461,961]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 2:
        eb_position = [519,959]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 1:
        eb_position = [579,960]
        screen.blit(eb, eb_position)
        pygame.display.update()


def feature_animation(num):
    global screen
    if num == 6:
        corners_position = [565,535]
        screen.blit(c, corners_position)
        pygame.display.update()

    if num == 5:
        rs_position = [6,959]
        screen.blit(star, rs_position)
        pygame.display.update()

    if num == 4:
        ys_position = [643,959]
        screen.blit(star, ys_position)
        pygame.display.update()

    if num == 3:
        p = [33,443]
        screen.blit(sc_arrow, p)
        pygame.display.update()

    if num == 2:
        p = [32,409]
        screen.blit(sc, p)
        pygame.display.update()

    if num == 1:
        p = [552,409]
        screen.blit(sc, p)
        pygame.display.update()


def odds_animation(num):
    global screen
    if num == 5:
        odds_position = [34,741]
        o = pygame.image.load('tropics/assets/odds1.png').convert_alpha()
        screen.blit(o, odds_position)
        pygame.display.update()
    if num == 4:
        odds_position = [139,748]
        o = pygame.image.load('tropics/assets/odds2.png').convert_alpha()
        screen.blit(o, odds_position)
        pygame.display.update()
    if num == 3:
        odds_position = [230,730]
        o = pygame.image.load('tropics/assets/odds3.png').convert_alpha()
        screen.blit(o, odds_position)
        pygame.display.update()
    if num == 2:
        odds_position = [292,755]
        o = pygame.image.load('tropics/assets/odds4.png').convert_alpha()
        screen.blit(o, odds_position)
        pygame.display.update()
    if num == 1:
        odds_position = [360,754]
        o = pygame.image.load('tropics/assets/odds5.png').convert_alpha()
        screen.blit(o, odds_position)
        pygame.display.update()
