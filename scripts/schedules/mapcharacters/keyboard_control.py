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
            sm.get_square (6, 17).set_walkable_south (1)
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

        # -- bring up the main menu
        elif input_has_been_pushed (SDLK_ESCAPE):
            import main_menu

            # -- create main menu without animation, with saving and background enabled
            menu = main_menu.main_menu (1, 1, 1)

            # -- Stop updating the map
            gamedata_engine ().set_update_map (0)

            # -- open the main menu
            gamedata_engine ().main (menu, "game_menu")
            
            # -- main menu closed -> see what to do
            if menu.get_result () == 5:
                # -- quit the game
                gamedata_engine ().main_quit ()
            else:
                # -- continue
                gamedata_engine ().set_update_map (1)
            
            menu = None

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

        # -- shortcut to the load screen
        elif input_has_been_pushed (SDLK_l):
            s = data_screen (LOAD_SCREEN)
            s.set_activate (1)	

            # -- Stop updating the map
            gamedata_engine ().set_update_map (0)
            
            # -- open the load screen
            gamedata_engine ().main (s, "load_screen")
            
            # -- continue
            gamedata_engine ().set_update_map (1)
            
        # -- and to the save screen
        elif input_has_been_pushed (SDLK_s):
            s = data_screen (SAVE_SCREEN)
            s.set_activate (1)	

            # -- Stop updating the map
            gamedata_engine ().set_update_map (0)
            
            # -- open the save screen
            gamedata_engine ().main (s, "save_screen")

            # -- continue
            gamedata_engine ().set_update_map (1)

        # -- python console
        elif input_has_been_pushed (SDLK_TAB):
            import console
            c = console.console (globals ())
            c.thisown = C
            # c.py_signal_connect (self.on_data_screen_close, win_event_CLOSE)
            # Stop updating the map
            # gamedata_map_engine ().set_should_update_map (0)
            c.set_activate (1)
            win_manager_add (c)
            win_manager_set_focus (c)
            c = None
