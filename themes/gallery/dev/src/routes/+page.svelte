<script>
	import { onMount } from 'svelte';
	import List from './List.svelte';
	import Item from './Item.svelte';

	let item;
	var baseUri;
	var id;
	
	async function hashchange() {
		// the poor man's router!
		const path = window.location.hash.slice(1);

		if (path.startsWith('/theme')) {
			window.id = path.slice(6);
			item = await fetch(`../platform_wallpapers_packs/${window.id}`).then(r => r.json());

			window.scrollTo(0,0);
		} else if (path.startsWith('/')) {
			item = null;
			window.id = null;
		}
	}

	onMount(hashchange);
</script>

<svelte:window on:hashchange={hashchange}/>

<main>
	{#if item}
		<Item {item} returnTo="#/top/"/>
	{:else }
		<List/>
	{/if}
</main>

<style>
	main {
		position: relative;
		max-width: 800px;
		margin: 0 auto;
		min-height: 101vh;
		padding: 1em;
      color: white;
      background-color: rgb(24, 24, 24);
      font-family: "Overpass", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen, Ubuntu, Cantarell, "Fira Sans", "Droid Sans", "Helvetica Neue", sans-serif;
	}

	main :global(.meta) {
		color: #999;
		font-size: 12px;
		margin: 0 0 1em 0;
	}

	main :global(a) {
		color: fuchsia;
	}
</style>