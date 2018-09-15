
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
        eb_position = [22,1033]
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

def screen_animation(args):
    dirty_rects = []
    s = args[0]
    num = args[1]
    direction = args[2]
    
    number_card_position = [235,363]

    dirty_rects.append(screen.blit(number_card, number_card_position))

    magic_screen.set_colorkey((255,0,252))

    if s.game.magic_screen.position == 0:
        p = [240,358]
    elif s.game.magic_screen.position == 1:
        p = [192,358]
    elif s.game.magic_screen.position == 2:
        p = [143,358]
    elif s.game.magic_screen.position == 3:
        p = [96,358]
    elif s.game.magic_screen.position == 4:
        p = [49,358]
    elif s.game.magic_screen.position == 5:
        p = [1,358]
    elif s.game.magic_screen.position == 6:
        p = [-45,358]
    elif s.game.magic_screen.position == 7:
        p = [-92,358]
    elif s.game.magic_screen.position == 8:
        p = [-139,358]
    elif s.game.magic_screen.position == 9:
        p = [-187,358]
    elif s.game.magic_screen.position == 10:
        p = [-234,358]

    if direction == "left":
       p[0] = p[0] + num
    else:
       p[0] = p[0] - num
 
    dirty_rects.append(screen.blit(magic_screen, p))
    
    backglass_position = [0, 0]
    if (s.game.anti_cheat.status == True):
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],710,270)))
    else:
        dirty_rects.append(screen.blit(bg_off, p, pygame.Rect(p[0],p[1],710,270)))
    
    if s.game.magic_screen_feature.position >= 7 or s.game.ok.status == True:
        if s.game.selection_feature.position < 7:
            bfp = [554,580]
            dirty_rects.append(screen.blit(bg_gi, bfp, pygame.Rect(bfp[0],bfp[1],118,55)))
            dirty_rects.append(screen.blit(time, bfp))
        elif s.game.selection_feature.position == 7:
            bfp = [554,410]
            dirty_rects.append(screen.blit(bg_gi, bfp, pygame.Rect(bfp[0],bfp[1],118,55)))
            screen.blit(time, bfp)
        elif s.game.selection_feature.position == 8:
            bfp = [554,351]
            dirty_rects.append(screen.blit(bg_gi, bfp, pygame.Rect(bfp[0],bfp[1],118,55)))
            screen.blit(time, bfp)
        
    if s.game.selection_feature.position == 1:
        i = [672,594]
        dirty_rects.append(screen.blit(bg_gi, i, pygame.Rect(i[0],i[1],39,29)))
        dirty_rects.append(screen.blit(ti, i))
    if s.game.selection_feature.position == 2 or s.game.selection_feature.position == 3:
        i = [672,534]
        dirty_rects.append(screen.blit(bg_gi, i, pygame.Rect(i[0],i[1],39,29)))
        dirty_rects.append(screen.blit(ti, i))
    if s.game.selection_feature.position == 4 or s.game.selection_feature.position == 5 or s.game.selection_feature.position == 6:
        i = [672,474]
        dirty_rects.append(screen.blit(bg_gi, i, pygame.Rect(i[0],i[1],39,29)))
        dirty_rects.append(screen.blit(ti, i))
    if s.game.selection_feature.position == 7:
        i = [672,417]
        dirty_rects.append(screen.blit(bg_gi, i, pygame.Rect(i[0],i[1],39,29)))
        dirty_rects.append(screen.blit(ti, i))
    if s.game.selection_feature.position == 8:
        i = [672,364]
        dirty_rects.append(screen.blit(bg_gi, i, pygame.Rect(i[0],i[1],39,29)))
        dirty_rects.append(screen.blit(ti, i))

    if s.game.red_star.status == True:
        rs_position = [550,466]
        dirty_rects.append(screen.blit(bg_gi, rs_position, pygame.Rect(rs_position[0],rs_position[1],118,55)))
        dirty_rects.append(screen.blit(time, rs_position))
    if s.game.yellow_star.status == True:
        rs_position = [550,522]
        dirty_rects.append(screen.blit(bg_gi, rs_position, pygame.Rect(rs_position[0],rs_position[1],118,55)))
        dirty_rects.append(screen.blit(time, rs_position))

    if s.game.red_super_section.status == True:
        rss = [578,796]
        dirty_rects.append(screen.blit(bg_gi, rss, pygame.Rect(rss[0],rss[1],114,86)))
        dirty_rects.append(screen.blit(super_section, rss))
    if s.game.yellow_super_section.status == True:
        yss = [578,894]
        dirty_rects.append(screen.blit(bg_gi, yss, pygame.Rect(yss[0],yss[1],114,86)))
        dirty_rects.append(screen.blit(super_section, yss))

   # dirty_rects.append(screen.blit(bg_gi, (70,465), pygame.Rect(70,465,58,84)))
    if 1 in s.game.skill_shot_selection:
        p = [78,386]
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],44,46)))
        dirty_rects.append(screen.blit(skill_shot_number, p))
    if 2 in s.game.skill_shot_selection:
        p = [25,473]
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],44,46)))
        dirty_rects.append(screen.blit(skill_shot_number, p))
    if 4 in s.game.skill_shot_selection:
        p = [131,474]
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],44,46)))
        dirty_rects.append(screen.blit(skill_shot_number, p))
    if 6 in s.game.skill_shot_selection:
        p = [25,528]
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],44,46)))
        dirty_rects.append(screen.blit(skill_shot_number, p))
    if 7 in s.game.skill_shot_selection:
        p = [130,529]
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],44,46)))
        dirty_rects.append(screen.blit(skill_shot_number, p))
    if 8 in s.game.skill_shot_selection:
        p = [36,419]
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],44,46)))
        dirty_rects.append(screen.blit(skill_shot_number, p))
    if 9 in s.game.skill_shot_selection:
        p = [106,577]
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],44,46)))
        dirty_rects.append(screen.blit(skill_shot_number, p))
    if 12 in s.game.skill_shot_selection:
        p = [51,577]
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],44,46)))
        dirty_rects.append(screen.blit(skill_shot_number, p))
    if 13 in s.game.skill_shot_selection:
        p = [121,420]
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],44,46)))
        dirty_rects.append(screen.blit(skill_shot_number, p))

    pygame.display.update(dirty_rects)


def clear_ss_number(s, num):
        global screen

        dirty_rects = []
    #if 1 not in s.game.skill_shot_selection:
        dirty_rects.append(screen.blit(bg_gi, (78,386), pygame.Rect(78,386,44,46)))
    #if 2 not in s.game.skill_shot_selection:
        dirty_rects.append(screen.blit(bg_gi, (25,473), pygame.Rect(25,473,44,46)))
    #if 4 in s.game.skill_shot_selection:
        dirty_rects.append(screen.blit(bg_gi, (131,474), pygame.Rect(131,474,44,46)))
    #if 6 in s.game.skill_shot_selection:
        dirty_rects.append(screen.blit(bg_gi, (25,528), pygame.Rect(25,528,44,46)))
    #if 7 in s.game.skill_shot_selection:
        dirty_rects.append(screen.blit(bg_gi, (130,529), pygame.Rect(130,529,44,46)))
    #if 8 in s.game.skill_shot_selection:
        dirty_rects.append(screen.blit(bg_gi, (36,419), pygame.Rect(36,419,44,46)))
    #if 9 in s.game.skill_shot_selection:
        dirty_rects.append(screen.blit(bg_gi, (106,577), pygame.Rect(106,577,44,46)))
    #if 12 in s.game.skill_shot_selection:
        dirty_rects.append(screen.blit(bg_gi, (51,577), pygame.Rect(51,577,44,46)))
    #if 13 in s.game.skill_shot_selection:
        dirty_rects.append(screen.blit(bg_gi, (121,420), pygame.Rect(121,420,44,46)))
        pygame.display.update(dirty_rects)

def draw_ss_number_animation(s, num):
    global screen
    dirty_rects = []
    if num in [0,3,16,25,9,41,50,12,21,34]:
        if 6 not in s.game.skill_shot_selection:
            p = [25,528]
            dirty_rects.append(screen.blit(skill_shot_number, p))
            pygame.display.update(dirty_rects)
            return
    if num in [6,19,43,31]:
        if 1 not in s.game.skill_shot_selection:
            p = [78,386]
            dirty_rects.append(screen.blit(skill_shot_number, p))
            pygame.display.update(dirty_rects)
            return
    if num in [43,6,18,30]:
        if 9 not in s.game.skill_shot_selection:
            p = [106,577]
            dirty_rects.append(screen.blit(skill_shot_number, p))
            pygame.display.update(dirty_rects)
            return
    if num in [5,14,20,23,30,39,45,48,18,27,33,36,2,8,11,43]:
        if 2 not in s.game.skill_shot_selection:
            p = [25,473]
            dirty_rects.append(screen.blit(skill_shot_number, p))
            pygame.display.update(dirty_rects)
            return
    if num in [29,38,47,17,26,35,4,14,22,1,10,42]:
        if 4 not in s.game.skill_shot_selection:
            p = [131,474]
            dirty_rects.append(screen.blit(skill_shot_number, p))
            pygame.display.update(dirty_rects)
            return
    if num in [33,42,21,30,8,17,5,47]:
        if 12 not in s.game.skill_shot_selection:
            p = [51,577]
            dirty_rects.append(screen.blit(skill_shot_number, p))
            pygame.display.update(dirty_rects)
            return
    if num in [0,25,13,16,4,41,29]:
        if 13 not in s.game.skill_shot_selection:
            p = [121,420]
            dirty_rects.append(screen.blit(skill_shot_number, p))
            pygame.display.update(dirty_rects)
            return
    if num in [7,20,32,44]:
        if 7 not in s.game.skill_shot_selection:
            p = [130,529]
            dirty_rects.append(screen.blit(skill_shot_number, p))
            pygame.display.update(dirty_rects)
            return
    if num in [7,18,32,43]:
        if 8 not in s.game.skill_shot_selection:
            p = [36,419]
            dirty_rects.append(screen.blit(skill_shot_number, p))
            pygame.display.update(dirty_rects)
            return
    pygame.display.update(dirty_rects)
    return

def clear_ss(s, num):
    global screen

    dirty_rects = []
    if s.game.skill_shot_scores.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (146,742), pygame.Rect(146,742,29,28)))
    if s.game.skill_shot_scores.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (174,742), pygame.Rect(174,742,29,28)))
    if s.game.skill_shot_scores.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (201,742), pygame.Rect(201,742,29,28)))
    if s.game.skill_shot_scores.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (229,742), pygame.Rect(229,742,29,28)))
    if s.game.skill_shot_scores.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (257,742), pygame.Rect(257,742,29,28)))
    if s.game.skill_shot_scores.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (286,742), pygame.Rect(286,742,29,28)))
    if s.game.skill_shot_scores.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (314,742), pygame.Rect(314,742,29,28)))
    if s.game.skill_shot_scores.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (342,742), pygame.Rect(342,742,29,28)))
    if s.game.skill_shot_scores.position != 9:
        dirty_rects.append(screen.blit(bg_gi, (370,742), pygame.Rect(370,742,29,28)))
    if s.game.skill_shot_scores.position != 10:
        dirty_rects.append(screen.blit(bg_gi, (398,742), pygame.Rect(398,742,29,28)))
    if s.game.skill_shot_scores.position != 11:
        dirty_rects.append(screen.blit(bg_gi, (425,742), pygame.Rect(425,742,29,28)))
    if s.game.skill_shot_scores.position != 12:
        dirty_rects.append(screen.blit(bg_gi, (453,742), pygame.Rect(453,742,29,28)))
    if s.game.skill_shot_scores.position != 13:
        dirty_rects.append(screen.blit(bg_gi, (481,742), pygame.Rect(481,742,29,28)))
    if s.game.skill_shot_scores.position != 14:
        dirty_rects.append(screen.blit(bg_gi, (508,742), pygame.Rect(508,742,29,28)))
    if s.game.skill_shot_scores.position != 15:
        dirty_rects.append(screen.blit(bg_gi, (536,742), pygame.Rect(536,742,29,28)))
    if s.game.skill_shot_scores.position != 16:
        dirty_rects.append(screen.blit(bg_gi, (564,742), pygame.Rect(564,742,29,28)))
    if s.game.skill_shot_scores.position != 17:
        dirty_rects.append(screen.blit(bg_gi, (592,742), pygame.Rect(592,742,29,28)))
    if s.game.skill_shot_scores.position != 18:
        dirty_rects.append(screen.blit(bg_gi, (620,742), pygame.Rect(620,742,29,28)))
    if s.game.skill_shot_scores.position != 19:
        dirty_rects.append(screen.blit(bg_gi, (648,742), pygame.Rect(648,742,29,28)))
    if s.game.skill_shot_scores.position != 20:
        dirty_rects.append(screen.blit(bg_gi, (676,742), pygame.Rect(676,742,29,28)))
    pygame.display.update(dirty_rects)

def draw_ss_animation(s, num):
    global screen
    dirty_rects = []

    if num in [1,2,26,27]:
        if s.game.skill_shot_scores.position != 2:
            p = [174,742]
            dirty_rects.append(screen.blit(skill_shot_odds, p))
    if num in [3,4,28,29]:
        if s.game.skill_shot_scores.position != 3:
            p = [201,742]
            dirty_rects.append(screen.blit(skill_shot_odds, p))
    if num in [5,6,30,31]:
        if s.game.skill_shot_scores.position != 5:
            p = [257,742]
            dirty_rects.append(screen.blit(skill_shot_odds, p))
    if num in [7,8,32,33]:
        if s.game.skill_shot_scores.position != 7:
            p = [314,742]
            dirty_rects.append(screen.blit(skill_shot_odds, p))
    if num in [9,10,34,35]:
        if s.game.skill_shot_scores.position != 9:
            p = [370,742]
            dirty_rects.append(screen.blit(skill_shot_odds, p))
    if num in [11,12,36,37]:
        if s.game.skill_shot_scores.position != 11:
            p = [425,742]
            dirty_rects.append(screen.blit(skill_shot_odds, p))
    if num in [13,14,38,39]:
        if s.game.skill_shot_scores.position != 13:
            p = [481,742]
            dirty_rects.append(screen.blit(skill_shot_odds, p))
    if num in [15,16,40,41]:
        if s.game.skill_shot_scores.position != 15:
            p = [536,742]
            dirty_rects.append(screen.blit(skill_shot_odds, p))
    if num in [16,17,42,43]:
        if s.game.skill_shot_scores.position != 17:
            p = [592,742]
            dirty_rects.append(screen.blit(skill_shot_odds, p))
    if num in [18,19,44,45]:
        if s.game.skill_shot_scores.position != 18:
            p = [620,742]
            dirty_rects.append(screen.blit(skill_shot_odds, p))
    if num in [21,22,46,47]:
        if s.game.skill_shot_scores.position != 19:
            p = [648,742]
            dirty_rects.append(screen.blit(skill_shot_odds, p))
    if num in [23,24,48,49]:
        if s.game.skill_shot_scores.position != 20:
            p = [676,742]
            dirty_rects.append(screen.blit(skill_shot_odds, p))
    pygame.display.update(dirty_rects)
    return

def ss_number_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]

    clear_ss_number(s, num)

    draw_ss_number_animation(s, num)

def ss_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]

    clear_ss(s, num)

    draw_ss_animation(s, num)

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

def blink_letter(args):
    dirty_rects = []
    s = args[0]
    b = args[1]
    sn = args[2]

    if b == 0:
        if sn == 4:
            p = [228,674]
            dirty_rects.append(screen.blit(ms_letter, p))
        elif sn == 5:
            p = [270,674]
            dirty_rects.append(screen.blit(ms_letter, p))
        elif sn == 6:
            p = [314,674]
            dirty_rects.append(screen.blit(ms_letter, p))
        elif sn == 7:
            p = [360,674]
            dirty_rects.append(screen.blit(ms_letter, p))
        elif sn == 8:
            p = [401,674]
            dirty_rects.append(screen.blit(ms_letter, p))
        elif sn == 9:
            p = [444,674]
            dirty_rects.append(screen.blit(ms_letter, p))
        elif sn == 10:
            p = [486,674]
            dirty_rects.append(screen.blit(ms_letter, p))
        pygame.display.update(dirty_rects)
    else:
        if sn == 4:
            dirty_rects.append(screen.blit(bg_gi, (228,674), pygame.Rect(228,674,41,51)))
        elif sn == 5:
            dirty_rects.append(screen.blit(bg_gi, (270,674), pygame.Rect(270,674,41,51)))
        elif sn == 6:
            dirty_rects.append(screen.blit(bg_gi, (314,674), pygame.Rect(314,674,41,51)))
        elif sn == 7:
            dirty_rects.append(screen.blit(bg_gi, (360,674), pygame.Rect(360,674,41,51)))
        elif sn == 8:
            dirty_rects.append(screen.blit(bg_gi, (401,674), pygame.Rect(401,674,41,51)))
        elif sn == 9:
            dirty_rects.append(screen.blit(bg_gi, (444,674), pygame.Rect(444,674,41,51)))
        elif sn == 10:
            dirty_rects.append(screen.blit(bg_gi, (486,674), pygame.Rect(486,674,41,51)))
        pygame.display.update(dirty_rects)
    b = not b

    args = [s,b,sn]

    s.delay(name="blink_letter", delay=0.1, handler=blink_letter, param=args)

def eb_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]

    if s.game.extra_ball.position < 1:
        dirty_rects.append(screen.blit(bg_gi, (153,1037), pygame.Rect(153,1037,48,32)))
    if s.game.extra_ball.position < 2:
        dirty_rects.append(screen.blit(bg_gi, (203,1037), pygame.Rect(203,1037,58,32)))
    if s.game.extra_ball.position < 3:
        dirty_rects.append(screen.blit(bg_gi, (269,1037), pygame.Rect(269,1037,58,32)))
    if s.game.extra_ball.position < 4:
        dirty_rects.append(screen.blit(bg_gi, (330,1037), pygame.Rect(330,1037,48,32)))
    if s.game.extra_ball.position < 5:
        dirty_rects.append(screen.blit(bg_gi, (379,1037), pygame.Rect(379,1037,58,32)))
    if s.game.extra_ball.position < 6:
        dirty_rects.append(screen.blit(bg_gi, (446,1037), pygame.Rect(446,1037,58,32)))
    if s.game.extra_ball.position < 7:
        dirty_rects.append(screen.blit(bg_gi, (506,1037), pygame.Rect(506,1037,48,32)))
    if s.game.extra_ball.position < 8:
        dirty_rects.append(screen.blit(bg_gi, (556,1037), pygame.Rect(556,1037,58,32)))
    if s.game.extra_ball.position < 9:
        dirty_rects.append(screen.blit(bg_gi, (622,1037), pygame.Rect(622,1037,58,32)))
    pygame.display.update(dirty_rects)

    if num in [0,25,14,49]:
        if s.game.extra_ball.position < 1:
            p = [153,1037]
            dirty_rects.append(screen.blit(eb_number, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [39,1,26,15]:
        if s.game.extra_ball.position < 2:
            p = [203,1037]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [3,4,17,28,29,40]:
        if s.game.extra_ball.position < 3:
            p = [269,1037]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [5,18,30,43]:
        if s.game.extra_ball.position < 4:
            p = [330,1037]
            dirty_rects.append(screen.blit(eb_number, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [7,8,19,32,33,44]:
        if s.game.extra_ball.position < 5:
            p = [379,1037]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [9,10,20,34,35,45]:
        if s.game.extra_ball.position < 6:
            p = [446,1037]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [11,21,36,46]:
        if s.game.extra_ball.position < 7:
            p = [506,1037]
            dirty_rects.append(screen.blit(eb_number, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [12,22,37,47]:
        if s.game.extra_ball.position < 8:
            p = [556,1037]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [2,6,13,16,23,27,31,38,41,48]:
        if s.game.extra_ball.position < 9:
            p = [622,1037]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return

def clear_odds(s, num):
    global screen

    dirty_rects = []

    if s.game.yellow_odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (220,850), pygame.Rect(220,850,39,66)))
    if s.game.yellow_odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (331,850), pygame.Rect(331,850,39,66)))
    if s.game.yellow_odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (426,850), pygame.Rect(426,850,39,66)))
    if s.game.yellow_odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (522,850), pygame.Rect(522,850,39,66)))

    if s.game.red_odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (277,778), pygame.Rect(277,778,39,66)))
    if s.game.red_odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (379,778), pygame.Rect(379,778,39,66)))
    if s.game.red_odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (474,778), pygame.Rect(474,778,39,66)))
    if s.game.red_odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (522,778), pygame.Rect(522,778,39,66)))

    if s.game.green_odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (277,920), pygame.Rect(277,920,39,66)))
    if s.game.green_odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (379,920), pygame.Rect(379,920,39,66)))
    if s.game.green_odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (474,920), pygame.Rect(474,920,39,66)))
    if s.game.green_odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (522,920), pygame.Rect(522,920,39,66)))

    pygame.display.update(dirty_rects)

def draw_odds_animation(s, num):
    global screen
    dirty_rects = []

    if num in [44,45,19,20]:
        if s.game.yellow_odds.position != 2:
            p = [220,850]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [32,33,7,8]:
        if s.game.yellow_odds.position != 4:
            p = [331,850]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [46,47,21,22]:
        if s.game.yellow_odds.position != 6:
            p = [426,850]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [36,37,11,12]:
        if s.game.yellow_odds.position != 8:
            p = [522,850]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return

    if num in [48,49,23,24]:
        if s.game.red_odds.position != 3:
            p = [277,778]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [38,39,13,14]:
        if s.game.red_odds.position != 5:
            p = [379,778]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [34,35,9,10]:
        if s.game.red_odds.position != 7:
            p = [474,778]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [26,27,1,2]:
        if s.game.red_odds.position != 8:
            p = [522,778]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return

    if num in [40,41,15,16]:
        if s.game.green_odds.position != 3:
            p = [277,920]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [42,43,17,18]:
        if s.game.green_odds.position != 5:
            p = [379,920]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [30,31,5,6]:
        if s.game.green_odds.position != 7:
            p = [474,920]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [3,4,28,29]:
        if s.game.green_odds.position != 8:
            p = [522,920]
            dirty_rects.append(screen.blit(odds, p))
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

    if s.game.selection_feature.position < 7 and s.game.ok.status == False and s.game.magic_screen_feature.position < 4:
        dirty_rects.append(screen.blit(bg_gi, (554,580), pygame.Rect(554,580,118,55)))
    if s.game.selection_feature.position != 4 and s.game.selection_feature.position != 5 and s.game.selection_feature.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (550,466), pygame.Rect(550,466,118,55)))
    if s.game.selection_feature.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (554,410), pygame.Rect(554,410,118,55)))
    if s.game.selection_feature.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (554,351), pygame.Rect(554,351,118,55)))
  
    if s.game.ok.status == False:
        dirty_rects.append(screen.blit(bg_gi, (144,674), pygame.Rect(144,674,58,53)))
    if s.game.extra_ok.status == False:
        dirty_rects.append(screen.blit(bg_gi, (86,674), pygame.Rect(86,674,57,47)))
    if s.game.yellow_super_section.status == False:
        dirty_rects.append(screen.blit(bg_gi, (578,894), pygame.Rect(578,894,114,86)))
    if s.game.red_super_section.status == False:
        dirty_rects.append(screen.blit(bg_gi, (578,796), pygame.Rect(578,796,114,86)))
    if s.game.three_blue.status == False:
        dirty_rects.append(screen.blit(bg_gi, (16,956), pygame.Rect(16,956,144,31)))
    if s.game.three_blue_six.status == False:
        dirty_rects.append(screen.blit(bg_gi, (16,922), pygame.Rect(16,922,144,31)))
    if s.game.two_blue.status == False:
        dirty_rects.append(screen.blit(bg_gi, (16,888), pygame.Rect(16,888,144,31)))

    if s.game.magic_screen_feature.position < 4:
        dirty_rects.append(screen.blit(bg_gi, (228,674), pygame.Rect(228,674,41,51)))
        dirty_rects.append(screen.blit(bg_gi, (270,674), pygame.Rect(270,674,41,51)))
        dirty_rects.append(screen.blit(bg_gi, (314,674), pygame.Rect(314,674,41,51)))
        dirty_rects.append(screen.blit(bg_gi, (360,674), pygame.Rect(360,674,41,51)))
    if s.game.magic_screen_feature.position < 8:
        dirty_rects.append(screen.blit(bg_gi, (401,674), pygame.Rect(401,674,41,51)))
    if s.game.magic_screen_feature.position < 9:
        dirty_rects.append(screen.blit(bg_gi, (444,674), pygame.Rect(444,674,41,51)))
    if s.game.magic_screen_feature.position < 10:
        dirty_rects.append(screen.blit(bg_gi, (486,674), pygame.Rect(486,674,41,51)))

    pygame.display.update(dirty_rects)


def draw_feature_animation(s, num):
    global screen
    dirty_rects = []

    if num in [17,18,42,43]:
        if s.game.selection_feature.position < 7 and s.game.ok.status == False and s.game.magic_screen_feature.position < 4:
            p = [554,580]
            dirty_rects.append(screen.blit(time, p))
        p = [554,351]
        dirty_rects.append(screen.blit(time, p))
        pygame.display.update(dirty_rects)
        return
    if num in [19,20,44,45]:
        p = [554,410]
        dirty_rects.append(screen.blit(time, p))
        pygame.display.update(dirty_rects)
        return
    if num in [23,24,48,49]:
        if s.game.yellow_super_section.status == False:
            if s.game.red_super_section.status == False:
                p = [578,796]
                dirty_rects.append(screen.blit(super_section, p))
                pygame.display.update(dirty_rects)
                return
    if num in [11,12,41,42]:
        if s.game.red_super_section.status == False:
            if s.game.yellow_super_section.status == False:
                p = [578,894]
                dirty_rects.append(screen.blit(super_section, p))
                pygame.display.update(dirty_rects)
                return
    if num in [15,16,40,41]:
        if s.game.ok.status == False:
            p = [144,674]
            dirty_rects.append(screen.blit(ok, p))
            pygame.display.update(dirty_rects)
            return
    if num in [1,2,26,27]:
        if s.game.extra_ok.status == False:
            p = [86,674]
            dirty_rects.append(screen.blit(extra_ok, p))
            pygame.display.update(dirty_rects)
            return
    if num in [3,4,28,29]:
        if s.game.three_blue.status == True:
            if s.game.three_blue_six.status == False:
                p = [16,922]
                dirty_rects.append(screen.blit(blue_section, p))
                pygame.display.update(dirty_rects)
                return
            else:
                p = [16,888]
                dirty_rects.append(screen.blit(blue_section, p))
                pygame.display.update(dirty_rects)
                return
    if num in [21,22,46,47]:
        if s.game.magic_screen_feature.position < 4:
            p = [228,674]
            dirty_rects.append(screen.blit(ms_letter, p))
            p = [270,674]
            dirty_rects.append(screen.blit(ms_letter, p))
            p = [314,674]
            dirty_rects.append(screen.blit(ms_letter, p))
            p = [360,674]
            dirty_rects.append(screen.blit(ms_letter, p))
            pygame.display.update(dirty_rects)
            return
    if num in [7,8,32,33]:
        if s.game.magic_screen_feature.position < 8:
            p = [401,674]
            dirty_rects.append(screen.blit(ms_letter, p))
            pygame.display.update(dirty_rects)
            return
    if num in [9,10,34,35]:
        if s.game.magic_screen_feature.position < 9:
            p = [444,674]
            dirty_rects.append(screen.blit(ms_letter, p))
            if s.game.three_blue.status == False and s.game.three_blue_six.status == False and s.game.two_blue.status == False:
                p = [16,956]
                dirty_rects.append(screen.blit(blue_section, p))
            pygame.display.update(dirty_rects)
            return
    if num in [13,14,38,39]:
        if s.game.magic_screen_feature.position < 10:
            p = [486,674]
            dirty_rects.append(screen.blit(ms_letter, p))
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

