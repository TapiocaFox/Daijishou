import os, re, json
indexFilename = "index.json"
devicesDir = "./devices"
regex = re.compile("^(?!(?:\._|\.).*).*\.json$")

files = [f for f in os.listdir('.') if os.path.isfile(f)]
files.sort()

# devices = [f for f in os.listdir(devicesDir) if os.path.isdir(f)]
devices = [f for f in os.listdir(devicesDir)]
devices.sort()

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

for d in devices:
    deviceDir = devicesDir+'/'+d
    files = [f for f in os.listdir(deviceDir) if os.path.isfile(deviceDir+'/'+f)]
    files.sort()
    
    for f in files:
        if regex.match(f) and f != indexFilename:
            f = deviceDir+'/'+f
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
