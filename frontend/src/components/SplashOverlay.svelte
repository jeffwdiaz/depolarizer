<script lang="ts">
  import { fade } from 'svelte/transition';
  import { onMount, tick } from 'svelte';
  let visible = $state(true);
  let mounted = $state(false);
  let gridKey = $state(0);

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
  let cells = $state<Cell[]>([]);
  let cols = $state(0);
  let rows = $state(0);

  function isMiddleCell(row: number, col: number): boolean {
    const middleRow = Math.floor(rows / 2);
    const startCol = Math.floor((cols - staticWord.length) / 2);
    return row === middleRow && col >= startCol && col < startCol + staticWord.length;
  }

  function getStaticLetter(col: number): string {
    const startCol = Math.floor((cols - staticWord.length) / 2);
    const letterIndex = col - startCol;
    return staticWord[letterIndex] || '';
  }

  function handleStaticLetterClick() {
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
    const newCells: Cell[] = [];
    for (let r = 0; r < rows; r++) {
      for (let c = 0; c < cols; c++) {
        const isStatic = isMiddleCell(r, c);
        newCells.push({
          row: r,
          col: c,
          letter: isStatic ? getStaticLetter(c) : letters[Math.floor(Math.random() * letters.length)],
          revealed: false,
          isStatic
        });
      }
    }
    cells = newCells;
  }

  function resetRevealedCells() {
    cells.forEach(cell => cell.revealed = false);
    cells = cells;
  }

  async function revealCellsStaggered() {
    const shuffledIndices = shuffle(cells.map((_, index) => index));
    for (const index of shuffledIndices) {
      cells[index].revealed = true;
      cells = cells;
      await new Promise(res => setTimeout(res, 40));
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
      }, 500);
    };

    updateGrid();

    window.addEventListener('resize', updateGrid);
    return () => window.removeEventListener('resize', updateGrid);
  });
</script>

{#if visible}
  <div class="splash-overlay" transition:fade={{ duration: 600 }}>
    {#if mounted}
      {#key gridKey}
        <div class="letter-grid" aria-hidden="true">
          {#each Array(rows) as _, rowIdx}
            <div class="grid-row">
              {#each Array(cols) as _, colIdx}
                {@const cellIndex = cells.findIndex(cell => cell.row === rowIdx && cell.col === colIdx)}
                {#if cellIndex !== -1}
                  {@const cell = cells[cellIndex]}
                  <span
                    class="grid-letter"
                    class:static={cell.isStatic && cell.revealed}
                    style="opacity: {cell.revealed ? 1 : 0}; transition: opacity 0.8s;"
                    transition:fade|local={{ duration: 800 }}
                    role={cell.isStatic ? "button" : undefined}
                    tabindex={cell.isStatic ? 0 : -1}
                    on:click={cell.isStatic ? handleStaticLetterClick : undefined}
                    on:keydown={(e) => { if (cell.isStatic && (e.key === 'Enter' || e.key === ' ')) handleStaticLetterClick() }}
                  >
                    {cell.letter}
                  </span>
                {/if}
              {/each}
            </div>
          {/each}
        </div>
      {/key}
    {/if}
  </div>
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
  pointer-events: auto;
  transition: opacity 0.8s, transform 0.2s ease;
  outline: none;
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
  cursor: pointer;
}
</style> 