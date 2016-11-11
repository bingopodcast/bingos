
import pygame

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

meter = pygame.image.load('graphics/assets/register_cover.png').convert()
card1_display = pygame.image.load('broadway_51/assets/broadway_51_gi.png').convert_alpha()
number = pygame.image.load('broadway_51/assets/number.png').convert_alpha()
tilt = pygame.image.load('broadway_51/assets/tilt.png').convert_alpha()

class scorereel():
    """ Score Reels are used to count replays """
    def __init__(self, pos, image):
        self.position = pos
        self.default_y = self.position[1]
        self.image = pygame.image.load(image).convert()

reel1 = scorereel([634,393], "graphics/assets/green_reel.png")
reel10 = scorereel([615,393], "graphics/assets/green_reel.png")
reel100 = scorereel([597,393], "graphics/assets/green_reel.png")

def display(s, replays=0, menu=False):
    
    meter.set_colorkey((255,0,252))
    meter_position = [588,393]

    screen.blit(reel1.image, reel1.position)
    screen.blit(reel10.image, reel10.position)
    screen.blit(reel100.image, reel100.position)
    screen.blit(meter, meter_position)

    backglass_position = [0, 0]
    backglass = pygame.Surface(screen.get_size(), flags=pygame.SRCALPHA)
    backglass.fill((0, 0, 0))
    if menu == True:
        backglass = pygame.image.load('broadway_51/assets/broadway_51_menu.png')
    else:
        if (s.game.anti_cheat.status == True):
            backglass = pygame.image.load('broadway_51/assets/broadway_51_gi.png')
        else:
            backglass = pygame.image.load('broadway_51/assets/broadway_51_off.png')
    backglass = pygame.transform.scale(backglass, (720, 1280))
    
    screen.blit(backglass, backglass_position)

    if s.game.selector.position >= 1:
        card1_position = [0,0]
        screen.blit(card1_display, card1_position)

    if s.game.tilt.status == False:
        if s.holes:
            if 1 in s.holes:
                number_position = [261,574]
                screen.blit(number, number_position)
            if 2 in s.holes:
                number_position = [329,843]
                screen.blit(number, number_position)
            if 3 in s.holes:
                number_position = [468,574]
                screen.blit(number, number_position)
            if 4 in s.holes:
                number_position = [397,842]
                screen.blit(number, number_position)
            if 5 in s.holes:
                number_position = [191,573]
                screen.blit(number, number_position)
            if 6 in s.holes:
                number_position = [191,707]
                screen.blit(number, number_position)
            if 7 in s.holes:
                number_position = [469,639]
                screen.blit(number, number_position)
            if 8 in s.holes:
                number_position = [191,638]
                screen.blit(number, number_position)
            if 9 in s.holes:
                number_position = [329,571]
                screen.blit(number, number_position)
            if 10 in s.holes:
                number_position = [329,638]
                screen.blit(number, number_position)
            if 11 in s.holes:
                number_position = [400,707]
                screen.blit(number, number_position)
            if 12 in s.holes:
                number_position = [191,841]
                screen.blit(number, number_position)
            if 13 in s.holes:
                number_position = [469,774]
                screen.blit(number, number_position)
            if 14 in s.holes:
                number_position = [329,776]
                screen.blit(number, number_position)
            if 15 in s.holes:
                number_position = [468,840]
                screen.blit(number, number_position)
            if 16 in s.holes:
                number_position = [329,707]
                screen.blit(number, number_position)
            if 17 in s.holes:
                number_position = [467,709]
                screen.blit(number, number_position)
            if 18 in s.holes:
                number_position = [259,709]
                screen.blit(number, number_position)
            if 19 in s.holes:
                number_position = [398,640]
                screen.blit(number, number_position)
            if 20 in s.holes:
                number_position = [399,773]
                screen.blit(number, number_position)
            if 21 in s.holes:
                number_position = [261,776]
                screen.blit(number, number_position)
            if 22 in s.holes:
                number_position = [261,639]
                screen.blit(number, number_position)
            if 23 in s.holes:
                number_position = [260,844]
                screen.blit(number, number_position)
            if 24 in s.holes:
                number_position = [191,775]
                screen.blit(number, number_position)
            if 25 in s.holes:
                number_position = [400,573]
                screen.blit(number, number_position)

    if s.game.tilt.status == True:
        tilt_position = [67,368]
        screen.blit(tilt, tilt_position)

    pygame.display.flip()
    pygame.display.update()

