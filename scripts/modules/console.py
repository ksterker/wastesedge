import sys
from adonthell import *

# -- A simple python console with command history
class console (win_container):

    # -- Constructor
    def __init__(self, ns):	
        win_container.__init__(self)

        self.namespace = ns
        self.history = []
        self.hist_idx = 0
        self.thisown = 0
        self.quit = 1

        # read the old history
        self.read_history ()

        self.py_signal_connect (self.on_destroy, win_event_DESTROY)
        self.py_signal_connect (self.on_update, win_event_UPDATE)
        
        # -- load font and theme
        self.font = win_font (WIN_THEME_ORIGINAL)
        self.theme = win_theme (WIN_THEME_ORIGINAL)
        
        self.move (10, 150)	
        self.resize (300, 80)
        self.set_border (self.theme)
        self.set_background (self.theme)
        self.set_trans_background (1)
        
        self.entry = win_write ()
        self.entry.thisown = 0
        self.entry.py_signal_connect (self.on_execute, win_event_ACTIVATE_KEY)
        self.entry.move (5, 5)
        self.entry.resize (290, 70)
        # -- causes a crash:
        # self.entry.set_form (label_AUTO_HEIGHT)
        self.entry.set_font (self.font)
        self.entry.set_cursor (1)
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

    # -- cleanup --
    def __del__(self):
        self.write_history ()

        del self.font
        del self.theme

    # -- callback for command execution
    def on_execute (self):
        text = self.entry.text_char ()
        # print "Execute", text
 
        # -- if we have a command ...
        if text != None:
            
            # -- ... add it to command history ...
            if self.hist_idx == 0 or text != self.history[-1]:
                self.history.append (text + '\n')
                self.hist_idx = len (self.history)
    
            # -- ... and try to execute it
            try:
                result = eval (text, self.namespace)
                self.entry.set_text (str (result))
            except:
                type, value = sys.exc_info()[:2]
                error = "Error:\n  " + str (type) + ":\n  \"" + str (value) + "\""
                self.entry.set_text (error)

    # -- callback to close the window
    def on_destroy (self):
        return self.quit

    # -- catch relevant keypresses 
    def on_update (self):
        
        # -- quit
        if input_has_been_pushed (SDLK_ESCAPE):
            # print "Quitting ..."
            self.quit = 0

        # -- clear screen
        elif input_has_been_pushed (SDLK_DELETE):
            # print "Deleting ..."
            self.entry.set_text ("")
        
        # -- previous command
        elif input_has_been_pushed (SDLK_UP):
            # print "Up ..."
            if self.hist_idx > 0:
                self.hist_idx = self.hist_idx - 1
                self.entry.set_text (self.history[ self.hist_idx ][:-1])
        
        # -- next command
        elif input_has_been_pushed (SDLK_DOWN):
            # print "Down ..."
            if self.hist_idx < len (self.history) - 1:
                self.hist_idx = self.hist_idx + 1
                self.entry.set_text (self.history[ self.hist_idx ][:-1])

    # -- Read the old history from ~/.adonthell/history
    def read_history (self):
        dir = gamedata_user_data_dir ()
        dir = dir + "/history"

        # -- try to open the file
        file = open (dir, 'r')
        if file != None:
            self.history = file.readlines ()
            self.hist_idx = len (self.history)
            file.close ()

    # -- Write the last 50 commands to ~/.adonthell/history
    def write_history (self):
        dir = gamedata_user_data_dir ()
        dir = dir + "/history"

        # -- try to open the file
        file = open (dir, 'w')
        if file != None:
            file.writelines (self.history[-50:])
            file.close ()
