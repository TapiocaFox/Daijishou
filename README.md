# Daijishō (Emulator frontend)
![](/imgs/cover_new.png)
<a href='https://play.google.com/store/apps/details?id=com.magneticchen.daijishou'><img alt='Get it on Google Play' src='https://cdn.rawgit.com/steverichey/google-play-badge-svg/master/img/en_get.svg' height='70px'/></a>

# Daijishō
Daijishō is a retro launcher that let you manage your retro games libraries. Daijishō cares about integrated experience, expansibility, aesthetic and pragmatical usabilities let you focus on games itself. It will be updated continuously in the future based on users responds and my own retro gaming experience in my free time. Beware it does not come with emulators.

Wat? What does "Daijishō" even mean? You asked. "Daijishō" aka "だいじしょう" actually stands for ["台字章"](https://zh.wikipedia.org/wiki/%E8%87%BA%E7%81%A3%E7%B8%BD%E7%9D%A3%E5%BA%9C%E6%96%87%E5%AE%98%E6%9C%8D%E8%A3%9D) in kanji. Which is a pattern widely used in Taiwan during the Japanese period. Anyway, happy gaming.

### About this Repository
Daijishō is currently **closed-source**. Nonetheless, I do have some prerequisites for open-sourcing it. You can still report issues or submit suggestions here. And Daijishō will always be free!

<!-- ### What's next? (1.4) (Planned to start working on it in 2023)
 - Items set (Merge discs and regions)
 - [Backup](/imgs/1_4_backup.png) and [restore](/imgs/1_4_restore.png) options
 - [Wallpaper](/imgs/1_4_wallpaper.png)
 - Better [settings](/imgs/1_4_settings.png) page and [logger](/imgs/1_4_logger.png) for debugging and [DSESS](/DSESS.md)
 - New [simplified](/imgs/1_4_platforms.png) and [synchronization](/imgs/1_4_synchronization.png) UIs
 - And more... -->
 ### [1.4 (Essential Features Update) Release Note](/release-notes/1_4_release_note.md)


# Make the most of Daijishō
 0. ***Install prefered emulators*** apps first, then Daijishō will select it automatically
 1. ***Setup hotkeys*** for better and intuitive navigation
 2. ***Download and import platforms*** you want
 3. ***Set game files path and sync*** for each platforms
 4. ***Download prefered wallpaper pack*** and ***select prefered theme color*** in settings page
 5. ***Add prefered widgets*** in widget page

Well done. You have now made the most of it. Here are some tips for you.
 - Take a look of [wiki from Jetup13](https://github.com/Jetup13/Retroid-Pocket-2-Plus-Wiki/wiki/Front-Ends#daijishou) or [video from RetroGameCorps](https://www.youtube.com/watch?v=l-AhfEGuMao) might helps.
 - You can long click items to see detail of the item.
 - You can inspect your RetroAchievements records if you login.
 - Switching hotkeys have different abilities in different sections.
 - Be sure to make use of widgets, they are very useful. Like RSS, Activity, Pining games etc.
 - You can update your platforms by re-downloading and re-importing platforms from the list without losing records
 - See "Main features" in Q&A to make sure you don't miss any features!
 - Click Daijishō icon 7 times in about page will enable NSFW mode.

# Quick look of Daijishō
### Is Daijishō a Pegasus fork? (0 of 4)
Nope. But you can import some config for emulators from pegasus.

### Main features (1 of 4)

![](/imgs/widgets_4.png)

(Widgets)

![](/release-notes/1_4_release_note/appearance_general.png)

(Detail view)

![](/imgs/genres_3.png)

(Genres)

![](/imgs/achievement_7.png)

(RetroAchievements)

![](/imgs/search_2.png)

(Search)

And a lot more...

### What is "player" (2 of 4)
Player is a set of arguments can be configured to execute playable files filtered by regular expression from your library with launching arguments. Player usually associated with emulators or retroarch.

### What is "platform" (3 of 4)
Platform contains players added in Daijishō that accepted various files from selected sync paths. Platform also can be configured to scrape correct boxarts and other preview media and to setup to match its appearance and aesthetics.

![](/imgs/platform_collection_wallpaper_view_2.png)

![](/imgs/platform_library_3.png)

### How to add platforms and players (4 of 4)
You can download from this GitHub page which is available in the Daijishō's settings page. Or you can import from pegasus frontend or other's shared and configured platform JSON files. Also you can manually added players then create platform from those players.

![](/imgs/download_platforms_2.png)


# Words from the author
### Before further disscussion
![](/imgs/tapicofox_widgets.png)
> Here is my widgets setup :3
### How much efforts does the author put on this project?
This is a side project. The project solely develop on my retroid pocket 2+ and Android emulators. I will make some progress whenever I feel motivated in my free time usually in the weekend.

### What can you do to support?
You can star this GitHub page, donate, promote Daijishō in the communities or update platform list in this GitHub page.
<!-- You can star this GitHub page, donate, promote Daijishō in the communities, summit your problems and ideas or update platform list in this GitHub page. -->

### Taking a break from the project
Daijishō has evolved a lot in the of 2022. Including UI improvements, retro achievements, wallpaper packs, the new widgets page, genres, backup, merge items and various other small details. I know that there is still room for Daijishō to be grown and things to be improved. And I am thankfully aware of people's ideas and suggestions. However, In the mean time, I also have important things to be done awaiting for me. And its time for me to leave for a while from this repetitive routine for 12 continuous months. Thus, I decided to take a break from the Daijishō project, probably for quarters. With the relatively low attentions and activities focusing on Daijishō. Nevertheless, if you are familiar with Android Kotlin development and you wish to contribute or intergrate features for Daijishō, you can still DM me for the possibilities.


# More about Daijishō
### Documentations
 - [Daijishō Console](/docs/daijishou_console.md)
 - [Daijishō DSESS](/docs/dsess.md)
 - [Daijishō Player Template (.dpt)](/docs/daijishou_player_template.md)

### Related links
 - [Daijishō Discord (Recommended)](https://discord.com/invite/nJbxdT3QQE)
 - [Daijishō YouTube](https://www.youtube.com/channel/UCLdTuA-K8bw4zLczwWwxEaA/featured)
 - [Daijishō EmuGen Wiki](https://emulation.gametechwiki.com/index.php/Daijish%C5%8D)
 - [Daijishō (台字章) History Wikipedia](https://zh.wikipedia.org/wiki/%E8%87%BA%E7%81%A3%E7%B8%BD%E7%9D%A3%E5%BA%9C%E6%96%87%E5%AE%98%E6%9C%8D%E8%A3%9D)

### Supported languages
1. English
2. Portuguese (Português)
3. Taiwanese mandarin (台灣國語)
4. Japanese (日本語)
5. French (Français)
6. Italian (Italiana)
7. Spanish (Español)
8. Korean (한국인)
9. German (Deutsche)
10. Hindi (हिंदी)

### Donation
[PayPal](https://paypal.me/magneticchen)

 (I am taking a break from the project)

<!-- [Patreon](https://www.patreon.com/magneticchen) -->

# Copyright
copyright©2023 TapiocaFox. Designed in Taiwan.
