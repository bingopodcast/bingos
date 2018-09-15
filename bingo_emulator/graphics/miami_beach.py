
import pygame
import random

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

meter = pygame.image.load('graphics/assets/register_cover.png').convert()
card = pygame.image.load('miami_beach/assets/card.png').convert_alpha()
c = pygame.image.load('miami_beach/assets/corners.png').convert_alpha()
eb = pygame.image.load('miami_beach/assets/eb.png').convert_alpha()
arrow = pygame.image.load('miami_beach/assets/arrow.png').convert_alpha()
line_arrow = pygame.image.load('miami_beach/assets/line_arrow.png').convert_alpha()
number_eb = pygame.image.load('miami_beach/assets/eb_number.png').convert_alpha()
ebs = pygame.image.load('miami_beach/assets/extra_balls.png').convert_alpha()
green = pygame.image.load('miami_beach/assets/green_three_as_four.png').convert_alpha()
yellow = pygame.image.load('miami_beach/assets/yellow_three_as_four.png').convert_alpha()
red = pygame.image.load('miami_beach/assets/red_three_as_four.png').convert_alpha()
number = pygame.image.load('miami_beach/assets/number.png').convert_alpha()
number_square = pygame.image.load('miami_beach/assets/number_square.png').convert_alpha()
number_card = pygame.image.load('miami_beach/assets/number_card.png').convert_alpha()
o1 = pygame.image.load('miami_beach/assets/odds1.png').convert_alpha()
o2 = pygame.image.load('miami_beach/assets/odds2.png').convert_alpha()
o3 = pygame.image.load('miami_beach/assets/odds3.png').convert_alpha()
o4 = pygame.image.load('miami_beach/assets/odds4.png').convert_alpha()
o5 = pygame.image.load('miami_beach/assets/odds5.png').convert_alpha()
o6 = pygame.image.load('miami_beach/assets/odds6.png').convert_alpha()
o7 = pygame.image.load('miami_beach/assets/odds7.png').convert_alpha()
o8 = pygame.image.load('miami_beach/assets/odds8.png').convert_alpha()
o9 = pygame.image.load('miami_beach/assets/odds9.png').convert_alpha()
select_number = pygame.image.load('miami_beach/assets/select_number.png').convert_alpha()
select_now = pygame.image.load('miami_beach/assets/select_now.png').convert_alpha()
spotted_numbers = pygame.image.load('miami_beach/assets/spotted_numbers.png').convert_alpha()
slat = pygame.image.load('miami_beach/assets/slat.png').convert_alpha()
tilt = pygame.image.load('miami_beach/assets/tilt.png').convert_alpha()
red_number = pygame.image.load('miami_beach/assets/red_number.png').convert_alpha()
bg_menu = pygame.image.load('miami_beach/assets/miami_beach_menu.png')
bg_gi = pygame.image.load('miami_beach/assets/miami_beach_gi.png')
bg_off = pygame.image.load('miami_beach/assets/miami_beach_off.png')

class scorereel():
    """ Score Reels are used to count replays """
    def __init__(self, pos, image):
        self.position = pos
        self.default_y = self.position[1]
        self.image = pygame.image.load(image).convert()

reel1 = scorereel([107,347], "graphics/assets/green_reel.png")
reel10 = scorereel([88,347], "graphics/assets/green_reel.png")
reel100 = scorereel([70,347], "graphics/assets/green_reel.png")

def display(s, replays=0, menu=False):
    
    meter.set_colorkey((255,0,252))
    meter_position = [60,347]

    screen.blit(reel1.image, reel1.position)
    screen.blit(reel10.image, reel10.position)
    screen.blit(reel100.image, reel100.position)
    screen.blit(meter, meter_position)

    number_card_position = [119,435]
    screen.blit(number_card, number_card_position)

    if s.game.curtains.position < 5:
        slat_position = [548,431]
        screen.blit(slat, slat_position)
    if s.game.curtains.position < 4:
        slat_position = [494,431]
        screen.blit(slat, slat_position)
    if s.game.curtains.position < 3:
        slat_position = [440,431]
        screen.blit(slat, slat_position)
    if s.game.curtains.position < 2:
        slat_position = [385,431]
        screen.blit(slat, slat_position)
 
    backglass_position = [0, 0]
    backglass = pygame.Surface(screen.get_size(), flags=pygame.SRCALPHA)
    backglass.set_colorkey((255,0,252))
    backglass.fill((0, 0, 0))
    if menu == True:
        screen.blit(bg_menu, backglass_position)
    else:
        if (s.game.anti_cheat.status == True):
            screen.blit(bg_gi, backglass_position)
        else:
            screen.blit(bg_off, backglass_position)

    if s.game.extra_ball.position >= 1:
        eb_position = [131,944]
        screen.blit(number_eb, eb_position)
    if s.game.extra_ball.position >= 2:
        eb_position = [181,944]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 3:
        eb_position = [249,944]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 4:
        eb_position = [320,944]
        screen.blit(number_eb, eb_position)
    if s.game.extra_ball.position >= 5:
        eb_position = [370,944]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 6:
        eb_position = [437,944]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 7:
        eb_position = [510,944]
        screen.blit(number_eb, eb_position)
    if s.game.extra_ball.position >= 8:
        eb_position = [560,944]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 9:
        eb_position = [628,944]
        screen.blit(eb, eb_position)
   
  
    if s.game.lines.position == 1:
        p = [26,765]
        screen.blit(line_arrow, p)
    if s.game.lines.position == 2:
        p = [53,765]
        screen.blit(line_arrow, p)
    if s.game.lines.position == 3:
        p = [79,765]
        screen.blit(line_arrow, p)
    if s.game.lines.position == 4:
        p = [106,765]
        screen.blit(line_arrow, p)
    if s.game.lines.position >= 5 and s.game.lines.position < 10:
        p = [131,761]
        screen.blit(card, p)
    if s.game.lines.position == 6:
        p = [210,765]
        screen.blit(line_arrow, p)
    if s.game.lines.position == 7:
        p = [236,765]
        screen.blit(line_arrow, p)
    if s.game.lines.position == 8:
        p = [263,765]
        screen.blit(line_arrow, p)
    if s.game.lines.position == 9:
        p = [288,765]
        screen.blit(line_arrow, p)
    if s.game.lines.position >= 10 and s.game.lines.position < 15:
        p = [314,761]
        screen.blit(card, p)
    if s.game.lines.position == 11:
        p = [395,765]
        screen.blit(line_arrow, p)
    if s.game.lines.position == 12:
        p = [422,765]
        screen.blit(line_arrow, p)
    if s.game.lines.position == 13:
        p = [449,765]
        screen.blit(line_arrow, p)
    if s.game.lines.position == 14:
        p = [476,765]
        screen.blit(line_arrow, p)
    if s.game.lines.position == 15:
        p = [500,760]
        screen.blit(card, p)

    if s.game.green_three_as_five.status == True:
        p = [594,720]
        screen.blit(green, p)
    if s.game.yellow_three_as_four.status == True:
        p = [594,795]
        screen.blit(yellow, p)
    if s.game.red_three_as_four.status == True:
        p = [591,860]
        screen.blit(red, p)

    if s.game.odds.position > 0:
        if s.game.odds.position == 1:
            odds_position = [20,852]
            screen.blit(o1, odds_position)
        if s.game.odds.position == 2:
            odds_position = [63,818]
            screen.blit(o2, odds_position)
        if s.game.odds.position == 3:
            odds_position = [129,818]
            screen.blit(o3, odds_position)
        if s.game.odds.position == 4:
            odds_position = [184,834]
            screen.blit(o4, odds_position)
        if s.game.odds.position == 5:
            odds_position = [245,808]
            screen.blit(o5, odds_position)
        if s.game.odds.position == 6:
            odds_position = [304,823]
            screen.blit(o6, odds_position)
        if s.game.odds.position == 7:
            odds_position = [363,808]
            screen.blit(o7, odds_position)
        if s.game.odds.position == 8:
            odds_position = [420,834]
            screen.blit(o8, odds_position)
        if s.game.odds.position == 9:
            odds_position = [494,813]
            screen.blit(o9, odds_position)

    if s.game.corners.status == True and s.game.super_corners.status == False:
        corners_position = [17,599]
        screen.blit(c, corners_position)
    if s.game.super_corners.status == True and s.game.corners.status == True:
        corners_position = [17,525]
        screen.blit(c, corners_position)

    if s.game.tilt.status == False:
        if s.holes:
            if 1 in s.holes:
                number_position = [337,532]
                screen.blit(number, number_position)
                if s.game.curtains.position >= 5:
                    number_position = [550,444]
                    screen.blit(number, number_position)
            if 2 in s.holes:
                number_position = [126,529]
                screen.blit(number, number_position)
                if s.game.curtains.position >= 2:
                    number_position = [390,620]
                    screen.blit(number, number_position)
            if 3 in s.holes:
                if s.game.curtains.position >= 5:
                    number_position = [549,490]
                    screen.blit(number, number_position)
                number_position = [336,620]
                screen.blit(number, number_position)
            if 4 in s.holes:
                number_position = [176,436]
                screen.blit(number, number_position)
                if s.game.curtains.position >= 4:
                    number_position = [497,444]
                    screen.blit(number, number_position)
            if 5 in s.holes:
                if s.game.curtains.position >= 2:
                    number_position = [390,444]
                    screen.blit(number, number_position)
                number_position = [227,619]
                screen.blit(number_square, number_position)
            if 6 in s.holes:
                number_position = [338,444]
                screen.blit(number, number_position)
                if s.game.curtains.position >= 4:
                    number_position = [495,620]
                    screen.blit(number, number_position)
            if 7 in s.holes:
                number_position = [176,620]
                screen.blit(number, number_position)
                if s.game.curtains.position >= 5:
                    number_position = [548,620]
                    screen.blit(number, number_position)
            if 8 in s.holes:
                number_position = [337,488]
                screen.blit(number, number_position)
                if s.game.curtains.position >= 5:
                    number_position = [548,534]
                    screen.blit(number, number_position)
            if 9 in s.holes:
                number_position = [125,435]
                screen.blit(number, number_position)
                if s.game.curtains.position >= 3:
                    number_position = [444,489]
                    screen.blit(number, number_position)
            if 10 in s.holes:
                number_position = [127,482]
                screen.blit(number, number_position)
                if s.game.curtains.position >= 3:
                    number_position = [444,533]
                    screen.blit(number, number_position)
            if 11 in s.holes:
                number_position = [124,620]
                screen.blit(number, number_position)
                if s.game.curtains.position >= 5:
                    number_position = [549,577]
                    screen.blit(number, number_position)
            if 12 in s.holes:
                number_position = [283,531]
                screen.blit(number, number_position)
                if s.game.curtains.position >= 3:
                    number_position = [441,621]
                    screen.blit(number_square, number_position)
            if 13 in s.holes:
                number_position = [127,574]
                screen.blit(number, number_position)
                if s.game.curtains.position >= 3:
                    number_position = [443,443]
                    screen.blit(number_square, number_position)
            if 14 in s.holes:
                number_position = [228,484]
                screen.blit(number, number_position)
                if s.game.curtains.position >= 3:
                    number_position = [444,576]
                    screen.blit(number, number_position)
            if 15 in s.holes:
                number_position = [284,442]
                screen.blit(number, number_position)
                if s.game.curtains.position >= 4:
                    number_position = [496,533]
                    screen.blit(number, number_position)
            if 16 in s.holes:
                number_position = [228,529]
                screen.blit(number, number_position)
            if 17 in s.holes:
                number_position = [337,576]
                screen.blit(number, number_position)
            if 18 in s.holes:
                number_position = [177,528]
                screen.blit(number, number_position)
            if 19 in s.holes:
                if s.game.curtains.position >= 2:
                    number_position = [391,488]
                    screen.blit(number, number_position)
                number_position = [177,484]
                screen.blit(number, number_position)
            if 20 in s.holes:
                number_position = [284,486]
                screen.blit(number, number_position)
                if s.game.curtains.position >= 4:
                    number_position = [496,489]
                    screen.blit(number, number_position)
            if 21 in s.holes:
                number_position = [283,575]
                screen.blit(number, number_position)
                if s.game.curtains.position >= 4:
                    number_position = [496,577]
                    screen.blit(number, number_position)
            if 22 in s.holes:
                number_position = [178,573]
                screen.blit(number, number_position)
                if s.game.curtains.position >= 2:
                    number_position = [390,577]
                    screen.blit(number, number_position)
            if 23 in s.holes:
                number_position = [284,621]
                screen.blit(number, number_position)
                if s.game.curtains.position >= 2:
                    number_position = [390,532]
                    screen.blit(number, number_position)
            if 24 in s.holes:
                number_position = [227,437]
                screen.blit(number_square, number_position)
            if 25 in s.holes:
                number_position = [228,575]
                screen.blit(number, number_position)

    if s.game.tilt.status == True:
        tilt_position = [600,307]
        screen.blit(tilt, tilt_position)

    if s.game.spotted_numbers.position == 1:
        p = [12,690]
        screen.blit(arrow, p)
    if s.game.spotted_numbers.position == 2:
        p = [67,690]
        screen.blit(arrow, p)
    if s.game.spotted_numbers.position == 3:
        p = [131,690]
        screen.blit(arrow, p)
    if s.game.spotted_numbers.position == 4:
        p = [180,690]
        screen.blit(arrow, p)
    if s.game.spotted_numbers.position == 5:
        p = [224,689]
        screen.blit(arrow, p)
    if s.game.spotted_numbers.position >= 6:
        p = [274,672]
        screen.blit(spotted_numbers, p)

    if s.game.spotted_numbers.position == 6 and s.game.ball_count.position == 3:
        s.cancel_delayed(name="blink")
        blink([s,1,1])
    else:
        s.cancel_delayed(name="blink")

    if s.game.eb_play.status == True:
        ebs_position = [18,940]
        screen.blit(ebs, ebs_position)

    if s.game.spotted_numbers.position >= 6:
        if s.game.ball_count.position < 4:
            if s.game.spotted.position == 0:
                #19
                if s.game.curtains.position >= 2:
                    number_position = [391,488]
                    screen.blit(red_number, number_position)
                number_position = [177,484]
                screen.blit(red_number, number_position)
            if s.game.spotted.position == 1:
                #20
                number_position = [284,486]
                screen.blit(red_number, number_position)
                if s.game.curtains.position >= 4:
                    number_position = [496,489]
                    screen.blit(red_number, number_position)
            if s.game.spotted.position == 2:
                #21
                number_position = [283,575]
                screen.blit(red_number, number_position)
                if s.game.curtains.position >= 4:
                    number_position = [496,577]
                    screen.blit(red_number, number_position)
            if s.game.spotted.position == 3:
                #22
                number_position = [178,573]
                screen.blit(red_number, number_position)
                if s.game.curtains.position >= 2:
                    number_position = [390,577]
                    screen.blit(red_number, number_position)
                    
    pygame.display.update()

def blink(args):
    dirty_rects = []
    s = args[0]
    b = args[1]
    sn = args[2]

    if b == 0:
        if sn == 1:
            p = [360,720]
            dirty_rects.append(screen.blit(select_now, p))
        pygame.display.update(dirty_rects)
    else:
        dirty_rects.append(screen.blit(bg_gi, (360,720), pygame.Rect(360,720,138,29)))
        pygame.display.update(dirty_rects)
    b = not b

    args = [s,b,sn]

    s.delay(name="blink", delay=0.1, handler=blink, param=args)

def curtain1_animation(args):
    dirty_rects = []
    s = args[0]
    num = args[1]
    direction = args[2]

    p = [385,431]
    dirty_rects.append(screen.blit(number_card, p, pygame.Rect(p[0],p[1],57,232)))

    if direction == "left":
       p[0] = p[0] + num
    else:
       p[0] = p[0] + 60 - num

    dirty_rects.append(screen.blit(slat, p))
    if s.game.lines.position < 15:
        p = [548,431]
        dirty_rects.append(screen.blit(slat, p))
    if s.game.lines.position < 10:
        p = [494,431]
        dirty_rects.append(screen.blit(slat, p))
 
    backglass_position = [0, 0]
    if (s.game.anti_cheat.status == True):
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],57,232)))
    else:
        dirty_rects.append(screen.blit(bg_off, p, pygame.Rect(p[0],p[1],57,232)))
    

    pygame.display.update(dirty_rects)

def curtain2_animation(args):
    dirty_rects = []
    s = args[0]
    num = args[1]
    direction = args[2]

    p = [440,431]
    dirty_rects.append(screen.blit(number_card, p, pygame.Rect(p[0],p[1],57,232)))

    if direction == "left":
       p[0] = p[0] + num
    else:
       p[0] = p[0] + 60 - num

    dirty_rects.append(screen.blit(slat, p))
    if s.game.lines.position < 15:
        p = [548,431]
        dirty_rects.append(screen.blit(slat, p))
    if s.game.lines.position < 10:
        p = [494,431]
        dirty_rects.append(screen.blit(slat, p))
 
    backglass_position = [0, 0]
    if (s.game.anti_cheat.status == True):
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],57,232)))
    else:
        dirty_rects.append(screen.blit(bg_off, p, pygame.Rect(p[0],p[1],57,232)))
    
    pygame.display.update(dirty_rects)

def curtain3_animation(args):
    dirty_rects = []
    s = args[0]
    num = args[1]
    direction = args[2]

    p = [494,431]
    dirty_rects.append(screen.blit(number_card, p, pygame.Rect(p[0],p[1],57,232)))

    if direction == "left":
       p[0] = p[0] + num
    else:
       p[0] = p[0] + 60 - num

    dirty_rects.append(screen.blit(slat, p))

    if s.game.lines.position < 15:
        p = [548,431]
        dirty_rects.append(screen.blit(slat, p))
    if s.game.lines.position < 5:
        p = [440,431]
        dirty_rects.append(screen.blit(slat, p))
    if s.game.lines.position < 5:
        p = [385,431]
        dirty_rects.append(screen.blit(slat, p))
 
    backglass_position = [0, 0]
    if (s.game.anti_cheat.status == True):
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],100,232)))
    else:
        dirty_rects.append(screen.blit(bg_off, p, pygame.Rect(p[0],p[1],100,232)))
    
    
    pygame.display.update(dirty_rects)

def curtain4_animation(args):
    dirty_rects = []
    s = args[0]
    num = args[1]
    direction = args[2]

    p = [548,431]
    number_card_position = [119,435]
    dirty_rects.append(screen.blit(number_card, number_card_position))

    if direction == "left":
       p[0] = p[0] + num
    else:
       p[0] = p[0] + 60 - num

    dirty_rects.append(screen.blit(slat, p))

    backglass_position = [0, 0]
    if (s.game.anti_cheat.status == True):
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],57,232)))
    else:
        dirty_rects.append(screen.blit(bg_off, p, pygame.Rect(p[0],p[1],57,232)))
    
    
    pygame.display.update(dirty_rects)

def eb_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]


    if s.game.extra_ball.position < 1:
        dirty_rects.append(screen.blit(bg_gi, (131,944), pygame.Rect(131,944,49,35)))
    if s.game.extra_ball.position < 2:
        dirty_rects.append(screen.blit(bg_gi, (181,944), pygame.Rect(181,944,68,33)))
    if s.game.extra_ball.position < 3:
        dirty_rects.append(screen.blit(bg_gi, (249,944), pygame.Rect(249,944,68,33)))
    if s.game.extra_ball.position < 4:
        dirty_rects.append(screen.blit(bg_gi, (320,944), pygame.Rect(320,944,49,35)))
    if s.game.extra_ball.position < 5:
        dirty_rects.append(screen.blit(bg_gi, (370,944), pygame.Rect(370,944,68,33)))
    if s.game.extra_ball.position < 6:
        dirty_rects.append(screen.blit(bg_gi, (437,944), pygame.Rect(437,944,68,33)))
    if s.game.extra_ball.position < 7:
        dirty_rects.append(screen.blit(bg_gi, (510,944), pygame.Rect(510,944,49,35)))
    if s.game.extra_ball.position < 8:
        dirty_rects.append(screen.blit(bg_gi, (560,944), pygame.Rect(560,944,68,33)))
    if s.game.extra_ball.position < 9:
        dirty_rects.append(screen.blit(bg_gi, (628,944), pygame.Rect(628,944,68,33)))
    pygame.display.update(dirty_rects)

    if num in [0,25,14,49,24,50]:
        if s.game.extra_ball.position < 1:
            p = [131,944]
            dirty_rects.append(screen.blit(number_eb, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [39,1,26,15]:
        if s.game.extra_ball.position < 2:
            p = [181,944]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [3,4,17,28,29,40]:
        if s.game.extra_ball.position < 3:
            p = [249,944]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [5,18,30,43]:
        if s.game.extra_ball.position < 4:
            p = [320,944]
            dirty_rects.append(screen.blit(number_eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [7,8,19,32,33,44]:
        if s.game.extra_ball.position < 5:
            p = [370,944]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [9,10,20,34,35,45]:
        if s.game.extra_ball.position < 6:
            p = [437,944]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [11,21,36,46]:
        if s.game.extra_ball.position < 7:
            p = [510,944]
            dirty_rects.append(screen.blit(number_eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [12,22,37,47]:
        if s.game.extra_ball.position < 8:
            p = [560,944]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [2,6,13,16,23,27,31,38,41,48]:
        if s.game.extra_ball.position < 9:
            p = [628,944]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return

def clear_odds(s, num):
    global screen

    dirty_rects = []


    if s.game.odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (20,852), pygame.Rect(20,852,46,70)))
    if s.game.odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (63,818), pygame.Rect(63,818,33,77)))
    if s.game.odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (129,818), pygame.Rect(129,818,48,78)))
    if s.game.odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (184,834), pygame.Rect(184,834,38,79)))
    if s.game.odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (245,808), pygame.Rect(245,808,48,83)))
    if s.game.odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (304,823), pygame.Rect(304,823,40,92)))
    if s.game.odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (363,808), pygame.Rect(363,808,39,80)))
    if s.game.odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (420,834), pygame.Rect(420,834,49,77)))
    if s.game.odds.position != 9:
        dirty_rects.append(screen.blit(bg_gi, (494,813), pygame.Rect(494,813,40,78)))

    pygame.display.update(dirty_rects)

def draw_odds_animation(s, num):
    global screen
    dirty_rects = []

    if num in [2,3,12,27,28,37]:
        if s.game.odds.position != 1:
            p = [20,852]
            dirty_rects.append(screen.blit(o1, p))
            pygame.display.update(dirty_rects)
            return
    if num in [4,5,29,30]:
        if s.game.odds.position != 2:
            p = [63,818]
            dirty_rects.append(screen.blit(o2, p))
            pygame.display.update(dirty_rects)
            return
    if num in [6,7,20,21,31,32,45,46]:
        if s.game.odds.position != 3:
            p = [129,818]
            dirty_rects.append(screen.blit(o3, p))
            pygame.display.update(dirty_rects)
            return
    if num in [8,9,33,34]:
        if s.game.odds.position != 4:
            p = [184,834]
            dirty_rects.append(screen.blit(o4, p))
            pygame.display.update(dirty_rects)
            return
    if num in [10,11,22,23,35,36,47,48]:
        if s.game.odds.position != 5:
            p = [245,808]
            dirty_rects.append(screen.blit(o5, p))
            pygame.display.update(dirty_rects)
            return
    if num in [12,13,24,25,37,38,49,0]:
        if s.game.odds.position != 6:
            p = [304,823]
            dirty_rects.append(screen.blit(o6, p))
            pygame.display.update(dirty_rects)
            return
    if num in [14,15,26,39,40,1]:
        if s.game.odds.position != 7:
            p = [363,808]
            dirty_rects.append(screen.blit(o7, p))
            pygame.display.update(dirty_rects)
            return
    if num in [16,17,41,42]:
        if s.game.odds.position != 8:
            p = [420,834]
            dirty_rects.append(screen.blit(o8, p))
            pygame.display.update(dirty_rects)
            return
    if num in [18,19,43,44]:
        if s.game.odds.position != 9:
            p = [494,813]
            dirty_rects.append(screen.blit(o9, p))
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

    if s.game.red_three_as_four.status == False:
        dirty_rects.append(screen.blit(bg_gi, (591,860), pygame.Rect(591,860,108,78)))
    if s.game.yellow_three_as_four.status == False:
        dirty_rects.append(screen.blit(bg_gi, (594,795), pygame.Rect(594,795,105,70)))
    if s.game.green_three_as_five.status == False:
        dirty_rects.append(screen.blit(bg_gi, (594,720), pygame.Rect(594,720,107,77)))
    if s.game.lines.position < 5:
        dirty_rects.append(screen.blit(bg_gi, (131,761), pygame.Rect(131,761,83,43)))
    if s.game.lines.position < 10:
        dirty_rects.append(screen.blit(bg_gi, (314,761), pygame.Rect(314,761,83,43)))
    if s.game.lines.position < 15:
        dirty_rects.append(screen.blit(bg_gi, (500,760), pygame.Rect(500,760,83,43)))
    if s.game.spotted_numbers.position < 6:
        dirty_rects.append(screen.blit(bg_gi, (274,672), pygame.Rect(274,672,89,77)))
    if s.game.corners.status == False:
        dirty_rects.append(screen.blit(bg_gi, (17,599), pygame.Rect(17,599,81,72)))
    if s.game.super_corners.status == False:
        dirty_rects.append(screen.blit(bg_gi, (17,525), pygame.Rect(17,525,81,72)))

    pygame.display.update(dirty_rects)


def draw_feature_animation(s, num):
    global screen
    dirty_rects = []

    if num in [14,15,39,40]:
        if s.game.red_three_as_four.status == False:
            p = [591,860]
            dirty_rects.append(screen.blit(red, p))
            pygame.display.update(dirty_rects)
            return
    if num in [16,17,41,42]:
        if s.game.yellow_three_as_four.status == False:
            p = [594,795]
            dirty_rects.append(screen.blit(yellow, p))
            pygame.display.update(dirty_rects)
            return
    if num in [18,19,43,44]:
        if s.game.green_three_as_five.status == False:
            p = [594,720]
            dirty_rects.append(screen.blit(yellow, p))
            pygame.display.update(dirty_rects)
            return
    if num in [20,21,45,46]:
        if s.game.lines.position < 5:
            p = [131,761]
            dirty_rects.append(screen.blit(card, p))
            pygame.display.update(dirty_rects)
            return
    if num in [22,23,47,48]:
        if s.game.lines.position < 10:
            p = [314,761]
            dirty_rects.append(screen.blit(card, p))
            pygame.display.update(dirty_rects)
            return
    if num in [12,13,24,25,37,38,49,0]:
        if s.game.lines.position < 15:
            p = [500,760]
            dirty_rects.append(screen.blit(card, p))
            pygame.display.update(dirty_rects)
            return
    if num in [6,7,31,32]:
        if s.game.spotted_numbers.position < 6:
            p = [274,672]
            dirty_rects.append(screen.blit(spotted_numbers, p))
            pygame.display.update(dirty_rects)
            return
    if num in [4,5,29,30]:
        if s.game.corners.status == False:
            p = [17,599]
            dirty_rects.append(screen.blit(c, p))
            pygame.display.update(dirty_rects)
            return
    if num in [2,3,27,28]:
        if s.game.super_corners.status == False:
            p = [17,525]
            dirty_rects.append(screen.blit(c, p))
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
