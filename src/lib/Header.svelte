<script>
  export const logoHeight = "35px";  // Adjustable via prop
  export let linkFontSize = "1rem"; // Adjustable prop for link size
  let showDropdown = false; // For toggling dropdown
  let showKidAiDropdown = false; // For kid ai dropdown
  let mobileMenuOpen = false; // For mobile menu toggle
  
  // Function to close the mobile menu
  function closeMobileMenu() {
      mobileMenuOpen = false;
  }
</script>

<style>
  /* Kid AI dropdown styles - matches donate dropdown but with navigation link styling */
  .kidai-dropdown-container {
    position: relative;
    display: inline-block;
  }

  .kidai-dropdown {
    position: absolute;
    left: 0;
    top: 100%;
    background-color: #ffffff;
    border: 1px solid #080808;
    border-radius: 0rem;
    box-shadow: 0 4px 8px rgba(46, 45, 45, 0.2);
    padding: 0.5rem 0;
    display: flex;
    flex-direction: column;
    min-width: 180px;
    z-index: 1000;
  }

  .kidai-dropdown a {
    color: #333;
    font-weight: 500;
    padding: 1rem 1rem;
    font-size: 1rem;
    text-decoration: none;
    transition: background-color 0.2s ease, color 0.2s ease;
    white-space: nowrap;
  }

  .kidai-dropdown a:hover {
    background-color: #f1f1f1;
    color: #000000;
    font-weight: 600;
  }

  /* Mobile adjustments for kid ai dropdown */
  @media (max-width: 768px) {
    .kidai-dropdown-container {
      width: 100%;
    }
    
    .kidai-dropdown {
      position: static;
      box-shadow: none;
      border: none;
      background-color: rgba(245, 245, 245, 0.95);
      margin-top: 0.5rem;
      border-radius: 4px;
    }
    
    .kidai-dropdown a {
      font-size: 1rem;
      padding: 0.8rem 1rem;
    }
  }
</style>

<header class="site-header" style="display: flex; align-items: center; justify-content: space-between; padding: 0.5rem 1rem;">
  <div class="logo-container">
    <a href="/">
      <img class="desktop-logo" src="/rainharder2.png" alt="Rain Harder Logo" />
      <img class="mobile-logo" src="/rainharder3.png" alt="Rain Harder Mobile Logo" />
    </a>
  </div>

  <!-- Mobile menu toggle button - only visible on mobile -->
  <button 
    class="menu-button" 
    on:click={() => mobileMenuOpen = !mobileMenuOpen}
    aria-label="Toggle mobile menu"
    aria-expanded={mobileMenuOpen}>
    {#if mobileMenuOpen}✕{:else}≡{/if}
  </button>

  <nav class="navigation" class:active={mobileMenuOpen} style="display: flex; gap: 2rem; margin-left: auto; padding-right: 3.2rem; font-size: {linkFontSize}">
      <!-- Kid AI with dropdown -->
      <!-- svelte-ignore a11y_no_static_element_interactions -->
      <div class="kidai-dropdown-container" 
           on:mouseenter={() => showKidAiDropdown = true} 
           on:mouseleave={() => showKidAiDropdown = false}>
        <a href="/kidai" on:click={closeMobileMenu}>kid ai</a>
        {#if showKidAiDropdown}
        <div class="kidai-dropdown">
          <a href="/kidai/subpage1" on:click={closeMobileMenu}>AI Analysis</a>
          <a href="/kidai/subpage2" on:click={closeMobileMenu}>Model Comparisons</a>
          <a href="/kidai/subpage3" on:click={closeMobileMenu}>Research Tools</a>
          <a href="/kidai/reports" on:click={closeMobileMenu}>Reports</a>
        </div>
        {/if}
      </div>
      
      <a href="https://www.rainharder.com/pdfs/The%20Art%20of%20Dressing%20Fiscally%20MS.pdf" on:click={closeMobileMenu}>the art</a>
      <a href="/words" on:click={closeMobileMenu}>words matter</a>
      <a href="/fools" on:click={closeMobileMenu}>beta condoms</a>
      <a href="https://rocketreach.co/jimmy-haslam-email_55376650" on:click={closeMobileMenu}>eye contact</a>
  </nav>

  <!-- Donate container with dropdown -->
  <!-- svelte-ignore a11y_no_static_element_interactions -->
  <div class="donate-container" style="margin-right: 1.5vw" on:mouseenter={() => showDropdown = true} on:mouseleave={() => showDropdown = false}>
    <button class="donate-button">DONATE</button>
    {#if showDropdown}
    <div class="donate-dropdown">
      <a href="https://1strcf.org/make-a-donation/" target="_blank" rel="noopener noreferrer">First Responders</a>
      <a href="https://www.coloradoveteranschamber.org" target="_blank" rel="noopener noreferrer">Colorado Veterans</a>
      <a href="https://give.dug.org/give/498865" target="_blank" rel="noopener noreferrer">Denver Urban</a>    
      <a href="https://give.propublica.org/give/346423/%23!/donation/checkout#!/donation/checkout" target="_blank" rel="noopener noreferrer">ProPublica</a>
    </div>      
    {/if}
  </div>
</header>