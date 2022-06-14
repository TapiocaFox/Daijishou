# IGDB Scraper syntax


## Template tags
You have to specify template tags you want to use inside the `TAGS()` brackets. Separated by comma without spaces. It is case sensitive. For example:

`TAGS(scraperKeyword,platformName)`

IGDB scraper string with more tags are recommended to order it at a higher priority position in your platform JSON file. Since it is more specific. However if Daijishō can't provide those tags, the scraper string will be ignored.

In order to use template tags in query. Surround it with curly brackets in query. Like:

`search "{scraperKeyword}";`

`where slug = "{scraperKeyword}";`

## Query
Before further instruction. Make sure to view the [doc](https://api-docs.igdb.com/#examples) from IGDB.

Here is the list of supported methods for querying.

 - search
 - where


## Formats

### Format
`IGDB:GAME:TAGS("template tags"):"query"`

#### description
Used when Daijishō need to get game related info from IGDB. For example scraping for boxarts, descriptions or videos etc. Endpoint the prefix used:

https://api.igdb.com/v4/games

#### template tags
- scraperKeyword
- platformName
- iGDBChecksum (Not yet supported)

#### example
`IGDB:GAME:TAGS(scraperKeyword):where platforms=48; search "{scraperKeyword}";`
