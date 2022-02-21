'''convert master csv data to master json file'''
from csv2json import convert

with open('master_format_1.csv', encoding='utf-8') as r, open('data.json', 'w', encoding='utf-8') as w:
    convert(r, w)
