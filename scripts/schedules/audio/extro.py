#
#  $Id: extro.py,v 1.1 2002/01/27 19:04:21 adondev Exp $
#
#  (C) Copyright 2002 Kai Sterker <kaisterker@linuxgames.com>
#  Part of the Adonthell Project http://adonthell.linuxgames.com
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License.
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY.
#
#  See the COPYING file for more details
#

# -- Schedule for the in game music

import adonthell

class extro:
    def __init__ (self):
        adonthell.gamedata_get_quest ("demo").set_val ("music", 0)

    # -- method called everytime a song has finished playing
    #    load song before playing, as the mixer seems to discard it
    #    after it's been played once
    def music_finished (self, song):
        music = adonthell.gamedata_get_quest ("demo").get_val ("music")
        
        if music == 0:
            adonthell.audio_load_background (0, "audio/at-demo-9.ogg")
            adonthell.audio_play_background (0)
            
        else:
            adonthell.audio_load_background (2, "audio/at-demo-2.ogg")
            adonthell.audio_play_background (2)
