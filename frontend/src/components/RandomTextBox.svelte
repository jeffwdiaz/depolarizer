<!-- =============================== -->
<!-- Random Text Box Component       -->
<!-- Generates static random text that looks like actual paragraphs -->
<!-- =============================== -->

<script lang="ts">
  // REMOVED: import { fade } from 'svelte/transition';
  // REMOVED: import { onMount, tick } from 'svelte';
  // import { fly } from 'svelte/transition';

  // Props with default values
  export let minWordsPerSentence = 4;
  export let maxWordsPerSentence = 12;
  export let minSentencesPerParagraph = 2;
  export let maxSentencesPerParagraph = 5;
  export let paragraphs = 2;
  
  // REMOVED: Animation Timing Configuration constants

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

  // Generate text directly
  let text = generateText();

  // REMOVED: onMount block

</script>

<div class="random-text">
  {#each text as paragraph}
    <p>
      {paragraph} <!-- Render paragraph directly -->
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