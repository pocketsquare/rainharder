<script lang="ts">
  import { onMount } from 'svelte';
  import { PUBLIC_API_URL } from '$env/static/public';

  let name = "";
  let email = "";
  let subject = "";
  let message = "";

onMount(() => {
  document.body.classList.add('contact-page');
  
  return () => document.body.classList.remove('contact-page');
});

  async function submitForm() {
    const response = await fetch(`${PUBLIC_API_URL}/email/send`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ name, email, subject, message }),
    });

    const contentType = response.headers.get("content-type");
    if (contentType && contentType.includes("application/json")) {
      const result = await response.json();
      if (response.ok) {
        window.location.href = '/confirmation';
      } else {
        alert(`Error: ${result.detail || "Unknown error."}`);
      }
    } else {
      const text = await response.text();
      alert(`Unexpected response: ${text}`);
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
