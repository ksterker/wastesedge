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

# -- Movement schedule for Tristan Illig
#
#    Illig will either be in the common room or outside at the gate.


import adonthell
import schedule
import random

def _(message): return message

class tristan (schedule.speak):

    def __init__ (self, mapcharacterinstance):
        self.myself = mapcharacterinstance

        # -- make random remarks
        self.speech = [_("Don't they know that I am losing money by the hour!?"), \
                       _("What a fuss about a few worthless gems!"), \
                       _("Ye gods! It cannot be that hard to find the thief!")]
        self.speech_delay = (20, 55)
        schedule.speak.__init__(self)
        
        # -- walking
        self.walk_event = adonthell.time_event ("35t")
        self.walk_event.set_callback (self.walk)
        adonthell.event_handler_register_event (self.walk_event)
        self.myself.set_callback (self.goal_reached)

    def walk (self):
        # -- in common room -> go outside
        if self.myself.submap () == 1 and \
            adonthell.gamedata_get_quest ("demo").get_val ("intro_on") == 0:
            self.myself.set_goal (13, 8, adonthell.STAND_SOUTH)
            self.walk_delay = "%it" % random.randint (60, 90)

        # -- outside -> goto common room
        else:
            self.myself.set_goal (18, 13, adonthell.STAND_NORTH)
            self.walk_delay = "%it" % random.randint (45, 90)
    
    def goal_reached (self):
        # -- reached common room
        if self.myself.submap () == 1 and self.myself.posx () == 13:
            self.myself.set_goal (4, 6, adonthell.STAND_WEST)
        # -- reached yard
        elif self.myself.submap () == 0 and self.myself.posx () == 18:
            self.myself.set_goal (12, 18, adonthell.STAND_WEST)
        # -- reached our final destination
        else:
            self.walk_event = adonthell.time_event (self.walk_delay)
            self.walk_event.set_callback (self.walk)
            adonthell.event_handler_register_event (self.walk_event)
