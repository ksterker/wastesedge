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

# -- Map Character Action Event to launch a dialogue with the requester.


import adonthell

class talk:

    def __init__ (self, mapcharacterinstance):
        self.myself = mapcharacterinstance

    def restore_schedule (self, retval, args):
        # -- activate the character's schedules
        args[0].set_schedule_active (1)
        args[1].set_schedule_active (1)

    def run (self, requester):
        if requester.get_name() == adonthell.gamedata_player ().get_name():
            # -- deactivate the schedule of the characters involved
            self.myself.set_schedule_active (0)
            requester.set_schedule_active (0)

            # -- look into the player's face
            self.myself.look_invert(requester.currentmove())

            # -- init the dialogue engine
            dlg = adonthell.dialog_screen (self.myself, self.myself.get_dialogue (), 0)
            
            # -- make sure the engine isn't deleted when we leave the script
            dlg.thisown = 0
                
            # -- attach the callback
            dlg.py_signal_connect (self.restore_schedule, adonthell.win_event_CLOSE, (requester, self.myself))

            # -- add the dialogue window to the win_manager
            adonthell.win_manager_add (dlg)
            adonthell.win_manager_set_focus (dlg)

            # -- start the dialogue
            dlg.run ()
