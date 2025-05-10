<script>
    export let logoHeight = "35px";  // Adjustable via prop
    // svelte-ignore export_let_unused
    export let linkFontSize = "1rem"; // NEW adjustable prop for link size
    let showDropdown = false; // For toggling dropdown
</script>

<header class="site-header" style="display: flex; align-items: center; justify-content: space-between; padding: 0.5rem 1rem;">
    <div class="logo-container">
      <a href="/">
        <img src="/rainharder2.png" alt="Rain Harder Logo" style="height: {logoHeight}; width: auto; margin-left: 1.5vw;">
      </a>
    </div>

    <!-- this is stupid and should be in CSS unless you keep pushing tailwind-->

    <nav class="navigation" style="display: flex; gap: 2rem; margin-left: auto; padding-right: 3.2rem; font-size: {linkFontSize}">
      <a href="https://www.rainharder.com/pdfs/The%20Art%20of%20Dressing%20Fiscally%20MS.pdf">the boozinf</a>
      <a href="/words">words matter</a>
      <a href="/fools">fool's gold</a>
      <a href="/fools">kid ai</a>      
      <a href="https://rocketreach.co/jimmy-haslam-email_55376650">contact</a>
    </nav>

    <!-- Completely untouched your Donate container styling & logic -->
    <!-- svelte-ignore a11y_no_static_element_interactions -->
    <div class="donate-container" style="margin-right: 1.5vw" on:mouseenter={() => showDropdown = true} on:mouseleave={() => showDropdown = false}>
      <button class="donate-button">DONATE</button>
      {#if showDropdown}
      <div class="donate-dropdown">
        <a href="https://1strcf.org/make-a-donation/" target="_blank" rel="noopener noreferrer">First Responders</a>
        <a href="https://www.coloradoveteranschamber.org" target="_blank" rel="noopener noreferrer">Colorado Veterans</a>
        <a href="https://denverzoo.org/support/donate/" target="_blank" rel="noopener noreferrer">Denver Zoo</a>    
        <a href="https://give.propublica.org/give/346423/%23!/donation/checkout#!/donation/checkout" target="_blank" rel="noopener noreferrer">ProPublica</a>
      </div>      
      {/if}
    </div>
</header>


