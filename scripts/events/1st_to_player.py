p = characters [name]

if p.submap () == 9:
  events.switch_submap (p, 12, 5, 2, STAND_SOUTH)
else:
  events.switch_submap (p, 9, 7, 3, STAND_NORTH)

