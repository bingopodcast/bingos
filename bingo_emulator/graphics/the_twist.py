
import pygame
import random

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

meter = pygame.image.load('graphics/assets/register_cover.png').convert()
magic_screen = pygame.image.load('the_twist/assets/magic_screen.png').convert()
odds = pygame.image.load('the_twist/assets/odds.png').convert_alpha()
eb = pygame.image.load('the_twist/assets/eb.png').convert_alpha()
eb_number = pygame.image.load('the_twist/assets/eb_number.png').convert_alpha()
extra_balls = pygame.image.load('the_twist/assets/extra_balls.png').convert_alpha()
feature = pygame.image.load('the_twist/assets/feature.png').convert_alpha()
magic_card = pygame.image.load('the_twist/assets/magic_card.png').convert_alpha()
before_fifth = pygame.image.load('the_twist/assets/before_fifth.png').convert_alpha()
before_fourth = pygame.image.load('the_twist/assets/before_fourth.png').convert_alpha()
number = pygame.image.load('the_twist/assets/number.png').convert_alpha()
tilt = pygame.image.load('the_twist/assets/tilt.png').convert_alpha()

class scorereel():
    """ Score Reels are used to count replays """
    def __init__(self, pos, image):
        self.position = pos
        self.default_y = self.position[1]
        self.image = pygame.image.load(image).convert()

reel1 = scorereel([93,813], "graphics/assets/white_reel.png")
reel10 = scorereel([74,813], "graphics/assets/white_reel.png")
reel100 = scorereel([54,813], "graphics/assets/white_reel.png")

def display(s, replays=0, menu=False):
    
    meter.set_colorkey((255,0,252))
    meter_position = [45,813]

    screen.blit(reel1.image, reel1.position)
    screen.blit(reel10.image, reel10.position)
    screen.blit(reel100.image, reel100.position)
    screen.blit(meter, meter_position)

    #default position 230x 359y
    #subtract 47 per position
    if s.game.magic_screen.position == 0:
        magic_screen_position = [225,325]
    elif s.game.magic_screen.position == 1:
        magic_screen_position = [176,327]
    elif s.game.magic_screen.position == 2:
        magic_screen_position = [125,327]
    elif s.game.magic_screen.position == 3:
        magic_screen_position = [74,327]
    elif s.game.magic_screen.position == 4:
        magic_screen_position = [23,327]
    elif s.game.magic_screen.position == 5:
        magic_screen_position = [-25,327]
    elif s.game.magic_screen.position == 6:
        magic_screen_position = [-75,327]
    elif s.game.magic_screen.position == 7:
        magic_screen_position = [-127,327]
    elif s.game.magic_screen.position == 8:
        magic_screen_position = [-178,327]
    elif s.game.magic_screen.position == 9:
        magic_screen_position = [-229,327]
    elif s.game.magic_screen.position == 10:
        magic_screen_position = [-281,327]


    screen.blit(magic_screen, magic_screen_position)

    backglass_position = [0, 0]
    backglass = pygame.Surface(screen.get_size(), flags=pygame.SRCALPHA)
    backglass.fill((0, 0, 0))
    if menu == True:
        backglass = pygame.image.load('the_twist/assets/the_twist_menu.png').convert()
        backglass.set_colorkey((255,0,252))
    else:
        if (s.game.anti_cheat.status == True):
            backglass = pygame.image.load('the_twist/assets/the_twist_gi.png').convert()
            backglass.set_colorkey((255,0,252))
        else:
            backglass = pygame.image.load('the_twist/assets/the_twist_off.png').convert()
            backglass.set_colorkey((255,0,252))
    backglass = pygame.transform.scale(backglass, (720, 1280))
    
    screen.blit(backglass, backglass_position)


    if s.game.eb_play.status == True:
        eb_position = [27,1056]
        screen.blit(extra_balls, eb_position)

    if s.game.extra_ball.position >= 1:
        eb_position = [143,1056]
        screen.blit(eb_number, eb_position)
    if s.game.extra_ball.position >= 2:
        eb_position = [194,1056]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 3:
        eb_position = [259,1056]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 4:
        eb_position = [326,1056]
        screen.blit(eb_number, eb_position)
    if s.game.extra_ball.position >= 5:
        eb_position = [375,1056]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 6:
        eb_position = [438,1056]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 7:
        eb_position = [505,1056]
        screen.blit(eb_number, eb_position)
    if s.game.extra_ball.position >= 8:
        eb_position = [555,1056]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 9:
        eb_position = [618,1056]
        screen.blit(eb, eb_position)
    
    if s.game.ball_count.position >= 1:
        if s.game.before_fifth.status == True:
            bf = [600,550]
            screen.blit(before_fifth, bf)
        elif s.game.before_fourth.status == True:
            bf = [598,623]
            screen.blit(before_fourth, bf)

    if s.game.tilt.status == False:
        if s.game.magic_card.position >= 0:
            mc = [123,691]
            screen.blit(magic_card, mc)
        if s.game.magic_card.position >= 1:
            mc = [165,691]
            screen.blit(magic_card, mc)
        if s.game.magic_card.position >= 2:
            mc = [210,691]
            screen.blit(magic_card, mc)
        if s.game.magic_card.position >= 3:
            mc = [257,691]
            screen.blit(magic_card, mc)
        if s.game.magic_card.position >= 4:
            mc = [301,691]
            screen.blit(magic_card, mc)
        if s.game.magic_card.position >= 5:
            mc = [347,691]
            screen.blit(magic_card, mc)
        if s.game.magic_card.position >= 6:
            mc = [391,691]
            screen.blit(magic_card, mc)
        if s.game.magic_card.position >= 7:
            mc = [435,691]
            screen.blit(magic_card, mc)
        if s.game.magic_card.position >= 8:
            mc = [480,691]
            screen.blit(magic_card, mc)
        if s.game.magic_card.position >= 9:
            mc = [526,691]
            screen.blit(magic_card, mc)
        if s.game.magic_card.position >= 10:
            mc = [570,691]
            screen.blit(magic_card, mc)
        if s.game.magic_screen.position == 0:
            mc = [123,691]
            screen.blit(magic_card, mc)
        elif s.game.magic_screen.position == 1:
            mc = [165,691]
            screen.blit(magic_card, mc)
        elif s.game.magic_screen.position == 2:
            mc = [210,691]
            screen.blit(magic_card, mc)
        elif s.game.magic_screen.position == 3:
            mc = [257,691]
            screen.blit(magic_card, mc)
        elif s.game.magic_screen.position == 4:
            mc = [301,691]
            screen.blit(magic_card, mc)
        elif s.game.magic_screen.position == 5:
            mc = [347,691]
            screen.blit(magic_card, mc)
        elif s.game.magic_screen.position == 6:
            mc = [391,691]
            screen.blit(magic_card, mc)
        elif s.game.magic_screen.position == 7:
            mc = [435,691]
            screen.blit(magic_card, mc)
        elif s.game.magic_screen.position == 8:
            mc = [480,691]
            screen.blit(magic_card, mc)
        elif s.game.magic_screen.position == 9:
            mc = [526,691]
            screen.blit(magic_card, mc)
        elif s.game.magic_screen.position == 10:
            mc = [570,691]
            screen.blit(magic_card, mc)

    if s.game.start.status == True:
        if s.game.advance_green.status == True:
            f = [34,563]
            screen.blit(feature, f)
        if s.game.advance_yellow.status == True:
            f = [34,481]
            screen.blit(feature, f)
        if s.game.advance_red.status == True:
            f = [34,398]
            screen.blit(feature, f)
        if s.game.advance_card.status == True:
            f = [34,313]
            screen.blit(feature, f)

    if s.game.tilt.status == False:
        if s.holes:
            if s.game.magic_screen.position == 0:
                if 1 in s.holes:
                    number_position = [377,560]
                    screen.blit(number, number_position)
                if 2 in s.holes:
                    number_position = [326,560]
                    screen.blit(number, number_position)
                if 3 in s.holes:
                    number_position = [278,346]
                    screen.blit(number, number_position)
                if 4 in s.holes:
                    number_position = [429,508]
                    screen.blit(number, number_position)
                if 5 in s.holes:
                    number_position = [329,400]
                    screen.blit(number, number_position)
                if 6 in s.holes:
                    number_position = [430,400]
                    screen.blit(number, number_position)
                if 7 in s.holes:
                    number_position = [327,507]
                    screen.blit(number, number_position)
                if 8 in s.holes:
                    number_position = [380,346]
                    screen.blit(number, number_position)
                if 9 in s.holes:
                    number_position = [430,560]
                    screen.blit(number, number_position)
                if 10 in s.holes:
                    number_position = [227,346]
                    screen.blit(number, number_position)
                if 11 in s.holes:
                    number_position = [278,560]
                    screen.blit(number, number_position)
                if 12 in s.holes:
                    number_position = [430,346]
                    screen.blit(number, number_position)
                if 13 in s.holes:
                    number_position = [277,453]
                    screen.blit(number, number_position)
                if 14 in s.holes:
                    number_position = [328,346]
                    screen.blit(number, number_position)
                if 15 in s.holes:
                    number_position = [226,560]
                    screen.blit(number, number_position)
                if 16 in s.holes:
                    number_position = [328,453]
                    screen.blit(number, number_position)
                if 17 in s.holes:
                    number_position = [226,453]
                    screen.blit(number, number_position)
                if 18 in s.holes:
                    number_position = [379,507]
                    screen.blit(number, number_position)
                if 19 in s.holes:
                    number_position = [226,507]
                    screen.blit(number, number_position)
                if 20 in s.holes:
                    number_position = [226,399]
                    screen.blit(number, number_position)
                if 21 in s.holes:
                    number_position = [277,399]
                    screen.blit(number, number_position)
                if 22 in s.holes:
                    number_position = [277,507]
                    screen.blit(number, number_position)
                if 23 in s.holes:
                    number_position = [380,400]
                    screen.blit(number, number_position)
                if 24 in s.holes:
                    number_position = [380,453]
                    screen.blit(number, number_position)
                if 25 in s.holes:
                    number_position = [430,453]
                    screen.blit(number, number_position)
            if s.game.magic_screen.position == 1:
                if 1 in s.holes:
                    number_position = [326,560]
                    screen.blit(number, number_position)
                if 2 in s.holes:
                    number_position = [278,560]
                    screen.blit(number, number_position)
                if 3 in s.holes:
                    number_position = [227,346]
                    screen.blit(number, number_position)
                    number_position = [430,346]
                    screen.blit(number, number_position)
                if 4 in s.holes:
                    number_position = [379,507]
                    screen.blit(number, number_position)
                if 5 in s.holes:
                    number_position = [277,399]
                    screen.blit(number, number_position)
                if 6 in s.holes:
                    number_position = [380,400]
                    screen.blit(number, number_position)
                if 7 in s.holes:
                    number_position = [277,507]
                    screen.blit(number, number_position)
                if 8 in s.holes:
                    number_position = [328,346]
                    screen.blit(number, number_position)
                    number_position = [430,560]
                    screen.blit(number, number_position)
                if 9 in s.holes:
                    number_position = [377,560]
                    screen.blit(number, number_position)
                if 11 in s.holes:
                    number_position = [226,560]
                    screen.blit(number, number_position)
                if 12 in s.holes:
                    number_position = [380,346]
                    screen.blit(number, number_position)
                if 13 in s.holes:
                    number_position = [226,453]
                    screen.blit(number, number_position)
                if 14 in s.holes:
                    number_position = [278,346]
                    screen.blit(number, number_position)
                    number_position = [430,400]
                    screen.blit(number, number_position)
                if 16 in s.holes:
                    number_position = [277,453]
                    screen.blit(number, number_position)
                    number_position = [429,508]
                    screen.blit(number, number_position)
                if 18 in s.holes:
                    number_position = [327,507]
                    screen.blit(number, number_position)
                if 21 in s.holes:
                    number_position = [226,399]
                    screen.blit(number, number_position)
                if 22 in s.holes:
                    number_position = [226,507]
                    screen.blit(number, number_position)
                    number_position = [430,453]
                    screen.blit(number, number_position)
                if 23 in s.holes:
                    number_position = [329,400]
                    screen.blit(number, number_position)
                if 24 in s.holes:
                    number_position = [328,453]
                    screen.blit(number, number_position)
                if 25 in s.holes:
                    number_position = [380,453]
                    screen.blit(number, number_position)
            if s.game.magic_screen.position == 2:
                if 1 in s.holes:
                    number_position = [278,560]
                    screen.blit(number, number_position)
                    number_position = [431,400]
                    screen.blit(number, number_position)
                if 2 in s.holes:
                    number_position = [226,560]
                    screen.blit(number, number_position)
                if 3 in s.holes:
                    number_position = [380,346]
                    screen.blit(number, number_position)
                if 4 in s.holes:
                    number_position = [327,507]
                    screen.blit(number, number_position)
                if 5 in s.holes:
                    number_position = [226,399]
                    screen.blit(number, number_position)
                    number_position = [429,508]
                    screen.blit(number, number_position)
                if 6 in s.holes:
                    number_position = [329,400]
                    screen.blit(number, number_position)
                if 7 in s.holes:
                    number_position = [226,507]
                    screen.blit(number, number_position)
                if 8 in s.holes:
                    number_position = [278,346]
                    screen.blit(number, number_position)
                    number_position = [377,560]
                    screen.blit(number, number_position)
                if 9 in s.holes:
                    number_position = [329,560]
                    screen.blit(number, number_position)
                if 12 in s.holes:
                    number_position = [330,346]
                    screen.blit(number, number_position)
                if 14 in s.holes:
                    number_position = [229,346]
                    screen.blit(number, number_position)
                    number_position = [379,400]
                    screen.blit(number, number_position)
                if 16 in s.holes:
                    number_position = [229,453]
                    screen.blit(number, number_position)
                    number_position = [379,508]
                    screen.blit(number, number_position)
                if 18 in s.holes:
                    number_position = [277,507]
                    screen.blit(number, number_position)
                if 19 in s.holes:
                    number_position = [430,453]
                    screen.blit(number, number_position)
                if 22 in s.holes:
                    number_position = [379,453]
                    screen.blit(number, number_position)
                if 23 in s.holes:
                    number_position = [277,397]
                    screen.blit(number, number_position)
                if 24 in s.holes:
                    number_position = [276,453]
                    screen.blit(number, number_position)
                    number_position = [430,345]
                    screen.blit(number, number_position)
                if 25 in s.holes:
                    number_position = [326,453]
                    screen.blit(number, number_position)
                    number_position = [430,559]
                    screen.blit(number, number_position)
            if s.game.magic_screen.position == 3:
                if 1 in s.holes:
                    number_position = [225,560]
                    screen.blit(number, number_position)
                    number_position = [376,400]
                    screen.blit(number, number_position)
                if 3 in s.holes:
                    number_position = [329,347]
                    screen.blit(number, number_position)
                if 4 in s.holes:
                    number_position = [277,508]
                    screen.blit(number, number_position)
                if 5 in s.holes:
                    number_position = [378,507]
                    screen.blit(number, number_position)
                if 6 in s.holes:
                    number_position = [277,400]
                    screen.blit(number, number_position)
                if 8 in s.holes:
                    number_position = [226,345]
                    screen.blit(number, number_position)
                    number_position = [325,560]
                    screen.blit(number, number_position)
                if 9 in s.holes:
                    number_position = [277,561]
                    screen.blit(number, number_position)
                    number_position = [429,453]
                    screen.blit(number, number_position)
                if 12 in s.holes:
                    number_position = [277,347]
                    screen.blit(number, number_position)
                    number_position = [431,400]
                    screen.blit(number, number_position)
                if 14 in s.holes:
                    number_position = [327,398]
                    screen.blit(number, number_position)
                if 16 in s.holes:
                    number_position = [327,508]
                    screen.blit(number, number_position)
                if 18 in s.holes:
                    number_position = [225,507]
                    screen.blit(number, number_position)
                if 19 in s.holes:
                    number_position = [379,453]
                    screen.blit(number, number_position)
                if 20 in s.holes:
                    number_position = [430,346]
                    screen.blit(number, number_position)
                if 21 in s.holes:
                    number_position = [430,560]
                    screen.blit(number, number_position)
                if 22 in s.holes:
                    number_position = [327,453]
                    screen.blit(number, number_position)
                if 23 in s.holes:
                    number_position = [225,397]
                    screen.blit(number, number_position)
                    number_position = [428,507]
                    screen.blit(number, number_position)
                if 24 in s.holes:
                    number_position = [379,345]
                    screen.blit(number, number_position)
                    number_position = [225,454]
                    screen.blit(number, number_position)
                if 25 in s.holes:
                    number_position = [277,453]
                    screen.blit(number, number_position)
                    number_position = [378,560]
                    screen.blit(number, number_position)
            if s.game.magic_screen.position == 4:
                if 1 in s.holes:
                    number_position = [329,400]
                    screen.blit(number, number_position)
                if 3 in s.holes:
                    number_position = [277,345]
                    screen.blit(number, number_position)
                if 4 in s.holes:
                    number_position = [431,400]
                    screen.blit(number, number_position)
                    number_position = [226,508]
                    screen.blit(number, number_position)
                if 5 in s.holes:
                    number_position = [327,508]
                    screen.blit(number, number_position)
                if 6 in s.holes:
                    number_position = [226,398]
                    screen.blit(number, number_position)
                if 7 in s.holes:
                    number_position = [430,452]
                    screen.blit(number, number_position)
                if 8 in s.holes:
                    number_position = [277,560]
                    screen.blit(number, number_position)
                if 9 in s.holes:
                    number_position = [379,453]
                    screen.blit(number, number_position)
                    number_position = [225,560]
                    screen.blit(number, number_position)
                if 12 in s.holes:
                    number_position = [228,346]
                    screen.blit(number, number_position)
                    number_position = [380,400]
                    screen.blit(number, number_position)
                if 13 in s.holes:
                    number_position = [430,507]
                    screen.blit(number, number_position)
                if 14 in s.holes:
                    number_position = [278,397]
                    screen.blit(number, number_position)
                if 15 in s.holes:
                    number_position = [431,560]
                    screen.blit(number, number_position)
                if 16 in s.holes:
                    number_position = [276,505]
                    screen.blit(number, number_position)
                if 17 in s.holes:
                    number_position = [432,347]
                    screen.blit(number, number_position)
                if 19 in s.holes:
                    number_position = [327,453]
                    screen.blit(number, number_position)
                if 20 in s.holes:
                    number_position = [380,347]
                    screen.blit(number, number_position)
                if 21 in s.holes:
                    number_position = [378,562]
                    screen.blit(number, number_position)
                if 22 in s.holes:
                    number_position = [275,453]
                    screen.blit(number, number_position)
                if 23 in s.holes:
                    number_position = [378,507]
                    screen.blit(number, number_position)
                if 24 in s.holes:
                    number_position = [328,347]
                    screen.blit(number, number_position)
                if 25 in s.holes:
                    number_position = [225,453]
                    screen.blit(number, number_position)
                    number_position = [327,560]
                    screen.blit(number, number_position)
            if s.game.magic_screen.position == 5:
                if 1 in s.holes:
                    number_position = [278,400]
                    screen.blit(number, number_position)
                if 2 in s.holes:
                    number_position = [430,560]
                    screen.blit(number, number_position)
                if 3 in s.holes:
                    number_position = [228,346]
                    screen.blit(number, number_position)
                if 4 in s.holes:
                    number_position = [380,400]
                    screen.blit(number, number_position)
                if 5 in s.holes:
                    number_position = [276,507]
                    screen.blit(number, number_position)
                if 6 in s.holes:
                    number_position = [431,347]
                    screen.blit(number, number_position)
                if 7 in s.holes:
                    number_position = [380,453]
                    screen.blit(number, number_position)
                if 8 in s.holes:
                    number_position = [226,559]
                    screen.blit(number, number_position)
                if 9 in s.holes:
                    number_position = [328,455]
                    screen.blit(number, number_position)
                if 10 in s.holes:
                    number_position = [432,400]
                    screen.blit(number, number_position)
                if 11 in s.holes:
                    number_position = [430,508]
                    screen.blit(number, number_position)
                if 12 in s.holes:
                    number_position = [329,400]
                    screen.blit(number, number_position)
                if 13 in s.holes:
                    number_position = [379,507]
                    screen.blit(number, number_position)
                if 14 in s.holes:
                    number_position = [227,398]
                    screen.blit(number, number_position)
                if 15 in s.holes:
                    number_position = [379,561]
                    screen.blit(number, number_position)
                if 16 in s.holes:
                    number_position = [229,506]
                    screen.blit(number, number_position)
                if 17 in s.holes:
                    number_position = [380,347]
                    screen.blit(number, number_position)
                if 18 in s.holes:
                    number_position = [432,453]
                    screen.blit(number, number_position)
                if 19 in s.holes:
                    number_position = [278,452]
                    screen.blit(number, number_position)
                if 20 in s.holes:
                    number_position = [329,346]
                    screen.blit(number, number_position)
                if 21 in s.holes:
                    number_position = [328,559]
                    screen.blit(number, number_position)
                if 22 in s.holes:
                    number_position = [226,454]
                    screen.blit(number, number_position)
                if 23 in s.holes:
                    number_position = [329,507]
                    screen.blit(number, number_position)
                if 24 in s.holes:
                    number_position = [278,346]
                    screen.blit(number, number_position)
                if 25 in s.holes:
                    number_position = [279,559]
                    screen.blit(number, number_position)
            if s.game.magic_screen.position == 6:
                if 1 in s.holes:
                    number_position = [228,397]
                    screen.blit(number, number_position)
                if 2 in s.holes:
                    number_position = [379,560]
                    screen.blit(number, number_position)
                if 4 in s.holes:
                    number_position = [329,397]
                    screen.blit(number, number_position)
                    number_position = [430,560]
                    screen.blit(number, number_position)
                if 5 in s.holes:
                    number_position = [226,507]
                    screen.blit(number, number_position)
                if 6 in s.holes:
                    number_position = [379,347]
                    screen.blit(number, number_position)
                if 7 in s.holes:
                    number_position = [328,453]
                    screen.blit(number, number_position)
                if 9 in s.holes:
                    number_position = [276,451]
                    screen.blit(number, number_position)
                if 10 in s.holes:
                    number_position = [379,398]
                    screen.blit(number, number_position)
                if 11 in s.holes:
                    number_position = [379,507]
                    screen.blit(number, number_position)
                if 12 in s.holes:
                    number_position = [279,399]
                    screen.blit(number, number_position)
                    number_position = [430,453]
                    screen.blit(number, number_position)
                if 13 in s.holes:
                    number_position = [432,347]
                    screen.blit(number, number_position)
                    number_position = [327,507]
                    screen.blit(number, number_position)
                if 15 in s.holes:
                    number_position = [326,560]
                    screen.blit(number, number_position)
                if 17 in s.holes:
                    number_position = [328,345]
                    screen.blit(number, number_position)
                if 18 in s.holes:
                    number_position = [379,453]
                    screen.blit(number, number_position)
                if 19 in s.holes:
                    number_position = [226,453]
                    screen.blit(number, number_position)
                    number_position = [430,507]
                    screen.blit(number, number_position)
                if 20 in s.holes:
                    number_position = [278,345]
                    screen.blit(number, number_position)
                if 21 in s.holes:
                    number_position = [432,400]
                    screen.blit(number, number_position)
                    number_position = [278,559]
                    screen.blit(number, number_position)
                if 23 in s.holes:
                    number_position = [276,505]
                    screen.blit(number, number_position)
                if 24 in s.holes:
                    number_position = [228,345]
                    screen.blit(number, number_position)
                if 25 in s.holes:
                    number_position = [226,559]
                    screen.blit(number, number_position)
            if s.game.magic_screen.position == 7:
                if 2 in s.holes:
                    number_position = [431,400]
                    screen.blit(number, number_position)
                    number_position = [328,560]
                    screen.blit(number, number_position)
                if 4 in s.holes:
                    number_position = [278,399]
                    screen.blit(number, number_position)
                    number_position = [379,561]
                    screen.blit(number, number_position)
                if 6 in s.holes:
                    number_position = [329,345]
                    screen.blit(number, number_position)
                    number_position = [431,506]
                    screen.blit(number, number_position)
                if 7 in s.holes:
                    number_position = [277,451]
                    screen.blit(number, number_position)
                if 9 in s.holes:
                    number_position = [432,346]
                    screen.blit(number, number_position)
                    number_position = [227,453]
                    screen.blit(number, number_position)
                if 10 in s.holes:
                    number_position = [328,400]
                    screen.blit(number, number_position)
                if 11 in s.holes:
                    number_position = [328,507]
                    screen.blit(number, number_position)
                if 12 in s.holes:
                    number_position = [380,453]
                    screen.blit(number, number_position)
                    number_position = [226,398]
                    screen.blit(number, number_position)
                if 13 in s.holes:
                    number_position = [379,345]
                    screen.blit(number, number_position)
                    number_position = [276,505]
                    screen.blit(number, number_position)
                if 15 in s.holes:
                    number_position = [277,560]
                    screen.blit(number, number_position)
                if 17 in s.holes:
                    number_position = [278,346]
                    screen.blit(number, number_position)
                if 18 in s.holes:
                    number_position = [328,452]
                    screen.blit(number, number_position)
                if 19 in s.holes:
                    number_position = [380,507]
                    screen.blit(number, number_position)
                if 20 in s.holes:
                    number_position = [227,346]
                    screen.blit(number, number_position)
                    number_position = [431,560]
                    screen.blit(number, number_position)
                if 21 in s.holes:
                    number_position = [379,400]
                    screen.blit(number, number_position)
                    number_position = [226,560]
                    screen.blit(number, number_position)
                if 23 in s.holes:
                    number_position = [430,453]
                    screen.blit(number, number_position)
                    number_position = [225,507]
                    screen.blit(number, number_position)
            if s.game.magic_screen.position == 8:
                if 2 in s.holes:
                    number_position = [379,400]
                    screen.blit(number, number_position)
                    number_position = [278,559]
                    screen.blit(number, number_position)
                if 4 in s.holes:
                    number_position = [227,398]
                    screen.blit(number, number_position)
                    number_position = [327,559]
                    screen.blit(number, number_position)
                if 6 in s.holes:
                    number_position = [276,343]
                    screen.blit(number, number_position)
                    number_position = [377,507]
                    screen.blit(number, number_position)
                if 7 in s.holes:
                    number_position = [226,455]
                    screen.blit(number, number_position)
                if 9 in s.holes:
                    number_position = [381,347]
                    screen.blit(number, number_position)
                if 10 in s.holes:
                    number_position = [277,398]
                    screen.blit(number, number_position)
                    number_position = [430,559]
                    screen.blit(number, number_position)
                if 11 in s.holes:
                    number_position = [430,453]
                    screen.blit(number, number_position)
                    number_position = [276,507]
                    screen.blit(number, number_position)
                if 12 in s.holes:
                    number_position = [328,453]
                    screen.blit(number, number_position)
                if 13 in s.holes:
                    number_position = [329,346]
                    screen.blit(number, number_position)
                    number_position = [225,507]
                    screen.blit(number, number_position)
                if 15 in s.holes:
                    number_position = [432,400]
                    screen.blit(number, number_position)
                    number_position = [227,562]
                    screen.blit(number, number_position)
                if 17 in s.holes:
                    number_position = [227,345]
                    screen.blit(number, number_position)
                    number_position = [430,507]
                    screen.blit(number, number_position)
                if 18 in s.holes:
                    number_position = [432,347]
                    screen.blit(number, number_position)
                    number_position = [277,453]
                    screen.blit(number, number_position)
                if 19 in s.holes:
                    number_position = [329,507]
                    screen.blit(number, number_position)
                if 20 in s.holes:
                    number_position = [378,560]
                    screen.blit(number, number_position)
                if 21 in s.holes:
                    number_position = [328,400]
                    screen.blit(number, number_position)
                if 23 in s.holes:
                    number_position = [380,454]
                    screen.blit(number, number_position)
            if s.game.magic_screen.position == 9:
                if 1 in s.holes:
                    number_position = [430,508]
                    screen.blit(number, number_position)
                if 2 in s.holes:
                    number_position = [330,400]
                    screen.blit(number, number_position)
                    number_position = [226,560]
                    screen.blit(number, number_position)
                if 4 in s.holes:
                    number_position = [278,560]
                    screen.blit(number, number_position)
                if 6 in s.holes:
                    number_position = [228,347]
                    screen.blit(number, number_position)
                    number_position = [329,507]
                    screen.blit(number, number_position)
                if 7 in s.holes:
                    number_position = [433,347]
                    screen.blit(number, number_position)
                if 8 in s.holes:
                    number_position = [433,400]
                    screen.blit(number, number_position)
                if 9 in s.holes:
                    number_position = [330,346]
                    screen.blit(number, number_position)
                if 10 in s.holes:
                    number_position = [226,400]
                    screen.blit(number, number_position)
                    number_position = [379,560]
                    screen.blit(number, number_position)
                if 11 in s.holes:
                    number_position = [379,453]
                    screen.blit(number, number_position)
                    number_position = [227,507]
                    screen.blit(number, number_position)
                if 12 in s.holes:
                    number_position = [277,453]
                    screen.blit(number, number_position)
                if 13 in s.holes:
                    number_position = [278,347]
                    screen.blit(number, number_position)
                if 15 in s.holes:
                    number_position = [379,400]
                    screen.blit(number, number_position)
                if 16 in s.holes:
                    number_position = [429,453]
                    screen.blit(number, number_position)
                if 17 in s.holes:
                    number_position = [379,507]
                    screen.blit(number, number_position)
                if 18 in s.holes:
                    number_position = [380,347]
                    screen.blit(number, number_position)
                    number_position = [227,453]
                    screen.blit(number, number_position)
                if 19 in s.holes:
                    number_position = [277,505]
                    screen.blit(number, number_position)
                if 20 in s.holes:
                    number_position = [328,560]
                    screen.blit(number, number_position)
                if 21 in s.holes:
                    number_position = [279,398]
                    screen.blit(number, number_position)
                if 22 in s.holes:
                    number_position = [432,561]
                    screen.blit(number, number_position)
                if 23 in s.holes:
                    number_position = [329,453]
                    screen.blit(number, number_position)
            if s.game.magic_screen.position == 10:
                if 1 in s.holes:
                    number_position = [378,507]
                    screen.blit(number, number_position)
                if 2 in s.holes:
                    number_position = [278,400]
                    screen.blit(number, number_position)
                if 3 in s.holes:
                    number_position = [431,560]
                    screen.blit(number, number_position)
                if 4 in s.holes:
                    number_position = [225,560]
                    screen.blit(number, number_position)
                if 5 in s.holes:
                    number_position = [431,347]
                    screen.blit(number, number_position)
                if 6 in s.holes:
                    number_position = [277,507]
                    screen.blit(number, number_position)
                if 7 in s.holes:
                    number_position = [381,346]
                    screen.blit(number, number_position)
                if 8 in s.holes:
                    number_position = [380,400]
                    screen.blit(number, number_position)
                if 9 in s.holes:
                    number_position = [278,346]
                    screen.blit(number, number_position)
                if 10 in s.holes:
                    number_position = [328,561]
                    screen.blit(number, number_position)
                if 11 in s.holes:
                    number_position = [328,453]
                    screen.blit(number, number_position)
                if 12 in s.holes:
                    number_position = [226,454]
                    screen.blit(number, number_position)
                if 13 in s.holes:
                    number_position = [227,347]
                    screen.blit(number, number_position)
                if 14 in s.holes:
                    number_position = [428,507]
                    screen.blit(number, number_position)
                if 15 in s.holes:
                    number_position = [328,400]
                    screen.blit(number, number_position)
                if 16 in s.holes:
                    number_position = [379,453]
                    screen.blit(number, number_position)
                if 17 in s.holes:
                    number_position = [328,507]
                    screen.blit(number, number_position)
                if 18 in s.holes:
                    number_position = [329,347]
                    screen.blit(number, number_position)
                if 19 in s.holes:
                    number_position = [225,507]
                    screen.blit(number, number_position)
                if 20 in s.holes:
                    number_position = [278,560]
                    screen.blit(number, number_position)
                if 21 in s.holes:
                    number_position = [227,400]
                    screen.blit(number, number_position)
                if 22 in s.holes:
                    number_position = [378,560]
                    screen.blit(number, number_position)
                if 23 in s.holes:
                    number_position = [277,453]
                    screen.blit(number, number_position)
                if 24 in s.holes:
                    number_position = [430,453]
                    screen.blit(number, number_position)
                if 25 in s.holes:
                    number_position = [430,400]
                    screen.blit(number, number_position)


    if s.game.red_odds.position == 1:
        o = [212,786]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 2:
        o = [260,786]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 3:
        o = [305,786]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 4:
        o = [351,786]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 5:
        o = [394,786]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 6:
        o = [442,786]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 7:
        o = [484,786]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 8:
        o = [529,786]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 9:
        o = [573,786]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 10:
        o = [614,786]
        screen.blit(odds, o)

    if s.game.yellow_odds.position == 1:
        o = [195,865]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 2:
        o = [240,865]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 3:
        o = [285,865]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 4:
        o = [326,865]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 5:
        o = [370,865]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 6:
        o = [415,865]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 7:
        o = [460,865]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 8:
        o = [505,865]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 9:
        o = [545,865]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 10:
        o = [590,865]
        screen.blit(odds, o)

    if s.game.green_odds.position == 1:
        o = [175,942]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 2:
        o = [220,942]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 3:
        o = [265,942]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 4:
        o = [308,942]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 5:
        o = [350,942]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 6:
        o = [395,942]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 7:
        o = [440,942]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 8:
        o = [485,942]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 9:
        o = [528,942]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 10:
        o = [572,942]
        screen.blit(odds, o)


    if s.game.tilt.status == True:
        tilt_position = [50,200]
        screen.blit(tilt, tilt_position)

    pygame.display.update()

def eb_animation(num):
    global screen

    if num == 3:
        eb_position = [145,1026]
        screen.blit(eb_number, eb_position)
        pygame.display.update()
    if num == 2:
        eb_position = [195,1025]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 1:
        eb_position = [257,1025]
        screen.blit(eb, eb_position)
        pygame.display.update()
