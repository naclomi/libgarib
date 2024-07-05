import base64
import enum
import xml.etree.cElementTree as ET

import kaitaistruct

from .parsers.glover_level import GloverLevel

HEX_CUTOFF = 10000
def kaitaiSubElement(node, obj, skip=None, extra=None):
    tag_name = type(obj).__name__.split(".")[-1]

    attribs = {}
    for attr_idx, attr_name in enumerate(obj.SEQ_FIELDS):
        if skip is not None and attr_name in skip:
            continue
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
            raise Exception("Can't disassemble attribute {:}.{:} (type {:})".format(tag_name, attr_name, type(raw_attr_val)))
        attribs[attr_name] = attr_val
    if extra is not None:
        attribs.update(extra)

    return ET.SubElement(node, tag_name, attrib=attribs)


def landscapeToXML(landscape):
    root = ET.Element("Level", attrib={
        "name": landscape.name.rstrip('\x00')
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

        if type(cmd_body) is GloverLevel.PuzzleCond:
            new_node = kaitaiSubElement(parent_node, cmd_body.body)
        elif type(cmd_body) is GloverLevel.PuzzleAction:
            new_node = kaitaiSubElement(parent_node, cmd_body.body)
        elif type(cmd_body) is GloverLevel.CameoInst:
            kaitaiSubElement(parent_node, cmd_body.body)
        elif (instr_context := {GloverLevel.EnemyNormalInstruction: "normal",
                                GloverLevel.EnemyConditionalInstruction: "conditional",
                                GloverLevel.EnemyAttackInstruction: "attack"}.get(
                                    type(cmd_body), None)):
            new_node = kaitaiSubElement(parent_node, cmd_body.instr, skip=["params"], extra={"context": instr_context})
            kaitaiSubElement(new_node, cmd_body.instr.params)
        else:
            new_node = kaitaiSubElement(parent_node, cmd_body)

        if "declares" in semantic:
            cursors[semantic["declares"]] = new_node
            active_type = semantic["declares"]

    return ET.ElementTree(root)
