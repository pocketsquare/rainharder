<script>
  import { onMount } from 'svelte';

  onMount(() => {
    document.body.classList.add('fools-page');
    return () => document.body.classList.remove('fools-page');
  });

  const title = "The Beta Condoms";
  const tagline = "We may be dumb, but we're not stupid.";

  // 1.07734807 = the current picture ratio

  let profiles = [
    { name: 'Stevie Cleveland', imgSrc: '/SC_1.png', alt: 'Stevie Cleveland' },
    { name: 'Clarence Diamond', imgSrc: '/CD_1.png', alt: 'Clarence Diamond' },
    { name: 'Stevie Cleveland', imgSrc: '/rockwell.png', alt: 'Stevie Cleveland' },
    { name: 'Clarence Diamond', imgSrc: '/goggins.png', alt: 'Clarence Diamond' }
  ];
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
    {#each profiles as profile}
      <div class="persona">
        <img src={profile.imgSrc} alt={profile.alt} />
        <p>{profile.name}</p>
      </div>
    {/each}
  </section>

  <!-- New negligee section -->
  <!-- <section class="negligee"></section> -->

  <section class="episode-sample">
    <h2>Episode 1: Nob Hill</h2>
    <p>In Colfax We Trust</p>
  </section>

  <section class="episode-sample">
    <h2>Episode 2: Fool's Gold</h2>
    <p>Denver Bones, Stone Roses.</p>
  </section>

  <section class="episode-sample">
    <h2>Episode 3: Kid AI</h2>
    <p>Mountainhead, Fountainhead.</p>
  </section>

  <section class="episode-sample">
    <h2>Episode 4: Le Humidor</h2>
    <p>The Gang fixes the Rockies</p>
  </section>

  <section class="episode-sample">
    <h2>Episode X: Titans at Broncos, X Bar</h2>
    <p>Sunday, September 7th, 2025</p>
  </section>

  <section class="episode-sample">
    <h2>Episode Y: Browns at Ravens, Y Bar</h2>
    <p>Sunday, September 14th, 2025</p>
  </section>

</div>
