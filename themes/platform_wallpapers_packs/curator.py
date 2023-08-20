import argparse, os, re, json, traceback

def sortDictionaryKeysByListOfStrings(dictionary, listOfStrings):
  sortedKeys = sorted(dictionary.keys(), key=lambda key: listOfStrings.index(key))
  return {key: dictionary[key] for key in sortedKeys}

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--path", default=".")
parser.add_argument("-i", "--index", default="../../platforms/index.json")
# parser.add_argument("-rev", "--increase_revisions", default=False)
args = parser.parse_args()

# Constants
jsonRegex = re.compile("^(?!(?:\._|\.).*).*\.json$")
platformWallpapersPackIndexWallpaperListItemJson = [
    "matchPlatformShortname",
    "matchPlatformUniqueId",
    "filename"
]
platformWallpapersPackIndexJson = [
    "name",
    "description",
    "authors",
    "sources",
    "previewThumbnailFilename",
    "isNSFW",
    "hasDefaultWallpaper",
    "defaultWallpaperFilename",
    "wallpaperList",
]

indexFilename = "index.json"
basePath = args.path
indexPath = args.index
curatedDirectory = os.path.join(basePath, "./curated")
shortnameToUniqueId = {}
with open(indexPath) as jsonFile:
    platformList = json.load(jsonFile)['platformList']
    for platform in platformList:
        shortnameToUniqueId[platform['platformShortname']] = platform['platformUniqueId']

if not os.path.exists(curatedDirectory):
    os.mkdir(curatedDirectory)

print("Directory '%s' created for curator." %curatedDirectory)

dirs = [f for f in os.listdir(basePath) if os.path.isdir(f)]
# files = []
# for dir in dirs:
#     fileList = os.listdir(os.path.join(basePath, dir))
#     for file in fileList:
#         if "index.json" in file:
#             files.append(os.path.join(basePath, dir, file))
#             print(file)

for dir in dirs:
    files = os.listdir(os.path.join(basePath, dir))
    for f in files:
        # print(f)
        if "index.json" == f:
            with open(os.path.join(basePath, dir, "index.json")) as jsonFile:
                try:
                    platformWallpapersPackIndex = json.load(jsonFile)
                    # print(str(platformWallpapersPackIndex))
                    # print(str(jsonFile))
                    print(platformWallpapersPackIndex['name'])
                    print(platformWallpapersPackIndex['description'])
                    print("Authors: "+str(platformWallpapersPackIndex['authors']))
                    print("")

                    wallpaperList = []
                    for wallpaper in platformWallpapersPackIndex['wallpaperList']:
                        try:
                            wallpaper["matchPlatformUniqueId"] = shortnameToUniqueId[wallpaper["matchPlatformShortname"]]
                        except Exception as e:
                            wallpaper["matchPlatformUniqueId"] = wallpaper["matchPlatformShortname"]
                        wallpaper = sortDictionaryKeysByListOfStrings(wallpaper, platformWallpapersPackIndexWallpaperListItemJson)
                        wallpaperList.append(wallpaper)
                    platformWallpapersPackIndex['wallpaperList'] = wallpaperList
                    # Write file
                    curatedSubDirectory = os.path.join(os.path.join(curatedDirectory, dir))
                    platformWallpapersPackIndex = sortDictionaryKeysByListOfStrings(platformWallpapersPackIndex, platformWallpapersPackIndexJson)
                    if not os.path.exists(curatedSubDirectory):
                        os.mkdir(curatedSubDirectory)
                    with open(os.path.join(curatedSubDirectory, "index.json"), 'w') as outfile:
                        json.dump(platformWallpapersPackIndex, outfile, indent=2, sort_keys=False)

                except Exception as e:
                    traceback.print_exc()
                    print(e)
                    print(f)