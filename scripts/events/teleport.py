#
#  (C) Copyright 2001 Alexandre Courbot <alexandrecourbot@linuxgames.com>
#  Part of the Adonthell Project http://adonthell.linuxgames.com
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License.
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY.
#
#  See the COPYING file for more details
#

# -- Map Event for teleporting a character.
#
#    Teleport the character that triggered this event to another position


import adonthell
import events

class teleport:

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
        events.switch_submap (adonthell.gamedata_get_character (name),
                              self.smdest, self.xdest, self.ydest, self.destdir)
