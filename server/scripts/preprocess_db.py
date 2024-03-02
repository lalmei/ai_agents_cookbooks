import json
import uuid

def filter_entries_with_website_and_save():
    with open('../../data/ListEmergencyFood.json', 'r') as file:
        data = json.load(file)
        filtered_data = [entry for entry in data if entry.get('Website')]
        for entry in filtered_data:
            entry['id'] = str(uuid.uuid4())
    
    with open('../database.json', 'w') as file:
        json.dump(filtered_data, file, indent=4)

filter_entries_with_website_and_save()

