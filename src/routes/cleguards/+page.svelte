<script>
  import { onMount } from 'svelte';

  onMount(() => {
    document.body.classList.add('hammy-page');
    return () => document.body.classList.remove('hammy-page');
  });

  const title = "WORTH IT";
  const tagline = "go back to Argentina";

</script>

<svelte:head>
  <title>{title}</title>
  <meta name="description" content={tagline} />
  <link rel="stylesheet" href="/styles.css" />
</svelte:head>

<div class="hammmy">
  <h1>{title}</h1>
  <p>{tagline}</p>
</div>