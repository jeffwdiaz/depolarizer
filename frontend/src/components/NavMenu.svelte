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
  const menuItems = $state<MenuItem[]>([]);
  const initialItems: MenuItem[] = [
    { name: 'Fox', selected: false },
    { name: 'CNN', selected: false },
    { name: 'Reuters', selected: false },
    { name: 'NPR', selected: true }
  ];

  // Hover state management
  let hoveredIndex = $state<number | null>(null);

  onMount(() => {
    // Trigger animation by setting the items after mount
    menuItems.push(...initialItems);
  });
</script>

<nav>
  {#if menuItems.length}
    <ul class="nav-menu-list">
      {#each menuItems as item, i}
        <li 
          class:selected={item.selected}
          onmouseenter={() => hoveredIndex = i}
          onmouseleave={() => hoveredIndex = null}
          style:background-color={ item.selected ? 'var(--color-dark)' : hoveredIndex === i ? 'var(--color-highlight)' : 'transparent' }
          style:color={item.selected ? 'var(--color-light)' : 'var(--color-dark)'}
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
}

.nav-menu-list li {
  padding: 12px 16px;
  cursor: pointer;
}

.nav-menu-list li:hover {
  background-color: var(--color-highlight);
}

.nav-menu-list li.selected {
  background-color: var(--color-dark);
  color: var(--color-light);
  font-weight: 500;
}
</style> 