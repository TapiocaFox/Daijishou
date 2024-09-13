import argparse, os, re, json, traceback

def sortDictionaryKeysByListOfStrings(dictionary, listOfStrings):
    sortedKeys = sorted(dictionary.keys(), key=lambda key: listOfStrings.index(key))
    return {key: dictionary[key] for key in sortedKeys}

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--path", default=".")
parser.add_argument("-rev", "--increase_revisions", action='store_true', default=False)
parser.add_argument("-c", "--curated", default="./curated")
args = parser.parse_args()

# Constants
jsonRegex = re.compile(r"^(?!(?:\._|\.).*).*\.json$")
retroArch64AmStartRegex = re.compile(r"^.*\-n\s+com\.retroarch\.aarch64/.*/cores/(.*)\.so[\n\r\s]+.*$", re.M|re.S)
retroArch32AmStartRegex = re.compile(r"^.*\-n\s+com\.retroarch\.ra32/.*/cores/(.*)\.so[\n\r\s]+.*$", re.M|re.S)
retroArchAmStartRegex = re.compile(r"^.*\-n\s+com\.retroarch/.*/cores/(.*)\.so[\n\r\s]+.*$", re.M|re.S)
standaloneAmStartRegex = re.compile(r"^.*\-n\s+([^/]+)/.*$", re.M|re.S)
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
    # "retroAchievementsAlias",
    # "retroAchievementsSystemId",  # This will be removed after conversion
    "retroAchievementsConsoleIdList",
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
curatedPath = args.curated
curatedDirectory = os.path.join(basePath,curatedPath)

if not os.path.exists(curatedDirectory):
    os.mkdir(curatedDirectory)
    print(f"Directory '{curatedDirectory}' created for curator.")
else:
    print(f"Directory '{curatedDirectory}' already exists.")

files = [f for f in os.listdir(basePath) if os.path.isfile(os.path.join(basePath, f))]

for f in files:
    if jsonRegex.match(f) and f != indexFilename:
        filePath = os.path.join(basePath, f)
        with open(filePath, 'r', encoding='utf-8') as jsonFile:
            try:
                platformSharable = json.load(jsonFile)
                platformEntityPortable = platformSharable['platform']
                playerEntityPortableList = platformSharable.get('playerList', [])
                print(f"{platformEntityPortable.get('name', 'Unknown')} ({platformEntityPortable.get('shortname', 'N/A')})")
                print(f"  RevisionNumber: {platformSharable.get('revisionNumber', 0)}")
                print(f"  Scrapers: {len(platformEntityPortable.get('scraperSourceList', []))}")
                print(f"  Players: {len(playerEntityPortableList)}")
                print("")

                # Platform
                uniqueId = platformEntityPortable.get('uniqueId') or platformEntityPortable.get('shortname')
                

                # Conversion: retroAchievementsSystemId -> retroAchievementsConsoleIdList
                retroAchievementsSystemId = platformEntityPortable.get('retroAchievementsSystemId')
                if retroAchievementsSystemId is not None:
                    if isinstance(retroAchievementsSystemId, int):
                        # Assign the system ID to the console ID list
                        platformSharable['platform']['retroAchievementsConsoleIdList'] = [retroAchievementsSystemId]
                        print(f"    Converted retroAchievementsSystemId {retroAchievementsSystemId} to retroAchievementsConsoleIdList [{retroAchievementsSystemId}]")
                    else:
                        print(f"    Warning: retroAchievementsSystemId is not an integer in file {f}. Skipping conversion.")
                    
                    # Remove the retroAchievementsSystemId field
                    del platformSharable['platform']['retroAchievementsSystemId']
                else:
                    # If retroAchievementsConsoleIdList is not present, ensure it's an empty list
                    if 'retroAchievementsConsoleIdList' not in platformSharable['platform']:
                        platformSharable['platform']['retroAchievementsConsoleIdList'] = []
                        print(f"    retroAchievementsConsoleIdList not found. Initialized as empty list.")

                if platformEntityPortable.get('retroAchievementsAlias') is not None:
                    del platformSharable['platform']['retroAchievementsAlias']

                platformSharable['platform'] = sortDictionaryKeysByListOfStrings(platformEntityPortable, platformEntityPortableKeysOrder)

                # Players
                standalonePlayers = []
                retroArch64Players = []
                retroArch32Players = []
                retroArchPlayers = []
                for playerEntityPortable in playerEntityPortableList:
                    amStartArguments = playerEntityPortable.get('amStartArguments', '')
                    retroArch64AmStartMatches = retroArch64AmStartRegex.match(amStartArguments)
                    retroArch32AmStartMatches = retroArch32AmStartRegex.match(amStartArguments)
                    retroArchAmStartMatches = retroArchAmStartRegex.match(amStartArguments)
                    standaloneAmStartMatches = standaloneAmStartRegex.match(amStartArguments)

                    if retroArch64AmStartMatches:
                        retroArchLibraryName = retroArch64AmStartMatches[1].replace("_libretro_android", "")
                        playerEntityPortable['uniqueId'] = f"{uniqueId}.ra64.{retroArchLibraryName}"
                        playerEntityPortable = sortDictionaryKeysByListOfStrings(playerEntityPortable, playerEntityPortableKeysOrder)
                        retroArch64Players.append(playerEntityPortable)

                    elif retroArch32AmStartMatches:
                        retroArchLibraryName = retroArch32AmStartMatches[1].replace("_libretro_android", "")
                        playerEntityPortable['uniqueId'] = f"{uniqueId}.ra32.{retroArchLibraryName}"
                        playerEntityPortable = sortDictionaryKeysByListOfStrings(playerEntityPortable, playerEntityPortableKeysOrder)
                        retroArch32Players.append(playerEntityPortable)

                    elif retroArchAmStartMatches:
                        retroArchLibraryName = retroArchAmStartMatches[1].replace("_libretro_android", "")
                        playerEntityPortable['uniqueId'] = f"{uniqueId}.ra.{retroArchLibraryName}"
                        playerEntityPortable = sortDictionaryKeysByListOfStrings(playerEntityPortable, playerEntityPortableKeysOrder)
                        retroArchPlayers.append(playerEntityPortable)
                    
                    elif standaloneAmStartMatches:
                        standalonePackageName = standaloneAmStartMatches[1]
                        playerEntityPortable['uniqueId'] = f"{uniqueId}.{standalonePackageName}"
                        playerEntityPortable = sortDictionaryKeysByListOfStrings(playerEntityPortable, playerEntityPortableKeysOrder)
                        standalonePlayers.append(playerEntityPortable)

                platformSharable['playerList'] = standalonePlayers + retroArch64Players + retroArch32Players + retroArchPlayers

                # Entire
                revisionNumber = platformSharable.get('revisionNumber', 0)
                if increaseRevisionNumber:
                    revisionNumber += 1
                platformSharable['revisionNumber'] = revisionNumber
                platformSharable['databaseVersion'] = databaseVersion
                platformSharable = sortDictionaryKeysByListOfStrings(platformSharable, platformSharableKeysOrder)

                # Write file
                outputFilePath = os.path.join(curatedDirectory, f)
                with open(outputFilePath, 'w', encoding='utf-8') as outfile:
                    json.dump(platformSharable, outfile, indent=2, sort_keys=False)
                print(f"  Successfully processed and wrote to '{outputFilePath}'.\n")

            except Exception as e:
                traceback.print_exc()
                print(f"Error processing file '{f}': {e}\n")