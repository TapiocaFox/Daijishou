<script>
	import { onMount } from 'svelte';
	import { goto } from '$app/navigation';
	import { rawSourceUri } from '../../constants';
	import WallpapersPackDetail from './WallpapersPackDetail.svelte';

 	/** @type {import('./$types').PageData} */
	// export let data;
	let index = {
		name: null,
		description: "Loading…",
		wallpaperList: [],
		authors: [],
		sources: []

	};
	let slug;
	
	onMount(async() => {
		let hash = window.location.hash;
		if(hash) {
			slug = hash.substring(1)
			try {
				index = await fetch(`${rawSourceUri}/themes/platform_wallpapers_packs/${slug}/index.json`).then(r => r.json());
			} catch (error) {
				console.error(error);
				goto("/")
			}
		}
		else {
			goto("/")
		}
	});
	
</script>

<svelte:head>
	{#if index.name}
		<title> {index.name} </title>
	{/if}
</svelte:head>

{#if index}
	<WallpapersPackDetail index={index} slug={slug}/>
{/if}
