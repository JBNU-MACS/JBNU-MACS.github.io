(() => {
  document.querySelectorAll('[data-home-notices]').forEach(root => {
    const panel = root.querySelector('[data-notice-panel]');
    const open = root.querySelector('[data-notice-open]');
    const key = 'macs-notices-collapsed';
    const collapse = value => {
      panel.hidden = value;
      open.hidden = !value;
      open.setAttribute('aria-expanded', String(!value));
    };
    const navigation = performance.getEntriesByType('navigation')[0];
    let internal = false;
    try { internal = new URL(document.referrer).origin === location.origin; } catch (_) {}
    const freshEntry = navigation?.type === 'reload' ||
      (navigation?.type !== 'back_forward' && !internal);
    try {
      if (freshEntry) sessionStorage.removeItem(key);
      collapse(sessionStorage.getItem(key) === 'true');
    } catch (_) { collapse(false); }
    root.querySelector('[data-notice-close]').addEventListener('click', () => {
      collapse(true);
      try { sessionStorage.setItem(key, 'true'); } catch (_) {}
      open.focus();
    });
    open.addEventListener('click', () => {
      collapse(false);
      try { sessionStorage.removeItem(key); } catch (_) {}
      root.querySelector('[data-notice-close]').focus();
    });
    window.addEventListener('pageshow', event => {
      if (!event.persisted) return;
      try { collapse(sessionStorage.getItem(key) === 'true'); } catch (_) {}
    });
  });
})();
