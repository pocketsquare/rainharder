<script>
  import { onMount } from 'svelte';

  const pdfs = [
    {
      title: 'Atlantic City',
      file: '/pdfs/words/Atlantic City.pdf',
      description: 'Lyrics and reflections on "Atlantic City"'
    },
    {
      title: 'Badlands',
      file: '/pdfs/words/Badlands.pdf',
      description: 'Lyrics and reflections on "Badlands"'
    },
    {
      title: 'Darkness on the Edge of Town',
      file: '/pdfs/words/Darkness on the Edge of Town.pdf',
      description: 'Lyrics and reflections on "Darkness at the Edge of Town'
    },
    {
      title: 'The Promised Land',
      file: '/pdfs/words/The Promised Land.pdf',
      description: 'Lyrics and reflections on "The Promised Land"'
    },
    {
      title: 'Born in the U.S.A.',
      file: '/pdfs/words/ACT_English_Words_4_Revised.pdf',
      description: 'Lyrics and reflections on ACT English'
    },
    {
      title: 'The Street of Brookpark',
      file: '/pdfs/words/Old_Brook_Parma_1.pdf',
      description: 'Lyrics and reflections on the Moon over Parma student nights'
    }
  ];

  onMount(() => {
    document.title = "Words Matter | Rain Harder";
  });
</script>

<svelte:head>
  <title>Words Matter | Rain Harder</title>
  <link rel="stylesheet" href="/styles.css">
</svelte:head>

<!-- needs specificity. vibe coding is for people who killed Kennedy -->

<div class="container"> 
  <h1>Words Matter</h1>
  <p>Lyrics and reflections live from Asbury Park and Olivewood Ave</p>

  <div class="pdf-grid">
    {#each pdfs as pdf}
      <a href={pdf.file} target="_blank" rel="noopener noreferrer" class="pdf-card">
        <!-- <div class="pdf-icon">[SVG ICON HERE]</div> -->
        <h2>{pdf.title}</h2>
        <p>{pdf.description}</p>
      </a>
    {/each}
  </div>

  <p>Mark Price. Bernie Kosar. Jose Ramirez.</p>
</div>
