<!-- =============================== -->
<!-- UrlInput Component             -->
<!-- =============================== -->
 
<script lang="ts">
  import { createEventDispatcher } from 'svelte';

  export let placeholder: string = "Paste article URL here to depolarize";
  export let value: string = "";

  const dispatch = createEventDispatcher();

  function handleKeydown(event: KeyboardEvent) {
    if (event.key === 'Enter') {
      event.preventDefault();
      console.log('Enter pressed in UrlInput, dispatching urlSubmitted');
      dispatch('urlSubmitted', { url: value });
    }
  }
</script>

<section class="url-input-section">
  <input
    type="text"
    class="url-input"
    {placeholder}
    bind:value
    on:keydown={handleKeydown}
  />
</section>

<style>
  .url-input-section {
    width: 100%;
    margin: 0;
    background-color: var(--color-dark);
  }

  .url-input {
    width: 100%;
    box-sizing: border-box;
    padding: 10px;
    font-size: .8rem;
    background-color: var(--color-dark);
    color: var(--color-light);
    border: 0;
  }

  .url-input:focus {
    outline: none;
    background-color: #333;
    border-width: 2px;
  }

  .url-input::placeholder {
    opacity: 0.5;
  }
</style>
