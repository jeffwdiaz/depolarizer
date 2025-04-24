<!-- =============================== -->
<!-- Filler Text Block Component     -->
<!-- A visual placeholder component that generates random-width lines
     to simulate text content. Used for mockups or loading states.    -->
<!-- =============================== -->

<script lang="ts">
  // Optional props to override the random ranges
  export let minParagraphs: number = 2;
  export let maxParagraphs: number = 4;
  export let minLinesPerParagraph: number = 3;
  export let maxLinesPerParagraph: number = 7;
  
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
  let paragraphLines = generateAllParagraphs();

  // Regenerate every 10-15 seconds for a dynamic effect
  setInterval(() => {
    paragraphLines = generateAllParagraphs();
  }, getRandomInt(20000, 60000));
</script>

<!-- Component Structure -->
<!-- Main container using module styling from global CSS -->
<div class="module filler-text-block">
  <!-- Content wrapper for line elements -->
  <div>
    <!-- Iterate through each paragraph -->
    {#each paragraphLines as paragraph}
      <div class="paragraph">
        <!-- Generate individual lines with dynamic widths -->
        {#each paragraph as lineWidth}
          <div class="line" style="width: {lineWidth}%"></div>
        {/each}
      </div>
    {/each}
  </div>
</div> 