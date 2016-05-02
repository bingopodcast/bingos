#!/usr/bin/python
import pygame
import time
import bright_lights
import coney_island
import broadway_51
import spot_lite

def replay_step_up(pos, reel1, reel10, reel100):
    delta_y = 38

    r1x = reel1.position[0]
    r10x = reel10.position[0]
    r100x = reel100.position[0]

    if (pos + 1) % 10 == 0 and not (pos + 1) % 100 == 0:
        reel1.position = [r1x,reel1.default_y]
        reel10.position = [r10x,reel10.position[1] - delta_y]
    elif (pos + 1) % 100 == 0:
        reel1.position = [r1x,reel1.default_y]
        reel10.position = [r10x,reel10.default_y]
        reel100.position = [r100x,reel100.position[1] - delta_y]
    else:
        reel1.position = [r1x,reel1.position[1] - delta_y]
    time.sleep(0.2)

def replay_step_down(pos, reel1, reel10, reel100):
    delta_y = 38

    r1x = reel1.position[0]
    r10x = reel10.position[0]
    r100x = reel100.position[0]

    if (pos + 1) % 10 == 0 and not (pos + 1) % 100 == 0:
        reel1.position = [r1x,reel1.default_y]
        reel10.position = [r10x,reel10.position[1] + delta_y]
    elif (pos + 1) % 100 == 0:
        reel1.position = [r1x,reel1.default_y]
        reel10.position = [r10x,reel10.default_y]
        reel100.position = [r100x,reel100.position[1] + delta_y]
    else:
        reel1.position = [r1x,reel1.position[1] + delta_y]

