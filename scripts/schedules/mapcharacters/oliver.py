#
#  (C) Copyright 2001/2002 Kai Sterker <kaisterker@linuxgames.com>
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

import adonthell
import schedule
import random

def _(message): return message

class oliver (schedule.speak):
    def __init__ (self, mapcharacterinstance):
        self.myself = mapcharacterinstance
        
        # -- make random remarks
        self.speech = [_("It's so exciting. An Elven Lady, here at Waste's Edge!"), \
                  _("I gotta hurry before mother complains again."), \
                  _("Why can't I have a little dog!?")]
        self.speech_delay = (20, 40)
        schedule.speak.__init__(self)
        
        # -- the tiles around Orloth
        self.offsets = [(1,1),(1,-1),(-1,1),(-1,-1),(1,0),(0,1),(-1,0),(0,-1)]


    def run (self):
        myself = self.myself
        
        # -- Oliver summoned to common room
        if myself.get_val ("goto_players_room") == 1:
            # -- beam him directly there, as it is faster that way
            if myself.submap () != 1:
                myself.jump_to (1, 13, 7, adonthell.STAND_NORTH)

            # -- find a free spot near Orloth and the player
            i = 0
            orloth = adonthell.gamedata_get_character ("Orloth Redwyne")
            while i < 7:
                x, y = self.offsets[i][:2]
                x = x + orloth.posx ()
                y = y + orloth.posy ()
                if myself.set_goal (x, y): break
                i = i + 1

            myself.set_val ("goto_players_room", 2)
            myself.set_val ("todo", 2)

        # -- in the player's room
        elif myself.get_val ("goto_players_room") == 3:
            # -- start talking to the player
            myself.launch_action (adonthell.gamedata_player ())

        # -- leave the player's room and goto the barn
        elif myself.get_val ("goto_barn") == 1:
            location = myself.submap ()
            myself.set_val ("goto_barn", 2)

            # -- Player's room
            if location == 12:
                myself.set_goal (5, 1)

            # -- First floor
            elif location == 9:
                myself.set_goal (8, 1)

            # -- Second floor (this shouldn't happen, but it once did ...)
            elif location == 14:
                myself.set_goal (4, 1)

            # -- Common Room
            elif location == 1:
                myself.set_goal (13, 8)

            # -- Yard, our final goal (for now)
            elif location == 0:
                myself.set_goal (25, 15)
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
