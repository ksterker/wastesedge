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

# -- Map Event to open / close the inn door.

import adonthell

class open_inn_door:

    def __init__ (self, eventinstance):
        pass

    def run (self, submap, x, y, dir, name):
        adonthell.gamedata_engine ().get_landmap ().get_mapobject (0).\
                                     get_animation (0).next_frame ()
