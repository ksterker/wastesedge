#
#  (C) Copyright 2001/2002 Kai Sterker <kaisterker@linuxgames.com>
#  Part of the Adonthell Project http://adonthell.linuxgames.com
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License.
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY.
#
#  See the COPYING file for more details
#

# -- Movement schedule for Bjarn Fingolson
#
#    He'll busy himself in his room

import adonthell
import schedule
import random

def _(message): return message

class bjarn (schedule.speak):

    def __init__ (self, mapcharacterinstance):
        self.myself = mapcharacterinstance
        
        # -- make random remarks
        self.speech = [_("Ha! A tradesman is an honourable person, they say!"), \
                       _("Why don't they just take that Silverhair woman to prison!?"), \
                       _("Elves! The head in the sky and the mind full of clouds!")]
        self.speech_delay = (20, 40)
        schedule.speak.__init__(self)
        
        self.coords = [(7, 5, adonthell.STAND_WEST), \
                       (2, 4, adonthell.STAND_SOUTH), \
                       (7, 3, adonthell.STAND_NORTH), \
                       (3, 6, adonthell.STAND_WEST)]

        self.myself.set_callback (self.goal_reached)

    # -- Get at the proper place when Erek lets the player into the room
    #    and at the end of the game.
    def await_player (self):
        self.myself.jump_to (7, 3, 6)
        self.myself.stand_west ()
    
    def start_talking (self):
        self.myself.launch_action (adonthell.gamedata_player ())
        adonthell.gamedata_get_character ("Erek Stonebreaker").pause ()
        
    def walk (self):
        x, y, dir = self.coords[random.randint (0, 3)]
        self.myself.set_goal (x, y, dir)
    
    def goal_reached (self):
        delay = "%it" % random.randrange (15, 30)
        self.myself.time_callback (delay, self.walk)
