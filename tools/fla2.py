#!/usr/bin/env python3
import sys
import argparse

import _prefer_local_implementation
from libgarib.fla2 import compress, decompress

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="compress/decompress FLA2 archives")
    parser.add_argument("file", type=str, nargs="+",
                        help="File to compress/decompress")
    parser.add_argument("--compress", action="store_true",
                        help="Compress the input files")
    parser.add_argument("--pure-python", action="store_true",
                        help="Force use of pure python implementations, rather than compiled C extensions")
    parser.add_argument("--quiet", action="store_true",
                        help="Don't display progress updates")

    args = parser.parse_args()

    if args.compress:
        in_name = ""
        if not args.quiet:
            def compression_progress_callback(percent):
                sys.stdout.write("\rCompressing {:} ({:}%)".format(in_name, percent));
        else:
            compression_progress_callback = None

        for in_name in args.file:
            out_name = in_name + ".fla2"
            with open(in_name, "rb") as f_in:
                with open(out_name, "wb") as f_out:
                    if not args.quiet:
                        compression_progress_callback(0)
                    compress(f_in, f_out, progress_callback=compression_progress_callback, force_pure_python=args.pure_python)
                    if not args.quiet:
                        compression_progress_callback(100)
                        sys.stdout.write("\n")
    else:
        for in_name in args.file:
            out_name = in_name + ".bin"
            with open(in_name, "rb") as f_in:
                with open(out_name, "wb") as f_out:
                    n_bytes = decompress(f_in, f_out)
                    if not args.quiet:
                        print("{:} bytes written".format(n_bytes))
    sys.exit(0)
