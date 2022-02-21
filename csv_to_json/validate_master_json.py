'''validate json'''
import json
import jsonschema
from jsonschema import validate

# read schema into program
schema_file = open('master_schema.json', encoding='utf-8')
jsonSchema = json.load(schema_file)
schema_file.close()


def validate_json(json_data):
    '''method to return whether json is valid or not'''
    try:
        validate(instance=json_data, schema=jsonSchema)
    except jsonschema.exceptions.ValidationError as err:
        print(err)
        return False
    return True


# Convert json to python object
with open('data.json', 'r', encoding='utf-8') as f:
    data = f.read()
json_data = json.loads(data)

# validate it
IS_VALID = validate_json(json_data)
if IS_VALID:
    print("Given JSON data is Valid")
else:
    print("Given JSON data is invalid")
