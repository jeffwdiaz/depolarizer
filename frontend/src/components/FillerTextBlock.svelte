<!-- =============================== -->
<!-- Filler Text Block Component     -->
<!-- A visual placeholder component that generates random-width lines
     to simulate text content. Used for mockups or loading states.    -->
<!-- =============================== -->

<script lang="ts">
  import { onMount } from 'svelte';
  import { paragraphFade, lineFade, getStaggeredDelay } from './animations';
  
  // Optional props with default values
  const { 
    minParagraphs = 2,
    maxParagraphs = 4,
    minLinesPerParagraph = 3,
    maxLinesPerParagraph = 7
  } = $props();
  
  /**
   * Generates a random integer between min and max (inclusive)
   * @param {number} min - Minimum value
   * @param {number} max - Maximum value
   * @returns {number} Random integer within range
   */
  function getRandomInt(min: number, max: number): number {
    return Math.floor(Math.random() * (max - min + 1)) + min;
  }

  /**
   * Generates a random width value between specified min and max
   * @param {number} min - Minimum width percentage
   * @param {number} max - Maximum width percentage
   * @returns {number} A random width percentage
   */
  function generateRandomWidth(min: number, max: number): number {
    return Math.floor(Math.random() * (max - min) + min);
  }

  /**
   * Generates a random width for regular lines (30-100%)
   */
  function generateRegularLineWidth(): number {
    return generateRandomWidth(70, 100);
  }

  /**
   * Generates a random width for last lines (10-60%)
   */
  function generateLastLineWidth(): number {
    return generateRandomWidth(10, 90);
  }

  /**
   * Generates an array of random widths for a single paragraph
   * @returns {number[]} Array of width percentages for each line
   */
  function generateParagraphLines(): number[] {
    const numLines = getRandomInt(minLinesPerParagraph, maxLinesPerParagraph);
    return Array(numLines).fill(0).map((_, index) => 
      index === numLines - 1 ? generateLastLineWidth() : generateRegularLineWidth()
    );
  }

  /**
   * Generates the complete structure of paragraphs and their lines
   * @returns {number[][]} 2D array: paragraphs containing arrays of line widths
   */
  function generateAllParagraphs(): number[][] {
    const numParagraphs = getRandomInt(minParagraphs, maxParagraphs);
    return Array(numParagraphs).fill(0).map(() => generateParagraphLines());
  }

  // Generate initial random structure
  let paragraphLines = $state(generateAllParagraphs());
  let visible = $state(true);

  // Regenerate every 10-15 seconds for a dynamic effect
  setInterval(() => {
    visible = false;
    setTimeout(() => {
      paragraphLines = generateAllParagraphs();
      visible = true;
    }, 200);
  }, getRandomInt(20000, 60000));

  onMount(() => {
    visible = true;
  });
</script>

<!-- Component Structure -->
<!-- Main container using module styling from global CSS -->
<div class="module filler-text-block">
  <!-- Content wrapper for line elements -->
  <div>
    {#if visible}
      <!-- Iterate through each paragraph -->
      {#each paragraphLines as paragraph, pIndex}
        <div 
          class="paragraph"
          in:paragraphFade={{ delay: getStaggeredDelay(pIndex, 100) }}
        >
          <!-- Generate individual lines with dynamic widths -->
          {#each paragraph as lineWidth, lIndex}
            <div 
              class="line" 
              style="width: {lineWidth}%"
              in:lineFade={{ 
                delay: getStaggeredDelay(pIndex * paragraph.length + lIndex) 
              }}
            ></div>
          {/each}
        </div>
      {/each}
    {/if}
  </div>
</div>

<style>
.filler-text-block {
  background-color: var(--color-text);
}

.line {
  height: 0.8em;
  background-color: var(--secondary);
  margin-bottom: 0.5em;
  border-radius: 2px;
}

.line:last-child {
  margin-bottom: 0;
}

.paragraph {
  margin-bottom: 1em;
}

.paragraph:last-child {
  margin-bottom: 0;
}
</style> 