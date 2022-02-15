'''convert csv to json'''
import csv
import json
def csv_to_json(csv_file_path, json_file_path):
    '''convert csv to json'''
    json_array = []
    #read csv file
    with open(csv_file_path, encoding='utf-8') as csvf:
        #load csv file data using csv library's dictionary reader
        csv_reader = csv.DictReader(csvf)
        #convert each csv row into python dict
        for row in csv_reader:
            #add this python dict to json array
            json_array.append(row)
    #convert python json_array to JSON String and write to file
    with open(json_file_path, 'w', encoding='utf-8') as jsonf:
        json_string = json.dumps(json_array, indent=4)
        jsonf.write(json_string)
csv_file_path = r'vpn_eval.csv'
json_file_path = r'data.json'
csv_to_json(csv_file_path, json_file_path)
