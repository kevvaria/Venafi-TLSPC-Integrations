#!/usr/bin/env python3
"""
CSV ID Parser

This script reads a CSV file and extracts all "id" values into an array,
excluding NULL values. 

The resulting array is used to perform an API call to Venafi Cloud to retire+blocklist the certificates.

Usage: python csv_serialNumber_parser.py <csv_file_path>

Example: python csv_serialNumber_parser.py certs.csv

Requirements:
- pandas
- requests
- sys
- os
- csv_file_path: Path to the CSV file
- vaas_api_key: API key for Venafi Cloud
"""

import pandas as pd
import sys
import os
import requests

vaas_api_key = input("Enter your Venafi Cloud API key: ")

def parse_ids_from_csv(file_path):
    """
    Read a CSV file and extract all "id" values into an array.
    
    Args:
        file_path (str): Path to the CSV file
        
    Returns:
        list: Array of id values (excluding NULL values)
    """
    try:
        # Read the CSV file
        print(f"Reading CSV file: {file_path}")
        df = pd.read_csv(file_path)
        id_values = []    #Extract id values, excluding NULL/NaN values

        # Check if "id" column exists
        if "id" not in df.columns:
            print("Error: 'id' column not found in the CSV file.")
            print(f"Available columns: {list(df.columns)}")
            return []
        
        for value in df["id"]:
            # Check if the value is not null/NaN and not empty
            if pd.notna(value) and str(value).strip() != "":
                id_values.append(str(value).strip())
        
        print(f"Found {len(id_values)} valid id values out of {len(df)} total rows")
        
        return id_values
        
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return []
    except Exception as e:
        print(f"Error reading CSV file: {str(e)}")
        return []


def main():
    """Main function to execute the id parsing."""
    
    # Check if file path is provided as command line argument
    if len(sys.argv) > 1:
        csv_file_path = sys.argv[1]
    else:
        # Default file path - you can change this to your CSV file path
        csv_file_path = "certs.csv"  # Change this to your actual file path
    
    # Check if file exists
    if not os.path.exists(csv_file_path):
        print(f"Error: File '{csv_file_path}' does not exist.")
        print("Usage: python csv_serialNumber_parser.py <csv_file_path>")
        print("Or modify the default file path in the script.")
        return
    
    # Parse ids from CSV file
    id_array = parse_ids_from_csv(csv_file_path)
    print(id_array)
    
    # Print the resulting array
    if id_array:
        print("\nid values found:")
        # print("=" * 50)
        # for i, id_value in enumerate(id_array, 1):
        #     print(f"{i:3d}. {id_value}")
        # print("=" * 50)
        print(f"Total ids: {len(id_array)}")
        
        # API call to Venafi Cloud
        url = "https://api.venafi.cloud/outagedetection/v1/certificates/retirement"

        payload = {
            "addToBlocklist": True,
            "certificateIds": id_array
        }
        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            'tppl-api-key': vaas_api_key
        }

        response = requests.post(url, json=payload, headers=headers)

        print(response.text)
    else:
        print("No valid id values found in the CSV file.")


if __name__ == "__main__":
    main() 