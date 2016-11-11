
import pygame, random

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

meter = pygame.image.load('graphics/assets/register_cover.png').convert()
card = pygame.image.load('holiday/assets/card.png').convert_alpha()
triple = pygame.image.load('holiday/assets/triple.png').convert_alpha()
number = pygame.image.load('holiday/assets/number.png').convert_alpha()
tilt = pygame.image.load('holiday/assets/tilt.png').convert_alpha()
sf = pygame.image.load('holiday/assets/sf.png').convert_alpha()

class scorereel():
    """ Score Reels are used to count replays """
    def __init__(self, pos, image):
        self.position = pos
        self.default_y = self.position[1]
        self.image = pygame.image.load(image).convert()

reel1 = scorereel([603,432], "graphics/assets/green_reel.png")
reel10 = scorereel([584,432], "graphics/assets/green_reel.png")
reel100 = scorereel([565,432], "graphics/assets/green_reel.png")

def display(s, replays=0, menu=False):
    
    meter.set_colorkey((255,0,252))
    meter_position = [555,432]

    screen.blit(reel1.image, reel1.position)
    screen.blit(reel10.image, reel10.position)
    screen.blit(reel100.image, reel100.position)
    screen.blit(meter, meter_position)

    backglass_position = [0, 0]
    backglass = pygame.Surface((0,0), pygame.SRCALPHA)
    backglass.fill((0, 0, 0))
    if menu == True:
        backglass = pygame.image.load('holiday/assets/holiday_menu.png')
    else:
        if (s.game.anti_cheat.status == True):
            backglass = pygame.image.load('holiday/assets/holiday_gi.png')
        else:
            backglass = pygame.image.load('holiday/assets/holiday_off.png')
    screen.blit(backglass, backglass_position)

    if s.game.selector.position >= 1:
        card1_position = [91,683]
        screen.blit(card, card1_position)
    if s.game.selector.position >= 2:
        card2_position = [292,684]
        screen.blit(card, card2_position)
    if s.game.selector.position >= 3:
        card3_position = [491,684]
        screen.blit(card, card3_position)
    if s.game.selector.position >= 4:
        card4_position = [93,869]
        screen.blit(card, card4_position)
    if s.game.selector.position >= 5:
        card5_position = [293,870]
        screen.blit(card, card5_position)
    if s.game.selector.position >= 6:
        card6_position = [494,871]
        screen.blit(card, card6_position)

    if s.game.special_1.status == True:
        p = [132,686]
        screen.blit(triple, p)
    if s.game.special_2.status == True:
        p = [335,686]
        screen.blit(triple, p)
    if s.game.special_3.status == True:
        p = [534,686]
        screen.blit(triple, p)
    if s.game.special_4.status == True:
        p = [136,872]
        screen.blit(triple, p)
    if s.game.special_5.status == True:
        p = [336,872]
        screen.blit(triple, p)
    if s.game.special_6.status == True:
        p = [538,873]
        screen.blit(triple, p)

    if s.game.special_feature.status == True:
        p = [48,401]
        screen.blit(sf, p)

    if s.game.tilt.status == False:
        if s.holes:
            if 1 in s.holes:
                number_position = [109,542]
                screen.blit(number, number_position)
                number_position = [278,628]
                screen.blit(number, number_position)
                number_position = [580,655]
                screen.blit(number, number_position)
                number_position = [214,728]
                screen.blit(number, number_position)
                number_position = [279,840]
                screen.blit(number, number_position)
                number_position = [546,728]
                screen.blit(number, number_position)
            if 2 in s.holes:
                number_position = [145,656]
                screen.blit(number, number_position)
                number_position = [277,600]
                screen.blit(number, number_position)
                number_position = [614,599]
                screen.blit(number, number_position)
                number_position = [213,756]
                screen.blit(number, number_position)
                number_position = [278,753]
                screen.blit(number, number_position)
                number_position = [582,841]
                screen.blit(number, number_position)

            if 3 in s.holes:
                number_position = [211,541]
                screen.blit(number, number_position)
                number_position = [411,655]
                screen.blit(number, number_position)
                number_position = [475,543]
                screen.blit(number, number_position)
                number_position = [144,727]
                screen.blit(number, number_position)
                number_position = [380,839]
                screen.blit(number, number_position)
                number_position = [546,755]
                screen.blit(number, number_position)

            if 4 in s.holes:
                number_position = [179,655]
                screen.blit(number, number_position)
                number_position = [376,542]
                screen.blit(number, number_position)
                number_position = [577,541]
                screen.blit(number, number_position)
                number_position = [179,841]
                screen.blit(number, number_position)
                number_position = [411,725]
                screen.blit(number, number_position)
                number_position = [477,725]
                screen.blit(number, number_position)
            if 5 in s.holes:
                number_position = [72,540]
                screen.blit(number, number_position)
                number_position = [342,655]
                screen.blit(number, number_position)
                number_position = [613,655]
                screen.blit(number, number_position)
                number_position = [74,784]
                screen.blit(number, number_position)
                number_position = [412,783]
                screen.blit(number, number_position)
                number_position = [614,727]
                screen.blit(number, number_position)
            if 6 in s.holes:
                number_position = [72,597]
                screen.blit(number, number_position)
                number_position = [409,544]
                screen.blit(number, number_position)
                number_position = [478,655]
                screen.blit(number, number_position)
                number_position = [74,727]
                screen.blit(number, number_position)
                number_position = [414,839]
                screen.blit(number, number_position)
                number_position = [510,726]
                screen.blit(number, number_position)

            if 7 in s.holes:
                number_position = [211,570]
                screen.blit(number, number_position)
                number_position = [310,655]
                screen.blit(number, number_position)
                number_position = [508,541]
                screen.blit(number, number_position)
                number_position = [110,726]
                screen.blit(number, number_position)
                number_position = [311,839]
                screen.blit(number, number_position)
                number_position = [478,840]
                screen.blit(number, number_position)

            if 8 in s.holes:
                number_position = [73,570]
                screen.blit(number, number_position)
                number_position = [411,628]
                screen.blit(number, number_position)
                number_position = [612,571]
                screen.blit(number, number_position)
                number_position = [213,840]
                screen.blit(number, number_position)
                number_position = [277,725]
                screen.blit(number, number_position)
                number_position = [615,813]
                screen.blit(number, number_position)

            if 9 in s.holes:
                number_position = [141,541]
                screen.blit(number, number_position)
                number_position = [274,541]
                screen.blit(number, number_position)
                number_position = [612,541]
                screen.blit(number, number_position)
                number_position = [144,813]
                screen.blit(number, number_position)
                number_position = [345,810]
                screen.blit(number, number_position)
                number_position = [477,784]
                screen.blit(number, number_position)

            if 10 in s.holes:
                number_position = [142,570]
                screen.blit(number, number_position)
                number_position = [276,655]
                screen.blit(number, number_position)
                number_position = [543,542]
                screen.blit(number, number_position)
                number_position = [76,841]
                screen.blit(number, number_position)
                number_position = [344,726]
                screen.blit(number, number_position)
                number_position = [477,812]
                screen.blit(number, number_position)

            if 11 in s.holes:
                number_position = [178,598]
                screen.blit(number, number_position)
                number_position = [344,627]
                screen.blit(number, number_position)
                number_position = [578,600]
                screen.blit(number, number_position)
                number_position = [75,814]
                screen.blit(number, number_position)
                number_position = [412,812]
                screen.blit(number, number_position)
                number_position = [616,842]
                screen.blit(number, number_position)

            if 12 in s.holes:
                number_position = [73,655]
                screen.blit(number, number_position)
                number_position = [377,600]
                screen.blit(number, number_position)
                number_position = [543,628]
                screen.blit(number, number_position)
                number_position = [143,756]
                screen.blit(number, number_position)
                number_position = [311,783]
                screen.blit(number, number_position)
                number_position = [581,785]
                screen.blit(number, number_position)

            if 13 in s.holes:
                number_position = [213,627]
                screen.blit(number, number_position)
                number_position = [275,569]
                screen.blit(number, number_position)
                number_position = [475,627]
                screen.blit(number, number_position)
                number_position = [109,841]
                screen.blit(number, number_position)
                number_position = [377,726]
                screen.blit(number, number_position)
                number_position = [614,756]
                screen.blit(number, number_position)

            if 14 in s.holes:
                number_position = [142,627]
                screen.blit(number, number_position)
                number_position = [343,570]
                screen.blit(number, number_position)
                number_position = [508,599]
                screen.blit(number, number_position)
                number_position = [109,756]
                screen.blit(number, number_position)
                number_position = [378,754]
                screen.blit(number, number_position)
                number_position = [581,813]
                screen.blit(number, number_position)

            if 15 in s.holes:
                number_position = [213,654]
                screen.blit(number, number_position)
                number_position = [344,599]
                screen.blit(number, number_position)
                number_position = [475,599]
                screen.blit(number, number_position)
                number_position = [178,812]
                screen.blit(number, number_position)
                number_position = [311,811]
                screen.blit(number, number_position)
                number_position = [510,754]
                screen.blit(number, number_position)

            if 16 in s.holes:
                number_position = [142,597]
                screen.blit(number, number_position)
                number_position = [342,542]
                screen.blit(number, number_position)
                number_position = [544,655]
                screen.blit(number, number_position)
                number_position = [179,783]
                screen.blit(number, number_position)
                number_position = [345,754]
                screen.blit(number, number_position)
                number_position = [547,812]
                screen.blit(number, number_position)

            if 17 in s.holes:
                number_position = [212,599]
                screen.blit(number, number_position)
                number_position = [410,599]
                screen.blit(number, number_position)
                number_position = [543,599]
                screen.blit(number, number_position)
                number_position = [110,813]
                screen.blit(number, number_position)
                number_position = [311,753]
                screen.blit(number, number_position)
                number_position = [580,757]
                screen.blit(number, number_position)

            if 18 in s.holes:
                number_position = [108,598]
                screen.blit(number, number_position)
                number_position = [310,599]
                screen.blit(number, number_position)
                number_position = [544,572]
                screen.blit(number, number_position)
                number_position = [179,756]
                screen.blit(number, number_position)
                number_position = [380,811]
                screen.blit(number, number_position)
                number_position = [512,813]
                screen.blit(number, number_position)

            if 19 in s.holes:
                number_position = [177,570]
                screen.blit(number, number_position)
                number_position = [309,571]
                screen.blit(number, number_position)
                number_position = [578,627]
                screen.blit(number, number_position)
                number_position = [108,784]
                screen.blit(number, number_position)
                number_position = [378,782]
                screen.blit(number, number_position)
                number_position = [511,784]
                screen.blit(number, number_position)

            if 20 in s.holes:
                number_position = [178,627]
                screen.blit(number, number_position)
                number_position = [377,571]
                screen.blit(number, number_position)
                number_position = [509,627]
                screen.blit(number, number_position)
                number_position = [144,784]
                screen.blit(number, number_position)
                number_position = [277,782]
                screen.blit(number, number_position)
                number_position = [615,786]
                screen.blit(number, number_position)

            if 21 in s.holes:
                number_position = [109,627]
                screen.blit(number, number_position)
                number_position = [378,628]
                screen.blit(number, number_position)
                number_position = [509,570]
                screen.blit(number, number_position)
                number_position = [144,841]
                screen.blit(number, number_position)
                number_position = [346,840]
                screen.blit(number, number_position)
                number_position = [546,784]
                screen.blit(number, number_position)

            if 22 in s.holes:
                number_position = [107,570]
                screen.blit(number, number_position)
                number_position = [310,627]
                screen.blit(number, number_position)
                number_position = [578,571]
                screen.blit(number, number_position)
                number_position = [212,784]
                screen.blit(number, number_position)
                number_position = [344,783]
                screen.blit(number, number_position)
                number_position = [547,842]
                screen.blit(number, number_position)

            if 23 in s.holes:
                number_position = [108,654]
                screen.blit(number, number_position)
                number_position = [378,655]
                screen.blit(number, number_position)
                number_position = [612,626]
                screen.blit(number, number_position)
                number_position = [75,756]
                screen.blit(number, number_position)
                number_position = [310,726]
                screen.blit(number, number_position)
                number_position = [578,728]
                screen.blit(number, number_position)

            if 24 in s.holes:
                number_position = [72,626]
                screen.blit(number, number_position)
                number_position = [308,543]
                screen.blit(number, number_position)
                number_position = [474,571]
                screen.blit(number, number_position)
                number_position = [177,728]
                screen.blit(number, number_position)
                number_position = [411,754]
                screen.blit(number, number_position)
                number_position = [512,841]
                screen.blit(number, number_position)

            if 25 in s.holes:
                number_position = [176,543]
                screen.blit(number, number_position)
                number_position = [411,570]
                screen.blit(number, number_position)
                number_position = [508,655]
                screen.blit(number, number_position)
                number_position = [213,811]
                screen.blit(number, number_position)
                number_position = [277,812]
                screen.blit(number, number_position)
                number_position = [476,756]
                screen.blit(number, number_position)


    if s.game.tilt.status == True:
        tilt_position = [11,378]
        screen.blit(tilt, tilt_position)

    pygame.display.flip()
    pygame.display.update()


