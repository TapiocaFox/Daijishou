# Daijishō Search Engine Scraper Syntax (DSESS)

DSESS uses search engine URL to obtain target sites. Then use the CSS selector syntax to acquire wanted sources.

## Template tags
You have to specify template tags you want to use inside the `TAGS()` brackets. Separated by comma without spaces. It is case sensitive. For example:

`TAGS(scraperKeyword,platformName)`

DSESS string with more tags are recommended to order it at a higher priority position in your platform JSON file. Since it is more specific. However if Daijishō can't provide those tags, that scraper string will be ignored.

In order to use template tags in query. Surround it with curly brackets in query. Like:

`PlayStationPortable "{scraperKeyword}";`

## CSS selector
Before further instruction. Make sure to view the [doc](https://jsoup.org/cookbook/extracting-data/selector-syntax) from JSoup.

## Query string
Query string is a part of a URL that assigns values to specified parameters. Which is useful for search engine.
Your parameters have to be encoded as [URL encoded string](https://www.urlencoder.org/)

## Regex
See https://regex101.com/.

## DSESS URL
DSESS URL including below parts and parameters.

### The body URL
The body URL contains the search engine HTTPS URL with template tags. The template tags will apply immediately before the URL parameters be analyzed. For example:

`https://www.google.com/search?q={scraperKeyword}&hl={localeLanguage}&tbm=isch`

Concat with following arguments.
All arguments must be translated to URL encoded string.

### Target site regex argument
`dsess_target_site=` + Target site regex. For example:
`^https:\/\/www.romspedia.com\/roms\/.*$`

And don't forget to translate it to URL encoded string like others arguments.

#### Selector argument
`dsess_selector=` + CSS selector.

When available the selector argument will be applied on target site.

#### Attribute argument
`dsess_attribute=` + Attribute you want from element selected by selector.

For example `href` for `<a>` element.
If `dsess_attribute` is not present the innerHTML will be resolved.


## Headers
`DSESS:BOXART:TAGS("template tags")`

`DSESS:TITLE:TAGS("template tags")`

`DSESS:SNAPSHOT:TAGS("template tags")`

`DSESS:YOUTUBE:TAGS("template tags")`

`DSESS:DESCRIPTION:TAGS("template tags")`

## Format summed up
`DSESS:BOXART:TAGS("template tags"):"DSESS URL"`

#### description


#### template tags
- scraperKeyword
- platformName
- localeLanguage

#### example
`DSESS:BOXART:TAGS("template tags"):"DSESS URL"`

`DSESS:TITLE:TAGS("template tags"):"DSESS URL"`
