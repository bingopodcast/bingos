
import pygame, random

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

meter = pygame.image.load('graphics/assets/register_cover.png').convert()
card = pygame.image.load('spelling_bee/assets/card.png').convert_alpha()
letter = pygame.image.load('spelling_bee/assets/letter.png').convert_alpha()
average = pygame.image.load('spelling_bee/assets/average.png').convert_alpha()
star_hole = pygame.image.load('spelling_bee/assets/star_hole.png').convert_alpha()
tilt = pygame.image.load('spelling_bee/assets/tilt.png').convert_alpha()

class scorereel():
    """ Score Reels are used to count replays """
    def __init__(self, pos, image):
        self.position = pos
        self.default_y = self.position[1]
        self.image = pygame.image.load(image).convert()

reel1 = scorereel([112,320], "graphics/assets/white_reel.png")
reel10 = scorereel([94,320], "graphics/assets/white_reel.png")
reel100 = scorereel([600,600], "graphics/assets/green_reel.png")

def display(s, replays=0, menu=False):
    
    meter.set_colorkey((255,0,252))
    meter_position = [84,320]

    screen.blit(reel1.image, reel1.position)
    screen.blit(reel10.image, reel10.position)
    screen.blit(meter, meter_position)

    backglass_position = [0, 0]
    backglass = pygame.Surface((0,0), pygame.SRCALPHA)
    backglass.fill((0, 0, 0))
    if menu == True:
        backglass = pygame.image.load('spelling_bee/assets/spelling_bee_menu.png')
    else:
        if (s.game.anti_cheat.status == True):
            backglass = pygame.image.load('spelling_bee/assets/spelling_bee_gi.png')
        else:
            backglass = pygame.image.load('spelling_bee/assets/spelling_bee_off.png')
    screen.blit(backglass, backglass_position)

    if s.game.selector.position >= 1:
        card1_position = [203,647]
        screen.blit(card, card1_position)
    if s.game.selector.position >= 2:
        card2_position = [298,504]
        screen.blit(card, card2_position)
    if s.game.selector.position >= 3:
        card3_position = [337,901]
        screen.blit(card, card3_position)
    if s.game.selector.position >= 4:
        card4_position = [451,750]
        screen.blit(card, card4_position)

    if s.game.tilt.status == False:
        if s.holes:
            if 2 in s.holes:
                p = [65,499]
                screen.blit(letter, p)
                p = [207,528]
                screen.blit(letter, p)
                p = [149,558]
                screen.blit(letter, p)
                p = [121,588]
                screen.blit(letter, p)
                p = [92,617]
                screen.blit(letter, p)
                p = [64,647]
                screen.blit(letter, p)
                #card 2
                p = [325,616]
                screen.blit(letter, p)
                p = [467,614]
                screen.blit(letter, p)
                p = [410,673]
                screen.blit(letter, p)
                #card 3
                p = [237,778]
                screen.blit(letter, p)
                p = [295,808]
                screen.blit(letter, p)
                p = [323,778]
                screen.blit(letter, p)
                p = [266,838]
                screen.blit(letter, p)
                p = [210,897]
                screen.blit(letter, p)
                p = [153,926]
                screen.blit(letter, p)
                #card 4
                p = [580,745]
                screen.blit(letter, p)
                p = [608,774]
                screen.blit(letter, p)
                p = [495,834]
                screen.blit(letter, p)
                p = [524,922]
                screen.blit(letter, p)
            if 3 in s.holes:
                p = [150,528]
                screen.blit(letter, p)
                p = [122,618]
                screen.blit(letter, p)
                #card 2
                p = [410,645]
                screen.blit(letter, p)
                #card 3
                p = [153,897]
                screen.blit(letter, p)
                p = [210,926]
                screen.blit(letter, p)
                #card 4
                p = [467,834]
                screen.blit(letter, p)
            if 4 in s.holes:
                p = [178,498]
                screen.blit(letter, p)
                p = [382,674]
                screen.blit(letter, p)
                p = [210,868]
                screen.blit(letter, p)
                p = [552,745]
                screen.blit(letter, p)
            if 5 in s.holes:
                p = [64,558]
                screen.blit(letter, p)
                p = [410,556]
                screen.blit(letter, p)
                p = [354,616]
                screen.blit(letter, p)
                p = [153,956]
                screen.blit(letter, p)
                p = [296,954]
                screen.blit(letter, p)
                p = [552,804]
                screen.blit(letter, p)
                p = [524,834]
                screen.blit(letter, p)
                p = [578,891]
                screen.blit(letter, p)
            if 7 in s.holes:
                p = [208,558]
                screen.blit(letter, p)
                p = [178,588]
                screen.blit(letter, p)
                p = [150,617]
                screen.blit(letter, p)
                p = [439,496]
                screen.blit(letter, p)
                p = [439,556]
                screen.blit(letter, p)
                p = [410,586]
                screen.blit(letter, p)
                p = [382,616]
                screen.blit(letter, p)
                p = [354,646]
                screen.blit(letter, p)
                p = [180,810]
                screen.blit(letter, p)
                p = [324,837]
                screen.blit(letter, p)
                p = [295,867]
                screen.blit(letter, p)
                p = [635,744]
                screen.blit(letter, p)
                p = [636,802]
                screen.blit(letter, p)
                p = [552,834]
                screen.blit(letter, p)
                p = [524,892]
                screen.blit(letter, p)
            if 8 in s.holes:
                p = [92,588]
                screen.blit(letter, p)
                p = [439,616]
                screen.blit(letter, p)
                p = [324,750]
                screen.blit(letter, p)
                p = [467,951]
                screen.blit(letter, p)
            if 9 in s.holes:
                p = [36,498]
                screen.blit(letter, p)
                p = [410,497]
                screen.blit(letter, p)
                p = [180,779]
                screen.blit(letter, p)
                p = [238,838]
                screen.blit(letter, p)
                p = [238,954]
                screen.blit(letter, p)
                p = [606,919]
                screen.blit(letter, p)
            if 10 in s.holes: #i
                p = [64,528]
                screen.blit(letter, p)
                p = [410,527]
                screen.blit(letter, p)
                p = [354,586]
                screen.blit(letter, p)
                p = [439,644]
                screen.blit(letter, p)
                p = [267,954]
                screen.blit(letter, p)
                p = [467,864]
                screen.blit(letter, p)
                p = [634,918]
                screen.blit(letter, p)
                p = [606,948]
                screen.blit(letter, p)
            if 11 in s.holes: #m
                p = [93,677]
                screen.blit(letter, p)
                p = [296,616]
                screen.blit(letter, p)
                p = [295,778]
                screen.blit(letter, p)
                p = [181,838]
                screen.blit(letter, p)
                p = [606,978]
                screen.blit(letter, p)
            if 12 in s.holes: #n
                p = [36,678]
                screen.blit(letter, p)
                p = [467,497]
                screen.blit(letter, p)
                p = [468,644]
                screen.blit(letter, p)
                p = [266,748]
                screen.blit(letter, p)
                p = [267,867]
                screen.blit(letter, p)
                p = [608,804]
                screen.blit(letter, p)
                p = [551,892]
                screen.blit(letter, p)
                p = [635,948]
                screen.blit(letter, p)
            if 13 in s.holes: #o
                p = [178,528]
                screen.blit(letter, p)
                p = [36,618]
                screen.blit(letter, p)
                p = [382,556]
                screen.blit(letter, p)
                p = [210,750]
                screen.blit(letter, p)
                p = [182,897]
                screen.blit(letter, p)
                p = [552,775]
                screen.blit(letter, p)
                p = [580,804]
                screen.blit(letter, p)
                p = [495,951]
                screen.blit(letter, p)
            if 14 in s.holes: #p
                p = [122,499]
                screen.blit(letter, p)
                p = [178,558]
                screen.blit(letter, p)
                p = [468,586]
                screen.blit(letter, p)
                p = [267,809]
                screen.blit(letter, p)
                p = [496,805]
                screen.blit(letter, p)
            if 15 in s.holes: #r
                p = [236,528]
                screen.blit(letter, p)
                p = [93,648]
                screen.blit(letter, p)
                p = [354,557]
                screen.blit(letter, p)
                p = [382,586]
                screen.blit(letter, p)
                p = [440,674]
                screen.blit(letter, p)
                p = [324,808]
                screen.blit(letter, p)
                p = [608,746]
                screen.blit(letter, p)
                p = [496,864]
                screen.blit(letter, p)
                p = [523,950]
                screen.blit(letter, p)
            if 16 in s.holes: #s
                p = [93,498]
                screen.blit(letter, p)
                p = [36,588]
                screen.blit(letter, p)
                p = [325,586]
                screen.blit(letter, p)
                p = [238,808]
                screen.blit(letter, p)
                p = [438,864]
                screen.blit(letter, p)
            if 17 in s.holes: #t
                p = [121,558]
                screen.blit(letter, p)
                p = [150,588]
                screen.blit(letter, p)
                p = [382,498]
                screen.blit(letter, p)
                p = [468,674]
                screen.blit(letter, p)
                p = [180,750]
                screen.blit(letter, p)
                p = [296,838]
                screen.blit(letter, p)
                p = [239,897]
                screen.blit(letter, p)
                p = [608,832]
                screen.blit(letter, p)
                p = [634,860]
                screen.blit(letter, p)
                p = [496,893]
                screen.blit(letter, p)
            if 18 in s.holes: #w
                p = [36,648]
                screen.blit(letter, p)
                p = [325,646]
                screen.blit(letter, p)
                p = [238,750]
                screen.blit(letter, p)
                p = [634,890]
                screen.blit(letter, p)

    if s.game.average.status == True:
        p = [33,952]
        screen.blit(average, p)
    if s.game.good.status == True:
        p = [34,868]
        screen.blit(star_hole, p)
    if s.game.expert.status == True:
        p = [34,782]
        screen.blit(star_hole, p)


    if s.game.tilt.status == True:
        tilt_position = [55,400]
        screen.blit(tilt, tilt_position)

    pygame.display.flip()
    pygame.display.update()


