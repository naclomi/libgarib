#!/usr/bin/env python3
import argparse
import os
import sys
from lxml import etree as ET

import yaml

import _prefer_local_implementation
import libgarib
from libgarib.parsers.glover_level import GloverLevel
from libgarib.levels import landscapeToXML, level_dtd_path
from libgarib.ksy import levelKsyToDtd


from libgarib.parsers.construct import glover_level as level_writer
def assemble(args):
    dtd = ET.DTD(file=level_dtd_path)
    errors_occurred = False
    for xml_filename in args.level_xml_file:
        tree = ET.parse(xml_filename)
        if not dtd.validate(tree.getroot()):
            errors_occurred = True
            print(dtd.error_log.filter_from_errors())
            continue

        root = tree.getroot()
        level_name = root.attrib["name"]
        for cmd in root:
            ksy_type = getattr(GloverLevel, cmd.tag)
            construct_type = ksy_type.getConstructType()
            raw_attrib = {}
            # for attrib in cmd.attrib:
            #     # TODO                
            raw_params = construct_type.build(raw_attrib)
            raw_cmd = level_writer.glover_level__cmd.build({
                "params": raw_params
            })
            print(cmd, raw_cmd)
        # breakpoint()


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

        doctype = "<!DOCTYPE level SYSTEM \"glover.lev.dtd\">"

        tree.write(output_handle, encoding='utf-8', xml_declaration=True, doctype=doctype)

        if output_handle is sys.stdout:
            output_handle.write("\n\n")
        else:
            output_handle.close()

def validate(args):
    dtd = ET.DTD(file=level_dtd_path)
    tree = ET.parse(args.xml_file)
    if not dtd.validate(tree.getroot()):
        print(dtd.error_log.filter_from_errors())
        sys.exit(1)

def schema(args):
    with open(args.ksy_file, "r") as f:
        ksy = yaml.safe_load(f)
    print(levelKsyToDtd(ksy, args.ksy_file))

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
        'xml-dtd', help='Extract XML DTD for level data from Kaitai level format')
    schema_parser.add_argument(
        "ksy_file", type=str,
        help="Kaitai structure definition of Glover level format")

    args = parser.parse_args()
    if args.command == "assemble":
        assemble(args)
    elif args.command == "disassemble":
        disassemble(args)
    elif args.command == "xml-dtd":
        schema(args)
    elif args.command == "validate":
        validate(args)
    sys.exit(0)