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

# -- Movement schedule for Alek Endhelm
#
#    He'll walk between his table and the bar

import schedules
import random

speech = ["   More Ale!", \
          "I'll cut 'em open like ripe fruits.", \
          "They should sort out this business like real men!"]

todo = myself.get_val ("switch_direction")

# -- calculate a new direction
if todo == 0:
    # -- the time we stay at one side of the gata
    delay = random.randint (60, 150) * 20

    # -- walk to table
    if myself.posx () == 1:
        myself.set_val ("switch_direction", -delay)

    # -- walk to bar
    else:
        myself.set_val ("switch_direction", delay)

# -- walk to table
elif todo < 0:
    myself.set_val ("switch_direction", todo + 1)
    if schedules.simple_goto_xy (myself, 12, 5) == 1:
        myself.stand_north ()

# -- walk to bar
else:
    myself.set_val ("switch_direction", todo - 1)
    if schedules.simple_goto_xy (myself, 1, 3) == 1:
        myself.stand_south ()

# -- utter a random remark
tmp = myself.get_val ("say_something")
myself.set_val ("say_something", tmp - 1)
if tmp == 0:
    schedules.speak (myself, speech[random.randint (0, 2)])
    delay = random.randint (40, 80) * 25
    myself.set_val ("say_something", delay)
