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

# -- Movement schedule for Rhayne Frostbloom
#
#    She just walks around the tree in the yard

import schedules
import random

# -- Borders of the area she will stay in
min_x = 16
max_x = 24
min_y = 21
max_y = 28

speech = ["This tree is so inspiring.", \
          "I wonder why everybody seems so excited.", \
          "Do you know a creature more lovely than the yeti?"]

todo = character_base.get (myself, "stand_still")

# -- calculate a new position
if todo == 0:
    # -- the position we want to reach
    character_base.set (myself, "goal_x", random.randint (min_x, max_x))
    character_base.set (myself, "goal_y", random.randint (min_y, max_y))

    delay = random.randint (30, 90) * 30
    character_base.set (myself, "stand_still", delay)

# -- walk to the new position and wait a while
else:
    x = character_base.get (myself, "goal_x")
    y = character_base.get (myself, "goal_y")

    schedules.simple_goto_xy (myself, x, y)
    character_base.set (myself, "stand_still", todo - 1)

    # -- utter a random remark
    tmp = character_base.get (myself, "say_something")
    character_base.set (myself, "say_something", tmp - 1)
    if tmp == 0:
        schedules.speak (myself, speech[random.randint (0, 2)])
        delay = random.randint (50, 150) * 20
        character_base.set (myself, "say_something", delay)
