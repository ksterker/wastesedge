pkgdatadir = $(gamedatadir)/scripts/modules

pkgdata_DATA = *.pyc

EXTRA_DIST = console.py main_menu.py events.py character_screen.py intro.py

all:
	$(adonthell_binary) -c

*.pyc: *.py

clean:
	rm -f *.pyc
