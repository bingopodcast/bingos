
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

def eb_animation(num):
    global screen
    if num == 9:
        eb_position = [51,943]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 8:
        eb_position = [123,940]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 7:
        eb_position = [197,940]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 6:
        eb_position = [269,940]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 5:
        eb_position = [342,940]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 4:
        eb_position = [413,940]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 3:
        eb_position = [486,940]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 2:
        eb_position = [556,940]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 1:
        eb_position = [629,944]
        screen.blit(eb, eb_position)
        pygame.display.update()

def feature_animation(num):
    global screen
    if num == 10:
        ad_position = [284,369]
        screen.blit(ad, ad_position)
        pygame.display.update()
    if num == 9:
        ad_position = [284,413]
        screen.blit(ad, ad_position)
        pygame.display.update()
    if num == 8:
        ad_position = [284,456]
        screen.blit(ad, ad_position)
        pygame.display.update()
    if num == 7:
        ad_position = [284,499]
        screen.blit(ad, ad_position)
        pygame.display.update()
    if num == 6:
        c1d_position = [20,598]
        c1d = pygame.transform.scale(rt_flag, (112, 38))
        screen.blit(c1d, c1d_position)
        pygame.display.update()
    if num == 5:
        c2d_position = [242,886]
        c2d = pygame.transform.scale(rt_flag, (112, 38))
        screen.blit(c2d, c2d_position)
        pygame.display.update()
    if num == 4:
        c3d_position = [478,597]
        screen.blit(lt_flag, c3d_position)
        pygame.display.update()
    if num == 3:
        c1d_position = [136,598]
        screen.blit(rt_flag, c1d_position)
        pygame.display.update()
    if num == 2:
        c2d_position = [364,884]
        screen.blit(lt_flag, c2d_position)
        pygame.display.update()
    if num == 1:
        c3d_position = [586,597]
        screen.blit(lt_flag, c3d_position)
