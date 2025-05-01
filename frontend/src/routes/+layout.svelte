<!-- =============================== -->
<!-- Main Layout Component           -->
<!-- =============================== -->
<script lang="ts">
  import '../app.css';
  import Header from '../components/Header.svelte';
  import NavMenu from '../components/NavMenu.svelte';
  import ContentViewer from '../components/ContentViewer.svelte';
  import FillerTextBlock from '../components/FillerTextBlock.svelte';
  import UrlInput from '../components/UrlInput.svelte';
  import FillerImageBlock from '../components/FillerImageBlock.svelte';
  import About from '../components/About.svelte';
  import SplashOverlay from '../components/SplashOverlay.svelte';
  import { RandomTextBox } from '../components';
  // Import your modules here
</script>

<SplashOverlay />

<div class="grid-container">
  <!-- Header -->
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
        refreshInterval={4000}
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
