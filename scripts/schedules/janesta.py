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

# -- Movement schedule for Janesta Skywind
#
#    She'll busy herself in Silverhair's room


speech = ["Oh, dear. Oh, dear.", \
          "What will happen to us if they take the Mistress?", \
          "I must do something about this awful room.", \
          "Oh, how do they expect us to live decently in a place like this?"]

coords = [(1, 3, STAND_NORTH), \
          (6, 3, STAND_NORTH), \
          (1, 5, STAND_SOUTH), \
          (4, 2, STAND_WEST)]

todo = myself.get_val ("todo")

# -- waiting
if todo == 0:
    delay = myself.get_val ("delay")
    # If standing delay expired, move around next time
    if delay == 0:
        myself.set_val ("todo", 1)
    else:
        myself.set_val ("delay", delay - 1)

# -- engage a new movement
elif todo == 1:
    x, y, dir = coords[randint (0, 3)]

    myself.set_goal (x, y, dir)
    myself.set_val ("todo", 2)

# -- moving
elif todo == 2:
    if myself.follow_path () == 1:
        # -- the time we stay at the same place
        delay = randint (20, 60) * 10

        myself.set_val ("delay", delay)
        myself.set_val ("todo", 0)


# -- utter a random remark
tmp = myself.get_val ("say_something")
myself.set_val ("say_something", tmp - 1)
if tmp == 0:
    myself.speak (speech[randint (0, 3)])
    delay = randint (50, 75) * 35
    myself.set_val ("say_something", delay)
