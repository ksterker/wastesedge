#
#  $Id: talk.py,v 1.8 2003/01/27 19:53:40 ksterker Exp $
#
#  (C) Copyright 2001/2003 Kai Sterker <kaisterker@linuxgames.com>
#  Part of the Adonthell Project http://adonthell.linuxgames.com
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License.
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY.
#
#  See the COPYING file for more details
#

# -- mapcharacter Action Event to launch a dialogue with the requester.


import adonthell

class talk:

    def __init__ (self, mapcharacterinstance):
        self.myself = mapcharacterinstance

    def restore_schedule (self, retval, args):
        # -- activate the characters' schedules
        # player isn't event-driven yet
        args[2].set_schedule_active (1)
        if not args[0]: args[2].resume ()
        if not args[1]: args[3].resume ()

        adonthell.gamedata_engine ().set_control_active (1)

    def run (self, requester):
        if requester.get_name() == adonthell.gamedata_player ().get_name():
            # -- get characters' current state
            player_state = requester.is_paused ()
            npc_state = self.myself.is_paused ()
            
            # -- deactivate the schedule of the characters involved
            self.myself.pause ()
            requester.pause ()
            # player isn't event-driven yet
            requester.set_schedule_active (0)

            # -- don't allow access to main menu and stuff
            adonthell.gamedata_engine ().set_control_active (0)

            # -- look into the player's face
            self.myself.look_invert (requester.currentmove ())

            # -- init the dialogue engine
            dlg = adonthell.dialog_screen (self.myself, self.myself.get_dialogue (), 0)

            # -- make sure the engine isn't deleted when we leave the script
            dlg.thisown = 0

            # -- attach the callback
            dlg.py_signal_connect (self.restore_schedule, adonthell.win_event_CLOSE, (player_state, npc_state, requester, self.myself))

            # -- add the dialogue window to the win_manager
            adonthell.win_manager_get_active ().add (dlg)
            adonthell.win_manager_get_active ().set_focus (dlg)

            # -- start the dialogue
            dlg.run ()
