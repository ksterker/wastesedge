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

# -- Borders of the area she will stay in
min_x = 16
max_x = 24
min_y = 21
max_y = 28

speech = ["This tree is so inspiring.", \
          "I wonder why everybody seems so excited.", \
          "Do you know a creature more lovely than the yeti?"]

todo = myself.get_val ("todo")

# -- waiting
if todo == 0:
    delay = myself.get_val ("delay")

    # If standing delay expired, move around next time
    if delay == 0:
        myself.set_val ("todo", 1)
    else:
        myself.set_val ("delay", delay - 1)

# -- get movement target
elif todo == 1:
    # -- the position we want to reach
    x = randint (min_x, max_x)
    y = randint (min_y, max_y)

    myself.set_goal (x, y, NO_MOVE)

    delay = randint (30, 90) * 30
    myself.set_val ("delay", delay)
    myself.set_val ("todo", 2)

# -- walk to the new position
elif todo == 2:
    if myself.follow_path () == 1:
        myself.set_val ("todo", 0)


# -- utter a random remark
tmp = myself.get_val ("say_something")
myself.set_val ("say_something", tmp - 1)
if tmp == 0:
    schedules.speak (myself, speech[randint (0, 2)])
    delay = randint (50, 150) * 20
    myself.set_val ("say_something", delay)
