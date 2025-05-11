<script>
  const title = "The Beta Condoms";
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

<section class="gruesome-twosome">
  <div class="persona">
    <img src="/SC_1.png" alt="Stevie Cleveland" />
    <p>Stevie Cleveland</p>
  </div>
  <div class="persona">
    <img src="/CD_1.png" alt="Clarence Diamond" />
    <p>Clarence Diamond</p>
  </div>
</section>

  <section class="episode-sample">
    <h2>Episode 1: Fool's Gold</h2>
    <p>Denver Stones, Denver Bones, Stone Roses. Special guest: Elvis.</p>
  </section>
</div>