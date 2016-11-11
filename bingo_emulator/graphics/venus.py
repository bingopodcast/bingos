
import pygame

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

meter = pygame.image.load('graphics/assets/black_register_cover.png').convert()
card = pygame.image.load('stock_market/assets/card.png').convert_alpha()
number = pygame.image.load('stock_market/assets/number.png').convert_alpha()
corners = pygame.image.load('stock_market/assets/corners.png').convert_alpha()
scores = pygame.image.load('stock_market/assets/scores_collected.png').convert_alpha()
c = pygame.image.load('stock_market/assets/card_collected.png').convert_alpha()
d = pygame.image.load('stock_market/assets/double.png').convert_alpha()
n = pygame.image.load('stock_market/assets/nothing.png').convert_alpha()
tilt = pygame.image.load('stock_market/assets/tilt.png').convert_alpha()
blink_image = pygame.image.load('stock_market/assets/double_or_nothing.png').convert_alpha()

class scorereel():
    """ Score Reels are used to count replays """
    def __init__(self, pos, image):
        self.position = pos
        self.default_y = self.position[1]
        self.image = pygame.image.load(image).convert()

reel1 = scorereel([377,660], "graphics/assets/white_reel.png")
reel10 = scorereel([359,660], "graphics/assets/white_reel.png")
reel100 = scorereel([340,660], "graphics/assets/white_reel.png")
reel1000 = scorereel([320,660], "graphics/assets/white_reel.png")

def display(s, replays=0, menu=False):
    
    meter.set_colorkey((255,0,252))
    meter_position = [311,660]

    screen.blit(reel1.image, reel1.position)
    screen.blit(reel10.image, reel10.position)
    screen.blit(reel100.image, reel100.position)
    screen.blit(reel1000.image, reel1000.position)
    screen.blit(meter, meter_position)

    backglass_position = [0, 0]
    backglass = pygame.Surface((0,0), pygame.SRCALPHA)
    backglass.fill((0, 0, 0))
    if menu == True:
        backglass = pygame.image.load('stock_market/assets/stock_market_menu.png')
    else:
        if (s.game.anti_cheat.status == True):
            backglass = pygame.image.load('stock_market/assets/stock_market_gi.png')
        else:
            backglass = pygame.image.load('stock_market/assets/stock_market_off.png')
    screen.blit(backglass, backglass_position)

    if s.game.selector.position >= 1:
        position = [89,374]
        screen.blit(card, position)
    if s.game.selector.position >= 2:
        position = [282,361]
        screen.blit(card, position)
    if s.game.selector.position >= 3:
        position = [472,374]
        screen.blit(card, position)
    if s.game.selector.position >= 4:
        position = [90,768]
        screen.blit(card, position)
    if s.game.selector.position >= 5:
        position = [282,781]
        screen.blit(card, position)
    if s.game.selector.position >= 6:
        position = [474,765]
        screen.blit(card, position)

    if s.game.tilt.status == False:
        if s.holes:
            if 1 in s.holes:
                position = [119,438]
                screen.blit(number, position)
                position = [279,520]
                screen.blit(number, position)
                position = [600,437]
                screen.blit(number, position)
                position = [184,964]
                screen.blit(number, position)
                position = [346,845]
                screen.blit(number, position)
                position = [474,961]
                screen.blit(number, position)
            if 2 in s.holes:
                position = [152,569]
                screen.blit(number, position)
                position = [280,491]
                screen.blit(number, position)
                position = [601,471]
                screen.blit(number, position)
                position = [217,899]
                screen.blit(number, position)
                position = [379,977]
                screen.blit(number, position)
                position = [474,863]
                screen.blit(number, position)
            if 3 in s.holes:
                position = [216,439]
                screen.blit(number, position)
                position = [408,555]
                screen.blit(number, position)
                position = [537,439]
                screen.blit(number, position)
                position = [88,834]
                screen.blit(number, position)
                position = [347,879]
                screen.blit(number, position)
                position = [570,961]
                screen.blit(number, position)
            if 4 in s.holes:
                position = [184,569]
                screen.blit(number, position)
                position = [376,424]
                screen.blit(number, position)
                position = [568,568]
                screen.blit(number, position)
                position = [185,834]
                screen.blit(number, position)
                position = [282,847]
                screen.blit(number, position)
                position = [602,831]
                screen.blit(number, position)
            if 5 in s.holes:
                position = [88,439]
                screen.blit(number, position)
                position = [345,556]
                screen.blit(number, position)
                position = [471,504]
                screen.blit(number, position)
                position = [217,965]
                screen.blit(number, position)
                position = [411,846]
                screen.blit(number, position)
                position = [602,897]
                screen.blit(number, position)
            if 6 in s.holes:
                position = [88,504]
                screen.blit(number, position)
                position = [409,424]
                screen.blit(number, position)
                position = [472,439]
                screen.blit(number, position)
                position = [88,964]
                screen.blit(number, position)
                position = [315,847]
                screen.blit(number, position)
                position = [603,962]
                screen.blit(number, position)
            if 7 in s.holes:
                position = [216,471]
                screen.blit(number, position)
                position = [312,556]
                screen.blit(number, position)
                position = [503,438]
                screen.blit(number, position)
                position = [120,833]
                screen.blit(number, position)
                position = [282,976]
                screen.blit(number, position)
                position = [506,962]
                screen.blit(number, position)
            if 8 in s.holes:
                position = [88,470]
                screen.blit(number, position)
                position = [409,522]
                screen.blit(number, position)
                position = [601,568]
                screen.blit(number, position)
                position = [216,865]
                screen.blit(number, position)
                position = [410,944]
                screen.blit(number, position)
                position = [473,832]
                screen.blit(number, position)
            if 9 in s.holes:
                position = [152,439]
                screen.blit(number, position)
                position = [280,425]
                screen.blit(number, position)
                position = [536,536]
                screen.blit(number, position)
                position = [217,834]
                screen.blit(number, position)
                position = [282,912]
                screen.blit(number, position)
                position = [538,929]
                screen.blit(number, position)
            if 10 in s.holes:
                position = [152,471]
                screen.blit(number, position)
                position = [280,556]
                screen.blit(number, position)
                position = [472,569]
                screen.blit(number, position)
                position = [153,835]
                screen.blit(number, position)
                position = [283,942]
                screen.blit(number, position)
                position = [538,831]
                screen.blit(number, position)
            if 11 in s.holes:
                position = [184,504]
                screen.blit(number, position)
                position = [345,523]
                screen.blit(number, position)
                position = [472,535]
                screen.blit(number, position)
                position = [185,899]
                screen.blit(number, position)
                position = [412,976]
                screen.blit(number, position)
                position = [602,928]
                screen.blit(number, position)
            if 12 in s.holes:
                position = [88,569]
                screen.blit(number, position)
                position = [377,490]
                screen.blit(number, position)
                position = [536,470]
                screen.blit(number, position)
                position = [153,932]
                screen.blit(number, position)
                position = [378,911]
                screen.blit(number, position)
                position = [506,898]
                screen.blit(number, position)
            if 13 in s.holes:
                position = [216,535]
                screen.blit(number, position)
                position = [280,458]
                screen.blit(number, position)
                position = [504,568]
                screen.blit(number, position)
                position = [87,931]
                screen.blit(number, position)
                position = [411,878]
                screen.blit(number, position)
                position = [569,831]
                screen.blit(number, position)
            if 14 in s.holes:
                position = [153,537]
                screen.blit(number, position)
                position = [344,458]
                screen.blit(number, position)
                position = [505,470]
                screen.blit(number, position)
                position = [121,900]
                screen.blit(number, position)
                position = [379,943]
                screen.blit(number, position)
                position = [571,865]
                screen.blit(number, position)
            if 15 in s.holes:
                position = [217,569]
                screen.blit(number, position)
                position = [345,490]
                screen.blit(number, position)
                position = [569,536]
                screen.blit(number, position)
                position = [88,899]
                screen.blit(number, position)
                position = [314,879]
                screen.blit(number, position)
                position = [505,929]
                screen.blit(number, position)
            if 16 in s.holes:
                position = [152,505]
                screen.blit(number, position)
                position = [344,425]
                screen.blit(number, position)
                position = [568,505]
                screen.blit(number, position)
                position = [153,965]
                screen.blit(number, position)
                position = [348,944]
                screen.blit(number, position)
                position = [538,864]
                screen.blit(number, position)
            if 17 in s.holes:
                position = [216,505]
                screen.blit(number, position)
                position = [409,491]
                screen.blit(number, position)
                position = [504,536]
                screen.blit(number, position)
                position = [153,900]
                screen.blit(number, position)
                position = [379,878]
                screen.blit(number, position)
                position = [505,864]
                screen.blit(number, position)
            if 18 in s.holes:
                position = [120,505]
                screen.blit(number, position)
                position = [312,490]
                screen.blit(number, position)
                position = [569,472]
                screen.blit(number, position)
                position = [153,867]
                screen.blit(number, position)
                position = [315,942]
                screen.blit(number, position)
                position = [570,929]
                screen.blit(number, position)
            if 19 in s.holes:
                position = [184,472]
                screen.blit(number, position)
                position = [312,457]
                screen.blit(number, position)
                position = [504,504]
                screen.blit(number, position)
                position = [184,931]
                screen.blit(number, position)
                position = [315,911]
                screen.blit(number, position)
                position = [570,898]
                screen.blit(number, position)
            if 20 in s.holes:
                position = [184,537]
                screen.blit(number, position)
                position = [376,458]
                screen.blit(number, position)
                position = [536,504]
                screen.blit(number, position)
                position = [120,932]
                screen.blit(number, position)
                position = [411,912]
                screen.blit(number, position)
                position = [474,897]
                screen.blit(number, position)
            if 21 in s.holes:
                position = [120,536]
                screen.blit(number, position)
                position = [376,521]
                screen.blit(number, position)
                position = [536,569]
                screen.blit(number, position)
                position = [120,867]
                screen.blit(number, position)
                position = [347,912]
                screen.blit(number, position)
                position = [538,962]
                screen.blit(number, position)
            if 22 in s.holes:
                position = [121,472]
                screen.blit(number, position)
                position = [312,523]
                screen.blit(number, position)
                position = [601,504]
                screen.blit(number, position)
                position = [185,867]
                screen.blit(number, position)
                position = [348,977]
                screen.blit(number, position)
                position = [538,897]
                screen.blit(number, position)
            if 23 in s.holes:
                position = [120,568]
                screen.blit(number, position)
                position = [376,555]
                screen.blit(number, position)
                position = [472,471]
                screen.blit(number, position)
                position = [217,932]
                screen.blit(number, position)
                position = [379,846]
                screen.blit(number, position)
                position = [507,832]
                screen.blit(number, position)
            if 24 in s.holes:
                position = [89,536]
                screen.blit(number, position)
                position = [311,426]
                screen.blit(number, position)
                position = [568,438]
                screen.blit(number, position)
                position = [88,867]
                screen.blit(number, position)
                position = [315,977]
                screen.blit(number, position)
                position = [603,865]
                screen.blit(number, position)
            if 25 in s.holes:
                position = [184,439]
                screen.blit(number, position)
                position = [409,458]
                screen.blit(number, position)
                position = [601,536]
                screen.blit(number, position)
                position = [121,965]
                screen.blit(number, position)
                position = [283,879]
                screen.blit(number, position)
                position = [473,929]
                screen.blit(number, position)

        if s.game.corners1.status == True:
            position = [199,372]
            screen.blit(corners, position)
        if s.game.corners2.status == True:
            position = [391,358]
            screen.blit(corners, position)
        if s.game.corners3.status == True:
            position = [583,373]
            screen.blit(corners, position)
        if s.game.corners4.status == True:
            position = [199,767]
            screen.blit(corners, position)
        if s.game.corners5.status == True:
            position = [391,779]
            screen.blit(corners, position)
        if s.game.corners6.status == True:
            position = [584,763]
            screen.blit(corners, position)

        if s.game.card1_replay_counter.position > 0 or s.game.card2_replay_counter.position > 0 or s.game.card3_replay_counter.position > 0 or s.game.card4_replay_counter.position > 0 or s.game.card5_replay_counter.position > 0 or s.game.card6_replay_counter.position > 0:
            position = [16,607]
            screen.blit(scores, position)
            if s.game.card1_replay_counter.position > 0:
                position = [16,651]
                screen.blit(c, position)
            if s.game.card2_replay_counter.position > 0:
                position = [46,668]
                screen.blit(c, position)
            if s.game.card3_replay_counter.position > 0:
                position = [17,685]
                screen.blit(c, position)
            if s.game.card4_replay_counter.position > 0:
                position = [46,702]
                screen.blit(c, position)
            if s.game.card5_replay_counter.position > 0:
                position = [16,717]
                screen.blit(c, position)
            if s.game.card6_replay_counter.position > 0:
                position = [46,735]
                screen.blit(c, position)

        if s.game.card1_double.status == True:
            position = [92,407]
            screen.blit(d, position)
        if s.game.card2_double.status == True:
            position = [282,393]
            screen.blit(d, position)
        if s.game.card3_double.status == True:
            position = [474,406]
            screen.blit(d, position)
        if s.game.card4_double.status == True:
            position = [92,800]
            screen.blit(d, position)
        if s.game.card5_double.status == True:
            position = [281,816]
            screen.blit(d, position)
        if s.game.card6_double.status == True:
            position = [476,797]
            screen.blit(d, position)

        if s.game.card1_missed.status == True:
            position = [142,407]
            screen.blit(n, position)
        if s.game.card2_missed.status == True:
            position = [336,393]
            screen.blit(n, position)
        if s.game.card3_missed.status == True:
            position = [526,406]
            screen.blit(n, position)
        if s.game.card4_missed.status == True:
            position = [144,800]
            screen.blit(n, position)
        if s.game.card5_missed.status == True:
            position = [336,816]
            screen.blit(n, position)
        if s.game.card6_missed.status == True:
            position = [530,797]
            screen.blit(n, position)

    if s.game.tilt.status == True:
        position = [667,818]
        screen.blit(tilt, position)

    pygame.display.update()

def blink_double(s):
    s.game.blink = not s.game.blink
    if s.game.blink == 1:
        blink_pos = [86,630]
        screen.blit(blink_image, blink_pos)
        pygame.display.update()
    else:
        display(s)
