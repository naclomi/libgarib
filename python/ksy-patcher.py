#!/usr/bin/env python3
import argparse
import os
import re
import sys

import yaml


def to_upper_camel(string):
    path_components = str(string).split(".")
    final_path = []
    for component in path_components:
        words = re.split(r"[\s_\-]+", component)
        final_path.append("".join(word.capitalize() for word in words))
    return ".".join(final_path)


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
    names = {}
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
            fields = scrapePrivateFields(ksy["types"], ksy["meta"]["id"])
            names = scrapeNames(ksy["types"], ksy["meta"]["id"])

        code_suffix = "\n"

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