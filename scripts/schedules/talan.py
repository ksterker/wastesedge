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

def init ():
    speech = ["Halt! Who goes there?", \
              "\"Ai! laurie lantar lassi surinen ...\"", \
              "Nobody may pass through the gate!"]

def run ():
    todo = myself.get_val ("todo")

    # If standing
    if todo == 0:
        delay = myself.get_val ("delay")
        # If standing delay expired, move around next time
        if delay == 0:
            myself.set_val ("todo", 1)
        else:
            myself.set_val ("delay", delay - 1)

    # Engage a new movement
    elif todo == 1:
        # Choose where to move, if destination is already occupied we'll
        # fall into the wait state (0) again automatically next time
        if myself.posy () == 17:
            myself.set_goal (11, 19, STAND_NORTH)
        else:
            myself.set_goal (11, 17, STAND_SOUTH)

        # Next time we'll actually move!
        myself.set_val ("todo", 2)

    # Moving, follow the path until it is reached.
    elif todo == 2:
        # Reached the goal? Wait a while then...
        if myself.follow_path ():
            myself.set_val ("delay", randint (25, 50) * 20)
            myself.set_val ("todo", 0)


    # -- utter a random remark
    tmp = myself.get_val ("say_something")
    myself.set_val ("say_something", tmp - 1)
    if tmp <= 0:
        myself.speak (speech[randint (0, 2)])
        delay = randint (50, 150) * 20
        myself.set_val ("say_something", delay)
