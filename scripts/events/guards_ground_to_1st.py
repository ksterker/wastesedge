def run ():
    mychar = characters [name]

    # -- From Guards ground to 1st floor
    if mychar.submap () == 18:
        events.switch_submap (mychar, 19, 2, 8, STAND_EAST)
    else:
        events.switch_submap (mychar, 18, 2, 8, STAND_EAST)
