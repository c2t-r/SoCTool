# SoC TextMap Tool

This tool decodes and encodes text map files (db_lang).

## Features
- Decode binary text map (db_lang) to JSON (db_lang.json)
- Encode JSON (db_lang.json) to binary text map (db_lang_encoded)

## Usage

- Decode (binary to JSON):
  ```bash
  python decode.py
  ```
  - Input: db_lang (binary file)
  - Output: db_lang.json (UTF-8 JSON file)

- Encode (JSON to binary):
  ```bash
  python encode.py
  ```
  - Input: db_lang.json
  - Output: db_lang_encoded (binary file)

## Requirements
- Python 3.x
- See requirements.txt for dependencies

## Output
- db_lang.json: Decoded text data
- db_lang_encoded: Encoded binary text map
