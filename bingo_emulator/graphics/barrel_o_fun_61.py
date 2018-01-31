import pygame

pygame.display.set_caption("Barrel O Fun '61")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

card = pygame.image.load('barrel_o_fun_61/assets/card.png').convert_alpha()
number = pygame.image.load('barrel_o_fun_61/assets/number.png').convert_alpha()
tilt = pygame.image.load('barrel_o_fun_61/assets/tilt.png').convert_alpha()
r10000 = pygame.image.load('barrel_o_fun_61/assets/10000.png').convert_alpha()
r20000 = pygame.image.load('barrel_o_fun_61/assets/20000.png').convert_alpha()
r1000 = pygame.image.load('barrel_o_fun_61/assets/1000.png').convert_alpha()
r2000 = pygame.image.load('barrel_o_fun_61/assets/2000.png').convert_alpha()
r3000 = pygame.image.load('barrel_o_fun_61/assets/3000.png').convert_alpha()
r4000 = pygame.image.load('barrel_o_fun_61/assets/4000.png').convert_alpha()
r5000 = pygame.image.load('barrel_o_fun_61/assets/5000.png').convert_alpha()
r6000 = pygame.image.load('barrel_o_fun_61/assets/6000.png').convert_alpha()
r7000 = pygame.image.load('barrel_o_fun_61/assets/7000.png').convert_alpha()
r8000 = pygame.image.load('barrel_o_fun_61/assets/8000.png').convert_alpha()
r9000 = pygame.image.load('barrel_o_fun_61/assets/9000.png').convert_alpha()
r100 = pygame.image.load('barrel_o_fun_61/assets/100.png').convert_alpha()
r200 = pygame.image.load('barrel_o_fun_61/assets/200.png').convert_alpha()
r300 = pygame.image.load('barrel_o_fun_61/assets/300.png').convert_alpha()
r400 = pygame.image.load('barrel_o_fun_61/assets/400.png').convert_alpha()
r500 = pygame.image.load('barrel_o_fun_61/assets/500.png').convert_alpha()
r600 = pygame.image.load('barrel_o_fun_61/assets/600.png').convert_alpha()
r700 = pygame.image.load('barrel_o_fun_61/assets/700.png').convert_alpha()
r800 = pygame.image.load('barrel_o_fun_61/assets/800.png').convert_alpha()
r900 = pygame.image.load('barrel_o_fun_61/assets/900.png').convert_alpha()
bg_menu = pygame.image.load('barrel_o_fun_61/assets/barrel_o_fun_61_menu.png')
bg_gi = pygame.image.load('barrel_o_fun_61/assets/barrel_o_fun_61_gi.png')
bg_off = pygame.image.load('barrel_o_fun_61/assets/barrel_o_fun_61_off.png')

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
        card1_position = [62,779]
        screen.blit(card, card1_position)
    if s.game.selector.position >= 2:
        card2_position = [285,780]
        screen.blit(card, card2_position)
    if s.game.selector.position >= 3:
        card3_position = [515,781]
        screen.blit(card, card3_position)
    if s.game.selector.position >= 4:
        card4_position = [64,1017]
        screen.blit(card, card4_position)
    if s.game.selector.position >= 5:
        card5_position = [289,1021]
        screen.blit(card, card5_position)
    if s.game.selector.position >= 6:
        card6_position = [516,1023]
        screen.blit(card, card6_position)

 
    if s.game.tilt.status == False:
        if s.holes:
            if 1 in s.holes:
                number1_position = [75,588]
                screen.blit(number, number1_position)
                number2_position = [264,697]
                screen.blit(number, number2_position)
                number3_position = [606,732]
                screen.blit(number, number3_position)
                number3_position = [190,831]
                screen.blit(number, number3_position)
                number3_position = [266,976]
                screen.blit(number, number3_position)
                number3_position = [569,830]
                screen.blit(number, number3_position)
            if 2 in s.holes:
                number_position = [114,734]
                screen.blit(number, number_position)
                number_position = [263,662]
                screen.blit(number, number_position)
                number_position = [645,660]
                screen.blit(number, number_position)
                number_position = [190,866]
                screen.blit(number, number_position)
                number_position = [265,866]
                screen.blit(number, number_position)
                number_position = [607,974]
                screen.blit(number, number_position)
            if 3 in s.holes:
                number_position = [189,587]
                screen.blit(number, number_position)
                number_position = [416,735]
                screen.blit(number, number_position)
                number_position = [490,589]
                screen.blit(number, number_position)
                number_position = [115,830]
                screen.blit(number, number_position)
                number_position = [381,973]
                screen.blit(number, number_position)
                number_position = [570,865]
                screen.blit(number, number_position)
            if 4 in s.holes:
                number_position = [152,734]
                screen.blit(number, number_position)
                number_position = [378,588]
                screen.blit(number, number_position)
                number_position = [607,588]
                screen.blit(number, number_position)
                number_position = [154,974]
                screen.blit(number, number_position)
                number_position = [417,832]
                screen.blit(number, number_position)
                number_position = [494,832]
                screen.blit(number, number_position)
            if 5 in s.holes:
                number_position = [38,587]
                screen.blit(number, number_position)
                number_position = [340,733]
                screen.blit(number, number_position)
                number_position = [646,733]
                screen.blit(number, number_position)
                number_position = [40,902]
                screen.blit(number, number_position)
                number_position = [418,902]
                screen.blit(number, number_position)
                number_position = [646,829]
                screen.blit(number, number_position)
            if 6 in s.holes:
                number_position = [38,660]
                screen.blit(number, number_position)
                number_position = [416,589]
                screen.blit(number, number_position)
                number_position = [494,734]
                screen.blit(number, number_position)
                number_position = [39,829]
                screen.blit(number, number_position)
                number_position = [418,974]
                screen.blit(number, number_position)
                number_position = [531,832]
                screen.blit(number, number_position)
            if 7 in s.holes:
                number_position = [188,626]
                screen.blit(number, number_position)
                number_position = [302,733]
                screen.blit(number, number_position)
                number_position = [528,590]
                screen.blit(number, number_position)
                number_position = [77,830]
                screen.blit(number, number_position)
                number_position = [304,975]
                screen.blit(number, number_position)
                number_position = [493,974]
                screen.blit(number, number_position)
            if 8 in s.holes:
                number_position = [39,625]
                screen.blit(number, number_position)
                number_position = [416,698]
                screen.blit(number, number_position)
                number_position = [644,624]
                screen.blit(number, number_position)
                number_position = [191,974]
                screen.blit(number, number_position)
                number_position = [265,831]
                screen.blit(number, number_position)
                number_position = [646,938]
                screen.blit(number, number_position)
            if 9 in s.holes:
                number_position = [111,590]
                screen.blit(number, number_position)
                number_position = [264,589]
                screen.blit(number, number_position)
                number_position = [644,588]
                screen.blit(number, number_position)
                number_position = [118,937]
                screen.blit(number, number_position)
                number_position = [342,940]
                screen.blit(number, number_position)
                number_position = [494,904]
                screen.blit(number, number_position)
            if 10 in s.holes:
                number_position = [113,626]
                screen.blit(number, number_position)
                number_position = [264,736]
                screen.blit(number, number_position)
                number_position = [568,589]
                screen.blit(number, number_position)
                number_position = [42,972]
                screen.blit(number, number_position)
                number_position = [340,832]
                screen.blit(number, number_position)
                number_position = [493,940]
                screen.blit(number, number_position)
            if 11 in s.holes:
                number_position = [152,664]
                screen.blit(number, number_position)
                number_position = [339,700]
                screen.blit(number, number_position)
                number_position = [608,662]
                screen.blit(number, number_position)
                number_position = [42,936]
                screen.blit(number, number_position)
                number_position = [418,939]
                screen.blit(number, number_position)
                number_position = [645,974]
                screen.blit(number, number_position)
            if 12 in s.holes:
                number_position = [39,732]
                screen.blit(number, number_position)
                number_position = [379,662]
                screen.blit(number, number_position)
                number_position = [569,698]
                screen.blit(number, number_position)
                number_position = [116,863]
                screen.blit(number, number_position)
                number_position = [304,902]
                screen.blit(number, number_position)
                number_position = [607,902]
                screen.blit(number, number_position)
            if 13 in s.holes:
                number_position = [189,698]
                screen.blit(number, number_position)
                number_position = [264,626]
                screen.blit(number, number_position)
                number_position = [493,698]
                screen.blit(number, number_position)
                number_position = [79,973]
                screen.blit(number, number_position)
                number_position = [378,832]
                screen.blit(number, number_position)
                number_position = [646,864]
                screen.blit(number, number_position)
            if 14 in s.holes:
                number_position = [114,697]
                screen.blit(number, number_position)
                number_position = [339,626]
                screen.blit(number, number_position)
                number_position = [530,661]
                screen.blit(number, number_position)
                number_position = [76,864]
                screen.blit(number, number_position)
                number_position = [380,868]
                screen.blit(number, number_position)
                number_position = [605,936]
                screen.blit(number, number_position)
            if 15 in s.holes:
                number_position = [190,734]
                screen.blit(number, number_position)
                number_position = [340,661]
                screen.blit(number, number_position)
                number_position = [493,663]
                screen.blit(number, number_position)
                number_position = [154,940]
                screen.blit(number, number_position)
                number_position = [305,940]
                screen.blit(number, number_position)
                number_position = [532,866]
                screen.blit(number, number_position)
            if 16 in s.holes:
                number_position = [114,663]
                screen.blit(number, number_position)
                number_position = [340,589]
                screen.blit(number, number_position)
                number_position = [569,734]
                screen.blit(number, number_position)
                number_position = [154,902]
                screen.blit(number, number_position)
                number_position = [341,867]
                screen.blit(number, number_position)
                number_position = [570,936]
                screen.blit(number, number_position)
            if 17 in s.holes:
                number_position = [188,662]
                screen.blit(number, number_position)
                number_position = [416,662]
                screen.blit(number, number_position)
                number_position = [570,661]
                screen.blit(number, number_position)
                number_position = [81,936]
                screen.blit(number, number_position)
                number_position = [302,867]
                screen.blit(number, number_position)
                number_position = [608,866]
                screen.blit(number, number_position)
            if 18 in s.holes:
                number_position = [78,662]
                screen.blit(number, number_position)
                number_position = [300,662]
                screen.blit(number, number_position)
                number_position = [569,624]
                screen.blit(number, number_position)
                number_position = [154,866]
                screen.blit(number, number_position)
                number_position = [382,940]
                screen.blit(number, number_position)
                number_position = [533,938]
                screen.blit(number, number_position)
            if 19 in s.holes:
                number_position = [150,625]
                screen.blit(number, number_position)
                number_position = [302,626]
                screen.blit(number, number_position)
                number_position = [608,696]
                screen.blit(number, number_position)
                number_position = [78,900]
                screen.blit(number, number_position)
                number_position = [382,902]
                screen.blit(number, number_position)
                number_position = [532,902]
                screen.blit(number, number_position)
            if 20 in s.holes:
                number_position = [152,698]
                screen.blit(number, number_position)
                number_position = [378,626]
                screen.blit(number, number_position)
                number_position = [532,698]
                screen.blit(number, number_position)
                number_position = [116,902]
                screen.blit(number, number_position)
                number_position = [266,902]
                screen.blit(number, number_position)
                number_position = [646,902]
                screen.blit(number, number_position)
            if 21 in s.holes:
                number_position = [77,697]
                screen.blit(number, number_position)
                number_position = [378,698]
                screen.blit(number, number_position)
                number_position = [532,626]
                screen.blit(number, number_position)
                number_position = [118,974]
                screen.blit(number, number_position)
                number_position = [344,976]
                screen.blit(number, number_position)
                number_position = [572,903]
                screen.blit(number, number_position)
            if 22 in s.holes:
                number_position = [76,624]
                screen.blit(number, number_position)
                number_position = [302,698]
                screen.blit(number, number_position)
                number_position = [606,624]
                screen.blit(number, number_position)
                number_position = [190,903]
                screen.blit(number, number_position)
                number_position = [344,904]
                screen.blit(number, number_position)
                number_position = [572,975]
                screen.blit(number, number_position)
            if 23 in s.holes:
                number_position = [76,734]
                screen.blit(number, number_position)
                number_position = [378,735]
                screen.blit(number, number_position)
                number_position = [644,696]
                screen.blit(number, number_position)
                number_position = [41,864]
                screen.blit(number, number_position)
                number_position = [304,834]
                screen.blit(number, number_position)
                number_position = [607,831]
                screen.blit(number, number_position)
            if 24 in s.holes:
                number_position = [40,698]
                screen.blit(number, number_position)
                number_position = [302,590]
                screen.blit(number, number_position)
                number_position = [492,624]
                screen.blit(number, number_position)
                number_position = [152,830]
                screen.blit(number, number_position)
                number_position = [418,869]
                screen.blit(number, number_position)
                number_position = [534,976]
                screen.blit(number, number_position)
            if 25 in s.holes:
                number_position = [151,590]
                screen.blit(number, number_position)
                number_position = [414,626]
                screen.blit(number, number_position)
                number_position = [532,734]
                screen.blit(number, number_position)
                number_position = [190,938]
                screen.blit(number, number_position)
                number_position = [266,940]
                screen.blit(number, number_position)
                number_position = [494,868]
                screen.blit(number, number_position)


    if s.game.tilt.status == True:
        tilt_position = [403,224]
        screen.blit(tilt, tilt_position)

    if s.game.replays:
        digits = [int(d) for d in list(str(s.game.replays))]
        if len(digits) == 3:
            if digits[0] == 1:
                r100_position = [211,262]
                screen.blit(r10000, r100_position)
            elif digits[0] == 2:
                r100_position = [450,332]
                screen.blit(r20000, r100_position)
            if digits[1] != 0:
                if digits[1] == 1:
                    r10_position = [35,529]
                    screen.blit(r1000, r10_position)
                if digits[1] == 2:
                    r10_position = [25,485]
                    screen.blit(r2000, r10_position)
                if digits[1] == 3:
                    r10_position = [18,444]
                    screen.blit(r3000, r10_position)
                if digits[1] == 4:
                    r10_position = [22,396]
                    screen.blit(r4000, r10_position)
                if digits[1] == 5:
                    r10_position = [25,356]
                    screen.blit(r5000, r10_position)
                if digits[1] == 6:
                    r10_position = [32,323]
                    screen.blit(r6000, r10_position)
                if digits[1] == 7:
                    r10_position = [42,286]
                    screen.blit(r7000, r10_position)
                if digits[1] == 8:
                    r10_position = [68,252]
                    screen.blit(r8000, r10_position)
                if digits[1] == 9:
                    r10_position = [102,218]
                    screen.blit(r9000, r10_position)

            if digits[2] != 0:
                if digits[2] == 1:
                    r1_position = [313,534]
                    screen.blit(r100, r1_position)
                if digits[2] == 2:
                    r1_position = [327,493]
                    screen.blit(r200, r1_position)
                if digits[2] == 3:
                    r1_position = [336,451]
                    screen.blit(r300, r1_position)
                if digits[2] == 4:
                    r1_position = [338,414]
                    screen.blit(r400, r1_position)
                if digits[2] == 5:
                    r1_position = [335,371]
                    screen.blit(r500, r1_position)
                if digits[2] == 6:
                    r1_position = [335,338]
                    screen.blit(r600, r1_position)
                if digits[2] == 7:
                    r1_position = [319,298]
                    screen.blit(r700, r1_position)
                if digits[2] == 8:
                    r1_position = [295,263]
                    screen.blit(r800, r1_position)
                if digits[2] == 9:
                    r1_position = [251,233]
                    screen.blit(r900, r1_position)
        if len(digits) == 2:
            if digits[0] != 0:
                if digits[0] == 1:
                    r10_position = [35,529]
                    screen.blit(r1000, r10_position)
                if digits[0] == 2:
                    r10_position = [25,485]
                    screen.blit(r2000, r10_position)
                if digits[0] == 3:
                    r10_position = [18,444]
                    screen.blit(r3000, r10_position)
                if digits[0] == 4:
                    r10_position = [22,396]
                    screen.blit(r4000, r10_position)
                if digits[0] == 5:
                    r10_position = [25,356]
                    screen.blit(r5000, r10_position)
                if digits[0] == 6:
                    r10_position = [32,323]
                    screen.blit(r6000, r10_position)
                if digits[0] == 7:
                    r10_position = [42,286]
                    screen.blit(r7000, r10_position)
                if digits[0] == 8:
                    r10_position = [68,252]
                    screen.blit(r8000, r10_position)
                if digits[0] == 9:
                    r10_position = [102,218]
                    screen.blit(r9000, r10_position)

            if digits[1] != 0:
                if digits[1] == 1:
                    r1_position = [313,534]
                    screen.blit(r100, r1_position)
                if digits[1] == 2:
                    r1_position = [327,493]
                    screen.blit(r200, r1_position)
                if digits[1] == 3:
                    r1_position = [336,451]
                    screen.blit(r300, r1_position)
                if digits[1] == 4:
                    r1_position = [338,414]
                    screen.blit(r400, r1_position)
                if digits[1] == 5:
                    r1_position = [335,371]
                    screen.blit(r500, r1_position)
                if digits[1] == 6:
                    r1_position = [335,338]
                    screen.blit(r600, r1_position)
                if digits[1] == 7:
                    r1_position = [319,298]
                    screen.blit(r700, r1_position)
                if digits[1] == 8:
                    r1_position = [295,263]
                    screen.blit(r800, r1_position)
                if digits[1] == 9:
                    r1_position = [251,233]
                    screen.blit(r900, r1_position)

        if len(digits) == 1:
            if digits[0] != 0:
                if digits[0] == 1:
                    r1_position = [313,534]
                    screen.blit(r100, r1_position)
                if digits[0] == 2:
                    r1_position = [327,493]
                    screen.blit(r200, r1_position)
                if digits[0] == 3:
                    r1_position = [336,451]
                    screen.blit(r300, r1_position)
                if digits[0] == 4:
                    r1_position = [338,414]
                    screen.blit(r400, r1_position)
                if digits[0] == 5:
                    r1_position = [335,371]
                    screen.blit(r500, r1_position)
                if digits[0] == 6:
                    r1_position = [335,338]
                    screen.blit(r600, r1_position)
                if digits[0] == 7:
                    r1_position = [319,298]
                    screen.blit(r700, r1_position)
                if digits[0] == 8:
                    r1_position = [295,263]
                    screen.blit(r800, r1_position)
                if digits[0] == 9:
                    r1_position = [251,233]
                    screen.blit(r900, r1_position)

    pygame.display.update()
