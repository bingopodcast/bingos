#!/usr/bin/python

import procgame.game, sys, os
from bingo_emulator.graphics import methods as graphics
from bingo_emulator.graphics.bright_lights import *

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
        if self.game.switches.shutter.is_inactive():
            self.game.coils.shutterMotor.pulse()
        self.holes = []
        self.game.selector.reset()
        self.game.ball_count.reset()
        self.game.extra_ball.reset()
        self.game.tilt.engage(self.game)
        # displays "Tilt" on the backglass, you have to recoin.
        graphics.bright_lights.display(self.holes, self.game.selector.position, True, False, True)
        self.game.modes.remove(Timeout)

