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

# -- Movement schedule for Talan Wendth
#
#    He guards the gate

import schedules
import random

speech = ["Halt! Who goes there?", \
          "\"Ai! laurie lantar lassi surinen ...\"", \
          "Nobody may pass through the gate!"]

todo = myself.get_val ("switch_direction")

# -- calculate a new direction
if todo == 0:
    # -- the time we stay at one side of the gata
    delay = random.randint (25, 50) * 20

    # -- walk downwards
    if myself.posy () == 17:
        myself.set_val ("switch_direction", -delay)

    # -- walk upwards
    else:
        myself.set_val ("switch_direction", delay)

# -- walk downwards
elif todo < 0:
    myself.set_val ("switch_direction", todo + 1)
    if schedules.simple_goto_xy (myself, 11, 20) == 1:
        myself.stand_north ()

# -- walk upwards
else:
    myself.set_val ("switch_direction", todo - 1)
    if schedules.simple_goto_xy (myself, 11, 17) == 1:
        myself.stand_south ()

# -- utter a random remark
tmp = myself.get_val ("say_something")
myself.set_val ("say_something", tmp - 1)
if tmp == 0:
    schedules.speak (myself, speech[random.randint (0, 2)])
    delay = random.randint (40, 120) * 15
    myself.set_val ("say_something", delay)
