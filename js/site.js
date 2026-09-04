(function () {
  const header = document.querySelector(".site-header");
  const toggle = document.querySelector(".menu-toggle");
  const nav = document.querySelector(".nav-wrap");
  const dropdown = document.querySelector("[data-dropdown]");
  const dropBtn = dropdown && dropdown.querySelector("button");

  function onScroll() {
    if (!header) return;
    header.classList.toggle("is-solid", window.scrollY > 12);
  }
  onScroll();
  window.addEventListener("scroll", onScroll, { passive: true });

  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      const open = nav.classList.toggle("is-open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
  }

  if (dropdown && dropBtn) {
    dropBtn.addEventListener("click", function (e) {
      e.preventDefault();
      const open = dropdown.classList.toggle("is-open");
      dropBtn.setAttribute("aria-expanded", open ? "true" : "false");
    });
    document.addEventListener("click", function (e) {
      if (!dropdown.contains(e.target)) {
        dropdown.classList.remove("is-open");
        dropBtn.setAttribute("aria-expanded", "false");
      }
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape") {
        dropdown.classList.remove("is-open");
        dropBtn.setAttribute("aria-expanded", "false");
        if (nav) nav.classList.remove("is-open");
      }
    });
  }

  document.querySelectorAll("[data-ba]").forEach(function (wrap) {
    const range = wrap.querySelector(".ba-range");
    const after = wrap.querySelector(".ba-after");
    const handle = wrap.querySelector(".ba-handle");
    if (!range || !after || !handle) return;
    function set(val) {
      const pct = Number(val);
      after.style.clipPath = "inset(0 " + (100 - pct) + "% 0 0)";
      handle.style.left = pct + "%";
    }
    range.addEventListener("input", function () { set(range.value); });
    set(range.value || 50);
  });

  const items = Array.from(document.querySelectorAll("[data-lightbox]"));
  if (items.length) {
    const box = document.createElement("div");
    box.className = "lightbox";
    box.setAttribute("role", "dialog");
    box.setAttribute("aria-modal", "true");
    box.setAttribute("aria-label", "Image viewer");
    box.innerHTML =
      '<button class="lightbox-close" type="button" aria-label="Close">×</button>' +
      '<button class="lightbox-btn prev" type="button" aria-label="Previous">‹</button>' +
      '<img alt="">' +
      '<button class="lightbox-btn next" type="button" aria-label="Next">›</button>' +
      '<p class="lightbox-caption"></p>';
    document.body.appendChild(box);
    const img = box.querySelector("img");
    const cap = box.querySelector(".lightbox-caption");
    let index = 0;

    function show(i) {
      index = (i + items.length) % items.length;
      const a = items[index];
      img.src = a.getAttribute("href");
      img.alt = a.getAttribute("data-alt") || a.querySelector("img")?.alt || "";
      cap.textContent = a.getAttribute("data-caption") || img.alt;
      box.classList.add("is-open");
      box.querySelector(".lightbox-close").focus();
    }
    function close() {
      box.classList.remove("is-open");
      img.src = "";
    }

    items.forEach(function (a, i) {
      a.addEventListener("click", function (e) {
        e.preventDefault();
        show(i);
      });
    });
    box.querySelector(".lightbox-close").addEventListener("click", close);
    box.querySelector(".prev").addEventListener("click", function () { show(index - 1); });
    box.querySelector(".next").addEventListener("click", function () { show(index + 1); });
    box.addEventListener("click", function (e) { if (e.target === box) close(); });
    document.addEventListener("keydown", function (e) {
      if (!box.classList.contains("is-open")) return;
      if (e.key === "Escape") close();
      if (e.key === "ArrowLeft") show(index - 1);
      if (e.key === "ArrowRight") show(index + 1);
    });
  }

  const form = document.getElementById("consult-form");
  if (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      const fields = {
        name: form.querySelector("#name"),
        email: form.querySelector("#email"),
        phone: form.querySelector("#phone"),
        piece: form.querySelector("#piece"),
        message: form.querySelector("#message")
      };
      let ok = true;
      Object.keys(fields).forEach(function (key) {
        const el = fields[key];
        const wrap = el.closest(".field");
        const empty = !el.value.trim();
        const badEmail = key === "email" && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(el.value.trim());
        const invalid = empty || badEmail;
        wrap.classList.toggle("is-invalid", invalid);
        if (invalid) ok = false;
      });
      if (!ok) return;
      const subject = "Consultation request — " + fields.piece.value.trim();
      const body = [
        "Name: " + fields.name.value.trim(),
        "Email: " + fields.email.value.trim(),
        "Phone: " + fields.phone.value.trim(),
        "Piece / service: " + fields.piece.value.trim(),
        "",
        fields.message.value.trim(),
        "",
        "(I will attach photographs of the piece in a follow-up email.)"
      ].join("\n");
      window.location.href =
        "mailto:nikteply@gmail.com?subject=" +
        encodeURIComponent(subject) +
        "&body=" +
        encodeURIComponent(body);
    });
  }
})();
