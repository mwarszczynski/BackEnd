import json
import csv

# json from existing in current dir file
def JSONfromFile():
    with open('colors.json') as f:
        data = json.load(f)

    for x in data['cars']:
        print('Manufacturer {} offers {}.'.format(x['name'], x['model']))

    with open('offer.json', 'w') as f:
        json.dump(data, f, indent = 2)

# def JSONfromURL():
#     with open('https://vimeo.com/api/v2/video/38356.json') as response:
#         source = response.read()
#
#     print(source)

# print(JSONfromFile())
# print(JSONfromURL())

# Next steps to do
# 1. Finish JSONfromURL function
# 2. Download any JSON and import to csv file

