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

# -- Map Event to teleport a character from Silverhair's room onto veranda

import adonthell
import events

class silverhair_to_brn:

    # Parameters:
    # smdest: destination submap
    # xdest: X position on smdest
    # ydest: Y position on smdest
    # destdir: direction where to look at after the teleport
    def __init__ (self, eventinstance, smdest, xdest, ydest, destdir):
        self.smdest = smdest
        self.xdest = xdest
        self.ydest = ydest
        self.destdir = destdir

    def run (self, submap, x, y, dir, name):
        # -- just arrived -> do nothing
        if dir == adonthell.STAND_WEST: return
        
        p = adonthell.gamedata_get_character (name)

        if p.get_val ("came_from_barn") == 1:
            p.set_val ("came_from_barn", 0)
            p.set_val ("on_veranda", 1)
            
            events.switch_submap (p, self.smdest, self.xdest, self.ydest, self.destdir)
            adonthell.audio_fade_out_background (500)
