#
#  $Id: in_game.py,v 1.1 2001/12/31 15:33:32 adondev Exp $
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
        self.playing = adonthell.audio_get_current_background ()
        
    def music_finished (self, song):
        if song == 0:
            adonthell.audio_play_background (1)
            self.playing = 1
        else:
            adonthell.audio_play_background (0)
            self.playing = 0
