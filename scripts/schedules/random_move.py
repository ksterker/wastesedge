move=randint(0,30)
if move>=30:
  dir=randint(0,3)

  if dir==0: myself.go_north();
  if dir==1: myself.go_south();
  if dir==2: myself.go_west();
  if dir==3: myself.go_east();
