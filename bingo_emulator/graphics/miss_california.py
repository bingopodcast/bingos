
import pygame
import random

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

card = pygame.image.load('miss_california/assets/card.png').convert_alpha()
double = pygame.image.load('miss_california/assets/double.png').convert_alpha()
c = pygame.image.load('miss_california/assets/corners.png').convert_alpha()
number = pygame.image.load('miss_california/assets/number.png').convert_alpha()
tilt = pygame.image.load('miss_california/assets/tilt.png').convert_alpha()
meter = pygame.image.load('graphics/assets/register_cover.png').convert()

class scorereel():
    """ Score Reels are used to count replays """
    def __init__(self, pos, image):
        self.position = pos
        self.default_y = self.position[1]
        self.image = pygame.image.load(image).convert()

reel1 = scorereel([607,295], "graphics/assets/green_reel.png")
reel10 = scorereel([588,295], "graphics/assets/green_reel.png")
reel100 = scorereel([568,295], "graphics/assets/green_reel.png")

def display(s, replays=0, menu=False):
    
    meter.set_colorkey((255,0,252))
    meter_position = [559,295]

    screen.blit(reel1.image, reel1.position)
    screen.blit(reel10.image, reel10.position)
    screen.blit(reel100.image, reel100.position)
    screen.blit(meter, meter_position)

    backglass_position = [0, 0]
    backglass = pygame.Surface(screen.get_size(), flags=pygame.SRCALPHA)
    backglass.fill((0, 0, 0))
    if menu == True:
        backglass = pygame.image.load('miss_california/assets/miss_california_menu.png')
    else:
        if (s.game.anti_cheat.status == True):
            backglass = pygame.image.load('miss_california/assets/miss_california_gi.png')
        else:
            backglass = pygame.image.load('miss_california/assets/miss_california_off.png')
    backglass = pygame.transform.scale(backglass, (720, 1280))
    
    screen.blit(backglass, backglass_position)

    if s.game.selector.position >= 1:
        card_position = [96,608]
        screen.blit(card, card_position)
    if s.game.selector.position >= 2:
        card_position = [310,287]
        screen.blit(card, card_position)
    if s.game.selector.position >= 3:
        card_position = [528,608]
        screen.blit(card, card_position)

    if s.game.c1_double.status == True:
        c1d_position = [75,645]
        screen.blit(double, c1d_position)

    if s.game.c2_double.status == True:
        c2d_position = [289,323]
        c2d = pygame.image.load('miss_california/assets/double.png').convert_alpha()
        screen.blit(double, c2d_position)

    if s.game.c3_double.status == True:
        c3d_position = [505,645]
        c3d = pygame.image.load('miss_california/assets/double.png').convert_alpha()
        screen.blit(double, c3d_position)

    if s.game.corners.status == True:
        corners_position = [299,705]
        c = pygame.image.load('miss_california/assets/corners.png').convert_alpha()
        screen.blit(c, corners_position)

    if s.game.tilt.status == False:
        if s.holes:
            if 1 in s.holes:
                number1_position = [70,695]
                screen.blit(number, number1_position)
                number2_position = [235,538]
                screen.blit(number, number2_position)
                number3_position = [553,915]
                screen.blit(number, number3_position)

            if 2 in s.holes:
                number1_position = [125,912]
                screen.blit(number, number1_position)
                number2_position = [233,483]
                screen.blit(number, number2_position)
                number3_position = [655,805]
                screen.blit(number, number3_position)
            if 3 in s.holes:
                number1_position = [225,693]
                screen.blit(number, number1_position)
                number2_position = [439,593]
                screen.blit(number, number2_position)
                number3_position = [499,750]
                screen.blit(number, number3_position)
            if 4 in s.holes:
                number1_position = [226,914]
                screen.blit(number, number1_position)
                number2_position = [335,374]
                screen.blit(number, number2_position)
                number3_position = [602,696]
                screen.blit(number, number3_position)
            if 5 in s.holes:
                number1_position = [19,695]
                screen.blit(number, number1_position)
                number2_position = [338,593]
                screen.blit(number, number2_position)
                number3_position = [654,914]
                screen.blit(number, number3_position)
            if 6 in s.holes:
                number1_position = [21,804]
                screen.blit(number, number1_position)
                number2_position = [439,372]
                screen.blit(number, number2_position)
                number3_position = [499,860]
                screen.blit(number, number3_position)
            if 7 in s.holes:
                number1_position = [226,803]
                screen.blit(number, number1_position)
                number2_position = [286,592]
                screen.blit(number, number2_position)
                number3_position = [498,694]
                screen.blit(number, number3_position)
            if 8 in s.holes:
                number1_position = [20,750]
                screen.blit(number, number1_position)
                number2_position = [439,485]
                screen.blit(number, number2_position)
                number3_position = [656,749]
                screen.blit(number, number3_position)

            if 9 in s.holes:
                number1_position = [121,695]
                screen.blit(number, number1_position)
                number2_position = [231,374]
                screen.blit(number, number2_position)
                number3_position = [653,694]
                screen.blit(number, number3_position)

            if 10 in s.holes:
                number1_position = [120,749]
                screen.blit(number, number1_position)
                number2_position = [232,593]
                screen.blit(number, number2_position)
                number3_position = [549,694]
                screen.blit(number, number3_position)

            if 11 in s.holes:
                number1_position = [175,805]
                screen.blit(number, number1_position)
                number2_position = [336,538]
                screen.blit(number, number2_position)
                number3_position = [604,806]
                screen.blit(number, number3_position)

            if 12 in s.holes:
                number1_position = [22,912]
                screen.blit(number, number1_position)
                number2_position = [389,481]
                screen.blit(number, number2_position)
                number3_position = [553,859]
                screen.blit(number, number3_position)

            if 13 in s.holes:
                number1_position = [228,858]
                screen.blit(number, number1_position)
                number2_position = [233,427]
                screen.blit(number, number2_position)
                number3_position = [449,861]
                screen.blit(number, number3_position)

            if 14 in s.holes:
                number1_position = [123,860]
                screen.blit(number, number1_position)
                number2_position = [335,428]
                screen.blit(number, number2_position)
                number3_position = [498,806]
                screen.blit(number, number3_position)

            if 15 in s.holes:
                number1_position = [177,913]
                screen.blit(number, number1_position)
                number2_position = [336,485]
                screen.blit(number, number2_position)
                number3_position = [446,750]
                screen.blit(number, number3_position)

            if 16 in s.holes:
                number1_position = [122,804]
                screen.blit(number, number1_position)
                number2_position = [386,373]
                screen.blit(number, number2_position)
                number3_position = [604,913]
                screen.blit(number, number3_position)

            if 17 in s.holes:
                number1_position = [226,750]
                screen.blit(number, number1_position)
                number2_position = [440,537]
                screen.blit(number, number2_position)
                number3_position = [553,805]
                screen.blit(number, number3_position)

            if 18 in s.holes:
                number1_position = [73,803]
                screen.blit(number, number1_position)
                number2_position = [284,483]
                screen.blit(number, number2_position)
                number3_position = [552,749]
                screen.blit(number, number3_position)

            if 19 in s.holes:
                number1_position = [176,750]
                screen.blit(number, number1_position)
                number2_position = [285,427]
                screen.blit(number, number2_position)
                number3_position = [605,858]
                screen.blit(number, number3_position)

            if 20 in s.holes:
                number1_position = [177,859]
                screen.blit(number, number1_position)
                number2_position = [389,428]
                screen.blit(number, number2_position)
                number3_position = [448,914]
                screen.blit(number, number3_position)

            if 21 in s.holes:
                number1_position = [70,861]
                screen.blit(number, number1_position)
                number2_position = [388,537]
                screen.blit(number, number2_position)
                number3_position = [448,693]
                screen.blit(number, number3_position)

            if 22 in s.holes:
                number1_position = [71,748]
                screen.blit(number, number1_position)
                number2_position = [284,537]
                screen.blit(number, number2_position)
                number3_position = [604,750]
                screen.blit(number, number3_position)

            if 23 in s.holes:
                number1_position = [70,913]
                screen.blit(number, number1_position)
                number2_position = [391,593]
                screen.blit(number, number2_position)
                number3_position = [656,859]
                screen.blit(number, number3_position)

            if 24 in s.holes:
                number1_position = [21,858]
                screen.blit(number, number1_position)
                number2_position = [284,373]
                screen.blit(number, number2_position)
                number3_position = [448,804]
                screen.blit(number, number3_position)

            if 25 in s.holes:
                number1_position = [174,693]
                screen.blit(number, number1_position)
                number2_position = [440,424]
                screen.blit(number, number2_position)
                number3_position = [501,913]
                screen.blit(number, number3_position)


    if s.game.tilt.status:
        tilt_position = [317,859]
        screen.blit(tilt, tilt_position)

    pygame.display.flip()
    pygame.display.update()

def feature_animation(num):
    global screen
    if num == 4:
        corners_position = [299,705]
        c = pygame.image.load('miss_california/assets/corners.png').convert_alpha()
        screen.blit(c, corners_position)
        pygame.display.update()
    if num == 3:
        c1d_position = [75,645]
        c1d = pygame.image.load('miss_california/assets/double.png').convert_alpha()
        screen.blit(c1d, c1d_position)
        pygame.display.update()
    if num == 2:
        c2d_position = [289,323]
        c2d = pygame.image.load('miss_california/assets/double.png').convert_alpha()
        screen.blit(c2d, c2d_position)
        pygame.display.update()
    if num == 1:
        c3d_position = [505,645]
        c3d = pygame.image.load('miss_california/assets/double.png').convert_alpha()
        screen.blit(c3d, c3d_position)
        pygame.display.update()
