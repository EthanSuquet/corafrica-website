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

   Reveals are REVERSIBLE: an element animates out as it leaves the viewport and
   back in when it returns, so scrolling up and down replays the motion without
   a reload. Direction matters — a block that left over the top comes back down
   from above, rather than always rising from below.

   Everything is additive: the `js-anim` class on <html> is what switches the CSS
   on, so if this file fails to load the page renders fully visible. All of it
   bails under prefers-reduced-motion. No dependencies — the Teeej sites use
   GSAP + ScrollTrigger, which is not worth ~100KB here. */
(function () {
  "use strict";

  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  document.documentElement.classList.add("js-anim");

  var nodes = [].slice.call(document.querySelectorAll("[data-reveal]"));

  if (reduce || !("IntersectionObserver" in window)) {
    nodes.forEach(function (el) { el.classList.add("is-in"); });
    return;
  }

  /* Stagger siblings so a grid arrives as a wave, not a slab. */
  var seen = new Map();
  nodes.forEach(function (el) {
    var p = el.parentNode;
    var i = seen.get(p) || 0;
    seen.set(p, i + 1);
    el.style.transitionDelay = i ? Math.min(i * 90, 420) + "ms" : "0ms";
  });

  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      var el = e.target;
      if (e.isIntersecting) {
        el.classList.add("is-in");
        if (el.classList.contains("panel")) countUp(el);
      } else {
        /* Reset, and remember which edge it left by so it returns from there. */
        el.style.setProperty("--rv", e.boundingClientRect.top < 0 ? "-1" : "1");
        el.classList.remove("is-in");
      }
    });
  }, { rootMargin: "-8% 0px -12% 0px", threshold: 0 });

  nodes.forEach(function (el) { io.observe(el); });

  /* Count the stat figures up. Only touches genuinely numeric values — anything
     without digits is left exactly as authored. Suffixes like "+" survive.
     Re-runs each time the panel re-enters, and cancels a run already in flight
     so scrubbing up and down cannot leave two loops fighting over one node. */
  function countUp(panel) {
    [].forEach.call(panel.querySelectorAll(".stat-n"), function (el) {
      if (!el.dataset.target) {
        var m = el.textContent.trim().match(/^([\d,]+)(\D*)$/);
        if (!m) { el.dataset.target = "skip"; return; }
        el.dataset.target = m[1].replace(/,/g, "");
        el.dataset.suffix = m[2] || "";
        el.dataset.group = m[1].indexOf(",") !== -1 ? "1" : "";
      }
      if (el.dataset.target === "skip") return;

      var target = parseInt(el.dataset.target, 10);
      if (!isFinite(target) || target <= 0) return;
      var suffix = el.dataset.suffix || "";
      var group = el.dataset.group === "1";

      if (el._raf) cancelAnimationFrame(el._raf);
      var dur = 1200, t0 = null;
      el.textContent = "0" + suffix;
      el._raf = requestAnimationFrame(function step(ts) {
        if (t0 === null) t0 = ts;
        var p = Math.min((ts - t0) / dur, 1);
        var v = Math.round(target * (1 - Math.pow(1 - p, 3)));
        el.textContent = (group ? v.toLocaleString("en-US") : String(v)) + suffix;
        if (p < 1) el._raf = requestAnimationFrame(step);
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
