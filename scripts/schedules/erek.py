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

# -- Movement schedule for Erek Stonebreaker
#
#    Erek will either be in the parlour or the common room.
#    He'll also help the player to get into Bjarn's room.

import schedules
import random

speech = ["How could they do that to the Master?", \
          "This place is so much different from home.", \
          "Who could have taken the gems?"]

coords = [(5, 5, STAND_NORTH), \
          (10, 6, STAND_WEST), \
          (5, 3, STAND_NORTH), \
          (4, 5, STAND_SOUTH)]


# -- lead the player into bjarn's room
if quests["demo"].get_val ("bjarn_door_open") == 2:
    myself.set_schedule_active (0)
    # -- start Bjanr's conversation with the player and Erek
    characters["Bjarn Fingolson"].launch_action (the_player)

# -- leave cellar again
elif myself.get_val ("leave_bjarn") == 1:
    submap = myself.submap ()

    # -- in Bjarn's room
    if submap == 7:
        schedules.simple_goto_xy (myself, 0, 7)

    # -- in the Cellar
    elif submap == 4:
        schedules.simple_goto_xy (myself, 5, 2)

    # -- hopefully in the common room
    else:
        myself.set_val ("leave_bjarn", 0)
        myself.set_val ("goal", random.randint (0, 1))

# -- "normal" schedule
else:
    todo = myself.get_val ("goto_parlour")

    # switch places
    if todo == 0:
        # -- in common room -> goto parlour
        if myself.submap () == 1 \
        and schedules.simple_goto_xy (myself, 13, 4) == 1:
            # since simple_goto_xy only returns 1 if the character
            # completely occupies the tile, but the enter event is
            # raised before, we have to do the last step manually.
            myself.go_east ()
            delay = random.randint (50, 150) * -30
            myself.set_val ("goto_parlour", delay)
            myself.set_val ("goal", random.randint (2, 3))

        # -- in parlour -> goto common room
        elif schedules.simple_goto_xy (myself, 1, 4) == 1:
            myself.go_west ()
            delay = random.randint (50, 150) * 20
            myself.set_val ("goto_parlour", delay)
            myself.set_val ("goal", random.randint (0, 1))

    # -- walk up to the new pos and stay there
    else:
        # -- In parlour
        if todo < 0:
            myself.set_val ("goto_parlour", todo + 1)
        # -- In common room
        else:
            myself.set_val ("goto_parlour", todo - 1)

        goal = myself.get_val ("goal")
        x, y, dir = coords[goal]

        if schedules.simple_goto_xy (myself, x, y) == 1:
            if dir == STAND_NORTH: myself.stand_north ()
            elif dir == STAND_EAST: myself.stand_east ()
            elif dir == STAND_SOUTH: myself.stand_south ()
            else: myself.stand_west ()

    # -- do some random babbling
    tmp = myself.get_val ("say_something")
    myself.set_val ("say_something", tmp - 1)
    if tmp == 0:
        schedules.speak (myself, speech[random.randint (0, 2)])
        delay = random.randint (60, 180) * 15
        myself.set_val ("say_something", delay)
