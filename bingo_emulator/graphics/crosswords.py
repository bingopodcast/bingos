
import pygame, random

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

meter = pygame.image.load('graphics/assets/register_cover.png').convert()
card = pygame.image.load('crosswords/assets/card.png').convert_alpha()
letter = pygame.image.load('crosswords/assets/letter.png').convert_alpha()
average = pygame.image.load('crosswords/assets/average.png').convert_alpha()
star_hole = pygame.image.load('crosswords/assets/star_hole.png').convert_alpha()
tilt = pygame.image.load('crosswords/assets/tilt.png').convert_alpha()

class scorereel():
    """ Score Reels are used to count replays """
    def __init__(self, pos, image):
        self.position = pos
        self.default_y = self.position[1]
        self.image = pygame.image.load(image).convert()

reel1 = scorereel([109,338], "graphics/assets/white_reel.png")
reel10 = scorereel([91,338], "graphics/assets/white_reel.png")
reel100 = scorereel([600,600], "graphics/assets/green_reel.png")

def display(s, replays=0, menu=False):
    
    meter.set_colorkey((255,0,252))
    meter_position = [81,338]

    screen.blit(reel1.image, reel1.position)
    screen.blit(reel10.image, reel10.position)
    screen.blit(meter, meter_position)

    backglass_position = [0, 0]
    backglass = pygame.Surface((0,0), pygame.SRCALPHA)
    backglass.fill((0, 0, 0))
    if menu == True:
        backglass = pygame.image.load('crosswords/assets/crosswords_menu.png')
    else:
        if (s.game.anti_cheat.status == True):
            backglass = pygame.image.load('crosswords/assets/crosswords_gi.png')
        else:
            backglass = pygame.image.load('crosswords/assets/crosswords_off.png')
    screen.blit(backglass, backglass_position)

    if s.game.selector.position >= 1:
        card1_position = [203,645]
        screen.blit(card, card1_position)
    if s.game.selector.position >= 2:
        card2_position = [297,510]
        screen.blit(card, card2_position)
    if s.game.selector.position >= 3:
        card3_position = [338,891]
        screen.blit(card, card3_position)
    if s.game.selector.position >= 4:
        card4_position = [452,747]
        screen.blit(card, card4_position)

    if s.game.tilt.status == False:
        if s.holes:
            if 2 in s.holes:
                p = [62,505]
                screen.blit(letter, p)
                p = [206,532]
                screen.blit(letter, p)
                p = [149,561]
                screen.blit(letter, p)
                p = [120,590]
                screen.blit(letter, p)
                p = [92,618]
                screen.blit(letter, p)
                p = [64,647]
                screen.blit(letter, p)
                #card 2
                p = [324,616]
                screen.blit(letter, p)
                p = [465,616]
                screen.blit(letter, p)
                p = [409,672]
                screen.blit(letter, p)
                #card 3
                p = [237,772]
                screen.blit(letter, p)
                p = [323,772]
                screen.blit(letter, p)
                p = [295,800]
                screen.blit(letter, p)
                p = [266,828]
                screen.blit(letter, p)
                p = [210,886]
                screen.blit(letter, p)
                p = [152,914]
                screen.blit(letter, p)
                #card 4
                p = [580,741]
                screen.blit(letter, p)
                p = [606,770]
                screen.blit(letter, p)
                p = [495,827]
                screen.blit(letter, p)
                p = [523,912]
                screen.blit(letter, p)
            if 3 in s.holes:
                p = [148,533]
                screen.blit(letter, p)
                p = [121,618]
                screen.blit(letter, p)
                #card 2
                p = [409,643]
                screen.blit(letter, p)
                #card 3
                p = [152,885]
                screen.blit(letter, p)
                p = [210,914]
                screen.blit(letter, p)
                #card 4
                p = [467,826]
                screen.blit(letter, p)
            if 4 in s.holes:
                p = [176,503]
                screen.blit(letter, p)
                p = [380,672]
                screen.blit(letter, p)
                p = [209,857]
                screen.blit(letter, p)
                p = [551,742]
                screen.blit(letter, p)
            if 5 in s.holes:
                p = [63,562]
                screen.blit(letter, p)
                p = [408,559]
                screen.blit(letter, p)
                p = [352,615]
                screen.blit(letter, p)
                p = [153,943]
                screen.blit(letter, p)
                p = [296,940]
                screen.blit(letter, p)
                p = [551,798]
                screen.blit(letter, p)
                p = [523,826]
                screen.blit(letter, p)
                p = [580,883]
                screen.blit(letter, p)
            if 7 in s.holes:
                p = [206,561]
                screen.blit(letter, p)
                p = [177,589]
                screen.blit(letter, p)
                p = [149,618]
                screen.blit(letter, p)
                p = [437,502]
                screen.blit(letter, p)
                p = [436,559]
                screen.blit(letter, p)
                p = [409,588]
                screen.blit(letter, p)
                p = [380,616]
                screen.blit(letter, p)
                p = [355,644]
                screen.blit(letter, p)
                p = [181,801]
                screen.blit(letter, p)
                p = [324,828]
                screen.blit(letter, p)
                p = [296,857]
                screen.blit(letter, p)
                p = [635,740]
                screen.blit(letter, p)
                p = [636,798]
                screen.blit(letter, p)
                p = [551,826]
                screen.blit(letter, p)
                p = [523,882]
                screen.blit(letter, p)
            if 8 in s.holes:
                p = [92,589]
                screen.blit(letter, p)
                p = [437,616]
                screen.blit(letter, p)
                p = [322,742]
                screen.blit(letter, p)
                p = [467,940]
                screen.blit(letter, p)
            if 9 in s.holes:
                p = [34,505]
                screen.blit(letter, p)
                p = [408,503]
                screen.blit(letter, p)
                p = [238,829]
                screen.blit(letter, p)
                p = [179,772]
                screen.blit(letter, p)
                p = [238,942]
                screen.blit(letter, p)
                p = [607,910]
                screen.blit(letter, p)
            if 10 in s.holes:
                p = [62,533]
                screen.blit(letter, p)
                p = [408,531]
                screen.blit(letter, p)
                p = [352,587]
                screen.blit(letter, p)
                p = [437,644]
                screen.blit(letter, p)
                p = [267,941]
                screen.blit(letter, p)
                p = [468,855]
                screen.blit(letter, p)
                p = [635,910]
                screen.blit(letter, p)
                p = [607,938]
                screen.blit(letter, p)
            if 11 in s.holes:
                p = [91,675]
                screen.blit(letter, p)
                p = [295,616]
                screen.blit(letter, p)
                p = [295,772]
                screen.blit(letter, p)
                p = [180,830]
                screen.blit(letter, p)
                p = [607,967]
                screen.blit(letter, p)
            if 12 in s.holes:
                p = [35,676]
                screen.blit(letter, p)
                p = [464,502]
                screen.blit(letter, p)
                p = [465,644]
                screen.blit(letter, p)
                p = [266,742]
                screen.blit(letter, p)
                p = [266,857]
                screen.blit(letter, p)
                p = [606,798]
                screen.blit(letter, p)
                p = [551,882]
                screen.blit(letter, p)
                p = [634,938]
                screen.blit(letter, p)
            if 13 in s.holes:
                p = [177,532]
                screen.blit(letter, p)
                p = [34,619]
                screen.blit(letter, p)
                p = [381,558]
                screen.blit(letter, p)
                p = [208,744]
                screen.blit(letter, p)
                p = [181,885]
                screen.blit(letter, p)
                p = [551,770]
                screen.blit(letter, p)
                p = [495,939]
                screen.blit(letter, p)
                p = [580,798]
                screen.blit(letter, p)
            if 14 in s.holes:
                p = [119,504]
                screen.blit(letter, p)
                p = [177,561]
                screen.blit(letter, p)
                p = [464,586]
                screen.blit(letter, p)
                p = [266,800]
                screen.blit(letter, p)
                p = [494,798]
                screen.blit(letter, p)
            if 15 in s.holes:
                p = [234,531]
                screen.blit(letter, p)
                p = [92,646]
                screen.blit(letter, p)
                p = [352,559]
                screen.blit(letter, p)
                p = [380,587]
                screen.blit(letter, p)
                p = [437,672]
                screen.blit(letter, p)
                p = [323,801]
                screen.blit(letter, p)
                p = [607,741]
                screen.blit(letter, p)
                p = [495,855]
                screen.blit(letter, p)
                p = [523,939]
                screen.blit(letter, p)
            if 16 in s.holes:
                p = [90,504]
                screen.blit(letter, p)
                p = [34,590]
                screen.blit(letter, p)
                p = [323,587]
                screen.blit(letter, p)
                p = [238,801]
                screen.blit(letter, p)
                p = [439,855]
                screen.blit(letter, p)
            if 17 in s.holes:
                p = [120,560]
                screen.blit(letter, p)
                p = [149,589]
                screen.blit(letter, p)
                p = [380,503]
                screen.blit(letter, p)
                p = [466,672]
                screen.blit(letter, p)
                p = [180,744]
                screen.blit(letter, p)
                p = [295,828]
                screen.blit(letter, p)
                p = [238,885]
                screen.blit(letter, p)
                p = [606,827]
                screen.blit(letter, p)
                p = [634,853]
                screen.blit(letter, p)
                p = [494,883]
                screen.blit(letter, p)
            if 18 in s.holes:
                p = [34,647]
                screen.blit(letter, p)
                p = [323,645]
                screen.blit(letter, p)
                p = [237,744]
                screen.blit(letter, p)
                p = [635,882]
                screen.blit(letter, p)

    if s.game.average.status == True:
        p = [34,940]
        screen.blit(average, p)
    if s.game.good.status == True:
        p = [33,857]
        screen.blit(star_hole, p)
    if s.game.expert.status == True:
        p = [33,775]
        screen.blit(star_hole, p)


    if s.game.tilt.status == True:
        tilt_position = [55,400]
        screen.blit(tilt, tilt_position)

    pygame.display.flip()
    pygame.display.update()


