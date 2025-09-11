import json

path = "db_lang.json"

def bytesLen(b: bytes):
    return len(b).to_bytes(2, "little")

with open(path, "r", encoding="utf-8") as f:
    db_lang = json.load(f)

length = len(db_lang)

binary = b''
n = 1
for d in db_lang:
    type_value = d["type"].encode()
    type_length = bytesLen(type_value)
    binary += type_length + type_value

    key_value = d["key"].encode()
    key_length = bytesLen(key_value)
    binary += key_length + key_value

    number = bytes.fromhex(d["number"])
    binary += number

    value_value = d["value"].encode()
    value_length = bytesLen(key_value)
    binary += value_length + value_value

    print(f'[{int((n/length)*100*100)/100}%] ({n}/{length})', end="\r")
    n += 1

print("\ndumping...")
with open("db_lang_encoded", "wb") as f:
    f.write(binary)

print("done")