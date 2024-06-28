#!/usr/bin/env python3
import argparse
import cmd
import io
import json
import os
import sys

import yaml

import _prefer_local_implementation
from libgarib.parsers.glover_level import GloverLevel


def assemble(args):
    pass


import xml.etree.cElementTree as ET
import kaitaistruct
import enum

HEX_CUTOFF = 10000
def kaitaiSubElement(node, obj, skip=None, extra=None):
    tag_name = type(obj).__name__.split(".")[-1]

    attribs = {}
    for attr_name in obj.SEQ_FIELDS:
        if skip is not None and attr_name in skip:
            continue
        attr_val = None
        raw_attr_val = getattr(obj, attr_name)
        if type(raw_attr_val) is str:
            attr_val = raw_attr_val.rstrip('\x00')
        elif type(raw_attr_val) is int and raw_attr_val > HEX_CUTOFF:
            attr_val = "0x{:08X}".format(raw_attr_val)
        elif isinstance(raw_attr_val, enum.Enum):
            attr_val = raw_attr_val._name_
        elif type(raw_attr_val) in (int, float):
            attr_val = str(raw_attr_val)
        else:
            raise Exception("Can't disassemble attribute {:}.{:} (type {:})".format(tag_name, attr_name, type(raw_attr_val)))
        attribs[attr_name] = attr_val
    if extra is not None:
        attribs.update(extra)

    return ET.SubElement(node, tag_name, attrib=attribs)


def disassemble(args):

    root = ET.Element("Level")

    for level_filename in args.level_binary_file:
        with open(level_filename, "rb") as f:
            raw_level = GloverLevel.from_io(f)
        for raw_cmd in raw_level.body:
            cmd_body = raw_cmd.params
            if type(cmd_body) is GloverLevel.PuzzleCond:
                kaitaiSubElement(root, cmd_body.body)
            elif type(cmd_body) is GloverLevel.PuzzleAction:
                kaitaiSubElement(root, cmd_body.body)
            elif type(cmd_body) is GloverLevel.CameoInst:
                kaitaiSubElement(root, cmd_body.body)
            elif (instr_context := {GloverLevel.EnemyNormalInstruction: "normal",
                                    GloverLevel.EnemyConditionalInstruction: "conditional",
                                    GloverLevel.EnemyAttackInstruction: "attack"}.get(
                                        type(cmd_body), None)):
                instr_node = kaitaiSubElement(root, cmd_body.instr, skip=["params"], extra={"context": instr_context})
                kaitaiSubElement(instr_node, cmd_body.instr.params)
            else:
                kaitaiSubElement(root, cmd_body)

        tree = ET.ElementTree(root)
        ET.indent(tree, space='   ', level=0)
        tree.write(sys.stdout, encoding='unicode')


def validate(args):
    pass


def schema(args):
    with open(args.ksy_file, "r") as f:
        ksy = yaml.safe_load(f)
        for type_name, type_def in ksy["types"].items():
            print(type_name)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Tool to work with landscape files from Glover (N64)")
    subparsers = parser.add_subparsers(dest="command", required=True)

    asm_parser = subparsers.add_parser(
        'assemble', help='Build binary lev files from XML level data')
    asm_parser.add_argument(
        "level_xml_file", type=str, nargs="+",
        help="Level file in XML format to assemble into binary lev data")
    asm_parser.add_argument(
        "--output-dir", type=str, default=os.getcwd(),
        help="Directory to output binary level data")

    disasm_parser = subparsers.add_parser(
        'disassemble', help='Extract XML level data from binary Glover level files')
    disasm_parser.add_argument(
        "level_binary_file", type=str, nargs="+",
        help="Binary level file")
    disasm_parser.add_argument(
        "--output-dir", type=str, default=os.getcwd(),
        help="Directory to output XML level data")

    validate_parser = subparsers.add_parser(
        'validate', help='Validate integrity and design rules of a level')
    validate_parser.add_argument(
        "level_or_xml_file", type=str,
        help="Glover level, either in binary format or XML")

    schema_parser = subparsers.add_parser(
        'xml-schema', help='Extract XML schema for level data from Kaitai level format')
    schema_parser.add_argument(
        "ksy_file", type=str,
        help="Kaitai structure definition of Glover level format")

    args = parser.parse_args()
    if args.command == "assemble":
        assemble(args)
    elif args.command == "disassemble":
        disassemble(args)
    elif args.command == "xml-schema":
        schema(args)
    elif args.command == "validate":
        validate(args)
