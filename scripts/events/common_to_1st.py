from events import switch_submap

mychar = characters [name]

# Common room to 1st floor
if mychar.submap() == 1:
    switch_submap (mychar, 9, 8, 2, STAND_SOUTH)
else:
    switch_submap (mychar, 1, 12, 2, STAND_SOUTH)

