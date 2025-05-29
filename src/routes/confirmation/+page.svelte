<script>
  import { onMount } from 'svelte';
  onMount(() => {
    document.body.classList.add('confirmation-page');
    return () => {
      document.body.classList.remove('confirmation-page');
    };
  });
</script>

<svelte:head>
  <title>Eye Contact | Rain Harder</title>
  <link rel="stylesheet" href="/styles.css">
</svelte:head>

<div class="container">
  <h1>Message Sent!</h1>
  <p>Your message has been successfully submitted.</p>
</div>
