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

# -- Let the player search Silverhair's chest

import adonthell

class search_chest:

    # Parameters:
    # name: name of the character that should speak when the event is triggered
    def __init__ (self, eventinstance, name):
        self.myself = eventinstance
        self.mapchar = adonthell.gamedata_get_character (name)

    def run (self, submap, x, y, dir, name):
        if adonthell.gamedata_get_quest ("demo").get_val ("get_item") == 1:
            self.mapchar.speak ("What is that!? There is one of Fingolson's gems in there!")
            adonthell.gamedata_get_quest ("demo").set_val ("get_item", 2)
            adonthell.gamedata_get_quest ("demo").set_val ("have_gem", 1)
        else:
            self.mapchar.speak ("I know this chest. The Lady uses it on her journeys.")
