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

# -- pygettext support
def N_(message): return message
def _(message): return adonthell.nls_translate (message)

class extro:
    def __init__(self, mapchar):
        # -- audio
        adonthell.audio_set_schedule_active (0)
        adonthell.audio_fade_out_background (1000)
        
        # -- grab the character's we need
        bjarn = adonthell.gamedata_get_character ("Bjarn Fingolson")
        erek = adonthell.gamedata_get_character ("Erek Stonebreaker")
        jelom = adonthell.gamedata_get_character ("Jelom Rasgar")
        talan = adonthell.gamedata_get_character ("Talan Wendth")
        talan.set_schedule_active (0)
        silverhair = adonthell.gamedata_get_character ("Imoen Silverhair")
        player = adonthell.gamedata_player ()

        # -- init the bubble texts
        #    (character, text)
        self.text = [(bjarn, N_("There is no denying it. Yes, I feigned the theft. ")), \
            (erek, N_("But Master? How could you do such an infamous deed? ")), \
			(jelom, N_("That I would know as well! And where are the gems then? ")), \
            (bjarn, N_("What? Haven't I made myself clear already? ")), \
            (bjarn, N_("I despise those Elves and their uncanny ways. ")), \
            (bjarn, N_("Their ... meddling with reality contradicts all principles I learnt to hold true.     ")), \
            (bjarn, N_("And yet, I had to provide them with the reagents they need to perform their dark art.     ")), \
            (bjarn, N_("I felt so ... ashamed! ")), \
            (player, N_("And you believe this justifies the discomfort you caused my mistress? ")), \
            (bjarn, N_("You cannot think further than your mistress, can you? ")), \
            (bjarn, N_("Theft by a high born like Lady Silverhair would have been considered a grave insult by the clan elders.     ")), \
            (bjarn, N_("Had she been convicted, they might have chosen to cease trading with her likes. ")), \
            (bjarn, N_("It might have been years before any Elf got his filthy hands on our beloved gems again! ")), \
			(silverhair, N_("I feared as much and I       feared the consequences.")), \
            (silverhair, N_("Without the arcane arts my kind would soon succumb to the human tides. ")), \
            (silverhair, N_("But without gems and ores purchased from the small folk we cannot create magic. ")), \
            (jelom, N_("Who would have thought that? ")), \
            (jelom, _("Seems you owe %s here a big favour, if I may say so, Lady. ") % player.get_name()), \
            (silverhair, _("Rest assured that %s's deeds will not be forgotten, good man. ") %  player.get_name()), \
            (jelom, N_("Well, this is settled then. What remains now are the whereabouts of the gems. ")), \
            (jelom, N_("Master Fingolson! ")), \
            (None, N_("They were here all the time, safe from thieving hands, ...")), \
            (None, N_("... well hidden in a niche I carved during my previous visits.")), \
            (None, N_("Right here.")), \
            (None, N_("But ...")), \
            (None, N_("... they are gone!")), \
            (talan, N_("Sir, sir! To the gate! Quick! The thief is loose!")), \
            (bjarn, N_("My jewels, oh my jewels!")), \
            (player, N_("By Andomiel's Tree! What happened to you, Talan?!")), \
            (talan, N_("It was the mercenary, sir! He sneaked upon me and hit me over the head.")), \
            (silverhair, N_("O sweet irony.")), \
            (jelom, N_("Then the gems have been stolen after all?!")), \
            (jelom, N_("By that scum, Alek!? Now that's funny.")), \
            (bjarn, N_("How can you say that? And why are you still here?")), \
            (bjarn, N_("Will nobody go after my gems!?")), \
            (jelom, N_("What for?")), \
            (jelom, N_("Where you are going you won't need them any more. Besides, Alek is probably long gone by now ..."))]

        # -- the typeover text
        self.typeover = [N_("And so Alek Endhelm escaped into the\nNorth, where he spent his newly gained\nwealth for Ale and other pleasures."), \
            N_("Bjarn Fingolson however, bereft of all\nhonour, was taken to Uzdun'kal and\nsentenced to the lowest labour.\nNowadays his fate serves as an example\nand a warning to generations of young Dwarves."), \
            N_("Lady Imoen Silverhair received the finest\nChrysoberyl Catseyes as a token of\nregret, and the magic rings and amulets\nshe crafted were of wondrous might and\nbeauty, desired and admired throughout\nthe realm."), \
            N_("Soon after his return, young Erek\naccomplished the Rite of Passage and\njoined adult society. To his surprise, he\nwas sent to the Elvish Council at the\nHigh City of Elgilad, as an ambassador\nfor his people.")]

        # -- the credits
        #    (text, delay)
        self.credits = [("Adonthell", 1), \
            ("- Waste's Edge -", 3), \
            (_("directed by:"), 1), \
            ("Alexandre Courbot", 1), \
            ("Kai Sterker", 3), \
            (_("written by:"), 1), \
            ("Kai Sterker", 1), \
            ("Mike Nieforth", 1), \
            ("Josh Glover", 3), \
            (_("based on an original idea by:"), 1), \
            ("Kai Sterker", 3), \
            (_("produced by:"), 1), \
            (_("the Adonthell team"), 3), \
            (_("executive producers:"), 1), \
            ("Sourceforge.net", 1), \
            ("GNU Savannah", 1), \
            ("Linuxgames.com", 5), \
            (_("cast:"), 1), \
            (adonthell.gamedata_player ().get_name () + _(" - you"), 1), \
            (_("Imoen Silverhair - herself"), 1), \
            (_("Bjarn Fingolson - himself"), 1), \
            (_("Erek Stonebreaker - himself"), 1), \
            (_("Orloth Redwyne - himself"), 1), \
            (_("Alek Endhelm - himself"), 1), \
            (_("Oliver Redwyne - himself"), 1), \
            (_("Talan Wendth - himself"), 1), \
            (_("Jelom Rasgar - himself"), 1), \
            (_("Tristan Illig - himself"), 1), \
            (_("Fellnir Kezular - himself"), 1), \
            (_("Lucia Redwyne - herself"), 1), \
            (_("Rhayne Frostbloom - herself"), 1), \
            (_("Sarin Trailfollower - himself"), 1), \
            (_("Janesta Skywind - herself"), 2), \
            (_("Mrs. Frostbloom's assistant:"), 1), \
            ("Yeti", 2), \
            (_("casting:"), 1), \
            ("Benjamin Walther-Franks", 5), \
            (_("director of photography:"), 1), \
            ("Alexandre Courbot", 2), \
            (_("art director:"), 1), \
            ("James Nash", 2), \
            (_("assistant art director:"), 1), \
            ("Benjamin Walther-Franks", 2), \
            (_("wardrobe:"), 1), \
            ("Benjamin Walther-Franks", 2), \
            (_("props masters:"), 1), \
            ("James Nash", 1), \
            ("Kai Sterker", 2), \
            (_("location managers:"), 1), \
            ("Alexandre Courbot", 1), \
            ("James Nash", 2), \
            (_("grip:"), 1), \
            ("Alexandre Courbot", 5), \
            (_("\"Window\" unit:"), 2), \
            (_("director:"), 1), \
            ("Joel Vennin", 2), \
            (_("assistant director:"), 1), \
            ("Joel Vennin", 2), \
            (_("best boy:"), 1), \
            ("Yeti", 2), \
            (_("runner:"), 1), \
            ("Joel Vennin", 5), \
            (_("music by:"), 1), \
            ("Joseph Toscano", 2), \
            (_("foley artist:"), 1), \
            ("Joseph Toscano", 2), \
            (_("title design:"), 1), \
            ("John Havard", 1), \
            ("James Nash", 2), \
            (_("soundtrack available on:"), 1), \
            ("http://zhaymusic.com/wastesedge/", 5), \
            (_("the Adonthell team wishes to thank:"), 2), \
            ("Al Koskelin", 1), \
            ("Andrew Henderson", 1), \
            ("Chris Harris", 1), \
            ("Mark Howson", 1), \
            ("Dave Peticolas", 1), \
            ("Ryan O'Neil", 1), \
            ("Meandus", 1), \
            ("Deniz Oezsen", 2), \
            (_("The people behind SDL, Ogg Vorbis,"), 1), \
            (_("Python, SWIG and all the other Free"), 1), \
            (_("Software developers whose work"), 1), \
            (_("made Adonthell possible"), 3), \
            (_("career portal:"), 1), \
            ("http://adonthell.linuxgames.com/development/", 5), \
            (_("No Yetis were harmed during\n the production of this game"), 5), \
            (_("presented in"), 2), \
            (_("Ogg Vorbis Stereo"), 1), \
            (_("(where available)"), 14), \
            (_("The END"), 6), \
            (_("Joel, you are fired! ;)"), -1)]

            
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

        # -- set new audio schedule and play extro music
        adonthell.audio_load_background (0, "audio/at-demo-9.ogg")
        adonthell.audio_play_background (0)
    
    def run (self):
        # -- deactivate game controls
        if self.index == 0:
            adonthell.gamedata_engine ().set_control_active (0)

        # -- Bjarn walks up to chest
        elif self.index == 20:
            bjarn = self.text[3][0]
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
        elif self.index == 25 and self.done == 0:
            bjarn = self.text[3][0]
            bjarn.go_south ()
            bjarn.load ('bjarn_crying.mchar')
            bjarn.pause ()
            
            talan = adonthell.gamedata_get_character ('Talan Wendth')
            talan.load ("talan_beaten.mchar")
            events.switch_submap (talan, 7, 1, 6, adonthell.STAND_EAST)
            
            # -- everyone look at Talan
            adonthell.gamedata_get_character ("Erek Stonebreaker").stand_west ()
            adonthell.gamedata_get_character ("Jelom Rasgar").stand_west ()
            adonthell.gamedata_get_character ("Imoen Silverhair").stand_west ()
            adonthell.gamedata_player ().stand_west ()
            
            talan.go_east ()
            talan.stand_south ()
            self.done = 1
        
        elif self.index == 36 and self.bubble == None:
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
            return
        
        # -- fading done
        elif self.step == 256:
            self.window.remove (self.chest)
            self.window.remove (self.wall)
            del self.chest
            del self.wall
            self.step = 257

        elif self.step > 256 and self.step <= 306:
            self.step = self.step + 1
            return

        elif self.step == 307 and self.bubble == None:            
            self.step = 308
            self.index = self.index + 1
            # -- "Right Here"
            self.bubble = self.make_bubble ()
        
        # -- fade in open bag 
        elif self.step == 308:
            self.o_bag.set_alpha (3)
            self.o_bag.set_visible (1)
            self.window.add (self.o_bag)
            self.step = self.step + 1

        elif self.step > 308 and self.step <= 561:
            self.o_bag.set_alpha (self.step - 307)
            self.step = self.step + 1
        
        # -- wait a little
        elif self.step > 561 and self.step <= 650:
            self.step = self.step + 1

        # -- zoom to bjarn's face        
        elif self.step == 651:
            # -- audio
            adonthell.audio_load_background (1, "audio/at-demo-a.ogg")
            adonthell.audio_play_background (1)
            
            self.bjarn.set_visible (1)
            self.window.add (self.bjarn)
            self.window.remove (self.c_bag)
            self.window.remove (self.o_bag)
            del self.c_bag
            del self.o_bag
            
            self.step = 652
            self.index = self.index + 1
            # -- "But ..."
            self.bubble = self.make_bubble ()
        
        elif self.step == 652 and self.bubble == None:            
            self.step = 653
            self.index = self.index + 1
            # -- "... they are gone"
            self.bubble = self.make_bubble ()

        # -- wait a little more
        elif self.step > 652 and self.step <= 850:
            if self.bubble == None: self.step = self.step + 1
            
        elif self.step == 851:
            if self.bubble != None: 
                adonthell.win_manager_get_active ().remove (self.bubble)
                self.bubble = None
            adonthell.gamedata_engine ().main_quit ()
            adonthell.gamedata_player ().set_schedule_active (1)
            self.done = 0
            self.index = 25
        
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

        self.alek_run = adonthell.animation ()
        self.alek_run.load ("gfx/cutscene/running_alek.anim")
        self.alek_run.play ()

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
        
        # -- audio
        adonthell.audio_fade_out_background (500)
        
        # -- misc stuff
        self.step = 0       # -- for the extro control
        self.anim = 0       # -- for the forest animation control
        self.index = 0      # -- index in the typeover array
        self.delay = 0      # -- delay before adding new text
        self.cursor = 0     # -- cursor in the typeover text
        self.x = [0, 0, 0]  # -- offsets of the 3 forest pics

        adonthell.gamedata_engine ().main (self.window, 'fmv')
        
        # -- quit!
        adonthell.audio_fade_out_background (500)
        adonthell.gamedata_engine ().main_quit ()
        
    def forest_animation (self):
        # -- animate
        update = 0
        self.anim = self.anim + 1
        if self.anim % 2 == 0:
            update = 1
            self.alek_run.update ()
            self.x[2] = self.update_wood (self.wood3, self.x[2])
        	
            if self.anim % 4 == 0:
                self.x[0] = self.update_wood (self.wood1, self.x[0])

        
        if self.anim % 3 == 0:
            update = 1
            self.x[1] = self.update_wood (self.wood2, self.x[1])
        
        # -- draw
        if update == 1:
            self.draw_wood (self.wood1, self.x[0])
            self.draw_wood (self.wood2, self.x[1])
            self.alek_run.draw (110, 120, self.da, self.target)
            self.draw_wood (self.wood3, self.x[2])
        
        # -- fade in
        if self.step == 0:
            alpha = self.black.alpha ()
            if alpha != 0:
                self.black.set_alpha (alpha - 1)
                return
            else:
                adonthell.audio_load_background (2, "audio/at-demo-2.ogg")
                adonthell.audio_play_background (2)

                self.window.remove (self.black)
                self.step = 1
        
        elif self.step == 1:
            if self.index < len (self.typeover):
                if self.cursor < len (self.typeover[self.index]):
                    self.delay = self.delay + 1
                    
                    if self.delay >= 6:
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
                    self.delay = -200
            else:
                self.delay = 0
                self.step = 2
        
        # -- wait some more
        elif self.step == 2:
            self.delay = self.delay + 1
            if self.delay == 350:
                  # -- audio
                  adonthell.audio_fade_out_background (2000)
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
        # -- audio
        adonthell.audio_load_background (0, "audio/at-demo-8.ogg")
        adonthell.audio_play_background (0)

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
        self.step = 0
        self.index = 0
        self.anim = 0
        
        # -- first label
        self.make_credit_label (190)
        
        self.window.py_signal_connect (self.on_draw, adonthell.win_event_UPDATE)
        
        return self.window
    
    # -- make a credit label
    def make_credit_label (self, ypos):
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

        if self.step == 0:
            idx = 0
        
            # -- scroll all visible labels
            while idx < len (self.labels):
                label = self.labels[idx]
                label.move (label.x (), label.y () - 1)
            
                # -- remove label once it is through
                if label.y () + label.height () < -5:
                    self.labels.remove (label)

                # -- next
                else:
                    idx = idx + 1
            
            # -- stop 'The END' in the middle of the screen 
            if self.credits[self.index][1] == -1:
                if label.y () + label.height ()/2 == 90:
                    self.labels.remove (label)
                    self.delay = 0
                    self.step = 1
        
            # -- else, add new line if necessary
            elif label.y () - 180 < 0:
                self.make_credit_label (label.y () + label.height ())
        
        # -- wait a little
        elif self.step == 1:
            self.delay = self.delay + 1
            if self.delay == 70:
                  self.make_credit_label (90)
                  self.step = 2

        # -- finish
        elif self.step == 2:
            self.delay = self.delay + 1
            if self.delay == 100:
                adonthell.gamedata_engine ().main_quit ()
