from events import switch_submap

mychar = characters [name]

# Common room to Kitchen
if mychar.submap() == 1:
    switch_submap (mychar, 3, 1, 2, STAND_SOUTH)
else:
    switch_submap (mychar, 1, 1, 7, STAND_NORTH)

