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

# -- Movement schedule for Orloth Redwyne
#
#    He'll walk up to a table occasionally and either set or clean it
#    From time to time he'll complain about the grandfather clock

import schedules
import random

speech = ["I gotta clean this mug!", \
          "That barrel is leaking.", \
          "I hope they'll find the thief!"]

coords = [(3, 5, STAND_SOUTH), \
          (7, 6, STAND_EAST), \
          (12, 3, STAND_SOUTH), \
          (7, 4, STAND_WEST), \
          (10, 3, STAND_NORTH)]

todo = myself.get_val ("wait_behind_bar")

# -- leave the bar
if todo == 0:
    # -- get the position we want to reach
    goal = myself.get_val ("goal")
    x, y, dir = coords[goal]

    if schedules.simple_goto_xy (myself, x, y) == 1:
        # -- wait a little
        myself.set_val ("wait_behind_bar", -150)

        if dir == STAND_NORTH: myself.stand_north ()
        elif dir == STAND_EAST: myself.stand_east ()
        elif dir == STAND_SOUTH: myself.stand_south ()
        else: myself.stand_west ()

        # -- standing in front of the clock
        if goal == 4:
            schedules.speak (myself, "That clock is late again!")


# -- stand still
elif todo < 0:
    myself.set_val ("wait_behind_bar", todo + 1)
    if todo == -1:
        # -- calculate the next move
        delay = random.randint (40, 120) * 20
        myself.set_val ("wait_behind_bar", delay)
        myself.set_val ("goal", random.randint (0, 4))

# -- go to/stay behind bar
else:
    myself.set_val ("wait_behind_bar", todo - 1)

    # -- reached the bar
    if schedules.simple_goto_xy (myself, 2, 2) == 1:
        myself.stand_south ()

    # -- utter a random remark
    tmp = myself.get_val ("say_something")
    myself.set_val ("say_something", tmp - 1)
    if tmp == 0:
        schedules.speak (myself, speech[random.randint (0, 2)])
        delay = random.randint (50, 150) * 20
        myself.set_val ("say_something", delay)
