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

# -- Movement schedule for Fellnir Kezular
#
#    He'll busy himself in his room

from adonthell import gamedata_player, STAND_NORTH, STAND_SOUTH, STAND_WEST, STAND_EAST
from random import randint

class fellnir:

    def __init__ (self, mapcharacterinstance):
        self.myself = mapcharacterinstance
        self.speech = ["Master Orloth should throw out that brute!", \
                       "Take equal parts of vitriol, nitre and sal ammoniac ..."]

        self.coords = [(2, 5, STAND_EAST), \
                       (4, 4, STAND_SOUTH), \
                       (4, 2, STAND_NORTH), \
                       (6, 5, STAND_WEST)]

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
            x, y, dir = self.coords[randint (0, 3)]

            myself.set_goal (x, y, dir)
            myself.set_val ("todo", 2)

        # -- moving
        elif todo == 2:
            if myself.follow_path () == 1:
                # -- the time we stay at the same place
                delay = randint (30, 60) * 25

                myself.set_val ("delay", delay)
                myself.set_val ("todo", 0)


        # -- utter a random remark
        tmp = myself.get_val ("say_something")
        myself.set_val ("say_something", tmp - 1)
        if tmp <= 0:
            myself.speak (self.speech[randint (0, 1)])
            delay = randint (20, 40) * 40
            myself.set_val ("say_something", delay)
