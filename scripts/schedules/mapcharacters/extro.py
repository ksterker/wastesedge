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

# -- the game's extro

import adonthell

class extro:
    def __init__(self, mapchar):
        # -- grab the character's we need
        bjarn = adonthell.gamedata_get_character ("Bjarn Fingolson")
        erek = adonthell.gamedata_get_character ("Erek Stonebreaker")
        jelom = adonthell.gamedata_get_character ("Jelom Rasgar")
        talan = adonthell.gamedata_get_character ("Talan Wendth")
        talan.set_schedule_active (0)
        silverhair = adonthell.gamedata_get_character ("Imoen Silverhair")
        player = adonthell.gamedata_player ()
        
        # -- init the bubble texts
        #    (character, wait until spoken?, text)
        self.text = [(bjarn, 1, "There is no denying it. Yes, I feigned the theft."), \
            (jelom, 1, "But why? And where are the gems then?"), \
            (bjarn, 1, "Why? Haven't I made myself clear already?"), \
            (bjarn, 1, "I despise those Elves and their uncanny ways."), \
            (bjarn, 1, "Their ... meddling with reality contradicts all principles I learned to hold true."), \
            (bjarn, 1, "And yet, I had to provide them with the reagents they need to perform their dark art."), \
            (bjarn, 1, "I felt so ... ashamed!"), \
            (player, 1, "And you believe that justifies the discomfort you caused my mistress?"), \
            (bjarn, 1, "You cannot think further than your mistress, can you?"), \
            (bjarn, 1, "Theft by a high born like Lady Silverhair would have been considered a grave insult by the clan elders."), \
            (bjarn, 1, "Had she been convicted, they might have chosen to cease trading with her people. And that probably for many years!"), \
            (silverhair, 1, "I feared as much and I feared the consequences."), \
            (silverhair, 1, "Without the arcane arts my kind would soon succumb to the human tides."), \
            (silverhair, 1, "But without gems and ores purchased from the small folk we cannot create magic."), \
            (jelom, 1, "Who would have thought that?"), \
            (jelom, 1, "Seems you owe " + player.get_name() + " here a big favour, if I may say so, Lady."), \
            (silverhair, 1, "Rest assured that " + player.get_name() + "'s deeds will not be forgotten, good man."), \
            (jelom, 1, "Well, this is settled then. What remains now are the whereabouts of the gems."), \
            (jelom, 1, "Master Fingolson!"), \
            (None, 1, "They were here all the time, safe from thieving hands, ..."), \
            (None, 1, "... well hidden in a niche I carved during my previous visits."), \
            (None, 1, "Here."), \
            (None, 1, "But ..."), \
            (None, 1, "... they are gone!"), \
            (talan, 1, "Sir, sir! To the gate! Quick! The thief is loose!"), \
            (bjarn, 0, "My jewels, oh my jewels!"), \
            (player, 1, "By Andomiel's Tree! What happened to you, Talan?!"), \
            (talan, 1, "It was the mercenary, sir! He sneaked upon me and hit me over the head."), \
            (silverhair, 0, "O sweet irony."), \
            (jelom, 1, "Then the gems have been stolen after all?!"), \
            (jelom, 1, "By that scum, Alek!? Now that's funny."), \
            (bjarn, 1, "How can you say that? And why are you still here?"), \
            (bjarn, 1, "Will nobody go after my gems!?"), \
            (jelom, 1, "What for?"), \
            (jelom, 1, "Where you are going you won't need them any more. Besides, Alek is probably long gone by now ...")]

        # -- the typeover text
        self.typeover = ["And so Alek Endhelm escaped into the\nNorth, where he spent his newly gained\nwealth for Ale and other pleasures.", \
            "Bjarn Fingolson however, bereft of all\nhonour, was taken to Uzdun'kal and\nsentenced to the lowest labour.\nNowadays his fate serves as an example\nand a warning to generations of young Dwarves.", \
            "Lady Imoen Silverhair received the finest\nChrysoberyl Catseyes as a token of\nregret, and the magic rings and amulets\nshe crafted were of wondrous might and\nbeauty, desired and admired throughout\nthe realm.", \
            "Soon after his return, young Erek\naccomplished the Rite of Passage and\njoined adult society. To his surprise, he\nwas sent to the Elvish Council at the\nHigh City of Elgilad, as an ambassador\nfor his people."]
        
        # -- text colors
        self.colors = ["white", "yellow", "red", "violet", "blue", "green"]
         
        # -- misc stuff
        self.index = 0
        self.bubble = self.make_bubble ()
        self.done = 0
        
        # -- the images
        self.wall = adonthell.win_image ()
        self.wall.load_raw ('gfx/cutscene/extro_wall.img')
        self.wall.pack ()
        self.wall.thisown = 0
        
        self.chest = adonthell.win_image ()
        self.chest.load_raw ('gfx/cutscene/extro_chest.img')
        self.chest.set_mask (1)
        self.chest.move (75, 0)
        self.chest.pack ()
        self.chest.thisown = 0
        
        self.o_bag = adonthell.win_image ()
        self.o_bag.load_raw ('gfx/cutscene/extro_open_bag.img')
        self.o_bag.pack ()
        self.o_bag.thisown = 0
        
        self.c_bag = adonthell.win_image ()
        self.c_bag.load_raw ('gfx/cutscene/extro_closed_bag.img')
        self.c_bag.pack ()
        self.c_bag.thisown = 0
        
        self.bjarn = adonthell.win_image ()
        self.bjarn.load_raw ('gfx/cutscene/extro_bjarn.img')
        self.bjarn.pack ()
        self.bjarn.thisown = 0


    def run (self):
        # -- Bjarn walks up to chest
        if self.index == 18:
            bjarn = self.text[2][0]
            if self.done == 0:
                bjarn.set_schedule_active (0)
                bjarn.set_goal (7, 3, adonthell.STAND_NORTH)
                self.done = 1
                
            if (bjarn.follow_path () == 0):
                return 
            else:
                adonthell.gamedata_player ().set_schedule_active (0)
                self.index = self.index + 1
                self.zoom_to_chest ()
                return
        
        # -- Talan bursts in
        elif self.index == 23 and self.done == 0:
            self.bubble = None
            bjarn = self.text[2][0]
            bjarn.go_south ()
            bjarn.load ('bjarn_crying.mchar')
            
            import events
            talan = adonthell.gamedata_get_character ('Talan Wendth')
            events.switch_submap (talan, 7, 1, 6, adonthell.STAND_EAST)
            talan.go_east ()
            talan.stand_south ()
            self.done = 1
        
        elif self.index == 34 and self.bubble == None:
            # -- shutdown the mapview, it's no longer needed
            adonthell.gamedata_player ().set_schedule_active (0)
            adonthell.gamedata_engine ().fade_out ()
            adonthell.gamedata_engine ().mapview_stop ()
            self.fade_to_forest ()
            return
        
        if self.bubble == None:
            self.index = self.index + 1
            self.bubble = self.make_bubble ()
            self.done = 0

    # -- create the text bubbles
    def make_bubble (self):
        (npc, wait, text) = self.text[self.index]
        length = len(text) + 100
        
        if npc != None:
            # -- get color
            color = self.colors[npc.get_color ()]
            
            # -- get position
            view = adonthell.gamedata_engine ().get_mapview ()
            area = adonthell.gamedata_engine ().get_landmap ().get_submap (7)
            
            offx = 0
            offy = 0
            
            if area.area_length () * 20 < view.length ():
                offx = (view.length () - area.area_length () * 20) / 2
            if ((area.area_height() * 20) < view.height()):
                offy = (view.height () - area.area_height() * 20) / 2
            
            x = (npc.posx () - view.posx ()) * 20 + offx + 10 - length / 2
            y = (npc.posy () - view.posy ()) * 20 + offy - 15
        else:
            color = 'red'
        
        # -- make bubble
        bubble = adonthell.text_bubble (text, color, 'original', length)
        bubble.thisown = 0
        
        # -- move it to the right place
        if npc != None:
            bubble.move (x, y - bubble.height ())
        else:
            bubble.move (160 - bubble.length () / 2, 20)
        
        # -- display
        bubble.set_visible (1)
        adonthell.win_manager_get_active ().add (bubble)
        
        if wait == 1:
            bubble.py_signal_connect (self.on_close_bubble, adonthell.win_event_CLOSE)
            return bubble
            
        else: return None

    # -- bubble death callback
    def on_close_bubble (self, retval):
        self.bubble = None

    # -- chest sequence
    def zoom_to_chest (self):
        self.window = adonthell.win_container ()
        self.window.move (0, 0)
        self.window.resize (320, 240)
        self.window.set_visible_border (0)
        self.window.add (self.wall)
        self.window.add (self.chest)
        self.window.set_activate (1)
        self.window.set_visible_all (1)
        self.window.py_signal_connect (self.on_draw, adonthell.win_event_UPDATE)
        
        self.draw_func = self.move_chest
        self.step = 0
        self.done = 1
        
        if self.bubble != None: 
            adonthell.win_manager_get_active ().remove (self.bubble)
            self.bubble = None
            
        adonthell.gamedata_engine ().main (self.window, 'fmv')

    def on_draw (self):
        if self.draw_func != None:
            self.draw_func ()

    # -- move the chest aside
    def move_chest (self):
        if self.step == 0:
            # -- "They were here ..."
            self.bubble = self.make_bubble ()
            self.step = 1
            return
        
        # -- wait a little
        elif self.step <= 80:
            self.step = self.step + 1
            return
         
        # -- wobble chest back and forth a little 
        elif self.step == 81:
            offset = -1
            if self.chest.x () <= 65: self.step = 82
        
        elif self.step == 82:
            offset = 2
            if self.chest.x () >= 70: self.step = 83
        
        elif self.step == 83:
            offset = -1
            if self.chest.x () <= 55: self.step = 84
            
        elif self.step == 84: 
            offset = 2
            if self.chest.x () >= 65: self.step = 85
        
        # -- slide (and accelerate) chest
        elif self.step == 85:
            offset = -1
            if self.chest.x () <= 20: self.step = 86
        
        elif self.step == 86:
            offset = -2
            if self.chest.x () <= -20: self.step = 87
        
        elif self.step == 87:
            offset = -3
            if self.chest.x () <= -200: self.step = 88
        
        # -- spring back a little
        elif self.step == 88:
            offset = 2
            if self.chest.x () >= -185: self.step = 89
        
        else:
            self.draw_func = self.show_niche
            self.step = 0
            return 
        
        self.chest.move (self.chest.x () + offset, 0)
        return 

    # -- show the bag
    def show_niche (self):
        if self.step == 0 and self.bubble == None:
            self.step = 1
            self.index = self.index + 1
            # -- "... well hidden and ..."
            self.bubble = self.make_bubble ()
            
        # -- fade closed bag in
        elif self.step == 1:
            self.c_bag.set_alpha (1)
            self.c_bag.set_visible (1)
            self.window.add (self.c_bag)
            self.step = self.step + 1            

        elif self.step > 1 and self.step <= 255:
            self.c_bag.set_alpha (self.step)
            self.step = self.step + 1
        
        # -- fading done
        elif self.step == 256:
            self.window.remove (self.chest)
            self.window.remove (self.wall)
            del self.chest
            del self.wall
            self.step = 257

        elif self.step == 257 and self.bubble == None:            
            self.step = 258
            self.index = self.index + 1
            # -- "Here"
            self.bubble = self.make_bubble ()
        
        # -- fade in open bag 
        elif self.step == 258:
            self.o_bag.set_alpha (3)
            self.o_bag.set_visible (1)
            self.window.add (self.o_bag)
            self.step = self.step + 1

        elif self.step > 258 and self.step <= 511:
            self.o_bag.set_alpha (self.step - 256)
            self.step = self.step + 1
        
        # -- wait a little
        elif self.step > 511 and self.step <= 600:
            self.step = self.step + 1

        # -- zoom to bjarn's face        
        elif self.step == 601:
            self.bjarn.set_visible (1)
            self.window.add (self.bjarn)
            self.window.remove (self.c_bag)
            self.window.remove (self.o_bag)
            del self.c_bag
            del self.o_bag
            
            self.step = 602
            self.index = self.index + 1
            # -- "But ..."
            self.bubble = self.make_bubble ()
        
        elif self.step == 602 and self.bubble == None:            
            self.step = 603
            self.index = self.index + 1
            # -- "... they are gone"
            self.bubble = self.make_bubble ()

        # -- wait a little more
        elif self.step > 602 and self.step <= 800:
            if self.bubble == None: self.step = self.step + 1
            
        elif self.step == 801:
            self.done = 0
            adonthell.gamedata_engine ().main_quit ()
            adonthell.gamedata_player ().set_schedule_active (1)
        
    # -- forest sequence
    def fade_to_forest (self):
    
        # -- drawing area
        self.da = adonthell.drawing_area ()
        self.da.resize (adonthell.screen_length (), adonthell.screen_height ())
        self.da.move (0, 0)

        # -- load images  
        self.wood1 = adonthell.image ()
        self.wood1.load_raw ("gfx/cutscene/forest3.img")
        
        self.wood2 = adonthell.image ()
        self.wood2.load_raw ("gfx/cutscene/forest2.img")
        self.wood2.set_mask (1)
        
        self.wood3 = adonthell.image ()
        self.wood3.load_raw ("gfx/cutscene/forest1.img")
        self.wood3.set_mask (1)

        self.black = adonthell.win_image ()
        self.black.resize (320, 240)
        self.black.fillrect (0, 0, 320, 240, 0)
        self.black.thisown = 0
        self.black.pack ()

        self.target = adonthell.win_image ()
        self.target.resize (320, 240)
        self.target.thisown = 0
        self.target.pack ()
        
        # -- label
        self.label = adonthell.win_label ()
        self.label.set_font (adonthell.win_manager_get_font ("white"))
        self.label.resize (240, 90)
        self.label.move (40, 20)
        self.label.thisown = 0
        self.label.pack ()
        
        # -- window
        self.window = adonthell.win_container ()
        self.window.move (0, 0)
        self.window.resize (320, 240)
        self.window.set_visible_border (0)
        self.window.set_trans_background (1)
        
        self.window.add (self.target)
        self.window.add (self.black)
        self.window.add (self.label)
        
        self.window.set_activate (1)
        self.window.set_visible_all (1)
        
        self.window.py_signal_connect (self.on_draw, adonthell.win_event_UPDATE)
        
        self.draw_func = self.forest_animation
        
        # -- misc stuff
        self.step = 0       # -- for the extro control
        self.anim = 0       # -- for the forest animation control
        self.index = 0      # -- index in the typeover array       
        self.delay = 0      # -- delay before adding new text
        self.cursor = 0     # -- cursor in the typeover text
        self.x = [0, 0, 0]  # -- offsets of the 3 forest pics

        adonthell.gamedata_engine ().main (self.window, 'fmv')

    def forest_animation (self):
        # -- animate
        update = 0
        self.anim = self.anim + 1
        if self.anim % 2 == 0:
            update = 1
            self.x[2] = self.update_wood (self.wood3, self.x[2])
        
        if self.anim % 3 == 0:
            update = 1
            self.x[1] = self.update_wood (self.wood2, self.x[1])
        
        if self.anim % 4 == 0:
            update = 1
            self.x[0] = self.update_wood (self.wood1, self.x[0])
        
        # -- draw
        if update == 1:
            self.draw_wood (self.wood1, self.x[0])
            self.draw_wood (self.wood2, self.x[1])
            self.draw_wood (self.wood3, self.x[2])
        
        # -- fade in
        if self.step == 0:
            alpha = self.black.alpha ()
            if alpha != 0:
                self.black.set_alpha (alpha - 1)
                return
            else:
                self.window.remove (self.black)
                del self.black
                self.step = 1
        
        elif self.step == 1:
            if self.index < len (self.typeover):
                if self.cursor < len (self.typeover[self.index]):
                    self.delay = self.delay + 1
                    
                    if self.delay >= 10:
                        if self.cursor == 0: self.label.set_text ("")
                        txt = self.typeover[self.index][self.cursor]
                        self.label.add_text (txt)
                        self.cursor = self.cursor + 1
                        
                        # -- little pause at the end of a sentence
                        if txt == '.': self.delay = -50
                        else: self.delay = 0
                else:
                    self.index = self.index + 1
                    self.cursor = 0
                    self.delay = -450
            else:
                self.delay = 0
                self.step = 2
        
        # -- wait some more
        elif self.step == 2:
            self.delay = self.delay + 1
            if self.delay == 500:
                  self.step = 3
        
        elif self.step == 3:
            adonthell.gamedata_engine ().main_quit ()

    # -- update the forest position
    def update_wood (self, pic, x):
        if x <= -pic.length (): x = x + pic.length ()
        else: x = x - 1
        return x

    # -- draw the forest
    def draw_wood (self, pic, x):
        pic.draw (x, 0, self.da, self.target)
        if x < adonthell.screen_length () - pic.length (): 
            pic.draw (pic.length () + x, 0, self.da, self.target)