#
#  (C) Copyright 2002 Kai Sterker <kaisterker@linuxgames.com>
#  Part of the Adonthell Project http://adonthell.linuxgames.com
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License.
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY.
#
#  See the COPYING file for more details
#

# -- Map Event for initiating dialogue with a character.

import adonthell

class speak:

    # Parameters:
    # speaker: name of character that shall speak
    def __init__ (self, eventinstance, speaker):
        self.speaker = adonthell.gamedata_get_character (speaker)
    
    def run (self, submap, x, y, dir, name):
        self.speaker.launch_action (adonthell.gamedata_player ())
