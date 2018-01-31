
import pygame, random

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

meter = pygame.image.load('graphics/assets/white_register_cover.png').convert()
card = pygame.image.load('venus/assets/card.png').convert_alpha()
number = pygame.image.load('venus/assets/number.png').convert_alpha()
tilt = pygame.image.load('venus/assets/tilt.png').convert_alpha()
green_button = pygame.image.load('venus/assets/green_button.png').convert_alpha()
green_button_info = pygame.image.load('venus/assets/green_button_info.png').convert_alpha()
red_button = pygame.image.load('venus/assets/red_button.png').convert_alpha()
double = pygame.image.load('venus/assets/double.png').convert_alpha()
nothing = pygame.image.load('venus/assets/nothing.png').convert_alpha()
feature = pygame.image.load('venus/assets/feature.png').convert_alpha()
bg_menu = pygame.image.load('venus/assets/venus_menu.png')
bg_gi = pygame.image.load('venus/assets/venus_gi.png')
bg_off = pygame.image.load('venus/assets/venus_off.png')

class scorereel():
    """ Score Reels are used to count replays """
    def __init__(self, pos, image):
        self.position = pos
        self.default_y = self.position[1]
        self.image = pygame.image.load(image).convert()

reel1 = scorereel([586,310], "graphics/assets/white_reel.png")
reel10 = scorereel([566,310], "graphics/assets/white_reel.png")
reel100 = scorereel([548,310], "graphics/assets/white_reel.png")
reel1000 = scorereel([529,310], "graphics/assets/white_reel.png")

def display(s, replays=0, menu=False):
    
    meter.set_colorkey((255,0,252))
    meter_position = [506,310]

    screen.blit(reel1.image, reel1.position)
    screen.blit(reel10.image, reel10.position)
    screen.blit(reel100.image, reel100.position)
    screen.blit(reel1000.image, reel1000.position)
    screen.blit(meter, meter_position)

    backglass_position = [0, 0]
    backglass = pygame.Surface((0,0), pygame.SRCALPHA)
    backglass.fill((0, 0, 0))
    if menu == True:
        screen.blit(bg_menu, backglass_position)
    else:
        if (s.game.anti_cheat.status == True):
            screen.blit(bg_gi, backglass_position)
        else:
            screen.blit(bg_off, backglass_position)

    if s.game.selector.position >= 1:
        card1_position = [16,673]
        screen.blit(card, card1_position)
    if s.game.selector.position >= 2:
        card2_position = [289,673]
        screen.blit(card, card2_position)
    if s.game.selector.position >= 3:
        card3_position = [562,677]
        screen.blit(card, card3_position)
    if s.game.selector.position >= 4:
        card4_position = [16,965]
        screen.blit(card, card4_position)
    if s.game.selector.position >= 5:
        card5_position = [287,965]
        screen.blit(card, card5_position)
    if s.game.selector.position >= 6:
        card6_position = [557,967]
        screen.blit(card, card6_position)

    if s.game.search_index.status == True:
        if s.game.double_win.status == True:
            f = [257,324]
            screen.blit(feature, f)
            d = [295,325]
            screen.blit(double, d)
        if s.game.nothing.status == True:
            print "HERE"
            f = [255,366]
            screen.blit(feature, f)
            n = [280,367]
            screen.blit(nothing, n)


    if s.game.tilt.status == False:
        if s.holes:
            if 1 in s.holes:
                #number_position = [62,469]
                number_position = [65,465]
                screen.blit(number, number_position)
                number_position = [255,595]
                screen.blit(number, number_position)
                number_position = [610,640]
                screen.blit(number, number_position)
                number_position = [186,752]
                screen.blit(number, number_position)
                number_position = [254,926]
                screen.blit(number, number_position)
                number_position = [568,755]
                screen.blit(number, number_position)
            if 2 in s.holes:
                number_position = [106,636]
                screen.blit(number, number_position)
                number_position = [257,552]
                screen.blit(number, number_position)
                number_position = [651,555]
                screen.blit(number, number_position)
                number_position = [186,796]
                screen.blit(number, number_position)
                number_position = [254,796]
                screen.blit(number, number_position)
                number_position = [606,931]
                screen.blit(number, number_position)

            if 3 in s.holes:
                number_position = [188,465]
                screen.blit(number, number_position)
                number_position = [419,639]
                screen.blit(number, number_position)
                number_position = [488,467]
                screen.blit(number, number_position)
                number_position = [105,752]
                screen.blit(number, number_position)
                number_position = [378,928]
                screen.blit(number, number_position)
                number_position = [567,798]
                screen.blit(number, number_position)

            if 4 in s.holes:
                number_position = [147,637]
                screen.blit(number, number_position)
                number_position = [382,466]
                screen.blit(number, number_position)
                number_position = [612,468]
                screen.blit(number, number_position)
                number_position = [145,926]
                screen.blit(number, number_position)
                number_position = [418,754]
                screen.blit(number, number_position)
                number_position = [485,755]
                screen.blit(number, number_position)
            if 5 in s.holes:
                number_position = [26,466]
                screen.blit(number, number_position)
                number_position = [339,638]
                screen.blit(number, number_position)
                number_position = [649,641]
                screen.blit(number, number_position)
                number_position = [22,838]
                screen.blit(number, number_position)
                number_position = [418,841]
                screen.blit(number, number_position)
                number_position = [647,757]
                screen.blit(number, number_position)
            if 6 in s.holes:
                number_position = [24,552]
                screen.blit(number, number_position)
                number_position = [421,466]
                screen.blit(number, number_position)
                number_position = [487,640]
                screen.blit(number, number_position)
                number_position = [22,753]
                screen.blit(number, number_position)
                number_position = [417,930]
                screen.blit(number, number_position)
                number_position = [526,755]
                screen.blit(number, number_position)

            if 7 in s.holes:
                number_position = [189,508]
                screen.blit(number, number_position)
                number_position = [297,639]
                screen.blit(number, number_position)
                number_position = [529,467]
                screen.blit(number, number_position)
                number_position = [64,751]
                screen.blit(number, number_position)
                number_position = [295,928]
                screen.blit(number, number_position)
                number_position = [482,928]
                screen.blit(number, number_position)

            if 8 in s.holes:
                number_position = [25,509]
                screen.blit(number, number_position)
                number_position = [419,597]
                screen.blit(number, number_position)
                number_position = [651,513]
                screen.blit(number, number_position)
                number_position = [186,926]
                screen.blit(number, number_position)
                number_position = [255,754]
                screen.blit(number, number_position)
                number_position = [646,887]
                screen.blit(number, number_position)

            if 9 in s.holes:
                number_position = [108,466]
                screen.blit(number, number_position)
                number_position = [259,466]
                screen.blit(number, number_position)
                number_position = [652,468]
                screen.blit(number, number_position)
                number_position = [105,883]
                screen.blit(number, number_position)
                number_position = [336,884]
                screen.blit(number, number_position)
                number_position = [484,841]
                screen.blit(number, number_position)

            if 10 in s.holes:
                number_position = [107,508]
                screen.blit(number, number_position)
                number_position = [256,638]
                screen.blit(number, number_position)
                number_position = [571,468]
                screen.blit(number, number_position)
                number_position = [23,926]
                screen.blit(number, number_position)
                number_position = [337,753]
                screen.blit(number, number_position)
                number_position = [484,884]
                screen.blit(number, number_position)

            if 11 in s.holes:
                number_position = [148,553]
                screen.blit(number, number_position)
                number_position = [338,595]
                screen.blit(number, number_position)
                number_position = [611,555]
                screen.blit(number, number_position)
                number_position = [22,882]
                screen.blit(number, number_position)
                number_position = [417,885]
                screen.blit(number, number_position)
                number_position = [647,930]
                screen.blit(number, number_position)

            if 12 in s.holes:
                number_position = [24,638]
                screen.blit(number, number_position)
                number_position = [381,552]
                screen.blit(number, number_position)
                number_position = [570,597]
                screen.blit(number, number_position)
                number_position = [105,795]
                screen.blit(number, number_position)
                number_position = [296,841]
                screen.blit(number, number_position)
                number_position = [607,843]
                screen.blit(number, number_position)

            if 13 in s.holes:
                number_position = [188,594]
                screen.blit(number, number_position)
                number_position = [257,508]
                screen.blit(number, number_position)
                number_position = [488,596]
                screen.blit(number, number_position)
                number_position = [64,924]
                screen.blit(number, number_position)
                number_position = [378,753]
                screen.blit(number, number_position)
                number_position = [647,799]
                screen.blit(number, number_position)

            if 14 in s.holes:
                number_position = [107,595]
                screen.blit(number, number_position)
                number_position = [339,509]
                screen.blit(number, number_position)
                number_position = [529,554]
                screen.blit(number, number_position)
                number_position = [64,795]
                screen.blit(number, number_position)
                number_position = [378,797]
                screen.blit(number, number_position)
                number_position = [606,887]
                screen.blit(number, number_position)

            if 15 in s.holes:
                number_position = [188,638]
                screen.blit(number, number_position)
                number_position = [340,552]
                screen.blit(number, number_position)
                number_position = [486,554]
                screen.blit(number, number_position)
                number_position = [145,881]
                screen.blit(number, number_position)
                number_position = [295,884]
                screen.blit(number, number_position)
                number_position = [527,798]
                screen.blit(number, number_position)

            if 16 in s.holes:
                number_position = [108,552]
                screen.blit(number, number_position)
                number_position = [341,466]
                screen.blit(number, number_position)
                number_position = [569,639]
                screen.blit(number, number_position)
                number_position = [146,839]
                screen.blit(number, number_position)
                number_position = [337,797]
                screen.blit(number, number_position)
                number_position = [566,886]
                screen.blit(number, number_position)

            if 17 in s.holes:
                number_position = [189,551]
                screen.blit(number, number_position)
                number_position = [422,553]
                screen.blit(number, number_position)
                number_position = [571,555]
                screen.blit(number, number_position)
                number_position = [64,883]
                screen.blit(number, number_position)
                number_position = [297,796]
                screen.blit(number, number_position)
                number_position = [608,799]
                screen.blit(number, number_position)

            if 18 in s.holes:
                number_position = [66,552]
                screen.blit(number, number_position)
                number_position = [298,553]
                screen.blit(number, number_position)
                number_position = [570,512]
                screen.blit(number, number_position)
                number_position = [146,796]
                screen.blit(number, number_position)
                number_position = [378,884]
                screen.blit(number, number_position)
                number_position = [526,886]
                screen.blit(number, number_position)

            if 19 in s.holes:
                number_position = [149,508]
                screen.blit(number, number_position)
                number_position = [299,510]
                screen.blit(number, number_position)
                number_position = [611,597]
                screen.blit(number, number_position)
                number_position = [64,839]
                screen.blit(number, number_position)
                number_position = [378,841]
                screen.blit(number, number_position)
                number_position = [526,842]
                screen.blit(number, number_position)

            if 20 in s.holes:
                number_position = [148,594]
                screen.blit(number, number_position)
                number_position = [381,509]
                screen.blit(number, number_position)
                number_position = [530,597]
                screen.blit(number, number_position)
                number_position = [105,839]
                screen.blit(number, number_position)
                number_position = [254,839]
                screen.blit(number, number_position)
                number_position = [646,843]
                screen.blit(number, number_position)

            if 21 in s.holes:
                number_position = [66,594]
                screen.blit(number, number_position)
                number_position = [381,595]
                screen.blit(number, number_position)
                number_position = [531,510]
                screen.blit(number, number_position)
                number_position = [105,926]
                screen.blit(number, number_position)
                number_position = [336,928]
                screen.blit(number, number_position)
                number_position = [566,841]
                screen.blit(number, number_position)

            if 22 in s.holes:
                number_position = [67,509]
                screen.blit(number, number_position)
                number_position = [298,595]
                screen.blit(number, number_position)
                number_position = [611,512]
                screen.blit(number, number_position)
                number_position = [187,839]
                screen.blit(number, number_position)
                number_position = [337,841]
                screen.blit(number, number_position)
                number_position = [567,930]
                screen.blit(number, number_position)

            if 23 in s.holes:
                number_position = [67,637]
                screen.blit(number, number_position)
                number_position = [379,638]
                screen.blit(number, number_position)
                number_position = [651,598]
                screen.blit(number, number_position)
                number_position = [22,794]
                screen.blit(number, number_position)
                number_position = [297,753]
                screen.blit(number, number_position)
                number_position = [608,756]
                screen.blit(number, number_position)

            if 24 in s.holes:
                number_position = [25,594]
                screen.blit(number, number_position)
                number_position = [299,466]
                screen.blit(number, number_position)
                number_position = [488,510]
                screen.blit(number, number_position)
                number_position = [146,752]
                screen.blit(number, number_position)
                number_position = [418,798]
                screen.blit(number, number_position)
                number_position = [526,930]
                screen.blit(number, number_position)

            if 25 in s.holes:
                number_position = [149,464]
                screen.blit(number, number_position)
                number_position = [420,510]
                screen.blit(number, number_position)
                number_position = [529,639]
                screen.blit(number, number_position)
                number_position = [186,883]
                screen.blit(number, number_position)
                number_position = [255,883]
                screen.blit(number, number_position)
                number_position = [485,798]
                screen.blit(number, number_position)


    if s.game.tilt.status == True:
        tilt_position = [330,405]
        screen.blit(tilt, tilt_position)

    pygame.display.update()


def blink_double(s):
    dirty_rects = []
    s.game.blink = not s.game.blink
    if s.game.blink == 1:
        blink_pos = [251,234]
        dirty_rects.append(screen.blit(green_button, blink_pos))
        b = [277,236]
        dirty_rects.append(screen.blit(green_button_info, b))
        r = [256,280]
        dirty_rects.append(screen.blit(feature, r))
        b = [271,284]
        dirty_rects.append(screen.blit(red_button, b))
        pygame.display.update(dirty_rects)
    else:
        dirty_rects.append(screen.blit(bg_gi, (251,234), pygame.Rect(251,234,218,54)))
        dirty_rects.append(screen.blit(bg_gi, (277,236), pygame.Rect(277,236,162,43)))
        dirty_rects.append(screen.blit(bg_gi, (256,280), pygame.Rect(256,280,207,50)))
        dirty_rects.append(screen.blit(bg_gi, (271,284), pygame.Rect(271,284,176,42)))
        pygame.display.update(dirty_rects)

