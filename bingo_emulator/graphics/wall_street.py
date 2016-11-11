
import pygame

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

meter = pygame.image.load('graphics/assets/black_register_cover.png').convert()
card = pygame.image.load('wall_street/assets/card.png').convert_alpha()
number = pygame.image.load('wall_street/assets/number.png').convert_alpha()
corners = pygame.image.load('wall_street/assets/corners.png').convert_alpha()
super_line = pygame.image.load('wall_street/assets/super_line.png').convert_alpha()
c = pygame.image.load('wall_street/assets/regular.png').convert_alpha()
d = pygame.image.load('wall_street/assets/double.png').convert_alpha()
n = pygame.image.load('wall_street/assets/nothing.png').convert_alpha()
tilt = pygame.image.load('wall_street/assets/tilt.png').convert_alpha()
blink_image = pygame.image.load('wall_street/assets/double_or_nothing.png').convert_alpha()

class scorereel():
    """ Score Reels are used to count replays """
    def __init__(self, pos, image):
        self.position = pos
        self.default_y = self.position[1]
        self.image = pygame.image.load(image).convert()

reel1 = scorereel([385,654], "graphics/assets/white_reel.png")
reel10 = scorereel([365,654], "graphics/assets/white_reel.png")
reel100 = scorereel([346,654], "graphics/assets/white_reel.png")
reel1000 = scorereel([327,654], "graphics/assets/white_reel.png")

def display(s, replays=0, menu=False):
    
    meter.set_colorkey((255,0,252))
    meter_position = [318,654]

    screen.blit(reel1.image, reel1.position)
    screen.blit(reel10.image, reel10.position)
    screen.blit(reel100.image, reel100.position)
    screen.blit(reel1000.image, reel1000.position)
    screen.blit(meter, meter_position)

    backglass_position = [0, 0]
    backglass = pygame.Surface((720,1280), pygame.SRCALPHA | pygame.FULLSCREEN)
    backglass.fill((0, 0, 0))
    if menu == True:
        backglass = pygame.image.load('wall_street/assets/wall_street_menu.png')
    else:
        if (s.game.anti_cheat.status == True):
            backglass = pygame.image.load('wall_street/assets/wall_street_gi.png')
        else:
            backglass = pygame.image.load('wall_street/assets/wall_street_off.png')
    #backglass = pygame.transform.scale(backglass, (1280,720))
    screen.blit(backglass, backglass_position)

    if s.game.selector.position >= 1:
        position = [120,383]
        screen.blit(card, position)
    if s.game.selector.position >= 2:
        position = [356,337]
        screen.blit(card, position)
    if s.game.selector.position >= 3:
        position = [587,384]
        screen.blit(card, position)
    if s.game.selector.position >= 4:
        position = [123,784]
        screen.blit(card, position)
    if s.game.selector.position >= 5:
        position = [354,793]
        screen.blit(card, position)
    if s.game.selector.position >= 6:
        position = [584,783]
        screen.blit(card, position)

    if s.game.tilt.status == False:
        if s.holes:
            if 1 in s.holes:
                position = [90,455]
                screen.blit(number, position)
                position = [291,514]
                screen.blit(number, position)
                position = [662,455]
                screen.blit(number, position)
                position = [163,990]
                screen.blit(number, position)
                position = [358,862]
                screen.blit(number, position)
                position = [523,988]
                screen.blit(number, position)
            if 2 in s.holes:
                position = [127,596]
                screen.blit(number, position)
                position = [291,480]
                screen.blit(number, position)
                position = [662,490]
                screen.blit(number, position)
                position = [195,922]
                screen.blit(number, position)
                position = [392,998]
                screen.blit(number, position)
                position = [522,886]
                screen.blit(number, position)
            if 3 in s.holes:
                position = [193,457]
                screen.blit(number, position)
                position = [428,549]
                screen.blit(number, position)
                position = [593,456]
                screen.blit(number, position)
                position = [61,856]
                screen.blit(number, position)
                position = [358,897]
                screen.blit(number, position)
                position = [622,992]
                screen.blit(number, position)
            if 4 in s.holes:
                position = [159,597]
                screen.blit(number, position)
                position = [393,408]
                screen.blit(number, position)
                position = [625,595]
                screen.blit(number, position)
                position = [163,854]
                screen.blit(number, position)
                position = [292,863]
                screen.blit(number, position)
                position = [655,852]
                screen.blit(number, position)
            if 5 in s.holes:
                position = [55,457]
                screen.blit(number, position)
                position = [359,552]
                screen.blit(number, position)
                position = [524,526]
                screen.blit(number, position)
                position = [197,989]
                screen.blit(number, position)
                position = [425,862]
                screen.blit(number, position)
                position = [657,921]
                screen.blit(number, position)
            if 6 in s.holes:
                position = [57,527]
                screen.blit(number, position)
                position = [427,409]
                screen.blit(number, position)
                position = [524,456]
                screen.blit(number, position)
                position = [62,992]
                screen.blit(number, position)
                position = [325,862]
                screen.blit(number, position)
                position = [656,989]
                screen.blit(number, position)
            if 7 in s.holes:
                position = [193,492]
                screen.blit(number, position)
                position = [327,551]
                screen.blit(number, position)
                position = [560,455]
                screen.blit(number, position)
                position = [96,855]
                screen.blit(number, position)
                position = [292,999]
                screen.blit(number, position)
                position = [555,989]
                screen.blit(number, position)
            if 8 in s.holes:
                position = [58,492]
                screen.blit(number, position)
                position = [428,514]
                screen.blit(number, position)
                position = [661,596]
                screen.blit(number, position)
                position = [197,887]
                screen.blit(number, position)
                position = [426,965]
                screen.blit(number, position)
                position = [522,853]
                screen.blit(number, position)
            if 9 in s.holes:
                position = [123,456]
                screen.blit(number, position)
                position = [292,409]
                screen.blit(number, position)
                position = [593,560]
                screen.blit(number, position)
                position = [196,854]
                screen.blit(number, position)
                position = [292,932]
                screen.blit(number, position)
                position = [590,954]
                screen.blit(number, position)
            if 10 in s.holes:
                position = [125,489]
                screen.blit(number, position)
                position = [292,550]
                screen.blit(number, position)
                position = [525,595]
                screen.blit(number, position)
                position = [127,854]
                screen.blit(number, position)
                position = [292,964]
                screen.blit(number, position)
                position = [588,852]
                screen.blit(number, position)
            if 11 in s.holes:
                position = [159,527]
                screen.blit(number, position)
                position = [359,516]
                screen.blit(number, position)
                position = [525,559]
                screen.blit(number, position)
                position = [162,922]
                screen.blit(number, position)
                position = [426,999]
                screen.blit(number, position)
                position = [656,955]
                screen.blit(number, position)
            if 12 in s.holes:
                position = [58,597]
                screen.blit(number, position)
                position = [393,478]
                screen.blit(number, position)
                position = [593,492]
                screen.blit(number, position)
                position = [127,957]
                screen.blit(number, position)
                position = [393,930]
                screen.blit(number, position)
                position = [556,921]
                screen.blit(number, position)
            if 13 in s.holes:
                position = [193,561]
                screen.blit(number, position)
                position = [292,444]
                screen.blit(number, position)
                position = [559,595]
                screen.blit(number, position)
                position = [62,957]
                screen.blit(number, position)
                position = [427,896]
                screen.blit(number, position)
                position = [623,853]
                screen.blit(number, position)
            if 14 in s.holes:
                position = [126,562]
                screen.blit(number, position)
                position = [358,443]
                screen.blit(number, position)
                position = [559,491]
                screen.blit(number, position)
                position = [95,922]
                screen.blit(number, position)
                position = [393,964]
                screen.blit(number, position)
                position = [623,886]
                screen.blit(number, position)
            if 15 in s.holes:
                position = [193,595]
                screen.blit(number, position)
                position = [362,478]
                screen.blit(number, position)
                position = [625,561]
                screen.blit(number, position)
                position = [61,923]
                screen.blit(number, position)
                position = [325,896]
                screen.blit(number, position)
                position = [556,954]
                screen.blit(number, position)
            if 16 in s.holes:
                position = [125,524]
                screen.blit(number, position)
                position = [360,409]
                screen.blit(number, position)
                position = [626,526]
                screen.blit(number, position)
                position = [128,991]
                screen.blit(number, position)
                position = [359,965]
                screen.blit(number, position)
                position = [589,886]
                screen.blit(number, position)
            if 17 in s.holes:
                position = [193,528]
                screen.blit(number, position)
                position = [427,479]
                screen.blit(number, position)
                position = [558,562]
                screen.blit(number, position)
                position = [128,923]
                screen.blit(number, position)
                position = [392,897]
                screen.blit(number, position)
                position = [557,887]
                screen.blit(number, position)
            if 18 in s.holes:
                position = [91,525]
                screen.blit(number, position)
                position = [326,479]
                screen.blit(number, position)
                position = [626,490]
                screen.blit(number, position)
                position = [127,889]
                screen.blit(number, position)
                position = [326,964]
                screen.blit(number, position)
                position = [622,955]
                screen.blit(number, position)
            if 19 in s.holes:
                position = [158,489]
                screen.blit(number, position)
                position = [327,445]
                screen.blit(number, position)
                position = [559,525]
                screen.blit(number, position)
                position = [162,957]
                screen.blit(number, position)
                position = [326,931]
                screen.blit(number, position)
                position = [623,921]
                screen.blit(number, position)
            if 20 in s.holes:
                position = [159,561]
                screen.blit(number, position)
                position = [394,443]
                screen.blit(number, position)
                position = [592,525]
                screen.blit(number, position)
                position = [96,957]
                screen.blit(number, position)
                position = [427,930]
                screen.blit(number, position)
                position = [523,920]
                screen.blit(number, position)
            if 21 in s.holes:
                position = [92,562]
                screen.blit(number, position)
                position = [395,515]
                screen.blit(number, position)
                position = [591,596]
                screen.blit(number, position)
                position = [94,888]
                screen.blit(number, position)
                position = [359,930]
                screen.blit(number, position)
                position = [589,989]
                screen.blit(number, position)
            if 22 in s.holes:
                position = [92,490]
                screen.blit(number, position)
                position = [326,515]
                screen.blit(number, position)
                position = [661,525]
                screen.blit(number, position)
                position = [162,887]
                screen.blit(number, position)
                position = [359,999]
                screen.blit(number, position)
                position = [589,920]
                screen.blit(number, position)
            if 23 in s.holes:
                position = [92,596]
                screen.blit(number, position)
                position = [393,549]
                screen.blit(number, position)
                position = [525,490]
                screen.blit(number, position)
                position = [197,956]
                screen.blit(number, position)
                position = [392,861]
                screen.blit(number, position)
                position = [557,852]
                screen.blit(number, position)
            if 24 in s.holes:
                position = [58,562]
                screen.blit(number, position)
                position = [326,409]
                screen.blit(number, position)
                position = [627,455]
                screen.blit(number, position)
                position = [61,888]
                screen.blit(number, position)
                position = [326,999]
                screen.blit(number, position)
                position = [655,885]
                screen.blit(number, position)
            if 25 in s.holes:
                position = [158,455]
                screen.blit(number, position)
                position = [428,443]
                screen.blit(number, position)
                position = [660,560]
                screen.blit(number, position)
                position = [96,992]
                screen.blit(number, position)
                position = [292,897]
                screen.blit(number, position)
                position = [522,955]
                screen.blit(number, position)

        if s.game.sixteen.status == True:
            p = [12,485]
            screen.blit(number, p)
        if s.game.fifteen.status == True:
            p = [248,439]
            screen.blit(number, p)
        if s.game.twenty.status == True:
            p = [481,486]
            screen.blit(number, p)
        if s.game.seventeen.status == True:
            p = [17,884]
            screen.blit(number, p)
        if s.game.twentyone.status == True:
            p = [249,892]
            screen.blit(number, p)
        if s.game.twentytwo.status == True:
            p = [479,881]
            screen.blit(number, p)

        if s.game.corners1.status == True:
            position = [12,382]
            screen.blit(corners, position)
        if s.game.corners2.status == True:
            position = [248,336]
            screen.blit(corners, position)
        if s.game.corners3.status == True:
            position = [483,383]
            screen.blit(corners, position)
        if s.game.corners4.status == True:
            position = [17,784]
            screen.blit(corners, position)
        if s.game.corners5.status == True:
            position = [249,792]
            screen.blit(corners, position)
        if s.game.corners6.status == True:
            position = [480,782]
            screen.blit(corners, position)

        if s.game.super1.status == True:
            position = [9,558]
            screen.blit(super_line, position)
        if s.game.super2.status == True:
            position = [245,512]
            screen.blit(super_line, position)
        if s.game.super3.status == True:
            position = [479,558]
            screen.blit(super_line, position)
        if s.game.super4.status == True:
            position = [13,954]
            screen.blit(super_line, position)
        if s.game.super5.status == True:
            position = [245,962]
            screen.blit(super_line, position)
        if s.game.super6.status == True:
            position = [475,952]
            screen.blit(super_line, position)

        if s.game.card1_replay_counter.position > 0 or s.game.card2_replay_counter.position > 0 or s.game.card3_replay_counter.position > 0 or s.game.card4_replay_counter.position > 0 or s.game.card5_replay_counter.position > 0 or s.game.card6_replay_counter.position > 0:
            if s.game.card1_replay_counter.position > 0 and s.game.card1_double.status == False:
                position = [73,404]
                screen.blit(c, position)
            if s.game.card2_replay_counter.position > 0 and s.game.card2_double.status == False:
                position = [309,358]
                screen.blit(c, position)
            if s.game.card3_replay_counter.position > 0 and s.game.card3_double.status == False:
                position = [543,406]
                screen.blit(c, position)
            if s.game.card4_replay_counter.position > 0 and s.game.card4_double.status == False:
                position = [77,805]
                screen.blit(c, position)
            if s.game.card5_replay_counter.position > 0 and s.game.card5_double.status == False:
                position = [309,814]
                screen.blit(c, position)
            if s.game.card6_replay_counter.position > 0 and s.game.card6_double.status == False:
                position = [540,804]
                screen.blit(c, position)

        if s.game.card1_double.status == True:
            position = [125,416]
            screen.blit(d, position)
        if s.game.card2_double.status == True:
            position = [361,370]
            screen.blit(d, position)
        if s.game.card3_double.status == True:
            position = [595,416]
            screen.blit(d, position)
        if s.game.card4_double.status == True:
            position = [129,815]
            screen.blit(d, position)
        if s.game.card5_double.status == True:
            position = [359,824]
            screen.blit(d, position)
        if s.game.card6_double.status == True:
            position = [590,813]
            screen.blit(d, position)

        if s.game.card1_missed.status == True:
            position = [178,416]
            screen.blit(n, position)
        if s.game.card2_missed.status == True:
            position = [411,370]
            screen.blit(n, position)
        if s.game.card3_missed.status == True:
            position = [645,416]
            screen.blit(n, position)
        if s.game.card4_missed.status == True:
            position = [181,815]
            screen.blit(n, position)
        if s.game.card5_missed.status == True:
            position = [411,824]
            screen.blit(n, position)
        if s.game.card6_missed.status == True:
            position = [641,813]
            screen.blit(n, position)

    if s.game.tilt.status == True:
        position = [40,676]
        screen.blit(tilt, position)

    pygame.display.update()

def blink_double(s):
    s.game.blink = not s.game.blink
    if s.game.blink == 1:
        blink_pos = [505,656]
        screen.blit(blink_image, blink_pos)
        pygame.display.update()
    else:
        display(s)
