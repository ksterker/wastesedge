#!/bin/sh
# First of all clean up the generated crud
rm -f configure config.log config.cache
rm -f config.status aclocal.m4
mv intl/Makefile.in intl/Makefile.bak
rm -f `find . -name 'Makefile.in'`
mv intl/Makefile.bak intl/Makefile.in
rm -f `find . -name 'Makefile'`

# Regenerate everything

#
# use aclocal v1.6 if available
#
if test "x`which aclocal-1.6`" = "x" ; then
  aclocal -I .
else
  aclocal-1.6 -I .
fi

#
# use Autmake v1.6 if available
#
if test "x`which automake-1.6`" = "x" ; then
  automake --add-missing --gnu --copy
else
  automake-1.6 --add-missing --gnu --copy
fi

autoconf 

echo
echo "Now type './configure' to prepare Adonthell for compilation."
echo "Afterwards, 'make' will build Adonthell."
echo
