/* Academy 21 University — interactions accessibles (amélioration progressive) */
(function () {
  "use strict";
  document.documentElement.classList.add("js");

  /* ---- Menu mobile ---- */
  var toggle = document.querySelector(".nav-toggle");
  var nav = document.getElementById("main-nav");
  if (toggle && nav) {
    var closeNav = function (focusToggle) {
      nav.classList.remove("is-open");
      toggle.setAttribute("aria-expanded", "false");
      if (focusToggle) toggle.focus();
    };
    toggle.addEventListener("click", function () {
      var open = toggle.getAttribute("aria-expanded") === "true";
      if (open) { closeNav(false); return; }
      nav.classList.add("is-open");
      toggle.setAttribute("aria-expanded", "true");
      var first = nav.querySelector("a");
      if (first) first.focus();
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && nav.classList.contains("is-open")) closeNav(true);
    });
    document.addEventListener("click", function (e) {
      if (nav.classList.contains("is-open") && !nav.contains(e.target) && !toggle.contains(e.target)) closeNav(false);
    });
    window.matchMedia("(min-width: 1061px)").addEventListener("change", function (mq) { if (mq.matches) closeNav(false); });
  }

  /* ---- Sous-navigation des fiches (section active) ---- */
  var subLinks = document.querySelectorAll(".subnav a[href^='#']");
  if (subLinks.length && "IntersectionObserver" in window) {
    var map = {};
    subLinks.forEach(function (a) { map[a.getAttribute("href").slice(1)] = a; });
    var spy = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (!en.isIntersecting) return;
        subLinks.forEach(function (a) { a.removeAttribute("aria-current"); });
        var link = map[en.target.id];
        if (link) {
          link.setAttribute("aria-current", "true");
          link.scrollIntoView({ block: "nearest", inline: "nearest" });
        }
      });
    }, { rootMargin: "-45% 0px -50% 0px" });
    Object.keys(map).forEach(function (id) { var s = document.getElementById(id); if (s) spy.observe(s); });
  }

  /* ---- Onglets (motif ARIA tabs, activation automatique) ---- */
  document.querySelectorAll("[data-tabs]").forEach(function (root) {
    var tabs = Array.prototype.slice.call(root.querySelectorAll("[role='tab']"));
    function select(tab, focus) {
      tabs.forEach(function (t) {
        var on = t === tab;
        t.setAttribute("aria-selected", String(on));
        t.tabIndex = on ? 0 : -1;
        document.getElementById(t.getAttribute("aria-controls")).hidden = !on;
      });
      if (focus) tab.focus();
    }
    tabs.forEach(function (tab, i) {
      tab.addEventListener("click", function () { select(tab, false); });
      tab.addEventListener("keydown", function (e) {
        var idx = null;
        if (e.key === "ArrowRight") idx = (i + 1) % tabs.length;
        if (e.key === "ArrowLeft") idx = (i - 1 + tabs.length) % tabs.length;
        if (e.key === "Home") idx = 0;
        if (e.key === "End") idx = tabs.length - 1;
        if (idx !== null) { e.preventDefault(); select(tabs[idx], true); }
      });
    });
  });

  /* ---- Filtres du catalogue ---- */
  var filterForm = document.querySelector("[data-filters]");
  if (filterForm) {
    var cards = document.querySelectorAll("[data-program]");
    var count = document.getElementById("results-count");
    var apply = function () {
      var level = (filterForm.querySelector("input[name='niveau']:checked") || {}).value || "all";
      var mode = (filterForm.querySelector("input[name='modalite']:checked") || {}).value || "all";
      var shown = 0;
      cards.forEach(function (c) {
        var okL = level === "all" || c.dataset.level === level;
        var okM = mode === "all" || (c.dataset.modes || "").split(" ").indexOf(mode) > -1;
        var ok = okL && okM;
        c.hidden = !ok;
        if (ok) shown++;
      });
      if (count) count.textContent = shown + (shown > 1 ? " formations correspondent" : " formation correspond") + " à votre sélection.";
    };
    filterForm.addEventListener("change", apply);
    apply();
  }

  /* ---- Formulaire de contact : validation accessible ---- */
  var form = document.querySelector("[data-validate]");
  if (form) {
    form.setAttribute("novalidate", "");
    var summary = form.querySelector(".error-summary");
    var status = form.querySelector(".form-status");
    var messages = {
      valueMissing: "Ce champ est obligatoire.",
      typeMismatch: "Le format saisi n'est pas valide (exemple : nom@domaine.fr).",
      patternMismatch: "Le format saisi n'est pas valide."
    };
    var errorFor = function (el) {
      if (el.validity.valid) return "";
      if (el.type === "checkbox" && el.validity.valueMissing) return "Vous devez accepter pour envoyer votre demande.";
      if (el.validity.valueMissing) return el.dataset.required || messages.valueMissing;
      if (el.validity.typeMismatch) return el.dataset.format || messages.typeMismatch;
      if (el.validity.patternMismatch) return el.dataset.format || messages.patternMismatch;
      return "Valeur invalide.";
    };
    var show = function (el) {
      var msg = errorFor(el);
      var box = document.getElementById(el.id + "-error");
      el.setAttribute("aria-invalid", msg ? "true" : "false");
      if (box) box.textContent = msg;
      return msg;
    };
    form.querySelectorAll("input, select, textarea").forEach(function (el) {
      el.addEventListener("blur", function () { if (el.getAttribute("aria-invalid") === "true" || el.value) show(el); });
      el.addEventListener("input", function () { if (el.getAttribute("aria-invalid") === "true") show(el); });
    });
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var errors = [];
      form.querySelectorAll("input, select, textarea").forEach(function (el) {
        if (!el.willValidate) return;
        var msg = show(el);
        if (msg) {
          var lab = form.querySelector("label[for='" + el.id + "']");
          errors.push({ id: el.id, label: el.dataset.label || (lab ? lab.textContent.replace("*", "").trim() : el.name), msg: msg });
        }
      });
      status.textContent = "";
      status.className = "form-status";
      if (errors.length) {
        var ul = summary.querySelector("ul");
        ul.innerHTML = "";
        errors.forEach(function (er) {
          var li = document.createElement("li");
          var a = document.createElement("a");
          a.href = "#" + er.id;
          a.textContent = er.label + " : " + er.msg;
          a.addEventListener("click", function (ev) { ev.preventDefault(); document.getElementById(er.id).focus(); });
          li.appendChild(a);
          ul.appendChild(li);
        });
        summary.querySelector("h2").textContent = errors.length + (errors.length > 1 ? " erreurs empêchent" : " erreur empêche") + " l'envoi du formulaire";
        summary.hidden = false;
        summary.focus();
        return;
      }
      summary.hidden = true;
      status.classList.add("is-success");
      status.textContent = "Merci ! Votre demande a bien été enregistrée. Un conseiller d'admission vous recontactera sous 48 h ouvrées.";
      form.reset();
      form.querySelectorAll("[aria-invalid]").forEach(function (el) { el.removeAttribute("aria-invalid"); });
    });
  }

  /* ---- Pré-sélection du programme via ?programme= ---- */
  var sel = document.getElementById("programme");
  if (sel) {
    var p = new URLSearchParams(window.location.search).get("programme");
    if (p && sel.querySelector("option[value='" + p.replace(/[^a-z-]/g, "") + "']")) sel.value = p;
  }

  /* ---- Apparition douce (désactivée si mouvement réduit) ---- */
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var reveals = document.querySelectorAll(".reveal");
  if (!reduce && "IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add("is-visible"); io.unobserve(en.target); } });
    }, { rootMargin: "0px 0px -8% 0px" });
    reveals.forEach(function (el) { io.observe(el); });
  } else {
    reveals.forEach(function (el) { el.classList.add("is-visible"); });
  }

  var y = document.getElementById("year");
  if (y) y.textContent = new Date().getFullYear();
})();
