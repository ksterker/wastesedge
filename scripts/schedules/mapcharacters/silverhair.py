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

# -- Movement schedule for Imoen Silverhair
#
#    She will mainly stand still, but occasionally walk up to the
#    window and make a remark about the weather.

import adonthell
import schedule
import random

# -- pygettext support
def _(message): return message

class silverhair (schedule.speak):

    def __init__ (self, mapcharacterinstance):
        self.myself = mapcharacterinstance
        self.speech = [_("In truth, Sarin, it is no bother. I am not offended."), \
                       _("Janesta, dear, worry not. I am content here."), \
                       _("Janesta, please bring my figurine. I wish to see it more closely."), \
                       _("It truly is a lovely day. I expect we will have time yet to enjoy it.")]
        self.speech_delay = (20, 72)
        schedule.speak.__init__(self)

        self.myself.set_callback (self.goal_reached)

    def walk (self):
        # -- goto the window
        if self.myself.posx () == 4:
            # ... and speak about the weather
            self.delay = "%it" % random.randrange (15, 22)
            self.myself.set_goal (6, 4, adonthell.STAND_EAST)

        # -- go back to our normal position
        else:
            self.delay = "%it" % random.randrange (70, 140)
            if self.myself.set_goal (4, 4, adonthell.STAND_SOUTH) == 0:
                self.myself.go_north ()
                                
    def goal_reached (self):
        # -- standing in front of the window
        if self.myself.posx () == 6:
            self.myself.speak (self.speech[3])
        
        self.myself.time_callback (self.delay, self.walk)
