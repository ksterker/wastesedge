#
#  $Id: init.py,v 1.92 2002/09/02 10:59:50 ksterker Exp $
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

import adonthell
import main_menu
import time

class title_screen:
    def __init__ (self):
        # -- load our music
        adonthell.audio_load_background (0, "audio/at-demo-1.ogg")

        # -- The themes and fonts we'll use
        adonthell.win_manager_add_theme ("original")
        adonthell.win_manager_add_theme ("silverleaf")

        adonthell.win_manager_add_font ("yellow")
        adonthell.win_manager_add_font ("red")
        adonthell.win_manager_add_font ("violet")
        adonthell.win_manager_add_font ("blue")
        adonthell.win_manager_add_font ("green")
        adonthell.win_manager_add_font ("white")
        adonthell.win_manager_add_font ("original")
        adonthell.win_manager_add_font ("silverleaf")

        # -- load our images
        self.bag_o = adonthell.win_image ()
        self.bag_o.load_raw ("gfx/cutscene/jewelbag_open.img")
        self.bag_o.set_alpha (0)
        self.bag_o.move (0, 0)
        self.bag_o.pack ()
        self.bag_o.set_visible (0)

        self.bag_c = adonthell.win_image ()
        self.bag_c.load_raw ("gfx/cutscene/jewelbag_closed.img")
        self.bag_c.set_visible (1)
        self.bag_c.set_alpha (0)
        self.bag_c.move (0, 0)
        self.bag_c.pack ()

        self.bag_t = adonthell.win_image ()
        self.bag_t.load_raw ("gfx/cutscene/adonthell_03.img")
        self.bag_t.move (33, 86)
        self.bag_t.pack ()
        self.bag_t.set_visible (0)

        # -- create the window
        self.window = adonthell.win_container ()
        self.window.move (0, 0)
        self.window.resize (320, 240)
        self.window.set_visible_border (0)

        # -- the order here is essential
        self.window.add (self.bag_c)
        self.window.add (self.bag_t)
        self.window.add (self.bag_o)

        self.window.set_activate (1)
        self.window.set_visible (1)

        self.window.py_signal_connect (self.on_update, adonthell.win_event_UPDATE)
        self.window.py_signal_connect (self.on_draw, adonthell.win_event_DRAW)

        self.draw_func = self.initial_fade_in

        self.alpha = 0

        adonthell.audio_play_background (0)

        # -- launch the engine
        adonthell.gametime_start_action ()
        adonthell.gamedata_engine ().main (self.window, "title_sequence")


    def __del__ (self):
        print "Destructor called"
        adonthell.gamedata_engine ().main_quit ()

    # -- catch ESC key
    def on_update (self):
        if self.draw_func != None:
            # -- Skip intro sequence
            if adonthell.input_has_been_pushed (adonthell.SDLK_ESCAPE):
                adonthell.audio_fade_out_background (500)
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
            self.alpha = self.alpha + adonthell.gametime_frames_to_skip() + 1
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
            self.alpha = self.alpha + adonthell.gametime_frames_to_skip()
            if self.alpha > 255: self.alpha = 255
            self.bag_o.set_alpha (self.alpha)

    # -- Show the main menu
    def show_menu (self, a, b):
        menu = main_menu.main_menu (a, b)
        
        # -- open the menu
        adonthell.gamedata_engine ().main (menu, "game_menu")
        
        # -- once the menu is closed, see what we got
        retval = menu.get_result ()

        # -- start new game
        if retval == 1:
            # -- let the player chose a name for his character
            import character_screen
            cs = character_screen.character_screen ()
            adonthell.gamedata_engine ().main (cs, "character_screen")

            adonthell.gamedata_engine ().fade_out ()
            self.cleanup ()

            # -- load the initial game
            adonthell.gamedata_load (0)
            adonthell.gamedata_player ().set_name (cs.name)
            
            # -- on to the intro
            self.play_intro ()
            
        # -- Load game
        elif retval == 2:
            adonthell.gamedata_player ().set_schedule_active (1)

            self.window.set_visible (0)
            self.cleanup ()
            adonthell.gamedata_engine ().mapview_start ()
            adonthell.gamedata_engine ().set_control_active (1)
            adonthell.gamedata_engine ().fade_in ()

        # -- quit the game
        else:
            adonthell.gamedata_engine ().main_quit ()

    # -- cleanup
    def cleanup (self):
        adonthell.win_manager_get_active ().remove (self.window)

        self.window.remove (self.bag_o)
        self.window.remove (self.bag_c)
        self.window.remove (self.bag_t)

        del self.bag_o
        del self.bag_c
        del self.bag_t

        adonthell.audio_fade_out_background (500)
        adonthell.audio_unload_background (0)


    def play_intro (self):
        # -- Launches the intro

        import intro

        # -- start the mapengine
        adonthell.gamedata_engine ().mapview_start ()
        adonthell.gametime_update ()
        adonthell.gamedata_engine ().fade_in ()

# -- Main --
adonthell.audio_load_wave (0, "audio/select.wav")
adonthell.audio_load_wave (1, "audio/switch.wav")
adonthell.audio_load_wave (2, "audio/unselect.wav")

if adonthell.gamedata_load_newest () == 0:
    title = title_screen ()
else:
    # -- Quick-load
    adonthell.gamedata_player ().set_schedule_active (1)
    adonthell.gametime_start_action ()
    adonthell.gamedata_engine ().main ()
