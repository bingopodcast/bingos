
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
        backglass = pygame.image.load('miss_america_supreme/assets/miss_america_supreme_menu.png')
    else:
        if (s.game.anti_cheat.status == True):
            backglass = pygame.image.load('miss_america_supreme/assets/miss_america_supreme_gi.png')
        else:
            backglass = pygame.image.load('miss_america_supreme/assets/miss_america_supreme_off.png')
    backglass = pygame.transform.scale(backglass, (720, 1280))
    
    screen.blit(backglass, backglass_position)

    if s.game.rollovers.status == True and s.game.selection_feature.position >= 5:
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
        eb_position = [314,1041]
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
                p = [274,941]
                screen.blit(select_now, p)
        elif s.game.before_fifth.status == True:
            if s.game.ball_count.position == 4:
                p = [274,941]
                screen.blit(select_now, p)
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
