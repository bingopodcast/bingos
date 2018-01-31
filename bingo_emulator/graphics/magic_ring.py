
import pygame
import random

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

meter = pygame.image.load('graphics/assets/black_register_cover.png').convert()
odds = pygame.image.load('magic_ring/assets/odds.png').convert_alpha()
time = pygame.image.load('magic_ring/assets/time.png').convert_alpha()
w_letter = pygame.image.load('magic_ring/assets/w_letter.png').convert_alpha()
up_arrow = pygame.image.load('magic_ring/assets/up_arrow.png').convert_alpha()
select_now = pygame.image.load('magic_ring/assets/select_now.png').convert_alpha()
tilt = pygame.image.load('magic_ring/assets/tilt.png').convert_alpha()
button = pygame.image.load('magic_ring/assets/button.png').convert_alpha()
wheel = pygame.image.load('magic_ring/assets/wheel.png').convert_alpha()
wheel1 = pygame.image.load('magic_ring/assets/wheel1.png').convert_alpha()
wheel2 = pygame.image.load('magic_ring/assets/wheel2.png').convert_alpha()
wheel3 = pygame.image.load('magic_ring/assets/wheel3.png').convert_alpha()
wheel4 = pygame.image.load('magic_ring/assets/wheel4.png').convert_alpha()
wheel5 = pygame.image.load('magic_ring/assets/wheel5.png').convert_alpha()
wheel6 = pygame.image.load('magic_ring/assets/wheel6.png').convert_alpha()
wheel7 = pygame.image.load('magic_ring/assets/wheel7.png').convert_alpha()
wheel8 = pygame.image.load('magic_ring/assets/wheel8.png').convert_alpha()
wheel9 = pygame.image.load('magic_ring/assets/wheel9.png').convert_alpha()
wheel10 = pygame.image.load('magic_ring/assets/wheel10.png').convert_alpha()
wheel11 = pygame.image.load('magic_ring/assets/wheel11.png').convert_alpha()
wheel12 = pygame.image.load('magic_ring/assets/wheel12.png').convert_alpha()
wheel13 = pygame.image.load('magic_ring/assets/wheel13.png').convert_alpha()
wheel14 = pygame.image.load('magic_ring/assets/wheel14.png').convert_alpha()
wheel15 = pygame.image.load('magic_ring/assets/wheel15.png').convert_alpha()
wheel16 = pygame.image.load('magic_ring/assets/wheel16.png').convert_alpha()
wheel17 = pygame.image.load('magic_ring/assets/wheel17.png').convert_alpha()
wheel18 = pygame.image.load('magic_ring/assets/wheel18.png').convert_alpha()
wheel19 = pygame.image.load('magic_ring/assets/wheel19.png').convert_alpha()
wheel_letters = pygame.image.load('magic_ring/assets/wheel_letters.png').convert_alpha()
dn_color = pygame.image.load('magic_ring/assets/dn_color.png').convert_alpha()
dn = pygame.image.load('magic_ring/assets/dn.png').convert_alpha()
dn_arrow = pygame.image.load('magic_ring/assets/dn_arrow.png').convert_alpha()
number = pygame.image.load('magic_ring/assets/number.png').convert_alpha()
spin_wheel = pygame.image.load('magic_ring/assets/spin_wheel.png').convert_alpha()
circle = pygame.image.load('magic_ring/assets/circle.png').convert_alpha()
collected = pygame.image.load('magic_ring/assets/collected.png').convert_alpha()
double_up = pygame.image.load('magic_ring/assets/double_up.png').convert_alpha()
stars = pygame.image.load('magic_ring/assets/stars.png').convert_alpha()
double_rectangle = pygame.image.load('magic_ring/assets/double_rectangle.png').convert_alpha()
bg_menu = pygame.image.load('magic_ring/assets/magic_ring_menu.png').convert_alpha()
bg_gi = pygame.image.load('magic_ring/assets/magic_ring_gi.png').convert_alpha()
bg_off = pygame.image.load('magic_ring/assets/magic_ring_off.png').convert_alpha()

class scorereel():
    """ Score Reels are used to count replays """
    def __init__(self, pos, image):
        self.position = pos
        self.default_y = self.position[1]
        self.image = pygame.image.load(image).convert()

reel1 = scorereel([105,815], "graphics/assets/white_reel.png")
reel10 = scorereel([86,815], "graphics/assets/white_reel.png")
reel100 = scorereel([67,815], "graphics/assets/white_reel.png")
reel1000 = scorereel([48,815], "graphics/assets/white_reel.png")

def display(s, replays=0, menu=False):
    
    meter.set_colorkey((255,0,252))
    meter_position = [38,815]

    screen.blit(reel1.image, reel1.position)
    screen.blit(reel10.image, reel10.position)
    screen.blit(reel100.image, reel100.position)
    screen.blit(reel1000.image, reel1000.position)
    screen.blit(meter, meter_position)


    wheel_position = [270,418]
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

    wheel_letter_pos = [305,450]
    screen.blit(wheel_letters, wheel_letter_pos)
    

    if s.game.ball_count.position < 1:
        if s.game.odds_only.status == True:
            b = [41,1046]
            screen.blit(button, b)
        elif s.game.features.status == True:
            b = [204,1051]
            screen.blit(button, b)
        elif s.game.special.status == True:
            b = [526,1049]
            screen.blit(button, b)
        else:
            b = [360,1052]
            screen.blit(button, b)

    if s.game.double.status == True:
        p = [224,741]
        screen.blit(double_rectangle, p)
    if s.game.double_double.status == True:
        p = [367,741]
        screen.blit(double_rectangle, p)

    if s.game.red_odds.position == 1:
        p = [176,868]
        screen.blit(odds, p)
    if s.game.red_odds.position == 2:
        p = [234,869]
        screen.blit(odds, p)
    if s.game.red_odds.position == 3:
        p = [296,869]
        screen.blit(odds, p)
    if s.game.red_odds.position == 4:
        p = [356,869]
        screen.blit(odds, p)
    if s.game.red_odds.position == 5:
        p = [416,868]
        screen.blit(odds, p)
    if s.game.red_odds.position == 6:
        p = [476,868]
        screen.blit(odds, p)
    if s.game.red_odds.position == 7:
        p = [536,868]
        screen.blit(odds, p)
    if s.game.red_odds.position == 8:
        p = [596,868]
        screen.blit(odds, p)
    if s.game.red_odds.position == 9:
        p = [654,868]
        screen.blit(odds, p)

    if s.game.yellow_odds.position == 1:
        p = [176,902]
        screen.blit(odds, p)
        p = [177,925]
        screen.blit(odds, p)
    if s.game.yellow_odds.position == 2:
        p = [236,902]
        screen.blit(odds, p)
        p = [236,926]
        screen.blit(odds, p)
    if s.game.yellow_odds.position == 3:
        p = [296,902]
        screen.blit(odds, p)
        p = [296,926]
        screen.blit(odds, p)
    if s.game.yellow_odds.position == 4:
        p = [356,902]
        screen.blit(odds, p)
        p = [360,926]
        screen.blit(odds, p)
    if s.game.yellow_odds.position == 5:
        p = [416,902]
        screen.blit(odds, p)
        p = [416,926]
        screen.blit(odds, p)
    if s.game.yellow_odds.position == 6:
        p = [476,902]
        screen.blit(odds, p)
        p = [476,926]
        screen.blit(odds, p)
    if s.game.yellow_odds.position == 7:
        p = [536,900]
        screen.blit(odds, p)
        p = [536,926]
        screen.blit(odds, p)
    if s.game.yellow_odds.position == 8:
        p = [596,900]
        screen.blit(odds, p)
        p = [595,924]
        screen.blit(odds, p)
    if s.game.yellow_odds.position == 9:
        p = [654,898]
        screen.blit(odds, p)
        p = [653,923]
        screen.blit(odds, p)

    if s.game.green_odds.position == 1:
        p = [177,960]
        screen.blit(odds, p)
        p = [178,987]
        screen.blit(odds, p)
        p = [178,1013]
        screen.blit(odds, p)
    if s.game.green_odds.position == 2:
        p = [236,962]
        screen.blit(odds, p)
        p = [236,987]
        screen.blit(odds, p)
        p = [236,1013]
        screen.blit(odds, p)
    if s.game.green_odds.position == 3:
        p = [297,962]
        screen.blit(odds, p)
        p = [297,988]
        screen.blit(odds, p)
        p = [297,1014]
        screen.blit(odds, p)
    if s.game.green_odds.position == 4:
        p = [360,962]
        screen.blit(odds, p)
        p = [360,988]
        screen.blit(odds, p)
        p = [358,1015]
        screen.blit(odds, p)
    if s.game.green_odds.position == 5:
        p = [417,963]
        screen.blit(odds, p)
        p = [417,988]
        screen.blit(odds, p)
        p = [417,1015]
        screen.blit(odds, p)
    if s.game.green_odds.position == 6:
        p = [477,962]
        screen.blit(odds, p)
        p = [476,988]
        screen.blit(odds, p)
        p = [476,1015]
        screen.blit(odds, p)
    if s.game.green_odds.position == 7:
        p = [536,962]
        screen.blit(odds, p)
        p = [536,988]
        screen.blit(odds, p)
        p = [536,1014]
        screen.blit(odds, p)
    if s.game.green_odds.position == 8:
        p = [596,961]
        screen.blit(odds, p)
        p = [595,986]
        screen.blit(odds, p)
        p = [594,1012]
        screen.blit(odds, p)
    if s.game.green_odds.position == 9:
        p = [654,960]
        screen.blit(odds, p)
        p = [653,985]
        screen.blit(odds, p)
        p = [653,1012]
        screen.blit(odds, p)
    
    if s.game.tilt.status == False:
        if 1 in s.holes:
            p = [231,507]
            screen.blit(number, p)
        if 2 in s.holes:
            p = [363,375]
            screen.blit(number, p)
        if 3 in s.holes:
            p = [291,593]
            screen.blit(number, p)
        if 4 in s.holes:
            p = [265,406]
            screen.blit(number, p)
        if 5 in s.holes:
            p = [458,508]
            screen.blit(number, p)
        if 6 in s.holes:
            p = [396,593]
            screen.blit(number, p)
        if 7 in s.holes:
            p = [447,438]
            screen.blit(number, p)
        if 8 in s.holes:
            p = [243,435]
            screen.blit(number, p)
        if 9 in s.holes:
            p = [293,386]
            screen.blit(number, p)
        if 10 in s.holes:
            p = [397,386]
            screen.blit(number, p)
        if 11 in s.holes:
            p = [328,376]
            screen.blit(number, p)
        if 12 in s.holes:
            p = [447,543]
            screen.blit(number, p)
        if 13 in s.holes:
            p = [360,606]
            screen.blit(number, p)
        if 14 in s.holes:
            p = [263,570]
            screen.blit(number, p)
        if 15 in s.holes:
            p = [232,468]
            screen.blit(number, p)
        if 16 in s.holes:
            p = [458,471]
            screen.blit(number, p)
        if 17 in s.holes:
            p = [426,407]
            screen.blit(number, p)
        if 18 in s.holes:
            p = [425,572]
            screen.blit(number, p)
        if 19 in s.holes:
            p = [326,605]
            screen.blit(number, p)
        if 20 in s.holes:
            p = [243,541]
            screen.blit(number, p)

    if s.game.ball_count.position == 5 and s.game.double.status == False:
        if (s.game.red_winner.status == True and s.game.red_replay_counter.position == 0) or (s.game.yellow_winner.status == True and s.game.yellow_replay_counter.position == 0) or (s.game.green_winner.status == True and s.game.green_replay_counter.position == 0):
            s.cancel_delayed(name="blink_double")
            blink_double([s,1,1])
    elif s.game.ball_count.position == 3 and s.game.double_double.status == False and s.game.double.status == True:
        if (s.game.red_winner.status == True and s.game.red_replay_counter.position == 0) or (s.game.yellow_winner.status == True and s.game.yellow_replay_counter.position == 0) or (s.game.green_winner.status == True and s.game.green_replay_counter.position == 0):
            s.cancel_delayed(name="blink_double")
            blink_double([s,1,1])
    else:
        s.cancel_delayed("blink_double")

    if s.game.double_colors.position >= 1:
        p = [140,675]
        screen.blit(dn_color, p)
    if s.game.double_colors.position == 2:
        p = [218,691]
        screen.blit(dn_arrow, p)
    if s.game.double_colors.position == 3:
        p = [238,691]
        screen.blit(dn_arrow, p)
    if s.game.double_colors.position >= 4:
        p = [260,675]
        screen.blit(dn_color, p)
    if s.game.double_colors.position == 5:
        p = [339,691]
        screen.blit(dn_arrow, p)
    if s.game.double_colors.position == 6:
        p = [360,691]
        screen.blit(dn_arrow, p)
    if s.game.double_colors.position >= 7:
        p = [382,675]
        screen.blit(dn_color, p)
    if s.game.double_colors.position == 8:
        p = [460,691]
        screen.blit(dn_arrow, p)
    if s.game.double_colors.position == 9:
        p = [481,691]
        screen.blit(dn_arrow, p)
    if s.game.double_colors.position == 10:
        p = [503,675]
        screen.blit(dn_color, p)

    if s.game.wheel.position > 0:
        if s.game.selection_feature.position in [1,2,3,4]:
            p = [560,534]
            screen.blit(time, p)
        if s.game.selection_feature.position == 2:
            p = [610,511]
            screen.blit(up_arrow, p)
        if s.game.selection_feature.position == 3:
            p = [610,482]
            screen.blit(up_arrow, p)
        if s.game.selection_feature.position == 4:
            p = [608,454]
            screen.blit(up_arrow, p)
        if s.game.selection_feature.position in [5,6,7,8]:
            p = [559,393]
            screen.blit(time, p)
        if s.game.selection_feature.position == 6:
            p = [607,372]
            screen.blit(up_arrow, p)
        if s.game.selection_feature.position == 7:
            p = [607,343]
            screen.blit(up_arrow, p)
        if s.game.selection_feature.position == 8:
            p = [607,314]
            screen.blit(up_arrow, p)
        if s.game.selection_feature.position == 9:
            p = [558,255]
            screen.blit(time, p)

        p = [92,284]
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
        p = [24,546]
        screen.blit(w_letter, p)
    if s.game.wheel.position == 2:
        p = [41,523]
        screen.blit(up_arrow, p)
    if s.game.wheel.position >= 3:
        p = [25,475]
        screen.blit(w_letter, p)
    if s.game.wheel.position == 4:
        p = [41,451]
        screen.blit(up_arrow, p)
    if s.game.wheel.position >= 5:
        p = [26,404]
        screen.blit(w_letter, p)
    if s.game.wheel.position == 6:
        p = [42,382]
        screen.blit(up_arrow, p)
    if s.game.wheel.position >= 7:
        p = [27,334]
        screen.blit(w_letter, p)
    if s.game.wheel.position == 8:
        p = [43,312]
        screen.blit(up_arrow, p)
    if s.game.wheel.position == 9:
        p = [27,265]
        screen.blit(w_letter, p)

    if s.game.red_replay_counter.position > 0:
        p = [29,618]
        screen.blit(collected, p)
    if s.game.yellow_replay_counter.position > 0:
        p = [29,661]
        screen.blit(collected, p)
    if s.game.green_replay_counter.position > 0:
        p = [29,705]
        screen.blit(collected, p)

    if s.game.double_up.status == True:
        p = [193,813]
        screen.blit(double_up, p)

    if s.game.tilt.status == True:
        tilt_position = [608,199]
        screen.blit(tilt, tilt_position)

    if s.game.three_stars.status == True:
        p = [591,734]
        screen.blit(stars, p)
    if s.game.six_stars.status == True:
        p = [590,779]
        screen.blit(stars, p)

    pygame.display.update()

def blink_double(args):
    dirty_rects = []
    s = args[0]
    b = args[1]
    sn = args[2]

    if b == 0:
        if sn == 1:
            p = [140,732]
            dirty_rects.append(screen.blit(dn, p))
        pygame.display.update(dirty_rects)
    else:
        dirty_rects.append(screen.blit(bg_gi, (140,732), pygame.Rect(140,732,433,74)))
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
            p = [90,495]
            dirty_rects.append(screen.blit(select_now, p))
        pygame.display.update(dirty_rects)
    else:
        dirty_rects.append(screen.blit(bg_gi, (90,495), pygame.Rect(90,495,63,78)))
        pygame.display.update(dirty_rects)
    b = not b

    args = [s,b,sn]

    s.delay(name="blink", delay=0.1, handler=blink, param=args)

def feature_animation(num):
    global screen

    if num == 4:
        p = [27,265]
        screen.blit(w_letter, p)
        pygame.display.update()
    else:
        p = [43,312]
        screen.blit(up_arrow, p)
        pygame.display.update()


def odds_animation(num):
    global screen

    if num == 8:
        p = [176,902]
        screen.blit(odds, p)
        p = [177,925]
        screen.blit(odds, p)
    if num == 7:
        p = [236,902]
        screen.blit(odds, p)
        p = [236,926]
        screen.blit(odds, p)
    if num == 6:
        p = [296,902]
        screen.blit(odds, p)
        p = [296,926]
        screen.blit(odds, p)
    if num == 5:
        p = [356,902]
        screen.blit(odds, p)
        p = [360,926]
        screen.blit(odds, p)
    if num == 4:
        p = [416,902]
        screen.blit(odds, p)
        p = [416,926]
        screen.blit(odds, p)
    if num == 3:
        p = [476,902]
        screen.blit(odds, p)
        p = [476,926]
        screen.blit(odds, p)
    if num == 2:
        p = [536,900]
        screen.blit(odds, p)
        p = [536,926]
        screen.blit(odds, p)
    if num == 1:
        p = [596,900]
        screen.blit(odds, p)
        p = [595,924]
        screen.blit(odds, p)
    pygame.display.update()


