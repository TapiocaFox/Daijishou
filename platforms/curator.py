import argparse, os, re, json, traceback

def sortDictionaryKeysByListOfStrings(dictionary, listOfStrings):
  sortedKeys = sorted(dictionary.keys(), key=lambda key: listOfStrings.index(key))
  return {key: dictionary[key] for key in sortedKeys}

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--path", default=".")
parser.add_argument("-rev", "--increase_revisions", default=False)
args = parser.parse_args()

# Constants
jsonRegex = re.compile("^(?!(?:\._|\.).*).*\.json$")
retroArch64AmStartRegex = re.compile("^.*\-n\s+com\.retroarch\.aarch64/.*/cores/(.*)\.so[\n\r\s]+.*$", re.M|re.S)
retroArch32AmStartRegex = re.compile("^.*\-n\s+com\.retroarch\.ra32/.*/cores/(.*)\.so[\n\r\s]+.*$", re.M|re.S)
retroArchAmStartRegex = re.compile("^.*\-n\s+com\.retroarch/.*/cores/(.*)\.so[\n\r\s]+.*$", re.M|re.S)
standaloneAmStartRegex = re.compile("^.*\-n\s+([^/]+)/.*$", re.M|re.S)
platformSharableKeysOrder = [
    "databaseVersion",
    "revisionNumber",
    "platform",
    "playerList",
]
platformEntityPortableKeysOrder = [
    "name",
    "uniqueId",
    "shortname",
    "description",
    "acceptedFilenameRegex",
    "scraperSourceList",
    "boxArtAspectRatioId",
    "useCustomBoxArtAspectRatio",
    "customBoxArtAspectRatio",
    "screenAspectRatioId",
    "useCustomScreenAspectRatio",
    "customScreenAspectRatio",
    "retroAchievementsAlias",
    "extra",
]

playerEntityPortableKeysOrder = [
    "name",
    "uniqueId",
    "description",
    "acceptedFilenameRegex",
    "amStartArguments",
    "killPackageProcesses",
    "killPackageProcessesWarning",
    "extra"
]

indexFilename = "index.json"
databaseVersion = 14
basePath = args.path
increaseRevisionNumber = args.increase_revisions
curatedDirectory = os.path.join(basePath, "./curated")

if not os.path.exists(curatedDirectory):
    os.mkdir(curatedDirectory)

print("Directory '%s' created for curator." %curatedDirectory)

files = [f for f in os.listdir(basePath) if os.path.isfile(f)]

for f in files:
    if jsonRegex.match(f) and f != indexFilename:
        with open(f) as jsonFile:
            try:
                platformSharable = json.load(jsonFile)
                platformEntityPortable = platformSharable['platform']
                playerEntityPortableList = platformSharable['playerList']
                print(platformEntityPortable['name']+" ("+platformEntityPortable['shortname']+")")
                print("  RevisionNumber: "+str(platformSharable['revisionNumber']))
                print("  Scrapers: "+str(len(platformEntityPortable['scraperSourceList'])))
                print("  Players: "+str(len(platformSharable['playerList'])))
                print("")


                 # Platform
                uniqueId = platformEntityPortable['uniqueId']
                if uniqueId == None:
                    uniqueId = platformEntityPortable['shortname']
                platformSharable['platform'] = sortDictionaryKeysByListOfStrings(platformEntityPortable, platformEntityPortableKeysOrder)


                # Players
                standalonePlayers = []
                retroArch64Players = []
                retroArch32Players = []
                retroArchPlayers = []
                for playerEntityPortable in playerEntityPortableList:
                    amStartArguments = playerEntityPortable['amStartArguments']
                    retroArch64AmStartMatches = retroArch64AmStartRegex.match(amStartArguments)
                    retroArch32AmStartMatches = retroArch32AmStartRegex.match(amStartArguments)
                    retroArchAmStartMatches = retroArchAmStartRegex.match(amStartArguments)
                    standaloneAmStartMatches = standaloneAmStartRegex.match(amStartArguments)

                    if retroArch64AmStartMatches:
                        retroArchLibraryName = retroArch64AmStartMatches[1].replace("_libretro_android", "")
                        playerEntityPortable['uniqueId'] = uniqueId+".ra64."+retroArchLibraryName
                        playerEntityPortable = sortDictionaryKeysByListOfStrings(playerEntityPortable, playerEntityPortableKeysOrder)
                        retroArch64Players.append(playerEntityPortable)

                    elif retroArch32AmStartMatches:
                        retroArchLibraryName = retroArch32AmStartMatches[1].replace("_libretro_android", "")
                        playerEntityPortable['uniqueId'] = uniqueId+".ra32."+retroArchLibraryName
                        playerEntityPortable = sortDictionaryKeysByListOfStrings(playerEntityPortable, playerEntityPortableKeysOrder)
                        retroArch64Players.append(playerEntityPortable)

                    elif retroArchAmStartMatches:
                        retroArchLibraryName = retroArchAmStartMatches[1].replace("_libretro_android", "")
                        playerEntityPortable['uniqueId'] = uniqueId+".ra."+retroArchLibraryName
                        playerEntityPortable = sortDictionaryKeysByListOfStrings(playerEntityPortable, playerEntityPortableKeysOrder)
                        retroArch64Players.append(playerEntityPortable)
                    elif standaloneAmStartMatches:
                        standalonePackageName = standaloneAmStartMatches[1]
                        playerEntityPortable['uniqueId'] = uniqueId+"."+standalonePackageName
                        playerEntityPortable = sortDictionaryKeysByListOfStrings(playerEntityPortable, playerEntityPortableKeysOrder)
                        standalonePlayers.append(playerEntityPortable)

                platformSharable['playerList'] = standalonePlayers+retroArch64Players+retroArch32Players+retroArchPlayers
                                    

                # Entire
                revisionNumber = platformSharable['revisionNumber'] if('revisionNumber' in platformSharable) else 0
                if increaseRevisionNumber:
                    revisionNumber += 1
                platformSharable['revisionNumber'] = revisionNumber
                platformSharable['databaseVersion'] = databaseVersion
                platformSharable = sortDictionaryKeysByListOfStrings(platformSharable, platformSharableKeysOrder)

                # Write file
                with open(os.path.join(curatedDirectory, f), 'w') as outfile:
                    json.dump(platformSharable, outfile, indent=2, sort_keys=False)

            except Exception as e:
                traceback.print_exc()
                print(e)
                print(f)