<script lang="ts">
  import { onMount } from 'svelte';

  let name = "";
  let email = "";
  let subject = "";
  let message = "";

  onMount(() => {
    document.body.classList.add('contact-page');
  });

  async function submitForm() {
    const apiUrl = import.meta.env.PUBLIC_API_URL; // Load from .env
    const response = await fetch(`${apiUrl}/email/send`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ name, email, subject, message }),
    });

    if (response.ok) {
      window.location.href = '/confirmation';
    } else {
      const errorData = await response.json();
      alert(`Error: ${errorData.detail || 'There was a problem sending your message.'}`);
    }
  }
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
      <input id="name" type="text" bind:value={name} required />
    </div>
    <div class="form-group">
      <label for="email">Email</label>
      <input id="email" type="email" bind:value={email} required />
    </div>
    <div class="form-group">
      <label for="subject">Subject</label>
      <input id="subject" type="text" bind:value={subject} required />
    </div>
    <div class="form-group">
      <label for="message">Message</label>
      <textarea id="message" bind:value={message} required></textarea>
    </div>
    <button type="submit">E.T. PHONE HOME</button>
  </form>
</div>