import json
import csv
import sys
from pathlib import Path

def json_to_csv(json_file, csv_file=None):
    """
    Convert a JSON file to CSV format.
    
    Args:
        json_file (str): Path to the input JSON file
        csv_file (str, optional): Path to the output CSV file. If not provided,
                                 uses the same name as json_file with .csv extension
    """
    # Read JSON file
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Error: File '{json_file}' not found.")
        return False
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON format in '{json_file}': {e}")
        return False
    
    # Ensure data is a list
    if not isinstance(data, list):
        data = [data]
    
    if not data:
        print("Error: JSON file is empty or contains no data.")
        return False
    
    # Determine output filename
    if csv_file is None:
        csv_file = Path(json_file).with_suffix('.csv')
    
    # Extract all possible keys from all objects
    fieldnames = set()
    for item in data:
        if isinstance(item, dict):
            fieldnames.update(item.keys())
    
    fieldnames = sorted(list(fieldnames))
    
    if not fieldnames:
        print("Error: No valid data structure found in JSON file.")
        return False
    
    # Write to CSV
    try:
        with open(csv_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            
            for item in data:
                if isinstance(item, dict):
                    writer.writerow(item)
        
        print(f"Successfully converted '{json_file}' to '{csv_file}'")
        return True
    
    except Exception as e:
        print(f"Error writing CSV file: {e}")
        return False

def main():
    """
    Main function to handle command-line usage.
    """
    if len(sys.argv) < 2:
        print("Usage: python JSON2CSV.py <input.json> [output.csv]")
        print("\nExample:")
        print("  python JSON2CSV.py data.json")
        print("  python JSON2CSV.py data.json output.csv")
        sys.exit(1)
    
    json_file = sys.argv[1]
    csv_file = sys.argv[2] if len(sys.argv) > 2 else None
    
    success = json_to_csv(json_file, csv_file)
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
