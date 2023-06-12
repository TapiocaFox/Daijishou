import os, re, json
indexFilename = "index.json"

regex = re.compile("^(?!(?:\._|\.).*).*\.json$")

platformThumbnailsPacks = [f for f in os.listdir('.') if os.path.isdir(f)]
platformThumbnailsPacks = sorted(platformThumbnailsPacks, key=str.casefold)

index = {
    "baseUri": "https://raw.githubusercontent.com/magneticchen/Daijishou/main/themes/platform_thumbnails_packs/",
    "platformThumbnailsPackList": []
}


for d in platformThumbnailsPacks:
    # print(d)
    platformThumbnailsPackDir = d
    files = [f for f in os.listdir(platformThumbnailsPackDir) if os.path.isfile(platformThumbnailsPackDir+'/'+f)]
    # files = sorted(files, key=str.casefold)

    for f in files:
        if f == indexFilename:
            f = platformThumbnailsPackDir+'/'+f
            with open(f, encoding='utf-8') as jsonFile:
                try:
                    platformThumbnailsPackIndex = json.load(jsonFile)
                    print(platformThumbnailsPackIndex['name'])
                    print("  Author(s): "+", ".join(platformThumbnailsPackIndex['authors'])+"")
                    print("  Description: "+str(platformThumbnailsPackIndex['description']))
                    if 'isNSFW' in platformThumbnailsPackIndex.keys():
                        print("  IsNSFW: "+str(platformThumbnailsPackIndex['isNSFW']))
                    else: 
                        print("  IsNSFW: "+str(False))
                    print("")
                    platformThumbnailsPackName = platformThumbnailsPackIndex['name']
                    platformThumbnailsPackDescription = platformThumbnailsPackIndex['description']
                    platformThumbnailsPackAuthors = platformThumbnailsPackIndex['authors']
                    platformThumbnailsPackPreviewThumbnailFilename = platformThumbnailsPackIndex['previewThumbnailFilename']
                    platformThumbnailsPackIsNSFW = platformThumbnailsPackIndex['isNSFW'] if 'isNSFW' in platformThumbnailsPackIndex.keys() else False
                    index['platformThumbnailsPackList'].append({
                        "platformThumbnailsPackRootPath": platformThumbnailsPackDir,
                        # "platformThumbnailPackIndexPath": f,
                        "platformThumbnailsPackPreviewThumbnailPath": platformThumbnailsPackDir+'/'+platformThumbnailsPackPreviewThumbnailFilename,
                        "platformThumbnailsPackAuthors": platformThumbnailsPackAuthors,
                        "platformThumbnailsPackName": platformThumbnailsPackName,
                        "platformThumbnailsPackDescription": platformThumbnailsPackDescription,
                        # "platformThumbnailsPackIsNSFW": platformThumbnailsPackIsNSFW
                    })
                except Exception as e:
                    print(e)
print("Total "+str(len(index['platformThumbnailsPackList']))+" entries in the index.")
with open(indexFilename, 'w') as outfile:
    json.dump(index, outfile, indent=2, sort_keys=True)
