def restore_schedule (retval, args):
    # -- activate the character's schedules
    args[0].set_schedule_active (1)
    args[1].set_schedule_active (1)

if requester.get_name()==the_player.get_name():
    # -- deactivate the schedule of the characters involved
    myself.set_schedule_active (0)
    requester.set_schedule_active (0)

    # -- look into the player's face
    myself.look_invert(requester.currentmove())

    # -- init the dialogue engine
    dlg = dialog_engine (myself, myself.get_dialogue (), 0)
    
    # -- make sure the engine isn't deleted when we leave the script
    dlg.thisown = 0

    # -- attach the callback
    dlg.py_signal_connect (restore_schedule, win_event_CLOSE, (requester, myself))

    # -- add the dialogue window to the win_manager
    win_manager_add (dlg)
    win_manager_set_focus (dlg)

    # -- start the dialogue
    dlg.run ()

