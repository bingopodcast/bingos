
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

reel1 = scorereel([634,293], "coney_island/assets/green_reel.png")
reel10 = scorereel([615,293], "coney_island/assets/green_reel.png")
reel100 = scorereel([597,293], "coney_island/assets/green_reel.png")

def display(numbers, selection, gi=False, tilt=False):
    
    meter = pygame.image.load('broadway_51/assets/register_cover.png').convert()
    meter.set_colorkey((255,0,252))
    meter_position = [589,295]

    screen.blit(reel1.image, reel1.position)
    screen.blit(reel10.image, reel10.position)
    screen.blit(reel100.image, reel100.position)
    screen.blit(meter, meter_position)

    backglass_position = [0, 0]
    backglass = pygame.Surface(screen.get_size(), flags=pygame.SRCALPHA)
    backglass.fill((0, 0, 0))
    if (gi == True):
        backglass = pygame.image.load('broadway_51/assets/broadway_51_gi.png')
    else:
        backglass = pygame.image.load('broadway_51/assets/broadway_51_off.png')
    backglass = pygame.transform.scale(backglass, (720, 1080))
    
    screen.blit(backglass, backglass_position)

    if selection >= 1:
        card1_position = [0,0]
        card1_display = pygame.image.load('broadway_51/assets/broadway_51_gi.png').convert_alpha()
        screen.blit(card1_display, card1_position)

 
    if numbers:
        for n in numbers:
            number_position = [0,0]
            number = pygame.image.load('broadway_51/assets/broadway_51_' + str(n) + '.png').convert_alpha()
            screen.blit(number, number_position)

    if tilt:
        tilt_position = [0,0]
        tilt = pygame.image.load('broadway_51/assets/broadway_51_tilt.png').convert_alpha()
        screen.blit(tilt, tilt_position)

    pygame.display.flip()
    pygame.display.update()

