import os, logging, procgame, procgame.game, procgame.dmd, pinproc
from procgame.game import SkeletonGame
from procgame import *
from procgame.modes import Attract
from procgame.game.skeletongame import run_proc_game
import sys
sys.path.insert(0,os.path.pardir)
from units.units import *

# these are modes that you define, and probably store in
# a my_modes folder under this one....
import my_modes
from my_modes import BaseGameMode

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
curr_file_path = os.path.dirname(os.path.abspath( __file__ ))

class CIGame(SkeletonGame):

    def __init__(self):
        self.curr_file_path = curr_file_path

        # NOTE: trough_count only counts the number of switches present in the  trough.  It does _not_ count
        #       the number of balls present.   In this game, there  should  be  8  balls.
        self.trough_count = 6

        # Subclass my units unique to this game -  modifications must be made to set up mixers and steppers unique to the game
        # NOTE: 'top' positions are indexed using a 0 index, so the top on a 24 position unit is actually 23.

        # Initialize reflex(es) and mixers unique to this game
        # NOTE: reflex unit drawing was not available for this game, so until I convince
        #       another Coney Island owner to take their game apart, I'll note that there
        #       are four lugs, three of which provides another path to the mixer, and one which is always connected
        #       and bypasses the mixer entirely.  There are no games from 1951 or 52 that have the reflex documented.
        reflex = Reflex("primary", 200)
       
        #Initialize the mixer units
	# NOTE: the mixers are not documented for this game either.  However, there are three different lugs connected.
	#	I will guess that 3/24 of all lugs are blanks, though looking at the docs for Bally Beauty shows that
	#	only 3/24 positions are not connected. Many of the other early games show similar patterns.
        mixer = Mixer("mixer", 23)

        #Initialize stepper units used to keep track of features or timing.
        selector = Stepper("selector", 3)
        ebselector = Stepper("ebselector", 7)
        timer = Stepper("timer", 40)
        ball_count = Stepper("ball_count", 7)
        extra_ball = Stepper("extra_ball", 4)

        #Check for status of the replay register zero switch.  If positive
        #and machine is just powered on, this will zero out the replays.
        replay_reset = Relay("replay_reset")
        
        #When engage()d, light 6v circuit, and enable game features, scoring,
        #etc. Disengage()d means that the machine is 'soft' tilted. 
        anti_cheat = Relay("anti_cheat")

        #When engage()d, spin.
        start = Relay("start")

        # When engage()d, allow for play for EB.  Engages with the press of the yellow button.
	# does not allow for play if there are no credits on the meter, nor if the EB unit is
	# at the top. Also does not allow for play if the timer has shut off.  You cannot revive
	# older games with a press of a yellow button like you can with games with an 8 step timer.
	eb_play = Relay("eb_play")      

        #Tilt is separate from anti-cheat in that the trip will move the shutter
        #when the game is tilted with 1st ball in the lane.  Also prevents you
        #from picking back up by killing the anti-cheat.  Can be engaged by 
        #tilt bob, slam tilt switches, or timer at 39th step.
        #Immediately kills motors.
        tilt = Relay("tilt")

        
        # Optional definition for 'auto-closed' switches
        # Saving this for testing without a cabinet
        self.osc_closed_switches = ['trough1','trough2','trough3','trough4','trough5','trough6']

        #Trough switches are numbered r-l in a bingo, but l-r in modern games
        super(CIGame, self).__init__('config/coney_island.yaml', self.curr_file_path)

        self.base_game_mode = BaseGameMode(game=self)

        # call reset (to reset the machine/modes/etc)
        self.reset()

        def reset(self, replay_reset):
            # EVERY SkeletonGame game should start its reset() with a call to super()
            super(CIGame,self).reset()
        
            #Every bingo requires the meter to register '0' 
            #before allowing coin entry - does the framework do this
            #on power up or game start?!?
            for sw in self.switches:
                if (sw.name == replay0):
                    if (sw.is_active):
                        pass
                    else:   
                        replay_reset.engage() # resets the replays to 0
                        if (sw.is_inactive):
                            replay_reset.disengage()
	    
		def startup(self, replay_reset):
        	    for sw in self.switches:
				if (sw.name == replay0):
					if (sw.is_inactive):
						coinup.allow()#hmm.
						if (sw.name == coin):
							pass 
if __name__ == '__main__':
    run_proc_game(CIGame)
