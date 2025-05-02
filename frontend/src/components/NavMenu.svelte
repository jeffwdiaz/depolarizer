<!-- =============================== -->
<!-- Navigation Menu Component       -->
<!-- =============================== -->

<script lang="ts">
  import { onMount } from 'svelte';
  
  interface MenuItem {
    name: string;
    selected: boolean;
  }
  
  // Menu items with their states
  let menuItems: MenuItem[] = [];
  const initialItems: MenuItem[] = [
    { name: 'Fox', selected: false },
    { name: 'CNN', selected: false },
    { name: 'Reuters', selected: false },
    { name: 'NPR', selected: false }
  ];

  onMount(() => {
    // Trigger animation by setting the items after mount
    menuItems = [...initialItems];
  });
</script>

<nav>
  {#if menuItems.length}
    <ul class="nav-menu-list">
      {#each menuItems as item, i}
        <li 
          class:selected={item.selected}
        >
          {item.name}
        </li>
      {/each}
    </ul>
  {/if}
</nav>

<style>
  .nav-menu-list {
    list-style: none;
    padding: 0;
    margin: 0;
    display: flex;
    flex-direction: column;
    gap: 8px;
    width: 100%;
    text-decoration: line-through;
  }

  .nav-menu-list li {
    padding: 12px 16px;
    cursor: pointer;
    /* Default state (inherits from module-dark parent) */
    color: var(--color-light);
    background-color: transparent;
    transition: background-color 0.2s ease, color 0.2s ease; /* Add transition */
    font-weight: normal; /* Default font weight */
  }

  /* Hover state */
  .nav-menu-list li:hover {
    background-color: var(--color-highlight);
    /* Text color on hover remains light by default, which should be fine */
  }

  /* Selected state */
  .nav-menu-list li.selected {
    font-weight: 500;
    color: var(--color-highlight);
    background-color: var(--color-light);
  }

  .nav-menu-list li.selected:hover {
     background-color: var(--color-highlight); 
     color: var(--color-light);
  }

</style> 