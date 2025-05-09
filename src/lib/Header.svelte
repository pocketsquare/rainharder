<script>
    export let logoHeight = "50px";  // Adjustable via prop
    let showDropdown = false; // For toggling dropdown
  </script>
  
  <header class="site-header">
    <div class="logo-container">
      <a href="/">
        <img src="/rainharder.png" alt="Rain Harder Logo" style="height: {logoHeight}; width: auto; margin-left: 1.5vw;">
      </a>
    </div>
  
    <nav class="navigation">
      <a href="/about">About</a>
      <a href="/episodes">Episodes</a>
      <a href="/contact">Contact</a>
    </nav>
  
    <!-- svelte-ignore a11y_no_static_element_interactions -->
    <div class="donate-container" style="margin-right: 1.5vw" on:mouseenter={() => showDropdown = true} on:mouseleave={() => showDropdown = false}>
      <button class="donate-button">DONATE</button>
      {#if showDropdown}
      <div class="donate-dropdown">
        <a href="https://give.propublica.org/give/346423/%23!/donation/checkout#!/donation/checkout" target="_blank" rel="noopener noreferrer">ProPublica</a>
        <a href="https://denverzoo.org/support/donate/" target="_blank" rel="noopener noreferrer">Denver Zoo</a>
        <a href="https://www.coloradoveteranschamber.org" target="_blank" rel="noopener noreferrer">Colorado Veterans</a>
      </div>      
      {/if}
    </div>
  </header>
  