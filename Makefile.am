SUBDIRS = . audio gfx intl maps po scripts 

pkgdatadir = $(gamedatadir)

pkgdata_DATA = gamename.txt character.data mapengine.data quest.data audio.data

EXTRA_DIST = config.rpath  $(pkgdata_DATA) PLAYING autogen.sh ABOUT-NLS \
	debian/README.debian debian/adonthell-wastesedge.6 debian/changelog debian/control \
	debian/copyright debian/dirs debian/rules debian/menu wastesedge.spec.in

bin_SCRIPTS = adonthell-wastesedge

CLEANFILES = $(bin_SCRIPTS)

# -- clean game directory before installing
install-exec-local:
	rm -Rf $(gamedatadir)

adonthell-wastesedge: Makefile
	echo -e "#!/bin/sh\n\n$(adonthell_binary) wastesedge" > adonthell-wastesedge

# -- make sure the data directory gets deleted
uninstall-local:
	rm -rf $(gamedatadir)

