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

# -- Movement schedule for Alek Endhelm
#
#    He'll walk between his table and the bar

import adonthell
import schedule
import random

def _(message): return message

class alek (schedule.speak):
    
    def __init__ (self, mapcharacterinstance):
        self.myself = mapcharacterinstance
        
        # -- make random remarks
        self.speech = [_("More Ale!"), \
                       _("I'll cut 'em open like ripe fruits."), \
                       _("They should sort out this business like real men!")]
        self.speech_delay = (20, 40)
        schedule.speak.__init__(self)
        
    def run (self):
        myself = self.myself

        todo = myself.get_val ("todo")

        # -- waiting
        if todo == 0:
            delay = myself.get_val ("delay")
            # If standing delay expired, move around next time
            if delay == 0:
                myself.set_val ("todo", 1)
            else:
                myself.set_val ("delay", delay - 1)

        # -- engage a new movement
        elif todo == 1:
            # -- walk to table
            if myself.posx () == 1:
                myself.set_goal (12, 5, adonthell.STAND_NORTH)
            # -- walk to bar
            else:
                myself.set_goal (1, 3, adonthell.STAND_SOUTH)

            myself.set_val ("todo", 2)

        # -- moving
        elif todo == 2:
            if myself.follow_path () == 1:
                # -- the time we stay at the same place
                delay = random.randrange (60, 150) * 20

                myself.set_val ("delay", delay)
                myself.set_val ("todo", 0)
