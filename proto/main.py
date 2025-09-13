from sys import exit as sysexit
import json
import os
from util.deserializer import bytesToProto

dir = "/path/to/game/assets/PB"
deserialized_dir = "deserialized"
out_dir = "out"

if "path/to/game" in dir:
    print('replace var [dir] in this script with your game path like ".../Games/CoolGame/assets/PB"')
    sysexit()

def switch(field: int):
    v_label= field["field_label"]
    v_type= field["field_type"]

    v_types = {
        1: "double",
        2: "float",
        3: "int64",
        4: "uint64",
        5: "int32",
        6: "fixed64",
        7: "fixed32",
        8: "bool",
        9: "string",
        10: "group",
        11: field["import"][1:], # message
        12: "bytes",
        13: "uint32",
        14: field["import"][1:], # enum
        15: "sfixed32",
        16: "sfixed64",
        17: "sint32",
        18: "sint64"
    }
    if v_type in v_types: t = v_types[v_type]
    else: raise Exception(f'wtf')

    v_labels = {
        1: f'{t}',
        2: f'required {t}',
        3: f'repeated {t}'
    }
    if v_label in v_labels: return v_labels[v_label]
    else: raise Exception("wtf")

def parse_message(m: dict, indent_size: int, current_indent) -> str:
    one = " " * indent_size
    space = current_indent * (one)

    proto = space + f'message {m["message_name"]} {{\n'

    for f in m["field_list"]:
        ftype = switch(f)
        proto += space + one + f'{ftype} {f["snake_case"]} = {f["field_number"]};\n'

    for nm in m["message_list"]:
        proto += parse_message(nm, indent_size, current_indent+1) + "\n"

    for e in m["enum_list"]:
        proto += space + one + f'enum {e["enum_name"]} {{\n'
        for ef in e["enum_field_list"]:
            proto += space + (one*2) + f'{ef["key"]} = {ef["value"]};\n'
        proto += space +  "  }\n"

    proto += space +  "}"

    return proto

def parse_enum(e: dict, indent_size: int, current_indent) -> str:
    one = " " * indent_size
    space = current_indent * (one)

    proto = space + f'enum {e["enum_name"]} {{\n'

    for ef in e["enum_field_list"]:
        proto += space + one + f'{ef["key"]} = {ef["value"]};\n'

    proto += space +  "}"

    return proto

os.makedirs(deserialized_dir, exist_ok=True)
os.makedirs(out_dir, exist_ok=True)

for file in os.listdir(dir):
    path = os.path.join(dir, file)
    if not os.path.isfile(path): continue
    
    with open(path, "rb") as f:
        bin = f.read()

    deserialized = bytesToProto(bin)
    print(deserialized["protobuf"]["name"])

    with open(os.path.join(deserialized_dir, file.replace(".proto", ".json")), "w", encoding="utf-8") as f:
        json.dump(deserialized, f, ensure_ascii=False, indent=4)
    
    out = "// this proto is parsed by SoC proto Tool by c2t-r\n"
    out += f'syntax = "{deserialized["protobuf"]["proto_syntax"]}";\n\n'
    out += f'package {deserialized["protobuf"]["package_name"]};\n'
    if deserialized["protobuf"]["import_protos"]:
        for i in deserialized["protobuf"]["import_protos"]: out += f'\nimport "{i}";'
        out += "\n"

    for p in deserialized["protobuf"]["message_list"]:
        out += "\n" + parse_message(p, 2, 0) + "\n"
    for p in deserialized["protobuf"]["enum_list"]:
        out += "\n" + parse_enum(p, 2, 0) + "\n"
    
    with open(os.path.join(out_dir, file), "w", encoding="utf-8") as f:
        f.write(out)
