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

# -- Movement schedule for all characters to get to Bjarn's room

import adonthell
import random

class to_cellar:

    def __init__ (self, mapcharacterinstance):
        self.myself = mapcharacterinstance

        # -- gives the proper exit for each submap to reach Bjarn's room
        # (yard, common room, parlour, kitchen, cellar, bath, Alek's room,
        # Bjarn's room, store room, 1st floor Fellnir's room, Frostbloom's
        # room, Player's room, Silverhair's room)
        self.exits = \
            [(18, 13, adonthell.STAND_NORTH), \
            (9, 1, adonthell.STAND_NORTH), \
            (0, 4, adonthell.STAND_WEST), \
            (6, 6, adonthell.STAND_SOUTH), \
            (10, 7, adonthell.STAND_EAST), \
            (4, 7, adonthell.STAND_SOUTH), \
            (6, 6, adonthell.STAND_SOUTH), \
            (-1, -1, -1), \
            (7, 3, adonthell.STAND_EAST), \
            (8, 1, adonthell.STAND_NORTH), \
            (0, 3, adonthell.STAND_WEST), \
            (5, 3, adonthell.STAND_EAST), \
            (5, 1, adonthell.STAND_NORTH), \
            (5, 1, adonthell.STAND_NORTH)]

        self.myself.set_val ("todo", 0)


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
            x, y, dir = self.exits[myself.submap ()]

            # -- in Bjarn's room
            if x == -1:
                submap = myself.mymap ().get_submap (myself.submap ())
                x = random.randint (1, 4)
                y = random.randint (5, 9)

                while not submap.get_square (x, y).is_free ():
                    x = random.randint (1, 4)
                    y = random.randint (5, 9)

                # -- calculate direction
                # -- north-western area
                if x + y < 10:
                    if x + 3 > y: dir = adonthell.STAND_SOUTH
                    else: dir = adonthell.STAND_EAST
                # -- south-east corner
                else:
                    if y - (x + 3) > 0: dir = adonthell.STAND_NORTH
                    else: dir = adonthell.STAND_WEST

            myself.set_goal (x, y, dir)
            myself.set_val ("todo", 2)

        # -- move
        elif todo == 2:
            if myself.follow_path () == 1:
                # -- reached our final destination
                myself.set_val ("todo", 0)

                if myself.submap () == 7 and myself.posx () != 1:
                    if myself.get_name () == adonthell.gamedata_player ().get_name ():
                        myself.set_schedule ("keyboard_control")
                        bjarn = adonthell.gamedata_get_character ("Bjarn Fingolson")
                        bjarn.set_dialogue ("dialogues/extro")
                        bjarn.launch_action (myself)
                        
                    else:
                        myself.set_schedule_active (0)
