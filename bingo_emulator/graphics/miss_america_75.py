
import pygame
import random

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

meter = pygame.image.load('graphics/assets/black_register_cover.png').convert()
eb = pygame.image.load('miss_america_75/assets/eb.png').convert_alpha()
number_eb = pygame.image.load('miss_america_75/assets/eb_number.png').convert_alpha()
ebs = pygame.image.load('miss_america_75/assets/extra_balls.png').convert_alpha()
number = pygame.image.load('miss_america_75/assets/number.png').convert_alpha()
card1 = pygame.image.load('miss_america_75/assets/card1.png').convert_alpha()
card2 = pygame.image.load('miss_america_75/assets/card2.png').convert_alpha()
feature = pygame.image.load('miss_america_75/assets/feature.png').convert_alpha()
letter = pygame.image.load('miss_america_75/assets/letter.png').convert_alpha()
odds = pygame.image.load('miss_america_75/assets/odds.png').convert_alpha()
rollover = pygame.image.load('miss_america_75/assets/rollover.png').convert_alpha()
s_arrow = pygame.image.load('miss_america_75/assets/s_arrow.png').convert_alpha()
select_now = pygame.image.load('miss_america_75/assets/select_now.png').convert_alpha()
time = pygame.image.load('miss_america_75/assets/time.png').convert_alpha()
tilt = pygame.image.load('miss_america_75/assets/tilt.png').convert_alpha()
line1 = pygame.image.load('miss_america_75/assets/line1.png').convert_alpha()
line2 = pygame.image.load('miss_america_75/assets/line2.png').convert_alpha()
line3 = pygame.image.load('miss_america_75/assets/line3.png').convert_alpha()
line4 = pygame.image.load('miss_america_75/assets/line4.png').convert_alpha()
line5 = pygame.image.load('miss_america_75/assets/line5.png').convert_alpha()
d = pygame.image.load('miss_america_75/assets/double.png').convert_alpha()
n = pygame.image.load('miss_america_75/assets/nothing.png').convert_alpha()
r = pygame.image.load('miss_america_75/assets/regular.png').convert_alpha()
blink_image = pygame.image.load('miss_america_75/assets/double_or_nothing.png').convert_alpha()
bg_menu = pygame.image.load('miss_america_75/assets/miss_america_75_menu.png')
bg_gi = pygame.image.load('miss_america_75/assets/miss_america_75_gi.png')
bg_off = pygame.image.load('miss_america_75/assets/miss_america_75_off.png')

class scorereel():
    """ Score Reels are used to count replays """
    def __init__(self, pos, image):
        self.position = pos
        self.default_y = self.position[1]
        self.image = pygame.image.load(image).convert()

reel1 = scorereel([107,800], "graphics/assets/white_reel.png")
reel10 = scorereel([88,800], "graphics/assets/white_reel.png")
reel100 = scorereel([68,800], "graphics/assets/white_reel.png")
reel1000 = scorereel([49,800], "graphics/assets/white_reel.png")

def display(s, replays=0, menu=False):
    
    meter.set_colorkey((255,0,252))
    meter_position = [40,800]

    screen.blit(reel1.image, reel1.position)
    screen.blit(reel10.image, reel10.position)
    screen.blit(reel100.image, reel100.position)
    screen.blit(reel1000.image, reel1000.position)
    screen.blit(meter, meter_position)

    if s.game.line1.position == 0 or s.game.line1.position == 2:
        p = [80,340]
        screen.blit(line1, p)
    if s.game.line1.position == 1:
        p = [120,340]
        screen.blit(line1, p)
    if s.game.line1.position == 3:
        p = [40,340]
        screen.blit(line1, p)

    if s.game.line2.position == 0 or s.game.line2.position == 2:
        p = [76,378]
        screen.blit(line2, p)
    if s.game.line2.position == 1:
        p = [120,378]
        screen.blit(line2, p)
    if s.game.line2.position == 3:
        p = [40,378]
        screen.blit(line2, p)

    if s.game.line3.position == 0 or s.game.line3.position == 2:
        p = [80,420]
        screen.blit(line3, p)
    if s.game.line3.position == 1:
        p = [120,420]
        screen.blit(line3, p)
    if s.game.line3.position == 3:
        p = [40,420]
        screen.blit(line3, p)

    if s.game.line4.position == 0 or s.game.line4.position == 2:
        p = [75,455]
        screen.blit(line4, p)
    if s.game.line4.position == 1:
        p = [115,455]
        screen.blit(line4, p)
    if s.game.line4.position == 3:
        p = [35,455]
        screen.blit(line4, p)

    if s.game.line5.position == 0 or s.game.line5.position == 2:
        p = [75,495]
        screen.blit(line5, p)
    if s.game.line5.position == 1:
        p = [115,495]
        screen.blit(line5, p)
    if s.game.line5.position == 3:
        p = [35,495]
        screen.blit(line5, p)

    backglass_position = [0, 0]
    backglass = pygame.Surface(screen.get_size(), flags=pygame.SRCALPHA)
    backglass.set_colorkey((255,0,252))
    backglass.fill((0, 0, 0))
    if menu == True:
        screen.blit(bg_menu, backglass_position)
    else:
        if (s.game.anti_cheat.status == True):
            screen.blit(bg_gi, backglass_position)
        else:
            screen.blit(bg_off, backglass_position)

    if s.game.rollovers.status == True and s.game.selection_feature.position >= 5:
        if s.game.cu:
            p = [7,958]
            screen.blit(rollover, p)
        else:
            p = [638,953]
            screen.blit(rollover, p)

    if s.game.eb_play.status == True:
        ebs_position = [46,1036]
        screen.blit(ebs, ebs_position)


    if s.game.extra_ball.position >= 1:
        eb_position = [155,1038]
        screen.blit(number_eb, eb_position)
    if s.game.extra_ball.position >= 2:
        eb_position = [202,1038]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 3:
        eb_position = [267,1038]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 4:
        eb_position = [327,1036]
        screen.blit(number_eb, eb_position)
    if s.game.extra_ball.position >= 5:
        eb_position = [378,1036]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 6:
        eb_position = [442,1036]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 7:
        eb_position = [503,1032]
        screen.blit(number_eb, eb_position)
    if s.game.extra_ball.position >= 8:
        eb_position = [551,1032]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 9:
        eb_position = [615,1032]
        screen.blit(eb, eb_position)

    if s.game.red_odds.position == 1:
        odds_position = [192,786]
        screen.blit(odds, odds_position)
    if s.game.red_odds.position == 2:
        odds_position = [268,786]
        screen.blit(odds, odds_position)
    if s.game.red_odds.position == 3:
        odds_position = [340,786]
        screen.blit(odds, odds_position)
    if s.game.red_odds.position == 4:
        odds_position = [410,786]
        screen.blit(odds, odds_position)
    if s.game.red_odds.position == 5:
        odds_position = [470,786]
        screen.blit(odds, odds_position)
    if s.game.red_odds.position == 6:
        odds_position = [530,786]
        screen.blit(odds, odds_position)
    if s.game.red_odds.position == 7:
        odds_position = [580,786]
        screen.blit(odds, odds_position)

    if s.game.yellow_odds.position == 1:
        odds_position = [192,848]
        screen.blit(odds, odds_position)
    if s.game.yellow_odds.position == 2:
        odds_position = [268,848]
        screen.blit(odds, odds_position)
    if s.game.yellow_odds.position == 3:
        odds_position = [340,848]
        screen.blit(odds, odds_position)
    if s.game.yellow_odds.position == 4:
        odds_position = [410,848]
        screen.blit(odds, odds_position)
    if s.game.yellow_odds.position == 5:
        odds_position = [470,848]
        screen.blit(odds, odds_position)
    if s.game.yellow_odds.position == 6:
        odds_position = [530,848]
        screen.blit(odds, odds_position)
    if s.game.yellow_odds.position == 7:
        odds_position = [580,848]
        screen.blit(odds, odds_position)

    if s.game.green_odds.position == 1:
        odds_position = [192,908]
        screen.blit(odds, odds_position)
    if s.game.green_odds.position == 2:
        odds_position = [268,908]
        screen.blit(odds, odds_position)
    if s.game.green_odds.position == 3:
        odds_position = [340,908]
        screen.blit(odds, odds_position)
    if s.game.green_odds.position == 4:
        odds_position = [410,908]
        screen.blit(odds, odds_position)
    if s.game.green_odds.position == 5:
        odds_position = [470,908]
        screen.blit(odds, odds_position)
    if s.game.green_odds.position == 6:
        odds_position = [530,908]
        screen.blit(odds, odds_position)
    if s.game.green_odds.position == 7:
        odds_position = [580,908]
        screen.blit(odds, odds_position)

    if s.game.white_odds.position == 1:
        odds_position = [192,968]
        screen.blit(odds, odds_position)
    if s.game.white_odds.position == 2:
        odds_position = [268,968]
        screen.blit(odds, odds_position)
    if s.game.white_odds.position == 3:
        odds_position = [340,968]
        screen.blit(odds, odds_position)
    if s.game.white_odds.position == 4:
        odds_position = [410,970]
        screen.blit(odds, odds_position)
    if s.game.white_odds.position == 5:
        odds_position = [470,970]
        screen.blit(odds, odds_position)
    if s.game.white_odds.position == 6:
        odds_position = [530,970]
        screen.blit(odds, odds_position)
    if s.game.white_odds.position == 7:
        odds_position = [580,970]
        screen.blit(odds, odds_position)

    if s.game.red_double.status == True:
        position = [26,655]
        screen.blit(d, position)
    if s.game.yellow_double.status == True:
        position = [152,654]
        screen.blit(d, position)
    if s.game.green_double.status == True:
        position = [467,653]
        screen.blit(d, position)
    if s.game.white_double.status == True:
        position = [590,652]
        screen.blit(d, position)

    if s.game.red_missed.status == True:
        position = [84,655]
        screen.blit(n, position)
    if s.game.yellow_missed.status == True:
        position = [210,654]
        screen.blit(n, position)
    if s.game.green_missed.status == True:
        position = [524,653]
        screen.blit(n, position)
    if s.game.white_missed.status == True:
        position = [644,652]
        screen.blit(n, position)

    if s.game.red_regular.status == True:
        position = [27,623]
        screen.blit(r, position)
    if s.game.yellow_regular.status == True:
        position = [154,622]
        screen.blit(r, position)
    if s.game.green_regular.status == True:
        position = [468,621]
        screen.blit(r, position)
    if s.game.white_regular.status == True:
        position = [594,621]
        screen.blit(r, position)

    if s.game.tilt.status == False:
        if s.holes:
            if 1 in s.holes:
                if s.game.line2.position == 0 or s.game.line2.position == 2:
                    p = [205,384]
                    screen.blit(number, p)
                if s.game.line4.position == 0 or s.game.line4.position == 2:
                    p = [403,460]
                    screen.blit(number, p)
                if s.game.line2.position == 1:
                    p = [245,384]
                    screen.blit(number, p)
                if s.game.line4.position == 1:
                    p = [442,461]
                    screen.blit(number, p)
                if s.game.line2.position == 3:
                    p = [166,385]
                    screen.blit(number, p)
                if s.game.line4.position == 3:
                    p = [285,461]
                    screen.blit(number, p)
            if 2 in s.holes:
                if s.game.line2.position == 0 or s.game.line2.position == 2:
                    p = [126,384]
                    screen.blit(number, p)
                if s.game.line1.position == 0 or s.game.line1.position == 2:
                    p = [559,346]
                    screen.blit(number, p)
                if s.game.line2.position == 1:
                    p = [165,385]
                    screen.blit(number, p)
                if s.game.line1.position == 1:
                    p = [127,346]
                    screen.blit(number, p)
                if s.game.line2.position == 3:
                    p = [560,385]
                    screen.blit(number, p)
                if s.game.line1.position == 3:
                    p = [520,346]
                    screen.blit(number, p)
            if 3 in s.holes:
                if s.game.line3.position == 0 or s.game.line3.position == 2:
                    p = [284,422]
                    screen.blit(number, p)
                if s.game.line4.position == 0 or s.game.line4.position == 2:
                    p = [560,462]
                    screen.blit(number, p)
                if s.game.line3.position == 1:
                    p = [404,423]
                    screen.blit(number, p)
                if s.game.line4.position == 1:
                    p = [125,462]
                    screen.blit(number, p)
                if s.game.line3.position == 3:
                    p = [245,423]
                    screen.blit(number, p)
                if s.game.line4.position == 3:
                    p = [522,461]
                    screen.blit(number, p)
            if 4 in s.holes:
                if s.game.line5.position == 0 or s.game.line5.position == 2:
                    p = [165,501]
                    screen.blit(number, p)
                    p = [561,499]
                    screen.blit(number, p)
                if s.game.line5.position == 1:
                    p = [206,499]
                    screen.blit(number, p)
                    p = [125,499]
                    screen.blit(number, p)
                if s.game.line5.position == 3:
                    p = [125,499]
                    screen.blit(number, p)
                    p = [522,499]
                    screen.blit(number, p)
            if 5 in s.holes:
                if s.game.line1.position == 0 or s.game.line1.position == 2:
                    p = [127,346]
                    screen.blit(number, p)
                if s.game.line5.position == 0 or s.game.line5.position == 2:
                    p = [522,499]
                    screen.blit(number, p)
                if s.game.line1.position == 1:
                    p = [166,346]
                    screen.blit(number, p)
                if s.game.line5.position == 1:
                    p = [560,498]
                    screen.blit(number, p)
                if s.game.line1.position == 3:
                    p = [560,346]
                    screen.blit(number, p)
                if s.game.line5.position == 3:
                    p = [482,499]
                    screen.blit(number, p)
            if 6 in s.holes:
                if s.game.line1.position == 0 or s.game.line1.position == 2:
                    p = [246,345]
                    screen.blit(number, p)
                    p = [404,345]
                    screen.blit(number, p)
                if s.game.line1.position == 1:
                    p = [285,347]
                    screen.blit(number, p)
                    p = [443,346]
                    screen.blit(number, p)
                if s.game.line1.position == 3:
                    p = [207,346]
                    screen.blit(number, p)
                    p = [285,346]
                    screen.blit(number, p)
            if 7 in s.holes:
                if s.game.line3.position == 0 or s.game.line3.position == 2:
                    p = [403,422]
                    screen.blit(number, p)
                if s.game.line5.position == 0 or s.game.line5.position == 2:
                    p = [126,500]
                    screen.blit(number, p)
                if s.game.line3.position == 1:
                    p = [442,423]
                    screen.blit(number, p)
                if s.game.line5.position == 1:
                    p = [166,501]
                    screen.blit(number, p)
                if s.game.line3.position == 3:
                    p = [285,422]
                    screen.blit(number, p)
                if s.game.line5.position == 3:
                    p = [561,499]
                    screen.blit(number, p)
            if 8 in s.holes:
                if s.game.line1.position == 0 or s.game.line1.position == 2:
                    p = [207,347]
                    screen.blit(number, p)
                    p = [443,345]
                    screen.blit(number, p)
                if s.game.line1.position == 1:
                    p = [246,346]
                    screen.blit(number, p)
                    p = [481,347]
                    screen.blit(number, p)
                if s.game.line1.position == 3:
                    p = [167,346]
                    screen.blit(number, p)
                    p = [403,346]
                    screen.blit(number, p)
            if 9 in s.holes:
                if s.game.line3.position == 0 or s.game.line3.position == 2:
                    p = [126,424]
                    screen.blit(number, p)
                if s.game.line5.position == 0 or s.game.line5.position == 2:
                    p = [483,498]
                    screen.blit(number, p)
                if s.game.line3.position == 1:
                    p = [165,423]
                    screen.blit(number, p)
                if s.game.line5.position == 1:
                    p = [522,499]
                    screen.blit(number, p)
                if s.game.line3.position == 3:
                    p = [561,423]
                    screen.blit(number, p)
                if s.game.line5.position == 3:
                    p = [444,499]
                    screen.blit(number, p)
            if 10 in s.holes:
                if s.game.line1.position == 0 or s.game.line1.position == 2:
                    p = [521,346]
                    screen.blit(number, p)
                if s.game.line5.position == 0 or s.game.line5.position == 2:
                    p = [206,499]
                    screen.blit(number, p)
                if s.game.line1.position == 1:
                    p = [560,346]
                    screen.blit(number, p)
                if s.game.line5.position == 1:
                    p = [245,498]
                    screen.blit(number, p)
                if s.game.line1.position == 3:
                    p = [482,347]
                    screen.blit(number, p)
                if s.game.line5.position == 3:
                    p = [166,501]
                    screen.blit(number, p)
            if 11 in s.holes:
                if s.game.line1.position == 0 or s.game.line1.position == 2:
                    p = [482,346]
                    screen.blit(number, p)
                if s.game.line5.position == 0 or s.game.line5.position == 2:
                    p = [245,499]
                    screen.blit(number, p)
                if s.game.line1.position == 1:
                    p = [521,346]
                    screen.blit(number, p)
                if s.game.line5.position == 1:
                    p = [285,499]
                    screen.blit(number, p)
                if s.game.line1.position == 3:
                    p = [443,345]
                    screen.blit(number, p)
                if s.game.line5.position == 3:
                    p = [206,499]
                    screen.blit(number, p)
            if 12 in s.holes:
                if s.game.line3.position == 0 or s.game.line3.position == 2:
                    p = [245,423]
                    screen.blit(number, p)
                if s.game.line4.position == 0 or s.game.line4.position == 2:
                    p = [483,461]
                    screen.blit(number, p)
                if s.game.line3.position == 1:
                    p = [285,423]
                    screen.blit(number, p)
                if s.game.line4.position == 1:
                    p = [522,461]
                    screen.blit(number, p)
                if s.game.line3.position == 3:
                    p = [205,422]
                    screen.blit(number, p)
                if s.game.line4.position == 3:
                    p = [443,461]
                    screen.blit(number, p)
            if 13 in s.holes:
                if s.game.line2.position == 0 or s.game.line2.position == 2:
                    p = [285,384]
                    screen.blit(number, p)
                if s.game.line5.position == 0 or s.game.line5.position == 2:
                    p = [443,499]
                    screen.blit(number, p)
                if s.game.line2.position == 1:
                    p = [403,384]
                    screen.blit(number, p)
                if s.game.line5.position == 1:
                    p = [482,499]
                    screen.blit(number, p)
                if s.game.line2.position == 3:
                    p = [245,384]
                    screen.blit(number, p)
                if s.game.line5.position == 3:
                    p = [403,499]
                    screen.blit(number, p)
            if 14 in s.holes:
                if s.game.line1.position == 0 or s.game.line1.position == 2:
                    p = [167,346]
                    screen.blit(number, p)
                if s.game.line2.position == 0 or s.game.line2.position == 2:
                    p = [404,385]
                    screen.blit(number, p)
                if s.game.line1.position == 1:
                    p = [207,347]
                    screen.blit(number, p)
                if s.game.line2.position == 1:
                    p = [443,385]
                    screen.blit(number, p)
                if s.game.line1.position == 3:
                    p = [127,346]
                    screen.blit(number, p)
                if s.game.line2.position == 3:
                    p = [285,385]
                    screen.blit(number, p)
            if 15 in s.holes:
                if s.game.line2.position == 0 or s.game.line2.position == 2:
                    p = [561,384]
                    screen.blit(number, p)
                if s.game.line4.position == 0 or s.game.line4.position == 2:
                    p = [285,461]
                    screen.blit(number, p)
                if s.game.line2.position == 1:
                    p = [126,385]
                    screen.blit(number, p)
                if s.game.line4.position == 1:
                    p = [404,461]
                    screen.blit(number, p)
                if s.game.line2.position == 3:
                    p = [521,385]
                    screen.blit(number, p)
                if s.game.line4.position == 3:
                    p = [246,460]
                    screen.blit(number, p)
            if 16 in s.holes:
                if s.game.line3.position == 0 or s.game.line3.position == 2:
                    p = [482,423]
                    screen.blit(number, p)
                if s.game.line4.position == 0 or s.game.line4.position == 2:
                    p = [127,461]
                    screen.blit(number, p)
                if s.game.line3.position == 1:
                    p = [522,422]
                    screen.blit(number, p)
                if s.game.line4.position == 1:
                    p = [165,462]
                    screen.blit(number, p)
                if s.game.line3.position == 3:
                    p = [444,422]
                    screen.blit(number, p)
                if s.game.line4.position == 3:
                    p = [561,461]
                    screen.blit(number, p)
            if 17 in s.holes:
                if s.game.line3.position == 0 or s.game.line3.position == 2:
                    p = [205,423]
                    screen.blit(number, p)
                    p = [522,422]
                    screen.blit(number, p)
                if s.game.line3.position == 1:
                    p = [246,422]
                    screen.blit(number, p)
                    p = [560,422]
                    screen.blit(number, p)
                if s.game.line3.position == 3:
                    p = [165,423]
                    screen.blit(number, p)
                    p = [482,423]
                    screen.blit(number, p)
            if 18 in s.holes:
                if s.game.line3.position == 0 or s.game.line3.position == 2:
                    p = [443,423]
                    screen.blit(number, p)
                if s.game.line4.position == 0 or s.game.line4.position == 2:
                    p = [206,461]
                    screen.blit(number, p)
                if s.game.line3.position == 1:
                    p = [483,422]
                    screen.blit(number, p)
                if s.game.line4.position == 1:
                    p = [245,461]
                    screen.blit(number, p)
                if s.game.line3.position == 3:
                    p = [404,422]
                    screen.blit(number, p)
                if s.game.line4.position == 3:
                    p = [165,462]
                    screen.blit(number, p)
            if 19 in s.holes:
                if s.game.line2.position == 0 or s.game.line2.position == 2:
                    p = [165,386]
                    screen.blit(number, p)
                    p = [443,385]
                    screen.blit(number, p)
                if s.game.line2.position == 1:
                    p = [206,385]
                    screen.blit(number, p)
                    p = [483,385]
                    screen.blit(number, p)
                if s.game.line2.position == 3:
                    p = [126,385]
                    screen.blit(number, p)
                    p = [404,385]
                    screen.blit(number, p)
            if 20 in s.holes:
                if s.game.line2.position == 0 or s.game.line2.position == 2:
                    p = [245,383]
                    screen.blit(number, p)
                if s.game.line4.position == 0 or s.game.line4.position == 2:
                    p = [443,461]
                    screen.blit(number, p)
                if s.game.line2.position == 1:
                    p = [286,385]
                    screen.blit(number, p)
                if s.game.line4.position == 1:
                    p = [482,461]
                    screen.blit(number, p)
                if s.game.line2.position == 3:
                    p = [206,384]
                    screen.blit(number, p)
                if s.game.line4.position == 3:
                    p = [403,461]
                    screen.blit(number, p)
            if 21 in s.holes:
                if s.game.line4.position == 0 or s.game.line4.position == 2:
                    p = [245,461]
                    screen.blit(number, p)
                    p = [523,461]
                    screen.blit(number, p)
                if s.game.line4.position == 1:
                    p = [286,461]
                    screen.blit(number, p)
                    p = [561,462]
                    screen.blit(number, p)
                if s.game.line4.position == 3:
                    p = [206,461]
                    screen.blit(number, p)
                    p = [482,461]
                    screen.blit(number, p)
            if 22 in s.holes:
                if s.game.line2.position == 0 or s.game.line2.position == 2:
                    p = [521,385]
                    screen.blit(number, p)
                if s.game.line4.position == 0 or s.game.line4.position == 2:
                    p = [165,462]
                    screen.blit(number, p)
                if s.game.line2.position == 1:
                    p = [561,384]
                    screen.blit(number, p)
                if s.game.line4.position == 1:
                    p = [206,461]
                    screen.blit(number, p)
                if s.game.line2.position == 3:
                    p = [483,385]
                    screen.blit(number, p)
                if s.game.line4.position == 3:
                    p = [126,462]
                    screen.blit(number, p)
            if 23 in s.holes:
                if s.game.line2.position == 0 or s.game.line2.position == 2:
                    p = [483,384]
                    screen.blit(number, p)
                if s.game.line3.position == 0 or s.game.line3.position == 2:
                    p = [165,423]
                    screen.blit(number, p)
                if s.game.line2.position == 1:
                    p = [522,385]
                    screen.blit(number, p)
                if s.game.line3.position == 1:
                    p = [206,422]
                    screen.blit(number, p)
                if s.game.line2.position == 3:
                    p = [443,385]
                    screen.blit(number, p)
                if s.game.line3.position == 3:
                    p = [127,423]
                    screen.blit(number, p)
            if 24 in s.holes:
                if s.game.line5.position == 0 or s.game.line5.position == 2:
                    p = [285,498]
                    screen.blit(number, p)
                    p = [404,498]
                    screen.blit(number, p)
                if s.game.line5.position == 1:
                    p = [404,498]
                    screen.blit(number, p)
                    p = [443,499]
                    screen.blit(number, p)
                if s.game.line5.position == 3:
                    p = [245,498]
                    screen.blit(number, p)
                    p = [285,498]
                    screen.blit(number, p)
            if 25 in s.holes:
                if s.game.line1.position == 0 or s.game.line1.position == 2:
                    p = [286,346]
                    screen.blit(number, p)
                if s.game.line3.position == 0 or s.game.line3.position == 2:
                    p = [561,422]
                    screen.blit(number, p)
                if s.game.line1.position == 1:
                    p = [404,346]
                    screen.blit(number, p)
                if s.game.line3.position == 1:
                    p = [127,423]
                    screen.blit(number, p)
                if s.game.line1.position == 3:
                    p = [246,345]
                    screen.blit(number, p)
                if s.game.line3.position == 3:
                    p = [523,423]
                    screen.blit(number, p)

    if s.game.tilt.status == True:
        tilt_position = [16,745]
        screen.blit(tilt, tilt_position)

    if s.game.corners.status == True:
        p = [10,414]
        screen.blit(feature, p)

    if s.game.selector.position >= 1:
        p = [145,311]
        screen.blit(card1, p)
    if s.game.selector.position >= 2:
        p = [407,311]
        screen.blit(card2, p)
        p = [632,414]
        screen.blit(feature, p)

    if s.game.selection_feature.position >= 5:
        if s.game.before_fourth.status == True:
            p = [460,694]
            screen.blit(time, p)
        if s.game.before_fifth.status == True:
            p = [575,693]
            screen.blit(time, p)

    if s.game.selection_feature.position == 1:
        p = [32,697]
        screen.blit(s_arrow, p)
    if s.game.selection_feature.position == 2:
        p = [76,697]
        screen.blit(s_arrow, p)
    if s.game.selection_feature.position == 3:
        p = [121,697]
        screen.blit(s_arrow, p)
    if s.game.selection_feature.position == 4:
        p = [166,697]
        screen.blit(s_arrow, p)
    if s.game.selection_feature.position >= 5:
        p = [206,695]
        screen.blit(letter, p)
    if s.game.selection_feature.position >= 6:
        p = [251,695]
        screen.blit(letter, p)
    if s.game.selection_feature.position >= 7:
        p = [296,695]
        screen.blit(letter, p)
    if s.game.selection_feature.position >= 8:
        p = [340,694]
        screen.blit(letter, p)
    if s.game.selection_feature.position >= 9:
        p = [385,695]
        screen.blit(letter, p)

    if s.game.selection_feature.position >= 5:
        if s.game.before_fourth.status == True:
            if s.game.ball_count.position == 3:
                s.cancel_delayed(name="blink")
                blink([s,1,1])
            else:
                s.cancel_delayed(name="blink")
        elif s.game.before_fifth.status == True:
            if s.game.ball_count.position == 4:
                s.cancel_delayed(name="blink")
                blink([s,1,1])
            else:
                s.cancel_delayed(name="blink")

    pygame.display.update()

def blink(args):
    dirty_rects = []
    s = args[0]
    b = args[1]
    sn = args[2]

    if b == 0:
        if sn == 1:
            p = [475,749]
            dirty_rects.append(screen.blit(select_now, p))
        pygame.display.update(dirty_rects)
    else:
        dirty_rects.append(screen.blit(bg_gi, (475,749), pygame.Rect(475,749,188,32)))
        pygame.display.update(dirty_rects)
    b = not b

    args = [s,b,sn]

    s.delay(name="blink", delay=0.1, handler=blink, param=args)

def eb_animation(num):
    global screen
    if num == 9:
        eb_position = [155,1038]
        screen.blit(number_eb, eb_position)
        pygame.display.update()
    if num == 8:
        eb_position = [202,1038]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 7:
        eb_position = [267,1038]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 6:
        eb_position = [327,1036]
        screen.blit(number_eb, eb_position)
        pygame.display.update()
    if num == 5:
        eb_position = [378,1036]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 4:
        eb_position = [442,1036]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 3:
        eb_position = [503,1032]
        screen.blit(number_eb, eb_position)
        pygame.display.update()
    if num == 2:
        eb_position = [551,1032]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 1:
        eb_position = [615,1032]
        screen.blit(eb, eb_position)
        pygame.display.update()


def feature_animation(num):
    global screen
    #if num == 6:
    #    p = [573,305]
    #    screen.blit(c, p)

    #if num == 5:
    #    p = [545,644]
    #    screen.blit(wild_pocket, p)

    #if num == 4:
    #    p = [545,743]
    #    screen.blit(wild_pocket, p)

    #if num == 3:
    #    p = [394,648]
    #    screen.blit(sc, p)
    #    p = [545,446]
    #    screen.blit(super_card, p)

    #if num == 2:
    #    p = [163,650]
    #    screen.blit(sc, p)
    #    p = [36,445]
    #    screen.blit(super_card, p)

    #if num == 1:
    #    p = [573,305]
    #    screen.blit(c, p)

    #pygame.display.update()

def odds_animation(num):
    global screen
    #if num == 5:
    #    odds_position = [24,816]
    #    screen.blit(o1, odds_position)
    #    pygame.display.update()
    #if num == 4:
    #    odds_position = [99,824]
    #    screen.blit(o2, odds_position)
    #    pygame.display.update()
    #if num == 3:
    #    odds_position = [188,834]
    #    screen.blit(o3, odds_position)
    #    pygame.display.update()
    #if num == 2:
    #    odds_position = [238,804]
    #    screen.blit(o4, odds_position)
    #    pygame.display.update()
    #if num == 1:
    #    odds_position = [289,802]
    #    screen.blit(o5, odds_position)
    #    pygame.display.update()

def blink_double(s):
    dirty_rects = []
    s.game.blink = not s.game.blink
    if s.game.blink == 1:
        blink_pos = [283,578]
        dirty_rects.append(screen.blit(blink_image, blink_pos))
        pygame.display.update(dirty_rects)
    else:
        dirty_rects.append(screen.blit(bg_gi, (283,578), pygame.Rect(283,578,164,102)))
        pygame.display.update(dirty_rects)
