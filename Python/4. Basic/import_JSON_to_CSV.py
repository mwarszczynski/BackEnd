import json, urllib.request

# json from existing in current dir file
def JSONfromFile():
    with open('colors.json') as f:
        data = json.load(f)

    for x in data['cars']:
        print('Manufacturer {} offers {}.'.format(x['name'], x['model']))

    with open('offer.json', 'w') as f:
        json.dump(data, f, indent = 2)

# get JSON from URL
def JSONfromURL():
    with urllib.request.urlopen('https://ip-ranges.amazonaws.com/ip-ranges.json') as url:
        y = url.read()
        return y

# save JSON to file
# def JSONtoFile(y):
#     with open('save_json_file.json', 'w+') as outfile:
#         json.dump(y, outfile, ensure_ascii=False)

print(JSONfromFile())
print(JSONfromURL())

