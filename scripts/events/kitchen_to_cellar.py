from events import switch_submap

mychar = characters [name]

# Kitchen to cellar
if mychar.submap() == 3:
    switch_submap (mychar, 4, 3, 12, STAND_NORTH)
else:
    switch_submap (mychar, 3, 6, 5, STAND_NORTH)

