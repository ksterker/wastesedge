p = characters [name]

if p.submap () == 9:
  events.switch_submap (p, 11, 4, 3, STAND_WEST)
else:
  events.switch_submap (p, 9, 1, 2, STAND_EAST)


