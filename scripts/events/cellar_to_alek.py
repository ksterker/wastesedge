def run ():
    p = characters [name]

    if p.submap () == 4:
      events.switch_submap (p, 6, 5, 6 + (p.posy () - 6), STAND_WEST)
    else:
      events.switch_submap (p, 4, 1, 6 + (p.posy () - 6), STAND_EAST)
