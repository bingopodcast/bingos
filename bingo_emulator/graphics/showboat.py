
import pygame
import random

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

meter = pygame.image.load('graphics/assets/silver_register_cover.png').convert()
card = pygame.image.load('showboat/assets/card.png').convert_alpha()
double_triple = pygame.image.load('showboat/assets/double_triple.png').convert_alpha()
i = pygame.image.load('showboat/assets/number.png').convert_alpha()
eb = pygame.image.load('showboat/assets/eb.png').convert_alpha()
tilt = pygame.image.load('showboat/assets/tilt.png').convert_alpha()
bg_menu = pygame.image.load('showboat/assets/showboat_menu.png')
bg_gi = pygame.image.load('showboat/assets/showboat_gi.png')
bg_off = pygame.image.load('showboat/assets/showboat_off.png')

class scorereel():
    """ Score Reels are used to count replays """
    def __init__(self, pos, image):
        self.position = pos
        self.default_y = self.position[1]
        self.image = pygame.image.load(image).convert()

reel1 = scorereel([97,325], "graphics/assets/white_reel.png")
reel10 = scorereel([78,325], "graphics/assets/white_reel.png")
reel100 = scorereel([60,325], "graphics/assets/white_reel.png")

def display(s, replays=0, menu=False):
    
    meter.set_colorkey((255,0,252))
    meter_position = [50,323]

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
        if (s.game.lock.status == True):
            screen.blit(bg_gi, backglass_position)
        else:
            screen.blit(bg_off, backglass_position)

    if s.game.selector.position >= 1:
        p = [48,450]
        screen.blit(card, p)
    if s.game.selector.position >= 2:
        p = [282,362]
        screen.blit(card, p)
    if s.game.selector.position >= 3:
        p = [520,453]
        screen.blit(card, p)
    if s.game.selector.position >= 4:
        p = [51,706]
        screen.blit(card, p)
    if s.game.selector.position >= 5:
        p = [284,706]
        screen.blit(card, p)
    if s.game.selector.position >= 6:
        p = [513,708]
        screen.blit(card, p)

    if s.game.c1_double.status == True:
        c1d_position = [24,660]
        screen.blit(double_triple, c1d_position)
    if s.game.c2_double.status == True:
        p = [261,573]
        screen.blit(double_triple, p)
    if s.game.c3_double.status == True:
        p = [492,662]
        screen.blit(double_triple, p)
    if s.game.c4_double.status == True:
        p = [27,918]
        screen.blit(double_triple, p)
    if s.game.c5_double.status == True:
        p = [258,916]
        screen.blit(double_triple, p)
    if s.game.c6_double.status == True:
        p = [490,916]
        screen.blit(double_triple, p)

    if s.game.c1_triple.status == True:
        p = [124,662]
        screen.blit(double_triple, p)
    if s.game.c2_triple.status == True:
        p = [363,573]
        screen.blit(double_triple, p)
    if s.game.c3_triple.status == True:
        p = [592,664]
        screen.blit(double_triple, p)
    if s.game.c4_triple.status == True:
        p = [124,916]
        screen.blit(double_triple, p)
    if s.game.c5_triple.status == True:
        p = [360,916]
        screen.blit(double_triple, p)
    if s.game.c6_triple.status == True:
        p = [590,918]
        screen.blit(double_triple, p)

    if s.game.tilt.status == False:
        if s.holes:
            if 1 in s.holes:
                p = [73,488]
                screen.blit(i, p)
                p = [273,467]
                screen.blit(i, p)
                p = [649,626]
                screen.blit(i, p)
                p = [110,778]
                screen.blit(i, p)
                p = [309,878]
                screen.blit(i, p)
                p = [612,846]
                screen.blit(i, p)
            if 2 in s.holes:
                p = [182,559]
                screen.blit(i, p)
                p = [311,536]
                screen.blit(i, p)
                p = [577,491]
                screen.blit(i, p)
                p = [145,878]
                screen.blit(i, p)
                p = [343,844]
                screen.blit(i, p)
                p = [647,780]
                screen.blit(i, p)            
            if 3 in s.holes:
                p = [109,623]
                screen.blit(i, p)
                p = [416,468]
                screen.blit(i, p)
                p = [508,491]
                screen.blit(i, p)
                p = [180,844]
                screen.blit(i, p)
                p = [377,877]
                screen.blit(i, p)
                p = [540,781]
                screen.blit(i, p)
            if 4 in s.holes:
                p = [36,555]
                screen.blit(i, p)
                p = [345,435]
                screen.blit(i, p)
                p = [507,525]
                screen.blit(i, p)
                p = [74,879]
                screen.blit(i, p)
                p = [415,811]
                screen.blit(i, p)
                p = [539,812]
                screen.blit(i, p)
            if 5 in s.holes:
                p = [39,491]
                screen.blit(i, p)
                p = [344,535]
                screen.blit(i, p)
                p = [577,625]
                screen.blit(i, p)
                p = [73,779]
                screen.blit(i, p)
                p = [413,845]
                screen.blit(i, p)
                p = [647,846]
                screen.blit(i, p)
            if 6 in s.holes:
                p = [181,591]
                screen.blit(i, p)
                p = [345,403]
                screen.blit(i, p)
                p = [612,524]
                screen.blit(i, p)
                p = [145,746]
                screen.blit(i, p)
                p = [413,779]
                screen.blit(i, p)
                p = [503,813]
                screen.blit(i, p)
            if 7 in s.holes:
                p = [73,623]
                screen.blit(i, p)
                p = [272,403]
                screen.blit(i, p)
                p = [576,591]
                screen.blit(i, p)
                p = [109,846]
                screen.blit(i, p)
                p = [307,779]
                screen.blit(i, p)
                p = [645,748]
                screen.blit(i, p)
            if 8 in s.holes:
                p = [109,524]
                screen.blit(i, p)
                p = [273,435]
                screen.blit(i, p)
                p = [649,491]
                screen.blit(i, p)
                p = [180,811]
                screen.blit(i, p)
                p = [307,812]
                screen.blit(i, p)
                p = [611,780]
                screen.blit(i, p)
            if 9 in s.holes:
                p = [180,491]
                screen.blit(i, p)
                p = [381,503]
                screen.blit(i, p)
                p = [507,560]
                screen.blit(i, p)
                p = [145,779]
                screen.blit(i, p)
                p = [273,749]
                screen.blit(i, p)
                p = [539,879]
                screen.blit(i, p)
            if 10 in s.holes:
                p = [146,557]
                screen.blit(i, p)
                p = [416,401]
                screen.blit(i, p)
                p = [649,559]
                screen.blit(i, p)
                p = [36,879]
                screen.blit(i, p)
                p = [377,780]
                screen.blit(i, p)
                p = [610,879]
                screen.blit(i, p)
            if 11 in s.holes:
                p = [109,590]
                screen.blit(i, p)
                p = [273,535]
                screen.blit(i, p)
                p = [541,592]
                screen.blit(i, p)
                p = [179,745]
                screen.blit(i, p)
                p = [307,845]
                screen.blit(i, p)
                p = [574,747]
                screen.blit(i, p)
            if 12 in s.holes:
                p = [37,623]
                screen.blit(i, p)
                p = [416,535]
                screen.blit(i, p)
                p = [541,491]
                screen.blit(i, p)
                p = [73,845]
                screen.blit(i, p)
                p = [377,845]
                screen.blit(i, p)
                p = [575,781]
                screen.blit(i, p)
            if 13 in s.holes:
                p = [37,523]
                screen.blit(i, p)
                p = [307,401]
                screen.blit(i, p)
                p = [505,625]
                screen.blit(i, p)
                p = [72,813]
                screen.blit(i, p)
                p = [341,778]
                screen.blit(i, p)
                p = [538,845]
                screen.blit(i, p)
            if 14 in s.holes:
                p = [109,491]
                screen.blit(i, p)
                p = [310,502]
                screen.blit(i, p)
                p = [613,558]
                screen.blit(i, p)
                p = [181,779]
                screen.blit(i, p)
                p = [343,747]
                screen.blit(i, p)
                p = [503,878]
                screen.blit(i, p)
            if 15 in s.holes:
                p = [73,524]
                screen.blit(i, p)
                p = [416,504]
                screen.blit(i, p)
                p = [575,526]
                screen.blit(i, p)
                p = [109,812]
                screen.blit(i, p)
                p = [377,747]
                screen.blit(i, p)
                p = [645,813]
                screen.blit(i, p)
            if 16 in s.holes:
                p = [145,590]
                screen.blit(i, p)
                p = [310,435]
                screen.blit(i, p)
                p = [507,592]
                screen.blit(i, p)
                p = [37,747]
                screen.blit(i, p)
                p = [342,813]
                screen.blit(i, p)
                p = [539,747]
                screen.blit(i, p)
            if 17 in s.holes:
                p = [145,492]
                screen.blit(i, p)
                p = [381,435]
                screen.blit(i, p)
                p = [540,525]
                screen.blit(i, p)
                p = [37,781]
                screen.blit(i, p)
                p = [272,813]
                screen.blit(i, p)
                p = [575,813]
                screen.blit(i, p)
            if 18 in s.holes:
                p = [182,624]
                screen.blit(i, p)
                p = [309,469]
                screen.blit(i, p)
                p = [540,558]
                screen.blit(i, p)
                p = [145,845]
                screen.blit(i, p)
                p = [342,878]
                screen.blit(i, p)
                p = [575,880]
                screen.blit(i, p)
            if 19 in s.holes:
                p = [73,557]
                screen.blit(i, p)
                p = [380,469]
                screen.blit(i, p)
                p = [613,591]
                screen.blit(i, p)
                p = [109,879]
                screen.blit(i, p)
                p = [271,877]
                screen.blit(i, p)
                p = [502,747]
                screen.blit(i, p)
            if 20 in s.holes:
                p = [73,591]
                screen.blit(i, p)
                p = [345,502]
                screen.blit(i, p)
                p = [648,525]
                screen.blit(i, p)
                p = [107,746]
                screen.blit(i, p)
                p = [411,747]
                screen.blit(i, p)
                p = [611,814]
                screen.blit(i, p)
            if 21 in s.holes:
                p = [143,525]
                screen.blit(i, p)
                p = [381,402]
                screen.blit(i, p)
                p = [611,624]
                screen.blit(i, p)
                p = [38,812]
                screen.blit(i, p)
                p = [272,778]
                screen.blit(i, p)
                p = [503,845]
                screen.blit(i, p)
            if 22 in s.holes:
                p = [144,624]
                screen.blit(i, p)
                p = [274,502]
                screen.blit(i, p)
                p = [541,627]
                screen.blit(i, p)
                p = [36,846]
                screen.blit(i, p)
                p = [305,749]
                screen.blit(i, p)
                p = [574,846]
                screen.blit(i, p)
            if 23 in s.holes:
                p = [109,557]
                screen.blit(i, p)
                p = [379,536]
                screen.blit(i, p)
                p = [647,592]
                screen.blit(i, p)
                p = [179,878]
                screen.blit(i, p)
                p = [272,845]
                screen.blit(i, p)
                p = [609,748]
                screen.blit(i, p)
            if 24 in s.holes:
                p = [181,525]
                screen.blit(i, p)
                p = [345,469]
                screen.blit(i, p)
                p = [612,491]
                screen.blit(i, p)
                p = [144,813]
                screen.blit(i, p)
                p = [411,878]
                screen.blit(i, p)
                p = [501,780]
                screen.blit(i, p)
            if 25 in s.holes:
                p = [37,590]
                screen.blit(i, p)
                p = [415,434]
                screen.blit(i, p)
                p = [575,558]
                screen.blit(i, p)
                p = [72,747]
                screen.blit(i, p)
                p = [376,813]
                screen.blit(i, p)
                p = [645,880]
                screen.blit(i, p)


    if s.game.fourteen_eighteen.status == True:
        p = [21,965]
        screen.blit(eb, p)

    if s.game.fifteen_seventeen.status == True:
        p = [487,965]
        screen.blit(eb, p)

    if s.game.sixteen.status == True:
        p = [256,965]
        screen.blit(eb, p)


    if s.game.tilt.status:
        tilt_position = [688,376]
        screen.blit(tilt, tilt_position)

    pygame.display.update()

def clear_mixers(s):
    global screen
    dirty_rects = []

    if s.game.fourteen_eighteen.status == False:
        dirty_rects.append(screen.blit(bg_gi, (21,965), pygame.Rect(21,965,209,59)))
    if s.game.fifteen_seventeen.status == False:
        dirty_rects.append(screen.blit(bg_gi, (487,965), pygame.Rect(487,965,209,59)))
    pygame.display.update(dirty_rects)
    return

def animate_mixer1(s):
    global screen
    dirty_rects = []
    if s.game.fourteen_eighteen.status == False:
        p = [21,965]
        dirty_rects.append(screen.blit(eb, p))
        pygame.display.update(dirty_rects)
        return

def animate_mixer2(s):
    global screen
    dirty_rects = []
    if s.game.fifteen_seventeen.status == False:
        p = [487,965]
        dirty_rects.append(screen.blit(eb, p))
    pygame.display.update(dirty_rects)
    return


def clear_features(s, num):
    global screen
    dirty_rects = []
    if s.game.c1_double.status == False:
        dirty_rects.append(screen.blit(bg_gi, (24,660), pygame.Rect(24,660,104,43)))
    if s.game.c2_double.status == False:
        dirty_rects.append(screen.blit(bg_gi, (261,573), pygame.Rect(261,573,104,43)))
    if s.game.c3_double.status == False:
        dirty_rects.append(screen.blit(bg_gi, (492,662), pygame.Rect(492,662,104,43)))
    if s.game.c4_double.status == False:
        dirty_rects.append(screen.blit(bg_gi, (27,918), pygame.Rect(27,918,104,43)))
    if s.game.c5_double.status == False:
        dirty_rects.append(screen.blit(bg_gi, (258,916), pygame.Rect(258,916,104,43)))
    if s.game.c6_double.status == False:
        dirty_rects.append(screen.blit(bg_gi, (490,916), pygame.Rect(490,916,104,43)))
    if s.game.c1_triple.status == False:
        dirty_rects.append(screen.blit(bg_gi, (124,662), pygame.Rect(124,662,104,43)))
    if s.game.c2_triple.status == False:
        dirty_rects.append(screen.blit(bg_gi, (363,573), pygame.Rect(363,573,104,43)))
    if s.game.c3_triple.status == False:
        dirty_rects.append(screen.blit(bg_gi, (592,664), pygame.Rect(592,664,104,43)))
    if s.game.c4_triple.status == False:
        dirty_rects.append(screen.blit(bg_gi, (124,916), pygame.Rect(124,916,104,43)))
    if s.game.c5_triple.status == False:
        dirty_rects.append(screen.blit(bg_gi, (360,916), pygame.Rect(360,916,104,43)))
    if s.game.c6_triple.status == False:
        dirty_rects.append(screen.blit(bg_gi, (590,918), pygame.Rect(590,918,104,43)))
    if s.game.sixteen.status == False:
        dirty_rects.append(screen.blit(bg_gi, (256,965), pygame.Rect(256,965,209,59)))
    pygame.display.update(dirty_rects)

def draw_feature_animation(s, num):
    global screen
    dirty_rects = []

    if num in [4,10]:
        if s.game.c1_double.status == False:
            p = [24,660]
            dirty_rects.append(screen.blit(double_triple, p))
            pygame.display.update(dirty_rects)
    if num in [0,11,22]:
        if s.game.c2_double.status == False:
            p = [261,573]
            dirty_rects.append(screen.blit(double_triple, p))
            pygame.display.update(dirty_rects)
    if num in [9,20,23]:
        if s.game.c3_double.status == False:
            p = [492,662]
            dirty_rects.append(screen.blit(double_triple, p))
            pygame.display.update(dirty_rects)
    if num in [1,12,24]:
        if s.game.c4_double.status == False:
            p = [27,918]
            dirty_rects.append(screen.blit(double_triple, p))
            pygame.display.update(dirty_rects)
    if num in [2,13]:
        if s.game.c5_double.status == False:
            p = [258,916]
            dirty_rects.append(screen.blit(double_triple, p))
            pygame.display.update(dirty_rects)
    if num in [3,14]:
        if s.game.c6_double.status == False:
            p = [490,916]
            dirty_rects.append(screen.blit(double_triple, p))
            pygame.display.update(dirty_rects)
    if num in [5,16]:
        if s.game.c1_triple.status == False:
            p = [124,662]
            dirty_rects.append(screen.blit(double_triple, p))
            pygame.display.update(dirty_rects)
    if num in [6,17]:
        if s.game.c2_triple.status == False:
            p = [363,573]
            dirty_rects.append(screen.blit(double_triple, p))
            pygame.display.update(dirty_rects)
    if num in [7,18]:
        if s.game.c3_triple.status == False:
            p = [592,664]
            dirty_rects.append(screen.blit(double_triple, p))
            pygame.display.update(dirty_rects)
    if num in [8,19]:
        if s.game.c4_triple.status == False:
            p = [124,916]
            dirty_rects.append(screen.blit(double_triple, p))
            pygame.display.update(dirty_rects)
    if num in [15,21]:
        if s.game.c5_triple.status == False:
            p = [360,916]
            dirty_rects.append(screen.blit(double_triple, p))
            pygame.display.update(dirty_rects)
    if num in [4,15]:
        if s.game.c6_triple.status == False:
            p = [590,918]
            dirty_rects.append(screen.blit(double_triple, p))
            pygame.display.update(dirty_rects)
    if num in [7,14,21,24]:
        if s.game.sixteen.status == False:
            p = [256,965]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)

def both_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]
    
    clear_features(s, num)
    
    if num % 2 == 0:
        clear_mixers(s)

    draw_feature_animation(s, num)
