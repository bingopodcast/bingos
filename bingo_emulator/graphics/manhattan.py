
import pygame
import random

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

meter = pygame.image.load('graphics/assets/silver_register_cover.png').convert()
eb = pygame.image.load('manhattan/assets/eb_arrow.png').convert_alpha()
extra_ball = pygame.image.load('manhattan/assets/extra_ball.png').convert_alpha()
extra_balls = pygame.image.load('manhattan/assets/extra_balls.png').convert_alpha()
o1 = pygame.image.load('manhattan/assets/odds1.png').convert_alpha()
o2 = pygame.image.load('manhattan/assets/odds2.png').convert_alpha()
o3 = pygame.image.load('manhattan/assets/odds3.png').convert_alpha()
o4 = pygame.image.load('manhattan/assets/odds4.png').convert_alpha()
o5 = pygame.image.load('manhattan/assets/odds5.png').convert_alpha()
o6 = pygame.image.load('manhattan/assets/odds6.png').convert_alpha()
o7 = pygame.image.load('manhattan/assets/odds7.png').convert_alpha()
o8 = pygame.image.load('manhattan/assets/odds8.png').convert_alpha()
star = pygame.image.load('manhattan/assets/rollover.png').convert_alpha()
number = pygame.image.load('manhattan/assets/number.png').convert_alpha()
tilt = pygame.image.load('manhattan/assets/tilt.png').convert_alpha()
scoring = pygame.image.load('manhattan/assets/scoring.png').convert_alpha()
select_now = pygame.image.load('manhattan/assets/before_fourth.png').convert_alpha()
red_number = pygame.image.load('manhattan/assets/red_number.png').convert_alpha()
scoring_arrow = pygame.image.load('manhattan/assets/scoring_arrow.png').convert_alpha()
s_arrow = pygame.image.load('manhattan/assets/spotted_arrow.png').convert_alpha()
before_fourth = pygame.image.load('manhattan/assets/before_fourth.png').convert_alpha()
s_number = pygame.image.load('manhattan/assets/spotted_number.png').convert_alpha()
corners1 = pygame.image.load('manhattan/assets/corners1.png').convert_alpha()
corners2 = pygame.image.load('manhattan/assets/corners2.png').convert_alpha()
letter1 = pygame.image.load('manhattan/assets/letter1.png').convert_alpha()
letter2 = pygame.image.load('manhattan/assets/letter2.png').convert_alpha()
letter3 = pygame.image.load('manhattan/assets/letter3.png').convert_alpha()
letter4 = pygame.image.load('manhattan/assets/letter4.png').convert_alpha()
letter5 = pygame.image.load('manhattan/assets/letter5.png').convert_alpha()
letter6 = pygame.image.load('manhattan/assets/letter6.png').convert_alpha()
letter7 = pygame.image.load('manhattan/assets/letter7.png').convert_alpha()
letter8 = pygame.image.load('manhattan/assets/letter8.png').convert_alpha()
letter9 = pygame.image.load('manhattan/assets/letter9.png').convert_alpha()
lite_a_name = pygame.image.load('manhattan/assets/lite_a_name.png').convert_alpha()
card = pygame.image.load('manhattan/assets/card.png').convert_alpha()
bg_menu = pygame.image.load('manhattan/assets/manhattan_menu.png')
bg_gi = pygame.image.load('manhattan/assets/manhattan_gi.png')
bg_off = pygame.image.load('manhattan/assets/manhattan_off.png')

class scorereel():
    """ Score Reels are used to count replays """
    def __init__(self, pos, image):
        self.position = pos
        self.default_y = self.position[1]
        self.image = pygame.image.load(image).convert()

reel1 = scorereel([109,840], "graphics/assets/white_reel.png")
reel10 = scorereel([90,840], "graphics/assets/white_reel.png")
reel100 = scorereel([71,840], "graphics/assets/white_reel.png")

def display(s, replays=0, menu=False):
    
    meter.set_colorkey((255,0,252))
    meter_position = [62,840]

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
        p = [192,265]
        screen.blit(letter1, p)
        p = [238,265]
        screen.blit(letter2, p)
        p = [275,265]
        screen.blit(letter3, p)
        p = [315,264]
        screen.blit(letter4, p)
        p = [352,265]
        screen.blit(letter5, p)
        p = [385,264]
        screen.blit(letter6, p)
        p = [423,264]
        screen.blit(letter7, p)
        p = [455,266]
        screen.blit(letter8, p)
        p = [496,266]
        screen.blit(letter9, p)
    else:
        if s.game.lite_a_name.status == True:
            p = [257,311]
            screen.blit(lite_a_name, p)

        if s.game.name.position >= 1:
            p = [192,265]
            screen.blit(letter1, p)
        if s.game.name.position >= 2:
            p = [238,265]
            screen.blit(letter2, p)
        if s.game.name.position >= 3:
            p = [275,265]
            screen.blit(letter3, p)
        if s.game.name.position >= 4:
            p = [315,264]
            screen.blit(letter4, p)
        if s.game.name.position >= 5:
            p = [352,265]
            screen.blit(letter5, p)
        if s.game.name.position >= 6:
            p = [385,264]
            screen.blit(letter6, p)
        if s.game.name.position >= 7:
            p = [423,264]
            screen.blit(letter7, p)
        if s.game.name.position >= 8:
            p = [455,266]
            screen.blit(letter8, p)
        if s.game.name.position >= 9:
            p = [496,266]
            screen.blit(letter9, p)

    if s.game.tilt.status == False:
        if s.game.selector.position >= 1:
            p = [85,244]
            screen.blit(card, p)
        if s.game.selector.position >= 2:
            p = [537,245]
            screen.blit(card, p)

    if s.game.extra_ball.position == 1:
        eb_position = [96,985]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 2:
        eb_position = [128,985]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 3:
        eb_position = [165,985]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 4:
        eb_position = [200,985]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 5:
        eb_position = [235,985]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 6:
        eb_position = [273,985]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 7:
        eb_position = [308,985]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 8:
        eb_position = [343,985]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 9:
        eb_position = [377,985]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 10:
        eb_position = [412,985]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 11:
        eb_position = [452,985]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 12:
        eb_position = [486,985]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 13:
        eb_position = [520,985]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 14:
        eb_position = [555,985]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 15:
        eb_position = [591,985]
        screen.blit(eb, eb_position)

    if s.game.extra_ball.position >= 5 and s.game.extra_ball.position < 10:
        eb_pos = [95,1017]
        screen.blit(extra_ball, eb_pos)
    if s.game.extra_ball.position >= 10 and s.game.extra_ball.position < 15:
        eb_pos = [275,1017]
        screen.blit(extra_ball, eb_pos)
    if s.game.extra_ball.position == 15:
        eb_pos = [453,1017]
        screen.blit(extra_ball, eb_pos)

    if s.game.odds.position > 0:
        if s.game.odds.position == 1:
            odds_position = [184,736]
            screen.blit(o1, odds_position)
        if s.game.odds.position == 2:
            odds_position = [218,722]
            screen.blit(o2, odds_position)
        if s.game.odds.position == 3:
            odds_position = [255,694]
            screen.blit(o3, odds_position)
        if s.game.odds.position == 4:
            odds_position = [474,717]
            screen.blit(o4, odds_position)
        if s.game.odds.position == 5:
            odds_position = [495,810]
            screen.blit(o5, odds_position)
        if s.game.odds.position == 6:
            odds_position = [556,707]
            screen.blit(o6, odds_position)
        if s.game.odds.position == 7:
            odds_position = [610,704]
            screen.blit(o7, odds_position)
        if s.game.odds.position == 8:
            odds_position = [631,815]
            screen.blit(o8, odds_position)

    if s.game.red_star.status == True:
        rs_position = [646,979]
        screen.blit(star, rs_position)

    if s.game.corners1.status == True:
        corners_position = [126,583]
        screen.blit(corners1, corners_position)
    if s.game.corners2.status == True:
        corners_position = [440,582]
        screen.blit(corners2, corners_position)

    if s.game.tilt.status == False:
        if s.holes:
            if 1 in s.holes:
                p = [123,304]
                screen.blit(number, p)
                p = [419,507]
                screen.blit(number, p)
            if 2 in s.holes:
                p = [120,530]
                screen.blit(number, p)
                p = [406,454]
                screen.blit(number, p)
            if 3 in s.holes:
                p = [281,347]
                screen.blit(number, p)
                p = [646,504]
                screen.blit(number, p)
            if 4 in s.holes:
                p = [226,556]
                screen.blit(number, p)
                p = [432,334]
                screen.blit(number, p)
            if 5 in s.holes:
                p = [134,476]
                screen.blit(number, p)
                p = [541,532]
                screen.blit(number, p)
            if 6 in s.holes:
                p = [42,396]
                screen.blit(number, p)
                p = [590,296]
                screen.blit(number, p)
            if 7 in s.holes:
                p = [254,452]
                screen.blit(number, p)
                p = [487,546]
                screen.blit(number, p)
            if 8 in s.holes:
                p = [56,344]
                screen.blit(number, p)
                p = [604,346]
                screen.blit(number, p)
            if 9 in s.holes:
                p = [176,318]
                screen.blit(number, p)
                p = [379,348]
                screen.blit(number, p)
            if 10 in s.holes:
                p = [163,371]
                screen.blit(number, p)
                p = [393,399]
                screen.blit(number, p)
            if 11 in s.holes:
                p = [202,438]
                screen.blit(number, p)
                p = [434,560]
                screen.blit(number, p)
            if 12 in s.holes:
                p = [14,500]
                screen.blit(number, p)
                p = [566,414]
                screen.blit(number, p)
            if 13 in s.holes:
                p = [241,504]
                screen.blit(number, p)
                p = [528,480]
                screen.blit(number, p)
            if 14 in s.holes:
                p = [70,290]
                screen.blit(number, p)
                p = [499,374]
                screen.blit(number, p)
            if 15 in s.holes:
                p = [174,542]
                screen.blit(number, p)
                p = [486,319]
                screen.blit(number, p)
            if 16 in s.holes:
                p = [149,423]
                screen.blit(number, p)
                p = [513,428]
                screen.blit(number, p)
            if 17 in s.holes:
                p = [268,398]
                screen.blit(number, p)
                p = [634,453]
                screen.blit(number, p)
            if 18 in s.holes:
                p = [96,410]
                screen.blit(number, p)
                p = [460,441]
                screen.blit(number, p)
            if 19 in s.holes:
                p = [216,386]
                screen.blit(number, p)
                p = [445,388]
                screen.blit(number, p)
            if 20 in s.holes:
                p = [188,489]
                screen.blit(number, p)
                p = [553,360]
                screen.blit(number, p)
            if 21 in s.holes:
                p = [82,460]
                screen.blit(number, p)
                p = [580,466]
                screen.blit(number, p)
            if 22 in s.holes:
                p = [110,356]
                screen.blit(number, p)
                p = [474,495]
                screen.blit(number, p)
            if 23 in s.holes:
                p = [68,513]
                screen.blit(number, p)
                p = [594,520]
                screen.blit(number, p)
            if 24 in s.holes:
                p = [30,447]
                screen.blit(number, p)
                p = [538,308]
                screen.blit(number, p)
            if 25 in s.holes:
                p = [229,333]
                screen.blit(number, p)
                p = [620,400]
                screen.blit(number, p)

    if s.game.each_card.position < 6 and s.game.odds.position > 0:
        p = [294,592]
        screen.blit(scoring, p)
    if s.game.each_card.position == 1:
        p = [342,380]
        screen.blit(scoring_arrow, p)
    if s.game.each_card.position == 2:
        p = [342,414]
        screen.blit(scoring_arrow, p)
    if s.game.each_card.position == 3:
        p = [342,447]
        screen.blit(scoring_arrow, p)
    if s.game.each_card.position == 4:
        p = [342,482]
        screen.blit(scoring_arrow, p)
    if s.game.each_card.position == 5:
        p = [342,514]
        screen.blit(scoring_arrow, p)
    if s.game.each_card.position == 6:
        p = [292,543]
        screen.blit(scoring, p)
        

    if s.game.tilt.status == True:
        tilt_position = [80,775]
        screen.blit(tilt, tilt_position)

    if s.game.selection_feature.position == 1:
        p = [126,648]
        screen.blit(s_arrow, p)
    if s.game.selection_feature.position == 2:
        p = [173,648]
        screen.blit(s_arrow, p)
    if s.game.selection_feature.position == 3:
        p = [222,648]
        screen.blit(s_arrow, p)
    if s.game.selection_feature.position >= 4:
        p = [266,646]
        screen.blit(s_number, p)
    if s.game.selection_feature.position >= 5:
        p = [314,646]
        screen.blit(s_number, p)
    if s.game.selection_feature.position >= 6:
        p = [360,646]
        screen.blit(s_number, p)
    if s.game.selection_feature.position >= 7:
        p = [408,646]
        screen.blit(s_number, p)
    if s.game.selection_feature.position >= 8:
        p = [456,648]
        screen.blit(s_number, p)
    if s.game.selection_feature.position >= 9:
        p = [504,648]
        screen.blit(s_number, p)
    if s.game.selection_feature.position >= 10:
        p = [550,648]
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
        p = [596,585]
        screen.blit(before_fourth, p)
    if s.game.before_fifth.status == True and (s.game.selection_feature.position > 3):
        p = [596,643]
        screen.blit(before_fourth, p)

    if s.game.before_fourth.status == True:
        if s.game.ball_count.position < 4:
            if s.game.select_spots.status == True:
                if s.game.selection_feature.position >= 4:
                    if s.game.spotted.position == 0:
                        #19
                        p = [216,386]
                        screen.blit(red_number, p)
                        p = [445,388]
                        screen.blit(red_number, p)
                if s.game.selection_feature.position >= 5:
                    if s.game.spotted.position == 1:
                        #20
                        p = [188,489]
                        screen.blit(red_number, p)
                        p = [553,360]
                        screen.blit(red_number, p)
                if s.game.selection_feature.position >= 6:
                    if s.game.spotted.position == 2:
                        #21
                        p = [82,460]
                        screen.blit(red_number, p)
                        p = [580,466]
                        screen.blit(red_number, p)
                if s.game.selection_feature.position >= 7:
                    if s.game.spotted.position == 3:
                        #22
                        p = [110,356]
                        screen.blit(red_number, p)
                        p = [474,495]
                        screen.blit(red_number, p)
                if s.game.selection_feature.position >= 8:
                    if s.game.spotted.position == 4:
                        #25
                        p = [229,333]
                        screen.blit(red_number, p)
                        p = [620,400]
                        screen.blit(red_number, p)
                if s.game.selection_feature.position >= 9:
                    if s.game.spotted.position == 5:
                        #10
                        p = [163,371]
                        screen.blit(red_number, p)
                        p = [393,399]
                        screen.blit(red_number, p)
                if s.game.selection_feature.position >= 10:
                    if s.game.spotted.position == 6:
                        #16
                        p = [149,423]
                        screen.blit(red_number, p)
                        p = [513,428]
                        screen.blit(red_number, p)


    if s.game.before_fifth.status == True:
        if s.game.ball_count.position < 5:
            if s.game.select_spots.status == True:
                if s.game.selection_feature.position >= 4:
                    if s.game.spotted.position == 0:
                        #19
                        p = [216,386]
                        screen.blit(red_number, p)
                        p = [445,388]
                        screen.blit(red_number, p)
                if s.game.selection_feature.position >= 5:
                    if s.game.spotted.position == 1:
                        #20
                        p = [188,489]
                        screen.blit(red_number, p)
                        p = [553,360]
                        screen.blit(red_number, p)
                if s.game.selection_feature.position >= 6:
                    if s.game.spotted.position == 2:
                        #21
                        p = [82,460]
                        screen.blit(red_number, p)
                        p = [580,466]
                        screen.blit(red_number, p)
                if s.game.selection_feature.position >= 7:
                    if s.game.spotted.position == 3:
                        #22
                        p = [110,356]
                        screen.blit(red_number, p)
                        p = [474,495]
                        screen.blit(red_number, p)
                if s.game.selection_feature.position >= 8:
                    if s.game.spotted.position == 4:
                        #25
                        p = [229,333]
                        screen.blit(red_number, p)
                        p = [620,400]
                        screen.blit(red_number, p)
                if s.game.selection_feature.position >= 9:
                    if s.game.spotted.position == 5:
                        #10
                        p = [163,371]
                        screen.blit(red_number, p)
                        p = [393,399]
                        screen.blit(red_number, p)
                if s.game.selection_feature.position >= 10:
                    if s.game.spotted.position == 6:
                        #16
                        p = [149,423]
                        screen.blit(red_number, p)
                        p = [513,428]
                        screen.blit(red_number, p)


    if s.game.eb_play.status == True:
        p = [29,989]
        screen.blit(extra_balls, p)

    pygame.display.update()

def blink(args):
    dirty_rects = []
    s = args[0]
    b = args[1]
    sn = args[2]

    if b == 0:
        if sn == 1:
            p = [10,582]
            dirty_rects.append(screen.blit(select_now, p))
        pygame.display.update(dirty_rects)
    else:
        dirty_rects.append(screen.blit(bg_gi, (10,582), pygame.Rect(10,582,109,57)))
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
        dirty_rects.append(screen.blit(bg_gi, (95,1017), pygame.Rect(95,1017,170,32)))
    if s.game.extra_ball.position < 10:
        dirty_rects.append(screen.blit(bg_gi, (275,1017), pygame.Rect(275,1017,170,32)))
    if s.game.extra_ball.position < 15:
        dirty_rects.append(screen.blit(bg_gi, (453,1017), pygame.Rect(453,1017,170,32)))
        dirty_rects.append(screen.blit(bg_gi, (591,985), pygame.Rect(591,985,35,30)))
    pygame.display.update(dirty_rects)

    if num in [0,1,6,7,12,13,18,19,26,27,32,33,38,39,44,45]:
        if s.game.extra_ball.position < 5:
            p = [95,1017]
            dirty_rects.append(screen.blit(extra_ball, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [2,3,8,9,14,15,20,21,28,29,34,35,40,41,46,47]:
        if s.game.extra_ball.position < 10:
            p = [275,1017]
            dirty_rects.append(screen.blit(extra_ball, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [4,5,10,11,16,17,22,23,24,30,31,36,37,42,43,48,49,50]:
        if s.game.extra_ball.position < 15:
            p = [453,1017]
            dirty_rects.append(screen.blit(extra_ball, p))
            p = [591,985]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return

def clear_odds(s, num):
    global screen

    dirty_rects = []
    if s.game.odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (184,736), pygame.Rect(184,736,29,102)))
    if s.game.odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (218,722), pygame.Rect(218,722,29,102)))
    if s.game.odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (255,694), pygame.Rect(255,694,31,102)))
    if s.game.odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (474,717), pygame.Rect(474,717,31,102)))
    if s.game.odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (495,810), pygame.Rect(495,810,53,100)))
    if s.game.odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (556,707), pygame.Rect(556,707,37,100)))
    if s.game.odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (610,704), pygame.Rect(610,704,37,100)))
    if s.game.odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (631,815), pygame.Rect(631,815,59,100)))

    pygame.display.update(dirty_rects)

def draw_odds_animation(s, num):
    global screen
    dirty_rects = []
    if num in [0,1,40,14,24,25]:
        if s.game.odds.position != 1:
            p = [184,736]
            dirty_rects.append(screen.blit(o1, p))
            pygame.display.update(dirty_rects)
            return
    if num in [2,3,41,15,26,27]:
        if s.game.odds.position != 2:
            p = [218,722]
            dirty_rects.append(screen.blit(o2, p))
            pygame.display.update(dirty_rects)
            return
    if num in [4,5,42,16,28,29]:
        if s.game.odds.position != 3:
            p = [255,694]
            dirty_rects.append(screen.blit(o3, p))
            pygame.display.update(dirty_rects)
            return
    if num in [6,7,43,17,30,31]:
        if s.game.odds.position != 4:
            p = [474,717]
            dirty_rects.append(screen.blit(o4, p))
            pygame.display.update(dirty_rects)
            return
    if num in [8,9,44,18,32,33]:
        if s.game.odds.position != 5:
            p = [495,810]
            dirty_rects.append(screen.blit(o5, p))
            pygame.display.update(dirty_rects)
            return
    if num in [10,11,45,19,34,35]:
        if s.game.odds.position != 6:
            p = [556,707]
            dirty_rects.append(screen.blit(o6, p))
            pygame.display.update(dirty_rects)
            return
    if num in [12,13,46,47,20,21,36,37]:
        if s.game.odds.position != 7:
            p = [610,704]
            dirty_rects.append(screen.blit(o7, p))
            pygame.display.update(dirty_rects)
            return
    if num in [14,48,49,22,23,38]:
        if s.game.odds.position != 8:
            p = [631,815]
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
        dirty_rects.append(screen.blit(bg_gi, (257,311), pygame.Rect(257,311,209,45)))
    if s.game.corners1.status == False:
        dirty_rects.append(screen.blit(bg_gi, (126,583), pygame.Rect(126,583,142,66)))
    if s.game.corners2.status == False:
        dirty_rects.append(screen.blit(bg_gi, (440,582), pygame.Rect(440,582,161,68)))
    if s.game.red_star.status == False:
        dirty_rects.append(screen.blit(bg_gi, (646,979), pygame.Rect(646,979,60,64)))
    if s.game.each_card.position < 6:
        dirty_rects.append(screen.blit(bg_gi, (292,543), pygame.Rect(292,543,132,53)))
    if s.game.selection_feature.position < 7:
        dirty_rects.append(screen.blit(bg_gi, (408,646), pygame.Rect(408,646,42,42)))
    if s.game.selection_feature.position < 8:
        dirty_rects.append(screen.blit(bg_gi, (456,648), pygame.Rect(456,648,42,42)))
    if s.game.selection_feature.position < 9:
        dirty_rects.append(screen.blit(bg_gi, (504,648), pygame.Rect(504,648,42,42)))
    if s.game.selection_feature.position < 10:
        dirty_rects.append(screen.blit(bg_gi, (550,648), pygame.Rect(550,648,42,42)))
    if s.game.selection_feature.position !=  1:
        dirty_rects.append(screen.blit(bg_gi, (126,648), pygame.Rect(126,648,38,46)))
    if s.game.selection_feature.position !=  2:
        dirty_rects.append(screen.blit(bg_gi, (173,648), pygame.Rect(173,648,38,46)))
    if s.game.selection_feature.position !=  3:
        dirty_rects.append(screen.blit(bg_gi, (222,648), pygame.Rect(222,648,38,46)))
    pygame.display.update(dirty_rects)


def draw_feature_animation(s, num):
    global screen
    dirty_rects = []
   
    if num in [11,12,36,37]:
        if s.game.red_star.status == False:
            p = [646,979]
            dirty_rects.append(screen.blit(star, p))
            s.game.coils.redROLamp.pulse(85)
            s.game.coils.yellowROLamp.pulse(85)
            pygame.display.update(dirty_rects)
            return
    if num in [9,10,34,35]:
        if s.game.each_card.position < 6:
            p = [292,543]
            dirty_rects.append(screen.blit(scoring, p))
            pygame.display.update(dirty_rects)
            return
    if num in [7,8,32,33]:
        if s.game.lite_a_name.status == False:
            p = [257,311]
            dirty_rects.append(screen.blit(lite_a_name, p))
            pygame.display.update(dirty_rects)
            return
    if num in [5,6,30,31]:
        if s.game.corners2.status == False:
            p = [440,582]
            dirty_rects.append(screen.blit(corners2, p))
            pygame.display.update(dirty_rects)
            return
    if num in [3,4,28,29]:
        if s.game.selection_feature.position < 8:
            p = [404,716]
            dirty_rects.append(screen.blit(s_number, p))
            pygame.display.update(dirty_rects)
            return
    if num in [1,2,26,27]:
        if s.game.selection_feature.position < 9:
            p = [504,648]
            dirty_rects.append(screen.blit(s_number, p))
            pygame.display.update(dirty_rects)
            return
    if num in [0,49,24,25]:
        if s.game.selection_feature.position < 10:
            p = [550,648]
            dirty_rects.append(screen.blit(s_number, p))
            pygame.display.update(dirty_rects)
            return
    if num in [47,48,22,23]:
        if s.game.selection_feature.position < 7:
            p = [408,646]
            dirty_rects.append(screen.blit(s_number, p))
            pygame.display.update(dirty_rects)
            return
    if num in [45,46,20,21]:
        if s.game.selection_feature.position != 3:
            p = [222,648]
            dirty_rects.append(screen.blit(s_arrow, p))
            pygame.display.update(dirty_rects)
            return
    if num in [43,44,18,19]:
        if s.game.selection_feature.position != 2:
            p = [173,648]
            dirty_rects.append(screen.blit(s_arrow, p))
            pygame.display.update(dirty_rects)
            return
    if num in [41,42,16,17]:
        if s.game.selection_feature.position != 1:
            p = [126,648]
            dirty_rects.append(screen.blit(s_arrow, p))
            pygame.display.update(dirty_rects)
            return
    if num in [39,40,14,15]:
        if s.game.corners1.status == False:
            p = [126,583]
            dirty_rects.append(screen.blit(corners1, p))
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

