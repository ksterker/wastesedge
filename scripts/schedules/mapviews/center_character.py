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

#  Mapview schedule that makes it always center on a constructor-time
#  given mapcharacter

import adonthell

class center_character:

    # Parameters:
    # mapcharinstance: Name of the mapcharacter to follow
    def __init__ (self, mapviewinstance, mapcharname):
        self.myself = mapviewinstance
        self.tofollow = adonthell.gamedata_get_character (mapcharname)

    def run (self):
        p = self.tofollow
        self.myself.center_on(p.submap(), p.posx(),
                              p.posy(), p.offx(), p.offy())
        
