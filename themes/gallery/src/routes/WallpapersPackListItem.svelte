<script>
	export let item;
</script>

<article>
	<img class="thumbnail" src="{window.baseUri}{item.platformWallpapersPackPreviewThumbnailPath}" alt="{item.platformWallpapersPackName}"/>
	<h2><a href=/wallpapers_pack/#{item.platformWallpapersPackRootPath}>{item.platformWallpapersPackName}</a></h2>
	<p>{item.platformWallpapersPackDescription}</p>
   	<p class="authors">Author(s): {item.platformWallpapersPackAuthors.join(", ")}</p>
</article>

<style>
	a {
		color: white;
	}
	img.thumbnail {
		object-fit: cover;
		width: 72px;
		height: 72px;
		margin-top: 12px;
		border-radius: 8px;
		box-shadow: 0 2px 2px 0 rgba(0,0,0,0.14), 0 3px 1px -2px rgba(0,0,0,0.12), 0 1px 5px 0 rgba(0,0,0,0.2);
	}
	article {
		position: relative;
		padding: 12px 32px 12px 32px;
	}
	article:not(:last-child) {
		border-bottom: 1px solid gray;
	}
	
</style>
