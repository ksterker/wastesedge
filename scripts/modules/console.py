#
#  $Id: console.py,v 1.11 2002/08/20 17:42:28 ksterker Exp $
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

import sys
import adonthell

# -- A simple python console with command history
class console (adonthell.win_container):

    # -- Constructor
    def __init__(self, ns):	
        adonthell.win_container.__init__(self)

        self.namespace = ns
        self.history = []
        self.hist_idx = 0

        # read the old history
        self.read_history ()

        self.py_signal_connect (self.on_update, adonthell.win_event_UPDATE)
        
        # -- get font and theme
        self.font = adonthell.win_manager_get_font ("silverleaf")
        self.theme = adonthell.win_manager_get_theme ("silverleaf")
        
        self.move (10, 150)	
        self.resize (300, 80)
        self.set_border (self.theme)
        self.set_background (self.theme)
        self.set_trans_background (1)
        
        self.entry = adonthell.win_write ()
        self.entry.thisown = 0

        self.entry.py_signal_connect (self.on_execute, adonthell.win_event_ACTIVATE_KEY)
        self.entry.move (5, 5)
        self.entry.resize (290, 70)
        # -- causes a crash:
        # self.entry.set_form (label_AUTO_HEIGHT)
        self.entry.set_font (self.font)
        self.entry.set_cursor_visible (1)
        self.entry.set_cursor_moveable (1)
        self.entry.set_text ("")
        self.entry.pack ()
        
        self.add (self.entry)
        self.set_focus_object (self.entry)
        
        self.set_visible_background (1);
        self.set_visible_border (1);
        self.set_visible_all (1);
        self.set_activate (1)

        self.entry.set_focus (1)
        self.entry.set_activate (1)

    # -- callback for command execution
    def on_execute (self):
        text = self.entry.text_char ()

        # -- if we have a command ...
        if text != None:
            
            # -- ... add it to command history ...
            if self.hist_idx == 0 or text != self.history[-1]:
                self.history.append (text + '\n')
                self.hist_idx = len (self.history)
    
            # -- quit?
            if text == "quit":
                self.write_history ()
                adonthell.gamedata_engine ().main_quit ()
            
            # -- ... and try to execute it
            try:
                result = eval (text, self.namespace)
                self.entry.set_text (str (result))
            except:
                type, value = sys.exc_info()[:2]
                error = "Error:\n  " + str (type) + ":\n  \"" + str (value) + "\""
                self.entry.set_text (error)

    # -- catch relevant keypresses
    def on_update (self):
        # -- quit
        if adonthell.input_has_been_pushed (adonthell.SDLK_TAB):
            self.write_history ()
            adonthell.gamedata_engine ().main_quit ()

        # -- clear screen
        elif adonthell.input_has_been_pushed (adonthell.SDLK_DELETE):
            self.entry.set_text ("")
        
        # -- previous command
        elif adonthell.input_has_been_pushed (adonthell.SDLK_UP):
            if self.hist_idx > 0:
                self.hist_idx = self.hist_idx - 1
                self.entry.set_text (self.history[ self.hist_idx ][:-1])
        
        # -- next command
        elif adonthell.input_has_been_pushed (adonthell.SDLK_DOWN):
            if self.hist_idx < len (self.history) - 1:
                self.hist_idx = self.hist_idx + 1
                self.entry.set_text (self.history[ self.hist_idx ][:-1])

    # -- Read the old history from ~/.adonthell/history
    def read_history (self):
        dir = adonthell.gamedata_user_data_dir ()
        dir = dir + "/history"

        # -- try to open the file
        try:
            file = open (dir, 'r')
        except IOError:
            return

        if file != None:
            self.history = file.readlines ()
            self.hist_idx = len (self.history)
            file.close ()

    # -- Write the last 50 commands to ~/.adonthell/history
    def write_history (self):
        dir = adonthell.gamedata_user_data_dir ()
        dir = dir + "/history"

        # -- try to open the file
        file = open (dir, 'w')
        if file != None:
            file.writelines (self.history[-50:])
            file.close ()
