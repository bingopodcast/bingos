
import pygame
import random

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

meter = pygame.image.load('graphics/assets/silver_register_cover.png').convert()
eb = pygame.image.load('brazil/assets/eb.png').convert_alpha()
extra_ball = pygame.image.load('brazil/assets/extra_ball.png').convert_alpha()
extra_balls = pygame.image.load('brazil/assets/extra_balls.png').convert_alpha()
o1 = pygame.image.load('brazil/assets/odds1.png').convert_alpha()
o2 = pygame.image.load('brazil/assets/odds2.png').convert_alpha()
o3 = pygame.image.load('brazil/assets/odds3.png').convert_alpha()
o4 = pygame.image.load('brazil/assets/odds4.png').convert_alpha()
o5 = pygame.image.load('brazil/assets/odds5.png').convert_alpha()
o6 = pygame.image.load('brazil/assets/odds6.png').convert_alpha()
o7 = pygame.image.load('brazil/assets/odds7.png').convert_alpha()
o8 = pygame.image.load('brazil/assets/odds8.png').convert_alpha()
star = pygame.image.load('brazil/assets/rollovers.png').convert_alpha()
number = pygame.image.load('brazil/assets/number.png').convert_alpha()
tilt = pygame.image.load('brazil/assets/tilt.png').convert_alpha()
feature = pygame.image.load('brazil/assets/feature.png').convert_alpha()
line = pygame.image.load('brazil/assets/line.png').convert_alpha()
top_arrow = pygame.image.load('brazil/assets/top_arrow.png').convert_alpha()
bottom_arrow = pygame.image.load('brazil/assets/bottom_arrow.png').convert_alpha()
before_fourth = pygame.image.load('brazil/assets/before_fourth.png').convert_alpha()
corners = pygame.image.load('brazil/assets/corners.png').convert_alpha()
letter1 = pygame.image.load('brazil/assets/letter1.png').convert_alpha()
letter2 = pygame.image.load('brazil/assets/letter2.png').convert_alpha()
letter3 = pygame.image.load('brazil/assets/letter3.png').convert_alpha()
letter4 = pygame.image.load('brazil/assets/letter4.png').convert_alpha()
letter5 = pygame.image.load('brazil/assets/letter5.png').convert_alpha()
letter6 = pygame.image.load('brazil/assets/letter6.png').convert_alpha()
bg_menu = pygame.image.load('brazil/assets/brazil_menu.png')
bg_gi = pygame.image.load('brazil/assets/brazil_gi.png')
bg_off = pygame.image.load('brazil/assets/brazil_off.png')

class scorereel():
    """ Score Reels are used to count replays """
    def __init__(self, pos, image):
        self.position = pos
        self.default_y = self.position[1]
        self.image = pygame.image.load(image).convert()

reel1 = scorereel([117,833], "graphics/assets/white_reel.png")
reel10 = scorereel([98,833], "graphics/assets/white_reel.png")
reel100 = scorereel([79,833], "graphics/assets/white_reel.png")

def display(s, replays=0, menu=False):
    
    meter.set_colorkey((255,0,252))
    meter_position = [70,833]

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

    if s.game.tilt.status == True:
        p = [299,246]
        screen.blit(letter1, p)
        p = [352,248]
        screen.blit(letter2, p)
        p = [403,246]
        screen.blit(letter3, p)
        p = [459,246]
        screen.blit(letter4, p)
        p = [514,246]
        screen.blit(letter5, p)
        p = [549,246]
        screen.blit(letter6, p)
    else:
        if s.game.lite_a_name.status == True:
            p = [594,301]
            screen.blit(feature, p)

        if s.game.name.position >= 1:
            p = [299,246]
            screen.blit(letter1, p)
        if s.game.name.position >= 2:
            p = [352,248]
            screen.blit(letter2, p)
        if s.game.name.position >= 3:
            p = [403,246]
            screen.blit(letter3, p)
        if s.game.name.position >= 4:
            p = [459,246]
            screen.blit(letter4, p)
        if s.game.name.position >= 5:
            p = [514,246]
            screen.blit(letter5, p)
        if s.game.name.position >= 6:
            p = [549,246]
            screen.blit(letter6, p)

    if s.game.extra_ball.position == 1:
        eb_position = [104,973]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 2:
        eb_position = [138,973]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 3:
        eb_position = [173,973]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 4:
        eb_position = [209,973]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 5:
        eb_position = [243,973]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 6:
        eb_position = [277,975]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 7:
        eb_position = [312,975]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 8:
        eb_position = [347,975]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 9:
        eb_position = [382,975]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 10:
        eb_position = [416,975]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 11:
        eb_position = [458,975]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 12:
        eb_position = [492,975]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 13:
        eb_position = [526,975]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 14:
        eb_position = [560,975]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 15:
        eb_position = [593,975]
        screen.blit(eb, eb_position)

    if s.game.extra_ball.position >= 5 and s.game.extra_ball.position < 10:
        eb_pos = [108,1003]
        screen.blit(extra_ball, eb_pos)
    if s.game.extra_ball.position >= 10 and s.game.extra_ball.position < 15:
        eb_pos = [283,1003]
        screen.blit(extra_ball, eb_pos)
    if s.game.extra_ball.position == 15:
        eb_pos = [458,1003]
        screen.blit(extra_ball, eb_pos)

    if s.game.odds.position > 0:
        if s.game.odds.position == 1:
            odds_position = [264,794]
            screen.blit(o1, odds_position)
        if s.game.odds.position == 2:
            odds_position = [417,807]
            screen.blit(o2, odds_position)
        if s.game.odds.position == 3:
            odds_position = [459,788]
            screen.blit(o3, odds_position)
        if s.game.odds.position == 4:
            odds_position = [659,803]
            screen.blit(o4, odds_position)
        if s.game.odds.position == 5:
            odds_position = [191,841]
            screen.blit(o5, odds_position)
        if s.game.odds.position == 6:
            odds_position = [267,893]
            screen.blit(o6, odds_position)
        if s.game.odds.position == 7:
            odds_position = [398,909]
            screen.blit(o7, odds_position)
        if s.game.odds.position == 8:
            odds_position = [657,887]
            screen.blit(o8, odds_position)

    if s.game.red_star.status == True:
        rs_position = [647,970]
        screen.blit(star, rs_position)

    if s.game.corners.status == True:
        corners_position = [27,304]
        screen.blit(feature, corners_position)

    if s.game.tilt.status == False:
        if s.holes:
            if 1 in s.holes:
                p = [495,575]
                screen.blit(number, p)
            if 2 in s.holes:
                p = [495,501]
                screen.blit(number, p)
            if 3 in s.holes:
                p = [190,650]
                screen.blit(number, p)
            if 4 in s.holes:
                p = [418,353]
                screen.blit(number, p)
            if 5 in s.holes:
                p = [341,650]
                screen.blit(number, p)
            if 6 in s.holes:
                p = [191,355]
                screen.blit(number, p)
            if 7 in s.holes:
                p = [417,649]
                screen.blit(number, p)
            if 8 in s.holes:
                p = [190,429]
                screen.blit(number, p)
            if 9 in s.holes:
                p = [495,353]
                screen.blit(number, p)
            if 10 in s.holes:
                p = [493,427]
                screen.blit(number, p)
            if 11 in s.holes:
                p = [495,649]
                screen.blit(number, p)
            if 12 in s.holes:
                p = [266,500]
                screen.blit(number, p)
            if 13 in s.holes:
                p = [341,576]
                screen.blit(number, p)
            if 14 in s.holes:
                p = [341,427]
                screen.blit(number, p)
            if 15 in s.holes:
                p = [343,353]
                screen.blit(number, p)
            if 16 in s.holes:
                p = [342,501]
                screen.blit(number, p)
            if 17 in s.holes:
                p = [189,577]
                screen.blit(number, p)
            if 18 in s.holes:
                p = [419,499]
                screen.blit(number, p)
            if 19 in s.holes:
                p = [417,427]
                screen.blit(number, p)
            if 20 in s.holes:
                p = [265,428]
                screen.blit(number, p)
            if 21 in s.holes:
                p = [265,577]
                screen.blit(number, p)
            if 22 in s.holes:
                p = [417,575]
                screen.blit(number, p)
            if 23 in s.holes:
                p = [266,650]
                screen.blit(number, p)
            if 24 in s.holes:
                p = [267,354]
                screen.blit(number, p)
            if 25 in s.holes:
                p = [191,501]
                screen.blit(number, p)

    if s.game.tilt.status == True:
        tilt_position = [80,800]
        screen.blit(tilt, tilt_position)

    if s.game.row1.status == True:
        if s.game.selection_feature.position >= 1:
            p = [198,308]
            screen.blit(top_arrow, p)
            p = [198,714]
            screen.blit(bottom_arrow, p)
        if s.game.selection_feature.position >= 2:
            p = [273,308]
            screen.blit(top_arrow, p)
            p = [273,711]
            screen.blit(bottom_arrow, p)
        if s.game.selection_feature.position >= 3:
            p = [347,306]
            screen.blit(top_arrow, p)
            p = [347,712]
            screen.blit(bottom_arrow, p)
        if s.game.selection_feature.position >= 4:
            p = [424,306]
            screen.blit(top_arrow, p)
            p = [424,711]
            screen.blit(bottom_arrow, p)
        if s.game.selection_feature.position >= 5:
            p = [500,306]
            screen.blit(top_arrow, p)
            p = [502,714]
            screen.blit(bottom_arrow, p)
        if s.game.selection_feature.position >= 2:
            p = [184,747]
            screen.blit(corners, p)

        if (s.game.select_spots.status == True or s.game.selection_feature_relay.status == True):
            if s.game.before_fourth.status == True:
                if s.game.ball_count.position == 3:
                    s.cancel_delayed(name="blink")
                    blink([s,1,1])
                else:
                    s.cancel_delayed(name="blink")

        if (s.game.select_spots.status == True or s.game.selection_feature_relay.status == True):
            if s.game.before_fifth.status == True:
                if s.game.ball_count.position == 4:
                    s.cancel_delayed(name="blink")
                    blink([s,1,1])
                else:
                    s.cancel_delayed(name="blink")

        if s.game.before_fourth.status == True and (s.game.selection_feature.position > 3):
            p = [25,725]
            screen.blit(before_fourth, p)
        if s.game.before_fifth.status == True and (s.game.selection_feature.position > 3):
            p = [563,725]
            screen.blit(before_fourth, p)

    if s.game.row1.status == True:
        p = [157,357]
        screen.blit(line, p)
    
    if s.game.row2.status == True:
        p = [156,504]
        screen.blit(line, p)

    if s.game.row3.status == True:
        p = [156,651]
        screen.blit(line, p)

    if s.game.eb_play.status == True:
        p = [29,969]
        screen.blit(extra_balls, p)

    pygame.display.update()

def eb_animation(num):
    global screen
    if num == 9:
        eb_position = [104,973]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 8:
        eb_position = [138,973]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 7:
        eb_position = [173,973]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 6:
        eb_position = [209,973]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 5:
        eb_position = [243,973]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 4:
        eb_position = [277,975]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 3:
        eb_position = [312,975]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 2:
        eb_position = [347,975]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 1:
        eb_position = [382,975]
        screen.blit(eb, eb_position)
        pygame.display.update()


def feature_animation(num):
    global screen
    if num == 6:
        p = [594,301]
        screen.blit(feature, p)
        pygame.display.update()

    if num == 5:
        rs_position = [647,970]
        screen.blit(star, rs_position)
        pygame.display.update()

    if num == 4:
        rs_position = [647,970]
        screen.blit(star, rs_position)
        pygame.display.update()

    if num == 3:
        p = [184,747]
        screen.blit(corners, p)
        pygame.display.update()
    
    if num == 2:
        p = [364,747]
        screen.blit(corners, p)
        pygame.display.update()
   
    if num == 1:
        p = [156,504]
        screen.blit(line, p)
        pygame.display.update()

def odds_animation(num):
    global screen

    if num == 5:
        odds_position = [264,794]
        o = pygame.image.load('brazil/assets/odds1.png').convert_alpha()
        screen.blit(o, odds_position)
        pygame.display.update()
    if num == 4:
        odds_position = [417,807]
        o = pygame.image.load('brazil/assets/odds2.png').convert_alpha()
        screen.blit(o, odds_position)
        pygame.display.update()
    if num == 3:
        odds_position = [459,788]
        o = pygame.image.load('brazil/assets/odds3.png').convert_alpha()
        screen.blit(o, odds_position)
        pygame.display.update()
    if num == 2:
        odds_position = [659,803]
        o = pygame.image.load('brazil/assets/odds4.png').convert_alpha()
        screen.blit(o, odds_position)
        pygame.display.update()
    if num == 1:
        odds_position = [191,841]
        o = pygame.image.load('brazil/assets/odds5.png').convert_alpha()
        screen.blit(o, odds_position)
        pygame.display.update()

def blink(args):
    dirty_rects = []
    s = args[0]
    b = args[1]
    sn = args[2]

    if b == 0:
        if sn == 1:
            p = [364,747]
            dirty_rects.append(screen.blit(corners, p))
        pygame.display.update(dirty_rects)
    else:
        dirty_rects.append(screen.blit(bg_gi, (364,747), pygame.Rect(364,747,182,41)))
        pygame.display.update(dirty_rects)
    b = not b

    args = [s,b,sn]

    s.delay(name="blink", delay=0.1, handler=blink, param=args)
