<!-- =============================== -->
<!-- LoadingDots Component           -->
<!-- Simple visual loading indicator -->
<!-- =============================== -->

<script lang="ts">
  import { onMount, onDestroy } from 'svelte';
  import { fade } from 'svelte/transition'; // Import fade

  let rotationAngle = 45; // State for rotation angle, start at 90 degrees
  let squareIntervalId: ReturnType<typeof setInterval>; // ID for the new interval

  onMount(() => {
    // Rotate square every 500ms
    squareIntervalId = setInterval(() => {
      rotationAngle += 90; // Increment angle by 90
    }, 1000);

    // Cleanup function
    return () => {
      clearInterval(squareIntervalId); // Clear the new interval
    };
  });
</script>

<!-- Container for centering -->
<div class="center-container module-light">
  <!-- Rotating Square -->
  <div 
    class="rotating-square" 
    style="transform: rotate({rotationAngle}deg);"
  ></div>
</div>

<style>
  /* =============================== */
  /* Rotating Square Styles          */
  /* =============================== */
  .rotating-square {
    width: 50px; /* Size of the square */
    height: 50px;
    background-color: black; /* Color of the square */
    margin: auto; /* Center within the container */
    transition: transform 0.7s ease-in-out; /* Smooth rotation transition */
  }

  /* =============================== */
  /* Centering Container Styles      */
  /* =============================== */
  .center-container {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    /* Ensure it doesn't stretch unexpectedly */
    width: fit-content;
    height: fit-content;
  }
</style> 