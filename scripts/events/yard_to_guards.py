mychar = characters [name]

# -- From Yard to Guards house
if mychar.submap () == 0:
    events.switch_submap (mychar, 18, 7, 3, STAND_WEST)
else:
    events.switch_submap (mychar, 0, 13, 23, STAND_EAST)
