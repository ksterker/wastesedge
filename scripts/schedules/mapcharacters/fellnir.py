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

# -- Movement schedule for Fellnir Kezular
#
#    He'll busy himself in his room

import adonthell
import schedule
import random

def _(message): return message

class fellnir (schedule.speak):

    def __init__ (self, mapcharacterinstance):
        self.myself = mapcharacterinstance
        
        # -- make random remarks
        self.speech = [_("Master Orloth should throw out that brute!"), \
                       _("Take equal parts of vitriol, nitre and sal ammoniac ...")]
        self.speech_delay = (20, 40)
        schedule.speak.__init__(self)

        self.coords = [(2, 5, adonthell.STAND_EAST), \
                       (4, 4, adonthell.STAND_SOUTH), \
                       (4, 2, adonthell.STAND_NORTH), \
                       (6, 5, adonthell.STAND_WEST)]

        delay = "%it" % random.randrange (37, 75)
        self.walk_event = adonthell.time_event (delay)
        self.walk_event.set_callback (self.walk)
        adonthell.event_handler_register_event (self.walk_event)
        self.myself.set_callback (self.goal_reached)

    def walk (self):
        x, y, dir = self.coords[random.randrange (0, 4)]
        self.myself.set_goal (x, y, dir)
    
    def goal_reached (self):
        delay = "%it" % random.randrange (37, 75)
        self.walk_event = adonthell.time_event (delay)
        self.walk_event.set_callback (self.walk)
        adonthell.event_handler_register_event (self.walk_event)
