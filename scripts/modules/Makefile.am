pkgdatadir = $(gamedatadir)/scripts/modules

pkgdata_DATA = *.pyc

EXTRA_DIST = console.py main_menu.py events.py character_screen.py intro.py \
	player_text.py

all:
	$(adonthell_binary) -c

*.pyc: *.py

CLEANFILES = *.pyc
