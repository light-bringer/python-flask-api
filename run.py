import sys
import os

from app import app

def set_paths():
    curfile = os.path.abspath(__file__)
    sys.path.append(os.path.dirname(curfile) + os.path.sep + '..' )
    print sys.path

set_paths()