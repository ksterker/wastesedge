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


# -- Borders of the area he should stay in
min_x = 1
max_x = 6
min_y = 2
max_y = 6

speech = ["Ruffinans, the lot of them!", \
          "How dare they imprison one better than they?", \
          "This is an insult to all of the High Born.", \
          "I cannot believe such disrespect. Barbarians!"]


# -- delay for orientation change
delay = myself.get_val ("delay")

# -- switch orientation
if delay == 0:
    # -- get the current direction ...
    dir = myself.get_val ("direction")

    # -- ... and set the new one accordingly
    if dir == WALK_EAST or dir == WALK_WEST:
        dir = randint (WALK_NORTH, WALK_SOUTH)
    else:
        dir = randint (WALK_WEST, WALK_EAST)

    # -- time until the next orientation change
    delay = randint (100, 200) * 15
    myself.set_val ("direction", dir)
    myself.set_val ("delay", delay)
    myself.set_val ("todo", 1)

else:
    myself.set_val ("delay", delay - 1)


todo = myself.get_val ("todo")

# -- waiting
if todo == 0:
    # -- delay for direction change
    delay = myself.get_val ("switch_direction")

    if delay == 0:
        myself.set_val ("todo", 1)
    else:
        myself.set_val ("switch_direction", delay - 1)

# -- get movement target
elif todo == 1:
    # -- get the current direction ...
    dir = myself.get_val ("direction")

    # -- switch direction
    if dir == WALK_NORTH:
        goal = (myself.posx (), min_y, STAND_SOUTH, 0, 1)
    elif dir == WALK_SOUTH:
        goal = (myself.posx (), max_y, STAND_NORTH, 0, -1)
    elif dir == WALK_EAST:
        goal = (max_x, myself.posy(), STAND_WEST, -1, 0)
    else:
        goal = (min_x, myself.posy (), STAND_EAST, 1, 0)

    x, y, d = goal[:3]
    myself.set_val ("direction", d + 4)

    while not myself.set_goal (x, y, d):
        offx, offy = goal [-2:]
        x = x + offx
        y = y + offy

    myself.set_val ("todo", 2)

# -- move
elif todo == 2:
    if myself.follow_path () == 1:
        # -- wait a little on the current tile
        delay = randint (15, 30) * 10
        myself.set_val ("switch_direction", delay)

        myself.set_val ("todo", 0)


# -- utter a random remark
tmp = myself.get_val ("say_something")
myself.set_val ("say_something", tmp - 1)
if tmp == 0:
    myself.speak (speech[randint (0, 3)])
    delay = randint (50, 150) * 15
    myself.set_val ("say_something", delay)
