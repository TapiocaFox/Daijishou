<script>
   import { onMount } from 'svelte';
	import { beforeUpdate } from "svelte";
	import Summary from "./Summary.svelte";

	let items;
    onMount(async () => {
   	fetch(`../platform_wallpapers_packs/`)
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
		<Summary {item} />
	{/each}
{:else}
	<p class="loading">loading...</p>
{/if}

<style>

	.loading {
		opacity: 0;
		animation: 0.4s 0.8s forwards fade-in;
	}

	@keyframes fade-in {
		from { opacity: 0; }
		to { opacity: 1; }
	}
</style>