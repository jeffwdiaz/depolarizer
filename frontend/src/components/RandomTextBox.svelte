<!-- =============================== -->
<!-- Random Text Box Component       -->
<!-- Generates static random text that looks like actual paragraphs -->
<!-- =============================== -->

<script lang="ts">
  // Optional props with default values
  const { 
    minWordsPerSentence = 4,
    maxWordsPerSentence = 12,
    minSentencesPerParagraph = 2,
    maxSentencesPerParagraph = 5,
    paragraphs = 2
  } = $props();
  
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

  const text = generateText();
</script>

<div>
  {#each text as paragraph}
    <p>
      {paragraph}
    </p>
  {/each}
</div>

<style>
  p {
    margin: 0 0 1em 0;
  }
  p:last-child {
    margin-bottom: 0;
  }
</style> 