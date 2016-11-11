
import pygame

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

meter = pygame.image.load('graphics/assets/black_register_cover.png').convert()
card = pygame.image.load('mississippi_showboat/assets/card.png').convert_alpha()
number = pygame.image.load('mississippi_showboat/assets/number.png').convert_alpha()
ball = pygame.image.load('mississippi_showboat/assets/ball.png').convert_alpha()
red_diagonal = pygame.image.load('mississippi_showboat/assets/red_diagonal.png').convert_alpha()
feature = pygame.image.load('mississippi_showboat/assets/feature.png').convert_alpha()
magic_number = pygame.image.load('mississippi_showboat/assets/magic_number.png').convert_alpha()
all_double = pygame.image.load('mississippi_showboat/assets/all_double.png').convert_alpha()
all_dd = pygame.image.load('mississippi_showboat/assets/all_dd.png').convert_alpha()
double_double = pygame.image.load('mississippi_showboat/assets/double_double.png').convert_alpha()
corners = pygame.image.load('mississippi_showboat/assets/corners.png').convert_alpha()
super_line = pygame.image.load('mississippi_showboat/assets/super_line.png').convert_alpha()
c = pygame.image.load('mississippi_showboat/assets/regular.png').convert_alpha()
d = pygame.image.load('mississippi_showboat/assets/double.png').convert_alpha()
n = pygame.image.load('mississippi_showboat/assets/nothing.png').convert_alpha()
tilt = pygame.image.load('mississippi_showboat/assets/tilt.png').convert_alpha()
blink_image = pygame.image.load('mississippi_showboat/assets/double_or_nothing.png').convert_alpha()

class scorereel():
    """ Score Reels are used to count replays """
    def __init__(self, pos, image):
        self.position = pos
        self.default_y = self.position[1]
        self.image = pygame.image.load(image).convert()

reel1 = scorereel([280,663], "graphics/assets/white_reel.png")
reel10 = scorereel([261,663], "graphics/assets/white_reel.png")
reel100 = scorereel([242,663], "graphics/assets/white_reel.png")
reel1000 = scorereel([223,663], "graphics/assets/white_reel.png")

def display(s, replays=0, menu=False):
    
    meter.set_colorkey((255,0,252))
    meter_position = [213,663]

    screen.blit(reel1.image, reel1.position)
    screen.blit(reel10.image, reel10.position)
    screen.blit(reel100.image, reel100.position)
    screen.blit(reel1000.image, reel1000.position)
    screen.blit(meter, meter_position)

    backglass_position = [0, 0]
    backglass = pygame.Surface((720,1280), pygame.SRCALPHA | pygame.FULLSCREEN)
    backglass.fill((0, 0, 0))
    if menu == True:
        backglass = pygame.image.load('mississippi_showboat/assets/mississippi_showboat_menu.png')
    else:
        if (s.game.anti_cheat.status == True):
            backglass = pygame.image.load('mississippi_showboat/assets/mississippi_showboat_gi.png')
        else:
            backglass = pygame.image.load('mississippi_showboat/assets/mississippi_showboat_off.png')
    #backglass = pygame.transform.scale(backglass, (1280,720))
    screen.blit(backglass, backglass_position)

    if s.game.selector.position >= 1:
        position = [3,267]
        screen.blit(card, position)
    if s.game.selector.position >= 2:
        position = [249,270]
        screen.blit(card, position)
    if s.game.selector.position >= 3:
        position = [486,275]
        screen.blit(card, position)
    if s.game.selector.position >= 4:
        position = [18,798]
        screen.blit(card, position)
    if s.game.selector.position >= 5:
        position = [253,799]
        screen.blit(card, position)
    if s.game.selector.position >= 6:
        position = [484,797]
        screen.blit(card, position)

    if s.game.tilt.status == False:
        if s.holes:
            if 1 in s.holes:
                position = [81,371]
                screen.blit(number, position)
                position = [291,490]
                screen.blit(number, position)
                position = [668,378]
                screen.blit(number, position)
                position = [170,1045]
                screen.blit(number, position)
                position = [365,896]
                screen.blit(number, position)
                position = [521,1041]
                screen.blit(number, position)
            if 2 in s.holes:
                position = [120,523]
                screen.blit(number, position)
                position = [291,450]
                screen.blit(number, position)
                position = [667,417]
                screen.blit(number, position)
                position = [206,970]
                screen.blit(number, position)
                position = [399,1042]
                screen.blit(number, position)
                position = [521,932]
                screen.blit(number, position)
            if 3 in s.holes:
                position = [198,372]
                screen.blit(number, position)
                position = [437,529]
                screen.blit(number, position)
                position = [597,377]
                screen.blit(number, position)
                position = [60,897]
                screen.blit(number, position)
                position = [364,932]
                screen.blit(number, position)
                position = [626,1042]
                screen.blit(number, position)
            if 4 in s.holes:
                position = [158,523]
                screen.blit(number, position)
                position = [400,374]
                screen.blit(number, position)
                position = [631,531]
                screen.blit(number, position)
                position = [169,897]
                screen.blit(number, position)
                position = [292,896]
                screen.blit(number, position)
                position = [662,896]
                screen.blit(number, position)
            if 5 in s.holes:
                position = [43,370]
                screen.blit(number, position)
                position = [364,529]
                screen.blit(number, position)
                position = [525,454]
                screen.blit(number, position)
                position = [207,1043]
                screen.blit(number, position)
                position = [437,896]
                screen.blit(number, position)
                position = [663,966]
                screen.blit(number, position)
            if 6 in s.holes:
                position = [43,447]
                screen.blit(number, position)
                position = [438,375]
                screen.blit(number, position)
                position = [525,378]
                screen.blit(number, position)
                position = [62,1045]
                screen.blit(number, position)
                position = [329,896]
                screen.blit(number, position)
                position = [663,1040]
                screen.blit(number, position)
            if 7 in s.holes:
                position = [198,409]
                screen.blit(number, position)
                position = [328,529]
                screen.blit(number, position)
                position = [561,378]
                screen.blit(number, position)
                position = [97,897]
                screen.blit(number, position)
                position = [292,1044]
                screen.blit(number, position)
                position = [556,1042]
                screen.blit(number, position)
            if 8 in s.holes:
                position = [43,408]
                screen.blit(number, position)
                position = [437,492]
                screen.blit(number, position)
                position = [668,530]
                screen.blit(number, position)
                position = [206,933]
                screen.blit(number, position)
                position = [436,1008]
                screen.blit(number, position)
                position = [523,896]
                screen.blit(number, position)
            if 9 in s.holes:
                position = [121,372]
                screen.blit(number, position)
                position = [291,374]
                screen.blit(number, position)
                position = [596,492]
                screen.blit(number, position)
                position = [206,896]
                screen.blit(number, position)
                position = [292,970]
                screen.blit(number, position)
                position = [593,1006]
                screen.blit(number, position)
            if 10 in s.holes:
                position = [121,409]
                screen.blit(number, position)
                position = [292,528]
                screen.blit(number, position)
                position = [524,531]
                screen.blit(number, position)
                position = [134,897]
                screen.blit(number, position)
                position = [293,1008]
                screen.blit(number, position)
                position = [593,895]
                screen.blit(number, position)
            if 11 in s.holes:
                position = [159,446]
                screen.blit(number, position)
                position = [365,491]
                screen.blit(number, position)
                position = [523,493]
                screen.blit(number, position)
                position = [170,970]
                screen.blit(number, position)
                position = [436,1043]
                screen.blit(number, position)
                position = [663,1004]
                screen.blit(number, position)
            if 12 in s.holes:
                position = [44,523]
                screen.blit(number, position)
                position = [401,452]
                screen.blit(number, position)
                position = [597,416]
                screen.blit(number, position)
                position = [135,1009]
                screen.blit(number, position)
                position = [400,969]
                screen.blit(number, position)
                position = [557,969]
                screen.blit(number, position)
            if 13 in s.holes:
                position = [199,486]
                screen.blit(number, position)
                position = [291,412]
                screen.blit(number, position)
                position = [560,531]
                screen.blit(number, position)
                position = [62,1010]
                screen.blit(number, position)
                position = [436,932]
                screen.blit(number, position)
                position = [629,896]
                screen.blit(number, position)
            if 14 in s.holes:
                position = [121,487]
                screen.blit(number, position)
                position = [364,414]
                screen.blit(number, position)
                position = [561,415]
                screen.blit(number, position)
                position = [98,971]
                screen.blit(number, position)
                position = [401,1007]
                screen.blit(number, position)
                position = [628,931]
                screen.blit(number, position)
            if 15 in s.holes:
                position = [198,524]
                screen.blit(number, position)
                position = [366,451]
                screen.blit(number, position)
                position = [632,495]
                screen.blit(number, position)
                position = [61,972]
                screen.blit(number, position)
                position = [329,933]
                screen.blit(number, position)
                position = [557,1006]
                screen.blit(number, position)
            if 16 in s.holes:
                position = [121,447]
                screen.blit(number, position)
                position = [364,375]
                screen.blit(number, position)
                position = [632,454]
                screen.blit(number, position)
                position = [135,1045]
                screen.blit(number, position)
                position = [365,1007]
                screen.blit(number, position)
                position = [593,931]
                screen.blit(number, position)
            if 17 in s.holes:
                position = [198,446]
                screen.blit(number, position)
                position = [437,452]
                screen.blit(number, position)
                position = [560,494]
                screen.blit(number, position)
                position = [133,971]
                screen.blit(number, position)
                position = [401,932]
                screen.blit(number, position)
                position = [558,932]
                screen.blit(number, position)
            if 18 in s.holes:
                position = [82,447]
                screen.blit(number, position)
                position = [328,452]
                screen.blit(number, position)
                position = [633,417]
                screen.blit(number, position)
                position = [134,934]
                screen.blit(number, position)
                position = [329,1008]
                screen.blit(number, position)
                position = [627,1005]
                screen.blit(number, position)
            if 19 in s.holes:
                position = [158,409]
                screen.blit(number, position)
                position = [327,413]
                screen.blit(number, position)
                position = [561,454]
                screen.blit(number, position)
                position = [171,1009]
                screen.blit(number, position)
                position = [329,970]
                screen.blit(number, position)
                position = [628,967]
                screen.blit(number, position)
            if 20 in s.holes:
                position = [159,486]
                screen.blit(number, position)
                position = [401,413]
                screen.blit(number, position)
                position = [597,455]
                screen.blit(number, position)
                position = [98,1010]
                screen.blit(number, position)
                position = [436,968]
                screen.blit(number, position)
                position = [522,969]
                screen.blit(number, position)
            if 21 in s.holes:
                position = [82,486]
                screen.blit(number, position)
                position = [401,492]
                screen.blit(number, position)
                position = [596,531]
                screen.blit(number, position)
                position = [98,934]
                screen.blit(number, position)
                position = [365,969]
                screen.blit(number, position)
                position = [593,1042]
                screen.blit(number, position)
            if 22 in s.holes:
                position = [81,408]
                screen.blit(number, position)
                position = [328,492]
                screen.blit(number, position)
                position = [668,455]
                screen.blit(number, position)
                position = [170,933]
                screen.blit(number, position)
                position = [364,1044]
                screen.blit(number, position)
                position = [593,969]
                screen.blit(number, position)
            if 23 in s.holes:
                position = [82,524]
                screen.blit(number, position)
                position = [401,528]
                screen.blit(number, position)
                position = [525,416]
                screen.blit(number, position)
                position = [207,1009]
                screen.blit(number, position)
                position = [400,897]
                screen.blit(number, position)
                position = [558,896]
                screen.blit(number, position)
            if 24 in s.holes:
                position = [43,485]
                screen.blit(number, position)
                position = [327,374]
                screen.blit(number, position)
                position = [632,378]
                screen.blit(number, position)
                position = [61,934]
                screen.blit(number, position)
                position = [329,1044]
                screen.blit(number, position)
                position = [664,932]
                screen.blit(number, position)
            if 25 in s.holes:
                position = [159,371]
                screen.blit(number, position)
                position = [439,413]
                screen.blit(number, position)
                position = [668,494]
                screen.blit(number, position)
                position = [98,1046]
                screen.blit(number, position)
                position = [293,933]
                screen.blit(number, position)
                position = [521,1006]
                screen.blit(number, position)
                
        if s.game.selector.position > 0 and s.game.selector.position <= 11:
            p = [27,694]
            screen.blit(ball, p)
        elif s.game.selector.position > 11:
            p = [26,737]
            screen.blit(ball, p)



        if s.game.selector.position > 6:
            p = [3,366]
            screen.blit(red_diagonal, p)
            p = [253,369]
            screen.blit(red_diagonal, p)
            p = [488,373]
            screen.blit(red_diagonal, p)
            p = [22,573]
            screen.blit(feature, p)

        if s.game.selector.position > 7:
            p = [21,892]
            screen.blit(red_diagonal, p)
            p = [255,891]
            screen.blit(red_diagonal, p)
            p = [483,892]
            screen.blit(red_diagonal, p)
            p = [23,636]
            screen.blit(feature, p)

        if s.game.selector.position > 8:
            p = [375,626]
            screen.blit(magic_number, p)

        if s.game.selector.position > 9:
            p = [375,661]
            screen.blit(magic_number, p)

        if 1 in s.game.magic:
            p = [355,592]
            screen.blit(number, p)
        if 7 in s.game.magic:
            p = [388,592]
            screen.blit(number, p)
        if 9 in s.game.magic:
            p = [420,592]
            screen.blit(number, p)
        if 22 in s.game.magic:
            p = [453,593]
            screen.blit(number, p)
        if 25 in s.game.magic:
            p = [485,593]
            screen.blit(number, p)

        if s.game.onetwothree.status == True:
            p = [137,337]
            screen.blit(all_double, p)
            p = [379,340]
            screen.blit(all_double, p)
            p = [611,343]
            screen.blit(all_double, p)
            if s.game.dd1.status == True:
                p = [136,297]
                screen.blit(all_dd, p)
            if s.game.dd2.status == True:
                p = [380,299]
                screen.blit(all_dd, p)
            if s.game.dd3.status == True:
                p = [612,303]
                screen.blit(all_dd, p)
        
        if s.game.fourfivesix.status == True:
            p = [149,862]
            screen.blit(all_double, p)
            p = [379,862]
            screen.blit(all_double, p)
            p = [608,861]
            screen.blit(all_double, p)
            if s.game.dd4.status == True:
                p = [148,823]
                screen.blit(all_dd, p)
            if s.game.dd5.status == True:
                p = [381,823]
                screen.blit(all_dd, p)
            if s.game.dd6.status == True:
                p = [609,823]
                screen.blit(all_dd, p)

        if s.game.selector.position >= 11:
            p = [541,573]
            screen.blit(double_double, p)
            p = [540,668]
            screen.blit(double_double, p)

        if s.game.dd1.status == True:
            p = [550,601]
            screen.blit(number, p)
        if s.game.dd2.status == True:
            p = [593,603]
            screen.blit(number, p)
        if s.game.dd3.status == True:
            p = [636,602]
            screen.blit(number, p)
        if s.game.dd4.status == True:
            p = [550,635]
            screen.blit(number, p)
        if s.game.dd5.status == True:
            p = [593,636]
            screen.blit(number, p)
        if s.game.dd6.status == True:
            p = [635,636]
            screen.blit(number, p)

        if s.game.corners1.status == True:
            position = [4,306]
            screen.blit(corners, position)
        if s.game.corners2.status == True:
            position = [253,309]
            screen.blit(corners, position)
        if s.game.corners3.status == True:
            position = [488,313]
            screen.blit(corners, position)
        if s.game.corners4.status == True:
            position = [23,835]
            screen.blit(corners, position)
        if s.game.corners5.status == True:
            position = [257,835]
            screen.blit(corners, position)
        if s.game.corners6.status == True:
            position = [488,834]
            screen.blit(corners, position)

        if s.game.super1.status == True:
            position = [4,480]
            screen.blit(super_line, position)
        if s.game.super2.status == True:
            position = [255,485]
            screen.blit(super_line, position)
        if s.game.super3.status == True:
            position = [488,487]
            screen.blit(super_line, position)
        if s.game.super4.status == True:
            position = [25,1004]
            screen.blit(super_line, position)
        if s.game.super5.status == True:
            position = [256,1003]
            screen.blit(super_line, position)
        if s.game.super6.status == True:
            position = [485,1002]
            screen.blit(super_line, position)

        if s.game.card1_replay_counter.position > 0 or s.game.card2_replay_counter.position > 0 or s.game.card3_replay_counter.position > 0 or s.game.card4_replay_counter.position > 0 or s.game.card5_replay_counter.position > 0 or s.game.card6_replay_counter.position > 0:
            if s.game.card1_replay_counter.position > 0 and s.game.card1_double.status == False:
                position = [91,273]
                screen.blit(c, position)
            if s.game.card2_replay_counter.position > 0 and s.game.card2_double.status == False:
                position = [334,273]
                screen.blit(c, position)
            if s.game.card3_replay_counter.position > 0 and s.game.card3_double.status == False:
                position = [567,276]
                screen.blit(c, position)
            if s.game.card4_replay_counter.position > 0 and s.game.card4_double.status == False:
                position = [104,800]
                screen.blit(c, position)
            if s.game.card5_replay_counter.position > 0 and s.game.card5_double.status == False:
                position = [336,799]
                screen.blit(c, position)
            if s.game.card6_replay_counter.position > 0 and s.game.card6_double.status == False:
                position = [564,798]
                screen.blit(c, position)

        if s.game.card1_double.status == True:
            position = [142,273]
            screen.blit(d, position)
        if s.game.card2_double.status == True:
            position = [383,275]
            screen.blit(d, position)
        if s.game.card3_double.status == True:
            position = [616,279]
            screen.blit(d, position)
        if s.game.card4_double.status == True:
            position = [150,801]
            screen.blit(d, position)
        if s.game.card5_double.status == True:
            position = [384,800]
            screen.blit(d, position)
        if s.game.card6_double.status == True:
            position = [612,799]
            screen.blit(d, position)

        if s.game.card1_missed.status == True:
            position = [190,272]
            screen.blit(n, position)
        if s.game.card2_missed.status == True:
            position = [429,275]
            screen.blit(n, position)
        if s.game.card3_missed.status == True:
            position = [660,278]
            screen.blit(n, position)
        if s.game.card4_missed.status == True:
            position = [196,801]
            screen.blit(n, position)
        if s.game.card5_missed.status == True:
            position = [429,800]
            screen.blit(n, position)
        if s.game.card6_missed.status == True:
            position = [658,799]
            screen.blit(n, position)

    if s.game.selector.position >= 12:
        p = [492,755]
        screen.blit(number, p)
    if s.game.selector.position >= 13:
        p = [528,755]
        screen.blit(number, p)
    if s.game.selector.position >= 14:
        p = [564,755]
        screen.blit(number, p)
    if s.game.selector.position >= 15:
        p = [599,755]
        screen.blit(number, p)
    if s.game.selector.position >= 16:
        p = [635,755]
        screen.blit(number, p)
    if s.game.selector.position == 17:
        p = [670,755]
        screen.blit(number, p)

    if s.game.tilt.status == True:
        position = [254,720]
        screen.blit(tilt, position)

    pygame.display.update()

def blink_double(s):
    s.game.blink = not s.game.blink
    if s.game.blink == 1:
        blink_pos = [207,582]
        screen.blit(blink_image, blink_pos)
        pygame.display.update()
    else:
        display(s)
