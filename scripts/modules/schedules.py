#
#  $Id: schedules.py,v 1.2 2001/08/08 17:00:47 adondev Exp $
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

# Helper functions for usage in schedules
from adonthell import *
import random

# -- A function that doesn't deserve the term 'pathfinding'
def simple_goto_xy (mychar, goal_x, goal_y):

    dist_x = mychar.posx () - goal_x
    dist_y = mychar.posy () - goal_y

    # -- reached the goal?
    if dist_x == 0 and dist_y == 0:
        # -- wait until we are truly there!
        if mychar.offx () == 0 and mychar.offy () == 0:
            return 1
        else:
            return 0

    dst = float (abs(dist_x)) / (abs (dist_x) + abs (dist_y))
    rnd = random.random ()

    # -- preferrably walk into the direction that is closest
    #    to the goal. But we allow a little variation.
    if rnd > dst:
        go_north_south (mychar, dist_x, dist_y, 1)
    else:
        go_east_west (mychar, dist_x, dist_y, 1)

    return 0


# -- try to walk in the direction that leads to the goal
def go_north_south (mychar, dist_x, dist_y, count):

    # -- All four directions blocked -> wait a turn
    if count >= 4: return

    # -- try to approach goal in y direction first,
    #    if blocked, try x direction, and if that's not
    #    possible then walk back
    if dist_y <= 0 and mychar.can_go_south ():
        mychar.go_south ()
    elif dist_y >= 0 and mychar.can_go_north ():
        mychar.go_north ()
    else:
        dist_y = -dist_y
        go_east_west (mychar, dist_x, dist_y, count+1)

# -- try to walk in the direction that leads to the goal
def go_east_west (mychar, dist_x, dist_y, count):

    # -- All four directions blocked -> wait a turn
    if count >= 4: return

    # -- try to approach goal in x direction first,
    #    if blocked, try y direction, and if that's not
    #    possible then walk back
    if dist_x >= 0 and mychar.can_go_west ():
        mychar.go_west ()
    elif dist_x <= 0 and mychar.can_go_east ():
        mychar.go_east ()
    else:
        dist_x = -dist_x
        go_north_south (mychar, dist_x, dist_y, count+1)


# -- display a "bubble" with some text above a character
def speak (mychar, text):
    # -- ... but only if he's on the player's submap
    if mychar.submap () == gamedata_player ().submap ():

        b = bubble (mychar, text)
        b.thisown = 0

        # -- add the bubble to the win_manager, but don't give it the focus
        win_manager_add (b)


# -- the "bubble"-window
class bubble (win_container):
    def __init__ (self, mychar, text):
        win_container.__init__(self)

        # -- the time the bubble will remain open
        self.remain = 75 + len (text) * 4

        self.py_signal_connect (self.on_destroy, win_event_DESTROY)
        self.py_signal_connect (self.on_update, win_event_UPDATE, mychar)

        # -- get the font that matches the NPC's text color
        if mychar.get_color () == 1: self.font = win_font ("yellow/")
        elif mychar.get_color () == 2: self.font = win_font ("red/")
        elif mychar.get_color () == 3: self.font = win_font ("violet/")
        elif mychar.get_color () == 4: self.font = win_font ("blue/")
        elif mychar.get_color () == 5: self.font = win_font ("green/")
        else: self.font = win_font( "white/")

        self.theme = win_theme (WIN_THEME_ORIGINAL)

        # -- if the submap is smaller than the mapview, we have to
        #    calculate the offset
        view = gamedata_map_engine ().get_mapview ()
        area = gamedata_map_engine ().get_landmap ().get_submap (mychar.submap ())
        if area.area_length () * MAPSQUARE_SIZE < view.length ():
            self.offx = (view.length () - area.area_length () * MAPSQUARE_SIZE) / 2
        else:
            self.offx = 0
        if area.area_height () * MAPSQUARE_SIZE < view.height ():
            self.offy = (view.height () - area.area_height () * MAPSQUARE_SIZE) / 2
        else:
            self.offy = 0

        # -- get the postion above the character's head
        x, y = self.get_window_pos (mychar)

        self.resize (120, 55)
        self.move (x, y)	

        self.bubble = win_label ()
        self.bubble.set_font (self.font)
        self.bubble.resize (110, 0)
        self.bubble.set_form (label_AUTO_HEIGHT)
        self.bubble.set_text (text)

        x = (self.length () - self.bubble.length ()) / 2
        y = self.height () - self.bubble.height () - 3

        self.bubble.move (x, y)
        self.bubble.thisown = 0
        self.bubble.pack()

        self.bubble.set_background (self.theme)
        self.bubble.set_visible_background (1)
        self.bubble.set_trans_background (1)

        self.bubble.set_border(self.theme, win_border_MINI)
        self.bubble.set_visible_border (1)

        self.add (self.bubble)
        self.set_visible_all (1)

    def __del__ (self):
        del self.theme
        del self.font

    # -- once this returns 0, the bubble will close
    def on_destroy (self):
        return self.remain

    # -- draws the bubble above the character's head
    def on_update (self, mychar):
        x, y = self.get_window_pos (mychar)
        self.move (x, y)
        self.remain = self.remain - 1

    # -- center the window above the characters head
    def get_window_pos (self, mychar):
        view = gamedata_map_engine ().get_mapview ()
        x = (mychar.posx () - view.posx () - mychar.base_x ()) * MAPSQUARE_SIZE
        x = x + mychar.offx () - view.offx () - 55 + self.offx
        y = (mychar.posy () - view.posy () - mychar.base_y ()) * MAPSQUARE_SIZE
        y = y + mychar.offy () - view.offy () - 40 + self.offy

        return (x, y)