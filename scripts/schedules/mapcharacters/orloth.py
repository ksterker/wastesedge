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

# -- Movement schedule for Orloth Redwyne
#
#    He'll walk up to a table occasionally and either set or clean it
#    From time to time he'll complain about the grandfather clock

import adonthell
import schedule
import random

def _(message): return message

class orloth (schedule.speak):

    def __init__ (self, mapcharacterinstance):
        self.myself = mapcharacterinstance
        
        # -- make random remarks
        self.speech = [_("I gotta clean this mug!"), \
                  _("That barrel is leaking."), \
                  _("I hope they'll find the thief!")]
        self.speech_delay = (25, 60)
        schedule.speak.__init__(self)

        self.coords = [(10, 3, adonthell.STAND_NORTH), \
                  (3, 5, adonthell.STAND_SOUTH), \
                  (7, 6, adonthell.STAND_EAST), \
                  (12, 3, adonthell.STAND_SOUTH), \
                  (7, 4, adonthell.STAND_WEST), \
                  (3, 7, 0), \
                  (9, 7, 0), \
                  (12, 5, 0), \
                  (6, 5, 0)]
        
        # -- improve that!!!
        self.goal_reached ()
        self.myself.set_callback (self.goal_reached)
        
    def walk (self):
        # -- return to bar
        if self.myself.posx () != 2:
            self.myself.set_goal (2, 2, adonthell.STAND_SOUTH)
            self.myself.set_val ("table_num", 0)

        # -- when we are at the bar, then wait a while before
        #    moving again
        else:
            index = random.randrange (0, 5)
            x, y, dir = self.coords[index]
            self.myself.set_goal (x, y, dir)
            self.myself.set_val ("table_num", index)
        
    def goal_reached (self):
        # -- standing in front of the clock
        if self.myself.posx () == 10:
            self.myself.speak (_("That clock is late again!"))
            delay = "%it" % random.randrange (3, 6)
        # -- standing at the bar 
        elif self.myself.posx () == 2:
            delay = "%it" % random.randrange (16, 48)
        # -- standing at a table
        else:
            delay = "3t"
            # -- put/take first mug
            frst_mug = adonthell.time_event ("1t")
            frst_mug.set_callback (self.put_object, (106, 0))
            frst_mug.thisown = 0
            self.myself.add_event (frst_mug)
            # -- put/take second mug
            scnd_mug = adonthell.time_event ("2t")
            scnd_mug.set_callback (self.put_object, (107, 1))
            scnd_mug.thisown = 0
            self.myself.add_event (scnd_mug)
            
        walk_event = adonthell.time_event (delay)
        walk_event.set_callback (self.walk)
        walk_event.thisown = 0
        self.myself.add_event (walk_event)

    # -- put/remove something from the table we're standing next to
    def put_object (self, args):
        object, update = args[:]
        
        # -- the table we're next to
        index = self.myself.get_val ("table_num")
        if index > 0:
            # -- see whether table is laid or not
            key = "table%i_set" % index
            val = self.myself.get_val (key)

            x, y = self.coords[index+4][:2]
            if val == 0:
                adonthell.gamedata_engine ().get_landmap ().put_mapobject (1, x, y, object)
                if update == 1: self.myself.set_val (key, 1)
            else:
                adonthell.gamedata_engine ().get_landmap ().remove_mapobject (1, x, y, object)
                if update == 1: self.myself.set_val (key, 0)
