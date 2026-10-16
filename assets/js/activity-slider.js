(() => {
  document.querySelectorAll('[data-activity-slider]').forEach(root => {
    if (root.dataset.ready) return;
    root.dataset.ready = 'true';
    const slides = [...root.querySelectorAll('[data-slide]')];
    const count = root.querySelector('[data-slide-count]');
    const dots = [...root.querySelectorAll('[data-slide-index]')];
    const toggle = root.querySelector('[data-toggle]');
    const ko = document.documentElement.lang.startsWith('ko');
    const motion = window.matchMedia('(prefers-reduced-motion: reduce)');
    let current = 0, playing = false, timer;
    const show = index => {
      current = (index + slides.length) % slides.length;
      slides.forEach((slide, i) => { slide.hidden = i !== current; });
      dots.forEach((dot, i) => dot.setAttribute('aria-pressed', String(i === current)));
      count.textContent = `${current + 1} / ${slides.length}`;
    };
    const stopTimer = () => { clearInterval(timer); };
    const startTimer = () => {
      stopTimer();
      if (playing && !document.hidden && !root.matches(':hover') && !root.contains(document.activeElement)) {
        timer = setInterval(() => show(current + 1), 6000);
      }
    };
    const setPlaying = value => {
      playing = value;
      toggle.setAttribute('aria-pressed', String(playing));
      toggle.textContent = ko ? (playing ? '정지' : '재생') : (playing ? 'Pause' : 'Play');
      startTimer();
    };
    root.querySelector('[data-prev]').addEventListener('click', () => { show(current - 1); startTimer(); });
    root.querySelector('[data-next]').addEventListener('click', () => { show(current + 1); startTimer(); });
    dots.forEach((dot, i) => dot.addEventListener('click', () => { show(i); startTimer(); }));
    toggle.addEventListener('click', () => setPlaying(!playing));
    root.addEventListener('mouseenter', stopTimer);
    root.addEventListener('mouseleave', startTimer);
    root.addEventListener('focusin', stopTimer);
    root.addEventListener('focusout', () => requestAnimationFrame(startTimer));
    document.addEventListener('visibilitychange', startTimer);
    motion.addEventListener('change', () => { if (motion.matches) setPlaying(false); });
    setPlaying(!motion.matches);
  });
})();
