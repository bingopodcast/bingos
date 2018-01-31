
import pygame

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

meter = pygame.image.load('graphics/assets/black_register_cover.png').convert()
card = pygame.image.load('ticker_tape/assets/card.png').convert_alpha()
number = pygame.image.load('ticker_tape/assets/number.png').convert_alpha()
corners = pygame.image.load('ticker_tape/assets/corners.png').convert_alpha()
super_line = pygame.image.load('ticker_tape/assets/super_line.png').convert_alpha()
c = pygame.image.load('ticker_tape/assets/regular.png').convert_alpha()
d = pygame.image.load('ticker_tape/assets/double.png').convert_alpha()
n = pygame.image.load('ticker_tape/assets/nothing.png').convert_alpha()
tilt = pygame.image.load('ticker_tape/assets/tilt.png').convert_alpha()
blink_image = pygame.image.load('ticker_tape/assets/double_or_nothing.png').convert_alpha()
bg_menu = pygame.image.load('ticker_tape/assets/ticker_tape_menu.png')
bg_gi = pygame.image.load('ticker_tape/assets/ticker_tape_gi.png')
bg_off = pygame.image.load('ticker_tape/assets/ticker_tape_off.png')

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
        position = [63,378]
        screen.blit(card, position)
    if s.game.selector.position >= 2:
        position = [286,343]
        screen.blit(card, position)
    if s.game.selector.position >= 3:
        position = [509,378]
        screen.blit(card, position)
    if s.game.selector.position >= 4:
        position = [63,767]
        screen.blit(card, position)
    if s.game.selector.position >= 5:
        position = [286,781]
        screen.blit(card, position)
    if s.game.selector.position >= 6:
        position = [509,765]
        screen.blit(card, position)

    if s.game.tilt.status == False:
        if s.holes:
            if 1 in s.holes:
                position = [95,445]
                screen.blit(number, position)
                position = [287,508]
                screen.blit(number, position)
                position = [638,445]
                screen.blit(number, position)
                position = [157,969]
                screen.blit(number, position)
                position = [350,848]
                screen.blit(number, position)
                position = [510,968]
                screen.blit(number, position)
            if 2 in s.holes:
                position = [127,579]
                screen.blit(number, position)
                position = [286,475]
                screen.blit(number, position)
                position = [638,479]
                screen.blit(number, position)
                position = [191,900]
                screen.blit(number, position)
                position = [383,983]
                screen.blit(number, position)
                position = [509,867]
                screen.blit(number, position)
            if 3 in s.holes:
                position = [193,445]
                screen.blit(number, position)
                position = [415,542]
                screen.blit(number, position)
                position = [573,443]
                screen.blit(number, position)
                position = [61,834]
                screen.blit(number, position)
                position = [349,881]
                screen.blit(number, position)
                position = [608,969]
                screen.blit(number, position)
            if 4 in s.holes:
                position = [161,580]
                screen.blit(number, position)
                position = [383,408]
                screen.blit(number, position)
                position = [605,578]
                screen.blit(number, position)
                position = [159,833]
                screen.blit(number, position)
                position = [285,848]
                screen.blit(number, position)
                position = [639,832]
                screen.blit(number, position)
            if 5 in s.holes:
                position = [63,444]
                screen.blit(number, position)
                position = [351,542]
                screen.blit(number, position)
                position = [509,511]
                screen.blit(number, position)
                position = [191,968]
                screen.blit(number, position)
                position = [415,848]
                screen.blit(number, position)
                position = [640,901]
                screen.blit(number, position)
            if 6 in s.holes:
                position = [63,511]
                screen.blit(number, position)
                position = [415,409]
                screen.blit(number, position)
                position = [509,445]
                screen.blit(number, position)
                position = [60,970]
                screen.blit(number, position)
                position = [318,848]
                screen.blit(number, position)
                position = [641,969]
                screen.blit(number, position)
            if 7 in s.holes:
                position = [193,478]
                screen.blit(number, position)
                position = [319,542]
                screen.blit(number, position)
                position = [541,445]
                screen.blit(number, position)
                position = [93,834]
                screen.blit(number, position)
                position = [286,984]
                screen.blit(number, position)
                position = [543,969]
                screen.blit(number, position)
            if 8 in s.holes:
                position = [63,478]
                screen.blit(number, position)
                position = [415,509]
                screen.blit(number, position)
                position = [637,578]
                screen.blit(number, position)
                position = [191,867]
                screen.blit(number, position)
                position = [416,949]
                screen.blit(number, position)
                position = [509,833]
                screen.blit(number, position)
            if 9 in s.holes:
                position = [128,446]
                screen.blit(number, position)
                position = [287,409]
                screen.blit(number, position)
                position = [573,546]
                screen.blit(number, position)
                position = [191,833]
                screen.blit(number, position)
                position = [286,916]
                screen.blit(number, position)
                position = [575,935]
                screen.blit(number, position)
            if 10 in s.holes:
                position = [129,478]
                screen.blit(number, position)
                position = [287,543]
                screen.blit(number, position)
                position = [509,579]
                screen.blit(number, position)
                position = [127,834]
                screen.blit(number, position)
                position = [286,949]
                screen.blit(number, position)
                position = [575,833]
                screen.blit(number, position)
            if 11 in s.holes:
                position = [160,512]
                screen.blit(number, position)
                position = [352,509]
                screen.blit(number, position)
                position = [509,545]
                screen.blit(number, position)
                position = [159,901]
                screen.blit(number, position)
                position = [416,984]
                screen.blit(number, position)
                position = [641,935]
                screen.blit(number, position)
            if 12 in s.holes:
                position = [63,579]
                screen.blit(number, position)
                position = [383,476]
                screen.blit(number, position)
                position = [573,479]
                screen.blit(number, position)
                position = [126,935]
                screen.blit(number, position)
                position = [383,915]
                screen.blit(number, position)
                position = [543,901]
                screen.blit(number, position)
            if 13 in s.holes:
                position = [193,545]
                screen.blit(number, position)
                position = [288,441]
                screen.blit(number, position)
                position = [541,579]
                screen.blit(number, position)
                position = [60,935]
                screen.blit(number, position)
                position = [416,881]
                screen.blit(number, position)
                position = [607,833]
                screen.blit(number, position)
            if 14 in s.holes:
                position = [129,545]
                screen.blit(number, position)
                position = [353,443]
                screen.blit(number, position)
                position = [541,479]
                screen.blit(number, position)
                position = [93,901]
                screen.blit(number, position)
                position = [384,949]
                screen.blit(number, position)
                position = [607,868]
                screen.blit(number, position)
            if 15 in s.holes:
                position = [193,579]
                screen.blit(number, position)
                position = [352,476]
                screen.blit(number, position)
                position = [607,545]
                screen.blit(number, position)
                position = [60,903]
                screen.blit(number, position)
                position = [319,881]
                screen.blit(number, position)
                position = [543,934]
                screen.blit(number, position)
            if 16 in s.holes:
                position = [128,512]
                screen.blit(number, position)
                position = [352,409]
                screen.blit(number, position)
                position = [607,511]
                screen.blit(number, position)
                position = [126,970]
                screen.blit(number, position)
                position = [352,950]
                screen.blit(number, position)
                position = [575,868]
                screen.blit(number, position)
            if 17 in s.holes:
                position = [193,514]
                screen.blit(number, position)
                position = [417,477]
                screen.blit(number, position)
                position = [541,545]
                screen.blit(number, position)
                position = [126,902]
                screen.blit(number, position)
                position = [384,882]
                screen.blit(number, position)
                position = [542,867]
                screen.blit(number, position)
            if 18 in s.holes:
                position = [95,513]
                screen.blit(number, position)
                position = [319,477]
                screen.blit(number, position)
                position = [607,479]
                screen.blit(number, position)
                position = [127,867]
                screen.blit(number, position)
                position = [319,949]
                screen.blit(number, position)
                position = [609,935]
                screen.blit(number, position)
            if 19 in s.holes:
                position = [161,479]
                screen.blit(number, position)
                position = [319,443]
                screen.blit(number, position)
                position = [542,513]
                screen.blit(number, position)
                position = [159,935]
                screen.blit(number, position)
                position = [319,917]
                screen.blit(number, position)
                position = [608,901]
                screen.blit(number, position)
            if 20 in s.holes:
                position = [161,545]
                screen.blit(number, position)
                position = [384,443]
                screen.blit(number, position)
                position = [574,511]
                screen.blit(number, position)
                position = [93,935]
                screen.blit(number, position)
                position = [416,917]
                screen.blit(number, position)
                position = [510,901]
                screen.blit(number, position)
            if 21 in s.holes:
                position = [96,545]
                screen.blit(number, position)
                position = [384,509]
                screen.blit(number, position)
                position = [574,579]
                screen.blit(number, position)
                position = [94,867]
                screen.blit(number, position)
                position = [351,916]
                screen.blit(number, position)
                position = [577,969]
                screen.blit(number, position)
            if 22 in s.holes:
                position = [97,479]
                screen.blit(number, position)
                position = [320,509]
                screen.blit(number, position)
                position = [639,511]
                screen.blit(number, position)
                position = [160,867]
                screen.blit(number, position)
                position = [352,985]
                screen.blit(number, position)
                position = [576,901]
                screen.blit(number, position)
            if 23 in s.holes:
                position = [96,579]
                screen.blit(number, position)
                position = [383,543]
                screen.blit(number, position)
                position = [510,480]
                screen.blit(number, position)
                position = [193,934]
                screen.blit(number, position)
                position = [384,848]
                screen.blit(number, position)
                position = [543,833]
                screen.blit(number, position)
            if 24 in s.holes:
                position = [63,545]
                screen.blit(number, position)
                position = [319,409]
                screen.blit(number, position)
                position = [607,445]
                screen.blit(number, position)
                position = [62,868]
                screen.blit(number, position)
                position = [319,984]
                screen.blit(number, position)
                position = [641,869]
                screen.blit(number, position)
            if 25 in s.holes:
                position = [161,445]
                screen.blit(number, position)
                position = [415,443]
                screen.blit(number, position)
                position = [639,545]
                screen.blit(number, position)
                position = [94,969]
                screen.blit(number, position)
                position = [287,881]
                screen.blit(number, position)
                position = [511,935]
                screen.blit(number, position)

        if s.game.corners1.status == True:
            position = [173,377]
            screen.blit(corners, position)
        if s.game.corners2.status == True:
            position = [397,341]
            screen.blit(corners, position)
        if s.game.corners3.status == True:
            position = [619,377]
            screen.blit(corners, position)
        if s.game.corners4.status == True:
            position = [173,765]
            screen.blit(corners, position)
        if s.game.corners5.status == True:
            position = [397,779]
            screen.blit(corners, position)
        if s.game.corners6.status == True:
            position = [619,765]
            screen.blit(corners, position)

        if s.game.super1.status == True:
            position = [17,443]
            screen.blit(super_line, position)
        if s.game.super2.status == True:
            position = [242,409]
            screen.blit(super_line, position)
        if s.game.super3.status == True:
            position = [463,445]
            screen.blit(super_line, position)
        if s.game.super4.status == True:
            position = [15,835]
            screen.blit(super_line, position)
        if s.game.super5.status == True:
            position = [240,849]
            screen.blit(super_line, position)
        if s.game.super6.status == True:
            position = [462,834]
            screen.blit(super_line, position)

        if s.game.card1_replay_counter.position > 0 or s.game.card2_replay_counter.position > 0 or s.game.card3_replay_counter.position > 0 or s.game.card4_replay_counter.position > 0 or s.game.card5_replay_counter.position > 0 or s.game.card6_replay_counter.position > 0:
            if s.game.card1_replay_counter.position > 0 and s.game.card1_double.status == False:
                position = [17,409]
                screen.blit(c, position)
            if s.game.card2_replay_counter.position > 0 and s.game.card2_double.status == False:
                position = [241,375]
                screen.blit(c, position)
            if s.game.card3_replay_counter.position > 0 and s.game.card3_double.status == False:
                position = [463,413]
                screen.blit(c, position)
            if s.game.card4_replay_counter.position > 0 and s.game.card4_double.status == False:
                position = [17,801]
                screen.blit(c, position)
            if s.game.card5_replay_counter.position > 0 and s.game.card5_double.status == False:
                position = [241,816]
                screen.blit(c, position)
            if s.game.card6_replay_counter.position > 0 and s.game.card6_double.status == False:
                position = [463,800]
                screen.blit(c, position)

        if s.game.card1_double.status == True:
            position = [68,414]
            screen.blit(d, position)
        if s.game.card2_double.status == True:
            position = [291,379]
            screen.blit(d, position)
        if s.game.card3_double.status == True:
            position = [512,414]
            screen.blit(d, position)
        if s.game.card4_double.status == True:
            position = [65,802]
            screen.blit(d, position)
        if s.game.card5_double.status == True:
            position = [290,817]
            screen.blit(d, position)
        if s.game.card6_double.status == True:
            position = [513,801]
            screen.blit(d, position)

        if s.game.card1_missed.status == True:
            position = [120,414]
            screen.blit(n, position)
        if s.game.card2_missed.status == True:
            position = [343,378]
            screen.blit(n, position)
        if s.game.card3_missed.status == True:
            position = [565,414]
            screen.blit(n, position)
        if s.game.card4_missed.status == True:
            position = [119,802]
            screen.blit(n, position)
        if s.game.card5_missed.status == True:
            position = [343,816]
            screen.blit(n, position)
        if s.game.card6_missed.status == True:
            position = [566,801]
            screen.blit(n, position)

    if s.game.tilt.status == True:
        position = [597,655]
        screen.blit(tilt, position)

    pygame.display.update()

def blink_double(s):
    dirty_rects = []
    s.game.blink = not s.game.blink
    if s.game.blink == 1:
        blink_pos = [80,638]
        dirty_rects.append(screen.blit(blink_image, blink_pos))
        pygame.display.update(dirty_rects)
    else:
        dirty_rects.append(screen.blit(bg_gi, (80,638), pygame.Rect(80,638,163,107)))
        pygame.display.update(dirty_rects)
