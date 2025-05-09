<script>
  import { onMount } from 'svelte';

  onMount(() => {
    document.title = "A Major | Rain Harder";
  });

  onMount(() => {
    document.body.classList.add('amajor-page');
  });
</script>

<svelte:head>
  <title>A Major | Rain Harder</title>
  <link rel="stylesheet" href="/styles.css">
</svelte:head>

<div class="container">
  <h1>A Major</h1>
  <p>we'll fill this out with proper words and styling, also  for h1</p>

  <p>(the proper quote, like extreme ownership but better. ooda loops. the hard thing about hard things)</p>
</div>


