def run ():
    mychar = characters [name]

    # Common room to cellar
    if mychar.submap() == 1:
        events.switch_submap (mychar, 4, 6, 2, STAND_SOUTH)
    else:
        events.switch_submap (mychar, 1, 9, 2, STAND_SOUTH)
