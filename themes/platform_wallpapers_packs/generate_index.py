import os, re, json
indexFilename = "index.json"

regex = re.compile("^(?!(?:\._|\.).*).*\.json$")

platformWallpapersPacks = [f for f in os.listdir('.') if os.path.isdir(f)]
platformWallpapersPacks.sort()

index = {
    "baseUri": "https://raw.githubusercontent.com/magneticchen/Daijishou/main/themes/platform_wallpapers_packs/",
    "platformWallpapersPackList": []
}


for d in platformWallpapersPacks:
    print(d)
    platformWallpapersPackDir = d
    files = [f for f in os.listdir(platformWallpapersPackDir) if os.path.isfile(platformWallpapersPackDir+'/'+f)]
    # files.sort()

    for f in files:
        if f == indexFilename:
            f = platformWallpapersPackDir+'/'+f
            with open(f, encoding='utf-8') as jsonFile:
                try:
                    platformWallpapersPackIndex = json.load(jsonFile)
                    platformWallpapersPackName = platformWallpapersPackIndex['name']
                    platformWallpapersPackDescription = platformWallpapersPackIndex['description']
                    platformWallpapersPackAuthors = platformWallpapersPackIndex['authors']
                    platformWallpapersPackPreviewThumbnailFilename = platformWallpapersPackIndex['previewThumbnailFilename']
                    index['platformWallpapersPackList'].append({
                        "platformWallpapersPackRootPath": platformWallpapersPackDir,
                        # "platformWallpaperPackIndexPath": f,
                        "platformWallpapersPackPreviewThumbnailPath": platformWallpapersPackDir+'/'+platformWallpapersPackPreviewThumbnailFilename,
                        "platformWallpapersPackAuthors": platformWallpapersPackAuthors,
                        "platformWallpapersPackName": platformWallpapersPackName,
                        "platformWallpapersPackDescription": platformWallpapersPackDescription
                    })
                except Exception as e:
                    print(e)

with open(indexFilename, 'w') as outfile:
    json.dump(index, outfile, indent=2, sort_keys=True)
