pkgdatadir = $(gamedatadir)/scripts/schedules/mapviews

pkgdata_DATA = *.pyc

EXTRA_DIST = center_character.py __init__.py

all:
	$(adonthell_binary) -c

*.pyc: *.py

CLEANFILES = *.pyc
