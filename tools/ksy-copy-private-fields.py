#!/usr/bin/env python3
import argparse
import os
import re
import sys

import yaml


def to_upper_camel(string):
    words = re.split(r"[\s_-]+", str(string))
    return "".join(word.capitalize() for word in words)

def to_camel(string):
    res = to_upper_camel(string)
    return res[0].lower() + res[1:]


def traverse(node, path, collected_fields):
    if type(node) is dict:
        for k, v in node.items():
            if str(k).startswith("-"):
                path_collection = collected_fields.get(path, {})
                path_collection[to_camel(k)] = v
                collected_fields[path] = path_collection
            else:
                traverse(node[k], "{:}.{:}".format(path, to_upper_camel(k)), collected_fields)
    elif type(node) is list:
        for idx, elem in enumerate(node):
            traverse(elem, "{:}[{:}]".format(path, idx), collected_fields)
    else:
        pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Tool to copy private fields from a ksy file to its Python implementation")
    parser.add_argument(
        "ksy_file", type=str, nargs="+",
        help="Kaitai struct specification")
    parser.add_argument(
        "--compiled-directory", type=str, required=True,
        help="Directory containing Kaitai-compiled Python output")

    args = parser.parse_args()
    for ksy_filename in args.ksy_file:
        fields = {}
        # TODO: scrape private fields outside of the 'types' region, and
        #       include sequences members
        with open(ksy_filename, "r") as f:
            ksy = yaml.safe_load(f)
            traverse(ksy["types"], to_upper_camel(ksy["meta"]["id"]), fields)

        if len(fields) > 0:
            code_suffix = "private_fields = {\n"
            for k, v in fields.items():
                code_suffix += "    '{:}': {:},\n".format(k, v)
            code_suffix += "}\n"

            code_suffix += """
import sys
@classmethod
def getPrivate(cls, field_name, default=None):
    try:
        private_fields = sys.modules[cls.__module__].private_fields
    except AttributeError:
        return default
    return private_fields.get(cls.__qualname__, {}).get(field_name, default)
KaitaiStruct.getPrivate = getPrivate
"""

            compiled_filename = os.path.join(
                args.compiled_directory,
                "{:}.py".format(ksy["meta"]["id"])
            )
            with open(compiled_filename, "a") as f:
                if f.tell() == 0:
                    sys.stderr.write("WARNING: Couldn't find compiled source '{:}'\n".format(compiled_filename))
                    continue
                f.write("\n#############\n")
                f.write("# PATCHED BY {:}\n".format(sys.argv[0]))
                f.write(code_suffix)
                f.write("#############\n")
