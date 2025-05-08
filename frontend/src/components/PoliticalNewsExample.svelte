<!-- =============================== -->
<!-- Political News Example Component -->
<!-- Displays a real political news article -->
<!-- =============================== -->
<script lang="ts">
  import { onMount } from 'svelte';
  import LoadingDots from './LoadingDots.svelte';
  import { fade } from 'svelte/transition';
  let article: any = null;
  let loading = false;
  let error = '';
  let files: string[] = [];
  let selectedFile = '';
  let articles: any[] = [];

  // Fetch the list of article JSON files on mount
  onMount(async () => {
    loading = true;
    error = '';
    try {
      // Trigger backend scraping
      const scrapeRes = await fetch('/backend/scrape_politics', { method: 'POST' });
      if (!scrapeRes.ok) throw new Error('Failed to start scraping');
      // Wait for scraping to finish (poll for files)
      let attempts = 0;
      let maxAttempts = 30; // ~30 seconds
      while (attempts < maxAttempts) {
        const res = await fetch('/backend/list_articles');
        if (res.ok) {
          const data = await res.json();
          if (data.files && data.files.length > 0) {
            files = data.files;
            break;
          }
        }
        await new Promise(r => setTimeout(r, 1000));
        attempts++;
      }
      if (files.length === 0) throw new Error('No articles found after scraping');
      // Load all articles and store in articles array
      articles = [];
      for (let i = 0; i < files.length; i++) {
        const file = files[i];
        try {
          const res = await fetch(`/backend/highlight_article?filename=${file}`);
          if (res.ok) {
            const art = await res.json();
            articles.push(art);
          }
        } catch (e) {
          // Skip failed articles
        }
      }
    } catch (e) {
      error = (e as Error).message || 'Unknown error';
    } finally {
      loading = false;
    }
  });

  // Fetch the highlighted article from the backend
  async function loadArticle(filename: string) {
    loading = true;
    error = '';
    article = null;
    try {
      const res = await fetch(`/backend/highlight_article?filename=${filename}`);
      if (!res.ok) throw new Error('Failed to load article');
      article = await res.json();
    } catch (e) {
      error = (e as Error).message || 'Unknown error';
    } finally {
      loading = false;
    }
  }
</script>

<div class="content-viewer">
  {#if loading}
    <div in:fade><LoadingDots /></div>
  {:else if error}
    <div class="error">{error}</div>
  {:else}
    {#each articles as article}
      <article>
        <h2>{article.title}</h2>
        <div class="article-meta">
          <span>
            {#if article.authors && article.authors.length}
              By {article.authors.join(', ')} |
            {/if}
            {article.publish_date ? new Date(article.publish_date).toLocaleDateString() : ''}
          </span>
        </div>
        <div class="article-body">
          {@html article.highlighted_text || article.text}
        </div>
        {#if article.url}
          <p><a href={article.url} target="_blank" rel="noopener">Read the original article</a></p>
        {/if}
      </article>
    {/each}
  {/if}
</div>

<style>
.content-viewer {
  padding: 20px;
  font-family: var(--font-sans-serif);
}

.article-list {
  margin-bottom: 1.5rem;
}

label {
  font-weight: bold;
  margin-right: 0.5rem;
}

select {
  font-size: 1rem;
  padding: 0.3rem 0.5rem;
  border-radius: 4px;
  border: 1px solid #ccc;
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

.article-image {
  max-width: 100%;
  margin-bottom: 1.5rem;
  border-radius: 8px;
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

.error {
  color: red;
  font-weight: bold;
}
</style> 