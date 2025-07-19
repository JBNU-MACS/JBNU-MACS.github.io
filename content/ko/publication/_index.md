---
title: Publications

# Optional banner image (relative to `assets/media/` folder).
banner:
  caption: 'Image credit: [**Unsplash**](https://unsplash.com/)'
  image: 'researchpaper.jpg'
---

<style>
.form-row {
  display: none !important;
}

#container-publications {
  display: none !important;
}

h2 {
  font-weight: bolder;
}

.glass-toggle-btn {
      padding: 18px 40px;
      font-size: 20px;
      font-weight: 600;
      color: #fff;
      background: rgba(255, 255, 255, 0.18);
      border: none;
      border-radius: 18px;
      box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.18);
      backdrop-filter: blur(10px);
      -webkit-backdrop-filter: blur(10px);
      outline: none;
      cursor: pointer;
      transition: background 0.25s, color 0.25s;
      text-shadow: 0 1px 2px rgba(31, 38, 135, 0.18);
}
.glass-toggle-btn:hover {
  background: rgba(255, 255, 255, 0.28);
  color: #4F8EF7;
}
</style>

<script>
  const btn = document.getElementById('toggleBtn');
  btn.addEventListener('click', function() {
    if (btn.textContent === 'ref') {
      btn.textContent = 'showcase';
    } else {
      btn.textContent = 'ref';
    }
  });
</script>

<button class="glass-toggle-btn" id="toggleBtn">ref</button>

{{< publications_by_type >}}