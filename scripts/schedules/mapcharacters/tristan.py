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

# -- Movement schedule for Tristan Illig
#
#    Illig will either be in the common room or outside at the gate.


import adonthell
import random

def _(message): return message

class tristan:

    def __init__ (self, mapcharacterinstance):
        self.myself = mapcharacterinstance

        self.speech = [_("Don't they know that I am losing money by the hour!?"), \
                       _("What a fuss about a few worthless gems!"), \
                       _("Ye gods! It cannot be that hard to find the thief!")]


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
            # -- in common room -> go outside
            if myself.submap () == 1 and \
                adonthell.gamedata_get_quest ("demo").get_val ("intro_on") == 0:
                myself.set_goal (13, 8, adonthell.STAND_SOUTH)
                delay = random.randint (100, 150) * 30

            # -- outside -> goto common room
            else:
                myself.set_goal (18, 13, adonthell.STAND_NORTH)
                delay = random.randint (75, 150) * 30

            myself.set_val ("delay", delay)
            myself.set_val ("todo", 2)

        # -- move
        elif todo == 2:
            if myself.follow_path () == 1:
                # -- reached common room
                if myself.submap () == 1 and myself.posx () == 13:
                    myself.set_goal (4, 6, adonthell.STAND_WEST)

                # -- reached yard
                elif myself.submap () == 0 and myself.posx () == 18:
                    myself.set_goal (12, 18, adonthell.STAND_WEST)

                # -- reached our final destination
                else:
                    myself.set_val ("todo", 0)


        # -- do some random babbling
        tmp = myself.get_val ("say_something")
        myself.set_val ("say_something", tmp - 1)

        if tmp == 0:
            myself.speak (self.speech[random.randint (0, 2)])
            delay = random.randint (50, 150) * 22
            myself.set_val ("say_something", delay)
