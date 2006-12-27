"""Append module search paths for third-party packages to sys.path.

****************************************************************
* This module is automatically imported during initialization. *
****************************************************************

Minimum site.py for Python embedded in Adonthell.
"""

import sys

def main():
	pass

main()

def _test():
    print "sys.path = ["
    for dir in sys.path:
        print "    %r," % (dir,)
    print "]"

if __name__ == '__main__':
    _test()
