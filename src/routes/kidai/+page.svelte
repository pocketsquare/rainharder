```svelte
<script>
  import { onMount } from 'svelte';

  const title = "SUBTRACTIVE CAPABILITY";
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
    margin-top: -1.3rem;
    box-sizing: border-box;
    border-radius: 0;
    overflow: visible;
  }


  h1 {
    font-family: 'BD Plakatbau', sans-serif;
    font-weight: normal;
    font-size: 5rem;
    margin-bottom: 1rem;
    margin-top: -1rem;
  }

  p {
    font-family: 'BD Plakatbau', sans-serif;
    font-size: 2.2rem;
    line-height: 1.6;
    margin-bottom: 1.5rem;
  }

  .ai-bros-list {
    display: flex;
    flex-direction: column;
  }

  .ai-bro-item {
    display: flex;
    margin-bottom: 10px;
    font-size: 18px;
  }

  .provider {
    flex: 1;
    text-align: left;
    font-weight: normal;
    font-size: 2.2rem;
    margin: 0;
    line-height: 2;
  }

  .description {
    flex: 1;
    text-align: left;
    font-weight: normal;
    font-size: 2.2rem;
    margin: 0;
    line-height: 2;
  }

  @media (max-width: 768px) {
  .provider,
  .description {
    font-size: 1.4rem; /* Change from 1.25rem */
  }

    h1 {
      font-size: 2.5rem;
    }

    p {
      font-size: 1.5rem;
    }

    .ai-bro-item {
      display: flex;
      flex-direction: row !important;
      margin-bottom: 10px;
      font-size: 16px;
    }

    .provider,
    .description {
      flex: 1;
      text-align: left !important;
      font-size: 1.25rem;
    }
  }

  @media (max-width: 480px) {
  .provider,
  .description {
    font-size: 1.1rem; /* Change from 1rem */
  }

    h1 {
      font-size: 2rem;
    }

    p {
      font-size: 1.25rem;
    }

    .ai-bro-item {
      display: flex;
      flex-direction: row !important;
      margin-bottom: 10px;
    }

    .provider,
    .description {
      flex: 1;
      text-align: left !important;
      font-size: 1rem;
    }
  }
</style>

<div class="kidai-container">
  <h1>{title}</h1>
  <p><a href="/wolfram-alpaca.png" target="_blank" rel="noopener noreferrer">{tagline}</a></p>

  <section class="ai-bros">
    <div class="ai-bros-list">
      <div class="ai-bro-item">
        <div class="provider">ChatGPT</div>
        <div class="description">
          <a href="/pdfs/Sammy_Buckets_Misses.pdf" target="_blank" rel="noopener noreferrer">Sammy Buckets</a>
        </div>
      </div>
      <div class="ai-bro-item">
        <div class="provider">Copilot</div>
        <div class="description">
          <a href="/goose.png" target="_blank" rel="noopener noreferrer">Goose</a>
        </div>
      </div>      
      <div class="ai-bro-item">
        <div class="provider">Claude</div>
        <div class="description">
          <a href="/pemulis.png" target="_blank" rel="noopener noreferrer">Claude Baudelaire</a>
        </div>
      </div>
      <div class="ai-bro-item">
        <div class="provider">Grok</div>
        <div class="description">
          <a href="grok.com" target="_blank" rel="noopener noreferrer">SuperGrok Pot</a>
        </div>
      </div>
      <div class="ai-bro-item">
        <div class="provider">Mistral</div>
        <div class="description">
          <a href="/pdfs/mightier.pdf" target="_blank" rel="noopener noreferrer">LePen Is</a>
        </div>
      </div>
      <div class="ai-bro-item">
        <div class="provider">Meta</div>
        <div class="description"> </div>
      </div>
      <!-- <div class="ai-bro-item">
        <div class="provider">Railway</div>
        <div class="description">
          <a href="https://www.rainharder.com/failway.png" target="_blank" rel="noopener noreferrer">Failway</a>
        </div>
      </div> -->
      <div class="ai-bro-item">
        <div class="provider">Gemini</div>
        <div class="description">
          <a href="https://en.wikipedia.org/wiki/Spotlight_(film)" target="_blank" rel="noopener noreferrer">Cardinal Sundar</a>
        </div>
      </div>
      <div class="ai-bro-item">
        <div class="provider">Perplexity</div>
        <div class="description">
          <a href="https://theoatmeal.com/comics/cats_actually_kill" target="_blank" rel="noopener noreferrer">Pets.com</a>
        </div>
      </div>
    </div>
  </section>
</div>
```