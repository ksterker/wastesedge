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

# -- Map Event to teleport a character into Silverhair's room, if allowed.
#
#    Teleport the character that triggered this event to another position
#    if silverhair is considered as innocent by Jelom.

import adonthell
import events

class fst_to_silverhair:

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

        free = adonthell.gamedata_get_quest ("demo").get_val("silverhair_free")

        # -- Jelom not convinced of Silverhair's innocence
        if not free and p.get_name () == adonthell.gamedata_player ().get_name ():
            # -- we only need that for the dialogue, ...
            p.set_val ("at_silverhairs_door", 1)
            p.stand ()
            p.go_north ()
            adonthell.gamedata_get_character ("Jelom Rasgar").launch_action (p)
            # -- ... so remove it again afterwards
            p.set_val ("at_silverhairs_door", 0)
        else:
            events.switch_submap (p, self.smdest, self.xdest, self.ydest, self.destdir)
            adonthell.audio_fade_out_background (500)