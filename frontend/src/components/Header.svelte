<!-- =============================== -->
<!-- Header Component               -->
<!-- Main site header with animated -->
<!-- title and underline           -->
<!-- =============================== -->
<script lang="ts">
  import { onMount, onDestroy } from 'svelte';
  import { headerTitle, headerUnderline, headerFadeOut } from './animations';
  import { fly } from 'svelte/transition';
  
  export let title = 'de · con · struct · ed';
  let visible = false;
  let mounted = false;

  onMount(() => {
    // Small delay to ensure proper mounting
    setTimeout(() => {
      visible = true;
      mounted = true;
    }, 100);
  });

  onDestroy(() => {
    mounted = false;
  });
</script>

{#if visible}
  <header class="site-header" class:mounted in:fly={{ y: -50, duration: 600, delay: 100 }}>
    <h1 in:headerTitle out:headerFadeOut>
      {title}
    </h1>
  </header>
{/if}

<style>
  .site-header {
    grid-area: header;
    background: var(--color-dark);
    color: var(--color-light);
    width: 100%;
    height: 150px; /* Use fixed height */
    position: relative;
    opacity: 0;
  }

  .site-header.mounted {
    opacity: 1;
  }

  h1 {
    font-family: var(--font-serif);
    font-size: var(--font-size-title);
    font-weight: 700;
    text-align: center;
    margin: 0;
    letter-spacing: 5px;
    width: 100%;
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
  }

  .underline {
    width: 100%;
    height: 5px;
    background: var(--color-light);  /* Changed to main-bg to be visible */
    margin: 0;
    position: absolute;
    bottom: 0;
  }
</style>
