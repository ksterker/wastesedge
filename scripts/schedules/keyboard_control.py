from main_menu import *

# -- When the menu is closing, react accordingly
def on_menu_close (retval, player):
    # -- Reactivate the player's schedule
#    player.set_schedule_active (1)
    # -- Quit was selected, so that's what we do :)
    if retval == 5:
        map_engine.quit ()

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
    # -- deactivate the player's schedule, so he can't move while the menu is open
#    myself.set_schedule_active (0)

    # -- open main menu without animation, with saving and background enabled
    	#print "rt"
    menu = main_menu (1, 1, 1)
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


# -- shortcut to the load screen
elif input_has_been_pushed (SDLK_l):
    # myself.set_schedule_active (0)
    s = data_screen (LOAD_SCREEN)
    s.thisown = 0
    s.set_activate (1)	
#    s.py_signal_connect (on_data_screen_close, win_event_CLOSE, (None))
    
    win_manager_add (s)
    win_manager_set_focus (s)


# -- and to the save screen
elif input_has_been_pushed (SDLK_s):
    # myself.set_schedule_active (0)

    s = data_screen (SAVE_SCREEN)
    s.thisown = 0
    s.set_activate (1)	
#    s.py_signal_connect (on_menu_close, win_event_CLOSE, (myself))
    win_manager_add (s)
    win_manager_set_focus (s)
