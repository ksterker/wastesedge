from adonthell import *

# The Game Menu
class main_menu (win_container):

    # Displays Waste's Edge's Main menu
    #   startup defines whether the options scroll into view (0) or simply appear (1)
    #   enable_s defines whether we have a "save" option (1) or not (0)
    #   enable_b turns background/border on (1) or off (0)
    def __init__ (self, startup, enable_s, enable_b = 0):	
        win_container.__init__(self)

        self.startup = startup

        # Init Position
        self.move (0,0)	
        self.resize(320,240)
        
        self.thisown = 0

        # load font and theme
        self.font = win_font (WIN_THEME_ORIGINAL)
        self.theme = win_theme (WIN_THEME_ORIGINAL)

        self.enable_save = enable_s
        
        self.lg = None
        
        self.quit = 1

        y_pos = 30
        if enable_s: y_pos = 15

        self.py_signal_connect (self.on_destroy, win_event_DESTROY)
        self.py_signal_connect (self.on_update, win_event_UPDATE)
        
        self.a_title = win_image()
        self.a_title.load_pnm ("gfx/cutscene/adonthell_green.pnm")
        self.a_title.set_mask (1)
        self.a_title.move ((self.length() - self.a_title.length())/2, y_pos)
        self.a_title.thisown = 0
        self.a_title.pack()
        y_pos = y_pos + 30

        self.title = win_label()
        self.title.set_font(self.font)
        self.title.set_form (label_AUTO_SIZE)
        self.title.set_text ("-- Waste's Edge --")
        self.title.move ((self.length()-self.title.length())/2, y_pos)
        self.title.thisown = 0
        self.title.pack()
        y_pos = y_pos + 40

        self.new_game = win_label()
        self.new_game.set_font(self.font)
       	self.new_game.set_form (label_AUTO_SIZE)
        if enable_s == 0: self.new_game.set_text ("New Game")
        else: self.new_game.set_text ("Continue")
        self.new_game.move (-self.new_game.length (), y_pos)
        self.new_game.pack()
        self.new_game.thisown = 0
        y_pos = y_pos + 30

        self.load_game = win_label ()
        self.load_game.set_font(self.font)
        self.load_game.set_form (label_AUTO_SIZE)
        self.load_game.set_text ("Load Game")
        self.load_game.move (self.length (), y_pos)
        self.load_game.pack()
        self.load_game.thisown = 0
        y_pos = y_pos + 30
	
        self.save_game = win_label ()
        self.save_game.set_font(self.font)
        self.save_game.set_form (label_AUTO_SIZE)
        self.save_game.set_text ("Save Game")
        self.save_game.move (-self.save_game.length (), y_pos)  
       	self.save_game.pack()
        self.save_game.thisown = 0
        if enable_s: y_pos = y_pos + 30
	
        self.options = win_label ()
        self.options.set_font (self.font)
        self.options.set_form (label_AUTO_SIZE)
        self.options.set_text ("Options")
        self.options.move (-self.options.length (), y_pos)
        self.options.pack()
        self.options.thisown = 0
        y_pos = y_pos + 30
	
        self.labquit = win_label ()
        self.labquit.set_font(self.font)
        self.labquit.set_form (label_AUTO_SIZE)
        self.labquit.set_text ("Quit")
        self.labquit.move (self.length (), y_pos)
        self.labquit.pack()
        self.labquit.thisown = 0
        y_pos = y_pos + 30

        self.labels = [self.new_game, self.load_game, self.options, self.labquit]
        if enable_s: self.labels.insert (2, self.save_game)
        else:
            self.save_game.thisown = Python
            del self.save_game
        
        for label in self.labels:
            self.add (label)    

	   	
        # activate self object
        self.set_activate (1)
        self.set_visible_all (1)	

        if startup == 0:
            done = 1
            sign = 1
            goals = ()
            moves = ()

            for label in self.labels:
                goals = goals + ((self.length () - label.length ())/2,)
                moves = moves + (3*sign,)
                sign = sign * -1

            gametime_start_action ()
            while done != 0:
                for k in range (gametime_frames_to_do()+1):
                    win_manager_update ()
                    self.update ()
                done = self.create_menu (moves, goals)
                win_manager_draw ()
                self.draw ()
                screen_show ()
                gametime_update()
            
        else:
            for label in self.labels:
                label.move ((self.length()-label.length())/2, label.y ())
            
        self.select = win_select()
        self.select.move(70,10)
        self.select.resize(180, 220)
	
        self.select.set_mode ( win_select_MODE_BRIGHTNESS )
        self.select.py_signal_connect (self.on_select, win_event_ACTIVATE_KEY);
        
        self.select.set_background(self.theme)
        self.select.set_visible_background (enable_b)
        self.select.set_trans_background (1)
        
        self.select.set_border(self.theme, win_border_MINI)
        self.select.set_visible_border (enable_b)
        
        self.select.set_circle (1)
        self.select.set_visible_all (1)
        self.select.thisown = 0
        
        self.select.set_activate (1)
        self.set_focus_object ( self.select )
        
        self.add (self.select)

        for label in self.labels:
            self.remove (label)
            label.move (label.x () - 70, label.y () - 10)
            self.select.add (label)
            
        # add the title
        self.set_align (win_base_ALIGN_CENTER)
        self.add (self.a_title)
        self.add (self.title)
        self.set_visible_all (1)

    # -- cleanup --
    def __del__(self):
        del self.font
        del self.theme
        
    # -- Callback to close the window
    def on_destroy (self):
        return self.quit

    # -- pressing ESC will close the menu if it's open
    def on_update (self):
        if self.lg == None:
            if input_has_been_pushed (SDLK_ESCAPE):
                self.quit = 0
                # If we're on the title screen, then leave.
                if self.startup == 0:
                    self.set_return_code (5)

    # -- Callback to get informed of the player's choice
    def on_select (self):
        sel = self.select.get_selected_position ()

        if self.enable_save == 0 and sel > 2:
            sel = sel + 1

        self.set_return_code (sel)
       
        # New Game
        if sel == 1:
            self.quit = 0

        # Load Game
        elif sel == 2:
            self.lg = data_screen (LOAD_SCREEN)
            self.lg.thisown = 0
            self.lg.set_activate (1)	
            if self.startup != 0:
                self.quit = 0
            else:
                self.lg.py_signal_connect (self.on_data_close, win_event_CLOSE)
            win_manager_add (self.lg)
            win_manager_set_focus (self.lg)

        # Save Game
        elif sel == 3:
            self.quit = 0
            self.lg = data_screen (SAVE_SCREEN)
            self.lg.thisown = 0
            self.lg.set_activate(1)
            win_manager_add (self.lg)
            win_manager_set_focus (self.lg)

        # Quit
        elif sel == 5:
            self.quit = 0

    def on_data_close (self, retval):
        self.lg = None
        if retval == 1:
            self.quit = 0

    # -- Scrolls the different menu options into view
    def create_menu (self, moves, goals):
        done = len (self.labels)

        for i in range (len (self.labels)):
            label = self.labels[i]
            step = moves[i]
            goal = goals[i]
            mod = 1
            j = 0

            if step < 0:
                step = -step
                mod = -1

            for j in range (step):
                if goal == label.x () + j*mod:
                    done = done - 1
                    break
            label.move (label.x () + j*mod, label.y ())

        return done
