#
#  $Id: init.py,v 1.58 2001/10/17 20:58:08 adondev Exp $
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


from adonthell import *
from main_menu import *
import time

# -- Fade the screen out
def fade_out ():
    i = 0

    while i < 60:
        gamedata_map_engine ().mainloop ()

        screen_transition (i * 2)
        screen_show ()

        gametime_update ()
        i = i + (gametime_frames_to_do () * 2)

# -- Fade the screen in
def fade_in ():
    i = 60

    while i > 0:
        gamedata_map_engine ().mainloop ()

        screen_transition (i * 2)
        screen_show ()

        gametime_update ()
        i = i - (gametime_frames_to_do () * 2)

class title_screen:
    def __init__ (self):
        # -- load our music
        audio_load_background (0, "audio/at-menu-full.ogg")
        audio_load_background (1, "audio/at-dummy-1.ogg")
        audio_load_wave (0, "audio/select.wav")
        audio_load_wave (1, "audio/switch.wav")
        audio_load_wave (2, "audio/unselect.wav")

        # -- The themes and fonts we'll use
        win_manager_add_theme ("original")
        win_manager_add_theme ("silverleaf")

        win_manager_add_font ("yellow")
        win_manager_add_font ("red")
        win_manager_add_font ("violet")
        win_manager_add_font ("blue")
        win_manager_add_font ("green")
        win_manager_add_font ("white")
        win_manager_add_font ("original")
        win_manager_add_font ("silverleaf")

        # -- load our images
        self.bag_o = win_image ()
        self.bag_o.load_raw ("gfx/cutscene/jewelbag_open.img")
        self.bag_o.set_alpha (0)
        self.bag_o.move (0, 0)
        self.bag_o.pack ()
        self.bag_o.set_visible (0)

        self.bag_c = win_image ()
        self.bag_c.load_raw ("gfx/cutscene/jewelbag_closed.img")
        self.bag_c.set_visible (1)
        self.bag_c.set_alpha (0)
        self.bag_c.move (0, 0)
        self.bag_c.pack ()

        self.bag_t = win_image ()
        self.bag_t.load_raw ("gfx/cutscene/adonthell_03.img")
        self.bag_t.move (33, 86)
        self.bag_t.pack ()
        self.bag_t.set_visible (0)

        # -- create the window
        self.window = win_container ()
        self.window.move (0, 0)
        self.window.resize (320, 240)
        self.window.set_visible_border (0)

        # -- the order here is essential
        self.window.add (self.bag_c)
        self.window.add (self.bag_t)
        self.window.add (self.bag_o)

        self.window.set_activate (1)
        self.window.set_visible (1)

        self.window.py_signal_connect (self.on_update, win_event_UPDATE)
        self.window.py_signal_connect (self.on_draw, win_event_DRAW)

        self.draw_func = self.initial_fade_in

        self.alpha = 0
        self.retval = 1

        # -- let the win_manager handle everything
        win_manager_add (self.window)
        win_manager_set_focus (self.window)

        audio_play_background (0)

        # -- launch the mapengine
        gametime_start_action ()
        gamedata_map_engine ().set_should_update_map (0)
        gamedata_map_engine ().run ()

    def __del__ (self):
        print "Destructor called"

    # -- catch ESC key
    def on_update (self):
        if self.draw_func != None:
            # -- Skip intro sequence
            if input_has_been_pushed (SDLK_ESCAPE):
                self.bag_t.set_visible (0)
                self.bag_c.set_visible (0)
                self.bag_o.set_visible (1)
                self.bag_o.set_alpha (255)
                self.draw_func = None
                self.show_menu (1, 0)

        return self.retval

    # -- callback for drawing operations
    def on_draw (self):
        if self.draw_func != None:
            self.draw_func ()

    # -- Fade in closed bag
    def initial_fade_in (self):
        if self.alpha == 255:
            # -- display "Adonthell v0.3"
            self.bag_t.set_visible (1)
            self.wait_time = 30
            self.draw_func = self.wait

        else:
            # -- fade in
            self.alpha = self.alpha + gametime_frames_to_do()
            if self.alpha > 255: self.alpha = 255
            self.bag_c.set_alpha (self.alpha)

    # -- Wait self.wait_time 10th's of a second
    def wait (self):
        if self.wait_time == 0:
            # -- fade in open bag
            self.alpha = 0
            self.bag_o.set_visible (1)
            self.draw_func = self.fade_to_open

        else:
            # -- wait
            self.wait_time = self.wait_time - 1
            time.sleep (0.1)

    # -- fade over to the open bag
    def fade_to_open (self):
        if self.alpha == 255:
            # -- Those pics are no longer needed
            self.bag_t.set_visible (0)
            self.bag_c.set_visible (0)

            # -- Add the menu
            self.draw_func = None
            self.show_menu (0, 0)

        else:
            # -- fade in
            self.alpha = self.alpha + gametime_frames_to_do()
            if self.alpha > 255: self.alpha = 255
            self.bag_o.set_alpha (self.alpha)

    # -- Show the main menu
    def show_menu (self, a, b):
        self.menu = main_menu (a, b)
        self.menu.thisown = C
        self.menu.py_signal_connect (self.on_menu_close, win_event_CLOSE)

        win_manager_add (self.menu)
        win_manager_set_focus (self.menu)

    # -- on to the main menu
    def on_menu_close (self, retval):
        fade_out ()

        screen_display.fillrect (0, 0, screen_length (), screen_height (), 0)
        screen_show ()

        # -- cleanup
        win_manager_remove (self.window)

        self.window.remove (self.bag_o)
        self.window.remove (self.bag_c)
        self.window.remove (self.bag_t)

        del self.bag_o
        del self.bag_c
        del self.bag_t

        self.retval = 0
        audio_pause_music ()

        ##retval = 1

        if retval < 5:
            gamedata_map_engine ().set_should_update_map (1)

            # -- start new game
            if retval == 1:
                gamedata_load_characters (0)
                gamedata_load_quests (0)

                # let the player chose a name for his character
                from character_screen import *
                self.cs = character_screen ()
                self.cs.thisown = C
                self.cs.py_signal_connect (self.on_cs_close, win_event_CLOSE)

                win_manager_add (self.cs)
                win_manager_set_focus (self.cs)

        else:
            gamedata_map_engine ().quit ()


    def on_cs_close (self, retval):
        # Launches the intro
        import intro

        # Creates the map engine context for the game start
        gamedata_map_engine ().load_map ("test.map")
        lm = gamedata_map_engine ().get_landmap ()

        the_player = gamedata_player ()

        the_player.set_val ("gender", MALE)
        the_player.set_val ("race", HALFELF)
        the_player.load ("player.mchar")
        the_player.set_map (lm)
        the_player.jump_to (0, 11, 18, STAND_EAST)
        the_player.set_schedule ("keyboard_control")
        gamedata_map_engine ().set_mapview_schedule ("center_character", (the_player.get_name (),))

        # Setting up the map events
        # Teleport events

        # From yard to common room
        # Open the inn door event
        ev = leave_event ()
        ev.thisown = C
        ev.submap = 0
        ev.x = 18
        ev.y = 14
        ev.dir = WALK_NORTH
        ev.set_script ("open_inn_door")
        lm.add_event (ev)

        # Close the inn door event
        ev = enter_event ()
        ev.thisown = C
        ev.submap = 0
        ev.x = 18
        ev.y = 13
        ev.set_script ("open_inn_door")
        lm.add_event (ev)

        # Teleport event
        ev = enter_event ()
        ev.thisown = C
        ev.submap = 0
        ev.x = 18
        ev.y = 13
        ev.set_script ("teleport", (1, 13, 7, STAND_NORTH))
        lm.add_event (ev)

        # From common room to yard
        ev = enter_event ()
        ev.thisown = C
        ev.submap = 1
        ev.x = 13
        ev.y = 8
        ev.set_script ("teleport", (0, 18, 14, STAND_SOUTH))
        lm.add_event (ev)

        # From common room to parlor
        ev = enter_event ()
        ev.thisown = C
        ev.submap = 1
        ev.x = 14
        ev.y = 4
        ev.set_script ("teleport", (2, 1, 4, STAND_EAST))
        lm.add_event (ev)

        # From parlor to common room
        ev = enter_event ()
        ev.thisown = C
        ev.submap = 2
        ev.x = 0
        ev.y = 4
        ev.set_script ("teleport", (1, 13, 4, STAND_WEST))
        lm.add_event (ev)

        # From common room to kitchen
        ev = enter_event ()
        ev.thisown = C
        ev.submap = 1
        ev.x = 1
        ev.y = 8
        ev.set_script ("teleport", (3, 1, 2, STAND_SOUTH))
        lm.add_event (ev)

        # From kitchen to common room
        ev = enter_event ()
        ev.thisown = C
        ev.submap = 3
        ev.x = 1
        ev.y = 1
        ev.set_script ("teleport", (1, 1, 7, STAND_NORTH))
        lm.add_event (ev)

        # From kitchen to yard
        ev = enter_event ()
        ev.thisown = C
        ev.submap = 3
        ev.x = 7
        ev.y = 3
        ev.set_script ("teleport", (0, 12, 14, STAND_EAST))
        lm.add_event (ev)

        # From yard to kitchen
        ev = enter_event ()
        ev.thisown = C
        ev.submap = 0
        ev.x = 11
        ev.y = 14
        ev.set_script ("teleport", (3, 6, 3, STAND_WEST))
        lm.add_event (ev)

        # From cellar to bathroom
        ev = enter_event ()
        ev.thisown = C
        ev.submap = 4
        ev.x = 3
        ev.y = 5
        ev.set_script ("teleport", (5, 4, 6, STAND_NORTH))
        lm.add_event (ev)

        # From bathroom to cellar
        ev = enter_event ()
        ev.thisown = C
        ev.submap = 5
        ev.x = 4
        ev.y = 7
        ev.set_script ("teleport", (4, 3, 6, STAND_SOUTH))
        lm.add_event (ev)

        # From cellar to alek's
        ev = enter_event ()
        ev.thisown = C
        ev.submap = 4
        ev.x = 0
        ev.y = 6
        ev.set_script ("teleport", (6, 5, 6, STAND_WEST))
        lm.add_event (ev)
        ev = enter_event ()
        ev.thisown = C
        ev.submap = 4
        ev.x = 0
        ev.y = 7
        ev.set_script ("teleport", (6, 5, 7, STAND_WEST))
        lm.add_event (ev)

        # From alek's to cellar
        ev = enter_event ()
        ev.thisown = C
        ev.submap = 6
        ev.x = 6
        ev.y = 6
        ev.set_script ("teleport", (4, 1, 6, STAND_EAST))
        lm.add_event (ev)
        ev = enter_event ()
        ev.thisown = C
        ev.submap = 6
        ev.x = 6
        ev.y = 7
        ev.set_script ("teleport", (4, 1, 7, STAND_EAST))
        lm.add_event (ev)

        # From cellar to storage
        ev = enter_event ()
        ev.thisown = C
        ev.submap = 4
        ev.x = 0
        ev.y = 9
        ev.set_script ("teleport", (8, 6, 3, STAND_WEST))
        lm.add_event (ev)
        ev = enter_event ()
        ev.thisown = C
        ev.submap = 4
        ev.x = 0
        ev.y = 10
        ev.set_script ("teleport", (8, 6, 4, STAND_WEST))
        lm.add_event (ev)

        # From storage to cellar
        ev = enter_event ()
        ev.thisown = C
        ev.submap = 8
        ev.x = 7
        ev.y = 3
        ev.set_script ("teleport", (4, 1, 9, STAND_EAST))
        lm.add_event (ev)
        ev = enter_event ()
        ev.thisown = C
        ev.submap = 8
        ev.x = 7
        ev.y = 4
        ev.set_script ("teleport", (4, 1, 10, STAND_EAST))
        lm.add_event (ev)

        # From cellar to dwarves'
        ev = enter_event ()
        ev.thisown = C
        ev.submap = 4
        ev.x = 10
        ev.y = 6
        ev.set_script ("cellar_to_bjarn", (7, 1, 6, STAND_EAST))
        lm.add_event (ev)
        ev = enter_event ()
        ev.thisown = C
        ev.submap = 4
        ev.x = 10
        ev.y = 7
        ev.set_script ("cellar_to_bjarn", (7, 1, 7, STAND_EAST))
        lm.add_event (ev)

        # From dwarves' to cellar
        ev = enter_event ()
        ev.thisown = C
        ev.submap = 7
        ev.x = 0
        ev.y = 6
        ev.set_script ("teleport", (4, 9, 6, STAND_WEST))
        lm.add_event (ev)
        ev = enter_event ()
        ev.thisown = C
        ev.submap = 7
        ev.x = 0
        ev.y = 7
        ev.set_script ("teleport", (4, 9, 7, STAND_WEST))
        lm.add_event (ev)

        # From 1st to Fellnir's
        ev = enter_event ()
        ev.thisown = C
        ev.submap = 9
        ev.x = 9
        ev.y = 2
        ev.set_script ("teleport", (10, 1, 3, STAND_EAST))
        lm.add_event (ev)

        # From Fellnir's to 1st
        ev = enter_event ()
        ev.thisown = C
        ev.submap = 10
        ev.x = 0
        ev.y = 3
        ev.set_script ("teleport", (9, 8, 2, STAND_WEST))
        lm.add_event (ev)

        # From 1st to Frostbloom's
        ev = enter_event ()
        ev.thisown = C
        ev.submap = 9
        ev.x = 0
        ev.y = 2
        ev.set_script ("teleport", (11, 4, 3, STAND_WEST))
        lm.add_event (ev)

        # From Frostbloom's to 1st
        ev = enter_event ()
        ev.thisown = C
        ev.submap = 11
        ev.x = 5
        ev.y = 3
        ev.set_script ("teleport", (9, 1, 2, STAND_EAST))
        lm.add_event (ev)

        # From 1st to Player's
        ev = enter_event ()
        ev.thisown = C
        ev.submap = 9
        ev.x = 7
        ev.y = 4
        ev.set_script ("teleport", (12, 5, 2, STAND_SOUTH))
        lm.add_event (ev)

        # From Player's to 1st
        ev = enter_event ()
        ev.thisown = C
        ev.submap = 12
        ev.x = 5
        ev.y = 1
        ev.set_script ("teleport", (9, 7, 3, STAND_NORTH))
        lm.add_event (ev)

        # From 1st to Silverhair's
        ev = enter_event ()
        ev.thisown = C
        ev.submap = 9
        ev.x = 1
        ev.y = 7
        ev.set_script ("fst_to_silverhair", (13, 5, 2, STAND_SOUTH))
        lm.add_event (ev)

        # From Silverhair's to 1st
        ev = enter_event ()
        ev.thisown = C
        ev.submap = 13
        ev.x = 5
        ev.y = 1
        ev.set_script ("teleport", (9, 1, 6, STAND_NORTH))
        lm.add_event (ev)

        # From 2nd to Redwyne's
        ev = enter_event ()
        ev.thisown = C
        ev.submap = 14
        ev.x = 3
        ev.y = 5
        ev.set_script ("teleport", (15, 1, 5, STAND_EAST))
        lm.add_event (ev)

        # From Redwyne's to 2nd
        ev = enter_event ()
        ev.thisown = C
        ev.submap = 15
        ev.x = 0
        ev.y = 5
        ev.set_script ("teleport", (14, 2, 5, STAND_WEST))
        lm.add_event (ev)

        # From 2nd to Oliver's
        ev = enter_event ()
        ev.thisown = C
        ev.submap = 14
        ev.x = 0
        ev.y = 5
        ev.set_script ("teleport", (16, 6, 5, STAND_WEST))
        lm.add_event (ev)

        # From Oliver's to 2nd
        ev = enter_event ()
        ev.thisown = C
        ev.submap = 16
        ev.x = 7
        ev.y = 5
        ev.set_script ("teleport", (14, 1, 5, STAND_EAST))
        lm.add_event (ev)

        # From 2nd to Illig's
        ev = enter_event ()
        ev.thisown = C
        ev.submap = 14
        ev.x = 1
        ev.y = 8
        ev.set_script ("teleport", (17, 6, 2, STAND_SOUTH))
        lm.add_event (ev)

        # From Illig's to 2nd
        ev = enter_event ()
        ev.thisown = C
        ev.submap = 17
        ev.x = 6
        ev.y = 1
        ev.set_script ("teleport", (14, 1, 7, STAND_NORTH))
        lm.add_event (ev)

        # From common room to 1st
        ev = enter_event ()
        ev.thisown = C
        ev.submap = 1
        ev.x = 12
        ev.y = 1
        ev.set_script ("teleport", (9, 8, 2, STAND_SOUTH))
        lm.add_event (ev)

        # From 1st to common room
        ev = enter_event ()
        ev.thisown = C
        ev.submap = 9
        ev.x = 8
        ev.y = 1
        ev.set_script ("teleport", (1, 12, 2, STAND_SOUTH))
        lm.add_event (ev)

        # From 1st to 2nd
        ev = enter_event ()
        ev.thisown = C
        ev.submap = 9
        ev.x = 6
        ev.y = 1
        ev.set_script ("teleport", (14, 4, 2, STAND_SOUTH))
        lm.add_event (ev)

        # From 2nd to 1st
        ev = enter_event ()
        ev.thisown = C
        ev.submap = 14
        ev.x = 4
        ev.y = 1
        ev.set_script ("teleport", (9, 6, 2, STAND_SOUTH))
        lm.add_event (ev)

        # From common room to cellar
        ev = enter_event ()
        ev.thisown = C
        ev.submap = 1
        ev.x = 9
        ev.y = 1
        ev.set_script ("teleport", (4, 6, 2, STAND_SOUTH))
        lm.add_event (ev)

        # From cellar to common room
        ev = enter_event ()
        ev.thisown = C
        ev.submap = 4
        ev.x = 6
        ev.y = 1
        ev.set_script ("teleport", (1, 9, 2, STAND_SOUTH))
        lm.add_event (ev)

        # From cellar to barn
        ev = enter_event ()
        ev.thisown = C
        ev.submap = 4
        ev.x = 12
        ev.y = 1
        ev.set_script ("teleport", (0, 24, 11, STAND_SOUTH))
        lm.add_event (ev)

        # From barn to cellar
        ev = enter_event ()
        ev.thisown = C
        ev.submap = 0
        ev.x = 24
        ev.y = 10
        ev.set_script ("teleport", (4, 12, 2, STAND_SOUTH))
        lm.add_event (ev)

        # From cellar to kitchen
        ev = enter_event ()
        ev.thisown = C
        ev.submap = 4
        ev.x = 3
        ev.y = 13
        ev.set_script ("teleport", (3, 6, 5, STAND_NORTH))
        lm.add_event (ev)

        # From kitchen to cellar
        ev = enter_event ()
        ev.thisown = C
        ev.submap = 3
        ev.x = 6
        ev.y = 6
        ev.set_script ("teleport", (4, 3, 12, STAND_NORTH))
        lm.add_event (ev)

        # From yard to guards'
        ev = enter_event ()
        ev.thisown = C
        ev.submap = 0
        ev.x = 12
        ev.y = 23
        ev.set_script ("teleport", (18, 7, 3, STAND_WEST))
        lm.add_event (ev)

        # From guards' to yard
        ev = enter_event ()
        ev.thisown = C
        ev.submap = 18
        ev.x = 8
        ev.y = 3
        ev.set_script ("teleport", (0, 13, 23, STAND_EAST))
        lm.add_event (ev)

        # From guards ground to guards 1st
        ev = enter_event ()
        ev.thisown = C
        ev.submap = 18
        ev.x = 1
        ev.y = 8
        ev.set_script ("teleport", (19, 2, 8, STAND_EAST))
        lm.add_event (ev)

        # From guards 1st to guards ground
        ev = enter_event ()
        ev.thisown = C
        ev.submap = 19
        ev.x = 1
        ev.y = 8
        ev.set_script ("teleport", (18, 2, 8, STAND_EAST))
        lm.add_event (ev)


        # Action events
        ev = action_event ()
        ev.thisown = C
        ev.submap = 1
        ev.x = 10
        ev.y = 2
        ev.dir = STAND_NORTH
        ev.set_script ("character_speak", (the_player.get_name (), \
                                           "That clock seems to be late!"))
        lm.add_event (ev)

        ev = action_event ()
        ev.thisown = C
        ev.submap = 10
        ev.x = 3
        ev.y = 6
        ev.dir = STAND_NORTH
        ev.set_script ("character_speak", (the_player.get_name (), \
                                           "I'd better not touch this... What if it explodes??"))
        lm.add_event (ev)

        ev = action_event ()
        ev.thisown = C
        ev.submap = 10
        ev.x = 4
        ev.y = 6
        ev.dir = STAND_NORTH
        ev.set_script ("character_speak", (the_player.get_name (), \
                                           "I'd better not touch this... What if it explodes??"))
        lm.add_event (ev)

        ev = action_event ()
        ev.thisown = C
        ev.submap = 10
        ev.x = 2
        ev.y = 5
        ev.dir = STAND_EAST
        ev.set_script ("character_speak", (the_player.get_name (), \
                                           "I'd better not touch this... What if it explodes??"))
        lm.add_event (ev)

        ev = action_event ()
        ev.thisown = C
        ev.submap = 10
        ev.x = 5
        ev.y = 5
        ev.dir = STAND_WEST
        ev.set_script ("character_speak", (the_player.get_name (), \
                                           "I'd better not touch this... What if it explodes??"))
        lm.add_event (ev)

        ev = action_event ()
        ev.thisown = C
        ev.submap = 10
        ev.x = 3
        ev.y = 4
        ev.dir = STAND_SOUTH
        ev.set_script ("character_speak", (the_player.get_name (), \
                                           "I'd better not touch this... What if it explodes??"))
        lm.add_event (ev)

        ev = action_event ()
        ev.thisown = C
        ev.submap = 10
        ev.x = 4
        ev.y = 4
        ev.dir = STAND_SOUTH
        ev.set_script ("character_speak", (the_player.get_name (), \
                                           "I'd better not touch this... What if it explodes??"))
        lm.add_event (ev)

        ev = action_event ()
        ev.thisown = C
        ev.submap = 0
        ev.x = 6
        ev.y = 17
        ev.dir = STAND_WEST
        ev.set_script ("character_speak", (the_player.get_name (), \
                                           "Closed. We are all emprisonned here..."))
        lm.add_event (ev)

        ev = action_event ()
        ev.thisown = C
        ev.submap = 0
        ev.x = 6
        ev.y = 18
        ev.dir = STAND_WEST
        ev.set_script ("character_speak", (the_player.get_name (), \
                                           "Closed. We are all emprisonned here..."))
        lm.add_event (ev)

        ev = action_event ()
        ev.thisown = C
        ev.submap = 0
        ev.x = 6
        ev.y = 19
        ev.dir = STAND_WEST
        ev.set_script ("character_speak", (the_player.get_name (), \
                                           "Closed. We are all emprisonned here..."))
        lm.add_event (ev)

        ev = action_event ()
        ev.thisown = C
        ev.submap = 17
        ev.x = 1
        ev.y = 6
        ev.dir = STAND_NORTH
        ev.set_script ("character_speak", (the_player.get_name (), \
                                           "It's locked."))
        lm.add_event (ev)

        ev = action_event ()
        ev.thisown = C
        ev.submap = 19
        ev.x = 2
        ev.y = 5
        ev.dir = STAND_NORTH
        ev.set_script ("character_speak", (the_player.get_name (), \
                                           "It's locked."))
        lm.add_event (ev)

        ev = action_event ()
        ev.thisown = C
        ev.submap = 19
        ev.x = 6
        ev.y = 4
        ev.dir = STAND_NORTH
        ev.set_script ("character_speak", (the_player.get_name (), \
                                           "It's locked."))
        lm.add_event (ev)

        ev = action_event ()
        ev.thisown = C
        ev.submap = 19
        ev.x = 6
        ev.y = 8
        ev.dir = STAND_NORTH
        ev.set_script ("character_speak", (the_player.get_name (), \
                                           "It's locked."))
        lm.add_event (ev)

        ev = action_event ()
        ev.thisown = C
        ev.submap = 6
        ev.x = 1
        ev.y = 4
        ev.dir = STAND_NORTH
        ev.set_script ("character_speak", (the_player.get_name (), \
                                           "It's locked."))
        lm.add_event (ev)

        ev = action_event ()
        ev.thisown = C
        ev.submap = 7
        ev.x = 7
        ev.y = 3
        ev.dir = STAND_NORTH
        ev.set_script ("character_speak", (the_player.get_name (), \
                                           "I doubt Master Fingolson would be happy if I go through his things..."))
        lm.add_event (ev)

        ev = action_event ()
        ev.thisown = C
        ev.submap = 13
        ev.x = 1
        ev.y = 6
        ev.dir = STAND_NORTH
        ev.set_script ("character_speak", (the_player.get_name (), \
                                           "Well, I can't dig into my mistress' shelf!"))
        lm.add_event (ev)


        # Now setup the characters
        player = gamedata_player ()
        player.jump_to (0, 4, 18)
        player.stand_east ()
        player.set_schedule ("intro")

        lucia = gamedata_get_character ("Lucia Redwyne")
        lucia.set_dialogue ("dialogues/lucia_start")
        lucia.load ("lucia.mchar")
        lucia.set_map (gamedata_map_engine ().get_landmap ())
        lucia.jump_to (3, 4, 3)
        lucia.set_action ("talk")
        lucia.set_schedule ("lucia")
        lucia.stand_south ()
        lucia.set_portrait ("lucia.pnm")

        orloth = gamedata_get_character ("Orloth Redwyne")
        orloth.set_dialogue ("dialogues/orloth_start")
        orloth.load ("orloth.mchar")
        orloth.set_map (gamedata_map_engine ().get_landmap ())
        orloth.jump_to (1, 2, 2)
        orloth.set_action ("talk")
        orloth.stand_south ()
        orloth.set_schedule ("orloth")
        orloth.set_portrait ("orloth.pnm")

        erek = gamedata_get_character ("Erek Stonebreaker")
        erek.set_dialogue ("dialogues/erek_start")
        erek.load ("erek.mchar")
        erek.set_map (gamedata_map_engine ().get_landmap ())
        erek.jump_to (1, 5, 5)
        erek.set_action ("talk")
        erek.stand_north ()
        # changed Erek's text color to violet
        erek.set_color (3)
        erek.set_schedule ("erek")
        erek.set_portrait ("erek.pnm")

        talan = gamedata_get_character ("Talan Wendth")
        talan.set_dialogue ("dialogues/demo_intro_1")
        talan.load ("talan.mchar")
        talan.set_map (gamedata_map_engine ().get_landmap ())
        talan.jump_to (0, 7, 17)
        talan.set_action ("talk")
        talan.stand_west ()
        talan.set_schedule ("talan")
        talan.set_portrait ("talan.pnm")

        jelom = gamedata_get_character ("Jelom Rasgar")
        jelom.set_dialogue ("dialogues/jelom_start")
        jelom.load ("jelom.mchar")
        jelom.set_map (gamedata_map_engine ().get_landmap ())
        jelom.jump_to (9, 2, 6)
        jelom.set_action ("talk")
        jelom.stand_north ()
        jelom.set_schedule ("jelom")
        jelom.set_portrait ("jelom.pnm")

        alek = gamedata_get_character ("Alek Endhelm")
        alek.set_dialogue ("dialogues/alek_start")
        alek.load ("alek.mchar")
        alek.set_map (gamedata_map_engine ().get_landmap ())
        alek.jump_to (1, 1, 3)
        alek.set_action ("talk")
        alek.stand_south ()
        alek.set_schedule ("alek")
        alek.set_portrait ("alek.pnm")

        oliver = gamedata_get_character ("Oliver Redwyne")
        oliver.set_dialogue ("dialogues/oliver_start")
        oliver.load ("oliver.mchar")
        oliver.set_map (gamedata_map_engine ().get_landmap ())
        oliver.jump_to (0, 25, 15)
        oliver.set_action ("talk")
        oliver.stand_west ()
        oliver.set_schedule ("oliver")
        oliver.set_portrait ("oliver.pnm")

        frostbloom = gamedata_get_character ("Rhayne Frostbloom")
        frostbloom.set_dialogue ("dialogues/frostbloom_start")
        frostbloom.load ("frostbloom.mchar")
        frostbloom.set_map (gamedata_map_engine ().get_landmap ())
        frostbloom.jump_to (0, 18, 22)
        frostbloom.set_action ("talk")
        frostbloom.stand_north ()
        frostbloom.set_schedule ("frostbloom")
        frostbloom.set_portrait ("frostbloom.pnm")

        bjarn = gamedata_get_character ("Bjarn Fingolson")
        bjarn.set_dialogue ("dialogues/bjarn_start")
        bjarn.load ("bjarn.mchar")
        bjarn.set_map (gamedata_map_engine ().get_landmap ())
        bjarn.jump_to (7, 3, 6)
        bjarn.set_action ("talk")
        bjarn.stand_west ()
        bjarn.set_schedule ("bjarn")
        bjarn.set_portrait ("bjarn.pnm")

        silverhair = gamedata_get_character ("Imoen Silverhair")
        silverhair.load ("silverhair.mchar")
        silverhair.set_map (gamedata_map_engine ().get_landmap ())
        silverhair.jump_to (13, 4, 4)
        silverhair.set_action ("talk")
        silverhair.stand_south ()
        silverhair.set_schedule ("silverhair")
        silverhair.set_portrait ("silverhair.pnm")

        sarin = gamedata_get_character ("Sarin Trailfollower")
        sarin.set_dialogue ("dialogues/sarin_start")
        sarin.load ("servant2.mchar")
        sarin.set_map (gamedata_map_engine ().get_landmap ())
        sarin.jump_to (13, 5, 3)
        sarin.set_action ("talk")
        sarin.stand_west ()
        sarin.set_schedule ("sarin")
        sarin.set_portrait ("sarin.pnm")

        janesta = gamedata_get_character ("Janesta Skywind")
        janesta.set_dialogue ("dialogues/janesta_start")
        janesta.load ("servant1.mchar")
        janesta.set_map (gamedata_map_engine ().get_landmap ())
        janesta.jump_to (13, 6, 3)
        janesta.set_action ("talk")
        janesta.stand_north ()
        janesta.set_schedule ("janesta")
        janesta.set_portrait ("janesta.pnm")

        fellnir = gamedata_get_character ("Fellnir Kezular")
        fellnir.set_dialogue ("dialogues/fellnir_start")
        fellnir.load ("fellnir.mchar")
        fellnir.set_map (gamedata_map_engine ().get_landmap ())
        fellnir.jump_to (10, 4, 4)
        fellnir.set_action ("talk")
        fellnir.stand_south ()
        fellnir.set_schedule ("fellnir")
        fellnir.set_portrait ("fellnir.pnm")

        tristan = gamedata_get_character ("Tristan Illig")
        tristan.set_dialogue ("dialogues/tristan_start")
        tristan.load ("illig.mchar")
        tristan.set_map (gamedata_map_engine ().get_landmap ())
        tristan.jump_to (1, 4, 6)
        tristan.set_action ("talk")
        tristan.stand_west ()
        tristan.set_schedule ("tristan")
        tristan.set_portrait ("illig.pnm")

        # Once we want to generate the data context files,
        # just call gamedata::save (1) and copy the .data files
        # to the game's root directory.

        audio_play_background (1)
        gametime_update ()
        fade_in ()

# -- Main --
title = title_screen ()
