
import pygame
import random

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

meter = pygame.image.load('graphics/assets/black_register_cover.png').convert()
odds = pygame.image.load('safari/assets/odds.png').convert_alpha()
eb = pygame.image.load('safari/assets/eb.png').convert_alpha()
eb_number = pygame.image.load('safari/assets/eb_number.png').convert_alpha()
extra_balls = pygame.image.load('safari/assets/extra_balls.png').convert_alpha()
time = pygame.image.load('safari/assets/time.png').convert_alpha()
ml_letter = pygame.image.load('safari/assets/ml_letter.png').convert_alpha()
ml_arrow = pygame.image.load('safari/assets/ml_arrow.png').convert_alpha()
ml_a = pygame.image.load('safari/assets/ml_a.png').convert_alpha()
ml_b = pygame.image.load('safari/assets/ml_b.png').convert_alpha()
ml_c = pygame.image.load('safari/assets/ml_c.png').convert_alpha()
select_now = pygame.image.load('safari/assets/select_now.png').convert_alpha()
tilt = pygame.image.load('safari/assets/tilt.png').convert_alpha()
button = pygame.image.load('safari/assets/pap.png').convert_alpha()
red_double = pygame.image.load('safari/assets/red_double.png').convert_alpha()
green_double = pygame.image.load('safari/assets/green_double.png').convert_alpha()
yellow_double = pygame.image.load('safari/assets/yellow_double.png').convert_alpha()
blue_double = pygame.image.load('safari/assets/blue_double.png').convert_alpha()
four_stars = pygame.image.load('safari/assets/four_stars.png').convert_alpha()
six_stars = pygame.image.load('safari/assets/six_stars.png').convert_alpha()
three_stars = pygame.image.load('safari/assets/three_stars.png').convert_alpha()
three_red = pygame.image.load('safari/assets/three_red.png').convert_alpha()
two_red = pygame.image.load('safari/assets/two_red.png').convert_alpha()
red_letter = pygame.image.load('safari/assets/red_letter.png').convert_alpha()
letter1 = pygame.image.load('safari/assets/letter1.png').convert_alpha()
letter2 = pygame.image.load('safari/assets/letter2.png').convert_alpha()
letter3 = pygame.image.load('safari/assets/letter3.png').convert_alpha()
letter4 = pygame.image.load('safari/assets/letter4.png').convert_alpha()
letter5 = pygame.image.load('safari/assets/letter5.png').convert_alpha()
letter6 = pygame.image.load('safari/assets/letter6.png').convert_alpha()
red_letter1 = pygame.image.load('safari/assets/red_letter1.png').convert_alpha()
red_letter2 = pygame.image.load('safari/assets/red_letter2.png').convert_alpha()
red_letter3 = pygame.image.load('safari/assets/red_letter3.png').convert_alpha()
red_letter4 = pygame.image.load('safari/assets/red_letter4.png').convert_alpha()
red_letter5 = pygame.image.load('safari/assets/red_letter5.png').convert_alpha()
red_letter6 = pygame.image.load('safari/assets/red_letter6.png').convert_alpha()
number_card = pygame.image.load('safari/assets/number_card.png').convert_alpha()
number = pygame.image.load('safari/assets/number.png').convert_alpha()
columnb1 = pygame.image.load('safari/assets/columnb1.png').convert_alpha()
columnb2 = pygame.image.load('safari/assets/columnb2.png').convert_alpha()
columna = pygame.image.load('safari/assets/columna.png').convert_alpha()
columnc1 = pygame.image.load('safari/assets/columnc1.png').convert_alpha()
columnc2 = pygame.image.load('safari/assets/columnc2.png').convert_alpha()
double_triple = pygame.image.load('safari/assets/double_triple.png').convert_alpha()
collected = pygame.image.load('safari/assets/collected.png').convert_alpha()
special_odds = pygame.image.load('safari/assets/special_odds.png').convert_alpha()
twin_number = pygame.image.load('safari/assets/twin_number.png').convert_alpha()
animal = pygame.image.load('safari/assets/animal.png').convert_alpha()
animal_arrow = pygame.image.load('safari/assets/animal_arrow.png').convert_alpha()
bg_menu = pygame.image.load('safari/assets/safari_menu.png').convert_alpha()
bg_gi = pygame.image.load('safari/assets/safari_gi.png').convert_alpha()
bg_off = pygame.image.load('safari/assets/safari_off.png').convert_alpha()

class scorereel():
    """ Score Reels are used to count replays """
    def __init__(self, pos, image):
        self.position = pos
        self.default_y = self.position[1]
        self.image = pygame.image.load(image).convert()

reel1 = scorereel([110,800], "graphics/assets/white_reel.png")
reel10 = scorereel([91,800], "graphics/assets/white_reel.png")
reel100 = scorereel([72,800], "graphics/assets/white_reel.png")
reel1000 = scorereel([53,800], "graphics/assets/white_reel.png")

def display(s, replays=0, menu=False):
    
    meter.set_colorkey((255,0,252))
    meter_position = [44,800]

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
        eb_position = [39,1044]
        screen.blit(extra_balls, eb_position)

    if s.game.extra_ball.position >= 1:
        eb_position = [146,1044]
        screen.blit(eb_number, eb_position)
    if s.game.extra_ball.position >= 2:
        eb_position = [198,1046]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 3:
        eb_position = [259,1046]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 4:
        eb_position = [321,1046]
        screen.blit(eb_number, eb_position)
    if s.game.extra_ball.position >= 5:
        eb_position = [372,1046]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 6:
        eb_position = [436,1046]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 7:
        eb_position = [498,1044]
        screen.blit(eb_number, eb_position)
    if s.game.extra_ball.position >= 8:
        eb_position = [548,1044]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 9:
        eb_position = [610,1044]
        screen.blit(eb, eb_position)

    if s.game.red_star.status == True:
        rs_position = [12,460]
        screen.blit(time, rs_position)
    if s.game.yellow_star.status == True:
        rs_position = [12,504]
        screen.blit(time, rs_position)

    if s.game.mystic_lines.position >= 4 or s.game.two_red_letter.status == True or s.game.three_red_letter.status == True:
        if s.game.selection_feature.position < 7:
            bfp = [12,549]
            screen.blit(time, bfp)
        elif s.game.selection_feature.position in [7,8]:
            bfp = [12,415]
            screen.blit(time, bfp)
        elif s.game.selection_feature.position == 9:
            bfp = [12,371]
            screen.blit(time, bfp)

    if s.game.ball_count.position < 1:
        if s.game.odds_only.status == True:
            b = [13,880]
            screen.blit(button, b)
        elif s.game.features.status == True:
            b = [14,918]
            screen.blit(button, b)
        elif s.game.special.status == True:
            b = [14,994]
            screen.blit(button, b)
        else:
            b = [14,956]
            screen.blit(button, b)


    if s.game.mystic_lines.position == 1:
        p = [198,686]
        screen.blit(ml_arrow, p)
    if s.game.mystic_lines.position == 2:
        p = [231,684]
        screen.blit(ml_arrow, p)
    if s.game.mystic_lines.position == 3:
        p = [263,684]
        screen.blit(ml_arrow, p)
    if s.game.mystic_lines.position >= 4:
        p = [299,686]
        screen.blit(ml_a, p)
        p = [334,591]
        screen.blit(ml_letter, p)
    if s.game.mystic_lines.position == 5:
        p = [330,683]
        screen.blit(ml_arrow, p)
    if s.game.mystic_lines.position == 6:
        p = [360,683]
        screen.blit(ml_arrow, p)
    if s.game.mystic_lines.position >= 7:
        p = [396,685]
        screen.blit(ml_b, p)
        p = [260,591]
        screen.blit(ml_letter, p)
    if s.game.mystic_lines.position == 8:
        p = [429,683]
        screen.blit(ml_arrow, p)
    if s.game.mystic_lines.position == 9:
        p = [458,683]
        screen.blit(ml_arrow, p)
    if s.game.mystic_lines.position == 10:
        p = [495,685]
        screen.blit(ml_c, p)
        p = [410,591]
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
        o = [192,788]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 2:
        o = [230,788]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 3:
        o = [267,788]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 4:
        o = [305,788]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 5:
        o = [343,788]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 6:
        o = [385,788]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 7:
        o = [436,788]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 8:
        o = [483,788]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 9:
        o = [530,788]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 10:
        o = [578,788]
        screen.blit(odds, o)

    if s.game.green_odds.position == 1:
        o = [192,850]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 2:
        o = [230,850]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 3:
        o = [267,850]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 4:
        o = [305,850]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 5:
        o = [343,850]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 6:
        o = [385,850]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 7:
        o = [436,850]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 8:
        o = [483,850]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 9:
        o = [530,850]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 10:
        o = [578,850]
        screen.blit(odds, o)

    if s.game.yellow_odds.position == 1:
        o = [192,914]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 2:
        o = [230,914]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 3:
        o = [267,914]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 4:
        o = [305,914]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 5:
        o = [343,914]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 6:
        o = [385,914]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 7:
        o = [436,914]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 8:
        o = [483,914]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 9:
        o = [530,914]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 10:
        o = [578,914]
        screen.blit(odds, o)
        
    if s.game.blue_odds.position == 1:
        o = [192,978]
        screen.blit(odds, o)
    elif s.game.blue_odds.position == 2:
        o = [230,978]
        screen.blit(odds, o)
    elif s.game.blue_odds.position == 3:
        o = [267,978]
        screen.blit(odds, o)
    elif s.game.blue_odds.position == 4:
        o = [305,978]
        screen.blit(odds, o)
    elif s.game.blue_odds.position == 5:
        o = [343,978]
        screen.blit(odds, o)
    elif s.game.blue_odds.position == 6:
        o = [385,978]
        screen.blit(odds, o)
    elif s.game.blue_odds.position == 7:
        o = [436,978]
        screen.blit(odds, o)
    elif s.game.blue_odds.position == 8:
        o = [483,978]
        screen.blit(odds, o)
    elif s.game.blue_odds.position == 9:
        o = [530,978]
        screen.blit(odds, o)
    elif s.game.blue_odds.position == 10:
        o = [578,978]
        screen.blit(odds, o)
   
    p = [301,213]
    screen.blit(letter1, p)
    p = [349,213]
    screen.blit(letter2, p)
    p = [415,213]
    screen.blit(letter3, p)
    p = [468,214]
    screen.blit(letter4, p)
    p = [529,215]
    screen.blit(letter5, p)
    p = [594,217]
    screen.blit(letter6, p)

    if s.game.red_odds.position < 5:
        p = [301,213]
        screen.blit(red_letter1, p)
    if s.game.red_odds.position in [5,6]:
        p = [349,213]
        screen.blit(red_letter2, p)
    if s.game.red_odds.position == 7:
        p = [415,213]
        screen.blit(red_letter3, p)
    if s.game.red_odds.position == 8:
        p = [468,214]
        screen.blit(red_letter4, p)
    if s.game.red_odds.position == 9:
        p = [529,215]
        screen.blit(red_letter5, p)
    if s.game.red_odds.position == 10:
        p = [594,217]
        screen.blit(red_letter6, p)

    if s.game.two_red_letter.status == True:
        p = [12,256]
        screen.blit(red_letter, p)
        p = [88,219]
        screen.blit(two_red, p)
    if s.game.three_red_letter.status == True:
        p = [12,256]
        screen.blit(red_letter, p)
        p = [13,219]
        screen.blit(three_red, p)

    if s.game.three_stars.status == True:
        p = [12,296]
        screen.blit(four_stars, p)
        p = [12,333]
        screen.blit(three_stars, p)
    if s.game.six_stars.status == True:
        p = [12,296]
        screen.blit(four_stars, p)
        p = [86,333]
        screen.blit(six_stars, p)

    if s.game.double_red.status == True:
        p = [12,612]
        screen.blit(red_double, p)
    if s.game.double_yellow.status == True:
        p = [88,612]
        screen.blit(yellow_double, p)
    if s.game.double_green.status == True:
        p = [12,686]
        screen.blit(green_double, p)
    if s.game.double_blue.status == True:
        p = [88,686]
        screen.blit(blue_double, p)

    if s.game.triple.status == False and (s.game.double_red.status == True or s.game.double_yellow.status == True or s.game.double_green.status == True or s.game.double_blue.status == True):
        p = [46,684]
        screen.blit(double_triple, p)

    if s.game.triple.status == True and (s.game.double_red.status == True or s.game.double_yellow.status == True or s.game.double_green.status == True or s.game.double_blue.status == True):
        p = [46,651]
        screen.blit(double_triple, p)

    if s.game.tilt.status == True:
        tilt_position = [555,740]
        screen.blit(tilt, tilt_position)

    # Special Game
    if s.game.special_odds.position > 0:
        #Add animal feature positioning
        if s.game.special_odds.position == 1:
            p = [541,596]
            screen.blit(special_odds, p)
        if s.game.special_odds.position == 2:
            p = [541,561]
            screen.blit(special_odds, p)
        if s.game.special_odds.position == 3:
            p = [541,525]
            screen.blit(special_odds, p)
        if s.game.special_odds.position == 4:
            p = [541,491]
            screen.blit(special_odds, p)
        if s.game.special_odds.position == 5:
            p = [541,456]
            screen.blit(special_odds, p)
        if s.game.special_odds.position == 6:
            p = [541,420]
            screen.blit(special_odds, p)
        if s.game.special_odds.position == 7:
            p = [541,385]
            screen.blit(special_odds, p)
        if s.game.special_odds.position == 8:
            p = [541,351]
            screen.blit(special_odds, p)
        if s.game.special_odds.position == 9:
            p = [541,316]
            screen.blit(special_odds, p)
    
        if s.game.animal_feature.position == 0:
            p = [649,991]
            screen.blit(animal, p)
        elif s.game.animal_feature.position == 1:
            p = [648,960]
            screen.blit(animal, p)
        elif s.game.animal_feature.position == 2:
            p = [652,927]
            screen.blit(animal_arrow, p)
        elif s.game.animal_feature.position == 3:
            p = [649,898]
            screen.blit(animal, p)
        elif s.game.animal_feature.position == 4:
            p = [653,866]
            screen.blit(animal_arrow, p)
        elif s.game.animal_feature.position == 5:
            p = [653,835]
            screen.blit(animal_arrow, p)
        elif s.game.animal_feature.position == 6:
            p = [650,805]
            screen.blit(animal, p)
        elif s.game.animal_feature.position == 7:
            p = [651,774]
            screen.blit(animal, p)
        elif s.game.animal_feature.position == 8:
            p = [655,741]
            screen.blit(animal_arrow, p)
        elif s.game.animal_feature.position == 9:
            p = [655,711]
            screen.blit(animal_arrow, p)
        elif s.game.animal_feature.position == 10:
            p = [655,679]
            screen.blit(animal_arrow, p)
        elif s.game.animal_feature.position == 11:
            p = [656,647]
            screen.blit(animal_arrow, p)
        elif s.game.animal_feature.position == 12:
            p = [656,616]
            screen.blit(animal_arrow, p)
        elif s.game.animal_feature.position == 13:
            p = [656,584]
            screen.blit(animal_arrow, p)
        elif s.game.animal_feature.position == 14:
            p = [656,553]
            screen.blit(animal_arrow, p)
        elif s.game.animal_feature.position == 15:
            p = [652,523]
            screen.blit(animal, p)
        elif s.game.animal_feature.position == 16:
            p = [656,491]
            screen.blit(animal_arrow, p)
        elif s.game.animal_feature.position == 17:
            p = [656,459]
            screen.blit(animal_arrow, p)
        elif s.game.animal_feature.position == 18:
            p = [652,429]
            screen.blit(animal, p)
        elif s.game.animal_feature.position == 19:
            p = [655,397]
            screen.blit(animal_arrow, p)
        elif s.game.animal_feature.position == 20:
            p = [655,366]
            screen.blit(animal_arrow, p)
        elif s.game.animal_feature.position == 21:
            p = [651,336]
            screen.blit(animal, p)
        elif s.game.animal_feature.position == 22:
            p = [655,305]
            screen.blit(animal_arrow, p)
        elif s.game.animal_feature.position == 23:
            p = [651,275]
            screen.blit(animal, p)
        elif s.game.animal_feature.position == 24:
            p = [651,244]
            screen.blit(animal, p)

    if s.game.special_replay_counter.position > 0:
        p = [541,667]
        screen.blit(collected, p)

    if s.game.twin_number.position == 1:
        p = [200,745]
        screen.blit(ml_arrow, p)
    elif s.game.twin_number.position == 2:
        p = [232,745]
        screen.blit(ml_arrow, p)
    elif s.game.twin_number.position == 3:
        p = [265,745]
        screen.blit(ml_arrow, p)
    if s.game.twin_number.position >= 4:
        if s.game.eleven.status == True:
            p = [299,758]
            screen.blit(twin_number, p)
        if s.game.seventeen.status == True:
            p = [299,735]
            screen.blit(twin_number, p)
    if s.game.twin_number.position == 5:
        p = [366,745]
        screen.blit(ml_arrow, p)
    elif s.game.twin_number.position == 6:
        p = [398,745]
        screen.blit(ml_arrow, p)
    elif s.game.twin_number.position == 7:
        p = [430,745]
        screen.blit(ml_arrow, p)
    if s.game.twin_number.position == 8:
        if s.game.eleven.status == True:
            p = [463,735]
            screen.blit(twin_number, p)
        if s.game.seventeen.status == True:
            p = [463,758]
            screen.blit(twin_number, p)

    pygame.display.update()

def eb_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]

    if s.game.extra_ball.position < 1:
        dirty_rects.append(screen.blit(bg_gi, (146,1044), pygame.Rect(146,1044,47,31)))
    if s.game.extra_ball.position < 2:
        dirty_rects.append(screen.blit(bg_gi, (198,1046), pygame.Rect(198,1046,59,34)))
    if s.game.extra_ball.position < 3:
        dirty_rects.append(screen.blit(bg_gi, (259,1046), pygame.Rect(259,1046,59,34)))
    if s.game.extra_ball.position < 4:
        dirty_rects.append(screen.blit(bg_gi, (321,1046), pygame.Rect(321,1046,47,31)))
    if s.game.extra_ball.position < 5:
        dirty_rects.append(screen.blit(bg_gi, (372,1046), pygame.Rect(372,1046,59,34)))
    if s.game.extra_ball.position < 6:
        dirty_rects.append(screen.blit(bg_gi, (436,1046), pygame.Rect(436,1046,59,34)))
    if s.game.extra_ball.position < 7:
        dirty_rects.append(screen.blit(bg_gi, (498,1044), pygame.Rect(498,1044,47,31)))
    if s.game.extra_ball.position < 8:
        dirty_rects.append(screen.blit(bg_gi, (548,1044), pygame.Rect(548,1044,59,34)))
    if s.game.extra_ball.position < 9:
        dirty_rects.append(screen.blit(bg_gi, (610,1044), pygame.Rect(610,1044,59,34)))
    pygame.display.update(dirty_rects)

    if num in [0,25,14,49]:
        if s.game.extra_ball.position < 1:
            p = [146,1044]
            dirty_rects.append(screen.blit(eb_number, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [39,1,26,15]:
        if s.game.extra_ball.position < 2:
            p = [198,1046]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [3,4,17,28,29,40]:
        if s.game.extra_ball.position < 3:
            p = [259,1046]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [5,18,30,43]:
        if s.game.extra_ball.position < 4:
            p = [321,1046]
            dirty_rects.append(screen.blit(eb_number, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [7,8,19,32,33,44]:
        if s.game.extra_ball.position < 5:
            p = [372,1046]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [9,10,20,34,35,45]:
        if s.game.extra_ball.position < 6:
            p = [436,1046]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [11,21,36,46]:
        if s.game.extra_ball.position < 7:
            p = [498,1044]
            dirty_rects.append(screen.blit(eb_number, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [12,22,37,47]:
        if s.game.extra_ball.position < 8:
            p = [548,1044]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [2,6,13,16,23,27,31,38,41,48]:
        if s.game.extra_ball.position < 9:
            p = [610,1044]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return

def clear_odds(s, num):
    global screen

    dirty_rects = []
    
    if s.game.double_red.status == False:
        dirty_rects.append(screen.blit(bg_gi, (12,612), pygame.Rect(12,612,74,74)))
    if s.game.double_yellow.status == False:
        dirty_rects.append(screen.blit(bg_gi, (88,612), pygame.Rect(88,612,74,74)))
    if s.game.double_green.status == False:
        dirty_rects.append(screen.blit(bg_gi, (12,686), pygame.Rect(12,686,74,74)))
    if s.game.double_blue.status == False:
        dirty_rects.append(screen.blit(bg_gi, (88,686), pygame.Rect(88,686,74,74)))

    if s.game.yellow_odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (230,914), pygame.Rect(230,914,46,61)))
    if s.game.yellow_odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (343,914), pygame.Rect(343,914,46,61)))
    if s.game.yellow_odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (385,914), pygame.Rect(385,914,46,61)))
    if s.game.yellow_odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (436,914), pygame.Rect(436,914,46,61)))
    if s.game.yellow_odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (483,914), pygame.Rect(483,914,46,61)))
    if s.game.yellow_odds.position != 9:
        dirty_rects.append(screen.blit(bg_gi, (530,914), pygame.Rect(530,914,46,61)))
    if s.game.yellow_odds.position != 10:
        dirty_rects.append(screen.blit(bg_gi, (578,914), pygame.Rect(578,914,46,61)))

    if s.game.red_odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (267,788), pygame.Rect(267,788,46,61)))
    if s.game.red_odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (305,788), pygame.Rect(305,788,46,61)))
    if s.game.red_odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (385,788), pygame.Rect(385,788,46,61)))
    if s.game.red_odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (436,788), pygame.Rect(436,788,46,61)))
    if s.game.red_odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (483,788), pygame.Rect(483,788,46,61)))
    if s.game.red_odds.position != 9:
        dirty_rects.append(screen.blit(bg_gi, (530,788), pygame.Rect(530,788,46,61)))
    if s.game.red_odds.position != 10:
        dirty_rects.append(screen.blit(bg_gi, (578,788), pygame.Rect(578,788,46,61)))


    if s.game.blue_odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (230,978), pygame.Rect(230,978,46,61)))
        dirty_rects.append(screen.blit(bg_gi, (230,850), pygame.Rect(230,850,46,61)))
    if s.game.blue_odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (343,978), pygame.Rect(343,978,46,61)))
        dirty_rects.append(screen.blit(bg_gi, (343,850), pygame.Rect(343,850,46,61)))
    if s.game.blue_odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (436,978), pygame.Rect(436,978,46,61)))
        dirty_rects.append(screen.blit(bg_gi, (436,850), pygame.Rect(436,850,46,61)))
    if s.game.blue_odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (483,978), pygame.Rect(483,978,46,61)))
        dirty_rects.append(screen.blit(bg_gi, (483,850), pygame.Rect(483,850,46,61)))
    if s.game.blue_odds.position != 9:
        dirty_rects.append(screen.blit(bg_gi, (530,978), pygame.Rect(530,978,46,61)))
        dirty_rects.append(screen.blit(bg_gi, (530,850), pygame.Rect(530,850,46,61)))
    if s.game.blue_odds.position != 10:
        dirty_rects.append(screen.blit(bg_gi, (578,978), pygame.Rect(578,978,46,61)))
        dirty_rects.append(screen.blit(bg_gi, (578,850), pygame.Rect(578,850,46,61)))

    pygame.display.update(dirty_rects)

def draw_odds_animation(s, num):
    global screen
    dirty_rects = []

    if num in [7,32]:
        if s.game.double_red.status == False:
            p = [12,612]
            dirty_rects.append(screen.blit(red_double, p))
            pygame.display.update(dirty_rects)
            return
    if num in [15,40]:
        if s.game.double_yellow.status == False:
            p = [88,612]
            dirty_rects.append(screen.blit(yellow_double, p))
            pygame.display.update(dirty_rects)
            return
    if num in [0,25]:
        if s.game.double_green.status == False:
            p = [12,686]
            dirty_rects.append(screen.blit(green_double, p))
            pygame.display.update(dirty_rects)
            return
    if num in [9,34]:
        if s.game.double_blue.status == False:
            p = [88,686]
            dirty_rects.append(screen.blit(blue_double, p))
            pygame.display.update(dirty_rects)
            return

    if num in [4,29]:
        if s.game.yellow_odds.position != 2:
            p = [230,914]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [13,38]:
        if s.game.yellow_odds.position != 5:
            p = [343,914]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [9,34]:
        if s.game.yellow_odds.position != 6:
            p = [385,914]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [22,2]:
        if s.game.yellow_odds.position != 7:
            p = [436,914]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [15,40]:
        if s.game.yellow_odds.position != 8:
            p = [483,914]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [19,44]:
        if s.game.yellow_odds.position != 9:
            p = [530,914]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [5,30]:
        if s.game.yellow_odds.position != 10:
            p = [578,914]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return

    if num in [24,49]:
        if s.game.red_odds.position != 3:
            p = [267,788]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [16,41]:
        if s.game.red_odds.position != 4:
            p = [305,788]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [14,39]:
        if s.game.red_odds.position != 6:
            p = [385,788]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [20,45]:
        if s.game.red_odds.position != 7:
            p = [436,788]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [12,37]:
        if s.game.red_odds.position != 8:
            p = [483,788]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [25,0]:
        if s.game.red_odds.position != 9:
            p = [530,788]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [6,31]:
        if s.game.red_odds.position != 10:
            p = [578,788]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return

    if num in [18,43]:
        if s.game.blue_odds.position != 2:
            p = [230,978]
            dirty_rects.append(screen.blit(odds, p))
            p = [230,850]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [3,28]:
        if s.game.blue_odds.position != 5:
            p = [343,978]
            dirty_rects.append(screen.blit(odds, p))
            p = [343,850]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [23,48]:
        if s.game.blue_odds.position != 7:
            p = [436,978]
            dirty_rects.append(screen.blit(odds, p))
            p = [436,850]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
    if num in [8,33]:
        if s.game.blue_odds.position != 8:
            p = [483,978]
            dirty_rects.append(screen.blit(odds, p))
            p = [483,850]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [21,46]:
        if s.game.blue_odds.position != 9:
            p = [530,978]
            dirty_rects.append(screen.blit(odds, p))
            p = [530,850]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [10,35]:
        if s.game.blue_odds.position != 10:
            p = [578,978]
            dirty_rects.append(screen.blit(odds, p))
            p = [578,850]
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

    if s.game.selection_feature.position > 7:
        dirty_rects.append(screen.blit(bg_gi, (12,549), pygame.Rect(12,549,148,48)))
    if s.game.mystic_lines.position < 4 and s.game.two_red_letter.status == False and s.game.three_red_letter.status == False:
        dirty_rects.append(screen.blit(bg_gi, (12,549), pygame.Rect(12,549,148,48)))

    if s.game.selection_feature.position not in [7,8]:
        dirty_rects.append(screen.blit(bg_gi, (12,415), pygame.Rect(12,415,148,48)))
    if s.game.mystic_lines.position < 4 and s.game.two_red_letter.status == False and s.game.three_red_letter.status == False:
        dirty_rects.append(screen.blit(bg_gi, (12,415), pygame.Rect(12,415,148,48)))
    
    if s.game.selection_feature.position < 9:
        dirty_rects.append(screen.blit(bg_gi, (12,371), pygame.Rect(12,371,148,48)))
    if s.game.mystic_lines.position < 4 and s.game.two_red_letter.status == False and s.game.three_red_letter.status == False:
        dirty_rects.append(screen.blit(bg_gi, (12,371), pygame.Rect(12,371,148,48)))

    if s.game.yellow_star.status == False:
        dirty_rects.append(screen.blit(bg_gi, (12,504), pygame.Rect(12,504,148,48)))
    if s.game.red_star.status == False:
        dirty_rects.append(screen.blit(bg_gi, (12,460), pygame.Rect(12,460,148,48)))

    if s.game.three_red_letter.status == False:
        dirty_rects.append(screen.blit(bg_gi, (13,219), pygame.Rect(13,219,76,41)))
    if s.game.two_red_letter.status == False:
        dirty_rects.append(screen.blit(bg_gi, (88,219), pygame.Rect(88,219,76,41)))

    if s.game.three_stars.status == False:
        dirty_rects.append(screen.blit(bg_gi, (12,333), pygame.Rect(12,333,77,27)))
    if s.game.six_stars.status == False:
        dirty_rects.append(screen.blit(bg_gi, (86,333), pygame.Rect(86,333,77,27)))

    if s.game.mystic_lines.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (231,684), pygame.Rect(231,684,29,29)))
    if s.game.mystic_lines.position < 4:
        dirty_rects.append(screen.blit(bg_gi, (334,591), pygame.Rect(334,591,49,48)))
    if s.game.mystic_lines.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (330,683), pygame.Rect(330,683,29,29)))
    if s.game.mystic_lines.position < 7:
        dirty_rects.append(screen.blit(bg_gi, (260,591), pygame.Rect(260,591,49,48)))
    if s.game.mystic_lines.position != 9:
        dirty_rects.append(screen.blit(bg_gi, (458,683), pygame.Rect(458,683,29,29)))
    if s.game.mystic_lines.position < 10:
        dirty_rects.append(screen.blit(bg_gi, (410,591), pygame.Rect(410,591,49,48)))

    pygame.display.update(dirty_rects)


def draw_feature_animation(s, num):
    global screen
    dirty_rects = []
     
    if num in [10,35]:
        if s.game.selection_feature.position not in [1,2,3,4,5,6] and (s.game.mystic_lines.position < 4 and s.game.two_red_letter.status == False and s.game.three_red_letter.status == False):
            p = [12,549]
            dirty_rects.append(screen.blit(time, p))
            pygame.display.update(dirty_rects)
            return
    if num in [9,34]:
        if s.game.selection_feature.position not in [7,8] and (s.game.mystic_lines.position < 4 and s.game.two_red_letter.status == False and s.game.three_red_letter.status == False):
            p = [12,415]
            dirty_rects.append(screen.blit(time, p))
            pygame.display.update(dirty_rects)
            return
    if num in [6,31]:
        if s.game.selection_feature.position not in [9] and (s.game.mystic_lines.position < 4 and s.game.two_red_letter.status == False and s.game.three_red_letter.status == False):
            p = [12,371]
            dirty_rects.append(screen.blit(time, p))
            pygame.display.update(dirty_rects)
            return

    if num in [4,29]:
        if s.game.red_star.status == False:
            p = [12,460]
            dirty_rects.append(screen.blit(time, p))
            pygame.display.update(dirty_rects)
            s.game.coils.redROLamp.pulse(85)
            return
    if num in [11,36]:
        if s.game.yellow_star.status == False:
            p = [12,504]
            dirty_rects.append(screen.blit(time, p))
            pygame.display.update(dirty_rects)
            s.game.coils.yellowROLamp.pulse(85)
            return

    if num in [16,24,41,49]:
        if s.game.three_red_letter.status == False:
            p = [13,219]
            dirty_rects.append(screen.blit(three_red, p))
            pygame.display.update(dirty_rects)
            return
    if num in [7,32]:
        if s.game.two_red_letter.status == False:
            p = [88,219]
            dirty_rects.append(screen.blit(two_red, p))
            pygame.display.update(dirty_rects)
            return
    if num in [8,33]:
        if s.game.three_stars.status == False:
            p = [12,333]
            dirty_rects.append(screen.blit(three_stars, p))
            pygame.display.update(dirty_rects)
            return
    if num in [20,45]:
        if s.game.six_stars.status == False:
            p = [86,333]
            dirty_rects.append(screen.blit(six_stars, p))
            pygame.display.update(dirty_rects)
            return

    if num in [8,33]:
        if s.game.mystic_lines.position != 2:
            p = [231,684]
            dirty_rects.append(screen.blit(ml_arrow, p))
            pygame.display.update(dirty_rects)
            return
    if num in [3,22,28,47]:
        if s.game.mystic_lines.position < 4:
            p = [334,591]
            dirty_rects.append(screen.blit(ml_letter, p))
            pygame.display.update(dirty_rects)
            return
    if num in [2,12,27,37]:
        if s.game.mystic_lines.position != 5:
            p = [330,683]
            dirty_rects.append(screen.blit(ml_arrow, p))
            pygame.display.update(dirty_rects)
            return
    if num in [4,29]:
        if s.game.mystic_lines.position < 7:
            p = [260,591]
            dirty_rects.append(screen.blit(ml_letter, p))
            pygame.display.update(dirty_rects)
            return
    if num in [15,40]:
        if s.game.mystic_lines.position != 9:
            p = [458,683]
            dirty_rects.append(screen.blit(ml_arrow, p))
            pygame.display.update(dirty_rects)
            return
    if num in [1,14,26,39]:
        if s.game.mystic_lines.position < 10:
            p = [410,591]
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

def special_animation(args):
    global screen
    dirty_rects = []
    s = args[0]
    num = args[1]

    if s.game.special_odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (541,561), pygame.Rect(541,561,103,34)))
    if s.game.special_odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (541,525), pygame.Rect(541,525,103,34)))
    if s.game.special_odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (541,491), pygame.Rect(541,491,103,34)))
    if s.game.special_odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (541,456), pygame.Rect(541,456,103,34)))
    if s.game.special_odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (541,420), pygame.Rect(541,420,103,34)))
    if s.game.special_odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (541,385), pygame.Rect(541,385,103,34)))
    if s.game.special_odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (541,351), pygame.Rect(541,351,103,34)))
    if s.game.special_odds.position != 9:
        dirty_rects.append(screen.blit(bg_gi, (541,316), pygame.Rect(541,316,103,34)))

    pygame.display.update(dirty_rects)

    if num in [5,6,30,31]:
        if s.game.special_odds.position < 2:
            p = [541,561]
            dirty_rects.append(screen.blit(special_odds, p))
            pygame.display.update(dirty_rects) 
            return
    if num in [4,5,29,30]:
        if s.game.special_odds.position < 3:
            p = [541,525]
            dirty_rects.append(screen.blit(special_odds, p))
            pygame.display.update(dirty_rects) 
            return
    if num in [10,11,35,36]:
        if s.game.special_odds.position < 4:
            p = [541,491]
            dirty_rects.append(screen.blit(special_odds, p))
            pygame.display.update(dirty_rects) 
            return
    if num in [8,9,33,34]:
        if s.game.special_odds.position < 5:
            p = [541,456]
            dirty_rects.append(screen.blit(special_odds, p))
            pygame.display.update(dirty_rects) 
            return
    if num in [14,15,18,19,39,40,43,44]:
        if s.game.special_odds.position < 6:
            p = [541,420]
            dirty_rects.append(screen.blit(special_odds, p))
            pygame.display.update(dirty_rects) 
            return
    if num in [12,13,20,21,37,38,45,46]:
        if s.game.special_odds.position < 7:
            p = [541,385]
            dirty_rects.append(screen.blit(special_odds, p))
            pygame.display.update(dirty_rects) 
            return
    if num in [16,17,22,23,24,25,41,42,47,48,49,0]:
        if s.game.special_odds.position < 8:
            p = [541,351]
            dirty_rects.append(screen.blit(special_odds, p))
            pygame.display.update(dirty_rects) 
            return
    if num in [2,3,27,28]:
        if s.game.special_odds.position < 9:
            p = [541,316]
            dirty_rects.append(screen.blit(special_odds, p))
            pygame.display.update(dirty_rects) 
            return

def blink(args):
    dirty_rects = []
    s = args[0]
    b = args[1]
    sn = args[2]

    if b == 0:
        if sn == 1:
            p = [286,643]
            dirty_rects.append(screen.blit(select_now, p))
        pygame.display.update(dirty_rects)
    else:
        dirty_rects.append(screen.blit(bg_gi, (286,643), pygame.Rect(286,643,146,30)))
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
            
        dirty_rects.append(screen.blit(bg_gi, (282,213), pygame.Rect(282,213,362,82)))

        p = [301,213]
        dirty_rects.append(screen.blit(letter1, p))
        p = [349,213]
        dirty_rects.append(screen.blit(letter2, p))
        p = [415,213]
        dirty_rects.append(screen.blit(letter3, p))
        p = [468,214]
        dirty_rects.append(screen.blit(letter4, p))
        p = [529,215]
        dirty_rects.append(screen.blit(letter5, p))
        p = [594,217]
        dirty_rects.append(screen.blit(letter6, p))

        if s.game.red_odds.position < 5:
            p = [301,213]
            dirty_rects.append(screen.blit(red_letter1, p))
        if s.game.red_odds.position in [5,6]:
            p = [349,213]
            dirty_rects.append(screen.blit(red_letter2, p))
        if s.game.red_odds.position == 7:
            p = [415,213]
            dirty_rects.append(screen.blit(red_letter3, p))
        if s.game.red_odds.position == 8:
            p = [468,214]
            dirty_rects.append(screen.blit(red_letter4, p))
        if s.game.red_odds.position == 9:
            p = [529,215]
            dirty_rects.append(screen.blit(red_letter5, p))
        if s.game.red_odds.position == 10:
            p = [594,217]
            dirty_rects.append(screen.blit(red_letter6, p))

        if s.game.mystic_lines.position == 1:
            p = [198,686]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],25,29)))
            dirty_rects.append(screen.blit(ml_arrow, p))
        if s.game.mystic_lines.position == 2:
            p = [231,684]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],25,29)))
            dirty_rects.append(screen.blit(ml_arrow, p))
        if s.game.mystic_lines.position == 3:
            p = [263,684]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],25,29)))
            dirty_rects.append(screen.blit(ml_arrow, p))
        if s.game.mystic_lines.position >= 4:
            p = [299,686]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],22,25)))
            dirty_rects.append(screen.blit(ml_a, p))
            p = [334,591]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],49,48)))
            dirty_rects.append(screen.blit(ml_letter, p))
        if s.game.mystic_lines.position == 5:
            p = [330,683]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],25,29)))
            dirty_rects.append(screen.blit(ml_arrow, p))
        if s.game.mystic_lines.position == 6:
            p = [360,683]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],25,29)))
            dirty_rects.append(screen.blit(ml_arrow, p))
        if s.game.mystic_lines.position >= 7:
            p = [396,685]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],24,27)))
            dirty_rects.append(screen.blit(ml_b, p))
            p = [260,591]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],49,48)))
            dirty_rects.append(screen.blit(ml_letter, p))
        if s.game.mystic_lines.position == 8:
            p = [429,683]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],25,29)))
            dirty_rects.append(screen.blit(ml_arrow, p))
        if s.game.mystic_lines.position == 9:
            p = [458,683]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],25,29)))
            dirty_rects.append(screen.blit(ml_arrow, p))
        if s.game.mystic_lines.position == 10:
            p = [495,685]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],22,27)))
            dirty_rects.append(screen.blit(ml_c, p))
            p = [410,591]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],49,48)))
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
            dirty_rects.append(screen.blit(bg_gi, (233,369), pygame.Rect(233,369,270,212)))
        else:
            dirty_rects.append(screen.blit(bg_off, (233,369), pygame.Rect(233,369,270,212)))

        if s.game.mystic_lines.position == 1:
            p = [198,686]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],25,29)))
            dirty_rects.append(screen.blit(ml_arrow, p))
        if s.game.mystic_lines.position == 2:
            p = [231,684]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],25,29)))
            dirty_rects.append(screen.blit(ml_arrow, p))
        if s.game.mystic_lines.position == 3:
            p = [263,684]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],25,29)))
            dirty_rects.append(screen.blit(ml_arrow, p))
        if s.game.mystic_lines.position >= 4:
            p = [299,686]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],22,25)))
            dirty_rects.append(screen.blit(ml_a, p))
            p = [334,591]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],49,48)))
            dirty_rects.append(screen.blit(ml_letter, p))
        if s.game.mystic_lines.position == 5:
            p = [330,683]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],25,29)))
            dirty_rects.append(screen.blit(ml_arrow, p))
        if s.game.mystic_lines.position == 6:
            p = [360,683]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],25,29)))
            dirty_rects.append(screen.blit(ml_arrow, p))
        if s.game.mystic_lines.position >= 7:
            p = [396,685]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],24,27)))
            dirty_rects.append(screen.blit(ml_b, p))
            p = [260,591]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],49,48)))
            dirty_rects.append(screen.blit(ml_letter, p))
        if s.game.mystic_lines.position == 8:
            p = [429,683]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],25,29)))
            dirty_rects.append(screen.blit(ml_arrow, p))
        if s.game.mystic_lines.position == 9:
            p = [458,683]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],25,29)))
            dirty_rects.append(screen.blit(ml_arrow, p))
        if s.game.mystic_lines.position == 10:
            p = [495,685]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],22,27)))
            dirty_rects.append(screen.blit(ml_c, p))
            p = [410,591]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],49,48)))
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
            p = [198,686]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],25,29)))
            dirty_rects.append(screen.blit(ml_arrow, p))
        if s.game.mystic_lines.position == 2:
            p = [231,684]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],25,29)))
            dirty_rects.append(screen.blit(ml_arrow, p))
        if s.game.mystic_lines.position == 3:
            p = [263,684]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],25,29)))
            dirty_rects.append(screen.blit(ml_arrow, p))
        if s.game.mystic_lines.position >= 4:
            p = [299,686]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],22,25)))
            dirty_rects.append(screen.blit(ml_a, p))
            p = [334,591]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],49,48)))
            dirty_rects.append(screen.blit(ml_letter, p))
        if s.game.mystic_lines.position == 5:
            p = [330,683]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],25,29)))
            dirty_rects.append(screen.blit(ml_arrow, p))
        if s.game.mystic_lines.position == 6:
            p = [360,683]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],25,29)))
            dirty_rects.append(screen.blit(ml_arrow, p))
        if s.game.mystic_lines.position >= 7:
            p = [396,685]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],24,27)))
            dirty_rects.append(screen.blit(ml_b, p))
            p = [260,591]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],49,48)))
            dirty_rects.append(screen.blit(ml_letter, p))
        if s.game.mystic_lines.position == 8:
            p = [429,683]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],25,29)))
            dirty_rects.append(screen.blit(ml_arrow, p))
        if s.game.mystic_lines.position == 9:
            p = [458,683]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],25,29)))
            dirty_rects.append(screen.blit(ml_arrow, p))
        if s.game.mystic_lines.position == 10:
            p = [495,685]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],22,27)))
            dirty_rects.append(screen.blit(ml_c, p))
            p = [410,591]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],49,48)))
            dirty_rects.append(screen.blit(ml_letter, p))

    pygame.display.update(dirty_rects)


