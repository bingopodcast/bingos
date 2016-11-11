
import pygame

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

meter = pygame.image.load('graphics/assets/black_register_cover.png').convert()
card = pygame.image.load('bali/assets/card.png').convert_alpha()
feature = pygame.image.load('bali/assets/feature.png').convert_alpha()
eb_display = pygame.image.load('bali/assets/sixth_ball.png').convert_alpha()
number = pygame.image.load('bali/assets/number.png').convert_alpha()
corners = pygame.image.load('bali/assets/corners.png').convert_alpha()
c = pygame.image.load('bali/assets/regular.png').convert_alpha()
d = pygame.image.load('bali/assets/double.png').convert_alpha()
n = pygame.image.load('bali/assets/nothing.png').convert_alpha()
tilt = pygame.image.load('bali/assets/tilt.png').convert_alpha()
blink_image = pygame.image.load('bali/assets/double_or_nothing.png').convert_alpha()


class scorereel():
    """ Score Reels are used to count replays """
    def __init__(self, pos, image):
        self.position = pos
        self.default_y = self.position[1]
        self.image = pygame.image.load(image).convert()

reel1 = scorereel([381,698], "graphics/assets/white_reel.png")
reel10 = scorereel([363,698], "graphics/assets/white_reel.png")
reel100 = scorereel([344,698], "graphics/assets/white_reel.png")
reel1000 = scorereel([324,698], "graphics/assets/white_reel.png")

def display(s, replays=0, menu=False):
    
    meter.set_colorkey((255,0,252))
    meter_position = [315,698]

    screen.blit(reel1.image, reel1.position)
    screen.blit(reel10.image, reel10.position)
    screen.blit(reel100.image, reel100.position)
    screen.blit(reel1000.image, reel1000.position)
    screen.blit(meter, meter_position)

    backglass_position = [0, 0]
    backglass = pygame.Surface((0,0), pygame.SRCALPHA)
    backglass.fill((0, 0, 0))
    if menu == True:
        backglass = pygame.image.load('bali/assets/bali_menu.png')
    else:
        if (s.game.anti_cheat.status == True):
            backglass = pygame.image.load('bali/assets/bali_gi.png')
        else:
            backglass = pygame.image.load('bali/assets/bali_off.png')
    screen.blit(backglass, backglass_position)

    if s.game.selector.position >= 1:
        position = [350,365]
        screen.blit(card, position)
    if s.game.selector.position >= 1 and s.game.selector.position <= 3:
        position = [249,602]
        screen.blit(feature, position)
    if s.game.selector.position >= 2:
        position = [124,540]
        screen.blit(card, position)
    if s.game.selector.position >= 2 and s.game.selector.position <= 4:
        position = [24,778]
        screen.blit(feature, position)
    if s.game.selector.position >= 3:
        position = [577,542]
        screen.blit(card, position)
    if s.game.selector.position >= 3 and s.game.selector.position <= 5:
        position = [475,779]
        screen.blit(feature, position)
    if s.game.selector.position >= 4:
        position = [354,602]
        screen.blit(feature, position)
    if s.game.selector.position >= 5:
        position = [127,778]
        screen.blit(feature, position)
    if s.game.selector.position >= 6:
        position = [580,779]
        screen.blit(feature, position)
    if s.game.selector.position == 7:
        position = [268,882]
        screen.blit(eb_display, position)

    if s.game.tilt.status == False:
        if s.holes:
            if 1 in s.holes:
                position = [372,556]
                screen.blit(number, position)
                position = [112,606]
                screen.blit(number, position)
                position = [498,732]
                screen.blit(number, position)
            if 2 in s.holes:
                position = [405,494]
                screen.blit(number, position)
                position = [144,732]
                screen.blit(number, position)
                position = [498,638]
                screen.blit(number, position)
            if 3 in s.holes:
                position = [272,430]
                screen.blit(number, position)
                position = [112,638]
                screen.blit(number, position)
                position = [596,732]
                screen.blit(number, position)
            if 4 in s.holes:
                position = [372,430]
                screen.blit(number, position)
                position = [46,606]
                screen.blit(number, position)
                position = [629,608]
                screen.blit(number, position)
            if 5 in s.holes:
                position = [406,556]
                screen.blit(number, position)
                position = [177,606]
                screen.blit(number, position)
                position = [630,670]
                screen.blit(number, position)
            if 6 in s.holes:
                position = [274,556]
                screen.blit(number, position)
                position = [80,606]
                screen.blit(number, position)
                position = [628,732]
                screen.blit(number, position)
            if 7 in s.holes:
                position = [304,430]
                screen.blit(number, position)
                position = [44,730]
                screen.blit(number, position)
                position = [531,732]
                screen.blit(number, position)
            if 8 in s.holes:
                position = [404,461]
                screen.blit(number, position)
                position = [176,701]
                screen.blit(number, position)
                position = [498,607]
                screen.blit(number, position)
            if 9 in s.holes:
                position = [403,430]
                screen.blit(number, position)
                position = [45,668]
                screen.blit(number, position)
                position = [564,702]
                screen.blit(number, position)
            if 10 in s.holes:
                position = [338,430]
                screen.blit(number, position)
                position = [45,700]
                screen.blit(number, position)
                position = [564,608]
                screen.blit(number, position)
            if 11 in s.holes:
                position = [372,492]
                screen.blit(number, position)
                position = [177,732]
                screen.blit(number, position)
                position = [630,702]
                screen.blit(number, position)
            if 12 in s.holes:
                position = [338,526]
                screen.blit(number, position)
                position = [144,669]
                screen.blit(number, position)
                position = [530,670]
                screen.blit(number, position)
            if 13 in s.holes:
                position = [273,525]
                screen.blit(number, position)
                position = [176,638]
                screen.blit(number, position)
                position = [597,607]
                screen.blit(number, position)
            if 14 in s.holes:
                position = [306,494]
                screen.blit(number, position)
                position = [144,702]
                screen.blit(number, position)
                position = [598,638]
                screen.blit(number, position)
            if 15 in s.holes:
                position = [272,492]
                screen.blit(number, position)
                position = [79,638]
                screen.blit(number, position)
                position = [532,702]
                screen.blit(number, position)
            if 16 in s.holes:
                position = [338,558]
                screen.blit(number, position)
                position = [112,700]
                screen.blit(number, position)
                position = [564,639]
                screen.blit(number, position)
            if 17 in s.holes:
                position = [340,494]
                screen.blit(number, position)
                position = [144,638]
                screen.blit(number, position)
                position = [532,638]
                screen.blit(number, position)
            if 18 in s.holes:
                position = [340,460]
                screen.blit(number, position)
                position = [79,700]
                screen.blit(number, position)
                position = [598,702]
                screen.blit(number, position)
            if 19 in s.holes:
                position = [371,525]
                screen.blit(number, position)
                position = [78,669]
                screen.blit(number, position)
                position = [598,670]
                screen.blit(number, position)
            if 20 in s.holes:
                position = [306,525]
                screen.blit(number, position)
                position = [177,670]
                screen.blit(number, position)
                position = [498,671]
                screen.blit(number, position)
            if 21 in s.holes:
                position = [306,461]
                screen.blit(number, position)
                position = [112,670]
                screen.blit(number, position)
                position = [564,732]
                screen.blit(number, position)
            if 22 in s.holes:
                position = [372,462]
                screen.blit(number, position)
                position = [112,731]
                screen.blit(number, position)
                position = [564,671]
                screen.blit(number, position)
            if 23 in s.holes:
                position = [404,525]
                screen.blit(number, position)
                position = [144,606]
                screen.blit(number, position)
                position = [532,608]
                screen.blit(number, position)
            if 24 in s.holes:
                position = [272,461]
                screen.blit(number, position)
                position = [79,732]
                screen.blit(number, position)
                position = [630,640]
                screen.blit(number, position)
            if 25 in s.holes:
                position = [306,556]
                screen.blit(number, position)
                position = [46,638]
                screen.blit(number, position)
                position = [498,702]
                screen.blit(number, position)

        if s.game.corners1.status == True:
            position = [246,362]
            screen.blit(corners, position)
        if s.game.corners2.status == True:
            position = [19,539]
            screen.blit(corners, position)
        if s.game.corners3.status == True:
            position = [472,542]
            screen.blit(corners, position)

        if s.game.card1_replay_counter.position > 0 or s.game.card2_replay_counter.position > 0 or s.game.card3_replay_counter.position > 0:
            if s.game.card1_replay_counter.position > 0 and s.game.card1_double.status == False:
                position = [304,377]
                screen.blit(c, position)
            if s.game.card2_replay_counter.position > 0 and s.game.card2_double.status == False:
                position = [78,554]
                screen.blit(c, position)
            if s.game.card3_replay_counter.position > 0 and s.game.card3_double.status == False:
                position = [530,555]
                screen.blit(c, position)

        if s.game.card1_double.status == True:
            position = [354,402]
            screen.blit(d, position)
        if s.game.card2_double.status == True:
            position = [128,577]
            screen.blit(d, position)
        if s.game.card3_double.status == True:
            position = [580,579]
            screen.blit(d, position)

        if s.game.card1_missed.status == True:
            position = [408,402]
            screen.blit(n, position)
        if s.game.card2_missed.status == True:
            position = [182,577]
            screen.blit(n, position)
        if s.game.card3_missed.status == True:
            position = [633,580]
            screen.blit(n, position)

    if s.game.tilt.status == True:
        position = [600,923]
        screen.blit(tilt, position)

    pygame.display.update()

def blink_double(s):
    s.game.blink = not s.game.blink
    if s.game.blink == 1:
        blink_pos = [518,394]
        screen.blit(blink_image, blink_pos)
        pygame.display.update()
    else:
        display(s)
