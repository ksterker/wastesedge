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

# -- Map Event to teleport a character into Bjarn's room, if allowed.
#
#    Teleport the character that triggered this event to another position
#    if bjarn's room door is open.

import adonthell
import events

class cellar_to_bjarn:

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
        # -- bjarn's door closed?
        open = adonthell.gamedata_get_quest ("demo").get_val("bjarn_door_open")
        if open == 0 or open == 1:
            if p.get_name () == adonthell.gamedata_player ().get_name ():
                adonthell.gamedata_get_character ("Bjarn Fingolson").launch_action (p)
            p.stand ()
            p.go_west ()
        else:
            events.switch_submap (p, self.smdest, self.xdest, self.ydest, self.destdir)
