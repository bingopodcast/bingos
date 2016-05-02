
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

reel1 = scorereel([634,277], "coney_island/assets/green_reel.png")
reel10 = scorereel([615,277], "coney_island/assets/green_reel.png")
reel100 = scorereel([597,277], "coney_island/assets/green_reel.png")

def display(numbers, selection, gi=False, tilt=False):
    
    meter = pygame.image.load('bright_lights/assets/register_cover.png').convert()
    meter.set_colorkey((255,0,252))
    meter_position = [589,278]

    screen.blit(reel1.image, reel1.position)
    screen.blit(reel10.image, reel10.position)
    screen.blit(reel100.image, reel100.position)
    screen.blit(meter, meter_position)

    backglass_position = [0, 0]
    backglass = pygame.Surface(screen.get_size(), flags=pygame.SRCALPHA)
    backglass.fill((0, 0, 0))
    if (gi == True):
        backglass = pygame.image.load('bright_lights/assets/bright_lights_gi.png')
    else:
        backglass = pygame.image.load('bright_lights/assets/bright_lights_off.png')
    backglass = pygame.transform.scale(backglass, (720, 1080))
    
    screen.blit(backglass, backglass_position)

    if selection >= 1:
        card1_position = [0,0]
        card1_display = pygame.image.load('bright_lights/assets/bright_lights_card_1.png').convert_alpha()
        screen.blit(card1_display, card1_position)
    if selection >= 2:
        card2_position = [0,0]
        card2_display = pygame.image.load('bright_lights/assets/bright_lights_card_2.png').convert_alpha()
        screen.blit(card2_display, card2_position)
    if selection >= 3:
        card3_position = [0,0]
        card3_display = pygame.image.load('bright_lights/assets/bright_lights_card_3.png').convert_alpha()
        screen.blit(card3_display, card3_position)
    if selection >= 4:
        card4_position = [0,0]
        card4_display = pygame.image.load('bright_lights/assets/bright_lights_card_4.png').convert_alpha()
        screen.blit(card4_display, card4_position)
    if selection >= 5:
        card5_position = [0,0]
        card5_display = pygame.image.load('bright_lights/assets/bright_lights_card_5.png').convert_alpha()
        screen.blit(card5_display, card5_position)
    if selection >= 6:
        card6_position = [0,0]
        card6_display = pygame.image.load('bright_lights/assets/bright_lights_card_6.png').convert_alpha()
        screen.blit(card6_display, card6_position)


 
    if numbers:
        for n in numbers:
            number_position = [0,0]
            number = pygame.image.load('bright_lights/assets/bright_lights_' + str(n) + '.png').convert_alpha()
            screen.blit(number, number_position)

    if tilt:
        tilt_position = [0,0]
        tilt = pygame.image.load('bright_lights/assets/bright_lights_tilt.png').convert_alpha()
        screen.blit(tilt, tilt_position)

    pygame.display.flip()
    pygame.display.update()

