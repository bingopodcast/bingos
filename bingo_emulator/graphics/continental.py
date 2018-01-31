
import pygame

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

card = pygame.image.load('continental/assets/card.png').convert_alpha()
number = pygame.image.load('continental/assets/number.png').convert_alpha()
red_diagonal = pygame.image.load('continental/assets/red_diagonal.png').convert_alpha()
feature = pygame.image.load('continental/assets/feature.png').convert_alpha()
magic_number = pygame.image.load('continental/assets/magic_number.png').convert_alpha()
all_double = pygame.image.load('continental/assets/all_double.png').convert_alpha()
eleventh_coin = pygame.image.load('continental/assets/eleventh_coin.png').convert_alpha()
dd_card = pygame.image.load('continental/assets/dd_card.png').convert_alpha()
corners = pygame.image.load('continental/assets/corners.png').convert_alpha()
super_line = pygame.image.load('continental/assets/super_line.png').convert_alpha()
c = pygame.image.load('continental/assets/regular.png').convert_alpha()
d = pygame.image.load('continental/assets/double.png').convert_alpha()
n = pygame.image.load('continental/assets/nothing.png').convert_alpha()
tilt = pygame.image.load('continental/assets/tilt.png').convert_alpha()
blink_image = pygame.image.load('continental/assets/double_or_nothing.png').convert_alpha()
bg_menu = pygame.image.load('continental/assets/continental_menu.png')
bg_gi = pygame.image.load('continental/assets/continental_gi.png')
bg_off = pygame.image.load('continental/assets/continental_off.png')

class scorereel():
    """ Score Reels are used to count replays """
    def __init__(self, pos, image):
        self.position = pos
        self.default_y = self.position[1]
        self.image = pygame.image.load(image).convert()

reel1 = scorereel([297,660], "graphics/assets/digital_reel.png")
reel10 = scorereel([275,660], "graphics/assets/digital_reel.png")
reel100 = scorereel([253,660], "graphics/assets/digital_reel.png")
reel1000 = scorereel([230,660], "graphics/assets/digital_reel.png")

def display(s, replays=0, menu=False):
    
    screen.blit(reel1.image, reel1.position)
    screen.blit(reel10.image, reel10.position)
    screen.blit(reel100.image, reel100.position)
    screen.blit(reel1000.image, reel1000.position)

    backglass_position = [0, 0]
    backglass = pygame.Surface((720,1280), pygame.SRCALPHA | pygame.FULLSCREEN)
    backglass.fill((0, 0, 0))
    if menu == True:
        screen.blit(bg_menu, backglass_position)
    else:
        if (s.game.anti_cheat.status == True):
            screen.blit(bg_gi, backglass_position)
        else:
            screen.blit(bg_off, backglass_position)

    if s.game.selector.position >= 1:
        position = [10,278]
        screen.blit(card, position)
    if s.game.selector.position >= 2:
        position = [247,277]
        screen.blit(card, position)
    if s.game.selector.position >= 3:
        position = [487,277]
        screen.blit(card, position)
    if s.game.selector.position >= 4:
        position = [11,787]
        screen.blit(card, position)
    if s.game.selector.position >= 5:
        position = [248,774]
        screen.blit(card, position)
    if s.game.selector.position >= 6:
        position = [487,781]
        screen.blit(card, position)

    if s.game.tilt.status == False:
        if s.holes:
            if 1 in s.holes:
                position = [85,374]
                screen.blit(number, position)
                position = [286,484]
                screen.blit(number, position)
                position = [674,376]
                screen.blit(number, position)
                position = [159,1029]
                screen.blit(number, position)
                position = [360,869]
                screen.blit(number, position)
                position = [525,1022]
                screen.blit(number, position)
            if 2 in s.holes:
                position = [120,522]
                screen.blit(number, position)
                position = [286,446]
                screen.blit(number, position)
                position = [674,412]
                screen.blit(number, position)
                position = [196,956]
                screen.blit(number, position)
                position = [398,1018]
                screen.blit(number, position)
                position = [526,912]
                screen.blit(number, position)
            if 3 in s.holes:
                position = [196,374]
                screen.blit(number, position)
                position = [434,523]
                screen.blit(number, position)
                position = [600,376]
                screen.blit(number, position)
                position = [50,883]
                screen.blit(number, position)
                position = [361,906]
                screen.blit(number, position)
                position = [634,1023]
                screen.blit(number, position)
            if 4 in s.holes:
                position = [158,522]
                screen.blit(number, position)
                position = [397,374]
                screen.blit(number, position)
                position = [636,524]
                screen.blit(number, position)
                position = [160,882]
                screen.blit(number, position)
                position = [288,870]
                screen.blit(number, position)
                position = [672,876]
                screen.blit(number, position)
            if 5 in s.holes:
                position = [50,374]
                screen.blit(number, position)
                position = [360,523]
                screen.blit(number, position)
                position = [526,448]
                screen.blit(number, position)
                position = [198,1030]
                screen.blit(number, position)
                position = [435,870]
                screen.blit(number, position)
                position = [671,949]
                screen.blit(number, position)
            if 6 in s.holes:
                position = [49,447]
                screen.blit(number, position)
                position = [434,374]
                screen.blit(number, position)
                position = [528,374]
                screen.blit(number, position)
                position = [52,1028]
                screen.blit(number, position)
                position = [325,870]
                screen.blit(number, position)
                position = [670,1022]
                screen.blit(number, position)
            if 7 in s.holes:
                position = [196,410]
                screen.blit(number, position)
                position = [324,522]
                screen.blit(number, position)
                position = [564,375]
                screen.blit(number, position)
                position = [87,882]
                screen.blit(number, position)
                position = [288,1016]
                screen.blit(number, position)
                position = [562,1022]
                screen.blit(number, position)
            if 8 in s.holes:
                position = [49,411]
                screen.blit(number, position)
                position = [434,484]
                screen.blit(number, position)
                position = [674,524]
                screen.blit(number, position)
                position = [197,919]
                screen.blit(number, position)
                position = [434,980]
                screen.blit(number, position)
                position = [526,877]
                screen.blit(number, position)
            if 9 in s.holes:
                position = [122,373]
                screen.blit(number, position)
                position = [287,373]
                screen.blit(number, position)
                position = [600,486]
                screen.blit(number, position)
                position = [197,883]
                screen.blit(number, position)
                position = [289,943]
                screen.blit(number, position)
                position = [599,986]
                screen.blit(number, position)
            if 10 in s.holes:
                position = [124,409]
                screen.blit(number, position)
                position = [287,522]
                screen.blit(number, position)
                position = [527,522]
                screen.blit(number, position)
                position = [124,883]
                screen.blit(number, position)
                position = [288,980]
                screen.blit(number, position)
                position = [599,875]
                screen.blit(number, position)
            if 11 in s.holes:
                position = [159,446]
                screen.blit(number, position)
                position = [361,484]
                screen.blit(number, position)
                position = [526,485]
                screen.blit(number, position)
                position = [161,956]
                screen.blit(number, position)
                position = [434,1016]
                screen.blit(number, position)
                position = [671,985]
                screen.blit(number, position)
            if 12 in s.holes:
                position = [49,521]
                screen.blit(number, position)
                position = [397,447]
                screen.blit(number, position)
                position = [601,411]
                screen.blit(number, position)
                position = [124,993]
                screen.blit(number, position)
                position = [398,943]
                screen.blit(number, position)
                position = [562,948]
                screen.blit(number, position)
            if 13 in s.holes:
                position = [195,484]
                screen.blit(number, position)
                position = [287,410]
                screen.blit(number, position)
                position = [564,523]
                screen.blit(number, position)
                position = [51,992]
                screen.blit(number, position)
                position = [435,906]
                screen.blit(number, position)
                position = [635,875]
                screen.blit(number, position)
            if 14 in s.holes:
                position = [122,484]
                screen.blit(number, position)
                position = [361,409]
                screen.blit(number, position)
                position = [564,411]
                screen.blit(number, position)
                position = [88,955]
                screen.blit(number, position)
                position = [398,981]
                screen.blit(number, position)
                position = [635,911]
                screen.blit(number, position)
            if 15 in s.holes:
                position = [196,522]
                screen.blit(number, position)
                position = [360,446]
                screen.blit(number, position)
                position = [637,486]
                screen.blit(number, position)
                position = [51,954]
                screen.blit(number, position)
                position = [325,906]
                screen.blit(number, position)
                position = [563,986]
                screen.blit(number, position)
            if 16 in s.holes:
                position = [123,446]
                screen.blit(number, position)
                position = [361,373]
                screen.blit(number, position)
                position = [637,448]
                screen.blit(number, position)
                position = [125,1029]
                screen.blit(number, position)
                position = [362,980]
                screen.blit(number, position)
                position = [599,912]
                screen.blit(number, position)
            if 17 in s.holes:
                position = [196,446]
                screen.blit(number, position)
                position = [434,447]
                screen.blit(number, position)
                position = [564,485]
                screen.blit(number, position)
                position = [123,955]
                screen.blit(number, position)
                position = [398,906]
                screen.blit(number, position)
                position = [563,912]
                screen.blit(number, position)
            if 18 in s.holes:
                position = [86,447]
                screen.blit(number, position)
                position = [324,447]
                screen.blit(number, position)
                position = [637,412]
                screen.blit(number, position)
                position = [125,919]
                screen.blit(number, position)
                position = [325,980]
                screen.blit(number, position)
                position = [635,985]
                screen.blit(number, position)
            if 19 in s.holes:
                position = [159,409]
                screen.blit(number, position)
                position = [324,409]
                screen.blit(number, position)
                position = [564,448]
                screen.blit(number, position)
                position = [161,992]
                screen.blit(number, position)
                position = [326,942]
                screen.blit(number, position)
                position = [635,948]
                screen.blit(number, position)
            if 20 in s.holes:
                position = [159,485]
                screen.blit(number, position)
                position = [398,409]
                screen.blit(number, position)
                position = [601,448]
                screen.blit(number, position)
                position = [88,991]
                screen.blit(number, position)
                position = [435,943]
                screen.blit(number, position)
                position = [526,948]
                screen.blit(number, position)
            if 21 in s.holes:
                position = [86,484]
                screen.blit(number, position)
                position = [397,485]
                screen.blit(number, position)
                position = [601,523]
                screen.blit(number, position)
                position = [88,919]
                screen.blit(number, position)
                position = [362,943]
                screen.blit(number, position)
                position = [599,1022]
                screen.blit(number, position)
            if 22 in s.holes:
                position = [86,409]
                screen.blit(number, position)
                position = [324,484]
                screen.blit(number, position)
                position = [674,449]
                screen.blit(number, position)
                position = [161,919]
                screen.blit(number, position)
                position = [362,1017]
                screen.blit(number, position)
                position = [599,948]
                screen.blit(number, position)
            if 23 in s.holes:
                position = [86,522]
                screen.blit(number, position)
                position = [398,522]
                screen.blit(number, position)
                position = [527,410]
                screen.blit(number, position)
                position = [197,993]
                screen.blit(number, position)
                position = [398,869]
                screen.blit(number, position)
                position = [563,876]
                screen.blit(number, position)
            if 24 in s.holes:
                position = [48,485]
                screen.blit(number, position)
                position = [325,373]
                screen.blit(number, position)
                position = [637,375]
                screen.blit(number, position)
                position = [51,918]
                screen.blit(number, position)
                position = [325,1017]
                screen.blit(number, position)
                position = [672,911]
                screen.blit(number, position)
            if 25 in s.holes:
                position = [159,373]
                screen.blit(number, position)
                position = [435,409]
                screen.blit(number, position)
                position = [674,487]
                screen.blit(number, position)
                position = [88,1028]
                screen.blit(number, position)
                position = [289,906]
                screen.blit(number, position)
                position = [526,986]
                screen.blit(number, position)

        if s.game.selector.position > 6:
            p = [8,371]
            screen.blit(red_diagonal, p)
            p = [245,371]
            screen.blit(red_diagonal, p)
            p = [486,371]
            screen.blit(red_diagonal, p)
            p = [29,590]
            screen.blit(feature, p)

        if s.game.selector.position > 7:
            p = [10,876]
            screen.blit(red_diagonal, p)
            p = [247,865]
            screen.blit(red_diagonal, p)
            p = [485,871]
            screen.blit(red_diagonal, p)
            p = [29,650]
            screen.blit(feature, p)

        if s.game.selector.position > 8:
            p = [366,573]
            screen.blit(feature, p)
            p = [395,729]
            screen.blit(magic_number, p)

        if s.game.selector.position > 9:
            p = [366,632]
            screen.blit(feature, p)

        if 1 in s.game.magic:
            p = [364,728]
            screen.blit(number, p)
        if 7 in s.game.magic:
            p = [386,696]
            screen.blit(number, p)
        if 9 in s.game.magic:
            p = [425,691]
            screen.blit(number, p)
        if 22 in s.game.magic:
            p = [464,695]
            screen.blit(number, p)
        if 25 in s.game.magic:
            p = [485,728]
            screen.blit(number, p)

        if s.game.onetwothree.status == True:
            p = [126,308]
            screen.blit(all_double, p)
            p = [364,308]
            screen.blit(all_double, p)
            p = [602,309]
            screen.blit(all_double, p)
            if s.game.dd1.status == True:
                p = [126,276]
                screen.blit(all_double, p)
            if s.game.dd2.status == True:
                p = [364,276]
                screen.blit(all_double, p)
            if s.game.dd3.status == True:
                p = [602,278]
                screen.blit(all_double, p)
        
        if s.game.fourfivesix.status == True:
            p = [126,818]
            screen.blit(all_double, p)
            p = [365,805]
            screen.blit(all_double, p)
            p = [602,811]
            screen.blit(all_double, p)
            if s.game.dd4.status == True:
                p = [126,786]
                screen.blit(all_double, p)
            if s.game.dd5.status == True:
                p = [364,773]
                screen.blit(all_double, p)
            if s.game.dd6.status == True:
                p = [602,779]
                screen.blit(all_double, p)

        if s.game.selector.position >= 11:
            p = [546,572]
            screen.blit(eleventh_coin, p)
            p = [544,706]
            screen.blit(feature, p)

        if s.game.dd1.status == True:
            p = [530,634]
            screen.blit(dd_card, p)
        if s.game.dd2.status == True:
            p = [591,634]
            screen.blit(dd_card, p)
        if s.game.dd3.status == True:
            p = [650,634]
            screen.blit(dd_card, p)
        if s.game.dd4.status == True:
            p = [530,680]
            screen.blit(dd_card, p)
        if s.game.dd5.status == True:
            p = [590,680]
            screen.blit(dd_card, p)
        if s.game.dd6.status == True:
            p = [650,680]
            screen.blit(dd_card, p)

        if s.game.corners1.status == True:
            position = [11,308]
            screen.blit(corners, position)
        if s.game.corners2.status == True:
            position = [247,308]
            screen.blit(corners, position)
        if s.game.corners3.status == True:
            position = [488,308]
            screen.blit(corners, position)
        if s.game.corners4.status == True:
            position = [11,817]
            screen.blit(corners, position)
        if s.game.corners5.status == True:
            position = [249,804]
            screen.blit(corners, position)
        if s.game.corners6.status == True:
            position = [487,811]
            screen.blit(corners, position)

        if s.game.super1.status == True:
            position = [10,480]
            screen.blit(super_line, position)
        if s.game.super2.status == True:
            position = [248,480]
            screen.blit(super_line, position)
        if s.game.super3.status == True:
            position = [488,481]
            screen.blit(super_line, position)
        if s.game.super4.status == True:
            position = [12,985]
            screen.blit(super_line, position)
        if s.game.super5.status == True:
            position = [250,974]
            screen.blit(super_line, position)
        if s.game.super6.status == True:
            position = [488,980]
            screen.blit(super_line, position)

        if s.game.card1_replay_counter.position > 0 or s.game.card2_replay_counter.position > 0 or s.game.card3_replay_counter.position > 0 or s.game.card4_replay_counter.position > 0 or s.game.card5_replay_counter.position > 0 or s.game.card6_replay_counter.position > 0:
            if s.game.card1_replay_counter.position > 0 and s.game.card1_double.status == False:
                position = [70,312]
                screen.blit(c, position)
            if s.game.card2_replay_counter.position > 0 and s.game.card2_double.status == False:
                position = [308,310]
                screen.blit(c, position)
            if s.game.card3_replay_counter.position > 0 and s.game.card3_double.status == False:
                position = [548,312]
                screen.blit(c, position)
            if s.game.card4_replay_counter.position > 0 and s.game.card4_double.status == False:
                position = [70,820]
                screen.blit(c, position)
            if s.game.card5_replay_counter.position > 0 and s.game.card5_double.status == False:
                position = [311,808]
                screen.blit(c, position)
            if s.game.card6_replay_counter.position > 0 and s.game.card6_double.status == False:
                position = [548,814]
                screen.blit(c, position)

        if s.game.card1_double.status == True:
            position = [92,347]
            screen.blit(d, position)
        if s.game.card2_double.status == True:
            position = [331,345]
            screen.blit(d, position)
        if s.game.card3_double.status == True:
            position = [571,347]
            screen.blit(d, position)
        if s.game.card4_double.status == True:
            position = [94,856]
            screen.blit(d, position)
        if s.game.card5_double.status == True:
            position = [334,842]
            screen.blit(d, position)
        if s.game.card6_double.status == True:
            position = [572,849]
            screen.blit(d, position)

        if s.game.card1_missed.status == True:
            position = [145,347]
            screen.blit(n, position)
        if s.game.card2_missed.status == True:
            position = [384,345]
            screen.blit(n, position)
        if s.game.card3_missed.status == True:
            position = [625,347]
            screen.blit(n, position)
        if s.game.card4_missed.status == True:
            position = [146,856]
            screen.blit(n, position)
        if s.game.card5_missed.status == True:
            position = [388,842]
            screen.blit(n, position)
        if s.game.card6_missed.status == True:
            position = [622,849]
            screen.blit(n, position)

    if s.game.tilt.status == True:
        position = [274,720]
        screen.blit(tilt, position)

    pygame.display.update()

def blink_double(s):
    dirty_rects = []
    s.game.blink = not s.game.blink
    if s.game.blink == 1:
        blink_pos = [218,569]
        dirty_rects.append(screen.blit(blink_image, blink_pos))
        pygame.display.update(dirty_rects)
    else:
        dirty_rects.append(screen.blit(bg_gi, (218,569), pygame.Rect(218,569,109,69)))
        pygame.display.update(dirty_rects)
