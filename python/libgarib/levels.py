import base64
import hashlib
import enum
import os

from lxml import etree as ET
import kaitaistruct

from . import parsers as parsers 
from .ksy import to_upper_camel
from .linkable import padSize
from .parsers.glover_level import GloverLevel, ksy_hash as glover_level_ksy_hash
from ._version import __version__

level_schema_path = os.path.join(os.path.dirname(parsers.__file__), "glover.lev.rng")

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


def xmlToLandscape(xml_tree):
    group_tags = {}
    for cls in kaitaistruct.KaitaiStruct.__subclasses__():
        semantic = cls.getPrivate("semantic", {})
        if "groups-into" in semantic:
            tag_name = to_upper_camel(semantic["groups-into"])
            group_tags[tag_name] = cls

    type_codes = GloverLevel.Cmd.getSwitches()["params"]["type-to-code"]

    root = xml_tree.getroot()
    level_name = root.attrib["name"]
    level_bytes = [
        b"\x00" * 4,  # Placeholder for file length
        level_name.encode("ASCII") + b"\x00"  # Null-terminated level name
    ]

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
                raw_cmd = GloverLevel.Cmd.getConstructType().build({
                    "type_code": type_codes[wrapper_cmd],
                    "params": {
                        wrapper_cmd.SEQ_FIELDS[0]: prepareConstructDict(grouped_cmd, cmd_iter)
                    }
                })
                level_bytes.append(raw_cmd)
                if grouped_cmd is last_grouped_cmd:
                    break

        else:
            ksy_type = getattr(GloverLevel, cmd.tag)
            raw_cmd = GloverLevel.Cmd.getConstructType().build({
                "type_code": type_codes[ksy_type],
                "params": prepareConstructDict(cmd, cmd_iter)
            })
            level_bytes.append(raw_cmd)

    level_len = sum(len(chunk) for chunk in level_bytes)
    if padSize(level_len) > 0:
        pad = b"\x00" * padSize(level_len)
        level_bytes.append(pad)
        level_len += len(pad)

    # Write level length into the placeholder spot
    level_bytes[0] = GloverLevel.getConstructType().subcons[0].build(level_len)
    level_bytes = b"".join(level_bytes)

    return level_bytes


HEX_CUTOFF = 10000
def kaitaiToAttribs(obj):
    attribs = {}
    for attr_idx, attr_name in enumerate(obj.SEQ_FIELDS):
        construct_type = obj.getConstructType()
        attr_val = None
        raw_attr_val = getattr(obj, attr_name)
        if isinstance(raw_attr_val, str):
            attr_val = raw_attr_val.rstrip('\x00')
        elif isinstance(raw_attr_val, int) and raw_attr_val > HEX_CUTOFF:
            num_hex_digits = construct_type.subcons[attr_idx].sizeof() * 2
            attr_val = "0x{:0{:}X}".format(raw_attr_val, num_hex_digits)
        elif isinstance(raw_attr_val, enum.Enum):
            attr_val = raw_attr_val._name_
        elif isinstance(raw_attr_val, bytes):
            attr_val = base64.b64encode(raw_attr_val).decode("utf8")
        elif type(raw_attr_val) in (int, float):
            attr_val = str(raw_attr_val)
        else:
            raise Exception("Can't disassemble attribute {:} (type {:})".format(attr_name, type(raw_attr_val)))
        attribs[attr_name] = attr_val
    return attribs


def kaitaiSubElement(node, obj):
    tag_name = type(obj).__name__.split(".")[-1]
    attribs = {}
    children = {}
    for attr_idx, attr_name in enumerate(obj.SEQ_FIELDS):
        construct_type = obj.getConstructType()
        raw_attr_val = getattr(obj, attr_name)
        if isinstance(raw_attr_val, str):
            attribs[attr_name] = raw_attr_val.rstrip('\x00')
        elif isinstance(raw_attr_val, int) and raw_attr_val > HEX_CUTOFF:
            num_hex_digits = construct_type.subcons[attr_idx].sizeof() * 2
            attribs[attr_name] = "0x{:0{:}X}".format(raw_attr_val, num_hex_digits)
        elif isinstance(raw_attr_val, enum.Enum):
            attribs[attr_name] = raw_attr_val._name_
        elif isinstance(raw_attr_val, bytes):
            attribs[attr_name] = base64.b64encode(raw_attr_val).decode("utf8")
        elif type(raw_attr_val) in (int, float):
            attribs[attr_name] = str(raw_attr_val)
        elif isinstance(raw_attr_val, kaitaistruct.KaitaiStruct):
            children[attr_name] = raw_attr_val
        else:
            raise Exception("Can't disassemble attribute {:} (type {:})".format(attr_name, type(raw_attr_val)))
    new_node = ET.SubElement(node, tag_name, attrib=attribs)
    for child_name, child_val in children.items():
        kaitaiSubElement(new_node, child_val)
    return new_node


def landscapeToXML(landscape, trim=True):
    root = ET.Element("Level", attrib={
        "name": landscape.name.rstrip('\x00'),
        "libgarib-version": __version__,
        "data-format-version": glover_level_ksy_hash[:7]
    })

    cursors = {
        "root": root
    }
    active_type = None
    for raw_cmd in landscape.body:
        cmd_body = raw_cmd.params
        semantic = cmd_body.getPrivate("semantic", {})

        parent_node = cursors["root"]
        if "modifies" in semantic:
            if type(semantic["modifies"]) is not list:
                semantic["modifies"] = [semantic["modifies"]]
            for applicable_type in semantic["modifies"]:
                if applicable_type == active_type:
                    parent_node = cursors[applicable_type]
                    break
            else:
                active_type = None

        if "groups-into" in semantic:
            group = to_upper_camel(semantic["groups-into"])
            if len(parent_node) == 0 or parent_node[-1].tag != group:
                ET.SubElement(parent_node, group)
            parent_node = parent_node[-1]
            cmd_body = getattr(cmd_body, cmd_body.SEQ_FIELDS[0])

        new_node = kaitaiSubElement(parent_node, cmd_body)

        if "declares" in semantic:
            cursors[semantic["declares"]] = new_node
            active_type = semantic["declares"]

    if trim:
        while root[-1].tag == "Noop":
            root.remove(root[-1])

    return ET.ElementTree(root)
