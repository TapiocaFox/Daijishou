import os, re, json

indexFilename = "index.json"

categoriesDir = "./categories"
categoriesNames = {
    "rp2_plus": "RP2+"
}

regex = re.compile("^(?!(?:\._|\.).*).*\.json$")

files = [f for f in os.listdir('.') if os.path.isfile(f)]
files.sort()

categories = []
try: 
    # categories = [f for f in os.listdir(categoriesDir) if os.path.isdir(f)]
    categories += [f for f in os.listdir(categoriesDir)]
    categories.sort()

except Exception:
    pass

index = {
    "baseUri": "https://raw.githubusercontent.com/magneticchen/Daijishou/main/platforms/",
    "platformList": []
}
for f in files:
    if regex.match(f) and f != indexFilename:
        with open(f) as jsonFile:
            try:
                platformSharable = json.load(jsonFile)
                platformEntityPortable = platformSharable['platform']
                print(platformEntityPortable['name']+" ("+platformEntityPortable['shortname']+")")
                print("  RevisionNumber: "+str(platformSharable['revisionNumber']))
                print("  Scrapers: "+str(len(platformEntityPortable['scraperSourceList'])))
                print("  Players: "+str(len(platformSharable['playerList'])))
                print("")
                revisionNumber = platformSharable['revisionNumber'] if('revisionNumber' in platformSharable) else None
                index['platformList'].append({
                    "filename": f,
                    "platformName": platformEntityPortable['name'],
                    "platformShortname": platformEntityPortable['shortname'],
                    'revisionNumber': revisionNumber
                })
            except Exception as e:
                print(e)
                print(f)

for d in categories:
    categoryDir = categoriesDir+'/'+d
    files = [f for f in os.listdir(categoryDir) if os.path.isfile(categoryDir+'/'+f)]
    files.sort()
    catagoriyName = d
    if d in categoriesNames:
        catagoriyName = categoriesNames[d]
    for f in files:
        if regex.match(f) and f != indexFilename:
            f = categoryDir+'/'+f
            with open(f) as jsonFile:
                try:
                    platformSharable = json.load(jsonFile)
                    platformEntityPortable = platformSharable['platform']
                    print(platformEntityPortable['name']+" ("+platformEntityPortable['shortname']+")")
                    print("  RevisionNumber: "+str(platformSharable['revisionNumber']))
                    print("  Scrapers: "+str(len(platformEntityPortable['scraperSourceList'])))
                    print("  Players: "+str(len(platformSharable['playerList'])))
                    print("")
                    index['platformList'].append({
                        "filename": f,
                        "platformName": '['+catagoriyName+'] '+platformEntityPortable['name'],
                        # "platformName": catagoriyName+' - '+platformEntityPortable['name'],
                        # "platformName": platformEntityPortable['name']+" ("+catagoriyName+")",
                        "platformShortname": platformEntityPortable['shortname']
                    })
                except Exception as e:
                    print(e)
                    print(f)
print("Total "+str(len(index['platformList']))+" entries in the index.")
with open(indexFilename, 'w') as outfile:
    json.dump(index, outfile, indent=2, sort_keys=True)
