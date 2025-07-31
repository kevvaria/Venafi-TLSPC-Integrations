# CSV SerialNumber Parser

This Python script reads a CSV file and extracts all "serialNumber" values into an array, excluding NULL values. It's a CSV version of the Excel parser with identical functionality.

## Key Differences from Excel Parser

| Feature | Excel Parser | CSV Parser |
|---------|-------------|------------|
| File Format | `.xlsx`, `.xls` | `.csv` |
| Reading Method | `pd.read_excel()` | `pd.read_csv()` |
| Default File | `certs.xlsx` | `certs.csv` |
| Script Name | `excel_fingerprint_parser.py` | `csv_serialNumber_parser.py` |

## Features

- Reads CSV files (.csv)
- Extracts all "serialNumber" column values
- Excludes NULL, NaN, and empty values
- Provides detailed output with count and listing
- Handles errors gracefully
- Makes API call to Venafi Cloud with extracted data

## Installation

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Method 1: Command Line Argument
```bash
python csv_serialNumber_parser.py path/to/your/file.csv
```

### Method 2: Modify Default Path
Edit the script and change the default file path:
```python
csv_file_path = "your_actual_file.csv"
```

## Example Output

```
Reading CSV file: certs.csv
Found 150 valid serialNumber values out of 200 total rows

serialNumber values found:
==================================================
  1. ABC123DEF456
  2. XYZ789GHI012
  3. MNO345PQR678
  ...
==================================================
Total serialNumbers: 150
```

## Requirements

- Python 3.6+
- pandas
- requests

## Error Handling

The script handles various error scenarios:
- File not found
- Missing "serialNumber" column
- Invalid CSV file format
- Empty or corrupted data

## Notes

- The script automatically strips whitespace from serialNumber values
- Only non-NULL, non-empty values are included in the final array
- The script will show available columns if "serialNumber" column is not found
- Makes the same API call to Venafi Cloud as the Excel version

## Comparison with Excel Parser

Both scripts perform identical functions:
1. Read file (Excel vs CSV)
2. Extract "serialNumber" column values
3. Filter out NULL/empty values
4. Print numbered list of values
5. Make API call to Venafi Cloud
6. Display API response

The only difference is the file format they can read. 