
import pygame
import random

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

meter = pygame.image.load('graphics/assets/register_cover.png').convert()
odds1 = pygame.image.load('big_wheel/assets/odds1.png').convert_alpha()
odds2 = pygame.image.load('big_wheel/assets/odds2.png').convert_alpha()
odds3 = pygame.image.load('big_wheel/assets/odds3.png').convert_alpha()
odds4 = pygame.image.load('big_wheel/assets/odds4.png').convert_alpha()
odds5 = pygame.image.load('big_wheel/assets/odds5.png').convert_alpha()
odds6 = pygame.image.load('big_wheel/assets/odds6.png').convert_alpha()
odds7 = pygame.image.load('big_wheel/assets/odds7.png').convert_alpha()
odds8 = pygame.image.load('big_wheel/assets/odds8.png').convert_alpha()
odds9 = pygame.image.load('big_wheel/assets/odds9.png').convert_alpha()
time = pygame.image.load('big_wheel/assets/time.png').convert_alpha()
w_letter = pygame.image.load('big_wheel/assets/w_letter.png').convert_alpha()
up_arrow = pygame.image.load('big_wheel/assets/up_arrow.png').convert_alpha()
select_now = pygame.image.load('big_wheel/assets/select_now.png').convert_alpha()
tilt = pygame.image.load('big_wheel/assets/tilt.png').convert_alpha()
button = pygame.image.load('big_wheel/assets/button.png').convert_alpha()
wheel = pygame.image.load('big_wheel/assets/wheel.png').convert_alpha()
wheel1 = pygame.image.load('big_wheel/assets/wheel1.png').convert_alpha()
wheel2 = pygame.image.load('big_wheel/assets/wheel2.png').convert_alpha()
wheel3 = pygame.image.load('big_wheel/assets/wheel3.png').convert_alpha()
wheel4 = pygame.image.load('big_wheel/assets/wheel4.png').convert_alpha()
wheel5 = pygame.image.load('big_wheel/assets/wheel5.png').convert_alpha()
wheel6 = pygame.image.load('big_wheel/assets/wheel6.png').convert_alpha()
wheel7 = pygame.image.load('big_wheel/assets/wheel7.png').convert_alpha()
wheel8 = pygame.image.load('big_wheel/assets/wheel8.png').convert_alpha()
wheel9 = pygame.image.load('big_wheel/assets/wheel9.png').convert_alpha()
wheel10 = pygame.image.load('big_wheel/assets/wheel10.png').convert_alpha()
wheel11 = pygame.image.load('big_wheel/assets/wheel11.png').convert_alpha()
wheel12 = pygame.image.load('big_wheel/assets/wheel12.png').convert_alpha()
wheel13 = pygame.image.load('big_wheel/assets/wheel13.png').convert_alpha()
wheel14 = pygame.image.load('big_wheel/assets/wheel14.png').convert_alpha()
wheel15 = pygame.image.load('big_wheel/assets/wheel15.png').convert_alpha()
wheel16 = pygame.image.load('big_wheel/assets/wheel16.png').convert_alpha()
wheel17 = pygame.image.load('big_wheel/assets/wheel17.png').convert_alpha()
wheel18 = pygame.image.load('big_wheel/assets/wheel18.png').convert_alpha()
wheel19 = pygame.image.load('big_wheel/assets/wheel19.png').convert_alpha()
wheel_letters = pygame.image.load('big_wheel/assets/wheel_letters.png').convert_alpha()
dn_color = pygame.image.load('big_wheel/assets/dn_color.png').convert_alpha()
dn = pygame.image.load('big_wheel/assets/dn.png').convert_alpha()
dn_arrow = pygame.image.load('big_wheel/assets/dn_arrow.png').convert_alpha()
number = pygame.image.load('big_wheel/assets/number.png').convert_alpha()
spin_wheel = pygame.image.load('big_wheel/assets/spin_wheel.png').convert_alpha()
circle = pygame.image.load('big_wheel/assets/circle.png').convert_alpha()
bg_menu = pygame.image.load('big_wheel/assets/big_wheel_menu.png').convert_alpha()
bg_gi = pygame.image.load('big_wheel/assets/big_wheel_gi.png').convert_alpha()
bg_off = pygame.image.load('big_wheel/assets/big_wheel_off.png').convert_alpha()
 
class scorereel():
    """ Score Reels are used to count replays """
    def __init__(self, pos, image):
        self.position = pos
        self.default_y = self.position[1]
        self.image = pygame.image.load(image).convert()

reel1 = scorereel([92,280], "graphics/assets/white_reel.png")
reel10 = scorereel([73,280], "graphics/assets/white_reel.png")
reel100 = scorereel([54,280], "graphics/assets/white_reel.png")

def display(s, replays=0, menu=False):
    
    meter.set_colorkey((255,0,252))
    meter_position = [45,280]

    screen.blit(reel1.image, reel1.position)
    screen.blit(reel10.image, reel10.position)
    screen.blit(reel100.image, reel100.position)
    screen.blit(meter, meter_position)


    wheel_position = [261,418]
    if s.game.ring.position == 0:
        screen.blit(wheel, wheel_position)
    elif s.game.ring.position == 1:
        screen.blit(wheel1, wheel_position)
    elif s.game.ring.position == 2:
        screen.blit(wheel2, wheel_position)
    elif s.game.ring.position == 3:
        screen.blit(wheel3, wheel_position)
    elif s.game.ring.position == 4:
        screen.blit(wheel4, wheel_position)
    elif s.game.ring.position == 5:
        screen.blit(wheel5, wheel_position)
    elif s.game.ring.position == 6:
        screen.blit(wheel6, wheel_position)
    elif s.game.ring.position == 7:
        screen.blit(wheel7, wheel_position)
    elif s.game.ring.position == 8:
        screen.blit(wheel8, wheel_position)
    elif s.game.ring.position == 9:
        screen.blit(wheel9, wheel_position)
    elif s.game.ring.position == 10:
        screen.blit(wheel10, wheel_position)
    elif s.game.ring.position == 11:
        screen.blit(wheel11, wheel_position)
    elif s.game.ring.position == 12:
        screen.blit(wheel12, wheel_position)
    elif s.game.ring.position == 13:
        screen.blit(wheel13, wheel_position)
    elif s.game.ring.position == 14:
        screen.blit(wheel14, wheel_position)
    elif s.game.ring.position == 15:
        screen.blit(wheel15, wheel_position)
    elif s.game.ring.position == 16:
        screen.blit(wheel16, wheel_position)
    elif s.game.ring.position == 17:
        screen.blit(wheel17, wheel_position)
    elif s.game.ring.position == 18:
        screen.blit(wheel18, wheel_position)
    elif s.game.ring.position == 19:
        screen.blit(wheel19, wheel_position)

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

    wheel_letter_pos = [297,450]
    screen.blit(wheel_letters, wheel_letter_pos)
    

    if s.game.ball_count.position < 1:
        if s.game.odds_only.status == True:
            b = [16,1044]
            screen.blit(button, b)
        elif s.game.features.status == True:
            b = [193,1042]
            screen.blit(button, b)
        elif s.game.special.status == True:
            b = [545,1040]
            screen.blit(button, b)
        else:
            b = [369,1041]
            screen.blit(button, b)

    if s.game.double.status == True:
        if s.game.winner == 3:
            p = [120,860]
            screen.blit(circle, p)
        if s.game.winner == 6:
            p = [157,860]
            screen.blit(circle, p)
        if s.game.winner == 9:
            p = [194,860]
            screen.blit(circle, p)
        if s.game.winner == 12:
            p = [232,860]
            screen.blit(circle, p)
        if s.game.winner == 18:
            p = [268,860]
            screen.blit(circle, p)
        if s.game.winner == 24:
            p = [305,859]
            screen.blit(circle, p)
        if s.game.winner == 36:
            p = [342,859]
            screen.blit(circle, p)
        if s.game.winner == 48:
            p = [378,858]
            screen.blit(circle, p)
        if s.game.winner == 72:
            p = [451,858]
            screen.blit(circle, p)
        if s.game.winner == 64:
            p = [415,858]
            screen.blit(circle, p)
        if s.game.winner == 100:
            p = [488,859]
            screen.blit(circle, p)
        if s.game.winner == 144:
            p = [524,857]
            screen.blit(circle, p)
        if s.game.winner == 200:
            p = [562,858]
            screen.blit(circle, p)
    if s.game.double_double.status == True:
        if s.game.winner == 3:
            p = [121,816]
            screen.blit(circle, p)
        if s.game.winner == 6:
            p = [157,817]
            screen.blit(circle, p)
        if s.game.winner == 9:
            p = [195,816]
            screen.blit(circle, p)
        if s.game.winner == 12:    
            p = [232,816]
            screen.blit(circle, p)
        if s.game.winner == 18: 
            p = [268,816]
            screen.blit(circle, p)
        if s.game.winner == 24:
            p = [305,815]
            screen.blit(circle, p)
        if s.game.winner == 36:
            p = [342,816]
            screen.blit(circle, p)
        if s.game.winner == 48:
            p = [378,815]
            screen.blit(circle, p)
        if s.game.winner == 72:
            p = [451,815]
            screen.blit(circle, p)
        if s.game.winner == 64:
            p = [416,815]
            screen.blit(circle, p)
        if s.game.winner == 100:
            p = [488,815]
            screen.blit(circle, p)
        if s.game.winner == 144:
            p = [526,815]
            screen.blit(circle, p)
        if s.game.winner == 200:
            p = [562,816]
            screen.blit(circle, p)

    if s.game.odds.position == 1:
        p = [100,952]
        screen.blit(odds1, p)
    if s.game.odds.position == 2:
        p = [156,952]
        screen.blit(odds2, p)
    if s.game.odds.position == 3:
        p = [223,952]
        screen.blit(odds3, p)
    if s.game.odds.position == 4:
        p = [286,952]
        screen.blit(odds4, p)
    if s.game.odds.position == 5:
        p = [345,951]
        screen.blit(odds5, p)
    if s.game.odds.position == 6:
        p = [401,951]
        screen.blit(odds6, p)
    if s.game.odds.position == 7:
        p = [465,951]
        screen.blit(odds7, p)
    if s.game.odds.position == 8:
        p = [522,950]
        screen.blit(odds8, p)
    if s.game.odds.position == 9:
        p = [586,950]
        screen.blit(odds9, p)
    
    if s.game.tilt.status == False:
        if 1 in s.holes:
            p = [227,508]
            screen.blit(number, p)
        if 2 in s.holes:
            p = [357,377]
            screen.blit(number, p)
        if 3 in s.holes:
            p = [288,593]
            screen.blit(number, p)
        if 4 in s.holes:
            p = [259,411]
            screen.blit(number, p)
        if 5 in s.holes:
            p = [450,508]
            screen.blit(number, p)
        if 6 in s.holes:
            p = [390,592]
            screen.blit(number, p)
        if 7 in s.holes:
            p = [439,438]
            screen.blit(number, p)
        if 8 in s.holes:
            p = [240,439]
            screen.blit(number, p)
        if 9 in s.holes:
            p = [289,390]
            screen.blit(number, p)
        if 10 in s.holes:
            p = [390,389]
            screen.blit(number, p)
        if 11 in s.holes:
            p = [322,378]
            screen.blit(number, p)
        if 12 in s.holes:
            p = [439,542]
            screen.blit(number, p)
        if 13 in s.holes:
            p = [357,603]
            screen.blit(number, p)
        if 14 in s.holes:
            p = [261,571]
            screen.blit(number, p)
        if 15 in s.holes:
            p = [228,472]
            screen.blit(number, p)
        if 16 in s.holes:
            p = [450,471]
            screen.blit(number, p)
        if 17 in s.holes:
            p = [418,408]
            screen.blit(number, p)
        if 18 in s.holes:
            p = [418,570]
            screen.blit(number, p)
        if 19 in s.holes:
            p = [321,604]
            screen.blit(number, p)
        if 20 in s.holes:
            p = [240,543]
            screen.blit(number, p)

    if s.game.ball_count.position == 5 and s.game.double.status == False and s.game.replay_counter.position == 0 and s.game.winner > 0:
        s.cancel_delayed(name="blink_double")
        blink_double([s,1,1])
    elif s.game.ball_count.position == 3 and s.game.double_double.status == False and s.game.double.status == True and s.game.replay_counter.position == 0 and s.game.winner > 0:
        s.cancel_delayed(name="blink_double")
        blink_double([s,1,1])
    else:
        s.cancel_delayed("blink_double")

    if s.game.double_colors.position >= 1:
        p = [94,754]
        screen.blit(dn_color, p)
    if s.game.double_colors.position == 2:
        p = [187,767]
        screen.blit(dn_arrow, p)
    if s.game.double_colors.position == 3:
        p = [217,767]
        screen.blit(dn_arrow, p)
    if s.game.double_colors.position >= 4:
        p = [238,754]
        screen.blit(dn_color, p)
    if s.game.double_colors.position == 5:
        p = [332,767]
        screen.blit(dn_arrow, p)
    if s.game.double_colors.position == 6:
        p = [360,764]
        screen.blit(dn_arrow, p)
    if s.game.double_colors.position >= 7:
        p = [384,752]
        screen.blit(dn_color, p)
    if s.game.double_colors.position == 8:
        p = [477,764]
        screen.blit(dn_arrow, p)
    if s.game.double_colors.position == 9:
        p = [506,764]
        screen.blit(dn_arrow, p)
    if s.game.double_colors.position == 10:
        p = [527,751]
        screen.blit(dn_color, p)

    if s.game.wheel.position > 0:
        if s.game.selection_feature.position in [1,2,3,4]:
            p = [570,645]
            screen.blit(time, p)
        if s.game.selection_feature.position == 2:
            p = [619,620]
            screen.blit(up_arrow, p)
        if s.game.selection_feature.position == 3:
            p = [619,592]
            screen.blit(up_arrow, p)
        if s.game.selection_feature.position == 4:
            p = [619,563]
            screen.blit(up_arrow, p)
        if s.game.selection_feature.position in [5,6,7,8]:
            p = [571,509]
            screen.blit(time, p)
        if s.game.selection_feature.position == 6:
            p = [619,484]
            screen.blit(up_arrow, p)
        if s.game.selection_feature.position == 7:
            p = [619,455]
            screen.blit(up_arrow, p)
        if s.game.selection_feature.position == 8:
            p = [619,429]
            screen.blit(up_arrow, p)
        if s.game.selection_feature.position == 9:
            p = [571,373]
            screen.blit(time, p)

        p = [83,397]
        screen.blit(spin_wheel, p)
        t = 3
        if s.game.selection_feature.position in [5,6,7,8]:
            t = 4
        elif s.game.selection_feature.position == 9:
            t = 5
        if s.game.ball_count.position == t:
            s.cancel_delayed(name="blink")
            blink([s,1,1])
        else:
            s.cancel_delayed(name="blink")
    if s.game.wheel.position >= 1:
        p = [17,655]
        screen.blit(w_letter, p)
    if s.game.wheel.position == 2:
        p = [31,633]
        screen.blit(up_arrow, p)
    if s.game.wheel.position >= 3:
        p = [18,586]
        screen.blit(w_letter, p)
    if s.game.wheel.position == 4:
        p = [31,563]
        screen.blit(up_arrow, p)
    if s.game.wheel.position >= 5:
        p = [18,518]
        screen.blit(w_letter, p)
    if s.game.wheel.position == 6:
        p = [31,495]
        screen.blit(up_arrow, p)
    if s.game.wheel.position >= 7:
        p = [18,448]
        screen.blit(w_letter, p)
    if s.game.wheel.position == 8:
        p = [31,425]
        screen.blit(up_arrow, p)
    if s.game.wheel.position == 9:
        p = [18,378]
        screen.blit(w_letter, p)

    if s.game.tilt.status == True:
        tilt_position = [551,317]
        screen.blit(tilt, tilt_position)

    pygame.display.update()


def blink_double(args):
    dirty_rects = []
    s = args[0]
    b = args[1]
    sn = args[2]

    if b == 0:
        if sn == 1:
            p = [137,905]
            dirty_rects.append(screen.blit(dn, p))
        pygame.display.update(dirty_rects)
    else:
        dirty_rects.append(screen.blit(bg_gi, (137,905), pygame.Rect(137,905,445,34)))
        pygame.display.update(dirty_rects)
    b = not b

    args = [s,b,sn]

    s.delay(name="blink_double", delay=0.1, handler=blink_double, param=args)

def blink(args):
    dirty_rects = []
    s = args[0]
    b = args[1]
    sn = args[2]

    if b == 0:
        if sn == 1:
            p = [81,606]
            dirty_rects.append(screen.blit(select_now, p))
        pygame.display.update(dirty_rects)
    else:
        dirty_rects.append(screen.blit(bg_gi, (81,606), pygame.Rect(81,606,59,70)))
        pygame.display.update(dirty_rects)
    b = not b

    args = [s,b,sn]

    s.delay(name="blink", delay=0.1, handler=blink, param=args)

def clear_odds(s, num):
    global screen

    dirty_rects = []

    if s.game.odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (100,952), pygame.Rect(100,952,18,77)))
    if s.game.odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (156,952), pygame.Rect(156,952,24,77)))
    if s.game.odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (223,952), pygame.Rect(223,952,24,77)))
    if s.game.odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (286,952), pygame.Rect(286,952,24,77)))
    if s.game.odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (345,951), pygame.Rect(345,951,24,77)))
    if s.game.odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (401,951), pygame.Rect(401,951,24,77)))
    if s.game.odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (465,951), pygame.Rect(465,951,24,77)))
    if s.game.odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (522,950), pygame.Rect(522,950,34,76)))
    if s.game.odds.position != 9:
        dirty_rects.append(screen.blit(bg_gi, (586,950), pygame.Rect(586,950,34,76)))

    pygame.display.update(dirty_rects)

def draw_odds_animation(s, num):
    global screen
    dirty_rects = []

    if num in [6,21,31,46]:
        if s.game.odds.position != 1:
            p = [100,952]
            dirty_rects.append(screen.blit(odds1, p))
            pygame.display.update(dirty_rects)
            return
    if num in [7,22,32,47]:
        if s.game.odds.position != 2:
            p = [156,952]
            dirty_rects.append(screen.blit(odds2, p))
            pygame.display.update(dirty_rects)
            return
    if num in [8,14,23,33,39,48]:
        if s.game.odds.position != 3:
            p = [223,952]
            dirty_rects.append(screen.blit(odds3, p))
            pygame.display.update(dirty_rects)
            return
    if num in [9,15,24,34,40,49]:
        if s.game.odds.position != 4:
            p = [286,952]
            dirty_rects.append(screen.blit(odds4, p))
            pygame.display.update(dirty_rects)
            return
    if num in [1,10,16,26,35,41]:
        if s.game.odds.position != 5:
            p = [345,951]
            dirty_rects.append(screen.blit(odds5, p))
            pygame.display.update(dirty_rects)
            return
    if num in [2,11,17,27,36,42]:
        if s.game.odds.position != 6:
            p = [401,951]
            dirty_rects.append(screen.blit(odds6, p))
            pygame.display.update(dirty_rects)
            return
    if num in [3,12,18,28,37,43]:
        if s.game.odds.position != 7:
            p = [465,951]
            dirty_rects.append(screen.blit(odds7, p))
            pygame.display.update(dirty_rects)
            return
    if num in [4,13,19,29,38,44]:
        if s.game.odds.position != 8:
            p = [522,950]
            dirty_rects.append(screen.blit(odds8, p))
            pygame.display.update(dirty_rects)
            return
    if num in [5,14,20,30,39,45]:
        if s.game.odds.position != 9:
            p = [586,950]
            dirty_rects.append(screen.blit(odds9, p))
            pygame.display.update(dirty_rects)
            return

def odds_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]

    clear_odds(s, num)

    draw_odds_animation(s, num)

def clear_double(s):
    global screen
    dirty_rects = []
    if s.game.double_colors.position < 1:
        dirty_rects.append(screen.blit(bg_gi, (94,754), pygame.Rect(94,754,93,52)))
    if s.game.double_colors.position < 2:
        dirty_rects.append(screen.blit(bg_gi, (187,767), pygame.Rect(187,767,22,26)))
    if s.game.double_colors.position < 3:
        dirty_rects.append(screen.blit(bg_gi, (217,767), pygame.Rect(217,767,22,26)))
    if s.game.double_colors.position < 4:
        dirty_rects.append(screen.blit(bg_gi, (238,754), pygame.Rect(238,754,93,52)))
    if s.game.double_colors.position < 5:
        dirty_rects.append(screen.blit(bg_gi, (332,767), pygame.Rect(332,767,22,26)))
    if s.game.double_colors.position < 6:
        dirty_rects.append(screen.blit(bg_gi, (360,767), pygame.Rect(360,767,22,26)))
    if s.game.double_colors.position < 7:
        dirty_rects.append(screen.blit(bg_gi, (384,752), pygame.Rect(384,752,93,52)))
    if s.game.double_colors.position < 8:
        dirty_rects.append(screen.blit(bg_gi, (477,764), pygame.Rect(477,764,22,26)))
    if s.game.double_colors.position < 9:
        dirty_rects.append(screen.blit(bg_gi, (506,764), pygame.Rect(506,764,22,26)))
    if s.game.double_colors.position < 10:
        dirty_rects.append(screen.blit(bg_gi, (527,751), pygame.Rect(527,751,93,52)))

    pygame.display.update(dirty_rects)

def draw_double_animation(args):
    global screen
    dirty_rects = []
    s = args[0]
    num = args[1]

    clear_double(s)

    if num in [6,16,31,41]:
        if s.game.double_colors.position < 1:
            p = [94,754]
            dirty_rects.append(screen.blit(dn_color, p))
            pygame.display.update(dirty_rects)
            return
    if num in [7,17,32,42]:
        if s.game.double_colors.position < 2:
            p = [187,767]
            dirty_rects.append(screen.blit(dn_arrow, p))
            pygame.display.update(dirty_rects)
            return
    if num in [8,18,33,43]:
        if s.game.double_colors.position < 3:
            p = [217,767]
            dirty_rects.append(screen.blit(dn_arrow, p))
            pygame.display.update(dirty_rects)
            return
    if num in [9,19,34,44]:
        if s.game.double_colors.position < 4:
            p = [238,754]
            dirty_rects.append(screen.blit(dn_color, p))
            pygame.display.update(dirty_rects)
            return
    if num in [10,20,35,45]:
        if s.game.double_colors.position < 5:
            p = [332,767]
            dirty_rects.append(screen.blit(dn_arrow, p))
            pygame.display.update(dirty_rects)
            return
    if num in [1,11,21,26,36,46]:
        if s.game.double_colors.position < 6:
            p = [360,767]
            dirty_rects.append(screen.blit(dn_arrow, p))
            pygame.display.update(dirty_rects)
            return
    if num in [2,12,22,27,37,47]:
        if s.game.double_colors.position < 7:
            p = [384,752]
            dirty_rects.append(screen.blit(dn_color, p))
            pygame.display.update(dirty_rects)
            return
    if num in [3,13,23,28,38,48]:
        if s.game.double_colors.position < 8:
            p = [477,764]
            dirty_rects.append(screen.blit(dn_arrow, p))
            pygame.display.update(dirty_rects)
            return
    if num in [4,14,24,29,39,49]:
        if s.game.double_colors.position < 9:
            p = [506,764]
            dirty_rects.append(screen.blit(dn_arrow, p))
            pygame.display.update(dirty_rects)
            return
    if num in [5,15,25,30,40,0]:
        if s.game.double_colors.position < 10:
            p = [527,751]
            dirty_rects.append(screen.blit(dn_color, p))
            pygame.display.update(dirty_rects)
            return


def clear_features(s, num):
    global screen

    dirty_rects = []

    if s.game.wheel.position < 1:
        dirty_rects.append(screen.blit(bg_gi, (17,655), pygame.Rect(17,655,61,43)))
    if s.game.wheel.position < 2:
        dirty_rects.append(screen.blit(bg_gi, (31,633), pygame.Rect(31,633,37,22)))
    if s.game.wheel.position < 3:
        dirty_rects.append(screen.blit(bg_gi, (18,586), pygame.Rect(18,586,61,43)))
    if s.game.wheel.position < 4:
        dirty_rects.append(screen.blit(bg_gi, (31,563), pygame.Rect(31,563,37,22)))
    if s.game.wheel.position < 5:
        dirty_rects.append(screen.blit(bg_gi, (18,518), pygame.Rect(18,518,61,43)))
    if s.game.wheel.position < 6:
        dirty_rects.append(screen.blit(bg_gi, (31,495), pygame.Rect(31,495,37,22)))
    if s.game.wheel.position < 7:
        dirty_rects.append(screen.blit(bg_gi, (18,448), pygame.Rect(18,448,61,43)))
    if s.game.wheel.position < 8:
        dirty_rects.append(screen.blit(bg_gi, (31,425), pygame.Rect(31,425,37,22)))
    if s.game.wheel.position < 9:
        dirty_rects.append(screen.blit(bg_gi, (18,378), pygame.Rect(18,378,61,43)))

    if s.game.selection_feature.position not in [1,2,3,4]:
        dirty_rects.append(screen.blit(bg_gi, (570,645), pygame.Rect(570,645,130,50)))
    if s.game.selection_feature.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (619,620), pygame.Rect(619,620,37,22)))
    if s.game.selection_feature.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (619,592), pygame.Rect(619,592,37,22)))
    if s.game.selection_feature.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (619,563), pygame.Rect(619,563,37,22)))
    if s.game.selection_feature.position not in [5,6,7,8]:
        dirty_rects.append(screen.blit(bg_gi, (571,509), pygame.Rect(571,509,130,50)))
    if s.game.selection_feature.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (619,484), pygame.Rect(619,484,37,22)))
    if s.game.selection_feature.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (619,455), pygame.Rect(619,455,37,22)))
    if s.game.selection_feature.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (619,429), pygame.Rect(619,429,37,22)))
    if s.game.selection_feature.position != 9:
        dirty_rects.append(screen.blit(bg_gi, (571,373), pygame.Rect(571,373,130,50)))

    pygame.display.update(dirty_rects)


def draw_feature_animation(s, num):
    global screen
    dirty_rects = []

    if num in [7,16,32,41]:
        if s.game.wheel.position < 1:
            p = [17,655]
            dirty_rects.append(screen.blit(w_letter, p))
            pygame.display.update(dirty_rects)
    if num in [8,17,33,42]:
        if s.game.wheel.position < 2:
            p = [31,633]
            dirty_rects.append(screen.blit(up_arrow, p))
            pygame.display.update(dirty_rects)
    if num in [0,9,18,25,34,43]:
        if s.game.wheel.position < 3:
            p = [18,586]
            dirty_rects.append(screen.blit(w_letter, p))
            pygame.display.update(dirty_rects)
    if num in [1,10,19,26,35,44]:
        if s.game.wheel.position < 4:
            p = [31,563]
            dirty_rects.append(screen.blit(up_arrow, p))
            pygame.display.update(dirty_rects)
    if num in [2,11,20,27,36,45]:
        if s.game.wheel.position < 5:
            p = [18,518]
            dirty_rects.append(screen.blit(w_letter, p))
            pygame.display.update(dirty_rects)
    if num in [3,12,21,28,37,46]:
        if s.game.wheel.position < 6:
            p = [31,495]
            dirty_rects.append(screen.blit(up_arrow, p))
            pygame.display.update(dirty_rects)
    if num in [4,13,22,29,38,47]:
        if s.game.wheel.position < 7:
            p = [18,448]
            dirty_rects.append(screen.blit(w_letter, p))
            pygame.display.update(dirty_rects)
    if num in [5,14,23,30,39,48]:
        if s.game.wheel.position < 8:
            p = [31,425]
            dirty_rects.append(screen.blit(up_arrow, p))
            pygame.display.update(dirty_rects)
    if num in [6,15,24,31,40,49]:
        if s.game.wheel.position < 9:
            p = [18,378]
            dirty_rects.append(screen.blit(w_letter, p))
            pygame.display.update(dirty_rects)

    if num in [7,16,32,41]:
        if s.game.selection_feature.position not in [1,2,3,4]:
            p = [570,645]
            dirty_rects.append(screen.blit(time, p))
            pygame.display.update(dirty_rects)
    if num in [8,17,33,42]:
        if s.game.selection_feature.position != 2:
            p = [619,620]
            dirty_rects.append(screen.blit(up_arrow, p))
            pygame.display.update(dirty_rects)
    if num in [0,9,18,25,34,43]:
        if s.game.selection_feature.position != 3:
            p = [619,592]
            dirty_rects.append(screen.blit(up_arrow, p))
            pygame.display.update(dirty_rects)
    if num in [1,10,19,26,35,44]:
        if s.game.selection_feature.position != 4:
            p = [619,563]
            dirty_rects.append(screen.blit(up_arrow, p))
            pygame.display.update(dirty_rects)
    if num in [2,11,20,27,36,45]:
        if s.game.selection_feature.position not in [5,6,7,8]:
            p = [571,509]
            dirty_rects.append(screen.blit(time, p))
            pygame.display.update(dirty_rects)
    if num in [3,12,21,28,37,46]:
        if s.game.selection_feature.position != 6:
            p = [619,484]
            dirty_rects.append(screen.blit(up_arrow, p))
            pygame.display.update(dirty_rects)
    if num in [4,13,22,29,38,47]:
        if s.game.selection_feature.position != 7:
            p = [619,455]
            dirty_rects.append(screen.blit(up_arrow, p))
            pygame.display.update(dirty_rects)
    if num in [5,14,23,30,39,48]:
        if s.game.selection_feature.position != 8:
            p = [619,429]
            dirty_rects.append(screen.blit(up_arrow, p))
            pygame.display.update(dirty_rects)
    if num in [6,15,24,31,40,49]:
        if s.game.selection_feature.position != 9:
            p = [571,373]
            dirty_rects.append(screen.blit(time, p))
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
