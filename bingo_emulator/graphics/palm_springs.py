
import pygame, random

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

meter = pygame.image.load('graphics/assets/register_cover.png').convert()
corners = pygame.image.load('palm_springs/assets/corners.png').convert_alpha()
odds1 = pygame.image.load('palm_springs/assets/odds1.png').convert_alpha()
odds2 = pygame.image.load('palm_springs/assets/odds2.png').convert_alpha()
odds3 = pygame.image.load('palm_springs/assets/odds3.png').convert_alpha()
odds4 = pygame.image.load('palm_springs/assets/odds4.png').convert_alpha()
odds5 = pygame.image.load('palm_springs/assets/odds5.png').convert_alpha()
odds6 = pygame.image.load('palm_springs/assets/odds6.png').convert_alpha()
odds7 = pygame.image.load('palm_springs/assets/odds7.png').convert_alpha()
odds8 = pygame.image.load('palm_springs/assets/odds8.png').convert_alpha()
extra_balls = pygame.image.load('palm_springs/assets/extra_balls.png').convert_alpha()
eb = pygame.image.load('palm_springs/assets/eb.png').convert_alpha()
eb2 = pygame.image.load('palm_springs/assets/eb2.png').convert_alpha()
number = pygame.image.load('palm_springs/assets/number.png').convert_alpha()
red_number = pygame.image.load('palm_springs/assets/red_number.png').convert_alpha()
sc_number = pygame.image.load('palm_springs/assets/sc_number.png').convert_alpha()
tilt = pygame.image.load('palm_springs/assets/tilt.png').convert_alpha()
hold_arrow = pygame.image.load('palm_springs/assets/spotted_arrow.png').convert_alpha()
sc = pygame.image.load('palm_springs/assets/super_card.png').convert_alpha()
hold = pygame.image.load('palm_springs/assets/hold.png').convert_alpha()
hold_now = pygame.image.load('palm_springs/assets/hold_time.png').convert_alpha()
select_now = pygame.image.load('palm_springs/assets/select_now.png').convert_alpha()
spot_arrow = pygame.image.load('palm_springs/assets/spotted_arrow.png').convert_alpha()
spotted = pygame.image.load('palm_springs/assets/spotted.png').convert_alpha()
spotted_number = pygame.image.load('palm_springs/assets/spotted_number.png').convert_alpha()
bg_menu = pygame.image.load('palm_springs/assets/palm_springs_menu.png')
bg_gi = pygame.image.load('palm_springs/assets/palm_springs_gi.png')
bg_off = pygame.image.load('palm_springs/assets/palm_springs_off.png')

class scorereel():
    """ Score Reels are used to count replays """
    def __init__(self, pos, image):
        self.position = pos
        self.default_y = self.position[1]
        self.image = pygame.image.load(image).convert()

reel1 = scorereel([613,320], "graphics/assets/green_reel.png")
reel10 = scorereel([594,320], "graphics/assets/green_reel.png")
reel100 = scorereel([575,320], "graphics/assets/green_reel.png")

def display(s, replays=0, menu=False):
    
    meter.set_colorkey((255,0,252))
    meter_position = [565,320]

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
        p = [82,820]
        screen.blit(odds1, p)
    if s.game.odds.position == 2:
        p = [122,819]
        screen.blit(odds2, p)
    if s.game.odds.position == 3:
        p = [172,821]
        screen.blit(odds3, p)
    if s.game.odds.position == 4:
        p = [282,817]
        screen.blit(odds4, p)
    if s.game.odds.position == 5:
        p = [384,820]
        screen.blit(odds5, p)
    if s.game.odds.position == 6:
        p = [463,817]
        screen.blit(odds6, p)
    if s.game.odds.position == 7:
        p = [568,818]
        screen.blit(odds7, p)
    if s.game.odds.position == 8:
        p = [619,820]
        screen.blit(odds8, p)

    if s.game.eb_play.status == True:
        p = [270,972]
        screen.blit(extra_balls, p)

    if s.game.extra_ball.position >= 1:
        p = [62,1011]
        screen.blit(eb, p)
    if s.game.extra_ball.position >= 2:
        p = [110,1011]
        screen.blit(eb2, p)
    if s.game.extra_ball.position >= 3:
        p = [174,1011]
        screen.blit(eb2, p)
    if s.game.extra_ball.position >= 4:
        p = [274,1011]
        screen.blit(eb, p)
    if s.game.extra_ball.position >= 5:
        p = [320,1011]
        screen.blit(eb2, p)
    if s.game.extra_ball.position >= 6:
        p = [385,1011]
        screen.blit(eb2, p)
    if s.game.extra_ball.position >= 7:
        p = [481,1011]
        screen.blit(eb, p)
    if s.game.extra_ball.position >= 8:
        p = [529,1011]
        screen.blit(eb2, p)
    if s.game.extra_ball.position >= 9:
        p = [594,1011]
        screen.blit(eb2, p)


    if s.game.tilt.status == False:
        if s.holes:
            if 1 in s.holes:
                number_position = [443,436]
                screen.blit(number, number_position)
            if 2 in s.holes:
                number_position = [220,436]
                screen.blit(number, number_position)
            if 3 in s.holes:
                number_position = [445,550]
                screen.blit(number, number_position)
                p = [546,532]
                screen.blit(sc_number, p)
            if 4 in s.holes:
                number_position = [276,320]
                screen.blit(number, number_position)
                p = [78,488]
                screen.blit(sc_number, p)
            if 5 in s.holes:
                number_position = [332,550]
                screen.blit(number, number_position)
            if 6 in s.holes:
                number_position = [445,321]
                screen.blit(number, number_position)
                p = [125,533]
                screen.blit(sc_number, p)
            if 7 in s.holes:
                number_position = [278,550]
                screen.blit(number, number_position)
                p = [592,486]
                screen.blit(sc_number, p)
            if 8 in s.holes:
                number_position = [332,322]
                screen.blit(number, number_position)
            if 9 in s.holes:
                number_position = [389,436]
                screen.blit(number, number_position)
                p = [592,533]
                screen.blit(sc_number, p)
            if 10 in s.holes:
                number_position = [220,378]
                screen.blit(number, number_position)
                p = [34,533]
                screen.blit(sc_number, p)
            if 11 in s.holes:
                number_position = [222,550]
                screen.blit(number, number_position)
                p = [593,579]
                screen.blit(sc_number, p)
            if 12 in s.holes:
                number_position = [333,380]
                screen.blit(number, number_position)
                p = [33,579]
                screen.blit(sc_number, p)
            if 13 in s.holes:
                number_position = [222,493]
                screen.blit(number, number_position)
                p = [639,533]
                screen.blit(sc_number, p)
            if 14 in s.holes:
                number_position = [278,436]
                screen.blit(number, number_position)
                p = [79,532]
                screen.blit(sc_number, p)
            if 15 in s.holes:
                number_position = [333,437]
                screen.blit(number, number_position)
                p = [545,487]
                screen.blit(sc_number, p)
            if 16 in s.holes:
                number_position = [389,322]
                screen.blit(number, number_position)
            if 17 in s.holes:
                number_position = [444,494]
                screen.blit(number, number_position)
                p = [546,579]
                screen.blit(sc_number, p)
            if 18 in s.holes:
                number_position = [220,321]
                screen.blit(number, number_position)
                p = [125,579]
                screen.blit(sc_number, p)
            if 19 in s.holes:
                number_position = [445,380]
                screen.blit(number, number_position)
                p = [638,580]
                screen.blit(sc_number, p)
            if 20 in s.holes:
                number_position = [390,380]
                screen.blit(number, number_position)
                p = [34,489]
                screen.blit(sc_number, p)
            if 21 in s.holes:
                number_position = [390,494]
                screen.blit(number, number_position)
            if 22 in s.holes:
                number_position = [277,494]
                screen.blit(number, number_position)
                p = [125,488]
                screen.blit(sc_number, p)
            if 23 in s.holes:
                number_position = [390,550]
                screen.blit(number, number_position)
                p = [639,486]
                screen.blit(sc_number, p)
            if 24 in s.holes:
                number_position = [278,380]
                screen.blit(number, number_position)
                p = [80,580]
                screen.blit(sc_number, p)
            if 25 in s.holes:
                number_position = [334,494]
                screen.blit(number, number_position)

        if s.game.hold_feature.position == 1:
            p = [130,722]
            screen.blit(hold_arrow, p)
        elif s.game.hold_feature.position == 2:
            p = [166,722]
            screen.blit(hold_arrow, p)
        elif s.game.hold_feature.position == 3:
            p = [200,722]
            screen.blit(hold_arrow, p)
        elif s.game.hold_feature.position == 4:
            p = [234,722]
            screen.blit(hold_arrow, p)
        elif s.game.hold_feature.position == 5:
            p = [268,722]
            screen.blit(hold_arrow, p)
        elif s.game.hold_feature.position == 6:
            p = [300,722]
            screen.blit(hold_arrow, p)
        elif s.game.hold_feature.position == 7:
            p = [333,722]
            screen.blit(hold_arrow, p)
        elif s.game.hold_feature.position == 8:
            p = [374,678]
            screen.blit(hold, p)
            if s.game.ball_count.position < 5:
                p = [409,766]
                screen.blit(hold_now, p)

        if s.game.super_card1.status == True:
            p = [34,448]
            screen.blit(sc, p)
        if s.game.super_card2.status == True:
            p = [548,448]
            screen.blit(sc, p)

        if s.game.spotted_numbers.position == 1:
            p = [24,631]
            screen.blit(hold_arrow, p)
        if s.game.spotted_numbers.position == 2:
            p = [60,633]
            screen.blit(hold_arrow, p)
        if s.game.spotted_numbers.position == 3:
            p = [96,633]
            screen.blit(hold_arrow, p)
        if s.game.spotted_numbers.position == 4:
            p = [130,633]
            screen.blit(hold_arrow, p)
        if s.game.spotted_numbers.position == 5:
            p = [168,633]
            screen.blit(hold_arrow, p)
        if s.game.spotted_numbers.position >= 6:
            p = [204,620]
            screen.blit(spotted, p)
        if s.game.spotted_numbers.position >= 7:
            p = [397,631]
            screen.blit(spotted_number, p)
            if s.game.spotted.position == 0 and s.game.ball_count.position < 4:
                number_position = [443,436]
                screen.blit(red_number, number_position)
        if s.game.spotted_numbers.position >= 8:
            p = [437,631]
            screen.blit(spotted_number, p)
            if s.game.spotted.position == 1 and s.game.ball_count.position < 4:
                number_position = [220,436]
                screen.blit(red_number, number_position)
        if s.game.spotted_numbers.position >= 9:
            p = [477,631]
            screen.blit(spotted_number, p)
            if s.game.spotted.position == 2 and s.game.ball_count.position < 4:
                number_position = [332,550]
                screen.blit(red_number, number_position)
        if s.game.spotted_numbers.position >= 10:
            p = [519,631]
            screen.blit(spotted_number, p)
            if s.game.spotted.position == 3 and s.game.ball_count.position < 4:
                number_position = [332,322]
                screen.blit(red_number, number_position)
        if s.game.spotted_numbers.position >= 11:
            p = [562,631]
            screen.blit(spotted_number, p)
            if s.game.spotted.position == 4 and s.game.ball_count.position < 4:
                number_position = [389,322]
                screen.blit(red_number, number_position)
        if s.game.spotted_numbers.position >= 12:
            p = [603,631]
            screen.blit(spotted_number, p)
            if s.game.spotted.position == 5 and s.game.ball_count.position < 4:
                number_position = [278,436]
                screen.blit(red_number, number_position)
        if s.game.spotted_numbers.position >= 13:
            p = [645,631]
            screen.blit(spotted_number, p)
            if s.game.spotted.position == 6 and s.game.ball_count.position < 4:
                number_position = [389,436]
                screen.blit(red_number, number_position)

    if s.game.spotted_numbers.position >= 7:
        if s.game.ball_count.position == 3:
            s.cancel_delayed(name="blink")
            blink([s,1,1])
        else:
            s.cancel_delayed(name="blink")

    if s.game.corners.status == True:
        p = [41,255]
        screen.blit(corners, p)

    if s.game.tilt.status == True:
        tilt_position = [580,250]
        screen.blit(tilt, tilt_position)

    pygame.display.update()

def blink(args):
    dirty_rects = []
    s = args[0]
    b = args[1]
    sn = args[2]

    if b == 0:
        if sn == 1:
            p = [239,666]
            dirty_rects.append(screen.blit(select_now, p))
        pygame.display.update(dirty_rects)
    else:
        dirty_rects.append(screen.blit(bg_gi, (239,666), pygame.Rect(239,666,140,32)))
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
        dirty_rects.append(screen.blit(bg_gi, (62,1011), pygame.Rect(62,1011,45,34)))
    if s.game.extra_ball.position < 2:
        dirty_rects.append(screen.blit(bg_gi, (110,1011), pygame.Rect(110,1011,60,34)))
    if s.game.extra_ball.position < 3:
        dirty_rects.append(screen.blit(bg_gi, (174,1011), pygame.Rect(174,1011,60,34)))
    if s.game.extra_ball.position < 4:
        dirty_rects.append(screen.blit(bg_gi, (274,1011), pygame.Rect(274,1011,45,34)))
    if s.game.extra_ball.position < 5:
        dirty_rects.append(screen.blit(bg_gi, (320,1011), pygame.Rect(320,1011,60,34)))
    if s.game.extra_ball.position < 6:
        dirty_rects.append(screen.blit(bg_gi, (385,1011), pygame.Rect(385,1011,60,34)))
    if s.game.extra_ball.position < 7:
        dirty_rects.append(screen.blit(bg_gi, (481,1011), pygame.Rect(481,1011,45,34)))
    if s.game.extra_ball.position < 8:
        dirty_rects.append(screen.blit(bg_gi, (529,1011), pygame.Rect(529,1011,60,34)))
    if s.game.extra_ball.position < 9:
        dirty_rects.append(screen.blit(bg_gi, (594,1011), pygame.Rect(594,1011,60,34)))

    pygame.display.update(dirty_rects)
    if num in [0,24,25,49]:
        if s.game.extra_ball.position < 1:
            p = [62,1011]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [1,15,26,40]:
        if s.game.extra_ball.position < 2:
            p = [110,1011]
            dirty_rects.append(screen.blit(eb2, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [3,4,17,28,29,42]:
        if s.game.extra_ball.position < 3:
            p = [174,1011]
            dirty_rects.append(screen.blit(eb2, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [5,18,30,43]:
        if s.game.extra_ball.position < 4:
            p = [274,1011]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [7,8,19,32,33,44]:
        if s.game.extra_ball.position < 5:
            p = [320,1011]
            dirty_rects.append(screen.blit(eb2, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [9,10,20,34,35,45]:
        if s.game.extra_ball.position < 6:
            p = [385,1011]
            dirty_rects.append(screen.blit(eb2, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [11,21,36,46]:
        if s.game.extra_ball.position < 7:
            p = [481,1011]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [12,22,37,47]:
        if s.game.extra_ball.position < 8:
            p = [529,1011]
            dirty_rects.append(screen.blit(eb2, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [2,6,13,16,23,27,31,38,41,48]:
        if s.game.extra_ball.position < 9:
            p = [594,1011]
            dirty_rects.append(screen.blit(eb2, p))
            pygame.display.update(dirty_rects) 
            return

def clear_odds(s, num):
    global screen

    dirty_rects = []
    if s.game.odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (82,820), pygame.Rect(82,820,33,105)))
    if s.game.odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (122,819), pygame.Rect(122,819,52,115)))
    if s.game.odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (172,821), pygame.Rect(172,821,48,127)))
    if s.game.odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (282,817), pygame.Rect(282,817,38,110)))
    if s.game.odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (384,820), pygame.Rect(384,820,44,105)))
    if s.game.odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (463,817), pygame.Rect(463,817,56,125)))
    if s.game.odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (568,818), pygame.Rect(568,818,43,108)))
    if s.game.odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (619,820), pygame.Rect(619,820,57,113)))

    pygame.display.update(dirty_rects)

def draw_odds_animation(s, num):
    global screen
    dirty_rects = []

    if num in [3,28]:
        if s.game.odds.position != 1:
            p = [82,820]
            dirty_rects.append(screen.blit(odds1, p))
            pygame.display.update(dirty_rects)
            return
    if num in [4,5,17,29,30,42]:
        if s.game.odds.position != 2:
            p = [122,819]
            dirty_rects.append(screen.blit(odds2, p))
            pygame.display.update(dirty_rects)
            return
    if num in [6,7,18,19,31,32,43,44]:
        if s.game.odds.position != 3:
            p = [172,821]
            dirty_rects.append(screen.blit(odds3, p))
            pygame.display.update(dirty_rects)
            return
    if num in [8,9,20,21,33,34,45,46]:
        if s.game.odds.position != 4:
            p = [282,817]
            dirty_rects.append(screen.blit(odds4, p))
            pygame.display.update(dirty_rects)
            return
    if num in [10,11,22,35,36,47]:
        if s.game.odds.position != 5:
            p = [384,820]
            dirty_rects.append(screen.blit(odds5, p))
            pygame.display.update(dirty_rects)
            return
    if num in [12,13,23,37,38,48]:
        if s.game.odds.position != 6:
            p = [463,817]
            dirty_rects.append(screen.blit(odds6, p))
            pygame.display.update(dirty_rects)
            return
    if num in [14,15,24,39,40,49]:
        if s.game.odds.position != 7:
            p = [568,818]
            dirty_rects.append(screen.blit(odds7, p))
            pygame.display.update(dirty_rects)
            return
    if num in [16,25,41,50]:
        if s.game.odds.position != 8:
            p = [619,820]
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
    if s.game.hold_feature.position < 8:
        dirty_rects.append(screen.blit(bg_gi, (374,678), pygame.Rect(374,678,233,93)))
    if s.game.super_card1.status == False:
        dirty_rects.append(screen.blit(bg_gi, (34,448), pygame.Rect(34,448,130,40)))
    if s.game.super_card2.status == False:
        dirty_rects.append(screen.blit(bg_gi, (548,448), pygame.Rect(548,448,130,40)))
    if s.game.spotted_numbers.position < 7:
        dirty_rects.append(screen.blit(bg_gi, (204,620), pygame.Rect(204,620,189,50)))
        dirty_rects.append(screen.blit(bg_gi, (397,631), pygame.Rect(397,631,36,38)))
    if s.game.spotted_numbers.position < 8:
        dirty_rects.append(screen.blit(bg_gi, (437,631), pygame.Rect(437,631,36,38)))
    if s.game.spotted_numbers.position < 9:
        dirty_rects.append(screen.blit(bg_gi, (477,631), pygame.Rect(477,631,36,38)))
    if s.game.spotted_numbers.position < 10:
        dirty_rects.append(screen.blit(bg_gi, (519,631), pygame.Rect(519,631,36,38)))
    if s.game.spotted_numbers.position < 11:
        dirty_rects.append(screen.blit(bg_gi, (562,631), pygame.Rect(562,631,36,38)))
    if s.game.spotted_numbers.position < 12:
        dirty_rects.append(screen.blit(bg_gi, (603,631), pygame.Rect(603,631,36,38)))
    if s.game.spotted_numbers.position < 13:
        dirty_rects.append(screen.blit(bg_gi, (645,631), pygame.Rect(645,631,36,38)))
    if s.game.corners.status == False:
        dirty_rects.append(screen.blit(bg_gi, (41,255), pygame.Rect(41,255,117,118)))

    pygame.display.update(dirty_rects)


def draw_feature_animation(s, num):
    global screen
    dirty_rects = []
 
    if num in [9,10,19,25,34,35,44,0]:
        if s.game.hold_feature.position < 8:
            p = [374,678]
            dirty_rects.append(screen.blit(hold, p))
            pygame.display.update(dirty_rects)
    if num in [20,45,5,30]:
        if s.game.super_card1.status == False:
            p = [34,448]
            dirty_rects.append(screen.blit(sc, p))
            pygame.display.update(dirty_rects)
    if num in [2,12,27,37]:
        if s.game.super_card2.status == False:
            p = [548,448]
            dirty_rects.append(screen.blit(sc, p))
            pygame.display.update(dirty_rects)
    if num in [1,26,9,34]:
        if s.game.spotted_numbers.position < 7:
            p = [204,620]
            dirty_rects.append(screen.blit(spotted, p))
            p = [397,631]
            dirty_rects.append(screen.blit(spotted_number, p))
            pygame.display.update(dirty_rects)
    if num in [2,27,10,35]:
        if s.game.spotted_numbers.position < 8:
            p = [437,631]
            dirty_rects.append(screen.blit(spotted_number, p))
            pygame.display.update(dirty_rects)
    if num in [3,28,11,36]:
        if s.game.spotted_numbers.position < 9:
            p = [477,631]
            dirty_rects.append(screen.blit(spotted_number, p))
            pygame.display.update(dirty_rects)
    if num in [4,29,12,37]:
        if s.game.spotted_numbers.position < 10:
            p = [519,631]
            dirty_rects.append(screen.blit(spotted_number, p))
            pygame.display.update(dirty_rects)
    if num in [5,30,13,38]:
        if s.game.spotted_numbers.position < 11:
            p = [562,631]
            dirty_rects.append(screen.blit(spotted_number, p))
            pygame.display.update(dirty_rects)
    if num in [6,31,14,39]:
        if s.game.spotted_numbers.position < 12:
            p = [603,631]
            dirty_rects.append(screen.blit(spotted_number, p))
            pygame.display.update(dirty_rects)
    if num in [7,32,15,40]:
        if s.game.spotted_numbers.position < 13:
            p = [645,631]
            dirty_rects.append(screen.blit(spotted_number, p))
            pygame.display.update(dirty_rects)
    if num in [8,18,33,43]:
        if s.game.corners.status == False:
            p = [41,255]
            dirty_rects.append(screen.blit(corners, p))
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


