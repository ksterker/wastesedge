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

# -- Movement schedule for Oliver Redwyne
#
#    He'll walk around in the stable and yard.
#    When summoned by Orloth, he'll show the player to his room

import schedules
import random

speech = ["It's so exciting. An Elven Lady at Waste's Edge!", \
          "I gotta hurry before mother complains again.", \
          "I want a little dog!"]

# -- Oliver summoned to common room
if myself.get_val ("goto_players_room") == 1:
    # -- beam him directly there, as it is faster that way
    if myself.submap () != 1:
        myself.jump_to (1, 13, 7, STAND_NORTH)

    goal_x = characters["Orloth Redwyne"].posx () + 1
    goal_y = characters["Orloth Redwyne"].posy () + 1

    schedules.simple_goto_xy (myself, goal_x, goal_y)

# -- in the player's room
elif myself.get_val ("goto_players_room") == 2:
    # -- start talking to the player
    myself.launch_action (the_player)
    # -- does not make a change
    myself.set_schedule_active (0)
    the_player.set_schedule_active (0)

# -- leave the player's room and goto the barn
elif myself.get_val ("goto_barn") == 1:
    location = myself.submap ()

    # -- Player's room
    if location == 12:
        schedules.simple_goto_xy (myself, 5, 1)

    # -- First floor
    elif location == 9:
        schedules.simple_goto_xy (myself, 8, 1)

    # -- Common Room
    elif location == 1:
        schedules.simple_goto_xy (myself, 13, 8)

    # -- Yard
    elif location == 0:
        if myself.posx () == 25 and myself.posy () == 15:
            myself.set_val ("goto_barn", 0)
        else:
            schedules.simple_goto_xy (myself, 25, 15)

    # -- should be outside the inn!
    else:
        myself.set_val ("goto_barn", 0)

