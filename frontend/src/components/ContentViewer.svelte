<!-- =============================== -->
<!-- Content Viewer Component        -->
<!-- Displays article content with   -->
<!-- polarizing language detection   -->
<!-- =============================== -->
<script lang="ts">
  import UrlInput from './UrlInput.svelte';
  import { fly } from 'svelte/transition';
</script>

<div class="content-viewer" in:fly={{ y: -500, duration: 1000, delay: 500 }}>
  <article>
    <h2>Comer Refers Cuomo to DOJ for Criminal Prosecution</h2>
    
    <div class="article-meta">
      <span>By Mark Swanson | Monday, 21 April 2025 04:25 PM EDT</span>
    </div>

    <div class="article-body">
      <p>
        House Oversight Committee Chairman James Comer, R-Ky., resent a criminal referral to the Department of Justice on Monday recommending that former New York Gov. Andrew Cuomo be charged with making false statements to Congress.
      </p>
      <p>
        Comer charges that Cuomo, a Democrat, "knowingly and willfully" lied to the House Select Subcommittee about his knowledge and involvement of a 2020 report regarding the COVID-19 "nursing home <span class="polarizing-language">disaster</span>" and "the ensuing <span class="polarizing-language">cover-up</span>."
      </p>
      <p>
        Comer and Select Committee Republicans assert that Cuomo took an active role in drafting and editing the New York State Department of Health report to dodge responsibility for the thousands of lost lives during the pandemic.
      </p>
      <p>
        "Andrew Cuomo is a man with a history of <span class="polarizing-language">corruption</span> and <span class="polarizing-language">deceit</span>, now caught <span class="polarizing-language">red-handed</span> lying to Congress during the Select Subcommittee's investigation into the COVID-19 nursing home <span class="polarizing-language">tragedy</span> in New York. This wasn't a slip-up — it was a <span class="polarizing-language">calculated cover-up</span> by a man seeking to shield himself from responsibility for the <span class="polarizing-language">devastating</span> loss of life in New York's nursing homes," Comer said in a Monday release.
      </p>
      <p>
        Cuomo is polling as one of the top Democrat candidates in the New York City mayoral race. The election is Nov. 4.
      </p>
      <p>
        Select Committee Chairman Brad Wenstrup, R-Ohio, sent a criminal referral against Cuomo dated Oct. 30 to former Attorney General Merrick Garland asserting that Cuomo made false statements in a transcribed interview with the committee on June 11.
      </p>
    </div>
  </article>
  
</div>

<style>
  .content-viewer {
    padding: 20px;
    font-family: var(--font-sans-serif);
  }

  h2 {
    font-size: 1.5rem;
    text-align: left;
    margin: 0 0 1rem 0;
    padding: 20px 0 20px 0;
    line-height: 1.2;
    background-color: var(--color-light);
    color: var(--color-dark);
  }

  .article-meta {
    font-size: 0.9rem;
    color: var(--color-dark);
    margin-bottom: 1.5rem;
  }

  .article-body {
    line-height: 1.6;
  }

  p {
    margin: 0 0 1rem 0;
  }

  p:last-child {
    margin-bottom: 0;
  }

  .polarizing-language {
    display: inline-block;
    color: var(--color-highlight);
    font-size: 1rem;
    font-style: italic;
  }

  .url-input-container {
    margin-top: 2rem;
  }

  /* Remove paragraph fade-in animation */
  /* @keyframes fadeInParagraph { ... } */
  /* .article-body p { ... } */
  /* .article-body p:nth-child(...) { ... } */
</style> 