#!/usr/bin/env python3
import argparse
import os
import sys
from lxml import etree as ET

import yaml

import _prefer_local_implementation
from libgarib.parsers.glover_level import GloverLevel
from libgarib.levels import landscapeToXML, xmlToLandscape, level_schema_path
from libgarib.ksy import levelKsyToSchema

def assemble(args):
    schema = ET.RelaxNG(file=level_schema_path)
    errors_occurred = False

    for xml_filename in args.level_xml_file:
        tree = ET.parse(xml_filename)
        if not schema.validate(tree.getroot()):
            errors_occurred = True
            print(schema.error_log.filter_from_errors())
            continue

        level_bytes = xmlToLandscape(tree)

        output_filename = os.path.splitext(os.path.basename(xml_filename))[0]
        if not output_filename.endswith(".lev"):
            output_filename += ".lev"
        with open(os.path.join(args.output_dir, output_filename), "wb") as f:
            f.write(level_bytes)

    if errors_occurred:
        sys.exit(1)


def disassemble(args):
    if args.output_dir is not None:
        os.makedirs(args.output_dir, exist_ok=True)
    for level_filename in args.level_binary_file:
        with open(level_filename, "rb") as f:
            raw_level = GloverLevel.from_io(f)
        tree = landscapeToXML(raw_level)

        try:
            ET.indent(tree, space='   ', level=0)
        except AttributeError:
            pass

        if args.output_dir is not None:
            xml_filename = os.path.basename(level_filename) + ".xml"
            output_handle = open(os.path.join(args.output_dir, xml_filename), "wb")
        else:
            output_handle = sys.stdout

        tree.write(output_handle, encoding='utf-8', xml_declaration=True)

        if output_handle is sys.stdout:
            output_handle.write("\n\n")
        else:
            output_handle.close()


def validate(args):
    schema = ET.RelaxNG(file=level_schema_path)
    tree = ET.parse(args.xml_file)
    if not schema.validate(tree.getroot()):
        print(schema.error_log.filter_from_errors())
        sys.exit(1)


def schema(args):
    with open(args.ksy_file, "r") as f:
        ksy = yaml.safe_load(f)
    print(levelKsyToSchema(ksy, args.ksy_file))


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
        "--output-dir", type=str, required=False,
        help="Directory to output XML level data (or print to stdout if omitted)")

    validate_parser = subparsers.add_parser(
        'validate', help='Validate integrity and design rules of XML level data')
    validate_parser.add_argument(
        "xml_file", type=str,
        help="Glover level in XML format")

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
    sys.exit(0)
