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

# -- Movement schedule for Imoen Silverhair
#
#    She will mainly stand still, but occasionally walk up to the
#    window and make a remark about the weather.

import schedules
import random

speech = ["In truth, Sarin, it is no bother. I am not offended.", \
          "Janesta, dear, worry not. I am content here.", \
          "Janesta, please bring my figurine. I wish to see it more closely.", \
          "It truly is a lovely day. I expect we will have time yet to enjoy it."]

todo = myself.get_val ("say_something")

# -- utter some remark
if todo == 0:

    # -- get a random remark
    index = random.randint (0, 3)

    # -- goto the window
    if index == 3:
        delay = random.randint (33, 66) * 10
        myself.set_val ("say_something", -delay)

    else:
        # -- speak
        schedules.speak (myself, speech[index])

        # -- wait a while before saying something else
        delay = random.randint (50, 150) * 20
        myself.set_val ("say_something", delay)

# -- walk up to the window and wait a little
elif todo < 0:
    if schedules.simple_goto_xy (myself, 6, 4) == 1:
        myself.stand_east ()

        # -- speak
        if todo == -250:
            myself.stand_east ()
            schedules.speak (myself, speech[3])

        # -- leave the window
        if todo == -1:
            delay = random.randint (50, 150) * 10
            myself.set_val ("say_something", delay)
        # -- wait
        else:
            myself.set_val ("say_something", todo + 1)

# -- leave the window
else:
    myself.set_val ("say_something", todo - 1)

    # -- reached the middle of the room
    if schedules.simple_goto_xy (myself, 4, 4) == 1:
        myself.stand_south ()
