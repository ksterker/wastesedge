#
#  $Id: intro.py,v 1.7 2002/08/19 19:59:06 ksterker Exp $
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

# -- Schedule for the player to get into the Inn after the intro

import adonthell

class intro:

    def __init__ (self, mapcharacterinstance):
        self.myself = mapcharacterinstance

        adonthell.gamedata_get_quest ("demo").set_val ("intro_on", 1)


    def run (self):
        myself = self.myself
        talk = adonthell.gamedata_get_quest ("demo").get_val ("intro_on")

        # -- first talk to talan to get into the inn
        if talk == 1:
            talan = adonthell.gamedata_get_character ("Talan Wendth")
            talan.launch_action (myself)

            adonthell.gamedata_get_quest ("demo").set_val ("intro_on", 2)

        # -- open the gate
        elif talk == 2:
        
            # -- start music
            adonthell.audio_load_background (0, "audio/at-demo-5.ogg")
            adonthell.audio_play_background (0)
            adonthell.audio_set_schedule ("in_game")
            adonthell.audio_set_schedule_active (1)
                        
            self.open_gate ()

            adonthell.gamedata_get_quest ("demo").set_val ("intro_on", 0)
            myself.set_goal (10, 18, adonthell.STAND_EAST)

        # -- move in and finally enable keyboard control
        else:
            if myself.follow_path () == 1:
                myself.set_schedule ("keyboard_control")
                self.close_gate ()
                myself.go_east ()
                talan = adonthell.gamedata_get_character ("Talan Wendth")
                talan.time_callback_string ("3t", "walk")


    # -- open the gate
    def open_gate (self):
        # Get the mapobjects
        gate_fore = adonthell.gamedata_engine ().get_landmap ().get_mapobject (90)
        gate_back = adonthell.gamedata_engine ().get_landmap ().get_mapobject (89)

        # Only open the gate if it's closed...
        if (gate_fore.get_animation (0).currentframe () == 0):
            # Plays the gate back animation
            gate_back.get_animation (0).next_frame ()
            # Plays the gate fore animation
            gate_fore.get_animation (0).next_frame ()

            # Update squares walkability
            sm = adonthell.gamedata_engine ().get_landmap ().get_submap (0)
            sm.get_square (6, 17).set_walkable_south (0)
            sm.get_square (7, 17).set_walkable_south (0)
            sm.get_square (6, 18).set_walkable_west (1)
            sm.get_square (6, 19).set_walkable_west (1)

    # Close the gate
    def close_gate (self):
        # Get the mapobjects
        gate_fore = adonthell.gamedata_engine ().get_landmap ().get_mapobject (90)
        gate_back = adonthell.gamedata_engine ().get_landmap ().get_mapobject (89)

        # Only close the gate if it's opened
        if (gate_fore.get_animation (0).currentframe () == 4):
            # Plays the gate back animation
            gate_back.get_animation (0).next_frame ()
            # Plays the gate fore animation
            gate_fore.get_animation (0).next_frame ()

            # Update squares walkability
            sm = adonthell.gamedata_engine ().get_landmap ().get_submap (0)
            sm.get_square (6, 17).set_walkable (0)
            sm.get_square (7, 17).set_walkable_south (1)
            sm.get_square (6, 18).set_walkable_west (0)
            sm.get_square (6, 19).set_walkable_west (0)
            sm.get_square (6, 20).set_walkable_west (0)
