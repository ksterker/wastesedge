pkgdatadir = $(gamedatadir)/scripts/actions

pkgdata_DATA = *.pyc

EXTRA_DIST = talk.py

all: *.pyc

*.pyc: *.py
	python -c 'import compileall; compileall.compile_dir (".", 0);'

clean:
	rm *.pyc
