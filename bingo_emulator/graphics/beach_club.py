
import pygame
import random

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

meter = pygame.image.load('graphics/assets/register_cover.png').convert()
arrow = pygame.image.load('beach_club/assets/arrow.png').convert_alpha()
sc = pygame.image.load('beach_club/assets/super_card.png').convert_alpha()
eb = pygame.image.load('beach_club/assets/eb.png').convert_alpha()
number_eb = pygame.image.load('beach_club/assets/number_eb.png').convert_alpha()
o1 = pygame.image.load('beach_club/assets/odds1.png').convert_alpha()
o2 = pygame.image.load('beach_club/assets/odds2.png').convert_alpha()
o3 = pygame.image.load('beach_club/assets/odds3.png').convert_alpha()
o4 = pygame.image.load('beach_club/assets/odds4.png').convert_alpha()
o5 = pygame.image.load('beach_club/assets/odds5.png').convert_alpha()
o6 = pygame.image.load('beach_club/assets/odds6.png').convert_alpha()
o7 = pygame.image.load('beach_club/assets/odds7.png').convert_alpha()
o8 = pygame.image.load('beach_club/assets/odds8.png').convert_alpha()
c = pygame.image.load('beach_club/assets/corners.png').convert_alpha()
star = pygame.image.load('beach_club/assets/star.png').convert_alpha()
number = pygame.image.load('beach_club/assets/number.png').convert_alpha()
sc_number = pygame.image.load('beach_club/assets/sc_number.png').convert_alpha()
tilt = pygame.image.load('beach_club/assets/tilt.png').convert_alpha()
s_number = pygame.image.load('beach_club/assets/s_number.png').convert_alpha()
s_arrow = pygame.image.load('beach_club/assets/s_arrow.png').convert_alpha()
feature = pygame.image.load('beach_club/assets/feature.png').convert_alpha()
select_now = pygame.image.load('beach_club/assets/select_now.png').convert_alpha()
time = pygame.image.load('beach_club/assets/time.png').convert_alpha()
ebs = pygame.image.load('beach_club/assets/extra_ball.png').convert_alpha()
red_number = pygame.image.load('beach_club/assets/red_number.png').convert_alpha()
red_sc_number = pygame.image.load('beach_club/assets/red_sc_number.png').convert_alpha()

class scorereel():
    """ Score Reels are used to count replays """
    def __init__(self, pos, image):
        self.position = pos
        self.default_y = self.position[1]
        self.image = pygame.image.load(image).convert()

reel1 = scorereel([626,315], "graphics/assets/green_reel.png")
reel10 = scorereel([606,315], "graphics/assets/green_reel.png")
reel100 = scorereel([588,315], "graphics/assets/green_reel.png")

def display(s, replays=0, menu=False):
    
    meter.set_colorkey((255,0,252))
    meter_position = [579,315]

    screen.blit(reel1.image, reel1.position)
    screen.blit(reel10.image, reel10.position)
    screen.blit(reel100.image, reel100.position)
    screen.blit(meter, meter_position)

    backglass_position = [0, 0]
    backglass = pygame.Surface(screen.get_size(), flags=pygame.SRCALPHA)
    backglass.fill((0, 0, 0))
    if menu == True:
        backglass = pygame.image.load('beach_club/assets/beach_club_menu.png')
    else:
        if (s.game.anti_cheat.status == True):
            backglass = pygame.image.load('beach_club/assets/beach_club_gi.png')
        else:
            backglass = pygame.image.load('beach_club/assets/beach_club_off.png')
    backglass = pygame.transform.scale(backglass, (720, 1280))
    
    screen.blit(backglass, backglass_position)

    if s.game.super_card.position == 1:
        p = [47,447]
        screen.blit(arrow, p)
    if s.game.super_card.position == 2:
        p = [73,446]
        screen.blit(arrow, p)
    if s.game.super_card.position == 3:
        p = [101,445]
        screen.blit(arrow, p)
    if s.game.super_card.position == 4:
        p = [128,445]
        screen.blit(arrow, p)
    if s.game.super_card.position == 5:
        p = [579,442]
        screen.blit(arrow, p)
    if s.game.super_card.position == 6:
        p = [607,442]
        screen.blit(arrow, p)
    if s.game.super_card.position == 7:
        p = [634,442]
        screen.blit(arrow, p)
    if s.game.super_card.position == 8:
        p = [659,443]
        screen.blit(arrow, p)

    if s.game.super_card.position >= 4:
        p = [46,470]
        screen.blit(sc, p)

    if s.game.super_card.position >= 8:
        p = [578,468]
        screen.blit(sc, p)

    if s.game.extra_ball.position >= 1:
        eb_position = [80,998]
        screen.blit(number_eb, eb_position)
    if s.game.extra_ball.position >= 2:
        eb_position = [128,998]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 3:
        eb_position = [192,998]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 4:
        eb_position = [271,996]
        screen.blit(number_eb, eb_position)
    if s.game.extra_ball.position >= 5:
        eb_position = [318,996]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 6:
        eb_position = [383,994]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 7:
        eb_position = [461,994]
        screen.blit(number_eb, eb_position)
    if s.game.extra_ball.position >= 8:
        eb_position = [510,992]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 9:
        eb_position = [575,990]
        screen.blit(eb, eb_position)
    
    
    if s.game.odds.position > 0:
        if s.game.odds.position == 1:
            odds_position = [94,811]
            screen.blit(o1, odds_position)
        if s.game.odds.position == 2:
            odds_position = [220,820]
            screen.blit(o2, odds_position)
        if s.game.odds.position == 3:
            odds_position = [267,815]
            screen.blit(o3, odds_position)
        if s.game.odds.position == 4:
            odds_position = [346,822]
            screen.blit(o4, odds_position)
        if s.game.odds.position == 5:
            odds_position = [411,802]
            screen.blit(o5, odds_position)
        if s.game.odds.position == 6:
            odds_position = [471,799]
            screen.blit(o6, odds_position)
        if s.game.odds.position == 7:
            odds_position = [518,799]
            screen.blit(o7, odds_position)
        if s.game.odds.position == 8:
            odds_position = [574,799]
            screen.blit(o8, odds_position)

    if s.game.red_star.status == True:
        rs_position = [22,739]
        screen.blit(star, rs_position)

    if s.game.yellow_star.status == True:
        ys_position = [623,735]
        screen.blit(star, ys_position)

    if s.game.corners.status == True:
        corners_position = [60,303]
        screen.blit(c, corners_position)

    if s.game.tilt.status == False:
        if s.holes:
            if 1 in s.holes:
                number_position = [221,501]
                screen.blit(number, number_position)
                number_position = [559,550]
                screen.blit(sc_number, number_position)
            if 2 in s.holes:
                number_position = [223,444]
                screen.blit(number, number_position)
            if 3 in s.holes:
                number_position = [457,559]
                screen.blit(number, number_position)
                number_position = [78,505]
                screen.blit(sc_number, number_position)
            if 4 in s.holes:
                number_position = [284,328]
                screen.blit(number, number_position)
                number_position = [610,600]
                screen.blit(sc_number, number_position)
            if 5 in s.holes:
                number_position = [340,560]
                screen.blit(number, number_position)
            if 6 in s.holes:
                number_position = [459,327]
                screen.blit(number, number_position)
            if 7 in s.holes:
                number_position = [281,558]
                screen.blit(number, number_position)
                number_position = [609,498]
                screen.blit(sc_number, number_position)
            if 8 in s.holes:
                number_position = [459,385]
                screen.blit(number, number_position)
            if 9 in s.holes:
                number_position = [225,328]
                screen.blit(number, number_position)
                number_position = [27,556]
                screen.blit(sc_number, number_position)
            if 10 in s.holes:
                number_position = [225,386]
                screen.blit(number, number_position)
                number_position = [609,550]
                screen.blit(sc_number, number_position)
            if 11 in s.holes:
                number_position = [222,559]
                screen.blit(number, number_position)
                number_position = [657,499]
                screen.blit(sc_number, number_position)
                number_position = [128,554]
                screen.blit(sc_number, number_position)
            if 12 in s.holes:
                number_position = [401,442]
                screen.blit(number, number_position)
                number_position = [26,605]
                screen.blit(sc_number, number_position)
            if 13 in s.holes:
                number_position = [341,500]
                screen.blit(number, number_position)
                number_position = [658,549]
                screen.blit(sc_number, number_position)
            if 14 in s.holes:
                number_position = [342,386]
                screen.blit(number, number_position)
                number_position = [128,604]
                screen.blit(sc_number, number_position)
            if 15 in s.holes:
                number_position = [343,328]
                screen.blit(number, number_position)
                number_position = [560,498]
                screen.blit(sc_number, number_position)
            if 16 in s.holes:
                number_position = [341,444]
                screen.blit(number, number_position)
            if 17 in s.holes:
                number_position = [459,499]
                screen.blit(number, number_position)
                number_position = [560,600]
                screen.blit(sc_number, number_position)
            if 18 in s.holes:
                number_position = [283,444]
                screen.blit(number, number_position)
                number_position = [658,599]
                screen.blit(sc_number, number_position)
                number_position = [128,505]
                screen.blit(sc_number, number_position)
            if 19 in s.holes:
                number_position = [283,386]
                screen.blit(number, number_position)
            if 20 in s.holes:
                number_position = [400,385]
                screen.blit(number, number_position)
            if 21 in s.holes:
                number_position = [400,499]
                screen.blit(number, number_position)
            if 22 in s.holes:
                number_position = [282,500]
                screen.blit(number, number_position)
            if 23 in s.holes:
                number_position = [400,560]
                screen.blit(number, number_position)
                number_position = [26,504]
                screen.blit(sc_number, number_position)
            if 24 in s.holes:
                number_position = [400,328]
                screen.blit(number, number_position)
                number_position = [76,605]
                screen.blit(sc_number, number_position)
            if 25 in s.holes:
                number_position = [458,443]
                screen.blit(number, number_position)
                number_position = [76,554]
                screen.blit(sc_number, number_position)

    if s.game.tilt.status == True:
        tilt_position = [138,746]
        screen.blit(tilt, tilt_position)

    if s.game.spotted_numbers.position == 1:
        p = [222,634]
        screen.blit(s_arrow, p)
    if s.game.spotted_numbers.position == 2:
        p = [261,634]
        screen.blit(s_arrow, p)
    if s.game.spotted_numbers.position == 3:
        p = [299,635]
        screen.blit(s_arrow, p)
    if s.game.spotted_numbers.position >= 4:
        p = [337,634]
        screen.blit(s_arrow, p)
        p = [200,675]
        screen.blit(s_number, p)
        p = [359,636]
        screen.blit(feature, p)
    if s.game.spotted_numbers.position >= 5:
        p = [249,679]
        screen.blit(s_number, p)
    if s.game.spotted_numbers.position >= 6:
        p = [296,678]
        screen.blit(s_number, p)
    if s.game.spotted_numbers.position >= 7:
        p = [343,678]
        screen.blit(s_number, p)
    if s.game.spotted_numbers.position >= 8:
        p = [390,678]
        screen.blit(s_number, p)
    if s.game.spotted_numbers.position >= 9:
        p = [437,676]
        screen.blit(s_number, p)
    if s.game.spotted_numbers.position >= 10:
        p = [484,676]
        screen.blit(s_number, p)

    if s.game.select_spots.status == True and s.game.before_fourth.status == True and s.game.ball_count.position == 3:
        p = [288,726]
        screen.blit(select_now, p)
    
    if s.game.select_spots.status == True and s.game.before_fifth.status == True and s.game.ball_count.position == 4:
        p = [288,726]
        screen.blit(select_now, p)

    if s.game.before_fourth.status == True and s.game.spotted_numbers.position > 3:
        p = [50,671]
        screen.blit(time, p)
    if s.game.before_fifth.status == True and s.game.spotted_numbers.position > 3:
        p = [583,664]
        screen.blit(time, p)

    if s.game.eb_play.status == True:
        ebs_position = [288,969]
        screen.blit(ebs, ebs_position)

    if s.game.select_spots.status == True:
        if s.game.before_fourth.status == True:
            if s.game.ball_count.position < 4:
                if s.game.spotted_numbers.position >= 6:
                    if s.game.spotted.position == 0:
                        #19
                        number_position = [283,386]
                        screen.blit(red_number, number_position)
                    elif s.game.spotted.position == 1:
                        #20
                        number_position = [400,385]
                        screen.blit(red_number, number_position)
                    elif s.game.spotted.position == 2:
                        #21
                        number_position = [400,499]
                        screen.blit(red_number, number_position)
                if s.game.spotted_numbers.position >= 7:
                    if s.game.spotted.position == 3:
                        #22
                        number_position = [282,500]
                        screen.blit(red_number, number_position)
                if s.game.spotted_numbers.position >= 8:
                    if s.game.spotted.position == 4:
                        #16
                        number_position = [341,444]
                        screen.blit(red_number, number_position)
                if s.game.spotted_numbers.position >= 9:
                    if s.game.spotted.position == 5:
                        #25
                        number_position = [458,443]
                        screen.blit(red_number, number_position)
                        number_position = [76,556]
                        screen.blit(red_sc_number, number_position)
                if s.game.spotted_numbers.position >= 10:
                    if s.game.spotted.position == 6:
                        #10
                        number_position = [225,386]
                        screen.blit(red_number, number_position)
                        number_position = [609,552]
                        screen.blit(red_sc_number, number_position)
        if s.game.before_fifth.status == True:
            if s.game.ball_count.position < 5:
                if s.game.spotted_numbers.position >= 6:
                    if s.game.spotted.position == 0:
                        #19
                        number_position = [283,386]
                        screen.blit(red_number, number_position)
                    elif s.game.spotted.position == 1:
                        #20
                        number_position = [400,385]
                        screen.blit(red_number, number_position)
                    elif s.game.spotted.position == 2:
                        #21
                        number_position = [400,499]
                        screen.blit(red_number, number_position)
                if s.game.spotted_numbers.position >= 7:
                    if s.game.spotted.position == 3:
                        #22
                        number_position = [282,500]
                        screen.blit(red_number, number_position)
                if s.game.spotted_numbers.position >= 8:
                    if s.game.spotted.position == 4:
                        #16
                        number_position = [341,444]
                        screen.blit(red_number, number_position)
                if s.game.spotted_numbers.position >= 9:
                    if s.game.spotted.position == 5:
                        #25
                        number_position = [458,443]
                        screen.blit(red_number, number_position)
                        number_position = [76,556]
                        screen.blit(red_sc_number, number_position)
                if s.game.spotted_numbers.position >= 10:
                    if s.game.spotted.position == 6:
                        #10
                        number_position = [225,386]
                        screen.blit(red_number, number_position)
                        number_position = [609,552]
                        screen.blit(red_sc_number, number_position)
                
    pygame.display.update()

def eb_animation(num):
    global screen
    if num == 9:
        eb_position = [80,998]
        screen.blit(number_eb, eb_position)
        pygame.display.update()
    if num == 8:
        eb_position = [128,998]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 7:
        eb_position = [192,998]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 6:
        eb_position = [271,996]
        screen.blit(number_eb, eb_position)
        pygame.display.update()
    if num == 5:
        eb_position = [318,996]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 4:
        eb_position = [383,994]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 3:
        eb_position = [461,994]
        screen.blit(number_eb, eb_position)
        pygame.display.update()
    if num == 2:
        eb_position = [510,992]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 1:
        eb_position = [575,990]
        screen.blit(eb, eb_position)
        pygame.display.update()


def feature_animation(num):
    global screen
    if num == 6:
        corners_position = [60,303]
        screen.blit(c, corners_position)
        pygame.display.update()

    if num == 5:
        rs_position = [22,739]
        screen.blit(star, rs_position)
        pygame.display.update()

    if num == 4:
        ys_position = [623,735]
        screen.blit(star, ys_position)
        pygame.display.update()

    if num == 3:
        p = [359,636]
        screen.blit(feature, p)
        pygame.display.update()
   
    if num == 2:
        p = [46,466]
        screen.blit(sc, p)
        pygame.display.update()

    if num == 1:
        p = [580,463]
        screen.blit(sc, p)
        pygame.display.update()


def odds_animation(num):
    global screen
    if num == 5:
        odds_position = [93,813]
        o = pygame.image.load('beach_club/assets/odds1.png').convert_alpha()
        screen.blit(o, odds_position)
        pygame.display.update()
    if num == 4:
        odds_position = [220,821]
        o = pygame.image.load('beach_club/assets/odds2.png').convert_alpha()
        screen.blit(o, odds_position)
        pygame.display.update()
    if num == 3:
        odds_position = [267,818]
        o = pygame.image.load('beach_club/assets/odds3.png').convert_alpha()
        screen.blit(o, odds_position)
        pygame.display.update()
    if num == 2:
        odds_position = [343,823]
        o = pygame.image.load('beach_club/assets/odds4.png').convert_alpha()
        screen.blit(o, odds_position)
        pygame.display.update()
    if num == 1:
        odds_position = [416,808]
        o = pygame.image.load('beach_club/assets/odds5.png').convert_alpha()
        screen.blit(o, odds_position)
        pygame.display.update()
