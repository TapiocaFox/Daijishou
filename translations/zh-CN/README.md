# Simplified Chinese localization proposal

This directory proposes `zh-CN` Android resources for Daijishō 1.5.0 (version code 416). The public repository does not contain the application source or its Android resource source tree, so these files are supplied for maintainer review and integration into the private application project. Adding them here alone will not change a released application.

## Resources

- `values-zh-rCN/strings.xml`: 898 strings: 894 application strings and 4 generic component labels. This includes 150 additions to the previous Traditional Chinese inventory, covering extension/recovery text, the accessibility service description, implementation selection, and component labels.
- `values-zh-rCN/arrays.xml`: 3 translated arrays, containing 18 options in the original order.
- `format-placeholders.json`: expected Java/Android formatting tokens per string, for validation without distributing original application code.
- `validate.py`: checks XML, unique resource names, string inventory, format tokens, and array lengths using Python's standard library.

The initial text was adapted from the existing Traditional Chinese localization credited to TapiocaFox. Character conversion was followed by terminology review and manual revisions to 172 strings. Terms are consistent with the launcher's behavior: Library → 游戏库, Player → 启动器, Widgets → 组件, Paths → 文件夹. Incorrect genre translations, snapshot/title import labels, shortcut instructions, and destructive-action descriptions have also been corrected in this proposed locale. Existing Traditional Chinese resources are left unchanged.

Product names, URLs, command names, regular-expression examples, `{file.path}` / `{file.uri}` templates, and format-token types and order are preserved. `Player` here refers to a launch configuration; emulator names and actual RetroAchievements players are not renamed.

## Integration

Copy the XML files into the application's `res/values-zh-rCN/` directory, merging with any library-provided or existing localized resources. If the application explicitly selects a script-based locale, the same application translations can also be supplied under `values-b+zh+Hans`. Keep the default resources as the fallback.

Run `python translations/zh-CN/validate.py` to verify the proposed resources. Build and exercise the real application with `zh-Hans-CN` / `zh-CN` after integration. Please adjust the staging location if the private project uses a different localization workflow.

## Local validation

Formatting placeholders were compared against the default English resources of the installed 1.5.0 application. The XML compiled with Android's resource compiler as part of a local APK resource rebuild. On an Odin2 running Android 13 with a Simplified Chinese system locale, the main library, settings, folder permissions, and launch confirmation displayed Simplified Chinese. An existing 16-platform, 550-item library with cover images was preserved in the local test installation. Game launch handoffs passed for GBA Pokémon Ruby (RetroArch/mGBA), NDS Pokémon HeartGold (melonDS), and 3DS Pokémon Omega Ruby (AzaharPlus). These were boot/title-screen checks, not full gameplay compatibility tests.

A follow-up inventory comparison against the installed 1.5.0 default resources found and filled two omitted application labels and four generic component labels. Of the 1,136 default string keys, this proposal covers 898; 186 additional library strings already have Simplified Chinese resources in the application, and the remaining 52 are technical constants (class names, font names, animation/vector paths, separators, and numeric formatting templates) that should not be translated. This is a resource inventory check, not a claim that every runtime message or future release is translated.

The resource-only local test build retained all six original executable DEX files byte-for-byte. Some strings embedded in application code remain outside the scope of this resource proposal. A maintainer build from the private application source is still required for an official release.

Only the proposed localization and its validation data are included here. No APKs, signing keys, decompiled application code, game files, or user configuration are included. The application remains closed-source, and this proposal makes no claim about a license for its binary.
