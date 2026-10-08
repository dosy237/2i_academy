/* Academy 21 University — interactions (amélioration progressive, accessibles au clavier) */
(function () {
  "use strict";

  var d = document;
  var root = d.documentElement;
  var params = new URLSearchParams(window.location.search);
  var CONTACT = (d.querySelector('meta[name="a21-contact"]') || {}).content || "";
  var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var desktop = window.matchMedia("(min-width: 1281px)");

  function $(sel, ctx) { return (ctx || d).querySelector(sel); }
  function $$(sel, ctx) { return Array.prototype.slice.call((ctx || d).querySelectorAll(sel)); }

  /* ------------------------------------------------------------------
     En-tête : ombre au défilement, retour en haut
  ------------------------------------------------------------------ */
  var header = $(".site-header");
  var toTop = $(".to-top");
  function onScroll() {
    var y = window.scrollY;
    if (header) header.classList.toggle("is-scrolled", y > 8);
    if (toTop) toTop.classList.toggle("is-visible", y > 700);
  }
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();
  if (toTop) {
    toTop.addEventListener("click", function () {
      window.scrollTo({ top: 0, behavior: reduceMotion ? "auto" : "smooth" });
      var main = d.getElementById("contenu");
      if (main) main.focus({ preventScroll: true });
    });
  }

  /* ------------------------------------------------------------------
     Menu principal (mobile) et menu déroulant « Formations »
  ------------------------------------------------------------------ */
  var toggle = $(".nav-toggle");
  var nav = d.getElementById("main-nav");
  function closeNav(focusToggle) {
    if (!nav) return;
    nav.classList.remove("is-open");
    toggle.setAttribute("aria-expanded", "false");
    if (focusToggle) toggle.focus();
  }
  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      if (toggle.getAttribute("aria-expanded") === "true") { closeNav(false); return; }
      nav.classList.add("is-open");
      toggle.setAttribute("aria-expanded", "true");
      var first = nav.querySelector("a, button");
      if (first) first.focus();
    });
    d.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && nav.classList.contains("is-open")) closeNav(true);
    });
    d.addEventListener("click", function (e) {
      if (nav.classList.contains("is-open") && !nav.contains(e.target) && !toggle.contains(e.target)) closeNav(false);
    });
    desktop.addEventListener("change", function (mq) { if (mq.matches) closeNav(false); });
  }

  $$("[data-dropdown]").forEach(function (btn) {
    var item = btn.parentNode;
    var menu = d.getElementById(btn.getAttribute("aria-controls"));
    if (!menu) return;
    function set(open) {
      btn.setAttribute("aria-expanded", String(open));
      menu.hidden = !open;
    }
    btn.addEventListener("click", function () { set(btn.getAttribute("aria-expanded") !== "true"); });
    item.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && btn.getAttribute("aria-expanded") === "true") {
        e.stopPropagation();
        set(false);
        btn.focus();
      }
    });
    item.addEventListener("focusout", function (e) {
      if (desktop.matches && !item.contains(e.relatedTarget)) set(false);
    });
    d.addEventListener("click", function (e) { if (!item.contains(e.target)) set(false); });
  });

  /* ------------------------------------------------------------------
     Sous-navigation des fiches : section active
  ------------------------------------------------------------------ */
  var subLinks = $$(".subnav a[href^='#']");
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
          var list = link.closest("ul");
          if (list) list.scrollTo({ left: link.offsetLeft - 24, behavior: reduceMotion ? "auto" : "smooth" });
        }
      });
    }, { rootMargin: "-40% 0px -55% 0px" });
    Object.keys(map).forEach(function (id) { var s = d.getElementById(id); if (s) spy.observe(s); });
  }

  /* ------------------------------------------------------------------
     Onglets (motif ARIA tabs)
  ------------------------------------------------------------------ */
  $$("[data-tabs]").forEach(function (tabsRoot) {
    var tabs = $$("[role='tab']", tabsRoot);
    function select(tab, focus) {
      tabs.forEach(function (t) {
        var on = t === tab;
        t.setAttribute("aria-selected", String(on));
        t.tabIndex = on ? 0 : -1;
        d.getElementById(t.getAttribute("aria-controls")).hidden = !on;
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

  /* ------------------------------------------------------------------
     Filtres du catalogue (?niveau=bac5&modalite=distanciel)
  ------------------------------------------------------------------ */
  var filterForm = $("[data-filters]");
  if (filterForm) {
    ["niveau", "modalite"].forEach(function (n) {
      var v = params.get(n);
      var input = v && filterForm.querySelector("input[name='" + n + "'][value='" + v.replace(/[^a-z0-9]/g, "") + "']");
      if (input) input.checked = true;
    });
    var cards = $$("[data-program]");
    var count = d.getElementById("results-count");
    var apply = function () {
      var level = (filterForm.querySelector("input[name='niveau']:checked") || {}).value || "all";
      var mode = (filterForm.querySelector("input[name='modalite']:checked") || {}).value || "all";
      var shown = 0;
      cards.forEach(function (c) {
        var ok = (level === "all" || c.dataset.level === level) &&
                 (mode === "all" || (c.dataset.modes || "").split(" ").indexOf(mode) > -1);
        c.hidden = !ok;
        if (ok) shown++;
      });
      if (count) {
        count.textContent = shown === 0
          ? "Aucune formation ne correspond à cette sélection. Modifiez vos filtres."
          : shown + (shown > 1 ? " formations correspondent" : " formation correspond") + " à votre sélection.";
      }
    };
    filterForm.addEventListener("change", apply);
    filterForm.addEventListener("submit", function (e) { e.preventDefault(); });
    apply();
  }

  /* ------------------------------------------------------------------
     Formulaires : utilitaires
  ------------------------------------------------------------------ */
  var EMAIL_RE = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/;
  var CV_MAX = 3 * 1024 * 1024;
  var CV_EXT = /\.(pdf|docx?)$/i;

  function labelOf(form, el) {
    if (el.type === "radio") {
      var fs = el.closest("fieldset");
      var lg = fs && fs.querySelector("legend");
      return lg ? lg.textContent.replace("*", "").trim() : el.name;
    }
    if (el.dataset.label) return el.dataset.label;
    var lab = form.querySelector("label[for='" + el.id + "']");
    if (!lab) return el.name;
    var text = lab.textContent.replace("*", "").trim();
    return text.length > 60 ? text.slice(0, 57) + "…" : text;
  }

  function errorBox(el) {
    return d.getElementById((el.type === "radio" ? el.name : el.id) + "-error");
  }

  function splitEmails(v) {
    var seen = {};
    return String(v || "").split(/[\s,;]+/).map(function (x) { return x.trim().toLowerCase(); })
      .filter(function (x) { if (!x || seen[x]) return false; seen[x] = true; return true; });
  }

  function messageFor(form, el) {
    if (el.disabled || el.closest("[hidden]")) return "";
    if (el.type === "radio") {
      var group = $$("input[name='" + el.name + "']", form);
      var required = group.some(function (r) { return r.required; });
      var checked = group.some(function (r) { return r.checked; });
      return required && !checked ? "Veuillez faire un choix." : "";
    }
    if (el.type === "checkbox") return el.required && !el.checked ? "Cette case doit être cochée pour continuer." : "";
    if (el.type === "file") {
      var f = el.files && el.files[0];
      if (!f) return "";
      if (!CV_EXT.test(f.name)) return "Format non accepté : choisissez un fichier PDF ou Word.";
      if (f.size > CV_MAX) return "Le fichier dépasse 3 Mo. Réduisez sa taille ou transmettez-le plus tard.";
      return "";
    }
    var v = (el.value || "").trim();
    if (el.required && !v) return el.dataset.required || "Ce champ est obligatoire.";
    if (el.hasAttribute("data-emails") && v) {
      var bad = splitEmails(v).filter(function (x) { return !EMAIL_RE.test(x); });
      if (bad.length) return "Adresse" + (bad.length > 1 ? "s" : "") + " non valide" + (bad.length > 1 ? "s" : "") + " : " + bad.slice(0, 3).join(", ") + ".";
      if (splitEmails(v).length > 50) return "50 adresses maximum par envoi.";
      return "";
    }
    if (!v) return "";
    if (el.type === "email" && !EMAIL_RE.test(v)) return el.dataset.format || "Le format n'est pas valide.";
    if (el.pattern && !new RegExp("^(?:" + el.pattern + ")$").test(v)) return el.dataset.format || "Le format n'est pas valide.";
    if (el.minLength > 0 && v.length < el.minLength) return el.dataset.format || ("Au moins " + el.minLength + " caractères.");
    return "";
  }

  function showError(form, el, msg) {
    var targets = el.type === "radio" ? $$("input[name='" + el.name + "']", form) : [el];
    targets.forEach(function (t) { t.setAttribute("aria-invalid", msg ? "true" : "false"); });
    var box = errorBox(el);
    if (box) box.textContent = msg;
  }

  function controls(scope) {
    var seen = {};
    return $$("input, select, textarea", scope).filter(function (el) {
      if (el.type === "hidden" || el.closest(".hp")) return false;
      if (el.type === "radio") {
        if (seen[el.name]) return false;
        seen[el.name] = true;
      }
      return true;
    });
  }

  function validate(form, scope) {
    var errors = [];
    controls(scope).forEach(function (el) {
      var msg = messageFor(form, el);
      showError(form, el, msg);
      if (msg) errors.push({ el: el, label: labelOf(form, el), msg: msg });
    });
    var summary = $("[data-error-summary]", form);
    if (!summary) return errors.length === 0;
    if (!errors.length) { summary.hidden = true; return true; }
    var ul = summary.querySelector("ul");
    ul.innerHTML = "";
    errors.forEach(function (er) {
      var li = d.createElement("li");
      var a = d.createElement("a");
      a.href = "#" + (er.el.id || "");
      a.textContent = er.label + " : " + er.msg;
      a.addEventListener("click", function (ev) { ev.preventDefault(); er.el.focus(); });
      li.appendChild(a);
      ul.appendChild(li);
    });
    summary.querySelector("h3").textContent = errors.length + (errors.length > 1 ? " points à corriger" : " point à corriger");
    summary.hidden = false;
    summary.focus();
    return false;
  }

  function wireLiveValidation(form) {
    controls(form).forEach(function (el) {
      var evt = (el.type === "radio" || el.type === "checkbox" || el.tagName === "SELECT" || el.type === "file") ? "change" : "blur";
      el.addEventListener(evt, function () {
        if (evt === "blur" && !el.value && el.getAttribute("aria-invalid") !== "true") return;
        showError(form, el, messageFor(form, el));
      });
      el.addEventListener("input", function () {
        if (el.getAttribute("aria-invalid") === "true") showError(form, el, messageFor(form, el));
      });
    });
  }

  /* Affichage conditionnel : data-show-if="champ=valeur" */
  function wireConditionals(form) {
    var blocks = $$("[data-show-if]", form);
    if (!blocks.length) return function () {};
    function update() {
      blocks.forEach(function (b) {
        var parts = b.dataset.showIf.split("=");
        var el = form.elements[parts[0]];
        var val = el ? (el.value !== undefined ? el.value : "") : "";
        if (el && el.length && el[0] && el[0].type === "radio") {
          var c = $$("input[name='" + parts[0] + "']:checked", form)[0];
          val = c ? c.value : "";
        }
        var show = val === parts[1];
        b.hidden = !show;
        $$("input, select, textarea", b).forEach(function (i) { i.disabled = !show; });
      });
    }
    form.addEventListener("change", update);
    update();
    return update;
  }

  /* Compteurs de caractères */
  $$("[data-counter-for]").forEach(function (counter) {
    var el = d.getElementById(counter.dataset.counterFor);
    if (!el) return;
    var max = el.maxLength > 0 ? el.maxLength : 3000;
    var fmt = function (n) { return n.toLocaleString("fr-FR"); };
    var upd = function () { counter.textContent = fmt(el.value.length) + " / " + fmt(max) + " caractères"; };
    el.addEventListener("input", upd);
    upd();
  });

  /* Valeur lisible d'un champ (pour le récapitulatif) */
  function displayValue(form, el) {
    if (el.type === "radio") {
      var c = $$("input[name='" + el.name + "']:checked", form)[0];
      var t = c && form.querySelector("label[for='" + c.id + "'] .choice__title");
      return t ? t.textContent.trim() : "";
    }
    if (el.tagName === "SELECT") return el.value ? el.options[el.selectedIndex].text : "";
    if (el.type === "file") return el.files && el.files[0] ? el.files[0].name : "";
    if (el.type === "checkbox") return el.checked ? "Oui" : "Non";
    return (el.value || "").trim();
  }

  function collect(form) {
    var data = {};
    $$("input, select, textarea", form).forEach(function (el) {
      if (!el.name || el.disabled || el.type === "file" || el.closest(".hp")) return;
      if ((el.type === "radio" || el.type === "checkbox") && !el.checked) return;
      data[el.name] = el.value;
    });
    return data;
  }

  function recapText(form) {
    var lines = [];
    controls(form).forEach(function (el) {
      if (el.disabled || el.closest("[hidden]") || el.type === "checkbox") return;
      var v = displayValue(form, el);
      if (v) lines.push(labelOf(form, el) + " : " + v);
    });
    return lines.join("\n");
  }

  function readFile(file) {
    return new Promise(function (resolve, reject) {
      var r = new FileReader();
      r.onload = function () { resolve(String(r.result).split(",")[1] || ""); };
      r.onerror = reject;
      r.readAsDataURL(file);
    });
  }

  function setStatus(form, kind, html) {
    var s = $("[data-status]", form);
    if (!s) return;
    s.className = "form-status" + (kind ? " is-" + kind : "");
    s.innerHTML = html || "";
  }

  function fallback(form, type) {
    var subject = type === "candidature" ? "Candidature — " + (displayValue(form, form.elements.programme[0] || form.elements.programme) || "Academy 21 University") : "Demande de contact — Academy 21 University";
    var text = recapText(form);
    var mailBody = text.length > 1700 ? text.slice(0, 1700) + "\n[…] (récapitulatif complet joint)" : text;
    var mailto = "mailto:" + CONTACT + "?subject=" + encodeURIComponent(subject) + "&body=" + encodeURIComponent(mailBody + "\n");
    var blob = new Blob([subject + "\n\n" + text + "\n"], { type: "text/plain;charset=utf-8" });
    var url = URL.createObjectURL(blob);
    setStatus(form, "info",
      "<strong>L'envoi en ligne est momentanément indisponible.</strong> Vos informations sont conservées sur cet appareil. " +
      "Transmettez votre demande par e-mail en un clic" + (type === "candidature" ? " (pensez à joindre votre CV et le récapitulatif)" : "") + " :" +
      '<div class="btn-row"><a class="btn btn--primary btn--sm" href="' + mailto + '">Envoyer par e-mail</a>' +
      '<a class="btn btn--ghost btn--sm" href="' + url + '" download="recapitulatif-academy21.txt">Télécharger le récapitulatif</a></div>');
  }

  function busy(btn, on) {
    if (!btn) return;
    if (on) {
      btn.dataset.label = btn.innerHTML;
      btn.innerHTML = '<span class="spinner" aria-hidden="true"></span> Envoi en cours…';
      btn.setAttribute("aria-disabled", "true");
      btn.disabled = true;
    } else if (btn.dataset.label) {
      btn.innerHTML = btn.dataset.label;
      btn.removeAttribute("aria-disabled");
      btn.disabled = false;
    }
  }

  var loadedAt = Date.now();

  function send(form, extra, onSuccess) {
    var type = (form.elements.type || {}).value || "contact";
    var payload = collect(form);
    payload.elapsed = Date.now() - loadedAt;
    Object.keys(extra || {}).forEach(function (k) { payload[k] = extra[k]; });
    var btn = $("[data-submit]", form);
    busy(btn, true);
    setStatus(form, "", "");
    return fetch(form.getAttribute("action") || "/api/submit", {
      method: "POST",
      headers: { "Content-Type": "application/json", "Accept": "application/json" },
      body: JSON.stringify(payload)
    }).then(function (res) {
      return res.json().catch(function () { return {}; }).then(function (json) { return { res: res, json: json }; });
    }).then(function (r) {
      busy(btn, false);
      if (r.res.ok && r.json.ok) {
        if (onSuccess) onSuccess();
        window.location.href = "merci.html?type=" + encodeURIComponent(type) + (r.json.ref ? "&ref=" + encodeURIComponent(r.json.ref) : "");
        return;
      }
      if (r.res.status === 400 && r.json.error === "validation") {
        setStatus(form, "error", "Certaines informations sont incomplètes : " + (r.json.fields || []).join(", ") + ". Vérifiez le formulaire puis réessayez.");
        return;
      }
      if (r.res.status === 413) {
        setStatus(form, "error", "Votre CV est trop volumineux pour être envoyé. Retirez-le ou choisissez un fichier de moins de 3 Mo.");
        return;
      }
      fallback(form, type);
    }).catch(function () {
      busy(btn, false);
      fallback(form, type);
    });
  }

  /* ------------------------------------------------------------------
     Formulaire de contact
  ------------------------------------------------------------------ */
  var contactForm = $("#contact-form");
  if (contactForm) {
    ["objet", "programme"].forEach(function (n) {
      var v = params.get(n);
      var el = contactForm.elements[n];
      if (v && el && el.querySelector("option[value='" + v.replace(/[^a-z0-9-]/g, "") + "']")) el.value = v;
    });
    wireConditionals(contactForm);
    wireLiveValidation(contactForm);
    contactForm.addEventListener("submit", function (e) {
      e.preventDefault();
      if (!validate(contactForm, contactForm)) return;
      send(contactForm);
    });
  }

  /* ------------------------------------------------------------------
     Assistant de candidature
  ------------------------------------------------------------------ */
  var wizard = $("[data-wizard]");
  if (wizard) {
    var DRAFT_KEY = "a21-candidature-brouillon";
    var steps = $$("[data-step]", wizard);
    var indicators = $$("[data-step-indicator]", wizard);
    var progress = $("[data-progress]", wizard);
    var current = 0;
    var updateConditionals = wireConditionals(wizard);
    wireLiveValidation(wizard);

    /* Brouillon local */
    var storage = null;
    try { storage = window.localStorage; storage.setItem("a21-test", "1"); storage.removeItem("a21-test"); } catch (e) { storage = null; }
    var saveTimer = null;
    var submitted = false;
    function writeDraft() {
      if (!storage || submitted) return;
      clearTimeout(saveTimer);
      saveTimer = null;
      var data = collect(wizard);
      delete data.exactitude; delete data.consentement; delete data.ts; delete data.type;
      try {
        storage.setItem(DRAFT_KEY, JSON.stringify({ step: current, data: data, savedAt: Date.now() }));
        $$("[data-draft-note]", wizard).forEach(function (n) { n.hidden = false; });
      } catch (e) { /* quota : on ignore */ }
    }
    function saveDraft() {
      if (!storage) return;
      clearTimeout(saveTimer);
      saveTimer = setTimeout(writeDraft, 400);
    }
    /* Enregistre immédiatement si l'on quitte la page avant la fin du délai */
    window.addEventListener("pagehide", function () { if (saveTimer) writeDraft(); });
    d.addEventListener("visibilitychange", function () { if (d.visibilityState === "hidden" && saveTimer) writeDraft(); });
    function restoreDraft() {
      if (!storage) return 0;
      var raw = null;
      try { raw = JSON.parse(storage.getItem(DRAFT_KEY) || "null"); } catch (e) { raw = null; }
      if (!raw || !raw.data) return 0;
      Object.keys(raw.data).forEach(function (name) {
        var el = wizard.elements[name];
        if (!el) return;
        if (el.length && el[0] && el[0].type === "radio") {
          $$("input[name='" + name + "']", wizard).forEach(function (r) { r.checked = r.value === raw.data[name]; });
        } else if (el.type !== "file") {
          el.value = raw.data[name];
        }
      });
      $$("[data-draft-note]", wizard).forEach(function (n) { n.hidden = false; });
      return Math.min(raw.step || 0, steps.length - 2);
    }

    /* Éligibilité indicative */
    var RANK = { aucun: 0, bac: 1, bac2: 2, bac3: 3, bac4: 4, bac5: 5, autre: -1 };
    var EXP = { "0-2": 1, "3-4": 3, "5-6": 5, "7-9": 7, "10+": 10 };
    function radioVal(name) { var c = $$("input[name='" + name + "']:checked", wizard)[0]; return c ? c.value : ""; }
    function eligibility() {
      var box = $("[data-eligibility]", wizard);
      if (!box) return;
      var prog = radioVal("programme");
      var dip = wizard.elements.diplome.value;
      var exp = EXP[wizard.elements.experience.value];
      var mgmt = wizard.elements.experience_management.value;
      var rank = RANK[dip];
      var msg = "", kind = "info";
      if (!prog || !dip || exp === undefined) { box.innerHTML = ""; return; }
      if (prog === "bachelor") {
        if (rank >= 2) { msg = "Votre profil correspond à l'<strong>accès sur diplôme</strong> du Bachelor (niveau 5 / Bac+2)."; kind = "success"; }
        else if (exp >= 5) { msg = "Votre profil correspond à l'<strong>accès sur expérience professionnelle</strong> du Bachelor (au moins 5 ans d'expérience significative)."; kind = "success"; }
        else { msg = "L'accès au Bachelor requiert en principe un Bac+2 ou 5 années d'expérience significative. Votre dossier sera étudié individuellement."; }
      } else if (prog === "mastere") {
        if (radioVal("entree") === "m2") { msg = "L'entrée directe en M2 fait l'objet d'une <strong>étude individualisée</strong> de vos acquis par la commission d'admission."; }
        else if (rank >= 3) { msg = "Votre profil correspond à l'<strong>entrée en M1</strong> du Mastère (niveau 6 / Bac+3 ou équivalent)."; kind = "success"; }
        else if (rank === 2 && mgmt === "3plus") { msg = "Votre profil correspond à l'<strong>admission dérogatoire</strong> du Mastère (Bac+2 et au moins 3 ans en fonctions managériales)."; kind = "success"; }
        else { msg = "L'entrée en M1 requiert un Bac+3, ou un Bac+2 avec au moins 3 ans d'expérience managériale. Votre dossier sera étudié individuellement."; }
      } else if (prog === "executive-mba") {
        if (exp >= 7) { msg = "Votre expérience correspond au profil attendu pour l'<strong>Executive MBA</strong> (au moins 7 ans, dont des responsabilités managériales significatives)."; kind = "success"; }
        else { msg = "L'Executive MBA s'adresse en priorité aux professionnels justifiant d'au moins 7 années d'expérience. Votre dossier sera étudié individuellement."; }
      } else {
        msg = "La formation IA ne requiert aucun prérequis technique : une activité, un projet ou une expérience en marketing de réseau suffit."; kind = "success";
      }
      box.innerHTML = '<div class="notice notice--' + kind + '" role="note"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 11v6M12 7.5h.01"/></svg><div><p><strong>Voie d\'accès indicative.</strong> ' + msg + "</p></div></div>";
    }

    /* Récapitulatif */
    function buildRecap() {
      var box = $("[data-recap]", wizard);
      box.innerHTML = "";
      steps.slice(0, -1).forEach(function (step, i) {
        var sec = d.createElement("section");
        var h = d.createElement("h3");
        h.textContent = step.querySelector("h2").textContent;
        var edit = d.createElement("button");
        edit.type = "button";
        edit.textContent = "Modifier";
        edit.setAttribute("aria-label", "Modifier : " + h.textContent);
        edit.addEventListener("click", function () { goTo(i); });
        h.appendChild(edit);
        var dl = d.createElement("dl");
        controls(step).forEach(function (el) {
          if (el.disabled || el.closest("[hidden]")) return;
          var v = displayValue(wizard, el);
          if (!v) return;
          var dt = d.createElement("dt"); dt.textContent = labelOf(wizard, el);
          var dd = d.createElement("dd"); dd.textContent = el.id === "motivation" && v.length > 220 ? v.slice(0, 220) + "…" : v;
          dl.appendChild(dt); dl.appendChild(dd);
        });
        sec.appendChild(h); sec.appendChild(dl);
        box.appendChild(sec);
      });
    }

    function goTo(i, noFocus) {
      current = i;
      steps.forEach(function (s, k) { s.classList.toggle("is-active", k === i); });
      indicators.forEach(function (li, k) {
        if (k === i) li.setAttribute("aria-current", "step"); else li.removeAttribute("aria-current");
        li.classList.toggle("is-done", k < i);
      });
      if (progress) progress.style.width = ((i + 1) / steps.length * 100) + "%";
      if (i === steps.length - 1) buildRecap();
      var summary = $("[data-error-summary]", wizard);
      if (summary) summary.hidden = true;
      if (!noFocus) {
        var h = steps[i].querySelector("h2");
        var top = wizard.getBoundingClientRect().top + window.scrollY - 110;
        if (window.scrollY > top) window.scrollTo({ top: top, behavior: reduceMotion ? "auto" : "smooth" });
        h.focus({ preventScroll: true });
      }
    }

    $$("[data-next]", wizard).forEach(function (b) {
      b.addEventListener("click", function () {
        if (!validate(wizard, steps[current])) return;
        goTo(current + 1);
        saveDraft();
      });
    });
    $$("[data-prev]", wizard).forEach(function (b) {
      b.addEventListener("click", function () { goTo(current - 1); });
    });

    wizard.addEventListener("input", saveDraft);
    wizard.addEventListener("change", function () { saveDraft(); eligibility(); updateConditionals(); });

    wizard.addEventListener("submit", function (e) {
      e.preventDefault();
      if (current < steps.length - 1) {
        if (validate(wizard, steps[current])) { goTo(current + 1); saveDraft(); }
        return;
      }
      for (var k = 0; k < steps.length; k++) {
        if (!validate(wizard, steps[k])) { if (k !== current) { goTo(k); validate(wizard, steps[k]); } return; }
      }
      var file = wizard.elements.cv && wizard.elements.cv.files && wizard.elements.cv.files[0];
      var extra = {};
      var go = function () {
        send(wizard, extra, function () {
          submitted = true;
          clearTimeout(saveTimer);
          try { if (storage) storage.removeItem(DRAFT_KEY); } catch (er) { /* ignore */ }
        });
      };
      if (file) {
        readFile(file).then(function (b64) {
          extra.cv = { name: file.name, type: file.type || "application/octet-stream", data: b64 };
          go();
        }).catch(go);
      } else {
        go();
      }
    });

    /* Initialisation */
    var startStep = restoreDraft();
    var pre = params.get("programme");
    if (pre) {
      var r = wizard.querySelector("input[name='programme'][value='" + pre.replace(/[^a-z-]/g, "") + "']");
      if (r) r.checked = true;
    }
    updateConditionals();
    eligibility();
    goTo(startStep, true);
  }

  /* ------------------------------------------------------------------
     Page de confirmation
  ------------------------------------------------------------------ */
  var refEl = $("[data-ref]");
  if (refEl) {
    var ref = (params.get("ref") || "").replace(/[^A-Z0-9-]/gi, "").slice(0, 32);
    if (ref) { refEl.textContent = ref; $("[data-ref-box]").hidden = false; }
    if (params.get("type") === "contact") {
      $("[data-merci-title]").textContent = "Merci, votre message a bien été envoyé";
      $("[data-merci-lead]").textContent = "Notre équipe vous répond par e-mail dans les meilleurs délais.";
      d.title = "Message envoyé — Academy 21 University";
    } else {
      $("[data-merci-title]").textContent = "Merci, votre candidature a bien été envoyée";
      d.title = "Candidature envoyée — Academy 21 University";
    }
  }

  (function () {
  /* ------------------------------------------------------------------
     Paiement des frais d'étude de dossier
  ------------------------------------------------------------------ */
  function api(url, opts) {
    return fetch(url, opts).then(function (r) {
      return r.json().catch(function () { return {}; }).then(function (j) { j._status = r.status; return j; });
    });
  }
  function fill(scope, attr, map) {
    Object.keys(map).forEach(function (k) {
      $$("[" + attr + "='" + k + "']", scope).forEach(function (el) { el.textContent = map[k] || "—"; });
    });
  }
  function frDate(iso) {
    try { return new Date(iso).toLocaleDateString("fr-FR", { day: "numeric", month: "long", year: "numeric" }); } catch (e) { return ""; }
  }

  var payBox = $("[data-pay]");
  if (payBox) {
    var token = params.get("t") || "";
    var show = function (name) {
      $$("[data-pay-state]", payBox).forEach(function (el) { el.hidden = el.getAttribute("data-pay-state") !== name; });
    };
    var payError = function (title, text) {
      show("error");
      if (title) $("[data-pay-error-title]", payBox).textContent = title;
      if (text) $("[data-pay-error-text]", payBox).textContent = text;
      $("[data-pay-error-title]", payBox).focus();
    };
    var payStatus = $("[data-pay-status]", payBox);
    var setPayStatus = function (kind, html) {
      payStatus.className = "form-status" + (kind ? " is-" + kind : "");
      payStatus.innerHTML = html || "";
    };

    if (!token) {
      payError("Lien de paiement incomplet", "Ouvrez cette page depuis le lien personnel reçu par e-mail après l'étude de votre dossier.");
    } else {
      api("/api/payment?action=session&t=" + encodeURIComponent(token)).then(function (s) {
        if (!s.ok) {
          if (s.error === "expired") return payError("Ce lien de paiement a expiré", "Pour votre sécurité, les liens de paiement ont une durée limitée. Écrivez-nous : nous vous en adressons un nouveau.");
          if (s.error === "not_configured" || s._status >= 500) return payError("Paiement momentanément indisponible", "Le paiement en ligne n'est pas encore ouvert. Écrivez-nous pour régler vos frais d'étude de dossier.");
          return payError();
        }
        fill(payBox, "data-f", {
          ref: s.ref, name: ((s.prenom || "") + " " + (s.nom || "")).trim() || s.email, programme: s.programme,
          eur: s.labelEur, fcfa: s.labelFcfa, expires: frDate(s.expires)
        });
        // Zones Mobile Money (XAF / XOF)
        var zones = s.zones || [];
        if (zones.length > 1) {
          var list = $("[data-zones-list]", payBox);
          list.innerHTML = "";
          zones.forEach(function (z, i) {
            var lab = d.createElement("label");
            var inp = d.createElement("input");
            inp.type = "radio"; inp.name = "zone"; inp.value = z.code; inp.checked = i === 0;
            lab.appendChild(inp);
            lab.appendChild(d.createTextNode(" " + z.label));
            list.appendChild(lab);
          });
          $("[data-zones]", payBox).hidden = false;
        }
        ["card", "mobile"].forEach(function (m) {
          var on = s.methods && s.methods[m];
          var art = $(".pay-method[data-method='" + m + "']", payBox);
          art.classList.toggle("is-off", !on);
          $("[data-off]", art).hidden = !!on;
          $("[data-pay-go]", art).hidden = !on;
          if (!on && m === "mobile") $("[data-zones]", art).hidden = true;
        });
        if (params.get("annule")) $("[data-pay-cancel]", payBox).hidden = false;
        show("ready");
      }).catch(function () {
        payError("Connexion impossible", "Vérifiez votre connexion internet puis rechargez la page.");
      });
    }

    $$("[data-pay-go]", payBox).forEach(function (btn) {
      btn.addEventListener("click", function () {
        var method = btn.getAttribute("data-pay-go");
        var zone = $("input[name='zone']:checked", payBox);
        var label = btn.innerHTML;
        btn.disabled = true;
        btn.innerHTML = '<span class="spinner" aria-hidden="true"></span> Redirection vers le paiement sécurisé…';
        setPayStatus("", "");
        api("/api/payment", {
          method: "POST",
          headers: { "Content-Type": "application/json", "Accept": "application/json" },
          body: JSON.stringify({ action: method, t: token, currency: zone ? zone.value : "" })
        }).then(function (r) {
          if (r.ok && r.url) { window.location.href = r.url; return; }
          btn.disabled = false; btn.innerHTML = label;
          if (r.error === "expired") return payError("Ce lien de paiement a expiré", "Écrivez-nous : nous vous en adressons un nouveau.");
          setPayStatus("error", "Le service de paiement ne répond pas pour le moment. Réessayez dans quelques instants ou choisissez un autre moyen de paiement.");
        }).catch(function () {
          btn.disabled = false; btn.innerHTML = label;
          setPayStatus("error", "Connexion impossible. Vérifiez votre connexion internet puis réessayez.");
        });
      });
    });
  }

  /* Confirmation de paiement : statut relu chez le prestataire, nouvelles tentatives si en attente */
  var paidBox = $("[data-paid-box]");
  if (paidBox) {
    var m = params.get("m") === "mobile" ? "mobile" : "card";
    var pid = params.get("id") || "";
    var tries = 0;
    var title = $("[data-paid-title]"), lead = $("[data-paid-lead]"), mark = $("[data-paid-mark]"), wait = $("[data-paid-wait]");
    var end = function (kind, t, l) {
      wait.hidden = true;
      mark.hidden = false;
      mark.className = "success-mark" + (kind === "paid" ? "" : kind === "failed" ? " success-mark--fail" : " success-mark--warn");
      if (kind === "failed") mark.innerHTML = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true" focusable="false"><path d="M6 6l12 12M18 6L6 18"/></svg>';
      if (kind === "pending") mark.innerHTML = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>';
      title.textContent = t; lead.textContent = l;
      title.focus();
    };
    var check = function () {
      if (!pid) return end("pending", "Paiement en cours de traitement", "Si votre paiement a été validé, vous recevrez votre reçu par e-mail. Sinon, utilisez à nouveau le lien reçu par e-mail.");
      api("/api/payment?action=status&m=" + m + "&id=" + encodeURIComponent(pid)).then(function (r) {
        if (r.ok && r.status === "paid") {
          d.title = "Paiement confirmé — Academy 21 University";
          fill(d, "data-p", { ref: r.ref, name: ((r.prenom || "") + " " + (r.nom || "")).trim() || r.email, amount: r.amount, provider: m === "card" ? "Carte bancaire" : "Mobile Money (" + (r.provider || "") + ")", transaction: r.transaction });
          $("[data-paid-details]").hidden = false;
          return end("paid", "Merci, votre paiement est confirmé", "Vos frais d'étude de dossier sont réglés. Un reçu vous a été envoyé par e-mail ; notre équipe vous recontacte pour la suite de votre admission.");
        }
        if (r.ok && r.status === "failed") {
          return end("failed", "Le paiement n'a pas abouti", "Aucun montant n'a été débité. Vous pouvez réessayer depuis le lien reçu par e-mail.");
        }
        if (r.ok && tries < 8) { tries += 1; return setTimeout(check, 4000); }
        end("pending", "Paiement en cours de confirmation", "La confirmation peut prendre quelques minutes, notamment en Mobile Money. Vous recevrez votre reçu par e-mail dès sa validation.");
      }).catch(function () {
        end("pending", "Vérification impossible pour le moment", "Si votre paiement a été validé, vous recevrez votre reçu par e-mail.");
      });
    };
    check();
  }

  /* Espace école : création et envoi du lien de paiement */
  var feeForm = $("#fee-form");
  if (feeForm) {
    ["ref", "prenom", "nom", "email", "programme"].forEach(function (n) {
      var v = params.get(n);
      var el = feeForm.elements[n];
      if (!v || !el) return;
      if (el.tagName === "SELECT") { if (el.querySelector("option[value='" + v.replace(/[^a-z0-9-]/g, "") + "']")) el.value = v; }
      else el.value = v.slice(0, 160);
    });
    wireLiveValidation(feeForm);
    var linkBox = $("[data-link-box]");
    var linkOut = $("#pay-link-out");
    var batchBox = $("[data-batch-box]");
    var emailEl = feeForm.elements.email;
    var batchMode = function () {
      var n = splitEmails(emailEl.value).length;
      var multi = n > 1;
      $$("[data-single]", feeForm).forEach(function (b) { b.hidden = multi; });
      $("[data-batch-note]", feeForm).hidden = !multi;
      if (multi) $("[data-batch-text]", feeForm).textContent = "Envoi groupé : " + n + " adresses. Chaque candidat reçoit son propre e-mail et son lien personnel ; une référence est attribuée à chacun et l'école reçoit un récapitulatif.";
      $("[data-submit]", feeForm).lastChild.textContent = multi ? " Créer et envoyer les " + n + " liens" : " Créer et envoyer le lien";
      return n;
    };
    emailEl.addEventListener("input", batchMode);
    batchMode();
    var esc = function (t) { var x = d.createElement("span"); x.textContent = t; return x.innerHTML; };
    feeForm.addEventListener("submit", function (e) {
      e.preventDefault();
      if (!validate(feeForm, feeForm)) return;
      var payload = collect(feeForm);
      payload.send = feeForm.elements.send.checked ? "1" : "0";
      var multi = batchMode() > 1;
      var btn = $("[data-submit]", feeForm);
      busy(btn, true);
      setStatus(feeForm, "", "");
      linkBox.hidden = true; batchBox.hidden = true;
      api("/api/payment", {
        method: "POST",
        headers: { "Content-Type": "application/json", "Accept": "application/json" },
        body: JSON.stringify(payload)
      }).then(function (r) {
        busy(btn, false);
        var res = r.results || [];
        if (res.length > 1) {
          $("[data-batch-rows]").innerHTML = res.map(function (x) {
            return '<tr><td data-label="E-mail">' + esc(x.email) + '</td><td data-label="Référence">' + esc(x.ref) + '</td><td data-label="Statut">' + (x.sent ? "Envoyé" : x.error ? "Échec de l'envoi" : "Créé") +
              '</td><td data-label="Lien"><a href="' + esc(x.link) + '" target="_blank" rel="noopener">Ouvrir<span class="visually-hidden"> le lien de ' + esc(x.email) + "</span></a></td></tr>";
          }).join("");
          batchBox.hidden = false;
        } else if (r.link) { linkOut.value = r.link; linkBox.hidden = false; }
        if (r.ok) {
          var when = r.labelEur + " · " + r.labelFcfa + ", valable jusqu'au " + frDate(r.expires) + ".";
          setStatus(feeForm, "success", multi
            ? (r.sent ? r.sent + " liens envoyés, chacun à son destinataire. Montant : " + when : res.length + " liens créés (aucun e-mail envoyé).")
            : (r.sent ? "Lien envoyé à " + emailEl.value.trim() + " (copie à l'école). Montant : " + when : "Lien créé (aucun e-mail envoyé). Copiez-le ci-dessous pour le transmettre au candidat."));
          return;
        }
        var msg = {
          key: "Clé d'accès incorrecte.",
          not_configured: "Le paiement n'est pas encore configuré : renseignez ADMIN_KEY (12 caractères minimum) et PAYMENT_SECRET dans Vercel.",
          validation: "Champs à vérifier : " + (r.fields || []).join(", ") + ".",
          delivery: (r.failed && res.length > 1 ? r.failed + " e-mail(s) n'ont pas pu partir (voir le tableau)." : "Le lien a été créé mais l'e-mail n'a pas pu partir : copiez le lien ci-dessous.") + " Vérifiez la configuration des e-mails."
        }[r.error] || "Une erreur est survenue. Réessayez dans quelques instants.";
        setStatus(feeForm, "error", msg);
      }).catch(function () {
        busy(btn, false);
        setStatus(feeForm, "error", "Connexion impossible. Vérifiez votre connexion internet puis réessayez.");
      });
    });
    var copyBtn = $("[data-copy]");
    if (copyBtn) copyBtn.addEventListener("click", function () {
      linkOut.select();
      var done = function () { setStatus(feeForm, "success", "Lien copié dans le presse-papiers."); };
      if (navigator.clipboard) navigator.clipboard.writeText(linkOut.value).then(done, function () { d.execCommand("copy"); done(); });
      else { d.execCommand("copy"); done(); }
    });
  }
  })();

  (function () {
  /* ------------------------------------------------------------------
     Visionneuse de photos : zoom depuis la vignette (FLIP), galerie
  ------------------------------------------------------------------ */
  var zoomBtns = $$(".zoom-btn");
  if (zoomBtns.length && typeof HTMLDialogElement === "function") {
    var EASE = "cubic-bezier(.2,.7,.2,1)";
    var ico = function (p) { return '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false">' + p + "</svg>"; };
    var lb = d.createElement("dialog");
    lb.className = "lightbox";
    lb.setAttribute("aria-label", "Visionneuse de photos");
    lb.innerHTML =
      '<div class="lightbox__veil"></div>' +
      '<div class="lightbox__stage"><figure class="lightbox__figure">' +
      '<img class="lightbox__img" alt="">' +
      '<figcaption class="lightbox__caption"><span class="lightbox__rule" aria-hidden="true"></span><span class="lightbox__text"></span><small aria-live="polite"></small></figcaption>' +
      "</figure></div>" +
      '<button type="button" class="lightbox__btn lightbox__close" aria-label="Fermer la visionneuse">' + ico('<path d="M6 6l12 12M18 6L6 18"/>') + "</button>" +
      '<button type="button" class="lightbox__btn lightbox__prev" aria-label="Photo précédente">' + ico('<path d="M15 5l-7 7 7 7"/>') + "</button>" +
      '<button type="button" class="lightbox__btn lightbox__next" aria-label="Photo suivante">' + ico('<path d="M9 5l7 7-7 7"/>') + "</button>";
    d.body.appendChild(lb);

    var lbImg = $(".lightbox__img", lb), lbText = $(".lightbox__text", lb), lbCount = $("small", lb);
    var lbVeil = $(".lightbox__veil", lb), lbCap = $(".lightbox__caption", lb);
    var lbPrev = $(".lightbox__prev", lb), lbNext = $(".lightbox__next", lb), lbClose = $(".lightbox__close", lb);
    var lbList = [], lbIndex = 0, lbTrigger = null, lbBusy = false;

    var load = function (src) {
      lbImg.src = src;
      var p = lbImg.decode ? lbImg.decode() : new Promise(function (res) { if (lbImg.complete) res(); else lbImg.onload = res; });
      return p.catch(function () {}).then(function () {
        // Pas d'agrandissement au-delà de 125 % de la taille réelle (netteté)
        if (lbImg.naturalWidth) lbImg.style.maxWidth = "min(100%, " + Math.round(lbImg.naturalWidth * 1.25) + "px)";
      });
    };
    var fill = function () {
      var b = lbList[lbIndex];
      lbImg.alt = b.getAttribute("data-zoom-alt") || "";
      lbText.textContent = lbImg.alt;
      var many = lbList.length > 1;
      lbCount.textContent = many ? (lbIndex + 1) + " / " + lbList.length : "";
      lbCount.hidden = !many;
      lbPrev.hidden = lbNext.hidden = !many;
      return load(b.getAttribute("data-zoom"));
    };

    // Transformation qui superpose l'image agrandie à sa vignette (recadrage « cover » compris)
    var flip = function (btn) {
      var host = btn.parentElement || btn;
      var t = host.getBoundingClientRect(), f = lbImg.getBoundingClientRect();
      if (!t.width || !f.width || t.bottom < 0 || t.top > window.innerHeight) return null;
      var s = Math.max(t.width / f.width, t.height / f.height);
      var dx = (t.left + t.width / 2) - (f.left + f.width / 2);
      var dy = (t.top + t.height / 2) - (f.top + f.height / 2);
      var ix = Math.max(0, (f.width - t.width / s) / 2), iy = Math.max(0, (f.height - t.height / s) / 2);
      var r = parseFloat(getComputedStyle(host).borderTopLeftRadius) || 0;
      return {
        transform: "translate(" + dx + "px," + dy + "px) scale(" + s + ")",
        clipPath: "inset(" + iy + "px " + ix + "px round " + Math.min(r / s, f.width / 2) + "px)"
      };
    };
    var END = { transform: "none", clipPath: "inset(0px 0px round 14px)" };

    var open = function (btn) {
      if (lbBusy) return;
      var g = btn.getAttribute("data-zoom-group");
      lbList = g ? zoomBtns.filter(function (b) { return b.getAttribute("data-zoom-group") === g; }) : [btn];
      lbIndex = Math.max(0, lbList.indexOf(btn));
      lbTrigger = btn;
      lbBusy = true;
      fill().then(function () {
        d.body.classList.add("lightbox-open");
        lb.showModal();
        if (reduceMotion || !lbImg.animate) { lbBusy = false; return; }
        var from = flip(btn);
        var dur = 460;
        lbVeil.animate([{ opacity: 0 }, { opacity: 1 }], { duration: dur, easing: "ease-out" });
        $$(".lightbox__btn, .lightbox__caption", lb).forEach(function (el) {
          el.animate([{ opacity: 0 }, { opacity: 1 }], { duration: 300, delay: dur * .55, easing: "ease-out", fill: "backwards" });
        });
        var a = lbImg.animate(from ? [from, END] : [{ opacity: 0, transform: "scale(.96)" }, { opacity: 1, transform: "none" }],
          { duration: dur, easing: EASE });
        a.onfinish = a.oncancel = function () { lbBusy = false; };
      });
    };

    var close = function () {
      if (!lb.open || lbBusy) return;
      var finish = function () {
        lb.close();
        d.body.classList.remove("lightbox-open");
        lbBusy = false;
        if (lbTrigger) lbTrigger.focus({ preventScroll: true });
      };
      if (reduceMotion || !lbImg.animate) return finish();
      var to = flip(lbList[lbIndex]);
      lbBusy = true;
      var dur = 380;
      $$(".lightbox__btn, .lightbox__caption", lb).forEach(function (el) {
        el.animate([{ opacity: 1 }, { opacity: 0 }], { duration: 160, fill: "forwards" });
      });
      lbVeil.animate([{ opacity: 1 }, { opacity: 0 }], { duration: dur, easing: "ease-in", fill: "forwards" });
      var a = lbImg.animate(to ? [END, to] : [{ opacity: 1 }, { opacity: 0, transform: "scale(.96)" }],
        { duration: dur, easing: EASE, fill: "forwards" });
      a.onfinish = function () {
        finish();
        if (lb.getAnimations) lb.getAnimations({ subtree: true }).forEach(function (x) { x.cancel(); });
      };
    };

    var go = function (step) {
      if (lbBusy || lbList.length < 2) return;
      lbBusy = true;
      lbIndex = (lbIndex + step + lbList.length) % lbList.length;
      var shift = reduceMotion ? 0 : 24 * step;
      var fade = function (el, k) { return el.animate ? el.animate(k, { duration: 200, easing: "ease-in", fill: "forwards" }).finished : Promise.resolve(); };
      Promise.all([fade(lbImg, [{ opacity: 1, transform: "none" }, { opacity: 0, transform: "translateX(" + -shift + "px)" }]),
                   fade(lbCap, [{ opacity: 1 }, { opacity: 0 }])])
        .catch(function () {})
        .then(fill)
        .then(function () {
          lbImg.getAnimations && lbImg.getAnimations().forEach(function (x) { x.cancel(); });
          lbCap.getAnimations && lbCap.getAnimations().forEach(function (x) { x.cancel(); });
          if (lbImg.animate) {
            lbImg.animate([{ opacity: 0, transform: "translateX(" + shift + "px)" }, { opacity: 1, transform: "none" }], { duration: 320, easing: EASE });
            lbCap.animate([{ opacity: 0 }, { opacity: 1 }], { duration: 320, easing: "ease-out" });
          }
          lbBusy = false;
        });
    };

    zoomBtns.forEach(function (b) { b.addEventListener("click", function () { open(b); }); });
    lbClose.addEventListener("click", close);
    lbPrev.addEventListener("click", function () { go(-1); });
    lbNext.addEventListener("click", function () { go(1); });
    lb.addEventListener("cancel", function (e) { e.preventDefault(); close(); });
    lb.addEventListener("click", function (e) {
      if (e.target === lb || e.target.classList.contains("lightbox__veil") || e.target.classList.contains("lightbox__stage")) close();
    });
    lb.addEventListener("keydown", function (e) {
      if (e.key === "ArrowLeft") { e.preventDefault(); go(-1); }
      else if (e.key === "ArrowRight") { e.preventDefault(); go(1); }
    });
    // Balayage horizontal sur mobile
    var x0 = null;
    lb.addEventListener("touchstart", function (e) { x0 = e.touches[0].clientX; }, { passive: true });
    lb.addEventListener("touchend", function (e) {
      if (x0 === null) return;
      var dx = e.changedTouches[0].clientX - x0; x0 = null;
      if (Math.abs(dx) > 50) go(dx < 0 ? 1 : -1);
    }, { passive: true });
  } else {
    zoomBtns.forEach(function (b) { b.hidden = true; });
  }
  })();

  /* ------------------------------------------------------------------
     Apparition douce
  ------------------------------------------------------------------ */
  var reveals = $$(".reveal, .reveal-stagger");
  if (!reduceMotion && "IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add("is-visible"); io.unobserve(en.target); }
      });
    }, { rootMargin: "0px 0px -6% 0px" });
    reveals.forEach(function (el) { io.observe(el); });
  } else {
    reveals.forEach(function (el) { el.classList.add("is-visible"); });
  }

  $$("[data-year]").forEach(function (el) { el.textContent = new Date().getFullYear(); });
  root.classList.add("is-ready");
})();
