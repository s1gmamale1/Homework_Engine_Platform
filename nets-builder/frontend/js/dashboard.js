// frontend/js/dashboard.js
// NETS Builder dashboard logic: library grid, filters, create flow.

(function () {
  "use strict";

  const SUBJECT_LABELS = {
    "math-algebra": "Algebra",
    "geometriya-g7-11": "Geometriya",
    physics: "Fizika",
    biology: "Biologiya",
    "kimyo-g7-11": "Kimyo",
    english: "English",
    history: "Tarix",
  };

  const SUBJECT_ICONS = {
    "math-algebra": "∑",
    "geometriya-g7-11": "△",
    physics: "⚛",
    biology: "🧬",
    "kimyo-g7-11": "⚗",
    english: "Aa",
    history: "🏛",
  };

  const DEFAULT_FAMILY_COLORS = {
    "aniq-fanlar": "#007AFF",
    "tabiy-fanlar": "#34C759",
    "til-fanlar": "#AF52DE",
    "ijtimoiy-fanlar": "#FF9500",
  };

  const state = {
    subjects: [],
    families: { ...DEFAULT_FAMILY_COLORS },
    homeworks: [],
    filters: {
      search: "",
      subject: "all",
      status: "all",
      mode: "all",
    },
    loading: false,
  };

  const els = {};

  function $(id) {
    return document.getElementById(id);
  }

  function cacheElements() {
    Object.assign(els, {
      healthPill: $("health-pill"),
      healthLabel: $("health-label"),
      newHomeworkBtn: $("new-homework-btn"),
      emptyNewBtn: $("empty-new-btn"),
      refreshBtn: $("refresh-btn"),
      searchInput: $("search-input"),
      subjectFilter: $("subject-filter"),
      statusFilter: $("status-filter"),
      modeFilter: $("mode-filter"),
      loadingState: $("loading-state"),
      emptyState: $("empty-state"),
      homeworkGrid: $("homework-grid"),
      statTotal: $("stat-total"),
      statReady: $("stat-ready"),
      statDraft: $("stat-draft"),
      modal: $("create-modal"),
      form: $("create-form"),
      closeCreateModal: $("close-create-modal"),
      cancelCreate: $("cancel-create"),
      titleInput: $("homework-title"),
      subjectSelect: $("homework-subject"),
      gradeSelect: $("homework-grade"),
      modeSelect: $("homework-mode"),
      modeNote: $("mode-note"),
      submitCreate: $("submit-create"),
      toastRegion: $("toast-region"),
    });
  }

  function escapeHtml(value) {
    return String(value ?? "")
      .replaceAll("&", "&amp;")
      .replaceAll("<", "&lt;")
      .replaceAll(">", "&gt;")
      .replaceAll('"', "&quot;")
      .replaceAll("'", "&#039;");
  }

  function normalize(value) {
    return String(value ?? "").trim().toLowerCase();
  }

  function getSubject(subjectId) {
    return state.subjects.find((subject) => subject.id === subjectId) || null;
  }

  function getSubjectLabel(subjectId) {
    return SUBJECT_LABELS[subjectId] || subjectId || "Unknown";
  }

  function getSubjectIcon(subjectId) {
    return SUBJECT_ICONS[subjectId] || "N";
  }

  function getFamilyColor(family) {
    return state.families[family] || DEFAULT_FAMILY_COLORS[family] || DEFAULT_FAMILY_COLORS["aniq-fanlar"];
  }

  function titleCase(value) {
    const clean = String(value || "").replaceAll("_", " ").replaceAll("-", " ");
    return clean.charAt(0).toUpperCase() + clean.slice(1);
  }

  function formatDate(value) {
    if (!value) return "No date";

    const date = new Date(value);
    if (Number.isNaN(date.getTime())) return "No date";

    return new Intl.DateTimeFormat("uz-UZ", {
      year: "numeric",
      month: "short",
      day: "numeric",
      hour: "2-digit",
      minute: "2-digit",
    }).format(date);
  }

  function setLoading(isLoading) {
    state.loading = isLoading;
    els.loadingState.classList.toggle("hidden", !isLoading);
    els.refreshBtn.disabled = isLoading;
  }

  function setHealth(status, label) {
    const dot = els.healthPill.querySelector(".status-dot");
    dot.className = `status-dot ${status}`;
    els.healthLabel.textContent = label;
  }

  function showToast(title, message, type = "success") {
    const toast = document.createElement("div");
    toast.className = `toast ${type}`;
    toast.innerHTML = `
      <span class="status-dot ${type === "error" ? "error" : type === "warning" ? "warn" : "ok"}"></span>
      <div>
        <strong>${escapeHtml(title)}</strong>
        <p>${escapeHtml(message)}</p>
      </div>
    `;

    els.toastRegion.appendChild(toast);
    window.setTimeout(() => {
      toast.style.opacity = "0";
      toast.style.transform = "translateY(8px) scale(0.98)";
      window.setTimeout(() => toast.remove(), 180);
    }, 3200);
  }

  function renderStats() {
    const total = state.homeworks.length;
    const ready = state.homeworks.filter((item) => item.status === "ready").length;
    const drafts = state.homeworks.filter((item) => item.status === "draft").length;

    els.statTotal.textContent = total;
    els.statReady.textContent = ready;
    els.statDraft.textContent = drafts;
  }

  function renderSubjectOptions() {
    const filterCurrent = els.subjectFilter.value || "all";
    const createCurrent = els.subjectSelect.value || "";

    els.subjectFilter.innerHTML = '<option value="all">All subjects</option>';
    els.subjectSelect.innerHTML = '<option value="" disabled selected>Select subject</option>';

    for (const subject of state.subjects) {
      const label = getSubjectLabel(subject.id);

      els.subjectFilter.insertAdjacentHTML(
        "beforeend",
        `<option value="${escapeHtml(subject.id)}">${escapeHtml(label)}</option>`
      );

      els.subjectSelect.insertAdjacentHTML(
        "beforeend",
        `<option value="${escapeHtml(subject.id)}">${escapeHtml(label)}</option>`
      );
    }

    els.subjectFilter.value = [...els.subjectFilter.options].some((option) => option.value === filterCurrent)
      ? filterCurrent
      : "all";

    els.subjectSelect.value = [...els.subjectSelect.options].some((option) => option.value === createCurrent)
      ? createCurrent
      : "";
  }

  function renderGradeOptions(subjectId) {
    const subject = getSubject(subjectId);
    els.gradeSelect.innerHTML = '<option value="" disabled selected>Select grade</option>';
    els.gradeSelect.disabled = !subject;

    if (!subject) return;

    for (const grade of subject.grades || []) {
      els.gradeSelect.insertAdjacentHTML("beforeend", `<option value="${grade}">${grade}-sinf</option>`);
    }
  }

  function applyModeRules(subjectId) {
    const subject = getSubject(subjectId);

    if (!subject) {
      els.modeSelect.disabled = false;
      els.modeSelect.value = "easy";
      els.modeNote.textContent = "Choose a subject to see available grades and mode rules.";
      return;
    }

    if (subject.always_hard) {
      els.modeSelect.value = "hard";
      els.modeSelect.disabled = true;
      els.modeNote.textContent = `${getSubjectLabel(subject.id)} is locked to Hard mode by contract.`;
      return;
    }

    els.modeSelect.disabled = false;
    els.modeNote.textContent = `${getSubjectLabel(subject.id)} supports Easy and Hard modes.`;
  }

  function getFilteredHomeworks() {
    const q = normalize(state.filters.search);

    return state.homeworks.filter((homework) => {
      const title = normalize(homework.title);
      const id = normalize(homework.id);
      const subjectId = normalize(homework.subject);
      const subjectLabel = normalize(getSubjectLabel(homework.subject));

      const matchesSearch = !q || title.includes(q) || id.includes(q) || subjectId.includes(q) || subjectLabel.includes(q);
      const matchesSubject = state.filters.subject === "all" || homework.subject === state.filters.subject;
      const matchesStatus = state.filters.status === "all" || homework.status === state.filters.status;
      const matchesMode = state.filters.mode === "all" || homework.mode === state.filters.mode;

      return matchesSearch && matchesSubject && matchesStatus && matchesMode;
    });
  }

  function openBuilder(id) {
    window.location.href = `/builder.html?id=${encodeURIComponent(id)}`;
  }

  function renderHomeworkCard(homework) {
    const familyColor = getFamilyColor(homework.family);
    const subjectLabel = getSubjectLabel(homework.subject);
    const subjectIcon = getSubjectIcon(homework.subject);
    const status = homework.status || "draft";
    const mode = homework.mode || "easy";

    return `
      <article class="homework-card glass-card" style="--family-color: ${escapeHtml(familyColor)}" data-id="${escapeHtml(homework.id)}">
        <div class="homework-card-top">
          <div class="subject-icon" aria-hidden="true">${escapeHtml(subjectIcon)}</div>
          <div class="card-menu">
            <button class="icon-btn js-delete" type="button" title="Delete homework" aria-label="Delete ${escapeHtml(homework.title)}">×</button>
          </div>
        </div>

        <div>
          <h3 class="homework-title">${escapeHtml(homework.title || "Untitled homework")}</h3>
        </div>

        <div class="homework-meta">
          <span>${escapeHtml(subjectLabel)} · ${escapeHtml(homework.grade)}-sinf</span>
          <span>${escapeHtml(homework.id || "No ID")}</span>
          <span>Updated ${escapeHtml(formatDate(homework.updated_at || homework.created_at))}</span>
        </div>

        <div class="pill-row">
          <span class="status-pill" data-status="${escapeHtml(status)}">
            <span class="status-dot ${escapeHtml(status)}"></span>
            ${escapeHtml(titleCase(status))}
          </span>
          <span class="mode-pill">${escapeHtml(titleCase(mode))}</span>
          <span class="grade-pill">Grade ${escapeHtml(homework.grade)}</span>
        </div>

        <div class="card-actions">
          <button class="btn btn-primary js-open" type="button">Open builder</button>
          <a class="btn btn-ghost" href="${escapeHtml(API.getPreviewUrl(homework.id))}" target="_blank" rel="noreferrer">Preview</a>
        </div>
      </article>
    `;
  }

  function renderHomeworks() {
    const filtered = getFilteredHomeworks();
    renderStats();

    els.homeworkGrid.innerHTML = filtered.map(renderHomeworkCard).join("");

    const hasAny = state.homeworks.length > 0;
    const hasFiltered = filtered.length > 0;

    els.emptyState.classList.toggle("hidden", state.loading || hasFiltered);
    els.homeworkGrid.classList.toggle("hidden", state.loading || !hasFiltered);

    if (!hasAny && !state.loading) {
      els.emptyState.querySelector("h3").textContent = "No homework yet";
      els.emptyState.querySelector("p").textContent = "Create your first NETS homework to begin the builder flow.";
    } else if (hasAny && !hasFiltered && !state.loading) {
      els.emptyState.querySelector("h3").textContent = "No matching homework";
      els.emptyState.querySelector("p").textContent = "Try clearing search or filters.";
    }
  }

  async function loadHealth() {
    try {
      const health = await API.getHealth();
      const geminiText = health.gemini ? "Gemini ready" : "Gemini off";
      setHealth(health.status === "ok" ? "ok" : "warn", `API ok · ${geminiText}`);
    } catch (error) {
      setHealth("error", "API offline");
    }
  }

  async function loadSubjects() {
    const payload = await API.getSubjects();
    state.subjects = Array.isArray(payload.subjects) ? payload.subjects : [];
    state.families = { ...DEFAULT_FAMILY_COLORS, ...(payload.families || {}) };
    renderSubjectOptions();
  }

  async function loadHomeworks() {
    setLoading(true);

    try {
      state.homeworks = await API.listHomeworks();
      if (!Array.isArray(state.homeworks)) state.homeworks = [];
      renderHomeworks();
    } catch (error) {
      showToast("Could not load library", error.message, "error");
      state.homeworks = [];
      renderHomeworks();
    } finally {
      setLoading(false);
      renderHomeworks();
    }
  }

  function openCreateModal() {
    els.form.reset();
    els.gradeSelect.innerHTML = '<option value="" disabled selected>Select grade</option>';
    els.gradeSelect.disabled = true;
    applyModeRules("");

    if (typeof els.modal.showModal === "function") {
      els.modal.showModal();
    } else {
      els.modal.setAttribute("open", "");
    }

    window.setTimeout(() => els.titleInput.focus(), 40);
  }

  function closeCreateModal() {
    if (typeof els.modal.close === "function") {
      els.modal.close();
    } else {
      els.modal.removeAttribute("open");
    }
  }

  async function handleCreate(event) {
    event.preventDefault();

    const title = els.titleInput.value.trim();
    const subject = els.subjectSelect.value;
    const grade = Number(els.gradeSelect.value);
    const mode = els.modeSelect.value;

    if (!title || !subject || !grade || !mode) {
      showToast("Missing fields", "Fill title, subject, grade, and mode.", "warning");
      return;
    }

    els.submitCreate.disabled = true;
    els.submitCreate.textContent = "Creating...";

    try {
      const homework = await API.createHomework({ title, subject, grade, mode });
      showToast("Homework created", "Opening builder now.", "success");
      closeCreateModal();
      openBuilder(homework.id);
    } catch (error) {
      showToast("Could not create homework", error.message, "error");
    } finally {
      els.submitCreate.disabled = false;
      els.submitCreate.textContent = "Create and open";
    }
  }

  async function handleDelete(homeworkId) {
    const homework = state.homeworks.find((item) => item.id === homeworkId);
    const title = homework?.title || homeworkId;

    const confirmed = window.confirm(`Delete "${title}"? This cannot be undone.`);
    if (!confirmed) return;

    try {
      await API.deleteHomework(homeworkId);
      state.homeworks = state.homeworks.filter((item) => item.id !== homeworkId);
      renderHomeworks();
      showToast("Deleted", "Homework removed from library.", "success");
    } catch (error) {
      showToast("Could not delete", error.message, "error");
    }
  }

  function bindEvents() {
    els.newHomeworkBtn.addEventListener("click", openCreateModal);
    els.emptyNewBtn.addEventListener("click", openCreateModal);
    els.closeCreateModal.addEventListener("click", closeCreateModal);
    els.cancelCreate.addEventListener("click", closeCreateModal);
    els.refreshBtn.addEventListener("click", loadHomeworks);
    els.form.addEventListener("submit", handleCreate);

    els.modal.addEventListener("click", (event) => {
      if (event.target === els.modal) closeCreateModal();
    });

    els.subjectSelect.addEventListener("change", () => {
      renderGradeOptions(els.subjectSelect.value);
      applyModeRules(els.subjectSelect.value);
    });

    els.searchInput.addEventListener("input", () => {
      state.filters.search = els.searchInput.value;
      renderHomeworks();
    });

    els.subjectFilter.addEventListener("change", () => {
      state.filters.subject = els.subjectFilter.value;
      renderHomeworks();
    });

    els.statusFilter.addEventListener("change", () => {
      state.filters.status = els.statusFilter.value;
      renderHomeworks();
    });

    els.modeFilter.addEventListener("change", () => {
      state.filters.mode = els.modeFilter.value;
      renderHomeworks();
    });

    els.homeworkGrid.addEventListener("click", (event) => {
      const card = event.target.closest(".homework-card");
      if (!card) return;

      const id = card.dataset.id;

      if (event.target.closest(".js-delete")) {
        handleDelete(id);
        return;
      }

      if (event.target.closest(".js-open")) {
        openBuilder(id);
      }
    });
  }

  async function init() {
    cacheElements();
    bindEvents();
    setLoading(true);

    await Promise.allSettled([loadHealth(), loadSubjects()]);
    await loadHomeworks();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
