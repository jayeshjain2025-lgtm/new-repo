# JSON2CSV

A simple, lightweight Python utility to convert JSON files to CSV format.

## Description

JSON2CSV is a command-line tool that makes it easy to convert JSON data into CSV format. It handles both single JSON objects and arrays of objects, automatically detecting all fields and creating appropriate CSV headers.

## Features

- **Simple to Use**: Just provide the input JSON file and optionally specify an output CSV file
- **Automatic Field Detection**: Automatically extracts all unique keys from JSON objects to create CSV headers
- **Flexible Input**: Handles both single JSON objects and arrays of objects
- **Smart Output Naming**: Automatically generates output filename based on input if not specified
- **Error Handling**: Comprehensive error messages for common issues (file not found, invalid JSON, etc.)
- **UTF-8 Support**: Full Unicode support for international characters
- **Sorted Headers**: CSV headers are alphabetically sorted for consistency

## Installation

1. Clone this repository:
```bash
git clone https://github.com/jayeshjain2025-lgtm/new-repo.git
cd new-repo
```

2. No additional dependencies required - uses only Python standard library!

## Usage

### Basic Usage

Convert a JSON file to CSV (output will be named automatically):
```bash
python JSON2CSV.py input.json
```

### Specify Output File

Convert JSON to CSV with a custom output filename:
```bash
python JSON2CSV.py input.json output.csv
```

### Example

If you have a JSON file `data.json`:
```json
[
  {"name": "Alice", "age": 30, "city": "New York"},
  {"name": "Bob", "age": 25, "city": "San Francisco"},
  {"name": "Charlie", "age": 35, "city": "Chicago"}
]
```

Running:
```bash
python JSON2CSV.py data.json
```

Will create `data.csv`:
```csv
age,city,name
30,New York,Alice
25,San Francisco,Bob
35,Chicago,Charlie
```

## Requirements

- Python 3.6 or higher
- No external dependencies

## Use as a Module

You can also import and use the conversion function in your own Python scripts:

```python
from JSON2CSV import json_to_csv

# Convert a JSON file to CSV
success = json_to_csv('input.json', 'output.csv')

if success:
    print("Conversion successful!")
else:
    print("Conversion failed")
```

## Error Handling

The tool provides clear error messages for common issues:
- File not found
- Invalid JSON format
- Empty JSON files
- No valid data structure

## License

MIT License - feel free to use this tool in your projects!

## Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests

## Author

Created by jayeshjain2025-lgtm

## Support

If you encounter any issues or have questions, please open an issue on GitHub.
