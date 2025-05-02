<script>
    // No script needed for this simple component
  </script>
  
  <svelte:head>
    <title>Rain Harder</title>
    <link rel="stylesheet" href="/styles.css">
  </svelte:head>
  
  <div class="container">
    <h1>Hello, World!</h1>
    <p>(Make it rain harder.)</p>
    
    <div class="video-container">
      <iframe 
        title="Prince Super Bowl Performance"
        src="https://player.vimeo.com/video/353526969" 
        width="560" 
        height="315" 
        frameborder="0" 
        allow="autoplay; fullscreen; picture-in-picture" 
        allowfullscreen>
      </iframe>
    </div>
    
    <ul class="link-list">
      <li><a href="/">Link One</a></li>
      <li><a href="/">Link Two</a></li>
      <li><a href="/">Link Three</a></li>
      <li><a href="/">Link Four</a></li>
    </ul>
  </div>
  
  <style>
    /* Component-specific styles could go here if needed */
  </style>