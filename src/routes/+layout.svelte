<!-- =============================== -->
<!-- Main Layout Component           -->
<!-- =============================== -->
<script lang="ts">
  import '../app.css';
  import Header from '$lib/Header.svelte';
  import NavMenu from '$lib/NavMenu.svelte';
  import ContentViewer from '$lib/ContentViewer.svelte';
  import FillerTextBlock from '$lib/FillerTextBlock.svelte';
  import UrlInput from '$lib/UrlInput.svelte';
    import FillerImageBlock from '$lib/FillerImageBlock.svelte';
  // Import your modules here
</script>

<div class="grid-container">
  <!-- Header -->
  <Header />
  
  <!-- Left Column -->
  <div class="left-column">
    <div class="module nav-menu">
      <NavMenu />
    </div>
    
    <FillerImageBlock />

    <FillerTextBlock />
    <FillerTextBlock />
    <FillerTextBlock />
    <FillerTextBlock />
    <FillerTextBlock />
  
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
    <div class="module info-panel">
      <p>Depolarizer is a tool designed to combat division and distrust in society by providing neutral, emotion-free news.</p>
    </div>

    <div class="module url-input-module">
      <UrlInput />
    </div>
    <FillerTextBlock />
    <FillerTextBlock />
    <FillerTextBlock />
    <FillerTextBlock />
    <FillerTextBlock />
  </div>
</div>
