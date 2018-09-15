
import pygame
import random

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

meter = pygame.image.load('graphics/assets/black_register_cover.png').convert()
odds = pygame.image.load('super_7/assets/odds.png').convert_alpha()
eb = pygame.image.load('super_7/assets/eb.png').convert_alpha()
eb_number = pygame.image.load('super_7/assets/eb_number.png').convert_alpha()
extra_balls = pygame.image.load('super_7/assets/extra_balls.png').convert_alpha()
time = pygame.image.load('super_7/assets/time.png').convert_alpha()
ml_letter = pygame.image.load('super_7/assets/ml_letter.png').convert_alpha()
ml_arrow = pygame.image.load('super_7/assets/ml_arrow.png').convert_alpha()
ml_a = pygame.image.load('super_7/assets/ml_a.png').convert_alpha()
ml_b = pygame.image.load('super_7/assets/ml_b.png').convert_alpha()
ml_c = pygame.image.load('super_7/assets/ml_c.png').convert_alpha()
select_now = pygame.image.load('super_7/assets/select_now.png').convert_alpha()
tilt = pygame.image.load('super_7/assets/tilt.png').convert_alpha()
button = pygame.image.load('super_7/assets/pap.png').convert_alpha()
red_double = pygame.image.load('super_7/assets/red_double.png').convert_alpha()
green_double = pygame.image.load('super_7/assets/green_double.png').convert_alpha()
yellow_double = pygame.image.load('super_7/assets/yellow_double.png').convert_alpha()
blue_double = pygame.image.load('super_7/assets/blue_double.png').convert_alpha()
four_stars = pygame.image.load('super_7/assets/four_stars.png').convert_alpha()
six_stars = pygame.image.load('super_7/assets/six_stars.png').convert_alpha()
three_stars = pygame.image.load('super_7/assets/three_stars.png').convert_alpha()
three_red = pygame.image.load('super_7/assets/three_red.png').convert_alpha()
two_red = pygame.image.load('super_7/assets/two_red.png').convert_alpha()
red_letter = pygame.image.load('super_7/assets/red_letter.png').convert_alpha()
letter1 = pygame.image.load('super_7/assets/letter1.png').convert_alpha()
letter2 = pygame.image.load('super_7/assets/letter2.png').convert_alpha()
letter3 = pygame.image.load('super_7/assets/letter3.png').convert_alpha()
letter4 = pygame.image.load('super_7/assets/letter4.png').convert_alpha()
letter5 = pygame.image.load('super_7/assets/letter5.png').convert_alpha()
letter6 = pygame.image.load('super_7/assets/letter6.png').convert_alpha()
red_letter1 = pygame.image.load('super_7/assets/red_letter1.png').convert_alpha()
red_letter2 = pygame.image.load('super_7/assets/red_letter2.png').convert_alpha()
red_letter3 = pygame.image.load('super_7/assets/red_letter3.png').convert_alpha()
red_letter4 = pygame.image.load('super_7/assets/red_letter4.png').convert_alpha()
red_letter5 = pygame.image.load('super_7/assets/red_letter5.png').convert_alpha()
red_letter6 = pygame.image.load('super_7/assets/red_letter6.png').convert_alpha()
number_card = pygame.image.load('super_7/assets/number_card.png').convert_alpha()
number = pygame.image.load('super_7/assets/number.png').convert_alpha()
columnb1 = pygame.image.load('super_7/assets/columnb1.png').convert_alpha()
columnb2 = pygame.image.load('super_7/assets/columnb2.png').convert_alpha()
columna = pygame.image.load('super_7/assets/columna.png').convert_alpha()
columnc1 = pygame.image.load('super_7/assets/columnc1.png').convert_alpha()
columnc2 = pygame.image.load('super_7/assets/columnc2.png').convert_alpha()
double_triple = pygame.image.load('super_7/assets/double_triple.png').convert_alpha()
collected = pygame.image.load('super_7/assets/collected.png').convert_alpha()
special_odds = pygame.image.load('super_7/assets/special_odds.png').convert_alpha()
twin_number = pygame.image.load('super_7/assets/twin_number.png').convert_alpha()
seven_odds = pygame.image.load('super_7/assets/seven_odds.png').convert_alpha()
diamond = pygame.image.load('super_7/assets/diamond.png').convert_alpha()
diamond_7 = pygame.image.load('super_7/assets/diamond_7.png').convert_alpha()
ball = pygame.image.load('super_7/assets/ball.png').convert_alpha()
bg_menu = pygame.image.load('super_7/assets/super_7_menu.png').convert_alpha()
bg_gi = pygame.image.load('super_7/assets/super_7_gi.png').convert_alpha()
bg_off = pygame.image.load('super_7/assets/super_7_off.png').convert_alpha()

class scorereel():
    """ Score Reels are used to count replays """
    def __init__(self, pos, image):
        self.position = pos
        self.default_y = self.position[1]
        self.image = pygame.image.load(image).convert()

reel1 = scorereel([110,797], "graphics/assets/white_reel.png")
reel10 = scorereel([91,797], "graphics/assets/white_reel.png")
reel100 = scorereel([72,797], "graphics/assets/white_reel.png")
reel1000 = scorereel([53,797], "graphics/assets/white_reel.png")

def display(s, replays=0, menu=False):
    
    meter.set_colorkey((255,0,252))
    meter_position = [44,797]

    screen.blit(reel1.image, reel1.position)
    screen.blit(reel10.image, reel10.position)
    screen.blit(reel100.image, reel100.position)
    screen.blit(reel1000.image, reel1000.position)
    screen.blit(meter, meter_position)

    if s.game.line2.position == 0:
        p = [233,368]
        screen.blit(columnb1, p)
        p = [284,369]
        screen.blit(columnb2, p)
    else:
        p = [233,368]
        screen.blit(columnb2, p)
        p = [284,369]
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


    nc_p = [230,368]
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
        eb_position = [41,1040]
        screen.blit(extra_balls, eb_position)

    if s.game.extra_ball.position >= 1:
        eb_position = [150,1040]
        screen.blit(eb_number, eb_position)
    if s.game.extra_ball.position >= 2:
        eb_position = [201,1040]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 3:
        eb_position = [262,1040]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 4:
        eb_position = [323,1040]
        screen.blit(eb_number, eb_position)
    if s.game.extra_ball.position >= 5:
        eb_position = [374,1040]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 6:
        eb_position = [436,1040]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 7:
        eb_position = [498,1040]
        screen.blit(eb_number, eb_position)
    if s.game.extra_ball.position >= 8:
        eb_position = [548,1040]
        screen.blit(eb, eb_position)
    if s.game.extra_ball.position >= 9:
        eb_position = [610,1040]
        screen.blit(eb, eb_position)

    if s.game.red_star.status == True:
        rs_position = [18,460]
        screen.blit(time, rs_position)
    if s.game.yellow_star.status == True:
        rs_position = [18,504]
        screen.blit(time, rs_position)

    if s.game.mystic_lines.position >= 4 or s.game.two_red_letter.status == True or s.game.three_red_letter.status == True:
        if s.game.selection_feature.position < 7:
            bfp = [18,548]
            screen.blit(time, bfp)
        elif s.game.selection_feature.position in [7,8]:
            bfp = [19,416]
            screen.blit(time, bfp)
        elif s.game.selection_feature.position == 9:
            bfp = [18,372]
            screen.blit(time, bfp)

    if s.game.ball_count.position < 1:
        if s.game.odds_only.status == True:
            b = [18,874]
            screen.blit(button, b)
        elif s.game.features.status == True:
            b = [18,912]
            screen.blit(button, b)
        elif s.game.special.status == True:
            b = [18,989]
            screen.blit(button, b)
        else:
            b = [18,950]
            screen.blit(button, b)


    if s.game.mystic_lines.position == 1:
        p = [203,680]
        screen.blit(ml_arrow, p)
    if s.game.mystic_lines.position == 2:
        p = [236,680]
        screen.blit(ml_arrow, p)
    if s.game.mystic_lines.position == 3:
        p = [267,680]
        screen.blit(ml_arrow, p)
    if s.game.mystic_lines.position >= 4:
        p = [300,683]
        screen.blit(ml_a, p)
        p = [335,591]
        screen.blit(ml_letter, p)
    if s.game.mystic_lines.position == 5:
        p = [334,680]
        screen.blit(ml_arrow, p)
    if s.game.mystic_lines.position == 6:
        p = [360,681]
        screen.blit(ml_arrow, p)
    if s.game.mystic_lines.position >= 7:
        p = [396,682]
        screen.blit(ml_b, p)
        p = [262,591]
        screen.blit(ml_letter, p)
    if s.game.mystic_lines.position == 8:
        p = [430,680]
        screen.blit(ml_arrow, p)
    if s.game.mystic_lines.position == 9:
        p = [459,680]
        screen.blit(ml_arrow, p)
    if s.game.mystic_lines.position == 10:
        p = [492,682]
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
                    p = [284,526]
                    screen.blit(number, p)
                else:
                    p = [234,529]
                    screen.blit(number, p)
            if 2 in s.holes:
                if s.game.line2.position == 0:
                    p = [282,377]
                    screen.blit(number, p)
                else:
                    p = [232,378]
                    screen.blit(number, p)
            if 3 in s.holes:
                if s.game.line2.position == 0:
                    p = [232,427]
                    screen.blit(number, p)
                else:
                    p = [282,426]
                    screen.blit(number, p)
            if 4 in s.holes:
                if s.game.line3.position == 0:
                    p = [387,378]
                    screen.blit(number, p)
                else:
                    p = [440,378]
                    screen.blit(number, p)
            if 5 in s.holes:
                if s.game.line1.position == 0 or s.game.line1.position == 2:
                    p = [336,477]
                    screen.blit(number, p)
                elif s.game.line1.position == 1:
                    p = [336,526]
                    screen.blit(number, p)
                else:
                    p = [336,428]
                    screen.blit(number, p)
            if 6 in s.holes:
                if s.game.line3.position == 0:
                    p = [440,378]
                    screen.blit(number, p)
                else:
                    p = [387,378]
                    screen.blit(number, p)
            if 7 in s.holes:
                if s.game.line1.position == 0 or s.game.line1.position == 2:
                    p = [336,526]
                    screen.blit(number, p)
                elif s.game.line1.position == 1:
                    p = [334,377]
                    screen.blit(number, p)
                else:
                    p = [336,476]
                    screen.blit(number, p)
            if 8 in s.holes:
                if s.game.line2.position == 0:
                    p = [232,378]
                    screen.blit(number, p)
                else:
                    p = [282,378]
                    screen.blit(number, p)
            if 9 in s.holes:
                if s.game.line1.position == 0 or s.game.line1.position == 2:
                    p = [336,427]
                    screen.blit(number, p)
                elif s.game.line1.position == 1:
                    p = [336,476]
                    screen.blit(number, p)
                else:
                    p = [336,377]
                    screen.blit(number, p)
            if 10 in s.holes:
                if s.game.line3.position == 0:
                    p = [442,477]
                    screen.blit(number, p)
                else:
                    p = [388,476]
                    screen.blit(number, p)
            if 11 in s.holes:
                if s.game.line3.position == 0:
                    p = [388,428]
                    screen.blit(number, p)
                else:
                    p = [442,428]
                    screen.blit(number, p)
            if 12 in s.holes:
                if s.game.line3.position == 0:
                    p = [387,476]
                    screen.blit(number, p)
                else:
                    p = [442,478]
                    screen.blit(number, p)
            if 13 in s.holes:
                if s.game.line3.position == 0:
                    p = [442,526]
                    screen.blit(number, p)
                else:
                    p = [387,526]
                    screen.blit(number, p)
            if 14 in s.holes:
                if s.game.line3.position == 0:
                    p = [442,428]
                    screen.blit(number, p)
                else:
                    p = [388,428]
                    screen.blit(number, p)
            if 15 in s.holes:
                if s.game.line2.position == 0:
                    p = [282,426]
                    screen.blit(number, p)
                else:
                    p = [232,426]
                    screen.blit(number, p)
            if 16 in s.holes:
                if s.game.line1.position == 0 or s.game.line1.position == 2:
                    p = [336,378]
                    screen.blit(number, p)
                elif s.game.line1.position == 1:
                    p = [336,428]
                    screen.blit(number, p)
                else:
                    p = [336,526]
                    screen.blit(number, p)
            if 17 in s.holes:
                if s.game.line2.position == 0:
                    p = [285,479]
                    screen.blit(number, p)
                else:
                    p = [233,479]
                    screen.blit(number, p)
            if 18 in s.holes:
                if s.game.line2.position == 0:
                    p = [233,479]
                    screen.blit(number, p)
                else:
                    p = [285,479]
                    screen.blit(number, p)
            if 19 in s.holes:
                if s.game.line3.position == 0:
                    p = [387,526]
                    screen.blit(number, p)
                else:
                    p = [442,526]
                    screen.blit(number, p)
            if 20 in s.holes:
                if s.game.line2.position == 0:
                    p = [232,528]
                    screen.blit(number, p)
                else:
                    p = [284,526]
                    screen.blit(number, p)

    if s.game.red_odds.position == 1:
        o = [192,783]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 2:
        o = [230,783]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 3:
        o = [267,783]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 4:
        o = [305,783]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 5:
        o = [343,783]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 6:
        o = [385,783]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 7:
        o = [436,783]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 8:
        o = [483,783]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 9:
        o = [530,783]
        screen.blit(odds, o)
    elif s.game.red_odds.position == 10:
        o = [578,783]
        screen.blit(odds, o)

    if s.game.green_odds.position == 1:
        o = [192,843]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 2:
        o = [230,843]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 3:
        o = [267,843]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 4:
        o = [305,843]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 5:
        o = [343,843]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 6:
        o = [385,843]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 7:
        o = [436,843]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 8:
        o = [483,843]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 9:
        o = [530,843]
        screen.blit(odds, o)
    elif s.game.green_odds.position == 10:
        o = [578,843]
        screen.blit(odds, o)

    if s.game.yellow_odds.position == 1:
        o = [192,907]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 2:
        o = [230,907]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 3:
        o = [267,907]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 4:
        o = [305,907]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 5:
        o = [343,907]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 6:
        o = [385,907]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 7:
        o = [436,907]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 8:
        o = [483,907]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 9:
        o = [530,907]
        screen.blit(odds, o)
    elif s.game.yellow_odds.position == 10:
        o = [578,907]
        screen.blit(odds, o)
        
    if s.game.blue_odds.position == 1:
        o = [192,973]
        screen.blit(odds, o)
    elif s.game.blue_odds.position == 2:
        o = [230,973]
        screen.blit(odds, o)
    elif s.game.blue_odds.position == 3:
        o = [267,973]
        screen.blit(odds, o)
    elif s.game.blue_odds.position == 4:
        o = [305,973]
        screen.blit(odds, o)
    elif s.game.blue_odds.position == 5:
        o = [343,973]
        screen.blit(odds, o)
    elif s.game.blue_odds.position == 6:
        o = [385,973]
        screen.blit(odds, o)
    elif s.game.blue_odds.position == 7:
        o = [436,973]
        screen.blit(odds, o)
    elif s.game.blue_odds.position == 8:
        o = [483,973]
        screen.blit(odds, o)
    elif s.game.blue_odds.position == 9:
        o = [530,973]
        screen.blit(odds, o)
    elif s.game.blue_odds.position == 10:
        o = [578,973]
        screen.blit(odds, o)
   
    p = [307,217]
    screen.blit(letter1, p)
    p = [346,217]
    screen.blit(letter2, p)
    p = [402,217]
    screen.blit(letter3, p)
    p = [451,217]
    screen.blit(letter4, p)
    p = [497,217]
    screen.blit(letter5, p)
    p = [572,217]
    screen.blit(letter6, p)

    if s.game.red_odds.position < 5:
        p = [307,217]
        screen.blit(red_letter1, p)
    if s.game.red_odds.position in [5,6]:
        p = [346,217]
        screen.blit(red_letter2, p)
    if s.game.red_odds.position == 7:
        p = [402,217]
        screen.blit(red_letter3, p)
    if s.game.red_odds.position == 8:
        p = [451,217]
        screen.blit(red_letter4, p)
    if s.game.red_odds.position == 9:
        p = [497,217]
        screen.blit(red_letter5, p)
    if s.game.red_odds.position == 10:
        p = [572,217]
        screen.blit(red_letter6, p)

    if s.game.two_red_letter.status == True:
        p = [18,258]
        screen.blit(red_letter, p)
        p = [92,220]
        screen.blit(two_red, p)
    if s.game.three_red_letter.status == True:
        p = [18,258]
        screen.blit(red_letter, p)
        p = [18,219]
        screen.blit(three_red, p)

    if s.game.three_stars.status == True:
        p = [18,297]
        screen.blit(four_stars, p)
        p = [18,334]
        screen.blit(three_stars, p)
    if s.game.six_stars.status == True:
        p = [18,297]
        screen.blit(four_stars, p)
        p = [92,334]
        screen.blit(six_stars, p)

    if s.game.double_red.status == True:
        p = [20,610]
        screen.blit(red_double, p)
    if s.game.double_yellow.status == True:
        p = [94,610]
        screen.blit(yellow_double, p)
    if s.game.double_green.status == True:
        p = [20,683]
        screen.blit(green_double, p)
    if s.game.double_blue.status == True:
        p = [94,683]
        screen.blit(blue_double, p)

    if s.game.triple.status == False and (s.game.double_red.status == True or s.game.double_yellow.status == True or s.game.double_green.status == True or s.game.double_blue.status == True):
        p = [52,680]
        screen.blit(double_triple, p)

    if s.game.triple.status == True and (s.game.double_red.status == True or s.game.double_yellow.status == True or s.game.double_green.status == True or s.game.double_blue.status == True):
        p = [52,647]
        screen.blit(double_triple, p)

    if s.game.tilt.status == True:
        tilt_position = [652,817]
        screen.blit(tilt, tilt_position)

    # Special Game
    if s.game.special_odds.position > 0:
        if s.game.special_odds.position == 1:
            p = [600,512]
            screen.blit(special_odds, p)
            p = [547,511]
            screen.blit(seven_odds, p)
        if s.game.special_odds.position == 2:
            p = [599,482]
            screen.blit(special_odds, p)
            p = [547,482]
            screen.blit(seven_odds, p)
        if s.game.special_odds.position == 3:
            p = [599,453]
            screen.blit(special_odds, p)
            p = [547,452]
            screen.blit(seven_odds, p)
        if s.game.special_odds.position == 4:
            p = [599,424]
            screen.blit(special_odds, p)
            p = [547,424]
            screen.blit(seven_odds, p)
        if s.game.special_odds.position == 5:
            p = [599,395]
            screen.blit(special_odds, p)
            p = [547,394]
            screen.blit(seven_odds, p)
        if s.game.special_odds.position == 6:
            p = [598,366]
            screen.blit(special_odds, p)
            p = [547,366]
            screen.blit(seven_odds, p)
        if s.game.special_odds.position == 7:
            p = [598,337]
            screen.blit(special_odds, p)
            p = [548,336]
            screen.blit(seven_odds, p)
        if s.game.special_odds.position == 8:
            p = [598,308]
            screen.blit(special_odds, p)
            p = [548,308]
            screen.blit(seven_odds, p)
        if s.game.special_odds.position == 9:
            p = [599,278]
            screen.blit(special_odds, p)
            p = [548,279]
            screen.blit(seven_odds, p)

    if s.game.special_odds.position > 0:
        if s.game.special_replay_counter.position > 0:
            p = [608,732]
            screen.blit(collected, p)
        
        if s.game.ball_count.position < 3:
            p = [531,731]
            screen.blit(collected, p)

        if s.game.special_game.position == 2:
            p = [598,540]
            screen.blit(ball, p)
            p = [608,635]
            screen.blit(collected, p)
        if s.game.special_game.position == 3:
            p = [626,540]
            screen.blit(ball, p)
            p = [608,635]
            screen.blit(collected, p)
        if s.game.special_game.position == 4:
            p = [656,540]
            screen.blit(ball, p)
            p = [608,635]
            screen.blit(collected, p)

        if s.game.missed.status == True:
            p = [608,684]
            screen.blit(collected, p)

    if s.game.twin_number.position == 1:
        p = [204,739]
        screen.blit(ml_arrow, p)
    elif s.game.twin_number.position == 2:
        p = [236,738]
        screen.blit(ml_arrow, p)
    elif s.game.twin_number.position == 3:
        p = [269,738]
        screen.blit(ml_arrow, p)
    if s.game.twin_number.position >= 4:
        if s.game.twelve.status == True:
            p = [300,728]
            screen.blit(twin_number, p)
        if s.game.eight.status == True:
            p = [300,752]
            screen.blit(twin_number, p)
    if s.game.twin_number.position == 5:
        p = [370,739]
        screen.blit(ml_arrow, p)
    elif s.game.twin_number.position == 6:
        p = [400,739]
        screen.blit(ml_arrow, p)
    elif s.game.twin_number.position == 7:
        p = [430,739]
        screen.blit(ml_arrow, p)
    if s.game.twin_number.position == 8:
        if s.game.eight.status == True:
            p = [462,730]
            screen.blit(twin_number, p)
        if s.game.twelve.status == True:
            p = [462,752]
            screen.blit(twin_number, p)

    if s.game.bonus.position == 1:
        p = [552,702]
        screen.blit(diamond, p)
    elif s.game.bonus.position == 2:
        p = [535,686]
        screen.blit(diamond, p)
    elif s.game.bonus.position == 3:
        p = [536,660]
        screen.blit(diamond, p)
    elif s.game.bonus.position == 4:
        p = [535,635]
        screen.blit(diamond, p)
    elif s.game.bonus.position == 5:
        p = [535,608]
        screen.blit(diamond, p)
    elif s.game.bonus.position == 6:
        p = [534,584]
        screen.blit(diamond, p)
    elif s.game.bonus.position == 7:
        p = [546,552]
        screen.blit(diamond_7, p)
    elif s.game.bonus.position == 8:
        p = [572,582]
        screen.blit(diamond, p)
    elif s.game.bonus.position == 9:
        p = [573,608]
        screen.blit(diamond, p)
    elif s.game.bonus.position == 10:
        p = [573,634]
        screen.blit(diamond, p)
    elif s.game.bonus.position == 11:
        p = [574,660]
        screen.blit(diamond, p)
    elif s.game.bonus.position == 12:
        p = [574,686]
        screen.blit(diamond, p)

    pygame.display.update()

def blink(args):
    dirty_rects = []
    s = args[0]
    b = args[1]
    sn = args[2]

    if b == 0:
        if sn == 1:
            p = [287,640]
            dirty_rects.append(screen.blit(select_now, p))
        pygame.display.update(dirty_rects)
    else:
        dirty_rects.append(screen.blit(bg_gi, (287,640), pygame.Rect(287,640,146,30)))
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
    
        nc_p = [230,368]
        dirty_rects.append(screen.blit(number_card, nc_p))
        if (s.game.anti_cheat.status == True):
            dirty_rects.append(screen.blit(bg_gi, (224,264), pygame.Rect(224,264,270,408)))
        else:
            dirty_rects.append(screen.blit(bg_off, (224,264), pygame.Rect(224,264,270,408)))

        p = [307,217]
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],42,57)))
        dirty_rects.append(screen.blit(letter1, p))

        p = [346,217]
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],55,57)))
        dirty_rects.append(screen.blit(letter2, p))
        
        p = [402,217]
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],49,57)))
        dirty_rects.append(screen.blit(letter3, p))

        p = [451,217]
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],43,57)))
        dirty_rects.append(screen.blit(letter4, p))

        p = [497,217]
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],54,57)))
        dirty_rects.append(screen.blit(letter5, p))
        
        p = [572,217]
        dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],53,57)))
        dirty_rects.append(screen.blit(letter6, p))
        
        if s.game.red_odds.position < 5:
            p = [307,217]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],42,57)))
            dirty_rects.append(screen.blit(letter1, p))
            dirty_rects.append(screen.blit(red_letter1, p))
        if s.game.red_odds.position  in [5,6]:
            p = [346,217]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],55,57)))
            dirty_rects.append(screen.blit(letter2, p))
            dirty_rects.append(screen.blit(red_letter2, p))
        if s.game.red_odds.position == 7:
            p = [402,217]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],49,57)))
            dirty_rects.append(screen.blit(letter3, p))
            dirty_rects.append(screen.blit(red_letter3, p))
        if s.game.red_odds.position == 8:
            p = [451,217]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],43,57)))
            dirty_rects.append(screen.blit(letter4, p))
            dirty_rects.append(screen.blit(red_letter4, p))
        if s.game.red_odds.position == 9:
            p = [497,217]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],54,57)))
            dirty_rects.append(screen.blit(letter5, p))
            dirty_rects.append(screen.blit(red_letter5, p))
        if s.game.red_odds.position == 10:
            p = [572,217]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],53,57)))
            dirty_rects.append(screen.blit(letter6, p))
            dirty_rects.append(screen.blit(red_letter6, p))

        if s.game.mystic_lines.position >= 4:
            p = [335,591]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],49,48)))
            dirty_rects.append(screen.blit(ml_letter, p))
        if s.game.mystic_lines.position >= 7:
            p = [262,591]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],49,48)))
            dirty_rects.append(screen.blit(ml_letter, p))
        if s.game.mystic_lines.position == 10:
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
     
        nc_p = [230,368]
        dirty_rects.append(screen.blit(number_card, nc_p))
        if (s.game.anti_cheat.status == True):
            dirty_rects.append(screen.blit(bg_gi, (233,369), pygame.Rect(233,369,270,212)))
        else:
            dirty_rects.append(screen.blit(bg_off, (233,369), pygame.Rect(233,369,270,212)))

        if s.game.mystic_lines.position >= 4:
            p = [335,591]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],49,48)))
            dirty_rects.append(screen.blit(ml_letter, p))
        if s.game.mystic_lines.position >= 7:
            p = [262,591]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],49,48)))
            dirty_rects.append(screen.blit(ml_letter, p))
        if s.game.mystic_lines.position == 10:
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

        nc_p = [230,368]
        dirty_rects.append(screen.blit(number_card, nc_p))
        if (s.game.anti_cheat.status == True):
            dirty_rects.append(screen.blit(bg_gi, (230,369), pygame.Rect(230,369,273,212)))
        else:
            dirty_rects.append(screen.blit(bg_off, (230,369), pygame.Rect(230,369,273,212)))

        if s.game.mystic_lines.position >= 4:
            p = [335,591]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],49,48)))
            dirty_rects.append(screen.blit(ml_letter, p))
        if s.game.mystic_lines.position >= 7:
            p = [262,591]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],49,48)))
            dirty_rects.append(screen.blit(ml_letter, p))
        if s.game.mystic_lines.position == 10:
            p = [410,591]
            dirty_rects.append(screen.blit(bg_gi, p, pygame.Rect(p[0],p[1],49,48)))
            dirty_rects.append(screen.blit(ml_letter, p))

    pygame.display.update(dirty_rects)


def eb_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]

    if s.game.extra_ball.position < 1:
        dirty_rects.append(screen.blit(bg_gi, (150,1040), pygame.Rect(150,1040,47,31)))
    if s.game.extra_ball.position < 2:
        dirty_rects.append(screen.blit(bg_gi, (201,1040), pygame.Rect(201,1040,59,34)))
    if s.game.extra_ball.position < 3:
        dirty_rects.append(screen.blit(bg_gi, (262,1040), pygame.Rect(262,1040,59,34)))
    if s.game.extra_ball.position < 4:
        dirty_rects.append(screen.blit(bg_gi, (323,1040), pygame.Rect(323,1040,47,31)))
    if s.game.extra_ball.position < 5:
        dirty_rects.append(screen.blit(bg_gi, (374,1040), pygame.Rect(374,1040,59,34)))
    if s.game.extra_ball.position < 6:
        dirty_rects.append(screen.blit(bg_gi, (436,1040), pygame.Rect(436,1040,59,34)))
    if s.game.extra_ball.position < 7:
        dirty_rects.append(screen.blit(bg_gi, (498,1040), pygame.Rect(498,1040,47,31)))
    if s.game.extra_ball.position < 8:
        dirty_rects.append(screen.blit(bg_gi, (548,1040), pygame.Rect(548,1040,59,34)))
    if s.game.extra_ball.position < 9:
        dirty_rects.append(screen.blit(bg_gi, (610,1040), pygame.Rect(610,1040,59,34)))
    pygame.display.update(dirty_rects)

    if num in [0,25,14,49]:
        if s.game.extra_ball.position < 1:
            p = [150,1040]
            dirty_rects.append(screen.blit(eb_number, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [39,1,26,15]:
        if s.game.extra_ball.position < 2:
            p = [201,1040]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects) 
            return
    elif num in [3,4,17,28,29,40]:
        if s.game.extra_ball.position < 3:
            p = [262,1040]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [5,18,30,43]:
        if s.game.extra_ball.position < 4:
            p = [323,1040]
            dirty_rects.append(screen.blit(eb_number, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [7,8,19,32,33,44]:
        if s.game.extra_ball.position < 5:
            p = [374,1040]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [9,10,20,34,35,45]:
        if s.game.extra_ball.position < 6:
            p = [436,1040]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [11,21,36,46]:
        if s.game.extra_ball.position < 7:
            p = [498,1040]
            dirty_rects.append(screen.blit(eb_number, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [12,22,37,47]:
        if s.game.extra_ball.position < 8:
            p = [548,1040]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return
    elif num in [2,6,13,16,23,27,31,38,41,48]:
        if s.game.extra_ball.position < 9:
            p = [610,1040]
            dirty_rects.append(screen.blit(eb, p))
            pygame.display.update(dirty_rects)
            return

def clear_odds(s, num):
    global screen

    dirty_rects = []
    
    if s.game.double_red.status == False:
        dirty_rects.append(screen.blit(bg_gi, (20,610), pygame.Rect(20,610,74,74)))
    if s.game.double_yellow.status == False:
        dirty_rects.append(screen.blit(bg_gi, (94,610), pygame.Rect(94,610,74,74)))
    if s.game.double_green.status == False:
        dirty_rects.append(screen.blit(bg_gi, (20,683), pygame.Rect(20,683,74,74)))
    if s.game.double_blue.status == False:
        dirty_rects.append(screen.blit(bg_gi, (94,683), pygame.Rect(94,683,74,74)))

    if s.game.yellow_odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (230,907), pygame.Rect(230,907,46,61)))
    if s.game.yellow_odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (343,907), pygame.Rect(343,907,46,61)))
    if s.game.yellow_odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (385,907), pygame.Rect(385,907,46,61)))
    if s.game.yellow_odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (436,907), pygame.Rect(436,907,46,61)))
    if s.game.yellow_odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (483,907), pygame.Rect(483,907,46,61)))
    if s.game.yellow_odds.position != 9:
        dirty_rects.append(screen.blit(bg_gi, (530,907), pygame.Rect(530,907,46,61)))
    if s.game.yellow_odds.position != 10:
        dirty_rects.append(screen.blit(bg_gi, (578,907), pygame.Rect(578,907,46,61)))

    if s.game.red_odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (267,783), pygame.Rect(267,783,46,61)))
    if s.game.red_odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (305,783), pygame.Rect(305,783,46,61)))
    if s.game.red_odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (385,783), pygame.Rect(385,783,46,61)))
    if s.game.red_odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (436,783), pygame.Rect(436,783,46,61)))
    if s.game.red_odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (483,783), pygame.Rect(483,783,46,61)))
    if s.game.red_odds.position != 9:
        dirty_rects.append(screen.blit(bg_gi, (530,783), pygame.Rect(530,783,46,61)))
    if s.game.red_odds.position != 10:
        dirty_rects.append(screen.blit(bg_gi, (578,783), pygame.Rect(578,783,46,61)))
    if s.game.blue_odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (230,973), pygame.Rect(230,973,46,61)))
        dirty_rects.append(screen.blit(bg_gi, (230,843), pygame.Rect(230,843,46,61)))
    if s.game.blue_odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (343,973), pygame.Rect(343,973,46,61)))
        dirty_rects.append(screen.blit(bg_gi, (343,843), pygame.Rect(343,843,46,61)))
    if s.game.blue_odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (436,973), pygame.Rect(436,973,46,61)))
        dirty_rects.append(screen.blit(bg_gi, (436,843), pygame.Rect(436,843,46,61)))
    if s.game.blue_odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (483,973), pygame.Rect(483,973,46,61)))
        dirty_rects.append(screen.blit(bg_gi, (483,843), pygame.Rect(483,843,46,61)))
    if s.game.blue_odds.position != 9:
        dirty_rects.append(screen.blit(bg_gi, (530,973), pygame.Rect(530,973,46,61)))
        dirty_rects.append(screen.blit(bg_gi, (530,843), pygame.Rect(530,843,46,61)))
    if s.game.blue_odds.position != 10:
        dirty_rects.append(screen.blit(bg_gi, (578,973), pygame.Rect(578,973,46,61)))
        dirty_rects.append(screen.blit(bg_gi, (578,843), pygame.Rect(578,843,46,61)))

    pygame.display.update(dirty_rects)

def draw_odds_animation(s, num):
    global screen
    dirty_rects = []

    if num in [7,32]:
        if s.game.double_red.status == False:
            p = [20,610]
            dirty_rects.append(screen.blit(red_double, p))
            pygame.display.update(dirty_rects)
            return
    if num in [15,40]:
        if s.game.double_yellow.status == False:
            p = [94,608]
            dirty_rects.append(screen.blit(yellow_double, p))
            pygame.display.update(dirty_rects)
            return
    if num in [0,25]:
        if s.game.double_green.status == False:
            p = [20,683]
            dirty_rects.append(screen.blit(green_double, p))
            pygame.display.update(dirty_rects)
            return
    if num in [9,34]:
        if s.game.double_blue.status == False:
            p = [94,683]
            dirty_rects.append(screen.blit(blue_double, p))
            pygame.display.update(dirty_rects)
            return

    if num in [22,47]:
        if s.game.yellow_odds.position != 2:
            p = [230,907]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [13,38]:
        if s.game.yellow_odds.position != 5:
            p = [343,907]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [20,45]:
        if s.game.yellow_odds.position != 6:
            p = [385,907]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [20,45]:
        if s.game.yellow_odds.position != 7:
            p = [436,907]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [12,37]:
        if s.game.yellow_odds.position != 8:
            p = [483,907]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [7,32]:
        if s.game.yellow_odds.position != 9:
            p = [530,907]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [21,46]:
        if s.game.yellow_odds.position != 10:
            p = [578,907]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return

    if num in [2,27]:
        if s.game.red_odds.position != 3:
            p = [267,783]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [10,35]:
        if s.game.red_odds.position != 4:
            p = [305,783]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [12,37]:
        if s.game.red_odds.position != 6:
            p = [385,783]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [6,31]:
        if s.game.red_odds.position != 7:
            p = [436,783]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [14,39]:
        if s.game.red_odds.position != 8:
            p = [483,783]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [1,26]:
        if s.game.red_odds.position != 9:
            p = [530,783]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [20,45]:
        if s.game.red_odds.position != 10:
            p = [578,783]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return

    if num in [8,33]:
        if s.game.blue_odds.position != 2:
            p = [230,973]
            dirty_rects.append(screen.blit(odds, p))
            p = [230,843]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [23,48]:
        if s.game.blue_odds.position != 5:
            p = [343,973]
            dirty_rects.append(screen.blit(odds, p))
            p = [343,843]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [3,28]:
        if s.game.blue_odds.position != 7:
            p = [436,973]
            dirty_rects.append(screen.blit(odds, p))
            p = [436,843]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
    if num in [18,43]:
        if s.game.blue_odds.position != 8:
            p = [483,973]
            dirty_rects.append(screen.blit(odds, p))
            p = [483,843]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [5,30]:
        if s.game.blue_odds.position != 9:
            p = [530,973]
            dirty_rects.append(screen.blit(odds, p))
            p = [530,843]
            dirty_rects.append(screen.blit(odds, p))
            pygame.display.update(dirty_rects)
            return
    if num in [16,41]:
        if s.game.blue_odds.position != 10:
            p = [578,973]
            dirty_rects.append(screen.blit(odds, p))
            p = [578,843]
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
        dirty_rects.append(screen.blit(bg_gi, (18,548), pygame.Rect(18,548,148,48)))
    if s.game.mystic_lines.position < 4 and s.game.two_red_letter.status == False and s.game.three_red_letter.status == False:
        dirty_rects.append(screen.blit(bg_gi, (18,548), pygame.Rect(18,548,148,48)))

    if s.game.selection_feature.position not in [7,8]:
        dirty_rects.append(screen.blit(bg_gi, (19,416), pygame.Rect(19,416,148,48)))
    if s.game.mystic_lines.position < 4 and s.game.two_red_letter.status == False and s.game.three_red_letter.status == False:
        dirty_rects.append(screen.blit(bg_gi, (19,416), pygame.Rect(19,416,148,48)))
    
    if s.game.selection_feature.position < 9:
        dirty_rects.append(screen.blit(bg_gi, (18,372), pygame.Rect(18,372,148,48)))
    if s.game.mystic_lines.position < 4 and s.game.two_red_letter.status == False and s.game.three_red_letter.status == False:
        dirty_rects.append(screen.blit(bg_gi, (18,372), pygame.Rect(18,372,148,48)))

    if s.game.yellow_star.status == False:
        dirty_rects.append(screen.blit(bg_gi, (18,504), pygame.Rect(18,504,148,48)))
    if s.game.red_star.status == False:
        dirty_rects.append(screen.blit(bg_gi, (18,460), pygame.Rect(18,460,148,48)))

    if s.game.two_red_letter.status == False:
        dirty_rects.append(screen.blit(bg_gi, (92,220), pygame.Rect(92,220,76,41)))
    if s.game.three_red_letter.status == False:
        dirty_rects.append(screen.blit(bg_gi, (18,219), pygame.Rect(18,219,76,41)))
    if s.game.three_stars.status == False:
        dirty_rects.append(screen.blit(bg_gi, (18,334), pygame.Rect(18,334,77,27)))
    if s.game.six_stars.status == False:
        dirty_rects.append(screen.blit(bg_gi, (92,334), pygame.Rect(92,334,77,27)))
    if s.game.mystic_lines.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (236,680), pygame.Rect(236,680,29,29)))
    if s.game.mystic_lines.position < 4:
        dirty_rects.append(screen.blit(bg_gi, (335,591), pygame.Rect(335,591,49,48)))
    if s.game.mystic_lines.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (334,680), pygame.Rect(334,680,29,29)))
    if s.game.mystic_lines.position < 7:
        dirty_rects.append(screen.blit(bg_gi, (262,591), pygame.Rect(262,591,49,48)))
    if s.game.mystic_lines.position != 9:
        dirty_rects.append(screen.blit(bg_gi, (459,680), pygame.Rect(459,680,29,29)))
    if s.game.mystic_lines.position < 10:
        dirty_rects.append(screen.blit(bg_gi, (410,591), pygame.Rect(410,591,49,48)))

    pygame.display.update(dirty_rects)


def draw_feature_animation(s, num):
    global screen
    dirty_rects = []
 
    if num in [10,35]:
        if s.game.selection_feature.position not in [1,2,3,4,5,6] and (s.game.mystic_lines.position < 4 and s.game.two_red_letter.status == False and s.game.three_red_letter.status == False):
            p = [18,548]
            dirty_rects.append(screen.blit(time, p))
            pygame.display.update(dirty_rects)
            return
    if num in [9,34]:
        if s.game.selection_feature.position not in [7,8] and (s.game.mystic_lines.position < 4 and s.game.two_red_letter.status == False and s.game.three_red_letter.status == False):
            p = [19,416]
            dirty_rects.append(screen.blit(time, p))
            pygame.display.update(dirty_rects)
            return
    if num in [6,31]:
        if s.game.selection_feature.position not in [9] and (s.game.mystic_lines.position < 4 and s.game.two_red_letter.status == False and s.game.three_red_letter.status == False):
            p = [18,372]
            dirty_rects.append(screen.blit(time, p))
            pygame.display.update(dirty_rects)
            return
    if num in [11,36]:
        if s.game.red_star.status == False:
            p = [18,460]
            dirty_rects.append(screen.blit(time, p))
            pygame.display.update(dirty_rects)
            s.game.coils.redROLamp.pulse(85)
            return
    if num in [4,29]:
        if s.game.yellow_star.status == False:
            p = [18,504]
            dirty_rects.append(screen.blit(time, p))
            pygame.display.update(dirty_rects)
            s.game.coils.yellowROLamp.pulse(85)
            return

    if num in [13,38]:
        if s.game.three_red_letter.status == False:
            p = [18,219]
            dirty_rects.append(screen.blit(three_red, p))
            pygame.display.update(dirty_rects)
            return
    if num in [44,19]:
        if s.game.two_red_letter.status == False:
            p = [92,220]
            dirty_rects.append(screen.blit(two_red, p))
            pygame.display.update(dirty_rects)
            return
    if num in [16,41]:
        if s.game.three_stars.status == False:
            p = [18,334]
            dirty_rects.append(screen.blit(three_stars, p))
            pygame.display.update(dirty_rects)
            return
    if num in [4,29]:
        if s.game.six_stars.status == False:
            p = [92,334]
            dirty_rects.append(screen.blit(six_stars, p))
            pygame.display.update(dirty_rects)
            return
    if num in [5,30]:
        if s.game.mystic_lines.position != 2:
            p = [236,680]
            dirty_rects.append(screen.blit(ml_arrow, p))
            pygame.display.update(dirty_rects)
            return
    if num in [23,48]:
        if s.game.mystic_lines.position < 4:
            p = [335,591]
            dirty_rects.append(screen.blit(ml_letter, p))
            pygame.display.update(dirty_rects)
            return
    if num in [0,25]:
        if s.game.mystic_lines.position != 5:
            p = [334,680]
            dirty_rects.append(screen.blit(ml_arrow, p))
            pygame.display.update(dirty_rects)
            return
    if num in [12,37,22,47]:
        if s.game.mystic_lines.position < 7:
            p = [262,591]
            dirty_rects.append(screen.blit(ml_letter, p))
            pygame.display.update(dirty_rects)
            return
    if num in [9,34]:
        if s.game.mystic_lines.position != 9:
            p = [459,680]
            dirty_rects.append(screen.blit(ml_arrow, p))
            pygame.display.update(dirty_rects)
            return
    if num in [10,35,24,49]:
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
        dirty_rects.append(screen.blit(bg_gi, (599,482), pygame.Rect(599,482,90,30)))
        dirty_rects.append(screen.blit(bg_gi, (547,482), pygame.Rect(547,482,42,32)))
    if s.game.special_odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (599,453), pygame.Rect(599,453,90,30)))
        dirty_rects.append(screen.blit(bg_gi, (547,452), pygame.Rect(547,452,42,32)))
    if s.game.special_odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (599,424), pygame.Rect(599,424,90,30)))
        dirty_rects.append(screen.blit(bg_gi, (547,424), pygame.Rect(547,424,42,32)))
    if s.game.special_odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (599,395), pygame.Rect(599,395,90,30)))
        dirty_rects.append(screen.blit(bg_gi, (547,394), pygame.Rect(547,394,42,32)))
    if s.game.special_odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (598,366), pygame.Rect(598,366,90,30)))
        dirty_rects.append(screen.blit(bg_gi, (547,366), pygame.Rect(547,366,42,32)))
    if s.game.special_odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (598,337), pygame.Rect(598,337,90,30)))
        dirty_rects.append(screen.blit(bg_gi, (548,336), pygame.Rect(548,336,42,32)))
    if s.game.special_odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (598,308), pygame.Rect(598,308,90,30)))
        dirty_rects.append(screen.blit(bg_gi, (548,308), pygame.Rect(548,308,42,32)))
    if s.game.special_odds.position != 9:
        dirty_rects.append(screen.blit(bg_gi, (599,278), pygame.Rect(599,278,90,30)))
        dirty_rects.append(screen.blit(bg_gi, (548,279), pygame.Rect(548,279,42,32)))

    pygame.display.update(dirty_rects)

    if num in [18,19,43,44]:
        if s.game.special_odds.position < 2:
            p = [599,482]
            dirty_rects.append(screen.blit(special_odds, p))
            p = [547,482]
            dirty_rects.append(screen.blit(seven_odds, p))
            pygame.display.update(dirty_rects) 
            return
    if num in [20,21,45,46]:
        if s.game.special_odds.position < 3:
            p = [599,453]
            dirty_rects.append(screen.blit(special_odds, p))
            p = [547,452]
            dirty_rects.append(screen.blit(seven_odds, p))
            pygame.display.update(dirty_rects) 
            return
    if num in [14,15,39,40]:
        if s.game.special_odds.position < 4:
            p = [599,424]
            dirty_rects.append(screen.blit(special_odds, p))
            p = [547,424]
            dirty_rects.append(screen.blit(seven_odds, p))
            pygame.display.update(dirty_rects) 
            return
    if num in [16,17,41,42]:
        if s.game.special_odds.position < 5:
            p = [599,395]
            dirty_rects.append(screen.blit(special_odds, p))
            p = [547,394]
            dirty_rects.append(screen.blit(seven_odds, p))
            pygame.display.update(dirty_rects) 
            return
    if num in [6,7,10,11,31,32,35,36]:
        if s.game.special_odds.position < 6:
            p = [598,366]
            dirty_rects.append(screen.blit(special_odds, p))
            p = [547,366]
            dirty_rects.append(screen.blit(seven_odds, p))
            pygame.display.update(dirty_rects) 
            return
    if num in [4,5,12,13,29,30,37,38]:
        if s.game.special_odds.position < 7:
            p = [598,337]
            dirty_rects.append(screen.blit(special_odds, p))
            p = [547,336]
            dirty_rects.append(screen.blit(seven_odds, p))
            pygame.display.update(dirty_rects) 
            return
    if num in [0,1,2,3,8,9,25,26,27,28,33,34]:
        if s.game.special_odds.position < 8:
            p = [598,308]
            dirty_rects.append(screen.blit(special_odds, p))
            p = [547,308]
            dirty_rects.append(screen.blit(seven_odds, p))
            pygame.display.update(dirty_rects) 
            return
    if num in [22,23,47,48]:
        if s.game.special_odds.position < 9:
            p = [599,278]
            dirty_rects.append(screen.blit(special_odds, p))
            p = [548,279]
            dirty_rects.append(screen.blit(seven_odds, p))
            pygame.display.update(dirty_rects) 
            return
