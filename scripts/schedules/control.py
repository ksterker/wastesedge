#
#  $Id: control.py,v 1.2 2002/08/25 15:35:53 ksterker Exp $
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

from adonthell import *

class control:

    def run (self):
        # -- bring up the main menu
        if input_has_been_pushed (SDLK_ESCAPE):
            import main_menu

            # -- create main menu without animation, 
            #    with saving and background enabled
            menu = main_menu.main_menu (1, 1, 1)

            # -- Stop updating the player
            gamedata_player ().set_schedule_active (0)
            gamedata_engine ().set_control_active (0)

            # -- open the main menu
            gamedata_engine ().main (menu, "game_menu")
            
            # -- main menu closed -> see what to do
            if menu.get_result () == 5:
                # -- quit the game
                gamedata_engine ().main_quit ()
            else:
                # -- continue
                gamedata_player ().set_schedule_active (1)
                gamedata_engine ().set_control_active (1)
           

        # -- shortcut to the load screen
        elif input_has_been_pushed (SDLK_l):
            s = data_screen (LOAD_SCREEN)
            s.set_activate (1)	

            # -- Stop updating the player
            gamedata_player ().set_schedule_active (0)
            gamedata_engine ().set_control_active (0)
            
            # -- open the load screen
            gamedata_engine ().main (s, "load_screen")
            
            # -- continue
            gamedata_player ().set_schedule_active (1)
            gamedata_engine ().set_control_active (1)
            

        # -- and to the save screen
        elif input_has_been_pushed (SDLK_s):
            s = data_screen (SAVE_SCREEN)
            s.set_activate (1)	

            # -- Stop updating the player
            gamedata_player ().set_schedule_active (0)
            gamedata_engine ().set_control_active (0)
            
            # -- open the save screen
            gamedata_engine ().main (s, "save_screen")

            # -- continue
            gamedata_player ().set_schedule_active (1)
            gamedata_engine ().set_control_active (1)


        # -- python console
        elif input_has_been_pushed (SDLK_TAB):
            import console

            c = console.console (globals ())
            c.set_activate (1)

            # -- Stop updating the player
            gamedata_player ().set_schedule_active (0)
            gamedata_engine ().set_control_active (0)

            # -- open the console
            gamedata_engine ().main (c, "console")

            # -- continue
            gamedata_player ().set_schedule_active (1)
            gamedata_engine ().set_control_active (1)
