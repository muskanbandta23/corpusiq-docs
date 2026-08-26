// Renders a visible "Last updated: YYYY-MM-DD" line under the page H1 from the
// last-updated meta tag (set in overrides/main.html from frontmatter).
// AEO/SEO freshness signal: visible dates correlate with citation + trust.
(function () {
  function inject() {
    var meta = document.querySelector('meta[name="last-updated"]');
    if (!meta || !meta.content) return;
    if (document.querySelector('.md-last-updated')) return;
    var h1 = document.querySelector('.md-content__inner h1');
    if (!h1) return;
    var p = document.createElement('p');
    p.className = 'md-last-updated';
    p.style.cssText = 'margin:0 0 1.2em;font-size:0.8em;color:var(--md-default-fg-color--light);';
    p.textContent = 'Last updated: ' + meta.content;
    h1.insertAdjacentElement('afterend', p);
  }
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', inject);
  } else {
    inject();
  }
})();
