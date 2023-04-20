<script>
	// import { useNavigate } from "svelte-navigator";
	import { rawSourceUri } from '../../constants';
	export let index;
	export let slug;
	// const navigate = useNavigate();
	function onBackClick() {
		// const ref = document.referrer;
  		// goto(ref.length > 0 ? ref : "/")
		// alert()
		// goto("/")
		// navigate(-1)
		history.back()
	}
</script>

<article>
	<p><a on:click={onBackClick}>&laquo; back to list</a></p>
    <img class="thumb" src="{rawSourceUri}/themes/platform_wallpapers_packs/{slug}/{index.previewThumbnailFilename}" alt="{index.platformWallpapersPackName}"/>
    <h1>{index.name}</h1>
	<p>Has default wallpaper: {index.hasDefaultWallpaper? "yes" : "no"}{index.isNSFW?" • NSFW":""}</p>
	<p>{index.description}</p>
	<p class="authors">Authors: {index.authors.join(", ")}.<br>Sources: {index.sources.join(", ")}.</p>
</article>

<div class="wallpapers">
	{#if index.hasDefaultWallpaper}
		<h2>default</h2>
		<a href={rawSourceUri}/themes/platform_wallpapers_packs/{slug}/{index.defaultWallpaperFilename} target="_blank" >
			<img class="wallpaper" src="{rawSourceUri}/themes/platform_wallpapers_packs/{slug}/{index.defaultWallpaperFilename}" alt="default" />
		</a>
		<span class="filename">{index.defaultWallpaperFilename}</span>
	{/if}
	{#each index.wallpaperList as wallpaperMeta}
		<h2>{wallpaperMeta.matchPlatformShortname}</h2>
		<a href={rawSourceUri}/themes/platform_wallpapers_packs/{slug}/{wallpaperMeta.filename} target="_blank" >
			<img class="wallpaper" src="{rawSourceUri}/themes/platform_wallpapers_packs/{slug}/{wallpaperMeta.filename}" alt="{wallpaperMeta.matchPlatformShortname}" />
		</a>
		<span class="filename">{wallpaperMeta.filename}</span>
	{/each}
</div>

<style>
	article {
		padding: 12px 32px 12px 32px;
		border-bottom: 1px solid gray;
	}
	div.wallpapers {
		padding: 0 32px 12px 32px;
		/* box-sizing: border-box; */
	}
	img.wallpaper {
		max-width: 800px;
		width: 100%;
		border-radius: 8px;
	}

	img.thumb {
		height: 128px;
		width: 128px;
		border-radius: 8px;
		box-shadow: 0 3px 8px 0 rgba(0, 0, 0, 0.25), 0 3px 20px 0 rgba(0, 0, 0, 0.19);
		object-fit: cover;
	}

	span.filename {
		color: gray;
		font-size: small;
	}
</style>
