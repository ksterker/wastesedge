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

# -- Let the player search Silverhair's chest

import adonthell

class search_chest:

    # Parameters:
    # name: name of the character that should speak when the event is triggered
    def __init__ (self, eventinstance, name):
        self.myself = eventinstance
        self.mapchar = adonthell.gamedata_get_character (name)

    def run (self, submap, x, y, dir, name):
        if adonthell.gamedata_get_quest ("demo").get_val ("get_item") == 1:
            fgs = find_gem_screen ()
            
            adonthell.gamedata_engine ().set_control_active (0)
            adonthell.gamedata_player ().set_schedule_active (0)
            adonthell.gamedata_engine ().main (fgs, "find_gem_screen")
            adonthell.gamedata_player ().set_schedule_active (1)
            adonthell.gamedata_engine ().set_control_active (1)
            
            adonthell.gamedata_get_quest ("demo").set_val ("get_item", 2)
            adonthell.gamedata_get_quest ("demo").set_val ("have_gem", 1)
        else:
            self.mapchar.speak ("I know this chest. The Lady uses it on her journeys.")


class find_gem_screen (adonthell.win_container):
    def __init__(self):
        adonthell.win_container.__init__(self)

        self.py_signal_connect (self.on_update, adonthell.win_event_UPDATE)
        self.state = 1

        # -- get font and theme
        self.font = adonthell.win_manager_get_font ("original")
        self.theme = adonthell.win_manager_get_theme ("original")
        
        self.move (58, 75)	
        self.resize (205, 70)
        self.set_border (self.theme, adonthell.win_border_MINI)
        self.set_background (self.theme)
        self.set_trans_background (1)

        # -- The window text
        self.text = adonthell.win_label ()
        self.text.thisown = 0
        self.text.resize (120, 0)
        self.text.set_font (self.font)
        self.text.set_form (adonthell.label_AUTO_HEIGHT)
        self.text.set_text ("Upon opening the chest, a small green something catches your attention ...")
        self.text.pack ()
        self.text.move (80, (self.height () - self.text.height ())/2)

        # -- The character image
        self.image = adonthell.win_image ()
        self.image.thisown = 0
        self.image.move (10, 3)
        self.image.resize (64, 64)
        self.image.load_pnm ("gfx/cutscene/gem.pnm")
        self.image.set_mask (1)
        self.image.pack ()
        
        self.add (self.text)
        self.add (self.image)
        
        self.set_visible_background (1)
        self.set_visible_border (1)
        self.set_visible_all (1)

    # -- catch relevant keypresses
    def on_update (self):
        # -- quit
        if adonthell.input_has_been_pushed (adonthell.SDLK_RETURN) or \
           adonthell.input_has_been_pushed (adonthell.SDLK_SPACE) or \
           adonthell.input_has_been_pushed (adonthell.SDLK_ESCAPE):
           
            # -- display second part of text
            if self.state == 1:
                self.text.set_text ("There, inmidst your mistress' luggage, lies one of Master Fingolson's gems.")
                self.text.pack ()
                self.text.move (80, (self.height () - self.text.height ())/2)
                self.state = 2
                
            # -- end
            else:
                adonthell.gamedata_engine ().main_quit ()
