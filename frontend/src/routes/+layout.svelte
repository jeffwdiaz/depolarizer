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
    SplashOverlay
  } from '../components';
  import type { LayoutData } from './$types';
  import { onMount } from 'svelte'; // Import onMount

  let showSplash = true;     // Controls splash visibility
  let showMainLayout = false; // Controls main layout visibility
  let autoDismissTimer: ReturnType<typeof setTimeout> | undefined = undefined; // Timer ID

  function enterApp() {
    // Prevent running twice and clear timer if dismissed manually
    if (!showSplash) return; 
    if (autoDismissTimer) clearTimeout(autoDismissTimer);

    console.log('Splash dismissed instantly.');
    showSplash = false; // Hide splash immediately

    // Wait 2 seconds before showing main layout
    console.log('Starting 2s delay for main layout...');
    setTimeout(() => {
      showMainLayout = true; // Show main layout after delay
      console.log('Delay finished, showing main layout.');
    }, 2000);
  }

  // --- TESTING ONLY: Auto-dismiss splash after 1 second --- 
  onMount(() => {
    // TODO: Remove this entire onMount block after testing
    autoDismissTimer = setTimeout(() => {
      console.log('TESTING: Auto-dismissing splash after 1 second.'); // Added TESTING prefix
      enterApp();
    }, 1000); // 1 second delay

    // Cleanup the timer if the component unmounts before it fires
    return () => {
      if (autoDismissTimer) clearTimeout(autoDismissTimer);
    };
  });
  // --- END TESTING ONLY --- 

</script>

{#if showSplash}
  <!-- Listen for the custom 'dismiss' event from SplashOverlay -->
  <SplashOverlay on:dismiss={enterApp} />
{/if} <!-- End of splash conditional -->

{#if showMainLayout}
  <!-- Main application layout -->
  <div class="grid-container">
    <Header />
    
    <!-- Left Column -->
    <div class="left-column">
      <div class="module nav-menu">
        <NavMenu />
      </div>
      
      <div class="module">
        <RandomTextBox 
          paragraphs={3}
          minWordsPerSentence={3}
          maxWordsPerSentence={8}
        />
      </div>

    </div>
    
    <!-- Main Column -->
    <div class="main-column">
      <div class="module content-viewer">
        <ContentViewer />
        <slot /> <!-- This is where child routes will render -->
      </div>
    </div>
    
    <!-- Right Column -->
    <div class="right-column">
      <About />

      <div class="module url-input-module">
        <UrlInput />
      </div>

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
