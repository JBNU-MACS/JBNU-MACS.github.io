---
title: Publications


# Listing view
view: community/custom_compact

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
  opacity: 0;
  transition: opacity 0.3s;
}

h2 {
  font-weight: bolder;
}

.article-banner {
  height: 200px;
}

.btn-row {
  display: flex;
  justify-content: flex-end;
  align-items: center;
  width: 100%;
  padding: 12px 8px 0 0;
  box-sizing: border-box;
}
.glass-toggle-btn {
  padding: 4px 16px;
  font-size: 16px;
  font-weight: 500;
  color: #222;
  min-width: 80px;
  background: rgba(255, 255, 255, 0.32);
  border: none;
  border-radius: 16px;
  box-shadow: 0 4px 16px 0 rgba(80, 100, 200, 0.08);
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
  outline: none;
  cursor: pointer;
  transition: background 0.18s, color 0.18s, box-shadow 0.18s;
  text-shadow: 0 2px 8px rgba(200, 210, 255, 0.16);
}
.glass-toggle-btn:hover {
  background: rgba(255, 255, 255, 0.5);
  color: #4F8EF7;
  box-shadow: 0 6px 20px 0 rgba(80, 100, 200, 0.15);
}

#publication-container {
  transition: opacity 0.3s;
}

.hidden-by-opacity {
  opacity: 0 !important;
  max-height: 0 !important;
  pointer-events: none !important;
}
.visible-by-opacity {
  opacity: 1 !important;
  height: auto !important;
  pointer-events: auto !important;
  overflow: visible !important;
  display: block !important;
}
</style>

{{< publications_by_type >}}