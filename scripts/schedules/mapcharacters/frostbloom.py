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

# -- Movement schedule for Rhayne Frostbloom
#
#    She just walks around the tree in the yard

import adonthell
import schedule
import random

def _(message): return message

class frostbloom (schedule.speak):
    
    def __init__ (self, mapcharacterinstance):
        self.myself = mapcharacterinstance
        
        # -- Borders of the area she will stay in
        self.min_x = 16
        self.max_x = 25
        self.min_y = 21
        self.max_y = 29

        # -- make random remarks
        self.speech = [_("This tree is so inspiring."), \
                  _("I wonder why everybody seems so excited."), \
                  _("Do you know a creature more lovely than the yeti?")]
        self.speech_delay = (20, 55)
        schedule.speak.__init__(self)
        
        delay = "%it" % random.randrange (20, 50)
        self.walk_event = adonthell.time_event (delay)
        self.walk_event.set_callback (self.walk)
        adonthell.event_handler_register_event (self.walk_event)
        self.myself.set_callback (self.goal_reached)

    def walk (self):
        # -- the position we want to reach
        x = random.randrange (self.min_x, self.max_x)
        y = random.randrange (self.min_y, self.max_y)

        self.myself.set_goal (x, y)
    
    def goal_reached (self):
        delay = "%it" % random.randrange (20, 50)
        self.walk_event = adonthell.time_event (delay)
        self.walk_event.set_callback (self.walk)
        adonthell.event_handler_register_event (self.walk_event)
