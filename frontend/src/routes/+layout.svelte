<!-- =============================== -->
<!-- Main Layout Component           -->
<!-- =============================== -->
<script lang="ts">
  import '../app.css';
  import {
    Header,
    NavMenu,
    ContentViewer,
    FillerTextBlock,
    UrlInput,
    FillerImageBlock,
    About,
    SplashOverlay,
    RandomTextBox
  } from '../components';
  // Import your modules here
</script>

<SplashOverlay />

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
