
import pygame

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

meter = pygame.image.load('graphics/assets/black_register_cover.png').convert()
card = pygame.image.load('high_flyer/assets/card.png').convert_alpha()
number = pygame.image.load('high_flyer/assets/number.png').convert_alpha()
red_diagonal = pygame.image.load('high_flyer/assets/red_diagonal.png').convert_alpha()
feature = pygame.image.load('high_flyer/assets/feature.png').convert_alpha()
corners = pygame.image.load('high_flyer/assets/corners.png').convert_alpha()
super_line = pygame.image.load('high_flyer/assets/super_line.png').convert_alpha()
c = pygame.image.load('high_flyer/assets/regular.png').convert_alpha()
d = pygame.image.load('high_flyer/assets/double.png').convert_alpha()
n = pygame.image.load('high_flyer/assets/nothing.png').convert_alpha()
tilt = pygame.image.load('high_flyer/assets/tilt.png').convert_alpha()
blink_image = pygame.image.load('high_flyer/assets/double_or_nothing.png').convert_alpha()
bg_menu = pygame.image.load('high_flyer/assets/high_flyer_menu.png')
bg_gi = pygame.image.load('high_flyer/assets/high_flyer_gi.png')
bg_off = pygame.image.load('high_flyer/assets/high_flyer_off.png')

class scorereel():
    """ Score Reels are used to count replays """
    def __init__(self, pos, image):
        self.position = pos
        self.default_y = self.position[1]
        self.image = pygame.image.load(image).convert()

reel1 = scorereel([375,652], "graphics/assets/white_reel.png")
reel10 = scorereel([357,652], "graphics/assets/white_reel.png")
reel100 = scorereel([338,652], "graphics/assets/white_reel.png")
reel1000 = scorereel([318,652], "graphics/assets/white_reel.png")

def display(s, replays=0, menu=False):
    
    meter.set_colorkey((255,0,252))
    meter_position = [309,652]

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
        position = [68,286]
        screen.blit(card, position)
    if s.game.selector.position >= 2:
        position = [304,266]
        screen.blit(card, position)
    if s.game.selector.position >= 3:
        position = [540,291]
        screen.blit(card, position)
    if s.game.selector.position >= 4:
        position = [70,770]
        screen.blit(card, position)
    if s.game.selector.position >= 5:
        position = [304,788]
        screen.blit(card, position)
    if s.game.selector.position >= 6:
        position = [538,773]
        screen.blit(card, position)

    if s.game.tilt.status == False:
        if s.holes:
            if 1 in s.holes:
                position = [89,400]
                screen.blit(number, position)
                position = [288,502]
                screen.blit(number, position)
                position = [669,405]
                screen.blit(number, position)
                position = [162,1047]
                screen.blit(number, position)
                position = [360,900]
                screen.blit(number, position)
                position = [523,1049]
                screen.blit(number, position)
            if 2 in s.holes:
                position = [126,565]
                screen.blit(number, position)
                position = [288,461]
                screen.blit(number, position)
                position = [669,445]
                screen.blit(number, position)
                position = [198,964]
                screen.blit(number, position)
                position = [395,1064]
                screen.blit(number, position)
                position = [522,925]
                screen.blit(number, position)
            if 3 in s.holes:
                position = [198,403]
                screen.blit(number, position)
                position = [431,543]
                screen.blit(number, position)
                position = [596,404]
                screen.blit(number, position)
                position = [52,882]
                screen.blit(number, position)
                position = [360,939]
                screen.blit(number, position)
                position = [632,1048]
                screen.blit(number, position)
            if 4 in s.holes:
                position = [161,563]
                screen.blit(number, position)
                position = [396,379]
                screen.blit(number, position)
                position = [631,566]
                screen.blit(number, position)
                position = [162,882]
                screen.blit(number, position)
                position = [287,899]
                screen.blit(number, position)
                position = [668,885]
                screen.blit(number, position)
            if 5 in s.holes:
                position = [52,399]
                screen.blit(number, position)
                position = [360,542]
                screen.blit(number, position)
                position = [523,485]
                screen.blit(number, position)
                position = [198,1045]
                screen.blit(number, position)
                position = [432,900]
                screen.blit(number, position)
                position = [668,967]
                screen.blit(number, position)
            if 6 in s.holes:
                position = [54,481]
                screen.blit(number, position)
                position = [433,380]
                screen.blit(number, position)
                position = [523,404]
                screen.blit(number, position)
                position = [52,1045]
                screen.blit(number, position)
                position = [324,899]
                screen.blit(number, position)
                position = [669,1049]
                screen.blit(number, position)
            if 7 in s.holes:
                position = [199,442]
                screen.blit(number, position)
                position = [324,542]
                screen.blit(number, position)
                position = [560,405]
                screen.blit(number, position)
                position = [89,881]
                screen.blit(number, position)
                position = [287,1063]
                screen.blit(number, position)
                position = [558,1048]
                screen.blit(number, position)
            if 8 in s.holes:
                position = [53,440]
                screen.blit(number, position)
                position = [432,502]
                screen.blit(number, position)
                position = [668,568]
                screen.blit(number, position)
                position = [198,923]
                screen.blit(number, position)
                position = [432,1023]
                screen.blit(number, position)
                position = [523,885]
                screen.blit(number, position)
            if 9 in s.holes:
                position = [126,401]
                screen.blit(number, position)
                position = [289,379]
                screen.blit(number, position)
                position = [595,526]
                screen.blit(number, position)
                position = [199,883]
                screen.blit(number, position)
                position = [288,980]
                screen.blit(number, position)
                position = [595,1007]
                screen.blit(number, position)
            if 10 in s.holes:
                position = [126,441]
                screen.blit(number, position)
                position = [288,541]
                screen.blit(number, position)
                position = [523,567]
                screen.blit(number, position)
                position = [126,882]
                screen.blit(number, position)
                position = [287,1021]
                screen.blit(number, position)
                position = [595,884]
                screen.blit(number, position)
            if 11 in s.holes:
                position = [162,482]
                screen.blit(number, position)
                position = [360,501]
                screen.blit(number, position)
                position = [523,526]
                screen.blit(number, position)
                position = [162,963]
                screen.blit(number, position)
                position = [432,1062]
                screen.blit(number, position)
                position = [668,1008]
                screen.blit(number, position)
            if 12 in s.holes:
                position = [54,563]
                screen.blit(number, position)
                position = [397,461]
                screen.blit(number, position)
                position = [596,444]
                screen.blit(number, position)
                position = [125,1004]
                screen.blit(number, position)
                position = [395,982]
                screen.blit(number, position)
                position = [558,966]
                screen.blit(number, position)
            if 13 in s.holes:
                position = [198,524]
                screen.blit(number, position)
                position = [288,420]
                screen.blit(number, position)
                position = [559,566]
                screen.blit(number, position)
                position = [51,1005]
                screen.blit(number, position)
                position = [432,941]
                screen.blit(number, position)
                position = [631,886]
                screen.blit(number, position)
            if 14 in s.holes:
                position = [126,523]
                screen.blit(number, position)
                position = [360,420]
                screen.blit(number, position)
                position = [560,445]
                screen.blit(number, position)
                position = [89,963]
                screen.blit(number, position)
                position = [395,1022]
                screen.blit(number, position)
                position = [632,926]
                screen.blit(number, position)
            if 15 in s.holes:
                position = [199,565]
                screen.blit(number, position)
                position = [360,461]
                screen.blit(number, position)
                position = [632,526]
                screen.blit(number, position)
                position = [53,963]
                screen.blit(number, position)
                position = [324,939]
                screen.blit(number, position)
                position = [559,1006]
                screen.blit(number, position)
            if 16 in s.holes:
                position = [127,482]
                screen.blit(number, position)
                position = [360,379]
                screen.blit(number, position)
                position = [633,486]
                screen.blit(number, position)
                position = [125,1045]
                screen.blit(number, position)
                position = [360,1022]
                screen.blit(number, position)
                position = [595,925]
                screen.blit(number, position)
            if 17 in s.holes:
                position = [198,483]
                screen.blit(number, position)
                position = [432,461]
                screen.blit(number, position)
                position = [559,525]
                screen.blit(number, position)
                position = [126,963]
                screen.blit(number, position)
                position = [396,940]
                screen.blit(number, position)
                position = [559,925]
                screen.blit(number, position)
            if 18 in s.holes:
                position = [90,482]
                screen.blit(number, position)
                position = [324,461]
                screen.blit(number, position)
                position = [632,444]
                screen.blit(number, position)
                position = [126,923]
                screen.blit(number, position)
                position = [323,1022]
                screen.blit(number, position)
                position = [632,1008]
                screen.blit(number, position)
            if 19 in s.holes:
                position = [163,441]
                screen.blit(number, position)
                position = [325,420]
                screen.blit(number, position)
                position = [560,485]
                screen.blit(number, position)
                position = [161,1004]
                screen.blit(number, position)
                position = [324,980]
                screen.blit(number, position)
                position = [632,967]
                screen.blit(number, position)
            if 20 in s.holes:
                position = [163,524]
                screen.blit(number, position)
                position = [397,421]
                screen.blit(number, position)
                position = [597,486]
                screen.blit(number, position)
                position = [88,1004]
                screen.blit(number, position)
                position = [432,981]
                screen.blit(number, position)
                position = [523,965]
                screen.blit(number, position)
            if 21 in s.holes:
                position = [90,522]
                screen.blit(number, position)
                position = [397,503]
                screen.blit(number, position)
                position = [596,567]
                screen.blit(number, position)
                position = [90,923]
                screen.blit(number, position)
                position = [360,981]
                screen.blit(number, position)
                position = [596,1049]
                screen.blit(number, position)
            if 22 in s.holes:
                position = [90,441]
                screen.blit(number, position)
                position = [325,501]
                screen.blit(number, position)
                position = [670,486]
                screen.blit(number, position)
                position = [162,922]
                screen.blit(number, position)
                position = [360,1063]
                screen.blit(number, position)
                position = [596,967]
                screen.blit(number, position)
            if 23 in s.holes:
                position = [91,563]
                screen.blit(number, position)
                position = [396,542]
                screen.blit(number, position)
                position = [524,445]
                screen.blit(number, position)
                position = [198,1004]
                screen.blit(number, position)
                position = [396,900]
                screen.blit(number, position)
                position = [559,885]
                screen.blit(number, position)
            if 24 in s.holes:
                position = [53,522]
                screen.blit(number, position)
                position = [324,379]
                screen.blit(number, position)
                position = [632,404]
                screen.blit(number, position)
                position = [53,922]
                screen.blit(number, position)
                position = [323,1062]
                screen.blit(number, position)
                position = [669,926]
                screen.blit(number, position)
            if 25 in s.holes:
                position = [162,401]
                screen.blit(number, position)
                position = [433,421]
                screen.blit(number, position)
                position = [669,526]
                screen.blit(number, position)
                position = [89,1045]
                screen.blit(number, position)
                position = [288,940]
                screen.blit(number, position)
                position = [523,1007]
                screen.blit(number, position)

        if s.game.selector.position > 6:
            p = [12,393]
            screen.blit(red_diagonal, p)
            p = [248,373]
            screen.blit(red_diagonal, p)
            p = [484,398]
            screen.blit(red_diagonal, p)
            p = [52,617]
            screen.blit(feature, p)

        if s.game.selector.position > 7:
            p = [13,876]
            screen.blit(red_diagonal, p)
            p = [248,893]
            screen.blit(red_diagonal, p)
            p = [483,879]
            screen.blit(red_diagonal, p)
            p = [53,697]
            screen.blit(feature, p)



        if s.game.corners1.status == True:
            position = [12,321]
            screen.blit(corners, position)
        if s.game.corners2.status == True:
            position = [248,301]
            screen.blit(corners, position)
        if s.game.corners3.status == True:
            position = [484,328]
            screen.blit(corners, position)
        if s.game.corners4.status == True:
            position = [13,804]
            screen.blit(corners, position)
        if s.game.corners5.status == True:
            position = [248,822]
            screen.blit(corners, position)
        if s.game.corners6.status == True:
            position = [482,807]
            screen.blit(corners, position)

        if s.game.super1.status == True:
            position = [16,519]
            screen.blit(super_line, position)
        if s.game.super2.status == True:
            position = [251,498]
            screen.blit(super_line, position)
        if s.game.super3.status == True:
            position = [486,523]
            screen.blit(super_line, position)
        if s.game.super4.status == True:
            position = [15,1001]
            screen.blit(super_line, position)
        if s.game.super5.status == True:
            position = [250,1018]
            screen.blit(super_line, position)
        if s.game.super6.status == True:
            position = [486,1004]
            screen.blit(super_line, position)

        if s.game.card1_replay_counter.position > 0 or s.game.card2_replay_counter.position > 0 or s.game.card3_replay_counter.position > 0 or s.game.card4_replay_counter.position > 0 or s.game.card5_replay_counter.position > 0 or s.game.card6_replay_counter.position > 0:
            if s.game.card1_replay_counter.position > 0 and s.game.card1_double.status == False:
                position = [72,347]
                screen.blit(c, position)
            if s.game.card2_replay_counter.position > 0 and s.game.card2_double.status == False:
                position = [307,328]
                screen.blit(c, position)
            if s.game.card3_replay_counter.position > 0 and s.game.card3_double.status == False:
                position = [543,352]
                screen.blit(c, position)
            if s.game.card4_replay_counter.position > 0 and s.game.card4_double.status == False:
                position = [72,830]
                screen.blit(c, position)
            if s.game.card5_replay_counter.position > 0 and s.game.card5_double.status == False:
                position = [306,849]
                screen.blit(c, position)
            if s.game.card6_replay_counter.position > 0 and s.game.card6_double.status == False:
                position = [541,833]
                screen.blit(c, position)

        if s.game.card1_double.status == True:
            position = [126,353]
            screen.blit(d, position)
        if s.game.card2_double.status == True:
            position = [360,332]
            screen.blit(d, position)
        if s.game.card3_double.status == True:
            position = [597,356]
            screen.blit(d, position)
        if s.game.card4_double.status == True:
            position = [125,835]
            screen.blit(d, position)
        if s.game.card5_double.status == True:
            position = [358,853]
            screen.blit(d, position)
        if s.game.card6_double.status == True:
            position = [595,838]
            screen.blit(d, position)

        if s.game.card1_missed.status == True:
            position = [178,354]
            screen.blit(n, position)
        if s.game.card2_missed.status == True:
            position = [412,333]
            screen.blit(n, position)
        if s.game.card3_missed.status == True:
            position = [649,357]
            screen.blit(n, position)
        if s.game.card4_missed.status == True:
            position = [177,836]
            screen.blit(n, position)
        if s.game.card5_missed.status == True:
            position = [412,854]
            screen.blit(n, position)
        if s.game.card6_missed.status == True:
            position = [647,839]
            screen.blit(n, position)

    if s.game.tilt.status == True:
        position = [486,254]
        screen.blit(tilt, position)

    pygame.display.update()

def blink_double(s):
    dirty_rects = []
    s.game.blink = not s.game.blink
    if s.game.blink == 1:
        blink_pos = [497,639]
        dirty_rects.append(screen.blit(blink_image, blink_pos))
        pygame.display.update(dirty_rects)
    else:
        dirty_rects.append(screen.blit(bg_gi, (497,639), pygame.Rect(497,639,154,104)))
        pygame.display.update(dirty_rects)
