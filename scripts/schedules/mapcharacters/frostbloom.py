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

# -- Movement schedule for Rhayne Frostbloom
#
#    She just walks around the tree in the yard

import adonthell
from random import randint

class frostbloom:
    
    def __init__ (self, mapcharacterinstance):
        self.myself = mapcharacterinstance
        
        # -- Borders of the area she will stay in
        self.min_x = 16
        self.max_x = 24
        self.min_y = 21
        self.max_y = 28

        self.speech = ["This tree is so inspiring.", \
                  "I wonder why everybody seems so excited.", \
                  "Do you know a creature more lovely than the yeti?"]

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

        # -- get movement target
        elif todo == 1:
            # -- the position we want to reach
            x = randint (self.min_x, self.max_x)
            y = randint (self.min_y, self.max_y)

            myself.set_goal (x, y)

            delay = randint (30, 90) * 30
            myself.set_val ("delay", delay)
            myself.set_val ("todo", 2)

        # -- walk to the new position
        elif todo == 2:
            if myself.follow_path () == 1:
                myself.set_val ("todo", 0)


        # -- utter a random remark
        tmp = myself.get_val ("say_something")
        myself.set_val ("say_something", tmp - 1)
        if tmp == 0:
            myself.speak (self.speech[randint (0, 2)])
            delay = randint (50, 150) * 20
            myself.set_val ("say_something", delay)
