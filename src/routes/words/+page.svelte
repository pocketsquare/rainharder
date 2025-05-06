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
      description: 'Lyrics and reflections on the album title track'
    },
    {
      title: 'The Promised Land',
      file: '/pdfs/words/The Promised Land.pdf',
      description: 'Lyrics and reflections on "The Promised Land"'
    }
  ];

  onMount(() => {
    document.title = "Words | Rain Harder";
  });
</script>

<h1>Words</h1>
<p>Lyrics and reflections Asbury Park and Olivewood Avenue</p>

<div class="pdf-grid">
  {#each pdfs as pdf}
    <a href={pdf.file} target="_blank" rel="noopener noreferrer" class="pdf-card">
      <div class="pdf-icon">
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" d="M19.5 14.25v-2.625a3.375 3.375 0 00-3.375-3.375h-1.5A1.125 1.125 0 0113.5 7.125v-1.5a3.375 3.375 0 00-3.375-3.375H8.25m2.25 0H5.625c-.621 0-1.125.504-1.125 1.125v17.25c0 .621.504 1.125 1.125 1.125h12.75c.621 0 1.125-.504 1.125-1.125V11.25a9 9 0 00-9-9z" />
        </svg>
      </div>
      <h2>{pdf.title}</h2>
      <p>{pdf.description}</p>
    </a>
  {/each}
</div>

<p>Mark Price. Bernie Kosar. Jose Ramirez.</p>