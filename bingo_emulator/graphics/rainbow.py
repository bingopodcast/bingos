
import pygame, random

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

meter = pygame.image.load('graphics/assets/white_register_cover.png').convert()
card = pygame.image.load('rainbow/assets/card.png').convert_alpha()
number = pygame.image.load('rainbow/assets/number.png').convert_alpha()
tilt = pygame.image.load('rainbow/assets/tilt.png').convert_alpha()

class scorereel():
    """ Score Reels are used to count replays """
    def __init__(self, pos, image):
        self.position = pos
        self.default_y = self.position[1]
        self.image = pygame.image.load(image).convert()

reel1 = scorereel([592,320], "graphics/assets/white_reel.png")
reel10 = scorereel([572,320], "graphics/assets/white_reel.png")
reel100 = scorereel([554,320], "graphics/assets/white_reel.png")
reel1000 = scorereel([535,320], "graphics/assets/white_reel.png")

def display(s, replays=0, menu=False):
    
    meter.set_colorkey((255,0,252))
    meter_position = [512,320]

    screen.blit(reel1.image, reel1.position)
    screen.blit(reel10.image, reel10.position)
    screen.blit(reel100.image, reel100.position)
    screen.blit(reel1000.image, reel1000.position)
    screen.blit(meter, meter_position)

    backglass_position = [0, 0]
    backglass = pygame.Surface((0,0), pygame.SRCALPHA)
    backglass.fill((0, 0, 0))
    if menu == True:
        backglass = pygame.image.load('rainbow/assets/rainbow_menu.png')
    else:
        if (s.game.anti_cheat.status == True):
            backglass = pygame.image.load('rainbow/assets/rainbow_gi.png')
        else:
            backglass = pygame.image.load('rainbow/assets/rainbow_off.png')
    screen.blit(backglass, backglass_position)

    if s.game.selector.position >= 1:
        card1_position = [12,664]
        screen.blit(card, card1_position)
    if s.game.selector.position >= 2:
        card2_position = [290,663]
        screen.blit(card, card2_position)
    if s.game.selector.position >= 3:
        card3_position = [566,662]
        screen.blit(card, card3_position)
    if s.game.selector.position >= 4:
        card4_position = [15,938]
        screen.blit(card, card4_position)
    if s.game.selector.position >= 5:
        card5_position = [290,937]
        screen.blit(card, card5_position)
    if s.game.selector.position >= 6:
        card6_position = [569,937]
        screen.blit(card, card6_position)

    if s.game.tilt.status == False:
        if s.holes:
            if 1 in s.holes:
                number_position = [62,469]
                screen.blit(number, number_position)
                number_position = [255,589]
                screen.blit(number, number_position)
                number_position = [615,629]
                screen.blit(number, number_position)
                number_position = [187,742]
                screen.blit(number, number_position)
                number_position = [255,907]
                screen.blit(number, number_position)
                number_position = [574,742]
                screen.blit(number, number_position)
            if 2 in s.holes:
                number_position = [103,632]
                screen.blit(number, number_position)
                number_position = [257,550]
                screen.blit(number, number_position)
                number_position = [655,549]
                screen.blit(number, number_position)
                number_position = [186,783]
                screen.blit(number, number_position)
                number_position = [256,783]
                screen.blit(number, number_position)
                number_position = [613,908]
                screen.blit(number, number_position)

            if 3 in s.holes:
                number_position = [187,471]
                screen.blit(number, number_position)
                number_position = [425,630]
                screen.blit(number, number_position)
                number_position = [492,467]
                screen.blit(number, number_position)
                number_position = [104,742]
                screen.blit(number, number_position)
                number_position = [380,908]
                screen.blit(number, number_position)
                number_position = [573,783]
                screen.blit(number, number_position)

            if 4 in s.holes:
                number_position = [147,632]
                screen.blit(number, number_position)
                number_position = [382,468]
                screen.blit(number, number_position)
                number_position = [616,468]
                screen.blit(number, number_position)
                number_position = [145,906]
                screen.blit(number, number_position)
                number_position = [422,741]
                screen.blit(number, number_position)
                number_position = [491,740]
                screen.blit(number, number_position)
            if 5 in s.holes:
                number_position = [22,468]
                screen.blit(number, number_position)
                number_position = [341,630]
                screen.blit(number, number_position)
                number_position = [657,630]
                screen.blit(number, number_position)
                number_position = [20,823]
                screen.blit(number, number_position)
                number_position = [422,823]
                screen.blit(number, number_position)
                number_position = [656,741]
                screen.blit(number, number_position)
            if 6 in s.holes:
                number_position = [23,550]
                screen.blit(number, number_position)
                number_position = [423,466]
                screen.blit(number, number_position)
                number_position = [493,630]
                screen.blit(number, number_position)
                number_position = [21,741]
                screen.blit(number, number_position)
                number_position = [422,907]
                screen.blit(number, number_position)
                number_position = [533,741]
                screen.blit(number, number_position)

            if 7 in s.holes:
                number_position = [189,506]
                screen.blit(number, number_position)
                number_position = [299,630]
                screen.blit(number, number_position)
                number_position = [533,466]
                screen.blit(number, number_position)
                number_position = [62,740]
                screen.blit(number, number_position)
                number_position = [299,906]
                screen.blit(number, number_position)
                number_position = [491,906]
                screen.blit(number, number_position)

            if 8 in s.holes:
                number_position = [23,507]
                screen.blit(number, number_position)
                number_position = [424,590]
                screen.blit(number, number_position)
                number_position = [658,507]
                screen.blit(number, number_position)
                number_position = [189,907]
                screen.blit(number, number_position)
                number_position = [258,740]
                screen.blit(number, number_position)
                number_position = [658,866]
                screen.blit(number, number_position)

            if 9 in s.holes:
                number_position = [105,467]
                screen.blit(number, number_position)
                number_position = [258,465]
                screen.blit(number, number_position)
                number_position = [657,467]
                screen.blit(number, number_position)
                number_position = [104,865]
                screen.blit(number, number_position)
                number_position = [340,865]
                screen.blit(number, number_position)
                number_position = [491,824]
                screen.blit(number, number_position)

            if 10 in s.holes:
                number_position = [105,507]
                screen.blit(number, number_position)
                number_position = [256,630]
                screen.blit(number, number_position)
                number_position = [574,466]
                screen.blit(number, number_position)
                number_position = [20,905]
                screen.blit(number, number_position)
                number_position = [340,740]
                screen.blit(number, number_position)
                number_position = [491,864]
                screen.blit(number, number_position)

            if 11 in s.holes:
                number_position = [146,549]
                screen.blit(number, number_position)
                number_position = [340,590]
                screen.blit(number, number_position)
                number_position = [616,548]
                screen.blit(number, number_position)
                number_position = [20,864]
                screen.blit(number, number_position)
                number_position = [422,865]
                screen.blit(number, number_position)
                number_position = [657,907]
                screen.blit(number, number_position)

            if 12 in s.holes:
                number_position = [22,631]
                screen.blit(number, number_position)
                number_position = [383,549]
                screen.blit(number, number_position)
                number_position = [575,589]
                screen.blit(number, number_position)
                number_position = [105,781]
                screen.blit(number, number_position)
                number_position = [299,823]
                screen.blit(number, number_position)
                number_position = [613,822]
                screen.blit(number, number_position)

            if 13 in s.holes:
                number_position = [189,591]
                screen.blit(number, number_position)
                number_position = [259,508]
                screen.blit(number, number_position)
                number_position = [490,589]
                screen.blit(number, number_position)
                number_position = [62,907]
                screen.blit(number, number_position)
                number_position = [382,740]
                screen.blit(number, number_position)
                number_position = [657,781]
                screen.blit(number, number_position)

            if 14 in s.holes:
                number_position = [105,590]
                screen.blit(number, number_position)
                number_position = [341,507]
                screen.blit(number, number_position)
                number_position = [533,549]
                screen.blit(number, number_position)
                number_position = [61,781]
                screen.blit(number, number_position)
                number_position = [382,782]
                screen.blit(number, number_position)
                number_position = [615,864]
                screen.blit(number, number_position)

            if 15 in s.holes:
                number_position = [190,632]
                screen.blit(number, number_position)
                number_position = [340,548]
                screen.blit(number, number_position)
                number_position = [494,548]
                screen.blit(number, number_position)
                number_position = [146,864]
                screen.blit(number, number_position)
                number_position = [298,865]
                screen.blit(number, number_position)
                number_position = [533,781]
                screen.blit(number, number_position)

            if 16 in s.holes:
                number_position = [105,549]
                screen.blit(number, number_position)
                number_position = [341,466]
                screen.blit(number, number_position)
                number_position = [576,631]
                screen.blit(number, number_position)
                number_position = [147,822]
                screen.blit(number, number_position)
                number_position = [341,783]
                screen.blit(number, number_position)
                number_position = [574,866]
                screen.blit(number, number_position)

            if 17 in s.holes:
                number_position = [189,549]
                screen.blit(number, number_position)
                number_position = [423,549]
                screen.blit(number, number_position)
                number_position = [575,548]
                screen.blit(number, number_position)
                number_position = [62,864]
                screen.blit(number, number_position)
                number_position = [299,782]
                screen.blit(number, number_position)
                number_position = [616,782]
                screen.blit(number, number_position)

            if 18 in s.holes:
                number_position = [64,549]
                screen.blit(number, number_position)
                number_position = [298,549]
                screen.blit(number, number_position)
                number_position = [575,508]
                screen.blit(number, number_position)
                number_position = [146,781]
                screen.blit(number, number_position)
                number_position = [382,865]
                screen.blit(number, number_position)
                number_position = [533,865]
                screen.blit(number, number_position)

            if 19 in s.holes:
                number_position = [147,508]
                screen.blit(number, number_position)
                number_position = [299,507]
                screen.blit(number, number_position)
                number_position = [617,588]
                screen.blit(number, number_position)
                number_position = [63,822]
                screen.blit(number, number_position)
                number_position = [382,823]
                screen.blit(number, number_position)
                number_position = [533,823]
                screen.blit(number, number_position)

            if 20 in s.holes:
                number_position = [147,589]
                screen.blit(number, number_position)
                number_position = [383,507]
                screen.blit(number, number_position)
                number_position = [534,588]
                screen.blit(number, number_position)
                number_position = [157,822]
                screen.blit(number, number_position)
                number_position = [256,823]
                screen.blit(number, number_position)
                number_position = [657,823]
                screen.blit(number, number_position)

            if 21 in s.holes:
                number_position = [64,591]
                screen.blit(number, number_position)
                number_position = [383,589]
                screen.blit(number, number_position)
                number_position = [534,507]
                screen.blit(number, number_position)
                number_position = [105,907]
                screen.blit(number, number_position)
                number_position = [339,907]
                screen.blit(number, number_position)
                number_position = [574,822]
                screen.blit(number, number_position)

            if 22 in s.holes:
                number_position = [63,507]
                screen.blit(number, number_position)
                number_position = [298,589]
                screen.blit(number, number_position)
                number_position = [615,507]
                screen.blit(number, number_position)
                number_position = [187,823]
                screen.blit(number, number_position)
                number_position = [340,823]
                screen.blit(number, number_position)
                number_position = [574,906]
                screen.blit(number, number_position)

            if 23 in s.holes:
                number_position = [63,630]
                screen.blit(number, number_position)
                number_position = [383,630]
                screen.blit(number, number_position)
                number_position = [657,590]
                screen.blit(number, number_position)
                number_position = [21,782]
                screen.blit(number, number_position)
                number_position = [298,738]
                screen.blit(number, number_position)
                number_position = [615,739]
                screen.blit(number, number_position)

            if 24 in s.holes:
                number_position = [20,590]
                screen.blit(number, number_position)
                number_position = [298,463]
                screen.blit(number, number_position)
                number_position = [492,506]
                screen.blit(number, number_position)
                number_position = [145,739]
                screen.blit(number, number_position)
                number_position = [423,782]
                screen.blit(number, number_position)
                number_position = [532,905]
                screen.blit(number, number_position)

            if 25 in s.holes:
                number_position = [147,467]
                screen.blit(number, number_position)
                number_position = [423,509]
                screen.blit(number, number_position)
                number_position = [533,631]
                screen.blit(number, number_position)
                number_position = [187,864]
                screen.blit(number, number_position)
                number_position = [255,865]
                screen.blit(number, number_position)
                number_position = [490,781]
                screen.blit(number, number_position)


    if s.game.tilt.status == True:
        tilt_position = [360,398]
        screen.blit(tilt, tilt_position)

    pygame.display.flip()
    pygame.display.update()


