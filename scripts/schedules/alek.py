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


speech = ["More Ale!", \
          "I'll cut 'em open like ripe fruits.", \
          "They should sort out this business like real men!"]

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
    # -- walk to table
    if myself.posx () == 1:
        myself.set_goal (12, 5, STAND_NORTH)
    # -- walk to bar
    else:
        myself.set_goal (1, 3, STAND_SOUTH)

    myself.set_val ("todo", 2)

# -- moving
elif todo == 2:
    if myself.follow_path () == 1:
        # -- the time we stay at the same place
        from random import randint
        delay = randint (60, 150) * 20

        myself.set_val ("delay", delay)
        myself.set_val ("todo", 0)


# -- utter a random remark
tmp = myself.get_val ("say_something")
myself.set_val ("say_something", tmp - 1)
if tmp == 0:
    from schedules import speak
    from random import randint

    speak (myself, speech[randint (0, 2)])
    delay = randint (40, 80) * 25
    myself.set_val ("say_something", delay)
