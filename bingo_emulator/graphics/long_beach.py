import pygame

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

card = pygame.image.load('long_beach/assets/card.png').convert_alpha()
balls_display = pygame.image.load('long_beach/assets/extra_balls.png').convert_alpha()
eball1_display = pygame.image.load('long_beach/assets/eb1.png').convert_alpha()
eball2_display = pygame.image.load('long_beach/assets/eb2.png').convert_alpha()
eball3_display = pygame.image.load('long_beach/assets/eb3.png').convert_alpha()
sign_display = pygame.image.load('long_beach/assets/return.png').convert_alpha()
b1 = pygame.image.load('long_beach/assets/arrow1.png').convert_alpha()
b = pygame.image.load('long_beach/assets/arrow.png').convert_alpha()
b15 = pygame.image.load('long_beach/assets/arrow15.png').convert_alpha()
number = pygame.image.load('long_beach/assets/number.png').convert_alpha()
tilt = pygame.image.load('long_beach/assets/tilt.png').convert_alpha()
r100 = pygame.image.load('long_beach/assets/100.png').convert_alpha()
r200 = pygame.image.load('long_beach/assets/200.png').convert_alpha()
r300 = pygame.image.load('long_beach/assets/300.png').convert_alpha()
r400 = pygame.image.load('long_beach/assets/400.png').convert_alpha()
r500 = pygame.image.load('long_beach/assets/500.png').convert_alpha()
r600 = pygame.image.load('long_beach/assets/600.png').convert_alpha()
r700 = pygame.image.load('long_beach/assets/700.png').convert_alpha()
r800 = pygame.image.load('long_beach/assets/800.png').convert_alpha()
r900 = pygame.image.load('long_beach/assets/900.png').convert_alpha()
r10 = pygame.image.load('long_beach/assets/10.png').convert_alpha()
r20 = pygame.image.load('long_beach/assets/20.png').convert_alpha()
r30 = pygame.image.load('long_beach/assets/30.png').convert_alpha()
r40 = pygame.image.load('long_beach/assets/40.png').convert_alpha()
r50 = pygame.image.load('long_beach/assets/50.png').convert_alpha()
r60 = pygame.image.load('long_beach/assets/60.png').convert_alpha()
r70 = pygame.image.load('long_beach/assets/70.png').convert_alpha()
r80 = pygame.image.load('long_beach/assets/80.png').convert_alpha()
r90 = pygame.image.load('long_beach/assets/90.png').convert_alpha()
r1 = pygame.image.load('long_beach/assets/1.png').convert_alpha()
r2 = pygame.image.load('long_beach/assets/2.png').convert_alpha()
r3 = pygame.image.load('long_beach/assets/3.png').convert_alpha()
r4 = pygame.image.load('long_beach/assets/4.png').convert_alpha()
r5 = pygame.image.load('long_beach/assets/5.png').convert_alpha()
r6 = pygame.image.load('long_beach/assets/6.png').convert_alpha()
r7 = pygame.image.load('long_beach/assets/7.png').convert_alpha()
r8 = pygame.image.load('long_beach/assets/8.png').convert_alpha()
r9 = pygame.image.load('long_beach/assets/9.png').convert_alpha()

def display(s, replays=0, menu=False):

    backglass_position = [0, 0]
    backglass = pygame.Surface(screen.get_size(), flags=pygame.SRCALPHA)
    backglass.fill((0, 0, 0))
    if menu == True:
        backglass = pygame.image.load('long_beach/assets/long_beach_menu.png')
    else:
        if (s.game.anti_cheat.status == True):
            backglass = pygame.image.load('long_beach/assets/long_beach_gi.png')
        else:
            backglass = pygame.image.load('long_beach/assets/long_beach_off.png')
    backglass = pygame.transform.scale(backglass, (720, 1280))
    
    screen.blit(backglass, backglass_position)

    if s.game.selector.position >= 1:
        card1_position = [250,475]
        screen.blit(card, card1_position)
    if s.game.selector.position >= 2:
        card2_position = [14,694]
        screen.blit(card, card2_position)
    if s.game.selector.position >= 3:
        card3_position = [486,700]
        screen.blit(card, card3_position)
 
    if s.game.eb_play.status == True:
        balls_position = [287,725]
        screen.blit(balls_display, balls_position)

    if s.game.extra_ball.position >= 1:
        balls_position = [313,884]
        screen.blit(eball1_display, balls_position)
    if s.game.extra_ball.position >= 2:
        balls_position = [350,872]
        screen.blit(eball2_display, balls_position)
    if s.game.extra_ball.position >= 3:
        balls_position = [391,840]
        screen.blit(eball3_display, balls_position)

    if s.game.selector.position > 0 and s.game.selector.position < 3:
        if s.game.ball_count.position <= 3:
            sign_position = [56,465]
            screen.blit(sign_display, sign_position)
    else:
        if s.game.selector.position > 0:
            if s.game.ball_count.position <= 5:
                sign_position = [56,465]
                screen.blit(sign_display, sign_position)

    if s.game.ball_return.position == 1:
        b_pos = [96,440]
        screen.blit(b1, b_pos)
    elif s.game.ball_return.position == 2:
        b_pos = [132,437]
        screen.blit(b, b_pos)
    elif s.game.ball_return.position == 3:
        b_pos = [168,437]
        screen.blit(b, b_pos)
    elif s.game.ball_return.position == 4:
        b_pos = [204,437]
        screen.blit(b, b_pos)
    elif s.game.ball_return.position == 5:
        b_pos = [241,437]
        screen.blit(b, b_pos)
    elif s.game.ball_return.position == 6:
        b_pos = [275,437]
        screen.blit(b, b_pos)
    elif s.game.ball_return.position == 7:
        b_pos = [312,437]
        screen.blit(b, b_pos)
    elif s.game.ball_return.position == 8:
        b_pos = [347,437]
        screen.blit(b, b_pos)
    elif s.game.ball_return.position == 9:
        b_pos = [381,437]
        screen.blit(b, b_pos)
    elif s.game.ball_return.position == 10:
        b_pos = [419,437]
        screen.blit(b, b_pos)
    elif s.game.ball_return.position == 11:
        b_pos = [454,437]
        screen.blit(b, b_pos)
    elif s.game.ball_return.position == 12:
        b_pos = [490,437]
        screen.blit(b, b_pos)
    elif s.game.ball_return.position == 13:
        b_pos = [526,437]
        screen.blit(b, b_pos)
    elif s.game.ball_return.position == 14:
        b_pos = [563,437]
        screen.blit(b, b_pos)
    elif s.game.ball_return.position == 15:
        b_pos = [596,447]
        screen.blit(b15, b_pos)



    if s.game.double.status == True:
        d_pos = [546,499]
        screen.blit(number, d_pos)
        d_pos = [585,499]
        screen.blit(number, d_pos)
        d_pos = [625,499]
        screen.blit(number, d_pos)

    if s.game.tilt.status == False:
        if s.holes:
            if 1 in s.holes:
                number_position = [295,510]
                screen.blit(number, number_position)
                number_position = [21,846]
                screen.blit(number, number_position)
                number_position = [573,892]
                screen.blit(number, number_position)
            if 2 in s.holes:
                number_position = [339,670]
                screen.blit(number, number_position)
                number_position = [20,808]
                screen.blit(number, number_position)
                number_position = [660,818]
                screen.blit(number, number_position)
            if 3 in s.holes:
                number_position = [425,514]
                screen.blit(number, number_position)
                number_position = [188,885]
                screen.blit(number, number_position)
                number_position = [528,774]
                screen.blit(number, number_position)
            if 4 in s.holes:
                number_position = [422,668]
                screen.blit(number, number_position)
                number_position = [103,731]
                screen.blit(number, number_position)
                number_position = [616,737]
                screen.blit(number, number_position)
            if 5 in s.holes:
                number_position = [250,511]
                screen.blit(number, number_position)
                number_position = [105,885]
                screen.blit(number, number_position)
                number_position = [656,891]
                screen.blit(number, number_position)
            if 6 in s.holes:
                number_position = [251,588]
                screen.blit(number, number_position)
                number_position = [187,731]
                screen.blit(number, number_position)
                number_position = [528,852]
                screen.blit(number, number_position)
            if 7 in s.holes:
                number_position = [424,588]
                screen.blit(number, number_position)
                number_position = [62,883]
                screen.blit(number, number_position)
                number_position = [529,735]
                screen.blit(number, number_position)
            if 8 in s.holes:
                number_position = [251,550]
                screen.blit(number, number_position)
                number_position = [188,808]
                screen.blit(number, number_position)
                number_position = [658,776]
                screen.blit(number, number_position)
            if 9 in s.holes:
                number_position = [338,510]
                screen.blit(number, number_position)
                number_position = [18,730]
                screen.blit(number, number_position)
                number_position = [660,737]
                screen.blit(number, number_position)
            if 10 in s.holes:
                number_position = [337,550]
                screen.blit(number, number_position)
                number_position = [20,883]
                screen.blit(number, number_position)
                number_position = [572,735]
                screen.blit(number, number_position)
            if 11 in s.holes:
                number_position = [380,590]
                screen.blit(number, number_position)
                number_position = [104,845]
                screen.blit(number, number_position)
                number_position = [614,815]
                screen.blit(number, number_position)
            if 12 in s.holes:
                number_position = [250,666]
                screen.blit(number, number_position)
                number_position = [145,808]
                screen.blit(number, number_position)
                number_position = [572,852]
                screen.blit(number, number_position)
            if 13 in s.holes:
                number_position = [423,628]
                screen.blit(number, number_position)
                number_position = [18,768]
                screen.blit(number, number_position)
                number_position = [485,851]
                screen.blit(number, number_position)
            if 14 in s.holes:
                number_position = [337,628]
                screen.blit(number, number_position)
                number_position = [103,768]
                screen.blit(number, number_position)
                number_position = [529,812]
                screen.blit(number, number_position)
            if 15 in s.holes:
                number_position = [380,667]
                screen.blit(number, number_position)
                number_position = [103,806]
                screen.blit(number, number_position)
                number_position = [486,772]
                screen.blit(number, number_position)
            if 16 in s.holes:
                number_position = [337,588]
                screen.blit(number, number_position)
                number_position = [145,730]
                screen.blit(number, number_position)
                number_position = [614,890]
                screen.blit(number, number_position)
            if 17 in s.holes:
                number_position = [422,550]
                screen.blit(number, number_position)
                number_position = [187,846]
                screen.blit(number, number_position)
                number_position = [571,812]
                screen.blit(number, number_position)
            if 18 in s.holes:
                number_position = [294,588]
                screen.blit(number, number_position)
                number_position = [60,806]
                screen.blit(number, number_position)
                number_position = [572,774]
                screen.blit(number, number_position)
            if 19 in s.holes:
                number_position = [380,550]
                screen.blit(number, number_position)
                number_position = [60,767]
                screen.blit(number, number_position)
                number_position = [614,851]
                screen.blit(number, number_position)
            if 20 in s.holes:
                number_position = [380,628]
                screen.blit(number, number_position)
                number_position = [146,768]
                screen.blit(number, number_position)
                number_position = [487,887]
                screen.blit(number, number_position)
            if 21 in s.holes:
                number_position = [294,628]
                screen.blit(number, number_position)
                number_position = [146,845]
                screen.blit(number, number_position)
                number_position = [487,735]
                screen.blit(number, number_position)
            if 22 in s.holes:
                number_position = [295,549]
                screen.blit(number, number_position)
                number_position = [62,845]
                screen.blit(number, number_position)
                number_position = [616,774]
                screen.blit(number, number_position)
            if 23 in s.holes:
                number_position = [294,666]
                screen.blit(number, number_position)
                number_position = [146,883]
                screen.blit(number, number_position)
                number_position = [658,853]
                screen.blit(number, number_position)
            if 24 in s.holes:
                number_position = [251,626]
                screen.blit(number, number_position)
                number_position = [60,730]
                screen.blit(number, number_position)
                number_position = [485,811]
                screen.blit(number, number_position)
            if 25 in s.holes:
                number_position = [381,510]
                screen.blit(number, number_position)
                number_position = [187,770]
                screen.blit(number, number_position)
                number_position = [529,890]
                screen.blit(number, number_position)

    if s.game.tilt.status == True:
        tilt_position = [10,650]
        screen.blit(tilt, tilt_position)

    if s.game.replays:
        digits = [int(d) for d in list(str(s.game.replays))]
        if len(digits) == 3:
            if digits[0] != 0:
                if digits[0] == 1:
                    r100_position = [68,346]
                    screen.blit(r100, r100_position)
                if digits[0] == 2:
                    r100_position = [26,355]
                    screen.blit(r200, r100_position)
                if digits[0] == 3:
                    r100_position = [6,388]
                    screen.blit(r300, r100_position)
                if digits[0] == 4:
                    r100_position = [6,427]
                    screen.blit(r400, r100_position)
                if digits[0] == 5:
                    r100_position = [7,465]
                    screen.blit(r500, r100_position)
                if digits[0] == 6:
                    r100_position = [9,501]
                    screen.blit(r600, r100_position)
                if digits[0] == 7:
                    r100_position = [10,538]
                    screen.blit(r700, r100_position)
                if digits[0] == 8:
                    r100_position = [10,575]
                    screen.blit(r800, r100_position)
                if digits[0] == 9:
                    r100_position = [10,613]
                    screen.blit(r900, r100_position)

            if digits[1] != 0:
                if digits[1] == 1:
                    r10_position = [624,350]
                    screen.blit(r10, r10_position)
                if digits[1] == 2:
                    r10_position = [582,350]
                    screen.blit(r20, r10_position)
                if digits[1] == 3:
                    r10_position = [540,352]
                    screen.blit(r30, r10_position)
                if digits[1] == 4:
                    r10_position = [496,352]
                    screen.blit(r40, r10_position)
                if digits[1] == 5:
                    r10_position = [454,351]
                    screen.blit(r50, r10_position)
                if digits[1] == 6:
                    r10_position = [235,348]
                    screen.blit(r60, r10_position)
                if digits[1] == 7:
                    r10_position = [196,348]
                    screen.blit(r70, r10_position)
                if digits[1] == 8:
                    r10_position = [154,347]
                    screen.blit(r80, r10_position)
                if digits[1] == 9:
                    r10_position = [113,346]
                    screen.blit(r90, r10_position)
            if digits[2] != 0:
                if digits[2] == 1:
                    r1_position = [682,656]
                    screen.blit(r1, r1_position)
                if digits[2] == 2:
                    r1_position = [682,618]
                    screen.blit(r2, r1_position)
                if digits[2] == 3:
                    r1_position = [684,580]
                    screen.blit(r3, r1_position)
                if digits[2] == 4:
                    r1_position = [684,544]
                    screen.blit(r4, r1_position)
                if digits[2] == 5:
                    r1_position = [685,508]
                    screen.blit(r5, r1_position)
                if digits[2] == 6:
                    r1_position = [685,470]
                    screen.blit(r6, r1_position)
                if digits[2] == 7:
                    r1_position = [688,430]
                    screen.blit(r7, r1_position)
                if digits[2] == 8:
                    r1_position = [688,393]
                    screen.blit(r8, r1_position)
                if digits[2] == 9:
                    r1_position = [668,358]
                    screen.blit(r9, r1_position)


        if len(digits) == 2:
            if digits[0] != 0:
                if digits[0] == 1:
                    r10_position = [624,350]
                    screen.blit(r10, r10_position)
                if digits[0] == 2:
                    r10_position = [582,350]
                    screen.blit(r20, r10_position)
                if digits[0] == 3:
                    r10_position = [540,352]
                    screen.blit(r30, r10_position)
                if digits[0] == 4:
                    r10_position = [496,352]
                    screen.blit(r40, r10_position)
                if digits[0] == 5:
                    r10_position = [454,351]
                    screen.blit(r50, r10_position)
                if digits[0] == 6:
                    r10_position = [235,348]
                    screen.blit(r60, r10_position)
                if digits[0] == 7:
                    r10_position = [196,348]
                    screen.blit(r70, r10_position)
                if digits[0] == 8:
                    r10_position = [154,347]
                    screen.blit(r80, r10_position)
                if digits[0] == 9:
                    r10_position = [113,346]
                    screen.blit(r90, r10_position)
            if digits[1] != 0:
                if digits[1] == 1:
                    r1_position = [682,656]
                    screen.blit(r1, r1_position)
                if digits[1] == 2:
                    r1_position = [682,618]
                    screen.blit(r2, r1_position)
                if digits[1] == 3:
                    r1_position = [684,580]
                    screen.blit(r3, r1_position)
                if digits[1] == 4:
                    r1_position = [684,544]
                    screen.blit(r4, r1_position)
                if digits[1] == 5:
                    r1_position = [685,508]
                    screen.blit(r5, r1_position)
                if digits[1] == 6:
                    r1_position = [685,470]
                    screen.blit(r6, r1_position)
                if digits[1] == 7:
                    r1_position = [688,430]
                    screen.blit(r7, r1_position)
                if digits[1] == 8:
                    r1_position = [688,393]
                    screen.blit(r8, r1_position)
                if digits[1] == 9:
                    r1_position = [668,358]
                    screen.blit(r9, r1_position)

        if len(digits) == 1:
            if digits[0] != 0:
                if digits[0] == 1:
                    r1_position = [682,656]
                    screen.blit(r1, r1_position)
                if digits[0] == 2:
                    r1_position = [682,618]
                    screen.blit(r2, r1_position)
                if digits[0] == 3:
                    r1_position = [684,580]
                    screen.blit(r3, r1_position)
                if digits[0] == 4:
                    r1_position = [684,544]
                    screen.blit(r4, r1_position)
                if digits[0] == 5:
                    r1_position = [685,508]
                    screen.blit(r5, r1_position)
                if digits[0] == 6:
                    r1_position = [685,470]
                    screen.blit(r6, r1_position)
                if digits[0] == 7:
                    r1_position = [688,430]
                    screen.blit(r7, r1_position)
                if digits[0] == 8:
                    r1_position = [688,393]
                    screen.blit(r8, r1_position)
                if digits[0] == 9:
                    r1_position = [668,358]
                    screen.blit(r9, r1_position)

    pygame.display.update()

def eb_animation(s):
    global screen
    balls_position = [287,725]
    screen.blit(balls_display, balls_position)
    pygame.display.update()
    if s == 0:
        position = [313,884]
        screen.blit(eball1_display, position)
        pygame.display.update()
    if s == 1:
        position = [350,872]
        screen.blit(eball2_display, position)
        pygame.display.update()
    if s == 2:
        position = [391,840]
        screen.blit(eball3_display, position)
        pygame.display.update()
