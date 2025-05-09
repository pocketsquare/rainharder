<!-- lib/Header.svelte -->
<script>
    export let logoHeight = "50px";  // Easily adjustable height
    // <Header height="80px" /> <!-- Easy to customize per file-->
  </script>
  
  <header class="site-header">
    <div class="logo-container">
      <img src="/rainharder.png" alt="Rain Harder Logo" style="height: {logoHeight}; width: auto;">
    </div>
    <nav class="navigation">
      <a href="/">Home</a>
      <a href="/about">About</a>
      <a href="/episodes">Episodes</a>
      <a href="/contact">Contact</a>
    </nav>
    <div class="donation-placeholder">Donate</div>
  </header>
  