from events import switch_submap

mychar = characters [name]

# -- From Yard to Kitchen
if mychar.submap () == 0:
    switch_submap (mychar, 3, 6, 3, STAND_WEST)
else:
    switch_submap (mychar, 0, 12, 14, STAND_EAST)

