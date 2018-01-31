
import pygame, random

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

meter = pygame.image.load('graphics/assets/register_cover.png').convert()
card = pygame.image.load('bright_lights/assets/card.png').convert_alpha()
number = pygame.image.load('bright_lights/assets/number.png').convert_alpha()
tilt = pygame.image.load('bright_lights/assets/tilt.png').convert_alpha()
bg_menu = pygame.image.load('bright_lights/assets/bright_lights_menu.png')
bg_gi = pygame.image.load('bright_lights/assets/bright_lights_gi.png')
bg_off = pygame.image.load('bright_lights/assets/bright_lights_off.png')

class scorereel():
    """ Score Reels are used to count replays """
    def __init__(self, pos, image):
        self.position = pos
        self.default_y = self.position[1]
        self.image = pygame.image.load(image).convert()

reel1 = scorereel([634,375], "graphics/assets/green_reel.png")
reel10 = scorereel([615,375], "graphics/assets/green_reel.png")
reel100 = scorereel([597,375], "graphics/assets/green_reel.png")

def display(s, replays=0, menu=False):
    
    meter.set_colorkey((255,0,252))
    meter_position = [587,375]

    screen.blit(reel1.image, reel1.position)
    screen.blit(reel10.image, reel10.position)
    screen.blit(reel100.image, reel100.position)
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
        card1_position = [69,692]
        screen.blit(card, card1_position)
    if s.game.selector.position >= 2:
        card2_position = [298,692]
        screen.blit(card, card2_position)
    if s.game.selector.position >= 3:
        card3_position = [525,692]
        screen.blit(card, card3_position)
    if s.game.selector.position >= 4:
        card4_position = [69,937]
        screen.blit(card, card4_position)
    if s.game.selector.position >= 5:
        card5_position = [298,937]
        screen.blit(card, card5_position)
    if s.game.selector.position >= 6:
        card6_position = [525,937]
        screen.blit(card, card6_position)

    if s.game.tilt.status == False:
        if s.holes:
            if 1 in s.holes:
                number_position = [75,514]
                screen.blit(number, number_position)
                number_position = [277,619]
                screen.blit(number, number_position)
                number_position = [606,645]
                screen.blit(number, number_position)
                number_position = [171,749]
                screen.blit(number, number_position)
                number_position = [278,898]
                screen.blit(number, number_position)
                number_position = [564,752]
                screen.blit(number, number_position)
            if 2 in s.holes:
                number_position = [116,650]
                screen.blit(number, number_position)
                number_position = [274,585]
                screen.blit(number, number_position)
                number_position = [634,573]
                screen.blit(number, number_position)
                number_position = [175,783]
                screen.blit(number, number_position)
                number_position = [271,794]
                screen.blit(number, number_position)
                number_position = [607,887]
                screen.blit(number, number_position)

            if 3 in s.holes:
                number_position = [173,506]
                screen.blit(number, number_position)
                number_position = [410,641]
                screen.blit(number, number_position)
                number_position = [498,513]
                screen.blit(number, number_position)
                number_position = [106,756]
                screen.blit(number, number_position)
                number_position = [378,890]
                screen.blit(number, number_position)
                number_position = [568,788]
                screen.blit(number, number_position)

            if 4 in s.holes:
                number_position = [150,646]
                screen.blit(number, number_position)
                number_position = [369,508]
                screen.blit(number, number_position)
                number_position = [596,507]
                screen.blit(number, number_position)
                number_position = [149,890]
                screen.blit(number, number_position)
                number_position = [402,748]
                screen.blit(number, number_position)
                number_position = [498,758]
                screen.blit(number, number_position)
            if 5 in s.holes:
                number_position = [40,516]
                screen.blit(number, number_position)
                number_position = [344,647]
                screen.blit(number, number_position)
                number_position = [639,642]
                screen.blit(number, number_position)
                number_position = [46,830]
                screen.blit(number, number_position)
                number_position = [406,818]
                screen.blit(number, number_position)
                number_position = [628,748]
                screen.blit(number, number_position)
            if 6 in s.holes:
                number_position = [46,586]
                screen.blit(number, number_position)
                number_position = [402,503]
                screen.blit(number, number_position)
                number_position = [509,652]
                screen.blit(number, number_position)
                number_position = [40,760]
                screen.blit(number, number_position)
                number_position = [411,886]
                screen.blit(number, number_position)
                number_position = [531,756]
                screen.blit(number, number_position)

            if 7 in s.holes:
                number_position = [174,540]
                screen.blit(number, number_position)
                number_position = [310,650]
                screen.blit(number, number_position)
                number_position = [530,512]
                screen.blit(number, number_position)
                number_position = [72,758]
                screen.blit(number, number_position)
                number_position = [312,894]
                screen.blit(number, number_position)
                number_position = [506,896]
                screen.blit(number, number_position)

            if 8 in s.holes:
                number_position = [44,550]
                screen.blit(number, number_position)
                number_position = [409,609]
                screen.blit(number, number_position)
                number_position = [632,538]
                screen.blit(number, number_position)
                number_position = [182,888]
                screen.blit(number, number_position)
                number_position = [268,760]
                screen.blit(number, number_position)
                number_position = [638,852]
                screen.blit(number, number_position)

            if 9 in s.holes:
                number_position = [107,510]
                screen.blit(number, number_position)
                number_position = [269,514]
                screen.blit(number, number_position)
                number_position = [628,504]
                screen.blit(number, number_position)
                number_position = [114,858]
                screen.blit(number, number_position)
                number_position = [343,857]
                screen.blit(number, number_position)
                number_position = [503,826]
                screen.blit(number, number_position)

            if 10 in s.holes:
                number_position = [111,546]
                screen.blit(number, number_position)
                number_position = [280,653]
                screen.blit(number, number_position)
                number_position = [564,510]
                screen.blit(number, number_position)
                number_position = [50,898]
                screen.blit(number, number_position)
                number_position = [336,753]
                screen.blit(number, number_position)
                number_position = [505,861]
                screen.blit(number, number_position)

            if 11 in s.holes:
                number_position = [144,578]
                screen.blit(number, number_position)
                number_position = [344,612]
                screen.blit(number, number_position)
                number_position = [603,576]
                screen.blit(number, number_position)
                number_position = [48,864]
                screen.blit(number, number_position)
                number_position = [409,852]
                screen.blit(number, number_position)
                number_position = [640,884]
                screen.blit(number, number_position)

            if 12 in s.holes:
                number_position = [51,654]
                screen.blit(number, number_position)
                number_position = [374,575]
                screen.blit(number, number_position)
                number_position = [572,612]
                screen.blit(number, number_position)
                number_position = [110,789]
                screen.blit(number, number_position)
                number_position = [308,826]
                screen.blit(number, number_position)
                number_position = [604,818]
                screen.blit(number, number_position)

            if 13 in s.holes:
                number_position = [182,609]
                screen.blit(number, number_position)
                number_position = [272,550]
                screen.blit(number, number_position)
                number_position = [506,616]
                screen.blit(number, number_position)
                number_position = [84,894]
                screen.blit(number, number_position)
                number_position = [368,750]
                screen.blit(number, number_position)
                number_position = [632,780]
                screen.blit(number, number_position)

            if 14 in s.holes:
                number_position = [114,614]
                screen.blit(number, number_position)
                number_position = [340,544]
                screen.blit(number, number_position)
                number_position = [538,581]
                screen.blit(number, number_position)
                number_position = [76,791]
                screen.blit(number, number_position)
                number_position = [372,786]
                screen.blit(number, number_position)
                number_position = [606,853]
                screen.blit(number, number_position)

            if 15 in s.holes:
                number_position = [184,642]
                screen.blit(number, number_position)
                number_position = [342,579]
                screen.blit(number, number_position)
                number_position = [503,583]
                screen.blit(number, number_position)
                number_position = [147,855]
                screen.blit(number, number_position)
                number_position = [311,860]
                screen.blit(number, number_position)
                number_position = [534,790]
                screen.blit(number, number_position)

            if 16 in s.holes:
                number_position = [113,580]
                screen.blit(number, number_position)
                number_position = [337,508]
                screen.blit(number, number_position)
                number_position = [576,646]
                screen.blit(number, number_position)
                number_position = [146,820]
                screen.blit(number, number_position)
                number_position = [339,788]
                screen.blit(number, number_position)
                number_position = [573,856]
                screen.blit(number, number_position)

            if 17 in s.holes:
                number_position = [178,574]
                screen.blit(number, number_position)
                number_position = [408,574]
                screen.blit(number, number_position)
                number_position = [570,578]
                screen.blit(number, number_position)
                number_position = [80,862]
                screen.blit(number, number_position)
                number_position = [305,790]
                screen.blit(number, number_position)
                number_position = [600,784]
                screen.blit(number, number_position)

            if 18 in s.holes:
                number_position = [80,582]
                screen.blit(number, number_position)
                number_position = [308,581]
                screen.blit(number, number_position)
                number_position = [568,544]
                screen.blit(number, number_position)
                number_position = [142,786]
                screen.blit(number, number_position)
                number_position = [376,855]
                screen.blit(number, number_position)
                number_position = [540,860]
                screen.blit(number, number_position)

            if 19 in s.holes:
                number_position = [142,542]
                screen.blit(number, number_position)
                number_position = [306,547]
                screen.blit(number, number_position)
                number_position = [605,609]
                screen.blit(number, number_position)
                number_position = [80,826]
                screen.blit(number, number_position)
                number_position = [374,820]
                screen.blit(number, number_position)
                number_position = [537,824]
                screen.blit(number, number_position)

            if 20 in s.holes:
                number_position = [148,611]
                screen.blit(number, number_position)
                number_position = [373,542]
                screen.blit(number, number_position)
                number_position = [541,616]
                screen.blit(number, number_position)
                number_position = [112,823]
                screen.blit(number, number_position)
                number_position = [274,828]
                screen.blit(number, number_position)
                number_position = [636,814]
                screen.blit(number, number_position)

            if 21 in s.holes:
                number_position = [82,616]
                screen.blit(number, number_position)
                number_position = [376,609]
                screen.blit(number, number_position)
                number_position = [534,544]
                screen.blit(number, number_position)
                number_position = [116,890]
                screen.blit(number, number_position)
                number_position = [346,890]
                screen.blit(number, number_position)
                number_position = [570,820]
                screen.blit(number, number_position)

            if 22 in s.holes:
                number_position = [78,548]
                screen.blit(number, number_position)
                number_position = [310,614]
                screen.blit(number, number_position)
                number_position = [600,540]
                screen.blit(number, number_position)
                number_position = [178,817]
                screen.blit(number, number_position)
                number_position = [341,820]
                screen.blit(number, number_position)
                number_position = [576,889]
                screen.blit(number, number_position)

            if 23 in s.holes:
                number_position = [84,650]
                screen.blit(number, number_position)
                number_position = [379,641]
                screen.blit(number, number_position)
                number_position = [638,605]
                screen.blit(number, number_position)
                number_position = [43,794]
                screen.blit(number, number_position)
                number_position = [302,756]
                screen.blit(number, number_position)
                number_position = [598,748]
                screen.blit(number, number_position)

            if 24 in s.holes:
                number_position = [46,620]
                screen.blit(number, number_position)
                number_position = [304,512]
                screen.blit(number, number_position)
                number_position = [500,548]
                screen.blit(number, number_position)
                number_position = [139,752]
                screen.blit(number, number_position)
                number_position = [404,782]
                screen.blit(number, number_position)
                number_position = [542,894]
                screen.blit(number, number_position)

            if 25 in s.holes:
                number_position = [141,508]
                screen.blit(number, number_position)
                number_position = [404,537]
                screen.blit(number, number_position)
                number_position = [542,648]
                screen.blit(number, number_position)
                number_position = [180,852]
                screen.blit(number, number_position)
                number_position = [276,862]
                screen.blit(number, number_position)
                number_position = [501,792]
                screen.blit(number, number_position)


    if s.game.tilt.status == True:
        tilt_position = [55,375]
        screen.blit(tilt, tilt_position)

    pygame.display.update()


