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

# -- Movement schedule for Talan Wendth
#
#    He guards the gate

import adonthell
import random
import schedule

def _(message): return message

class talan (schedule.speak):

    def __init__ (self, mapcharacterinstance):
        self.myself = mapcharacterinstance
        
        # -- make random remarks
        self.speech = [_("Halt! Who goes there?"), \
                       "\"Ai! laurie lantar lassi surinen ...\"", \
                       _("Nobody may pass through the gate!")]
        self.speech_delay = (30, 60)
        schedule.speak.__init__(self)
        
        # -- walking stuff
        self.walk_event = adonthell.time_event ("5t")
        self.walk_event.set_callback (self.walk)
        adonthell.event_handler_register_event (self.walk_event)
        self.myself.set_callback (self.goal_reached)
        
    def walk (self):
        if self.myself.posy () == 17:
            self.myself.set_goal (11, 19, adonthell.STAND_NORTH)
        else:
            self.myself.set_goal (11, 17, adonthell.STAND_SOUTH)
        
    def goal_reached (self):
        delay = "%it" % random.randrange (10, 20)
        self.walk_event = adonthell.time_event (delay)
        self.walk_event.set_callback (self.walk)
        adonthell.event_handler_register_event (self.walk_event)
