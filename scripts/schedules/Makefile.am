SUBDIRS = audio mapcharacters mapviews

pkgdatadir = $(gamedatadir)/scripts/schedules

pkgdata_DATA = *.pyc

EXTRA_DIST = control.py __init__.py

*.pyc: *.py
	$(adonthell_binary) -c

CLEANFILES = *.pyc
