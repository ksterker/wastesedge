SUBDIRS = mapcharacters mapviews

pkgdatadir = $(gamedatadir)/scripts/schedules

pkgdata_DATA = *.pyc

EXTRA_DIST = control.py

all:
	$(adonthell_binary) -c

*.pyc: *.py

clean:
	rm -f *.pyc
