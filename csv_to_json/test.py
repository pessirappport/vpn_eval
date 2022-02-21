import json


def notes_formatter(field):
    print(len(data[field]))
    if len(data[field]) > 300:
        errors.append(f'{field} are too long. Limited to 300 characters')


with open('data.json', 'r', encoding='utf-8') as f:
    data = f.read()
data = json.loads(data)

errors = []

notes_formatter('Windows Notes')
notes_formatter('IoS Notes')
notes_formatter('Ubuntu Notes')
notes_formatter('Android Notes')
notes_formatter('Notes')
print(errors)