pkgdatadir = $(gamedatadir)/scripts/events

pkgdata_DATA = *.pyc

EXTRA_DIST = teleport.py cellar_to_bjarn.py fst_to_silverhair.py \
	character_speak.py open_inn_door.py

all: *.pyc

*.pyc: *.py
	python -c 'import compileall; compileall.compile_dir (".", 0);'

clean:
	rm *.pyc
