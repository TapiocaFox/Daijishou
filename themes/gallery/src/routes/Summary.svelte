<script>
	export let item;
</script>

<article>
	<h2><a href=#/theme/{item.platformWallpapersPackRootPath}>
       <img src="{window.baseUri}{item.platformWallpapersPackPreviewThumbnailPath}" alt="{item.platformWallpapersPackName}"/>
	{item.platformWallpapersPackName}</a></h2>
	<p>{item.platformWallpapersPackDescription}</p>
   <p class="meta">by {item.platformWallpapersPackAuthors}</p>
</article>

<style>
	article {
		position: relative;
		padding: 0 0 0 2em;
		border-bottom: 1px solid #eee;
	}

	h2 {
		font-size: 1em;
		margin: 0.5em 0;
	}

	a {
		color: #333;
	}
	
	img {
		width: 64px;
	}
</style>
