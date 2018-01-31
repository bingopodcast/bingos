
import pygame, random

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

meter = pygame.image.load('graphics/assets/register_cover.png').convert()
card = pygame.image.load('ice_frolics/assets/card.png').convert_alpha()
corners = pygame.image.load('ice_frolics/assets/corners.png').convert_alpha()
odds1 = pygame.image.load('ice_frolics/assets/odds1.png').convert_alpha()
odds2 = pygame.image.load('ice_frolics/assets/odds2.png').convert_alpha()
odds3 = pygame.image.load('ice_frolics/assets/odds3.png').convert_alpha()
odds4 = pygame.image.load('ice_frolics/assets/odds4.png').convert_alpha()
odds5 = pygame.image.load('ice_frolics/assets/odds5.png').convert_alpha()
odds6 = pygame.image.load('ice_frolics/assets/odds6.png').convert_alpha()
odds7 = pygame.image.load('ice_frolics/assets/odds7.png').convert_alpha()
super_score = pygame.image.load('ice_frolics/assets/super_score.png').convert_alpha()
star = pygame.image.load('ice_frolics/assets/rollover.png').convert_alpha()
three_as_four = pygame.image.load('ice_frolics/assets/three_as_four.png').convert_alpha()
extra_balls = pygame.image.load('ice_frolics/assets/extra_balls.png').convert_alpha()
eb = pygame.image.load('ice_frolics/assets/eb_number.png').convert_alpha()
eb2 = pygame.image.load('ice_frolics/assets/eb2.png').convert_alpha()
eb3 = pygame.image.load('ice_frolics/assets/eb3.png').convert_alpha()
number = pygame.image.load('ice_frolics/assets/number.png').convert_alpha()
tilt = pygame.image.load('ice_frolics/assets/tilt.png').convert_alpha()
hold_arrow = pygame.image.load('ice_frolics/assets/hold_arrow.png').convert_alpha()
hold = pygame.image.load('ice_frolics/assets/hold.png').convert_alpha()
hold_time = pygame.image.load('ice_frolics/assets/hold_time.png').convert_alpha()
before_first = pygame.image.load('ice_frolics/assets/before_first.png').convert_alpha()
before_fourth = pygame.image.load('ice_frolics/assets/before_fourth.png').convert_alpha()
select_now = pygame.image.load('ice_frolics/assets/select_now.png').convert_alpha()
bg_menu = pygame.image.load('ice_frolics/assets/ice_frolics_menu.png')
bg_gi = pygame.image.load('ice_frolics/assets/ice_frolics_gi.png')
bg_off = pygame.image.load('ice_frolics/assets/ice_frolics_off.png')

class scorereel():
    """ Score Reels are used to count replays """
    def __init__(self, pos, image):
        self.position = pos
        self.default_y = self.position[1]
        self.image = pygame.image.load(image).convert()

reel1 = scorereel([619,341], "graphics/assets/green_reel.png")
reel10 = scorereel([601,341], "graphics/assets/green_reel.png")
reel100 = scorereel([582,341], "graphics/assets/green_reel.png")

def display(s, replays=0, menu=False):
    
    meter.set_colorkey((255,0,252))
    meter_position = [572,341]

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

    if s.game.selector.position >= 1:
        card1_position = [74,442]
        screen.blit(card, card1_position)
    if s.game.selector.position >= 2:
        card2_position = [301,340]
        screen.blit(card, card2_position)
    if s.game.selector.position >= 3:
        card3_position = [533,442]
        screen.blit(card, card3_position)

    if s.game.odds.position == 1:
        p = [30,799]
        screen.blit(odds1, p)
    if s.game.odds.position == 2:
        p = [124,799]
        screen.blit(odds2, p)
    if s.game.odds.position == 3:
        p = [218,801]
        screen.blit(odds3, p)
    if s.game.odds.position == 4:
        p = [312,801]
        screen.blit(odds4, p)
    if s.game.odds.position == 5:
        p = [406,802]
        screen.blit(odds5, p)
    if s.game.odds.position == 6:
        p = [500,802]
        screen.blit(odds6, p)
    if s.game.odds.position == 7:
        p = [594,802]
        screen.blit(odds7, p)

    if s.game.super_score.status == True:
        if s.game.super_score_selector.position == 0:
            p = [55,471]
            screen.blit(super_score, p)
        elif s.game.super_score_selector.position == 1:
            p = [282,370]
            screen.blit(super_score, p)
        else:
            p = [512,471]
            screen.blit(super_score, p)
        if s.game.before_first.status == True:
            if s.game.ball_count.position < 1:
                s.cancel_delayed(name="blink")
                blink([s,1,1])
            else:
                s.cancel_delayed(name="blink")
            p = [252,619]
            screen.blit(before_first, p)
        else:
            if s.game.ball_count.position == 3:
                s.cancel_delayed(name="blink")
                blink([s,1,1])
            else:
                s.cancel_delayed(name="blink")
            p = [336,616]
            screen.blit(before_fourth, p)


    if s.game.red_star.status == True:
        p = [625,950]
        screen.blit(star, p)

    if s.game.yellow_star.status == True:
        p = [23,950]
        screen.blit(star, p)

    if s.game.eb_play.status == True:
        p = [300,950]
        screen.blit(extra_balls, p)

    if s.game.extra_ball.position >= 1:
        p = [104,982]
        screen.blit(eb, p)
    if s.game.extra_ball.position >= 2:
        p = [152,982]
        screen.blit(eb2, p)
    if s.game.extra_ball.position >= 3:
        p = [227,983]
        screen.blit(eb3, p)
    if s.game.extra_ball.position >= 4:
        p = [276,982]
        screen.blit(eb, p)
    if s.game.extra_ball.position >= 5:
        p = [324,982]
        screen.blit(eb2, p)
    if s.game.extra_ball.position >= 6:
        p = [399,983]
        screen.blit(eb3, p)
    if s.game.extra_ball.position >= 7:
        p = [452,982]
        screen.blit(eb, p)
    if s.game.extra_ball.position >= 8:
        p = [500,982]
        screen.blit(eb2, p)
    if s.game.extra_ball.position >= 9:
        p = [575,983]
        screen.blit(eb3, p)


    if s.game.tilt.status == False:
        if s.holes:
            if 1 in s.holes:
                number_position = [73,507]
                screen.blit(number, number_position)
                number_position = [429,487]
                screen.blit(number, number_position)
                number_position = [616,665]
                screen.blit(number, number_position)
            if 2 in s.holes:
                number_position = [116,664]
                screen.blit(number, number_position)
                number_position = [260,487]
                screen.blit(number, number_position)
                number_position = [616,587]
                screen.blit(number, number_position)
            if 3 in s.holes:
                number_position = [199,507]
                screen.blit(number, number_position)
                number_position = [430,564]
                screen.blit(number, number_position)
                number_position = [491,664]
                screen.blit(number, number_position)

            if 4 in s.holes:
                number_position = [158,664]
                screen.blit(number, number_position)
                number_position = [302,409]
                screen.blit(number, number_position)
                number_position = [616,509]
                screen.blit(number, number_position)
            if 5 in s.holes:
                number_position = [116,547]
                screen.blit(number, number_position)
                number_position = [345,566]
                screen.blit(number, number_position)
                number_position = [658,665]
                screen.blit(number, number_position)
            if 6 in s.holes:
                number_position = [33,587]
                screen.blit(number, number_position)
                number_position = [430,409]
                screen.blit(number, number_position)
                number_position = [533,508]
                screen.blit(number, number_position)

            if 7 in s.holes:
                number_position = [200,547]
                screen.blit(number, number_position)
                number_position = [303,565]
                screen.blit(number, number_position)
                number_position = [575,626]
                screen.blit(number, number_position)

            if 8 in s.holes:
                number_position = [32,547]
                screen.blit(number, number_position)
                number_position = [346,408]
                screen.blit(number, number_position)
                number_position = [657,548]
                screen.blit(number, number_position)

            if 9 in s.holes:
                number_position = [116,507]
                screen.blit(number, number_position)
                number_position = [387,487]
                screen.blit(number, number_position)
                number_position = [533,588]
                screen.blit(number, number_position)

            if 10 in s.holes:
                number_position = [33,507]
                screen.blit(number, number_position)
                number_position = [261,447]
                screen.blit(number, number_position)
                number_position = [575,508]
                screen.blit(number, number_position)

            if 11 in s.holes:
                number_position = [158,587]
                screen.blit(number, number_position)
                number_position = [261,565]
                screen.blit(number, number_position)
                number_position = [532,666]
                screen.blit(number, number_position)

            if 12 in s.holes:
                number_position = [33,664]
                screen.blit(number, number_position)
                number_position = [346,448]
                screen.blit(number, number_position)
                number_position = [658,587]
                screen.blit(number, number_position)

            if 13 in s.holes:
                number_position = [200,625]
                screen.blit(number, number_position)
                number_position = [261,525]
                screen.blit(number, number_position)
                number_position = [491,626]
                screen.blit(number, number_position)

            if 14 in s.holes:
                number_position = [116,625]
                screen.blit(number, number_position)
                number_position = [303,488]
                screen.blit(number, number_position)
                number_position = [658,508]
                screen.blit(number, number_position)

            if 15 in s.holes:
                number_position = [200,664]
                screen.blit(number, number_position)
                number_position = [346,487]
                screen.blit(number, number_position)
                number_position = [491,587]
                screen.blit(number, number_position)

            if 16 in s.holes:
                number_position = [117,586]
                screen.blit(number, number_position)
                number_position = [388,409]
                screen.blit(number, number_position)
                number_position = [491,548]
                screen.blit(number, number_position)

            if 17 in s.holes:
                number_position = [200,586]
                screen.blit(number, number_position)
                number_position = [430,527]
                screen.blit(number, number_position)
                number_position = [575,587]
                screen.blit(number, number_position)

            if 18 in s.holes:
                number_position = [75,586]
                screen.blit(number, number_position)
                number_position = [261,408]
                screen.blit(number, number_position)
                number_position = [575,549]
                screen.blit(number, number_position)

            if 19 in s.holes:
                number_position = [158,547]
                screen.blit(number, number_position)
                number_position = [430,448]
                screen.blit(number, number_position)
                number_position = [616,626]
                screen.blit(number, number_position)

            if 20 in s.holes:
                number_position = [75,625]
                screen.blit(number, number_position)
                number_position = [388,447]
                screen.blit(number, number_position)
                number_position = [533,547]
                screen.blit(number, number_position)

            if 21 in s.holes:
                number_position = [158,625]
                screen.blit(number, number_position)
                number_position = [387,526]
                screen.blit(number, number_position)
                number_position = [533,626]
                screen.blit(number, number_position)

            if 22 in s.holes:
                number_position = [75,665]
                screen.blit(number, number_position)
                number_position = [304,526]
                screen.blit(number, number_position)
                number_position = [616,548]
                screen.blit(number, number_position)

            if 23 in s.holes:
                number_position = [74,547]
                screen.blit(number, number_position)
                number_position = [388,565]
                screen.blit(number, number_position)
                number_position = [658,626]
                screen.blit(number, number_position)

            if 24 in s.holes:
                number_position = [34,625]
                screen.blit(number, number_position)
                number_position = [304,447]
                screen.blit(number, number_position)
                number_position = [491,508]
                screen.blit(number, number_position)

            if 25 in s.holes:
                number_position = [158,507]
                screen.blit(number, number_position)
                number_position = [346,526]
                screen.blit(number, number_position)
                number_position = [575,665]
                screen.blit(number, number_position)

    if s.game.hold_feature.position == 1:
        p = [161,731]
        screen.blit(hold_arrow, p)
    elif s.game.hold_feature.position == 2:
        p = [195,731]
        screen.blit(hold_arrow, p)
    elif s.game.hold_feature.position == 3:
        p = [230,731]
        screen.blit(hold_arrow, p)
    elif s.game.hold_feature.position == 4:
        p = [264,731]
        screen.blit(hold_arrow, p)
    elif s.game.hold_feature.position == 5:
        p = [299,731]
        screen.blit(hold_arrow, p)
    elif s.game.hold_feature.position == 6:
        p = [333,731]
        screen.blit(hold_arrow, p)
    elif s.game.hold_feature.position == 7:
        p = [368,731]
        screen.blit(hold_arrow, p)
    elif s.game.hold_feature.position == 8:
        p = [401,725]
        screen.blit(hold, p)
        p = [633,723]
        screen.blit(hold_time, p)

    if s.game.three_as_four.status == True:
        p = [28,721]
        screen.blit(three_as_four, p)

    if s.game.corners.status == True:
        p = [69,330]
        screen.blit(corners, p)

    if s.game.tilt.status == True:
        tilt_position = [35,405]
        screen.blit(tilt, tilt_position)

    pygame.display.flip()
    pygame.display.update()

def eb_animation(num):
    global screen

    if num == 6:
        p = [104,982]
        screen.blit(eb, p)
        pygame.display.update()
    if num == 5:
        p = [152,982]
        screen.blit(eb2, p)
        pygame.display.update()
    if num == 4:
        p = [227,983]
        screen.blit(eb3, p)
        pygame.display.update()
    if num == 3:
        p = [276,982]
        screen.blit(eb, p)
        pygame.display.update()
    if num == 2:
        p = [324,982]
        screen.blit(eb2, p)
        pygame.display.update()
    if num == 1:
        p = [399,983]
        screen.blit(eb3, p)
        pygame.display.update()

def feature_animation(num):
    global screen

    if num == 5:
        p = [30,799]
        screen.blit(odds1, p)
        pygame.display.update()
    if num == 4:
        p = [124,799]
        screen.blit(odds2, p)
        pygame.display.update()
    if num == 3:
        p = [218,801]
        screen.blit(odds3, p)
        pygame.display.update()
    if num == 2:
        p = [312,801]
        screen.blit(odds4, p)
        pygame.display.update()
    if num == 1:
        p = [406,802]
        screen.blit(odds5, p)
        pygame.display.update()

def blink(args):
    dirty_rects = []
    s = args[0]
    b = args[1]
    sn = args[2]

    if b == 0:
        if sn == 1:
            p = [335,686]
            dirty_rects.append(screen.blit(select_now, p))
        pygame.display.update(dirty_rects)
    else:
        dirty_rects.append(screen.blit(bg_gi, (335,686), pygame.Rect(335,686,140,33)))
        pygame.display.update(dirty_rects)
    b = not b

    args = [s,b,sn]

    s.delay(name="blink", delay=0.1, handler=blink, param=args)
