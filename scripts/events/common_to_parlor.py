from events import switch_submap

mychar = characters [name]

# -- From Common Room to Parlour
if mychar.submap () == 1:
    switch_submap (mychar, 2, 1, 4, STAND_EAST)
else:
    switch_submap (mychar, 1, 13, 4, STAND_WEST)

