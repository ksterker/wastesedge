pkgdatadir = $(gamedatadir)/scripts/schedules/audio

pkgdata_DATA = *.pyc

EXTRA_DIST = in_game.py

all:
	$(adonthell_binary) -c

*.pyc: *.py

CLEANFILES = *.pyc
