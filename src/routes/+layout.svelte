<script lang="ts">
  import '../app.css';
  import Sidebar from '$lib/Sidebar.svelte';
  import Article from '$lib/Article.svelte';
  import Header from '$lib/Header.svelte';
  // Layout logic can go here if needed
</script>

<!-- =============================== -->
<!-- Main Grid Layout Structure      -->
<!-- =============================== -->
 
<div class="grid-container">
  <aside class="sidebar grid-sidebar">
    <Sidebar />
  </aside>
  <!-- Full-width header -->
  <Header title="The Depolarizer" />
  <!-- About info in cols 9-12 -->
  <div class="header-description about-info">
    <p>Depolarizer is a tool designed to combat division and distrust in society by providing neutral, emotion-free news. It scrapes articles from a diverse set of sources, analyzes their sentiment, and generates balanced summaries to promote informed, rational public discourse and strengthen democracy.</p>
  </div>
  <main class="main-content grid-main-content">
    <Article />
  </main>
</div>

<slot /> <!-- This is where child routes will render -->
