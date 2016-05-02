import pygame

pygame.init()
pygame.display.set_caption("Coney Island")
screen = pygame.display.set_mode((720,1080))
screen.fill([0,0,0])

class scorereel():
    """ Score Reels are used to count replays """
    def __init__(self, pos, image):
        self.position = pos
        self.default_y = self.position[1]
        self.image = pygame.image.load(image).convert()

reel1 = scorereel([630,298], "coney_island/assets/green_reel.png")
reel10 = scorereel([611,298], "coney_island/assets/green_reel.png")
reel100 = scorereel([592,298], "coney_island/assets/green_reel.png")

def display(numbers, selection, gi=False, eb=False, tilt=False, eb_position=False):


    meter = pygame.image.load('coney_island/assets/register_cover.png').convert()
    meter.set_colorkey((255,0,252))
    meter_position = [585,298]

    screen.blit(reel1.image, reel1.position)
    screen.blit(reel10.image, reel10.position)
    screen.blit(reel100.image, reel100.position)
    screen.blit(meter, meter_position)

    backglass_position = [0, 0]
    backglass = pygame.Surface(screen.get_size(), flags=pygame.SRCALPHA)
    backglass.fill((0, 0, 0))
    if (gi == True):
        backglass = pygame.image.load('coney_island/assets/coney_island_gi.png')
    else:
        backglass = pygame.image.load('coney_island/assets/coney_island_off.png')
    backglass = pygame.transform.scale(backglass, (720, 1080))
    
    screen.blit(backglass, backglass_position)

    if selection >= 1:
        card1_position = [0,0]
        card1_display = pygame.image.load('coney_island/assets/coney_island_card_1.png').convert_alpha()
        screen.blit(card1_display, card1_position)
    if selection >= 2:
        card2_position = [0,0]
        card2_display = pygame.image.load('coney_island/assets/coney_island_card_2.png').convert_alpha()
        screen.blit(card2_display, card2_position)
    if selection >= 3:
        card3_position = [0,0]
        card3_display = pygame.image.load('coney_island/assets/coney_island_card_3.png').convert_alpha()
        screen.blit(card3_display, card3_position)
 
    if numbers:
        for n in numbers:
            number_position = [0,0]
            number = pygame.image.load('coney_island/assets/coney_island_' + str(n) + '.png').convert_alpha()
            screen.blit(number, number_position)

    if (eb == True):
        extra_ball = pygame.image.load('coney_island/assets/coney_island_extra_balls.png').convert_alpha()
        extra_ball_position = [0,0]
        screen.blit(extra_ball, extra_ball_position)

    if eb_position >= 1:
        eb1 = pygame.image.load('coney_island/assets/coney_island_1eb.png').convert_alpha()
        eb1_position = [0,0]
        screen.blit(eb1, eb1_position)

    if eb_position >= 2:
        eb2 = pygame.image.load('coney_island/assets/coney_island_2eb.png').convert_alpha()
        eb2_position = [0,0]
        screen.blit(eb2, eb2_position)

    if eb_position >= 3:
        eb3 = pygame.image.load('coney_island/assets/coney_island_3eb.png').convert_alpha()
        eb3_position = [0,0]
        screen.blit(eb3, eb3_position)

    if tilt:
        tilt_position = [0,0]
        tilt = pygame.image.load('coney_island/assets/coney_island_tilt.png').convert_alpha()
        screen.blit(tilt, tilt_position)

    pygame.display.flip()
    pygame.display.update()

