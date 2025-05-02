<!-- =============================== -->
<!-- Random Character Grid Component -->
<!-- Displays a grid of randomly appearing letters -->
<!-- =============================== -->

<script lang="ts">
  import { onMount, onDestroy, tick } from 'svelte';

  // Configuration
  const updateInterval = 1; // ms - How often to update a character (Increased for slower effect)
  const characters = 'abcdefghijklmnopqrstuvwxyz'; // Characters to choose from (Lowercase letters only)
  const cellWidth = 20; // Fixed cell width in pixels (matches CSS)
  const cellHeight = 20; // Fixed cell height in pixels (matches CSS)
  const minFadeDelay = 10; // ms
  const maxFadeDelay = 1000; // ms
  const fadeDuration = 2000; // ms - How long the CSS fade takes
  const holdDuration = 30000; // ms - How long the letter stays visible after fade-in

  // Grid state
  type GridCell = { char: string; visible: boolean } | null;
  let gridLetters: GridCell[][] = [];
  let rows = 0;
  let cols = 0;
  let containerElement: HTMLDivElement; // To bind to the container div

  let intervalId: ReturnType<typeof setInterval>;
  let resizeObserver: ResizeObserver;

  /**
   * Gets a random character from the available set
   */
  function getRandomChar(): string {
    return characters[Math.floor(Math.random() * characters.length)];
  }

  /**
   * Calculates grid dimensions and initializes/resizes the grid array
   */
  async function updateGridDimensions() {
    if (!containerElement) return;

    // Measure the container
    const containerWidth = containerElement.clientWidth;
    const containerHeight = containerElement.clientHeight;

    // Calculate new dimensions (ensure at least 1x1 grid)
    const newCols = Math.max(1, Math.floor(containerWidth / cellWidth));
    const newRows = Math.max(1, Math.floor(containerHeight / cellHeight));

    // Only update if dimensions changed
    if (newRows !== rows || newCols !== cols) {
      console.log(`Resizing grid to ${newRows}x${newCols}`);
      rows = newRows;
      cols = newCols;

      // Recreate the grid array, preserving existing characters where possible
      const newGrid: GridCell[][] = Array(rows)
        .fill(0)
        .map((_, r) =>
          Array(cols)
            .fill(0)
            .map((_, c): GridCell => 
              gridLetters[r]?.[c] || null // Keep old cell object if possible, else null
            )
        );
      gridLetters = newGrid;
    }
  }

  /**
   * Starts the interval to update characters
   */
  function startInterval() {
    if (intervalId) clearInterval(intervalId); // Clear existing interval
    
    intervalId = setInterval(() => {
      if (rows === 0 || cols === 0) return; // Don't run if grid not initialized

      // Find all empty cells
      const emptyCells: [number, number][] = [];
      for (let r = 0; r < rows; r++) {
        for (let c = 0; c < cols; c++) {
          // Check if cell is null (truly empty)
          if (gridLetters[r][c] === null) { 
            emptyCells.push([r, c]);
          }
        }
      }

      if (emptyCells.length > 0) {
        // If empty cells exist, pick one randomly
        const randomIndex = Math.floor(Math.random() * emptyCells.length);
        const [targetRow, targetCol] = emptyCells[randomIndex];

        // Update the letter in the target cell (ensure reactivity)
        if (gridLetters[targetRow]) { // Check if row exists (might be resizing)
          const newChar = getRandomChar();
          // Set character but mark as not visible initially
          gridLetters[targetRow][targetCol] = { char: newChar, visible: false };
          gridLetters = gridLetters; // Trigger reactivity for initial placement

          // Schedule the fade-in
          const delay = minFadeDelay + Math.random() * (maxFadeDelay - minFadeDelay);
          
          // Use constants for row/col in timeout closure
          const r = targetRow; 
          const c = targetCol; 

          setTimeout(() => {
            // Check if the cell still exists and hasn't been overwritten
            const cell = gridLetters[r]?.[c];
            if (cell && cell.char === newChar && !cell.visible) {
              cell.visible = true;
              gridLetters = gridLetters; // Trigger reactivity for visibility change

              // Schedule the fade-out
              setTimeout(() => {
                // Check if the cell *still* exists and is the same character before removing
                if (gridLetters[r]?.[c]?.char === newChar && gridLetters[r][c]?.visible === true) {
                  gridLetters[r][c] = null; // Set back to null to trigger fade-out and removal
                  gridLetters = gridLetters; // Trigger reactivity
                }
              }, holdDuration); // Wait holdDuration after becoming visible
            }
          }, delay);
        }
      }
    }, updateInterval);
  }

  onMount(() => {
    // Initial calculation
    updateGridDimensions();
    startInterval();

    // Observe container size changes
    resizeObserver = new ResizeObserver(async () => {
        await updateGridDimensions();
        // Restart interval only if dimensions changed? Or just let it run?
        // Let's restart to ensure it uses new rows/cols immediately if needed.
        // Optional: debounce this if performance becomes an issue.
        startInterval(); 
    });
    resizeObserver.observe(containerElement);

    return () => {
      if (intervalId) clearInterval(intervalId);
      if (resizeObserver) resizeObserver.disconnect();
    };
  });

</script>

<div class="random-char-grid" bind:this={containerElement}>
  {#each gridLetters as row, i}
    <div class="grid-row">
      {#each row as cell, j}
        {#if cell}
          <span class="grid-cell" class:visible={cell.visible}>
            {cell.char}
          </span>
        {:else}
          <!-- Render an empty placeholder cell if needed, or just nothing -->
          <span class="grid-cell empty">&nbsp;</span> 
        {/if}
      {/each}
    </div>
  {/each}
</div>

<style>
  /* =============================== */
  /* Component Styles              */
  /* =============================== */
  .random-char-grid {
    font-family: var(--font-serif);
    font-size: 1rem;
    font-weight: 400;
    line-height: 1.1;
    overflow: hidden;
    display: block;
    width: 100%;
    height: 420px;
    background-color: transparent;
    box-sizing: border-box;
  }

  .grid-row {
    display: flex;
    width: 100%; /* Ensure row takes full width */
    /* Allow rows to wrap if they exceed container width */
    flex-wrap: wrap; 
  }
  
  .grid-cell {
    display: inline-block; /* Keep cells inline */
    color: var(--color-text); /* Character color */
    width: 20px; /* Fixed width */
    height: 20px; /* Fixed height */
    display: flex; /* Use flex to center content */
    align-items: center; /* Center vertically */
    justify-content: center; /* Center horizontally */
    box-sizing: border-box; /* Include border in size */
    opacity: 0; /* Start invisible */
    transition: opacity 300ms ease-in-out; /* CSS transition for fade (fixed duration) */
    /* Use estimated char dimensions for spacing (optional, adjust as needed) */
    /* width: calc(1em * 0.6); 
       height: calc(1em * 1.1); */
  }

  .grid-cell.visible {
    opacity: 1; /* Become visible */
  }

  .grid-cell.empty {
    /* Style placeholder cells differently if needed, e.g., no border */
    opacity: 0; /* Ensure empty placeholders are also invisible */
    border: none;
  }
</style> 