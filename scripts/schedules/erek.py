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

# -- Movement schedule for Erek Stonebreaker
#
#    Erek will either be in the parlour or the common room.
#    He'll also help the player to get into Bjarn's room.

from adonthell import STAND_NORTH, STAND_SOUTH, STAND_EAST, STAND_WEST
import adonthell
from random import randint

class erek:

    def __init__ (self, mapcharacterinstance):
        self.myself = mapcharacterinstance

        self.speech = ["How could they do that to the Master?", \
                  "This place is so much different from home.", \
                  "Who could have taken the gems?"]

        self.coords = [(5, 5, STAND_NORTH), \
                       (10, 6, STAND_WEST), \
                       (5, 3, STAND_NORTH), \
                       (4, 5, STAND_SOUTH)]


    def run (self):
        myself = self.myself
        
        # -- lead the player into bjarn's room
        if adonthell.quests["demo"].get_val ("bjarn_door_open") == 2:
            myself.set_schedule_active (0)
            # -- start Bjanr's conversation with the player and Erek
            adonthell.characters["Bjarn Fingolson"].launch_action (adonthell.the_player)

        # -- leave cellar again
        elif myself.get_val ("leave_bjarn") == 1:
            submap = myself.submap ()

            # -- in Bjarn's room
            if submap == 7:
                myself.set_val ("delay", 0)
                myself.set_goal (0, 7, STAND_WEST)
                myself.set_val ("leave_bjarn", 2)

            # -- in the Cellar
            elif submap == 4:
                myself.set_goal (6, 1, STAND_NORTH)
                myself.set_val ("leave_bjarn", 2)

            # -- hopefully in the common room
            else:
                myself.set_val ("leave_bjarn", 0)
                x, y, dir = self.coords[randint (0, 1)]
                myself.set_goal (x, y, dir)

            myself.set_val ("todo", 2)


        # -- "normal" schedule
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
            # -- on our way back from bjarn's room
            if myself.get_val ("leave_bjarn") == 2:
                myself.set_val ("leave_bjarn", 1)

            # -- switch places
            else:
                # -- in common room -> goto parlour
                if myself.submap () == 1:
                    myself.set_goal (14, 4, STAND_EAST)

                # -- in parlour -> goto common room
                else:
                    myself.set_goal (0, 4, STAND_WEST)

            myself.set_val ("todo", 2)

        # -- move
        elif todo == 2:
            if myself.follow_path () == 1:
                # -- reached common room
                if myself.submap () == 1 and myself.posx () == 13:
                    x, y, dir = self.coords[randint (0, 1)]
                    myself.set_goal (x, y, dir)

                    delay = randint (50, 150) * 20
                    myself.set_val ("delay", delay)

                # -- reached parlour
                elif myself.submap () == 2 and myself.posx () == 1:
                    x, y, dir = self.coords[randint (2, 3)]
                    myself.set_goal (x, y, dir)

                    delay = randint (60, 180) * 30
                    myself.set_val ("delay", delay)

                # -- reached our final destination
                else:
                    myself.set_val ("todo", 0)


        # -- do some random babbling
        tmp = myself.get_val ("say_something")
        myself.set_val ("say_something", tmp - 1)

        if tmp == 0:
            myself.speak (self.speech[randint (0, 2)])
            delay = randint (60, 180) * 15
            myself.set_val ("say_something", delay)
