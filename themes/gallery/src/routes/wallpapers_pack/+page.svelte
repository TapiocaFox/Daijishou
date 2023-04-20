<script>
	import { onMount } from 'svelte';
	import { goto } from '$app/navigation';
	import { rawSourceUri } from '../../constants';
	import WallpapersPackDetail from './WallpapersPackDetail.svelte';

 	/** @type {import('./$types').PageData} */
	// export let data;
	let index;
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
	{#if index}
		<title> {index.name} </title>
	{/if}
</svelte:head>

{#if index}
	<WallpapersPackDetail index={index} slug={slug}/>
{/if}
