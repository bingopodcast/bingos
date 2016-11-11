
import pygame

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

meter = pygame.image.load('graphics/assets/black_register_cover.png').convert()
card = pygame.image.load('nashville/assets/card.png').convert_alpha()
number = pygame.image.load('nashville/assets/number.png').convert_alpha()
red_diagonal = pygame.image.load('nashville/assets/red_diagonal.png').convert_alpha()
feature = pygame.image.load('nashville/assets/feature.png').convert_alpha()
magic_number = pygame.image.load('nashville/assets/magic_number.png').convert_alpha()
all_double = pygame.image.load('nashville/assets/all_double.png').convert_alpha()
corners = pygame.image.load('nashville/assets/corners.png').convert_alpha()
super_line = pygame.image.load('nashville/assets/super_line.png').convert_alpha()
c = pygame.image.load('nashville/assets/regular.png').convert_alpha()
d = pygame.image.load('nashville/assets/double.png').convert_alpha()
n = pygame.image.load('nashville/assets/nothing.png').convert_alpha()
tilt = pygame.image.load('nashville/assets/tilt.png').convert_alpha()
blink_image = pygame.image.load('nashville/assets/double_or_nothing.png').convert_alpha()

class scorereel():
    """ Score Reels are used to count replays """
    def __init__(self, pos, image):
        self.position = pos
        self.default_y = self.position[1]
        self.image = pygame.image.load(image).convert()

reel1 = scorereel([288,648], "graphics/assets/white_reel.png")
reel10 = scorereel([269,648], "graphics/assets/white_reel.png")
reel100 = scorereel([250,648], "graphics/assets/white_reel.png")
reel1000 = scorereel([230,648], "graphics/assets/white_reel.png")

def display(s, replays=0, menu=False):
    
    meter.set_colorkey((255,0,252))
    meter_position = [221,648]

    screen.blit(reel1.image, reel1.position)
    screen.blit(reel10.image, reel10.position)
    screen.blit(reel100.image, reel100.position)
    screen.blit(reel1000.image, reel1000.position)
    screen.blit(meter, meter_position)

    backglass_position = [0, 0]
    backglass = pygame.Surface((720,1280), pygame.SRCALPHA | pygame.FULLSCREEN)
    backglass.fill((0, 0, 0))
    if menu == True:
        backglass = pygame.image.load('nashville/assets/nashville_menu.png')
    else:
        if (s.game.anti_cheat.status == True):
            backglass = pygame.image.load('nashville/assets/nashville_gi.png')
        else:
            backglass = pygame.image.load('nashville/assets/nashville_off.png')
    #backglass = pygame.transform.scale(backglass, (1280,720))
    screen.blit(backglass, backglass_position)

    if s.game.selector.position >= 1:
        position = [10,245]
        screen.blit(card, position)
    if s.game.selector.position >= 2:
        position = [251,229]
        screen.blit(card, position)
    if s.game.selector.position >= 3:
        position = [487,215]
        screen.blit(card, position)
    if s.game.selector.position >= 4:
        position = [13,793]
        screen.blit(card, position)
    if s.game.selector.position >= 5:
        position = [249,780]
        screen.blit(card, position)
    if s.game.selector.position >= 6:
        position = [490,765]
        screen.blit(card, position)

    if s.game.tilt.status == False:
        if s.holes:
            if 1 in s.holes:
                position = [86,355]
                screen.blit(number, position)
                position = [288,464]
                screen.blit(number, position)
                position = [669,328]
                screen.blit(number, position)
                position = [162,1068]
                screen.blit(number, position)
                position = [362,892]
                screen.blit(number, position)
                position = [527,1038]
                screen.blit(number, position)
            if 2 in s.holes:
                position = [121,518]
                screen.blit(number, position)
                position = [288,422]
                screen.blit(number, position)
                position = [671,368]
                screen.blit(number, position)
                position = [198,988]
                screen.blit(number, position)
                position = [398,1053]
                screen.blit(number, position)
                position = [528,918]
                screen.blit(number, position)
            if 3 in s.holes:
                position = [195,355]
                screen.blit(number, position)
                position = [435,503]
                screen.blit(number, position)
                position = [598,327]
                screen.blit(number, position)
                position = [52,907]
                screen.blit(number, position)
                position = [362,933]
                screen.blit(number, position)
                position = [634,1035]
                screen.blit(number, position)
            if 4 in s.holes:
                position = [158,518]
                screen.blit(number, position)
                position = [397,341]
                screen.blit(number, position)
                position = [636,488]
                screen.blit(number, position)
                position = [159,907]
                screen.blit(number, position)
                position = [288,893]
                screen.blit(number, position)
                position = [671,875]
                screen.blit(number, position)
            if 5 in s.holes:
                position = [50,357]
                screen.blit(number, position)
                position = [362,504]
                screen.blit(number, position)
                position = [528,407]
                screen.blit(number, position)
                position = [198,1068]
                screen.blit(number, position)
                position = [435,892]
                screen.blit(number, position)
                position = [670,955]
                screen.blit(number, position)
            if 6 in s.holes:
                position = [50,438]
                screen.blit(number, position)
                position = [434,341]
                screen.blit(number, position)
                position = [526,326]
                screen.blit(number, position)
                position = [55,1067]
                screen.blit(number, position)
                position = [325,893]
                screen.blit(number, position)
                position = [670,1036]
                screen.blit(number, position)
            if 7 in s.holes:
                position = [195,397]
                screen.blit(number, position)
                position = [324,505]
                screen.blit(number, position)
                position = [562,327]
                screen.blit(number, position)
                position = [87,907]
                screen.blit(number, position)
                position = [290,1055]
                screen.blit(number, position)
                position = [563,1038]
                screen.blit(number, position)
            if 8 in s.holes:
                position = [50,398]
                screen.blit(number, position)
                position = [436,463]
                screen.blit(number, position)
                position = [671,490]
                screen.blit(number, position)
                position = [197,948]
                screen.blit(number, position)
                position = [435,1014]
                screen.blit(number, position)
                position = [528,877]
                screen.blit(number, position)
            if 9 in s.holes:
                position = [122,356]
                screen.blit(number, position)
                position = [288,341]
                screen.blit(number, position)
                position = [600,448]
                screen.blit(number, position)
                position = [195,909]
                screen.blit(number, position)
                position = [289,974]
                screen.blit(number, position)
                position = [598,996]
                screen.blit(number, position)
            if 10 in s.holes:
                position = [122,396]
                screen.blit(number, position)
                position = [288,505]
                screen.blit(number, position)
                position = [529,489]
                screen.blit(number, position)
                position = [124,907]
                screen.blit(number, position)
                position = [289,1015]
                screen.blit(number, position)
                position = [599,877]
                screen.blit(number, position)
            if 11 in s.holes:
                position = [158,437]
                screen.blit(number, position)
                position = [361,463]
                screen.blit(number, position)
                position = [528,448]
                screen.blit(number, position)
                position = [161,988]
                screen.blit(number, position)
                position = [435,1054]
                screen.blit(number, position)
                position = [670,995]
                screen.blit(number, position)
            if 12 in s.holes:
                position = [50,520]
                screen.blit(number, position)
                position = [398,422]
                screen.blit(number, position)
                position = [599,367]
                screen.blit(number, position)
                position = [126,1028]
                screen.blit(number, position)
                position = [398,973]
                screen.blit(number, position)
                position = [562,957]
                screen.blit(number, position)
            if 13 in s.holes:
                position = [195,478]
                screen.blit(number, position)
                position = [287,381]
                screen.blit(number, position)
                position = [564,489]
                screen.blit(number, position)
                position = [54,1028]
                screen.blit(number, position)
                position = [435,934]
                screen.blit(number, position)
                position = [635,876]
                screen.blit(number, position)
            if 14 in s.holes:
                position = [121,479]
                screen.blit(number, position)
                position = [361,381]
                screen.blit(number, position)
                position = [562,366]
                screen.blit(number, position)
                position = [88,987]
                screen.blit(number, position)
                position = [398,1014]
                screen.blit(number, position)
                position = [635,915]
                screen.blit(number, position)
            if 15 in s.holes:
                position = [194,519]
                screen.blit(number, position)
                position = [361,421]
                screen.blit(number, position)
                position = [635,448]
                screen.blit(number, position)
                position = [53,986]
                screen.blit(number, position)
                position = [324,932]
                screen.blit(number, position)
                position = [563,998]
                screen.blit(number, position)
            if 16 in s.holes:
                position = [121,436]
                screen.blit(number, position)
                position = [361,340]
                screen.blit(number, position)
                position = [635,407]
                screen.blit(number, position)
                position = [126,1067]
                screen.blit(number, position)
                position = [362,1013]
                screen.blit(number, position)
                position = [599,916]
                screen.blit(number, position)
            if 17 in s.holes:
                position = [195,437]
                screen.blit(number, position)
                position = [435,422]
                screen.blit(number, position)
                position = [564,447]
                screen.blit(number, position)
                position = [125,987]
                screen.blit(number, position)
                position = [398,932]
                screen.blit(number, position)
                position = [563,916]
                screen.blit(number, position)
            if 18 in s.holes:
                position = [86,437]
                screen.blit(number, position)
                position = [324,421]
                screen.blit(number, position)
                position = [635,367]
                screen.blit(number, position)
                position = [124,947]
                screen.blit(number, position)
                position = [326,1015]
                screen.blit(number, position)
                position = [635,997]
                screen.blit(number, position)
            if 19 in s.holes:
                position = [158,396]
                screen.blit(number, position)
                position = [324,380]
                screen.blit(number, position)
                position = [564,407]
                screen.blit(number, position)
                position = [162,1029]
                screen.blit(number, position)
                position = [325,973]
                screen.blit(number, position)
                position = [635,956]
                screen.blit(number, position)
            if 20 in s.holes:
                position = [158,478]
                screen.blit(number, position)
                position = [398,382]
                screen.blit(number, position)
                position = [600,408]
                screen.blit(number, position)
                position = [90,1027]
                screen.blit(number, position)
                position = [435,973]
                screen.blit(number, position)
                position = [528,958]
                screen.blit(number, position)
            if 21 in s.holes:
                position = [86,479]
                screen.blit(number, position)
                position = [399,464]
                screen.blit(number, position)
                position = [601,489]
                screen.blit(number, position)
                position = [88,947]
                screen.blit(number, position)
                position = [362,974]
                screen.blit(number, position)
                position = [598,1037]
                screen.blit(number, position)
            if 22 in s.holes:
                position = [85,396]
                screen.blit(number, position)
                position = [325,463]
                screen.blit(number, position)
                position = [671,408]
                screen.blit(number, position)
                position = [160,947]
                screen.blit(number, position)
                position = [362,1053]
                screen.blit(number, position)
                position = [599,957]
                screen.blit(number, position)
            if 23 in s.holes:
                position = [86,520]
                screen.blit(number, position)
                position = [399,504]
                screen.blit(number, position)
                position = [527,366]
                screen.blit(number, position)
                position = [198,1029]
                screen.blit(number, position)
                position = [398,893]
                screen.blit(number, position)
                position = [563,877]
                screen.blit(number, position)
            if 24 in s.holes:
                position = [50,480]
                screen.blit(number, position)
                position = [323,341]
                screen.blit(number, position)
                position = [633,328]
                screen.blit(number, position)
                position = [53,947]
                screen.blit(number, position)
                position = [325,1054]
                screen.blit(number, position)
                position = [671,916]
                screen.blit(number, position)
            if 25 in s.holes:
                position = [158,356]
                screen.blit(number, position)
                position = [435,382]
                screen.blit(number, position)
                position = [672,449]
                screen.blit(number, position)
                position = [90,1067]
                screen.blit(number, position)
                position = [288,933]
                screen.blit(number, position)
                position = [527,999]
                screen.blit(number, position)

        if s.game.selector.position > 6:
            p = [13,351]
            screen.blit(red_diagonal, p)
            p = [250,335]
            screen.blit(red_diagonal, p)
            p = [489,320]
            screen.blit(red_diagonal, p)
            p = [14,605]
            screen.blit(feature, p)

        if s.game.selector.position > 7:
            p = [14,898]
            screen.blit(red_diagonal, p)
            p = [249,886]
            screen.blit(red_diagonal, p)
            p = [489,870]
            screen.blit(red_diagonal, p)
            p = [15,688]
            screen.blit(feature, p)

        if s.game.selector.position > 8:
            p = [539,550]
            screen.blit(feature, p)
            p = [576,730]
            screen.blit(magic_number, p)

        if s.game.selector.position > 9:
            p = [538,623]
            screen.blit(feature, p)

        if 1 in s.game.magic:
            p = [537,719]
            screen.blit(number, p)
        if 7 in s.game.magic:
            p = [568,692]
            screen.blit(number, p)
        if 9 in s.game.magic:
            p = [607,689]
            screen.blit(number, p)
        if 22 in s.game.magic:
            p = [646,692]
            screen.blit(number, p)
        if 25 in s.game.magic:
            p = [678,719]
            screen.blit(number, p)

        if s.game.onetwothree.status == True:
            p = [125,241]
            screen.blit(all_double, p)
            p = [363,230]
            screen.blit(all_double, p)
            p = [599,216]
            screen.blit(all_double, p)
        
        if s.game.fourfivesix.status == True:
            p = [124,792]
            screen.blit(all_double, p)
            p = [364,778]
            screen.blit(all_double, p)
            p = [603,762]
            screen.blit(all_double, p)

        if s.game.corners1.status == True:
            position = [14,282]
            screen.blit(corners, position)
        if s.game.corners2.status == True:
            position = [249,264]
            screen.blit(corners, position)
        if s.game.corners3.status == True:
            position = [487,249]
            screen.blit(corners, position)
        if s.game.corners4.status == True:
            position = [13,829]
            screen.blit(corners, position)
        if s.game.corners5.status == True:
            position = [249,816]
            screen.blit(corners, position)
        if s.game.corners6.status == True:
            position = [490,801]
            screen.blit(corners, position)

        if s.game.super1.status == True:
            position = [13,475]
            screen.blit(super_line, position)
        if s.game.super2.status == True:
            position = [250,458]
            screen.blit(super_line, position)
        if s.game.super3.status == True:
            position = [490,443]
            screen.blit(super_line, position)
        if s.game.super4.status == True:
            position = [17,1021]
            screen.blit(super_line, position)
        if s.game.super5.status == True:
            position = [251,1009]
            screen.blit(super_line, position)
        if s.game.super6.status == True:
            position = [490,993]
            screen.blit(super_line, position)

        if s.game.card1_replay_counter.position > 0 or s.game.card2_replay_counter.position > 0 or s.game.card3_replay_counter.position > 0 or s.game.card4_replay_counter.position > 0 or s.game.card5_replay_counter.position > 0 or s.game.card6_replay_counter.position > 0:
            if s.game.card1_replay_counter.position > 0 and s.game.card1_double.status == False:
                position = [71,306]
                screen.blit(c, position)
            if s.game.card2_replay_counter.position > 0 and s.game.card2_double.status == False:
                position = [309,290]
                screen.blit(c, position)
            if s.game.card3_replay_counter.position > 0 and s.game.card3_double.status == False:
                position = [547,275]
                screen.blit(c, position)
            if s.game.card4_replay_counter.position > 0 and s.game.card4_double.status == False:
                position = [72,856]
                screen.blit(c, position)
            if s.game.card5_replay_counter.position > 0 and s.game.card5_double.status == False:
                position = [310,843]
                screen.blit(c, position)
            if s.game.card6_replay_counter.position > 0 and s.game.card6_double.status == False:
                position = [549,826]
                screen.blit(c, position)

        if s.game.card1_double.status == True:
            position = [122,307]
            screen.blit(d, position)
        if s.game.card2_double.status == True:
            position = [359,291]
            screen.blit(d, position)
        if s.game.card3_double.status == True:
            position = [597,279]
            screen.blit(d, position)
        if s.game.card4_double.status == True:
            position = [123,858]
            screen.blit(d, position)
        if s.game.card5_double.status == True:
            position = [360,843]
            screen.blit(d, position)
        if s.game.card6_double.status == True:
            position = [599,827]
            screen.blit(d, position)

        if s.game.card1_missed.status == True:
            position = [174,306]
            screen.blit(n, position)
        if s.game.card2_missed.status == True:
            position = [414,291]
            screen.blit(n, position)
        if s.game.card3_missed.status == True:
            position = [648,280]
            screen.blit(n, position)
        if s.game.card4_missed.status == True:
            position = [177,859]
            screen.blit(n, position)
        if s.game.card5_missed.status == True:
            position = [415,843]
            screen.blit(n, position)
        if s.game.card6_missed.status == True:
            position = [652,826]
            screen.blit(n, position)

    if s.game.tilt.status == True:
        position = [403,576]
        screen.blit(tilt, position)

    pygame.display.update()

def blink_double(s):
    s.game.blink = not s.game.blink
    if s.game.blink == 1:
        blink_pos = [361,640]
        screen.blit(blink_image, blink_pos)
        pygame.display.update()
    else:
        display(s)
