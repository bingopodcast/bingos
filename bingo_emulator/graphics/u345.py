import pygame

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

number1 = pygame.image.load('u345/assets/number1.png').convert_alpha()
number2 = pygame.image.load('u345/assets/number2.png').convert_alpha()
number3 = pygame.image.load('u345/assets/number3.png').convert_alpha()
r100 = pygame.image.load('u345/assets/100.png').convert_alpha()
r200 = pygame.image.load('u345/assets/200.png').convert_alpha()
r300 = pygame.image.load('u345/assets/300.png').convert_alpha()
r400 = pygame.image.load('u345/assets/400.png').convert_alpha()
r10 = pygame.image.load('u345/assets/10.png').convert_alpha()
r20 = pygame.image.load('u345/assets/20.png').convert_alpha()
r30 = pygame.image.load('u345/assets/30.png').convert_alpha()
r40 = pygame.image.load('u345/assets/40.png').convert_alpha()
r50 = pygame.image.load('u345/assets/50.png').convert_alpha()
r60 = pygame.image.load('u345/assets/60.png').convert_alpha()
r70 = pygame.image.load('u345/assets/70.png').convert_alpha()
r80 = pygame.image.load('u345/assets/80.png').convert_alpha()
r90 = pygame.image.load('u345/assets/90.png').convert_alpha()
r1 = pygame.image.load('u345/assets/1.png').convert_alpha()
r2 = pygame.image.load('u345/assets/2.png').convert_alpha()
r3 = pygame.image.load('u345/assets/3.png').convert_alpha()
r4 = pygame.image.load('u345/assets/4.png').convert_alpha()
r5 = pygame.image.load('u345/assets/5.png').convert_alpha()
r6 = pygame.image.load('u345/assets/6.png').convert_alpha()
r7 = pygame.image.load('u345/assets/7.png').convert_alpha()
r8 = pygame.image.load('u345/assets/8.png').convert_alpha()
r9 = pygame.image.load('u345/assets/9.png').convert_alpha()
tilt = pygame.image.load('u345/assets/tilt.png').convert_alpha()

def display(s, replays=0, menu=False):

    backglass_position = [0, 0]
    backglass = pygame.Surface(screen.get_size(), flags=pygame.SRCALPHA)
    backglass.fill((0, 0, 0))
    if menu == True:
        backglass = pygame.image.load('u345/assets/u345_menu.png')
    else:
        if (s.game.anti_cheat.status == True):
            backglass = pygame.image.load('u345/assets/u345_gi.png')
        else:
            backglass = pygame.image.load('u345/assets/u345_off.png')
    backglass = pygame.transform.scale(backglass, (720, 1280))
    
    screen.blit(backglass, backglass_position)

    if s.game.tilt.status == False:
        if s.holes:
            if 1 in s.holes:
                number_position = [48,320]
                screen.blit(number1, number_position)
                number_position = [531,450]
                screen.blit(number3, number_position)
            if 2 in s.holes:
                number_position = [235,514]
                screen.blit(number1, number_position)
                number_position = [587,495]
                screen.blit(number3, number_position)
            if 3 in s.holes:
                number_position = [142,446]
                screen.blit(number1, number_position)
                number_position = [644,541]
                screen.blit(number3, number_position)
            if 4 in s.holes:
                number_position = [200,400]
                screen.blit(number1, number_position)
                number_position = [568,330]
                screen.blit(number3, number_position)
            if 5 in s.holes:
                number_position = [24,540]
                screen.blit(number1, number_position)
                number_position = [491,560]
                screen.blit(number3, number_position)
            if 6 in s.holes:
                number_position = [258,350]
                screen.blit(number1, number_position)
                number_position = [525,398]
                screen.blit(number3, number_position)
            if 7 in s.holes:
                number_position = [42,380]
                screen.blit(number1, number_position)
                number_position = [581,443]
                screen.blit(number3, number_position)
            if 8 in s.holes:
                number_position = [102,330]
                screen.blit(number1, number_position)
                number_position = [427,460]
                screen.blit(number3, number_position)
            if 9 in s.holes:
                number_position = [188,507]
                screen.blit(number1, number_position)
                number_position = [464,344]
                screen.blit(number3, number_position)
            if 10 in s.holes:
                number_position = [247,461]
                screen.blit(number1, number_position)
                number_position = [616,325]
                screen.blit(number3, number_position)
            if 11 in s.holes:
                number_position = [136,499]
                screen.blit(number1, number_position)
                number_position = [536,501]
                screen.blit(number3, number_position)
            if 12 in s.holes:
                number_position = [233,569]
                screen.blit(number1, number_position)
                number_position = [421,408]
                screen.blit(number3, number_position)
            if 13 in s.holes:
                number_position = [38,433]
                screen.blit(number1, number_position)
                number_position = [639,490]
                screen.blit(number3, number_position)
            if 14 in s.holes:
                number_position = [85,495]
                screen.blit(number1, number_position)
                number_position = [439,567]
                screen.blit(number3, number_position)
            if 15 in s.holes:
                number_position = [194,453]
                screen.blit(number1, number_position)
                number_position = [485,507]
                screen.blit(number3, number_position)
            if 16 in s.holes:
                number_position = [130,554]
                screen.blit(number1, number_position)
                number_position = [626,386]
                screen.blit(number3, number_position)
            if 17 in s.holes:
                number_position = [146,393]
                screen.blit(number1, number_position)
                number_position = [412,353]
                screen.blit(number3, number_position)
            if 18 in s.holes:
                number_position = [206,344]
                screen.blit(number1, number_position)
                number_position = [542,553]
                screen.blit(number3, number_position)
            if 19 in s.holes:
                number_position = [181,562]
                screen.blit(number1, number_position)
                number_position = [479,455]
                screen.blit(number3, number_position)
            if 20 in s.holes:
                number_position = [90,438]
                screen.blit(number1, number_position)
                number_position = [514,338]
                screen.blit(number3, number_position)
            if 21 in s.holes:
                number_position = [32,487]
                screen.blit(number1, number_position)
                number_position = [575,392]
                screen.blit(number3, number_position)
            if 22 in s.holes:
                number_position = [155,336]
                screen.blit(number1, number_position)
                number_position = [432,514]
                screen.blit(number3, number_position)
            if 23 in s.holes:
                number_position = [252,407]
                screen.blit(number1, number_position)
                number_position = [473,404]
                screen.blit(number3, number_position)
            if 24 in s.holes:
                number_position = [94,387]
                screen.blit(number1, number_position)
                number_position = [632,438]
                screen.blit(number3, number_position)
            if 25 in s.holes:
                number_position = [77,548]
                screen.blit(number1, number_position)
                number_position = [593,550]
                screen.blit(number3, number_position)

    if s.game.tilt.status == True:
        tilt_position = [355,360]
        screen.blit(tilt, tilt_position)

    if s.game.replays:
        digits = [int(d) for d in list(str(s.game.replays))]
        if len(digits) == 3:
            if digits[0] != 0:
                if digits[0] == 1:
                    r100_position = [14,856]
                    screen.blit(r100, r100_position)
                if digits[0] == 2:
                    r100_position = [16,797]
                    screen.blit(r200, r100_position)
                if digits[0] == 3:
                    r100_position = [17,741]
                    screen.blit(r300, r100_position)
                if digits[0] == 4:
                    r100_position = [17,682]
                    screen.blit(r400, r100_position)
            if digits[1] != 0:
                if digits[1] == 1:
                    r10_position = [427,1008]
                    screen.blit(r10, r10_position)
                if digits[1] == 2:
                    r10_position = [373,1005]
                    screen.blit(r20, r10_position)
                if digits[1] == 3:
                    r10_position = [314,1007]
                    screen.blit(r30, r10_position)
                if digits[1] == 4:
                    r10_position = [254,1007]
                    screen.blit(r40, r10_position)
                if digits[1] == 5:
                    r10_position = [200,1007]
                    screen.blit(r50, r10_position)
                if digits[1] == 6:
                    r10_position = [142,1007]
                    screen.blit(r60, r10_position)
                if digits[1] == 7:
                    r10_position = [85,1005]
                    screen.blit(r70, r10_position)
                if digits[1] == 8:
                    r10_position = [38,972]
                    screen.blit(r80, r10_position)
                if digits[1] == 9:
                    r10_position = [18,916]
                    screen.blit(r90, r10_position)
            if digits[2] != 0:
                if digits[2] == 1:
                    r1_position = [673,677]
                    screen.blit(r1, r1_position)
                if digits[2] == 2:
                    r1_position = [672,738]
                    screen.blit(r2, r1_position)
                if digits[2] == 3:
                    r1_position = [674,797]
                    screen.blit(r3, r1_position)
                if digits[2] == 4:
                    r1_position = [674,855]
                    screen.blit(r4, r1_position)
                if digits[2] == 5:
                    r1_position = [675,915]
                    screen.blit(r5, r1_position)
                if digits[2] == 6:
                    r1_position = [657,972]
                    screen.blit(r6, r1_position)
                if digits[2] == 7:
                    r1_position = [609,1004]
                    screen.blit(r7, r1_position)
                if digits[2] == 8:
                    r1_position = [552,1005]
                    screen.blit(r8, r1_position)
                if digits[2] == 9:
                    r1_position = [496,1008]
                    screen.blit(r9, r1_position)


        if len(digits) == 2:
            if digits[0] != 0:
                if digits[0] == 1:
                    r10_position = [427,1008]
                    screen.blit(r10, r10_position)
                if digits[0] == 2:
                    r10_position = [373,1005]
                    screen.blit(r20, r10_position)
                if digits[0] == 3:
                    r10_position = [314,1007]
                    screen.blit(r30, r10_position)
                if digits[0] == 4:
                    r10_position = [254,1007]
                    screen.blit(r40, r10_position)
                if digits[0] == 5:
                    r10_position = [200,1007]
                    screen.blit(r50, r10_position)
                if digits[0] == 6:
                    r10_position = [142,1007]
                    screen.blit(r60, r10_position)
                if digits[0] == 7:
                    r10_position = [85,1005]
                    screen.blit(r70, r10_position)
                if digits[0] == 8:
                    r10_position = [38,972]
                    screen.blit(r80, r10_position)
                if digits[0] == 9:
                    r10_position = [18,916]
                    screen.blit(r90, r10_position)
            if digits[1] != 0:
                if digits[1] == 1:
                    r1_position = [673,677]
                    screen.blit(r1, r1_position)
                if digits[1] == 2:
                    r1_position = [672,738]
                    screen.blit(r2, r1_position)
                if digits[1] == 3:
                    r1_position = [674,797]
                    screen.blit(r3, r1_position)
                if digits[1] == 4:
                    r1_position = [674,855]
                    screen.blit(r4, r1_position)
                if digits[1] == 5:
                    r1_position = [675,915]
                    screen.blit(r5, r1_position)
                if digits[1] == 6:
                    r1_position = [657,972]
                    screen.blit(r6, r1_position)
                if digits[1] == 7:
                    r1_position = [609,1004]
                    screen.blit(r7, r1_position)
                if digits[1] == 8:
                    r1_position = [552,1005]
                    screen.blit(r8, r1_position)
                if digits[1] == 9:
                    r1_position = [496,1008]
                    screen.blit(r9, r1_position)

        if len(digits) == 1:
            if digits[0] != 0:
                if digits[0] == 1:
                    r1_position = [673,677]
                    screen.blit(r1, r1_position)
                if digits[0] == 2:
                    r1_position = [672,738]
                    screen.blit(r2, r1_position)
                if digits[0] == 3:
                    r1_position = [674,797]
                    screen.blit(r3, r1_position)
                if digits[0] == 4:
                    r1_position = [674,855]
                    screen.blit(r4, r1_position)
                if digits[0] == 5:
                    r1_position = [675,915]
                    screen.blit(r5, r1_position)
                if digits[0] == 6:
                    r1_position = [657,972]
                    screen.blit(r6, r1_position)
                if digits[0] == 7:
                    r1_position = [609,1004]
                    screen.blit(r7, r1_position)
                if digits[0] == 8:
                    r1_position = [552,1005]
                    screen.blit(r8, r1_position)
                if digits[0] == 9:
                    r1_position = [496,1008]
                    screen.blit(r9, r1_position)

    pygame.display.update()

    
