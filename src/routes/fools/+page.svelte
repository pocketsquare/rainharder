<script>
  const title = "Fools's Gold";
  const tagline = "We may be dumb, but we're not stupid.";
</script>

<svelte:head>
  <title>{title}</title>
  <meta name="description" content={tagline} />
  <link rel="stylesheet" href="/styles.css" />
</svelte:head>

<div class="fools-container">
  <h1>{title}</h1>
  <p>{tagline}</p>

  <p>
    &nbsp;<a href="/pdfs/The%20Art%20of%20Dressing%20Fiscally%20MS.pdf#page=90" target="_blank">
      Last Night was another Night of Long Knives.
    </a>
  </p>

  <section class="episode-sample">
    <h2>Episode 1: Infinite Jest, Infinite Debts</h2>
    <p>Denver Stones, Denver Bones, Stone Roses. Special guest: Elvis.</p>
  </section>
</div>
