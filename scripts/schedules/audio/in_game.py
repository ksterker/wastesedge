#
#  $Id: in_game.py,v 1.3 2002/01/15 22:07:24 adondev Exp $
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
        self.next_song = -1

    # -- method called everytime a song has finished playing
    #    load song before playing, as the mixer seems to discard it
    #    after it's been played once
    def music_finished (self, song):
        # -- if we're in Silverhair's room, play special tune
        if adonthell.gamedata_player ().submap () == 13:
            # -- resume with the song that played before entering
            if self.next_song != 2 and song != 2: self.next_song = song

            adonthell.audio_load_background (2, "audio/at-demo-7.ogg")
            adonthell.audio_play_background (2)

        # -- right after leaving Silverhair's room
        elif self.next_song >= 0:
            adonthell.audio_fade_in_background (self.next_song, 500)
            self.next_song = -1

        # -- otherwise just loop at-demo-5 and at-demo-6
        else:
            if song == 0:
                adonthell.audio_load_background (1, "audio/at-demo-6.ogg")
                adonthell.audio_play_background (1)
            else:
                adonthell.audio_load_background (0, "audio/at-demo-5.ogg")
                adonthell.audio_play_background (0)
            
