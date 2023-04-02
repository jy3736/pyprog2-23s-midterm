#! /usr/bin/env python

import os
import argparse

CMD = "python"
DIR_HW = "src"
DIR_CHECK = "../../lib/tests"
EXT_PY = "py"
EXT_PYC = "pyc"
THIS_DIR = os.path.basename(os.getcwd())

def main(ext):
    os.system(f"{CMD} {DIR_CHECK}/chk_{THIS_DIR}.{ext}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--py', help='use .py instead of .pyc', action='store_true')
    args = parser.parse_args()
    
    if args.py:
        ext = EXT_PY
    else:
        ext = EXT_PYC
        
    main(ext)
