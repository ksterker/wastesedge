pkgdatadir = $(gamedatadir)/scripts/actions

pkgdata_DATA = *.pyc

EXTRA_DIST = talk.py __init__.py

all:
	$(adonthell_binary) -c

*.pyc: *.py

CLEANFILES = *.pyc
