p = characters [name]

if p.submap () == 9:
  events.switch_submap (p, 13, 5, 2, STAND_SOUTH)
else:
  events.switch_submap (p, 9, 1, 6, STAND_NORTH)

