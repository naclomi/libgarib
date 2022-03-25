#!/usr/bin/env python3
import sys

import _prefer_local_implementation
from libgarib.hash import hash_str

if __name__=="__main__":
    for word in sys.argv[1:]:
        print("0x{:08X}".format(hash_str(word)))
