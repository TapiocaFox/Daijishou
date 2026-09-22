# OpenBOR in Daijishō

OpenBOR (Open Beats of Rage) runs fan-made brawlers such as the X-Men arcade remakes, Streets of Rage Z and Final Fight LNS. Each game ships as one `.pak` file. This page covers the `OpenBOR` platform in `platforms/OpenBOR.json`, the engine build it needs, and how to give the games library art when no cover exists.

## Why the stock engine is not enough

The official OpenBOR Android APK starts with its own file picker and then a mod-select menu. It ignores every launch argument, so Daijishō cannot hand it a pak. On Android 11 and later the engine also lacks the storage permission it would need to open a pak outside its private folder.

`docs/openbor/openbor-frontend-launch.patch` fixes both against OpenBOR tag `v7533` (engine 4.0 build 7533):

- `engine/sdl/sdlport.c`: before the engine falls back to its menu, it reads the string extra `pak` from the launching Intent through JNI. If that path exists, the engine loads it and skips the menu.
- `engine/sdl/sdlport.c`: the legacy `/mnt/sdcard/OpenBOR` branch is disabled, so saves and logs always live in `Android/data/org.openbor.engine/files`.
- `AndroidManifest.xml`: declares `MANAGE_EXTERNAL_STORAGE` ("All files access"), which Android needs before it lets the engine read your ROM folders.

## Build the engine

1. `git clone https://github.com/DCurrent/openbor && cd openbor && git checkout v7533`
2. `git apply /path/to/openbor-frontend-launch.patch`
3. Build `engine/android` as the OpenBOR README describes (Gradle, or `ndk-build` inside `engine/android/app/jni` for arm64 only).
4. Sign the APK with your own key and install it. Later updates keep saves as long as you sign with the same key.

After the install, grant the storage permission once. Either open Android Settings › Apps › OpenBOR › "All files access", or over adb:

```
adb shell pm grant org.openbor.engine android.permission.READ_EXTERNAL_STORAGE
adb shell appops set org.openbor.engine MANAGE_EXTERNAL_STORAGE allow
```

Check a game from the shell before you touch Daijishō. This command must show the game's title screen, not the OpenBOR menu:

```
adb shell am start -n org.openbor.engine/.GameActivity -e pak "/storage/emulated/0/Games/openbor/Game.pak"
```

If you land in the menu, the engine could not read the file. `appops get org.openbor.engine` tells you whether Android revoked the permission; a `rejectTime` in that output means a system dialog denied it.

## Set up the platform

1. Import `OpenBOR.json` from the platform list.
2. Add the folder that holds your `.pak` files as a sync path and sync.
3. Play a game. Daijishō runs `am start -n org.openbor.engine/.GameActivity -e pak {file.path}`. The engine gets the plain file path, so the pak folder must be readable by the engine: internal storage or a physical SD card both work, but not another app's private folder.

Two paks with the same name in different folders confuse the engine's save files, which it names after the pak. Keep names unique.

## Library art

OpenBOR games have no box art anywhere; scrapers return nothing or the wrong game. The paks carry their own title screens at `data/bgs/title.gif` (`titleb.gif` is the "press start" variant). `docs/openbor/pak-title.sh` pulls that image straight from a pak on the device, reading only the file table and the one image, so a 2 GB pak costs a few seconds:

```
docs/openbor/pak-title.sh "/storage/emulated/0/Games/openbor/Game.pak" out/
```

Use the result as the game's box art. The platform ships with a custom box art ratio of 4:3 so the title screens keep their proportions in the library. Title screens come in several sizes (320x240, 396x224, 480x272, 960x480); pad the wider ones to 4:3 with black bars instead of scaling, then they line up on the grid.

To install the art without the scraper, put `title.png` in `files/preview_media/<item id>/` inside Daijishō's data folder and point `boxArtPath` at it in that folder's `index.json`. The three keys `boxArtPath`, `snapshotPath` and `titlePath` must all be present; use `null` for a slot you do not fill.

## Tested on

Anbernic RG405M (Unisoc T618, Android 12), Daijishō 1.8.1, OpenBOR 4.0 build 7533 with the patch, 19 paks between internal storage and an exFAT SD card. Every game starts from the Daijishō Play button into its own title screen.
