#!/usr/bin/python

import procgame.game, sys, os, time


class Tilt(procgame.game.Mode):
    """Displays tilt on the backglass and waits for a new coin to restart the game"""
    def __init__(self, game):
        super(Tilt, self).__init__(game=game, priority=5)

    def mode_stopped(self):
        print ("IN MODE STOPPED")
        self.spin_cycle()

    def tilt_actions(self):
        if self.game.switches.shutter.is_inactive():
            self.game.coils.shutterMotor.pulse()
        self.game.tilt.engage(self.game)
        print "TILTED"
        # displays "Tilt" on the backglass, you have to recoin.

    def sw_trough4_inactive(self, sw):
        for i in range(self.game.timer.position, 40):
            starttime = time.time()
            self.game.timer.step()
                
            print "Timer position %s" % self.game.timer.position
            time.sleep(3.0 - ((time.time() - starttime) % 3.0))
        else:
            self.tilt_actions()

    def sw_tilt_active(self, sw):
        self.tilt_actions()

    def sw_replay0_inactive(self, sw):
        if self.game.switches.coin.is_active():
            self.mode_stopped()

    def sw_replay0_active(self, sw):
        if self.game.switches.startButton.is_active():
           self.mode_stopped()
