import os, re, json
indexFilename = "index.json"
files = [f for f in os.listdir('.') if os.path.isfile(f)]
index = {
    'platformList': []
}
for f in files:
    regex = re.compile("^(?!(?:\._|\.).*).*\.json$")
    if regex.match(f) and f != indexFilename:
        with open(f) as jsonFile:
            platformSharable = json.load(jsonFile)
            platformEntityPortable = platformSharable['platform']
            index['platformList'].append({
                "filename": f,
                "platformName": platformEntityPortable['name'],
                "platformShortname": platformEntityPortable['shortname']
            })

with open(indexFilename, 'w') as outfile:
    json.dump(index, outfile, indent=2)
