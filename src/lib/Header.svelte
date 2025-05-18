<script>
    export let logoHeight = "35px";  // Adjustable via prop
    // svelte-ignore export_let_unused
    export let linkFontSize = "1rem"; // NEW adjustable prop for link size
    let showDropdown = false; // For toggling dropdown
    let mobileMenuOpen = false; // For mobile menu toggle
    
    // Function to close the mobile menu
    function closeMobileMenu() {
        mobileMenuOpen = false;
    }
    
    // Handle keyboard events for accessibility
    function handleKeyDown(event) {
        if (event.key === 'Escape') {
            closeMobileMenu();
        }
    }
</script>

<header class="site-header" style="display: flex; align-items: center; justify-content: space-between; padding: 0.5rem 1rem;">
    <div class="logo-container">
      <a href="/">
        <img class="desktop-logo" src="/rainharder2.png" alt="Rain Harder Logo" style="height: {logoHeight}; width: auto; margin-left: 1.5vw;">
        <img class="mobile-logo" src="/rainharder3.png" alt="Rain Harder Mobile Logo" style="height: {logoHeight}; width: auto; margin-left: 1.5vw;">
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

    <!-- this is stupid and should be in CSS unless you keep pushing tailwind -->
    <nav class="navigation" class:active={mobileMenuOpen} style="display: flex; gap: 2rem; margin-left: auto; padding-right: 3.2rem; font-size: {linkFontSize}">
        <a href="/kidai" on:click={closeMobileMenu}>kid ai</a>
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

{#if mobileMenuOpen}
  <!-- Use button instead of div for better accessibility -->
  <button 
    class="mobile-menu-backdrop" 
    on:click={closeMobileMenu}
    on:keydown={handleKeyDown}
    aria-label="Close mobile menu"
    tabindex="0">
  </button>
{/if}