from events import switch_submap

mychar = characters [name]

# Common room to cellar
if mychar.submap() == 1:
    switch_submap (mychar, 4, 6, 2, STAND_SOUTH)
else:
    switch_submap (mychar, 1, 9, 2, STAND_SOUTH)

