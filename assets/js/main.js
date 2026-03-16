/* ============================================
   FAMAD PLC — Roofing Inspection Report
   Main JavaScript — Multi-Page Edition
   ============================================ */

(function () {
  'use strict';

  /* ---- Navbar scroll effect ---- */
  var navbar = document.getElementById('navbar');
  if (navbar) {
    window.addEventListener('scroll', function () {
      navbar.classList.toggle('scrolled', window.scrollY > 60);
    });
  }

  /* ---- Mobile nav toggle ---- */
  var navToggle = document.getElementById('navToggle');
  var navLinks  = document.getElementById('navLinks');

  if (navToggle && navLinks) {
    navToggle.addEventListener('click', function () {
      navLinks.classList.toggle('open');
    });

    navLinks.querySelectorAll('a').forEach(function (link) {
      link.addEventListener('click', function () {
        navLinks.classList.remove('open');
      });
    });
  }

  /* ---- Gallery thumbnails (structure detail pages) ---- */
  var fgMain   = document.querySelector('.fg-main');
  var thumbsEl = document.querySelectorAll('.fg-thumbs .thumb');

  if (fgMain && thumbsEl.length) {
    var slides = fgMain.querySelectorAll('img');

    thumbsEl.forEach(function (thumb, i) {
      thumb.addEventListener('click', function () {
        /* Deactivate all */
        slides.forEach(function (s) { s.classList.remove('active'); });
        thumbsEl.forEach(function (t) { t.classList.remove('active'); });
        /* Activate selected */
        if (slides[i]) { slides[i].classList.add('active'); }
        thumb.classList.add('active');
      });
    });
  }

  /* ---- Lightbox ---- */
  var lightbox = document.getElementById('lightbox');
  var lbImg    = document.getElementById('lbImg');
  var lbClose  = document.getElementById('lbClose');
  var lbPrev   = document.getElementById('lbPrev');
  var lbNext   = document.getElementById('lbNext');

  if (!lightbox) { return; }

  var lbImages = [];
  var lbIndex  = 0;

  function collectImages () {
    /* Collect all visible image srcs for lightbox navigation */
    lbImages = [];
    document.querySelectorAll(
      '.gal-item img, .meas-card img, .calc-img-wrap img, .fg-main img, .photo-gallery img'
    ).forEach(function (img) {
      if (img.src && !lbImages.includes(img.src)) {
        lbImages.push(img.src);
      }
    });
  }

  function openLightbox (src) {
    collectImages();
    lbIndex = lbImages.indexOf(src);
    if (lbIndex === -1) { lbIndex = 0; lbImages = [src]; }
    lbImg.src = lbImages[lbIndex];
    lightbox.classList.add('open');
    document.body.style.overflow = 'hidden';
  }

  function closeLightbox () {
    lightbox.classList.remove('open');
    document.body.style.overflow = '';
    lbImg.src = '';
  }

  function showAt (idx) {
    if (!lbImages.length) { return; }
    lbIndex = (idx + lbImages.length) % lbImages.length;
    lbImg.src = lbImages[lbIndex];
  }

  /* Click on any lightbox-trigger element */
  document.addEventListener('click', function (e) {
    var el = e.target;

    /* Direct img click inside a lightbox-trigger container */
    if (el.tagName === 'IMG') {
      var parent = el.closest('.lightbox-trigger, .meas-card, .gal-item, .calc-img-wrap');
      if (parent) { openLightbox(el.src); return; }
    }

    /* Click on fg-main active slide */
    if (el.tagName === 'IMG' && el.classList.contains('active') && el.closest('.fg-main')) {
      openLightbox(el.src); return;
    }

    /* Click directly on a lightbox-trigger img */
    if (el.tagName === 'IMG' && el.classList.contains('lightbox-trigger')) {
      openLightbox(el.src); return;
    }
  });

  lbClose.addEventListener('click', closeLightbox);
  lbPrev.addEventListener('click', function () { showAt(lbIndex - 1); });
  lbNext.addEventListener('click', function () { showAt(lbIndex + 1); });

  lightbox.addEventListener('click', function (e) {
    if (e.target === lightbox) { closeLightbox(); }
  });

  document.addEventListener('keydown', function (e) {
    if (!lightbox.classList.contains('open')) { return; }
    if (e.key === 'Escape')     { closeLightbox(); }
    if (e.key === 'ArrowLeft')  { showAt(lbIndex - 1); }
    if (e.key === 'ArrowRight') { showAt(lbIndex + 1); }
  });

  /* ---- Clickable table rows ---- */
  document.querySelectorAll('.site-table tbody tr[data-href]').forEach(function (row) {
    row.addEventListener('click', function () {
      window.location.href = row.getAttribute('data-href');
    });
  });

  /* ---- Scroll fade-in animation ---- */
  var fadeTargets = document.querySelectorAll(
    '.lcard, .env-card, .calc-card, .gal-item, .meas-card, .struct-index-card, .prop-table-wrap, .elevation-banner'
  );

  if ('IntersectionObserver' in window && fadeTargets.length) {
    fadeTargets.forEach(function (el) { el.classList.add('fade-in'); });

    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.08, rootMargin: '0px 0px -32px 0px' });

    fadeTargets.forEach(function (el) { observer.observe(el); });
  }

})();
