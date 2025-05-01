<!-- =============================== -->
<!-- Random Text Box Component       -->
<!-- Generates static random text that looks like actual paragraphs -->
<!-- =============================== -->

<script lang="ts">
  import { fade } from 'svelte/transition'; // Re-import fade
  import { onMount } from 'svelte'; // Import onMount for interval cleanup

  // Props with default values
  export let minWordsPerSentence = 4;
  export let maxWordsPerSentence = 12;
  export let minSentencesPerParagraph = 2;
  export let maxSentencesPerParagraph = 5;
  export let paragraphs = 2;
  
  // Animation Timing Configuration
  const delayIncrement = 50; // ms delay between each character start (Increased)
  const fadeDuration = 50;   // ms duration for each character fade (Matched to increment)

  const letters = 'abcdefghijklmnopqrstuvwxyz';
  
  /**
   * Generates a random integer between min and max (inclusive)
   */
  function getRandomInt(min: number, max: number): number {
    return Math.floor(Math.random() * (max - min + 1)) + min;
  }

  /**
   * Generates a random word with random length (3-10 characters)
   */
  function generateWord(): string {
    const length = getRandomInt(3, 10);
    return Array(length)
      .fill(0)
      .map(() => letters[Math.floor(Math.random() * letters.length)])
      .join('');
  }

  /**
   * Generates a random sentence with random number of words
   */
  function generateSentence(): string {
    const numWords = getRandomInt(minWordsPerSentence, maxWordsPerSentence);
    const words = Array(numWords).fill(0).map(() => generateWord());
    return words.join(' ') + '.';
  }

  /**
   * Generates a paragraph with random number of sentences
   */
  function generateParagraph(): string {
    const numSentences = getRandomInt(minSentencesPerParagraph, maxSentencesPerParagraph);
    const sentences = Array(numSentences).fill(0).map(() => generateSentence());
    return sentences.join(' ');
  }

  /**
   * Generates all paragraphs
   */
  function generateText(): string[] {
    return Array(paragraphs).fill(0).map(() => generateParagraph());
  }

  // Holds the raw generated paragraphs
  let rawText: string[] = [];

  // Holds characters with their delays for rendering
  type CharInfo = { char: string; delay: number }; // Use delay again
  type ParagraphInfo = CharInfo[];
  let displayedText: ParagraphInfo[] = [];

  // Function to update text and calculate delays
  function updateText() {
    rawText = generateText();
    let charIndex = 0;
    // Removed timing config from here

    displayedText = rawText.map(paragraph => {
      const paragraphChars: CharInfo[] = [];
      for (const char of paragraph) {
        // Calculate the start delay for this character
        paragraphChars.push({ char, delay: charIndex * delayIncrement });
        charIndex++;
      }
      // Optional: add gap between paragraph animations
      // charIndex += Math.round(50 / delayIncrement); // Add gap equivalent to ~50ms
      return paragraphChars;
    });
  }

  // Initial generation
  updateText();

  // Set up refresh interval if specified and clean up on destroy
  onMount(() => {
    // Cleanup function
    return () => {
    };
  });
</script>

<div class="module random-text">
  {#each displayedText as paragraphData, pIndex}
    <p>
      {#each paragraphData as { char, delay }, cIndex (pIndex + '-' + cIndex)}
        <span transition:fade={{ delay, duration: fadeDuration }}>{char}</span>
      {/each}
    </p>
  {/each}
</div>

<style>
  /* =============================== */
  /* Component Styles              */
  /* =============================== */
  .random-text {
    font-family: var(--font-sans-serif);
    border: none;
    margin: 0;
    padding: 0;
  }
  
  p {
    margin: 0 0 1em 0;
    line-height: 1.5;
  }
  
  p:last-child {
    margin-bottom: 0;
  }
</style> 