from main_menu import *
import time

bag_o = image ()
bag_c = image ()
bag_t = image ()
bag_o.load_pnm ("gfx/cutscene/jewelbag_open.pnm")
bag_c.load_pnm ("gfx/cutscene/jewelbag_closed.pnm")
bag_t.load_pnm ("gfx/cutscene/adonthell_03.pnm")

bag_o.set_alpha (0)
bag_c.set_alpha (0)
bag_t.set_alpha (255)


# Fade in/out multiple pictures
# Returns current alpha of last picture
# Usage fade (pic1, ..., picN, step1, ..., stepN)
def fade (*args):
    pics = args[:len (args)/2]
    vals = args[len (args)/2:]
    alpha = 0
    for i in range (len (pics)):
        alpha = pics[i].alpha () + vals[i]
        if alpha < 0: alpha = 0
        if alpha > 255: alpha = 255
        pics[i].set_alpha (alpha)
        pics[i].draw (0,0)
    return alpha
 
alpha = 0

audio_load_background (0, "audio/at-menu-full.ogg")
audio_load_background (1, "audio/at-dummy-1.ogg")
audio_load_wave (0, "audio/select.wav")
audio_load_wave (1, "audio/switch.wav")
audio_load_wave (2, "audio/unselect.wav")

audio_play_background (0)
gametime_start_action ()

k=0

# Fade in closed bag
while alpha < 255:
    for k in range (gametime_frames_to_do()): pass
    screen_clear ()
    alpha = fade (bag_c, k+1)
    bag_c.draw(0,0)
    screen_show ()
    gametime_update()
    
bag_t.draw (33, 86)
screen_show ()
gametime_update ()

# wait ~2.5 seconds
for i in range (25):
    time.sleep (0.1)
    screen_show ()
    gametime_update()

alpha = 0

# fade in open bag
while alpha < 255:
    for k in range (gametime_frames_to_do()): pass
    screen_clear ()
    bag_c.draw (0, 0)
    bag_t.draw (33, 86)
    alpha = fade (bag_o, k+1)
    screen_show ()
    gametime_update ()
    
del bag_c
del bag_t

class title_screen:
    def __init__ (self, background):
        self.quit = 0
        self.image = win_image (0, 0, background, None)

        self.window = win_container (0, 0, 320, 240, None)
        self.window.set_border_visible (0)
        self.window.add (self.image)
        self.window.set_visible_all (1)

        win_manager_add (self.window)

        self.menu = main_menu (0, 0)
        self.menu.py_signal_connect (self.on_menu_close, WIN_SIG_CLOSE)

        win_manager_set_focus (self.menu)

    # on to the main menu
    def on_menu_close (self, retval):
        self.quit = retval


    def loop (self):
        while self.quit == 0:
            input_update ()

            for k in range (gametime_frames_to_do()+1):
                win_manager_update ()

            if input_has_been_pushed (SDLK_ESCAPE):
                self.quit = 5
                break
    
            win_manager_draw ()
            screen_show ()
            gametime_update()

        self.window.remove (self.image)
        win_manager_remove (self.window)
        alpha = 255
	bag_o.set_alpha(255)
        gametime_start_action()
        while alpha > 0:
          for k in range (gametime_frames_to_do()): pass
          screen_clear ()
          alpha = fade (bag_o, (-(k+1)*2))
          screen_show ()
          gametime_update()


# -- Main --
title = title_screen (bag_o)
title.loop ()
retval = title.quit
del bag_o

if retval < 5: 
    if retval == 1: gamedata_load(0)
    audio_play_background (1)
    map_engine.run()
