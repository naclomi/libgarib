#!/usr/bin/env python3
import sys

import _prefer_local_implementation
from libgarib.fla2 import compress, decompress

if __name__ == "__main__":
    if len(sys.argv) == 1:
        sys.stdout.write("usage: {:} [--compress] file ...\n".format(sys.argv[0]))
        sys.stdout.write("compress/decompress FLA2 archives\n")
        sys.exit(1)
    if sys.argv[1] == "--compress":
        for in_name in sys.argv[2:]:
            out_name = in_name + ".fla2"
            with open(in_name, "rb") as f_in:
                with open(out_name, "wb") as f_out:
                    compress(f_in, f_out)
    else:
        for in_name in sys.argv[1:]:
            out_name = in_name + ".bin"
            with open(in_name, "rb") as f_in:
                with open(out_name, "wb") as f_out:
                    n_bytes = decompress(f_in, f_out)
                    print("{:} bytes written".format(n_bytes))
    sys.exit(0)
