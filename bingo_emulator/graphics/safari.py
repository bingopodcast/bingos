
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
        backglass = pygame.image.load('safari/assets/safari_menu.png').convert_alpha()
    else:
        if (s.game.anti_cheat.status == True):
            backglass = pygame.image.load('safari/assets/safari_gi.png').convert_alpha()
        else:
            backglass = pygame.image.load('safari/assets/safari_off.png').convert_alpha()
    backglass = pygame.transform.scale(backglass, (720, 1280))
    
    screen.blit(backglass, backglass_position)


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
        t = 4
        if s.game.selection_feature.position in [7,8]:
            t = 5
        if s.game.selection_feature.position == 9:
            t = 6
        if s.game.ball_count.position == t:
            p = [286,643]
            screen.blit(select_now, p)

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
                    p = [337,370]
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

    if s.game.red_odds.position < 4:
        p = [301,213]
        screen.blit(red_letter1, p)
    if s.game.red_odds.position == 4:
        p = [349,213]
        screen.blit(red_letter2, p)
    if s.game.red_odds.position == 5:
        p = [415,213]
        screen.blit(red_letter3, p)
    if s.game.red_odds.position == 6:
        p = [468,214]
        screen.blit(red_letter4, p)
    if s.game.red_odds.position == 7:
        p = [529,215]
        screen.blit(red_letter5, p)
    if s.game.red_odds.position == 8:
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
        tilt_position = [215,196]
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

def eb_animation(num):
    global screen

    if num == 3:
        eb_position = [498,1044]
        screen.blit(eb_number, eb_position)
        pygame.display.update()
    if num == 2:
        eb_position = [548,1044]
        screen.blit(eb, eb_position)
        pygame.display.update()
    if num == 1:
        eb_position = [610,1044]
        screen.blit(eb, eb_position)
        pygame.display.update()

def feature_animation(num):
    global screen

    if num == 4:
        p = [458,683]
        screen.blit(ml_arrow, p)
        pygame.display.update()
    else:
        p = [495,685]
        screen.blit(ml_c, p)
        p = [410,591]
        screen.blit(ml_letter, p)
        pygame.display.update()


def odds_animation(num):
    global screen

    if num == 8:
        o = [192,850]
        screen.blit(odds, o)
    if num == 7:
        o = [230,850]
        screen.blit(odds, o)
    if num == 6:
        o = [267,850]
        screen.blit(odds, o)
    if num == 5:
        o = [305,850]
        screen.blit(odds, o)
    if num == 4:
        o = [343,850]
        screen.blit(odds, o)
    if num == 3:
        o = [385,850]
        screen.blit(odds, o)
    if num == 2:
        o = [436,850]
        screen.blit(odds, o)
    if num == 1:
        o = [483,850]
        screen.blit(odds, o)
    pygame.display.update()


