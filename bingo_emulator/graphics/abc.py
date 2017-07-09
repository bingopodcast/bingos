import pygame

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

card1_display = pygame.image.load('abc/assets/card1.png').convert_alpha()
card2_display = pygame.image.load('abc/assets/card2.png').convert_alpha()
card3_display = pygame.image.load('abc/assets/card3.png').convert_alpha()
number1 = pygame.image.load('abc/assets/number1.png').convert_alpha()
number2 = pygame.image.load('abc/assets/number2.png').convert_alpha()
number3 = pygame.image.load('abc/assets/number3.png').convert_alpha()
r100 = pygame.image.load('abc/assets/100.png').convert_alpha()
r200 = pygame.image.load('abc/assets/200.png').convert_alpha()
r300 = pygame.image.load('abc/assets/300.png').convert_alpha()
r400 = pygame.image.load('abc/assets/400.png').convert_alpha()
r10 = pygame.image.load('abc/assets/10.png').convert_alpha()
r20 = pygame.image.load('abc/assets/20.png').convert_alpha()
r30 = pygame.image.load('abc/assets/30.png').convert_alpha()
r40 = pygame.image.load('abc/assets/40.png').convert_alpha()
r50 = pygame.image.load('abc/assets/50.png').convert_alpha()
r60 = pygame.image.load('abc/assets/60.png').convert_alpha()
r70 = pygame.image.load('abc/assets/70.png').convert_alpha()
r80 = pygame.image.load('abc/assets/80.png').convert_alpha()
r90 = pygame.image.load('abc/assets/90.png').convert_alpha()
r1 = pygame.image.load('abc/assets/1.png').convert_alpha()
r2 = pygame.image.load('abc/assets/2.png').convert_alpha()
r3 = pygame.image.load('abc/assets/3.png').convert_alpha()
r4 = pygame.image.load('abc/assets/4.png').convert_alpha()
r5 = pygame.image.load('abc/assets/5.png').convert_alpha()
r6 = pygame.image.load('abc/assets/6.png').convert_alpha()
r7 = pygame.image.load('abc/assets/7.png').convert_alpha()
r8 = pygame.image.load('abc/assets/8.png').convert_alpha()
r9 = pygame.image.load('abc/assets/9.png').convert_alpha()
tilt = pygame.image.load('abc/assets/tilt.png').convert_alpha()

def display(s, replays=0, menu=False):

    backglass_position = [0, 0]
    backglass = pygame.Surface(screen.get_size(), flags=pygame.SRCALPHA)
    backglass.fill((0, 0, 0))
    if menu == True:
        backglass = pygame.image.load('abc/assets/abc_menu.png')
    else:
        if (s.game.anti_cheat.status == True):
            backglass = pygame.image.load('abc/assets/abc_gi.png')
        else:
            backglass = pygame.image.load('abc/assets/abc_off.png')
    backglass = pygame.transform.scale(backglass, (720, 1280))
    
    screen.blit(backglass, backglass_position)

    if s.game.selector.position >= 1:
        card1_position = [85,611]
        screen.blit(card1_display, card1_position)
    if s.game.selector.position >= 2:
        card2_position = [298,581]
        screen.blit(card2_display, card2_position)
    if s.game.selector.position >= 3:
        card3_position = [518,616]
        screen.blit(card3_display, card3_position)

    if s.game.tilt.status == False:
        if s.holes:
            if 1 in s.holes:
                number_position = [59,327]
                screen.blit(number1, number_position)
                number_position = [388,912]
                screen.blit(number2, number_position)
                number_position = [531,450]
                screen.blit(number3, number_position)
            if 2 in s.holes:
                number_position = [245,510]
                screen.blit(number1, number_position)
                number_position = [443,748]
                screen.blit(number2, number_position)
                number_position = [587,495]
                screen.blit(number3, number_position)
            if 3 in s.holes:
                number_position = [149,444]
                screen.blit(number1, number_position)
                number_position = [391,694]
                screen.blit(number2, number_position)
                number_position = [644,541]
                screen.blit(number3, number_position)
            if 4 in s.holes:
                number_position = [206,400]
                screen.blit(number1, number_position)
                number_position = [231,855]
                screen.blit(number2, number_position)
                number_position = [570,340]
                screen.blit(number3, number_position)
            if 5 in s.holes:
                number_position = [31,535]
                screen.blit(number1, number_position)
                number_position = [337,802]
                screen.blit(number2, number_position)
                number_position = [491,560]
                screen.blit(number3, number_position)
            if 6 in s.holes:
                number_position = [264,355]
                screen.blit(number1, number_position)
                number_position = [283,855]
                screen.blit(number2, number_position)
                number_position = [525,398]
                screen.blit(number3, number_position)
            if 7 in s.holes:
                number_position = [52,380]
                screen.blit(number1, number_position)
                number_position = [234,693]
                screen.blit(number2, number_position)
                number_position = [581,443]
                screen.blit(number3, number_position)
            if 8 in s.holes:
                number_position = [110,334]
                screen.blit(number1, number_position)
                number_position = [284,910]
                screen.blit(number2, number_position)
                number_position = [427,460]
                screen.blit(number3, number_position)
            if 9 in s.holes:
                number_position = [193,503]
                screen.blit(number1, number_position)
                number_position = [340,694]
                screen.blit(number2, number_position)
                number_position = [467,350]
                screen.blit(number3, number_position)
            if 10 in s.holes:
                number_position = [250,459]
                screen.blit(number1, number_position)
                number_position = [390,802]
                screen.blit(number2, number_position)
                number_position = [620,335]
                screen.blit(number3, number_position)
            if 11 in s.holes:
                number_position = [142,496]
                screen.blit(number1, number_position)
                number_position = [231,910]
                screen.blit(number2, number_position)
                number_position = [536,501]
                screen.blit(number3, number_position)
            if 12 in s.holes:
                number_position = [238,561]
                screen.blit(number1, number_position)
                number_position = [338,855]
                screen.blit(number2, number_position)
                number_position = [421,408]
                screen.blit(number3, number_position)
            if 13 in s.holes:
                number_position = [45,433]
                screen.blit(number1, number_position)
                number_position = [287,694]
                screen.blit(number2, number_position)
                number_position = [639,490]
                screen.blit(number3, number_position)
            if 14 in s.holes:
                number_position = [90,490]
                screen.blit(number1, number_position)
                number_position = [339,746]
                screen.blit(number2, number_position)
                number_position = [439,567]
                screen.blit(number3, number_position)
            if 15 in s.holes:
                number_position = [199,453]
                screen.blit(number1, number_position)
                number_position = [441,912]
                screen.blit(number2, number_position)
                number_position = [485,507]
                screen.blit(number3, number_position)
            if 16 in s.holes:
                number_position = [135,548]
                screen.blit(number1, number_position)
                number_position = [391,748]
                screen.blit(number2, number_position)
                number_position = [626,386]
                screen.blit(number3, number_position)
            if 17 in s.holes:
                number_position = [155,393]
                screen.blit(number1, number_position)
                number_position = [337,910]
                screen.blit(number2, number_position)
                number_position = [415,356]
                screen.blit(number3, number_position)
            if 18 in s.holes:
                number_position = [212,348]
                screen.blit(number1, number_position)
                number_position = [443,802]
                screen.blit(number2, number_position)
                number_position = [542,553]
                screen.blit(number3, number_position)
            if 19 in s.holes:
                number_position = [186,555]
                screen.blit(number1, number_position)
                number_position = [234,746]
                screen.blit(number2, number_position)
                number_position = [479,455]
                screen.blit(number3, number_position)
            if 20 in s.holes:
                number_position = [97,438]
                screen.blit(number1, number_position)
                number_position = [443,694]
                screen.blit(number2, number_position)
                number_position = [519,345]
                screen.blit(number3, number_position)
            if 21 in s.holes:
                number_position = [38,483]
                screen.blit(number1, number_position)
                number_position = [233,800]
                screen.blit(number2, number_position)
                number_position = [575,392]
                screen.blit(number3, number_position)
            if 22 in s.holes:
                number_position = [161,340]
                screen.blit(number1, number_position)
                number_position = [390,856]
                screen.blit(number2, number_position)
                number_position = [432,514]
                screen.blit(number3, number_position)
            if 23 in s.holes:
                number_position = [259,406]
                screen.blit(number1, number_position)
                number_position = [286,746]
                screen.blit(number2, number_position)
                number_position = [473,404]
                screen.blit(number3, number_position)
            if 24 in s.holes:
                number_position = [103,387]
                screen.blit(number1, number_position)
                number_position = [442,856]
                screen.blit(number2, number_position)
                number_position = [632,438]
                screen.blit(number3, number_position)
            if 25 in s.holes:
                number_position = [84,542]
                screen.blit(number1, number_position)
                number_position = [285,800]
                screen.blit(number2, number_position)
                number_position = [593,547]
                screen.blit(number3, number_position)

    if s.game.tilt.status == True:
        tilt_position = [348,474]
        screen.blit(tilt, tilt_position)

    if s.game.replays:
        digits = [int(d) for d in list(str(s.game.replays))]
        if len(digits) == 3:
            if digits[0] != 0:
                if digits[0] == 1:
                    r100_position = [14,856]
                    screen.blit(r100, r100_position)
                if digits[0] == 2:
                    r100_position = [15,797]
                    screen.blit(r200, r100_position)
                if digits[0] == 3:
                    r100_position = [17,741]
                    screen.blit(r300, r100_position)
                if digits[0] == 4:
                    r100_position = [17,682]
                    screen.blit(r400, r100_position)
            if digits[1] != 0:
                if digits[1] == 1:
                    r10_position = [427,999]
                    screen.blit(r10, r10_position)
                if digits[1] == 2:
                    r10_position = [373,999]
                    screen.blit(r20, r10_position)
                if digits[1] == 3:
                    r10_position = [314,999]
                    screen.blit(r30, r10_position)
                if digits[1] == 4:
                    r10_position = [254,999]
                    screen.blit(r40, r10_position)
                if digits[1] == 5:
                    r10_position = [200,999]
                    screen.blit(r50, r10_position)
                if digits[1] == 6:
                    r10_position = [142,999]
                    screen.blit(r60, r10_position)
                if digits[1] == 7:
                    r10_position = [85,996]
                    screen.blit(r70, r10_position)
                if digits[1] == 8:
                    r10_position = [38,966]
                    screen.blit(r80, r10_position)
                if digits[1] == 9:
                    r10_position = [18,910]
                    screen.blit(r90, r10_position)
            if digits[2] != 0:
                if digits[2] == 1:
                    r1_position = [673,677]
                    screen.blit(r1, r1_position)
                if digits[2] == 2:
                    r1_position = [673,685]
                    screen.blit(r2, r1_position)
                if digits[2] == 3:
                    r1_position = [675,744]
                    screen.blit(r3, r1_position)
                if digits[2] == 4:
                    r1_position = [673,799]
                    screen.blit(r4, r1_position)
                if digits[2] == 5:
                    r1_position = [672,858]
                    screen.blit(r5, r1_position)
                if digits[2] == 6:
                    r1_position = [670,912]
                    screen.blit(r6, r1_position)
                if digits[2] == 7:
                    r1_position = [652,969]
                    screen.blit(r7, r1_position)
                if digits[2] == 8:
                    r1_position = [601,999]
                    screen.blit(r8, r1_position)
                if digits[2] == 9:
                    r1_position = [547,999]
                    screen.blit(r9, r1_position)


        if len(digits) == 2:
            if digits[0] != 0:
                if digits[0] == 1:
                    r10_position = [427,999]
                    screen.blit(r10, r10_position)
                if digits[0] == 2:
                    r10_position = [373,999]
                    screen.blit(r20, r10_position)
                if digits[0] == 3:
                    r10_position = [314,999]
                    screen.blit(r30, r10_position)
                if digits[0] == 4:
                    r10_position = [254,999]
                    screen.blit(r40, r10_position)
                if digits[0] == 5:
                    r10_position = [200,999]
                    screen.blit(r50, r10_position)
                if digits[0] == 6:
                    r10_position = [142,999]
                    screen.blit(r60, r10_position)
                if digits[0] == 7:
                    r10_position = [85,996]
                    screen.blit(r70, r10_position)
                if digits[0] == 8:
                    r10_position = [38,966]
                    screen.blit(r80, r10_position)
                if digits[0] == 9:
                    r10_position = [18,910]
                    screen.blit(r90, r10_position)
            if digits[1] != 0:
                if digits[1] == 1:
                    r1_position = [673,677]
                    screen.blit(r1, r1_position)
                if digits[1] == 2:
                    r1_position = [673,685]
                    screen.blit(r2, r1_position)
                if digits[1] == 3:
                    r1_position = [675,744]
                    screen.blit(r3, r1_position)
                if digits[1] == 4:
                    r1_position = [673,799]
                    screen.blit(r4, r1_position)
                if digits[1] == 5:
                    r1_position = [672,858]
                    screen.blit(r5, r1_position)
                if digits[1] == 6:
                    r1_position = [670,912]
                    screen.blit(r6, r1_position)
                if digits[1] == 7:
                    r1_position = [652,969]
                    screen.blit(r7, r1_position)
                if digits[1] == 8:
                    r1_position = [601,999]
                    screen.blit(r8, r1_position)
                if digits[1] == 9:
                    r1_position = [547,999]
                    screen.blit(r9, r1_position)

        if len(digits) == 1:
            if digits[0] != 0:
                if digits[0] == 1:
                    r1_position = [673,677]
                    screen.blit(r1, r1_position)
                if digits[0] == 2:
                    r1_position = [673,685]
                    screen.blit(r2, r1_position)
                if digits[0] == 3:
                    r1_position = [675,744]
                    screen.blit(r3, r1_position)
                if digits[0] == 4:
                    r1_position = [673,799]
                    screen.blit(r4, r1_position)
                if digits[0] == 5:
                    r1_position = [672,858]
                    screen.blit(r5, r1_position)
                if digits[0] == 6:
                    r1_position = [670,912]
                    screen.blit(r6, r1_position)
                if digits[0] == 7:
                    r1_position = [652,969]
                    screen.blit(r7, r1_position)
                if digits[0] == 8:
                    r1_position = [601,999]
                    screen.blit(r8, r1_position)
                if digits[0] == 9:
                    r1_position = [547,999]
                    screen.blit(r9, r1_position)

    pygame.display.update()

    
