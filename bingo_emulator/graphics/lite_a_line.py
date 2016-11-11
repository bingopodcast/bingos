
import pygame

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

meter = pygame.image.load('graphics/assets/black_register_cover.png').convert()
card = pygame.image.load('lite_a_line/assets/card.png').convert_alpha()
number = pygame.image.load('lite_a_line/assets/number.png').convert_alpha()
tilt = pygame.image.load('lite_a_line/assets/tilt.png').convert_alpha()

class scorereel():
    """ Score Reels are used to count replays """
    def __init__(self, pos, image):
        self.position = pos
        self.default_y = self.position[1]
        self.image = pygame.image.load(image).convert()

reel1 = scorereel([589,340], "graphics/assets/white_reel.png")
reel10 = scorereel([570,340], "graphics/assets/white_reel.png")
reel100 = scorereel([550,340], "graphics/assets/white_reel.png")
reel1000 = scorereel([532,340], "graphics/assets/white_reel.png")

def display(s, replays=0, menu=False):
    
    meter.set_colorkey((255,0,252))
    meter_position = [522,340]

    screen.blit(reel1.image, reel1.position)
    screen.blit(reel10.image, reel10.position)
    screen.blit(reel100.image, reel100.position)
    screen.blit(reel1000.image, reel1000.position)
    screen.blit(meter, meter_position)

    backglass_position = [0, 0]
    backglass = pygame.Surface((0,0), pygame.SRCALPHA)
    backglass.fill((0, 0, 0))
    if menu == True:
        backglass = pygame.image.load('lite_a_line/assets/lite_a_line_menu.png')
    else:
        if (s.game.anti_cheat.status == True):
            backglass = pygame.image.load('lite_a_line/assets/lite_a_line_gi.png')
        else:
            backglass = pygame.image.load('lite_a_line/assets/lite_a_line_off.png')
    screen.blit(backglass, backglass_position)

    if s.game.selector.position >= 1:
        position = [96,761]
        screen.blit(card, position)
    if s.game.selector.position >= 2:
        position = [297,761]
        screen.blit(card, position)
    if s.game.selector.position >= 3:
        position = [498,761]
        screen.blit(card, position)
    if s.game.selector.position >= 4:
        position = [92,1006]
        screen.blit(card, position)
    if s.game.selector.position >= 5:
        position = [297,1006]
        screen.blit(card, position)
    if s.game.selector.position >= 6:
        position = [496,1006]
        screen.blit(card, position)

    if s.game.tilt.status == False:
        if s.holes:
            if 1 in s.holes:
                position = [110,570]
                screen.blit(number, position)
                position = [277,684]
                screen.blit(number, position)
                position = [580,722]
                screen.blit(number, position)
                position = [213,816]
                screen.blit(number, position)
                position = [275,966]
                screen.blit(number, position)
                position = [546,815]
                screen.blit(number, position)
            if 2 in s.holes:
                position = [144,719]
                screen.blit(number, position)
                position = [276,647]
                screen.blit(number, position)
                position = [613,648]
                screen.blit(number, position)
                position = [211,855]
                screen.blit(number, position)
                position = [275,854]
                screen.blit(number, position)
                position = [577,964]
                screen.blit(number, position)
            if 3 in s.holes:
                position = [213,571]
                screen.blit(number, position)
                position = [414,720]
                screen.blit(number, position)
                position = [478,573]
                screen.blit(number, position)
                position = [143,815]
                screen.blit(number, position)
                position = [377,966]
                screen.blit(number, position)
                position = [545,854]
                screen.blit(number, position)
            if 4 in s.holes:
                position = [179,721]
                screen.blit(number, position)
                position = [381,573]
                screen.blit(number, position)
                position = [578,575]
                screen.blit(number, position)
                position = [176,967]
                screen.blit(number, position)
                position = [414,816]
                screen.blit(number, position)
                position = [477,816]
                screen.blit(number, position)
            if 5 in s.holes:
                position = [76,569]
                screen.blit(number, position)
                position = [346,722]
                screen.blit(number, position)
                position = [611,720]
                screen.blit(number, position)
                position = [72,890]
                screen.blit(number, position)
                position = [413,890]
                screen.blit(number, position)
                position = [611,815]
                screen.blit(number, position)
            if 6 in s.holes:
                position = [75,643]
                screen.blit(number, position)
                position = [414,572]
                screen.blit(number, position)
                position = [476,721]
                screen.blit(number, position)
                position = [72,814]
                screen.blit(number, position)
                position = [412,963]
                screen.blit(number, position)
                position = [511,815]
                screen.blit(number, position)
            if 7 in s.holes:
                position = [212,608]
                screen.blit(number, position)
                position = [310,720]
                screen.blit(number, position)
                position = [512,574]
                screen.blit(number, position)
                position = [109,815]
                screen.blit(number, position)
                position = [310,966]
                screen.blit(number, position)
                position = [475,965]
                screen.blit(number, position)
            if 8 in s.holes:
                position = [74,606]
                screen.blit(number, position)
                position = [414,684]
                screen.blit(number, position)
                position = [612,610]
                screen.blit(number, position)
                position = [208,963]
                screen.blit(number, position)
                position = [276,816]
                screen.blit(number, position)
                position = [612,927]
                screen.blit(number, position)
            if 9 in s.holes:
                position = [144,569]
                screen.blit(number, position)
                position = [276,570]
                screen.blit(number, position)
                position = [612,574]
                screen.blit(number, position)
                position = [142,927]
                screen.blit(number, position)
                position = [345,928]
                screen.blit(number, position)
                position = [476,890]
                screen.blit(number, position)
            if 10 in s.holes:
                position = [143,606]
                screen.blit(number, position)
                position = [277,721]
                screen.blit(number, position)
                position = [545,573]
                screen.blit(number, position)
                position = [71,965]
                screen.blit(number, position)
                position = [345,817]
                screen.blit(number, position)
                position = [476,927]
                screen.blit(number, position)
            if 11 in s.holes:
                position = [176,646]
                screen.blit(number, position)
                position = [345,685]
                screen.blit(number, position)
                position = [579,648]
                screen.blit(number, position)
                position = [72,928]
                screen.blit(number, position)
                position = [414,929]
                screen.blit(number, position)
                position = [611,963]
                screen.blit(number, position)
            if 12 in s.holes:
                position = [75,718]
                screen.blit(number, position)
                position = [380,648]
                screen.blit(number, position)
                position = [545,685]
                screen.blit(number, position)
                position = [143,854]
                screen.blit(number, position)
                position = [310,891]
                screen.blit(number, position)
                position = [578,889]
                screen.blit(number, position)
            if 13 in s.holes:
                position = [212,683]
                screen.blit(number, position)
                position = [277,610]
                screen.blit(number, position)
                position = [478,683]
                screen.blit(number, position)
                position = [107,966]
                screen.blit(number, position)
                position = [379,815]
                screen.blit(number, position)
                position = [612,852]
                screen.blit(number, position)
            if 14 in s.holes:
                position = [144,682]
                screen.blit(number, position)
                position = [345,611]
                screen.blit(number, position)
                position = [511,648]
                screen.blit(number, position)
                position = [107,851]
                screen.blit(number, position)
                position = [379,854]
                screen.blit(number, position)
                position = [576,924]
                screen.blit(number, position)
            if 15 in s.holes:
                position = [212,720]
                screen.blit(number, position)
                position = [345,646]
                screen.blit(number, position)
                position = [478,648]
                screen.blit(number, position)
                position = [176,928]
                screen.blit(number, position)
                position = [310,928]
                screen.blit(number, position)
                position = [511,853]
                screen.blit(number, position)
            if 16 in s.holes:
                position = [144,645]
                screen.blit(number, position)
                position = [345,572]
                screen.blit(number, position)
                position = [545,721]
                screen.blit(number, position)
                position = [177,891]
                screen.blit(number, position)
                position = [345,854]
                screen.blit(number, position)
                position = [544,927]
                screen.blit(number, position)
            if 17 in s.holes:
                position = [212,644]
                screen.blit(number, position)
                position = [414,648]
                screen.blit(number, position)
                position = [544,647]
                screen.blit(number, position)
                position = [108,930]
                screen.blit(number, position)
                position = [311,853]
                screen.blit(number, position)
                position = [579,854]
                screen.blit(number, position)
            if 18 in s.holes:
                position = [109,645]
                screen.blit(number, position)
                position = [312,647]
                screen.blit(number, position)
                position = [545,610]
                screen.blit(number, position)
                position = [177,854]
                screen.blit(number, position)
                position = [378,926]
                screen.blit(number, position)
                position = [510,927]
                screen.blit(number, position)
            if 19 in s.holes:
                position = [178,609]
                screen.blit(number, position)
                position = [312,610]
                screen.blit(number, position)
                position = [578,685]
                screen.blit(number, position)
                position = [107,890]
                screen.blit(number, position)
                position = [379,892]
                screen.blit(number, position)
                position = [511,890]
                screen.blit(number, position)
            if 20 in s.holes:
                position = [178,682]
                screen.blit(number, position)
                position = [380,612]
                screen.blit(number, position)
                position = [512,685]
                screen.blit(number, position)
                position = [142,892]
                screen.blit(number, position)
                position = [275,891]
                screen.blit(number, position)
                position = [611,890]
                screen.blit(number, position)
            if 21 in s.holes:
                position = [108,683]
                screen.blit(number, position)
                position = [379,683]
                screen.blit(number, position)
                position = [511,610]
                screen.blit(number, position)
                position = [142,965]
                screen.blit(number, position)
                position = [344,965]
                screen.blit(number, position)
                position = [544,889]
                screen.blit(number, position)
            if 22 in s.holes:
                position = [109,606]
                screen.blit(number, position)
                position = [311,685]
                screen.blit(number, position)
                position = [579,610]
                screen.blit(number, position)
                position = [211,891]
                screen.blit(number, position)
                position = [344,890]
                screen.blit(number, position)
                position = [544,964]
                screen.blit(number, position)
            if 23 in s.holes:
                position = [109,720]
                screen.blit(number, position)
                position = [379,721]
                screen.blit(number, position)
                position = [612,684]
                screen.blit(number, position)
                position = [73,853]
                screen.blit(number, position)
                position = [311,816]
                screen.blit(number, position)
                position = [579,815]
                screen.blit(number, position)
            if 24 in s.holes:
                position = [73,682]
                screen.blit(number, position)
                position = [311,572]
                screen.blit(number, position)
                position = [478,611]
                screen.blit(number, position)
                position = [177,816]
                screen.blit(number, position)
                position = [413,853]
                screen.blit(number, position)
                position = [510,966]
                screen.blit(number, position)
            if 25 in s.holes:
                position = [178,570]
                screen.blit(number, position)
                position = [414,610]
                screen.blit(number, position)
                position = [512,722]
                screen.blit(number, position)
                position = [211,928]
                screen.blit(number, position)
                position = [275,929]
                screen.blit(number, position)
                position = [477,854]
                screen.blit(number, position)

    if s.game.tilt.status == True:
        position = [537,519]
        screen.blit(tilt, position)

    pygame.display.update()

