#
#  $Id: in_game.py,v 1.2 2001/12/31 18:08:37 adondev Exp $
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

# -- Schedule for the in game music

import adonthell

class in_game:
    def __init__ (self):
        pass
    
    # -- method called everytime a song has finished playing
    #    load song before playing, as the mixer seems to discard it
    #    after it's been played once
    def music_finished (self, song):
        if song == 0:
            adonthell.audio_load_background (1, "audio/at-demo-6.ogg")
            adonthell.audio_play_background (1)
        else:
            adonthell.audio_load_background (0, "audio/at-demo-5.ogg")
            adonthell.audio_play_background (0)
            
