import pygame

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

card1 = pygame.image.load('bolero/assets/card1.png').convert_alpha()
card2 = pygame.image.load('bolero/assets/card2.png').convert_alpha()
card3 = pygame.image.load('bolero/assets/card3.png').convert_alpha()
balls5_display = pygame.image.load('bolero/assets/5_balls.png').convert_alpha()
balls6_display = pygame.image.load('bolero/assets/6_balls.png').convert_alpha()
balls7_display = pygame.image.load('bolero/assets/7_balls.png').convert_alpha()
balls8_display = pygame.image.load('bolero/assets/8_balls.png').convert_alpha()
number1 = pygame.image.load('bolero/assets/number1.png').convert_alpha()
number2 = pygame.image.load('bolero/assets/number2.png').convert_alpha()
number3 = pygame.image.load('bolero/assets/number3.png').convert_alpha()
tilt = pygame.image.load('bolero/assets/tilt.png').convert_alpha()
r100 = pygame.image.load('bolero/assets/100.png').convert_alpha()
r200 = pygame.image.load('bolero/assets/200.png').convert_alpha()
r300 = pygame.image.load('bolero/assets/300.png').convert_alpha()
r400 = pygame.image.load('bolero/assets/400.png').convert_alpha()
r10 = pygame.image.load('bolero/assets/10.png').convert_alpha()
r20 = pygame.image.load('bolero/assets/20.png').convert_alpha()
r30 = pygame.image.load('bolero/assets/30.png').convert_alpha()
r40 = pygame.image.load('bolero/assets/40.png').convert_alpha()
r50 = pygame.image.load('bolero/assets/50.png').convert_alpha()
r60 = pygame.image.load('bolero/assets/60.png').convert_alpha()
r70 = pygame.image.load('bolero/assets/70.png').convert_alpha()
r80 = pygame.image.load('bolero/assets/80.png').convert_alpha()
r90 = pygame.image.load('bolero/assets/90.png').convert_alpha()
r1 = pygame.image.load('bolero/assets/1.png').convert_alpha()
r2 = pygame.image.load('bolero/assets/2.png').convert_alpha()
r3 = pygame.image.load('bolero/assets/3.png').convert_alpha()
r4 = pygame.image.load('bolero/assets/4.png').convert_alpha()
r5 = pygame.image.load('bolero/assets/5.png').convert_alpha()
r6 = pygame.image.load('bolero/assets/6.png').convert_alpha()
r7 = pygame.image.load('bolero/assets/7.png').convert_alpha()
r8 = pygame.image.load('bolero/assets/8.png').convert_alpha()
r9 = pygame.image.load('bolero/assets/9.png').convert_alpha()
bg_menu = pygame.image.load('bolero/assets/bolero_menu.png')
bg_gi = pygame.image.load('bolero/assets/bolero_gi.png')
bg_off = pygame.image.load('bolero/assets/bolero_off.png')

def display(s, replays=0, menu=False):

    backglass_position = [0, 0]
    backglass = pygame.Surface(screen.get_size(), flags=pygame.SRCALPHA)
    backglass.fill((0, 0, 0))
    if menu == True:
        backglass = pygame.image.load('bolero/assets/bolero_menu.png')
        screen.blit(bg_menu, backglass_position)
    else:
        if (s.game.anti_cheat.status == True):
            screen.blit(bg_gi, backglass_position)
        else:
            screen.blit(bg_off, backglass_position)

    if s.game.selector.position >= 1:
        card1_position = [84,618]
        screen.blit(card1, card1_position)
    if s.game.selector.position >= 2:
        card2_position = [296,584]
        screen.blit(card2, card2_position)
    if s.game.selector.position >= 3:
        card3_position = [515,620]
        screen.blit(card3, card3_position)
 
    if s.game.selector.position > 0:
        if s.game.selector.position <= 3:
            balls_position = [90,806]
            screen.blit(balls5_display, balls_position)
        elif s.game.selector.position == 4:
            balls_position = [90,871]
            screen.blit(balls6_display, balls_position)
        elif s.game.selector.position == 5:
            balls_position = [521,805]
            screen.blit(balls7_display, balls_position)
        elif s.game.selector.position == 6:
            balls_position = [521,870]
            screen.blit(balls8_display, balls_position)

    if s.game.tilt.status == False:
        if s.holes:
            if 1 in s.holes:
                number_position = [56,351]
                screen.blit(number1, number_position)
                number_position = [390,894]
                screen.blit(number2, number_position)
                number_position = [528,462]
                screen.blit(number3, number_position)
            if 2 in s.holes:
                number_position = [244,522]
                screen.blit(number1, number_position)
                number_position = [442,743]
                screen.blit(number2, number_position)
                number_position = [587,505]
                screen.blit(number3, number_position)
            if 3 in s.holes:
                number_position = [146,461]
                screen.blit(number1, number_position)
                number_position = [392,693]
                screen.blit(number2, number_position)
                number_position = [643,548]
                screen.blit(number3, number_position)
            if 4 in s.holes:
                number_position = [205,418]
                screen.blit(number1, number_position)
                number_position = [234,845]
                screen.blit(number2, number_position)
                number_position = [567,358]
                screen.blit(number3, number_position)
            if 5 in s.holes:
                number_position = [30,549]
                screen.blit(number1, number_position)
                number_position = [339,795]
                screen.blit(number2, number_position)
                number_position = [490,566]
                screen.blit(number3, number_position)
            if 6 in s.holes:
                number_position = [264,375]
                screen.blit(number1, number_position)
                number_position = [286,845]
                screen.blit(number2, number_position)
                number_position = [523,413]
                screen.blit(number3, number_position)
            if 7 in s.holes:
                number_position = [50,400]
                screen.blit(number1, number_position)
                number_position = [236,694]
                screen.blit(number2, number_position)
                number_position = [580,456]
                screen.blit(number3, number_position)
            if 8 in s.holes:
                number_position = [108,357]
                screen.blit(number1, number_position)
                number_position = [286,895]
                screen.blit(number2, number_position)
                number_position = [426,474]
                screen.blit(number3, number_position)
            if 9 in s.holes:
                number_position = [193,516]
                screen.blit(number1, number_position)
                number_position = [340,694]
                screen.blit(number2, number_position)
                number_position = [465,370]
                screen.blit(number3, number_position)
            if 10 in s.holes:
                number_position = [251,473]
                screen.blit(number1, number_position)
                number_position = [390,795]
                screen.blit(number2, number_position)
                number_position = [618,352]
                screen.blit(number3, number_position)
            if 11 in s.holes:
                number_position = [140,511]
                screen.blit(number1, number_position)
                number_position = [234,895]
                screen.blit(number2, number_position)
                number_position = [535,511]
                screen.blit(number3, number_position)
            if 12 in s.holes:
                number_position = [239,572]
                screen.blit(number1, number_position)
                number_position = [338,845]
                screen.blit(number2, number_position)
                number_position = [420,425]
                screen.blit(number3, number_position)
            if 13 in s.holes:
                number_position = [44,450]
                screen.blit(number1, number_position)
                number_position = [288,694]
                screen.blit(number2, number_position)
                number_position = [637,500]
                screen.blit(number3, number_position)
            if 14 in s.holes:
                number_position = [89,505]
                screen.blit(number1, number_position)
                number_position = [339,744]
                screen.blit(number2, number_position)
                number_position = [438,573]
                screen.blit(number3, number_position)
            if 15 in s.holes:
                number_position = [200,467]
                screen.blit(number1, number_position)
                number_position = [441,894]
                screen.blit(number2, number_position)
                number_position = [484,517]
                screen.blit(number3, number_position)
            if 16 in s.holes:
                number_position = [135,561]
                screen.blit(number1, number_position)
                number_position = [392,744]
                screen.blit(number2, number_position)
                number_position = [624,401]
                screen.blit(number3, number_position)
            if 17 in s.holes:
                number_position = [154,412]
                screen.blit(number1, number_position)
                number_position = [338,895]
                screen.blit(number2, number_position)
                number_position = [414,374]
                screen.blit(number3, number_position)
            if 18 in s.holes:
                number_position = [212,368]
                screen.blit(number1, number_position)
                number_position = [442,795]
                screen.blit(number2, number_position)
                number_position = [541,560]
                screen.blit(number3, number_position)
            if 19 in s.holes:
                number_position = [186,566]
                screen.blit(number1, number_position)
                number_position = [235,745]
                screen.blit(number2, number_position)
                number_position = [478,468]
                screen.blit(number3, number_position)
            if 20 in s.holes:
                number_position = [95,455]
                screen.blit(number1, number_position)
                number_position = [444,694]
                screen.blit(number2, number_position)
                number_position = [517,364]
                screen.blit(number3, number_position)
            if 21 in s.holes:
                number_position = [38,499]
                screen.blit(number1, number_position)
                number_position = [235,795]
                screen.blit(number2, number_position)
                number_position = [574,407]
                screen.blit(number3, number_position)
            if 22 in s.holes:
                number_position = [161,363]
                screen.blit(number1, number_position)
                number_position = [390,844]
                screen.blit(number2, number_position)
                number_position = [432,523]
                screen.blit(number3, number_position)
            if 23 in s.holes:
                number_position = [257,423]
                screen.blit(number1, number_position)
                number_position = [287,745]
                screen.blit(number2, number_position)
                number_position = [472,419]
                screen.blit(number3, number_position)
            if 24 in s.holes:
                number_position = [102,406]
                screen.blit(number1, number_position)
                number_position = [442,844]
                screen.blit(number2, number_position)
                number_position = [631,451]
                screen.blit(number3, number_position)
            if 25 in s.holes:
                number_position = [83,555]
                screen.blit(number1, number_position)
                number_position = [287,795]
                screen.blit(number2, number_position)
                number_position = [592,555]
                screen.blit(number3, number_position)

    if s.game.tilt.status == True:
        tilt_position = [355,470]
        screen.blit(tilt, tilt_position)

    if s.game.replays:
        digits = [int(d) for d in list(str(s.game.replays))]
        if len(digits) == 3:
            if digits[0] != 0:
                if digits[0] == 1:
                    r100_position = [20,848]
                    screen.blit(r100, r100_position)
                if digits[0] == 2:
                    r100_position = [19,794]
                    screen.blit(r200, r100_position)
                if digits[0] == 3:
                    r100_position = [19,739]
                    screen.blit(r300, r100_position)
                if digits[0] == 4:
                    r100_position = [19,685]
                    screen.blit(r400, r100_position)
            if digits[1] != 0:
                if digits[1] == 1:
                    r10_position = [427,979]
                    screen.blit(r10, r10_position)
                if digits[1] == 2:
                    r10_position = [373,977]
                    screen.blit(r20, r10_position)
                if digits[1] == 3:
                    r10_position = [316,978]
                    screen.blit(r30, r10_position)
                if digits[1] == 4:
                    r10_position = [259,980]
                    screen.blit(r40, r10_position)
                if digits[1] == 5:
                    r10_position = [205,980]
                    screen.blit(r50, r10_position)
                if digits[1] == 6:
                    r10_position = [150,980]
                    screen.blit(r60, r10_position)
                if digits[1] == 7:
                    r10_position = [91,977]
                    screen.blit(r70, r10_position)
                if digits[1] == 8:
                    r10_position = [44,951]
                    screen.blit(r80, r10_position)
                if digits[1] == 9:
                    r10_position = [22,901]
                    screen.blit(r90, r10_position)
            if digits[2] != 0:
                if digits[2] == 1:
                    r1_position = [669,679]
                    screen.blit(r1, r1_position)
                if digits[2] == 2:
                    r1_position = [669,735]
                    screen.blit(r2, r1_position)
                if digits[2] == 3:
                    r1_position = [669,787]
                    screen.blit(r3, r1_position)
                if digits[2] == 4:
                    r1_position = [669,840]
                    screen.blit(r4, r1_position)
                if digits[2] == 5:
                    r1_position = [669,895]
                    screen.blit(r5, r1_position)
                if digits[2] == 6:
                    r1_position = [649,945]
                    screen.blit(r6, r1_position)
                if digits[2] == 7:
                    r1_position = [600,974]
                    screen.blit(r7, r1_position)
                if digits[2] == 8:
                    r1_position = [545,979]
                    screen.blit(r8, r1_position)
                if digits[2] == 9:
                    r1_position = [490,980]
                    screen.blit(r9, r1_position)


        if len(digits) == 2:
            if digits[0] != 0:
                if digits[0] == 1:
                    r10_position = [427,979]
                    screen.blit(r10, r10_position)
                if digits[0] == 2:
                    r10_position = [373,977]
                    screen.blit(r20, r10_position)
                if digits[0] == 3:
                    r10_position = [316,978]
                    screen.blit(r30, r10_position)
                if digits[0] == 4:
                    r10_position = [259,980]
                    screen.blit(r40, r10_position)
                if digits[0] == 5:
                    r10_position = [205,980]
                    screen.blit(r50, r10_position)
                if digits[0] == 6:
                    r10_position = [150,980]
                    screen.blit(r60, r10_position)
                if digits[0] == 7:
                    r10_position = [91,977]
                    screen.blit(r70, r10_position)
                if digits[0] == 8:
                    r10_position = [44,951]
                    screen.blit(r80, r10_position)
                if digits[0] == 9:
                    r10_position = [22,901]
                    screen.blit(r90, r10_position)
            if digits[1] != 0:
                if digits[1] == 1:
                    r1_position = [669,679]
                    screen.blit(r1, r1_position)
                if digits[1] == 2:
                    r1_position = [669,735]
                    screen.blit(r2, r1_position)
                if digits[1] == 3:
                    r1_position = [669,787]
                    screen.blit(r3, r1_position)
                if digits[1] == 4:
                    r1_position = [669,840]
                    screen.blit(r4, r1_position)
                if digits[1] == 5:
                    r1_position = [669,895]
                    screen.blit(r5, r1_position)
                if digits[1] == 6:
                    r1_position = [649,945]
                    screen.blit(r6, r1_position)
                if digits[1] == 7:
                    r1_position = [600,974]
                    screen.blit(r7, r1_position)
                if digits[1] == 8:
                    r1_position = [545,979]
                    screen.blit(r8, r1_position)
                if digits[1] == 9:
                    r1_position = [490,980]
                    screen.blit(r9, r1_position)

        if len(digits) == 1:
            if digits[0] != 0:
                if digits[0] == 1:
                    r1_position = [669,679]
                    screen.blit(r1, r1_position)
                if digits[0] == 2:
                    r1_position = [669,735]
                    screen.blit(r2, r1_position)
                if digits[0] == 3:
                    r1_position = [669,787]
                    screen.blit(r3, r1_position)
                if digits[0] == 4:
                    r1_position = [669,840]
                    screen.blit(r4, r1_position)
                if digits[0] == 5:
                    r1_position = [669,895]
                    screen.blit(r5, r1_position)
                if digits[0] == 6:
                    r1_position = [649,945]
                    screen.blit(r6, r1_position)
                if digits[0] == 7:
                    r1_position = [600,974]
                    screen.blit(r7, r1_position)
                if digits[0] == 8:
                    r1_position = [545,979]
                    screen.blit(r8, r1_position)
                if digits[0] == 9:
                    r1_position = [490,980]
                    screen.blit(r9, r1_position)

    pygame.display.update()
