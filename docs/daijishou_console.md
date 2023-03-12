# 💻 Daijishō Console

## ⚠️ Before Enabling Console
 - You better have some basic programming knowledges before you decide to use console.
 - App can be unstable. Which can ruin your experience.
 - Your data might be lost and gone forever because of the command.
 - You have to be aware and responsible for your decision.

## Enable Console
Type `\debug on` in your the logger.

![](/imgs/daijishou_console.png)

## Learn More About Console
Type `\help` in your the logger.

### Notes
 - `\prefs` let you view and modify preferences.
 - `\am_start` command can be used by emulator dev to check if Daijishō can launch items via Daijishō to emulator app.
 - `\dsess` command can be used to check whether the site can be used by Daijishō [DSESS](\docs\DSESS.md) scraper.

## Hidden Preferences For `\prefs` Command

| Key | Data Type | Description  |
|---|---|---|
| `force_set_wallpaper_for_all` | Boolean | Set wallpaper for every pages if `true`. It is for cosmetic uses. |
| `hide_platforms_page_subtitle` | Boolean | Hide platforms page subtitle if `true`. It is for cosmetic uses. |
| `enable_non_home_activity` | Boolean | Enable non home activity of Daijishō if `true`. For Android 13 Dex users. |
| `disable_widgets_page` | Boolean | Disable widgets page if `true`. |
| `use_pure_dark_theme` | Boolean | Use pure dark theme if `true`. For OLED devices.|
| `use_lightweight_backup` | Boolean | Skip backups like images `true`.|
| `scale_ui` | String | Scale your UI. For example `1.25`.|

