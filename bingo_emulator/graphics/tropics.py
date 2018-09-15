
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
red_s_eb = pygame.image.load('tropics/assets/red_s_eb.png').convert_alpha()
red_s_scores = pygame.image.load('tropics/assets/red_s_scores.png').convert_alpha()
red_s_sc = pygame.image.load('tropics/assets/red_s_sc.png').convert_alpha()
red_s_corners = pygame.image.load('tropics/assets/red_s_corners.png').convert_alpha()
advance_score = pygame.image.load('tropics/assets/advance_scores.png').convert_alpha()
bg_menu = pygame.image.load('tropics/assets/tropics_menu.png')
bg_gi = pygame.image.load('tropics/assets/tropics_gi.png')
bg_off = pygame.image.load('tropics/assets/tropics_off.png')

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
        screen.blit(bg_menu, backglass_position)
    else:
        if (s.game.anti_cheat.status == True):
            screen.blit(bg_gi, backglass_position)
        else:
            screen.blit(bg_off, backglass_position)

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

    if (s.game.select_spots.status == True or s.game.selection_feature_relay.status == True):
        if s.game.before_fourth.status == True:
            if s.game.ball_count.position == 3:
                s.cancel_delayed(name="blink")
                blink([s,1,1])
            else:
                s.cancel_delayed(name="blink")
    
    if (s.game.select_spots.status == True or s.game.selection_feature_relay.status == True):
        if s.game.before_fifth.status == True:
            if s.game.ball_count.position == 4:
                s.cancel_delayed(name="blink")
                blink([s,1,1])
            else:
                s.cancel_delayed(name="blink")

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
                p = [197,662]
                screen.blit(s_eb, p)
                p = [277,649]
                screen.blit(s_scores, p)
                p = [359,649]
                screen.blit(s_sc, p)
                p = [439,659]
                screen.blit(s_corners, p)
                if s.game.spotted.position == 7:
                    p = [197,662]
                    screen.blit(red_s_eb, p)
                if s.game.spotted.position == 8:
                    p = [277,649]
                    screen.blit(red_s_scores, p)
                if s.game.spotted.position == 9:
                    p = [359,649]
                    screen.blit(red_s_sc, p)
                if s.game.spotted.position == 10:
                    p = [439,659]
                    screen.blit(red_s_corners, p)

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

def blink(args):
    dirty_rects = []
    s = args[0]
    b = args[1]
    sn = args[2]

    if b == 0:
        if sn == 1:
            p = [269,700]
            dirty_rects.append(screen.blit(select_now, p))
        pygame.display.update(dirty_rects)
    else:
        dirty_rects.append(screen.blit(bg_gi, (269,700), pygame.Rect(269,700,185,49)))
        pygame.display.update(dirty_rects)
    b = not b

    args = [s,b,sn]

    s.delay(name="blink", delay=0.1, handler=blink, param=args)

def eb_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]
    if s.game.extra_ball.position not in [2,11,20]:
        dirty_rects.append(screen.blit(bg_gi, (167,960), pygame.Rect(167,960,39,41)))
    if s.game.extra_ball.position not in [3,12,21]:
        dirty_rects.append(screen.blit(bg_gi, (223,960), pygame.Rect(223,960,39,41)))
    if s.game.extra_ball.position not in [4,13,22]:
        dirty_rects.append(screen.blit(bg_gi, (282,960), pygame.Rect(282,960,39,41)))
    if s.game.extra_ball.position not in [5,14,23]:
        dirty_rects.append(screen.blit(bg_gi, (341,959), pygame.Rect(341,959,39,41)))
    if s.game.extra_ball.position not in [6,15]:
        dirty_rects.append(screen.blit(bg_gi, (402,960), pygame.Rect(402,960,39,41)))
    if s.game.extra_ball.position not in [7,16]:
        dirty_rects.append(screen.blit(bg_gi, (461,961), pygame.Rect(461,961,39,41)))
    if s.game.extra_ball.position not in [8,17]:
        dirty_rects.append(screen.blit(bg_gi, (519,959), pygame.Rect(519,959,39,41)))
    if s.game.extra_ball.position not in [9,18]:
        dirty_rects.append(screen.blit(bg_gi, (579,960), pygame.Rect(579,960,39,41)))
    if s.game.extra_ball.position < 8:
        dirty_rects.append(screen.blit(bg_gi, (106,1002), pygame.Rect(106,1002,155,35)))
    if s.game.extra_ball.position < 17:
        dirty_rects.append(screen.blit(bg_gi, (283,1002), pygame.Rect(283,1002,155,35)))
    if s.game.extra_ball.position < 24:
        dirty_rects.append(screen.blit(bg_gi, (461,1002), pygame.Rect(461,1002,155,35)))
    pygame.display.update(dirty_rects)

    if num in [1,9,17]:
        if s.game.extra_ball.position not in [2,11,20]:
            p = [167,960]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects) 
    elif num in [2,10,18]:
        if s.game.extra_ball.position not in [3,12,21]:
            p = [223,960]
            dirty_rects.append(screen.blit(eb, p))
            if s.game.extra_ball.position not in range(8,19):
                p = [106,1002]
                screen.blit(extra_ball, p)
            pygame.display.update(dirty_rects)
    elif num in [3,11,18]:
        if s.game.extra_ball.position not in [4,13,22]:
            p = [282,960]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
    elif num in [4,12,20]:
        if s.game.extra_ball.position not in [5,14,23]:
            p = [341,959]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
    elif num in [5,13,21]:
        if s.game.extra_ball.position not in [6,15]:
            p = [402,960]
            dirty_rects.append(screen.blit(eb, p))
            if s.game.extra_ball.position not in range(17,25):
                p = [283,1002]
                screen.blit(extra_ball, p)
            pygame.display.update(dirty_rects)
    elif num in [6,14,22]:
        if s.game.extra_ball.position not in [7,16]:
            p = [461,961]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
    elif num in [7,15,23]:
        if s.game.extra_ball.position not in [8,17]:
            p = [519,959]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
    elif num in [8,16,24]:
        if s.game.extra_ball.position not in [9,18]:
            p = [579,960]
            dirty_rects.append(screen.blit(eb, p))
            if s.game.extra_ball.position != 24:
                p = [461,1002]
                screen.blit(extra_ball, p)
            pygame.display.update(dirty_rects)

def clear_odds(s, num):
    global screen

    dirty_rects = []
    if s.game.odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (34,741), pygame.Rect(34,741,35,166)))
    if s.game.odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (139,748), pygame.Rect(139,748,39,168)))
    if s.game.odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (230,730), pygame.Rect(230,730,33,145)))
    if s.game.odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (292,755), pygame.Rect(292,755,58,148)))
    if s.game.odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (360,754), pygame.Rect(360,754,47,142)))
    if s.game.odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (470,737), pygame.Rect(470,737,49,137)))
    if s.game.odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (532,728), pygame.Rect(532,728,54,148)))
    if s.game.odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (638,745), pygame.Rect(638,745,49,160)))

    pygame.display.update(dirty_rects)

def draw_odds_animation(s, num):
    global screen
    dirty_rects = []
    if num in [0,11,17]:
        if s.game.odds.position != 1:
            p = [34,741]
            dirty_rects.append(screen.blit(o1, p))
            pygame.display.update(dirty_rects)
            return
    if num in [1,10,18]:
        if s.game.odds.position != 2:
            p = [139,748]
            dirty_rects.append(screen.blit(o2, p))
            pygame.display.update(dirty_rects)
            return
    if num in [4,12,19]:
        if s.game.odds.position != 3:
            p = [230,730]
            dirty_rects.append(screen.blit(o3, p))
            pygame.display.update(dirty_rects)
            return
    if num in [3,9,20]:
        if s.game.odds.position != 4:
            p = [292,755]
            dirty_rects.append(screen.blit(o4, p))
            pygame.display.update(dirty_rects)
            return
    if num in [5,13,21]:
        if s.game.odds.position != 5:
            p = [360,754]
            dirty_rects.append(screen.blit(o5, p))
            pygame.display.update(dirty_rects)
            return
    if num in [6,14,22]:
        if s.game.odds.position != 6:
            p = [470,737]
            dirty_rects.append(screen.blit(o6, p))
            pygame.display.update(dirty_rects)
            return
    if num in [7,16,23]:
        if s.game.odds.position != 7:
            p = [532,728]
            dirty_rects.append(screen.blit(o7, p))
            pygame.display.update(dirty_rects)
            return
    if num in [8,15,24]:
        if s.game.odds.position != 8:
            p = [638,745]
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

def clear_mixers(s):
    global screen
    dirty_rects = []
    if s.game.super_card.position < 4:
        dirty_rects.append(screen.blit(bg_gi, (32,409), pygame.Rect(32,409,134,30)))
    if s.game.super_card.position < 8:
        dirty_rects.append(screen.blit(bg_gi, (552,409), pygame.Rect(552,409,134,30)))
    if s.game.corners.status == False:
        dirty_rects.append(screen.blit(bg_gi, (565,535), pygame.Rect(565,535,109,75)))
    if s.game.yellow_star.status == False:
        dirty_rects.append(screen.blit(bg_gi, (643,959), pygame.Rect(643,959,76,75)))
    if s.game.red_star.status == False:
        dirty_rects.append(screen.blit(bg_gi, (6,959), pygame.Rect(6,959,76,75)))
    pygame.display.update(dirty_rects)
    return

def animate_mixer1(s):
    global screen
    dirty_rects = []
    if s.game.super_card.position < 4:
        p = [32,409]
        dirty_rects.append(screen.blit(sc, p))
        pygame.display.update(dirty_rects)
        return

def animate_mixer2(s):
    global screen
    dirty_rects = []
    if s.game.super_card.position < 8:
        p = [552,409]
        dirty_rects.append(screen.blit(sc, p))
    pygame.display.update(dirty_rects)
    return

def animate_mixer3(s):
    global screen
    dirty_rects = []
    if s.game.corners.status == False:
        p = [565,535]
        dirty_rects.append(screen.blit(c, p))
    if s.game.red_star.status == False:
        p = [6,959]
        dirty_rects.append(screen.blit(star, p))
        s.game.coils.redROLamp.pulse(85)
    if s.game.yellow_star.status == False:
        p = [643,959]
        dirty_rects.append(screen.blit(star, p))
        s.game.coils.yellowROLamp.pulse(85)
    pygame.display.update(dirty_rects)
    return

def animate_mixer4(s):
    return

def clear_features(s, num):
    global screen
    dirty_rects = []
    if s.game.before_fourth.status == False:
        dirty_rects.append(screen.blit(bg_gi, (14,673), pygame.Rect(14,673,165,58)))
    if s.game.before_fifth.status == False:
        dirty_rects.append(screen.blit(bg_gi, (535,672), pygame.Rect(535,672,165,58)))

    if s.game.selection_feature.position < 2:
        dirty_rects.append(screen.blit(bg_gi, (174,647), pygame.Rect(174,647,35,34)))
    if s.game.selection_feature.position < 3:
        dirty_rects.append(screen.blit(bg_gi, (211,632), pygame.Rect(211,632,34,35)))
    if s.game.selection_feature.position < 4:
        dirty_rects.append(screen.blit(bg_gi, (249,623), pygame.Rect(249,623,32,35)))
    if s.game.selection_feature.position < 6:
        dirty_rects.append(screen.blit(bg_gi, (285,616), pygame.Rect(285,616,34,34)))
        dirty_rects.append(screen.blit(bg_gi, (323,609), pygame.Rect(323,609,34,34)))
    if s.game.selection_feature.position < 7:
        dirty_rects.append(screen.blit(bg_gi, (360,611), pygame.Rect(360,611,34,34)))
        if s.game.selection_feature_relay.status == False:
            dirty_rects.append(screen.blit(bg_gi, (197,662), pygame.Rect(197,662,84,66)))
            dirty_rects.append(screen.blit(bg_gi, (277,649), pygame.Rect(277,649,82,53)))
            dirty_rects.append(screen.blit(bg_gi, (359,649), pygame.Rect(359,649,79,56)))
            dirty_rects.append(screen.blit(bg_gi, (439,659), pygame.Rect(439,659,79,70)))
    if s.game.selection_feature.position < 8:
        dirty_rects.append(screen.blit(bg_gi, (400,615), pygame.Rect(400,615,34,34)))
    if s.game.selection_feature.position < 9:
        dirty_rects.append(screen.blit(bg_gi, (437,623), pygame.Rect(437,623,34,34)))
    if s.game.selection_feature.position < 10:
        dirty_rects.append(screen.blit(bg_gi, (473,635), pygame.Rect(473,635,34,34)))
    if s.game.selection_feature.position < 11:
        dirty_rects.append(screen.blit(bg_gi, (507,649), pygame.Rect(507,649,34,34)))

    pygame.display.update(dirty_rects)

def draw_feature_animation(s, num):
    global screen
    dirty_rects = []

    if num in [4,15,10,21,5,16]:
        if s.game.before_fourth.status == False:
            p = [14,673]
            dirty_rects.append(screen.blit(before_fourth, p))
        if s.game.before_fifth.status == False and s.game.before_fourth.status == True:
            p = [535,672]
            dirty_rects.append(screen.blit(before_fourth, p))
        if s.game.selection_feature.position < 8:
            p = [400,615]
            dirty_rects.append(screen.blit(s_number, p))
        pygame.display.update(dirty_rects)
        return
    if num in [0,11,22]:
        if s.game.selection_feature.position < 2:
            p = [174,647]
            dirty_rects.append(screen.blit(s_arrow1, p))
            pygame.display.update(dirty_rects)
            return
    if num in [9,20,23]:
        if s.game.selection_feature.position < 3:
            p = [211,632]
            dirty_rects.append(screen.blit(s_arrow2, p))
            pygame.display.update(dirty_rects)
            return
    if num in [1,12,24]:
        if s.game.selection_feature.position < 4:
            p = [249,623]
            dirty_rects.append(screen.blit(s_arrow3, p))
            pygame.display.update(dirty_rects)
            return
    if num in [2,13]:
        if s.game.selection_feature.position < 6:
            p = [285,616]
            dirty_rects.append(screen.blit(s_number, p))
            p = [323,609]
            dirty_rects.append(screen.blit(s_number, p))
            pygame.display.update(dirty_rects)
            return
    if num in [3,14,4,15]:
        if s.game.selection_feature.position < 7:
            p = [360,611]
            dirty_rects.append(screen.blit(s_number, p))
        if s.game.selection_feature_relay.status == False:
            p = [197,662]
            dirty_rects.append(screen.blit(s_eb, p))
            p = [277,649]
            dirty_rects.append(screen.blit(s_scores, p))
            p = [359,649]
            dirty_rects.append(screen.blit(s_sc, p))
            p = [439,659]
            dirty_rects.append(screen.blit(s_corners, p))
        pygame.display.update(dirty_rects)
        return
    if num in [6,17]:
        if s.game.selection_feature.position < 9:
            p = [437,623]
            dirty_rects.append(screen.blit(s_number, p))
            pygame.display.update(dirty_rects)
            return
    if num in [7,18]:
        if s.game.selection_feature.position < 10:
            p = [473,635]
            dirty_rects.append(screen.blit(s_number, p))
            pygame.display.update(dirty_rects)
            return
    if num in [8,19]:
        if s.game.selection_feature.position < 11:
            p = [507,649]
            dirty_rects.append(screen.blit(s_number, p))
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

    if num % 2 == 0:
        clear_mixers(s)

    draw_odds_animation(s, num)
    draw_feature_animation(s, num)

