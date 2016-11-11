import pygame

pygame.display.set_caption("Barrel O Fun")
screen = pygame.display.set_mode((720,1280))
screen.fill([0,0,0])
        
card1_display = pygame.image.load('barrel_o_fun/assets/barrel_o_fun_card_1.png').convert_alpha()
card2_display = pygame.image.load('barrel_o_fun/assets/barrel_o_fun_card_2.png').convert_alpha()
card3_display = pygame.image.load('barrel_o_fun/assets/barrel_o_fun_card_3.png').convert_alpha()
card4_display = pygame.image.load('barrel_o_fun/assets/barrel_o_fun_card_4.png').convert_alpha()

def display(s, replays=0, menu=False):

    backglass_position = [0, 0]
    backglass = pygame.Surface(screen.get_size(), flags=pygame.SRCALPHA)
    backglass.fill((0, 0, 0))
    if menu == True:
        backglass = pygame.image.load('barrel_o_fun/assets/barrel_o_fun_menu.png')
    else:
        if (s.game.anti_cheat.status == True):
            backglass = pygame.image.load('barrel_o_fun/assets/barrel_o_fun_gi.png')
        else:
            backglass = pygame.image.load('barrel_o_fun/assets/barrel_o_fun_off.png')
    backglass = pygame.transform.scale(backglass, (720, 1280))
    
    screen.blit(backglass, backglass_position)

    if s.game.selector.position >= 1:
        card1_position = [0,0]
        screen.blit(card1_display, card1_position)
    if s.game.selector.position >= 2:
        card2_position = [0,0]
        screen.blit(card2_display, card2_position)
    if s.game.selector.position >= 3:
        card3_position = [0,0]
        screen.blit(card3_display, card3_position)
    if s.game.selector.position >= 4:
        card4_position = [0,0]
        screen.blit(card4_display, card4_position)
    if s.game.selector.position >= 5:
        card5_position = [0,0]
        card5_display = pygame.image.load('barrel_o_fun/assets/barrel_o_fun_card_5.png').convert_alpha()
        screen.blit(card5_display, card5_position)
    if s.game.selector.position >= 6:
        card6_position = [0,0]
        card6_display = pygame.image.load('barrel_o_fun/assets/barrel_o_fun_card_6.png').convert_alpha()
        screen.blit(card6_display, card6_position)

 
    if game.tilt.status == False:
        if numbers:
            if 1 in numbers:
                number_position = [0,0]
                number = pygame.image.load('barrel_o_fun/assets/barrel_o_fun_1.png').convert_alpha()
                screen.blit(number, number_position)
            if 2 in numbers:
                number_position = [0,0]
                number = pygame.image.load('barrel_o_fun/assets/barrel_o_fun_2.png').convert_alpha()
                screen.blit(number, number_position)
            if 3 in numbers:
                number_position = [0,0]
                number = pygame.image.load('barrel_o_fun/assets/barrel_o_fun_3.png').convert_alpha()
                screen.blit(number, number_position)
            if 4 in numbers:
                number_position = [0,0]
                number = pygame.image.load('barrel_o_fun/assets/barrel_o_fun_4.png').convert_alpha()
                screen.blit(number, number_position)
            if 5 in numbers:
                number_position = [0,0]
                number = pygame.image.load('barrel_o_fun/assets/barrel_o_fun_5.png').convert_alpha()
                screen.blit(number, number_position)
            if 6 in numbers:
                number_position = [0,0]
                number = pygame.image.load('barrel_o_fun/assets/barrel_o_fun_6.png').convert_alpha()
                screen.blit(number, number_position)
            if 7 in numbers:
                number_position = [0,0]
                number = pygame.image.load('barrel_o_fun/assets/barrel_o_fun_7.png').convert_alpha()
                screen.blit(number, number_position)
            if 8 in numbers:
                number_position = [0,0]
                number = pygame.image.load('barrel_o_fun/assets/barrel_o_fun_8.png').convert_alpha()
                screen.blit(number, number_position)
            if 9 in numbers:
                number_position = [0,0]
                number = pygame.image.load('barrel_o_fun/assets/barrel_o_fun_9.png').convert_alpha()
                screen.blit(number, number_position)
            if 10 in numbers:
                number_position = [0,0]
                number = pygame.image.load('barrel_o_fun/assets/barrel_o_fun_10.png').convert_alpha()
                screen.blit(number, number_position)
            if 11 in numbers:
                number_position = [0,0]
                number = pygame.image.load('barrel_o_fun/assets/barrel_o_fun_11.png').convert_alpha()
                screen.blit(number, number_position)
            if 12 in numbers:
                number_position = [0,0]
                number = pygame.image.load('barrel_o_fun/assets/barrel_o_fun_12.png').convert_alpha()
                screen.blit(number, number_position)
            if 13 in numbers:
                number_position = [0,0]
                number = pygame.image.load('barrel_o_fun/assets/barrel_o_fun_13.png').convert_alpha()
                screen.blit(number, number_position)
            if 14 in numbers:
                number_position = [0,0]
                number = pygame.image.load('barrel_o_fun/assets/barrel_o_fun_14.png').convert_alpha()
                screen.blit(number, number_position)
            if 15 in numbers:
                number_position = [0,0]
                number = pygame.image.load('barrel_o_fun/assets/barrel_o_fun_15.png').convert_alpha()
                screen.blit(number, number_position)
            if 16 in numbers:
                number_position = [0,0]
                number = pygame.image.load('barrel_o_fun/assets/barrel_o_fun_16.png').convert_alpha()
                screen.blit(number, number_position)
            if 17 in numbers:
                number_position = [0,0]
                number = pygame.image.load('barrel_o_fun/assets/barrel_o_fun_17.png').convert_alpha()
                screen.blit(number, number_position)
            if 18 in numbers:
                number_position = [0,0]
                number = pygame.image.load('barrel_o_fun/assets/barrel_o_fun_18.png').convert_alpha()
                screen.blit(number, number_position)
            if 19 in numbers:
                number_position = [0,0]
                number = pygame.image.load('barrel_o_fun/assets/barrel_o_fun_19.png').convert_alpha()
                screen.blit(number, number_position)
            if 20 in numbers:
                number_position = [0,0]
                number = pygame.image.load('barrel_o_fun/assets/barrel_o_fun_20.png').convert_alpha()
                screen.blit(number, number_position)
            if 21 in numbers:
                number_position = [0,0]
                number = pygame.image.load('barrel_o_fun/assets/barrel_o_fun_21.png').convert_alpha()
                screen.blit(number, number_position)
            if 22 in numbers:
                number_position = [0,0]
                number = pygame.image.load('barrel_o_fun/assets/barrel_o_fun_22.png').convert_alpha()
                screen.blit(number, number_position)
            if 23 in numbers:
                number_position = [0,0]
                number = pygame.image.load('barrel_o_fun/assets/barrel_o_fun_23.png').convert_alpha()
                screen.blit(number, number_position)
            if 24 in numbers:
                number_position = [0,0]
                number = pygame.image.load('barrel_o_fun/assets/barrel_o_fun_24.png').convert_alpha()
                screen.blit(number, number_position)
            if 25 in numbers:
                number_position = [0,0]
                number = pygame.image.load('barrel_o_fun/assets/barrel_o_fun_25.png').convert_alpha()
                screen.blit(number, number_position)


    if game.tilt.status == True:
        tilt_position = [0,0]
        tilt = pygame.image.load('barrel_o_fun/assets/barrel_o_fun_tilt.png').convert_alpha()
        screen.blit(tilt, tilt_position)

    if replays:
        digits = [int(d) for d in list(str(replays))]
        if len(digits) == 3:
            r100_position = [0,0]
            r100_display = pygame.image.load('barrel_o_fun/assets/barrel_o_fun_replay_' + str(digits[0]) + '00.png').convert_alpha()
            screen.blit(r100_display, r100_position)
            if digits[1] != 0:
                r10_position = [0,0]
                r10_display = pygame.image.load('barrel_o_fun/assets/barrel_o_fun_replay_' + str(digits[1]) + '0.png').convert_alpha()
                screen.blit(r10_display, r10_position)
            r1_position = [0,0]
            r1_display = pygame.image.load('barrel_o_fun/assets/barrel_o_fun_replay_' + str(digits[2]) + '.png').convert_alpha()
            screen.blit(r1_display, r1_position)
        if len(digits) == 2:
            r10_position = [0,0]
            r10_display = pygame.image.load('barrel_o_fun/assets/barrel_o_fun_replay_' + str(digits[0]) + '0.png').convert_alpha()
            r1_position = [0,0]
            r1_display = pygame.image.load('barrel_o_fun/assets/barrel_o_fun_replay_' + str(digits[1]) + '.png').convert_alpha()
            screen.blit(r10_display, r10_position)
            screen.blit(r1_display, r1_position)
        if len(digits) == 1:
            r1_position = [0,0]
            r1_display = pygame.image.load('barrel_o_fun/assets/barrel_o_fun_replay_' + str(digits[0]) + '.png').convert_alpha()
            screen.blit(r1_display, r1_position)

    pygame.display.flip()
    pygame.display.update()

    
