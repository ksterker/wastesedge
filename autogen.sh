#!/bin/sh
# First of all clean up the generated crud
rm -f configure config.log config.guess config.sub config.cache
rm -f config.status
rm -f `find . -name 'Makefile.in'`
rm -f `find . -name 'Makefile'`

# Regenerate everything
aclocal -I .
automake --add-missing --gnu
autoconf 

echo
echo "Now type './configure' to prepare Waste's Edge for installation."
echo "Afterwards, 'make install' will install it."
echo
