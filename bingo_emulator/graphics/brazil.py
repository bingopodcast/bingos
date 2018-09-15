
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

def eb_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]

    if s.game.extra_ball.position < 5:
        dirty_rects.append(screen.blit(bg_gi, (108,1003), pygame.Rect(108,1003,168,35)))
    if s.game.extra_ball.position < 10:
        dirty_rects.append(screen.blit(bg_gi, (283,1003), pygame.Rect(283,1003,168,35)))
    if s.game.extra_ball.position < 15:
        dirty_rects.append(screen.blit(bg_gi, (458,1003), pygame.Rect(458,1003,168,35)))
    pygame.display.update(dirty_rects)

    if num in [0,1,6,7,12,13,18,19,26,27,32,33,38,39,44,45]:
        if s.game.extra_ball.position < 5:
            p = [108,1003]
            dirty_rects.append(screen.blit(extra_ball, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [2,3,8,9,14,15,20,21,28,29,34,35,40,41,46,47]:
        if s.game.extra_ball.position < 10:
            p = [283,1003]
            dirty_rects.append(screen.blit(extra_ball, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [4,5,10,11,16,17,22,23,24,30,31,36,37,42,43,48,49,50]:
        if s.game.extra_ball.position < 15:
            p = [458,1003]
            dirty_rects.append(screen.blit(extra_ball, p))
            pygame.display.update(dirty_rects)
            return

def clear_odds(s, num):
    global screen

    dirty_rects = []

    if s.game.odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (264,794), pygame.Rect(264,794,56,69)))
    if s.game.odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (417,807), pygame.Rect(417,807,31,80)))
    if s.game.odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (459,788), pygame.Rect(459,788,39,84)))
    if s.game.odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (659,803), pygame.Rect(659,803,39,79)))
    if s.game.odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (191,841), pygame.Rect(191,841,50,78)))
    if s.game.odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (267,893), pygame.Rect(267,893,72,70)))
    if s.game.odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (398,909), pygame.Rect(398,909,96,57)))
    if s.game.odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (657,887), pygame.Rect(657,887,44,75)))

    pygame.display.update(dirty_rects)

def draw_odds_animation(s, num):
    global screen
    dirty_rects = []

    if num in [0,1,40,14,24,25]:
        if s.game.odds.position != 1:
            p = [264,794]
            dirty_rects.append(screen.blit(o1, p))
            pygame.display.update(dirty_rects)
            return
    if num in [2,3,41,15,26,27]:
        if s.game.odds.position != 2:
            p = [417,807]
            dirty_rects.append(screen.blit(o2, p))
            pygame.display.update(dirty_rects)
            return
    if num in [4,5,42,16,28,29]:
        if s.game.odds.position != 3:
            p = [459,788]
            dirty_rects.append(screen.blit(o3, p))
            pygame.display.update(dirty_rects)
            return
    if num in [6,7,43,17,30,31]:
        if s.game.odds.position != 4:
            p = [659,803]
            dirty_rects.append(screen.blit(o4, p))
            pygame.display.update(dirty_rects)
            return
    if num in [8,9,44,18,32,33]:
        if s.game.odds.position != 5:
            p = [191,841]
            dirty_rects.append(screen.blit(o5, p))
            pygame.display.update(dirty_rects)
            return
    if num in [10,11,45,19,34,35]:
        if s.game.odds.position != 6:
            p = [267,893]
            dirty_rects.append(screen.blit(o6, p))
            pygame.display.update(dirty_rects)
            return
    if num in [12,13,46,47,20,21,36,37]:
        if s.game.odds.position != 7:
            p = [398,909]
            dirty_rects.append(screen.blit(o7, p))
            pygame.display.update(dirty_rects)
            return
    if num in [14,48,49,22,23,38]:
        if s.game.odds.position != 8:
            p = [657,887]
            dirty_rects.append(screen.blit(o8, p))
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
    if s.game.lite_a_name.status == False:
        dirty_rects.append(screen.blit(bg_gi, (594,301), pygame.Rect(594,301,119,63)))
    if s.game.corners.status == False:
        dirty_rects.append(screen.blit(bg_gi, (24,304), pygame.Rect(24,304,119,63)))
    if s.game.red_star.status == False:
        dirty_rects.append(screen.blit(bg_gi, (647,970), pygame.Rect(647,970,63,61)))
    if s.game.row2.status == False:
        dirty_rects.append(screen.blit(bg_gi, (156,504), pygame.Rect(156,504,423,40)))
    if s.game.row3.status == False:
        dirty_rects.append(screen.blit(bg_gi, (156,651), pygame.Rect(156,651,423,40)))
    if s.game.selection_feature.position < 5:
        dirty_rects.append(screen.blit(bg_gi, (500,306), pygame.Rect(500,306,36,36)))
        dirty_rects.append(screen.blit(bg_gi, (502,714), pygame.Rect(502,714,35,33)))
    if s.game.selection_feature.position < 4:
        dirty_rects.append(screen.blit(bg_gi, (424,306), pygame.Rect(424,306,36,36)))
        dirty_rects.append(screen.blit(bg_gi, (424,711), pygame.Rect(424,711,35,33)))
    if s.game.selection_feature.position < 3:
        dirty_rects.append(screen.blit(bg_gi, (347,306), pygame.Rect(347,306,36,36)))
        dirty_rects.append(screen.blit(bg_gi, (347,712), pygame.Rect(347,712,35,33)))
    if s.game.selection_feature.position < 2:
        if s.game.selection_feature.position < 2:
            dirty_rects.append(screen.blit(bg_gi, (184,747), pygame.Rect(184,747,182,41)))
        dirty_rects.append(screen.blit(bg_gi, (198,308), pygame.Rect(198,308,36,36)))
        dirty_rects.append(screen.blit(bg_gi, (198,714), pygame.Rect(198,714,35,33)))
    if s.game.selection_feature.position < 1:
        dirty_rects.append(screen.blit(bg_gi, (273,308), pygame.Rect(273,308,36,36)))
        dirty_rects.append(screen.blit(bg_gi, (273,711), pygame.Rect(273,711,35,33)))

    pygame.display.update(dirty_rects)


def draw_feature_animation(s, num):
    global screen
    dirty_rects = []
    
    if num in [7,8,33,34]:
        if s.game.red_star.status == False:
            p = [647,970]
            dirty_rects.append(screen.blit(star, p))
            pygame.display.update(dirty_rects)
            return
    if num in [5,6,31,32]:
        if s.game.lite_a_name.status == False:
            p = [594,301]
            dirty_rects.append(screen.blit(feature, p))
            pygame.display.update(dirty_rects)
            return
    if num in [3,4,29,30]:
        if s.game.corners.status == False:
            p = [24,304]
            dirty_rects.append(screen.blit(feature, p))
            pygame.display.update(dirty_rects)
            return
    if num in [1,2,11,12,27,28,37,38]:
        if s.game.row2.status == False:
            p = [156,504]
            dirty_rects.append(screen.blit(line, p))
            pygame.display.update(dirty_rects)
            return
    if num in [0,49,9,10,25,26,35,36]:
        if s.game.row3.status == False:
            p = [156,651]
            dirty_rects.append(screen.blit(line, p))
            pygame.display.update(dirty_rects)
            return
    if num in [48,47,24,23]:
        if s.game.selection_feature.position < 5:
            p = [500,306]
            dirty_rects.append(screen.blit(top_arrow, p))
            p = [502,714]
            dirty_rects.append(screen.blit(bottom_arrow, p))
            pygame.display.update(dirty_rects)
            return
    if num in [21,22,46,45]:
        if s.game.selection_feature.position < 4:
            p = [424,306]
            dirty_rects.append(screen.blit(top_arrow, p))
            p = [424,711]
            dirty_rects.append(screen.blit(bottom_arrow, p))
            pygame.display.update(dirty_rects)
            return
    if num in [19,20,44,43]:
        if s.game.selection_feature.position < 3:
            p = [347,306]
            dirty_rects.append(screen.blit(top_arrow, p))
            p = [347,712]
            dirty_rects.append(screen.blit(bottom_arrow, p))
            pygame.display.update(dirty_rects)
            return
    if num in [18,17,42,41]:
        if s.game.selection_feature.position < 2:
            p = [198,308]
            dirty_rects.append(screen.blit(top_arrow, p))
            p = [198,714]
            dirty_rects.append(screen.blit(bottom_arrow, p))
            if s.game.selection_feature.position < 2:
                p = [184,747]
                dirty_rects.append(screen.blit(corners, p))
            pygame.display.update(dirty_rects)
            return
    if num in [16,15,40,39]:
        if s.game.selection_feature.position < 1:
            p = [273,308]
            dirty_rects.append(screen.blit(top_arrow, p))
            p = [273,711]
            dirty_rects.append(screen.blit(bottom_arrow, p))
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
