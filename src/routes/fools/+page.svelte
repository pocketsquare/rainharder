<script>
  const title = "Fools & Fiscality Podcast";
  const tagline = "Smart takes for dumb money.";
</script>

<svelte:head>
  <title>{title}</title>
  <meta name="description" content={tagline} />
</svelte:head>

<div class="fools-container">
  <h1>{title}</h1>
  <p>{tagline}</p>

  <section class="episode-sample">
    <h2>Episode 1: Infinite Jest, Infinite Debt</h2>
    <p>How literary pretension and financial irresponsibility collide spectacularly. Special guest: A hologram of David Foster Wallace.</p>
  </section>
</div>

<style>
  .fools-container {
    max-width: 700px;
    margin: 0 auto;
    padding: 2rem;
    font-family: sans-serif;
    color: #222;
  }

  h1 {
    font-size: 2rem;
    margin-bottom: 1rem;
  }

  .episode-sample {
    margin-top: 2rem;
    border-top: 2px solid #eee;
    padding-top: 1.5rem;
  }

  h2 {
    font-size: 1.5rem;
    color: #444;
  }

  p {
    font-size: 1rem;
    line-height: 1.6;
    color: #666;
  }
</style>
