import json
from io import BufferedReader

path = "db_lang"

def readOneByteString(f: BufferedReader):
    byte_length = f.read(2)
    length = int.from_bytes(byte_length, byteorder='little')
    string = f.read(length)
    return string.decode(encoding="utf-8")

print("parsing...")
db_lang = []
with open(path, "rb") as f:

    size = f.seek(0, 2)
    f.seek(0)

    while not f.tell() == size:
        entry = readOneByteString(f)
        #print(entry)

        key = readOneByteString(f)
        #print(key)

        address = f.read(4).hex()
        
        value = readOneByteString(f)
        #print(value)

        db_lang.append({
            "type": entry,
            "number": address,
            "key": key,
            "value": value
        })

        print(entry)

print("dumping...")
with open("db_lang.json", "w", encoding="utf-8") as f:
    json.dump(db_lang, f, indent=4, ensure_ascii=False)

pass