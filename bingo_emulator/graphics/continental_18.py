
import pygame
import random

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

meter = pygame.image.load('graphics/assets/black_register_cover.png').convert()
odds = pygame.image.load('continental_18/assets/odds.png').convert_alpha()
select_now = pygame.image.load('continental_18/assets/select_now.png').convert_alpha()
tilt = pygame.image.load('continental_18/assets/tilt.png').convert_alpha()
circle = pygame.image.load('continental_18/assets/circle.png').convert_alpha()
corners = pygame.image.load('continental_18/assets/corners.png').convert_alpha()
mystery_arrow = pygame.image.load('continental_18/assets/mystery_arrow.png').convert_alpha()
screen_arrow = pygame.image.load('continental_18/assets/screen_arrow.png').convert_alpha()
screen_select_now = pygame.image.load('continental_18/assets/screen_select_now.png').convert_alpha()
select_now = pygame.image.load('continental_18/assets/select_now.png').convert_alpha()
select_spots = pygame.image.load('continental_18/assets/select_spots.png').convert_alpha()
spot_arrow = pygame.image.load('continental_18/assets/spot_arrow.png').convert_alpha()
spot_letter = pygame.image.load('continental_18/assets/spot_letter.png').convert_alpha()
up_down = pygame.image.load('continental_18/assets/up_down.png').convert_alpha()
screen_card = pygame.image.load('continental_18/assets/screen.png').convert_alpha()
number_card = pygame.image.load('continental_18/assets/number_card.png').convert_alpha()
number = pygame.image.load('continental_18/assets/number.png').convert_alpha()
time = pygame.image.load('continental_18/assets/time.png').convert_alpha()
bg_menu = pygame.image.load('continental_18/assets/continental_18_menu.png').convert_alpha()
bg_gi = pygame.image.load('continental_18/assets/continental_18_gi.png').convert_alpha()
bg_off = pygame.image.load('continental_18/assets/continental_18_off.png').convert_alpha()

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
        o = [61,872]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 2:
        o = [102,872]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 3:
        o = [145,872]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 4:
        o = [189,872]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 5:
        o = [233,872]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 6:
        o = [285,872]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 7:
        o = [337,872]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 8:
        o = [391,872]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 9:
        o = [443,872]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 10:
        o = [495,872]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 11:
        o = [547,872]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 12:
        o = [600,872]
        screen.blit(odds, o)

    if s.game.yellow_odds.position == 1:
        o = [61,939]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 2:
        o = [102,939]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 3:
        o = [145,939]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 4:
        o = [189,939]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 5:
        o = [233,939]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 6:
        o = [285,939]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 7:
        o = [337,939]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 8:
        o = [391,939]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 9:
        o = [443,939]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 10:
        o = [495,939]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 11:
        o = [547,939]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 12:
        o = [600,939]
        screen.blit(odds, o)

    if s.game.green_odds.position == 1:
        o = [61,1007]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 2:
        o = [102,1007]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 3:
        o = [145,1007]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 4:
        o = [189,1007]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 5:
        o = [233,1007]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 6:
        o = [285,1007]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 7:
        o = [337,1007]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 8:
        o = [391,1007]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 9:
        o = [443,1007]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 10:
        o = [495,1007]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 11:
        o = [547,1007]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 12:
        o = [600,1007]
        screen.blit(odds, o)

    if s.game.magic_spot.status == True:
        max_ball = 0
        p = [497,599]
        screen.blit(select_now, p)
        if s.game.selection_feature.position == 1:
            max_ball = 4
            p = [49,721]
            screen.blit(time, p)
        if s.game.selection_feature.position == 2:
            max_ball = 5
            p = [50,671]
            screen.blit(time, p)
        if s.game.selection_feature.position == 3:
            max_ball = 6
            p = [50,617]
            screen.blit(time, p)

        if s.game.ball_count.position == max_ball - 1:
            s.cancel_delayed(name="blink")
            blink([s,1,1])
        else:
            s.cancel_delayed(name="blink")
        if s.game.select_spot.position == 0:
            p = [505,677]
            screen.blit(circle, p)
        if s.game.select_spot.position == 1:
            p = [565,642]
            screen.blit(circle, p)
        if s.game.select_spot.position == 2:
            p = [626,677]
            screen.blit(circle, p)
        if s.game.select_spot.position == 3:
            p = [625,747]
            screen.blit(circle, p)
        if s.game.select_spot.position == 4:
            p = [564,783]
            screen.blit(circle, p)
        if s.game.select_spot.position == 5:
            p = [505,746]
            screen.blit(circle, p)

    if s.game.line_feature.position == 1:
        p = [614,506]
        screen.blit(screen_arrow, p)
    if s.game.line_feature.position == 2:
        p = [614,473]
        screen.blit(screen_arrow, p)
    if s.game.line_feature.position in [3,4]:
        if s.game.down.status == False:
            p = [562,425]
            screen.blit(up_down, p)
        else:
            p = [627,427]
            screen.blit(up_down, p)
    if s.game.line_feature.position == 4:
        p = [614,394]
        screen.blit(screen_arrow, p)
    if s.game.line_feature.position == 5:
        p = [561,341]
        screen.blit(screen_select_now, p)

    if s.game.line_feature.position >= 3:
        if s.game.ball_count.position == 3:
            s.cancel_delayed(name="blink_screen")
            blink_screen([s,1,1])
        else:
            s.cancel_delayed("blink_screen")

    if s.game.corners384.status == True:
        p = [22,461]
        screen.blit(corners, p)
    if s.game.corners192.status == True:
        p = [21,512]
        screen.blit(corners, p)


    if s.game.tilt.status == True:
        tilt_position = [684,780]
        screen.blit(tilt, tilt_position)

    pygame.display.update()

def blink_screen(args):
    dirty_rects = []
    s = args[0]
    b = args[1]
    sn = args[2]

    if b == 0:
        if sn == 1:
            p = [561,536]
            dirty_rects.append(screen.blit(screen_select_now, p))
        pygame.display.update(dirty_rects)
    else:
        dirty_rects.append(screen.blit(bg_gi, (561,536), pygame.Rect(561,536,133,49)))
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
            p = [495,823]
            dirty_rects.append(screen.blit(select_now, p))
        pygame.display.update(dirty_rects)
    else:
        dirty_rects.append(screen.blit(bg_gi, (495,823), pygame.Rect(495,823,171,40)))
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
    
    if s.game.selection_feature.position == 1:
        p = [49,721]
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],216,52)))
        dirty_rects.append(screen.blit(time, p))
    if s.game.selection_feature.position == 2:
        p = [50,671]
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],216,52)))
        dirty_rects.append(screen.blit(time, p))
    if s.game.selection_feature.position == 3:
        p = [50,617]
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],216,52)))
        dirty_rects.append(screen.blit(time, p))

    if s.game.select_spot.position == 0:
        p = [505,677]
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],35,34)))
        dirty_rects.append(screen.blit(circle, p))
    if s.game.select_spot.position == 1:
        p = [565,642]
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],35,34)))
        dirty_rects.append(screen.blit(circle, p))
    if s.game.select_spot.position == 2:
        p = [626,677]
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],35,34)))
        dirty_rects.append(screen.blit(circle, p))
    if s.game.select_spot.position == 3:
        p = [625,747]
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],35,34)))
        dirty_rects.append(screen.blit(circle, p))
    if s.game.select_spot.position == 4:
        p = [564,783]
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],35,34)))
        dirty_rects.append(screen.blit(circle, p))
    if s.game.select_spot.position == 5:
        p = [505,746]
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],35,34)))
        dirty_rects.append(screen.blit(circle, p))

    if s.game.magic_spot.status == True:
        p = [497,599]
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],171,40)))
        dirty_rects.append(screen.blit(select_now, p))
    
    pygame.display.update(dirty_rects)


def clear_odds(s, num):
    global screen
    dirty_rects = []
    # red 5,10 - yellow 6,9,12,11 - Green 8,5,11,10,12
    dirty_rects.append(screen.blit(bg_gi, (233,872), pygame.Rect(233,872,48,67)))
    dirty_rects.append(screen.blit(bg_gi, (495,872), pygame.Rect(495,872,48,67)))
    dirty_rects.append(screen.blit(bg_gi, (285,939), pygame.Rect(285,939,48,67)))
    dirty_rects.append(screen.blit(bg_gi, (443,939), pygame.Rect(443,939,48,67)))
    dirty_rects.append(screen.blit(bg_gi, (600,939), pygame.Rect(600,939,48,67)))
    dirty_rects.append(screen.blit(bg_gi, (547,939), pygame.Rect(547,939,48,67)))
    dirty_rects.append(screen.blit(bg_gi, (391,1007), pygame.Rect(391,1007,48,67)))
    dirty_rects.append(screen.blit(bg_gi, (233,1007), pygame.Rect(233,1007,48,67)))
    dirty_rects.append(screen.blit(bg_gi, (547,1007), pygame.Rect(547,1007,48,67)))
    dirty_rects.append(screen.blit(bg_gi, (495,1007), pygame.Rect(495,1007,48,67)))
    dirty_rects.append(screen.blit(bg_gi, (600,1007), pygame.Rect(600,1007,48,67)))

    pygame.display.update(dirty_rects)

def draw_odds_animation(s, num):
    global screen
    dirty_rects = []
    if num in [1,36,38,26,11,13]:
        if s.game.red_odds.position != 5:
            p = [233,872]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
    if num in [10,19,35,44]:
        if s.game.red_odds.position != 10:
            p = [495,872]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
    if num in [44,19]:
        if s.game.yellow_odds.position != 6:
            p = [285,939]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
    if num in [17,42]:
        if s.game.yellow_odds.position != 9:
            p = [443,939]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
    if num in [1,36,38,26,11,13]:
        if s.game.yellow_odds.position != 12:
            p = [600,939]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
    if num in [10,39,35,14]:
        if s.game.yellow_odds.position != 11:
            p = [547,939]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
    if num in [44,19]:
        if s.game.green_odds.position != 8:
            p = [391,1007]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
    if num in [17,42]:
        if s.game.green_odds.position != 5:
            p = [233,1007]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
    if num in [21,46]:
        if s.game.green_odds.position != 11:
            p = [547,1007]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
    if num in [23,48]:
        if s.game.green_odds.position != 11:
            p = [495,1007]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
    if num in [25,50]:
        if s.game.green_odds.position != 10:
            p = [495,1007]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
    if num in [2,27,8,33]:
        if s.game.green_odds.position != 12:
            p = [600,1007]
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
    # before fifth, after fifth, spot 0,1,2,3,4,5, corners lower, corners upper, up, down
    if s.game.selection_feature.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (50,671), pygame.Rect(50,671,216,52)))
    if s.game.selection_feature.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (50,617), pygame.Rect(50,617,216,52)))

    if s.game.magic_spot.status == False:
        dirty_rects.append(screen.blit(bg_gi, (505,677), pygame.Rect(505,677,35,34)))
        dirty_rects.append(screen.blit(bg_gi, (565,642), pygame.Rect(565,642,35,34)))
        dirty_rects.append(screen.blit(bg_gi, (626,677), pygame.Rect(626,677,35,34)))
        dirty_rects.append(screen.blit(bg_gi, (625,747), pygame.Rect(625,747,35,34)))
        dirty_rects.append(screen.blit(bg_gi, (564,783), pygame.Rect(564,783,35,34)))
        dirty_rects.append(screen.blit(bg_gi, (505,746), pygame.Rect(505,746,35,34)))

    if s.game.corners384.status == False:
        dirty_rects.append(screen.blit(bg_gi, (22,461), pygame.Rect(22,461,120,47)))
    if s.game.corners192.status == False:
        dirty_rects.append(screen.blit(bg_gi, (21,512), pygame.Rect(21,512,120,47)))

    if s.game.line_feature.position not in [3,4]:
        if s.game.down.status == False:
            dirty_rects.append(screen.blit(bg_gi, (562,425), pygame.Rect(562,425,63,42)))
        else:
            dirty_rects.append(screen.blit(bg_gi, (627,427), pygame.Rect(627,427,63,42)))

    pygame.display.update(dirty_rects)


def draw_feature_animation(s, num):
    global screen
    dirty_rects = []

    if num in [19,30,5,44]:
        if s.game.selection_feature.position != 2:
            p = [50,671]
            dirty_rects.append(screen.blit(time, p))
            pygame.display.update(dirty_rects)
    if num in [10,39,35,14]:
        if s.game.selection_feature.position != 3:
            p = [50,617]
            dirty_rects.append(screen.blit(time, p))
            pygame.display.update(dirty_rects)
    if num in [7,16,32,41]:
        if s.game.magic_spot.status == False:
            p = [505,677]
            dirty_rects.append(screen.blit(circle, p))
            pygame.display.update(dirty_rects)
    if num in [11,32,36,7]:
        if s.game.magic_spot.status == False:
            p = [565,642]
            dirty_rects.append(screen.blit(circle, p))
            pygame.display.update(dirty_rects)
    if num in [1,36,38,26,11,13]:
        if s.game.magic_spot.status == False:
            p = [626,677]
            dirty_rects.append(screen.blit(circle, p))
            pygame.display.update(dirty_rects)
    if num in [14,18,39,43]:
        if s.game.magic_spot.status == False:
            p = [625,747]
            dirty_rects.append(screen.blit(circle, p))
            pygame.display.update(dirty_rects)
    if num in [44,19]:
        if s.game.magic_spot.status == False:
            p = [564,783]
            dirty_rects.append(screen.blit(circle, p))
            pygame.display.update(dirty_rects)
    if num in [1,26]:
        if s.game.magic_spot.status == False:
            p = [505,746]
            dirty_rects.append(screen.blit(circle, p))
            pygame.display.update(dirty_rects)
    if num in [15,40]:
        if s.game.corners384.status == False: 
            p = [22,461]
            dirty_rects.append(screen.blit(corners, p))
            pygame.display.update(dirty_rects)
    if num in [16,41]:
        if s.game.corners192.status == False: 
            p = [21,512]
            dirty_rects.append(screen.blit(corners, p))
            pygame.display.update(dirty_rects)
    if num in [17,42]:
        if s.game.line_feature.position not in [3,4]:
            if s.game.down.status == False:
                p = [562,425]
                dirty_rects.append(screen.blit(up_down, p))
                pygame.display.update(dirty_rects)
    if num in [14,18,39,43]:
        if s.game.line_feature.position not in [3,4]:
            if s.game.down.status == True:
                p = [627,427]
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

