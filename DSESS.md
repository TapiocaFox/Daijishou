# Daijishō Search Engine Scraper Syntax (DSESS)

DSESS uses search engine URL to obtain target sites. Then use the CSS selector syntax to acquire wanted sources.

## Preknowledges
### CSS selector
Before further instruction. Make sure to view the [doc](https://jsoup.org/cookbook/extracting-data/selector-syntax) from JSoup.

### URL Query string
Query string is a part of a URL that assigns values to specified parameters. Which is useful for search engine.
Your parameters have to be encoded as [URL encode/decode](https://www.url-encode-decode.com/) and [URL encoded string](https://www.urlencoder.org/)

### Regex
See https://regex101.com/.

## Overview
DSESS has below format.

`Headers` + `:` + `Template tags` + `:` + `DSESS URL`

## Headers
`DSESS:` + scraper target

`DSESS:BOX_ART`

`DSESS:SNAPSHOT`

`DSESS:TITLE`

`DSESS:YOUTUBE`

`DSESS:DESCRIPTION`

## Template tags
You have to specify template tags you want to use inside the `TAGS()` brackets. Separated by comma without spaces. It is case sensitive. For example:

`TAGS(scraperKeyword,platformName)`

DSESS string with more tags are recommended to order it at a higher priority position in your platform JSON file. Since it is more specific. However if Daijishō can't provide those tags, that scraper string will be ignored.

In order to use template tags in query. Surround it with curly brackets in query. Like:

`PlayStationPortable {scraperKeyword}` `q={scraperKeyword}&hl={localeLanguage}` `query={scraperKeyword}`

Encoded as

`PlayStationPortable+%7BscraperKeyword%7D` `q=%7BscraperKeyword%7D&hl=%7BlocaleLanguage%7D` `query=%7BscraperKeyword%7D`

### Template tags
- scraperKeyword
- platformName, like `DOOM Game Engine`
- localeLanguage, like `en-US` `zh-TW`


## DSESS URL
DSESS URL contains **The body URL** and several **URL parameters**.

### 0. The body URL
The body URL contains the search engine HTTPS URL with template tags. The template tags will apply for each URL parameter be analyzed. And DSESS defined parameters will be extracted and removed before HTTPS request. For example:

`https://www.google.com/search?q=%7BscraperKeyword%7D&hl=%7BlocaleLanguage%7D&tbm=isch`

You can see  `{scraperKeyword}` is encoded as `%7BscraperKeyword%7D`. So do `{localeLanguage}`.

All parameters **must be translated to URL query encoded string**. Concatenate by URL parameters rules.
With following DSESS URL parameters. The parameters is processed below order.

### 1. Target site Regex parameter
`dsess_target_site=` + Target site Regex.

For example: `^https:\/\/www.romspedia.com\/roms\/.*$`.
And don't forget to **translate the Regex to URL encoded query string** like others parameters.

Encoded as: `%5Ehttps%3A%5C%2F%5C%2Fwww.romspedia.com%5C%2Froms%5C%2F.%2A%24`.

It will matches all links available from search results from search engine. And if matched, the first matched by "**1.Target site Regex**"  will be used by "**2.selector parameter**" in next process.

If `dsess_target_site` is not present. The search engine site itself will be used by **2.selector parameter**'s CSS selector.

### 2. Selector parameter
`dsess_selector=` + CSS selector.

When target site is available, the selector parameter will be applied on target site.

### 3. Attribute parameter
`dsess_attribute=` + Attribute you want from the element selected by CSS selector.

For example `href` for `<a>` element.
If `dsess_attribute` is not present the innerHTML will be resolved.

## Examples
<!-- `DSESS:BOXART:TAGS("template tags"):"DSESS URL"` -->
