<script lang="ts">
  import { fade } from 'svelte/transition';
  import { onMount, tick } from 'svelte';
  let visible = true;
  let mounted = false;
  let gridKey = 0;

  // Letters to use in the grid
  const letters = ['d', 'e', 'c', 'o', 'n', 's', 't', 'r', 'u'];
  let grid: string[][] = [];
  let delays: number[][] = [];
  let cols = 0;
  let rows = 0;
  let revealedGrid: boolean[][] = [];

  function handleClick() {
    visible = false;
  }

  function shuffle<T>(array: T[]): T[] {
    // Fisher-Yates shuffle
    for (let i = array.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [array[i], array[j]] = [array[j], array[i]];
    }
    return array;
  }

  function generateGrid() {
    cols = Math.ceil(window.innerWidth / 100);
    rows = Math.ceil(window.innerHeight / 100);
    grid = Array.from({ length: rows }, () =>
      Array.from({ length: cols }, () => letters[Math.floor(Math.random() * letters.length)])
    );
    // Generate a flat array of delays, shuffle, then map to grid shape
    const total = rows * cols;
    const baseDelay = 500; // ms between each letter
    let delayList = Array.from({ length: total }, (_, i) => i * baseDelay);
    shuffle(delayList);
    delays = Array.from({ length: rows }, (_, r) =>
      Array.from({ length: cols }, (_, c) => delayList[r * cols + c])
    );
    console.log('generateGrid:', { cols, rows, grid, delays }); // debug grid and delays
  }

  function resetRevealedGrid() {
    revealedGrid = Array.from({ length: rows }, () => Array(cols).fill(false));
  }

  async function revealLettersStaggered() {
    // Create a flat list of all grid positions
    const positions: [number, number][] = [];
    for (let r = 0; r < rows; r++) {
      for (let c = 0; c < cols; c++) {
        positions.push([r, c]);
      }
    }
    // Shuffle the positions
    shuffle(positions);
    // Reveal each letter in shuffled order
    for (const [r, c] of positions) {
      revealedGrid[r][c] = true;
      await new Promise(res => setTimeout(res, 400)); // 40ms per letter
    }
  }

  onMount(() => {
    const updateGrid = async () => {
      mounted = false;
      gridKey += 1;
      await tick(); // Wait for DOM to update and remove the grid
      generateGrid();
      resetRevealedGrid();
      await tick(); // Wait for DOM to update with new grid
      // Delay mounting the grid to trigger transitions
      setTimeout(async () => {
        mounted = true;
        await tick();
        revealLettersStaggered();
      }, 1000); // 1000ms delay; adjust as needed
    };

    updateGrid();

    window.addEventListener('resize', updateGrid);
    return () => window.removeEventListener('resize', updateGrid);
  });
</script>

{#if visible}
  <button type="button" class="splash-overlay" on:click={handleClick} transition:fade={{ duration: 600 }}>
    {#if mounted}
      {#key gridKey}
        <div class="letter-grid" aria-hidden="true">
          {#each grid as row, rowIdx (rowIdx)}
            <div class="grid-row">
              {#each row as letter, colIdx (`${rowIdx}-${colIdx}`)}
                {#if revealedGrid[rowIdx] && revealedGrid[rowIdx][colIdx]}
                  <span
                    class="grid-letter"
                    transition:fade={{ duration: 800 }}
                  >
                    {letter}
                  </span>
                {/if}
              {/each}
            </div>
          {/each}
        </div>
      {/key}
    {/if}
    <span class="splash-title">de · con · struct · ed</span>
  </button>
{/if}

<style>
.splash-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background: #000;
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 9999;
  cursor: pointer;
  overflow: hidden;
  border: none;
  padding: 0;
  margin: 0;
  outline: none;
}
.splash-overlay:focus {
  outline: 2px solid #fff;
}
.letter-grid {
  position: absolute;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  display: flex;
  flex-direction: column;
  pointer-events: none;
}
.grid-row {
  display: flex;
}
.grid-letter {
  width: 100px;
  height: 100px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 2.5rem;
  color: #fff;
  opacity: 1;
  user-select: none;
  font-family: var(--font-serif, serif);
}
.splash-title {
  color: #fff;
  font-size: 3rem;
  font-family: var(--font-serif, serif);
  letter-spacing: 0.1em;
  user-select: none;
  z-index: 1;
}
</style> 