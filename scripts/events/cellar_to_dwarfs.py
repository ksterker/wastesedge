from events import switch_submap

p = characters [name]

if p.submap () == 4:
    # -- bjarn's door closed
    open = quests["demo"].get_val("bjarn_door_open")
    if open == 0 or open == 1:
        if p == the_player:
            characters["Bjarn Fingolson"].launch_action (p)
            p.go_west ()
    else:
        switch_submap (p, 7, 1, 6 + (p.posy () - 6), STAND_EAST)
else:
    switch_submap (p, 4, 9, 6 + (p.posy () - 6), STAND_WEST)

