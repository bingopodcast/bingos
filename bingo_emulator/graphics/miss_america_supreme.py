
import pygame
import random

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

meter = pygame.image.load('graphics/assets/black_register_cover.png').convert()
eb = pygame.image.load('miss_america_supreme/assets/eb.png').convert_alpha()
number_eb = pygame.image.load('miss_america_supreme/assets/eb_number.png').convert_alpha()
ebs = pygame.image.load('miss_america_supreme/assets/extra_balls.png').convert_alpha()
number = pygame.image.load('miss_america_supreme/assets/number.png').convert_alpha()
card1 = pygame.image.load('miss_america_supreme/assets/main_card.png').convert_alpha()
card2 = pygame.image.load('miss_america_supreme/assets/extra_card.png').convert_alpha()
feature = pygame.image.load('miss_america_supreme/assets/feature.png').convert_alpha()
s_letter = pygame.image.load('miss_america_supreme/assets/s_letter.png').convert_alpha()
odds = pygame.image.load('miss_america_supreme/assets/odds.png').convert_alpha()
rollover = pygame.image.load('miss_america_supreme/assets/rollovers.png').convert_alpha()
s_arrow = pygame.image.load('miss_america_supreme/assets/s_arrow.png').convert_alpha()
select_now = pygame.image.load('miss_america_supreme/assets/select_now.png').convert_alpha()
time = pygame.image.load('miss_america_supreme/assets/time.png').convert_alpha()
tilt = pygame.image.load('miss_america_supreme/assets/tilt.png').convert_alpha()
line1 = pygame.image.load('miss_america_supreme/assets/line1.png').convert_alpha()
line2 = pygame.image.load('miss_america_supreme/assets/line2.png').convert_alpha()
line3 = pygame.image.load('miss_america_supreme/assets/line3.png').convert_alpha()
line4 = pygame.image.load('miss_america_supreme/assets/line4.png').convert_alpha()
line5 = pygame.image.load('miss_america_supreme/assets/line5.png').convert_alpha()
letter1 = pygame.image.load('miss_america_supreme/assets/letter1.png').convert_alpha()
letter2 = pygame.image.load('miss_america_supreme/assets/letter2.png').convert_alpha()
letter3 = pygame.image.load('miss_america_supreme/assets/letter3.png').convert_alpha()
letter4 = pygame.image.load('miss_america_supreme/assets/letter4.png').convert_alpha()
letter5 = pygame.image.load('miss_america_supreme/assets/letter5.png').convert_alpha()
letter6 = pygame.image.load('miss_america_supreme/assets/letter6.png').convert_alpha()
letter7 = pygame.image.load('miss_america_supreme/assets/letter7.png').convert_alpha()
red_letter1 = pygame.image.load('miss_america_supreme/assets/red_letter1.png').convert_alpha()
red_letter2 = pygame.image.load('miss_america_supreme/assets/red_letter2.png').convert_alpha()
red_letter3 = pygame.image.load('miss_america_supreme/assets/red_letter3.png').convert_alpha()
red_letter4 = pygame.image.load('miss_america_supreme/assets/red_letter4.png').convert_alpha()
red_letter5 = pygame.image.load('miss_america_supreme/assets/red_letter5.png').convert_alpha()
red_letter6 = pygame.image.load('miss_america_supreme/assets/red_letter6.png').convert_alpha()
red_letter7 = pygame.image.load('miss_america_supreme/assets/red_letter7.png').convert_alpha()
red_stars = pygame.image.load('miss_america_supreme/assets/red_stars.png').convert_alpha()
red_letter_game = pygame.image.load('miss_america_supreme/assets/red_letter_game.png').convert_alpha()
four_green = pygame.image.load('miss_america_supreme/assets/four_green.png').convert_alpha()
bg_menu = pygame.image.load('miss_america_supreme/assets/miss_america_supreme_menu.png')
bg_gi = pygame.image.load('miss_america_supreme/assets/miss_america_supreme_gi.png')
bg_off = pygame.image.load('miss_america_supreme/assets/miss_america_supreme_off.png')

class scorereel():
    """ Score Reels are used to count replays """
    def __init__(self, pos, image):
        self.position = pos
        self.default_y = self.position[1]
        self.image = pygame.image.load(image).convert()

reel1 = scorereel([637,920], "graphics/assets/white_reel.png")
reel10 = scorereel([619,920], "graphics/assets/white_reel.png")
reel100 = scorereel([599,920], "graphics/assets/white_reel.png")
reel1000 = scorereel([581,920], "graphics/assets/white_reel.png")

def display(s, replays=0, menu=False):
    
    meter.set_colorkey((255,0,252))
    meter_position = [571,920]

    screen.blit(reel1.image, reel1.position)
    screen.blit(reel10.image, reel10.position)
    screen.blit(reel100.image, reel100.position)
    screen.blit(reel1000.image, reel1000.position)
    screen.blit(meter, meter_position)

    if s.game.line1.position == 0 or s.game.line1.position == 2:
        p = [80,582]
        screen.blit(line1, p)
    if s.game.line1.position == 1:
        p = [120,582]
        screen.blit(line1, p)
    if s.game.line1.position == 3:
        p = [40,582]
        screen.blit(line1, p)

    if s.game.line2.position == 0 or s.game.line2.position == 2:
        p = [76,627]
        screen.blit(line2, p)
    if s.game.line2.position == 1:
        p = [115,627]
        screen.blit(line2, p)
    if s.game.line2.position == 3:
        p = [35,627]
        screen.blit(line2, p)

    if s.game.line3.position == 0 or s.game.line3.position == 2:
        p = [80,666]
        screen.blit(line3, p)
    if s.game.line3.position == 1:
        p = [120,666]
        screen.blit(line3, p)
    if s.game.line3.position == 3:
        p = [40,666]
        screen.blit(line3, p)

    if s.game.line4.position == 0 or s.game.line4.position == 2:
        p = [75,705]
        screen.blit(line4, p)
    if s.game.line4.position == 1:
        p = [115,705]
        screen.blit(line4, p)
    if s.game.line4.position == 3:
        p = [35,705]
        screen.blit(line4, p)

    if s.game.line5.position == 0 or s.game.line5.position == 2:
        p = [75,745]
        screen.blit(line5, p)
    if s.game.line5.position == 1:
        p = [115,745]
        screen.blit(line5, p)
    if s.game.line5.position == 3:
        p = [35,745]
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
            p = [266,991]
            screen.blit(rollover, p)
        else:
            p = [389,991]
            screen.blit(rollover, p)

    if s.game.tilt.status == False:
        if s.game.red_odds.position == 1:
            p = [310,203]
            screen.blit(red_letter1, p)
        elif s.game.red_odds.position == 2:
            p = [351,203]
            screen.blit(red_letter2, p)
        elif s.game.red_odds.position == 3:
            p = [405,203]
            screen.blit(red_letter3, p)
        elif s.game.red_odds.position == 4:
            p = [441,203]
            screen.blit(red_letter4, p)
        elif s.game.red_odds.position == 5:
            p = [483,203]
            screen.blit(red_letter5, p)
        elif s.game.red_odds.position == 6:
            p = [511,203]
            screen.blit(red_letter6, p)
        elif s.game.red_odds.position == 7:
            p = [549,203]
            screen.blit(red_letter7, p)

        p = [310,203]
        screen.blit(letter1, p)
        p = [351,203]
        screen.blit(letter2, p)
        p = [405,203]
        screen.blit(letter3, p)
        p = [441,203]
        screen.blit(letter4, p)
        p = [483,203]
        screen.blit(letter5, p)
        p = [511,203]
        screen.blit(letter6, p)
        p = [549,203]
        screen.blit(letter7, p)


    if s.game.eb_play.status == True:
        ebs_position = [41,1041]
        screen.blit(ebs, ebs_position)


    if s.game.extra_ball.position >= 1:
        eb_position = [148,1041]
        screen.blit(number_eb, eb_position)
    if s.game.extra_ball.position >= 2:
        eb_position = [199,1041]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 3:
        eb_position = [261,1041]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 4:
        eb_position = [322,1041]
        screen.blit(number_eb, eb_position)
    if s.game.extra_ball.position >= 5:
        eb_position = [374,1041]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 6:
        eb_position = [437,1041]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 7:
        eb_position = [499,1041]
        screen.blit(number_eb, eb_position)
    if s.game.extra_ball.position >= 8:
        eb_position = [551,1041]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 9:
        eb_position = [614,1041]
        screen.blit(eb, eb_position)

    if s.game.red_odds.position == 1:
        odds_position = [135,271]
        screen.blit(odds, odds_position)
    if s.game.red_odds.position == 2:
        odds_position = [207,271]
        screen.blit(odds, odds_position)
    if s.game.red_odds.position == 3:
        odds_position = [281,271]
        screen.blit(odds, odds_position)
    if s.game.red_odds.position == 4:
        odds_position = [350,271]
        screen.blit(odds, odds_position)
    if s.game.red_odds.position == 5:
        odds_position = [410,271]
        screen.blit(odds, odds_position)
    if s.game.red_odds.position == 6:
        odds_position = [469,271]
        screen.blit(odds, odds_position)
    if s.game.red_odds.position == 7:
        odds_position = [521,271]
        screen.blit(odds, odds_position)

    if s.game.yellow_odds.position == 1:
        odds_position = [135,333]
        screen.blit(odds, odds_position)
    if s.game.yellow_odds.position == 2:
        odds_position = [207,333]
        screen.blit(odds, odds_position)
    if s.game.yellow_odds.position == 3:
        odds_position = [281,333]
        screen.blit(odds, odds_position)
    if s.game.yellow_odds.position == 4:
        odds_position = [350,333]
        screen.blit(odds, odds_position)
    if s.game.yellow_odds.position == 5:
        odds_position = [410,333]
        screen.blit(odds, odds_position)
    if s.game.yellow_odds.position == 6:
        odds_position = [469,333]
        screen.blit(odds, odds_position)
    if s.game.yellow_odds.position == 7:
        odds_position = [521,333]
        screen.blit(odds, odds_position)

    if s.game.green_odds.position == 1:
        odds_position = [135,397]
        screen.blit(odds, odds_position)
    if s.game.green_odds.position == 2:
        odds_position = [207,397]
        screen.blit(odds, odds_position)
    if s.game.green_odds.position == 3:
        odds_position = [281,397]
        screen.blit(odds, odds_position)
    if s.game.green_odds.position == 4:
        odds_position = [350,397]
        screen.blit(odds, odds_position)
    if s.game.green_odds.position == 5:
        odds_position = [410,397]
        screen.blit(odds, odds_position)
    if s.game.green_odds.position == 6:
        odds_position = [469,397]
        screen.blit(odds, odds_position)
    if s.game.green_odds.position == 7:
        odds_position = [521,397]
        screen.blit(odds, odds_position)

    if s.game.white_odds.position == 1:
        odds_position = [135,463]
        screen.blit(odds, odds_position)
    if s.game.white_odds.position == 2:
        odds_position = [207,463]
        screen.blit(odds, odds_position)
    if s.game.white_odds.position == 3:
        odds_position = [281,463]
        screen.blit(odds, odds_position)
    if s.game.white_odds.position == 4:
        odds_position = [350,463]
        screen.blit(odds, odds_position)
    if s.game.white_odds.position == 5:
        odds_position = [410,463]
        screen.blit(odds, odds_position)
    if s.game.white_odds.position == 6:
        odds_position = [469,463]
        screen.blit(odds, odds_position)
    if s.game.white_odds.position == 7:
        odds_position = [521,463]
        screen.blit(odds, odds_position)

    if s.game.tilt.status == False:
        if s.holes:
            if 1 in s.holes:
                if s.game.line2.position == 0 or s.game.line2.position == 2:
                    p = [203,629]
                    screen.blit(number, p)
                if s.game.line4.position == 0 or s.game.line4.position == 2:
                    p = [401,708]
                    screen.blit(number, p)
                if s.game.line2.position == 1:
                    p = [243,629]
                    screen.blit(number, p)
                if s.game.line4.position == 1:
                    p = [440,708]
                    screen.blit(number, p)
                if s.game.line2.position == 3:
                    p = [164,629]
                    screen.blit(number, p)
                if s.game.line4.position == 3:
                    p = [283,708]
                    screen.blit(number, p)
            if 2 in s.holes:
                if s.game.line2.position == 0 or s.game.line2.position == 2:
                    p = [124,627]
                    screen.blit(number, p)
                if s.game.line1.position == 0 or s.game.line1.position == 2:
                    p = [557,589]
                    screen.blit(number, p)
                if s.game.line2.position == 1:
                    p = [163,627]
                    screen.blit(number, p)
                if s.game.line1.position == 1:
                    p = [125,589]
                    screen.blit(number, p)
                if s.game.line2.position == 3:
                    p = [558,627]
                    screen.blit(number, p)
                if s.game.line1.position == 3:
                    p = [518,589]
                    screen.blit(number, p)
            if 3 in s.holes:
                if s.game.line3.position == 0 or s.game.line3.position == 2:
                    p = [282,668]
                    screen.blit(number, p)
                if s.game.line4.position == 0 or s.game.line4.position == 2:
                    p = [558,708]
                    screen.blit(number, p)
                if s.game.line3.position == 1:
                    p = [402,668]
                    screen.blit(number, p)
                if s.game.line4.position == 1:
                    p = [123,708]
                    screen.blit(number, p)
                if s.game.line3.position == 3:
                    p = [243,668]
                    screen.blit(number, p)
                if s.game.line4.position == 3:
                    p = [520,708]
                    screen.blit(number, p)
            if 4 in s.holes:
                if s.game.line5.position == 0 or s.game.line5.position == 2:
                    p = [163,747]
                    screen.blit(number, p)
                    p = [559,747]
                    screen.blit(number, p)
                if s.game.line5.position == 1:
                    p = [204,747]
                    screen.blit(number, p)
                    p = [123,747]
                    screen.blit(number, p)
                if s.game.line5.position == 3:
                    p = [123,747]
                    screen.blit(number, p)
                    p = [520,747]
                    screen.blit(number, p)
            if 5 in s.holes:
                if s.game.line1.position == 0 or s.game.line1.position == 2:
                    p = [125,588]
                    screen.blit(number, p)
                if s.game.line5.position == 0 or s.game.line5.position == 2:
                    p = [520,747]
                    screen.blit(number, p)
                if s.game.line1.position == 1:
                    p = [164,588]
                    screen.blit(number, p)
                if s.game.line5.position == 1:
                    p = [558,747]
                    screen.blit(number, p)
                if s.game.line1.position == 3:
                    p = [558,588]
                    screen.blit(number, p)
                if s.game.line5.position == 3:
                    p = [480,747]
                    screen.blit(number, p)
            if 6 in s.holes:
                if s.game.line1.position == 0 or s.game.line1.position == 2:
                    p = [244,588]
                    screen.blit(number, p)
                    p = [402,588]
                    screen.blit(number, p)
                if s.game.line1.position == 1:
                    p = [283,588]
                    screen.blit(number, p)
                    p = [441,588]
                    screen.blit(number, p)
                if s.game.line1.position == 3:
                    p = [205,588]
                    screen.blit(number, p)
                    p = [283,588]
                    screen.blit(number, p)
            if 7 in s.holes:
                if s.game.line2.position == 0 or s.game.line2.position == 2:
                    p = [556,629]
                    screen.blit(number, p)
                if s.game.line4.position == 0 or s.game.line4.position == 2:
                    p = [282,707]
                    screen.blit(number, p)
                if s.game.line2.position == 1:
                    p = [124,628]
                    screen.blit(number, p)
                if s.game.line4.position == 1:
                    p = [400,707]
                    screen.blit(number, p)
                if s.game.line2.position == 3:
                    p = [518,629]
                    screen.blit(number, p)
                if s.game.line4.position == 3:
                    p = [242,707]
                    screen.blit(number, p)
            if 8 in s.holes:
                if s.game.line1.position == 0 or s.game.line1.position == 2:
                    p = [205,589]
                    screen.blit(number, p)
                    p = [441,589]
                    screen.blit(number, p)
                if s.game.line1.position == 1:
                    p = [244,589]
                    screen.blit(number, p)
                    p = [479,589]
                    screen.blit(number, p)
                if s.game.line1.position == 3:
                    p = [165,589]
                    screen.blit(number, p)
                    p = [401,589]
                    screen.blit(number, p)
            if 9 in s.holes:
                if s.game.line3.position == 0 or s.game.line3.position == 2:
                    p = [163,669]
                    screen.blit(number, p)
                if s.game.line5.position == 0 or s.game.line5.position == 2:
                    p = [478,747]
                    screen.blit(number, p)
                if s.game.line3.position == 1:
                    p = [202,669]
                    screen.blit(number, p)
                if s.game.line5.position == 1:
                    p = [518,747]
                    screen.blit(number, p)
                if s.game.line3.position == 3:
                    p = [124,669]
                    screen.blit(number, p)
                if s.game.line5.position == 3:
                    p = [438,747]
                    screen.blit(number, p)
            if 10 in s.holes:
                if s.game.line1.position == 0 or s.game.line1.position == 2:
                    p = [519,588]
                    screen.blit(number, p)
                if s.game.line5.position == 0 or s.game.line5.position == 2:
                    p = [204,747]
                    screen.blit(number, p)
                if s.game.line1.position == 1:
                    p = [558,588]
                    screen.blit(number, p)
                if s.game.line5.position == 1:
                    p = [243,747]
                    screen.blit(number, p)
                if s.game.line1.position == 3:
                    p = [480,588]
                    screen.blit(number, p)
                if s.game.line5.position == 3:
                    p = [164,747]
                    screen.blit(number, p)
            if 11 in s.holes:
                if s.game.line1.position == 0 or s.game.line1.position == 2:
                    p = [480,588]
                    screen.blit(number, p)
                if s.game.line5.position == 0 or s.game.line5.position == 2:
                    p = [243,747]
                    screen.blit(number, p)
                if s.game.line1.position == 1:
                    p = [519,588]
                    screen.blit(number, p)
                if s.game.line5.position == 1:
                    p = [283,747]
                    screen.blit(number, p)
                if s.game.line1.position == 3:
                    p = [441,588]
                    screen.blit(number, p)
                if s.game.line5.position == 3:
                    p = [204,747]
                    screen.blit(number, p)
            if 12 in s.holes:
                if s.game.line3.position == 0 or s.game.line3.position == 2:
                    p = [243,668]
                    screen.blit(number, p)
                if s.game.line4.position == 0 or s.game.line4.position == 2:
                    p = [481,707]
                    screen.blit(number, p)
                if s.game.line3.position == 1:
                    p = [283,668]
                    screen.blit(number, p)
                if s.game.line4.position == 1:
                    p = [520,707]
                    screen.blit(number, p)
                if s.game.line3.position == 3:
                    p = [203,668]
                    screen.blit(number, p)
                if s.game.line4.position == 3:
                    p = [441,707]
                    screen.blit(number, p)
            if 13 in s.holes:
                if s.game.line2.position == 0 or s.game.line2.position == 2:
                    p = [283,628]
                    screen.blit(number, p)
                if s.game.line5.position == 0 or s.game.line5.position == 2:
                    p = [441,747]
                    screen.blit(number, p)
                if s.game.line2.position == 1:
                    p = [401,628]
                    screen.blit(number, p)
                if s.game.line5.position == 1:
                    p = [480,747]
                    screen.blit(number, p)
                if s.game.line2.position == 3:
                    p = [243,628]
                    screen.blit(number, p)
                if s.game.line5.position == 3:
                    p = [401,747]
                    screen.blit(number, p)
            if 14 in s.holes:
                if s.game.line1.position == 0 or s.game.line1.position == 2:
                    p = [165,588]
                    screen.blit(number, p)
                if s.game.line2.position == 0 or s.game.line2.position == 2:
                    p = [402,628]
                    screen.blit(number, p)
                if s.game.line1.position == 1:
                    p = [205,588]
                    screen.blit(number, p)
                if s.game.line2.position == 1:
                    p = [441,628]
                    screen.blit(number, p)
                if s.game.line1.position == 3:
                    p = [125,588]
                    screen.blit(number, p)
                if s.game.line2.position == 3:
                    p = [283,628]
                    screen.blit(number, p)
            if 15 in s.holes:
                if s.game.line3.position == 0 or s.game.line3.position == 2:
                    p = [399,669]
                    screen.blit(number, p)
                if s.game.line5.position == 0 or s.game.line5.position == 2:
                    p = [123,746]
                    screen.blit(number, p)
                if s.game.line3.position == 1:
                    p = [438,669]
                    screen.blit(number, p)
                if s.game.line5.position == 1:
                    p = [163,746]
                    screen.blit(number, p)
                if s.game.line3.position == 3:
                    p = [281,669]
                    screen.blit(number, p)
                if s.game.line5.position == 3:
                    p = [555,746]
                    screen.blit(number, p)
            if 16 in s.holes:
                if s.game.line3.position == 0 or s.game.line3.position == 2:
                    p = [480,668]
                    screen.blit(number, p)
                if s.game.line4.position == 0 or s.game.line4.position == 2:
                    p = [125,705]
                    screen.blit(number, p)
                if s.game.line3.position == 1:
                    p = [520,668]
                    screen.blit(number, p)
                if s.game.line4.position == 1:
                    p = [163,705]
                    screen.blit(number, p)
                if s.game.line3.position == 3:
                    p = [442,668]
                    screen.blit(number, p)
                if s.game.line4.position == 3:
                    p = [559,705]
                    screen.blit(number, p)
            if 17 in s.holes:
                if s.game.line3.position == 0 or s.game.line3.position == 2:
                    p = [203,668]
                    screen.blit(number, p)
                    p = [520,668]
                    screen.blit(number, p)
                if s.game.line3.position == 1:
                    p = [244,668]
                    screen.blit(number, p)
                    p = [558,668]
                    screen.blit(number, p)
                if s.game.line3.position == 3:
                    p = [163,668]
                    screen.blit(number, p)
                    p = [480,668]
                    screen.blit(number, p)
            if 18 in s.holes:
                if s.game.line3.position == 0 or s.game.line3.position == 2:
                    p = [441,668]
                    screen.blit(number, p)
                if s.game.line4.position == 0 or s.game.line4.position == 2:
                    p = [204,707]
                    screen.blit(number, p)
                if s.game.line3.position == 1:
                    p = [481,668]
                    screen.blit(number, p)
                if s.game.line4.position == 1:
                    p = [243,707]
                    screen.blit(number, p)
                if s.game.line3.position == 3:
                    p = [402,668]
                    screen.blit(number, p)
                if s.game.line4.position == 3:
                    p = [163,707]
                    screen.blit(number, p)
            if 19 in s.holes:
                if s.game.line2.position == 0 or s.game.line2.position == 2:
                    p = [163,628]
                    screen.blit(number, p)
                    p = [441,628]
                    screen.blit(number, p)
                if s.game.line2.position == 1:
                    p = [204,628]
                    screen.blit(number, p)
                    p = [481,628]
                    screen.blit(number, p)
                if s.game.line2.position == 3:
                    p = [124,628]
                    screen.blit(number, p)
                    p = [402,628]
                    screen.blit(number, p)
            if 20 in s.holes:
                if s.game.line2.position == 0 or s.game.line2.position == 2:
                    p = [243,629]
                    screen.blit(number, p)
                if s.game.line4.position == 0 or s.game.line4.position == 2:
                    p = [441,707]
                    screen.blit(number, p)
                if s.game.line2.position == 1:
                    p = [284,629]
                    screen.blit(number, p)
                if s.game.line4.position == 1:
                    p = [480,707]
                    screen.blit(number, p)
                if s.game.line2.position == 3:
                    p = [204,629]
                    screen.blit(number, p)
                if s.game.line4.position == 3:
                    p = [401,707]
                    screen.blit(number, p)
            if 21 in s.holes:
                if s.game.line4.position == 0 or s.game.line4.position == 2:
                    p = [243,707]
                    screen.blit(number, p)
                    p = [521,707]
                    screen.blit(number, p)
                if s.game.line4.position == 1:
                    p = [284,707]
                    screen.blit(number, p)
                    p = [559,707]
                    screen.blit(number, p)
                if s.game.line4.position == 3:
                    p = [204,707]
                    screen.blit(number, p)
                    p = [480,707]
                    screen.blit(number, p)
            if 22 in s.holes:
                if s.game.line2.position == 0 or s.game.line2.position == 2:
                    p = [519,628]
                    screen.blit(number, p)
                if s.game.line4.position == 0 or s.game.line4.position == 2:
                    p = [163,707]
                    screen.blit(number, p)
                if s.game.line2.position == 1:
                    p = [559,628]
                    screen.blit(number, p)
                if s.game.line4.position == 1:
                    p = [204,707]
                    screen.blit(number, p)
                if s.game.line2.position == 3:
                    p = [481,628]
                    screen.blit(number, p)
                if s.game.line4.position == 3:
                    p = [124,707]
                    screen.blit(number, p)
            if 23 in s.holes:
                if s.game.line2.position == 0 or s.game.line2.position == 2:
                    p = [481,628]
                    screen.blit(number, p)
                if s.game.line3.position == 0 or s.game.line3.position == 2:
                    p = [123,668]
                    screen.blit(number, p)
                if s.game.line2.position == 1:
                    p = [520,628]
                    screen.blit(number, p)
                if s.game.line3.position == 1:
                    p = [163,668]
                    screen.blit(number, p)
                if s.game.line2.position == 3:
                    p = [441,628]
                    screen.blit(number, p)
                if s.game.line3.position == 3:
                    p = [557,668]
                    screen.blit(number, p)
            if 24 in s.holes:
                if s.game.line5.position == 0 or s.game.line5.position == 2:
                    p = [283,747]
                    screen.blit(number, p)
                    p = [402,747]
                    screen.blit(number, p)
                if s.game.line5.position == 1:
                    p = [402,747]
                    screen.blit(number, p)
                    p = [441,747]
                    screen.blit(number, p)
                if s.game.line5.position == 3:
                    p = [243,747]
                    screen.blit(number, p)
                    p = [283,747]
                    screen.blit(number, p)
            if 25 in s.holes:
                if s.game.line1.position == 0 or s.game.line1.position == 2:
                    p = [284,589]
                    screen.blit(number, p)
                if s.game.line3.position == 0 or s.game.line3.position == 2:
                    p = [559,669]
                    screen.blit(number, p)
                if s.game.line1.position == 1:
                    p = [402,589]
                    screen.blit(number, p)
                if s.game.line3.position == 1:
                    p = [125,669]
                    screen.blit(number, p)
                if s.game.line1.position == 3:
                    p = [244,589]
                    screen.blit(number, p)
                if s.game.line3.position == 3:
                    p = [521,669]
                    screen.blit(number, p)

    if s.game.tilt.status == True:
        tilt_position = [36,1005]
        screen.blit(tilt, tilt_position)

    if s.game.corners.status == True:
        p = [9,644]
        screen.blit(feature, p)

    if s.game.selector.position >= 1:
        p = [159,526]
        screen.blit(card1, p)
    if s.game.selector.position >= 2:
        p = [407,525]
        screen.blit(card2, p)
        p = [630,644]
        screen.blit(feature, p)

    if s.game.selection_feature.position >= 5:
        if s.game.before_fourth.status == True:
            p = [252,888]
            screen.blit(time, p)
        if s.game.before_fifth.status == True:
            p = [368,888]
            screen.blit(time, p)

    if s.game.selection_feature.position == 1:
        p = [158,842]
        screen.blit(s_arrow, p)
    if s.game.selection_feature.position == 2:
        p = [202,842]
        screen.blit(s_arrow, p)
    if s.game.selection_feature.position == 3:
        p = [247,842]
        screen.blit(s_arrow, p)
    if s.game.selection_feature.position == 4:
        p = [291,842]
        screen.blit(s_arrow, p)
    if s.game.selection_feature.position >= 5:
        p = [335,842]
        screen.blit(s_letter, p)
    if s.game.selection_feature.position >= 6:
        p = [378,842]
        screen.blit(s_letter, p)
    if s.game.selection_feature.position >= 7:
        p = [424,842]
        screen.blit(s_letter, p)
    if s.game.selection_feature.position >= 8:
        p = [467,842]
        screen.blit(s_letter, p)
    if s.game.selection_feature.position >= 9:
        p = [512,842]
        screen.blit(s_letter, p)

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
    if s.game.selector.position >= 2:
        if s.game.red_letter_two.status == True:
            p = [11,916]
            screen.blit(red_stars, p)
            p = [10,957]
            screen.blit(red_letter_game, p)
        if s.game.red_letter_three.status == True:
            p = [84, 916]
            screen.blit(red_stars, p)
            p = [10,957]
            screen.blit(red_letter_game, p)

        if s.game.green_corners.status == True:
            p = [7,830]
            screen.blit(four_green, p)

    pygame.display.update()

def blink(args):
    dirty_rects = []
    s = args[0]
    b = args[1]
    sn = args[2]

    if b == 0:
        if sn == 1:
            p = [274,941]
            dirty_rects.append(screen.blit(select_now, p))
        pygame.display.update(dirty_rects)
    else:
        dirty_rects.append(screen.blit(bg_gi, (274,941), pygame.Rect(274,941,172,34)))
        pygame.display.update(dirty_rects)
    b = not b

    args = [s,b,sn]

    s.delay(name="blink", delay=0.1, handler=blink, param=args)

def line_animation(args):
    dirty_rects = []
    s = args[0]
    num = args[1]
    line = args[2]

    if line == 1:
        if s.game.line1.position == 0:
            dirty_rects.append(screen.blit(line1, (40 - num, 582)))
        elif s.game.line1.position == 1:
            dirty_rects.append(screen.blit(line1, (80 - num, 582)))
        elif s.game.line1.position == 2:
            dirty_rects.append(screen.blit(line1, (120 + num, 582)))
        elif s.game.line1.position == 3:
            dirty_rects.append(screen.blit(line1, (80 + num, 582)))

        if (s.game.anti_cheat.status == True):
            dirty_rects.append(screen.blit(bg_gi, (5,582), pygame.Rect(5,582,800,44)))
        else:
            dirty_rects.append(screen.blit(bg_off, (5,582), pygame.Rect(5,582,800,50)))

        if s.game.corners.status == True:
            p = [9,644]
            dirty_rects.append(screen.blit(bg_gi, (9,644), pygame.Rect(9,644,80,108)))
            dirty_rects.append(screen.blit(feature, p))

        if s.game.selector.position >= 2:
            p = [630,644]
            dirty_rects.append(screen.blit(bg_gi, (630,644), pygame.Rect(630,644,80,108)))
            dirty_rects.append(screen.blit(feature, p))

    if line == 2:
        if s.game.line2.position == 0:
             dirty_rects.append(screen.blit(line2, (35 - num, 627)))
        elif s.game.line2.position == 1:
            dirty_rects.append(screen.blit(line2, (76 - num, 627)))
        elif s.game.line2.position == 2:
            dirty_rects.append(screen.blit(line2, (115 + num, 627)))
        elif s.game.line2.position == 3:
            dirty_rects.append(screen.blit(line2, (76 + num, 627)))
        
        if (s.game.anti_cheat.status == True):
            dirty_rects.append(screen.blit(bg_gi, (5,627), pygame.Rect(5,627,800,44)))
        else:
            dirty_rects.append(screen.blit(bg_off, (5,627), pygame.Rect(5,627,800,50)))

        if s.game.corners.status == True:
            p = [9,644]
            dirty_rects.append(screen.blit(bg_gi, (9,644), pygame.Rect(9,644,80,108)))
            dirty_rects.append(screen.blit(feature, p))

        if s.game.selector.position >= 2:
            p = [630,644]
            dirty_rects.append(screen.blit(bg_gi, (630,644), pygame.Rect(630,644,80,108)))
            dirty_rects.append(screen.blit(feature, p))

    if line == 3:
        if s.game.line3.position == 0:
             dirty_rects.append(screen.blit(line3, (40 - num, 666)))
        elif s.game.line3.position == 1:
            dirty_rects.append(screen.blit(line3, (80 - num, 666)))
        elif s.game.line3.position == 2:
            dirty_rects.append(screen.blit(line3, (120 + num, 666)))
        elif s.game.line3.position == 3:
            dirty_rects.append(screen.blit(line3, (80 + num, 666)))
        
        if (s.game.anti_cheat.status == True):
            dirty_rects.append(screen.blit(bg_gi, (5,666), pygame.Rect(5,666,800,44)))
        else:
            dirty_rects.append(screen.blit(bg_off, (5,666), pygame.Rect(5,666,800,50)))

        if s.game.corners.status == True:
            p = [9,644]
            dirty_rects.append(screen.blit(bg_gi, (9,644), pygame.Rect(9,644,80,108)))
            dirty_rects.append(screen.blit(feature, p))

        if s.game.selector.position >= 2:
            p = [630,644]
            dirty_rects.append(screen.blit(bg_gi, (630,644), pygame.Rect(630,644,80,108)))
            dirty_rects.append(screen.blit(feature, p))

    if line == 4:
        if s.game.line4.position == 0:
             dirty_rects.append(screen.blit(line4, (35 - num, 705)))
        elif s.game.line4.position == 1:
            dirty_rects.append(screen.blit(line4, (75 - num, 705)))
        elif s.game.line4.position == 2:
            dirty_rects.append(screen.blit(line4, (115 + num, 705)))
        elif s.game.line4.position == 3:
            dirty_rects.append(screen.blit(line4, (75 + num, 705)))
        
        if (s.game.anti_cheat.status == True):
            dirty_rects.append(screen.blit(bg_gi, (5,705), pygame.Rect(5,705,800,44)))
        else:
            dirty_rects.append(screen.blit(bg_off, (5,705), pygame.Rect(5,705,800,50)))

        if s.game.corners.status == True:
            p = [9,644]
            dirty_rects.append(screen.blit(bg_gi, (9,644), pygame.Rect(9,644,80,108)))
            dirty_rects.append(screen.blit(feature, p))

        if s.game.selector.position >= 2:
            p = [630,644]
            dirty_rects.append(screen.blit(bg_gi, (630,644), pygame.Rect(630,644,80,108)))
            dirty_rects.append(screen.blit(feature, p))

    if line == 5:
        if s.game.line5.position == 0:
             dirty_rects.append(screen.blit(line5, (35 - num, 745)))
        elif s.game.line5.position == 1:
            dirty_rects.append(screen.blit(line5, (75 - num, 745)))
        elif s.game.line5.position == 2:
            dirty_rects.append(screen.blit(line5, (115 + num, 745)))
        elif s.game.line5.position == 3:
            dirty_rects.append(screen.blit(line5, (75 + num, 745)))
        
        if (s.game.anti_cheat.status == True):
            dirty_rects.append(screen.blit(bg_gi, (5,745), pygame.Rect(5,745,800,44)))
        else:
            dirty_rects.append(screen.blit(bg_off, (5,745), pygame.Rect(5,745,800,50)))

        if s.game.corners.status == True:
            p = [9,644]
            dirty_rects.append(screen.blit(bg_gi, (9,644), pygame.Rect(9,644,80,108)))
            dirty_rects.append(screen.blit(feature, p))

        if s.game.selector.position >= 2:
            p = [630,644]
            dirty_rects.append(screen.blit(bg_gi, (630,644), pygame.Rect(630,644,80,108)))
            dirty_rects.append(screen.blit(feature, p))

    pygame.display.update(dirty_rects)



def eb_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]

    if s.game.extra_ball.position < 1:
        dirty_rects.append(screen.blit(bg_gi, (148,1041), pygame.Rect(148,1041,48,33)))
    if s.game.extra_ball.position < 2:
        dirty_rects.append(screen.blit(bg_gi, (199,1041), pygame.Rect(199,1041,57,33)))
    if s.game.extra_ball.position < 3:
        dirty_rects.append(screen.blit(bg_gi, (261,1041), pygame.Rect(261,1041,57,33)))
    if s.game.extra_ball.position < 4:
        dirty_rects.append(screen.blit(bg_gi, (322,1041), pygame.Rect(322,1041,48,33)))
    if s.game.extra_ball.position < 5:
        dirty_rects.append(screen.blit(bg_gi, (374,1041), pygame.Rect(374,1041,57,33)))
    if s.game.extra_ball.position < 6:
        dirty_rects.append(screen.blit(bg_gi, (437,1041), pygame.Rect(437,1041,57,33)))
    if s.game.extra_ball.position < 7:
        dirty_rects.append(screen.blit(bg_gi, (499,1041), pygame.Rect(499,1041,48,33)))
    if s.game.extra_ball.position < 8:
        dirty_rects.append(screen.blit(bg_gi, (551,1041), pygame.Rect(551,1041,57,33)))
    if s.game.extra_ball.position < 9:
        dirty_rects.append(screen.blit(bg_gi, (614,1041), pygame.Rect(614,1041,57,33)))
    pygame.display.update(dirty_rects)

    if num in [0,24,25,14,49,50]:
        if s.game.extra_ball.position < 1:
            p = [148,1041]
            dirty_rects.append(screen.blit(number_eb, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [39,1,26,15]:
        if s.game.extra_ball.position < 2:
            p = [199,1041]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [3,4,17,28,29,40]:
        if s.game.extra_ball.position < 3:
            p = [261,1041]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [5,18,30,43]:
        if s.game.extra_ball.position < 4:
            p = [322,1041]
            dirty_rects.append(screen.blit(number_eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [7,8,19,32,33,44]:
        if s.game.extra_ball.position < 5:
            p = [374,1041]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [9,10,20,34,35,45]:
        if s.game.extra_ball.position < 6:
            p = [437,1041]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [11,21,36,46]:
        if s.game.extra_ball.position < 7:
            p = [499,1041]
            dirty_rects.append(screen.blit(number_eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [12,22,37,47]:
        if s.game.extra_ball.position < 8:
            p = [551,1041]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [2,6,13,16,23,27,31,38,41,48]:
        if s.game.extra_ball.position < 9:
            p = [614,1041]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return

def clear_odds(s, num):
    global screen

    dirty_rects = []

    if s.game.white_odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (207,463), pygame.Rect(207,463,58,64)))
    if s.game.white_odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (281,463), pygame.Rect(281,463,58,64)))
    if s.game.white_odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (350,463), pygame.Rect(350,463,58,64)))
    if s.game.white_odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (469,463), pygame.Rect(469,463,58,64)))
    if s.game.white_odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (521,463), pygame.Rect(521,463,58,64)))

    if s.game.yellow_odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (207,333), pygame.Rect(207,333,58,64)))
    if s.game.yellow_odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (350,333), pygame.Rect(350,333,58,64)))
    if s.game.yellow_odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (410,333), pygame.Rect(410,333,58,64)))
    if s.game.yellow_odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (469,333), pygame.Rect(469,333,58,64)))
    if s.game.yellow_odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (521,333), pygame.Rect(521,333,58,64)))

    if s.game.red_odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (207,271), pygame.Rect(207,271,58,64)))
    if s.game.red_odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (281,271), pygame.Rect(281,271,58,64)))
    if s.game.red_odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (350,271), pygame.Rect(350,271,58,64)))
    if s.game.red_odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (410,271), pygame.Rect(410,271,58,64)))
    if s.game.red_odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (469,271), pygame.Rect(469,271,58,64)))

    if s.game.green_odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (135,397), pygame.Rect(135,397,58,64)))
    if s.game.green_odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (281,397), pygame.Rect(281,397,58,64)))
    if s.game.green_odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (350,397), pygame.Rect(350,397,58,64)))
    if s.game.green_odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (410,397), pygame.Rect(410,397,58,64)))
    if s.game.green_odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (521,397), pygame.Rect(521,397,58,64)))

    pygame.display.update(dirty_rects)

def draw_odds_animation(s, num):
    global screen
    dirty_rects = []

    if num in [12,37]:
        if s.game.white_odds.position != 2:
            p = [207,463]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [1,26]:
        if s.game.white_odds.position != 3:
            p = [281,463]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [6,31]:
        if s.game.white_odds.position != 4:
            p = [350,463]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [16,41]:
        if s.game.white_odds.position != 6:
            p = [469,463]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [18,43]:
        if s.game.white_odds.position != 7:
            p = [521,463]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return

    if num in [4,29]:
        if s.game.yellow_odds.position != 2:
            p = [207,333]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [7,32]:
        if s.game.yellow_odds.position != 4:
            p = [350,333]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [13,38]:
        if s.game.yellow_odds.position != 5:
            p = [410,333]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [22,47]:
        if s.game.yellow_odds.position != 6:
            p = [469,333]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [17,42]:
        if s.game.yellow_odds.position != 7:
            p = [521,333]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return

    if num in [5,30]:
        if s.game.red_odds.position != 2:
            p = [207,271]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [2,27]:
        if s.game.red_odds.position != 3:
            p = [281,271]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [15,40]:
        if s.game.red_odds.position != 4:
            p = [350,271]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [0,25]:
        if s.game.red_odds.position != 5:
            p = [410,271]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [9,34]:
        if s.game.red_odds.position != 6:
            p = [469,271]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return

    if num in [14,39]:
        if s.game.green_odds.position != 1:
            p = [135,397]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [23,48]:
        if s.game.green_odds.position != 3:
            p = [281,397]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [8,33]:
        if s.game.green_odds.position != 4:
            p = [350,397]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [21,46]:
        if s.game.green_odds.position != 5:
            p = [410,397]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [10,35]:
        if s.game.green_odds.position != 7:
            p = [521,397]
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
        dirty_rects.append(screen.blit(bg_gi, (252,888), pygame.Rect(252,888,100,48)))
    if s.game.before_fifth.status == False:
        dirty_rects.append(screen.blit(bg_gi, (368,888), pygame.Rect(368,888,100,48)))
    if not s.game.cu or s.game.rollovers.status == False:
        dirty_rects.append(screen.blit(bg_gi, (266,991), pygame.Rect(266,991,59,47)))
    if s.game.cu or s.game.rollovers.status == False:
        dirty_rects.append(screen.blit(bg_gi, (389,991), pygame.Rect(389,991,59,47)))
    if s.game.selection_feature.position < 5:
        dirty_rects.append(screen.blit(bg_gi, (335,842), pygame.Rect(335,842,39,39)))
    if s.game.selection_feature.position < 6:
        dirty_rects.append(screen.blit(bg_gi, (378,842), pygame.Rect(378,842,39,39)))
    if s.game.selection_feature.position < 7:
        dirty_rects.append(screen.blit(bg_gi, (424,842), pygame.Rect(424,842,39,39)))
    if s.game.selection_feature.position < 8:
        dirty_rects.append(screen.blit(bg_gi, (467,842), pygame.Rect(467,842,39,39)))
    if s.game.selection_feature.position < 9:
        dirty_rects.append(screen.blit(bg_gi, (512,842), pygame.Rect(512,842,39,39)))
    if s.game.selector.position < 2:
        dirty_rects.append(screen.blit(bg_gi, (407,525), pygame.Rect(407,525,158,44)))
        dirty_rects.append(screen.blit(bg_gi, (630,644), pygame.Rect(630,644,80,108)))
        
    if s.game.red_letter_three.status == False:
        dirty_rects.append(screen.blit(bg_gi, (84,916), pygame.Rect(84,916,72,41)))
    if s.game.red_letter_two.status == False:
        dirty_rects.append(screen.blit(bg_gi, (11,916), pygame.Rect(11,916,72,41)))
    if s.game.corners.status == False:
        dirty_rects.append(screen.blit(bg_gi, (9,644), pygame.Rect(9,644,80,108)))
    if s.game.green_corners.status == False:
        dirty_rects.append(screen.blit(bg_gi, (7,830), pygame.Rect(7,830,124,64)))

    pygame.display.update(dirty_rects)


def draw_feature_animation(s, num):
    global screen
    dirty_rects = []

    if num in [19,34]:
        if s.game.before_fourth.status == False:
            p = [252,888]
            dirty_rects.append(screen.blit(time, p))
            pygame.display.update(dirty_rects)
            return
    if num in [17,24,42,49]:
        if s.game.before_fifth.status == False:
            p = [368,888]
            dirty_rects.append(screen.blit(time, p))
            pygame.display.update(dirty_rects)
            return
    if num in [11,25,36,0]:
        if not s.game.cu or s.game.rollovers.status == False:
            p = [266,991]
            dirty_rects.append(screen.blit(rollover, p))
            s.game.coils.yellowROLamp.pulse(85)
            pygame.display.update(dirty_rects)
            return
    if num in [10,21,25,35,46,50]:
        if s.game.cu or s.game.rollovers.status == False:
            p = [389,991]
            dirty_rects.append(screen.blit(rollover, p))
            s.game.coils.redROLamp.pulse(85)
            pygame.display.update(dirty_rects)
            return
    if num in [4,13,29,38]: 
        if s.game.selection_feature.position < 5:
            p = [335,842]
            dirty_rects.append(screen.blit(s_letter, p))
            p = [378,842]
            dirty_rects.append(screen.blit(s_letter, p))
            pygame.display.update(dirty_rects)
            return
    if num in [5,14,30,39]: 
        if s.game.selection_feature.position < 7:
            p = [424,842]
            dirty_rects.append(screen.blit(s_letter, p))
            pygame.display.update(dirty_rects)
            return
    if num in [6,15,31,40]:
        if s.game.selection_feature.position < 8:
            p = [467,842]
            dirty_rects.append(screen.blit(s_letter, p))
            pygame.display.update(dirty_rects)
            return
    if num in [7,16,32,41]:
        if s.game.selection_feature.position < 9:
            p = [512,842]
            dirty_rects.append(screen.blit(s_letter, p))
            pygame.display.update(dirty_rects)
            return
    if num in [2,9,22,27,34,47]:
        if s.game.corners.status == False:
            p = [9,644]
            dirty_rects.append(screen.blit(feature, p))
            pygame.display.update(dirty_rects)
            return
    if num in [3,8,12,18,23,28,33,37,43,48]:
        if s.game.selector.position < 2:
            p = [407,525]
            dirty_rects.append(screen.blit(card2, p))
            p = [630,644]
            dirty_rects.append(screen.blit(feature, p))
            pygame.display.update(dirty_rects)
            return
    if num in [3,11,28,36]:
        if s.game.red_letter_three.status == False:
            p = [84,916]
            dirty_rects.append(screen.blit(red_stars, p))
            pygame.display.update(dirty_rects)
            return
    if num in [20,45]:
        if s.game.red_letter_two.status == False:
            p = [11,916]
            dirty_rects.append(screen.blit(red_stars, p))
            pygame.display.update(dirty_rects)
            return
    if num in [19,44]:
        if s.game.green_corners.status == False:
            p = [7,830]
            dirty_rects.append(screen.blit(four_green, p))
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
