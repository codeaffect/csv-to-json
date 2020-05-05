import csv
import json

data = {}
id = 1

with open('quotes.csv', 'r') as rf:
    reader = csv.DictReader(rf, delimiter=';')
    for row in reader:
        data[id] = row
        id += 1

    with open('quote.json', 'w') as jsonFile:
        jsonFile.write(json.dumps(data, indent=4))
