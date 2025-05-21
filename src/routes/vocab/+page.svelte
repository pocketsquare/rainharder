<script lang="ts">
    import { onMount } from 'svelte';
  
    type Entry = {
      id: number;
      question_id: number;
      text: string;
    };
  
    type Question = {
      id: number;
      prompt: string;
      left_entries: Entry[];
      right_entries: Entry[];
    };
  
    let question: Question | null = null;
  
    onMount(async () => {
    const res = await fetch(`${import.meta.env.PUBLIC_API_URL}/questions/1`);
      if (!res.ok) {
        console.error('Failed to fetch:', res.statusText);
        return;
      }
      question = await res.json();
    });
  </script>
  
  <svelte:head>
    <title>Vocabulary Page</title>
    <meta name="description" content="Vocabulary matching exercise." />
    <link rel="stylesheet" href="/styles.css" />
  </svelte:head>
  
  <!-- Vocabulary Section (no header touched) -->
  <div class="vocabulary-container">
    {#if question}
      <h2>{question.prompt}</h2>
  
      <section class="entries">
        <div class="left">
          <h3>Words</h3>
          <ul>
            {#each question.left_entries as entry}
              <li>{entry.text}</li>
            {/each}
          </ul>
        </div>
  
        <div class="right">
          <h3>Definitions</h3>
          <ul>
            {#each question.right_entries as entry}
              <li>{entry.text}</li>
            {/each}
          </ul>
        </div>
      </section>
    {:else}
      <p>Loading vocabulary...</p>
    {/if}
  </div>
  
  <style>
  .vocabulary-container {
    padding: 1rem;
    margin-top: 2rem; /* Ensures separation from existing header */
  }
  
  .entries {
    display: flex;
    justify-content: space-between;
    gap: 2rem;
  }
  
  .entries div {
    flex: 1;
  }
  
  ul {
    list-style-type: none;
    padding: 0;
  }
  
  li {
    margin-bottom: 0.5rem;
  }
  </style>
  