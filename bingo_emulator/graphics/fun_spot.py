import pygame

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

card = pygame.image.load('fun_spot/assets/card.png').convert_alpha()
number = pygame.image.load('fun_spot/assets/number.png').convert_alpha()
tilt = pygame.image.load('fun_spot/assets/tilt.png').convert_alpha()
r10000 = pygame.image.load('fun_spot/assets/10000.png').convert_alpha()
r20000 = pygame.image.load('fun_spot/assets/20000.png').convert_alpha()
r1000 = pygame.image.load('fun_spot/assets/1000.png').convert_alpha()
r2000 = pygame.image.load('fun_spot/assets/2000.png').convert_alpha()
r3000 = pygame.image.load('fun_spot/assets/3000.png').convert_alpha()
r4000 = pygame.image.load('fun_spot/assets/4000.png').convert_alpha()
r5000 = pygame.image.load('fun_spot/assets/5000.png').convert_alpha()
r6000 = pygame.image.load('fun_spot/assets/6000.png').convert_alpha()
r7000 = pygame.image.load('fun_spot/assets/7000.png').convert_alpha()
r8000 = pygame.image.load('fun_spot/assets/8000.png').convert_alpha()
r9000 = pygame.image.load('fun_spot/assets/9000.png').convert_alpha()
r100 = pygame.image.load('fun_spot/assets/100.png').convert_alpha()
r200 = pygame.image.load('fun_spot/assets/200.png').convert_alpha()
r300 = pygame.image.load('fun_spot/assets/300.png').convert_alpha()
r400 = pygame.image.load('fun_spot/assets/400.png').convert_alpha()
r500 = pygame.image.load('fun_spot/assets/500.png').convert_alpha()
r600 = pygame.image.load('fun_spot/assets/600.png').convert_alpha()
r700 = pygame.image.load('fun_spot/assets/700.png').convert_alpha()
r800 = pygame.image.load('fun_spot/assets/800.png').convert_alpha()
r900 = pygame.image.load('fun_spot/assets/900.png').convert_alpha()

def display(s, replays=0, menu=False):

    backglass_position = [0, 0]
    backglass = pygame.Surface(screen.get_size(), flags=pygame.SRCALPHA)
    backglass.fill((0, 0, 0))
    if menu == True:
        backglass = pygame.image.load('fun_spot/assets/fun_spot_menu.png')
    else:
        if (s.game.anti_cheat.status == True):
            backglass = pygame.image.load('fun_spot/assets/fun_spot_gi.png')
        else:
            backglass = pygame.image.load('fun_spot/assets/fun_spot_off.png')
    backglass = pygame.transform.scale(backglass, (720, 1280))
    
    screen.blit(backglass, backglass_position)

    if s.game.selector.position >= 1:
        card1_position = [82,771]
        screen.blit(card, card1_position)
    if s.game.selector.position >= 2:
        card2_position = [288,775]
        screen.blit(card, card2_position)
    if s.game.selector.position >= 3:
        card3_position = [498,770]
        screen.blit(card, card3_position)
    if s.game.selector.position >= 4:
        card4_position = [86,1020]
        screen.blit(card, card4_position)
    if s.game.selector.position >= 5:
        card5_position = [290,1022]
        screen.blit(card, card5_position)
    if s.game.selector.position >= 6:
        card6_position = [497,1016]
        screen.blit(card, card6_position)

    if s.game.tilt.status == False:
        if s.holes:
            if 1 in s.holes:
                number_position = [100,579]
                screen.blit(number, number_position)
                number_position = [272,693]
                screen.blit(number, number_position)
                number_position = [584,729]
                screen.blit(number, number_position)
                number_position = [202,829]
                screen.blit(number, number_position)
                number_position = [273,978]
                screen.blit(number, number_position)
                number_position = [548,826]
                screen.blit(number, number_position)
            if 2 in s.holes:
                number_position = [132,730]
                screen.blit(number, number_position)
                number_position = [272,654]
                screen.blit(number, number_position)
                number_position = [616,652]
                screen.blit(number, number_position)
                number_position = [204,866]
                screen.blit(number, number_position)
                number_position = [272,866]
                screen.blit(number, number_position)
                number_position = [580,975]
                screen.blit(number, number_position)
            if 3 in s.holes:
                number_position = [202,578]
                screen.blit(number, number_position)
                number_position = [411,730]
                screen.blit(number, number_position)
                number_position = [478,578]
                screen.blit(number, number_position)
                number_position = [135,828]
                screen.blit(number, number_position)
                number_position = [376,978]
                screen.blit(number, number_position)
                number_position = [549,864]
                screen.blit(number, number_position)
            if 4 in s.holes:
                number_position = [168,730]
                screen.blit(number, number_position)
                number_position = [375,578]
                screen.blit(number, number_position)
                number_position = [582,576]
                screen.blit(number, number_position)
                number_position = [171,978]
                screen.blit(number, number_position)
                number_position = [410,830]
                screen.blit(number, number_position)
                number_position = [480,828]
                screen.blit(number, number_position)
            if 5 in s.holes:
                number_position = [64,578]
                screen.blit(number, number_position)
                number_position = [341,730]
                screen.blit(number, number_position)
                number_position = [618,727]
                screen.blit(number, number_position)
                number_position = [68,903]
                screen.blit(number, number_position)
                number_position = [411,903]
                screen.blit(number, number_position)
                number_position = [615,826]
                screen.blit(number, number_position)
            if 6 in s.holes:
                number_position = [64,654]
                screen.blit(number, number_position)
                number_position = [411,578]
                screen.blit(number, number_position)
                number_position = [480,728]
                screen.blit(number, number_position)
                number_position = [66,828]
                screen.blit(number, number_position)
                number_position = [411,977]
                screen.blit(number, number_position)
                number_position = [513,826]
                screen.blit(number, number_position)
            if 7 in s.holes:
                number_position = [202,616]
                screen.blit(number, number_position)
                number_position = [306,732]
                screen.blit(number, number_position)
                number_position = [513,577]
                screen.blit(number, number_position)
                number_position = [100,830]
                screen.blit(number, number_position)
                number_position = [306,980]
                screen.blit(number, number_position)
                number_position = [478,979]
                screen.blit(number, number_position)
            if 8 in s.holes:
                number_position = [64,619]
                screen.blit(number, number_position)
                number_position = [411,694]
                screen.blit(number, number_position)
                number_position = [616,616]
                screen.blit(number, number_position)
                number_position = [204,980]
                screen.blit(number, number_position)
                number_position = [272,832]
                screen.blit(number, number_position)
                number_position = [615,938]
                screen.blit(number, number_position)
            if 9 in s.holes:
                number_position = [134,580]
                screen.blit(number, number_position)
                number_position = [272,580]
                screen.blit(number, number_position)
                number_position = [616,578]
                screen.blit(number, number_position)
                number_position = [134,944]
                screen.blit(number, number_position)
                number_position = [340,944]
                screen.blit(number, number_position)
                number_position = [480,904]
                screen.blit(number, number_position)
            if 10 in s.holes:
                number_position = [134,619]
                screen.blit(number, number_position)
                number_position = [273,730]
                screen.blit(number, number_position)
                number_position = [548,576]
                screen.blit(number, number_position)
                number_position = [68,980]
                screen.blit(number, number_position)
                number_position = [340,832]
                screen.blit(number, number_position)
                number_position = [478,943]
                screen.blit(number, number_position)
            if 11 in s.holes:
                number_position = [168,656]
                screen.blit(number, number_position)
                number_position = [344,694]
                screen.blit(number, number_position)
                number_position = [582,654]
                screen.blit(number, number_position)
                number_position = [68,942]
                screen.blit(number, number_position)
                number_position = [411,943]
                screen.blit(number, number_position)
                number_position = [616,976]
                screen.blit(number, number_position)
            if 12 in s.holes:
                number_position = [64,733]
                screen.blit(number, number_position)
                number_position = [375,655]
                screen.blit(number, number_position)
                number_position = [549,692]
                screen.blit(number, number_position)
                number_position = [135,868]
                screen.blit(number, number_position)
                number_position = [306,907]
                screen.blit(number, number_position)
                number_position = [582,902]
                screen.blit(number, number_position)
            if 13 in s.holes:
                number_position = [204,694]
                screen.blit(number, number_position)
                number_position = [272,619]
                screen.blit(number, number_position)
                number_position = [483,692]
                screen.blit(number, number_position)
                number_position = [100,980]
                screen.blit(number, number_position)
                number_position = [375,830]
                screen.blit(number, number_position)
                number_position = [614,865]
                screen.blit(number, number_position)
            if 14 in s.holes:
                number_position = [132,694]
                screen.blit(number, number_position)
                number_position = [340,618]
                screen.blit(number, number_position)
                number_position = [514,655]
                screen.blit(number, number_position)
                number_position = [100,870]
                screen.blit(number, number_position)
                number_position = [376,870]
                screen.blit(number, number_position)
                number_position = [580,940]
                screen.blit(number, number_position)
            if 15 in s.holes:
                number_position = [202,734]
                screen.blit(number, number_position)
                number_position = [340,655]
                screen.blit(number, number_position)
                number_position = [482,655]
                screen.blit(number, number_position)
                number_position = [170,944]
                screen.blit(number, number_position)
                number_position = [308,944]
                screen.blit(number, number_position)
                number_position = [514,868]
                screen.blit(number, number_position)
            if 16 in s.holes:
                number_position = [134,656]
                screen.blit(number, number_position)
                number_position = [340,578]
                screen.blit(number, number_position)
                number_position = [549,728]
                screen.blit(number, number_position)
                number_position = [170,903]
                screen.blit(number, number_position)
                number_position = [341,866]
                screen.blit(number, number_position)
                number_position = [548,938]
                screen.blit(number, number_position)
            if 17 in s.holes:
                number_position = [204,656]
                screen.blit(number, number_position)
                number_position = [411,655]
                screen.blit(number, number_position)
                number_position = [549,655]
                screen.blit(number, number_position)
                number_position = [100,943]
                screen.blit(number, number_position)
                number_position = [306,870]
                screen.blit(number, number_position)
                number_position = [582,866]
                screen.blit(number, number_position)
            if 18 in s.holes:
                number_position = [99,656]
                screen.blit(number, number_position)
                number_position = [306,658]
                screen.blit(number, number_position)
                number_position = [548,618]
                screen.blit(number, number_position)
                number_position = [170,870]
                screen.blit(number, number_position)
                number_position = [375,944]
                screen.blit(number, number_position)
                number_position = [513,943]
                screen.blit(number, number_position)
            if 19 in s.holes:
                number_position = [168,618]
                screen.blit(number, number_position)
                number_position = [306,618]
                screen.blit(number, number_position)
                number_position = [582,692]
                screen.blit(number, number_position)
                number_position = [100,907]
                screen.blit(number, number_position)
                number_position = [376,907]
                screen.blit(number, number_position)
                number_position = [514,902]
                screen.blit(number, number_position)
            if 20 in s.holes:
                number_position = [168,696]
                screen.blit(number, number_position)
                number_position = [375,619]
                screen.blit(number, number_position)
                number_position = [514,692]
                screen.blit(number, number_position)
                number_position = [135,907]
                screen.blit(number, number_position)
                number_position = [272,908]
                screen.blit(number, number_position)
                number_position = [615,902]
                screen.blit(number, number_position)
            if 21 in s.holes:
                number_position = [99,694]
                screen.blit(number, number_position)
                number_position = [375,694]
                screen.blit(number, number_position)
                number_position = [513,618]
                screen.blit(number, number_position)
                number_position = [136,980]
                screen.blit(number, number_position)
                number_position = [342,980]
                screen.blit(number, number_position)
                number_position = [548,904]
                screen.blit(number, number_position)
            if 22 in s.holes:
                number_position = [100,618]
                screen.blit(number, number_position)
                number_position = [306,692]
                screen.blit(number, number_position)
                number_position = [584,616]
                screen.blit(number, number_position)
                number_position = [204,907]
                screen.blit(number, number_position)
                number_position = [340,907]
                screen.blit(number, number_position)
                number_position = [548,975]
                screen.blit(number, number_position)
            if 23 in s.holes:
                number_position = [99,732]
                screen.blit(number, number_position)
                number_position = [376,732]
                screen.blit(number, number_position)
                number_position = [616,692]
                screen.blit(number, number_position)
                number_position = [66,870]
                screen.blit(number, number_position)
                number_position = [306,832]
                screen.blit(number, number_position)
                number_position = [582,828]
                screen.blit(number, number_position)
            if 24 in s.holes:
                number_position = [64,696]
                screen.blit(number, number_position)
                number_position = [306,580]
                screen.blit(number, number_position)
                number_position = [480,618]
                screen.blit(number, number_position)
                number_position = [168,832]
                screen.blit(number, number_position)
                number_position = [411,868]
                screen.blit(number, number_position)
                number_position = [513,979]
                screen.blit(number, number_position)
            if 25 in s.holes:
                number_position = [168,580]
                screen.blit(number, number_position)
                number_position = [411,618]
                screen.blit(number, number_position)
                number_position = [514,730]
                screen.blit(number, number_position)
                number_position = [206,944]
                screen.blit(number, number_position)
                number_position = [272,944]
                screen.blit(number, number_position)
                number_position = [480,868]
                screen.blit(number, number_position)

    if s.game.tilt.status == True:
        tilt_position = [450,352]
        screen.blit(tilt, tilt_position)

    if s.game.replays:
        digits = [int(d) for d in list(str(s.game.replays))]
        if len(digits) == 3:
            if digits[0] == 1:
                r100_position = [296,361]
                screen.blit(r10000, r100_position)
            elif digits[0] == 2:
                r100_position = [382,445]
                screen.blit(r20000, r100_position)
            if digits[1] != 0:
                if digits[1] == 1:
                    r10_position = [216,512]
                    screen.blit(r1000, r10_position)
                if digits[1] == 2:
                    r10_position = [208,475]
                    screen.blit(r2000, r10_position)
                if digits[1] == 3:
                    r10_position = [206,442]
                    screen.blit(r3000, r10_position)
                if digits[1] == 4:
                    r10_position = [211,398]
                    screen.blit(r4000, r10_position)
                if digits[1] == 5:
                    r10_position = [212,366]
                    screen.blit(r5000, r10_position)
                if digits[1] == 6:
                    r10_position = [218,333]
                    screen.blit(r6000, r10_position)
                if digits[1] == 7:
                    r10_position = [228,292]
                    screen.blit(r7000, r10_position)
                if digits[1] == 8:
                    r10_position = [224,258]
                    screen.blit(r8000, r10_position)
                if digits[1] == 9:
                    r10_position = [220,227]
                    screen.blit(r9000, r10_position)

            if digits[2] != 0:
                if digits[2] == 1:
                    r1_position = [11,512]
                    screen.blit(r100, r1_position)
                if digits[2] == 2:
                    r1_position = [15,478]
                    screen.blit(r200, r1_position)
                if digits[2] == 3:
                    r1_position = [22,447]
                    screen.blit(r300, r1_position)
                if digits[2] == 4:
                    r1_position = [30,402]
                    screen.blit(r400, r1_position)
                if digits[2] == 5:
                    r1_position = [24,370]
                    screen.blit(r500, r1_position)
                if digits[2] == 6:
                    r1_position = [22,338]
                    screen.blit(r600, r1_position)
                if digits[2] == 7:
                    r1_position = [15,296]
                    screen.blit(r700, r1_position)
                if digits[2] == 8:
                    r1_position = [15,260]
                    screen.blit(r800, r1_position)
                if digits[2] == 9:
                    r1_position = [24,232]
                    screen.blit(r900, r1_position)
        if len(digits) == 2:
            if digits[0] != 0:
                if digits[0] == 1:
                    r10_position = [216,512]
                    screen.blit(r1000, r10_position)
                if digits[0] == 2:
                    r10_position = [208,475]
                    screen.blit(r2000, r10_position)
                if digits[0] == 3:
                    r10_position = [206,442]
                    screen.blit(r3000, r10_position)
                if digits[0] == 4:
                    r10_position = [211,398]
                    screen.blit(r4000, r10_position)
                if digits[0] == 5:
                    r10_position = [212,366]
                    screen.blit(r5000, r10_position)
                if digits[0] == 6:
                    r10_position = [218,333]
                    screen.blit(r6000, r10_position)
                if digits[0] == 7:
                    r10_position = [228,292]
                    screen.blit(r7000, r10_position)
                if digits[0] == 8:
                    r10_position = [224,258]
                    screen.blit(r8000, r10_position)
                if digits[0] == 9:
                    r10_position = [220,227]
                    screen.blit(r9000, r10_position)

            if digits[1] != 0:
                if digits[1] == 1:
                    r1_position = [11,512]
                    screen.blit(r100, r1_position)
                if digits[1] == 2:
                    r1_position = [15,478]
                    screen.blit(r200, r1_position)
                if digits[1] == 3:
                    r1_position = [22,447]
                    screen.blit(r300, r1_position)
                if digits[1] == 4:
                    r1_position = [30,402]
                    screen.blit(r400, r1_position)
                if digits[1] == 5:
                    r1_position = [24,370]
                    screen.blit(r500, r1_position)
                if digits[1] == 6:
                    r1_position = [22,338]
                    screen.blit(r600, r1_position)
                if digits[1] == 7:
                    r1_position = [15,296]
                    screen.blit(r700, r1_position)
                if digits[1] == 8:
                    r1_position = [15,260]
                    screen.blit(r800, r1_position)
                if digits[1] == 9:
                    r1_position = [24,232]
                    screen.blit(r900, r1_position)

        if len(digits) == 1:
            if digits[0] != 0:
                if digits[0] == 1:
                    r1_position = [11,512]
                    screen.blit(r100, r1_position)
                if digits[0] == 2:
                    r1_position = [15,478]
                    screen.blit(r200, r1_position)
                if digits[0] == 3:
                    r1_position = [22,447]
                    screen.blit(r300, r1_position)
                if digits[0] == 4:
                    r1_position = [30,402]
                    screen.blit(r400, r1_position)
                if digits[0] == 5:
                    r1_position = [24,370]
                    screen.blit(r500, r1_position)
                if digits[0] == 6:
                    r1_position = [22,338]
                    screen.blit(r600, r1_position)
                if digits[0] == 7:
                    r1_position = [15,296]
                    screen.blit(r700, r1_position)
                if digits[0] == 8:
                    r1_position = [15,260]
                    screen.blit(r800, r1_position)
                if digits[0] == 9:
                    r1_position = [24,232]
                    screen.blit(r900, r1_position)

    pygame.display.update()

    
