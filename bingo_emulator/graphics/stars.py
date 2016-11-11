
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
        backglass = pygame.image.load('stars/assets/stars_menu.png')
    else:
        if (s.game.anti_cheat.status == True):
            backglass = pygame.image.load('stars/assets/stars_gi.png')
        else:
            backglass = pygame.image.load('stars/assets/stars_off.png')
    backglass = pygame.transform.scale(backglass, (720, 1280))
    
    screen.blit(backglass, backglass_position)

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

def eb_animation(num):
    global screen

    if num == 9:
        eb_position = [43,960]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 8:
        eb_position = [118,960]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 7:
        eb_position = [191,957]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 6:
        eb_position = [265,957]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 5:
        eb_position = [338,957]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 4:
        eb_position = [409,957]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 3:
        eb_position = [483,957]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 2:
        eb_position = [556,957]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 1:
        eb_position = [630,957]
        screen.blit(eb, eb_position)
        pygame.display.update()

    
def feature_animation(num):
    global screen
    if num == 4:
        ad_position = [304,378]
        screen.blit(ad, ad_position)
        pygame.display.update()
    if num == 3:
        c1d_position = [70,596]
        screen.blit(double, c1d_position)
        pygame.display.update()
    if num == 2:
        c2d_position = [282,894]
        screen.blit(double, c2d_position)
        pygame.display.update()
    if num == 1:
        c3d_position = [496,596]
        screen.blit(double, c3d_position)
        pygame.display.update()
