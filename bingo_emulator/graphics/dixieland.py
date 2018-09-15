
import pygame

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

meter = pygame.image.load('graphics/assets/black_register_cover.png').convert()
card = pygame.image.load('dixieland/assets/card.png').convert_alpha()
number = pygame.image.load('dixieland/assets/number.png').convert_alpha()
red_diagonal = pygame.image.load('dixieland/assets/red_diagonal.png').convert_alpha()
feature = pygame.image.load('dixieland/assets/feature.png').convert_alpha()
magic_number = pygame.image.load('dixieland/assets/magic_number.png').convert_alpha()
all_double = pygame.image.load('dixieland/assets/all_double.png').convert_alpha()
eleventh_coin = pygame.image.load('dixieland/assets/eleventh_coin.png').convert_alpha()
dd_card = pygame.image.load('dixieland/assets/dd_card.png').convert_alpha()
corners = pygame.image.load('dixieland/assets/corners.png').convert_alpha()
super_line = pygame.image.load('dixieland/assets/super_line.png').convert_alpha()
c = pygame.image.load('dixieland/assets/regular.png').convert_alpha()
d = pygame.image.load('dixieland/assets/double.png').convert_alpha()
n = pygame.image.load('dixieland/assets/nothing.png').convert_alpha()
tilt = pygame.image.load('dixieland/assets/tilt.png').convert_alpha()
blink_image = pygame.image.load('dixieland/assets/double_or_nothing.png').convert_alpha()
bg_menu = pygame.image.load('dixieland/assets/dixieland_menu.png')
bg_gi = pygame.image.load('dixieland/assets/dixieland_gi.png')
bg_off = pygame.image.load('dixieland/assets/dixieland_off.png')

class scorereel():
    """ Score Reels are used to count replays """
    def __init__(self, pos, image):
        self.position = pos
        self.default_y = self.position[1]
        self.image = pygame.image.load(image).convert()

reel1 = scorereel([288,653], "graphics/assets/white_reel.png")
reel10 = scorereel([269,653], "graphics/assets/white_reel.png")
reel100 = scorereel([250,653], "graphics/assets/white_reel.png")
reel1000 = scorereel([230,653], "graphics/assets/white_reel.png")

def display(s, replays=0, menu=False):
    
    meter.set_colorkey((255,0,252))
    meter_position = [221,653]

    screen.blit(reel1.image, reel1.position)
    screen.blit(reel10.image, reel10.position)
    screen.blit(reel100.image, reel100.position)
    screen.blit(reel1000.image, reel1000.position)
    screen.blit(meter, meter_position)

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
        position = [7,281]
        screen.blit(card, position)
    if s.game.selector.position >= 2:
        position = [243,277]
        screen.blit(card, position)
    if s.game.selector.position >= 3:
        position = [489,279]
        screen.blit(card, position)
    if s.game.selector.position >= 4:
        position = [4,780]
        screen.blit(card, position)
    if s.game.selector.position >= 5:
        position = [245,771]
        screen.blit(card, position)
    if s.game.selector.position >= 6:
        position = [491,779]
        screen.blit(card, position)

    if s.game.tilt.status == False:
        if s.holes:
            if 1 in s.holes:
                position = [77,377]
                screen.blit(number, position)
                position = [283,486]
                screen.blit(number, position)
                position = [680,379]
                screen.blit(number, position)
                position = [157,1021]
                screen.blit(number, position)
                position = [361,871]
                screen.blit(number, position)
                position = [529,1019]
                screen.blit(number, position)
            if 2 in s.holes:
                position = [113,522]
                screen.blit(number, position)
                position = [284,448]
                screen.blit(number, position)
                position = [682,416]
                screen.blit(number, position)
                position = [193,952]
                screen.blit(number, position)
                position = [398,1013]
                screen.blit(number, position)
                position = [531,913]
                screen.blit(number, position)
            if 3 in s.holes:
                position = [190,375]
                screen.blit(number, position)
                position = [436,523]
                screen.blit(number, position)
                position = [606,378]
                screen.blit(number, position)
                position = [45,879]
                screen.blit(number, position)
                position = [362,907]
                screen.blit(number, position)
                position = [639,1018]
                screen.blit(number, position)
            if 4 in s.holes:
                position = [151,523]
                screen.blit(number, position)
                position = [398,376]
                screen.blit(number, position)
                position = [645,526]
                screen.blit(number, position)
                position = [155,882]
                screen.blit(number, position)
                position = [286,871]
                screen.blit(number, position)
                position = [679,876]
                screen.blit(number, position)
            if 5 in s.holes:
                position = [42,377]
                screen.blit(number, position)
                position = [360,524]
                screen.blit(number, position)
                position = [532,451]
                screen.blit(number, position)
                position = [194,1022]
                screen.blit(number, position)
                position = [437,872]
                screen.blit(number, position)
                position = [678,946]
                screen.blit(number, position)
            if 6 in s.holes:
                position = [41,450]
                screen.blit(number, position)
                position = [435,376]
                screen.blit(number, position)
                position = [532,378]
                screen.blit(number, position)
                position = [49,1018]
                screen.blit(number, position)
                position = [324,871]
                screen.blit(number, position)
                position = [675,1015]
                screen.blit(number, position)
            if 7 in s.holes:
                position = [190,412]
                screen.blit(number, position)
                position = [321,524]
                screen.blit(number, position)
                position = [570,378]
                screen.blit(number, position)
                position = [81,880]
                screen.blit(number, position)
                position = [287,1013]
                screen.blit(number, position)
                position = [566,1019]
                screen.blit(number, position)
            if 8 in s.holes:
                position = [41,413]
                screen.blit(number, position)
                position = [436,486]
                screen.blit(number, position)
                position = [682,526]
                screen.blit(number, position)
                position = [192,917]
                screen.blit(number, position)
                position = [437,979]
                screen.blit(number, position)
                position = [531,878]
                screen.blit(number, position)
            if 9 in s.holes:
                position = [114,376]
                screen.blit(number, position)
                position = [283,375]
                screen.blit(number, position)
                position = [608,488]
                screen.blit(number, position)
                position = [192,882]
                screen.blit(number, position)
                position = [286,942]
                screen.blit(number, position)
                position = [603,982]
                screen.blit(number, position)
            if 10 in s.holes:
                position = [114,412]
                screen.blit(number, position)
                position = [283,523]
                screen.blit(number, position)
                position = [533,525]
                screen.blit(number, position)
                position = [117,881]
                screen.blit(number, position)
                position = [287,978]
                screen.blit(number, position)
                position = [605,877]
                screen.blit(number, position)
            if 11 in s.holes:
                position = [151,449]
                screen.blit(number, position)
                position = [360,486]
                screen.blit(number, position)
                position = [533,489]
                screen.blit(number, position)
                position = [156,952]
                screen.blit(number, position)
                position = [435,1013]
                screen.blit(number, position)
                position = [676,981]
                screen.blit(number, position)
            if 12 in s.holes:
                position = [40,523]
                screen.blit(number, position)
                position = [398,448]
                screen.blit(number, position)
                position = [607,415]
                screen.blit(number, position)
                position = [120,986]
                screen.blit(number, position)
                position = [398,943]
                screen.blit(number, position)
                position = [567,948]
                screen.blit(number, position)
            if 13 in s.holes:
                position = [189,486]
                screen.blit(number, position)
                position = [283,411]
                screen.blit(number, position)
                position = [570,526]
                screen.blit(number, position)
                position = [48,983]
                screen.blit(number, position)
                position = [437,908]
                screen.blit(number, position)
                position = [642,876]
                screen.blit(number, position)
            if 14 in s.holes:
                position = [113,486]
                screen.blit(number, position)
                position = [359,412]
                screen.blit(number, position)
                position = [570,414]
                screen.blit(number, position)
                position = [83,950]
                screen.blit(number, position)
                position = [399,979]
                screen.blit(number, position)
                position = [641,911]
                screen.blit(number, position)
            if 15 in s.holes:
                position = [189,523]
                screen.blit(number, position)
                position = [360,448]
                screen.blit(number, position)
                position = [644,488]
                screen.blit(number, position)
                position = [46,948]
                screen.blit(number, position)
                position = [323,906]
                screen.blit(number, position)
                position = [567,983]
                screen.blit(number, position)
            if 16 in s.holes:
                position = [114,449]
                screen.blit(number, position)
                position = [359,375]
                screen.blit(number, position)
                position = [644,451]
                screen.blit(number, position)
                position = [121,1020]
                screen.blit(number, position)
                position = [361,978]
                screen.blit(number, position)
                position = [605,912]
                screen.blit(number, position)
            if 17 in s.holes:
                position = [189,448]
                screen.blit(number, position)
                position = [437,449]
                screen.blit(number, position)
                position = [570,488]
                screen.blit(number, position)
                position = [119,950]
                screen.blit(number, position)
                position = [399,907]
                screen.blit(number, position)
                position = [567,912]
                screen.blit(number, position)
            if 18 in s.holes:
                position = [78,450]
                screen.blit(number, position)
                position = [322,449]
                screen.blit(number, position)
                position = [644,415]
                screen.blit(number, position)
                position = [118,916]
                screen.blit(number, position)
                position = [325,978]
                screen.blit(number, position)
                position = [640,983]
                screen.blit(number, position)
            if 19 in s.holes:
                position = [152,412]
                screen.blit(number, position)
                position = [321,411]
                screen.blit(number, position)
                position = [570,451]
                screen.blit(number, position)
                position = [157,988]
                screen.blit(number, position)
                position = [324,942]
                screen.blit(number, position)
                position = [641,947]
                screen.blit(number, position)
            if 20 in s.holes:
                position = [151,487]
                screen.blit(number, position)
                position = [398,411]
                screen.blit(number, position)
                position = [607,452]
                screen.blit(number, position)
                position = [85,985]
                screen.blit(number, position)
                position = [437,943]
                screen.blit(number, position)
                position = [530,948]
                screen.blit(number, position)
            if 21 in s.holes:
                position = [77,485]
                screen.blit(number, position)
                position = [398,487]
                screen.blit(number, position)
                position = [607,526]
                screen.blit(number, position)
                position = [82,915]
                screen.blit(number, position)
                position = [361,943]
                screen.blit(number, position)
                position = [602,1017]
                screen.blit(number, position)
            if 22 in s.holes:
                position = [77,412]
                screen.blit(number, position)
                position = [322,486]
                screen.blit(number, position)
                position = [681,452]
                screen.blit(number, position)
                position = [155,916]
                screen.blit(number, position)
                position = [361,1012]
                screen.blit(number, position)
                position = [604,947]
                screen.blit(number, position)
            if 23 in s.holes:
                position = [77,524]
                screen.blit(number, position)
                position = [398,524]
                screen.blit(number, position)
                position = [532,414]
                screen.blit(number, position)
                position = [194,988]
                screen.blit(number, position)
                position = [399,873]
                screen.blit(number, position)
                position = [569,878]
                screen.blit(number, position)
            if 24 in s.holes:
                position = [40,487]
                screen.blit(number, position)
                position = [322,376]
                screen.blit(number, position)
                position = [644,379]
                screen.blit(number, position)
                position = [46,914]
                screen.blit(number, position)
                position = [324,1014]
                screen.blit(number, position)
                position = [679,912]
                screen.blit(number, position)
            if 25 in s.holes:
                position = [152,376]
                screen.blit(number, position)
                position = [436,412]
                screen.blit(number, position)
                position = [682,490]
                screen.blit(number, position)
                position = [85,1019]
                screen.blit(number, position)
                position = [286,907]
                screen.blit(number, position)
                position = [530,985]
                screen.blit(number, position)

        if s.game.selector.position > 6:
            p = [2,373]
            screen.blit(red_diagonal, p)
            p = [243,370]
            screen.blit(red_diagonal, p)
            p = [491,372]
            screen.blit(red_diagonal, p)
            p = [22,592]
            screen.blit(feature, p)

        if s.game.selector.position > 7:
            p = [7,872]
            screen.blit(red_diagonal, p)
            p = [245,865]
            screen.blit(red_diagonal, p)
            p = [491,873]
            screen.blit(red_diagonal, p)
            p = [23,650]
            screen.blit(feature, p)

        if s.game.selector.position > 8:
            p = [371,576]
            screen.blit(feature, p)
            p = [398,731]
            screen.blit(magic_number, p)

        if s.game.selector.position > 9:
            p = [371,635]
            screen.blit(feature, p)

        if 1 in s.game.magic:
            p = [366,730]
            screen.blit(number, p)
        if 7 in s.game.magic:
            p = [389,699]
            screen.blit(number, p)
        if 9 in s.game.magic:
            p = [430,694]
            screen.blit(number, p)
        if 22 in s.game.magic:
            p = [469,699]
            screen.blit(number, p)
        if 25 in s.game.magic:
            p = [492,731]
            screen.blit(number, p)

        if s.game.onetwothree.status == True:
            if s.game.dd1.status == True:
                p = [119,279]
                screen.blit(all_double, p)
            else:
                p = [119,312]
                screen.blit(all_double, p)

            if s.game.dd2.status == True:
                p = [361,277]
                screen.blit(all_double, p)
            else:
                p = [362,311]
                screen.blit(all_double, p)

            if s.game.dd3.status == True:
                p = [605,281]
                screen.blit(all_double, p)
            else:
                p = [606,314]
                screen.blit(all_double, p)


        if s.game.fourfivesix.status == True:
            if s.game.dd4.status == True:
                p = [118,783]
                screen.blit(all_double, p)
            else:
                p = [119,817]
                screen.blit(all_double, p)
            if s.game.dd5.status == True:
                p = [362,772]
                screen.blit(all_double, p)
            else:
                p = [363,807]
                screen.blit(all_double, p)
            if s.game.dd6.status == True:
                p = [608,778]
                screen.blit(all_double, p)
            else:
                p = [608,813]
                screen.blit(all_double, p)

        if s.game.selector.position >= 11:
            p = [559,577]
            screen.blit(eleventh_coin, p)
            p = [554,707]
            screen.blit(feature, p)

        if s.game.dd1.status == True:
            p = [546,636]
            screen.blit(dd_card, p)
        if s.game.dd2.status == True:
            p = [605,636]
            screen.blit(dd_card, p)
        if s.game.dd3.status == True:
            p = [665,636]
            screen.blit(dd_card, p)
        if s.game.dd4.status == True:
            p = [546,681]
            screen.blit(dd_card, p)
        if s.game.dd5.status == True:
            p = [605,681]
            screen.blit(dd_card, p)
        if s.game.dd6.status == True:
            p = [665,681]
            screen.blit(dd_card, p)

        if s.game.corners1.status == True:
            position = [5,316]
            screen.blit(corners, position)
        if s.game.corners2.status == True:
            position = [245,312]
            screen.blit(corners, position)
        if s.game.corners3.status == True:
            position = [492,313]
            screen.blit(corners, position)
        if s.game.corners4.status == True:
            position = [6,815]
            screen.blit(corners, position)
        if s.game.corners5.status == True:
            position = [246,806]
            screen.blit(corners, position)
        if s.game.corners6.status == True:
            position = [492,814]
            screen.blit(corners, position)

        if s.game.super1.status == True:
            position = [3,481]
            screen.blit(super_line, position)
        if s.game.super2.status == True:
            position = [244,480]
            screen.blit(super_line, position)
        if s.game.super3.status == True:
            position = [493,482]
            screen.blit(super_line, position)
        if s.game.super4.status == True:
            position = [11,976]
            screen.blit(super_line, position)
        if s.game.super5.status == True:
            position = [248,971]
            screen.blit(super_line, position)
        if s.game.super6.status == True:
            position = [492,979]
            screen.blit(super_line, position)

        if s.game.card1_replay_counter.position > 0 or s.game.card2_replay_counter.position > 0 or s.game.card3_replay_counter.position > 0 or s.game.card4_replay_counter.position > 0 or s.game.card5_replay_counter.position > 0 or s.game.card6_replay_counter.position > 0:
            if s.game.card1_replay_counter.position > 0 and s.game.card1_double.status == False:
                position = [67,317]
                screen.blit(c, position)
            if s.game.card2_replay_counter.position > 0 and s.game.card2_double.status == False:
                position = [309,314]
                screen.blit(c, position)
            if s.game.card3_replay_counter.position > 0 and s.game.card3_double.status == False:
                position = [554,316]
                screen.blit(c, position)
            if s.game.card4_replay_counter.position > 0 and s.game.card4_double.status == False:
                position = [67,819]
                screen.blit(c, position)
            if s.game.card5_replay_counter.position > 0 and s.game.card5_double.status == False:
                position = [309,809]
                screen.blit(c, position)
            if s.game.card6_replay_counter.position > 0 and s.game.card6_double.status == False:
                position = [555,816]
                screen.blit(c, position)

        if s.game.card1_double.status == True:
            position = [89,351]
            screen.blit(d, position)
        if s.game.card2_double.status == True:
            position = [333,349]
            screen.blit(d, position)
        if s.game.card3_double.status == True:
            position = [580,352]
            screen.blit(d, position)
        if s.game.card4_double.status == True:
            position = [90,854]
            screen.blit(d, position)
        if s.game.card5_double.status == True:
            position = [333,845]
            screen.blit(d, position)
        if s.game.card6_double.status == True:
            position = [580,851]
            screen.blit(d, position)

        if s.game.card1_missed.status == True:
            position = [142,351]
            screen.blit(n, position)
        if s.game.card2_missed.status == True:
            position = [386,349]
            screen.blit(n, position)
        if s.game.card3_missed.status == True:
            position = [635,353]
            screen.blit(n, position)
        if s.game.card4_missed.status == True:
            position = [143,856]
            screen.blit(n, position)
        if s.game.card5_missed.status == True:
            position = [390,845]
            screen.blit(n, position)
        if s.game.card6_missed.status == True:
            position = [633,850]
            screen.blit(n, position)

    if s.game.tilt.status == True:
        position = [251,720]
        screen.blit(tilt, position)

    pygame.display.update()

def blink_double(s):
    dirty_rects = []
    s.game.blink = not s.game.blink
    if s.game.blink == 1:
        blink_pos = [217,567]
        dirty_rects.append(screen.blit(blink_image, blink_pos))
        pygame.display.update(dirty_rects)
    else:
        dirty_rects.append(screen.blit(bg_gi, (217,567), pygame.Rect(217,567,109,69)))
        pygame.display.update(dirty_rects)

