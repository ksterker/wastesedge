from events import switch_submap

mychar = characters [name]

# Barn to cellar
if mychar.submap() == 0:
    switch_submap (mychar, 4, 12, 2, STAND_SOUTH)
else:
    switch_submap (mychar, 0, 24, 11, STAND_SOUTH)

