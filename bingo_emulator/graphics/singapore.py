
import pygame
import random

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

meter = pygame.image.load('graphics/assets/silver_register_cover.png').convert()
sc_arrow = pygame.image.load('singapore/assets/sc_arrow.png').convert_alpha()
sc = pygame.image.load('singapore/assets/special_card.png').convert_alpha()
eb = pygame.image.load('singapore/assets/eb.png').convert_alpha()
extra_ball = pygame.image.load('singapore/assets/extra_ball.png').convert_alpha()
extra_balls = pygame.image.load('singapore/assets/extra_balls.png').convert_alpha()
o1 = pygame.image.load('singapore/assets/odds1.png').convert_alpha()
o2 = pygame.image.load('singapore/assets/odds2.png').convert_alpha()
o3 = pygame.image.load('singapore/assets/odds3.png').convert_alpha()
o4 = pygame.image.load('singapore/assets/odds4.png').convert_alpha()
o5 = pygame.image.load('singapore/assets/odds5.png').convert_alpha()
o6 = pygame.image.load('singapore/assets/odds6.png').convert_alpha()
o7 = pygame.image.load('singapore/assets/odds7.png').convert_alpha()
o8 = pygame.image.load('singapore/assets/odds8.png').convert_alpha()
star = pygame.image.load('singapore/assets/rollover.png').convert_alpha()
number = pygame.image.load('singapore/assets/number.png').convert_alpha()
sc_number = pygame.image.load('singapore/assets/sc_number.png').convert_alpha()
tilt = pygame.image.load('singapore/assets/tilt.png').convert_alpha()
select_now = pygame.image.load('singapore/assets/select_now.png').convert_alpha()
red_number = pygame.image.load('singapore/assets/red_number.png').convert_alpha()
red_sc_number = pygame.image.load('singapore/assets/red_sc_number.png').convert_alpha()
s_number = pygame.image.load('singapore/assets/spotted_numbers.png').convert_alpha()
s_arrow = pygame.image.load('singapore/assets/selection_arrow.png').convert_alpha()
before_fourth = pygame.image.load('singapore/assets/before_fourth.png').convert_alpha()
super_selection = pygame.image.load('singapore/assets/super_selection.png').convert_alpha()
select_feature = pygame.image.load('singapore/assets/select_feature.png').convert_alpha()
red_select_feature = pygame.image.load('singapore/assets/red_select_feature.png').convert_alpha()
four_five = pygame.image.load('singapore/assets/4_as_5.png').convert_alpha()
letter_s = pygame.image.load('singapore/assets/letter_s.png').convert_alpha()
letter_i = pygame.image.load('singapore/assets/letter_i.png').convert_alpha()
letter_n = pygame.image.load('singapore/assets/letter_n.png').convert_alpha()
letter_g = pygame.image.load('singapore/assets/letter_g.png').convert_alpha()
letter_a = pygame.image.load('singapore/assets/letter_a.png').convert_alpha()
letter_p = pygame.image.load('singapore/assets/letter_p.png').convert_alpha()
letter_o = pygame.image.load('singapore/assets/letter_o.png').convert_alpha()
letter_r = pygame.image.load('singapore/assets/letter_r.png').convert_alpha()
letter_e = pygame.image.load('singapore/assets/letter_e.png').convert_alpha()
lite_a_name = pygame.image.load('singapore/assets/lite_a_name.png').convert_alpha()
return_arrow = pygame.image.load('singapore/assets/return_arrow.png').convert_alpha()
ball_return = pygame.image.load('singapore/assets/return.png').convert_alpha()
bg_menu = pygame.image.load('singapore/assets/singapore_menu.png')
bg_gi = pygame.image.load('singapore/assets/singapore_gi.png')
bg_off = pygame.image.load('singapore/assets/singapore_off.png')

class scorereel():
    """ Score Reels are used to count replays """
    def __init__(self, pos, image):
        self.position = pos
        self.default_y = self.position[1]
        self.image = pygame.image.load(image).convert()

reel1 = scorereel([109,837], "graphics/assets/green_reel.png")
reel10 = scorereel([90,837], "graphics/assets/green_reel.png")
reel100 = scorereel([71,837], "graphics/assets/green_reel.png")

def display(s, replays=0, menu=False):
    
    meter.set_colorkey((255,0,252))
    meter_position = [62,835]

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
        p = [191,270]
        screen.blit(letter_s, p)
        p = [236,270]
        screen.blit(letter_i, p)
        p = [258,270]
        screen.blit(letter_n, p)
        p = [300,272]
        screen.blit(letter_g, p)
        p = [341,273]
        screen.blit(letter_a, p)
        p = [376,272]
        screen.blit(letter_p, p)
        p = [414,272]
        screen.blit(letter_o, p)
        p = [450,272]
        screen.blit(letter_r, p)
        p = [488,272]
        screen.blit(letter_e, p)
    else:
        if s.game.lite_a_name.status == True:
            p = [195,315]
            screen.blit(lite_a_name, p)

        if s.game.name.position >= 1:
            p = [191,270]
            screen.blit(letter_s, p)
        if s.game.name.position >= 2:
            p = [236,270]
            screen.blit(letter_i, p)
        if s.game.name.position >= 3:
            p = [258,270]
            screen.blit(letter_n, p)
        if s.game.name.position >= 4:
            p = [300,272]
            screen.blit(letter_g, p)
        if s.game.name.position >= 5:
            p = [341,273]
            screen.blit(letter_a, p)
        if s.game.name.position >= 6:
            p = [376,272]
            screen.blit(letter_p, p)
        if s.game.name.position >= 7:
            p = [414,272]
            screen.blit(letter_o, p)
        if s.game.name.position >= 8:
            p = [450,272]
            screen.blit(letter_r, p)
        if s.game.name.position >= 9:
            p = [488,272]
            screen.blit(letter_e, p)

    if s.game.super_card.position == 1:
        p = [70,252]
        screen.blit(sc_arrow, p)
    if s.game.super_card.position == 2:
        p = [118,254]
        screen.blit(sc_arrow, p)
    if s.game.super_card.position == 3:
        p = [566,252]
        screen.blit(sc_arrow, p)
    if s.game.super_card.position == 4:
        p = [610,252]
        screen.blit(sc_arrow, p)
    if s.game.super_card.position == 5:
        p = [68,438]
        screen.blit(sc_arrow, p)
    if s.game.super_card.position == 6:
        p = [118,438]
        screen.blit(sc_arrow, p)
    if s.game.super_card.position == 7:
        p = [568,434]
        screen.blit(sc_arrow, p)
    if s.game.super_card.position == 8:
        p = [614,434]
        screen.blit(sc_arrow, p)

    if s.game.super_card.position >= 2:
        p = [43,378]
        screen.blit(sc, p)
    if s.game.super_card.position >= 4:
        p = [542,376]
        screen.blit(sc, p)
    if s.game.super_card.position >= 6:
        p = [42,562]
        screen.blit(sc, p)
    if s.game.super_card.position >= 8:
        p = [540,561]
        screen.blit(sc, p)


    if s.game.extra_ball.position == 1:
        eb_position = [91,968]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 2:
        eb_position = [128,968]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 3:
        eb_position = [163,968]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 4:
        eb_position = [197,968]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 5:
        eb_position = [235,968]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 6:
        eb_position = [271,968]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 7:
        eb_position = [306,968]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 8:
        eb_position = [342,968]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 9:
        eb_position = [377,968]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 10:
        eb_position = [411,968]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 11:
        eb_position = [450,968]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 12:
        eb_position = [485,968]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 13:
        eb_position = [520,968]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 14:
        eb_position = [555,968]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position == 15:
        eb_position = [590,968]
        screen.blit(eb, eb_position)

    if s.game.extra_ball.position >= 5 and s.game.extra_ball.position < 10:
        eb_pos = [93,996]
        screen.blit(extra_ball, eb_pos)
    if s.game.extra_ball.position >= 10 and s.game.extra_ball.position < 15:
        eb_pos = [272,998]
        screen.blit(extra_ball, eb_pos)
    if s.game.extra_ball.position == 15:
        eb_pos = [449,997]
        screen.blit(extra_ball, eb_pos)

    if s.game.odds.position > 0:
        if s.game.odds.position == 1:
            odds_position = [179,730]
            screen.blit(o1, odds_position)
        if s.game.odds.position == 2:
            odds_position = [239,769]
            screen.blit(o2, odds_position)
        if s.game.odds.position == 3:
            odds_position = [313,750]
            screen.blit(o3, odds_position)
        if s.game.odds.position == 4:
            odds_position = [364,745]
            screen.blit(o4, odds_position)
        if s.game.odds.position == 5:
            odds_position = [440,753]
            screen.blit(o5, odds_position)
        if s.game.odds.position == 6:
            odds_position = [487,724]
            screen.blit(o6, odds_position)
        if s.game.odds.position == 7:
            odds_position = [535,730]
            screen.blit(o7, odds_position)
        if s.game.odds.position == 8:
            odds_position = [640,737]
            screen.blit(o8, odds_position)

    if s.game.red_star.status == True:
        rs_position = [645,953]
        screen.blit(star, rs_position)

    if s.game.corners.status == True:
        corners_position = [360,609]
        screen.blit(four_five, corners_position)

    if s.game.tilt.status == False:
        if s.holes:
            if 1 in s.holes:
                number_position = [221,505]
                screen.blit(number, number_position)
                number_position = [564,291]
                screen.blit(sc_number, number_position)
            if 2 in s.holes:
                number_position = [221,450]
                screen.blit(number, number_position)
                number_position = [70,294]
                screen.blit(sc_number, number_position)
            if 3 in s.holes:
                number_position = [448,553]
                screen.blit(number, number_position)
                number_position = [566,472]
                screen.blit(sc_number, number_position)
            if 4 in s.holes:
                number_position = [279,344]
                screen.blit(number, number_position)
                number_position = [566,336]
                screen.blit(sc_number, number_position)
            if 5 in s.holes:
                number_position = [334,554]
                screen.blit(number, number_position)
            if 6 in s.holes:
                number_position = [446,346]
                screen.blit(number, number_position)
                number_position = [118,338]
                screen.blit(sc_number, number_position)
            if 7 in s.holes:
                number_position = [278,556]
                screen.blit(number, number_position)
                number_position = [68,474]
                screen.blit(sc_number, number_position)
            if 8 in s.holes:
                number_position = [446,396]
                screen.blit(number, number_position)
            if 9 in s.holes:
                number_position = [222,344]
                screen.blit(number, number_position)
                number_position = [118,294]
                screen.blit(sc_number, number_position)
            if 10 in s.holes:
                number_position = [222,396]
                screen.blit(number, number_position)
                number_position = [69,523]
                screen.blit(sc_number, number_position)
            if 11 in s.holes:
                number_position = [221,554]
                screen.blit(number, number_position)
                number_position = [569,521]
                screen.blit(sc_number, number_position)
            if 12 in s.holes:
                number_position = [392,450]
                screen.blit(number, number_position)
                number_position = [613,290]
                screen.blit(sc_number, number_position)
            if 13 in s.holes:
                number_position = [334,501]
                screen.blit(number, number_position)
            if 14 in s.holes:
                number_position = [335,398]
                screen.blit(number, number_position)
                number_position = [115,475]
                screen.blit(sc_number, number_position)
            if 15 in s.holes:
                number_position = [334,346]
                screen.blit(number, number_position)
            if 16 in s.holes:
                number_position = [335,450]
                screen.blit(number, number_position)
            if 17 in s.holes:
                number_position = [446,500]
                screen.blit(number, number_position)
                number_position = [70,339]
                screen.blit(sc_number, number_position)
            if 18 in s.holes:
                number_position = [278,451]
                screen.blit(number, number_position)
                number_position = [614,474]
                screen.blit(sc_number, number_position)
            if 19 in s.holes:
                number_position = [280,399]
                screen.blit(number, number_position)
            if 20 in s.holes:
                number_position = [392,398]
                screen.blit(number, number_position)
            if 21 in s.holes:
                number_position = [392,502]
                screen.blit(number, number_position)
            if 22 in s.holes:
                number_position = [280,504]
                screen.blit(number, number_position)
            if 23 in s.holes:
                number_position = [391,556]
                screen.blit(number, number_position)
                number_position = [116,520]
                screen.blit(sc_number, number_position)
            if 24 in s.holes:
                number_position = [390,345]
                screen.blit(number, number_position)
                number_position = [612,334]
                screen.blit(sc_number, number_position)
            if 25 in s.holes:
                number_position = [445,450]
                screen.blit(number, number_position)
                number_position = [614,518]
                screen.blit(sc_number, number_position)

    if s.game.tilt.status == True:
        tilt_position = [80,775]
        screen.blit(tilt, tilt_position)

    if s.game.selection_feature.position == 2:
        p = [100,646]
        screen.blit(s_arrow, p)
    if s.game.selection_feature.position == 3:
        p = [140,645]
        screen.blit(s_arrow, p)
    if s.game.selection_feature.position == 4:
        p = [180,645]
        screen.blit(s_arrow, p)
    if s.game.selection_feature.position >= 5:
        p = [213,642]
        screen.blit(s_number, p)
    if s.game.selection_feature.position >= 6:
        p = [252,642]
        screen.blit(s_number, p)
    if s.game.selection_feature.position >= 7:
        p = [291,642]
        screen.blit(s_number, p)
    if s.game.selection_feature.position >= 8:
        p = [332,642]
        screen.blit(s_number, p)
    if s.game.selection_feature.position >= 9:
        p = [370,640]
        screen.blit(s_number, p)
    if s.game.selection_feature.position >= 10:
        p = [412,640]
        screen.blit(s_number, p)
    if s.game.selection_feature.position >= 11:
        p = [449,640]
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
        p = [7,616]
        screen.blit(before_fourth, p)
    if s.game.before_fifth.status == True and (s.game.selection_feature.position > 3 or s.game.selection_feature_relay.status == True):
        p = [619,618]
        screen.blit(before_fourth, p)

    if s.game.before_fourth.status == True:
        if s.game.ball_count.position < 4:
            if s.game.select_spots.status == True:
                if s.game.selection_feature.position >= 5:
                    if s.game.spotted.position == 0:
                        #19
                        number_position = [280,399]
                        screen.blit(red_number, number_position)
                if s.game.selection_feature.position >= 6:
                    if s.game.spotted.position == 1:
                        #20
                        number_position = [392,398]
                        screen.blit(red_number, number_position)
                if s.game.selection_feature.position >= 7:
                    if s.game.spotted.position == 2:
                        #21
                        number_position = [392,502]
                        screen.blit(red_number, number_position)
                if s.game.selection_feature.position >= 8:
                    if s.game.spotted.position == 3:
                        #22
                        number_position = [280,504]
                        screen.blit(red_number, number_position)
                if s.game.selection_feature.position >= 9:
                    if s.game.spotted.position == 4:
                        #16
                        number_position = [335,450]
                        screen.blit(red_number, number_position)
                if s.game.selection_feature.position >= 10:
                    if s.game.spotted.position == 5:
                        #25
                        number_position = [445,450]
                        screen.blit(red_number, number_position)
                        number_position = [614,518]
                        screen.blit(red_sc_number, number_position)
                if s.game.selection_feature.position >= 11:
                    if s.game.spotted.position == 6:
                        #10
                        number_position = [222,396]
                        screen.blit(red_number, number_position)
                        number_position = [69,523]
                        screen.blit(red_sc_number, number_position)
            if s.game.selection_feature_relay.status == True:
                if s.game.spotted.position == 7:
                    p = [98,683]
                    screen.blit(red_select_feature, p)
                if s.game.spotted.position == 8:
                    p = [202,683]
                    screen.blit(red_select_feature, p)
                if s.game.spotted.position == 9:
                    p = [414,682]
                    screen.blit(red_select_feature, p)
                if s.game.spotted.position == 10:
                    p = [518,680]
                    screen.blit(red_select_feature, p)

    if s.game.before_fifth.status == True:
        if s.game.ball_count.position < 5:
            if s.game.select_spots.status == True:
                if s.game.selection_feature.position >= 5:
                    if s.game.spotted.position == 0:
                        #19
                        number_position = [280,399]
                        screen.blit(red_number, number_position)
                if s.game.selection_feature.position >= 6:
                    if s.game.spotted.position == 1:
                        #20
                        number_position = [392,398]
                        screen.blit(red_number, number_position)
                if s.game.selection_feature.position >= 7:
                    if s.game.spotted.position == 2:
                        #21
                        number_position = [392,502]
                        screen.blit(red_number, number_position)
                if s.game.selection_feature.position >= 8:
                    if s.game.spotted.position == 3:
                        #22
                        number_position = [280,504]
                        screen.blit(red_number, number_position)
                if s.game.selection_feature.position >= 9:
                    if s.game.spotted.position == 4:
                        #16
                        number_position = [335,450]
                        screen.blit(red_number, number_position)
                if s.game.selection_feature.position >= 10:
                    if s.game.spotted.position == 5:
                        #25
                        number_position = [445,450]
                        screen.blit(red_number, number_position)
                        number_position = [614,518]
                        screen.blit(red_sc_number, number_position)
                if s.game.selection_feature.position >= 11:
                    if s.game.spotted.position == 6:
                        #10
                        number_position = [222,396]
                        screen.blit(red_number, number_position)
                        number_position = [69,523]
                        screen.blit(red_sc_number, number_position)
            if s.game.selection_feature_relay.status == True:
                if s.game.spotted.position == 7:
                    p = [98,683]
                    screen.blit(red_select_feature, p)
                if s.game.spotted.position == 8:
                    p = [202,683]
                    screen.blit(red_select_feature, p)
                if s.game.spotted.position == 9:
                    p = [414,682]
                    screen.blit(red_select_feature, p)
                if s.game.spotted.position == 10:
                    p = [518,680]
                    screen.blit(red_select_feature, p)

                                
    if s.game.selection_feature_relay.status == True:
        p = [98,683]
        screen.blit(select_feature, p)
        p = [202,683]
        screen.blit(select_feature, p)
        p = [308,676]
        screen.blit(super_selection, p)
        p = [414,682]
        screen.blit(select_feature, p)
        p = [518,680]
        screen.blit(select_feature, p)


    if s.game.selection_feature_relay.status == True:
        if s.game.before_fourth.status == True:
            max_ball = 4
        else:
            max_ball = 5
        if s.game.ball_count.position == max_ball:
            if s.game.spotted.position == 8:
                p = [168,610]
                screen.blit(four_five, p)

    if s.game.four_as_five.status == True:
        p = [168,610]
        screen.blit(four_five, p)

    if s.game.eb_play.status == True:
        p = [26,972]
        screen.blit(extra_balls, p)

    if s.game.ball_return.position == 1:
        p = [180,930]
        screen.blit(return_arrow, p)
    if s.game.ball_return.position == 2:
        p = [212,930]
        screen.blit(return_arrow, p)
    if s.game.ball_return.position == 3:
        p = [243,930]
        screen.blit(return_arrow, p)
    if s.game.ball_return.position == 4:
        p = [277,930]
        screen.blit(return_arrow, p)
    if s.game.ball_return.position == 5:
        p = [309,930]
        screen.blit(return_arrow, p)
    if s.game.ball_return.position == 6:
        p = [340,930]
        screen.blit(return_arrow, p)
    if s.game.ball_return.position == 7:
        p = [378,922]
        screen.blit(ball_return, p)

    pygame.display.update()

def blink(args):
    dirty_rects = []
    s = args[0]
    b = args[1]
    sn = args[2]

    if b == 0:
        if sn == 1:
            p = [488,641]
            dirty_rects.append(screen.blit(select_now, p))
        pygame.display.update(dirty_rects)
    else:
        dirty_rects.append(screen.blit(bg_gi, (488,641), pygame.Rect(488,641,134,40)))
        pygame.display.update(dirty_rects)
    b = not b

    args = [s,b,sn]

    s.delay(name="blink", delay=0.1, handler=blink, param=args)

def eb_animation(num):
    global screen
    if num == 9:
        eb_position = [91,968]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 8:
        eb_position = [128,968]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 7:
        eb_position = [163,968]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 6:
        eb_position = [197,968]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 5:
        eb_position = [235,968]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 4:
        eb_position = [271,968]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 3:
        eb_position = [306,968]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 2:
        eb_position = [342,968]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 1:
        eb_position = [377,968]
        screen.blit(eb, eb_position)
        pygame.display.update()


def feature_animation(num):
    global screen
    if num == 6:
        corners_position = [360,609]
        screen.blit(four_five, corners_position)
        pygame.display.update()

    if num == 5:
        rs_position = [645,953]
        screen.blit(star, rs_position)
        pygame.display.update()

    if num == 4:
        rs_position = [645,953]
        screen.blit(star, rs_position)
        pygame.display.update()

    if num == 3:
        p = [70,252]
        screen.blit(sc_arrow, p)
        pygame.display.update()

    if num == 2:
        p = [43,378]
        screen.blit(sc, p)
        pygame.display.update()

    if num == 1:
        p = [542,376]
        screen.blit(sc, p)
        pygame.display.update()


def odds_animation(num):
    global screen
    if num == 5:
        odds_position = [179,730]
        o = pygame.image.load('singapore/assets/odds1.png').convert_alpha()
        screen.blit(o, odds_position)
        pygame.display.update()
    if num == 4:
        odds_position = [239,769]
        o = pygame.image.load('singapore/assets/odds2.png').convert_alpha()
        screen.blit(o, odds_position)
        pygame.display.update()
    if num == 3:
        odds_position = [313,750]
        o = pygame.image.load('singapore/assets/odds3.png').convert_alpha()
        screen.blit(o, odds_position)
        pygame.display.update()
    if num == 2:
        odds_position = [364,745]
        o = pygame.image.load('singapore/assets/odds4.png').convert_alpha()
        screen.blit(o, odds_position)
        pygame.display.update()
    if num == 1:
        odds_position = [440,753]
        o = pygame.image.load('singapore/assets/odds5.png').convert_alpha()
        screen.blit(o, odds_position)
        pygame.display.update()
