SUBDIRS = audio gfx maps scripts 

pkgdatadir = $(gamedatadir)

pkgdata_DATA = gamename.txt character.data mapengine.data quest.data

EXTRA_DIST = $(pkgdata_DATA)

bin_SCRIPTS = adonthell-wastesedge


adonthell-wastesedge:
	echo -e "#!/bin/sh\n\n$(adonthell_binary) wastesedge" > adonthell-wastesedge

## Be sure the data directory gets deleted
uninstall-local:
	rm -Rf $(gamedatadir)
