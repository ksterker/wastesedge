mychar = characters [name]

# Common room to Kitchen
if mychar.submap() == 1:
    events.switch_submap (mychar, 3, 1, 2, STAND_SOUTH)
else:
    events.switch_submap (mychar, 1, 1, 7, STAND_NORTH)

