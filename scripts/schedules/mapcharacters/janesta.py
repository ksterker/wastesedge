#
#  (C) Copyright 2001 Kai Sterker <kaisterker@linuxgames.com>
#  Part of the Adonthell Project http://adonthell.linuxgames.com
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License.
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY.
#
#  See the COPYING file for more details
#

# -- Movement schedule for Janesta Skywind
#
#    She'll busy herself in Silverhair's room

import adonthell
import schedule
import random

def _(message): return message

class janesta (schedule.speak):

    def __init__ (self, mapcharacterinstance):
        self.myself = mapcharacterinstance
        
        # -- make random remarks
        self.speech = [_("Oh, dear. Oh, dear."), \
                       _("What will happen to us if they take the Mistress?"), \
                       _("I must do something about this awful room."), \
                       _("Oh, how do they expect us to live decently in a place like this?")]
        self.speech_delay = (25, 45)
        schedule.speak.__init__(self)

        self.coords = [(1, 3, adonthell.STAND_NORTH), \
                       (6, 3, adonthell.STAND_NORTH), \
                       (1, 5, adonthell.STAND_SOUTH), \
                       (4, 2, adonthell.STAND_WEST)]

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
            x, y, dir = self.coords[random.randrange (0, 4)]

            myself.set_goal (x, y, dir)
            myself.set_val ("todo", 2)

        # -- moving
        elif todo == 2:
            if myself.follow_path () == 1:
                # -- the time we stay at the same place
                delay = random.randrange (20, 60) * 10

                myself.set_val ("delay", delay)
                myself.set_val ("todo", 0)
