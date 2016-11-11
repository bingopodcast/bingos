
import pygame, random

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

meter = pygame.image.load('graphics/assets/register_cover.png').convert()
card = pygame.image.load('bright_spot/assets/card.png').convert_alpha()
number = pygame.image.load('bright_spot/assets/number.png').convert_alpha()
tilt = pygame.image.load('bright_spot/assets/tilt.png').convert_alpha()

class scorereel():
    """ Score Reels are used to count replays """
    def __init__(self, pos, image):
        self.position = pos
        self.default_y = self.position[1]
        self.image = pygame.image.load(image).convert()

reel1 = scorereel([609,397], "graphics/assets/green_reel.png")
reel10 = scorereel([591,397], "graphics/assets/green_reel.png")
reel100 = scorereel([571,397], "graphics/assets/green_reel.png")

def display(s, replays=0, menu=False):
    
    meter.set_colorkey((255,0,252))
    meter_position = [562,397]

    screen.blit(reel1.image, reel1.position)
    screen.blit(reel10.image, reel10.position)
    screen.blit(reel100.image, reel100.position)
    screen.blit(meter, meter_position)

    backglass_position = [0, 0]
    backglass = pygame.Surface((0,0), pygame.SRCALPHA)
    backglass.fill((0, 0, 0))
    if menu == True:
        backglass = pygame.image.load('bright_spot/assets/bright_spot_menu.png')
    else:
        if (s.game.anti_cheat.status == True):
            backglass = pygame.image.load('bright_spot/assets/bright_spot_gi.png')
        else:
            backglass = pygame.image.load('bright_spot/assets/bright_spot_off.png')
    screen.blit(backglass, backglass_position)

    if s.game.selector.position >= 1:
        card1_position = [88,694]
        screen.blit(card, card1_position)
    if s.game.selector.position >= 2:
        card2_position = [292,694]
        screen.blit(card, card2_position)
    if s.game.selector.position >= 3:
        card3_position = [496,694]
        screen.blit(card, card3_position)
    if s.game.selector.position >= 4:
        card4_position = [90,911]
        screen.blit(card, card4_position)
    if s.game.selector.position >= 5:
        card5_position = [293,910]
        screen.blit(card, card5_position)
    if s.game.selector.position >= 6:
        card6_position = [495,908]
        screen.blit(card, card6_position)

    if s.game.tilt.status == False:
        if s.holes:
            if 1 in s.holes:
                number_position = [103,523]
                screen.blit(number, number_position)
                number_position = [273,624]
                screen.blit(number, number_position)
                number_position = [583,656]
                screen.blit(number, number_position)
                number_position = [209,743]
                screen.blit(number, number_position)
                number_position = [275,875]
                screen.blit(number, number_position)
                number_position = [547,742]
                screen.blit(number, number_position)
            if 2 in s.holes:
                number_position = [139,658]
                screen.blit(number, number_position)
                number_position = [273,590]
                screen.blit(number, number_position)
                number_position = [616,590]
                screen.blit(number, number_position)
                number_position = [210,776]
                screen.blit(number, number_position)
                number_position = [275,777]
                screen.blit(number, number_position)
                number_position = [581,873]
                screen.blit(number, number_position)

            if 3 in s.holes:
                number_position = [208,523]
                screen.blit(number, number_position)
                number_position = [413,656]
                screen.blit(number, number_position)
                number_position = [479,522]
                screen.blit(number, number_position)
                number_position = [140,742]
                screen.blit(number, number_position)
                number_position = [379,874]
                screen.blit(number, number_position)
                number_position = [547,775]
                screen.blit(number, number_position)

            if 4 in s.holes:
                number_position = [175,658]
                screen.blit(number, number_position)
                number_position = [378,523]
                screen.blit(number, number_position)
                number_position = [582,523]
                screen.blit(number, number_position)
                number_position = [176,875]
                screen.blit(number, number_position)
                number_position = [413,742]
                screen.blit(number, number_position)
                number_position = [479,742]
                screen.blit(number, number_position)
            if 5 in s.holes:
                number_position = [69,523]
                screen.blit(number, number_position)
                number_position = [344,657]
                screen.blit(number, number_position)
                number_position = [617,658]
                screen.blit(number, number_position)
                number_position = [72,810]
                screen.blit(number, number_position)
                number_position = [413,810]
                screen.blit(number, number_position)
                number_position = [616,742]
                screen.blit(number, number_position)
            if 6 in s.holes:
                number_position = [69,589]
                screen.blit(number, number_position)
                number_position = [412,522]
                screen.blit(number, number_position)
                number_position = [478,656]
                screen.blit(number, number_position)
                number_position = [71,742]
                screen.blit(number, number_position)
                number_position = [413,874]
                screen.blit(number, number_position)
                number_position = [513,741]
                screen.blit(number, number_position)

            if 7 in s.holes:
                number_position = [207,556]
                screen.blit(number, number_position)
                number_position = [309,657]
                screen.blit(number, number_position)
                number_position = [513,522]
                screen.blit(number, number_position)
                number_position = [106,742]
                screen.blit(number, number_position)
                number_position = [310,874]
                screen.blit(number, number_position)
                number_position = [479,875]
                screen.blit(number, number_position)

            if 8 in s.holes:
                number_position = [69,557]
                screen.blit(number, number_position)
                number_position = [413,623]
                screen.blit(number, number_position)
                number_position = [616,555]
                screen.blit(number, number_position)
                number_position = [211,875]
                screen.blit(number, number_position)
                number_position = [274,741]
                screen.blit(number, number_position)
                number_position = [615,840]
                screen.blit(number, number_position)

            if 9 in s.holes:
                number_position = [137,523]
                screen.blit(number, number_position)
                number_position = [273,522]
                screen.blit(number, number_position)
                number_position = [616,522]
                screen.blit(number, number_position)
                number_position = [141,843]
                screen.blit(number, number_position)
                number_position = [344,841]
                screen.blit(number, number_position)
                number_position = [479,807]
                screen.blit(number, number_position)

            if 10 in s.holes:
                number_position = [138,556]
                screen.blit(number, number_position)
                number_position = [273,656]
                screen.blit(number, number_position)
                number_position = [547,522]
                screen.blit(number, number_position)
                number_position = [72,875]
                screen.blit(number, number_position)
                number_position = [344,742]
                screen.blit(number, number_position)
                number_position = [478,840]
                screen.blit(number, number_position)

            if 11 in s.holes:
                number_position = [174,589]
                screen.blit(number, number_position)
                number_position = [344,624]
                screen.blit(number, number_position)
                number_position = [582,589]
                screen.blit(number, number_position)
                number_position = [73,841]
                screen.blit(number, number_position)
                number_position = [413,841]
                screen.blit(number, number_position)
                number_position = [615,871]
                screen.blit(number, number_position)

            if 12 in s.holes:
                number_position = [70,657]
                screen.blit(number, number_position)
                number_position = [378,589]
                screen.blit(number, number_position)
                number_position = [547,624]
                screen.blit(number, number_position)
                number_position = [140,776]
                screen.blit(number, number_position)
                number_position = [309,807]
                screen.blit(number, number_position)
                number_position = [581,807]
                screen.blit(number, number_position)

            if 13 in s.holes:
                number_position = [207,624]
                screen.blit(number, number_position)
                number_position = [276,556]
                screen.blit(number, number_position)
                number_position = [478,623]
                screen.blit(number, number_position)
                number_position = [107,875]
                screen.blit(number, number_position)
                number_position = [379,742]
                screen.blit(number, number_position)
                number_position = [615,774]
                screen.blit(number, number_position)

            if 14 in s.holes:
                number_position = [138,624]
                screen.blit(number, number_position)
                number_position = [343,555]
                screen.blit(number, number_position)
                number_position = [512,589]
                screen.blit(number, number_position)
                number_position = [106,776]
                screen.blit(number, number_position)
                number_position = [379,775]
                screen.blit(number, number_position)
                number_position = [580,840]
                screen.blit(number, number_position)

            if 15 in s.holes:
                number_position = [208,658]
                screen.blit(number, number_position)
                number_position = [342,590]
                screen.blit(number, number_position)
                number_position = [478,589]
                screen.blit(number, number_position)
                number_position = [176,841]
                screen.blit(number, number_position)
                number_position = [310,842]
                screen.blit(number, number_position)
                number_position = [513,775]
                screen.blit(number, number_position)

            if 16 in s.holes:
                number_position = [139,588]
                screen.blit(number, number_position)
                number_position = [343,522]
                screen.blit(number, number_position)
                number_position = [547,657]
                screen.blit(number, number_position)
                number_position = [177,810]
                screen.blit(number, number_position)
                number_position = [344,776]
                screen.blit(number, number_position)
                number_position = [547,841]
                screen.blit(number, number_position)

            if 17 in s.holes:
                number_position = [207,589]
                screen.blit(number, number_position)
                number_position = [412,590]
                screen.blit(number, number_position)
                number_position = [547,589]
                screen.blit(number, number_position)
                number_position = [106,842]
                screen.blit(number, number_position)
                number_position = [310,776]
                screen.blit(number, number_position)
                number_position = [582,774]
                screen.blit(number, number_position)

            if 18 in s.holes:
                number_position = [103,590]
                screen.blit(number, number_position)
                number_position = [308,589]
                screen.blit(number, number_position)
                number_position = [547,556]
                screen.blit(number, number_position)
                number_position = [175,776]
                screen.blit(number, number_position)
                number_position = [378,841]
                screen.blit(number, number_position)
                number_position = [512,840]
                screen.blit(number, number_position)

            if 19 in s.holes:
                number_position = [173,557]
                screen.blit(number, number_position)
                number_position = [309,557]
                screen.blit(number, number_position)
                number_position = [582,623]
                screen.blit(number, number_position)
                number_position = [106,809]
                screen.blit(number, number_position)
                number_position = [378,808]
                screen.blit(number, number_position)
                number_position = [513,808]
                screen.blit(number, number_position)

            if 20 in s.holes:
                number_position = [174,623]
                screen.blit(number, number_position)
                number_position = [378,557]
                screen.blit(number, number_position)
                number_position = [513,624]
                screen.blit(number, number_position)
                number_position = [140,809]
                screen.blit(number, number_position)
                number_position = [274,809]
                screen.blit(number, number_position)
                number_position = [616,808]
                screen.blit(number, number_position)

            if 21 in s.holes:
                number_position = [104,623]
                screen.blit(number, number_position)
                number_position = [378,623]
                screen.blit(number, number_position)
                number_position = [513,556]
                screen.blit(number, number_position)
                number_position = [142,875]
                screen.blit(number, number_position)
                number_position = [345,874]
                screen.blit(number, number_position)
                number_position = [549,807]
                screen.blit(number, number_position)

            if 22 in s.holes:
                number_position = [104,555]
                screen.blit(number, number_position)
                number_position = [309,623]
                screen.blit(number, number_position)
                number_position = [582,556]
                screen.blit(number, number_position)
                number_position = [210,809]
                screen.blit(number, number_position)
                number_position = [345,808]
                screen.blit(number, number_position)
                number_position = [546,874]
                screen.blit(number, number_position)

            if 23 in s.holes:
                number_position = [104,658]
                screen.blit(number, number_position)
                number_position = [378,657]
                screen.blit(number, number_position)
                number_position = [616,623]
                screen.blit(number, number_position)
                number_position = [71,776]
                screen.blit(number, number_position)
                number_position = [309,742]
                screen.blit(number, number_position)
                number_position = [582,741]
                screen.blit(number, number_position)

            if 24 in s.holes:
                number_position = [69,623]
                screen.blit(number, number_position)
                number_position = [309,523]
                screen.blit(number, number_position)
                number_position = [478,557]
                screen.blit(number, number_position)
                number_position = [175,742]
                screen.blit(number, number_position)
                number_position = [413,775]
                screen.blit(number, number_position)
                number_position = [512,874]
                screen.blit(number, number_position)

            if 25 in s.holes:
                number_position = [174,522]
                screen.blit(number, number_position)
                number_position = [412,556]
                screen.blit(number, number_position)
                number_position = [512,657]
                screen.blit(number, number_position)
                number_position = [210,842]
                screen.blit(number, number_position)
                number_position = [275,842]
                screen.blit(number, number_position)
                number_position = [479,775]
                screen.blit(number, number_position)


    if s.game.tilt.status == True:
        tilt_position = [74,449]
        screen.blit(tilt, tilt_position)

    pygame.display.flip()
    pygame.display.update()


