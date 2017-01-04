#!/usr/bin/python
import pygame
import time
import bright_lights
import coney_island
import broadway_51
import spot_lite
import atlantic_city
import palm_beach
import zingo
import leader
import stars
import circus
import lotta_fun
import fun_way
import barrel_o_fun_61
import stock_market
import ticker_tape
import fun_spot
import continental
import dixieland
import high_flyer
import nashville
import wall_street
import super_wall_street
import bali
import long_beach
import miss_california
import mississippi_showboat
import lite_a_line
import hole_in_one
import frolics
import blue_chip
import bull_market
import bright_spot
import holiday
import bally_beauty
import beach_club
import yacht_club
import rodeo_3
import rodeo_1
import dude_ranch
import showboat
import carnival_queen
import county_fair
import sea_island
import circus_queen
import golden_gate
import silver_sails
import laguna_beach
import malibu_beach
import roller_derby
import the_twist
import rainbow
import venus
import cabana
import tropics
import tahiti_1
import rio
import havana
import mexico
import hawaii_1
import nevada
import singapore
import tropicana
import miami_beach
import fun_spot_61
import fun_spot_62
import fun_spot_63
import barrel_o_fun
import barrel_o_fun_62
import single_coin_pittsburgh
import variety
import big_time
import triple_play
import manhattan
import pixies
import south_seas
import monaco
import brazil
import beach_beauty
import miss_america
import miss_america_75
import miss_america_supreme
import miss_america_deluxe
import ballerina
import bikini
import lido
import can_can
import bounty
import broadway
import night_club
import parade
import double_header
import big_show
import key_west
import showtime
import sun_valley
import cypress_gardens
import beach_time
import bonanza
import playtime
import starlet
import caravan
import stardust
import touchdown


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

