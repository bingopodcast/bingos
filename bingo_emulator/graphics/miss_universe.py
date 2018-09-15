
import pygame
import random

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

meter = pygame.image.load('graphics/assets/black_register_cover.png').convert()
odds = pygame.image.load('miss_universe/assets/odds.png').convert_alpha()
select_now = pygame.image.load('miss_universe/assets/select_now.png').convert_alpha()
tilt = pygame.image.load('miss_universe/assets/tilt.png').convert_alpha()
circle = pygame.image.load('miss_universe/assets/circle.png').convert_alpha()
corners = pygame.image.load('miss_universe/assets/corners.png').convert_alpha()
mystery_arrow = pygame.image.load('miss_universe/assets/mystery_arrow.png').convert_alpha()
red_mystery = pygame.image.load('miss_universe/assets/red_mystery.png').convert_alpha()
screen_arrow = pygame.image.load('miss_universe/assets/screen_arrow.png').convert_alpha()
screen_select_now = pygame.image.load('miss_universe/assets/screen_select_now.png').convert_alpha()
select_now = pygame.image.load('miss_universe/assets/select_now.png').convert_alpha()
select_spots = pygame.image.load('miss_universe/assets/select_spots.png').convert_alpha()
spot_arrow = pygame.image.load('miss_universe/assets/spot_arrow.png').convert_alpha()
spot_letter = pygame.image.load('miss_universe/assets/spot_letter.png').convert_alpha()
up_down = pygame.image.load('miss_universe/assets/up_down.png').convert_alpha()
yellow_mystery = pygame.image.load('miss_universe/assets/yellow_mystery.png').convert_alpha()
screen_card = pygame.image.load('miss_universe/assets/screen.png').convert_alpha()
number_card = pygame.image.load('miss_universe/assets/number_card.png').convert_alpha()
number = pygame.image.load('miss_universe/assets/number.png').convert_alpha()
bg_menu = pygame.image.load('miss_universe/assets/miss_universe_menu.png').convert_alpha()
bg_gi = pygame.image.load('miss_universe/assets/miss_universe_gi.png').convert_alpha()
bg_off = pygame.image.load('miss_universe/assets/miss_universe_off.png').convert_alpha()

class scorereel():
    """ Score Reels are used to count replays """
    def __init__(self, pos, image):
        self.position = pos
        self.default_y = self.position[1]
        self.image = pygame.image.load(image).convert()

reel1 = scorereel([376,737], "graphics/assets/white_reel.png")
reel10 = scorereel([357,737], "graphics/assets/white_reel.png")
reel100 = scorereel([338,737], "graphics/assets/white_reel.png")
reel1000 = scorereel([319,737], "graphics/assets/white_reel.png")

def display(s, replays=0, menu=False):
    
    meter.set_colorkey((255,0,252))
    meter_position = [309,737]

    screen.blit(reel1.image, reel1.position)
    screen.blit(reel10.image, reel10.position)
    screen.blit(reel100.image, reel100.position)
    screen.blit(reel1000.image, reel1000.position)
    screen.blit(meter, meter_position)

    nc_position = [202,405]
    screen.blit(number_card, nc_position)

    if s.game.line.position in [0,2]:
        p = [196,340]
        screen.blit(screen_card, p)
    elif s.game.line.position == 1:
        p = [196,396]
        screen.blit(screen_card, p)
    elif s.game.line.position == 3:
        p = [196,284]
        screen.blit(screen_card, p)

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

    if s.game.tilt.status == False:
        if s.holes:
            if 1 in s.holes:
                p = [420,517]
                screen.blit(number, p)
            if 2 in s.holes:
                p = [420,463]
                screen.blit(number, p)
            if 3 in s.holes:
                p = [311,519]
                screen.blit(number, p)
            if 4 in s.holes:
                p = [311,407]
                screen.blit(number, p)
            if 5 in s.holes:
                p = [475,406]
                screen.blit(number, p)
            if 6 in s.holes:
                p = [255,408]
                screen.blit(number, p)
            if 7 in s.holes:
                p = [201,463]
                screen.blit(number, p)
            if 8 in s.holes:
                p = [257,463]
                screen.blit(number, p)
            if 9 in s.holes:
                p = [421,405]
                screen.blit(number, p)
            if 10 in s.holes:
                p = [201,519]
                screen.blit(number, p)
            if 11 in s.holes:
                p = [365,406]
                screen.blit(number, p)
            if 12 in s.holes:
                p = [256,519]
                screen.blit(number, p)
            if 13 in s.holes:
                p = [474,461]
                screen.blit(number, p)
            if 14 in s.holes:
                p = [311,462]
                screen.blit(number, p)
            if 15 in s.holes:
                p = [474,515]
                screen.blit(number, p)
            if 16 in s.holes:
                p = [201,408]
                screen.blit(number, p)
            if 17 in s.holes:
                p = [367,517]
                screen.blit(number, p)
            if 18 in s.holes:
                p = [366,462]
                screen.blit(number, p)

    if s.game.red_odds.position == 1:
        o = [61,863]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 2:
        o = [102,863]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 3:
        o = [145,863]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 4:
        o = [189,863]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 5:
        o = [233,863]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 6:
        o = [285,863]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 7:
        o = [337,863]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 8:
        o = [391,863]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 9:
        o = [443,863]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 10:
        o = [495,863]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 11:
        o = [547,863]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 12:
        o = [600,863]
        screen.blit(odds, o)

    if s.game.yellow_odds.position == 1:
        o = [61,927]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 2:
        o = [102,927]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 3:
        o = [145,927]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 4:
        o = [189,927]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 5:
        o = [233,927]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 6:
        o = [285,927]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 7:
        o = [337,927]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 8:
        o = [391,927]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 9:
        o = [443,927]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 10:
        o = [495,927]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 11:
        o = [547,927]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 12:
        o = [600,927]
        screen.blit(odds, o)

    if s.game.green_odds.position == 1:
        o = [61,989]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 2:
        o = [102,989]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 3:
        o = [145,989]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 4:
        o = [189,989]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 5:
        o = [233,989]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 6:
        o = [285,989]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 7:
        o = [337,989]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 8:
        o = [391,989]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 9:
        o = [443,989]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 10:
        o = [495,989]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 11:
        o = [547,989]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 12:
        o = [600,989]
        screen.blit(odds, o)

    if s.game.mystery_red.status == True:
        p = [512,598]
        screen.blit(red_mystery, p)
        if s.game.ball_count.position >= 2:
            if s.game.mystery_yellow.status == False:
                if s.game.mystery_spot.position in [0,1]:
                    p = [568,642]
                    screen.blit(circle, p)
                if s.game.mystery_spot.position in [2,3]:
                    p = [506,743]
                    screen.blit(circle, p)
                if s.game.mystery_spot.position in [4,5]:
                    p = [627,742]
                    screen.blit(circle, p)
            else:
                if s.game.mystery_spot.position in [1]:
                    p = [568,642]
                    screen.blit(circle, p)
                if s.game.mystery_spot.position in [3]:
                    p = [506,743]
                    screen.blit(circle, p)
                if s.game.mystery_spot.position in [5]:
                    p = [627,742]
                    screen.blit(circle, p)
    if s.game.mystery_yellow.status == True:
        p = [510,815]
        screen.blit(yellow_mystery, p)
        if s.game.ball_count.position >= 2:
            if s.game.mystery_red.status == False:
                if s.game.mystery_spot.position in [0,1]:
                    p = [507,675]
                    screen.blit(circle, p)
                if s.game.mystery_spot.position in [2,3]:
                    p = [629,674]
                    screen.blit(circle, p)
                if s.game.mystery_spot.position in [4,5]:
                    p = [565,777]
                    screen.blit(circle, p)
            else:
                if s.game.mystery_spot.position in [0]:
                    p = [507,675]
                    screen.blit(circle, p)
                if s.game.mystery_spot.position in [2]:
                    p = [629,674]
                    screen.blit(circle, p)
                if s.game.mystery_spot.position in [4]:
                    p = [565,777]
                    screen.blit(circle, p)




    if s.game.line_feature.position == 1:
        p = [615,511]
        screen.blit(screen_arrow, p)
    if s.game.line_feature.position == 2:
        p = [617,481]
        screen.blit(screen_arrow, p)
    if s.game.line_feature.position in [3,4]:
        if s.game.down.status == False:
            p = [565,437]
            screen.blit(up_down, p)
        else:
            p = [633,438]
            screen.blit(up_down, p)
    if s.game.line_feature.position == 4:
        p = [615,405]
        screen.blit(screen_arrow, p)
    if s.game.line_feature.position == 5:
        p = [563,352]
        screen.blit(screen_select_now, p)

    if s.game.line_feature.position >= 3:
        if s.game.ball_count.position == 2:
            s.cancel_delayed(name="blink_screen")
            blink_screen([s,1,1])
        else:
            s.cancel_delayed(name="blink_screen")

    if s.game.corners384.status == True:
        p = [22,470]
        screen.blit(corners, p)
    if s.game.corners192.status == True:
        p = [21,519]
        screen.blit(corners, p)

    if s.game.spot.position >= 1:
        p = [100,626]
        screen.blit(circle, p)
        p = [99,677]
        screen.blit(circle, p)
        p = [99,727]
        screen.blit(circle, p)
        if s.game.select_spot.position == 0:
            p = [55,626]
            screen.blit(spot_letter, p)
        if s.game.select_spot.position == 1:
            p = [56,676]
            screen.blit(spot_letter, p)
        if s.game.select_spot.position == 2:
            p = [55,725]
            screen.blit(spot_letter, p)
        if s.game.ball_count.position == 1:
            s.cancel_delayed(name="blink")
            blink([s,1,1])
        else:
            s.cancel_delayed(name="blink")
    if s.game.spot.position >= 2:
        p = [145,626]
        screen.blit(circle, p)
        p = [143,677]
        screen.blit(circle, p)
        p = [144,728]
        screen.blit(circle, p)
    if s.game.spot.position >= 3:
        p = [189,630]
        screen.blit(spot_arrow, p)
        p = [189,681]
        screen.blit(spot_arrow, p)
        p = [189,732]
        screen.blit(spot_arrow, p)
    if s.game.spot.position >= 4:
        p = [223,626]
        screen.blit(circle, p)
        p = [223,677]
        screen.blit(circle, p)
        p = [223,728]
        screen.blit(circle, p)

    if s.game.tilt.status == True:
        tilt_position = [682,768]
        screen.blit(tilt, tilt_position)

    pygame.display.update()

def blink_screen(args):
    dirty_rects = []
    s = args[0]
    b = args[1]
    sn = args[2]

    if b == 0:
        if sn == 1:
            p = [563,539]
            dirty_rects.append(screen.blit(screen_select_now, p))
        pygame.display.update(dirty_rects)
    else:
        dirty_rects.append(screen.blit(bg_gi, (563,539), pygame.Rect(563,539,137,51)))
        pygame.display.update(dirty_rects)
    b = not b

    args = [s,b,sn]

    s.delay(name="blink_screen", delay=0.1, handler=blink_screen, param=args)

def blink(args):
    dirty_rects = []
    s = args[0]
    b = args[1]
    sn = args[2]

    if b == 0:
        if sn == 1:
            p = [77,811]
            dirty_rects.append(screen.blit(select_now, p))
        pygame.display.update(dirty_rects)
    else:
        dirty_rects.append(screen.blit(bg_gi, (77,811), pygame.Rect(77,811,156,30)))
        pygame.display.update(dirty_rects)
    b = not b

    args = [s,b,sn]

    s.delay(name="blink", delay=0.1, handler=blink, param=args)

def line_animation(args):
    dirty_rects = []
    s = args[0]
    num = args[1]
    direction = args[2]

    nc_position = [202,405]
    dirty_rects.append(screen.blit(number_card, nc_position))

    if direction == "up":
        if s.game.line.position == 0:
            dirty_rects.append(screen.blit(screen_card, (196,284 - num)))
        elif s.game.line.position == 1:
            dirty_rects.append(screen.blit(screen_card, (196,340 - num)))
        elif s.game.line.position == 2:
            dirty_rects.append(screen.blit(screen_card, (196, 396 + num)))
        elif s.game.line.position == 3:
            dirty_rects.append(screen.blit(screen_card, (196, 340 + num)))
    else:
        if s.game.line.position == 0:
            dirty_rects.append(screen.blit(screen_card, (196, 396 + num)))
        elif s.game.line.position == 1:
            dirty_rects.append(screen.blit(screen_card, (196, 340 - num)))
        elif s.game.line.position == 2:
            dirty_rects.append(screen.blit(screen_card, (196,284 - num)))
        elif s.game.line.position == 3:
            dirty_rects.append(screen.blit(screen_card, (196,340 - num)))


    if (s.game.anti_cheat.status == True):
        dirty_rects.append(screen.blit(bg_gi, (196,284), pygame.Rect(196,284,332,406)))
    else:
        dirty_rects.append(screen.blit(bg_off, (196,284), pygame.Rect(196,284,332,406)))
    
    if s.game.mystery_red.status == True:
        dirty_rects.append(screen.blit(bg_gi, (512,598), pygame.Rect(512,598,148,39)))
        dirty_rects.append(screen.blit(red_mystery, (512,598)))

    if s.game.spot.position >= 3:
        dirty_rects.append(screen.blit(bg_gi, (189,630), pygame.Rect(189,630,28,27)))
        dirty_rects.append(screen.blit(spot_arrow, (189,630)))
        dirty_rects.append(screen.blit(bg_gi, (189,681), pygame.Rect(189,681,28,27)))
        dirty_rects.append(screen.blit(spot_arrow, (189,681)))
        dirty_rects.append(screen.blit(bg_gi, (189,732), pygame.Rect(189,732,28,27)))
        dirty_rects.append(screen.blit(spot_arrow, (189,732)))
    if s.game.spot.position >= 4:
        dirty_rects.append(screen.blit(bg_gi, (223,626), pygame.Rect(223,626,35,34)))
        dirty_rects.append(screen.blit(circle, (223,626)))
        dirty_rects.append(screen.blit(bg_gi, (223,677), pygame.Rect(223,677,35,34)))
        dirty_rects.append(screen.blit(circle, (223,677)))
        dirty_rects.append(screen.blit(bg_gi, (223,728), pygame.Rect(223,728,35,34)))
        dirty_rects.append(screen.blit(circle, (223,728)))


    pygame.display.update(dirty_rects)

def clear_odds(s, num):
    global screen

    dirty_rects = []

    # red 5,10 - yellow 6,9,12,11 - Green 8,5,11,10,12
    dirty_rects.append(screen.blit(bg_gi, (233,863), pygame.Rect(233,863,42,54)))
    dirty_rects.append(screen.blit(bg_gi, (495,863), pygame.Rect(495,863,42,54)))
    dirty_rects.append(screen.blit(bg_gi, (285,927), pygame.Rect(285,927,42,54)))
    dirty_rects.append(screen.blit(bg_gi, (443,927), pygame.Rect(443,927,42,54)))
    dirty_rects.append(screen.blit(bg_gi, (600,927), pygame.Rect(600,927,42,54)))
    dirty_rects.append(screen.blit(bg_gi, (547,927), pygame.Rect(547,927,42,54)))
    dirty_rects.append(screen.blit(bg_gi, (391,989), pygame.Rect(391,989,42,54)))
    dirty_rects.append(screen.blit(bg_gi, (233,989), pygame.Rect(233,989,42,54)))
    dirty_rects.append(screen.blit(bg_gi, (547,989), pygame.Rect(547,989,42,54)))
    dirty_rects.append(screen.blit(bg_gi, (495,989), pygame.Rect(495,989,42,54)))
    dirty_rects.append(screen.blit(bg_gi, (600,989), pygame.Rect(600,989,42,54)))

    pygame.display.update(dirty_rects)

def draw_odds_animation(s, num):
    global screen
    dirty_rects = []
    if num in [1,36,38,26,11,13]:
        if s.game.red_odds.position != 5:
            p = [233,863]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
    if num in [10,19,35,44]:
        if s.game.red_odds.position != 10:
            p = [495,863]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
    if num in [44,19]:
        if s.game.yellow_odds.position != 6:
            p = [285,927]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
    if num in [17,42]:
        if s.game.yellow_odds.position != 9:
            p = [443,927]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
    if num in [1,36,38,26,11,13]:
        if s.game.yellow_odds.position != 12:
            p = [600,927]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
    if num in [10,39,35,14]:
        if s.game.yellow_odds.position != 11:
            p = [547,927]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
    if num in [44,19]:
        if s.game.green_odds.position != 8:
            p = [391,989]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
    if num in [17,42]:
        if s.game.green_odds.position != 5:
            p = [233,989]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
    if num in [21,46]:
        if s.game.green_odds.position != 11:
            p = [547,989]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
    if num in [23,48]:
        if s.game.green_odds.position != 11:
            p = [495,989]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
    if num in [25,50]:
        if s.game.green_odds.position != 10:
            p = [495,989]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
    if num in [2,27,8,33]:
        if s.game.green_odds.position != 12:
            p = [600,989]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)

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

    # Red mystery, yellow mystery, spot 10,2,5,14,16,1, corners lower, corners upper, up, down
    if s.game.mystery_red.status == False:
        dirty_rects.append(screen.blit(bg_gi, (512,598), pygame.Rect(512,598,148,39)))
    if s.game.mystery_yellow.status == False:
        dirty_rects.append(screen.blit(bg_gi, (510,815), pygame.Rect(510,815,143,39)))

    if s.game.spot.position < 2:
        dirty_rects.append(screen.blit(bg_gi, (145,626), pygame.Rect(145,626,35,34)))
        dirty_rects.append(screen.blit(bg_gi, (143,677), pygame.Rect(143,677,35,34)))
        dirty_rects.append(screen.blit(bg_gi, (144,728), pygame.Rect(144,728,35,34)))
    if s.game.spot.position < 4:
        dirty_rects.append(screen.blit(bg_gi, (223,626), pygame.Rect(223,626,35,34)))
        dirty_rects.append(screen.blit(bg_gi, (223,677), pygame.Rect(223,677,35,34)))
        dirty_rects.append(screen.blit(bg_gi, (223,728), pygame.Rect(223,728,35,34)))

    if s.game.corners384.status == False:
        dirty_rects.append(screen.blit(bg_gi, (22,470), pygame.Rect(22,470,120,47)))
    if s.game.corners192.status == False:
        dirty_rects.append(screen.blit(bg_gi, (21,519), pygame.Rect(21,519,120,47)))

    if s.game.line_feature.position not in [3,4]:
        if s.game.down.status == False:
            dirty_rects.append(screen.blit(bg_gi, (565,437), pygame.Rect(565,437,63,37)))
        else:
            dirty_rects.append(screen.blit(bg_gi, (633,438), pygame.Rect(633,438,63,37)))

    pygame.display.update(dirty_rects)


def draw_feature_animation(s, num):
    global screen
    dirty_rects = []
    if num in [19,30,5,44]:
        if s.game.mystery_red.status == False:
            p = [512,598]
            dirty_rects.append(screen.blit(red_mystery, p))
            pygame.display.update(dirty_rects)
    if num in [10,39,35,14]:
        if s.game.mystery_yellow.status == False:
            p = [510,815]
            dirty_rects.append(screen.blit(yellow_mystery, p))
            pygame.display.update(dirty_rects)
    if num in [7,16,32,41]:
        if s.game.spot.position < 2:
            p = [145,626]
            dirty_rects.append(screen.blit(circle, p))
            pygame.display.update(dirty_rects)
    if num in [11,32,36,7]:
        if s.game.spot.position < 4:
            p = [223,626]
            dirty_rects.append(screen.blit(circle, p))
            pygame.display.update(dirty_rects)
    if num in [1,36,38,26,11,13]:
        if s.game.spot.position < 2:
            p = [143,677]
            dirty_rects.append(screen.blit(circle, p))
            pygame.display.update(dirty_rects)
    if num in [14,18,39,43]:
        if s.game.spot.position < 4:
            p = [223,677]
            dirty_rects.append(screen.blit(circle, p))
            pygame.display.update(dirty_rects)
    if num in [44,19]:
        if s.game.spot.position < 2:
            p = [144,728]
            dirty_rects.append(screen.blit(circle, p))
            pygame.display.update(dirty_rects)
    if num in [1,26]:
        if s.game.spot.position < 4: 
            p = [223,728]
            dirty_rects.append(screen.blit(circle, p))
            pygame.display.update(dirty_rects)
    if num in [15,40]:
        if s.game.corners384.status == False: 
            p = [22,470]
            dirty_rects.append(screen.blit(corners, p))
            pygame.display.update(dirty_rects)
    if num in [16,41]:
        if s.game.corners192.status == False: 
            p = [21,519]
            dirty_rects.append(screen.blit(corners, p))
            pygame.display.update(dirty_rects)
    if num in [17,42]:
        if s.game.line_feature.position not in [3,4]:
            if s.game.down.status == False:
                p = [565,437]
                dirty_rects.append(screen.blit(up_down, p))
                pygame.display.update(dirty_rects)
    if num in [14,18,39,43]:
        if s.game.line_feature.position not in [3,4]:
            if s.game.down.status == True:
                p = [633,438]
                dirty_rects.append(screen.blit(up_down, p))
                pygame.display.update(dirty_rects)

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

