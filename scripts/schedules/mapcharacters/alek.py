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

# -- Movement schedule for Alek Endhelm
#
#    He'll walk between his table and the bar

import adonthell
import schedule
import random

def _(message): return message

class alek (schedule.speak):
    
    def __init__ (self, mapcharacterinstance):
        self.myself = mapcharacterinstance
        
        # -- make random remarks
        self.speech = [_("More Ale!"), \
                       _("I'll cut 'em open like ripe fruits."), \
                       _("They should sort out this business like real men!")]
        self.speech_delay = (20, 40)
        schedule.speak.__init__(self)
    
        self.myself.set_callback (self.goal_reached)
       
    def walk (self):
        # -- walk to table
        if self.myself.posx () == 1:
            self.myself.set_goal (12, 5, adonthell.STAND_NORTH)
        # -- walk to bar
        else:
            self.myself.set_goal (1, 3, adonthell.STAND_SOUTH)

    def goal_reached (self):
        delay = "%it" % random.randrange (65, 90)
        self.myself.time_callback (delay, self.walk)
