pkgdatadir = $(gamedatadir)/scripts/modules

pkgdata_DATA = *.pyc

EXTRA_DIST = console.py main_menu.py events.py character_screen.py intro.py

all: *.pyc

*.pyc: *.py
	python -c 'import compileall; compileall.compile_dir (".", 0);'

clean:
	rm *.pyc
