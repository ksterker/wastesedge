p=characters[name]
p.set_schedule_active(0)
p.stand()
i=0
while i<60:
  map_engine.mainloop()
#  screen_makesquare(0,0,i*2)
  screen_show()
  gametime_update()
  i=i+(gametime_frames_to_do()*2)
p.jump_to(1,10,11,STAND_NORTH)
i=60
while i>0:
  map_engine.mainloop()
#  screen_makesquare(0,0,i*2)
  screen_show()
  gametime_update()
  i=i-(gametime_frames_to_do()*2)
p.set_schedule_active(1)
