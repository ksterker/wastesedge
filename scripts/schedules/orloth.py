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

speech = ["I gotta clean this mug!", \
          "That barrel is leaking.", \
          "I hope they'll find the thief!"]

coords = [(3, 5, STAND_SOUTH), \
          (7, 6, STAND_EAST), \
          (12, 3, STAND_SOUTH), \
          (7, 4, STAND_WEST), \
          (10, 3, STAND_NORTH)]

todo = myself.get_val ("todo")

# -- waiting
if todo == 0:
    delay = myself.get_val ("delay")

    # -- If standing delay expired, move around next time
    if delay == 0:
        myself.set_val ("todo", 1)
    else:
        myself.set_val ("delay", delay - 1)

# -- engage a new movement
elif todo == 1:
    # -- when we are at the bar, then wait a while before
    #    moving again
    if myself.posx () == 2:
        x, y, dir = coords[randint (0, 4)]
        myself.set_goal (x, y, dir)
        myself.set_val ("delay", 150)

    # -- otherwise only wait a little
    else:
        delay = randint (40, 120) * 20
        myself.set_val ("delay", delay)
        myself.set_goal (2, 2, STAND_SOUTH)

    myself.set_val ("todo", 2)

# -- moving
elif todo == 2:
    if myself.follow_path () == 1:
        # -- standing in front of the clock
        if myself.posx () == 10:
            schedules.speak (myself, "That clock is late again!")

            tmp = myself.get_val ("say_something")
            myself.set_val ("say_something", tmp + 75)

        myself.set_val ("todo", 0)


# -- utter a random remark
tmp = myself.get_val ("say_something")
myself.set_val ("say_something", tmp - 1)
if tmp == 0:
    schedules.speak (myself, speech[randint (0, 2)])
    delay = randint (50, 150) * 20
    myself.set_val ("say_something", delay)
