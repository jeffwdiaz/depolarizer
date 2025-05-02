<!-- =============================== -->
<!-- LoadingDots Component           -->
<!-- Simple visual loading indicator -->
<!-- =============================== -->

<script lang="ts">
  import { onMount, onDestroy } from 'svelte';
  import { fade } from 'svelte/transition'; // Import fade

  let visibleDots = 1;
  let intervalId: ReturnType<typeof setInterval>;

  onMount(() => {
    // Cycle through 1 to 5 dots every 400ms
    intervalId = setInterval(() => {
      visibleDots = (visibleDots % 5) + 1; 
    }, 400); 

    // Cleanup function
    return () => {
      clearInterval(intervalId);
    };
  });
</script>

<div class="loading-dots-container module-light">
  <span class="loading-dots-text">
    Analyzing URL
    <br>
  </span>
  
  <span class="dots">
    {'.'.repeat(visibleDots)}
  </span>
</div>

<style>
  /* =============================== */
  /* Component Styles              */
  /* =============================== */
  
  
  .loading-dots-container {
    font-family: var(--font-sans-serif);
    text-align: center;
    padding: 20px 10px;
    padding-top: 150px;
  }
  
  .loading-dots-text   {
    font-family: var(--font-sans-serif);
    font-size: 1.2rem;
    font-weight: 400;
    padding-bottom: 10px;
    padding-right: 10px;
    padding-left: 10px;
    padding-top: 10px;
    margin: 0;
  }

  .dots {
    font-family: var(--font-serif);
    font-size: 4rem;
    line-height: .7;
    letter-spacing: 0.2em;
    font-weight: bold;
    padding-top: 10px;
    padding-right: 10px;
    padding-left: 10px;
    padding-bottom: 10px;
    margin: 0;
  }
</style> 