def run ():
    p = characters [name]

    if p.submap () == 14:
      events.switch_submap (p, 17, 6, 2, STAND_SOUTH)
    else:
      events.switch_submap (p, 14, 1, 7, STAND_NORTH)

