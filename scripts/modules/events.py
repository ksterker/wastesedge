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

from adonthell import gamedata_player, gamedata_map_engine, mapcharacter
from adonthell import screen_transition, screen_show, gametime_update
from adonthell import gametime_frames_to_do, mapengine

# -- Fade the screen out
def fade_out ():
    i = 0

    while i < 60:
        gamedata_map_engine ().mainloop ()

        screen_transition (i * 2)
        screen_show ()

        gametime_update ()
        i = i + (gametime_frames_to_do () * 2)

# -- Fade the screen in
def fade_in ():
    i = 60

    while i > 0:
        gamedata_map_engine ().mainloop ()

        screen_transition(i * 2)
        screen_show ()

        gametime_update ()
        i = i - (gametime_frames_to_do () * 2)

# -- switch submaps (character, new coordinates, new submap,
#    direction the character shall face)
def switch_submap (mychar, x, y, submap, dir):
    if mychar.is_schedule_activated ():
        mychar.set_schedule_active (0)
        mychar.stand ()
        schedule_active = 1
    else:
        schedule_active = 0

    # -- comparing mychar and player directly does not work (???)
    if mychar.get_name () == gamedata_player ().get_name ():
        mychar.set_schedule_active (0)
        mychar.stand ()
        fade_out ()
        mychar.jump_to (x, y, submap, dir)
        fade_in ()
        mychar.set_schedule_active (1)
    else:
        mychar.jump_to (x, y, submap, dir)

    if schedule_active == 1:
        mychar.set_schedule_active (1)
