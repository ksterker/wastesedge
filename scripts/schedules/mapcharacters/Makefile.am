pkgdatadir = $(gamedatadir)/scripts/schedules/mapcharacters

pkgdata_DATA = *.pyc

EXTRA_DIST = alek.py erek.py frostbloom.py janesta.py jelom.py bjarn.py \
	keyboard_control.py oliver.py orloth.py sarin.py silverhair.py \
	talan.py tristan.py fellnir.py to_cellar.py lucia.py intro.py \
	extro.py __init__.py

all:
	$(adonthell_binary) -c

*.pyc: *.py

CLEANFILES = *.pyc
