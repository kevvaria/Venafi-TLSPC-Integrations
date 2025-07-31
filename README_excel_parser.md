# Excel Fingerprint Parser

This Python script reads an Excel file and extracts all "Fingerprint" values into an array, excluding NULL values.

## Features

- Reads Excel files (.xlsx, .xls)
- Extracts all "Fingerprint" column values
- Excludes NULL, NaN, and empty values
- Provides detailed output with count and listing
- Handles errors gracefully

## Installation

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Method 1: Command Line Argument
```bash
python excel_fingerprint_parser.py path/to/your/file.xlsx
```

### Method 2: Modify Default Path
Edit the script and change the default file path:
```python
excel_file_path = "your_actual_file.xlsx"
```

## Example Output

```
Reading Excel file: data.xlsx
Found 15 valid fingerprint values out of 20 total rows

Fingerprint values found:
==================================================
  1. ABC123DEF456
  2. XYZ789GHI012
  3. MNO345PQR678
  ...
==================================================
Total fingerprints: 15
```

## Requirements

- Python 3.6+
- pandas
- openpyxl (for Excel file support)

## Error Handling

The script handles various error scenarios:
- File not found
- Missing "Fingerprint" column
- Invalid Excel file format
- Empty or corrupted data

## Notes

- The script automatically strips whitespace from fingerprint values
- Only non-NULL, non-empty values are included in the final array
- The script will show available columns if "Fingerprint" column is not found 