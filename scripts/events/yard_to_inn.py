from events import switch_submap

# -- From Yard to Common Room
map_engine.get_landmap ().get_mapobject (0).get_animation (0).next_frame ()
switch_submap (characters [name], 1, 13, 7, STAND_NORTH)
