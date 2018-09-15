
import pygame
import random

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

meter = pygame.image.load('graphics/assets/black_register_cover.png').convert()
odds = pygame.image.load('zodiac/assets/odds.png').convert_alpha()
eb = pygame.image.load('zodiac/assets/eb.png').convert_alpha()
eb_number = pygame.image.load('zodiac/assets/eb_number.png').convert_alpha()
extra_balls = pygame.image.load('zodiac/assets/extra_balls.png').convert_alpha()
time = pygame.image.load('zodiac/assets/time.png').convert_alpha()
ml_letter = pygame.image.load('zodiac/assets/ml_letter.png').convert_alpha()
ml_arrow = pygame.image.load('zodiac/assets/ml_arrow.png').convert_alpha()
ml_a = pygame.image.load('zodiac/assets/ml_a.png').convert_alpha()
ml_b = pygame.image.load('zodiac/assets/ml_b.png').convert_alpha()
ml_c = pygame.image.load('zodiac/assets/ml_c.png').convert_alpha()
select_now = pygame.image.load('zodiac/assets/select_now.png').convert_alpha()
tilt = pygame.image.load('zodiac/assets/tilt.png').convert_alpha()
button = pygame.image.load('zodiac/assets/pap.png').convert_alpha()
red_double = pygame.image.load('zodiac/assets/red_double.png').convert_alpha()
green_double = pygame.image.load('zodiac/assets/green_double.png').convert_alpha()
yellow_double = pygame.image.load('zodiac/assets/yellow_double.png').convert_alpha()
blue_double = pygame.image.load('zodiac/assets/blue_double.png').convert_alpha()
four_stars = pygame.image.load('zodiac/assets/four_stars.png').convert_alpha()
six_stars = pygame.image.load('zodiac/assets/six_stars.png').convert_alpha()
three_stars = pygame.image.load('zodiac/assets/three_stars.png').convert_alpha()
three_red = pygame.image.load('zodiac/assets/three_red.png').convert_alpha()
two_red = pygame.image.load('zodiac/assets/two_red.png').convert_alpha()
red_letter = pygame.image.load('zodiac/assets/red_letter.png').convert_alpha()
letter1 = pygame.image.load('zodiac/assets/letter1.png').convert_alpha()
letter2 = pygame.image.load('zodiac/assets/letter2.png').convert_alpha()
letter3 = pygame.image.load('zodiac/assets/letter3.png').convert_alpha()
letter4 = pygame.image.load('zodiac/assets/letter4.png').convert_alpha()
letter5 = pygame.image.load('zodiac/assets/letter5.png').convert_alpha()
letter6 = pygame.image.load('zodiac/assets/letter6.png').convert_alpha()
red_letter1 = pygame.image.load('zodiac/assets/red_letter1.png').convert_alpha()
red_letter2 = pygame.image.load('zodiac/assets/red_letter2.png').convert_alpha()
red_letter3 = pygame.image.load('zodiac/assets/red_letter3.png').convert_alpha()
red_letter4 = pygame.image.load('zodiac/assets/red_letter4.png').convert_alpha()
red_letter5 = pygame.image.load('zodiac/assets/red_letter5.png').convert_alpha()
red_letter6 = pygame.image.load('zodiac/assets/red_letter6.png').convert_alpha()
number_card = pygame.image.load('zodiac/assets/number_card.png').convert_alpha()
number = pygame.image.load('zodiac/assets/number.png').convert_alpha()
columnb1 = pygame.image.load('zodiac/assets/columnb1.png').convert_alpha()
columnb2 = pygame.image.load('zodiac/assets/columnb2.png').convert_alpha()
columna = pygame.image.load('zodiac/assets/columna.png').convert_alpha()
columnc1 = pygame.image.load('zodiac/assets/columnc1.png').convert_alpha()
columnc2 = pygame.image.load('zodiac/assets/columnc2.png').convert_alpha()
double_triple = pygame.image.load('zodiac/assets/double_triple.png').convert_alpha()
bg_menu = pygame.image.load('zodiac/assets/zodiac_menu.png').convert_alpha()
bg_gi = pygame.image.load('zodiac/assets/zodiac_gi.png').convert_alpha()
bg_off = pygame.image.load('zodiac/assets/zodiac_off.png').convert_alpha()


class scorereel():
    """ Score Reels are used to count replays """
    def __init__(self, pos, image):
        self.position = pos
        self.default_y = self.position[1]
        self.image = pygame.image.load(image).convert()

reel1 = scorereel([105,809], "graphics/assets/white_reel.png")
reel10 = scorereel([86,809], "graphics/assets/white_reel.png")
reel100 = scorereel([67,809], "graphics/assets/white_reel.png")
reel1000 = scorereel([48,809], "graphics/assets/white_reel.png")

def display(s, replays=0, menu=False):
    
    meter.set_colorkey((255,0,252))
    meter_position = [39,809]

    screen.blit(reel1.image, reel1.position)
    screen.blit(reel10.image, reel10.position)
    screen.blit(reel100.image, reel100.position)
    screen.blit(reel1000.image, reel1000.position)
    screen.blit(meter, meter_position)

    if s.game.line2.position == 0:
        p = [233,368]
        screen.blit(columnb1, p)
        p = [286,369]
        screen.blit(columnb2, p)
    else:
        p = [233,368]
        screen.blit(columnb2, p)
        p = [286,369]
        screen.blit(columnb1, p)

    if s.game.line1.position == 0 or s.game.line1.position == 2:
        p = [337,318]
        screen.blit(columna, p)
    elif s.game.line1.position == 1:
        p = [337,368]
        screen.blit(columna, p)
    else:
        p = [337,269]
        screen.blit(columna, p)

    if s.game.line3.position == 0:
        p = [389,368]
        screen.blit(columnc1, p)
        p = [440,369]
        screen.blit(columnc2, p)
    else:
        p = [389,368]
        screen.blit(columnc2, p)
        p = [440,369]
        screen.blit(columnc1, p)


    nc_p = [228,368]
    screen.blit(number_card, nc_p)

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

    if s.game.eb_play.status == True:
        eb_position = [34,1041]
        screen.blit(extra_balls, eb_position)

    if s.game.extra_ball.position >= 1:
        eb_position = [140,1040]
        screen.blit(eb_number, eb_position)
    if s.game.extra_ball.position >= 2:
        eb_position = [188,1042]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 3:
        eb_position = [252,1044]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 4:
        eb_position = [318,1044]
        screen.blit(eb_number, eb_position)
    if s.game.extra_ball.position >= 5:
        eb_position = [369,1044]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 6:
        eb_position = [432,1044]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 7:
        eb_position = [496,1044]
        screen.blit(eb_number, eb_position)
    if s.game.extra_ball.position >= 8:
        eb_position = [546,1044]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 9:
        eb_position = [609,1041]
        screen.blit(eb, eb_position)

    if s.game.red_star.status == True:
        rs_position = [559,462]
        screen.blit(time, rs_position)
    if s.game.yellow_star.status == True:
        rs_position = [559,517]
        screen.blit(time, rs_position)

    if s.game.mystic_lines.position >= 4 or s.game.two_red_letter.status == True or s.game.three_red_letter.status == True:
        if s.game.selection_feature.position < 7:
            bfp = [559,575]
            screen.blit(time, bfp)
        elif s.game.selection_feature.position in [7,8]:
            bfp = [559,408]
            screen.blit(time, bfp)
        elif s.game.selection_feature.position == 9:
            bfp = [559,351]
            screen.blit(time, bfp)

    if s.game.ball_count.position < 1:
        if s.game.odds_only.status == True:
            b = [12,880]
            screen.blit(button, b)
        elif s.game.features.status == True:
            b = [12,923]
            screen.blit(button, b)
        else:
            b = [14,965]
            screen.blit(button, b)


    if s.game.mystic_lines.position == 1:
        p = [198,708]
        screen.blit(ml_arrow, p)
    if s.game.mystic_lines.position == 2:
        p = [230,708]
        screen.blit(ml_arrow, p)
    if s.game.mystic_lines.position == 3:
        p = [263,708]
        screen.blit(ml_arrow, p)
    if s.game.mystic_lines.position >= 4:
        p = [290,700]
        screen.blit(ml_a, p)
        p = [338,591]
        screen.blit(ml_letter, p)
    if s.game.mystic_lines.position == 5:
        p = [329,708]
        screen.blit(ml_arrow, p)
    if s.game.mystic_lines.position == 6:
        p = [362,708]
        screen.blit(ml_arrow, p)
    if s.game.mystic_lines.position >= 7:
        p = [392,700]
        screen.blit(ml_b, p)
        p = [263,591]
        screen.blit(ml_letter, p)
    if s.game.mystic_lines.position == 8:
        p = [430,708]
        screen.blit(ml_arrow, p)
    if s.game.mystic_lines.position == 9:
        p = [462,708]
        screen.blit(ml_arrow, p)
    if s.game.mystic_lines.position == 10:
        p = [488,700]
        screen.blit(ml_c, p)
        p = [417,591]
        screen.blit(ml_letter, p)

    if s.game.mystic_lines.position >= 4:
        t = 3
        if s.game.selection_feature.position in [7,8]:
            t = 4
        if s.game.selection_feature.position == 9:
            t = 5
        if s.game.ball_count.position == t:
            s.cancel_delayed(name="blink")
            blink([s,1,1])
        else:
            s.cancel_delayed(name="blink")


    if s.game.tilt.status == False:
        if s.holes:
            if 1 in s.holes:
                if s.game.line2.position == 0:
                    p = [287,471]
                    screen.blit(number, p)
                else:
                    p = [235,471]
                    screen.blit(number, p)
            if 2 in s.holes:
                if s.game.line3.position == 0:
                    p = [389,471]
                    screen.blit(number, p)
                else:
                    p = [440,471]
                    screen.blit(number, p)
            if 3 in s.holes:
                if s.game.line3.position == 0:
                    p = [389,522]
                    screen.blit(number, p)
                else:
                    p = [441,521]
                    screen.blit(number, p)
            if 4 in s.holes:
                if s.game.line2.position == 0:
                    p = [287,371]
                    screen.blit(number, p)
                else:
                    p = [236,371]
                    screen.blit(number, p)
            if 5 in s.holes:
                if s.game.line1.position == 0 or s.game.line1.position == 2:
                    p = [336,521]
                    screen.blit(number, p)
                elif s.game.line1.position == 1:
                    p = [337,371]
                    screen.blit(number, p)
                else:
                    p = [337,471]
                    screen.blit(number, p)
            if 6 in s.holes:
                if s.game.line3.position == 0:
                    p = [389,421]
                    screen.blit(number, p)
                else:
                    p = [441,419]
                    screen.blit(number, p)
            if 7 in s.holes:
                if s.game.line1.position == 0 or s.game.line1.position == 2:
                    p = [337,370]
                    screen.blit(number, p)
                elif s.game.line1.position == 1:
                    p = [337,420]
                    screen.blit(number, p)
                else:
                    p = [335,521]
                    screen.blit(number, p)
            if 8 in s.holes:
                if s.game.line2.position == 0:
                    p = [286,421]
                    screen.blit(number, p)
                else:
                    p = [233,420]
                    screen.blit(number, p)
            if 9 in s.holes:
                if s.game.line3.position == 0:
                    p = [389,369]
                    screen.blit(number, p)
                else:
                    p = [440,371]
                    screen.blit(number, p)
            if 10 in s.holes:
                if s.game.line3.position == 0:
                    p = [440,521]
                    screen.blit(number, p)
                else:
                    p = [389,521]
                    screen.blit(number, p)
            if 11 in s.holes:
                if s.game.line2.position == 0:
                    p = [233,420]
                    screen.blit(number, p)
                else:
                    p = [286,420]
                    screen.blit(number, p)
            if 12 in s.holes:
                if s.game.line1.position in [0,2]:
                    p = [336,419]
                    screen.blit(number, p)
                elif s.game.line1.position == 1:
                    p = [336,471]
                    screen.blit(number, p)
                else:
                    p = [337,370]
                    screen.blit(number, p)
            if 13 in s.holes:
                if s.game.line3.position == 0:
                    p = [440,420]
                    screen.blit(number, p)
                else:
                    p = [388,420]
                    screen.blit(number, p)
            if 14 in s.holes:
                if s.game.line2.position == 0:
                    p = [285,521]
                    screen.blit(number, p)
                else:
                    p = [233,521]
                    screen.blit(number, p)
            if 15 in s.holes:
                if s.game.line2.position == 0:
                    p = [234,470]
                    screen.blit(number, p)
                else:
                    p = [286,471]
                    screen.blit(number, p)
            if 16 in s.holes:
                if s.game.line2.position == 0:
                    p = [234,521]
                    screen.blit(number, p)
                else:
                    p = [285,521]
                    screen.blit(number, p)
            if 17 in s.holes:
                if s.game.line3.position == 0:
                    p = [440,370]
                    screen.blit(number, p)
                else:
                    p = [389,370]
                    screen.blit(number, p)
            if 18 in s.holes:
                if s.game.line2.position == 0:
                    p = [235,370]
                    screen.blit(number, p)
                else:
                    p = [286,370]
                    screen.blit(number, p)
            if 19 in s.holes:
                if s.game.line3.position == 0:
                    p = [441,470]
                    screen.blit(number, p)
                else:
                    p = [389,470]
                    screen.blit(number, p)
            if 20 in s.holes:
                if s.game.line1.position in [0,2]:
                    p = [337,471]
                    screen.blit(number, p)
                elif s.game.line1.position == 1:
                    p = [336,521]
                    screen.blit(number, p)
                else:
                    p = [336,419]
                    screen.blit(number, p)

    if s.game.red_odds.position == 1:
        o = [180,773]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 2:
        o = [228,773]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 3:
        o = [280,773]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 4:
        o = [329,773]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 5:
        o = [380,773]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 6:
        o = [429,773]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 7:
        o = [478,773]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 8:
        o = [530,773]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 9:
        o = [581,773]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 10:
        o = [630,773]
        screen.blit(odds, o)

    if s.game.yellow_odds.position == 1:
        o = [180,905]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 2:
        o = [228,905]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 3:
        o = [280,905]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 4:
        o = [329,905]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 5:
        o = [380,905]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 6:
        o = [429,905]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 7:
        o = [478,905]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 8:
        o = [530,905]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 9:
        o = [581,905]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 10:
        o = [630,905]
        screen.blit(odds, o)

    if s.game.green_odds.position == 1:
        o = [180,842]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 2:
        o = [228,842]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 3:
        o = [280,842]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 4:
        o = [329,842]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 5:
        o = [380,842]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 6:
        o = [429,842]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 7:
        o = [478,842]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 8:
        o = [530,842]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 9:
        o = [581,842]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 10:
        o = [630,840]
        screen.blit(odds, o)

    if s.game.blue_odds.position == 1:
        o = [180,970]
        screen.blit(odds, o)
    elif s.game.blue_odds.position == 2:
        o = [228,970]
        screen.blit(odds, o)
    elif s.game.blue_odds.position == 3:
        o = [280,970]
        screen.blit(odds, o)
    elif s.game.blue_odds.position == 4:
        o = [329,970]
        screen.blit(odds, o)
    elif s.game.blue_odds.position == 5:
        o = [380,970]
        screen.blit(odds, o)
    elif s.game.blue_odds.position == 6:
        o = [429,970]
        screen.blit(odds, o)
    elif s.game.blue_odds.position == 7:
        o = [478,970]
        screen.blit(odds, o)
    elif s.game.blue_odds.position == 8:
        o = [530,970]
        screen.blit(odds, o)
    elif s.game.blue_odds.position == 9:
        o = [579,970]
        screen.blit(odds, o)
    elif s.game.blue_odds.position == 10:
        o = [627,970]
        screen.blit(odds, o)

    p = [33,209]
    screen.blit(letter1, p)
    p = [85,210]
    screen.blit(letter2, p)
    p = [124,201]
    screen.blit(letter3, p)
    p = [180,212]
    screen.blit(letter4, p)
    p = [220,207]
    screen.blit(letter5, p)
    p = [285,213]
    screen.blit(letter6, p)

    if s.game.red_odds.position < 5:
        p = [33,209]
        screen.blit(red_letter1, p)
    if s.game.red_odds.position in [5,6]:
        p = [85,210]
        screen.blit(red_letter2, p)
    if s.game.red_odds.position == 7:
        p = [124,201]
        screen.blit(red_letter3, p)
    if s.game.red_odds.position == 8:
        p = [180,212]
        screen.blit(red_letter4, p)
    if s.game.red_odds.position == 9:
        p = [220,207]
        screen.blit(red_letter5, p)
    if s.game.red_odds.position == 10:
        p = [285,213]
        screen.blit(red_letter6, p)

    if s.game.two_red_letter.status == True:
        p = [8,400]
        screen.blit(red_letter, p)
        p = [85,347]
        screen.blit(two_red, p)
    if s.game.three_red_letter.status == True:
        p = [8,400]
        screen.blit(red_letter, p)
        p = [10,348]
        screen.blit(three_red, p)

    if s.game.three_stars.status == True:
        p = [8,444]
        screen.blit(four_stars, p)
        p = [8,498]
        screen.blit(three_stars, p)
    if s.game.six_stars.status == True:
        p = [8,444]
        screen.blit(four_stars, p)
        p = [84,496]
        screen.blit(six_stars, p)

    if s.game.double_red.status == True:
        p = [8,560]
        screen.blit(red_double, p)
    if s.game.double_yellow.status == True:
        p = [84,557]
        screen.blit(yellow_double, p)
    if s.game.double_green.status == True:
        p = [9,663]
        screen.blit(green_double, p)
    if s.game.double_blue.status == True:
        p = [87,665]
        screen.blit(blue_double, p)

    if s.game.triple.status == False and (s.game.double_red.status == True or s.game.double_yellow.status == True or s.game.double_green.status == True or s.game.double_blue.status == True):
        p = [43,663]
        screen.blit(double_triple, p)

    if s.game.triple.status == True and (s.game.double_red.status == True or s.game.double_yellow.status == True or s.game.double_green.status == True or s.game.double_blue.status == True):
        p = [43,607]
        screen.blit(double_triple, p)

    if s.game.tilt.status == True:
        tilt_position = [551,317]
        screen.blit(tilt, tilt_position)

    pygame.display.update()

def blink(args):
    dirty_rects = []
    s = args[0]
    b = args[1]
    sn = args[2]

    if b == 0:
        if sn == 1:
            p = [522,719]
            dirty_rects.append(screen.blit(select_now, p))
        pygame.display.update(dirty_rects)
    else:
        dirty_rects.append(screen.blit(bg_gi, (522,719), pygame.Rect(522,719,149,40)))
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
        if s.game.line1.position == 0:
            dirty_rects.append(screen.blit(columna, (337, 269 - num)))
        elif s.game.line1.position == 1:
            dirty_rects.append(screen.blit(columna, (337, 318 - num)))
        elif s.game.line1.position == 2:
            dirty_rects.append(screen.blit(columna, (337, 368 + num)))
        elif s.game.line1.position == 3:
            dirty_rects.append(screen.blit(columna, (337, 318 + num)))
    
        nc_p = [228,368]
        dirty_rects.append(screen.blit(number_card, nc_p))
        if (s.game.anti_cheat.status == True):
            dirty_rects.append(screen.blit(bg_gi, (224,264), pygame.Rect(224,264,270,408)))
        else:
            dirty_rects.append(screen.blit(bg_off, (224,264), pygame.Rect(224,264,270,408)))
    

        dirty_rects.append(screen.blit(bg_gi, (25,200), pygame.Rect(25,200,312,97)))
        

        p = [33,209]
        dirty_rects.append(screen.blit(letter1, p))
        p = [85,210]
        dirty_rects.append(screen.blit(letter2, p))
        p = [124,201]
        dirty_rects.append(screen.blit(letter3, p))
        p = [180,212]
        dirty_rects.append(screen.blit(letter4, p))
        p = [220,207]
        dirty_rects.append(screen.blit(letter5, p))
        p = [285,213]
        dirty_rects.append(screen.blit(letter6, p))

        if s.game.red_odds.position < 5:
            p = [33,209]
            dirty_rects.append(screen.blit(red_letter1, p))
        if s.game.red_odds.position in [5,6]:
            p = [85,210]
            dirty_rects.append(screen.blit(red_letter2, p))
        if s.game.red_odds.position == 7:
            p = [124,201]
            dirty_rects.append(screen.blit(red_letter3, p))
        if s.game.red_odds.position == 8:
            p = [180,212]
            dirty_rects.append(screen.blit(red_letter4, p))
        if s.game.red_odds.position == 9:
            p = [220,207]
            dirty_rects.append(screen.blit(red_letter5, p))
        if s.game.red_odds.position == 10:
            p = [285,213]
            dirty_rects.append(screen.blit(red_letter6, p))

#        p = [180,212]
#        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],51,80)))
#        dirty_rects.append(screen.blit(letter4, p))
#        p = [220,207]
#        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],82,86)))
#        dirty_rects.append(screen.blit(letter5, p))
#        p = [180,212]
#        dirty_rects.append(screen.blit(letter4, p))
#        p = [285,213]
#        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],51,77)))
#        dirty_rects.append(screen.blit(letter6, p))
#        p = [220,207]
#        dirty_rects.append(screen.blit(letter5, p))

#        if s.game.red_odds.position == 6:
#            p = [180,212]
#            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],51,80)))
#            dirty_rects.append(screen.blit(letter4, p))
#            dirty_rects.append(screen.blit(red_letter4, p))
#        if s.game.red_odds.position == 7:
#            p = [220,207]
#            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],82,86)))
#            dirty_rects.append(screen.blit(letter5, p))
#            dirty_rects.append(screen.blit(red_letter5, p))
#        if s.game.red_odds.position == 8:
#            p = [285,213]
#            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],51,77)))
#            dirty_rects.append(screen.blit(letter6, p))
#            dirty_rects.append(screen.blit(red_letter6, p))

        if s.game.mystic_lines.position == 1:
            p = [198,708]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],25,29)))
            dirty_rects.append(screen.blit(ml_arrow, p))
        if s.game.mystic_lines.position == 2:
            p = [230,708]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],25,29)))
            dirty_rects.append(screen.blit(ml_arrow, p))
        if s.game.mystic_lines.position == 3:
            p = [263,708]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],25,29)))
            dirty_rects.append(screen.blit(ml_arrow, p))
        if s.game.mystic_lines.position >= 4:
            p = [290,700]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],38,46)))
            dirty_rects.append(screen.blit(ml_a, p))
            p = [338,591]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],44,50)))
            dirty_rects.append(screen.blit(ml_letter, p))
        if s.game.mystic_lines.position == 5:
            p = [329,708]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],25,29)))
            dirty_rects.append(screen.blit(ml_arrow, p))
        if s.game.mystic_lines.position == 6:
            p = [362,708]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],25,29)))
            dirty_rects.append(screen.blit(ml_arrow, p))
        if s.game.mystic_lines.position >= 7:
            p = [392,700]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],38,46)))
            dirty_rects.append(screen.blit(ml_b, p))
            p = [263,591]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],44,50)))
            dirty_rects.append(screen.blit(ml_letter, p))
        if s.game.mystic_lines.position == 8:
            p = [430,708]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],25,29)))
            dirty_rects.append(screen.blit(ml_arrow, p))
        if s.game.mystic_lines.position == 9:
            p = [462,708]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],25,29)))
            dirty_rects.append(screen.blit(ml_arrow, p))
        if s.game.mystic_lines.position == 10:
            p = [488,700]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],38,46)))
            dirty_rects.append(screen.blit(ml_c, p))
            p = [417,591]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],44,50)))
            dirty_rects.append(screen.blit(ml_letter, p))
    pygame.display.update(dirty_rects)

def line2_animation(args):
    dirty_rects = []
    s = args[0]
    num = args[1]
    line = args[2]
    if line == 2:
        if s.game.line2.position == 0:
            dirty_rects.append(screen.blit(columnb2, (233 - num, 369)))
            dirty_rects.append(screen.blit(columnb1, (286 + num, 369)))
        elif s.game.line2.position == 1:
            dirty_rects.append(screen.blit(columnb1, (233 - num, 369)))
            dirty_rects.append(screen.blit(columnb2, (286 + num, 369)))
     
        nc_p = [228,368]
        dirty_rects.append(screen.blit(number_card, nc_p))
        if (s.game.anti_cheat.status == True):
            dirty_rects.append(screen.blit(bg_gi, (229,369), pygame.Rect(229,369,274,212)))
        else:
            dirty_rects.append(screen.blit(bg_off, (229,369), pygame.Rect(229,369,274,212)))

        if s.game.mystic_lines.position == 1:
            p = [198,708]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],25,29)))
            dirty_rects.append(screen.blit(ml_arrow, p))
        if s.game.mystic_lines.position == 2:
            p = [230,708]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],25,29)))
            dirty_rects.append(screen.blit(ml_arrow, p))
        if s.game.mystic_lines.position == 3:
            p = [263,708]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],25,29)))
            dirty_rects.append(screen.blit(ml_arrow, p))
        if s.game.mystic_lines.position >= 4:
            p = [290,700]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],38,46)))
            dirty_rects.append(screen.blit(ml_a, p))
            p = [338,591]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],44,50)))
            dirty_rects.append(screen.blit(ml_letter, p))
        if s.game.mystic_lines.position == 5:
            p = [329,708]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],25,29)))
            dirty_rects.append(screen.blit(ml_arrow, p))
        if s.game.mystic_lines.position == 6:
            p = [362,708]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],25,29)))
            dirty_rects.append(screen.blit(ml_arrow, p))
        if s.game.mystic_lines.position >= 7:
            p = [392,700]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],38,46)))
            dirty_rects.append(screen.blit(ml_b, p))
            p = [263,591]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],44,50)))
            dirty_rects.append(screen.blit(ml_letter, p))
        if s.game.mystic_lines.position == 8:
            p = [430,708]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],25,29)))
            dirty_rects.append(screen.blit(ml_arrow, p))
        if s.game.mystic_lines.position == 9:
            p = [462,708]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],25,29)))
            dirty_rects.append(screen.blit(ml_arrow, p))
        if s.game.mystic_lines.position == 10:
            p = [488,700]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],38,46)))
            dirty_rects.append(screen.blit(ml_c, p))
            p = [417,591]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],44,50)))
            dirty_rects.append(screen.blit(ml_letter, p))
    pygame.display.update(dirty_rects)

def line3_animation(args):
    dirty_rects = []
    s = args[0]
    num = args[1]
    line = args[2]
    
    if line == 3:
        if s.game.line3.position == 0:
            dirty_rects.append(screen.blit(columnc2, (389 - num, 369)))
            dirty_rects.append(screen.blit(columnc1, (440 + num, 369)))
        elif s.game.line3.position == 1:
            dirty_rects.append(screen.blit(columnc1, (389 - num, 369)))
            dirty_rects.append(screen.blit(columnc2, (440 + num, 369)))

        nc_p = [228,368]
        dirty_rects.append(screen.blit(number_card, nc_p))
        if (s.game.anti_cheat.status == True):
            dirty_rects.append(screen.blit(bg_gi, (389,369), pygame.Rect(389,369,100,212)))
        else:
            dirty_rects.append(screen.blit(bg_off, (389,369), pygame.Rect(389,369,100,212)))

        if s.game.mystic_lines.position == 1:
            p = [198,708]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],25,29)))
            dirty_rects.append(screen.blit(ml_arrow, p))
        if s.game.mystic_lines.position == 2:
            p = [230,708]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],25,29)))
            dirty_rects.append(screen.blit(ml_arrow, p))
        if s.game.mystic_lines.position == 3:
            p = [263,708]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],25,29)))
            dirty_rects.append(screen.blit(ml_arrow, p))
        if s.game.mystic_lines.position >= 4:
            p = [290,700]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],38,46)))
            dirty_rects.append(screen.blit(ml_a, p))
            p = [338,591]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],44,50)))
            dirty_rects.append(screen.blit(ml_letter, p))
        if s.game.mystic_lines.position == 5:
            p = [329,708]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],25,29)))
            dirty_rects.append(screen.blit(ml_arrow, p))
        if s.game.mystic_lines.position == 6:
            p = [362,708]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],25,29)))
            dirty_rects.append(screen.blit(ml_arrow, p))
        if s.game.mystic_lines.position >= 7:
            p = [392,700]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],38,46)))
            dirty_rects.append(screen.blit(ml_b, p))
            p = [263,591]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],44,50)))
            dirty_rects.append(screen.blit(ml_letter, p))
        if s.game.mystic_lines.position == 8:
            p = [430,708]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],25,29)))
            dirty_rects.append(screen.blit(ml_arrow, p))
        if s.game.mystic_lines.position == 9:
            p = [462,708]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],25,29)))
            dirty_rects.append(screen.blit(ml_arrow, p))
        if s.game.mystic_lines.position == 10:
            p = [488,700]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],38,46)))
            dirty_rects.append(screen.blit(ml_c, p))
            p = [417,591]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],44,50)))
            dirty_rects.append(screen.blit(ml_letter, p))
    pygame.display.update(dirty_rects)


def eb_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]
    if s.game.extra_ball.position < 1:
        dirty_rects.append(screen.blit(bg_gi, (140,1040), pygame.Rect(140,1040,50,36)))
    if s.game.extra_ball.position < 2:
        dirty_rects.append(screen.blit(bg_gi, (188,1042), pygame.Rect(188,1042,63,36)))
    if s.game.extra_ball.position < 3:
        dirty_rects.append(screen.blit(bg_gi, (252,1044), pygame.Rect(252,1044,63,36)))
    if s.game.extra_ball.position < 4:
        dirty_rects.append(screen.blit(bg_gi, (318,1044), pygame.Rect(318,1044,50,36)))
    if s.game.extra_ball.position < 5:
        dirty_rects.append(screen.blit(bg_gi, (369,1044), pygame.Rect(369,1044,63,36)))
    if s.game.extra_ball.position < 6:
        dirty_rects.append(screen.blit(bg_gi, (432,1044), pygame.Rect(432,1044,63,36)))
    if s.game.extra_ball.position < 7:
        dirty_rects.append(screen.blit(bg_gi, (496,1044), pygame.Rect(496,1044,50,36)))
    if s.game.extra_ball.position < 8:
        dirty_rects.append(screen.blit(bg_gi, (546,1044), pygame.Rect(546,1044,63,36)))
    if s.game.extra_ball.position < 9:
        dirty_rects.append(screen.blit(bg_gi, (609,1041), pygame.Rect(609,1041,63,36)))
    pygame.display.update(dirty_rects)

    if num in [0,25,14,49]:
        if s.game.extra_ball.position < 1:
            p = [140,1040]
            dirty_rects.append(screen.blit(eb_number, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [39,1,26,15]:
        if s.game.extra_ball.position < 2:
            p = [188,1042]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [3,4,17,28,29,40]:
        if s.game.extra_ball.position < 3:
            p = [252,1044]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [5,18,30,43]:
        if s.game.extra_ball.position < 4:
            p = [318,1044]
            dirty_rects.append(screen.blit(eb_number, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [7,8,19,32,33,44]:
        if s.game.extra_ball.position < 5:
            p = [369,1044]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [9,10,20,34,35,45]:
        if s.game.extra_ball.position < 6:
            p = [432,1044]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [11,21,36,46]:
        if s.game.extra_ball.position < 7:
            p = [496,1044]
            dirty_rects.append(screen.blit(eb_number, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [12,22,37,47]:
        if s.game.extra_ball.position < 8:
            p = [546,1044]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [2,6,13,16,23,27,31,38,41,48]:
        if s.game.extra_ball.position < 9:
            p = [609,1041]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return

def clear_odds(s, num):
    global screen

    dirty_rects = []


    if s.game.triple.status == False:
        dirty_rects.append(screen.blit(bg_gi, (43,607), pygame.Rect(43,607,82,54)))
    if s.game.double_red.status == False:
        dirty_rects.append(screen.blit(bg_gi, (8,560), pygame.Rect(8,560,73,101)))
    if s.game.double_yellow.status == False:
        dirty_rects.append(screen.blit(bg_gi, (84,557), pygame.Rect(84,557,73,101)))
    if s.game.double_green.status == False:
        dirty_rects.append(screen.blit(bg_gi, (9,663), pygame.Rect(9,663,73,101)))
    if s.game.double_blue.status == False:
        dirty_rects.append(screen.blit(bg_gi, (87,665), pygame.Rect(87,665,73,101)))

    if s.game.yellow_odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (228,905), pygame.Rect(228,905,46,61)))
    if s.game.yellow_odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (380,905), pygame.Rect(380,905,46,61)))
    if s.game.yellow_odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (478,905), pygame.Rect(478,905,46,61)))
    if s.game.yellow_odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (530,905), pygame.Rect(530,905,46,61)))
    if s.game.yellow_odds.position != 10:
        dirty_rects.append(screen.blit(bg_gi, (630,905), pygame.Rect(630,905,46,61)))

    if s.game.red_odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (280,773), pygame.Rect(280,773,46,61)))
    if s.game.red_odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (478,773), pygame.Rect(478,773,46,61)))
    if s.game.red_odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (530,773), pygame.Rect(530,773,46,61)))
    if s.game.red_odds.position != 9:
        dirty_rects.append(screen.blit(bg_gi, (581,773), pygame.Rect(581,773,46,61)))
    if s.game.red_odds.position != 10:
        dirty_rects.append(screen.blit(bg_gi, (630,773), pygame.Rect(630,773,46,61)))

    if s.game.green_odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (280,842), pygame.Rect(280,842,46,61)))
    if s.game.green_odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (380,842), pygame.Rect(380,842,46,61)))
    if s.game.green_odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (478,842), pygame.Rect(478,842,46,61)))
    if s.game.green_odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (530,842), pygame.Rect(530,842,46,61)))
    if s.game.green_odds.position != 10:
        dirty_rects.append(screen.blit(bg_gi, (630,840), pygame.Rect(630,840,46,61)))

    if s.game.blue_odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (228,970), pygame.Rect(228,970,46,61)))
    if s.game.blue_odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (380,970), pygame.Rect(380,970,46,61)))
    if s.game.blue_odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (530,970), pygame.Rect(530,970,46,61)))
    if s.game.blue_odds.position != 9:
        dirty_rects.append(screen.blit(bg_gi, (579,970), pygame.Rect(579,970,46,61)))
    if s.game.blue_odds.position != 10:
        dirty_rects.append(screen.blit(bg_gi, (627,970), pygame.Rect(627,970,46,61)))

    pygame.display.update(dirty_rects)

def draw_odds_animation(s, num):
    global screen
    dirty_rects = []


    if num in [5,30]:
        if s.game.triple.status == False:
            p = [43,607]
            dirty_rects.append(screen.blit(double_triple, p))
            pygame.display.update(dirty_rects)
            return
    if num in [7,32]:
        if s.game.double_red.status == False:
            p = [8,560]
            dirty_rects.append(screen.blit(red_double, p))
            pygame.display.update(dirty_rects)
            return
    if num in [11,36]:
        if s.game.double_yellow.status == False:
            p = [84,557]
            dirty_rects.append(screen.blit(yellow_double, p))
            pygame.display.update(dirty_rects)
            return
    if num in [0,25]:
        if s.game.double_green.status == False:
            p = [9,663]
            dirty_rects.append(screen.blit(green_double, p))
            pygame.display.update(dirty_rects)
            return
    if num in [17,42]:
        if s.game.double_blue.status == False:
            p = [87,665]
            dirty_rects.append(screen.blit(blue_double, p))
            pygame.display.update(dirty_rects)
            return

    if num in [4,29]:
        if s.game.yellow_odds.position != 2:
            p = [228,905]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [13,38]:
        if s.game.yellow_odds.position != 5:
            p = [380,905]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [22,47]:
        if s.game.yellow_odds.position != 7:
            p = [478,905]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [19,44]:
        if s.game.yellow_odds.position != 8:
            p = [530,905]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [5,30]:
        if s.game.yellow_odds.position != 10:
            p = [630,905]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
        
    if num in [49,24]:
        if s.game.red_odds.position != 3:
            p = [280,773]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [20,45]:
        if s.game.red_odds.position != 7:
            p = [478,773]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [12,37]:
        if s.game.red_odds.position != 8:
            p = [530,773]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [25,50]:
        if s.game.red_odds.position != 9:
            p = [581,773]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [6,31]:
        if s.game.red_odds.position != 10:
            p = [630,773]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return

    if num in [18,43]:
        if s.game.blue_odds.position != 2:
            p = [228,970]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [3,28]:
        if s.game.blue_odds.position != 5:
            p = [380,970]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [8,33]:
        if s.game.blue_odds.position != 8:
            p = [530,970]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [21,46]:
        if s.game.blue_odds.position != 9:
            p = [579,970]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [10,35]:
        if s.game.blue_odds.position != 10:
            p = [627,970]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return

    if num in [15,40]:
        if s.game.green_odds.position != 3:
            p = [280,842]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [9,34]:
        if s.game.green_odds.position != 5:
            p = [380,842]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [16,41]:
        if s.game.green_odds.position != 7:
            p = [478,842]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [14,39]:
        if s.game.green_odds.position != 8:
            p = [530,842]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [48,23]:
        if s.game.green_odds.position != 10:
            p = [630,840]
            dirty_rects.append(screen.blit(odds, p))
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

    if s.game.mystic_lines.position < 4 and s.game.two_red_letter.status == False and s.game.three_red_letter.status == False and s.game.selection_feature > 7:
        dirty_rects.append(screen.blit(bg_gi, (559,575), pygame.Rect(559,575,122,58)))

    if s.game.selection_feature.position not in [7,8]:
        dirty_rects.append(screen.blit(bg_gi, (559,408), pygame.Rect(559,408,122,58)))
    if s.game.mystic_lines.position < 4 and s.game.two_red_letter.status == False and s.game.three_red_letter.status == False:
        dirty_rects.append(screen.blit(bg_gi, (559,408), pygame.Rect(559,408,122,58)))
    
    if s.game.selection_feature.position < 9:
        dirty_rects.append(screen.blit(bg_gi, (559,351), pygame.Rect(559,351,122,58)))
    if s.game.mystic_lines.position < 4 and s.game.two_red_letter.status == False and s.game.three_red_letter.status == False:
        dirty_rects.append(screen.blit(bg_gi, (559,351), pygame.Rect(559,351,122,58)))

    if s.game.yellow_star.status == False:
        dirty_rects.append(screen.blit(bg_gi, (559,517), pygame.Rect(559,517,122,58)))
    if s.game.red_star.status == False:
        dirty_rects.append(screen.blit(bg_gi, (559,462), pygame.Rect(559,462,122,58)))

    if s.game.three_red_letter.status == False:
        dirty_rects.append(screen.blit(bg_gi, (10,348), pygame.Rect(10,348,76,53)))
    if s.game.two_red_letter.status == False:
        dirty_rects.append(screen.blit(bg_gi, (85,347), pygame.Rect(85,347,76,53)))
    if s.game.three_stars.status == False:
        dirty_rects.append(screen.blit(bg_gi, (8,498), pygame.Rect(8,498,77,32)))
    if s.game.six_stars.status == False:
        dirty_rects.append(screen.blit(bg_gi, (84,496), pygame.Rect(84,496,77,32)))

    if s.game.mystic_lines.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (230,708), pygame.Rect(230,708,25,29)))
    if s.game.mystic_lines.position < 4:
        dirty_rects.append(screen.blit(bg_gi, (338,591), pygame.Rect(338,591,44,50)))
    if s.game.mystic_lines.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (329,708), pygame.Rect(329,708,25,29)))
    if s.game.mystic_lines.position < 7:
        dirty_rects.append(screen.blit(bg_gi, (263,591), pygame.Rect(263,591,44,50)))
    if s.game.mystic_lines.position != 9:
        dirty_rects.append(screen.blit(bg_gi, (462,708), pygame.Rect(462,708,25,29)))
    if s.game.mystic_lines.position < 10:
        dirty_rects.append(screen.blit(bg_gi, (417,591), pygame.Rect(417,591,44,50)))

    pygame.display.update(dirty_rects)


def draw_feature_animation(s, num):
    global screen
    dirty_rects = []
    
    if num in [10,35]:
        if s.game.selection_feature.position not in [1,2,3,4,5,6] and (s.game.mystic_lines.position < 4 and s.game.two_red_letter.status == False and s.game.three_red_letter.status == False):
            p = [559,575]
            dirty_rects.append(screen.blit(time, p))
            pygame.display.update(dirty_rects)
            return
    if num in [9,34]:
        if s.game.selection_feature.position not in [7,8] and (s.game.mystic_lines.position < 4 and s.game.two_red_letter.status == False and s.game.three_red_letter.status == False):
            p = [559,408]
            dirty_rects.append(screen.blit(time, p))
            pygame.display.update(dirty_rects)
            return
    if num in [6,31]:
        if s.game.selection_feature.position not in [9] and (s.game.mystic_lines.position < 4 and s.game.two_red_letter.status == False and s.game.three_red_letter.status == False):
            p = [559,351]
            dirty_rects.append(screen.blit(time, p))
            pygame.display.update(dirty_rects)
            return

    if num in [11,36]:
        if s.game.red_star.status == False:
            p = [559,462]
            dirty_rects.append(screen.blit(time, p))
            pygame.display.update(dirty_rects)
            s.game.coils.redROLamp.pulse(85)
            return
    if num in [4,29]:
        if s.game.yellow_star.status == False:
            p = [559,517]
            dirty_rects.append(screen.blit(time, p))
            pygame.display.update(dirty_rects)
            s.game.coils.yellowROLamp.pulse(85)
            return
    if num in [16,23]:
        if s.game.three_red_letter.status == False:
            p = [10,348]
            dirty_rects.append(screen.blit(three_red, p))
            pygame.display.update(dirty_rects)
            return
    if num in [7,32]:
        if s.game.two_red_letter.status == False:
            p = [85,347]
            dirty_rects.append(screen.blit(two_red, p))
            pygame.display.update(dirty_rects)
            return
    if num in [8,33]:
        if s.game.three_stars.status == False:
            p = [8,498]
            dirty_rects.append(screen.blit(three_stars, p))
            pygame.display.update(dirty_rects)
            return
    if num in [20,45]:
        if s.game.six_stars.status == False:
            p = [84,496]
            dirty_rects.append(screen.blit(six_stars, p))
            pygame.display.update(dirty_rects)
            return
    if num in [13,19,44,38]:
        if s.game.mystic_lines.position != 2:
            p = [230,708]
            dirty_rects.append(screen.blit(ml_arrow, p))
            pygame.display.update(dirty_rects)
            return
    if num in [3,22,28,47]:
        if s.game.mystic_lines.position < 4:
            p = [338,591]
            dirty_rects.append(screen.blit(ml_letter, p))
            pygame.display.update(dirty_rects)
            return
    if num in [18,0,25,43]:
        if s.game.mystic_lines.position != 5:
            p = [329,708]
            dirty_rects.append(screen.blit(ml_arrow, p))
            pygame.display.update(dirty_rects)
            return
    if num in [2,12,27,37]:
        if s.game.mystic_lines.position < 7:
            p = [263,591]
            dirty_rects.append(screen.blit(ml_letter, p))
            pygame.display.update(dirty_rects)
            return
    if num in [5,15,30,40]:
        if s.game.mystic_lines.position != 9:
            p = [462,708]
            dirty_rects.append(screen.blit(ml_arrow, p))
            pygame.display.update(dirty_rects)
            return
    if num in [1,14,26,39]:
        if s.game.mystic_lines.position < 10:
            p = [417,591]
            dirty_rects.append(screen.blit(ml_letter, p))
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

