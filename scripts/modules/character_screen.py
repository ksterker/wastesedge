#
#  $Id: character_screen.py,v 1.4 2001/12/27 00:40:49 adondev Exp $
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

# -- GUI for chosing the name of the main character
class character_screen (adonthell.win_container):

    # -- Constructor
    def __init__(self):	
        adonthell.win_container.__init__(self)

        # -- get font and theme
        self.font = adonthell.win_manager_get_font ("original")
        self.theme = adonthell.win_manager_get_theme ("original")
        
        self.move (60, 55)	
        self.resize (200, 110)
        self.set_border (self.theme)
        self.set_background (self.theme)
        self.set_trans_background (1)

        # -- The window title
        self.title = adonthell.win_label ()
        self.title.thisown = 0
        self.title.resize (0, 20)
        self.title.set_font (self.font)
        self.title.set_form (adonthell.label_AUTO_SIZE)
        self.title.set_text ("Enter your character's name")
        self.title.pack ()
        self.title.move ((self.length () - self.title.length ())/2, 10)

        # -- The character image
        self.image = adonthell.win_image ()
        self.image.thisown = 0
        self.image.move (10, 35)
        self.image.resize (64, 64)
        self.image.load_pnm ("gfx/portraits/player.pnm")
        self.image.set_mask (1)
        self.image.pack ()

        # -- The text entry
        self.entry = adonthell.win_write ()
        self.entry.thisown = 0
        self.entry.py_signal_connect (self.on_enter, adonthell.win_event_ACTIVATE_KEY)
        self.entry.move (90, 62)
        self.entry.resize (100, 20)
        self.entry.set_font (self.font)
        self.entry.set_cursor_visible (1)
        self.entry.set_cursor_moveable (1)
        self.entry.set_text ("Banec")
        self.entry.pack ()
        
        self.add (self.title)
        self.add (self.image)
        self.add (self.entry)
        self.set_focus_object (self.entry)
        
        self.set_visible_background (1)
        self.set_visible_border (1)
        self.set_visible_all (1)
        self.set_activate (1)

        self.entry.set_focus (1)
        self.entry.set_activate (1)

    # -- callback for accepting name
    def on_enter (self):
        self.name = self.entry.text_char ()
        adonthell.gamedata_engine ().main_quit ()
