import pygame

screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

card = pygame.image.load('fun_spot_63/assets/card.png').convert_alpha()
number = pygame.image.load('fun_spot_63/assets/number.png').convert_alpha()
tilt = pygame.image.load('fun_spot_63/assets/tilt.png').convert_alpha()
r10000 = pygame.image.load('fun_spot_63/assets/10000.png').convert_alpha()
r20000 = pygame.image.load('fun_spot_63/assets/20000.png').convert_alpha()
r1000 = pygame.image.load('fun_spot_63/assets/1000.png').convert_alpha()
r2000 = pygame.image.load('fun_spot_63/assets/2000.png').convert_alpha()
r3000 = pygame.image.load('fun_spot_63/assets/3000.png').convert_alpha()
r4000 = pygame.image.load('fun_spot_63/assets/4000.png').convert_alpha()
r5000 = pygame.image.load('fun_spot_63/assets/5000.png').convert_alpha()
r6000 = pygame.image.load('fun_spot_63/assets/6000.png').convert_alpha()
r7000 = pygame.image.load('fun_spot_63/assets/7000.png').convert_alpha()
r8000 = pygame.image.load('fun_spot_63/assets/8000.png').convert_alpha()
r9000 = pygame.image.load('fun_spot_63/assets/9000.png').convert_alpha()
r100 = pygame.image.load('fun_spot_63/assets/100.png').convert_alpha()
r200 = pygame.image.load('fun_spot_63/assets/200.png').convert_alpha()
r300 = pygame.image.load('fun_spot_63/assets/300.png').convert_alpha()
r400 = pygame.image.load('fun_spot_63/assets/400.png').convert_alpha()
r500 = pygame.image.load('fun_spot_63/assets/500.png').convert_alpha()
r600 = pygame.image.load('fun_spot_63/assets/600.png').convert_alpha()
r700 = pygame.image.load('fun_spot_63/assets/700.png').convert_alpha()
r800 = pygame.image.load('fun_spot_63/assets/800.png').convert_alpha()
r900 = pygame.image.load('fun_spot_63/assets/900.png').convert_alpha()
bg_menu = pygame.image.load('fun_spot_63/assets/fun_spot_63_menu.png')
bg_gi = pygame.image.load('fun_spot_63/assets/fun_spot_63_gi.png')
bg_off = pygame.image.load('fun_spot_63/assets/fun_spot_63_off.png')

def display(s, replays=0, menu=False):

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

    if s.game.selector.position >= 1:
        card1_position = [73,772]
        screen.blit(card, card1_position)
    if s.game.selector.position >= 2:
        card2_position = [284,770]
        screen.blit(card, card2_position)
    if s.game.selector.position >= 3:
        card3_position = [494,770]
        screen.blit(card, card3_position)
    if s.game.selector.position >= 4:
        card4_position = [71,1007]
        screen.blit(card, card4_position)
    if s.game.selector.position >= 5:
        card5_position = [283,1005]
        screen.blit(card, card5_position)
    if s.game.selector.position >= 6:
        card6_position = [495,1006]
        screen.blit(card, card6_position)

 
    if s.game.tilt.status == False:
        if s.holes:
            if 1 in s.holes:
                number1_position = [92,592]
                screen.blit(number, number1_position)
                number2_position = [268,696]
                screen.blit(number, number2_position)
                number3_position = [585,732]
                screen.blit(number, number3_position)
                number3_position = [198,826]
                screen.blit(number, number3_position)
                number3_position = [267,968]
                screen.blit(number, number3_position)
                number3_position = [550,828]
                screen.blit(number, number3_position)
            if 2 in s.holes:
                number_position = [128,732]
                screen.blit(number, number_position)
                number_position = [269,661]
                screen.blit(number, number_position)
                number_position = [619,662]
                screen.blit(number, number_position)
                number_position = [198,862]
                screen.blit(number, number_position)
                number_position = [268,862]
                screen.blit(number, number_position)
                number_position = [584,966]
                screen.blit(number, number_position)
            if 3 in s.holes:
                number_position = [198,591]
                screen.blit(number, number_position)
                number_position = [410,731]
                screen.blit(number, number_position)
                number_position = [480,590]
                screen.blit(number, number_position)
                number_position = [128,826]
                screen.blit(number, number_position)
                number_position = [373,966]
                screen.blit(number, number_position)
                number_position = [549,862]
                screen.blit(number, number_position)
            if 4 in s.holes:
                number_position = [163,732]
                screen.blit(number, number_position)
                number_position = [374,590]
                screen.blit(number, number_position)
                number_position = [584,590]
                screen.blit(number, number_position)
                number_position = [162,966]
                screen.blit(number, number_position)
                number_position = [408,827]
                screen.blit(number, number_position)
                number_position = [479,828]
                screen.blit(number, number_position)
            if 5 in s.holes:
                number_position = [57,592]
                screen.blit(number, number_position)
                number_position = [338,730]
                screen.blit(number, number_position)
                number_position = [620,731]
                screen.blit(number, number_position)
                number_position = [57,896]
                screen.blit(number, number_position)
                number_position = [408,896]
                screen.blit(number, number_position)
                number_position = [618,827]
                screen.blit(number, number_position)
            if 6 in s.holes:
                number_position = [58,662]
                screen.blit(number, number_position)
                number_position = [408,590]
                screen.blit(number, number_position)
                number_position = [480,730]
                screen.blit(number, number_position)
                number_position = [57,826]
                screen.blit(number, number_position)
                number_position = [406,966]
                screen.blit(number, number_position)
                number_position = [514,827]
                screen.blit(number, number_position)
            if 7 in s.holes:
                number_position = [198,626]
                screen.blit(number, number_position)
                number_position = [304,730]
                screen.blit(number, number_position)
                number_position = [514,591]
                screen.blit(number, number_position)
                number_position = [92,826]
                screen.blit(number, number_position)
                number_position = [302,966]
                screen.blit(number, number_position)
                number_position = [480,966]
                screen.blit(number, number_position)
            if 8 in s.holes:
                number_position = [58,626]
                screen.blit(number, number_position)
                number_position = [409,696]
                screen.blit(number, number_position)
                number_position = [619,626]
                screen.blit(number, number_position)
                number_position = [198,968]
                screen.blit(number, number_position)
                number_position = [268,826]
                screen.blit(number, number_position)
                number_position = [619,932]
                screen.blit(number, number_position)
            if 9 in s.holes:
                number_position = [128,592]
                screen.blit(number, number_position)
                number_position = [269,591]
                screen.blit(number, number_position)
                number_position = [619,591]
                screen.blit(number, number_position)
                number_position = [127,932]
                screen.blit(number, number_position)
                number_position = [338,932]
                screen.blit(number, number_position)
                number_position = [480,898]
                screen.blit(number, number_position)
            if 10 in s.holes:
                number_position = [128,626]
                screen.blit(number, number_position)
                number_position = [269,732]
                screen.blit(number, number_position)
                number_position = [549,590]
                screen.blit(number, number_position)
                number_position = [56,966]
                screen.blit(number, number_position)
                number_position = [338,826]
                screen.blit(number, number_position)
                number_position = [480,932]
                screen.blit(number, number_position)
            if 11 in s.holes:
                number_position = [164,662]
                screen.blit(number, number_position)
                number_position = [339,695]
                screen.blit(number, number_position)
                number_position = [585,660]
                screen.blit(number, number_position)
                number_position = [57,931]
                screen.blit(number, number_position)
                number_position = [408,931]
                screen.blit(number, number_position)
                number_position = [618,966]
                screen.blit(number, number_position)
            if 12 in s.holes:
                number_position = [58,731]
                screen.blit(number, number_position)
                number_position = [374,660]
                screen.blit(number, number_position)
                number_position = [550,696]
                screen.blit(number, number_position)
                number_position = [127,860]
                screen.blit(number, number_position)
                number_position = [303,896]
                screen.blit(number, number_position)
                number_position = [584,896]
                screen.blit(number, number_position)
            if 13 in s.holes:
                number_position = [198,696]
                screen.blit(number, number_position)
                number_position = [270,626]
                screen.blit(number, number_position)
                number_position = [480,695]
                screen.blit(number, number_position)
                number_position = [92,966]
                screen.blit(number, number_position)
                number_position = [374,826]
                screen.blit(number, number_position)
                number_position = [618,861]
                screen.blit(number, number_position)
            if 14 in s.holes:
                number_position = [127,696]
                screen.blit(number, number_position)
                number_position = [338,624]
                screen.blit(number, number_position)
                number_position = [514,660]
                screen.blit(number, number_position)
                number_position = [92,861]
                screen.blit(number, number_position)
                number_position = [374,862]
                screen.blit(number, number_position)
                number_position = [584,932]
                screen.blit(number, number_position)
            if 15 in s.holes:
                number_position = [198,732]
                screen.blit(number, number_position)
                number_position = [338,660]
                screen.blit(number, number_position)
                number_position = [480,660]
                screen.blit(number, number_position)
                number_position = [162,932]
                screen.blit(number, number_position)
                number_position = [302,932]
                screen.blit(number, number_position)
                number_position = [514,862]
                screen.blit(number, number_position)
            if 16 in s.holes:
                number_position = [128,662]
                screen.blit(number, number_position)
                number_position = [340,590]
                screen.blit(number, number_position)
                number_position = [549,730]
                screen.blit(number, number_position)
                number_position = [162,896]
                screen.blit(number, number_position)
                number_position = [338,860]
                screen.blit(number, number_position)
                number_position = [549,932]
                screen.blit(number, number_position)
            if 17 in s.holes:
                number_position = [198,661]
                screen.blit(number, number_position)
                number_position = [409,660]
                screen.blit(number, number_position)
                number_position = [550,660]
                screen.blit(number, number_position)
                number_position = [92,932]
                screen.blit(number, number_position)
                number_position = [303,860]
                screen.blit(number, number_position)
                number_position = [584,862]
                screen.blit(number, number_position)
            if 18 in s.holes:
                number_position = [92,662]
                screen.blit(number, number_position)
                number_position = [304,659]
                screen.blit(number, number_position)
                number_position = [549,625]
                screen.blit(number, number_position)
                number_position = [162,860]
                screen.blit(number, number_position)
                number_position = [372,932]
                screen.blit(number, number_position)
                number_position = [514,932]
                screen.blit(number, number_position)
            if 19 in s.holes:
                number_position = [162,626]
                screen.blit(number, number_position)
                number_position = [304,625]
                screen.blit(number, number_position)
                number_position = [585,696]
                screen.blit(number, number_position)
                number_position = [91,895]
                screen.blit(number, number_position)
                number_position = [374,896]
                screen.blit(number, number_position)
                number_position = [514,896]
                screen.blit(number, number_position)
            if 20 in s.holes:
                number_position = [164,696]
                screen.blit(number, number_position)
                number_position = [374,625]
                screen.blit(number, number_position)
                number_position = [515,696]
                screen.blit(number, number_position)
                number_position = [126,896]
                screen.blit(number, number_position)
                number_position = [268,895]
                screen.blit(number, number_position)
                number_position = [618,896]
                screen.blit(number, number_position)
            if 21 in s.holes:
                number_position = [92,695]
                screen.blit(number, number_position)
                number_position = [374,695]
                screen.blit(number, number_position)
                number_position = [514,626]
                screen.blit(number, number_position)
                number_position = [127,966]
                screen.blit(number, number_position)
                number_position = [338,965]
                screen.blit(number, number_position)
                number_position = [549,896]
                screen.blit(number, number_position)
            if 22 in s.holes:
                number_position = [93,626]
                screen.blit(number, number_position)
                number_position = [304,694]
                screen.blit(number, number_position)
                number_position = [584,625]
                screen.blit(number, number_position)
                number_position = [197,896]
                screen.blit(number, number_position)
                number_position = [337,894]
                screen.blit(number, number_position)
                number_position = [549,966]
                screen.blit(number, number_position)
            if 23 in s.holes:
                number_position = [92,730]
                screen.blit(number, number_position)
                number_position = [374,730]
                screen.blit(number, number_position)
                number_position = [618,695]
                screen.blit(number, number_position)
                number_position = [57,861]
                screen.blit(number, number_position)
                number_position = [303,826]
                screen.blit(number, number_position)
                number_position = [584,828]
                screen.blit(number, number_position)
            if 24 in s.holes:
                number_position = [58,697]
                screen.blit(number, number_position)
                number_position = [304,590]
                screen.blit(number, number_position)
                number_position = [479,626]
                screen.blit(number, number_position)
                number_position = [162,826]
                screen.blit(number, number_position)
                number_position = [408,860]
                screen.blit(number, number_position)
                number_position = [514,965]
                screen.blit(number, number_position)
            if 25 in s.holes:
                number_position = [162,592]
                screen.blit(number, number_position)
                number_position = [409,625]
                screen.blit(number, number_position)
                number_position = [514,730]
                screen.blit(number, number_position)
                number_position = [197,930]
                screen.blit(number, number_position)
                number_position = [268,931]
                screen.blit(number, number_position)
                number_position = [479,862]
                screen.blit(number, number_position)


    if s.game.tilt.status == True:
        tilt_position = [403,224]
        screen.blit(tilt, tilt_position)

    if s.game.replays:
        digits = [int(d) for d in list(str(s.game.replays))]
        if len(digits) == 3:
            if digits[0] == 1:
                r100_position = [228,283]
                screen.blit(r10000, r100_position)
            elif digits[0] == 2:
                r100_position = [458,356]
                screen.blit(r20000, r100_position)
            if digits[1] != 0:
                if digits[1] == 1:
                    r10_position = [63,532]
                    screen.blit(r1000, r10_position)
                if digits[1] == 2:
                    r10_position = [50,488]
                    screen.blit(r2000, r10_position)
                if digits[1] == 3:
                    r10_position = [46,448]
                    screen.blit(r3000, r10_position)
                if digits[1] == 4:
                    r10_position = [46,405]
                    screen.blit(r4000, r10_position)
                if digits[1] == 5:
                    r10_position = [52,367]
                    screen.blit(r5000, r10_position)
                if digits[1] == 6:
                    r10_position = [61,327]
                    screen.blit(r6000, r10_position)
                if digits[1] == 7:
                    r10_position = [81,296]
                    screen.blit(r7000, r10_position)
                if digits[1] == 8:
                    r10_position = [97,263]
                    screen.blit(r8000, r10_position)
                if digits[1] == 9:
                    r10_position = [134,234]
                    screen.blit(r9000, r10_position)

            if digits[2] != 0:
                if digits[2] == 1:
                    r1_position = [334,536]
                    screen.blit(r100, r1_position)
                if digits[2] == 2:
                    r1_position = [344,500]
                    screen.blit(r200, r1_position)
                if digits[2] == 3:
                    r1_position = [355,464]
                    screen.blit(r300, r1_position)
                if digits[2] == 4:
                    r1_position = [354,422]
                    screen.blit(r400, r1_position)
                if digits[2] == 5:
                    r1_position = [353,387]
                    screen.blit(r500, r1_position)
                if digits[2] == 6:
                    r1_position = [349,349]
                    screen.blit(r600, r1_position)
                if digits[2] == 7:
                    r1_position = [338,316]
                    screen.blit(r700, r1_position)
                if digits[2] == 8:
                    r1_position = [317,279]
                    screen.blit(r800, r1_position)
                if digits[2] == 9:
                    r1_position = [286,248]
                    screen.blit(r900, r1_position)

        if len(digits) == 2:
            if digits[0] != 0:
                if digits[0] == 1:
                    r10_position = [63,532]
                    screen.blit(r1000, r10_position)
                if digits[0] == 2:
                    r10_position = [50,488]
                    screen.blit(r2000, r10_position)
                if digits[0] == 3:
                    r10_position = [46,448]
                    screen.blit(r3000, r10_position)
                if digits[0] == 4:
                    r10_position = [46,405]
                    screen.blit(r4000, r10_position)
                if digits[0] == 5:
                    r10_position = [52,367]
                    screen.blit(r5000, r10_position)
                if digits[0] == 6:
                    r10_position = [61,327]
                    screen.blit(r6000, r10_position)
                if digits[0] == 7:
                    r10_position = [81,296]
                    screen.blit(r7000, r10_position)
                if digits[0] == 8:
                    r10_position = [97,263]
                    screen.blit(r8000, r10_position)
                if digits[0] == 9:
                    r10_position = [134,234]
                    screen.blit(r9000, r10_position)

            if digits[1] != 0:
                if digits[1] == 1:
                    r1_position = [334,536]
                    screen.blit(r100, r1_position)
                if digits[1] == 2:
                    r1_position = [344,500]
                    screen.blit(r200, r1_position)
                if digits[1] == 3:
                    r1_position = [355,464]
                    screen.blit(r300, r1_position)
                if digits[1] == 4:
                    r1_position = [354,422]
                    screen.blit(r400, r1_position)
                if digits[1] == 5:
                    r1_position = [353,387]
                    screen.blit(r500, r1_position)
                if digits[1] == 6:
                    r1_position = [349,349]
                    screen.blit(r600, r1_position)
                if digits[1] == 7:
                    r1_position = [338,316]
                    screen.blit(r700, r1_position)
                if digits[1] == 8:
                    r1_position = [317,279]
                    screen.blit(r800, r1_position)
                if digits[1] == 9:
                    r1_position = [286,248]
                    screen.blit(r900, r1_position)


        if len(digits) == 1:
            if digits[0] != 0:
                if digits[0] == 1:
                    r1_position = [334,536]
                    screen.blit(r100, r1_position)
                if digits[0] == 2:
                    r1_position = [344,500]
                    screen.blit(r200, r1_position)
                if digits[0] == 3:
                    r1_position = [355,464]
                    screen.blit(r300, r1_position)
                if digits[0] == 4:
                    r1_position = [354,422]
                    screen.blit(r400, r1_position)
                if digits[0] == 5:
                    r1_position = [353,387]
                    screen.blit(r500, r1_position)
                if digits[0] == 6:
                    r1_position = [349,349]
                    screen.blit(r600, r1_position)
                if digits[0] == 7:
                    r1_position = [338,316]
                    screen.blit(r700, r1_position)
                if digits[0] == 8:
                    r1_position = [317,279]
                    screen.blit(r800, r1_position)
                if digits[0] == 9:
                    r1_position = [286,248]
                    screen.blit(r900, r1_position)

    pygame.display.update()
