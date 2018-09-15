
import pygame
import random

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

meter = pygame.image.load('graphics/assets/silver_register_cover.png').convert()
card = pygame.image.load('stars/assets/card.png').convert_alpha()
double = pygame.image.load('stars/assets/double.png').convert_alpha()
eb = pygame.image.load('stars/assets/arrow.png').convert_alpha()
exb = pygame.image.load('stars/assets/eb.png').convert_alpha()
ad = pygame.image.load('stars/assets/all_double.png').convert_alpha()
number = pygame.image.load('stars/assets/number.png').convert_alpha()
tilt = pygame.image.load('stars/assets/tilt.png').convert_alpha()
bg_menu = pygame.image.load('stars/assets/stars_menu.png')
bg_gi = pygame.image.load('stars/assets/stars_gi.png')
bg_off = pygame.image.load('stars/assets/stars_off.png')

class scorereel():
    """ Score Reels are used to count replays """
    def __init__(self, pos, image):
        self.position = pos
        self.default_y = self.position[1]
        self.image = pygame.image.load(image).convert()

reel1 = scorereel([123,769], "graphics/assets/green_reel.png")
reel10 = scorereel([104,769], "graphics/assets/green_reel.png")
reel100 = scorereel([85,769], "graphics/assets/green_reel.png")

def display(s, replays=0, menu=False):
    
    meter.set_colorkey((255,0,252))
    meter_position = [75,767]

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

    if s.game.selector.position >= 1:
        card_position = [99,247]
        screen.blit(card, card_position)
    if s.game.selector.position >= 2:
        card_position = [313,547]
        screen.blit(card, card_position)
    if s.game.selector.position >= 3:
        card_position = [525,247]
        screen.blit(card, card_position)

    if s.game.c1_double.status == True:
        c1d_position = [70,596]
        screen.blit(double, c1d_position)

    if s.game.c2_double.status == True:
        c2d_position = [282,894]
        screen.blit(double, c2d_position)

    if s.game.c3_double.status == True:
        c3d_position = [496,596]
        screen.blit(double, c3d_position)

    if s.game.extra_ball.position > 0:
        if s.game.extra_ball.position == 1:
            eb_position = [43,960]
            screen.blit(eb, eb_position)
        if s.game.extra_ball.position == 2:
            eb_position = [118,960]
            screen.blit(eb, eb_position)
        if s.game.extra_ball.position == 3:
            eb_position = [191,957]
            screen.blit(eb, eb_position)
        if s.game.extra_ball.position == 5:
            eb_position = [265,957]
            screen.blit(eb, eb_position)
        if s.game.extra_ball.position == 6:
            eb_position = [338,957]
            screen.blit(eb, eb_position)
        if s.game.extra_ball.position == 7:
            eb_position = [409,957]
            screen.blit(eb, eb_position)
        if s.game.extra_ball.position == 9:
            eb_position = [483,957]
            screen.blit(eb, eb_position)
        if s.game.extra_ball.position == 10:
            eb_position = [556,957]
            screen.blit(eb, eb_position)
        if s.game.extra_ball.position == 11:
            eb_position = [630,957]
            screen.blit(eb, eb_position)
        if s.game.extra_ball.position > 3 and s.game.extra_ball.position < 8:
            eb_position = [35,1000]
            screen.blit(exb, eb_position)
        if s.game.extra_ball.position > 7 and s.game.extra_ball.position < 12:
            eb_position = [255,1000]
            screen.blit(exb, eb_position)
        if s.game.extra_ball.position > 11:
            eb_position = [473,1000]
            screen.blit(exb, eb_position)

    if s.game.all_double.status == True:
        ad_position = [304,378]
        screen.blit(ad, ad_position)

    if s.game.tilt.status == False:
        if s.holes:
            if 1 in s.holes:
                number_position = [68,336]
                screen.blit(number, number_position)
                number_position = [232,792]
                screen.blit(number, number_position)
                number_position = [546,542]
                screen.blit(number, number_position)
            if 2 in s.holes:
                number_position = [118,542]
                screen.blit(number, number_position)
                number_position = [232,740]
                screen.blit(number, number_position)
                number_position = [648,438]
                screen.blit(number, number_position)
            if 3 in s.holes:
                number_position = [218,337]
                screen.blit(number, number_position)
                number_position = [430,842]
                screen.blit(number, number_position)
                number_position = [498,389]
                screen.blit(number, number_position)
            if 4 in s.holes:
                number_position = [220,542]
                screen.blit(number, number_position)
                number_position = [332,638]
                screen.blit(number, number_position)
                number_position = [598,334]
                screen.blit(number, number_position)
            if 5 in s.holes:
                number_position = [18,336]
                screen.blit(number, number_position)
                number_position = [332,842]
                screen.blit(number, number_position)
                number_position = [648,542]
                screen.blit(number, number_position)
            if 6 in s.holes:
                number_position = [18,438]
                screen.blit(number, number_position)
                number_position = [432,636]
                screen.blit(number, number_position)
                number_position = [494,492]
                screen.blit(number, number_position)
            if 7 in s.holes:
                number_position = [218,440]
                screen.blit(number, number_position)
                number_position = [282,842]
                screen.blit(number, number_position)
                number_position = [496,336]
                screen.blit(number, number_position)
            if 8 in s.holes:
                number_position = [18,386]
                screen.blit(number, number_position)
                number_position = [432,740]
                screen.blit(number, number_position)
                number_position = [648,386]
                screen.blit(number, number_position)
            if 9 in s.holes:
                number_position = [116,336]
                screen.blit(number, number_position)
                number_position = [234,638]
                screen.blit(number, number_position)
                number_position = [648,334]
                screen.blit(number, number_position)
            if 10 in s.holes:
                number_position = [117,388]
                screen.blit(number, number_position)
                number_position = [232,844]
                screen.blit(number, number_position)
                number_position = [546,336]
                screen.blit(number, number_position)
            if 11 in s.holes:
                number_position = [170,438]
                screen.blit(number, number_position)
                number_position = [332,792]
                screen.blit(number, number_position)
                number_position = [596,438]
                screen.blit(number, number_position)
            if 12 in s.holes:
                number_position = [18,540]
                screen.blit(number, number_position)
                number_position = [382,740]
                screen.blit(number, number_position)
                number_position = [546,490]
                screen.blit(number, number_position)
            if 13 in s.holes:
                number_position = [218,490]
                screen.blit(number, number_position)
                number_position = [232,688]
                screen.blit(number, number_position)
                number_position = [445,490]
                screen.blit(number, number_position)
            if 14 in s.holes:
                number_position = [116,490]
                screen.blit(number, number_position)
                number_position = [330,688]
                screen.blit(number, number_position)
                number_position = [496,438]
                screen.blit(number, number_position)
            if 15 in s.holes:
                number_position = [168,542]
                screen.blit(number, number_position)
                number_position = [330,740]
                screen.blit(number, number_position)
                number_position = [446,387]
                screen.blit(number, number_position)
            if 16 in s.holes:
                number_position = [116,438]
                screen.blit(number, number_position)
                number_position = [382,638]
                screen.blit(number, number_position)
                number_position = [596,542]
                screen.blit(number, number_position)
            if 17 in s.holes:
                number_position = [218,388]
                screen.blit(number, number_position)
                number_position = [431,792]
                screen.blit(number, number_position)
                number_position = [546,438]
                screen.blit(number, number_position)
            if 18 in s.holes:
                number_position = [66,438]
                screen.blit(number, number_position)
                number_position = [282,740]
                screen.blit(number, number_position)
                number_position = [546,386]
                screen.blit(number, number_position)
            if 19 in s.holes:
                number_position = [168,387]
                screen.blit(number, number_position)
                number_position = [281,688]
                screen.blit(number, number_position)
                number_position = [597,490]
                screen.blit(number, number_position)
            if 20 in s.holes:
                number_position = [168,490]
                screen.blit(number, number_position)
                number_position = [382,688]
                screen.blit(number, number_position)
                number_position = [444,544]
                screen.blit(number, number_position)
            if 21 in s.holes:
                number_position = [66,490]
                screen.blit(number, number_position)
                number_position = [382,791]
                screen.blit(number, number_position)
                number_position = [446,335]
                screen.blit(number, number_position)
            if 22 in s.holes:
                number_position = [68,386]
                screen.blit(number, number_position)
                number_position = [281,791]
                screen.blit(number, number_position)
                number_position = [597,387]
                screen.blit(number, number_position)
            if 23 in s.holes:
                number_position = [66,542]
                screen.blit(number, number_position)
                number_position = [380,842]
                screen.blit(number, number_position)
                number_position = [648,490]
                screen.blit(number, number_position)
            if 24 in s.holes:
                number_position = [18,490]
                screen.blit(number, number_position)
                number_position = [282,638]
                screen.blit(number, number_position)
                number_position = [446,440]
                screen.blit(number, number_position)
            if 25 in s.holes:
                number_position = [168,334]
                screen.blit(number, number_position)
                number_position = [432,687]
                screen.blit(number, number_position)
                number_position = [496,542]
                screen.blit(number, number_position)

    if s.game.tilt.status:
        tilt_position = [572,783]
        screen.blit(tilt, tilt_position)

    pygame.display.update()

def eb_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]


    if s.game.extra_ball.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (118,960), pygame.Rect(118,960,35,35)))
    if s.game.extra_ball.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (191,957), pygame.Rect(191,957,35,35)))
    if s.game.extra_ball.position < 4:
        dirty_rects.append(screen.blit(bg_gi, (35,1000), pygame.Rect(35,1000,203,32)))
    if s.game.extra_ball.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (265,957), pygame.Rect(265,957,35,35)))
    if s.game.extra_ball.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (338,957), pygame.Rect(338,957,35,35)))
    if s.game.extra_ball.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (409,957), pygame.Rect(409,957,35,35)))
    if s.game.extra_ball.position < 8:
        dirty_rects.append(screen.blit(bg_gi, (255,1000), pygame.Rect(255,1000,203,32)))
    if s.game.extra_ball.position != 9:
        dirty_rects.append(screen.blit(bg_gi, (483,957), pygame.Rect(483,957,35,35)))
    if s.game.extra_ball.position != 10:
        dirty_rects.append(screen.blit(bg_gi, (556,957), pygame.Rect(556,957,35,35)))
    if s.game.extra_ball.position != 11:
        dirty_rects.append(screen.blit(bg_gi, (630,957), pygame.Rect(630,957,35,35)))
    if s.game.extra_ball.position < 12:
        dirty_rects.append(screen.blit(bg_gi, (473,1000), pygame.Rect(473,1000,203,32)))
    pygame.display.update(dirty_rects)

    if num in [1,9,17]:
        if s.game.extra_ball.position != 2:
            p = [118,960]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects) 
    elif num in [2,10,18]:
        if s.game.extra_ball.position != 3:
            p = [191,957]
            dirty_rects.append(screen.blit(eb, p))
            p = [35,1000]
            dirty_rects.append(screen.blit(exb, p))
            pygame.display.update(dirty_rects)
    elif num in [3,11,18]:
        if s.game.extra_ball.position != 5:
            p = [265,957]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
    elif num in [4,12,20]:
        if s.game.extra_ball.position != 6:
            p = [338,957]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
    elif num in [5,13,21]:
        if s.game.extra_ball.position != 7:
            p = [409,957]
            dirty_rects.append(screen.blit(eb, p))
            p = [255,1000]
            dirty_rects.append(screen.blit(exb, p))
            pygame.display.update(dirty_rects)
    elif num in [6,14,22]:
        if s.game.extra_ball.position != 9:
            p = [483,957]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
    elif num in [7,15,23]:
        if s.game.extra_ball.position != 10:
            p = [556,957]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
    elif num in [8,16,24]:
        if s.game.extra_ball.position != 11:
            p = [630,957]
            dirty_rects.append(screen.blit(eb, p))
            p = [473,1000]
            dirty_rects.append(screen.blit(exb, p))
            pygame.display.update(dirty_rects)

def clear_mixers(s):
    global screen
    dirty_rects = []
    if s.game.c1_double.status == False:
        dirty_rects.append(screen.blit(bg_gi, (70,596), pygame.Rect(70,596,148,42)))
    if s.game.c2_double.status == False:
        dirty_rects.append(screen.blit(bg_gi, (282,894), pygame.Rect(282,894,148,42)))
    if s.game.c3_double.status == False:
        dirty_rects.append(screen.blit(bg_gi, (496,596), pygame.Rect(496,596,148,42)))
    if s.game.all_double.status == False:
        dirty_rects.append(screen.blit(bg_gi, (304,378), pygame.Rect(304,378,105,104)))
    pygame.display.update(dirty_rects)
    return

def animate_mixer1(s):
    global screen
    dirty_rects = []
    if s.game.c1_double.status == False:
        p = [70,596]
        dirty_rects.append(screen.blit(double, p))
        pygame.display.update(dirty_rects)
        return

def animate_mixer2(s):
    global screen
    dirty_rects = []
    if s.game.c2_double.status == False:
        p = [282,894]
        dirty_rects.append(screen.blit(double, p))
    pygame.display.update(dirty_rects)
    return

def animate_mixer3(s):
    global screen
    dirty_rects = []
    if s.game.c3_double.status == False:
        p = [496,596]
        dirty_rects.append(screen.blit(double, p))
    pygame.display.update(dirty_rects)
    return

def animate_mixer4(s):
    global screen
    dirty_rects = []
    if s.game.all_double.status == False:
        p = [304,378]
        dirty_rects.append(screen.blit(ad, p))
    pygame.display.update(dirty_rects)
    return

def clear_features(s, num):
    global screen
    dirty_rects = []
    if 14 not in s.holes:
        dirty_rects.append(screen.blit(bg_gi, (116,490), pygame.Rect(116,490,50,49)))
        dirty_rects.append(screen.blit(bg_gi, (330,688), pygame.Rect(330,688,50,49)))
        dirty_rects.append(screen.blit(bg_gi, (496,438), pygame.Rect(496,438,50,49)))
    if 15 not in s.holes:
        dirty_rects.append(screen.blit(bg_gi, (168,542), pygame.Rect(168,542,50,49)))
        dirty_rects.append(screen.blit(bg_gi, (330,740), pygame.Rect(330,740,50,49)))
        dirty_rects.append(screen.blit(bg_gi, (446,387), pygame.Rect(446,387,50,49)))
    if 16 not in s.holes:
        dirty_rects.append(screen.blit(bg_gi, (116,438), pygame.Rect(116,438,50,49)))
        dirty_rects.append(screen.blit(bg_gi, (382,638), pygame.Rect(382,638,50,49)))
        dirty_rects.append(screen.blit(bg_gi, (596,542), pygame.Rect(596,542,50,49)))
    if 17 not in s.holes:
        dirty_rects.append(screen.blit(bg_gi, (218,388), pygame.Rect(218,388,50,49)))
        dirty_rects.append(screen.blit(bg_gi, (431,792), pygame.Rect(431,792,50,49)))
        dirty_rects.append(screen.blit(bg_gi, (546,438), pygame.Rect(546,438,50,49)))
    if 19 not in s.holes:
        dirty_rects.append(screen.blit(bg_gi, (168,387), pygame.Rect(168,387,50,49)))
        dirty_rects.append(screen.blit(bg_gi, (281,688), pygame.Rect(281,688,50,49)))
        dirty_rects.append(screen.blit(bg_gi, (597,490), pygame.Rect(597,490,50,49)))
    if 22 not in s.holes:
        dirty_rects.append(screen.blit(bg_gi, (68,386), pygame.Rect(68,386,50,49)))
        dirty_rects.append(screen.blit(bg_gi, (281,791), pygame.Rect(281,791,50,49)))
        dirty_rects.append(screen.blit(bg_gi, (597,387), pygame.Rect(597,387,50,49)))

    pygame.display.update(dirty_rects)

def draw_feature_animation(s, num):
    global screen
    dirty_rects = []
 
    if num in [1,13]:
        if 14 not in s.holes:
            p = [116,490]
            dirty_rects.append(screen.blit(number, p))
            p = [330,688]
            dirty_rects.append(screen.blit(number, p))
            p = [496,438]
            dirty_rects.append(screen.blit(number, p))
            pygame.display.update(dirty_rects)
            return
    if num in [3,15]:
        if 15 not in s.holes:
            p = [168,542]
            dirty_rects.append(screen.blit(number, p))
            p = [330,740]
            dirty_rects.append(screen.blit(number, p))
            p = [446,387]
            dirty_rects.append(screen.blit(number, p))
            pygame.display.update(dirty_rects)
            return
    if num in [5,17]:
        if 16 not in s.holes:
            p = [116,438]
            dirty_rects.append(screen.blit(number, p))
            p = [382,638]
            dirty_rects.append(screen.blit(number, p))
            p = [596,542]
            dirty_rects.append(screen.blit(number, p))
            pygame.display.update(dirty_rects)
            return
    if num in [7,19]:
        if 17 not in s.holes:
            p = [218,388]
            dirty_rects.append(screen.blit(number, p))
            p = [431,792]
            dirty_rects.append(screen.blit(number, p))
            p = [546,438]
            dirty_rects.append(screen.blit(number, p))
            pygame.display.update(dirty_rects)
            return
    if num in [9,21]:
        if 19 not in s.holes:
            p = [168,387]
            dirty_rects.append(screen.blit(number, p))
            p = [281,688]
            dirty_rects.append(screen.blit(number, p))
            p = [597,490]
            dirty_rects.append(screen.blit(number, p))
            pygame.display.update(dirty_rects)
            return
    if num in [11,23]:
        if 22 not in s.holes:
            p = [68,386]
            dirty_rects.append(screen.blit(number, p))
            p = [281,791]
            dirty_rects.append(screen.blit(number, p))
            p = [597,387]
            dirty_rects.append(screen.blit(number, p))
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

    if num % 2 == 0:
        clear_mixers(s)

    draw_feature_animation(s, num)

