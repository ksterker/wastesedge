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

# -- Movement schedule for Sarin Trailfollower
#
#    He walks from one end of the room to the other. From time to
#    to time he'll stop and chose another direction

import schedules
import random

# -- Borders of the area he should stay in
min_x = 1
max_x = 7
min_y = 2
max_y = 6

speech = ["Ruffinans, the lot of them!", \
          "How dare they imprison one better than they?", \
          "This is an insult to all of the High Born.", \
          "I cannot believe such disrespect. Barbarians!"]

todo = myself.get_val ("switch_direction")

# -- calculate a new direction
if todo == 0:
    # -- wait until we're completely on the tile
    if schedules.simple_goto_xy (myself, myself.posx (), myself.posy ()) == 1:
        # -- get the current direction ...
        dir = myself.get_val ("direction")

        # -- ... and set the new one accordingly
        if dir == WALK_EAST or dir == WALK_WEST:
            myself.set_val ("direction", random.randint (WALK_NORTH, WALK_SOUTH))
        else:
            myself.set_val ("direction", random.randint (WALK_WEST, WALK_EAST))

        # -- wait a little on the current tile
        delay = random.randint (30, 50) * 10
        myself.set_val ("switch_direction", -delay)

        # -- time until the next direction change
        delay = random.randint (100, 200) * 15
        myself.set_val ("delay", delay)

# -- wait a moment
elif todo < 0:
    myself.set_val ("switch_direction", todo + 1)
    if todo == -1:
        delay = myself.get_val ("delay")
        myself.set_val ("switch_direction", delay)

# -- walk up to the wall, wait a little, then turn around
else:
    myself.set_val ("switch_direction", todo - 1)
    dir = myself.get_val ("direction")

    if dir == WALK_NORTH:
        if schedules.simple_goto_xy (myself, myself.posx (), min_y) == 1:
            myself.set_val ("direction", WALK_SOUTH)
            myself.set_val ("switch_direction", random.randint (-300, -150))
            myself.set_val ("delay", todo)
            myself.stand_south ()

    elif dir == WALK_SOUTH:
        if schedules.simple_goto_xy (myself, myself.posx (), max_y) == 1:
            myself.set_val ("direction", WALK_NORTH)
            myself.set_val ("switch_direction", random.randint (-300, -150))
            myself.set_val ("delay", todo)
            myself.stand_north ()

    elif dir == WALK_WEST:
        if schedules.simple_goto_xy (myself, min_x, myself.posy ()) == 1:
            myself.set_val ("direction", WALK_EAST)
            myself.set_val ("switch_direction", random.randint (-300, -150))
            myself.set_val ("delay", todo)
            myself.stand_east ()

    else:
        if schedules.simple_goto_xy (myself, max_x, myself.posy ()) == 1:
            myself.set_val ("direction", WALK_WEST)
            myself.set_val ("switch_direction", random.randint (-300, -105))
            myself.set_val ("delay", todo)
            myself.stand_west ()

    # -- utter a random remark
    tmp = myself.get_val ("say_something")
    myself.set_val ("say_something", tmp - 1)
    if tmp == 0:
        schedules.speak (myself, speech[random.randint (0, 3)])
        delay = random.randint (50, 150) * 10
        myself.set_val ("say_something", delay)
