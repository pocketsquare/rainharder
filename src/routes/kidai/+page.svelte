```svelte
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

<style>
  @font-face {
    font-family: 'BD Plakatbau';
    src: url('/fonts/bd-plakatbau.ttf') format('truetype');
    font-weight: normal;
    font-style: normal;
    font-display: swap;
  }

  .kidai-container {
    font-family: 'BD Plakatbau', sans-serif;
    font-weight: normal;
    max-width: 900px;
    padding: 2rem;
    margin: 0 auto;
    box-sizing: border-box;
    border-radius: 0;
    overflow: visible;
  }

  h1 {
    font-family: 'BD Plakatbau', sans-serif;
    font-weight: normal;
    font-size: 3rem;
    margin-bottom: 1rem;
    margin-top: -1rem;
  }

  p {
    font-family: 'BD Plakatbau', sans-serif;
    font-size: 1.5rem;
    line-height: 1.6;
    margin-bottom: 1.5rem;
  }

  .ai-bros-list {
    display: flex;
    flex-direction: column;
    gap: 1.5rem;
  }

  .ai-bro-item {
    padding: 0.5rem;
    border-radius: 0;
    display: flex;
    align-items: baseline;
  }

  .provider {
    flex: 1;
    text-align: left;
    font-weight: normal;
    margin: 0;
    line-height: 1.2;
  }

  .description {
    flex: 1;
    text-align: left;
    font-weight: normal;
    margin: 0;
    line-height: 1.2;
  }

  @media (max-width: 768px) {
    .kidai-container {
      padding: 1.5rem;
      width: 100%;
    }

    h1 {
      font-size: 2rem;
    }

    p {
      font-size: 1.1rem;
    }

    .ai-bro-item {
      flex: 1 1 100%;
    }
  }

  @media (max-width: 480px) {
    .kidai-container {
      padding: 1rem;
    }

    h1 {
      font-size: 1.75rem;
    }

    p {
      font-size: 1rem;
    }
  }
</style>

<div class="kidai-container">
  <h1>{title}</h1>
  <p>{tagline}</p>

  <section class="ai-bros">
    <div class="ai-bros-list">
      <div class="ai-bro-item">
        <div class="provider">ChatGPT</div>
        <div class="description">
          <a href="/pdfs/Sammy_Buckets_Misses.pdf" target="_blank" rel="noopener noreferrer">Sammy Buckets</a>
        </div>
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
        <div class="description"> </div>
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
```