<script lang="ts">

  import { onMount } from 'svelte';

  onMount(() => {
    document.body.classList.add('contact-page');
    return () => {
      document.body.classList.remove('contact-page');
    };
  });

</script>

<svelte:head>
  <title>Eye Contact | Rain Harder</title>
  <link rel="stylesheet" href="/styles.css">
</svelte:head>

<div class="container"> 
  <h1>Eye Contact</h1>
  <p>placeholder</p>
</div>