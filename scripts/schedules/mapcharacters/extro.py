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
import events

class extro:
    def __init__(self, mapchar):
        # -- deactivate game controls
        adonthell.gamedata_engine ().set_control_active (0)
        
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
        self.text = [(bjarn, "There is no denying it. Yes, I feigned the theft."), \
            (jelom, "But why? And where are the gems then?"), \
            (bjarn, "Why? Haven't I made myself clear already?"), \
            (bjarn, "I despise those Elves and their uncanny ways."), \
            (bjarn, "Their ... meddling with reality contradicts all principles I learned to hold true."), \
            (bjarn, "And yet, I had to provide them with the reagents they need to perform their dark art."), \
            (bjarn, "I felt so ... ashamed!"), \
            (player, "And you believe that justifies the discomfort you caused my mistress?"), \
            (bjarn, "You cannot think further than your mistress, can you?"), \
            (bjarn, "Theft by a high born like Lady Silverhair would have been considered a grave insult by the clan elders."), \
            (bjarn, "Had she been convicted, they might have chosen to cease trading with her people. And that probably for many years!"), \
            (silverhair, "I feared as much and I feared the consequences."), \
            (silverhair, "Without the arcane arts my kind would soon succumb to the human tides."), \
            (silverhair, "But without gems and ores purchased from the small folk we cannot create magic."), \
            (jelom, "Who would have thought that?"), \
            (jelom, "Seems you owe " + player.get_name() + " here a big favour, if I may say so, Lady."), \
            (silverhair, "Rest assured that " + player.get_name() + "'s deeds will not be forgotten, good man."), \
            (jelom, "Well, this is settled then. What remains now are the whereabouts of the gems."), \
            (jelom, "Master Fingolson!"), \
            (None, "They were here all the time, safe from thieving hands, ..."), \
            (None, "... well hidden in a niche I carved during my previous visits."), \
            (None, "Here."), \
            (None, "But ..."), \
            (None, "... they are gone!"), \
            (talan, "Sir, sir! To the gate! Quick! The thief is loose!"), \
            (bjarn, "My jewels, oh my jewels!"), \
            (player, "By Andomiel's Tree! What happened to you, Talan?!"), \
            (talan, "It was the mercenary, sir! He sneaked upon me and hit me over the head."), \
            (silverhair, "O sweet irony."), \
            (jelom, "Then the gems have been stolen after all?!"), \
            (jelom, "By that scum, Alek!? Now that's funny."), \
            (bjarn, "How can you say that? And why are you still here?"), \
            (bjarn, "Will nobody go after my gems!?"), \
            (jelom, "What for?"), \
            (jelom, "Where you are going you won't need them any more. Besides, Alek is probably long gone by now ...")]

        # -- the typeover text
        self.typeover = ["And so Alek Endhelm escaped into the\nNorth, where he spent his newly gained\nwealth for Ale and other pleasures.", \
            "Bjarn Fingolson however, bereft of all\nhonour, was taken to Uzdun'kal and\nsentenced to the lowest labour.\nNowadays his fate serves as an example\nand a warning to generations of young Dwarves.", \
            "Lady Imoen Silverhair received the finest\nChrysoberyl Catseyes as a token of\nregret, and the magic rings and amulets\nshe crafted were of wondrous might and\nbeauty, desired and admired throughout\nthe realm.", \
            "Soon after his return, young Erek\naccomplished the Rite of Passage and\njoined adult society. To his surprise, he\nwas sent to the Elvish Council at the\nHigh City of Elgilad, as an ambassador\nfor his people."]

        # -- the credits
        self.credits = [("Adonthell", 1), \
            ("- Waste's Edge -", 3), \
            ("directed by:", 1), \
            ("Alexandre Courbot", 1), \
            ("Kai Sterker", 3), \
            ("written by:", 1), \
            ("Kai Sterker", 1), \
            ("Mike Nieforth", 1), \
            ("Josh Glover", 3), \
            ("based on an orignal idea by:", 1), \
            ("Kai Sterker", 3), \
            ("produced by:", 1), \
            ("the Adonthell team", 3), \
            ("executive producers:", 1), \
            ("GNU Savannah", 1), \
            ("Linuxgames.com", 5), \
            ("cast:", 1), \
            (adonthell.gamedata_player ().get_name () + " - you", 1), \
            ("Imoen Silverhair - herself", 1), \
            ("Bjarn Fingolson - himself", 1), \
            ("Erek Stonebreaker - himself", 1), \
            ("Orloth Redwyne - himself", 1), \
            ("Alek Endhelm - himself", 1), \
            ("Oliver Redwyne - himself", 1), \
            ("Talan Wendth - himself", 1), \
            ("Jelom Rasgar - himself", 1), \
            ("Tristan Illig - himself", 1), \
            ("Fellnir Kezular - himself", 1), \
            ("Lucia Redwyne - herself", 1), \
            ("Rhayne Frostbloom - herself", 1), \
            ("Sarin Trailfollower - himself", 1), \
            ("Janesta Skywind - herself", 2), \
            ("Mrs. Frostbloom's assistant:", 1), \
            ("Yeti", 2), \
            ("casting:", 1), \
            ("Benjamin Walther-Franks", 5), \
            ("director of photography:", 1), \
            ("Alexandre Courbot", 2), \
            ("art director:", 1), \
            ("James Nash", 2), \
            ("assistant art director:", 1), \
            ("Benjamin Walther-Franks", 2), \
            ("wardrobe:", 1), \
            ("Benjamin Walther-Franks", 2), \
            ("props masters:", 1), \
            ("James Nash", 1), \
            ("Kai Sterker", 2), \
            ("location managers:", 1), \
            ("Alexandre Courbot", 1), \
            ("James Nash", 2), \
            ("grip:", 1), \
            ("Alexandre Courbot", 5), \
            ("\"Window\" unit:", 2), \
            ("director:", 1), \
            ("Joel Vennin", 2), \
            ("assistant director:", 1), \
            ("Joel Vennin", 2), \
            ("best boy:", 1), \
            ("Yeti", 2), \
            ("runner:", 1), \
            ("Joel Vennin", 5), \
            ("music by:", 1), \
            ("Joseph Toscano", 2), \
            ("foley artist:", 1), \
            ("Joseph Toscano", 2), \
            ("title design:", 1), \
            ("John Havard", 1), \
            ("James Nash", 3), \
            ("soundtrack available on:", 1), \
            ("http://www.zhaytee.com/...", 5), \
            ("the Adonthell team whishes to thank:", 2), \
            ("Al Koskelin", 1), \
            ("Andrew Henderson", 1), \
            ("Chris Harris", 1), \
            ("Mark Howson", 1), \
            ("Dave Peticolas", 1), \
            ("Josh's friend doing the CVS", 1), \
            ("Meandus", 1), \
            ("Deniz Oezsen", 2), \
            ("The people behind SDL, Ogg Vorbis,", 1), \
            ("Python and all the other Free", 1), \
            ("Software developers whose work", 1), \
            ("made Adonthell possible", 3), \
            ("career portal:", 1), \
            ("http://adonthell.linuxgames.com/development/", 3), \
            ("No Yetis were harmed during\n the production of this game", 5), \
            ("presented in", 2), \
            ("Ogg Vorbis Stereo", 1), \
            ("(where available)", 7), \
            ("The END", 13), \
            ("Joel, you're fired!", -1)]

        # -- text colors
        self.colors = ["white", "yellow", "red", "violet", "blue", "green"]
         
        # -- misc stuff
        self.index = 34
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
            bjarn = self.text[2][0]
            bjarn.go_south ()
            bjarn.load ('bjarn_crying.mchar')
            
            talan = adonthell.gamedata_get_character ('Talan Wendth')
            talan.load ("talan_beaten.mchar")
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
        (npc, text) = self.text[self.index]
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
        
        bubble.py_signal_connect (self.on_close_bubble, adonthell.win_event_CLOSE)
        return bubble

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
            if self.bubble != None: 
                adonthell.win_manager_get_active ().remove (self.bubble)
                self.bubble = None
            adonthell.gamedata_engine ().main_quit ()
            adonthell.gamedata_player ().set_schedule_active (1)
            self.done = 0
            self.index = 23
        
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
        self.label.move (40, 30)
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
        self.index = 3      # -- index in the typeover array       
        self.delay = 0      # -- delay before adding new text
        self.cursor = 0     # -- cursor in the typeover text
        self.x = [0, 0, 0]  # -- offsets of the 3 forest pics

        adonthell.gamedata_engine ().main (self.window, 'fmv')
        
        # -- quit!
        adonthell.gamedata_engine ().main_quit ()
        
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
                self.step = 1
        
        elif self.step == 1:
            if self.index < len (self.typeover):
                if self.cursor < len (self.typeover[self.index]):
                    self.delay = self.delay + 1
                    
                    if self.delay >= 7:
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
                    self.delay = -350
            else:
                self.delay = 0
                self.step = 2
        
        # -- wait some more
        elif self.step == 2:
            self.delay = self.delay + 1
            if self.delay == 350:
                  self.window.add (self.black)
                  self.step = 3
        
        # -- fade out
        elif self.step == 3:
            alpha = self.black.alpha ()
            if alpha != 255:
                self.black.set_alpha (alpha + 1)
                return
            else:
                self.draw_func = self.scroll_credits
                adonthell.win_manager_get_active ().remove (self.window)
                del self.window
                adonthell.win_manager_get_active ().add (self.make_credits ())        
    
    # -- update the forest position
    def update_wood (self, pic, x):
        if x >= pic.length (): x = x - pic.length ()
        else: x = x + 1
        return x

    # -- draw the forest
    def draw_wood (self, pic, x):
        pic.draw (x - pic.length (), 0, self.da, self.target)
        if x < adonthell.screen_length (): 
            pic.draw (x, 0, self.da, self.target)

    # -- prepare credits
    def make_credits (self):
        # -- window
        self.window = adonthell.win_container ()
        self.window.move (0, 30)
        self.window.resize (320, 180)
        self.window.set_visible_border (0)
        self.window.set_trans_background (1)
        self.window.set_activate (1)
        self.window.set_visible (1)

        # -- list of visible credit lines        
        self.labels = []
        self.index = 0
        self.anim = 0
        
        # -- first label
        self.make_credit_label (190)
        
        self.window.py_signal_connect (self.on_draw, adonthell.win_event_UPDATE)
        
        return self.window
    
    # -- make a credit label
    def make_credit_label (self, ypos):
        if self.index >= len (self.credits):
            return             
        
        if self.index > 0:
             ypos = ypos + (self.credits[self.index - 1][1] - 1) * 14

        label = adonthell.win_label ()
        label.resize (10, 0)
        label.set_font (adonthell.win_manager_get_font ("white"))
        label.set_align (adonthell.win_base_ALIGN_CENTER)
        label.set_form (adonthell.label_AUTO_SIZE)
        label.set_text (self.credits[self.index][0])
        label.move (label.x (), ypos)
        label.set_visible (1)
        label.thisown = 0
        label.pack ()

        self.labels.append (label)
        self.window.add (label)
            
        self.index = self.index + 1
        
        
    # -- scroll credits
    def scroll_credits (self):
        self.anim = self.anim + 1
        if self.anim % 3 != 0: return
        
        idx = 0
        
        # -- scroll all visible labels
        while idx < len (self.labels):
            label = self.labels[idx]
            label.move (label.x (), label.y () - 1)
            
            # -- remove label once it is through
            if label.y () + label.height () < -5:
                self.labels.remove (label)
            else:
                idx = idx + 1
        
        # -- add new line if necessary
        if label.y () - 180 < 0:
            self.make_credit_label (label.y () + label.height ())
            
        # -- finished
        if len (self.labels) == 0:
            adonthell.gamedata_engine ().main_quit ()
