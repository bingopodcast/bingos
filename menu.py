#!/usr/bin/python

import logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
import pinproc
import procgame.game, sys, os
import procgame.config
import pygame
import time
import thread

sys.path.insert(0,os.path.pardir)
from bingo_emulator.graphics import methods as graphics

pygame.init()
pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((720,1080))
screen.fill([0,0,0])

class Menu(procgame.game.BasicGame):
    """ This menu lets you select games to play """
    def __init__(self, machine_type):
        super(Menu, self).__init__(machine_type)

    def reset(self, selection, select):
        super(Menu, self).reset()
        self.load_config('coney_island.yaml')
        mainmenu = MainMenu(self, selection, select)
        self.modes.add(mainmenu)
        self.logger = logging.getLogger('game')

        selection[select]
        __import__("graphics.%s" % (selection[select]))
        g = "graphics.%s.display(0,0)" % (selection[select])
        eval(g)

        
class MainMenu(procgame.game.Mode):
    def __init__(self, game, selection, select):
        super(MainMenu, self).__init__(game=game, priority=5)
        self.game.select = select
        self.game.selection = selection

    def sw_yellow_active(self, sw):
        try:
            t = thread.start_new(__import__("%s.game" % (self.game.selection[self.game.select])))
            if t.isAlive():
                t.join()
        except:
            g = (__import__("%s.game" % (self.game.selection[self.game.select])))
            t = thread.start_new(eval(g))
            if t.isAlive():
                t.join()
        self.game.reset(self.game.selection, self.game.select)

    def sw_left_active(self, sw):
        if self.game.select != 1:
            self.game.select -= 1
            self.game.selection[self.game.select]
            __import__("graphics.%s" % (self.game.selection[self.game.select]))
            g = "graphics.%s.display(0,0)" % (self.game.selection[self.game.select])
            eval(g)
    def sw_right_active(self, sw):
        if self.game.select != len(self.game.selection):
            self.game.select += 1
            self.game.selection[self.game.select]
            __import__("graphics.%s" % (self.game.selection[self.game.select]))
            g = "graphics.%s.display(0,0)" % (self.game.selection[self.game.select])
            eval(g)

def main():
    selection = {}
    selection[1] = "bright_lights"
    selection[2] = "broadway_51"
    selection[3] = "coney_island"

    select = 1

    game = Menu(machine_type='pdb')
    game.reset(selection, select)
    game.run_loop()

if __name__ == "__main__":
    main()
