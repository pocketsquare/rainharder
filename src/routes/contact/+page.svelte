<script lang="ts">
  import { onMount } from 'svelte';

  let name: string = '';
  let email: string = '';
  let subject: string = '';
  let message: string = '';

  const submitForm = (): void => {
    console.log({ name, email, subject, message });
    window.location.href = '/confirmation';
  };

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

  <form class="form" on:submit|preventDefault={submitForm}>
    <div class="form-group">
      <label for="name">Name</label>
      <input id="name" type="text" bind:value={name} maxlength="50" required />
    </div>

    <div class="form-group">
      <label for="email">Email</label>
      <input id="email" type="email" bind:value={email} maxlength="50" required />
    </div>

    <div class="form-group">
      <label for="subject">Subject</label>
      <input id="subject" type="text" bind:value={subject} maxlength="50" required />
    </div>

    <div class="form-group">
      <label for="message">Message</label>
      <textarea id="message" bind:value={message} maxlength="250" required></textarea>
    </div>

    <button type="submit">E.T. PHONE HOME</button>
  </form>
</div>
