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

# -- Movement schedule for Bjarn Fingolson
#
#    He'll busy himself in his room

import adonthell
import random

def _(message): return message

class bjarn:

    def __init__ (self, mapcharacterinstance):
        self.myself = mapcharacterinstance
        self.speech = [_("Ha! A tradesman is an honourable person, they say!"), \
                       _("Why don't they just take that Silverhair woman to prison!?"), \
                       _("Elves! The head in the sky and the mind full of clouds!")]

        self.coords = [(7, 5, adonthell.STAND_WEST), \
                       (2, 4, adonthell.STAND_SOUTH), \
                       (7, 3, adonthell.STAND_NORTH), \
                       (3, 6, adonthell.STAND_WEST)]

    def run (self):
        myself = self.myself

        # -- Get at the proper place when Erek lets the player into the room
        #    and at the end of the game.
        if adonthell.gamedata_get_quest ("demo").get_val("the_end") == 1 or \
           adonthell.gamedata_get_quest ("demo").get_val("bjarn_door_open") == 2:
            myself.jump_to (myself.submap (), 3, 6)
            myself.stand_west ()
            myself.set_val ("delay", 150)
            return

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
            x, y, dir = self.coords[random.randint (0, 3)]

            myself.set_goal (x, y, dir)
            myself.set_val ("todo", 2)

        # -- moving
        elif todo == 2:
            if myself.follow_path () == 1:
                # -- the time we stay at the same place
                delay = random.randint (30, 60) * 25

                myself.set_val ("delay", delay)
                myself.set_val ("todo", 0)


        # -- utter a random remark
        tmp = myself.get_val ("say_something")
        myself.set_val ("say_something", tmp - 1)
        if tmp <= 0:
            myself.speak (self.speech[random.randint (0, 2)])
            delay = random.randint (20, 40) * 40
            myself.set_val ("say_something", delay)
