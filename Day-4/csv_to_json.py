import csv
import json

with open('students.csv', 'r') as new_file:
        csv_reader = csv.DictReader(new_file)    
        data = list(csv_reader)
        json_data = json.dumps(data, indent=2)
        print(json_data)