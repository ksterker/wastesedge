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

# -- Movement schedule for Sarin Trailfollower
#
#    He walks from one end of the room to the other. From time to
#    to time he'll stop and chose another direction

from adonthell import WALK_NORTH, WALK_SOUTH, WALK_EAST, WALK_WEST, \
     STAND_NORTH, STAND_SOUTH, STAND_WEST, STAND_EAST
import schedule 
import random

def _(message): return message

class sarin (schedule.speak):
    
    def __init__ (self, mapcharacterinstance):
        self.myself = mapcharacterinstance

        # -- Borders of the area he should stay in
        self.min_x = 1
        self.max_x = 6
        self.min_y = 2
        self.max_y = 6

        # -- make random remarks
        self.speech = [_("Ruffinans, the lot of them!"), \
                       _("How dare they imprison one better than they?"), \
                       _("This is an insult to all of the High Born."), \
                       _("I cannot believe such disrespect. Barbarians!")]
        self.speech_delay = (20, 40)
        schedule.speak.__init__(self)
        
    def walk (self):
        pass
    def goal_reached (self):
        pass
    def run_old (self):
        myself = self.myself

        # -- delay for orientation change
        delay = myself.get_val ("delay")

        # -- switch orientation
        if delay == 0:
            # -- get the current direction ...
            dir = myself.get_val ("direction")

            # -- ... and set the new one accordingly
            if dir == WALK_EAST or dir == WALK_WEST:
                dir = random.randrange (WALK_NORTH, WALK_SOUTH + 1)
            else:
                dir = random.randrange (WALK_WEST, WALK_EAST + 1)

            # -- time until the next orientation change
            delay = random.randrange (100, 200) * 15
            myself.set_val ("direction", dir)
            myself.set_val ("delay", delay)
            myself.set_val ("todo", 1)

        else:
            myself.set_val ("delay", delay - 1)


        todo = myself.get_val ("todo")

        # -- waiting
        if todo == 0:
            # -- delay for direction change
            delay = myself.get_val ("switch_direction")

            if delay == 0:
                myself.set_val ("todo", 1)
            else:
                myself.set_val ("switch_direction", delay - 1)

        # -- get movement target
        elif todo == 1:
            # -- get the current direction ...
            dir = myself.get_val ("direction")

            # -- switch direction
            if dir == WALK_NORTH:
                goal = (myself.posx (), self.min_y, STAND_SOUTH, 0, 1)
            elif dir == WALK_SOUTH:
                goal = (myself.posx (), self.max_y, STAND_NORTH, 0, -1)
            elif dir == WALK_EAST:
                goal = (self.max_x, myself.posy(), STAND_WEST, -1, 0)
            else:
                goal = (self.min_x, myself.posy (), STAND_EAST, 1, 0)

            x, y, d = goal[:3]
            myself.set_val ("direction", d + 4)

            while not myself.set_goal (x, y, d):
                offx, offy = goal [-2:]
                x = x + offx
                y = y + offy

            myself.set_val ("todo", 2)

        # -- move
        elif todo == 2:
            if myself.follow_path () == 1:
                # -- wait a little on the current tile
                delay = random.randrange (15, 30) * 10
                myself.set_val ("switch_direction", delay)

                myself.set_val ("todo", 0)
