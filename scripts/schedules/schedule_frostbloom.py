move=randint(0,70)
if move>=70:
  dir=randint(0,3)

  if dir==0:
    if myself.posy()<=20: myself.go_south()
    else: myself.go_north()
  if dir==1: 
    if myself.posy()>=22: myself.go_north()
    else: myself.go_south()
  if dir==2: 
    if myself.posx()<=23: myself.go_east()
    else: myself.go_west()
  if dir==3: 
    if myself.posx()>=26: myself.go_west()
    else: myself.go_east()
