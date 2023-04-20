<script>
	export let item;
	export let returnTo;
</script>

<a href={returnTo}>&laquo; back</a>

<article>
   <img class="thumb" src="{window.baseUri}{window.id}/{item.previewThumbnailFilename}" alt="{item.platformWallpapersPackName}"/>
   <h1>{item.name}</h1>
	<p>{item.description}</p>
	<p class="meta">by {item.authors}
</article>

<div class="art">
	{#each item.wallpaperList as image}
		<h3>{image.matchPlatformShortname}</h3>
		<a href={window.baseUri}{window.id}/{image.filename} target="_blank" >
           <img src="{window.baseUri}{window.id}/{image.filename}" alt="{image.matchPlatformShortname}" /></a>
	{/each}
</div>

<style>
	article {
		margin: 0 0 1em 0;
	}

	a {
		display: block;
		margin: 0 0 1em 0;
	}

	h1 {
		font-size: 1.4em;
		margin: 0;
	}
	
	img {
		max-width: 800px;
	}

   img.thumb {
		height: 64px
	}
</style>
