
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
        backglass = pygame.image.load('rodeo_3/assets/rodeo_3_menu.png')
    else:
        if (s.game.lock.status == True):
            backglass = pygame.image.load('rodeo_3/assets/rodeo_3_gi.png')
        else:
            backglass = pygame.image.load('rodeo_3/assets/rodeo_3_off.png')
    backglass = pygame.transform.scale(backglass, (720, 1280))
    
    screen.blit(backglass, backglass_position)

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

    pygame.display.flip()
    pygame.display.update()

def eb_animation(num):
    global screen
    if num == 9:
        eb_position = [48,898]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 8:
        eb_position = [120,897]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 7:
        eb_position = [195,896]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 6:
        eb_position = [265,897]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 5:
        eb_position = [337,897]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 4:
        eb_position = [410,897]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 3:
        eb_position = [481,898]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 2:
        eb_position = [553,898]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 1:
        eb_position = [623,898]
        screen.blit(eb, eb_position)
        pygame.display.update()

def feature_animation(num):
    global screen
    if num == 10:
        ad_position = [283,467]
        screen.blit(ad, ad_position)
        pygame.display.update()
    if num == 9:
        ad_position = [283,509]
        screen.blit(ad, ad_position)
        pygame.display.update()
    if num == 8:
        ad_position = [283,392]
        screen.blit(ad, ad_position)
        pygame.display.update()
    if num == 7:
        ad_position = [283,431]
        screen.blit(ad, ad_position)
        pygame.display.update()
    if num == 6:
        c1d_position = [62,606]
        screen.blit(double_triple, c1d_position)
        pygame.display.update()
    if num == 5:
        c2d_position = [277,861]
        screen.blit(double_triple, c2d_position)
        pygame.display.update()
    if num == 4:
        c3d_position = [491,606]
        screen.blit(double_triple, c3d_position)
        pygame.display.update()
    if num == 3:
        c1d_position = [150,605]
        screen.blit(double_triple, c1d_position)
        pygame.display.update()
    if num == 2:
        c2d_position = [360,861]
        screen.blit(double_triple, c2d_position)
        pygame.display.update()
    if num == 1:
        c3d_position = [576,604]
        screen.blit(double_triple, c3d_position)
