
import pygame
import random

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

meter = pygame.image.load('graphics/assets/register_cover.png').convert()
eb = pygame.image.load('gay_time/assets/eb.png').convert_alpha()
ebs = pygame.image.load('gay_time/assets/extra_balls.png').convert_alpha()
number_eb = pygame.image.load('gay_time/assets/eb_number.png').convert_alpha()
o1 = pygame.image.load('gay_time/assets/odds1.png').convert_alpha()
o2 = pygame.image.load('gay_time/assets/odds2.png').convert_alpha()
o3 = pygame.image.load('gay_time/assets/odds3.png').convert_alpha()
o4 = pygame.image.load('gay_time/assets/odds4.png').convert_alpha()
o5 = pygame.image.load('gay_time/assets/odds5.png').convert_alpha()
o6 = pygame.image.load('gay_time/assets/odds6.png').convert_alpha()
o7 = pygame.image.load('gay_time/assets/odds7.png').convert_alpha()
o8 = pygame.image.load('gay_time/assets/odds8.png').convert_alpha()
o9 = pygame.image.load('gay_time/assets/odds9.png').convert_alpha()
o10 = pygame.image.load('gay_time/assets/odds10.png').convert_alpha()
c = pygame.image.load('gay_time/assets/corners.png').convert_alpha()
m = pygame.image.load('gay_time/assets/pockets.png').convert_alpha()
number = pygame.image.load('gay_time/assets/number.png').convert_alpha()
tilt = pygame.image.load('gay_time/assets/tilt.png').convert_alpha()
magic_arrow = pygame.image.load('gay_time/assets/magic_arrow.png').convert_alpha()
magic_line = pygame.image.load('gay_time/assets/magic_line.png').convert_alpha()
magic_line2 = pygame.image.load('gay_time/assets/magic_line2.png').convert_alpha()
select_now = pygame.image.load('gay_time/assets/select_now.png').convert_alpha()
pockets_now = pygame.image.load('gay_time/assets/pockets_now.png').convert_alpha()
line1 = pygame.image.load('gay_time/assets/line1.png').convert_alpha()
line2 = pygame.image.load('gay_time/assets/line2.png').convert_alpha()
line3 = pygame.image.load('gay_time/assets/line3.png').convert_alpha()
line4 = pygame.image.load('gay_time/assets/line4.png').convert_alpha()
three_as_four = pygame.image.load('gay_time/assets/three_as_four.png').convert_alpha()
spotted = pygame.image.load('gay_time/assets/spotted.png').convert_alpha()
bg_menu = pygame.image.load('gay_time/assets/gay_time_menu.png').convert()
bg_menu.set_colorkey((255,0,252))
bg_gi = pygame.image.load('gay_time/assets/gay_time_gi.png').convert_alpha()
bg_off = pygame.image.load('gay_time/assets/gay_time_off.png').convert()
bg_off.set_colorkey((255,0,252))

class scorereel():
    """ Score Reels are used to count replays """
    def __init__(self, pos, image):
        self.position = pos
        self.default_y = self.position[1]
        self.image = pygame.image.load(image).convert()

reel1 = scorereel([98,300], "graphics/assets/green_reel.png")
reel10 = scorereel([79,300], "graphics/assets/green_reel.png")
reel100 = scorereel([61,300], "graphics/assets/green_reel.png")

def display(s, replays=0, menu=False):
    
    meter.set_colorkey((255,0,252))
    meter_position = [51,300]

    screen.blit(reel1.image, reel1.position)
    screen.blit(reel10.image, reel10.position)
    screen.blit(reel100.image, reel100.position)
    screen.blit(meter, meter_position)

    if s.game.line1.position in [0,2]:
        line1_position = [227,344]
    elif s.game.line1.position == 1:
        line1_position = [227,399]
    elif s.game.line1.position == 3:
        line1_position = [227,289]
    
    screen.blit(line1, line1_position)

    if s.game.line2.position in [0,2]:
        line2_position = [280,344]
    elif s.game.line2.position == 1:
        line2_position = [280,399]
    elif s.game.line2.position == 3:
        line2_position = [280,289]
    
    screen.blit(line2, line2_position)

    if s.game.line3.position in [0,2]:
        line3_position = [333,344]
    elif s.game.line3.position == 1:
        line3_position = [333,399]
    elif s.game.line3.position == 3:
        line3_position = [333,289]
    
    screen.blit(line3, line3_position)

    if s.game.line4.position in [0,2]:
        line4_position = [387,344]
    elif s.game.line4.position == 1:
        line4_position = [387,399]
    elif s.game.line4.position == 3:
        line4_position = [387,289]

    screen.blit(line4, line4_position)

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

    if s.game.extra_ball.position >= 1:
        eb_position = [140,1016]
        screen.blit(number_eb, eb_position)
    if s.game.extra_ball.position >= 2:
        eb_position = [185,1016]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 3:
        eb_position = [253,1016]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 4:
        eb_position = [326,1016]
        screen.blit(number_eb, eb_position)
    if s.game.extra_ball.position >= 5:
        eb_position = [375,1016]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 6:
        eb_position = [442,1016]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 7:
        eb_position = [512,1016]
        screen.blit(number_eb, eb_position)
    if s.game.extra_ball.position >= 8:
        eb_position = [564,1016]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 9:
        eb_position = [630,1016]
        screen.blit(eb, eb_position)
    
    
    if s.game.odds.position > 0:
        if s.game.odds.position == 1:
            odds_position = [21,889]
            screen.blit(o1, odds_position)
        if s.game.odds.position == 2:
            odds_position = [104,846]
            screen.blit(o2, odds_position)
        if s.game.odds.position == 3:
            odds_position = [174,844]
            screen.blit(o3, odds_position)
        if s.game.odds.position == 4:
            odds_position = [234,871]
            screen.blit(o4, odds_position)
        if s.game.odds.position == 5:
            odds_position = [292,850]
            screen.blit(o5, odds_position)
        if s.game.odds.position == 6:
            odds_position = [365,847]
            screen.blit(o6, odds_position)
        if s.game.odds.position == 7:
            odds_position = [424,880]
            screen.blit(o7, odds_position)
        if s.game.odds.position == 8:
            odds_position = [470,851]
            screen.blit(o8, odds_position)
        if s.game.odds.position == 9:
            odds_position = [568,852]
            screen.blit(o9, odds_position)
        if s.game.odds.position == 10:
            odds_position = [620,880]
            screen.blit(o10, odds_position)

    if s.game.corners.status == True:
        corners_position = [72,456]
        screen.blit(c, corners_position)


    if s.game.tilt.status == False:
        if s.holes:
            if 1 in s.holes:
                if s.game.line1.position in [0,2]:
                    number_position = [339,565]
                    screen.blit(number, number_position)
                elif s.game.line1.position == 1:
                    number_position = [339,618]
                    screen.blit(number, number_position)
                elif s.game.line1.position == 3:
                    number_position = [337,509]
                    screen.blit(number, number_position)
            if 2 in s.holes:
                if s.game.line1.position in [0,2]:
                    number_position = [230,507]
                    screen.blit(number, number_position)
                elif s.game.line1.position == 1:
                    number_position = [230,564]
                    screen.blit(number, number_position)
                elif s.game.line1.position == 3:
                    number_position = [230,453]
                    screen.blit(number, number_position)
            if 3 in s.holes:
                number_position = [444,617]
                screen.blit(number, number_position)
            if 4 in s.holes:
                if s.game.line2.position in [0,2]:
                    number_position = [282,400]
                    screen.blit(number, number_position)
                elif s.game.line2.position == 1:
                    number_position = [282,456]
                    screen.blit(number, number_position)
                elif s.game.line2.position == 3:
                    number_position = [282,618]
                    screen.blit(number, number_position)
            if 5 in s.holes:
                if s.game.line3.position in [0,2]:
                    number_position = [338,618]
                    screen.blit(number, number_position)
                elif s.game.line3.position == 1:
                    number_position = [338,400]
                    screen.blit(number, number_position)
                elif s.game.line3.position == 3:
                    number_position = [338,564]
                    screen.blit(number, number_position)
            if 6 in s.holes:
                number_position = [443,454]
                screen.blit(number, number_position)
            if 7 in s.holes:
                if s.game.line2.position in [0,2]:
                    number_position = [285,618]
                    screen.blit(number, number_position)
                elif s.game.line2.position == 1:
                    number_position = [285,400]
                    screen.blit(number, number_position)
                elif s.game.line2.position == 3:
                    number_position = [285,564]
                    screen.blit(number, number_position)
            if 8 in s.holes:
                number_position = [442,401]
                screen.blit(number, number_position)
            if 9 in s.holes:
                if s.game.line1.position in [0,2]:
                    number_position = [228,402]
                    screen.blit(number, number_position)
                elif s.game.line1.position == 1:
                    number_position = [228,454]
                    screen.blit(number, number_position)
                elif s.game.line1.position == 3:
                    number_position = [230,618]
                    screen.blit(number, number_position)
            if 10 in s.holes:
                if s.game.line1.position in [0,2]:
                    number_position = [228,454]
                    screen.blit(number, number_position)
                elif s.game.line1.position == 1:
                    number_position = [228,508]
                    screen.blit(number, number_position)
                elif s.game.line1.position == 3:
                    number_position = [228,402]
                    screen.blit(number, number_position)
            if 11 in s.holes:
                if s.game.line1.position in [0,2]:
                    number_position = [228,618]
                    screen.blit(number, number_position)
                elif s.game.line1.position == 1:
                    number_position = [228,399]
                    screen.blit(number, number_position)
                elif s.game.line1.position == 3:
                    number_position = [228,564]
                    screen.blit(number, number_position)
            if 12 in s.holes:
                if s.game.line4.position in [0,2]:
                    p = [389,508]
                    screen.blit(number, p)
                elif s.game.line4.position == 1:
                    p = [389,563]
                    screen.blit(number, p)
                elif s.game.line4.position == 3:
                    p = [389,451]
                    screen.blit(number, p)
            if 13 in s.holes:
                if s.game.line1.position in [0,2]:
                    number_position = [230,564]
                    screen.blit(number, number_position)
                elif s.game.line1.position == 1:
                    number_position = [230,618]
                    screen.blit(number, number_position)
                elif s.game.line1.position == 3:
                    number_position = [228,509]
                    screen.blit(number, number_position)
            if 14 in s.holes:
                if s.game.line3.position in [0,2]:
                    number_position = [337,455]
                    screen.blit(number, number_position)
                elif s.game.line3.position == 1:
                    number_position = [337,510]
                    screen.blit(number, number_position)
                elif s.game.line3.position == 3:
                    number_position = [337,400]
                    screen.blit(number, number_position)
            if 15 in s.holes:
                if s.game.line3.position in [0,2]:
                    number_position = [337,400]
                    screen.blit(number, number_position)
                elif s.game.line3.position == 1:
                    number_position = [337,455]
                    screen.blit(number, number_position)
                elif s.game.line3.position == 3:
                    number_position = [337,618]
                    screen.blit(number, number_position)
            if 16 in s.holes:
                if s.game.line3.position in [0,2]:
                    number_position = [337,509]
                    screen.blit(number, number_position)
                elif s.game.line3.position == 1:
                    number_position = [337,564]
                    screen.blit(number, number_position)
                elif s.game.line3.position == 3:
                    number_position = [337,454]
                    screen.blit(number, number_position)
            if 17 in s.holes:
                number_position = [442,562]
                screen.blit(number, number_position)
            if 18 in s.holes:
                if s.game.line2.position in [0,2]:
                    number_position = [282,510]
                    screen.blit(number, number_position)
                elif s.game.line2.position == 1:
                    number_position = [282,564]
                    screen.blit(number, number_position)
                elif s.game.line2.position == 3:
                    number_position = [282,454]
                    screen.blit(number, number_position)
            if 19 in s.holes:
                if s.game.line2.position in [0,2]:
                    number_position = [282,455]
                    screen.blit(number, number_position)
                elif s.game.line2.position == 1:
                    number_position = [282,508]
                    screen.blit(number, number_position)
                elif s.game.line2.position == 3:
                    number_position = [282,400]
                    screen.blit(number, number_position)
            if 20 in s.holes:
                if s.game.line4.position in [0,2]:
                    p = [389,450]
                    screen.blit(number, p)
                elif s.game.line4.position == 1:
                    p = [389,506]
                    screen.blit(number, p)
                elif s.game.line4.position == 3:
                    p = [389,398]
                    screen.blit(number, p)
            if 21 in s.holes:
                if s.game.line4.position in [0,2]:
                    p = [389,564]
                    screen.blit(number, p)
                elif s.game.line4.position == 1:
                    p = [389,618]
                    screen.blit(number, p)
                elif s.game.line4.position == 3:
                    p = [389,507]
                    screen.blit(number, p)
            if 22 in s.holes:
                if s.game.line2.position in [0,2]:
                    number_position = [282,564]
                    screen.blit(number, number_position)
                elif s.game.line2.position == 1:
                    number_position = [282,618]
                    screen.blit(number, number_position)
                elif s.game.line2.position == 3:
                    number_position = [282,508]
                    screen.blit(number, number_position)
            if 23 in s.holes:
                if s.game.line4.position in [0,2]:
                    p = [389,616]
                    screen.blit(number, p)
                elif s.game.line4.position == 1:
                    p = [389,397]
                    screen.blit(number, p)
                elif s.game.line4.position == 3:
                    p = [389,562]
                    screen.blit(number, p)
            if 24 in s.holes:
                if s.game.line4.position in [0,2]:
                    p = [389,397]
                    screen.blit(number, p)
                elif s.game.line4.position == 1:
                    p = [389,451]
                    screen.blit(number, p)
                elif s.game.line4.position == 3:
                    p = [389,616]
                    screen.blit(number, p)
            if 25 in s.holes:
                number_position = [441,508]
                screen.blit(number, number_position)

    if s.game.tilt.status == True:
        tilt_position = [443,692]
        screen.blit(tilt, tilt_position)

    if s.game.eb_play.status == True:
        ebs_position = [23,1015]
        screen.blit(ebs, ebs_position)

    if s.game.magic_lines.position == 1:
        p = [41,803]
        screen.blit(magic_arrow, p)
    elif s.game.magic_lines.position == 2:
        p = [76,803]
        screen.blit(magic_arrow, p)
    elif s.game.magic_lines.position == 3:
        p = [111,803]
        screen.blit(magic_arrow, p)
    elif s.game.magic_lines.position == 4:
        p = [148,803]
        screen.blit(magic_arrow, p)
    elif s.game.magic_lines.position >= 5:
        p = [184,807]
        screen.blit(magic_line, p)
        if s.game.ball_count.position == 3:
            s.cancel_delayed(name="blink")
            blink([s,1,1])
        else:
            s.cancel_delayed(name="blink")
            p = [525,799]
    if s.game.magic_lines.position >= 5:
        p = [307,807]
        screen.blit(magic_line2, p)
    if s.game.magic_lines.position >= 6:
        p = [413,807]
        screen.blit(magic_line2, p)


    if s.game.magic_pockets.status == True:
        p = [29,545]
        screen.blit(m, p)
        if s.game.ball_count.position == 3:
            s.cancel_delayed(name="blink_pockets")
            blink_pockets([s,1,1])
        else:
            s.cancel_delayed("blink_pockets")
   
    if s.game.red_three_as_four.status == True:
        p = [544,527]
        screen.blit(three_as_four, p)
    if s.game.yellow_three_as_four.status == True:
        p = [543,661]
        screen.blit(three_as_four, p)

    if s.game.spot_10.status == True:
        p = [538,454]
        screen.blit(spotted, p)
    if s.game.spot_25.status == True:
        p = [617,454]
        screen.blit(spotted, p)

    pygame.display.update()

def blink_pockets(args):
    dirty_rects = []
    s = args[0]
    b = args[1]
    sn = args[2]

    if b == 1:
        if sn == 1:
            p = [28,735]
            dirty_rects.append(screen.blit(pockets_now, p))
        pygame.display.update(dirty_rects)
    else:
        dirty_rects.append(screen.blit(bg_gi, (28,735), pygame.Rect(28,735,168,50)))
        pygame.display.update(dirty_rects)
    b = not b

    args = [s,b,sn]

    s.delay(name="blink_pockets", delay=0.1, handler=blink_pockets, param=args)

def blink(args):
    dirty_rects = []
    s = args[0]
    b = args[1]
    sn = args[2]

    if b == 1:
        if sn == 1:
            p = [526,801]
            dirty_rects.append(screen.blit(select_now, p))
        pygame.display.update(dirty_rects)
    else:
        dirty_rects.append(screen.blit(bg_gi, (526,801), pygame.Rect(526,801,147,44)))
        pygame.display.update(dirty_rects)
    b = not b

    args = [s,b,sn]

    s.delay(name="blink", delay=0.1, handler=blink, param=args)

def line1_animation(args):
    dirty_rects = []
    s = args[0]
    num = args[1]
    line = args[2]

    if line == 1:
        if num % 45 == 0:
            if s.game.line1.position == 0:
                dirty_rects.append(screen.blit(line1, (227,289 - num - 5)))
            elif s.game.line1.position == 1:
                dirty_rects.append(screen.blit(line1, (227,344 - num - 5)))
            elif s.game.line1.position == 2:
                dirty_rects.append(screen.blit(line1, (227,399 + num - 5)))
            elif s.game.line1.position == 3:
                dirty_rects.append(screen.blit(line1, (227,344 + num - 5)))

        if (s.game.anti_cheat.status == True):
            dirty_rects.append(screen.blit(bg_gi, (227,279), pygame.Rect(227,279,53,506)))
        else:
            dirty_rects.append(screen.blit(bg_off, (227,279), pygame.Rect(227,279,53,506)))
        
    pygame.display.update(dirty_rects)

def line2_animation(args):
    dirty_rects = []
    s = args[0]
    num = args[1]
    line = args[2]

    if line == 2:
        if num % 45 == 0:
            if s.game.line2.position == 0:
                dirty_rects.append(screen.blit(line2, (280,289 - num - 5)))
            elif s.game.line2.position == 1:
                dirty_rects.append(screen.blit(line2, (280,344 - num - 5)))
            elif s.game.line2.position == 2:
                dirty_rects.append(screen.blit(line2, (280,399 + num - 5)))
            elif s.game.line2.position == 3:
                dirty_rects.append(screen.blit(line2, (280,344 + num - 5)))

        if (s.game.anti_cheat.status == True):
            dirty_rects.append(screen.blit(bg_gi, (280,279), pygame.Rect(280,279,53,506)))
        else:
            dirty_rects.append(screen.blit(bg_off, (280,279), pygame.Rect(280,279,53,506)))
        
    pygame.display.update(dirty_rects)

def line3_animation(args):
    dirty_rects = []
    s = args[0]
    num = args[1]
    line = args[2]
    
    if line == 3:
        if num % 45 == 0:
            if s.game.line3.position == 0:
                dirty_rects.append(screen.blit(line3, (333,289 - num - 5)))
            elif s.game.line3.position == 1:
                dirty_rects.append(screen.blit(line3, (333,344 - num - 5)))
            elif s.game.line3.position == 2:
                dirty_rects.append(screen.blit(line3, (333,399 + num - 5)))
            elif s.game.line3.position == 3:
                dirty_rects.append(screen.blit(line3, (333,344 + num - 5)))

        if (s.game.anti_cheat.status == True):
            dirty_rects.append(screen.blit(bg_gi, (333,279), pygame.Rect(333,279,53,506)))
        else:
            dirty_rects.append(screen.blit(bg_off, (333,279), pygame.Rect(333,279,53,506)))
        
    pygame.display.update(dirty_rects)

def line4_animation(args):
    dirty_rects = []
    s = args[0]
    num = args[1]
    line = args[2]

    if line == 4:
        if num % 45 == 0:
            if s.game.line4.position == 0:
                dirty_rects.append(screen.blit(line4, (387,289 - num - 5)))
            elif s.game.line4.position == 1:
                dirty_rects.append(screen.blit(line4, (387,344 - num - 5)))
            elif s.game.line4.position == 2:
                dirty_rects.append(screen.blit(line4, (387,399 + num - 5)))
            elif s.game.line4.position == 3:
                dirty_rects.append(screen.blit(line4, (387,344 + num - 5)))

        if (s.game.anti_cheat.status == True):
            dirty_rects.append(screen.blit(bg_gi, (387,279), pygame.Rect(387,279,53,506)))
        else:
            dirty_rects.append(screen.blit(bg_off, (387,279), pygame.Rect(387,279,53,506)))
        
    pygame.display.update(dirty_rects)


def eb_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]

    if s.game.extra_ball.position < 1:
        dirty_rects.append(screen.blit(bg_gi, (140,1016), pygame.Rect(140,1016,44,33)))
    if s.game.extra_ball.position < 2:
        dirty_rects.append(screen.blit(bg_gi, (185,1016), pygame.Rect(185,1016,63,33)))
    if s.game.extra_ball.position < 3:
        dirty_rects.append(screen.blit(bg_gi, (253,1016), pygame.Rect(253,1016,63,33)))
    if s.game.extra_ball.position < 4:
        dirty_rects.append(screen.blit(bg_gi, (326,1016), pygame.Rect(326,1016,44,33)))
    if s.game.extra_ball.position < 5:
        dirty_rects.append(screen.blit(bg_gi, (375,1016), pygame.Rect(375,1016,63,33)))
    if s.game.extra_ball.position < 6:
        dirty_rects.append(screen.blit(bg_gi, (442,1016), pygame.Rect(442,1016,63,33)))
    if s.game.extra_ball.position < 7:
        dirty_rects.append(screen.blit(bg_gi, (512,1016), pygame.Rect(512,1016,44,33)))
    if s.game.extra_ball.position < 8:
        dirty_rects.append(screen.blit(bg_gi, (564,1016), pygame.Rect(564,1016,63,33)))
    if s.game.extra_ball.position < 9:
        dirty_rects.append(screen.blit(bg_gi, (630,1016), pygame.Rect(630,1016,63,33)))
    pygame.display.update(dirty_rects)

    if num in [0,25,14,49]:
        if s.game.extra_ball.position < 1:
            p = [140,1016]
            dirty_rects.append(screen.blit(number_eb, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [39,1,26,15]:
        if s.game.extra_ball.position < 2:
            p = [185,1016]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [3,4,17,28,29,40]:
        if s.game.extra_ball.position < 3:
            p = [253,1016]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [5,18,30,43]:
        if s.game.extra_ball.position < 4:
            p = [326,1016]
            dirty_rects.append(screen.blit(number_eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [7,8,19,32,33,44]:
        if s.game.extra_ball.position < 5:
            p = [375,1016]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [9,10,20,34,35,45]:
        if s.game.extra_ball.position < 6:
            p = [442,1016]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [11,21,36,46]:
        if s.game.extra_ball.position < 7:
            p = [512,1016]
            dirty_rects.append(screen.blit(number_eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [12,22,37,47]:
        if s.game.extra_ball.position < 8:
            p = [564,1016]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [2,6,13,16,23,27,31,38,41,48]:
        if s.game.extra_ball.position < 9:
            p = [630,1016]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return

def clear_odds(s, num):
    global screen
    dirty_rects = []
    if s.game.odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (21,889), pygame.Rect(21,889,77,117)))
    if s.game.odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (104,846), pygame.Rect(104,846,51,148)))
    if s.game.odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (174,844), pygame.Rect(174,844,64,160)))
    if s.game.odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (234,871), pygame.Rect(234,871,51,106)))
    if s.game.odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (292,850), pygame.Rect(292,850,44,145)))
    if s.game.odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (365,847), pygame.Rect(365,847,54,157)))
    if s.game.odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (424,880), pygame.Rect(424,880,47,107)))
    if s.game.odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (470,851), pygame.Rect(470,851,78,135)))
    if s.game.odds.position != 9:
        dirty_rects.append(screen.blit(bg_gi, (568,852), pygame.Rect(568,852,55,150)))
    if s.game.odds.position != 10:
        dirty_rects.append(screen.blit(bg_gi, (620,880), pygame.Rect(620,880,83,130)))

    pygame.display.update(dirty_rects)

def draw_odds_animation(s, num):
    global screen
    dirty_rects = []

    if num in [2,3,27,28]:
        if s.game.odds.position != 1:
            p = [21,889]
            dirty_rects.append(screen.blit(o1, p))
            pygame.display.update(dirty_rects)
            return
    if num in [4,5,29,30]:
        if s.game.odds.position != 2:
            p = [104,846]
            dirty_rects.append(screen.blit(o2, p))
            pygame.display.update(dirty_rects)
            return
    if num in [6,7,31,32]:
        if s.game.odds.position != 3:
            p = [174,844]
            dirty_rects.append(screen.blit(o3, p))
            pygame.display.update(dirty_rects)
            return
    if num in [8,9,33,34]:
        if s.game.odds.position != 4:
            p = [234,871]
            dirty_rects.append(screen.blit(o4, p))
            pygame.display.update(dirty_rects)
            return
    if num in [10,11,22,35,36,47]:
        if s.game.odds.position != 5:
            p = [292,850]
            dirty_rects.append(screen.blit(o5, p))
            pygame.display.update(dirty_rects)
            return
    if num in [12,13,23,37,38,48]:
        if s.game.odds.position != 6:
            p = [365,847]
            dirty_rects.append(screen.blit(o6, p))
            pygame.display.update(dirty_rects)
            return
    if num in [14,15,24,39,40,49]:
        if s.game.odds.position != 7:
            p = [424,880]
            dirty_rects.append(screen.blit(o7, p))
            pygame.display.update(dirty_rects)
            return
    if num in [16,17,25,41,42,50]:
        if s.game.odds.position != 8:
            p = [470,851]
            dirty_rects.append(screen.blit(o8, p))
            pygame.display.update(dirty_rects)
            return
    if num in [18,19,43,44]:
        if s.game.odds.position != 9:
            p = [568,852]
            dirty_rects.append(screen.blit(o9, p))
            pygame.display.update(dirty_rects)
            return
    if num in [20,21,45,46]:
        if s.game.odds.position != 10:
            p = [620,880]
            dirty_rects.append(screen.blit(o10, p))
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
    if s.game.corners.status == False:
        dirty_rects.append(screen.blit(bg_gi, (72,456), pygame.Rect(72,456,85,80)))
    if s.game.magic_pockets.status == False:
        dirty_rects.append(screen.blit(bg_gi, (29,545), pygame.Rect(29,545,167,192)))
    if s.game.red_three_as_four.status == False:
        dirty_rects.append(screen.blit(bg_gi, (544,527), pygame.Rect(544,527,138,137)))
    if s.game.yellow_three_as_four:
        dirty_rects.append(screen.blit(bg_gi, (543,661), pygame.Rect(543,661,138,137)))
    if s.game.spot_10.status == False:
        dirty_rects.append(screen.blit(bg_gi, (538,454), pygame.Rect(538,454,73,64)))
    if s.game.spot_25.status == False:
        dirty_rects.append(screen.blit(bg_gi, (617,454), pygame.Rect(617,454,73,64)))

    pygame.display.update(dirty_rects)


def draw_feature_animation(s, num):
    global screen
    dirty_rects = []

    if num in [4,5,12,13,20,29,30,37,38,45]:
        if s.game.corners.status == False:
            p = [72,456]
            dirty_rects.append(screen.blit(c, p))
            pygame.display.update(dirty_rects)
    if num in [6,7,14,15,21,31,32,39,40,46]:
        if s.game.magic_pockets.status == False:
            p = [29,545]
            dirty_rects.append(screen.blit(m, p))
            pygame.display.update(dirty_rects)
    if num in [2,3,10,0,27,28,35,26]:
        if s.game.red_three_as_four.status == False:
            p = [544,527]
            dirty_rects.append(screen.blit(three_as_four, p))
            pygame.display.update(dirty_rects)
    if num in [0,1,8,9,16,25,26,33,34,41]:
        if s.game.yellow_three_as_four.status == False:
            p = [543,661]
            dirty_rects.append(screen.blit(three_as_four, p))
            pygame.display.update(dirty_rects)
    if num in [11,18,19]:
        if s.game.spot_10.status == False:
            p = [538,454]
            dirty_rects.append(screen.blit(spotted, p))
            pygame.display.update(dirty_rects)
    if num in [17,22,23]:
        if s.game.spot_25.status == False:
            p = [617,454]
            dirty_rects.append(screen.blit(spotted, p))
            pygame.display.update(dirty_rects)

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

