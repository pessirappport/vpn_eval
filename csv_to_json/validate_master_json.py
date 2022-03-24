'''validate json'''
import json
from datetime import datetime
import jsonschema
from jsonschema import validate
import validators

# read schema into program
schema_file = open('master_schema.json', encoding='utf-8')
jsonSchema = json.load(schema_file)
schema_file.close()


def validate_json(data):
    '''method to return whether json is valid or not'''
    try:
        validate(instance=data, schema=jsonSchema)
    except jsonschema.exceptions.ValidationError as err:
        return False
    return True


def date_formatter(field):
    '''checks if dates are formatted correctly.'''
    # checks to see if date field has been filled out or is not empty space
    if data[field] and len(data[field]) > 1:
        date_format = "%m/%d/%y"
        date_res = True
        try:
            date_res = bool(datetime.strptime(data[field], date_format))
        except ValueError:
            date_res = False
        if not date_res:
            errors.append(f'{field} is formatted incorrectly')


def url_formatter(url):
    '''checks if url is formatted correctly.'''
    if not url or url.isspace():
        pass
    else:
        url_res = validators.url(url)
        if not url_res:
            errors.append('URL is formatted incorrectly')


def os_formatter(os):
    '''checks if operating system is entered into the right place'''
    if not data[os] or data[os].isspace():
        pass
    else:
        if data[os] != "Windows 10":
            if data[os].split()[0] not in os.split()[0]:
                errors.append(f"{os} is formatted incorrectly")
        if os == 'Windows Operating System' and data[os] != "Windows 10":
            errors.append(f"{os} is formatted incorrectly")


def eval_formatter(field):
    '''checks if evaluations are properly entered'''
    options = ['No Issues', 'Concerns', 'Failures', '', ' ']
    if data[field] not in options:
        errors.append(f'{field} must be "No Issues", "Concerns", "Failures".')


def character_counter(field, number):
    '''checks if notes are longer than character limit'''
    if len(data[field]) > number:
        errors.append(f'{field} are too long. Limited to {number} characters')


# Convert json to python object
with open('ExpressVPN_data.json', 'r', encoding='utf-8') as f:
    data = f.read()
data = json.loads(data)

# validate it
IS_VALID = validate_json(data)
if IS_VALID:
    print("Given JSON data is valid according to schema")
else:
    print("Given JSON data is invalid according to schema")

errors = []

date_formatter('Background Date')
date_formatter('Windows Evaluation Date')
date_formatter('Ubuntu Evaluation Date')
date_formatter('iOS Evaluation Date')
date_formatter('Android Evaluation Date')
url_formatter(data['URL'])
os_formatter('Windows Operating System')
os_formatter('Android Operating System')
os_formatter('Ubuntu Operating System')
os_formatter('iOS Operating System')
eval_formatter("Ubuntu Configuration")
eval_formatter("Ubuntu IP Geolocation")
eval_formatter("Ubuntu Browser Geolocation")
eval_formatter("Ubuntu DNS Status")
eval_formatter("Ubuntu VPN_Proxy Detection")
eval_formatter("Ubuntu IP Ownership")
eval_formatter("Windows Configuration")
eval_formatter("Windows IP Geolocation")
eval_formatter("Windows Browser Geolocation")
eval_formatter("Windows DNS Status")
eval_formatter("Windows VPN_Proxy Detection")
eval_formatter("Windows IP Ownership")
eval_formatter("iOS Configuration")
eval_formatter("iOS IP Geolocation")
eval_formatter("iOS Browser Geolocation")
eval_formatter("iOS DNS Status")
eval_formatter("iOS VPN_Proxy Detection")
eval_formatter("iOS IP Ownership")
eval_formatter("Android Configuration")
eval_formatter("Android IP Geolocation")
eval_formatter("Android Browser Geolocation")
eval_formatter("Android DNS Status")
eval_formatter("Android VPN_Proxy Detection")
eval_formatter("Android IP Ownership")
character_counter('Windows Notes', 700)
character_counter('iOS Notes', 700)
character_counter('Ubuntu Notes', 700)
character_counter('Android Notes', 700)
character_counter('Notes', 700)
character_counter('Evaluation Summary', 1000)

if errors:
    print(errors)
else:
    print("No errors")
