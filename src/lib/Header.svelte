<script>
    export let links = [
      { name: "Home", href: "/" },
      { name: "About", href: "/about" },
      { name: "Episodes", href: "/episodes" },
      { name: "Contact", href: "/contact" }
    ];
  </script>
  
  <header class="site-header">
    <div class="logo-placeholder">
      LOGO
    </div>
  
    <nav class="navigation">
      {#each links as link}
        <a href="{link.href}">{link.name}</a>
      {/each}
    </nav>
  
    <div class="donation-placeholder">
      Donate
    </div>
  </header>