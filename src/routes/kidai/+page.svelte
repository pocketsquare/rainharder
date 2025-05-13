<script>
  import { onMount } from 'svelte';

  const title = "Subtractive Capability";
  const tagline = "Adventures in the Skein Trade";

  onMount(() => {
    document.body.classList.add('kidai-page');
    return () => {
      document.body.classList.remove('kidai-page');
    };
  });
</script>

<svelte:head>
  <title>{title}</title>
  <meta name="description" content={tagline} />
  <link rel="stylesheet" href="/styles.css" />
</svelte:head>

<div class="kidai-container">
  <h1>{title}</h1>
  <p>{tagline}</p>

  <section class="ai-bros">
    <div class="ai-bros-list">
      <div class="ai-bro-item">
        <div class="provider">ChatGPT</div>
        <div class="description">Sammy Buckets</div>
      </div>
      <div class="ai-bro-item">
        <div class="provider">Claude</div>
        <div class="description">Claude Baudelaire</div>
      </div>
      <div class="ai-bro-item">
        <div class="provider">Grok</div>
        <div class="description">SuperGrok Pot</div>
      </div>
      <div class="ai-bro-item">
        <div class="provider"><a href="https://mistral.ai" target="_blank" rel="noopener noreferrer">Mistral</a></div>
        <div class="description">LePen is</div>
      </div>
      <div class="ai-bro-item">
        <div class="provider">Meta</div>
        <div class="description"></div>
      </div>
      <div class="ai-bro-item">
        <div class="provider">Gemini</div>
        <div class="description">Cardinal Sundar</div>
      </div>
      <div class="ai-bro-item">
        <div class="provider">Perplexity</div>
        <div class="description">Pets.com</div>
      </div>
    </div>
  </section>
</div>
