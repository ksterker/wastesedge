#
#  $Id: keyboard_control.py,v 1.6 2001/12/15 11:40:22 adondev Exp $
#
#  (C) Copyright 2001 Alexandre Courbot
#  Part of the Adonthell Project http://adonthell.linuxgames.com
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License.
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY.
#
#  See the COPYING file for more details
#

from adonthell import *

class keyboard_control:

    def __init__ (self, mapcharinstance):
        self.myself = mapcharinstance

    # Opens the gate
    def open_gate (self):
        # Get the mapobjects
        gate_fore = gamedata_engine ().get_landmap ().get_mapobject (90)
        gate_back = gamedata_engine ().get_landmap ().get_mapobject (89)
                    
        # Only open the gate if it's closed...
        if (gate_fore.get_animation (0).currentframe () == 0):
            # Plays the gate back animation
            gate_back.get_animation (0).next_frame ()
            # Plays the gate fore animation
            gate_fore.get_animation (0).next_frame ()
                        
            # Update squares walkability
            sm = gamedata_engine ().get_landmap ().get_submap (0)
            sm.get_square (6, 17).set_walkable_south (0)
            sm.get_square (7, 17).set_walkable_south (0)
            sm.get_square (6, 18).set_walkable_west (1)
            sm.get_square (6, 19).set_walkable_west (1)
                        
    # Close the gate
    def close_gate (self):
        # Get the mapobjects
        gate_fore = gamedata_engine ().get_landmap ().get_mapobject (90)
        gate_back = gamedata_engine ().get_landmap ().get_mapobject (89)
                            
        # Only close the gate if it's opened
        if (gate_fore.get_animation (0).currentframe () == 4):
            # Plays the gate back animation
            gate_back.get_animation (0).next_frame ()
            # Plays the gate fore animation
            gate_fore.get_animation (0).next_frame ()

            # Update squares walkability
            sm = gamedata_engine ().get_landmap ().get_submap (0)
            sm.get_square (6, 17).set_walkable (0)
            sm.get_square (7, 17).set_walkable_south (1)
            sm.get_square (6, 18).set_walkable_west (0)
            sm.get_square (6, 19).set_walkable_west (0)
            sm.get_square (6, 20).set_walkable_west (0)


    def run (self):
        if input_has_been_pushed (SDLK_o):
            self.open_gate ()

        if input_has_been_pushed (SDLK_c):
            self.close_gate ()

        # -- react to the action key
        if input_has_been_pushed (SDLK_SPACE):
            # -- see whether a character(/object) is next to the player
            p = self.myself.whosnext ()

            # - Yes :)
            if p != None and p.currentmove () < WALK_NORTH:
                # -- launch the other guy's (object's) action script
                p.launch_action (self.myself)

                # -- Cleanup
                p = None

            # -- otherwise launch an action event
            elif p == None:
                evt = action_event ()
                evt.submap = self.myself.submap ()
                evt.x = self.myself.posx ()
                evt.y = self.myself.posy ()
                evt.dir = self.myself.currentmove ()
                evt.c = self.myself
                event_handler_raise_event (evt)


        # -- move the player around
        if input_is_pushed (SDLK_UP): self.myself.go_north ()
        elif input_is_pushed (SDLK_DOWN): self.myself.go_south ()
        elif input_is_pushed (SDLK_RIGHT): self.myself.go_east ()
        elif input_is_pushed (SDLK_LEFT): self.myself.go_west ()

        # Special tip! :)
        elif input_has_been_pushed (SDLK_n):
            if self.myself.submap () < gamedata_engine ().get_landmap ().nbr_of_submaps () - 1:
                self.myself.jump_to (self.myself.submap () + 1, 5, 3)
            else:
                self.myself.jump_to (0, 7, 18)

        elif input_has_been_pushed (SDLK_p):
            if self.myself.submap () > 1:
                self.myself.jump_to (self.myself.submap () - 1, 5, 3)
            elif self.myself.submap () == 1:
                self.myself.jump_to (0, 7, 18)
            else:
                self.myself.jump_to (gamedata_engine ().get_landmap ().nbr_of_submaps () - 1, 5, 3)

