#
#  (C) Copyright 2001 Alexandre Courbot <alexandrecourbot@linuxgames.com>
#  Part of the Adonthell Project http://adonthell.linuxgames.com
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License.
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY.
#
#  See the COPYING file for more details
#

# -- Movement schedule for Lucia Redwyne
#
# She just walk around in the kitchen, doing her business and
# complaining about her life.

import adonthell
from adonthell import STAND_NORTH, STAND_SOUTH, STAND_WEST, STAND_EAST
from random import randint

class lucia:

    def __init__ (self, mapcharacterinstance):
        self.myself = mapcharacterinstance
        
        self.speech = ["When could I finally rest a bit?", \
                       "I told Orloth this place would bring us problems!", \
                       "This smoke! I'm dying!"]

        self.coords = [(3, 3, STAND_NORTH), \
                  (6, 3, STAND_EAST)]

    def run (self):
        myself = self.myself
        todo = myself.get_val ("todo")

        # -- waiting
        if todo == 0:
            delay = myself.get_val ("delay")

            # -- If standing delay expired, move around next time
            if delay == 0:
                myself.set_val ("todo", 1)
            else:
                myself.set_val ("delay", delay - 1)


        # -- engage a new movement
        elif todo == 1:
            if myself.posx () != 3:
                x, y, dir = self.coords[0]
            else:
                x, y, dir = self.coords[randint(0, 1)]
            myself.set_goal (x, y, dir)
            myself.set_val ("todo", 2)

        # -- moving
        elif todo == 2:
            if myself.follow_path () == 1:
                # -- standing in front of the exit
                if myself.posx () == 6:
                    myself.speak ("Ah, some fresh air!")

                    tmp = myself.get_val ("say_something")
                    myself.set_val ("say_something", tmp + 75)
                    myself.set_val ("delay", 300)

                else:
                    myself.set_val ("delay", 1000 + randint (0, 2000))
                                    
                myself.set_val ("todo", 0)



        # -- utter a random remark
        tmp = myself.get_val ("say_something")
        myself.set_val ("say_something", tmp - 1)
        if tmp == 0:
            myself.speak (self.speech[randint (0, 2)])
            delay = randint (50, 100) * 20
            myself.set_val ("say_something", delay)
