<!-- =============================== -->
<!-- UrlInfo Component               -->
<!-- Instructions for URL Input      -->
<!-- =============================== -->

<script lang="ts">
  // No props needed for static instructions
</script>

<div class="url-info-container">
  <h2>How to Use</h2>
  <p>
    Paste the full URL of a news article into the input box below.
  </p>
  <p>
    Press the <strong>Enter</strong> key to submit the article for analysis.
  </p>
  <!-- Add more instructions or details if needed -->
</div>

<style>
  /* =============================== */
  /* Component Styles              */
  /* =============================== */
  .url-info-container {
    /* Inherits base styles from .module and .module-light */
    font-family: var(--font-sans-serif);
  }

  h2 {
    margin-top: 0;
    font-size: 1.2rem;
  }

  p {
    margin-bottom: 0.5em;
    line-height: 1.4;
  }

  p:last-child {
    margin-bottom: 0;
  }

  strong {
    font-weight: 600;
  }
</style> 