def run ():
    mychar = characters [name]

    # -- From Common Room to Parlour
    if mychar.submap () == 1:
        events.switch_submap (mychar, 2, 1, 4, STAND_EAST)
    else:
        events.switch_submap (mychar, 1, 13, 4, STAND_WEST)
