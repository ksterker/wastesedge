p = characters [name]

if p.submap () == 4:
  events.switch_submap (p, 5, 3, 6, STAND_NORTH)
else:
  events.switch_submap (p, 4, 2, 6, STAND_SOUTH)

