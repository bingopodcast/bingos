
import pygame
import random

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

meter = pygame.image.load('graphics/assets/register_cover.png').convert()
sa = pygame.image.load('yacht_club/assets/super1_arrow.png').convert_alpha()
s1 = pygame.image.load('yacht_club/assets/super1.png').convert_alpha()
s2 = pygame.image.load('yacht_club/assets/super2.png').convert_alpha()
s2a = pygame.image.load('yacht_club/assets/super2_arrow.png').convert_alpha()
eb = pygame.image.load('yacht_club/assets/eb_arrow.png').convert_alpha()
exb = pygame.image.load('yacht_club/assets/eb.png').convert_alpha()
o1 = pygame.image.load('yacht_club/assets/odds1.png').convert_alpha()
o2 = pygame.image.load('yacht_club/assets/odds2.png').convert_alpha()
o3 = pygame.image.load('yacht_club/assets/odds3.png').convert_alpha()
o4 = pygame.image.load('yacht_club/assets/odds4.png').convert_alpha()
o5 = pygame.image.load('yacht_club/assets/odds5.png').convert_alpha()
o6 = pygame.image.load('yacht_club/assets/odds6.png').convert_alpha()
o7 = pygame.image.load('yacht_club/assets/odds7.png').convert_alpha()
o8 = pygame.image.load('yacht_club/assets/odds8.png').convert_alpha()
star = pygame.image.load('yacht_club/assets/star.png').convert_alpha()
number = pygame.image.load('yacht_club/assets/number.png').convert_alpha()
select = pygame.image.load('yacht_club/assets/select_arrow.png').convert_alpha()
border = pygame.image.load('yacht_club/assets/card_border.png').convert_alpha()
card_arrow = pygame.image.load('yacht_club/assets/card_arrow.png').convert_alpha()
select_card = pygame.image.load('yacht_club/assets/select_card.png').convert_alpha()
cards = pygame.image.load('yacht_club/assets/cards.png').convert_alpha()
tilt = pygame.image.load('yacht_club/assets/tilt.png').convert_alpha()
select_now = pygame.image.load('yacht_club/assets/select_now.png').convert_alpha()
ebs = pygame.image.load('yacht_club/assets/extra_ball.png').convert_alpha()
bg_menu = pygame.image.load('yacht_club/assets/yacht_club_menu.png')
bg_gi = pygame.image.load('yacht_club/assets/yacht_club_gi.png')
bg_off = pygame.image.load('yacht_club/assets/yacht_club_off.png')

class scorereel():
    """ Score Reels are used to count replays """
    def __init__(self, pos, image):
        self.position = pos
        self.default_y = self.position[1]
        self.image = pygame.image.load(image).convert()

reel1 = scorereel([124,805], "graphics/assets/green_reel.png")
reel10 = scorereel([103,805], "graphics/assets/green_reel.png")
reel100 = scorereel([84,805], "graphics/assets/green_reel.png")

def display(s, replays=0, menu=False):
    
    meter.set_colorkey((255,0,252))
    meter_position = [75,805]

    screen.blit(reel1.image, reel1.position)
    screen.blit(reel10.image, reel10.position)
    screen.blit(reel100.image, reel100.position)
    screen.blit(meter, meter_position)

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
    
    if s.game.super_card.position == 1:
        p = [38,362]
        screen.blit(sa, p)
    if s.game.super_card.position == 2:
        p = [40,399]
        screen.blit(sa, p)
    if s.game.super_card.position == 3:
        p = [40,435]
        screen.blit(sa, p)
    if s.game.super_card.position == 4:
        p = [40,470]
        screen.blit(sa, p)
    if s.game.super_card.position >= 5:
        p = [19,507]
        screen.blit(s1, p)
    if s.game.super_card.position == 6:
        p = [655,584]
        screen.blit(s2a, p)
    if s.game.super_card.position == 7:
        p = [656,547]
        screen.blit(s2a, p)
    if s.game.super_card.position == 8:
        p = [656,511]
        screen.blit(s2a, p)
    if s.game.super_card.position == 9:
        p = [656,475]
        screen.blit(s2a, p)
    if s.game.super_card.position >= 10:
        p = [635,404]
        screen.blit(s2, p)

    if s.game.extra_ball.position == 1:
        eb_position = [33,971]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 2:
        eb_position = [64,971]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 3:
        eb_position = [93,971]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 4:
        eb_position = [123,971]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 5:
        eb_position = [152,971]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 6:
        eb_position = [183,971]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 7:
        eb_position = [212,971]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 8:
        eb_position = [258,971]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 9:
        eb_position = [289,971]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 10:
        eb_position = [318,971]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 11:
        eb_position = [349,971]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 12:
        eb_position = [378,971]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 13:
        eb_position = [409,971]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 14:
        eb_position = [440,971]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 15:
        eb_position = [486,971]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 16:
        eb_position = [518,971]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 17:
        eb_position = [547,971]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 18:
        eb_position = [577,971]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 19:
        eb_position = [607,971]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 20:
        eb_position = [636,971]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 21:
        eb_position = [667,971]
        screen.blit(eb, eb_position)
    
   
    if s.game.extra_ball.position >= 7:
        p = [27,996]
        screen.blit(exb, p)
    if s.game.extra_ball.position >= 14:
        p = [252,996]
        screen.blit(exb, p)
    if s.game.extra_ball.position >= 21:
        p = [479,996]
        screen.blit(exb, p)
    
    if s.game.odds.position > 0:
        if s.game.odds.position == 1:
            odds_position = [183,789]
            screen.blit(o1, odds_position)
        if s.game.odds.position == 2:
            odds_position = [239,816]
            screen.blit(o2, odds_position)
        if s.game.odds.position == 3:
            odds_position = [284,787]
            screen.blit(o3, odds_position)
        if s.game.odds.position == 4:
            odds_position = [348,822]
            screen.blit(o4, odds_position)
        if s.game.odds.position == 5:
            odds_position = [396,790]
            screen.blit(o5, odds_position)
        if s.game.odds.position == 6:
            odds_position = [450,788]
            screen.blit(o6, odds_position)
        if s.game.odds.position == 7:
            odds_position = [497,844]
            screen.blit(o7, odds_position)
        if s.game.odds.position == 8:
            odds_position = [596,818]
            screen.blit(o8, odds_position)

    if s.game.yellow_star.status == True:
        rs_position = [22,684]
        screen.blit(star, rs_position)

    if s.game.red_star.status == True:
        ys_position = [633,683]
        screen.blit(star, ys_position)

    if s.game.tilt.status == False:
        if s.holes:
            if s.game.card.position == 0:
                if 1 in s.holes:
                    number_position = [162,343]
                    screen.blit(number, number_position)
                if 2 in s.holes:
                    number_position = [107,567]
                    screen.blit(number, number_position)
                if 3 in s.holes:
                    number_position = [219,512]
                    screen.blit(number, number_position)
                if 4 in s.holes:
                    number_position = [275,566]
                    screen.blit(number, number_position)
                if 5 in s.holes:
                    number_position = [162,455]
                    screen.blit(number, number_position)
                if 6 in s.holes:
                    number_position = [106,400]
                    screen.blit(number, number_position)
                if 7 in s.holes:
                    number_position = [275,344]
                    screen.blit(number, number_position)
                if 8 in s.holes:
                    number_position = [219,400]
                    screen.blit(number, number_position)
                if 9 in s.holes:
                    number_position = [106,512]
                    screen.blit(number, number_position)
                if 10 in s.holes:
                    number_position = [106,343]
                    screen.blit(number, number_position)
                if 11 in s.holes:
                    number_position = [219,566]
                    screen.blit(number, number_position)
                if 12 in s.holes:
                    number_position = [219,343]
                    screen.blit(number, number_position)
                if 13 in s.holes:
                    number_position = [162,566]
                    screen.blit(number, number_position)
                if 14 in s.holes:
                    number_position = [331,566]
                    screen.blit(number, number_position)
                if 15 in s.holes:
                    number_position = [331,455]
                    screen.blit(number, number_position)
                if 16 in s.holes:
                    number_position = [331,343]
                    screen.blit(number, number_position)
                if 17 in s.holes:
                    number_position = [219,455]
                    screen.blit(number, number_position)
                if 18 in s.holes:
                    number_position = [106,455]
                    screen.blit(number, number_position)
                if 19 in s.holes:
                    number_position = [162,400]
                    screen.blit(number, number_position)
                if 20 in s.holes:
                    number_position = [275,400]
                    screen.blit(number, number_position)
                if 21 in s.holes:
                    number_position = [275,512]
                    screen.blit(number, number_position)
                if 22 in s.holes:
                    number_position = [162,512]
                    screen.blit(number, number_position)
                if 23 in s.holes:
                    number_position = [331,512]
                    screen.blit(number, number_position)
                if 24 in s.holes:
                    number_position = [331,400]
                    screen.blit(number, number_position)
                if 25 in s.holes:
                    number_position = [275,455]
                    screen.blit(number, number_position)

            elif s.game.card.position == 1:
                if 1 in s.holes:
                    number_position = [162,343]
                    screen.blit(number, number_position)
                if 2 in s.holes:
                    number_position = [387,512]
                    screen.blit(number, number_position)
                if 3 in s.holes:
                    number_position = [219,512]
                    screen.blit(number, number_position)
                if 4 in s.holes:
                    number_position = [275,566]
                    screen.blit(number, number_position)
                if 5 in s.holes:
                    number_position = [162,455]
                    screen.blit(number, number_position)
                if 6 in s.holes:
                    number_position = [387,566]
                    screen.blit(number, number_position)
                if 7 in s.holes:
                    number_position = [275,344]
                    screen.blit(number, number_position)
                if 8 in s.holes:
                    number_position = [219,400]
                    screen.blit(number, number_position)
                if 9 in s.holes:
                    number_position = [387,400]
                    screen.blit(number, number_position)
                if 10 in s.holes:
                    number_position = [387,455]
                    screen.blit(number, number_position)
                if 11 in s.holes:
                    number_position = [219,566]
                    screen.blit(number, number_position)
                if 12 in s.holes:
                    number_position = [219,343]
                    screen.blit(number, number_position)
                if 13 in s.holes:
                    number_position = [162,566]
                    screen.blit(number, number_position)
                if 14 in s.holes:
                    number_position = [331,566]
                    screen.blit(number, number_position)
                if 15 in s.holes:
                    number_position = [331,455]
                    screen.blit(number, number_position)
                if 16 in s.holes:
                    number_position = [331,343]
                    screen.blit(number, number_position)
                if 17 in s.holes:
                    number_position = [219,455]
                    screen.blit(number, number_position)
                if 18 in s.holes:
                    number_position = [387,343]
                    screen.blit(number, number_position)
                if 19 in s.holes:
                    number_position = [162,400]
                    screen.blit(number, number_position)
                if 20 in s.holes:
                    number_position = [275,400]
                    screen.blit(number, number_position)
                if 21 in s.holes:
                    number_position = [275,512]
                    screen.blit(number, number_position)
                if 22 in s.holes:
                    number_position = [162,512]
                    screen.blit(number, number_position)
                if 23 in s.holes:
                    number_position = [331,512]
                    screen.blit(number, number_position)
                if 24 in s.holes:
                    number_position = [331,400]
                    screen.blit(number, number_position)
                if 25 in s.holes:
                    number_position = [275,455]
                    screen.blit(number, number_position)

            elif s.game.card.position == 2:
                if 1 in s.holes:
                    number_position = [443,455]
                    screen.blit(number, number_position)
                if 2 in s.holes:
                    number_position = [387,512]
                    screen.blit(number, number_position)
                if 3 in s.holes:
                    number_position = [219,512]
                    screen.blit(number, number_position)
                if 4 in s.holes:
                    number_position = [275,566]
                    screen.blit(number, number_position)
                if 5 in s.holes:
                    number_position = [443,511]
                    screen.blit(number, number_position)
                if 6 in s.holes:
                    number_position = [387,566]
                    screen.blit(number, number_position)
                if 7 in s.holes:
                    number_position = [275,344]
                    screen.blit(number, number_position)
                if 8 in s.holes:
                    number_position = [219,400]
                    screen.blit(number, number_position)
                if 9 in s.holes:
                    number_position = [387,400]
                    screen.blit(number, number_position)
                if 10 in s.holes:
                    number_position = [387,455]
                    screen.blit(number, number_position)
                if 11 in s.holes:
                    number_position = [219,566]
                    screen.blit(number, number_position)
                if 12 in s.holes:
                    number_position = [219,343]
                    screen.blit(number, number_position)
                if 13 in s.holes:
                    number_position = [443,400]
                    screen.blit(number, number_position)
                if 14 in s.holes:
                    number_position = [331,566]
                    screen.blit(number, number_position)
                if 15 in s.holes:
                    number_position = [331,455]
                    screen.blit(number, number_position)
                if 16 in s.holes:
                    number_position = [331,343]
                    screen.blit(number, number_position)
                if 17 in s.holes:
                    number_position = [219,455]
                    screen.blit(number, number_position)
                if 18 in s.holes:
                    number_position = [387,343]
                    screen.blit(number, number_position)
                if 19 in s.holes:
                    number_position = [443,343]
                    screen.blit(number, number_position)
                if 20 in s.holes:
                    number_position = [275,400]
                    screen.blit(number, number_position)
                if 21 in s.holes:
                    number_position = [275,512]
                    screen.blit(number, number_position)
                if 22 in s.holes:
                    number_position = [443,566]
                    screen.blit(number, number_position)
                if 23 in s.holes:
                    number_position = [331,512]
                    screen.blit(number, number_position)
                if 24 in s.holes:
                    number_position = [331,400]
                    screen.blit(number, number_position)
                if 25 in s.holes:
                    number_position = [275,455]
                    screen.blit(number, number_position)

            elif s.game.card.position == 3:
                if 1 in s.holes:
                    number_position = [443,455]
                    screen.blit(number, number_position)
                if 2 in s.holes:
                    number_position = [387,512]
                    screen.blit(number, number_position)
                if 3 in s.holes:
                    number_position = [500,344]
                    screen.blit(number, number_position)
                if 4 in s.holes:
                    number_position = [275,566]
                    screen.blit(number, number_position)
                if 5 in s.holes:
                    number_position = [443,511]
                    screen.blit(number, number_position)
                if 6 in s.holes:
                    number_position = [387,566]
                    screen.blit(number, number_position)
                if 7 in s.holes:
                    number_position = [275,344]
                    screen.blit(number, number_position)
                if 8 in s.holes:
                    number_position = [500,400]
                    screen.blit(number, number_position)
                if 9 in s.holes:
                    number_position = [387,400]
                    screen.blit(number, number_position)
                if 10 in s.holes:
                    number_position = [387,455]
                    screen.blit(number, number_position)
                if 11 in s.holes:
                    number_position = [500,455]
                    screen.blit(number, number_position)
                if 12 in s.holes:
                    number_position = [500,511]
                    screen.blit(number, number_position)
                if 13 in s.holes:
                    number_position = [443,400]
                    screen.blit(number, number_position)
                if 14 in s.holes:
                    number_position = [331,566]
                    screen.blit(number, number_position)
                if 15 in s.holes:
                    number_position = [331,455]
                    screen.blit(number, number_position)
                if 16 in s.holes:
                    number_position = [331,343]
                    screen.blit(number, number_position)
                if 17 in s.holes:
                    number_position = [500,566]
                    screen.blit(number, number_position)
                if 18 in s.holes:
                    number_position = [387,343]
                    screen.blit(number, number_position)
                if 19 in s.holes:
                    number_position = [443,343]
                    screen.blit(number, number_position)
                if 20 in s.holes:
                    number_position = [275,400]
                    screen.blit(number, number_position)
                if 21 in s.holes:
                    number_position = [275,512]
                    screen.blit(number, number_position)
                if 22 in s.holes:
                    number_position = [443,566]
                    screen.blit(number, number_position)
                if 23 in s.holes:
                    number_position = [331,512]
                    screen.blit(number, number_position)
                if 24 in s.holes:
                    number_position = [331,400]
                    screen.blit(number, number_position)
                if 25 in s.holes:
                    number_position = [275,455]
                    screen.blit(number, number_position)

            elif s.game.card.position == 4:
                if 1 in s.holes:
                    number_position = [443,455]
                    screen.blit(number, number_position)
                if 2 in s.holes:
                    number_position = [387,512]
                    screen.blit(number, number_position)
                if 3 in s.holes:
                    number_position = [500,344]
                    screen.blit(number, number_position)
                if 4 in s.holes:
                    number_position = [556,511]
                    screen.blit(number, number_position)
                if 5 in s.holes:
                    number_position = [443,511]
                    screen.blit(number, number_position)
                if 6 in s.holes:
                    number_position = [387,566]
                    screen.blit(number, number_position)
                if 7 in s.holes:
                    number_position = [556,400]
                    screen.blit(number, number_position)
                if 8 in s.holes:
                    number_position = [500,400]
                    screen.blit(number, number_position)
                if 9 in s.holes:
                    number_position = [387,400]
                    screen.blit(number, number_position)
                if 10 in s.holes:
                    number_position = [387,455]
                    screen.blit(number, number_position)
                if 11 in s.holes:
                    number_position = [500,455]
                    screen.blit(number, number_position)
                if 12 in s.holes:
                    number_position = [500,511]
                    screen.blit(number, number_position)
                if 13 in s.holes:
                    number_position = [443,400]
                    screen.blit(number, number_position)
                if 14 in s.holes:
                    number_position = [331,566]
                    screen.blit(number, number_position)
                if 15 in s.holes:
                    number_position = [331,455]
                    screen.blit(number, number_position)
                if 16 in s.holes:
                    number_position = [331,343]
                    screen.blit(number, number_position)
                if 17 in s.holes:
                    number_position = [500,566]
                    screen.blit(number, number_position)
                if 18 in s.holes:
                    number_position = [387,343]
                    screen.blit(number, number_position)
                if 19 in s.holes:
                    number_position = [443,343]
                    screen.blit(number, number_position)
                if 20 in s.holes:
                    number_position = [556,566]
                    screen.blit(number, number_position)
                if 21 in s.holes:
                    number_position = [556,455]
                    screen.blit(number, number_position)
                if 22 in s.holes:
                    number_position = [443,566]
                    screen.blit(number, number_position)
                if 23 in s.holes:
                    number_position = [331,512]
                    screen.blit(number, number_position)
                if 24 in s.holes:
                    number_position = [331,400]
                    screen.blit(number, number_position)
                if 25 in s.holes:
                    number_position = [556,343]
                    screen.blit(number, number_position)


    if s.game.tilt.status == False and menu == False:
        if s.game.card.position == 0:
            #selector lamp
            p = [93,644]
            screen.blit(select, p)
            #boundary lamps
            p = [96,335]
            screen.blit(border, p)
            p = [383,335]
            screen.blit(border, p)
        elif s.game.card.position == 1:
            #boundary lamps
            p = [155,335]
            screen.blit(border, p)
            p = [437,335]
            screen.blit(border, p)
        elif s.game.card.position == 2:
            #selector lamp
            p = [488,644]
            screen.blit(select, p)
            #boundary lamps
            p = [211,335]
            screen.blit(border, p)
            p = [493,335]
            screen.blit(border, p)
        elif s.game.card.position == 3:
            #selector lamp
            p = [543,644]
            screen.blit(select, p)
            #boundary lamps
            p = [268,335]
            screen.blit(border, p)
            p = [550,335]
            screen.blit(border, p)
        elif s.game.card.position == 4:
            #selector lamp
            p = [599,644]
            screen.blit(select, p)
            #boundary lamps
            p = [325,335]
            screen.blit(border, p)
            p = [607,335]
            screen.blit(border, p)


    if s.game.select_card.position == 1:
        p = [95,683]
        screen.blit(card_arrow, p)
    if s.game.select_card.position == 2:
        p = [135,683]
        screen.blit(card_arrow, p)
    if s.game.select_card.position == 3:
        p = [177,683]
        screen.blit(card_arrow, p)
    if s.game.select_card.position == 4:
        p = [219,683]
        screen.blit(card_arrow, p)
    if s.game.select_card.position == 5:
        p = [259,683]
        screen.blit(card_arrow, p)
    if s.game.select_card.position >= 6:
        p = [301,679]
        screen.blit(select_card, p)
    
    if s.game.select_card.position == 6:
        p = [411,679]
        screen.blit(cards, p)
    if s.game.select_card.position == 7:
        p = [480,679]
        screen.blit(cards, p)
    if s.game.select_card.position == 8:
        p = [550,679]
        screen.blit(cards, p)

    if s.game.tilt.status == True:
        tilt_position = [645,285]
        screen.blit(tilt, tilt_position)


    if s.game.select_card.position >= 6 and s.game.ball_count.position == 3:
        s.cancel_delayed(name="blink")
        blink([s,1,1])
    else:
        s.cancel_delayed(name="blink")
    
    if s.game.eb_play.status == True:
        ebs_position = [285,929]
        screen.blit(ebs, ebs_position)

    pygame.display.update()

def blink(args):
    dirty_rects = []
    s = args[0]
    b = args[1]
    sn = args[2]

    if b == 0:
        if sn == 1:
            p = [362,717]
            dirty_rects.append(screen.blit(select_now, p))
        pygame.display.update(dirty_rects)
    else:
        dirty_rects.append(screen.blit(bg_gi, (362,717), pygame.Rect(362,717,180,30)))
        pygame.display.update(dirty_rects)
    b = not b

    args = [s,b,sn]

    s.delay(name="blink", delay=0.1, handler=blink, param=args)

def eb_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]

    if s.game.extra_ball.position < 7:
        dirty_rects.append(screen.blit(bg_gi, (27,996), pygame.Rect(27,996,217,32)))
    if s.game.extra_ball.position < 14:
        dirty_rects.append(screen.blit(bg_gi, (252,996), pygame.Rect(252,996,217,32)))
    if s.game.extra_ball.position < 21:
        dirty_rects.append(screen.blit(bg_gi, (479,996), pygame.Rect(479,996,217,32)))
    pygame.display.update(dirty_rects)

    if num in [2,10,18,27,35,43]:
        if s.game.extra_ball.position < 7:
            p = [27,996]
            dirty_rects.append(screen.blit(exb, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [3,11,19,28,36,44]:
        if s.game.extra_ball.position < 14:
            p = [252,996]
            dirty_rects.append(screen.blit(exb, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [4,12,20,29,37,45]:
        if s.game.extra_ball.position < 21:
            p = [479,996]
            dirty_rects.append(screen.blit(exb, p))
            pygame.display.update(dirty_rects)
            return

def clear_odds(s, num):
    global screen

    dirty_rects = []

    if s.game.odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (183,789), pygame.Rect(183,789,29,97)))
    if s.game.odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (239,816), pygame.Rect(239,816,37,100)))
    if s.game.odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (284,787), pygame.Rect(284,787,30,110)))
    if s.game.odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (348,822), pygame.Rect(348,822,33,93)))
    if s.game.odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (396,790), pygame.Rect(396,790,42,96)))
    if s.game.odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (450,788), pygame.Rect(450,788,30,104)))
    if s.game.odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (497,844), pygame.Rect(497,844,35,98)))
    if s.game.odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (596,818), pygame.Rect(596,818,45,97)))
    
    pygame.display.update(dirty_rects)

def draw_odds_animation(s, num):
    global screen
    dirty_rects = []
    if num in [2,3,12,27,28,37]:
        if s.game.odds.position != 1:
            p = [183,789]
            dirty_rects.append(screen.blit(o1, p))
            pygame.display.update(dirty_rects)
            return
    if num in [13,14,38,39]:
        if s.game.odds.position != 2:
            p = [239,816]
            dirty_rects.append(screen.blit(o2, p))
            pygame.display.update(dirty_rects)
            return
    if num in [4,5,15,16,29,30,40,41]:
        if s.game.odds.position != 3:
            p = [284,787]
            dirty_rects.append(screen.blit(o3, p))
            pygame.display.update(dirty_rects)
            return
    if num in [17,18,42,43]:
        if s.game.odds.position != 4:
            p = [348,822]
            dirty_rects.append(screen.blit(o4, p))
            pygame.display.update(dirty_rects)
            return
    if num in [6,7,19,31,32,44]:
        if s.game.odds.position != 5:
            p = [396,790]
            dirty_rects.append(screen.blit(o5, p))
            pygame.display.update(dirty_rects)
            return
    if num in [20,21,45,46]:
        if s.game.odds.position != 6:
            p = [450,788]
            dirty_rects.append(screen.blit(o6, p))
            pygame.display.update(dirty_rects)
            return
    if num in [8,9,22,23,33,34,47,48]:
        if s.game.odds.position != 7:
            p = [497,844]
            dirty_rects.append(screen.blit(o7, p))
            pygame.display.update(dirty_rects)
            return
    if num in [0,25,50,10,35,1,26]:
        if s.game.odds.position != 8:
            p = [596,818]
            dirty_rects.append(screen.blit(o8, p))
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
    #stars, 3,4,5 cards and indicator arrows, super cards
    if s.game.yellow_star.status == False:
        dirty_rects.append(screen.blit(bg_gi, (22,684), pygame.Rect(22,684,66,68)))
    if s.game.red_star.status == False:
        dirty_rects.append(screen.blit(bg_gi, (633,683), pygame.Rect(633,683,66,68)))
    if s.game.select_card.position < 6:
        dirty_rects.append(screen.blit(bg_gi, (488,644), pygame.Rect(488,644,24,29)))
        dirty_rects.append(screen.blit(bg_gi, (411,679), pygame.Rect(411,679,67,34)))
    if s.game.select_card.position < 7:
        dirty_rects.append(screen.blit(bg_gi, (543,644), pygame.Rect(543,644,24,29)))
        dirty_rects.append(screen.blit(bg_gi, (480,679), pygame.Rect(480,679,67,34)))
    if s.game.select_card.position < 8:
        dirty_rects.append(screen.blit(bg_gi, (599,644), pygame.Rect(599,644,24,29)))
        dirty_rects.append(screen.blit(bg_gi, (550,679), pygame.Rect(550,679,67,34)))
    if s.game.super_card.position < 5:
        dirty_rects.append(screen.blit(bg_gi, (19,507), pygame.Rect(19,507,70,59)))
    if s.game.super_card.position < 10:
        dirty_rects.append(screen.blit(bg_gi, (635,404), pygame.Rect(635,404,71,60)))

    pygame.display.update(dirty_rects)


def draw_feature_animation(s, num):
    global screen
    dirty_rects = []
 
    if num in [2,3,16,17,27,28,41,42]:
        if s.game.yellow_star.status == False:
            p = [22,684]
            dirty_rects.append(screen.blit(star, p))
            s.game.coils.redROLamp.pulse(85)
            pygame.display.update(dirty_rects)
            return
    if num in [4,5,14,15,29,30,39,40]:
        if s.game.red_star.status == False:
            p = [633,683]
            dirty_rects.append(screen.blit(star, p))
            s.game.coils.yellowROLamp.pulse(85)
            pygame.display.update(dirty_rects)
            return
    if num in [6,7,18,19,31,32,43,44]:
        if s.game.select_card.position < 6:
            p = [488,644]
            dirty_rects.append(screen.blit(select, p))
            p = [411,679]
            dirty_rects.append(screen.blit(cards, p))
            pygame.display.update(dirty_rects)
            return
    if num in [8,9,20,21,33,34,45,46]:
        if s.game.select_card.position < 7:
            p = [543,644]
            dirty_rects.append(screen.blit(select, p))
            p = [480,679]
            dirty_rects.append(screen.blit(cards, p))
            pygame.display.update(dirty_rects)
            return
    if num in [10,11,22,23,35,36,47,48]:
        if s.game.select_card.position < 8:
            p = [599,644]
            dirty_rects.append(screen.blit(select, p))
            p = [550,679]
            dirty_rects.append(screen.blit(cards, p))
            pygame.display.update(dirty_rects)
            return
    if num in [1,10,16,24,26,35,41,49]:
        if s.game.super_card.position < 5:
            p = [19,507]
            dirty_rects.append(screen.blit(s1, p))
            pygame.display.update(dirty_rects)
            return
    if num in [3,12,17,28,37,42]:
        if s.game.super_card.position < 10:
            p = [635,404]
            dirty_rects.append(screen.blit(s2, p))
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


