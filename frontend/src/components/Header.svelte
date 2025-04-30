<!-- =============================== -->
<!-- Header Component               -->
<!-- =============================== -->
<script lang="ts">
  import { onMount } from 'svelte';
  import { headerTitle, headerUnderline, headerFadeOut } from './animations';
  
  const { title = 'de · con · struct · ed' } = $props();
  let visible = $state(false);

  onMount(() => {
    visible = true;
  });
</script>

{#if visible}
  <header class="header-area">
    <h1 class="header-title" in:headerTitle out:headerFadeOut>
      {title}
    </h1>
    <div 
      class="header-underline" 
      in:headerUnderline
      out:headerFadeOut
    ></div>
  </header>
{/if}
