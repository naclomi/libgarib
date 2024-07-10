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

def levelKsyToDtd(ksy, ksy_filename):
    type_codes = ksy_scrape_type_codes(ksy)
    valid_children = ksy_scrape_valid_children(ksy)

    root = ET.Element("grammar", xmlns="http://relaxng.org/ns/structure/1.0")

    level = ET.SubElement(ET.SubElement(root, "start"), "element", name="Level", xmlns="http://relaxng.org/ns/structure/1.0")
    ET.SubElement(ET.SubElement(level, "attribute", name="name"), "text")
    ET.SubElement(ET.SubElement(level, "attribute", name="libgarib-version"), "text")
    ET.SubElement(ET.SubElement(level, "attribute", name="data-format-version"), "text")
    cmd_list = ET.SubElement(level, "zeroOrMore")

    for type_name, type_def in ksy["types"].items():
        py_type_name = to_upper_camel(type_name)
        pattern = ET.SubElement(root, "define", name=py_type_name)
        cmd = ET.SubElement(pattern, "element", name=py_type_name)
        for arg_def in type_def["seq"]:
            if isinstance(arg_def.get("type", None), str) and arg_def["type"] not in ksy["types"].keys():
                ET.SubElement(ET.SubElement(cmd, "attribute", name=arg_def["id"]), "text")
        for arg_def in type_def["seq"]:
            if isinstance(arg_def.get("type", None), str) and arg_def["type"] in ksy["types"].keys():
                ET.SubElement(cmd, "ref", name=to_upper_camel(arg_def["type"]))
            elif isinstance(arg_def.get("type", None), dict) and "switch-on" in arg_def["type"]:
                cmd_child_choice = ET.SubElement(cmd, "choice")
                arg_switch = type_codes[type_name][arg_def["id"]]
                for case in arg_switch[1].items():
                    case_group = ET.SubElement(cmd_child_choice, "group")
                    ET.SubElement(ET.SubElement(case_group, "attribute", name=arg_switch[0]), "value").text = str(case[0])
                    ET.SubElement(case_group, "ref", name=to_upper_camel(case[1]))
        if type_name in valid_children:
            cmd_children_list = ET.SubElement(cmd, "zeroOrMore")
            for child in valid_children[type_name]:
                ET.SubElement(cmd_children_list, "ref", name=to_upper_camel(child))
        if len(cmd) == 0:
            ET.SubElement(cmd, "empty")
        ET.SubElement(cmd_list, "ref", name=py_type_name)

    tree = ET.ElementTree(root)
    return ET.tostring(tree, pretty_print=True).decode()

    # indent = "   "
    # dtd = ["<!--\n{indent}WARNING!!\n{indent}THIS FILE IS AUTOGENERATED FROM {ksy_filename}\n{indent}DIRECT EDITS TO IT WILL LIKELY BE LOST\n-->\n".format(**locals())]

    # cmd_list = []
    # for type_name, type_def in ksy["types"].items():
    #     polymorphic = type_def.get("-semantic", {}).get("polymorphic-wrapper-of", None)
    #     if polymorphic is None:
    #         cmd_list.append(to_upper_camel(type_name))

    # cmd_list = " |\n{indent}".format(**locals()).join(cmd_list)
    # version = __version__


    # cmd_declares = {}
    # valid_children = {}
    # polymorphic_types = {}

    # for type_name, type_def in ksy["types"].items():
    #     polymorphic = type_def.get("-semantic", {}).get("polymorphic-wrapper-of", None)
    #     if polymorphic is not None:
    #         polymorphic_types[type_name] = list(set(seq_by_id(type_def["seq"], polymorphic)["type"]["cases"].values()))

    # for type_name, type_def in ksy["types"].items():
    #     declares = type_def.get("-semantic", {}).get("declares", [])
    #     if not isinstance(declares, list):
    #         declares = [declares]
    #     for decl_type in declares:
    #         decl_list = cmd_declares.get(decl_type, [])
    #         decl_list.append(type_name)
    #         cmd_declares[decl_type] = decl_list
    #     if len(declares) > 0:
    #         valid_children[type_name] = []

    # for type_name, type_def in ksy["types"].items():
    #     modifies = type_def.get("-semantic", {}).get("modifies", [])
    #     if not isinstance(modifies, list):
    #         modifies = [modifies]

    #     polymorphic = type_def.get("-semantic", {}).get("polymorphic-wrapper-of", None)
    #     if polymorphic is not None:
    #         child_tags = polymorphic_types[type_name]
    #     else:
    #         child_tags = [type_name]

    #     for mod_type in modifies:
    #         parent_tags = cmd_declares[mod_type]
    #         for parent_tag in parent_tags:
    #             for child_tag in child_tags:
    #                 valid_children[parent_tag].append(child_tag)


    # for type_name, type_def in ksy["types"].items():
    #     polymorphic = type_def.get("-semantic", {}).get("polymorphic-wrapper-of", None)
    #     if polymorphic is not None:
    #         continue
    #     if type_name in valid_children:
    #         type_list = " | \n{indent}".format(**locals()).join(to_upper_camel(name) for name in valid_children[type_name])
    #         type_body = "(\n{indent}{type_list}\n)*".format(**locals())
    #     else:
    #         type_body = "EMPTY"
    #     py_type_name = to_upper_camel(type_name)
    #     dtd.append("<!ELEMENT {py_type_name} {type_body}>".format(**locals()))
    #     for arg_def in type_def["seq"]:
    #         arg_name = arg_def["id"]
    #         dtd.append("{indent}<!ATTLIST {py_type_name} {arg_name} CDATA #REQUIRED>".format(**locals()))
    #     dtd.append("")

    # return "\n".join(dtd)


######
# relax ng example that allows attribute-parametric type trees:
#
#
# 
# <element name="some_element">
#   <choice>
#     <attribute name="has_name">
#       <value>false</value>
#     </attribute>
#     <group>
#       <attribute name="has_name">
#         <value>true</value>
#       </attribute>
#       <element name="name"><text /></element>
#     </group>
#   </choice>
# </element>
#
#  
# also:
#
# <element name="addressBook" xmlns="http://relaxng.org/ns/structure/1.0">
#   <zeroOrMore>
#     <element name="card">
#       <choice>
#         <group>
#             <attribute name="type"><value>n</value></attribute>
#             <element name="name"><text/></element>
#         </group>
#         <group>
#             <attribute name="type"><value>e</value></attribute>
#             <element name="email"><text/></element>
#         </group>
#       </choice>
#     </element>
#   </zeroOrMore>
# </element>
#
# Example:
# <addressBook>
#   <card type="e">
#     <email>js@example.com</email>
#   </card>
#   <card type="n">
#     <name>Fred Bloggs</name>
#   </card>
# </addressBook>