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

speech = ["Halt! Who goes there?", \
          "\"Ai! laurie lantar lassi surinen ...\"", \
          "Nobody may pass through the gate!"]

todo = myself.get_val ("todo")

# If standing
if todo == 0:
    delay = myself.get_val ("delay")
    # If standing delay expired, move around next time
    if delay == 0:
        myself.set_val ("todo", 1)
    else:
        myself.set_val ("delay", delay - 1)

# Moving, follow the path until it is reached.
elif todo == 2:
    # Reached the goal? Wait a while then...
    if myself.follow_path ():
        if myself.posy () == 17: myself.stand_south ()
        else: myself.stand_north ()
        import random
        myself.set_val ("delay", random.randint (25, 50) * 20)
        myself.set_val ("todo", 0)
        
        
# Engage a new movement
elif todo == 1:
    # Choose where to move, if destination is already occupied we'll
    # fall into the wait state (0) again automatically next time
    if myself.posy () == 17:
        myself.set_goal (11, 20)
    else:
        myself.set_goal (11, 17)
        
    # Next time we'll actually move!
    myself.set_val ("todo", 2)

# -- utter a random remark
tmp = myself.get_val ("say_something")
myself.set_val ("say_something", tmp - 1)
if tmp <= 0:
    import schedules
    import random
    schedules.speak (myself, speech[random.randint (0, 2)])
    delay = random.randint (50, 150) * 20
    myself.set_val ("say_something", delay)
