p = characters [name]

if p.submap () == 14:
  events.switch_submap (p, 15, 1, 5, STAND_EAST)
else:
  events.switch_submap (p, 14, 2, 5, STAND_WEST)

