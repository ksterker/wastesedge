### The themes and fonts we'll use
win_manager_add_theme ("original")
win_manager_add_theme ("silverleaf")

win_manager_add_font ("yellow")
win_manager_add_font ("red")
win_manager_add_font ("violet")
win_manager_add_font ("blue")
win_manager_add_font ("green")
win_manager_add_font ("white")
win_manager_add_font ("original")
win_manager_add_font ("silverleaf")

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
        self.bgimage = win_image ()
        self.bgimage.move (0, 0)
        image.copy (self.bgimage, background)
        self.bgimage.pack ()
        
        self.window = win_container ()
        self.window.move (0, 0)
        self.window.resize (320, 240)
        self.window.set_visible_border (0)
        self.window.add (self.bgimage)
        self.window.set_visible_all (1)

        win_manager_add (self.window)

        self.menu = main_menu (0, 0)
        self.menu.thisown = C
        self.menu.py_signal_connect (self.on_menu_close, win_event_CLOSE)
        
        win_manager_add (self.menu)
        win_manager_set_focus (self.menu)
        self.menu = None

    # on to the main menu
    def on_menu_close (self, retval):
        self.quit = retval


    def loop (self):
        self.cont = 0
        while self.cont == 0:
            input_update ()

            for k in range (gametime_frames_to_do()+1):
                win_manager_input_update ()
                win_manager_update ()

            win_manager_draw ()
            screen_show ()
            gametime_update()

            self.cont = self.quit

        self.window.remove (self.bgimage)
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

audio_pause_music ()

##retval = 1

if retval < 5: 
    if retval == 1:
        gamedata_load (0)

        # Creates the context for the game start
        map_engine.load_map ("test.map")
        
        lm = map_engine.get_landmap ()
        the_player.set_val ("gender", MALE)
        the_player.set_val ("race", HALFELF)
        the_player.load ("player.mchar")
        the_player.set_map (lm)
        the_player.jump_to (0, 11, 18, STAND_EAST)
        the_player.set_schedule ("keyboard_control")
        map_engine.set_mapview_schedule ("center_player")
        
        # Now add a few events...
        ev = enter_event ()
        ev.thisown = C
        ev.submap = 0
        ev.x = 18
        ev.y = 13
        ev.set_script ("inn_to_yard")
        lm.add_event (ev)
        
        ev = enter_event ()
        ev.thisown = C
        ev.submap = 1
        ev.x = 13
        ev.y = 8
        ev.set_script ("inn_to_yard")
        lm.add_event (ev)
        
        ev = enter_event ()
        ev.thisown = C
        ev.submap = 1
        ev.x = 14
        ev.y = 4
        ev.set_script ("common_to_parlor")
        lm.add_event (ev)
        
        ev = enter_event ()
        ev.thisown = C
        ev.submap = 2
        ev.x = 0
        ev.y = 4
        ev.set_script ("common_to_parlor")
        lm.add_event (ev)

        ev = enter_event ()
        ev.thisown = C
        ev.submap = 1
        ev.x = 1
        ev.y = 8
        ev.set_script ("common_to_kitchen")
        lm.add_event (ev)
        
        ev = enter_event ()
        ev.thisown = C
        ev.submap = 3
        ev.x = 1
        ev.y = 1
        ev.set_script ("common_to_kitchen")
        lm.add_event (ev)

        ev = enter_event ()
        ev.thisown = C
        ev.submap = 3
        ev.x = 7
        ev.y = 3
        ev.set_script ("yard_to_kitchen")
        lm.add_event (ev)

        ev = enter_event ()
        ev.thisown = C
        ev.submap = 0
        ev.x = 11
        ev.y = 14
        ev.set_script ("yard_to_kitchen")
        lm.add_event (ev)

        ev = leave_event ()
        ev.thisown = C
        ev.submap = 0
        ev.x = 18
        ev.y = 14
        ev.dir = WALK_NORTH
        ev.set_script ("open_inn_door")
        lm.add_event (ev)

        ev = enter_event ()
        ev.thisown = C
        ev.submap = 4
        ev.x = 3
        ev.y = 5
        ev.set_script ("cellar_to_bath")
        lm.add_event (ev)

        ev = enter_event ()
        ev.thisown = C
        ev.submap = 5
        ev.x = 4
        ev.y = 7
        ev.set_script ("cellar_to_bath")
        lm.add_event (ev)

        ev = enter_event ()
        ev.thisown = C
        ev.submap = 4
        ev.x = 0
        ev.y = 6
        ev.set_script ("cellar_to_alek")
        lm.add_event (ev)

        ev = enter_event ()
        ev.thisown = C
        ev.submap = 4
        ev.x = 0
        ev.y = 7
        ev.set_script ("cellar_to_alek")
        lm.add_event (ev)

        ev = enter_event ()
        ev.thisown = C
        ev.submap = 6
        ev.x = 6
        ev.y = 6
        ev.set_script ("cellar_to_alek")
        lm.add_event (ev)

        ev = enter_event ()
        ev.thisown = C
        ev.submap = 6
        ev.x = 6
        ev.y = 7
        ev.set_script ("cellar_to_alek")
        lm.add_event (ev)

        ev = enter_event ()
        ev.thisown = C
        ev.submap = 4
        ev.x = 0
        ev.y = 9
        ev.set_script ("cellar_to_storage")
        lm.add_event (ev)

        ev = enter_event ()
        ev.thisown = C
        ev.submap = 4
        ev.x = 0
        ev.y = 10
        ev.set_script ("cellar_to_storage")
        lm.add_event (ev)

        ev = enter_event ()
        ev.thisown = C
        ev.submap = 8
        ev.x = 7
        ev.y = 3
        ev.set_script ("cellar_to_storage")
        lm.add_event (ev)

        ev = enter_event ()
        ev.thisown = C
        ev.submap = 8
        ev.x = 7
        ev.y = 4
        ev.set_script ("cellar_to_storage")
        lm.add_event (ev)

        ev = enter_event ()
        ev.thisown = C
        ev.submap = 4
        ev.x = 10
        ev.y = 6
        ev.set_script ("cellar_to_dwarfs")
        lm.add_event (ev)

        ev = enter_event ()
        ev.thisown = C
        ev.submap = 4
        ev.x = 10
        ev.y = 7
        ev.set_script ("cellar_to_dwarfs")
        lm.add_event (ev)

        ev = enter_event ()
        ev.thisown = C
        ev.submap = 7
        ev.x = 0
        ev.y = 6
        ev.set_script ("cellar_to_dwarfs")
        lm.add_event (ev)

        ev = enter_event ()
        ev.thisown = C
        ev.submap = 7
        ev.x = 0
        ev.y = 7
        ev.set_script ("cellar_to_dwarfs")
        lm.add_event (ev)

        ev = enter_event ()
        ev.thisown = C
        ev.submap = 9
        ev.x = 9
        ev.y = 2
        ev.set_script ("1st_to_fellnir")
        lm.add_event (ev)

        ev = enter_event ()
        ev.thisown = C
        ev.submap = 10
        ev.x = 0
        ev.y = 3
        ev.set_script ("1st_to_fellnir")
        lm.add_event (ev)

        ev = enter_event ()
        ev.thisown = C
        ev.submap = 9
        ev.x = 0
        ev.y = 2
        ev.set_script ("1st_to_frostbloom")
        lm.add_event (ev)

        ev = enter_event ()
        ev.thisown = C
        ev.submap = 11
        ev.x = 5
        ev.y = 3
        ev.set_script ("1st_to_frostbloom")
        lm.add_event (ev)

        ev = enter_event ()
        ev.thisown = C
        ev.submap = 9
        ev.x = 7
        ev.y = 4
        ev.set_script ("1st_to_player")
        lm.add_event (ev)

        ev = enter_event ()
        ev.thisown = C
        ev.submap = 12
        ev.x = 5
        ev.y = 1
        ev.set_script ("1st_to_player")
        lm.add_event (ev)

        ev = enter_event ()
        ev.thisown = C
        ev.submap = 9
        ev.x = 1
        ev.y = 7
        ev.set_script ("1st_to_silverhair")
        lm.add_event (ev)

        ev = enter_event ()
        ev.thisown = C
        ev.submap = 13
        ev.x = 5
        ev.y = 1
        ev.set_script ("1st_to_silverhair")
        lm.add_event (ev)

        ev = enter_event ()
        ev.thisown = C
        ev.submap = 14
        ev.x = 3
        ev.y = 5
        ev.set_script ("2nd_to_redwyne")
        lm.add_event (ev)

        ev = enter_event ()
        ev.thisown = C
        ev.submap = 15
        ev.x = 0
        ev.y = 5
        ev.set_script ("2nd_to_redwyne")
        lm.add_event (ev)

        ev = enter_event ()
        ev.thisown = C
        ev.submap = 14
        ev.x = 0
        ev.y = 5
        ev.set_script ("2nd_to_oliver")
        lm.add_event (ev)

        ev = enter_event ()
        ev.thisown = C
        ev.submap = 16
        ev.x = 7
        ev.y = 5
        ev.set_script ("2nd_to_oliver")
        lm.add_event (ev)

        ev = enter_event ()
        ev.thisown = C
        ev.submap = 14
        ev.x = 1
        ev.y = 8
        ev.set_script ("2nd_to_illig")
        lm.add_event (ev)

        ev = enter_event ()
        ev.thisown = C
        ev.submap = 17
        ev.x = 6
        ev.y = 1
        ev.set_script ("2nd_to_illig")
        lm.add_event (ev)

        ev = enter_event ()
        ev.thisown = C
        ev.submap = 1
        ev.x = 12
        ev.y = 1
        ev.set_script ("common_to_1st")
        lm.add_event (ev)

        ev = enter_event ()
        ev.thisown = C
        ev.submap = 9
        ev.x = 8
        ev.y = 1
        ev.set_script ("common_to_1st")
        lm.add_event (ev)

        ev = enter_event ()
        ev.thisown = C
        ev.submap = 9
        ev.x = 6
        ev.y = 1
        ev.set_script ("1st_to_2nd")
        lm.add_event (ev)

        ev = enter_event ()
        ev.thisown = C
        ev.submap = 14
        ev.x = 4
        ev.y = 1
        ev.set_script ("1st_to_2nd")
        lm.add_event (ev)

        ev = enter_event ()
        ev.thisown = C
        ev.submap = 1
        ev.x = 9
        ev.y = 1
        ev.set_script ("common_to_cellar")
        lm.add_event (ev)

        ev = enter_event ()
        ev.thisown = C
        ev.submap = 4
        ev.x = 6
        ev.y = 1
        ev.set_script ("common_to_cellar")
        lm.add_event (ev)

        ev = enter_event ()
        ev.thisown = C
        ev.submap = 4
        ev.x = 12
        ev.y = 1
        ev.set_script ("barn_to_cellar")
        lm.add_event (ev)

        ev = enter_event ()
        ev.thisown = C
        ev.submap = 0
        ev.x = 24
        ev.y = 10
        ev.set_script ("barn_to_cellar")
        lm.add_event (ev)

        ev = enter_event ()
        ev.thisown = C
        ev.submap = 3
        ev.x = 6
        ev.y = 6
        ev.set_script ("kitchen_to_cellar")
        lm.add_event (ev)

        ev = enter_event ()
        ev.thisown = C
        ev.submap = 4
        ev.x = 3
        ev.y = 13
        ev.set_script ("kitchen_to_cellar")
        lm.add_event (ev)

        ev = enter_event ()
        ev.thisown = C
        ev.submap = 0
        ev.x = 12
        ev.y = 23
        ev.set_script ("yard_to_guards")
        lm.add_event (ev)

        ev = enter_event ()
        ev.thisown = C
        ev.submap = 18
        ev.x = 8
        ev.y = 3
        ev.set_script ("yard_to_guards")
        lm.add_event (ev)

        ev = enter_event ()
        ev.thisown = C
        ev.submap = 18
        ev.x = 1
        ev.y = 8
        ev.set_script ("guards_ground_to_1st")
        lm.add_event (ev)

        ev = enter_event ()
        ev.thisown = C
        ev.submap = 19
        ev.x = 1
        ev.y = 8
        ev.set_script ("guards_ground_to_1st")
        lm.add_event (ev)


        # Action events
        ev = action_event ()
        ev.thisown = C
        ev.submap = 1
        ev.x = 10
        ev.y = 2
        ev.dir = STAND_NORTH
        ev.set_script ("action_clock")
        lm.add_event (ev)

        ev = action_event ()
        ev.thisown = C
        ev.submap = 10
        ev.x = 3
        ev.y = 6
        ev.dir = STAND_NORTH
        ev.set_script ("action_alch_table")
        lm.add_event (ev)

        ev = action_event ()
        ev.thisown = C
        ev.submap = 10
        ev.x = 4
        ev.y = 6
        ev.dir = STAND_NORTH
        ev.set_script ("action_alch_table")
        lm.add_event (ev)

        ev = action_event ()
        ev.thisown = C
        ev.submap = 10
        ev.x = 2
        ev.y = 5
        ev.dir = STAND_EAST
        ev.set_script ("action_alch_table")
        lm.add_event (ev)

        ev = action_event ()
        ev.thisown = C
        ev.submap = 10
        ev.x = 5
        ev.y = 5
        ev.dir = STAND_WEST
        ev.set_script ("action_alch_table")
        lm.add_event (ev)

        ev = action_event ()
        ev.thisown = C
        ev.submap = 10
        ev.x = 3
        ev.y = 4
        ev.dir = STAND_SOUTH
        ev.set_script ("action_alch_table")
        lm.add_event (ev)

        ev = action_event ()
        ev.thisown = C
        ev.submap = 10
        ev.x = 4
        ev.y = 4
        ev.dir = STAND_SOUTH
        ev.set_script ("action_alch_table")
        lm.add_event (ev)

        # Now setup the characters
        lucia = characters ["Lucia Redwyne"]
        lucia.set_dialogue ("dialogues/lucia_start")
        lucia.load ("lucia.mchar")
        lucia.set_map (map_engine.get_landmap ())
        lucia.jump_to (3, 4, 2)
        lucia.set_action ("action_talk")
        lucia.stand_south ()
        
        orloth = characters ["Orloth Redwyne"]
        orloth.set_dialogue ("dialogues/orloth_start")
        orloth.load ("orloth.mchar")
        orloth.set_map (map_engine.get_landmap ())
        orloth.jump_to (1, 2, 2)
        orloth.set_action ("action_talk")
        orloth.stand_south ()
        orloth.set_schedule ("orloth")

        erek = characters ["Erek Stonebreaker"]
        erek.set_dialogue ("dialogues/erek_start")
        erek.load ("erek.mchar")
        erek.set_map (map_engine.get_landmap ())
        erek.jump_to (1, 5, 5)
        erek.set_action ("action_talk")
        erek.stand_north ()
        # changed Erek's text color to violet
        erek.set_color (3)
        erek.set_schedule ("erek")
        erek.set_portrait ("erek.pnm")

        talan = characters ["Talan Wendth"]
        talan.set_dialogue ("dialogues/talan_start")
        talan.load ("talan.mchar")
        talan.set_map (map_engine.get_landmap ())
        talan.jump_to (0, 11, 19)
        talan.set_action ("action_talk")
        talan.stand_north ()
        talan.set_schedule ("talan")

        # -- that's a clone for now
        jelom = characters ["Jelom Rasgar"]
        jelom.set_dialogue ("dialogues/jelom_start")
        jelom.load ("talan.mchar")
        jelom.set_map (map_engine.get_landmap ())
        jelom.jump_to (9, 2, 6)
        jelom.set_action ("action_talk")
        jelom.stand_north ()
        jelom.set_schedule ("jelom")
        jelom.set_portrait ("jelom.pnm")

        # -- that's a clone for now
        alek = characters ["Alek Endhelm"]
        alek.set_dialogue ("dialogues/alek_start")
        alek.load ("servant2.mchar")
        alek.set_map (map_engine.get_landmap ())
        alek.jump_to (1, 1, 3)
        alek.set_action ("action_talk")
        alek.stand_south ()
        alek.set_schedule ("alek")

        oliver = characters ["Oliver Redwyne"]
        oliver.set_dialogue ("dialogues/oliver_start")
        oliver.load ("oliver.mchar")
        oliver.set_map (map_engine.get_landmap ())
        oliver.jump_to (0, 25, 15)
        oliver.set_action ("action_talk")
        oliver.stand_west ()
        oliver.set_schedule ("oliver")

        frostbloom = characters ["Rhayne Frostbloom"]
        frostbloom.set_dialogue ("dialogues/frostbloom_start")
        frostbloom.load ("frostbloom.mchar")
        frostbloom.set_map (map_engine.get_landmap ())
        frostbloom.jump_to (0, 18, 22)
        frostbloom.set_action ("action_talk")
        frostbloom.stand_north ()
        frostbloom.set_schedule ("frostbloom")

        bjarn = characters ["Bjarn Fingolson"]
        bjarn.set_dialogue ("dialogues/bjarn_start")
        bjarn.load ("bjarn.mchar")
        bjarn.set_map (map_engine.get_landmap ())
        bjarn.jump_to (7, 3, 6)
        bjarn.set_action ("action_talk")
        bjarn.stand_west ()

        silverhair = characters ["Imoen Silverhair"]
        silverhair.load ("silverhair.mchar")
        silverhair.set_map (map_engine.get_landmap ())
        silverhair.jump_to (13, 4, 6)
        silverhair.set_action ("action_talk")
        silverhair.stand_north ()
        silverhair.set_schedule ("silverhair")

        sarin = characters ["Sarin Trailfollower"]
        sarin.set_dialogue ("dialogues/sarin_start")
        sarin.load ("servant2.mchar")
        sarin.set_map (map_engine.get_landmap ())
        sarin.jump_to (13, 5, 3)
        sarin.set_action ("action_talk")
        sarin.stand_west ()
        sarin.set_schedule ("sarin")

        janesta = characters ["Janesta Skywind"]
        janesta.set_dialogue ("dialogues/janesta_start")
        janesta.load ("servant1.mchar")
        janesta.set_map (map_engine.get_landmap ())
        janesta.jump_to (13, 6, 3)
        janesta.set_action ("action_talk")
        janesta.stand_north ()
        janesta.set_schedule ("janesta")

        # Once we want to generate the data context files,
        # just call gamedata::save (1) and copy the .data files
        # to the game's root directory.

    audio_play_background (1)
    gametime_update ()
    map_engine.run()
