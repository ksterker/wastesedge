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

# -- Movement schedule for Oliver Redwyne
#
#    He'll walk around in the stable and yard.
#    When summoned by Orloth, he'll show the player to his room


speech = ["It's so exciting. An Elven Lady, here at Waste's Edge!", \
          "I gotta hurry before mother complains again.", \
          "Why can't I have a little dog!?"]

# -- Oliver summoned to common room
if myself.get_val ("goto_players_room") == 1:
    # -- beam him directly there, as it is faster that way
    if myself.submap () != 1:
        myself.jump_to (1, 13, 7, STAND_NORTH)

    # -- the tiles around Orloth
    offsets = [(1,1),(1,-1),(-1,1),(-1,-1),(1,0),(0,1),(-1,0),(0,-1)]

    # -- find a free spot near Orloth and the player
    i = 0
    orloth = characters["Orloth Redwyne"]
    while i < 7:
        x, y = offsets[i][:2]
        x = x + orloth.posx ()
        y = y + orloth.posy ()
        if myself.set_goal (x, y, NO_MOVE): break
        i = i + 1

    myself.set_val ("goto_players_room", 2)
    myself.set_val ("todo", 2)

# -- in the player's room
elif myself.get_val ("goto_players_room") == 3:
    # -- start talking to the player
    myself.launch_action (the_player)
    
# -- leave the player's room and goto the barn
elif myself.get_val ("goto_barn") == 1:
    location = myself.submap ()

    # -- Player's room
    if location == 12:
        myself.set_goal (5, 1, NO_MOVE)
        myself.set_val ("goto_barn", 2)

    # -- First floor
    elif location == 9:
        myself.set_goal (8, 1, NO_MOVE)
        myself.set_val ("goto_barn", 2)

    # -- Common Room
    elif location == 1:
        myself.set_goal (13, 8, NO_MOVE)
        myself.set_val ("goto_barn", 2)

    # -- Yard, our final goal (for now)
    elif location == 0:
        myself.set_goal (25, 15, NO_MOVE)
        myself.set_val ("goto_barn", 0)

    myself.set_val ("todo", 2)


# -- "normal" schedule
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
    # -- on our way back from bjarn's room
    if myself.get_val ("goto_barn") == 2:
        myself.set_val ("goto_barn", 1)

# -- move
elif todo == 2:
    if myself.follow_path () == 1:
        myself.set_val ("todo", 0)


# -- do some random babbling
tmp = myself.get_val ("say_something")
myself.set_val ("say_something", tmp - 1)

if tmp == 0:
    myself.speak (speech[randint (0, 2)])
    delay = randint (80, 160) * 10
    myself.set_val ("say_something", delay)
