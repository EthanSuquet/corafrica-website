/* CORAfrica — minimal progressive enhancement.
   The site is fully readable and navigable with JS disabled; this only
   drives the mobile menu. */
(function () {
  "use strict";

  var toggle = document.querySelector("[data-nav-toggle]");
  var nav = document.querySelector("[data-nav]");
  if (!toggle || !nav) return;

  var mq = window.matchMedia("(max-width: 639px)");

  function setOpen(open) {
    toggle.setAttribute("aria-expanded", open ? "true" : "false");
    nav.classList.toggle("is-open", open);
    document.body.style.overflow = open ? "hidden" : "";
  }

  function isOpen() {
    return toggle.getAttribute("aria-expanded") === "true";
  }

  toggle.addEventListener("click", function () {
    setOpen(!isOpen());
  });

  // Following a link closes the menu.
  nav.addEventListener("click", function (e) {
    if (e.target.closest("a")) setOpen(false);
  });

  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape" && isOpen()) {
      setOpen(false);
      toggle.focus();
    }
  });

  document.addEventListener("click", function (e) {
    if (!isOpen()) return;
    if (nav.contains(e.target) || toggle.contains(e.target)) return;
    setOpen(false);
  });

  // Leaving the mobile breakpoint must not strand the page in a locked state.
  function onChange() {
    if (!mq.matches) setOpen(false);
  }
  if (mq.addEventListener) mq.addEventListener("change", onChange);
  else if (mq.addListener) mq.addListener(onChange);
})();

/* ---------------------------------------------------------------- motion
   Scroll reveals, a header state, and counting stat numbers.

   Everything here is additive: the `js-anim` class on <html> is what switches
   the CSS on, so if this file fails to load the page renders fully visible.
   All of it bails under prefers-reduced-motion. No dependencies — the Teeej
   sites use GSAP + ScrollTrigger, which is not worth 100KB here. */
(function () {
  "use strict";

  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var root = document.documentElement;
  root.classList.add("js-anim");

  if (reduce || !("IntersectionObserver" in window)) {
    [].forEach.call(document.querySelectorAll("[data-reveal]"), function (el) {
      el.classList.add("is-in");
    });
    return;
  }

  /* Stagger siblings so a grid of cards arrives as a wave, not a block. */
  var groups = new Map();
  [].forEach.call(document.querySelectorAll("[data-reveal]"), function (el) {
    var p = el.parentNode;
    if (!groups.has(p)) groups.set(p, 0);
    var i = groups.get(p);
    groups.set(p, i + 1);
    if (i) el.style.transitionDelay = Math.min(i * 70, 350) + "ms";
  });

  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      if (!e.isIntersecting) return;
      e.target.classList.add("is-in");
      io.unobserve(e.target);
      if (e.target.classList.contains("panel")) countUp(e.target);
    });
  }, { rootMargin: "0px 0px -12% 0px", threshold: 0.08 });

  [].forEach.call(document.querySelectorAll("[data-reveal]"), function (el) {
    io.observe(el);
  });

  /* Count the stat figures up. Only touches values that are actually numeric —
     "2006" and "2" count, and anything else (or a value with no digits) is
     left exactly as authored. Suffixes like "+" are preserved. */
  function countUp(panel) {
    [].forEach.call(panel.querySelectorAll(".stat-n"), function (el) {
      var raw = el.textContent.trim();
      var m = raw.match(/^([\d,]+)(\D*)$/);
      if (!m) return;
      var target = parseInt(m[1].replace(/,/g, ""), 10);
      var suffix = m[2] || "";
      if (!isFinite(target) || target <= 0) return;
      var group = m[1].indexOf(",") !== -1;
      var dur = 1100, t0 = null;
      el.textContent = "0" + suffix;
      requestAnimationFrame(function step(ts) {
        if (t0 === null) t0 = ts;
        var p = Math.min((ts - t0) / dur, 1);
        var eased = 1 - Math.pow(1 - p, 3);
        var v = Math.round(target * eased);
        el.textContent = (group ? v.toLocaleString("en-US") : String(v)) + suffix;
        if (p < 1) requestAnimationFrame(step);
      });
    });
  }

  /* Header weight on scroll. */
  var header = document.querySelector(".site-header");
  if (header) {
    var ticking = false;
    var onScroll = function () {
      if (ticking) return;
      ticking = true;
      requestAnimationFrame(function () {
        header.classList.toggle("is-scrolled", window.scrollY > 12);
        ticking = false;
      });
    };
    window.addEventListener("scroll", onScroll, { passive: true });
    onScroll();
  }
})();
