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

# -- Movement schedule for Erek Stonebreaker
#
#    Erek will either be in the parlour or the common room.
#    He'll also help the player to get into Bjarn's room.

import adonthell
import schedule
import random

def _(message): return message

class erek (schedule.speak):

    def __init__ (self, mapcharacterinstance):
        self.myself = mapcharacterinstance

        # -- make random remarks
        self.speech = [_("How could they do that to the Master?"), \
                  _("This place is so much different from home."), \
                  _("Who could have taken the gems?")]
        self.speech_delay = (20, 40)
        schedule.speak.__init__(self)
        
        # -- the coordinates for normal schedule
        self.coords = \
            [(5, 5, adonthell.STAND_NORTH), \
            (10, 6, adonthell.STAND_WEST), \
            (5, 3, adonthell.STAND_NORTH), \
            (4, 5, adonthell.STAND_SOUTH)]

        # -- the coordinates for getting back to common room
        self.to_common = \
            [(0, 7, adonthell.STAND_WEST), \
            (6, 1, adonthell.STAND_NORTH)]

        # -- the coordinates for getting back to the 1st floor
        self.to_1st = \
            [(0, 7, adonthell.STAND_WEST), \
            (6, 1, adonthell.STAND_NORTH), \
            (12, 1, adonthell.STAND_NORTH), \
            (2, 4, adonthell.STAND_SOUTH)]

        self.index = 0
        self.walk_delay = "45t"
        
        if self.myself.get_val ("goto") != 0:
            self.myself.set_callback (self.leave_cellar)
        else:
            self.myself.set_callback (self.goal_reached)
        
    def walk (self):
        # -- in common room -> goto parlour
        if self.myself.submap () == 1:
            self.myself.set_goal (14, 4, adonthell.STAND_EAST)
            self.walk_delay = "%it" % random.randrange (36, 108)
            
        # -- in parlour -> goto common room
        else:
            self.myself.set_goal (0, 4, adonthell.STAND_WEST)
            self.walk_delay = "%it" % random.randrange (20, 60)

    def goal_reached (self):
        # -- reached common room
        if self.myself.submap () == 1 and self.myself.posx () == 13:
            x, y, dir = self.coords[random.randrange (0, 2)]
            self.myself.set_goal (x, y, dir)
        # -- reached parlour
        elif self.myself.submap () == 2 and self.myself.posx () == 1:
            x, y, dir = self.coords[random.randrange (2, 4)]
            self.myself.set_goal (x, y, dir)
        # -- reached our final destination
        else:
            self.myself.time_callback (self.walk_delay, self.walk)

    # -- leave Bjarn's room
    def leave_bjarn (self):
        # -- set alternative schedule
        self.myself.set_callback (self.leave_cellar)

        x, y, dir = self.to_common[self.index]
        self.myself.set_goal (x, y, dir)
    
    def leave_cellar (self):
        self.index = self.index + 1
        goto = self.myself.get_val ("goto")
        
        # -- goto first floor
        if goto == 9: coords = self.to_1st
        # -- goto common room
        else: coords = self.to_common
    
        if self.index < len (coords):
            x, y, dir = coords[self.index]
            self.myself.set_goal (x, y, dir)

        # -- arrived
        else:
            # -- restore normal schedule
            self.myself.set_callback (self.goal_reached)
            self.myself.set_val ("goto", 0)
            
            if self.myself.submap () == 1:
                x, y, dir = self.coords[random.randrange (0, 2)]
                self.myself.set_goal (x, y, dir)
            else:
                self.myself.pause ()
