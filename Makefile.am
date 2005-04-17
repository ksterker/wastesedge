SUBDIRS = . audio gfx m4 maps pixmaps po scripts 

pkgdatadir = $(gamedatadir)

pkgdata_DATA = gamename.txt character.data mapengine.data quest.data audio.data

EXTRA_DIST = config.rpath mkinstalldirs  config.rpath  $(pkgdata_DATA) PLAYING autogen.sh ABOUT-NLS \
	debian/README.debian debian/adonthell-wastesedge.6 debian/changelog \
        debian/control debian/copyright debian/dirs debian/rules debian/menu \
        debian/compat debian/docs wastesedge.spec.in wastesedge.spec \
	win32/COPYING win32/PLAYING.txt win32/prepare.bat win32/README.txt \
	win32/wastesedge.ico win32/wastesedge.nsi \
	pixmaps/wastesedge_16x16.xpm pixmaps/wastesedge_32x32.xpm \
        osx/Copying.html osx/Install.html osx/Playing.html osx/ReadMe.html \
	osx/adonthell.icns

bin_SCRIPTS = adonthell-wastesedge

CLEANFILES = $(bin_SCRIPTS)

# -- clean game directory before installing
install-exec-local:
	rm -Rf $DESTDIR$(gamedatadir)

adonthell-wastesedge: Makefile
	echo -e "#!/bin/sh\n\n$(adonthell_binary) wastesedge" > adonthell-wastesedge

# -- make sure the data directory gets deleted
uninstall-local:
	rm -rf $DESTDIR$(gamedatadir)


ACLOCAL_AMFLAGS = -I m4
