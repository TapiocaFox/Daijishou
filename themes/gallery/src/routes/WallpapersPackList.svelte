<script>
    import { onMount } from 'svelte';
    import { rawSourceUri } from '../constants';
	import WallpapersPackListItem from "./WallpapersPackListItem.svelte";

	let items;
    onMount(async () => {
   	fetch(`${rawSourceUri}/themes/platform_wallpapers_packs/index.json`)
   		.then(r => r.json())
   		.then(data => {
   			items = data.platformWallpapersPackList;
   			window.baseUri = data.baseUri;
   			window.scrollTo(0, 0);
   		});
    });
</script>

{#if items}
	{#each items as item}
		<WallpapersPackListItem {item} />
	{/each}
{:else}
	<p class="loading">Loading...</p>
{/if}

<style>
	p.loading {
		padding: 12px 24px 12px 24px;
	}
</style>