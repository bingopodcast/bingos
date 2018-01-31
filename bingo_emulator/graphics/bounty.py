
import pygame
import random

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

meter = pygame.image.load('graphics/assets/register_cover.png').convert()
magic_screen = pygame.image.load('bounty/assets/magic_screen.png').convert()
number_card = pygame.image.load('bounty/assets/number_card.png').convert()
odds = pygame.image.load('bounty/assets/odds.png').convert_alpha()
eb = pygame.image.load('bounty/assets/eb.png').convert_alpha()
eb_number = pygame.image.load('bounty/assets/eb_number.png').convert_alpha()
extra_balls = pygame.image.load('bounty/assets/extra_balls.png').convert_alpha()
time = pygame.image.load('bounty/assets/time.png').convert_alpha()
ti = pygame.image.load('bounty/assets/time_indicator.png').convert_alpha()
super_section = pygame.image.load('bounty/assets/super_section.png').convert_alpha()
orange_section = pygame.image.load('bounty/assets/orange_section.png').convert_alpha()
ms_letter = pygame.image.load('bounty/assets/ms_letter.png').convert_alpha()
number = pygame.image.load('bounty/assets/number.png').convert_alpha()
select_now = pygame.image.load('bounty/assets/select_now.png').convert_alpha()
blue_section = pygame.image.load('bounty/assets/blue_section.png').convert_alpha()
tilt = pygame.image.load('bounty/assets/tilt.png').convert_alpha()
button = pygame.image.load('bounty/assets/button.png').convert_alpha()
ok = pygame.image.load('bounty/assets/ok.png').convert_alpha()
extra_ok = pygame.image.load('bounty/assets/extra_ok.png').convert_alpha()
super_ok = pygame.image.load('bounty/assets/super_ok.png').convert_alpha()
skill_shot = pygame.image.load('bounty/assets/skill_shot.png').convert_alpha()
skill_shot_number = pygame.image.load('bounty/assets/skill_shot_number.png').convert_alpha()
skill_shot_odds = pygame.image.load('bounty/assets/skill_shot_odds.png').convert_alpha()
shoot_now = pygame.image.load('bounty/assets/shoot_now.png').convert_alpha()
letter1 = pygame.image.load('bounty/assets/letter1.png').convert_alpha()
letter2 = pygame.image.load('bounty/assets/letter2.png').convert_alpha()
letter3 = pygame.image.load('bounty/assets/letter3.png').convert_alpha()
letter4 = pygame.image.load('bounty/assets/letter4.png').convert_alpha()
letter5 = pygame.image.load('bounty/assets/letter5.png').convert_alpha()
letter6 = pygame.image.load('bounty/assets/letter6.png').convert_alpha()
red_letter1 = pygame.image.load('bounty/assets/red_letter1.png').convert_alpha()
red_letter2 = pygame.image.load('bounty/assets/red_letter2.png').convert_alpha()
red_letter3 = pygame.image.load('bounty/assets/red_letter3.png').convert_alpha()
red_letter4 = pygame.image.load('bounty/assets/red_letter4.png').convert_alpha()
red_letter5 = pygame.image.load('bounty/assets/red_letter5.png').convert_alpha()
red_letter6 = pygame.image.load('bounty/assets/red_letter6.png').convert_alpha()
bg_menu = pygame.image.load('bounty/assets/bounty_menu.png').convert_alpha()
bg_gi = pygame.image.load('bounty/assets/bounty_gi.png').convert_alpha()
bg_off = pygame.image.load('bounty/assets/bounty_off.png').convert_alpha()

class scorereel():
    """ Score Reels are used to count replays """
    def __init__(self, pos, image):
        self.position = pos
        self.default_y = self.position[1]
        self.image = pygame.image.load(image).convert()

reel1 = scorereel([102,799], "graphics/assets/white_reel.png")
reel10 = scorereel([83,799], "graphics/assets/white_reel.png")
reel100 = scorereel([64,799], "graphics/assets/white_reel.png")

def display(s, replays=0, menu=False):
    
    meter.set_colorkey((255,0,252))
    meter_position = [55,799]

    screen.blit(reel1.image, reel1.position)
    screen.blit(reel10.image, reel10.position)
    screen.blit(reel100.image, reel100.position)
    screen.blit(meter, meter_position)

    number_card_position = [235,363]

    screen.blit(number_card, number_card_position)

    magic_screen.set_colorkey((255,0,252))
    #default position 230x 359y
    #subtract 47 per position
    if s.game.magic_screen.position == 0:
        magic_screen_position = [240,358]
    elif s.game.magic_screen.position == 1:
        magic_screen_position = [192,358]
    elif s.game.magic_screen.position == 2:
        magic_screen_position = [143,358]
    elif s.game.magic_screen.position == 3:
        magic_screen_position = [96,358]
    elif s.game.magic_screen.position == 4:
        magic_screen_position = [49,358]
    elif s.game.magic_screen.position == 5:
        magic_screen_position = [1,358]
    elif s.game.magic_screen.position == 6:
        magic_screen_position = [-45,358]
    elif s.game.magic_screen.position == 7:
        magic_screen_position = [-92,358]
    elif s.game.magic_screen.position == 8:
        magic_screen_position = [-139,358]
    elif s.game.magic_screen.position == 9:
        magic_screen_position = [-187,358]
    elif s.game.magic_screen.position == 10:
        magic_screen_position = [-234,358]


    screen.blit(magic_screen, magic_screen_position)

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

    if s.game.eb_play.status == True:
        eb_position = [22,1037]
        screen.blit(extra_balls, eb_position)

    if s.game.extra_ball.position >= 1:
        eb_position = [153,1037]
        screen.blit(eb_number, eb_position)
    if s.game.extra_ball.position >= 2:
        eb_position = [203,1037]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 3:
        eb_position = [269,1037]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 4:
        eb_position = [330,1037]
        screen.blit(eb_number, eb_position)
    if s.game.extra_ball.position >= 5:
        eb_position = [379,1037]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 6:
        eb_position = [446,1037]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 7:
        eb_position = [506,1037]
        screen.blit(eb_number, eb_position)
    if s.game.extra_ball.position >= 8:
        eb_position = [556,1037]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 9:
        eb_position = [622,1037]
        screen.blit(eb, eb_position)
    

    if s.game.selection_feature.position == 1:
        i = [672,594]
        screen.blit(ti, i)
    if s.game.selection_feature.position == 2 or s.game.selection_feature.position == 3:
        i = [672,534]
        screen.blit(ti, i)
    if s.game.selection_feature.position == 4 or s.game.selection_feature.position == 5 or s.game.selection_feature.position == 6:
        i = [672,474]
        screen.blit(ti, i)
    if s.game.selection_feature.position == 7:
        i = [672,417]
        screen.blit(ti, i)
    if s.game.selection_feature.position == 8:
        i = [672,364]
        screen.blit(ti, i)

    if s.game.red_star.status == True:
        rs_position = [550,466]
        screen.blit(time, rs_position)
    if s.game.yellow_star.status == True:
        rs_position = [550,522]
        screen.blit(time, rs_position)

    if s.game.magic_screen_feature.position >= 7 or s.game.ok.status == True:
        if s.game.selection_feature.position < 7:
            bfp = [554,580]
            screen.blit(time, bfp)
            if s.game.ball_count.position == 3:
                s.cancel_delayed(name="blink")
                blink([s,1,1])
            else:
                s.cancel_delayed(name="blink")
        elif s.game.selection_feature.position == 7:
            bfp = [554,410]
            screen.blit(time, bfp)
            if s.game.ball_count.position == 4:
                s.cancel_delayed(name="blink")
                blink([s,1,1])
            else:
                s.cancel_delayed(name="blink")
        elif s.game.selection_feature.position == 8:
            bfp = [554,351]
            screen.blit(time, bfp)
            if s.game.ball_count.position == 5:
                s.cancel_delayed(name="blink")
                blink([s,1,1])
            else:
                s.cancel_delayed(name="blink")

    if s.game.magic_screen_feature.position >= 9:
        if s.game.three_blue.status == True:
            bp = [16,956]
            screen.blit(blue_section, bp)
        elif s.game.three_blue_six.status == True:
            bp = [16,922]
            screen.blit(blue_section, bp)
        elif s.game.two_blue.status == True:
            bp = [16,888]
            screen.blit(blue_section, bp)


    if s.game.ball_count.position < 1:
        if s.game.ss.status == True:
            b = [38,986]
            screen.blit(button, b)
        elif s.game.odds_only.status == True:
            b = [198,986]
            screen.blit(button, b)
        elif s.game.features.status == True:
            b = [360,986]
            screen.blit(button, b)
        else:
            b = [523,986]
            screen.blit(button, b)


    if s.game.red_super_section.status == True:
        rss = [578,796]
        screen.blit(super_section, rss)
    if s.game.yellow_super_section.status == True:
        yss = [578,894]
        screen.blit(super_section, yss)
    
    if s.game.magic_screen_feature.position >= 4:
        ms = [228,674]
        screen.blit(ms_letter, ms)
    if s.game.magic_screen_feature.position >= 5:
        ms = [270,674]
        screen.blit(ms_letter, ms)
    if s.game.magic_screen_feature.position >= 6:
        ms = [314,674]
        screen.blit(ms_letter, ms)
    if s.game.magic_screen_feature.position >= 7:
        ms = [360,674]
        screen.blit(ms_letter, ms)
    if s.game.magic_screen_feature.position >= 8:
        ms = [401,674]
        screen.blit(ms_letter, ms)
    if s.game.magic_screen_feature.position >= 9:
        ms = [444,674]
        screen.blit(ms_letter, ms)
    if s.game.magic_screen_feature.position >= 10:
        ms = [486,674]
        screen.blit(ms_letter, ms)

    if s.game.ok.status == True:
        ms = [144,674]
        screen.blit(ok, ms)
    if s.game.extra_ok.status == True:
        ms = [86,674]
        screen.blit(extra_ok, ms)
    if s.game.super_ok.status == True:
        ms = [29,674]
        screen.blit(super_ok, ms)

    if s.game.tilt.status == False:
        if s.holes:
            if 1 in s.holes:
                number_position = [287,373]
                screen.blit(number, number_position)
            if 2 in s.holes:
                number_position = [333,373]
                screen.blit(number, number_position)
            if 3 in s.holes:
                number_position = [382,568]
                screen.blit(number, number_position)
            if 4 in s.holes:
                number_position = [238,423]
                screen.blit(number, number_position)
            if 5 in s.holes:
                number_position = [335,520]
                screen.blit(number, number_position)
            if 6 in s.holes:
                number_position = [238,520]
                screen.blit(number, number_position)
            if 7 in s.holes:
                number_position = [333,423]
                screen.blit(number, number_position)
            if 8 in s.holes:
                number_position = [286,568]
                screen.blit(number, number_position)
            if 9 in s.holes:
                number_position = [240,374]
                screen.blit(number, number_position)
            if 10 in s.holes:
                number_position = [430,565]
                screen.blit(number, number_position)
            if 11 in s.holes:
                number_position = [382,373]
                screen.blit(number, number_position)
            if 12 in s.holes:
                number_position = [238,568]
                screen.blit(number, number_position)
            if 13 in s.holes:
                number_position = [382,470]
                screen.blit(number, number_position)
            if 14 in s.holes:
                number_position = [334,569]
                screen.blit(number, number_position)
            if 15 in s.holes:
                number_position = [428,373]
                screen.blit(number, number_position)
            if 16 in s.holes:
                number_position = [334,470]
                screen.blit(number, number_position)
            if 17 in s.holes:
                number_position = [428,470]
                screen.blit(number, number_position)
            if 18 in s.holes:
                number_position = [428,423]
                screen.blit(number, number_position)
            if 19 in s.holes:
                number_position = [285,421]
                screen.blit(number, number_position)
            if 20 in s.holes:
                number_position = [430,520]
                screen.blit(number, number_position)
            if 21 in s.holes:
                number_position = [382,520]
                screen.blit(number, number_position)
            if 22 in s.holes:
                number_position = [382,421]
                screen.blit(number, number_position)
            if 23 in s.holes:
                number_position = [286,520]
                screen.blit(number, number_position)
            if 24 in s.holes:
                number_position = [286,470]
                screen.blit(number, number_position)
            if 25 in s.holes:
                number_position = [240,470]
                screen.blit(number, number_position)

    if s.game.red_odds.position == 1:
        o = [164,778]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 2:
        o = [220,778]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 3:
        o = [277,778]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 4:
        o = [331,778]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 5:
        o = [379,778]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 6:
        o = [426,778]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 7:
        o = [474,778]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 8:
        o = [522,778]
        screen.blit(odds, o)

    if s.game.yellow_odds.position == 1:
        o = [164,850]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 2:
        o = [220,850]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 3:
        o = [277,850]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 4:
        o = [331,850]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 5:
        o = [379,850]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 6:
        o = [426,850]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 7:
        o = [474,850]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 8:
        o = [522,850]
        screen.blit(odds, o)

    if s.game.green_odds.position == 1:
        o = [164,920]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 2:
        o = [220,920]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 3:
        o = [277,920]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 4:
        o = [331,920]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 5:
        o = [379,920]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 6:
        o = [426,920]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 7:
        o = [474,920]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 8:
        o = [522,920]
        screen.blit(odds, o)

    if 1 in s.game.skill_shot_selection:
        p = [78,386]
        screen.blit(skill_shot_number, p)
    if 2 in s.game.skill_shot_selection:
        p = [25,473]
        screen.blit(skill_shot_number, p)
    if 4 in s.game.skill_shot_selection:
        p = [131,474]
        screen.blit(skill_shot_number, p)
    if 6 in s.game.skill_shot_selection:
        p = [25,528]
        screen.blit(skill_shot_number, p)
    if 7 in s.game.skill_shot_selection:
        p = [130,529]
        screen.blit(skill_shot_number, p)
    if 8 in s.game.skill_shot_selection:
        p = [36,419]
        screen.blit(skill_shot_number, p)
    if 9 in s.game.skill_shot_selection:
        p = [106,577]
        screen.blit(skill_shot_number, p)
    if 12 in s.game.skill_shot_selection:
        p = [51,577]
        screen.blit(skill_shot_number, p)
    if 13 in s.game.skill_shot_selection:
        p = [121,420]
        screen.blit(skill_shot_number, p)

    p = [261,230]
    screen.blit(letter1, p)
    p = [317,228]
    screen.blit(letter2, p)
    p = [373,230]
    screen.blit(letter3, p)
    p = [431,230]
    screen.blit(letter4, p)
    p = [486,230]
    screen.blit(letter5, p)
    p = [536,230]
    screen.blit(letter6, p)

    if s.game.green_odds.position < 4:
        if s.game.super_ok.status == False:
            p = [261,230]
            screen.blit(red_letter1, p)
        else:
            p = [431,230]
            screen.blit(red_letter4, p)
    if s.game.green_odds.position == 4:
        if s.game.super_ok.status == False:
            p = [317,228]
            screen.blit(red_letter2, p)
        else:
            p = [486,230]
            screen.blit(red_letter5, p)
    if s.game.green_odds.position == 5:
        if s.game.super_ok.status == False:
            p = [373,230]
            screen.blit(red_letter3, p)
        else:
            p = [536,230]
            screen.blit(red_letter6, p)
    if s.game.green_odds.position == 6:
        p = [431,230]
        screen.blit(red_letter4, p)
    if s.game.green_odds.position == 7:
        p = [486,230]
        screen.blit(red_letter5, p)
    if s.game.green_odds.position == 8:
        p = [536,230]
        screen.blit(red_letter6, p)


    if s.game.tilt.status == False:
        p = [17,742]
        screen.blit(skill_shot, p)
        if s.game.skill_shot_scores.position == 1:
            p = [146,742]
            screen.blit(skill_shot_odds, p)
        if s.game.skill_shot_scores.position == 2:
            p = [174,742]
            screen.blit(skill_shot_odds, p)
        if s.game.skill_shot_scores.position == 3:
            p = [201,742]
            screen.blit(skill_shot_odds, p)
        if s.game.skill_shot_scores.position == 4:
            p = [229,742]
            screen.blit(skill_shot_odds, p)
        if s.game.skill_shot_scores.position == 5:
            p = [257,742]
            screen.blit(skill_shot_odds, p)
        if s.game.skill_shot_scores.position == 6:
            p = [286,742]
            screen.blit(skill_shot_odds, p)
        if s.game.skill_shot_scores.position == 7:
            p = [314,742]
            screen.blit(skill_shot_odds, p)
        if s.game.skill_shot_scores.position == 8:
            p = [342,742]
            screen.blit(skill_shot_odds, p)
        if s.game.skill_shot_scores.position == 9:
            p = [370,742]
            screen.blit(skill_shot_odds, p)
        if s.game.skill_shot_scores.position == 10:
            p = [398,742]
            screen.blit(skill_shot_odds, p)
        if s.game.skill_shot_scores.position == 11:
            p = [425,742]
            screen.blit(skill_shot_odds, p)
        if s.game.skill_shot_scores.position == 12:
            p = [453,742]
            screen.blit(skill_shot_odds, p)
        if s.game.skill_shot_scores.position == 13:
            p = [481,742]
            screen.blit(skill_shot_odds, p)
        if s.game.skill_shot_scores.position == 14:
            p = [508,742]
            screen.blit(skill_shot_odds, p)
        if s.game.skill_shot_scores.position == 15:
            p = [536,742]
            screen.blit(skill_shot_odds, p)
        if s.game.skill_shot_scores.position == 16:
            p = [564,742]
            screen.blit(skill_shot_odds, p)
        if s.game.skill_shot_scores.position == 17:
            p = [592,742]
            screen.blit(skill_shot_odds, p)
        if s.game.skill_shot_scores.position == 18:
            p = [620,742]
            screen.blit(skill_shot_odds, p)
        if s.game.skill_shot_scores.position == 19:
            p = [648,742]
            screen.blit(skill_shot_odds, p)
        if s.game.skill_shot_scores.position == 20:
            p = [676,742]
            screen.blit(skill_shot_odds, p)
        if len(s.game.skill_shot_selection) > 0:
            if s.game.ball_count.position <= 1:
                s.cancel_delayed(name="blink_ss")
                blink_ss([s,1,1])
            else:
                s.cancel_delayed(name="blink_ss")
        if s.game.skill_shot_replay_counter.position > 0:
            s.cancel_delayed(name="blink_ss")

    if s.game.tilt.status == True:
        tilt_position = [602,254]
        screen.blit(tilt, tilt_position)

    pygame.display.update()

def eb_animation(num):
    global screen

    if num == 3:
        eb_position = [153,1037]
        screen.blit(eb_number, eb_position)
        pygame.display.update()
    if num == 2:
        eb_position = [203,1037]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 1:
        eb_position = [269,1037]
        screen.blit(eb, eb_position)
        pygame.display.update()

def ss_animation(num):
    global screen

    if num == 4:
        p = [508,742]
        screen.blit(skill_shot_odds, p)
        pygame.display.update()
    else:
        p = [536,742]
        screen.blit(skill_shot_odds, p)
        pygame.display.update()


def feature_animation(num):
    global screen

    if num == 4:
        rss = [578,796]
        screen.blit(super_section, rss)
        pygame.display.update()
    else:
        yss = [578,894]
        screen.blit(super_section, yss)
        pygame.display.update()


def odds_animation(num):
    global screen
    if num == 8:
        odds_position = [187,778]
        screen.blit(odds, odds_position)
    if num == 7:
        odds_position = [247,850]
        screen.blit(odds, odds_position)
    if num == 6:
        odds_position = [309,920]
        screen.blit(odds, odds_position)
    if num == 5:
        odds_position = [370,778]
        screen.blit(odds, odds_position)
    if num == 4:
        odds_position = [423,850]
        screen.blit(odds, odds_position)
    if num == 3:
        odds_position = [472,920]
        screen.blit(odds, odds_position)
    if num == 2:
        odds_position = [522,778]
        screen.blit(odds, odds_position)
    if num == 1:
        odds_position = [568,850]
        screen.blit(odd, odds_position)
    pygame.display.update()

def blink(args):
    dirty_rects = []
    s = args[0]
    b = args[1]
    sn = args[2]

    if b == 0:
        if sn == 1:
            p = [541,685]
            dirty_rects.append(screen.blit(select_now, p))
        pygame.display.update(dirty_rects)
    else:
        dirty_rects.append(screen.blit(bg_gi, (541,685), pygame.Rect(541,685,142,35)))
        pygame.display.update(dirty_rects)
    b = not b

    args = [s,b,sn]

    s.delay(name="blink", delay=0.1, handler=blink, param=args)

def blink_ss(args):
    dirty_rects = []
    s = args[0]
    b = args[1]
    sn = args[2]

    if b == 0:
        if sn == 1:
            p = [70,465]
            dirty_rects.append(screen.blit(shoot_now, p))
        pygame.display.update(dirty_rects)
    else:
        dirty_rects.append(screen.blit(bg_gi, (70,465), pygame.Rect(70,465,58,84)))
        pygame.display.update(dirty_rects)
    b = not b

    args = [s,b,sn]

    s.delay(name="blink_ss", delay=0.1, handler=blink_ss, param=args)
