<!-- =============================== -->
<!-- Navigation Menu Component       -->
<!-- =============================== -->

<script lang="ts">
  import { onMount } from 'svelte';
  import { navMenuFade } from './animations';
  
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
    <ul class="nav-menu-list" in:navMenuFade>
      {#each menuItems as item, i}
        <li 
          class:selected={item.selected}
          on:mouseenter={() => hoveredIndex = i}
          on:mouseleave={() => hoveredIndex = null}
          style:background-color={hoveredIndex === i && !item.selected ? 'var(--nav-menu-hover)' : 
                                item.selected ? 'var(--accent)' : 'transparent'}
          style:color={item.selected ? 'var(--main-bg)' : 'var(--main-text)'}
        >
          {item.name}
        </li>
      {/each}
    </ul>
  {/if}
</nav> 