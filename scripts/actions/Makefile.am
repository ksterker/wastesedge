pkgdatadir = $(gamedatadir)/scripts/actions

pkgdata_DATA = *.pyc

EXTRA_DIST = talk.py

all:
	$(adonthell_binary) -c

*.pyc: *.py

clean:
	rm -f *.pyc
