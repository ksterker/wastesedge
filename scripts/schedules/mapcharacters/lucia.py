#
#  (C) Copyright 2001/2002 Alexandre Courbot <alexandrecourbot@linuxgames.com>
#  Part of the Adonthell Project http://adonthell.linuxgames.com
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License.
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY.
#
#  See the COPYING file for more details
#

# -- Movement schedule for Lucia Redwyne
#
# She just walk around in the kitchen, doing her business and
# complaining about her life.

import adonthell
import schedule
import random

def _(message): return message

class lucia (schedule.speak):

    def __init__ (self, mapcharacterinstance):
        self.myself = mapcharacterinstance
        
        # -- make random remarks
        self.speech = [_("When can I finally rest a bit?"), \
                       _("I told Orloth this place would bring us nothing but trouble!"), \
                       _("This smoke! I'm dying!")]
        self.speech_delay = (20, 40)
        schedule.speak.__init__(self)
        
        self.coords = [(3, 3, adonthell.STAND_NORTH), \
                  (6, 3, adonthell.STAND_EAST)]

        delay = "%it" % random.randrange (20, 40)
        walk_event = adonthell.time_event (delay)
        walk_event.set_callback (self.walk)
        walk_event.thisown = 0
        self.myself.add_event (walk_event)
        
        self.myself.set_callback (self.goal_reached)

    def walk (self):
        if self.myself.posx () != 3:
            x, y, dir = self.coords[0]
        else:
            x, y, dir = self.coords[random.randrange(0, 2)]
        self.myself.set_goal (x, y, dir)
    
    def goal_reached (self):
        # -- standing in front of the exit
        if self.myself.posx () == 6:
            self.myself.speak (_("Ah, some fresh air!"))
            delay = "8t"
        else:
            delay = "%it" % random.randrange (20, 40)
        
        walk_event = adonthell.time_event (delay)
        walk_event.set_callback (self.walk)
        walk_event.thisown = 0
        self.myself.add_event (walk_event)
