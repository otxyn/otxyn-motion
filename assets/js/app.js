/* Otxyn Motion site logic — reads the generated data bundle (window.OTXYN_DATA).
   When served over http(s), re-checks research/candidates.json for freshness;
   under file:// the pre-generated bundle is used as-is. No frameworks. */

(function () {
  "use strict";

  var DATA = window.OTXYN_DATA;
  if (!DATA || !DATA.candidates) {
    document.body.insertAdjacentHTML(
      "afterbegin",
      '<div style="padding:12px 20px;border-bottom:1px solid #c9cdce;font-size:14px">' +
      "Data bundle missing — run <code>python scripts/gen_website_data.py</code> in the repo root.</div>"
    );
    return;
  }

  var CATS = DATA.categories;
  var state = { q: "", cat: "all", sort: "score" };

  /* ---------- hero stats ---------- */
  var statsEl = document.getElementById("stats");
  var c = DATA.counts;
  var stats = [
    [c.candidates, "research candidates"],
    [c.shortlisted, "shortlisted"],
    [c.browser_inspected, "browser inspected"],
    [c.previewed, "with previews"],
    [c.entries, "library entries · all planned"],
    [c.fonts_verified, "OFL-verified fonts"],
  ];
  statsEl.innerHTML = stats
    .map(function (s) {
      return "<div class='stat'><b>" + s[0] + "</b><span>" + s[1] + "</span></div>";
    })
    .join("");
  document.getElementById("lede").textContent = DATA.counts.implemented_entries
    ? "A research archive feeding a reference library of web motion graphics — every technique recorded with verified links, inspection evidence, licence findings and measured performance notes."
    : "A research archive feeding a curated library catalogue of web motion graphics: every technique recorded with verified links, inspection evidence and licence findings. All 40 library entries are planned — the catalogue documents intent, not shipped demos.";

  /* ---------- research collection ---------- */
  var cardsEl = document.getElementById("cards");
  var countLine = document.getElementById("count-line");
  var emptyEl = document.getElementById("empty");
  var qInput = document.getElementById("q");
  var sortEl = document.getElementById("sort");
  var chipsEl = document.getElementById("cat-chips");

  chipsEl.innerHTML =
    chip("all", "All categories", true) +
    CATS.map(function (cat) { return chip(cat, catLabel(cat), false); }).join("");

  function catLabel(cat) {
    var d = DATA.per_category.filter(function (p) { return p.category === cat; })[0];
    var n = d ? d.candidates : "";
    return cat === "3d-shaders" ? "3D & shaders" : cat.charAt(0).toUpperCase() + cat.slice(1);
  }
  function chip(val, label, pressed) {
    return "<button class='chip' type='button' data-cat='" + val + "' aria-pressed='" + pressed + "'>" + label + "</button>";
  }
  chipsEl.addEventListener("click", function (ev) {
    var btn = ev.target.closest(".chip");
    if (!btn) return;
    state.cat = btn.dataset.cat;
    chipsEl.querySelectorAll(".chip").forEach(function (b) {
      b.setAttribute("aria-pressed", String(b === btn));
    });
    render();
  });

  qInput.addEventListener("input", function () {
    state.q = qInput.value.trim().toLowerCase();
    render();
  });
  sortEl.addEventListener("change", function () {
    state.sort = sortEl.value;
    render();
  });

  function hay(t) { return (t || "").toLowerCase(); }

  function filtered() {
    var out = DATA.candidates.filter(function (x) {
      if (state.cat !== "all" && x.category !== state.cat) return false;
      if (!state.q) return true;
      return [x.name, x.description, x.creator, x.subcategory, x.notes,
              x.technologies, x.techniques, x.rendering, x.id]
        .some(function (f) { return hay(Array.isArray(f) ? f.join(" ") : f).includes(state.q); });
    });
    if (state.sort === "name") out.sort(function (a, b) { return a.name.localeCompare(b.name); });
    else if (state.sort === "depth")
      out.sort(function (a, b) { return depth(b) - depth(a) || (b.score || -1) - (a.score || -1); });
    else out.sort(function (a, b) { return (b.score || -1) - (a.score || -1); });
    return out;

    function depth(x) { return (x.browser_inspected ? 2 : 0) + (x.source_inspected ? 1 : 0); }
  }

  function pill(x) {
    var bits = "";
    if (x.status === "shortlisted") bits += "<span class='pill pill-short'>shortlisted</span>";
    if (x.browser_inspected) bits += "<span class='pill pill-ok'>browser seen</span>";
    else if (x.source_inspected) bits += "<span class='pill pill-ok'>source read</span>";
    if (x.licence && x.licence !== "unverified")
      bits += "<span class='pill pill-verified'>" + esc(x.licence) + "</span>";
    else bits += "<span class='pill pill-warn'>licence unverified</span>";
    return bits;
  }

  function render() {
    var rows = filtered();
    countLine.textContent =
      rows.length + " of " + DATA.counts.candidates + " references" +
      (state.cat === "all" ? " · all categories" : " · " + state.cat) +
      " · sorted by " + (state.sort === "score" ? "score" : state.sort === "name" ? "name" : "inspection depth");
    emptyEl.hidden = rows.length > 0;
    cardsEl.innerHTML = rows
      .map(function (x) {
        var img = x.preview_desktop
          ? "<img class='thumb' loading='lazy' alt='' src='research/" + esc(x.preview_desktop) + "'>"
          : "";
        return (
          "<button class='card' type='button' data-id='" + x.id + "'>" +
          "<div class='card-top'><span class='card-cat'>" + esc(x.category) +
          (x.subcategory ? " / " + esc(x.subcategory) : "") + "</span>" +
          "<span class='card-score'>" + (x.score != null ? esc(String(x.score)) : "—") + "</span></div>" +
          img +
          "<p class='card-name'>" + esc(x.name) + "</p>" +
          "<p class='card-desc'>" + esc(x.description) + "</p>" +
          "<div class='card-meta'>" + pill(x) + "</div>" +
          "</button>"
        );
      })
      .join("");
  }

  cardsEl.addEventListener("click", function (ev) {
    var btn = ev.target.closest(".card");
    if (btn) openDetail(btn.dataset.id);
  });

  render();  /* initial paint of the research collection */

  /* ---------- detail dialog ---------- */
  var dlg = document.getElementById("detail");
  var body = document.getElementById("detail-body");

  function fact(term, val) {
    return "<div class='d-row'><dt>" + term + "</dt><dd>" + val + "</dd></div>";
  }
  function linkify(u, label) {
    return u ? "<a href='" + esc(u) + "' target='_blank' rel='noopener noreferrer'>" + (label || esc(u)) + "</a>" : "—";
  }

  function openDetail(id) {
    var x = DATA.candidates.filter(function (v) { return v.id === id; })[0];
    if (!x) return;
    var prev = x.preview_desktop
      ? "<img class='d-img' alt='Preview screenshot of " + esc(x.name) + "' src='research/" + esc(x.preview_desktop) + "'>"
      : "";
    body.innerHTML =
      "<p class='d-kicker'>" + esc(x.category) + (x.subcategory ? " / " + esc(x.subcategory) : "") + "</p>" +
      "<h3 id='detail-title'>" + esc(x.name) + "</h3>" +
      "<p class='d-desc'>" + esc(x.description) + "</p>" +
      prev +
      "<dl class='d-facts'>" +
      fact("Creator", esc(x.creator || "—")) +
      fact("Candidate id", "<code>" + esc(x.id) + "</code>") +
      fact("Status", esc(x.status) + (x.status === "shortlisted" ? " — passed quality + licence gauntlet" : " — not shortlisted")) +
      fact("Rendering", esc(x.rendering || "—")) +
      fact("Complexity", esc(x.complexity || "—")) +
      fact("Technologies", esc((x.technologies || []).join(", ") || "—")) +
      fact("Techniques", esc((x.techniques || []).join(", ") || "—")) +
      fact("Interaction", esc((x.interaction || []).join(", ") || "—")) +
      fact("Score", x.score != null ? esc(String(x.score)) + " / 10 (weighted)" : "unscored") +
      fact("Inspection",
        (x.browser_inspected ? "browser inspected" : x.source_inspected ? "source read" : "not inspected deeply") +
        " · demo: " + linkify(x.demo_url) + " · source: " + linkify(x.source_url) + " · repo: " + linkify(x.repository_url)) +
      fact("Licence", esc(x.licence) + (x.licence_url
        ? " · " + linkify(x.licence_url, "evidence") : "") + (x.licence === "unverified"
        ? " — <strong>blocked from library adoption until resolved</strong>" : "")) +
      "</dl>" +
      (x.notes ? "<div class='d-notes'><strong>Research notes.</strong> " + esc(x.notes) + "</div>" : "") +
      "<p style='font-size:12.5px;color:#83898e;margin:14px 0 0'>Full record: <code>research/candidates.json</code> → <code>" + esc(x.id) + "</code></p>";
    dlg.showModal();
  }
  document.querySelector(".detail-close").addEventListener("click", function () { dlg.close(); });
  dlg.addEventListener("click", function (ev) {
    if (ev.target === dlg) dlg.close(); /* backdrop click */
  });

  /* ---------- library section ---------- */
  var groupsEl = document.getElementById("library-groups");
  var authorities = DATA.library.authorities || {};

  groupsEl.innerHTML = DATA.per_category
    .filter(function (p) { return p.entries > 0; })
    .map(function (p) {
      var entries = DATA.library.entries.filter(function (e) { return e.category === p.category; });
      return (
        "<div class='lib-group'><div class='lib-cat'><h3>" + esc(catLabel(p.category)) +
        "</h3><span class='lib-count'>" + entries.length + " entries · " + p.candidates +
        " researched references</span></div><div class='lib-grid'>" +
        entries.map(libCard).join("") +
        "</div></div>"
      );
    })
    .join("");

  function libCard(e) {
    return (
      "<div class='lib-card'><div class='lib-card-top'><span class='lib-id'>" + esc(e.id) +
      "</span><span class='badge badge-planned'>" + esc(e.status) + "</span></div>" +
      "<p class='lib-name'>" + esc(e.name) + "</p>" +
      "<p class='lib-sub'>" + esc(e.description || "") + "</p>" +
      "<div class='lib-foot'>" +
      "<span class='badge badge-" + esc(e.authority) + "'>" + esc(e.authority) + "</span>" +
      "<span class='pill " + (e.verified ? "pill-verified" : "pill-warn") + "'>" +
      esc(e.licence) + (e.verified ? "" : " · unverified") + "</span>" +
      (e.reference_path
        ? "<a class='more' href='" + esc(e.reference_path) + "'>reference →</a>"
        : "") +
      "</div></div>"
    );
  }

  document.getElementById("reserve-count").textContent =
    String((DATA.library.reserves || []).length);
  document.getElementById("reserve-list").textContent =
    (DATA.library.reserves || []).slice(0, 5)
      .map(function (r) { return esc(r.research_candidate || r.name || "?"); })
      .join(", ") + (DATA.library.reserves && DATA.library.reserves.length > 5 ? ", …" : "");

  /* legend counts for authorities */
  document.getElementById("library-legend").insertAdjacentHTML(
    "beforeend",
    " <span class='dot'>·</span> " +
    [c.authorities && c.authorities.adapt ? "<span class='badge badge-adapt'>adapt " + c.authorities.adapt + "</span>" : "",
     c.authorities && c.authorities.reinvent ? "<span class='badge badge-reinvent'>reinvent " + c.authorities.reinvent + "</span>" : "",
     c.authorities && c.authorities.pattern ? "<span class='badge badge-pattern'>pattern " + c.authorities.pattern + "</span>" : ""]
      .filter(Boolean).join(" ")
  );

  function esc(s) {
    return String(s == null ? "" : s)
      .replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;").replace(/'/g, "&#39;");
  }

  /* optional: refresh data when served over http (dev convenience) */
  if (location.protocol.startsWith("http")) {
    fetch("research/candidates.json").then(function (r) { return r.ok ? r.json() : null; }).then(function (fresh) {
      if (fresh && fresh.length === DATA.candidates.length) return; /* unchanged */
      if (fresh) { /* length changed — tell the visitor to regenerate */
        console.warn("[otxyn] candidates.json now holds %d records but the page bundle has %d — regenerate with scripts/gen_website_data.py", fresh.length, DATA.candidates.length);
      }
    }).catch(function () { /* file served but fetch blocked — ignore */ });
  }
})();
