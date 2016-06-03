#!/usr/bin/env python


# lonlat2maiden -- long/lat to Maidenhead grid calculator not limited to 6 characters
# Copyright       : http://www.fsf.org/copyleft/gpl.html
# Author          : Dan Jacobson -- http://jidanni.org/geo/maidenhead/
# Created On      : Sat Mar 15 03:54:08 2003
# Last Modified On: Fri Nov 28 06:00:24 2003
# Update Count    : 175


import re
import sys
import string
import maidenhead


if len(sys.argv) == 2:  # slob city
    stringlength = string.atoi(sys.argv[1])
    if stringlength < 2 or stringlength % 2 != 0:
        sys.stderr.write('string length requested must be even integer > 0\n')
        sys.exit(87)
else:
    stringlength = 6


while 1:
    line = sys.stdin.readline()
    if not line:
        break
    ll = re.findall(r'([-0-9.]+)\s+([-0-9.]+)', line)

    if ll:
        for leftval, rightval in ll:
            lat = string.atof(leftval)
            lon = string.atof(rightval)
    else:
        sys.stderr.write(sys.argv[0] + ': cannot even get the basic items\n')
        sys.exit(44)

    astring = maidenhead.mh1(lat, lon, stringlength)
    print('{0}'.format(astring))
