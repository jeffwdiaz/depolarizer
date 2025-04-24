<!-- =============================== -->
<!-- Filler Image Block Component    -->
<!-- A visual placeholder component that generates two random-width lines
     to simulate image content. Used for mockups or loading states.    -->
<!-- =============================== -->

<script lang="ts">
  // Optional props to override the random ranges
  export let minWidth: number = 70;
  export let maxWidth: number = 100;
  export let height: string = "0.8em";
  export let gap: string = "0.5em";
  
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
   * Generates widths for both lines
   * @returns {{ first: number, second: number }} Object containing widths for both lines
   */
  function generateWidths() {
    return {
      first: getRandomInt(minWidth, maxWidth),
      second: getRandomInt(minWidth, maxWidth)
    };
  }

  // Generate initial widths
  let widths = generateWidths();

  // Regenerate every 10-15 seconds for a dynamic effect
  setInterval(() => {
    widths = generateWidths();
  }, getRandomInt(10000, 15000));
</script>

<!-- Component Structure -->
<!-- Main container using module styling from global CSS -->
<div class="module filler-image-block">
  <!-- Two lines with dynamic widths -->
  <div 
    class="line"
    style="height: {height}; width: {widths.first}%; margin-bottom: {gap};"
  >
  </div>
  <div 
    class="line"
    style="height: {height}; width: {widths.second}%"
  >
  </div>
</div> 