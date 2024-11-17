#!/usr/bin/env python3
import re
import sys

if __name__=="__main__":
    block_list = sys.argv[1:]
    log_format = re.compile(r"([^:]+)\:\s*([^:]+)\:\s*([^:]+)\:\s*(.+)")
    style_guide_format = re.compile(r"\(see [^#]+#([^)]+)\)")
    for line in sys.stdin.readlines():
        passthru = True
        if (m := log_format.match(line)) is not None:
            file, node, log_type, msg = m.groups()
            if log_type == "warning":
                anchors = style_guide_format.findall(msg)
                for anchor in anchors:
                    if anchor in block_list:
                        passthru = False
        if passthru:
            sys.stdout.write(line)
