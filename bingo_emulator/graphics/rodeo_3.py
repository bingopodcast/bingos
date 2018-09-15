
import pygame
import random

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

meter = pygame.image.load('graphics/assets/silver_register_cover.png').convert()
card = pygame.image.load('rodeo_3/assets/card.png').convert_alpha()
double_triple = pygame.image.load('rodeo_3/assets/double_triple.png').convert_alpha()
extra_ball = pygame.image.load('rodeo_3/assets/eb.png').convert_alpha()
eb = pygame.image.load('rodeo_3/assets/extra_ball.png').convert_alpha()
ad = pygame.image.load('rodeo_3/assets/feature.png').convert_alpha()
number = pygame.image.load('rodeo_3/assets/number.png').convert_alpha()
tilt = pygame.image.load('rodeo_3/assets/tilt.png').convert_alpha()
bg_menu = pygame.image.load('rodeo_3/assets/rodeo_3_menu.png')
bg_gi = pygame.image.load('rodeo_3/assets/rodeo_3_gi.png')
bg_off = pygame.image.load('rodeo_3/assets/rodeo_3_off.png')

class scorereel():
    """ Score Reels are used to count replays """
    def __init__(self, pos, image):
        self.position = pos
        self.default_y = self.position[1]
        self.image = pygame.image.load(image).convert()

reel1 = scorereel([128,744], "graphics/assets/white_reel.png")
reel10 = scorereel([109,744], "graphics/assets/white_reel.png")
reel100 = scorereel([90,744], "graphics/assets/white_reel.png")

def display(s, replays=0, menu=False):
    
    meter.set_colorkey((255,0,252))
    meter_position = [81,744]

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
        card_position = [74,296]
        screen.blit(card, card_position)
    if s.game.selector.position >= 2:
        card_position = [287,551]
        screen.blit(card, card_position)
    if s.game.selector.position >= 3:
        card_position = [497,295]
        screen.blit(card, card_position)

    if s.game.c1_double.status == True:
        c1d_position = [60,604]
        screen.blit(double_triple, c1d_position)

    if s.game.c2_double.status == True:
        c2d_position = [275,859]
        screen.blit(double_triple, c2d_position)

    if s.game.c3_double.status == True:
        c3d_position = [489,604]
        screen.blit(double_triple, c3d_position)

    if s.game.c1_triple.status == True:
        c1d_position = [148,603]
        screen.blit(double_triple, c1d_position)

    if s.game.c2_triple.status == True:
        c2d_position = [360,858]
        screen.blit(double_triple, c2d_position)

    if s.game.c3_triple.status == True:
        c3d_position = [575,602]
        screen.blit(double_triple, c3d_position)

    if s.game.extra_ball.position == 1 or s.game.extra_ball.position == 10 or s.game.extra_ball.position == 19:
        eb_position = [48,898]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 2 or s.game.extra_ball.position == 11 or s.game.extra_ball.position == 20:
        eb_position = [120,897]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 3 or s.game.extra_ball.position == 12 or s.game.extra_ball.position == 21:
        eb_position = [195,896]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 4 or s.game.extra_ball.position == 13 or s.game.extra_ball.position == 22:
        eb_position = [265,897]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 5 or s.game.extra_ball.position == 14 or s.game.extra_ball.position == 23:
        eb_position = [337,897]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 6 or s.game.extra_ball.position == 15:
        eb_position = [410,897]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 7 or s.game.extra_ball.position == 16:
        eb_position = [481,898]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 8 or s.game.extra_ball.position == 17:
        eb_position = [553,898]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 9 or s.game.extra_ball.position == 18:
        eb_position = [623,898]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position > 8 and s.game.extra_ball.position < 18:
        eb_position = [45,943]
        screen.blit(extra_ball, eb_position)
    if s.game.extra_ball.position > 17 and s.game.extra_ball.position < 24:
        eb_position = [262,944]
        screen.blit(extra_ball, eb_position)
    if s.game.extra_ball.position > 23:
        eb_position = [478,943]
        screen.blit(extra_ball, eb_position)


    if s.game.fss.status == True:
        ad_position = [283,467]
        screen.blit(ad, ad_position)

    if s.game.fnt.status == True:
        ad_position = [283,509]
        screen.blit(ad, ad_position)

    if s.game.all_double.status == True:
        ad_position = [283,392]
        screen.blit(ad, ad_position)

    if s.game.all_triple.status == True:
        ad_position = [283,431]
        screen.blit(ad, ad_position)

    if s.game.tilt.status == False:
        if s.holes:
            if 1 in s.holes:
                number_position = [76,382]
                screen.blit(number, number_position)
                number_position = [242,769]
                screen.blit(number, number_position)
                number_position = [551,556]
                screen.blit(number, number_position)
            if 2 in s.holes:
                number_position = [126,556]
                screen.blit(number, number_position)
                number_position = [242,724]
                screen.blit(number, number_position)
                number_position = [651,469]
                screen.blit(number, number_position)
            if 3 in s.holes:
                number_position = [226,381]
                screen.blit(number, number_position)
                number_position = [440,812]
                screen.blit(number, number_position)
                number_position = [501,424]
                screen.blit(number, number_position)
            if 4 in s.holes:
                number_position = [226,556]
                screen.blit(number, number_position)
                number_position = [340,636]
                screen.blit(number, number_position)
                number_position = [600,381]
                screen.blit(number, number_position)
            if 5 in s.holes:
                number_position = [25,382]
                screen.blit(number, number_position)
                number_position = [340,812]
                screen.blit(number, number_position)
                number_position = [652,556]
                screen.blit(number, number_position)
            if 6 in s.holes:
                number_position = [28,468]
                screen.blit(number, number_position)
                number_position = [440,636]
                screen.blit(number, number_position)
                number_position = [502,512]
                screen.blit(number, number_position)
            if 7 in s.holes:
                number_position = [226,468]
                screen.blit(number, number_position)
                number_position = [290,812]
                screen.blit(number, number_position)
                number_position = [500,381]
                screen.blit(number, number_position)
            if 8 in s.holes:
                number_position = [27,424]
                screen.blit(number, number_position)
                number_position = [441,724]
                screen.blit(number, number_position)
                number_position = [652,424]
                screen.blit(number, number_position)
            if 9 in s.holes:
                number_position = [126,382]
                screen.blit(number, number_position)
                number_position = [240,636]
                screen.blit(number, number_position)
                number_position = [652,380]
                screen.blit(number, number_position)
            if 10 in s.holes:
                number_position = [126,424]
                screen.blit(number, number_position)
                number_position = [241,811]
                screen.blit(number, number_position)
                number_position = [551,380]
                screen.blit(number, number_position)
            if 11 in s.holes:
                number_position = [176,468]
                screen.blit(number, number_position)
                number_position = [341,768]
                screen.blit(number, number_position)
                number_position = [601,468]
                screen.blit(number, number_position)
            if 12 in s.holes:
                number_position = [28,557]
                screen.blit(number, number_position)
                number_position = [390,724]
                screen.blit(number, number_position)
                number_position = [551,512]
                screen.blit(number, number_position)
            if 13 in s.holes:
                number_position = [226,512]
                screen.blit(number, number_position)
                number_position = [240,680]
                screen.blit(number, number_position)
                number_position = [452,511]
                screen.blit(number, number_position)
            if 14 in s.holes:
                number_position = [126,512]
                screen.blit(number, number_position)
                number_position = [340,680]
                screen.blit(number, number_position)
                number_position = [502,468]
                screen.blit(number, number_position)
            if 15 in s.holes:
                number_position = [178,556]
                screen.blit(number, number_position)
                number_position = [340,724]
                screen.blit(number, number_position)
                number_position = [452,424]
                screen.blit(number, number_position)
            if 16 in s.holes:
                number_position = [126,468]
                screen.blit(number, number_position)
                number_position = [390,636]
                screen.blit(number, number_position)
                number_position = [602,556]
                screen.blit(number, number_position)
            if 17 in s.holes:
                number_position = [226,424]
                screen.blit(number, number_position)
                number_position = [440,767]
                screen.blit(number, number_position)
                number_position = [552,468]
                screen.blit(number, number_position)
            if 18 in s.holes:
                number_position = [76,469]
                screen.blit(number, number_position)
                number_position = [291,724]
                screen.blit(number, number_position)
                number_position = [552,424]
                screen.blit(number, number_position)
            if 19 in s.holes:
                number_position = [176,424]
                screen.blit(number, number_position)
                number_position = [290,680]
                screen.blit(number, number_position)
                number_position = [602,512]
                screen.blit(number, number_position)
            if 20 in s.holes:
                number_position = [177,512]
                screen.blit(number, number_position)
                number_position = [390,680]
                screen.blit(number, number_position)
                number_position = [452,556]
                screen.blit(number, number_position)
            if 21 in s.holes:
                number_position = [76,513]
                screen.blit(number, number_position)
                number_position = [392,768]
                screen.blit(number, number_position)
                number_position = [452,382]
                screen.blit(number, number_position)
            if 22 in s.holes:
                number_position = [75,424]
                screen.blit(number, number_position)
                number_position = [291,768]
                screen.blit(number, number_position)
                number_position = [602,424]
                screen.blit(number, number_position)
            if 23 in s.holes:
                number_position = [77,558]
                screen.blit(number, number_position)
                number_position = [390,812]
                screen.blit(number, number_position)
                number_position = [652,512]
                screen.blit(number, number_position)
            if 24 in s.holes:
                number_position = [28,513]
                screen.blit(number, number_position)
                number_position = [290,638]
                screen.blit(number, number_position)
                number_position = [452,468]
                screen.blit(number, number_position)
            if 25 in s.holes:
                number_position = [176,381]
                screen.blit(number, number_position)
                number_position = [440,680]
                screen.blit(number, number_position)
                number_position = [502,556]
                screen.blit(number, number_position)

    if s.game.tilt.status:
        tilt_position = [644,296]
        screen.blit(tilt, tilt_position)

    pygame.display.update()

def eb_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]

    if s.game.extra_ball.position not in [2,11,20]:
        dirty_rects.append(screen.blit(bg_gi, (120,897), pygame.Rect(120,897,47,44)))
    if s.game.extra_ball.position not in [3,12,21]:
        dirty_rects.append(screen.blit(bg_gi, (195,896), pygame.Rect(195,896,47,44)))
    if s.game.extra_ball.position not in [4,13,22]:
        dirty_rects.append(screen.blit(bg_gi, (265,897), pygame.Rect(265,897,47,44)))
    if s.game.extra_ball.position not in [5,14,23]:
        dirty_rects.append(screen.blit(bg_gi, (337,897), pygame.Rect(337,897,47,44)))
    if s.game.extra_ball.position not in [6,15]:
        dirty_rects.append(screen.blit(bg_gi, (410,897), pygame.Rect(410,897,47,44)))
    if s.game.extra_ball.position not in [7,16]:
        dirty_rects.append(screen.blit(bg_gi, (481,898), pygame.Rect(481,898,47,44)))
    if s.game.extra_ball.position not in [8,17]:
        dirty_rects.append(screen.blit(bg_gi, (553,898), pygame.Rect(553,898,47,44)))
    if s.game.extra_ball.position not in [9,18]:
        dirty_rects.append(screen.blit(bg_gi, (623,898), pygame.Rect(623,898,47,44)))
    if s.game.extra_ball.position < 8:
        dirty_rects.append(screen.blit(bg_gi, (45,943), pygame.Rect(45,943,201,33)))
    if s.game.extra_ball.position < 17:
        dirty_rects.append(screen.blit(bg_gi, (262,944), pygame.Rect(262,944,201,33)))
    if s.game.extra_ball.position < 24:
        dirty_rects.append(screen.blit(bg_gi, (478,943), pygame.Rect(478,943,201,33)))
    pygame.display.update(dirty_rects)
    if num in [1,9,17]:
        if s.game.extra_ball.position not in [2,11,20]:
            p = [120,897]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects) 
    elif num in [2,10,18]:
        if s.game.extra_ball.position not in [3,12,21]:
            p = [195,896]
            dirty_rects.append(screen.blit(eb, p))
            if s.game.extra_ball.position not in range(8,19):
                p = [45,943]
                screen.blit(extra_ball, p)
            pygame.display.update(dirty_rects)
    elif num in [3,11,18]:
        if s.game.extra_ball.position not in [4,13,22]:
            p = [265,897]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
    elif num in [4,12,20]:
        if s.game.extra_ball.position not in [5,14,23]:
            p = [337,897]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
    elif num in [5,13,21]:
        if s.game.extra_ball.position not in [6,15]:
            p = [410,897]
            dirty_rects.append(screen.blit(eb, p))
            if s.game.extra_ball.position not in range(17,25):
                p = [262,944]
                screen.blit(extra_ball, p)
            pygame.display.update(dirty_rects)
    elif num in [6,14,22]:
        if s.game.extra_ball.position not in [7,16]:
            p = [481,898]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
    elif num in [7,15,23]:
        if s.game.extra_ball.position not in [8,17]:
            p = [553,898]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
    elif num in [8,16,24]:
        if s.game.extra_ball.position not in [9,18]:
            p = [623,898]
            dirty_rects.append(screen.blit(eb, p))
            if s.game.extra_ball.position != 24:
                p = [478,943]
                screen.blit(extra_ball, p)
            pygame.display.update(dirty_rects)

def clear_mixers(s):
    global screen
    dirty_rects = []

    if s.game.c1_double.status == False:
        dirty_rects.append(screen.blit(bg_gi, (60,604), pygame.Rect(60,604,86,36)))
    if s.game.c2_double.status == False:
        dirty_rects.append(screen.blit(bg_gi, (275,859), pygame.Rect(275,859,86,36)))
    if s.game.c3_double.status == False:
        dirty_rects.append(screen.blit(bg_gi, (489,604), pygame.Rect(489,604,86,36)))
    if s.game.c1_triple.status == False:
        dirty_rects.append(screen.blit(bg_gi, (148,603), pygame.Rect(148,603,86,36)))
    if s.game.c2_triple.status == False:
        dirty_rects.append(screen.blit(bg_gi, (360,858), pygame.Rect(360,858,86,36)))
    if s.game.c3_triple.status == False:
        dirty_rects.append(screen.blit(bg_gi, (575,602), pygame.Rect(575,602,86,36)))
    if s.game.fss.status == False:
        dirty_rects.append(screen.blit(bg_gi, (283,467), pygame.Rect(283,467,153,42)))
    if s.game.fnt.status == False:
        dirty_rects.append(screen.blit(bg_gi, (283,509), pygame.Rect(283,509,153,42)))
    if s.game.all_double.status == False:
        dirty_rects.append(screen.blit(bg_gi, (283,392), pygame.Rect(283,392,153,42)))
    if s.game.all_triple.status == False:
        dirty_rects.append(screen.blit(bg_gi, (283,431), pygame.Rect(283,431,153,42)))
    pygame.display.update(dirty_rects)
    return

def animate_mixer1(s):
    global screen
    dirty_rects = []

    if s.game.c1_double.status == False:
        p = [60,604]
        dirty_rects.append(screen.blit(double_triple, p))
    if s.game.c2_triple.status == False:
        p = [360,858]
        dirty_rects.append(screen.blit(double_triple, p))
    if s.game.fss.status == False:
        p = [283,467]
        dirty_rects.append(screen.blit(ad, p))
    pygame.display.update(dirty_rects)
    return

def animate_mixer2(s):
    global screen
    dirty_rects = []
    if s.game.c2_double.status == False:
        p = [275,859]
        dirty_rects.append(screen.blit(double_triple, p))
    if s.game.c3_triple.status == False:
        p = [575,602]
        dirty_rects.append(screen.blit(double_triple, p))
    if s.game.fnt.status == False:
        p = [283,509]
        dirty_rects.append(screen.blit(ad, p))
    pygame.display.update(dirty_rects)
    return

def animate_mixer3(s):
    global screen
    dirty_rects = []

    if s.game.c3_double.status == False:
        p = [489,604]
        dirty_rects.append(screen.blit(double_triple, p))
    if s.game.all_triple.status == False:
        p = [283,431]
        dirty_rects.append(screen.blit(ad, p))
    pygame.display.update(dirty_rects)
    return

def animate_mixer4(s):
    global screen
    dirty_rects = []

    if s.game.all_double.status == False:
        p = [283,392]
        dirty_rects.append(screen.blit(ad, p))
    if s.game.c1_triple.status == False:
        p = [148,603]
        dirty_rects.append(screen.blit(double_triple, p))
    pygame.display.update(dirty_rects)
    return

def clear_features(s, num):
    global screen
    dirty_rects = []
    if 14 not in s.holes:
        dirty_rects.append(screen.blit(bg_gi, (126,512), pygame.Rect(126,512,46,44)))
        dirty_rects.append(screen.blit(bg_gi, (340,680), pygame.Rect(340,680,46,44)))
        dirty_rects.append(screen.blit(bg_gi, (502,468), pygame.Rect(502,468,46,44)))
    if 15 not in s.holes:
        dirty_rects.append(screen.blit(bg_gi, (178,556), pygame.Rect(178,556,46,44)))
        dirty_rects.append(screen.blit(bg_gi, (340,724), pygame.Rect(340,724,46,44)))
        dirty_rects.append(screen.blit(bg_gi, (452,424), pygame.Rect(452,424,46,44)))
    if 16 not in s.holes:
        dirty_rects.append(screen.blit(bg_gi, (126,468), pygame.Rect(126,468,46,44)))
        dirty_rects.append(screen.blit(bg_gi, (390,636), pygame.Rect(390,636,46,44)))
        dirty_rects.append(screen.blit(bg_gi, (602,556), pygame.Rect(602,556,46,44)))
    if 17 not in s.holes:
        dirty_rects.append(screen.blit(bg_gi, (226,424), pygame.Rect(226,424,46,44)))
        dirty_rects.append(screen.blit(bg_gi, (440,767), pygame.Rect(440,767,46,44)))
        dirty_rects.append(screen.blit(bg_gi, (552,468), pygame.Rect(552,468,46,44)))
    if 19 not in s.holes:
        dirty_rects.append(screen.blit(bg_gi, (176,424), pygame.Rect(176,424,46,44)))
        dirty_rects.append(screen.blit(bg_gi, (290,680), pygame.Rect(290,680,46,44)))
        dirty_rects.append(screen.blit(bg_gi, (602,512), pygame.Rect(602,512,46,44)))
    if 22 not in s.holes:
        dirty_rects.append(screen.blit(bg_gi, (75,424), pygame.Rect(75,424,46,44)))
        dirty_rects.append(screen.blit(bg_gi, (291,768), pygame.Rect(291,768,46,44)))
        dirty_rects.append(screen.blit(bg_gi, (602,424), pygame.Rect(602,424,46,44)))

    pygame.display.update(dirty_rects)

def draw_feature_animation(s, num):
    global screen
    dirty_rects = []
    if num in [1,13]:
        if 14 not in s.holes:
            p = [126,512]
            dirty_rects.append(screen.blit(number, p))
            p = [340,680]
            dirty_rects.append(screen.blit(number, p))
            p = [502,468]
            dirty_rects.append(screen.blit(number, p))
            pygame.display.update(dirty_rects)
            return
    if num in [3,15]:
        if 15 not in s.holes:
            p = [178,556]
            dirty_rects.append(screen.blit(number, p))
            p = [340,724]
            dirty_rects.append(screen.blit(number, p))
            p = [452,424]
            dirty_rects.append(screen.blit(number, p))
            pygame.display.update(dirty_rects)
            return
    if num in [5,17]:
        if 16 not in s.holes:
            p = [126,468]
            dirty_rects.append(screen.blit(number, p))
            p = [390,636]
            dirty_rects.append(screen.blit(number, p))
            p = [602,556]
            dirty_rects.append(screen.blit(number, p))
            pygame.display.update(dirty_rects)
            return
    if num in [7,19]:
        if 17 not in s.holes:
            p = [226,424]
            dirty_rects.append(screen.blit(number, p))
            p = [440,767]
            dirty_rects.append(screen.blit(number, p))
            p = [552,468]
            dirty_rects.append(screen.blit(number, p))
            pygame.display.update(dirty_rects)
            return
    if num in [9,21]:
        if 19 not in s.holes:
            p = [176,424]
            dirty_rects.append(screen.blit(number, p))
            p = [290,680]
            dirty_rects.append(screen.blit(number, p))
            p = [602,512]
            dirty_rects.append(screen.blit(number, p))
            pygame.display.update(dirty_rects)
            return
    if num in [11,23]:
        if 22 not in s.holes:
            p = [75,424]
            dirty_rects.append(screen.blit(number, p))
            p = [291,768]
            dirty_rects.append(screen.blit(number, p))
            p = [602,424]
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

