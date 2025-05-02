<!-- =============================== -->
<!-- Main Layout Component           -->
<!-- =============================== -->
<script lang="ts">
  import '../styles/app.css';
  import {
    Header,
    NavMenu,
    ContentViewer,
    UrlInput,
    RandomTextBox,
    FillerTextBlock,
    FillerImageBlock,
    About,
    SplashOverlay,
    UrlInfo,
    LoadingDots
  } from '../components';
  import type { LayoutData } from './$types';
  import { onMount } from 'svelte'; // Keep onMount
  import { fly, fade } from 'svelte/transition'; // Import fly and fade

  let showSplash = true;     // Controls splash visibility
  let phase1_components = false; // Was: showHeaderNavUrl
  let phase2_components = false; // Was: showOtherComponents
  let isLoadingPhase2 = false; // Add loading state variable
  
  let autoDismissTimer: ReturnType<typeof setTimeout> | undefined = undefined; // Timer ID

  function enterApp() {
    // Prevent running twice and clear timer if dismissed manually
    if (!showSplash) return; 
    if (autoDismissTimer) clearTimeout(autoDismissTimer);

    console.log('Splash dismissed.'); // Updated log
    showSplash = false; // Hide splash immediately
    
    // Show Phase 1 components
    phase1_components = true; 
    console.log('Showing Phase 1 components (Header, NavMenu, UrlInput, About).');
  }
  
  // Updated function to handle loading state
  function loadOtherComponents(event: CustomEvent<{ url: string }>) {
    console.log('urlSubmitted event received in layout. URL:', event.detail.url);
    console.log('Starting loading phase...');
    isLoadingPhase2 = true; // Show loading indicator
    phase2_components = false; // Ensure phase 2 isn't shown yet

    // Wait 5 seconds
    setTimeout(() => {
      console.log('Loading finished. Showing Phase 2 components.');
      isLoadingPhase2 = false; // Hide loading indicator
      phase2_components = true;  // Show actual phase 2 components
    }, 7000); // 7000 milliseconds = 7 seconds
  }



  /*

  // --- TESTING ONLY: Auto-dismiss splash after 1 second --- 
  onMount(() => {
    // TODO: Remove this entire onMount block after testing
    autoDismissTimer = setTimeout(() => {
      console.log('TESTING: Auto-dismissing splash after 1 second.'); // Added TESTING prefix
      enterApp();
    }, 100); // 1 second delay

    // Cleanup the timer if the component unmounts before it fires
    return () => {
      if (autoDismissTimer) clearTimeout(autoDismissTimer);
    };
  });
  // --- END TESTING ONLY --- 


*/




</script>

{#if showSplash}
  <!-- Listen for the custom 'dismiss' event from SplashOverlay -->
  <SplashOverlay on:dismiss={enterApp} />
{/if} <!-- End of splash conditional -->

{#if phase1_components}
  <div class="grid-container">
    <Header />
    
    <div class="left-column">
      <div class="module nav-menu module-dark" in:fly={{ x: -500, duration: 1000, delay: 500 }}>
        <NavMenu />
      </div>
      
      {#if phase2_components}
        <!-- Left Column RandomTextBox -->
        <div class="module module-dark" in:fly={{ x: -500, duration: 1000, delay: 700 }}> 
          <RandomTextBox />
        </div>
        <!-- Second Left Column RandomTextBox -->
        <div class="module module-dark" in:fly={{ x: -500, duration: 1000, delay: 800 }}> 
          <RandomTextBox />
        </div>
      {/if}
    </div>
    
    <div class="main-column">
      {#if !isLoadingPhase2 && !phase2_components}
        <div class="module about-module module-light" 
             in:fly={{ y: -500, duration: 1000, delay: 500 }}
             out:fade={{ duration: 300 }}>  
          <About />
        </div>
      {/if}
      
      <!-- Show LoadingDots when isLoadingPhase2 is true -->
      {#if isLoadingPhase2}
        <div class="loading-module" 
             in:fade={{ duration: 300 }}
             out:fade={{ duration: 300 }}>
          <LoadingDots />
        </div>
      {/if}

      <!-- Show ContentViewer only when phase2 is active -->
      {#if phase2_components}
        <div class="module-light" 
             in:fly={{ y: -500, duration: 1000, delay: 500 }}> 
          <ContentViewer />
        </div>
      {/if}
      <slot />
    </div>
    
    <div class="right-column">
      <!-- Apply module-dark to the URL input wrapper -->
      <div class="module url-input-module module-dark" in:fly={{ x: 500, duration: 1000, delay: 500 }}>
        <UrlInput on:urlSubmitted={loadOtherComponents} />
      </div>

      <!-- Apply module-dark to UrlInfo wrapper -->
      <div class="module url-info-module module-dark" in:fly={{ x: 500, duration: 1000, delay: 500 }}>
        <UrlInfo />
      </div>

      {#if phase2_components}
        <!-- Right Column RandomTextBox -->
        <div class="module module-dark" in:fly={{ x: 500, duration: 1000, delay: 700 }}> 
          <RandomTextBox />
        </div>
        <!-- Second Right Column RandomTextBox -->
        <div class="module module-dark" in:fly={{ x: 500, duration: 1000, delay: 800 }}> 
          <RandomTextBox />
        </div>
      {/if}
    </div>
  </div>

  <style>
    .grid-container {
      display: grid;
      grid-template-columns: repeat(12, 1fr);
      grid-template-rows: auto 1fr;
      grid-template-areas:
        "header header header header header header header header header header header header"
        "left left left main main main main main main right right right";
      gap: 10px;
      padding: 10px;
      min-height: 100vh;
      box-sizing: border-box;
    }
  </style>
{/if} <!-- End of main layout conditional -->
