from events import switch_submap

p = characters [name]

if p.submap () == 4:
  switch_submap (p, 8, 6, 3 + (p.posy () - 9), STAND_WEST)
else:
  switch_submap (p, 4, 1, 9 + (p.posy () - 3), STAND_EAST)

