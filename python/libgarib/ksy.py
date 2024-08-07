import re
import warnings

from lxml import etree as ET

from ._version import __version__

def to_upper_camel(string):
    path_components = str(string).split(".")
    final_path = []
    for component in path_components:
        words = re.split(r"[\s_\-]+", component)
        final_path.append("".join(word.capitalize() for word in words))
    return ".".join(final_path)

def seq_by_id(seq, key):
    for elem in seq:
        if elem["id"] == key:
            return elem
    else:
        raise KeyError(key)

def ksy_scrape_type_codes(ksy):
    codes = {}
    for type_name, type_def in ksy["types"].items():
        for attr in type_def["seq"]:
            attr_type = attr.get("type", None)
            if isinstance(attr_type, dict) and "switch-on" in attr_type:
                switch_on = attr_type["switch-on"]
                cases = attr_type["cases"]
                inverse = {}
                for k, v in cases.items():
                    if v in inverse:
                        # TODO: make this fatal once the level KSY has
                        #       stabilized:
                        warnings.warn("Ambiguous type {:}".format(type_name))
                        if not isinstance(inverse[v], list):
                            inverse[v] = [inverse[v]]
                        inverse[v].append(k)
                    else:
                        inverse[v] = k
                if type_name not in codes:
                    codes[type_name] = {}
                codes[type_name][attr["id"]] = (switch_on, cases, inverse)
    return codes

def ksy_scrape_valid_children(ksy):
    cmd_declares = {}
    valid_children = {}

    for type_name, type_def in ksy["types"].items():
        declares = type_def.get("-semantic", {}).get("declares", [])
        if not isinstance(declares, list):
            declares = [declares]
        for decl_type in declares:
            decl_list = cmd_declares.get(decl_type, [])
            decl_list.append(type_name)
            cmd_declares[decl_type] = decl_list
        if len(declares) > 0:
            valid_children[type_name] = []

    for type_name, type_def in ksy["types"].items():
        modifies = type_def.get("-semantic", {}).get("modifies", [])
        if not isinstance(modifies, list):
            modifies = [modifies]
        child_tags = [type_name]
        for mod_type in modifies:
            parent_tags = cmd_declares[mod_type]
            for parent_tag in parent_tags:
                for child_tag in child_tags:
                    valid_children[parent_tag].append(child_tag)

    return valid_children

def ksy_scrape_groupables(ksy):
    groupables = {}
    for type_name, type_def in ksy["types"].items():
        semantic = type_def.get("-semantic", {})
        if "groups-into" in semantic:
            groupables[type_name] = semantic["groups-into"]
    return groupables

def levelKsyToSchema(ksy, ksy_filename):
    type_codes = ksy_scrape_type_codes(ksy)
    valid_children = ksy_scrape_valid_children(ksy)
    top_level_commands = set(type_codes["cmd"]["params"][1].values())
    group_commands = ksy_scrape_groupables(ksy)

    root = ET.Element("grammar",
        xmlns="http://relaxng.org/ns/structure/1.0",
        datatypeLibrary="http://www.w3.org/2001/XMLSchema-datatypes")
    root.addprevious(ET.Comment("\n   WARNING!!\n   THIS FILE IS AUTOGENERATED FROM {ksy_filename}\n   DIRECT EDITS TO IT WILL LIKELY BE LOST\n".format(**locals())))

    level = ET.SubElement(ET.SubElement(root, "start"), "element", name="Level", xmlns="http://relaxng.org/ns/structure/1.0")
    ET.SubElement(ET.SubElement(level, "attribute", name="name"), "text")
    ET.SubElement(ET.SubElement(level, "attribute", name="libgarib-version"), "text")
    ET.SubElement(ET.SubElement(level, "attribute", name="data-format-version"), "text")
    cmd_list = ET.SubElement(level, "interleave")

    def append_reference(xml_parent, ref_type):
        ET.SubElement(ET.SubElement(xml_parent, "zeroOrMore"), "ref", name=to_upper_camel(ref_type))

    def process_type(type_name, type_def):
        semantic = type_def.get("-semantic", {})
        if type_name in group_commands:
            group_pattern = ET.SubElement(root, "define", name=to_upper_camel(group_commands[type_name]))
            group_cmd = ET.SubElement(group_pattern, "element", name=to_upper_camel(group_commands[type_name]))
            group_cmd_children_list = ET.SubElement(group_cmd, "interleave")
            if len(type_def["seq"]) > 1:
                raise Exception("Non-trivial groupable tag {:}".format(type_name))
            wrap_type = type_def["seq"][0]["type"]
            append_reference(group_cmd_children_list, wrap_type)
            append_reference(cmd_list, group_commands[type_name])
        elif type_name == "cmd":
            pass
        else:
            py_type_name = to_upper_camel(type_name)
            pattern = ET.SubElement(root, "define", name=py_type_name)
            cmd = ET.SubElement(pattern, "element", name=py_type_name)
            for arg_def in type_def["seq"]:
                if not isinstance(arg_def.get("type", None), str):
                    continue
                if arg_def["type"] in ksy["types"].keys():
                    continue
                if type_name in type_codes:
                    if any(arg_def["id"] == field[0] for field in type_codes[type_name].values()):
                        continue
                ET.SubElement(ET.SubElement(cmd, "attribute", name=arg_def["id"]), "text")
            for arg_def in type_def["seq"]:
                if isinstance(arg_def.get("type", None), str) and arg_def["type"] in ksy["types"].keys():
                    append_reference(cmd, arg_def["type"])
                elif isinstance(arg_def.get("type", None), dict) and "switch-on" in arg_def["type"]:
                    cmd_child_choice = ET.SubElement(cmd, "choice")
                    arg_switch = type_codes[type_name][arg_def["id"]]
                    for case in arg_switch[1].items():
                        case_group = ET.SubElement(cmd_child_choice, "group")
                        if case[0] == "_":
                            case_group.append(ET.Comment("Default case (only for types not listed above!)"))
                            ET.SubElement(ET.SubElement(case_group, "attribute", name=arg_switch[0]), "text")
                        else:
                            full_hex = "{:X}".format(case[0])
                            regex_hex = "0x0*"
                            for char in full_hex:
                                if char.isalpha():
                                    regex_hex = regex_hex + "[{:}{:}]".format(char.upper(), char.lower())
                                else:
                                    regex_hex = regex_hex + char
                            case_pattern= str(case[0]) + "|" + regex_hex
                            case_group.append(ET.Comment("Case 0x{:X}".format(case[0])))
                            ET.SubElement(ET.SubElement(ET.SubElement(case_group, "attribute", name=arg_switch[0]), "data", type="string"), "param", name="pattern").text = case_pattern
                        if case[1] in group_commands:
                            case_value = group_commands[case[1]]
                        else:
                            case_value = case[1]
                        ET.SubElement(case_group, "ref", name=to_upper_camel(case_value))
            if type_name in valid_children:
                cmd_children_list = ET.SubElement(cmd, "interleave")
                for child in valid_children[type_name]:
                    if child in group_commands:
                        child = group_commands[child]
                    append_reference(cmd_children_list, child)
            if len(cmd) == 0:
                ET.SubElement(cmd, "empty")
            if type_name in top_level_commands:
                append_reference(cmd_list, type_name)


    for ksy_type in ksy["types"].items():
        process_type(*ksy_type)

    tree = ET.ElementTree(root)
    return ET.tostring(tree, pretty_print=True).decode()
