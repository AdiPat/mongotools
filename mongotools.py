#
# mongotools: Database Migration Utility
# Author: Aditya Patange
#

import sys
from importdb import import_all
from exportdb import export_all
from config import CONFIG

if len(sys.argv) < 2:
    print("USAGE: python mongotools.py option[import,export]")
    sys.exit(0)

option = sys.argv[1]

if option == 'import':
    print("IMPORTING FILES FROM", CONFIG['DATA_PATH']+"/import")
    import_all()
elif option == 'export':
    print("EXPORTING FILES TO", CONFIG['DATA_PATH']+"/export")
    export_all()
