SUBDIRS = dialogues events modules schedules actions

pkgdatadir = $(gamedatadir)/scripts

pkgdata_DATA = *.pyc

EXTRA_DIST = init.py

all: *.pyc

*.pyc: *.py
	python -c 'import compileall; compileall.compile_dir (".", 0);'

clean:
	rm *.pyc
