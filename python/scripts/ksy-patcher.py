#!/usr/bin/env python3
import argparse
import os
import re
import sys
import hashlib

import yaml

from libgarib.ksy import to_upper_camel, ksy_scrape_type_codes

def crawlYaml(node, path, dict_callback=None, list_callback=None, scalar_callback=None):
    if type(node) is dict:
        for k, v in node.items():
            if dict_callback is not None:
                if dict_callback[0](node, path, k, v, *dict_callback[1:]) is False:
                    continue
            crawlYaml(node[k], "{:}.{:}".format(path, k), dict_callback, list_callback, scalar_callback)
    elif type(node) is list:
        for idx, elem in enumerate(node):
            if list_callback is not None:
                if list_callback[0](node, path, idx, elem, *list_callback[1:]) is False:
                    continue
            crawlYaml(elem, "{:}[{:}]".format(path, idx), dict_callback, list_callback, scalar_callback)
    else:
        if scalar_callback is not None:
            scalar_callback[0](node, path, idx, elem, *scalar_callback[1:])


def _scrapePrivateFieldsCallback(node, path, k, v, fields):
    if str(k).startswith("-"):
        path_collection = fields.get(path, {})
        path_collection[k[1:]] = v
        fields[path] = path_collection
        return False
    return True
def scrapePrivateFields(node, path):
    fields = {}
    crawlYaml(node, path, dict_callback=(_scrapePrivateFieldsCallback, fields))
    return fields


def _scrapeNamesCallback(node, path, k, v, names):
    if len(path.split(".")) <= 1:
        k_path = "{:}.{:}".format(path, k)
        names[to_upper_camel(k_path)] = k_path
        return True
    else:
        return False
def scrapeNames(node, path):
    names = {
        to_upper_camel(path): path
    }
    crawlYaml(node, path, dict_callback=(_scrapeNamesCallback, names))
    return names


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
        # TODO: scrape private fields outside of the 'types' region, and
        #       include sequences members
        with open(ksy_filename, "r") as f:
            ksy = yaml.safe_load(f)
            f.seek(0)
            ksy_sha1 = hashlib.sha1(f.read().encode("utf-8"))

        fields = scrapePrivateFields(ksy["types"], ksy["meta"]["id"])
        names = scrapeNames(ksy["types"], ksy["meta"]["id"])
        type_codes = ksy_scrape_type_codes(ksy)

        code_suffix = "\n"


        code_suffix += "switch_fields = {\n"
        for type_name, type_def in type_codes.items():
            code_suffix += "    '{:}': {{\n".format(to_upper_camel(ksy["meta"]["id"]) + "." + to_upper_camel(type_name))
            for attr_name, attr_def in type_def.items():
                code_suffix += "        '{:}': {{\n".format(attr_name, "foo")
                code_suffix += "            'field': '{:}',\n".format(attr_def[0])
                code_suffix += "            'code-to-type': {\n"
                for code, val in attr_def[1].items():
                    if code == "_":
                        case_literal = None
                    elif isinstance(code, int):
                        case_literal = hex(code)
                    else:
                        case_literal = code
                    code_suffix += "                {:}: {:},\n".format(case_literal, to_upper_camel(ksy["meta"]["id"]) + "." + to_upper_camel(val))
                code_suffix += "            },\n"
                code_suffix += "            'type-to-code': {\n"
                for val, code in attr_def[2].items():
                    if code == "_":
                        case_literal = None
                    elif isinstance(code, int):
                        case_literal = hex(code)
                    else:
                        case_literal = code
                    code_suffix += "                {:}: {:},\n".format(to_upper_camel(ksy["meta"]["id"]) + "." + to_upper_camel(val), case_literal)
                code_suffix += "            }\n"
                code_suffix += "        },\n"
            code_suffix += "    },\n"
        code_suffix += "}\n"

        code_suffix += "original_names = {\n"
        for k, v in names.items():
            code_suffix += "    '{:}': '{:}',\n".format(k, v)
        code_suffix += "}\n"

        code_suffix += "private_fields = {\n"
        for k, v in fields.items():
            code_suffix += "    '{:}': {:},\n".format(to_upper_camel(k), v)
        code_suffix += "}\n"

        code_suffix += r"""
import sys
import importlib

_module_cache = {}
_cls_cache = {}
@classmethod
def getConstructType(cls):
    global _module_cache
    global _cls_cache
    if cls.__qualname__ not in _cls_cache:
        if __name__ not in _module_cache:
            module_tokens = __name__.split(".")
            package_name = ".".join(module_tokens[:-1])
            module_name = module_tokens[-1]
            _module_cache[__name__] = importlib.import_module(".construct.{:}".format(module_name), package_name)
        construct_mod = _module_cache[__name__]
        type_name = cls.getOriginalName().replace(".", "__")
        _cls_cache[cls.__qualname__] = getattr(construct_mod, type_name)
    return _cls_cache[cls.__qualname__]
KaitaiStruct.getConstructType = getConstructType

@classmethod
def getOriginalName(cls):
    original_names = sys.modules[cls.__module__].original_names
    return original_names[cls.__qualname__]
KaitaiStruct.getOriginalName = getOriginalName

@classmethod
def getPrivate(cls, field_name, default=None):
    try:
        private_fields = sys.modules[cls.__module__].private_fields
    except AttributeError:
        return default
    return private_fields.get(cls.__qualname__, {}).get(field_name, default)
KaitaiStruct.getPrivate = getPrivate

@classmethod
def getSwitches(cls):
    try:
        switch_fields = sys.modules[cls.__module__].switch_fields
    except AttributeError:
        return None
    return switch_fields.get(cls.__qualname__, {})
KaitaiStruct.getSwitches = getSwitches

"""

        code_suffix += "ksy_hash = '{:}'\n".format(ksy_sha1.hexdigest())

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
