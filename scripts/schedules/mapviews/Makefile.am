pkgdatadir = $(gamedatadir)/scripts/schedules/mapviews

pkgdata_DATA = *.pyc

EXTRA_DIST = center_character.py

all: *.pyc

*.pyc: *.py
	python -c 'import compileall; compileall.compile_dir (".", 0);'

clean:
	rm *.pyc
