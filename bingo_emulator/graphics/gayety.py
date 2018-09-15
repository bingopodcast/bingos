
import pygame
import random

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

meter = pygame.image.load('graphics/assets/register_cover.png').convert()
eb = pygame.image.load('gayety/assets/eb.png').convert_alpha()
ebs = pygame.image.load('gayety/assets/extra_balls.png').convert_alpha()
number_eb = pygame.image.load('gayety/assets/eb_number.png').convert_alpha()
o1 = pygame.image.load('gayety/assets/odds1.png').convert_alpha()
o2 = pygame.image.load('gayety/assets/odds2.png').convert_alpha()
o3 = pygame.image.load('gayety/assets/odds3.png').convert_alpha()
o4 = pygame.image.load('gayety/assets/odds4.png').convert_alpha()
o5 = pygame.image.load('gayety/assets/odds5.png').convert_alpha()
o6 = pygame.image.load('gayety/assets/odds6.png').convert_alpha()
o7 = pygame.image.load('gayety/assets/odds7.png').convert_alpha()
o8 = pygame.image.load('gayety/assets/odds8.png').convert_alpha()
c = pygame.image.load('gayety/assets/corners.png').convert_alpha()
m = pygame.image.load('gayety/assets/magic.png').convert_alpha()
number = pygame.image.load('gayety/assets/number.png').convert_alpha()
tilt = pygame.image.load('gayety/assets/tilt.png').convert_alpha()
magic_arrow = pygame.image.load('gayety/assets/magic_arrow.png').convert_alpha()
select_now = pygame.image.load('gayety/assets/select_now.png').convert_alpha()
line1 = pygame.image.load('gayety/assets/line1.png').convert_alpha()
line2 = pygame.image.load('gayety/assets/line2.png').convert_alpha()
line3 = pygame.image.load('gayety/assets/line3.png').convert_alpha()
bg_menu = pygame.image.load('gayety/assets/gayety_menu.png').convert()
bg_menu.set_colorkey((255,0,252))
bg_gi = pygame.image.load('gayety/assets/gayety_gi.png').convert_alpha()
bg_off = pygame.image.load('gayety/assets/gayety_off.png').convert()
bg_off.set_colorkey((255,0,252))

class scorereel():
    """ Score Reels are used to count replays """
    def __init__(self, pos, image):
        self.position = pos
        self.default_y = self.position[1]
        self.image = pygame.image.load(image).convert()

reel1 = scorereel([91,314], "graphics/assets/green_reel.png")
reel10 = scorereel([72,314], "graphics/assets/green_reel.png")
reel100 = scorereel([53,314], "graphics/assets/green_reel.png")

def display(s, replays=0, menu=False):
    
    meter.set_colorkey((255,0,252))
    meter_position = [44,314]

    screen.blit(reel1.image, reel1.position)
    screen.blit(reel10.image, reel10.position)
    screen.blit(reel100.image, reel100.position)
    screen.blit(meter, meter_position)

    if s.game.line1.position in [0,2]:
        line1_position = [228,347]
    elif s.game.line1.position == 1:
        line1_position = [228,402]
    elif s.game.line1.position == 3:
        line1_position = [228,292]
    
    screen.blit(line1, line1_position)

    if s.game.line2.position in [0,2]:
        line2_position = [283,347]
    elif s.game.line2.position == 1:
        line2_position = [283,402]
    elif s.game.line2.position == 3:
        line2_position = [283,292]
    
    screen.blit(line2, line2_position)

    if s.game.line3.position in [0,2]:
        line3_position = [335,347]
    elif s.game.line3.position == 1:
        line3_position = [335,402]
    elif s.game.line3.position == 3:
        line3_position = [335,292]
    
    screen.blit(line3, line3_position)

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
        eb_position = [146,1018]
        screen.blit(number_eb, eb_position)
    if s.game.extra_ball.position >= 2:
        eb_position = [192,1017]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 3:
        eb_position = [261,1016]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 4:
        eb_position = [332,1016]
        screen.blit(number_eb, eb_position)
    if s.game.extra_ball.position >= 5:
        eb_position = [381,1015]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 6:
        eb_position = [448,1015]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 7:
        eb_position = [520,1014]
        screen.blit(number_eb, eb_position)
    if s.game.extra_ball.position >= 8:
        eb_position = [568,1014]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 9:
        eb_position = [634,1013]
        screen.blit(eb, eb_position)
    
    
    if s.game.odds.position > 0:
        if s.game.odds.position == 1:
            odds_position = [37,817]
            screen.blit(o1, odds_position)
        if s.game.odds.position == 2:
            odds_position = [107,816]
            screen.blit(o2, odds_position)
        if s.game.odds.position == 3:
            odds_position = [174,815]
            screen.blit(o3, odds_position)
        if s.game.odds.position == 4:
            odds_position = [240,813]
            screen.blit(o4, odds_position)
        if s.game.odds.position == 5:
            odds_position = [313,813]
            screen.blit(o5, odds_position)
        if s.game.odds.position == 6:
            odds_position = [482,812]
            screen.blit(o6, odds_position)
        if s.game.odds.position == 7:
            odds_position = [552,810]
            screen.blit(o7, odds_position)
        if s.game.odds.position == 8:
            odds_position = [617,811]
            screen.blit(o8, odds_position)

    if s.game.corners.status == True:
        corners_position = [22,467]
        screen.blit(c, corners_position)
    if s.game.corners300.status == True:
        corners_position = [119,466]
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
                number_position = [389,510]
                screen.blit(number, number_position)
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
                number_position = [391,454]
                screen.blit(number, number_position)
            if 21 in s.holes:
                number_position = [391,564]
                screen.blit(number, number_position)
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
                number_position = [389,616]
                screen.blit(number, number_position)
            if 24 in s.holes:
                number_position = [390,400]
                screen.blit(number, number_position)
            if 25 in s.holes:
                number_position = [441,508]
                screen.blit(number, number_position)

    if s.game.tilt.status == True:
        tilt_position = [147,263]
        screen.blit(tilt, tilt_position)

    if s.game.eb_play.status == True:
        ebs_position = [30,1018]
        screen.blit(ebs, ebs_position)

    if s.game.m_pockets.position == 1:
        p = [539,511]
        screen.blit(magic_arrow, p)
    elif s.game.m_pockets.position == 2:
        p = [577,511]
        screen.blit(magic_arrow, p)
    elif s.game.m_pockets.position == 3:
        p = [614,511]
        screen.blit(magic_arrow, p)
    elif s.game.m_pockets.position == 4:
        p = [652,511]
        screen.blit(magic_arrow, p)
        p = [519,548]
        screen.blit(m, p)
        if s.game.ball_count.position == 3:
            s.cancel_delayed(name="blink_pockets")
            blink_pockets([s,1,1])
        else:
            s.cancel_delayed("blink_pockets")

    if s.game.m_lines.status == True:
        p = [22,550]
        screen.blit(m, p)
        if s.game.ball_count.position == 3:
            s.cancel_delayed(name="blink")
            blink([s,1,1])
        else:
            s.cancel_delayed(name="blink")

    pygame.display.update()

def blink_pockets(args):
    dirty_rects = []
    s = args[0]
    b = args[1]
    sn = args[2]

    if b == 1:
        if sn == 1:
            p = [520,756]
            dirty_rects.append(screen.blit(select_now, p))
        pygame.display.update(dirty_rects)
    else:
        dirty_rects.append(screen.blit(bg_gi, (520,756), pygame.Rect(520,756,177,36)))
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
            p = [24,758]
            dirty_rects.append(screen.blit(select_now, p))
        pygame.display.update(dirty_rects)
    else:
        dirty_rects.append(screen.blit(bg_gi, (24,758), pygame.Rect(24,758,177,36)))
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
                dirty_rects.append(screen.blit(line1, (228,292 - num - 5)))
            elif s.game.line1.position == 1:
                dirty_rects.append(screen.blit(line1, (228,347 - num - 5)))
            elif s.game.line1.position == 2:
                dirty_rects.append(screen.blit(line1, (228,402 + num - 5)))
            elif s.game.line1.position == 3:
                dirty_rects.append(screen.blit(line1, (228,347 + num - 5)))

        if (s.game.anti_cheat.status == True):
            dirty_rects.append(screen.blit(bg_gi, (228,282), pygame.Rect(228,282,53,706)))
        else:
            dirty_rects.append(screen.blit(bg_off, (228,282), pygame.Rect(228,282,53,706)))
     
        if s.game.odds.position == 3:
            dirty_rects.append(screen.blit(bg_gi, (174,815), pygame.Rect(174,815,55,177)))
            dirty_rects.append(screen.blit(o3, (174,815)))
        if s.game.odds.position == 4:
            dirty_rects.append(screen.blit(bg_gi, (240,813), pygame.Rect(240,813,60,177)))
            dirty_rects.append(screen.blit(o4, (240,813)))
        if s.game.odds.position == 5:
            dirty_rects.append(screen.blit(bg_gi, (313,813), pygame.Rect(313,813,55,176)))
            dirty_rects.append(screen.blit(o5, (313,813)))
   
    pygame.display.update(dirty_rects)

def line2_animation(args):
    dirty_rects = []
    s = args[0]
    num = args[1]
    line = args[2]

    if line == 2:
        if num % 45 == 0:
            if s.game.line2.position == 0:
                dirty_rects.append(screen.blit(line2, (283,292 - num - 5)))
            elif s.game.line2.position == 1:
                dirty_rects.append(screen.blit(line2, (283,347 - num - 5)))
            elif s.game.line2.position == 2:
                dirty_rects.append(screen.blit(line2, (283,402 + num - 5)))
            elif s.game.line2.position == 3:
                dirty_rects.append(screen.blit(line2, (283,347 + num - 5)))

        if (s.game.anti_cheat.status == True):
            dirty_rects.append(screen.blit(bg_gi, (283,282), pygame.Rect(283,282,53,706)))
        else:
            dirty_rects.append(screen.blit(bg_off, (283,282), pygame.Rect(283,282,53,706)))
        
        if s.game.odds.position == 3:
            dirty_rects.append(screen.blit(bg_gi, (174,815), pygame.Rect(174,815,55,177)))
            dirty_rects.append(screen.blit(o3, (174,815)))
        if s.game.odds.position == 4:
            dirty_rects.append(screen.blit(bg_gi, (240,813), pygame.Rect(240,813,60,177)))
            dirty_rects.append(screen.blit(o4, (240,813)))
        if s.game.odds.position == 5:
            dirty_rects.append(screen.blit(bg_gi, (313,813), pygame.Rect(313,813,55,176)))
            dirty_rects.append(screen.blit(o5, (313,813)))
    pygame.display.update(dirty_rects)

def line3_animation(args):
    dirty_rects = []
    s = args[0]
    num = args[1]
    line = args[2]

    if line == 3:
        if num % 45 == 0:
            if s.game.line3.position == 0:
                dirty_rects.append(screen.blit(line3, (335, 292 - num - 5)))
            elif s.game.line3.position == 1:
                dirty_rects.append(screen.blit(line3, (335, 347 - num - 5)))
            elif s.game.line3.position == 2:
                dirty_rects.append(screen.blit(line3, (335, 402 + num - 5)))
            elif s.game.line3.position == 3:
                dirty_rects.append(screen.blit(line3, (335, 347 + num - 5)))

        if (s.game.anti_cheat.status == True):
            dirty_rects.append(screen.blit(bg_gi, (335,282), pygame.Rect(335,282,53,706)))
        else:
            dirty_rects.append(screen.blit(bg_off, (335,282), pygame.Rect(335,282,53,706)))
        
        if s.game.odds.position == 3:
            dirty_rects.append(screen.blit(bg_gi, (174,815), pygame.Rect(174,815,55,177)))
            dirty_rects.append(screen.blit(o3, (174,815)))
        if s.game.odds.position == 4:
            dirty_rects.append(screen.blit(bg_gi, (240,813), pygame.Rect(240,813,60,177)))
            dirty_rects.append(screen.blit(o4, (240,813)))
        if s.game.odds.position == 5:
            dirty_rects.append(screen.blit(bg_gi, (313,813), pygame.Rect(313,813,55,176)))
            dirty_rects.append(screen.blit(o5, (313,813)))
    pygame.display.update(dirty_rects)


def eb_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]

    if s.game.extra_ball.position < 1:
        dirty_rects.append(screen.blit(bg_gi, (146,1018), pygame.Rect(146,1018,45,31)))
    if s.game.extra_ball.position < 2:
        dirty_rects.append(screen.blit(bg_gi, (192,1017), pygame.Rect(192,1017,64,33)))
    if s.game.extra_ball.position < 3:
        dirty_rects.append(screen.blit(bg_gi, (261,1016), pygame.Rect(261,1016,64,33)))
    if s.game.extra_ball.position < 4:
        dirty_rects.append(screen.blit(bg_gi, (332,1016), pygame.Rect(332,1016,45,31)))
    if s.game.extra_ball.position < 5:
        dirty_rects.append(screen.blit(bg_gi, (381,1015), pygame.Rect(381,1015,64,33)))
    if s.game.extra_ball.position < 6:
        dirty_rects.append(screen.blit(bg_gi, (448,1015), pygame.Rect(448,1015,64,33)))
    if s.game.extra_ball.position < 7:
        dirty_rects.append(screen.blit(bg_gi, (520,1014), pygame.Rect(520,1014,45,31)))
    if s.game.extra_ball.position < 8:
        dirty_rects.append(screen.blit(bg_gi, (568,1014), pygame.Rect(568,1014,64,33)))
    if s.game.extra_ball.position < 9:
        dirty_rects.append(screen.blit(bg_gi, (634,1013), pygame.Rect(634,1013,64,33)))
    pygame.display.update(dirty_rects)

    if num in [0,25,14,49]:
        if s.game.extra_ball.position < 1:
            p = [146,1018]
            dirty_rects.append(screen.blit(number_eb, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [39,1,26,15]:
        if s.game.extra_ball.position < 2:
            p = [192,1017]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [3,4,17,28,29,40]:
        if s.game.extra_ball.position < 3:
            p = [261,1016]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [5,18,30,43]:
        if s.game.extra_ball.position < 4:
            p = [332,1016]
            dirty_rects.append(screen.blit(number_eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [7,8,19,32,33,44]:
        if s.game.extra_ball.position < 5:
            p = [381,1015]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [9,10,20,34,35,45]:
        if s.game.extra_ball.position < 6:
            p = [448,1015]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [11,21,36,46]:
        if s.game.extra_ball.position < 7:
            p = [520,1014]
            dirty_rects.append(screen.blit(number_eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [12,22,37,47]:
        if s.game.extra_ball.position < 8:
            p = [568,1014]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [2,6,13,16,23,27,31,38,41,48]:
        if s.game.extra_ball.position < 9:
            p = [634,1013]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return

def clear_odds(s, num):
    global screen

    dirty_rects = []
    if s.game.odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (37,817), pygame.Rect(37,817,55,173)))
    if s.game.odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (107,816), pygame.Rect(107,816,55,177)))
    if s.game.odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (174,815), pygame.Rect(174,815,55,177)))
    if s.game.odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (240,813), pygame.Rect(240,813,60,177)))
    if s.game.odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (313,813), pygame.Rect(313,813,55,176)))
    if s.game.odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (482,812), pygame.Rect(482,812,65,179)))
    if s.game.odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (552,810), pygame.Rect(552,810,65,179)))
    if s.game.odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (617,811), pygame.Rect(617,811,70,179)))

    pygame.display.update(dirty_rects)

def draw_odds_animation(s, num):
    global screen
    dirty_rects = []

    if num in [2,3,27,28]:
        if s.game.odds.position != 1:
            p = [37,817]
            dirty_rects.append(screen.blit(o1, p))
            pygame.display.update(dirty_rects)
            return
    if num in [4,5,17,29,30,42]:
        if s.game.odds.position != 2:
            p = [107,816]
            dirty_rects.append(screen.blit(o2, p))
            pygame.display.update(dirty_rects)
            return
    if num in [6,7,18,19,31,32,43,44]:
        if s.game.odds.position != 3:
            p = [174,815]
            dirty_rects.append(screen.blit(o3, p))
            pygame.display.update(dirty_rects)
            return
    if num in [8,9,20,21,33,34,45,46]:
        if s.game.odds.position != 4:
            p = [240,813]
            dirty_rects.append(screen.blit(o4, p))
            pygame.display.update(dirty_rects)
            return
    if num in [10,11,22,35,36,47]:
        if s.game.odds.position != 5:
            p = [313,813]
            dirty_rects.append(screen.blit(o5, p))
            pygame.display.update(dirty_rects)
            return
    if num in [12,13,23,37,38,48]:
        if s.game.odds.position != 6:
            p = [482,812]
            dirty_rects.append(screen.blit(o6, p))
            pygame.display.update(dirty_rects)
            return
    if num in [14,15,24,39,40,49]:
        if s.game.odds.position != 7:
            p = [552,810]
            dirty_rects.append(screen.blit(o7, p))
            pygame.display.update(dirty_rects)
            return
    if num in [16,25,41,50]:
        if s.game.odds.position != 8:
            p = [617,811]
            dirty_rects.append(screen.blit(o8, p))
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
        dirty_rects.append(screen.blit(bg_gi, (22,467), pygame.Rect(22,467,85,75)))
    if s.game.corners300.status == False:
        dirty_rects.append(screen.blit(bg_gi, (119,466), pygame.Rect(119,466,85,75)))
    if s.game.m_lines.status == False:
        dirty_rects.append(screen.blit(bg_gi, (22,550), pygame.Rect(22,550,183,201)))
    if s.game.m_pockets.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (519,548), pygame.Rect(519,548,183,201)))

    pygame.display.update(dirty_rects)


def draw_feature_animation(s, num):
    global screen
    dirty_rects = []

    if num in [4,5,12,13,20,29,30,37,38,45]:
        if s.game.corners.status == False:
            p = [22,467]
            dirty_rects.append(screen.blit(c, p))
            pygame.display.update(dirty_rects)
            return
    if num in [6,7,14,15,21,31,32,39,40,46]:
        if s.game.corners300.status == False:
            p = [119,466]
            dirty_rects.append(screen.blit(c, p))
            pygame.display.update(dirty_rects)
            return
    if num in [2,3,10,11,18,19,0,27,28,35,36,43,44,26]:
        if s.game.m_lines.status == False:
            p = [22,550]
            dirty_rects.append(screen.blit(m, p))
            pygame.display.update(dirty_rects)
            return
    if num in [0,1,8,9,16,17,22,23,25,26,33,34,41,42,47,48]:
        if s.game.m_pockets.position != 4:
            p = [519,548]
            dirty_rects.append(screen.blit(m, p))
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


def blink(args):
    dirty_rects = []
    s = args[0]
    b = args[1]
    sn = args[2]

    if b == 0:
        if sn == 1:
            p = [258,738]
            dirty_rects.append(screen.blit(select_now, p))
        pygame.display.update(dirty_rects)
    else:
        dirty_rects.append(screen.blit(bg_gi, (258,738), pygame.Rect(258,738,200,35)))
        pygame.display.update(dirty_rects)
    b = not b

    args = [s,b,sn]

    s.delay(name="blink", delay=0.1, handler=blink, param=args)

