from adonthell import *

class keyboard_control:

    def __init__ (self, mapcharinstance):
        self.myself = mapcharinstance

    # -- When the menu is closing, react accordingly
    def on_menu_close (self, retval, player):
        # Tells the map engine to update the map
        gamedata_map_engine ().set_should_update_map (1)
        # -- Quit was selected, so that's what we do :)
        if retval == 5:
            gamedata_map_engine ().quit ()
            
    # Reactivate map update when data_screen closed
    def on_data_screen_close (self, retval):
        gamedata_map_engine ().set_should_update_map (1)
                
    # Opens the gate
    def open_gate (self):
        # Get the mapobjects
        gate_fore = gamedata_map_engine ().get_landmap ().get_mapobject (90)
        gate_back = gamedata_map_engine ().get_landmap ().get_mapobject (89)
                    
        # Only open the gate if it's closed...
        if (gate_fore.get_animation (0).currentframe () == 0):
            # Plays the gate back animation
            gate_back.get_animation (0).next_frame ()
            # Plays the gate fore animation
            gate_fore.get_animation (0).next_frame ()
                        
            # Update squares walkability
            sm = gamedata_map_engine ().get_landmap ().get_submap (0)
            sm.get_square (6, 17).set_walkable_south (0)
            sm.get_square (7, 17).set_walkable_south (0)
            sm.get_square (6, 18).set_walkable_west (1)
            sm.get_square (6, 19).set_walkable_west (1)
                        
    # Close the gate
    def close_gate (self):
        # Get the mapobjects
        gate_fore = gamedata_map_engine ().get_landmap ().get_mapobject (90)
        gate_back = gamedata_map_engine ().get_landmap ().get_mapobject (89)
                            
        # Only close the gate if it's opened
        if (gate_fore.get_animation (0).currentframe () == 4):
            # Plays the gate back animation
            gate_back.get_animation (0).next_frame ()
            # Plays the gate fore animation
            gate_fore.get_animation (0).next_frame ()

            # Update squares walkability
            sm = gamedata_map_engine ().get_landmap ().get_submap (0)
            sm.get_square (6, 17).set_walkable_south (1)
            sm.get_square (7, 17).set_walkable_south (1)
            sm.get_square (6, 18).set_walkable_west (0)
            sm.get_square (6, 19).set_walkable_west (0)
            sm.get_square (6, 20).set_walkable_west (0)


    def run (self):
        if input_has_been_pushed (SDLK_h):
            gamedata_map_engine ().set_mapview_schedule ("center_character",
                                                         ("Talan Wendth",))
            gamedata_player ().set_schedule ("")
            gamedata_get_character ("Talan Wendth").set_schedule ("keyboard_control")

        if input_has_been_pushed (SDLK_g):
            gamedata_map_engine ().set_mapview_schedule ("center_character",
                                                         (gamedata_player ().get_name (),))
            gamedata_player ().set_schedule ("keyboard_control")
            gamedata_get_character ("Talan Wendth").set_schedule ("talan")

        if input_has_been_pushed (SDLK_o):
            self.open_gate ()

        if input_has_been_pushed (SDLK_c):
            self.close_gate ()

        # -- react to the action key
        if input_has_been_pushed (SDLK_SPACE):
            # -- see whether a character(/object) is next to the player
            p = self.myself.whosnext ()

            # - Yes :)
            if p != None and p.currentmove() < WALK_NORTH:
                # -- launch the other guy's (object's) action script
                p.launch_action (self.myself)

                # -- Cleanup
                p = None
            elif p == None:
                evt = action_event ()
                evt.submap = self.myself.submap ()
                evt.x = self.myself.posx ()
                evt.y = self.myself.posy ()
                evt.dir = self.myself.currentmove ()
                evt.c = self.myself
                event_handler_raise_event (evt)

        # -- bring up the main menu
        elif input_has_been_pushed (SDLK_ESCAPE):
            import main_menu

            # -- open main menu without animation, with saving and background enabled
            menu = main_menu.main_menu (1, 1, 1)
            menu.thisown = C

            # Stop updating the map
            gamedata_map_engine ().set_should_update_map (0)

            # -- this tells us when the main menu is closed
            menu.py_signal_connect (self.on_menu_close, win_event_CLOSE, (self.myself))

            # -- add stuff to the win_manager
            win_manager_add (menu)
            win_manager_set_focus (menu)
            menu = None

        # -- move the player around
        if input_is_pushed (SDLK_UP): self.myself.go_north ()
        elif input_is_pushed (SDLK_DOWN): self.myself.go_south ()
        elif input_is_pushed (SDLK_RIGHT): self.myself.go_east ()
        elif input_is_pushed (SDLK_LEFT): self.myself.go_west ()

        # Special tip! :)
        elif input_has_been_pushed (SDLK_n):
            if self.myself.submap () < gamedata_map_engine ().get_landmap ().nbr_of_submaps () - 1:
                self.myself.jump_to (self.myself.submap () + 1, 5, 3)
            else:
                self.myself.jump_to (0, 7, 18)

        elif input_has_been_pushed (SDLK_p):
            if self.myself.submap () > 1:
                self.myself.jump_to (self.myself.submap () - 1, 5, 3)
            elif self.myself.submap () == 1:
                self.myself.jump_to (0, 7, 18)
            else:
                self.myself.jump_to (gamedata_map_engine ().get_landmap ().nbr_of_submaps () - 1, 5, 3)

        # -- shortcut to the load screen
        elif input_has_been_pushed (SDLK_l):
            s = data_screen (LOAD_SCREEN)
            s.thisown = C
            s.py_signal_connect (self.on_data_screen_close, win_event_CLOSE)
            # Stop updating the map
            gamedata_map_engine ().set_should_update_map (0)
            s.set_activate (1)	
            win_manager_add (s)
            win_manager_set_focus (s)


        # -- and to the save screen
        elif input_has_been_pushed (SDLK_s):
            s = data_screen (SAVE_SCREEN)
            s.thisown = C
            s.py_signal_connect (self.on_data_screen_close, win_event_CLOSE)
            # Stop updating the map
            gamedata_map_engine ().set_should_update_map (0)
            s.set_activate (1)	
            win_manager_add (s)
            win_manager_set_focus (s)


        # -- python console
        elif input_has_been_pushed (SDLK_TAB):
            import console
            c = console.console (globals ())
            c.thisown = C
            c.py_signal_connect (self.on_data_screen_close, win_event_CLOSE)
            # Stop updating the map
            gamedata_map_engine ().set_should_update_map (0)
            c.set_activate (1)
            win_manager_add (c)
            win_manager_set_focus (c)
            c = None
