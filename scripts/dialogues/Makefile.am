pkgdatadir = $(gamedatadir)/scripts/dialogues

pkgdata_DATA = *.pyc

EXTRA_DIST = orloth_start.py lucia_start.py sarin_start.py \
    janesta_start.py erek_start.py oliver_start.py bjarn_start.py \
    frostbloom_start.py talan_start.py alek_start.py jelom_start.py \
    tristan_start.py jelom_2nd.py demo_intro_1.py

all:
	$(adonthell_binary) -c

*.pyc: *.py

clean:
	rm -f *.pyc
