def run ():
    mychar = characters [name]

    # -- 1st floor to 2nd floor
    if mychar.submap() == 9:
        events.switch_submap (mychar, 14, 4, 2, STAND_SOUTH)
    else:
        events.switch_submap (mychar, 9, 6, 2, STAND_SOUTH)
