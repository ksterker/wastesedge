def run ():
    mychar = characters [name]

    # Barn to cellar
    if mychar.submap() == 0:
        events.switch_submap (mychar, 4, 12, 2, STAND_SOUTH)
    else:
        events.switch_submap (mychar, 0, 24, 11, STAND_SOUTH)
