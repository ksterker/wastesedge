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

from adonthell import STAND_EAST, STAND_SOUTH
from random import randint

class silverhair:

    def __init__ (self, mapcharacterinstance):
        self.myself = mapcharacterinstance
        self.speech = ["In truth, Sarin, it is no bother. I am not offended.", \
                       "Janesta, dear, worry not. I am content here.", \
                       "Janesta, please bring my figurine. I wish to see it more closely.", \
                       "It truly is a lovely day. I expect we will have time yet to enjoy it."]

    def run (self):
        myself = self.myself

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
            # -- goto the window
            if myself.posx () == 4:
                # ... and speak about the weather
                say = randint (33, 66) * 10
                delay = randint (50, 75) * 15
                myself.set_val ("say_something", say)
                myself.set_goal (6, 4, STAND_EAST)

            # -- go back to our normal position
            else:
                say = randint (33, 66) * 10
                delay = randint (100, 200) * 35
                if myself.set_goal (4, 4, STAND_SOUTH) == 0:
                    return

            myself.set_val ("say_something", say)
            myself.set_val ("delay", delay)
            myself.set_val ("todo", 2)

        # -- move
        elif todo == 2:
            if myself.follow_path () == 1:
                myself.set_val ("todo", 0)

        # -- speak
        say = myself.get_val ("say_something")
        myself.set_val ("say_something", say - 1)
        if say == 0:
            if myself.posx () == 6:
                myself.speak (self.speech[3])
            else:
                myself.speak (self.speech[randint (0, 2)])

            say = randint (60, 180) * 20
            myself.set_val ("say_something", say)
