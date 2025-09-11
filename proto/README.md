# SoC Proto Tool

This tool deserializes encrypted binary files and generates raw data files (.json) and Protocol Buffers definition files (.proto).

## Features
- Deserialization of encrypted binaries
- Output of raw data (.json)
- Generation of protobuf definition files (.proto)

## Usage
Run main.py with the following command:

```bash
python main.py
```

No command-line arguments are required. Input/output directories are fixed in the script:
- Input: ../../SwordOfConvallaria/assets/PB
- Output (raw JSON): deserialized/
- Output (protobuf): out/

## Requirements
- Python 3.x
- See requirements.txt for dependencies

## Output
- .json files: Raw deserialized data
- .proto files: Protobuf data structure definitions
