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

# -- Movement schedule for Fellnir Kezular
#
#    He'll busy himself in his room

import adonthell
import schedule
import random

def _(message): return message

class fellnir (schedule.speak):

    def __init__ (self, mapcharacterinstance):
        self.myself = mapcharacterinstance
        
        # -- make random remarks
        self.speech = [_("Master Orloth should throw out that brute!"), \
                       _("Take equal parts of vitriol, nitre and sal ammoniac ...")]
        self.speech_delay = (20, 40)
        schedule.speak.__init__(self)

        self.coords = [(2, 5, adonthell.STAND_EAST), \
                       (4, 4, adonthell.STAND_SOUTH), \
                       (4, 2, adonthell.STAND_NORTH), \
                       (6, 5, adonthell.STAND_WEST)]

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
                delay = random.randrange (30, 60) * 25

                myself.set_val ("delay", delay)
                myself.set_val ("todo", 0)
