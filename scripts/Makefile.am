SUBDIRS = dialogues events modules schedules actions

pkgdatadir = $(gamedatadir)/scripts

pkgdata_DATA = *.pyc

EXTRA_DIST = init.py

all:
	$(adonthell_binary) -c

*.pyc: *.py

CLEANFILES = *.pyc
