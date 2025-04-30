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
