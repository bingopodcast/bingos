
import pygame, random

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

meter = pygame.image.load('graphics/assets/black_register_cover.png').convert()
card = pygame.image.load('hole_in_one/assets/card.png').convert_alpha()
number = pygame.image.load('hole_in_one/assets/number.png').convert_alpha()
good = pygame.image.load('hole_in_one/assets/good.png').convert_alpha()
excellent = pygame.image.load('hole_in_one/assets/excellent.png').convert_alpha()
superior = pygame.image.load('hole_in_one/assets/superior.png').convert_alpha()
tilt = pygame.image.load('hole_in_one/assets/tilt.png').convert_alpha()

class scorereel():
    """ Score Reels are used to count replays """
    def __init__(self, pos, image):
        self.position = pos
        self.default_y = self.position[1]
        self.image = pygame.image.load(image).convert()

reel1 = scorereel([357,634], "graphics/assets/white_reel.png")
reel10 = scorereel([600,375], "graphics/assets/green_reel.png")
reel100 = scorereel([600,375], "graphics/assets/green_reel.png")

def display(s, replays=0, menu=False):
    
    meter.set_colorkey((255,0,252))
    meter_position = [347,634]

    screen.blit(reel1.image, reel1.position)
    screen.blit(meter, meter_position)

    backglass_position = [0, 0]
    backglass = pygame.Surface((0,0), pygame.SRCALPHA)
    backglass.fill((0, 0, 0))
    if menu == True:
        backglass = pygame.image.load('hole_in_one/assets/hole_in_one_menu.png')
    else:
        if (s.game.anti_cheat.status == True):
            backglass = pygame.image.load('hole_in_one/assets/hole_in_one_gi.png')
        else:
            backglass = pygame.image.load('hole_in_one/assets/hole_in_one_off.png')
    screen.blit(backglass, backglass_position)

    if s.game.selector.position >= 1:
        card1_position = [141,383]
        screen.blit(card, card1_position)
    if s.game.selector.position >= 2:
        card2_position = [345,370]
        screen.blit(card, card2_position)
    if s.game.selector.position >= 3:
        card3_position = [545,386]
        screen.blit(card, card3_position)
    if s.game.selector.position >= 4:
        card4_position = [140,727]
        screen.blit(card, card4_position)
    if s.game.selector.position >= 5:
        card5_position = [342,743]
        screen.blit(card, card5_position)
    if s.game.selector.position >= 6:
        card6_position = [542,724]
        screen.blit(card, card6_position)

    if s.game.tilt.status == False:
        if s.holes:
            if 1 in s.holes:
                number_position = [111,433]
                screen.blit(number, number_position)
                number_position = [280,518]
                screen.blit(number, number_position)
                number_position = [584,566]
                screen.blit(number, number_position)
                number_position = [214,777]
                screen.blit(number, number_position)
                number_position = [279,926]
                screen.blit(number, number_position)
                number_position = [549,774]
                screen.blit(number, number_position)
            if 2 in s.holes:
                number_position = [146,566]
                screen.blit(number, number_position)
                number_position = [280,485]
                screen.blit(number, number_position)
                number_position = [618,502]
                screen.blit(number, number_position)
                number_position = [214,812]
                screen.blit(number, number_position)
                number_position = [279,827]
                screen.blit(number, number_position)
                number_position = [583,907]
                screen.blit(number, number_position)

            if 3 in s.holes:
                number_position = [214,434]
                screen.blit(number, number_position)
                number_position = [417,552]
                screen.blit(number, number_position)
                number_position = [483,435]
                screen.blit(number, number_position)
                number_position = [145,779]
                screen.blit(number, number_position)
                number_position = [383,925]
                screen.blit(number, number_position)
                number_position = [549,809]
                screen.blit(number, number_position)

            if 4 in s.holes:
                number_position = [180,566]
                screen.blit(number, number_position)
                number_position = [384,420]
                screen.blit(number, number_position)
                number_position = [584,436]
                screen.blit(number, number_position)
                number_position = [180,912]
                screen.blit(number, number_position)
                number_position = [416,792]
                screen.blit(number, number_position)
                number_position = [480,776]
                screen.blit(number, number_position)
            if 5 in s.holes:
                number_position = [75,433]
                screen.blit(number, number_position)
                number_position = [349,551]
                screen.blit(number, number_position)
                number_position = [618,568]
                screen.blit(number, number_position)
                number_position = [74,848]
                screen.blit(number, number_position)
                number_position = [416,859]
                screen.blit(number, number_position)
                number_position = [616,776]
                screen.blit(number, number_position)
            if 6 in s.holes:
                number_position = [75,499]
                screen.blit(number, number_position)
                number_position = [417,420]
                screen.blit(number, number_position)
                number_position = [482,566]
                screen.blit(number, number_position)
                number_position = [75,780]
                screen.blit(number, number_position)
                number_position = [417,924]
                screen.blit(number, number_position)
                number_position = [516,775]
                screen.blit(number, number_position)

            if 7 in s.holes:
                number_position = [214,467]
                screen.blit(number, number_position)
                number_position = [316,551]
                screen.blit(number, number_position)
                number_position = [518,435]
                screen.blit(number, number_position)
                number_position = [112,778]
                screen.blit(number, number_position)
                number_position = [315,925]
                screen.blit(number, number_position)
                number_position = [482,907]
                screen.blit(number, number_position)

            if 8 in s.holes:
                number_position = [75,466]
                screen.blit(number, number_position)
                number_position = [418,518]
                screen.blit(number, number_position)
                number_position = [618,468]
                screen.blit(number, number_position)
                number_position = [214,911]
                screen.blit(number, number_position)
                number_position = [279,793]
                screen.blit(number, number_position)
                number_position = [617,874]
                screen.blit(number, number_position)

            if 9 in s.holes:
                number_position = [145,433]
                screen.blit(number, number_position)
                number_position = [281,421]
                screen.blit(number, number_position)
                number_position = [619,437]
                screen.blit(number, number_position)
                number_position = [144,879]
                screen.blit(number, number_position)
                number_position = [349,891]
                screen.blit(number, number_position)
                number_position = [481,841]
                screen.blit(number, number_position)

            if 10 in s.holes:
                number_position = [145,466]
                screen.blit(number, number_position)
                number_position = [280,551]
                screen.blit(number, number_position)
                number_position = [551,436]
                screen.blit(number, number_position)
                number_position = [74,913]
                screen.blit(number, number_position)
                number_position = [349,792]
                screen.blit(number, number_position)
                number_position = [481,875]
                screen.blit(number, number_position)

            if 11 in s.holes:
                number_position = [180,500]
                screen.blit(number, number_position)
                number_position = [350,517]
                screen.blit(number, number_position)
                number_position = [585,502]
                screen.blit(number, number_position)
                number_position = [75,880]
                screen.blit(number, number_position)
                number_position = [416,891]
                screen.blit(number, number_position)
                number_position = [617,907]
                screen.blit(number, number_position)

            if 12 in s.holes:
                number_position = [75,565]
                screen.blit(number, number_position)
                number_position = [384,486]
                screen.blit(number, number_position)
                number_position = [550,534]
                screen.blit(number, number_position)
                number_position = [144,813]
                screen.blit(number, number_position)
                number_position = [315,860]
                screen.blit(number, number_position)
                number_position = [583,841]
                screen.blit(number, number_position)

            if 13 in s.holes:
                number_position = [214,533]
                screen.blit(number, number_position)
                number_position = [279,452]
                screen.blit(number, number_position)
                number_position = [483,533]
                screen.blit(number, number_position)
                number_position = [110,912]
                screen.blit(number, number_position)
                number_position = [382,792]
                screen.blit(number, number_position)
                number_position = [616,807]
                screen.blit(number, number_position)

            if 14 in s.holes:
                number_position = [146,532]
                screen.blit(number, number_position)
                number_position = [349,452]
                screen.blit(number, number_position)
                number_position = [517,501]
                screen.blit(number, number_position)
                number_position = [111,812]
                screen.blit(number, number_position)
                number_position = [383,824]
                screen.blit(number, number_position)
                number_position = [582,874]
                screen.blit(number, number_position)

            if 15 in s.holes:
                number_position = [215,566]
                screen.blit(number, number_position)
                number_position = [350,485]
                screen.blit(number, number_position)
                number_position = [482,501]
                screen.blit(number, number_position)
                number_position = [179,878]
                screen.blit(number, number_position)
                number_position = [314,893]
                screen.blit(number, number_position)
                number_position = [515,808]
                screen.blit(number, number_position)

            if 16 in s.holes:
                number_position = [145,500]
                screen.blit(number, number_position)
                number_position = [349,419]
                screen.blit(number, number_position)
                number_position = [550,566]
                screen.blit(number, number_position)
                number_position = [180,846]
                screen.blit(number, number_position)
                number_position = [348,826]
                screen.blit(number, number_position)
                number_position = [549,874]
                screen.blit(number, number_position)

            if 17 in s.holes:
                number_position = [215,500]
                screen.blit(number, number_position)
                number_position = [418,485]
                screen.blit(number, number_position)
                number_position = [550,501]
                screen.blit(number, number_position)
                number_position = [110,880]
                screen.blit(number, number_position)
                number_position = [315,826]
                screen.blit(number, number_position)
                number_position = [583,808]
                screen.blit(number, number_position)

            if 18 in s.holes:
                number_position = [111,499]
                screen.blit(number, number_position)
                number_position = [316,484]
                screen.blit(number, number_position)
                number_position = [550,468]
                screen.blit(number, number_position)
                number_position = [179,812]
                screen.blit(number, number_position)
                number_position = [382,892]
                screen.blit(number, number_position)
                number_position = [515,874]
                screen.blit(number, number_position)

            if 19 in s.holes:
                number_position = [180,466]
                screen.blit(number, number_position)
                number_position = [316,452]
                screen.blit(number, number_position)
                number_position = [583,534]
                screen.blit(number, number_position)
                number_position = [111,846]
                screen.blit(number, number_position)
                number_position = [383,859]
                screen.blit(number, number_position)
                number_position = [515,842]
                screen.blit(number, number_position)

            if 20 in s.holes:
                number_position = [180,532]
                screen.blit(number, number_position)
                number_position = [384,452]
                screen.blit(number, number_position)
                number_position = [517,534]
                screen.blit(number, number_position)
                number_position = [145,845]
                screen.blit(number, number_position)
                number_position = [279,859]
                screen.blit(number, number_position)
                number_position = [616,841]
                screen.blit(number, number_position)

            if 21 in s.holes:
                number_position = [111,532]
                screen.blit(number, number_position)
                number_position = [384,517]
                screen.blit(number, number_position)
                number_position = [517,467]
                screen.blit(number, number_position)
                number_position = [144,912]
                screen.blit(number, number_position)
                number_position = [349,925]
                screen.blit(number, number_position)
                number_position = [549,842]
                screen.blit(number, number_position)

            if 22 in s.holes:
                number_position = [111,465]
                screen.blit(number, number_position)
                number_position = [316,518]
                screen.blit(number, number_position)
                number_position = [585,469]
                screen.blit(number, number_position)
                number_position = [214,844]
                screen.blit(number, number_position)
                number_position = [348,860]
                screen.blit(number, number_position)
                number_position = [549,907]
                screen.blit(number, number_position)

            if 23 in s.holes:
                number_position = [111,566]
                screen.blit(number, number_position)
                number_position = [384,550]
                screen.blit(number, number_position)
                number_position = [618,535]
                screen.blit(number, number_position)
                number_position = [75,814]
                screen.blit(number, number_position)
                number_position = [315,792]
                screen.blit(number, number_position)
                number_position = [583,775]
                screen.blit(number, number_position)

            if 24 in s.holes:
                number_position = [74,532]
                screen.blit(number, number_position)
                number_position = [316,419]
                screen.blit(number, number_position)
                number_position = [482,468]
                screen.blit(number, number_position)
                number_position = [180,778]
                screen.blit(number, number_position)
                number_position = [417,825]
                screen.blit(number, number_position)
                number_position = [515,907]
                screen.blit(number, number_position)

            if 25 in s.holes:
                number_position = [180,433]
                screen.blit(number, number_position)
                number_position = [418,452]
                screen.blit(number, number_position)
                number_position = [516,565]
                screen.blit(number, number_position)
                number_position = [213,878]
                screen.blit(number, number_position)
                number_position = [280,893]
                screen.blit(number, number_position)
                number_position = [480,808]
                screen.blit(number, number_position)

    if s.game.good.status == True:
        p = [48,692]
        screen.blit(good, p)
    if s.game.excellent.status == True:
        p = [48,668]
        screen.blit(excellent, p)
    if s.game.superior.status == True:
        p = [48,645]
        screen.blit(superior, p)


    if s.game.tilt.status == True:
        tilt_position = [55,375]
        screen.blit(tilt, tilt_position)

    pygame.display.flip()
    pygame.display.update()


