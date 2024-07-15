import base64
import hashlib
import enum
import os

from lxml import etree as ET
import kaitaistruct

from . import ksy
from . import parsers as parsers 
from .parsers.glover_level import GloverLevel, ksy_hash as glover_level_ksy_hash
from ._version import __version__

level_schema_path = os.path.join(os.path.dirname(parsers.__file__), "glover.lev.rng")

def xmlToLandscape(root):
    # TODO
    ...

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


def landscapeToXML(landscape):
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

        if "closes" in semantic:
            skip_tag = False
            if type(semantic["closes"]) is not list:
                semantic["closes"] = [semantic["closes"]]
            for applicable_type in semantic["closes"]:
                if applicable_type == active_type:
                    skip_tag = True
                    break
            if skip_tag is True:
                active_type = None
                continue

        if "groups-into" in semantic:
            group = ksy.to_upper_camel(semantic["groups-into"])
            if len(parent_node) == 0 or parent_node[-1].tag != group:
                ET.SubElement(parent_node, group)
            parent_node = parent_node[-1]

        if "wraps" in semantic:
            cmd_body = getattr(cmd_body, semantic["wraps"])

        new_node = kaitaiSubElement(parent_node, cmd_body)

        if "declares" in semantic:
            cursors[semantic["declares"]] = new_node
            active_type = semantic["declares"]

    return ET.ElementTree(root)
