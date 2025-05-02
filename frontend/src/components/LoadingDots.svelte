<!-- =============================== -->
<!-- LoadingDots Component           -->
<!-- Simple visual loading indicator -->
<!-- =============================== -->

<script lang="ts">
  // No props or logic needed for this simple component
</script>

<div class="loading-dots-container module module-light">
  <span class="dots">.....</span>
</div>

<style>
  /* =============================== */
  /* Component Styles              */
  /* =============================== */
  .loading-dots-container {
    /* Inherits base styles from .module and .module-light */
    font-family: var(--font-sans-serif);
    text-align: center; /* Center the dots */
    padding: 20px 10px; /* Adjust padding */
  }

  .dots {
    font-size: 2rem; /* Make dots larger */
    letter-spacing: 0.2em; /* Space out the dots */
    font-weight: bold;
  }
</style> 