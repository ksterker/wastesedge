def run ():
    p = characters [name]

    if p.submap () == 14:
      events.switch_submap (p, 16, 6, 5, STAND_WEST)
    else:
      events.switch_submap (p, 14, 1, 5, STAND_EAST)
