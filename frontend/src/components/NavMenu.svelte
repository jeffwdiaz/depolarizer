<!-- =============================== -->
<!-- Navigation Menu Component       -->
<!-- =============================== -->

<script lang="ts">
  import { onMount } from 'svelte';
  
  interface MenuItem {
    name: string;
    selected: boolean;
    strikethrough?: boolean;
  }
  
  // Menu items with their states
  let menuItems: MenuItem[] = [];
  const initialItems: MenuItem[] = [
    { name: 'Politics', selected: false },
    { name: 'CNN', selected: false, strikethrough: true },
    { name: 'FOX', selected: false, strikethrough: true },
    { name: 'NPR', selected: false, strikethrough: true }
  ];

  onMount(() => {
    // Trigger animation by setting the items after mount
    menuItems = [...initialItems];
  });
</script>

<nav class="nav-menu">
  {#if menuItems.length}
    <ul class="nav-menu-list">
      {#each menuItems as item, i}
        <li 
          class:selected={item.selected}
          class:strikethrough={item.strikethrough}
        >
          {item.name}
        </li>
      {/each}
    </ul>
  {/if}
</nav>

<style>
  .nav-menu {
    color: var(--color-dark);
    font-size: 2rem;
    font-weight: 700;
  }
  .nav-menu-list {
    list-style: none;
    padding: 10px 10px 10px 0px;
    margin: 0;
    display: flex;
    flex-direction: column;
    gap: 8px;
    width: 100%;
  }

  .nav-menu-list li {
    padding: 0px 10px;
    cursor: pointer;
    /* Default state (inherits from module-dark parent) */
    background-color: transparent;
    transition: background-color 0.2s ease, color 0.2s ease; /* Add transition */
  }

  /* Hover state */
  .nav-menu-list li:hover {
    color: var(--color-highlight);
  }

  /* Selected state */
  .nav-menu-list li.selected {
    color: var(--color-highlight);
    background-color: var(--color-light);
  }

  .nav-menu-list li.selected:hover {
     background-color: var(--color-highlight); 
     color: var(--color-light);
  }

  /* Strikethrough style for specific items */
  .nav-menu-list li.strikethrough {
    text-decoration: line-through;
  }

</style> 