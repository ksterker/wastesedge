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

import adonthell
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

        self.direction = self.myself.get_val ("direction")

        # -- make random remarks
        self.speech = [_("Ruffinans, the lot of them!"), \
                       _("How dare they imprison one better than they?"), \
                       _("This is an insult to all of the High Born."), \
                       _("I cannot believe such disrespect. Barbarians!")]
        self.speech_delay = (20, 40)
        schedule.speak.__init__(self)

        delay = "%it" % random.randrange (3, 6)
        walk_event = adonthell.time_event (delay)
        walk_event.set_callback (self.walk)
        walk_event.thisown = 0
        self.myself.add_event (walk_event)
        
        self.myself.set_callback (self.goal_reached)

        delay = "%it" % random.randrange (30, 60)
        switch_event = adonthell.time_event (delay)
        switch_event.set_callback (self.switch_direction)
        switch_event.thisown = 0
        self.myself.add_event (switch_event)

    def switch_direction (self):
        # -- ... and set the new one accordingly
        if self.direction == adonthell.WALK_EAST or self.direction == adonthell.WALK_WEST:
            self.direction = random.randrange (adonthell.WALK_NORTH, adonthell.WALK_SOUTH + 1)
        else:
            self.direction = random.randrange (adonthell.WALK_WEST, adonthell.WALK_EAST + 1)
        
        delay = "%it" % random.randrange (30, 60)
        switch_event = adonthell.time_event (delay)
        switch_event.set_callback (self.switch_direction)
        switch_event.thisown = 0
        self.myself.add_event (switch_event)

        self.walk ()
    
    def walk (self):
        # -- switch direction
        if self.direction == adonthell.WALK_NORTH:
            goal = (self.myself.posx (), self.min_y, adonthell.STAND_SOUTH, 0, 1)
        elif self.direction == adonthell.WALK_SOUTH:
            goal = (self.myself.posx (), self.max_y, adonthell.STAND_NORTH, 0, -1)
        elif self.direction == adonthell.WALK_EAST:
            goal = (self.max_x, self.myself.posy (), adonthell.STAND_WEST, -1, 0)
        else:
            goal = (self.min_x, self.myself.posy (), adonthell.STAND_EAST, 1, 0)

        x, y, d = goal[:3]
        self.direction = d + 4

        while not self.myself.set_goal (x, y, d):
            offx, offy = goal [-2:]
            x = x + offx
            y = y + offy

    def goal_reached (self):
        delay = "%it" % random.randrange (3, 6)
        walk_event = adonthell.time_event (delay)
        walk_event.set_callback (self.walk)
        walk_event.thisown = 0
        self.myself.add_event (walk_event)
