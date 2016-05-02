
import pygame

pygame.init()
pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((720,1080))
screen.fill([0,0,0])

class scorereel():
    """ Score Reels are used to count replays """
    def __init__(self, pos, image):
        self.position = pos
        self.default_y = self.position[1]
        self.image = pygame.image.load(image).convert()

reel1 = scorereel([625,682], "coney_island/assets/green_reel.png")
reel10 = scorereel([605,682], "coney_island/assets/green_reel.png")
reel100 = scorereel([587,682], "coney_island/assets/green_reel.png")

def display(numbers, odds, gi=False, tilt=False):
    
    meter = pygame.image.load('coney_island/assets/register_cover.png').convert()
    meter.set_colorkey((255,0,252))
    meter_position = [579,683]

    screen.blit(reel1.image, reel1.position)
    screen.blit(reel10.image, reel10.position)
    screen.blit(reel100.image, reel100.position)
    screen.blit(meter, meter_position)

    backglass_position = [0, 0]
    backglass = pygame.Surface(screen.get_size(), flags=pygame.SRCALPHA)
    backglass.fill((0, 0, 0))
    if (gi == True):
        backglass = pygame.image.load('spot_lite/assets/spot_lite_gi.png')
    else:
        backglass = pygame.image.load('spot_lite/assets/spot_lite_off.png')
    backglass = pygame.transform.scale(backglass, (720, 1080))
    
    screen.blit(backglass, backglass_position)

    if odds:
        odds_position = [0,0]
        o = pygame.image.load('spot_lite/assets/spot_lite_odds' + str(odds) + '.png').convert_alpha()
        screen.blit(o, odds_position)

    if numbers:
        for n in numbers:
            number_position = [0,0]
            number = pygame.image.load('spot_lite/assets/spot_lite' + str(n) + '.png').convert_alpha()
            screen.blit(number, number_position)

    if tilt:
        tilt_position = [0,0]
        tilt = pygame.image.load('spot_lite/assets/spot_lite_tilt.png').convert_alpha()
        screen.blit(tilt, tilt_position)

    pygame.display.flip()
    pygame.display.update()

