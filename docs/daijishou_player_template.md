# Daijishō Player Template
## What is Daijishō Player Template
Daijishō Player Template File is a file that can be treated as playable item. And apply player template values to tags when you play the file, based on how you define the template file.

## Why Daijishō Player Template

### Tasker
Say that you want to launch `exampleTask` of Tasker in Daijishō. You can do this by setting players' `am start arguments` with template tags, and create `.dpt` files with tags names and values.

Player Am Start Arguments:

 `-n ... --es task_name {tags.task_name}`

And with the Daijishō player template file (Like `exampleTask.dpt`):
```
# Daijishou Player Template
[task_name] exampleTask
...
```

### Vita3k
Daijishō Player Template can possiblly be used to solve the PS Vita3k issues. With below settings.

Player Am Start Arguments:

`-n org.vita3k.emulator/org.vita3k.emulator.Emulator -e launch {tags.vita_game_id}`

or

`-n org.vita3k.emulator/org.vita3k.emulator.Emulator --esa "AppStartParameters" "-r","{tags.vita_game_id}"`

Then in Daijishou player template file for `Golden Abyss` (For example `Golden Abyss.dpt`):
```
# Daijishou Player Template
[vita_game_id] PCSF00001
...
```

With above settings `{tags.vita_game_id}` will be replaced with `PCSF00001` defined in `Golden Abyss.dpt`.

## Notes
 - The Daijishō Player Template File has the extension `.dpt`. 
 - The first line of the file must be `# Daijishou Player Template` or `# DST` so that Daijishō can recognized the format and apply template.
