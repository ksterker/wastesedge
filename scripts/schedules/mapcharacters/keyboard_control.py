#
#  $Id: keyboard_control.py,v 1.8 2002/01/19 18:08:48 adondev Exp $
#
#  (C) Copyright 2001 Alexandre Courbot
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

class keyboard_control:

    def __init__ (self, mapcharinstance):
        self.myself = mapcharinstance
        self.wnd = None
        
    def run (self):
        # -- allow smooth movement on the veranda
        if self.myself.get_val ("on_veranda") == 1 and self.wnd == None:
            self.enable_veranda_hack ()
        elif self.myself.get_val ("on_veranda") != 1 and self.wnd != None:
            self.disable_veranda_hack ()
        
        # -- react to the action key
        if adonthell.input_has_been_pushed (adonthell.SDLK_SPACE):
            # -- see whether a character(/object) is next to the player
            p = self.myself.whosnext ()

            # - Yes :)
            if p != None and p.currentmove () < adonthell.WALK_NORTH:
                # -- launch the other guy's (object's) action script
                p.launch_action (self.myself)

                # -- Cleanup
                p = None

            # -- otherwise launch an action event
            elif p == None:
                evt = adonthell.action_event ()
                evt.submap = self.myself.submap ()
                evt.x = self.myself.posx ()
                evt.y = self.myself.posy ()
                evt.dir = self.myself.currentmove ()
                evt.c = self.myself
                adonthell.event_handler_raise_event (evt)

        # -- move the player around
        elif adonthell.input_is_pushed (adonthell.SDLK_UP): self.myself.go_north ()
        elif adonthell.input_is_pushed (adonthell.SDLK_DOWN): self.myself.go_south ()
        elif adonthell.input_is_pushed (adonthell.SDLK_RIGHT): self.myself.go_east ()
        elif adonthell.input_is_pushed (adonthell.SDLK_LEFT): self.myself.go_west ()

    # -- BEGIN veranda hack
    def enable_veranda_hack (self):
        self.wnd = adonthell.win_container ()
        self.wnd.set_visible (0)
        self.wnd.thisown = 0
        self.wnd.py_signal_connect (self.on_draw, adonthell.win_event_DRAW, self.myself)
        adonthell.win_manager_get_active ().add (self.wnd)

    def disable_veranda_hack (self):
        adonthell.win_manager_get_active ().remove (self.wnd)
        del self.wnd
        self.wnd = None
    
    def on_draw (self, mychar):
        if mychar.submap () == 0 and mychar.posx () >= 17 and mychar.posx () <= 19 \
        and mychar.posy () == 12:
            view = adonthell.gamedata_engine ().get_mapview ()
            
            x = (mychar.posx () - view.posx () - mychar.base_x ()) * 20 \
                + mychar.offx () - view.offx () 
    
            y = (mychar.posy () - view.posy () - mychar.base_y ()) * 20 \
                + mychar.offy () - view.offy ()

            mychar.draw (x, y)
    # -- END veranda hack
