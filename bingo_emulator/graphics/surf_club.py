
import pygame, random

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

meter = pygame.image.load('graphics/assets/register_cover.png').convert()
corners = pygame.image.load('surf_club/assets/corners.png').convert_alpha()
odds1 = pygame.image.load('surf_club/assets/odds1.png').convert_alpha()
odds2 = pygame.image.load('surf_club/assets/odds2.png').convert_alpha()
odds3 = pygame.image.load('surf_club/assets/odds3.png').convert_alpha()
odds4 = pygame.image.load('surf_club/assets/odds4.png').convert_alpha()
odds5 = pygame.image.load('surf_club/assets/odds5.png').convert_alpha()
odds6 = pygame.image.load('surf_club/assets/odds6.png').convert_alpha()
odds7 = pygame.image.load('surf_club/assets/odds7.png').convert_alpha()
odds8 = pygame.image.load('surf_club/assets/odds8.png').convert_alpha()
star = pygame.image.load('surf_club/assets/rollover.png').convert_alpha()
extra_balls = pygame.image.load('surf_club/assets/extra_ball.png').convert_alpha()
eb = pygame.image.load('surf_club/assets/eb.png').convert_alpha()
eb2 = pygame.image.load('surf_club/assets/eb_extra.png').convert_alpha()
eb3 = pygame.image.load('surf_club/assets/eb_ball.png').convert_alpha()
number = pygame.image.load('surf_club/assets/number.png').convert_alpha()
sc_number = pygame.image.load('surf_club/assets/sc_number.png').convert_alpha()
tilt = pygame.image.load('surf_club/assets/tilt.png').convert_alpha()
hold_arrow = pygame.image.load('surf_club/assets/sc_arrow.png').convert_alpha()
sc = pygame.image.load('surf_club/assets/sc.png').convert_alpha()
hold = pygame.image.load('surf_club/assets/hold.png').convert_alpha()
double_hold = pygame.image.load('surf_club/assets/double_hold.png').convert_alpha()
hold_now = pygame.image.load('surf_club/assets/hold_now.png').convert_alpha()
select_now = pygame.image.load('surf_club/assets/select_now.png').convert_alpha()
spot_number = pygame.image.load('surf_club/assets/spot_number.png').convert_alpha()
super_line = pygame.image.load('surf_club/assets/super_line.png').convert_alpha()
super_line_info = pygame.image.load('surf_club/assets/super_line_info.png').convert_alpha()
spot_arrow = pygame.image.load('surf_club/assets/super_line_arrow.png').convert_alpha()
rollover = pygame.image.load('surf_club/assets/rollover.png').convert_alpha()
bg_menu = pygame.image.load('surf_club/assets/surf_club_menu.png')
bg_gi = pygame.image.load('surf_club/assets/surf_club_gi.png')
bg_off = pygame.image.load('surf_club/assets/surf_club_off.png')

class scorereel():
    """ Score Reels are used to count replays """
    def __init__(self, pos, image):
        self.position = pos
        self.default_y = self.position[1]
        self.image = pygame.image.load(image).convert()

reel1 = scorereel([619,327], "graphics/assets/green_reel.png")
reel10 = scorereel([601,327], "graphics/assets/green_reel.png")
reel100 = scorereel([582,327], "graphics/assets/green_reel.png")

def display(s, replays=0, menu=False):
    
    meter.set_colorkey((255,0,252))
    meter_position = [572,327]

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

    if s.game.odds.position == 1:
        p = [107,818]
        screen.blit(odds1, p)
    if s.game.odds.position == 2:
        p = [170,821]
        screen.blit(odds2, p)
    if s.game.odds.position == 3:
        p = [220,819]
        screen.blit(odds3, p)
    if s.game.odds.position == 4:
        p = [289,849]
        screen.blit(odds4, p)
    if s.game.odds.position == 5:
        p = [325,822]
        screen.blit(odds5, p)
    if s.game.odds.position == 6:
        p = [383,846]
        screen.blit(odds6, p)
    if s.game.odds.position == 7:
        p = [503,820]
        screen.blit(odds7, p)
    if s.game.odds.position == 8:
        p = [649,820]
        screen.blit(odds8, p)

    if s.game.eb_play.status == True:
        p = [299,974]
        screen.blit(extra_balls, p)

    if s.game.extra_ball.position >= 1:
        p = [115,1011]
        screen.blit(eb, p)
    if s.game.extra_ball.position >= 2:
        p = [154,1011]
        screen.blit(eb2, p)
    if s.game.extra_ball.position >= 3:
        p = [214,1011]
        screen.blit(eb3, p)
    if s.game.extra_ball.position >= 4:
        p = [287,1010]
        screen.blit(eb, p)
    if s.game.extra_ball.position >= 5:
        p = [325,1010]
        screen.blit(eb2, p)
    if s.game.extra_ball.position >= 6:
        p = [388,1010]
        screen.blit(eb3, p)
    if s.game.extra_ball.position >= 7:
        p = [462,1008]
        screen.blit(eb, p)
    if s.game.extra_ball.position >= 8:
        p = [500,1008]
        screen.blit(eb2, p)
    if s.game.extra_ball.position >= 9:
        p = [561,1008]
        screen.blit(eb3, p)


    if s.game.tilt.status == False:
        if s.holes:
            if 1 in s.holes:
                number_position = [455,469]
                screen.blit(number, number_position)
            if 2 in s.holes:
                number_position = [221,470]
                screen.blit(number, number_position)
            if 3 in s.holes:
                number_position = [456,585]
                screen.blit(number, number_position)
                p = [557,561]
                screen.blit(sc_number, p)
            if 4 in s.holes:
                number_position = [279,358]
                screen.blit(number, number_position)
                p = [78,517]
                screen.blit(sc_number, p)
            if 5 in s.holes:
                number_position = [338,586]
                screen.blit(number, number_position)
            if 6 in s.holes:
                number_position = [454,358]
                screen.blit(number, number_position)
                p = [124,562]
                screen.blit(sc_number, p)
            if 7 in s.holes:
                number_position = [279,586]
                screen.blit(number, number_position)
                p = [602,516]
                screen.blit(sc_number, p)
            if 8 in s.holes:
                number_position = [338,357]
                screen.blit(number, number_position)
            if 9 in s.holes:
                number_position = [396,470]
                screen.blit(number, number_position)
                p = [602,561]
                screen.blit(sc_number, p)
            if 10 in s.holes:
                number_position = [222,414]
                screen.blit(number, number_position)
                p = [33,562]
                screen.blit(sc_number, p)
            if 11 in s.holes:
                number_position = [223,585]
                screen.blit(number, number_position)
                p = [603,607]
                screen.blit(sc_number, p)
            if 12 in s.holes:
                number_position = [338,413]
                screen.blit(number, number_position)
                p = [33,608]
                screen.blit(sc_number, p)
            if 13 in s.holes:
                number_position = [222,528]
                screen.blit(number, number_position)
                p = [648,561]
                screen.blit(sc_number, p)
            if 14 in s.holes:
                number_position = [280,470]
                screen.blit(number, number_position)
                p = [79,562]
                screen.blit(sc_number, p)
            if 15 in s.holes:
                number_position = [338,470]
                screen.blit(number, number_position)
            if 16 in s.holes:
                number_position = [396,358]
                screen.blit(number, number_position)
            if 17 in s.holes:
                number_position = [455,527]
                screen.blit(number, number_position)
                p = [556,607]
                screen.blit(sc_number, p)
            if 18 in s.holes:
                number_position = [223,358]
                screen.blit(number, number_position)
                p = [124,608]
                screen.blit(sc_number, p)
            if 19 in s.holes:
                number_position = [455,414]
                screen.blit(number, number_position)
                p = [647,607]
                screen.blit(sc_number, p)
            if 20 in s.holes:
                number_position = [397,413]
                screen.blit(number, number_position)
                p = [33,518]
                screen.blit(sc_number, p)
            if 21 in s.holes:
                number_position = [398,527]
                screen.blit(number, number_position)
                p = [557,516]
                screen.blit(sc_number, p)
            if 22 in s.holes:
                number_position = [279,527]
                screen.blit(number, number_position)
                p = [124,516]
                screen.blit(sc_number, p)
            if 23 in s.holes:
                number_position = [397,584]
                screen.blit(number, number_position)
                p = [649,517]
                screen.blit(sc_number, p)
            if 24 in s.holes:
                number_position = [281,412]
                screen.blit(number, number_position)
                p = [79,608]
                screen.blit(sc_number, p)
            if 25 in s.holes:
                number_position = [339,527]
                screen.blit(number, number_position)

        if s.game.hold_feature.position == 1:
            p = [522,664]
            screen.blit(hold_arrow, p)
        elif s.game.hold_feature.position == 2:
            p = [568,665]
            screen.blit(hold_arrow, p)
        elif s.game.hold_feature.position == 3:
            p = [614,664]
            screen.blit(hold_arrow, p)
        elif s.game.hold_feature.position == 4:
            p = [658,663]
            screen.blit(hold_arrow, p)
            p = [523,705]
            screen.blit(hold, p)
            if s.game.ball_count.position == 5:
                s.cancel_delayed(name="blink_return")
                blink_return([s,1,1])
            else:
                s.cancel_delayed("blink_return")
        elif s.game.hold_feature.position == 5 or s.game.hold_feature.position == 6:
            p = [658,663]
            screen.blit(hold_arrow, p)
            p = [615,705]
            screen.blit(double_hold, p)
            if s.game.ball_count.position == 5:
                s.cancel_delayed(name="blink_return")
                blink_return([s,1,1])
            else:
                s.cancel_delayed("blink_return")

        if s.game.super_card.position == 1:
            p = [34,454]
            screen.blit(hold_arrow, p)
        elif s.game.super_card.position == 2:
            p = [67,454]
            screen.blit(hold_arrow, p)
        elif s.game.super_card.position == 3:
            p = [103,453]
            screen.blit(hold_arrow, p)
        elif s.game.super_card.position == 4:
            p = [137,452]
            screen.blit(hold_arrow, p)
        elif s.game.super_card.position == 5:
            p = [557,452]
            screen.blit(hold_arrow, p)
        elif s.game.super_card.position == 6:
            p = [591,453]
            screen.blit(hold_arrow, p)
        elif s.game.super_card.position == 7:
            p = [625,453]
            screen.blit(hold_arrow, p)
        elif s.game.super_card.position == 8:
            p = [660,453]
            screen.blit(hold_arrow, p)
            p = [569,481]
            screen.blit(sc, p)

        if s.game.super_card.position >= 4:
            p = [45,480]
            screen.blit(sc, p)


        if s.game.super_card.position < 4:
            p = [23,974]
            screen.blit(rollover, p)

        if s.game.super_card.position >= 4 and s.game.super_card.position < 8:
            p = [627,971]
            screen.blit(rollover, p)

        if s.game.spotted_numbers.position == 1:
            p = [34,666]
            screen.blit(hold_arrow, p)
        if s.game.spotted_numbers.position == 2:
            p = [78,666]
            screen.blit(hold_arrow, p)
        if s.game.spotted_numbers.position == 3:
            p = [124,665]
            screen.blit(hold_arrow, p)
        if s.game.spotted_numbers.position == 4:
            p = [170,665]
            screen.blit(hold_arrow, p)

        if s.game.spotted_numbers.position >= 5:
            p = [19,747]
            screen.blit(spot_number, p)
            if s.game.ball_count.position == 3 and s.game.spotted.position < 3:
                s.cancel_delayed(name="blink")
                blink([s,1,1])
            else:
                s.cancel_delayed(name="blink")
        if s.game.spotted_numbers.position >= 6:
            p = [56,747]
            screen.blit(spot_number, p)
        if s.game.spotted_numbers.position >= 7:
            p = [91,747]
            screen.blit(spot_number, p)
        if s.game.spotted_numbers.position >= 8:
            p = [128,747]
            screen.blit(super_line, p)

            if s.game.spotted.position >= 3:
                if s.game.ball_count.position == 3:
                    s.cancel_delayed(name="blink_super")
                    blink_super([s,1,1])
                else:
                    s.cancel_delayed(name="blink_super")
                    p = [259,681]
                    screen.blit(super_line_info, p)
                if s.game.spotted.position == 3:
                    if 3 in s.holes:
                        p = [231,734]
                        screen.blit(sc_number, p)
                    if 16 in s.holes:
                        p = [275,734]
                        screen.blit(sc_number, p)
                    if 11 in s.holes:
                        p = [319,734]
                        screen.blit(sc_number, p)
                    p = [240,779]
                    screen.blit(spot_arrow, p)
                    p = [283,779]
                    screen.blit(spot_arrow, p)
                    p = [325,779]
                    screen.blit(spot_arrow, p)
                elif s.game.spotted.position == 4:
                    if 16 in s.holes:
                        p = [275,734]
                        screen.blit(sc_number, p)
                    if 11 in s.holes:
                        p = [319,734]
                        screen.blit(sc_number, p)
                    if 10 in s.holes:
                        p = [361,734]
                        screen.blit(sc_number, p)
                    p = [283,779]
                    screen.blit(spot_arrow, p)
                    p = [325,779]
                    screen.blit(spot_arrow, p)
                    p = [367,778]
                    screen.blit(spot_arrow, p)
                elif s.game.spotted.position == 5:
                    if 11 in s.holes:
                        p = [319,734]
                        screen.blit(sc_number, p)
                    if 10 in s.holes:
                        p = [361,734]
                        screen.blit(sc_number, p)
                    if 20 in s.holes:
                        p = [403,733]
                        screen.blit(sc_number, p)
                    p = [325,779]
                    screen.blit(spot_arrow, p)
                    p = [367,779]
                    screen.blit(spot_arrow, p)
                    p = [410,779]
                    screen.blit(spot_arrow, p)
                elif s.game.spotted.position == 6:
                    if 10 in s.holes:
                        p = [361,734]
                        screen.blit(sc_number, p)
                    if 20 in s.holes:
                        p = [403,733]
                        screen.blit(sc_number, p)
                    if 5 in s.holes:
                        p = [446,732]
                        screen.blit(sc_number, p)
                    p = [367,779]
                    screen.blit(spot_arrow, p)
                    p = [410,779]
                    screen.blit(spot_arrow, p)
                    p = [451,778]
                    screen.blit(spot_arrow, p)

        if s.game.corners.status == True:
            p = [69,317]
            screen.blit(corners, p)

    if s.game.tilt.status == True:
        tilt_position = [35,330]
        screen.blit(tilt, tilt_position)

    pygame.display.update()

def blink_super(args):
    dirty_rects = []
    s = args[0]
    b = args[1]
    sn = args[2]

    if b == 0:
        if sn == 1:
            p = [259,681]
            dirty_rects.append(screen.blit(super_line_info, p))
        pygame.display.update(dirty_rects)
    else:
        dirty_rects.append(screen.blit(bg_gi, (259,681), pygame.Rect(259,681,207,55)))
        pygame.display.update(dirty_rects)
    b = not b

    args = [s,b,sn]

    s.delay(name="blink_super", delay=0.1, handler=blink_super, param=args)

def blink(args):
    dirty_rects = []
    s = args[0]
    b = args[1]
    sn = args[2]

    if b == 0:
        if sn == 1:
            p = [45,783]
            dirty_rects.append(screen.blit(select_now, p))
        pygame.display.update(dirty_rects)
    else:
        dirty_rects.append(screen.blit(bg_gi, (45,783), pygame.Rect(45,783,147,33)))
        pygame.display.update(dirty_rects)
    b = not b

    args = [s,b,sn]

    s.delay(name="blink", delay=0.1, handler=blink, param=args)

def blink_return(args):
    dirty_rects = []
    s = args[0]
    b = args[1]
    sn = args[2]

    if b == 0:
        if sn == 1:
            p = [534,782]
            dirty_rects.append(screen.blit(hold_now, p))
        pygame.display.update(dirty_rects)
    else:
        dirty_rects.append(screen.blit(bg_gi, (534,782), pygame.Rect(534,782,143,32)))
        pygame.display.update(dirty_rects)
    b = not b

    args = [s,b,sn]

    s.delay(name="blink_return", delay=0.1, handler=blink_return, param=args)

def eb_animation(num):
    global screen

    if num == 6:
        p = [115,1011]
        screen.blit(eb, p)
        pygame.display.update()
    if num == 5:
        p = [154,1011]
        screen.blit(eb2, p)
        pygame.display.update()
    if num == 4:
        p = [214,1011]
        screen.blit(eb3, p)
        pygame.display.update()
    if num == 3:
        p = [287,1010]
        screen.blit(eb, p)
        pygame.display.update()
    if num == 2:
        p = [325,1010]
        screen.blit(eb2, p)
        pygame.display.update()
    if num == 1:
        p = [388,1010]
        screen.blit(eb3, p)
        pygame.display.update()

def feature_animation(num):
    global screen

    if num == 5:
        p = [107,818]
        screen.blit(odds1, p)
        pygame.display.update()
    if num == 4:
        p = [170,821]
        screen.blit(odds2, p)
        pygame.display.update()
    if num == 3:
        p = [220,819]
        screen.blit(odds3, p)
        pygame.display.update()
    if num == 2:
        p = [289,849]
        screen.blit(odds4, p)
        pygame.display.update()
    if num == 1:
        p = [325,822]
        screen.blit(odds5, p)
        pygame.display.update()

