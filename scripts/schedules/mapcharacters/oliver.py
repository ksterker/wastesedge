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

# -- Movement schedule for Oliver Redwyne
#
#    He'll walk around in the stable and yard.
#    When summoned by Orloth, he'll show the player to his room

import adonthell
import schedule
import random

def _(message): return message

class oliver (schedule.speak):
    def __init__ (self, mapcharacterinstance):
        self.myself = mapcharacterinstance
        
        # -- make random remarks
        self.speech = [_("It's so exciting. An Elven Lady, here at Waste's Edge!"), \
                  _("I gotta hurry before mother complains again."), \
                  _("Why can't I have a little dog!?")]
        self.speech_delay = (20, 40)
        schedule.speak.__init__(self)
        
        # -- the tiles around Orloth
        self.offsets = [(1,1),(1,-1),(-1,1),(-1,-1),(1,0),(0,1),(-1,0),(0,-1)]

        self.myself.set_callback (self.goal_reached)
    
    # -- summoned to the common room player to his room
    def goto_common_room (self):
        # -- beam directly to common room, as it is faster that way
        self.myself.jump_to (1, 13, 7, adonthell.STAND_NORTH)
        
        # -- find a free spot near Orloth and the player
        orloth = adonthell.gamedata_get_character ("Orloth Redwyne")
        for (x, y) in self.offsets:
            x = x + orloth.posx ()
            y = y + orloth.posy ()
            
            if self.myself.set_goal (x, y): 
                break
        
    # -- leave the player's room and goto the barn
    def goto_barn (self):
        location = self.myself.submap ()

        # -- Player's room
        if location == 12:
            self.myself.set_goal (5, 1)

        # -- First floor
        elif location == 9:
            self.myself.set_goal (8, 1)

        # -- Second floor (this shouldn't happen, but it once did ...)
        elif location == 14:
            self.myself.set_goal (4, 1)

        # -- Common Room
        elif location == 1:
            self.myself.set_goal (13, 8)

        # -- Yard, our final goal (for now)
        elif location == 0:
            self.myself.set_goal (25, 15)
            self.myself.goto_barn = 0
            
    def goal_reached (self):
        if self.myself.get_val ("goto_barn") == 1:
            self.goto_barn ()
