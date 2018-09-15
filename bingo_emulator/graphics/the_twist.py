
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
select_now = pygame.image.load('the_twist/assets/select_now.png').convert_alpha()
bg_menu = pygame.image.load('the_twist/assets/the_twist_menu.png').convert()
bg_menu.set_colorkey((255,0,252))
bg_gi = pygame.image.load('the_twist/assets/the_twist_gi.png').convert()
bg_gi.set_colorkey((255,0,252))
bg_off = pygame.image.load('the_twist/assets/the_twist_off.png').convert()
bg_off.set_colorkey((255,0,252))

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
        screen.blit(bg_menu, backglass_position)
    else:
        if (s.game.anti_cheat.status == True):
            screen.blit(bg_gi, backglass_position)
        else:
            screen.blit(bg_off, backglass_position)

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
            if s.game.ball_count.position == 4:
                s.cancel_delayed(name="blink")
                blink([s,1,1])
                s.cancel_delayed(name="blink_time")
                blink_time([s,1,1])
            else:
                s.cancel_delayed(name="blink")
                s.cancel_delayed(name="blink_time")
        elif s.game.before_fourth.status == True:
            bf = [598,623]
            screen.blit(before_fourth, bf)
            if s.game.ball_count.position == 3:
                s.cancel_delayed(name="blink")
                blink([s,1,1])
                s.cancel_delayed(name="blink_time")
                blink_time([s,1,1])
            else:
                s.cancel_delayed(name="blink")
                s.cancel_delayed(name="blink_time")

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

def blink_time(args):
    dirty_rects = []
    s = args[0]
    b = args[1]
    sn = args[2]

    if b == 0:
        if sn == 1:
            if s.game.before_fourth.status == True:
                p = [598,623]
                dirty_rects.append(screen.blit(before_fourth, p))
            else:
                p = [600,550]
                dirty_rects.append(screen.blit(before_fifth, p))
        pygame.display.update(dirty_rects)
    else:
        if s.game.before_fourth.status == True:
            dirty_rects.append(screen.blit(bg_gi, (598,623), pygame.Rect(598,623,119,59)))
        else:
            dirty_rects.append(screen.blit(bg_gi, (600,550), pygame.Rect(600,550,118,75)))
        pygame.display.update(dirty_rects)
    b = not b

    args = [s,b,sn]

    s.delay(name="blink_time", delay=0.1, handler=blink_time, param=args)

def blink(args):
    dirty_rects = []
    s = args[0]
    b = args[1]
    sn = args[2]

    if b == 0:
        if sn == 1:
            p = [141,655]
            dirty_rects.append(screen.blit(select_now, p))
        pygame.display.update(dirty_rects)
    else:
        dirty_rects.append(screen.blit(bg_gi, (141,655), pygame.Rect(141,655,453,38)))
        pygame.display.update(dirty_rects)
    b = not b

    args = [s,b,sn]

    s.delay(name="blink", delay=0.1, handler=blink, param=args)

def blink_letter(args):
    dirty_rects = []
    s = args[0]
    b = args[1]
    sn = args[2]

    if b == 0:
        if sn == 0:
            p = [123,691]
            dirty_rects.append(screen.blit(magic_card, p))
        elif sn == 1:
            p = [165,691]
            dirty_rects.append(screen.blit(magic_card, p))
        elif sn == 2:
            p = [210,691]
            dirty_rects.append(screen.blit(magic_card, p))
        elif sn == 3:
            p = [257,691]
            dirty_rects.append(screen.blit(magic_card, p))
        elif sn == 4:
            p = [301,691]
            dirty_rects.append(screen.blit(magic_card, p))
        elif sn == 5:
            p = [347,691]
            dirty_rects.append(screen.blit(magic_card, p))
        elif sn == 6:
            p = [391,691]
            dirty_rects.append(screen.blit(magic_card, p))
        elif sn == 7:
            p = [435,691]
            dirty_rects.append(screen.blit(magic_card, p))
        elif sn == 8:
            p = [480,691]
            dirty_rects.append(screen.blit(magic_card, p))
        elif sn == 9:
            p = [526,691]
            dirty_rects.append(screen.blit(magic_card, p))
        elif sn == 10:
            p = [570,691]
            dirty_rects.append(screen.blit(magic_card, p))
        pygame.display.update(dirty_rects)
    else:
        if sn == 0:
            dirty_rects.append(screen.blit(bg_gi, (123,691), pygame.Rect(123,691,46,81)))
        if sn == 1:
            dirty_rects.append(screen.blit(bg_gi, (165,691), pygame.Rect(165,691,46,81)))
        if sn == 2:
            dirty_rects.append(screen.blit(bg_gi, (210,691), pygame.Rect(210,691,46,81)))
        if sn == 3:
            dirty_rects.append(screen.blit(bg_gi, (257,691), pygame.Rect(257,691,46,81)))
        if sn == 4:
            dirty_rects.append(screen.blit(bg_gi, (301,691), pygame.Rect(301,691,46,81)))
        if sn == 5:
            dirty_rects.append(screen.blit(bg_gi, (347,691), pygame.Rect(347,691,46,81)))
        if sn == 6:
            dirty_rects.append(screen.blit(bg_gi, (391,691), pygame.Rect(391,691,46,81)))
        if sn == 7:
            dirty_rects.append(screen.blit(bg_gi, (435,691), pygame.Rect(435,691,46,81)))
        if sn == 8:
            dirty_rects.append(screen.blit(bg_gi, (480,691), pygame.Rect(480,691,46,81)))
        if sn == 9:
            dirty_rects.append(screen.blit(bg_gi, (526,691), pygame.Rect(526,691,46,81)))
        if sn == 10:
            dirty_rects.append(screen.blit(bg_gi, (570,691), pygame.Rect(570,691,46,81)))
        pygame.display.update(dirty_rects)
    b = not b

    args = [s,b,sn]

    s.delay(name="blink_letter", delay=0.1, handler=blink_letter, param=args)

def screen_animation(args):
    dirty_rects = []
    s = args[0]
    num = args[1]
    direction = args[2]
    
    if s.game.magic_screen.position == 0:
        p = [225,325]
    elif s.game.magic_screen.position == 1:
        p = [176,327]
    elif s.game.magic_screen.position == 2:
        p = [125,327]
    elif s.game.magic_screen.position == 3:
        p = [74,327]
    elif s.game.magic_screen.position == 4:
        p = [23,327]
    elif s.game.magic_screen.position == 5:
        p = [-25,327]
    elif s.game.magic_screen.position == 6:
        p = [-75,327]
    elif s.game.magic_screen.position == 7:
        p = [-127,327]
    elif s.game.magic_screen.position == 8:
        p = [-178,327]
    elif s.game.magic_screen.position == 9:
        p = [-229,327]
    elif s.game.magic_screen.position == 10:
        p = [-281,327]

    if direction == "left":
       p[0] = p[0] + num
    else:
       p[0] = p[0] - num
 
    dirty_rects.append(screen.blit(magic_screen, p))
    
    backglass_position = [0, 0]
    if (s.game.anti_cheat.status == True):
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],797,300)))
    else:
        dirty_rects.append(screen.blit(bg_off, p, pygame.Rect(p[0],p[1],797,300)))
    
    if s.game.start.status == True:
        if s.game.advance_green.status == True:
            p = [34,563]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],126,86)))
            dirty_rects.append(screen.blit(feature, p))
        if s.game.advance_yellow.status == True:
            p = [34,481]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],126,86)))
            dirty_rects.append(screen.blit(feature, p))
        if s.game.advance_red.status == True:
            p = [34,398]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],126,86)))
            dirty_rects.append(screen.blit(feature, p))
        if s.game.advance_card.status == True:
            p = [34,313]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],126,86)))
            dirty_rects.append(screen.blit(feature, p))

    if s.game.before_fifth.status == True:
        p = [600,550]
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],118,75)))
        dirty_rects.append(screen.blit(before_fifth, p))
    elif s.game.before_fourth.status == True:
        p = [598,623]
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],119,59)))
        dirty_rects.append(screen.blit(before_fourth, p))

    pygame.display.update(dirty_rects)


def eb_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]


    if s.game.extra_ball.position < 1:
        dirty_rects.append(screen.blit(bg_gi, (143,1056), pygame.Rect(143,1056,52,40)))
    if s.game.extra_ball.position < 2:
        dirty_rects.append(screen.blit(bg_gi, (194,1056), pygame.Rect(194,1056,69,38)))
    if s.game.extra_ball.position < 3:
        dirty_rects.append(screen.blit(bg_gi, (259,1056), pygame.Rect(259,1056,69,38)))
    if s.game.extra_ball.position < 4:
        dirty_rects.append(screen.blit(bg_gi, (326,1056), pygame.Rect(326,1056,52,40)))
    if s.game.extra_ball.position < 5:
        dirty_rects.append(screen.blit(bg_gi, (375,1056), pygame.Rect(375,1056,69,38)))
    if s.game.extra_ball.position < 6:
        dirty_rects.append(screen.blit(bg_gi, (438,1056), pygame.Rect(438,1056,69,38)))
    if s.game.extra_ball.position < 7:
        dirty_rects.append(screen.blit(bg_gi, (505,1056), pygame.Rect(505,1056,52,40)))
    if s.game.extra_ball.position < 8:
        dirty_rects.append(screen.blit(bg_gi, (555,1056), pygame.Rect(555,1056,69,38)))
    if s.game.extra_ball.position < 9:
        dirty_rects.append(screen.blit(bg_gi, (618,1056), pygame.Rect(618,1056,69,38)))
    pygame.display.update(dirty_rects)

    if num in [4,5,16,17,29,30,41,42]:
        if s.game.extra_ball.position < 1:
            p = [143,1056]
            dirty_rects.append(screen.blit(eb_number, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [0,6,7,25,31,32]:
        if s.game.extra_ball.position < 2:
            p = [194,1056]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [8,9,33,34]:
        if s.game.extra_ball.position < 3:
            p = [259,1056]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [1,10,11,24,26,35,36,49]:
        if s.game.extra_ball.position < 4:
            p = [326,1056]
            dirty_rects.append(screen.blit(eb_number, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [12,13,37,38]:
        if s.game.extra_ball.position < 5:
            p = [375,1056]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [2,14,15,27,39,40]:
        if s.game.extra_ball.position < 6:
            p = [438,1056]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [18,19,31,32]:
        if s.game.extra_ball.position < 7:
            p = [505,1056]
            dirty_rects.append(screen.blit(eb_number, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [3,20,21,28,33,34]:
        if s.game.extra_ball.position < 8:
            p = [555,1056]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [22,23,47,48]:
        if s.game.extra_ball.position < 9:
            p = [618,1056]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return

def clear_odds(s, num):
    global screen

    dirty_rects = []

    if s.game.yellow_odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (195,865), pygame.Rect(195,865,52,78)))
    if s.game.yellow_odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (285,865), pygame.Rect(285,865,52,78)))
    if s.game.yellow_odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (370,865), pygame.Rect(370,865,52,78)))
    if s.game.yellow_odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (460,865), pygame.Rect(460,865,52,78)))
    if s.game.yellow_odds.position != 10:
        dirty_rects.append(screen.blit(bg_gi, (590,865), pygame.Rect(590,865,52,78)))

    if s.game.red_odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (212,786), pygame.Rect(212,786,52,78)))
    if s.game.red_odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (305,786), pygame.Rect(305,786,52,78)))
    if s.game.red_odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (394,786), pygame.Rect(394,786,52,78)))
    if s.game.red_odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (484,786), pygame.Rect(484,786,52,78)))
    if s.game.red_odds.position != 10:
        dirty_rects.append(screen.blit(bg_gi, (614,786), pygame.Rect(614,786,52,78)))

    if s.game.green_odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (175,942), pygame.Rect(175,942,52,78)))
    if s.game.green_odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (265,942), pygame.Rect(265,942,52,78)))
    if s.game.green_odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (350,942), pygame.Rect(350,942,52,78)))
    if s.game.green_odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (440,942), pygame.Rect(440,942,52,78)))
    if s.game.green_odds.position != 10:
        dirty_rects.append(screen.blit(bg_gi, (572,942), pygame.Rect(572,942,52,78)))

    pygame.display.update(dirty_rects)

def draw_odds_animation(s, num):
    global screen
    dirty_rects = []

    if num in [3,28]:
        if s.game.yellow_odds.position != 1:
            p = [195,865]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [6,31]:
        if s.game.yellow_odds.position != 3:
            p = [285,865]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [16,41]:
        if s.game.yellow_odds.position != 5:
            p = [370,865]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [2,27]:
        if s.game.yellow_odds.position != 7:
            p = [460,865]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [19,44]:
        if s.game.yellow_odds.position != 10:
            p = [590,865]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return

    if num in [4,29]:
        if s.game.red_odds.position != 1:
            p = [212,786]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [7,32]:
        if s.game.red_odds.position != 3:
            p = [305,786]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [17,42]:
        if s.game.red_odds.position != 5:
            p = [394,786]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [1,26]:
        if s.game.red_odds.position != 7:
            p = [484,786]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [20,45]:
        if s.game.red_odds.position != 10:
            p = [614,786]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return

    if num in [5,30]:
        if s.game.green_odds.position != 1:
            p = [175,942]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [8,33]:
        if s.game.green_odds.position != 3:
            p = [265,942]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [18,43]:
        if s.game.green_odds.position != 5:
            p = [350,942]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [0,25]:
        if s.game.green_odds.position != 7:
            p = [440,942]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [21,46]:
        if s.game.green_odds.position != 10:
            p = [572,942]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return

def odds_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]

    clear_odds(s, num)

    draw_odds_animation(s, num)

def clear_features(s, num):
    global screen

    dirty_rects = []

    if s.game.magic_card.position < 1:
        dirty_rects.append(screen.blit(bg_gi, (165,691), pygame.Rect(165,691,46,81)))
    if s.game.magic_card.position < 2:
        dirty_rects.append(screen.blit(bg_gi, (210,691), pygame.Rect(210,691,46,81)))
    if s.game.magic_card.position < 3:
        dirty_rects.append(screen.blit(bg_gi, (257,691), pygame.Rect(257,691,46,81)))
    if s.game.magic_card.position < 4:
        dirty_rects.append(screen.blit(bg_gi, (301,691), pygame.Rect(301,691,46,81)))
    if s.game.magic_card.position < 5:
        dirty_rects.append(screen.blit(bg_gi, (347,691), pygame.Rect(347,691,46,81)))
    if s.game.magic_card.position < 6:
        dirty_rects.append(screen.blit(bg_gi, (391,691), pygame.Rect(391,691,46,81)))
    if s.game.magic_card.position < 7:
        dirty_rects.append(screen.blit(bg_gi, (435,691), pygame.Rect(435,691,46,81)))
    if s.game.magic_card.position < 8:
        dirty_rects.append(screen.blit(bg_gi, (480,691), pygame.Rect(480,691,46,81)))
    if s.game.magic_card.position < 9:
        dirty_rects.append(screen.blit(bg_gi, (526,691), pygame.Rect(526,691,46,81)))
    if s.game.magic_card.position < 10:
        dirty_rects.append(screen.blit(bg_gi, (570,691), pygame.Rect(570,691,46,81)))

    pygame.display.update(dirty_rects)


def draw_feature_animation(s, num):
    global screen
    dirty_rects = []
 
    if num in [12,37]:
        if s.game.magic_card.position < 1:
            p = [165,691]
            dirty_rects.append(screen.blit(magic_card, p))
            pygame.display.update(dirty_rects)
            return
    if num in [22,47]:
        if s.game.magic_card.position < 2:
            p = [210,691]
            dirty_rects.append(screen.blit(magic_card, p))
            pygame.display.update(dirty_rects)
            return
    if num in [11,36]:
        if s.game.magic_card.position < 3:
            p = [257,691]
            dirty_rects.append(screen.blit(magic_card, p))
            pygame.display.update(dirty_rects)
            return
    if num in [23,48]:
        if s.game.magic_card.position < 4:
            p = [301,691]
            dirty_rects.append(screen.blit(magic_card, p))
            pygame.display.update(dirty_rects)
            return
    if num in [10,35]:
        if s.game.magic_card.position < 5:
            p = [347,691]
            dirty_rects.append(screen.blit(magic_card, p))
            pygame.display.update(dirty_rects)
            return
    if num in [24,49]:
        if s.game.magic_card.position < 6:
            p = [391,691]
            dirty_rects.append(screen.blit(magic_card, p))
            pygame.display.update(dirty_rects)
            return
    if num in [9,34]:
        if s.game.magic_card.position < 7:
            p = [435,691]
            dirty_rects.append(screen.blit(magic_card, p))
            pygame.display.update(dirty_rects)
            return
    if num in [15,40]:
        if s.game.magic_card.position < 8:
            p = [480,691]
            dirty_rects.append(screen.blit(magic_card, p))
            pygame.display.update(dirty_rects)
            return
    if num in [14,39]:
        if s.game.magic_card.position < 9:
            p = [526,691]
            dirty_rects.append(screen.blit(magic_card, p))
            pygame.display.update(dirty_rects)
            return
    if num in [13,38]:
        if s.game.magic_card.position < 10:
            p = [570,691]
            dirty_rects.append(screen.blit(magic_card, p))
            pygame.display.update(dirty_rects)
            return

def feature_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]

    clear_features(s, num)

    draw_feature_animation(s, num)

def both_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]

    clear_features(s, num)
    clear_odds(s, num)

    draw_odds_animation(s, num)
    draw_feature_animation(s, num)
