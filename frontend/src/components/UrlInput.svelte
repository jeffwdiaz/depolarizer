<!-- =============================== -->
<!-- UrlInput Component             -->
<!-- =============================== -->
 
<script lang="ts">
  export let placeholder: string = "Paste article URL here to depolarize";
  export let value: string = "";
  export let onInput: (event: Event) => void = () => {};
</script>

<section class="url-input-section">
  <input
    type="text"
    class="url-input"
    {placeholder}
    bind:value
    on:input={onInput}
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
