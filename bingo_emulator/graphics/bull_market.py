
import pygame

pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

meter = pygame.image.load('graphics/assets/black_register_cover.png').convert()
card = pygame.image.load('bull_market/assets/card.png').convert_alpha()
feature = pygame.image.load('bull_market/assets/feature.png').convert_alpha()
select = pygame.image.load('bull_market/assets/select.png').convert_alpha()
number = pygame.image.load('bull_market/assets/number.png').convert_alpha()
corners = pygame.image.load('bull_market/assets/corners.png').convert_alpha()
super_line = pygame.image.load('bull_market/assets/super_line.png').convert_alpha()
c = pygame.image.load('bull_market/assets/regular.png').convert_alpha()
d = pygame.image.load('bull_market/assets/double.png').convert_alpha()
n = pygame.image.load('bull_market/assets/nothing.png').convert_alpha()
tilt = pygame.image.load('bull_market/assets/tilt.png').convert_alpha()
blink_image = pygame.image.load('bull_market/assets/double_or_nothing.png').convert_alpha()


class scorereel():
    """ Score Reels are used to count replays """
    def __init__(self, pos, image):
        self.position = pos
        self.default_y = self.position[1]
        self.image = pygame.image.load(image).convert()

reel1 = scorereel([375,652], "graphics/assets/white_reel.png")
reel10 = scorereel([357,652], "graphics/assets/white_reel.png")
reel100 = scorereel([338,652], "graphics/assets/white_reel.png")
reel1000 = scorereel([318,652], "graphics/assets/white_reel.png")

def display(s, replays=0, menu=False):
    
    meter.set_colorkey((255,0,252))
    meter_position = [309,652]

    screen.blit(reel1.image, reel1.position)
    screen.blit(reel10.image, reel10.position)
    screen.blit(reel100.image, reel100.position)
    screen.blit(reel1000.image, reel1000.position)
    screen.blit(meter, meter_position)

    backglass_position = [0, 0]
    backglass = pygame.Surface((720,1280), pygame.SRCALPHA | pygame.FULLSCREEN)
    backglass.fill((0, 0, 0))
    if menu == True:
        backglass = pygame.image.load('bull_market/assets/bull_market_menu.png')
    else:
        if (s.game.anti_cheat.status == True):
            backglass = pygame.image.load('bull_market/assets/bull_market_gi.png')
        else:
            backglass = pygame.image.load('bull_market/assets/bull_market_off.png')
    #backglass = pygame.transform.scale(backglass, (1280,720))
    screen.blit(backglass, backglass_position)

    if s.game.selector.position >= 1:
        position = [121,383]
        screen.blit(card, position)
    if s.game.selector.position >= 2:
        position = [348,364]
        screen.blit(card, position)
    if s.game.selector.position >= 3:
        position = [575,386]
        screen.blit(card, position)
    if s.game.selector.position >= 4:
        position = [123,763]
        screen.blit(card, position)
    if s.game.selector.position >= 5:
        position = [350,779]
        screen.blit(card, position)
    if s.game.selector.position >= 6:
        position = [574,766]
        screen.blit(card, position)

    if s.game.before_third.status == True:
        p = [17,672]
        screen.blit(feature, p)

    if s.game.before_fourth.status == True:
        p = [17,632]
        screen.blit(feature, p)

    if s.game.before_fourth.status == True:
        if s.game.ball_count.position == 3:
            p = [17,713]
            screen.blit(select, p)
    elif s.game.before_third.status == True:
        if s.game.ball_count.position == 2:
            p = [17,713]
            screen.blit(select, p)

    if s.game.before_fourth.status == True or s.game.before_third.status == True:
        if s.game.spotting.position == 0:
            p = [131,682]
            screen.blit(number, p)
        elif s.game.spotting.position == 1:
            p = [162,682]
            screen.blit(number, p)
        elif s.game.spotting.position == 2:
            p = [193,683]
            screen.blit(number, p)
        elif s.game.spotting.position == 3:
            p = [132,711]
            screen.blit(number, p)
        elif s.game.spotting.position == 4:
            p = [162,711]
            screen.blit(number, p)
        elif s.game.spotting.position == 5:
            p = [192,711]
            screen.blit(number, p)
        

    if s.game.tilt.status == False:
        if s.holes:
            if 1 in s.holes:
                position = [93,448]
                screen.blit(number, position)
                position = [289,525]
                screen.blit(number, position)
                position = [646,451]
                screen.blit(number, position)
                position = [160,957]
                screen.blit(number, position)
                position = [354,843]
                screen.blit(number, position)
                position = [515,957]
                screen.blit(number, position)
            if 2 in s.holes:
                position = [127,576]
                screen.blit(number, position)
                position = [288,493]
                screen.blit(number, position)
                position = [645,484]
                screen.blit(number, position)
                position = [194,891]
                screen.blit(number, position)
                position = [387,970]
                screen.blit(number, position)
                position = [514,862]
                screen.blit(number, position)
            if 3 in s.holes:
                position = [192,449]
                screen.blit(number, position)
                position = [419,558]
                screen.blit(number, position)
                position = [579,451]
                screen.blit(number, position)
                position = [61,829]
                screen.blit(number, position)
                position = [289,874]
                screen.blit(number, position)
                position = [613,959]
                screen.blit(number, position)
            if 4 in s.holes:
                position = [161,577]
                screen.blit(number, position)
                position = [386,431]
                screen.blit(number, position)
                position = [612,579]
                screen.blit(number, position)
                position = [160,828]
                screen.blit(number, position)
                position = [289,843]
                screen.blit(number, position)
                position = [644,831]
                screen.blit(number, position)
            if 5 in s.holes:
                position = [59,448]
                screen.blit(number, position)
                position = [354,557]
                screen.blit(number, position)
                position = [513,516]
                screen.blit(number, position)
                position = [193,955]
                screen.blit(number, position)
                position = [420,843]
                screen.blit(number, position)
                position = [646,895]
                screen.blit(number, position)
            if 6 in s.holes:
                position = [59,511]
                screen.blit(number, position)
                position = [418,431]
                screen.blit(number, position)
                position = [514,452]
                screen.blit(number, position)
                position = [60,956]
                screen.blit(number, position)
                position = [321,843]
                screen.blit(number, position)
                position = [646,959]
                screen.blit(number, position)
            if 7 in s.holes:
                position = [193,481]
                screen.blit(number, position)
                position = [322,557]
                screen.blit(number, position)
                position = [547,452]
                screen.blit(number, position)
                position = [94,828]
                screen.blit(number, position)
                position = [289,970]
                screen.blit(number, position)
                position = [548,958]
                screen.blit(number, position)
            if 8 in s.holes:
                position = [60,479]
                screen.blit(number, position)
                position = [419,527]
                screen.blit(number, position)
                position = [645,579]
                screen.blit(number, position)
                position = [193,859]
                screen.blit(number, position)
                position = [420,939]
                screen.blit(number, position)
                position = [514,830]
                screen.blit(number, position)
            if 9 in s.holes:
                position = [126,447]
                screen.blit(number, position)
                position = [288,429]
                screen.blit(number, position)
                position = [579,548]
                screen.blit(number, position)
                position = [194,828]
                screen.blit(number, position)
                position = [288,906]
                screen.blit(number, position)
                position = [580,926]
                screen.blit(number, position)
            if 10 in s.holes:
                position = [126,480]
                screen.blit(number, position)
                position = [290,557]
                screen.blit(number, position)
                position = [514,579]
                screen.blit(number, position)
                position = [128,828]
                screen.blit(number, position)
                position = [289,938]
                screen.blit(number, position)
                position = [579,830]
                screen.blit(number, position)
            if 11 in s.holes:
                position = [160,512]
                screen.blit(number, position)
                position = [354,526]
                screen.blit(number, position)
                position = [514,547]
                screen.blit(number, position)
                position = [160,891]
                screen.blit(number, position)
                position = [420,971]
                screen.blit(number, position)
                position = [647,927]
                screen.blit(number, position)
            if 12 in s.holes:
                position = [61,575]
                screen.blit(number, position)
                position = [386,494]
                screen.blit(number, position)
                position = [579,484]
                screen.blit(number, position)
                position = [127,924]
                screen.blit(number, position)
                position = [387,906]
                screen.blit(number, position)
                position = [547,894]
                screen.blit(number, position)
            if 13 in s.holes:
                position = [194,546]
                screen.blit(number, position)
                position = [288,461]
                screen.blit(number, position)
                position = [547,579]
                screen.blit(number, position)
                position = [60,924]
                screen.blit(number, position)
                position = [419,874]
                screen.blit(number, position)
                position = [612,831]
                screen.blit(number, position)
            if 14 in s.holes:
                position = [127,544]
                screen.blit(number, position)
                position = [353,462]
                screen.blit(number, position)
                position = [547,484]
                screen.blit(number, position)
                position = [94,892]
                screen.blit(number, position)
                position = [387,939]
                screen.blit(number, position)
                position = [612,863]
                screen.blit(number, position)
            if 15 in s.holes:
                position = [194,577]
                screen.blit(number, position)
                position = [354,494]
                screen.blit(number, position)
                position = [612,548]
                screen.blit(number, position)
                position = [61,892]
                screen.blit(number, position)
                position = [322,874]
                screen.blit(number, position)
                position = [548,926]
                screen.blit(number, position)
            if 16 in s.holes:
                position = [126,512]
                screen.blit(number, position)
                position = [353,430]
                screen.blit(number, position)
                position = [612,515]
                screen.blit(number, position)
                position = [127,956]
                screen.blit(number, position)
                position = [354,938]
                screen.blit(number, position)
                position = [580,862]
                screen.blit(number, position)
            if 17 in s.holes:
                position = [193,513]
                screen.blit(number, position)
                position = [419,495]
                screen.blit(number, position)
                position = [547,547]
                screen.blit(number, position)
                position = [127,891]
                screen.blit(number, position)
                position = [387,875]
                screen.blit(number, position)
                position = [547,861]
                screen.blit(number, position)
            if 18 in s.holes:
                position = [94,511]
                screen.blit(number, position)
                position = [322,494]
                screen.blit(number, position)
                position = [612,484]
                screen.blit(number, position)
                position = [128,860]
                screen.blit(number, position)
                position = [322,938]
                screen.blit(number, position)
                position = [613,927]
                screen.blit(number, position)
            if 19 in s.holes:
                position = [159,480]
                screen.blit(number, position)
                position = [321,462]
                screen.blit(number, position)
                position = [546,516]
                screen.blit(number, position)
                position = [160,924]
                screen.blit(number, position)
                position = [322,906]
                screen.blit(number, position)
                position = [613,894]
                screen.blit(number, position)
            if 20 in s.holes:
                position = [160,545]
                screen.blit(number, position)
                position = [386,463]
                screen.blit(number, position)
                position = [579,516]
                screen.blit(number, position)
                position = [94,925]
                screen.blit(number, position)
                position = [420,906]
                screen.blit(number, position)
                position = [514,893]
                screen.blit(number, position)
            if 21 in s.holes:
                position = [94,544]
                screen.blit(number, position)
                position = [387,526]
                screen.blit(number, position)
                position = [579,579]
                screen.blit(number, position)
                position = [94,860]
                screen.blit(number, position)
                position = [354,906]
                screen.blit(number, position)
                position = [581,958]
                screen.blit(number, position)
            if 22 in s.holes:
                position = [94,479]
                screen.blit(number, position)
                position = [322,526]
                screen.blit(number, position)
                position = [646,515]
                screen.blit(number, position)
                position = [160,860]
                screen.blit(number, position)
                position = [355,970]
                screen.blit(number, position)
                position = [580,894]
                screen.blit(number, position)
            if 23 in s.holes:
                position = [95,576]
                screen.blit(number, position)
                position = [387,559]
                screen.blit(number, position)
                position = [514,484]
                screen.blit(number, position)
                position = [194,924]
                screen.blit(number, position)
                position = [386,842]
                screen.blit(number, position)
                position = [546,830]
                screen.blit(number, position)
            if 24 in s.holes:
                position = [60,543]
                screen.blit(number, position)
                position = [321,429]
                screen.blit(number, position)
                position = [613,451]
                screen.blit(number, position)
                position = [61,860]
                screen.blit(number, position)
                position = [322,970]
                screen.blit(number, position)
                position = [646,863]
                screen.blit(number, position)
            if 25 in s.holes:
                position = [159,449]
                screen.blit(number, position)
                position = [419,462]
                screen.blit(number, position)
                position = [646,548]
                screen.blit(number, position)
                position = [94,956]
                screen.blit(number, position)
                position = [354,874]
                screen.blit(number, position)
                position = [515,925]
                screen.blit(number, position)

        if s.game.corners1.status == True:
            position = [15,377]
            screen.blit(corners, position)
        if s.game.corners2.status == True:
            position = [245,360]
            screen.blit(corners, position)
        if s.game.corners3.status == True:
            position = [471,383]
            screen.blit(corners, position)
        if s.game.corners4.status == True:
            position = [17,761]
            screen.blit(corners, position)
        if s.game.corners5.status == True:
            position = [247,774]
            screen.blit(corners, position)
        if s.game.corners6.status == True:
            position = [471,763]
            screen.blit(corners, position)

        if s.game.super1.status == True:
            position = [12,439]
            screen.blit(super_line, position)
        if s.game.super2.status == True:
            position = [242,422]
            screen.blit(super_line, position)
        if s.game.super3.status == True:
            position = [468,444]
            screen.blit(super_line, position)
        if s.game.super4.status == True:
            position = [14,821]
            screen.blit(super_line, position)
        if s.game.super5.status == True:
            position = [244,836]
            screen.blit(super_line, position)
        if s.game.super6.status == True:
            position = [468,821]
            screen.blit(super_line, position)

        if s.game.card1_replay_counter.position > 0 or s.game.card2_replay_counter.position > 0 or s.game.card3_replay_counter.position > 0 or s.game.card4_replay_counter.position > 0 or s.game.card5_replay_counter.position > 0 or s.game.card6_replay_counter.position > 0:
            if s.game.card1_replay_counter.position > 0 and s.game.card1_double.status == False:
                position = [75,402]
                screen.blit(c, position)
            if s.game.card2_replay_counter.position > 0 and s.game.card2_double.status == False:
                position = [302,383]
                screen.blit(c, position)
            if s.game.card3_replay_counter.position > 0 and s.game.card3_double.status == False:
                position = [529,407]
                screen.blit(c, position)
            if s.game.card4_replay_counter.position > 0 and s.game.card4_double.status == False:
                position = [76,783]
                screen.blit(c, position)
            if s.game.card5_replay_counter.position > 0 and s.game.card5_double.status == False:
                position = [304,796]
                screen.blit(c, position)
            if s.game.card6_replay_counter.position > 0 and s.game.card6_double.status == False:
                position = [528,785]
                screen.blit(c, position)

        if s.game.card1_double.status == True:
            position = [124,415]
            screen.blit(d, position)
        if s.game.card2_double.status == True:
            position = [352,398]
            screen.blit(d, position)
        if s.game.card3_double.status == True:
            position = [579,419]
            screen.blit(d, position)
        if s.game.card4_double.status == True:
            position = [127,796]
            screen.blit(d, position)
        if s.game.card5_double.status == True:
            position = [353,810]
            screen.blit(d, position)
        if s.game.card6_double.status == True:
            position = [578,798]
            screen.blit(d, position)

        if s.game.card1_missed.status == True:
            position = [177,415]
            screen.blit(n, position)
        if s.game.card2_missed.status == True:
            position = [403,396]
            screen.blit(n, position)
        if s.game.card3_missed.status == True:
            position = [630,419]
            screen.blit(n, position)
        if s.game.card4_missed.status == True:
            position = [178,796]
            screen.blit(n, position)
        if s.game.card5_missed.status == True:
            position = [403,810]
            screen.blit(n, position)
        if s.game.card6_missed.status == True:
            position = [630,798]
            screen.blit(n, position)

    if s.game.tilt.status == True:
        position = [309,715]
        screen.blit(tilt, position)

    pygame.display.update()

def blink_double(s):
    s.game.blink = not s.game.blink
    if s.game.blink == 1:
        blink_pos = [490,637]
        screen.blit(blink_image, blink_pos)
        pygame.display.update()
    else:
        display(s)
