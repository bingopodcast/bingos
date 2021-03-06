#!/usr/bin/python

import procgame.game, sys, os
from bingo_emulator.graphics import methods as graphics
from bingo_emulator.graphics.circus import *


class Timeout(procgame.game.Mode):
    """Displays tilt on the backglass and waits for a new coin to restart the game"""
    def __init__(self, game, priority):
        super(Timeout, self).__init__(game=game, priority=7)

    def mode_started(self):
            self.starting()

    def delayed_actions(self):
        if (self.game.timer.position < 40):
            self.game.timer.step()
            print self.game.timer.position
        else:
            self.tilt_actions()

    def starting(self):
        for i in range(self.game.timer.position,41):
            self.delay(delay=120.0, handler=self.delayed_actions)

    def tilt_actions(self):
        self.game.start.disengage()
        self.cancel_delayed(name="replay_reset")
        self.holes = []
        self.game.selector.reset()
        self.game.extra_ball.reset()
        self.game.c1_double.disengage()
        self.game.c2_double.disengage()
        self.game.c3_double.disengage()
        self.game.all_double.disengage()
        self.game.c1_triple.disengage()
        self.game.c2_triple.disengage()
        self.game.c3_triple.disengage()
        self.game.all_triple.disengage()
        self.game.sixteen.disengage()
        self.game.fifteen.disengage()
        self.game.fourteen.disengage()
        self.game.nineteen.disengage()
        self.game.seventeen.disengage()
        self.game.twentytwo.disengage()
        self.game.fss.disengage()
        self.game.fnt.disengage()
        self.game.ball_count.reset()
        self.game.anti_cheat.engage(self.game)
        self.game.tilt.engage(self.game)
        # displays "Tilt" on the backglass, you have to recoin.
        graphics.circus.display(self.holes, self.game)
        self.game.modes.remove(Timeout)
