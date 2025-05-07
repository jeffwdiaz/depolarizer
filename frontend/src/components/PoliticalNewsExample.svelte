<!-- =============================== -->
<!-- Political News Example Component -->
<!-- Displays a real political news article -->
<!-- =============================== -->
<script lang="ts">
  import { onMount } from 'svelte';
  let article: any = null;
  let loading = false;
  let error = '';
  let files: string[] = [];
  let selectedFile = '';

  // Fetch the list of article JSON files on mount
  onMount(async () => {
    loading = true;
    error = '';
    try {
      const res = await fetch('/backend/list_articles');
      if (!res.ok) throw new Error('Failed to load article list');
      const data = await res.json();
      files = data.files;
      if (files.length > 0) {
        selectedFile = files[0];
        await loadArticle(selectedFile);
      }
    } catch (e) {
      error = (e as Error).message || 'Unknown error';
    } finally {
      loading = false;
    }
  });

  async function loadArticle(filename: string) {
    loading = true;
    error = '';
    article = null;
    try {
      const res = await fetch(`/backend/article_json?filename=${filename}`);
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
    <div>Loading...</div>
  {:else if error}
    <div class="error">{error}</div>
  {:else}
    {#if article}
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
        {#if article.top_image}
          <img src={article.top_image} alt="Article image" class="article-image" />
        {/if}
        <div class="article-body">
          {#each article.text.split('\n') as para, i (i)}
            {#if para.trim()}
              <p>{para}</p>
            {/if}
          {/each}
        </div>
        {#if article.url}
          <p><a href={article.url} target="_blank" rel="noopener">Read the original article</a></p>
        {/if}
      </article>
    {/if}
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