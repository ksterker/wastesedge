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

# -- Movement schedule for Erek Stonebreaker
#
#    Erek will either be in the parlour or the common room.
#    He'll also help the player to get into Bjarn's room.

import adonthell
import schedule
import random

def _(message): return message

class erek (schedule.speak):

    def __init__ (self, mapcharacterinstance):
        self.myself = mapcharacterinstance

        # -- make random remarks
        self.speech = [_("How could they do that to the Master?"), \
                  _("This place is so much different from home."), \
                  _("Who could have taken the gems?")]
        self.speech_delay = (20, 40)
        schedule.speak.__init__(self)
        
        # -- the coordinates for normal schedule
        self.coords = \
            [(5, 5, adonthell.STAND_NORTH), \
            (10, 6, adonthell.STAND_WEST), \
            (5, 3, adonthell.STAND_NORTH), \
            (4, 5, adonthell.STAND_SOUTH)]

        # -- the coordinates for getting back to common room
        self.to_common = \
            [(0, 7, adonthell.STAND_WEST), \
            (6, 1, adonthell.STAND_NORTH)]

        # -- the coordinates for getting back to the 1st floor
        self.to_1st = \
            [(0, 7, adonthell.STAND_WEST), \
            (6, 1, adonthell.STAND_NORTH), \
            (12, 1, adonthell.STAND_NORTH), \
            (2, 4, adonthell.STAND_SOUTH)]

        self.index = 0

    def run (self):
        myself = self.myself
        
        # -- lead the player into bjarn's room
        if adonthell.gamedata_get_quest ("demo").get_val ("bjarn_door_open") == 2:
            myself.set_schedule_active (0)
            # -- start Bjanr's conversation with the player and Erek
            fingolson = adonthell.gamedata_get_character ("Bjarn Fingolson")
            fingolson.launch_action (adonthell.gamedata_player ())

        # -- help the player with jelom
        elif adonthell.gamedata_get_quest ("demo").get_val ("convince_jelom") == 2:
            myself.set_schedule_active (0)
            # -- start Jelom's conversation with the player and Erek
            jelom = adonthell.gamedata_get_character ("Jelom Rasgar")
            jelom.launch_action (adonthell.gamedata_player ())

        # -- leave Bjarn's room
        elif myself.get_val ("leave_bjarn") == 1:
            goto = myself.get_val ("goto")
            myself.set_val ("delay", 0)

            # -- goto first floor
            if goto == 9: coords = self.to_1st
            # -- goto common room
            else: coords = self.to_common

            if self.index < len (coords):
                myself.set_val ("leave_bjarn", 2)
                x, y, dir = coords[self.index]
                myself.set_goal (x, y, dir)

            # -- arrived
            else:
                myself.set_val ("leave_bjarn", 0)
                if myself.submap () == 1:
                    x, y, dir = self.coords[random.randrange (0, 2)]
                    myself.set_goal (x, y, dir)
                else:
                    myself.set_schedule_active (0)

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
            if myself.get_val ("leave_bjarn") == 2:
                myself.set_val ("leave_bjarn", 1)
                self.index = self.index + 1

            # -- switch places
            else:
                # -- in common room -> goto parlour
                if myself.submap () == 1:
                    myself.set_goal (14, 4, adonthell.STAND_EAST)

                # -- in parlour -> goto common room
                else:
                    myself.set_goal (0, 4, adonthell.STAND_WEST)

            myself.set_val ("todo", 2)

        # -- move
        elif todo == 2:
            if myself.follow_path () == 1:
                # -- reached common room
                if myself.submap () == 1 and myself.posx () == 13:
                    x, y, dir = self.coords[random.randrange (0, 2)]
                    myself.set_goal (x, y, dir)

                    delay = random.randrange (50, 150) * 20
                    myself.set_val ("delay", delay)

                # -- reached parlour
                elif myself.submap () == 2 and myself.posx () == 1:
                    x, y, dir = self.coords[random.randrange (2, 4)]
                    myself.set_goal (x, y, dir)

                    delay = random.randrange (60, 180) * 30
                    myself.set_val ("delay", delay)

                # -- reached our final destination
                else:
                    myself.set_val ("todo", 0)
