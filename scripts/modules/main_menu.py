from adonthell import *

# The Game Menu
class main_menu (win_container):

    # Displays Waste's Edge's Main menu
    #   startup defines whether the options scroll into view (0) or simply appear (1)
    #   enable_s defines whether we have a "save" option (1) or not (0)
    #   enable_b turns background/border on (1) or off (0)
    def __init__ (self, startup, enable_s, enable_b = 0):
        win_container.__init__(self, 0, 0, 320, 240, None)

        self.thisown = 0
        
        self.font = win_font (WIN_THEME_ORIGINAL)
        self.theme = win_theme (WIN_THEME_ORIGINAL)
        self.enable_save = enable_s
        self.lg = None
        self.quit = 1
        
        y_pos = 30
        if enable_s: y_pos = 15

        # win_containerPtr.__init__ (self, )
        self.py_signal_connect (self.on_destroy, WIN_SIG_DESTROY)
        self.py_signal_connect (self.on_update, WIN_SIG_UPDATE)
        self.set_border_visible (0)

        self.title_img = image ()
        self.title_img.load_pnm ("gfx/cutscene/adonthell_green.pnm")
        self.title_img.set_mask (1)

        self.a_title = win_image (0, y_pos, self.title_img, self.theme)
        self.a_title.move ((self.length()-self.a_title.length())/2, self.a_title.y ())
        self.a_title.thisown = 0
        y_pos = y_pos + 30

        self.title = win_label (0, y_pos, 0, 0, self.theme, self.font)
        self.title.set_auto_size (1)
        self.title.set_text ("-- Waste's Edge --")
        self.title.move ((self.length()-self.title.length())/2, self.title.y ())
        self.title.thisown = 0
        y_pos = y_pos + 40

        self.new_game = win_label (0, y_pos, 0, 0, self.theme, self.font)
        self.new_game.set_auto_size (1)
        if enable_s == 0: self.new_game.set_text ("New Game")
        else: self.new_game.set_text ("Continue")
        self.new_game.move (-self.new_game.length (), self.new_game.y ())
        self.new_game.thisown = 0
        y_pos = y_pos + 30

        self.load_game = win_label (0, y_pos, 0, 0, self.theme, self.font)
        self.load_game.set_auto_size (1)
        self.load_game.set_text ("Load Game")
        self.load_game.move (self.length (), self.load_game.y ())
        self.load_game.thisown = 0
        y_pos = y_pos + 30

        self.save_game = win_label (0, y_pos, 0, 0, self.theme, self.font)
        self.save_game.set_auto_size (1)
        self.save_game.set_text ("Save Game")
        self.save_game.move (-self.save_game.length (), self.save_game.y ())  
        self.save_game.thisown = 0
        if enable_s: y_pos = y_pos + 30

        self.options = win_label (0, y_pos, 0, 0, self.theme, self.font)
        self.options.set_auto_size (1)
        self.options.set_text ("Options")
        self.options.move (-self.options.length (), self.options.y ())
        self.options.thisown = 0
        y_pos = y_pos + 30
    
        self.quit = win_label (0, y_pos, 0, 0, self.theme, self.font)
        self.quit.set_auto_size (1)
        self.quit.set_text ("Quit")
        self.quit.move (self.length (), self.quit.y ())
        self.quit.thisown = 0
        y_pos = y_pos + 30

        self.labels = [self.new_game, self.load_game, self.options, self.quit]
        if enable_s: self.labels.insert (2, self.save_game)
        else:
            self.save_game.thisown = Python
            del self.save_game
        
        for label in self.labels:
            self.add (label)    

        win_manager_add (self.this)

        if startup == 0:
            self.set_visible_all (1)
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

                done = self.create_menu (moves, goals)
                win_manager_draw ()
                screen_show ()
                gametime_update()
        else:
            for label in self.labels:
                label.move ((self.length()-label.length())/2, label.y ())
            
        self.select = win_select (70, 10, 180, 220, self.theme)
        self.select.set_select_mode (WIN_SELECT_MODE_BRIGHTNESS)
        self.select.py_signal_connect (self.on_select, WIN_SIG_ACTIVATE_KEY);
        self.select.set_background_visible (enable_b)
        self.select.set_border_size (WIN_SIZE_MINI)
        self.select.set_border_visible (enable_b)
        self.select.set_select_circle (1)
        self.select.set_can_be_selected_all (1)
        self.select.set_activated (1)
        self.select.set_visible_all (1)
        self.select.thisown = 0
        win_select_set_activate_keyboard (1)
        
        self.add (self.select)

        for label in self.labels:
            self.remove (label)
            label.move (label.x () - 70, label.y () - 10)
            self.select.add (label)
            
        # add the title
        self.set_align (WIN_ALIGN_CENTER)
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
        if input_has_been_pushed (SDLK_ESCAPE):
            if self.lg == None:
                self.set_return_code (6)
                self.quit = 0
                

    # -- Callback to get informed of the player's choice
    def on_select (self):
        sel = self.select.get_pos ()

        if self.enable_save == 0 and sel > 2:
            sel = sel + 1

        self.set_return_code (sel)
       
        # New Game
        if sel == 1:
            # data_load (0)
            self.quit = 0

        # Load Game
        elif sel == 2:
            self.lg = data_screen (LOAD_SCREEN)
            self.lg.py_signal_connect (self.on_load, WIN_SIG_CLOSE)
            self.lg.thisown = 0

            win_manager_add (self.lg)
            win_manager_set_focus (self.lg)

        # Save Game
        elif sel == 3:
            self.lg = data_screen (SAVE_SCREEN)
            self.lg.py_signal_connect (self.on_load, WIN_SIG_CLOSE)
            self.lg.thisown = 0

            win_manager_add (self.lg)
            win_manager_set_focus (self.lg)

        # Quit
        elif sel == 5:
            self.quit = 0


    # -- a game has been loaded
    def on_load (self, retval):
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
