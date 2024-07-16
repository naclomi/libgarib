#!/usr/bin/env python3
import argparse
import os
import sys
from lxml import etree as ET

import yaml

import _prefer_local_implementation
import libgarib
from libgarib.parsers.glover_level import GloverLevel
from libgarib.levels import landscapeToXML, level_schema_path
from libgarib.ksy import levelKsyToSchema, to_upper_camel


from libgarib.parsers.construct import glover_level as level_writer
def coerce_to_subcon_type(str_value, subcon):
    subcon_cursor = subcon
    try:
        while not (hasattr(subcon_cursor, "fmtstr") or
                   hasattr(subcon_cursor, "encmapping")):
            subcon_cursor = subcon_cursor.subcon
        fmtstr = subcon_cursor.fmtstr
    except AttributeError:
        pass

    if hasattr(subcon_cursor, "fmtstr"):
        datatype = fmtstr[1]
        if datatype.lower() in "xcbhilqn":
            cast_value = int(str_value, 0)
            # TODO: bounds checking based on signedness and size
        elif datatype in "efd":
            cast_value = float(str_value)
        else:
            raise Exception()
    elif hasattr(subcon_cursor, "encmapping"):
        try:
            cast_value = subcon_cursor.encmapping[str_value]
        except KeyError:
            cast_value = int(str_value, 0)
    else:
        # TODO: pad/truncate if fixed size string
        # use field_size = subcon_curson.sizeof()
        cast_value = str_value

    return cast_value


def prepareConstructDict(xml_node, xml_iter):
    ksy_type = getattr(GloverLevel, xml_node.tag)
    construct_type = ksy_type.getConstructType()
    switches = ksy_type.getSwitches()
    switch_fields = {v["field"]:k for k,v in switches.items()}

    complex_param_types = {}
    cmd_params = {}

    for subcon in construct_type.subcons:
        if (subcon.name not in xml_node.attrib and
                subcon.name not in switch_fields):
            # Order of XML node's child tags is implicitly the order
            # they appear in the binary command's format
            next_tag = next(xml_iter)
            cmd_params[subcon.name] = prepareConstructDict(next_tag, xml_iter)
            complex_param_types[subcon.name] = getattr(GloverLevel, next_tag.tag)

    for subcon in construct_type.subcons:
        if subcon.name in cmd_params:
            continue
        elif subcon.name in xml_node.attrib:
            cmd_params[subcon.name] = coerce_to_subcon_type(xml_node.attrib[subcon.name], subcon)

    for subcon in construct_type.subcons:
        if subcon.name not in cmd_params and subcon.name in switch_fields:
            switch = switches[switch_fields[subcon.name]]
            cmd_params[subcon.name] = switch["type-to-code"][complex_param_types[switch_fields[subcon.name]]]

    return cmd_params

import kaitaistruct
def assemble(args):
    schema = ET.RelaxNG(file=level_schema_path)
    errors_occurred = False

    group_tags = {}
    for cls in kaitaistruct.KaitaiStruct.__subclasses__():
        semantic = cls.getPrivate("semantic", {})
        if "groups-into" in semantic:
            tag_name = to_upper_camel(semantic["groups-into"])
            group_tags[tag_name] = cls

    for xml_filename in args.level_xml_file:
        tree = ET.parse(xml_filename)
        if not schema.validate(tree.getroot()):
            errors_occurred = True
            print(schema.error_log.filter_from_errors())
            continue

        level_bytes = []

        type_codes = GloverLevel.Cmd.getSwitches()["params"]["type-to-code"]
        root = tree.getroot()
        level_name = root.attrib["name"]
        cmd_iter = root.iter(tag=ET.Element)

        while True:
            try:
                cmd = next(cmd_iter)
            except StopIteration:
                break
            if cmd.tag == "Level":
                continue

            if cmd.tag in group_tags:
                wrapper_cmd = group_tags[cmd.tag]
                last_grouped_cmd = cmd[-1]
                while True:
                    grouped_cmd = next(cmd_iter)
                    raw_cmd = wrapper_cmd.getConstructType().build({
                        wrapper_cmd.SEQ_FIELDS[0]: prepareConstructDict(grouped_cmd, cmd_iter)
                    })
                    level_bytes.append(raw_cmd)
                    if grouped_cmd is last_grouped_cmd:
                        break

            else:
                ksy_type = getattr(GloverLevel, cmd.tag)
                raw_cmd = level_writer.glover_level__cmd.build({
                    "type_code": type_codes[ksy_type],
                    "params": prepareConstructDict(cmd, cmd_iter)
                })
                level_bytes.append(raw_cmd)

        # TODO: figure out padding:
        level_header = GloverLevel.getConstructType().build({
            "name": level_name,
            "length": sum(len(chunk) for chunk in level_bytes) + 4 + len(level_name) + 1,
            "body": {}
        })

        level_bytes.insert(0, level_header)

        level_bytes = b"".join(level_bytes)

        print(level_bytes)

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