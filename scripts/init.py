#
#  $Id: init.py,v 1.87 2002/02/05 15:09:21 adondev Exp $
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

class title_screen:
    def __init__ (self):
        # -- load our music
        audio_load_background (0, "audio/at-demo-1.ogg")
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

        audio_play_background (0)

        # -- launch the engine
        gametime_start_action ()
        gamedata_engine ().main (self.window, "title_sequence")


    def __del__ (self):
        print "Destructor called"
        gamedata_engine ().main_quit ()

    # -- catch ESC key
    def on_update (self):
        if self.draw_func != None:
            # -- Skip intro sequence
            if input_has_been_pushed (SDLK_ESCAPE):
                audio_fade_out_background (500)
                self.bag_t.set_visible (0)
                self.bag_c.set_visible (0)
                self.bag_o.set_visible (1)
                self.bag_o.set_alpha (255)
                self.draw_func = None
                self.show_menu (1, 0)

        # return self.retval
        return 1

    # -- callback for drawing operations
    def on_draw (self):
        if self.draw_func != None:
            self.draw_func ()

    # -- Fade in closed bag
    def initial_fade_in (self):
        if self.alpha == 255:
            # -- display "Adonthell v0.3"
            self.bag_t.set_visible (1)
            self.wait_time = 35
            self.draw_func = self.wait

        else:
            # -- fade in
            self.alpha = self.alpha + gametime_frames_to_skip() + 1
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
            self.alpha = self.alpha + gametime_frames_to_skip()
            if self.alpha > 255: self.alpha = 255
            self.bag_o.set_alpha (self.alpha)

    # -- Show the main menu
    def show_menu (self, a, b):
        menu = main_menu (a, b)
        
        # -- open the menu
        gamedata_engine ().main (menu, "game_menu")
        
        # -- once the menu is closed, see what we got
        retval = menu.get_result ()

        # -- start new game
        if retval == 1:
            # -- let the player chose a name for his character
            from character_screen import *
            cs = character_screen ()
            gamedata_engine ().main (cs, "character_screen")
                
            gamedata_engine ().fade_out ()
            self.cleanup ()

            # -- load the initial game
            gamedata_load (0)
            adonthell.gamedata_player ().set_name (cs.name)
            
            # -- on to the intro
            self.play_intro ()
            
        # -- Load game
        elif retval == 2:
            self.window.set_visible (0)
            self.cleanup ()
            gamedata_engine ().mapview_start ()
            gamedata_engine ().set_control_active (1)
            gamedata_engine ().fade_in ()

        # -- quit the game
        else:
            gamedata_engine ().main_quit ()

    # -- cleanup
    def cleanup (self):
        win_manager_get_active ().remove (self.window)

        self.window.remove (self.bag_o)
        self.window.remove (self.bag_c)
        self.window.remove (self.bag_t)

        del self.bag_o
        del self.bag_c
        del self.bag_t

        audio_fade_out_background (500)
        audio_unload_background (0)


    def play_intro (self):
        # -- Launches the intro
        import intro
        
        # -- start the mapengine
        gamedata_engine ().mapview_start ()
        gametime_update ()
        gamedata_engine ().fade_in ()

# -- Main --
title = title_screen ()
