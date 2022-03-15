import os, re, json
indexFilename = "index.json"
categoriesDir = "./categories"
regex = re.compile("^(?!(?:\._|\.).*).*\.json$")

files = [f for f in os.listdir('.') if os.path.isfile(f)]
files.sort()

# categories = [f for f in os.listdir(categoriesDir) if os.path.isdir(f)]
categories = [f for f in os.listdir(categoriesDir)]
categories.sort()

index = {
    "baseUri": "https://raw.githubusercontent.com/magneticchen/Daijishou/main/platforms/",
    "platformList": []
}
for f in files:
    if regex.match(f) and f != indexFilename:
        with open(f) as jsonFile:
            platformSharable = json.load(jsonFile)
            platformEntityPortable = platformSharable['platform']
            index['platformList'].append({
                "filename": f,
                "platformName": platformEntityPortable['name'],
                "platformShortname": platformEntityPortable['shortname']
            })

for d in categories:
    categoryDir = categoriesDir+'/'+d
    files = [f for f in os.listdir(categoryDir) if os.path.isfile(categoryDir+'/'+f)]
    files.sort()

    for f in files:
        if regex.match(f) and f != indexFilename:
            f = categoryDir+'/'+f
            with open(f) as jsonFile:
                platformSharable = json.load(jsonFile)
                platformEntityPortable = platformSharable['platform']
                index['platformList'].append({
                    "filename": f,
                    "platformName": d+' - '+platformEntityPortable['name'],
                    "platformShortname": platformEntityPortable['shortname']
                })

with open(indexFilename, 'w') as outfile:
    json.dump(index, outfile, indent=2, sort_keys=True)
