
import pygame, random

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

meter = pygame.image.load('graphics/assets/register_cover.png').convert()
corners = pygame.image.load('hi_fi/assets/corners.png').convert_alpha()
odds1 = pygame.image.load('hi_fi/assets/odds1.png').convert_alpha()
odds2 = pygame.image.load('hi_fi/assets/odds2.png').convert_alpha()
odds3 = pygame.image.load('hi_fi/assets/odds3.png').convert_alpha()
odds4 = pygame.image.load('hi_fi/assets/odds4.png').convert_alpha()
odds5 = pygame.image.load('hi_fi/assets/odds5.png').convert_alpha()
odds6 = pygame.image.load('hi_fi/assets/odds6.png').convert_alpha()
odds7 = pygame.image.load('hi_fi/assets/odds7.png').convert_alpha()
odds8 = pygame.image.load('hi_fi/assets/odds8.png').convert_alpha()
extra_balls = pygame.image.load('hi_fi/assets/extra_balls.png').convert_alpha()
eb = pygame.image.load('hi_fi/assets/eb.png').convert_alpha()
eb2 = pygame.image.load('hi_fi/assets/eb2.png').convert_alpha()
number = pygame.image.load('hi_fi/assets/number.png').convert_alpha()
sc_number = pygame.image.load('hi_fi/assets/sc_number.png').convert_alpha()
sc_arrow = pygame.image.load('hi_fi/assets/sc_arrow.png').convert_alpha()
sf_arrow = pygame.image.load('hi_fi/assets/sf_arrow.png').convert_alpha()
tilt = pygame.image.load('hi_fi/assets/tilt.png').convert_alpha()
bump_arrow = pygame.image.load('hi_fi/assets/bump_arrow.png').convert_alpha()
bump = pygame.image.load('hi_fi/assets/bump.png').convert_alpha()
bump_number = pygame.image.load('hi_fi/assets/bump_number.png').convert_alpha()
sc = pygame.image.load('hi_fi/assets/super_card.png').convert_alpha()
select_now = pygame.image.load('hi_fi/assets/select_now.png').convert_alpha()
select_number = pygame.image.load('hi_fi/assets/select_number.png').convert_alpha()
spot_arrow = pygame.image.load('hi_fi/assets/sf_arrow.png').convert_alpha()
spotted = pygame.image.load('hi_fi/assets/select_number.png').convert_alpha()
time = pygame.image.load('hi_fi/assets/time.png').convert_alpha()
rollover = pygame.image.load('hi_fi/assets/rollover.png').convert_alpha()
bg_menu = pygame.image.load('hi_fi/assets/hi_fi_menu.png')
bg_gi = pygame.image.load('hi_fi/assets/hi_fi_gi.png')
bg_off = pygame.image.load('hi_fi/assets/hi_fi_off.png')

class scorereel():
    """ Score Reels are used to count replays """
    def __init__(self, pos, image):
        self.position = pos
        self.default_y = self.position[1]
        self.image = pygame.image.load(image).convert()

reel1 = scorereel([613,575], "graphics/assets/green_reel.png")
reel10 = scorereel([594,575], "graphics/assets/green_reel.png")
reel100 = scorereel([575,575], "graphics/assets/green_reel.png")

def display(s, replays=0, menu=False):
    
    meter.set_colorkey((255,0,252))
    meter_position = [565,575]

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

    if s.game.odds.position == 1:
        p = [30,245]
        screen.blit(odds1, p)
    if s.game.odds.position == 2:
        p = [68,254]
        screen.blit(odds2, p)
    if s.game.odds.position == 3:
        p = [174,260]
        screen.blit(odds3, p)
    if s.game.odds.position == 4:
        p = [256,255]
        screen.blit(odds4, p)
    if s.game.odds.position == 5:
        p = [382,255]
        screen.blit(odds5, p)
    if s.game.odds.position == 6:
        p = [501,255]
        screen.blit(odds6, p)
    if s.game.odds.position == 7:
        p = [560,251]
        screen.blit(odds7, p)
    if s.game.odds.position == 8:
        p = [633,248]
        screen.blit(odds8, p)

    if s.game.eb_play.status == True:
        p = [275,964]
        screen.blit(extra_balls, p)

    if s.game.extra_ball.position >= 1:
        p = [81,999]
        screen.blit(eb, p)
    if s.game.extra_ball.position >= 2:
        p = [128,999]
        screen.blit(eb2, p)
    if s.game.extra_ball.position >= 3:
        p = [193,999]
        screen.blit(eb2, p)
    if s.game.extra_ball.position >= 4:
        p = [269,999]
        screen.blit(eb, p)
    if s.game.extra_ball.position >= 5:
        p = [317,999]
        screen.blit(eb2, p)
    if s.game.extra_ball.position >= 6:
        p = [381,999]
        screen.blit(eb2, p)
    if s.game.extra_ball.position >= 7:
        p = [456,999]
        screen.blit(eb, p)
    if s.game.extra_ball.position >= 8:
        p = [504,999]
        screen.blit(eb2, p)
    if s.game.extra_ball.position >= 9:
        p = [567,999]
        screen.blit(eb2, p)


    if s.game.tilt.status == False:
        if s.holes:
            if 1 in s.holes:
                number_position = [217,753]
                screen.blit(number, number_position)
                p = [547,824]
                screen.blit(sc_number, p)
            if 2 in s.holes:
                number_position = [217,697]
                screen.blit(number, number_position)
            if 3 in s.holes:
                number_position = [446,809]
                screen.blit(number, number_position)
                p = [76,776]
                screen.blit(sc_number, p)
            if 4 in s.holes:
                number_position = [273,583]
                screen.blit(number, number_position)
                p = [596,871]
                screen.blit(sc_number, p)
            if 5 in s.holes:
                number_position = [331,809]
                screen.blit(number, number_position)
            if 6 in s.holes:
                number_position = [447,583]
                screen.blit(number, number_position)
            if 7 in s.holes:
                number_position = [275,809]
                screen.blit(number, number_position)
                p = [596,775]
                screen.blit(sc_number, p)
            if 8 in s.holes:
                number_position = [446,638]
                screen.blit(number, number_position)
            if 9 in s.holes:
                number_position = [215,583]
                screen.blit(number, number_position)
                p = [27,822]
                screen.blit(sc_number, p)
            if 10 in s.holes:
                number_position = [215,638]
                screen.blit(number, number_position)
                p = [595,822]
                screen.blit(sc_number, p)
            if 11 in s.holes:
                number_position = [215,808]
                screen.blit(number, number_position)
                p = [126,823]
                screen.blit(sc_number, p)
                p = [645,772]
                screen.blit(sc_number, p)
            if 12 in s.holes:
                number_position = [388,695]
                screen.blit(number, number_position)
                p = [27,870]
                screen.blit(sc_number, p)
            if 13 in s.holes:
                number_position = [332,751]
                screen.blit(number, number_position)
                p = [645,821]
                screen.blit(sc_number, p)
            if 14 in s.holes:
                number_position = [331,637]
                screen.blit(number, number_position)
                p = [127,872]
                screen.blit(sc_number, p)
            if 15 in s.holes:
                number_position = [331,579]
                screen.blit(number, number_position)
                p = [546,775]
                screen.blit(sc_number, p)
            if 16 in s.holes:
                number_position = [331,695]
                screen.blit(number, number_position)
            if 17 in s.holes:
                number_position = [446,751]
                screen.blit(number, number_position)
                p = [547,870]
                screen.blit(sc_number, p)
            if 18 in s.holes:
                number_position = [275,695]
                screen.blit(number, number_position)
                p = [126,776]
                screen.blit(sc_number, p)
                p = [645,871]
                screen.blit(sc_number, p)
            if 19 in s.holes:
                number_position = [274,638]
                screen.blit(number, number_position)
            if 20 in s.holes:
                number_position = [389,639]
                screen.blit(number, number_position)
            if 21 in s.holes:
                number_position = [390,753]
                screen.blit(number, number_position)
            if 22 in s.holes:
                number_position = [275,752]
                screen.blit(number, number_position)
            if 23 in s.holes:
                number_position = [389,808]
                screen.blit(number, number_position)
                p = [27,775]
                screen.blit(sc_number, p)
            if 24 in s.holes:
                number_position = [389,581]
                screen.blit(number, number_position)
                p = [78,871]
                screen.blit(sc_number, p)
            if 25 in s.holes:
                number_position = [447,696]
                screen.blit(number, number_position)
                p = [77,823]
                screen.blit(sc_number, p)

        if s.game.super_card.position == 1:
            p = [43,714]
            screen.blit(sc_arrow, p)
        if s.game.super_card.position == 2:
            p = [70,715]
            screen.blit(sc_arrow, p)
        if s.game.super_card.position == 3:
            p = [97,715]
            screen.blit(sc_arrow, p)
        if s.game.super_card.position == 4:
            p = [123,715]
            screen.blit(sc_arrow, p)

        if s.game.super_card.position >= 4:
            p = [45,741]
            screen.blit(sc, p)

        if s.game.super_card.position == 5:
            p = [565,712]
            screen.blit(sc_arrow, p)
        if s.game.super_card.position == 6:
            p = [591,712]
            screen.blit(sc_arrow, p)
        if s.game.super_card.position == 7:
            p = [618,712]
            screen.blit(sc_arrow, p)
        if s.game.super_card.position == 8:
            p = [643,712]
            screen.blit(sc_arrow, p)

        if s.game.super_card.position >= 8:
            p = [563,737]
            screen.blit(sc, p)

    if s.game.spotted_numbers.position == 1:
        p = [145,931]
        screen.blit(sf_arrow, p)
    if s.game.spotted_numbers.position == 2:
        p = [181,931]
        screen.blit(sf_arrow, p)
    if s.game.spotted_numbers.position == 3:
        p = [218,931]
        screen.blit(sf_arrow, p)
    if s.game.spotted_numbers.position >= 4:
        if s.game.before_fourth.status == True:
            p = [31,924]
            screen.blit(time, p)
        if s.game.before_fifth.status == True:
            p = [582,925]
            screen.blit(time, p)
        p = [255,931]
        screen.blit(sf_arrow, p)
        p = [276,926]
        screen.blit(select_number, p)
    if s.game.spotted_numbers.position >= 5:
        p = [202,877]
        screen.blit(sc_number, p)
    if s.game.spotted_numbers.position >= 6:
        p = [245,877]
        screen.blit(sc_number, p)
    if s.game.spotted_numbers.position >= 7:
        p = [293,877]
        screen.blit(sc_number, p)
    if s.game.spotted_numbers.position >= 8:
        p = [338,877]
        screen.blit(sc_number, p)
    if s.game.spotted_numbers.position >= 9:
        p = [385,877]
        screen.blit(sc_number, p)
    if s.game.spotted_numbers.position >= 10:
        p = [429,877]
        screen.blit(sc_number, p)
    if s.game.spotted_numbers.position >= 11:
        p = [475,876]
        screen.blit(sc_number, p)

    if s.game.spotted_numbers.position >= 4:
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

    if s.game.bump_feature.position == 1:
        p = [20,507]
        screen.blit(bump_arrow, p)
    if s.game.bump_feature.position == 2:
        p = [52,507]
        screen.blit(bump_arrow, p)
    if s.game.bump_feature.position == 3:
        p = [86,507]
        screen.blit(bump_arrow, p)
    if s.game.bump_feature.position >= 4:
        p = [119,496]
        screen.blit(bump, p)
    if s.game.bump_feature.position >= 5:
        p = [237,507]
        screen.blit(bump_number, p)
    if s.game.bump_feature.position >= 6:
        p = [266,507]
        screen.blit(bump_number, p)
    if s.game.bump_feature.position >= 7:
        p = [297,507]
        screen.blit(bump_number, p)
    if s.game.bump_feature.position >= 8:
        p = [327,507]
        screen.blit(bump_number, p)
    if s.game.bump_feature.position >= 9:
        p = [358,507]
        screen.blit(bump_number, p)
    if s.game.bump_feature.position >= 10:
        p = [390,507]
        screen.blit(bump_number, p)
    if s.game.bump_feature.position >= 11:
        p = [419,507]
        screen.blit(bump_number, p)
    if s.game.bump_feature.position >= 12:
        p = [450,507]
        screen.blit(bump_number, p)
    if s.game.bump_feature.position >= 13:
        p = [481,507]
        screen.blit(bump_number, p)
    if s.game.bump_feature.position >= 14:
        p = [512,507]
        screen.blit(bump_number, p)

    if s.game.corners.status == True:
        p = [53,567]
        screen.blit(corners, p)

    if s.game.yellow_rollover.status == True:
        p = [19,417]
        screen.blit(rollover, p)
    if s.game.red_rollover.status == True:
        p = [630,421]
        screen.blit(rollover, p)

    if s.game.tilt.status == True:
        tilt_position = [567,510]
        screen.blit(tilt, tilt_position)

    pygame.display.update()

def blink(args):
    dirty_rects = []
    s = args[0]
    b = args[1]
    sn = args[2]

    if b == 0:
        if sn == 1:
            p = [422,925]
            dirty_rects.append(screen.blit(select_now, p))
        pygame.display.update(dirty_rects)
    else:
        dirty_rects.append(screen.blit(bg_gi, (422,925), pygame.Rect(422,925,145,34)))
        pygame.display.update(dirty_rects)
    b = not b

    args = [s,b,sn]

    s.delay(name="blink", delay=0.1, handler=blink, param=args)

def eb_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]


    if s.game.extra_ball.position < 1:
        dirty_rects.append(screen.blit(bg_gi, (81,999), pygame.Rect(81,999,47,33)))
    if s.game.extra_ball.position < 2:
        dirty_rects.append(screen.blit(bg_gi, (128,999), pygame.Rect(128,999,63,35)))
    if s.game.extra_ball.position < 3:
        dirty_rects.append(screen.blit(bg_gi, (193,999), pygame.Rect(193,999,63,35)))
    if s.game.extra_ball.position < 4:
        dirty_rects.append(screen.blit(bg_gi, (269,999), pygame.Rect(269,999,47,33)))
    if s.game.extra_ball.position < 5:
        dirty_rects.append(screen.blit(bg_gi, (317,999), pygame.Rect(317,999,63,35)))
    if s.game.extra_ball.position < 6:
        dirty_rects.append(screen.blit(bg_gi, (381,999), pygame.Rect(381,999,63,35)))
    if s.game.extra_ball.position < 7:
        dirty_rects.append(screen.blit(bg_gi, (456,999), pygame.Rect(456,999,47,33)))
    if s.game.extra_ball.position < 8:
        dirty_rects.append(screen.blit(bg_gi, (504,999), pygame.Rect(504,999,63,35)))
    if s.game.extra_ball.position < 9:
        dirty_rects.append(screen.blit(bg_gi, (567,999), pygame.Rect(567,999,63,35)))

    pygame.display.update(dirty_rects)

    if num in [0,24,25,49]:
        if s.game.extra_ball.position < 1:
            p = [81,999]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [1,15,26,40]:
        if s.game.extra_ball.position < 2:
            p = [128,999]
            dirty_rects.append(screen.blit(eb2, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [3,4,17,28,29,42]:
        if s.game.extra_ball.position < 3:
            p = [193,999]
            dirty_rects.append(screen.blit(eb2, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [5,18,30,43]:
        if s.game.extra_ball.position < 4:
            p = [269,999]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [7,8,19,32,33,44]:
        if s.game.extra_ball.position < 5:
            p = [317,999]
            dirty_rects.append(screen.blit(eb2, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [9,10,20,34,35,45]:
        if s.game.extra_ball.position < 6:
            p = [381,999]
            dirty_rects.append(screen.blit(eb2, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [11,21,36,46]:
        if s.game.extra_ball.position < 7:
            p = [456,999]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [12,22,37,47]:
        if s.game.extra_ball.position < 8:
            p = [504,999]
            dirty_rects.append(screen.blit(eb2, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [2,6,13,16,23,27,31,38,41,48]:
        if s.game.extra_ball.position < 9:
            p = [567,999]
            dirty_rects.append(screen.blit(eb2, p))
            pygame.display.update(dirty_rects) 
            return

def clear_odds(s, num):
    global screen

    dirty_rects = []


    if s.game.odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (30,245), pygame.Rect(30,245,50,114)))
    if s.game.odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (68,254), pygame.Rect(68,254,87,137)))
    if s.game.odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (174,260), pygame.Rect(174,260,42,114)))
    if s.game.odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (256,255), pygame.Rect(256,255,81,83)))
    if s.game.odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (382,255), pygame.Rect(382,255,83,86)))
    if s.game.odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (501,255), pygame.Rect(501,255,33,116)))
    if s.game.odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (560,251), pygame.Rect(560,251,87,119)))
    if s.game.odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (633,248), pygame.Rect(633,248,58,111)))

    pygame.display.update(dirty_rects)

def draw_odds_animation(s, num):
    global screen
    dirty_rects = []

    if num in [2,3,12,27,28,37]:
        if s.game.odds.position != 1:
            p = [30,245]
            dirty_rects.append(screen.blit(odds1, p))
            pygame.display.update(dirty_rects)
            return
    if num in [13,14,38,39]:
        if s.game.odds.position != 2:
            p = [68,254]
            dirty_rects.append(screen.blit(odds2, p))
            pygame.display.update(dirty_rects)
            return
    if num in [4,5,15,16,29,30,40,41]:
        if s.game.odds.position != 3:
            p = [174,260]
            dirty_rects.append(screen.blit(odds3, p))
            pygame.display.update(dirty_rects)
            return
    if num in [17,18,42,43]:
        if s.game.odds.position != 4:
            p = [256,255]
            dirty_rects.append(screen.blit(odds4, p))
            pygame.display.update(dirty_rects)
            return
    if num in [6,7,19,20,31,32,44,45]:
        if s.game.odds.position != 5:
            p = [382,255]
            dirty_rects.append(screen.blit(odds5, p))
            pygame.display.update(dirty_rects)
            return
    if num in [21,22,46,47]:
        if s.game.odds.position != 6:
            p = [501,255]
            dirty_rects.append(screen.blit(odds6, p))
            pygame.display.update(dirty_rects)
            return
    if num in [8,9,23,24,33,34,48,49]:
        if s.game.odds.position != 7:
            p = [560,251]
            dirty_rects.append(screen.blit(odds7, p))
            pygame.display.update(dirty_rects)
            return
    if num in [10,11,25,26,0,35,36,50]:
        if s.game.odds.position != 8:
            p = [633,248]
            dirty_rects.append(screen.blit(odds8, p))
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
        dirty_rects.append(screen.blit(bg_gi, (31,924), pygame.Rect(31,924,97,58)))
    if s.game.before_fifth.status == False:
        dirty_rects.append(screen.blit(bg_gi, (582,925), pygame.Rect(582,925,97,58)))
    if s.game.spotted_numbers.position < 8:
        dirty_rects.append(screen.blit(bg_gi, (202,877), pygame.Rect(202,877,41,41)))
        dirty_rects.append(screen.blit(bg_gi, (245,877), pygame.Rect(245,877,41,41)))
        dirty_rects.append(screen.blit(bg_gi, (293,877), pygame.Rect(293,877,41,41)))
        dirty_rects.append(screen.blit(bg_gi, (338,877), pygame.Rect(338,877,41,41)))
    if s.game.spotted_numbers.position < 9:
        dirty_rects.append(screen.blit(bg_gi, (385,877), pygame.Rect(385,877,41,41)))
    if s.game.spotted_numbers.position < 10:
        dirty_rects.append(screen.blit(bg_gi, (429,877), pygame.Rect(429,877,41,41)))
    if s.game.spotted_numbers.position < 11:
        dirty_rects.append(screen.blit(bg_gi, (475,876), pygame.Rect(475,876,41,41)))

    if s.game.yellow_rollover.status == False:
        dirty_rects.append(screen.blit(bg_gi, (19,417), pygame.Rect(19,417,69,68)))
    if s.game.red_rollover.status == False:
        dirty_rects.append(screen.blit(bg_gi, (630,421), pygame.Rect(630,421,69,68)))
    if s.game.bump_feature.position < 4:
        dirty_rects.append(screen.blit(bg_gi, (119,496), pygame.Rect(119,496,118,56)))
    if s.game.super_card.position < 4:
        dirty_rects.append(screen.blit(bg_gi, (45,741), pygame.Rect(45,741,110,30)))
    if s.game.super_card.position < 8:
        dirty_rects.append(screen.blit(bg_gi, (563,737), pygame.Rect(563,737,110,30)))
    if s.game.corners.status == False:
        dirty_rects.append(screen.blit(bg_gi, (53,567), pygame.Rect(53,567,115,80)))
    pygame.display.update(dirty_rects)


def draw_feature_animation(s, num):
    global screen
    dirty_rects = []
 
    if num in [8,20,33,45]:
        if s.game.before_fourth.status == False:
            p = [31,924]
            dirty_rects.append(screen.blit(time, p))
            pygame.display.update(dirty_rects)
            return
    if num in [9,21,34,46]:
        if s.game.before_fifth.status == False:
            p = [582,925]
            dirty_rects.append(screen.blit(time, p))
            pygame.display.update(dirty_rects)
            return
    if num in [4,16,24,29,41,0]:
        if s.game.spotted_numbers.position < 8:
            p = [202,877]
            dirty_rects.append(screen.blit(sc_number, p))
            p = [245,877]
            dirty_rects.append(screen.blit(sc_number, p))
            p = [293,877]
            dirty_rects.append(screen.blit(sc_number, p))
            p = [338,877]
            dirty_rects.append(screen.blit(sc_number, p))
            pygame.display.update(dirty_rects)
            return
    if num in [5,17,30,42]:
        if s.game.spotted_numbers.position < 9:
            p = [385,877]
            dirty_rects.append(screen.blit(sc_number, p))
            pygame.display.update(dirty_rects)
            return
    if num in [6,18,31,43]:
        if s.game.spotted_numbers.position < 10:
            p = [429,877]
            dirty_rects.append(screen.blit(sc_number, p))
            pygame.display.update(dirty_rects)
            return
    if num in [7,19,32,44]:
        if s.game.spotted_numbers.position < 11:
            p = [475,876]
            dirty_rects.append(screen.blit(sc_number, p))
            pygame.display.update(dirty_rects)
            return
    if num in [0,12,25,37]:
        if s.game.yellow_rollover.status == False:
            p = [19,417]
            dirty_rects.append(screen.blit(rollover, p))
            pygame.display.update(dirty_rects)
            s.game.coils.yellowROLamp.pulse(85)
            return
    if num in [1,13,26,38]:
        if s.game.red_rollover.status == False:
            p = [630,421]
            dirty_rects.append(screen.blit(rollover, p))
            pygame.display.update(dirty_rects)
            s.game.coils.redROLamp.pulse(85)
            return
    if num in [10,22,35,47]:
        if s.game.bump_feature.position < 4:
            p = [119,496]
            dirty_rects.append(screen.blit(bump, p))
            pygame.display.update(dirty_rects)
            return
    if num in [2,14,27,39]:
        if s.game.super_card.position < 4:
            p = [45,741]
            dirty_rects.append(screen.blit(sc, p))
            pygame.display.update(dirty_rects)
            return
    if num in [3,15,28,40]:
        if s.game.super_card.position < 8:
            p = [563,737]
            dirty_rects.append(screen.blit(sc, p))
            pygame.display.update(dirty_rects)
            return
    if num in [11,24,36,0]:
        if s.game.corners.status == False:
            p = [53,567]
            dirty_rects.append(screen.blit(corners, p))
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
