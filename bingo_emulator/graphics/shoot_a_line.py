
import pygame

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

meter = pygame.image.load('graphics/assets/black_register_cover.png').convert()
card = pygame.image.load('shoot_a_line/assets/card.png').convert_alpha()
number = pygame.image.load('shoot_a_line/assets/number.png').convert_alpha()
tilt = pygame.image.load('shoot_a_line/assets/tilt.png').convert_alpha()

class scorereel():
    """ Score Reels are used to count replays """
    def __init__(self, pos, image):
        self.position = pos
        self.default_y = self.position[1]
        self.image = pygame.image.load(image).convert()

reel1 = scorereel([597,345], "graphics/assets/white_reel.png")
reel10 = scorereel([578,345], "graphics/assets/white_reel.png")
reel100 = scorereel([558,345], "graphics/assets/white_reel.png")
reel1000 = scorereel([540,345], "graphics/assets/white_reel.png")

def display(s, replays=0, menu=False):
    
    meter.set_colorkey((255,0,252))
    meter_position = [531,345]

    screen.blit(reel1.image, reel1.position)
    screen.blit(reel10.image, reel10.position)
    screen.blit(reel100.image, reel100.position)
    screen.blit(reel1000.image, reel1000.position)
    screen.blit(meter, meter_position)

    backglass_position = [0, 0]
    backglass = pygame.Surface((0,0), pygame.SRCALPHA)
    backglass.fill((0, 0, 0))
    if menu == True:
        backglass = pygame.image.load('shoot_a_line/assets/shoot_a_line_menu.png')
    else:
        if (s.game.anti_cheat.status == True):
            backglass = pygame.image.load('shoot_a_line/assets/shoot_a_line_gi.png')
        else:
            backglass = pygame.image.load('shoot_a_line/assets/shoot_a_line_off.png')
    screen.blit(backglass, backglass_position)

    if s.game.selector.position >= 1:
        position = [93,767]
        screen.blit(card, position)
    if s.game.selector.position >= 2:
        position = [295,769]
        screen.blit(card, position)
    if s.game.selector.position >= 3:
        position = [494,769]
        screen.blit(card, position)
    if s.game.selector.position >= 4:
        position = [93,999]
        screen.blit(card, position)
    if s.game.selector.position >= 5:
        position = [295,999]
        screen.blit(card, position)
    if s.game.selector.position >= 6:
        position = [494,999]
        screen.blit(card, position)

    if s.game.tilt.status == False:
        if s.holes:
            if 1 in s.holes:
                position = [149,587]
                screen.blit(number, position)
                position = [383,625]
                screen.blit(number, position)
                position = [517,625]
                screen.blit(number, position)
                position = [214,819]
                screen.blit(number, position)
                position = [381,820]
                screen.blit(number, position)
                position = [516,891]
                screen.blit(number, position)
            if 2 in s.holes:
                position = [83,657]
                screen.blit(number, position)
                position = [351,589]
                screen.blit(number, position)
                position = [549,729]
                screen.blit(number, position)
                position = [82,958]
                screen.blit(number, position)
                position = [582,961]
                screen.blit(number, position)
            if 3 in s.holes:
                position = [214,657]
                screen.blit(number, position)
                position = [285,623]
                screen.blit(number, position)
                position = [584,661]
                screen.blit(number, position)
                position = [116,888]
                screen.blit(number, position)
                position = [414,960]
                screen.blit(number, position)
            if 4 in s.holes:
                position = [181,623]
                screen.blit(number, position)
                position = [384,659]
                screen.blit(number, position)
                position = [614,590]
                screen.blit(number, position)
                position = [283,959]
                screen.blit(number, position)
                position = [582,891]
                screen.blit(number, position)
            if 5 in s.holes:
                position = [182,692]
                screen.blit(number, position)
                position = [317,728]
                screen.blit(number, position)
                position = [485,589]
                screen.blit(number, position)
                position = [84,852]
                screen.blit(number, position)
                position = [383,890]
                screen.blit(number, position)
            if 6 in s.holes:
                position = [149,726]
                screen.blit(number, position)
                position = [285,658]
                screen.blit(number, position)
                position = [484,728]
                screen.blit(number, position)
                position = [182,889]
                screen.blit(number, position)
                position = [382,960]
                screen.blit(number, position)
                position = [517,962]
                screen.blit(number, position)
            if 7 in s.holes:
                position = [118,621]
                screen.blit(number, position)
                position = [415,728]
                screen.blit(number, position)
                position = [582,625]
                screen.blit(number, position)
                position = [117,818]
                screen.blit(number, position)
                position = [317,819]
                screen.blit(number, position)
                position = [550,857]
                screen.blit(number, position)
            if 8 in s.holes:
                position = [117,692]
                screen.blit(number, position)
                position = [318,694]
                screen.blit(number, position)
                position = [517,694]
                screen.blit(number, position)
                position = [213,958]
                screen.blit(number, position)
                position = [317,890]
                screen.blit(number, position)
                position = [518,821]
                screen.blit(number, position)
            if 9 in s.holes:
                position = [149,657]
                screen.blit(number, position)
                position = [416,659]
                screen.blit(number, position)
                position = [550,590]
                screen.blit(number, position)
                position = [182,819]
                screen.blit(number, position)
                position = [284,854]
                screen.blit(number, position)
                position = [485,820]
                screen.blit(number, position)
            if 10 in s.holes:
                position = [85,586]
                screen.blit(number, position)
                position = [284,727]
                screen.blit(number, position)
                position = [615,729]
                screen.blit(number, position)
                position = [83,922]
                screen.blit(number, position)
                position = [415,820]
                screen.blit(number, position)
                position = [485,855]
                screen.blit(number, position)
            if 11 in s.holes:
                position = [214,725]
                screen.blit(number, position)
                position = [416,590]
                screen.blit(number, position)
                position = [484,659]
                screen.blit(number, position)
                position = [181,958]
                screen.blit(number, position)
                position = [350,855]
                screen.blit(number, position)
                position = [615,857]
                screen.blit(number, position)
            if 12 in s.holes:
                position = [214,587]
                screen.blit(number, position)
                position = [350,728]
                screen.blit(number, position)
                position = [550,625]
                screen.blit(number, position)
                position = [115,958]
                screen.blit(number, position)
                position = [415,855]
                screen.blit(number, position)
                position = [484,960]
                screen.blit(number, position)
            if 13 in s.holes:
                position = [83,727]
                screen.blit(number, position)
                position = [350,659]
                screen.blit(number, position)
                position = [615,660]
                screen.blit(number, position)
                position = [149,854]
                screen.blit(number, position)
                position = [283,925]
                screen.blit(number, position)
                position = [614,962]
                screen.blit(number, position)
            if 14 in s.holes:
                position = [84,622]
                screen.blit(number, position)
                position = [286,589]
                screen.blit(number, position)
                position = [582,695]
                screen.blit(number, position)
                position = [148,923]
                screen.blit(number, position)
                position = [349,926]
                screen.blit(number, position)
                position = [614,822]
                screen.blit(number, position)
            if 15 in s.holes:
                position = [214,693]
                screen.blit(number, position)
                position = [319,590]
                screen.blit(number, position)
                position = [582,729]
                screen.blit(number, position)
                position = [215,854]
                screen.blit(number, position)
                position = [285,820]
                screen.blit(number, position)
                position = [582,822]
                screen.blit(number, position)
            if 16 in s.holes:
                position = [182,587]
                screen.blit(number, position)
                position = [351,624]
                screen.blit(number, position)
                position = [517,659]
                screen.blit(number, position)
                position = [213,924]
                screen.blit(number, position)
                position = [382,855]
                screen.blit(number, position)
                position = [484,926]
                screen.blit(number, position)
            if 17 in s.holes:
                position = [116,726]
                screen.blit(number, position)
                position = [383,728]
                screen.blit(number, position)
                position = [517,730]
                screen.blit(number, position)
                position = [149,889]
                screen.blit(number, position)
                position = [414,926]
                screen.blit(number, position)
                position = [550,961]
                screen.blit(number, position)
            if 18 in s.holes:
                position = [183,726]
                screen.blit(number, position)
                position = [416,694]
                screen.blit(number, position)
                position = [582,591]
                screen.blit(number, position)
                position = [85,819]
                screen.blit(number, position)
                position = [316,960]
                screen.blit(number, position)
                position = [550,926]
                screen.blit(number, position)
            if 19 in s.holes:
                position = [118,588]
                screen.blit(number, position)
                position = [383,694]
                screen.blit(number, position)
                position = [550,695]
                screen.blit(number, position)
                position = [180,924]
                screen.blit(number, position)
                position = [349,959]
                screen.blit(number, position)
                position = [615,927]
                screen.blit(number, position)
            if 20 in s.holes:
                position = [216,622]
                screen.blit(number, position)
                position = [417,625]
                screen.blit(number, position)
                position = [518,590]
                screen.blit(number, position)
                position = [150,819]
                screen.blit(number, position)
                position = [381,925]
                screen.blit(number, position)
                position = [583,857]
                screen.blit(number, position)
            if 21 in s.holes:
                position = [84,692]
                screen.blit(number, position)
                position = [319,659]
                screen.blit(number, position)
                position = [484,624]
                screen.blit(number, position)
                position = [149,958]
                screen.blit(number, position)
                position = [415,891]
                screen.blit(number, position)
                position = [518,855]
                screen.blit(number, position)
            if 22 in s.holes:
                position = [117,657]
                screen.blit(number, position)
                position = [285,693]
                screen.blit(number, position)
                position = [614,695]
                screen.blit(number, position)
                position = [214,889]
                screen.blit(number, position)
                position = [318,854]
                screen.blit(number, position)
                position = [518,926]
                screen.blit(number, position)
            if 23 in s.holes:
                position = [150,622]
                screen.blit(number, position)
                position = [350,694]
                screen.blit(number, position)
                position = [550,660]
                screen.blit(number, position)
                position = [118,852]
                screen.blit(number, position)
                position = [350,820]
                screen.blit(number, position)
                position = [583,927]
                screen.blit(number, position)
            if 24 in s.holes:
                position = [149,692]
                screen.blit(number, position)
                position = [319,624]
                screen.blit(number, position)
                position = [484,694]
                screen.blit(number, position)
                position = [84,888]
                screen.blit(number, position)
                position = [316,925]
                screen.blit(number, position)
                position = [551,892]
                screen.blit(number, position)
            if 25 in s.holes:
                position = [182,657]
                screen.blit(number, position)
                position = [384,590]
                screen.blit(number, position)
                position = [615,625]
                screen.blit(number, position)
                position = [284,890]
                screen.blit(number, position)
                position = [551,821]
                screen.blit(number, position)
                position = [117,924]
                screen.blit(number, position)
            if 26 in s.holes:
                position = [349,890]
                screen.blit(number, position)
            if 27 in s.holes:
                position = [182,854]
                screen.blit(number, position)
                position = [484,891]
                screen.blit(number, position)
            if 28 in s.holes:
                position = [615,892]
                screen.blit(number, position)

    if s.game.tilt.status == True:
        position = [25,262]
        screen.blit(tilt, position)

    pygame.display.update()

