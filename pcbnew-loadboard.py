#!/gnu/store/rc4kwzk7g7knfpsrd5agvg7n8qyr283p-python-2.7.13/bin/python2
import sys

STOREPATH = '/gnu/store/06jgh4s50jagi91pf4d1wl5i1c3afwsg-kicad-5.0.0-1.e53c3af'
sys.path.append(STOREPATH + '/lib/python2.7/site-packages')

import pcbnew

pcbnew.LoadBoard(sys.argv[1])
