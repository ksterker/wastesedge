from events import switch_submap

p = characters [name]

if p.submap () == 4:
  switch_submap (p, 6, 5, 6 + (p.posy () - 6), STAND_WEST)
else:
  switch_submap (p, 4, 1, 6 + (p.posy () - 6), STAND_EAST)

