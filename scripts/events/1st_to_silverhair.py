p = characters [name]

if p.submap () == 9:
    # -- bjarn's door closed
    free = quests["demo"].get_val("silverhair_free")

    # -- Jelom not convinced of Silverhair's innocence
    if not free and p == the_player:
        # -- we only need that for the dialogue, ...
        p.set_val ("at_silverhairs_door", 1)
        p.stand ()
        p.go_north ()
        characters["Jelom Rasgar"].launch_action (p)
        # -- ... so remove it again afterwards
        p.set_val ("at_silverhairs_door", 0)
    else:
        events.switch_submap (p, 13, 5, 2, STAND_SOUTH)
else:
    events.switch_submap (p, 9, 1, 6, STAND_NORTH)

