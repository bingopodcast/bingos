import pygame

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

card = pygame.image.load('fun_way/assets/card.png').convert_alpha()
number = pygame.image.load('fun_way/assets/number.png').convert_alpha()
tilt = pygame.image.load('fun_way/assets/tilt.png').convert_alpha()
r10000 = pygame.image.load('fun_way/assets/10000.png').convert_alpha()
r20000 = pygame.image.load('fun_way/assets/20000.png').convert_alpha()
r1000 = pygame.image.load('fun_way/assets/1000.png').convert_alpha()
r2000 = pygame.image.load('fun_way/assets/2000.png').convert_alpha()
r3000 = pygame.image.load('fun_way/assets/3000.png').convert_alpha()
r4000 = pygame.image.load('fun_way/assets/4000.png').convert_alpha()
r5000 = pygame.image.load('fun_way/assets/5000.png').convert_alpha()
r6000 = pygame.image.load('fun_way/assets/6000.png').convert_alpha()
r7000 = pygame.image.load('fun_way/assets/7000.png').convert_alpha()
r8000 = pygame.image.load('fun_way/assets/8000.png').convert_alpha()
r9000 = pygame.image.load('fun_way/assets/9000.png').convert_alpha()
r100 = pygame.image.load('fun_way/assets/100.png').convert_alpha()
r200 = pygame.image.load('fun_way/assets/200.png').convert_alpha()
r300 = pygame.image.load('fun_way/assets/300.png').convert_alpha()
r400 = pygame.image.load('fun_way/assets/400.png').convert_alpha()
r500 = pygame.image.load('fun_way/assets/500.png').convert_alpha()
r600 = pygame.image.load('fun_way/assets/600.png').convert_alpha()
r700 = pygame.image.load('fun_way/assets/700.png').convert_alpha()
r800 = pygame.image.load('fun_way/assets/800.png').convert_alpha()
r900 = pygame.image.load('fun_way/assets/900.png').convert_alpha()

def display(s, replays=0, menu=False):

    backglass_position = [0, 0]
    backglass = pygame.Surface(screen.get_size(), flags=pygame.SRCALPHA)
    backglass.fill((0, 0, 0))
    if menu == True:
        backglass = pygame.image.load('fun_way/assets/fun_way_menu.png')
    else:
        if (s.game.anti_cheat.status == True):
            backglass = pygame.image.load('fun_way/assets/fun_way_gi.png')
        else:
            backglass = pygame.image.load('fun_way/assets/fun_way_off.png')
    backglass = pygame.transform.scale(backglass, (720, 1280))
    
    screen.blit(backglass, backglass_position)

    if s.game.selector.position >= 1:
        card1_position = [88,765]
        screen.blit(card, card1_position)
    if s.game.selector.position >= 2:
        card2_position = [288,765]
        screen.blit(card, card2_position)
    if s.game.selector.position >= 3:
        card3_position = [492,765]
        screen.blit(card, card3_position)
    if s.game.selector.position >= 4:
        card4_position = [90,993]
        screen.blit(card, card4_position)
    if s.game.selector.position >= 5:
        card5_position = [290,993]
        screen.blit(card, card5_position)
    if s.game.selector.position >= 6:
        card6_position = [492,993]
        screen.blit(card, card6_position)

    if s.game.tilt.status == False:
        if s.holes:
            if 1 in s.holes:
                number_position = [102,582]
                screen.blit(number, number_position)
                number_position = [270,688]
                screen.blit(number, number_position)
                number_position = [578,723]
                screen.blit(number, number_position)
                number_position = [207,815]
                screen.blit(number, number_position)
                number_position = [271,954]
                screen.blit(number, number_position)
                number_position = [542,814]
                screen.blit(number, number_position)
            if 2 in s.holes:
                number_position = [137,722]
                screen.blit(number, number_position)
                number_position = [270,652]
                screen.blit(number, number_position)
                number_position = [613,651]
                screen.blit(number, number_position)
                number_position = [206,848]
                screen.blit(number, number_position)
                number_position = [272,849]
                screen.blit(number, number_position)
                number_position = [577,951]
                screen.blit(number, number_position)
            if 3 in s.holes:
                number_position = [207,581]
                screen.blit(number, number_position)
                number_position = [410,721]
                screen.blit(number, number_position)
                number_position = [474,580]
                screen.blit(number, number_position)
                number_position = [137,811]
                screen.blit(number, number_position)
                number_position = [375,953]
                screen.blit(number, number_position)
                number_position = [542,849]
                screen.blit(number, number_position)
            if 4 in s.holes:
                number_position = [172,723]
                screen.blit(number, number_position)
                number_position = [374,580]
                screen.blit(number, number_position)
                number_position = [578,580]
                screen.blit(number, number_position)
                number_position = [174,954]
                screen.blit(number, number_position)
                number_position = [410,811]
                screen.blit(number, number_position)
                number_position = [475,814]
                screen.blit(number, number_position)
            if 5 in s.holes:
                number_position = [66,581]
                screen.blit(number, number_position)
                number_position = [340,724]
                screen.blit(number, number_position)
                number_position = [612,723]
                screen.blit(number, number_position)
                number_position = [68,884]
                screen.blit(number, number_position)
                number_position = [409,883]
                screen.blit(number, number_position)
                number_position = [611,814]
                screen.blit(number, number_position)
            if 6 in s.holes:
                number_position = [68,653]
                screen.blit(number, number_position)
                number_position = [410,580]
                screen.blit(number, number_position)
                number_position = [474,723]
                screen.blit(number, number_position)
                number_position = [68,813]
                screen.blit(number, number_position)
                number_position = [409,954]
                screen.blit(number, number_position)
                number_position = [508,814]
                screen.blit(number, number_position)
            if 7 in s.holes:
                number_position = [206,616]
                screen.blit(number, number_position)
                number_position = [306,724]
                screen.blit(number, number_position)
                number_position = [509,582]
                screen.blit(number, number_position)
                number_position = [103,814]
                screen.blit(number, number_position)
                number_position = [307,954]
                screen.blit(number, number_position)
                number_position = [474,955]
                screen.blit(number, number_position)
            if 8 in s.holes:
                number_position = [67,617]
                screen.blit(number, number_position)
                number_position = [409,688]
                screen.blit(number, number_position)
                number_position = [613,617]
                screen.blit(number, number_position)
                number_position = [208,954]
                screen.blit(number, number_position)
                number_position = [271,814]
                screen.blit(number, number_position)
                number_position = [611,919]
                screen.blit(number, number_position)
            if 9 in s.holes:
                number_position = [137,582]
                screen.blit(number, number_position)
                number_position = [271,581]
                screen.blit(number, number_position)
                number_position = [614,583]
                screen.blit(number, number_position)
                number_position = [139,920]
                screen.blit(number, number_position)
                number_position = [342,920]
                screen.blit(number, number_position)
                number_position = [474,884]
                screen.blit(number, number_position)
            if 10 in s.holes:
                number_position = [138,618]
                screen.blit(number, number_position)
                number_position = [271,724]
                screen.blit(number, number_position)
                number_position = [544,582]
                screen.blit(number, number_position)
                number_position = [70,955]
                screen.blit(number, number_position)
                number_position = [341,813]
                screen.blit(number, number_position)
                number_position = [475,918]
                screen.blit(number, number_position)
            if 11 in s.holes:
                number_position = [173,653]
                screen.blit(number, number_position)
                number_position = [340,689]
                screen.blit(number, number_position)
                number_position = [578,653]
                screen.blit(number, number_position)
                number_position = [68,919]
                screen.blit(number, number_position)
                number_position = [410,919]
                screen.blit(number, number_position)
                number_position = [611,953]
                screen.blit(number, number_position)
            if 12 in s.holes:
                number_position = [68,724]
                screen.blit(number, number_position)
                number_position = [376,652]
                screen.blit(number, number_position)
                number_position = [544,688]
                screen.blit(number, number_position)
                number_position = [139,849]
                screen.blit(number, number_position)
                number_position = [307,884]
                screen.blit(number, number_position)
                number_position = [578,884]
                screen.blit(number, number_position)
            if 13 in s.holes:
                number_position = [207,689]
                screen.blit(number, number_position)
                number_position = [272,618]
                screen.blit(number, number_position)
                number_position = [475,690]
                screen.blit(number, number_position)
                number_position = [105,955]
                screen.blit(number, number_position)
                number_position = [376,814]
                screen.blit(number, number_position)
                number_position = [613,849]
                screen.blit(number, number_position)
            if 14 in s.holes:
                number_position = [138,690]
                screen.blit(number, number_position)
                number_position = [340,619]
                screen.blit(number, number_position)
                number_position = [511,652]
                screen.blit(number, number_position)
                number_position = [104,850]
                screen.blit(number, number_position)
                number_position = [374,850]
                screen.blit(number, number_position)
                number_position = [577,919]
                screen.blit(number, number_position)
            if 15 in s.holes:
                number_position = [208,725]
                screen.blit(number, number_position)
                number_position = [341,653]
                screen.blit(number, number_position)
                number_position = [476,654]
                screen.blit(number, number_position)
                number_position = [174,920]
                screen.blit(number, number_position)
                number_position = [306,920]
                screen.blit(number, number_position)
                number_position = [510,849]
                screen.blit(number, number_position)
            if 16 in s.holes:
                number_position = [138,654]
                screen.blit(number, number_position)
                number_position = [341,581]
                screen.blit(number, number_position)
                number_position = [544,723]
                screen.blit(number, number_position)
                number_position = [174,884]
                screen.blit(number, number_position)
                number_position = [341,850]
                screen.blit(number, number_position)
                number_position = [543,920]
                screen.blit(number, number_position)
            if 17 in s.holes:
                number_position = [207,654]
                screen.blit(number, number_position)
                number_position = [411,653]
                screen.blit(number, number_position)
                number_position = [545,653]
                screen.blit(number, number_position)
                number_position = [105,920]
                screen.blit(number, number_position)
                number_position = [307,849]
                screen.blit(number, number_position)
                number_position = [579,850]
                screen.blit(number, number_position)
            if 18 in s.holes:
                number_position = [103,653]
                screen.blit(number, number_position)
                number_position = [308,654]
                screen.blit(number, number_position)
                number_position = [546,618]
                screen.blit(number, number_position)
                number_position = [173,850]
                screen.blit(number, number_position)
                number_position = [375,919]
                screen.blit(number, number_position)
                number_position = [510,920]
                screen.blit(number, number_position)
            if 19 in s.holes:
                number_position = [173,618]
                screen.blit(number, number_position)
                number_position = [307,617]
                screen.blit(number, number_position)
                number_position = [580,688]
                screen.blit(number, number_position)
                number_position = [105,884]
                screen.blit(number, number_position)
                number_position = [376,884]
                screen.blit(number, number_position)
                number_position = [510,885]
                screen.blit(number, number_position)
            if 20 in s.holes:
                number_position = [173,688]
                screen.blit(number, number_position)
                number_position = [376,619]
                screen.blit(number, number_position)
                number_position = [511,690]
                screen.blit(number, number_position)
                number_position = [138,885]
                screen.blit(number, number_position)
                number_position = [273,885]
                screen.blit(number, number_position)
                number_position = [612,885]
                screen.blit(number, number_position)
            if 21 in s.holes:
                number_position = [103,688]
                screen.blit(number, number_position)
                number_position = [375,688]
                screen.blit(number, number_position)
                number_position = [510,618]
                screen.blit(number, number_position)
                number_position = [139,954]
                screen.blit(number, number_position)
                number_position = [342,955]
                screen.blit(number, number_position)
                number_position = [543,885]
                screen.blit(number, number_position)
            if 22 in s.holes:
                number_position = [103,617]
                screen.blit(number, number_position)
                number_position = [308,689]
                screen.blit(number, number_position)
                number_position = [580,617]
                screen.blit(number, number_position)
                number_position = [209,885]
                screen.blit(number, number_position)
                number_position = [343,885]
                screen.blit(number, number_position)
                number_position = [544,954]
                screen.blit(number, number_position)
            if 23 in s.holes:
                number_position = [104,724]
                screen.blit(number, number_position)
                number_position = [377,724]
                screen.blit(number, number_position)
                number_position = [614,689]
                screen.blit(number, number_position)
                number_position = [71,850]
                screen.blit(number, number_position)
                number_position = [307,815]
                screen.blit(number, number_position)
                number_position = [577,814]
                screen.blit(number, number_position)
            if 24 in s.holes:
                number_position = [69,689]
                screen.blit(number, number_position)
                number_position = [307,581]
                screen.blit(number, number_position)
                number_position = [475,618]
                screen.blit(number, number_position)
                number_position = [173,815]
                screen.blit(number, number_position)
                number_position = [410,849]
                screen.blit(number, number_position)
                number_position = [508,954]
                screen.blit(number, number_position)
            if 25 in s.holes:
                number_position = [171,581]
                screen.blit(number, number_position)
                number_position = [411,617]
                screen.blit(number, number_position)
                number_position = [512,724]
                screen.blit(number, number_position)
                number_position = [208,920]
                screen.blit(number, number_position)
                number_position = [273,919]
                screen.blit(number, number_position)
                number_position = [476,850]
                screen.blit(number, number_position)

    if s.game.tilt.status == True:
        tilt_position = [58,271]
        screen.blit(tilt, tilt_position)

    if s.game.replays:
        digits = [int(d) for d in list(str(s.game.replays))]
        if len(digits) == 3:
            if digits[0] == 1:
                r100_position = [345,386]
                screen.blit(r10000, r100_position)
            elif digits[0] == 2:
                r100_position = [488,385]
                screen.blit(r20000, r100_position)
            if digits[1] != 0:
                if digits[1] == 1:
                    r10_position = [158,384]
                    screen.blit(r1000, r10_position)
                if digits[1] == 2:
                    r10_position = [213,362]
                    screen.blit(r2000, r10_position)
                if digits[1] == 3:
                    r10_position = [273,349]
                    screen.blit(r3000, r10_position)
                if digits[1] == 4:
                    r10_position = [331,338]
                    screen.blit(r4000, r10_position)
                if digits[1] == 5:
                    r10_position = [394,332]
                    screen.blit(r5000, r10_position)
                if digits[1] == 6:
                    r10_position = [455,330]
                    screen.blit(r6000, r10_position)
                if digits[1] == 7:
                    r10_position = [516,329]
                    screen.blit(r7000, r10_position)
                if digits[1] == 8:
                    r10_position = [580,330]
                    screen.blit(r8000, r10_position)
                if digits[1] == 9:
                    r10_position = [642,334]
                    screen.blit(r9000, r10_position)

            if digits[2] != 0:
                if digits[2] == 1:
                    r1_position = [139,343]
                    screen.blit(r100, r1_position)
                if digits[2] == 2:
                    r1_position = [200,322]
                    screen.blit(r200, r1_position)
                if digits[2] == 3:
                    r1_position = [264,305]
                    screen.blit(r300, r1_position)
                if digits[2] == 4:
                    r1_position = [329,293]
                    screen.blit(r400, r1_position)
                if digits[2] == 5:
                    r1_position = [389,284]
                    screen.blit(r500, r1_position)
                if digits[2] == 6:
                    r1_position = [456,280]
                    screen.blit(r600, r1_position)
                if digits[2] == 7:
                    r1_position = [519,280]
                    screen.blit(r700, r1_position)
                if digits[2] == 8:
                    r1_position = [584,283]
                    screen.blit(r800, r1_position)
                if digits[2] == 9:
                    r1_position = [649,285]
                    screen.blit(r900, r1_position)
        if len(digits) == 2:
            if digits[0] != 0:
                if digits[0] == 1:
                    r10_position = [158,384]
                    screen.blit(r1000, r10_position)
                if digits[0] == 2:
                    r10_position = [213,362]
                    screen.blit(r2000, r10_position)
                if digits[0] == 3:
                    r10_position = [273,349]
                    screen.blit(r3000, r10_position)
                if digits[0] == 4:
                    r10_position = [331,338]
                    screen.blit(r4000, r10_position)
                if digits[0] == 5:
                    r10_position = [394,332]
                    screen.blit(r5000, r10_position)
                if digits[0] == 6:
                    r10_position = [455,330]
                    screen.blit(r6000, r10_position)
                if digits[0] == 7:
                    r10_position = [516,329]
                    screen.blit(r7000, r10_position)
                if digits[0] == 8:
                    r10_position = [580,330]
                    screen.blit(r8000, r10_position)
                if digits[0] == 9:
                    r10_position = [642,334]
                    screen.blit(r9000, r10_position)

            if digits[1] != 0:
                if digits[1] == 1:
                    r1_position = [139,343]
                    screen.blit(r100, r1_position)
                if digits[1] == 2:
                    r1_position = [200,322]
                    screen.blit(r200, r1_position)
                if digits[1] == 3:
                    r1_position = [264,305]
                    screen.blit(r300, r1_position)
                if digits[1] == 4:
                    r1_position = [329,293]
                    screen.blit(r400, r1_position)
                if digits[1] == 5:
                    r1_position = [389,284]
                    screen.blit(r500, r1_position)
                if digits[1] == 6:
                    r1_position = [456,280]
                    screen.blit(r600, r1_position)
                if digits[1] == 7:
                    r1_position = [519,280]
                    screen.blit(r700, r1_position)
                if digits[1] == 8:
                    r1_position = [584,283]
                    screen.blit(r800, r1_position)
                if digits[1] == 9:
                    r1_position = [649,285]
                    screen.blit(r900, r1_position)

        if len(digits) == 1:
            if digits[0] != 0:
                if digits[0] == 1:
                    r1_position = [139,343]
                    screen.blit(r100, r1_position)
                if digits[0] == 2:
                    r1_position = [200,322]
                    screen.blit(r200, r1_position)
                if digits[0] == 3:
                    r1_position = [264,305]
                    screen.blit(r300, r1_position)
                if digits[0] == 4:
                    r1_position = [329,293]
                    screen.blit(r400, r1_position)
                if digits[0] == 5:
                    r1_position = [389,284]
                    screen.blit(r500, r1_position)
                if digits[0] == 6:
                    r1_position = [456,280]
                    screen.blit(r600, r1_position)
                if digits[0] == 7:
                    r1_position = [519,280]
                    screen.blit(r700, r1_position)
                if digits[0] == 8:
                    r1_position = [584,283]
                    screen.blit(r800, r1_position)
                if digits[0] == 9:
                    r1_position = [649,285]
                    screen.blit(r900, r1_position)

    pygame.display.update()


