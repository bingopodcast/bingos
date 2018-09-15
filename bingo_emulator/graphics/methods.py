#!/usr/bin/python
import pygame
import time
import bright_lights, coney_island, broadway_51, spot_lite, atlantic_city, palm_beach, zingo
import leader, stars, circus, lotta_fun, fun_way, barrel_o_fun_61, stock_market, ticker_tape
import fun_spot, continental, dixieland, high_flyer, nashville, wall_street, super_wall_street
import bali, long_beach, miss_california, mississippi_showboat, lite_a_line, hole_in_one
import frolics, blue_chip, bull_market, bright_spot, holiday, bally_beauty, beach_club
import yacht_club, rodeo_3, rodeo_1, dude_ranch, showboat, carnival_queen, county_fair
import sea_island, circus_queen, golden_gate, silver_sails, laguna_beach, malibu_beach
import roller_derby, the_twist, rainbow, venus, cabana, tropics, tahiti_1, rio, havana
import mexico, hawaii_1, nevada, singapore, tropicana, miami_beach, fun_spot_61, fun_spot_62
import fun_spot_63, barrel_o_fun, barrel_o_fun_62, single_coin_pittsburgh, variety, big_time
import triple_play, manhattan, pixies, south_seas, monaco, brazil, beach_beauty, miss_america
import miss_america_75, miss_america_supreme, miss_america_deluxe, ballerina, bikini
import lido, can_can, bounty, broadway, night_club, parade, double_header, big_show
import key_west, showtime, sun_valley, cypress_gardens, beach_time, bonanza, playtime
import starlet, caravan, stardust, touchdown, acapulco, palm_springs, surf_club
import shoot_a_line, shoot_a_line_63, abc, bolero, u345, serenade, ice_frolics, surf_club
import crosswords, spelling_bee, hi_fi, gayety, gay_time, border_beauty, beauty_beach
import folies_bergeres, bahama_beach, zodiac, orient, venice, london, safari, super_7
import bonus_7, double_up, hawaii_2, mystic_gate, tahiti_2, big_wheel, magic_ring, miss_universe
import continental_18, galaxy, hi_hand, joker_wild, twin_joker, yukon

def digital_replay_step_up(pos, reel1, reel10, reel100, reel1000):
    delta_y = 38
    delta = []
    delta.append(0)
    delta.append(delta_y)
    delta.append(delta_y * 2)
    delta.append(delta_y * 3)
    delta.append(delta_y * 4)
    delta.append(delta_y * 5)
    delta.append(delta_y * 6)
    delta.append(delta_y * 7)
    delta.append(delta_y * 8)
    delta.append(delta_y * 9)

    r1x = reel1.position[0]
    r10x = reel10.position[0]
    r100x = reel100.position[0]
    r1000x = reel1000.position[0]

    p = map(int,str(pos).zfill(4))

    if p[3] != 0:
        if reel1.position != [r1x, delta[p[3]]]:
            reel1.position = [r1x,reel1.default_y - delta[p[3]]]
    else:
        reel1.position = [r1x,reel1.default_y]

    if p[2] != 0:
        if reel10.position != [r10x, delta[p[2]]]:
            reel10.position = [r10x,reel10.default_y - delta[p[2]]]
    else:
        reel10.position = [r10x,reel10.default_y]
    
    if p[1] != 0:
        if reel100.position != [r100x, delta[p[1]]]:
            reel100.position = [r100x,reel100.default_y - delta[p[1]]]
    else:
        reel100.position = [r100x,reel100.default_y]
    
    if p[0] != 0:
        if reel1000.position != [r1000x, delta[p[0]]]:
            reel1000.position = [r1000x,reel1000.default_y - delta[p[0]]]
    else:
        reel1000.position = [r1000x,reel1000.default_y]

    return

def replay_step_up(pos, reel1, reel10, reel100, reel1000=False):
    delta_y = 38

    r1x = reel1.position[0]
    r10x = reel10.position[0]
    r100x = reel100.position[0]
    if reel1000 is not False:
        r1000x = reel1000.position[0]

    if (pos) % 10 == 0 and not (pos) % 100 == 0:
        reel1.position = [r1x,reel1.default_y]
        reel10.position = [r10x,reel10.position[1] - delta_y]
    elif (pos) % 100 == 0 and not (pos) % 1000 == 0:
        reel1.position = [r1x,reel1.default_y]
        reel10.position = [r10x,reel10.default_y]
        reel100.position = [r100x,reel100.position[1] - delta_y]
    elif (pos) % 1000 == 0:
        reel1.position = [r1x,reel1.default_y]
        reel10.position = [r10x,reel10.default_y]
        reel100.position = [r100x,reel100.default_y]
        reel1000.position = [r1000x,reel1000.position[1] - delta_y]
    else:
        reel1.position = [r1x,reel1.position[1] - delta_y]

def replay_step_down(pos, reel1, reel10, reel100, reel1000=False):
    delta_y = 38 

    r1x = reel1.position[0]
    r10x = reel10.position[0]
    r100x = reel100.position[0]
    if reel1000 is not False:
        r1000x = reel1000.position[0]

    if (pos + 1) % 10 == 0 and not (pos + 1) % 100 == 0:
        reel1.position = [r1x,reel1.default_y - delta_y * 9]
        reel10.position = [r10x,reel10.position[1] + delta_y]
    elif (pos + 1) % 100 == 0 and not (pos + 1) % 1000 == 0:
        reel1.position = [r1x,reel1.default_y - delta_y * 9]
        reel10.position = [r10x,reel10.default_y - delta_y * 9]
        reel100.position = [r100x,reel100.position[1] + delta_y]
    elif (pos + 1) % 1000 == 0:
        reel1.position = [r1x,reel1.default_y - delta_y * 9]
        reel10.position = [r10x,reel10.default_y - delta_y * 9]
        reel100.position = [r100x,reel100.default_y - delta_y * 9]
        reel1000.position = [r1000x,reel1000.position[1] + delta_y]
    else:
        if reel1.position[1] != reel1.default_y:
            reel1.position = [r1x,reel1.position[1] + delta_y]

