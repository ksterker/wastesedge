#
#  (C) Copyright 2001 Alexandre Courbot
#  Part of the Adonthell Project http://adonthell.linuxgames.com
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License.
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY.
#
#  See the COPYING file for more details
#

import adonthell

# -- switch submaps (character, new coordinates, new submap,
#    direction the character shall face)
def switch_submap (mychar, x, y, submap, dir):
    # -- deactivate schedule during teleport
    if mychar.is_schedule_activated ():
        mychar.set_schedule_active (0)
        schedule_active = 1
    else:
        schedule_active = 0

    # -- comparing mychar and player directly does not work (???)
    if mychar.get_name () == adonthell.gamedata_player ().get_name ():
        # -- fade the new submap in if we teleport the player
        adonthell.gamedata_engine ().fade_out ()
        mychar.jump_to (x, y, submap, dir)
        adonthell.gamedata_engine ().fade_in ()
    else:
        mychar.jump_to (x, y, submap, dir)

    # -- restore character's schedule
    if schedule_active == 1:
        mychar.set_schedule_active (1)
