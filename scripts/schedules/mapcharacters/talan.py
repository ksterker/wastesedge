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

# -- Movement schedule for Talan Wendth
#
#    He guards the gate

import adonthell
import random
import schedule

def _(message): return message

class talan (schedule.speak):

    def __init__ (self, mapcharacterinstance):
        self.myself = mapcharacterinstance
        
        # -- make random remarks
        self.speech = [_("Halt! Who goes there?"), \
                       "\"Ai! laurie lantar lassi surinen ...\"", \
                       _("Nobody may pass through the gate!")]
        self.speech_delay = (30, 60)
        schedule.speak.__init__(self)

    def run (self):
        # Caching this often used variable for faster access
        myself = self.myself
        todo = myself.get_val ("todo")

        # If standing
        if todo == 0:
            delay = myself.get_val ("delay")
            # If standing delay expired, move around next time
            if delay == 0:
                myself.set_val ("todo", 1)
            else:
                myself.set_val ("delay", delay - 1)

        # Engage a new movement
        elif todo == 1:
            # Choose where to move, if destination is already occupied we'll
            # fall into the wait state (0) again automatically next time
            if myself.posy () == 17:
                myself.set_goal (11, 19, adonthell.STAND_NORTH)
            else:
                myself.set_goal (11, 17, adonthell.STAND_SOUTH)

            # Next time we'll actually move!
            myself.set_val ("todo", 2)

        # Moving, follow the path until it is reached.
        elif todo == 2:
            # Reached the goal? Wait a while then...
            if myself.follow_path ():
                myself.set_val ("delay", random.randrange (25, 50) * 20)
                myself.set_val ("todo", 0)
