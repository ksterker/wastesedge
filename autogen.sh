#!/bin/sh
# First of all clean up the generated crud
rm -f configure config.log config.cache
rm -f config.status aclocal.m4
rm -f `find . -name 'Makefile.in'`
rm -f `find . -name 'Makefile'`

# Regenerate everything

aclocal -I m4 
automake --add-missing --gnu --copy
autoconf 

echo
echo "Now type './configure' to prepare Waste's Edge for compilation."
echo "Afterwards, 'make install' will install it."
echo
