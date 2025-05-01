<script lang="ts">
  import { fade } from 'svelte/transition';
  import { onMount, tick } from 'svelte';
  let visible = true;
  let mounted = false;
  let gridKey = 0;

  // Letters to use in the grid
  const letters = ['d', 'e', 'c', 'o', 'n', 's', 't', 'r', 'u'];
  
  // Static word in the middle
  const staticWord = 'deconstructed';
  
  type Cell = {
    row: number;
    col: number;
    letter: string;
    revealed: boolean;
    isStatic: boolean;
  };
  let cells: Cell[] = [];
  let cols = 0;
  let rows = 0;

  function isMiddleCell(row: number, col: number): boolean {
    const middleRow = Math.floor(rows / 2);
    const startCol = Math.floor((cols - 13) / 2);
    return row === middleRow && col >= startCol && col < startCol + 13;
  }

  function getStaticLetter(col: number): string {
    const startCol = Math.floor((cols - 13) / 2);
    const letterIndex = col - startCol;
    return staticWord[letterIndex] || '';
  }

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

  function generateCells() {
    cols = Math.ceil(window.innerWidth / 50);
    rows = Math.ceil(window.innerHeight / 50);
    cells = [];
    for (let r = 0; r < rows; r++) {
      for (let c = 0; c < cols; c++) {
        const isStatic = isMiddleCell(r, c);
        cells.push({
          row: r,
          col: c,
          letter: isStatic ? getStaticLetter(c) : letters[Math.floor(Math.random() * letters.length)],
          revealed: false,
          isStatic
        });
      }
    }
  }

  function resetRevealedCells() {
    for (const cell of cells) {
      cell.revealed = false;
    }
  }

  async function revealCellsStaggered() {
    const shuffled = shuffle([...cells]); // Include all cells in the animation
    for (const cell of shuffled) {
      const originalCell = cells.find(c => c.row === cell.row && c.col === cell.col);
      if (originalCell) {
        originalCell.revealed = true;
        cells = cells; // Trigger Svelte reactivity
        await tick();
        await new Promise(res => setTimeout(res, 40));
      }
    }
  }

  onMount(() => {
    const updateGrid = async () => {
      mounted = false;
      gridKey += 1;
      await tick();
      generateCells();
      resetRevealedCells();
      await tick();
      setTimeout(async () => {
        mounted = true;
        await tick();
        revealCellsStaggered();
      }, 1000);
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
          {#each Array(rows) as _, rowIdx}
            <div class="grid-row">
              {#each Array(cols) as _, colIdx}
                {@const cell = cells.find(cell => cell.row === rowIdx && cell.col === colIdx)}
                <span
                  class="grid-letter"
                  class:static={cell?.isStatic && cell?.revealed}
                  style="opacity: {cell && cell.revealed ? 1 : 0}; transition: opacity 0.8s;"
                  transition:fade|local={{ duration: 800 }}
                >
                  {cell ? cell.letter : ''}
                </span>
              {/each}
            </div>
          {/each}
        </div>
      {/key}
    {/if}
    <span class="splash-title"></span>
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
  width: 50px;
  height: 50px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 2rem;
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
.grid-letter.static {
  color: var(--accent, #fd3232);
  font-weight: bold;
  opacity: 1 !important;
}
</style> 