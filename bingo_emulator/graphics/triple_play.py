
import pygame
import random

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

meter = pygame.image.load('graphics/assets/silver_register_cover.png').convert()
eb = pygame.image.load('triple_play/assets/eb_arrow.png').convert_alpha()
extra_ball = pygame.image.load('triple_play/assets/extra_ball.png').convert_alpha()
extra_balls = pygame.image.load('triple_play/assets/extra_balls.png').convert_alpha()
o1 = pygame.image.load('triple_play/assets/odds1.png').convert_alpha()
o2 = pygame.image.load('triple_play/assets/odds2.png').convert_alpha()
o3 = pygame.image.load('triple_play/assets/odds3.png').convert_alpha()
o4 = pygame.image.load('triple_play/assets/odds4.png').convert_alpha()
o5 = pygame.image.load('triple_play/assets/odds5.png').convert_alpha()
o6 = pygame.image.load('triple_play/assets/odds6.png').convert_alpha()
o7 = pygame.image.load('triple_play/assets/odds7.png').convert_alpha()
o8 = pygame.image.load('triple_play/assets/odds8.png').convert_alpha()
star = pygame.image.load('triple_play/assets/rollover.png').convert_alpha()
number = pygame.image.load('triple_play/assets/number.png').convert_alpha()
tilt = pygame.image.load('triple_play/assets/tilt.png').convert_alpha()
scoring = pygame.image.load('triple_play/assets/scoring.png').convert_alpha()
select_now = pygame.image.load('triple_play/assets/before_fourth.png').convert_alpha()
red_number = pygame.image.load('triple_play/assets/red_number.png').convert_alpha()
scoring_arrow = pygame.image.load('triple_play/assets/scoring_arrow.png').convert_alpha()
s_arrow = pygame.image.load('triple_play/assets/spotted_arrow.png').convert_alpha()
before_fourth = pygame.image.load('triple_play/assets/before_fourth.png').convert_alpha()
s_number = pygame.image.load('triple_play/assets/spotted_number.png').convert_alpha()
four_five = pygame.image.load('triple_play/assets/4_as_5.png').convert_alpha()
letter1 = pygame.image.load('triple_play/assets/letter1.png').convert_alpha()
letter2 = pygame.image.load('triple_play/assets/letter2.png').convert_alpha()
letter3 = pygame.image.load('triple_play/assets/letter3.png').convert_alpha()
letter4 = pygame.image.load('triple_play/assets/letter4.png').convert_alpha()
letter5 = pygame.image.load('triple_play/assets/letter5.png').convert_alpha()
letter6 = pygame.image.load('triple_play/assets/letter6.png').convert_alpha()
letter7 = pygame.image.load('triple_play/assets/letter7.png').convert_alpha()
letter8 = pygame.image.load('triple_play/assets/letter8.png').convert_alpha()
letter9 = pygame.image.load('triple_play/assets/letter9.png').convert_alpha()
letter10 = pygame.image.load('triple_play/assets/letter10.png').convert_alpha()
lite_a_name = pygame.image.load('triple_play/assets/lite_a_name.png').convert_alpha()
card = pygame.image.load('triple_play/assets/card.png').convert_alpha()
bg_menu = pygame.image.load('triple_play/assets/triple_play_menu.png')
bg_gi = pygame.image.load('triple_play/assets/triple_play_gi.png')
bg_off = pygame.image.load('triple_play/assets/triple_play_off.png')

class scorereel():
    """ Score Reels are used to count replays """
    def __init__(self, pos, image):
        self.position = pos
        self.default_y = self.position[1]
        self.image = pygame.image.load(image).convert()

reel1 = scorereel([109,829], "graphics/assets/green_reel.png")
reel10 = scorereel([90,829], "graphics/assets/green_reel.png")
reel100 = scorereel([71,829], "graphics/assets/green_reel.png")

def display(s, replays=0, menu=False):
    
    meter.set_colorkey((255,0,252))
    meter_position = [62,829]

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
        p = [193,265]
        screen.blit(letter1, p)
        p = [227,259]
        screen.blit(letter2, p)
        p = [261,252]
        screen.blit(letter3, p)
        p = [284,247]
        screen.blit(letter4, p)
        p = [319,245]
        screen.blit(letter5, p)
        p = [347,242]
        screen.blit(letter6, p)
        p = [399,243]
        screen.blit(letter7, p)
        p = [428,252]
        screen.blit(letter8, p)
        p = [455,257]
        screen.blit(letter9, p)
        p = [491,267]
        screen.blit(letter10, p)
    else:
        if s.game.lite_a_name.status == True:
            p = [561,254]
            screen.blit(lite_a_name, p)

        if s.game.name.position >= 1:
            p = [193,265]
            screen.blit(letter1, p)
        if s.game.name.position >= 2:
            p = [227,259]
            screen.blit(letter2, p)
        if s.game.name.position >= 3:
            p = [261,252]
            screen.blit(letter3, p)
        if s.game.name.position >= 4:
            p = [284,247]
            screen.blit(letter4, p)
        if s.game.name.position >= 5:
            p = [319,245]
            screen.blit(letter5, p)
        if s.game.name.position >= 6:
            p = [347,242]
            screen.blit(letter6, p)
        if s.game.name.position >= 7:
            p = [399,243]
            screen.blit(letter7, p)
        if s.game.name.position >= 8:
            p = [428,252]
            screen.blit(letter8, p)
        if s.game.name.position >= 9:
            p = [455,257]
            screen.blit(letter9, p)
        if s.game.name.position >= 10:
            p = [491,267]
            screen.blit(letter10, p)

    if s.game.tilt.status == False:
        if s.game.selector.position >= 1:
            p = [65,312]
            screen.blit(card, p)
        if s.game.selector.position >= 2:
            p = [302,397]
            screen.blit(card, p)
        if s.game.selector.position == 3:
            p = [539,309]
            screen.blit(card, p)

    if s.game.extra_ball.position == 1:
        eb_position = [91,960]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 2:
        eb_position = [128,960]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 3:
        eb_position = [163,960]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 4:
        eb_position = [197,960]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 5:
        eb_position = [235,960]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 6:
        eb_position = [274,960]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 7:
        eb_position = [310,960]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 8:
        eb_position = [346,960]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 9:
        eb_position = [382,960]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 10:
        eb_position = [417,960]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 11:
        eb_position = [457,960]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 12:
        eb_position = [493,960]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 13:
        eb_position = [525,960]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 14:
        eb_position = [557,960]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 15:
        eb_position = [595,960]
        screen.blit(eb, eb_position)

    if s.game.extra_ball.position >= 5 and s.game.extra_ball.position < 10:
        eb_pos = [93,985]
        screen.blit(extra_ball, eb_pos)
    if s.game.extra_ball.position >= 10 and s.game.extra_ball.position < 15:
        eb_pos = [270,985]
        screen.blit(extra_ball, eb_pos)
    if s.game.extra_ball.position == 15:
        eb_pos = [445,985]
        screen.blit(extra_ball, eb_pos)

    if s.game.odds.position > 0:
        if s.game.odds.position == 1:
            odds_position = [150,727]
            screen.blit(o1, odds_position)
        if s.game.odds.position == 2:
            odds_position = [191,729]
            screen.blit(o2, odds_position)
        if s.game.odds.position == 3:
            odds_position = [431,727]
            screen.blit(o3, odds_position)
        if s.game.odds.position == 4:
            odds_position = [514,727]
            screen.blit(o4, odds_position)
        if s.game.odds.position == 5:
            odds_position = [148,804]
            screen.blit(o5, odds_position)
        if s.game.odds.position == 6:
            odds_position = [195,804]
            screen.blit(o6, odds_position)
        if s.game.odds.position == 7:
            odds_position = [457,804]
            screen.blit(o7, odds_position)
        if s.game.odds.position == 8:
            odds_position = [549,803]
            screen.blit(o8, odds_position)

    if s.game.red_star.status == True:
        rs_position = [641,953]
        screen.blit(star, rs_position)

    if s.game.corners1.status == True:
        corners_position = [45,550]
        screen.blit(four_five, corners_position)
    if s.game.corners2.status == True:
        corners_position = [279,633]
        screen.blit(four_five, corners_position)
    if s.game.corners3.status == True:
        corners_position = [515,546]
        screen.blit(four_five, corners_position)

    if s.game.tilt.status == False:
        if s.holes:
            if 1 in s.holes:
                p = [63,348]
                screen.blit(number, p)
                p = [255,554]
                screen.blit(number, p)
                p = [494,345]
                screen.blit(number, p)
            if 2 in s.holes:
                p = [105,508]
                screen.blit(number, p)
                p = [256,513]
                screen.blit(number, p)
                p = [493,425]
                screen.blit(number, p)
            if 3 in s.holes:
                p = [190,348]
                screen.blit(number, p)
                p = [425,592]
                screen.blit(number, p)
                p = [662,386]
                screen.blit(number, p)
            if 4 in s.holes:
                p = [189,508]
                screen.blit(number, p)
                p = [298,433]
                screen.blit(number, p)
                p = [662,505]
                screen.blit(number, p)
            if 5 in s.holes:
                p = [105,468]
                screen.blit(number, p)
                p = [340,593]
                screen.blit(number, p)
                p = [663,426]
                screen.blit(number, p)
            if 6 in s.holes:
                p = [23,429]
                screen.blit(number, p)
                p = [425,432]
                screen.blit(number, p)
                p = [619,506]
                screen.blit(number, p)
            if 7 in s.holes:
                p = [190,427]
                screen.blit(number, p)
                p = [297,593]
                screen.blit(number, p)
                p = [620,346]
                screen.blit(number, p)
            if 8 in s.holes:
                p = [21,390]
                screen.blit(number, p)
                p = [426,472]
                screen.blit(number, p)
                p = [535,506]
                screen.blit(number, p)
            if 9 in s.holes:
                p = [106,349]
                screen.blit(number, p)
                p = [256,434]
                screen.blit(number, p)
                p = [536,346]
                screen.blit(number, p)
            if 10 in s.holes:
                p = [106,390]
                screen.blit(number, p)
                p = [256,473]
                screen.blit(number, p)
                p = [577,506]
                screen.blit(number, p)
            if 11 in s.holes:
                p = [147,429]
                screen.blit(number, p)
                p = [256,593]
                screen.blit(number, p)
                p = [578,466]
                screen.blit(number, p)
            if 12 in s.holes:
                p = [22,509]
                screen.blit(number, p)
                p = [383,513]
                screen.blit(number, p)
                p = [536,426]
                screen.blit(number, p)
            if 13 in s.holes:
                p = [190,468]
                screen.blit(number, p)
                p = [340,552]
                screen.blit(number, p)
                p = [493,465]
                screen.blit(number, p)
            if 14 in s.holes:
                p = [22,350]
                screen.blit(number, p)
                p = [341,473]
                screen.blit(number, p)
                p = [620,425]
                screen.blit(number, p)
            if 15 in s.holes:
                p = [148,508]
                screen.blit(number, p)
                p = [341,433]
                screen.blit(number, p)
                p = [579,345]
                screen.blit(number, p)
            if 16 in s.holes:
                p = [107,428]
                screen.blit(number, p)
                p = [341,513]
                screen.blit(number, p)
                p = [579,426]
                screen.blit(number, p)
            if 17 in s.holes:
                p = [190,388]
                screen.blit(number, p)
                p = [425,552]
                screen.blit(number, p)
                p = [493,505]
                screen.blit(number, p)
            if 18 in s.holes:
                p = [64,429]
                screen.blit(number, p)
                p = [298,512]
                screen.blit(number, p)
                p = [663,346]
                screen.blit(number, p)
            if 19 in s.holes:
                p = [148,389]
                screen.blit(number, p)
                p = [299,473]
                screen.blit(number, p)
                p = [620,466]
                screen.blit(number, p)
            if 20 in s.holes:
                p = [148,469]
                screen.blit(number, p)
                p = [384,474]
                screen.blit(number, p)
                p = [536,467]
                screen.blit(number, p)
            if 21 in s.holes:
                p = [64,470]
                screen.blit(number, p)
                p = [383,553]
                screen.blit(number, p)
                p = [537,387]
                screen.blit(number, p)
            if 22 in s.holes:
                p = [65,390]
                screen.blit(number, p)
                p = [298,554]
                screen.blit(number, p)
                p = [621,387]
                screen.blit(number, p)
            if 23 in s.holes:
                p = [64,510]
                screen.blit(number, p)
                p = [382,594]
                screen.blit(number, p)
                p = [494,386]
                screen.blit(number, p)
            if 24 in s.holes:
                p = [22,469]
                screen.blit(number, p)
                p = [384,433]
                screen.blit(number, p)
                p = [662,466]
                screen.blit(number, p)
            if 25 in s.holes:
                p = [148,349]
                screen.blit(number, p)
                p = [426,513]
                screen.blit(number, p)
                p = [579,386]
                screen.blit(number, p)

    if s.game.each_card.position < 6 and s.game.odds.position > 0:
        p = [270,339]
        screen.blit(scoring, p)
    if s.game.each_card.position == 1:
        p = [276,311]
        screen.blit(scoring_arrow, p)
    if s.game.each_card.position == 2:
        p = [310,311]
        screen.blit(scoring_arrow, p)
    if s.game.each_card.position == 3:
        p = [345,311]
        screen.blit(scoring_arrow, p)
    if s.game.each_card.position == 4:
        p = [381,311]
        screen.blit(scoring_arrow, p)
    if s.game.each_card.position == 5:
        p = [414,311]
        screen.blit(scoring_arrow, p)
    if s.game.each_card.position == 6:
        p = [360,339]
        screen.blit(scoring, p)
        

    if s.game.tilt.status == True:
        tilt_position = [80,775]
        screen.blit(tilt, tilt_position)

    if s.game.selection_feature.position == 1:
        p = [157,666]
        screen.blit(s_arrow, p)
    if s.game.selection_feature.position == 2:
        p = [198,666]
        screen.blit(s_arrow, p)
    if s.game.selection_feature.position == 3:
        p = [237,666]
        screen.blit(s_arrow, p)
    if s.game.selection_feature.position >= 4:
        p = [274,663]
        screen.blit(s_number, p)
    if s.game.selection_feature.position >= 5:
        p = [316,663]
        screen.blit(s_number, p)
    if s.game.selection_feature.position >= 6:
        p = [357,663]
        screen.blit(s_number, p)
    if s.game.selection_feature.position >= 7:
        p = [398,663]
        screen.blit(s_number, p)
    if s.game.selection_feature.position >= 8:
        p = [440,663]
        screen.blit(s_number, p)
    if s.game.selection_feature.position >= 9:
        p = [482,663]
        screen.blit(s_number, p)
    if s.game.selection_feature.position >= 10:
        p = [522,663]
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

    if s.game.before_fourth.status == True and (s.game.selection_feature.position > 3):
        p = [565,598]
        screen.blit(before_fourth, p)
    if s.game.before_fifth.status == True and (s.game.selection_feature.position > 3):
        p = [565,653]
        screen.blit(before_fourth, p)

    if s.game.before_fourth.status == True:
        if s.game.ball_count.position < 4:
            if s.game.select_spots.status == True:
                if s.game.selection_feature.position >= 4:
                    if s.game.spotted.position == 0:
                        #19
                        p = [148,389]
                        screen.blit(red_number, p)
                        p = [299,473]
                        screen.blit(red_number, p)
                        p = [620,466]
                        screen.blit(red_number, p)
                if s.game.selection_feature.position >= 5:
                    if s.game.spotted.position == 1:
                        #20
                        p = [148,469]
                        screen.blit(red_number, p)
                        p = [384,474]
                        screen.blit(red_number, p)
                        p = [536,467]
                        screen.blit(red_number, p)
                if s.game.selection_feature.position >= 6:
                    if s.game.spotted.position == 2:
                        #21
                        p = [64,470]
                        screen.blit(red_number, p)
                        p = [383,553]
                        screen.blit(red_number, p)
                        p = [537,387]
                        screen.blit(red_number, p)
                if s.game.selection_feature.position >= 7:
                    if s.game.spotted.position == 3:
                        #22
                        p = [65,390]
                        screen.blit(red_number, p)
                        p = [298,554]
                        screen.blit(red_number, p)
                        p = [621,387]
                        screen.blit(red_number, p)
                if s.game.selection_feature.position >= 8:
                    if s.game.spotted.position == 4:
                        #25
                        p = [148,349]
                        screen.blit(red_number, p)
                        p = [426,513]
                        screen.blit(red_number, p)
                        p = [579,386]
                        screen.blit(red_number, p)
                if s.game.selection_feature.position >= 9:
                    if s.game.spotted.position == 5:
                        #10
                        p = [106,390]
                        screen.blit(red_number, p)
                        p = [256,473]
                        screen.blit(red_number, p)
                        p = [577,506]
                        screen.blit(red_number, p)
                if s.game.selection_feature.position >= 10:
                    if s.game.spotted.position == 6:
                        #16
                        p = [107,428]
                        screen.blit(red_number, p)
                        p = [341,513]
                        screen.blit(red_number, p)
                        p = [579,426]
                        screen.blit(red_number, p)


    if s.game.before_fifth.status == True:
        if s.game.ball_count.position < 5:
            if s.game.select_spots.status == True:
                if s.game.selection_feature.position >= 4:
                    if s.game.spotted.position == 0:
                        #19
                        p = [148,389]
                        screen.blit(red_number, p)
                        p = [299,473]
                        screen.blit(red_number, p)
                        p = [620,466]
                        screen.blit(red_number, p)
                if s.game.selection_feature.position >= 5:
                    if s.game.spotted.position == 1:
                        #20
                        p = [148,469]
                        screen.blit(red_number, p)
                        p = [384,474]
                        screen.blit(red_number, p)
                        p = [536,467]
                        screen.blit(red_number, p)
                if s.game.selection_feature.position >= 6:
                    if s.game.spotted.position == 2:
                        #21
                        p = [64,470]
                        screen.blit(red_number, p)
                        p = [383,553]
                        screen.blit(red_number, p)
                        p = [537,387]
                        screen.blit(red_number, p)
                if s.game.selection_feature.position >= 7:
                    if s.game.spotted.position == 3:
                        #22
                        p = [65,390]
                        screen.blit(red_number, p)
                        p = [298,554]
                        screen.blit(red_number, p)
                        p = [621,387]
                        screen.blit(red_number, p)
                if s.game.selection_feature.position >= 8:
                    if s.game.spotted.position == 4:
                        #25
                        p = [148,349]
                        screen.blit(red_number, p)
                        p = [426,513]
                        screen.blit(red_number, p)
                        p = [579,386]
                        screen.blit(red_number, p)
                if s.game.selection_feature.position >= 9:
                    if s.game.spotted.position == 5:
                        #10
                        p = [106,390]
                        screen.blit(red_number, p)
                        p = [256,473]
                        screen.blit(red_number, p)
                        p = [577,506]
                        screen.blit(red_number, p)
                if s.game.selection_feature.position >= 10:
                    if s.game.spotted.position == 6:
                        #16
                        p = [107,428]
                        screen.blit(red_number, p)
                        p = [341,513]
                        screen.blit(red_number, p)
                        p = [579,426]
                        screen.blit(red_number, p)


    if s.game.eb_play.status == True:
        p = [25,963]
        screen.blit(extra_balls, p)

    pygame.display.update()

def blink(args):
    dirty_rects = []
    s = args[0]
    b = args[1]
    sn = args[2]

    if b == 0:
        if sn == 1:
            p = [10,598]
            dirty_rects.append(screen.blit(select_now, p))
        pygame.display.update(dirty_rects)
    else:
        dirty_rects.append(screen.blit(bg_gi, (10,598), pygame.Rect(10,598,144,55)))
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
        dirty_rects.append(screen.blit(bg_gi, (93,985), pygame.Rect(93,985,171,36)))
    if s.game.extra_ball.position < 10:
        dirty_rects.append(screen.blit(bg_gi, (270,985), pygame.Rect(270,985,171,36)))
    if s.game.extra_ball.position < 15:
        dirty_rects.append(screen.blit(bg_gi, (445,985), pygame.Rect(445,985,171,36)))
        dirty_rects.append(screen.blit(bg_gi, (595,960), pygame.Rect(595,960,28,29)))
    pygame.display.update(dirty_rects)

    if num in [0,1,6,7,12,13,18,19,26,27,32,33,38,39,44,45]:
        if s.game.extra_ball.position < 5:
            p = [93,985]
            dirty_rects.append(screen.blit(extra_ball, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [2,3,8,9,14,15,20,21,28,29,34,35,40,41,46,47]:
        if s.game.extra_ball.position < 10:
            p = [270,985]
            dirty_rects.append(screen.blit(extra_ball, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [4,5,10,11,16,17,22,23,24,30,31,36,37,42,43,48,49,50]:
        if s.game.extra_ball.position < 15:
            p = [445,985]
            dirty_rects.append(screen.blit(extra_ball, p))
            p = [595,960]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return

def clear_odds(s, num):
    global screen
    dirty_rects = []
    if s.game.odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (150,727), pygame.Rect(150,727,35,72)))
    if s.game.odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (191,729), pygame.Rect(191,729,36,71)))
    if s.game.odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (431,727), pygame.Rect(431,727,47,76)))
    if s.game.odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (514,727), pygame.Rect(514,727,47,76)))
    if s.game.odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (148,804), pygame.Rect(148,804,47,76)))
    if s.game.odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (195,804), pygame.Rect(195,804,47,76)))
    if s.game.odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (457,804), pygame.Rect(457,804,47,76)))
    if s.game.odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (549,803), pygame.Rect(549,803,47,76)))

    pygame.display.update(dirty_rects)

def draw_odds_animation(s, num):
    global screen
    dirty_rects = []
    if num in [0,1,40,14,24,25]:
        if s.game.odds.position != 1:
            p = [150,727]
            dirty_rects.append(screen.blit(o1, p))
            pygame.display.update(dirty_rects)
            return
    if num in [2,3,41,15,26,27]:
        if s.game.odds.position != 2:
            p = [191,729]
            dirty_rects.append(screen.blit(o2, p))
            pygame.display.update(dirty_rects)
            return
    if num in [4,5,42,16,28,29]:
        if s.game.odds.position != 3:
            p = [431,727]
            dirty_rects.append(screen.blit(o3, p))
            pygame.display.update(dirty_rects)
            return
    if num in [6,7,43,17,30,31]:
        if s.game.odds.position != 4:
            p = [514,727]
            dirty_rects.append(screen.blit(o4, p))
            pygame.display.update(dirty_rects)
            return
    if num in [8,9,44,18,32,33]:
        if s.game.odds.position != 5:
            p = [148,804]
            dirty_rects.append(screen.blit(o5, p))
            pygame.display.update(dirty_rects)
            return
    if num in [10,11,45,19,34,35]:
        if s.game.odds.position != 6:
            p = [195,804]
            dirty_rects.append(screen.blit(o6, p))
            pygame.display.update(dirty_rects)
            return
    if num in [12,13,46,47,20,21,36,37]:
        if s.game.odds.position != 7:
            p = [457,804]
            dirty_rects.append(screen.blit(o7, p))
            pygame.display.update(dirty_rects)
            return
    if num in [14,48,49,22,23,38]:
        if s.game.odds.position != 8:
            p = [549,803]
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
    if s.game.lite_a_name.status == False:
        dirty_rects.append(screen.blit(bg_gi, (561,254), pygame.Rect(561,254,126,43)))
    if s.game.corners1.status == False:
        dirty_rects.append(screen.blit(bg_gi, (45,550), pygame.Rect(45,550,159,32)))
    if s.game.each_card.position < 6:
        dirty_rects.append(screen.blit(bg_gi, (360,339), pygame.Rect(360,339,93,44)))
    if s.game.red_star.status == False:
        dirty_rects.append(screen.blit(bg_gi, (641,953), pygame.Rect(641,953,61,60)))
    if s.game.corners3.status == False:
        dirty_rects.append(screen.blit(bg_gi, (515,546), pygame.Rect(515,546,159,32)))
    if s.game.selection_feature.position < 7:
        dirty_rects.append(screen.blit(bg_gi, (398,663), pygame.Rect(398,663,42,45)))
    if s.game.selection_feature.position < 8:
        dirty_rects.append(screen.blit(bg_gi, (440,663), pygame.Rect(440,663,42,45)))
    if s.game.selection_feature.position < 9:
        dirty_rects.append(screen.blit(bg_gi, (482,663), pygame.Rect(482,663,42,45)))
    if s.game.selection_feature.position < 10:
        dirty_rects.append(screen.blit(bg_gi, (522,663), pygame.Rect(522,663,42,45)))
    if s.game.selection_feature.position !=  1:
        dirty_rects.append(screen.blit(bg_gi, (157,666), pygame.Rect(157,666,35,42)))
    if s.game.selection_feature.position !=  2:
        dirty_rects.append(screen.blit(bg_gi, (198,666), pygame.Rect(198,666,35,42)))
    if s.game.selection_feature.position !=  3:
        dirty_rects.append(screen.blit(bg_gi, (237,666), pygame.Rect(237,666,35,42)))
    pygame.display.update(dirty_rects)


def draw_feature_animation(s, num):
    global screen
    dirty_rects = []

    if num in [11,12,36,37]:
        if s.game.red_star.status == False:
            p = [641,953]
            dirty_rects.append(screen.blit(star, p))
            s.game.coils.redROLamp.pulse(85)
            s.game.coils.yellowROLamp.pulse(85)
            pygame.display.update(dirty_rects)
            return
    if num in [9,10,34,35]:
        if s.game.each_card.position < 6:
            p = [360,339]
            dirty_rects.append(screen.blit(scoring, p))
            pygame.display.update(dirty_rects)
            return
    if num in [7,8,32,33]:
        if s.game.lite_a_name.status == False:
            p = [561,254]
            dirty_rects.append(screen.blit(lite_a_name, p))
            pygame.display.update(dirty_rects)
            return
    if num in [5,6,30,31]:
        if s.game.corners3.status == False:
            p = [515,546]
            dirty_rects.append(screen.blit(four_five, p))
            pygame.display.update(dirty_rects)
            return
    if num in [3,4,28,29]:
        if s.game.selection_feature.position < 8:
            p = [440,663]
            dirty_rects.append(screen.blit(s_number, p))
            pygame.display.update(dirty_rects)
            return
    if num in [1,2,26,27]:
        if s.game.selection_feature.position < 9:
            p = [482,663]
            dirty_rects.append(screen.blit(s_number, p))
            pygame.display.update(dirty_rects)
            return
    if num in [0,49,24,25]:
        if s.game.selection_feature.position < 10:
            p = [522,663]
            dirty_rects.append(screen.blit(s_number, p))
            pygame.display.update(dirty_rects)
            return
    if num in [47,48,22,23]:
        if s.game.selection_feature.position < 7:
            p = [398,663]
            dirty_rects.append(screen.blit(s_number, p))
            pygame.display.update(dirty_rects)
            return
    if num in [45,46,20,21]:
        if s.game.selection_feature.position != 3:
            p = [237,666]
            dirty_rects.append(screen.blit(s_arrow, p))
            pygame.display.update(dirty_rects)
            return
    if num in [43,44,18,19]:
        if s.game.selection_feature.position != 2:
            p = [198,666]
            dirty_rects.append(screen.blit(s_arrow, p))
            pygame.display.update(dirty_rects)
            return
    if num in [41,42,16,17]:
        if s.game.selection_feature.position != 1:
            p = [157,666]
            dirty_rects.append(screen.blit(s_arrow, p))
            pygame.display.update(dirty_rects)
            return
    if num in [39,40,14,15]:
        if s.game.corners1.status == False:
            p = [45,550]
            dirty_rects.append(screen.blit(four_five, p))
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

