mychar = characters [name]

# Close the inn door.
if mychar.submap () == 0:
    map_engine.get_landmap ().get_mapobject (0).get_animation (0).next_frame ()

# -- From Common Room to Yard
if mychar.submap () == 1:
    events.switch_submap (mychar, 0, 18, 14, STAND_SOUTH)
else:
    events.switch_submap (mychar, 1, 13, 7, STAND_NORTH)
