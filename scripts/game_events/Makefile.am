pkgdatadir = $(gamedatadir)/scripts/game_events

pkgdata_DATA = *.pyc

EXTRA_DIST = teleport.py cellar_to_bjarn.py fst_to_silverhair.py \
	character_speak.py open_inn_door.py silverhair_to_fst.py \
	silverhair_to_brn.py brn_to_silverhair.py search_chest.py \
	to_storage.py lft_to_vnd.py vnd_to_lft.py __init__.py \
        speak.py

all:
	$(adonthell_binary) -c

*.pyc: *.py

CLEANFILES = *.pyc
