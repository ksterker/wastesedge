# -- When the menu is closing, react accordingly
def on_menu_close (retval, player):
    # -- Reactivate the player's schedule
#    player.set_schedule_active (1)
    # -- Quit was selected, so that's what we do :)
    if retval == 5:
        map_engine.quit ()

# Opens the gate
def open_gate ():
    # Get the mapobjects
    gate_fore = map_engine.get_landmap ().get_mapobject (90)
    gate_back = map_engine.get_landmap ().get_mapobject (89)

    # Only open the gate if it's closed...
    if (gate_fore.get_animation (0).currentframe () == 0):
        # Plays the gate back animation
        gate_back.get_animation (0).next_frame ()
        # Plays the gate fore animation
        gate_fore.get_animation (0).next_frame ()

        # Update squares walkability
        sm = map_engine.get_landmap ().get_submap (0)
        sm.get_square (6, 18).set_walkable_west (1)
        sm.get_square (6, 19).set_walkable_west (1)
        sm.get_square (6, 20).set_walkable_west (1)

# Close the gate
def close_gate ():
    # Get the mapobjects
    gate_fore = map_engine.get_landmap ().get_mapobject (90)
    gate_back = map_engine.get_landmap ().get_mapobject (89)

    # Only close the gate if it's opened
    if (gate_fore.get_animation (0).currentframe () == 4):
        # Plays the gate back animation
        gate_back.get_animation (0).next_frame ()
        # Plays the gate fore animation
        gate_fore.get_animation (0).next_frame ()

        # Update squares walkability
        sm = map_engine.get_landmap ().get_submap (0)
        sm.get_square (6, 18).set_walkable_west (0)
        sm.get_square (6, 19).set_walkable_west (0)
        sm.get_square (6, 20).set_walkable_west (0)

#print "%d %d %d" % (myself.submap (), myself.posx (), myself.posy ())

if input_has_been_pushed (SDLK_o):
    open_gate ()

if input_has_been_pushed (SDLK_c):
    close_gate ()

# -- react to the action key
if input_has_been_pushed (SDLK_SPACE):
    # -- see whether a character(/object) is next to the player
    p = myself.whosnext ()

    # - Yes :)
    if p != None and p.currentmove() < WALK_NORTH:
        # -- launch the other guy's (object's) action script 
        p.launch_action (myself)

        # -- Cleanup
        p = None

# -- bring up the main menu
elif input_has_been_pushed (SDLK_ESCAPE):
    import main_menu

    # -- open main menu without animation, with saving and background enabled
    menu = main_menu.main_menu (1, 1, 1)
    menu.thisown = C

    # -- this tells us when the main menu is closed
    menu.py_signal_connect (on_menu_close, win_event_CLOSE, (myself))

    # -- add stuff to the win_manager
    win_manager_add (menu)
    win_manager_set_focus (menu)
    menu = None

# -- move the player around
elif input_is_pushed (SDLK_UP): myself.go_north ()
elif input_is_pushed (SDLK_DOWN): myself.go_south ()
elif input_is_pushed (SDLK_RIGHT): myself.go_east ()
elif input_is_pushed (SDLK_LEFT): myself.go_west ()

# Special tip! :)
elif input_has_been_pushed (SDLK_n):
    if myself.submap () < map_engine.get_landmap ().nbr_of_submaps () - 1:
        myself.jump_to (myself.submap () + 1, 5, 3)
    else:
        myself.jump_to (0, 7, 18)

elif input_has_been_pushed (SDLK_p):
    if myself.submap () > 1:
        myself.jump_to (myself.submap () - 1, 5, 3)
    elif myself.submap () == 1:
        myself.jump_to (0, 7, 18)        
    else:
        myself.jump_to (map_engine.get_landmap ().nbr_of_submaps () - 1, 5, 3)

# -- shortcut to the load screen
elif input_has_been_pushed (SDLK_l):
    s = data_screen (LOAD_SCREEN)
    s.thisown = C
    s.set_activate (1)	
    win_manager_add (s)
    win_manager_set_focus (s)


# -- and to the save screen
elif input_has_been_pushed (SDLK_s):
    s = data_screen (SAVE_SCREEN)
    s.thisown = C
    s.set_activate (1)	
    win_manager_add (s)
    win_manager_set_focus (s)


# -- python console
elif input_has_been_pushed (SDLK_TAB):
    import console
    c = console.console (globals ())
    c.thisown = C
    c.set_activate (1)
    win_manager_add (c)
    win_manager_set_focus (c)
    c = None
