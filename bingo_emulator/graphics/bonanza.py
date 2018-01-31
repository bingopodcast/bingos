
import pygame

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

meter = pygame.image.load('graphics/assets/black_register_cover.png').convert()
number = pygame.image.load('bonanza/assets/number.png').convert_alpha()
feature = pygame.image.load('bonanza/assets/feature.png').convert_alpha()
ms_letter = pygame.image.load('bonanza/assets/ms_letter.png').convert_alpha()
ms_arrow = pygame.image.load('bonanza/assets/ms_arrow.png').convert_alpha()
select_now = pygame.image.load('bonanza/assets/select_now.png').convert_alpha()
corners = pygame.image.load('bonanza/assets/feature.png').convert_alpha()
ballyhole = pygame.image.load('bonanza/assets/feature.png').convert_alpha()
odds = pygame.image.load('bonanza/assets/odds.png').convert_alpha()
tilt = pygame.image.load('bonanza/assets/tilt.png').convert_alpha()
time = pygame.image.load('bonanza/assets/feature.png').convert_alpha()
s_arrow = pygame.image.load('bonanza/assets/s_arrow.png').convert_alpha()
a0 = pygame.image.load('bonanza/assets/a0.png').convert_alpha()
a1 = pygame.image.load('bonanza/assets/a1.png').convert_alpha()
a2 = pygame.image.load('bonanza/assets/a2.png').convert_alpha()
a3 = pygame.image.load('bonanza/assets/a3.png').convert_alpha()
b0 = pygame.image.load('bonanza/assets/b0.png').convert_alpha()
b1 = pygame.image.load('bonanza/assets/b1.png').convert_alpha()
b2 = pygame.image.load('bonanza/assets/b2.png').convert_alpha()
b3 = pygame.image.load('bonanza/assets/b3.png').convert_alpha()
c0 = pygame.image.load('bonanza/assets/c0.png').convert_alpha()
c1 = pygame.image.load('bonanza/assets/c1.png').convert_alpha()
c2 = pygame.image.load('bonanza/assets/c2.png').convert_alpha()
c3 = pygame.image.load('bonanza/assets/c3.png').convert_alpha()
d0 = pygame.image.load('bonanza/assets/d0.png').convert_alpha()
d1 = pygame.image.load('bonanza/assets/d1.png').convert_alpha()
d2 = pygame.image.load('bonanza/assets/d2.png').convert_alpha()
d3 = pygame.image.load('bonanza/assets/d3.png').convert_alpha()
e0 = pygame.image.load('bonanza/assets/e0.png').convert_alpha()
bg_menu = pygame.image.load('bonanza/assets/bonanza_menu.png')
bg_gi = pygame.image.load('bonanza/assets/bonanza_gi.png')
bg_off = pygame.image.load('bonanza/assets/bonanza_off.png')
 
class scorereel():
    """ Score Reels are used to count replays """
    def __init__(self, pos, image):
        self.position = pos
        self.default_y = self.position[1]
        self.image = pygame.image.load(image).convert()

reel1 = scorereel([112,808], "graphics/assets/white_reel.png")
reel10 = scorereel([93,808], "graphics/assets/white_reel.png")
reel100 = scorereel([74,808], "graphics/assets/white_reel.png")
reel1000 = scorereel([55,808], "graphics/assets/white_reel.png")

def display(s, replays=0, menu=False):
    
    meter.set_colorkey((255,0,252))
    meter_position = [45,808]

    screen.blit(reel1.image, reel1.position)
    screen.blit(reel10.image, reel10.position)
    screen.blit(reel100.image, reel100.position)
    screen.blit(reel1000.image, reel1000.position)
    screen.blit(meter, meter_position)

    if s.game.square_a.position == 0:
        p = [220,362]
        screen.blit(a0, p)
    if s.game.square_a.position == 1:
        p = [220,362]
        screen.blit(a1, p)
    if s.game.square_a.position == 2:
        p = [220,362]
        screen.blit(a2, p)
    if s.game.square_a.position == 3:
        p = [220,362]
        screen.blit(a3, p)
    if s.game.square_b.position == 0:
        p = [226,530]
        screen.blit(b0, p)
    if s.game.square_b.position == 1:
        p = [226,530]
        screen.blit(b1, p)
    if s.game.square_b.position == 2:
        p = [226,530]
        screen.blit(b2, p)
    if s.game.square_b.position == 3:
        p = [226,530]
        screen.blit(b3, p)
    if s.game.square_c.position == 0:
        p = [384,362]
        screen.blit(c0, p)
    if s.game.square_c.position == 1:
        p = [384,364]
        screen.blit(c1, p)
    if s.game.square_c.position == 2:
        p = [384,364]
        screen.blit(c2, p)
    if s.game.square_c.position == 3:
        p = [384,364]
        screen.blit(c3, p)
    if s.game.square_d.position == 0:
        p = [387,533]
        screen.blit(d0, p)
    if s.game.square_d.position == 1:
        p = [387,533]
        screen.blit(d1, p)
    if s.game.square_d.position == 2:
        p = [387,533]
        screen.blit(d2, p)
    if s.game.square_d.position == 3:
        p = [387,533]
        screen.blit(d3, p)
    if s.game.square_e.position == 0 or s.game.square_e.position == 2:
        p = [328,310]
        screen.blit(e0, p)
    elif s.game.square_e.position == 1:
        p = [328,364]
        screen.blit(e0, p)
    elif s.game.square_e.position == 3:
        p = [328,260]
        screen.blit(e0, p)


    backglass_position = [0, 0]
    backglass = pygame.Surface(screen.get_size(), flags=pygame.SRCALPHA)
    backglass.fill((0, 0, 0))
    if menu == True:
        screen.blit(bg_menu, backglass_position)
    else:
        if (s.game.anti_cheat.status == True):
            screen.blit(bg_gi, backglass_position)
        else:
            screen.blit(bg_off, backglass_position)

    if s.game.tilt.status == False:
        if s.holes:
            if 1 in s.holes:
                if s.game.square_a.position == 0:
                    p = [222,422]
                    screen.blit(number, p)
                elif s.game.square_a.position == 1:
                    p = [222,365]
                    screen.blit(number, p)
                elif s.game.square_a.position == 2:
                    p = [277,365]
                    screen.blit(number, p)
                else:
                    p = [277,423]
                    screen.blit(number, p)
            if 2 in s.holes:
                p = [441,480]
                screen.blit(number, p)
            if 3 in s.holes:
                if s.game.square_d.position == 0:
                    p = [387,534]
                    screen.blit(number, p)
                elif s.game.square_d.position == 1:
                    p = [441,535]
                    screen.blit(number, p)
                elif s.game.square_d.position == 2:
                    p = [442,592]
                    screen.blit(number, p)
                else:
                    p = [388,590]
                    screen.blit(number, p)
            if 4 in s.holes:
                if s.game.square_a.position == 0:
                    p = [277,368]
                    screen.blit(number, p)
                elif s.game.square_a.position == 1:
                    p = [277,424]
                    screen.blit(number, p)
                elif s.game.square_a.position == 2:
                    p = [224,422]
                    screen.blit(number, p)
                else:
                    p = [223,367]
                    screen.blit(number, p)
            if 5 in s.holes:
                if s.game.square_e.position == 0 or s.game.square_e.position == 2:
                    p = [334,590]
                    screen.blit(number, p)
                elif s.game.square_e.position == 1:
                    p = [331,367]
                    screen.blit(number, p)
                elif s.game.square_e.position == 3:
                    p = [333,534]
                    screen.blit(number, p)
            if 6 in s.holes:
                if s.game.square_c.position == 0:
                    p = [440,368]
                    screen.blit(number, p)
                elif s.game.square_c.position == 1:
                    p = [439,425]
                    screen.blit(number, p)
                elif s.game.square_c.position == 2:
                    p = [386,424]
                    screen.blit(number, p)
                else:
                    p = [386,367]
                    screen.blit(number, p)
            if 7 in s.holes:
                if s.game.square_d.position == 0:
                    p = [442,592]
                    screen.blit(number, p)
                elif s.game.square_d.position == 1:
                    p = [387,590]
                    screen.blit(number, p)
                elif s.game.square_d.position == 2:
                    p = [387,533]
                    screen.blit(number, p)
                else:
                    p = [440,534]
                    screen.blit(number, p)
            if 8 in s.holes:
                if s.game.square_c.position == 0:
                    p = [385,366]
                    screen.blit(number, p)
                elif s.game.square_c.position == 1:
                    p = [439,368]
                    screen.blit(number, p)
                elif s.game.square_c.position == 2:
                    p = [439,425]
                    screen.blit(number, p)
                else:
                    p = [385,423]
                    screen.blit(number, p)
            if 9 in s.holes:
                if s.game.square_a.position == 0:
                    p = [278,425]
                    screen.blit(number, p)
                elif s.game.square_a.position == 1:
                    p = [223,423]
                    screen.blit(number, p)
                elif s.game.square_a.position == 2:
                    p = [223,366]
                    screen.blit(number, p)
                else:
                    p = [277,367]
                    screen.blit(number, p)
            if 10 in s.holes:
                if s.game.square_b.position == 0:
                    p = [224,590]
                    screen.blit(number, p)
                elif s.game.square_b.position == 1:
                    p = [225,533]
                    screen.blit(number, p)
                elif s.game.square_b.position == 2:
                    p = [278,534]
                    screen.blit(number, p)
                else:
                    p = [279,590]
                    screen.blit(number, p)
            if 11 in s.holes:
                p = [225,479]
                screen.blit(number, p)
            if 12 in s.holes:
                p = [387,481]
                screen.blit(number, p)
            if 13 in s.holes:
                if s.game.square_e.position == 0 or s.game.square_e.position == 2:
                    p = [333,534]
                    screen.blit(number, p)
                if s.game.square_e.position == 1:
                    p = [333,589]
                    screen.blit(number, p)
                elif s.game.square_e.position == 3:
                    p = [332,479]
                    screen.blit(number, p)
            if 14 in s.holes:
                if s.game.square_c.position == 0:
                    p = [439,424]
                    screen.blit(number, p)
                elif s.game.square_c.position == 1:
                    p = [386,424]
                    screen.blit(number, p)
                elif s.game.square_c.position == 2:
                    p = [385,367]
                    screen.blit(number, p)
                else:
                    p = [440,369]
                    screen.blit(number, p)
            if 15 in s.holes:
                if s.game.square_b.position == 0:
                    p = [279,591]
                    screen.blit(number, p)
                if s.game.square_b.position == 1:
                    p = [224,590]
                    screen.blit(number, p)
                if s.game.square_b.position == 2:
                    p = [224,532]
                    screen.blit(number, p)
                if s.game.square_b.position == 3:
                    p = [278,534]
                    screen.blit(number, p)
            if 16 in s.holes:
                if s.game.square_e.position == 0 or s.game.square_e.position == 2:
                    p = [332,479]
                    screen.blit(number, p)
                elif s.game.square_e.position == 1:
                    p = [333,534]
                    screen.blit(number, p)
                elif s.game.square_e.position == 3:
                    p = [332,422]
                    screen.blit(number, p)
            if 17 in s.holes:
                if s.game.square_d.position == 0:
                    p = [441,535]
                    screen.blit(number, p)
                elif s.game.square_d.position == 1:
                    p = [442,591]
                    screen.blit(number, p)
                elif s.game.square_d.position == 2:
                    p = [387,590]
                    screen.blit(number, p)
                elif s.game.square_d.position == 3:
                    p = [388,533]
                    screen.blit(number, p)
            if 18 in s.holes:
                p = [279,480]
                screen.blit(number, p)
            if 19 in s.holes:
                if s.game.square_a.position == 0:
                    p = [224,367]
                    screen.blit(number, p)
                elif s.game.square_a.position == 1:
                    p = [278,367]
                    screen.blit(number, p)
                elif s.game.square_a.position == 2:
                    p = [278,423]
                    screen.blit(number, p)
                else:
                    p = [223,422]
                    screen.blit(number, p)
            if 20 in s.holes:
                if s.game.square_c.position == 0:
                    p = [386,423]
                    screen.blit(number, p)
                elif s.game.square_c.position == 1:
                    p = [385,367]
                    screen.blit(number, p)
                elif s.game.square_e.position == 2:
                    p = [440,368]
                    screen.blit(number, p)
                elif s.game.square_e.position == 3:
                    p = [440,425]
                    screen.blit(number, p)
            if 21 in s.holes:
                if s.game.square_d.position == 0:
                    p = [388,590]
                    screen.blit(number, p)
                elif s.game.square_d.position == 1:
                    p = [387,534]
                    screen.blit(number, p)
                elif s.game.square_d.position == 2:
                    p = [441,534]
                    screen.blit(number, p)
                else:
                    p = [442,592]
                    screen.blit(number, p)
            if 22 in s.holes:
                if s.game.square_b.position == 0:
                    p = [225,533]
                    screen.blit(number, p)
                elif s.game.square_b.position == 1:
                    p = [278,534]
                    screen.blit(number, p)
                elif s.game.square_b.position == 2:
                    p = [279,590]
                    screen.blit(number, p)
                else:
                    p = [224,590]
                    screen.blit(number, p)
            if 23 in s.holes:
                if s.game.square_b.position == 0:
                    p = [278,535]
                    screen.blit(number, p)
                elif s.game.square_b.position == 1:
                    p = [281,590]
                    screen.blit(number, p)
                elif s.game.square_b.position == 2:
                    p = [224,589]
                    screen.blit(number, p)
                else:
                    p = [224,532]
                    screen.blit(number, p)
            if 24 in s.holes:
                if s.game.square_e.position == 0 or s.game.square_e.position == 2:
                    p = [333,423]
                    screen.blit(number, p)
                elif s.game.square_e.position == 1:
                    p = [332,479]
                    screen.blit(number, p)
                elif s.game.square_e.position == 3:
                    p = [331,368]
                    screen.blit(number, p)
            if 25 in s.holes:
                if s.game.square_e.position == 0 or s.game.square_e.position == 2:
                    p = [331,368]
                    screen.blit(number, p)
                elif s.game.square_e.position == 1:
                    p = [333,423]
                    screen.blit(number, p)
                elif s.game.square_e.position == 2:
                    p = [334,591]
                    screen.blit(number, p)


    if s.game.magic_squares_feature.position == 1:
        p = [190,704]
        screen.blit(ms_arrow, p)
    if s.game.magic_squares_feature.position >= 2:
        p = [235,704]
        screen.blit(ms_letter, p)
    if s.game.magic_squares_feature.position == 3:
        p = [278,704]
        screen.blit(ms_arrow, p)
    if s.game.magic_squares_feature.position >= 4:
        p = [323,704]
        screen.blit(ms_letter, p)
    if s.game.magic_squares_feature.position == 5:
        p = [360,704]
        screen.blit(ms_arrow, p)
    if s.game.magic_squares_feature.position >= 6:
        p = [411,704]
        screen.blit(ms_letter, p)
    if s.game.magic_squares_feature.position == 7:
        p = [455,704]
        screen.blit(ms_arrow, p)
    if s.game.magic_squares_feature.position >= 8:
        p = [499,704]
        screen.blit(ms_letter, p)
    if s.game.magic_line.status == True:
        p = [343,653]
        screen.blit(ms_letter, p)
        p = [16,580]
        screen.blit(feature, p)

    sf = s.game.selection_feature.position 
    if s.game.magic_squares_feature.position >= 2 or s.game.magic_line.status == True:
        if sf <= 2:
            p = [586,582]
            screen.blit(feature, p)
            if sf == 2:
                p = [627,533]
                screen.blit(s_arrow, p)
            if s.game.ball_count.position == 3:
                s.cancel_delayed(name="blink")
                blink([s,1,1])
            else:
                s.cancel_delayed(name="blink")
        if sf == 3 or sf == 4:
            p = [585,466]
            screen.blit(feature, p)
            if sf == 4:
                p = [625,420]
                screen.blit(s_arrow, p)
            if s.game.ball_count.position == 4:
                s.cancel_delayed(name="blink")
                blink([s,1,1])
            else:
                s.cancel_delayed(name="blink")
        if sf == 5:
            p = [585,355]
            screen.blit(feature, p)
            if s.game.ball_count.position == 5:
                s.cancel_delayed(name="blink")
                blink([s,1,1])
            else:
                s.cancel_delayed(name="blink")

    if s.game.corners.status == True:
        p = [14,467]
        screen.blit(feature, p)
    if s.game.corners2.status == True:
        p = [15,355]
        screen.blit(feature, p)

    if s.game.red_odds.position == 1:
        p = [188,812]
        screen.blit(odds, p)
    elif s.game.red_odds.position == 2:
        p = [225,812]
        screen.blit(odds, p)
    elif s.game.red_odds.position == 3:
        p = [262,812]
        screen.blit(odds, p)
    elif s.game.red_odds.position == 4:
        p = [298,812]
        screen.blit(odds, p)
    elif s.game.red_odds.position == 5:
        p = [337,812]
        screen.blit(odds, p)
    elif s.game.red_odds.position == 6:
        p = [369,811]
        screen.blit(odds, p)
    elif s.game.red_odds.position == 7:
        p = [412,811]
        screen.blit(odds, p)
    elif s.game.red_odds.position == 8:
        p = [453,811]
        screen.blit(odds, p)
    elif s.game.red_odds.position == 9:
        p = [499,811]
        screen.blit(odds, p)
    elif s.game.red_odds.position == 10:
        p = [544,812]
        screen.blit(odds, p)
    elif s.game.red_odds.position == 11:
        p = [592,811]
        screen.blit(odds, p)
    elif s.game.red_odds.position == 12:
        p = [638,811]
        screen.blit(odds, p)

    if s.game.green_odds.position == 1:
        p = [188,876]
        screen.blit(odds, p)
    elif s.game.green_odds.position == 2:
        p = [225,876]
        screen.blit(odds, p)
    elif s.game.green_odds.position == 3:
        p = [262,876]
        screen.blit(odds, p)
    elif s.game.green_odds.position == 4:
        p = [298,876]
        screen.blit(odds, p)
    elif s.game.green_odds.position == 5:
        p = [337,876]
        screen.blit(odds, p)
    elif s.game.green_odds.position == 6:
        p = [369,876]
        screen.blit(odds, p)
    elif s.game.green_odds.position == 7:
        p = [412,876]
        screen.blit(odds, p)
    elif s.game.green_odds.position == 8:
        p = [453,876]
        screen.blit(odds, p)
    elif s.game.green_odds.position == 9:
        p = [499,876]
        screen.blit(odds, p)
    elif s.game.green_odds.position == 10:
        p = [544,876]
        screen.blit(odds, p)
    elif s.game.green_odds.position == 11:
        p = [592,876]
        screen.blit(odds, p)
    elif s.game.green_odds.position == 12:
        p = [638,876]
        screen.blit(odds, p)

    if s.game.yellow_odds.position == 1:
        p = [188,941]
        screen.blit(odds, p)
    elif s.game.yellow_odds.position == 2:
        p = [225,941]
        screen.blit(odds, p)
    elif s.game.yellow_odds.position == 3:
        p = [262,941]
        screen.blit(odds, p)
    elif s.game.yellow_odds.position == 4:
        p = [298,941]
        screen.blit(odds, p)
    elif s.game.yellow_odds.position == 5:
        p = [337,941]
        screen.blit(odds, p)
    elif s.game.yellow_odds.position == 6:
        p = [369,941]
        screen.blit(odds, p)
    elif s.game.yellow_odds.position == 7:
        p = [412,941]
        screen.blit(odds, p)
    elif s.game.yellow_odds.position == 8:
        p = [453,941]
        screen.blit(odds, p)
    elif s.game.yellow_odds.position == 9:
        p = [499,941]
        screen.blit(odds, p)
    elif s.game.yellow_odds.position == 10:
        p = [544,941]
        screen.blit(odds, p)
    elif s.game.yellow_odds.position == 11:
        p = [592,941]
        screen.blit(odds, p)
    elif s.game.yellow_odds.position == 12:
        p = [638,941]
        screen.blit(odds, p)

    if s.game.blue_odds.position == 1:
        p = [188,1005]
        screen.blit(odds, p)
    elif s.game.blue_odds.position == 2:
        p = [225,1005]
        screen.blit(odds, p)
    elif s.game.blue_odds.position == 3:
        p = [262,1005]
        screen.blit(odds, p)
    elif s.game.blue_odds.position == 4:
        p = [298,1005]
        screen.blit(odds, p)
    elif s.game.blue_odds.position == 5:
        p = [337,1005]
        screen.blit(odds, p)
    elif s.game.blue_odds.position == 6:
        p = [369,1005]
        screen.blit(odds, p)
    elif s.game.blue_odds.position == 7:
        p = [412,1005]
        screen.blit(odds, p)
    elif s.game.blue_odds.position == 8:
        p = [453,1005]
        screen.blit(odds, p)
    elif s.game.blue_odds.position == 9:
        p = [499,1005]
        screen.blit(odds, p)
    elif s.game.blue_odds.position == 10:
        p = [544,1005]
        screen.blit(odds, p)
    elif s.game.blue_odds.position == 11:
        p = [592,1005]
        screen.blit(odds, p)
    elif s.game.blue_odds.position == 12:
        p = [638,1005]
        screen.blit(odds, p)

    if s.game.tilt.status == True:
        tilt_position = [47,950]
        screen.blit(tilt, tilt_position)

    pygame.display.update()

def blink(args):
    dirty_rects = []
    s = args[0]
    b = args[1]
    sn = args[2]

    if b == 0:
        if sn == 1:
            p = [546,705]
            dirty_rects.append(screen.blit(select_now, p))
        pygame.display.update(dirty_rects)
    else:
        dirty_rects.append(screen.blit(bg_gi, (546,705), pygame.Rect(546,705,108,37)))
        pygame.display.update(dirty_rects)
    b = not b

    args = [s,b,sn]

    s.delay(name="blink", delay=0.1, handler=blink, param=args)

def clear_odds(s, num):
    global screen

    dirty_rects = []

    dirty_rects.append(screen.blit(bg_gi, (191,769), pygame.Rect(191,769,39,39)))
    dirty_rects.append(screen.blit(bg_gi, (256,770), pygame.Rect(256,770,39,39)))
    dirty_rects.append(screen.blit(bg_gi, (322,770), pygame.Rect(322,770,39,39)))
    dirty_rects.append(screen.blit(bg_gi, (387,770), pygame.Rect(387,770,39,39)))
    dirty_rects.append(screen.blit(bg_gi, (452,770), pygame.Rect(452,770,39,39)))
    dirty_rects.append(screen.blit(bg_gi, (519,770), pygame.Rect(519,770,39,39)))
    dirty_rects.append(screen.blit(bg_gi, (582,770), pygame.Rect(582,770,39,39)))
    dirty_rects.append(screen.blit(bg_gi, (647,770), pygame.Rect(647,770,39,39)))

    pygame.display.update(dirty_rects)

def draw_odds_animation(s, num):
    global screen
    dirty_rects = []

    if num in range(0,11):
        p = [191,769]
        dirty_rects.append(screen.blit(ms_arrow, p))
        pygame.display.update(dirty_rects)
        return
    if num in range(11,21):
        p = [256,770]
        dirty_rects.append(screen.blit(ms_arrow, p))
        pygame.display.update(dirty_rects)
        return
    if num in range(21,31):
        p = [322,770]
        dirty_rects.append(screen.blit(ms_arrow, p))
        pygame.display.update(dirty_rects)
        return
    if num in range(31,41):
        p = [387,770]
        dirty_rects.append(screen.blit(ms_arrow, p))
        pygame.display.update(dirty_rects)
        return
    if num in range(41,50):
        p = [452,770]
        dirty_rects.append(screen.blit(ms_arrow, p))
        pygame.display.update(dirty_rects)
        return
    if num in range(0,11):
        p = [519,770]
        dirty_rects.append(screen.blit(ms_arrow, p))
        pygame.display.update(dirty_rects)
        return
    if num in range(11,21):
        p = [582,770]
        dirty_rects.append(screen.blit(ms_arrow, p))
        pygame.display.update(dirty_rects)
        return
    if num in range(21,31):
        p = [647,770]
        dirty_rects.append(screen.blit(ms_arrow, p))
        pygame.display.update(dirty_rects)
        return

def odds_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]

    clear_odds(s, num)

    draw_odds_animation(s, num)

def clear_features(s, num):
    global screen

    dirty_rects = []
   
    if s.game.selection_feature.position not in [3,4]:
        dirty_rects.append(screen.blit(bg_gi, (585,466), pygame.Rect(585,466,115,59)))
    if s.game.selection_feature.position < 5:
        dirty_rects.append(screen.blit(bg_gi, (585,355), pygame.Rect(585,355,115,59)))
    if s.game.magic_squares_feature.position < 2:
        dirty_rects.append(screen.blit(bg_gi, (235,704), pygame.Rect(235,704,40,37)))
    if s.game.magic_squares_feature.position < 4:
        dirty_rects.append(screen.blit(bg_gi, (323,704), pygame.Rect(323,704,40,37)))
    if s.game.magic_squares_feature.position < 6:
        dirty_rects.append(screen.blit(bg_gi, (411,704), pygame.Rect(411,704,40,37)))
    if s.game.magic_squares_feature.position < 8:
        dirty_rects.append(screen.blit(bg_gi, (499,704), pygame.Rect(499,704,40,37)))
    if s.game.magic_line.status == False:
        dirty_rects.append(screen.blit(bg_gi, (343,653), pygame.Rect(343,653,40,37)))
    if s.game.corners.status == False: 
        dirty_rects.append(screen.blit(bg_gi, (14,467), pygame.Rect(14,467,115,59)))
    if s.game.corners2.status == False: 
        dirty_rects.append(screen.blit(bg_gi, (15,355), pygame.Rect(15,355,115,59)))

    pygame.display.update(dirty_rects)


def draw_feature_animation(s, num):
    global screen
    dirty_rects = []
 
    if num in [19,30,5,44]:
        if s.game.selection_feature.position not in [3,4]:
            p = [585,466]
            dirty_rects.append(screen.blit(feature, p))
            pygame.display.update(dirty_rects)
            return
    if num in [10,39,35,14]:
        if s.game.selection_feature.position < 5:
            p = [585,355]
            dirty_rects.append(screen.blit(feature, p))
            pygame.display.update(dirty_rects)
            return
    if num in [7,16,14,22,23,40,48,49,32,41,39,47]:
        if s.game.magic_squares_feature.position < 2:
            p = [235,704]
            dirty_rects.append(screen.blit(ms_letter, p))
            pygame.display.update(dirty_rects)
            return
    if num in [44,19,11,36,32,7]:
        if s.game.magic_squares_feature.position < 4:
            p = [323,704]
            dirty_rects.append(screen.blit(ms_letter, p))
            pygame.display.update(dirty_rects)
            return
    if num in [25,50,34,9,1,26,38,13]:
        if s.game.magic_squares_feature.position < 6:
            p = [411,704]
            dirty_rects.append(screen.blit(ms_letter, p))
            pygame.display.update(dirty_rects)
            return
    if num in [14,39,18,43]:
        if s.game.magic_squares_feature.position < 8:
            p = [499,704]
            dirty_rects.append(screen.blit(ms_letter, p))
            pygame.display.update(dirty_rects)
            return
    if num in [44,19]:
        if s.game.magic_line.status == False:
            p = [343,653]
            dirty_rects.append(screen.blit(ms_letter, p))
            pygame.display.update(dirty_rects)
            return
    if num in [1,26]:
        if s.game.corners.status == False: 
            p = [14,467]
            dirty_rects.append(screen.blit(feature, p))
            pygame.display.update(dirty_rects)
            return
    if num in [9,34,18,43,27,2]:
        if s.game.corners2.status == False: 
            p = [15,355]
            dirty_rects.append(screen.blit(feature, p))
            pygame.display.update(dirty_rects)
            return

def feature_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]

    clear_features(s, num)

    draw_feature_animation(s, num)

def both_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]

    clear_features(s, num)
    clear_odds(s, num)

    draw_odds_animation(s, num)
    draw_feature_animation(s, num)


