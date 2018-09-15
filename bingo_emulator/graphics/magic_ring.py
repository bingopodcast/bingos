
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
            b = [366,1052]
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

def wheel_animation(args):
    dirty_rects = []
    s = args[0]
    num = args[1]
    direction = args[2]
    
    p = [270,418]
    if s.game.ring.position == 0:
        w = wheel
    elif s.game.ring.position == 1:
        w = wheel1
    elif s.game.ring.position == 2:
        w = wheel2
    elif s.game.ring.position == 3:
        w = wheel3
    elif s.game.ring.position == 4:
        w = wheel4
    elif s.game.ring.position == 5:
        w = wheel5
    elif s.game.ring.position == 6:
        w = wheel6
    elif s.game.ring.position == 7:
        w = wheel7
    elif s.game.ring.position == 8:
        w = wheel8
    elif s.game.ring.position == 9:
        w = wheel9
    elif s.game.ring.position == 10:
        w = wheel10
    elif s.game.ring.position == 11:
        w = wheel11
    elif s.game.ring.position == 12:
        w = wheel12
    elif s.game.ring.position == 13:
        w = wheel13
    elif s.game.ring.position == 14:
        w = wheel14
    elif s.game.ring.position == 15:
        w = wheel15
    elif s.game.ring.position == 16:
        w = wheel16
    elif s.game.ring.position == 17:
        w = wheel17
    elif s.game.ring.position == 18:
        w = wheel18
    elif s.game.ring.position == 19:
        w = wheel19

    if direction == "left":
        num = num * -1 + 4
    else:
        num = num - 2

    old_rect = pygame.Rect(p[0],p[1],180,178)
    old_center = old_rect.center
    img_rotated = pygame.transform.rotate(w,num)
    rect = img_rotated.get_rect()
    rect.center = old_center

    dirty_rects.append(screen.blit(img_rotated, rect))

    if (s.game.anti_cheat.status == True):
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],180,178)))
    else:
        dirty_rects.append(screen.blit(bg_off, p, pygame.Rect(p[0],p[1],180,178)))
    
    wheel_letter_pos = [305,450]
    dirty_rects.append(screen.blit(wheel_letters, wheel_letter_pos))
    
    pygame.display.update(dirty_rects)



def clear_odds(s, num):
    global screen

    dirty_rects = []

    if s.game.green_odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (236,962), pygame.Rect(236,962,45,23)))
        dirty_rects.append(screen.blit(bg_gi, (236,987), pygame.Rect(236,987,45,23)))
        dirty_rects.append(screen.blit(bg_gi, (236,1013), pygame.Rect(236,1013,45,23)))
    if s.game.green_odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (297,962), pygame.Rect(297,962,45,23)))
        dirty_rects.append(screen.blit(bg_gi, (297,988), pygame.Rect(297,988,45,23)))
        dirty_rects.append(screen.blit(bg_gi, (297,1014), pygame.Rect(297,1014,45,23)))
    if s.game.green_odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (360,962), pygame.Rect(360,962,45,23)))
        dirty_rects.append(screen.blit(bg_gi, (360,988), pygame.Rect(360,988,45,23)))
        dirty_rects.append(screen.blit(bg_gi, (358,1015), pygame.Rect(358,1015,45,23)))
    if s.game.green_odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (417,963), pygame.Rect(417,963,45,23)))
        dirty_rects.append(screen.blit(bg_gi, (417,988), pygame.Rect(417,988,45,23)))
        dirty_rects.append(screen.blit(bg_gi, (417,1015), pygame.Rect(417,1015,45,23)))
    if s.game.green_odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (477,962), pygame.Rect(477,962,45,23)))
        dirty_rects.append(screen.blit(bg_gi, (476,988), pygame.Rect(476,988,45,23)))
        dirty_rects.append(screen.blit(bg_gi, (476,1015), pygame.Rect(476,1015,45,23)))
    if s.game.green_odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (536,962), pygame.Rect(536,962,45,23)))
        dirty_rects.append(screen.blit(bg_gi, (536,988), pygame.Rect(536,988,45,23)))
        dirty_rects.append(screen.blit(bg_gi, (536,1014), pygame.Rect(536,1014,45,23)))
    if s.game.green_odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (596,961), pygame.Rect(596,961,45,23)))
        dirty_rects.append(screen.blit(bg_gi, (595,986), pygame.Rect(595,986,45,23)))
        dirty_rects.append(screen.blit(bg_gi, (594,1012), pygame.Rect(594,1012,45,23)))
    if s.game.green_odds.position != 9:
        dirty_rects.append(screen.blit(bg_gi, (654,960), pygame.Rect(654,960,45,23)))
        dirty_rects.append(screen.blit(bg_gi, (653,985), pygame.Rect(653,985,45,23)))
        dirty_rects.append(screen.blit(bg_gi, (653,1012), pygame.Rect(653,1012,45,23)))
    if s.game.yellow_odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (236,902), pygame.Rect(236,902,45,23)))
        dirty_rects.append(screen.blit(bg_gi, (236,926), pygame.Rect(236,926,45,23)))
    if s.game.yellow_odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (296,902), pygame.Rect(296,902,45,23)))
        dirty_rects.append(screen.blit(bg_gi, (296,926), pygame.Rect(296,926,45,23)))
    if s.game.yellow_odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (356,902), pygame.Rect(356,902,45,23)))
        dirty_rects.append(screen.blit(bg_gi, (360,926), pygame.Rect(360,926,45,23)))
    if s.game.yellow_odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (416,902), pygame.Rect(416,902,45,23)))
        dirty_rects.append(screen.blit(bg_gi, (416,926), pygame.Rect(416,926,45,23)))
    if s.game.yellow_odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (476,902), pygame.Rect(476,902,45,23)))
        dirty_rects.append(screen.blit(bg_gi, (476,926), pygame.Rect(476,926,45,23)))
    if s.game.yellow_odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (536,900), pygame.Rect(536,900,45,23)))
        dirty_rects.append(screen.blit(bg_gi, (536,926), pygame.Rect(536,926,45,23)))
    if s.game.yellow_odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (596,900), pygame.Rect(596,900,45,23)))
        dirty_rects.append(screen.blit(bg_gi, (595,924), pygame.Rect(595,924,45,23)))
    if s.game.yellow_odds.position != 9:
        dirty_rects.append(screen.blit(bg_gi, (654,898), pygame.Rect(654,898,45,23)))
        dirty_rects.append(screen.blit(bg_gi, (653,923), pygame.Rect(653,923,45,23)))
    if s.game.red_odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (234,869), pygame.Rect(234,869,45,23)))
    if s.game.red_odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (296,869), pygame.Rect(296,869,45,23)))
    if s.game.red_odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (356,869), pygame.Rect(356,869,45,23)))
    if s.game.red_odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (416,868), pygame.Rect(416,868,45,23)))
    if s.game.red_odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (476,868), pygame.Rect(476,868,45,23)))
    if s.game.red_odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (536,868), pygame.Rect(536,868,45,23)))
    if s.game.red_odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (596,868), pygame.Rect(596,868,45,23)))
    if s.game.red_odds.position != 9:
        dirty_rects.append(screen.blit(bg_gi, (654,868), pygame.Rect(654,868,45,23)))


    pygame.display.update(dirty_rects)

def draw_odds_animation(s, num):
    global screen
    dirty_rects = []

    if num in [38,5,0,17,12,29,42,25]:
        if s.game.green_odds.position != 2:
            p = [236,962]
            dirty_rects.append(screen.blit(odds, p))
            p = [236,987]
            dirty_rects.append(screen.blit(odds, p))
            p = [236,1013]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
    if num in [37,4,36,16,11,28,41,24]:
        if s.game.green_odds.position != 3:
            p = [297,962]
            dirty_rects.append(screen.blit(odds, p))
            p = [297,988]
            dirty_rects.append(screen.blit(odds, p))
            p = [297,1014]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
    if num in [36,3,35,15,10,27,40,23]:
        if s.game.green_odds.position != 4:
            p = [360,962]
            dirty_rects.append(screen.blit(odds, p))
            p = [360,988]
            dirty_rects.append(screen.blit(odds, p))
            p = [358,1015]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
    if num in [35,2,34,14,9,26,39,22]:
        if s.game.green_odds.position != 5:
            p = [417,963]
            dirty_rects.append(screen.blit(odds, p))
            p = [417,988]
            dirty_rects.append(screen.blit(odds, p))
            p = [417,1015]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
    if num in [34,1,33,13,8,25,38,21]:
        if s.game.green_odds.position != 6:
            p = [477,962]
            dirty_rects.append(screen.blit(odds, p))
            p = [476,988]
            dirty_rects.append(screen.blit(odds, p))
            p = [476,1015]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
    if num in [33,0,32,12,7,24,37,20]:
        if s.game.green_odds.position != 7:
            p = [536,962]
            dirty_rects.append(screen.blit(odds, p))
            p = [536,988]
            dirty_rects.append(screen.blit(odds, p))
            p = [536,1014]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
    if num in [32,49,31,11,6,23,36,19]:
        if s.game.green_odds.position != 8:
            p = [596,961]
            dirty_rects.append(screen.blit(odds, p))
            p = [595,986]
            dirty_rects.append(screen.blit(odds, p))
            p = [594,1012]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
    if num in [31,48,43,10,5,22,35,18]:
        if s.game.green_odds.position != 9:
            p = [654,960]
            dirty_rects.append(screen.blit(odds, p))
            p = [653,985]
            dirty_rects.append(screen.blit(odds, p))
            p = [653,1012]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
    if num in [13,21,25,33,0,8,37,45]:
        if s.game.yellow_odds.position != 2:
            p = [236,902]
            dirty_rects.append(screen.blit(odds, p))
            p = [236,926]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
    if num in [12,20,24,32,49,7,36,44]:
        if s.game.yellow_odds.position != 3:
            p = [296,902]
            dirty_rects.append(screen.blit(odds, p))
            p = [296,926]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
    if num in [11,19,23,31,48,6,35,43]:
        if s.game.yellow_odds.position != 4:
            p = [356,902]
            dirty_rects.append(screen.blit(odds, p))
            p = [360,926]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
    if num in [10,18,22,30,47,5,34,42]:
        if s.game.yellow_odds.position != 5:
            p = [416,902]
            dirty_rects.append(screen.blit(odds, p))
            p = [416,926]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
    if num in [9,17,21,29,46,4,33,41]:
        if s.game.yellow_odds.position != 6:
            p = [476,902]
            dirty_rects.append(screen.blit(odds, p))
            p = [476,926]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
    if num in [8,16,20,28,45,3,32,40]:
        if s.game.yellow_odds.position != 7:
            p = [536,900]
            dirty_rects.append(screen.blit(odds, p))
            p = [536,926]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
    if num in [7,15,19,27,44,2,31,39]:
        if s.game.yellow_odds.position != 8:
            p = [596,900]
            dirty_rects.append(screen.blit(odds, p))
            p = [595,924]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
    if num in [6,14,18,26,43,1,30,38]:
        if s.game.yellow_odds.position != 9:
            p = [654,898]
            dirty_rects.append(screen.blit(odds, p))
            p = [653,923]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
    if num in [47,29,41,9,16,34,3,21]:
        if s.game.red_odds.position != 2:
            p = [653,923]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
    if num in [46,28,40,8,15,33,2,20,42,4,17,29]:
        if s.game.red_odds.position != 3:
            p = [296,869]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
    if num in [45,27,39,7,14,32,1,19]:
        if s.game.red_odds.position != 4:
            p = [356,869]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
    if num in [44,26,38,6,13,31,0,18]:
        if s.game.red_odds.position != 5:
            p = [416,868]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
    if num in [43,25,37,5,12,30,49,17]:
        if s.game.red_odds.position != 6:
            p = [476,868]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
    if num in [42,24,36,4,11,29,48,16]:
        if s.game.red_odds.position != 7:
            p = [536,868]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
    if num in [41,23,35,3,10,28,47,15]:
        if s.game.red_odds.position != 8:
            p = [596,868]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
    if num in [40,22,34,2,9,27,46,14]:
        if s.game.red_odds.position != 9:
            p = [654,868]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)

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
    if s.game.double_colors.position < 2:
        dirty_rects.append(screen.blit(bg_gi, (218,691), pygame.Rect(218,691,19,27)))
    if s.game.double_colors.position < 3:
        dirty_rects.append(screen.blit(bg_gi, (238,691), pygame.Rect(238,691,19,27)))
    if s.game.double_colors.position < 5:
        dirty_rects.append(screen.blit(bg_gi, (339,691), pygame.Rect(339,691,19,27)))
    if s.game.double_colors.position < 6:
        dirty_rects.append(screen.blit(bg_gi, (360,691), pygame.Rect(360,691,19,27)))
    if s.game.double_colors.position < 7:
        dirty_rects.append(screen.blit(bg_gi, (382,675), pygame.Rect(382,675,75,61)))
    if s.game.double_colors.position < 8:
        dirty_rects.append(screen.blit(bg_gi, (460,691), pygame.Rect(460,691,19,27)))
    if s.game.double_colors.position < 9:
        dirty_rects.append(screen.blit(bg_gi, (481,691), pygame.Rect(481,691,19,27)))
    if s.game.double_colors.position < 10:
        dirty_rects.append(screen.blit(bg_gi, (503,675), pygame.Rect(503,675,75,61)))

    pygame.display.update(dirty_rects)

def draw_double_animation(args):
    global screen
    dirty_rects = []
    s = args[0]
    num = args[1]

    clear_double(s)


    if num in [47,5,22,30]:
        if s.game.double_colors.position < 2:
            p = [218,691]
            dirty_rects.append(screen.blit(dn_arrow, p))
            pygame.display.update(dirty_rects)
            return
    if num in [46,4,21,29]:
        if s.game.double_colors.position < 3:
            p = [238,691]
            dirty_rects.append(screen.blit(dn_arrow, p))
            pygame.display.update(dirty_rects)
            return
    if num in [45,3,20,28]:
        if s.game.double_colors.position < 5:
            p = [339,691]
            dirty_rects.append(screen.blit(dn_arrow, p))
            pygame.display.update(dirty_rects)
            return
    if num in [44,2,19,27]:
        if s.game.double_colors.position < 6:
            p = [360,691]
            dirty_rects.append(screen.blit(dn_arrow, p))
            pygame.display.update(dirty_rects)
            return
    if num in [39,43,1,9,14,18,26,34]:
        if s.game.double_colors.position < 7:
            p = [382,675]
            dirty_rects.append(screen.blit(dn_color, p))
            pygame.display.update(dirty_rects)
            return
    if num in [38,42,0,8,13,17,25,35]:
        if s.game.double_colors.position < 8:
            p = [460,691]
            dirty_rects.append(screen.blit(dn_arrow, p))
            pygame.display.update(dirty_rects)
            return
    if num in [37,41,49,7,12,16,24,34]:
        if s.game.double_colors.position < 9:
            p = [481,691]
            dirty_rects.append(screen.blit(dn_arrow, p))
            pygame.display.update(dirty_rects)
            return
    if num in [36,40,48,6,11,15,23,33]:
        if s.game.double_colors.position < 10:
            p = [503,675]
            dirty_rects.append(screen.blit(dn_color, p))
            pygame.display.update(dirty_rects)
            return


def clear_features(s, num):
    global screen

    dirty_rects = []

    if s.game.wheel.position < 2:
        dirty_rects.append(screen.blit(bg_gi, (41,523), pygame.Rect(41,523,30,20)))
    if s.game.wheel.position < 3:
        dirty_rects.append(screen.blit(bg_gi, (25,475), pygame.Rect(25,475,63,48)))
    if s.game.wheel.position < 4:
        dirty_rects.append(screen.blit(bg_gi, (41,451), pygame.Rect(41,451,30,20)))
    if s.game.wheel.position < 5:
        dirty_rects.append(screen.blit(bg_gi, (26,404), pygame.Rect(26,404,63,48)))
    if s.game.wheel.position < 6:
        dirty_rects.append(screen.blit(bg_gi, (42,382), pygame.Rect(42,382,30,20)))
    if s.game.wheel.position < 7:
        dirty_rects.append(screen.blit(bg_gi, (27,334), pygame.Rect(27,334,63,48)))
    if s.game.wheel.position < 8:
        dirty_rects.append(screen.blit(bg_gi, (43,312), pygame.Rect(43,312,30,20)))
    if s.game.wheel.position < 9:
        dirty_rects.append(screen.blit(bg_gi, (27,265), pygame.Rect(27,265,63,48)))

    if s.game.selection_feature.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (610,511), pygame.Rect(610,511,30,20)))
    if s.game.selection_feature.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (610,482), pygame.Rect(610,482,30,20)))
    if s.game.selection_feature.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (608,454), pygame.Rect(608,454,30,20)))
    if s.game.selection_feature.position not in [5,6,7,8]:
        dirty_rects.append(screen.blit(bg_gi, (559,393), pygame.Rect(559,393,133,57)))
    if s.game.selection_feature.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (607,372), pygame.Rect(607,372,30,20)))
    if s.game.selection_feature.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (607,343), pygame.Rect(607,343,30,20)))
    if s.game.selection_feature.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (607,314), pygame.Rect(607,314,30,20)))
    if s.game.selection_feature.position != 9:
        dirty_rects.append(screen.blit(bg_gi, (558,255), pygame.Rect(558,255,133,57)))
    if s.game.three_stars.status == False:
        dirty_rects.append(screen.blit(bg_gi, (591,734), pygame.Rect(591,734,106,46)))
    if s.game.six_stars.status == False:
        dirty_rects.append(screen.blit(bg_gi, (590,779), pygame.Rect(590,779,106,46)))
    
    if s.game.double_up.status == False:
        dirty_rects.append(screen.blit(bg_gi, (193,813), pygame.Rect(193,813,334,48)))
    pygame.display.update(dirty_rects)


def draw_feature_animation(s, num):
    global screen
    dirty_rects = []

    if num in [2,27]:
        if s.game.wheel.position < 2:
            p = [41,523]
            dirty_rects.append(screen.blit(up_arrow, p))
            pygame.display.update(dirty_rects)
    if num in [0,25]:
        if s.game.wheel.position < 3:
            p = [25,475]
            dirty_rects.append(screen.blit(w_letter, p))
            pygame.display.update(dirty_rects)
    if num in [48,23]:
        if s.game.wheel.position < 4:
            p = [41,451]
            dirty_rects.append(screen.blit(up_arrow, p))
            pygame.display.update(dirty_rects)
    if num in [46,21]:
        if s.game.wheel.position < 5:
            p = [26,404]
            dirty_rects.append(screen.blit(w_letter, p))
            pygame.display.update(dirty_rects)
    if num in [44,19]:
        if s.game.wheel.position < 6:
            p = [42,382]
            dirty_rects.append(screen.blit(up_arrow, p))
            pygame.display.update(dirty_rects)
    if num in [43,10,17,35]:
        if s.game.wheel.position < 7:
            p = [27,334]
            dirty_rects.append(screen.blit(w_letter, p))
            pygame.display.update(dirty_rects)
    if num in [40,8,15,33]:
        if s.game.wheel.position < 8:
            p = [43,312]
            dirty_rects.append(screen.blit(up_arrow, p))
            pygame.display.update(dirty_rects)
    if num in [38,6,13,31]:
        if s.game.wheel.position < 9:
            p = [27,265]
            dirty_rects.append(screen.blit(w_letter, p))
            pygame.display.update(dirty_rects)

    if num in [9,34]:
        if s.game.selection_feature.position != 2:
            p = [610,511]
            dirty_rects.append(screen.blit(up_arrow, p))
            pygame.display.update(dirty_rects)
    if num in [7,32]:
        if s.game.selection_feature.position != 3:
            p = [610,482]
            dirty_rects.append(screen.blit(up_arrow, p))
            pygame.display.update(dirty_rects)
    if num in [5,30]:
        if s.game.selection_feature.position != 4:
            p = [608,454]
            dirty_rects.append(screen.blit(up_arrow, p))
            pygame.display.update(dirty_rects)
    if num in [3,28]:
        if s.game.selection_feature.position not in [5,6,7,8]:
            p = [559,393]
            dirty_rects.append(screen.blit(time, p))
            pygame.display.update(dirty_rects)
    if num in [1,26]:
        if s.game.selection_feature.position != 6:
            p = [607,372]
            dirty_rects.append(screen.blit(up_arrow, p))
            pygame.display.update(dirty_rects)
    if num in [49,24]:
        if s.game.selection_feature.position != 7:
            p = [607,343]
            dirty_rects.append(screen.blit(up_arrow, p))
            pygame.display.update(dirty_rects)
    if num in [15,40]:
        if s.game.selection_feature.position != 8:
            p = [607,314]
            dirty_rects.append(screen.blit(up_arrow, p))
            pygame.display.update(dirty_rects)
    if num in [38,13,45,20]:
        if s.game.selection_feature.position != 9:
            p = [558,255]
            dirty_rects.append(screen.blit(time, p))
            pygame.display.update(dirty_rects)
    if num in [36,11]:
        if s.game.three_stars.status == False:
            p = [591,734]
            dirty_rects.append(screen.blit(stars, p))
            pygame.display.update(dirty_rects)
    if num in [47,22]:
        if s.game.six_stars.status == False:
            p = [590,779]
            dirty_rects.append(screen.blit(stars, p))
            pygame.display.update(dirty_rects)
    if num in [17,42]:
        if s.game.double_up.status == False:
            p = [193,813]
            dirty_rects.append(screen.blit(double_up, p))
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
