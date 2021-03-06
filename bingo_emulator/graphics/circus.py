
import pygame
import random

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

meter = pygame.image.load('graphics/assets/silver_register_cover.png').convert()
card = pygame.image.load('circus/assets/card.png').convert_alpha()
rt_flag = pygame.image.load('circus/assets/rt_flag.png').convert_alpha()
lt_flag = pygame.image.load('circus/assets/lt_flag.png').convert_alpha()
eb = pygame.image.load('circus/assets/eb.png').convert_alpha()
extra_ball = pygame.image.load('circus/assets/extra_ball.png').convert_alpha()
ad = pygame.image.load('circus/assets/options.png').convert_alpha()
number = pygame.image.load('circus/assets/number.png').convert_alpha()
tilt = pygame.image.load('circus/assets/tilt.png').convert_alpha()
bg_menu = pygame.image.load('circus/assets/circus_menu.png')
bg_gi = pygame.image.load('circus/assets/circus_gi.png')
bg_off = pygame.image.load('circus/assets/circus_off.png')

class scorereel():
    """ Score Reels are used to count replays """
    def __init__(self, pos, image):
        self.position = pos
        self.default_y = self.position[1]
        self.image = pygame.image.load(image).convert()

reel1 = scorereel([123,769], "graphics/assets/white_reel.png")
reel10 = scorereel([104,769], "graphics/assets/white_reel.png")
reel100 = scorereel([85,769], "graphics/assets/white_reel.png")

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
        if (s.game.lock.status == True):
            screen.blit(bg_gi, backglass_position)
        else:
            screen.blit(bg_off, backglass_position)

    if s.game.selector.position >= 1:
        card_position = [94,258]
        screen.blit(card, card_position)
    if s.game.selector.position >= 2:
        card_position = [308,552]
        screen.blit(card, card_position)
    if s.game.selector.position >= 3:
        card_position = [524,258]
        screen.blit(card, card_position)

    if s.game.c1_double.status == True:
        c1d_position = [20,598]
        c1d = pygame.transform.scale(rt_flag, (112, 38))
        screen.blit(c1d, c1d_position)

    if s.game.c2_double.status == True:
        c2d_position = [242,886]
        c2d = pygame.transform.scale(rt_flag, (112, 38))
        screen.blit(c2d, c2d_position)

    if s.game.c3_double.status == True:
        c3d_position = [478,597]
        screen.blit(lt_flag, c3d_position)

    if s.game.c1_triple.status == True:
        c1d_position = [136,598]
        screen.blit(rt_flag, c1d_position)

    if s.game.c2_triple.status == True:
        c2d_position = [364,884]
        screen.blit(lt_flag, c2d_position)

    if s.game.c3_triple.status == True:
        c3d_position = [586,597]
        screen.blit(lt_flag, c3d_position)

    if s.game.extra_ball.position == 1 or s.game.extra_ball.position == 10 or s.game.extra_ball.position == 19:
        eb_position = [51,943]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 2 or s.game.extra_ball.position == 11 or s.game.extra_ball.position == 20:
        eb_position = [123,940]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 3 or s.game.extra_ball.position == 12 or s.game.extra_ball.position == 21:
        eb_position = [197,940]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 4 or s.game.extra_ball.position == 13 or s.game.extra_ball.position == 22:
        eb_position = [269,940]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 5 or s.game.extra_ball.position == 14 or s.game.extra_ball.position == 23:
        eb_position = [342,940]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 6 or s.game.extra_ball.position == 15:
        eb_position = [413,940]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 7 or s.game.extra_ball.position == 16:
        eb_position = [486,940]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 8 or s.game.extra_ball.position == 17:
        eb_position = [556,940]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 9 or s.game.extra_ball.position == 18:
        eb_position = [629,944]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position > 8 and s.game.extra_ball.position < 18:
        eb_position = [40,985]
        screen.blit(extra_ball, eb_position)
    if s.game.extra_ball.position > 17 and s.game.extra_ball.position < 24:
        eb_position = [257,981]
        screen.blit(extra_ball, eb_position)
    if s.game.extra_ball.position > 23:
        eb_position = [472,983]
        screen.blit(extra_ball, eb_position)


    if s.game.fss.status == True:
        ad_position = [284,456]
        screen.blit(ad, ad_position)

    if s.game.fnt.status == True:
        ad_position = [284,499]
        screen.blit(ad, ad_position)

    if s.game.all_double.status == True:
        ad_position = [284,369]
        screen.blit(ad, ad_position)

    if s.game.all_triple.status == True:
        ad_position = [284,413]
        screen.blit(ad, ad_position)

    if s.game.tilt.status == False:
        if s.holes:
            if 1 in s.holes:
                number_position = [68,350]
                screen.blit(number, number_position)
                number_position = [235,786]
                screen.blit(number, number_position)
                number_position = [546,549]
                screen.blit(number, number_position)
            if 2 in s.holes:
                number_position = [120,548]
                screen.blit(number, number_position)
                number_position = [235,735]
                screen.blit(number, number_position)
                number_position = [647,447]
                screen.blit(number, number_position)
            if 3 in s.holes:
                number_position = [219,348]
                screen.blit(number, number_position)
                number_position = [434,834]
                screen.blit(number, number_position)
                number_position = [495,399]
                screen.blit(number, number_position)
            if 4 in s.holes:
                number_position = [222,547]
                screen.blit(number, number_position)
                number_position = [334,639]
                screen.blit(number, number_position)
                number_position = [597,348]
                screen.blit(number, number_position)
            if 5 in s.holes:
                number_position = [18,348]
                screen.blit(number, number_position)
                number_position = [334,836]
                screen.blit(number, number_position)
                number_position = [645,548]
                screen.blit(number, number_position)
            if 6 in s.holes:
                number_position = [21,448]
                screen.blit(number, number_position)
                number_position = [434,639]
                screen.blit(number, number_position)
                number_position = [496,498]
                screen.blit(number, number_position)
            if 7 in s.holes:
                number_position = [222,450]
                screen.blit(number, number_position)
                number_position = [284,834]
                screen.blit(number, number_position)
                number_position = [495,348]
                screen.blit(number, number_position)
            if 8 in s.holes:
                number_position = [18,399]
                screen.blit(number, number_position)
                number_position = [435,738]
                screen.blit(number, number_position)
                number_position = [648,396]
                screen.blit(number, number_position)
            if 9 in s.holes:
                number_position = [118,346]
                screen.blit(number, number_position)
                number_position = [236,639]
                screen.blit(number, number_position)
                number_position = [646,348]
                screen.blit(number, number_position)
            if 10 in s.holes:
                number_position = [122,399]
                screen.blit(number, number_position)
                number_position = [237,836]
                screen.blit(number, number_position)
                number_position = [548,350]
                screen.blit(number, number_position)
            if 11 in s.holes:
                number_position = [171,448]
                screen.blit(number, number_position)
                number_position = [334,784]
                screen.blit(number, number_position)
                number_position = [598,447]
                screen.blit(number, number_position)
            if 12 in s.holes:
                number_position = [22,549]
                screen.blit(number, number_position)
                number_position = [385,736]
                screen.blit(number, number_position)
                number_position = [545,500]
                screen.blit(number, number_position)
            if 13 in s.holes:
                number_position = [221,500]
                screen.blit(number, number_position)
                number_position = [235,687]
                screen.blit(number, number_position)
                number_position = [446,498]
                screen.blit(number, number_position)
            if 14 in s.holes:
                number_position = [123,500]
                screen.blit(number, number_position)
                number_position = [334,688]
                screen.blit(number, number_position)
                number_position = [496,450]
                screen.blit(number, number_position)
            if 15 in s.holes:
                number_position = [174,549]
                screen.blit(number, number_position)
                number_position = [334,736]
                screen.blit(number, number_position)
                number_position = [446,400]
                screen.blit(number, number_position)
            if 16 in s.holes:
                number_position = [122,450]
                screen.blit(number, number_position)
                number_position = [382,639]
                screen.blit(number, number_position)
                number_position = [594,548]
                screen.blit(number, number_position)
            if 17 in s.holes:
                number_position = [220,399]
                screen.blit(number, number_position)
                number_position = [433,786]
                screen.blit(number, number_position)
                number_position = [547,450]
                screen.blit(number, number_position)
            if 18 in s.holes:
                number_position = [70,448]
                screen.blit(number, number_position)
                number_position = [285,738]
                screen.blit(number, number_position)
                number_position = [548,398]
                screen.blit(number, number_position)
            if 19 in s.holes:
                number_position = [172,398]
                screen.blit(number, number_position)
                number_position = [284,687]
                screen.blit(number, number_position)
                number_position = [596,498]
                screen.blit(number, number_position)
            if 20 in s.holes:
                number_position = [171,498]
                screen.blit(number, number_position)
                number_position = [384,688]
                screen.blit(number, number_position)
                number_position = [447,550]
                screen.blit(number, number_position)
            if 21 in s.holes:
                number_position = [70,496]
                screen.blit(number, number_position)
                number_position = [384,786]
                screen.blit(number, number_position)
                number_position = [446,348]
                screen.blit(number, number_position)
            if 22 in s.holes:
                number_position = [69,398]
                screen.blit(number, number_position)
                number_position = [286,784]
                screen.blit(number, number_position)
                number_position = [598,396]
                screen.blit(number, number_position)
            if 23 in s.holes:
                number_position = [72,549]
                screen.blit(number, number_position)
                number_position = [384,834]
                screen.blit(number, number_position)
                number_position = [650,498]
                screen.blit(number, number_position)
            if 24 in s.holes:
                number_position = [20,501]
                screen.blit(number, number_position)
                number_position = [285,640]
                screen.blit(number, number_position)
                number_position = [447,450]
                screen.blit(number, number_position)
            if 25 in s.holes:
                number_position = [170,350]
                screen.blit(number, number_position)
                number_position = [434,690]
                screen.blit(number, number_position)
                number_position = [500,547]
                screen.blit(number, number_position)

    if s.game.tilt.status:
        tilt_position = [525,746]
        screen.blit(tilt, tilt_position)

    pygame.display.update()

def eb_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]
    if s.game.extra_ball.position not in [2,11,20]:
        dirty_rects.append(screen.blit(bg_gi, (123,940), pygame.Rect(123,940,44,34)))
    if s.game.extra_ball.position not in [3,12,21]:
        dirty_rects.append(screen.blit(bg_gi, (197,940), pygame.Rect(197,940,44,34)))
    if s.game.extra_ball.position not in [4,13,22]:
        dirty_rects.append(screen.blit(bg_gi, (269,940), pygame.Rect(269,940,44,34)))
    if s.game.extra_ball.position not in [5,14,23]:
        dirty_rects.append(screen.blit(bg_gi, (342,940), pygame.Rect(342,940,44,34)))
    if s.game.extra_ball.position not in [6,15]:
        dirty_rects.append(screen.blit(bg_gi, (413,940), pygame.Rect(413,940,44,34)))
    if s.game.extra_ball.position not in [7,16]:
        dirty_rects.append(screen.blit(bg_gi, (486,940), pygame.Rect(486,940,44,34)))
    if s.game.extra_ball.position not in [8,17]:
        dirty_rects.append(screen.blit(bg_gi, (556,940), pygame.Rect(556,940,44,34)))
    if s.game.extra_ball.position not in [9,18]:
        dirty_rects.append(screen.blit(bg_gi, (629,944), pygame.Rect(629,944,44,34)))
    if s.game.extra_ball.position < 8:
        dirty_rects.append(screen.blit(bg_gi, (40,985), pygame.Rect(40,985,207,35)))
    if s.game.extra_ball.position < 17:
        dirty_rects.append(screen.blit(bg_gi, (257,981), pygame.Rect(257,981,207,35)))
    if s.game.extra_ball.position < 24:
        dirty_rects.append(screen.blit(bg_gi, (472,983), pygame.Rect(472,983,207,35)))
    pygame.display.update(dirty_rects)
    if num in [1,9,17]:
        if s.game.extra_ball.position not in [2,11,20]:
            p = [123,940]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects) 
    elif num in [2,10,18]:
        if s.game.extra_ball.position not in [3,12,21]:
            p = [197,940]
            dirty_rects.append(screen.blit(eb, p))
            if s.game.extra_ball.position not in range(8,19):
                p = [40,985]
                screen.blit(extra_ball, p)
            pygame.display.update(dirty_rects)
    elif num in [3,11,18]:
        if s.game.extra_ball.position not in [4,13,22]:
            p = [269,940]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
    elif num in [4,12,20]:
        if s.game.extra_ball.position not in [5,14,23]:
            p = [342,940]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
    elif num in [5,13,21]:
        if s.game.extra_ball.position not in [6,15]:
            p = [413,940]
            dirty_rects.append(screen.blit(eb, p))
            if s.game.extra_ball.position not in range(17,25):
                p = [257,981]
                screen.blit(extra_ball, p)
            pygame.display.update(dirty_rects)
    elif num in [6,14,22]:
        if s.game.extra_ball.position not in [7,16]:
            p = [486,940]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
    elif num in [7,15,23]:
        if s.game.extra_ball.position not in [8,17]:
            p = [556,940]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
    elif num in [8,16,24]:
        if s.game.extra_ball.position not in [9,18]:
            p = [629,944]
            dirty_rects.append(screen.blit(eb, p))
            if s.game.extra_ball.position != 24:
                p = [472,983]
                screen.blit(extra_ball, p)
            pygame.display.update(dirty_rects)

def clear_mixers(s):
    global screen
    dirty_rects = []

    if s.game.c1_double.status == False:
        dirty_rects.append(screen.blit(bg_gi, (20,598), pygame.Rect(20,598,112,38)))
    if s.game.c2_double.status == False:
        dirty_rects.append(screen.blit(bg_gi, (242,886), pygame.Rect(242,886,112,38)))
    if s.game.c3_double.status == False:
        dirty_rects.append(screen.blit(bg_gi, (478,597), pygame.Rect(478,597,111,41)))
    if s.game.c1_triple.status == False:
        dirty_rects.append(screen.blit(bg_gi, (136,598), pygame.Rect(136,598,100,37)))
    if s.game.c2_triple.status == False:
        dirty_rects.append(screen.blit(bg_gi, (364,884), pygame.Rect(364,884,111,41)))
    if s.game.c3_triple.status == False:
        dirty_rects.append(screen.blit(bg_gi, (586,597), pygame.Rect(586,597,111,41)))
    if s.game.fss.status == False:
        dirty_rects.append(screen.blit(bg_gi, (284,456), pygame.Rect(284,456,153,44)))
    if s.game.fnt.status == False:
        dirty_rects.append(screen.blit(bg_gi, (284,499), pygame.Rect(284,499,153,44)))
    if s.game.all_double.status == False:
        dirty_rects.append(screen.blit(bg_gi, (284,369), pygame.Rect(284,369,153,44)))
    if s.game.all_triple.status == False:
        dirty_rects.append(screen.blit(bg_gi, (284,413), pygame.Rect(284,413,153,44)))
    pygame.display.update(dirty_rects)
    return

def animate_mixer1(s):
    global screen
    dirty_rects = []

    if s.game.c1_double.status == False:
        p = [20,598]
        c1d = pygame.transform.scale(rt_flag, (112, 38))
        dirty_rects.append(screen.blit(c1d, p))
    if s.game.c2_triple.status == False:
        p = [364,884]
        dirty_rects.append(screen.blit(lt_flag, p))
    if s.game.fss.status == False:
        p = [284,456]
        dirty_rects.append(screen.blit(ad, p))
    pygame.display.update(dirty_rects)
    return

def animate_mixer2(s):
    global screen
    dirty_rects = []

    if s.game.c2_double.status == False:
        p = [242,886]
        c1d = pygame.transform.scale(rt_flag, (112, 38))
        dirty_rects.append(screen.blit(c1d, p))
    if s.game.c3_triple.status == False:
        p = [586,597]
        dirty_rects.append(screen.blit(lt_flag, p))
    if s.game.fnt.status == False:
        p = [284,499]
        dirty_rects.append(screen.blit(ad, p))
    pygame.display.update(dirty_rects)
    return

def animate_mixer3(s):
    global screen
    dirty_rects = []

    if s.game.c3_double.status == False:
        p = [478,597]
        dirty_rects.append(screen.blit(lt_flag, p))
    if s.game.all_triple.status == False:
        p = [284,413]
        dirty_rects.append(screen.blit(ad, p))
    pygame.display.update(dirty_rects)
    return

def animate_mixer4(s):
    global screen
    dirty_rects = []
    if s.game.all_double.status == False:
        p = [284,369]
        dirty_rects.append(screen.blit(ad, p))
    if s.game.c1_triple.status == False:
        p = [136,598]
        dirty_rects.append(screen.blit(rt_flag, p))
    pygame.display.update(dirty_rects)
    return

def clear_features(s, num):
    global screen
    dirty_rects = []
    if 14 not in s.holes:
        dirty_rects.append(screen.blit(bg_gi, (123,500), pygame.Rect(123,500,51,50)))
        dirty_rects.append(screen.blit(bg_gi, (334,688), pygame.Rect(334,688,51,50)))
        dirty_rects.append(screen.blit(bg_gi, (496,450), pygame.Rect(496,450,51,50)))
    if 15 not in s.holes:
        dirty_rects.append(screen.blit(bg_gi, (174,549), pygame.Rect(174,549,51,50)))
        dirty_rects.append(screen.blit(bg_gi, (334,736), pygame.Rect(334,736,51,50)))
        dirty_rects.append(screen.blit(bg_gi, (446,400), pygame.Rect(446,400,51,50)))
    if 16 not in s.holes:
        dirty_rects.append(screen.blit(bg_gi, (122,450), pygame.Rect(122,450,51,50)))
        dirty_rects.append(screen.blit(bg_gi, (382,639), pygame.Rect(382,639,51,50)))
        dirty_rects.append(screen.blit(bg_gi, (594,548), pygame.Rect(594,548,51,50)))
    if 17 not in s.holes:
        dirty_rects.append(screen.blit(bg_gi, (220,399), pygame.Rect(220,399,51,50)))
        dirty_rects.append(screen.blit(bg_gi, (433,786), pygame.Rect(433,786,51,50)))
        dirty_rects.append(screen.blit(bg_gi, (547,450), pygame.Rect(547,450,51,50)))
    if 19 not in s.holes:
        dirty_rects.append(screen.blit(bg_gi, (172,398), pygame.Rect(172,398,51,50)))
        dirty_rects.append(screen.blit(bg_gi, (284,687), pygame.Rect(284,687,51,50)))
        dirty_rects.append(screen.blit(bg_gi, (596,498), pygame.Rect(596,498,51,50)))
    if 22 not in s.holes:
        dirty_rects.append(screen.blit(bg_gi, (69,398), pygame.Rect(69,398,51,50)))
        dirty_rects.append(screen.blit(bg_gi, (286,784), pygame.Rect(286,784,51,50)))
        dirty_rects.append(screen.blit(bg_gi, (598,396), pygame.Rect(598,396,51,50)))

    pygame.display.update(dirty_rects)

def draw_feature_animation(s, num):
    global screen
    dirty_rects = []
    if num in [1,13]:
        if 14 not in s.holes:
            p = [123,500]
            dirty_rects.append(screen.blit(number, p))
            p = [334,688]
            dirty_rects.append(screen.blit(number, p))
            p = [496,450]
            dirty_rects.append(screen.blit(number, p))
            pygame.display.update(dirty_rects)
            return
    if num in [3,15]:
        if 15 not in s.holes:
            p = [174,549]
            dirty_rects.append(screen.blit(number, p))
            p = [334,736]
            dirty_rects.append(screen.blit(number, p))
            p = [446,400]
            dirty_rects.append(screen.blit(number, p))
            pygame.display.update(dirty_rects)
            return
    if num in [5,17]:
        if 16 not in s.holes:
            p = [122,450]
            dirty_rects.append(screen.blit(number, p))
            p = [382,639]
            dirty_rects.append(screen.blit(number, p))
            p = [594,548]
            dirty_rects.append(screen.blit(number, p))
            pygame.display.update(dirty_rects)
            return
    if num in [7,19]:
        if 17 not in s.holes:
            p = [220,399]
            dirty_rects.append(screen.blit(number, p))
            p = [433,786]
            dirty_rects.append(screen.blit(number, p))
            p = [547,450]
            dirty_rects.append(screen.blit(number, p))
            pygame.display.update(dirty_rects)
            return
    if num in [9,21]:
        if 19 not in s.holes:
            p = [172,398]
            dirty_rects.append(screen.blit(number, p))
            p = [284,687]
            dirty_rects.append(screen.blit(number, p))
            p = [596,498]
            dirty_rects.append(screen.blit(number, p))
            pygame.display.update(dirty_rects)
            return
    if num in [11,23]:
        if 22 not in s.holes:
            p = [69,398]
            dirty_rects.append(screen.blit(number, p))
            p = [286,784]
            dirty_rects.append(screen.blit(number, p))
            p = [598,396]
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

