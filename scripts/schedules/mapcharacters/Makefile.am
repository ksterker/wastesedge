pkgdatadir = $(gamedatadir)/scripts/schedules/mapcharacters

pkgdata_DATA = *.pyc

EXTRA_DIST = alek.py erek.py frostbloom.py janesta.py jelom.py \
	keyboard_control.py oliver.py orloth.py sarin.py silverhair.py \
	talan.py tristan.py fellnir.py to_cellar.py lucia.py intro.py

all: *.pyc

*.pyc: *.py
	python -c 'import compileall; compileall.compile_dir (".", 0);'

clean:
	rm *.pyc
