#!/usr/bin/env python
import sys
from os.path import splitext


def db_to_norm(db):
    return 10**(db/10.)


antfilename = sys.argv[1]
basename = splitext(antfilename)[0]

with open(antfilename, 'r') as ant:
    with open(basename + '.az', 'w') as az:
        # azimuth offset (e.g., 0, 120, or 240)
        az.write("0\n")
        # Read the first 360 lines of the file, which correspond to azimuth
        for i in xrange(360):
            az.write("%d\t%0.4f\n" % (i, db_to_norm(float(next(ant)))))
    with open(basename + '.el', 'w') as el:
        # (mechanical downtilt, azimuth of tilt)
        el.write("%0.1f\t%0.1f\n" % (0.0, 0.0))
        # Read the lines for elevations +10 through -90).
        # The rest of the .ant is unused.
        for i, line in enumerate(list(ant)[80:181], -10):
            el.write("%d\t%0.4f\n" % (i, db_to_norm(float(line))))
