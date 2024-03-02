import csv
import json

def convert_csv_to_json(csv_filepath, json_filepath):
    print(f'Converting {csv_filepath} to {json_filepath}')
    # Create a list to hold the rows as dictionaries
    data = []
    # Open the CSV file for reading. If encountering a UnicodeDecodeError, try different encodings like 'utf-8' or 'latin1'.
    try:
        with open(csv_filepath, mode='r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                # print(row)
                data.append(row)
    except UnicodeDecodeError:
        with open(csv_filepath, mode='r', encoding='latin1') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                data.append(row)

    print(f'Writing to {json_filepath}')

    # Open the JSON file for writing
    with open(json_filepath, mode='w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4)

# Example usage, saving the JSON in the same folder as the CSV
convert_csv_to_json('../../data/ListEmergencyFood.csv', '../../data/ListEmergencyFood.json')
