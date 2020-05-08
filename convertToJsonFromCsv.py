import csv
import json

data = {}
id = 1

# inFile = 'quotes.csv'
# outFile = 'quotes.json'
inFile = 'joke.csv'
outFile = 'joke.json'

with open(inFile, 'r') as rf:
    reader = csv.DictReader(rf, delimiter='|')
    for row in reader:
        print(row)
        data[id] = row
        id += 1

    with open(outFile, 'w') as jsonFile:
        jsonFile.write(json.dumps(data, indent=4))
