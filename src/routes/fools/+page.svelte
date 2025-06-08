<script>
  import { onMount } from 'svelte';

  onMount(() => {
    document.body.classList.add('fools-page');
    return () => document.body.classList.remove('fools-page');
  });

  const title = "The Beta Condoms";
  const tagline = "we may be dumb, but we're not stupid.";

  let profiles = [
    { name: 'Stevie Cleveland', imgSrc: '/rockwell.png', alt: 'Stevie Cleveland' },
    { name: 'Clarence Diamond', imgSrc: '/goggins.png', alt: 'Clarence Diamond' },
    { name: 'Gino Prime', imgSrc: '/posey.png', alt: 'Gino Prime' },
    { name: 'Kendall & Shiv', imgSrc: '/kitties.png', alt: 'Kendall & Shiv' }
  ];
</script>

<svelte:head>
  <title>{title}</title>
  <meta name="description" content={tagline} />
  <link rel="stylesheet" href="/styles.css" />
</svelte:head>

<div class="fools-header">
  <h1>{title}</h1>
  <p>{tagline}</p>

  <section class="gruesome-twosome">
    {#each profiles as profile}
      <div class="persona">
        <img src={profile.imgSrc} alt={profile.alt} />
        <p>{profile.name}</p>
      </div>
    {/each}
  </section>

</div>

<div class="container fools-container">

  <div class="episodes-grid">
    <section class="episode-sample">
      <h2>Episode 1: Nob Hill</h2>
      <p>In Colfax We Trust</p>
    </section>

    <section class="episode-sample">
      <h2>Episode 2: Fool's Gold</h2>
      <p>Denver Bones, Stone Roses</p>
    </section>

    <section class="episode-sample">
      <h2>Episode 3: Kid AI</h2>
      <p>Mountainhead, Fountainhead</p>
    </section>

    <section class="episode-sample">
      <h2>Episode 4: Omaha!</h2>
      <p>Manning, Meat, and Menks</p>
    </section>

    <section class="episode-sample">
      <h2>Episode 5: The Humidor</h2>
      <p>The Gang Fixes the Rockies</p>
    </section>

    <section class="episode-sample">
      <h2>Episode 6: Red Right 88</h2>
      <p>A Deep Drive into Cleveland QBs</p>
    </section>

    <section class="episode-sample">
      <h2>Episode X: Titans at Broncos</h2>
      <p>X Bar (date inherent)</p>
    </section>

    <section class="episode-sample">
      <h2>Episode Y: Browns at Ravens</h2>
      <p>Y Bar (date inherent)</p>
    </section>
  </div>
</div>