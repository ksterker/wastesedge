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

# -- Movement schedule for Jelom Rasgar
#
#    He guards the door to Lady Silverhair's room

import adonthell
import schedule
import random

# -- pygettext support
def _(message): return message

class jelom (schedule.speak):

    def __init__ (self, mapcharacterinstance):
        self.myself = mapcharacterinstance
        
        # -- make random remarks
        self.speech = [_("Someone fetch me a drink!"), \
                       _("That'll teach them fancy Elves a lesson!"), \
                       _("Send them to the cursed island, I say!")]
        self.speech_delay = (30, 60)
        schedule.speak.__init__(self)
        
        self.myself.set_callback (self.goal_reached)

    def walk (self):
        if self.myself.posy () == 3:
            self.myself.set_goal (2, 6, adonthell.STAND_NORTH)
        else:
            self.myself.set_goal (2, 3, adonthell.STAND_SOUTH)
    
    def goal_reached (self):
        delay = "%it" % random.randrange (20, 65)
        self.myself.time_callback (delay, self.walk)
