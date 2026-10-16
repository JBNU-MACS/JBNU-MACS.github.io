(() => {
  const root = document.getElementById('publications-index');
  if (!root) return;
  const buttons = [...root.querySelectorAll('.publications-filter [data-kind]')];
  const categories = [...root.querySelectorAll('[data-category]')];
  const years = [...root.querySelectorAll('[data-publication-year]')];
  const yearSelect = root.querySelector('[data-publication-year-select]');
  const fieldSelect = root.querySelector('[data-publication-field-select]');
  const entries = [...root.querySelectorAll('.publication-entry')];
  const ko = root.dataset.language === 'ko';
  const countLabel = n => ko ? `${n}편` : `${n} ${n === 1 ? 'paper' : 'papers'}`;
  const validOption = (select, value) => [...select.options].some(option => option.value === value) ? value : 'all';
  let kind = 'all';

  const readURL = () => {
    const params = new URLSearchParams(window.location.search);
    fieldSelect.value = validOption(fieldSelect, params.get('field'));
    yearSelect.value = validOption(yearSelect, params.get('year'));
    kind = buttons.some(button => button.dataset.kind === params.get('kind')) ? params.get('kind') : 'all';
  };
  const writeURL = () => {
    const url = new URL(window.location.href);
    for (const [key, value] of Object.entries({field: fieldSelect.value, year: yearSelect.value, kind})) {
      if (value === 'all') url.searchParams.delete(key);
      else url.searchParams.set(key, value);
    }
    if (url.href !== window.location.href) window.history.pushState(null, '', url);
  };
  const applyFilters = () => {
    const matchesFieldAndYear = entry =>
      (fieldSelect.value === 'all' || (entry.dataset.fields || '').split(' ').includes(fieldSelect.value)) &&
      (yearSelect.value === 'all' || entry.closest('[data-publication-year]').dataset.year === yearSelect.value);
    entries.forEach(entry => {
      entry.hidden = !matchesFieldAndYear(entry) || (kind !== 'all' && entry.dataset.kind !== kind);
    });
    buttons.forEach(button => {
      button.setAttribute('aria-pressed', String(button.dataset.kind === kind));
      button.querySelector('span').textContent = entries.filter(entry => matchesFieldAndYear(entry) && (button.dataset.kind === 'all' || entry.dataset.kind === button.dataset.kind)).length;
    });
    categories.forEach(category => {
      const count = [...category.querySelectorAll('.publication-entry')].filter(entry => !entry.hidden).length;
      category.hidden = count === 0;
      category.querySelector('.publications-category-count').textContent = countLabel(count);
    });
    years.forEach(year => {
      const count = [...year.querySelectorAll('.publication-entry')].filter(entry => !entry.hidden).length;
      year.hidden = count === 0;
      year.querySelector('[data-year-count]').textContent = countLabel(count);
    });
    const additional = root.querySelector('[data-other-publications]');
    if (additional) {
      const count = [...additional.querySelectorAll('.publication-entry')].filter(entry => !entry.hidden).length;
      additional.hidden = count === 0;
      additional.querySelector('[data-additional-count]').textContent = countLabel(count);
    }
    const count = entries.filter(entry => !entry.hidden).length;
    root.querySelector('[data-publication-empty]').hidden = count !== 0;
    const label = fieldSelect.selectedOptions[0].textContent;
    root.querySelector('[data-publication-result]').textContent = `${label} · ${countLabel(count)}`;
  };
  const update = () => { applyFilters(); writeURL(); };
  buttons.forEach(button => button.addEventListener('click', () => { kind = button.dataset.kind; update(); }));
  yearSelect.addEventListener('change', update);
  fieldSelect.addEventListener('change', update);
  root.querySelector('[data-publication-reset]').addEventListener('click', () => {
    kind = 'all'; yearSelect.value = 'all'; fieldSelect.value = 'all'; update();
  });
  window.addEventListener('popstate', () => { readURL(); applyFilters(); });
  readURL();
  applyFilters();
})();
