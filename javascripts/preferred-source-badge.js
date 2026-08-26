// Google Preferred Sources badge injector for the CorpusIQ docs site.
// Injects the "Add to Preferred Sources" button (dark theme) at the end of
// the page content, then loads Google's publisher.js library which renders
// the badge. See https://developers.google.com/search/docs/appearance/preferred-sources
(function () {
  function loadPublisher() {
    if (document.querySelector('script[src*="publisher.js"]')) return;
    var s = document.createElement('script');
    s.async = true;
    s.src = 'https://news.google.com/swg/js/v1/publisher.js';
    document.head.appendChild(s);
  }

  function injectBadge() {
    if (document.querySelector('[google-add-preferred-source-btn]')) {
      loadPublisher();
      return true;
    }
    var container = document.querySelector('.md-content__inner');
    if (!container) return false;

    var div = document.createElement('div');
    div.setAttribute('google-add-preferred-source-btn', '');
    div.setAttribute('data-theme', 'dark');
    div.style.margin = '32px 0 8px';
    div.style.paddingTop = '24px';
    div.style.borderTop = '1px solid #e2e8f0';
    container.appendChild(div);

    var p = document.createElement('p');
    p.style.cssText = 'font-size:12px;color:#627d98;margin:10px 0 0;';
    var a = document.createElement('a');
    a.href = 'https://www.google.com/preferences/source?q=https://corpusiq.io';
    a.textContent = 'Add corpusiq.io as a preferred source in Google';
    a.style.cssText = 'color:#627d98;text-decoration:underline;';
    p.appendChild(a);
    div.appendChild(p);

    loadPublisher();
    return true;
  }

  if (!injectBadge()) {
    var obs = new MutationObserver(function () {
      if (injectBadge()) obs.disconnect();
    });
    obs.observe(document.body, { childList: true, subtree: true });
    setTimeout(function () { obs.disconnect(); }, 15000);
  }
})();
