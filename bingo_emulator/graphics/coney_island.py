import pygame
import random

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

meter = pygame.image.load('graphics/assets/register_cover.png').convert()
card = pygame.image.load('coney_island/assets/card.png').convert_alpha()
number = pygame.image.load('coney_island/assets/number.png').convert_alpha()
extra_ball = pygame.image.load('coney_island/assets/extra_balls.png').convert_alpha()
eb = pygame.image.load('coney_island/assets/extra_ball.png').convert_alpha()
tilt = pygame.image.load('coney_island/assets/tilt.png').convert_alpha()
bg_menu = pygame.image.load('coney_island/assets/coney_island_menu.png')
bg_gi = pygame.image.load('coney_island/assets/coney_island_gi.png')
bg_off = pygame.image.load('coney_island/assets/coney_island_off.png')

class scorereel():
    """ Score Reels are used to count replays """
    def __init__(self, pos, image):
        self.position = pos
        self.default_y = self.position[1]
        self.image = pygame.image.load(image).convert()

reel1 = scorereel([630,398], "graphics/assets/green_reel.png")
reel10 = scorereel([611,398], "graphics/assets/green_reel.png")
reel100 = scorereel([592,398], "graphics/assets/green_reel.png")

def display(s, replays=0, menu=False):


    meter.set_colorkey((255,0,252))
    meter_position = [582,398]

    screen.blit(reel1.image, reel1.position)
    screen.blit(reel10.image, reel10.position)
    screen.blit(reel100.image, reel100.position)
    screen.blit(meter, meter_position)

    backglass_position = [0, 0]
    if menu == True:
        screen.blit(bg_menu, backglass_position)
    else:
        if (s.game.anti_cheat.status == True):
            screen.blit(bg_gi, backglass_position)
        else:
            screen.blit(bg_off, backglass_position)
    

    if s.game.selector.position >= 1:
        card1_position = [52,906]
        screen.blit(card, card1_position)
    if s.game.selector.position >= 2:
        card2_position = [278,674]
        screen.blit(card, card2_position)
    if s.game.selector.position >= 3:
        card3_position = [503,906]
        screen.blit(card, card3_position)
 
    if s.game.tilt.status == False:
        if s.holes:
            if 1 in s.holes:
                number_position = [76,688]
                screen.blit(number, number_position)
                number_position = [260,580]
                screen.blit(number, number_position)
                number_position = [608,852]
                screen.blit(number, number_position)
            if 2 in s.holes:
                number_position = [116,851]
                screen.blit(number, number_position)
                number_position = [258,540]
                screen.blit(number, number_position)
                number_position = [650,772]
                screen.blit(number, number_position)
            if 3 in s.holes:
                number_position = [198,689]
                screen.blit(number, number_position)
                number_position = [425,620]
                screen.blit(number, number_position)
                number_position = [484,689]
                screen.blit(number, number_position)
            if 4 in s.holes:
                number_position = [158,851]
                screen.blit(number, number_position)
                number_position = [382,458]
                screen.blit(number, number_position)
                number_position = [608,689]
                screen.blit(number, number_position)
            if 5 in s.holes:
                number_position = [34,689]
                screen.blit(number, number_position)
                number_position = [342,623]
                screen.blit(number, number_position)
                number_position = [648,854]
                screen.blit(number, number_position)
            if 6 in s.holes:
                number_position = [32,768]
                screen.blit(number, number_position)
                number_position = [424,456]
                screen.blit(number, number_position)
                number_position = [484,854]
                screen.blit(number, number_position)
            if 7 in s.holes:
                number_position = [198,730]
                screen.blit(number, number_position)
                number_position = [300,620]
                screen.blit(number, number_position)
                number_position = [524,689]
                screen.blit(number, number_position)
            if 8 in s.holes:
                number_position = [34,731]
                screen.blit(number, number_position)
                number_position = [425,581]
                screen.blit(number, number_position)
                number_position = [650,731]
                screen.blit(number, number_position)
            if 9 in s.holes:
                number_position = [116,688]
                screen.blit(number, number_position)
                number_position = [258,458]
                screen.blit(number, number_position)
                number_position = [648,689]
                screen.blit(number, number_position)
            if 10 in s.holes:
                number_position = [116,730]
                screen.blit(number, number_position)
                number_position = [258,622]
                screen.blit(number, number_position)
                number_position = [566,689]
                screen.blit(number, number_position)
            if 11 in s.holes:
                number_position = [160,770]
                screen.blit(number, number_position)
                number_position = [342,581]
                screen.blit(number, number_position)
                number_position = [608,772]
                screen.blit(number, number_position)
            if 12 in s.holes:
                number_position = [35,852]
                screen.blit(number, number_position)
                number_position = [383,539]
                screen.blit(number, number_position)
                number_position = [566,812]
                screen.blit(number, number_position)
            if 13 in s.holes:
                number_position = [202,812]
                screen.blit(number, number_position)
                number_position = [258,500]
                screen.blit(number, number_position)
                number_position = [485,812]
                screen.blit(number, number_position)
            if 14 in s.holes:
                number_position = [116,812]
                screen.blit(number, number_position)
                number_position = [341,498]
                screen.blit(number, number_position)
                number_position = [526,772]
                screen.blit(number, number_position)
            if 15 in s.holes:
                number_position = [200,852]
                screen.blit(number, number_position)
                number_position = [342,539]
                screen.blit(number, number_position)
                number_position = [484,773]
                screen.blit(number, number_position)
            if 16 in s.holes:
                number_position = [116,771]
                screen.blit(number, number_position)
                number_position = [341,456]
                screen.blit(number, number_position)
                number_position = [568,852]
                screen.blit(number, number_position)
            if 17 in s.holes:
                number_position = [200,770]
                screen.blit(number, number_position)
                number_position = [425,540]
                screen.blit(number, number_position)
                number_position = [566,770]
                screen.blit(number, number_position)
            if 18 in s.holes:
                number_position = [76,772]
                screen.blit(number, number_position)
                number_position = [302,539]
                screen.blit(number, number_position)
                number_position = [566,731]
                screen.blit(number, number_position)
            if 19 in s.holes:
                number_position = [158,731]
                screen.blit(number, number_position)
                number_position = [298,497]
                screen.blit(number, number_position)
                number_position = [606,812]
                screen.blit(number, number_position)
            if 20 in s.holes:
                number_position = [158,809]
                screen.blit(number, number_position)
                number_position = [383,498]
                screen.blit(number, number_position)
                number_position = [524,814]
                screen.blit(number, number_position)
            if 21 in s.holes:
                number_position = [76,810]
                screen.blit(number, number_position)
                number_position = [383,578]
                screen.blit(number, number_position)
                number_position = [524,731]
                screen.blit(number, number_position)
            if 22 in s.holes:
                number_position = [76,730]
                screen.blit(number, number_position)
                number_position = [300,578]
                screen.blit(number, number_position)
                number_position = [608,731]
                screen.blit(number, number_position)
            if 23 in s.holes:
                number_position = [76,850]
                screen.blit(number, number_position)
                number_position = [384,618]
                screen.blit(number, number_position)
                number_position = [650,810]
                screen.blit(number, number_position)
            if 24 in s.holes:
                number_position = [34,812]
                screen.blit(number, number_position)
                number_position = [299,456]
                screen.blit(number, number_position)
                number_position = [482,730]
                screen.blit(number, number_position)
            if 25 in s.holes:
                number_position = [156,688]
                screen.blit(number, number_position)
                number_position = [424,500]
                screen.blit(number, number_position)
                number_position = [526,854]
                screen.blit(number, number_position)


    if (s.game.eb_play.status == True):
        extra_ball_position = [302,845]
        screen.blit(extra_ball, extra_ball_position)

    if s.game.extra_ball.position >= 1:
        eb1_position = [259,882]
        screen.blit(eb, eb1_position)

    if s.game.extra_ball.position >= 2:
        eb2_position = [336,881]
        screen.blit(eb, eb2_position)

    if s.game.extra_ball.position >= 3:
        eb3_position = [409,882]
        screen.blit(eb, eb3_position)

    if s.game.tilt.status == True:
        tilt_position = [26,327]
        screen.blit(tilt, tilt_position)

    pygame.display.update()

def eb_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]

    if s.game.extra_ball.position < 1:
        dirty_rects.append(screen.blit(bg_gi, (259,882), pygame.Rect(259,882,61,65)))
    if s.game.extra_ball.position < 2:
        dirty_rects.append(screen.blit(bg_gi, (336,881), pygame.Rect(336,881,61,65)))
    if s.game.extra_ball.position < 3:
        dirty_rects.append(screen.blit(bg_gi, (409,882), pygame.Rect(409,882,61,65)))
    pygame.display.update(dirty_rects)

    if num in [0,1,6,7,12,13,18,19,26,27,32,33,38,39,44,45]:
        if s.game.extra_ball.position < 1:
            p = [259,882]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [2,3,8,9,14,15,20,21,28,29,34,35,40,41,46,47]:
        if s.game.extra_ball.position < 2:
            p = [336,881]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [4,5,10,11,16,17,22,23,24,30,31,36,37,42,43,48,49,50]:
        if s.game.extra_ball.position < 3:
            p = [409,882]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return

