pkgdatadir = $(gamedatadir)/scripts/schedules/mapviews

pkgdata_DATA = *.pyc

EXTRA_DIST = center_character.py

all:
	$(adonthell_binary) -c

*.pyc: *.py

clean:
	rm -f *.pyc
