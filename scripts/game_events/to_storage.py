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

# -- Map Event to teleport the player into the storageroom, if he has the
#    key.

import adonthell
import events

def _(message): return message

class to_storage:

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
        p = adonthell.gamedata_get_character (name)
        
        # -- pantry door closed?
        locked = adonthell.gamedata_get_quest ("demo").get_val("pantry_locked")
        if locked == 0 or locked == 1:
            adonthell.gamedata_get_quest ("demo").set_val("pantry_locked", 1)
            p.stand ()
            p.go_east ()
            p.speak (_("The door to the pantry is locked."))
        else:
            events.switch_submap (p, self.smdest, self.xdest, self.ydest, self.destdir)
