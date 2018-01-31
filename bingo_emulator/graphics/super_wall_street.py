
import pygame

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

meter = pygame.image.load('graphics/assets/black_register_cover.png').convert()
card = pygame.image.load('super_wall_street/assets/card.png').convert_alpha()
feature = pygame.image.load('super_wall_street/assets/feature.png').convert_alpha()
eb_display = pygame.image.load('super_wall_street/assets/sixth_ball.png').convert_alpha()
number = pygame.image.load('super_wall_street/assets/number.png').convert_alpha()
corners = pygame.image.load('super_wall_street/assets/corners.png').convert_alpha()
c = pygame.image.load('super_wall_street/assets/regular.png').convert_alpha()
d = pygame.image.load('super_wall_street/assets/double.png').convert_alpha()
n = pygame.image.load('super_wall_street/assets/nothing.png').convert_alpha()
tilt = pygame.image.load('super_wall_street/assets/tilt.png').convert_alpha()
blink_image = pygame.image.load('super_wall_street/assets/double_or_nothing.png').convert_alpha()
bg_menu = pygame.image.load('super_wall_street/assets/super_wall_street_menu.png')
bg_gi = pygame.image.load('super_wall_street/assets/super_wall_street_gi.png')
bg_off = pygame.image.load('super_wall_street/assets/super_wall_street_off.png')

class scorereel():
    """ Score Reels are used to count replays """
    def __init__(self, pos, image):
        self.position = pos
        self.default_y = self.position[1]
        self.image = pygame.image.load(image).convert()

reel1 = scorereel([378,695], "graphics/assets/white_reel.png")
reel10 = scorereel([360,695], "graphics/assets/white_reel.png")
reel100 = scorereel([341,695], "graphics/assets/white_reel.png")
reel1000 = scorereel([321,695], "graphics/assets/white_reel.png")

def display(s, replays=0, menu=False):
    
    meter.set_colorkey((255,0,252))
    meter_position = [312,695]

    screen.blit(reel1.image, reel1.position)
    screen.blit(reel10.image, reel10.position)
    screen.blit(reel100.image, reel100.position)
    screen.blit(reel1000.image, reel1000.position)
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
        position = [345,362]
        screen.blit(card, position)
    if s.game.selector.position >= 1 and s.game.selector.position <= 3:
        position = [247,600]
        screen.blit(feature, position)
    if s.game.selector.position >= 2:
        position = [120,538]
        screen.blit(card, position)
    if s.game.selector.position >= 2 and s.game.selector.position <= 4:
        position = [20,777]
        screen.blit(feature, position)
    if s.game.selector.position >= 3:
        position = [571,540]
        screen.blit(card, position)
    if s.game.selector.position >= 3 and s.game.selector.position <= 5:
        position = [471,777]
        screen.blit(feature, position)
    if s.game.selector.position >= 4:
        position = [349,600]
        screen.blit(feature, position)
    if s.game.selector.position >= 5:
        position = [125,776]
        screen.blit(feature, position)
    if s.game.selector.position >= 6:
        position = [575,776]
        screen.blit(feature, position)
    if s.game.selector.position == 7:
        position = [266,880]
        screen.blit(eb_display, position)

    if s.game.tilt.status == False:
        if s.holes:
            if 1 in s.holes:
                position = [367,556]
                screen.blit(number, position)
                position = [110,606]
                screen.blit(number, position)
                position = [496,732]
                screen.blit(number, position)
            if 2 in s.holes:
                position = [400,494]
                screen.blit(number, position)
                position = [142,732]
                screen.blit(number, position)
                position = [496,638]
                screen.blit(number, position)
            if 3 in s.holes:
                position = [269,430]
                screen.blit(number, position)
                position = [110,638]
                screen.blit(number, position)
                position = [594,732]
                screen.blit(number, position)
            if 4 in s.holes:
                position = [368,430]
                screen.blit(number, position)
                position = [44,606]
                screen.blit(number, position)
                position = [627,608]
                screen.blit(number, position)
            if 5 in s.holes:
                position = [402,556]
                screen.blit(number, position)
                position = [175,606]
                screen.blit(number, position)
                position = [626,670]
                screen.blit(number, position)
            if 6 in s.holes:
                position = [272,556]
                screen.blit(number, position)
                position = [76,606]
                screen.blit(number, position)
                position = [624,732]
                screen.blit(number, position)
            if 7 in s.holes:
                position = [304,430]
                screen.blit(number, position)
                position = [44,730]
                screen.blit(number, position)
                position = [528,732]
                screen.blit(number, position)
            if 8 in s.holes:
                position = [401,461]
                screen.blit(number, position)
                position = [176,701]
                screen.blit(number, position)
                position = [495,607]
                screen.blit(number, position)
            if 9 in s.holes:
                position = [401,430]
                screen.blit(number, position)
                position = [45,668]
                screen.blit(number, position)
                position = [561,702]
                screen.blit(number, position)
            if 10 in s.holes:
                position = [336,430]
                screen.blit(number, position)
                position = [45,700]
                screen.blit(number, position)
                position = [560,608]
                screen.blit(number, position)
            if 11 in s.holes:
                position = [368,492]
                screen.blit(number, position)
                position = [177,732]
                screen.blit(number, position)
                position = [626,702]
                screen.blit(number, position)
            if 12 in s.holes:
                position = [335,525]
                screen.blit(number, position)
                position = [144,669]
                screen.blit(number, position)
                position = [528,670]
                screen.blit(number, position)
            if 13 in s.holes:
                position = [271,525]
                screen.blit(number, position)
                position = [176,638]
                screen.blit(number, position)
                position = [593,607]
                screen.blit(number, position)
            if 14 in s.holes:
                position = [304,494]
                screen.blit(number, position)
                position = [142,702]
                screen.blit(number, position)
                position = [594,638]
                screen.blit(number, position)
            if 15 in s.holes:
                position = [272,492]
                screen.blit(number, position)
                position = [79,638]
                screen.blit(number, position)
                position = [528,702]
                screen.blit(number, position)
            if 16 in s.holes:
                position = [336,557]
                screen.blit(number, position)
                position = [112,700]
                screen.blit(number, position)
                position = [560,639]
                screen.blit(number, position)
            if 17 in s.holes:
                position = [336,494]
                screen.blit(number, position)
                position = [144,638]
                screen.blit(number, position)
                position = [528,638]
                screen.blit(number, position)
            if 18 in s.holes:
                position = [336,462]
                screen.blit(number, position)
                position = [79,700]
                screen.blit(number, position)
                position = [594,702]
                screen.blit(number, position)
            if 19 in s.holes:
                position = [369,525]
                screen.blit(number, position)
                position = [78,669]
                screen.blit(number, position)
                position = [593,670]
                screen.blit(number, position)
            if 20 in s.holes:
                position = [304,525]
                screen.blit(number, position)
                position = [177,670]
                screen.blit(number, position)
                position = [496,671]
                screen.blit(number, position)
            if 21 in s.holes:
                position = [304,461]
                screen.blit(number, position)
                position = [112,670]
                screen.blit(number, position)
                position = [562,732]
                screen.blit(number, position)
            if 22 in s.holes:
                position = [369,462]
                screen.blit(number, position)
                position = [112,731]
                screen.blit(number, position)
                position = [560,671]
                screen.blit(number, position)
            if 23 in s.holes:
                position = [402,525]
                screen.blit(number, position)
                position = [144,606]
                screen.blit(number, position)
                position = [528,608]
                screen.blit(number, position)
            if 24 in s.holes:
                position = [272,461]
                screen.blit(number, position)
                position = [79,732]
                screen.blit(number, position)
                position = [627,640]
                screen.blit(number, position)
            if 25 in s.holes:
                position = [304,556]
                screen.blit(number, position)
                position = [46,638]
                screen.blit(number, position)
                position = [494,700]
                screen.blit(number, position)

        if s.game.corners1.status == True:
            position = [244,360]
            screen.blit(corners, position)
        if s.game.corners2.status == True:
            position = [17,537]
            screen.blit(corners, position)
        if s.game.corners3.status == True:
            position = [470,540]
            screen.blit(corners, position)

        if s.game.card1_replay_counter.position > 0 or s.game.card2_replay_counter.position > 0 or s.game.card3_replay_counter.position > 0:
            if s.game.card1_replay_counter.position > 0 and s.game.card1_double.status == False:
                position = [302,384]
                screen.blit(c, position)
            if s.game.card2_replay_counter.position > 0 and s.game.card2_double.status == False:
                position = [76,560]
                screen.blit(c, position)
            if s.game.card3_replay_counter.position > 0 and s.game.card3_double.status == False:
                position = [527,561]
                screen.blit(c, position)

        if s.game.card1_double.status == True:
            position = [349,400]
            screen.blit(d, position)
        if s.game.card2_double.status == True:
            position = [123,575]
            screen.blit(d, position)
        if s.game.card3_double.status == True:
            position = [575,577]
            screen.blit(d, position)

        if s.game.card1_missed.status == True:
            position = [405,400]
            screen.blit(n, position)
        if s.game.card2_missed.status == True:
            position = [179,577]
            screen.blit(n, position)
        if s.game.card3_missed.status == True:
            position = [630,578]
            screen.blit(n, position)

    if s.game.tilt.status == True:
        position = [600,923]
        screen.blit(tilt, position)

    pygame.display.update()

def blink_double(s):
    dirty_rects = []
    s.game.blink = not s.game.blink
    if s.game.blink == 1:
        blink_pos = [510,394]
        dirty_rects.append(screen.blit(blink_image, blink_pos))
        pygame.display.update(dirty_rects)
    else:
        dirty_rects.append(screen.blit(bg_gi, (510,394), pygame.Rect(510,394,156,93)))
        pygame.display.update(dirty_rects)
