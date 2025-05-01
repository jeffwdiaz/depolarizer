<!-- =============================== -->
<!-- Header Component               -->
<!-- Main site header with animated -->
<!-- title and underline           -->
<!-- =============================== -->
<script lang="ts">
  import { onMount, onDestroy } from 'svelte';
  import { headerTitle, headerUnderline, headerFadeOut } from './animations';
  
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
  <header class="site-header" class:mounted>
    <h1 in:headerTitle out:headerFadeOut>
      {title}
    </h1>
    <div 
      class="underline" 
      in:headerUnderline
      out:headerFadeOut
    ></div>
  </header>
{/if}

<style>
  .site-header {
    grid-area: header;
    background: var(--main-text);
    color: var(--main-bg);
    width: 100%;
    height: var(--header-height);
    position: relative;
    opacity: 0;
    transition: opacity 0.3s ease-in-out;
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
    background: var(--main-bg);  /* Changed to main-bg to be visible */
    margin: 0;
    position: absolute;
    bottom: 0;
  }
</style>
