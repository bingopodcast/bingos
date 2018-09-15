
import pygame
import random

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

meter = pygame.image.load('graphics/assets/silver_register_cover.png').convert()
sc_arrow = pygame.image.load('monaco/assets/sc_arrow.png').convert_alpha()
selection_arrow = pygame.image.load('monaco/assets/selection_arrow.png').convert_alpha()
sc = pygame.image.load('monaco/assets/super_card.png').convert_alpha()
eb = pygame.image.load('monaco/assets/eb.png').convert_alpha()
extra_ball = pygame.image.load('monaco/assets/extra_ball.png').convert_alpha()
extra_balls = pygame.image.load('monaco/assets/extra_balls.png').convert_alpha()
o1 = pygame.image.load('monaco/assets/odds1.png').convert_alpha()
o2 = pygame.image.load('monaco/assets/odds2.png').convert_alpha()
o3 = pygame.image.load('monaco/assets/odds3.png').convert_alpha()
o4 = pygame.image.load('monaco/assets/odds4.png').convert_alpha()
o5 = pygame.image.load('monaco/assets/odds5.png').convert_alpha()
o6 = pygame.image.load('monaco/assets/odds6.png').convert_alpha()
o7 = pygame.image.load('monaco/assets/odds7.png').convert_alpha()
o8 = pygame.image.load('monaco/assets/odds8.png').convert_alpha()
star = pygame.image.load('monaco/assets/rollovers.png').convert_alpha()
number = pygame.image.load('monaco/assets/number.png').convert_alpha()
sc_number = pygame.image.load('monaco/assets/sc_number.png').convert_alpha()
tilt = pygame.image.load('monaco/assets/tilt.png').convert_alpha()
select_now = pygame.image.load('monaco/assets/select_now.png').convert_alpha()
red_number = pygame.image.load('monaco/assets/red_number.png').convert_alpha()
red_sc_number = pygame.image.load('monaco/assets/red_sc_number.png').convert_alpha()
s_number = pygame.image.load('monaco/assets/spotted_number.png').convert_alpha()
s_arrow = pygame.image.load('monaco/assets/selection_arrow.png').convert_alpha()
before_fourth = pygame.image.load('monaco/assets/before_fourth.png').convert_alpha()
letter1 = pygame.image.load('monaco/assets/letter1.png').convert_alpha()
letter2 = pygame.image.load('monaco/assets/letter2.png').convert_alpha()
letter3 = pygame.image.load('monaco/assets/letter3.png').convert_alpha()
letter4 = pygame.image.load('monaco/assets/letter4.png').convert_alpha()
letter5 = pygame.image.load('monaco/assets/letter5.png').convert_alpha()
letter6 = pygame.image.load('monaco/assets/letter6.png').convert_alpha()
lite_a_name = pygame.image.load('monaco/assets/lite_a_name.png').convert_alpha()
three_four = pygame.image.load('monaco/assets/corners.png').convert_alpha()
bg_menu = pygame.image.load('monaco/assets/monaco_menu.png')
bg_gi = pygame.image.load('monaco/assets/monaco_gi.png')
bg_off = pygame.image.load('monaco/assets/monaco_off.png')

class scorereel():
    """ Score Reels are used to count replays """
    def __init__(self, pos, image):
        self.position = pos
        self.default_y = self.position[1]
        self.image = pygame.image.load(image).convert()

reel1 = scorereel([108,818], "graphics/assets/white_reel.png")
reel10 = scorereel([89,818], "graphics/assets/white_reel.png")
reel100 = scorereel([70,818], "graphics/assets/white_reel.png")

def display(s, replays=0, menu=False):
    
    meter.set_colorkey((255,0,252))
    meter_position = [60,818]

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
        p = [203,284]
        screen.blit(letter1, p)
        p = [272,285]
        screen.blit(letter2, p)
        p = [315,285]
        screen.blit(letter3, p)
        p = [366,284]
        screen.blit(letter4, p)
        p = [426,283]
        screen.blit(letter5, p)
        p = [473,284]
        screen.blit(letter6, p)
    else:
        if s.game.lite_a_name.status == True:
            p = [558,294]
            screen.blit(lite_a_name, p)
        if s.game.name.position >= 1:
            p = [203,284]
            screen.blit(letter1, p)
        if s.game.name.position >= 2:
            p = [272,285]
            screen.blit(letter2, p)
        if s.game.name.position >= 3:
            p = [315,285]
            screen.blit(letter3, p)
        if s.game.name.position >= 4:
            p = [366,284]
            screen.blit(letter4, p)
        if s.game.name.position >= 5:
            p = [426,283]
            screen.blit(letter5, p)
        if s.game.name.position >= 6:
            p = [473,284]
            screen.blit(letter6, p)


    if s.game.super_super_card.position == 1:
        p = [266,361]
        screen.blit(s_arrow, p)
    if s.game.super_super_card.position == 2:
        p = [305,361]
        screen.blit(s_arrow, p)
    if s.game.super_super_card.position == 3:
        p = [345,361]
        screen.blit(s_arrow, p)
    if s.game.super_super_card.position == 4:
        p = [384,361]
        screen.blit(s_arrow, p)
    if s.game.super_super_card.position == 5:
        p = [426,361]
        screen.blit(s_arrow, p)
    if s.game.super_super_card.position == 6:
        p = [463,361]
        screen.blit(three_four, p)

    if s.game.super_card.position == 1:
        p = [78,660]
        screen.blit(sc_arrow, p)
    if s.game.super_card.position == 2:
        p = [109,636]
        screen.blit(sc_arrow, p)
    if s.game.super_card.position == 3:
        p = [78,615]
        screen.blit(sc_arrow, p)
    if s.game.super_card.position == 4:
        p = [111,593]
        screen.blit(sc_arrow, p)
    if s.game.super_card.position == 5:
        p = [611,659]
        screen.blit(sc_arrow, p)
    if s.game.super_card.position == 6:
        p = [577,637]
        screen.blit(sc_arrow, p)
    if s.game.super_card.position == 7:
        p = [611,614]
        screen.blit(sc_arrow, p)
    if s.game.super_card.position == 8:
        p = [579,593]
        screen.blit(sc_arrow, p)

    if s.game.super_card.position >= 4:
        p = [54,396]
        screen.blit(sc, p)

    if s.game.super_card.position >= 8:
        p = [555,395]
        screen.blit(sc, p)

    if s.game.extra_ball.position == 1:
        eb_position = [97,954]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 2:
        eb_position = [132,954]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 3:
        eb_position = [167,954]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 4:
        eb_position = [202,954]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 5:
        eb_position = [236,954]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 6:
        eb_position = [273,954]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 7:
        eb_position = [309,954]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 8:
        eb_position = [345,954]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 9:
        eb_position = [379,954]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 10:
        eb_position = [415,954]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 11:
        eb_position = [453,954]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 12:
        eb_position = [489,954]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 13:
        eb_position = [523,954]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 14:
        eb_position = [559,954]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 15:
        eb_position = [592,954]
        screen.blit(eb, eb_position)

    if s.game.extra_ball.position >= 5 and s.game.extra_ball.position < 10:
        eb_pos = [96,980]
        screen.blit(extra_ball, eb_pos)
    if s.game.extra_ball.position >= 10 and s.game.extra_ball.position < 15:
        eb_pos = [271,980]
        screen.blit(extra_ball, eb_pos)
    if s.game.extra_ball.position == 15:
        eb_pos = [452,980]
        screen.blit(extra_ball, eb_pos)

    if s.game.odds.position > 0:
        if s.game.odds.position == 1:
            odds_position = [235,747]
            screen.blit(o1, odds_position)
        if s.game.odds.position == 2:
            odds_position = [471,747]
            screen.blit(o2, odds_position)
        if s.game.odds.position == 3:
            odds_position = [582,750]
            screen.blit(o3, odds_position)
        if s.game.odds.position == 4:
            odds_position = [667,747]
            screen.blit(o4, odds_position)
        if s.game.odds.position == 5:
            odds_position = [209,853]
            screen.blit(o5, odds_position)
        if s.game.odds.position == 6:
            odds_position = [301,759]
            screen.blit(o6, odds_position)
        if s.game.odds.position == 7:
            odds_position = [431,841]
            screen.blit(o7, odds_position)
        if s.game.odds.position == 8:
            odds_position = [665,836]
            screen.blit(o8, odds_position)

    if s.game.red_star.status == True:
        rs_position = [642,947]
        screen.blit(star, rs_position)

    if s.game.corners.status == True:
        corners_position = [25,363]
        screen.blit(three_four, corners_position)

    if s.game.tilt.status == False:
        if s.holes:
            if 1 in s.holes:
                number_position = [218,563]
                screen.blit(number, number_position)
                number_position = [545,460]
                screen.blit(sc_number, number_position)
            if 2 in s.holes:
                number_position = [217,508]
                screen.blit(number, number_position)
            if 3 in s.holes:
                number_position = [452,615]
                screen.blit(number, number_position)
                number_position = [92,420]
                screen.blit(sc_number, number_position)
            if 4 in s.holes:
                number_position = [278,404]
                screen.blit(number, number_position)
                number_position = [591,503]
                screen.blit(sc_number, number_position)
            if 5 in s.holes:
                number_position = [335,614]
                screen.blit(number, number_position)
            if 6 in s.holes:
                number_position = [452,404]
                screen.blit(number, number_position)
            if 7 in s.holes:
                number_position = [275,615]
                screen.blit(number, number_position)
                number_position = [591,419]
                screen.blit(sc_number, number_position)
            if 8 in s.holes:
                number_position = [453,456]
                screen.blit(number, number_position)
            if 9 in s.holes:
                number_position = [220,404]
                screen.blit(number, number_position)
                number_position = [46,461]
                screen.blit(sc_number, number_position)
            if 10 in s.holes:
                number_position = [218,457]
                screen.blit(number, number_position)
                number_position = [591,461]
                screen.blit(sc_number, number_position)
            if 11 in s.holes:
                number_position = [218,614]
                screen.blit(number, number_position)
                number_position = [136,462]
                screen.blit(sc_number, number_position)
                number_position = [636,419]
                screen.blit(sc_number, number_position)
            if 12 in s.holes:
                number_position = [395,509]
                screen.blit(number, number_position)
                number_position = [46,504]
                screen.blit(sc_number, number_position)
            if 13 in s.holes:
                number_position = [336,562]
                screen.blit(number, number_position)
                number_position = [637,461]
                screen.blit(sc_number, number_position)
            if 14 in s.holes:
                number_position = [336,457]
                screen.blit(number, number_position)
                number_position = [137,504]
                screen.blit(sc_number, number_position)
            if 15 in s.holes:
                number_position = [337,404]
                screen.blit(number, number_position)
                number_position = [545,419]
                screen.blit(sc_number, number_position)
            if 16 in s.holes:
                number_position = [336,510]
                screen.blit(number, number_position)
            if 17 in s.holes:
                number_position = [452,562]
                screen.blit(number, number_position)
                number_position = [545,502]
                screen.blit(sc_number, number_position)
            if 18 in s.holes:
                number_position = [278,510]
                screen.blit(number, number_position)
                number_position = [137,420]
                screen.blit(sc_number, number_position)
                number_position = [637,503]
                screen.blit(sc_number, number_position)
            if 19 in s.holes:
                number_position = [278,457]
                screen.blit(number, number_position)
            if 20 in s.holes:
                number_position = [395,456]
                screen.blit(number, number_position)
            if 21 in s.holes:
                number_position = [395,561]
                screen.blit(number, number_position)
            if 22 in s.holes:
                number_position = [277,563]
                screen.blit(number, number_position)
            if 23 in s.holes:
                number_position = [394,615]
                screen.blit(number, number_position)
                number_position = [47,420]
                screen.blit(sc_number, number_position)
            if 24 in s.holes:
                number_position = [395,404]
                screen.blit(number, number_position)
                number_position = [91,504]
                screen.blit(sc_number, number_position)
            if 25 in s.holes:
                number_position = [454,509]
                screen.blit(number, number_position)
                number_position = [92,461]
                screen.blit(sc_number, number_position)

    if s.game.tilt.status == True:
        tilt_position = [80,775]
        screen.blit(tilt, tilt_position)

    if s.game.selection_feature.position == 1:
        p = [162,710]
        screen.blit(s_arrow, p)
    if s.game.selection_feature.position == 2:
        p = [201,710]
        screen.blit(s_arrow, p)
    if s.game.selection_feature.position == 3:
        p = [242,711]
        screen.blit(s_arrow, p)
    if s.game.selection_feature.position >= 4:
        p = [276,707]
        screen.blit(s_number, p)
    if s.game.selection_feature.position >= 5:
        p = [318,709]
        screen.blit(s_number, p)
    if s.game.selection_feature.position >= 6:
        p = [359,708]
        screen.blit(s_number, p)
    if s.game.selection_feature.position >= 7:
        p = [401,707]
        screen.blit(s_number, p)
    if s.game.selection_feature.position >= 8:
        p = [442,707]
        screen.blit(s_number, p)
    if s.game.selection_feature.position >= 9:
        p = [483,708]
        screen.blit(s_number, p)
    if s.game.selection_feature.position >= 10:
        p = [525,707]
        screen.blit(s_number, p)

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

    if s.game.before_fourth.status == True and (s.game.selection_feature.position > 3 or s.game.selection_feature_relay.status == True):
        p = [16,695]
        screen.blit(before_fourth, p)
    if s.game.before_fifth.status == True and (s.game.selection_feature.position > 3 or s.game.selection_feature_relay.status == True):
        p = [567,695]
        screen.blit(before_fourth, p)

    if s.game.before_fourth.status == True:
        if s.game.ball_count.position < 4:
            if s.game.select_spots.status == True:
                if s.game.selection_feature.position >= 4:
                    if s.game.spotted.position == 0:
                        p = [280,676]
                        screen.blit(selection_arrow, p)
                        #19
                        number_position = [278,457]
                        screen.blit(red_number, number_position)
                if s.game.selection_feature.position >= 5:
                    if s.game.spotted.position == 1:
                        p = [323,675]
                        screen.blit(selection_arrow, p)
                        #20
                        number_position = [395,456]
                        screen.blit(red_number, number_position)
                if s.game.selection_feature.position >= 6:
                    if s.game.spotted.position == 2:
                        p = [364,676]
                        screen.blit(selection_arrow, p)
                        #21
                        number_position = [395,561]
                        screen.blit(red_number, number_position)
                if s.game.selection_feature.position >= 7:
                    if s.game.spotted.position == 3:
                        p = [405,676]
                        screen.blit(selection_arrow, p)
                        #22
                        number_position = [277,563]
                        screen.blit(red_number, number_position)
                if s.game.selection_feature.position >= 8:
                    if s.game.spotted.position == 4:
                        p = [446,675]
                        screen.blit(selection_arrow, p)
                        #16
                        number_position = [336,510]
                        screen.blit(red_number, number_position)
                if s.game.selection_feature.position >= 9:
                    if s.game.spotted.position == 5:
                        p = [487,676]
                        screen.blit(selection_arrow, p)
                        #25
                        number_position = [454,509]
                        screen.blit(red_number, number_position)
                        number_position = [92,461]
                        screen.blit(red_sc_number, number_position)
                if s.game.selection_feature.position >= 10:
                    if s.game.spotted.position == 6:
                        p = [528,676]
                        screen.blit(selection_arrow, p)
                        #10
                        number_position = [218,457]
                        screen.blit(red_number, number_position)
                        number_position = [591,461]
                        screen.blit(red_sc_number, number_position)

    if s.game.before_fifth.status == True:
        if s.game.ball_count.position < 5:
            if s.game.select_spots.status == True:
                if s.game.selection_feature.position >= 4:
                    if s.game.spotted.position == 0:
                        p = [280,676]
                        screen.blit(selection_arrow, p)
                        #19
                        number_position = [278,457]
                        screen.blit(red_number, number_position)
                if s.game.selection_feature.position >= 5:
                    if s.game.spotted.position == 1:
                        p = [323,675]
                        screen.blit(selection_arrow, p)
                        #20
                        number_position = [395,456]
                        screen.blit(red_number, number_position)
                if s.game.selection_feature.position >= 6:
                    if s.game.spotted.position == 2:
                        p = [364,676]
                        screen.blit(selection_arrow, p)
                        #21
                        number_position = [395,561]
                        screen.blit(red_number, number_position)
                if s.game.selection_feature.position >= 7:
                    if s.game.spotted.position == 3:
                        p = [405,676]
                        screen.blit(selection_arrow, p)
                        #22
                        number_position = [277,563]
                        screen.blit(red_number, number_position)
                if s.game.selection_feature.position >= 8:
                    if s.game.spotted.position == 4:
                        p = [446,675]
                        screen.blit(selection_arrow, p)
                        #16
                        number_position = [336,510]
                        screen.blit(red_number, number_position)
                if s.game.selection_feature.position >= 9:
                    if s.game.spotted.position == 5:
                        p = [487,676]
                        screen.blit(selection_arrow, p)
                        #25
                        number_position = [454,509]
                        screen.blit(red_number, number_position)
                        number_position = [92,461]
                        screen.blit(red_sc_number, number_position)
                if s.game.selection_feature.position >= 10:
                    if s.game.spotted.position == 6:
                        p = [528,676]
                        screen.blit(selection_arrow, p)
                        #10
                        number_position = [218,457]
                        screen.blit(red_number, number_position)
                        number_position = [591,461]
                        screen.blit(red_sc_number, number_position)

    if s.game.eb_play.status == True:
        p = [14,949]
        screen.blit(extra_balls, p)

    pygame.display.update()

def blink(args):
    dirty_rects = []
    s = args[0]
    b = args[1]
    sn = args[2]

    if b == 0:
        if sn == 1:
            p = [153,673]
            dirty_rects.append(screen.blit(select_now, p))
        pygame.display.update(dirty_rects)
    else:
        dirty_rects.append(screen.blit(bg_gi, (153,673), pygame.Rect(153,673,122,36)))
        pygame.display.update(dirty_rects)
    b = not b

    args = [s,b,sn]

    s.delay(name="blink", delay=0.1, handler=blink, param=args)

def eb_animation(args):
    global screen
    dirty_rects = []
    s = args[0]
    num = args[1]
    if s.game.extra_ball.position < 5:
        dirty_rects.append(screen.blit(bg_gi, (96,980), pygame.Rect(96,980,173,37)))
    if s.game.extra_ball.position < 10:
        dirty_rects.append(screen.blit(bg_gi, (271,980), pygame.Rect(271,980,173,37)))
    if s.game.extra_ball.position < 15:
        dirty_rects.append(screen.blit(bg_gi, (452,980), pygame.Rect(452,980,173,37)))
        dirty_rects.append(screen.blit(bg_gi, (592,954), pygame.Rect(592,954,33,27)))
    pygame.display.update(dirty_rects)
    if num in [0,1,6,7,12,13,18,19,26,27,32,33,38,39,44,45]:
        if s.game.extra_ball.position < 5:
            p = [96,980]
            dirty_rects.append(screen.blit(extra_ball, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [2,3,8,9,14,15,20,21,28,29,34,35,40,41,46,47]:
        if s.game.extra_ball.position < 10:
            p = [271,980]
            dirty_rects.append(screen.blit(extra_ball, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [4,5,10,11,16,17,22,23,24,30,31,36,37,42,43,48,49,50]:
        if s.game.extra_ball.position < 15:
            p = [452,980]
            dirty_rects.append(screen.blit(extra_ball, p))
            p = [592,954]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return

def clear_odds(s, num):
    global screen
    dirty_rects = []
    if s.game.odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (235,747), pygame.Rect(235,747,37,75)))
    if s.game.odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (471,747), pygame.Rect(471,747,38,80)))
    if s.game.odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (582,750), pygame.Rect(582,750,39,78)))
    if s.game.odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (667,747), pygame.Rect(667,747,39,78)))
    if s.game.odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (209,853), pygame.Rect(209,853,57,74)))
    if s.game.odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (301,759), pygame.Rect(301,759,80,108)))
    if s.game.odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (431,841), pygame.Rect(431,841,59,91)))
    if s.game.odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (665,836), pygame.Rect(665,836,43,79)))

    pygame.display.update(dirty_rects)

def draw_odds_animation(s, num):
    global screen
    dirty_rects = []

    if num in [0,1,40,14,24,25]:
        if s.game.odds.position != 1:
            p = [235,747]
            dirty_rects.append(screen.blit(o1, p))
            pygame.display.update(dirty_rects)
            return
    if num in [2,3,41,15,26,27]:
        if s.game.odds.position != 2:
            p = [471,747]
            dirty_rects.append(screen.blit(o2, p))
            pygame.display.update(dirty_rects)
            return
    if num in [4,5,42,16,28,29]:
        if s.game.odds.position != 3:
            p = [582,750]
            dirty_rects.append(screen.blit(o3, p))
            pygame.display.update(dirty_rects)
            return
    if num in [6,7,43,17,30,31]:
        if s.game.odds.position != 4:
            p = [667,747]
            dirty_rects.append(screen.blit(o4, p))
            pygame.display.update(dirty_rects)
            return
    if num in [8,9,44,18,32,33]:
        if s.game.odds.position != 5:
            p = [209,853]
            dirty_rects.append(screen.blit(o5, p))
            pygame.display.update(dirty_rects)
            return
    if num in [10,11,45,19,34,35]:
        if s.game.odds.position != 6:
            p = [301,759]
            dirty_rects.append(screen.blit(o6, p))
            pygame.display.update(dirty_rects)
            return
    if num in [12,13,46,47,20,21,36,37]:
        if s.game.odds.position != 7:
            p = [431,841]
            dirty_rects.append(screen.blit(o7, p))
            pygame.display.update(dirty_rects)
            return
    if num in [14,48,49,22,23,38]:
        if s.game.odds.position != 8:
            p = [665,836]
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

    if s.game.red_star.status == False:
        dirty_rects.append(screen.blit(bg_gi, (642,947), pygame.Rect(642,947,63,60)))
    if s.game.lite_a_name.status == False:
        dirty_rects.append(screen.blit(bg_gi, (558,294), pygame.Rect(558,294,120,42)))
    if s.game.corners.status == False:
        dirty_rects.append(screen.blit(bg_gi, (25,363), pygame.Rect(25,363,235,34)))
    if s.game.super_card.position < 4:
        dirty_rects.append(screen.blit(bg_gi, (54,396), pygame.Rect(54,396,114,24)))
    if s.game.super_card.position < 8:
        dirty_rects.append(screen.blit(bg_gi, (555,395), pygame.Rect(555,395,114,24)))
    if s.game.super_super_card.position < 6:
        dirty_rects.append(screen.blit(bg_gi, (463,361), pygame.Rect(463,361,235,34)))
    if s.game.selection_feature.position < 7:
        dirty_rects.append(screen.blit(bg_gi, (401,707), pygame.Rect(401,707,43,37)))
    if s.game.selection_feature.position < 8:
        dirty_rects.append(screen.blit(bg_gi, (442,707), pygame.Rect(442,707,43,47)))
    if s.game.selection_feature.position < 9:
        dirty_rects.append(screen.blit(bg_gi, (483,708), pygame.Rect(483,708,43,47)))
    if s.game.selection_feature.position < 10:
        dirty_rects.append(screen.blit(bg_gi, (525,707), pygame.Rect(525,707,43,47)))
    if s.game.selection_feature.position !=  1:
        dirty_rects.append(screen.blit(bg_gi, (162,710), pygame.Rect(162,710,32,29)))
    if s.game.selection_feature.position !=  2:
        dirty_rects.append(screen.blit(bg_gi, (201,710), pygame.Rect(201,710,32,29)))
    if s.game.selection_feature.position !=  3:
        dirty_rects.append(screen.blit(bg_gi, (242,711), pygame.Rect(242,711,32,29)))
    pygame.display.update(dirty_rects)


def draw_feature_animation(s, num):
    global screen
    dirty_rects = []

    if num in [11,12,36,37]:
        if s.game.red_star.status == False:
            p = [642,947]
            dirty_rects.append(screen.blit(star, p))
            s.game.coils.redROLamp.pulse(85)
            s.game.coils.yellowROLamp.pulse(85)
            pygame.display.update(dirty_rects)
            return
    if num in [9,10,34,35]:
        if s.game.lite_a_name.status == False:
            p = [558,294]
            dirty_rects.append(screen.blit(lite_a_name, p))
            pygame.display.update(dirty_rects)
            return
    if num in [7,8,32,33]:
        if s.game.super_super_card.position < 6:
            p = [463,361]
            dirty_rects.append(screen.blit(three_four, p))
            pygame.display.update(dirty_rects)
            return
    if num in [5,6,30,31]:
        if s.game.super_card.position < 4:
            p = [54,396]
            dirty_rects.append(screen.blit(sc, p))
            pygame.display.update(dirty_rects)
            return
    if num in [3,4,28,29]:
        if s.game.super_card.position < 8:
            p = [555,395]
            dirty_rects.append(screen.blit(sc, p))
            pygame.display.update(dirty_rects)
            return
    if num in [1,2,26,27]:
        if s.game.selection_feature.position < 10:
            p = [525,707]
            dirty_rects.append(screen.blit(s_number, p))
            pygame.display.update(dirty_rects)
            return
    if num in [0,49,24,25]:
        if s.game.selection_feature.position < 9:
            p = [525,707]
            dirty_rects.append(screen.blit(s_number, p))
            pygame.display.update(dirty_rects)
            return
    if num in [47,48,22,23]:
        if s.game.selection_feature.position < 8:
            p = [442,707]
            dirty_rects.append(screen.blit(s_number, p))
            pygame.display.update(dirty_rects)
            return
    if num in [20,21,45,46]:
        if s.game.selection_feature.position < 7:
            p = [401,707]
            dirty_rects.append(screen.blit(s_number, p))
            pygame.display.update(dirty_rects)
            return
    if num in [43,44,18,19]:
        if s.game.selection_feature.position != 3:
            p = [242,711]
            dirty_rects.append(screen.blit(s_arrow, p))
            pygame.display.update(dirty_rects)
            return
    if num in [41,42,16,17]:
        if s.game.selection_feature.position != 2:
            p = [201,710]
            dirty_rects.append(screen.blit(s_arrow, p))
            pygame.display.update(dirty_rects)
            return
    if num in [39,40,14,15]:
        if s.game.selection_feature.position != 1:
            p = [162,710]
            dirty_rects.append(screen.blit(s_arrow, p))
            pygame.display.update(dirty_rects)
            return
    if num in [16,17,41,42]:
        if s.game.corners.status == False:
            p = [25,363]
            dirty_rects.append(screen.blit(three_four, p))
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

