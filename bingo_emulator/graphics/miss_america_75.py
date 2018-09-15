
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

    if s.game.rollovers.status == True and s.game.selection_feature.position >= 5 and s.game.eb_play.status == False:
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

def line_animation(args):
    dirty_rects = []
    s = args[0]
    num = args[1]
    line = args[2]

    if line == 1:
        if s.game.line1.position == 0:
            dirty_rects.append(screen.blit(line1, (40 - num, 340)))
        elif s.game.line1.position == 1:
            dirty_rects.append(screen.blit(line1, (80 - num, 340)))
        elif s.game.line1.position == 2:
            dirty_rects.append(screen.blit(line1, (120 + num, 340)))
        elif s.game.line1.position == 3:
            dirty_rects.append(screen.blit(line1, (80 + num, 340)))

        if (s.game.anti_cheat.status == True):
            dirty_rects.append(screen.blit(bg_gi, (5,340), pygame.Rect(5,340,800,44)))
        else:
            dirty_rects.append(screen.blit(bg_off, (5,340), pygame.Rect(5,340,800,50)))

    if line == 2:
        if s.game.line2.position == 0:
             dirty_rects.append(screen.blit(line2, (40 - num, 378)))
        elif s.game.line2.position == 1:
            dirty_rects.append(screen.blit(line2, (80 - num, 378)))
        elif s.game.line2.position == 2:
            dirty_rects.append(screen.blit(line2, (120 + num, 378)))
        elif s.game.line2.position == 3:
            dirty_rects.append(screen.blit(line2, (80 + num, 378)))
        
        if (s.game.anti_cheat.status == True):
            dirty_rects.append(screen.blit(bg_gi, (5,378), pygame.Rect(5,378,800,44)))
        else:
            dirty_rects.append(screen.blit(bg_off, (5,378), pygame.Rect(5,378,800,50)))

        if s.game.corners.status == True:
            p = [10,414]
            dirty_rects.append(screen.blit(bg_gi, (10,414), pygame.Rect(10,414,81,107)))
            dirty_rects.append(screen.blit(feature, p))
        if s.game.selector.position >= 2:
            p = [632,414]
            dirty_rects.append(screen.blit(bg_gi, (632,414), pygame.Rect(632,414,81,107)))
            dirty_rects.append(screen.blit(feature, p))


    if line == 3:
        if s.game.line3.position == 0:
             dirty_rects.append(screen.blit(line3, (40 - num, 420)))
        elif s.game.line3.position == 1:
            dirty_rects.append(screen.blit(line3, (80 - num, 420)))
        elif s.game.line3.position == 2:
            dirty_rects.append(screen.blit(line3, (120 + num, 420)))
        elif s.game.line3.position == 3:
            dirty_rects.append(screen.blit(line3, (80 + num, 420)))
        
        if (s.game.anti_cheat.status == True):
            dirty_rects.append(screen.blit(bg_gi, (5,420), pygame.Rect(5,420,800,44)))
        else:
            dirty_rects.append(screen.blit(bg_off, (5,420), pygame.Rect(5,420,800,50)))

        if s.game.corners.status == True:
            p = [10,414]
            dirty_rects.append(screen.blit(bg_gi, (10,414), pygame.Rect(10,414,81,107)))
            dirty_rects.append(screen.blit(feature, p))
        if s.game.selector.position >= 2:
            p = [632,414]
            dirty_rects.append(screen.blit(bg_gi, (632,414), pygame.Rect(632,414,81,107)))
            dirty_rects.append(screen.blit(feature, p))


    if line == 4:
        if s.game.line4.position == 0:
             dirty_rects.append(screen.blit(line4, (35 - num, 455)))
        elif s.game.line4.position == 1:
            dirty_rects.append(screen.blit(line4, (75 - num, 455)))
        elif s.game.line4.position == 2:
            dirty_rects.append(screen.blit(line4, (115 + num, 455)))
        elif s.game.line4.position == 3:
            dirty_rects.append(screen.blit(line4, (75 + num, 455)))
        
        if (s.game.anti_cheat.status == True):
            dirty_rects.append(screen.blit(bg_gi, (5,455), pygame.Rect(5,455,800,44)))
        else:
            dirty_rects.append(screen.blit(bg_off, (5,455), pygame.Rect(5,455,800,50)))

        if s.game.corners.status == True:
            p = [10,414]
            dirty_rects.append(screen.blit(bg_gi, (10,414), pygame.Rect(10,414,81,107)))
            dirty_rects.append(screen.blit(feature, p))
        if s.game.selector.position >= 2:
            p = [632,414]
            dirty_rects.append(screen.blit(bg_gi, (632,414), pygame.Rect(632,414,81,107)))
            dirty_rects.append(screen.blit(feature, p))


    if line == 5:
        if s.game.line5.position == 0:
             dirty_rects.append(screen.blit(line5, (35 - num, 495)))
        elif s.game.line5.position == 1:
            dirty_rects.append(screen.blit(line5, (75 - num, 495)))
        elif s.game.line5.position == 2:
            dirty_rects.append(screen.blit(line5, (115 + num, 495)))
        elif s.game.line5.position == 3:
            dirty_rects.append(screen.blit(line5, (75 + num, 495)))
        
        if (s.game.anti_cheat.status == True):
            dirty_rects.append(screen.blit(bg_gi, (5,495), pygame.Rect(5,495,800,44)))
        else:
            dirty_rects.append(screen.blit(bg_off, (5,495), pygame.Rect(5,495,800,50)))

        if s.game.corners.status == True:
            p = [10,414]
            dirty_rects.append(screen.blit(bg_gi, (10,414), pygame.Rect(10,414,81,107)))
            dirty_rects.append(screen.blit(feature, p))
        if s.game.selector.position >= 2:
            p = [632,414]
            dirty_rects.append(screen.blit(bg_gi, (632,414), pygame.Rect(632,414,81,107)))
            dirty_rects.append(screen.blit(feature, p))


    
    pygame.display.update(dirty_rects)


def eb_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]

    if s.game.extra_ball.position < 1:
        dirty_rects.append(screen.blit(bg_gi, (155,1038), pygame.Rect(155,1038,50,33)))
    if s.game.extra_ball.position < 2:
        dirty_rects.append(screen.blit(bg_gi, (202,1038), pygame.Rect(202,1038,60,32)))
    if s.game.extra_ball.position < 3:
        dirty_rects.append(screen.blit(bg_gi, (267,1038), pygame.Rect(267,1038,60,32)))
    if s.game.extra_ball.position < 4:
        dirty_rects.append(screen.blit(bg_gi, (327,1036), pygame.Rect(327,1036,50,33)))
    if s.game.extra_ball.position < 5:
        dirty_rects.append(screen.blit(bg_gi, (378,1036), pygame.Rect(378,1036,60,32)))
    if s.game.extra_ball.position < 6:
        dirty_rects.append(screen.blit(bg_gi, (442,1036), pygame.Rect(442,1036,60,32)))
    if s.game.extra_ball.position < 7:
        dirty_rects.append(screen.blit(bg_gi, (503,1032), pygame.Rect(503,1032,50,33)))
    if s.game.extra_ball.position < 8:
        dirty_rects.append(screen.blit(bg_gi, (551,1032), pygame.Rect(551,1032,60,32)))
    if s.game.extra_ball.position < 9:
        dirty_rects.append(screen.blit(bg_gi, (615,1032), pygame.Rect(615,1032,60,32)))
    pygame.display.update(dirty_rects)

    if num in [0,24,25,14,49,50]:
        if s.game.extra_ball.position < 1:
            p = [155,1038]
            dirty_rects.append(screen.blit(number_eb, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [39,1,26,15]:
        if s.game.extra_ball.position < 2:
            p = [202,1038]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [3,4,17,28,29,40]:
        if s.game.extra_ball.position < 3:
            p = [267,1038]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [5,18,30,43]:
        if s.game.extra_ball.position < 4:
            p = [327,1036]
            dirty_rects.append(screen.blit(number_eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [7,8,19,32,33,44]:
        if s.game.extra_ball.position < 5:
            p = [378,1036]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [9,10,20,34,35,45]:
        if s.game.extra_ball.position < 6:
            p = [442,1036]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [11,21,36,46]:
        if s.game.extra_ball.position < 7:
            p = [503,1032]
            dirty_rects.append(screen.blit(number_eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [12,22,37,47]:
        if s.game.extra_ball.position < 8:
            p = [551,1032]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [2,6,13,16,23,27,31,38,41,48]:
        if s.game.extra_ball.position < 9:
            p = [615,1032]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return

def clear_odds(s, num):
    global screen

    dirty_rects = []

    if s.game.white_odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (192,968), pygame.Rect(192,968,54,64)))
    if s.game.white_odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (268,968), pygame.Rect(268,968,54,64)))
    if s.game.white_odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (340,968), pygame.Rect(340,968,54,64)))
    if s.game.white_odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (410,970), pygame.Rect(410,970,54,64)))
    if s.game.white_odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (530,970), pygame.Rect(530,970,54,64)))
    if s.game.white_odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (580,970), pygame.Rect(580,970,54,64)))

    if s.game.yellow_odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (192,848), pygame.Rect(192,848,54,64)))
    if s.game.yellow_odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (268,848), pygame.Rect(268,848,54,64)))
    if s.game.yellow_odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (410,848), pygame.Rect(410,848,54,64)))
    if s.game.yellow_odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (470,848), pygame.Rect(470,848,54,64)))
    if s.game.yellow_odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (530,848), pygame.Rect(530,848,54,64)))
    if s.game.yellow_odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (580,848), pygame.Rect(580,848,54,64)))

    if s.game.red_odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (192,786), pygame.Rect(192,786,54,64)))
    if s.game.red_odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (268,786), pygame.Rect(268,786,54,64)))
    if s.game.red_odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (340,786), pygame.Rect(340,786,54,64)))
    if s.game.red_odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (410,786), pygame.Rect(410,786,54,64)))
    if s.game.red_odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (470,786), pygame.Rect(470,786,54,64)))
    if s.game.red_odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (530,786), pygame.Rect(530,786,54,64)))

    if s.game.green_odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (192,908), pygame.Rect(192,908,54,64)))
    if s.game.green_odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (268,908), pygame.Rect(268,908,54,64)))
    if s.game.green_odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (340,908), pygame.Rect(340,908,54,64)))
    if s.game.green_odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (410,908), pygame.Rect(410,908,54,64)))
    if s.game.green_odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (470,908), pygame.Rect(470,908,54,64)))
    if s.game.green_odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (580,908), pygame.Rect(580,908,54,64)))

    pygame.display.update(dirty_rects)

def draw_odds_animation(s, num):
    global screen
    dirty_rects = []

    if num in [20,45]:
        if s.game.white_odds.position != 1:
            p = [192,968]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [12,37]:
        if s.game.white_odds.position != 2:
            p = [268,968]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [1,26]:
        if s.game.white_odds.position != 3:
            p = [340,968]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [6,31]:
        if s.game.white_odds.position != 4:
            p = [410,970]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [19,44]:
        if s.game.white_odds.position != 6:
            p = [530,970]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [18,43]:
        if s.game.white_odds.position != 7:
            p = [580,970]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return

    if num in [11,36]:
        if s.game.yellow_odds.position != 1:
            p = [192,848]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [4,29]:
        if s.game.yellow_odds.position != 2:
            p = [268,848]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [7,32]:
        if s.game.yellow_odds.position != 4:
            p = [410,848]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [13,38]:
        if s.game.yellow_odds.position != 5:
            p = [470,848]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [22,47]:
        if s.game.yellow_odds.position != 6:
            p = [530,848]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [17,42]:
        if s.game.yellow_odds.position != 7:
            p = [580,848]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return

    if num in [19,44]:
        if s.game.red_odds.position != 1:
            p = [192,786]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [5,30]:
        if s.game.red_odds.position != 2:
            p = [268,786]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [2,27]:
        if s.game.red_odds.position != 3:
            p = [340,786]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [15,40]:
        if s.game.red_odds.position != 4:
            p = [410,786]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [0,25]:
        if s.game.red_odds.position != 5:
            p = [470,786]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [9,34]:
        if s.game.red_odds.position != 6:
            p = [530,786]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return

    if num in [14,39]:
        if s.game.green_odds.position != 1:
            p = [192,908]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [3,28]:
        if s.game.green_odds.position != 2:
            p = [268,908]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [23,48]:
        if s.game.green_odds.position != 3:
            p = [340,908]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [8,33]:
        if s.game.green_odds.position != 4:
            p = [410,908]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [22,47]:
        if s.game.green_odds.position != 5:
            p = [470,908]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [10,35]:
        if s.game.green_odds.position != 7:
            p = [580,908]
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

    if s.game.before_fourth.status == False:
        dirty_rects.append(screen.blit(bg_gi, (460,694), pygame.Rect(460,694,99,47)))
    if s.game.before_fifth.status == False:
        dirty_rects.append(screen.blit(bg_gi, (575,693), pygame.Rect(575,693,99,47)))
    if not s.game.cu or s.game.rollovers.status == False:
        dirty_rects.append(screen.blit(bg_gi, (7,958), pygame.Rect(7,958,73,70)))
    if s.game.cu or s.game.rollovers.status == False:
        dirty_rects.append(screen.blit(bg_gi, (638,953), pygame.Rect(638,953,73,70)))
    if s.game.selection_feature.position < 5:
        dirty_rects.append(screen.blit(bg_gi, (206,695), pygame.Rect(206,695,43,42)))
    if s.game.selection_feature.position < 6:
        dirty_rects.append(screen.blit(bg_gi, (251,695), pygame.Rect(251,695,43,42)))
    if s.game.selection_feature.position < 7:
        dirty_rects.append(screen.blit(bg_gi, (296,695), pygame.Rect(296,695,43,42)))
    if s.game.selection_feature.position < 8:
        dirty_rects.append(screen.blit(bg_gi, (340,694), pygame.Rect(340,694,43,42)))
    if s.game.selection_feature.position < 9:
        dirty_rects.append(screen.blit(bg_gi, (385,695), pygame.Rect(385,695,43,42)))
    if s.game.corners.status == False:
        dirty_rects.append(screen.blit(bg_gi, (10,414), pygame.Rect(10,414,81,107)))
    if s.game.selector.position < 2:
        dirty_rects.append(screen.blit(bg_gi, (407,311), pygame.Rect(407,311,178,30)))
        dirty_rects.append(screen.blit(bg_gi, (632,414), pygame.Rect(632,414,81,107)))


    pygame.display.update(dirty_rects)


def draw_feature_animation(s, num):
    global screen
    dirty_rects = []

    if num in [19,34]:
        if s.game.before_fourth.status == False:
            p = [460,694]
            dirty_rects.append(screen.blit(time, p))
            pygame.display.update(dirty_rects)
            return
    if num in [17,24,42,49]:
        if s.game.before_fifth.status == False:
            p = [575,693]
            dirty_rects.append(screen.blit(time, p))
            pygame.display.update(dirty_rects)
            return
    if num in [11,25,36,0]:
        if not s.game.cu or s.game.rollovers.status == False:
            p = [7,958]
            dirty_rects.append(screen.blit(rollover, p))
            s.game.coils.yellowROLamp.pulse(85)
            pygame.display.update(dirty_rects)
            return
    if num in [10,21,25,35,46,50]:
        if s.game.cu or s.game.rollovers.status == False:
            p = [638,953]
            dirty_rects.append(screen.blit(rollover, p))
            s.game.coils.redROLamp.pulse(85)
            pygame.display.update(dirty_rects)
            return
    if num in [4,13,29,38]: 
        if s.game.selection_feature.position < 5:
            p = [206,695]
            dirty_rects.append(screen.blit(letter, p))
            p = [251,695]
            dirty_rects.append(screen.blit(letter, p))
            pygame.display.update(dirty_rects)
            return
    if num in [5,14,30,39]: 
        if s.game.selection_feature.position < 7:
            p = [296,695]
            dirty_rects.append(screen.blit(letter, p))
            pygame.display.update(dirty_rects)
            return
    if num in [6,15,31,40]:
        if s.game.selection_feature.position < 8:
            p = [340,694]
            dirty_rects.append(screen.blit(letter, p))
            pygame.display.update(dirty_rects)
            return
    if num in [7,16,32,41]:
        if s.game.selection_feature.position < 9:
            p = [385,695]
            dirty_rects.append(screen.blit(letter, p))
            pygame.display.update(dirty_rects)
            return
    if num in [2,9,22,27,34,47]:
        if s.game.corners.status == False:
            p = [10,414]
            dirty_rects.append(screen.blit(feature, p))
            pygame.display.update(dirty_rects)
            return
    if num in [3,8,12,18,23,28,33,37,43,48]:
        if s.game.selector.position < 2:
            p = [407,311]
            dirty_rects.append(screen.blit(card2, p))
            p = [632,414]
            dirty_rects.append(screen.blit(feature, p))
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
