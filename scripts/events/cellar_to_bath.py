p = characters [name]
p.set_schedule_active (0)
p.stand ()

if p == the_player:
  i = 0
  while i < 60:
    map_engine.mainloop ()
    screen_transition (i * 2)
    screen_show ()
    gametime_update ()
    i = i + (gametime_frames_to_do () * 2)

if p.submap () == 4:
  p.jump_to (5, 3, 6, STAND_NORTH)
else:
  p.jump_to (4, 2, 6, STAND_SOUTH)

if p == the_player:
  i=60
  while i > 0:
    map_engine.mainloop ()
    screen_transition (i * 2)
    screen_show ()
    gametime_update ()
    i = i - (gametime_frames_to_do () * 2)
    
p.set_schedule_active (1)
