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

# -- Map Event to make a character say something.

import adonthell

class character_speak:

    # Parameters:
    # name: name of the character that should speak when the event is triggered
    # sentence: sentence to say when the event is triggered
    def __init__ (self, eventinstance, name, sentence):
        self.myself = eventinstance
        self.mapchar = adonthell.gamedata_get_character (name)
        self.sentence = sentence

    def run (self, submap, x, y, dir, name):
        self.mapchar.speak (self.sentence)
