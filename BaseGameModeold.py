import procgame.game
from procgame.game import AdvancedMode

import pygame
from pygame.locals import *
from pygame.font import *

import random

odds_position = 0
squares_position = 0
red_position = 0
yellow_position = 0
reflex_position = 100
spotted_number = 0
timer_position = 0
squareA_position = 0
squareB_position = 0
squareC_position = 0
squareD_position = 0
spotting_disc_position = 0
mixer1_position = 0
mixer2_position = 0
mixer3_position = 0
mixer4_position = 0

class BaseGameMode(procgame.game.AdvancedMode):
    """
    A mode that runs whenever the GAME is in progress.
    (notice the super() function call specifies type .Game)
    - it is automatically added when a game starts
        (mode_started will be called once per game)
    - it is automatically removed when a game ends
        (mode_stopped will be called once per game)

    NOTE: a second player does not cause a second game
        (confusing, no doubt).  When a new player is
        added, an evt_player_added will fire.  When
        a new ball starts, that's a good time to ensure
        our data comes from that player and sync up
        lamps via a call to update_lamps.  Read on...
    """

    def __init__(self, game):
        """ 
        The __init__ function is called automatically whenever an instance 
        of this object is created --e.g., whenever the code:
                something = new BaseGameMode() 
        is executed, this __init__ function is called
        """

        # a call to 'super' call's the parent object's __init__ method
        # in this case, it calls the procgame.game.Mode's init()
        super(BaseGameMode, self).__init__(game=game, priority=5, mode_type=AdvancedMode.Game)

    def evt_player_added(self, player):
        self.game.coils.shutter.pulse()
        reset_squares()
        if self.game.switches.trough6.is_active() and self.game.switches.lane.is_inactive():
            self.game.coils.trough.pulse()
            step_odds(1)
            light_number(self, 0)
            step_timer()

    def scan_all(self):
        if self.game.switches.replay0.is_inactive() or self.game.switches.coin.is_active():
            if self.game.switches.startButton.is_active():
                move_mixers()
                animate_scan()
                jump = determine_probability()
                if jump is True:
                    jump_type = determine_jump()
                    if jump_type == "All":
                        step_odds()
                        step_squares()
                        step_red()
                        step_yellow()
                    if jump_type == "Odds":
                        step_odds()
                    if jump_type == "Squares":
                        step_squares()
                    if jump_type == "DoubleRed":
                        step_red()
                    if jump_type == "DoubleYellow":
                        step_yellow()
                decrease_reflex()
                replay_step_down()

    def move_mixers():
        move_mixer1()
        move_mixer2()
        move_mixer3()
        move_mixer4()
        move_spotting_disc()

    def animate_scan(self):
        self.layer = self.game.animations['flash']

    def determine_jump():
        global mixer1_position, mixer2_position, mixer3_position
        global mixer4_position, spotting_disc_position, reflex_position

        #reflex max position = 300  if the reflex is at this point, the only connected wire is 23-3 on the schem.
        #this will prevent any checks through the mixer for many items until the stepper goes down 113 steps.
        #at 100 steps, 54-4 is connected, but not 53-4.  This is crucial for understanding how the mixers function.

        return jump_type

    def light_number(self, new_number):
        if new_number == 0:
            self.layer = self.game.animations['card_empty']
        if new_number > 0:
            self.layer = self.game.animations['card_%s'] % (new_number)

    def light_square(self):
        global squares_position
        self.layer = self.game.animations['square_%s'] % (squares_position)

    def light_red(self):
        global red_position
        self.layer = self.game.animations['red_%s'] % (red_position)

    def light_yellow(self):
        global yellow_position
        self.layer = self.game.animations['yellow_%s'] % (yellow_position)

    def decrease_reflex():
        global reflex_position
        reflex_position -= 1

    def increase_reflex():
        global reflex_position
        reflex_position += 2

    def step_odds(value=None):
        global odds_position
        odds_max = 8

        if odds_position + 1 != odds_max:
            extra = extra_step("odds")
            if extra:
                if odds_position + extra != odds_max:
                    odds_position + extra
                else:
                    odds_position += 1
            else:
                odds_position += 1
        
        if value:
            odds_position += value

    def step_squares():
        global squares_position, spotted_number
        squares_max = 7

        if squares_position != squares_max:
            extra = extra_step("squares")
            if extra:
                if squares_position + extra != squares_max:
                    squares_position + extra
                else:
                    squares_position += 1
            else :
                squares_position += 1
        if squares_position == 5:
            determine_lockout()
        if squares_position == 6:
            if spotted_number == 0:
                spot_number()
        if squares_position == 7 and spotted_number == 0:
            spot_number()

    def spot_number():
        global spotted_number
        random.choice([2,18])
        light_number(self, 18)

    def step_red():
        global red_position
        red_max = 15

        if red_position != red_max:
            extra = extra_step("red")
            if extra:
                if red_position + extra != red_max:
                    red_position += extra
                else:
                    red_position += 1
            else :
                red_position += 1

    def step_yellow():
        global yellow_position
        yellow_max = 15

        if yellow_position != yellow_max:
            extra = extra_step("yellow")
            if extra:
                if yellow_position + extra != yellow_max:
                    yellow_position += extra
                else:
                    yellow_position += 1
            else :
                yellow_position += 1

    def timer_step(self, lockout):
        global timer_position, squares_position
        timer_position += 1
        if squares_position > 4:
            if timer_position > 1:
                move_squares(self)
            prior = lockout - 1
            if timer_position == lockout:
                lockout_squares(self)
            if timer_position == prior:
                flash_lockout()

    def determine_lockout():
        global spotting_disc_position

        random.choice([1-50])


    def move_mixer1():
        global mixer1_position

        mixer1_position += random.choice([1-24])

        if mixer1_position + movement_amount > 24:
            mixer1_position -= 24

    def move_mixer2():
        global mixer2_position

        mixer2_position += random.choice([1-24])

        if mixer2_position + movement_amount > 24:
            mixer2_position -= 24

    def move_mixer3():
        global mixer3_position

        mixer3_position += random.choice([1-24])

        if mixer3_position + movement_amount > 24:
            mixer3_position -= 24

    def move_mixer4():
        global mixer4_position

        mixer4_position += random.choice([1-24])

        if mixer4_position + movement_amount > 24:
            mixer4_position -= 24

    def move_squares(self):
        if self.game.switches.squareA.is_active():
            moveA()
        if self.game.switches.squareB.is_active():
            moveB()
        if self.game.switches.squareC.is_active():
            moveC()
        if self.game.switches.squareD.is_active():
            moveD()

    def reset_squares():
        global squareA_position, squareB_position
        global squareC_position, squareD_position
        squares = ['A', 'B', 'C', 'D']
        for corner in squares:
            square = square%s_position % (corner)
            if square != 0:
                move%s() % (corner)

    def moveA():
        global squareA_position
        if squareA_position == 3:
            squareA_position = 0
        else :
            squareA_position += 1
        self.layer = self.game.animations['squareA-pos%s'] % (squareA_position)

    def moveB():
        global squareB_position
        if squareB_position == 3:
            squareB_position = 0
        else:
            squareB_position += 1
        self.layer = self.game.animations['squareB-pos%s'] % (squareB_position)
    
    def moveC():
        global squareC_position
        if squareC_position == 3:
            squareC_position = 0
        else:
            squareC_position += 1
        self.layer = self.game.animations['squareC-pos%s'] % (squareC_position)
    
    def moveD():
        global squareD_position
        if squareD_position == 3:
            squareD_position = 0
        else:
            squareD_position += 1
        self.layer = self.game.animations['squareD-pos%s'] % (squareD_position)    

    def lockout_squares(self):
        if self.game.switches.squareA.is_active():
            pass
        if self.game.switches.squareB.is_active():
            pass
        if self.game.switches.squareC.is_active():
            pass
        if self.game.switches.squareD.is_active():
            pass

    def evt_ball_starting(self):
        pass
        # to use the ball saver, we give it the name of a ball-saver
        # method to be called when the ball is saved --that is 
        # defined below
        #self.game.ball_saver_enable(num_balls_to_save=1, time=5, now=True, 
        #    allow_multiple_saves=False, callback=self.ballsaved)
#        self.game.sound.fadeout_music()
#        self.game.sound.play_music('base-music-bgm')

    #def ballsaved(self):
     #   """ this is the method that we told the ball-saver to call if
     #       the ball is saved by the ball-saver; see the call to 
     #       ball_saver_enable.  This just shows a message and plays a
     #       sound but does NOT launch balls.  The ballsaver/trough
     #       handle this for us!
     #   """
     #   self.game.log("BaseGameMode: BALL SAVED from Trough callback")
     #   self.game.sound.play('ball_saved')
     #   self.game.displayText('Ball Saved!')
     #   self.game.coils.flasherShootAgain.pulse()
     #   # Do NOT tell the trough to launch balls!  It's handled automatically!
     #   # self.game.trough.launch_balls(1)

    def mode_started(self):
        """
        the mode_started method is called whenever this mode is added
        to the mode queue; this might happen multiple times per game,
        depending on how the Game itself adds/removes it.  B/C this is 
        an advancedMode, we know when it will be added/removed.
        """
        pass

    def mode_stopped(self): 
        """
        the mode_stopped method is called whenever this mode is removed
        from the mode queue; this might happen multiple times per game,
        depending on how the Game itself adds/removes it
        """
        pass

    #def update_lamps(self):
    #    """ 
    #    update_lamps is a very important method -- you use it to set the lamps
    #    to reflect the current state of the internal mode progress variables.
    #    This function is called after a lampshow is played so that the state
    #    variables are correct after the lampshow is done.  It's also used other
    #    times.
#
#        Notice that progress is stored in the player object, so check with:
#            self.game.getPlayerState(key)
#        which is a wrapper around:
#            self.game.get_current_player().getState(key)
#        """
#        if(self.game.getPlayerState('kickbackEnabled')==True):
#                self.game.lamps.kickback.enable()
#        else:
#                self.game.lamps.kickback.disable()      
#
#        if(self.game.getPlayerState('multiplier') == 2):
#            self.game.lamps.mult2x.enable()
#        else:
#            self.game.lamps.mult2x.disable()
#
#         # standupMid target states
#        if(self.game.getPlayerState('standupSwitchL')):
#            self.game.lamps.standupMidL.enable()
#        else:
#            self.game.lamps.standupMidL.disable()
#
#        if(self.game.getPlayerState('standupSwitchC')): 
#            self.game.lamps.standupMidC.enable()
#        else:
#            self.game.lamps.standupMidC.disable()
#
#        if(self.game.getPlayerState('standupSwitchR')): 
#            self.game.lamps.standupMidR.enable()
#        else:
#            self.game.lamps.standupMidR.disable()
#
        # here's an example of using an array (list) of lamps
        # defined in the game (look at T2Game's __init__ method)
        # and an array of player states to make quick work of syncing
        # several lamps to target states:
#        leftTargetStates = self.game.getPlayerState('leftTargets')
#
#        for target,lamp in zip(leftTargetStates,self.game.leftTargetLamps):
#            if(target):
#                lamp.enable()
#            else:
#                lamp.disable()                        
#
#    """ The following are the event handlers for events broadcast by SkeletonGame.  
#        handling these events lets your mode give custom feedback to the player
#        (lamps, dmd, sound, etc)
#    """
#
#    def evt_ball_ending(self, (shoot_again, last_ball)):
#        """ this is the handler for the evt_ball_ending event.  It shows    
#            the player information about the specific event.  You can optionally
#            return a number, which is the number of seconds that you are requesting
#            to delay the commitment of the event.  For example, if I wanted to show
#            a message for 5 seconds before the ball actually ended (and bonus mode
#            began), I would return 5.  Returning 0 (or None) would indicate no delay.
#        """
#        self.game.log("base game mode trough changed notification ('ball_ending - again=%s, last=%s')" % (shoot_again,last_ball))

        # stop any music as appropriate
        # self.game.sound.fadeout_music()
#        self.game.sound.play('ball_drain')
#        self.game.sound.play_music('sonic')
#        self.game.displayText('BGM Ball Ended!')
#        return 2.0

    def evt_game_ending(self):
        self.game.log("base game mode game changed notification ('game_ending')")

        self.game.displayText("GAME ENDED", 'gameover')

        # Do NOT call game_ended any more!!!!!
        # not now or later!

        return 2


    """
    this is an example of a timed switch handler
         sw_      : indicates a switch handler
         outhole  : the name of the switch
         active   : the state (could be inactive, open, closed)
         for_200ms: how long that the switch must be detected
                                in this state before this handler is called

    in this case, if the controller sees this switch closed
    for 200ms, then this function is called; waiting 200ms
    will wait for long enough for the ball to settle in the
    slot before responding
"""

    

#    def sw_outhole_active_for_200ms(self,sw):
#            self.game.coils.outhole.pulse()
        
#    def sw_ballPopper_active_for_200ms(self, sw):
#        # ballPopper is the vertical up kicker (VUK) in the Skull.
#        # note that blindly kicking the ball up is unwise...
#        if(self.game.gun_mode.clearToLaunchFromSkull()):
#            self.game.coils.ballPopper.pulse()
#
#        # either way, reset the droptarget
#        self.game.lamps.dropTarget.pulse()
#        return procgame.game.SwitchStop

#    def sw_lockLeft_active_for_200ms(self, sw):
#        self.game.coils.lockLeft.pulse()
#        return procgame.game.SwitchStop

#    def sw_lockTop_active_for_200ms(self, sw):
#        self.game.coils.lockTop.pulse()
#        return procgame.game.SwitchStop

#    def sw_rampRightEnter_active(self, sw):       
#        # self.game.displayText("Right Ramp Enter")    
#        return procgame.game.SwitchStop

#    def rampRightMade_active(self, sw):
#        self.game.score(500)
#        # self.game.displayText("Right Ramp Made")    
#        return procgame.game.SwitchStop

#    def sw_rampLeftEnter_active(self, sw):    
#        # self.game.displayText("Left Ramp Enter")    
#        return procgame.game.SwitchStop
#
#    def sw_rampLeftMade_active(self, sw):
#        self.game.score(500)
#        # self.game.displayText("Left Ramp Made")    
#        return procgame.game.SwitchStop
#
#    def kickback_disabler(self):
#        self.game.setPlayerState('kickbackEnabled',False)
#        self.game.lamps.kickback.disable()
#
#    def sw_outlaneL_active(self, sw):
#        if(self.game.getPlayerState('kickbackEnabled')):
#            self.game.coils.kickback.pulse()
#            self.game.score(100)
#            self.game.displayText("Kickback!!!")
#            self.game.lamps.kickback.schedule(schedule=0xff00ff00)
#            self.delay(name='disable_kickback',
#                                 delay=3.0,
#                                 handler=self.kickback_disabler)
#        else:
#            self.game.displayText("Too bad")
#
#        return procgame.game.SwitchContinue   
#
#    """ The following methods illustrate handling a bank of related
#        targets.  Notice that the logical state of the switch is 
#        stored in the player's object.  Each of these functions
#        are VERY similar, and that might be annoying to you
#        (and should be).  An example of a 'better way' follows these.
#    """
#    def sw_standupMidL_active(self, sw): 
#        self.game.setPlayerState('standupSwitchL',True)
#        self.game.lamps.standupMidL.enable()
#        self.checkAllSwitches()
#        return procgame.game.SwitchContinue 
#        
#    def sw_standupMidC_active(self, sw):
#        self.game.setPlayerState('standupSwitchC',True)
#        self.game.lamps.standupMidC.enable()
#        self.checkAllSwitches()
#        return procgame.game.SwitchContinue
#        
#    def sw_standupMidR_active(self, sw):
#        self.game.setPlayerState('standupSwitchR',True)
#        self.game.lamps.standupMidR.enable()
#        self.checkAllSwitches()
#        return procgame.game.SwitchContinue
#
#    def checkAllSwitches(self):
#        """ called by each of the standupMid? handlers to 
#            determine if the bank has been completed """
#        if((self.game.getPlayerState('standupSwitchL') == True) and
#            (self.game.getPlayerState('standupSwitchC') == True) and
#            (self.game.getPlayerState('standupSwitchR') == True)): # all three are True
#                self.game.displayText("All Targets Hit")
#                self.game.score(1000)
#                self.game.sound.play('target_bank')
#                self.game.lamps.standupMidL.disable()
#                self.game.lamps.standupMidC.disable()
#                self.game.lamps.standupMidR.disable()
#                self.game.setPlayerState('standupSwitchL', False)
#                self.game.setPlayerState('standupSwitchC', False)
#                self.game.setPlayerState('standupSwitchR', False)
#        else:
#                self.game.sound.play('target')
#
#    """ An alternate way of handling a bank of related switches
#        using lists (for switch states and lamps) we can have
#        every switch handler call a single function.  Removes
#        redundancy, makes maintanence easier, life better, etc.
#    """
#    def leftTargetHitHelper(self, targetNum):
#        """ called by each of the target active functions
#            the targetNums are actually 0..4 to coincide
#            with the indexes in the arrays, not their numbers
#        """
#        vals = self.game.getPlayerState('leftTargets')
#        vals[targetNum] = True
#        if(False in vals):
#            self.game.setPlayerState('leftTargets',vals)
#            self.game.score(5000)
#            self.game.leftTargetLamps[targetNum].enable()
#            self.game.sound.play('target')
#        else:
#            self.game.setPlayerState('leftTargets',vals)            
#            self.game.score(50000)
#            self.game.sound.play('target_bank')
#            self.game.displayText("LEFT TARGETS COMPLETE!", 'explosion')
#            self.game.setPlayerState('leftTargets',[False]*5)
#
#        return procgame.game.SwitchContinue    
#
#    def sw_target1_active(self, sw):
#        return self.leftTargetHitHelper(0)        
#
#    def sw_target2_active(self, sw):
#        return self.leftTargetHitHelper(1)        
#
#    def sw_target3_active(self, sw):
#        return self.leftTargetHitHelper(2)        
#
#    def sw_target4_active(self, sw):
#        return self.leftTargetHitHelper(3)        
#
#    def sw_target5_active(self, sw):
#        return self.leftTargetHitHelper(4)        
#
#    def sw_slingL_active(self, sw):
#        self.game.score(100)
#        self.game.sound.play('sling')
#        return procgame.game.SwitchContinue
#
#    def sw_slingR_active(self, sw):
#        self.game.score(100)
#        self.game.sound.play('sling')
#        return procgame.game.SwitchContinue
#
#    def sw_dropTarget_active(self,sw):
#        self.game.displayText("STAY OUT!")
#        self.game.coils.dropTarget.pulse()
#        self.game.lamps.dropTarget.pulse(20)
#        return procgame.game.SwitchStop  
#
#    def sw_gripTrigger_active(self, sw):
#        if self.game.switches.shooter.is_active():
#            self.game.coils.plunger.pulse()
#            self.game.sound.play('sling')
#        return procgame.game.SwitchStop
