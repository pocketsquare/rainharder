<script>
    import Header from '$lib/Header.svelte';
    import { page } from '$app/stores';
    import { onMount, afterUpdate } from 'svelte';
    
    // Function to update the body class based on the current path
    function updateBodyClass() {
      if (typeof document !== 'undefined') {
        // Clear any existing page-specific classes
        document.body.classList.remove('home-page', 'words-page');
        
        // Add the appropriate class
        if ($page.url.pathname === '/words') {
          document.body.classList.add('words-page');
        } else if ($page.url.pathname === '/') {
          document.body.classList.add('home-page');
        }
      }
    }
    
    // Update class when component mounts
    onMount(updateBodyClass);
    
    // Update class when route changes
    $: if ($page) updateBodyClass();
  </script>
  
  <Header />
  
  <slot></slot>