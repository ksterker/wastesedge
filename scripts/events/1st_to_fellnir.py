def run ():
    p = characters [name]

    if p.submap () == 9:
        events.switch_submap (p, 10, 1, 3, STAND_EAST)
    else:
        events.switch_submap (p, 9, 8, 2, STAND_WEST)

